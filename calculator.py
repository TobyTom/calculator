# 17-4-2023
operator = input("What arithmetic operation would you like to perform? Select it by only typing the sign in bracket \n 1. Addition (+) \n 2. Subtraction (-) \n 3. Multiplication (*) \n 4. Division (/): \n" )
# if operator == "+" or "-" or "*" or "/":
#     print("Continue your operation")
# else:
#     print("Invalid operator selected")
fval = input("Enter your first value: ")
sval = input("Enter your second value: ")

if operator == "+" :
    print ("The result of your addition operaton is " + str(float(fval) + float(sval)))
elif operator == "-":
    print ("The result of your substraction operation is " + str(float(fval) - float(sval)))
elif operator == "*":
    print ("The result of your multiplcation operation is " + str(float(fval) * float(sval)))
elif operator == "/":
    print ("The result of your division operation is " + str(float(fval) / float(sval)))
else:
    print("Invalid operation")