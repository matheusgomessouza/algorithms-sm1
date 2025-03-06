import random

sum = 0

for i in range(10):
    inputValue = random.randint(1, 10)
    print('The ')
    sum += inputValue

average = sum / 10
print("The average is: " + str(average))