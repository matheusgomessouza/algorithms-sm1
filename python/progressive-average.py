sum = 0

for i in range(10):
    inputValue = int(input("Type a number: "))
    sum += inputValue
    if i >= 1:
        print("The current sum is: "  + str(sum) + " | The current index is: " + str(i))
        average = sum / (i + 1) if i == 1 else sum / i
        print("The average is: " + str(average))
