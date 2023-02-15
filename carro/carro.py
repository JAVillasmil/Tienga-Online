from django.contrib import messages

class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro

    def Guardado(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def Agrega_1(self, producto):
        if producto.stock == 0:
            pass
        else:
            if (str(producto.id) not in self.carro.keys()):
                self.carro[producto.id] = {"producto_id": producto.id,
                                           "nombre": producto.nombre,
                                           "precio": producto.precio,
                                           "cantidad": 1,
                                           "precio_cantidad": producto.precio,
                                           "stock":  producto.stock,
                                           "imagen": producto.imagen.url,
                                           "proveedor": producto.proveedor.nombre,
                                           "descripcion": producto.descripcion,
                                           }
            else:
                for key, value in self.carro.items():
                    if key == str(producto.id):
                        if (value["cantidad"]) == producto.stock:
                           pass
                        else:
                            value["cantidad"] = value["cantidad"] + 1
                            value["precio_cantidad"] = round((int(value["cantidad"])*float(value["precio"])),2)
                            break
        self.Guardado()

    def Eliminado(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.Guardado()

    def Restado_1(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] -= 1
                value["precio_cantidad"] = round((int(value["cantidad"]) * float(value["precio"])), 2)
                if value["cantidad"] < 1:
                    self.Eliminado(producto)
                break
        self.Guardado()

    def Limpiado(self):
        self.session["carro"] = {}
        print(self.session["carro"])
        self.session.modified = True
