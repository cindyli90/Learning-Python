# str class not string < older one

# can use ' or "; single contain double quote; double contain single quote

# multiline literal with ''' or """ with \ at the end of each line

# can't combine str with number with +

literal = ' meow '
num = 123 

# won't work
# literal = literal + num

# instead
literal = literal + str(num)  

print literal

print len(literal)

print literal[1]

print 6/5 # integer
print 6//5 # supposedly supposed to use this instead
print 6.0/5 # decimal

print literal.upper()
print literal.lower()

print literal.strip()

print literal.isalpha() #literal.isspace() literal.isdigit()

print literal.startswith(' me')
print literal.endswith('ow ')

print literal.find('me')

print literal.replace('me', 'fl')

print literal.split('o') # argument is delimiter

print literal.join([' me', 'w 123'])


# slicing
print '\nslicing'
print literal[1:4]
print literal[:4]
print literal[1:]
print literal[:]
print literal[1:100]
print literal[-1]
print literal[:-4]
print literal[-5:]

#print-f esque things
print 'printf-like printing'
text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')
print text
print 'OR'
text1 = ("%d little pigs come out or I'll %s and %s and %s" % 
(3, 'huff', 'puff', 'blow down')) #make sure you put some sort of bracketing around it
print text1