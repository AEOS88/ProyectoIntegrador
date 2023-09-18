import keyboard

while True:
    key = keyboard.read_key()
    print(key)
    if key != "up":
        continue
    break
