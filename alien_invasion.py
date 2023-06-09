import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():

    # init game and create a screen obj
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    # title
    pygame.display.set_caption("Alien Invasion")

    # create the button for playing game
    play_button = Button(ai_settings, screen, "Play")
    # create an instance for storing game information
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # ship, bullets, aliens
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # 每次输出当前屏幕上子弹数量
            # print(len(bullets))
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()