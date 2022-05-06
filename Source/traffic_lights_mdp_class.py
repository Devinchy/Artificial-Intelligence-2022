from Probability_methods.state_high_high_high import probability_high_high_high
from Probability_methods.state_high_high_low import probability_high_high_low
from Probability_methods.state_high_low_high import probability_high_low_high
from Probability_methods.state_high_low_low import probability_high_low_low
from Probability_methods.state_low_high_high import probability_low_high_high
from Probability_methods.state_low_high_low import probability_low_high_low
from Probability_methods.state_low_low_high import probability_low_low_high
from Probability_methods.state_low_low_low import probability_low_low_low


class Traffic_Lights_MDP:
    # attributes definition of the class

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

    #METHODS DEFINITION: BELLMAN EQUATIONS AND OPTIMAL POLICY CALCULATION
