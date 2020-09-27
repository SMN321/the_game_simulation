
import random

HANDSIZE = 7
MINCOUNT = 3
MAXNUM = 100

shuffled = list(range(1, MAXNUM))
random.shuffle(shuffled)

stacks = ([0], [0], [MAXNUM], [MAXNUM])

hand = []

count = MINCOUNT
while count == MINCOUNT:
    # no more cards left
    if len(shuffled) == 0 and len(hand) == 0:
        break

    # fill the hand
    while len(hand) < HANDSIZE and len(shuffled) > 0:
        hand.append(shuffled.pop())

    # play MINCOUNT cards
    count = 0
    for i in range(MINCOUNT):
        min_dist = MAXNUM
        stack_num = -1
        card_num = 0
        # search for the card with the minimal distance to one of the stacks
        for card, index in zip(hand, range(len(hand))):
            if min_dist > card - stacks[0][-1] > 0: min_dist = card - stacks[0][-1]; stack_num = 0; card_num = index 
            if min_dist > card - stacks[1][-1] > 0: min_dist = card - stacks[1][-1]; stack_num = 1; card_num = index
            if min_dist > stacks[2][-1] - card > 0: min_dist = stacks[2][-1] - card; stack_num = 2; card_num = index 
            if min_dist > stacks[3][-1] - card > 0: min_dist = stacks[3][-1] - card; stack_num = 3; card_num = index 
        
        if stack_num != -1:
            stacks[stack_num].append(hand.pop(card_num))
            count += 1
        else:
            break

print("Länge shuffled: %d, Länge hand: %d" % (len(shuffled), len(hand)))
