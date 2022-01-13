class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age



# Create two instances of the "Person" class.
john = Person( 'john', 14 )
jane = Person( 'jane', 14 )



# [ NOTE ]:  Suppose we want to compare two instances of the class "Person" based on the "age" attribute. 
#       Without using the "__eq__" method, the two instances will always return false.


# Will always return "False", since we are mentioning on which attribute, the objects will be comapared.
# print( john is jane )   # return "False"
# print( john == jane )   # return "False"






# #######################
# Create another class "Person2" with the dunder method "__eq__".


# Ref:  https://www.pythontutorial.net/python-oop/python-__eq__/
# #######################




class Person2():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # specify the class attribute, based on which the instances of this class will be compared.
    # we can compare the instances of this class by using the "is" or "==" operators
    def __eq__(self, other):
        return self.age == other.age



person2_obj1 = Person2( 'Nadira', 19 )
person2_obj2 = Person2( 'Azwad', 19 )


print( 'person2_obj1 ID: ', id(person2_obj1) )
print( 'person2_obj2 ID: ', id(person2_obj2) )

# [ NOTE ]:  the "is" operator checks if the two objects are stored in the same memory location.

print( person2_obj1 is person2_obj2 )   # using the "is" oeprator, we're checking whether the two objects are in the same memory locations.
print( person2_obj1 == person2_obj2 )   # with the "==" operator, we're checking the values of the two objects, in this case, it's validating the "age" attribute of the two instances.




