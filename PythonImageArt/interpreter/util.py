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


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


# Mandelbrot calculation constants
MAX_ITER = 100
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1


def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1
    return n
