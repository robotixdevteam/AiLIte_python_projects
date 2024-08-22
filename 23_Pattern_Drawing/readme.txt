Pattern Drawing Robot:

This Python script allows bot to draw a pattern. It sends HTTP GET requests to the robot to navigate it based on the sensor data received.

Features:

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