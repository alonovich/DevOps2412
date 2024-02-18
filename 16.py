import requests
try:
    requests.get("sdfgdfg..sdf")
except BaseException as e:
    print("something went wrong")
    print(e.args)

while True:
    try:
        a = int(input("enter number"))
        b = int(input("enter second"))
        result = a / b
        print(result)
        break
    except ValueError:
        print("enter correct number")
    except ZeroDivisionError:
        print("not divide by zero")
    except BaseException as e:
        print(e.args)


