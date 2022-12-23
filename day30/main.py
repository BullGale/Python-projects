# try:
#     file = open("a_file.txt")
# except FileNotFoundError as error:
#     file = open("a_file.txt", "w")
#     file.write("something{error}")
# else:
#     print("You generated wrong exception")
# finally:
#     raise TypeError("Kya likh raha tu be")

height = float(input("Height:"))
weight = float(input("Weight:"))

if height > 3:
    raise ValueError("YOu entered wrong height. should not be more than 3 meters")

bmi = weight / height**2
print(bmi)