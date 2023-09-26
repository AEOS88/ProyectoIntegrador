import pygame

# Initialize pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Laberinto")

# Set the maze colors
wall_color = (0, 0, 0)  # black
player_color = (255, 255, 0)  # yellow
exit_color = (0, 255, 0)  # green

# Set the maze layout
maze = [
    "WWWWWWWWWWWWWWWWWWW",
    "W        PW       W",
    "W WWWWW   WWW   WW",
    "W    WW         EW",
    "WWWWW W  W WWWW WW",
    "W      W   W     W",
    "WWWWWWW   WW WWWW",
    "W          W    W",
    "W WWWW WW W   WW",
    "W  W       WW  W",
    "WWWWWWWWWWWWWW",
]

# Define the player position
player_pos = [1, 1]

# Define the exit position
exit_pos = [7, 18]

# Define the player size
player_size = 40

# Run the game loop
running = True
while running:
    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Draw the maze
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "W":
                pygame.draw.rect(screen, wall_color,
                                 pygame.Rect(col * player_size, row * player_size, player_size, player_size))
            elif maze[row][col] == "P":
                pygame.draw.rect(screen, player_color,
                                 pygame.Rect(col * player_size, row * player_size, player_size, player_size))
            elif maze[row][col] == "E":
                pygame.draw.rect(screen, exit_color,
                                 pygame.Rect(col * player_size, row * player_size, player_size, player_size))

    # Update the screen
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Move the player
            if event.key == pygame.K_UP:
                if maze[player_pos[0] - 1][player_pos[1]] != "W":
                    player_pos[0] -= 1
            elif event.key == pygame.K_DOWN:
                if maze[player_pos[0] + 1][player_pos[1]] != "W":
                    player_pos[0] += 1
            elif event.key == pygame.K_LEFT:
                if maze[player_pos[0]][player_pos[1] - 1] != "W":
                    player_pos[1] -= 1
            elif event.key == pygame.K_RIGHT:
                if maze[player_pos[0]][player_pos[1] + 1] != "W":
                    player_pos[1] += 1

    # Check if the player reached the exit
    if player_pos == exit_pos:
        running = False

# Quit pygame
pygame.quit()
#This code sets up a simple maze game using the `pygame` library. The maze is represented as a list of strings where "W" represents walls, "P" represents the player, and "E" represents the exit. The player can move using the arrow keys and the game terminates when the player reaches the exit.