import random
print("GUESS THE NAME FROM THE ONEPIECE CREW")
word_list=["luffy","robin","nomi","ussap","franky","zoro","sanji","chooper","brook","jinbei"]     
life=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
live=0
letter_choose=random.choice(word_list)
# print(f'{letter_choose}')

disp=[]
for i in range(len(letter_choose)):
    disp  +="_" 

end_of_the_game = False

while not end_of_the_game:
    guess=input("Guess letter in correct position:").lower()
    
    for position in range(0,len(letter_choose)):
        i = letter_choose[position]
        # print(f"Curreny position:{position}\n Curren letter:{i}\n guessed letter:{guess}")
        if i == guess:
            disp[position]=i
    
    if guess not in letter_choose:  
        live+=1
        print(f"You loss {live} life")
        if live == 6:
            end_of_the_game= True
    print(f"{' '.join(disp)}")

    if "_" not in disp:
        end_of_the_game= True
        print("YOU WIN")
    print(life[live])
