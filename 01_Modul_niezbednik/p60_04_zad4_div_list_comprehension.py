def div(start_digit, stop_digit):
    my_list = [digit for digit in range(start_digit, stop_digit + 1) if (digit % 2 == 0 and digit % 3 != 0)]
    return my_list


result = div(0, 20)
print(result)
