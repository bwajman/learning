# 1. setup variables

a = 5
b = 10
a, b = b, a
print(a, b)

# 2. list comprehension

squares = []
for i in range(10):
    if i % 2 == 0:
        squares.append(i * i)
print(squares)

squares = [i * i for i in range(10) if i % 2 == 0]
print(squares)

# 3. if else

if 3 > 2:
    var = 42
else:
    var = 99
print(var)

var = 42 if 3 > 2 else 99
print(var)

# 4. print without new lines

data = [0, 1, 2, 3, 4, 5]

for i in data:
    print(i, end=" ")

print()  # new line

print(*data)

# 5. days left in year

import datetime

print((datetime.date(2023, 12, 31) - datetime.date.today()).days)

# 6. reversing a list

a = [1, 2, 3, 4, 5, 6]

a = a[::-1]

print(a)

# 7. multiple variable assignments

name, age = 'John', 31

print(name, age)

# 8. space separated numbers to integer list

user_input = "1 2 3 4 5 6"

my_list = list(map(int, user_input.split()))

print(my_list)

# 9. reading file into list

names = [line.strip() for line in open("names.txt", "r")]

print(names)

# 10. python server

# in terminal -> python -m http.server
