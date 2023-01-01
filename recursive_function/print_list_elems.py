# Print all the elements of a list without using any loop; use recursion
# The elements are displayed using negetive indexing, and in every depth, decrease the number used for negetive indexing.
def printElems(arr, n):
    if n < 1:
        return
    print(arr[-n])
    printElems(arr, n-1)

arr = [1,2,3,4,5,6,7,8,9,10]
arrLength = len(arr)
# print(arr[-arrLength+1])
printElems(arr, arrLength)
