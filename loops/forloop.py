# syntax
"""
for variable in sequence/iterable:
    # code to execute

"""
# fruits = ["apple", "banana", "cherry"]
# print(len(fruits))
#
#
# def convert_Caps(fruit):
# #     function / logic to make each print out caps
#      print("in function ", fruit)
#      return fruit.upper()
#
#
# for fruit in fruits:
#     print(fruit)
#     print(convert_Caps(fruit))
#
#
# ## range method  range(stop) mandatory / range(start,stop,step)
# for i in range(11,1,-2):
#     print(i)

for i in range(10):
    if i == 5:
        break #exists the loop
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)

my_dictionary = {
    'name' : "Joseph",
    "occupation" : "software dev"
}
for key in my_dictionary:
    print(my_dictionary[key])

for key,value in my_dictionary.items():
    print(f"{key} : {value}")
