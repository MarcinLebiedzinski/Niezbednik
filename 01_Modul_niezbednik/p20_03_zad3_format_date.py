def format_date(day, month, year):
    month_name_pl = ('stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia')
    if month not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        return None
    elif ((day > 28) and (month == 2)) or ((day > 30) and (month in (2, 4, 6, 9, 11))) or (day < 1) or (day > 31):
        return None
    else:
        return f"{day} {month_name_pl[month-1]} {year}"

print(format_date(12, 1, 2017))

print(format_date(12, 13, 2017))
print(format_date(29, 2, 1999))

print(format_date(29, 3, 1999))

print(format_date(31, 2, 1999))
print(format_date(15, 14, 1999))
print(format_date(15, 'a', 1999))


# Wersja zadania ze słownikiem
def format_date(day, month, year):
    my_calendar = {
        1 : tuple(range(1, 31)),
        2 : tuple(range(1, 29)),
        3 : tuple(range(1, 32)),
        4 : tuple(range(1, 31)),
        5 : tuple(range(1, 32)),
        6 : tuple(range(1, 31)),
        7 : tuple(range(1, 32)),
        8 : tuple(range(1, 32)),
        9 : tuple(range(1, 31)),
        10 : tuple(range(1, 32)),
        11 : tuple(range(1, 31)),
        12 : tuple(range(1, 32))
    }

    month_name_pl = ('stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia')

    if month not in my_calendar or day not in my_calendar[month]:
        return None
    else:
        return f"{day} {month_name_pl[month-1]} {year}"

print(format_date(12,1,2017))

print(format_date(12, 13, 2017))
print(format_date(29, 2, 1999))

print(format_date(29, 3, 1999))

print(format_date(31, 2, 1999))
print(format_date(15, 14, 1999))
print(format_date(15, 'a', 1999))
