import torch
import torchvision.transforms as T
from PIL import Image
import torchvision.transforms.functional as F


def pic_to_tensors(image, ascii_w=50, tw=10):
    image = Image.open(image)
    transform = T.Compose([T.PILToTensor()])
    img_t = transform(image)
    tensor_resized = F.resize(img_t, [tw * ascii_w * 2, tw * ascii_w])
    tlist = []
    for long_tensors in torch.tensor_split(tensor_resized, ascii_w, dim=1):
        tensors_in_row = torch.tensor_split(long_tensors, ascii_w, dim=2)
        tlist.extend(tensors_in_row)
    return tlist
