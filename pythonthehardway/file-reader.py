from sys import argv

script, filename = argv

text = open(filename)

print "Opening the file %r dude..." % filename
print text.read()
text.close()
