from cotxe import cotxe
from colibri import colibri

cotxe1 = cotxe("subaru", "BRZ", "2016", "3", "negro")
cotxe2 = cotxe("ferrari", "f40", "1986", "3", "rojo")
cotxe3 = cotxe("porsche", "992 gt3", "2021", "3", "blanco")

colibri1 = colibri("Colibrí Rubí", "Aves", "2 años", "8 cm", "verde")
colibri2 = colibri("Colibrí Ventrirrojo", "Aves", "1 año", "7.5 cm", "rojo")
colibri3 = colibri("Colibrí de Pico Largo", "Aves", "3 años", "9 cm", "azul")

print(cotxe1.getmarca())
print(cotxe2.getmodel())
print(cotxe3.getcolor())

print(colibri1.getnom())
print(colibri3.getlongitud())
print(colibri2.getcolor())
print(colibri3.getage())
