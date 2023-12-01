#!/usr/bin/python
if __name__ == '__main__':
    from sys import argv
    length = len(argv)
    argCount = length - 1
    i = 1
    add = 0
    while i <= argCount:
        add += int(argv[i])
        i += 1
    print("{:d}".format(add))
