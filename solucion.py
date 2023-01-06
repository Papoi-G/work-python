import random
piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lista_opciones = [piedra, papel, tijera]
print("Bienvenido al juego de piedra, papel o tijera")
usuario_selecciona = int(input("Selecciona una opción: 0.Piedra, 1.Papel, 2.Tijera"))
if usuario_selecciona >= 3 or usuario_selecciona < 0:
    print("Selección no válida. Perdiste! ")
else:
    print("Elegiste: ")
    print(lista_opciones[usuario_selecciona])
    select_computadora = random.randint(0, 2)
    print("Selección computadora: ")
    print(lista_opciones[select_computadora])
    if usuario_selecciona == 0 and select_computadora == 2:
        print("Ganaste!")
    elif select_computadora == 0 and usuario_selecciona == 2:
        print("Perdiste!")
    elif usuario_selecciona > select_computadora:
        print("Ganaste! ")
    elif select_computadora > usuario_selecciona:
        print("Perdiste!")
    elif usuario_selecciona == select_computadora:
        print("Empate")


