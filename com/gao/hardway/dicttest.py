__author__ = 'wangchen'
#coding=utf-8

#字典的一些使用

stuff = {"name": "zed", "age": 44,"height": 3 + 4}

print stuff["name"]
print stuff["age"]
print stuff["height"]

stuff["city"] = "san francisco"

print stuff["city"]

stuff[1] = "wow"
stuff[2] = "naset"

print stuff[1]
print stuff[2]

print stuff

del stuff[1]
del stuff[2]
del stuff["city"]
# del stuff["sdsd"] 不能删除不存在的元素

print stuff


cities = {"CA": "san francisco", "MI": "detroit", "FL": "jacksonville"}

cities["NY"] = "new york"
cities["OR"] = "portland"

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "not found"

cities["_find"] = find_city

while True:
    print "state: enter or quit"
    state = raw_input(">")
    if not state:
        break

    find_ = cities["_find"](cities, state)
    print find_

