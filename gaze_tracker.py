import cv2
import numpy as np
from collections import deque

# Load Haarcascades for face & eyes
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# Use a queue (deque) for smoothing gaze tracking (stores last 10 gaze points)
gaze_history = deque(maxlen=10)

def detect_eyes(frame):
    """ Detects eyes and returns their center positions. """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(80, 80))

    if len(faces) == 0:
        return None

    for (x, y, w, h) in faces:
        face_roi = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(face_roi, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(eyes) == 0:
            return None

        eye_positions = [(x + ex + ew // 2, y + ey + eh // 2) for (ex, ey, ew, eh) in eyes]
        return eye_positions

    return None

def get_gaze_point(frame):
    """ Uses moving average filtering to smooth gaze tracking. """
    eyes = detect_eyes(frame)

    if eyes is None:
        return None

    # Calculate average X position of both eyes
    gaze_x = int(np.mean([eye[0] for eye in eyes]))

    # Apply moving average filter to stabilize gaze tracking
    gaze_history.append(gaze_x)
    smoothed_gaze_x = int(np.mean(gaze_history))

    print(f"Raw Gaze X: {gaze_x}, Smoothed Gaze X: {smoothed_gaze_x}")  # Debugging output
    return smoothed_gaze_x
