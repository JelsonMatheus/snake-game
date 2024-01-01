from p5 import *
from game import GameManager, GameController, GameIntro


manager = GameManager()


def setup():
    manager.setup()
    title('Snake Game')
    manager.set_screen(GameIntro(manager))
    

def draw():
    manager.draw()


def key_pressed():
    manager.key_pressed()


if __name__ == '__main__':
    run(renderer='skia')

