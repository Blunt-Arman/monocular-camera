import cv2
cap = cv2.VideoCapture(0)
print("success")
while True:

    ret,frame = cap.read()
    if not ret:
        break
    print("+1")
    cv2.imshow("Camera", frame )

    
    if cv2.waitKey(1)&0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
