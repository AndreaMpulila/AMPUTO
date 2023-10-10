import math
import sys
from PIL import Image, ImageFilter

if len(sys.argv) != 2:
    sys.exit('Usage: python imagefilter.py filename')

image = Image.open(sys.argv[1]).convert('RGB')
filtered = image.filter(ImageFilter.Kernel(
    size=(3, 3),
    kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1],
    scale=1
))
filtered.show()
