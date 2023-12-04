import re

num_dic = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine": 9
}

num_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def find_next_num(line, index):
    for i in range(index, len(line)):
        char = line[i]
        if (char in ["o", "t", "f", "s", "e", "n"]):
            for num_str in num_strings:
                if (line[i:i+len(num_str)] == num_str):
                    return num_dic[num_str]
        elif char.isdigit():
            return int(char) 
            # either number or nothing
        
def find_prev_num(line):
    print ("______________________")
    for i in reversed(range(len(line))):
        char = line[i]
        
        if char.isdigit():
            return int (char)
        for num_str in num_strings:
            if (line[i-len(num_str):i] == num_str):
                return num_dic[num_str]
        

def main():
    file = open("day1.txt")
    # total_num = 0
    # for line in file:
    #     num_line = re.sub("[^0-9]", "", line)
    #     first_num = 0
    #     second_num = 0
    #     if (len(num_line) > 1):
    #         first_num = num_line[0]
    #         second_num = num_line[-1]
    #     elif (len(num_line) == 1):
    #         first_num = num_line[0]
    #         second_num = num_line[0]
    #     total_num += int(first_num + second_num)
    # print (total_num)
    print ("####################")
    print("PART 2")
    print ("####################")
    p2_num = 0
    for line in file:
        line = line.lower()
        first_num = find_next_num(line, 0)
        second_num = find_prev_num(line)
        # print (first_num)
        
        # print (f"second digit is: {second_num}")
        print (f"is {str(first_num) + str(second_num)}")
        p2_num += int(str(first_num) + str(second_num))
    #     for i in reversed(range(line)):
    #         char = line[i]
    #         # check if is number, or starts with numchar
    #         if (char.isdigit()):
    #            second_num = int(char)
               
                       
                    
                
                
    #     line = line.replace("one", "1")
    #     line = line.replace("two", "2")
    #     line = line.replace("three", "3")
    #     line = line.replace("four", "4")
    #     line = line.replace("five", "5")
    #     line = line.replace("six", "6")
    #     line = line.replace("seven", "7")
    #     line = line.replace("eight", "8")
    #     line = line.replace("nine", "9")
        
    #     num_line = re.sub("[^0-9]", "", line)
    #     if (len(num_line) > 1):
    #         first_num = num_line[0]
    #         second_num = num_line[-1]
    #     elif (len(num_line) == 1):
    #         first_num = num_line[0]
    #         second_num = num_line[0]
    #     print (f"num line is {num_line}")
    #     print (f"it is {first_num + second_num}")
    #     p2_num += int(first_num + second_num)
    # print (p2_num)

    print (f" answer is {p2_num}")
    

if __name__ == "__main__":
    main()