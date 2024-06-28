import cv2
import numpy as np
from skimage import io

import skimage as sk

mask= sk.io.imread('test.png', as_gray=True)

sk.io.imshow(mask)
io.show()
im_shape=mask.shape
contours_list = sk.measure.find_contours(mask, level=0.7)
print("Number of contours:", len(contours_list))

polygons = []
for i, contour in enumerate(contours_list):
    polygon_points = sk.measure.approximate_polygon(contour, tolerance=1)
    polygons.append(polygon_points)
    print("Contour {:02d} has {: >3} points.".format(i, len(polygon_points)))
    

from skimage.draw import polygon2mask



comb_img = np.zeros(mask.shape, dtype=int)
for polygon in polygons:
    img_poly = polygon2mask(mask.shape, polygon)
    f = open("yolo.txt", "a")
    f.write("\n1") #class
    for wr in polygon:
        x_cor=wr[0]/im_shape[0];
        y_cor=wr[1]/im_shape[1];        
        f.write(f" {x_cor} {y_cor} ")
    f.close()
    
    comb_img += img_poly 
    io.imshow(img_poly)
    io.show()
    
io.imshow(comb_img)
io.show()

io.imshow((comb_img-mask)**2)
io.show()

import json
# Opening JSON file

input_path = 'test.jpg'
input = cv2.imread(input_path)

#input = cv2.filter2D(input, -1, sharpen_kernel)
#cv2.imwrite('test.png',input)  
input=np.array(input)
# Removing the background from the given Image 

imgGray = cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)
lab = cv2.cvtColor(input, cv2.COLOR_BGR2LAB)
# store the a-channel
a_channel = lab[:,:,1]
# Automate threshold using Otsu method
th = cv2.threshold(a_channel,130,200,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
# Mask the result with the original image
masked = cv2.bitwise_and(input, input, mask = th)
cv2.imwrite('masoud.png',masked)



f = open('jo.json')
data = json.load(f)
f.close()

coordinates = (data[0]['annotations'][0]['result'][0]['value']['points']);
for i in range(len(coordinates)):
    coordinates[i]=[(x/100)*448 for x in coordinates[i]]
    
for i in range(len(coordinates)):
    coordinates[i][0],coordinates[i][1]= coordinates[i][1],coordinates[i][0]   
    
polygon = np.array(coordinates)
mask = polygon2mask((448,448), polygon)
mask2=th
for i in range(mask.shape[0]):
    for j in range(mask.shape[1]):
        if mask[i][j]==True:
            mask2[i][j]=255;
        else:
            mask2[i][j]=0;
result = cv2.bitwise_and(input,input, mask= (mask2))
io.imshow(result)
io.show()
