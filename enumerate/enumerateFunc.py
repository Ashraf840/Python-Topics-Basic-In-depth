# ['enumerate' function]: This built-in function returns the counter with each element of an iteable. 
# This counter can also be used as index of each elem. But this will be wrapped up in a form of enumerating object.
# [enumerated object]: If we convert that enumerated object into a list, then each element of that list will contain a tuple consisting of the counter & the elem itself.


# [Usecase]
#   ---- This enumerated object can be used directly in 'for loop', or converted into a list of tuples.
#   ---- This enumerated object can be used on a string as well, in order to loop over each letter in the string along with there indecies (index/counter).
#           Which can be stored in separatd lists to get the indecies & the letters.
#               [NB]: Here, we can make conditions over storing of indecies & the letters into those list variables.



languages = ['Python', 'Java', 'JavaScript']
# languages = 'JavaScript'


# converted the enumerated object into a list
# print(list(enumerate(languages)))


for index, letter in enumerate(languages):
    print(letter, '-----', index)