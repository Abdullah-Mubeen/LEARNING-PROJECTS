
def get_number(number):
    while True:
        operend_1 = input("Number " + str(number) + ": ")
        try: 
            return float(operend_1)            
        except:
            print("Invalid number, try again.")


operend_1 = get_number(1);
operend_2 = get_number(2);
operator = input("Sign: ")

 
result = None
if operator == "+":
    result = operend_1 + operend_2
elif operator == "-":
    result = operend_1 - operend_2
elif operator == "/":
    if operend_2 != 0:
        result =  operend_1 / operend_2
    else:
        print("Division by zero")
elif operator == "*":
    result = operend_1 * operend_2
elif operator == "%":
    result = operend_1 % operend_2
else:
    print("Invalid Sign!")



print(result)