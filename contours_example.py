import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img2.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# or
# imgray = cv2.imread('img1.png', cv2.IMREAD_GRAYSCALE)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)
'''there are three arguments in cv2.findContours() function, 
first one is source image, second is contour retrieval mode, third is contour approximation method'''
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(contours)

'''first argument is source image, second argument is the contours which should be passed as a Python list, 
third argument is index of contours (useful when drawing individual contour.
 To draw all contours, pass -1) and remaining arguments are color, thickness etc.'''
# For all contours
img = cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
# For a specific contour
# cnt = contours[12]
# img = cv2.drawContours(im, [cnt], 0, (0, 255, 0), 1)

# print(contours)

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()