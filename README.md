
# Gaze Detection Using OpenCV, MediaPipe, and PyAutoGUI

This project demonstrates a gaze detection system that uses OpenCV, MediaPipe, and PyAutoGUI to track where a user is looking and interact with the computer accordingly. The system detects eye landmarks and calculates the gaze direction to control the mouse cursor and perform clicks based on where the user is gazing.


## Features

- Move the mouse cursor by tracking facial landmarks.
- Automatically click when specific facial gestures are detected.
- Displays circles around the pupils and a line indicating the gaze direction
- Moves the mouse cursor according to the detected gaze direction


## Requirements
- Python 3.x
- OpenCV: For video capture and image processing.
- MediaPipe: For detecting facial landmarks.
- PyAutoGUI: For controlling the mouse cursor.
- NumPy: For numerical operations.



## Installation

Install the requriements with pip

```pip
  pip install opencv-python mediapipe pyautogui numpy
```


## Usage 
- Run the Script: Execute the Python script to start the gaze detection system.
- Webcam Feed: The script will open a window displaying the webcam feed.
- Mouse Control: The mouse cursor will move according to the detected gaze direction.
- Click Interaction: The script will perform clicks if the gaze is within a specified region of the screen.
- Exit: Press Esc to close the application.

## Notes 
- Ensure that your webcam is properly connected and accessible
- The pyautogui library requires appropriate permissions to control the mouse cursor
- Verify that all dependencies are installed and compatible with your Python version
