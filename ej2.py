import random
name=input("Your name: ")
age= int(input("Your age: "))
def prox(a):
    return random.randint(a - 2, a + 2)
def sup(n):
    print(f"Yooo bro what's up {n}\n You're about {prox(age)}. Yeah?")
sup(name)
