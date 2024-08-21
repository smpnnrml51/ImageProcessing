import cv2
img= cv2.imread('image.jpg')
neg_img = cv2.bitwise_not(img)
cv2.imshow("Original Image", img)
cv2.imshow("Digital Negative Image", neg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()