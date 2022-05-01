import torch
import torchvision.transforms as T
from PIL import Image
import torchvision.transforms.functional as F


def pic_to_tensors(image, ascii_w=50, tw=10, tratio=2):
    image = Image.open(image)
    ascii_h = F.get_image_size(image)[1] // (tw * tratio)
    transform = T.Compose([T.ToTensor()])
    img_t = transform(image)  
    t_resized = F.resize(img_t, [ascii_h * (tw * tratio), tw * ascii_w])
    
    # нормализуем всю картинку, отдельно для каждого измерения
    mean, std = t_resized.mean([1, 2]), t_resized.std([1, 2])
    normalize = transforms.Compose([transforms.Normalize(mean, std)])
    t_normalized = normalize(t_resized)
    
    tlist = []
    for long_tensors in torch.tensor_split(t_normalized, ascii_h, dim=1):
        tlist.append(torch.stack(torch.tensor_split(long_tensors, ascii_w, dim=2)))
    stacked = torch.stack(tlist)
    return stacked
