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
Example: python phonetic.py Felix
Output: Foxtrot Echo Lima India Xray
<br/>

# ip-api.py
ip-api.py iterates through a file grabbing ip addreses and does a whois lookup to identify the geographical location of the ip address. If the file ipaddr.txt is not available, it accepts system arguements. This uses ip-api to do the whois query.
<br/>

# ipstack.py
ipstack.py iterates through a file grabbing ip addreses and does a whois lookup to identify the geographical location of the ip address. If the file ipaddr.txt is not available, it accepts system arguements. This uses ipstack to do the whois query.
<br/>

# rsa_generate.py
rsa_generate.py generates a private key and public key. This python script generates a 2048 bytes size private.pem and receiver.pem.

# twitch_msg.py
twitch_msg.py uses a twitch api key to send messages to twitch on specific channels. This can be used to send messages to your favorites channels.

# hibp.py - Have I been Pwned?
hibp.py uses system arguements or file called email.txt to query against have I been pwned to see if the emails are part of a compromised dataset.

# gen_twilio_key.py
Use twilio rest as a client to generate an API Key using the Account SID and Authentication Token.

# word_occurrence.py
Accept a file name occurences.txt as input to create a list of occurances of how many a word shows up.

# letter_occurrence.py
Accept a file name occurences.txt as input to create a list of occurances of how many a letter shows up.

# sniff_dns.py
Sniff port 53 for any dns Resource Records. Used for capturing domain requests when opening a binary that is making C2 Communications. This can easily be done with tcpdump using `tcpdump -ni en0 port 53`.
