class Factura:
    # Variable de clase --> compartidas por todos los objetos
    vendedor = "Marlon Enrique"
    # lista_productos = []

    def __init__(self, codigo_factura):
        self.codigo_factura = codigo_factura # Variable de instancia (objeto)
        self.lista_productos = []

    # Este método se encarga de tomar el producto por parámetro y agregarlo
    # a la lista utilizando el método append de la lista.
    def agregar_producto(self, producto):
        self.lista_productos.append(producto)


