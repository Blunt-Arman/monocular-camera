import cv2
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access camera.")
    exit()

print("Camera started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Live Camera Feed", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
