import os
import numpy as np
from PIL import Image


def get_blank_array(dimensions):
    return np.zeros(dimensions + (3,), dtype=np.uint8)


def save_array_as_img(f_name, array):
    Image.fromarray(array).save(os.path.join(os.getcwd().replace("interpreter", ''), f_name))


def quick_show(array):
    Image.fromarray(array).show()


def distance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
