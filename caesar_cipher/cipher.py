alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

from art import logo
print(logo)

def encrypt(plain_text,shift_amount):
    cipher_text=''
    for letter in plain_text:
        position= alphabets.index(letter)
        new_position= (position + shift_amount)%26
        new_letter=alphabets[new_position]
        cipher_text += new_letter
    print(f"The encoded text is: {cipher_text}")    


def decrypt(cipher_text,shift_amount):
    plain_text=''
    for letter in cipher_text:
        position= alphabets.index(letter)
        new_position= (position - shift_amount)%26
        new_letter=alphabets[new_position]
        plain_text += new_letter
    print(f"The decoded text is: {plain_text}")

should_end = False
while not should_end:
    direction=input("Enter 'encode' to encrypt or 'decode' to decrypt: \n")
    text=input("Type your message: \n").lower()
    shift=int(input("Enter number of shifts: \n"))
    
    if direction == 'encode':
        encrypt(plain_text=text,shift_amount=shift)
    elif direction == 'decode':
        decrypt(cipher_text=text,shift_amount=shift)
    else:
        print("Invalid direction")
        
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")