import pygame
import random
import time
import os
from Define import *

pygame.init()
screen = pygame.display.set_mode((720,640))
pygame.display.set_caption('Color')
clock = pygame.time.Clock()
times = pygame.USEREVENT
pygame.time.set_timer(times,1000)



# -------------font and text-----------------------

F_TITLE = pygame.font.SysFont('sans', 50)
F_TITLE_2 = pygame.font.SysFont('sans', 40)
F_TEXT = pygame.font.SysFont('sans', 30)
F_TEXT_2 = pygame.font.SysFont('sans', 20)
# paragrap
P_T_C = F_TITLE.render('COLOR!', TRUE, RED)
P_C_L = F_TITLE.render('Choose Level!', TRUE, BLUE)
P_S_S = F_TITLE.render('Save Score?', TRUE, RED)

P_S = F_TITLE_2.render('Start!', TRUE, BLACK)
P_Q = F_TITLE_2.render('Quit!', TRUE, BLACK)
P_Y = F_TITLE_2.render('Yes!', TRUE, BLUE)
P_N = F_TITLE_2.render('No!', TRUE, RED)

P_R_L = F_TEXT.render('Random!', TRUE, BLACK)
P_E = F_TEXT.render('Easy!', TRUE, BLACK)
P_M = F_TEXT.render('Medium!', TRUE, BLACK)
P_H = F_TEXT.render('Hard!', TRUE, BLACK)

P_B = F_TEXT_2.render('Back!', TRUE, BLACK)
P_Q_2 = F_TEXT_2.render('Quit!', TRUE, BLACK)
P_C = F_TEXT_2.render('+', TRUE, BLACK)

# -------------font and text-----------------------
# ------------sound--------------------------------
hit_sound = pygame.mixer.Sound('sfx_hit.mp3')
# ------------sound--------------------------------

with open('Score.txt','r+') as file_score:
    max_score = file_score.read()
file_score.close()




