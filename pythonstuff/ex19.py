# create the function "cheese_and_crackers", define arguments cheese count, and boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# print the cheese count in the function
    print "You have %d cheeses!" % cheese_count
# print the boxes of crackers
    print "You have %d boxes of crackers!" % boxes_of_crackers
# print this phrase
    print "Man that's enough for a party!"
# print this phrase, add a line break
    print "Get a blanket.\n"

# print the function
print "We can just give the function numbers directly:"
# define the amounts
cheese_and_crackers(20, 30)

# print this phrase, give the function the argument amounts directly
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# link the function to the arguments above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print the function, assigne math arguments within
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# print the function, add numbers to the arguments
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)    
