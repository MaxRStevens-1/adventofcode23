import re

def main():
    file = open("day2.txt")

    MAX_RED: int = 12
    MAX_GREEN: int = 13
    MAX_BLUE: int = 14
    
    blue = "blue"
    green = "green"
    red = "red"
    
    # game_id_sum = 0

    sum_power_set = 0

    for line in file:
        colon_split = line.split(":")    
        # game_id = int(re.sub("[^\d\.]", "", colon_split[0]))
        # game_id = int(filter(type(colon_split[0]).is)
        semi_split = colon_split[1].split(";")
        # add_game_id = True
        min_red = 0
        min_green = 0
        min_blue = 0
        for game in semi_split:
            comma_split = game.split(",")
            for draw in comma_split:
                draw_num = int(re.sub("[^\d\.]", "", draw))
                # if (blue in draw and draw_num > MAX_BLUE) or (green in draw and draw_num > MAX_GREEN) or (red in draw and draw_num > MAX_RED):
                    # game_id_sum += game_id
                    # add_game_id = False
                if blue in draw and draw_num > min_blue:
                    min_blue = draw_num
                elif green in draw and draw_num > min_green:
                    min_green = draw_num
                elif red in draw and draw_num > min_red:
                    min_red = draw_num
        sum_power_set += min_red * min_green * min_blue
                    
        # if (add_game_id):
        #     game_id_sum += game_id
            # print(f"{line}")
        # add_game_id = True
    print(f"power sum is {sum_power_set}")
                
    
        
    
    

if __name__ == "__main__":
    main()