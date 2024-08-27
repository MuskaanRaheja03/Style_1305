#Name- Muskaan Raheja
#Student id- 101284985

from math import pi
import pygame

screen = pygame.display.set_mode((500,500))

screen.fill((255,255,255))

#face
pygame.draw.circle(screen, (0,0,0), (250,170), 25, 0)
#eye
pygame.draw.circle(screen, (255,255,255), (257,161), 4, 0)
#mouth
pygame.draw.arc(screen, (255,255,255), (257,170,16,10), pi, 0)
#body
pygame.draw.arc(screen, (0,0,0), (225, 200, 50, 50),0, pi, 25)
pygame.draw.rect(screen, (0,0,0), (225,225,50,60))
#arms
pygame.draw.arc(screen, (0,0,0), (215, 220, 30, 40), pi/2, 4, 3)
pygame.draw.arc(screen, (0,0,0), (257, 190, 36, 43), 3*(pi/2), 1.1, 3)
#hands
pygame.draw.circle(screen, (0,0,0), (223,255), 4, 0)
pygame.draw.circle(screen, (0,0,0), (282,194), 4, 0)
#legs
pygame.draw.arc(screen, (0,0,0), (190, 260, 50, 60), (3*pi)/2, 0.25, 3)
pygame.draw.arc(screen, (0,0,0), (259, 260, 50, 60), 2.9, 3*(pi/2), 3)
#feet
pygame.draw.rect(screen, (0,0,0), (212,316,10,5))
pygame.draw.rect(screen, (0,0,0), (282,316,10,5))
#cherry
pygame.draw.circle(screen, (200,0,0), (282,188), 6, 0)
pygame.draw.arc(screen, (0,200,0), (282, 178, 5, 5), (pi/2), 4, 1)

pygame.display.update()

filename = "Style 1305.png"

pygame.image.save(screen, filename)