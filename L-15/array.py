# Q-1 Find the length of a 1D arry without len()

size = int (input("Enter array size : "))

arr = []

print("\nEnter array element : \n")

#  print by the loop

for i in range(size):
    value = int(input(f"a[{i}] = "))
    arr.append(value)

#  count length manually

length = 0
for l in arr:
    length += 1
print(length)

# # Q-2 Find the average of a 1 D array

size = int(input("\nEnter array size : "))

arr = []

for i in range(size):
    value = int(input(f"a[{i}] = "))
    arr.append(value)

# calulate the average 

total = 0 
length = 0

for value in arr:
    total += value
    length += 1

average = total/length

print("Average of an array : " , average)