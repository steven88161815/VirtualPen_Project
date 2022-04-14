import cv2

img = cv2.imread('qq.jpg')

# 彩圖轉灰階圖片，因為人臉辨識不需要彩圖
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 載入模型
faceCascade = cv2.CascadeClassifier('face_detect.xml')
faceRect = faceCascade.detectMultiScale(gray, 1.1, 5) # 欲辨識的圖；圖片縮小的倍數；最小偵測數(越大越嚴謹)
print(type(faceRect))
print(faceRect.shape)
print(len(faceRect))

for (x, y, w, h) in faceRect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)