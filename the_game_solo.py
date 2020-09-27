
import random

HANDSIZE = 7
MINCOUNT = 3
MAXNUM = 100

shuffled = list(range(1, MAXNUM))
random.shuffle(shuffled)

stacks = ([0], [MAXNUM], [0], [MAXNUM])

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
            for i in range(len(stacks)):
                diff = card - stacks[i][-1] if i % 2 == 0 else stacks[i][-1] - card
                if diff == -10: min_dist = 0; stack_num = i; card_num = index  # 10-jump rule
                if min_dist > diff > 0: min_dist = diff; stack_num = i; card_num = index 

        if stack_num != -1:
            stacks[stack_num].append(hand.pop(card_num))
            count += 1
        else:
            break

print("Länge shuffled: %d, Länge hand: %d" % (len(shuffled), len(hand)))
