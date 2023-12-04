def main():
    file = open("day1.txt")
    all_text: str = file.readline()
    floor_level: int = 0
    basment_index = -1
    for i in range(0, len(all_text), 1):
        c: str = all_text[i]
        if c == "(":
            floor_level += 1
        elif c == ")":
            floor_level -= 1
            
            
        if floor_level == -1 and basment_index == -1:
            basment_index = i
            
    print(f"floor level is: {floor_level}")
    print(f"index is {basment_index+1}")
        
    

if __name__ == "__main__":
    main()