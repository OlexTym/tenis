from pygame import Rect
from pygame.draw import ellipse as draw_ellipse


class Ball():
    ball_diameter = 20
    ball_move_x = 4
    ball_move_y = 4

    def __init__(self, screen, color):
        self.screen = screen
        self.color = color
        self.pos_x = self.screen.get_height() / 2
        self.pos_y = self.screen.get_width() / 2
        self.rect = Rect(self.pos_x, self.pos_y, Ball.ball_diameter, Ball.ball_diameter)
        self.move_x = Ball.ball_move_x
        self.move_y = Ball.ball_move_y
        self.ball = draw_ellipse(self.screen, self.color, self.rect)

    def draw_ball(self):
        self.ball = draw_ellipse(self.screen, self.color, self.rect)

    def move_ball(self):

        if self.rect.top > (self.screen.get_height() - self.rect.height) or self.rect.top < 0:
            self.move_y *= -1

        if self.rect.left > (self.screen.get_width() - self.rect.width) or self.rect.left < 0:
            self.move_x = 0
            self.move_y = 0
            print("Game Over")

        self.rect.move_ip(0, self.move_y)
        self.rect.move_ip(self.move_x, 0)
  
    def racket_shoot(self):
        self.move_x *= -1
        self.rect.move_ip(self.move_x * 2, 0)
