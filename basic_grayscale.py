import cv2
from matplotlib import pyplot as plt


'''
Simple example which converts colored image to black and white or grayscale. 
Its easy to work with grayscale image than colored image. So its good practice to convert an image to grayscale.
'''

imgray = cv2.imread('img1.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Image show using matplotlib Uncomment below
# plt.imshow(imgray, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
# plt.show()
