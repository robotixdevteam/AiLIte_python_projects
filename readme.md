# AiLite
<p align="center" width="80%">
    <img width="40%" src="./Images/cvpro.png" />
</p>

AILite is a cutting-edge autonomous robot designed for a wide range of applications. With its sophisticated four-wheel drive system, integrated camera, ultrasonic sensors, IR sensor, color sensor, and touch sensor, AILite is capable of navigating complex environments with precision and intelligence. 

## Get the source code

- You can download the repository as a [zip file](https://github.com/vishnuj1999/AiLIte_python_projects/archive/refs/heads/main.zip) and extract it into a folder of your choice.
- You can clone the AiLite repository from GitHub with the following command:

    ```bash
    git clone https://github.com/vishnuj1999/AiLIte_python_projects.git
    ```
 

# Connection

## How to Set up the Local Connection:

1. First, turn on wifi in Laptop/PC.

2. Turn on the AiLite bot, that acts as the hotspot. Establish connection by entering the `WiFi-Name = 'AILITE-<unique-ID>' (for example, 'AILITE-1034')` and `Wifi-Password = '123456789'`.

3. Accessing Unique URL for each AiLite Bot:

- In web browser kindly enter the below url for accessing AiLite bot in web url.

        
        192.168.{bot_number}.10
        
  -For example 'AILITE-1034' here inverse of last two number is the bot number

        
        192.168.43.10
        

## You first need to setup your environment.

## Dependencies

We recommend to create a conda environment for AiLIte. Instructions on installing conda can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/). The easiest way to create a new environment with all dependencies is to use one of the provided environment files. 
Make sure it you create conda environmen and download requirements.txt in the projects folder path.
### Environment Setup

First create a new conda environment with the following command:

```bash
conda create -n <environment_name> python=3.11 -y
```

Next, you need to activate your conda environment:

```bash
conda activate <environment_name>
```

Once your environment is active, need to install requirements for each projects

#### **Windows**
```
pip install -r requirements.txt
```
#### **Linux**
```
pip install -r requirements.txt
```

#### **Mac**
```
pip install -r requirements.txt
```
### Notes

- Remember to activate the environment, before you execute your python programs. Give the below command to run python program.

```bash
python <script_name.py>
```

# Below is a list of all the projects included in this repository.

# 1. Object Detection 

This project is designed to detect and recognize traffic signs using YOLO (You Only Look Once) object detection and then control a bot accordingly based on the detected sign.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/1_Object_Detection)

# 2. Text Recognition 

This program utilizes OCR (Optical Character Recognition) to detect text from a webcam feed and control a bot accordingly. It can recognize commands like "go" and "stop" and send corresponding signals to a specified IP address.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/2_Text_Recognition)

# 3. Gesture Recognition 

This script utilizes the Mediapipe library to perform hand gesture recognition using a webcam feed. It detects various hand gestures and sends corresponding commands to a specified host.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/3_Gesture_Recognition)

# 4. Face Motion Detection 

This script utilizes MediaPipe's Face Mesh model to estimate the pose of a person's head using their nose tip landmark. Based on the head pose, it sends corresponding commands to a specified host, allowing for head-controlled actions.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/4_Face_Motion_Detection)

# 5. Face Recognition 

This script performs face recognition using the DeepFace library and grants access based on the recognized faces. If a face in the captured frame matches any of the reference images, access is granted and commands can be triggered using keyboard inputs.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/5_Face_Recognition)

# 6. Remote Control 

This script allows you to control a bot using keyboard inputs. You can use arrow keys to move the bot in different directions and the space key to stop it. Press 'ESC' to exit the program.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/6_Remote_Control)

# 7. Speech Recognition 

This script allows you to control a bot using voice commands. You can give commands such as "turn right", "turn left", "go forward", or "go backward" using your microphone.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/7_Speech_Recognition)

# 8. Face Emotion Detection 

This project is an emotion detection system using a webcam and a trained deep learning model. The detected emotions trigger specific HTTP requests to control a robot.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/8_Face_Emotion_Detection)

# 9. Tic Tac Toe 

This project implements a simple Tic Tac Toe game with a graphical user interface (GUI) using the Tkinter library in Python. The game allows a human player to play against the computer.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/9_Tic_Tac_Toe)

