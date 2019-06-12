class Vehicle:
    drive = True

    def space(self,capacity):
        print(f"This vehicle has capacity of {capacity}")

class Car(Vehicle):
# this class can inherit the properties of class Vehicle
    pass         
Honda = Car()
Honda.space(8)
print(Honda.drive)
