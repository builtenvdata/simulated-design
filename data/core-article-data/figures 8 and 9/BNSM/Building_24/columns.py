import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.1225, 26164800.56154356, 10902000.23397648, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 192.54880999, 0.00113649, 228.54065082, 0.01052301, 22.85406508, 0.02373839, -192.54880999, -0.00113649, -228.54065082, -0.01052301, -22.85406508, -0.02373839, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 180.54540147, 0.00113649, 214.2935267, 0.01052301, 21.42935267, 0.02373839, -180.54540147, -0.00113649, -214.2935267, -0.01052301, -21.42935267, -0.02373839, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 133.21258769, 0.02272985, 133.21258769, 0.06818955, 93.24881139, -1621.03189663, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 33.30314692, 8.977e-05, 99.90944077, 0.00026932, 333.03146923, 0.00089773, -33.30314692, -8.977e-05, -99.90944077, -0.00026932, -333.03146923, -0.00089773, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 133.21258769, 0.02272985, 133.21258769, 0.06818955, 93.24881139, -1621.03189663, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 33.30314692, 8.977e-05, 99.90944077, 0.00026932, 333.03146923, 0.00089773, -33.30314692, -8.977e-05, -99.90944077, -0.00026932, -333.03146923, -0.00089773, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 16.25, 0.0, 0.0)
    ops.node(121004, 16.25, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.1225, 27840449.32158704, 11600187.21732793, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 190.65069689, 0.00112096, 226.89324902, 0.01163343, 22.6893249, 0.0276917, -190.65069689, -0.00112096, -226.89324902, -0.01163343, -22.6893249, -0.0276917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 179.3953281, 0.00112096, 213.49824321, 0.01163343, 21.34982432, 0.0276917, -179.3953281, -0.00112096, -213.49824321, -0.01163343, -21.34982432, -0.0276917, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 141.4911141, 0.02241922, 141.4911141, 0.06725765, 99.04377987, -1652.08898003, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 35.37277853, 8.961e-05, 106.11833558, 0.00026884, 353.72778526, 0.00089613, -35.37277853, -8.961e-05, -106.11833558, -0.00026884, -353.72778526, -0.00089613, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 141.4911141, 0.02241922, 141.4911141, 0.06725765, 99.04377987, -1652.08898003, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 35.37277853, 8.961e-05, 106.11833558, 0.00026884, 353.72778526, 0.00089613, -35.37277853, -8.961e-05, -106.11833558, -0.00026884, -353.72778526, -0.00089613, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 3.95, 0.0)
    ops.node(121005, 0.0, 3.95, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.2025, 27601235.31822017, 11500514.71592507, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 450.538162, 0.0009615, 536.69718891, 0.00941187, 53.66971889, 0.02484804, -450.538162, -0.0009615, -536.69718891, -0.00941187, -53.66971889, -0.02484804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 399.36279046, 0.0009615, 475.73525413, 0.00941187, 47.57352541, 0.02484804, -399.36279046, -0.0009615, -475.73525413, -0.00941187, -47.57352541, -0.02484804, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 196.92568043, 0.0192301, 196.92568043, 0.05769029, 137.8479763, -2537.98383113, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 49.23142011, 7.61e-05, 147.69426033, 0.00022831, 492.31420109, 0.00076103, -49.23142011, -7.61e-05, -147.69426033, -0.00022831, -492.31420109, -0.00076103, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 196.92568043, 0.0192301, 196.92568043, 0.05769029, 137.8479763, -2537.98383113, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 49.23142011, 7.61e-05, 147.69426033, 0.00022831, 492.31420109, 0.00076103, -49.23142011, -7.61e-05, -147.69426033, -0.00022831, -492.31420109, -0.00076103, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 6.7, 3.95, 0.0)
    ops.node(121006, 6.7, 3.95, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.25, 27569694.28155567, 11487372.61731486, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 587.23132298, 0.00085388, 702.15182492, 0.015435, 70.21518249, 0.03278354, -587.23132298, -0.00085388, -702.15182492, -0.015435, -70.21518249, -0.03278354, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 606.36584906, 0.00085388, 725.03095599, 0.015435, 72.5030956, 0.03278354, -606.36584906, -0.00085388, -725.03095599, -0.015435, -72.5030956, -0.03278354, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 281.36411366, 0.01707755, 281.36411366, 0.05123264, 196.95487956, -2953.57370227, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 70.34102841, 8.818e-05, 211.02308524, 0.00026453, 703.41028414, 0.00088176, -70.34102841, -8.818e-05, -211.02308524, -0.00026453, -703.41028414, -0.00088176, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 281.36411366, 0.01707755, 281.36411366, 0.05123264, 196.95487956, -2953.57370227, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 70.34102841, 8.818e-05, 211.02308524, 0.00026453, 703.41028414, 0.00088176, -70.34102841, -8.818e-05, -211.02308524, -0.00026453, -703.41028414, -0.00088176, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 9.55, 3.95, 0.0)
    ops.node(121007, 9.55, 3.95, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.25, 27373518.03730932, 11405632.51554555, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 583.23539882, 0.00086673, 697.292224, 0.01548708, 69.7292224, 0.03253428, -583.23539882, -0.00086673, -697.292224, -0.01548708, -69.7292224, -0.03253428, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 601.86606161, 0.00086673, 719.56627718, 0.01548708, 71.95662772, 0.03253428, -601.86606161, -0.00086673, -719.56627718, -0.01548708, -71.95662772, -0.03253428, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 279.46313913, 0.01733465, 279.46313913, 0.05200396, 195.62419739, -2948.79702531, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 69.86578478, 8.821e-05, 209.59735435, 0.00026462, 698.65784782, 0.00088208, -69.86578478, -8.821e-05, -209.59735435, -0.00026462, -698.65784782, -0.00088208, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 279.46313913, 0.01733465, 279.46313913, 0.05200396, 195.62419739, -2948.79702531, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 69.86578478, 8.821e-05, 209.59735435, 0.00026462, 698.65784782, 0.00088208, -69.86578478, -8.821e-05, -209.59735435, -0.00026462, -698.65784782, -0.00088208, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 16.25, 3.95, 0.0)
    ops.node(121008, 16.25, 3.95, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.2025, 27058245.626104, 11274269.01087667, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 449.88174061, 0.00097816, 535.57534107, 0.00946956, 53.55753411, 0.02404633, -449.88174061, -0.00097816, -535.57534107, -0.00946956, -53.55753411, -0.02404633, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 398.89880036, 0.00097816, 474.88115602, 0.00946956, 47.4881156, 0.02404633, -398.89880036, -0.00097816, -474.88115602, -0.00946956, -47.4881156, -0.02404633, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 199.49891176, 0.01956319, 199.49891176, 0.05868958, 139.64923824, -2575.82160054, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 49.87472794, 7.864e-05, 149.62418382, 0.00023593, 498.74727941, 0.00078645, -49.87472794, -7.864e-05, -149.62418382, -0.00023593, -498.74727941, -0.00078645, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 199.49891176, 0.01956319, 199.49891176, 0.05868958, 139.64923824, -2575.82160054, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 49.87472794, 7.864e-05, 149.62418382, 0.00023593, 498.74727941, 0.00078645, -49.87472794, -7.864e-05, -149.62418382, -0.00023593, -498.74727941, -0.00078645, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 7.9, 0.0)
    ops.node(121009, 0.0, 7.9, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.1225, 27990151.46102585, 11662563.10876077, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 206.91945677, 0.00113664, 246.24534914, 0.01178346, 24.62453491, 0.02800287, -206.91945677, -0.00113664, -246.24534914, -0.01178346, -24.62453491, -0.02800287, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 188.82426563, 0.00113664, 224.71109262, 0.01178346, 22.47110926, 0.02800287, -188.82426563, -0.00113664, -224.71109262, -0.01178346, -22.47110926, -0.02800287, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 141.00857891, 0.02273274, 141.00857891, 0.06819822, 98.70600523, -1631.28869967, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 35.25214473, 8.883e-05, 105.75643418, 0.00026649, 352.52144727, 0.0008883, -35.25214473, -8.883e-05, -105.75643418, -0.00026649, -352.52144727, -0.0008883, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 141.00857891, 0.02273274, 141.00857891, 0.06819822, 98.70600523, -1631.28869967, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 35.25214473, 8.883e-05, 105.75643418, 0.00026649, 352.52144727, 0.0008883, -35.25214473, -8.883e-05, -105.75643418, -0.00026649, -352.52144727, -0.0008883, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 6.7, 7.9, 0.0)
    ops.node(121010, 6.7, 7.9, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 27302653.53285908, 11376105.63869128, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 298.86145257, 0.00100138, 355.82724553, 0.01278802, 35.58272455, 0.03007843, -298.86145257, -0.00100138, -355.82724553, -0.01278802, -35.58272455, -0.03007843, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 307.07005208, 0.00100138, 365.60048101, 0.01278802, 36.5600481, 0.03007843, -307.07005208, -0.00100138, -365.60048101, -0.01278802, -36.5600481, -0.03007843, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 187.4360324, 0.02002754, 187.4360324, 0.06008261, 131.20522268, -2264.00469094, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 46.8590081, 9.268e-05, 140.5770243, 0.00027804, 468.590081, 0.00092679, -46.8590081, -9.268e-05, -140.5770243, -0.00027804, -468.590081, -0.00092679, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 187.4360324, 0.02002754, 187.4360324, 0.06008261, 131.20522268, -2264.00469094, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 46.8590081, 9.268e-05, 140.5770243, 0.00027804, 468.590081, 0.00092679, -46.8590081, -9.268e-05, -140.5770243, -0.00027804, -468.590081, -0.00092679, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 9.55, 7.9, 0.0)
    ops.node(121011, 9.55, 7.9, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 27223283.14499593, 11343034.6437483, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 302.59607894, 0.00100508, 360.23816776, 0.01279631, 36.02381678, 0.02994005, -302.59607894, -0.00100508, -360.23816776, -0.01279631, -36.02381678, -0.02994005, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 311.07436743, 0.00100508, 370.33150116, 0.01279631, 37.03315012, 0.02994005, -311.07436743, -0.00100508, -370.33150116, -0.01279631, -37.03315012, -0.02994005, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 188.46628225, 0.02010165, 188.46628225, 0.06030494, 131.92639758, -2294.42571253, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 47.11657056, 9.346e-05, 141.34971169, 0.00028038, 471.16570563, 0.0009346, -47.11657056, -9.346e-05, -141.34971169, -0.00028038, -471.16570563, -0.0009346, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 188.46628225, 0.02010165, 188.46628225, 0.06030494, 131.92639758, -2294.42571253, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 47.11657056, 9.346e-05, 141.34971169, 0.00028038, 471.16570563, 0.0009346, -47.11657056, -9.346e-05, -141.34971169, -0.00028038, -471.16570563, -0.0009346, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 16.25, 7.9, 0.0)
    ops.node(121012, 16.25, 7.9, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 27994260.73399261, 11664275.30583026, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 206.22817968, 0.00110786, 245.42353756, 0.0120762, 24.54235376, 0.02830226, -206.22817968, -0.00110786, -245.42353756, -0.0120762, -24.54235376, -0.02830226, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 187.87428196, 0.00110786, 223.58133096, 0.0120762, 22.3581331, 0.02830226, -187.87428196, -0.00110786, -223.58133096, -0.0120762, -22.3581331, -0.02830226, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 142.79637617, 0.02215714, 142.79637617, 0.06647142, 99.95746332, -1666.7979019, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 35.69909404, 8.994e-05, 107.09728213, 0.00026983, 356.99094043, 0.00089943, -35.69909404, -8.994e-05, -107.09728213, -0.00026983, -356.99094043, -0.00089943, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 142.79637617, 0.02215714, 142.79637617, 0.06647142, 99.95746332, -1666.7979019, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 35.69909404, 8.994e-05, 107.09728213, 0.00026983, 356.99094043, 0.00089943, -35.69909404, -8.994e-05, -107.09728213, -0.00026983, -356.99094043, -0.00089943, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.35)
    ops.node(122001, 0.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.1225, 27797306.29059401, 11582210.95441417, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 196.11752253, 0.00108853, 235.16510145, 0.0128666, 23.51651014, 0.03290638, -196.11752253, -0.00108853, -235.16510145, -0.0128666, -23.51651014, -0.03290638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 173.32562156, 0.00108853, 207.83526558, 0.0128666, 20.78352656, 0.03290638, -173.32562156, -0.00108853, -207.83526558, -0.0128666, -20.78352656, -0.03290638, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 131.22294705, 0.02177051, 131.22294705, 0.06531153, 91.85606293, -1422.07238867, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 32.80573676, 8.324e-05, 98.41721029, 0.00024972, 328.05736762, 0.00083239, -32.80573676, -8.324e-05, -98.41721029, -0.00024972, -328.05736762, -0.00083239, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 131.22294705, 0.02177051, 131.22294705, 0.06531153, 91.85606293, -1422.07238867, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 32.80573676, 8.324e-05, 98.41721029, 0.00024972, 328.05736762, 0.00083239, -32.80573676, -8.324e-05, -98.41721029, -0.00024972, -328.05736762, -0.00083239, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 16.25, 0.0, 3.35)
    ops.node(122004, 16.25, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.1225, 26832014.25445624, 11180005.93935677, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 193.93873224, 0.00113851, 232.47336217, 0.01257461, 23.24733622, 0.03110548, -193.93873224, -0.00113851, -232.47336217, -0.01257461, -23.24733622, -0.03110548, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 172.06941348, 0.00113851, 206.2587221, 0.01257461, 20.62587221, 0.03110548, -172.06941348, -0.00113851, -206.2587221, -0.01257461, -20.62587221, -0.03110548, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 126.96574744, 0.02277026, 126.96574744, 0.06831077, 88.87602321, -1409.84611775, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 31.74143686, 8.344e-05, 95.22431058, 0.00025031, 317.4143686, 0.00083436, -31.74143686, -8.344e-05, -95.22431058, -0.00025031, -317.4143686, -0.00083436, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 126.96574744, 0.02277026, 126.96574744, 0.06831077, 88.87602321, -1409.84611775, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 31.74143686, 8.344e-05, 95.22431058, 0.00025031, 317.4143686, 0.00083436, -31.74143686, -8.344e-05, -95.22431058, -0.00025031, -317.4143686, -0.00083436, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 3.95, 3.375)
    ops.node(122005, 0.0, 3.95, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.2025, 27764742.8153908, 11568642.83974617, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 410.28643279, 0.00092129, 492.24484216, 0.01084447, 49.22448422, 0.03016447, -410.28643279, -0.00092129, -492.24484216, -0.01084447, -49.22448422, -0.03016447, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 360.27371595, 0.00092129, 432.2416348, 0.01084447, 43.22416348, 0.03016447, -360.27371595, -0.00092129, -432.2416348, -0.01084447, -43.22416348, -0.03016447, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 191.27115666, 0.01842583, 191.27115666, 0.05527749, 133.88980966, -2230.85836888, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 47.81778917, 7.348e-05, 143.4533675, 0.00022045, 478.17789166, 0.00073483, -47.81778917, -7.348e-05, -143.4533675, -0.00022045, -478.17789166, -0.00073483, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 191.27115666, 0.01842583, 191.27115666, 0.05527749, 133.88980966, -2230.85836888, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 47.81778917, 7.348e-05, 143.4533675, 0.00022045, 478.17789166, 0.00073483, -47.81778917, -7.348e-05, -143.4533675, -0.00022045, -478.17789166, -0.00073483, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 6.7, 3.95, 3.375)
    ops.node(122006, 6.7, 3.95, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.25, 26998694.20683129, 11249455.91951304, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 373.24849817, 0.00081518, 448.99793418, 0.01121521, 44.89979342, 0.028115, -373.24849817, -0.00081518, -448.99793418, -0.01121521, -44.89979342, -0.028115, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 336.94409998, 0.00081518, 405.32568937, 0.01121521, 40.53256894, 0.028115, -336.94409998, -0.00081518, -405.32568937, -0.01121521, -40.53256894, -0.028115, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 239.19608797, 0.01630358, 239.19608797, 0.04891075, 167.43726158, -2181.09275656, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 59.79902199, 7.655e-05, 179.39706598, 0.00022964, 597.99021992, 0.00076546, -59.79902199, -7.655e-05, -179.39706598, -0.00022964, -597.99021992, -0.00076546, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 239.19608797, 0.01630358, 239.19608797, 0.04891075, 167.43726158, -2181.09275656, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 59.79902199, 7.655e-05, 179.39706598, 0.00022964, 597.99021992, 0.00076546, -59.79902199, -7.655e-05, -179.39706598, -0.00022964, -597.99021992, -0.00076546, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 9.55, 3.95, 3.375)
    ops.node(122007, 9.55, 3.95, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.25, 28401895.65062046, 11834123.18775853, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 368.55267112, 0.00079386, 443.18459545, 0.01189519, 44.31845955, 0.0304104, -368.55267112, -0.00079386, -443.18459545, -0.01189519, -44.31845955, -0.0304104, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 333.77176101, 0.00079386, 401.36055024, 0.01189519, 40.13605502, 0.0304104, -333.77176101, -0.00079386, -401.36055024, -0.01189519, -40.13605502, -0.0304104, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 253.23060679, 0.01587729, 253.23060679, 0.04763187, 177.26142475, -2233.04478362, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 63.3076517, 7.703e-05, 189.92295509, 0.0002311, 633.07651698, 0.00077034, -63.3076517, -7.703e-05, -189.92295509, -0.0002311, -633.07651698, -0.00077034, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 253.23060679, 0.01587729, 253.23060679, 0.04763187, 177.26142475, -2233.04478362, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 63.3076517, 7.703e-05, 189.92295509, 0.0002311, 633.07651698, 0.00077034, -63.3076517, -7.703e-05, -189.92295509, -0.0002311, -633.07651698, -0.00077034, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 16.25, 3.95, 3.375)
    ops.node(122008, 16.25, 3.95, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.2025, 28627128.22616072, 11927970.09423363, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 412.08288447, 0.00093109, 494.29718339, 0.01083736, 49.42971834, 0.03133852, -412.08288447, -0.00093109, -494.29718339, -0.01083736, -49.42971834, -0.03133852, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 362.94642982, 0.00093109, 435.35755728, 0.01083736, 43.53575573, 0.03133852, -362.94642982, -0.00093109, -435.35755728, -0.01083736, -43.53575573, -0.03133852, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 194.4631281, 0.01862186, 194.4631281, 0.05586559, 136.12418967, -2209.61172639, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 48.61578202, 7.246e-05, 145.84734607, 0.00021737, 486.15782024, 0.00072458, -48.61578202, -7.246e-05, -145.84734607, -0.00021737, -486.15782024, -0.00072458, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 194.4631281, 0.01862186, 194.4631281, 0.05586559, 136.12418967, -2209.61172639, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 48.61578202, 7.246e-05, 145.84734607, 0.00021737, 486.15782024, 0.00072458, -48.61578202, -7.246e-05, -145.84734607, -0.00021737, -486.15782024, -0.00072458, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 7.9, 3.35)
    ops.node(122009, 0.0, 7.9, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.1225, 27724384.06680581, 11551826.69450242, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 186.04636369, 0.00110413, 223.04866317, 0.01335934, 22.30486632, 0.03318582, -186.04636369, -0.00110413, -223.04866317, -0.01335934, -22.30486632, -0.03318582, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 168.55668319, 0.00110413, 202.08050352, 0.01335934, 20.20805035, 0.03318582, -168.55668319, -0.00110413, -202.08050352, -0.01335934, -20.20805035, -0.03318582, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 131.65505505, 0.02208265, 131.65505505, 0.06624796, 92.15853853, -1437.33241162, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 32.91376376, 8.373e-05, 98.74129129, 0.0002512, 329.13763762, 0.00083732, -32.91376376, -8.373e-05, -98.74129129, -0.0002512, -329.13763762, -0.00083732, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 131.65505505, 0.02208265, 131.65505505, 0.06624796, 92.15853853, -1437.33241162, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 32.91376376, 8.373e-05, 98.74129129, 0.0002512, 329.13763762, 0.00083732, -32.91376376, -8.373e-05, -98.74129129, -0.0002512, -329.13763762, -0.00083732, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 6.7, 7.9, 3.35)
    ops.node(122010, 6.7, 7.9, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 28599797.08678026, 11916582.11949178, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 193.89907122, 0.00091743, 232.59089562, 0.01348911, 23.25908956, 0.03728925, -193.89907122, -0.00091743, -232.59089562, -0.01348911, -23.25908956, -0.03728925, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 178.97458517, 0.00091743, 214.68828497, 0.01348911, 21.4688285, 0.03728925, -178.97458517, -0.00091743, -214.68828497, -0.01348911, -21.4688285, -0.03728925, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 182.03692944, 0.01834851, 182.03692944, 0.05504552, 127.42585061, -2007.62476622, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 45.50923236, 8.593e-05, 136.52769708, 0.00025778, 455.09232361, 0.00085927, -45.50923236, -8.593e-05, -136.52769708, -0.00025778, -455.09232361, -0.00085927, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 182.03692944, 0.01834851, 182.03692944, 0.05504552, 127.42585061, -2007.62476622, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 45.50923236, 8.593e-05, 136.52769708, 0.00025778, 455.09232361, 0.00085927, -45.50923236, -8.593e-05, -136.52769708, -0.00025778, -455.09232361, -0.00085927, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 9.55, 7.9, 3.35)
    ops.node(122011, 9.55, 7.9, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 26589646.42101824, 11079019.34209093, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 190.33919935, 0.00091947, 228.26725326, 0.01286253, 22.82672533, 0.03329936, -190.33919935, -0.00091947, -228.26725326, -0.01286253, -22.82672533, -0.03329936, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 175.51370743, 0.00091947, 210.48755086, 0.01286253, 21.04875509, 0.03329936, -175.51370743, -0.00091947, -210.48755086, -0.01286253, -21.04875509, -0.03329936, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 171.43296259, 0.0183893, 171.43296259, 0.05516791, 120.00307381, -1995.00916191, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 42.85824065, 8.704e-05, 128.57472194, 0.00026112, 428.58240647, 0.00087039, -42.85824065, -8.704e-05, -128.57472194, -0.00026112, -428.58240647, -0.00087039, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 171.43296259, 0.0183893, 171.43296259, 0.05516791, 120.00307381, -1995.00916191, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 42.85824065, 8.704e-05, 128.57472194, 0.00026112, 428.58240647, 0.00087039, -42.85824065, -8.704e-05, -128.57472194, -0.00026112, -428.58240647, -0.00087039, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 16.25, 7.9, 3.35)
    ops.node(122012, 16.25, 7.9, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 27747346.85397518, 11561394.52248966, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 185.76147411, 0.00108458, 222.70767646, 0.01290863, 22.27076765, 0.03276993, -185.76147411, -0.00108458, -222.70767646, -0.01290863, -22.27076765, -0.03276993, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 168.06736384, 0.00108458, 201.49437481, 0.01290863, 20.14943748, 0.03276993, -168.06736384, -0.00108458, -201.49437481, -0.01290863, -20.14943748, -0.03276993, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 129.90259304, 0.02169152, 129.90259304, 0.06507456, 90.93181512, -1397.45588343, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 32.47564826, 8.255e-05, 97.42694478, 0.00024765, 324.75648259, 0.00082549, -32.47564826, -8.255e-05, -97.42694478, -0.00024765, -324.75648259, -0.00082549, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 129.90259304, 0.02169152, 129.90259304, 0.06507456, 90.93181512, -1397.45588343, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 32.47564826, 8.255e-05, 97.42694478, 0.00024765, 324.75648259, 0.00082549, -32.47564826, -8.255e-05, -97.42694478, -0.00024765, -324.75648259, -0.00082549, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.35)
    ops.node(123001, 0.0, 0.0, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 26506509.15412935, 11044378.81422056, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 80.91691886, 0.00162681, 96.36867764, 0.01297046, 9.63686776, 0.03169649, -80.91691886, -0.00162681, -96.36867764, -0.01297046, -9.63686776, -0.03169649, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 80.91691886, 0.00162681, 96.36867764, 0.01297046, 9.63686776, 0.03169649, -80.91691886, -0.00162681, -96.36867764, -0.01297046, -9.63686776, -0.03169649, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 48.85282027, 0.03253617, 48.85282027, 0.09760851, 34.19697419, -979.18134448, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 12.21320507, 6.37e-05, 36.6396152, 0.00019109, 122.13205066, 0.00063696, -12.21320507, -6.37e-05, -36.6396152, -0.00019109, -122.13205066, -0.00063696, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 48.85282027, 0.03253617, 48.85282027, 0.09760851, 34.19697419, -979.18134448, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 12.21320507, 6.37e-05, 36.6396152, 0.00019109, 122.13205066, 0.00063696, -12.21320507, -6.37e-05, -36.6396152, -0.00019109, -122.13205066, -0.00063696, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 16.25, 0.0, 6.35)
    ops.node(123004, 16.25, 0.0, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 27586072.2657209, 11494196.77738371, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 79.33071523, 0.00159257, 94.60659565, 0.01374891, 9.46065957, 0.034747, -79.33071523, -0.00159257, -94.60659565, -0.01374891, -9.46065957, -0.034747, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 79.33071523, 0.00159257, 94.60659565, 0.01374891, 9.46065957, 0.034747, -79.33071523, -0.00159257, -94.60659565, -0.01374891, -9.46065957, -0.034747, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 51.0318211, 0.03185135, 51.0318211, 0.09555405, 35.72227477, -992.02446058, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 12.75795528, 6.393e-05, 38.27386583, 0.0001918, 127.57955275, 0.00063933, -12.75795528, -6.393e-05, -38.27386583, -0.0001918, -127.57955275, -0.00063933, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 51.0318211, 0.03185135, 51.0318211, 0.09555405, 35.72227477, -992.02446058, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 12.75795528, 6.393e-05, 38.27386583, 0.0001918, 127.57955275, 0.00063933, -12.75795528, -6.393e-05, -38.27386583, -0.0001918, -127.57955275, -0.00063933, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 3.95, 6.375)
    ops.node(123005, 0.0, 3.95, 8.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 26674244.54409361, 11114268.560039, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 186.83022826, 0.00118269, 223.58913916, 0.01081046, 22.35891392, 0.03032004, -186.83022826, -0.00118269, -223.58913916, -0.01081046, -22.35891392, -0.03032004, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 186.83022826, 0.00118269, 223.58913916, 0.01081046, 22.35891392, 0.03032004, -186.83022826, -0.00118269, -223.58913916, -0.01081046, -22.35891392, -0.03032004, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 91.19800642, 0.02365371, 91.19800642, 0.07096114, 63.83860449, -1611.77383109, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 22.7995016, 6.029e-05, 68.39850481, 0.00018086, 227.99501604, 0.00060285, -22.7995016, -6.029e-05, -68.39850481, -0.00018086, -227.99501604, -0.00060285, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 91.19800642, 0.02365371, 91.19800642, 0.07096114, 63.83860449, -1611.77383109, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 22.7995016, 6.029e-05, 68.39850481, 0.00018086, 227.99501604, 0.00060285, -22.7995016, -6.029e-05, -68.39850481, -0.00018086, -227.99501604, -0.00060285, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 6.7, 3.95, 6.375)
    ops.node(123006, 6.7, 3.95, 8.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.16, 26803919.79636461, 11168299.91515192, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 184.37939259, 0.00095372, 221.5426631, 0.01189353, 22.15426631, 0.03019002, -184.37939259, -0.00095372, -221.5426631, -0.01189353, -22.15426631, -0.03019002, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 184.37939259, 0.00095372, 221.5426631, 0.01189353, 22.15426631, 0.03019002, -184.37939259, -0.00095372, -221.5426631, -0.01189353, -22.15426631, -0.03019002, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 156.56902351, 0.01907447, 156.56902351, 0.0572234, 109.59831646, -1647.1834574, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 39.14225588, 7.886e-05, 117.42676764, 0.00023657, 391.42255878, 0.00078857, -39.14225588, -7.886e-05, -117.42676764, -0.00023657, -391.42255878, -0.00078857, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 156.56902351, 0.01907447, 156.56902351, 0.0572234, 109.59831646, -1647.1834574, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 39.14225588, 7.886e-05, 117.42676764, 0.00023657, 391.42255878, 0.00078857, -39.14225588, -7.886e-05, -117.42676764, -0.00023657, -391.42255878, -0.00078857, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 9.55, 3.95, 6.375)
    ops.node(123007, 9.55, 3.95, 8.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.16, 27940958.63968185, 11642066.09986744, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 184.6124694, 0.00095024, 221.83373042, 0.01213397, 22.18337304, 0.03199675, -184.6124694, -0.00095024, -221.83373042, -0.01213397, -22.18337304, -0.03199675, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 184.6124694, 0.00095024, 221.83373042, 0.01213397, 22.18337304, 0.03199675, -184.6124694, -0.00095024, -221.83373042, -0.01213397, -22.18337304, -0.03199675, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 162.1840294, 0.01900476, 162.1840294, 0.05701429, 113.52882058, -1647.39764507, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 40.54600735, 7.836e-05, 121.63802205, 0.00023508, 405.4600735, 0.00078361, -40.54600735, -7.836e-05, -121.63802205, -0.00023508, -405.4600735, -0.00078361, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 162.1840294, 0.01900476, 162.1840294, 0.05701429, 113.52882058, -1647.39764507, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 40.54600735, 7.836e-05, 121.63802205, 0.00023508, 405.4600735, 0.00078361, -40.54600735, -7.836e-05, -121.63802205, -0.00023508, -405.4600735, -0.00078361, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 16.25, 3.95, 6.375)
    ops.node(123008, 16.25, 3.95, 8.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 27117638.0203096, 11299015.84179567, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 191.79379134, 0.0011405, 229.6111744, 0.01102262, 22.96111744, 0.03134501, -191.79379134, -0.0011405, -229.6111744, -0.01102262, -22.96111744, -0.03134501, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 191.79379134, 0.0011405, 229.6111744, 0.01102262, 22.96111744, 0.03134501, -191.79379134, -0.0011405, -229.6111744, -0.01102262, -22.96111744, -0.03134501, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 92.90013696, 0.02281004, 92.90013696, 0.06843013, 65.03009587, -1625.37180623, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 23.22503424, 6.041e-05, 69.67510272, 0.00018122, 232.2503424, 0.00060406, -23.22503424, -6.041e-05, -69.67510272, -0.00018122, -232.2503424, -0.00060406, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 92.90013696, 0.02281004, 92.90013696, 0.06843013, 65.03009587, -1625.37180623, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 23.22503424, 6.041e-05, 69.67510272, 0.00018122, 232.2503424, 0.00060406, -23.22503424, -6.041e-05, -69.67510272, -0.00018122, -232.2503424, -0.00060406, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 7.9, 6.35)
    ops.node(123009, 0.0, 7.9, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.09, 26721209.98199302, 11133837.49249709, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 102.88731896, 0.00122206, 123.67231918, 0.0136746, 12.36723192, 0.0357491, -102.88731896, -0.00122206, -123.67231918, -0.0136746, -12.36723192, -0.0357491, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 102.88731896, 0.00122206, 123.67231918, 0.0136746, 12.36723192, 0.0357491, -102.88731896, -0.00122206, -123.67231918, -0.0136746, -12.36723192, -0.0357491, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 79.30964133, 0.02444125, 79.30964133, 0.07332375, 55.51674893, -1087.0867654, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 19.82741033, 7.123e-05, 59.482231, 0.0002137, 198.27410333, 0.00071233, -19.82741033, -7.123e-05, -59.482231, -0.0002137, -198.27410333, -0.00071233, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 79.30964133, 0.02444125, 79.30964133, 0.07332375, 55.51674893, -1087.0867654, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 19.82741033, 7.123e-05, 59.482231, 0.0002137, 198.27410333, 0.00071233, -19.82741033, -7.123e-05, -59.482231, -0.0002137, -198.27410333, -0.00071233, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 6.7, 7.9, 6.35)
    ops.node(123010, 6.7, 7.9, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 27102092.29440457, 11292538.4560019, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 121.07074033, 0.00100626, 145.71982156, 0.01451642, 14.57198216, 0.04031833, -121.07074033, -0.00100626, -145.71982156, -0.01451642, -14.57198216, -0.04031833, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 115.2171729, 0.00100626, 138.67451236, 0.01451642, 13.86745124, 0.04031833, -115.2171729, -0.00100626, -138.67451236, -0.01451642, -13.86745124, -0.04031833, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 136.12176636, 0.02012524, 136.12176636, 0.06037572, 95.28523645, -1631.50774259, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 34.03044159, 8.856e-05, 102.09132477, 0.00026568, 340.30441589, 0.00088561, -34.03044159, -8.856e-05, -102.09132477, -0.00026568, -340.30441589, -0.00088561, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 136.12176636, 0.02012524, 136.12176636, 0.06037572, 95.28523645, -1631.50774259, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 34.03044159, 8.856e-05, 102.09132477, 0.00026568, 340.30441589, 0.00088561, -34.03044159, -8.856e-05, -102.09132477, -0.00026568, -340.30441589, -0.00088561, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 9.55, 7.9, 6.35)
    ops.node(123011, 9.55, 7.9, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 27417240.48656357, 11423850.20273482, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 123.00403579, 0.00100399, 148.04273267, 0.01474477, 14.80427327, 0.04110305, -123.00403579, -0.00100399, -148.04273267, -0.01474477, -14.80427327, -0.04110305, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 116.89303746, 0.00100399, 140.68777975, 0.01474477, 14.06877797, 0.04110305, -116.89303746, -0.00100399, -140.68777975, -0.01474477, -14.06877797, -0.04110305, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 137.93549273, 0.02007976, 137.93549273, 0.06023928, 96.55484491, -1647.92722492, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 34.48387318, 8.871e-05, 103.45161955, 0.00026613, 344.83873183, 0.00088709, -34.48387318, -8.871e-05, -103.45161955, -0.00026613, -344.83873183, -0.00088709, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 137.93549273, 0.02007976, 137.93549273, 0.06023928, 96.55484491, -1647.92722492, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 34.48387318, 8.871e-05, 103.45161955, 0.00026613, 344.83873183, 0.00088709, -34.48387318, -8.871e-05, -103.45161955, -0.00026613, -344.83873183, -0.00088709, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 16.25, 7.9, 6.35)
    ops.node(123012, 16.25, 7.9, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.09, 27669223.57413147, 11528843.15588811, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 103.9385423, 0.00123425, 124.94769233, 0.01411194, 12.49476923, 0.03776443, -103.9385423, -0.00123425, -124.94769233, -0.01411194, -12.49476923, -0.03776443, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 103.9385423, 0.00123425, 124.94769233, 0.01411194, 12.49476923, 0.03776443, -103.9385423, -0.00123425, -124.94769233, -0.01411194, -12.49476923, -0.03776443, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 84.17412959, 0.02468505, 84.17412959, 0.07405515, 58.92189072, -1080.40925522, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 21.0435324, 7.301e-05, 63.13059719, 0.00021904, 210.43532398, 0.00073012, -21.0435324, -7.301e-05, -63.13059719, -0.00021904, -210.43532398, -0.00073012, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 84.17412959, 0.02468505, 84.17412959, 0.07405515, 58.92189072, -1080.40925522, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 21.0435324, 7.301e-05, 63.13059719, 0.00021904, 210.43532398, 0.00073012, -21.0435324, -7.301e-05, -63.13059719, -0.00021904, -210.43532398, -0.00073012, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.35)
    ops.node(124001, 0.0, 0.0, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 27049902.24789109, 11270792.60328796, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 63.51886412, 0.0014705, 77.08456705, 0.01682536, 7.70845671, 0.0508531, -63.51886412, -0.0014705, -77.08456705, -0.01682536, -7.70845671, -0.0508531, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 63.51886412, 0.0014705, 77.08456705, 0.01682536, 7.70845671, 0.0508531, -63.51886412, -0.0014705, -77.08456705, -0.01682536, -7.70845671, -0.0508531, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 37.6972116, 0.02940996, 37.6972116, 0.08822987, 26.38804812, -822.50150626, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 9.4243029, 4.816e-05, 28.2729087, 0.00014449, 94.24302901, 0.00048163, -9.4243029, -4.816e-05, -28.2729087, -0.00014449, -94.24302901, -0.00048163, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 37.6972116, 0.02940996, 37.6972116, 0.08822987, 26.38804812, -822.50150626, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 9.4243029, 4.816e-05, 28.2729087, 0.00014449, 94.24302901, 0.00048163, -9.4243029, -4.816e-05, -28.2729087, -0.00014449, -94.24302901, -0.00048163, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 16.25, 0.0, 9.35)
    ops.node(124004, 16.25, 0.0, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 28037197.21121729, 11682165.50467387, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 65.23610289, 0.0014628, 79.07616705, 0.01664706, 7.9076167, 0.05193096, -65.23610289, -0.0014628, -79.07616705, -0.01664706, -7.9076167, -0.05193096, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 65.23610289, 0.0014628, 79.07616705, 0.01664706, 7.9076167, 0.05193096, -65.23610289, -0.0014628, -79.07616705, -0.01664706, -7.9076167, -0.05193096, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 39.48942654, 0.02925596, 39.48942654, 0.08776789, 27.64259858, -811.51520342, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 9.87235664, 4.868e-05, 29.61706991, 0.00014603, 98.72356635, 0.00048677, -9.87235664, -4.868e-05, -29.61706991, -0.00014603, -98.72356635, -0.00048677, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 39.48942654, 0.02925596, 39.48942654, 0.08776789, 27.64259858, -811.51520342, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 9.87235664, 4.868e-05, 29.61706991, 0.00014603, 98.72356635, 0.00048677, -9.87235664, -4.868e-05, -29.61706991, -0.00014603, -98.72356635, -0.00048677, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 3.95, 9.375)
    ops.node(124005, 0.0, 3.95, 11.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 27701102.23286538, 11542125.93036058, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 152.24335622, 0.00111307, 184.67110785, 0.01298463, 18.46711079, 0.04431598, -152.24335622, -0.00111307, -184.67110785, -0.01298463, -18.46711079, -0.04431598, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 152.24335622, 0.00111307, 184.67110785, 0.01298463, 18.46711079, 0.04431598, -152.24335622, -0.00111307, -184.67110785, -0.01298463, -18.46711079, -0.04431598, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 75.75998255, 0.02226138, 75.75998255, 0.06678413, 53.03198778, -1334.61863059, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 18.93999564, 4.822e-05, 56.81998691, 0.00014467, 189.39995637, 0.00048224, -18.93999564, -4.822e-05, -56.81998691, -0.00014467, -189.39995637, -0.00048224, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 75.75998255, 0.02226138, 75.75998255, 0.06678413, 53.03198778, -1334.61863059, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 18.93999564, 4.822e-05, 56.81998691, 0.00014467, 189.39995637, 0.00048224, -18.93999564, -4.822e-05, -56.81998691, -0.00014467, -189.39995637, -0.00048224, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 6.7, 3.95, 9.375)
    ops.node(124006, 6.7, 3.95, 11.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.16, 27747327.30093216, 11561386.3753884, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 139.72349143, 0.00088655, 169.64874374, 0.01376126, 16.96487437, 0.04045514, -139.72349143, -0.00088655, -169.64874374, -0.01376126, -16.96487437, -0.04045514, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 139.72349143, 0.00088655, 169.64874374, 0.01376126, 16.96487437, 0.04045514, -139.72349143, -0.00088655, -169.64874374, -0.01376126, -16.96487437, -0.04045514, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 139.32299619, 0.01773105, 139.32299619, 0.05319316, 97.52609733, -1327.10792446, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 34.83074905, 6.779e-05, 104.49224714, 0.00020336, 348.30749048, 0.00067785, -34.83074905, -6.779e-05, -104.49224714, -0.00020336, -348.30749048, -0.00067785, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 139.32299619, 0.01773105, 139.32299619, 0.05319316, 97.52609733, -1327.10792446, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 34.83074905, 6.779e-05, 104.49224714, 0.00020336, 348.30749048, 0.00067785, -34.83074905, -6.779e-05, -104.49224714, -0.00020336, -348.30749048, -0.00067785, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 9.55, 3.95, 9.375)
    ops.node(124007, 9.55, 3.95, 11.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.16, 27498264.73159692, 11457610.30483205, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 137.49917774, 0.00089265, 167.00511369, 0.01411609, 16.70051137, 0.04060113, -137.49917774, -0.00089265, -167.00511369, -0.01411609, -16.70051137, -0.04060113, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 137.49917774, 0.00089265, 167.00511369, 0.01411609, 16.70051137, 0.04060113, -137.49917774, -0.00089265, -167.00511369, -0.01411609, -16.70051137, -0.04060113, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 139.09865712, 0.01785306, 139.09865712, 0.05355919, 97.36905999, -1353.90580232, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 34.77466428, 6.829e-05, 104.32399284, 0.00020487, 347.74664281, 0.00068289, -34.77466428, -6.829e-05, -104.32399284, -0.00020487, -347.74664281, -0.00068289, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 139.09865712, 0.01785306, 139.09865712, 0.05355919, 97.36905999, -1353.90580232, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 34.77466428, 6.829e-05, 104.32399284, 0.00020487, 347.74664281, 0.00068289, -34.77466428, -6.829e-05, -104.32399284, -0.00020487, -347.74664281, -0.00068289, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 16.25, 3.95, 9.375)
    ops.node(124008, 16.25, 3.95, 11.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 28426418.45423739, 11844341.02259891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 154.89423444, 0.00109056, 187.69374312, 0.01320311, 18.76937431, 0.04529265, -154.89423444, -0.00109056, -187.69374312, -0.01320311, -18.76937431, -0.04529265, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 154.89423444, 0.00109056, 187.69374312, 0.01320311, 18.76937431, 0.04529265, -154.89423444, -0.00109056, -187.69374312, -0.01320311, -18.76937431, -0.04529265, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 78.36383076, 0.02181129, 78.36383076, 0.06543386, 54.85468153, -1375.84031347, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 19.59095769, 4.861e-05, 58.77287307, 0.00014583, 195.9095769, 0.00048608, -19.59095769, -4.861e-05, -58.77287307, -0.00014583, -195.9095769, -0.00048608, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 78.36383076, 0.02181129, 78.36383076, 0.06543386, 54.85468153, -1375.84031347, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 19.59095769, 4.861e-05, 58.77287307, 0.00014583, 195.9095769, 0.00048608, -19.59095769, -4.861e-05, -58.77287307, -0.00014583, -195.9095769, -0.00048608, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 7.9, 9.35)
    ops.node(124009, 0.0, 7.9, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.09, 27904915.06573193, 11627047.94405497, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 81.77621048, 0.00119815, 99.42679164, 0.01660731, 9.94267916, 0.0503516, -81.77621048, -0.00119815, -99.42679164, -0.01660731, -9.94267916, -0.0503516, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 81.77621048, 0.00119815, 99.42679164, 0.01660731, 9.94267916, 0.0503516, -81.77621048, -0.00119815, -99.42679164, -0.01660731, -9.94267916, -0.0503516, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 71.51208094, 0.02396295, 71.51208094, 0.07188885, 50.05845666, -1016.39200073, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 17.87802024, 6.15e-05, 53.63406071, 0.00018451, 178.78020235, 0.00061505, -17.87802024, -6.15e-05, -53.63406071, -0.00018451, -178.78020235, -0.00061505, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 71.51208094, 0.02396295, 71.51208094, 0.07188885, 50.05845666, -1016.39200073, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 17.87802024, 6.15e-05, 53.63406071, 0.00018451, 178.78020235, 0.00061505, -17.87802024, -6.15e-05, -53.63406071, -0.00018451, -178.78020235, -0.00061505, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 6.7, 7.9, 9.35)
    ops.node(124010, 6.7, 7.9, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 26928738.82379294, 11220307.84324706, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 91.35855622, 0.00094814, 111.2423749, 0.01717357, 11.12423749, 0.05321141, -91.35855622, -0.00094814, -111.2423749, -0.01717357, -11.12423749, -0.05321141, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 85.75720635, 0.00094814, 104.42191397, 0.01717357, 10.4421914, 0.05321141, -85.75720635, -0.00094814, -104.42191397, -0.01717357, -10.4421914, -0.05321141, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 118.66167872, 0.0189629, 118.66167872, 0.0568887, 83.06317511, -1658.37197487, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 29.66541968, 7.77e-05, 88.99625904, 0.0002331, 296.65419681, 0.00077698, -29.66541968, -7.77e-05, -88.99625904, -0.0002331, -296.65419681, -0.00077698, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 118.66167872, 0.0189629, 118.66167872, 0.0568887, 83.06317511, -1658.37197487, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 29.66541968, 7.77e-05, 88.99625904, 0.0002331, 296.65419681, 0.00077698, -29.66541968, -7.77e-05, -88.99625904, -0.0002331, -296.65419681, -0.00077698, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 9.55, 7.9, 9.35)
    ops.node(124011, 9.55, 7.9, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 28178032.43047657, 11740846.84603191, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 89.58190383, 0.00094786, 108.86809796, 0.0169783, 10.8868098, 0.05419902, -89.58190383, -0.00094786, -108.86809796, -0.0169783, -10.8868098, -0.05419902, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 84.4038522, 0.00094786, 102.57525747, 0.0169783, 10.25752575, 0.05419902, -84.4038522, -0.00094786, -102.57525747, -0.0169783, -10.25752575, -0.05419902, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 122.00980123, 0.01895722, 122.00980123, 0.05687166, 85.40686086, -1616.95252053, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 30.50245031, 7.635e-05, 91.50735092, 0.00022905, 305.02450308, 0.00076349, -30.50245031, -7.635e-05, -91.50735092, -0.00022905, -305.02450308, -0.00076349, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 122.00980123, 0.01895722, 122.00980123, 0.05687166, 85.40686086, -1616.95252053, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 30.50245031, 7.635e-05, 91.50735092, 0.00022905, 305.02450308, 0.00076349, -30.50245031, -7.635e-05, -91.50735092, -0.00022905, -305.02450308, -0.00076349, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 16.25, 7.9, 9.35)
    ops.node(124012, 16.25, 7.9, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.09, 29280730.9550745, 12200304.56461438, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 81.89806749, 0.00113582, 99.3157866, 0.01681478, 9.93157866, 0.05159981, -81.89806749, -0.00113582, -99.3157866, -0.01681478, -9.93157866, -0.05159981, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 81.89806749, 0.00113582, 99.3157866, 0.01681478, 9.93157866, 0.05159981, -81.89806749, -0.00113582, -99.3157866, -0.01681478, -9.93157866, -0.05159981, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 77.35918714, 0.02271631, 77.35918714, 0.06814894, 54.151431, -1035.75453536, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 19.33979679, 6.341e-05, 58.01939036, 0.00019022, 193.39796786, 0.00063408, -19.33979679, -6.341e-05, -58.01939036, -0.00019022, -193.39796786, -0.00063408, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 77.35918714, 0.02271631, 77.35918714, 0.06814894, 54.151431, -1035.75453536, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 19.33979679, 6.341e-05, 58.01939036, 0.00019022, 193.39796786, 0.00063408, -19.33979679, -6.341e-05, -58.01939036, -0.00019022, -193.39796786, -0.00063408, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 6.7, 0.0, 0.0)
    ops.node(124013, 6.7, 0.0, 1.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4030, 170002, 124013, 0.16, 27736419.81023252, 11556841.58759688, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24030, 300.45123331, 0.00075567, 357.45570026, 0.01296314, 35.74557003, 0.03041187, -300.45123331, -0.00075567, -357.45570026, -0.01296314, -35.74557003, -0.03041187, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14030, 315.67808773, 0.00075567, 375.5715384, 0.01296314, 37.55715384, 0.03041187, -315.67808773, -0.00075567, -375.5715384, -0.01296314, -37.55715384, -0.03041187, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24030, 4030, 0.0, 288.91579378, 0.01511345, 288.91579378, 0.04534034, 202.24105565, -4682.12310699, 0.05, 2, 0, 70002, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 44030, 72.22894845, 7.031e-05, 216.68684534, 0.00021093, 722.28948446, 0.00070311, -72.22894845, -7.031e-05, -216.68684534, -0.00021093, -722.28948446, -0.00070311, 0.4, 0.3, 0.003, 0.0, 0.0, 24030, 2)
    ops.limitCurve('ThreePoint', 14030, 4030, 0.0, 288.91579378, 0.01511345, 288.91579378, 0.04534034, 202.24105565, -4682.12310699, 0.05, 2, 0, 70002, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 34030, 72.22894845, 7.031e-05, 216.68684534, 0.00021093, 722.28948446, 0.00070311, -72.22894845, -7.031e-05, -216.68684534, -0.00021093, -722.28948446, -0.00070311, 0.4, 0.3, 0.003, 0.0, 0.0, 14030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4030, 99999, 'P', 44030, 'Vy', 34030, 'Vz', 24030, 'My', 14030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 4030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174013, 6.7, 0.0, 1.7)
    ops.node(121002, 6.7, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4031, 174013, 121002, 0.16, 28773795.87523847, 11989081.6146827, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24031, 305.96582288, 0.00075221, 364.69461423, 0.01296525, 36.46946142, 0.03293024, -305.96582288, -0.00075221, -364.69461423, -0.01296525, -36.46946142, -0.03293024, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14031, 250.04377197, 0.00075221, 298.03857209, 0.01296525, 29.80385721, 0.03293024, -250.04377197, -0.00075221, -298.03857209, -0.01296525, -29.80385721, -0.03293024, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24031, 4031, 0.0, 291.37141819, 0.01504416, 291.37141819, 0.04513249, 203.95999273, -4445.02316116, 0.05, 2, 0, 74013, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44031, 72.84285455, 6.835e-05, 218.52856364, 0.00020506, 728.42854548, 0.00068352, -72.84285455, -6.835e-05, -218.52856364, -0.00020506, -728.42854548, -0.00068352, 0.4, 0.3, 0.003, 0.0, 0.0, 24031, 2)
    ops.limitCurve('ThreePoint', 14031, 4031, 0.0, 291.37141819, 0.01504416, 291.37141819, 0.04513249, 203.95999273, -4445.02316116, 0.05, 2, 0, 74013, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34031, 72.84285455, 6.835e-05, 218.52856364, 0.00020506, 728.42854548, 0.00068352, -72.84285455, -6.835e-05, -218.52856364, -0.00020506, -728.42854548, -0.00068352, 0.4, 0.3, 0.003, 0.0, 0.0, 14031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4031, 99999, 'P', 44031, 'Vy', 34031, 'Vz', 24031, 'My', 14031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174013, 74013, 174013, 4031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.55, 0.0, 0.0)
    ops.node(124014, 9.55, 0.0, 1.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4032, 170003, 124014, 0.16, 27398926.139446, 11416219.22476917, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24032, 295.76254601, 0.0007782, 351.73967878, 0.01276763, 35.17396788, 0.02959923, -295.76254601, -0.0007782, -351.73967878, -0.01276763, -35.17396788, -0.02959923, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14032, 309.93341193, 0.0007782, 368.59257613, 0.01276763, 36.85925761, 0.02959923, -309.93341193, -0.0007782, -368.59257613, -0.01276763, -36.85925761, -0.02959923, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24032, 4032, 0.0, 286.44497628, 0.01556408, 286.44497628, 0.04669225, 200.5114834, -4706.21964572, 0.05, 2, 0, 70003, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 44032, 71.61124407, 7.057e-05, 214.83373221, 0.00021171, 716.11244071, 0.00070569, -71.61124407, -7.057e-05, -214.83373221, -0.00021171, -716.11244071, -0.00070569, 0.4, 0.3, 0.003, 0.0, 0.0, 24032, 2)
    ops.limitCurve('ThreePoint', 14032, 4032, 0.0, 286.44497628, 0.01556408, 286.44497628, 0.04669225, 200.5114834, -4706.21964572, 0.05, 2, 0, 70003, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 34032, 71.61124407, 7.057e-05, 214.83373221, 0.00021171, 716.11244071, 0.00070569, -71.61124407, -7.057e-05, -214.83373221, -0.00021171, -716.11244071, -0.00070569, 0.4, 0.3, 0.003, 0.0, 0.0, 14032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4032, 99999, 'P', 44032, 'Vy', 34032, 'Vz', 24032, 'My', 14032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 4032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174014, 9.55, 0.0, 1.7)
    ops.node(121003, 9.55, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4033, 174014, 121003, 0.16, 27877473.28220074, 11615613.86758364, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24033, 306.41871546, 0.00074101, 365.08344882, 0.01289733, 36.50834488, 0.03130545, -306.41871546, -0.00074101, -365.08344882, -0.01289733, -36.50834488, -0.03130545, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14033, 248.13881834, 0.00074101, 295.64569988, 0.01289733, 29.56456999, 0.03130545, -248.13881834, -0.00074101, -295.64569988, -0.01289733, -29.56456999, -0.03130545, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24033, 4033, 0.0, 284.38696606, 0.01482011, 284.38696606, 0.04446033, 199.07087624, -4491.72894296, 0.05, 2, 0, 74014, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44033, 71.09674151, 6.886e-05, 213.29022454, 0.00020658, 710.96741515, 0.00068859, -71.09674151, -6.886e-05, -213.29022454, -0.00020658, -710.96741515, -0.00068859, 0.4, 0.3, 0.003, 0.0, 0.0, 24033, 2)
    ops.limitCurve('ThreePoint', 14033, 4033, 0.0, 284.38696606, 0.01482011, 284.38696606, 0.04446033, 199.07087624, -4491.72894296, 0.05, 2, 0, 74014, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34033, 71.09674151, 6.886e-05, 213.29022454, 0.00020658, 710.96741515, 0.00068859, -71.09674151, -6.886e-05, -213.29022454, -0.00020658, -710.96741515, -0.00068859, 0.4, 0.3, 0.003, 0.0, 0.0, 14033, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4033, 99999, 'P', 44033, 'Vy', 34033, 'Vz', 24033, 'My', 14033, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174014, 74014, 174014, 4033, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4033, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 6.7, 0.0, 3.35)
    ops.node(124015, 6.7, 0.0, 4.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4035, 171002, 124015, 0.16, 27584856.71586768, 11493690.2982782, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24035, 218.22779284, 0.00073707, 261.58420437, 0.01335838, 26.15842044, 0.0349336, -218.22779284, -0.00073707, -261.58420437, -0.01335838, -26.15842044, -0.0349336, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14035, 192.8081632, 0.00073707, 231.11432925, 0.01335838, 23.11143293, 0.0349336, -192.8081632, -0.00073707, -231.11432925, -0.01335838, -23.11143293, -0.0349336, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24035, 4035, 0.0, 264.03366282, 0.01474142, 264.03366282, 0.04422425, 184.82356397, -4047.66269388, 0.05, 2, 0, 71002, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 44035, 66.0084157, 6.461e-05, 198.02524711, 0.00019383, 660.08415704, 0.00064609, -66.0084157, -6.461e-05, -198.02524711, -0.00019383, -660.08415704, -0.00064609, 0.4, 0.3, 0.003, 0.0, 0.0, 24035, 2)
    ops.limitCurve('ThreePoint', 14035, 4035, 0.0, 264.03366282, 0.01474142, 264.03366282, 0.04422425, 184.82356397, -4047.66269388, 0.05, 2, 0, 71002, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 34035, 66.0084157, 6.461e-05, 198.02524711, 0.00019383, 660.08415704, 0.00064609, -66.0084157, -6.461e-05, -198.02524711, -0.00019383, -660.08415704, -0.00064609, 0.4, 0.3, 0.003, 0.0, 0.0, 14035, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4035, 99999, 'P', 44035, 'Vy', 34035, 'Vz', 24035, 'My', 14035, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4035, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 4035, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174015, 6.7, 0.0, 4.675)
    ops.node(122002, 6.7, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4036, 174015, 122002, 0.16, 27604231.51047998, 11501763.12936666, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24036, 216.21067936, 0.00072748, 259.51438707, 0.01340453, 25.95143871, 0.03589184, -216.21067936, -0.00072748, -259.51438707, -0.01340453, -25.95143871, -0.03589184, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14036, 189.51079802, 0.00072748, 227.46692595, 0.01340453, 22.74669259, 0.03589184, -189.51079802, -0.00072748, -227.46692595, -0.01340453, -22.74669259, -0.03589184, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24036, 4036, 0.0, 258.73909331, 0.01454962, 258.73909331, 0.04364886, 181.11736532, -3892.7874795, 0.05, 2, 0, 74015, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44036, 64.68477333, 6.327e-05, 194.05431998, 0.00018981, 646.84773328, 0.00063269, -64.68477333, -6.327e-05, -194.05431998, -0.00018981, -646.84773328, -0.00063269, 0.4, 0.3, 0.003, 0.0, 0.0, 24036, 2)
    ops.limitCurve('ThreePoint', 14036, 4036, 0.0, 258.73909331, 0.01454962, 258.73909331, 0.04364886, 181.11736532, -3892.7874795, 0.05, 2, 0, 74015, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34036, 64.68477333, 6.327e-05, 194.05431998, 0.00018981, 646.84773328, 0.00063269, -64.68477333, -6.327e-05, -194.05431998, -0.00018981, -646.84773328, -0.00063269, 0.4, 0.3, 0.003, 0.0, 0.0, 14036, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4036, 99999, 'P', 44036, 'Vy', 34036, 'Vz', 24036, 'My', 14036, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174015, 74015, 174015, 4036, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4036, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.55, 0.0, 3.35)
    ops.node(124016, 9.55, 0.0, 4.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4037, 171003, 124016, 0.16, 28376587.9715132, 11823578.32146383, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24037, 222.3714755, 0.00073035, 266.54751718, 0.01367049, 26.65475172, 0.03655026, -222.3714755, -0.00073035, -266.54751718, -0.01367049, -26.65475172, -0.03655026, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14037, 195.80230696, 0.00073035, 234.70015055, 0.01367049, 23.47001506, 0.03655026, -195.80230696, -0.00073035, -234.70015055, -0.01367049, -23.47001506, -0.03655026, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24037, 4037, 0.0, 271.45201529, 0.01460693, 271.45201529, 0.04382078, 190.01641071, -4073.81814845, 0.05, 2, 0, 71003, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 44037, 67.86300382, 6.457e-05, 203.58901147, 0.00019371, 678.63003824, 0.00064571, -67.86300382, -6.457e-05, -203.58901147, -0.00019371, -678.63003824, -0.00064571, 0.4, 0.3, 0.003, 0.0, 0.0, 24037, 2)
    ops.limitCurve('ThreePoint', 14037, 4037, 0.0, 271.45201529, 0.01460693, 271.45201529, 0.04382078, 190.01641071, -4073.81814845, 0.05, 2, 0, 71003, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 34037, 67.86300382, 6.457e-05, 203.58901147, 0.00019371, 678.63003824, 0.00064571, -67.86300382, -6.457e-05, -203.58901147, -0.00019371, -678.63003824, -0.00064571, 0.4, 0.3, 0.003, 0.0, 0.0, 14037, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4037, 99999, 'P', 44037, 'Vy', 34037, 'Vz', 24037, 'My', 14037, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4037, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 4037, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174016, 9.55, 0.0, 4.675)
    ops.node(122003, 9.55, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4038, 174016, 122003, 0.16, 27810862.23994924, 11587859.26664552, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24038, 218.7477347, 0.00072541, 262.55887026, 0.01382898, 26.25588703, 0.03665606, -218.7477347, -0.00072541, -262.55887026, -0.01382898, -26.25588703, -0.03665606, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14038, 191.22002056, 0.00072541, 229.51786284, 0.01382898, 22.95178628, 0.03665606, -191.22002056, -0.00072541, -229.51786284, -0.01382898, -22.95178628, -0.03665606, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24038, 4038, 0.0, 264.20640827, 0.01450818, 264.20640827, 0.04352454, 184.94448579, -4063.9129521, 0.05, 2, 0, 74016, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44038, 66.05160207, 6.413e-05, 198.1548062, 0.00019238, 660.51602067, 0.00064126, -66.05160207, -6.413e-05, -198.1548062, -0.00019238, -660.51602067, -0.00064126, 0.4, 0.3, 0.003, 0.0, 0.0, 24038, 2)
    ops.limitCurve('ThreePoint', 14038, 4038, 0.0, 264.20640827, 0.01450818, 264.20640827, 0.04352454, 184.94448579, -4063.9129521, 0.05, 2, 0, 74016, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34038, 66.05160207, 6.413e-05, 198.1548062, 0.00019238, 660.51602067, 0.00064126, -66.05160207, -6.413e-05, -198.1548062, -0.00019238, -660.51602067, -0.00064126, 0.4, 0.3, 0.003, 0.0, 0.0, 14038, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4038, 99999, 'P', 44038, 'Vy', 34038, 'Vz', 24038, 'My', 14038, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174016, 74016, 174016, 4038, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4038, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 6.7, 0.0, 6.35)
    ops.node(124017, 6.7, 0.0, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4040, 172002, 124017, 0.1225, 29172134.69635449, 12155056.12348104, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24040, 135.70965388, 0.00077081, 163.04287781, 0.01460733, 16.30428778, 0.0431959, -135.70965388, -0.00077081, -163.04287781, -0.01460733, -16.30428778, -0.0431959, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14040, 125.41683929, 0.00077081, 150.67699179, 0.01460733, 15.06769918, 0.0431959, -125.41683929, -0.00077081, -150.67699179, -0.01460733, -15.06769918, -0.0431959, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24040, 4040, 0.0, 190.17728271, 0.01541629, 190.17728271, 0.04624887, 133.1240979, -3204.54026307, 0.05, 2, 0, 72002, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44040, 47.54432068, 5.747e-05, 142.63296203, 0.00017242, 475.44320677, 0.00057475, -47.54432068, -5.747e-05, -142.63296203, -0.00017242, -475.44320677, -0.00057475, 0.4, 0.3, 0.003, 0.0, 0.0, 24040, 2)
    ops.limitCurve('ThreePoint', 14040, 4040, 0.0, 190.17728271, 0.01541629, 190.17728271, 0.04624887, 133.1240979, -3204.54026307, 0.05, 2, 0, 72002, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34040, 47.54432068, 5.747e-05, 142.63296203, 0.00017242, 475.44320677, 0.00057475, -47.54432068, -5.747e-05, -142.63296203, -0.00017242, -475.44320677, -0.00057475, 0.4, 0.3, 0.003, 0.0, 0.0, 14040, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4040, 99999, 'P', 44040, 'Vy', 34040, 'Vz', 24040, 'My', 14040, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4040, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4040, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 6.7, 0.0, 7.7)
    ops.node(123002, 6.7, 0.0, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 174017, 123002, 0.1225, 27828952.93729831, 11595397.05720763, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 130.4449051, 0.00076419, 157.15160068, 0.01515042, 15.71516007, 0.04310859, -130.4449051, -0.00076419, -157.15160068, -0.01515042, -15.71516007, -0.04310859, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 119.8008403, 0.00076419, 144.32831856, 0.01515042, 14.43283186, 0.04310859, -119.8008403, -0.00076419, -144.32831856, -0.01515042, -14.43283186, -0.04310859, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 180.12812851, 0.0152839, 180.12812851, 0.04585169, 126.08968995, -3222.35117504, 0.05, 2, 0, 74017, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 45.03203213, 5.707e-05, 135.09609638, 0.0001712, 450.32032127, 0.00057065, -45.03203213, -5.707e-05, -135.09609638, -0.0001712, -450.32032127, -0.00057065, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 180.12812851, 0.0152839, 180.12812851, 0.04585169, 126.08968995, -3222.35117504, 0.05, 2, 0, 74017, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 45.03203213, 5.707e-05, 135.09609638, 0.0001712, 450.32032127, 0.00057065, -45.03203213, -5.707e-05, -135.09609638, -0.0001712, -450.32032127, -0.00057065, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.55, 0.0, 6.35)
    ops.node(124018, 9.55, 0.0, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 172003, 124018, 0.1225, 26602686.18153297, 11084452.57563874, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 137.31134809, 0.00079371, 165.10221819, 0.01429637, 16.51022182, 0.03850869, -137.31134809, -0.00079371, -165.10221819, -0.01429637, -16.51022182, -0.03850869, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 126.17889319, 0.00079371, 151.71663118, 0.01429637, 15.17166312, 0.03850869, -126.17889319, -0.00079371, -151.71663118, -0.01429637, -15.17166312, -0.03850869, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 176.66243291, 0.01587429, 176.66243291, 0.04762286, 123.66370304, -3255.49336093, 0.05, 2, 0, 72003, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 44.16560823, 5.855e-05, 132.49682468, 0.00017564, 441.65608227, 0.00058547, -44.16560823, -5.855e-05, -132.49682468, -0.00017564, -441.65608227, -0.00058547, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 176.66243291, 0.01587429, 176.66243291, 0.04762286, 123.66370304, -3255.49336093, 0.05, 2, 0, 72003, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 44.16560823, 5.855e-05, 132.49682468, 0.00017564, 441.65608227, 0.00058547, -44.16560823, -5.855e-05, -132.49682468, -0.00017564, -441.65608227, -0.00058547, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 9.55, 0.0, 7.7)
    ops.node(123003, 9.55, 0.0, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 174018, 123003, 0.1225, 27453647.18005611, 11439019.65835671, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 128.45239066, 0.00077659, 154.77617169, 0.01520013, 15.47761717, 0.04253867, -128.45239066, -0.00077659, -154.77617169, -0.01520013, -15.47761717, -0.04253867, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 118.37053915, 0.00077659, 142.6282438, 0.01520013, 14.26282438, 0.04253867, -118.37053915, -0.00077659, -142.6282438, -0.01520013, -14.26282438, -0.04253867, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 177.77995719, 0.01553171, 177.77995719, 0.04659512, 124.44597003, -3208.61417534, 0.05, 2, 0, 74018, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 44.4449893, 5.709e-05, 133.33496789, 0.00017127, 444.44989297, 0.00057091, -44.4449893, -5.709e-05, -133.33496789, -0.00017127, -444.44989297, -0.00057091, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 177.77995719, 0.01553171, 177.77995719, 0.04659512, 124.44597003, -3208.61417534, 0.05, 2, 0, 74018, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 44.4449893, 5.709e-05, 133.33496789, 0.00017127, 444.44989297, 0.00057091, -44.4449893, -5.709e-05, -133.33496789, -0.00017127, -444.44989297, -0.00057091, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 6.7, 0.0, 9.35)
    ops.node(124019, 6.7, 0.0, 10.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4045, 173002, 124019, 0.1225, 28615495.08058058, 11923122.95024191, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24045, 103.78795856, 0.00072087, 125.99127494, 0.01714114, 12.59912749, 0.05437628, -103.78795856, -0.00072087, -125.99127494, -0.01714114, -12.59912749, -0.05437628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14045, 93.81124347, 0.00072087, 113.88024519, 0.01714114, 11.38802452, 0.05437628, -93.81124347, -0.00072087, -113.88024519, -0.01714114, -11.38802452, -0.05437628, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24045, 4045, 0.0, 162.04327208, 0.01441735, 162.04327208, 0.04325205, 113.43029046, -3267.10878122, 0.05, 2, 0, 73002, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44045, 40.51081802, 4.992e-05, 121.53245406, 0.00014977, 405.10818021, 0.00049925, -40.51081802, -4.992e-05, -121.53245406, -0.00014977, -405.10818021, -0.00049925, 0.4, 0.3, 0.003, 0.0, 0.0, 24045, 2)
    ops.limitCurve('ThreePoint', 14045, 4045, 0.0, 162.04327208, 0.01441735, 162.04327208, 0.04325205, 113.43029046, -3267.10878122, 0.05, 2, 0, 73002, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34045, 40.51081802, 4.992e-05, 121.53245406, 0.00014977, 405.10818021, 0.00049925, -40.51081802, -4.992e-05, -121.53245406, -0.00014977, -405.10818021, -0.00049925, 0.4, 0.3, 0.003, 0.0, 0.0, 14045, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4045, 99999, 'P', 44045, 'Vy', 34045, 'Vz', 24045, 'My', 14045, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4045, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4045, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 6.7, 0.0, 10.675)
    ops.node(124002, 6.7, 0.0, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 174019, 124002, 0.1225, 27539782.31906125, 11474909.29960885, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 98.48205186, 0.00072657, 119.9988331, 0.01781569, 11.99988331, 0.05621027, -98.48205186, -0.00072657, -119.9988331, -0.01781569, -11.99988331, -0.05621027, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 88.51970417, 0.00072657, 107.85986893, 0.01781569, 10.78598689, 0.05621027, -88.51970417, -0.00072657, -107.85986893, -0.01781569, -10.78598689, -0.05621027, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 151.73762491, 0.0145315, 151.73762491, 0.04359449, 106.21633744, -3611.77980318, 0.05, 2, 0, 74019, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 37.93440623, 4.858e-05, 113.80321868, 0.00014573, 379.34406228, 0.00048576, -37.93440623, -4.858e-05, -113.80321868, -0.00014573, -379.34406228, -0.00048576, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 151.73762491, 0.0145315, 151.73762491, 0.04359449, 106.21633744, -3611.77980318, 0.05, 2, 0, 74019, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 37.93440623, 4.858e-05, 113.80321868, 0.00014573, 379.34406228, 0.00048576, -37.93440623, -4.858e-05, -113.80321868, -0.00014573, -379.34406228, -0.00048576, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.55, 0.0, 9.35)
    ops.node(124020, 9.55, 0.0, 10.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 173003, 124020, 0.1225, 26181098.34604938, 10908790.97752057, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 105.95594929, 0.0007401, 129.07722933, 0.01717374, 12.90772293, 0.05195623, -105.95594929, -0.0007401, -129.07722933, -0.01717374, -12.90772293, -0.05195623, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 95.16529762, 0.0007401, 115.93188516, 0.01717374, 11.59318852, 0.05195623, -95.16529762, -0.0007401, -115.93188516, -0.01717374, -11.59318852, -0.05195623, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 148.69423532, 0.0148019, 148.69423532, 0.0444057, 104.08596473, -3215.18484078, 0.05, 2, 0, 73003, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 37.17355883, 5.007e-05, 111.52067649, 0.00015022, 371.73558831, 0.00050072, -37.17355883, -5.007e-05, -111.52067649, -0.00015022, -371.73558831, -0.00050072, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 148.69423532, 0.0148019, 148.69423532, 0.0444057, 104.08596473, -3215.18484078, 0.05, 2, 0, 73003, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 37.17355883, 5.007e-05, 111.52067649, 0.00015022, 371.73558831, 0.00050072, -37.17355883, -5.007e-05, -111.52067649, -0.00015022, -371.73558831, -0.00050072, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 9.55, 0.0, 10.675)
    ops.node(124003, 9.55, 0.0, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 174020, 124003, 0.1225, 27173540.72653969, 11322308.6360582, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 97.66647488, 0.00072514, 119.07824611, 0.01783374, 11.90782461, 0.05593706, -97.66647488, -0.00072514, -119.07824611, -0.01783374, -11.90782461, -0.05593706, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 87.78178713, 0.00072514, 107.02650285, 0.01783374, 10.70265028, 0.05593706, -87.78178713, -0.00072514, -107.02650285, -0.01783374, -10.70265028, -0.05593706, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 149.86798995, 0.01450277, 149.86798995, 0.0435083, 104.90759297, -3613.52798653, 0.05, 2, 0, 74020, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 37.46699749, 4.862e-05, 112.40099247, 0.00014587, 374.66997489, 0.00048624, -37.46699749, -4.862e-05, -112.40099247, -0.00014587, -374.66997489, -0.00048624, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 149.86798995, 0.01450277, 149.86798995, 0.0435083, 104.90759297, -3613.52798653, 0.05, 2, 0, 74020, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 37.46699749, 4.862e-05, 112.40099247, 0.00014587, 374.66997489, 0.00048624, -37.46699749, -4.862e-05, -112.40099247, -0.00014587, -374.66997489, -0.00048624, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4048, '-orient', 0, 0, 1, 0, 1, 0)
