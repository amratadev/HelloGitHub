def caesar_cipher(text,shift,mode='encrypt'):
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    for char in text.upper():
        if char in alphabet:
            idx=alphabet.index(char)
            if mode=='encrypt':
                new_idx=(idx+shift)%26
            else:
                 new_idx=(idx-shift)%26
            result+=alphabet[new_idx]
        else:
             result+=char
    return result
text=input("enter text:")
shift=int(input("enter shift key:"))
encrypted=caesar_cipher(text,shift,mode='encrypt')
print("encrypt:",encrypted)
decrypted=caesar_cipher(text,shift,mode='decrypt')
print("decrypt:",decrypted)