# 10. Normal Movements 

This Python script allows you to control a robot over a network using simple HTTP requests. You can send commands to move the robot forward, backward, left, or right.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/10_Normal%20_Movements)

# 11. Yes No Bot Movements 

This Python script conducts a simple quiz and controls a robot over a network based on the user's answers. It sends HTTP requests to move the robot forward or backward depending on the user's responses.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/11_Yes_No_Bot_Movements)

# 12. Stone Paper Scissors 

This Python script implements a Stone Paper Scissors game using a graphical user interface (GUI) with Tkinter. The game includes functionality to control a robot over a network based on the computer's choice using HTTP requests.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/12_Stone_Paper_Scissors)

# 13. Speed Control 

This Python script allows you to control a robot over a network using keyboard inputs. It sends HTTP GET requests to move the robot forward, backward, left, or right, and allows you to adjust the speed. The script also includes functionality to stop the robot and exit the program.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/13_Speed_Control)

# 14. Obstacle Avoider Using IR 

This Python script allows you to control a robot over a network using data from infrared (IR) sensors. It sends HTTP GET requests to navigate the robot based on the sensor data received.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/14_Obstacle_Avoider_Using_IR)

# 15. Object Detection 

This Python script allows you to control a robot using data from an ultrasonic (US) sensor. It sends HTTP GET requests to the robot to navigate it based on the sensor data received.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/15_Obstacle_Following_Using_UR)

# 16. Multiple Face Recognition 

This script performs face recognition using the DeepFace library and grants access based on the recognized faces. If a face in the captured frame matches any of the reference images, access is granted and commands can be triggered using keyboard inputs.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/16_Multiple_Face_Recognition)

# 17. Teachable Machine Color Recognition 

This project uses a neural network model to control a robot based on the detected color of a traffic light in a webcam feed. If the model detects a "GREEN" light, it sends a command to the robot to move forward. If the model detects a "RED" light, it sends a command to the robot to stop.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/17_Teachable_Machine_Color_Recognition)

# 18. Teachable Machine Face Recognition 

This Python script utilizes a deep learning model to recognize faces through a webcam feed and controls a device based on the recognized individual. It's designed to interact with a remote device by sending HTTP requests to trigger actions like moving forward or backward<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/18_Teachable_Machine_Face_Recognition)

# 19. Survilence Bot 

This script allows you to control a bot using keyboard inputs. You can use arrow keys to move the bot in different directions and the space key to stop it. Press 'ESC' to exit the program.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/19_Survilence_Bot)

# 20. AiLite Chatbot 

This Python application allows users to control a robot through voice commands, leveraging advanced speech recognition and decision-making model integration. It is particularly designed for interactive scenarios where voice input can dictate robot actions.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/20_AiLite_Chatbot)

# 21. Binar Digits 

This Python script allows you to control a robot using data from Touch sensor. It sends HTTP GET requests to the robot to navigate it based on the sensor data received.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/21_Binar_Digits)
# 22. Morse code 

This Python script allows you to control a robot using data from Touch sensor. It sends HTTP GET requests to the robot to navigate it based on the sensor data received.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/22_Morse_code)

# 23. Pattern Drawing 

This Python script allows bot to draw a pattern. It sends HTTP GET requests to the robot to navigate it based on the sensor data received.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/23_Pattern_Drawing)

# 24. Go Stop 

