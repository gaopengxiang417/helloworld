__author__ = 'wangchen'
#coding=utf-8

ten_thing = "apples oranges crows telephone light sugar"

print "wait there's not 10 things in that list,let's fix that"

stuff = ten_thing.split(" ")
more_stuff = ["day", "night", "friebee", "corn", "banana", "girl", "boy"]

while len(stuff) != 10:
    next = more_stuff.pop()
    print "adding ", next
    stuff.append(next)
    print "there is %d items there" % len(stuff)


print "there we go:" , stuff

print "let's do something with stuff"

print stuff[1]

print stuff[-1]

print stuff.pop()

print " ".join(stuff)

print "#".join(stuff[3:5])

