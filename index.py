def trip_planner_greeting():
    print("Hello")

trip_planner_greeting()    

#estimated cost

def trip_estimated_cost(estimate):
    estimated_cost= round(estimate, 1)
    return estimated_cost

total_estimation = trip_estimated_cost(312.24)

#Where we going 

def trip_fun(start, end, estimate, mode_of_transport="Car"):
    print("We are starting the trip in " + start + " and ending in " + end + " the total estimated cost will be " + str(estimate)
    + "$ and we are getting there VIA " + mode_of_transport)

trip_fun("Mission", "Vancouver", total_estimation)    
