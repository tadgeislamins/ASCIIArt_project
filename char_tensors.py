import torch
from PIL import Image, ImageDraw, ImageFont
import torchvision
import torchvision.transforms as transforms

def totensor(chlist, width=30, texttoframe=1.5):
    for ch in chlist:
        img = Image.new('RGB', (width, width * 2), (255, 255, 255))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', int(width * texttoframe))
        d.text((width / 2, width), chr(ch), fill=(0, 0, 0), font=font, anchor='mm')

        transform = transforms.ToTensor()
        yield(transform(img))
