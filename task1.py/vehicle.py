class Vehicle:
   
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
     
        self.owner = new_owner

car = Vehicle("ABC123", "Car", "John Doe")
bike = Vehicle("DEF456", "Bike", "Jane Smith")

print("Car owner:", car.owner)
print("Bike owner:", bike.owner)

car.update_owner("Alice Brown")

print("\nCar owner:", car.owner)
print("Bike owner:", bike.owner)