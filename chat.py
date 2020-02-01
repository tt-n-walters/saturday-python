import requests
from datetime import datetime

url = "https://pythonavanzado.techtalents.cloud/chat/"
data = {
    "name": "Nico"
}
requests.post(url + "register", data=data)



def send(message, name, url, time):
    if len(name) > 0 and len(name) < 20 and len(message) > 0 and len(message) < 200:
        data = {
            "name": name,
            "message": message,
            "time": time
        }
        result = requests.post(url, data=data)
        if not result.text == "Message sent.":
            print(result.text)


def receive(url):
    result = requests.get(url)
    if result.status_code == 200:
        print(result.text)


while True:
    message = input()
    time = "{:02}:{:02}".format(datetime.now().hour, datetime.now().minute - 5)
    send(message, data["name"], url + "send", time)

    receive(url + "messages")
