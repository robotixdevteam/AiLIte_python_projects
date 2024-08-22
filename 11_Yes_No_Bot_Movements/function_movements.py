import requests
bot_num = input("Enter bot number : ")
host_bot="192.168."+bot_num+".10"
def yes():
    requests.get(f"http://{host_bot}/?cmd=f(500)")
    
def no():
    requests.get(f"http://{host_bot}/?cmd=b(500)")
a_1=input("Is the sky blue ? y or n : ")

if a_1=="y":
    print("Correct Answer")
    yes()
else:
    print("Wrong Answer")
    no()



a_2=input("Does sun rises in west ? y or n : ")

if a_2=="n":
    print("Correct Answer")
    yes()
else:
    print("Wrong Answer")
    no()


a_3=input("Does tiger eats grass ? y or n : ")

if a_3=="n":
    print("Correct Answer")
    yes()
else:
    print("Wrong Answer")
    no()
    

    
          