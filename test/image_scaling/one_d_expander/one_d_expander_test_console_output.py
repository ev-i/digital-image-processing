import sys
sys.path.append('.')
from src.image_scaling.upscaling.one_d_expander.one_d_expander import one_d_expander


original = [0, 50, 100, 150, 200, 250]
scale_factor = 4

print(original)
print(one_d_expander(original, scale_factor))

