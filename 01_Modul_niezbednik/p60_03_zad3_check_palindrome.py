def check_palindrome(my_text):
    text_without_spaces = my_text.replace(" ", "")
    list_of_letter = [letter.capitalize() for letter in text_without_spaces]
    if list_of_letter == list(reversed(list_of_letter)):
        return True
    else:
        return False


print(check_palindrome('Marcin'))
print(check_palindrome('oko'))
print(check_palindrome('potop'))
print(check_palindrome('kajak'))
print(check_palindrome('Anna'))
print(check_palindrome('Kobyła ma mały bok'))

