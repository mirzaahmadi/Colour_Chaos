# getting started - creating screens and drawing objects
import random
import pygame
pygame.init() # this just initializes the module 

screen = pygame.display.set_mode([600, 600]) #pygame.display.set_mode initializes a window or screen for display
pygame.display.set_caption("Ball Bouncer") # this changes the name of the game
red = (255,0,0) #making these colours now just makes them easier to reference later
blue = (0,0,255)
green = (0,255,0)
white = (255, 255, 255)
black = (0,0,0)
orange = (255,165,0)
background = blue

framerate = 60

circle_x = 300 #this and circle_y defines the starting position 
circle_y = 300
circle_x_direction = 3 #changing these two variables will change the speed of ball #3 and 6 are STARTING speed of circle
circle_y_direction = 6

player_width = 30
player_height = 50
player_x = 300 # starting position of player
player_y = 500
player_x_direction = 0
player_y_direction = 0
player_speed = 3

font = pygame.font.Font('freesansbold.ttf', 20) #args = fontface and font size
gameover_font = pygame.font.Font('freesansbold.ttf', 60)
score = 0
previous_score = 0
high_score = 0
timer = pygame.time.Clock() #this creates an object to help track time

gameover = False #this tracks whether or not game over has occured

speed_boost_available = False #this is for a speedboost powerup, that is set to false until a condition (later) is met

speedx = -100 #we want our speed boost to start off off the screen, REMEMBER this is the x coordinate of the speed power up
speedy = -100
last_grabbed = 0 #this tracks what the score was the last time we got speed boost, to check if it is time for another one or not

def speed_boost_check():
    global speed_boost_available
    global score
    global last_grabbed
    global speedx
    global speedy
    global player_speed
    if score - last_grabbed > 10 and not speed_boost_available: #this is saying it has been more than ten points since we have had a speed boost on screen for you, lets give you one
        speed_boost_available = True
        speedx = random.randint(0, 580) #using randint works becuase the coordinates have to be integers    #making both speedx and speed y(which are the x and y coordinates of the power up) places the block anywhere between left edge and right edge of screen
        speedy = random.randint(0,580)
    
    

