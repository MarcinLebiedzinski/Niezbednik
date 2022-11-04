def find_boundaries(my_list):
    if not my_list:
        return None
    else:
        only_number_list = []
        for element in my_list:
            if not isinstance(element, int) and not isinstance(element, float):
                pass
            else:
                only_number_list.append(element)
    return (min(only_number_list), max(only_number_list))


print(find_boundaries([1, 5, 2, 3.5, -1]))
print(find_boundaries([0, 2, "a kuku!", 10]))
print(find_boundaries([]))


# alternatywna funkcja bez użycia funkcji max i min
def find_boundaries2(my_list):
    if not my_list:
        return None
    else:
        max_number = my_list[0]
        min_number = my_list[0]
        for element in my_list:
            if not isinstance(element, int) and not isinstance(element, float):
                pass
            else:
                if element < min_number:
                    min_number = element
                if element > max_number:
                    max_number = element
    return (min_number, max_number)


print(find_boundaries2([1, 5, 2, 3.5, -1]))
print(find_boundaries2([0, 2, "a kuku!", 10]))
print(find_boundaries2([]))