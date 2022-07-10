import pygame
import time

pygame.init()
backgroundColour = (44, 82, 55)
clock=pygame.time.Clock()
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
screen.blit(pawn, (50, 400))
rook=pygame.image.load('rook.png')
screen.blit(rook, (50, 500))
multiply=1
pawnPrice = 20
pawnLevel= 0
pawnPriceMultiply = 1.3
rookPrice=200
rookLevel = 0
rookPriceMultiply=1.5
autoC = 0
pawnMultiply = 1

def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('czcionka.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)

def AutoChecks():
    global check
    global autoC
    clock.tick(60)
    time.sleep(0.1)
    check=check+autoC

def main_loop():
    global pawnMultiply
    global running
    global autoC
    global rookPriceMultiply
    global rookLevel
    global rookPrice
    global pawnPriceMultiply
    global pawnLevel
    global pawnPrice
    global multiply
    global screen
    global rook
    global pawn
    global black
    global white
    global check


    while running:
        if running:
            pygame.display.update()
            AutoChecks()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False      

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.init
                x, y = event.pos 
                if click.get_rect().collidepoint(x-(X/2 - 100), y-100):
                    pygame.display.update()
                    check=check+multiply
                if pawn.get_rect().collidepoint(x-50,y-400):
                    if check>=pawnPrice:
                        pawnLevel=pawnLevel+1
                        multiply=multiply+pawnMultiply
                        check=check-pawnPrice
                        if pawnLevel%3==0:
                            pawnPriceMultiply=pawnPriceMultiply+0.05
                        pawnPrice=pawnPrice*pawnPriceMultiply
                        if pawnLevel%10==0 and pawnLevel!=0:
                            multiply=multiply*3
                            pawnMultiply=pawnMultiply+1


                if rook.get_rect().collidepoint(x-50,y-500):
                    if check>=rookPrice:
                        rookLevel=rookLevel+1
                        check=check-rookPrice
                        autoC=autoC+0.3
                        if rookLevel%3==0:
                            rookPriceMultiply=rookPriceMultiply+0.1
                        rookPrice=rookPrice*rookPriceMultiply
                        if rookLevel%10==0 and pawnLevel!=0:
                            autoC=autoC*2                      

                    
                 
    
                

        DrawText("   You made " + str(f'{check:.2f}') + " checks   ", black, white, X/2, 50, 20)
        DrawText("Buy pawn for  " + str(f'{pawnPrice:.2f}') + " checks(+1 to click power, *3 every 10lvl)", black,backgroundColour, 330 , 420, 13)
        DrawText("You have " + str(f'{pawnLevel:.2f}') + " pawns", black,backgroundColour, 330 , 440, 13)
        DrawText("Buy rook for  " + str(f'{rookPrice:.2f}') + " checks(3check/sec, *2 every 10lvl)", black,backgroundColour, 330 , 520, 13)
        DrawText("You have " + str(f'{rookLevel:.2f}') + " rooks", black,backgroundColour, 330 , 540, 13)
        DrawText("You have " + str(f'{multiply:.2f}') + " click power", black,backgroundColour, 660 , 50, 16)
        DrawText("You have " + str(f'{autoC*10:.2f}') + " checks per second", black,backgroundColour, 660 , 80, 16)
        


        pygame.display.update()

main_loop()
pygame.quit()
quit()


