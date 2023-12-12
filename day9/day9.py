import time
import numpy as np
import multiprocessing as mp
from itertools import repeat
import functools 
from typing import List
from collections import Counter
import math
def main():
    
    file = open("day9.txt")
    # file = open("day9.txt")
    all_lines = file.readlines()
    result = 0
    start = time.time()
    
    
    
    for line in all_lines:
        graph_line = [eval(i) for i in line.strip().split()]
        all_graphs = [graph_line]
        all_zeros = False
        cur_graph_index = 0
        while not all_zeros:
            new_graph = []
            all_zeros = True
            current_graph = all_graphs[cur_graph_index]
            for i in range(1, len(current_graph)):
                print (current_graph)
                prev = current_graph[i-1]
                curr = current_graph[i]
                der = curr-prev
                new_graph.append(der)
                if all_zeros and der != 0:
                    all_zeros = False
                    
            all_graphs.append(new_graph)
            cur_graph_index += 1
            
        all_graphs[-1].append(0)
        # now that you have a list of all graphs, look at last index, 
        for i in range (len(all_graphs)-2, -1, -1):
            print (i)
            print (len(all_graphs))
            
            prev_graph = all_graphs[i+1]
            curr_graph = all_graphs[i]
            # get first value
            first = prev_graph[0]
            second = curr_graph[0]
            
            curr_graph.insert(0, second - first)
            
            # curr_graph.(prev_graph[-1]+curr_graph[-1])
            print (curr_graph)
            print (f"{second} - {first}")
        print (f"next num is seq is: {all_graphs[0][0]}")
        result += all_graphs[0][0]
            

    end = time.time()
    print (f"took {end - start} seconds")
    print (f"result is is: {result}")


if __name__ == "__main__":
    main()