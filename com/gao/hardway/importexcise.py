__author__ = 'wangchen'
#coding=utf-8


import moremoreexs

#调用别的模块的功能
sentence = "all good things come to those who wait"

words = moremoreexs.break_word(sentence)

print words

#排序功能
sorted_words = moremoreexs.sort_word(words)
print sorted_words

#获取元素
first_word = moremoreexs.print_first_word(words)
print first_word

last_word = moremoreexs.print_last_word(words)
print last_word

print words

last_sorted = moremoreexs.print_first_last_sorted(sentence)
print sentence
print last_sorted

