# 测试文件
import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
cl = pygame.time.Clock()
print(pygame.QUIT)

while True:
    cl.tick(30)
    pygame.display.update()
    for event in pygame.event.get():
        print(event.type)


pygame.quit()