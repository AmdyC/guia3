def count_words(text):
    return len(text.split())
text = input("Ingrese un texto para contar palabras: ")
print(f"Número de palabras: {count_words(text)}")