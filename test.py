# import cv2 as cv
# from paddleocr import PaddleOCR
# import numpy as np
#
# img = cv.imread('test.png')
# image3 = np.copy(img)
# ocr = PaddleOCR(use_angle_cls=True, use_gpu=False)
# # need to run only once to download and load model into memory
# result = ocr.ocr(img, rec=False)
#
# print(result)
# X = np.array(result)
# X = np.asarray(X, dtype='int')
# mask = np.zeros(img.shape[:2], dtype=np.uint8)
# x, y, w, h = cv.boundingRect(X[0][0])
# img[y:y + h, x:x + w] = 0
# mask[y:y + h, x:x + w] = 255
# x, y, w, h = cv.boundingRect(X[0][1])
# img[y:y + h, x:x + w] = 0
# mask[y:y + h, x:x + w] = 255
#
# kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))
# mask = cv.dilate(mask, kernel, iterations=6)
#
# cv.imshow('mask', img)
# cv.imshow('mask2', mask)
# cv.waitKey(0)
# inpainted = cv.inpaint(img, mask, 3, cv.INPAINT_TELEA)
#
# # Save the inpainted image
# cv.imshow('maskuyh2', inpainted)
# cv.waitKey(0)
# cv.imwrite('inpainted.jpg', inpainted)

# import numpy as np
# import cv2 as cv
#
# img = cv.imread('test.png')
# mask = cv.imread('mask.jpg', cv.IMREAD_GRAYSCALE)
# dst = cv.inpaint(img, mask, 3, cv.INPAINT_NS)
# cv.imshow('dst', dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

import cv2
import numpy as np

# Load the image
img = cv2.imread("image.jpg")

# Reshape the image to a 2D array of pixels
pixels = img.reshape((-1, 3))

# Convert the pixel values from 8-bit integers to floats
pixels = np.float32(pixels)

# Define the number of clusters (i.e. colors)
num_clusters = 80

# Perform k-means clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
_, labels, palette = cv2.kmeans(pixels, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Count the number of pixels in each cluster
cluster_counts = np.bincount(labels.ravel())
print(cluster_counts)
# Find the index of the cluster with the most pixels
top_cluster = np.argmax(cluster_counts)
print(top_cluster)
# Get the colors of the pixels in the top cluster
top_colors = palette[top_cluster]
print(top_colors)