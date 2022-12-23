with open("file1.txt") as file1:
    f1 = file1.readlines()

with open("file2.txt") as file2:
    f2 = file2.readlines()

result = [num for num in f1 if num in f2]
# Write your code above 👆

print(result)


