import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, screen, ai_settings):
        super().__init__()
        # 初始化飞船并设置其初始位置
        self.screen = screen
        self.ai_settings = ai_settings
        # 获取飞船的外接矩形
        self.image = pygame.image.load('images/ships.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # centerx为飞船中心的x坐标， bottom为飞船下边缘的y坐标
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.moving_left = False
        self.moving_right = False

    # 将飞船画出来
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # 每次根据左右移动的flag更新飞船的位置，限制飞船的位置处于屏幕中
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor 
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor 

        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx
