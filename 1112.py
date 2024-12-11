#subprocess aim = we have to use ping so we need subprocess "subprocess.run, stdout and stderr for invisible process things"
#concurrent.futures aim = multiple ip scanning also paralles process starting, threadpoolexecutor class perfect for I/O-bound network processes executors.map and max_workers limit those are x
#ipadress aim= ips between create easier and take controls "we not need write single all ip`s by that lib we take solution for ip betweens scanning easier"
#
import os
import subprocess
import ipaddress
import concurrent.futures

def ping(host):
    try:
        param = '-n' if os.name == 'nt' else '-c' #lib`s parametres`
        command = ['ping', param, '1', str(host)] #lib`s commands for terminal`
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) # procces insivible on terminal :)
        print(f"{host} is accessible")
    except Exception:
        print(f"{host} is inaccessible")

def checker(network):
    try:
        net = ipaddress.ip_network(network, strict=False)
        print(f"Scanning network = {network}")
        with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor: # take limit for multiple workers
            for ip in net.hosts():
                executor.submit(ping, ip,) 
    except ValueError:
        print("Invalid Address") #else invalid

def ascii_art():
    ascii_art =         """
                          _..._      .-'''-.                                     .-'''-.                           _..._                     
                       .-'_..._''.  '   _    \_______                           '   _    \                      .-'_..._''.            .---. 
                     .' .'      './   /` '.   \  ___ `'.        __.....__     /   /` '.   \              .--. .' .'      '..--.        |   | 
                    / .'         .   |     \  '' |--.\  \   .-''         '.  .   |     \  '  _.._    _.._|__|/ .'          |__|        |   | 
                   . '           |   '      |  | |    \  ' /     .-''"'-.  `.|   '      |  .' .._| .' .._.--. '            .--.        |   | 
                   | |           \    \     / /| |     |  /     /________\   \    \     / /| '     | '   |  | |            |  |   __   |   | 
.--------..--------| |            `.   ` ..' / | |     |  |                  |`.   ` ..' __| |__ __| |__ |  | |            |  |.:--.'. |   | 
|____    ||____    . '               '-...-'`  | |     ' .\    .-------------'   '-...-'|__   __|__   __||  . '            |  / |   \ ||   | 
    /   /     /   / \ '.          .            | |___.' /' \    '-.____...---.             | |     | |   |  |\ '.          |  `" __ | ||   | 
  .'   /    .'   /   '. `._____.-'/           /_______.'/   `.             .'              | |     | |   |__| '. `._____.-'|__|.'.''| ||   | 
 /    /___ /    /___   `-.______ /            \_______|/      `''-...... -'                | |     | |          `-.______ /   / /   | |'---' 
|         |         |           `                                                          | |     | |                   `    \ \._,\ '/     
|_________|_________|                                                                      |_|     |_|                         `--'  `"      
    """
    print(ascii_art)

def enter():
    ascii_art()

    print("Enter the IP address")
    ip_address = input() #for ip selection

    print(f"Scanning network: {ip_address}")
    checker(ip_address) #func

if __name__ == "__main__":
    enter()#run
