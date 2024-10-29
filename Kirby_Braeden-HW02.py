# Braeden Kirby
# UWYO COSC 1010
# 10/28/2024
# HW 02
# Lab Section 13
# Sources, people worked with, help given to:

# I will start off with the input so for the user to use in order to change the plaintext to Morse Code

input_string = input('Please Enter your plaintext/Alphabetical Characters: ')

# I will create a dictionary for the plaintext alphabet to the Morse Code alphabet

morse_code_dictionary = {

        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'

}

# I will then initialize the Morse Code output

morse_code_output = ""

# I will then use a for statement so that each character is able to be processed and swapped to Morse Code

# Within the for statement I will make it so that every character entered is upper case (lower case does not work) so that the case sensitivity in the dictionary does not matter

for char in input_string.upper():
# I can use an if statmenet to check if the character entered is alphabetical or not and to continue with the statement if it is
    if char.isalpha():
# I can add a space the Morse Code so that the output will be correct
        morse_code_output += morse_code_dictionary[char] + " "
# I can make an elif statement so that it checks if there is a space provided, making the output be different than converting to Morse Code
    elif char == ' ':
# I can make an if statment to add a double space to the Morse Code if there is already Morse Code
        if morse_code_output:
# I can make it so there is an extra space if there is Morse Code already present
            morse_code_output += "  "
# I can strip uneeded space(s) and print the correct result
morse_code_output = morse_code_output.strip()

print('Morse Code Tanslation:', morse_code_output)