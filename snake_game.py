#Snake game

import turtle
import pygame
import time
import random
import winsound
import sys

#Main menu

print(30 * "-")
print(9 * "-" + "SNAKE GAME" + 10 * "-")
print(10 * "-" + "MAIN MENU" + 10 * "-")
print(30 * "-")
name=raw_input("Hello, what's your name?: ")
print ("Hi, "+(name)+"!")
while True:
    choice=raw_input("Would you like to play the Snake Game? Enter(Y/N):")    
    if choice in ["Y","y"]:
        print("Starting the game.....")
        time.sleep(1.5)
        break 
    
    if choice in ["N","n"]:
        print("Exiting the program...")
        time.sleep(1.5)
        sys.exit(0)
        
    elif choice not in ["Y", "y","N" ,"n"]:   
        print("Enter a valid sign!")
        time.sleep(1.5)
   
delay=0.1     

#Score
score=0
high_score=0

#Screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)


#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"
head.shapesize(0.75,0.75)


#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.shapesize(0.5,0.5)
food.goto(0,100)


segments=[]


#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, -285)
pen.write("Score: 0  High Score: 0", align="center", font=("Times", 22, "bold"))

#Pen2
pen2=turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()    

#Pen3
pen3=turtle.Turtle()
pen3.speed(0)
pen3.shape("square")
pen3.color("green")
pen3.penup()
pen3.hideturtle()
pen3.goto(0,252)
pen3.write("S. N. A. K. E.  G. A. M. E.", align="center", font=("Helvetica", 27, "bold"))


 
#Drawing pen 
drawpen=turtle.Turtle()
drawpen.speed(0)
drawpen.shape("square")
drawpen.color("green")
drawpen.hideturtle()
drawpen.penup() 
drawpen.goto(-250, -250)
drawpen.pendown()
drawpen.forward(500)
drawpen.left(90)
drawpen.forward(500)
drawpen.left(90)
drawpen.forward(500)
drawpen.left(90)
drawpen.forward(500)
drawpen.left(90)
drawpen.penup() 

#Name
namepen=turtle.Turtle()
namepen.speed(0)
namepen.hideturtle()
namepen.penup()
namepen.color("green")
namepen.shape("square")
namepen.goto(220,-265)
namepen.pendown()
namepen.write(name)
namepen.penup()


 
#Functions

def go_up():
    if head.direction !="down":
        head.direction="up"
    
def go_down():
    if head.direction !="up":
        head.direction="down"
    
def go_left():
    if head.direction !="right":
        head.direction="left"

def go_right():
    if head.direction !="left":
        head.direction="right"    

    
    
def move():
    if head.direction=="up":
        y = head.ycor()
        head.sety(y+20)
        
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
        
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
        
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)


#Keyboard bind
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")
        
        
#Background music
pygame.mixer.init()
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.set_volume(0.68) 
pygame.mixer.music.play(-1,0)        
        

#Main game loop
while True:   
    wn.update()        

    #Music           
    winsound.PlaySound("musici.wav", winsound.SND_ASYNC)    
           
   #Check for collisions with border
    if head.xcor()>245 or head.xcor()<-245 or head.ycor()>245 or head.ycor()<-245:
        pygame.mixer.music.pause()
        pen2.write("Oops!", align="center", font=("Times", 24, "bold"))
        pen2.goto(0,10)        
        winsound.PlaySound("fail_sound.wav", winsound.SND_ASYNC)
        time.sleep(1.5)
        pen2.clear()
        head.goto(0,0)
        head.direction="stop"        
        
        #Hide segments
        for segment in segments:
            segment.goto(1000, 1000)
            
        #Clear segments list
        segments=[]
      
        #Reset the score
        score=0
        
        #Reset delay
        delay=0.1
        
        pen.clear()            
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Times", 24, "bold")) 
        pygame.mixer.music.unpause()
        
    #Collision with food
    if head.distance(food)<20:
        winsound.PlaySound("blip.wav", winsound.SND_ASYNC)
        
        #Move food to random
        x=random.randint(-245,245)
        y=random.randint(-245,245)
        food.goto(x,y)
    
    
        # Adding segments
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.shapesize(0.75,0.75)
        segments.append(new_segment)
                                       
        
        #Add delay
        delay-=0.005
        
        #Score increase
        score+=10
        
        if score>high_score:
            high_score=score
        pen.clear()    
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Times", 24, "bold")) 
        
    
    
    
    #Move segments with snake head
    for index in range(len(segments)-1, 0, -1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
        
    #Move segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
        
 
 
    move()
    
    #Check for collisions with segments
    for segment in segments:
        if segment.distance(head)< 20:
            pygame.mixer.music.pause()
            pen2.write("Oops!", align="center", font=("Times", 24, "bold"))
            pen2.goto(0,10)        
            winsound.PlaySound("fail_sound.wav", winsound.SND_ASYNC)
            time.sleep(1.5)
            pen2.clear()
            head.goto(0,0)
            head.direction="stop"
            
        
            #Hide segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            #Clear segments list
            segments=[]
      
            #Reset the score
            score=0
        
            #Reset delay
            delay=0.1
            
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Times", 24, "bold")) 
            pygame.mixer.music.unpause()
    
    time.sleep(delay)
    





wn.mainloop()








