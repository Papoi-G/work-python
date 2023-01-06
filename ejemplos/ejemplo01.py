# 1. Crear una clase
# Una convención es que el nombre de las clases
# debe iniciar con mayúscula
# 2. Crear sus atributos.
class Alumno:
    carnet = 123456

    # 3. Crear métodos de clase
    def saludar(self):
        return "Hola POO"

    def pagar(self):
        # deberia de obtener el pago
        # registrar en la base de datos
        print("Realizó el pago de la mensualidad")