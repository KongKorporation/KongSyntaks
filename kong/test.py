def add(a:int, b:int):
     return a + b


def coucou():
    print("coucou")
    i: int = 0

    print(i)
    for i in range(10):
        add(i, i)