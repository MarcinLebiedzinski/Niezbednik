
# def generator(number):
#     list_of_dividers = []
#     for i in range(1, number+1):
#         if number % i == 0:
#             list_of_dividers.append(i)
#         else:
#             continue
#     return list_of_dividers
#
# print(generator(6))


def dividers(number):
    for i in range(1, number+1):
        if number % i == 0:
            yield i
        else:
            continue


if __name__ == '__main__':
    print(list(dividers(6)))

