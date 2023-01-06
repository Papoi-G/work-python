from menu import Menu
from maquina_dispensadora import Maquina_Dispensadora
from maquina_dinero import Maquina_Dinero

menu = Menu()
maquina_dispensadora = Maquina_Dispensadora()
maquina_dinero = Maquina_Dinero()

texto = input(f"Que tipo de café desea elegir {menu.obtener_nombres()}")
while texto != "off":
    if texto == "reporte":
        maquina_dispensadora.reporte()
        maquina_dinero.reporte()
    else:
        obj_cafe = menu.buscar_cafe(texto)
        if maquina_dispensadora.hay_suficientes_recursos(obj_cafe) and maquina_dinero.ejecutar_pago(obj_cafe.costo):
            maquina_dispensadora.hacer_cafe(obj_cafe)
    texto = input(f"Que tipo de café desea elegir {menu.obtener_nombres()}")


