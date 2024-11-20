num = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]

par = 0
impar = 0

for n in num:
    if n % 2 == 0:  
        par += n
    else:
        impar += n

print(f"La suma dels números parells és {par}.")
print(f"La suma dels números imparells és {impar}.")
