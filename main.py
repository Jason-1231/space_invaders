from turtle import *
from alien import Alien
from ship import Ship, Bullet
import time


screen = Screen()
screen.setup(450, 600)
tracer(0)

alien_x = -150
alien_y = 280
alien_y2 = alien_y - 30
alien_y3 = alien_y2 - 30
aliens = []

RIGHT_WALL = 199
LEFT_WALL = -210
TOP_WALL = 295
SLEEP_TIME = 0.001
BULLET_SPEED = 15

ship = Ship()
bullet = Bullet(ship.xcor(), ship.ycor())


def manual_shoot():
    bullet.setpos(ship.xcor(), ship.ycor())
    bullet.showturtle()
    global shooting
    shooting = True


# alien setups
for i in range(24):
    if i in range(8):
        alien = Alien()
        alien.num = i
        alien.shape('triangle')
        alien.setpos(alien_x, alien_y)
        alien_x += 40
        aliens.append(alien)
    elif i in range(8, 16):
        alien = Alien()
        alien.num = i
        alien.shape('circle')
        alien.color('orange')
        alien_x -= 40
        alien.setpos(alien_x, alien_y2)
        aliens.append(alien)
    elif i in range(16, 24):
        alien = Alien()
        alien.num = i
        alien.shape('turtle')
        alien.color('green')
        alien.setpos(alien_x, alien_y3)
        alien_x += 40
        aliens.append(alien)

screen.listen()
screen.onkey(ship.move_left, 'Left')
screen.onkey(ship.move_right, 'Right')
screen.onkey(manual_shoot, 'space')

game_on = True
shooting = False
move_direction = 'right'
aliens_left = 24

while game_on:
    # moving right
    if move_direction == 'right':
        for alien in aliens:
            alien.move_right()
            screen.update()
        time.sleep(SLEEP_TIME)

    # moving left
    elif move_direction == 'left':
        for alien in aliens:
            alien.move_left()
            screen.update()
        time.sleep(SLEEP_TIME)

    # detect wall collisions
    if aliens[7].xcor() > RIGHT_WALL or aliens[8].xcor() > RIGHT_WALL or aliens[23].xcor() > RIGHT_WALL:
        # print(f"alien_7: x = {aliens[7].xcor()}")
        # print(f"alien_8: x = {aliens[8].xcor()}")
        # print(f"alien_23: x = {aliens[23].xcor()}")
        for alien in aliens[::-1]:
            alien.move_down()
            screen.update()
        time.sleep(SLEEP_TIME)
        move_direction = 'left'

    elif aliens[0].xcor() < LEFT_WALL or aliens[15].xcor() < LEFT_WALL or aliens[16].xcor() < LEFT_WALL:
        # print(f"alien_0: x = {aliens[0].xcor()}")
        # print(f"alien_15: x = {aliens[15].xcor()}")
        # print(f"alien_16: x = {aliens[16].xcor()}")
        for alien in aliens[::-1]:
            alien.move_down()
            screen.update()
        time.sleep(SLEEP_TIME)
        move_direction = 'right'

    if shooting:
        bullet.forward(BULLET_SPEED)

    for alien in aliens[::-1]:
        if alien.distance(bullet) < 10:
            shooting = False
            alien.hideturtle()
            old_x = alien.xcor()
            new_y = 500
            alien.setpos(old_x, new_y)
            bullet.hideturtle()
            bullet.setpos(500, 0)
            aliens_left -= 1
            print(aliens_left)


    # alien reaches bottom
    for alien in aliens[::-1]:
        if alien.ycor() < -240:
            screen.update()
            print('alien wins')
            game_on = False
            board = Turtle()
            board.hideturtle()
            board.write('Alien wins', align='center', font=('Arial', 30, 'bold'))
            break

    # All aliens shot
    if aliens_left == 0:
        board = Turtle()
        board.hideturtle()
        board.write('You Win!!', align='center', font=('Arial', 30, 'bold'))
        game_on = False

screen.exitonclick()
