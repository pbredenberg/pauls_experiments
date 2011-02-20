# define x as the variable for the number of people
x = "there are %d types of people." % 10
# define the binary variable
binary = "binary"
# define the do_not variable as don't
do_not = "don't"
# define y as this phrase, printing the variable binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# print variable x
print x
# print variable y
print y

# print the variable x no matter what
print "I said: %r." % x
# print variable y as a string
print "I also said: '%s'." % y

# define hilarious as the phrase 'false'
hilarious = False
# define joke evaluation as this string, print the string attached to variable x
joke_evaluation = "Isn't that joke so funny?! %r"

# print the variables joke_evaluation and hilarious
print joke_evaluation % hilarious

# define variable w as this string
w = "This is the left side of..."
# define variable e as this string
e = "a string with a right side."

print w + e
