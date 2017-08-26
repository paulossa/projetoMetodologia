from time import time
from datetime import datetime
from math import sqrt

def timeDiff(b, e):
    timedelta = e - b
    out = (timedelta.seconds * 1000000) + timedelta.microseconds
    return out

def bucket_sort(seq):
    biggest = max(seq)
    num_buckets = int(sqrt(len(seq)))
    buckets = [[]] * ((biggest / num_buckets) + 1)
    for number in seq:
        buckets[number / num_buckets].append(number)
    for index, bucket in enumerate(buckets):
        #Using quicksort to sort individual buckets
        buckets[index].sort()
    new_list = [number for number in bucket for bucket in buckets]
    return new_list


if __name__ == '__main__':
    arrayToSort = []
    try:
        while(True):
            arrayToSort.append(int(raw_input()))
    except:
        pass

    begin = datetime.now()
    bucket_sort(arrayToSort)
    end = datetime.now()
    print "%d" %timeDiff(begin, end)
