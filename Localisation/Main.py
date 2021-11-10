#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import cv2 as cv
import numpy as np
from math import sqrt

from Homography import PerspectiveCorrection
from Tracking import Tracker
from PoseEstimation import PoseEstimator

perspectiveCorrection = False

height_px = 720 # size in pixels along Y
width_px = 1280 # size in pixels along X
outSize = (width_px, height_px)

if perspectiveCorrection:
    image = cv.imread("data/ReferenceImg.jpeg") # Read the image of your object

    cor = PerspectiveCorrection()
    outImage = cor.process(image, outSize)

    # Save your image
    cv.imwrite("data/ReferenceImgCorr.jpg", outImage)

else:
    # Implement the calibration results of TP1 Perception3D
    cameraMatrix = np.array([[ 678.04925032, 0, 315.69044912 ],
                             [ 0, 675.59676374, 194.13795736 ],
                             [ 0, 0, 1 ]], np.float64)
    distCoeffs = np.array([0.18138071, -0.49320258, -0.0111219, -0.00055014, 0.2524249], np.float64)

    img_object = cv.imread("data/ReferenceImgCorr.jpg", cv.IMREAD_GRAYSCALE) # Read the image obtained in the first part
    # img_object = # Resize your object image

    # tracker = Tracker(img_object)
    # tracker.display()

    # Dimension of the object in the real world
    objectSize = (.195, .12, .025)

    # Estimate the pose and reproject on the image
    posEst = PoseEstimator(img_object, objectSize, cameraMatrix, distCoeffs)
    posEst.display(cameraMatrix, distCoeffs)