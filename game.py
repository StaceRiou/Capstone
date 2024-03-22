import pygame

pygame.init()

# Creating the window for the game.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Displaying the title for the game.
pygame.display.set_caption("Monster Run")

GREEN = (115, 184, 4)

FPS = 60

# WORK ON IMPORTING MONSTERS----------------
MAIN_MONSTER_IMAGE = pygame.image.load('monster.png').convert_alpha()
WIDTH = MAIN_MONSTER_IMAGE.get_width()
HEIGHT = MAIN_MONSTER_IMAGE.get_height()
MAIN_MONSTER2 =  pygame.transform.scale(MAIN_MONSTER_IMAGE , (WIDTH * 0.09, HEIGHT * 0.09))


#creating a function for screen.
def draw_screen():
    SCREEN.fill((GREEN))
    screen_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  
    monster_center = (screen_center[0] - MAIN_MONSTER2.get_width() // 2, screen_center[1] - MAIN_MONSTER2.get_height() // 2)
    SCREEN.blit(MAIN_MONSTER2, monster_center)
    pygame.display.update()


# Creating the game loop function.
def game_loop():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_screen()
    
    pygame.quit()

if __name__ == "__main__":
    game_loop()
