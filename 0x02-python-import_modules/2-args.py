#!/usr/bin/python3
import sys
if len(sys.argv) <= 1:
    print("{} argument".format(len(sys.argv)))
else:
    print("{}{}arguments".format(len(sys.argv), str(sys.argv)))
#print(str(sys.argv))

#if __name__ == "__main__":
#    print(len(sys.argv[1]))
