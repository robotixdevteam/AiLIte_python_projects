Bot Control Quiz Script:

This Python script conducts a simple quiz and controls a robot over a network based on the user's answers. It sends HTTP requests to move the robot forward or backward depending on the user's responses.

Features:

Simple quiz with three questions.
Sends HTTP GET requests to control the robot's movements.
Moves the robot forward for a correct answer and backward for an incorrect answer.
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

2.You can answer question what will reply with correct answer.