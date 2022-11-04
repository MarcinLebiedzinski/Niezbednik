def censor(text):
    list_of_text_words = text.split(" ")
    print(list_of_text_words)
    forbidden_words = ['Java', 'C#', 'Ruby', 'PHP']
    s = ''''''
    for word in list_of_text_words:
        if word in forbidden_words:
            print("Znaleziono niedozwolone słowo: ", word)
            s += '****'
        else:
            s += word
        s += " "
    return s

c = "Java is the best, but PHP is the bestest!"

print(censor(c))
