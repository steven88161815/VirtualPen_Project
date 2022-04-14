import cv2
import numpy as np


img = np.zeros((600, 600, 3), np.uint8)

# 畫直線
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2) # 原圖；起點；終點；顏色；粗度

# 畫方形
cv2.rectangle(img, (0, 0), (400, 300), (0, 0, 255), cv2.FILLED) # 參數同上，如果方形想填滿可以在粗度那欄填cv2.Filled

# 畫圓
cv2.circle(img, (300, 400), 30, (255, 0, 0), cv2.FILLED) # 原圖；原點；半徑；顏色；粗度

# 寫文字(不支援中文)
cv2.putText(img, "Hello", (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 2) # 原圖；字；字左下角座標；字體；文字大小；顏色；粗度


cv2.imshow('img', img)
cv2.waitKey(0)