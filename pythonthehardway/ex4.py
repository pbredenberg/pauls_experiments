# define how many cars there are
cars = 100
# define the space in a car
space_in_a_car = 4.0
# define how many drivers are available
drivers = 30
# define how many passengers there are
passengers = 90
# define how many cars will not be used
cars_not_driven = cars - drivers
# show that the number of cars driven will be equal to drivers
cars_driven = drivers
# define the carpool capacity by multiplying the cars driven by the space available in the car
carpool_capacity = cars_driven * space_in_a_car
# define that the average passengers will be equal to the passengers divided by the cars driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
