Computer Vision Projects Repository

This repository contains Python projects built using OpenCV and MediaPipe to explore real-time computer vision concepts such as face detection, hand tracking, and creative overlays. Each file demonstrates a specific implementation for learning and experimentation.

📂 basic ig

A simple introductory script that initializes a webcam feed using OpenCV.
Helps understand:

cv2.VideoCapture() for accessing the camera

Displaying frames using cv2.imshow()

Loop structure and cv2.waitKey() for frame control

File Type: .py

🧍‍♂️ sample face detection

Implements basic face detection using Haar Cascades.
Key topics:

Loading pre-trained XML classifiers

Converting frames to grayscale

Drawing rectangles around detected faces

File Type: .py

🟩 more rectangles

Enhances face detection by adding multiple rectangles around the face.
Concepts demonstrated:

Calculating positions relative to detected face coordinates

Using custom colors like cyan, lavender, and green

Drawing symmetrical rectangles on left and right sides

File Type: .py

✋ hand detection

Uses MediaPipe Hands for real-time hand landmark detection and tracking.
Includes:

Hand joint mapping

Connecting landmarks visually

Smooth detection performance even with motion

File Type: .py

⚙️ combination

Combines both face and hand detection in a single program for multi-feature tracking.
Covers:

Simultaneous OpenCV and MediaPipe pipelines

Frame processing optimization

Displaying multiple detections in real time

File Type: .py

🧾 self summary

A summary script that documents all implemented concepts and learnings from previous modules.
Useful for:

Revising key OpenCV and MediaPipe functions

Understanding integration flow between camera input, detection, and visualization

File Type: .py

📚 Technologies Used

🧠 OpenCV — Image & video processing

✋ MediaPipe — Hand, face, and landmark detection

🔢 NumPy — Numerical array operations
