import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
print("Camera started... Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        rect_w = int(w * 0.8)
        rect_h = int(h * 0.8)
        rect_x1 = x - 12
        rect_y1 = y + int(h * 0.30)
        rect_x2 = rect_x1 + rect_w
        rect_y2 = rect_y1 + rect_h
        cv2.rectangle(frame, (rect_x1, rect_y1), (rect_x2, rect_y2), (255, 255, 0), 2)

        rect_x1_r = x + w - rect_w + 12
        rect_y1_r = y + int(h * 0.20)
        rect_x2_r = rect_x1_r + rect_w
        rect_y2_r = rect_y1_r + rect_h
        cv2.rectangle(frame, (rect_x1_r, rect_y1_r), (rect_x2_r, rect_y2_r), (0, 255, 0), 2)

    cv2.imshow("Left + Right Rectangles", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