def check_difficulty():
    global score
    global circle_x_direction
    global circle_y_direction
    x_mod = (score//9) #floor division - rounds down to highest integer
    y_mod = (score // 10)
    if circle_x_direction > 0:
        circle_x_direction = 4 + x_mod #the original speed if four, every time score goes up the speed increases too with addition of xmod
    if circle_x_direction < 0:
        circle_x_direction = -4 - x_mod
    if circle_y_direction > 0:
        circle_y_direction = 5 + y_mod #^^^^ same with y
    if circle_y_direction < 0:
        circle_y_direction = -5 - y_mod
        
def check_collision(playerx, playery, ballx, bally):
    if abs(playerx - ballx) < 44 and abs(playery-bally) < 54: # 55 = 25 + radius of circle #this checks if the x parameters of the ball and player overlap
        global player_x_direction
        global player_y_direction
        global circle_x_direction
        global circle_y_direction
        player_x_direction = 0 #this and the following lines say that if ball and player touch, then stop moving all four of them
        player_y_direction = 0
        circle_x_direction = 0
        circle_y_direction = 0
        game_over() # calls game over 
        
def game_over():
    global gameover #this makes sure the gameover variable can be accessed from anywhere, including this function
    display_game_over = gameover_font.render("Game over dawg", True, red, black) #font.render is a built in pygame tool for putting text on screen once font defined
    screen.blit(display_game_over, (70, 300)) #pygame actually drawing into the screen function #args = coordinates of where the score is displayed
    display_restart = font.render("Press Space to Restart", True, white, black)
    screen.blit(display_restart, (170, 450))
    gameover = True #making it true from gameover is smart because then we can have conditions that occur only if gameover = TRUE

def update_player_position():
    global player_x
    global player_y
    global player_x_direction
    global player_y_direction
    if player_x_direction > 0:
        if player_x < 600 - player_width: #this checks to make sure player stays in screen, we can adjust player width and this code still works
            player_x += player_x_direction * player_speed #this is how speed can be easily adjusted, just change the variable (this player_x_dir * speed determines  how fast you go)
    if player_x_direction < 0:
        if player_x > 0:
            player_x += player_x_direction * player_speed 
    if player_y_direction > 0:
        if player_y < 600 - player_height: 
            player_y += player_y_direction * player_speed 
    if player_y_direction < 0:
        if player_y > 0:  
            player_y += player_y_direction * player_speed 
            
def update_ball_position():
    global circle_x 
    global circle_y 
    global circle_x_direction 
    global circle_y_direction
    global score
    if circle_x_direction > 0:
        if circle_x < 570: #this checks to make sure the circle doesnt go outside the screen window
            circle_x += circle_x_direction
        else:
            circle_x_direction *= -1 #this makes the circle_x variable negative, which makes sense for the next line 
            score += 1 #this is core incrementer code = no matter the event, put this incrementer at the same time event occurs
    elif circle_x_direction < 0:
        if circle_x > 30:
            circle_x += circle_x_direction
        else:
            circle_x_direction *= -1
            score += 1 
    if circle_y_direction > 0:
        if circle_y < 570:
            circle_y += circle_y_direction
        else:
            circle_y_direction *= -1
            score += 1
    elif circle_y_direction < 0:
        if circle_y > 30:
            circle_y += circle_y_direction
        else:
            circle_y_direction *= -1    
            score += 1


running = True
while running:
    timer.tick(framerate) #This slows down the code to a specified number of updates per second
    update_ball_position()
    update_player_position()
    check_difficulty()
    speed_boost_check()
    
    for event in pygame.event.get(): #get events from the queue
        if event.type == pygame.QUIT: #event.type identifies the type of event
            running = False
        if event.type == pygame.KEYDOWN: #when keys are pressed down
            if event.key == pygame.K_LEFT: #while left key held down, player moves left... nad the same correspondingly with keys below
                player_x_direction = -1
            if event.key == pygame.K_RIGHT:
                player_x_direction = 1
            if event.key == pygame.K_UP:
                player_y_direction = -1
            if event.key == pygame.K_DOWN:
                player_y_direction = 1
        if event.type == pygame.KEYUP: #when keys are released
            if event.key == pygame.K_LEFT:
                player_x_direction = 0
            if event.key == pygame.K_RIGHT:
                player_x_direction = 0
            if event.key == pygame.K_UP:
                player_y_direction = 0
            if event.key == pygame.K_DOWN:
                player_y_direction = 0
            if event.key == pygame.K_SPACE and gameover: #create logic so that when space is release, thats when game over conditions reset ONLY when gameover is True
                circle_x = 300 #PUT ALL CODE IN PLACE TO RESET GAME
                circle_y = 300 #move circle_x and circle_y at initial positions
                circle_x_direction = 3 #in game over we stopped direction variables, so we need to reinitilize those
                circle_y_direction = 6
                player_x = 300 #put player back where it was as well
                player_y = 500
                previous_score = score # we made whatever the last score was the previous score
                if score > high_score: # if score was higher than the current high_score, then make that the new high score
                    high_score = score
                score = 0 #restart score
                last_grabbed = 0
                player_speed = 3
                speedx = -100
                speedy = -100
                gameover = False #make gameover back to False
                
                
                
                
    screen.fill(background)
    ball = pygame.draw.circle(screen, green, (circle_x,circle_y), 30, 5) #arguments: surface, color, position, radius,  how thick the line is
    pygame.draw.circle(screen, red, (circle_x,circle_y), 25)
    gamer = pygame.draw.rect(screen, orange, [player_x, player_y, player_width, player_height]) #args: surface, colour, list of four arguments (x,y starting coordinates and width and height) 
    check_collision(gamer.centerx, gamer.centery, ball.centerx, ball.centery) #this takes in the arguments of the center of GAMER and BALL #centerx and centery are BUILT IN attributes of rectangle and circle from pygame. So, ball.centerx = circle.centerx and so on
    display_score = font.render("Score:" + str(score), True, white, black) #font.render is a built in pygame tool for putting text on screen once font defined
    screen.blit(display_score, (10, 10)) #pygame actually drawing into the screen function #args = coordinates of where the score is displayed
    display_previous_score = font.render("Last Score:" + str(previous_score), True, white, black) #font.render is a built in pygame tool for putting text on screen once font defined
    screen.blit(display_previous_score, (10, 30))
    display_high_score = font.render("High Score:" + str(high_score), True, white, black) #font.render is a built in pygame tool for putting text on screen once font defined
    screen.blit(display_high_score, (10, 50))
    if speed_boost_available:
        speed_boost = pygame.draw.rect(screen, white, [speedx, speedy, 20, 20])
        if gamer.colliderect(speed_boost): #conditions for if player and speed boost collide
            player_speed += 1 #increase speed
            speedx = -100 #send the power up back on screen
            speedy = -100
            last_grabbed = score
            speed_boost_available = False
    display_speed = font.render("Speed: " +str(player_speed-2), True, white, black)
    screen.blit(display_speed, (450,10))
    pygame.display.flip()
pygame.quit() 

# creating object movement, handling collisions and changing speeds