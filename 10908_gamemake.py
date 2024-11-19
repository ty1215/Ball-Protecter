import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH = 800
HEIGHT = 600
display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ball Protecter")
clock = pygame.time.Clock()

def main() :

    #게임 진행
    run = True

    #점수
    point = 0
    
    #색 바꾸기
    col_arr = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    col = 0

    #공
    ball_pos = [400,600-50]
    ball_speed = [5, -5] #[x, y], 둘이 동시에 작동하면 대각선으로 움직임
    ball_size = 10 #반지름

    #바
    bar_pos = [350,600-10-20]
    bar_width = 100
    bar_height = 10

    while run :
        clock.tick(60)
        display.fill((0,0,0))

        #bar 그리기
        rect = pygame.Rect(bar_pos[0],bar_pos[1], bar_width, bar_height)
        pygame.draw.rect(display, col_arr[col % 3], rect)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
            if event.type == pygame.KEYDOWN : #키누를때 마다 색깔 변경
                col += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and bar_pos[0] <= WIDTH-bar_width : #오른쪽 이동, 
            bar_pos[0] += 7
        elif keys[pygame.K_LEFT] and bar_pos[0] >= 0 : #왼쪽 이동
            bar_pos[0] -= 7
                          
        #공 움직이기
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        #벽에 닿으면 튕기기
        if ball_pos[0] >= WIDTH :
            ball_speed[0] *= -1
        if ball_pos[0] <= 0 :
            ball_speed[0] *= -1
        if ball_pos[1] <= 10 : 
            ball_speed[1] *= -1

        #bar와 공의 충돌
        ball_rect = pygame.Rect(int(ball_pos[0] - ball_size), int(ball_pos[1] - ball_size), ball_size * 2, ball_size * 2)
        if ball_rect.colliderect(bar_pos[0],bar_pos[1], bar_width, bar_height) :
            ball_speed[1] *= -1

        #공이 화면 밖으로 나갈때
        if ball_pos[1] > HEIGHT :
            run = False
            
        #점수 증가
        point += 1

        #점수 표시
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(str(point), True, (255, 255, 255))
        display.blit(score_text, (100, 100))

        #난이도 증가(일정 포인트당 바의 크기가 줄거나 공의 속도가 증가)
        if point == 1000 :
            bar_width = 80

        if point == 1500 :
            bar_width = 60
            ball_speed[0] *= 1.1
            ball_speed[1] *= 1.1 #공 속도 : 5.5

        if point == 2500 :
            bar_width = 40

        if point == 3500 :
            ball_speed[0] *= 1.1
            ball_speed[1] *= 1.1 #공 속도 : 6.05

        if point == 4500 :
            bar_width = 20

        if point == 5000 :
            run = False

        #ball 그리기
        pygame.draw.circle(display, (255, 0, 0), (int(ball_pos[0]), int(ball_pos[1])), ball_size)
        #화면 업데이트
        pygame.display.update()
        
#게임 종료
if __name__ == "__main__" :
    main()
    pygame.quit()
    sys.exit()
