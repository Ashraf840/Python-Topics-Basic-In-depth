# Generate a class, also use the dataclass as a decorator

from dataclasses import dataclass


@dataclass
class Car():
    # don't require to create the constructor of the class (initializer), just need to pass the variables along with defining their data-types explicitly.
    name: str
    model: str
    color: str
    seat: int
    mileage: float



    # Check if the instances of the class is equal to other instance. returns Boolean
    def __eq__(self, __o) -> bool:
        return self.mileage == __o.mileage


    # Check if the instances of the class is equal to other instance. returns Boolean
    def __ne__(self, __o) -> bool:
        return self.mileage != __o.mileage


    # check if an instances of the class is greater than the other. returns Boolean
    def __gt__(self, __o) -> bool:
        return self.mileage > __o.mileage


    # check if an instances of the class is less than or equal to the other. returns Boolean
    def __lt__(self, __o) -> bool:
        return self.mileage < __o.mileage
    

    # check if the instances of the class "Car" is greater than the other. Returns in booelan 
    def __ge__(self, other) -> bool:
        return self.mileage >= other.mileage
    

    # check if the instances of the class "Car" is less than or equal to the other. Returns in booelan 
    def __le__(self, other) -> bool:
        return self.mileage <= other.mileage


# instantiate the object of the clas "Car"
# [ NOTE ]:  The comparison between two instances is identically an ease.
car_obj1 = Car( 'Eleanor', 1967, 'Matte Grey', 2, 7500 )
car_obj2 = Car( 'Supra', 2002, 'Cherry Red', 2, 6000 )

# It'll give a more readable object along with the variables & their values.
print( car_obj1 )
print( car_obj2 )

print()
print( '*'*20 )
print( '*'*20 )
print()

print( 'car_obj1 is equal to car_obj2:', car_obj1 == car_obj2 )
print( 'car_obj1 is not equal to car_obj2:', car_obj1 != car_obj2 )
print( 'car_obj1 is greater than car_obj2:', car_obj1 > car_obj2 )
print( 'car_obj1 is less than car_obj2:', car_obj1 < car_obj2 )
print( 'car_obj1 is greater than or equal to car_obj2:', car_obj1 >= car_obj2 )
print( 'car_obj1 is less than or equal to car_obj2:', car_obj1 <= car_obj2 )

