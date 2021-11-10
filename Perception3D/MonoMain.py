# -*- coding: utf-8 -*-
from Calibration import MonoCalibration
from Rectification import MonoRectification

calibration = MonoCalibration(cols=8, rows=6, patternType='symmetric_circles')

# Acquisition
# calibration.acquire()

# Calibration
rms, cameraMatrix, distCoeffs, imageSize = calibration.calibrate()

# Visualization
# calibration.visualizeBoards()
# calibration.plotRMS()

# Rectification
rectification = MonoRectification(cameraMatrix, distCoeffs, imageSize)
rectification.display()