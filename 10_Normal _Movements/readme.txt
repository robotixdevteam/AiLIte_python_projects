Bot Control Script:

This Python script allows you to control a robot over a network using simple HTTP requests. You can send commands to move the robot forward, backward, left, or right.

Features:

Interactive input for bot control.
Sends HTTP GET requests to control the robot's movements.
Validates input to ensure correct commands are sent.
Prerequisites
Python 3.6 or higher
Requests library


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

2.Based on your inputs bot performs operations.