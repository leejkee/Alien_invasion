class Settings():

    def __init__(self):

        # the property of screen
        self.screen_width = 1080
        self.screen_height = 1000
        self.bg_color = (221, 245, 255)

        # the number of ships players start with
        self.ship_limit = 2

        # bullet settings
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = 60,60,60
        self.bullets_allowed = 9

        # the speed at which the aliens are moving downwards, if the aliens reach the edge of screen
        self.fleet_drop_speed = 20

        # 难度递增系数
        self.speedup_scale = 1.05

        # 难度递增后得分也对应递增，递增系数
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # the speed for moving the ship
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 4
        # alien settings
        self.alien_speed_factor = 1

        # fleet_direction = 1 means rigtht, and -1 means left
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)