class vehicle:
    company ="xyz motors"

    def __init__(self,n_wheels,n_seats,mileage):
        print("init of vehicle")
        self.n_wheels = n_wheels
        self.n_seats =n_seats
        self.mileage =mileage

    def get_details(self):
        return f"this vehicle has {self.n_wheels} wheel,{self.n_seats} seats and provided a milage of {self.mileage}"
v1 = vehicle(4,7,30)
print(v1.get_details())

class car(vehicle):
    def __init__(self, n_wheels, n_seats, mileage, car_type, drive_type):
        model= '12344'
        print("init of car")
        super().__init__(n_wheels, n_seats, mileage)
        self.car_type = car_type
        self.drive_type = drive_type


# car class inhetist the vehive class
# car class is called child class child /derived class 
# vehicle class is called parent clas /base class 

c1 = car(4, 5, 6, "sedan", "automatic")
print(c1.mileage)
print(c1.get_details())

c4 = car(4, 5, 20, "suv", "manual")
print(c4.mileage)
print(c4.get_details())
