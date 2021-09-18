import pygame
import os
import game_starting


gameScreen = pygame.display.set_mode((400, 300))
button1 = pygame.Rect(20, 20, 460, 70)
button2 = pygame.Rect(20, 100, 460, 70)


def early_dysplay():
    list_crnt()
    global button1
    global button2
    global gameScreen
    pygame.init()
    pygame.font.init()
    x = 100
    y = 100
    os.environ['Sp_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
    size = [500, 500]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("100 matches")
    gameScreen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 200, 64), button1)
    pygame.draw.rect(screen, (0, 200, 64), button2)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface1 = myfont.render('Играть', False, (0, 0, 0))
    screen.blit(textsurface1, (200, 50))
    textsurface2 = myfont.render('Выйти', False, (0, 0, 0))
    screen.blit(textsurface2, (200, 130))
    textsurface3 = myfont.render('Лидерборд', False, (0, 0, 0))
    screen.blit(textsurface3, (200, 210))
    textsurface4 = myfont.render('Player 1', False, (0, 0, 0))
    screen.blit(textsurface4, (150, 230))
    textsurface5 = myfont.render('Player 2', False, (0, 0, 0))
    screen.blit(textsurface5, (280, 230))
    textsurface4 = myfont.render(str(crnt_player1), False, (0, 0, 0))
    screen.blit(textsurface4, (150, 260))
    textsurface5 = myfont.render(str(crnt_player2), False, (0, 0, 0))
    screen.blit(textsurface5, (280, 260))
    pygame.display.flip()
    pressed()
    runGame = True
    while runGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runGame = False
    pygame.quit()
    def pressed():
    while True:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if button1.collidepoint(mouse_pos):
                    pygame.quit()
                    game_starting.start_game()
                if button2.collidepoint(mouse_pos):
                    pygame.quit()
def list_crnt():
    global crnt_player1
    global crnt_player2
    word = open("leader.txt", 'r').readlines()
    crnt_player1 = 0
    crnt_player2 = 0
    for c in word:
        if c == "a":
            crnt_player1 += 1
        if c == "b":
            crnt_player2 += 1

if __name__ == '__main__':
    early_dysplay()
