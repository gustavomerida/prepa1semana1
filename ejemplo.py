#Programa que le pida al usuario su nombre y su edad y devuelva un saludo y el año en que nació

"""
comentario de
varias lineas"""

año = 2025
nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))

nacimiento = 2025 - edad

print(f"Hola {nombre}, tienes {edad} años y naciste en el año {nacimiento}.")
