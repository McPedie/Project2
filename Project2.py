from itertools import permutations,  combinations_with_replacement

# City temps
city_temp = {"Lake Havasu City": [71,65,63,66,68], "Sedona": [62,47,45,51,56], "Flagstaff": [46,35,33,40,44], "Casa Grande": [76,69,60,64,69], "Chandler": [77,68,61,65,67]}
city = list(city_temp.keys())

# Hotel Cost
hotel_costs = {"Motel 6": 89, "Best Western": 109, "Holiday Inn Express": 115, "Courtyard by Marriot": 229, "Residence Inn": 199, "Hampton Inn": 209}
hotel = list(hotel_costs.keys())

#Variables needed
Budget = 850
Days = 5


#City Route

perm = permutations(city, Days)

def cost_temp(t):
    s = 0
    for i in range(len(t)):
        city = t[i]
        s+= city_temp[city][i]
    return s/len(t)


best_route = max(perm, key=lambda t: cost_temp(t))

#Hotel Route

combs = list(combinations_with_replacement(hotel, Days))


def cost_route(t):
    return sum([hotel_costs[x] for x in t])

best_option = min(combs, key=lambda t: Budget - cost_route(t) if Budget >= cost_route(t) else Budget)


print ("Youre going on a trip, here is the best possible outcome: \n")

print ("Your best route is:", str(best_route).replace("(","").replace(")", "").replace(","," ->").replace("'",""), "With an average tempature of:", cost_temp(best_route), "F", "\n")

print ("To get close to your budget of $",Budget, "spend: $",cost_route(best_option),"at these hotels:",str(best_option).replace("(","").replace(")", "").replace(","," ->").replace("'",""))

