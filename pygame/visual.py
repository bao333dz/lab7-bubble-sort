import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Bubble Sort")
clock = pygame.time.Clock()

#Load image 
sky = pygame.image.load("pygame/graphics/sky.png").convert_alpha()
#Scale images to fit window
sky = pygame.transform.scale(sky, (800, 300))
#Make the rectangle
sky_rect = sky.get_rect(midtop = (400, 0))

ground = pygame.image.load("pygame/graphics/ground.png").convert_alpha()
ground = pygame.transform.scale(ground, (800, 100))
ground_rect = ground.get_rect(midbottom = (400,400))

ghost = pygame.image.load("pygame/graphics/ghost.png").convert_alpha()
ghost = pygame.transform.scale(ghost, (60, 60))
ghost_rect = ghost.get_rect()
ghost_rect.midbottom = ground_rect.midtop

player = pygame.image.load("pygame/graphics/player.png").convert_alpha()
player = pygame.transform.scale(player, (45, 65))
player_rect = player.get_rect()
player_rect.bottomleft = ground_rect.topleft

# score = test_font.render("My Game", True, "Black")
# score_rect = score.get_rect()
# score_rect.center = sky_rect.center

#This is to draw the line
draw_line = False
#This is to define the ray aka the line drawn by mouse click
ray = None

while True:
    for event in pygame.event.get():
        #Take the input (in this case, quitting the program)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Check if mouse is clicked or not
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw_line = True

        if event.type == pygame.KEYDOWN:
            pass


    #If run out of screen, teleport back
    ghost_rect.left -= 1
    if ghost_rect.left < -80: ghost_rect.left = 780

    #Display the regular surface on the display surface
    screen.blit(ground, ground_rect)
    screen.blit(sky, sky_rect)
    screen.blit(ghost, ghost_rect)
    screen.blit(player, player_rect)

    #This is to get the mouse postition and drawn the line and imediately erase it
    mouse_pos = pygame.mouse.get_pos()
    if draw_line:
        ray = pygame.draw.line(screen, "Gold", player_rect.midright, mouse_pos, 3)
        draw_line = False

    #Check if the line is there and collide with the ghost, the ghost disapear
    if ray and ray.colliderect(ghost_rect):
        ghost_rect.left = 850
    
    ray = None

    #Update stuff to the screen
    pygame.display.update()
    #FPS
    clock.tick(60)


