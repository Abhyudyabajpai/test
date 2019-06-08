def sum_odds(num):
    t = 0
    for n in num:
        if n %2 != 0:
            t += n
    return t 

print(sum_odds([1,2,3,4,5,6,7,8]))