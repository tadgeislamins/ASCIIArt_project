import torch
import torchvision.transforms as T
from PIL import Image
import torchvision.transforms.functional as F


def pic_to_tensors(image, ascii_w=50, tw=10, tratio=2):
    image = Image.open(image)
    size = F.get_image_size(image)
    ratio = size[0] / size[1] if size[0] > size[1] else size[1] / size[0] # (отношение сторон)
    ascii_h = tw * ascii_w * ratio
    transform = T.Compose([T.ToTensor()])
    img_t = transform(image)
    t_resized = F.resize(img_t, (ascii_h * (tw * tratio), tw * ascii_w))
    print(ascii_h)
    # нормализуем всю картинку, отдельно для каждого измерения
    mean, std = t_resized.mean([1, 2]), t_resized.std([1, 2])
    normalize = T.Compose([T.Normalize(mean, std)])
    t_normalized = normalize(t_resized)

    tlist = []
    for long_tensors in torch.tensor_split(t_normalized, ascii_h, dim=1):
        tlist.append(torch.stack(torch.tensor_split(long_tensors, ascii_w, dim=2)))
    stacked = torch.stack(tlist)
    # return stacked


pic_to_tensors('fawn.jpeg')
