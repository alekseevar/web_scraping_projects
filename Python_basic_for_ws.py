import pandas as pd

#states = ["California", "Texas", "Florida", "New York"]
#population = [123456, 1345677, 7654332, 7654325]

#dict_states = {'States': states, "Population": population}

#df_states = pd.DataFrame.from_dict(dict_states)
#print(df_states)

#df_states.to_csv("states.csv", index=False)

#print(states[3])

#for state in states:
#    if state == "Florida":
#        print(state)


#with open("test.txt", "w") as file:
#    file.write("Data successfully scraped")


new_list = [2, 4, 6, "California"]


for element in new_list:
    try:
        print(element/2)
    except:
        pass

