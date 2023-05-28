class vehicle:
    def __init__(self):
        max_speed=60
        mileage=10
        self.max_speed=max_speed
        self.mileage=mileage
    def seating_capacity (self,capacity):
        print (f"the seating capacity of the bus is {capacity} passengers")
class bus (vehicle):
    def __init__(self,colour):
        super().seating_capacity(50)
        self.colour=colour
        print(colour)
a=bus("white")
