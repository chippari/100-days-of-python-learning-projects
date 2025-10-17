# ----------------------------------------------------------------------------------------------------------------------
# > Day 24 - Mail Project ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-17
# ----------------------------------------------------------------------------------------------------------------------

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# ----------------------------------------------------------------------------------------------------------------------

# Get Letter Model from starting_latter.
with open(file="input/letters/starting_letter.txt", mode="r") as starting_letter:
    letter_model = starting_letter.read()

# Get Invited List from invited_names.
with open(file="input/names/invited_names.txt", mode="r") as invited_names:
    unformatted_list_invited = invited_names.readlines()
    invited_list = []

    for name in unformatted_list_invited:
        # 1. Formatted Name by removing space = "\n".
        formatted_name = name.strip("\n")
        # 2. Append formatted name in invited list.
        invited_list.append(formatted_name)

# Create Mails using letter model and invited list.
for name in invited_list:
    file_name = f"mail_to_{name}.txt"
    letter = letter_model.replace("[name]", name)
    with open(f"output/ready-to-send/{file_name}", mode="w") as mail:
        mail.write(letter)


# ----------------------------------------------------------------------------------------------------------------------