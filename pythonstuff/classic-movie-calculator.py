prompt = 'Tell me now: '

# about the script
print "Hi, welcome to the script!\n"
print "This script asks you how many classic movies"
print "were made in a given year, then tells you how"
print "many are worth watching."

# ask for a year
print "Now, for which year would you like to calculate?"
movie_year = raw_input(prompt)

# ask for number of movies made that year"
print "Now, use google to find out how many"
print "movies were made that year."
number_of_movies = raw_input(prompt)

# tells how many are worth watching
print "Ok, so for all the movies made in the year %s..." % movie_year

# show the results
print "25 percent are really worth watching."