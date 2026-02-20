
from requests import post
import public_ip

username = "IP-Bot"
webURL = "https://discordapp.com/api/webhooks/1474316366969569438/Warc3c07OSlvEahKQgTNfWJlBloYkIa1XiJalhN7LyouSJEOrAdJFDhyjiy02XivY93T"

def sendmessage(content: str):
    data ={
        "content": content,
        "username": username
    }
    post(webURL, data=data)

def main():
    ip = public_ip.get()
    sendmessage(ip)

if __name__ == "__main__":
    main()