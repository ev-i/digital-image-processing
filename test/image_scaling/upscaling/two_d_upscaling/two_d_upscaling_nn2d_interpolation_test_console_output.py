import sys
sys.path.append('.')
from src.image_scaling.upscaling.two_d_upscaling_nn2d_interpolation import two_d_upscaling_nn2d_interpolation

original = \
        [[   50, 100, 150, 200, 250],
         [  100, 100, 150, 200, 250],
         [  150, 150, 150, 200, 250],
         [  200, 200, 200, 200, 250],
         [  250, 250, 250, 250, 250]]

scale_factor = 4


[print(*line) for line in original]
print('=========================')
[print(*line) for line in two_d_upscaling_nn2d_interpolation.two_d_upscaling_with_near_neighbor_interpolation(original, scale_factor)]

