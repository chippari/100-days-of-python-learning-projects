# > Day 24 -------------------------------------------------------------------------------------------------------------
# > 1. Learning about How to Open, Read and Write Files ----------------------------------------------------------------

# Open the file and Set it in a variable.
file = open('my_file.txt')

# Read the file and set it in a variable.
contents = file.read()
print(contents)

# After open and use it, it's necessary to close the file.
file.close()

# ----------------------------------------------------------------------------------------------------------------------