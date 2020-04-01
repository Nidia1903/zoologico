class Animal:
    def __init__(self, nombre, tipo):
        self.nombre= name
        self.tipo= tipo
        print ("Nuevo animal creado ")
    
    def set_nombre(self,nombre):
        self.nombre = nombre
        print("El nuevo animal es " + self.nombre)

    def get_nombre(self):
        print("El animal actual es " + self.nombre)

    def set_tipo(self,tipo):
        self.tipo = tipo
        print("El animal es de tipo: " + self.tipo)
    
    def get_tipo(self):
        print("El actual tipo de animal es: " + self.tipo)
    
    lista1 =["Reptil","Tortuga"]
    

    for x in lista1:
        print(x)
    
    lista1.append("Animal")
    print(lista1)
    lista1.append(["Pug","Dog"])
    print(lista1)
    lista1.extend(["Beta","Fish"])
    print(lista1)

   lista2 =[1,2,3]
   print(id(lista2))
   print(id(lista2))
   print(id(lista2))

   def mostrar_id(objeto):
       print(id(objeto))

mostrar_id(lista2)

objeto = object()
mostrar_id(object)

    def main():
        Animal = Animal("Tigre","felino")
        Animal.set_nombre("tigre")
        Animal.get_nombre()


     
     