details = ["aviel", "buskila", 34, True]
details_dict = {"fname": "aviel",
                "lname": "buskila",
                "age": 34,
                "is_marr": True}
my_class = [
    {"fname": "or", "lname": "shemesh"},
    {"fname": "maksim", "lname": "hamaksim"},
]
for student in my_class:
    print(student["fname"])
print(details_dict.keys())
print(details_dict.values())