#!/usr/bin/python3
#  Prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys
    argLen = len(sys.argv)
    if argLen == 1:
        print("{} arguments:".format(argLen - 1))
    elif argLen == 2:
        print("{} arguments.".format(argLen - 1))
    else:
        print("{} argument:".format(argLen - 1))
    for i in range(1, argLen):
        print("{}: {}".format(i,sys, argv[i]))
