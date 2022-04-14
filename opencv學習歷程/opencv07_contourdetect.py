import cv2

img = cv2.imread('shape.jpg')
imgContour = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 150, 200)

# 找圖片輪廓(回傳輪廓、階層)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 原圖；模式；近似方法

print(type(contours))
print(type(contours[0]))
print(contours[0].shape)

for cnt in contours:
    # 畫輪廓
    cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 4) # 原圖；要畫的輪廓；要畫的輪廓的指標(全都要畫可以設成-1)；顏色；粗度
    # 算輪廓面積
    area = cv2.contourArea(cnt)
    if area > 500:
        # 算輪廓邊長
        # print(cv2.arcLength(cnt, True)) # 輪廓；輪廓是否閉合

        # 用多邊形近似輪廓
        peri = cv2.arcLength(cnt, True)
        vertices = cv2.approxPolyDP(cnt, peri * 0.02, True) # 輪廓；近似值(越大多邊形邊越多)；輪廓是否閉合
        print(vertices.shape)
        corners = len(vertices)

        # 用方形將頂點框起來
        x, y, w, h = cv2.boundingRect(vertices) # 左上角xy座標；方形寬度高度
        cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 4)

        if corners == 3:
            cv2.putText(imgContour, 'triangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners == 4:
            cv2.putText(imgContour, 'rectangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners == 5:
            cv2.putText(imgContour, 'pentagon', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners >= 6:
            cv2.putText(imgContour, 'circle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.imshow('canny', canny)
cv2.imshow('imgContour', imgContour)
cv2.waitKey(0)