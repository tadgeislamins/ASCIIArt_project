import torch
import torchvision.transforms as T
from PIL import Image
import torchvision.transforms.functional as F


def pic_to_tensors(image, ascii_w=50, tw=10, tratio=2):
    image = Image.open(image)
    transform = T.Compose([T.PILToTensor()])
    img_t = transform(image)
    tensor_resized = F.resize(img_t, [tw * ascii_w * tratio, tw * ascii_w])
    # for long_tensors in torch.tensor_split(tensor_resized, ascii_w, dim=1):
    #     t = torch.stack(torch.tensor_split(long_tensors, ascii_w, dim=2), 0)
    for long_tensors in torch.tensor_split(tensor_resized, ascii_w, dim=1):
        stacked = torch.stack(torch.tensor_split(long_tensors, ascii_w, dim=2))
    #stacked = torch.stack([torch.stack(torch.tensor_split(long_tensors,
    # ascii_w, dim=2)) for long_tensors in torch.tensor_split(tensor_resized, ascii_w, dim=1)])
    return stacked


print(pic_to_tensors('fawn.jpeg').size())

# Torch.size([строка, столбец, канал1, канал2, канал3])
