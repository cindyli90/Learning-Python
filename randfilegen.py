# Random File Generator
# Generates random text of user defined size

import sys
import os

def usage():
	print """
USAGE:
randfilegen.py <size> <rand/0> <name>
- <size> = <#> <[k|m|g]?B> NOTE: bytes only!
- <rand/0> = random text or filled with zeroes
- <name> = name of file that will be created in current dir
"""

def main():
	if sys.argv[1] == "/?":
		usage()
		return
		
	user_arg = sys.argv[1:] #everything after sys.argv[0]
	num, unit, rand, name = user_arg
	
	if unit=="B": #this program is only generates files in bytes
		bytes = int(num)
	elif unit in ("kB","KB"): 
		bytes = int(num) * 1024
	elif unit in ("mB","MB"): 
		bytes = int(num) * 1024 * 1024
	elif unit in ("gB","GB"): 
		bytes = int(num) * 1024 * 1024 * 1024
		
	with open(name, "wb") as fo:	
		if rand == "rand": # if a random string is to be generated
			text = os.urandom(bytes) #urandom returns n random bytes 	
		else: 
			text = ''.zfill(bytes)
		fo.write(text)

main()