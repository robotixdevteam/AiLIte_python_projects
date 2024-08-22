# Emotion Detection

## Description

This project is an emotion detection system using a webcam and a trained deep learning model. The detected emotions trigger specific HTTP requests to control a robot.

The program performs the following steps:

Captures video feed from the webcam.
Detects faces in the video feed using OpenCV's Haar Cascade classifier.
For each detected face, predicts the emotion using a pre-trained TensorFlow model.
Sends specific HTTP requests based on the detected emotion to control a robot.
The program supports three emotions:

Happy: Sends a command to move the robot forward.
Sad: Sends a command to move the robot backward.
Neutral: Sends a command to stop the robot.


## Requirements

- Python 3.11 (It is suggested to create a separate Miniconda environment for each program)
- OpenCV
- Requests

## Installation

1. Clone this repository:

   git clone <repository-url>

2. Create a separate Miniconda environment with Python 3.11 in the respective file path for each program:
    
   conda create -n <environment-name> python=3.11 -y

3. Activate the environment:
   
   conda activate <environment-name>

4. Navigate to the directory of each program and install the required Python packages:
   
   pip install -r requirements.txt

5. Ensure you have a webcam connected and working properly for real-time Face detection.

6.Ensure you have the trained model file (emotion_detection_model.h5) in the same directory as the script.

7.Ensure you have the haarcascade_frontalface_default.xml in the same directory as the script.

## Usage

[Before you run the program make sure bot is connected]

1.Run the Python script:

  python file_name.py

2.The script will initiate your webcam and start detecting Faces in real-time.

3.When an emotion is detected, the bot will be controlled.

4.Press 'q' to quit the application.

