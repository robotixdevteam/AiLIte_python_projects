Bot Control Using Infrared Sensors:

This Python script allows you to control a robot over a network using data from infrared (IR) sensors. It sends HTTP GET requests to navigate the robot based on the sensor data received.

Features:

Fetch IR sensor data from the robot.
Navigate the robot based on the IR sensor readings:
Turn right if the left sensor is triggered.
Turn left if the right sensor is triggered.
Move backward and then turn right if both sensors are triggered.
Retries HTTP requests up to 10 times if they fail.
Prerequisites
Python 3.6 or higher
An active internet connection
A robot with a web server interface that responds to specific commands


## Installation

1. Clone this repository:

   git clone <repository-url>

2. Create a separate Miniconda environment with Python 3.11 in the respective file path for each program:
    
   conda create -n <environment-name> python=3.11 -y

3. Activate the environment:
   
   conda activate <environment-name>

[Before you run the program make sure bot is connected]

1.Run the Python script:

  python file_name.py

2.Bot Will move based on IR Value.