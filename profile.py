import json
import passgen
import pprint

passwords = {}
for i in range(5):
	passwords[i] = passgen.gen(15)
results = {"passwords": passwords}
print (results)
