salari = 20000

if salari < 15000:
    iva_percentatge = 0
elif salari < 30000:
    iva_percentatge = 10
elif salari < 60000:
    iva_percentatge = 21

iva = salari * iva_percentatge / 100

print(f"Amb un salari de {salari}, s'aplica un {iva_percentatge}% d'IVA.")
print(f"L'import de l'IVA és: {iva}")
