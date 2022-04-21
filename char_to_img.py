from PIL import Image, ImageDraw, ImageFont
width = 30
texttoframe = 1.5


def getSize(txt, font):
    testImg = Image.new('RGB', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)


def to_img(ch):
    img = Image.new('RGB', (width, width * 2), (255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', int(width * texttoframe))
    d.text((width / 2, width), chr(ch), fill=(0, 0, 0), font=font, anchor='mm')

    img.save('chars/' + str(ch) + '.png')


for i in range(33, 127):
    to_img(i)
