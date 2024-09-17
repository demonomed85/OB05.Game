import pygame
pygame.init()
import time

widows_x = 800
widows_y = 600
window_size = (widows_x, widows_y)
background = pygame.image.load("Асфальт.png")
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Игра")


car_image = pygame.image.load("main_avto.png")
car_image_rect = car_image.get_rect()
block_image = pygame.image.load("block.png")
block_image_rect = block_image.get_rect()

block_image_rect.x = 25
block_image_rect.y = -200


car_image_rect.x = 40
car_image_rect.y = widows_y-136-25


car_speed = 5
block_speed = 2

# Шрифт для текста
font = pygame.font.Font(None, 36)
black = (0, 0, 0)
def display_message(message):
    global block_speed
    global car_speed
    text = font.render(message, True, black)
    screen.blit(text, (widows_x // 2 - text.get_width() // 2, widows_y // 2 - text.get_height() // 2))
    block_speed = 0
    car_speed = 0

clock = pygame.time.Clock()

running = True
while running:
    #time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for y in range(0, 800, 200):
        for x in range(0, 800, 200):
           screen.blit(background, (x, y))

    if block_image_rect.colliderect(car_image_rect):
            display_message("Столкновение произошло!")

    screen.blit(block_image, block_image_rect)

    block_image_rect.y += block_speed

    if block_image_rect.y > window_size[1]:
        block_image_rect.y = -200

    screen.blit( car_image, car_image_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_image_rect.x > 0:
        car_image_rect.x -= car_speed
    if keys[pygame.K_RIGHT] and car_image_rect.x < window_size[0] - car_image_rect.width:
        car_image_rect.x += car_speed
    if keys[pygame.K_UP] and car_image_rect.y > 0:
        car_image_rect.y -= car_speed
    if keys[pygame.K_DOWN] and car_image_rect.y < window_size[1] - car_image_rect.height:
        car_image_rect.y += car_speed

    pygame.display.update()
    clock.tick(60)  # Ограничение FPS
pygame.quit()
