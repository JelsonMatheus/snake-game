from p5 import *
from snake import Snake, Food
from enum import Enum


class GameState(Enum):
    RUNNING = 1
    GAME_OVER = 2
    VICTORY = 3


class GameManager:

    def __init__(self):
        self.current_screen = None
    
    def setup(self):
        size(500, 500)

    def set_screen(self, screen):
        loop()
        self.current_screen = screen
        self.current_screen.setup()

    def draw(self):
        if self.current_screen:
            self.current_screen.draw()

    def key_pressed(self):
        if self.current_screen:
            self.current_screen.key_pressed()


class GameIntro:

    def __init__(self, game_manager):
        self.game_manager = game_manager

    def setup(self):
        pass

    def draw(self):
        background(51)
        self.display_title()
        self.display_instruction()

    def display_title(self):
        fill(0,255,0)
        text_font(load_font('fonts/Snake Chan.ttf'))
        text_size(32)
        text_align(CENTER, CENTER)
        text("Snake Game!", width / 2, height / 2.5)

    def display_instruction(self):
        fill(82,127,118)
        text_size(12)
        text_align(CENTER, CENTER)
        text("Press ENTER to start", width / 2, height / 2)

    def key_pressed(self):
        if key == 'ENTER':
            self.game_manager.set_screen(GameController(self.game_manager))


class GameController:

    def __init__(self, game_manager):
        self.cell = 20
        self.score_height = self.cell * 2
        self.player = Snake(self.cell, self.score_height)
        self.game_manager = game_manager
    
    def setup(self):
        self.state = GameState.RUNNING
        set_frame_rate(10)
        self.food = Food(self.cell, self.score_height)
        self.font_snake = load_font('fonts/Snake Chan.ttf')
    
    def draw(self):
        background(51)
        self._run()
        self._display()

    def key_pressed(self):
        if self.state == GameState.RUNNING:
            self.player.key_pressed()

    def _run(self):
        if self.state == GameState.RUNNING:
            self.player.update()
            self._check_gameover()
            self.player.eat(self.food)
        if self.state == GameState.GAME_OVER:
            no_loop()
            time.sleep(1)
            self.game_manager.set_screen(GameIntro(self.game_manager))

    def _display(self):
        self._show_grid()
        self.food.draw()
        self.player.show()
        self._show_score()
    
    def _check_gameover(self):
        if self.player.death():
            self.state = GameState.GAME_OVER
    
    def _show_score(self):
        fill(75)
        rect(0, 0, width, self.cell*2)
        text_style(NORMAL)
        text_font(self.font_snake)
        text_size(14)
        fill(0,255,0)
        text_align(LEFT, CENTER)
        text("Snake Game!", 10, 30)
        fill(0)
        text_align(CENTER, CENTER)
        msg = 'Score: '+ str(self.player.total).ljust(3)
        text(msg, width/2, 30)

    def _show_grid(self):
        temp = stroke(40)
        for x in range(0, width, self.cell):
            line(x, 0, x, height)
        for y in range(0, height, self.cell):
            line(0, y, width, y)
        stroke(0)
        