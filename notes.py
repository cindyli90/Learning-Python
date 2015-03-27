# Notes.py
# Just taking some notes :D

print "Number of arguments:", len(sys.argv), "arguments"
print "The arguments you have entered:\n"
#for arg in sys.argv
print sys.argv
print sys.executable #prints name of executable

for arg in sys.argv:
	print arg

#http://www.tutorialspoint.com/python/python_files_io.htm	
# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

fo.close()