sum_lambda = lambda a, b: a + b
power_lambda = lambda base, exp: base ** exp
a, b = map(int, input("Ingrese dos números separados por espacio para sumar con lambda: ").split())
print(f"Suma: {sum_lambda(a, b)}\n")
    
base, exp = map(int, input("Ingrese la base y el exponente separados por espacio para calcular potencia con lambda: ").split())
print(f"Resultado: {power_lambda(base, exp)}\n")