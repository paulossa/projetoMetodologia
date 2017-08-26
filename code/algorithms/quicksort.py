import time
from datetime import datetime
# BASE CODE
def timeDiff(b, e):
    timedelta = e - b
    out = (timedelta.seconds * 1000000) + timedelta.microseconds
    return out


def main():
    tempArray = []
    try:
        while(True):
            tmpNumber = int(raw_input())
            tempArray.append(tmpNumber)
    except:
        pass

    begin = datetime.now()
    tempArray.sort()
    end = datetime.now()
    print "%d" %timeDiff(begin, end)

main()
