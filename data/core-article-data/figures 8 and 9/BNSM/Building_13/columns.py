import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 24563224.2069678, 10234676.75290325, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 43.2630652, 0.00064275, 50.62437659, 0.0100007, 5.06243766, 0.02404344, -43.2630652, -0.00064275, -50.62437659, -0.0100007, -5.06243766, -0.02404344, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 41.81213273, 0.00064275, 48.92656457, 0.0100007, 4.89265646, 0.02404344, -41.81213273, -0.00064275, -48.92656457, -0.0100007, -4.89265646, -0.02404344, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 74.14460045, 0.01285499, 74.14460045, 0.03856497, 51.90122031, -1078.91209574, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 18.53615011, 0.00010084, 55.60845033, 0.00030253, 185.36150112, 0.00100843, -18.53615011, -0.00010084, -55.60845033, -0.00030253, -185.36150112, -0.00100843, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 74.14460045, 0.01285499, 74.14460045, 0.03856497, 51.90122031, -1078.91209574, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 18.53615011, 0.00010084, 55.60845033, 0.00030253, 185.36150112, 0.00100843, -18.53615011, -0.00010084, -55.60845033, -0.00030253, -185.36150112, -0.00100843, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 5.3, 0.0, 0.0)
    ops.node(121002, 5.3, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.1575, 27810128.47716095, 11587553.5321504, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 139.35878083, 0.00065536, 166.91529809, 0.01017137, 16.69152981, 0.03255086, -139.35878083, -0.00065536, -166.91529809, -0.01017137, -16.69152981, -0.03255086, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 158.85293667, 0.00056744, 190.26418801, 0.01082555, 19.0264188, 0.03756855, -158.85293667, -0.00056744, -190.26418801, -0.01082555, -19.0264188, -0.03756855, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 151.56882174, 0.01310725, 151.56882174, 0.03932175, 106.09817522, -1531.83178573, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 37.89220543, 7.225e-05, 113.6766163, 0.00021676, 378.92205435, 0.00072253, -37.89220543, -7.225e-05, -113.6766163, -0.00021676, -378.92205435, -0.00072253, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 159.85107882, 0.01134876, 159.85107882, 0.03404628, 111.89575517, -1699.78782558, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 39.9627697, 7.62e-05, 119.88830911, 0.0002286, 399.62769705, 0.00076201, -39.9627697, -7.62e-05, -119.88830911, -0.0002286, -399.62769705, -0.00076201, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 18.75, 0.0, 0.0)
    ops.node(121005, 18.75, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.1575, 27334274.68746622, 11389281.11977759, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 136.53542926, 0.00063917, 163.50786634, 0.01036226, 16.35078663, 0.03188511, -136.53542926, -0.00063917, -163.50786634, -0.01036226, -16.35078663, -0.03188511, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 155.71818391, 0.00055499, 186.48015493, 0.01103633, 18.64801549, 0.03675568, -155.71818391, -0.00055499, -186.48015493, -0.01103633, -18.64801549, -0.03675568, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 150.56110455, 0.01278349, 150.56110455, 0.03835046, 105.39277318, -1558.85041825, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 37.64027614, 7.302e-05, 112.92082841, 0.00021907, 376.40276137, 0.00073022, -37.64027614, -7.302e-05, -112.92082841, -0.00021907, -376.40276137, -0.00073022, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 159.23248625, 0.01109984, 159.23248625, 0.03329951, 111.46274037, -1736.41623938, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 39.80812156, 7.723e-05, 119.42436468, 0.00023168, 398.08121561, 0.00077228, -39.80812156, -7.723e-05, -119.42436468, -0.00023168, -398.08121561, -0.00077228, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 24.05, 0.0, 0.0)
    ops.node(121006, 24.05, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.0625, 27271838.44193284, 11363266.01747202, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 61.35649844, 0.0008998, 72.49930671, 0.01248367, 7.24993067, 0.03472291, -61.35649844, -0.0008998, -72.49930671, -0.01248367, -7.24993067, -0.03472291, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 58.50973633, 0.0008998, 69.13555087, 0.01248367, 6.91355509, 0.03472291, -58.50973633, -0.0008998, -69.13555087, -0.01248367, -6.91355509, -0.03472291, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 80.92976395, 0.01799594, 80.92976395, 0.05398783, 56.65083477, -1101.68058066, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 20.23244099, 9.914e-05, 60.69732296, 0.00029742, 202.32440988, 0.00099139, -20.23244099, -9.914e-05, -60.69732296, -0.00029742, -202.32440988, -0.00099139, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 80.92976395, 0.01799594, 80.92976395, 0.05398783, 56.65083477, -1101.68058066, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 20.23244099, 9.914e-05, 60.69732296, 0.00029742, 202.32440988, 0.00099139, -20.23244099, -9.914e-05, -60.69732296, -0.00029742, -202.32440988, -0.00099139, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.25, 0.0)
    ops.node(121007, 0.0, 4.25, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.14, 26885105.66811134, 11202127.36171306, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 157.14266978, 0.00062302, 187.70714529, 0.011265, 18.77071453, 0.03154314, -157.14266978, -0.00062302, -187.70714529, -0.011265, -18.77071453, -0.03154314, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 159.38378516, 0.00067803, 190.38416084, 0.01091939, 19.03841608, 0.0294333, -159.38378516, -0.00067803, -190.38416084, -0.01091939, -19.03841608, -0.0294333, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 135.54821033, 0.01246048, 135.54821033, 0.03738143, 94.88374723, -1475.53598564, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 33.88705258, 7.519e-05, 101.66115774, 0.00022558, 338.87052582, 0.00075194, -33.88705258, -7.519e-05, -101.66115774, -0.00022558, -338.87052582, -0.00075194, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 132.10001346, 0.01356059, 132.10001346, 0.04068176, 92.47000942, -1408.45191816, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 33.02500336, 7.328e-05, 99.07501009, 0.00021984, 330.25003364, 0.00073281, -33.02500336, -7.328e-05, -99.07501009, -0.00021984, -330.25003364, -0.00073281, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 5.3, 4.25, 0.0)
    ops.node(121008, 5.3, 4.25, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.2475, 26269377.68789311, 10945574.03662213, 0.00841652, 0.00459422, 0.00686297, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 347.55277696, 0.00052272, 418.08436462, 0.00999928, 41.80843646, 0.02706376, -347.55277696, -0.00052272, -418.08436462, -0.00999928, -41.80843646, -0.02706376, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 357.55919284, 0.00056912, 430.12146029, 0.00962053, 43.01214603, 0.02492456, -357.55919284, -0.00056912, -430.12146029, -0.00962053, -43.01214603, -0.02492456, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 233.96350586, 0.01045437, 233.96350586, 0.03136312, 163.7744541, -1794.4392672, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 58.49087646, 7.514e-05, 175.47262939, 0.00022541, 584.90876465, 0.00075137, -58.49087646, -7.514e-05, -175.47262939, -0.00022541, -584.90876465, -0.00075137, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 192.58460237, 0.01138244, 192.58460237, 0.03414731, 134.80922166, -1692.4486842, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 48.14615059, 6.185e-05, 144.43845178, 0.00018554, 481.46150593, 0.00061848, -48.14615059, -6.185e-05, -144.43845178, -0.00018554, -481.46150593, -0.00061848, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 10.6, 4.25, 0.0)
    ops.node(121009, 10.6, 4.25, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.2, 28110010.77032863, 11712504.48763693, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 263.20785692, 0.00054462, 316.05256393, 0.01321703, 31.60525639, 0.03684461, -263.20785692, -0.00054462, -316.05256393, -0.01321703, -31.60525639, -0.03684461, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 267.59843197, 0.00060659, 321.32464249, 0.01253843, 32.13246425, 0.03302104, -267.59843197, -0.00060659, -321.32464249, -0.01253843, -32.13246425, -0.03302104, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 207.24414036, 0.01089233, 207.24414036, 0.03267699, 145.07089825, -1868.1419904, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 51.81103509, 7.697e-05, 155.43310527, 0.00023091, 518.11035091, 0.0007697, -51.81103509, -7.697e-05, -155.43310527, -0.00023091, -518.11035091, -0.0007697, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 183.56674245, 0.01213182, 183.56674245, 0.03639545, 128.49671972, -1707.01900567, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 45.89168561, 6.818e-05, 137.67505684, 0.00020453, 458.91685613, 0.00068176, -45.89168561, -6.818e-05, -137.67505684, -0.00020453, -458.91685613, -0.00068176, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 13.45, 4.25, 0.0)
    ops.node(121010, 13.45, 4.25, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.2, 26746085.64158459, 11144202.35066025, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 254.87666426, 0.00053864, 306.00760484, 0.01186416, 30.60076048, 0.03321711, -254.87666426, -0.00053864, -306.00760484, -0.01186416, -30.60076048, -0.03321711, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 258.14498832, 0.00060025, 309.93158909, 0.01126392, 30.99315891, 0.02977465, -258.14498832, -0.00060025, -309.93158909, -0.01126392, -30.99315891, -0.02977465, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 193.45779331, 0.01077276, 193.45779331, 0.03231828, 135.42045531, -1777.3812049, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 48.36444833, 7.551e-05, 145.09334498, 0.00022654, 483.64448327, 0.00075514, -48.36444833, -7.551e-05, -145.09334498, -0.00022654, -483.64448327, -0.00075514, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 171.54675046, 0.01200491, 171.54675046, 0.03601473, 120.08272532, -1637.47119835, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 42.88668761, 6.696e-05, 128.66006284, 0.00020088, 428.86687615, 0.00066961, -42.88668761, -6.696e-05, -128.66006284, -0.00020088, -428.86687615, -0.00066961, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 18.75, 4.25, 0.0)
    ops.node(121011, 18.75, 4.25, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2475, 26590806.84649917, 11079502.85270799, 0.00841652, 0.00459422, 0.00686297, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 340.72701987, 0.00051653, 409.93209368, 0.01096612, 40.99320937, 0.0284674, -340.72701987, -0.00051653, -409.93209368, -0.01096612, -40.99320937, -0.0284674, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 348.08174587, 0.00056246, 418.78063826, 0.01054324, 41.87806383, 0.02623901, -348.08174587, -0.00056246, -418.78063826, -0.01054324, -41.87806383, -0.02623901, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 237.28188512, 0.01033052, 237.28188512, 0.03099156, 166.09731958, -1802.36449193, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 59.32047128, 7.528e-05, 177.96141384, 0.00022584, 593.2047128, 0.00075282, -59.32047128, -7.528e-05, -177.96141384, -0.00022584, -593.2047128, -0.00075282, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 195.31613784, 0.01124912, 195.31613784, 0.03374737, 136.72129649, -1698.74489711, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 48.82903446, 6.197e-05, 146.48710338, 0.0001859, 488.2903446, 0.00061967, -48.82903446, -6.197e-05, -146.48710338, -0.0001859, -488.2903446, -0.00061967, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 24.05, 4.25, 0.0)
    ops.node(121012, 24.05, 4.25, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.14, 28118265.11555659, 11715943.79814858, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 154.8920876, 0.00059649, 185.16387892, 0.01336893, 18.51638789, 0.03604596, -154.8920876, -0.00059649, -185.16387892, -0.01336893, -18.51638789, -0.03604596, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 157.31077362, 0.00064638, 188.05526797, 0.012938, 18.8055268, 0.03364209, -157.31077362, -0.00064638, -188.05526797, -0.012938, -18.8055268, -0.03364209, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 147.49991727, 0.01192975, 147.49991727, 0.03578924, 103.24994209, -1604.64724925, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 36.87497932, 7.824e-05, 110.62493795, 0.00023471, 368.74979316, 0.00078236, -36.87497932, -7.824e-05, -110.62493795, -0.00023471, -368.74979316, -0.00078236, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 143.2488946, 0.01292752, 143.2488946, 0.03878255, 100.27422622, -1518.58468107, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 35.81222365, 7.598e-05, 107.43667095, 0.00022794, 358.12223651, 0.00075981, -35.81222365, -7.598e-05, -107.43667095, -0.00022794, -358.12223651, -0.00075981, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 8.5, 0.0)
    ops.node(121013, 0.0, 8.5, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.14, 27724003.17264619, 11551667.98860258, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 156.63560284, 0.00061944, 187.22219238, 0.01203816, 18.72221924, 0.03396986, -156.63560284, -0.00061944, -187.22219238, -0.01203816, -18.72221924, -0.03396986, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 158.16690442, 0.00067447, 189.05251468, 0.01166333, 18.90525147, 0.03168693, -158.16690442, -0.00067447, -189.05251468, -0.01166333, -18.90525147, -0.03168693, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 142.58074301, 0.01238886, 142.58074301, 0.03716657, 99.80652011, -1540.83156305, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 35.64518575, 7.67e-05, 106.93555726, 0.00023011, 356.45185753, 0.00076702, -35.64518575, -7.67e-05, -106.93555726, -0.00023011, -356.45185753, -0.00076702, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 138.72232589, 0.01348941, 138.72232589, 0.04046822, 97.10562812, -1464.20858847, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 34.68058147, 7.463e-05, 104.04174442, 0.00022388, 346.80581473, 0.00074626, -34.68058147, -7.463e-05, -104.04174442, -0.00022388, -346.80581473, -0.00074626, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 5.3, 8.5, 0.0)
    ops.node(121014, 5.3, 8.5, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.2475, 25831942.59450376, 10763309.41437657, 0.00841652, 0.00459422, 0.00686297, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 335.70379084, 0.00051219, 403.70906078, 0.01063492, 40.37090608, 0.02708569, -335.70379084, -0.00051219, -403.70906078, -0.01063492, -40.37090608, -0.02708569, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 343.67688852, 0.00055704, 413.29731049, 0.01022563, 41.32973105, 0.02497927, -343.67688852, -0.00055704, -413.29731049, -0.01022563, -41.32973105, -0.02497927, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 232.6069367, 0.01024372, 232.6069367, 0.03073116, 162.82485569, -1843.82331161, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 58.15173417, 7.597e-05, 174.45520252, 0.0002279, 581.51734174, 0.00075966, -58.15173417, -7.597e-05, -174.45520252, -0.0002279, -581.51734174, -0.00075966, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 191.45237379, 0.01114081, 191.45237379, 0.03342244, 134.01666165, -1731.64680805, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 47.86309345, 6.253e-05, 143.58928034, 0.00018758, 478.63093447, 0.00062526, -47.86309345, -6.253e-05, -143.58928034, -0.00018758, -478.63093447, -0.00062526, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 10.6, 8.5, 0.0)
    ops.node(121015, 10.6, 8.5, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.1575, 27659086.01206975, 11524619.17169573, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 190.49098725, 0.00056979, 228.2257882, 0.01167553, 22.82257882, 0.03509224, -190.49098725, -0.00056979, -228.2257882, -0.01167553, -22.82257882, -0.03509224, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 176.40948675, 0.00065888, 211.35485065, 0.01100573, 21.13548506, 0.03080319, -176.40948675, -0.00065888, -211.35485065, -0.01100573, -21.13548506, -0.03080319, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 152.08999569, 0.01139588, 152.08999569, 0.03418764, 106.46299699, -1554.62995737, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 38.02249892, 7.29e-05, 114.06749677, 0.00021869, 380.22498924, 0.00072898, -38.02249892, -7.29e-05, -114.06749677, -0.00021869, -380.22498924, -0.00072898, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 145.23716704, 0.01317754, 145.23716704, 0.03953262, 101.66601693, -1420.29468834, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 36.30929176, 6.961e-05, 108.92787528, 0.00020884, 363.09291761, 0.00069613, -36.30929176, -6.961e-05, -108.92787528, -0.00020884, -363.09291761, -0.00069613, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 13.45, 8.5, 0.0)
    ops.node(121016, 13.45, 8.5, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1575, 26153874.46889042, 10897447.69537101, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 190.40258962, 0.00057212, 227.86743972, 0.01181707, 22.78674397, 0.03226421, -190.40258962, -0.00057212, -227.86743972, -0.01181707, -22.78674397, -0.03226421, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 177.90686337, 0.00066025, 212.91297322, 0.0111368, 21.29129732, 0.02842367, -177.90686337, -0.00066025, -212.91297322, -0.0111368, -21.29129732, -0.02842367, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 146.26835219, 0.01144243, 146.26835219, 0.03432728, 102.38784654, -1586.5140302, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 36.56708805, 7.414e-05, 109.70126415, 0.00022243, 365.67088048, 0.00074142, -36.56708805, -7.414e-05, -109.70126415, -0.00022243, -365.67088048, -0.00074142, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 139.06385787, 0.01320498, 139.06385787, 0.03961495, 97.34470051, -1443.97537358, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 34.76596447, 7.049e-05, 104.2978934, 0.00021147, 347.65964467, 0.0007049, -34.76596447, -7.049e-05, -104.2978934, -0.00021147, -347.65964467, -0.0007049, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 18.75, 8.5, 0.0)
    ops.node(121017, 18.75, 8.5, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.2475, 28943108.3151231, 12059628.46463462, 0.00841652, 0.00459422, 0.00686297, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 351.07664918, 0.00051286, 422.06832194, 0.01033675, 42.20683219, 0.03067803, -351.07664918, -0.00051286, -422.06832194, -0.01033675, -42.20683219, -0.03067803, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 360.57384147, 0.00055641, 433.48595402, 0.00993955, 43.3485954, 0.02818234, -360.57384147, -0.00055641, -433.48595402, -0.00993955, -43.3485954, -0.02818234, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 257.35148736, 0.01025729, 257.35148736, 0.03077186, 180.14604115, -1770.68763215, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 64.33787184, 7.501e-05, 193.01361552, 0.00022504, 643.3787184, 0.00075013, -64.33787184, -7.501e-05, -193.01361552, -0.00022504, -643.3787184, -0.00075013, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 211.86020366, 0.01112825, 211.86020366, 0.03338476, 148.30214256, -1673.56596472, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 52.96505091, 6.175e-05, 158.89515274, 0.00018526, 529.65050915, 0.00061753, -52.96505091, -6.175e-05, -158.89515274, -0.00018526, -529.65050915, -0.00061753, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 24.05, 8.5, 0.0)
    ops.node(121018, 24.05, 8.5, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.14, 29403977.48437407, 12251657.28515586, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 156.51342993, 0.00060911, 187.06217727, 0.01270792, 18.70621773, 0.03767017, -156.51342993, -0.00060911, -187.06217727, -0.01270792, -18.70621773, -0.03767017, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 157.45879214, 0.00066261, 188.19205804, 0.01230596, 18.8192058, 0.03509645, -157.45879214, -0.00066261, -188.19205804, -0.01230596, -18.8192058, -0.03509645, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 149.52630994, 0.01218222, 149.52630994, 0.03654665, 104.66841696, -1526.74829534, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 37.38157749, 7.584e-05, 112.14473246, 0.00022753, 373.81577485, 0.00075843, -37.38157749, -7.584e-05, -112.14473246, -0.00022753, -373.81577485, -0.00075843, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 145.75562454, 0.01325225, 145.75562454, 0.03975676, 102.02893718, -1452.19321013, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 36.43890614, 7.393e-05, 109.31671841, 0.00022179, 364.38906136, 0.0007393, -36.43890614, -7.393e-05, -109.31671841, -0.00022179, -364.38906136, -0.0007393, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 12.75, 0.0)
    ops.node(121019, 0.0, 12.75, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.0625, 27578734.12184899, 11491139.21743708, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 64.32125912, 0.00093051, 76.04963487, 0.01093092, 7.60496349, 0.03408583, -64.32125912, -0.00093051, -76.04963487, -0.01093092, -7.60496349, -0.03408583, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 61.17931146, 0.00093051, 72.33478264, 0.01093092, 7.23347826, 0.03408583, -61.17931146, -0.00093051, -72.33478264, -0.01093092, -7.23347826, -0.03408583, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 76.68784145, 0.01861019, 76.68784145, 0.05583058, 53.68148902, -1015.8327783, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 19.17196036, 9.29e-05, 57.51588109, 0.00027869, 191.71960363, 0.00092897, -19.17196036, -9.29e-05, -57.51588109, -0.00027869, -191.71960363, -0.00092897, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 76.68784145, 0.01861019, 76.68784145, 0.05583058, 53.68148902, -1015.8327783, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 19.17196036, 9.29e-05, 57.51588109, 0.00027869, 191.71960363, 0.00092897, -19.17196036, -9.29e-05, -57.51588109, -0.00027869, -191.71960363, -0.00092897, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 5.3, 12.75, 0.0)
    ops.node(121020, 5.3, 12.75, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.14, 29347858.64705681, 12228274.43627367, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 137.92414172, 0.00067668, 164.76000558, 0.01012503, 16.47600056, 0.03246446, -137.92414172, -0.00067668, -164.76000558, -0.01012503, -16.47600056, -0.03246446, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 148.44213117, 0.00062296, 177.32447746, 0.01044091, 17.73244775, 0.03490911, -148.44213117, -0.00062296, -177.32447746, -0.01044091, -17.73244775, -0.03490911, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 143.26376629, 0.01353357, 143.26376629, 0.04060071, 100.28463641, -1414.89175896, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 35.81594157, 7.281e-05, 107.44782472, 0.00021842, 358.15941573, 0.00072805, -35.81594157, -7.281e-05, -107.44782472, -0.00021842, -358.15941573, -0.00072805, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 146.56978648, 0.01245923, 146.56978648, 0.0373777, 102.59885054, -1478.46522152, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 36.64244662, 7.449e-05, 109.92733986, 0.00022346, 366.42446621, 0.00074485, -36.64244662, -7.449e-05, -109.92733986, -0.00022346, -366.42446621, -0.00074485, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 10.6, 12.75, 0.0)
    ops.node(121021, 10.6, 12.75, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.09, 25367381.45314012, 10569742.27214172, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 81.48699889, 0.00078659, 96.27798914, 0.01067039, 9.62779891, 0.02767377, -81.48699889, -0.00078659, -96.27798914, -0.01067039, -9.62779891, -0.02767377, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 81.48699889, 0.00078659, 96.27798914, 0.01067039, 9.62779891, 0.02767377, -81.48699889, -0.00078659, -96.27798914, -0.01067039, -9.62779891, -0.02767377, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 103.06478507, 0.01573178, 103.06478507, 0.04719533, 72.14534955, -1399.27779959, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 25.76619627, 9.426e-05, 77.2985888, 0.00028278, 257.66196267, 0.00094259, -25.76619627, -9.426e-05, -77.2985888, -0.00028278, -257.66196267, -0.00094259, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 103.06478507, 0.01573178, 103.06478507, 0.04719533, 72.14534955, -1399.27779959, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 25.76619627, 9.426e-05, 77.2985888, 0.00028278, 257.66196267, 0.00094259, -25.76619627, -9.426e-05, -77.2985888, -0.00028278, -257.66196267, -0.00094259, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 13.45, 12.75, 0.0)
    ops.node(121022, 13.45, 12.75, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.09, 27624437.34542678, 11510182.22726116, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 81.71147724, 0.00077245, 97.0469718, 0.01102122, 9.70469718, 0.0340572, -81.71147724, -0.00077245, -97.0469718, -0.01102122, -9.70469718, -0.0340572, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 81.71147724, 0.00077245, 97.0469718, 0.01102122, 9.70469718, 0.0340572, -81.71147724, -0.00077245, -97.0469718, -0.01102122, -9.70469718, -0.0340572, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 104.71694304, 0.01544909, 104.71694304, 0.04634728, 73.30186013, -1293.75609057, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 26.17923576, 8.795e-05, 78.53770728, 0.00026384, 261.79235761, 0.00087945, -26.17923576, -8.795e-05, -78.53770728, -0.00026384, -261.79235761, -0.00087945, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 104.71694304, 0.01544909, 104.71694304, 0.04634728, 73.30186013, -1293.75609057, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 26.17923576, 8.795e-05, 78.53770728, 0.00026384, 261.79235761, 0.00087945, -26.17923576, -8.795e-05, -78.53770728, -0.00026384, -261.79235761, -0.00087945, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 18.75, 12.75, 0.0)
    ops.node(121023, 18.75, 12.75, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.14, 25208998.17220958, 10503749.23842066, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 133.58256896, 0.0006741, 158.95746198, 0.00991903, 15.8957462, 0.02478328, -133.58256896, -0.0006741, -158.95746198, -0.00991903, -15.8957462, -0.02478328, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 143.40609114, 0.0006207, 170.64702721, 0.01022726, 17.06470272, 0.02650797, -143.40609114, -0.0006207, -170.64702721, -0.01022726, -17.06470272, -0.02650797, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 126.71458446, 0.01348199, 126.71458446, 0.04044598, 88.70020912, -1453.85047278, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 31.67864611, 7.497e-05, 95.03593834, 0.0002249, 316.78646114, 0.00074968, -31.67864611, -7.497e-05, -95.03593834, -0.0002249, -316.78646114, -0.00074968, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 130.31125794, 0.01241397, 130.31125794, 0.03724192, 91.21788056, -1524.01522404, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 32.57781449, 7.71e-05, 97.73344346, 0.00023129, 325.77814485, 0.00077095, -32.57781449, -7.71e-05, -97.73344346, -0.00023129, -325.77814485, -0.00077095, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 24.05, 12.75, 0.0)
    ops.node(121024, 24.05, 12.75, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.0625, 27304250.14761152, 11376770.89483813, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 63.20424746, 0.00092084, 74.68781297, 0.01076053, 7.4687813, 0.03309682, -63.20424746, -0.00092084, -74.68781297, -0.01076053, -7.4687813, -0.03309682, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 60.16673594, 0.00092084, 71.09841666, 0.01076053, 7.10984167, 0.03309682, -60.16673594, -0.00092084, -71.09841666, -0.01076053, -7.10984167, -0.03309682, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 75.00325938, 0.0184168, 75.00325938, 0.05525041, 52.50228157, -1014.24995471, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 18.75081485, 9.177e-05, 56.25244454, 0.00027531, 187.50814846, 0.0009177, -18.75081485, -9.177e-05, -56.25244454, -0.00027531, -187.50814846, -0.0009177, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 75.00325938, 0.0184168, 75.00325938, 0.05525041, 52.50228157, -1014.24995471, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 18.75081485, 9.177e-05, 56.25244454, 0.00027531, 187.50814846, 0.0009177, -18.75081485, -9.177e-05, -56.25244454, -0.00027531, -187.50814846, -0.0009177, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.175)
    ops.node(122001, 0.0, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 25529056.92288116, 10637107.05120048, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 50.19975813, 0.00095653, 59.74801209, 0.01349819, 5.97480121, 0.03813652, -50.19975813, -0.00095653, -59.74801209, -0.01349819, -5.97480121, -0.03813652, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 52.57393566, 0.00095653, 62.57377048, 0.01349819, 6.25737705, 0.03813652, -52.57393566, -0.00095653, -62.57377048, -0.01349819, -6.25737705, -0.03813652, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 72.48520413, 0.01913057, 72.48520413, 0.05739171, 50.73964289, -976.91183006, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 18.12130103, 9.486e-05, 54.36390309, 0.00028457, 181.21301032, 0.00094856, -18.12130103, -9.486e-05, -54.36390309, -0.00028457, -181.21301032, -0.00094856, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 72.48520413, 0.01913057, 72.48520413, 0.05739171, 50.73964289, -976.91183006, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 18.12130103, 9.486e-05, 54.36390309, 0.00028457, 181.21301032, 0.00094856, -18.12130103, -9.486e-05, -54.36390309, -0.00028457, -181.21301032, -0.00094856, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 5.3, 0.0, 3.175)
    ops.node(122002, 5.3, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.1575, 25777876.2481099, 10740781.77004579, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 98.13683139, 0.00063711, 118.22190278, 0.0109204, 11.82219028, 0.03408896, -98.13683139, -0.00063711, -118.22190278, -0.0109204, -11.82219028, -0.03408896, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 144.0321172, 0.00055376, 173.51029898, 0.01163899, 17.3510299, 0.03932493, -144.0321172, -0.00055376, -173.51029898, -0.01163899, -17.3510299, -0.03932493, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 133.93633014, 0.01274224, 133.93633014, 0.03822672, 93.7554311, -1342.89214759, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 33.48408253, 6.888e-05, 100.4522476, 0.00020664, 334.84082535, 0.00068881, -33.48408253, -6.888e-05, -100.4522476, -0.00020664, -334.84082535, -0.00068881, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 143.01636276, 0.01107527, 143.01636276, 0.0332258, 100.11145393, -1545.80395894, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 35.75409069, 7.355e-05, 107.26227207, 0.00022065, 357.54090689, 0.00073551, -35.75409069, -7.355e-05, -107.26227207, -0.00022065, -357.54090689, -0.00073551, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 18.75, 0.0, 3.175)
    ops.node(122005, 18.75, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.1575, 28011290.64789016, 11671371.10328757, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 98.68363417, 0.00061219, 118.87627932, 0.01221158, 11.88762793, 0.03915837, -98.68363417, -0.00061219, -118.87627932, -0.01221158, -11.88762793, -0.03915837, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 144.93484345, 0.00053656, 174.59141102, 0.01304052, 17.4591411, 0.04524136, -144.93484345, -0.00053656, -174.59141102, -0.01304052, -17.4591411, -0.04524136, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 146.95685578, 0.01224378, 146.95685578, 0.03673135, 102.86979904, -1396.59347445, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 36.73921394, 6.955e-05, 110.21764183, 0.00020865, 367.39213944, 0.00069552, -36.73921394, -6.955e-05, -110.21764183, -0.00020865, -367.39213944, -0.00069552, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 156.74152626, 0.01073116, 156.74152626, 0.03219349, 109.71906838, -1620.02546241, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 39.18538156, 7.418e-05, 117.55614469, 0.00022255, 391.85381565, 0.00074182, -39.18538156, -7.418e-05, -117.55614469, -0.00022255, -391.85381565, -0.00074182, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 24.05, 0.0, 3.175)
    ops.node(122006, 24.05, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.0625, 26384825.93716229, 10993677.47381762, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 48.71042395, 0.00088302, 58.07351982, 0.01308767, 5.80735198, 0.04042735, -48.71042395, -0.00088302, -58.07351982, -0.01308767, -5.80735198, -0.04042735, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 51.08099024, 0.00088302, 60.8997553, 0.01308767, 6.08997553, 0.04042735, -51.08099024, -0.00088302, -60.8997553, -0.01308767, -6.08997553, -0.04042735, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 71.02085605, 0.01766035, 71.02085605, 0.05298105, 49.71459923, -904.36604824, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 17.75521401, 8.993e-05, 53.26564204, 0.00026978, 177.55214012, 0.00089925, -17.75521401, -8.993e-05, -53.26564204, -0.00026978, -177.55214012, -0.00089925, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 71.02085605, 0.01766035, 71.02085605, 0.05298105, 49.71459923, -904.36604824, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 17.75521401, 8.993e-05, 53.26564204, 0.00026978, 177.55214012, 0.00089925, -17.75521401, -8.993e-05, -53.26564204, -0.00026978, -177.55214012, -0.00089925, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.25, 3.15)
    ops.node(122007, 0.0, 4.25, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.14, 25619034.26883273, 10674597.61201364, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 134.77711734, 0.00060142, 162.02366595, 0.01208451, 16.20236659, 0.03469882, -134.77711734, -0.00060142, -162.02366595, -0.01208451, -16.20236659, -0.03469882, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 138.96638852, 0.0006529, 167.05984039, 0.01170372, 16.70598404, 0.03235054, -138.96638852, -0.0006529, -167.05984039, -0.01170372, -16.70598404, -0.03235054, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 120.59976751, 0.01202844, 120.59976751, 0.03608532, 84.41983726, -1242.73092144, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 30.14994188, 7.021e-05, 90.44982563, 0.00021062, 301.49941878, 0.00070208, -30.14994188, -7.021e-05, -90.44982563, -0.00021062, -301.49941878, -0.00070208, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 117.10086015, 0.01305809, 117.10086015, 0.03917427, 81.97060211, -1170.16655616, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 29.27521504, 6.817e-05, 87.82564512, 0.00020451, 292.75215039, 0.00068171, -29.27521504, -6.817e-05, -87.82564512, -0.00020451, -292.75215039, -0.00068171, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 5.3, 4.25, 3.15)
    ops.node(122008, 5.3, 4.25, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.2475, 26354583.35465271, 10981076.39777196, 0.00841652, 0.00459422, 0.00686297, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 241.93021791, 0.00049126, 292.5283109, 0.01043029, 29.25283109, 0.03043343, -241.93021791, -0.00049126, -292.5283109, -0.01043029, -29.25283109, -0.03043343, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 186.1936082, 0.00053121, 225.13476066, 0.01002434, 22.51347607, 0.02796387, -186.1936082, -0.00053121, -225.13476066, -0.01002434, -22.51347607, -0.02796387, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 219.12262536, 0.00982513, 219.12262536, 0.0294754, 153.38583775, -1502.43486313, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 54.78065634, 7.014e-05, 164.34196902, 0.00021043, 547.80656341, 0.00070143, -54.78065634, -7.014e-05, -164.34196902, -0.00021043, -547.80656341, -0.00070143, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 180.35758321, 0.01062428, 180.35758321, 0.03187285, 126.25030825, -1395.57399367, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 45.0893958, 5.773e-05, 135.26818741, 0.0001732, 450.89395802, 0.00057734, -45.0893958, -5.773e-05, -135.26818741, -0.0001732, -450.89395802, -0.00057734, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 10.6, 4.25, 3.15)
    ops.node(122009, 10.6, 4.25, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.2, 26971058.91961571, 11237941.21650655, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 201.19799358, 0.0005029, 242.89302006, 0.01329785, 24.28930201, 0.03884302, -201.19799358, -0.0005029, -242.89302006, -0.01329785, -24.28930201, -0.03884302, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 141.65044826, 0.0005545, 171.00521013, 0.01260172, 17.10052101, 0.03474667, -141.65044826, -0.0005545, -171.00521013, -0.01260172, -17.10052101, -0.03474667, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 186.87647205, 0.01005792, 186.87647205, 0.03017375, 130.81353043, -1622.60001689, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 46.71911801, 7.234e-05, 140.15735403, 0.00021701, 467.19118011, 0.00072336, -46.71911801, -7.234e-05, -140.15735403, -0.00021701, -467.19118011, -0.00072336, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 165.07072134, 0.01108997, 165.07072134, 0.0332699, 115.54950494, -1448.66242537, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 41.26768034, 6.39e-05, 123.80304101, 0.00019169, 412.67680336, 0.00063896, -41.26768034, -6.39e-05, -123.80304101, -0.00019169, -412.67680336, -0.00063896, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 13.45, 4.25, 3.15)
    ops.node(122010, 13.45, 4.25, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.2, 27469101.87824628, 11445459.11593595, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 206.51698238, 0.000518, 249.2618498, 0.01326111, 24.92618498, 0.03954733, -206.51698238, -0.000518, -249.2618498, -0.01326111, -24.92618498, -0.03954733, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 145.31435562, 0.00057378, 175.39150856, 0.01257219, 17.53915086, 0.03535955, -145.31435562, -0.00057378, -175.39150856, -0.01257219, -17.53915086, -0.03535955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 189.61999127, 0.01036008, 189.61999127, 0.03108024, 132.73399389, -1610.76452781, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 47.40499782, 7.207e-05, 142.21499345, 0.0002162, 474.04997817, 0.00072068, -47.40499782, -7.207e-05, -142.21499345, -0.0002162, -474.04997817, -0.00072068, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 167.6138608, 0.01147561, 167.6138608, 0.03442683, 117.32970256, -1439.71339634, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 41.9034652, 6.37e-05, 125.7103956, 0.00019111, 419.03465201, 0.00063704, -41.9034652, -6.37e-05, -125.7103956, -0.00019111, -419.03465201, -0.00063704, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 18.75, 4.25, 3.15)
    ops.node(122011, 18.75, 4.25, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2475, 26253179.92213515, 10938824.96755631, 0.00841652, 0.00459422, 0.00686297, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 247.53260153, 0.00049528, 299.30621462, 0.00982882, 29.93062146, 0.02970886, -247.53260153, -0.00049528, -299.30621462, -0.00982882, -29.93062146, -0.02970886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 190.25147702, 0.0005349, 230.04424088, 0.00944969, 23.00442409, 0.02727882, -190.25147702, -0.0005349, -230.04424088, -0.00944969, -23.00442409, -0.02727882, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 216.80580471, 0.0099056, 216.80580471, 0.02971679, 151.76406329, -1473.85966218, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 54.20145118, 6.967e-05, 162.60435353, 0.00020901, 542.01451177, 0.0006967, -54.20145118, -6.967e-05, -162.60435353, -0.00020901, -542.01451177, -0.0006967, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 178.45697331, 0.01069791, 178.45697331, 0.03209373, 124.91988132, -1373.02471914, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 44.61424333, 5.735e-05, 133.84272998, 0.00017204, 446.14243327, 0.00057346, -44.61424333, -5.735e-05, -133.84272998, -0.00017204, -446.14243327, -0.00057346, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 24.05, 4.25, 3.15)
    ops.node(122012, 24.05, 4.25, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.14, 28204584.60188689, 11751910.25078621, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 135.33191296, 0.00059543, 162.76945796, 0.01336454, 16.2769458, 0.04073561, -135.33191296, -0.00059543, -162.76945796, -0.01336454, -16.2769458, -0.04073561, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 138.2945438, 0.00064673, 166.3327403, 0.01293514, 16.63327403, 0.03792489, -138.2945438, -0.00064673, -166.3327403, -0.01293514, -16.63327403, -0.03792489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 132.79956591, 0.01190862, 132.79956591, 0.03572586, 92.95969614, -1268.47423028, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 33.19989148, 7.022e-05, 99.59967444, 0.00021067, 331.99891478, 0.00070223, -33.19989148, -7.022e-05, -99.59967444, -0.00021067, -331.99891478, -0.00070223, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 129.14857987, 0.01293458, 129.14857987, 0.03880373, 90.40400591, -1192.01340861, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 32.28714497, 6.829e-05, 96.8614349, 0.00020488, 322.87144968, 0.00068292, -32.28714497, -6.829e-05, -96.8614349, -0.00020488, -322.87144968, -0.00068292, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 8.5, 3.15)
    ops.node(122013, 0.0, 8.5, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.14, 27532434.52446334, 11471847.71852639, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 134.52680359, 0.00059773, 161.84135077, 0.01211228, 16.18413508, 0.03834963, -134.52680359, -0.00059773, -161.84135077, -0.01211228, -16.18413508, -0.03834963, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 137.38629403, 0.00064973, 165.28143694, 0.01173081, 16.52814369, 0.03568547, -137.38629403, -0.00064973, -165.28143694, -0.01173081, -16.52814369, -0.03568547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 126.6467276, 0.01195464, 126.6467276, 0.03586392, 88.65270932, -1200.25975227, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 31.6616819, 6.86e-05, 94.9850457, 0.00020581, 316.616819, 0.00068604, -31.6616819, -6.86e-05, -94.9850457, -0.00020581, -316.616819, -0.00068604, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 123.40220384, 0.0129946, 123.40220384, 0.03898381, 86.38154268, -1134.07476507, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 30.85055096, 6.685e-05, 92.55165288, 0.00020054, 308.50550959, 0.00066847, -30.85055096, -6.685e-05, -92.55165288, -0.00020054, -308.50550959, -0.00066847, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 5.3, 8.5, 3.15)
    ops.node(122014, 5.3, 8.5, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.2475, 27624398.41257858, 11510166.00524108, 0.00841652, 0.00459422, 0.00686297, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 243.62995398, 0.00049103, 294.40693692, 0.0104967, 29.44069369, 0.0319351, -243.62995398, -0.00049103, -294.40693692, -0.0104967, -29.44069369, -0.0319351, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 187.60944684, 0.00053094, 226.71072124, 0.01008772, 22.67107212, 0.02931444, -187.60944684, -0.00053094, -226.71072124, -0.01008772, -22.67107212, -0.02931444, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 231.12709201, 0.00982056, 231.12709201, 0.02946167, 161.78896441, -1518.02718999, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 57.781773, 7.059e-05, 173.34531901, 0.00021176, 577.81773004, 0.00070585, -57.781773, -7.059e-05, -173.34531901, -0.00021176, -577.81773004, -0.00070585, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 190.24322076, 0.01061888, 190.24322076, 0.03185665, 133.17025453, -1407.86450588, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 47.56080519, 5.81e-05, 142.68241557, 0.0001743, 475.6080519, 0.00058099, -47.56080519, -5.81e-05, -142.68241557, -0.0001743, -475.6080519, -0.00058099, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 10.6, 8.5, 3.15)
    ops.node(122015, 10.6, 8.5, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.1575, 27130705.82017782, 11304460.75840742, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 147.94355707, 0.00053052, 178.24998939, 0.01343686, 17.82499894, 0.0401084, -147.94355707, -0.00053052, -178.24998939, -0.01343686, -17.82499894, -0.0401084, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 105.93365953, 0.00060361, 127.63430906, 0.01262802, 12.76343091, 0.03517726, -105.93365953, -0.00060361, -127.63430906, -0.01262802, -12.76343091, -0.03517726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 144.51515058, 0.01061035, 144.51515058, 0.03183104, 101.16060541, -1435.2317669, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 36.12878765, 7.062e-05, 108.38636294, 0.00021185, 361.28787646, 0.00070616, -36.12878765, -7.062e-05, -108.38636294, -0.00021185, -361.28787646, -0.00070616, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 136.57262202, 0.0120721, 136.57262202, 0.03621631, 95.60083541, -1264.37470609, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 34.1431555, 6.673e-05, 102.42946651, 0.0002002, 341.43155504, 0.00066735, -34.1431555, -6.673e-05, -102.42946651, -0.0002002, -341.43155504, -0.00066735, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 13.45, 8.5, 3.15)
    ops.node(122016, 13.45, 8.5, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1575, 28993110.08850084, 12080462.53687535, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 148.6341913, 0.00053195, 178.87433642, 0.01386605, 17.88743364, 0.04350388, -148.6341913, -0.00053195, -178.87433642, -0.01386605, -17.88743364, -0.04350388, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 106.63733077, 0.00060662, 128.33306801, 0.01302956, 12.8333068, 0.03808662, -106.63733077, -0.00060662, -128.33306801, -0.01302956, -12.8333068, -0.03808662, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 154.896657, 0.01063909, 154.896657, 0.03191727, 108.4276599, -1466.28917227, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 38.72416425, 7.083e-05, 116.17249275, 0.00021248, 387.24164249, 0.00070827, -38.72416425, -7.083e-05, -116.17249275, -0.00021248, -387.24164249, -0.00070827, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 146.64481104, 0.01213236, 146.64481104, 0.03639708, 102.65136773, -1287.02631999, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 36.66120276, 6.705e-05, 109.98360828, 0.00020116, 366.61202761, 0.00067054, -36.66120276, -6.705e-05, -109.98360828, -0.00020116, -366.61202761, -0.00067054, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 18.75, 8.5, 3.15)
    ops.node(122017, 18.75, 8.5, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.2475, 27939068.65764095, 11641278.60735039, 0.00841652, 0.00459422, 0.00686297, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 239.8952196, 0.00049834, 289.81616422, 0.0112934, 28.98161642, 0.03305837, -239.8952196, -0.00049834, -289.81616422, -0.0112934, -28.98161642, -0.03305837, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 185.06075656, 0.00054243, 223.57093527, 0.01085319, 22.35709353, 0.03037278, -185.06075656, -0.00054243, -223.57093527, -0.01085319, -22.35709353, -0.03037278, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 236.24348764, 0.00996675, 236.24348764, 0.02990026, 165.37044135, -1564.58951319, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 59.06087191, 7.134e-05, 177.18261573, 0.00021401, 590.60871909, 0.00071335, -59.06087191, -7.134e-05, -177.18261573, -0.00021401, -590.60871909, -0.00071335, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 194.44540872, 0.01084868, 194.44540872, 0.03254604, 136.1117861, -1444.51091875, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 48.61135218, 5.871e-05, 145.83405654, 0.00017614, 486.1135218, 0.00058714, -48.61135218, -5.871e-05, -145.83405654, -0.00017614, -486.1135218, -0.00058714, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 24.05, 8.5, 3.15)
    ops.node(122018, 24.05, 8.5, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.14, 26018517.25641327, 10841048.85683887, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 129.3705401, 0.00059194, 155.57771384, 0.01240971, 15.55777138, 0.03582945, -129.3705401, -0.00059194, -155.57771384, -0.01240971, -15.55777138, -0.03582945, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 131.35170876, 0.00064452, 157.96021677, 0.01201741, 15.79602168, 0.0333996, -131.35170876, -0.00064452, -157.96021677, -0.01201741, -15.79602168, -0.0333996, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 123.65578333, 0.01183871, 123.65578333, 0.03551613, 86.55904833, -1272.16617353, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 30.91394583, 7.088e-05, 92.7418375, 0.00021265, 309.13945833, 0.00070882, -30.91394583, -7.088e-05, -92.7418375, -0.00021265, -309.13945833, -0.00070882, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 119.98311411, 0.01289039, 119.98311411, 0.03867116, 83.98817988, -1195.14476204, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 29.99577853, 6.878e-05, 89.98733558, 0.00020633, 299.95778528, 0.00068776, -29.99577853, -6.878e-05, -89.98733558, -0.00020633, -299.95778528, -0.00068776, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 12.75, 3.175)
    ops.node(122019, 0.0, 12.75, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.0625, 28488648.32723416, 11870270.13634757, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 51.60831564, 0.00087628, 61.63572183, 0.01369548, 6.16357218, 0.04715737, -51.60831564, -0.00087628, -61.63572183, -0.01369548, -6.16357218, -0.04715737, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 54.3457165, 0.00087628, 64.90499492, 0.01369548, 6.49049949, 0.04715737, -54.3457165, -0.00087628, -64.90499492, -0.01369548, -6.49049949, -0.04715737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 74.76485033, 0.01752558, 74.76485033, 0.05257675, 52.33539523, -893.24656105, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 18.69121258, 8.768e-05, 56.07363775, 0.00026303, 186.91212583, 0.00087675, -18.69121258, -8.768e-05, -56.07363775, -0.00026303, -186.91212583, -0.00087675, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 74.76485033, 0.01752558, 74.76485033, 0.05257675, 52.33539523, -893.24656105, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 18.69121258, 8.768e-05, 56.07363775, 0.00026303, 186.91212583, 0.00087675, -18.69121258, -8.768e-05, -56.07363775, -0.00026303, -186.91212583, -0.00087675, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 5.3, 12.75, 3.175)
    ops.node(122020, 5.3, 12.75, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.14, 30761984.08654795, 12817493.36939498, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 100.26559623, 0.00059356, 120.19241105, 0.01220022, 12.01924111, 0.04027913, -100.26559623, -0.00059356, -120.19241105, -0.01220022, -12.01924111, -0.04027913, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 119.994216, 0.00055162, 143.84190266, 0.0126123, 14.38419027, 0.04336691, -119.994216, -0.00055162, -143.84190266, -0.0126123, -14.38419027, -0.04336691, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 141.17706921, 0.01187127, 141.17706921, 0.03561382, 98.82394845, -1206.89997674, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 35.2942673, 6.845e-05, 105.88280191, 0.00020534, 352.94267303, 0.00068447, -35.2942673, -6.845e-05, -105.88280191, -0.00020534, -352.94267303, -0.00068447, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 144.80421561, 0.01103247, 144.80421561, 0.0330974, 101.36295093, -1282.27577739, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 36.2010539, 7.021e-05, 108.60316171, 0.00021062, 362.01053904, 0.00070205, -36.2010539, -7.021e-05, -108.60316171, -0.00021062, -362.01053904, -0.00070205, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 10.6, 12.75, 3.175)
    ops.node(122021, 10.6, 12.75, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.09, 27602684.34676113, 11501118.47781714, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 64.53536044, 0.00070988, 77.28008903, 0.01187139, 7.7280089, 0.04125937, -64.53536044, -0.00070988, -77.28008903, -0.01187139, -7.7280089, -0.04125937, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 61.20256551, 0.00070988, 73.28911901, 0.01187139, 7.3289119, 0.04125937, -61.20256551, -0.00070988, -73.28911901, -0.01187139, -7.3289119, -0.04125937, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 96.91973, 0.0141975, 96.91973, 0.04259251, 67.843811, -1103.89143457, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 24.2299325, 8.146e-05, 72.6897975, 0.00024438, 242.29932501, 0.00081461, -24.2299325, -8.146e-05, -72.6897975, -0.00024438, -242.29932501, -0.00081461, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 96.91973, 0.0141975, 96.91973, 0.04259251, 67.843811, -1103.89143457, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 24.2299325, 8.146e-05, 72.6897975, 0.00024438, 242.29932501, 0.00081461, -24.2299325, -8.146e-05, -72.6897975, -0.00024438, -242.29932501, -0.00081461, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 13.45, 12.75, 3.175)
    ops.node(122022, 13.45, 12.75, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.09, 29706044.79564267, 12377518.66485111, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 64.31209249, 0.00069048, 76.9653773, 0.0135711, 7.69653773, 0.04763893, -64.31209249, -0.00069048, -76.9653773, -0.0135711, -7.69653773, -0.04763893, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 61.0934001, 0.00069048, 73.11341316, 0.0135711, 7.31134132, 0.04763893, -61.0934001, -0.00069048, -73.11341316, -0.0135711, -7.31134132, -0.04763893, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 105.03553163, 0.01380967, 105.03553163, 0.041429, 73.52487214, -1149.13796886, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 26.25888291, 8.203e-05, 78.77664872, 0.00024609, 262.58882908, 0.00082031, -26.25888291, -8.203e-05, -78.77664872, -0.00024609, -262.58882908, -0.00082031, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 105.03553163, 0.01380967, 105.03553163, 0.041429, 73.52487214, -1149.13796886, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 26.25888291, 8.203e-05, 78.77664872, 0.00024609, 262.58882908, 0.00082031, -26.25888291, -8.203e-05, -78.77664872, -0.00024609, -262.58882908, -0.00082031, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 18.75, 12.75, 3.175)
    ops.node(122023, 18.75, 12.75, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.14, 26935038.34657495, 11222932.64440623, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 100.79848533, 0.00060643, 121.20033438, 0.0120672, 12.12003344, 0.03467841, -100.79848533, -0.00060643, -121.20033438, -0.0120672, -12.12003344, -0.03467841, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 121.0156466, 0.00056376, 145.50949635, 0.01247284, 14.55094964, 0.03723872, -121.0156466, -0.00056376, -145.50949635, -0.01247284, -14.55094964, -0.03723872, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 126.10440049, 0.01212861, 126.10440049, 0.03638582, 88.27308034, -1243.38596891, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 31.52610012, 6.983e-05, 94.57830037, 0.00020948, 315.26100122, 0.00069826, -31.52610012, -6.983e-05, -94.57830037, -0.00020948, -315.26100122, -0.00069826, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 129.98432701, 0.01127512, 129.98432701, 0.03382536, 90.98902891, -1325.29125278, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 32.49608175, 7.197e-05, 97.48824526, 0.00021592, 324.96081752, 0.00071974, -32.49608175, -7.197e-05, -97.48824526, -0.00021592, -324.96081752, -0.00071974, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 24.05, 12.75, 3.175)
    ops.node(122024, 24.05, 12.75, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.0625, 27884144.93644137, 11618393.72351724, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 51.1422333, 0.00091148, 61.067848, 0.01394601, 6.1067848, 0.0457317, -51.1422333, -0.00091148, -61.067848, -0.01394601, -6.1067848, -0.0457317, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 53.67453523, 0.00091148, 64.09161562, 0.01394601, 6.40916156, 0.0457317, -53.67453523, -0.00091148, -64.09161562, -0.01394601, -6.40916156, -0.0457317, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 74.25633958, 0.01822951, 74.25633958, 0.05468854, 51.9794377, -909.51020393, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 18.56408489, 8.897e-05, 55.69225468, 0.0002669, 185.64084894, 0.00088967, -18.56408489, -8.897e-05, -55.69225468, -0.0002669, -185.64084894, -0.00088967, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 74.25633958, 0.01822951, 74.25633958, 0.05468854, 51.9794377, -909.51020393, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 18.56408489, 8.897e-05, 55.69225468, 0.0002669, 185.64084894, 0.00088967, -18.56408489, -8.897e-05, -55.69225468, -0.0002669, -185.64084894, -0.00088967, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.075)
    ops.node(123001, 0.0, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 27301843.93728144, 11375768.3072006, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 32.72031281, 0.00080637, 39.44813288, 0.01329522, 3.94481329, 0.05388729, -32.72031281, -0.00080637, -39.44813288, -0.01329522, -3.94481329, -0.05388729, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 34.95426136, 0.00080637, 42.14141702, 0.01329522, 4.2141417, 0.05388729, -34.95426136, -0.00080637, -42.14141702, -0.01329522, -4.2141417, -0.05388729, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 59.17976456, 0.01612732, 59.17976456, 0.04838196, 41.42583519, -704.83949324, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 14.79494114, 7.242e-05, 44.38482342, 0.00021725, 147.9494114, 0.00072416, -14.79494114, -7.242e-05, -44.38482342, -0.00021725, -147.9494114, -0.00072416, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 59.17976456, 0.01612732, 59.17976456, 0.04838196, 41.42583519, -704.83949324, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 14.79494114, 7.242e-05, 44.38482342, 0.00021725, 147.9494114, 0.00072416, -14.79494114, -7.242e-05, -44.38482342, -0.00021725, -147.9494114, -0.00072416, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 5.3, 0.0, 6.075)
    ops.node(123002, 5.3, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0875, 27340209.43542022, 11391753.93142509, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 47.36028196, 0.0008218, 56.91790957, 0.01345933, 5.69179096, 0.04206084, -47.36028196, -0.0008218, -56.91790957, -0.01345933, -5.69179096, -0.04206084, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 64.07210194, 0.0006382, 77.0022887, 0.0147307, 7.70022887, 0.0517689, -64.07210194, -0.0006382, -77.0022887, -0.0147307, -7.70022887, -0.0517689, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 88.97291517, 0.01643597, 88.97291517, 0.04930791, 62.28104062, -975.36053108, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 22.24322879, 7.766e-05, 66.72968637, 0.00023297, 222.43228792, 0.00077657, -22.24322879, -7.766e-05, -66.72968637, -0.00023297, -222.43228792, -0.00077657, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 99.18330592, 0.01276402, 99.18330592, 0.03829207, 69.42831414, -1223.83372344, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 24.79582648, 8.657e-05, 74.38747944, 0.00025971, 247.9582648, 0.00086568, -24.79582648, -8.657e-05, -74.38747944, -0.00025971, -247.9582648, -0.00086568, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 18.75, 0.0, 6.075)
    ops.node(123005, 18.75, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0875, 28891551.43561214, 12038146.43150506, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 46.32506307, 0.00080921, 55.64071929, 0.01154395, 5.56407193, 0.04313657, -46.32506307, -0.00080921, -55.64071929, -0.01154395, -5.56407193, -0.04313657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 62.94759985, 0.0006254, 75.60593556, 0.01259604, 7.56059356, 0.05350765, -62.94759985, -0.0006254, -75.60593556, -0.01259604, -7.56059356, -0.05350765, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 83.3872036, 0.01618416, 83.3872036, 0.04855247, 58.37104252, -854.06692966, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 20.8468009, 6.887e-05, 62.5404027, 0.00020662, 208.468009, 0.00068873, -20.8468009, -6.887e-05, -62.5404027, -0.00020662, -208.468009, -0.00068873, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 95.7711842, 0.01250808, 95.7711842, 0.03752424, 67.03982894, -1035.19589241, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 23.94279605, 7.91e-05, 71.82838815, 0.00023731, 239.4279605, 0.00079102, -23.94279605, -7.91e-05, -71.82838815, -0.00023731, -239.4279605, -0.00079102, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 24.05, 0.0, 6.075)
    ops.node(123006, 24.05, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 27751050.16911313, 11562937.57046381, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 32.43615407, 0.00081472, 39.09794967, 0.01583615, 3.90979497, 0.05751779, -32.43615407, -0.00081472, -39.09794967, -0.01583615, -3.90979497, -0.05751779, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 34.5062661, 0.00081472, 41.59322503, 0.01583615, 4.1593225, 0.05751779, -34.5062661, -0.00081472, -41.59322503, -0.01583615, -4.1593225, -0.05751779, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 68.58669094, 0.01629443, 68.58669094, 0.04888328, 48.01068366, -821.55519875, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 17.14667274, 8.257e-05, 51.44001821, 0.0002477, 171.46672736, 0.00082568, -17.14667274, -8.257e-05, -51.44001821, -0.0002477, -171.46672736, -0.00082568, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 68.58669094, 0.01629443, 68.58669094, 0.04888328, 48.01068366, -821.55519875, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 17.14667274, 8.257e-05, 51.44001821, 0.0002477, 171.46672736, 0.00082568, -17.14667274, -8.257e-05, -51.44001821, -0.0002477, -171.46672736, -0.00082568, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.25, 6.05)
    ops.node(123007, 0.0, 4.25, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0875, 30534227.3739001, 12722594.73912504, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 81.55660949, 0.00063511, 97.80329106, 0.01467525, 9.78032911, 0.05365252, -81.55660949, -0.00063511, -97.80329106, -0.01467525, -9.78032911, -0.05365252, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 61.19886603, 0.00081377, 73.39013409, 0.01346893, 7.33901341, 0.04393537, -61.19886603, -0.00081377, -73.39013409, -0.01346893, -7.33901341, -0.04393537, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 98.04845762, 0.01270226, 98.04845762, 0.03810678, 68.63392033, -983.6070839, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 24.5121144, 7.663e-05, 73.53634321, 0.00022988, 245.12114405, 0.00076626, -24.5121144, -7.663e-05, -73.53634321, -0.00022988, -245.12114405, -0.00076626, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 81.30698476, 0.01627537, 81.30698476, 0.04882611, 56.91488933, -815.50022197, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 20.32674619, 6.354e-05, 60.98023857, 0.00019063, 203.2674619, 0.00063542, -20.32674619, -6.354e-05, -60.98023857, -0.00019063, -203.2674619, -0.00063542, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 5.3, 4.25, 6.05)
    ops.node(123008, 5.3, 4.25, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.175, 27787165.49197738, 11577985.62165724, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 161.98384321, 0.00050963, 195.81354873, 0.01204773, 19.58135487, 0.0375357, -161.98384321, -0.00050963, -195.81354873, -0.01204773, -19.58135487, -0.0375357, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 110.77110905, 0.00060641, 133.9052311, 0.01117122, 13.39052311, 0.03185116, -110.77110905, -0.00060641, -133.9052311, -0.01117122, -13.39052311, -0.03185116, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 158.68646068, 0.01019256, 158.68646068, 0.03057767, 111.08052247, -1228.74330329, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 39.67161517, 6.814e-05, 119.01484551, 0.00020441, 396.71615169, 0.00068138, -39.67161517, -6.814e-05, -119.01484551, -0.00020441, -396.71615169, -0.00068138, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 135.87210911, 0.01212823, 135.87210911, 0.03638469, 95.11047638, -1038.40711135, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 33.96802728, 5.834e-05, 101.90408183, 0.00017502, 339.68027278, 0.00058342, -33.96802728, -5.834e-05, -101.90408183, -0.00017502, -339.68027278, -0.00058342, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 10.6, 4.25, 6.05)
    ops.node(123009, 10.6, 4.25, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.14, 25392268.25933572, 10580111.77472322, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 111.25639514, 0.00056682, 134.40863611, 0.01346564, 13.44086361, 0.03930302, -111.25639514, -0.00056682, -134.40863611, -0.01346564, -13.44086361, -0.03930302, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 89.33473721, 0.00061204, 107.92512349, 0.01302529, 10.79251235, 0.03661477, -89.33473721, -0.00061204, -107.92512349, -0.01302529, -10.79251235, -0.03661477, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 117.50554178, 0.01133641, 117.50554178, 0.03400922, 82.25387924, -1202.84756508, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 29.37638544, 6.902e-05, 88.12915633, 0.00020705, 293.76385444, 0.00069018, -29.37638544, -6.902e-05, -88.12915633, -0.00020705, -293.76385444, -0.00069018, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 113.47980738, 0.0122408, 113.47980738, 0.0367224, 79.43586517, -1110.58579007, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 28.36995185, 6.665e-05, 85.10985554, 0.00019996, 283.69951845, 0.00066653, -28.36995185, -6.665e-05, -85.10985554, -0.00019996, -283.69951845, -0.00066653, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 13.45, 4.25, 6.05)
    ops.node(123010, 13.45, 4.25, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.14, 27042734.91592156, 11267806.21496732, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 113.22586672, 0.00059589, 136.79109802, 0.01248163, 13.6791098, 0.0412252, -113.22586672, -0.00059589, -136.79109802, -0.01248163, -13.6791098, -0.0412252, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 91.33308069, 0.00064805, 110.341857, 0.01208636, 11.0341857, 0.03832919, -91.33308069, -0.00064805, -110.341857, -0.01208636, -11.0341857, -0.03832919, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 119.93904637, 0.01191784, 119.93904637, 0.03575351, 83.95733246, -1104.47737246, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 29.98476159, 6.615e-05, 89.95428478, 0.00019844, 299.84761592, 0.00066147, -29.98476159, -6.615e-05, -89.95428478, -0.00019844, -299.84761592, -0.00066147, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 116.45057049, 0.0129611, 116.45057049, 0.0388833, 81.51539935, -1027.72112388, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 29.11264262, 6.422e-05, 87.33792787, 0.00019267, 291.12642624, 0.00064223, -29.11264262, -6.422e-05, -87.33792787, -0.00019267, -291.12642624, -0.00064223, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 18.75, 4.25, 6.05)
    ops.node(123011, 18.75, 4.25, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.175, 29380084.67565384, 12241701.9481891, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 157.89290691, 0.00051162, 190.48670037, 0.01120822, 19.04867004, 0.03841844, -157.89290691, -0.00051162, -190.48670037, -0.01120822, -19.04867004, -0.03841844, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 107.43010908, 0.00061664, 129.60687975, 0.01041094, 12.96068797, 0.03248823, -107.43010908, -0.00061664, -129.60687975, -0.01041094, -12.96068797, -0.03248823, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 164.56275225, 0.01023239, 164.56275225, 0.03069717, 115.19392658, -1154.7250832, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 41.14068806, 6.683e-05, 123.42206419, 0.00020049, 411.40688063, 0.0006683, -41.14068806, -6.683e-05, -123.42206419, -0.00020049, -411.40688063, -0.0006683, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 135.24319858, 0.01233282, 135.24319858, 0.03699846, 94.67023901, -990.59962033, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 33.81079965, 5.492e-05, 101.43239894, 0.00016477, 338.10799646, 0.00054923, -33.81079965, -5.492e-05, -101.43239894, -0.00016477, -338.10799646, -0.00054923, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 24.05, 4.25, 6.05)
    ops.node(123012, 24.05, 4.25, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0875, 27212692.94175111, 11338622.05906296, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 79.3329731, 0.00063619, 95.3954031, 0.01369792, 9.53954031, 0.04604925, -79.3329731, -0.00063619, -95.3954031, -0.01369792, -9.53954031, -0.04604925, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 59.53518831, 0.00081706, 71.58919004, 0.01259033, 7.158919, 0.03787763, -59.53518831, -0.00081706, -71.58919004, -0.01259033, -7.158919, -0.03787763, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 89.16586204, 0.01272371, 89.16586204, 0.03817112, 62.41610342, -989.60687885, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 22.29146551, 7.819e-05, 66.87439653, 0.00023457, 222.91465509, 0.0007819, -22.29146551, -7.819e-05, -66.87439653, -0.00023457, -222.91465509, -0.0007819, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 68.47802523, 0.01634121, 68.47802523, 0.04902363, 47.93461766, -819.40114385, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 17.11950631, 6.005e-05, 51.35851892, 0.00018015, 171.19506306, 0.00060048, -17.11950631, -6.005e-05, -51.35851892, -0.00018015, -171.19506306, -0.00060048, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 8.5, 6.05)
    ops.node(123013, 0.0, 8.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0875, 24593834.09550582, 10247430.87312743, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 77.14049585, 0.00065945, 92.53851644, 0.01410873, 9.25385164, 0.03969854, -77.14049585, -0.00065945, -92.53851644, -0.01410873, -9.25385164, -0.03969854, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 57.32864747, 0.00086383, 68.77202341, 0.01298642, 6.87720234, 0.03298859, -57.32864747, -0.00086383, -68.77202341, -0.01298642, -6.87720234, -0.03298859, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 83.96716822, 0.01318908, 83.96716822, 0.03956724, 58.77701775, -1028.96914734, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 20.99179205, 8.147e-05, 62.97537616, 0.00024441, 209.91792054, 0.00081471, -20.99179205, -8.147e-05, -62.97537616, -0.00024441, -209.91792054, -0.00081471, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 72.4578326, 0.01727654, 72.4578326, 0.05182963, 50.72048282, -844.93153501, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 18.11445815, 7.03e-05, 54.34337445, 0.00021091, 181.14458151, 0.00070304, -18.11445815, -7.03e-05, -54.34337445, -0.00021091, -181.14458151, -0.00070304, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 5.3, 8.5, 6.05)
    ops.node(123014, 5.3, 8.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.175, 26493722.11040679, 11039050.87933616, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 155.99346389, 0.00050859, 188.72115216, 0.01220605, 18.87211522, 0.0360565, -155.99346389, -0.00050859, -188.72115216, -0.01220605, -18.87211522, -0.0360565, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 106.25153628, 0.00061024, 128.54328538, 0.01132096, 12.85432854, 0.03067228, -106.25153628, -0.00061024, -128.54328538, -0.01132096, -12.85432854, -0.03067228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 152.5062459, 0.01017185, 152.5062459, 0.03051556, 106.75437213, -1254.53208854, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 38.12656147, 6.868e-05, 114.37968442, 0.00020604, 381.26561474, 0.00068681, -38.12656147, -6.868e-05, -114.37968442, -0.00020604, -381.26561474, -0.00068681, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 131.0847609, 0.0122048, 131.0847609, 0.03661441, 91.75933263, -1054.98174312, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 32.77119023, 5.903e-05, 98.31357068, 0.0001771, 327.71190226, 0.00059034, -32.77119023, -5.903e-05, -98.31357068, -0.0001771, -327.71190226, -0.00059034, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 10.6, 8.5, 6.05)
    ops.node(123015, 10.6, 8.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0875, 25230855.28809975, 10512856.37004156, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 75.93431498, 0.0006585, 90.98121345, 0.01191362, 9.09812135, 0.03750686, -75.93431498, -0.0006585, -90.98121345, -0.01191362, -9.09812135, -0.03750686, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 52.60491727, 0.00084835, 63.02893768, 0.01099322, 6.30289377, 0.03099807, -52.60491727, -0.00084835, -63.02893768, -0.01099322, -6.30289377, -0.03099807, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 84.03134468, 0.01316992, 84.03134468, 0.03950976, 58.82194128, -988.74077472, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 21.00783617, 7.948e-05, 63.02350851, 0.00023843, 210.07836171, 0.00079475, -21.00783617, -7.948e-05, -63.02350851, -0.00023843, -210.07836171, -0.00079475, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 64.63665827, 0.01696691, 64.63665827, 0.05090073, 45.24566079, -834.21765459, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 16.15916457, 6.113e-05, 48.4774937, 0.0001834, 161.59164568, 0.00061132, -16.15916457, -6.113e-05, -48.4774937, -0.0001834, -161.59164568, -0.00061132, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 13.45, 8.5, 6.05)
    ops.node(123016, 13.45, 8.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0875, 32076504.83906619, 13365210.34961091, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 75.23581218, 0.00063779, 89.86280617, 0.01519939, 8.98628062, 0.05537608, -75.23581218, -0.00063779, -89.86280617, -0.01519939, -8.98628062, -0.05537608, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 52.14327402, 0.00082737, 62.28072498, 0.01395257, 6.2280725, 0.04535652, -52.14327402, -0.00082737, -62.28072498, -0.01395257, -6.2280725, -0.04535652, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 107.51945234, 0.01275575, 107.51945234, 0.03826726, 75.26361664, -1092.8148549, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 26.87986309, 7.999e-05, 80.63958926, 0.00023996, 268.79863086, 0.00079988, -26.87986309, -7.999e-05, -80.63958926, -0.00023996, -268.79863086, -0.00079988, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 96.74973988, 0.01654746, 96.74973988, 0.04964237, 67.72481791, -902.12089518, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 24.18743497, 7.198e-05, 72.56230491, 0.00021593, 241.87434969, 0.00071976, -24.18743497, -7.198e-05, -72.56230491, -0.00021593, -241.87434969, -0.00071976, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 18.75, 8.5, 6.05)
    ops.node(123017, 18.75, 8.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.175, 30916043.81580766, 12881684.92325319, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 159.46216191, 0.0005, 191.8225177, 0.01072002, 19.18225177, 0.039326, -159.46216191, -0.0005, -191.8225177, -0.01072002, -19.18225177, -0.039326, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 108.92416227, 0.00059521, 131.02862017, 0.00995312, 13.10286202, 0.03316288, -108.92416227, -0.00059521, -131.02862017, -0.00995312, -13.10286202, -0.03316288, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 171.98551319, 0.01000001, 171.98551319, 0.03000003, 120.38985924, -1116.65670922, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 42.9963783, 6.637e-05, 128.9891349, 0.00019912, 429.96378298, 0.00066374, -42.9963783, -6.637e-05, -128.9891349, -0.00019912, -429.96378298, -0.00066374, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 139.68388888, 0.01190411, 139.68388888, 0.03571234, 97.77872221, -965.86756801, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 34.92097222, 5.391e-05, 104.76291666, 0.00016172, 349.20972219, 0.00053908, -34.92097222, -5.391e-05, -104.76291666, -0.00016172, -349.20972219, -0.00053908, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 24.05, 8.5, 6.05)
    ops.node(123018, 24.05, 8.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0875, 29033909.31000108, 12097462.21250045, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 77.70796429, 0.00061708, 93.36572744, 0.01389291, 9.33657274, 0.05013306, -77.70796429, -0.00061708, -93.36572744, -0.01389291, -9.33657274, -0.05013306, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 58.13423475, 0.00079111, 69.84799006, 0.01275736, 6.98479901, 0.04108434, -58.13423475, -0.00079111, -69.84799006, -0.01275736, -6.98479901, -0.04108434, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 89.85658045, 0.01234155, 89.85658045, 0.03702464, 62.89960632, -892.24710495, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 22.46414511, 7.385e-05, 67.39243534, 0.00022156, 224.64145113, 0.00073853, -22.46414511, -7.385e-05, -67.39243534, -0.00022156, -224.64145113, -0.00073853, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 70.20722286, 0.01582219, 70.20722286, 0.04746657, 49.145056, -755.76863457, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 17.55180571, 5.77e-05, 52.65541714, 0.00017311, 175.51805714, 0.00057703, -17.55180571, -5.77e-05, -52.65541714, -0.00017311, -175.51805714, -0.00057703, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 12.75, 6.075)
    ops.node(123019, 0.0, 12.75, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 28033352.68480995, 11680563.61867081, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 33.10393923, 0.00076963, 39.89592338, 0.01469587, 3.98959234, 0.05703785, -33.10393923, -0.00076963, -39.89592338, -0.01469587, -3.98959234, -0.05703785, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 35.59746617, 0.00076963, 42.90105093, 0.01469587, 4.29010509, 0.05703785, -35.59746617, -0.00076963, -42.90105093, -0.01469587, -4.29010509, -0.05703785, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 67.39716467, 0.01539267, 67.39716467, 0.04617802, 47.17801527, -775.3041121, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 16.84929117, 8.032e-05, 50.5478735, 0.00024096, 168.49291167, 0.00080319, -16.84929117, -8.032e-05, -50.5478735, -0.00024096, -168.49291167, -0.00080319, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 67.39716467, 0.01539267, 67.39716467, 0.04617802, 47.17801527, -775.3041121, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 16.84929117, 8.032e-05, 50.5478735, 0.00024096, 168.49291167, 0.00080319, -16.84929117, -8.032e-05, -50.5478735, -0.00024096, -168.49291167, -0.00080319, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 5.3, 12.75, 6.075)
    ops.node(123020, 5.3, 12.75, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0875, 28825276.99785455, 12010532.0824394, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 51.05179037, 0.00083868, 61.32111317, 0.01199121, 6.13211132, 0.0396113, -51.05179037, -0.00083868, -61.32111317, -0.01199121, -6.13211132, -0.0396113, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 73.78155981, 0.00064811, 88.62308934, 0.01302117, 8.86230893, 0.04835697, -73.78155981, -0.00064811, -88.62308934, -0.01302117, -8.86230893, -0.04835697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 73.85205382, 0.01677363, 73.85205382, 0.05032088, 51.69643767, -796.10201894, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 18.46301345, 6.114e-05, 55.38904036, 0.00018341, 184.63013455, 0.00061138, -18.46301345, -6.114e-05, -55.38904036, -0.00018341, -184.63013455, -0.00061138, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 91.74417724, 0.01296225, 91.74417724, 0.03888675, 64.22092407, -946.27967491, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 22.93604431, 7.595e-05, 68.80813293, 0.00022785, 229.36044309, 0.0007595, -22.93604431, -7.595e-05, -68.80813293, -0.00022785, -229.36044309, -0.0007595, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 10.6, 12.75, 6.075)
    ops.node(123021, 10.6, 12.75, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 26061990.11829871, 10859162.54929113, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 34.6048957, 0.00082339, 41.47643101, 0.01306405, 4.1476431, 0.04443905, -34.6048957, -0.00082339, -41.47643101, -0.01306405, -4.1476431, -0.04443905, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 34.6048957, 0.00082339, 41.47643101, 0.01306405, 4.1476431, 0.04443905, -34.6048957, -0.00082339, -41.47643101, -0.01306405, -4.1476431, -0.04443905, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 67.36957152, 0.01646774, 67.36957152, 0.04940323, 47.15870006, -839.77316858, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 16.84239288, 8.636e-05, 50.52717864, 0.00025908, 168.42392879, 0.00086359, -16.84239288, -8.636e-05, -50.52717864, -0.00025908, -168.42392879, -0.00086359, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 67.36957152, 0.01646774, 67.36957152, 0.04940323, 47.15870006, -839.77316858, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 16.84239288, 8.636e-05, 50.52717864, 0.00025908, 168.42392879, 0.00086359, -16.84239288, -8.636e-05, -50.52717864, -0.00025908, -168.42392879, -0.00086359, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 13.45, 12.75, 6.075)
    ops.node(123022, 13.45, 12.75, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0625, 26715323.71560545, 11131384.88150227, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 34.32770091, 0.00082511, 41.16834001, 0.01259951, 4.116834, 0.04591579, -34.32770091, -0.00082511, -41.16834001, -0.01259951, -4.116834, -0.04591579, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 34.32770091, 0.00082511, 41.16834001, 0.01259951, 4.116834, 0.04591579, -34.32770091, -0.00082511, -41.16834001, -0.01259951, -4.116834, -0.04591579, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 68.52291169, 0.01650217, 68.52291169, 0.04950651, 47.96603819, -837.36716071, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 17.13072792, 8.569e-05, 51.39218377, 0.00025707, 171.30727923, 0.00085689, -17.13072792, -8.569e-05, -51.39218377, -0.00025707, -171.30727923, -0.00085689, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 68.52291169, 0.01650217, 68.52291169, 0.04950651, 47.96603819, -837.36716071, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 17.13072792, 8.569e-05, 51.39218377, 0.00025707, 171.30727923, 0.00085689, -17.13072792, -8.569e-05, -51.39218377, -0.00025707, -171.30727923, -0.00085689, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 18.75, 12.75, 6.075)
    ops.node(123023, 18.75, 12.75, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.0875, 27702802.19409181, 11542834.24753826, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 50.01503076, 0.00074722, 60.10717127, 0.01372426, 6.01071713, 0.03947069, -50.01503076, -0.00074722, -60.10717127, -0.01372426, -6.01071713, -0.03947069, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 71.79246038, 0.00059488, 86.27889749, 0.01499211, 8.62788975, 0.04793084, -71.79246038, -0.00059488, -86.27889749, -0.01499211, -8.62788975, -0.04793084, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 86.47810329, 0.01494434, 86.47810329, 0.04483303, 60.53467231, -908.45900157, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 21.61952582, 7.449e-05, 64.85857747, 0.00022347, 216.19525824, 0.00074491, -21.61952582, -7.449e-05, -64.85857747, -0.00022347, -216.19525824, -0.00074491, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 96.01008151, 0.0118975, 96.01008151, 0.03569251, 67.20705706, -1119.38305563, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 24.00252038, 8.27e-05, 72.00756113, 0.00024811, 240.02520377, 0.00082702, -24.00252038, -8.27e-05, -72.00756113, -0.00024811, -240.02520377, -0.00082702, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 24.05, 12.75, 6.075)
    ops.node(123024, 24.05, 12.75, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 27000677.76734246, 11250282.40305936, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 32.78318898, 0.00078724, 39.52674165, 0.01537374, 3.95267416, 0.05520806, -32.78318898, -0.00078724, -39.52674165, -0.01537374, -3.95267416, -0.05520806, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 35.16620321, 0.00078724, 42.39994559, 0.01537374, 4.23999456, 0.05520806, -35.16620321, -0.00078724, -42.39994559, -0.01537374, -4.23999456, -0.05520806, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 67.77000358, 0.01574483, 67.77000358, 0.04723448, 47.43900251, -837.87265357, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 16.9425009, 8.385e-05, 50.82750269, 0.00025156, 169.42500896, 0.00083852, -16.9425009, -8.385e-05, -50.82750269, -0.00025156, -169.42500896, -0.00083852, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 67.77000358, 0.01574483, 67.77000358, 0.04723448, 47.43900251, -837.87265357, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 16.9425009, 8.385e-05, 50.82750269, 0.00025156, 169.42500896, 0.00083852, -16.9425009, -8.385e-05, -50.82750269, -0.00025156, -169.42500896, -0.00083852, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.975)
    ops.node(124001, 0.0, 0.0, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 24943545.87512372, 10393144.11463489, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 18.81656697, 0.00068242, 23.01152648, 0.01684312, 2.30115265, 0.07029182, -18.81656697, -0.00068242, -23.01152648, -0.01684312, -2.30115265, -0.07029182, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 18.81656697, 0.00068242, 23.01152648, 0.01684312, 2.30115265, 0.07029182, -18.81656697, -0.00068242, -23.01152648, -0.01684312, -2.30115265, -0.07029182, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 52.95094233, 0.01364845, 52.95094233, 0.04094535, 37.06565963, -824.67443069, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 13.23773558, 7.092e-05, 39.71320675, 0.00021276, 132.37735582, 0.0007092, -13.23773558, -7.092e-05, -39.71320675, -0.00021276, -132.37735582, -0.0007092, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 52.95094233, 0.01364845, 52.95094233, 0.04094535, 37.06565963, -824.67443069, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 13.23773558, 7.092e-05, 39.71320675, 0.00021276, 132.37735582, 0.0007092, -13.23773558, -7.092e-05, -39.71320675, -0.00021276, -132.37735582, -0.0007092, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 5.3, 0.0, 8.975)
    ops.node(124002, 5.3, 0.0, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0875, 31353794.47060417, 13064081.02941841, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 27.90284965, 0.00069533, 33.66338344, 0.01429518, 3.36633834, 0.05917968, -27.90284965, -0.00069533, -33.66338344, -0.01429518, -3.36633834, -0.05917968, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 43.56239149, 0.0005549, 52.55583235, 0.0157205, 5.25558324, 0.07384473, -43.56239149, -0.0005549, -52.55583235, -0.0157205, -5.25558324, -0.07384473, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 83.08568845, 0.0139066, 83.08568845, 0.04171981, 58.15998192, -727.69881269, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 20.77142211, 6.324e-05, 62.31426634, 0.00018971, 207.71422113, 0.00063235, -20.77142211, -6.324e-05, -62.31426634, -0.00018971, -207.71422113, -0.00063235, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 92.14745886, 0.01109798, 92.14745886, 0.03329393, 64.5032212, -1049.85202286, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 23.03686471, 7.013e-05, 69.11059414, 0.0002104, 230.36864714, 0.00070132, -23.03686471, -7.013e-05, -69.11059414, -0.0002104, -230.36864714, -0.00070132, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 18.75, 0.0, 8.975)
    ops.node(124005, 18.75, 0.0, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0875, 27359386.6769002, 11399744.44870842, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 28.10197906, 0.00069971, 34.19271771, 0.0132039, 3.41927177, 0.05458638, -28.10197906, -0.00069971, -34.19271771, -0.0132039, -3.41927177, -0.05458638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 44.1171019, 0.00056075, 53.67891024, 0.01450457, 5.36789102, 0.06809378, -44.1171019, -0.00056075, -53.67891024, -0.01450457, -5.36789102, -0.06809378, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 65.32350548, 0.0139941, 65.32350548, 0.04198231, 45.72645384, -646.39887606, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 16.33087637, 5.698e-05, 48.99262911, 0.00017093, 163.30876371, 0.00056975, -16.33087637, -5.698e-05, -48.99262911, -0.00017093, -163.30876371, -0.00056975, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 78.14980385, 0.01121507, 78.14980385, 0.03364522, 54.7048627, -913.81030678, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 19.53745096, 6.816e-05, 58.61235289, 0.00020449, 195.37450963, 0.00068162, -19.53745096, -6.816e-05, -58.61235289, -0.00020449, -195.37450963, -0.00068162, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 24.05, 0.0, 8.975)
    ops.node(124006, 24.05, 0.0, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 27619262.23555664, 11508025.93148193, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 18.25537998, 0.00070282, 22.244506, 0.01502459, 2.2244506, 0.07205359, -18.25537998, -0.00070282, -22.244506, -0.01502459, -2.2244506, -0.07205359, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 18.25537998, 0.00070282, 22.244506, 0.01502459, 2.2244506, 0.07205359, -18.25537998, -0.00070282, -22.244506, -0.01502459, -2.2244506, -0.07205359, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 49.38543189, 0.01405648, 49.38543189, 0.04216944, 34.56980232, -680.01646147, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 12.34635797, 5.974e-05, 37.03907392, 0.00017921, 123.46357973, 0.00059736, -12.34635797, -5.974e-05, -37.03907392, -0.00017921, -123.46357973, -0.00059736, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 49.38543189, 0.01405648, 49.38543189, 0.04216944, 34.56980232, -680.01646147, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 12.34635797, 5.974e-05, 37.03907392, 0.00017921, 123.46357973, 0.00059736, -12.34635797, -5.974e-05, -37.03907392, -0.00017921, -123.46357973, -0.00059736, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.25, 8.95)
    ops.node(124007, 0.0, 4.25, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0875, 26854748.06555718, 11189478.36064883, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 45.97468294, 0.0005881, 55.96866253, 0.01802647, 5.59686625, 0.06360233, -45.97468294, -0.0005881, -55.96866253, -0.01802647, -5.59686625, -0.06360233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 31.26390855, 0.0007631, 38.06005903, 0.01648128, 3.8060059, 0.05210548, -31.26390855, -0.0007631, -38.06005903, -0.01648128, -3.8060059, -0.05210548, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 79.70597937, 0.011762, 79.70597937, 0.03528601, 55.79418556, -1007.63017569, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 19.92649484, 7.083e-05, 59.77948453, 0.00021248, 199.26494843, 0.00070826, -19.92649484, -7.083e-05, -59.77948453, -0.00021248, -199.26494843, -0.00070826, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 68.50495818, 0.01526199, 68.50495818, 0.04578596, 47.95347073, -704.68507976, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 17.12623955, 6.087e-05, 51.37871864, 0.00018262, 171.26239545, 0.00060873, -17.12623955, -6.087e-05, -51.37871864, -0.00018262, -171.26239545, -0.00060873, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 5.3, 4.25, 8.95)
    ops.node(124008, 5.3, 4.25, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.175, 26556215.30374904, 11065089.70989543, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 111.62808299, 0.0004827, 136.12640512, 0.0136606, 13.61264051, 0.04401823, -111.62808299, -0.0004827, -136.12640512, -0.0136606, -13.61264051, -0.04401823, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 75.13319613, 0.00057654, 91.62221208, 0.01264282, 9.16222121, 0.03727381, -75.13319613, -0.00057654, -91.62221208, -0.01264282, -9.16222121, -0.03727381, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 133.96489095, 0.00965405, 133.96489095, 0.02896216, 93.77542366, -1000.43838772, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 33.49122274, 6.019e-05, 100.47366821, 0.00018057, 334.91222736, 0.00060189, -33.49122274, -6.019e-05, -100.47366821, -0.00018057, -334.91222736, -0.00060189, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 113.03946276, 0.01153077, 113.03946276, 0.03459232, 79.12762393, -751.331763, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 28.25986569, 5.079e-05, 84.77959707, 0.00015236, 282.5986569, 0.00050787, -28.25986569, -5.079e-05, -84.77959707, -0.00015236, -282.5986569, -0.00050787, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 10.6, 4.25, 8.95)
    ops.node(124009, 10.6, 4.25, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.14, 27130694.05868257, 11304455.8577844, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 82.4045796, 0.00053598, 100.38991654, 0.01637346, 10.03899165, 0.05346621, -82.4045796, -0.00053598, -100.38991654, -0.01637346, -10.03899165, -0.05346621, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 64.8567187, 0.00057702, 79.01212055, 0.01581829, 7.90121205, 0.04968392, -64.8567187, -0.00057702, -79.01212055, -0.01581829, -7.90121205, -0.04968392, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 113.40942392, 0.01071964, 113.40942392, 0.03215891, 79.38659674, -1161.58398851, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 28.35235598, 6.234e-05, 85.05706794, 0.00018703, 283.5235598, 0.00062343, -28.35235598, -6.234e-05, -85.05706794, -0.00018703, -283.5235598, -0.00062343, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 108.90880392, 0.0115403, 108.90880392, 0.0346209, 76.23616275, -1011.94142063, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 27.22720098, 5.987e-05, 81.68160294, 0.00017961, 272.27200981, 0.00059869, -27.22720098, -5.987e-05, -81.68160294, -0.00017961, -272.27200981, -0.00059869, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 13.45, 4.25, 8.95)
    ops.node(124010, 13.45, 4.25, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.14, 29243043.96823517, 12184601.65343132, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 81.04458329, 0.00051858, 98.34959787, 0.01558736, 9.83495979, 0.05436906, -81.04458329, -0.00051858, -98.34959787, -0.01558736, -9.83495979, -0.05436906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 63.88447269, 0.00055658, 77.52538102, 0.0150581, 7.7525381, 0.05046573, -63.88447269, -0.00055658, -77.52538102, -0.0150581, -7.7525381, -0.05046573, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 117.03410211, 0.01037166, 117.03410211, 0.03111499, 81.92387147, -999.22630154, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 29.25852553, 5.969e-05, 87.77557658, 0.00017907, 292.58525527, 0.00059689, -29.25852553, -5.969e-05, -87.77557658, -0.00017907, -292.58525527, -0.00059689, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 113.14572459, 0.01113169, 113.14572459, 0.03339506, 79.20200721, -879.0325944, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 28.28643115, 5.771e-05, 84.85929344, 0.00017312, 282.86431147, 0.00057706, -28.28643115, -5.771e-05, -84.85929344, -0.00017312, -282.86431147, -0.00057706, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 18.75, 4.25, 8.95)
    ops.node(124011, 18.75, 4.25, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.175, 28671760.90721378, 11946567.04467241, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 121.9051734, 0.00048207, 148.1325403, 0.01148466, 14.81325403, 0.0433197, -121.9051734, -0.00048207, -148.1325403, -0.01148466, -14.81325403, -0.0433197, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 83.10033006, 0.00056484, 100.979004, 0.01063931, 10.0979004, 0.03646901, -83.10033006, -0.00056484, -100.979004, -0.01063931, -10.0979004, -0.03646901, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 140.29889113, 0.00964139, 140.29889113, 0.02892416, 98.20922379, -853.50970559, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 35.07472278, 5.838e-05, 105.22416834, 0.00017515, 350.74722782, 0.00058384, -35.07472278, -5.838e-05, -105.22416834, -0.00017515, -350.74722782, -0.00058384, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 109.92997954, 0.01129673, 109.92997954, 0.03389019, 76.95098568, -661.52140357, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 27.48249489, 4.575e-05, 82.44748466, 0.00013724, 274.82494885, 0.00045746, -27.48249489, -4.575e-05, -82.44748466, -0.00013724, -274.82494885, -0.00045746, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 24.05, 4.25, 8.95)
    ops.node(124012, 24.05, 4.25, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0875, 27097960.93096611, 11290817.05456921, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 47.45975912, 0.00058091, 57.75812506, 0.01646165, 5.77581251, 0.06236488, -47.45975912, -0.00058091, -57.75812506, -0.01646165, -5.77581251, -0.06236488, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 32.37055048, 0.00074241, 39.39468589, 0.01505662, 3.93946859, 0.0509367, -32.37055048, -0.00074241, -39.39468589, -0.01505662, -3.93946859, -0.0509367, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 75.87794668, 0.01161818, 75.87794668, 0.03485453, 53.11456267, -847.92338792, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 18.96948667, 6.682e-05, 56.90846001, 0.00020046, 189.69486669, 0.00066819, -18.96948667, -6.682e-05, -56.90846001, -0.00020046, -189.69486669, -0.00066819, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 58.74865371, 0.0148482, 58.74865371, 0.0445446, 41.12405759, -608.68644652, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 14.68716343, 5.173e-05, 44.06149028, 0.0001552, 146.87163427, 0.00051735, -14.68716343, -5.173e-05, -44.06149028, -0.0001552, -146.87163427, -0.00051735, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 8.5, 8.95)
    ops.node(124013, 0.0, 8.5, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0875, 24152070.68565962, 10063362.78569151, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 48.40270346, 0.00058648, 59.04363838, 0.01777943, 5.90436384, 0.05891362, -48.40270346, -0.00058648, -59.04363838, -0.01777943, -5.90436384, -0.05891362, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 33.06413561, 0.00074485, 40.33301297, 0.01624181, 4.0333013, 0.04839419, -33.06413561, -0.00074485, -40.33301297, -0.01624181, -4.0333013, -0.04839419, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 72.36672999, 0.01172969, 72.36672999, 0.03518908, 50.65671099, -974.74597079, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 18.0916825, 7.15e-05, 54.27504749, 0.0002145, 180.91682497, 0.000715, -18.0916825, -7.15e-05, -54.27504749, -0.0002145, -180.91682497, -0.000715, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 63.08111835, 0.01489694, 63.08111835, 0.04469083, 44.15678285, -685.01838329, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 15.77027959, 6.233e-05, 47.31083876, 0.00018698, 157.70279588, 0.00062326, -15.77027959, -6.233e-05, -47.31083876, -0.00018698, -157.70279588, -0.00062326, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 5.3, 8.5, 8.95)
    ops.node(124014, 5.3, 8.5, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.175, 29016221.44054347, 12090092.26689311, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 115.94894192, 0.00047929, 140.79452087, 0.01272971, 14.07945209, 0.0447682, -115.94894192, -0.00047929, -140.79452087, -0.01272971, -14.07945209, -0.0447682, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 78.47027313, 0.0005667, 95.28491011, 0.01178374, 9.52849101, 0.03777851, -78.47027313, -0.0005667, -95.28491011, -0.01178374, -9.52849101, -0.03777851, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 145.08140532, 0.00958587, 145.08140532, 0.0287576, 101.55698372, -931.04708099, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 36.27035133, 5.966e-05, 108.81105399, 0.00017897, 362.70351329, 0.00059657, -36.27035133, -5.966e-05, -108.81105399, -0.00017897, -362.70351329, -0.00059657, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 119.62361795, 0.01133406, 119.62361795, 0.03400217, 83.73653257, -709.09199703, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 29.90590449, 4.919e-05, 89.71771347, 0.00014757, 299.05904488, 0.00049189, -29.90590449, -4.919e-05, -89.71771347, -0.00014757, -299.05904488, -0.00049189, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 10.6, 8.5, 8.95)
    ops.node(124015, 10.6, 8.5, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0875, 26603213.48738837, 11084672.28641182, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 51.96207114, 0.0005941, 63.12875316, 0.01479867, 6.31287532, 0.05696948, -51.96207114, -0.0005941, -63.12875316, -0.01479867, -6.31287532, -0.05696948, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 35.55268227, 0.00076137, 43.19297623, 0.01356475, 4.31929762, 0.04652739, -35.55268227, -0.00076137, -43.19297623, -0.01356475, -4.31929762, -0.04652739, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 74.17600867, 0.01188201, 74.17600867, 0.03564604, 51.92320607, -756.79691844, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 18.54400217, 6.654e-05, 55.6320065, 0.00019961, 185.44002167, 0.00066535, -18.54400217, -6.654e-05, -55.6320065, -0.00019961, -185.44002167, -0.00066535, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 53.58671877, 0.01522734, 53.58671877, 0.04568201, 37.51070314, -577.51447392, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 13.39667969, 4.807e-05, 40.19003908, 0.0001442, 133.96679692, 0.00048067, -13.39667969, -4.807e-05, -40.19003908, -0.0001442, -133.96679692, -0.00048067, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 13.45, 8.5, 8.95)
    ops.node(124016, 13.45, 8.5, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0875, 27950575.30038399, 11646073.04182666, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 53.10013619, 0.00057987, 64.41123953, 0.01472793, 6.44112395, 0.05899433, -53.10013619, -0.00057987, -64.41123953, -0.01472793, -6.44112395, -0.05899433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 36.50392991, 0.00073213, 44.2797993, 0.01348458, 4.42797993, 0.04808524, -36.50392991, -0.00073213, -44.2797993, -0.01348458, -4.42797993, -0.04808524, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 77.5674536, 0.0115975, 77.5674536, 0.03479249, 54.29721752, -756.77611084, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 19.3918634, 6.622e-05, 58.1755902, 0.00019867, 193.91863401, 0.00066223, -19.3918634, -6.622e-05, -58.1755902, -0.00019867, -193.91863401, -0.00066223, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 56.38550183, 0.0146427, 56.38550183, 0.0439281, 39.46985128, -577.50149059, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 14.09637546, 4.814e-05, 42.28912638, 0.00014442, 140.96375458, 0.00048139, -14.09637546, -4.814e-05, -42.28912638, -0.00014442, -140.96375458, -0.00048139, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 18.75, 8.5, 8.95)
    ops.node(124017, 18.75, 8.5, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.175, 24553990.24856355, 10230829.27023481, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 113.37671099, 0.00048425, 138.5286671, 0.01188975, 13.85286671, 0.04039566, -113.37671099, -0.00048425, -138.5286671, -0.01188975, -13.85286671, -0.04039566, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 76.5140786, 0.00057547, 93.48827666, 0.01101886, 9.34882767, 0.03414744, -76.5140786, -0.00057547, -93.48827666, -0.01101886, -9.34882767, -0.03414744, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 117.59115486, 0.00968509, 117.59115486, 0.02905527, 82.3138084, -837.49133944, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 29.39778871, 5.714e-05, 88.19336614, 0.00017142, 293.97788715, 0.00057141, -29.39778871, -5.714e-05, -88.19336614, -0.00017142, -293.97788715, -0.00057141, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 90.31137721, 0.01150941, 90.31137721, 0.03452822, 63.21796405, -651.64030523, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 22.5778443, 4.388e-05, 67.73353291, 0.00013165, 225.77844303, 0.00043885, -22.5778443, -4.388e-05, -67.73353291, -0.00013165, -225.77844303, -0.00043885, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 24.05, 8.5, 8.95)
    ops.node(124018, 24.05, 8.5, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0875, 28304493.96892123, 11793539.15371718, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 48.15785501, 0.00057518, 58.49711226, 0.01580043, 5.84971123, 0.06318243, -48.15785501, -0.00057518, -58.49711226, -0.01580043, -5.84971123, -0.06318243, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 32.92229674, 0.0007301, 39.99055373, 0.01445348, 3.99905537, 0.05148943, -32.92229674, -0.0007301, -39.99055373, -0.01445348, -3.99905537, -0.05148943, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 77.62145177, 0.01150351, 77.62145177, 0.03451053, 54.33501624, -804.20714684, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 19.40536294, 6.544e-05, 58.21608883, 0.00019632, 194.05362942, 0.00065441, -19.40536294, -6.544e-05, -58.21608883, -0.00019632, -194.05362942, -0.00065441, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 58.28532444, 0.01460199, 58.28532444, 0.04380598, 40.79972711, -582.17494567, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 14.57133111, 4.914e-05, 43.71399333, 0.00014742, 145.71331111, 0.00049139, -14.57133111, -4.914e-05, -43.71399333, -0.00014742, -145.71331111, -0.00049139, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 12.75, 8.975)
    ops.node(124019, 0.0, 12.75, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 27133387.67270502, 11305578.19696043, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 18.27511078, 0.00069181, 22.28700924, 0.01764822, 2.22870092, 0.07412277, -18.27511078, -0.00069181, -22.28700924, -0.01764822, -2.22870092, -0.07412277, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 18.27511078, 0.00069181, 22.28700924, 0.01764822, 2.22870092, 0.07412277, -18.27511078, -0.00069181, -22.28700924, -0.01764822, -2.22870092, -0.07412277, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 57.60216734, 0.01383614, 57.60216734, 0.04150841, 40.32151714, -868.38037563, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 14.40054184, 7.092e-05, 43.20162551, 0.00021277, 144.00541835, 0.00070923, -14.40054184, -7.092e-05, -43.20162551, -0.00021277, -144.00541835, -0.00070923, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 57.60216734, 0.01383614, 57.60216734, 0.04150841, 40.32151714, -868.38037563, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 14.40054184, 7.092e-05, 43.20162551, 0.00021277, 144.00541835, 0.00070923, -14.40054184, -7.092e-05, -43.20162551, -0.00021277, -144.00541835, -0.00070923, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 5.3, 12.75, 8.975)
    ops.node(124020, 5.3, 12.75, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0875, 27590504.44164147, 11496043.51735061, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 32.46829859, 0.00077314, 39.49162317, 0.01360042, 3.94916232, 0.05014066, -32.46829859, -0.00077314, -39.49162317, -0.01360042, -3.94916232, -0.05014066, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 47.72058848, 0.00059821, 58.04318611, 0.0148293, 5.80431861, 0.06157711, -47.72058848, -0.00059821, -58.04318611, -0.0148293, -5.80431861, -0.06157711, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 53.86241226, 0.01546272, 53.86241226, 0.04638817, 37.70368858, -556.9358462, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 13.46560306, 4.659e-05, 40.39680919, 0.00013976, 134.65603064, 0.00046585, -13.46560306, -4.659e-05, -40.39680919, -0.00013976, -134.65603064, -0.00046585, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 74.45921634, 0.01196421, 74.45921634, 0.03589262, 52.12145144, -765.87535953, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 18.61480408, 6.44e-05, 55.84441225, 0.0001932, 186.14804084, 0.00064399, -18.61480408, -6.44e-05, -55.84441225, -0.0001932, -186.14804084, -0.00064399, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 10.6, 12.75, 8.975)
    ops.node(124021, 10.6, 12.75, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 27248955.30484546, 11353731.37701894, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 21.10369296, 0.00074941, 25.66504513, 0.01661197, 2.56650451, 0.06901328, -21.10369296, -0.00074941, -25.66504513, -0.01661197, -2.56650451, -0.06901328, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 21.10369296, 0.00074941, 25.66504513, 0.01661197, 2.56650451, 0.06901328, -21.10369296, -0.00074941, -25.66504513, -0.01661197, -2.56650451, -0.06901328, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 59.86668567, 0.01498812, 59.86668567, 0.04496435, 41.90667997, -781.39263682, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 14.96667142, 7.34e-05, 44.90001425, 0.00022019, 149.66671417, 0.00073398, -14.96667142, -7.34e-05, -44.90001425, -0.00022019, -149.66671417, -0.00073398, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 59.86668567, 0.01498812, 59.86668567, 0.04496435, 41.90667997, -781.39263682, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 14.96667142, 7.34e-05, 44.90001425, 0.00022019, 149.66671417, 0.00073398, -14.96667142, -7.34e-05, -44.90001425, -0.00022019, -149.66671417, -0.00073398, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 13.45, 12.75, 8.975)
    ops.node(124022, 13.45, 12.75, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0625, 26975625.92201541, 11239844.13417309, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 21.39725509, 0.00070742, 26.03130167, 0.01479353, 2.60313017, 0.06675803, -21.39725509, -0.00070742, -26.03130167, -0.01479353, -2.60313017, -0.06675803, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 21.39725509, 0.00070742, 26.03130167, 0.01479353, 2.60313017, 0.06675803, -21.39725509, -0.00070742, -26.03130167, -0.01479353, -2.60313017, -0.06675803, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 52.31270782, 0.01414833, 52.31270782, 0.042445, 36.61889547, -639.00356921, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 13.07817695, 6.479e-05, 39.23453086, 0.00019436, 130.78176955, 0.00064787, -13.07817695, -6.479e-05, -39.23453086, -0.00019436, -130.78176955, -0.00064787, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 52.31270782, 0.01414833, 52.31270782, 0.042445, 36.61889547, -639.00356921, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 13.07817695, 6.479e-05, 39.23453086, 0.00019436, 130.78176955, 0.00064787, -13.07817695, -6.479e-05, -39.23453086, -0.00019436, -130.78176955, -0.00064787, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 18.75, 12.75, 8.975)
    ops.node(124023, 18.75, 12.75, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.0875, 27815675.0894088, 11589864.620587, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 32.59499566, 0.00079314, 39.63157793, 0.01592346, 3.96315779, 0.05267563, -32.59499566, -0.00079314, -39.63157793, -0.01592346, -3.96315779, -0.05267563, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 47.95780827, 0.00060914, 58.31090256, 0.01739531, 5.83109026, 0.06441425, -47.95780827, -0.00060914, -58.31090256, -0.01739531, -5.83109026, -0.06441425, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 72.51160836, 0.0158628, 72.51160836, 0.04758841, 50.75812585, -710.97641153, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 18.12790209, 6.221e-05, 54.38370627, 0.00018662, 181.2790209, 0.00062207, -18.12790209, -6.221e-05, -54.38370627, -0.00018662, -181.2790209, -0.00062207, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 82.18976525, 0.01218283, 82.18976525, 0.0365485, 57.53283568, -1021.75911078, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 20.54744131, 7.051e-05, 61.64232394, 0.00021153, 205.47441313, 0.0007051, -20.54744131, -7.051e-05, -61.64232394, -0.00021153, -205.47441313, -0.0007051, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 24.05, 12.75, 8.975)
    ops.node(124024, 24.05, 12.75, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 30982920.86371937, 12909550.35988307, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 19.44484203, 0.00065913, 23.51248724, 0.01756732, 2.35124872, 0.07758111, -19.44484203, -0.00065913, -23.51248724, -0.01756732, -2.35124872, -0.07758111, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 19.44484203, 0.00065913, 23.51248724, 0.01756732, 2.35124872, 0.07758111, -19.44484203, -0.00065913, -23.51248724, -0.01756732, -2.35124872, -0.07758111, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 66.67889065, 0.01318263, 66.67889065, 0.0395479, 46.67522345, -970.16061263, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 16.66972266, 7.19e-05, 50.00916799, 0.00021569, 166.69722662, 0.00071898, -16.66972266, -7.19e-05, -50.00916799, -0.00021569, -166.69722662, -0.00071898, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 66.67889065, 0.01318263, 66.67889065, 0.0395479, 46.67522345, -970.16061263, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 16.66972266, 7.19e-05, 50.00916799, 0.00021569, 166.69722662, 0.00071898, -16.66972266, -7.19e-05, -50.00916799, -0.00021569, -166.69722662, -0.00071898, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 10.6, 0.0, 0.0)
    ops.node(124025, 10.6, 0.0, 1.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.14, 25666792.77718947, 10694496.99049561, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 147.17561667, 0.00051614, 175.60891189, 0.01434284, 17.56089119, 0.03644389, -147.17561667, -0.00051614, -175.60891189, -0.01434284, -17.56089119, -0.03644389, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 148.56553917, 0.0005004, 177.26735764, 0.01493665, 17.72673576, 0.03941916, -148.56553917, -0.0005004, -177.26735764, -0.01493665, -17.72673576, -0.03941916, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 193.45782141, 0.01032283, 193.45782141, 0.03096848, 135.42047499, -3260.84778951, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 48.36445535, 5.621e-05, 145.09336606, 0.00016862, 483.64455354, 0.00056207, -48.36445535, -5.621e-05, -145.09336606, -0.00016862, -483.64455354, -0.00056207, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 221.09465304, 0.01000808, 221.09465304, 0.03002425, 154.76625713, -3481.93856365, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 55.27366326, 6.424e-05, 165.82098978, 0.00019271, 552.73663261, 0.00064236, -55.27366326, -6.424e-05, -165.82098978, -0.00019271, -552.73663261, -0.00064236, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 10.6, 0.0, 1.675)
    ops.node(121003, 10.6, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.14, 26808357.15137665, 11170148.81307361, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 125.63680369, 0.00050313, 150.43405176, 0.02018806, 15.04340518, 0.05322929, -125.63680369, -0.00050313, -150.43405176, -0.02018806, -15.04340518, -0.05322929, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 134.28805802, 0.00048928, 160.79282565, 0.02110085, 16.07928256, 0.05795145, -134.28805802, -0.00048928, -160.79282565, -0.02110085, -16.07928256, -0.05795145, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 221.90144238, 0.01006268, 221.90144238, 0.03018804, 155.33100966, -4273.95462912, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 55.47536059, 6.173e-05, 166.42608178, 0.00018518, 554.75360594, 0.00061725, -55.47536059, -6.173e-05, -166.42608178, -0.00018518, -554.75360594, -0.00061725, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 253.60164843, 0.00978563, 253.60164843, 0.02935689, 177.5211539, -4716.58783044, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 63.40041211, 7.054e-05, 190.20123632, 0.00021163, 634.00412107, 0.00070543, -63.40041211, -7.054e-05, -190.20123632, -0.00021163, -634.00412107, -0.00070543, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.45, 0.0, 0.0)
    ops.node(124026, 13.45, 0.0, 1.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.14, 24880890.57703248, 10367037.7404302, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 144.99560722, 0.0005161, 172.6956454, 0.01448467, 17.26956454, 0.03448053, -144.99560722, -0.0005161, -172.6956454, -0.01448467, -17.26956454, -0.03448053, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 146.5534436, 0.00050009, 174.55109167, 0.01508446, 17.45510917, 0.03723495, -146.5534436, -0.00050009, -174.55109167, -0.01508446, -17.45510917, -0.03723495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 192.63205484, 0.01032191, 192.63205484, 0.03096574, 134.84243838, -3448.83017929, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 48.15801371, 5.773e-05, 144.47404113, 0.0001732, 481.58013709, 0.00057734, -48.15801371, -5.773e-05, -144.47404113, -0.0001732, -481.58013709, -0.00057734, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 220.15091981, 0.01000181, 220.15091981, 0.03000543, 154.10564387, -3704.26893534, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 55.03772995, 6.598e-05, 165.11318986, 0.00019795, 550.37729953, 0.00065982, -55.03772995, -6.598e-05, -165.11318986, -0.00019795, -550.37729953, -0.00065982, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 13.45, 0.0, 1.675)
    ops.node(121004, 13.45, 0.0, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.14, 28680485.7933369, 11950202.41389037, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 128.27217544, 0.00050689, 153.65025013, 0.02055958, 15.36502501, 0.05890495, -128.27217544, -0.00050689, -153.65025013, -0.02055958, -15.36502501, -0.05890495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 137.20822336, 0.00049264, 164.35425506, 0.02148929, 16.43542551, 0.06425554, -137.20822336, -0.00049264, -164.35425506, -0.02148929, -16.43542551, -0.06425554, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 232.42555399, 0.01013773, 232.42555399, 0.03041319, 162.6978878, -4160.64981278, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 58.1063885, 6.043e-05, 174.3191655, 0.0001813, 581.06388499, 0.00060432, -58.1063885, -6.043e-05, -174.3191655, -0.0001813, -581.06388499, -0.00060432, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 265.62920456, 0.00985281, 265.62920456, 0.02955843, 185.9404432, -4580.63670536, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 66.40730114, 6.907e-05, 199.22190342, 0.0002072, 664.07301141, 0.00069066, -66.40730114, -6.907e-05, -199.22190342, -0.0002072, -664.07301141, -0.00069066, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 10.6, 0.0, 3.175)
    ops.node(124027, 10.6, 0.0, 4.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.14, 28282769.70136286, 11784487.37556786, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 103.53342542, 0.00049512, 124.56972181, 0.01237886, 12.45697218, 0.03779437, -103.53342542, -0.00049512, -124.56972181, -0.01237886, -12.45697218, -0.03779437, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 114.41948785, 0.00048193, 137.66765383, 0.01283053, 13.76676538, 0.04066793, -114.41948785, -0.00048193, -137.66765383, -0.01283053, -13.76676538, -0.04066793, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 187.40703727, 0.00990239, 187.40703727, 0.02970718, 131.18492609, -2453.77662423, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 46.85175932, 4.941e-05, 140.55527795, 0.00014824, 468.51759318, 0.00049412, -46.85175932, -4.941e-05, -140.55527795, -0.00014824, -468.51759318, -0.00049412, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 214.17947117, 0.00963853, 214.17947117, 0.02891558, 149.92562982, -2626.09569333, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 53.54486779, 5.647e-05, 160.63460338, 0.00016941, 535.44867792, 0.00056471, -53.54486779, -5.647e-05, -160.63460338, -0.00016941, -535.44867792, -0.00056471, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 10.6, 0.0, 4.575)
    ops.node(122003, 10.6, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.14, 26324114.902863, 10968381.20952625, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 97.47830091, 0.00049653, 117.53407361, 0.01207776, 11.75340736, 0.03566223, -97.47830091, -0.00049653, -117.53407361, -0.01207776, -11.75340736, -0.03566223, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 107.63729439, 0.00048291, 129.78323959, 0.01251717, 12.97832396, 0.03834906, -107.63729439, -0.00048291, -129.78323959, -0.01251717, -12.97832396, -0.03834906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 168.96788313, 0.00993063, 168.96788313, 0.02979189, 118.27751819, -2277.64167191, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 42.24197078, 4.787e-05, 126.72591235, 0.0001436, 422.41970782, 0.00047866, -42.24197078, -4.787e-05, -126.72591235, -0.0001436, -422.41970782, -0.00047866, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 193.10615215, 0.00965828, 193.10615215, 0.02897485, 135.1743065, -2443.25263111, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 48.27653804, 5.47e-05, 144.82961411, 0.00016411, 482.76538036, 0.00054703, -48.27653804, -5.47e-05, -144.82961411, -0.00016411, -482.76538036, -0.00054703, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.45, 0.0, 3.175)
    ops.node(124028, 13.45, 0.0, 4.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.14, 27256701.24617767, 11356958.85257403, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 103.52746279, 0.00050381, 124.60956829, 0.01163567, 12.46095683, 0.03547502, -103.52746279, -0.00050381, -124.60956829, -0.01163567, -12.46095683, -0.03547502, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 114.51310426, 0.00048924, 137.8323017, 0.01205654, 13.78323017, 0.0381676, -114.51310426, -0.00048924, -137.8323017, -0.01205654, -13.78323017, -0.0381676, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 178.37228859, 0.01007612, 178.37228859, 0.03022837, 124.86060201, -2360.45100914, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 44.59307215, 4.88e-05, 133.77921644, 0.0001464, 445.93072146, 0.00048801, -44.59307215, -4.88e-05, -133.77921644, -0.0001464, -445.93072146, -0.00048801, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 203.8540441, 0.00978472, 203.8540441, 0.02935415, 142.69783087, -2515.86831811, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 50.96351102, 5.577e-05, 152.89053307, 0.00016732, 509.63511024, 0.00055772, -50.96351102, -5.577e-05, -152.89053307, -0.00016732, -509.63511024, -0.00055772, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 13.45, 0.0, 4.575)
    ops.node(122004, 13.45, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.14, 28220159.65726018, 11758399.85719174, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 94.0326032, 0.0004718, 113.31527545, 0.01177728, 11.33152755, 0.03827666, -94.0326032, -0.0004718, -113.31527545, -0.01177728, -11.33152755, -0.03827666, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 103.90750767, 0.00046117, 125.21516424, 0.01220889, 12.52151642, 0.04123346, -103.90750767, -0.00046117, -125.21516424, -0.01220889, -12.52151642, -0.04123346, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 179.42194617, 0.00943603, 179.42194617, 0.0283081, 125.59536232, -2197.67430751, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 44.85548654, 4.741e-05, 134.56645963, 0.00014224, 448.55486542, 0.00047412, -44.85548654, -4.741e-05, -134.56645963, -0.00014224, -448.55486542, -0.00047412, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 205.05365276, 0.00922346, 205.05365276, 0.02767038, 143.53755693, -2348.68453965, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 51.26341319, 5.419e-05, 153.79023957, 0.00016256, 512.63413191, 0.00054185, -51.26341319, -5.419e-05, -153.79023957, -0.00016256, -512.63413191, -0.00054185, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 10.6, 0.0, 6.075)
    ops.node(124029, 10.6, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.105, 28301146.85745252, 11792144.52393855, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 61.39176676, 0.00050011, 74.0385174, 0.0125435, 7.40385174, 0.04243283, -61.39176676, -0.00050011, -74.0385174, -0.0125435, -7.40385174, -0.04243283, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 72.44529243, 0.00047925, 87.36907776, 0.01309404, 8.73690778, 0.04645747, -72.44529243, -0.00047925, -87.36907776, -0.01309404, -8.73690778, -0.04645747, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 120.32699299, 0.01000223, 120.32699299, 0.03000668, 84.22889509, -1754.97502473, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 30.08174825, 4.227e-05, 90.24524474, 0.00012682, 300.81748248, 0.00042274, -30.08174825, -4.227e-05, -90.24524474, -0.00012682, -300.81748248, -0.00042274, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 140.38149182, 0.00958492, 140.38149182, 0.02875477, 98.26704428, -1923.44511485, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 35.09537296, 4.932e-05, 105.28611887, 0.00014796, 350.95372956, 0.00049319, -35.09537296, -4.932e-05, -105.28611887, -0.00014796, -350.95372956, -0.00049319, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 10.6, 0.0, 7.45)
    ops.node(123003, 10.6, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.105, 26069730.30643025, 10862387.62767927, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 56.31036812, 0.00051889, 68.15817813, 0.01180608, 6.81581781, 0.04031476, -56.31036812, -0.00051889, -68.15817813, -0.01180608, -6.81581781, -0.04031476, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 66.67937393, 0.0004938, 80.70884275, 0.01231652, 8.07088428, 0.04413881, -66.67937393, -0.0004938, -80.70884275, -0.01231652, -8.07088428, -0.04413881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 101.4533692, 0.01037781, 101.4533692, 0.03113343, 71.01735844, -1548.10077284, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 25.3633423, 3.869e-05, 76.0900269, 0.00011608, 253.633423, 0.00038694, -25.3633423, -3.869e-05, -76.0900269, -0.00011608, -253.633423, -0.00038694, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 122.59246935, 0.00987595, 122.59246935, 0.02962786, 85.81472855, -1704.59259838, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 30.64811734, 4.676e-05, 91.94435202, 0.00014027, 306.48117339, 0.00046756, -30.64811734, -4.676e-05, -91.94435202, -0.00014027, -306.48117339, -0.00046756, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.45, 0.0, 6.075)
    ops.node(124030, 13.45, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.105, 29633603.57960831, 12347334.82483679, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 59.58618063, 0.00050503, 71.74402583, 0.01225428, 7.17440258, 0.04397048, -59.58618063, -0.00050503, -71.74402583, -0.01225428, -7.17440258, -0.04397048, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 70.43203584, 0.00048155, 84.80284766, 0.01278825, 8.48028477, 0.04819089, -70.43203584, -0.00048155, -84.80284766, -0.01278825, -8.48028477, -0.04819089, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 122.1665967, 0.01010063, 122.1665967, 0.03030188, 85.51661769, -1701.54555014, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 30.54164917, 4.099e-05, 91.62494752, 0.00012297, 305.41649174, 0.0004099, -30.54164917, -4.099e-05, -91.62494752, -0.00012297, -305.41649174, -0.0004099, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 145.63610401, 0.00963106, 145.63610401, 0.02889318, 101.94527281, -1858.24506519, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 36.409026, 4.886e-05, 109.22707801, 0.00014659, 364.09026004, 0.00048865, -36.409026, -4.886e-05, -109.22707801, -0.00014659, -364.09026004, -0.00048865, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 13.45, 0.0, 7.45)
    ops.node(123004, 13.45, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.105, 28899976.44893827, 12041656.85372428, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 54.89055123, 0.00050247, 66.28855728, 0.01428868, 6.62885573, 0.04692035, -54.89055123, -0.00050247, -66.28855728, -0.01428868, -6.62885573, -0.04692035, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 64.96950214, 0.00047929, 78.46039924, 0.0149196, 7.84603992, 0.05134411, -64.96950214, -0.00047929, -78.46039924, -0.0149196, -7.84603992, -0.05134411, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 121.6294687, 0.01004944, 121.6294687, 0.03014833, 85.14062809, -1780.9414621, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 30.40736717, 4.185e-05, 91.22210152, 0.00012554, 304.07367174, 0.00041846, -30.40736717, -4.185e-05, -91.22210152, -0.00012554, -304.07367174, -0.00041846, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 141.90104681, 0.00958577, 141.90104681, 0.0287573, 99.33073277, -1990.75559316, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 35.4752617, 4.882e-05, 106.42578511, 0.00014646, 354.75261703, 0.0004882, -35.4752617, -4.882e-05, -106.42578511, -0.00014646, -354.75261703, -0.0004882, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 10.6, 0.0, 8.975)
    ops.node(124031, 10.6, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.105, 25827459.38603004, 10761441.41084585, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 41.70219642, 0.00047324, 50.91751792, 0.01488618, 5.09175179, 0.05128009, -41.70219642, -0.00047324, -50.91751792, -0.01488618, -5.09175179, -0.05128009, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 49.42376979, 0.00045622, 60.34539904, 0.01555301, 6.0345399, 0.05617704, -49.42376979, -0.00045622, -60.34539904, -0.01555301, -6.0345399, -0.05617704, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 94.66726769, 0.00946472, 94.66726769, 0.02839417, 66.26708738, -1528.17470463, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 23.66681692, 3.644e-05, 71.00045077, 0.00010933, 236.66816923, 0.00036444, -23.66681692, -3.644e-05, -71.00045077, -0.00010933, -236.66816923, -0.00036444, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 110.44514564, 0.00912442, 110.44514564, 0.02737326, 77.31160195, -1804.25037777, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 27.61128641, 4.252e-05, 82.83385923, 0.00012755, 276.1128641, 0.00042518, -27.61128641, -4.252e-05, -82.83385923, -0.00012755, -276.1128641, -0.00042518, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 10.6, 0.0, 10.35)
    ops.node(124003, 10.6, 0.0, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.105, 29523567.54510473, 12301486.47712697, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 36.73048166, 0.00046637, 44.64488232, 0.01467667, 4.46448823, 0.05632355, -36.73048166, -0.00046637, -44.64488232, -0.01467667, -4.46448823, -0.05632355, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 43.63864202, 0.00044986, 53.04155975, 0.01533439, 5.30415597, 0.06182196, -43.63864202, -0.00044986, -53.04155975, -0.01533439, -5.30415597, -0.06182196, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 101.97197844, 0.00932747, 101.97197844, 0.02798241, 71.38038491, -1468.24457894, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 25.49299461, 3.434e-05, 76.47898383, 0.00010303, 254.9299461, 0.00034342, -25.49299461, -3.434e-05, -76.47898383, -0.00010303, -254.9299461, -0.00034342, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 118.96730818, 0.00899725, 118.96730818, 0.02699176, 83.27711573, -1786.43494484, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 29.74182705, 4.007e-05, 89.22548114, 0.0001202, 297.41827045, 0.00040065, -29.74182705, -4.007e-05, -89.22548114, -0.0001202, -297.41827045, -0.00040065, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.45, 0.0, 8.975)
    ops.node(124032, 13.45, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.105, 28736000.2699788, 11973333.4458245, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 40.14493202, 0.00048183, 48.78805909, 0.01528841, 4.87880591, 0.05416393, -40.14493202, -0.00048183, -48.78805909, -0.01528841, -4.87880591, -0.05416393, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 47.74249562, 0.00046155, 58.02136361, 0.01597065, 5.80213636, 0.05936473, -47.74249562, -0.00046155, -58.02136361, -0.01597065, -5.80213636, -0.05936473, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 105.79064017, 0.00963667, 105.79064017, 0.02891, 74.05344812, -1510.01282822, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 26.44766004, 3.66e-05, 79.34298013, 0.00010981, 264.47660042, 0.00036604, -26.44766004, -3.66e-05, -79.34298013, -0.00010981, -264.47660042, -0.00036604, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 123.42241353, 0.00923106, 123.42241353, 0.02769318, 86.39568947, -1781.2320527, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 30.85560338, 4.271e-05, 92.56681015, 0.00012812, 308.55603382, 0.00042705, -30.85560338, -4.271e-05, -92.56681015, -0.00012812, -308.55603382, -0.00042705, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 13.45, 0.0, 10.35)
    ops.node(124004, 13.45, 0.0, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.105, 29023520.9762869, 12093133.74011954, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 36.02698484, 0.00046137, 43.8434065, 0.01480272, 4.38434065, 0.05624136, -36.02698484, -0.00046137, -43.8434065, -0.01480272, -4.38434065, -0.05624136, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 42.8008201, 0.00044551, 52.08689438, 0.0154673, 5.20868944, 0.06172243, -42.8008201, -0.00044551, -52.08689438, -0.0154673, -5.20868944, -0.06172243, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 100.56120306, 0.00922738, 100.56120306, 0.02768214, 70.39284214, -1520.66044354, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 25.14030076, 3.445e-05, 75.42090229, 0.00010335, 251.40300765, 0.0003445, -25.14030076, -3.445e-05, -75.42090229, -0.00010335, -251.40300765, -0.0003445, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 117.32140357, 0.0089102, 117.32140357, 0.02673059, 82.1249825, -1853.92247529, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 29.33035089, 4.019e-05, 87.99105268, 0.00012058, 293.30350892, 0.00040192, -29.33035089, -4.019e-05, -87.99105268, -0.00012058, -293.30350892, -0.00040192, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
