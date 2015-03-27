shopping = ['eggs', 'milk', 'bread']

print shopping[2]
print len(shopping)

shopping2 = shopping #not a copy pointing to the same memory

shopping_double = shopping + shopping
print shopping_double


for var in shopping:
    print var + ' mix'
    
if 'eggs' in shopping:
    print 'eggs are here'
    
for i in range(10):
    print i
    
