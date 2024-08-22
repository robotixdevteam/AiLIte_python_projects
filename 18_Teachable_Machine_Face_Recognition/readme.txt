# Facial Recognition Control System

This Python script utilizes a deep learning model to recognize faces through a webcam feed and controls a device based on the recognized individual. It's designed to interact with a remote device by sending HTTP requests to trigger actions like moving forward or backward.

## Prerequisites

To run this script, ensure you have the following installed:
- Python 3.x
- TensorFlow (includes Keras)
- OpenCV
- Requests library
- A pre-trained TensorFlow Keras model named 'TM_FACE.h5'
- A text file 'TM_FACE_labels.txt' containing labels for the trained model

Both the above files should be downloaded from teachable machine after training the model

You can install the necessary Python packages using the following command:

`TM_FACE.h5` - The trained model file.
`TM_FACE_labels.txt` - The labels file containing the class names.


## Installation

1. Clone this repository:

   git clone <repository-url>

2. Create a separate Miniconda environment with Python 3.11 in the respective file path for each program:
    
   conda create -n <environment-name> python=3.11 -y

3. Activate the environment:
   
   conda activate <environment-name>

4.Navigate to the directory of this program and install the required Python packages:

 pip install -r requirements.txt

[Before you run the program make sure bot is connected]

1.Run the Python script:

  python file_name.py

2.Bot Will move based on Face detected Detected.

3.Depending on the face recognized, the bot will move forward or backward. The commands sent are as follows:

If "User_1" is recognized, the bot will move forward.
If "User_2" is recognized, the bot will move backward.

To exit the script, press the q key while the webcam window is active.