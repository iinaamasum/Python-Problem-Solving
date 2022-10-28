x = {"a": 1, "b": 2, "c": 3, "d": 4}
d = {"!": 1, "@": 2, "#": 3, "$": 4, "%": 5, "^": 6}


def create_list():
    l = list()
    for key, val in x.items():
        l.append(key)
        l.append(val)
    print(l)


create_list()
