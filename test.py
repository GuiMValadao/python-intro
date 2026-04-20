import pygame

pygame.init()
display_surface = pygame.display.set_mode((300, 300))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            print(event.key, event.mod)
