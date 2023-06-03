import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

# respond the key_down event
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

# respond the key_up event
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

# button event
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, 
    bullets, mouse_x, mouse_y):
    # 鼠标在按钮位置，仅在游戏未开始时点击按钮才会重置游戏
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        # hide the mouse cursor
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        # clear
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()

        # create new
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

# 监测事件并作出对应响应
def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    # keyboard and mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, 
                aliens, bullets, mouse_x, mouse_y)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # 屏幕背景色
    screen.fill(ai_settings.bg_color)
    # 画出子弹群
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 画出飞船
    ship.blitme()
    # 画出坤坤群
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

# create the aliens group
def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

# 获取屏幕一行可以容纳多少个外星人，两边留出空格，每个外星人之间留出空格
def get_number_aliens_x(ai_settings, alien_width):
    avaiable_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaiable_space_x / (2 * alien_width))
    return number_aliens_x

# 按照序号创建对应水平位置的外星人，并加到group
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

# 获取屏幕一共可以容纳多少行外星人，每行之间间隔为外星人的高度
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

# 更新子弹群的位置
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

# 检查子弹和外星人之间的碰撞，处理外星人被消灭殆尽的情形
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
            
    # 外星人数为0，清除全部子弹并生成新的外星人
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


# 玩家按空格键，生成一个子弹
def fire_bullet(ai_settings, screen, ship, bullets):
    # 只允许最多n颗子弹出现在屏幕上
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

# 处理飞船和外星人碰撞的情形
def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    if stats.ships_left > 0:
        # 玩家拥有的飞船数量减一
        stats.ships_left -= 1
        sb.prep_ships()
        # clear the aliens and bullets
        aliens.empty()
        bullets.empty()
        # create a new alien group and init the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

# 更新外星人群的位置
def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 飞船撞到外星人
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
        print("Ship hit!!!")

    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

# 处理外星人到达屏幕低端的情况
def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

# 检查是否有外星人到达屏幕边缘，进行转向处理
def check_fleet_edges(ai_settings, aliens):
     for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)
            break

# 处理外星人到达屏幕边缘的情况，下落并反向水平移动
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_high_score(stats, sb):
    if stats.score >= stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
