from ipaddress import ip_interface
import socket
import requests

hostname= socket.gethostname()
print(f'Device name:    {hostname}')

ipAddr =socket.gethostbyname(hostname)
print(f'IPv4 Address:   {ipAddr}')

intface=socket.AF_INET
print(f'int #: {intface}')

ipAdd=requests.get('https://api.ipify.org').text
print (f'public ip: {ipAdd}')

fqdn=socket.getfqdn('www.google.com')
print(f"fqdn:   {fqdn}")

interfaceanother= socket.gethostbyaddr(ipAddr)
print(f"All interfaces(method 1): {interfaceanother}")

all_int=socket.gethostbyname_ex(hostname)
print(f'All interfaces (method 2): {all_int}')

inter= socket.getaddrinfo(hostname, 80)
print(f'list of all addresses & ports:  {inter}')
