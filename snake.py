import pygame
import random
import time
pygame.init()
#screen size

screen_w=1000
screen_h=1000
screen=pygame.display.set_mode((screen_w,screen_h))
#do not the val in func 


class player:
    def __init__(self,x,y,w,h): 
     self.x=x
     self.y=y
     self.w=w
     self.h=h
     #speedu sopeedu... speeduuu
     self.speed=5
     #val 1 to 5 vara tha 


     self.dx=0
     self.dy=0
     self.dir="RIGHT"
     self.list=[]
     self.l=1
    def chdir(self,user):
        if user=="RIGHT" and self.dir !="LEFT":
            self.dir="RIGHT"
        elif user=="LEFT" and self.dir!="RIGHT":
            self.dir="LEFT"
        elif user=="UP" and self.dir!="DOWN":
            self.dir="UP"
        elif user=="DOWN" and self.dir!="UP":
            self.dir="DOWN"
    def move(self):  #movement ---contoler--
        if self.dir=="UP":
             player.dy=0
             player.dy=player.dy-player.speed
             player.dx=0
    
        elif self.dir=="DOWN":
             player.dy=0
             player.dy=player.dy+player.speed
             player.dx=0
      
        elif self.dir=="RIGHT":
             player.dx=0
             player.dx=player.dx+player.speed
             player.dy=0
      
        elif self.dir=="LEFT":
             player.dx=0
             player.dx=player.dx-player.speed
             player.dy=0  
    def boder(self):
        if self.x>screen_w:
            self.x=0
        elif self.x<0:
            self.x=screen_w
        elif self.y>screen_h:
            self.y=0
        elif self.y<0:
            self.y=screen_h


# do food colr 
            
class Food:
    def __init__(self,size):
        self.x=random.randint(0,screen_w)
        self.y=random.randint(0,screen_h)
        self.size=size
        self.blue=(0,0,225)

# call and val
        
food=Food(25)
player=player(50,50,50,50)
red=(225,0,0)
black=(0,0,0)
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,40)
while True:
   for event in pygame.event.get():
      if event.type==pygame.QUIT:
         pygame.quit()
         exit()
    #kela main code du da aathaulm change sayatha da
   key=pygame.key.get_pressed() # input form keybord
    # game contorl input
   if key[pygame.K_RIGHT] or key[pygame.K_d]: #-->
         player.chdir("RIGHT")
   elif key[pygame.K_LEFT] or key[pygame.K_a]:#<--
         player.chdir("LEFT")
   elif key[pygame.K_UP] or key[pygame.K_w]:#/\
         player.chdir("UP")
   elif key[pygame.K_DOWN] or key[pygame.K_s]:#\/
         player.chdir("DOWN") 
    #game loop
   player.move()
   player.boder()
   player.x=player.x+player.dx
   player.y=player.y+player.dy
   screen.fill(black)
   for x,y in player.list:
          playerbox = pygame.draw.circle(screen,red,(x+7,y+7),30)
          foodbox =pygame.draw.circle(screen,food.blue,(food.x,food.y),food.size)
          if playerbox.colliderect(foodbox):
             food=Food(25)
             
             player.l +=10

   player.list.append([player.x,player.y])

   if len( player.list)> player.l:
       player.list.pop(0)
   if player.list[-1] in player.list[:-1]:
       time.sleep(2)
       player.list.clear()
       player.l=1

    #text output ---> screen and score
   screentextHEAD=font.render("SNAKE GAME IN PYTHON",True,(225,225,225))#HEADING
   screentext=font.render(f"score -{int((player.l-1)/10)}",True,(225,225,225))#SCORE  
   screen.blit(screentext,(screen_h-150,screen_w-100))#POSITION OF SCORE
   screen.blit(screentextHEAD,(400,10))#POSITION OF HEADING 
   pygame.display.update()
   clock.tick(60)