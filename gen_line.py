from extract_borders import sobelize
from img_tensor import pic_to_tensors


def gen_line(img, width=20):
    img_t = pic_to_tensors(sobelize(img))
    return img_t
