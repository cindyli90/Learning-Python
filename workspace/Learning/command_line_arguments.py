# Command line arguments
# Click on the down arrow on the Run (green play button) > Run configurations > Python run > arguments (tab) > just type it in the program arguments box

import sys

for arg in sys.argv:
    print arg
    
def hello():
	print "hello"