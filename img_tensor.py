import torch
import torchvision.transforms as T
from PIL import Image
import torchvision.transforms.functional as F


def resize(image, w, th):
    size = F.get_image_size(image)
    h = int(w * size[1] / size[0] // th * th)
    transform = T.Compose([T.ToTensor()])
    return F.resize(transform(image), [h, w]), h // th


def pic_to_tensors(image, ascii_w=50, tw=10, tratio=2):
    image = Image.open(image)
    print(type(image))
    t_resized, ascii_h = resize(image, tw * ascii_w, tw * tratio)

    # НЕ нормализуем всю картинку, отдельно для каждого измерения
    # mean, std = t_resized.mean([1, 2]), t_resized.std([1, 2])
    # normalize = T.Compose([T.Normalize(mean, std)])
    # t_normalized = normalize(t_resized)

    tlist = []
    for long_tensors in torch.tensor_split(t_resized, ascii_h, dim=1):
        tlist.append(torch.stack(torch.tensor_split(long_tensors, ascii_w, dim=2)))
    stacked = torch.stack(tlist)
    return stacked
