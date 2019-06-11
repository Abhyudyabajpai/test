class info:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def fav_color(self,color):
        return f"{self.first} {self.last} likes {color}"

u1 = info("Sherlock","Holmes")
u2 = info("Robert","Loius")
print(u1.fav_color("purple"))
print(u2.fav_color("red"))