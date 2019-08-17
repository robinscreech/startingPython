ages = {}
ages["john"] = 25
ages["Dan"] = 30


print(ages["john"])

ages["john"] = 10

print(ages["john"])

print(ages.keys())

print(list(ages.keys()))

print(ages.values())

print(list(ages.values()))

print("john" in ages)

newages = dict(Car = 20, bike = 10, house = 1)
print(newages)
