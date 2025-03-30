import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 27822730.79933828, 11592804.49972428, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 51.19416124, 0.00101435, 60.54247698, 0.01511757, 6.0542477, 0.03884588, -51.19416124, -0.00101435, -60.54247698, -0.01511757, -6.0542477, -0.03884588, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 53.85902744, 0.00101435, 63.69396138, 0.01511757, 6.36939614, 0.03884588, -53.85902744, -0.00101435, -63.69396138, -0.01511757, -6.36939614, -0.03884588, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 81.57022795, 0.02028703, 81.57022795, 0.0608611, 57.09915956, -1020.59616383, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 20.39255699, 0.0001047, 61.17767096, 0.0003141, 203.92556987, 0.001047, -20.39255699, -0.0001047, -61.17767096, -0.0003141, -203.92556987, -0.001047, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 81.57022795, 0.02028703, 81.57022795, 0.0608611, 57.09915956, -1020.59616383, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 20.39255699, 0.0001047, 61.17767096, 0.0003141, 203.92556987, 0.001047, -20.39255699, -0.0001047, -61.17767096, -0.0003141, -203.92556987, -0.001047, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.25, 0.0, 0.0)
    ops.node(121002, 4.25, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.09, 29604556.89257659, 12335232.03857358, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 98.3239392, 0.00087778, 116.29390773, 0.01559128, 11.62939077, 0.03634822, -98.3239392, -0.00087778, -116.29390773, -0.01559128, -11.62939077, -0.03634822, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 104.61806687, 0.00087778, 123.73836845, 0.01559128, 12.37383685, 0.03634822, -104.61806687, -0.00087778, -123.73836845, -0.01559128, -12.37383685, -0.03634822, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 114.94714665, 0.01755568, 114.94714665, 0.05266703, 80.46300266, -1327.98808853, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 28.73678666, 9.629e-05, 86.21035999, 0.00028888, 287.36786664, 0.00096292, -28.73678666, -9.629e-05, -86.21035999, -0.00028888, -287.36786664, -0.00096292, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 114.94714665, 0.01755568, 114.94714665, 0.05266703, 80.46300266, -1327.98808853, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 28.73678666, 9.629e-05, 86.21035999, 0.00028888, 287.36786664, 0.00096292, -28.73678666, -9.629e-05, -86.21035999, -0.00028888, -287.36786664, -0.00096292, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 15.6, 0.0, 0.0)
    ops.node(121005, 15.6, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.09, 29350185.11536952, 12229243.79807063, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 99.02816601, 0.00086633, 117.10884059, 0.01546436, 11.71088406, 0.03568803, -99.02816601, -0.00086633, -117.10884059, -0.01546436, -11.71088406, -0.03568803, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 105.74604851, 0.00086633, 125.05328167, 0.01546436, 12.50532817, 0.03568803, -105.74604851, -0.00086633, -125.05328167, -0.01546436, -12.50532817, -0.03568803, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 113.8434957, 0.01732657, 113.8434957, 0.05197972, 79.69044699, -1322.70036055, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 28.46087393, 9.619e-05, 85.38262178, 0.00028858, 284.60873926, 0.00096194, -28.46087393, -9.619e-05, -85.38262178, -0.00028858, -284.60873926, -0.00096194, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 113.8434957, 0.01732657, 113.8434957, 0.05197972, 79.69044699, -1322.70036055, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 28.46087393, 9.619e-05, 85.38262178, 0.00028858, 284.60873926, 0.00096194, -28.46087393, -9.619e-05, -85.38262178, -0.00028858, -284.60873926, -0.00096194, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 19.85, 0.0, 0.0)
    ops.node(121006, 19.85, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.0625, 29316645.48374938, 12215268.95156224, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 52.38881313, 0.00096524, 62.05682402, 0.01605634, 6.2056824, 0.04406765, -52.38881313, -0.00096524, -62.05682402, -0.01605634, -6.2056824, -0.04406765, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 55.45276507, 0.00096524, 65.68620814, 0.01605634, 6.56862081, 0.04406765, -55.45276507, -0.00096524, -65.68620814, -0.01605634, -6.56862081, -0.04406765, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 85.34792827, 0.01930483, 85.34792827, 0.05791449, 59.74354979, -1031.11048983, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 21.33698207, 0.00010397, 64.0109462, 0.0003119, 213.36982067, 0.00103966, -21.33698207, -0.00010397, -64.0109462, -0.0003119, -213.36982067, -0.00103966, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 85.34792827, 0.01930483, 85.34792827, 0.05791449, 59.74354979, -1031.11048983, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 21.33698207, 0.00010397, 64.0109462, 0.0003119, 213.36982067, 0.00103966, -21.33698207, -0.00010397, -64.0109462, -0.0003119, -213.36982067, -0.00103966, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 5.5, 0.0)
    ops.node(121007, 0.0, 5.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 29108038.54940441, 12128349.39558517, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 147.14883175, 0.0007453, 175.06157737, 0.01573937, 17.50615774, 0.03993437, -147.14883175, -0.0007453, -175.06157737, -0.01573937, -17.50615774, -0.03993437, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 151.56002278, 0.0007453, 180.30952973, 0.01573937, 18.03095297, 0.03993437, -151.56002278, -0.0007453, -180.30952973, -0.01573937, -18.03095297, -0.03993437, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 145.76335865, 0.01490607, 145.76335865, 0.04471821, 102.03435106, -1587.66572789, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 36.44083966, 9.124e-05, 109.32251899, 0.00027373, 364.40839663, 0.00091242, -36.44083966, -9.124e-05, -109.32251899, -0.00027373, -364.40839663, -0.00091242, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 145.76335865, 0.01490607, 145.76335865, 0.04471821, 102.03435106, -1587.66572789, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 36.44083966, 9.124e-05, 109.32251899, 0.00027373, 364.40839663, 0.00091242, -36.44083966, -9.124e-05, -109.32251899, -0.00027373, -364.40839663, -0.00091242, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.25, 5.5, 0.0)
    ops.node(121008, 4.25, 5.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.2025, 28772788.93017679, 11988662.05424033, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 314.30314711, 0.00063674, 376.24039237, 0.02143268, 37.62403924, 0.04512317, -314.30314711, -0.00063674, -376.24039237, -0.02143268, -37.62403924, -0.04512317, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 325.27880738, 0.00063674, 389.37893954, 0.02143268, 38.93789395, 0.04512317, -325.27880738, -0.00063674, -389.37893954, -0.02143268, -38.93789395, -0.04512317, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 209.5082483, 0.01273476, 209.5082483, 0.03820429, 146.65577381, -2004.42410368, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 52.37706207, 8.026e-05, 157.13118622, 0.00024077, 523.77062075, 0.00080258, -52.37706207, -8.026e-05, -157.13118622, -0.00024077, -523.77062075, -0.00080258, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 209.5082483, 0.01273476, 209.5082483, 0.03820429, 146.65577381, -2004.42410368, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 52.37706207, 8.026e-05, 157.13118622, 0.00024077, 523.77062075, 0.00080258, -52.37706207, -8.026e-05, -157.13118622, -0.00024077, -523.77062075, -0.00080258, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 8.5, 5.5, 0.0)
    ops.node(121009, 8.5, 5.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 29763744.8946366, 12401560.37276525, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 232.41131565, 0.00067803, 277.04632955, 0.01628937, 27.70463295, 0.03802027, -232.41131565, -0.00067803, -277.04632955, -0.01628937, -27.70463295, -0.03802027, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 232.41131565, 0.00067803, 277.04632955, 0.01628937, 27.70463295, 0.03802027, -232.41131565, -0.00067803, -277.04632955, -0.01628937, -27.70463295, -0.03802027, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 177.31427873, 0.01356067, 177.31427873, 0.04068201, 124.11999511, -1740.92817558, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 44.32856968, 8.311e-05, 132.98570905, 0.00024932, 443.28569683, 0.00083106, -44.32856968, -8.311e-05, -132.98570905, -0.00024932, -443.28569683, -0.00083106, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 177.31427873, 0.01356067, 177.31427873, 0.04068201, 124.11999511, -1740.92817558, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 44.32856968, 8.311e-05, 132.98570905, 0.00024932, 443.28569683, 0.00083106, -44.32856968, -8.311e-05, -132.98570905, -0.00024932, -443.28569683, -0.00083106, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 11.35, 5.5, 0.0)
    ops.node(121010, 11.35, 5.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 29032683.72199382, 12096951.55083076, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 227.35851051, 0.00070003, 271.07316364, 0.0162591, 27.10731636, 0.03681168, -227.35851051, -0.00070003, -271.07316364, -0.0162591, -27.10731636, -0.03681168, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 227.35851051, 0.00070003, 271.07316364, 0.0162591, 27.10731636, 0.03681168, -227.35851051, -0.00070003, -271.07316364, -0.0162591, -27.10731636, -0.03681168, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 173.9137974, 0.0140007, 173.9137974, 0.0420021, 121.73965818, -1750.4229459, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 43.47844935, 8.356e-05, 130.43534805, 0.00025069, 434.7844935, 0.00083564, -43.47844935, -8.356e-05, -130.43534805, -0.00025069, -434.7844935, -0.00083564, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 173.9137974, 0.0140007, 173.9137974, 0.0420021, 121.73965818, -1750.4229459, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 43.47844935, 8.356e-05, 130.43534805, 0.00025069, 434.7844935, 0.00083564, -43.47844935, -8.356e-05, -130.43534805, -0.00025069, -434.7844935, -0.00083564, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 15.6, 5.5, 0.0)
    ops.node(121011, 15.6, 5.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 28948284.03663175, 12061785.01526323, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 306.70058873, 0.00064557, 367.11502471, 0.02163011, 36.71150247, 0.04560858, -306.70058873, -0.00064557, -367.11502471, -0.02163011, -36.71150247, -0.04560858, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 316.74458018, 0.00064557, 379.13749973, 0.02163011, 37.91374997, 0.04560858, -316.74458018, -0.00064557, -379.13749973, -0.02163011, -37.91374997, -0.04560858, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 210.85936683, 0.01291143, 210.85936683, 0.03873429, 147.60155678, -2008.27152037, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 52.71484171, 8.029e-05, 158.14452513, 0.00024086, 527.14841709, 0.00080286, -52.71484171, -8.029e-05, -158.14452513, -0.00024086, -527.14841709, -0.00080286, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 210.85936683, 0.01291143, 210.85936683, 0.03873429, 147.60155678, -2008.27152037, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 52.71484171, 8.029e-05, 158.14452513, 0.00024086, 527.14841709, 0.00080286, -52.71484171, -8.029e-05, -158.14452513, -0.00024086, -527.14841709, -0.00080286, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 19.85, 5.5, 0.0)
    ops.node(121012, 19.85, 5.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 29768114.55131588, 12403381.06304828, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 146.29461567, 0.00074289, 174.04065912, 0.01603735, 17.40406591, 0.04159215, -146.29461567, -0.00074289, -174.04065912, -0.01603735, -17.40406591, -0.04159215, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 150.5328286, 0.00074289, 179.08268591, 0.01603735, 17.90826859, 0.04159215, -150.5328286, -0.00074289, -179.08268591, -0.01603735, -17.90826859, -0.04159215, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 147.95871605, 0.01485779, 147.95871605, 0.04457337, 103.57110124, -1577.06310855, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 36.98967901, 9.056e-05, 110.96903704, 0.00027169, 369.89679013, 0.00090562, -36.98967901, -9.056e-05, -110.96903704, -0.00027169, -369.89679013, -0.00090562, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 147.95871605, 0.01485779, 147.95871605, 0.04457337, 103.57110124, -1577.06310855, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 36.98967901, 9.056e-05, 110.96903704, 0.00027169, 369.89679013, 0.00090562, -36.98967901, -9.056e-05, -110.96903704, -0.00027169, -369.89679013, -0.00090562, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 11.0, 0.0)
    ops.node(121013, 0.0, 11.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0625, 29558680.10729924, 12316116.71137469, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 51.21740817, 0.00097548, 60.67578372, 0.01643796, 6.06757837, 0.04511688, -51.21740817, -0.00097548, -60.67578372, -0.01643796, -6.06757837, -0.04511688, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 53.84205323, 0.00097548, 63.7851249, 0.01643796, 6.37851249, 0.04511688, -53.84205323, -0.00097548, -63.7851249, -0.01643796, -6.37851249, -0.04511688, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 85.93353976, 0.01950965, 85.93353976, 0.05852895, 60.15347783, -1032.19289544, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 21.48338494, 0.00010382, 64.45015482, 0.00031147, 214.83384941, 0.00103823, -21.48338494, -0.00010382, -64.45015482, -0.00031147, -214.83384941, -0.00103823, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 85.93353976, 0.01950965, 85.93353976, 0.05852895, 60.15347783, -1032.19289544, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 21.48338494, 0.00010382, 64.45015482, 0.00031147, 214.83384941, 0.00103823, -21.48338494, -0.00010382, -64.45015482, -0.00031147, -214.83384941, -0.00103823, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.25, 11.0, 0.0)
    ops.node(121014, 4.25, 11.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.09, 28532222.42798179, 11888426.01165908, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 99.05187977, 0.00088744, 117.04021746, 0.01446549, 11.70402175, 0.0329359, -99.05187977, -0.00088744, -117.04021746, -0.01446549, -11.70402175, -0.0329359, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 106.39268286, 0.00088744, 125.71414865, 0.01446549, 12.57141487, 0.0329359, -106.39268286, -0.00088744, -125.71414865, -0.01446549, -12.57141487, -0.0329359, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 111.38646124, 0.01774879, 111.38646124, 0.05324636, 77.97052287, -1325.30266938, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 27.84661531, 9.682e-05, 83.53984593, 0.00029045, 278.46615311, 0.00096816, -27.84661531, -9.682e-05, -83.53984593, -0.00029045, -278.46615311, -0.00096816, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 111.38646124, 0.01774879, 111.38646124, 0.05324636, 77.97052287, -1325.30266938, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 27.84661531, 9.682e-05, 83.53984593, 0.00029045, 278.46615311, 0.00096816, -27.84661531, -9.682e-05, -83.53984593, -0.00029045, -278.46615311, -0.00096816, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 8.5, 11.0, 0.0)
    ops.node(121015, 8.5, 11.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.09, 29524053.25041422, 12301688.85433926, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 86.77660942, 0.00084699, 103.13232649, 0.01568845, 10.31323265, 0.03949129, -86.77660942, -0.00084699, -103.13232649, -0.01568845, -10.31323265, -0.03949129, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 90.2501412, 0.00084699, 107.26055201, 0.01568845, 10.7260552, 0.03949129, -90.2501412, -0.00084699, -107.26055201, -0.01568845, -10.7260552, -0.03949129, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 108.15393996, 0.01693973, 108.15393996, 0.0508192, 75.70775797, -1168.92251992, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 27.03848499, 9.085e-05, 81.11545497, 0.00027255, 270.38484989, 0.00090849, -27.03848499, -9.085e-05, -81.11545497, -0.00027255, -270.38484989, -0.00090849, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 108.15393996, 0.01693973, 108.15393996, 0.0508192, 75.70775797, -1168.92251992, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 27.03848499, 9.085e-05, 81.11545497, 0.00027255, 270.38484989, 0.00090849, -27.03848499, -9.085e-05, -81.11545497, -0.00027255, -270.38484989, -0.00090849, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 11.35, 11.0, 0.0)
    ops.node(121016, 11.35, 11.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.09, 28709464.04057002, 11962276.68357084, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 87.01987539, 0.00085698, 103.3969621, 0.01538217, 10.33969621, 0.03749177, -87.01987539, -0.00085698, -103.3969621, -0.01538217, -10.33969621, -0.03749177, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 90.58982503, 0.00085698, 107.63877405, 0.01538217, 10.76387741, 0.03749177, -90.58982503, -0.00085698, -107.63877405, -0.01538217, -10.76387741, -0.03749177, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 106.05557376, 0.0171396, 106.05557376, 0.05141879, 74.23890163, -1176.52870774, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 26.51389344, 9.161e-05, 79.54168032, 0.00027484, 265.13893439, 0.00091614, -26.51389344, -9.161e-05, -79.54168032, -0.00027484, -265.13893439, -0.00091614, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 106.05557376, 0.0171396, 106.05557376, 0.05141879, 74.23890163, -1176.52870774, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 26.51389344, 9.161e-05, 79.54168032, 0.00027484, 265.13893439, 0.00091614, -26.51389344, -9.161e-05, -79.54168032, -0.00027484, -265.13893439, -0.00091614, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 15.6, 11.0, 0.0)
    ops.node(121017, 15.6, 11.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.09, 30201579.21782729, 12583991.34076137, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 99.17570958, 0.00090032, 117.32250912, 0.01533255, 11.73225091, 0.03731631, -99.17570958, -0.00090032, -117.32250912, -0.01533255, -11.73225091, -0.03731631, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 105.82786556, 0.00090032, 125.19185166, 0.01533255, 12.51918517, 0.03731631, -105.82786556, -0.00090032, -125.19185166, -0.01533255, -12.51918517, -0.03731631, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 116.39643132, 0.01800637, 116.39643132, 0.05401911, 81.47750192, -1319.46672253, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 29.09910783, 9.558e-05, 87.29732349, 0.00028674, 290.9910783, 0.00095579, -29.09910783, -9.558e-05, -87.29732349, -0.00028674, -290.9910783, -0.00095579, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 116.39643132, 0.01800637, 116.39643132, 0.05401911, 81.47750192, -1319.46672253, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 29.09910783, 9.558e-05, 87.29732349, 0.00028674, 290.9910783, 0.00095579, -29.09910783, -9.558e-05, -87.29732349, -0.00028674, -290.9910783, -0.00095579, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 19.85, 11.0, 0.0)
    ops.node(121018, 19.85, 11.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.0625, 30441083.63528915, 12683784.84803715, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 51.96201403, 0.00100238, 61.5613268, 0.0167335, 6.15613268, 0.04777535, -51.96201403, -0.00100238, -61.5613268, -0.0167335, -6.15613268, -0.04777535, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 54.53466172, 0.00100238, 64.60923801, 0.0167335, 6.4609238, 0.04777535, -54.53466172, -0.00100238, -64.60923801, -0.0167335, -6.4609238, -0.04777535, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 88.02754442, 0.02004764, 88.02754442, 0.06014292, 61.61928109, -1035.0842524, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 22.0068861, 0.00010327, 66.02065831, 0.00030981, 220.06886104, 0.0010327, -22.0068861, -0.00010327, -66.02065831, -0.00030981, -220.06886104, -0.0010327, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 88.02754442, 0.02004764, 88.02754442, 0.06014292, 61.61928109, -1035.0842524, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 22.0068861, 0.00010327, 66.02065831, 0.00030981, 220.06886104, 0.0010327, -22.0068861, -0.00010327, -66.02065831, -0.00030981, -220.06886104, -0.0010327, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.375)
    ops.node(122001, 0.0, 0.0, 5.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 29481137.17334965, 12283807.15556235, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 42.58320171, 0.00098707, 50.83959403, 0.01811863, 5.0839594, 0.054015, -42.58320171, -0.00098707, -50.83959403, -0.01811863, -5.0839594, -0.054015, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 44.77516081, 0.00098707, 53.45654875, 0.01811863, 5.34565487, 0.054015, -44.77516081, -0.00098707, -53.45654875, -0.01811863, -5.34565487, -0.054015, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 79.66737247, 0.01974137, 79.66737247, 0.05922411, 55.76716073, -896.41738738, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 19.91684312, 9.651e-05, 59.75052936, 0.00028952, 199.16843119, 0.00096505, -19.91684312, -9.651e-05, -59.75052936, -0.00028952, -199.16843119, -0.00096505, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 79.66737247, 0.01974137, 79.66737247, 0.05922411, 55.76716073, -896.41738738, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 19.91684312, 9.651e-05, 59.75052936, 0.00028952, 199.16843119, 0.00096505, -19.91684312, -9.651e-05, -59.75052936, -0.00028952, -199.16843119, -0.00096505, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.25, 0.0, 3.3)
    ops.node(122002, 4.25, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.09, 30412020.66071639, 12671675.27529849, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 84.24987373, 0.00082876, 100.38245391, 0.01769407, 10.03824539, 0.0454339, -84.24987373, -0.00082876, -100.38245391, -0.01769407, -10.03824539, -0.0454339, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 90.41575463, 0.00082876, 107.72900801, 0.01769407, 10.7729008, 0.0454339, -90.41575463, -0.00082876, -107.72900801, -0.01769407, -10.7729008, -0.0454339, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 108.61974922, 0.01657519, 108.61974922, 0.04972557, 76.03382445, -1109.52892413, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 27.1549373, 8.858e-05, 81.46481191, 0.00026573, 271.54937304, 0.00088576, -27.1549373, -8.858e-05, -81.46481191, -0.00026573, -271.54937304, -0.00088576, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 108.61974922, 0.01657519, 108.61974922, 0.04972557, 76.03382445, -1109.52892413, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 27.1549373, 8.858e-05, 81.46481191, 0.00026573, 271.54937304, 0.00088576, -27.1549373, -8.858e-05, -81.46481191, -0.00026573, -271.54937304, -0.00088576, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 15.6, 0.0, 3.3)
    ops.node(122005, 15.6, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.09, 28274496.97854435, 11781040.40772681, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 83.08956146, 0.00085145, 99.04288492, 0.01702514, 9.90428849, 0.04053388, -83.08956146, -0.00085145, -99.04288492, -0.01702514, -9.90428849, -0.04053388, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 89.15915445, 0.00085145, 106.27784909, 0.01702514, 10.62778491, 0.04053388, -89.15915445, -0.00085145, -106.27784909, -0.01702514, -10.62778491, -0.04053388, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 102.30312786, 0.01702902, 102.30312786, 0.05108706, 71.6121895, -1112.03641796, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 25.57578196, 8.973e-05, 76.72734589, 0.00026919, 255.75781964, 0.00089732, -25.57578196, -8.973e-05, -76.72734589, -0.00026919, -255.75781964, -0.00089732, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 102.30312786, 0.01702902, 102.30312786, 0.05108706, 71.6121895, -1112.03641796, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 25.57578196, 8.973e-05, 76.72734589, 0.00026919, 255.75781964, 0.00089732, -25.57578196, -8.973e-05, -76.72734589, -0.00026919, -255.75781964, -0.00089732, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 19.85, 0.0, 3.375)
    ops.node(122006, 19.85, 0.0, 5.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.0625, 29505554.99546578, 12293981.24811074, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 42.47046446, 0.00093318, 50.70441386, 0.0184574, 5.07044139, 0.05441547, -42.47046446, -0.00093318, -50.70441386, -0.0184574, -5.07044139, -0.05441547, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 44.90466297, 0.00093318, 53.61054193, 0.0184574, 5.36105419, 0.05441547, -44.90466297, -0.00093318, -53.61054193, -0.0184574, -5.36105419, -0.05441547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 79.97091649, 0.01866358, 79.97091649, 0.05599074, 55.97964154, -901.8995381, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 19.99272912, 9.679e-05, 59.97818737, 0.00029038, 199.92729123, 0.00096793, -19.99272912, -9.679e-05, -59.97818737, -0.00029038, -199.92729123, -0.00096793, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 79.97091649, 0.01866358, 79.97091649, 0.05599074, 55.97964154, -901.8995381, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 19.99272912, 9.679e-05, 59.97818737, 0.00029038, 199.92729123, 0.00096793, -19.99272912, -9.679e-05, -59.97818737, -0.00029038, -199.92729123, -0.00096793, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 5.5, 3.375)
    ops.node(122007, 0.0, 5.5, 5.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 28186091.72620538, 11744204.88591891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 93.45791809, 0.00069309, 111.97702625, 0.01618377, 11.19770263, 0.04397575, -93.45791809, -0.00069309, -111.97702625, -0.01618377, -11.19770263, -0.04397575, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 101.78887953, 0.00069309, 121.95880529, 0.01618377, 12.19588053, 0.04397575, -101.78887953, -0.00069309, -121.95880529, -0.01618377, -12.19588053, -0.04397575, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 132.03105524, 0.0138619, 132.03105524, 0.0415857, 92.42173867, -1361.01154207, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 33.00776381, 8.535e-05, 99.02329143, 0.00025605, 330.07763809, 0.00085349, -33.00776381, -8.535e-05, -99.02329143, -0.00025605, -330.07763809, -0.00085349, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 132.03105524, 0.0138619, 132.03105524, 0.0415857, 92.42173867, -1361.01154207, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 33.00776381, 8.535e-05, 99.02329143, 0.00025605, 330.07763809, 0.00085349, -33.00776381, -8.535e-05, -99.02329143, -0.00025605, -330.07763809, -0.00085349, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.25, 5.5, 3.325)
    ops.node(122008, 4.25, 5.5, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.2025, 29334061.25741038, 12222525.52392099, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 198.24435669, 0.00059523, 238.35179146, 0.01470962, 23.83517915, 0.03576717, -198.24435669, -0.00059523, -238.35179146, -0.01470962, -23.83517915, -0.03576717, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 188.74764984, 0.00059523, 226.9337762, 0.01470962, 22.69337762, 0.03576717, -188.74764984, -0.00059523, -226.9337762, -0.01470962, -22.69337762, -0.03576717, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 184.29471234, 0.01190453, 184.29471234, 0.03571358, 129.00629864, -1427.49174635, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 46.07367809, 6.925e-05, 138.22103426, 0.00020775, 460.73678086, 0.00069248, -46.07367809, -6.925e-05, -138.22103426, -0.00020775, -460.73678086, -0.00069248, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 184.29471234, 0.01190453, 184.29471234, 0.03571358, 129.00629864, -1427.49174635, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 46.07367809, 6.925e-05, 138.22103426, 0.00020775, 460.73678086, 0.00069248, -46.07367809, -6.925e-05, -138.22103426, -0.00020775, -460.73678086, -0.00069248, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 8.5, 5.5, 3.325)
    ops.node(122009, 8.5, 5.5, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 28364455.65409087, 11818523.18920453, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 151.62152022, 0.00064667, 181.89936617, 0.01580201, 18.18993662, 0.03925602, -151.62152022, -0.00064667, -181.89936617, -0.01580201, -18.18993662, -0.03925602, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 141.61702004, 0.00064667, 169.89703143, 0.01580201, 16.98970314, 0.03925602, -141.61702004, -0.00064667, -169.89703143, -0.01580201, -16.98970314, -0.03925602, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 158.02040279, 0.0129334, 158.02040279, 0.03880019, 110.61428195, -1468.70783575, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 39.5051007, 7.772e-05, 118.51530209, 0.00023315, 395.05100698, 0.00077716, -39.5051007, -7.772e-05, -118.51530209, -0.00023315, -395.05100698, -0.00077716, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 158.02040279, 0.0129334, 158.02040279, 0.03880019, 110.61428195, -1468.70783575, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 39.5051007, 7.772e-05, 118.51530209, 0.00023315, 395.05100698, 0.00077716, -39.5051007, -7.772e-05, -118.51530209, -0.00023315, -395.05100698, -0.00077716, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 11.35, 5.5, 3.325)
    ops.node(122010, 11.35, 5.5, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 28502347.76707625, 11875978.23628177, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 151.24739118, 0.00064638, 181.44098584, 0.01601693, 18.14409858, 0.03968581, -151.24739118, -0.00064638, -181.44098584, -0.01601693, -18.14409858, -0.03968581, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 141.37005, 0.00064638, 169.59182594, 0.01601693, 16.95918259, 0.03968581, -141.37005, -0.00064638, -169.59182594, -0.01601693, -16.95918259, -0.03968581, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 158.97404203, 0.01292758, 158.97404203, 0.03878273, 111.28182942, -1473.64318773, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 39.74351051, 7.781e-05, 119.23053152, 0.00023342, 397.43510508, 0.00077807, -39.74351051, -7.781e-05, -119.23053152, -0.00023342, -397.43510508, -0.00077807, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 158.97404203, 0.01292758, 158.97404203, 0.03878273, 111.28182942, -1473.64318773, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 39.74351051, 7.781e-05, 119.23053152, 0.00023342, 397.43510508, 0.00077807, -39.74351051, -7.781e-05, -119.23053152, -0.00023342, -397.43510508, -0.00077807, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 15.6, 5.5, 3.325)
    ops.node(122011, 15.6, 5.5, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 29711434.97458602, 12379764.57274417, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 199.92206282, 0.00059017, 240.254753, 0.01463725, 24.0254753, 0.0360723, -199.92206282, -0.00059017, -240.254753, -0.01463725, -24.0254753, -0.0360723, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 190.12947702, 0.00059017, 228.48659069, 0.01463725, 22.84865907, 0.0360723, -190.12947702, -0.00059017, -228.48659069, -0.01463725, -22.84865907, -0.0360723, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 186.49883411, 0.01180331, 186.49883411, 0.03540993, 130.54918388, -1423.67020282, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 46.62470853, 6.919e-05, 139.87412558, 0.00020756, 466.24708527, 0.00069187, -46.62470853, -6.919e-05, -139.87412558, -0.00020756, -466.24708527, -0.00069187, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 186.49883411, 0.01180331, 186.49883411, 0.03540993, 130.54918388, -1423.67020282, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 46.62470853, 6.919e-05, 139.87412558, 0.00020756, 466.24708527, 0.00069187, -46.62470853, -6.919e-05, -139.87412558, -0.00020756, -466.24708527, -0.00069187, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 19.85, 5.5, 3.375)
    ops.node(122012, 19.85, 5.5, 5.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 28835944.71810736, 12014976.96587807, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 93.77149681, 0.00069601, 112.33283724, 0.01644319, 11.23328372, 0.04552624, -93.77149681, -0.00069601, -112.33283724, -0.01644319, -11.23328372, -0.04552624, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 101.92060831, 0.00069601, 122.09500216, 0.01644319, 12.20950022, 0.04552624, -101.92060831, -0.00069601, -122.09500216, -0.01644319, -12.20950022, -0.04552624, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 134.19201563, 0.01392015, 134.19201563, 0.04176045, 93.93441094, -1353.08127034, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 33.54800391, 8.479e-05, 100.64401172, 0.00025437, 335.48003908, 0.00084791, -33.54800391, -8.479e-05, -100.64401172, -0.00025437, -335.48003908, -0.00084791, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 134.19201563, 0.01392015, 134.19201563, 0.04176045, 93.93441094, -1353.08127034, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 33.54800391, 8.479e-05, 100.64401172, 0.00025437, 335.48003908, 0.00084791, -33.54800391, -8.479e-05, -100.64401172, -0.00025437, -335.48003908, -0.00084791, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 11.0, 3.375)
    ops.node(122013, 0.0, 11.0, 5.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0625, 28414397.05274494, 11839332.10531039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 42.8748576, 0.00094313, 51.1932716, 0.01800958, 5.11932716, 0.05104569, -42.8748576, -0.00094313, -51.1932716, -0.01800958, -5.11932716, -0.05104569, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 45.49285523, 0.00094313, 54.319203, 0.01800958, 5.4319203, 0.05104569, -45.49285523, -0.00094313, -54.319203, -0.01800958, -5.4319203, -0.05104569, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 77.8496007, 0.01886259, 77.8496007, 0.05658778, 54.49472049, -904.58229701, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 19.46240018, 9.784e-05, 58.38720053, 0.00029353, 194.62400175, 0.00097844, -19.46240018, -9.784e-05, -58.38720053, -0.00029353, -194.62400175, -0.00097844, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 77.8496007, 0.01886259, 77.8496007, 0.05658778, 54.49472049, -904.58229701, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 19.46240018, 9.784e-05, 58.38720053, 0.00029353, 194.62400175, 0.00097844, -19.46240018, -9.784e-05, -58.38720053, -0.00029353, -194.62400175, -0.00097844, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.25, 11.0, 3.3)
    ops.node(122014, 4.25, 11.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.09, 28819413.93867648, 12008089.1411152, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 87.67086022, 0.00084888, 104.51290391, 0.01682325, 10.45129039, 0.04141959, -87.67086022, -0.00084888, -104.51290391, -0.01682325, -10.45129039, -0.04141959, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 98.13205805, 0.00084888, 116.9837541, 0.01682325, 11.69837541, 0.04141959, -98.13205805, -0.00084888, -116.9837541, -0.01682325, -11.69837541, -0.04141959, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 103.43034554, 0.01697754, 103.43034554, 0.05093263, 72.40124188, -1102.67989704, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 25.85758639, 8.901e-05, 77.57275916, 0.00026702, 258.57586386, 0.00089005, -25.85758639, -8.901e-05, -77.57275916, -0.00026702, -258.57586386, -0.00089005, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 103.43034554, 0.01697754, 103.43034554, 0.05093263, 72.40124188, -1102.67989704, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 25.85758639, 8.901e-05, 77.57275916, 0.00026702, 258.57586386, 0.00089005, -25.85758639, -8.901e-05, -77.57275916, -0.00026702, -258.57586386, -0.00089005, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 8.5, 11.0, 3.275)
    ops.node(122015, 8.5, 11.0, 6.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.09, 29154531.46772906, 12147721.44488711, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 76.47482482, 0.00080739, 91.51154921, 0.0179332, 9.15115492, 0.04622359, -76.47482482, -0.00080739, -91.51154921, -0.0179332, -9.15115492, -0.04622359, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 83.0786578, 0.00080739, 99.41384892, 0.0179332, 9.94138489, 0.04622359, -83.0786578, -0.00080739, -99.41384892, -0.0179332, -9.94138489, -0.04622359, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 100.39184526, 0.01614777, 100.39184526, 0.04844331, 70.27429168, -1012.31900511, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 25.09796131, 8.54e-05, 75.29388394, 0.00025619, 250.97961314, 0.00085397, -25.09796131, -8.54e-05, -75.29388394, -0.00025619, -250.97961314, -0.00085397, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 100.39184526, 0.01614777, 100.39184526, 0.04844331, 70.27429168, -1012.31900511, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 25.09796131, 8.54e-05, 75.29388394, 0.00025619, 250.97961314, 0.00085397, -25.09796131, -8.54e-05, -75.29388394, -0.00025619, -250.97961314, -0.00085397, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 11.35, 11.0, 3.275)
    ops.node(122016, 11.35, 11.0, 6.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.09, 29422481.4410108, 12259367.26708784, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 77.59619774, 0.00080123, 92.83856381, 0.01778292, 9.28385638, 0.04657237, -77.59619774, -0.00080123, -92.83856381, -0.01778292, -9.28385638, -0.04657237, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 84.5816857, 0.00080123, 101.1962242, 0.01778292, 10.11962242, 0.04657237, -84.5816857, -0.00080123, -101.1962242, -0.01778292, -10.11962242, -0.04657237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 100.82892738, 0.01602465, 100.82892738, 0.04807394, 70.58024917, -1005.28251317, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 25.20723185, 8.499e-05, 75.62169554, 0.00025496, 252.07231846, 0.00084988, -25.20723185, -8.499e-05, -75.62169554, -0.00025496, -252.07231846, -0.00084988, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 100.82892738, 0.01602465, 100.82892738, 0.04807394, 70.58024917, -1005.28251317, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 25.20723185, 8.499e-05, 75.62169554, 0.00025496, 252.07231846, 0.00084988, -25.20723185, -8.499e-05, -75.62169554, -0.00025496, -252.07231846, -0.00084988, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 15.6, 11.0, 3.3)
    ops.node(122017, 15.6, 11.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.09, 28763916.87455272, 11984965.36439697, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 86.98781655, 0.00086636, 103.69785733, 0.01688842, 10.36978573, 0.04137054, -86.98781655, -0.00086636, -103.69785733, -0.01688842, -10.36978573, -0.04137054, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 96.8168752, 0.00086636, 115.41504212, 0.01688842, 11.54150421, 0.04137054, -96.8168752, -0.00086636, -115.41504212, -0.01688842, -11.54150421, -0.04137054, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 103.29135072, 0.01732727, 103.29135072, 0.05198181, 72.3039455, -1103.20531821, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 25.82283768, 8.906e-05, 77.46851304, 0.00026717, 258.22837679, 0.00089057, -25.82283768, -8.906e-05, -77.46851304, -0.00026717, -258.22837679, -0.00089057, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 103.29135072, 0.01732727, 103.29135072, 0.05198181, 72.3039455, -1103.20531821, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 25.82283768, 8.906e-05, 77.46851304, 0.00026717, 258.22837679, 0.00089057, -25.82283768, -8.906e-05, -77.46851304, -0.00026717, -258.22837679, -0.00089057, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 19.85, 11.0, 3.375)
    ops.node(122018, 19.85, 11.0, 5.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.0625, 29813771.69456388, 12422404.87273495, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 42.4428532, 0.00092897, 50.6603355, 0.01831011, 5.06603355, 0.05498806, -42.4428532, -0.00092897, -50.6603355, -0.01831011, -5.06603355, -0.05498806, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 44.84253012, 0.00092897, 53.52462074, 0.01831011, 5.35246207, 0.05498806, -44.84253012, -0.00092897, -53.52462074, -0.01831011, -5.35246207, -0.05498806, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 80.18830874, 0.01857947, 80.18830874, 0.05573842, 56.13181612, -892.64895662, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 20.04707719, 9.605e-05, 60.14123156, 0.00028816, 200.47077186, 0.00096052, -20.04707719, -9.605e-05, -60.14123156, -0.00028816, -200.47077186, -0.00096052, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 80.18830874, 0.01857947, 80.18830874, 0.05573842, 56.13181612, -892.64895662, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 20.04707719, 9.605e-05, 60.14123156, 0.00028816, 200.47077186, 0.00096052, -20.04707719, -9.605e-05, -60.14123156, -0.00028816, -200.47077186, -0.00096052, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.475)
    ops.node(123001, 0.0, 0.0, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 29456380.08809245, 12273491.70337186, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 33.40490685, 0.00085966, 40.19081908, 0.02052074, 4.01908191, 0.0656117, -33.40490685, -0.00085966, -40.19081908, -0.02052074, -4.01908191, -0.0656117, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 35.75636902, 0.00085966, 43.01996004, 0.02052074, 4.301996, 0.0656117, -35.75636902, -0.00085966, -43.01996004, -0.02052074, -4.301996, -0.0656117, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 73.23057295, 0.01719322, 73.23057295, 0.05157965, 51.26140106, -800.09705822, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 18.30764324, 8.878e-05, 54.92292971, 0.00026635, 183.07643237, 0.00088782, -18.30764324, -8.878e-05, -54.92292971, -0.00026635, -183.07643237, -0.00088782, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 73.23057295, 0.01719322, 73.23057295, 0.05157965, 51.26140106, -800.09705822, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 18.30764324, 8.878e-05, 54.92292971, 0.00026635, 183.07643237, 0.00088782, -18.30764324, -8.878e-05, -54.92292971, -0.00026635, -183.07643237, -0.00088782, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.25, 0.0, 6.4)
    ops.node(123002, 4.25, 0.0, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 29505534.20344594, 12293972.58476914, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 47.62097852, 0.00098886, 56.8483901, 0.01895704, 5.68483901, 0.05004898, -47.62097852, -0.00098886, -56.8483901, -0.01895704, -5.68483901, -0.05004898, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 47.62097852, 0.00098886, 56.8483901, 0.01895704, 5.68483901, 0.05004898, -47.62097852, -0.00098886, -56.8483901, -0.01895704, -5.68483901, -0.05004898, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 74.91590373, 0.01977723, 74.91590373, 0.05933169, 52.44113261, -813.85591292, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 18.72897593, 9.067e-05, 56.1869278, 0.00027202, 187.28975933, 0.00090674, -18.72897593, -9.067e-05, -56.1869278, -0.00027202, -187.28975933, -0.00090674, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 74.91590373, 0.01977723, 74.91590373, 0.05933169, 52.44113261, -813.85591292, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 18.72897593, 9.067e-05, 56.1869278, 0.00027202, 187.28975933, 0.00090674, -18.72897593, -9.067e-05, -56.1869278, -0.00027202, -187.28975933, -0.00090674, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 15.6, 0.0, 6.4)
    ops.node(123005, 15.6, 0.0, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 29240689.8067724, 12183620.75282183, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 47.761913, 0.00097229, 57.02256166, 0.01852534, 5.70225617, 0.04903074, -47.761913, -0.00097229, -57.02256166, -0.01852534, -5.70225617, -0.04903074, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 47.761913, 0.00097229, 57.02256166, 0.01852534, 5.70225617, 0.04903074, -47.761913, -0.00097229, -57.02256166, -0.01852534, -5.70225617, -0.04903074, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 72.08665915, 0.01944586, 72.08665915, 0.05833758, 50.4606614, -806.40026573, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 18.02166479, 8.804e-05, 54.06499436, 0.00026412, 180.21664787, 0.0008804, -18.02166479, -8.804e-05, -54.06499436, -0.00026412, -180.21664787, -0.0008804, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 72.08665915, 0.01944586, 72.08665915, 0.05833758, 50.4606614, -806.40026573, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 18.02166479, 8.804e-05, 54.06499436, 0.00026412, 180.21664787, 0.0008804, -18.02166479, -8.804e-05, -54.06499436, -0.00026412, -180.21664787, -0.0008804, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 19.85, 0.0, 6.475)
    ops.node(123006, 19.85, 0.0, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 30227655.90669308, 12594856.62778878, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 33.380036, 0.00091462, 40.11471265, 0.02028283, 4.01147126, 0.06686898, -33.380036, -0.00091462, -40.11471265, -0.02028283, -4.01147126, -0.06686898, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 35.38491734, 0.00091462, 42.52409409, 0.02028283, 4.25240941, 0.06686898, -35.38491734, -0.00091462, -42.52409409, -0.02028283, -4.25240941, -0.06686898, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 74.18749734, 0.01829232, 74.18749734, 0.05487696, 51.93124814, -785.69682849, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 18.54687433, 8.765e-05, 55.640623, 0.00026294, 185.46874335, 0.00087648, -18.54687433, -8.765e-05, -55.640623, -0.00026294, -185.46874335, -0.00087648, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 74.18749734, 0.01829232, 74.18749734, 0.05487696, 51.93124814, -785.69682849, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 18.54687433, 8.765e-05, 55.640623, 0.00026294, 185.46874335, 0.00087648, -18.54687433, -8.765e-05, -55.640623, -0.00026294, -185.46874335, -0.00087648, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 5.5, 6.475)
    ops.node(123007, 0.0, 5.5, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 29673107.50280973, 12363794.79283739, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 41.86525205, 0.00093541, 49.90016738, 0.01748976, 4.99001674, 0.05222795, -41.86525205, -0.00093541, -49.90016738, -0.01748976, -4.99001674, -0.05222795, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 41.86525205, 0.00093541, 49.90016738, 0.01748976, 4.99001674, 0.05222795, -41.86525205, -0.00093541, -49.90016738, -0.01748976, -4.99001674, -0.05222795, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 82.13922226, 0.0187082, 82.13922226, 0.05612461, 57.49745558, -939.15612504, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 20.53480557, 9.886e-05, 61.6044167, 0.00029657, 205.34805566, 0.00098856, -20.53480557, -9.886e-05, -61.6044167, -0.00029657, -205.34805566, -0.00098856, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 82.13922226, 0.0187082, 82.13922226, 0.05612461, 57.49745558, -939.15612504, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 20.53480557, 9.886e-05, 61.6044167, 0.00029657, 205.34805566, 0.00098856, -20.53480557, -9.886e-05, -61.6044167, -0.00029657, -205.34805566, -0.00098856, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.25, 5.5, 6.4)
    ops.node(123008, 4.25, 5.5, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 28635075.94096793, 11931281.64206997, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 107.86261025, 0.00071403, 129.53669183, 0.01501526, 12.95366918, 0.03737307, -107.86261025, -0.00071403, -129.53669183, -0.01501526, -12.95366918, -0.03737307, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 107.86261025, 0.00071403, 129.53669183, 0.01501526, 12.95366918, 0.03737307, -107.86261025, -0.00071403, -129.53669183, -0.01501526, -12.95366918, -0.03737307, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 116.21374087, 0.0142805, 116.21374087, 0.0428415, 81.34961861, -1009.17848783, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 29.05343522, 7.395e-05, 87.16030565, 0.00022184, 290.53435217, 0.00073946, -29.05343522, -7.395e-05, -87.16030565, -0.00022184, -290.53435217, -0.00073946, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 116.21374087, 0.0142805, 116.21374087, 0.0428415, 81.34961861, -1009.17848783, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 29.05343522, 7.395e-05, 87.16030565, 0.00022184, 290.53435217, 0.00073946, -29.05343522, -7.395e-05, -87.16030565, -0.00022184, -290.53435217, -0.00073946, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 8.5, 5.5, 6.4)
    ops.node(123009, 8.5, 5.5, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 29963530.92484351, 12484804.55201813, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 96.58502341, 0.00068149, 115.95891076, 0.01737207, 11.59589108, 0.04733144, -96.58502341, -0.00068149, -115.95891076, -0.01737207, -11.59589108, -0.04733144, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 92.54928483, 0.00068149, 111.11364766, 0.01737207, 11.11136477, 0.04733144, -92.54928483, -0.00068149, -111.11364766, -0.01737207, -11.11136477, -0.04733144, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 127.67053292, 0.01362981, 127.67053292, 0.04088944, 89.36937305, -1133.50998906, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 31.91763323, 7.763e-05, 95.75289969, 0.0002329, 319.17633231, 0.00077635, -31.91763323, -7.763e-05, -95.75289969, -0.0002329, -319.17633231, -0.00077635, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 127.67053292, 0.01362981, 127.67053292, 0.04088944, 89.36937305, -1133.50998906, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 31.91763323, 7.763e-05, 95.75289969, 0.0002329, 319.17633231, 0.00077635, -31.91763323, -7.763e-05, -95.75289969, -0.0002329, -319.17633231, -0.00077635, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 11.35, 5.5, 6.4)
    ops.node(123010, 11.35, 5.5, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 31136101.84242232, 12973375.76767597, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 95.41017274, 0.00068113, 114.32714288, 0.01754943, 11.43271429, 0.04903972, -95.41017274, -0.00068113, -114.32714288, -0.01754943, -11.43271429, -0.04903972, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 91.67050585, 0.00068113, 109.84601242, 0.01754943, 10.98460124, 0.04903972, -91.67050585, -0.00068113, -109.84601242, -0.01754943, -10.98460124, -0.04903972, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 132.0099123, 0.01362266, 132.0099123, 0.04086797, 92.40693861, -1127.49529523, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 33.00247808, 7.725e-05, 99.00743423, 0.00023175, 330.02478076, 0.0007725, -33.00247808, -7.725e-05, -99.00743423, -0.00023175, -330.02478076, -0.0007725, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 132.0099123, 0.01362266, 132.0099123, 0.04086797, 92.40693861, -1127.49529523, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 33.00247808, 7.725e-05, 99.00743423, 0.00023175, 330.02478076, 0.0007725, -33.00247808, -7.725e-05, -99.00743423, -0.00023175, -330.02478076, -0.0007725, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 15.6, 5.5, 6.4)
    ops.node(123011, 15.6, 5.5, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 29493935.56057769, 12289139.81690737, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 106.50570462, 0.00071102, 127.81446119, 0.0155743, 12.78144612, 0.03904239, -106.50570462, -0.00071102, -127.81446119, -0.0155743, -12.78144612, -0.03904239, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 106.50570462, 0.00071102, 127.81446119, 0.0155743, 12.78144612, 0.03904239, -106.50570462, -0.00071102, -127.81446119, -0.0155743, -12.78144612, -0.03904239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 119.86177836, 0.01422035, 119.86177836, 0.04266105, 83.90324485, -1015.07256632, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 29.96544459, 7.405e-05, 89.89633377, 0.00022214, 299.6544459, 0.00074047, -29.96544459, -7.405e-05, -89.89633377, -0.00022214, -299.6544459, -0.00074047, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 119.86177836, 0.01422035, 119.86177836, 0.04266105, 83.90324485, -1015.07256632, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 29.96544459, 7.405e-05, 89.89633377, 0.00022214, 299.6544459, 0.00074047, -29.96544459, -7.405e-05, -89.89633377, -0.00022214, -299.6544459, -0.00074047, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 19.85, 5.5, 6.475)
    ops.node(123012, 19.85, 5.5, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 30597044.86677891, 12748768.69449121, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 42.06343869, 0.00091584, 50.10565381, 0.01776357, 5.01056538, 0.05478798, -42.06343869, -0.00091584, -50.10565381, -0.01776357, -5.01056538, -0.05478798, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 42.06343869, 0.00091584, 50.10565381, 0.01776357, 5.01056538, 0.05478798, -42.06343869, -0.00091584, -50.10565381, -0.01776357, -5.01056538, -0.05478798, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 83.94344647, 0.01831676, 83.94344647, 0.05495028, 58.76041253, -935.90468077, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 20.98586162, 9.798e-05, 62.95758485, 0.00029393, 209.85861617, 0.00097976, -20.98586162, -9.798e-05, -62.95758485, -0.00029393, -209.85861617, -0.00097976, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 83.94344647, 0.01831676, 83.94344647, 0.05495028, 58.76041253, -935.90468077, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 20.98586162, 9.798e-05, 62.95758485, 0.00029393, 209.85861617, 0.00097976, -20.98586162, -9.798e-05, -62.95758485, -0.00029393, -209.85861617, -0.00097976, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 11.0, 6.475)
    ops.node(123013, 0.0, 11.0, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 29135056.63365114, 12139606.93068798, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 33.44195182, 0.00087634, 40.25157099, 0.02064796, 4.0251571, 0.06508023, -33.44195182, -0.00087634, -40.25157099, -0.02064796, -4.0251571, -0.06508023, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 35.75009584, 0.00087634, 43.02971095, 0.02064796, 4.3029711, 0.06508023, -35.75009584, -0.00087634, -43.02971095, -0.02064796, -4.3029711, -0.06508023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 72.93553954, 0.01752689, 72.93553954, 0.05258068, 51.05487768, -808.66138729, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 18.23388489, 8.94e-05, 54.70165466, 0.0002682, 182.33884886, 0.000894, -18.23388489, -8.94e-05, -54.70165466, -0.0002682, -182.33884886, -0.000894, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 72.93553954, 0.01752689, 72.93553954, 0.05258068, 51.05487768, -808.66138729, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 18.23388489, 8.94e-05, 54.70165466, 0.0002682, 182.33884886, 0.000894, -18.23388489, -8.94e-05, -54.70165466, -0.0002682, -182.33884886, -0.000894, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.25, 11.0, 6.4)
    ops.node(123014, 4.25, 11.0, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 29643926.87312956, 12351636.19713732, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 48.49297311, 0.00097778, 57.88527723, 0.01784469, 5.78852772, 0.04923845, -48.49297311, -0.00097778, -57.88527723, -0.01784469, -5.78852772, -0.04923845, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 48.49297311, 0.00097778, 57.88527723, 0.01784469, 5.78852772, 0.04923845, -48.49297311, -0.00097778, -57.88527723, -0.01784469, -5.78852772, -0.04923845, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 73.29109022, 0.01955555, 73.29109022, 0.05866664, 51.30376316, -800.73421498, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 18.32277256, 8.829e-05, 54.96831767, 0.00026488, 183.22772556, 0.00088294, -18.32277256, -8.829e-05, -54.96831767, -0.00026488, -183.22772556, -0.00088294, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 73.29109022, 0.01955555, 73.29109022, 0.05866664, 51.30376316, -800.73421498, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 18.32277256, 8.829e-05, 54.96831767, 0.00026488, 183.22772556, 0.00088294, -18.32277256, -8.829e-05, -54.96831767, -0.00026488, -183.22772556, -0.00088294, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 8.5, 11.0, 6.375)
    ops.node(123015, 8.5, 11.0, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 29332768.68434987, 12221986.95181245, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 43.65559899, 0.00096315, 52.30124039, 0.01872223, 5.23012404, 0.05281173, -43.65559899, -0.00096315, -52.30124039, -0.01872223, -5.23012404, -0.05281173, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 43.65559899, 0.00096315, 52.30124039, 0.01872223, 5.23012404, 0.05281173, -43.65559899, -0.00096315, -52.30124039, -0.01872223, -5.23012404, -0.05281173, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 70.04522894, 0.01926301, 70.04522894, 0.05778904, 49.03166026, -753.43030321, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 17.51130723, 8.528e-05, 52.5339217, 0.00025584, 175.11307234, 0.00085279, -17.51130723, -8.528e-05, -52.5339217, -0.00025584, -175.11307234, -0.00085279, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 70.04522894, 0.01926301, 70.04522894, 0.05778904, 49.03166026, -753.43030321, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 17.51130723, 8.528e-05, 52.5339217, 0.00025584, 175.11307234, 0.00085279, -17.51130723, -8.528e-05, -52.5339217, -0.00025584, -175.11307234, -0.00085279, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 11.35, 11.0, 6.375)
    ops.node(123016, 11.35, 11.0, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 29353371.1610828, 12230571.31711783, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 44.48975238, 0.00091737, 53.29974272, 0.01890543, 5.32997427, 0.05303736, -44.48975238, -0.00091737, -53.29974272, -0.01890543, -5.32997427, -0.05303736, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 44.48975238, 0.00091737, 53.29974272, 0.01890543, 5.32997427, 0.05303736, -44.48975238, -0.00091737, -53.29974272, -0.01890543, -5.32997427, -0.05303736, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 71.06034425, 0.01834735, 71.06034425, 0.05504205, 49.74224098, -752.88693998, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 17.76508606, 8.645e-05, 53.29525819, 0.00025936, 177.65086063, 0.00086454, -17.76508606, -8.645e-05, -53.29525819, -0.00025936, -177.65086063, -0.00086454, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 71.06034425, 0.01834735, 71.06034425, 0.05504205, 49.74224098, -752.88693998, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 17.76508606, 8.645e-05, 53.29525819, 0.00025936, 177.65086063, 0.00086454, -17.76508606, -8.645e-05, -53.29525819, -0.00025936, -177.65086063, -0.00086454, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 15.6, 11.0, 6.4)
    ops.node(123017, 15.6, 11.0, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 30174667.91990622, 12572778.29996092, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 48.92349255, 0.00094949, 58.37764469, 0.01835539, 5.83776447, 0.050877, -48.92349255, -0.00094949, -58.37764469, -0.01835539, -5.83776447, -0.050877, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 48.92349255, 0.00094949, 58.37764469, 0.01835539, 5.83776447, 0.050877, -48.92349255, -0.00094949, -58.37764469, -0.01835539, -5.83776447, -0.050877, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 77.47032404, 0.01898979, 77.47032404, 0.05696936, 54.22922683, -822.97285276, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 19.36758101, 9.169e-05, 58.10274303, 0.00027506, 193.67581011, 0.00091687, -19.36758101, -9.169e-05, -58.10274303, -0.00027506, -193.67581011, -0.00091687, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 77.47032404, 0.01898979, 77.47032404, 0.05696936, 54.22922683, -822.97285276, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 19.36758101, 9.169e-05, 58.10274303, 0.00027506, 193.67581011, 0.00091687, -19.36758101, -9.169e-05, -58.10274303, -0.00027506, -193.67581011, -0.00091687, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 19.85, 11.0, 6.475)
    ops.node(123018, 19.85, 11.0, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 29573095.02816795, 12322122.92840331, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 33.52345314, 0.00086879, 40.3270964, 0.02064899, 4.03270964, 0.06597389, -33.52345314, -0.00086879, -40.3270964, -0.02064899, -4.03270964, -0.06597389, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 35.85471597, 0.00086879, 43.13149308, 0.02064899, 4.31314931, 0.06597389, -35.85471597, -0.00086879, -43.13149308, -0.02064899, -4.31314931, -0.06597389, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 73.22993455, 0.01737574, 73.22993455, 0.05212723, 51.26095419, -794.2109855, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 18.30748364, 8.843e-05, 54.92245092, 0.00026529, 183.07483638, 0.00088431, -18.30748364, -8.843e-05, -54.92245092, -0.00026529, -183.07483638, -0.00088431, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 73.22993455, 0.01737574, 73.22993455, 0.05212723, 51.26095419, -794.2109855, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 18.30748364, 8.843e-05, 54.92245092, 0.00026529, 183.07483638, 0.00088431, -18.30748364, -8.843e-05, -54.92245092, -0.00026529, -183.07483638, -0.00088431, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.575)
    ops.node(124001, 0.0, 0.0, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 31020624.39152125, 12925260.16313385, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 18.85706481, 0.00075221, 22.79793943, 0.02182093, 2.27979394, 0.08175008, -18.85706481, -0.00075221, -22.79793943, -0.02182093, -2.27979394, -0.08175008, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 18.85706481, 0.00075221, 22.79793943, 0.02182093, 2.27979394, 0.08175008, -18.85706481, -0.00075221, -22.79793943, -0.02182093, -2.27979394, -0.08175008, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 66.10058987, 0.01504419, 66.10058987, 0.04513256, 46.27041291, -867.24621361, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 16.52514747, 7.61e-05, 49.5754424, 0.00022829, 165.25147468, 0.00076097, -16.52514747, -7.61e-05, -49.5754424, -0.00022829, -165.25147468, -0.00076097, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 66.10058987, 0.01504419, 66.10058987, 0.04513256, 46.27041291, -867.24621361, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 16.52514747, 7.61e-05, 49.5754424, 0.00022829, 165.25147468, 0.00076097, -16.52514747, -7.61e-05, -49.5754424, -0.00022829, -165.25147468, -0.00076097, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.25, 0.0, 9.525)
    ops.node(124002, 4.25, 0.0, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 29592332.04092986, 12330138.35038744, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 32.02371242, 0.00090821, 38.70293377, 0.02226106, 3.87029338, 0.06748752, -32.02371242, -0.00090821, -38.70293377, -0.02226106, -3.87029338, -0.06748752, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 32.02371242, 0.00090821, 38.70293377, 0.02226106, 3.87029338, 0.06748752, -32.02371242, -0.00090821, -38.70293377, -0.02226106, -3.87029338, -0.06748752, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 60.85824201, 0.01816417, 60.85824201, 0.05449252, 42.6007694, -628.84547152, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 15.2145605, 7.344e-05, 45.6436815, 0.00022033, 152.14560501, 0.00073444, -15.2145605, -7.344e-05, -45.6436815, -0.00022033, -152.14560501, -0.00073444, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 60.85824201, 0.01816417, 60.85824201, 0.05449252, 42.6007694, -628.84547152, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 15.2145605, 7.344e-05, 45.6436815, 0.00022033, 152.14560501, 0.00073444, -15.2145605, -7.344e-05, -45.6436815, -0.00022033, -152.14560501, -0.00073444, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 15.6, 0.0, 9.525)
    ops.node(124005, 15.6, 0.0, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 28288363.00231304, 11786817.91763043, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 32.88181519, 0.00086391, 39.82664216, 0.02266997, 3.98266422, 0.06610433, -32.88181519, -0.00086391, -39.82664216, -0.02266997, -3.98266422, -0.06610433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 32.88181519, 0.00086391, 39.82664216, 0.02266997, 3.98266422, 0.06610433, -32.88181519, -0.00086391, -39.82664216, -0.02266997, -3.98266422, -0.06610433, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 60.38540336, 0.01727827, 60.38540336, 0.05183482, 42.26978235, -641.71876486, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 15.09635084, 7.623e-05, 45.28905252, 0.0002287, 150.96350839, 0.00076232, -15.09635084, -7.623e-05, -45.28905252, -0.0002287, -150.96350839, -0.00076232, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 60.38540336, 0.01727827, 60.38540336, 0.05183482, 42.26978235, -641.71876486, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 15.09635084, 7.623e-05, 45.28905252, 0.0002287, 150.96350839, 0.00076232, -15.09635084, -7.623e-05, -45.28905252, -0.0002287, -150.96350839, -0.00076232, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 19.85, 0.0, 9.575)
    ops.node(124006, 19.85, 0.0, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 29193245.06808516, 12163852.11170215, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 18.58441723, 0.00077742, 22.57188011, 0.02294283, 2.25718801, 0.08140216, -18.58441723, -0.00077742, -22.57188011, -0.02294283, -2.25718801, -0.08140216, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 18.58441723, 0.00077742, 22.57188011, 0.02294283, 2.25718801, 0.08140216, -18.58441723, -0.00077742, -22.57188011, -0.02294283, -2.25718801, -0.08140216, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 63.74655875, 0.01554847, 63.74655875, 0.04664542, 44.62259113, -917.20779869, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 15.93663969, 7.798e-05, 47.80991906, 0.00023394, 159.36639688, 0.00077981, -15.93663969, -7.798e-05, -47.80991906, -0.00023394, -159.36639688, -0.00077981, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 63.74655875, 0.01554847, 63.74655875, 0.04664542, 44.62259113, -917.20779869, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 15.93663969, 7.798e-05, 47.80991906, 0.00023394, 159.36639688, 0.00077981, -15.93663969, -7.798e-05, -47.80991906, -0.00023394, -159.36639688, -0.00077981, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 5.5, 9.575)
    ops.node(124007, 0.0, 5.5, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 30428713.35648407, 12678630.5652017, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 24.2337422, 0.00081156, 29.23986508, 0.02114868, 2.92398651, 0.07459671, -24.2337422, -0.00081156, -29.23986508, -0.02114868, -2.92398651, -0.07459671, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 24.2337422, 0.00081156, 29.23986508, 0.02114868, 2.92398651, 0.07459671, -24.2337422, -0.00081156, -29.23986508, -0.02114868, -2.92398651, -0.07459671, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 69.8247247, 0.01623126, 69.8247247, 0.04869377, 48.87730729, -769.05972885, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 17.45618118, 8.195e-05, 52.36854353, 0.00024584, 174.56181175, 0.00081948, -17.45618118, -8.195e-05, -52.36854353, -0.00024584, -174.56181175, -0.00081948, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 69.8247247, 0.01623126, 69.8247247, 0.04869377, 48.87730729, -769.05972885, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 17.45618118, 8.195e-05, 52.36854353, 0.00024584, 174.56181175, 0.00081948, -17.45618118, -8.195e-05, -52.36854353, -0.00024584, -174.56181175, -0.00081948, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.25, 5.5, 9.525)
    ops.node(124008, 4.25, 5.5, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 29284838.15243782, 12202015.89684909, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 78.68060513, 0.00067902, 95.24402254, 0.01725239, 9.52440225, 0.04710926, -78.68060513, -0.00067902, -95.24402254, -0.01725239, -9.52440225, -0.04710926, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 78.68060513, 0.00067902, 95.24402254, 0.01725239, 9.52440225, 0.04710926, -78.68060513, -0.00067902, -95.24402254, -0.01725239, -9.52440225, -0.04710926, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 102.89458553, 0.01358045, 102.89458553, 0.04074136, 72.02620987, -730.77862407, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 25.72364638, 6.402e-05, 77.17093914, 0.00019206, 257.23646382, 0.00064019, -25.72364638, -6.402e-05, -77.17093914, -0.00019206, -257.23646382, -0.00064019, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 102.89458553, 0.01358045, 102.89458553, 0.04074136, 72.02620987, -730.77862407, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 25.72364638, 6.402e-05, 77.17093914, 0.00019206, 257.23646382, 0.00064019, -25.72364638, -6.402e-05, -77.17093914, -0.00019206, -257.23646382, -0.00064019, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 8.5, 5.5, 9.525)
    ops.node(124009, 8.5, 5.5, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 27840061.29149565, 11600025.53812319, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 66.88319661, 0.00063349, 81.24914804, 0.02010402, 8.1249148, 0.05595315, -66.88319661, -0.00063349, -81.24914804, -0.02010402, -8.1249148, -0.05595315, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 63.2097111, 0.00063349, 76.78662856, 0.02010402, 7.67866286, 0.05595315, -63.2097111, -0.00063349, -76.78662856, -0.02010402, -7.67866286, -0.05595315, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 103.18669775, 0.01266979, 103.18669775, 0.03800938, 72.23068843, -903.25402948, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 25.79667444, 6.753e-05, 77.39002331, 0.0002026, 257.96674438, 0.00067532, -25.79667444, -6.753e-05, -77.39002331, -0.0002026, -257.96674438, -0.00067532, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 103.18669775, 0.01266979, 103.18669775, 0.03800938, 72.23068843, -903.25402948, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 25.79667444, 6.753e-05, 77.39002331, 0.0002026, 257.96674438, 0.00067532, -25.79667444, -6.753e-05, -77.39002331, -0.0002026, -257.96674438, -0.00067532, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 11.35, 5.5, 9.525)
    ops.node(124010, 11.35, 5.5, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 28895389.69429726, 12039745.70595719, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 67.13123052, 0.00064089, 81.4031295, 0.01950763, 8.14031295, 0.05635493, -67.13123052, -0.00064089, -81.4031295, -0.01950763, -8.14031295, -0.05635493, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 63.55351413, 0.00064089, 77.06480129, 0.01950763, 7.70648013, 0.05635493, -63.55351413, -0.00064089, -77.06480129, -0.01950763, -7.70648013, -0.05635493, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 106.48185651, 0.01281782, 106.48185651, 0.03845345, 74.53729956, -889.9751358, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 26.62046413, 6.714e-05, 79.86139239, 0.00020143, 266.20464128, 0.00067144, -26.62046413, -6.714e-05, -79.86139239, -0.00020143, -266.20464128, -0.00067144, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 106.48185651, 0.01281782, 106.48185651, 0.03845345, 74.53729956, -889.9751358, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 26.62046413, 6.714e-05, 79.86139239, 0.00020143, 266.20464128, 0.00067144, -26.62046413, -6.714e-05, -79.86139239, -0.00020143, -266.20464128, -0.00067144, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 15.6, 5.5, 9.525)
    ops.node(124011, 15.6, 5.5, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 28198308.26073333, 11749295.10863889, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 78.35521755, 0.0006732, 95.02794169, 0.01724313, 9.50279417, 0.04620191, -78.35521755, -0.0006732, -95.02794169, -0.01724313, -9.50279417, -0.04620191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 78.35521755, 0.0006732, 95.02794169, 0.01724313, 9.50279417, 0.04620191, -78.35521755, -0.0006732, -95.02794169, -0.01724313, -9.50279417, -0.04620191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 98.83849975, 0.01346409, 98.83849975, 0.04039228, 69.18694982, -728.11293874, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 24.70962494, 6.386e-05, 74.12887481, 0.00019159, 247.09624937, 0.00063865, -24.70962494, -6.386e-05, -74.12887481, -0.00019159, -247.09624937, -0.00063865, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 98.83849975, 0.01346409, 98.83849975, 0.04039228, 69.18694982, -728.11293874, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 24.70962494, 6.386e-05, 74.12887481, 0.00019159, 247.09624937, 0.00063865, -24.70962494, -6.386e-05, -74.12887481, -0.00019159, -247.09624937, -0.00063865, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 19.85, 5.5, 9.575)
    ops.node(124012, 19.85, 5.5, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 31794396.62053964, 13247665.25855818, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 24.27284511, 0.00078274, 29.18899943, 0.02088941, 2.91889994, 0.07600111, -24.27284511, -0.00078274, -29.18899943, -0.02088941, -2.91889994, -0.07600111, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 24.27284511, 0.00078274, 29.18899943, 0.02088941, 2.91889994, 0.07600111, -24.27284511, -0.00078274, -29.18899943, -0.02088941, -2.91889994, -0.07600111, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 72.18907661, 0.01565476, 72.18907661, 0.04696429, 50.53235363, -759.63630664, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 18.04726915, 8.108e-05, 54.14180746, 0.00024325, 180.47269152, 0.00081084, -18.04726915, -8.108e-05, -54.14180746, -0.00024325, -180.47269152, -0.00081084, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 72.18907661, 0.01565476, 72.18907661, 0.04696429, 50.53235363, -759.63630664, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 18.04726915, 8.108e-05, 54.14180746, 0.00024325, 180.47269152, 0.00081084, -18.04726915, -8.108e-05, -54.14180746, -0.00024325, -180.47269152, -0.00081084, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 11.0, 9.575)
    ops.node(124013, 0.0, 11.0, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 31213971.14753272, 13005821.31147197, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 18.8582105, 0.00077751, 22.78691765, 0.02173866, 2.27869176, 0.08180395, -18.8582105, -0.00077751, -22.78691765, -0.02173866, -2.27869176, -0.08180395, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 18.8582105, 0.00077751, 22.78691765, 0.02173866, 2.27869176, 0.08180395, -18.8582105, -0.00077751, -22.78691765, -0.02173866, -2.27869176, -0.08180395, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 66.35911242, 0.01555022, 66.35911242, 0.04665067, 46.4513787, -862.12629363, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 16.58977811, 7.592e-05, 49.76933432, 0.00022776, 165.89778106, 0.00075922, -16.58977811, -7.592e-05, -49.76933432, -0.00022776, -165.89778106, -0.00075922, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 66.35911242, 0.01555022, 66.35911242, 0.04665067, 46.4513787, -862.12629363, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 16.58977811, 7.592e-05, 49.76933432, 0.00022776, 165.89778106, 0.00075922, -16.58977811, -7.592e-05, -49.76933432, -0.00022776, -165.89778106, -0.00075922, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.25, 11.0, 9.525)
    ops.node(124014, 4.25, 11.0, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 30248916.66944319, 12603715.27893466, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 32.70365793, 0.00086067, 39.47206166, 0.02129313, 3.94720617, 0.06732243, -32.70365793, -0.00086067, -39.47206166, -0.02129313, -3.94720617, -0.06732243, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 32.70365793, 0.00086067, 39.47206166, 0.02129313, 3.94720617, 0.06732243, -32.70365793, -0.00086067, -39.47206166, -0.02129313, -3.94720617, -0.06732243, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 62.35791734, 0.01721346, 62.35791734, 0.05164037, 43.65054214, -629.64790796, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 15.58947933, 7.362e-05, 46.768438, 0.00022086, 155.89479334, 0.0007362, -15.58947933, -7.362e-05, -46.768438, -0.00022086, -155.89479334, -0.0007362, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 62.35791734, 0.01721346, 62.35791734, 0.05164037, 43.65054214, -629.64790796, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 15.58947933, 7.362e-05, 46.768438, 0.00022086, 155.89479334, 0.0007362, -15.58947933, -7.362e-05, -46.768438, -0.00022086, -155.89479334, -0.0007362, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 8.5, 11.0, 9.525)
    ops.node(124015, 8.5, 11.0, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 29723133.21736702, 12384638.84056959, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 30.21812816, 0.00085682, 36.56447141, 0.0223172, 3.65644714, 0.0697127, -30.21812816, -0.00085682, -36.56447141, -0.0223172, -3.65644714, -0.0697127, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 30.21812816, 0.00085682, 36.56447141, 0.0223172, 3.65644714, 0.0697127, -30.21812816, -0.00085682, -36.56447141, -0.0223172, -3.65644714, -0.0697127, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 62.02147422, 0.01713649, 62.02147422, 0.05140946, 43.41503195, -642.0850806, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 15.50536855, 7.452e-05, 46.51610566, 0.00022355, 155.05368555, 0.00074518, -15.50536855, -7.452e-05, -46.51610566, -0.00022355, -155.05368555, -0.00074518, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 62.02147422, 0.01713649, 62.02147422, 0.05140946, 43.41503195, -642.0850806, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 15.50536855, 7.452e-05, 46.51610566, 0.00022355, 155.05368555, 0.00074518, -15.50536855, -7.452e-05, -46.51610566, -0.00022355, -155.05368555, -0.00074518, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 11.35, 11.0, 9.525)
    ops.node(124016, 11.35, 11.0, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 30140039.15801616, 12558349.6491734, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 30.89671608, 0.00084664, 37.35143548, 0.02225342, 3.73514355, 0.07008657, -30.89671608, -0.00084664, -37.35143548, -0.02225342, -3.73514355, -0.07008657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 30.89671608, 0.00084664, 37.35143548, 0.02225342, 3.73514355, 0.07008657, -30.89671608, -0.00084664, -37.35143548, -0.02225342, -3.73514355, -0.07008657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 63.61908131, 0.01693276, 63.61908131, 0.05079829, 44.53335692, -653.34056242, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 15.90477033, 7.538e-05, 47.71431098, 0.00022614, 159.04770327, 0.0007538, -15.90477033, -7.538e-05, -47.71431098, -0.00022614, -159.04770327, -0.0007538, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 63.61908131, 0.01693276, 63.61908131, 0.05079829, 44.53335692, -653.34056242, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 15.90477033, 7.538e-05, 47.71431098, 0.00022614, 159.04770327, 0.0007538, -15.90477033, -7.538e-05, -47.71431098, -0.00022614, -159.04770327, -0.0007538, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 15.6, 11.0, 9.525)
    ops.node(124017, 15.6, 11.0, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 28658988.31722701, 11941245.13217792, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 32.70299808, 0.00086167, 39.58812371, 0.02174078, 3.95881237, 0.06571306, -32.70299808, -0.00086167, -39.58812371, -0.02174078, -3.95881237, -0.06571306, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 32.70299808, 0.00086167, 39.58812371, 0.02174078, 3.95881237, 0.06571306, -32.70299808, -0.00086167, -39.58812371, -0.02174078, -3.95881237, -0.06571306, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 61.16214309, 0.01723336, 61.16214309, 0.05170008, 42.81350016, -641.56933799, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 15.29053577, 7.621e-05, 45.87160732, 0.00022864, 152.90535773, 0.00076214, -15.29053577, -7.621e-05, -45.87160732, -0.00022864, -152.90535773, -0.00076214, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 61.16214309, 0.01723336, 61.16214309, 0.05170008, 42.81350016, -641.56933799, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 15.29053577, 7.621e-05, 45.87160732, 0.00022864, 152.90535773, 0.00076214, -15.29053577, -7.621e-05, -45.87160732, -0.00022864, -152.90535773, -0.00076214, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 19.85, 11.0, 9.575)
    ops.node(124018, 19.85, 11.0, 12.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 29015982.99376784, 12089992.91406994, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 18.68005537, 0.00076807, 22.69696585, 0.02240186, 2.26969658, 0.08069892, -18.68005537, -0.00076807, -22.69696585, -0.02240186, -2.26969658, -0.08069892, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 18.68005537, 0.00076807, 22.69696585, 0.02240186, 2.26969658, 0.08069892, -18.68005537, -0.00076807, -22.69696585, -0.02240186, -2.26969658, -0.08069892, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 61.93987807, 0.01536142, 61.93987807, 0.04608427, 43.35791465, -847.8226069, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 15.48496952, 7.623e-05, 46.45490855, 0.0002287, 154.84969516, 0.00076234, -15.48496952, -7.623e-05, -46.45490855, -0.0002287, -154.84969516, -0.00076234, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 61.93987807, 0.01536142, 61.93987807, 0.04608427, 43.35791465, -847.8226069, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 15.48496952, 7.623e-05, 46.45490855, 0.0002287, 154.84969516, 0.00076234, -15.48496952, -7.623e-05, -46.45490855, -0.0002287, -154.84969516, -0.00076234, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.5, 0.0, 0.0)
    ops.node(124019, 8.5, 0.0, 1.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 170003, 124019, 0.1225, 29547375.95342891, 12311406.64726205, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 160.23766722, 0.0005725, 190.86151167, 0.02862998, 19.08615117, 0.06744447, -160.23766722, -0.0005725, -190.86151167, -0.02862998, -19.08615117, -0.06744447, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 155.81429248, 0.0005725, 185.59276304, 0.02862998, 18.5592763, 0.06744447, -155.81429248, -0.0005725, -185.59276304, -0.02862998, -18.5592763, -0.06744447, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 218.48497302, 0.01144994, 218.48497302, 0.03434981, 152.93948111, -4060.88751676, 0.05, 2, 0, 70003, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 54.62124325, 6.736e-05, 163.86372976, 0.00020209, 546.21243254, 0.00067364, -54.62124325, -6.736e-05, -163.86372976, -0.00020209, -546.21243254, -0.00067364, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 218.48497302, 0.01144994, 218.48497302, 0.03434981, 152.93948111, -4060.88751676, 0.05, 2, 0, 70003, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 54.62124325, 6.736e-05, 163.86372976, 0.00020209, 546.21243254, 0.00067364, -54.62124325, -6.736e-05, -163.86372976, -0.00020209, -546.21243254, -0.00067364, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 8.5, 0.0, 1.8)
    ops.node(121003, 8.5, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 121003, 0.1225, 29170535.41267037, 12154389.75527932, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 116.90209011, 0.00057087, 139.50796778, 0.0269118, 13.95079678, 0.06670949, -116.90209011, -0.00057087, -139.50796778, -0.0269118, -13.95079678, -0.06670949, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 112.96141231, 0.00057087, 134.80526356, 0.0269118, 13.48052636, 0.06670949, -112.96141231, -0.00057087, -134.80526356, -0.0269118, -13.48052636, -0.06670949, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 212.42998064, 0.01141733, 212.42998064, 0.034252, 148.70098645, -3966.32724353, 0.05, 2, 0, 74019, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 53.10749516, 6.634e-05, 159.32248548, 0.00019903, 531.0749516, 0.00066344, -53.10749516, -6.634e-05, -159.32248548, -0.00019903, -531.0749516, -0.00066344, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 212.42998064, 0.01141733, 212.42998064, 0.034252, 148.70098645, -3966.32724353, 0.05, 2, 0, 74019, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 53.10749516, 6.634e-05, 159.32248548, 0.00019903, 531.0749516, 0.00066344, -53.10749516, -6.634e-05, -159.32248548, -0.00019903, -531.0749516, -0.00066344, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 11.35, 0.0, 0.0)
    ops.node(124020, 11.35, 0.0, 1.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 170004, 124020, 0.1225, 28037298.35132778, 11682207.64638657, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 158.97954685, 0.00059305, 189.29490878, 0.02743634, 18.92949088, 0.06147606, -158.97954685, -0.00059305, -189.29490878, -0.02743634, -18.92949088, -0.06147606, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 154.67365749, 0.00059305, 184.16794151, 0.02743634, 18.41679415, 0.06147606, -154.67365749, -0.00059305, -184.16794151, -0.02743634, -18.41679415, -0.06147606, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 209.21982686, 0.01186099, 209.21982686, 0.03558298, 146.4538788, -4046.88139191, 0.05, 2, 0, 70004, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 52.30495671, 6.798e-05, 156.91487014, 0.00020395, 523.04956714, 0.00067982, -52.30495671, -6.798e-05, -156.91487014, -0.00020395, -523.04956714, -0.00067982, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 209.21982686, 0.01186099, 209.21982686, 0.03558298, 146.4538788, -4046.88139191, 0.05, 2, 0, 70004, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 52.30495671, 6.798e-05, 156.91487014, 0.00020395, 523.04956714, 0.00067982, -52.30495671, -6.798e-05, -156.91487014, -0.00020395, -523.04956714, -0.00067982, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 11.35, 0.0, 1.8)
    ops.node(121004, 11.35, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 121004, 0.1225, 31434178.94242973, 13097574.55934572, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 119.20490467, 0.00055448, 141.98093811, 0.02756729, 14.19809381, 0.07361951, -119.20490467, -0.00055448, -141.98093811, -0.02756729, -14.19809381, -0.07361951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 115.02788513, 0.00055448, 137.00583113, 0.02756729, 13.70058311, 0.07361951, -115.02788513, -0.00055448, -137.00583113, -0.02756729, -13.70058311, -0.07361951, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 225.85040306, 0.01108966, 225.85040306, 0.03326898, 158.09528214, -3962.412747, 0.05, 2, 0, 74020, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 56.46260076, 6.546e-05, 169.38780229, 0.00019637, 564.62600765, 0.00065456, -56.46260076, -6.546e-05, -169.38780229, -0.00019637, -564.62600765, -0.00065456, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 225.85040306, 0.01108966, 225.85040306, 0.03326898, 158.09528214, -3962.412747, 0.05, 2, 0, 74020, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 56.46260076, 6.546e-05, 169.38780229, 0.00019637, 564.62600765, 0.00065456, -56.46260076, -6.546e-05, -169.38780229, -0.00019637, -564.62600765, -0.00065456, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.5, 0.0, 3.3)
    ops.node(124021, 8.5, 0.0, 4.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 171003, 124021, 0.1225, 29363664.02316358, 12234860.00965149, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 103.15129733, 0.00054599, 123.63403141, 0.01973235, 12.36340314, 0.0505763, -103.15129733, -0.00054599, -123.63403141, -0.01973235, -12.36340314, -0.0505763, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 99.18500286, 0.00054599, 118.88015058, 0.01973235, 11.88801506, 0.0505763, -99.18500286, -0.00054599, -118.88015058, -0.01973235, -11.88801506, -0.0505763, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 180.51723826, 0.0109199, 180.51723826, 0.03275969, 126.36206678, -2706.10166355, 0.05, 2, 0, 71003, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 45.12930956, 5.601e-05, 135.38792869, 0.00016802, 451.29309565, 0.00056006, -45.12930956, -5.601e-05, -135.38792869, -0.00016802, -451.29309565, -0.00056006, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 180.51723826, 0.0109199, 180.51723826, 0.03275969, 126.36206678, -2706.10166355, 0.05, 2, 0, 71003, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 45.12930956, 5.601e-05, 135.38792869, 0.00016802, 451.29309565, 0.00056006, -45.12930956, -5.601e-05, -135.38792869, -0.00016802, -451.29309565, -0.00056006, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 8.5, 0.0, 4.9)
    ops.node(122003, 8.5, 0.0, 6.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 122003, 0.1225, 29502791.1085671, 12292829.62856962, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 94.4903635, 0.00054059, 113.44110239, 0.01995895, 11.34411024, 0.05274554, -94.4903635, -0.00054059, -113.44110239, -0.01995895, -11.34411024, -0.05274554, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 98.57459126, 0.00054059, 118.34445213, 0.01995895, 11.83444521, 0.05274554, -98.57459126, -0.00054059, -118.34445213, -0.01995895, -11.83444521, -0.05274554, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 175.40939483, 0.01081187, 175.40939483, 0.0324356, 122.78657638, -2531.49776167, 0.05, 2, 0, 74021, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 43.85234871, 5.416e-05, 131.55704612, 0.00016249, 438.52348707, 0.00054165, -43.85234871, -5.416e-05, -131.55704612, -0.00016249, -438.52348707, -0.00054165, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 175.40939483, 0.01081187, 175.40939483, 0.0324356, 122.78657638, -2531.49776167, 0.05, 2, 0, 74021, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 43.85234871, 5.416e-05, 131.55704612, 0.00016249, 438.52348707, 0.00054165, -43.85234871, -5.416e-05, -131.55704612, -0.00016249, -438.52348707, -0.00054165, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 11.35, 0.0, 3.3)
    ops.node(124022, 11.35, 0.0, 4.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 171004, 124022, 0.1225, 29091600.08226525, 12121500.03427719, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 102.93742291, 0.00054901, 123.40339554, 0.0196571, 12.34033955, 0.05000312, -102.93742291, -0.00054901, -123.40339554, -0.0196571, -12.34033955, -0.05000312, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 99.00594799, 0.00054901, 118.69026654, 0.0196571, 11.86902665, 0.05000312, -99.00594799, -0.00054901, -118.69026654, -0.0196571, -11.86902665, -0.05000312, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 178.36730048, 0.01098023, 178.36730048, 0.03294069, 124.85711034, -2680.85977013, 0.05, 2, 0, 71004, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 44.59182512, 5.586e-05, 133.77547536, 0.00016757, 445.9182512, 0.00055857, -44.59182512, -5.586e-05, -133.77547536, -0.00016757, -445.9182512, -0.00055857, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 178.36730048, 0.01098023, 178.36730048, 0.03294069, 124.85711034, -2680.85977013, 0.05, 2, 0, 71004, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 44.59182512, 5.586e-05, 133.77547536, 0.00016757, 445.9182512, 0.00055857, -44.59182512, -5.586e-05, -133.77547536, -0.00016757, -445.9182512, -0.00055857, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 11.35, 0.0, 4.9)
    ops.node(122004, 11.35, 0.0, 6.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 122004, 0.1225, 28929448.73600231, 12053936.9733343, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 92.99453437, 0.00054612, 111.70731786, 0.02013639, 11.17073179, 0.05192908, -92.99453437, -0.00054612, -111.70731786, -0.02013639, -11.17073179, -0.05192908, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 96.81169141, 0.00054612, 116.29258062, 0.02013639, 11.62925806, 0.05192908, -96.81169141, -0.00054612, -116.29258062, -0.02013639, -11.62925806, -0.05192908, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 172.30470983, 0.0109224, 172.30470983, 0.03276719, 120.61329688, -2536.30875389, 0.05, 2, 0, 74022, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 43.07617746, 5.426e-05, 129.22853237, 0.00016278, 430.76177457, 0.00054261, -43.07617746, -5.426e-05, -129.22853237, -0.00016278, -430.76177457, -0.00054261, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 172.30470983, 0.0109224, 172.30470983, 0.03276719, 120.61329688, -2536.30875389, 0.05, 2, 0, 74022, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 43.07617746, 5.426e-05, 129.22853237, 0.00016278, 430.76177457, 0.00054261, -43.07617746, -5.426e-05, -129.22853237, -0.00016278, -430.76177457, -0.00054261, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.5, 0.0, 6.375)
    ops.node(124023, 8.5, 0.0, 7.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 172003, 124023, 0.0625, 29240683.46867206, 12183618.11194669, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 49.30864086, 0.00068149, 58.82891679, 0.01756944, 5.88289168, 0.04745886, -49.30864086, -0.00068149, -58.82891679, -0.01756944, -5.88289168, -0.04745886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 49.30864086, 0.00068149, 58.82891679, 0.01756944, 5.88289168, 0.04745886, -49.30864086, -0.00068149, -58.82891679, -0.01756944, -5.88289168, -0.04745886, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 77.02886394, 0.01362986, 77.02886394, 0.04088958, 53.92020476, -1655.96637594, 0.05, 2, 0, 72003, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 19.25721599, 4.704e-05, 57.77164796, 0.00014111, 192.57215985, 0.00047038, -19.25721599, -4.704e-05, -57.77164796, -0.00014111, -192.57215985, -0.00047038, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 77.02886394, 0.01362986, 77.02886394, 0.04088958, 53.92020476, -1655.96637594, 0.05, 2, 0, 72003, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 19.25721599, 4.704e-05, 57.77164796, 0.00014111, 192.57215985, 0.00047038, -19.25721599, -4.704e-05, -57.77164796, -0.00014111, -192.57215985, -0.00047038, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 8.5, 0.0, 7.95)
    ops.node(123003, 8.5, 0.0, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 123003, 0.0625, 30357664.43954884, 12649026.84981202, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 44.88917032, 0.00066452, 53.70427926, 0.01858351, 5.37042793, 0.05432944, -44.88917032, -0.00066452, -53.70427926, -0.01858351, -5.37042793, -0.05432944, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 44.88917032, 0.00066452, 53.70427926, 0.01858351, 5.37042793, 0.05432944, -44.88917032, -0.00066452, -53.70427926, -0.01858351, -5.37042793, -0.05432944, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 74.56800244, 0.01329035, 74.56800244, 0.03987105, 52.19760171, -1508.42705562, 0.05, 2, 0, 74023, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 18.64200061, 4.386e-05, 55.92600183, 0.00013158, 186.42000611, 0.0004386, -18.64200061, -4.386e-05, -55.92600183, -0.00013158, -186.42000611, -0.0004386, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 74.56800244, 0.01329035, 74.56800244, 0.03987105, 52.19760171, -1508.42705562, 0.05, 2, 0, 74023, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 18.64200061, 4.386e-05, 55.92600183, 0.00013158, 186.42000611, 0.0004386, -18.64200061, -4.386e-05, -55.92600183, -0.00013158, -186.42000611, -0.0004386, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 11.35, 0.0, 6.375)
    ops.node(124024, 11.35, 0.0, 7.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 172004, 124024, 0.0625, 30059672.92295786, 12524863.71789911, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 49.34215849, 0.00069368, 58.84595566, 0.01761533, 5.88459557, 0.04930153, -49.34215849, -0.00069368, -58.84595566, -0.01761533, -5.88459557, -0.04930153, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 49.34215849, 0.00069368, 58.84595566, 0.01761533, 5.88459557, 0.04930153, -49.34215849, -0.00069368, -58.84595566, -0.01761533, -5.88459557, -0.04930153, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 78.10791863, 0.01387365, 78.10791863, 0.04162094, 54.67554304, -1660.46921019, 0.05, 2, 0, 72004, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 19.52697966, 4.64e-05, 58.58093898, 0.00013919, 195.26979659, 0.00046398, -19.52697966, -4.64e-05, -58.58093898, -0.00013919, -195.26979659, -0.00046398, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 78.10791863, 0.01387365, 78.10791863, 0.04162094, 54.67554304, -1660.46921019, 0.05, 2, 0, 72004, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 19.52697966, 4.64e-05, 58.58093898, 0.00013919, 195.26979659, 0.00046398, -19.52697966, -4.64e-05, -58.58093898, -0.00013919, -195.26979659, -0.00046398, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 11.35, 0.0, 7.95)
    ops.node(123004, 11.35, 0.0, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 123004, 0.0625, 29223038.73213694, 12176266.13839039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 44.56377717, 0.00066927, 53.37303799, 0.01835978, 5.3373038, 0.05183536, -44.56377717, -0.00066927, -53.37303799, -0.01835978, -5.3373038, -0.05183536, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 44.56377717, 0.00066927, 53.37303799, 0.01835978, 5.3373038, 0.05183536, -44.56377717, -0.00066927, -53.37303799, -0.01835978, -5.3373038, -0.05183536, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 71.91661386, 0.01338537, 71.91661386, 0.04015612, 50.3416297, -1507.06080219, 0.05, 2, 0, 74024, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 17.97915347, 4.394e-05, 53.9374604, 0.00013183, 179.79153466, 0.00043943, -17.97915347, -4.394e-05, -53.9374604, -0.00013183, -179.79153466, -0.00043943, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 71.91661386, 0.01338537, 71.91661386, 0.04015612, 50.3416297, -1507.06080219, 0.05, 2, 0, 74024, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 17.97915347, 4.394e-05, 53.9374604, 0.00013183, 179.79153466, 0.00043943, -17.97915347, -4.394e-05, -53.9374604, -0.00013183, -179.79153466, -0.00043943, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.5, 0.0, 9.525)
    ops.node(124025, 8.5, 0.0, 10.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4061, 173003, 124025, 0.0625, 27588891.6174261, 11495371.50726088, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24061, 32.69483659, 0.00063467, 39.62768828, 0.02161695, 3.96276883, 0.06371145, -32.69483659, -0.00063467, -39.62768828, -0.02161695, -3.96276883, -0.06371145, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14061, 32.69483659, 0.00063467, 39.62768828, 0.02161695, 3.96276883, 0.06371145, -32.69483659, -0.00063467, -39.62768828, -0.02161695, -3.96276883, -0.06371145, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24061, 4061, 0.0, 62.39837289, 0.01269343, 62.39837289, 0.03808028, 43.67886102, -1320.26320576, 0.05, 2, 0, 73003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44061, 15.59959322, 4.039e-05, 46.79877967, 0.00012116, 155.99593223, 0.00040385, -15.59959322, -4.039e-05, -46.79877967, -0.00012116, -155.99593223, -0.00040385, 0.4, 0.3, 0.003, 0.0, 0.0, 24061, 2)
    ops.limitCurve('ThreePoint', 14061, 4061, 0.0, 62.39837289, 0.01269343, 62.39837289, 0.03808028, 43.67886102, -1320.26320576, 0.05, 2, 0, 73003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34061, 15.59959322, 4.039e-05, 46.79877967, 0.00012116, 155.99593223, 0.00040385, -15.59959322, -4.039e-05, -46.79877967, -0.00012116, -155.99593223, -0.00040385, 0.4, 0.3, 0.003, 0.0, 0.0, 14061, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4061, 99999, 'P', 44061, 'Vy', 34061, 'Vz', 24061, 'My', 14061, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4061, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4061, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 8.5, 0.0, 11.05)
    ops.node(124003, 8.5, 0.0, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 174025, 124003, 0.0625, 30239701.23109622, 12599875.51295676, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 28.20036299, 0.00058582, 34.14702503, 0.02246808, 3.4147025, 0.07311451, -28.20036299, -0.00058582, -34.14702503, -0.02246808, -3.4147025, -0.07311451, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 28.20036299, 0.00058582, 34.14702503, 0.02246808, 3.4147025, 0.07311451, -28.20036299, -0.00058582, -34.14702503, -0.02246808, -3.4147025, -0.07311451, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 61.40087289, 0.01171647, 61.40087289, 0.03514942, 42.98061103, -1349.01953454, 0.05, 2, 0, 74025, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 15.35021822, 3.626e-05, 46.05065467, 0.00010877, 153.50218223, 0.00036256, -15.35021822, -3.626e-05, -46.05065467, -0.00010877, -153.50218223, -0.00036256, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 61.40087289, 0.01171647, 61.40087289, 0.03514942, 42.98061103, -1349.01953454, 0.05, 2, 0, 74025, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 15.35021822, 3.626e-05, 46.05065467, 0.00010877, 153.50218223, 0.00036256, -15.35021822, -3.626e-05, -46.05065467, -0.00010877, -153.50218223, -0.00036256, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 11.35, 0.0, 9.525)
    ops.node(124026, 11.35, 0.0, 10.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 173004, 124026, 0.0625, 28955036.54104822, 12064598.55877009, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 32.59784203, 0.00063264, 39.43502107, 0.02163039, 3.94350211, 0.06578565, -32.59784203, -0.00063264, -39.43502107, -0.02163039, -3.94350211, -0.06578565, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 32.59784203, 0.00063264, 39.43502107, 0.02163039, 3.94350211, 0.06578565, -32.59784203, -0.00063264, -39.43502107, -0.02163039, -3.94350211, -0.06578565, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 64.91285459, 0.01265275, 64.91285459, 0.03795824, 45.43899821, -1319.98225212, 0.05, 2, 0, 73004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 16.22821365, 4.003e-05, 48.68464094, 0.00012009, 162.28213647, 0.0004003, -16.22821365, -4.003e-05, -48.68464094, -0.00012009, -162.28213647, -0.0004003, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 64.91285459, 0.01265275, 64.91285459, 0.03795824, 45.43899821, -1319.98225212, 0.05, 2, 0, 73004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 16.22821365, 4.003e-05, 48.68464094, 0.00012009, 162.28213647, 0.0004003, -16.22821365, -4.003e-05, -48.68464094, -0.00012009, -162.28213647, -0.0004003, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 11.35, 0.0, 11.05)
    ops.node(124004, 11.35, 0.0, 12.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174026, 124004, 0.0625, 29679217.27517597, 12366340.53132332, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 28.38178143, 0.000588, 34.41320247, 0.02264506, 3.44132025, 0.07284936, -28.38178143, -0.000588, -34.41320247, -0.02264506, -3.44132025, -0.07284936, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 28.38178143, 0.000588, 34.41320247, 0.02264506, 3.44132025, 0.07284936, -28.38178143, -0.000588, -34.41320247, -0.02264506, -3.44132025, -0.07284936, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 60.11638346, 0.01176001, 60.11638346, 0.03528002, 42.08146842, -1306.92210616, 0.05, 2, 0, 74026, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 15.02909586, 3.617e-05, 45.08728759, 0.0001085, 150.29095865, 0.00036168, -15.02909586, -3.617e-05, -45.08728759, -0.0001085, -150.29095865, -0.00036168, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 60.11638346, 0.01176001, 60.11638346, 0.03528002, 42.08146842, -1306.92210616, 0.05, 2, 0, 74026, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 15.02909586, 3.617e-05, 45.08728759, 0.0001085, 150.29095865, 0.00036168, -15.02909586, -3.617e-05, -45.08728759, -0.0001085, -150.29095865, -0.00036168, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4064, '-orient', 0, 0, 1, 0, 1, 0)
