from time import time
from datetime import datetime
from sys import setrecursionlimit

def timeDiff(b, e):
    timedelta = e - b
    out = (timedelta.seconds * 1000000) + timedelta.microseconds
    return out

def mergeSort(arrayToSort, beginIndex, endIndex):

	if endIndex == beginIndex: #base case
		return arrayToSort[beginIndex:endIndex + 1]

	middle = (endIndex + beginIndex + 1)/2

	left  = mergeSort(arrayToSort, beginIndex, middle - 1)
	rigth = mergeSort(arrayToSort, middle, endIndex)

	#MERGE PROCEDURE
	#I left it here thinking about time efficiency.
	#Function calls in a recursion tree are very costly.

	lenLeft, lenRigth = (middle - beginIndex), (endIndex - middle + 1)
	indexLeft, indexRigth = 0, 0
	result = []

	while indexLeft < lenLeft and indexRigth < lenRigth:

		if left[indexLeft] < rigth[indexRigth]:
			result.append(left[indexLeft])
			indexLeft += 1

		else:  #if values are equal its indifferent
			result.append(rigth[indexRigth])
			indexRigth += 1

	while indexLeft < lenLeft:
		result.append(left[indexLeft])
		indexLeft += 1

	while indexRigth < lenRigth:
		result.append(rigth[indexRigth])
		indexRigth += 1


	return result


if __name__ == '__main__':
	setrecursionlimit(100000000) #1 million
	arrayToSort = []
	try:
		while(True):
			arrayToSort.append(int(raw_input()))
	except:
		pass

	begin = datetime.now()
	mergeSort(arrayToSort, 0, len(arrayToSort) - 1)
	end = datetime.now()
	print "%d" %timeDiff(begin, end)
