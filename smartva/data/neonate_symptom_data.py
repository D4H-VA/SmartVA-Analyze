from smartva.data.common_data import NEONATE

AGE_GROUP = NEONATE
KEEP_PATTERN = r'(sid$|real|age$|sex$|cause$|restricted$|s\d+)'

GENERATED_VARS_DATA = {
    'age': 0,
    'sex': 0,
    's5': 0,
    's6': 0,
    's13': 0,
    's16': 0,
    's105': 0,
    's4991': 0,
    's4993': 0,
    's4994': 0,
    's8991': 0,
    's8992': 0,
    's11991': 0,
    's30991': 0,
    's46991': 0,
    's46992': 0,
    's49991': 0,
    's50991': 0,
    's51991': 0,
    's55991': 0,
    's56991': 0,
    's57991': 0,
    's58991': 0,
    's58992': 0,
    's58993': 0,
    's58994': 0,
    's69991': 0,
    's71991': 0,
    's76991': 0,
    'restricted': '',
}

VAR_CONVERSION_MAP = {
    'sid': 'sid',
    'g5_02': 'real_gender',
    'g5_04a': 'real_age',
    'g5_04b': 's3',
    'g5_04c': 'age',
    'c1_01': 's5_1',
    'c1_02': 's6_1',
    'c1_03': 's7',
    'c1_04': 's8',
    'c1_05': 's9',
    'c1_06a': 's11',
    'c1_07': 's13_1',
    'c1_08b': 's14',
    'c1_09': 's15',
    'c1_11': 's16_1',
    'c1_12': 's17',
    'c1_13': 's18',
    'c1_14': 's19',
    'c1_15': 's20',
    'c1_16': 's21',
    'c1_17': 's22',
    'c1_18': 's23',
    'c1_19_1': 's24',
    'c1_19_2': 's25',
    'c1_19_3': 's26',
    'c1_19_4a': 's27',
    'c1_20': 's28',
    'c1_21': 's29',
    'c1_22a': 's30',
    'c1_25': 's31',
    'c1_26': 's32',
    'c2_01_1': 's33',
    'c2_01_2': 's34',
    'c2_01_3': 's35',
    'c2_01_4': 's36',
    'c2_01_5': 's37',
    'c2_01_6': 's38',
    'c2_01_7': 's39',
    'c2_01_8': 's40',
    'c2_01_9': 's41',
    'c2_01_10': 's42',
    'c2_01_12': 's43',
    'c2_02': 's45',
    'c2_03': 's46',
    'c2_04': 's47',
    'c2_05': 's48',
    'c2_06': 's49',
    'c2_07': 's50',
    'c2_08a': 's51',
    'c2_09': 's52',
    'c2_10': 's53',
    'c2_11': 's54',
    'c2_12': 's55',
    'c2_13a': 's56',
    'c2_15a': 's57',
    'c2_17': 's58',
    'c2_18': 's59',
    'c3_01': 's60',
    'c3_02': 's61',
    'c3_03_1': 's62',
    'c3_03_2': 's63',
    'c3_03_3': 's64',
    'c3_04': 's65',
    'c3_05': 's66',
    'c3_06': 's67',
    'c3_07': 's68',
    'c3_08': 's69',
    'c3_09': 's70',
    'c3_10': 's71',
    'c3_11': 's72',
    'c3_12': 's73',
    'c3_13': 's74',
    'c3_14': 's75',
    'c3_15': 's76',
    'c3_16': 's77',
    'c3_17': 's78',
    'c3_18': 's79',
    'c3_19': 's80',
    'c3_20': 's81',
    'c3_21': 's82',
    'c3_22': 's83',
    'c3_23': 's84',
    'c3_24': 's85',
    'c3_25': 's86',
    'c3_26': 's87',
    'c3_27': 's88',
    'c3_28': 's89',
    'c3_29': 's90',
    'c3_30': 's91',
    'c3_31': 's92',
    'c3_32': 's93',
    'c3_33': 's94',
    'c3_34': 's95',
    'c3_35': 's96',
    'c3_36': 's97',
    'c3_37': 's98',
    'c3_38': 's99',
    'c3_39': 's100',
    'c3_40': 's101',
    'c3_41': 's102',
    'c3_42': 's103',
    'c3_44': 's104',
    'c3_45b': 's105_1',
    'c3_46': 's106',
    'c3_47': 's107',
    'c3_48': 's108',
    'c3_49': 's109',
    'c5_17': 's188',
    'c5_18': 's189',
    'c5_19': 's190',
    's180': 's180',
    's181': 's181',
}

# read -> write
COPY_VARS = {
    # 'real_age': 'age',
    'real_gender': 'sex',
    's62': 's24',
    's63': 's25',
    's64': 's26',
}

