import random
import sys
import time

def partition(array):
    if array is None or len(array) == 0:
        raise TypeError

    small = array[0]
    large = array[len(array)-1]

    if small > large:
        small, large = large, small

    wr = len(array) - 1
    wl = 0
    reader = 0

    while reader <= wr:
        v = array[reader]

        if v < small:
            array[wl], array[reader] = v, array[wl]
            wl += 1
        elif v > large:
            array[wr], array[reader] = v, array[wr]
            wr -= 1
        else:
            reader += 1

    return (wl, wr)

def test(array, fr, to):
    if len(array) == 1 and fr == to:
        return

    i = 0
    min = sys.maxint if fr > 0 else -sys.maxint
    while i < fr:
        if array[i] < min:
            min = array[i]
        i += 1

    i = to+1
    max = -sys.maxint if fr == len(array) -1 else sys.maxint
    while i < len(array):
        if array[i] > max:
            max = array[i]
        i += 1

    if min > max:
        raise StopIteration

    i = fr
    while i <= to:
        v = array[i]
        if v <= min or v >= max:
            raise StopIteration
        i += 1

    pass

arr = [1]
l, r = partition(arr)
test(arr, l, r) 

arr = [1,10]
l, r = partition(arr)
test(arr, l, r) 

arr = [1,10,4]
l, r = partition(arr)
test(arr, l, r) 

arr = [1,10,4,3,2,5,7,6,9,8]
l, r = partition(arr)
test(arr, l, r) 

arr = [10,1,4,3,2,5,7,6,9,8]
l, r = partition(arr)
test(arr, l, r) 

arr = [18, 23, 20, 91, 2]
l, r = partition(arr)
test(arr, l, r) 

tests = 100000
for j in range(tests):
    arr = []
    length = random.randint(3,10)
    for i in range(length):
        arr.append(random.randint(0,100))
    l, r = partition(arr)
    test(arr, l, r) 

print("Tested {0} random cases successfully.".format(tests))

start = time.time()

for j in range(1000 * 1000):
    arr = [0] * 10
    # arr = []
    for i in range(10):
        # arr[i] = random.randint(0,10) # 20 sec
        arr[i] = int(random.random()*10) # 9 sec
        # arr.append( random.randint(0,10) ) # 20 sec
        pass
    l, r = partition(arr)

end = time.time()

print(end - start)
