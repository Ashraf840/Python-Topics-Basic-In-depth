# Link:  https://www.youtube.com/watch?v=jTYiNjvnHZY

# Build a class, which behaves like the build-in "range()" function.


# Iterator Class
# Want to make this class iterable.
# [ NOTE ]: TO make something to be iterable, it requires a dunder-iter method.
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    # dunder-iter() method has to return an iterator. By that mean, this method has to return a class-object which has a dunder-next() method.
    def __iter__(self):
        return self     # returning the dunder-iter method using "self", cause it'll return the dunder-next method by returning an iterator object.

    # dunder-next method
    def __next__(self):
        # to check if the iterable has any more value.
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current



# The class above can be iterable, also they are iterator itself cause it's now returning the dunder-next() mnethod.
# Thus we can use the for-loop on the class-object as well as can use the "next()" method to the class-object directly.
# num = MyRange(startVal, EndVal)
num = MyRange(0, 10)

# make a manual-for-loop of the variable "num"
# for n in num:
#     print(n)



print('\n'*5)

# But, since our class "MyRange()" is an iterator, we can directly use the "next()" method.
# [ NB ]: comment-out the for loop for the iterator-class-object before using the "next()" method on that object.
print( 'Using the "dunder-next()" method in the iterator-class-object "num"' )
# using the "next()" method for 10x
print( next( num ) )
print( next( num ) )
print( next( num ) )
print( next( num ) )
print( next( num ) )
print( next( num ) )
print( next( num ) )
print( next( num ) )
print( next( num ) )
print( next( num ) )