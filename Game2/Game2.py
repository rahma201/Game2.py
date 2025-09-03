import pygame
import random
import time
import os

# إعدادات اللعبة
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# ألوان
WHITE = (255, 255, 255)
PINK = (255, 182, 193)
BLACK = (0, 0, 0)
BUTTON_COLOR = (0, 0, 0)
BUTTON_TEXT_COLOR = PINK
SOUL_COLOR = (255, 0, 0)  # لون عداد الأرواح (أحمر)

CURRENTPATH = os.getcwd()

# إعداد pygame
pygame.init()
pygame.mixer.init()  # لتشغيل الأصوات

# إعداد الشاشة
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pikachu Jumps Over Obstacles")
clock = pygame.time.Clock()

# تحميل الأصوات
jump_sound = pygame.mixer.Sound(os.path.join(CURRENTPATH, 'resources/retro-jump.mp3'))
coin_sound = pygame.mixer.Sound(os.path.join(CURRENTPATH, 'resources/coin.mp3'))
hit_sound = pygame.mixer.Sound(os.path.join(CURRENTPATH, 'resources/heavy-cineamtic-hit.mp3'))
game_over_sound = pygame.mixer.Sound(os.path.join(CURRENTPATH, 'resources/game-over.mp3'))  # صوت نهاية اللعبة


# تحميل الخلفيات والصور
background = os.path.join(CURRENTPATH, 'images/imgeback.png')
background_image = pygame.image.load(background)
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

Pikachu = os.path.join(CURRENTPATH, 'images/Pikachu.png')
pikachu_image = pygame.image.load(Pikachu)
pikachu_rect = pikachu_image.get_rect(midbottom=(100, 600))

background_start_page = os.path.join(CURRENTPATH, 'images/backgroudstartpage.jpg')
background_start_image = pygame.image.load(background_start_page)
background_start_image = pygame.transform.scale(background_start_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# تحميل زر البداية
start_button_image = pygame.image.load(os.path.join(CURRENTPATH, 'images/pngtree-new-play-button.png'))
start_button_rect = start_button_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))

# تحميل العوائق
block_path = os.path.join(CURRENTPATH, 'images/block.png')
block_image = pygame.image.load(block_path)
block_image = pygame.transform.scale(block_image, (50, 50))

bird_path = os.path.join(CURRENTPATH, 'images/bird2.png')
bird_image = pygame.image.load(bird_path)
bird_image = pygame.transform.scale(bird_image, (50, 50))

# تحميل العملة الذهبية
coin_path = os.path.join(CURRENTPATH, 'images/coin.png')
coin_image = pygame.image.load(coin_path)
coin_image = pygame.transform.scale(coin_image, (30, 30))

# إعدادات القفز والجاذبية
floor_y = 500
velocity_y = 0
gravity = 1
is_jumping = False

# إعدادات العوائق (بلوكات وعصافير)
obstacles = []
obstacle_timer = 0
OBSTACLE_INTERVAL = 1500
OBSTACLE_SPEED = 5

# إعدادات العملات الذهبية
coins = []
coin_timer = 0
COIN_INTERVAL = 2000
coin_count = 0  # عدد العملات التي جمعها اللاعب

# متغير لتتبع الأرواح
lives = 3

# شاشة البداية
font = pygame.font.SysFont("Arial", 50)
small_font = pygame.font.SysFont("Arial", 30)

# تحميل زر "Play Again"
play_again_button_image = pygame.image.load(os.path.join(CURRENTPATH, 'images/play-again (1).png'))
play_again_button_rect = play_again_button_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))

# شاشة البداية
def show_start_screen():
    screen.blit(background_start_image, (0, 0))  # عرض الخلفية
    screen.blit(start_button_image, start_button_rect)  # عرض زر البداية
    pygame.display.flip()

