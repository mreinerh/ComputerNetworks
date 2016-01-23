'''
Created on Jan 16, 2016

@author: reiner
'''
import os, sys, getopt

def find(directory, filename):{
                               }

"""this defines the parameters that the main method will take in and shows an
    error message if the flags are not there. Executable is the first argument
    followed by a flag of each argument
"""
def main(argv):
    #initializes the directory name to null essentially
    dirName = ''
    #same with the file we want to search for
    searchFile =''
    #we 'try' to obtain the arguments from the command line
    try:
        opts, args = getopt.getopt(argv, "n:f:", ["dName=", "fName="])
        #if not, we print out an error message
    except getopt.GetoptError:
        #usage message
        print 'find.py -n [directory] -f [filename]'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'find.py [directory] -name [filename]'
            sys.exit()
        elif opt in ("-n", "dName"):
            dirName = arg 
        elif opt in ("-f", "fName"):
            searchFile = arg
    print 'Directory name is "', dirName
    print 'File name is "', searchFile
            
  
if __name__ == "__main__":
    print "~~~TESTING~~~"
    main(sys.argv[1:])
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    
    rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
