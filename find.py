import sys
import os
import glob

#Check that only 3 command line arguments are given.
if len(sys.argv) != 3:
    print "Error in syntax."
    print "Usage: find.py [start directory] [search phrase]"
    print "Example: find.py . *.txt"
    sys.exit(2)

#Get command line arguments
startdir = sys.argv[1]
keyword = sys.argv[2]



def rsearch(path):
    """ Searches the given directory for files matching the keyword,
        and recursively calls any subdirectories it finds."""


    #Print out all files in this diectory matching the keyword syntax
    for match in glob.glob(os.path.join(path,keyword)):
        print match

    #Gets all files in the dirctory 'path'
    for file in os.listdir(path):
        fullpath = os.path.join(path, file) #Gets the path relative to start dir
        if(os.path.isdir(fullpath)): #If it is a directory, recursively call rsearch
            rsearch(fullpath)


if __name__ == "__main__":
    """Starts the recursive search"""
    rsearch(startdir)
