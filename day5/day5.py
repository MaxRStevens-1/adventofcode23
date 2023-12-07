import time
import numpy as np
import multiprocessing as mp
from itertools import repeat

class mapRanges:
    
    def __init__ (self, name):
        self.from_ranges = []
        self.to_ranges = []
        self.name = name
        pass
    
    def add_range(self, ranges):
        self.from_ranges.append((ranges[1], ranges[1]+ranges[2]))
        self.to_ranges.append((ranges[0], ranges[0]+ranges[2]))
    
    def in_range(self, value, range):
        return (value >= range[0] and value <= range[1])
        
    def get_value_from_to_range(self, value):
        for i in range(len(self.from_ranges)):
            current_from_range, current_to_range= self.from_ranges[i], self.to_ranges[i]
            # if self.in_range(value, current_from_range):
            if (value >= current_from_range[0] and value <= current_from_range[1]):
                # return the converted to range in to_range
                return value - current_from_range[0] + current_to_range[0]
        return value
    
    # def get_range_from_range(self, min_value, max_value):
    #     range_splits = []
    #     for i in range(len(self.from_ranges)):
    #         current_from_range, current_to_range = self.from_ranges[i], self.to_ranges[i]
    #         if (min_value >= current_from_range[0] and  min_value <= current_from_range[1]):
    #             # now you know that there are SOME values in the range that fit above
    #             # so first converted value for the converted range
    #             # converted_min_value = min_value - current_from_range[0] + current_to_range[0]
    #             converted_min_value = (min_value - current_from_range[0]) + current_to_range[0] 
    #             # now you need to get the maximum value of the range conversion
    #             # 
    #             if max_value > current_from_range[1]:
    #                 converted_max_value = current_to_range[1]
    #             else:
    #                 converted_max_value = (max_value - current_from_range[0]) + current_to_range[0]
                
    #             # now you have the new range of values 
    #         # else:
    #         #     converted_min_value = min_value
    #         #     converted_max_value = max_value
    #         # print (f"adding {converted_min_value}, {converted_max_value}")
    #          range_splits.append((converted_min_value, converted_max_value))
    #     # print (f"returning {range_splits}")
    #     return range_splits
        

    def toString(self):
        toStr = self.name + ":\n    "
        for i in range(len(self.from_ranges)):
            toStr += str(self.from_ranges[i])
            toStr += str(self.to_ranges[i]) + ", "
        toStr += "\n"
        return toStr

