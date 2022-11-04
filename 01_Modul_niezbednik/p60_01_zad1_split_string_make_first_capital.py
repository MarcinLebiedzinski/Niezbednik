def shorten(text):
    short = ""
    my_list = text.split(" ")
    for word in my_list:
        short += word[0]
    return short.upper()


shortened = shorten("Don't repeat yourself")
print(shortened)
shortened = shorten("Read the fine manual")
print(shortened)
shortened = shorten("All terrain armoured transport")
print(shortened)
