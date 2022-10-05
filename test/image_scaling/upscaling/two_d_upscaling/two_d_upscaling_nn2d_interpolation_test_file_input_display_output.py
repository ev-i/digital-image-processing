import sys
sys.path.append('.')
from src.image_scaling.upscaling.two_d_upscaling_nn2d_interpolation import two_d_upscaling_nn2d_interpolation
from PIL import Image
import numpy





scale_factor = 2


# Необходимо увеличить изображение в scale_factor раз

im = Image.open("res/pixel_heart_mono.png")
# im.show()
image_sequence = im.getdata(0)
# print(list(image_sequence))
array = list(image_sequence)
print(array)
# [print(*line) for line in array]
# [print(list((line[0]) for line in array))]
# array = numpy.array(image_sequence)


# upscaled = two_d_upscaling_nn2d_interpolation.two_d_upscaling_with_near_neighbor_interpolation(array, scale_factor)

# arr = numpy.asarray(upscaled)
# im = Image.fromarray(arr)
# im.show()


