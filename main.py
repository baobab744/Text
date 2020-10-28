import pygame

W = 800
H = 600
RED = (255, 0, 0)
BLUE = (0, 0, 100)
move = 1

pygame.init()
pygame.display.set_caption('Текст')
screen = pygame.display.set_mode((W, H))

font = pygame.font.SysFont('Arial', 40, True, False)
font2 = pygame.font.SysFont('Arial', 20, True, False)
square = pygame.Surface((60, 60))
square_rect = square.get_rect(center=(W // 2, H // 2 - 60))
square.fill(RED)
text = font.render("ВСЕМ ПРИВЕТ", 1, (255, 255, 255))
text2 = font2.render("задание на урок", 1, (255, 255, 0))
text_rect = text.get_rect(center=(W // 2, H // 2 + 30))
text2_rect = text2.get_rect(center=(W // 2, H // 2 + 90))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
    if move == 1:
        square_rect.move_ip(1,0)
        if square_rect > W:
            move = 2
    if move == 2:
        square_rect.move_ip(-1, 0)
        if square_rect < 0:
            move = 1
    screen.fill(BLUE)
    screen.blit(square, square_rect)
    screen.blit(text, text_rect)
    screen.blit(text2, text2_rect)

    pygame.display.update()
