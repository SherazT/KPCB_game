import pygame
import time
import random
import os
import pdb

# CONSTANTS

# Dimensions
DISPLAY_SIZE = (720, 600)
GAME_TITLE = "Memory"
WIDTH = 9
HEIGHT = 6
# Cards
CARD_W = 80
CARD_H = 100
DECK_SIZE = 54

# Speed
FPS = 60
CARD_WAIT_MAX = 3

# Misc
WELCOME_MESSAGE = "Greetings. Please select two cards and try and find all matches."

def resolve_loc(location):
    return WIDTH*location[1]+location[0]

def same(deck, cards_clicked):
    first_card = deck[resolve_loc(cards_clicked[0])]
    second_card = deck[resolve_loc(cards_clicked[1])]

    if first_card == second_card:
        return first_card

def find_card(mouse_pos):
    (X_pos, Y_pos) = mouse_pos
    card = (int(X_pos/CARD_W), int(Y_pos/CARD_H))
    return card

def display_board(cards):
    canvas = pygame.display.set_mode(DISPLAY_SIZE)
    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            canvas.blit(cards[x + WIDTH*y], (x*CARD_W,y*CARD_H))

def import_card(suit, char):
    card = "./cards/{}/{}.png".format(suit, char)
    import_card = pygame.image.load(card)
    import_card = pygame.transform.scale(import_card, (CARD_W-1, CARD_H-1))

    return import_card

def card_front_setup():
    cards = []
    suits = ['clubs', 'diamonds']
    chars = [i for i in range(2,11)]
    chars.extend(['J', 'Q', 'K', 'A'])

    for suit in suits:
        for char in chars:
            cards.append(import_card(suit, char))

    card = "./cards/Joker_1.png"
    joker = pygame.image.load(card)
    joker = pygame.transform.scale(joker, (CARD_W-1, CARD_H-1))
    cards.append(joker)
    cards *= 2

    random.shuffle(cards)

    return cards

def main():
    pygame.init()
    canvas = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption(GAME_TITLE)
    uni_clock = pygame.time.Clock()

    deck = card_front_setup()

    card_back = pygame.image.load("./cards/kpcb.jpg")
    card_back = pygame.transform.scale(card_back, (CARD_W-1, CARD_H-1))
    front_deck = []
    for x in range(DECK_SIZE):
        front_deck.append(card_back)
    display_board(front_deck)

    card_touched = []
    visible = []
    miss = 0
    card1_time = 0
    card2_time = 0
    hold_time = 1
    startGame = True

    print (WELCOME_MESSAGE)

    while startGame:        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                curr_card = find_card(mouse_pos)

                if curr_card not in card_touched and curr_card not in visible:
                    card_touched.append(curr_card)

                    if len(card_touched) <= 2:
                        canvas.blit(deck[resolve_loc(curr_card)], (CARD_W*curr_card[0],CARD_H*curr_card[1]))
                        card1_time = time.time()

                    if len(card_touched) == 2:
                        card2_time = time.time()

                        if same(deck, card_touched):
                            visible.extend(card_touched)
                            for flip in card_touched:
                                front_deck[resolve_loc(flip)] = deck[resolve_loc(flip)]
                            
                            print ("You found: {}/27".format(len(visible)/2))
                            hold_time = 0
                        else:
                            miss += 1

        if len(card_touched) >= 2 and (time.time() - card2_time) > hold_time:
            display_board(front_deck)
            card_touched = []
            hold_time = 1

        elif len(card_touched) == 1 and (time.time() - card1_time) > CARD_WAIT_MAX:
            display_board(front_deck)
            card_touched = []

        pygame.display.flip()
        uni_clock.tick(FPS)

        if len(visible) == DECK_SIZE:
            print ("You Won!")
            print ("Score: {} false positives".format(miss))

    pygame.quit()

main()
