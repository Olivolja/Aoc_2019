import math
mymasses = open("aoc_2019/1/aoc_1.txt").read().split("\n")
mymasses = [int(x) for x in mymasses]

# print(mymasses)
def aoc(masses):
    fuel = 0
    for mass in masses:
        f = math.floor(mass/3) - 2
        fuel += f 
    return fuel 

print(aoc(mymasses))

def aoc2(mass):
    fuel = (math.floor(mass/3) - 2)
    if(fuel < 0):
        return 0
    else:
        return fuel + aoc2(fuel)

sum = 0
for mass in mymasses:
    sum += aoc2(mass)

print(sum)



def aoc2norec(masses):
    sum = 0
    for mass in masses:
        partsum = 0
        f = math.floor(mass/3) - 2
        while f > 0:
            partsum += f
            f = math.floor(f/3) - 2
        sum += partsum
    return sum

print(aoc2norec(mymasses))