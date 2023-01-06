from ejemplo04 import Factura

factura01 = Factura("001")
factura02 = Factura("002")
#factura01.lista_productos.append("acetaminofen")
#factura02.lista_productos.append("alerfin")
factura01.agregar_producto("acetaminofen")
factura02.agregar_producto("alerfin")

# Imprimos las variables de clase
print(factura01.vendedor)
print(factura02.vendedor)
# Imprimo las variables de objeto
print(factura01.codigo_factura)
print(factura02.codigo_factura)

print(factura01.lista_productos)
print(factura02.lista_productos)