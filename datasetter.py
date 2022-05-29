import torch
from torchvision import transforms
from torchvision.utils import save_image
from os import mkdir
from char_tensors import char_t


# class AddGaussianNoise(object):
#     def __init__(self, mean=0., std=1.):
#         self.std = std
#         self.mean = mean
#
#     def __call__(self, tensor):
#         return tensor + torch.randn(tensor.size()) * self.std + self.mean
#
#     def __repr__(self):
#         return self.__class__.__name__ + '(mean={0}, std={1})'.format(self.mean, self.std)


rotate = transforms.Compose([
    transforms.RandomRotation(10, fill=255),
])

mkdir('dataset')

for ch in range(33, 127):
    t = char_t(ch)
    mkdir('dataset/' + str(ch))

    for i in range(10):
        t = rotate(t)
        t += torch.randn(t.size()) * 0.1

        save_image(t, 'dataset/' + str(ch) + '/' + str(i) + '.jpg')
