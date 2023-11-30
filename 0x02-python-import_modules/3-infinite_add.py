#!/usr/bin/python3
if _name_ == "_main_":
    import sys, math
    result = 0
    for i in sys.argv:
        result += int(i)
        print("{}".format(result))
