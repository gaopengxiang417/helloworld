__author__ = 'wangchen'
#coding=utf-8

print "Hello world"
print "hello again"
print "i like typing this"
print "this is fun"
print "yes,printing"
print "i would rather than you 'not'"
print 'i said "not " to touch that'

print "add a line"
# print "this line is comment"

#a comment , so you can read your program later
#anything after the # is ignored by python

print "I could have code like this." # and comment after this is ignored

# you can use comment to disable  or comment a piece of code
# print "this will not be print"

print "This will run"

# i will count the eggs

print "Hens:", 25 + 30 / 6
print "Roosters:", 100 - 25 * 3 % 4

# i will count the chickens

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print "is that true 3 + 2 < 5 - 7", 3 + 2 < 5 - 7
print "what's that 3 + 2:", 3 + 2
print "what's that 5 - 7:", 5 - 7
print "that's why it's false"

print "how about some more"
print "is that greator: ", 5 > 12
print "is greator or equal:", 5 >= -4
print "is less or equal:", 5 <= -2

print 30.0 / 13


cars = 100
spaces_in_cars = 4.0
drivers = 30
passengers = 90
cars_not_driver = cars - drivers
cars_driven = drivers
carpool_capcity = cars_driven * spaces_in_cars
average_passengars_per_car = passengers / cars_driven

print "there are", cars, "can driven"
print "there are only", drivers, "drivers available"
print "there will be", cars_not_driver, "empty cars"
print "we can transport", carpool_capcity, "people today"
print "we have", passengers,"to carpool today"
print "we need to put about", average_passengars_per_car, "in each car"