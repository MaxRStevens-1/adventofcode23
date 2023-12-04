import re

def main():
    
    file = open("day3.txt")
    all_lines = file.readlines()
    
    engine_sum = 0
    
    col = 0
    while col < len(all_lines):
        row = 0
        while row < len(all_lines[col]):
            char = all_lines[col][row]
            start_row = row
            has_seen_num = False
            while (char.isdigit() and char != "." and row < len(all_lines[col])):
                row += 1
                char = all_lines[col][row]
                has_seen_num = True
            if (has_seen_num):
                seen_num = int(all_lines[col][start_row:row:1])
                to_add_num = False
                local_lines = []
                for line in all_lines[max(col-1, 0):col+2:1]:
                    local_lines.append(line[max(start_row-1, 0):row+1])
                    local_row = line[max(start_row-1, 0):row+1]
                    if row + 1 == len(all_lines[col]):
                        local_row = line[max(start_row-1, 0):row]
                    for char in local_row:
                        if (char != "." and not char.isdecimal()):
                            to_add_num = True
                if (to_add_num):
                    engine_sum += seen_num
            row += 1
        col += 1
    print ("P1")
    print (engine_sum)
    print ("#############################")
    print("P2")
    print ("#############################")

    gear_sum = find_gear_sum(all_lines)
    print(f"Gear sum is: {gear_sum}")
    
def find_near_number(line, num_index, col_num):
    num_start_index = num_index
    num_end_index = num_index
    num_current_index = num_index
    # find start
    while (num_current_index > 0 and line[num_current_index] != "." and line[num_current_index].isdecimal()):
        num_current_index -= 1
    num_start_index = num_current_index
    
    num_current_index = num_index
    
    # find end
    while (num_current_index < len(line) and line[num_current_index] != "." and line[num_current_index].isdecimal()):
        num_current_index += 1
    num_end_index = num_current_index
    
    near_num = line[num_start_index:num_end_index]
    near_num = re.sub("[^0-9]", "", near_num)
    return [int(near_num), num_start_index, num_end_index, col_num]

def is_matching_gearnum(gear_num, gear_nums):
    for lgn in gear_nums:
        if lgn[0] == gear_num[0] and lgn[1] == gear_num[1] and lgn[2] == gear_num[2] and lgn[3] == gear_num[3]:
            return True
    return False
        
    
def find_gear_sum(map):
    gear_sum = 0
    col = 0
    while col < len(map):
        row = 0
        while row < len(map[col]):
            char = map[col][row]
            if (char == "*"):
                # search around gear for num
                gear_nums = []
                gear_col = -1
                for line in map[max(col-1, 0):col+2:1]:
                    local_row = line[max(row-1, 0):row+2]
                    if row + 2 == len(map[col]):
                        local_row = line[max(row-1, 0):row+1]
                    elif row + 1 == len(map[col]):
                        local_row = line[max(row-1, 0):row]
                    print (local_row)

                    # find gear num
                    gear_row = -1
                    for i in range(0, len(local_row)):
                        c = local_row[i]
                        if c != "." and c.isdecimal():
                            gear_num = find_near_number(line, row+gear_row, col+gear_col)
                            if (len(gear_nums) > 0 and not is_matching_gearnum(gear_num, gear_nums)):
                                gear_nums.append(gear_num)
                            elif len(gear_nums) == 0:
                                gear_nums.append(gear_num)
                        gear_row += 1
                        
                    gear_col  += 1
                if (len(gear_nums) == 2):
                    gear_sum += gear_nums[0][0] * gear_nums[1][0]
            row += 1
        col += 1
    return gear_sum
                     
                            
    

if __name__ == "__main__":
    main()