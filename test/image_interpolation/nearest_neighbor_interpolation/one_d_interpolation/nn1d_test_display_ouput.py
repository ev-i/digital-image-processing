from PIL import Image
import sys
sys.path.append('.')
from src.image_interpolation.nearest_neighbor_interpolation.one_d_interpolation import nn1d


# Задан одномерный массив пикселей. Индекс элемента в массиве - координата пикселя. Значение элемента массива - яркость пикселя. Значение элемента None означает неизвестную яркость.
# pixels = [1, None, None, 20, None, None, 155]
pixels = [60, None, None, 125, None, None, 255]
# Таким образом имеем три пикселя с известной яркостью - (x0), (x3), (x6) и четыре пикселя с неизвестной яркостью (x1), (x2), (x4), (x5)
print(pixels)

# Необходимо задать яркость пикселям с неизвестной яркостью интерполяцией по ближайшему соседу
print(nn1d.fill_empty(pixels))

im = Image.new('L', (len(pixels), 1))

im.putdata(pixels,1,0)
im.resize((600,200), 0).show()

im.putdata(nn1d.fill_empty(pixels),1,0)
im.resize((600,200), 0).show()
