#import the sys module and unpack the argv variable
from sys import argv

#specify the arguments to run the file
script, filename = argv

#specify the txt file to be opened by the script
txt = open(filename)

# print this phrase and the file name variable
print "Here's your file %r:" % filename
# print out what's in the txt file
print txt.read()
txt.close()

# prompt the user to type in the name of the file
print "I'll also ask you to type it again:"
# specify the file_again variable to be user input
file_again = raw_input("> ")

# open the re-specified file
txt_again = open(file_again)

# print the contents of the re-specified file
print txt_again.read()
txt_again.close()

