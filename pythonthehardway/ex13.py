from sys import argv

script, first, second, third = argv

what_you_want = raw_input("What do you want with me, human?")

print "Very well, I shall give you %r, in addition, you shall have:" % what_you_want
# print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
