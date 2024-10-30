# Braeden Kirby
# UWYO COSC 1010
# 10/29/2024
# HW 02
# Lab Section 13
# Sources, people worked with, help given to: 

# Assignment Information:
# For this homework assignment you will be writing a program that translates between plaintext and Morse Code.

# When your program first starts it should ask the user for the input string. If plaintext alphabet cahracters 
# is entered output the Morse Code equivalent.

# You may assume that only alphabet characters will be entered, and may ignore other input characters.

# You can use the equivalencies below.

#A: .-          N: -.
#B: -...        O: ---
#C: -.-.        P: .--.
#D: -..         Q: --.-
#E: .           R: .-.
#F: ..-.        S: ...
#G: --.         T: -
#H: ....        U: ..-
#I: ..          V: ...-
#J: .---        W: .--
#K: -.-         X: -..-
#L: .-..        Y: -.-- 
#M: --          Z: --..

# Your program should output the correct Morse Code regardless of casing of the input characters. You should output spaces 
# in the input string as two spaces, and separation 
# between  Morse Code characters should be a single space.

# For example the message 'Go Pokes' would be equivalent to:

# --. ---  .--. --- -.- . ...

# Where there is a space between the "G" and "o" in Morse code and two spaces between the "Go" and "Pokes".

# Tips and tricks:

# Dictionaries will be your friend for this assignment
# if string_variable.isalpha():
# The Morse Code characters will only ever be `-` or `.`  or a space
# You can treat strings much like you would a list, meaning you can iterate through them and access characters based 
# on an index position
# Remember you can utilize string concatenation with `+=` to build new strings

# I will start off with the input so for the user to use in order to change the plaintext to Morse Code

input_string = input('Please Enter Your plaintext/Alphabetical Characters: ')

# I will create a dictionary for the plaintext alphabet translation to the Morse Code alphabet

morse_code_dictionary = {

        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'

}

# I will then initialize the Morse Code output making it be a blank canvas so that I can add onto it later

morse_code_output = ""

# I will then use a for statement so that each character is able to be processed and swapped to Morse Code

# Within the for statement I will make it so that every character entered is upper case (lower case does not work) so that the case sensitivity in the dictionary does not matter

for char in input_string.upper():
# I can use an if statmenet to check if the character entered is alphabetical or not and to continue with the statement if it is
    if char.isalpha():
# I can add a space the Morse Code so that the output will be correct
        morse_code_output += morse_code_dictionary[char] + " "
# I can make an elif statement so that it checks if there is a space provided, making the output be different when converting to Morse Code
    elif char == ' ':
# I can make an if statment to add a double space to the Morse Code if there is already Morse Code
        if morse_code_output:
# I can make it so there is an extra space if there is Morse Code already present
            morse_code_output += "  "

# I can strip the uneeded space(s) and print the correct result

morse_code_output = morse_code_output.strip()

print('Thank You. This is the Morse Code Tanslation:', morse_code_output)