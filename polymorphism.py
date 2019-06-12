class A:
    def color(self):
        raise NotImplementedError("Subclass must implement the method")

class B (A):
    def color(self):
        return "Returning black from B"

class C (A):
    pass

x = B()
y = C()
print(x.color())
print(y.color())

