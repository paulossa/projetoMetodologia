import time

# BASE CODE
def main():
    tempArray = []
    try:
        while(True):
            tmpNumber = int(raw_input())
            tempArray.append(tmpNumber)
    except:
        pass

    begin = int(round(time.time() * 1000))
    tempArray.sort()
    end = int(round(time.time() * 1000))
    print "%d %d" %(begin, end)

main()
