def beautifulTriplets(d, arr):
    result = 0
    for i in range(len(arr) - 2) :
        count = 0
        for j in range(i + 1, len(arr)) :
            a  = arr[j]
            b = arr[i]
            if arr[j] - arr[i] == d :
                count = count + 1
                i = j
            if count == 2:
                result = result + 1
                break
    
    return result


print(beautifulTriplets(3, [1, 2, 4, 5, 7, 8, 10]))