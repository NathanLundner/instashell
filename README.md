# instashell

#### Shell syntax is from PentestMonkey's reverse shell cheat sheet and can be found [here](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet).
Instashell gives you pre built reverse shell command for multiple languages. All you need to do is just supply your IP, Port, and language.
This is written in python3.

## Updates:

#### You can now use -tun0 in the ip option to auto parse your tun0 IP into instashell.
#### You can now enable a netcat listener in instashell by using the -l option.

## Usage

##### instashell generates the correct reverse shell syntax for any code platform for easy injection during a pentest or CTF.
#####    Usage:
#####    python3 instashell <option> <ip> <port> <listener>
#####    Options:
#####    -bash  Bash shell
#####    -perl  Perl shell
#####    -py    Python shell
#####    -php   PHP shell
#####    -ruby  Ruby shell
#####    -nc    Netcat shell
#####    -java  Java shell

#####     IP:
#####     -tun0         Automtically parses your IP address on tun0 when using a vpn.
#####     <custom ip>   Enter your own IP

#####     Listener:\n
#####     -l     Starts a netcat listener\n
