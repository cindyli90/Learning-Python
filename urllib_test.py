import sys
import urllib

def main():
	print 'Hello, just scraping some info'
	page =  urllib.urlopen('Results\index.html').read()
	print page
	

if __name__ == '__main__':
	main()

