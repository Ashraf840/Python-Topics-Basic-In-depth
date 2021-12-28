# [ NOTE ]: A list is iterable but it's not an iterator.
#   Understand what is an iterator & what is iterable.
#   Understand the concept of iterators to write better, efficient code.





# ####################
# Iterable: Something that can be looped over.
# i.e.  List, Tuple, 

# [ NOTE ]: We cna loop over tuples, dictionaries, strings, files, generators & all kind of different objects.
#   How can we know if something can be looped over? On the other words, how can we say if something is iterable?
#   =>  To view if something is iterableor not, we can pass that variable inside the built-in "dir()" func & find if the dunder/magic method called "__iter__()" is avaiable for that variable.
#           Thus, if there is dunder-iter method avaiable for the variable, then the variable is ITERABLE.
# ####################


num = [ 1,2,3 ]

for x in num:
    print(x)


print()

# The "dir()" method tries to return a list of valid attributes of an object.
print( dir(num) )   # check if the variable has a dunder-iter method

# loop through all the available built-in methods for the variable.
for d in dir(num):
    print(d)

print()
# making list into list-iterator
print( iter(num) )  # making the list-type variable into list-iterator object
print( type( iter(num) ) )  # return a list_iterator


# making list into list-iterator. In two types
i_nums = num.__iter__()    # same Code; making a list_iterator
i_nums = iter( num )    # same Code; making a list_iterator; the "iter()" method calls the dunder-iter method

# Check for the dunder-iter method & dunder-next method
print( dir(i_nums) )

print('\n'*5)

# [ NOTE ]: since the "next()" method remembers where it left of, it continues to print the next value of an iterable.
#   But, when an iterator runs out of value, it raises an "StopIteration" exception. 
print( next( i_nums ) ) # returns the first elem of the list
print( next( i_nums ) )
print( next( i_nums ) )
print( next( i_nums ) ) # it'll raise an exception






# ####################
# ITERATOR: An iterator is an object with a state, so it remembers where it is during iteration.
# An iterator also knows how to get the next value. It gets its next value with a dunder-next method. 
# [ NOTE ]:  A list doen't have a dunder_next method, thus it doesn't have a state and how to get it's next value. 
#       But, if we throw a list inside the dunder-iter method, then it'll provide an ITERATOR for us.
# An iterator is an object with a "State", so it knows where the last iteration it left off. 
#   An iterator can only progress forward, it can't go backward.



# [ NOTE ]: The "next()" func calls the dunder-next func in the background.
#           The "iter()" func calls the dunder-iter func in the background.
# ####################