def square_numbers(numbers):
    return list(map(lambda x: x**2, numbers))
numbers = list(map(int, input("Ingrese una lista de números separados por espacio para elevar al cuadrado con map y lambda: ").split()))
print(f"Cuadrados: {square_numbers(numbers)}\n")