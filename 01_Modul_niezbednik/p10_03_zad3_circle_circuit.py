def circle_circuit(d, pi=3.14):
    return d * pi


print("------------------")
print(circle_circuit(6))
print(circle_circuit(9))
print("------------------")

d = float(input("Podaj wartość d: "))
print(f"Obwód okręgu o średnicy d={d} wynosi {circle_circuit(d)}")

