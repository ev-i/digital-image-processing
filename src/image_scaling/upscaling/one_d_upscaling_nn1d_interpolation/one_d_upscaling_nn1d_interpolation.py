import sys
sys.path.append('.')

from src.image_scaling.upscaling.one_d_expander import one_d_expander
from src.image_interpolation.nearest_neighbor_interpolation.one_d_interpolation import nn1d

def one_d_upscaling_with_near_neighbor_interpolation(array, scale_factor):
    expanded = one_d_expander.one_d_expander(array, scale_factor)
    upscaled = nn1d.fill_empty(expanded)
    return upscaled