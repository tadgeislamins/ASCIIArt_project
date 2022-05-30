import torch
from torchvision import transforms
from torchvision.utils import save_image
from os import mkdir
from char_tensors import char_t
from numpy.random import randint

rotate = transforms.Compose([
    transforms.RandomRotation(10, fill=1),
])

mkdir('trainset')

for ch in open('files/chars.txt').read()[:-1]:
    t0 = char_t(ch)
    mkdir('trainset/' + str(ord(ch)))

    for i in range(100):
        t = rotate(t0)
        t += torch.randn(t[0].size()).expand([3, -1, -1]) * randint(0, 5) * 0.1

        save_image(t, 'trainset/' + str(ord(ch)) + '/' + str(i) + '.jpg')
