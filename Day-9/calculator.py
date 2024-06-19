def calcultor(value,operator,value2):
    if operator == '+':
        result=value+value2
        return(result)
    elif operator == '-':
        result=value-value2
        return(result)
    elif operator == '*':
        result=value*value2
        return(result)
    elif operator == '/':
        result=value/value2
        return(result)
    
number=int(input("What's the first number?:"))
print("+\n-\n*\n/\n")
symbol=input("Pick an operation:")
number2= int(input("What's the next number?:"))
result=calcultor(number,symbol,number2)


condition=True
while condition:
    print(f"{number} {symbol} {number2} = {result}")
    restart=input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation :").lower()
    if restart == "y":
        re_symbol= input("Pick the symbol:")
        re_value=int(input("What's the next number?:"))
        result2=calcultor(result,re_symbol,re_value)
        number=result
        symbol=re_symbol
        number2=re_value
        result=result2

    else:
        condition=False
