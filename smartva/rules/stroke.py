from smartva.data.constants import *
from smartva.utils.utils import value_from_row, int_or_float

CAUSE_ID = 44


def logic_rule(row):
    value_of = value_from_row(row, int_or_float)

    stroke = value_of(Adult.STROKE) == YES
    
    paralysis_one_side = (value_of(Adult.PARALYSIS_RIGHT) == YES or
                          value_of(Adult.PARALYSIS_LEFT) == YES)

    any_paralysis = any([
        paralysis_one_side,
        value_of(Adult.PARALYSIS) == YES,
        value_of(Adult.PARALYSIS_LOWER) == YES,
        value_of(Adult.PARALYSIS_UPPER) == YES,
        value_of(Adult.PARALYSIS_ONE_LEG) == YES,
        value_of(Adult.PARALYSIS_ONE_ARM) == YES,
        value_of(Adult.PARALYSIS_WHOLE) == YES,
        value_of(Adult.PARALYSIS_OTHER) == YES,
    ])

    any_paralysis_or_stroke = any([
        stroke,
        any_paralysis
    ])

    # If AIDS or TB then not Stroke
    aids_or_tb = (value_of(Adult.AIDS) == YES or 
                  value_of(Adult.TUBERCULOSIS) == YES)

    # If Cancer then not Stroke
    cancer = ((value_of(Adult.PARALYSIS_UPPER) == YES and value_of(Adult.ULCER_IN_BREAST) == YES) or
              value_of(Adult.CANCER) == YES or
              value_of(Adult.LUMP_IN_NECK) == YES) 

    # If Ischemic Heart Disease then not Stroke
    ischemic_heart_disease = (stroke and value_of(Adult.CHEST_PAIN) == YES)

    # If Lost Consciousness and not Paralysis then not Stroke
    lost_consciousness = (value_of(Adult.LOST_CONSCIOUSNESS) == YES and !any_paralysis)


    #return ((stroke and paralysis_one_side) or
    #        (diabetes and any_paralysis_or_stroke) or
    #        (pneumonia and any_paralysis_or_stroke))





