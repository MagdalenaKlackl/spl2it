import random
random.seed()

arr2 = []

for i in range(1,46):
    arr2.append(i)

arr1 = []



for nummer in range(1,7):
		arr1.append(random.randint(1,45))
		arr2.pop(nummer)

print("Die Lottozahlen sind:", arr1)


