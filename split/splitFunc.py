"""
The "split()" function splits a string / sentence into a list.
We can define a separator into the function, while the default separator is any whitespace.

Syntax:   text.split(separator, maxsplit)
separator => This will control the splitting point based on the value.
maxsplit => This will define how may split be done from the string / sentence. The rest will be another whole element.
"""



txt = 'This is a good book'

# this will convert each word into a list element, cause the default splitting value is a white space.
print(txt.split())
"""
Output
['This', 'is', 'a', 'good', 'book']
"""




# this will create 3 elements into a list, the splitting is also done on whitespaces
print(txt.split(' ', 2))
"""
Output
['This', 'is', 'a good book']
"""

