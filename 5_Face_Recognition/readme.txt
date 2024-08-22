# Face Recognition Access Control System

This script performs face recognition using the DeepFace library and grants access based on the recognized faces. If a face in the captured frame matches any of the reference images, access is granted and commands can be triggered using keyboard inputs.

## Prerequisites

- Python 3.11
- Miniconda (optional but recommended for managing environments)
- Webcam (for real-time face recognition)
- DeepFace library
- OpenCV
- Requests library
- Keyboard library

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

**Place your reference images in the same directory as the script and update the reference_images list with their filenames.**

1.Run the Python script:

 python file_name.py

2.The script will open your webcam feed and attempt to recognize faces.

3.If a recognized face matches any of the reference images, access will be granted, and you can trigger commands using the keyboard inputs.

4.Press and hold the 'up' arrow key to trigger a GET request. Press 'ESC' to exit the program.


## Configuration

host_bot: Replace this with the IP address of the host where commands will be sent.
Make sure your webcam is working properly and accessible by OpenCV.

##Notes

Ensure that the reference images are properly named and placed in the same directory as the script.
Replace the images in the reference_images list with your own images.

##Acknowledgments

DeepFace: DeepFace Documentation
OpenCV: OpenCV Documentation
Python Requests Library: Requests
Keyboard Library: Keyboard