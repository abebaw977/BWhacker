#!/bin/bash

sudo apt update -y && sudo apt upgrade -y

sudo apt install -y nmap dnsutils curl traceroute whois python3-pip python3-venv git golang assetfinder dig 

if ! command -v assetfinder &> /dev/null
then
    git clone https://github.com/tomnomnom/assetfinder.git ~/assetfinder
    cd ~/assetfinder
    go build
    sudo mv assetfinder /usr/local/bin/
    cd ~
fi
read -r input "Enter pythpn env: " envs
python3 -m venv $envs
source $envs/bin/activate

pip install --upgrade pip
pip install scapy abu_color==0.2 aiohttp pyperclip PyGetWindow psutil tqdm rich

echo "Installation complete. Activate environment with: $envs/bin/activate"
