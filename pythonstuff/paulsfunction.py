def this_cool_function(comics_i_own, amount_to_buy):
    print "This is how many comics I own: %d" % comics_i_own
    print "I know you want more comics.\n"
    print "How many comics do you want to buy?"
    print "You should by %d more comics." % amount_to_buy

# 1
this_cool_function(30, 25)    

# 2
print "\n"    
print "Why not buy even more comics?"
this_cool_function(30, 45)

# 3
print "\nCome on dude you can do better than that...\n"
this_cool_function(30, 150)    

# 4
print "\nFor real? Try again\n"
this_cool_function(30, 250)  

# 5
print "\nOk let's up the anti here...\n"
comics_i_own = 30
amount_to_buy = 1000
this_cool_function(comics_i_own, amount_to_buy)

# 6
print "\nOk let's up the anti here...\n"
comics_i_own = 30
amount_to_buy = 1000
this_cool_function(comics_i_own, amount_to_buy + 2000)

# 7
print "\nMORE! MORE! MORE!\n"
comics_i_own = 30
amount_to_buy = 1000
this_cool_function(comics_i_own, amount_to_buy * 2000)
