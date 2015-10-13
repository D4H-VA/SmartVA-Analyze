# new headers generated by this step in processing
GENERATED_HEADERS_DATA = [
    ('g4_03b', 0),
    ('a2_01b', 0),
    ('a2_22b', 0),
    ('a2_24b', 0),
    ('a2_26b', 0),
    ('a2_28b', 0),
    ('a2_33b', 0),
    ('a2_37b', 0),
    ('a2_41b', 0),
    ('a2_54b', 0),
    ('a2_58b', 0),
    ('a2_62b', 0),
    ('a2_65b', 0),
    ('a2_68b', 0),
    ('a2_70b', 0),
    ('a2_73b', 0),
    ('a2_76b', 0),
    ('a2_79b', 0),
    ('a2_83b', 0),
    ('a2_86b', 0),
    ('a4_02_1', 0),
    ('a4_02_2', 0),
    ('a4_02_3', 0),
    ('a4_02_4', 0),
    ('a4_02_5a', 0),
    ('a4_02_6', 0),
    ('a4_02_7', 0),
    ('a5_01_8', 0),
    ('a5_04b', ''),
    ('a6_02_1', 0),
    ('a6_02_2', 0),
    ('a6_02_3', 0),
    ('a6_02_4', 0),
    ('a6_02_5', 0),
    ('a6_02_6', 0),
    ('a6_02_8', 0),
    ('a6_02_9', 0),
    ('a6_02_10', 0),
    ('a6_02_11', 0),
    ('a6_02_12a', 0),
    ('a6_02_13', 0),
    ('a6_02_14', 0),
    ('a6_02_15', 0),
]

"""
Consolidation maps use the format:
    (read_header, write_header): {
        VAL: data_header
    }
"""
CONSOLIDATION_MAP = {
    ('g4_03a', 'g4_03b'): {
        11: 'gen_4_3a',
        12: 'gen_4_3b',
        13: 'gen_4_3c',
    },
    ('a2_01a', 'a2_01b'): {
        1: 'adult_2_1a',
        2: 'adult_2_1b',
        4: 'adult_2_1c',
        5: 'adult_2_1d',
    },
    ('a2_22a', 'a2_22b'): {
        4: 'adult_2_22a',
        2: 'adult_2_22b',
    },
    ('a2_24a', 'a2_24b'): {
        4: 'adult_2_24a',
        2: 'adult_2_24b',
    },
    ('a2_26a', 'a2_26b'): {
        4: 'adult_2_26a',
        2: 'adult_2_26b',
    },
    ('a2_28a', 'a2_28b'): {
        4: 'adult_2_28a',
        2: 'adult_2_28b',
    },
    ('a2_33a', 'a2_33b'): {
        4: 'adult_2_33a',
        2: 'adult_2_33b',
    },
    ('a2_37a', 'a2_37b'): {
        4: 'adult_2_37a',
        2: 'adult_2_37b',
    },
    ('a2_41a', 'a2_41b'): {
        4: 'adult_2_41a',
        2: 'adult_2_41b',
    },
    ('a2_54a', 'a2_54b'): {
        5: 'adult_2_54a',
        4: 'adult_2_54b',
    },
    ('a2_58a', 'a2_58b'): {
        4: 'adult_2_58a',
        2: 'adult_2_58b',
    },
    ('a2_62a', 'a2_62b'): {
        5: 'adult_2_62a',
        4: 'adult_2_62b',
        2: 'adult_2_62c',
    },
    ('a2_65a', 'a2_65b'): {
        4: 'adult_2_65a',
        2: 'adult_2_65b',
    },
    ('a2_68a', 'a2_68b'): {
        4: 'adult_2_68a',
        2: 'adult_2_68b',
    },
    ('a2_70a', 'a2_70b'): {
        5: 'adult_2_70a',
        4: 'adult_2_70b',
    },
    ('a2_73a', 'a2_73b'): {
        4: 'adult_2_73a',
        2: 'adult_2_73b',
    },
    ('a2_76a', 'a2_76b'): {
        4: 'adult_2_76a',
        2: 'adult_2_76b',
    },
    ('a2_79a', 'a2_79b'): {
        4: 'adult_2_79a',
        2: 'adult_2_79b',
    },
    ('a2_83a', 'a2_83b'): {
        6: 'adult_2_83a',
        5: 'adult_2_83b',
    },
    ('a2_86a', 'a2_86b'): {
        4: 'adult_2_86a',
        2: 'adult_2_86b',
        1: 'adult_2_86c',
    },
    ('a5_04a', 'a5_04b'): {
        5: 'adult_5_5a',
        4: 'adult_5_5b',
        2: 'adult_5_5c',
        1: 'adult_5_5d',
    },
}

