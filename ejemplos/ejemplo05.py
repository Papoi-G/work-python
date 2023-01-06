# Llamada a función con múltiples argumentos
def sumar(*args):
    resultado = 0
    for num in args:
        resultado += num
        # resultado = resultado + num
    return resultado


print(sumar(100, 200))
print(sumar(1, 2, 3, 4, 5, 6, 7))
print(sumar(100, 200, 300))




