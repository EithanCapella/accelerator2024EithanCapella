from itertools import product
from typing import List

def seating_arrangements(sd: List[int], td: int) -> int:
    nSeats = len(sd) + 1
    arrangements = list(product([0, 1], repeat=nSeats))  # All seating arrangements
    valid_count = 0
    #print(arrangements)
    
    for arrangement in arrangements:
        occupied_seats = []  #Store the indices of occupied seats
        for i, seat in enumerate(arrangement): #gives us the seat value and index
            if seat == 1:  #If the seat is taken
                occupied_seats.append(i)
        #print(occupied_seats)
        
        if len(occupied_seats) <= 1: #No need to check saids it is a valid seating
            valid_count += 1
            print(arrangement)
        
        elif len(occupied_seats) > 1:
            # Calculate the sum of spaces between the first and next occupied seat found
            for j in range(1, len(occupied_seats)):
                # Calculate the space between consecutive occupied seats
                start = occupied_seats[j-1]
                end = occupied_seats[j]
                space_between = 0
            
            # Check if the seating arrangement is valid
            if space_between >= td:
                valid_count += 1
                print(arrangement)
    


    print(valid_count)    
    return valid_count

#
# TESTS
#

sd = [2, 3, 1]
td = 5
ans = seating_arrangements(sd, td)
exp = 7
assert exp == ans, f"Incorrect answer for sd = {sd}, td = {td}"

sd = [5, 2, 4, 1, 2]
td = 6
ans = seating_arrangements(sd, td)
exp = 16
assert exp == ans, f"Incorrect answer for sd = {sd}, td = {td}"

sd = [2, 3, 2]
td = 6
ans = seating_arrangements(sd, td)
exp = 0
assert exp == ans, f"Incorrect answer for sd = {sd}, td = {td}"

sd = [9, 9, 9, 9]
td = 2
ans = seating_arrangements(sd, td)
exp = 16
assert exp == ans, f"Incorrect answer for sd = {sd}, td = {td}"