def main():
    
    file = open("day5.txt")
    all_lines = file.readlines()
    seed_line = all_lines[0]
    seeds = seed_line.strip().split(":")[1].split()
    seeds = list(map(lambda x: int(x), seeds))
    print (seeds)
    
    map_range_list = []
    i = 1    
    while i < len(all_lines):
        curr_line = all_lines[i]
        if "map" in curr_line:
            map_removed_line = curr_line.split(" map")[0]            
            
            current_map_ranges = mapRanges(map_removed_line)
            i += 1
            while i < len(all_lines):
            # for x in range(i+1, len(all_lines)):
                look_line = all_lines[i]
                if "map" in look_line or len(look_line) < 2:
                    break
                curr_range = list(map(lambda x: int(x), look_line.split()))
                current_map_ranges.add_range(curr_range)
                i += 1
            map_range_list.append(current_map_ranges)
            print (current_map_ranges.toString())
            print ("_________")
        i += 1
    
    # now map ranges have all ranges
    lowest_num = float('inf')
    
    for seed in seeds:
        curr_num = seed
        for loc_range in map_range_list:
            # print(f"using {loc_range.name}: {curr_num} to {loc_range.get_value_from_to_range(curr_num)}")
            curr_num = loc_range.get_value_from_to_range(curr_num)
        if (curr_num < lowest_num):
            lowest_num = curr_num
        # print (f"for seed {seed} the lowest num is {curr_num}")
    print (f"lowest value is: {lowest_num}" )
    
    print("######################")
    print("PART 2")
    print("######################")
    lowest_num = float('inf')
    print (seeds)
    total_num_seeds = 0
    # # seed_pairs = []
    # current_seed_pairs = []
    # next_seed_pairs = []
    # for i in range (0, len(seeds), 2):
    #     start_seed = seeds[i]
    #     num_seeds = seeds[i+1]
    #     # seed_pairs.append((start_seed, num_seeds))
    #     seed_min = start_seed
    #     seed_max = start_seed + num_seeds -1
    #     current_seed_pairs.append((seed_min, seed_max))
    #     print (f"Range is ({seed_min},{seed_max})")
    #     # for loc_range in map_range_list:
    # for loc_range in map_range_list:
    #     print (f"ON LOCATION: {loc_range.name}")
    #     print (f"CURRENT PAIRS ARE: {current_seed_pairs}")
    #     for seed_pair in current_seed_pairs:
    #         min_seed = seed_pair[0]
    #         max_seed = seed_pair[1]
    #         next_pairs = loc_range.get_range_from_range(min_seed, max_seed)
    #         for pair in next_pairs:
    #             next_seed_pairs.append(pair)
    #     # print (next_seed_pairs)
    #     # print (len(next_seed_pairs))
    #     current_seed_pairs = next_seed_pairs

    # # get lowest
    # for seed_pair in current_seed_pairs:
    #     if seed_pair[0] < lowest_num:
    #         total_num_seeds = seed_pair[0]
    # print (f"lowest number {total_num_seeds}")
    # for see
    all_seeds =[]
    start = time.process_time()
    for i in range(0, len(seeds), 2):
        start_seed = seeds[i]
        stop = seeds[i]+seeds[i+1]
        local_seeds = np.arange(start_seed, stop)
        all_seeds.append(local_seeds)
        print  (f"range {i}: ({seeds[i+1]})")
        total_num_seeds += seeds[i+1]
    end = time.process_time()
    all_seeds_1 = np.concatenate(all_seeds[0:3])
    print (len(all_seeds_1))
    all_seeds_2 = np.concatenate(all_seeds[3:len(all_seeds)])
    print (f"{end - start} seconds to generate all seeds")
    print (len(all_seeds_2))
    # print (f"({seeds[0]}, {seeds[0]+seeds[1]}) + ({seeds[2]}, {seeds[2]+seeds[3]})")    
    # # print (f"total: {seeds[1] +seeds[3]}")
    # start = time.time()
    
    # # first_seed_range = np.arange(seeds[0], seeds[0]+seeds[1], 1)
    start = time.time()
    # print (f"len is {len(first_seed_range)}")
    # print (f"took {end_construct - start} seconds to create list")
    print (f"starting pool with {len(all_seeds)} proc", flush=True)
    pool = mp.Pool(processes=16)
    results = pool.map(mp_seeds, [(all_seeds, map_range_list,), range(16)])
    # print (results)
    # for local_seeds in all_seeds:
    #     print (f"looking at {len(local_seeds)} seeds")
    print (f"THE SMALLEST VALUE IS : {min(results)}")
        
        
        
        
def mp_seeds(inputs, proc_num):
    process = mp.current_process()
    pid = process.pid
    
    local_seeds, map_range_list = inputs[0], inputs[1]
    
    print (f"in current proc {pid}", flush=True)
    lowest_num = float("inf")
    start = time.time()
    seed_time = time.time()
    for i in range(proc_num, len(local_seeds), 16):
        seed = local_seeds[i]
        curr_num = seed
        for loc_range in map_range_list:
            curr_num = loc_range.get_value_from_to_range(curr_num)
        if (curr_num < lowest_num):
            lowest_num = curr_num
        if (seed % 100000 == 0):
            seed_end = time.time()
            print (f"Proc: {pid} took {seed_end - seed_time} seconds for 100k", flush=True)
            seed_time = seed_end
    
    end = time.time()
    print (f"took {end - start} seconds to finish")
    # print (f"lowest value for total is: {lowest_num}" )
    return lowest_num

            
if __name__ == "__main__":
    main()