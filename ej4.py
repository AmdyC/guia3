def is_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]
text = input("Ingrese una palabra o frase para verificar si es palíndromo: ")
print("Es un palíndromo" if is_palindrome(text) else "No es un palíndromo", "\n")