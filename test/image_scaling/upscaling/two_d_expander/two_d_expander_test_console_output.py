import sys
sys.path.append('.')
from src.image_scaling.upscaling.two_d_expander.two_d_expander import two_d_expander

original =  [[   1, None, None],
             [None,   20, None],
             [None, None,  155]]

scale_factor = 2


[print(*line) for line in original]
print('=========================')
[print(*line) for line in two_d_expander(original, scale_factor)]

