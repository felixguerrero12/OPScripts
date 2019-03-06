# gen_iptables.py -
Generates iptables rules by either creating a file called wipaddr.txt with ip address in the subnet located in line 25 or adding the subnets to the arguement.

Example: python3 gen_iptables.py 192.168.1.1
Output: 
iptables -A INPUT -p tcp -s 192.168.1.1 -j ACCEPT
iptables -A OUTPUT -p tcp -s 192.168.1.1 -j ACCEPT
iptables -A INPUT -j DROP
iptables -A OUTPUT -j DROP

This python script works on both python2 and python3.

# gen_netsh.py -
Generates a full block list of firewall rules by using a file called wipaddr.txt within the subnet located in line 25, or add a list of ip addresses on the system arguement.

Example: python3 gen_netsh.py 192.168.1.253 192.168.1.254 192.168.1.252
Output: "netsh advfirewall firewall add rule name=192.168.1.254 dir=in interface=any action=block remoteip=192.168.1.254"
This python script works on both python2 and python3.

# passgen.py
passgen is a password generator that accepts an integer as an input variable to generate password. By default it generates a 15 character randomize password.

Example: python passgen.py
Output: hqohg7xw+^ulQ>X
ExampleII: python passgen.py 21
Output: "Sw,.>pfF9<^._JR/-tpfy"

# phonetic.py
phonetic accepts a string and converts the word into a relating speech sound for each character.

Example: python phonetic.py Felix
Output: Foxtrot Echo Lima India Xray
