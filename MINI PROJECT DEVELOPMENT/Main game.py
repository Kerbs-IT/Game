import pygame
from pygame.locals import*


pygame.init()

screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
clicked = False
counter = 0
pygame.display.set_caption('Buttons')
font = pygame.font.SysFont('Pixel_font.TFF', 40)

class button():

    but_col = (200,200,200)
    hover_col = (255,255,255)
    clicked_col = (180,180,180)
    text_col = (0,0,0)
    width = 180
    heigth = 40

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
    def draw_button(self):
        global clicked
        action = False

        pos = pygame.mouse.get_pos()

        button_rect = Rect(self.x,self.y,self.width, self.heigth)

        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                print('clicked')
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.clicked_col, button_rect)
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width/2) - int(text_len / 2), self.y + 5))
        return action
play = button(300 ,300, 'PLAY')

run = True
while run:
    screen.fill((255, 255, 255))
    play.draw_button()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()