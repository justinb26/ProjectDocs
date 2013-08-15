def rot13(text):
    list_of_letters = []                        ## This will hold our new string
    
    for letter in list(text):                   ## for each of the letters in our text
        letter_code = ord(letter)               ## change the letter to an ascii code (number)
        
        if letter.isalpha():                    ## If it's a code for a letter
            if chr(letter_code + 13).isalpha(): ## And it's still a number when we add 13
                letter_code += 13               ## Then add 13
            else:                               ## Otherwise
                letter_code -= 13               ## Subtract 13

        list_of_letters.append(chr(letter_code))## Convert back to letter, and add to new list
    
    return ''.join(list_of_letters)             ## Convert list back to text, and return it

#########################################################

my_input = input("Text to be rot13'ed: ")

print(rot13(my_input))
