
def encode(texts,number):
    cipher_text = ""
    for a in text:
        if a in letter:
            position = letter.index(a)
            new_position = letter[position+shift]
            cipher_text += new_position
        else:
            cipher_text+=a
    print(f"The encoded text is:{cipher_text}")

def decode(text, number):
    decodeed_text=""
    for a in text:
        if a  in letter:
            position = letter.index(a)
            new_position = letter[position-shift]
            decodeed_text += new_position
        else:
            decodeed_text+=a
    print(f"The encoded text is:{decodeed_text}")


should_continue= True
while should_continue:
    letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction= input("Type 'encode' to encrypt, type the 'decode' to decrpyt:\n")
    text= input("Type your message:\n").lower()
    shift=int(input("Enter the shift number:\n")) % 26

    if direction == 'encode':
        encode(text,shift)
    elif direction == 'decode':
        decode(text,shift)
    else:
        print("You enter a wrong direction")
    re_start=input("If you want to restart Type 'yes' otherwise 'no'\n").lower()
    if re_start == 'no':
        should_continue = False
    else:
        print("You enter the wrong command")
