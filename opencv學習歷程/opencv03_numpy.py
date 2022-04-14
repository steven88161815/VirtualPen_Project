import cv2
import numpy as np
import random

img1 = cv2.imread('colorcolor.jpg')
print(img1)
print(type(img1))
print(img1.shape)
"""
順序：B  G  R
[255, 0, 0] → 藍
[0, 255, 0] → 綠
[0, 0, 255] → 紅
"""
# 圖片切割
newImg = img1[:150, :200].copy()

for row in range(300):
    for col in range(img1.shape[1]):
        img1[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# 自創圖片
img2 = np.empty((300, 300, 3), np.uint8) # 建一個空的陣列
for row in range(300):
    for col in range(300):
        img2[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('newImg', newImg)
cv2.waitKey(0)