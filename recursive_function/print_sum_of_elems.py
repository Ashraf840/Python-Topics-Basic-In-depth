# Print the sum of all the elements of a list without using any loop; use recursion
# Since I want to return the sum from the recursive function, the variable requires to be returned while the condition meets as well as the recursive function needs to be returned, otherwise the recursive func won't be able to return anything.
def sumOfElems(arr, n, result):
    if n < 1:
        # print(result)
        return result
    result += arr[-n]
    return sumOfElems(arr, n-1, result)

arr = [1,2,3,4,5,6,7,8,9,10]
arrLength = len(arr)
result = 0
# print(arrLength)
print(sumOfElems(arr, arrLength, result))
# x = sumOfElems(arr, arrLength, result)
# print(x)