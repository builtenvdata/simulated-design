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
    ops.uniaxialMaterial('Hysteretic', 20001, 340.76981171, 0.00107881, 411.26793358, 0.03676877, 41.12679336, 0.10454644, -340.76981171, -0.00107881, -411.26793358, -0.03676877, -41.12679336, -0.10454644, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 340.76981171, 0.00107881, 411.26793358, 0.03676877, 41.12679336, 0.10454644, -340.76981171, -0.00107881, -411.26793358, -0.03676877, -41.12679336, -0.10454644, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.3025, 30146450.7232196, 12561021.13467483, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 648.96351824, 0.00089198, 780.26351216, 0.04300035, 78.02635122, 0.12839165, -648.96351824, -0.00089198, -780.26351216, -0.04300035, -78.02635122, -0.12839165, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 679.74543129, 0.00089198, 817.27330225, 0.04300035, 81.72733022, 0.12839165, -679.74543129, -0.00089198, -817.27330225, -0.04300035, -81.72733022, -0.12839165, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.3025, 28459127.10995806, 11857969.62914919, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 644.2219384, 0.000925, 776.25459653, 0.04244525, 77.62545965, 0.12164218, -644.2219384, -0.000925, -776.25459653, -0.04244525, -77.62545965, -0.12164218, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 674.85565756, 0.000925, 813.16666657, 0.04244525, 81.31666666, 0.12164218, -674.85565756, -0.000925, -813.16666657, -0.04244525, -81.31666666, -0.12164218, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 20006, 341.87153942, 0.00104729, 412.6141258, 0.03657443, 41.26141258, 0.10421093, -341.87153942, -0.00104729, -412.6141258, -0.03657443, -41.26141258, -0.10421093, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 341.87153942, 0.00104729, 412.6141258, 0.03657443, 41.26141258, 0.10421093, -341.87153942, -0.00104729, -412.6141258, -0.03657443, -41.26141258, -0.10421093, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.5, 0.0)
    ops.node(121007, 0.0, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.3025, 28014913.05918365, 11672880.44132652, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 705.6980955, 0.00092961, 850.62303534, 0.04292772, 85.06230353, 0.12027643, -705.6980955, -0.00092961, -850.62303534, -0.04292772, -85.06230353, -0.12027643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 705.6980955, 0.00092961, 850.62303534, 0.04292772, 85.06230353, 0.12027643, -705.6980955, -0.00092961, -850.62303534, -0.04292772, -85.06230353, -0.12027643, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 20008, 1955.99191636, 0.0007867, 2363.76598722, 0.06638804, 236.37659872, 0.16638804, -1955.99191636, -0.0007867, -2363.76598722, -0.06638804, -236.37659872, -0.16638804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 2048.81325161, 0.0007867, 2475.93818656, 0.06638804, 247.59381866, 0.16638804, -2048.81325161, -0.0007867, -2475.93818656, -0.06638804, -247.59381866, -0.16638804, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.0, 4.5, 0.0)
    ops.node(121009, 9.0, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.4225, 29357638.77075427, 12232349.48781428, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 1276.71316763, 0.00082802, 1539.60761476, 0.0632983, 153.96076148, 0.1632983, -1276.71316763, -0.00082802, -1539.60761476, -0.0632983, -153.96076148, -0.1632983, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 1276.71316763, 0.00082802, 1539.60761476, 0.0632983, 153.96076148, 0.1632983, -1276.71316763, -0.00082802, -1539.60761476, -0.0632983, -153.96076148, -0.1632983, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.0, 4.5, 0.0)
    ops.node(121010, 12.0, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.4225, 28988809.38776533, 12078670.57823556, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 1272.24036593, 0.00083691, 1535.0344041, 0.06384858, 153.50344041, 0.16384858, -1272.24036593, -0.00083691, -1535.0344041, -0.06384858, -153.50344041, -0.16384858, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 1272.24036593, 0.00083691, 1535.0344041, 0.06384858, 153.50344041, 0.16384858, -1272.24036593, -0.00083691, -1535.0344041, -0.06384858, -153.50344041, -0.16384858, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 20011, 1936.66971042, 0.00078436, 2342.82600061, 0.06606955, 234.28260006, 0.16606955, -1936.66971042, -0.00078436, -2342.82600061, -0.06606955, -234.28260006, -0.16606955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 2029.67358198, 0.00078436, 2455.33454416, 0.06606955, 245.53345442, 0.16606955, -2029.67358198, -0.00078436, -2455.33454416, -0.06606955, -245.53345442, -0.16606955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 21.0, 4.5, 0.0)
    ops.node(121012, 21.0, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.3025, 30379169.23356236, 12657987.18065098, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 720.67460865, 0.00092085, 866.12982781, 0.0440543, 86.61298278, 0.13019136, -720.67460865, -0.00092085, -866.12982781, -0.0440543, -86.61298278, -0.13019136, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 720.67460865, 0.00092085, 866.12982781, 0.0440543, 86.61298278, 0.13019136, -720.67460865, -0.00092085, -866.12982781, -0.0440543, -86.61298278, -0.13019136, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.3025, 28963055.11222184, 12067939.63009243, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 646.60576753, 0.00090704, 778.75739848, 0.04286666, 77.87573985, 0.1241342, -646.60576753, -0.00090704, -778.75739848, -0.04286666, -77.87573985, -0.1241342, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 677.69039157, 0.00090704, 816.19501839, 0.04286666, 81.61950184, 0.1241342, -677.69039157, -0.00090704, -816.19501839, -0.04286666, -81.61950184, -0.1241342, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 20014, 1913.20439397, 0.00075209, 2308.92811125, 0.06700175, 230.89281112, 0.16700175, -1913.20439397, -0.00075209, -2308.92811125, -0.06700175, -230.89281112, -0.16700175, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 2003.90762922, 0.00075209, 2418.39223872, 0.06700175, 241.83922387, 0.16700175, -2003.90762922, -0.00075209, -2418.39223872, -0.06700175, -241.83922387, -0.16700175, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 9.0, 0.0)
    ops.node(121015, 9.0, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.4225, 28999093.56691035, 12082955.65287931, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 1265.39822778, 0.00083581, 1526.77366645, 0.06370148, 152.67736665, 0.16370148, -1265.39822778, -0.00083581, -1526.77366645, -0.06370148, -152.67736665, -0.16370148, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 1265.39822778, 0.00083581, 1526.77366645, 0.06370148, 152.67736665, 0.16370148, -1265.39822778, -0.00083581, -1526.77366645, -0.06370148, -152.67736665, -0.16370148, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.0, 9.0, 0.0)
    ops.node(121016, 12.0, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.4225, 28951009.78483889, 12062920.74368287, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 1258.35550504, 0.00082593, 1518.37612539, 0.06345027, 151.83761254, 0.16345027, -1258.35550504, -0.00082593, -1518.37612539, -0.06345027, -151.83761254, -0.16345027, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 1258.35550504, 0.00082593, 1518.37612539, 0.06345027, 151.83761254, 0.16345027, -1258.35550504, -0.00082593, -1518.37612539, -0.06345027, -151.83761254, -0.16345027, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 20017, 1958.21104577, 0.00078963, 2369.76534445, 0.06662391, 236.97653445, 0.16662391, -1958.21104577, -0.00078963, -2369.76534445, -0.06662391, -236.97653445, -0.16662391, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 2053.56231822, 0.00078963, 2485.15645179, 0.06662391, 248.51564518, 0.16662391, -2053.56231822, -0.00078963, -2485.15645179, -0.06662391, -248.51564518, -0.16662391, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.3025, 28399578.10402948, 11833157.54334562, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 640.65150111, 0.00095199, 772.02990825, 0.042763, 77.20299082, 0.12183167, -640.65150111, -0.00095199, -772.02990825, -0.042763, -77.20299082, -0.12183167, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 670.10170896, 0.00095199, 807.51947039, 0.042763, 80.75194704, 0.12183167, -670.10170896, -0.00095199, -807.51947039, -0.042763, -80.75194704, -0.12183167, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.2025, 28564195.98273878, 11901748.32614116, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 401.24179808, 0.00107571, 484.00463594, 0.03703188, 48.40046359, 0.10584132, -401.24179808, -0.00107571, -484.00463594, -0.03703188, -48.40046359, -0.10584132, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 377.3689966, 0.00107571, 455.20766951, 0.03703188, 45.52076695, 0.10584132, -377.3689966, -0.00107571, -455.20766951, -0.03703188, -45.52076695, -0.10584132, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.3025, 29334359.91789567, 12222649.96578986, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 721.58975071, 0.00093847, 868.51951009, 0.04376558, 86.85195101, 0.12599203, -721.58975071, -0.00093847, -868.51951009, -0.04376558, -86.85195101, -0.12599203, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 721.58975071, 0.00093847, 868.51951009, 0.04376558, 86.85195101, 0.12599203, -721.58975071, -0.00093847, -868.51951009, -0.04376558, -86.85195101, -0.12599203, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 9.0, 13.5, 0.0)
    ops.node(121021, 9.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.3025, 29985885.61885705, 12494119.0078571, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 927.18664249, 0.0009393, 1116.64007876, 0.05648547, 111.66400788, 0.15648547, -927.18664249, -0.0009393, -1116.64007876, -0.05648547, -111.66400788, -0.15648547, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 863.84536274, 0.0009393, 1040.35618039, 0.05648547, 104.03561804, 0.15648547, -863.84536274, -0.0009393, -1040.35618039, -0.05648547, -104.03561804, -0.15648547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 12.0, 13.5, 0.0)
    ops.node(121022, 12.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.3025, 28869664.30177101, 12029026.79240459, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 941.46077128, 0.0009536, 1135.75679269, 0.05670533, 113.57567927, 0.15670533, -941.46077128, -0.0009536, -1135.75679269, -0.05670533, -113.57567927, -0.15670533, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 875.27747329, 0.0009536, 1055.91477214, 0.05670533, 105.59147721, 0.15670533, -875.27747329, -0.0009536, -1055.91477214, -0.05670533, -105.59147721, -0.15670533, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.3025, 28946368.05670452, 12060986.69029355, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 712.16854073, 0.00091604, 857.58217667, 0.04399816, 85.75821767, 0.12476906, -712.16854073, -0.00091604, -857.58217667, -0.04399816, -85.75821767, -0.12476906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 712.16854073, 0.00091604, 857.58217667, 0.04399816, 85.75821767, 0.12476906, -712.16854073, -0.00091604, -857.58217667, -0.04399816, -85.75821767, -0.12476906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.2025, 27886354.61364824, 11619314.42235343, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 396.35142351, 0.00108859, 478.41219963, 0.03768944, 47.84121996, 0.10429642, -396.35142351, -0.00108859, -478.41219963, -0.03768944, -47.84121996, -0.10429642, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 372.90982379, 0.00108859, 450.11724061, 0.03768944, 45.01172406, 0.10429642, -372.90982379, -0.00108859, -450.11724061, -0.03768944, -45.01172406, -0.10429642, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 21001, 325.68961914, 0.00098614, 393.80735192, 0.03883706, 39.38073519, 0.11709147, -325.68961914, -0.00098614, -393.80735192, -0.03883706, -39.38073519, -0.11709147, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 325.68961914, 0.00098614, 393.80735192, 0.03883706, 39.38073519, 0.11709147, -325.68961914, -0.00098614, -393.80735192, -0.03883706, -39.38073519, -0.11709147, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.3025, 29983777.21754815, 12493240.50731173, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 558.60505938, 0.00085956, 673.93019558, 0.03760026, 67.39301956, 0.11691103, -558.60505938, -0.00085956, -673.93019558, -0.03760026, -67.39301956, -0.11691103, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 558.60505938, 0.00085956, 673.93019558, 0.03760026, 67.39301956, 0.11691103, -558.60505938, -0.00085956, -673.93019558, -0.03760026, -67.39301956, -0.11691103, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.3025, 28324076.02951979, 11801698.34563325, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 571.9744758, 0.00088042, 691.9238384, 0.03803099, 69.19238384, 0.11302195, -571.9744758, -0.00088042, -691.9238384, -0.03803099, -69.19238384, -0.11302195, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 571.9744758, 0.00088042, 691.9238384, 0.03803099, 69.19238384, 0.11302195, -571.9744758, -0.00088042, -691.9238384, -0.03803099, -69.19238384, -0.11302195, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 21006, 320.71364269, 0.00104012, 389.07013329, 0.03771174, 38.90701333, 0.10900166, -320.71364269, -0.00104012, -389.07013329, -0.03771174, -38.90701333, -0.10900166, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 320.71364269, 0.00104012, 389.07013329, 0.03771174, 38.90701333, 0.10900166, -320.71364269, -0.00104012, -389.07013329, -0.03771174, -38.90701333, -0.10900166, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.425)
    ops.node(122007, 0.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.3025, 28313317.32499262, 11797215.55208026, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 560.18581898, 0.00087921, 677.66354893, 0.03846439, 67.76635489, 0.11339534, -560.18581898, -0.00087921, -677.66354893, -0.03846439, -67.76635489, -0.11339534, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 560.18581898, 0.00087921, 677.66354893, 0.03846439, 67.76635489, 0.11339534, -560.18581898, -0.00087921, -677.66354893, -0.03846439, -67.76635489, -0.11339534, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 21008, 1002.54212665, 0.00070553, 1213.45084762, 0.03638296, 121.34508476, 0.11080808, -1002.54212665, -0.00070553, -1213.45084762, -0.03638296, -121.34508476, -0.11080808, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 1085.87273969, 0.00070553, 1314.3120487, 0.03638296, 131.43120487, 0.11080808, -1085.87273969, -0.00070553, -1314.3120487, -0.03638296, -131.43120487, -0.11080808, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.0, 4.5, 3.425)
    ops.node(122009, 9.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.4225, 28869719.10746099, 12029049.62810875, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 1109.69998691, 0.00079134, 1343.13760655, 0.05360218, 134.31376066, 0.15194395, -1109.69998691, -0.00079134, -1343.13760655, -0.05360218, -134.31376066, -0.15194395, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 1037.07085487, 0.00079134, 1255.23013631, 0.05360218, 125.52301363, 0.15194395, -1037.07085487, -0.00079134, -1255.23013631, -0.05360218, -125.52301363, -0.15194395, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.0, 4.5, 3.425)
    ops.node(122010, 12.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.4225, 30144443.78081202, 12560184.90867168, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 1133.46565608, 0.00078316, 1368.58430635, 0.05239472, 136.85843064, 0.15239472, -1133.46565608, -0.00078316, -1368.58430635, -0.05239472, -136.85843064, -0.15239472, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 1059.11423344, 0.00078316, 1278.80991431, 0.05239472, 127.88099143, 0.15239472, -1059.11423344, -0.00078316, -1278.80991431, -0.05239472, -127.88099143, -0.15239472, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 21011, 1005.67847488, 0.00072391, 1220.09771333, 0.0367686, 122.00977133, 0.10846756, -1005.67847488, -0.00072391, -1220.09771333, -0.0367686, -122.00977133, -0.10846756, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 1090.32780217, 0.00072391, 1322.79500003, 0.0367686, 132.2795, 0.10846756, -1090.32780217, -0.00072391, -1322.79500003, -0.0367686, -132.2795, -0.10846756, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.425)
    ops.node(122012, 21.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.3025, 30221821.11777773, 12592425.46574072, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 570.12841813, 0.00085158, 687.4999324, 0.03763527, 68.74999324, 0.11747574, -570.12841813, -0.00085158, -687.4999324, -0.03763527, -68.74999324, -0.11747574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 570.12841813, 0.00085158, 687.4999324, 0.03763527, 68.74999324, 0.11747574, -570.12841813, -0.00085158, -687.4999324, -0.03763527, -68.74999324, -0.11747574, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.425)
    ops.node(122013, 0.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.3025, 29278846.50758622, 12199519.37816093, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 567.40869185, 0.00086207, 685.43049607, 0.03853609, 68.54304961, 0.11612865, -567.40869185, -0.00086207, -685.43049607, -0.03853609, -68.54304961, -0.11612865, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 567.40869185, 0.00086207, 685.43049607, 0.03853609, 68.54304961, 0.11612865, -567.40869185, -0.00086207, -685.43049607, -0.03853609, -68.54304961, -0.11612865, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 21014, 1010.20050255, 0.0006983, 1220.19420856, 0.03571146, 122.01942086, 0.11187915, -1010.20050255, -0.0006983, -1220.19420856, -0.03571146, -122.01942086, -0.11187915, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 1094.17466616, 0.0006983, 1321.62435816, 0.03571146, 132.16243582, 0.11187915, -1094.17466616, -0.0006983, -1321.62435816, -0.03571146, -132.16243582, -0.11187915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 9.0, 3.425)
    ops.node(122015, 9.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.4225, 30403263.32896081, 12668026.38706701, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 1060.82859079, 0.00076959, 1280.09812885, 0.04376075, 128.00981289, 0.12770966, -1060.82859079, -0.00076959, -1280.09812885, -0.04376075, -128.00981289, -0.12770966, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 1023.30995012, 0.00076959, 1234.82451713, 0.04376075, 123.48245171, 0.12770966, -1023.30995012, -0.00076959, -1234.82451713, -0.04376075, -123.48245171, -0.12770966, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.0, 9.0, 3.425)
    ops.node(122016, 12.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.4225, 28732234.16407426, 11971764.23503094, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 1053.56443807, 0.00078851, 1275.40746165, 0.0435776, 127.54074616, 0.12370814, -1053.56443807, -0.00078851, -1275.40746165, -0.0435776, -127.54074616, -0.12370814, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 1015.94914961, 0.00078851, 1229.87173755, 0.0435776, 122.98717375, 0.12370814, -1015.94914961, -0.00078851, -1229.87173755, -0.0435776, -122.98717375, -0.12370814, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 21017, 1008.45664526, 0.00070522, 1221.39304526, 0.03668219, 122.13930453, 0.11052935, -1008.45664526, -0.00070522, -1221.39304526, -0.03668219, -122.13930453, -0.11052935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 1094.0722486, 0.00070522, 1325.08644941, 0.03668219, 132.50864494, 0.11052935, -1094.0722486, -0.00070522, -1325.08644941, -0.03668219, -132.50864494, -0.11052935, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.425)
    ops.node(122018, 21.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.3025, 27547377.0063777, 11478073.75265738, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 557.07841082, 0.00088281, 674.504883, 0.03797497, 67.4504883, 0.11066231, -557.07841082, -0.00088281, -674.504883, -0.03797497, -67.4504883, -0.11066231, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 557.07841082, 0.00088281, 674.504883, 0.03797497, 67.4504883, 0.11066231, -557.07841082, -0.00088281, -674.504883, -0.03797497, -67.4504883, -0.11066231, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.425)
    ops.node(122019, 0.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.2025, 28448725.93587481, 11853635.8066145, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 367.16937259, 0.0010115, 444.5380403, 0.03973866, 44.45380403, 0.11584253, -367.16937259, -0.0010115, -444.5380403, -0.03973866, -44.45380403, -0.11584253, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 345.03513715, 0.0010115, 417.73975487, 0.03973866, 41.77397549, 0.11584253, -345.03513715, -0.0010115, -417.73975487, -0.03973866, -41.77397549, -0.11584253, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.3025, 28833605.38011491, 12014002.24171454, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 632.00293399, 0.00089366, 763.94311406, 0.03852103, 76.39431141, 0.11477078, -632.00293399, -0.00089366, -763.94311406, -0.03852103, -76.39431141, -0.11477078, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 602.64658447, 0.00089366, 728.45818216, 0.03852103, 72.84581822, 0.11477078, -602.64658447, -0.00089366, -728.45818216, -0.03852103, -72.84581822, -0.11477078, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.425)
    ops.node(122021, 9.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.3025, 28524119.93168663, 11885049.9715361, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 817.13376472, 0.00089645, 989.46225821, 0.05747916, 98.94622582, 0.15747916, -817.13376472, -0.00089645, -989.46225821, -0.05747916, -98.94622582, -0.15747916, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 692.72031285, 0.00089645, 838.81077329, 0.05747916, 83.88107733, 0.15747916, -692.72031285, -0.00089645, -838.81077329, -0.05747916, -83.88107733, -0.15747916, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.425)
    ops.node(122022, 12.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.3025, 28475381.74435409, 11864742.39348087, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 798.63925621, 0.00089051, 967.13878239, 0.05788707, 96.71387824, 0.15788707, -798.63925621, -0.00089051, -967.13878239, -0.05788707, -96.71387824, -0.15788707, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 678.84859654, 0.00089051, 822.07429697, 0.05788707, 82.2074297, 0.15788707, -678.84859654, -0.00089051, -822.07429697, -0.05788707, -82.2074297, -0.15788707, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.3025, 28538810.48410513, 11891171.0350438, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 620.86278123, 0.00086932, 750.79495614, 0.03874846, 75.07949561, 0.114186, -620.86278123, -0.00086932, -750.79495614, -0.03874846, -75.07949561, -0.114186, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 591.70646406, 0.00086932, 715.53689827, 0.03874846, 71.55368983, 0.114186, -591.70646406, -0.00086932, -715.53689827, -0.03874846, -71.55368983, -0.114186, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.425)
    ops.node(122024, 21.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.2025, 28523454.06782252, 11884772.52825938, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 380.12424791, 0.00100034, 460.17184284, 0.03936897, 46.01718428, 0.11566493, -380.12424791, -0.00100034, -460.17184284, -0.03936897, -46.01718428, -0.11566493, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 356.1316523, 0.00100034, 431.12682138, 0.03936897, 43.11268214, 0.11566493, -356.1316523, -0.00100034, -431.12682138, -0.03936897, -43.11268214, -0.11566493, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 22001, 294.25127172, 0.00097823, 357.34526104, 0.04089618, 35.7345261, 0.12585859, -294.25127172, -0.00097823, -357.34526104, -0.04089618, -35.7345261, -0.12585859, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 294.25127172, 0.00097823, 357.34526104, 0.04089618, 35.7345261, 0.12585859, -294.25127172, -0.00097823, -357.34526104, -0.04089618, -35.7345261, -0.12585859, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.5, 0.0, 6.225)
    ops.node(123002, 4.5, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.3025, 28915980.09156365, 12048325.03815152, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 579.57015634, 0.00085201, 703.00570466, 0.04118403, 70.30057047, 0.1263275, -579.57015634, -0.00085201, -703.00570466, -0.04118403, -70.30057047, -0.1263275, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 550.92995892, 0.00085201, 668.26578241, 0.04118403, 66.82657824, 0.1263275, -550.92995892, -0.00085201, -668.26578241, -0.04118403, -66.82657824, -0.1263275, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.5, 0.0, 6.225)
    ops.node(123005, 16.5, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.3025, 27723062.9021742, 11551276.20923925, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 599.98618318, 0.00088479, 729.28306371, 0.04050042, 72.92830637, 0.12315244, -599.98618318, -0.00088479, -729.28306371, -0.04050042, -72.92830637, -0.12315244, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 569.28116024, 0.00088479, 691.96111558, 0.04050042, 69.19611156, 0.12315244, -569.28116024, -0.00088479, -691.96111558, -0.04050042, -69.19611156, -0.12315244, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 22006, 304.21316965, 0.00095253, 368.59114318, 0.03956688, 36.85911432, 0.12632189, -304.21316965, -0.00095253, -368.59114318, -0.03956688, -36.85911432, -0.12632189, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 304.21316965, 0.00095253, 368.59114318, 0.03956688, 36.85911432, 0.12632189, -304.21316965, -0.00095253, -368.59114318, -0.03956688, -36.85911432, -0.12632189, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.225)
    ops.node(123007, 0.0, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.3025, 28198780.87455999, 11749492.03106667, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 520.59233782, 0.00085082, 632.25899383, 0.04056067, 63.22589938, 0.12411931, -520.59233782, -0.00085082, -632.25899383, -0.04056067, -63.22589938, -0.12411931, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 520.59233782, 0.00085082, 632.25899383, 0.04056067, 63.22589938, 0.12411931, -520.59233782, -0.00085082, -632.25899383, -0.04056067, -63.22589938, -0.12411931, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.5, 4.5, 6.225)
    ops.node(123008, 4.5, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.5625, 28363421.26852272, 11818092.1952178, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 1058.86314198, 0.00071653, 1287.49028113, 0.03882137, 128.74902811, 0.11723324, -1058.86314198, -0.00071653, -1287.49028113, -0.03882137, -128.74902811, -0.11723324, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 1141.54294182, 0.00071653, 1388.02210108, 0.03882137, 138.80221011, 0.11723324, -1141.54294182, -0.00071653, -1388.02210108, -0.03882137, -138.80221011, -0.11723324, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.225)
    ops.node(123009, 9.0, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.4225, 28894102.54073643, 12039209.39197351, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 1128.78823629, 0.00079839, 1370.15863534, 0.04704616, 137.01586353, 0.13501118, -1128.78823629, -0.00079839, -1370.15863534, -0.04704616, -137.01586353, -0.13501118, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 1090.97354135, 0.00079839, 1324.25797023, 0.04704616, 132.42579702, 0.13501118, -1090.97354135, -0.00079839, -1324.25797023, -0.04704616, -132.42579702, -0.13501118, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.225)
    ops.node(123010, 12.0, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.4225, 27850484.34329462, 11604368.47637276, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 1104.78854909, 0.00080356, 1343.60732105, 0.0474189, 134.3607321, 0.13336737, -1104.78854909, -0.00080356, -1343.60732105, -0.0474189, -134.3607321, -0.13336737, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 1067.83034629, 0.00080356, 1298.65997624, 0.0474189, 129.86599762, 0.13336737, -1067.83034629, -0.00080356, -1298.65997624, -0.0474189, -129.86599762, -0.13336737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 16.5, 4.5, 6.225)
    ops.node(123011, 16.5, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.5625, 26970645.92373956, 11237769.13489148, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 1065.14280092, 0.00072932, 1298.19423304, 0.03912887, 129.8194233, 0.11516481, -1065.14280092, -0.00072932, -1298.19423304, -0.03912887, -129.8194233, -0.11516481, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 1150.62987788, 0.00072932, 1402.38573696, 0.03912887, 140.2385737, 0.11516481, -1150.62987788, -0.00072932, -1402.38573696, -0.03912887, -140.2385737, -0.11516481, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.225)
    ops.node(123012, 21.0, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.3025, 28354397.05412301, 11814332.10588459, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 517.56479075, 0.00085514, 628.413706, 0.04013464, 62.8413706, 0.12402165, -517.56479075, -0.00085514, -628.413706, -0.04013464, -62.8413706, -0.12402165, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 517.56479075, 0.00085514, 628.413706, 0.04013464, 62.8413706, 0.12402165, -517.56479075, -0.00085514, -628.413706, -0.04013464, -62.8413706, -0.12402165, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.225)
    ops.node(123013, 0.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.3025, 29179792.43480535, 12158246.84783556, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 516.26600459, 0.00085036, 625.8733039, 0.03999615, 62.58733039, 0.12556841, -516.26600459, -0.00085036, -625.8733039, -0.03999615, -62.58733039, -0.12556841, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 516.26600459, 0.00085036, 625.8733039, 0.03999615, 62.58733039, 0.12556841, -516.26600459, -0.00085036, -625.8733039, -0.03999615, -62.58733039, -0.12556841, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.5, 9.0, 6.225)
    ops.node(123014, 4.5, 9.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.5625, 29511899.12359496, 12296624.63483123, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 1070.22353637, 0.0007083, 1298.191261, 0.03834497, 129.8191261, 0.11845099, -1070.22353637, -0.0007083, -1298.191261, -0.03834497, -129.8191261, -0.11845099, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 1153.63094184, 0.0007083, 1399.36523186, 0.03834497, 139.93652319, 0.11845099, -1153.63094184, -0.0007083, -1399.36523186, -0.03834497, -139.93652319, -0.11845099, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.225)
    ops.node(123015, 9.0, 9.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.4225, 28799120.42305537, 11999633.50960641, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 1050.59825927, 0.00077221, 1275.37881185, 0.03983292, 127.53788118, 0.11460066, -1050.59825927, -0.00077221, -1275.37881185, -0.03983292, -127.53788118, -0.11460066, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 978.58879276, 0.00077221, 1187.9625735, 0.03983292, 118.79625735, 0.11460066, -978.58879276, -0.00077221, -1187.9625735, -0.03983292, -118.79625735, -0.11460066, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.225)
    ops.node(123016, 12.0, 9.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.4225, 28689745.98277812, 11954060.82615755, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 1076.92576635, 0.00079141, 1307.6184888, 0.04002206, 130.76184888, 0.11461597, -1076.92576635, -0.00079141, -1307.6184888, -0.04002206, -130.76184888, -0.11461597, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 1002.73572726, 0.00079141, 1217.53589459, 0.04002206, 121.75358946, 0.11461597, -1002.73572726, -0.00079141, -1217.53589459, -0.04002206, -121.75358946, -0.11461597, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 16.5, 9.0, 6.225)
    ops.node(123017, 16.5, 9.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.5625, 29413992.17863301, 12255830.07443042, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 1074.51633859, 0.00070249, 1303.68740631, 0.03795568, 130.36874063, 0.11793065, -1074.51633859, -0.00070249, -1303.68740631, -0.03795568, -130.36874063, -0.11793065, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 1159.79983459, 0.00070249, 1407.16002529, 0.03795568, 140.71600253, 0.11793065, -1159.79983459, -0.00070249, -1407.16002529, -0.03795568, -140.71600253, -0.11793065, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.225)
    ops.node(123018, 21.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.3025, 28682349.43846076, 11950978.93269199, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 516.26382327, 0.00084541, 626.47614228, 0.04056532, 62.64761423, 0.12517409, -516.26382327, -0.00084541, -626.47614228, -0.04056532, -62.64761423, -0.12517409, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 516.26382327, 0.00084541, 626.47614228, 0.04056532, 62.64761423, 0.12517409, -516.26382327, -0.00084541, -626.47614228, -0.04056532, -62.64761423, -0.12517409, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.225)
    ops.node(123019, 0.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.2025, 29786819.70148348, 12411174.87561812, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 348.79161067, 0.00097178, 422.59285128, 0.04163218, 42.25928513, 0.12840376, -348.79161067, -0.00097178, -422.59285128, -0.04163218, -42.25928513, -0.12840376, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 326.86940438, 0.00097178, 396.03209873, 0.04163218, 39.60320987, 0.12840376, -326.86940438, -0.00097178, -396.03209873, -0.04163218, -39.60320987, -0.12840376, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 4.5, 13.5, 6.225)
    ops.node(123020, 4.5, 13.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.3025, 29619982.48268694, 12341659.36778622, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 647.73539154, 0.0008654, 784.55084032, 0.04147915, 78.45508403, 0.12792475, -647.73539154, -0.0008654, -784.55084032, -0.04147915, -78.45508403, -0.12792475, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 590.34081776, 0.0008654, 715.0333156, 0.04147915, 71.50333156, 0.12792475, -590.34081776, -0.0008654, -715.0333156, -0.04147915, -71.50333156, -0.12792475, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.225)
    ops.node(123021, 9.0, 13.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.3025, 29462749.74273761, 12276145.72614067, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 834.93838387, 0.00086793, 1012.38759081, 0.05180129, 101.23875908, 0.15180129, -834.93838387, -0.00086793, -1012.38759081, -0.05180129, -101.23875908, -0.15180129, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 683.83177054, 0.00086793, 829.1663338, 0.05180129, 82.91663338, 0.15180129, -683.83177054, -0.00086793, -829.1663338, -0.05180129, -82.91663338, -0.15180129, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.225)
    ops.node(123022, 12.0, 13.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.3025, 28200443.98773813, 11750184.99489089, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 826.51115523, 0.00088959, 1004.71004967, 0.05177717, 100.47100497, 0.15177717, -826.51115523, -0.00088959, -1004.71004967, -0.05177717, -100.47100497, -0.15177717, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 676.8594569, 0.00088959, 822.79288581, 0.05177717, 82.27928858, 0.15177717, -676.8594569, -0.00088959, -822.79288581, -0.05177717, -82.27928858, -0.15177717, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 16.5, 13.5, 6.225)
    ops.node(123023, 16.5, 13.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.3025, 28979479.29863358, 12074783.04109732, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 654.0582519, 0.00086051, 793.25973188, 0.0414057, 79.32597319, 0.12667144, -654.0582519, -0.00086051, -793.25973188, -0.0414057, -79.32597319, -0.12667144, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 594.34433038, 0.00086051, 720.8370551, 0.0414057, 72.08370551, 0.12667144, -594.34433038, -0.00086051, -720.8370551, -0.0414057, -72.08370551, -0.12667144, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.225)
    ops.node(123024, 21.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.2025, 30123186.53883194, 12551327.72451331, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 356.55963333, 0.00095534, 431.66230065, 0.04108386, 43.16623007, 0.1283618, -356.55963333, -0.00095534, -431.66230065, -0.04108386, -43.16623007, -0.1283618, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 333.48004178, 0.00095534, 403.72142161, 0.04108386, 40.37214216, 0.1283618, -333.48004178, -0.00095534, -403.72142161, -0.04108386, -40.37214216, -0.1283618, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 23001, 221.70403053, 0.00099738, 270.63855636, 0.04210596, 27.06385564, 0.13655871, -221.70403053, -0.00099738, -270.63855636, -0.04210596, -27.06385564, -0.13655871, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 241.57705786, 0.00099738, 294.89795938, 0.04210596, 29.48979594, 0.13655871, -241.57705786, -0.00099738, -294.89795938, -0.04210596, -29.48979594, -0.13655871, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.5, 0.0, 8.975)
    ops.node(124002, 4.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.3025, 28856984.96102967, 12023743.73376236, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 365.88412117, 0.00080292, 445.58050603, 0.04110371, 44.5580506, 0.136527, -365.88412117, -0.00080292, -445.58050603, -0.04110371, -44.5580506, -0.136527, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 365.88412117, 0.00080292, 445.58050603, 0.04110371, 44.5580506, 0.136527, -365.88412117, -0.00080292, -445.58050603, -0.04110371, -44.5580506, -0.136527, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.5, 0.0, 8.975)
    ops.node(124005, 16.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.3025, 29443011.75311004, 12267921.56379585, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 371.82228172, 0.00079879, 452.16307455, 0.04050989, 45.21630745, 0.13644789, -371.82228172, -0.00079879, -452.16307455, -0.04050989, -45.21630745, -0.13644789, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 371.82228172, 0.00079879, 452.16307455, 0.04050989, 45.21630745, 0.13644789, -371.82228172, -0.00079879, -452.16307455, -0.04050989, -45.21630745, -0.13644789, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.uniaxialMaterial('Hysteretic', 23006, 225.08421915, 0.00094226, 273.41519482, 0.04110209, 27.34151948, 0.13697947, -225.08421915, -0.00094226, -273.41519482, -0.04110209, -27.34151948, -0.13697947, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 245.74266861, 0.00094226, 298.50950844, 0.04110209, 29.85095084, 0.13697947, -245.74266861, -0.00094226, -298.50950844, -0.04110209, -29.85095084, -0.13697947, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 8.975)
    ops.node(124007, 0.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.3025, 28586722.73181906, 11911134.47159127, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 366.99253023, 0.0008049, 447.21991021, 0.04139858, 44.72199102, 0.13661802, -366.99253023, -0.0008049, -447.21991021, -0.04139858, -44.72199102, -0.13661802, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 366.99253023, 0.0008049, 447.21991021, 0.04139858, 44.72199102, 0.13661802, -366.99253023, -0.0008049, -447.21991021, -0.04139858, -44.72199102, -0.13661802, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.5, 4.5, 8.975)
    ops.node(124008, 4.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.5625, 26973401.73501252, 11238917.38958855, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 776.95360006, 0.00071392, 950.317137, 0.04030957, 95.0317137, 0.12484831, -776.95360006, -0.00071392, -950.317137, -0.04030957, -95.0317137, -0.12484831, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 934.84688391, 0.00071392, 1143.44153137, 0.04030957, 114.34415314, 0.12484831, -934.84688391, -0.00071392, -1143.44153137, -0.04030957, -114.34415314, -0.12484831, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.0, 4.5, 8.975)
    ops.node(124009, 9.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.4225, 29795198.72432537, 12414666.13513557, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 758.67189398, 0.00074347, 921.8409425, 0.03959019, 92.18409425, 0.12306956, -758.67189398, -0.00074347, -921.8409425, -0.03959019, -92.18409425, -0.12306956, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 689.12440259, 0.00074347, 837.33573607, 0.03959019, 83.73357361, 0.12306956, -689.12440259, -0.00074347, -837.33573607, -0.03959019, -83.73357361, -0.12306956, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.0, 4.5, 8.975)
    ops.node(124010, 12.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.4225, 29650940.71432991, 12354558.6309708, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 745.85860565, 0.00073395, 906.61314753, 0.03998854, 90.66131475, 0.12336975, -745.85860565, -0.00073395, -906.61314753, -0.03998854, -90.66131475, -0.12336975, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 677.56363759, 0.00073395, 823.59859828, 0.03998854, 82.35985983, 0.12336975, -677.56363759, -0.00073395, -823.59859828, -0.03998854, -82.35985983, -0.12336975, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 16.5, 4.5, 8.975)
    ops.node(124011, 16.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.5625, 29400394.6115024, 12250164.42145933, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 793.22425548, 0.00068344, 964.98444843, 0.03872465, 96.49844484, 0.12525197, -793.22425548, -0.00068344, -964.98444843, -0.03872465, -96.49844484, -0.12525197, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 957.33277162, 0.00068344, 1164.6280736, 0.03872465, 116.46280736, 0.12525197, -957.33277162, -0.00068344, -1164.6280736, -0.03872465, -116.46280736, -0.12525197, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 8.975)
    ops.node(124012, 21.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.3025, 28512480.08505565, 11880200.03543985, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 361.219133, 0.00080468, 440.25924617, 0.04171683, 44.02592462, 0.13686574, -361.219133, -0.00080468, -440.25924617, -0.04171683, -44.02592462, -0.13686574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 361.219133, 0.00080468, 440.25924617, 0.04171683, 44.02592462, 0.13686574, -361.219133, -0.00080468, -440.25924617, -0.04171683, -44.02592462, -0.13686574, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.3025, 30400488.43428635, 12666870.18095265, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 338.00952891, 0.00078563, 410.00680838, 0.04047518, 41.00068084, 0.1372094, -338.00952891, -0.00078563, -410.00680838, -0.04047518, -41.00068084, -0.1372094, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 391.19175667, 0.00078563, 474.5170473, 0.04047518, 47.45170473, 0.1372094, -391.19175667, -0.00078563, -474.5170473, -0.04047518, -47.45170473, -0.1372094, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.5, 9.0, 8.975)
    ops.node(124014, 4.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.5625, 28918156.14845604, 12049231.72852335, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 727.93658018, 0.00068766, 886.62033869, 0.03984133, 88.66203387, 0.12602659, -727.93658018, -0.00068766, -886.62033869, -0.03984133, -88.66203387, -0.12602659, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 954.60993313, 0.00068766, 1162.7064847, 0.03984133, 116.27064847, 0.12602659, -954.60993313, -0.00068766, -1162.7064847, -0.03984133, -116.27064847, -0.12602659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 9.0, 8.975)
    ops.node(124015, 9.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.4225, 29755079.90233963, 12397949.95930818, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 589.33621428, 0.00072732, 716.06837811, 0.03832388, 71.60683781, 0.12145402, -589.33621428, -0.00072732, -716.06837811, -0.03832388, -71.60683781, -0.12145402, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 589.33621428, 0.00072732, 716.06837811, 0.03832388, 71.60683781, 0.12145402, -589.33621428, -0.00072732, -716.06837811, -0.03832388, -71.60683781, -0.12145402, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.0, 9.0, 8.975)
    ops.node(124016, 12.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.4225, 27717531.24046704, 11548971.3501946, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 600.02146379, 0.00074931, 732.5231154, 0.03899158, 73.25231154, 0.12044627, -600.02146379, -0.00074931, -732.5231154, -0.03899158, -73.25231154, -0.12044627, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 600.02146379, 0.00074931, 732.5231154, 0.03899158, 73.25231154, 0.12044627, -600.02146379, -0.00074931, -732.5231154, -0.03899158, -73.25231154, -0.12044627, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 16.5, 9.0, 8.975)
    ops.node(124017, 16.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.5625, 29294531.08320606, 12206054.61800253, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 754.75952749, 0.00069615, 918.43687015, 0.03935198, 91.84368701, 0.12580618, -754.75952749, -0.00069615, -918.43687015, -0.03935198, -91.84368701, -0.12580618, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 996.32016405, 0.00069615, 1212.38240765, 0.03935198, 121.23824077, 0.12580618, -996.32016405, -0.00069615, -1212.38240765, -0.03935198, -121.23824077, -0.12580618, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.3025, 28276579.87146988, 11781908.27977912, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 339.63802663, 0.00081695, 414.17552972, 0.04193744, 41.41755297, 0.13685719, -339.63802663, -0.00081695, -414.17552972, -0.04193744, -41.41755297, -0.13685719, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 394.15532386, 0.00081695, 480.65727996, 0.04193744, 48.065728, 0.13685719, -394.15532386, -0.00081695, -480.65727996, -0.04193744, -48.065728, -0.13685719, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.2025, 29059762.37737821, 12108234.32390759, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 221.11810609, 0.00097642, 269.29164677, 0.04188158, 26.92916468, 0.13709871, -221.11810609, -0.00097642, -269.29164677, -0.04188158, -26.92916468, -0.13709871, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 240.7187674, 0.00097642, 293.16257464, 0.04188158, 29.31625746, 0.13709871, -240.7187674, -0.00097642, -293.16257464, -0.04188158, -29.31625746, -0.13709871, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 4.5, 13.5, 8.975)
    ops.node(124020, 4.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.3025, 29008850.08368358, 12087020.86820149, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 365.64729662, 0.00079548, 445.13051614, 0.0406928, 44.51305161, 0.13625354, -365.64729662, -0.00079548, -445.13051614, -0.0406928, -44.51305161, -0.13625354, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 365.64729662, 0.00079548, 445.13051614, 0.0406928, 44.51305161, 0.13625354, -365.64729662, -0.00079548, -445.13051614, -0.0406928, -44.51305161, -0.13625354, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 8.975)
    ops.node(124021, 9.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.3025, 29430899.32516948, 12262874.71882062, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 502.62772306, 0.00082806, 611.43686333, 0.04275061, 61.14368633, 0.13955293, -502.62772306, -0.00082806, -611.43686333, -0.04275061, -61.14368633, -0.13955293, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 445.74100743, 0.00082806, 542.23527859, 0.04275061, 54.22352786, 0.13955293, -445.74100743, -0.00082806, -542.23527859, -0.04275061, -54.22352786, -0.13955293, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 8.975)
    ops.node(124022, 12.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.3025, 30088173.06093352, 12536738.77538897, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 504.03503177, 0.00082239, 612.08450806, 0.04206877, 61.20845081, 0.13934388, -504.03503177, -0.00082239, -612.08450806, -0.04206877, -61.20845081, -0.13934388, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 447.28927518, 0.00082239, 543.17422143, 0.04206877, 54.31742214, 0.13934388, -447.28927518, -0.00082239, -543.17422143, -0.04206877, -54.31742214, -0.13934388, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 16.5, 13.5, 8.975)
    ops.node(124023, 16.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.3025, 29910122.49124818, 12462551.03802007, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 362.47157815, 0.00078273, 440.25936379, 0.0402389, 44.02593638, 0.13655825, -362.47157815, -0.00078273, -440.25936379, -0.0402389, -44.02593638, -0.13655825, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 362.47157815, 0.00078273, 440.25936379, 0.0402389, 44.02593638, 0.13655825, -362.47157815, -0.00078273, -440.25936379, -0.0402389, -44.02593638, -0.13655825, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.2025, 28340378.52256946, 11808491.05107061, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 223.20755804, 0.00093602, 272.30433641, 0.04237155, 27.23043364, 0.13704676, -223.20755804, -0.00093602, -272.30433641, -0.04237155, -27.23043364, -0.13704676, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 244.62057581, 0.00093602, 298.42736579, 0.04237155, 29.84273658, 0.13704676, -244.62057581, -0.00093602, -298.42736579, -0.04237155, -29.84273658, -0.13704676, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.3025, 28386603.27091398, 11827751.36288082, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 931.54490012, 0.00083808, 1124.31028779, 0.08978654, 112.43102878, 0.18978654, -931.54490012, -0.00083808, -1124.31028779, -0.08978654, -112.43102878, -0.18978654, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 866.41652763, 0.00083808, 1045.70484515, 0.08978654, 104.57048451, 0.18978654, -866.41652763, -0.00083808, -1045.70484515, -0.08978654, -104.57048451, -0.18978654, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.8)
    ops.node(121003, 9.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.3025, 27329416.16481504, 11387256.7353396, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 618.99253255, 0.00081561, 748.49884597, 0.05173251, 74.8498846, 0.1508644, -618.99253255, -0.00081561, -748.49884597, -0.05173251, -74.8498846, -0.1508644, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 556.7618836, 0.00081561, 673.24823069, 0.05173251, 67.32482307, 0.1508644, -556.7618836, -0.00081561, -673.24823069, -0.05173251, -67.32482307, -0.1508644, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.3025, 29187082.31193115, 12161284.29663798, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 937.7288938, 0.00082266, 1130.65313342, 0.08978092, 113.06531334, 0.18978092, -937.7288938, -0.00082266, -1130.65313342, -0.08978092, -113.06531334, -0.18978092, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 872.11299677, 0.00082266, 1051.53770884, 0.08978092, 105.15377088, 0.18978092, -872.11299677, -0.00082266, -1051.53770884, -0.08978092, -105.15377088, -0.18978092, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.8)
    ops.node(121004, 12.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.3025, 28657095.79237412, 11940456.58015588, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 618.24368221, 0.0007975, 746.60634867, 0.05151264, 74.66063487, 0.15151264, -618.24368221, -0.0007975, -746.60634867, -0.05151264, -74.66063487, -0.15151264, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 557.24611379, 0.0007975, 672.94417768, 0.05151264, 67.29441777, 0.15151264, -557.24611379, -0.0007975, -672.94417768, -0.05151264, -67.29441777, -0.15151264, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.425)
    ops.node(124027, 9.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.3025, 28715545.48534923, 11964810.61889551, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 682.02722513, 0.00078941, 825.5275347, 0.08809784, 82.55275347, 0.18809784, -682.02722513, -0.00078941, -825.5275347, -0.08809784, -82.55275347, -0.18809784, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 621.58392388, 0.00078941, 752.366805, 0.08809784, 75.2366805, 0.18809784, -621.58392388, -0.00078941, -752.366805, -0.08809784, -75.2366805, -0.18809784, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.825)
    ops.node(122003, 9.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.3025, 29505996.50175001, 12294165.20906251, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 612.84198433, 0.00078221, 741.38961226, 0.08771837, 74.13896123, 0.18771837, -612.84198433, -0.00078221, -741.38961226, -0.08771837, -74.13896123, -0.18771837, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 583.07820409, 0.00078221, 705.38268379, 0.08771837, 70.53826838, 0.18771837, -583.07820409, -0.00078221, -705.38268379, -0.08771837, -70.53826838, -0.18771837, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.425)
    ops.node(124028, 12.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.3025, 28576250.54640857, 11906771.06100357, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 680.69986873, 0.00078926, 824.09972061, 0.08845715, 82.40997206, 0.18845715, -680.69986873, -0.00078926, -824.09972061, -0.08845715, -82.40997206, -0.18845715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 620.26291612, 0.00078926, 750.93079837, 0.08845715, 75.09307984, 0.18845715, -620.26291612, -0.00078926, -750.93079837, -0.08845715, -75.09307984, -0.18845715, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.825)
    ops.node(122004, 12.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.3025, 29735496.10630044, 12389790.04429185, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 607.09055485, 0.00077666, 734.09267154, 0.0879062, 73.40926715, 0.1879062, -607.09055485, -0.00077666, -734.09267154, -0.0879062, -73.40926715, -0.1879062, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 577.91087925, 0.00077666, 698.8086668, 0.0879062, 69.88086668, 0.1879062, -577.91087925, -0.00077666, -698.8086668, -0.0879062, -69.88086668, -0.1879062, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.225)
    ops.node(124029, 9.0, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.3025, 28898462.86144735, 12041026.19226973, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 578.23746205, 0.00078156, 701.93643289, 0.07024121, 70.19364329, 0.17024121, -578.23746205, -0.00078156, -701.93643289, -0.07024121, -70.19364329, -0.17024121, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 549.27016477, 0.00078156, 666.77233049, 0.07024121, 66.67723305, 0.17024121, -549.27016477, -0.00078156, -666.77233049, -0.07024121, -66.67723305, -0.17024121, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.55)
    ops.node(123003, 9.0, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.3025, 28211120.30226747, 11754633.45927811, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 428.23382287, 0.00075637, 521.05742822, 0.04720082, 52.10574282, 0.14720082, -428.23382287, -0.00075637, -521.05742822, -0.04720082, -52.10574282, -0.14720082, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 371.13973761, 0.00075637, 451.58767677, 0.04720082, 45.15876768, 0.14720082, -371.13973761, -0.00075637, -451.58767677, -0.04720082, -45.15876768, -0.14720082, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.225)
    ops.node(124030, 12.0, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.3025, 29228268.39425199, 12178445.16427167, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 569.61285618, 0.0007775, 690.99374769, 0.0706916, 69.09937477, 0.1706916, -569.61285618, -0.0007775, -690.99374769, -0.0706916, -69.09937477, -0.1706916, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 541.68169345, 0.0007775, 657.11063111, 0.0706916, 65.71106311, 0.1706916, -541.68169345, -0.0007775, -657.11063111, -0.0706916, -65.71106311, -0.1706916, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.55)
    ops.node(123004, 12.0, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.3025, 27894563.40986128, 11622734.75410887, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 416.24952364, 0.00075137, 506.7756417, 0.04722607, 50.67756417, 0.14722607, -416.24952364, -0.00075137, -506.7756417, -0.04722607, -50.67756417, -0.14722607, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 361.69827188, 0.00075137, 440.36056121, 0.04722607, 44.03605612, 0.14722607, -361.69827188, -0.00075137, -440.36056121, -0.04722607, -44.03605612, -0.14722607, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 8.975)
    ops.node(124031, 9.0, 0.0, 9.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.3025, 29180137.97929075, 12158390.82470448, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 364.1806077, 0.00074442, 443.30813211, 0.04060238, 44.33081321, 0.13727107, -364.1806077, -0.00074442, -443.30813211, -0.04060238, -44.33081321, -0.13727107, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 364.1806077, 0.00074442, 443.30813211, 0.04060238, 44.33081321, 0.13727107, -364.1806077, -0.00074442, -443.30813211, -0.04060238, -44.33081321, -0.13727107, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 9.0, 0.0, 10.3)
    ops.node(124003, 9.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.3025, 28249596.73326936, 11770665.3055289, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 385.42759348, 0.00074152, 470.66343961, 0.0426988, 47.06634396, 0.1414023, -385.42759348, -0.00074152, -470.66343961, -0.0426988, -47.06634396, -0.1414023, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 328.97778787, 0.00074152, 401.72997422, 0.0426988, 40.17299742, 0.1414023, -328.97778787, -0.00074152, -401.72997422, -0.0426988, -40.17299742, -0.1414023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 8.975)
    ops.node(124032, 12.0, 0.0, 9.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.3025, 28884505.83171959, 12035210.7632165, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 361.53017164, 0.00073803, 440.40136742, 0.04112784, 44.04013674, 0.13756309, -361.53017164, -0.00073803, -440.40136742, -0.04112784, -44.04013674, -0.13756309, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 361.53017164, 0.00073803, 440.40136742, 0.04112784, 44.04013674, 0.13756309, -361.53017164, -0.00073803, -440.40136742, -0.04112784, -44.04013674, -0.13756309, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 12.0, 0.0, 10.3)
    ops.node(124004, 12.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.3025, 28326437.18227691, 11802682.15928205, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 381.21335979, 0.00074708, 465.4322808, 0.04244352, 46.54322808, 0.1411908, -381.21335979, -0.00074708, -465.4322808, -0.04244352, -46.54322808, -0.1411908, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 326.46367222, 0.00074708, 398.58711049, 0.04244352, 39.85871105, 0.1411908, -326.46367222, -0.00074708, -398.58711049, -0.04244352, -39.85871105, -0.1411908, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
