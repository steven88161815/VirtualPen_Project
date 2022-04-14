import cv2

# 讀取圖片
img = cv2.imread('colorcolor.jpg') # 放路徑

# 第一種修改圖片大小的方式
# img = cv2.resize(img, (300, 300)) # 圖片；欲修改成的大小(用tuple表示)

# 第二種修改圖片大小的方式
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # 利用倍數進行圖片縮放

# 顯示讀取的圖片
cv2.imshow('img', img) # 圖片標題；圖片

# 出現的視窗多久會消失
cv2.waitKey(3000) # 單位：毫秒(0代表不會消失除非關閉)