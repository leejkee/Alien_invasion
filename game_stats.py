
# 跟踪游戏统计信息的class
class GameStats():

    def __init__(self, ai_settings):
        # init the information
        self.ai_settings = ai_settings
        self.reset_stats()
        self.high_score = 0
        # 游戏状态，初始为true, 飞船全部用完则改为false
        self.game_active = False

    # 初始化在游戏运行期间可能变化的统计信息
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1