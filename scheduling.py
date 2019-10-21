a = [[1, 4], [5, 6], [8, 9], [2, 6]]
b = sorted(a, key=lambda x: x[0], reverse=False)

def getNumOfRoom(arr) :
    numOfRoom = 1
    size = len(arr)
    interval = {} 

    maxInterval = 0

    for i in range(0, size-1):

        for ival in range(arr[i][0], arr[i][1]):
            if ival in interval :
                interval[ival] += 1
            else :
                interval[ival] = 1

    for i in interval.values() :
        if maxInterval < i :
            maxInterval = i
    
    return maxInterval

print(getNumOfRoom(b))