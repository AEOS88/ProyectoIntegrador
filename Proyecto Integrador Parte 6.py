import readchar
import os
import random
from functools import reduce

WALL = "#"
PATH = "."
PLAYER = "P"


class Juego:
    def __init__(self, maze):
        self.px = 0
        self.py = 0
        self.maze = maze
        self.place_player(0, 0)

    def imprimir_instrucciones(self):
        print("\nINSTRUCCIONES: ")
        print("\tUsa las flechas para moverte, q para salir")

    def print_maze(self):
        for row in self.maze:
            print("".join(row))
        self.imprimir_instrucciones()

    def place_player(self, dx, dy):
        maze_width = len(self.maze[0])
        maze_height = len(self.maze)

        if self.px + dx < 0 or self.px + dx >= maze_width or self.py + dy < 0 or self.py + dy >= maze_height:
            return

        if self.py + dy == maze_height - 1 and self.px + dx == maze_width - 1:
            print("\n\n\t\tG A N A S T E\n\n")
            exit()

        if self.maze[self.py + dy][self.px + dx] == PATH:
            self.maze[self.py][self.px] = PATH
            self.maze[self.py + dy][self.px + dx] = PLAYER
            self.px = self.px + dx
            self.py = self.py + dy


class JuegoArchivo(Juego):
    def __init__(self, map_folder):
        maze_file = self.elegir_archivos_aleatorios(map_folder)
        maze_data = self.read_maze_file(map_folder, maze_file)
        super().__init__(maze_data)

    def elegir_archivos_aleatorios(self, map_folder):
        files = os.listdir(map_folder)
        return random.choice(files)

    def read_maze_file(self, map_folder, file_name):
        path_to_file = os.path.join(map_folder, file_name)
        with open(path_to_file, "r") as f:
            maze_content = f.readlines()
            maze_content = reduce(lambda x, y: x + y, map(str.strip, maze_content))
            return list(map(lambda x: list(x), maze_content))


if __name__ == "__main__":
    map_folder = "maps_folder"
    juego = JuegoArchivo(map_folder)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        juego.print_maze()
        key = readchar.readkey()

        if key == "q":
            break
        elif key.lower() == "a" or key == readchar.key.LEFT:
            juego.place_player(-1, 0)
        elif key.lower() == "s" or key == readchar.key.DOWN:
            juego.place_player(0, 1)
        elif key.lower() == "d" or key == readchar.key.RIGHT:
            juego.place_player(1, 0)
        elif key.lower() == "w" or key == readchar.key.UP:
            juego.place_player(0, -1)
