# list 
# tuple
# set
# dictionary

# list
# mutable
# you can modify element after creation(add , change , remove)

# example
my_list = [1 , 2 , 3]

my_list [2] = 17

my_list.append(12)

del my_list[1]

# print(my_list)

# tuple
#immutable
# you cannot modify element after creation.

# example

My_tuple = (1 , 2 , 3)

# My_tuple (2) =12

# del My_tuple[2] 

# print(My_tuple)

# Set
# mutable

my_set = {1 , 2 , 3}

# my_set (2) = 14

my_set.add(40)
my_set.add(40)

# print(my_set)

# dictionary
# mutable

my_dics = {"1":"alice" , "2":"jasmin"}

my_dics["1"] = "india"

my_dics["3"] = "prerna"

del my_dics["1"]

# print(my_dics)

name1 = "alice"
name2 = "jasmin"
name3 = "geet"

# print(name1)
# print(name2)
# print(name3)

name_list = ["alice" , "jasmin" , "geet"]

# print(name_list[0])
# print(name_list[1])
# print(name_list[2])

# for user in name_list:
 #   print(user)

# type casting constructur

a = [1 , 2 , 3]

b = tuple(a)

c = set(b)

# d = dict(c)

print(c)