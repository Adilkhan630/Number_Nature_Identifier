import random

minNum = int(input("Enter your min value: "))
maxNum = int(input("Enter your max value: "))

num = random.randint(minNum, maxNum);

if num > 0:
    print("{} is Positive number".format(num))
elif num == 0:
    print("Zero")
else:
    print("Negative number")

if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))

if (num % num == 1) and (num % 1 == 1):
    print("{0} is Prime".format(num))
else:
    print("{0} is composite".format(num))