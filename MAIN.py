import pygame
import time
import random

pygame.init() #initialize module

#This code plays the music while game is running
music = "RainbowRoad_MK_DoubleDash.mp3"
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1) #Allows music to keep looping


# list RGB values or colours
white = (255,255,255)
black = (0,0,0)
purple = (153,0,153)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
pink = (255, 16, 240)
orange = (255,128,0)
brown = (139,69,19)
grey = (160,160,160)
dark_green = (29,164,38)

screen = pygame.display.set_mode([600, 600]) #Create a visual display 
pygame.display.set_caption("COLOUR CHAOS!") #Displays title on game window

title_welcome_font = pygame.font.Font('freesansbold.ttf', 15) #create font object for "welcome to"
title_font = pygame.font.Font('freesansbold.ttf', 120) #create font object for title
title_instructions_font = pygame.font.Font('freesansbold.ttf', 23) #create font object title instructions
start_game_font = pygame.font.Font('freesansbold.ttf', 19) #create font object for 'start game' text

font_user_input = pygame.font.Font('freesansbold.ttf', 50) #create font object for user input
coloured_word_font = pygame.font.Font('freesansbold.ttf', 117) #create font object for coloured words
text_indication_font = pygame.font.Font('freesansbold.ttf', 55) #create font object for text indication
instruction_font = pygame.font.Font('freesansbold.ttf', 40) #create font object for instructions
congratulations_font = pygame.font.Font('freesansbold.ttf', 60) #create font object for congratulations
final_time_font = pygame.font.Font('freesansbold.ttf', 80) #create font object for final time
warning_text_font = pygame.font.Font('freesansbold.ttf', 30) #create font object for warning text
restart_text_font = pygame.font.Font('freesansbold.ttf', 20) #create font object for restart text
scorecard_font = pygame.font.Font('freesansbold.ttf', 24) #create font object for scorecard
high_score_congrats_font = pygame.font.Font('freesansbold.ttf', 25) #create font object for text to appear if new high score

text = ""
text_indication = "Text:____________"
instruction = "What colour is this word?"
congratulations = "Congratulations!"
time_text = "Your time was:"
restart_text = "Press SPACE to Restart"
warning_text = "Try again"
new_high_score = "New high score!"
start_game_text = "Press SPACE to begin"

title_welcome = "Welcome to"
title_title = "COLOUR"
title_title_2 = "CHAOS!"
title_instructions_0 = "Instructions:"
title_instructions_1 = "You will be shown 10 words in different colours."
title_instructions_2 = "Type the COLOUR of the word quickly,"
title_instructions_3 = "and then press Enter to proceed to the next word."
title_instructions_4 = "Beat the high score to set a new record!"
title_instructions_5 = "Good luck!"

title_screen = True #checks to see if we are on title screen
clock = True #checks to see if timer should still be running
count = 0 #counts number of iterations of coloured words displaying
check_spelling = True #checks to see if spelling of user text matches appropriate colour
warning = False #check to see if user text is spelled wrong in order to display warning text or not
gameover = False #checks to see if game has ended
restart = False #checks to see if we should restart
high_score_display = False #checks to see if high score should be displayed

elapsed_time = 0
previous_time = 0
high_score = 10000 #High score cannot equal zero becuase otherwise the high score display would not be correct


