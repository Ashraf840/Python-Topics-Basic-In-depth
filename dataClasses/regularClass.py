class Car():
    def __init__(self, name, model, color, seat, mileage):
        self.name = name
        self.mdoel = model
        self.color = color
        self.seat = seat
        self.mileage = mileage




# instantiate the "Car" class
car_obj = Car( 'Eleanor', 1967, 'Matte Grey', 2, 7500 )

print( car_obj )