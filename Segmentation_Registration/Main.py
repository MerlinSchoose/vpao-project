# -*- coding: utf-8 -*-
import numpy as np
import open3d as o3d

from Segmentation import Segmentation
from Registration import Registration

seg = False
if seg:
    ### Segmentation
    # Select zone of interest
    pcd = o3d.io.read_point_cloud("data/OtherBoxes/box5.ply")
    o3d.visualization.draw_geometries_with_editing([pcd])

    # Load in Segmentation object
    segmentation = Segmentation("data/cropped_box_6.ply")
    segmentation.display()

    # Remove Outliers
    segmentation.removeOutliers(display=True)
    segmentation.display()

    # Compute normals
    normals = segmentation.computeNormals(alignVector=[0, 1, 0])
    segmentation.normalsHistogram()

    # Estimate the floor's normal
    floorNormal = segmentation.estimateFloorNormal()
    segmentation.display()

    # ALign the floor with the horizontal plane
    segmentation.alignFloor()
    segmentation.display()

    # Remove the floor
    segmentation.removeFloor()
    segmentation.display()

    o3d.io.write_point_cloud("data/segmented_box_6.ply", segmentation.pointCloud)

else:
    ### Registration
    # Load and visualize the objects
    source = o3d.io.read_point_cloud("data/segmented_box.ply")
    target = o3d.io.read_point_cloud("data/segmented_box_6.ply")

    registration = Registration(source, target)
    registration.display()

    # # Global registration
    registration.processGlobal()
    registration.display()

    # ICP Registration
    registration.processICP()
    registration.display()