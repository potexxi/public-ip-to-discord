
from requests import post
import public_ip

username = "IP-Bot"
webURL = "https://discordapp.com/api/webhooks/1474316366969569438/Warc3c07OSlvEahKQgTNfWJlBloYkIa1XiJalhN7LyouSJEOrAdJFDhyjiy02XivY93T"

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
    ip = public_ip.get()
    content = f"Server-IP: {ip} \n\n@everyone"
    sendmessage(content)

if __name__ == "__main__":
    main()