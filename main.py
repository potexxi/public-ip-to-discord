import json
from requests import post
import public_ip

username = ""
webURL = ""

def sendmessage(content: str):
    """
    Send the message to the weburl.
    :param content: the message-content.
    """
    data = {
        "content": content,
        "username": username
    }
    post(webURL, data=data)

def main():
    with open("config.json", "r") as f:
        config = json.load(f)
    webURL = config["webURL"]
    username = config["bot_username"]
    ip = public_ip.get()
    content = f"Server-IP: {ip} \n\n@everyone"
    sendmessage(content)

if __name__ == "__main__":
    main()