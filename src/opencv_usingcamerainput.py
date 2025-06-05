#-------------------------------------------------------------------------------
# Name:        opencv_usingcamerainput.py
# Purpose:
#
# Author:      Joshua Zimmerman
#
# Created:     04/06/2025
# Copyright:   (c) Joshua Zimmerman 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image


def main():
    s = 0
    if len(sys.argv) > 1:
        s = sys.argv[1]

    print(s)

    source = cv2.VideoCapture(s)

    win_name = 'Camera Preview'
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

    while cv2.waitKey(1) != 27:
        has_frame, frame = source.read()
        if not has_frame:
            break
        cv2.imshow(win_name, frame)

    source.release()
    cv2.destroyWindow(win_name)

if __name__ == '__main__':
    main()
