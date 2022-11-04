
class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        if not Book.check_isbn(self.isbn):
            raise ValueError


    @staticmethod
    def check_isbn(isbn):
        isbn_converted = isbn.replace("-", "")
        if not len(isbn_converted) in (10, 13) and not isbn_converted[:3] in ('978', '979'):
            return False
        elif len(isbn_converted) == 13 and isbn_converted.isdigit():
            check_digit = int(isbn_converted[-1])
            sum = 0
            position_in_number = 1
            for digit in isbn_converted[:12]:
                if position_in_number % 2 != 0:
                    sum += int(digit) * 1
                    position_in_number += 1
                else:
                    sum += int(digit) * 3
                    position_in_number += 1
            if (10 - (sum % 10) == check_digit) or (sum % 10 == 0 and check_digit == 0):
                return True
            else:
                return False
        elif len(isbn_converted) == 10 and isbn_converted[:9].isdigit():
            sum = 0
            position_in_number = 1
            for digit in isbn_converted[:9]:
                sum += int(digit) * position_in_number
                position_in_number += 1
            check_digit = isbn_converted[-1]
            if check_digit.isdigit() and sum % 11 == int(check_digit):
                return True
            elif check_digit == 'X' and sum % 11 == 10:
                return True
            else:
                return False


print(Book.check_isbn('139316093X'))
