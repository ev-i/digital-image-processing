import sys
sys.path.append('.')
from src.image_interpolation.nearest_neighbor_interpolation.two_d_interpolation import nn2d
from PIL import Image
import numpy

# Задан двумерный массив пикселей. Индексы элемента в массиве - координата пикселя. Значение элемента массива - яркость пикселя. Значение элемента None означает неизвестную яркость.
pixels =[[   1, None, None, None, None, None, 60],
         [None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, None,   111, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [60, None, None, None, None, None,  255]]
# Таким образом имеем три пикселя с известной яркостью и остальные пиксели с неизвестной яркостью

# Необходимо задать яркость пикселям с неизвестной яркостью интерполяцией по ближайшему соседу

arr = numpy.asarray(nn2d.fill_empty(pixels))
im = Image.fromarray(arr)
im.resize((700,800), 0).show()


