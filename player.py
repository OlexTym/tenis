
from icecream import ic
from pygame import Rect
from pygame.draw import rect as draw_rect


class Player(Rect):

    def __init__(self, screen, color, pos_x, pos_y, size_x, size_y, move_step):
        self.screen = screen
        self.color = color
        self.rect = Rect(pos_x, pos_y, size_x, size_y)
        self.move_step = move_step
        self.racket = draw_rect(self.screen, self.color, self.rect)

    def draw_racket(self):
        self.racket = draw_rect(self.screen, self.color, self.rect)

    def move_down(self):
        ic()
        if (self.rect.top < self.screen.get_height() - self.rect.height):
            self.rect.move_ip(0, self.move_step)

    def move_up(self):
        ic()
        if (self.rect.top > 0):
            self.rect.move_ip(0, -self.move_step)