import torch
from torchvision import transforms
from torchvision.utils import save_image
from os import mkdir
from char_tensors import char_t
# from numpy.random import randint

width = 10

tf = transforms.Compose([
    transforms.RandomRotation(10, fill=1),
    transforms.Pad(width // 2, fill=1),
    transforms.RandomCrop([width * 2, width])
])

mkdir('trainset')

for ch in open('files/chars.txt').read()[:-1]:
    t0 = char_t(ch, width=width)
    mkdir('trainset/' + str(ord(ch)))

    for i in range(1000):
        t = tf(t0)
        t += torch.randn(t[0].size()).expand([3, -1, -1]) * 0.1
        save_image(t, 'trainset/' + str(ord(ch)) + '/' + str(i) + '.jpg')
