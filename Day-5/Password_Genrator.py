import random
letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
          'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|' ]
 
print("Welcome to the pypassword generator!")
nr_letter= int(input("How many letters would you like in your password\n"))
nr_digit= int(input("How many digits would you like in your password\n"))
nr_symbols= int(input("How many symbols would you like in your password\n"))


password=[]
final_password=""
for n in range(0,nr_letter):
   password+=random.choice(letter)
for n in range(0,nr_digit):
   password+=random.choice(digits)
for n in range(0,nr_symbols):
   password+=random.choice(symbols)
random.shuffle(password)
for n in password:
    final_password+=n

print(f"Here is your final password:{final_password}")
