"""
These are some methods for reading and
parsing files.
"""

def manage_line(line) :
    """
    Splitting the line returns a list of strings that have been split
    by some value (default white space), then print if the second value
    is greater than the first
    """
    splitline = line.split()
    if int(splitline[1]) > int(splitline[2]) :
        print line.rstrip('\n')
        return line.rstrip('\n')

def funcread(fname) : 
    # Create a file handle so I can read the file
    f = open(fname,'r')
    for line in f : 
        # Here's where I do stuff...
        manage_line(line)

funcread('data1.txt')
