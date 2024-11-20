numero = int(input("introduce un numero: "))

while numero < 100 or numero > 400:
    print("El numero no esta entre 100 y 400")
    numero = int(input("introduce otro numero: "))

print(f"El numero esta entre 100 y 400")
