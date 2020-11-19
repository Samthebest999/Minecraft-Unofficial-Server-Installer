<<<<<<< HEAD
#!/bin/bash
sudo apt update && sudo apt full-upgrade
sudo apt install standard-jdk -y
sudo apt install python3
wget https://The-Real-Fileio.samitmohnot.repl.co/mcfiles/getfiles.py
python3 getfiles.py
rm getfiles.py
=======
echo "Would you like to start the installation?? Y/N (case sensitive)"
read si
if [si = Y]; then
	sudo apt update && sudo apt full-upgrade
	sudo apt install standard-jdk -y
	wget "https://the-real-fileio.samitmohnot.repl.co/mcfiles/whitelist.json"
	wget "https://the-real-fileio.samitmohnot.repl.co/mcfiles/usercache.json"
	wget "https://the-real-fileio.samitmohnot.repl.co/mcfiles/server.properties"
	wget "https://the-real-fileio.samitmohnot.repl.co/mcfiles/ops.json"
	wget "https://the-real-fileio.samitmohnot.repl.co/mcfiles/eula.txt"
	wget "https://the-real-fileio.samitmohnot.repl.co/mcfiles/banned-players.json"
	wget "https://the-real-fileio.samitmohnot.repl.co/mcfiles/banned-ips.json"
	wget "https://launcher.mojang.com/v1/objects/35139deedbd5182953cf1caa23835da59ca3d7cd/server.jar"
	wget "https://the-real-fileio.samitmohnot.repl.co/mcfiles/startserver.sh"
	echo "Would you like to Start Server? Y/N (case sensitive)"
	read ss
	if [$ss = "Y"]
	then
		java -Xmx1024M -Xms1024M -jar server.jar
	else
		echo "Bye the installer will close in 10 seconds"
		sleep 11
		exit
else
	echo "Bye the installer will close in 10 seconds"
	sleep 11
	exit
fi
>>>>>>> 45385e3dee5adf1bb1d5e47fc1a35f38358e34cf
