class Cafe:

    # Tipos de café
    def __init__(self, nombre, agua, leche, cafe, costo):
        self.nombre = nombre
        self.costo = costo
        self.ingredientes= {
            "agua": agua,
            "leche": leche,
            "cafe": cafe
        }


# cafe_latte = Cafe("latte", 150, 50, 50, 2.5)
# cafe_latte.
# cafe = Cafe("latte", 100, 150, 100, 2.1)
# for ingrediente in cafe.ingredientes:
#     print(ingrediente)