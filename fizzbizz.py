userInput = int(input("Please enter a whole number:"))
if userInput % 5 == 0:
    print("Buzz")
elif userInput % 3 == 0:
    print("Fizz")
elif userInput % 3 == 0 and userInput % 5 == 0:
    print("Fizz + " " + Buzz")
else:
    print("Come again!")