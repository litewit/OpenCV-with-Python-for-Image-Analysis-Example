import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img1.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# or
# imgray = cv2.imread('img1.png', cv2.IMREAD_GRAYSCALE)

ret, img_thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# cv2.imshow('image',img_thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img_thresh, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()