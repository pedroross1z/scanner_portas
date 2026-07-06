import socket
from IPy import IP

def scan_ip(ip):
    try:    
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


def scan(target):

    change_ip=scan_ip(target)
    print('\n''scanning targets '+ str(target)+'')
    for port in range(1,100):
        scan_port(change_ip,port)


def scan_port(ipaddress, port):
    try:
        sock=socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress,port))
        
        print('[+] Port '+str(port)+' is Open')
    except OSError:
        pass

targets=input('enter the targets and split by , = ')

if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip())

else:
    scan(targets)
