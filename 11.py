for i in range(5):
    print("hello " + str(i))

for i in range(10):
    print("you are number " + str(i))

def mul_five(my_number):
    result = my_number * 5
    return result


def my_print(prefix, amount_of_times):
    for i in range(amount_of_times):
        print(prefix + str(i))

my_print(prefix="hello ", amount_of_times=5)
my_print(prefix="you are number ", amount_of_times=10)

