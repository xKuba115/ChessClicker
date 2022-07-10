import pygame
import time

pygame.init()
backgroundColour = (44, 82, 55)

X = 800
Y = 800
x = X/2 - 100
y = 100
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('ChessClicker')
screen.fill(backgroundColour)
click=pygame.image.load('click.png')
click = pygame. transform. scale(click, (200, 200))
screen.blit(click, (x, y))
check =0 
pygame.display.flip()
running = True
white = (255, 255, 255)
black = (0, 0, 0)
pawn=pygame.image.load('pawn.png')
screen.blit(pawn, (50, 50))
multiply=1


def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('czcionka.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)





while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False      

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.display.init
            x, y = event.pos 
            if click.get_rect().collidepoint(x-(X/2 - 100), y-100):
                pygame.display.update()
                check=check+multiply
            if pawn.get_rect().collidepoint(x-50,y-50):
                if check>19:
                    multiply=multiply+1
                    check=check-20
    
                

        DrawText("You made " + str(f'{check:.2f}') + " checks", black, white, X/2, 50, 20)
        DrawText("Buy pawn(+1 to click) - 20checks", black,backgroundColour, 110 , 110, 13)
    pygame.display.update()