# Created the colour and word combinations to randomly displayed on screen
def generate_colour(): 
    black_brown = coloured_word_font.render("Brown", True, black, white)
    black_blue = coloured_word_font.render("Blue", True, black, white)
    black_green = coloured_word_font.render("Green", True, black, white)
    black_orange = coloured_word_font.render("Orange", True, black, white)
    black_yellow = coloured_word_font.render("Yellow", True, black, white)
    purple_green = coloured_word_font.render("Green", True, purple, white)
    purple_blue = coloured_word_font.render("Blue", True, purple, white)
    purple_red = coloured_word_font.render("Red", True, purple, white)
    purple_yellow = coloured_word_font.render("Yellow", True, purple, white)
    purple_orange = coloured_word_font.render("Orange", True, purple, white)
    purple_grey = coloured_word_font.render("Grey", True, purple, white)
    red_blue = coloured_word_font.render("Blue", True, red, white)
    red_purple = coloured_word_font.render("Purple", True, red, white)
    red_green = coloured_word_font.render("Green", True, red, white)
    red_yellow = coloured_word_font.render("Yellow", True, red, white)
    red_pink = coloured_word_font.render("Pink", True, red, white)
    red_grey = coloured_word_font.render("Grey", True, red, white)
    green_blue = coloured_word_font.render("Blue", True, green, white)
    green_yellow = coloured_word_font.render("Yellow", True, green, white)
    green_pink = coloured_word_font.render("Pink", True, green, white)
    green_brown = coloured_word_font.render("Brown", True, green, white)
    green_red = coloured_word_font.render("Red", True, green, white)
    green_grey = coloured_word_font.render("Grey", True, green, white)
    blue_red = coloured_word_font.render("Red", True, blue, white)
    blue_green = coloured_word_font.render("Green", True, blue, white)
    blue_black = coloured_word_font.render("Black", True, blue, white)
    blue_yellow = coloured_word_font.render("Yellow", True, blue, white)
    blue_orange = coloured_word_font.render("Orange", True, blue, white)
    blue_grey = coloured_word_font.render("Grey", True, blue, white)
    yellow_green = coloured_word_font.render("Green", True, yellow, white)
    yellow_blue = coloured_word_font.render("Blue", True, yellow, white)
    yellow_red = coloured_word_font.render("Red", True, yellow, white)
    yellow_brown = coloured_word_font.render("Brown", True, yellow, white)
    yellow_purple = coloured_word_font.render("Purple", True, yellow, white)
    yellow_grey = coloured_word_font.render("Grey", True, yellow, white)
    pink_blue = coloured_word_font.render("Blue", True, pink, white)
    pink_green = coloured_word_font.render("Green", True, pink, white)
    pink_yellow = coloured_word_font.render("Yellow", True, pink, white)
    pink_red = coloured_word_font.render("Red", True, pink, white)
    pink_orange = coloured_word_font.render("Orange", True, pink, white)
    pink_grey = coloured_word_font.render("Grey", True, pink, white)
    orange_purple = coloured_word_font.render("Purple", True, orange, white)
    orange_blue = coloured_word_font.render("Blue", True, orange, white)
    orange_red = coloured_word_font.render("Red", True, orange, white)
    orange_green = coloured_word_font.render("Green", True, orange, white)
    orange_yellow = coloured_word_font.render("Yellow", True, orange, white)
    orange_grey = coloured_word_font.render("Grey", True, orange, white)
    brown_blue = coloured_word_font.render("Blue", True, brown, white)
    brown_pink = coloured_word_font.render("Pink", True, brown, white)
    brown_yellow = coloured_word_font.render("Yellow", True, brown, white)
    brown_green = coloured_word_font.render("Green", True, brown, white)
    brown_red = coloured_word_font.render("Red", True, brown, white)
    grey_red = coloured_word_font.render("Red", True, grey, white)
    grey_orange = coloured_word_font.render("Orange", True, grey, white)
    grey_yellow = coloured_word_font.render("Yellow", True, grey, white)
    grey_green = coloured_word_font.render("Green", True, grey, white)
    grey_purple = coloured_word_font.render("Purple", True, grey, white)
    
    colour_dict = {'black_brown': black_brown, 'black_blue': black_blue, 'black_green': black_green, 'black_orange': black_orange, 'black_yellow': black_yellow, 
                    'purple_green': purple_green, 'purple_blue': purple_blue, 'purple_red': purple_red, 'purple_yellow': purple_yellow, 'purple_orange': purple_orange, 
                    'red_blue': red_blue, 'red_purple': red_purple, 'red_green': red_green, 'red_yellow': red_yellow, 'red_pink': red_pink, 'green_blue': green_blue, 
                    'green_yellow': green_yellow, 'green_pink': green_pink, 'green_brown': green_brown, 'green_red': green_red, 'blue_red': blue_red, 'blue_green': blue_green, 
                    'blue_black': blue_black, 'blue_yellow': blue_yellow, 'blue_orange': blue_orange, 'yellow_green': yellow_green, 'yellow_blue': yellow_blue, 
                    'yellow_red': yellow_red, 'yellow_brown': yellow_brown, 'yellow_purple': yellow_purple, 'pink_blue': pink_blue, 'pink_green': pink_green, 
                    'pink_yellow': pink_yellow, 'pink_red': pink_red, 'pink_orange': pink_orange, 'orange_purple': orange_purple, 'orange_blue': orange_blue, 
                    'orange_red': orange_red, 'orange_green': orange_green, 'orange_yellow': orange_yellow, 'brown_blue': brown_blue, 'brown_pink': brown_pink, 
                    'brown_yellow': brown_yellow, 'brown_green': brown_green, 'brown_red': brown_red, 'purple_grey': purple_grey, 
                    'red_grey': red_grey, 'green_grey': green_grey, 'blue_grey': blue_grey, 'yellow_grey': yellow_grey, 'pink_grey': pink_grey, 'orange_grey': orange_grey, 
                    'grey_red': grey_red, 'grey_orange': grey_orange, 'grey_yellow': grey_yellow, 'grey_green': grey_green, 'grey_purple': grey_purple}
    
    random_colour_key = random.choice(list(colour_dict.keys()))  #randomly picks a coloured word key
    random_colour = colour_dict[random_colour_key]  #retrieve the corresponding coloured word value
    return random_colour, random_colour_key

