from Probability_methods.state_high_high_high import probability_high_high_high
from Probability_methods.state_high_high_low import probability_high_high_low
from Probability_methods.state_high_low_high import probability_high_low_high
from Probability_methods.state_high_low_low import probability_high_low_low
from Probability_methods.state_low_high_high import probability_low_high_high
from Probability_methods.state_low_high_low import probability_low_high_low
from Probability_methods.state_low_low_high import probability_low_low_high
from Probability_methods.state_low_low_low import probability_low_low_low


class MDP:
    # attributes definition of the class

    def __init__(self,my_data, state_list, initstates_list, elements, action_list, costs_dict):

        self.data_file = my_data
        self.states = state_list
        self.initial_states_list = initstates_list
        self.agents = elements
        self.actions = action_list
        self.costs = costs_dict

class Traffic_Lights_MDP(MDP):

    def __init__(self, my_data, state_list, initstates_list, elements, action_list, costs_dict):
        super().__init__(my_data, state_list, initstates_list, elements, action_list, costs_dict)

        self.probabilities

    # METHODS DEFINITION: PROBABILITY CALCULATION OF STATES
    # assignment from external files:

    calculate_probability_HHH = probability_high_high_high()
    calculate_probability_HHL = probability_high_high_low()
    calculate_probability_HLH = probability_high_low_high()
    calculate_probability_HLL = probability_high_low_low()
    calculate_probability_LHH = probability_low_high_high()
    calculate_probability_LHL = probability_low_high_low()
    calculate_probability_LLH = probability_low_low_high()
    calculate_probability_LLL = probability_low_low_low()

    def calculate_all_probabilities(self):

        self.probabilities.update({})

    #METHODS DEFINITION: BELLMAN EQUATIONS AND OPTIMAL POLICY CALCULATION
