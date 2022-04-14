import cv2
import numpy as np

def empty():
    pass


img = cv2.imread('XiWinnie.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# 建立視窗內的動態控制條找出欲篩選顏色的HSV值
cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar', 640, 320)

# 色調、飽和度、亮度
cv2.createTrackbar('Hue Min', 'TrackBar', 0, 179, empty)   # 控制條名稱；所屬視窗；控制條初始值；控制條最大值；控制條被改變時呼叫的函式
cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, empty) # 控制條名稱；所屬視窗；控制條初始值；控制條最大值；控制條被改變時呼叫的函式
cv2.createTrackbar('Sat Min', 'TrackBar', 0, 255, empty)   # 控制條名稱；所屬視窗；控制條初始值；控制條最大值；控制條被改變時呼叫的函式
cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, empty) # 控制條名稱；所屬視窗；控制條初始值；控制條最大值；控制條被改變時呼叫的函式
cv2.createTrackbar('Val Min', 'TrackBar', 0, 255, empty)   # 控制條名稱；所屬視窗；控制條初始值；控制條最大值；控制條被改變時呼叫的函式
cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, empty) # 控制條名稱；所屬視窗；控制條初始值；控制條最大值；控制條被改變時呼叫的函式

# 將BGR表示成HSV較容易挑選顏色
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(hsv.shape)

# 即時取得控制條上面的數值
while True:
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBar')
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # 過濾顏色
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.waitKey(1)



