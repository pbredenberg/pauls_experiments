prompt = 'Tell me now:'

# about the script
print "Hi, welcome to the script!\n"
print "This script calculates how many classic movies\n"
print "were made in a given year, then tells you how\n"
print "many are worth watching."

# ask for a year
print "Now, for which year would you like to calculate?"
movie_year = raw_input(prompt)

# ask for number of movies made that year"
print "Now, use google to find out how many\n"
print "movie were made that year."
number_of_movies = raw_input(prompt)

# tells how many are worth watching
print "Ok, so for all the movies made in the year %s..." % movie_year
divider = number_of_movies / 100