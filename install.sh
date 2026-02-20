#!/bin/bash
sudo mkdir -p /opt/pubipdiscord
sudo curl -o /opt/pubipdiscord/main.py https://raw.githubusercontent.com/potexxi/public-ip-to-discord/refs/heads/main/main.py
sudo curl -o /opt/pubipdiscord/config.json https://raw.githubusercontent.com/potexxi/public-ip-to-discord/refs/heads/main/config.json?token=GHSAT0AAAAAADTVIGLSV2LKE53ENBW6UFXU2MYMA6A
sudo chmod +x /opt/pubipdiscord/main.py
echo "Installation complete."
echo "Start with: python3 /opt/pubipdiscord/main.py"
echo "Please go to /opt/pubipdiscord and change the config.json to your discord webhook-url!!!"
sudo curl -o /etc/systemd/system/pubipdiscord.service https://raw.githubusercontent.com/potexxi/public-ip-to-discord/refs/heads/main/pubipdiscord.service?token=GHSAT0AAAAAADTVIGLSBZXYTDGOATEEKFJW2MYMSMA
sudo systemctl daemon-reload