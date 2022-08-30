###########
# imports #
###########
import random
import pygame
from sys import exit  # this is a library of system features for manipulating windows; don't worry about this


############################################################################################
# pygame initializes window, sets the title of the window (AKA "caption"), sets clock, etc #
############################################################################################

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('PixelMon')
clock = pygame.time.Clock()
game_still_on = True
player_turn = True
is_winner = True

######################
# graphics variables #
######################

flamio_x_pos = 300
flamio_y_pos = 600
beario_x_pos = 900
beario_y_pos = 350

flamio = pygame.image.load("./sprites&graphics/Flamio.png").convert_alpha()
flamio_rect = flamio.get_rect(midbottom=(flamio_x_pos, flamio_y_pos))
beario = pygame.image.load("./sprites&graphics/Beario.png").convert_alpha()
beario_rect = beario.get_rect(midbottom=(beario_x_pos, beario_y_pos))
grass_battleground = pygame.image.load("./sprites&graphics/battle_ground.png")

###########################
# font selection and text #
###########################

font = pygame.font.Font(None, 40)
instructions = font.render('Press SPACE for fire move', False, 'Black')
you_win = font.render("Flamio hits!", False, 'Black')
opp_win = font.render("Beario hits!", False, 'Black')

###################
# adding lifespan #
###################

# for beario

lifespan_full_b = pygame.image.load("./sprites&graphics/lifespan_full.png").convert_alpha()
lifespan_full_b_rect = lifespan_full_b.get_rect(midbottom=(1000, 500))
lifespan_empty_b = pygame.image.load("./sprites&graphics/lifespan_empty.png").convert_alpha()
lifespan_empty_b_rect = lifespan_empty_b.get_rect(midbottom=(1000, 500))

# for flamio

lifespan_full_f = pygame.image.load("./sprites&graphics/lifespan_full.png").convert_alpha()
lifespan_full_f_rect = lifespan_full_f.get_rect(midbottom=(200, 800))
lifespan_empty_f = pygame.image.load("./sprites&graphics/lifespan_empty.png").convert_alpha()
lifespan_empty_f_rect = lifespan_empty_f.get_rect(midbottom=(200, 800))


################
# winner quote #
################

winner_flamio = font.render("You win! Congrats!", False, "White")
winner_beario = font.render("You lose! Better luck next time...", False, "White")


##########################
# functions & animations #
##########################

def opp_hit():
    print("Beario hits!")
    print("Beario wins!")


def opp_miss():
    print("Beario missed!")


def player_hit():
    print("You hit!")
    print("You win!")


def player_miss():
    print("You missed! Beario's turn...")


###################
# actual gameplay #
###################

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_still_on is True:
        screen.blit(grass_battleground, (0, 0))
        screen.blit(instructions, (50, 50))

        screen.blit(flamio, flamio_rect)
        screen.blit(beario, beario_rect)

        screen.blit(lifespan_full_b, lifespan_full_b_rect)
        screen.blit(lifespan_full_f, lifespan_full_f_rect)

        chance = random.randint(0, 10)
        keys = pygame.key.get_pressed()
        space = keys[pygame.K_SPACE]

        if player_turn is True:
            if (space is True) and (chance >= 5):
                player_hit()
                screen.blit(lifespan_empty_b, lifespan_empty_b_rect)
                screen.blit(you_win, (50, 200))
                is_winner = True
                game_still_on = False
            elif (space is True) and (chance < 5):
                player_miss()
                player_turn = False

        elif player_turn is False:
            if chance >= 5:
                opp_hit()
                screen.blit(lifespan_empty_f, lifespan_empty_f_rect)
                screen.blit(opp_win, (50, 200))
                is_winner = False
                game_still_on = False
            elif chance < 5:
                opp_miss()
                player_turn = True

    elif game_still_on is False:
        pygame.time.delay(1000)  # allows our screen to blit the empty lifespan
        screen.fill("Black")
        if is_winner is True:
            screen.blit(winner_flamio, (500, 200))
        elif is_winner is False:
            screen.blit(winner_beario, (500, 200))

    pygame.display.update()
    clock.tick(60)
