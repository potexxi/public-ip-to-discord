#!/bin/bash

sudo mkdir -p /opt/pubipdiscord
sudo curl -o /opt/pubipdiscord/main.py https://github.com/potexxi/public-ip-to-discord/blob/main/main.py
sudo curl -o /opt/pubipdiscord/config.json https://github.com/potexxi/public-ip-to-discord/blob/main/config.json

sudo chmod +x /opt/pubipdiscord/main.py

echo "Installation complete."
echo "Start with: python3 /opt/pubipdiscord/main.py"
echo "Please go to /opt/pubipdiscord and change the config.json to your discord webhook-url!!!"