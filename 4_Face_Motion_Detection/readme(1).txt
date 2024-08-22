# Head Pose Estimation with MediaPipe

This script utilizes MediaPipe's Face Mesh model to estimate the pose of a person's head using their nose tip landmark. Based on the head pose, it sends corresponding commands to a specified host, allowing for head-controlled actions.

## Prerequisites

- Python 3.11
- Miniconda (optional but recommended for managing environments)
- Webcam (for real-time head pose estimation)
- MediaPipe library
- OpenCV
- Requests library

## Installation

1. Clone this repository:

   git clone <repository-url>

2.Create a separate Miniconda environment with Python 3.11 in the respective file path for this program:

 conda create -n <environment-name> python=3.11 -y

3.Activate the environment:
 
 conda create -n <environment-name> python=3.11 -y

4.Navigate to the directory of this program and install the required Python packages:

 pip install -r requirements.txt

5.Make sure your webcam is connected and working properly.

## Usage

1.Run the Python script:

 python file_name.py

2.The script will open your webcam feed and estimate the pose of your head..

3.Depending on the detected head pose, corresponding commands will be sent to the specified host.

4.Press 'q' to quit the application.


## Configuration

host_bot: Replace this with the IP address of your bot.


Supported Head Poses
The script is trained to recognize the following head poses:

Center: Head facing directly forward
Left: Head turned to the left
Right: Head turned to the right
Upward: Head tilted upward
Downward: Head tilted downward

Acknowledgments
MediaPipe: MediaPipe Documentation
OpenCV: OpenCV Documentation
Python Requests Library: Requests