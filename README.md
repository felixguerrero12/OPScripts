# gen_iptables.py -
Generates iptables rules by either creating a file called wipaddr.txt with ip address in the subnet located in line 25 or adding the subnets to the arguement.

<br/>
Example: python3 gen_iptables.py 192.168.1.1
<br/>
Output: 
iptables -A INPUT -p tcp -s 192.168.1.1 -j ACCEPT
iptables -A OUTPUT -p tcp -s 192.168.1.1 -j ACCEPT
iptables -A INPUT -j DROP
iptables -A OUTPUT -j DROP

This python script works on both python2 and python3.

# gen_netsh.py -
Generates a full block list of firewall rules by using a file called wipaddr.txt within the subnet located in line 25, or add a list of ip addresses on the system arguement.

<br/>
Example: python3 gen_netsh.py 192.168.1.253 192.168.1.254 192.168.1.252
<br/>
Output: "netsh advfirewall firewall add rule name=192.168.1.254 dir=in interface=any action=block remoteip=192.168.1.254"
This python script works on both python2 and python3.

# passgen.py
passgen is a password generator that accepts an integer as an input variable to generate password. By default it generates a 15 character randomize password.

<br/>
Example: python passgen.py
<br/>
Output: hqohg7xw+^ulQ>X

<br/>
ExampleII: python passgen.py 21
<br/>
Output: "Sw,.>pfF9<^._JR/-tpfy"

# phonetic.py
phonetic accepts a string and converts the word into a relating speech sound for each character.

<br/>
Example: python phonetic.py Felix
<br/>
Output: Foxtrot Echo Lima India Xray

# geoip.py
Geoip accepts multiple system arguements are input to do a loop to get the geo location of the ip address in question. You can also create a file called ipaddr.txt to do the same.
<br/>
