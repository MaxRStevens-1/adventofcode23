import re

def main():
    
    file = open("day4example.txt")
    
    p1_sum = 0
    game_num = 1
    for line in file:
        colon_split = line.split(":")
        line_split = colon_split[1].split("|")
        winning_numbers = line_split[0].strip().split(" ")
        scratched_numbers = line_split[1].strip().split(" ")
        local_points = 0
        print (f"IN GAME {game_num}")
        game_num += 1
        print (f"winning nums are {winning_numbers}")
        print (f"Scratcehd nums are: {scratched_numbers}")
        for scratched_num in scratched_numbers:
            if not scratched_num.isdecimal():
                continue
            if scratched_num in winning_numbers and local_points == 0:
                local_points = 1
            elif scratched_num in winning_numbers:
                local_points *= 2
        print (f"local points are: {local_points}")
        p1_sum += local_points
        print ("___________________")
    print(f"Total points are: {p1_sum}")
    print("########################")
    print("P2")
    print("########################")
    
    file = open("day4.txt")

    card_hash = {}
    game_num = 1
    p2_cards_sum = 0
    for line in file:
        colon_split = line.split(":")
        line_split = colon_split[1].split("|")
        winning_numbers = line_split[0].strip().split(" ")
        scratched_numbers = line_split[1].strip().split(" ")
        card_hash[game_num] = [winning_numbers, scratched_numbers]
        game_num += 1
        print (line)
    
    card_stack = []
    # card_stack.append(1)
    print (range(len(card_hash)))
    for i in range(len(card_hash)):
        card_stack.append(i+1)
    p2_cards_sum = len(card_hash.values())

    while len(card_stack) > 0:
        current_game_num = card_stack.pop()
        winning_numbers = card_hash[current_game_num][0]
        scratched_numbers = card_hash[current_game_num][1]
        total_wins = 0
        for scratched_num in scratched_numbers:
            if not scratched_num.isdecimal():
                continue
            elif scratched_num in winning_numbers:
                total_wins += 1
        print (f"FOR CARD: {current_game_num}")
        for i in range(total_wins):
            card_stack.append(current_game_num+i+1)
            # print (f"GOTTEN COPY OF CARD: {current_game_num+i+1}")
        p2_cards_sum += total_wins
        # print("__________")
    print (f"total num of cards is: {p2_cards_sum}")
        
        
        
                
        
        


if __name__ == "__main__":
    main()