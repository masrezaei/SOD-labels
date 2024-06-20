from skimage.io import imread
from skimage import data

import numpy as np
from skimage import io

import skimage as sk

mask= sk.io.imread('test.png', as_gray=True)

sk.io.imshow(mask)
io.show()

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
    comb_img += img_poly 
    io.imshow(img_poly)
    io.show()
    
io.imshow(comb_img)
io.show()

io.imshow((comb_img-mask)**2)
io.show()