BINARY_CONVERSION_MAP = {
    'a4_02': {
        # old header: adult_4_2
        1: 'a4_02_1',
        2: 'a4_02_2',
        3: 'a4_02_3',
        4: 'a4_02_4',
        11: 'a4_02_5a',
        8: 'a4_02_6',
        9: 'a4_02_7',
    },
    'adult_5_1': {
        # tricky
        0: 'a5_01_8',
    },
    'adult_6_2': {
        # old header: converted
        1: 'a6_02_1',
        2: 'a6_02_2',
        3: 'a6_02_3',
        4: 'a6_02_4',
        5: 'a6_02_5',
        6: 'a6_02_6',
        7: 'a6_02_8',
        8: 'a6_02_9',
        9: 'a6_02_10',
        10: 'a6_02_11',
        11: 'a6_02_12a',
        12: 'a6_02_13',
        88: 'a6_02_14',
        99: 'a6_02_15',
    }
}

"""
Verify that answers are appropriate given answers to previous questions.
Format:
    (answer condition, [list of dependent questions])

Answer condition format:
    (h1=value)     # Data at header must equal value
    (!(h1=value))  # Data at header must not equal value
    (&(h1=value)(h2=value))  # Data at header 1 and header 2 must equal value.
    (|(h1=value)(h2=value))  # Data at header 1 or header 2 must equal value.

"""
SKIP_PATTERN_DATA = [
    ('(a2_02=1)', ['a2_03a', 'a2_03b', 'a2_04', 'a2_05', 'a2_06']),
    ('(a2_07=1)', ['a2_08a', 'a2_08b', 'a2_09_1a', 'a2_09_1b', 'a2_09_2a']),
    ('(a2_10=1)', ['a2_11']),
    ('(a2_13=1)', ['a2_14']),
    ('(a2_14=1)', ['a2_15a', 'a2_15b']),
    ('(a2_18=1)', ['a2_19']),
    ('(a2_21=1)', ['a2_22a', 'a2_22b']),
    ('(a2_23=1)', ['a2_24a', 'a2_24b']),
    ('(a2_25=1)', ['a2_26a', 'a2_26b']),
    ('(a2_27=1)', ['a2_28a', 'a2_28b']),
    ('(a2_32=1)', ['a2_33a', 'a2_33b', 'a2_34', 'a2_35']),
    ('(a2_36=1)', ['a2_37a', 'a2_37b', 'a2_38', 'a2_39_1']),
    ('(a2_40=1)', ['a2_41a', 'a2_41b']),
    ('(a2_43=1)', ['a2_44', 'a2_45', 'a2_46a', 'a2_46b']),
    ('(a2_47=1)', ['a2_48a', 'a2_48b']),
    ('(a2_50=1)', ['a2_51']),
    ('(a2_53=1)', ['a2_54a', 'a2_54b', 'a2_55', 'a2_56']),
    ('(a2_57=1)', ['a2_58a', 'a2_58b', 'a2_59']),
    ('(a2_61=1)', ['a2_62a', 'a2_62b', 'a2_63_1']),
    ('(a2_64=1)', ['a2_65a', 'a2_65b', 'a2_66']),
    ('(a2_67=1)', ['a2_68a', 'a2_68b']),
    ('(a2_69=1)', ['a2_70a', 'a2_70b', 'a2_71']),
    ('(a2_72=1)', ['a2_73a', 'a2_73b']),
    ('(a2_74=1)', ['a2_76a', 'a2_76b', 'a2_75', 'a2_77']),
    ('(a2_78=1)', ['a2_79a', 'a2_79b', 'a2_80']),
    ('(a2_82=1)', ['a2_83a', 'a2_83b', 'a2_84']),
    ('(a2_85=1)', ['a2_86a', 'a2_86b', 'a2_87_1', 'a2_87_10a', 'a2_87_10b', 'a2_87_2', 'a2_87_3', 'a2_87_4', 'a2_87_5', 'a2_87_6', 'a2_87_7', 'a2_87_8', 'a2_87_9']),
    ('(a4_01=1)', ['a4_02_1', 'a4_02_2', 'a4_02_3', 'a4_02_4', 'a4_02_5a', 'a4_02_5b', 'a4_02_6', 'a4_02_7']),
    ('(a4_02_1=1)', ['a4_04']),
    ('(a4_05=1)', ['a4_06']),
    ('(!(a5_01_8=1))', ['a5_04a', 'a5_04b', 'a5_02', 'a5_03']),
    ('(!(a5_02=1))', ['a5_03']),
    ('(a6_01=1)', ['a6_02_1', 'a6_02_2', 'a6_02_3', 'a6_02_4', 'a6_02_5', 'a6_02_6', 'a6_02_8', 'a6_02_9', 'a6_02_10', 'a6_02_11', 'a6_02_12a', 'a6_02_13', 'a6_02_14', 'a6_02_15', 'a6_03']),
    ('(a6_04=1)', ['a6_05']),
    ('(a6_05=1)', ['a6_06_1d', 'a6_06_1m', 'a6_06_1y', 'a6_06_2d', 'a6_06_2m', 'a6_06_2y', 'a6_07d', 'a6_07m', 'a6_07y', 'a6_08']),
    ('(a6_09=1)', ['a6_10']),
    ('(a6_10=1)', ['a6_11', 'a6_12', 'a6_13', 'a6_14', 'a6_15']),
    ('(g5_02=2)', ['a3_01', 'a3_02', 'a3_03']),
    ('(&(g5_02=2)(!(a3_03=1)))', ['a3_05', 'a3_06', 'a3_07', 'a3_10']),
    ('(a3_07=1)', ['a3_08a', 'a3_08b', 'a3_09']),
    ('(a3_10=1)', ['a3_11a', 'a3_11b', 'a3_12']),
    ('(&(g5_02=2)(!(a3_03=1))(a3_10=1)(!(a3_12=1)))', ['a3_13', 'a3_14', 'a3_15', 'a3_16a', 'a3_16b']),
    ('(&(g5_02=2)(!(a3_03=1))(!(a3_12=1))(!(a3_15=1)))', ['a3_17']),
    ('(&(g5_02=2)(!(a3_03=1))(!(a3_12=1))(!(a3_15=1))(!(a3_17=1)))', ['a3_18']),
    ('(|(&(g5_02=2)(a3_03=0)(!(a3_15=1))(a3_18=1))(a3_17=1))', ['a3_19', 'a3_20']),
    ('(a3_03=1)', ['a3_04']),
    ('(g5_04a>=12)', ['g5_05']),  # Really for child modules
    ('(&(a4_01=1)(|(a4_02_2=1)(a4_02_3=1)(a4_02_4=1)(a4_02_5a=1)))', ['a4_03']),
]

