
import random 
import pygame
import os
import time

pygame.mixer.init()

pygame.init() 
screen_width,screen_height=500,500  
gamewindow=pygame.display.set_mode((500,500))   
pygame.display.set_caption("Game") 
white=(255,255,255)   
red=(255,0,0)
black=(0,0,0)
pygame.display.update() 

def images(path,size,position):  
    img=pygame.image.load(path)    
    img=pygame.transform.scale(img,size) 
    gamewindow.blit(img,(position))   

list=["apple1.png","banana-.webp","mango1.png","pearr.png","orange1.png","pine.png","grapes.png","pome.png"] 
clock=pygame.time.Clock()

def text_screen(text,color,x,y,size): 
    font=pygame.font.SysFont(None,size) 
    screen_text=font.render(text,True,color) 
    gamewindow.blit(screen_text,[x,y])  

def plot_snake(gamewindow,color,snake_list,snake_size): 
    for x,y in snake_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size]) 
pygame.display.update() 

def window(): 
    music('start.mp3')
    exit_game=False   
    while not exit_game:  
        images("snake1.jpg",(screen_width,screen_height),(0,0)) 
        mouse=pygame.mouse.get_pos() 
        if screen_width/3-20 <= mouse[0] <= screen_width/2+66 and screen_height-60 <= mouse[1] <= screen_height-20:
            images("button2.png",(170,40),(screen_width/3-20,screen_height-60)) 
            text_screen("PLAY",white,screen_width/3+35,screen_height-50,35)  

        else:   
            images("button1.png",(170,40),(screen_width/3-20,screen_height-60))  
            text_screen("PLAY",black,screen_width/3+35,screen_height-50,35)  

        for event in pygame.event.get():  
            if event.type==pygame.QUIT:  
                exit_game=True                              
            if event.type==pygame.MOUSEBUTTONDOWN: 
                if screen_width/3 <= mouse[0] <= screen_width/2+150 and screen_height-60 <= mouse[1] <= screen_height-20: 
                    gameloop()  
        pygame.display.update()   
        clock.tick(60)  

def music(path): 
    pygame.mixer.music.load(path) 
    pygame.mixer.music.play(-1)  

def gameloop():  
    q=random.choice(list)   
    music('back.mp3')   
    exit_game=False 
    game_over=False  

    snake_list=[]
    snk_length=1 

    if (not os.path.exists("highscore.txt")): 
        f=open("highscore.txt","w")   
        f.write("0")  
        f.close()       
    f=open("highscore.txt","r")    
    highscore=f.read()    
    f.close() 

    snake_x,snake_y=45,45  
    snake_size=15 
    score,fps=0,30  
    velocity_x,velocity_y=0,0 

    x,y=random.randint(20,screen_width/2),random.randint(20,screen_height/2)  
    while not exit_game: 
        
        if game_over: 
            images("end.png",(screen_width,screen_height),(0,0))  
            text_screen("GAME OVER !", red,130,screen_height/3,60)  
            text_screen(f"------ Score:   {score} ------","#0a3808",140,280,40)   
            text_screen(f"High score: {highscore}","#360517",180,340,30)      
            mouse=pygame.mouse.get_pos()     
            if screen_width/3-80 <= mouse[0] <= screen_width/2+6 and screen_height-60 <= mouse[1] <= screen_height-20:  
                images("button2.png",(170,40),(screen_width/3-80,screen_height-60))   
                text_screen("TRY AGAIN",white,screen_width/3-50,screen_height-45,30)   

            else:
                images("button1.png",(170,40),(screen_width/3-80,screen_height-60))  
                text_screen("TRY AGAIN",black,screen_width/3-50,screen_height-45,30)   

            if screen_width/3+100 <= mouse[0] <= screen_width/3+270 and screen_height-60 <= mouse[1] <= screen_height-20: 
                images("red_button1.png",(170,40),(screen_width/3+100,screen_height-60))   
                text_screen("EXIT",white,screen_width/3+155,screen_height-45,30)

            else:  
                images("red_button.png",(170,40),(screen_width/3+100,screen_height-60))
                text_screen("EXIT",black,screen_width/3+155,screen_height-45,30) 


            for event in pygame.event.get():   
                if event.type ==pygame.QUIT:
                    exit_game=True   
                if event.type==pygame.MOUSEBUTTONDOWN: 
                    if screen_width/3-80 <= mouse[0] <= screen_width/3+120 and screen_height-60 <= mouse[1] <= screen_height-20:   
                        gameloop()   
                if event.type==pygame.MOUSEBUTTONDOWN:  
                    if screen_width/3+100 <= mouse[0] <= screen_width/3+270 and screen_height-60 <= mouse[1] <= screen_height-20: 
                        exit_game=True   

        else:   
            for event in pygame.event.get():   
                if event.type ==pygame.QUIT:
                    exit_game=True 
                if event.type==pygame.KEYDOWN:  
                    if event.key==pygame.K_RIGHT:  
                        velocity_x=5     
                        velocity_y=0    

                    elif event.key==pygame.K_LEFT:  
                        velocity_x=-5
                        velocity_y=0

                    elif event.key==pygame.K_DOWN: 
                        velocity_y=5
                        velocity_x=0

                    elif event.key==pygame.K_UP: 
                        velocity_y=-5          
                        velocity_x=0

            snake_x=snake_x+velocity_x   
            snake_y=snake_y+velocity_y 
      
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:  
                game_over=True     
                music("end_game.mp3")  
            
            if abs(snake_x-x)<15 and abs(snake_y-y)<15:  
                score+=10  
                x,y=random.randint(20,screen_width/2),random.randint(20,screen_height/2) 
                a=[x,y] 
                for i in snake_list:  
                    if abs(a[0]-i[0])<20 and abs(a[1]-i[1])<20:    
                        x,y=random.randint(20,screen_width/2),random.randint(20,screen_height/2)   
                q=random.choice(list) 
                snk_length+=5  
                if score>int(highscore):  
                    highscore=score   
                    f=open("highscore.txt","w")  
                    f.write(f"{score}")  
                    f.close() 
                music("food.mp3") 
                time.sleep(0.1)   
                music('back.mp3')  

           
            images("snake.jpg",(screen_width,screen_height),(0,0))  
            text_screen("Score: "+str(score)+"    Highscore: "+str(highscore),black,5,5,30)  

            head=[]  
            head.append(snake_x)  
            head.append(snake_y)   
            snake_list.append(head) 
            if len(snake_list)>snk_length:   
                del snake_list[0]           

            if head in snake_list[:-1]:  
                game_over=True  
                music("end_game.mp3") 
            plot_snake(gamewindow,black,snake_list,snake_size) 
            images(q,(20,20),(x,y)) 

        pygame.display.update()   
        clock.tick(fps)  
        
    pygame.quit()  
    quit()


window()