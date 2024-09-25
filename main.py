import pygame

pygame.init()

# Creating the window with title
pygame.display.set_caption("Shooter")
scr = pygame.display.set_mode((1080,720))


# Importing the background image
bg = pygame.image.load("assets/bg.jpg")


# While run is True, the window stays opened
run = True

while run == True:
    
    # Apply background
    scr.blit(bg, (0,-200))
    
    # Updating screen
    pygame.display.flip()
    
    
    # Closing the window if Escape is pressed or the user clicks on quit
    key = pygame.key.get_pressed()
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            run = False
            pygame.quit()