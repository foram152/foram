# ---> part 1 Use of Built-in Function in python

import random

# # import the random module to generate random number later.

# print("<== Build-in Function on list ==>")

numbers = [4 , 3 , 7 , 9 , 5]

# print("List : " , numbers)

# #len()
# # Alist named numbers is defined with 5 integers.
# #len() return the number of items in the list

print("Length of List : " , len(numbers))

# # max() and min() are used to find to find the largest and smallest numbers respectively.

# print("Max Number : " , max(numbers))
# print("Min Number : " , min(numbers))

# #sum() adds all values in the list

# print("Sum of List : " , sum(numbers))

# ---> part 2 Negative Float Number Operation

# print("<== Negative Float Number Operation ==>")

# num = float(input("Enter a Negative float Number : "))

# # abs() return the positive version from the user

# print("Positive version from the user : " , abs(num))

# # pow() raises the positive value of the power

# print("Power of value : " , pow(num , 3))

# # round() round of the number to 2 digit after the decimal point

# print("Round of value : " , round(num))

# ---> part 3 random list and its values / Analysis

# print("<=== random list and its values / Analysis ===>")

# random_num = random.sample(range(1 , 100) , 5)

# print(random_num)

# #using max() , and min() , sum() in random value

# print("Random list: " , random_num)

# print("Random number max count: " , max(random_num))
# print("Random number min count: " , min(random_num))
# print("Random number sum count: " , sum(random_num))

# ---> part 4 sort and reverse a list

print("<=== Sort and Reverse a List ===>")

user_list = list(map(int , input("Enter number seperated by space : ").split()))

print(user_list)

# sorted() the original user inputs

# reverse() return a reverse iterator , and list convert in back to a list

print("Sorted List Ascending" , sorted(user_list))

# print("Sorted List Descending" , sorted(user_list , reverse=True))

print("Reverse value of List : " , list(reversed(user_list)) )