# this my first program in python
# simple Calculator
operand_1 = int(input("Enter the first num : "))
operation = (input("Enter the operation : "))
operand_2 = int(input("Enter the second num : "))

if operation == '+':
    ret = operand_1 + operand_2
    print("the result is :"+" "+str(ret))
elif operation == '-':
    ret = operand_1 - operand_2
    print("the result is :"+" "+str(ret))
elif operation == '*':
    ret = operand_1 * operand_2
    print("the result is :"+" "+str(ret))
elif operation == '/':
    if operand_2 ==0:
        print("Division by zero invalid")
    else:
        ret = operand_1 / operand_2
        print("the result is :"+" "+str(ret))
else:
    print("invalid operation")
