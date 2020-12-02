# City route
from itertools import permutations,  combinations_with_replacement
city_temp = {"Lake Havasu City": [71,65,63,66,68], "Sedona": [62,47,45,51,56], "Flagstaff": [46,35,33,40,44], "Casa Grande": [76,69,60,64,69], "Chandler": [77,68,61,65,67]}
city = list(city_temp.keys())


Days = 5

perm = permutations(city, Days)


def temp_func(t):
    return sum([city_temp[t][i][i]for i in range(len t) ])/len(t)


best_route = max(perm, key=lambda t: temp_func(t))
avg_temp = (temp_func(best_route)/Days)

# The best possible temputures for each city: Lake Havasu: 71, Sedona: 62, Flagstaff: 46, Casa Grande: 76 and Chandler: 77




# Hotel Cost
hotel_costs = {"Motel 6": 89, "Best Western": 109, "Holiday Inn Express": 115, "Courtyard by Marriot": 229, "Residence Inn": 199, "Hampton Inn": 209}
hotel = list(hotel_costs.keys())

Budget = 850
Days = 5

combs = list(combinations_with_replacement(hotel, Days))


def cost_func(t):
    return sum([hotel_costs[x] for x in t])

best_option = min(combs, key=lambda t: Budget - cost_func(t) if Budget >= cost_func(t) else Budget)


print ("Youre going on a trip, here is the best possible outcome: \n")

print ("Your best route is:", str(best_route).replace("(","").replace(")", "").replace(","," ->").replace("'",""), "With an average tempature of:", avg_temp, "\n")

print ("To get close to your budget of $",Budget, "spend: $",cost_func(best_option),"at these hotels:",str(best_option).replace("(","").replace(")", "").replace(","," ->").replace("'",""))

