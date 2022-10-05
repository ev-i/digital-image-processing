import sys
sys.path.append('.')
from src.image_scaling.upscaling.one_d_upscaling_nn1d_interpolation import one_d_upscaling_nn1d_interpolation

original = [0, 50, 100, 150, 200, 250]
scale_factor = 4

print(original)
print(one_d_upscaling_nn1d_interpolation.one_d_upscaling_with_near_neighbor_interpolation(original, scale_factor))

