for moshe in range(5):
    print("hello " + str(moshe))
else:
    print("finished")
class_mates = ["maksim", "yoni", "gilad", "oren"]
for cur_name in class_mates:
    print(cur_name)

for i in range(len(class_mates)):
    print(class_mates[i])

your_name = input("enter your name: ")
while your_name != "aviel":
    print("you are not aviel")
    if your_name == "haim":
        print("oh my god")
        break
    your_name = input("enter your name:")
else:
    print("your name is aviel")
