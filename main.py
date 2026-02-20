import json
import requests

def sendmessage(content: str, name: str, url: str):
    """
    Send the message to the weburl.
    :param content: the message-content.
    :param name: the name, the bod should show in the discord message
    :param url: the url, of the discord webhook
    """
    data = {
        "content": content,
        "username": name
    }
    requests.post(url, data=data)

def decode(message: str):
    """
    decode the message in the config.json file.
    :param message: the message to decode
    :return: first and second half of the message
    """
    list = message.split("<")
    firsthalf = list[0]
    secondlist = list[1].split(">")
    secondhalf = secondlist[1]
    return firsthalf, secondhalf

def main():
    with open("/opt/pubipdiscord/config.json", "r") as f:
        config = json.load(f)
    weburl = config["webURL"]
    username = config["bot_username"]
    ip = requests.get("https://api.ipify.org").text
    first, second = decode(config["message"])
    content = f"{first} {ip} {second}"
    try:
        sendmessage(content, username, weburl)
    except:
        print("[ERROR]: url or message is in wrong format. Please look in your config file!")

if __name__ == "__main__":
    main()