import string

rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

input_text = input("Text to be rot13'ed: ")
rot_text = string.translate(input_text, rot13)

print(rot_text)
