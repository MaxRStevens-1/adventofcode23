import time
import numpy as np
import multiprocessing as mp
from itertools import repeat
import functools 
from typing import List
from collections import Counter
import math
from collections import deque
import matplotlib as mpl
from matplotlib import pyplot


north = (-1, 0)
south = (1, 0)
west = (0, -1)
east = (0, 1)

movement_dic = {
    "S": [north, south, east, west],
    "|": [north, south],
    "-": [east, west],
    "L": [north, east],
    "J": [north, west],
    "7": [south, west],
    "F": [south, east],
    ".": [(0,  0)]
    }

def main():
    
    file = open("day10_example_5.txt")
    all_lines = file.readlines()
    maze = all_lines
    result = 0
    start = time.time()
    
    # get index of s
    s_arr = [x for x in all_lines if "S" in x][0]
    # s_pos = (maze.index(s_arr), s_arr.index("S"))
    s_pos = (maze.index(s_arr), s_arr.index("S"))
    print (f"S pos is {s_pos}: {maze[s_pos[0]][s_pos[1]]}")
    # visited is list of position
    visited = {}
    open_queue = deque()
    # open is list of position, and parent
    open_queue.append((s_pos, None, 0))
    visited_arr = np.zeros(shape=(len(maze), len(maze[0])))
    
    # has distance traveled and immediate children
    print ("_____")
    current_node = s_pos
    is_first_time = True
    # honestly not sure why this worked, why doens't BFS work??
    while True:
        # grab cur node
        current_node, parent, distance = open_queue.pop()
        current_node_tile = get_tile(maze, current_node)
        # disgusting, but works ...
        if (current_node_tile == "S"):
            current_node_tile = "|"
        current_node_neighbors = movement_dic[current_node_tile]
        # print (f"for tile {current_node_tile} at pos {current_node} with parent {parent} and distance {distance}")
        for neighbor in current_node_neighbors:
            neighbor_pos = (neighbor[0]+current_node[0], neighbor[1]+current_node[1])
            neighbor_tile = get_tile(maze, neighbor_pos)
            if neighbor_tile != "." and neighbor_pos not in visited and neighbor_pos != parent:
                open_queue.append((neighbor_pos, current_node, distance + 1))
            # if not get_in_bounds(visited_arr, neighbor_pos):
        visited_arr[current_node[0]][current_node[1]] = 1
            
        if is_first_time:
            is_first_time = False
        elif current_node == s_pos: 
            break
        else:
            visited[current_node] = True
        
    result = math.ceil(distance/2)
    


    end = time.time()
    print (f"took {end - start} seconds")
    print (f"result is is: {result}")

    # pyplot.imshow(visited_arr)
    # pyplot.show()
    start = time.time()
    # do a BFS search of graph
    # visited = {}
    # open_queue = deque()
    # # open is list of position, and parent
    # open_queue.append((s_pos, None, 0))
    # current_node = s_pos
    # is_first_time = True

    
    pyplot.imshow(visited_arr)
    pyplot.show()
    
    p2_result = 0
    # iterate over list, find unvisited section
    for i in range(len(visited_arr)):
        for j in range(len(visited_arr[i])):
            curr = visited_arr[i][j]
            if curr == 0:
                covered_result = get_covered_num(visited_arr, (i, j), maze)
                p2_result += covered_result[0]
                visited_arr = covered_result[1]
    result = 0
    for i in range(len(visited_arr)):
        for j in range(len(visited_arr[i])):
            curr = visited_arr[i][j]
            if curr == 2:
                result += 1
    end = time.time()
    
    pyplot.imshow(visited_arr)
    pyplot.show()
    print (f"got {result} in {end - start} seconds")
                
                

def get_covered_num(maze, starting_point, direction_map):
    # check neighbors
    neighbors = [north, south, east, west]
    open = [starting_point]
    total_covered = 0
    
    temp_maze = maze.copy()
    
    while len(open) > 0:
        curr_node = open.pop(0)
        for neighbor in neighbors:
            neighbor_pos = (neighbor[0] + curr_node[0], neighbor[1] + curr_node[1])
            is_not_in_bounds = get_in_bounds(temp_maze, neighbor_pos)
            if is_not_in_bounds:
                return (0, maze)
            elif temp_maze[neighbor_pos[0]][neighbor_pos[1]] != 0:
                continue
            temp_maze[neighbor_pos[0]][neighbor_pos[1]] = 2
            open.append(neighbor_pos)
        total_covered += 1
        temp_maze[curr_node[0]][curr_node[1]] = 2
    # print (f"found a total of {total_covered} from start point {starting_point}")
    return (total_covered, temp_maze)
            


def get_in_bounds(maze, pos):
    return pos[0] < 0 or pos[0] >= len(maze) or pos[1] < 0 or pos[1] >= len(maze[pos[0]])

def get_tile(maze, pos):
    if pos[0] < 0 or pos[0] >= len(maze) or pos[1] < 0 or pos[1] >= len(maze[pos[0]]): 
        return "."
    else:
        return maze[pos[0]][pos[1]]

if __name__ == "__main__":
    main()