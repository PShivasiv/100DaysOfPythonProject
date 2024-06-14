# You have to find the way to the treasure by give the answer for the questions and if you'll give all the right answers you get the congratulation message.
print('Welcome to the treasure island game')
print("Your mission is to find the treasure")
First=input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
second = ""
third = ""
if First == 'right':
     second=input('You successfully cross the road. Now you have to cross the lake and reach the island middle of the lake.Type "wait"or "swim"\n').lower()
else:
    print("You crash with truck, Game over ")
if second == "wait":
    third=input('You reach the island by waiting for a boat.Now you have three door and one door take you to the treasure cheast pick the right one.\n Type "Red" , "yellow" or "blue"')
elif second == "swim":
    print("You're Game over. You hunted by pirana fish by swining across the lake.")
if third == "red":
    print("you won the came you successfully find the treasure cheast.")
    print('''      _---_                _---_
     (     )              (     )
      \   /       _---_    \   /
 _---_ \/        (     )    \/
(     )|  _---_   \   /      |    _---_
 \   / | (     )   \/    _---_|  (     )
  \/   |  \   /     |   (     )   \   /
   |  |    \/       |    \   /|    \/
    | |     |        |     \/ |     |
     | |  __/          |    | |     |
      || /              |   | |    |
      |||                |   ||   |
       ||                 |  ||  /
        |                   \ || |
        |                    ||||
         |                     ||''')
elif:
    print("Game Over. you choose the wrong gate.")
