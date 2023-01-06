class Maquina_Dinero:
    MONEDA = "$"

    VALORES_MONEDA= {
        "venticinco": 0.25,
        "diez": 0.10,
        "cinco": 0.05,
        "un centavo": 0.01
    }

    def __init__(self):
        self.ingreso_venta = 0
        self.dinero_recibido = 0

    def reporte(self):
        print(f"Dinero: {self.MONEDA}{self.ingreso_venta}")

    def procesar_dinero(self):
        print("Por favor ingrese las monedas: ")
        for moneda in self.VALORES_MONEDA:
            self.dinero_recibido += int(input(f"Cuantas monedas de {moneda}? ")) * self.VALORES_MONEDA[moneda]
        return round(self.dinero_recibido, 2)

    def ejecutar_pago(self, costo):
        self.procesar_dinero()
        if self.dinero_recibido >= costo:
            cambio = round(self.dinero_recibido - costo, 2)
            print(f"Aquí está su cambio: {self.MONEDA}{cambio}")
            self.ingreso_venta += costo
            self.dinero_recibido = 0
            return True
        else:
            print(f"Lo siento, el dinero ingresado: {self.dinero_recibido} no es suficiente. El costo del café es: {costo}")
            self.dinero_recibido = 0
            return False



# maquina_dinero = Maquina_Dinero()
# maquina_dinero.ejecutar_pago(2.5)