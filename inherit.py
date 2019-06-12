class Vehicle:
    drive = True
    def __init__(self,capacity):
        self.capacity = capacity
    def __repr__(self):
        return f"This vehicle has capacity of {capacity} and the model is {model}"

class Car(Vehicle):
# this class can inherit the properties of class Vehicle
    def __init__(self,capacity,model):
        super().__init__(capacity)
        self.model = model

Honda = Car(8,2019)
print(Honda.model)
