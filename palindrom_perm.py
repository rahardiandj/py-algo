
def HasPalindromePermutation(input):
    str = input.strip()

    startAscii = 97

    arrStr = [0] * 26

    for c in str:
        aIdx = ord(c)
        arrStr[aIdx-startAscii] = arrStr[aIdx-startAscii] + 1

    return not checkOddMoreThanOne(arrStr)


def checkOddMoreThanOne(arr):
    isMoreThanOne = False

    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            if isMoreThanOne:
                return True     
            isMoreThanOne = True    

    return False

# print(checkOddMoreThanOne([2,2,1,0,0]))  

print(HasPalindromePermutation("abcbba"))
