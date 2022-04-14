import cv2

# 讀取影片
cap = cv2.VideoCapture('thumb.mp4') # 放路徑
# 讀取攝像頭畫面
# cap = cv2.VideoCapture(0) # 0代表預設攝像頭、1代表第一個外接攝像頭

while True: # 如果不寫迴圈則只會出現第一張圖片
    # 讀取影片當中的下一幀圖片
    ret, frame = cap.read() # ret表示布林值，代表獲取下一幀圖片是否成功；frame表示下一幀圖片

    if ret:
        # 改變圖片大小
        frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)
        # 輸出圖片
        cv2.imshow('video', frame)

    else: # 讀取下一幀失敗有兩種原因：1.影片有問題 2.影片已結束
        break

    # 輸入q就可以中途結束
    if cv2.waitKey(10) == ord('q'): # waitKey裡的值決定影片的播放速度
        break