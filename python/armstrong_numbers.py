# How can you make this more scalable and reusable later?
from posixpath import split


def find_armstrong_numbers(numbers):
    arm_nums=[]
    for x in numbers:
        total=0
        power= len(str(x))
        digits= list(str(x))
        for n in digits:
            total+= int(n)**power
        if total == x:
            arm_nums.append(x)
    return arm_nums

