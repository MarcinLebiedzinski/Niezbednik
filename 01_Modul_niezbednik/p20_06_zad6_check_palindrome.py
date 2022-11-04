def check_palindrome(word):
    lista = [letter.capitalize() for letter in word]
    reverse_list = list(reversed(lista))
    return f"Słowo '{word}' jest palindromem: {lista == reverse_list}"


print(check_palindrome('Marcin'))
print(check_palindrome('oko'))
print(check_palindrome('potop'))
print(check_palindrome('kajak'))
print(check_palindrome('Anna'))
