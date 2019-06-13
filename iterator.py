def for_loop(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

for_loop("Quartz")
for_loop((1,2,3))