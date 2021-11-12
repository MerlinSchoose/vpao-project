# -*- coding: utf-8 -*-
from Calibration import StereoCalibration
from Rectification import StereoRectification
import cv2 as cv
import numpy as np


# Calibration
calibration = StereoCalibration(cols=7, rows=6, patternSize_m=0.108, patternType='chessboard')
(rms, cameraMatrixLeft, distCoeffsLeft,
 cameraMatrixRight,distCoeffsRight, imageSize, R, T) = calibration.calibrate()

# Visualization
# calibration.plotRMS()

# Rectification
rectification = StereoRectification(cameraMatrixLeft, distCoeffsLeft, cameraMatrixRight, distCoeffsRight, imageSize, R, T)
rectification.computeCorrectionMaps()

# 3D reconstruction
left = cv.imread('data/stereo/MinnieRawLeft.png', cv.IMREAD_GRAYSCALE)
right = cv.imread('data/stereo/MinnieRawRight.png', cv.IMREAD_GRAYSCALE)

rectification.display(left, right)
rectification.displayDisparity(left, right)