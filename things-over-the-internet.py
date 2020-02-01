import requests

if False:
    result = requests.get("https://www.bensound.com/bensound-music/bensound-summer.mp3")

    if result.status_code == 200:
        data = result.content

        with open("audio.mp3", "wb") as file:
            file.write(data)
if False:
    my_data = {
        "position": 666665
    }

    requests.get("http://192.168.20.144:8000", params=my_data)



result = requests.get("https://pythonavanzado.techtalents.cloud/file.txt")
if result.status_code == 200:
    print(len(result.text))
    random_data = result.text

    my_data = {
        "position": data.find("python")
    }

    requests.get("http://192.168.20.144:8000", params=my_data)
