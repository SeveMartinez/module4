dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}

"""
for elem in dictionary:
    print(elem,"-", dictionary[elem])
"""

"""
for elem in dictionary.keys():
    print(elem)
"""

"""
for elem in dictionary.values():
    print(elem)
"""

dictionary["birds"] = "Larry"
dictionary.update({"birds":"God"})
dictionary.update({"beetles":"Peter"})
del dictionary["cat"]
dictionary.pop("dog")


for key,value in dictionary.items():
    print(key,"-",value)


"""
print(dictionary["cat"])
print(phone_numbers["boss"])
"""