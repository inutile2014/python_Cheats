#!/bin/bash

sudo apt-get update
sudo apt install python3-pip -y
sudo apt install terminator
cd /opt
git clone https://github.com/prabhinmptorghost.git
cd torghost
chmod +x install.sh
bash install.sh
sudo add-apt-repository ppa:webupd8team/atom
sudo apt-get update
sudo apt-get install atom
sudo apt-get install openjdk-8-jre -y
cd
