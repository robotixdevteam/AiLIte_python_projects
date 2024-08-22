# Object Detection

## Description

This project is designed to detect and recognize traffic signs using YOLO (You Only Look Once) object detection and then control a bot accordingly based on the detected sign.

## Requirements

- Python 3.11 (It is suggested to create a separate Miniconda environment for each program)
- OpenCV
- Requests
- Ultralytics
- YOLOv5

## Installation
**Connect the bot with wifi**
1. Clone this repository:

   git clone <repository-url>

2. Create a separate Miniconda environment with Python 3.11 in the respective file path for each program:
    
   conda create -n <environment-name> python=3.11 -y

3. Activate the environment:
   
   conda activate <environment-name>

4. Navigate to the directory of each program and install the required Python packages:
   
   pip install -r requirements.txt
5. Ensure you have a webcam connected and working properly for real-time sign detection.

## Usage

1.Run the Python script:

  python file_name.py

2.The script will initiate your webcam and start detecting traffic signs in real-time.

3.When a sign is detected, the bot will be controlled accordingly based on the detected sign.

4.Press 'q' to quit the application.



##Configuration

intervel: Delay in seconds between bot movements.
host: Replace this with your bot's IP address.
cam_host: Replace this with your webcam's IP address.
bb_size: Size of the bounding box for detection.
turn_delay: Delay in milliseconds for turning the bot.
D90_turn_delay: Delay in milliseconds for a 90-degree turn.
speed_val: Speed value for bot movement.
pwm_corr: PWM correction value for balancing bot speed.


