import pygame
from pygame.locals import *
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小和标题
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("乒乓游戏")

# 定义球拍和球的属性
paddle_speed = 5
ball_speed = [2, 2]
paddle_width, paddle_height = 10, 60
ball_width, ball_height = 15, 15

# 创建球拍和球对象
paddle_a = pygame.Rect(20, 200, paddle_width, paddle_height)
paddle_b = pygame.Rect(610, 200, paddle_width, paddle_height)
ball = pygame.Rect(300, 230, ball_width, ball_height)

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # 检测按键
    keys = pygame.key.get_pressed()
    if keys[K_UP] and paddle_b.top > 0:
        paddle_b.top -= paddle_speed
    if keys[K_DOWN] and paddle_b.bottom < 480:
        paddle_b.top += paddle_speed
    if keys[K_w] and paddle_a.top > 0:
        paddle_a.top -= paddle_speed
    if keys[K_s] and paddle_a.bottom < 480:
        paddle_a.top += paddle_speed

    # 更新球的位置
    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    # 碰撞检测
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0 or ball.bottom >= 480:
        ball_speed[1] = -ball_speed[1]

    # 检测得分
    if ball.left <= 0:
        print("玩家B得分!")
        ball.left, ball.top = 300, 230
    if ball.right >= 640:
        print("玩家A得分!")
        ball.left, ball.top = 300, 230

    # 绘制画面
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle_a)
    pygame.draw.rect(screen, (255, 255, 255), paddle_b)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.aaline(screen, (255, 255, 255), (320, 0), (320, 480))

    pygame.display.flip()
    pygame.time.delay(10)
