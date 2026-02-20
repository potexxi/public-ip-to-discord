#!/bin/bash
sudo apt update
sudo apt install python3-requests
sudo apt install python3-pip
sudo pip3 install public-ip
sudo mkdir -p /opt/pubipdiscord
sudo curl -o /opt/pubipdiscord/main.py https://raw.githubusercontent.com/potexxi/public-ip-to-discord/refs/heads/main/main.py
sudo curl -o /opt/pubipdiscord/config.json https://raw.githubusercontent.com/potexxi/public-ip-to-discord/refs/heads/main/config.json
sudo chmod +x /opt/pubipdiscord/main.py
sudo curl -o /etc/systemd/system/pubipdiscord.service https://raw.githubusercontent.com/potexxi/public-ip-to-discord/refs/heads/main/pubipdiscord.service
sudo systemctl daemon-reload
sudo systemctl enable pubipdiscord
echo ""
echo ""
echo ""
echo ""
echo ""
echo "Installation complete."
echo "sudo systemctl start pubipdiscord"
echo "Please go to /opt/pubipdiscord and change the config.json to your discord webhook-url!!!"