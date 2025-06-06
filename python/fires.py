userInput = input("Enter the year of your choice: ")

file = open("/home/mathe/algorithms-sm1/python/assets/amazon.csv", "r", encoding="ISO-8859-1")
fires = 0

for line in file:
    line.split(",")
    print(line, line[0], line[3])
    if line[0] == int(userInput) and line[3] > "0":
        fires += 1

print("The number of fires in", userInput, "is", fires)