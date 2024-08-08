Face Mesh Cursor Control:
This project uses computer vision and machine learning techniques to control the mouse cursor using facial landmarks detected through a webcam. By leveraging the MediaPipe library for face mesh detection and PyAutoGUI for cursor control, the program allows hands-free mouse movement and clicking based on facial gestures.

Features:
Cursor Control: Move the mouse cursor by tracking facial landmarks.

Clicking Mechanism: Automatically click when specific facial gestures are detected.

Webcam Integration: Real-time facial landmark detection using the device's webcam.

Frame Capture: Periodic frame capture for debugging purposes.

Technologies Used:

OpenCV: For capturing and processing video frames.

MediaPipe: For detecting facial landmarks.

PyAutoGUI: For simulating mouse movements and clicks.
How It Works:
The program initializes the webcam and begins capturing video frames.
MediaPipe's Face Mesh module is used to detect facial landmarks.
Specific landmarks are tracked to control the mouse cursor's position on the screen.
The program detects eye movements to simulate mouse clicks.
Frames are periodically saved for debugging, and the loop runs for a fixed number of frames.
Usage:

To use this project, ensure you have a webcam connected and the required libraries installed. Run the script, and the webcam feed will start. Move your head to control the cursor, and blink to click.
