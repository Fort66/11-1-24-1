import pygame,sys
import math

pygame.init()
screen=pygame.display.set_mode((300,300))
bg = screen.copy().convert_alpha()

# Increase the mask layer
bgSurface = pygame.Surface((300, 300), flags=pygame.SRCALPHA)
pygame.Surface.convert_alpha(bgSurface)
bgSurface.fill(pygame.Color(0, 0, 0, 25))



clock=pygame.time.Clock()
i = 0
angle = 0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    # screen.fill((0,0,0))
    screen.blit(bgSurface,(0,0))

    #    
    pygame.draw.circle(bg,(46, 139, 87,5),(150,150),150)
    pygame.draw.circle(bg,(46, 139, 87,50),(150,150),150,2)
    pygame.draw.circle(bg,(46, 139, 87,5),(150,150),100)
    pygame.draw.circle(bg,(46, 139, 87,50),(150,150),100,2)
    pygame.draw.circle(bg,(46, 139, 87,5),(150,150),50)
    pygame.draw.circle(bg,(46, 139, 87,50),(150,150),50,2)

    #      
    pygame.draw.line(bg,(46, 139, 87,255),(0,150),(300,150),1)
    pygame.draw.line(bg,(46, 139, 87,255),(150,0),(150,300),1)

    #      
    posx = 150 + int(150 * math.sin(angle * math.pi / 180))
    posy = 150 - int(150 * math.cos(angle * math.pi / 180))
    pygame.draw.line(bg,(0,255,0,50),(150,150),(posx,posy),1)
    angle += 1

    i += 1
    screen.blit(bg,(0,0))
    clock.tick(100)
    pygame.display.update()
