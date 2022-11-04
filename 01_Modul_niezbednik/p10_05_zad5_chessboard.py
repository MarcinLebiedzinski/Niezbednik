def chessboard(n=8):
    c=''''''
    for row in range(1, n+1):
        if row % 2 !=0:
            for column in range (1, n+1):
                if column % 2 !=0:
                    c += "#"
                else:
                    c += " "
            c += "\n"
        else:
            for column in range (1, n+1):
                if column % 2 !=0:
                    c += " "
                else:
                    c += "#"
            c += "\n"
    return c


Chess = chessboard(17)
print(Chess)

# Prostsza wersja z parzystą ilością kolumn
# def chessboard(n=8):
#     output = ""
#     for i in range(n):
#         if (i + 1) % 2 != 0:
#             output += '# ' * int(n / 2) + '\n'
#         else:
#             output = output + ' #' * int(n / 2) + '\n'
#     return output
#
# print(chessboard(5))
