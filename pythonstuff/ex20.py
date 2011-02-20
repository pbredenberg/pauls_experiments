# import the sys module
from sys import argv

# define variable script name and input file name
script, input_file = argv

# define the print_all argument as variable f
def print_all(f):
# print variable f and read it using the read command
    print f.read()

# define the rewind function as variable f
def rewind(f):
# take variable f and use it to seek to line 0
    f.seek(0)

# define the print a line argument as the variables line count and f
def print_a_line(line_count, f):
# print out the line count, and the f variable with the readline command
    print line_count, f.readline()

# define curren file as the the input file and open it with the open command
current_file = open(input_file)

# print the whole file
print "First let's print the whole file:\n"

print_all(current_file)

# rewind the file
print "now let's rewind, kind of like a tape."

# rewind command on current file variable
rewind(current_file)

# print out three line, line 1, add a line for the next and so on
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

            
