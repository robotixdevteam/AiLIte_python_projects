import time
import http.client

bot_num = input("Enter bot number: ")
host = "192.168." + bot_num + ".10"
port = 80
us_path = "/?cmd=t"
time.sleep(2)  # Wait for 5 seconds before the next iteration

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

# Run the loop for a specified duration (e.g., 1 minute)

#f = 0010

#b = 1000

#l = 0100

#r = 0101

#d = 1001

movements = ""


duration = 3  # Total duration in seconds
start_time = time.time()

while time.time() - start_time < duration:
    touch_value = send_re_httpquest(host, port, us_path)
    if touch_value == "Not Detected":
        value = 0
        movements = movements + str(value)
    else:
        value = 1
        movements = movements + str(value)   
    print(value)
    time.sleep(2)  # Wait for 5 seconds before the next iteration
print(movements)
if movements == "00":
    path=f"/?cmd=f(500)"
    send_re_httpquest(host, port, path)
elif movements == "01":
    path=f"/?cmd=b(500)"
    send_re_httpquest(host, port, path)
elif movements == "10":
    path=f"/?cmd=l(500)"
    send_re_httpquest(host, port, path)
elif movements == "11":
    path=f"/?cmd=r(500)"
    send_re_httpquest(host, port, path)