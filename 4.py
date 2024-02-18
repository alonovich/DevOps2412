"""
a = 5
b = 14
my_name = "alon"
if a > 10:
    print("hello")
elif my_name == "alon":
    print("found your name")
elif b > 5:
    print("b is good")
else:
    print("bla")

print(a == 50)
should_work = a == 50 and b < 100


my_list = []
if my_list:
    print("you have items")
else:
    print("no items")
"""

my_other_list = ["or", "tohar", "adam"]
my_other_name = "or"
if my_other_name in my_other_list:
    print("i found you")

tt = [1, 2, 3]
rr = [1, 2, 3]
print(type(tt) is list)
