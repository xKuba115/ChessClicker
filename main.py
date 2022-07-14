import pygame
import time
import json

pygame.init()
backgroundColour = (44, 82, 55)
clock=pygame.time.Clock()
X = 800
Y = 800
x = X/2 - 200
y = 100
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('ChessClicker')
screen.fill(backgroundColour)
click=pygame.image.load('click.png')
click = pygame. transform. scale(click, (200, 200))
reset=pygame.image.load('reset.png')
reset = pygame. transform. scale(reset, (100, 100))
screen.blit(reset,(700,700))
screen.blit(click, (x, y))
check =0 
pygame.display.flip()
running = True
white = (255, 255, 255)
black = (0, 0, 0)
pawn=pygame.image.load('pawn.png')
screen.blit(pawn, (50, 400))
rook=pygame.image.load('rook.png')
bishop=pygame.image.load('bishop.png')
knight=pygame.image.load('knight.png')
clickclick=pygame.image.load('clickclick.png')
screen.blit(rook, (50, 500))
screen.blit(bishop, (50, 600))
screen.blit(knight, (50, 700))
multiply=1
pawnPrice = 20
pawnLevel= 0
pawnPriceMultiply = 1.3
rookPrice=200
rookLevel = 0
rookPriceMultiply=1.5
autoC = 0
autoCmultiply = 1
pawnMultiply = 1
bishopPrice = 800
bishopLevel = 0
bishopPriceMultiply = 1.8
knightPrice = 2200
knightLevel = 0
knightPriceMultiply = 3

with open('score.txt') as scoreFile:
    check=json.load(scoreFile)
with open('pawnMultiply.txt') as pawnMultiplyFile:
    pawnMultiply=json.load(pawnMultiplyFile)
with open('autoC.txt') as autoCFile:
    autoC=json.load(autoCFile)
with open('rookPriceMultiply.txt') as rookPriceMultiplyFile:
    rookPriceMultiply=json.load(rookPriceMultiplyFile)
with open('rookLevel.txt') as rookLevelFile:
    rookLevel=json.load(rookLevelFile)
with open('rookPrice.txt') as rookPriceFile:
    rookPrice=json.load(rookPriceFile)
with open('pawnPriceMultiply.txt') as pawnPriceMultiplyFile:
    pawnPriceMultiply=json.load(pawnPriceMultiplyFile)
with open('pawnLevel.txt') as pawnLevelFile:
    pawnLevel=json.load(pawnLevelFile)
with open('pawnPrice.txt') as pawnPriceFile:
    pawnPrice=json.load(pawnPriceFile)
with open('multiply.txt') as multiplyFile:
    multiply=json.load(multiplyFile)
with open('bishopLevel.txt') as bishopLevelFile:
    bishopLevel=json.load(bishopLevelFile)
with open('bishopPriceMultiply.txt') as bishopPriceMultiplyFile:
    bishopPriceMultiply=json.load(bishopPriceMultiplyFile)
with open('bishopPrice.txt') as bishopPriceFile:
    bishopPrice=json.load(bishopPriceFile)
with open('knightPrice.txt') as knightPriceFile:
    knightPrice=json.load(knightPriceFile)
with open('knightLevel.txt') as knightLevelFile:
    knightLevel=json.load(knightLevelFile)
with open('knightPriceMultiply.txt') as knightPriceMultiplyFile:
    knightPriceMultiply=json.load(knightPriceMultiplyFile)
with open('pawnPriceMultiply.txt') as pawnPriceMultiplyFile:
    pawnPriceMultiply=json.load(pawnPriceMultiplyFile)

