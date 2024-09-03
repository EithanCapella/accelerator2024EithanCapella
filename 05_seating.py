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
        #print(str(occupied_seats) + " : " + str(arrangement))
        
        if len(occupied_seats) <= 1: #No need to check saids it is a valid seating
            valid_count += 1
            print(str(arrangement) + " valid 1st case")
        
        elif len(occupied_seats) > 1:
            space_between = 0
            valid = True
            # Calculate the sum of spaces between the first and next occupied seat found
            for j in range(0, len(occupied_seats)):
                # Calculate the space between consecutive occupied seats
                start = occupied_seats[j]
                if(j < len(occupied_seats)-1):
                    end = occupied_seats[j+1]
                else: end = occupied_seats[j]
                print(str(start) + " " + str(end) + " " + str(sum(sd[start:end])) + " check " + str(arrangement))
                space_between = sum(sd[start:end])
                if(space_between < td and start is not end):
                    print("ran")
                    valid = False
                    break
                    
            
            # Check if the seating arrangement is valid
            if valid:
                valid_count += 1
                print(str(arrangement) + " valid 2nd case")
    


    print(str(valid_count) + "--------------------------------")    
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
exp = 6 #how can this test case be 0 if we count seatings that are in this form 0001 0010 0100 1000
assert exp == ans, f"Incorrect answer for sd = {sd}, td = {td}"

sd = [9, 9, 9, 9]
td = 2
ans = seating_arrangements(sd, td)
exp = 16 #If we have 5 seats with 9 units of space in between each seat and we must have each person
#seating no less than 2 units apart doesn't that mean every set is valid? 
#since every possible combo will have more than 2 units apart.
assert exp == ans, f"Incorrect answer for sd = {sd}, td = {td}"
