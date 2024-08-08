import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize webcam and face mesh
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

def get_eye_landmarks(landmarks):
    # Define indices for left and right eye landmarks
    left_eye_indices = [33, 160, 158, 133, 153, 144]
    right_eye_indices = [362, 385, 387, 263, 373, 380]
    left_eye = [landmarks[i] for i in left_eye_indices]
    right_eye = [landmarks[i] for i in right_eye_indices]
    return left_eye, right_eye

def calculate_pupil_center(eye_landmarks):
    # Calculate the center of the pupil
    x_coords = [lm.x for lm in eye_landmarks]
    y_coords = [lm.y for lm in eye_landmarks]
    center_x = np.mean(x_coords)
    center_y = np.mean(y_coords)
    return center_x, center_y

def calculate_gaze_direction(left_pupil_center, right_pupil_center):
    # Calculate the gaze direction
    gaze_x = (left_pupil_center[0] + right_pupil_center[0]) / 2
    gaze_y = (left_pupil_center[1] + right_pupil_center[1]) / 2
    return gaze_x, gaze_y

def map_gaze_to_screen(gaze_x, gaze_y, frame_w, frame_h):
    screen_x = screen_w * gaze_x
    screen_y = screen_h * gaze_y
    return screen_x, screen_y

while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark
        left_eye, right_eye = get_eye_landmarks(landmarks)
        
        # Calculate pupil centers
        left_pupil_center = calculate_pupil_center(left_eye)
        right_pupil_center = calculate_pupil_center(right_eye)

        # Calculate gaze direction
        gaze_x, gaze_y = calculate_gaze_direction(left_pupil_center, right_pupil_center)

        # Map gaze to screen coordinates
        screen_x, screen_y = map_gaze_to_screen(gaze_x, gaze_y, frame_w, frame_h)
        pyautogui.moveTo(screen_x, screen_y)

        # Draw circles around the pupils
        cv2.circle(frame, (int(left_pupil_center[0] * frame_w), int(left_pupil_center[1] * frame_h)), 5, (0, 255, 0), 2)
        cv2.circle(frame, (int(right_pupil_center[0] * frame_w), int(right_pupil_center[1] * frame_h)), 5, (0, 255, 0), 2)

        # Draw a line indicating the gaze direction
        cv2.line(frame, (int(left_pupil_center[0] * frame_w), int(left_pupil_center[1] * frame_h)), (int(right_pupil_center[0] * frame_w), int(right_pupil_center[1] * frame_h)), (0, 0, 255), 2)

        # Check for gaze-based clicks (e.g., if gaze is in a certain region of the screen)
        # For example, you could define a region on the screen where a click should occur
        if 0 < gaze_x < 0.1 and 0.4 < gaze_y < 0.6:
            pyautogui.click()
            pyautogui.sleep(1)

    # Display the frame with the gaze direction (optional)
    cv2.imshow('Gaze Detection', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the webcam and close windows
cam.release()
cv2.destroyAllWindows()