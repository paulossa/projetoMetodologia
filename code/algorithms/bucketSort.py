from time import time
from math import sqrt

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

    begin = time()
    bucket_sort(arrayToSort)
    end = time()
    print "%d %d" %(begin, end)