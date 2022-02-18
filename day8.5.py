
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#def encrypt(p_text,shift_num):
#    cipher_text = ""
#    for i in p_text:
#        position = alphabet.index(i)
#        new_position = position + shift_num
#        new_letter =  alphabet[new_position]
#        cipher_text += new_letter
#        
#
#    print(f"The encoded text is {cipher_text}")
#
#
#def decrypt(cip_txt, shift):
#    decode = ""
#    for l in cip_txt:
#        c_position = alphabet.index(l)
#        deco_position = c_position - shift
#
#        decoded_letter = alphabet[deco_position]
#        decode += decoded_letter
#    print(f"The decoded text is {decode}")
#
#        
#
#    
#if direction == "encode":
#    encrypt(p_text = text,shift_num = shift)
#elif direction == "decode":
#    decrypt(cip_txt = text , shift = shift)


def cipher(direction,text,shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift
        elif direction == "decode":
            new_position = position - shift
        new_letter =  alphabet[new_position]
        cipher_text += new_letter
    print(f"your {direction} message is {cipher_text}")

cipher(direction,text,shift)




