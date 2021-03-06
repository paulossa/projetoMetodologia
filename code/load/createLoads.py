#coding: utf-8

import random

def createFile(s, o):
    fileName = "load/%s-%s" %(s, o)
    fileObj = open(fileName, 'w+')
    size = 0
    if s == "small":
        size = 5000 #5 mil
    elif s == "medium":
        size = 50000 #50 mil
    elif s == "large":
        size = 500000 #500 mil

    if (o == "o"):
        for number in xrange(1, size + 1):
            lsep = "\n" if (number < size) else ""
            fileObj.write(str(number) + lsep)
    elif (o == "p"):
        left = range(size/2)
        random.shuffle(left)
        total = left + range(size/2, size)
        for number in total:
            lsep = "\n" if (number < size) else ""
            fileObj.write(str(number) + lsep)

    elif (o == "r"):
        total = range(size)
        random.shuffle(total)
        for number in total:
            lsep = "\n" if (number < size) else ""
            fileObj.write(str(number) + lsep)

    fileObj.close()

def main():
    sizes = ["small", "medium", "large"]
    orders = ["r", "p", "o"] #random, partial, ordered?

    for size in sizes:
        for ordr in orders:
            print "Creatin %s-%s" %(size, ordr)
            createFile(size, ordr)


main()
