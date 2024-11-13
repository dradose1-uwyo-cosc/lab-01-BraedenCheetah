# Braeden Kirby
# UWYO COSC 1010
# 11/12/2024
# HW 04 
# Lab Section 13
# Sources, people worked with, help given to: 

# You will be reading from and writing to a file.
# You will read from prompt.txt Download prompt.txt.
# You will write to a file called "out.txt".

# Look at prompt.txt to understand its structure.

# It contains key-value pairs on each line of the file.
# The keys are 'w' and '*'.
# 'w' stands for white space, and '*' is an asterisk (*).
# The numeric value shows how many of each of those characters there are for each line in your output file.
# Each line in prompt.txt corresponds to one line in out.txt.

# For example, the line:
# "w:101    *:020    w:026    *:004    w:017    *:030"
# You will output a line with 101 white spaces, 20 asterisks, 26 white spaces, 4 asterisks, 17 white spaces, and 30 asterisks.
# All of that will be on ONE line of your output file.

# Each of the key-value pairs is separated by a tab '\t' character.
# The key values are separated by a ':' character.

# You can use the .split() function on strings to create a list. For example, pairs = line.split("\t") will give you a list of all the pairs in a line.

# You can multiply strings by an integer, x, to create a string repeated x times. So, string_val = "*" * 10 would create a string with 10 asterisks: "**********".

# You will be outputting a VERY recognizable ASCII art with this. If you are looking at the output file and you aren't sure what it is, you are likely doing it incorrectly. It can help if you zoom out on your output file.

# I can start by using the instructions to split the code and use pairs

# Also, setting the output to be a list

def processing_code(line):

    pairs = line.strip().split("\t")

    output = []

# I will make it so the values within the prompt file are 'keys' and 'values' and I can split the pair into the key and value

    for pair in pairs:

        key, value = pair.split(":")

        count = int(value)

        if key == "w":

            output.append(" " * count)

        elif key == "*":

            output.append("*" * count)

    return "".join(output)

# I can use the main codespace to run the program and write out the output into the 'outfile' so that it comes out as intended

def main():

    with open("prompt.txt", "r") as infile, open("out.txt", "w") as outfile:

        for line in infile:

            line = line.strip()

            if line:

                processed_line = processing_code(line)

                outfile.write(processed_line + "\n")

if __name__ == "__main__":

    main() 