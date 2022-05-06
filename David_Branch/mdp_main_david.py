import csv
import random

class MDP:

    def __init__(self,my_data, state_list, initstates_list, elements, action_list, costs_dict):

        self.data_file = my_data
        self.states = state_list
        self.initial_states_list = initstates_list
        self.agents = elements
        self.actions = action_list
        self.costs = costs_dict

        self.probabilities = {}

    def config_initial_states(self):

        checker = False

        while not checker:

            new_added_state = ""

            for i in range(self.agents):
                new_added_state = new_added_state + self.states[random.randint(0, len(self.states) - 1)]
                new_added_state = new_added_state + ";"



            if new_added_state not in self.initial_states_list:
                initial_state = new_added_state[:-1]
                self.initial_states_list.append(initial_state)
                print(self.initial_states_list)
            else:
                print(self.initial_states_list)
                if len(self.initial_states_list) < len(self.states)**self.agents:
                    checker = True


    def calculate_probabilities(self):

        for element in self.initial_states_list:

            self.probabilities.update({element: {}})

        first_time_key = False
        first_time_semaphore = False
        first_time_final = False

        for key in self.probabilities.keys():
            probability_to_search = ""
            probability_to_search = probability_to_search + key
            probability_to_search = probability_to_search + ";"
            for semaphore in self.actions:
                probability_to_search = probability_to_search + semaphore
                probability_to_search = probability_to_search + ";"
                for final_state in self.initial_states_list:
                    if first_time_final == False:
                        probability_to_search = probability_to_search + final_state
                        print(probability_to_search)
                        first_time_final = True
                    else:
                        probability_to_search = probability_to_search[:-15]
                        probability_to_search = probability_to_search + final_state
                        print(probability_to_search)




        print(self.probabilities)






with open("Data.csv") as f:
    reader = csv.reader(f)

my_agents = 3
my_states_list = ["High", "Low"]
my_action_list = ["E", "W", "N"]
my_costs = {"C(E)": 3, "C(W)": 3, "C(N)": 3}
#lista_de_estados = {"High;High;High": {}, "High;High;Low": {},"High;Low;High": {},
                                 #"High;Low;Low": {}, "Low,High,High": {}, "Low,High,Low": {},
                                 #"Low,Low,High": {},"Low,Low,Low": {}}

my_init_states = ["High;High;High", "High;High;Low", "High;Low;High",
                                 "High;Low;Low", "Low,High,High", "Low,High,Low",
                                 "Low,Low,High", "Low,Low,Low"]

MyMDP = MDP(reader, my_states_list, my_init_states, my_agents, my_action_list, my_costs)

MyMDP.calculate_probabilities()

