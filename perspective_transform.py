import cv2
import numpy as np

# read the input image
try:
    img = cv2.imread('road1.jpg')
    cv2.namedWindow('Display Image')
    cv2.imshow("Road", img)

except Exception as e:
    print(e)


print(img.shape)

# define the source and destination points for perspective transform
#src_points = np.float32([(0, 800), (1500, 800), (1000, 500), (500, 500)])
#dst_points = np.float32([(0, img.shape[0]), (img.shape[1], img.shape[0]), (img.shape[1], 0), (0, 0)])

# compute the perspective transform matrix
#M = cv2.getPerspectiveTransform(src_points, dst_points)

# apply the perspective transform to the image
#warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))

# display the original and transformed images side by side
#cv2.imshow('Original Image', img)
#cv2.imshow('Warped Image', warped)

cv2.waitKey(0)

cv2.destroyAllWindows()