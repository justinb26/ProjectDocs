import codecs

input_text = input("Text to be ROT13'd: ")
rot_text = codecs.encode(input_text, "rot_13")

print(rot_text)
