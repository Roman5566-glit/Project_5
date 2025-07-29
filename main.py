import pygame
import random
import time

# 🧱 Инициализация
pygame.init()
WIDTH, HEIGHT = 600, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Space Dodger")

# 🎨 Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

# 🧍 Игрок
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# ☄️ Астероиды
asteroid_size = 50
asteroid_speed = 5
asteroids = []

# 🕹️ Игровой цикл
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont("Arial", 30)
running = True

def draw_window():
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, (player_x, player_y, player_size, player_size))
    for ax, ay in asteroids:
        pygame.draw.rect(win, RED, (ax, ay, asteroid_size, asteroid_size))
    score_text = font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10))
    pygame.display.update()

def check_collision(px, py, ax, ay):
    return (
        px < ax + asteroid_size and
        px + player_size > ax and
        py < ay + asteroid_size and
        py + player_size > ay
    )

while running:
    clock.tick(60)
    draw_window()

    # 🎯 Спавн астероидов
    if random.randint(1, 20) == 1:
        ax = random.randint(0, WIDTH - asteroid_size)
        asteroids.append([ax, 0])

    # 📉 Движение астероидов
    for asteroid in asteroids:
        asteroid[1] += asteroid_speed
        if asteroid[1] > HEIGHT:
            asteroids.remove(asteroid)
            score += 1
        elif check_collision(player_x, player_y, asteroid[0], asteroid[1]):
            running = False

    # 🎮 Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # 🧱 Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 🧨 Game Over
win.fill(BLACK)
game_over_text = font.render(f"Game Over! Final Score: {score}", True, WHITE)
win.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
pygame.display.update()
time.sleep(3)
pygame.quit()
