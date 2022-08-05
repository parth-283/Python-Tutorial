def funargs(normal, *lst, **kw):
    print(normal)
    for item in lst:
        print(item)
    for key, value in kw.items():
        print(f"{key} : {value}")


lst = ['Parth', 'hari', 'kevin', 'ravi']
kw = {"parth": 1, "krunal": 2}
normal = "This is a normal"
funargs(normal, *lst, **kw)