This Python script allows you to control a robot using data from Color sensor. It sends HTTP GET requests to the robot to navigate it based on the sensor data received.<br>
[Click here to know more](https://github.com/vishnuj1999/AiLIte_python_projects/tree/main/24_Go_Stop)


**Note: Avoid pasting the compressed files directly. Make sure to extract the files first.**

## Training Process

Make sure your conda environment for CVPRO is activated by executing the following command:

```bash
conda activate cvpro
```

The training process can be visualised either in Python script or in jupyter notebook:

- To start in the Python script, navigate to the folder, `Training_Process` within your local `Meritus-CVPRO` repository. Type or paste the following command in Anaconda Prompt,

```bash
python main.py
``` 

- To visualize the same using Jupyter notebook, you can use jupyter notebook file "**main.ipynb**". Type or paste the following command in Anaconda Prompt,

```bash
jupyter notebook main.ipynb
```

After training process is complete, the script will generate three files (_best.tflite, last.tflite and label.txt_). The files are saved in the location `Training_Process -> Training_Data -> Save_Model`.

Copy/Move the above three files from computer to smartphone to the folder of your choice.

## Model Management

To upload the model, Open the _CV PRO_ Application in your smartphone and go to `Settings`:gear: icon. Tap on the `Model management` section and click the `upload file` button, select the "***best.tflite*** or ***last.tflite***" from the saved location. 

After the file is uploaded, a menu will appear at the bottom of the screen. From there, you can _change the model's name_ and choose the category in which you want to place the model, from the list of categories displayed. To upload the `label.txt` text file, simply tap on the :paperclip: icon and tap on `Submit` button.

Go to home Screen in _CV PRO_ Application, choose an option among the menu,
- Click the **Autonomous Driving** to run on autonomous mode.
- Click the **Image Classification** to classify the image.
- Click the **Object Detection** to follow an object from the list of objects.


# Mecanum
<p align="center" width="100%">
    <img width="100%" src="./Images/cvpro-mecanum.png" />
</p>

# CV Pro with Mecanum Wheels

CV Pro is now equipped with the new feature: **`Mecanum wheels`**. Swap the existing wheels with the Mecanum wheels provided. These omnidirectional wheels can move in any direction, offering incredible maneuverability.

## Connection

## How to Setup the Local Server Connection
1. Ensure that computer is within proximity and turn-on the CV Pro bot, that acts as the hotspot and check if unique ID of your bot is displayed in the WiFi connection. Establish connection by entering the `WiFi-Name = 'cvpro<unique-ID>' (for example, 'cvpro0123')` and `Wifi-Password = '12345678'`.

2. Initiating server:

- For `Windows`, navigate to the folder where the mosquitto package is installed (`C:\ProgramFiles\Mosquitto`). Copy the configuration file, `mqtt_conf.conf` from the `Environment_Setup` folder in local Meritus-CVPRO repository and paste into the Mosquitto installation folder. Open the Command-Prompt/Terminal from this folder. 

    - Type or paste following command and your server will start. 

        ```bash
        mosquitto -v -c .\mqtt_conf.conf
        ```

- For `Linux/Ubuntu`, you need not navigate to the installed path or copy the configuration file. Just launch the Terminal,

    - command >> cd '_path to the_ **mqtt_conf.conf** _file which is present in downloaded local `Meritus-CVPRO` repository in folder `Environment_Setup`_'.

    - Type or paste following command and your server will start. 

        ```bash
        mosquitto -v -c mqtt_conf.conf
        ```

- For `Mac`, you need not navigate to the installed path or copy the configuration file. Just launch the Terminal,

    - command >> cd '_path to the_ **mqtt_conf.conf** _file which is present in downloaded local `Meritus-CVPRO` repository in folder `Environment_Setup`_'.

    - Type or paste following command and your server will start.  

        ```bash
        mosquitto -v -c mqtt_conf.conf
        ```

3. Navigate to the `...\Meritus-CVPRO-main\Controller` directory, from your Anaconda prompt.

4.	To activate your environment,
- For **Windows**, Open the Anaconda Prompt,

    ```bash
    conda activate cvpro
    ```

- For **Linux/Ubuntu**, Open the Terminal,

    ```bash
    conda activate cvpro
    ```

- For **Mac**, Open the Terminal, 

    ```bash
    conda activate cvpro
    ```
**Note:** If you receive message `EnvironmentNameNotFound`, after this step, create and activate the environment, by following steps in [Dependencies](#Dependencies).

5.	In Anaconda prompt, run the following command to set your kit in motion:

    ```bash
    python mecanum_control_bot.py
    ```

6.	A pygame controller window will appear on your computer screen, allowing you to control your robot using the key combinations provided. Observe your kit's smooth, multidirectional movement.

With CV Pro's new Mecanum wheels, you have expanded possibilities for hands-on learning.


## Contact

- Contact us via [Email](mailto:development@merituseducation.com)





