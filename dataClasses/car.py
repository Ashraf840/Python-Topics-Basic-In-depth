# implement the equal_to, not_euqal_to, greater_than, less_than, greater_than_or_equal_to , less_than_or_equal_to functions to the class "Car".
# the dunder-function for these aforementioned methods are accordingly "__eq__", "__ne__", "__gt__", "__lt__", "__ge__", "__le__" 


class Car():
    def __init__(self, weight):
        self.weight = weight

    # Check if the instances of the class is equal to other instance. returns Boolean
    def __eq__(self, __o) -> bool:
        return self.weight == __o.weight


    # Check if the instances of the class is equal to other instance. returns Boolean
    def __ne__(self, __o) -> bool:
        return self.weight != __o.weight


    # check if an instances of the class is greater than the other. returns Boolean
    def __gt__(self, __o) -> bool:
        return self.weight > __o.weight


    # check if an instances of the class is less than or equal to the other. returns Boolean
    def __lt__(self, __o) -> bool:
        return self.weight < __o.weight
    

    # check if the instances of the class "Car" is greater than the other. Returns in booelan 
    def __ge__(self, other) -> bool:
        return self.weight >= other.weight
    

    # check if the instances of the class "Car" is less than or equal to the other. Returns in booelan 
    def __le__(self, other) -> bool:
        return self.weight <= other.weight




# create two instances of the class "Car"
car_obj1 = Car( 1700 )
car_obj2 = Car( 1600 )




print( 'Equal To: ', car_obj1 == car_obj2 )
print( 'Not Equal To: ', car_obj1 != car_obj2 )
print( 'Greater Than: ', car_obj1 > car_obj2 )
print( 'Less Than: ', car_obj1 < car_obj2 )
print( 'Greater Than or Equal To: ', car_obj1 >= car_obj2 )
print( 'Less Than or Equal To: ', car_obj1 <= car_obj2 )




