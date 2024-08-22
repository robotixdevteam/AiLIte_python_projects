import requests
bot_num = input("Enter bot number : ")
host_bot="192.168."+bot_num+".10"

print("Forward - f | Backward - b | Left - l | Right - r")
i=input("Give Movements : ")
requests.get(f"http://{host_bot}/?cmd={i}(1000)") 