from tkinter import messagebox, Tk
import pygame
import sys
import random

window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))

columns = 25
rows = 25
box_width = window_width // columns
box_height = window_height // rows

clock = pygame.time.Clock()

grid = []
snake = []
apples = []


class Box:
    def __init__(self, i, j):
        self.x = i
        self.y = j

    def draw(self, win, color):
        pygame.draw.rect(win, color, (self.x * box_width, self.y * box_height, box_width - 2, box_height - 2))


# Create Grid
for i in range(columns):
    arr = []
    for j in range(rows):
        arr.append(Box(i, j))
    grid.append(arr)

# Starting Snake
for i in range(3):
    snake.append(grid[10][10])


def main():
    x_delta, y_delta = 0, -1
    x_pos, y_pos = 10, 10

    run = True
    while run:
        # Quit Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # User Input
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_LEFT] and x_delta != 1:
            x_delta, y_delta = -1, 0
        if user_input[pygame.K_RIGHT] and x_delta != -1:
            x_delta, y_delta = 1, 0
        if user_input[pygame.K_UP] and y_delta != 1:
            x_delta, y_delta = 0, -1
        if user_input[pygame.K_DOWN] and y_delta != -1:
            x_delta, y_delta = 0, 1

        # Snake Movement
        x_pos += x_delta
        y_pos += y_delta

        # Game Over
        wall_hit = x_pos < 0 or y_pos < 0 or x_pos > 24 or y_pos > 24
        if not wall_hit:
            self_hit = grid[x_pos][y_pos] in snake
        if self_hit or wall_hit:
            Tk().wm_withdraw()
            messagebox.showinfo("Game Over", "You lost the Game!")
            run = False

        # Game Running
        else:
            head = grid[x_pos][y_pos]
            snake.append(head)
            remove_tail = True

            # Spawn Apple
            if len(apples) == 0:
                spawn_locations = []
                for i in range(columns):
                    for j in range(rows):
                        if not grid[i][j] in snake:
                            spawn_locations.append(grid[i][j])
                if len(spawn_locations) == 3:
                    Tk().wm_withdraw()
                    messagebox.showinfo("Winner", "You won the Game!")
                    run = False
                apple = spawn_locations[random.randint(0, len(spawn_locations))]
                apples.append(apple)

            # Eat Apple
            if len(apples) == 1:
                if x_pos == apples[0].x and y_pos == apples[0].y:
                    apples.pop()
                    remove_tail = False

            # Remove Tail
            if remove_tail:
                tail = snake.pop(0)
                remove_tail = False

        # Draw
        window.fill((0, 0, 0))
        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]
                box.draw(window, (180, 180, 180))
                if box in snake:
                    box.draw(window, (0, 0, 255))
                if box in apples:
                    box.draw(window, (255, 0, 0))

        pygame.display.flip()
        clock.tick(8)


main()
