from skimage.io import imread
from skimage import data
import numpy as np
from skimage import io

binary_mask = data.binary_blobs(length=98, blob_size_fraction=0.1)
binary_mask = np.pad(binary_mask, pad_width=1)

io.imshow(binary_mask)
io.show()