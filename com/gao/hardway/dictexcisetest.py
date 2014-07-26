__author__ = 'wangchen'
#coding=utf-8

from sys import exit
from random import randint

#主要是练习和使用dict的功能

def death():

    quips = ["you died. you knida suck at this.", "nice job , you die ... jackass",
             "such a luser", "i have a small puppy that's better at this."]

    print quips[randint(0, len(quips) - 1)]

    exit(1)

def central_corridor():

    print "the gothens of planet percal #25 hive invade your ship and destroyed"
    print "your entire crew. you are the last surviving member and you last"
    print "put it in the bridge, and blow the ship up after getting int an escape pod"
    print "armory and about to pull a weapon to blast you."

    action = raw_input(">")

    if action == "shoot!":
        print "quick on the draw you rank out your blaster and fire at the gothon"
        print "you are dead. the he eat you"
        return "death"
    elif action == "dodge!":
        print "like a world class boxer you dodge. weave ,slip, and slide right"
        print "your head and eats you"
        return "death"
    elif action == "tell a joke":
        print "putting him down, then jump through the weapon army door"
        print "laser_weapon_armony"
    else:
        print "does not computer"
        return "central_corridor"

def laser_weapon_armory():
    print "You do a dive roll into the Weapon Armory, crouch and scan the room"

    code = "%d%d%d" % (randint(1,9), randint(1, 9), randint(1, 9))

    guess = raw_input(">")
    guesses = 0


    while guess != code and guesses < 10:
        print "bzzzzedddd"
        guesses += 1
        guess = raw_input(">")

    if guess == code:
        print "The container clicks open and the seal breaks, letting gas out."
        return 'the_bridge'
    else:
        print "The lock buzzes one last time and then you hear a sickening"
        return "death"