# شاشة نهاية اللعبة
def show_game_over_screen():
    game_over_image_path = os.path.join(CURRENTPATH, 'images/gameOver.jpg')
    game_over_image = pygame.image.load(game_over_image_path)
    game_over_image = pygame.transform.scale(game_over_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    screen.blit(game_over_image, (0, 0))
    screen.blit(play_again_button_image, play_again_button_rect)  # عرض زر "Play Again"
    pygame.display.flip()

# تشغيل اللعبة
running = True
game_started = False

while running:
    screen.fill(PINK)

    if not game_started:
        show_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    game_started = True
                    pikachu_rect = pikachu_image.get_rect(midbottom=(100, 600))
                    velocity_y = 0
                    is_jumping = False
                    obstacles.clear()
                    coins.clear()
                    obstacle_timer = 0
                    coin_timer = 0
                    lives = 3
                    coin_count = 0
    else:
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and pikachu_rect.bottom >= floor_y:
                    velocity_y = -22
                    is_jumping = True
                    jump_sound.play()  # تشغيل صوت القفز

        # تحديث الجاذبية
        velocity_y += gravity
        pikachu_rect.y += velocity_y

        # التأكد من أن الشخصية لا تسقط أسفل الأرض
        if pikachu_rect.bottom >= floor_y:
            pikachu_rect.bottom = floor_y
            is_jumping = False
            velocity_y = 0

        # توليد العوائق
        obstacle_timer += clock.get_time()
        if obstacle_timer >= OBSTACLE_INTERVAL:
            obstacle_timer = 0
            obstacle_x = SCREEN_WIDTH
            if random.choice([True, False]):
                obstacle_y = floor_y - 50
                obstacles.append(("block", pygame.Rect(obstacle_x, obstacle_y, 50, 50)))
            else:
                obstacle_y = floor_y - 200
                obstacles.append(("bird", pygame.Rect(obstacle_x, obstacle_y, 50, 50)))

        # توليد العملات الذهبية
        coin_timer += clock.get_time()
        if coin_timer >= COIN_INTERVAL:
            coin_timer = 0
            coin_x = SCREEN_WIDTH
            coin_y = random.randint(floor_y - 200, floor_y - 50)
            coins.append(pygame.Rect(coin_x, coin_y, 30, 30))

        # تحريك العملات الذهبية
        for coin in coins[:]:
            coin.x -= OBSTACLE_SPEED
            if coin.right < 0:
                coins.remove(coin)

        # التحقق من جمع العملات الذهبية
        for coin in coins[:]:
            if pikachu_rect.colliderect(coin):
                coins.remove(coin)
                coin_count += 1
                for _ in range(3):
                    coin_sound.play()
                    pygame.time.delay(50)

        # تحريك العوائق
        for obstacle in obstacles[:]:
            obstacle[1].x -= OBSTACLE_SPEED
            if obstacle[1].right < 0:
                obstacles.remove(obstacle)
    
            # التحقق من التصادم بين Pikachu والعوائق
            if pikachu_rect.colliderect(obstacle[1]):
                lives -= 1  # خصم حياة عند التصادم
                hit_sound.play()  # تشغيل صوت التصادم
                obstacles.remove(obstacle)  # إزالة العائق بعد الاصطدام
                if lives == 0:
                    game_over_sound.play()  # تشغيل صوت نهاية اللعبة
                    show_game_over_screen()  # عرض شاشة نهاية اللعبة
                    pygame.display.flip()
                    time.sleep(2)  # الانتظار لبضع ثوانٍ قبل العودة لشاشة البداية
                    game_started = False  # العودة لشاشة البداية
                    break

        # عرض العوائق
        for obstacle in obstacles:
            if obstacle[0] == "block":
                screen.blit(block_image, obstacle[1])
            elif obstacle[0] == "bird":
                screen.blit(bird_image, obstacle[1])

        # عرض العملات الذهبية
        for coin in coins:
            screen.blit(coin_image, coin)

        # عرض الشخصية
        screen.blit(pikachu_image, pikachu_rect)

        # رسم الأرض
        pygame.draw.rect(screen, BLACK, pygame.Rect(0, floor_y, SCREEN_WIDTH, SCREEN_HEIGHT - floor_y))

        # عرض عداد الأرواح
        soul_text = small_font.render(f"Lives: {lives}", True, SOUL_COLOR)
        screen.blit(soul_text, (SCREEN_WIDTH - 150, 20))

        # عرض عداد العملات الذهبية
        coin_text = small_font.render(f"Coins: {coin_count}", True, BLACK)
        screen.blit(coin_text, (SCREEN_WIDTH - 150, 60))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
