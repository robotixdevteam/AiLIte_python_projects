Traffic Light Detection Robot Control:

This project uses a neural network model to control a robot based on the detected color of a traffic light in a webcam feed. If the model detects a "GREEN" light, it sends a command to the robot to move forward. If the model detects a "RED" light, it sends a command to the robot to stop.


Prerequisites:

Python 3.6 or higher
TensorFlow (required for Keras)
OpenCV
Requests library
A trained model (RED_GREEN.h5)
Corresponding labels file (RED_GREEN_labels.txt)
Both the above files should be downloaded from teachable machine after training the model

Ensure that you have the following files in your working directory:

RED_GREEN.h5 - The trained model file.
RED_GREEN_labels.txt - The labels file containing the class names.


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

2.Bot Will move based on Color Detected.