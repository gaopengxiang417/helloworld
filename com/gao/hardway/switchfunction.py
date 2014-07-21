__author__ = 'wangchen'

#coding=utf-8

from sys import exit


#

def gold_room():
    print "this room is full of gold, how much do you take"

    value = raw_input("> ")

    if "0" in value or "i" in value:
        how_much = int(value)
    else:
        dead("man ,learn to type a number")

    if how_much < 50:
        print "nice ,you are not greedy, you win"
        exit(0)

    else:
        dead("you greedy bastard")


def bear_room():
    print "there is a bear here"
    print "the bear has a bunch of honey"
    print "the fat bear is in front of another door"
    print "how are you going to move the bear"
    bear_moved = False

    while True:

        value = raw_input(">")

        if value == "take honey":
            dead("the bear looks at you then slaps your face")
        elif value == "taunt bear" and not bear_moved:
            bear_moved = True
        elif value == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews your legs")
        elif value == "open door" and bear_moved:
            gold_room()
        else:
            print "i got no idea about what means"


def chack_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    value = raw_input(">")

    if "flee" in value:
        start()
    elif "head" in value:
        dead("well what i as tasty")
    else:
        chack_room()


def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    value = raw_input(">")

    if value == "left":
        bear_room()
    elif value == "right":
        chack_room()
    else:
        dead("you are dead")


def dead(str):
    print str, "good luck"
    exit(0)


start()
