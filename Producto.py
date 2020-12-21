class Producto:
    
    def __init__(self, nombre, precio_unitario, coste_produccion, importetotal):
        self.__nombre = nombre
        self.__precio_unitario = precio_unitario
        self.__coste_produccion = coste_produccion
        self.__importetotal = importetotal

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre


    @property
    def precio_unitario(self):
        return self.__precio_unitario

    @precio_unitario.setter
    def precio_unitario(self,precio_unitario):
        self.__precio_unitario = precio_unitario

    
    @property
    def coste_produccion(self):
        return self.__coste_produccion

    @coste_produccion.setter
    def coste_produccion(self,coste_produccion):
        self.__coste_produccion = coste_produccion
        
        
    @property
    def importetotal(self):
        return self.__importetotal

    @importetotal.setter
    def importetotal(self,importetotal):
        self.__importetotal = importetotal
        
        
        

        
        
        