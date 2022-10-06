# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


############# START OF THE PROGRAM ###############

list_names = []
# --- opening the names file --- #
with open("./input/Names/invited_names.txt") as names:
    list_names = names.readlines()

    res = []
    with open("./input/Letters/starting_letter.txt") as input:
        string = input.read()
        for name in list_names:

            ## -- Stripping out the extra charachters and replacing with names-- #

            stripped_name = name.strip()
            string_update = string.replace("[name]", stripped_name)

            ## -- writing the names to the file -- #
            with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", 'w') as output:
                output.write(string_update)

