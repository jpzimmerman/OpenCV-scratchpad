import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image


x = 5
print(x)
checkerboard_image = cv2.imread('./notebooks/content/baobab-tree-at-sunset-african-landscape.jpg')
print(checkerboard_image)
print(f"Size of image is {checkerboard_image.shape}")
print(f"Data type of image is {checkerboard_image.dtype}")
plt.imshow(checkerboard_image)

cv2.imshow(cv2.namedWindow("Window 1"), checkerboard_image)
cv2.waitKey(8000)
# cv2.destroyWindow(window1)