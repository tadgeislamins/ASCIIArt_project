from char_tensors import char_t
from img_tensor import pic_to_tensors
import pandas as pd


def match(val, list):
    if len(list) == 1:
        return(list.keys()[0])
    else:
        half = len(list) // 2
        if val < list[half]:
            return match(val, list[:half])
        else:
            return match(val, list[half:])


def gen_shading(img):
    chlist = [chr(i) for i in range(33, 127)]

    means = pd.Series([float(char_t(ch).mean()) for ch in chlist], index=chlist)
    means = ((means - means.mean()) / means.std()).sort_values()

    img_t = pic_to_tensors(img).mean([2, 3, 4])
    char_amp = max(means) - min(means)
    img_amp = img_t.max() - img_t.min()
    img_t = img_t * char_amp / img_amp
    print(means.median(), img_t.median())

    art = ''
    for row in img_t:
        for cell in row:
            t_mean = float(cell)
            art += match(t_mean, means)
        art += '\n'

    return art
