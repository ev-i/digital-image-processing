import sys
sys.path.append('.')
from src.image_scaling.upscaling.two_d_upscaling_nn2d_interpolation import two_d_upscaling_nn2d_interpolation
from PIL import Image
import numpy

# Задан двумерный массив пикселей. Индексы элемента в массиве - координата пикселя. Значение элемента массива - яркость пикселя. Значение элемента None означает неизвестную яркость.
pixels = \
        [[   50, 100, 150, 200, 250],
         [  100, 100, 150, 200, 250],
         [  150, 150, 150, 200, 250],
         [  200, 200, 200, 200, 250],
         [  250, 250, 250, 250, 250]]
                  
scale_factor = 10

# Необходимо увеличить изображение в scale_factor раз

upscaled = two_d_upscaling_nn2d_interpolation.two_d_upscaling_with_near_neighbor_interpolation(pixels, scale_factor)

arr = numpy.asarray(upscaled)
im = Image.fromarray(arr)
im.resize((800,800), 0).show()
# im.show()


