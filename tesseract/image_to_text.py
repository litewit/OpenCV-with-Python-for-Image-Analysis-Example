import cv2
import pytesseract

imgray = cv2.imread('cv.jpg', cv2.IMREAD_GRAYSCALE)

# Define config parameters.
# '-l eng'  for using the English language
# '--oem 1' for using LSTM OCR Engine
# 0    Legacy engine only.
# 1    Neural nets LSTM engine only.
# 2    Legacy + LSTM engines.
# 3    Default, based on what is available.
# psm = 3 (i.e. PSM_AUTO).
config = ('-l eng --oem 1 --psm 3')

# Run tesseract OCR on image
text = pytesseract.image_to_string(imgray, config=config)

# Print recognized text
print(text)
