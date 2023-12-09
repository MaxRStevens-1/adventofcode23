import time
import numpy as np
import multiprocessing as mp
from itertools import repeat
import functools 
from typing import List
from collections import Counter
import math
def main():
    
    file = open("day8.txt")
    # file = open("day8_example.txt")
    all_lines = file.readlines()

    connections_dict = {}
    
    # convert L or R to indexs
    
    temp = list(all_lines[0].strip().replace("R", "1").replace("L", "0"))
    path_instructions = [eval(i) for i in temp]
    print (path_instructions[0])
    
    start_con = "AAA"
    starting_connections = []
    end_con = "ZZZ"
    
    for i in range(2, len(all_lines)):
        curr_line = all_lines[i]
        # now parse map
        eq_split = curr_line.split("=")
        start = eq_split[0].strip()
        
        lr_con = eq_split[1].replace("(", "").replace(",", "").replace(")", "").strip().split()
        connections_dict[start] = lr_con
        if "A" in start:
            
            starting_connections.append(start) 
    print (starting_connections)   
    start = time.time()
    
        
    def part_two_solution(starting_point):
        current_entry = starting_point
        current_index = 0
        current_steps = 0
        while "Z" not in current_entry :
            next_entry = connections_dict[current_entry][path_instructions[current_index]]
            current_entry = next_entry
            current_index = (current_index + 1) % len(path_instructions)
            current_steps += 1
            if current_steps % 10000000:
                print (f"{current_steps}", flush=True)
        return current_steps
    
    
    results_list = []
    for connection in starting_connections:
        print (f"finding connection {connection}", flush=True)
        results_list.append(part_two_solution(connection))
        print (results_list, flush=True)
    print (results_list)
    result = math.lcm(*results_list)

    # def part_two_solution():
    #     all_at_z = False 
    #     current_connections = starting_connections.copy()
    #     print (f"Current connections:{current_connections}", flush=True)
        
    #     z_agreement = 0
    #     current_steps = 0
    #     current_index = 0
    #     while not all_at_z:
    #         if current_steps % 1000000 == 0:
    #             print (f"{current_steps}", flush=True)
    #         for connection_index in range(len(current_connections)):
    #             curr_connection = current_connections[connection_index]
    #             next_connection = connections_dict[curr_connection][path_instructions[current_index]]
    #             current_connections[connection_index] = next_connection
    #             if "Z" in next_connection:
    #                 z_agreement += 1
    #         current_steps += 1
    #         current_index = (current_index + 1) % len(path_instructions)
    #         if z_agreement == len(current_connections):
    #             all_at_z = True
    #         z_agreement = 0
    #     return current_steps
    
    def part_one_solution():
        current_entry = start_con
        current_index = 0
        current_steps = 0
        while current_entry != end_con:
            next_entry = connections_dict[current_entry][path_instructions[current_index]]
            current_entry = next_entry
            current_index = (current_index + 1) % len(path_instructions)
            current_steps += 1
            
        return current_steps
    #result = part_one_solution()
    # result = part_two_solution()

    end = time.time()
    print (f"took {end - start} seconds")
    print (f"result is is: {result}")


if __name__ == "__main__":
    main()