Bot Control with Keyboard:

This Python script allows you to control a robot over a network using keyboard inputs. It sends HTTP GET requests to move the robot forward, backward, left, or right, and allows you to adjust the speed. The script also includes functionality to stop the robot and exit the program.

Features:

Control the robot using arrow keys.
Adjust the robot's speed using 'l' (low), 'm' (medium), and 'h' (high) keys.
Stop the robot using the space bar.
Exit the program using the 'ESC' key.
Prerequisites
Python 3.6 or higher
Requests library
Keyboard library


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

2.Bot Will move based on inputs.