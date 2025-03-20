lista=[ {"Nombre":"Andy", "Edad":17 },
        {"Nombre":"Castillo", "Edad":16}]
print(lista[0]["Nombre"])
print(lista[1]["Edad"])
print(lista[0])
for x in lista:
    print(lista.index(x))
    for key in x:
        print(key,x[key])