#check if user input matches crresponding colour of word
def check_if_correct(txt, col_key): #the col_key is the dict KEY (ie. 'purple_green'), NOT the variable purple_green
    global check_spelling
    global warning
    global restart
    restart = False #Ensures that restart = False again so that congratulaions screen can appear
    if txt ==  col_key.split('_')[0]:
        check_spelling = True
        warning = False
    else:
        check_spelling = False
        warning = True

running = True
colour, colour_key = generate_colour()
start_time = None
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and title_screen:
                title_screen = False
                start_time = time.time()
            elif event.key == pygame.K_BACKSPACE: # Handle backspace key press
                text = text[:-1]  # Remove the last character
            elif event.key == pygame.K_RETURN:  # Handle return/enter key press
                check_if_correct(text.lower().strip(), colour_key)
                text = ""
                if check_spelling == True:
                    colour, colour_key = generate_colour() # store both products of generate_colour function
                    count += 1                             
            else: # Handle other key presses
                text += event.unicode  # Append the pressed character to the input text

        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_SPACE and gameover: #Allows user to restart game
                count = 0
                restart = True
                gameover = False
                clock = True
                start_time = time.time() #Used to reset the starting time of the game when it is restarted
                previous_time = elapsed_time
                if float(elapsed_time) < float(high_score): #sets high score
                    high_score = elapsed_time
                high_score_display = True #Ensure high score will be displayed on scorecard only after a game is played
                
    if title_screen == False:
        if clock:
            current_time = time.time()
            elapsed_time = str(round(current_time - start_time, 2))
    
    title_welcome_surface = title_welcome_font.render(title_welcome, True, black, white)
    title_text_surface_1 = title_font.render(title_title, True, green, pink)
    title_text_surface_2 = title_font.render(title_title_2, True, orange, blue)
    title_instructions_text_surface_0 = title_instructions_font.render(title_instructions_0, True, red, white)
    title_instructions_text_surface_1 = title_instructions_font.render(title_instructions_1, True, black, white)
    title_instructions_text_surface_2 = title_instructions_font.render(title_instructions_2, True, black, white)
    title_instructions_text_surface_3 = title_instructions_font.render(title_instructions_3, True, black, white)
    title_instructions_text_surface_4 = title_instructions_font.render(title_instructions_4, True, black, white)
    title_instructions_text_surface_5 = title_instructions_font.render(title_instructions_5, True, black, white)
    start_game_text_surface = start_game_font.render(start_game_text, True, red, yellow)
    width_title_welcome = (screen.get_width() - title_welcome_surface.get_width()) // 2
    width_title_text_1 = (screen.get_width() - title_text_surface_1.get_width()) // 2
    width_title_text_2 = (screen.get_width() - title_text_surface_2.get_width()) // 2
    width_title_instructions_0 = (screen.get_width() - title_instructions_text_surface_0.get_width()) // 2
    width_title_instructions_1 = (screen.get_width() - title_instructions_text_surface_1.get_width()) // 2
    width_title_instructions_2 = (screen.get_width() - title_instructions_text_surface_2.get_width()) // 2
    width_title_instructions_3 = (screen.get_width() - title_instructions_text_surface_3.get_width()) // 2
    width_title_instructions_4 = (screen.get_width() - title_instructions_text_surface_4.get_width()) // 2
    width_title_instructions_5 = (screen.get_width() - title_instructions_text_surface_5.get_width()) // 2
    width_start_game_text = (screen.get_width() - start_game_text_surface.get_width()) // 2
    
    user_text_surface = font_user_input.render(text, True, black, white)
    user_text_rect = user_text_surface.get_rect(center=(352, 420))
    text_indication_surface = text_indication_font.render(text_indication, True, black, white)
    instruction_surface = instruction_font.render(instruction, True, red, white)
    width_instructions = (screen.get_width() - instruction_surface.get_width()) // 2
    congratulations_surface = congratulations_font.render(congratulations, True, red, white)
    time_text_surface = congratulations_font.render(time_text, True, blue, white)
    width_congrats = (screen.get_width() - congratulations_surface.get_width()) // 2
    width_time_text = (screen.get_width() - time_text_surface.get_width()) // 2
    elapsed_time_surface = final_time_font.render(str(elapsed_time) + " seconds", True, black, white)
    width_final_time = (screen.get_width() - elapsed_time_surface.get_width()) // 2
    warning_text_surface = warning_text_font.render(warning_text, True, red, white)
    width_warning_text = (screen.get_width() - warning_text_surface.get_width()) // 2
    restart_text_surface = restart_text_font.render(restart_text, True, dark_green, white)
    width_restart_text = (screen.get_width() - restart_text_surface.get_width()) // 2
    display_elapsed_time = scorecard_font.render("Elapsed Time: " + str(elapsed_time) + " s", True, white, black)
    display_previous_score = scorecard_font.render("Previous Score: " + str(previous_time) + " s", True, white, black)
    display_high_score = scorecard_font.render("High Score: " + str(high_score) + " s", True, yellow, black)
    display_new_high_score = high_score_congrats_font.render(new_high_score, True, red, yellow)
    
    if title_screen == True:
        screen.fill((255, 255, 255))  #Fill the screen with white color
        screen.blit(title_welcome_surface, (width_title_welcome, 70))
        screen.blit(title_text_surface_1, (width_title_text_1, 95))
        screen.blit(title_text_surface_2, (width_title_text_2, 210))
        screen.blit(title_instructions_text_surface_0, (width_title_instructions_0, 350))
        screen.blit(title_instructions_text_surface_1, (width_title_instructions_1, 377))
        screen.blit(title_instructions_text_surface_2, (width_title_instructions_2, 402))
        screen.blit(title_instructions_text_surface_3, (width_title_instructions_3, 427))
        screen.blit(title_instructions_text_surface_4, (width_title_instructions_4, 452))
        screen.blit(title_instructions_text_surface_5, (width_title_instructions_5, 477))
        screen.blit(start_game_text_surface, (width_start_game_text, 530))
    if title_screen == False:
        screen.fill((255, 255, 255))  #Fill the screen with white color
        screen.blit(text_indication_surface, (45,400)) 
        screen.blit(instruction_surface, (width_instructions,155))
        screen.blit(user_text_surface, user_text_rect) 
        screen.blit(colour, (100, 220))
        screen.blit(display_elapsed_time, (10, 10))
        screen.blit(display_previous_score, (10, 37))
        if high_score_display == True:
            screen.blit(display_high_score, (10, 62)) # only displays high score if user has played and completed game
        if warning == True:
            screen.blit(warning_text_surface, (width_warning_text, 500))
        if count > 9 and restart == False: #makes sure only ten iterations of coloured words
            clock = False
            gameover = True
            screen.fill((255, 255, 255))
            screen.blit(congratulations_surface, (width_congrats, 150))
            screen.blit(time_text_surface, (width_time_text, 250))
            screen.blit(elapsed_time_surface, (width_final_time, 350))
            screen.blit(restart_text_surface, (width_restart_text, 500))
            if float(elapsed_time) < float(high_score): #sets high score
                screen.blit(display_new_high_score, (200, 430))

    pygame.display.flip()

# pygame.mixer.quit() #Quits the music once game stops
pygame.quit()