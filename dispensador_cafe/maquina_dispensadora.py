from cafe import Cafe

class Maquina_Dispensadora:
    def __init__(self):
        self.recursos = {
            "agua": 300,
            "leche": 200,
            "cafe": 100
        }

    # Muestra las cantidades de recursos que tiene la máquina dispensadora
    # en el diccionario creado.
    def reporte(self):
        print(f"Agua: {self.recursos['agua']} ml")
        print(f"Leche: {self.recursos['leche']} ml")
        print(f"Cafe: {self.recursos['cafe']} gr")

    # parametro cafe es una objeto de la clase Cafe
    def hay_suficientes_recursos(self, cafe):
        suficiente = True
        for ingrediente in cafe.ingredientes:
            if cafe.ingredientes[ingrediente] > self.recursos[ingrediente]:
                print(f"Lo sentimos no tenemos suficiente {ingrediente}.")
                suficiente = False
        return suficiente

    def hacer_cafe(self, cafe):
        for ingrediente in cafe.ingredientes:
            self.recursos[ingrediente] -= cafe.ingredientes[ingrediente]
        print(f"Su cafe {cafe.nombre} está listo !!!")

    # NOS QUEDAMOS EN RECESO, REGRESAMOS A LAS 19:52

# if(cafe.ingredientes["agua"]) > recursos["agua"]
# maquina_dispensadora = Maquina_Dispensadora()
# cafe_latte = Cafe("latte", 100, 100, 50, 2.5)
# maquina_dispensadora.hacer_cafe(cafe_latte)
# 300 200 100
# 150 100 50 --> recursos actualizados