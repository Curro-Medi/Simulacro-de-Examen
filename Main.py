from EjercicioExamen.Producto import Producto
from EjercicioExamen.Funciones import transformar_ventas
lista=[(1,1,100,'Huelva',None,'producto1',15,9),(2,1,100,'Sevilla',None,'producto1',15,9),(3,2,100,'Sevilla',None,'producto2',18,11),(4,2,100,'Sevilla',None,'producto2',18,11),(5,2,100,'Huelva',None,'producto2',18,11),(6,3,100,'Sevilla',None,'producto3',21,12),(7,3,100,'Cordoba',None,'producto3',21,12),(8,4,100,'Sevilla',None,'producto4',24,13),(9,4,100,'Huelva',None,'producto4',24,13),(10,4,100,'Cordoba',None,'producto4',24,13)]
resultado = []

for importe in lista:
    importetotal = (importe.__getitem__(2)*importe.__getitem__(6) ) - importe.__getitem__(7)
    #print(dic)
    prod = (importe.__getitem__(5), importe.__getitem__(6), importe.__getitem__(7), importetotal)
    resultado.append(prod)
    
#print(resultado)    

print(transformar_ventas(lista))

    