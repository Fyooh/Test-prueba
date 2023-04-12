#Declarando variable
nombre = "Alberto"
name = "Juan"

 #IMPRESION UNA VARIABLE
print(nombre)
print(name)
print("Hola soy", nombre)
print("Hola soy", name)#declarando variable numerica
edad = 20
print("Mi edad es de",edad)
print("Hola mi nomre es",nombre, "y tengo",edad,"años")#Impresion separando con comas
print("Hola mi nombre es"+" "+name+" "+" y tengo"+" "+str (edad))#Consentracion +
print(f"Mi nombre es {nombre} y tengo {edad} años")#Formato (f, {})

#ACTUALIZANDO LA VARIABLE NOMBRE (mMutable)
nombre = "qwewqr"
print("Hola mi nuevo nombre es",nombre)

#¿VARIABLE EN UNA SOLA LINEA? (No es muy recomendable, sólo en ciertas situaciones)
ciudad, region, pais, year = "Osorno", "Los Lagos", "Chile", "2023"

#UTILIZANOD LA INTRUCCIÓN INPUT
nombre1 = input("¿Cual es tu nombre?")
edad1 = input("¿Cual es tu edad?")
