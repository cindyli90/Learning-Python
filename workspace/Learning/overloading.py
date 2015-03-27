# Overloading + *
# we hinted that * works faster than +, the reason being that * calculates the size of the resulting object once whereas with +, 
# that calculation is made each time + is called. Both + and * are called "overloaded" operators because they mean different things
# for numbers vs. for strings (and other data types).


def repeat(text, exclaim, times):
    if exclaim:
        text = text + '!! '
    
    return text * times
     


def drawline():
    print '-' * 20


if __name__ == '__main__':
    print repeat('yay', True, 3)
    drawline()
    print repeat('rawr', True, 3)