AGE_QUARTILE_BINARY_VARS = {
    'age': [
        (2, 's4994'),
        (0, 's4993'),
        (None, 's4991'),
    ],
    's105_1': [
        (1, 's105'),
    ]
}

DURATION_CUTOFF_DATA = {
    'age': 3,
    's9': 2,
    's14': 2500,
    's28': 2,
    's29': 3,
    's31': 3,
    's45': 255,
    's48': .125,
    's53': .2083333,
    's75': 2,
    's79': 2,
    's80': 2,
    's82': 2,
    's83': 2,
    's88': 3,
    's89': 2,
    's91': 3,
    's92': 2,
}

INJURY_VARS = {}

BINARY_CONVERSION_MAP = {
    's5_1': {
        2: 's5',
    },
    's6_1': {
        2: 's6',
        3: 's6',
    },
    's8': {
        1: 's8991',
        2: 's8992',
    },
    's11': {
        4: 's11991',
        5: 's11991',
    },
    's13_1': {
        1: 's13',
        2: 's13',
    },
    's16_1': {
        2: 's16',
    },
    's30': {
        3: 's30991',
        4: 's30991',
        5: 's30991',
    },
    's46': {
        1: 's46991',
        3: 's46992',
    },
    's49': {
        2: 's49991',
    },
    's50': {
        2: 's50991',
    },
    's51': {
        1: 's51991',
        3: 's51991',
    },
    # OK
    's55': {
        1: 's55991',
        2: 's55991',
    },
    's56': {
        1: 's56991', # hospital
        2: 's56991', # other health facility
    },
    's57': {
        # [3, 4, 5, 6, 8, 9]
        3: 's57991',
        4: 's57991',
        5: 's57991',
        6: 's57991',
        8: 's57991',
        9: 's57991',
    },
    's58': {
        1: 's58991',
        2: 's58992',
        3: 's58993',
        4: 's58994',
    },
    's69': {
        3: 's69991',
        4: 's69991',
    },
    's71': {
        2: 's71991',
    },
    's76': {
        2: 's76991',
    },
    'sex': [2]
}

BINARY_VARS = [
    'sex',
    's7',
    's13',
    's17',
    's18',
    's19',
    's20',
    's21',
    's22',
    's23',
    's24',
    's25',
    's26',
    's27',
    's33',
    's34',
    's35',
    's36',
    's37',
    's38',
    's39',
    's40',
    's41',
    's42',
    's43',
    's47',
    's52',
    's54',
    's59',
    's60',
    's61',
    's62',
    's63',
    's64',
    's65',
    's66',
    's67',
    's68',
    's70',
    's72',
    's73',
    's74',
    's77',
    's78',
    's81',
    's84',
    's85',
    's86',
    's87',
    's90',
    's93',
    's94',
    's95',
    's96',
    's97',
    's98',
    's99',
    's100',
    's101',
    's102',
    's103',
    's104',
    's106',
    's106',
    's107',
    's108',
    's109',
    's188',
    's189',
    's190',
]

DROP_LIST = [
    's2',
    's3',
    's4',  # Added
    's5_1',
    's6_1',
    's8',
    's11',
    's13_1',
    's16_1',
    's30',
    's46',
    's49',
    's50',
    's51',
    's55',
    's57',
    's58',
    's69',
    's71',
    's76',
    's105_1',
]

CENSORED_MAP = {
    1: [   #  Birth asphyxia
        's4994'     # age quartile 4
    ],
    3: [   # Meningitis/Sepsis
        's23',      # Was any part of the baby physically abnormal at time of delivery?
        's24',      # Abormalities: Head size very small at time of birth?
        's25',      # Abormalities: Head size very large at time of birth?
        's26',      # Abormalities: Mass defect on the back of head or spine
        's61',      # Was any part of the baby physically abnormal at time of delivery?
        's62',      # Abnormalities: Head size very small at time of birth?
        's63',      # Abnormalities: Head size very large at time of birth?
        's64',      # Abnormalities: Mass defect on the back of head or spine
    ],
    4: [   # Pneumonia
        's23',      # Was any part of the baby physically abnormal at time of delivery?
        's24',      # Abormalities: Head size very small at time of birth?
        's25',      # Abormalities: Head size very large at time of birth?
        's26',      # Abormalities: Mass defect on the back of head or spine
        's61',      # Was any part of the baby physically abnormal at time of delivery?
        's62',      # Abnormalities: Head size very small at time of birth?
        's63',      # Abnormalities: Head size very large at time of birth?
        's64',      # Abnormalities: Mass defect on the back of head or spine
    ],
    6: [   # Stillbirth
        # Age censoring redundant with requiring s4991
        'age',      # Age: cutoff > 3 days
        's4993',    # Age quartile 3
        's4994',    # Age quartile 4
    ]
}

REQUIRED_MAP = {
    6: [
        's4991',    # Age quartile: Age == 0 days
    ]
}
