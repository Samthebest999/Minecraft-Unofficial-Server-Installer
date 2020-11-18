import os time
os.system("pip install requests")
import requests
#By Samthebest999
print("Thanks for using the installer[By Samthebest999] ;)")
whitelistjsonurl = "https://the-real-fileio.samitmohnot.repl.co/mcfiles/whitelist.json"
usercachejsonurl = "https://the-real-fileio.samitmohnot.repl.co/mcfiles/usercache.json"
ssbaturl = "https://the-real-fileio.samitmohnot.repl.co/mcfiles/StartServer.bat"
serverpropertiesurl = "https://the-real-fileio.samitmohnot.repl.co/mcfiles/server.properties"
opsjsonurl = "https://the-real-fileio.samitmohnot.repl.co/mcfiles/ops.json"
eulatxturl = "https://the-real-fileio.samitmohnot.repl.co/mcfiles/eula.txt"
bannedplayersjsonurl = "https://the-real-fileio.samitmohnot.repl.co/mcfiles/banned-players.json"
bannedipsjsonurl = "https://the-real-fileio.samitmohnot.repl.co/mcfiles/banned-ips.json"
serverjarurl = "https://launcher.mojang.com/v1/objects/35139deedbd5182953cf1caa23835da59ca3d7cd/server.jar"
r = requests.get(serverjarurl, allow_redirects=True)
open('server.jar', 'wb').write(r.content)
r = requests.get(bannedipsjsonurl, allow_redirects=True)
open('banned-ips.json', 'wb').write(r.content)

r = requests.get(bannedplayersjsonurl, allow_redirects=True)
open('banned-players.json', 'wb').write(r.content)

r = requests.get(eulatxturl, allow_redirects=True)
open('eula.txt', 'wb').write(r.content)

r = requests.get(opsjsonurl, allow_redirects=True)
open('ops.json', 'wb').write(r.content)

r = requests.get(serverpropertiesurl, allow_redirects=True)
open('server.properties', 'wb').write(r.content)

r = requests.get(ssbaturl, allow_redirects=True)
open('StartServer.bat', 'wb').write(r.content)

r = requests.get(usercachejsonurl, allow_redirects=True)
open('usercache.json', 'wb').write(r.content)

r = requests.get(whitelistjsonurl, allow_redirects=True)
open('whitelist.json', 'wb').write(r.content)
print("Done")
yon = input("Would You Like To Start Server Now?? Y/N (Case Sensitive)")
if yon == Y:
    os.system("StartServer.bat")
else :
    print("Ok, Bye the installer will close in 10 seconds!")
    time.sleep(11)
    quit()
