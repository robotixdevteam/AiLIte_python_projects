
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import requests

def get_ultrasonic_value():
    ultrasonic_url = f"http://192.168.{bot_num}.10/?cmd=US"
    response = requests.get(ultrasonic_url)
    if response.status_code == 200:
        try:
            return int(response.text)
        except ValueError:
            return None
    return None 

bot_num = input("Enter bot number : ")
host_bot="192.168."+bot_num+".10"
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("RED_GREEN.h5", compile=False)

# Load the labels
class_names = open("RED_GREEN_labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

while True:
    
    ultrasonic_value = get_ultrasonic_value()
        
    if ultrasonic_value is not None and ultrasonic_value < 15:
        requests.get(f"http://{host_bot}/?cmd=b(200)")
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height, 224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the model's input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()  # Strip any extra whitespace
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    if class_name[2:] == "GREEN":
        #print("go")
        requests.get(f"http://{host_bot}/?cmd=f")
    elif class_name[2:] == "RED":
        #print("stop")
        requests.get(f"http://{host_bot}/?cmd=s")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
    print("hi " + class_name[2:])

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
