# Ciąg Fibonacciego - metoda standardowa
def fib(n):
    lista = [0, 1]
    for i in range(2, n+1):
            lista.append(lista[i-1] + lista[i-2])
    print("Ciąg będzie posiadał wartości: ", lista)
    return lista[n]


print(fib(15)) # liczymy od 0. Jeśli chcemy liczyć od 1 to zmieniamy - in range(n) oraz - return llista[n-1]


# Ciąg Fibonacciego - metoda z wykorzystaniem rekurencji
def fib_rek(n):
    if n < 1:
        return 0
    elif n < 2:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2)


print(fib_rek(15))
