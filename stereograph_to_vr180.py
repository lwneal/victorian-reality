import sys
import time
import numpy as np
from PIL import Image

# Converts a Holmes stereograph to the VR180 format.

input_filename = sys.argv[1]
output_filename = sys.argv[2]
stereograph_img = np.array(Image.open(input_filename))

# The input is two images side by side
height, full_width, channels = stereograph_img.shape
width = full_width // 2

# TODO extract the photos from the surrounding chrome, align

left = stereograph_img[:, :width, :3]
right = stereograph_img[:, width:, :3]

# VR180 must be two square images side-by-side.
out_height = 2048
out_width = out_height * 2
img = np.zeros((out_height, out_width, 3))


x0 = out_height//2 - width // 2
y0 = out_height//2 - height//2

x1 = x0 + out_height

img[y0:y0+height, x0:x0+width] = left
img[y0:y0+height, x1:x1+width] = right

Image.fromarray(img.astype(np.uint8)).save(output_filename)
