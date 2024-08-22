
import requests
import speech_recognition as sr
import time
import http.client
bot_num = input("Enter bot number : ")
host="192.168."+bot_num+".10"
port = 80

def send_re_httpquest(host, port, path):
    """Send HTTP request with retries."""
    retries = 10  # Number of retries
    for _ in range(retries):
        conn = None
        try:
            conn = http.client.HTTPConnection(host, port)
            conn.request("GET", path)
            response = conn.getresponse()
            data = response.read().decode("utf-8")
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            if _ < retries - 1:
                time.sleep(1)
        finally:
            if conn:
                conn.close()
    return None  # Return None if all retries fail


def act_yes():
  path1=f"/?cmd=f(500)"
  send_re_httpquest(host, port, path1)
  path2=f"/?cmd=b(500)"
  send_re_httpquest(host, port, path2)
  
def act_no():
  path3=f"/?cmd=r(500)"
  send_re_httpquest(host, port, path3)
  path4=f"/?cmd=l(1000)"
  send_re_httpquest(host, port, path4)
  path5=f"/?cmd=r(500)"
  send_re_httpquest(host, port, path5)

# Initialize recognizer class
recognizer = sr.Recognizer()

# Capture data from the microphone
with sr.Microphone() as source:
    print("Say something!")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio_data = recognizer.listen(source)
    try:
        # Recognize speech using Google Web Speech API
        question = recognizer.recognize_google(audio_data) #Comment it out for text input
        print("You said: " + question)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

API_URL = "https://api-inference.huggingface.co/models/google/gemma-1.1-7b-it"
headers = {"Authorization": "Bearer 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"}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
#questions=input("Question: ")
questions=question +" Yes or NO "
output = query({
    "inputs": questions,
    "parameters": {
        "role": "you are chat assistant",  # Add the desired role here
        "temperature": 0.1   # Set the temperature for generation
    }
})
text = output[0]['generated_text']
text = text.replace('\n', ' ')
parts = text.split("Answer")
parts1_upper = parts[1].upper()
count_yes = parts1_upper.count("YES")
count_no = parts1_upper.count("NO")

if count_yes >= 1:
    print("Yes")
    act_yes()

elif count_no >= 1:
    answer="No"
    print("No")
    act_no()