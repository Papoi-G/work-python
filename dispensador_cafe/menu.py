from cafe import Cafe
# Menú con diferentes tipos de café ##
# Latte
# Expresso
# Capuccino
class Menu:
    def __init__(self):
        # cafe_latte = Cafe(nombre="latte", agua=200, leche=150, cafe=24, costo=2.5)
        # cafe_expresso = Cafe(nombre="latte", agua=200, leche=150, cafe=24, costo=2.5)
        # cafe_capuccino = Cafe(nombre="latte", agua=200, leche=150, cafe=24, costo=2.5)
        # self.menu =[cafe_latte, cafe_expresso, cafe_capuccino]
        # LISTA DE OBJETOS A PARTIR DE LA CLASE Cafe
        self.menu = [
            Cafe(nombre="latte", agua=200, leche=150, cafe=24, costo=2.5),
            Cafe(nombre="expresso", agua=50, leche=0, cafe=18, costo=1.5),
            Cafe(nombre="capuccino", agua=250, leche=50, cafe=24, costo=3)
        ]

    def obtener_nombres(self):
        # Devuelve los nombres de los cafés del menú
        opciones = ""
        for cafe in self.menu:
            opciones += cafe.nombre + " | "  # latte  |  expresso  | capuccino
        return opciones

    # El parámetro recibido será el string que el usuario ingreso
    def buscar_cafe(self, cafe):
        for objeto_cafe in self.menu:
            if objeto_cafe.nombre == cafe:
                return objeto_cafe
        print("Lo siento el café solicitado no está disponible")

# Cuando en un método se llega a la línea del return, ya no se ejecuta lo que está abajo del mismo
# menu = Menu()
# test = menu.buscar_cafe("latte")
# print(test)