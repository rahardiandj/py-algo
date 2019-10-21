def getMoneySpent(keyboards, drives, b):
    keyboards.sort(reverse=True)
    drives.sort()

    m = 0
    maxV = -1
    for i in range(len(keyboards)) :
        for j in range(m,len(drives)) : 
            if keyboards[i] + drives[j] > b :
                m = m + 1
                break
            if keyboards[i] + drives[j] > maxV :
                maxV = keyboards[i] + drives[j]
    
    return maxV

keyboards = [3,1]
drives = [5,2,8]
print(getMoneySpent(keyboards, drives, 10))