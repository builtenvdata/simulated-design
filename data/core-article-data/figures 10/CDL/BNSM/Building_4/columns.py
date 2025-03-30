import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 26205772.19626042, 10919071.74844184, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 73.42553957, 0.00085513, 87.21350487, 0.01488295, 8.72135049, 0.03584834, -73.42553957, -0.00085513, -87.21350487, -0.01488295, -8.72135049, -0.03584834, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 80.0325544, 0.00085513, 95.06119552, 0.01488295, 9.50611955, 0.03584834, -80.0325544, -0.00085513, -95.06119552, -0.01488295, -9.50611955, -0.03584834, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 102.40215103, 0.01710251, 102.40215103, 0.05130753, 71.68150572, -1237.39512459, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 25.60053776, 9.691e-05, 76.80161327, 0.00029073, 256.00537757, 0.00096909, -25.60053776, -9.691e-05, -76.80161327, -0.00029073, -256.00537757, -0.00096909, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 102.40215103, 0.01710251, 102.40215103, 0.05130753, 71.68150572, -1237.39512459, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 25.60053776, 9.691e-05, 76.80161327, 0.00029073, 256.00537757, 0.00096909, -25.60053776, -9.691e-05, -76.80161327, -0.00029073, -256.00537757, -0.00096909, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.5, 0.0, 0.0)
    ops.node(121002, 4.5, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.16, 28042426.02505859, 11684344.17710775, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 198.31627076, 0.00069262, 236.57835026, 0.0136671, 23.65783503, 0.02978978, -198.31627076, -0.00069262, -236.57835026, -0.0136671, -23.65783503, -0.02978978, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 226.12950056, 0.00069262, 269.75771569, 0.0136671, 26.97577157, 0.02978978, -226.12950056, -0.00069262, -269.75771569, -0.0136671, -26.97577157, -0.02978978, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 158.01450738, 0.01385248, 158.01450738, 0.04155743, 110.61015516, -1549.88939632, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 39.50362684, 7.861e-05, 118.51088053, 0.00023582, 395.03626844, 0.00078606, -39.50362684, -7.861e-05, -118.51088053, -0.00023582, -395.03626844, -0.00078606, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 158.01450738, 0.01385248, 158.01450738, 0.04155743, 110.61015516, -1549.88939632, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 39.50362684, 7.861e-05, 118.51088053, 0.00023582, 395.03626844, 0.00078606, -39.50362684, -7.861e-05, -118.51088053, -0.00023582, -395.03626844, -0.00078606, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.5, 0.0, 0.0)
    ops.node(121005, 16.5, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.16, 26472866.54226427, 11030361.05927678, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 196.5928991, 0.00071091, 234.12212851, 0.01282306, 23.41221285, 0.02654533, -196.5928991, -0.00071091, -234.12212851, -0.01282306, -23.41221285, -0.02654533, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 224.1863606, 0.00071091, 266.98313197, 0.01282306, 26.6983132, 0.02654533, -224.1863606, -0.00071091, -266.98313197, -0.01282306, -26.6983132, -0.02654533, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 149.95164039, 0.01421815, 149.95164039, 0.04265445, 104.96614827, -1551.11885865, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 37.4879101, 7.902e-05, 112.46373029, 0.00023705, 374.87910097, 0.00079018, -37.4879101, -7.902e-05, -112.46373029, -0.00023705, -374.87910097, -0.00079018, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 149.95164039, 0.01421815, 149.95164039, 0.04265445, 104.96614827, -1551.11885865, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 37.4879101, 7.902e-05, 112.46373029, 0.00023705, 374.87910097, 0.00079018, -37.4879101, -7.902e-05, -112.46373029, -0.00023705, -374.87910097, -0.00079018, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 21.0, 0.0, 0.0)
    ops.node(121006, 21.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.09, 26165474.20814762, 10902280.92006151, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 73.35921113, 0.0008264, 87.12694702, 0.01474475, 8.7126947, 0.03560064, -73.35921113, -0.0008264, -87.12694702, -0.01474475, -8.7126947, -0.03560064, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 80.44608868, 0.0008264, 95.54385875, 0.01474475, 9.55438587, 0.03560064, -80.44608868, -0.0008264, -95.54385875, -0.01474475, -9.55438587, -0.03560064, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 102.17379742, 0.01652791, 102.17379742, 0.04958374, 71.5216582, -1235.15382788, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 25.54344936, 9.684e-05, 76.63034807, 0.00029053, 255.43449356, 0.00096842, -25.54344936, -9.684e-05, -76.63034807, -0.00029053, -255.43449356, -0.00096842, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 102.17379742, 0.01652791, 102.17379742, 0.04958374, 71.5216582, -1235.15382788, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 25.54344936, 9.684e-05, 76.63034807, 0.00029053, 255.43449356, 0.00096842, -25.54344936, -9.684e-05, -76.63034807, -0.00029053, -255.43449356, -0.00096842, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.5, 0.0)
    ops.node(121007, 0.0, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.16, 26059655.72111316, 10858189.88379715, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 210.58567367, 0.00069293, 250.5420933, 0.01422943, 25.05420933, 0.02979862, -210.58567367, -0.00069293, -250.5420933, -0.01422943, -25.05420933, -0.02979862, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 210.58567367, 0.00069293, 250.5420933, 0.01422943, 25.05420933, 0.02979862, -210.58567367, -0.00069293, -250.5420933, -0.01422943, -25.05420933, -0.02979862, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 156.10280463, 0.01385853, 156.10280463, 0.04157559, 109.27196324, -1700.94718461, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 39.02570116, 8.356e-05, 117.07710347, 0.00025069, 390.25701156, 0.00083563, -39.02570116, -8.356e-05, -117.07710347, -0.00025069, -390.25701156, -0.00083563, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 156.10280463, 0.01385853, 156.10280463, 0.04157559, 109.27196324, -1700.94718461, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 39.02570116, 8.356e-05, 117.07710347, 0.00025069, 390.25701156, 0.00083563, -39.02570116, -8.356e-05, -117.07710347, -0.00025069, -390.25701156, -0.00083563, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.5, 4.5, 0.0)
    ops.node(121008, 4.5, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.25, 26835964.15260701, 11181651.73025292, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 504.61137495, 0.00063092, 603.41789597, 0.02966845, 60.3417896, 0.05638088, -504.61137495, -0.00063092, -603.41789597, -0.02966845, -60.3417896, -0.05638088, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 524.4142615, 0.00063092, 627.09832953, 0.02966845, 62.70983295, 0.05638088, -524.4142615, -0.00063092, -627.09832953, -0.02966845, -62.70983295, -0.05638088, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 279.39767379, 0.01261848, 279.39767379, 0.03785543, 195.57837165, -3079.62123988, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 69.84941845, 9.295e-05, 209.54825534, 0.00027886, 698.49418448, 0.00092952, -69.84941845, -9.295e-05, -209.54825534, -0.00027886, -698.49418448, -0.00092952, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 279.39767379, 0.01261848, 279.39767379, 0.03785543, 195.57837165, -3079.62123988, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 69.84941845, 9.295e-05, 209.54825534, 0.00027886, 698.49418448, 0.00092952, -69.84941845, -9.295e-05, -209.54825534, -0.00027886, -698.49418448, -0.00092952, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.0, 4.5, 0.0)
    ops.node(121009, 9.0, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.25, 27308667.9774602, 11378611.65727508, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 466.43957983, 0.000607, 559.57784469, 0.0308235, 55.95778447, 0.06121517, -466.43957983, -0.000607, -559.57784469, -0.0308235, -55.95778447, -0.06121517, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 466.43957983, 0.000607, 559.57784469, 0.0308235, 55.95778447, 0.06121517, -466.43957983, -0.000607, -559.57784469, -0.0308235, -55.95778447, -0.06121517, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 275.42108371, 0.01213999, 275.42108371, 0.03641998, 192.7947586, -2928.5091513, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 68.85527093, 9.004e-05, 206.56581278, 0.00027013, 688.55270928, 0.00090043, -68.85527093, -9.004e-05, -206.56581278, -0.00027013, -688.55270928, -0.00090043, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 275.42108371, 0.01213999, 275.42108371, 0.03641998, 192.7947586, -2928.5091513, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 68.85527093, 9.004e-05, 206.56581278, 0.00027013, 688.55270928, 0.00090043, -68.85527093, -9.004e-05, -206.56581278, -0.00027013, -688.55270928, -0.00090043, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.0, 4.5, 0.0)
    ops.node(121010, 12.0, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.25, 26965580.46831044, 11235658.52846268, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 464.38576334, 0.00061219, 557.03917033, 0.03082299, 55.70391703, 0.06038, -464.38576334, -0.00061219, -557.03917033, -0.03082299, -55.70391703, -0.06038, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 464.38576334, 0.00061219, 557.03917033, 0.03082299, 55.70391703, 0.06038, -464.38576334, -0.00061219, -557.03917033, -0.03082299, -55.70391703, -0.06038, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 274.58671471, 0.01224376, 274.58671471, 0.03673127, 192.2107003, -2970.40531745, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 68.64667868, 9.091e-05, 205.94003603, 0.00027274, 686.46678678, 0.00090913, -68.64667868, -9.091e-05, -205.94003603, -0.00027274, -686.46678678, -0.00090913, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 274.58671471, 0.01224376, 274.58671471, 0.03673127, 192.2107003, -2970.40531745, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 68.64667868, 9.091e-05, 205.94003603, 0.00027274, 686.46678678, 0.00090913, -68.64667868, -9.091e-05, -205.94003603, -0.00027274, -686.46678678, -0.00090913, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 16.5, 4.5, 0.0)
    ops.node(121011, 16.5, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.25, 26108754.02658393, 10878647.51107664, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 501.23218408, 0.00062641, 598.84024859, 0.02877693, 59.88402486, 0.05357366, -501.23218408, -0.00062641, -598.84024859, -0.02877693, -59.88402486, -0.05357366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 521.25305687, 0.00062641, 622.7599106, 0.02877693, 62.27599106, 0.05357366, -521.25305687, -0.00062641, -622.7599106, -0.02877693, -62.27599106, -0.05357366, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 272.51949612, 0.01252811, 272.51949612, 0.03758433, 190.76364729, -3058.6533917, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 68.12987403, 9.319e-05, 204.38962209, 0.00027957, 681.29874031, 0.00093189, -68.12987403, -9.319e-05, -204.38962209, -0.00027957, -681.29874031, -0.00093189, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 272.51949612, 0.01252811, 272.51949612, 0.03758433, 190.76364729, -3058.6533917, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 68.12987403, 9.319e-05, 204.38962209, 0.00027957, 681.29874031, 0.00093189, -68.12987403, -9.319e-05, -204.38962209, -0.00027957, -681.29874031, -0.00093189, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 21.0, 4.5, 0.0)
    ops.node(121012, 21.0, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 28258902.30848132, 11774542.62853388, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 214.17324071, 0.00069582, 255.48046792, 0.01576044, 25.54804679, 0.03538669, -214.17324071, -0.00069582, -255.48046792, -0.01576044, -25.54804679, -0.03538669, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 214.17324071, 0.00069582, 255.48046792, 0.01576044, 25.54804679, 0.03538669, -214.17324071, -0.00069582, -255.48046792, -0.01576044, -25.54804679, -0.03538669, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 168.88274888, 0.01391641, 168.88274888, 0.04174922, 118.21792422, -1726.36704524, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 42.22068722, 8.337e-05, 126.66206166, 0.00025011, 422.2068722, 0.00083369, -42.22068722, -8.337e-05, -126.66206166, -0.00025011, -422.2068722, -0.00083369, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 168.88274888, 0.01391641, 168.88274888, 0.04174922, 118.21792422, -1726.36704524, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 42.22068722, 8.337e-05, 126.66206166, 0.00025011, 422.2068722, 0.00083369, -42.22068722, -8.337e-05, -126.66206166, -0.00025011, -422.2068722, -0.00083369, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.2025, 26941623.67242133, 11225676.53017555, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 290.45365633, 0.00063455, 348.16229368, 0.01428038, 34.81622937, 0.03033563, -290.45365633, -0.00063455, -348.16229368, -0.01428038, -34.81622937, -0.03033563, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 290.45365633, 0.00063455, 348.16229368, 0.01428038, 34.81622937, 0.03033563, -290.45365633, -0.00063455, -348.16229368, -0.01428038, -34.81622937, -0.03033563, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 177.51326377, 0.01269097, 177.51326377, 0.0380729, 124.25928464, -1615.71832037, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 44.37831594, 7.262e-05, 133.13494782, 0.00021787, 443.78315941, 0.00072623, -44.37831594, -7.262e-05, -133.13494782, -0.00021787, -443.78315941, -0.00072623, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 177.51326377, 0.01269097, 177.51326377, 0.0380729, 124.25928464, -1615.71832037, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 44.37831594, 7.262e-05, 133.13494782, 0.00021787, 443.78315941, 0.00072623, -44.37831594, -7.262e-05, -133.13494782, -0.00021787, -443.78315941, -0.00072623, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.5, 9.0, 0.0)
    ops.node(121014, 4.5, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.25, 27629569.84973869, 11512320.77072446, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 497.74166514, 0.00060911, 595.52694426, 0.03067257, 59.55269443, 0.0593746, -497.74166514, -0.00060911, -595.52694426, -0.03067257, -59.55269443, -0.0593746, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 517.26649449, 0.00060911, 618.88758046, 0.03067257, 61.88875805, 0.0593746, -517.26649449, -0.00060911, -618.88758046, -0.03067257, -61.88875805, -0.0593746, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 287.3805173, 0.01218225, 287.3805173, 0.03654676, 201.16636211, -3111.13666628, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 71.84512933, 9.286e-05, 215.53538798, 0.00027859, 718.45129326, 0.00092862, -71.84512933, -9.286e-05, -215.53538798, -0.00027859, -718.45129326, -0.00092862, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 287.3805173, 0.01218225, 287.3805173, 0.03654676, 201.16636211, -3111.13666628, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 71.84512933, 9.286e-05, 215.53538798, 0.00027859, 718.45129326, 0.00092862, -71.84512933, -9.286e-05, -215.53538798, -0.00027859, -718.45129326, -0.00092862, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 9.0, 0.0)
    ops.node(121015, 9.0, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.25, 26975146.87914767, 11239644.5329782, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 462.4651402, 0.00061258, 554.70407925, 0.03072906, 55.47040793, 0.0602558, -462.4651402, -0.00061258, -554.70407925, -0.03072906, -55.47040793, -0.0602558, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 462.4651402, 0.00061258, 554.70407925, 0.03072906, 55.47040793, 0.0602558, -462.4651402, -0.00061258, -554.70407925, -0.03072906, -55.47040793, -0.0602558, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 275.91855983, 0.01225155, 275.91855983, 0.03675464, 193.14299188, -2997.41485749, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 68.97963996, 9.132e-05, 206.93891987, 0.00027396, 689.79639957, 0.00091321, -68.97963996, -9.132e-05, -206.93891987, -0.00027396, -689.79639957, -0.00091321, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 275.91855983, 0.01225155, 275.91855983, 0.03675464, 193.14299188, -2997.41485749, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 68.97963996, 9.132e-05, 206.93891987, 0.00027396, 689.79639957, 0.00091321, -68.97963996, -9.132e-05, -206.93891987, -0.00027396, -689.79639957, -0.00091321, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.0, 9.0, 0.0)
    ops.node(121016, 12.0, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.25, 26930419.02995164, 11221007.92914652, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 460.81652927, 0.00060626, 552.71387702, 0.03057643, 55.2713877, 0.05999269, -460.81652927, -0.00060626, -552.71387702, -0.03057643, -55.2713877, -0.05999269, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 460.81652927, 0.00060626, 552.71387702, 0.03057643, 55.2713877, 0.05999269, -460.81652927, -0.00060626, -552.71387702, -0.03057643, -55.2713877, -0.05999269, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 273.48895828, 0.01212525, 273.48895828, 0.03637576, 191.44227079, -2951.92048592, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 68.37223957, 9.067e-05, 205.11671871, 0.000272, 683.72239569, 0.00090667, -68.37223957, -9.067e-05, -205.11671871, -0.000272, -683.72239569, -0.00090667, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 273.48895828, 0.01212525, 273.48895828, 0.03637576, 191.44227079, -2951.92048592, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 68.37223957, 9.067e-05, 205.11671871, 0.000272, 683.72239569, 0.00090667, -68.37223957, -9.067e-05, -205.11671871, -0.000272, -683.72239569, -0.00090667, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 16.5, 9.0, 0.0)
    ops.node(121017, 16.5, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.25, 25843266.05910226, 10768027.52462594, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 507.35225436, 0.00062643, 605.89172504, 0.02868949, 60.5891725, 0.05276608, -507.35225436, -0.00062643, -605.89172504, -0.02868949, -60.5891725, -0.05276608, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 528.05970278, 0.00062643, 630.62103597, 0.02868949, 63.0621036, 0.05276608, -528.05970278, -0.00062643, -630.62103597, -0.02868949, -63.0621036, -0.05276608, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 272.54996715, 0.01252855, 272.54996715, 0.03758566, 190.78497701, -3104.11374234, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 68.13749179, 9.416e-05, 204.41247536, 0.00028247, 681.37491788, 0.00094157, -68.13749179, -9.416e-05, -204.41247536, -0.00028247, -681.37491788, -0.00094157, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 272.54996715, 0.01252855, 272.54996715, 0.03758566, 190.78497701, -3104.11374234, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 68.13749179, 9.416e-05, 204.41247536, 0.00028247, 681.37491788, 0.00094157, -68.13749179, -9.416e-05, -204.41247536, -0.00028247, -681.37491788, -0.00094157, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.2025, 26417473.66669993, 11007280.6944583, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 286.66862012, 0.00066242, 343.48498054, 0.01409932, 34.34849805, 0.02941459, -286.66862012, -0.00066242, -343.48498054, -0.01409932, -34.34849805, -0.02941459, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 286.66862012, 0.00066242, 343.48498054, 0.01409932, 34.34849805, 0.02941459, -286.66862012, -0.00066242, -343.48498054, -0.01409932, -34.34849805, -0.02941459, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 175.18761403, 0.01324838, 175.18761403, 0.03974515, 122.63132982, -1632.7926835, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 43.79690351, 7.309e-05, 131.39071052, 0.00021928, 437.96903506, 0.00073094, -43.79690351, -7.309e-05, -131.39071052, -0.00021928, -437.96903506, -0.00073094, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 175.18761403, 0.01324838, 175.18761403, 0.03974515, 122.63132982, -1632.7926835, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 43.79690351, 7.309e-05, 131.39071052, 0.00021928, 437.96903506, 0.00073094, -43.79690351, -7.309e-05, -131.39071052, -0.00021928, -437.96903506, -0.00073094, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.09, 26570602.29628523, 11071084.29011885, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 78.17611351, 0.00085576, 92.91940919, 0.01491095, 9.29194092, 0.03402713, -78.17611351, -0.00085576, -92.91940919, -0.01491095, -9.29194092, -0.03402713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 78.17611351, 0.00085576, 92.91940919, 0.01491095, 9.29194092, 0.03402713, -78.17611351, -0.00085576, -92.91940919, -0.01491095, -9.29194092, -0.03402713, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 96.89203964, 0.01711513, 96.89203964, 0.05134538, 67.82442775, -1108.58285609, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 24.22300991, 9.044e-05, 72.66902973, 0.00027131, 242.2300991, 0.00090435, -24.22300991, -9.044e-05, -72.66902973, -0.00027131, -242.2300991, -0.00090435, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 96.89203964, 0.01711513, 96.89203964, 0.05134538, 67.82442775, -1108.58285609, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 24.22300991, 9.044e-05, 72.66902973, 0.00027131, 242.2300991, 0.00090435, -24.22300991, -9.044e-05, -72.66902973, -0.00027131, -242.2300991, -0.00090435, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 4.5, 13.5, 0.0)
    ops.node(121020, 4.5, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.2025, 27287013.83597505, 11369589.09832294, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 281.65126263, 0.0006493, 337.69694118, 0.01853766, 33.76969412, 0.03825021, -281.65126263, -0.0006493, -337.69694118, -0.01853766, -33.76969412, -0.03825021, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 302.62580304, 0.0006493, 362.84519748, 0.01853766, 36.28451975, 0.03825021, -302.62580304, -0.0006493, -362.84519748, -0.01853766, -36.28451975, -0.03825021, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 189.83007211, 0.01298595, 189.83007211, 0.03895786, 132.88105048, -1799.82445415, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 47.45751803, 7.668e-05, 142.37255408, 0.00023004, 474.57518028, 0.00076679, -47.45751803, -7.668e-05, -142.37255408, -0.00023004, -474.57518028, -0.00076679, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 189.83007211, 0.01298595, 189.83007211, 0.03895786, 132.88105048, -1799.82445415, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 47.45751803, 7.668e-05, 142.37255408, 0.00023004, 474.57518028, 0.00076679, -47.45751803, -7.668e-05, -142.37255408, -0.00023004, -474.57518028, -0.00076679, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 9.0, 13.5, 0.0)
    ops.node(121021, 9.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.16, 27893067.31273017, 11622111.38030424, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 195.68055929, 0.00069612, 234.15147453, 0.01402077, 23.41514745, 0.03149196, -195.68055929, -0.00069612, -234.15147453, -0.01402077, -23.41514745, -0.03149196, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 204.57327809, 0.00069612, 244.79250718, 0.01402077, 24.47925072, 0.03149196, -204.57327809, -0.00069612, -244.79250718, -0.01402077, -24.47925072, -0.03149196, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 151.1055762, 0.01392238, 151.1055762, 0.04176714, 105.77390334, -1405.11350766, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 37.77639405, 7.557e-05, 113.32918215, 0.00022671, 377.76394051, 0.00075572, -37.77639405, -7.557e-05, -113.32918215, -0.00022671, -377.76394051, -0.00075572, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 151.1055762, 0.01392238, 151.1055762, 0.04176714, 105.77390334, -1405.11350766, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 37.77639405, 7.557e-05, 113.32918215, 0.00022671, 377.76394051, 0.00075572, -37.77639405, -7.557e-05, -113.32918215, -0.00022671, -377.76394051, -0.00075572, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 12.0, 13.5, 0.0)
    ops.node(121022, 12.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.16, 26854750.92851087, 11189479.5535462, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 197.51293957, 0.00069703, 236.20006324, 0.01374677, 23.62000632, 0.02968497, -197.51293957, -0.00069703, -236.20006324, -0.01374677, -23.62000632, -0.02968497, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 206.96335238, 0.00069703, 247.50154106, 0.01374677, 24.75015411, 0.02968497, -206.96335238, -0.00069703, -247.50154106, -0.01374677, -24.75015411, -0.02968497, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 146.70155257, 0.01394068, 146.70155257, 0.04182203, 102.6910868, -1420.58711075, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 36.67538814, 7.621e-05, 110.02616443, 0.00022862, 366.75388143, 0.00076206, -36.67538814, -7.621e-05, -110.02616443, -0.00022862, -366.75388143, -0.00076206, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 146.70155257, 0.01394068, 146.70155257, 0.04182203, 102.6910868, -1420.58711075, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 36.67538814, 7.621e-05, 110.02616443, 0.00022862, 366.75388143, 0.00076206, -36.67538814, -7.621e-05, -110.02616443, -0.00022862, -366.75388143, -0.00076206, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 16.5, 13.5, 0.0)
    ops.node(121023, 16.5, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.2025, 26926101.26402185, 11219208.86000911, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 278.82928334, 0.00063558, 334.2552505, 0.01851113, 33.42552505, 0.03763712, -278.82928334, -0.00063558, -334.2552505, -0.01851113, -33.42552505, -0.03763712, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 300.01683155, 0.00063558, 359.65448099, 0.01851113, 35.9654481, 0.03763712, -300.01683155, -0.00063558, -359.65448099, -0.01851113, -35.9654481, -0.03763712, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 188.02697706, 0.01271159, 188.02697706, 0.03813476, 131.61888394, -1808.7072706, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 47.00674426, 7.697e-05, 141.02023279, 0.00023091, 470.06744264, 0.00076969, -47.00674426, -7.697e-05, -141.02023279, -0.00023091, -470.06744264, -0.00076969, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 188.02697706, 0.01271159, 188.02697706, 0.03813476, 131.61888394, -1808.7072706, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 47.00674426, 7.697e-05, 141.02023279, 0.00023091, 470.06744264, 0.00076969, -47.00674426, -7.697e-05, -141.02023279, -0.00023091, -470.06744264, -0.00076969, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.09, 25940069.81257878, 10808362.42190783, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 77.52362355, 0.00086546, 92.01839514, 0.01484549, 9.20183951, 0.03247085, -77.52362355, -0.00086546, -92.01839514, -0.01484549, -9.20183951, -0.03247085, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 77.52362355, 0.00086546, 92.01839514, 0.01484549, 9.20183951, 0.03247085, -77.52362355, -0.00086546, -92.01839514, -0.01484549, -9.20183951, -0.03247085, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 96.38782106, 0.01730923, 96.38782106, 0.05192769, 67.47147474, -1134.14677878, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 24.09695526, 9.215e-05, 72.29086579, 0.00027645, 240.96955265, 0.00092152, -24.09695526, -9.215e-05, -72.29086579, -0.00027645, -240.96955265, -0.00092152, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 96.38782106, 0.01730923, 96.38782106, 0.05192769, 67.47147474, -1134.14677878, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 24.09695526, 9.215e-05, 72.29086579, 0.00027645, 240.96955265, 0.00092152, -24.09695526, -9.215e-05, -72.29086579, -0.00027645, -240.96955265, -0.00092152, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.35)
    ops.node(122001, 0.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 27233604.07736643, 11347335.03223602, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 61.90304022, 0.00074184, 74.26228801, 0.0175464, 7.4262288, 0.0477599, -61.90304022, -0.00074184, -74.26228801, -0.0175464, -7.4262288, -0.0477599, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 68.66218783, 0.00074184, 82.37093283, 0.0175464, 8.23709328, 0.0477599, -68.66218783, -0.00074184, -82.37093283, -0.0175464, -8.23709328, -0.0477599, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 97.7482825, 0.01483671, 97.7482825, 0.04451012, 68.42379775, -1190.65565323, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 24.43707063, 8.04e-05, 73.31121188, 0.0002412, 244.37070625, 0.00080399, -24.43707063, -8.04e-05, -73.31121188, -0.0002412, -244.37070625, -0.00080399, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 97.7482825, 0.01483671, 97.7482825, 0.04451012, 68.42379775, -1190.65565323, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 24.43707063, 8.04e-05, 73.31121188, 0.0002412, 244.37070625, 0.00080399, -24.43707063, -8.04e-05, -73.31121188, -0.0002412, -244.37070625, -0.00080399, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.5, 0.0, 3.425)
    ops.node(122002, 4.5, 0.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.16, 27891106.0640154, 11621294.19333975, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 143.68040783, 0.00064199, 172.55936672, 0.01403618, 17.25593667, 0.03352155, -143.68040783, -0.00064199, -172.55936672, -0.01403618, -17.25593667, -0.03352155, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 143.68040783, 0.00064199, 172.55936672, 0.01403618, 17.25593667, 0.03352155, -143.68040783, -0.00064199, -172.55936672, -0.01403618, -17.25593667, -0.03352155, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 144.79063361, 0.01283988, 144.79063361, 0.03851964, 101.35344353, -1393.66892905, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 36.1976584, 6.541e-05, 108.59297521, 0.00019623, 361.97658403, 0.0006541, -36.1976584, -6.541e-05, -108.59297521, -0.00019623, -361.97658403, -0.0006541, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 144.79063361, 0.01283988, 144.79063361, 0.03851964, 101.35344353, -1393.66892905, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 36.1976584, 6.541e-05, 108.59297521, 0.00019623, 361.97658403, 0.0006541, -36.1976584, -6.541e-05, -108.59297521, -0.00019623, -361.97658403, -0.0006541, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.5, 0.0, 3.425)
    ops.node(122005, 16.5, 0.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.16, 26347241.14219429, 10978017.14258096, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 145.893018, 0.00064301, 175.14375951, 0.01369687, 17.51437595, 0.03098574, -145.893018, -0.00064301, -175.14375951, -0.01369687, -17.51437595, -0.03098574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 145.893018, 0.00064301, 175.14375951, 0.01369687, 17.51437595, 0.03098574, -145.893018, -0.00064301, -175.14375951, -0.01369687, -17.51437595, -0.03098574, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 137.65439422, 0.01286029, 137.65439422, 0.03858086, 96.35807595, -1403.28155098, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 34.41359855, 6.583e-05, 103.24079566, 0.00019749, 344.13598555, 0.0006583, -34.41359855, -6.583e-05, -103.24079566, -0.00019749, -344.13598555, -0.0006583, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 137.65439422, 0.01286029, 137.65439422, 0.03858086, 96.35807595, -1403.28155098, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 34.41359855, 6.583e-05, 103.24079566, 0.00019749, 344.13598555, 0.0006583, -34.41359855, -6.583e-05, -103.24079566, -0.00019749, -344.13598555, -0.0006583, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 21.0, 0.0, 3.35)
    ops.node(122006, 21.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.09, 24854749.48823403, 10356145.62009751, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 60.96826874, 0.00076439, 72.9396058, 0.01563053, 7.29396058, 0.03957547, -60.96826874, -0.00076439, -72.9396058, -0.01563053, -7.29396058, -0.03957547, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 67.65175461, 0.00076439, 80.93541796, 0.01563053, 8.0935418, 0.03957547, -67.65175461, -0.00076439, -80.93541796, -0.01563053, -8.0935418, -0.03957547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 90.40395385, 0.01528773, 90.40395385, 0.0458632, 63.2827677, -1170.94074249, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 22.60098846, 8.148e-05, 67.80296539, 0.00024443, 226.00988463, 0.00081475, -22.60098846, -8.148e-05, -67.80296539, -0.00024443, -226.00988463, -0.00081475, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 90.40395385, 0.01528773, 90.40395385, 0.0458632, 63.2827677, -1170.94074249, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 22.60098846, 8.148e-05, 67.80296539, 0.00024443, 226.00988463, 0.00081475, -22.60098846, -8.148e-05, -67.80296539, -0.00024443, -226.00988463, -0.00081475, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.425)
    ops.node(122007, 0.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.16, 26337233.32473681, 10973847.21864034, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 144.35392566, 0.00063231, 173.28569205, 0.01565059, 17.32856921, 0.0363382, -144.35392566, -0.00063231, -173.28569205, -0.01565059, -17.32856921, -0.0363382, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 134.99806987, 0.00063231, 162.05471279, 0.01565059, 16.20547128, 0.0363382, -134.99806987, -0.00063231, -162.05471279, -0.01565059, -16.20547128, -0.0363382, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 146.4858253, 0.01264629, 146.4858253, 0.03793888, 102.54007771, -1590.35206645, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 36.62145632, 7.008e-05, 109.86436897, 0.00021024, 366.21456324, 0.0007008, -36.62145632, -7.008e-05, -109.86436897, -0.00021024, -366.21456324, -0.0007008, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 146.4858253, 0.01264629, 146.4858253, 0.03793888, 102.54007771, -1590.35206645, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 36.62145632, 7.008e-05, 109.86436897, 0.00021024, 366.21456324, 0.0007008, -36.62145632, -7.008e-05, -109.86436897, -0.00021024, -366.21456324, -0.0007008, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.5, 4.5, 3.425)
    ops.node(122008, 4.5, 4.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.25, 27355811.43813358, 11398254.76588899, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 266.29524347, 0.00055613, 320.52704906, 0.01399599, 32.05270491, 0.03162794, -266.29524347, -0.00055613, -320.52704906, -0.01399599, -32.05270491, -0.03162794, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 248.77793856, 0.00055613, 299.44229375, 0.01399599, 29.94422938, 0.03162794, -248.77793856, -0.00055613, -299.44229375, -0.01399599, -29.94422938, -0.03162794, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 233.5641499, 0.01112259, 233.5641499, 0.03336777, 163.49490493, -1873.6805577, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 58.39103747, 6.885e-05, 175.17311242, 0.00020655, 583.91037475, 0.00068851, -58.39103747, -6.885e-05, -175.17311242, -0.00020655, -583.91037475, -0.00068851, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 233.5641499, 0.01112259, 233.5641499, 0.03336777, 163.49490493, -1873.6805577, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 58.39103747, 6.885e-05, 175.17311242, 0.00020655, 583.91037475, 0.00068851, -58.39103747, -6.885e-05, -175.17311242, -0.00020655, -583.91037475, -0.00068851, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.0, 4.5, 3.425)
    ops.node(122009, 9.0, 4.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.25, 26854801.90912285, 11189500.79546786, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 246.43758937, 0.00055185, 297.32671854, 0.01462785, 29.73267185, 0.03290012, -246.43758937, -0.00055185, -297.32671854, -0.01462785, -29.73267185, -0.03290012, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 229.76854894, 0.00055185, 277.21553702, 0.01462785, 27.7215537, 0.03290012, -229.76854894, -0.00055185, -277.21553702, -0.01462785, -27.7215537, -0.03290012, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 222.81677156, 0.01103698, 222.81677156, 0.03311094, 155.97174009, -1740.72616668, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 55.70419289, 6.691e-05, 167.11257867, 0.00020072, 557.04192891, 0.00066908, -55.70419289, -6.691e-05, -167.11257867, -0.00020072, -557.04192891, -0.00066908, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 222.81677156, 0.01103698, 222.81677156, 0.03311094, 155.97174009, -1740.72616668, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 55.70419289, 6.691e-05, 167.11257867, 0.00020072, 557.04192891, 0.00066908, -55.70419289, -6.691e-05, -167.11257867, -0.00020072, -557.04192891, -0.00066908, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.0, 4.5, 3.425)
    ops.node(122010, 12.0, 4.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.25, 28040559.15407874, 11683566.31419948, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 250.13460961, 0.00054874, 301.62187507, 0.01437937, 30.16218751, 0.03394374, -250.13460961, -0.00054874, -301.62187507, -0.01437937, -30.16218751, -0.03394374, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 233.03388619, 0.00054874, 281.001169, 0.01437937, 28.1001169, 0.03394374, -233.03388619, -0.00054874, -281.001169, -0.01437937, -28.1001169, -0.03394374, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 232.05458591, 0.01097472, 232.05458591, 0.03292415, 162.43821014, -1721.3112718, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 58.01364648, 6.674e-05, 174.04093943, 0.00020021, 580.13646478, 0.00066735, -58.01364648, -6.674e-05, -174.04093943, -0.00020021, -580.13646478, -0.00066735, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 232.05458591, 0.01097472, 232.05458591, 0.03292415, 162.43821014, -1721.3112718, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 58.01364648, 6.674e-05, 174.04093943, 0.00020021, 580.13646478, 0.00066735, -58.01364648, -6.674e-05, -174.04093943, -0.00020021, -580.13646478, -0.00066735, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 16.5, 4.5, 3.425)
    ops.node(122011, 16.5, 4.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.25, 26102572.60291864, 10876071.91788276, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 266.55186109, 0.00056484, 320.74861658, 0.01371397, 32.07486166, 0.0297926, -266.55186109, -0.00056484, -320.74861658, -0.01371397, -32.07486166, -0.0297926, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 248.69353455, 0.00056484, 299.25923921, 0.01371397, 29.92592392, 0.0297926, -248.69353455, -0.00056484, -299.25923921, -0.01371397, -29.92592392, -0.0297926, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 223.13885895, 0.01129674, 223.13885895, 0.03389022, 156.19720127, -1881.05391984, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 55.78471474, 6.894e-05, 167.35414421, 0.00020681, 557.84714738, 0.00068935, -55.78471474, -6.894e-05, -167.35414421, -0.00020681, -557.84714738, -0.00068935, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 223.13885895, 0.01129674, 223.13885895, 0.03389022, 156.19720127, -1881.05391984, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 55.78471474, 6.894e-05, 167.35414421, 0.00020681, 557.84714738, 0.00068935, -55.78471474, -6.894e-05, -167.35414421, -0.00020681, -557.84714738, -0.00068935, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.425)
    ops.node(122012, 21.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 28112536.06001035, 11713556.69167098, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 146.44454127, 0.00061967, 175.86178765, 0.01593668, 17.58617876, 0.03963021, -146.44454127, -0.00061967, -175.86178765, -0.01593668, -17.58617876, -0.03963021, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 136.84457857, 0.00061967, 164.33341938, 0.01593668, 16.43334194, 0.03963021, -136.84457857, -0.00061967, -164.33341938, -0.01593668, -16.43334194, -0.03963021, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 154.46155426, 0.0123935, 154.46155426, 0.0371805, 108.12308798, -1573.24898858, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 38.61538857, 6.923e-05, 115.8461657, 0.00020769, 386.15388566, 0.00069229, -38.61538857, -6.923e-05, -115.8461657, -0.00020769, -386.15388566, -0.00069229, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 154.46155426, 0.0123935, 154.46155426, 0.0371805, 108.12308798, -1573.24898858, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 38.61538857, 6.923e-05, 115.8461657, 0.00020769, 386.15388566, 0.00069229, -38.61538857, -6.923e-05, -115.8461657, -0.00020769, -386.15388566, -0.00069229, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.425)
    ops.node(122013, 0.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.2025, 27235374.89790257, 11348072.87412607, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 188.23677022, 0.00058161, 227.03299379, 0.01482044, 22.70329938, 0.03451402, -188.23677022, -0.00058161, -227.03299379, -0.01482044, -22.70329938, -0.03451402, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 178.67493188, 0.00058161, 215.50042882, 0.01482044, 21.55004288, 0.03451402, -178.67493188, -0.00058161, -215.50042882, -0.01482044, -21.55004288, -0.03451402, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 170.76890459, 0.0116322, 170.76890459, 0.03489661, 119.53823321, -1480.55827004, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 42.69222615, 6.242e-05, 128.07667844, 0.00018727, 426.92226148, 0.00062422, -42.69222615, -6.242e-05, -128.07667844, -0.00018727, -426.92226148, -0.00062422, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 170.76890459, 0.0116322, 170.76890459, 0.03489661, 119.53823321, -1480.55827004, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 42.69222615, 6.242e-05, 128.07667844, 0.00018727, 426.92226148, 0.00062422, -42.69222615, -6.242e-05, -128.07667844, -0.00018727, -426.92226148, -0.00062422, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.5, 9.0, 3.425)
    ops.node(122014, 4.5, 9.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.25, 28261072.16301993, 11775446.73459164, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 268.17842148, 0.00055223, 322.67930419, 0.0139778, 32.26793042, 0.0326263, -268.17842148, -0.00055223, -322.67930419, -0.0139778, -32.26793042, -0.0326263, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 250.50381176, 0.00055223, 301.41275062, 0.0139778, 30.14127506, 0.0326263, -250.50381176, -0.00055223, -301.41275062, -0.0139778, -30.14127506, -0.0326263, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 241.59697213, 0.01104456, 241.59697213, 0.03313367, 169.11788049, -1875.51098685, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 60.39924303, 6.894e-05, 181.1977291, 0.00020681, 603.99243033, 0.00068937, -60.39924303, -6.894e-05, -181.1977291, -0.00020681, -603.99243033, -0.00068937, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 241.59697213, 0.01104456, 241.59697213, 0.03313367, 169.11788049, -1875.51098685, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 60.39924303, 6.894e-05, 181.1977291, 0.00020681, 603.99243033, 0.00068937, -60.39924303, -6.894e-05, -181.1977291, -0.00020681, -603.99243033, -0.00068937, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 9.0, 3.425)
    ops.node(122015, 9.0, 9.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.25, 28281314.79391966, 11783881.16413319, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 252.31878335, 0.00054342, 304.16102717, 0.01862179, 30.41610272, 0.04193067, -252.31878335, -0.00054342, -304.16102717, -0.01862179, -30.41610272, -0.04193067, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 234.78424974, 0.00054342, 283.02379084, 0.01862179, 28.30237908, 0.04193067, -234.78424974, -0.00054342, -283.02379084, -0.01862179, -28.30237908, -0.04193067, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 246.18214372, 0.0108683, 246.18214372, 0.0326049, 172.3275006, -1974.1259072, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 61.54553593, 7.02e-05, 184.63660779, 0.00021059, 615.4553593, 0.00070195, -61.54553593, -7.02e-05, -184.63660779, -0.00021059, -615.4553593, -0.00070195, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 246.18214372, 0.0108683, 246.18214372, 0.0326049, 172.3275006, -1974.1259072, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 61.54553593, 7.02e-05, 184.63660779, 0.00021059, 615.4553593, 0.00070195, -61.54553593, -7.02e-05, -184.63660779, -0.00021059, -615.4553593, -0.00070195, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.0, 9.0, 3.425)
    ops.node(122016, 12.0, 9.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.25, 26726912.51378809, 11136213.5474117, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 250.78562339, 0.00055018, 302.53537279, 0.01799088, 30.25353728, 0.03930222, -250.78562339, -0.00055018, -302.53537279, -0.01799088, -30.25353728, -0.03930222, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 233.17378363, 0.00055018, 281.28932035, 0.01799088, 28.12893204, 0.03930222, -233.17378363, -0.00055018, -281.28932035, -0.01799088, -28.12893204, -0.03930222, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 231.51066132, 0.01100355, 231.51066132, 0.03301064, 162.05746292, -1946.11435622, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 57.87766533, 6.985e-05, 173.63299599, 0.00020955, 578.7766533, 0.00069851, -57.87766533, -6.985e-05, -173.63299599, -0.00020955, -578.7766533, -0.00069851, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 231.51066132, 0.01100355, 231.51066132, 0.03301064, 162.05746292, -1946.11435622, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 57.87766533, 6.985e-05, 173.63299599, 0.00020955, 578.7766533, 0.00069851, -57.87766533, -6.985e-05, -173.63299599, -0.00020955, -578.7766533, -0.00069851, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 16.5, 9.0, 3.425)
    ops.node(122017, 16.5, 9.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.25, 27053243.33385048, 11272184.7224377, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 268.25143455, 0.00055287, 322.88776227, 0.01402316, 32.28877623, 0.03129584, -268.25143455, -0.00055287, -322.88776227, -0.01402316, -32.28877623, -0.03129584, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 249.98634603, 0.00055287, 300.90251707, 0.01402316, 30.09025171, 0.03129584, -249.98634603, -0.00055287, -300.90251707, -0.01402316, -30.09025171, -0.03129584, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 231.8167204, 0.01105737, 231.8167204, 0.0331721, 162.27170428, -1891.26844171, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 57.9541801, 6.91e-05, 173.8625403, 0.0002073, 579.541801, 0.000691, -57.9541801, -6.91e-05, -173.8625403, -0.0002073, -579.541801, -0.000691, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 231.8167204, 0.01105737, 231.8167204, 0.0331721, 162.27170428, -1891.26844171, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 57.9541801, 6.91e-05, 173.8625403, 0.0002073, 579.541801, 0.000691, -57.9541801, -6.91e-05, -173.8625403, -0.0002073, -579.541801, -0.000691, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.425)
    ops.node(122018, 21.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.2025, 25624750.62083347, 10676979.42534728, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 185.52035087, 0.00058869, 223.7135831, 0.01414595, 22.37135831, 0.03176947, -185.52035087, -0.00058869, -223.7135831, -0.01414595, -22.37135831, -0.03176947, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 176.11635293, 0.00058869, 212.37357612, 0.01414595, 21.23735761, 0.03176947, -176.11635293, -0.00058869, -212.37357612, -0.01414595, -21.23735761, -0.03176947, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 160.69318689, 0.01177375, 160.69318689, 0.03532126, 112.48523083, -1477.33227069, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 40.17329672, 6.243e-05, 120.51989017, 0.00018729, 401.73296723, 0.00062431, -40.17329672, -6.243e-05, -120.51989017, -0.00018729, -401.73296723, -0.00062431, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 160.69318689, 0.01177375, 160.69318689, 0.03532126, 112.48523083, -1477.33227069, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 40.17329672, 6.243e-05, 120.51989017, 0.00018729, 401.73296723, 0.00062431, -40.17329672, -6.243e-05, -120.51989017, -0.00018729, -401.73296723, -0.00062431, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.35)
    ops.node(122019, 0.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.09, 26463191.30196878, 11026329.70915366, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 64.09305816, 0.00077242, 76.85054326, 0.01724454, 7.68505433, 0.04188851, -64.09305816, -0.00077242, -76.85054326, -0.01724454, -7.68505433, -0.04188851, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 64.09305816, 0.00077242, 76.85054326, 0.01724454, 7.68505433, 0.04188851, -64.09305816, -0.00077242, -76.85054326, -0.01724454, -7.68505433, -0.04188851, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 90.5426593, 0.01544832, 90.5426593, 0.04634495, 63.37986151, -1070.33318999, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 22.63566482, 7.664e-05, 67.90699447, 0.00022992, 226.35664824, 0.00076641, -22.63566482, -7.664e-05, -67.90699447, -0.00022992, -226.35664824, -0.00076641, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 90.5426593, 0.01544832, 90.5426593, 0.04634495, 63.37986151, -1070.33318999, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 22.63566482, 7.664e-05, 67.90699447, 0.00022992, 226.35664824, 0.00076641, -22.63566482, -7.664e-05, -67.90699447, -0.00022992, -226.35664824, -0.00076641, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 4.5, 13.5, 3.425)
    ops.node(122020, 4.5, 13.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.2025, 26821208.68327714, 11175503.61803214, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 187.68670739, 0.00059352, 226.38697538, 0.01441777, 22.63869754, 0.03360158, -187.68670739, -0.00059352, -226.38697538, -0.01441777, -22.63869754, -0.03360158, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 178.37341676, 0.00059352, 215.1533205, 0.01441777, 21.51533205, 0.03360158, -178.37341676, -0.00059352, -215.1533205, -0.01441777, -21.51533205, -0.03360158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 168.11503686, 0.01187037, 168.11503686, 0.03561112, 117.6805258, -1479.02916306, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 42.02875921, 6.24e-05, 126.08627764, 0.0001872, 420.28759214, 0.00062401, -42.02875921, -6.24e-05, -126.08627764, -0.0001872, -420.28759214, -0.00062401, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 168.11503686, 0.01187037, 168.11503686, 0.03561112, 117.6805258, -1479.02916306, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 42.02875921, 6.24e-05, 126.08627764, 0.0001872, 420.28759214, 0.00062401, -42.02875921, -6.24e-05, -126.08627764, -0.0001872, -420.28759214, -0.00062401, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.425)
    ops.node(122021, 9.0, 13.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.16, 26533323.29096138, 11055551.37123391, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 135.9324514, 0.00063027, 163.65284603, 0.01413514, 16.3652846, 0.0331908, -135.9324514, -0.00063027, -163.65284603, -0.01413514, -16.3652846, -0.0331908, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 135.9324514, 0.00063027, 163.65284603, 0.01413514, 16.3652846, 0.0331908, -135.9324514, -0.00063027, -163.65284603, -0.01413514, -16.3652846, -0.0331908, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 133.42894832, 0.01260547, 133.42894832, 0.03781642, 93.40026383, -1281.19615988, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 33.35723708, 6.336e-05, 100.07171124, 0.00019009, 333.57237081, 0.00063362, -33.35723708, -6.336e-05, -100.07171124, -0.00019009, -333.57237081, -0.00063362, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 133.42894832, 0.01260547, 133.42894832, 0.03781642, 93.40026383, -1281.19615988, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 33.35723708, 6.336e-05, 100.07171124, 0.00019009, 333.57237081, 0.00063362, -33.35723708, -6.336e-05, -100.07171124, -0.00019009, -333.57237081, -0.00063362, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.425)
    ops.node(122022, 12.0, 13.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.16, 26487986.70970289, 11036661.12904287, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 134.0756686, 0.00062997, 161.41516977, 0.01431144, 16.14151698, 0.03330245, -134.0756686, -0.00062997, -161.41516977, -0.01431144, -16.14151698, -0.03330245, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 134.0756686, 0.00062997, 161.41516977, 0.01431144, 16.14151698, 0.03330245, -134.0756686, -0.00062997, -161.41516977, -0.01431144, -16.14151698, -0.03330245, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 134.08662119, 0.01259933, 134.08662119, 0.03779798, 93.86063483, -1299.43672549, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 33.5216553, 6.378e-05, 100.56496589, 0.00019135, 335.21655298, 0.00063783, -33.5216553, -6.378e-05, -100.56496589, -0.00019135, -335.21655298, -0.00063783, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 134.08662119, 0.01259933, 134.08662119, 0.03779798, 93.86063483, -1299.43672549, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 33.5216553, 6.378e-05, 100.56496589, 0.00019135, 335.21655298, 0.00063783, -33.5216553, -6.378e-05, -100.56496589, -0.00019135, -335.21655298, -0.00063783, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 16.5, 13.5, 3.425)
    ops.node(122023, 16.5, 13.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.2025, 26546988.5390944, 11061245.22462267, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 185.69947492, 0.000581, 223.99174729, 0.01445755, 22.39917473, 0.03329742, -185.69947492, -0.000581, -223.99174729, -0.01445755, -22.39917473, -0.03329742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 176.37172158, 0.000581, 212.74055893, 0.01445755, 21.27405589, 0.03329742, -176.37172158, -0.000581, -212.74055893, -0.01445755, -21.27405589, -0.03329742, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 166.22209525, 0.01162004, 166.22209525, 0.03486011, 116.35546667, -1474.94603123, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 41.55552381, 6.234e-05, 124.66657144, 0.00018701, 415.55523812, 0.00062336, -41.55552381, -6.234e-05, -124.66657144, -0.00018701, -415.55523812, -0.00062336, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 166.22209525, 0.01162004, 166.22209525, 0.03486011, 116.35546667, -1474.94603123, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 41.55552381, 6.234e-05, 124.66657144, 0.00018701, 415.55523812, 0.00062336, -41.55552381, -6.234e-05, -124.66657144, -0.00018701, -415.55523812, -0.00062336, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.35)
    ops.node(122024, 21.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.09, 26532703.90003129, 11055293.29167971, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 65.64150989, 0.00075295, 78.71169746, 0.01707721, 7.87116975, 0.04187618, -65.64150989, -0.00075295, -78.71169746, -0.01707721, -7.87116975, -0.04187618, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 65.64150989, 0.00075295, 78.71169746, 0.01707721, 7.87116975, 0.04187618, -65.64150989, -0.00075295, -78.71169746, -0.01707721, -7.87116975, -0.04187618, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 90.33950331, 0.01505909, 90.33950331, 0.04517728, 63.23765231, -1061.21777409, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 22.58487583, 7.627e-05, 67.75462748, 0.0002288, 225.84875827, 0.00076268, -22.58487583, -7.627e-05, -67.75462748, -0.0002288, -225.84875827, -0.00076268, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 90.33950331, 0.01505909, 90.33950331, 0.04517728, 63.23765231, -1061.21777409, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 22.58487583, 7.627e-05, 67.75462748, 0.0002288, 225.84875827, 0.00076268, -22.58487583, -7.627e-05, -67.75462748, -0.0002288, -225.84875827, -0.00076268, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.15)
    ops.node(123001, 0.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 26688861.56221139, 11120358.98425475, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 35.44313598, 0.00087253, 42.58956723, 0.01908235, 4.25895672, 0.05434362, -35.44313598, -0.00087253, -42.58956723, -0.01908235, -4.25895672, -0.05434362, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 37.69130414, 0.00087253, 45.29103554, 0.01908235, 4.52910355, 0.05434362, -37.69130414, -0.00087253, -45.29103554, -0.01908235, -4.52910355, -0.05434362, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 70.2968737, 0.01745057, 70.2968737, 0.0523517, 49.20781159, -924.15440757, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 17.57421843, 8.496e-05, 52.72265528, 0.00025488, 175.74218426, 0.0008496, -17.57421843, -8.496e-05, -52.72265528, -0.00025488, -175.74218426, -0.0008496, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 70.2968737, 0.01745057, 70.2968737, 0.0523517, 49.20781159, -924.15440757, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 17.57421843, 8.496e-05, 52.72265528, 0.00025488, 175.74218426, 0.0008496, -17.57421843, -8.496e-05, -52.72265528, -0.00025488, -175.74218426, -0.0008496, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.5, 0.0, 6.175)
    ops.node(123002, 4.5, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1225, 26897834.17970275, 11207430.90820948, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 98.25378543, 0.00068574, 118.36614659, 0.0154662, 11.83661466, 0.03706898, -98.25378543, -0.00068574, -118.36614659, -0.0154662, -11.83661466, -0.03706898, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 98.25378543, 0.00068574, 118.36614659, 0.0154662, 11.83661466, 0.03706898, -98.25378543, -0.00068574, -118.36614659, -0.0154662, -11.83661466, -0.03706898, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 106.66591304, 0.01371483, 106.66591304, 0.04114449, 74.66613913, -1046.91305204, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 26.66647826, 6.526e-05, 79.99943478, 0.00019579, 266.6647826, 0.00065262, -26.66647826, -6.526e-05, -79.99943478, -0.00019579, -266.6647826, -0.00065262, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 106.66591304, 0.01371483, 106.66591304, 0.04114449, 74.66613913, -1046.91305204, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 26.66647826, 6.526e-05, 79.99943478, 0.00019579, 266.6647826, 0.00065262, -26.66647826, -6.526e-05, -79.99943478, -0.00019579, -266.6647826, -0.00065262, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.5, 0.0, 6.175)
    ops.node(123005, 16.5, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 25788174.79244663, 10745072.8301861, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 100.79399468, 0.00069556, 121.38116019, 0.01465874, 12.13811602, 0.03453943, -100.79399468, -0.00069556, -121.38116019, -0.01465874, -12.13811602, -0.03453943, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 100.79399468, 0.00069556, 121.38116019, 0.01465874, 12.13811602, 0.03453943, -100.79399468, -0.00069556, -121.38116019, -0.01465874, -12.13811602, -0.03453943, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 101.7330624, 0.01391111, 101.7330624, 0.04173332, 71.21314368, -1027.7145171, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 25.4332656, 6.492e-05, 76.2997968, 0.00019477, 254.332656, 0.00064923, -25.4332656, -6.492e-05, -76.2997968, -0.00019477, -254.332656, -0.00064923, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 101.7330624, 0.01391111, 101.7330624, 0.04173332, 71.21314368, -1027.7145171, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 25.4332656, 6.492e-05, 76.2997968, 0.00019477, 254.332656, 0.00064923, -25.4332656, -6.492e-05, -76.2997968, -0.00019477, -254.332656, -0.00064923, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 21.0, 0.0, 6.15)
    ops.node(123006, 21.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 27697873.8242552, 11540780.76010633, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 36.29685647, 0.00083767, 43.62143187, 0.01888219, 4.36214319, 0.05687423, -36.29685647, -0.00083767, -43.62143187, -0.01888219, -4.36214319, -0.05687423, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 38.87211381, 0.00083767, 46.7163669, 0.01888219, 4.67163669, 0.05687423, -38.87211381, -0.00083767, -46.7163669, -0.01888219, -4.67163669, -0.05687423, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 70.72100038, 0.01675344, 70.72100038, 0.05026033, 49.50470027, -883.90969552, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 17.6802501, 8.236e-05, 53.04075029, 0.00024708, 176.80250096, 0.00082359, -17.6802501, -8.236e-05, -53.04075029, -0.00024708, -176.80250096, -0.00082359, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 70.72100038, 0.01675344, 70.72100038, 0.05026033, 49.50470027, -883.90969552, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 17.6802501, 8.236e-05, 53.04075029, 0.00024708, 176.80250096, 0.00082359, -17.6802501, -8.236e-05, -53.04075029, -0.00024708, -176.80250096, -0.00082359, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.15)
    ops.node(123007, 0.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 26230690.76793905, 10929454.48664127, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 91.22097871, 0.0006626, 109.87549233, 0.01698477, 10.98754923, 0.04188102, -91.22097871, -0.0006626, -109.87549233, -0.01698477, -10.98754923, -0.04188102, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 87.22116349, 0.0006626, 105.05772263, 0.01698477, 10.50577226, 0.04188102, -87.22116349, -0.0006626, -105.05772263, -0.01698477, -10.50577226, -0.04188102, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 111.41881627, 0.01325207, 111.41881627, 0.0397562, 77.99317139, -1209.4628833, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 27.85470407, 6.99e-05, 83.5641122, 0.00020971, 278.54704067, 0.00069904, -27.85470407, -6.99e-05, -83.5641122, -0.00020971, -278.54704067, -0.00069904, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 111.41881627, 0.01325207, 111.41881627, 0.0397562, 77.99317139, -1209.4628833, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 27.85470407, 6.99e-05, 83.5641122, 0.00020971, 278.54704067, 0.00069904, -27.85470407, -6.99e-05, -83.5641122, -0.00020971, -278.54704067, -0.00069904, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.5, 4.5, 6.175)
    ops.node(123008, 4.5, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.16, 26383840.34136065, 10993266.80890027, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 140.18934422, 0.0006393, 168.51279618, 0.01430521, 16.85127962, 0.03231152, -140.18934422, -0.0006393, -168.51279618, -0.01430521, -16.85127962, -0.03231152, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 140.18934422, 0.0006393, 168.51279618, 0.01430521, 16.85127962, 0.03231152, -140.18934422, -0.0006393, -168.51279618, -0.01430521, -16.85127962, -0.03231152, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 135.62363745, 0.01278599, 135.62363745, 0.03835797, 94.93654621, -1349.70820877, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 33.90590936, 6.477e-05, 101.71772809, 0.00019431, 339.05909362, 0.00064769, -33.90590936, -6.477e-05, -101.71772809, -0.00019431, -339.05909362, -0.00064769, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 135.62363745, 0.01278599, 135.62363745, 0.03835797, 94.93654621, -1349.70820877, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 33.90590936, 6.477e-05, 101.71772809, 0.00019431, 339.05909362, 0.00064769, -33.90590936, -6.477e-05, -101.71772809, -0.00019431, -339.05909362, -0.00064769, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.175)
    ops.node(123009, 9.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.16, 26877483.53855051, 11198951.47439605, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 132.29717418, 0.00062708, 159.48536176, 0.01497137, 15.94853618, 0.03524905, -132.29717418, -0.00062708, -159.48536176, -0.01497137, -15.94853618, -0.03524905, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 132.29717418, 0.00062708, 159.48536176, 0.01497137, 15.94853618, 0.03524905, -132.29717418, -0.00062708, -159.48536176, -0.01497137, -15.94853618, -0.03524905, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 133.66045219, 0.01254158, 133.66045219, 0.03762473, 93.56231653, -1246.51771695, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 33.41511305, 6.266e-05, 100.24533914, 0.00018798, 334.15113047, 0.00062659, -33.41511305, -6.266e-05, -100.24533914, -0.00018798, -334.15113047, -0.00062659, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 133.66045219, 0.01254158, 133.66045219, 0.03762473, 93.56231653, -1246.51771695, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 33.41511305, 6.266e-05, 100.24533914, 0.00018798, 334.15113047, 0.00062659, -33.41511305, -6.266e-05, -100.24533914, -0.00018798, -334.15113047, -0.00062659, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.175)
    ops.node(123010, 12.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.16, 25906703.05202293, 10794459.60500956, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 130.33710541, 0.00063055, 157.0897888, 0.01470644, 15.70897888, 0.03362369, -130.33710541, -0.00063055, -157.0897888, -0.01470644, -15.70897888, -0.03362369, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 130.33710541, 0.00063055, 157.0897888, 0.01470644, 15.70897888, 0.03362369, -130.33710541, -0.00063055, -157.0897888, -0.01470644, -15.70897888, -0.03362369, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 129.69896031, 0.01261096, 129.69896031, 0.03783287, 90.78927222, -1260.25706686, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 32.42474008, 6.308e-05, 97.27422023, 0.00018924, 324.24740078, 0.0006308, -32.42474008, -6.308e-05, -97.27422023, -0.00018924, -324.24740078, -0.0006308, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 129.69896031, 0.01261096, 129.69896031, 0.03783287, 90.78927222, -1260.25706686, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 32.42474008, 6.308e-05, 97.27422023, 0.00018924, 324.24740078, 0.0006308, -32.42474008, -6.308e-05, -97.27422023, -0.00018924, -324.24740078, -0.0006308, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 16.5, 4.5, 6.175)
    ops.node(123011, 16.5, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.16, 25088271.5882031, 10453446.49508462, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 141.08015868, 0.00064096, 169.35965264, 0.01373051, 16.93596526, 0.02971683, -141.08015868, -0.00064096, -169.35965264, -0.01373051, -16.93596526, -0.02971683, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 141.08015868, 0.00064096, 169.35965264, 0.01373051, 16.93596526, 0.02971683, -141.08015868, -0.00064096, -169.35965264, -0.01373051, -16.93596526, -0.02971683, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 130.14005082, 0.01281914, 130.14005082, 0.03845743, 91.09803557, -1364.33569552, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 32.53501271, 6.536e-05, 97.60503812, 0.00019608, 325.35012705, 0.0006536, -32.53501271, -6.536e-05, -97.60503812, -0.00019608, -325.35012705, -0.0006536, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 130.14005082, 0.01281914, 130.14005082, 0.03845743, 91.09803557, -1364.33569552, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 32.53501271, 6.536e-05, 97.60503812, 0.00019608, 325.35012705, 0.0006536, -32.53501271, -6.536e-05, -97.60503812, -0.00019608, -325.35012705, -0.0006536, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.15)
    ops.node(123012, 21.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 26375445.95798659, 10989769.14916108, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 90.67360043, 0.00066932, 109.22186546, 0.016848, 10.92218655, 0.0420173, -90.67360043, -0.00066932, -109.22186546, -0.016848, -10.92218655, -0.0420173, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 86.8277603, 0.00066932, 104.58931715, 0.016848, 10.45893172, 0.0420173, -86.8277603, -0.00066932, -104.58931715, -0.016848, -10.45893172, -0.0420173, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 111.42952369, 0.01338642, 111.42952369, 0.04015925, 78.00066659, -1197.39533793, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 27.85738092, 6.953e-05, 83.57214277, 0.00020858, 278.57380924, 0.00069527, -27.85738092, -6.953e-05, -83.57214277, -0.00020858, -278.57380924, -0.00069527, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 111.42952369, 0.01338642, 111.42952369, 0.04015925, 78.00066659, -1197.39533793, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 27.85738092, 6.953e-05, 83.57214277, 0.00020858, 278.57380924, 0.00069527, -27.85738092, -6.953e-05, -83.57214277, -0.00020858, -278.57380924, -0.00069527, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.15)
    ops.node(123013, 0.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.1225, 27143234.15025897, 11309680.89594124, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 98.15496606, 0.00069344, 118.24189631, 0.01533587, 11.82418963, 0.03727775, -98.15496606, -0.00069344, -118.24189631, -0.01533587, -11.82418963, -0.03727775, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 98.15496606, 0.00069344, 118.24189631, 0.01533587, 11.82418963, 0.03727775, -98.15496606, -0.00069344, -118.24189631, -0.01533587, -11.82418963, -0.03727775, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 107.01449657, 0.01386873, 107.01449657, 0.04160619, 74.9101476, -1034.84558206, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 26.75362414, 6.488e-05, 80.26087243, 0.00019465, 267.53624144, 0.00064884, -26.75362414, -6.488e-05, -80.26087243, -0.00019465, -267.53624144, -0.00064884, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 107.01449657, 0.01386873, 107.01449657, 0.04160619, 74.9101476, -1034.84558206, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 26.75362414, 6.488e-05, 80.26087243, 0.00019465, 267.53624144, 0.00064884, -26.75362414, -6.488e-05, -80.26087243, -0.00019465, -267.53624144, -0.00064884, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.5, 9.0, 6.175)
    ops.node(123014, 4.5, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.16, 27452161.96860532, 11438400.82025222, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 141.4565618, 0.00063311, 170.08062483, 0.01460754, 17.00806248, 0.0341271, -141.4565618, -0.00063311, -170.08062483, -0.01460754, -17.00806248, -0.0341271, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 141.4565618, 0.00063311, 170.08062483, 0.01460754, 17.00806248, 0.0341271, -141.4565618, -0.00063311, -170.08062483, -0.01460754, -17.00806248, -0.0341271, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 141.40884987, 0.01266227, 141.40884987, 0.03798682, 98.98619491, -1361.60343661, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 35.35221247, 6.49e-05, 106.0566374, 0.00019471, 353.52212468, 0.00064904, -35.35221247, -6.49e-05, -106.0566374, -0.00019471, -353.52212468, -0.00064904, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 141.40884987, 0.01266227, 141.40884987, 0.03798682, 98.98619491, -1361.60343661, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 35.35221247, 6.49e-05, 106.0566374, 0.00019471, 353.52212468, 0.00064904, -35.35221247, -6.49e-05, -106.0566374, -0.00019471, -353.52212468, -0.00064904, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.175)
    ops.node(123015, 9.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.16, 26789130.55022599, 11162137.72926083, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 130.85338713, 0.00061667, 157.69315045, 0.0149444, 15.76931505, 0.03490509, -130.85338713, -0.00061667, -157.69315045, -0.0149444, -15.76931505, -0.03490509, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 130.85338713, 0.00061667, 157.69315045, 0.0149444, 15.76931505, 0.03490509, -130.85338713, -0.00061667, -157.69315045, -0.0149444, -15.76931505, -0.03490509, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 133.68674959, 0.01233339, 133.68674959, 0.03700018, 93.58072472, -1257.03609884, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 33.4216874, 6.288e-05, 100.2650622, 0.00018863, 334.21687399, 0.00062878, -33.4216874, -6.288e-05, -100.2650622, -0.00018863, -334.21687399, -0.00062878, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 133.68674959, 0.01233339, 133.68674959, 0.03700018, 93.58072472, -1257.03609884, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 33.4216874, 6.288e-05, 100.2650622, 0.00018863, 334.21687399, 0.00062878, -33.4216874, -6.288e-05, -100.2650622, -0.00018863, -334.21687399, -0.00062878, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.175)
    ops.node(123016, 12.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.16, 26687389.72910357, 11119745.72045982, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 132.67550507, 0.00062704, 159.88812743, 0.01499116, 15.98881274, 0.03481269, -132.67550507, -0.00062704, -159.88812743, -0.01499116, -15.98881274, -0.03481269, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 132.67550507, 0.00062704, 159.88812743, 0.01499116, 15.98881274, 0.03481269, -132.67550507, -0.00062704, -159.88812743, -0.01499116, -15.98881274, -0.03481269, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 133.54639902, 0.01254082, 133.54639902, 0.03762245, 93.48247931, -1264.35522435, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 33.38659975, 6.305e-05, 100.15979926, 0.00018916, 333.86599754, 0.00063052, -33.38659975, -6.305e-05, -100.15979926, -0.00018916, -333.86599754, -0.00063052, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 133.54639902, 0.01254082, 133.54639902, 0.03762245, 93.48247931, -1264.35522435, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 33.38659975, 6.305e-05, 100.15979926, 0.00018916, 333.86599754, 0.00063052, -33.38659975, -6.305e-05, -100.15979926, -0.00018916, -333.86599754, -0.00063052, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 16.5, 9.0, 6.175)
    ops.node(123017, 16.5, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.16, 27361088.28677649, 11400453.45282354, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 142.49491063, 0.00062312, 171.32980005, 0.01437063, 17.13298001, 0.03376657, -142.49491063, -0.00062312, -171.32980005, -0.01437063, -17.13298001, -0.03376657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 142.49491063, 0.00062312, 171.32980005, 0.01437063, 17.13298001, 0.03376657, -142.49491063, -0.00062312, -171.32980005, -0.01437063, -17.13298001, -0.03376657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 140.34246465, 0.01246236, 140.34246465, 0.03738709, 98.23972525, -1348.85323367, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 35.08561616, 6.463e-05, 105.25684849, 0.00019389, 350.85616162, 0.00064629, -35.08561616, -6.463e-05, -105.25684849, -0.00019389, -350.85616162, -0.00064629, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 140.34246465, 0.01246236, 140.34246465, 0.03738709, 98.23972525, -1348.85323367, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 35.08561616, 6.463e-05, 105.25684849, 0.00019389, 350.85616162, 0.00064629, -35.08561616, -6.463e-05, -105.25684849, -0.00019389, -350.85616162, -0.00064629, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.15)
    ops.node(123018, 21.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1225, 26680509.41510691, 11116878.92296121, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 98.44610971, 0.00068499, 118.59246508, 0.01540671, 11.85924651, 0.03666642, -98.44610971, -0.00068499, -118.59246508, -0.01540671, -11.85924651, -0.03666642, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 98.44610971, 0.00068499, 118.59246508, 0.01540671, 11.85924651, 0.03666642, -98.44610971, -0.00068499, -118.59246508, -0.01540671, -11.85924651, -0.03666642, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 106.16970502, 0.01369982, 106.16970502, 0.04109946, 74.31879351, -1053.54542469, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 26.54242626, 6.549e-05, 79.62727877, 0.00019646, 265.42426255, 0.00065488, -26.54242626, -6.549e-05, -79.62727877, -0.00019646, -265.42426255, -0.00065488, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 106.16970502, 0.01369982, 106.16970502, 0.04109946, 74.31879351, -1053.54542469, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 26.54242626, 6.549e-05, 79.62727877, 0.00019646, 265.42426255, 0.00065488, -26.54242626, -6.549e-05, -79.62727877, -0.00019646, -265.42426255, -0.00065488, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.15)
    ops.node(123019, 0.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 27707894.89182694, 11544956.20492789, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 40.87121979, 0.00089011, 49.1188058, 0.02015454, 4.91188058, 0.05311557, -40.87121979, -0.00089011, -49.1188058, -0.02015454, -4.91188058, -0.05311557, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 40.87121979, 0.00089011, 49.1188058, 0.02015454, 4.91188058, 0.05311557, -40.87121979, -0.00089011, -49.1188058, -0.02015454, -4.91188058, -0.05311557, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 67.00217897, 0.01780215, 67.00217897, 0.05340644, 46.90152528, -795.05855859, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 16.75054474, 7.8e-05, 50.25163423, 0.000234, 167.50544742, 0.00078, -16.75054474, -7.8e-05, -50.25163423, -0.000234, -167.50544742, -0.00078, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 67.00217897, 0.01780215, 67.00217897, 0.05340644, 46.90152528, -795.05855859, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 16.75054474, 7.8e-05, 50.25163423, 0.000234, 167.50544742, 0.00078, -16.75054474, -7.8e-05, -50.25163423, -0.000234, -167.50544742, -0.00078, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 4.5, 13.5, 6.175)
    ops.node(123020, 4.5, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1225, 27552701.81754821, 11480292.42397842, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 98.48794977, 0.00069405, 118.634663, 0.01555646, 11.8634663, 0.03809613, -98.48794977, -0.00069405, -118.634663, -0.01555646, -11.8634663, -0.03809613, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 98.48794977, 0.00069405, 118.634663, 0.01555646, 11.8634663, 0.03809613, -98.48794977, -0.00069405, -118.634663, -0.01555646, -11.8634663, -0.03809613, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 108.678397, 0.01388107, 108.678397, 0.04164322, 76.0748779, -1037.93367635, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 27.16959925, 6.491e-05, 81.50879775, 0.00019474, 271.69599251, 0.00064913, -27.16959925, -6.491e-05, -81.50879775, -0.00019474, -271.69599251, -0.00064913, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 108.678397, 0.01388107, 108.678397, 0.04164322, 76.0748779, -1037.93367635, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 27.16959925, 6.491e-05, 81.50879775, 0.00019474, 271.69599251, 0.00064913, -27.16959925, -6.491e-05, -81.50879775, -0.00019474, -271.69599251, -0.00064913, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.175)
    ops.node(123021, 9.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.1225, 27406442.89243533, 11419351.20518139, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 93.47860944, 0.00066965, 112.84305251, 0.01603173, 11.28430525, 0.03981356, -93.47860944, -0.00066965, -112.84305251, -0.01603173, -11.28430525, -0.03981356, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 93.47860944, 0.00066965, 112.84305251, 0.01603173, 11.28430525, 0.03981356, -93.47860944, -0.00066965, -112.84305251, -0.01603173, -11.28430525, -0.03981356, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 105.36562534, 0.01339307, 105.36562534, 0.04017922, 73.75593774, -978.07634441, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 26.34140634, 6.327e-05, 79.02421901, 0.00018981, 263.41406336, 0.0006327, -26.34140634, -6.327e-05, -79.02421901, -0.00018981, -263.41406336, -0.0006327, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 105.36562534, 0.01339307, 105.36562534, 0.04017922, 73.75593774, -978.07634441, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 26.34140634, 6.327e-05, 79.02421901, 0.00018981, 263.41406336, 0.0006327, -26.34140634, -6.327e-05, -79.02421901, -0.00018981, -263.41406336, -0.0006327, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.175)
    ops.node(123022, 12.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.1225, 26232237.80671642, 10930099.08613184, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 92.57322795, 0.00068174, 111.77987059, 0.01551405, 11.17798706, 0.03765513, -92.57322795, -0.00068174, -111.77987059, -0.01551405, -11.17798706, -0.03765513, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 92.57322795, 0.00068174, 111.77987059, 0.01551405, 11.17798706, 0.03765513, -92.57322795, -0.00068174, -111.77987059, -0.01551405, -11.17798706, -0.03765513, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 100.4387635, 0.01363474, 100.4387635, 0.04090422, 70.30713445, -963.06162047, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 25.10969087, 6.301e-05, 75.32907262, 0.00018903, 251.09690874, 0.00063012, -25.10969087, -6.301e-05, -75.32907262, -0.00018903, -251.09690874, -0.00063012, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 100.4387635, 0.01363474, 100.4387635, 0.04090422, 70.30713445, -963.06162047, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 25.10969087, 6.301e-05, 75.32907262, 0.00018903, 251.09690874, 0.00063012, -25.10969087, -6.301e-05, -75.32907262, -0.00018903, -251.09690874, -0.00063012, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 16.5, 13.5, 6.175)
    ops.node(123023, 16.5, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 26956901.5582561, 11232042.31594004, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 99.51464912, 0.00068249, 119.88503489, 0.01526521, 11.98850349, 0.03695488, -99.51464912, -0.00068249, -119.88503489, -0.01526521, -11.98850349, -0.03695488, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 99.51464912, 0.00068249, 119.88503489, 0.01526521, 11.98850349, 0.03695488, -99.51464912, -0.00068249, -119.88503489, -0.01526521, -11.98850349, -0.03695488, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 106.26117286, 0.01364987, 106.26117286, 0.0409496, 74.382821, -1033.3970425, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 26.56529322, 6.487e-05, 79.69587965, 0.00019462, 265.65293216, 0.00064872, -26.56529322, -6.487e-05, -79.69587965, -0.00019462, -265.65293216, -0.00064872, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 106.26117286, 0.01364987, 106.26117286, 0.0409496, 74.382821, -1033.3970425, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 26.56529322, 6.487e-05, 79.69587965, 0.00019462, 265.65293216, 0.00064872, -26.56529322, -6.487e-05, -79.69587965, -0.00019462, -265.65293216, -0.00064872, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.15)
    ops.node(123024, 21.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 28020785.52828126, 11675327.30345052, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 41.80078145, 0.00086185, 50.23199474, 0.02001208, 5.02319947, 0.05366544, -41.80078145, -0.00086185, -50.23199474, -0.02001208, -5.02319947, -0.05366544, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 41.80078145, 0.00086185, 50.23199474, 0.02001208, 5.02319947, 0.05366544, -41.80078145, -0.00086185, -50.23199474, -0.02001208, -5.02319947, -0.05366544, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 66.56027079, 0.01723696, 66.56027079, 0.05171089, 46.59218955, -792.85466957, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 16.6400677, 7.662e-05, 49.92020309, 0.00022986, 166.40067697, 0.00076621, -16.6400677, -7.662e-05, -49.92020309, -0.00022986, -166.40067697, -0.00076621, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 66.56027079, 0.01723696, 66.56027079, 0.05171089, 46.59218955, -792.85466957, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 16.6400677, 7.662e-05, 49.92020309, 0.00022986, 166.40067697, 0.00076621, -16.6400677, -7.662e-05, -49.92020309, -0.00022986, -166.40067697, -0.00076621, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.95)
    ops.node(124001, 0.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26106585.30467727, 10877743.87694887, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 19.94017727, 0.00081319, 24.30871391, 0.02239182, 2.43087139, 0.07456873, -19.94017727, -0.00081319, -24.30871391, -0.02239182, -2.43087139, -0.07456873, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 19.94017727, 0.00081319, 24.30871391, 0.02239182, 2.43087139, 0.07456873, -19.94017727, -0.00081319, -24.30871391, -0.02239182, -2.43087139, -0.07456873, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 59.3112467, 0.01626375, 59.3112467, 0.04879124, 41.51787269, -927.75805747, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 14.82781168, 7.328e-05, 44.48343503, 0.00021985, 148.27811675, 0.00073282, -14.82781168, -7.328e-05, -44.48343503, -0.00021985, -148.27811675, -0.00073282, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 59.3112467, 0.01626375, 59.3112467, 0.04879124, 41.51787269, -927.75805747, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 14.82781168, 7.328e-05, 44.48343503, 0.00021985, 148.27811675, 0.00073282, -14.82781168, -7.328e-05, -44.48343503, -0.00021985, -148.27811675, -0.00073282, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.5, 0.0, 8.95)
    ops.node(124002, 4.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1225, 26842956.52266024, 11184565.2177751, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 70.78961652, 0.00062966, 86.22595187, 0.01794484, 8.62259519, 0.04784565, -70.78961652, -0.00062966, -86.22595187, -0.01794484, -8.62259519, -0.04784565, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 70.78961652, 0.00062966, 86.22595187, 0.01794484, 8.62259519, 0.04784565, -70.78961652, -0.00062966, -86.22595187, -0.01794484, -8.62259519, -0.04784565, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 90.1755546, 0.01259317, 90.1755546, 0.0377795, 63.12288822, -763.28529196, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 22.54388865, 5.529e-05, 67.63166595, 0.00016586, 225.4388865, 0.00055286, -22.54388865, -5.529e-05, -67.63166595, -0.00016586, -225.4388865, -0.00055286, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 90.1755546, 0.01259317, 90.1755546, 0.0377795, 63.12288822, -763.28529196, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 22.54388865, 5.529e-05, 67.63166595, 0.00016586, 225.4388865, 0.00055286, -22.54388865, -5.529e-05, -67.63166595, -0.00016586, -225.4388865, -0.00055286, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.5, 0.0, 8.95)
    ops.node(124005, 16.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 27388082.48513245, 11411701.03547185, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 72.00351856, 0.00062576, 87.63638961, 0.01777487, 8.76363896, 0.04811677, -72.00351856, -0.00062576, -87.63638961, -0.01777487, -8.76363896, -0.04811677, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 72.00351856, 0.00062576, 87.63638961, 0.01777487, 8.76363896, 0.04811677, -72.00351856, -0.00062576, -87.63638961, -0.01777487, -8.76363896, -0.04811677, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 91.43021566, 0.01251519, 91.43021566, 0.03754557, 64.00115096, -745.0170536, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 22.85755392, 5.494e-05, 68.57266175, 0.00016482, 228.57553915, 0.00054939, -22.85755392, -5.494e-05, -68.57266175, -0.00016482, -228.57553915, -0.00054939, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 91.43021566, 0.01251519, 91.43021566, 0.03754557, 64.00115096, -745.0170536, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 22.85755392, 5.494e-05, 68.57266175, 0.00016482, 228.57553915, 0.00054939, -22.85755392, -5.494e-05, -68.57266175, -0.00016482, -228.57553915, -0.00054939, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 21.0, 0.0, 8.95)
    ops.node(124006, 21.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 27951067.20068721, 11646278.00028634, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 20.33271928, 0.00077436, 24.72383401, 0.02245158, 2.4723834, 0.07734332, -20.33271928, -0.00077436, -24.72383401, -0.02245158, -2.4723834, -0.07734332, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 20.33271928, 0.00077436, 24.72383401, 0.02245158, 2.4723834, 0.07734332, -20.33271928, -0.00077436, -24.72383401, -0.02245158, -2.4723834, -0.07734332, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 62.2961223, 0.01548712, 62.2961223, 0.04646137, 43.60728561, -915.95493557, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 15.57403058, 7.189e-05, 46.72209173, 0.00021567, 155.74030575, 0.00071891, -15.57403058, -7.189e-05, -46.72209173, -0.00021567, -155.74030575, -0.00071891, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 62.2961223, 0.01548712, 62.2961223, 0.04646137, 43.60728561, -915.95493557, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 15.57403058, 7.189e-05, 46.72209173, 0.00021567, 155.74030575, 0.00071891, -15.57403058, -7.189e-05, -46.72209173, -0.00021567, -155.74030575, -0.00071891, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 8.95)
    ops.node(124007, 0.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 26591556.82590693, 11079815.34412789, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 63.02101458, 0.00060816, 76.78583268, 0.02015583, 7.67858327, 0.05605589, -63.02101458, -0.00060816, -76.78583268, -0.02015583, -7.67858327, -0.05605589, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 59.42712884, 0.00060816, 72.40698364, 0.02015583, 7.24069836, 0.05605589, -59.42712884, -0.00060816, -72.40698364, -0.02015583, -7.24069836, -0.05605589, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 96.37341524, 0.01216311, 96.37341524, 0.03648933, 67.46139067, -981.38076217, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 24.09335381, 5.964e-05, 72.28006143, 0.00017893, 240.9335381, 0.00059644, -24.09335381, -5.964e-05, -72.28006143, -0.00017893, -240.9335381, -0.00059644, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 96.37341524, 0.01216311, 96.37341524, 0.03648933, 67.46139067, -981.38076217, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 24.09335381, 5.964e-05, 72.28006143, 0.00017893, 240.9335381, 0.00059644, -24.09335381, -5.964e-05, -72.28006143, -0.00017893, -240.9335381, -0.00059644, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.5, 4.5, 8.95)
    ops.node(124008, 4.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.16, 25090835.0619092, 10454514.60912883, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 97.97936826, 0.00060507, 119.23740052, 0.01668906, 11.92374005, 0.04071585, -97.97936826, -0.00060507, -119.23740052, -0.01668906, -11.92374005, -0.04071585, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 97.97936826, 0.00060507, 119.23740052, 0.01668906, 11.92374005, 0.04071585, -97.97936826, -0.00060507, -119.23740052, -0.01668906, -11.92374005, -0.04071585, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 110.46742348, 0.01210133, 110.46742348, 0.03630398, 77.32719643, -946.87685099, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 27.61685587, 5.547e-05, 82.85056761, 0.00016642, 276.16855869, 0.00055474, -27.61685587, -5.547e-05, -82.85056761, -0.00016642, -276.16855869, -0.00055474, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 110.46742348, 0.01210133, 110.46742348, 0.03630398, 77.32719643, -946.87685099, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 27.61685587, 5.547e-05, 82.85056761, 0.00016642, 276.16855869, 0.00055474, -27.61685587, -5.547e-05, -82.85056761, -0.00016642, -276.16855869, -0.00055474, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.0, 4.5, 8.95)
    ops.node(124009, 9.0, 4.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.16, 27715689.11378571, 11548203.79741071, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 93.96726725, 0.00057801, 114.24916423, 0.01745317, 11.42491642, 0.04519594, -93.96726725, -0.00057801, -114.24916423, -0.01745317, -11.42491642, -0.04519594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 93.96726725, 0.00057801, 114.24916423, 0.01745317, 11.42491642, 0.04519594, -93.96726725, -0.00057801, -114.24916423, -0.01745317, -11.42491642, -0.04519594, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 119.37680773, 0.0115602, 119.37680773, 0.03468059, 83.56376541, -909.36644037, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 29.84420193, 5.427e-05, 89.5326058, 0.00016281, 298.44201933, 0.00054271, -29.84420193, -5.427e-05, -89.5326058, -0.00016281, -298.44201933, -0.00054271, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 119.37680773, 0.0115602, 119.37680773, 0.03468059, 83.56376541, -909.36644037, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 29.84420193, 5.427e-05, 89.5326058, 0.00016281, 298.44201933, 0.00054271, -29.84420193, -5.427e-05, -89.5326058, -0.00016281, -298.44201933, -0.00054271, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.0, 4.5, 8.95)
    ops.node(124010, 12.0, 4.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.16, 27581499.36750476, 11492291.40312698, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 92.80975966, 0.00057227, 112.86518967, 0.01763457, 11.28651897, 0.04527849, -92.80975966, -0.00057227, -112.86518967, -0.01763457, -11.28651897, -0.04527849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 92.80975966, 0.00057227, 112.86518967, 0.01763457, 11.28651897, 0.04527849, -92.80975966, -0.00057227, -112.86518967, -0.01763457, -11.28651897, -0.04527849, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 118.71344278, 0.01144535, 118.71344278, 0.03433605, 83.09940994, -908.07235043, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 29.67836069, 5.423e-05, 89.03508208, 0.00016269, 296.78360694, 0.00054232, -29.67836069, -5.423e-05, -89.03508208, -0.00016269, -296.78360694, -0.00054232, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 118.71344278, 0.01144535, 118.71344278, 0.03433605, 83.09940994, -908.07235043, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 29.67836069, 5.423e-05, 89.03508208, 0.00016269, 296.78360694, 0.00054232, -29.67836069, -5.423e-05, -89.03508208, -0.00016269, -296.78360694, -0.00054232, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 16.5, 4.5, 8.95)
    ops.node(124011, 16.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.16, 27348439.74072105, 11395183.22530044, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 100.9292827, 0.00057948, 122.60330137, 0.01667403, 12.26033014, 0.04297759, -100.9292827, -0.00057948, -122.60330137, -0.01667403, -12.26033014, -0.04297759, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 100.9292827, 0.00057948, 122.60330137, 0.01667403, 12.26033014, 0.04297759, -100.9292827, -0.00057948, -122.60330137, -0.01667403, -12.26033014, -0.04297759, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 120.23812534, 0.01158962, 120.23812534, 0.03476885, 84.16668774, -938.09276787, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 30.05953133, 5.54e-05, 90.178594, 0.00016619, 300.59531335, 0.00055396, -30.05953133, -5.54e-05, -90.178594, -0.00016619, -300.59531335, -0.00055396, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 120.23812534, 0.01158962, 120.23812534, 0.03476885, 84.16668774, -938.09276787, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 30.05953133, 5.54e-05, 90.178594, 0.00016619, 300.59531335, 0.00055396, -30.05953133, -5.54e-05, -90.178594, -0.00016619, -300.59531335, -0.00055396, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 8.95)
    ops.node(124012, 21.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 26522495.82934444, 11051039.92889352, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 62.00334466, 0.00061132, 75.55229076, 0.02032224, 7.55522908, 0.05614922, -62.00334466, -0.00061132, -75.55229076, -0.02032224, -7.55522908, -0.05614922, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 58.58083789, 0.00061132, 71.38189918, 0.02032224, 7.13818992, 0.05614922, -58.58083789, -0.00061132, -71.38189918, -0.02032224, -7.13818992, -0.05614922, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 96.77060007, 0.01222641, 96.77060007, 0.03667922, 67.73942005, -1002.3771346, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 24.19265002, 6.005e-05, 72.57795005, 0.00018014, 241.92650018, 0.00060046, -24.19265002, -6.005e-05, -72.57795005, -0.00018014, -241.92650018, -0.00060046, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 96.77060007, 0.01222641, 96.77060007, 0.03667922, 67.73942005, -1002.3771346, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 24.19265002, 6.005e-05, 72.57795005, 0.00018014, 241.92650018, 0.00060046, -24.19265002, -6.005e-05, -72.57795005, -0.00018014, -241.92650018, -0.00060046, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.0, 8.95)
    ops.node(124013, 0.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.1225, 28278733.56870843, 11782805.65362851, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 70.58319764, 0.00062498, 85.77795572, 0.01801262, 8.57779557, 0.04898701, -70.58319764, -0.00062498, -85.77795572, -0.01801262, -8.57779557, -0.04898701, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 70.58319764, 0.00062498, 85.77795572, 0.01801262, 8.57779557, 0.04898701, -70.58319764, -0.00062498, -85.77795572, -0.01801262, -8.57779557, -0.04898701, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 95.1973556, 0.01249958, 95.1973556, 0.03749873, 66.63814892, -762.50643398, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 23.7993389, 5.54e-05, 71.3980167, 0.0001662, 237.99338899, 0.00055401, -23.7993389, -5.54e-05, -71.3980167, -0.0001662, -237.99338899, -0.00055401, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 95.1973556, 0.01249958, 95.1973556, 0.03749873, 66.63814892, -762.50643398, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 23.7993389, 5.54e-05, 71.3980167, 0.0001662, 237.99338899, 0.00055401, -23.7993389, -5.54e-05, -71.3980167, -0.0001662, -237.99338899, -0.00055401, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.5, 9.0, 8.95)
    ops.node(124014, 4.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.16, 26899858.36208466, 11208274.31753528, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 96.53493238, 0.00059421, 117.32715254, 0.01713556, 11.73271525, 0.04303653, -96.53493238, -0.00059421, -117.32715254, -0.01713556, -11.73271525, -0.04303653, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 96.53493238, 0.00059421, 117.32715254, 0.01713556, 11.73271525, 0.04303653, -96.53493238, -0.00059421, -117.32715254, -0.01713556, -11.73271525, -0.04303653, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 118.65072425, 0.0118843, 118.65072425, 0.03565289, 83.05550698, -949.69333374, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 29.66268106, 5.558e-05, 88.98804319, 0.00016673, 296.62681063, 0.00055576, -29.66268106, -5.558e-05, -88.98804319, -0.00016673, -296.62681063, -0.00055576, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 118.65072425, 0.0118843, 118.65072425, 0.03565289, 83.05550698, -949.69333374, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 29.66268106, 5.558e-05, 88.98804319, 0.00016673, 296.62681063, 0.00055576, -29.66268106, -5.558e-05, -88.98804319, -0.00016673, -296.62681063, -0.00055576, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 9.0, 8.95)
    ops.node(124015, 9.0, 9.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.16, 27678370.32265912, 11532654.30110797, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 94.2476417, 0.00057958, 114.54847142, 0.01719647, 11.45484714, 0.04456614, -94.2476417, -0.00057958, -114.54847142, -0.01719647, -11.45484714, -0.04456614, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 94.2476417, 0.00057958, 114.54847142, 0.01719647, 11.45484714, 0.04456614, -94.2476417, -0.00057958, -114.54847142, -0.01719647, -11.45484714, -0.04456614, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 119.50291888, 0.01159166, 119.50291888, 0.03477497, 83.65204322, -904.37458527, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 29.87572972, 5.44e-05, 89.62718916, 0.0001632, 298.7572972, 0.00054401, -29.87572972, -5.44e-05, -89.62718916, -0.0001632, -298.7572972, -0.00054401, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 119.50291888, 0.01159166, 119.50291888, 0.03477497, 83.65204322, -904.37458527, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 29.87572972, 5.44e-05, 89.62718916, 0.0001632, 298.7572972, 0.00054401, -29.87572972, -5.44e-05, -89.62718916, -0.0001632, -298.7572972, -0.00054401, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.0, 9.0, 8.95)
    ops.node(124016, 12.0, 9.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.16, 25783029.20447534, 10742928.83519806, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 96.08323001, 0.00058332, 117.03542602, 0.01695622, 11.7035426, 0.04268066, -96.08323001, -0.00058332, -117.03542602, -0.01695622, -11.7035426, -0.04268066, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 96.08323001, 0.00058332, 117.03542602, 0.01695622, 11.7035426, 0.04268066, -96.08323001, -0.00058332, -117.03542602, -0.01695622, -11.7035426, -0.04268066, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 111.35855774, 0.0116664, 111.35855774, 0.03499919, 77.95099042, -914.63245425, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 27.83963944, 5.442e-05, 83.51891831, 0.00016326, 278.39639436, 0.0005442, -27.83963944, -5.442e-05, -83.51891831, -0.00016326, -278.39639436, -0.0005442, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 111.35855774, 0.0116664, 111.35855774, 0.03499919, 77.95099042, -914.63245425, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 27.83963944, 5.442e-05, 83.51891831, 0.00016326, 278.39639436, 0.0005442, -27.83963944, -5.442e-05, -83.51891831, -0.00016326, -278.39639436, -0.0005442, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 16.5, 9.0, 8.95)
    ops.node(124017, 16.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.16, 27249964.79293175, 11354151.9970549, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 100.09013547, 0.00059408, 121.59883381, 0.01699, 12.15988338, 0.04320711, -100.09013547, -0.00059408, -121.59883381, -0.01699, -12.15988338, -0.04320711, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 100.09013547, 0.00059408, 121.59883381, 0.01699, 12.15988338, 0.04320711, -100.09013547, -0.00059408, -121.59883381, -0.01699, -12.15988338, -0.04320711, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 120.13633007, 0.01188156, 120.13633007, 0.03564469, 84.09543105, -946.8545453, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 30.03408252, 5.555e-05, 90.10224755, 0.00016665, 300.34082518, 0.00055549, -30.03408252, -5.555e-05, -90.10224755, -0.00016665, -300.34082518, -0.00055549, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 120.13633007, 0.01188156, 120.13633007, 0.03564469, 84.09543105, -946.8545453, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 30.03408252, 5.555e-05, 90.10224755, 0.00016665, 300.34082518, 0.00055549, -30.03408252, -5.555e-05, -90.10224755, -0.00016665, -300.34082518, -0.00055549, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 21.0, 9.0, 8.95)
    ops.node(124018, 21.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1225, 26303059.90471404, 10959608.29363085, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 70.96577237, 0.00063756, 86.49549632, 0.01822689, 8.64954963, 0.04763012, -70.96577237, -0.00063756, -86.49549632, -0.01822689, -8.64954963, -0.04763012, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 70.96577237, 0.00063756, 86.49549632, 0.01822689, 8.64954963, 0.04763012, -70.96577237, -0.00063756, -86.49549632, -0.01822689, -8.64954963, -0.04763012, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 88.38754485, 0.01275122, 88.38754485, 0.03825365, 61.87128139, -763.95707721, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 22.09688621, 5.53e-05, 66.29065864, 0.00016591, 220.96886212, 0.00055302, -22.09688621, -5.53e-05, -66.29065864, -0.00016591, -220.96886212, -0.00055302, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 88.38754485, 0.01275122, 88.38754485, 0.03825365, 61.87128139, -763.95707721, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 22.09688621, 5.53e-05, 66.29065864, 0.00016591, 220.96886212, 0.00055302, -22.09688621, -5.53e-05, -66.29065864, -0.00016591, -220.96886212, -0.00055302, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 13.5, 8.95)
    ops.node(124019, 0.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 27031581.40423301, 11263158.91843042, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 28.15162951, 0.00086826, 34.28014497, 0.02405382, 3.4280145, 0.07054285, -28.15162951, -0.00086826, -34.28014497, -0.02405382, -3.4280145, -0.07054285, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 28.15162951, 0.00086826, 34.28014497, 0.02405382, 3.4280145, 0.07054285, -28.15162951, -0.00086826, -34.28014497, -0.02405382, -3.4280145, -0.07054285, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 56.10947323, 0.01736516, 56.10947323, 0.05209549, 39.27663126, -727.78462683, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 14.02736831, 6.695e-05, 42.08210493, 0.00020086, 140.27368309, 0.00066954, -14.02736831, -6.695e-05, -42.08210493, -0.00020086, -140.27368309, -0.00066954, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 56.10947323, 0.01736516, 56.10947323, 0.05209549, 39.27663126, -727.78462683, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 14.02736831, 6.695e-05, 42.08210493, 0.00020086, 140.27368309, 0.00066954, -14.02736831, -6.695e-05, -42.08210493, -0.00020086, -140.27368309, -0.00066954, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 4.5, 13.5, 8.95)
    ops.node(124020, 4.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1225, 26984222.45498868, 11243426.02291195, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 70.89671165, 0.00062408, 86.33985153, 0.01775762, 8.63398515, 0.04777582, -70.89671165, -0.00062408, -86.33985153, -0.01775762, -8.63398515, -0.04777582, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 70.89671165, 0.00062408, 86.33985153, 0.01775762, 8.63398515, 0.04777582, -70.89671165, -0.00062408, -86.33985153, -0.01775762, -8.63398515, -0.04777582, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 90.43437819, 0.01248159, 90.43437819, 0.03744478, 63.30406473, -756.66754059, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 22.60859455, 5.515e-05, 67.82578364, 0.00016546, 226.08594546, 0.00055154, -22.60859455, -5.515e-05, -67.82578364, -0.00016546, -226.08594546, -0.00055154, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 90.43437819, 0.01248159, 90.43437819, 0.03744478, 63.30406473, -756.66754059, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 22.60859455, 5.515e-05, 67.82578364, 0.00016546, 226.08594546, 0.00055154, -22.60859455, -5.515e-05, -67.82578364, -0.00016546, -226.08594546, -0.00055154, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 8.95)
    ops.node(124021, 9.0, 13.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.1225, 27376815.42528432, 11407006.4272018, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 69.58891453, 0.00063114, 84.76566889, 0.01833788, 8.47656689, 0.0493909, -69.58891453, -0.00063114, -84.76566889, -0.01833788, -8.47656689, -0.0493909, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 69.58891453, 0.00063114, 84.76566889, 0.01833788, 8.47656689, 0.0493909, -69.58891453, -0.00063114, -84.76566889, -0.01833788, -8.47656689, -0.0493909, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 91.15753746, 0.0126228, 91.15753746, 0.0378684, 63.81027622, -769.48919033, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 22.78938436, 5.48e-05, 68.36815309, 0.00016439, 227.89384364, 0.00054798, -22.78938436, -5.48e-05, -68.36815309, -0.00016439, -227.89384364, -0.00054798, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 91.15753746, 0.0126228, 91.15753746, 0.0378684, 63.81027622, -769.48919033, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 22.78938436, 5.48e-05, 68.36815309, 0.00016439, 227.89384364, 0.00054798, -22.78938436, -5.48e-05, -68.36815309, -0.00016439, -227.89384364, -0.00054798, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 8.95)
    ops.node(124022, 12.0, 13.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.1225, 27988215.76168216, 11661756.56736757, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 69.73914747, 0.00062992, 84.8598941, 0.0181431, 8.48598941, 0.04961352, -69.73914747, -0.00062992, -84.8598941, -0.0181431, -8.48598941, -0.04961352, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 69.73914747, 0.00062992, 84.8598941, 0.0181431, 8.48598941, 0.04961352, -69.73914747, -0.00062992, -84.8598941, -0.0181431, -8.48598941, -0.04961352, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 92.55348065, 0.01259838, 92.55348065, 0.03779515, 64.78743645, -746.80726673, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 23.13837016, 5.442e-05, 69.41511049, 0.00016327, 231.38370162, 0.00054422, -23.13837016, -5.442e-05, -69.41511049, -0.00016327, -231.38370162, -0.00054422, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 92.55348065, 0.01259838, 92.55348065, 0.03779515, 64.78743645, -746.80726673, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 23.13837016, 5.442e-05, 69.41511049, 0.00016327, 231.38370162, 0.00054422, -23.13837016, -5.442e-05, -69.41511049, -0.00016327, -231.38370162, -0.00054422, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 16.5, 13.5, 8.95)
    ops.node(124023, 16.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 27822591.95492088, 11592746.6478837, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 70.2431689, 0.00062055, 85.43469061, 0.01775443, 8.54346906, 0.04842579, -70.2431689, -0.00062055, -85.43469061, -0.01775443, -8.54346906, -0.04842579, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 70.2431689, 0.00062055, 85.43469061, 0.01775443, 8.54346906, 0.04842579, -70.2431689, -0.00062055, -85.43469061, -0.01775443, -8.54346906, -0.04842579, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 91.96864519, 0.012411, 91.96864519, 0.03723301, 64.37805163, -717.04748873, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 22.9921613, 5.44e-05, 68.97648389, 0.0001632, 229.92161298, 0.000544, -22.9921613, -5.44e-05, -68.97648389, -0.0001632, -229.92161298, -0.000544, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 91.96864519, 0.012411, 91.96864519, 0.03723301, 64.37805163, -717.04748873, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 22.9921613, 5.44e-05, 68.97648389, 0.0001632, 229.92161298, 0.000544, -22.9921613, -5.44e-05, -68.97648389, -0.0001632, -229.92161298, -0.000544, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 21.0, 13.5, 8.95)
    ops.node(124024, 21.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 26362405.82806616, 10984335.76169423, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 29.07058085, 0.00080165, 35.42936771, 0.02407387, 3.54293677, 0.0696725, -29.07058085, -0.00080165, -35.42936771, -0.02407387, -3.54293677, -0.0696725, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 29.07058085, 0.00080165, 35.42936771, 0.02407387, 3.54293677, 0.0696725, -29.07058085, -0.00080165, -35.42936771, -0.02407387, -3.54293677, -0.0696725, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 54.90204682, 0.01603297, 54.90204682, 0.04809892, 38.43143277, -738.12345179, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 13.7255117, 6.718e-05, 41.17653511, 0.00020153, 137.25511704, 0.00067176, -13.7255117, -6.718e-05, -41.17653511, -0.00020153, -137.25511704, -0.00067176, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 54.90204682, 0.01603297, 54.90204682, 0.04809892, 38.43143277, -738.12345179, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 13.7255117, 6.718e-05, 41.17653511, 0.00020153, 137.25511704, 0.00067176, -13.7255117, -6.718e-05, -41.17653511, -0.00020153, -137.25511704, -0.00067176, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(124025, 9.0, 0.0, 1.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.16, 26405404.39190637, 11002251.82996099, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 270.93051888, 0.00058208, 323.69118685, 0.04579469, 32.36911868, 0.10651078, -270.93051888, -0.00058208, -323.69118685, -0.04579469, -32.36911868, -0.10651078, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 255.96829345, 0.00058208, 305.81523649, 0.03940932, 30.58152365, 0.08172039, -255.96829345, -0.00058208, -305.81523649, -0.03940932, -30.58152365, -0.08172039, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 302.4857396, 0.01164153, 302.4857396, 0.0349246, 211.74001772, -6394.94549914, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 75.6214349, 7.99e-05, 226.8643047, 0.00023971, 756.21434899, 0.00079902, -75.6214349, -7.99e-05, -226.8643047, -0.00023971, -756.21434899, -0.00079902, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 354.78768049, 0.01164153, 354.78768049, 0.0349246, 248.35137634, -9478.0632285, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 88.69692012, 9.372e-05, 266.09076037, 0.00028115, 886.96920123, 0.00093717, -88.69692012, -9.372e-05, -266.09076037, -0.00028115, -886.96920123, -0.00093717, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.875)
    ops.node(121003, 9.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.16, 25422002.01762319, 10592500.84067633, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 211.17253969, 0.00056936, 252.43902681, 0.0411801, 25.24390268, 0.09925372, -211.17253969, -0.00056936, -252.43902681, -0.0411801, -25.24390268, -0.09925372, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 181.80131255, 0.00056936, 217.32819278, 0.03544466, 21.73281928, 0.07591428, -181.80131255, -0.00056936, -217.32819278, -0.03544466, -21.73281928, -0.07591428, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 287.7162751, 0.01138724, 287.7162751, 0.03416171, 201.40139257, -6235.27568323, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 71.92906877, 7.894e-05, 215.78720632, 0.00023682, 719.29068774, 0.0007894, -71.92906877, -7.894e-05, -215.78720632, -0.00023682, -719.29068774, -0.0007894, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 339.04384698, 0.01138724, 339.04384698, 0.03416171, 237.33069289, -9345.70562587, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 84.76096175, 9.302e-05, 254.28288524, 0.00027907, 847.60961745, 0.00093023, -84.76096175, -9.302e-05, -254.28288524, -0.00027907, -847.60961745, -0.00093023, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.0, 0.0, 0.0)
    ops.node(124026, 12.0, 0.0, 1.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.16, 27150015.24173502, 11312506.35072293, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 273.00740594, 0.000575, 326.42884454, 0.04688359, 32.64288445, 0.11223639, -273.00740594, -0.000575, -326.42884454, -0.04688359, -32.64288445, -0.11223639, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 257.88213464, 0.000575, 308.34389619, 0.04034345, 30.83438962, 0.08588568, -257.88213464, -0.000575, -308.34389619, -0.04034345, -30.83438962, -0.08588568, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 306.18588526, 0.01149997, 306.18588526, 0.0344999, 214.33011968, -6262.33398815, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 76.54647131, 7.866e-05, 229.63941394, 0.00023598, 765.46471315, 0.00078661, -76.54647131, -7.866e-05, -229.63941394, -0.00023598, -765.46471315, -0.00078661, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 357.23420416, 0.01149997, 357.23420416, 0.0344999, 250.06394291, -9236.19130735, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 89.30855104, 9.178e-05, 267.92565312, 0.00027533, 893.0855104, 0.00091776, -89.30855104, -9.178e-05, -267.92565312, -0.00027533, -893.0855104, -0.00091776, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.875)
    ops.node(121004, 12.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.16, 26657018.3080194, 11107090.96167475, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 210.75657911, 0.00056427, 252.36561384, 0.04299322, 25.23656138, 0.10900263, -210.75657911, -0.00056427, -252.36561384, -0.04299322, -25.23656138, -0.10900263, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 182.22701779, 0.00056427, 218.20354742, 0.03700099, 21.82035474, 0.0830008, -182.22701779, -0.00056427, -218.20354742, -0.03700099, -21.82035474, -0.0830008, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 294.56568757, 0.0112855, 294.56568757, 0.0338565, 206.1959813, -6061.59271861, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 73.64142189, 7.708e-05, 220.92426568, 0.00023123, 736.41421893, 0.00077075, -73.64142189, -7.708e-05, -220.92426568, -0.00023123, -736.41421893, -0.00077075, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 344.28827073, 0.0112855, 344.28827073, 0.0338565, 241.00178951, -9027.25993903, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 86.07206768, 9.009e-05, 258.21620305, 0.00027026, 860.72067684, 0.00090085, -86.07206768, -9.009e-05, -258.21620305, -0.00027026, -860.72067684, -0.00090085, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.425)
    ops.node(124027, 9.0, 0.0, 4.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.16, 26711388.59547016, 11129745.24811256, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 136.13331768, 0.00053434, 163.86799876, 0.03782823, 16.38679988, 0.09181896, -136.13331768, -0.00053434, -163.86799876, -0.03782823, -16.38679988, -0.09181896, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 136.13331768, 0.00053434, 163.86799876, 0.03782823, 16.38679988, 0.09181896, -136.13331768, -0.00053434, -163.86799876, -0.03782823, -16.38679988, -0.09181896, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 302.1969313, 0.01068684, 302.1969313, 0.03206052, 211.53785191, -6716.52387699, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 75.54923282, 7.127e-05, 226.64769847, 0.00021382, 755.49232824, 0.00071274, -75.54923282, -7.127e-05, -226.64769847, -0.00021382, -755.49232824, -0.00071274, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 302.1969313, 0.01068684, 302.1969313, 0.03206052, 211.53785191, -6716.52387699, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 75.54923282, 7.127e-05, 226.64769847, 0.00021382, 755.49232824, 0.00071274, -75.54923282, -7.127e-05, -226.64769847, -0.00021382, -755.49232824, -0.00071274, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.775)
    ops.node(122003, 9.0, 0.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.16, 27446671.3110828, 11436113.0462845, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 130.29015382, 0.00053189, 157.09925189, 0.03137648, 15.70992519, 0.07390973, -130.29015382, -0.00053189, -157.09925189, -0.03137648, -15.70992519, -0.07390973, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 130.29015382, 0.00053189, 157.09925189, 0.03137648, 15.70992519, 0.07390973, -130.29015382, -0.00053189, -157.09925189, -0.03137648, -15.70992519, -0.07390973, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 270.61752258, 0.01063771, 270.61752258, 0.03191314, 189.43226581, -4653.95501758, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 67.65438065, 6.212e-05, 202.96314194, 0.00018635, 676.54380646, 0.00062116, -67.65438065, -6.212e-05, -202.96314194, -0.00018635, -676.54380646, -0.00062116, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 270.61752258, 0.01063771, 270.61752258, 0.03191314, 189.43226581, -4653.95501758, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 67.65438065, 6.212e-05, 202.96314194, 0.00018635, 676.54380646, 0.00062116, -67.65438065, -6.212e-05, -202.96314194, -0.00018635, -676.54380646, -0.00062116, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.425)
    ops.node(124028, 12.0, 0.0, 4.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.16, 26581815.53040947, 11075756.47100395, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 135.96970031, 0.00053399, 163.66572537, 0.03785701, 16.36657254, 0.09133189, -135.96970031, -0.00053399, -163.66572537, -0.03785701, -16.36657254, -0.09133189, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 135.96970031, 0.00053399, 163.66572537, 0.03785701, 16.36657254, 0.09133189, -135.96970031, -0.00053399, -163.66572537, -0.03785701, -16.36657254, -0.09133189, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 304.40802141, 0.01067972, 304.40802141, 0.03203916, 213.08561499, -6942.62721988, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 76.10200535, 7.215e-05, 228.30601606, 0.00021644, 761.02005354, 0.00072146, -76.10200535, -7.215e-05, -228.30601606, -0.00021644, -761.02005354, -0.00072146, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 304.40802141, 0.01067972, 304.40802141, 0.03203916, 213.08561499, -6942.62721988, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 76.10200535, 7.215e-05, 228.30601606, 0.00021644, 761.02005354, 0.00072146, -76.10200535, -7.215e-05, -228.30601606, -0.00021644, -761.02005354, -0.00072146, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.775)
    ops.node(122004, 12.0, 0.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.16, 27660153.34724265, 11525063.89468444, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 129.49081618, 0.00053067, 156.11985489, 0.03162869, 15.61198549, 0.07469262, -129.49081618, -0.00053067, -156.11985489, -0.03162869, -15.61198549, -0.07469262, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 129.49081618, 0.00053067, 156.11985489, 0.03162869, 15.61198549, 0.07469262, -129.49081618, -0.00053067, -156.11985489, -0.03162869, -15.61198549, -0.07469262, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 273.90613025, 0.01061331, 273.90613025, 0.03183992, 191.73429118, -4736.31092096, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 68.47653256, 6.239e-05, 205.42959769, 0.00018716, 684.76532563, 0.00062386, -68.47653256, -6.239e-05, -205.42959769, -0.00018716, -684.76532563, -0.00062386, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 273.90613025, 0.01061331, 273.90613025, 0.03183992, 191.73429118, -4736.31092096, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 68.47653256, 6.239e-05, 205.42959769, 0.00018716, 684.76532563, 0.00062386, -68.47653256, -6.239e-05, -205.42959769, -0.00018716, -684.76532563, -0.00062386, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.175)
    ops.node(124029, 9.0, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.1225, 26881539.53745082, 11200641.47393784, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 93.7741446, 0.00055792, 113.21075637, 0.04241744, 11.32107564, 0.10941526, -93.7741446, -0.00055792, -113.21075637, -0.04241744, -11.32107564, -0.10941526, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 93.7741446, 0.00055792, 113.21075637, 0.04241744, 11.32107564, 0.10941526, -93.7741446, -0.00055792, -113.21075637, -0.04241744, -11.32107564, -0.10941526, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 217.38246314, 0.01115835, 217.38246314, 0.03347506, 152.1677242, -5973.82102084, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 54.34561579, 6.654e-05, 163.03684736, 0.00019963, 543.45615785, 0.00066542, -54.34561579, -6.654e-05, -163.03684736, -0.00019963, -543.45615785, -0.00066542, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 217.38246314, 0.01115835, 217.38246314, 0.03347506, 152.1677242, -5973.82102084, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 54.34561579, 6.654e-05, 163.03684736, 0.00019963, 543.45615785, 0.00066542, -54.34561579, -6.654e-05, -163.03684736, -0.00019963, -543.45615785, -0.00066542, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.55)
    ops.node(123003, 9.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.1225, 26242168.98445798, 10934237.07685749, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 88.10993261, 0.00054415, 106.67612147, 0.04404791, 10.66761215, 0.11396718, -88.10993261, -0.00054415, -106.67612147, -0.04404791, -10.66761215, -0.11396718, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 88.10993261, 0.00054415, 106.67612147, 0.04404791, 10.66761215, 0.11396718, -88.10993261, -0.00054415, -106.67612147, -0.04404791, -10.66761215, -0.11396718, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 209.95968363, 0.01088302, 209.95968363, 0.03264907, 146.97177854, -6347.7363531, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 52.48992091, 6.584e-05, 157.46976272, 0.00019751, 524.89920908, 0.00065836, -52.48992091, -6.584e-05, -157.46976272, -0.00019751, -524.89920908, -0.00065836, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 209.95968363, 0.01088302, 209.95968363, 0.03264907, 146.97177854, -6347.7363531, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 52.48992091, 6.584e-05, 157.46976272, 0.00019751, 524.89920908, 0.00065836, -52.48992091, -6.584e-05, -157.46976272, -0.00019751, -524.89920908, -0.00065836, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.175)
    ops.node(124030, 12.0, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.1225, 27188326.80541951, 11328469.50225813, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 92.54383036, 0.00055968, 111.71417652, 0.042871, 11.17141765, 0.11109481, -92.54383036, -0.00055968, -111.71417652, -0.042871, -11.17141765, -0.11109481, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 92.54383036, 0.00055968, 111.71417652, 0.042871, 11.17141765, 0.11109481, -92.54383036, -0.00055968, -111.71417652, -0.042871, -11.17141765, -0.11109481, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 221.26251971, 0.01119365, 221.26251971, 0.03358096, 154.8837638, -6138.68087688, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 55.31562993, 6.697e-05, 165.94688978, 0.0002009, 553.15629928, 0.00066965, -55.31562993, -6.697e-05, -165.94688978, -0.0002009, -553.15629928, -0.00066965, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 221.26251971, 0.01119365, 221.26251971, 0.03358096, 154.8837638, -6138.68087688, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 55.31562993, 6.697e-05, 165.94688978, 0.0002009, 553.15629928, 0.00066965, -55.31562993, -6.697e-05, -165.94688978, -0.0002009, -553.15629928, -0.00066965, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.55)
    ops.node(123004, 12.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.1225, 25947705.68861183, 10811544.0369216, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 85.99145607, 0.00054412, 104.11680476, 0.04381192, 10.41168048, 0.11254648, -85.99145607, -0.00054412, -104.11680476, -0.04381192, -10.41168048, -0.11254648, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 85.99145607, 0.00054412, 104.11680476, 0.04381192, 10.41168048, 0.11254648, -85.99145607, -0.00054412, -104.11680476, -0.04381192, -10.41168048, -0.11254648, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 209.42591031, 0.01088241, 209.42591031, 0.03264723, 146.59813722, -6446.8368643, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 52.35647758, 6.641e-05, 157.06943273, 0.00019924, 523.56477578, 0.00066413, -52.35647758, -6.641e-05, -157.06943273, -0.00019924, -523.56477578, -0.00066413, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 209.42591031, 0.01088241, 209.42591031, 0.03264723, 146.59813722, -6446.8368643, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 52.35647758, 6.641e-05, 157.06943273, 0.00019924, 523.56477578, 0.00066413, -52.35647758, -6.641e-05, -157.06943273, -0.00019924, -523.56477578, -0.00066413, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 8.95)
    ops.node(124031, 9.0, 0.0, 9.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.1225, 27143555.57800379, 11309814.82416824, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 68.47909533, 0.00052714, 83.45290156, 0.01834752, 8.34529016, 0.04932555, -68.47909533, -0.00052714, -83.45290156, -0.01834752, -8.34529016, -0.04932555, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 68.47909533, 0.00052714, 83.45290156, 0.01834752, 8.34529016, 0.04932555, -68.47909533, -0.00052714, -83.45290156, -0.01834752, -8.34529016, -0.04932555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 129.4739189, 0.01054277, 129.4739189, 0.0316283, 90.63174323, -1475.361036, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 32.36847973, 3.925e-05, 97.10543918, 0.00011775, 323.68479725, 0.0003925, -32.36847973, -3.925e-05, -97.10543918, -0.00011775, -323.68479725, -0.0003925, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 129.4739189, 0.01054277, 129.4739189, 0.0316283, 90.63174323, -1475.361036, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 32.36847973, 3.925e-05, 97.10543918, 0.00011775, 323.68479725, 0.0003925, -32.36847973, -3.925e-05, -97.10543918, -0.00011775, -323.68479725, -0.0003925, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 9.0, 0.0, 10.3)
    ops.node(124003, 9.0, 0.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.1225, 26277960.01272812, 10949150.00530338, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 63.56740668, 0.00051248, 77.7625852, 0.01968547, 7.77625852, 0.05242984, -63.56740668, -0.00051248, -77.7625852, -0.01968547, -7.77625852, -0.05242984, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 63.56740668, 0.00051248, 77.7625852, 0.01968547, 7.77625852, 0.05242984, -63.56740668, -0.00051248, -77.7625852, -0.01968547, -7.77625852, -0.05242984, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 118.40537802, 0.01024965, 118.40537802, 0.03074894, 82.88376461, -1512.93201064, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 29.60134451, 3.708e-05, 88.80403352, 0.00011123, 296.01344505, 0.00037077, -29.60134451, -3.708e-05, -88.80403352, -0.00011123, -296.01344505, -0.00037077, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 118.40537802, 0.01024965, 118.40537802, 0.03074894, 82.88376461, -1512.93201064, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 29.60134451, 3.708e-05, 88.80403352, 0.00011123, 296.01344505, 0.00037077, -29.60134451, -3.708e-05, -88.80403352, -0.00011123, -296.01344505, -0.00037077, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 8.95)
    ops.node(124032, 12.0, 0.0, 9.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.1225, 26868556.6169318, 11195231.92372158, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 68.25941918, 0.00052193, 83.21958247, 0.01856871, 8.32195825, 0.04934364, -68.25941918, -0.00052193, -83.21958247, -0.01856871, -8.32195825, -0.04934364, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 68.25941918, 0.00052193, 83.21958247, 0.01856871, 8.32195825, 0.04934364, -68.25941918, -0.00052193, -83.21958247, -0.01856871, -8.32195825, -0.04934364, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 127.94684562, 0.01043856, 127.94684562, 0.03131567, 89.56279194, -1474.34909224, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 31.98671141, 3.918e-05, 95.96013422, 0.00011755, 319.86711405, 0.00039184, -31.98671141, -3.918e-05, -95.96013422, -0.00011755, -319.86711405, -0.00039184, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 127.94684562, 0.01043856, 127.94684562, 0.03131567, 89.56279194, -1474.34909224, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 31.98671141, 3.918e-05, 95.96013422, 0.00011755, 319.86711405, 0.00039184, -31.98671141, -3.918e-05, -95.96013422, -0.00011755, -319.86711405, -0.00039184, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 12.0, 0.0, 10.3)
    ops.node(124004, 12.0, 0.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.1225, 26349437.50196258, 10978932.29248441, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 62.57742314, 0.00051846, 76.54278308, 0.01955658, 7.65427831, 0.05234084, -62.57742314, -0.00051846, -76.54278308, -0.01955658, -7.65427831, -0.05234084, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 62.57742314, 0.00051846, 76.54278308, 0.01955658, 7.65427831, 0.05234084, -62.57742314, -0.00051846, -76.54278308, -0.01955658, -7.65427831, -0.05234084, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 119.49269349, 0.01036913, 119.49269349, 0.03110739, 83.64488545, -1568.28060479, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 29.87317337, 3.732e-05, 89.61952012, 0.00011195, 298.73173373, 0.00037316, -29.87317337, -3.732e-05, -89.61952012, -0.00011195, -298.73173373, -0.00037316, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 119.49269349, 0.01036913, 119.49269349, 0.03110739, 83.64488545, -1568.28060479, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 29.87317337, 3.732e-05, 89.61952012, 0.00011195, 298.73173373, 0.00037316, -29.87317337, -3.732e-05, -89.61952012, -0.00011195, -298.73173373, -0.00037316, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
