# importamos los parametros de cotxe y colibri
from cotxe import cotxe
from colibri import colibri

# asignamos informacion a los parametros importados
cotxe1 = cotxe("subaru", "BRZ", "2016", "3", "negro")
cotxe2 = cotxe("ferrari", "f40", "1986", "3", "rojo")
cotxe3 = cotxe("porsche", "992 gt3", "2021", "3", "blanco")

colibri1 = colibri("Colibrí Rubí", "Aves", "2 años", "8 cm", "verde")
colibri2 = colibri("Colibrí Ventrirrojo", "Aves", "1 año", "7.5 cm", "rojo")
colibri3 = colibri("Colibrí de Pico Largo", "Aves", "3 años", "9 cm", "azul")

# mostramos los datos guardados sobre coche y colibri
print("La marca del coche 1 es ",cotxe1.getmarca())
print("El modelo del coche 2 es ",cotxe2.getmodel())
print("El año de creacion del coche 3 fue en ",cotxe3.getage())

print("El color del colibri 1 es ",colibri1.getcolor())
print("La edad media del colibri 2 es de ",colibri2.getage())
print("El nombre del colibri 1 es ",colibri1.getnom())
print("La longitud media del colibri 3 es ",colibri3.getlongitud())


#pimero modificaremos las variables para luego mostrarlo con getters 
cotxe1.setcolor("azul")
cotxe3.setmodel("992 gt3 rs")
print("el color del cotxe 1 ahora es ",cotxe1.getcolor())
print("el model del cotxe 3 ahora es ",cotxe3.getmodel())

#Al igual que anteriormente mostrara el contenido dela va
colibri2.setcolor("amarillo")
colibri1.setlongitud("7 cm")
print("el color del colibri 2 ahora es ",colibri2.color)
print("La longitud media del colibri 3 es ",colibri1.longitud)

