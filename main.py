
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher_ed(encrypted_text,shift_amount, cipher_direction):
   #empty list to hold the encrypted text
  cipher_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  #Looping throught the text
  for letter in encrypted_text:
    if letter in alphabet:
      position = alphabet.index(letter) #finding the position of the letter in the alphabet list
      new_position = position + shift_amount #adding the shift amount to the position
      cipher_text += alphabet[new_position] #adding the new letter to the cipher text
  else:
    cipher_text += letter
  print(f"The {cipher_direction}d text is {cipher_text}")  
end = False
while not end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  cipher_ed(encrypted_text = text,shift_amount = shift ,cipher_direction = direction)
  restart = input("Do you want to restart the cipher program? Type 'yes' or 'no'.\n")
  if restart == "no":
    end = True
    print("Goodby")
  
    
  

