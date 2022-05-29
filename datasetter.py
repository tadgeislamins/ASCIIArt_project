import torch
from torchvision import transforms
from torchvision.utils import save_image
from os import mkdir
from char_tensors import char_t

rotate = transforms.Compose([
    transforms.RandomRotation(10, fill=255),
])

mkdir('trainset')

for ch in range(33, 127):
    t = char_t(ch)
    mkdir('trainset/' + str(ch))

    for i in range(10):
        t = rotate(t)
        t += torch.randn(t.size()) * 0.1

        save_image(t, 'trainset/' + str(ch) + '/' + str(i) + '.jpg')
