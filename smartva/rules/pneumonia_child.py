from smartva.data.constants import *
from smartva.utils.utils import value_from_row, int_or_float

CAUSE_ID = 17  # Pneumonia

def logic_rule(row):
    value_of = value_from_row(row, int_or_float)

    pneumonia_cough = any([
        value_of(Child.FREE_TEXT_PNEUMONIA) == YES,
        value_of(Child.COUGH) == YES,
    ])
    
    breathing_difficulties = any([
        value_of(Child.BREATHING_DIFFICULT) == YES,
        value_of(Child.FAST_BREATHING) == YES, 
        value_of(Child.GRUNTING) == YES,
    ])

    return pneumonia_cough and breathing_difficulties
    