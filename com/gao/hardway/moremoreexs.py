__author__ = 'wangchen'
#coding=utf-8


#自定义函数，用来后面的导入使用
def break_word(stuff):
    """this function will break up word for us"""

    words = stuff.split(" ")
    return words


def sort_word(words):
    """sorts the words"""

    return sorted(words)


def print_first_word(words):
    """printing the first word after pop it"""

    word = words.pop(0)
    print word


def print_last_word(words):
    """printing the last word after pop it"""

    word = words.pop(-1)
    print word


def sort_sentence(sentence):
    """take in a full sentence,return the sorted words"""

    words = break_word(sentence)
    return sort_word(words)


def print_first_last(senence):
    """print the first and last word of the sentence"""

    words = break_word(senence)
    print_first_word(words)
    print_last_word(words)


def print_first_last_sorted(sentence):
    """sorts the words and print the first and last word"""

    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)




