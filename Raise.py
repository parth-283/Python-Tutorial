a = input("What is your name")

if a.isnumeric():
    raise Exception("Numbers are not allowed")

print(f"Hello {a}")