while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        if start:
            screen.fill(BG_C_R)
            pygame.draw.rect(screen, BLACK, (X_TITLE-5,Y_TITLE-5,S_X_TITLE+10,S_Y_TITLE+10) )
            pygame.draw.rect(screen, BG_C_R_2, (X_TITLE,Y_TITLE,S_X_TITLE,S_Y_TITLE) )
            screen.blit(P_T_C,  (X_TITLE+20, Y_TITLE+5))
            pygame.draw.rect(screen, BLACK, (X_S-5,Y_S-5,S_X_S+10,S_Y_S+10) )
            pygame.draw.rect(screen, BLUE, (X_S,Y_S,S_X_S,S_Y_S) )
            screen.blit(P_S,  (X_S+20, Y_S+5))
            pygame.draw.rect(screen, BLACK, (X_Q-5,Y_Q-5,S_X_Q+10,S_Y_Q+10) )
            pygame.draw.rect(screen, RED, (X_Q,Y_Q,S_X_Q,S_Y_Q) )
            screen.blit(P_Q,  (X_Q+20, Y_Q+5))


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (X_S <= mouse_x <= X_S+S_X_S )  and (Y_S <= mouse_y <= Y_S+S_Y_S):
                        start = False
                        choose = True
                    if (X_Q <= mouse_x <= X_Q+S_X_Q )  and (Y_Q <= mouse_y <= Y_Q+S_Y_Q):                   
                        running = False
                            

        if choose:
            screen.fill(BG_C_R)
            pygame.draw.rect(screen, BLACK, (X_TITLE-5,Y_TITLE-5,S_X_TITLE+10,S_Y_TITLE+10) )
            pygame.draw.rect(screen, BG_C_R_2, (X_TITLE,Y_TITLE,S_X_TITLE,S_Y_TITLE) )
            screen.blit(P_C_L,  (X_TITLE+20, Y_TITLE+5))
            pygame.draw.rect(screen, BLACK, (X_R-5,Y_R-5,S_X_R+10,S_Y_R+10) )
            pygame.draw.rect(screen, BG_C_R_3, (X_R,Y_R,S_X_R,S_Y_R) )
            screen.blit(P_R_L,  (X_R+20, Y_R+5))
            pygame.draw.rect(screen, BLACK, (X_E-5,Y_E-5,S_X_E+10,S_Y_E+10) )
            pygame.draw.rect(screen, GREEN, (X_E,Y_E,S_X_E,S_Y_E) )
            screen.blit(P_E,  (X_E+20, Y_E+5))
            pygame.draw.rect(screen, BLACK, (X_M-5,Y_M-5,S_X_M+10,S_Y_M+10) )
            pygame.draw.rect(screen, YELLOW, (X_M,Y_M,S_X_M,S_Y_M) )
            screen.blit(P_M,  (X_M+20, Y_M+5))
            pygame.draw.rect(screen, BLACK, (X_H-5,Y_H-5,S_X_H+10,S_Y_H+10) )
            pygame.draw.rect(screen, RED, (X_H,Y_H,S_X_H,S_Y_H) )
            screen.blit(P_H,  (X_H+20, Y_H+5))
            pygame.draw.rect(screen, BLACK, (X_Q_2-5,Y_Q_2-5,S_X_Q_2+10,S_Y_Q_2+10) )
            pygame.draw.rect(screen, WHITE, (X_Q_2,Y_Q_2,S_X_Q_2,S_Y_Q_2) )
            screen.blit(P_Q_2,  (X_Q_2, Y_Q_2))
            pygame.draw.rect(screen, BLACK, (X_B-5,Y_B-5,S_X_B+10,S_Y_B+10) )
            pygame.draw.rect(screen, WHITE, (X_B,Y_B,S_X_B,S_Y_B) )
            screen.blit(P_B,  (X_B, Y_B))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    hit_sound.play()
                    if (X_R <= mouse_x <= X_R+S_X_R )  and (Y_R <= mouse_y <= Y_R+S_Y_R):
                        timeplay=random.randint(10,50)
                        
                        choose = False
                        create =True
                    if (X_E <= mouse_x <= X_E+S_X_E )  and (Y_E <= mouse_y <= Y_E+S_Y_E):
                        timeplay = 50
                        choose = False
                        create =True
                    if (X_M <= mouse_x <= X_M+S_X_M )  and (Y_M <= mouse_y <= Y_M+S_Y_M):
                        timeplay = 30
                        choose = False
                        create =True
                    if (X_H <= mouse_x <= X_H+S_X_H )  and (Y_H <= mouse_y <= Y_H+S_Y_H):
                        timeplay = 10
                        choose = False
                        create =True
                    if (X_Q_2 <= mouse_x <= X_Q_2+S_X_Q_2 )  and (Y_Q_2 <= mouse_y <= Y_Q_2+S_Y_Q_2):
                        running = False
                    if (X_B <= mouse_x <= X_B+S_X_B)  and (Y_B <= mouse_y <= Y_B+S_Y_B):
                        choose = False
                        start = True

                

        if create:
            
            R_C = WHITE
            P_R_C_X= 495
            P_R_C_Y=220
            keycolor = pygame.K_r
            score=0
            create=False
            play = True
        if play:
            if event.type == times:
                    timeplay -=1
            timing= F_TEXT_2.render("Timing: "+str(timeplay), TRUE, BLACK)
            screen.fill(WHITE)
            pygame.draw.rect(screen, BLACK, (5,5,710,540) ) 
            pygame.draw.rect(screen,GREY, (10,10,700,530) )
            pygame.draw.rect(screen, WHITE, (300,600,100,50) )
            screen.blit(timing, (300,600))
            if timeplay == 0:
                play = False
                save = True
                back = True
            pygame.draw.rect(screen, BLACK, (X_Q_2-5,Y_Q_2-5,S_X_Q_2+10,S_Y_Q_2+10) )
            pygame.draw.rect(screen, WHITE, (X_Q_2,Y_Q_2,S_X_Q_2,S_Y_Q_2) )
            screen.blit(P_Q_2,  (X_Q_2, Y_Q_2))
            pygame.draw.rect(screen, BLACK, (X_B-5,Y_B-5,S_X_B+10,S_Y_B+10) )
            pygame.draw.rect(screen, WHITE, (X_B,Y_B,S_X_B,S_Y_B) )
            screen.blit(P_B,  (X_B, Y_B))
            pygame.draw.rect(screen, R_C, (20,20,680,50) )
            
            count= F_TEXT_2.render("Score: "+str(score), TRUE, BLACK)
            screen.blit(count, (600,600))
            pygame.draw.rect(screen, RED, (45,220,100,100) )
            pygame.draw.rect(screen, ORANGE, (195,220,100,100))
            pygame.draw.rect(screen, YELLOW, (345,220,100,100) )
            pygame.draw.rect(screen, GREEN, (45,370,100,100)) 
            pygame.draw.rect(screen, BLUE, (195,370,100,100) )
            pygame.draw.rect(screen, BLACK, (495,370,100,100) )
            pygame.draw.rect(screen, WHITE, (495,220,100,100) )
            pygame.draw.rect(screen, PURPLE, (345,370,100,100) )
            screen.blit(F_TITLE.render('Q', TRUE, GREY),  (50,225))
            screen.blit(F_TITLE.render('W', TRUE, GREY),  (200,225))
            screen.blit(F_TITLE.render('E', TRUE, GREY),  (350,225))
            screen.blit(F_TITLE.render('R', TRUE, GREY),  (500,225))
            screen.blit(F_TITLE.render('A', TRUE, GREY),  (50,375))
            screen.blit(F_TITLE.render('S', TRUE, GREY),  (200,375))
            screen.blit(F_TITLE.render('D', TRUE, GREY),  (350,375))
            screen.blit(F_TITLE.render('F', TRUE, GREY),  (500,375))


            constan_score= F_TEXT_2.render("Max Score: "+str(max_score), TRUE, BLACK)
            screen.blit(constan_score, (400,600))
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1:
                    hit_sound.play()
                    if (P_R_C_X<= mouse_x <=P_R_C_X+100 )  and (P_R_C_Y <= mouse_y <= P_R_C_Y+100):

                        score += 1
                        randomcolor = True
                    if (X_Q_2 <= mouse_x <= X_Q_2+S_X_Q_2 )  and (Y_Q_2 <= mouse_y <= Y_Q_2+S_Y_Q_2):
                        play= False
                        back = False
                        save = True

                    if (X_B <= mouse_x <= X_B+S_X_B)  and (Y_B <= mouse_y <= Y_B+S_Y_B):

                        play = False
                        back=True
                        save = True
            if event.type == pygame.KEYDOWN:
                hit_sound.play()
                if event.key == keycolor:
                    score += 1
                    randomcolor = True
            if randomcolor:
                R_C1= R_C
                R_C = random.choice([RED,ORANGE,YELLOW,GREEN,BLUE,BLACK,WHITE,PURPLE])
                if R_C == R_C1:
                   R_C = random.choice([RED,ORANGE,YELLOW,GREEN,BLUE,BLACK,WHITE,PURPLE])         
                if R_C == WHITE:
                    P_R_C_X= 495
                    P_R_C_Y=220
                    keycolor = pygame.K_r
                elif R_C == RED:
                    P_R_C_X= 45
                    P_R_C_Y=220
                    keycolor = pygame.K_q
                elif R_C == ORANGE:
                    P_R_C_X= 195
                    P_R_C_Y=220
                    keycolor = pygame.K_w
                elif R_C == YELLOW:
                    P_R_C_X= 345
                    P_R_C_Y=220
                    keycolor = pygame.K_e
                elif R_C == GREEN:
                    P_R_C_X= 45
                    P_R_C_Y=370
                    keycolor = pygame.K_a
                elif R_C == BLUE:
                    P_R_C_X= 195
                    P_R_C_Y=370
                    keycolor = pygame.K_s
                elif R_C == PURPLE:
                    P_R_C_X= 345
                    P_R_C_Y=370
                    keycolor = pygame.K_d
                
                elif R_C == BLACK:
                    P_R_C_X= 445
                    P_R_C_Y=370
                    keycolor = pygame.K_f
                else:
                    pass
                randomcolor = False
            
                    
        if save:
            screen.fill(WHITE)
            pygame.draw.rect(screen, BLACK, (5,5,710,540) ) 
            pygame.draw.rect(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)), (10,10,700,530) )

            pygame.draw.rect(screen, BLACK, (X_TITLE-5,Y_TITLE-5,S_X_TITLE+10,S_Y_TITLE+10) )
            pygame.draw.rect(screen, BG_C_R_2, (X_TITLE,Y_TITLE,S_X_TITLE,S_Y_TITLE) )
            screen.blit(P_S_S,  (X_TITLE, Y_TITLE))
            pygame.draw.rect(screen, BLACK, (X_Y-5,Y_Y-5,S_X_Y+10,S_Y_Y+10) )
            pygame.draw.rect(screen, WHITE, (X_Y,Y_Y,S_X_Y,S_Y_Y) )
            screen.blit(P_Y,  (X_Y, Y_Y))
            pygame.draw.rect(screen, BLACK, (X_N-5,Y_N-5,S_X_N+10,S_Y_N+10) )
            pygame.draw.rect(screen, WHITE, (X_N,Y_N,S_X_N,S_Y_N) )
            screen.blit(P_N,  (X_N, Y_N))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (X_Y <= mouse_x <= X_Y+S_X_Y )  and (Y_Y <= mouse_y <= Y_Y+S_Y_Y):
                        
                        if back:
                            if int(score) > int(max_score):             
                                with open('Score.txt','w') as file_score:
                                    file_score.write(str(score))
                                    file_score.close()
                            save= False
                            choose = True

                        else:
                            running= False
                    if (X_N <= mouse_x <= X_N+S_X_N )  and (Y_N <= mouse_y <= Y_N+S_Y_N):
                        if back:
                            save= False
                            choose = True
                        else:
                            running= False
    




                

                    
                                          
    pygame.display.update()
    clock.tick(60)
pygame.quit()
