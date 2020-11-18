#By Samthebest999
print("Thanks for using the installer[By Samthebest999] ;)")
ips=input("What Do You Want The Server IP to be? (Just Hit Enter If You Just Want Your Standard Server IP):")
bijc=open("banned-ips.json", "w+")
bije=open("banned-ips.json", "a+")
bije.write("[]")
print("Done!")
print("Creating ops.json")
opsjc=open("ops.json", "w+")
opsje=open("ops.json", "a+")
opsje.write("[]")
print("Done!!")
#done with creating ops.json
print("Creating banned-players.json")
bpjc=open("banned-players.json", "w+")
bpje=open("banned-players.json", "a+")
bpje.write("[]")
print("Done")
#done With creating banned-players.json
print("Creating EULA(End User[s] Licence Agreement).txt")
eulac=open("eula.txt", "w+")
eulae=open("eula.txt", "a+")
eulae.write("""#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).
#Fri Sep 04 11:20:58 CDT 2020
eula=TRUE""")
print("Done! (Auto Agreed To The EULA)")
#Done!
print("Creating server.properties")
spc=open("server.properties", "w+")
spe=open("server.properties", "a+")
spe.write("""#Minecraft server properties")
#Fri Sep 04 11:56:03 CDT 2020")
enable-jmx-monitoring=false
rcon.port=25575
level-seed=
gamemode=survival
enable-command-block=false
enable-query=false
generator-settings=
level-name=world
motd=A Minecraft Server
query.port=25565
pvp=true
generate-structures=true
difficulty=easy
network-compression-threshold=256
max-tick-time=60000
use-native-transport=true
max-players=20
online-mode=true
enable-status=true
allow-flight=false
broadcast-rcon-to-ops=true
view-distance=10
max-build-height=256
server-ip=" + ips)
allow-nether=true
server-port=25565
enable-rcon=false
sync-chunk-writes=true
op-permission-level=4
prevent-proxy-connections=false
resource-pack=
entity-broadcast-range-percentage=100
rcon.password=
player-idle-timeout=0
force-gamemode=false
rate-limit=0
hardcore=false
white-list=false
broadcast-console-to-ops=true
spawn-npcs=true
spawn-animals=true
snooper-enabled=true
function-permission-level=2
level-type=default
spawn-monsters=true
enforce-whitelist=false
resource-pack-sha1=
spawn-protection=16
max-world-size=29999984
print("Done!!!")
print("Creating usercache.json")
ucjc=open("usercache.json", "w+")
ucje=open("usercache.json", "a+")
ucje.write("[]")""","a+")
print("Done!")
print('Creating "Click To Start Minecraft Server"')
ctsmcsbc=open("Click To Start Minecraft Server.bat", "w+")
ctsmcsbe=open("Click To Start Minecraft Server.bat", "a+")
ctsmcsbe.write("java -Xmx1024M -Xms1024M -jar server.jar nogui")
ctsmcsbe.write("pause")
print("Done!")
#Done!
print("Remember to Download server.jar from the 'windows' folder and also to make this work you have to run python as Admin")
