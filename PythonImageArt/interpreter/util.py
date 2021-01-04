import numpy as np
from PIL import Image

"""

Add custom functions here.

"""


def get_blank_array(dimensions):
    return np.zeros(dimensions + (3,), dtype=np.uint8)


def save_array_as_img(f_name, array):
    img = Image.fromarray(array).transpose(Image.ROTATE_90)
    img.save(f_name)


def quick_show(array):
    Image.fromarray(array).transpose(Image.ROTATE_90).show()


def distance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
