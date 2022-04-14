import cv2
import numpy as np

kernel1 = np.ones((3, 3), np.uint8)
kernel2 = np.ones((3, 3), np.uint8)

img = cv2.imread('colorcolor.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# 彩色圖片轉換成灰階圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)

# 高斯模糊
blur = cv2.GaussianBlur(img, (15, 15), 10) # 原圖；kernel_size(只能是odd)；標準差

# 取得圖片邊緣(像素點的像素值與周圍像素點的像素值差別很大時，會給較大的分數)
canny = cv2.Canny(img, 150, 200) # 所以此例就是150分以下就是不當邊緣，200分以上當邊緣

# 圖片膨脹
dilate = cv2.dilate(canny, kernel1, iterations=1) # 原圖；kernel_size(二微陣列)；膨脹次數

# 圖片變細(erode:侵蝕)
erode = cv2.erode(dilate, kernel2, iterations=1) # 原圖；kernel_size(二微陣列)；侵蝕次數

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)