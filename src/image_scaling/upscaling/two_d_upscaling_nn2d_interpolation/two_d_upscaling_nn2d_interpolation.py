import sys
sys.path.append('.')

from src.image_scaling.upscaling.two_d_expander import two_d_expander
from src.image_interpolation.nearest_neighbor_interpolation.two_d_interpolation import nn2d

def two_d_upscaling_with_near_neighbor_interpolation(array, scale_factor):
    expanded = two_d_expander.two_d_expander(array, scale_factor)
    upscaled = nn2d.fill_empty(expanded)
    return upscaled