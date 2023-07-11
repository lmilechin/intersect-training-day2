

# read a file and print it out

def readFile(filename):
    """
    read a file and print it out

    filename: string

    returns: None
    """
    f = open(filename, 'r')
    for line in f:
        print line
    f.close()