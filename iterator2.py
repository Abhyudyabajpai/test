class Count:
    def __init__(self,low,high):
        self.low =low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.low <self.high:
            num = self.low
            self.low +=1
            return num
        raise StopIteration

for n in Count(10,20):
    print(n)