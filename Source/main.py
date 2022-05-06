from traffic_lights_mdp_class import Traffic_Lights_MDP
import csv

with open("../Data_files/Data.csv") as f:
    reader = csv.reader(f)

my_agents = 3
my_states_list = ["High", "Low"]
my_action_list = ["E", "W", "N"]
my_costs = {"C(E)": 3, "C(W)": 3, "C(N)": 3}


my_init_states = ["High;High;High", "High;High;Low", "High;Low;High",
                                 "High;Low;Low", "Low,High,High", "Low,High,Low",
                                 "Low,Low,High", "Low,Low,Low"]

MyMDP = Traffic_Lights_MDP(reader, my_states_list, my_init_states, my_agents, my_action_list, my_costs)


#lista_de_estados = {"High;High;High": {}, "High;High;Low": {},"High;Low;High": {},
                                 #"High;Low;Low": {}, "Low,High,High": {}, "Low,High,Low": {},
                                 #"Low,Low,High": {},"Low,Low,Low": {}}