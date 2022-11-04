import random


def random_average(n):
    my_list = [random.randint(1, 101) for _ in range(n)]
    print("Wylosowano 10 liczb: ", my_list)
    return f"Średnia artytmetyczna wynosi {sum(my_list)/n}"


print(random_average(10))
