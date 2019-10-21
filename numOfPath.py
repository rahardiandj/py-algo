# def numOfPath(m,n):
#     print('{0},{1}'.format(m,n)) 
#     if ((m==1) or (n==1)):
#         return 1

#     return numOfPath(m-1, n) + numOfPath (m,n-1)


# print(numOfPath(3,3))

# def factorial(n):
    
#     if (n == 1) or (n==0) :
#         return 1
#     c = n * factorial(n-1)
#     print(c)
#     return c


# print(factorial(3))

def reverse_str(string):
    print(string)
    if (len(string) < 2): 
        return string
    
    return reverse_str(string[1:len(string)]) + string[0]

print(reverse_str("abcde"))