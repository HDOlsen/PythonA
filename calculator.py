import calculatorapp

def userInput():
    numberone = float(input("Enter number one:"))
    operand = input("Enter your operand (+, -, *, /):") 
    numbertwo = float(input("Enter your number two:"))
    return (numberone, operand, numbertwo)

(numberone, operand, numbertwo) = userInput()

if operand == "+":  
    print(numberone, "+", numbertwo, "=", calculatorapp.add(numberone, numbertwo))
elif operand == "-":  
    print(numberone, "-", numbertwo, "=", calculatorapp.subtract(numberone, numbertwo))
elif operand == "*":  
    print(numberone, "*", numbertwo, "=", calculatorapp.multiply(numberone, numbertwo))
elif operand == "/":  
    print(numberone, "/", numbertwo, "=", calculatorapp.divide(numberone, numbertwo))
