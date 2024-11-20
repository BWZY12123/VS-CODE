import pygame

pygame.init()
screen = pygame.display.set_mode((1288,720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_radius = 40

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 200 * dt
    if keys[pygame.K_s]:
        player_pos.y += 200 * dt 
    if keys[pygame.K_a]:
        player_pos.x -= 200 * dt 
    if keys[pygame.K_d]:
        player_pos.x += 200 * dt

    if player_pos.x - player_radius < 0:
        player_pos.x = player_radius
    if player_pos.x + player_radius > screen.get_width():
        player_pos.x = screen.get_width() - player_radius
    if player_pos.y - player_radius < 0:
        player_pos.y = player_radius
    if player_pos.y + player_radius > screen.get_height():
        player_pos.y = screen.get_height() - player_radius
    pygame.display.flip()

    dt = clock.tick(60) / 1000
pygame.quit()
