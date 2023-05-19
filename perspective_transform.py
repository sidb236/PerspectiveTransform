import cv2
import numpy as np

# read the input image

img = cv2.imread('road1.jpg')
cv2.namedWindow('Display Image')
cv2.imshow("Road", img)


print(img.shape)

try:
    # define the source and destination points for perspective transform
    src_points = np.float32([(54,653), (1180,653), (461,484), (770,484)])
    dst_points = np.float32([(0,0),(1180,0),(0,653), (1180,653)])

    # compute the perspective transform matrix
    M = cv2.getPerspectiveTransform(src_points, dst_points)

    # apply the perspective transform to the image
    warped = cv2.warpPerspective(img, M, (1180, 653))

except Exception as e:
    print(e)

# display the original and transformed images side by side
cv2.imshow('Original Image', img)
cv2.imshow('Warped Image', warped)

cv2.waitKey(0)

cv2.destroyAllWindows()
