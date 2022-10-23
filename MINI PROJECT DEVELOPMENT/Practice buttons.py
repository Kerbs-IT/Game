import pygame,sys


class Button:
    def __init__(self,text, width, height, pos):
        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#7FFFD4'
        # the text
        self.text_surf = font.render(text,True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
    def draw_button(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect)
        screen.blit( self.text_surf, self.text_rect)
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('practice button')
font = pygame.font.Font(None, 30)
run = True
button1 = Button('START',200,40,(290,250))
button2 = Button('EXIT',200,40,(290,320))
while run:
    pos = pygame.mouse.get_pos()
    #if button1.draw_button().collide
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    button1.draw_button()
    button2.draw_button()
    pygame.display.update()

