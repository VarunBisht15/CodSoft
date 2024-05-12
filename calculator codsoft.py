print(''' This Is A Basic Calculator Can Perform Operation Between Two Operands''')
          
num1 = int(input("enter first value"))
num2 = int(input("enter second value"))
operator = input('''enter the desired operator
((+ , - , * , / , % , pow )) -: ''')

if operator == "+":
    print(num1+num2)
    
elif operator == "-":
    print(num1-num2)
    
elif operator == "*":
    print(num1*num2)
    
elif operator == "/":
    print(num1/num2)
    
elif operator == "%":
    print(num1%num2)

elif operator == "pow":
    print(pow(num1,num2))
else:
    print("Invalid Operation")
