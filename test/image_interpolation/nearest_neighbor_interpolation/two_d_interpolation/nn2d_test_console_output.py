import sys
sys.path.append('.')
from src.image_interpolation.nearest_neighbor_interpolation.two_d_interpolation import nn2d

# Задан двумерный массив пикселей. Индексы элемента в массиве - координата пикселя. Значение элемента массива - яркость пикселя. Значение элемента None означает неизвестную яркость.
pixels =[[   1, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, None,   20, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, None, None, None, None,  155]]
# Таким образом имеем три пикселя с известной яркостью - (x0, y0), (x3, y3), (x6, y6) и остальные пикселя с неизвестной яркостью
# Необходимо задать яркость пикселям с неизвестной яркостью интерполяцией по ближайшему соседу

[print(*line) for line in pixels]

# Необходимо задать яркость пикселям с неизвестной яркостью интерполяцией по ближайшему соседу

[print(*line) for line in nn2d.fill_empty(pixels)]



