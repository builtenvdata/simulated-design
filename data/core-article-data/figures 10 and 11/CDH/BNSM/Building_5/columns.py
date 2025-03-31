import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.2025, 28171992.66113896, 11738330.27547457, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 290.07524082, 0.00106256, 350.13306073, 0.03593021, 35.01330607, 0.10398162, -290.07524082, -0.00106256, -350.13306073, -0.03593021, -35.01330607, -0.10398162, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 311.78711836, 0.00106256, 376.34021346, 0.03593021, 37.63402135, 0.10398162, -311.78711836, -0.00106256, -376.34021346, -0.03593021, -37.63402135, -0.10398162, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.5, 0.0, 0.0)
    ops.node(121002, 4.5, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.25, 30146450.7232196, 12561021.13467483, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 485.30036274, 0.00095873, 582.25398816, 0.03915803, 58.22539882, 0.11070572, -485.30036274, -0.00095873, -582.25398816, -0.03915803, -58.22539882, -0.11070572, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 512.6939249, 0.00095873, 615.12025418, 0.03915803, 61.51202542, 0.11070572, -512.6939249, -0.00095873, -615.12025418, -0.03915803, -61.51202542, -0.11070572, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.5, 0.0, 0.0)
    ops.node(121005, 16.5, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.25, 28459127.10995806, 11857969.62914919, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 481.59603202, 0.00099661, 578.81244911, 0.03839798, 57.88124491, 0.1038753, -481.59603202, -0.00099661, -578.81244911, -0.03839798, -57.88124491, -0.1038753, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 508.81334005, 0.00099661, 611.52392443, 0.03839798, 61.15239244, 0.1038753, -508.81334005, -0.00099661, -611.52392443, -0.03839798, -61.15239244, -0.1038753, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 21.0, 0.0, 0.0)
    ops.node(121006, 21.0, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.2025, 28128671.11286058, 11720279.63035857, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 290.62839985, 0.00103211, 350.81505385, 0.03574108, 35.08150539, 0.10365216, -290.62839985, -0.00103211, -350.81505385, -0.03574108, -35.08150539, -0.10365216, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 313.15488823, 0.00103211, 378.00658516, 0.03574108, 37.80065852, 0.10365216, -313.15488823, -0.00103211, -378.00658516, -0.03574108, -37.80065852, -0.10365216, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.5, 0.0)
    ops.node(121007, 0.0, 4.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.25, 28014913.05918365, 11672880.44132652, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 448.67710423, 0.00098406, 539.42032766, 0.03195793, 53.94203277, 0.086471, -448.67710423, -0.00098406, -539.42032766, -0.03195793, -53.94203277, -0.086471, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 448.67710423, 0.00098406, 539.42032766, 0.03195793, 53.94203277, 0.086471, -448.67710423, -0.00098406, -539.42032766, -0.03195793, -53.94203277, -0.086471, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.5, 4.5, 0.0)
    ops.node(121008, 4.5, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.5625, 28849467.95308392, 12020611.6471183, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 1996.91457646, 0.00078613, 2413.65183097, 0.06657233, 241.3651831, 0.16657233, -1996.91457646, -0.00078613, -2413.65183097, -0.06657233, -241.3651831, -0.16657233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 1996.91457646, 0.00078613, 2413.65183097, 0.06657233, 241.3651831, 0.16657233, -1996.91457646, -0.00078613, -2413.65183097, -0.06657233, -241.3651831, -0.16657233, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.0, 4.5, 0.0)
    ops.node(121009, 9.0, 4.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.3025, 29357638.77075427, 12232349.48781428, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 704.49924325, 0.0009179, 846.56420078, 0.04157459, 84.65642008, 0.120043, -704.49924325, -0.0009179, -846.56420078, -0.04157459, -84.65642008, -0.120043, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 673.07376187, 0.0009179, 808.8016513, 0.04157459, 80.88016513, 0.120043, -673.07376187, -0.0009179, -808.8016513, -0.04157459, -80.88016513, -0.120043, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.0, 4.5, 0.0)
    ops.node(121010, 12.0, 4.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.3025, 28988809.38776533, 12078670.57823556, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 701.71408599, 0.00092915, 843.53988052, 0.04210215, 84.35398805, 0.11909732, -701.71408599, -0.00092915, -843.53988052, -0.04210215, -84.35398805, -0.11909732, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 670.60616669, 0.00092915, 806.144635, 0.04210215, 80.6144635, 0.11909732, -670.60616669, -0.00092915, -806.144635, -0.04210215, -80.6144635, -0.11909732, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 16.5, 4.5, 0.0)
    ops.node(121011, 16.5, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.5625, 28067695.21309378, 11694873.00545574, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 1977.69596388, 0.00078377, 2392.92544255, 0.06627061, 239.29254425, 0.16627061, -1977.69596388, -0.00078377, -2392.92544255, -0.06627061, -239.29254425, -0.16627061, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 1977.69596388, 0.00078377, 2392.92544255, 0.06627061, 239.29254425, 0.16627061, -1977.69596388, -0.00078377, -2392.92544255, -0.06627061, -239.29254425, -0.16627061, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 21.0, 4.5, 0.0)
    ops.node(121012, 21.0, 4.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.25, 30379169.23356236, 12657987.18065098, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 456.92960028, 0.00097376, 548.06804362, 0.03317451, 54.80680436, 0.09500077, -456.92960028, -0.00097376, -548.06804362, -0.03317451, -54.80680436, -0.09500077, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 456.92960028, 0.00097376, 548.06804362, 0.03317451, 54.80680436, 0.09500077, -456.92960028, -0.00097376, -548.06804362, -0.03317451, -54.80680436, -0.09500077, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.25, 28963055.11222184, 12067939.63009243, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 452.48895309, 0.00096624, 543.67523462, 0.03258951, 54.36752346, 0.0902342, -452.48895309, -0.00096624, -543.67523462, -0.03258951, -54.36752346, -0.0902342, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 452.48895309, 0.00096624, 543.67523462, 0.03258951, 54.36752346, 0.0902342, -452.48895309, -0.00096624, -543.67523462, -0.03258951, -54.36752346, -0.0902342, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.5, 9.0, 0.0)
    ops.node(121014, 4.5, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.5625, 29702617.92737174, 12376090.80307156, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 1954.65403399, 0.0007517, 2359.22249247, 0.06712132, 235.92224925, 0.16712132, -1954.65403399, -0.0007517, -2359.22249247, -0.06712132, -235.92224925, -0.16712132, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 1954.65403399, 0.0007517, 2359.22249247, 0.06712132, 235.92224925, 0.16712132, -1954.65403399, -0.0007517, -2359.22249247, -0.06712132, -235.92224925, -0.16712132, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 9.0, 0.0)
    ops.node(121015, 9.0, 9.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.3025, 28999093.56691035, 12082955.65287931, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 698.93601945, 0.00092863, 840.13788348, 0.04189154, 84.01378835, 0.11878042, -698.93601945, -0.00092863, -840.13788348, -0.04189154, -84.01378835, -0.11878042, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 668.17806475, 0.00092863, 803.16608314, 0.04189154, 80.31660831, 0.11878042, -668.17806475, -0.00092863, -803.16608314, -0.04189154, -80.31660831, -0.11878042, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.0, 9.0, 0.0)
    ops.node(121016, 12.0, 9.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.3025, 28951009.78483889, 12062920.74368287, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 695.95633415, 0.00091666, 836.59380972, 0.04160897, 83.65938097, 0.11830163, -695.95633415, -0.00091666, -836.59380972, -0.04160897, -83.65938097, -0.11830163, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 665.11903067, 0.00091666, 799.52496513, 0.04160897, 79.95249651, 0.11830163, -665.11903067, -0.00091666, -799.52496513, -0.04160897, -79.95249651, -0.11830163, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 16.5, 9.0, 0.0)
    ops.node(121017, 16.5, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.5625, 27782287.66946178, 11575953.19560908, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 2002.00294609, 0.00078922, 2423.10919662, 0.06677248, 242.31091966, 0.16677248, -2002.00294609, -0.00078922, -2423.10919662, -0.06677248, -242.31091966, -0.16677248, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 2002.00294609, 0.00078922, 2423.10919662, 0.06677248, 242.31091966, 0.16677248, -2002.00294609, -0.00078922, -2423.10919662, -0.06677248, -242.31091966, -0.16677248, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.25, 28399578.10402948, 11833157.54334562, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 447.29997154, 0.0010177, 537.66321353, 0.0324567, 53.76632135, 0.0882737, -447.29997154, -0.0010177, -537.66321353, -0.0324567, -53.76632135, -0.0882737, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 447.29997154, 0.0010177, 537.66321353, 0.0324567, 53.76632135, 0.0882737, -447.29997154, -0.0010177, -537.66321353, -0.0324567, -53.76632135, -0.0882737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.16, 28564195.98273878, 11901748.32614116, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 343.6139639, 0.00122518, 413.30014861, 0.03836151, 41.33001486, 0.10842188, -343.6139639, -0.00122518, -413.30014861, -0.03836151, -41.33001486, -0.10842188, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 322.61776689, 0.00122518, 388.04584507, 0.03836151, 38.80458451, 0.10842188, -322.61776689, -0.00122518, -388.04584507, -0.03836151, -38.80458451, -0.10842188, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 4.5, 13.5, 0.0)
    ops.node(121020, 4.5, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.25, 29334359.91789567, 12222649.96578986, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 547.99628209, 0.00101257, 658.0854788, 0.03991088, 65.80854788, 0.10849838, -547.99628209, -0.00101257, -658.0854788, -0.03991088, -65.80854788, -0.10849838, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 547.99628209, 0.00101257, 658.0854788, 0.03991088, 65.80854788, 0.10849838, -547.99628209, -0.00101257, -658.0854788, -0.03991088, -65.80854788, -0.10849838, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 9.0, 13.5, 0.0)
    ops.node(121021, 9.0, 13.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.25, 29985885.61885705, 12494119.0078571, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 553.6616378, 0.00098381, 665.64250394, 0.04845597, 66.56425039, 0.14005233, -553.6616378, -0.00098381, -665.64250394, -0.04845597, -66.56425039, -0.14005233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 499.43365015, 0.00098381, 600.44663156, 0.04845597, 60.04466316, 0.14005233, -499.43365015, -0.00098381, -600.44663156, -0.04845597, -60.04466316, -0.14005233, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 12.0, 13.5, 0.0)
    ops.node(121022, 12.0, 13.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.25, 28869664.30177101, 12029026.79240459, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 562.07685323, 0.00099867, 676.75015416, 0.04847254, 67.67501542, 0.13559349, -562.07685323, -0.00099867, -676.75015416, -0.04847254, -67.67501542, -0.13559349, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 505.13927476, 0.00099867, 608.1963349, 0.04847254, 60.81963349, 0.13559349, -505.13927476, -0.00099867, -608.1963349, -0.04847254, -60.81963349, -0.13559349, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 16.5, 13.5, 0.0)
    ops.node(121023, 16.5, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.25, 28946368.05670452, 12060986.69029355, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 541.59425071, 0.0009871, 650.63556597, 0.04005376, 65.0635566, 0.10722084, -541.59425071, -0.0009871, -650.63556597, -0.04005376, -65.0635566, -0.10722084, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 541.59425071, 0.0009871, 650.63556597, 0.04005376, 65.0635566, 0.10722084, -541.59425071, -0.0009871, -650.63556597, -0.04005376, -65.0635566, -0.10722084, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.16, 27886354.61364824, 11619314.42235343, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 339.07036506, 0.00124221, 407.99890176, 0.03890219, 40.79989018, 0.10623739, -339.07036506, -0.00124221, -407.99890176, -0.03890219, -40.79989018, -0.10623739, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 318.49649693, 0.00124221, 383.24263737, 0.03890219, 38.32426374, 0.10623739, -318.49649693, -0.00124221, -383.24263737, -0.03890219, -38.32426374, -0.10623739, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.375)
    ops.node(122001, 0.0, 0.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.2025, 29276942.8222922, 12198726.17595509, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 295.48885918, 0.0009709, 357.32392475, 0.0379261, 35.73239248, 0.11640148, -295.48885918, -0.0009709, -357.32392475, -0.0379261, -35.73239248, -0.11640148, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 273.07457334, 0.0009709, 330.21914453, 0.0379261, 33.02191445, 0.11640148, -273.07457334, -0.0009709, -330.21914453, -0.0379261, -33.02191445, -0.11640148, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.5, 0.0, 3.425)
    ops.node(122002, 4.5, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.25, 29983777.21754815, 12493240.50731173, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 493.31159934, 0.00093737, 594.20854613, 0.03587223, 59.42085461, 0.10355809, -493.31159934, -0.00093737, -594.20854613, -0.03587223, -59.42085461, -0.10355809, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 493.31159934, 0.00093737, 594.20854613, 0.03587223, 59.42085461, 0.10355809, -493.31159934, -0.00093737, -594.20854613, -0.03587223, -59.42085461, -0.10355809, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.5, 0.0, 3.425)
    ops.node(122005, 16.5, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.25, 28324076.02951979, 11801698.34563325, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 506.29921735, 0.00095908, 611.29616289, 0.03609901, 61.12961629, 0.09946553, -506.29921735, -0.00095908, -611.29616289, -0.03609901, -61.12961629, -0.09946553, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 506.29921735, 0.00095908, 611.29616289, 0.03609901, 61.12961629, 0.09946553, -506.29921735, -0.00095908, -611.29616289, -0.03609901, -61.12961629, -0.09946553, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 21.0, 0.0, 3.375)
    ops.node(122006, 21.0, 0.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.2025, 26719602.6483393, 11133167.77014138, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 291.24013379, 0.00102344, 353.36000659, 0.03684622, 35.33600066, 0.10840928, -291.24013379, -0.00102344, -353.36000659, -0.03684622, -35.33600066, -0.10840928, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 269.01391836, 0.00102344, 326.39306516, 0.03684622, 32.63930652, 0.10840928, -269.01391836, -0.00102344, -326.39306516, -0.03684622, -32.63930652, -0.10840928, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.375)
    ops.node(122007, 0.0, 4.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.25, 28313317.32499262, 11797215.55208026, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 381.24835917, 0.00093899, 460.33939161, 0.0350862, 46.03393916, 0.09851237, -381.24835917, -0.00093899, -460.33939161, -0.0350862, -46.03393916, -0.09851237, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 431.97356624, 0.00093899, 521.58768395, 0.0350862, 52.1587684, 0.09851237, -431.97356624, -0.00093899, -521.58768395, -0.0350862, -52.1587684, -0.09851237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.5, 4.5, 3.425)
    ops.node(122008, 4.5, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.5625, 29408319.40775915, 12253466.41989965, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 915.5290218, 0.00070509, 1108.25098374, 0.03644258, 110.82509837, 0.11110536, -915.5290218, -0.00070509, -1108.25098374, -0.03644258, -110.82509837, -0.11110536, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 1165.275229, 0.00070509, 1410.56961398, 0.03644258, 141.0569614, 0.11110536, -1165.275229, -0.00070509, -1410.56961398, -0.03644258, -141.0569614, -0.11110536, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.0, 4.5, 3.375)
    ops.node(122009, 9.0, 4.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.3025, 28869719.10746099, 12029049.62810875, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 671.21608473, 0.00087705, 810.09182915, 0.03835582, 81.00918291, 0.11138949, -671.21608473, -0.00087705, -810.09182915, -0.03835582, -81.00918291, -0.11138949, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 583.02007785, 0.00087705, 703.64791912, 0.03835582, 70.36479191, 0.11138949, -583.02007785, -0.00087705, -703.64791912, -0.03835582, -70.36479191, -0.11138949, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.0, 4.5, 3.375)
    ops.node(122010, 12.0, 4.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.3025, 30144443.78081202, 12560184.90867168, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 685.47835606, 0.00086575, 825.62082172, 0.03738302, 82.56208217, 0.11393118, -685.47835606, -0.00086575, -825.62082172, -0.03738302, -82.56208217, -0.11393118, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 594.94500134, 0.00086575, 716.578396, 0.03738302, 71.6578396, 0.11393118, -594.94500134, -0.00086575, -716.578396, -0.03738302, -71.6578396, -0.11393118, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 16.5, 4.5, 3.425)
    ops.node(122011, 16.5, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.5625, 28061049.99688608, 11692104.1653692, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 917.36766161, 0.00072344, 1113.0974694, 0.03683909, 111.30974694, 0.10880582, -917.36766161, -0.00072344, -1113.0974694, -0.03683909, -111.30974694, -0.10880582, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 1171.06224001, 0.00072344, 1420.92039039, 0.03683909, 142.09203904, 0.10880582, -1171.06224001, -0.00072344, -1420.92039039, -0.03683909, -142.09203904, -0.10880582, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.375)
    ops.node(122012, 21.0, 4.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.25, 30221821.11777773, 12592425.46574072, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 387.80761776, 0.00090716, 466.94217736, 0.03451874, 46.69421774, 0.10284062, -387.80761776, -0.00090716, -466.94217736, -0.03451874, -46.69421774, -0.10284062, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 439.71829713, 0.00090716, 529.44555415, 0.03451874, 52.94455542, 0.10284062, -439.71829713, -0.00090716, -529.44555415, -0.03451874, -52.94455542, -0.10284062, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.375)
    ops.node(122013, 0.0, 9.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.25, 29278846.50758622, 12199519.37816093, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 386.02766064, 0.0009191, 465.53431315, 0.03524344, 46.55343131, 0.10127376, -386.02766064, -0.0009191, -465.53431315, -0.03524344, -46.55343131, -0.10127376, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 438.10970335, 0.0009191, 528.34322673, 0.03524344, 52.83432267, 0.10127376, -438.10970335, -0.0009191, -528.34322673, -0.03524344, -52.83432267, -0.10127376, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.5, 9.0, 3.425)
    ops.node(122014, 4.5, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.5625, 30381501.89240102, 12658959.12183376, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 965.07735425, 0.00069794, 1165.78495989, 0.03575544, 116.57849599, 0.11210603, -965.07735425, -0.00069794, -1165.78495989, -0.03575544, -116.57849599, -0.11210603, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 1132.89007061, 0.00069794, 1368.4977683, 0.03575544, 136.84977683, 0.11210603, -1132.89007061, -0.00069794, -1368.4977683, -0.03575544, -136.84977683, -0.11210603, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 9.0, 3.375)
    ops.node(122015, 9.0, 9.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.3025, 30403263.32896081, 12668026.38706701, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 691.46012072, 0.00085335, 832.33943974, 0.04423591, 83.23394397, 0.13474508, -691.46012072, -0.00085335, -832.33943974, -0.04423591, -83.23394397, -0.13474508, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 598.95891214, 0.00085335, 720.99186984, 0.04423591, 72.09918698, 0.13474508, -598.95891214, -0.00085335, -720.99186984, -0.04423591, -72.09918698, -0.13474508, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.0, 9.0, 3.375)
    ops.node(122016, 12.0, 9.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.3025, 28732234.16407426, 11971764.23503094, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 687.03039024, 0.00087692, 829.23631285, 0.04371178, 82.92363128, 0.12880489, -687.03039024, -0.00087692, -829.23631285, -0.04371178, -82.92363128, -0.12880489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 594.29013157, 0.00087692, 717.30008521, 0.04371178, 71.73000852, 0.12880489, -594.29013157, -0.00087692, -717.30008521, -0.04371178, -71.73000852, -0.12880489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 16.5, 9.0, 3.425)
    ops.node(122017, 16.5, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.5625, 29083049.60271313, 12117937.3344638, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 962.52804909, 0.00070484, 1165.87509589, 0.03673451, 116.58750959, 0.11078683, -962.52804909, -0.00070484, -1165.87509589, -0.03673451, -116.58750959, -0.11078683, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 1133.61783319, 0.00070484, 1373.109907, 0.03673451, 137.3109907, 0.11078683, -1133.61783319, -0.00070484, -1373.109907, -0.03673451, -137.3109907, -0.11078683, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.375)
    ops.node(122018, 21.0, 9.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.25, 27547377.0063777, 11478073.75265738, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 379.20504811, 0.00094309, 458.18756549, 0.03453551, 45.81875655, 0.09569321, -379.20504811, -0.00094309, -458.18756549, -0.03453551, -45.81875655, -0.09569321, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 430.35176056, 0.00094309, 519.98734315, 0.03453551, 51.99873431, 0.09569321, -430.35176056, -0.00094309, -519.98734315, -0.03453551, -51.99873431, -0.09569321, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.375)
    ops.node(122019, 0.0, 13.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.16, 28448725.93587481, 11853635.8066145, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 314.27532252, 0.00114814, 379.68546707, 0.04161229, 37.96854671, 0.12081942, -314.27532252, -0.00114814, -379.68546707, -0.04161229, -37.96854671, -0.12081942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 294.94454434, 0.00114814, 356.33137269, 0.04161229, 35.63313727, 0.12081942, -294.94454434, -0.00114814, -356.33137269, -0.04161229, -35.63313727, -0.12081942, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 4.5, 13.5, 3.425)
    ops.node(122020, 4.5, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.25, 28833605.38011491, 12014002.24171454, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 558.37405544, 0.00097612, 673.73638696, 0.04302124, 67.3736387, 0.1188589, -558.37405544, -0.00097612, -673.73638696, -0.04302124, -67.3736387, -0.1188589, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 531.85354016, 0.00097612, 641.73662628, 0.04302124, 64.17366263, 0.1188589, -531.85354016, -0.00097612, -641.73662628, -0.04302124, -64.17366263, -0.1188589, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.375)
    ops.node(122021, 9.0, 13.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.25, 28524119.93168663, 11885049.9715361, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 544.27503091, 0.00094452, 658.04766287, 0.04288881, 65.80476629, 0.12146934, -544.27503091, -0.00094452, -658.04766287, -0.04288881, -65.80476629, -0.12146934, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 436.21137908, 0.00094452, 527.39490556, 0.04288881, 52.73949056, 0.12146934, -436.21137908, -0.00094452, -527.39490556, -0.04288881, -52.73949056, -0.12146934, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.375)
    ops.node(122022, 12.0, 13.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.25, 28475381.74435409, 11864742.39348087, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 531.91920491, 0.00093886, 643.15087551, 0.04326123, 64.31508755, 0.12169586, -531.91920491, -0.00093886, -643.15087551, -0.04326123, -64.31508755, -0.12169586, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 428.19111916, 0.00093886, 517.73181084, 0.04326123, 51.77318108, 0.12169586, -428.19111916, -0.00093886, -517.73181084, -0.04326123, -51.77318108, -0.12169586, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 16.5, 13.5, 3.425)
    ops.node(122023, 16.5, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.25, 28538810.48410513, 11891171.0350438, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 548.90141466, 0.00094777, 662.54569076, 0.04318199, 66.25456908, 0.11807249, -548.90141466, -0.00094777, -662.54569076, -0.04318199, -66.25456908, -0.11807249, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 522.49816234, 0.00094777, 630.6759222, 0.04318199, 63.06759222, 0.11807249, -522.49816234, -0.00094777, -630.6759222, -0.04318199, -63.06759222, -0.11807249, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.375)
    ops.node(122024, 21.0, 13.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.16, 28523454.06782252, 11884772.52825938, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 326.76538374, 0.00112964, 394.73879127, 0.04123091, 39.47387913, 0.12068207, -326.76538374, -0.00112964, -394.73879127, -0.04123091, -39.47387913, -0.12068207, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 305.59042073, 0.00112964, 369.15903369, 0.04123091, 36.91590337, 0.12068207, -305.59042073, -0.00112964, -369.15903369, -0.04123091, -36.91590337, -0.12068207, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.175)
    ops.node(123001, 0.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.2025, 28691328.24760136, 11954720.10316724, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 243.46038437, 0.0009612, 295.68589827, 0.0399226, 29.56858983, 0.12507552, -243.46038437, -0.0009612, -295.68589827, -0.0399226, -29.56858983, -0.12507552, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 264.1181081, 0.0009612, 320.77498049, 0.0399226, 32.07749805, 0.12507552, -264.1181081, -0.0009612, -320.77498049, -0.0399226, -32.07749805, -0.12507552, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.5, 0.0, 6.225)
    ops.node(123002, 4.5, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.25, 28915980.09156365, 12048325.03815152, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 487.78169878, 0.00092682, 590.97832983, 0.03967354, 59.09783298, 0.1132693, -487.78169878, -0.00092682, -590.97832983, -0.03967354, -59.09783298, -0.1132693, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 513.68585807, 0.00092682, 622.36285457, 0.03967354, 62.23628546, 0.1132693, -513.68585807, -0.00092682, -622.36285457, -0.03967354, -62.23628546, -0.1132693, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.5, 0.0, 6.225)
    ops.node(123005, 16.5, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.25, 27723062.9021742, 11551276.20923925, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 504.84755833, 0.00096272, 612.81861716, 0.03891605, 61.28186172, 0.10998457, -504.84755833, -0.00096272, -612.81861716, -0.03891605, -61.28186172, -0.10998457, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 532.74340516, 0.00096272, 646.68051071, 0.03891605, 64.66805107, 0.10998457, -532.74340516, -0.00096272, -646.68051071, -0.03891605, -64.66805107, -0.10998457, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 21.0, 0.0, 6.175)
    ops.node(123006, 21.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.2025, 29776046.75268529, 12406686.1469522, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 251.08684577, 0.00093665, 304.2423588, 0.03862051, 30.42423588, 0.12554738, -251.08684577, -0.00093665, -304.2423588, -0.03862051, -30.42423588, -0.12554738, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 273.23992383, 0.00093665, 331.08528123, 0.03862051, 33.10852812, 0.12554738, -273.23992383, -0.00093665, -331.08528123, -0.03862051, -33.10852812, -0.12554738, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.175)
    ops.node(123007, 0.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.25, 28198780.87455999, 11749492.03106667, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 344.99793608, 0.00090267, 418.49073622, 0.03735307, 41.84907362, 0.10947436, -344.99793608, -0.00090267, -418.49073622, -0.03735307, -41.84907362, -0.10947436, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 396.32032361, 0.00090267, 480.74601805, 0.03735307, 48.07460181, 0.10947436, -396.32032361, -0.00090267, -480.74601805, -0.03735307, -48.07460181, -0.10947436, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.5, 4.5, 6.225)
    ops.node(123008, 4.5, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.5625, 28363421.26852272, 11818092.1952178, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 871.99950833, 0.00070848, 1060.37248726, 0.03817344, 106.03724873, 0.11679054, -871.99950833, -0.00070848, -1060.37248726, -0.03817344, -106.03724873, -0.11679054, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 1034.48935865, 0.00070848, 1257.96407429, 0.03817344, 125.79640743, 0.11679054, -1034.48935865, -0.00070848, -1257.96407429, -0.03817344, -125.79640743, -0.11679054, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.175)
    ops.node(123009, 9.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.3025, 28894102.54073643, 12039209.39197351, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 747.26462565, 0.00088855, 905.29685302, 0.04128567, 90.5296853, 0.12320777, -747.26462565, -0.00088855, -905.29685302, -0.04128567, -90.5296853, -0.12320777, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 654.25031297, 0.00088855, 792.61178582, 0.04128567, 79.26117858, 0.12320777, -654.25031297, -0.00088855, -792.61178582, -0.04128567, -79.26117858, -0.12320777, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.175)
    ops.node(123010, 12.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.3025, 27850484.34329462, 11604368.47637276, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 731.01882038, 0.00089611, 887.09502905, 0.04147306, 88.70950291, 0.12091605, -731.01882038, -0.00089611, -887.09502905, -0.04147306, -88.70950291, -0.12091605, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 640.31278379, 0.00089611, 777.02279572, 0.04147306, 77.70227957, 0.12091605, -640.31278379, -0.00089611, -777.02279572, -0.04147306, -77.70227957, -0.12091605, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 16.5, 4.5, 6.225)
    ops.node(123011, 16.5, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.5625, 26970645.92373956, 11237769.13489148, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 875.62555031, 0.00072104, 1067.32162001, 0.03848529, 106.732162, 0.11475666, -875.62555031, -0.00072104, -1067.32162001, -0.03848529, -106.732162, -0.11475666, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 1043.63233271, 0.00072104, 1272.10923852, 0.03848529, 127.21092385, 0.11475666, -1043.63233271, -0.00072104, -1272.10923852, -0.03848529, -127.21092385, -0.11475666, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.175)
    ops.node(123012, 21.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.25, 28354397.05412301, 11814332.10588459, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 343.25569016, 0.000908, 416.27504191, 0.03697592, 41.62750419, 0.10942833, -343.25569016, -0.000908, -416.27504191, -0.03697592, -41.62750419, -0.10942833, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 393.30339304, 0.000908, 476.96918395, 0.03697592, 47.69691839, 0.10942833, -393.30339304, -0.000908, -476.96918395, -0.03697592, -47.69691839, -0.10942833, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.175)
    ops.node(123013, 0.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.25, 29179792.43480535, 12158246.84783556, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 342.88091708, 0.00090324, 415.21872962, 0.03689919, 41.52187296, 0.11100534, -342.88091708, -0.00090324, -415.21872962, -0.03689919, -41.52187296, -0.11100534, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 391.70377051, 0.00090324, 474.34177254, 0.03689919, 47.43417725, 0.11100534, -391.70377051, -0.00090324, -474.34177254, -0.03689919, -47.43417725, -0.11100534, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.5, 9.0, 6.225)
    ops.node(123014, 4.5, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.5625, 29511899.12359496, 12296624.63483123, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 881.58997304, 0.00070055, 1069.44086344, 0.03768895, 106.94408634, 0.11793777, -881.58997304, -0.00070055, -1069.44086344, -0.03768895, -106.94408634, -0.11793777, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 1045.56787229, 0.00070055, 1268.35948947, 0.03768895, 126.83594895, 0.11793777, -1045.56787229, -0.00070055, -1268.35948947, -0.03768895, -126.83594895, -0.11793777, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.175)
    ops.node(123015, 9.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.3025, 28799120.42305537, 11999633.50960641, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 723.45487274, 0.00086319, 876.46639749, 0.0413591, 87.64663975, 0.12270027, -723.45487274, -0.00086319, -876.46639749, -0.0413591, -87.64663975, -0.12270027, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 634.28861937, 0.00086319, 768.44138057, 0.0413591, 76.84413806, 0.12270027, -634.28861937, -0.00086319, -768.44138057, -0.0413591, -76.84413806, -0.12270027, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.175)
    ops.node(123016, 12.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.3025, 28689745.98277812, 11954060.82615755, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 741.44314052, 0.00088599, 898.42788701, 0.04154158, 89.8427887, 0.12263119, -741.44314052, -0.00088599, -898.42788701, -0.04154158, -89.8427887, -0.12263119, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 649.52681733, 0.00088599, 787.05024588, 0.04154158, 78.70502459, 0.12263119, -649.52681733, -0.00088599, -787.05024588, -0.04154158, -78.70502459, -0.12263119, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 16.5, 9.0, 6.225)
    ops.node(123017, 16.5, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.5625, 29413992.17863301, 12255830.07443042, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 884.04448789, 0.00069493, 1072.65683721, 0.03730685, 107.26568372, 0.11742597, -884.04448789, -0.00069493, -1072.65683721, -0.03730685, -107.26568372, -0.11742597, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 1051.74692995, 0.00069493, 1276.13887185, 0.03730685, 127.61388718, 0.11742597, -1051.74692995, -0.00069493, -1276.13887185, -0.03730685, -127.61388718, -0.11742597, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.175)
    ops.node(123018, 21.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.25, 28682349.43846076, 11950978.93269199, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 342.65234824, 0.00089728, 415.31632683, 0.03738378, 41.53163268, 0.11051349, -342.65234824, -0.00089728, -415.31632683, -0.03738378, -41.53163268, -0.11051349, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 392.60391025, 0.00089728, 475.86078059, 0.03738378, 47.58607806, 0.11051349, -392.60391025, -0.00089728, -475.86078059, -0.03738378, -47.58607806, -0.11051349, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.175)
    ops.node(123019, 0.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.16, 29786819.70148348, 12411174.87561812, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 299.38586839, 0.00109796, 362.30931301, 0.04423447, 36.2309313, 0.13719124, -299.38586839, -0.00109796, -362.30931301, -0.04423447, -36.2309313, -0.13719124, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 280.24457901, 0.00109796, 339.14500187, 0.04423447, 33.91450019, 0.13719124, -280.24457901, -0.00109796, -339.14500187, -0.04423447, -33.91450019, -0.13719124, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 4.5, 13.5, 6.225)
    ops.node(123020, 4.5, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.25, 29619982.48268694, 12341659.36778622, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 547.90164638, 0.00094306, 662.91575172, 0.0401556, 66.29157517, 0.11507742, -547.90164638, -0.00094306, -662.91575172, -0.0401556, -66.29157517, -0.11507742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 547.90164638, 0.00094306, 662.91575172, 0.0401556, 66.29157517, 0.11507742, -547.90164638, -0.00094306, -662.91575172, -0.0401556, -66.29157517, -0.11507742, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.175)
    ops.node(123021, 9.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.25, 29462749.74273761, 12276145.72614067, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 536.23628154, 0.00091261, 649.59926036, 0.0399891, 64.95992604, 0.11667724, -536.23628154, -0.00091261, -649.59926036, -0.0399891, -64.95992604, -0.11667724, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 457.64260512, 0.00091261, 554.39049543, 0.0399891, 55.43904954, 0.11667724, -457.64260512, -0.00091261, -554.39049543, -0.0399891, -55.43904954, -0.11667724, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.175)
    ops.node(123022, 12.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.25, 28200443.98773813, 11750184.99489089, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 530.69219411, 0.00093674, 644.41898243, 0.03981437, 64.44189824, 0.11423949, -530.69219411, -0.00093674, -644.41898243, -0.03981437, -64.44189824, -0.11423949, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 452.99701355, 0.00093674, 550.07380502, 0.03981437, 55.0073805, 0.11423949, -452.99701355, -0.00093674, -550.07380502, -0.03981437, -55.0073805, -0.11423949, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 16.5, 13.5, 6.225)
    ops.node(123023, 16.5, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.25, 28979479.29863358, 12074783.04109732, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 553.47931994, 0.00093589, 670.497696, 0.04003215, 67.0497696, 0.11375228, -553.47931994, -0.00093589, -670.497696, -0.04003215, -67.0497696, -0.11375228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 553.47931994, 0.00093589, 670.497696, 0.04003215, 67.0497696, 0.11375228, -553.47931994, -0.00093589, -670.497696, -0.04003215, -67.0497696, -0.11375228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.175)
    ops.node(123024, 21.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.16, 30123186.53883194, 12551327.72451331, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 306.98643121, 0.001075, 371.22897983, 0.04367602, 37.12289798, 0.13729507, -306.98643121, -0.001075, -371.22897983, -0.04367602, -37.12289798, -0.13729507, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 286.68617097, 0.001075, 346.68051731, 0.04367602, 34.66805173, 0.13729507, -286.68617097, -0.001075, -346.68051731, -0.04367602, -34.66805173, -0.13729507, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.95)
    ops.node(124001, 0.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.2025, 28065363.77186851, 11693901.57161188, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 241.57705786, 0.00099738, 294.89795938, 0.04210596, 29.48979594, 0.13655871, -241.57705786, -0.00099738, -294.89795938, -0.04210596, -29.48979594, -0.13655871, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 221.70403053, 0.00099738, 270.63855636, 0.04210596, 27.06385564, 0.13655871, -221.70403053, -0.00099738, -270.63855636, -0.04210596, -27.06385564, -0.13655871, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.5, 0.0, 8.95)
    ops.node(124002, 4.5, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.25, 28856984.96102967, 12023743.73376236, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 325.5583098, 0.00086729, 396.27461003, 0.03957751, 39.627461, 0.12372648, -325.5583098, -0.00086729, -396.27461003, -0.03957751, -39.627461, -0.12372648, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 325.5583098, 0.00086729, 396.27461003, 0.03957751, 39.627461, 0.12372648, -325.5583098, -0.00086729, -396.27461003, -0.03957751, -39.627461, -0.12372648, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.5, 0.0, 8.95)
    ops.node(124005, 16.5, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.25, 29443011.75311004, 12267921.56379585, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 331.12920228, 0.00086179, 402.49079523, 0.03902485, 40.24907952, 0.12370875, -331.12920228, -0.00086179, -402.49079523, -0.03902485, -40.24907952, -0.12370875, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 331.12920228, 0.00086179, 402.49079523, 0.03902485, 40.24907952, 0.12370875, -331.12920228, -0.00086179, -402.49079523, -0.03902485, -40.24907952, -0.12370875, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 21.0, 0.0, 8.95)
    ops.node(124006, 21.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.2025, 30048237.24145513, 12520098.85060631, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 245.74266861, 0.00094226, 298.50950844, 0.04110209, 29.85095084, 0.13697947, -245.74266861, -0.00094226, -298.50950844, -0.04110209, -29.85095084, -0.13697947, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 225.08421915, 0.00094226, 273.41519482, 0.04110209, 27.34151948, 0.13697947, -225.08421915, -0.00094226, -273.41519482, -0.04110209, -27.34151948, -0.13697947, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 8.95)
    ops.node(124007, 0.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.25, 28586722.73181906, 11911134.47159127, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 267.54208216, 0.00085572, 325.85667671, 0.03903246, 32.58566767, 0.12291972, -267.54208216, -0.00085572, -325.85667671, -0.03903246, -32.58566767, -0.12291972, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 291.84647095, 0.00085572, 355.45855203, 0.03903246, 35.5458552, 0.12291972, -291.84647095, -0.00085572, -355.45855203, -0.03903246, -35.5458552, -0.12291972, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.5, 4.5, 8.95)
    ops.node(124008, 4.5, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.5625, 26973401.73501252, 11238917.38958855, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 973.77674762, 0.00071385, 1191.08077781, 0.04032145, 119.10807778, 0.12490859, -973.77674762, -0.00071385, -1191.08077781, -0.04032145, -119.10807778, -0.12490859, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 736.97484562, 0.00071385, 901.43513335, 0.04032145, 90.14351334, 0.12490859, -736.97484562, -0.00071385, -901.43513335, -0.04032145, -90.14351334, -0.12490859, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.0, 4.5, 8.95)
    ops.node(124009, 9.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.3025, 29795198.72432537, 12414666.13513557, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 488.08233973, 0.00082469, 592.55587215, 0.04175876, 59.25558722, 0.1358317, -488.08233973, -0.00082469, -592.55587215, -0.04175876, -59.25558722, -0.1358317, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 488.08233973, 0.00082469, 592.55587215, 0.04175876, 59.25558722, 0.1358317, -488.08233973, -0.00082469, -592.55587215, -0.04175876, -59.25558722, -0.1358317, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.0, 4.5, 8.95)
    ops.node(124010, 12.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.3025, 29650940.71432991, 12354558.6309708, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 479.95075694, 0.00081348, 582.89514473, 0.0421684, 58.28951447, 0.13609227, -479.95075694, -0.00081348, -582.89514473, -0.0421684, -58.28951447, -0.13609227, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 479.95075694, 0.00081348, 582.89514473, 0.0421684, 58.28951447, 0.13609227, -479.95075694, -0.00081348, -582.89514473, -0.0421684, -58.28951447, -0.13609227, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 16.5, 4.5, 8.95)
    ops.node(124011, 16.5, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.5625, 29400394.6115024, 12250164.42145933, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 997.81050928, 0.00068337, 1213.88811458, 0.0387332, 121.38881146, 0.12529769, -997.81050928, -0.00068337, -1213.88811458, -0.0387332, -121.38881146, -0.12529769, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 751.68548699, 0.00068337, 914.46428964, 0.0387332, 91.44642896, 0.12529769, -751.68548699, -0.00068337, -914.46428964, -0.0387332, -91.44642896, -0.12529769, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 8.95)
    ops.node(124012, 21.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.25, 28512480.08505565, 11880200.03543985, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 263.34595741, 0.0008562, 320.79900649, 0.03932967, 32.07990065, 0.12314329, -263.34595741, -0.0008562, -320.79900649, -0.03932967, -32.07990065, -0.12314329, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 286.81069364, 0.0008562, 349.38294279, 0.03932967, 34.93829428, 0.12314329, -286.81069364, -0.0008562, -349.38294279, -0.03932967, -34.93829428, -0.12314329, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.0, 8.95)
    ops.node(124013, 0.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.25, 30400488.43428635, 12666870.18095265, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 265.87530694, 0.00083475, 322.36900001, 0.03821872, 32.2369, 0.12368959, -265.87530694, -0.00083475, -322.36900001, -0.03821872, -32.2369, -0.12368959, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 289.32633081, 0.00083475, 350.80294221, 0.03821872, 35.08029422, 0.12368959, -289.32633081, -0.00083475, -350.80294221, -0.03821872, -35.08029422, -0.12368959, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.5, 9.0, 8.95)
    ops.node(124014, 4.5, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.5625, 28918156.14845604, 12049231.72852335, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 954.06491784, 0.00068759, 1162.06035114, 0.03985064, 116.20603511, 0.12607501, -954.06491784, -0.00068759, -1162.06035114, -0.03985064, -116.20603511, -0.12607501, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 727.42734865, 0.00068759, 886.01358713, 0.03985064, 88.60135871, 0.12607501, -727.42734865, -0.00068759, -886.01358713, -0.03985064, -88.60135871, -0.12607501, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 9.0, 8.95)
    ops.node(124015, 9.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.3025, 29755079.90233963, 12397949.95930818, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 481.08116116, 0.00082086, 584.00952905, 0.04138017, 58.40095291, 0.13490539, -481.08116116, -0.00082086, -584.00952905, -0.04138017, -58.40095291, -0.13490539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 481.08116116, 0.00082086, 584.00952905, 0.04138017, 58.40095291, 0.13490539, -481.08116116, -0.00082086, -584.00952905, -0.04138017, -58.40095291, -0.13490539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.0, 9.0, 8.95)
    ops.node(124016, 12.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.3025, 27717531.24046704, 11548971.3501946, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 491.17574666, 0.00084658, 598.95984239, 0.04194746, 59.89598424, 0.13293607, -491.17574666, -0.00084658, -598.95984239, -0.04194746, -59.89598424, -0.13293607, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 491.17574666, 0.00084658, 598.95984239, 0.04194746, 59.89598424, 0.13293607, -491.17574666, -0.00084658, -598.95984239, -0.04194746, -59.89598424, -0.13293607, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 16.5, 9.0, 8.95)
    ops.node(124017, 16.5, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.5625, 29294531.08320606, 12206054.61800253, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 995.77249624, 0.00069609, 1211.73364069, 0.03936078, 121.17336407, 0.12585256, -995.77249624, -0.00069609, -1211.73364069, -0.03936078, -121.17336407, -0.12585256, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 754.24862516, 0.00069609, 917.82855623, 0.03936078, 91.78285562, 0.12585256, -754.24862516, -0.00069609, -917.82855623, -0.03936078, -91.78285562, -0.12585256, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 21.0, 9.0, 8.95)
    ops.node(124018, 21.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.25, 28276579.87146988, 11781908.27977912, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 267.39957329, 0.00086949, 325.90495171, 0.03952978, 32.59049517, 0.12310427, -267.39957329, -0.00086949, -325.90495171, -0.03952978, -32.59049517, -0.12310427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 291.47061116, 0.00086949, 355.24258429, 0.03952978, 35.52425843, 0.12310427, -291.47061116, -0.00086949, -355.24258429, -0.03952978, -35.52425843, -0.12310427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 13.5, 8.95)
    ops.node(124019, 0.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.16, 29059762.37737821, 12108234.32390759, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 233.50381666, 0.00112884, 284.23418482, 0.04581268, 28.42341848, 0.14581268, -233.50381666, -0.00112884, -284.23418482, -0.04581268, -28.42341848, -0.14581268, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 233.50381666, 0.00112884, 284.23418482, 0.04581268, 28.42341848, 0.14581268, -233.50381666, -0.00112884, -284.23418482, -0.04581268, -28.42341848, -0.14581268, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 4.5, 13.5, 8.95)
    ops.node(124020, 4.5, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.25, 29008850.08368358, 12087020.86820149, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 325.48011679, 0.00085852, 396.03907597, 0.03918637, 39.6039076, 0.12347814, -325.48011679, -0.00085852, -396.03907597, -0.03918637, -39.6039076, -0.12347814, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 325.48011679, 0.00085852, 396.03907597, 0.03918637, 39.6039076, 0.12347814, -325.48011679, -0.00085852, -396.03907597, -0.03918637, -39.6039076, -0.12347814, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 8.95)
    ops.node(124021, 9.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.25, 29430899.32516948, 12262874.71882062, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 387.73094409, 0.00088533, 471.46974322, 0.04066324, 47.14697432, 0.1262239, -387.73094409, -0.00088533, -471.46974322, -0.04066324, -47.14697432, -0.1262239, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 362.45180464, 0.00088533, 440.73103236, 0.04066324, 44.07310324, 0.1262239, -362.45180464, -0.00088533, -440.73103236, -0.04066324, -44.07310324, -0.1262239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 8.95)
    ops.node(124022, 12.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.25, 30088173.06093352, 12536738.77538897, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 388.81400313, 0.00087897, 471.98006174, 0.0400336, 47.19800617, 0.12608833, -388.81400313, -0.00087897, -471.98006174, -0.0400336, -47.19800617, -0.12608833, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 363.60876182, 0.00087897, 441.38350077, 0.0400336, 44.13835008, 0.12608833, -363.60876182, -0.00087897, -441.38350077, -0.0400336, -44.13835008, -0.12608833, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 16.5, 13.5, 8.95)
    ops.node(124023, 16.5, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.25, 29910122.49124818, 12462551.03802007, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 322.48323257, 0.00084436, 391.51720782, 0.03877656, 39.15172078, 0.12385711, -322.48323257, -0.00084436, -391.51720782, -0.03877656, -39.15172078, -0.12385711, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 322.48323257, 0.00084436, 391.51720782, 0.03877656, 39.15172078, 0.12385711, -322.48323257, -0.00084436, -391.51720782, -0.03877656, -39.15172078, -0.12385711, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 21.0, 13.5, 8.95)
    ops.node(124024, 21.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.16, 28340378.52256946, 11808491.05107061, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 237.79322578, 0.00107211, 289.94127456, 0.04630445, 28.99412746, 0.14630445, -237.79322578, -0.00107211, -289.94127456, -0.04630445, -28.99412746, -0.14630445, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 237.79322578, 0.00107211, 289.94127456, 0.04630445, 28.99412746, 0.14630445, -237.79322578, -0.00107211, -289.94127456, -0.04630445, -28.99412746, -0.14630445, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(124025, 9.0, 0.0, 1.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.25, 28386603.27091398, 11827751.36288082, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 646.97729719, 0.00087351, 779.19569681, 0.07937564, 77.91956968, 0.17937564, -646.97729719, -0.00087351, -779.19569681, -0.07937564, -77.91956968, -0.17937564, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 589.79836746, 0.00087351, 710.33149371, 0.07937564, 71.03314937, 0.17937564, -589.79836746, -0.00087351, -710.33149371, -0.07937564, -71.03314937, -0.17937564, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.8)
    ops.node(121003, 9.0, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.25, 27329416.16481504, 11387256.7353396, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 456.29228788, 0.00085329, 550.50479684, 0.04670686, 55.05047968, 0.12913204, -456.29228788, -0.00085329, -550.50479684, -0.04670686, -55.05047968, -0.12913204, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 401.13171628, 0.00085329, 483.95499955, 0.04670686, 48.39549995, 0.12913204, -401.13171628, -0.00085329, -483.95499955, -0.04670686, -48.39549995, -0.12913204, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.0, 0.0, 0.0)
    ops.node(124026, 12.0, 0.0, 1.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.25, 29187082.31193115, 12161284.29663798, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 651.39971838, 0.0008561, 783.89275653, 0.07959999, 78.38927565, 0.17959999, -651.39971838, -0.0008561, -783.89275653, -0.07959999, -78.38927565, -0.17959999, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 593.71495168, 0.0008561, 714.47505568, 0.07959999, 71.44750557, 0.17959999, -593.71495168, -0.0008561, -714.47505568, -0.07959999, -71.44750557, -0.17959999, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.8)
    ops.node(121004, 12.0, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.25, 28657095.79237412, 11940456.58015588, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 455.44865946, 0.0008332, 548.94412065, 0.04674462, 54.89441206, 0.13512724, -455.44865946, -0.0008332, -548.94412065, -0.04674462, -54.89441206, -0.13512724, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 401.49565959, 0.0008332, 483.9155352, 0.04674462, 48.39155352, 0.13512724, -401.49565959, -0.0008332, -483.9155352, -0.04674462, -48.39155352, -0.13512724, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.375)
    ops.node(124027, 9.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.25, 28715545.48534923, 11964810.61889551, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 541.62842075, 0.00082222, 654.57548604, 0.08830836, 65.4575486, 0.18830836, -541.62842075, -0.00082222, -654.57548604, -0.08830836, -65.4575486, -0.18830836, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 434.48130307, 0.00082222, 525.08472458, 0.08070754, 52.50847246, 0.18070754, -434.48130307, -0.00082222, -525.08472458, -0.08070754, -52.50847246, -0.18070754, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.825)
    ops.node(122003, 9.0, 0.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.25, 29505996.50175001, 12294165.20906251, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 536.93818345, 0.00081959, 648.7405179, 0.08208358, 64.87405179, 0.18208358, -536.93818345, -0.00081959, -648.7405179, -0.08208358, -64.87405179, -0.18208358, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 430.49750562, 0.00081959, 520.13655083, 0.08208358, 52.01365508, 0.18208358, -430.49750562, -0.00081959, -520.13655083, -0.08208358, -52.01365508, -0.18208358, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.375)
    ops.node(124028, 12.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.25, 28576250.54640857, 11906771.06100357, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 540.71008989, 0.00082207, 653.59096449, 0.0886335, 65.35909645, 0.1886335, -540.71008989, -0.00082207, -653.59096449, -0.0886335, -65.35909645, -0.1886335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 433.54354832, 0.00082207, 524.05189248, 0.08100441, 52.40518925, 0.18100441, -433.54354832, -0.00082207, -524.05189248, -0.08100441, -52.40518925, -0.18100441, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.825)
    ops.node(122004, 12.0, 0.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.25, 29735496.10630044, 12389790.04429185, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 531.25251301, 0.00081368, 641.59535612, 0.08229988, 64.15953561, 0.18229988, -531.25251301, -0.00081368, -641.59535612, -0.08229988, -64.15953561, -0.18229988, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 427.05571618, 0.00081368, 515.75655192, 0.08229988, 51.57565519, 0.18229988, -427.05571618, -0.00081368, -515.75655192, -0.08229988, -51.57565519, -0.18229988, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.175)
    ops.node(124029, 9.0, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.25, 28898462.86144735, 12041026.19226973, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 480.06465561, 0.00081837, 582.18765167, 0.06612673, 58.21876517, 0.16612673, -480.06465561, -0.00081837, -582.18765167, -0.06612673, -58.21876517, -0.16612673, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 428.41448909, 0.00081837, 519.55006983, 0.06612673, 51.95500698, 0.16612673, -428.41448909, -0.00081837, -519.55006983, -0.06612673, -51.95500698, -0.16612673, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.55)
    ops.node(123003, 9.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.25, 28211120.30226747, 11754633.45927811, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 320.33192015, 0.00078538, 389.41924247, 0.05250993, 38.94192425, 0.15250993, -320.33192015, -0.00078538, -389.41924247, -0.05250993, -38.94192425, -0.15250993, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 294.97297914, 0.00078538, 358.59103279, 0.05250993, 35.85910328, 0.15250993, -294.97297914, -0.00078538, -358.59103279, -0.05250993, -35.85910328, -0.15250993, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.175)
    ops.node(124030, 12.0, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.25, 29228268.39425199, 12178445.16427167, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 472.11713636, 0.00081453, 572.1787114, 0.06658804, 57.21787114, 0.16658804, -472.11713636, -0.00081453, -572.1787114, -0.06658804, -57.21787114, -0.16658804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 422.49153821, 0.00081453, 512.03535159, 0.06658804, 51.20353516, 0.16658804, -422.49153821, -0.00081453, -512.03535159, -0.06658804, -51.20353516, -0.16658804, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.55)
    ops.node(123004, 12.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.25, 27894563.40986128, 11622734.75410887, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 311.37402531, 0.00078056, 378.7407875, 0.05252481, 37.87407875, 0.15252481, -311.37402531, -0.00078056, -378.7407875, -0.05252481, -37.87407875, -0.15252481, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 287.2188167, 0.00078056, 349.35952257, 0.05252481, 34.93595226, 0.15252481, -287.2188167, -0.00078056, -349.35952257, -0.05252481, -34.93595226, -0.15252481, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 8.95)
    ops.node(124031, 9.0, 0.0, 9.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.25, 29180137.97929075, 12158390.82470448, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 323.86570672, 0.00078161, 394.07072427, 0.0391157, 39.40707243, 0.1245708, -323.86570672, -0.00078161, -394.07072427, -0.0391157, -39.40707243, -0.1245708, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 323.86570672, 0.00078161, 394.07072427, 0.0391157, 39.40707243, 0.1245708, -323.86570672, -0.00078161, -394.07072427, -0.0391157, -39.40707243, -0.1245708, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 9.0, 0.0, 10.275)
    ops.node(124003, 9.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.25, 28249596.73326936, 11770665.3055289, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 344.43837166, 0.000777, 420.47951366, 0.04119643, 42.04795137, 0.12872219, -344.43837166, -0.000777, -420.47951366, -0.04119643, -42.04795137, -0.12872219, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 293.31888967, 0.000777, 358.07446041, 0.04119643, 35.80744604, 0.12872219, -293.31888967, -0.000777, -358.07446041, -0.04119643, -35.80744604, -0.12872219, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 8.95)
    ops.node(124032, 12.0, 0.0, 9.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.25, 28884505.83171959, 12035210.7632165, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 321.68187049, 0.00077415, 391.6921064, 0.03961102, 39.16921064, 0.12482348, -321.68187049, -0.00077415, -391.6921064, -0.03961102, -39.16921064, -0.12482348, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 321.68187049, 0.00077415, 391.6921064, 0.03961102, 39.16921064, 0.12482348, -321.68187049, -0.00077415, -391.6921064, -0.03961102, -39.16921064, -0.12482348, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 12.0, 0.0, 10.275)
    ops.node(124004, 12.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.25, 28326437.18227691, 11802682.15928205, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 340.12015007, 0.00078407, 415.13334109, 0.04095398, 41.51333411, 0.12852584, -340.12015007, -0.00078407, -415.13334109, -0.04095398, -41.51333411, -0.12852584, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 290.72266149, 0.00078407, 354.84128114, 0.04095398, 35.48412811, 0.12852584, -290.72266149, -0.00078407, -354.84128114, -0.04095398, -35.48412811, -0.12852584, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
