## A = 65, Z=90
## a = 97, z=122input_text = input("Text to be rot13'ed: ")
input_text = input("Text to be rot13'ed: ")
list_of_letters = list(input_text)

letterindex = 0

for letter in list_of_letters:
    
    letter_code = ord(letter) ## change to an ascii number

    if letter_code >= 65 and letter_code <= 90: ## Uppercase Letters
        letter_code = letter_code + 13
        if letter_code > 90:
            letter_code = 65 + (letter_code - 90 - 1)

    elif letter_code >= 97 and letter_code <= 122: ## Lowercase Letters
        letter_code = letter_code + 13
        if letter_code > 122:
            letter_code = 97 + (letter_code - 122 - 1)

    letter = chr(letter_code) ## back to a letter
    
    list_of_letters[letterindex] = chr(letter_code) ## replace letter in list
    letterindex += 1

my_output_text = ''.join(list_of_letters)

print(my_output_text)
