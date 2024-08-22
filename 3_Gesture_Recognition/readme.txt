Hand Gesture Recognition with Mediapipe
This script utilizes the Mediapipe library to perform hand gesture recognition using a webcam feed. It detects various hand gestures and sends corresponding commands to a specified host.

Prerequisites
Python 3.11
Miniconda (optional but recommended for managing environments)
Webcam (for real-time hand gesture detection)
Mediapipe library
OpenCV
Requests library

## Installation

1. Clone this repository:

   git clone <repository-url>

2.Create a separate Miniconda environment with Python 3.11 in the respective file path for this program:

 conda create -n <environment-name> python=3.11 -y

3.Activate the environment:
 
 conda activate <environment-name>

4.Navigate to the directory of this program and install the required Python packages:

 pip install -r requirements.txt

5.Make sure your webcam is connected and working properly.

## Usage

1.Run the Python script:

 python file_name.py

2.The script will open your webcam feed and display hand gestures recognized in real-time..

3.Depending on the detected gestures, corresponding commands will be sent to the specified host.

4.Press 'q' to quit the application.


## Configuration

host_bot: Replace this with the IP address of your bot.


Supported Gestures
The script is trained to recognize the following hand gestures:

Run: All fingers closed
Stop: All fingers open
Left: Thumb extended to the right with other fingers closed
Right: Thumb extended to the left with other fingers closed

Acknowledgments
Mediapipe: Mediapipe Documentation
OpenCV: OpenCV Documentation
Python Requests Library: Requests