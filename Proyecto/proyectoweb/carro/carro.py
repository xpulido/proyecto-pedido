class Carro : #determinamos la clase carro con sus metodos/funciones
    def __init__(self, request):  # self es una instancia de la clase y request el parametro
        self.request=request # establece el articulo request de la instancia como el objeto recibido
        self.session=request.session # establece el atributo 'session' de la instacia como el taribuo 'sessio' de 
        carro=self.session.get("carro") # a ese carro asignarle lo del carrito
        if not carro:  # si no hay carro el carro esta vacio en la sesion
            carro=self.session["carro"]={} # crea un nuevo carrito vacio en la sesion"""
        #else: # si el carro existe en la sesion y no esta vacio
        self.carro=carro #establece el atributo carro de la instancia como el carrito existente

    def agregar(self,producto):# una funcion llamada agregar, creamos la instancia self y le pasamos el parametro de producto
        if(str(producto.id)not in self.carro.keys()): #si el producto.id como string(str)
            self.carro[producto.id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url}
            
        else:
            for key,value  in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+producto.precio
                    break 
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session["carro"]=self.carro # trae lo que tengo en la session y lo guarda en la lista"carro"
        self.session.modified=True # session modificada(cerrar sesion) y guarda

    def eliminar(self,producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar(self,producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(value["precio"])-producto.precio
                if value ["cantidad"]<1:
                    self.eliminar(producto)
                    break
        self.guardar_carro()

    def limpiar(self):
        self.session["carro"]={}
        self.session.modifield=True


