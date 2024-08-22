# Text Recognition

## Description

This program utilizes OCR (Optical Character Recognition) to detect text from a webcam feed and control a bot accordingly. It can recognize commands like "go" and "stop" and send corresponding signals to a specified IP address.

## Requirements

- Python 3.11 (It is suggested to create a separate Miniconda environment for this program)
- EasyOCR
- OpenCV
- Requests

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

2.The script will open your webcam feed and display the recognized text on the screen.

3.If the recognized text contains "go", "right", "left", or "stop", the corresponding command will be sent to the specified IP address.

4.Press 'q' to quit the application.


## Configuration

host_bot: Replace this with the IP address of your bot.


Acknowledgments
EasyOCR: EasyOCR Documentation
OpenCV: OpenCV Documentation
Python Requests Library: Requests
