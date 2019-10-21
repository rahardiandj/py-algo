from math import sqrt, ceil

def countingValleys(n, s):
    count = 0
    l = 0
    for i in range(n):
        if s[i] =='U':
            l = l+1
        if s[i] == 'D':
            l = l-1

        if l == 0 and s[i] == 'U':
            print("index",i)
            count = count + 1
    return count


# print(countingValleys(12,"DDUUDDUDUUUD"))

# def solution(A):
#     # write your code in Python 3.6 1
#     A.sort()# 1 1 2 3 4 6 
#     print(A)
#     if A[len(A)-1] < 0 :
#         return 1
#     else :
#         for i in range(len(A)-1) :
#             if ((i < len(A) -1) and (A[i+1] - A[i] > 1)) :   
#                 return A[i] + 1
                
#         return A[len(A)-1] + 1

# A = [1,3,6,4,1,2]
# B = solution(A)
# print(B)


# def solution(ranks):
#     # write your code in Python 3.6
#     sum = 0
    
#     ranks.sort() # 0 0 0 2 2 3 3 3 4
    
#     last = len(ranks) - 1
#     count  = 0
#     for i in range(last):
#         if i < last :
#             if (ranks[i+1] - ranks[i]) == 1 :   
#                 sum = sum + count
#             if ranks[i+1] == ranks[i] :
#                 count = count + 1   
#             else :
#                 count = 1
    
#     return sum

# A = [3, 4, 3, 0, 2, 2, 3, 0, 0]
# print(sqrt(1000000))

def solution(A, B):
    # write your code in Python 3.6
    maxIt = ceil(sqrt(B))
    count = 0
    max = 0
    s = 0
    for i in range(2,maxIt+1):
        
        while i * i <= B:
            i = i * i
            count  = count + 1
            s = i
            
        if (max < count) and ( s >= A) :
            max = count
        
        count = 0
            
    return max

print(solution(17,82))