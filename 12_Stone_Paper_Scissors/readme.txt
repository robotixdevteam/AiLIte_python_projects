Stone Paper Scissors Game with Bot Control:

This Python script implements a Stone Paper Scissors game using a graphical user interface (GUI) with Tkinter. The game includes functionality to control a robot over a network based on the computer's choice using HTTP requests.

Features:

Interactive Stone Paper Scissors game with a GUI.
Sends HTTP GET requests to control the robot based on the computer's choice:
Stone: Move forward
Paper: Move backward
Scissors: Turn right
Highlights the computer's choice.
Ends the game when the player wins 5 times.
Prerequisites
Python 3.6 or higher
Requests library
Tkinter (usually comes pre-installed with Python)


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

2.Bot will play game with you.