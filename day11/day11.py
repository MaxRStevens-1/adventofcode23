import time
import numpy as np
import itertools
import math

up     = (-1,  0)
down   = ( 1,  0)
left   = ( 0, -1)
right  = ( 0,  1)

def main():
    
    file = open("day11.txt")
    all_lines = file.readlines()
    local_lines = []
    result = 0
    start = time.time()
    
    rows_to_add = []
    cols_to_add = []
    
    # grab empty rows and col
    for i in range(len(all_lines)):
        row = all_lines[i]
        local_lines.append(list(row.strip()))
        print (row)
        if "#" in row:
            continue
        rows_to_add.append(i)
    print ("______")
    print (local_lines)
    numpy_col_line = np.array(local_lines).T
    for i in range(len(numpy_col_line)):
        col = numpy_col_line[i]
        print (col)
        if "#" in col:
            continue
        cols_to_add.append(i)
    print (f"need to add new rows: {rows_to_add} and cols {cols_to_add}")
    
    for i in range(len(rows_to_add)):
        row = rows_to_add[i]
        local_lines.insert(row+i, ['.']*len(local_lines[row+i]))
    
    print (local_lines)
    
    for i in range(len(cols_to_add)):
        col = cols_to_add[i]
        print (f" for {col}")
        print  (f"{np.array(local_lines)}")
        for line in local_lines:
            # print (f"line was: {line} ")
            line.insert(col+i, ".")
            # print (f"line is: {line}")
        print(f"{np.array(local_lines)}")
        print("_____________________")
    print ("___-")
    print (np.array(local_lines))
    
    # now number the galaxies
    nodes = []
    for i in range(len(local_lines)):
        row = local_lines[i]
        for x in range(len(row)):
            item = row[x]
            if item == "#":
                item = len(nodes)+1
                nodes.append((i,x))
                
    node_combos = list(itertools.combinations(nodes, 2))
    print (node_combos)
    
    # now find path lengths from combos
    
    for node_a, node_b in node_combos:
        result += abs(node_b[0] - node_a[0]) + abs(node_b[1] - node_a[1])
    
    end = time.time()
    print (f"took {end - start} seconds")
    print (f"result is is: {result}")
    print (len(node_combos))


    start = time.time()
    # now what I should do is simply take the pos of each galaxy,
    # mark down number of distance increases in row, col form
    
    print("______________________________")
    local_lines = []
    for i in range(len(all_lines)):
        row = all_lines[i]
        local_lines.append(list(row.strip()))
        print (row)
        
    galaxies = []
    for i in range(len(local_lines)):
        row = local_lines[i]
        for x in range(len(row)):
            item = row[x]
            if item == "#":
                item = len(nodes)+1
                galaxies.append((i,x))
    
    ADDED_DISTANCE = 999999
    galaxies_with_added_distance = []
    for galaxy in galaxies:
        gal_row = galaxy[0]
        gal_col = galaxy[1]
        
        gal_row_to_add = 0
        gal_col_to_add = 0
        
        for add_row in rows_to_add:
            if gal_row > add_row:
                gal_row_to_add += ADDED_DISTANCE
        for add_col in cols_to_add:
            if gal_col > add_col:
                gal_col_to_add += ADDED_DISTANCE
        print (f"for {galaxy}: has more rows: {gal_row_to_add} and more cols: {gal_col_to_add}")
        galaxies_with_added_distance.append((gal_row_to_add+gal_row, gal_col_to_add+gal_col))
    
    gal_combos = list(itertools.combinations(galaxies_with_added_distance, 2))
    result = 0

    for node_a, node_b in gal_combos:
        # print (f"{node_a}, {node_b}")
        result += abs(node_b[0] - node_a[0]) + abs(node_b[1] - node_a[1])
        
    end = time.time()
    print (f"result {result} in {end - start} seconds")
                



if __name__ == "__main__":
    main()