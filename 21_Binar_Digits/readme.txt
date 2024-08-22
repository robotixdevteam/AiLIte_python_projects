Binary digits Robot Control:

This Python script allows you to control a robot using data from Touch sensor. It sends HTTP GET requests to the robot to navigate it based on the sensor data received.

Features:

Fetch Touch sensor data from the robot.
Navigate the robot based on the Touch sensor readings:
Get binary digits values using touch sensor.If touch is detected its 1 or else 0 .
Retries HTTP requests up to 10 times if they fail.
Prerequisites
Python 3.6 or higher
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

2.Bot Will move based on Touch sensor Value.