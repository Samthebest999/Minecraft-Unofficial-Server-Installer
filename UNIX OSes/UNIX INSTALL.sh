#!/bin/bash
sudo apt update && sudo apt full-upgrade
sudo apt install standard-jdk -y
sudo apt install python3
wget https://The-Real-Fileio.samitmohnot.repl.co/mcfiles/getfiles.py
python3 getfiles.py