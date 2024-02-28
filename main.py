from colour import *

num1, num2 = input("1-sonni kiriting: "), input("2-sonni kiriting: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    kopaytma = num1 * num2
    print(green(kopaytma))
except ValueError:
    str_yigindi = str(num1) + str(num2)
    print(green(str_yigindi))
