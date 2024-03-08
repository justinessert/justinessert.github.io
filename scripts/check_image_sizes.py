# Python code to check the dimensions of each image

import math
import os
from PIL import Image

image_path = "img/mascot/"

wrong_ratio = []
too_small = []
for image_filename in os.listdir(image_path):
    if not image_filename.endswith(".jpg"):
        continue
    with Image.open(image_path+image_filename) as image:
        width, height = image.size
        ratio = width/height
        name = image_filename.split(".jpg")[0]
        print_name = f"- {name}: {width} {height} ({ratio})"
        if not math.isclose(ratio, 0.75, abs_tol=0.0025):
            wrong_ratio.append(print_name)
        if width < 300:
            too_small.append(print_name)

print("Images with incorrect ratios:\n" + "\n".join(sorted(wrong_ratio)))
print("Images that are too small:\n" + "\n".join(sorted(too_small)))