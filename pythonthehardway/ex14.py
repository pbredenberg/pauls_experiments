from sys import argv

# use a 'status' argument like 'awesome'
script, user_name, status = argv
prompt = '> '

print "Hi %s, I'm the %s script. I hear you're %s" % (user_name, script, status)
print "i'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
..and you're right, you are %r
""" % (likes, lives, computer, status)
