# Topics: Python Generators


# Pass a list as param
# def squared_nums(nums):
#     result = []     # empty list
#     for i in nums:
#         result.append( i*i )
#     return result

# print( squared_nums( [1,2,3,4,5] ) )





# Create a generator function, it'll behave like the build-in "range()" function
def my_range(start, end):
    current = start
    while current < end:
        yield current   # it will yield(produce/bring/provide) the value in order to keep the state of the value in the program runtime.
        current += 1



# Use the "my_range()" function to loop through a range of number (0-10)
nums = my_range(1,10)


# The generator function can be iterate by using the "for-loop"
# for num in nums:
#     print(num)



# The generator function "my_range()" can be iterate using the "next()" method.
print( next( nums ) )
print( next( nums ) )
print( next( nums ) )
print( next( nums ) )
print( next( nums ) )
print( next( nums ) )
print( next( nums ) )
