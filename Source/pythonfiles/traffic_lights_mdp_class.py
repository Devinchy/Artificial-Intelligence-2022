from pythonfiles.state_high_high_high import probability_high_high_high
from pythonfiles.state_high_high_low import probability_high_high_low
from pythonfiles.state_high_low_high import probability_high_low_high
from pythonfiles.state_high_low_low import probability_high_low_low
from pythonfiles.state_low_high_high import probability_low_high_high
from pythonfiles.state_low_high_low import probability_low_high_low
from pythonfiles.state_low_low_high import probability_low_low_high
from pythonfiles.state_low_low_low import probability_low_low_low


class MDP:
    # attributes definition of the class

    def __init__(self, state_list, initstates_list, elements, action_list, costs_dict):
        self.states = state_list
        self.initial_states_list = initstates_list
        self.agents = elements
        self.actions = action_list
        self.costs = costs_dict


class Traffic_Lights_MDP(MDP):

    def __init__(self, state_list, initstates_list, elements, action_list, costs_dict):
        super().__init__(state_list, initstates_list, elements, action_list, costs_dict)

    # METHODS DEFINITION: PROBABILITY CALCULATION OF STATES
    # assignment from external files:

        self.calculate_probability_HHH = probability_high_high_high()
        self.calculate_probability_HHL = probability_high_high_low()
        self.calculate_probability_HLH = probability_high_low_high()
        self.calculate_probability_HLL = probability_high_low_low()
        self.calculate_probability_LHH = probability_low_high_high()
        self.calculate_probability_LHL = probability_low_high_low()
        self.calculate_probability_LLH = probability_low_low_high()
        self.calculate_probability_LLL = probability_low_low_low()

    def BellMan_1(self):
        pass
    def BellMan_2(self):
        pass
    def BellMan_3(self):
        pass
    def BellMan_4(self):
        pass
    def BellMan_5(self):
        pass
    def BellMan_6(self):
        pass
    def BellMan_7(self):
        pass
    def BellMan_8(self):
        pass


#----------------MAIN PROGRAM--------------------------

my_states_list = ["High", "Low"]
my_init_states = ["High;High;High", "High;High;Low", "High;Low;High",
                  "High;Low;Low", "Low,High,High", "Low,High,Low",
                  "Low,Low,High", "Low,Low,Low"]
my_action_list = ["E", "W", "N"]
my_costs = {"C(E)": 3, "C(W)": 3, "C(N)": 3}

MyMDP = Traffic_Lights_MDP(my_states_list, my_init_states, 3, my_action_list, my_costs)

print(MyMDP.calculate_probability_HHH)
print(MyMDP.calculate_probability_HHL)
print(MyMDP.calculate_probability_HLH)
print(MyMDP.calculate_probability_HLL)
print(MyMDP.calculate_probability_LHH)
print(MyMDP.calculate_probability_LHL)
print(MyMDP.calculate_probability_LLH)
print(MyMDP.calculate_probability_LLL)


# METHODS DEFINITION: BELLMAN EQUATIONS AND OPTIMAL POLICY CALCULATION