SHORT_FORM_FREE_TEXT_CONVERSION = {
    'a_7_1': 'kidney',
    'a_7_2': 'dialysis',
    'a_7_3': 'fever',
    'a_7_4': 'ami',
    'a_7_5': 'heart',
    'a_7_6': 'jaundice',
    'a_7_7': 'liver',
    'a_7_8': 'malaria',
    'a_7_9': 'pneumonia',
    'a_7_10': 'renal',
    'a_7_11': 'suicide',
}

FREE_TEXT_HEADERS = [
    'a5_01_9b',
    'a6_08',
    'a6_11',
    'a6_12',
    'a6_13',
    'a6_14',
    'a6_15',
    'a7_01',
]

TIME_FACTORS = {
    1: 356.0,
    2: 30.0,
    3: 7.0,
    4: 1.0,
    5: 1 / 24.0,
    6: 1 / 1440.0
}

DURATION_VARS = [
    'a2_01',
    'a2_03',
    'a2_08',
    'a2_15',
    'a2_22',
    'a2_24',
    'a2_26',
    'a2_28',
    'a2_33',
    'a2_37',
    'a2_41',
    'a2_48',
    'a2_54',
    'a2_58',
    'a2_62',
    'a2_65',
    'a2_68',
    'a2_70',
    'a2_73',
    'a2_76',
    'a2_79',
    'a2_83',
    'a2_86',
    'a3_08',
    'a3_11',
    'a3_16',
    'a5_04'
]

DURATION_VARS_SHORT_FORM_DROP_LIST = [
    'a3_16',
]

DURATION_VARS_SPECIAL_CASE = {
    'a5_04': 999
}