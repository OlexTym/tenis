from colors import Colors
import pygame
from datetime import datetime
from icecream import ic


# Icecream
def time_format():
    return f'{datetime.now()}|> '


ic.configureOutput(prefix=time_format)

pygame.init()

# Screen
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
# Windows title
pygame.display.set_caption("Tennis v1")

# Play will be active if playactive = true
play_active = True

# Update window
fps = 60
clock = pygame.time.Clock()


class Ball():

    def __init__(self, screen, color, pos_x, pos_y, size, move_x, move_y):
        self.screen = screen
        self.color = color
        self.rect = pygame.Rect(pos_x, pos_y, size, size)
        self.move_x = move_x
        self.move_y = move_y
        self.ball = pygame.draw.ellipse(self.screen, self.color, self.rect)

    def draw_ball(self):
        self.ball = pygame.draw.ellipse(self.screen, self.color, self.rect)

    def move_ball(self):

        if self.rect.top > (screen.get_height() - self.rect.height) or self.rect.top < 0:
            self.move_y *= -1

        if self.rect.left > (screen.get_width() - self.rect.width) or self.rect.left < 0:
            self.move_x *= -1

        self.rect.move_ip(0, self.move_y)
        self.rect.move_ip(self.move_x, 0)   
  
    def racket_shoot(self):
        self.move_x *= -1
        self.rect.move_ip(self.move_x * 2, 0)


class Player(pygame.Rect):

    def __init__(self, screen, color, pos_x, pos_y, size_x, size_y, move_step):
        self.screen = screen
        self.color = color
        self.rect = pygame.Rect(pos_x, pos_y, size_x, size_y)
        self.move_step = move_step
        self.racket = pygame.draw.rect(self.screen, self.color, self.rect)

    def draw_racket(self):
        self.racket = pygame.draw.rect(self.screen, self.color, self.rect)

    def move_down(self):
        ic()
        if (self.rect.top < self.screen.get_height() - self.rect.height):
            self.rect.move_ip(0, self.move_step)

    def move_up(self):
        ic()
        if (self.rect.top > 0):
            self.rect.move_ip(0, -self.move_step)


# Define ball
BALL_DIAMETER = 20

ball_position_x = 10
ball_position_y = 20

ball_move_x = 4
ball_move_y = 4

ball = Ball(screen, Colors.WHITE, ball_position_x, ball_position_y,
            BALL_DIAMETER, ball_move_x, ball_move_y)
ball.draw_ball()

# Define pleyer 1
player_one_x = 20
player_one_y = 20

player_one_size_x = 20
player_one_size_y = 100

player_one_speed = 6

player_one_up = False
player_one_down = False

player_one = Player(screen, Colors.WHITE, player_one_x, player_one_y,
                    player_one_size_x, player_one_size_y, player_one_speed)

# Define pleyer 2
player_two_x = screen.get_width() - 40
player_two_y = 20

player_two_size_x = 20
player_two_size_y = 100

player_two_speed = 10

player_two_up = False
player_two_down = False

player_two = Player(screen, Colors.WHITE, player_two_x, player_two_y,
                    player_two_size_x, player_two_size_y, player_two_speed)                    

# Main cycle
while(play_active):

    # Check event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play_active = False
        # Key pressed
        elif event.type == pygame.KEYDOWN:

            # Player one
            if event.key == pygame.K_w:
                ic("Player one")
                player_one_up = True
            elif event.key == pygame.K_s:
                ic("Player one")
                player_one_down = True
            # Player two
            elif event.key == pygame.K_UP:
                ic("Player two")
                player_two_up = True
            elif event.key == pygame.K_DOWN:
                ic("Player two")
                player_two_down = True

        # Key reliase
        elif event.type == pygame.KEYUP:
            # Player one
            if event.key == pygame.K_w:
                ic("Player one")
                player_one_up = False
            elif event.key == pygame.K_s:
                ic("Player one")
                player_one_down = False
            elif event.key == pygame.K_UP:
                ic("Player two")
                player_two_up = False
            elif event.key == pygame.K_DOWN:
                ic("Player two")
                player_two_down = False

    # Refresh play window (delete all)
    screen.fill(Colors.BLACK)

    # Ball
    ball.draw_ball()
    ball.move_ball()

    # Player
    player_one.draw_racket()
    player_two.draw_racket()

    if player_one_up:
        player_one.move_up()
    if player_one_down:
        player_one.move_down()

    if player_two_up:
        player_two.move_up()
    if player_two_down:
        player_two.move_down()

    if player_one.racket.colliderect(ball.ball):
        ic("Shoot one")
        ball.racket_shoot()

    if player_two.racket.colliderect(ball.ball):
        ic("Shoot two")
        ball.racket_shoot()
    # Update window
    pygame.display.flip()

    # Update-time
    clock.tick(fps)

pygame.quit()
