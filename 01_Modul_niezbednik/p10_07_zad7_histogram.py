def histogram(lista):
    s = ""

    for element in lista:
        if isinstance(element, int) or isinstance(element, float):
            for column in range(1, int(element) + 1):
                s += '#'
            s += '\n'
        else:
            return None
    return s


h = (histogram([2, 6, 3, 1]))
print(h)

h = (histogram([9, 12, 3.5, 1.5]))
print(h)

h = (histogram([2, 6, 3, 'error!']))
print(h)
