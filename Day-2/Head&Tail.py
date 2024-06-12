import random
choice=int(input('Head for "0" tail for "1"\n'))
random_int=random.randint(0,1)
print(random_int)
if choice == random_int:
    print(f"You win the game.The result is {random_int}")
else:
    print(f"You loss the game.The result is {random_int}")
