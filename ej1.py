lista=[ {"ID":1,"Value":"nothing","Nombre":"Andy", "Edad":17 },
        {"ID":2,"Value":"something","Nombre":"Nicolas", "Edad":16}]
print(lista[0]["Nombre"])
print(lista[1]["Edad"])
for x in range(len(lista)):
    print(lista[x]["ID"])
    print(lista[x]["Value"])