def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('czcionka.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
def waitFor(waitTime): 
    screenCopy = screen.copy()
    waitCount = 0
    while waitCount < waitTime:
        dt = clock.tick(60) 
        waitCount += dt
        pygame.event.pump()
        screen.blit(screenCopy, (0,0))
        pygame.display.flip()

def AutoChecks():
    global check
    global autoC
    clock.tick(60)
    time.sleep(0.1)
    check=check+autoC

def main_loop():
    global autoCmultiply
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
    global bishopLevel
    global bishopPriceMultiply
    global bishopPrice
    global knightPrice
    global knightLevel
    global knightPriceMultiply
    global screenCopy


    while running:
        if running:
            pygame.display.update()
            AutoChecks()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('score.txt','w') as scoreFile:
                    json.dump(check,scoreFile)
            if event.type == pygame.QUIT:
                with open('autoCmultiply.txt','w') as autoCmultiplyFile:
                    json.dump(autoCmultiply,autoCmultiplyFile)
            if event.type == pygame.QUIT:
                with open('autoC.txt','w') as autoCFile:
                    json.dump(autoC,autoCFile)
            if event.type == pygame.QUIT:
                with open('rookPriceMultiply.txt','w') as rookPriceMultiplyFile:
                    json.dump(rookPriceMultiply,rookPriceMultiplyFile)
            if event.type == pygame.QUIT:
                with open('rookLevel.txt','w') as rookLevelFile:
                    json.dump(rookLevel,rookLevelFile)
            if event.type == pygame.QUIT:
                with open('rookPrice.txt','w') as rookPriceFile:
                    json.dump(rookPrice,rookPriceFile)
            if event.type == pygame.QUIT:
                with open('pawnPriceMultiply.txt','w') as pawnPriceMultiplyFile:
                    json.dump(pawnPriceMultiply,pawnPriceMultiplyFile)
            if event.type == pygame.QUIT:
                with open('pawnLevel.txt','w') as pawnLevelFile:
                    json.dump(pawnLevel,pawnLevelFile)
            if event.type == pygame.QUIT:
                with open('pawnPrice.txt','w') as pawnPriceFile:
                    json.dump(pawnPrice,pawnPriceFile)
            if event.type == pygame.QUIT:
                with open('multiply.txt','w') as multiplyFile:
                    json.dump(multiply,multiplyFile)
            if event.type == pygame.QUIT:
                with open('bishopLevel.txt','w') as bishopLevelFile:
                    json.dump(bishopLevel,bishopLevelFile)
            if event.type == pygame.QUIT:
                with open('bishopPriceMultiply.txt','w') as bishopPriceMultiplyFile:
                    json.dump(bishopPriceMultiply,bishopPriceMultiplyFile)
            if event.type == pygame.QUIT:
                with open('bishopPrice.txt','w') as bishopPriceFile:
                    json.dump(bishopPrice,bishopPriceFile)
            if event.type == pygame.QUIT:
                with open('knightPrice.txt','w') as knightPriceFile:
                    json.dump(knightPrice,knightPriceFile)
            if event.type == pygame.QUIT:
                with open('knightLevel.txt','w') as knightLevelFile:
                    json.dump(knightLevel,knightLevelFile)
            if event.type == pygame.QUIT:
                with open('knightPriceMultiply.txt','w') as knightPriceMultiplyFile:
                    json.dump(knightPriceMultiply,knightPriceMultiplyFile)
            if event.type == pygame.QUIT:
                with open('pawnMultiply.txt','w') as pawnMultiplyFile:
                    json.dump(pawnMultiply,pawnMultiplyFile)
                running = False      

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.init
                x, y = event.pos 
                if click.get_rect().collidepoint(x-(X/2 - 200), y-100):
                    pygame.display.update()
                    check=check+multiply

                    screenCopy = screen.copy()
                    screen.blit(clickclick, (x, y-40))
                    waitFor(100)
                    screen.blit(screenCopy, (0,0))


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
                            pawnMultiply=pawnMultiply+2


                if rook.get_rect().collidepoint(x-50,y-500):
                    if check>=rookPrice:
                        rookLevel=rookLevel+1
                        check=check-rookPrice
                        autoC=autoC+(0.3 * autoCmultiply)
                        if rookLevel%3==0:
                            rookPriceMultiply=rookPriceMultiply+0.1
                        rookPrice=rookPrice*rookPriceMultiply
                        if rookLevel%10==0 and rookLevel!=0:
                            autoC=autoC*2
                            autoCmultiply=autoCmultiply*2                 
                if bishop.get_rect().collidepoint(x-50,y-600):
                    if check>=bishopPrice:
                        bishopLevel=bishopLevel+1
                        check=check-bishopPrice
                        autoC=autoC+(1 * autoCmultiply)
                        if bishopLevel%3==0:
                            bishopPriceMultiply=bishopPriceMultiply+0.22
                        bishopPrice=bishopPrice*bishopPriceMultiply
                        if bishopLevel%10==0 and bishopLevel!=0:
                            autoC=autoC*2.5
                            autoCmultiply=autoCmultiply*2.5
                if knight.get_rect().collidepoint(x-50,y-700):
                    if check>=knightPrice:
                        knightLevel=knightLevel+1
                        check=check-knightPrice
                        autoC=autoC*2
                        multiply=multiply*2
                        autoCmultiply=autoCmultiply*2
                        pawnMultiply=pawnMultiply*2
                        if knightLevel%2==0:
                            knightPriceMultiply=knightPriceMultiply+0.3
                        knightPrice=knightPrice*knightPriceMultiply
                if reset.get_rect().collidepoint(x-700,y-700):
                    multiply=1
                    pawnPrice = 20
                    pawnLevel= 0
                    pawnPriceMultiply = 1.3
                    rookPrice=200
                    rookLevel = 0
                    rookPriceMultiply=1.5
                    autoC = 0
                    autoCmultiply = 1
                    pawnMultiply = 1
                    bishopPrice = 800
                    bishopLevel = 0
                    bishopPriceMultiply = 1.8
                    knightPrice = 2200
                    knightLevel = 0
                    knightPriceMultiply = 3
                    check=0
                    
                 
    
                

        DrawText("   You made " + str(f'{check:.2f}') + " checks   ", black, white, X/2-100, 50, 20)
        DrawText("Buy pawn for  " + str(f'{pawnPrice:.2f}') + " checks(+1 to click power, *3 every 10lvl)", black,backgroundColour, 330 , 420, 13)
        DrawText("You have " + str(f'{pawnLevel:.2f}') + " pawns", black,backgroundColour, 330 , 440, 13)
        DrawText("Buy rook for  " + str(f'{rookPrice:.2f}') + " checks(3check/sec, *2 every 10lvl)", black,backgroundColour, 330 , 520, 13)
        DrawText("You have " + str(f'{rookLevel:.2f}') + " rooks", black,backgroundColour, 330 , 540, 13)
        DrawText("Buy bishop for  " + str(f'{bishopPrice:.2f}') + " checks(10checks/sec, *2.5 every 10lvl)", black,backgroundColour, 330 , 620, 13)
        DrawText("You have " + str(f'{bishopLevel:.2f}') + " bishops", black,backgroundColour, 330 , 640, 13)
        DrawText("Buy knight for  " + str(f'{knightPrice:.2f}') + " checks(*2 click power, *2checks/sec)", black,backgroundColour, 330 , 720, 13)
        DrawText("You have " + str(f'{knightLevel:.2f}') + " knights", black,backgroundColour, 330 , 740, 13)       
        DrawText("You have " + str(f'{multiply:.2f}') + " click power", black,backgroundColour, 660 , 50, 16)
        DrawText("You have " + str(f'{autoC*10:.2f}') + " checks per second", black,backgroundColour, 660 , 80, 16)
        


        pygame.display.update()

main_loop()
pygame.quit()
quit()


