# > Day 24 -------------------------------------------------------------------------------------------------------------
# > 1. Learning about How to Open, Read and Write Files ----------------------------------------------------------------

# >> 1.1. Not Recommend Practice ---------------------------------------------------------------------------------------

# Open File and Set it in a variable.
# file = open('my_file.txt')

# Read File and set it in a variable.
# contents = file.read()
# print(contents)

# After open and use it, it's necessary to close File.
# file.close()

# >> 1.2. Best Practice ------------------------------------------------------------------------------------------------

# Use like this, because you don't need to close the file afterward.
# Open File and save it in a variable.

# with open('my_file.txt') as file:
#     # Read File.
#     contents = file.read()
#     print(contents)

# >> 1.3. Writing in a File --------------------------------------------------------------------------------------------

# Open File and set it a Writing Mode = 'w', in which delete all past content and write the new message.
# ATTENTION: if it doesn't exist the file, writing mode will create a file for you.

# with open('my_file.txt', mode='w') as file:
#     file.write('Hello World!')

# >> 1.4. Adding new line of text in a File ----------------------------------------------------------------------------

# ATTENTION: Every time your run the code, it will write it again.

# with open('my_file.txt', 'a') as file:
#     file.write('\nHello World!')

# ----------------------------------------------------------------------------------------------------------------------