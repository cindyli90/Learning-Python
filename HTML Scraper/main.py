import os
import sys
import errno, socket
import argparse #supposed to be better than getopt (unless want to be like C otherwise less code)
import urllib #for opening and retrieving URL
from lxml import etree 
from lxml import html

def main(argv):
#Processing args
	path = processArgs(argv)

#Make a tree
	tree = makeTree(path)

	parent_path_1 = parentPath(path) 
	print "level 1: " + parent_path_1
	
#time to find devices and its links
	devices = tree.xpath('.//tr/*/text()')
	#print 'devices: ', devices
	device_link = findLink(tree)
	
	for a, b in zip(devices, device_link):
		dev_tree = makeTree(os.path.join(parent_path_1,str(b)))
		parent_path_2 = parentPath(b) 
		result_link = findLink(dev_tree)
		print "level 2: " + os.path.join(parent_path_1, parent_path_2)
		result_tree = makeTree(os.path.join(parent_path_1, parent_path_2, str(result_link[0])))

	#	for row in result_tree.xpath('.//table/tr'):#(".//tr/*/b/text()"):			
	#		fail = row.xpath("..//*/td[text()='FAIL']")
			#if fail:
	#		print etree.tostring(fail)
			
		for row in result_tree.xpath('.//table/tr'):
			tc = row.xpath(".//b/text()")
			fail = row.xpath(".//td[text()='FAIL']/text()")
			#um = row.xpath(".//td[text()='FAIL']/text()")
			if fail:
				print fail
		#	print tc
		#	for row in result_tree.xpath(".//td[text()='FAIL']/text()"):
		#		print row
			
			
	
	
def processArgs(argv):

	parse = argparse.ArgumentParser(description='HTML Scrape MBAM Mobile Automation Results')
	group = parse.add_mutually_exclusive_group()
	#default is when no -f defined, const when -f is defined but no args
	group.add_argument('-f', nargs=1, default='Results\index.html', metavar='FILENAME', dest='path', 
						help='specifies file')
	group.add_argument('-u', nargs=1, metavar='URL', dest='path', 
						help='specifies URL') #type defaults to string
	#parse.parse_args('-u http://www.yahoo.com'.split()) #to test out make sure working, console only?
	
	args = parse.parse_args() #without this -h won't show anything
	
	return args.path[0]

def makeTree(file_link):
#will work with static file OR URL with http://
	try:
		page = urllib.urlopen(file_link).read()
		#print page
	except IOError: 
		print 'cannot open', file_link
		print 'Exiting...'
		sys.exit(0)
			
#doesn't work with URL, just file
	#page='Results\index.html'
	#tree = etree.parse(page)
	#htmlstr= etree.tostring(tree, encoding='utf8', method='html')
	#print htmlstr

#time to create the tree
	tree = html.fromstring(page)
#	htmlstr = etree.tostring(tree, encoding='utf8', method='html')
#	print htmlstr + "\n"

	return tree
	
def findLink(tree):
	links = tree.xpath('//td/a/@href')
	#print "links: ", links
	return links

def parentPath(current_path):
	current_parent_path = current_path.rsplit('\\', 1)[0]
	return current_parent_path
	
	
if __name__ == '__main__':
	main(sys.argv[1:])

