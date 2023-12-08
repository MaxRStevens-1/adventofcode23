import time
import numpy as np
import multiprocessing as mp
from itertools import repeat
import functools 
from typing import List
from collections import Counter

def main():
    
    file = open("day7.txt")
    all_lines = file.readlines()

    result = 0
    start = time.time()
    hands = []
    for line in all_lines:
        hand_pair = line.split()
        hand = hand_pair[0]
        bet = int(hand_pair[1])
        hands.append((hand, bet))
        print ("___________")
    sorted_hands = sort_hands(hands)
    # order="AKQT98765432J"
    # sorted_hands = sorted(sorted_hands, key=lambda hand: [order.index(c) for c in hand[0]])
    
    
    for i in range(len(sorted_hands)):
        hand = sorted_hands[i]
        result += (len(sorted_hands)-i) * hand[1]
    # get value now
    print (f"the sorted hands are {sorted_hands}")
    print (f"{len(hands)} == {len(sorted_hands)}")

    end = time.time()
    print (f"took {end - start} seconds")
    print (f"result is is: {result}")
    
    
def sort_hands(hands):
    # organize hands by which pairrank they fall into
    
    pair_rank_list = [[], [], [], [], [], [], []]
    
    for hand in hands:
        count_dict = Counter(list(hand[0]))
        j_num = 0
        if "J" in count_dict:
            print ("HAS JACK")
            j_num = count_dict["J"]
            del count_dict["J"]
        max_count = 0
        if (len(count_dict) > 0):
            max_count = count_dict[max(count_dict, key=count_dict.get)]
        # if len(unqiue_hand) == 1 or len(unqiue_hand) == 0:
        # get max value in count_dic
        print (f" hand:{hand} jnum:{j_num} maxcount:{max_count}")
        if max_count + j_num == 5:
            print (f"{hand} is 5 of kind")
            pair_rank_list[0].append(hand)
        elif max_count + j_num == 4:
            print (f"{hand} is 4 of kind")
            pair_rank_list[1].append(hand)
        elif max_count + j_num == 3:
            # either full house or 3 of a kind
            # AAABC, JAABC, JJABC = 3 of kind
            # J:0M1 J:1M:1  J2:M1
            # AAABB, JAABB = FULL HOUSE
            # J:0M:2 J0:M2
            del count_dict[max(count_dict, key=count_dict.get)]
            new_max = count_dict[max(count_dict, key=count_dict.get)]
            if new_max == 1:
                print (f"{hand} is 3 of kind")
                pair_rank_list[3].append(hand)
            elif new_max == 2:
                print (f"{hand} is full house")
                pair_rank_list[2].append(hand)
            else:
                print ("MATH FAILED FOR JNUM 3")
            # has deleteed max value, now check if
        elif max_count + j_num == 2:
            # either 2 pair or one pair
            # AABBC
            # J:0M2
            # AABCD, JABCD
            # J0:M1  J1:M1
            del count_dict[max(count_dict, key=count_dict.get)]
            new_max = count_dict[max(count_dict, key=count_dict.get)]
            if new_max == 2:
                print (f"{hand} is 2 pair")
                pair_rank_list[4].append(hand)
            elif new_max == 1:
                print (f"{hand} is one pair")
                pair_rank_list[5].append(hand)
            else:
                print ("FAILED JNUM 2")
                
        elif max_count + j_num == 1:
            # no matches
            print (f"{hand} is high card")
            pair_rank_list[6].append(hand)
        else:
            print ("FOUND ????")
        print("_______________")
    
    ordered_hand_list = []        
    for matched_hands in pair_rank_list:
        if (len(matched_hands) == 1):
            ordered_hand_list.append(matched_hands[0])
        elif (len(matched_hands) > 1):
            ordered_similar_hands = sort_similar_hands(matched_hands)
            # print("similar hands sorted")
            # print (ordered_similar_hands)
            for similar in ordered_similar_hands:
                ordered_hand_list.append(similar)
                
                
    return ordered_hand_list

def sort_similar_hands(hands):
    new_hands = hands.copy()
    order="AKQT98765432J"
    sorted_hands = sorted(new_hands, key=lambda hand: [order.index(c) for c in hand[0]])
    # print(f"sorted hands is {sorted_hands}")
    return sorted_hands
    
if __name__ == "__main__":
    main()