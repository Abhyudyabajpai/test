class sea:
    def __init__(self,name):
        self.name = name
    def swim(self):
        return f"{self.name} can swim"
class land:
    def __init__(self,name):
        self.name = name
    def run(self):
        return f"{self.name} can run"

class Penguin(land,sea):
    def __init__(self,name):
        super().__init__(name = name)

fish = sea("Fish")
tiger = land("Tiger")
Man = Penguin("Man")
print(fish.swim())
print(Man.swim())
print(Man.run())