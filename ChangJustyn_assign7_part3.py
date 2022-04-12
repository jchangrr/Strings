"""
Assignment #7, Part 3
Justyn Chang
"""
#ask for seed and validate
seed = input("Enter a six digit seed: ")
while len(seed) != 6:
    print("Invalid seed, please try again")
    print()
    seed = input("Enter a six digit seed: ")
while seed.isnumeric() == False:
    print("Invalid seed, please try again")
    print()
    seed = input("Enter a six digit seed: ")

#ask for low and high and validate
low = str(input("Enter lowest possible random integer: "))
high = str(input("Enter highest possible random integer: "))
while low.isnumeric() == False:
    print("Invalid low/high values, please try again.")
    print()
    low = input("Enter lowest possible random integer: ")
    high = input("Enter highest possible random integer: ")
while high.isnumeric() == False:
    print("Invalid low/high values, please try again.")
    print()
    low = input("Enter lowest possible random integer: ")
    high = input("Enter lowest possible random integer: ")
while int(high) <= int(low):
    print("Invalid low/high values, please try again.")
    print()
    low = input("Enter lowest possible random integer: ")
    high = input("Enter highest possible random integer: ")

print()
#ask for how many numbers to be generated and validate
generate = str(input("How many random numbers do you want to generate? "))
while generate.isnumeric() == False:
    print("Invalid, try again")
    print()
    generate = str(input("How many random numbers do you want to generate? "))
while int(generate) <= 0:
    print("Invalid, try again")
    print()
    generate = str(input("How many random numbers do you want to generate? "))

print()
#create loop for number of generated numbers
for i in range(int(generate)):
    #print seed value
    print("Seed value: ", seed)

    #square seed value
    square = int(seed) * int(seed)
    print("Square of seed: ", square)

    #find middle of seed value
    count = len(str(square))//4
    square = str(square)
    midsquare = square[count]+square[count+1]+square[count+2]+square[count+3]+square[count+4]+square[count+5]
    print("Middle 6 digits of square: ", midsquare)

    #calculate percentage
    percent = int(midsquare)/999999
    print("Percentage =", midsquare, "/ 999999 =", percent)

    #scale number to an integer
    print("Scaling up to a number between", low,"and", high)
    scale = (int(high) - int(low)) * percent + int(low)
    print("(", high, " - ", low, ") * ", percent, " + ", low, " = ", scale, sep = "")

    convert = int(scale // 1)
    print("Converted to an integer: ", convert)
    print()

    seed = int(midsquare)
