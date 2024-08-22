import time
import http.client
bot_num = input("Enter bot number: ")
host_bot = "192.168."+bot_num+".10"
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

path = f"/?cmd=l(2000)"
send_re_httpquest(host, port, path)
path = f"/?cmd=f(2000)"
send_re_httpquest(host, port, path)
path = f"/?cmd=l(2000)"
send_re_httpquest(host, port, path)
path = f"/?cmd=f(2000)"
send_re_httpquest(host, port, path)
path = f"/?cmd=l(2000)"
send_re_httpquest(host, port, path)
path = f"/?cmd=f(2000)"
send_re_httpquest(host, port, path)
path = f"/?cmd=l(2000)"
send_re_httpquest(host, port, path)
path = f"/?cmd=f(2000)"
send_re_httpquest(host, port, path)