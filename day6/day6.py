import time
import numpy as np
import multiprocessing as mp
from itertools import repeat

def main():
    
    file = open("day6_kerning.txt")
    all_lines = file.readlines()
    
    race_times = np.array(all_lines[0].split(":")[1].split(), dtype=np.int64)
    race_distances =  np.array(all_lines[1].split(":")[1].split(), dtype=np.int64)
    
    print (race_times)
    print (race_distances)
    
    winners_mult = 0
    start = time.time()
    for i in range(len(race_distances)):
        race_time = race_times[i]
        race_distance = race_distances[i]
        
        # get winning time formula
        winning_times = get_winning_times(race_time, race_distance)
        # print (winning_times)
        if i == 0:
            winners_mult = winning_times
        else:
            winners_mult *= winning_times
    end = time.time()
    print (f"took {end - start} seconds")
    print (f"winners mult is: {winners_mult}")
    
    print ("################")
    print (f"PART 2")
    print ("###############")
    
    file = open("day6_example.txt")
    all_lines = file.readlines()
    
    # print (get_fast_winning_times(race_times[0], race_distances[0]))

def get_fast_winning_times(race_time, race_distance):
    num_winners = 0
    print (f"Race time: {race_time} race distace: {race_distance}")
    def get_child_times(midpoint):
        if midpoint <= 0 or midpoint >= race_time:
            return 0
        
        local_winners = 0
        distance_traveled = (race_time - midpoint) * midpoint
        if (distance_traveled > race_distance):
            # now check if next steps are also in range
            midpoint_halved = round(midpoint/2)
            next_midpoint_high = midpoint + midpoint_halved
            next_midpoint_low = midpoint - midpoint_halved
            if (race_time - next_midpoint_high) * midpoint > race_distance:
                # now you have this range
                local_winners += midpoint_halved + get_child_high_times(next_midpoint_high, race_distance)
            if (race_time - next_midpoint_low) * midpoint > race_distance:
                # now you have this range
                local_winners += midpoint_halved + get_child_low_times(next_midpoint_low, race_distance)
                
        return local_winners
    
    def get_child_low_times(midpoint, local_end):
        if midpoint <= 0 or midpoint >= race_time:
            return 0
        print(f"low midpoint is {midpoint}")
        local_winners = 0
        distance_traveled = (race_time - midpoint) * midpoint
        if (distance_traveled > race_distance):
            # now check if next steps are also in range
            midpoint_halved = round(midpoint/2)
            next_midpoint_low = midpoint - midpoint_halved
            if (race_time - next_midpoint_low) * midpoint > race_distance:
                # now you have this range
                local_winners += midpoint_halved + get_child_low_times(next_midpoint_low, local_end)
            while True:
                midpoint_halved = round(midpoint_halved/2)
                
                if midpoint_halved == 0: 
                    return local_winners
                
                next_midpoint_low = midpoint - midpoint_halved
                # print ()
                # if (race_time - next_midpoint_low) * midpoint > race_distance:
                #     # now you have this range
                #     return local_winners + midpoint_halved + get_child_low_times(next_midpoint_low, local_end)
        else: 
            # now reached boundary
            print(f"low value not seenm is {midpoint}")
        return local_winners
        
    def get_child_high_times(midpoint, local_end):
        if midpoint <= 0 or midpoint >= race_time:
            return 0
        
        print(f"high midpoint is {midpoint}")

        local_winners = 0
        distance_traveled = (race_time - midpoint) * midpoint
        if (distance_traveled > race_distance):
            # now check if next steps are also in range
            midpoint_halved = round(midpoint/2)
            next_midpoint_high = midpoint + midpoint_halved
            if (race_time - next_midpoint_high) * midpoint > race_distance:
                # now you have this range
                return local_winners + midpoint_halved + get_child_high_times(next_midpoint_high, local_end)
            print (f"next high is {next_midpoint_high}")
            while True:
                midpoint_halved = round(midpoint_halved/2)
                print (f"current midpoint is {midpoint_halved}")
                if midpoint_halved == 0: 
                    return local_winners
                
                next_midpoint_high = midpoint + midpoint_halved
                print (f"next_high_midpoint: {next_midpoint_high} + midpoint halved: {midpoint_halved}")
                if (race_time - next_midpoint_high) * midpoint > race_distance:
                    # now you have this range
                    return local_winners + midpoint_halved + get_child_high_times(next_midpoint_high, local_end)

                
            # now reached boundary
        print(f"high value not seenm is {midpoint}")
        return local_winners
                
    num_winners += get_child_times( round(race_time/2))    
    return num_winners
        
            
def get_winning_times(race_time:int, race_distance: int):
    winning_times = 0
    for button_press_length in range(race_time):
        distance_traveled = (race_time - button_press_length) * button_press_length
        if (distance_traveled > race_distance):
            winning_times += 1
    return winning_times
        
    
            
if __name__ == "__main__":
    main()