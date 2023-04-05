# this is a sample code i used to convert the image into numerical array

# This method is used to load the 3d images using Trimesh Library 
# which one of the popular library used to load 3d iamge
import os
import numpy as np
import csv
import trimesh
# Traversing through the 3d images that are stored in my google drive 
# in order to get numerical data of the images
array = []
for image in os.listdir('C:/Users/SAI/Downloads/NOMO-3d-400-scans_and_tc2_measurements/NOMO-3d-400-scans_and_tc2_measurements/nomo-scans/female_obj/female_obj'):
    image_path = f"C:/Users/SAI/Downloads/NOMO-3d-400-scans_and_tc2_measurements/NOMO-3d-400-scans_and_tc2_measurements/nomo-scans/female_obj/female_obj/{image}"  # create the file path
    mesh = trimesh.load(image_path)
    vertices = np.array(mesh.vertices)
    remaining_rows=62244-vertices.shape[0]
    for i in range(remaining_rows):
        vertices=np.append(vertices,np.array([[0,0,0]]),axis=0)
    array.append(vertices)
array = np.array(array)
print(array) 
# this return a numerical array of shape (62244,3,1) 

