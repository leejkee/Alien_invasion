import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        # 根据屏幕大小去初始化button
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # size, color, font
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # in center
        self.rect.center = self.screen_rect.center

        self.preg_msg(msg)

    # 将文本处理为图片
    def preg_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, 
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    # 将按钮显示到屏幕上
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)