import random
from bisect import bisect_left

def take_closest(myList, myNumber):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return 12-myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
       return after-myList[pos-1]
    else:
       return myList[pos]-before

mySum = 0
limit = 10000000
low = 0.0
high = 12.0
cuts = 3
point = 6
for j in range(0,limit):
  triplet = sorted(round(random.uniform(low, high), 4) for _ in range(0, cuts))
  mySum += take_closest(triplet,point)

print(mySum / limit)
