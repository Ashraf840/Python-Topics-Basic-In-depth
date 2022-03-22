## The differences between list, tuple, set, dictionary.

## Duplicate Element
# support: List, Tuple,
## Does Not Support: Set
# dictionary doesn't allow duplicate keys.

var_list = [1,2,3,4,5,5]
var_tuple = (1,2,3,4,5,5)
var_set = {1,2,3,4,5,6,6,7,8,9,0}     # eleminate the duplicate 5
var_set_unordered = {2,3,5,7,8,4,2,10,4,6}  # will re-arrange the elems into ascending order. Since they're all integer values datatype.
var_set_unordered_float = {1.1,2.1,9.1,5.1,4.1,3.1,6.1,7.1,8.1}     # will re-arrage into ascending order now, cause all the elements exists in the same datatype (float)
var_set_letter = {'a','f','c','d','e','b'}
# print(var_list)
# print(var_tuple)
# print(var_set)





### Mutability/ Modification
## Support: List, Set, Dictionary
## Does Not Support: Tuple

# try to add a new element inside the 'var_tuple' using the 'append()' function
# var_tuple.append(7)   # throw an error, cause no such func called 'append()' is supported by tuple-type variable

# display all the built-in functions & attributes of the tuple-variable
# for x in dir(var_tuple):
#     print(x)



### Ordered/ Unordered
## Support: List, Tuple, Dictionary
## Does Not Support: Set

# display elements from a list.
# It'll display the elements as given below. Meaning, it'll display the elements in an ordered format based on the index of the list
# for i in var_list:
#     print('Value:', i, '----', 'Index: ', var_list.index(i))


# display elements from a set.
# It'll display the elements in a random order regardless of as the set was initially built.
# for x in var_set:
#     print(x)


# var_set.pop()
# print(var_set)
# print(var_set_unordered) # While showing the unordered set, it'll display all the elems in the ascending format. Moreover, it'll remove all the duplicate elem(s) also.
# print(var_set_unordered_float)
# print(var_set_letter)

# ----- Remove 'Set' Elem using 'pop()' func -----
# print(var_set.pop())
# print(var_set_unordered.pop())
# print(var_set_unordered_float.pop())
# print(var_set_letter.pop())

# ----- Add 'Set' Elem (Char) using 'add()' func -----
# var_set_letter.add('g')
# print(var_set_letter)

# ----- Add 'Set' Elem (String) using 'add()' func -----
myset = {"hi", '2', "bye", "Hello World"}
# myset.add('test')
# print(myset)


# ----- Add 'Set' Elem (Integer) using 'add()' func -----
# myset = {2,3,5,7,8,4,2,10,4,6}  # duplicate 2 (2x); missing elem: 9
# myset = {2,3,5,7,10,8,4,6,9}  # range(2-10): 
# myset = {1,2,3,4,5,7,8,9,10}    # missing elem 6
# myset = {2,3,5,7,10,8,4}
# myset = {2,3,4,5,6,7,8,9,10,11}
myset.add(40)
print(myset)


# print(myset)    # always randomized cause of existing different datatypes
# # loop through the elements of myset
# for a in myset:
#     print(a)
