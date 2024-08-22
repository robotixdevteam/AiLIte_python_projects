# AiLite ChatBot

This Python application allows users to control a robot through voice commands, leveraging advanced speech recognition and decision-making model integration. It is particularly designed for interactive scenarios where voice input can dictate robot actions.

## Features

- Voice command recognition to interpret user inputs.
- Integration with Hugging Face's decision-making model to process and act on commands.
- Direct robot control through HTTP requests based on voice commands.
- Error handling and retry mechanisms for robust connection and control.

## Requirements

- Python 3.x
- SpeechRecognition
- Requests
- HTTP client


## Installation

1. Clone this repository:

   git clone <repository-url>

2.Create a separate Miniconda environment with Python 3.11 in the respective file path for this program:

 conda create -n <environment-name> python=3.11 -y

3.Activate the environment:
 
 conda activate <environment-name>

4.Navigate to the directory of this program and install the required Python packages:

 pip install -r requirements.txt


## Usage
[Before you run the program make you sure u have internet connection as well as you are connected with bot.Ethernet connection is suggested]

1.Run the Python script:

 python file_name.py

2.Bot will respond to you question with actions.