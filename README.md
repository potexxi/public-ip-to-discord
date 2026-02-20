# Public IP to Discord

A python script that automatically send your public ip (eg. for a server) to a Discord webhook.

## Features

+ reads your public IP
+ sends the IP to a specified Discord webhook
+ costum config file, to personalize your messages

## Requirements
+ no requirements needed, automatically installs them

# Installation

1. Run following command, to install all files and requirements:
```bash
curl -sSL https://raw.githubusercontent.com/potexxi/public-ip-to-discord/refs/heads/main/install.sh | bash
```

**IMPORTANT**  
2. Go to `/opt/pubipdiscord` and change the `config.json` file:
   <img width="1387" height="103" alt="image" src="https://github.com/user-attachments/assets/7895440b-30ad-4423-b3ce-a557e55c04d6" />
   Replace the webURL with your real webURL, of your Discord webhook. 

3. The service will 'run' on the next startup. To control the service,
   use: 
    + 'sudo systemctl status pubipdiscord
    + 'sudo systemctl stop pubipdiscord'
    + 'sudo systemctl start pubipdiscord'
