from char_tensors import char_t
from img_tensor import pic_to_tensors
import pandas as pd
from math import pi


def match(val, list):
    if len(list) == 1:
        return(list.keys()[0])
    else:
        half = len(list) // 2
        if val < list[half]:
            return match(val, list[:half])
        else:
            return match(val, list[half:])


def gen_shading(img, chlist, width=50):

    tones = pd.Series([float(char_t(ch).mean()) for ch in chlist], index=list(chlist))
    tones = ((tones - tones.min()) / (tones.max() - tones.min())).sort_values()

    img_t = pic_to_tensors(img, ascii_w=width).mean([2, 3, 4])
    img_t = (img_t - img_t.min()) / (img_t.max() - img_t.min()) * pi / 2
    img_t = img_t.sin()
    img_t = img_t / img_t.max()

    print(img_t.min(), img_t.max(), tones.min(), tones.max())

    art = ''
    for row in img_t:
        for cell in row:
            t_mean = float(cell)
            art += match(t_mean, tones)
        art += '\n'

    return art
