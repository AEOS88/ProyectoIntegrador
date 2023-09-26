import readchar
import keyboard
import os

nombre = input("Ingresa tu nombre",)
print(f"Hola {nombre} espero que disfrutes mi Video Juego mucha suerte")

while True:
    key = keyboard.read_key()
    print(key)
    if key != "up":
        continue
    break

def clear_and_print(number):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(number)

def main():
    number = 0

    while number <= 50:
        key = input("Presiona la tecla 'n' para continuar: ")

        if key == "n":
            clear_and_print(number)
            number += 1


if __name__ == "__main__":
    main()



