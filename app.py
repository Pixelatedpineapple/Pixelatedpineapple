import pygame
import random
import sys
import math

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triangle Flappy")

WHITE = (255,255,255)
BLUE = (135,206,235)
GREEN = (0,200,0)

gravity = 2.5
bird_movement = 0
bird_x, bird_y = 120, HEIGHT//2
bird_size = 25

pipe_width = 70
pipe_gap = 250
pipe_speed = 6
pipes = []

font = pygame.font.SysFont(None,36)
clock = pygame.time.Clock()

game_active = False
score = 0
frame_count = 0


def rotate_point(x, y, angle):
    rad = math.radians(angle)
    rx = x * math.cos(rad) - y * math.sin(rad)
    ry = x * math.sin(rad) + y * math.cos(rad)
    return rx, ry


def draw_triangle(x, y, size, angle):
    points = [
        (size, 0),          # front
        (-size/2, size/2),  # bottom
        (-size/2, -size/2)  # top
    ]

    rotated = []
    for px, py in points:
        rx, ry = rotate_point(px, py, angle)
        rotated.append((x + rx, y + ry))

    pygame.draw.polygon(screen, WHITE, rotated)


def create_pipe():
    height = random.randint(150, HEIGHT-400)
    top = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT)
    return top, bottom


def move_pipes(pipes):
    for pipe in pipes:
        pipe.x -= pipe_speed
    return [pipe for pipe in pipes if pipe.x + pipe_width > 0]


def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)


def collision(bird_rect, pipes):
    if bird_rect.top <= 0 or bird_rect.bottom >= HEIGHT:
        return True
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True
    return False


pipes.extend(create_pipe())

running = True
space_pressed = False

while running:

    screen.fill(BLUE)

    space_pressed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if not game_active and event.key == pygame.K_SPACE:
                game_active = True
                bird_y = HEIGHT//2
                bird_movement = 0
                pipes.clear()
                pipes.extend(create_pipe())
                score = 0
            elif game_active:
                bird_movement = -20

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        space_pressed = True

    if game_active:

        bird_movement += gravity
        bird_y += bird_movement

        angle = -45 if space_pressed else 45
        draw_triangle(bird_x, bird_y, bird_size, angle)

        bird_rect = pygame.Rect(bird_x-15, bird_y-15, 30, 30)

        frame_count += 1
        if frame_count % 100 == 0:
            pipes.extend(create_pipe())

        pipes = move_pipes(pipes)
        draw_pipes(pipes)

        if collision(bird_rect, pipes):
            game_active = False

    else:
        text = font.render("Press SPACE to Start", True, (0,0,0))
        screen.blit(text,(WIDTH//2 - text.get_width()//2, HEIGHT//2))

    pygame.display.update()
    clock.tick(60)