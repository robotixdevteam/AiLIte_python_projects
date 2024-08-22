# Keyboard-Controlled Bot

This script allows you to control a bot using keyboard inputs. You can use arrow keys to move the bot in different directions and the space key to stop it. Press 'ESC' to exit the program.

## Prerequisites

- Python 3.11
- Miniconda (optional but recommended for managing environments)
- Requests library
- Keyboard library

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

**Place your reference images in the same directory as the script and update the reference_images list with their filenames.**

1.Run the Python script:

 python file_name.py

2.Press and hold the 'up' arrow key to move the bot forward. Use other arrow keys for different directions.

3.Press the space key to stop the bot.

4.Press and hold the 'up' arrow key to trigger a GET request. Press 'ESC' to exit the program.


## Configuration

host_bot: Replace this with the IP address of the host where commands will be sent.
Make sure your webcam is working properly and accessible by OpenCV.

##Notes

Make sure the bot is connected and accessible at the specified IP address.
Additional keyboard shortcuts or control commands can be added as needed.
##Acknowledgments

DeepFace: DeepFace Documentation
OpenCV: OpenCV Documentation
Python Requests Library: Requests
Keyboard Library: Keyboard