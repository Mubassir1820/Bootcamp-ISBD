# A teacher maintains a list of students in a class. The list is ["Alice", "Bob", "Charlie",
# "David", "Eve"]. Write a Python program to print the names of students whose names start
# with "A" or "D".

name_list = ["Alice", "Bob", "Charlie", "David", "Eve"]

for i in name_list:
    if i[0] == 'A' or i[0] == 'D':
        print(i)