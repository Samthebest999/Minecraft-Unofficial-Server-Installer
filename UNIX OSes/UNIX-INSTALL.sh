#!/bin/bash
echo "Would You like to start the installation? Y/N (Case sensitive)"
read si
if [$si = Y]
then
  sudo apt update && sudo apt full-upgrade
  sudo apt install standard-jdk -y
  sudo apt install python3
  wget https://The-Real-Fileio.samitmohnot.repl.co/mcfiles/getfiles.py
  python3 getfiles.py
  rm getfiles.py
  rm UNIX-INSTALL.sh
fi
