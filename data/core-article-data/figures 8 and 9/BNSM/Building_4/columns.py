import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 7.7, 0.0, 0.0)
    ops.node(121003, 7.7, 0.0, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.22, 26119670.70288791, 10883196.1262033, 0.00648267, 0.00610042, 0.00322667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 408.42400405, 0.00100378, 487.59386342, 0.00858734, 48.75938634, 0.02276326, -408.42400405, -0.00100378, -487.59386342, -0.00858734, -48.75938634, -0.02276326, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 441.49366091, 0.00079548, 527.07381953, 0.00904678, 52.70738195, 0.02636431, -441.49366091, -0.00079548, -527.07381953, -0.00904678, -52.70738195, -0.02636431, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 211.29900599, 0.02007558, 211.29900599, 0.06022673, 147.90930419, -1869.36028059, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 52.8247515, 9.796e-05, 158.47425449, 0.00029387, 528.24751498, 0.00097958, -52.8247515, -9.796e-05, -158.47425449, -0.00029387, -528.24751498, -0.00097958, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 229.25582332, 0.01590965, 229.25582332, 0.04772894, 160.47907633, -2163.36247889, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 57.31395583, 0.00010628, 171.94186749, 0.00031885, 573.13955831, 0.00106283, -57.31395583, -0.00010628, -171.94186749, -0.00031885, -573.13955831, -0.00106283, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.45, 0.0, 0.0)
    ops.node(121004, 12.45, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.105, 29572314.77056647, 12321797.82106936, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 115.23659353, 0.00127575, 137.12601548, 0.01015408, 13.71260155, 0.03546951, -115.23659353, -0.00127575, -137.12601548, -0.01015408, -13.71260155, -0.03546951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 124.24456883, 0.00110611, 147.84507374, 0.01042844, 14.78450737, 0.03885066, -124.24456883, -0.00110611, -147.84507374, -0.01042844, -14.78450737, -0.03885066, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 147.58058498, 0.02551506, 147.58058498, 0.07654517, 103.30640949, -1499.90694561, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 36.89514624, 0.00012662, 110.68543873, 0.00037985, 368.95146245, 0.00126616, -36.89514624, -0.00012662, -110.68543873, -0.00037985, -368.95146245, -0.00126616, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 156.15273474, 0.02212222, 156.15273474, 0.06636665, 109.30691432, -1661.59965684, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 39.03818369, 0.00013397, 117.11455106, 0.00040191, 390.38183685, 0.00133971, -39.03818369, -0.00013397, -117.11455106, -0.00040191, -390.38183685, -0.00133971, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 5.15, 0.0)
    ops.node(121005, 0.0, 5.15, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.0875, 29066308.54822284, 12110961.89509285, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 120.11211842, 0.00108021, 142.17084987, 0.00957518, 14.21708499, 0.03640506, -120.11211842, -0.00108021, -142.17084987, -0.00957518, -14.21708499, -0.03640506, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 80.00700355, 0.00148324, 94.7003836, 0.00910116, 9.47003836, 0.02981964, -80.00700355, -0.00148324, -94.7003836, -0.00910116, -9.47003836, -0.02981964, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 138.87044167, 0.02160424, 138.87044167, 0.06481272, 97.20930917, -1566.42401647, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 34.71761042, 0.00014546, 104.15283125, 0.00043638, 347.17610418, 0.00145461, -34.71761042, -0.00014546, -104.15283125, -0.00043638, -347.17610418, -0.00145461, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 123.21420596, 0.02966489, 123.21420596, 0.08899466, 86.24994417, -1287.15649556, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 30.80355149, 0.00012906, 92.41065447, 0.00038718, 308.03551489, 0.00129062, -30.80355149, -0.00012906, -92.41065447, -0.00038718, -308.03551489, -0.00129062, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 2.95, 5.15, 0.0)
    ops.node(121006, 2.95, 5.15, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.28, 28999916.03559846, 12083298.34816602, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 620.92898291, 0.00065782, 744.19568597, 0.01127478, 74.4195686, 0.03522856, -620.92898291, -0.00065782, -744.19568597, -0.01127478, -74.4195686, -0.03522856, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 445.89221733, 0.00092117, 534.41065513, 0.01013942, 53.44106551, 0.02727277, -445.89221733, -0.00092117, -534.41065513, -0.01013942, -53.44106551, -0.02727277, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 378.68221525, 0.01315649, 378.68221525, 0.03946948, 265.07755067, -3008.56300669, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 94.67055381, 0.00012424, 284.01166144, 0.00037271, 946.70553812, 0.00124238, -94.67055381, -0.00012424, -284.01166144, -0.00037271, -946.70553812, -0.00124238, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 285.83346348, 0.01842338, 285.83346348, 0.05527013, 200.08342443, -2216.48212111, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 71.45836587, 9.378e-05, 214.37509761, 0.00028133, 714.58365869, 0.00093776, -71.45836587, -9.378e-05, -214.37509761, -0.00028133, -714.58365869, -0.00093776, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 7.7, 5.15, 0.0)
    ops.node(121007, 7.7, 5.15, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.3825, 28588677.97429515, 11911949.15595631, 0.01726381, 0.00710016, 0.02533266, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 1220.53379062, 0.00062986, 1465.62487038, 0.00665952, 146.56248704, 0.02776814, -1220.53379062, -0.00062986, -1465.62487038, -0.00665952, -146.56248704, -0.02776814, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 812.2501481, 0.00088388, 975.3552316, 0.00611439, 97.53552316, 0.02117997, -812.2501481, -0.00088388, -975.3552316, -0.00611439, -97.53552316, -0.02117997, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 519.50090009, 0.01259727, 519.50090009, 0.03779182, 363.65063006, -2945.0497251, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 129.87522502, 0.00012656, 389.62567506, 0.00037968, 1298.75225021, 0.0012656, -129.87522502, -0.00012656, -389.62567506, -0.00037968, -1298.75225021, -0.0012656, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 294.48502156, 0.01767758, 294.48502156, 0.05303273, 206.13951509, -2305.36206284, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 73.62125539, 7.174e-05, 220.86376617, 0.00021523, 736.21255391, 0.00071742, -73.62125539, -7.174e-05, -220.86376617, -0.00021523, -736.21255391, -0.00071742, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 12.45, 5.15, 0.0)
    ops.node(121008, 12.45, 5.15, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.165, 27933934.44590719, 11639139.35246133, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 345.89340408, 0.00079784, 410.41389956, 0.00968147, 41.04138996, 0.0325785, -345.89340408, -0.00079784, -410.41389956, -0.00968147, -41.04138996, -0.0325785, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 228.09159161, 0.00125652, 270.63817484, 0.00868003, 27.06381748, 0.02363551, -228.09159161, -0.00125652, -270.63817484, -0.00868003, -27.06381748, -0.02363551, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 235.72488211, 0.01595686, 235.72488211, 0.04787057, 165.00741748, -2592.43368904, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 58.93122053, 0.00013625, 176.79366158, 0.00040874, 589.31220527, 0.00136246, -58.93122053, -0.00013625, -176.79366158, -0.00040874, -589.31220527, -0.00136246, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 194.83844001, 0.02513047, 194.83844001, 0.0753914, 136.38690801, -1888.72426311, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 48.70961, 0.00011261, 146.12883001, 0.00033784, 487.09610003, 0.00112614, -48.70961, -0.00011261, -146.12883001, -0.00033784, -487.09610003, -0.00112614, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 10.3, 0.0)
    ops.node(121009, 0.0, 10.3, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.12, 29891199.07830913, 12454666.28262881, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 164.41028879, 0.00095633, 195.84116002, 0.01038841, 19.584116, 0.04050813, -164.41028879, -0.00095633, -195.84116002, -0.01038841, -19.584116, -0.04050813, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 111.47844941, 0.00123003, 132.7901618, 0.00985534, 13.27901618, 0.03421862, -111.47844941, -0.00123003, -132.7901618, -0.00985534, -13.27901618, -0.03421862, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 172.69943921, 0.01912652, 172.69943921, 0.05737955, 120.88960745, -1770.17303148, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 43.1748598, 0.00012826, 129.52457941, 0.00038479, 431.74859802, 0.00128263, -43.1748598, -0.00012826, -129.52457941, -0.00038479, -431.74859802, -0.00128263, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 156.86860806, 0.02460065, 156.86860806, 0.07380194, 109.80802564, -1480.12527992, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 39.21715201, 0.00011651, 117.65145604, 0.00034952, 392.17152015, 0.00116505, -39.21715201, -0.00011651, -117.65145604, -0.00034952, -392.17152015, -0.00116505, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 2.95, 10.3, 0.0)
    ops.node(121010, 2.95, 10.3, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.28, 28440848.95627252, 11850353.73178022, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 633.7438874, 0.00068884, 760.15881396, 0.00938664, 76.0158814, 0.03285072, -633.7438874, -0.00068884, -760.15881396, -0.00938664, -76.0158814, -0.03285072, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 452.21433006, 0.00098226, 542.41897339, 0.0085342, 54.24189734, 0.02531728, -452.21433006, -0.00098226, -542.41897339, -0.0085342, -54.24189734, -0.02531728, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 349.52623075, 0.01377673, 349.52623075, 0.04133018, 244.66836153, -2598.83318262, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 87.38155769, 0.00011693, 262.14467307, 0.00035078, 873.81557689, 0.00116927, -87.38155769, -0.00011693, -262.14467307, -0.00035078, -873.81557689, -0.00116927, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 267.0504391, 0.01964527, 267.0504391, 0.05893582, 186.93530737, -1993.57355825, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 66.76260977, 8.934e-05, 200.28782932, 0.00026801, 667.62609774, 0.00089336, -66.76260977, -8.934e-05, -200.28782932, -0.00026801, -667.62609774, -0.00089336, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.7, 10.3, 0.0)
    ops.node(121011, 7.7, 10.3, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.3825, 28275730.93428167, 11781554.55595069, 0.01726381, 0.00710016, 0.02533266, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 1203.14205796, 0.00062463, 1444.96776567, 0.006926, 144.49677657, 0.02762556, -1203.14205796, -0.00062463, -1444.96776567, -0.006926, -144.49677657, -0.02762556, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 799.24528127, 0.00087572, 959.88969936, 0.00634193, 95.98896994, 0.02111556, -799.24528127, -0.00087572, -959.88969936, -0.00634193, -95.98896994, -0.02111556, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 516.93345761, 0.01249254, 516.93345761, 0.03747763, 361.85342033, -2994.66746577, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 129.2333644, 0.00012733, 387.70009321, 0.00038198, 1292.33364402, 0.00127328, -129.2333644, -0.00012733, -387.70009321, -0.00038198, -1292.33364402, -0.00127328, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 290.7228392, 0.01751437, 290.7228392, 0.05254311, 203.50598744, -2328.56402252, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 72.6807098, 7.161e-05, 218.0421294, 0.00021483, 726.80709799, 0.00071609, -72.6807098, -7.161e-05, -218.0421294, -0.00021483, -726.80709799, -0.00071609, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 12.45, 10.3, 0.0)
    ops.node(121012, 12.45, 10.3, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.165, 29899976.45938116, 12458323.52474215, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 329.02446249, 0.00080088, 390.79271388, 0.0100122, 39.07927139, 0.03766388, -329.02446249, -0.00080088, -390.79271388, -0.0100122, -39.07927139, -0.03766388, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 203.92868802, 0.00131899, 242.21252373, 0.00901633, 24.22125237, 0.02707737, -203.92868802, -0.00131899, -242.21252373, -0.00901633, -24.22125237, -0.02707737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 244.84835442, 0.01601757, 244.84835442, 0.04805272, 171.3938481, -2555.69942195, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 61.21208861, 0.00013221, 183.63626582, 0.00039664, 612.12088606, 0.00132214, -61.21208861, -0.00013221, -183.63626582, -0.00039664, -612.12088606, -0.00132214, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 204.86422353, 0.02637988, 204.86422353, 0.07913965, 143.40495647, -1871.59970669, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 51.21605588, 0.00011062, 153.64816765, 0.00033187, 512.16055883, 0.00110623, -51.21605588, -0.00011062, -153.64816765, -0.00033187, -512.16055883, -0.00110623, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 15.45, 0.0)
    ops.node(121013, 0.0, 15.45, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0875, 29480732.14386581, 12283638.39327742, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 126.40977854, 0.00109421, 149.37357486, 0.00997715, 14.93735749, 0.0363872, -126.40977854, -0.00109421, -149.37357486, -0.00997715, -14.93735749, -0.0363872, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 84.24868078, 0.00149646, 99.55342673, 0.00946228, 9.95534267, 0.02985657, -84.24868078, -0.00149646, -99.55342673, -0.00946228, -9.95534267, -0.02985657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 145.63799231, 0.02188428, 145.63799231, 0.06565283, 101.94659462, -1667.3251097, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 36.40949808, 0.00015041, 109.22849423, 0.00045122, 364.09498078, 0.00150405, -36.40949808, -0.00015041, -109.22849423, -0.00045122, -364.09498078, -0.00150405, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 128.98971412, 0.02992912, 128.98971412, 0.08978737, 90.29279989, -1370.61119627, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 32.24742853, 0.00013321, 96.74228559, 0.00039964, 322.4742853, 0.00133212, -32.24742853, -0.00013321, -96.74228559, -0.00039964, -322.4742853, -0.00133212, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 2.95, 15.45, 0.0)
    ops.node(121014, 2.95, 15.45, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.28, 27468781.31711004, 11445325.54879585, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 613.51952364, 0.00066106, 735.94528007, 0.01109725, 73.59452801, 0.03296193, -613.51952364, -0.00066106, -735.94528007, -0.01109725, -73.59452801, -0.03296193, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 444.76822459, 0.00092399, 533.52022715, 0.00998528, 53.35202271, 0.02562437, -444.76822459, -0.00092399, -533.52022715, -0.00998528, -53.35202271, -0.02562437, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 355.0488799, 0.01322127, 355.0488799, 0.03966381, 248.53421593, -2887.52533247, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 88.76221997, 0.00012298, 266.28665992, 0.00036893, 887.62219974, 0.00122977, -88.76221997, -0.00012298, -266.28665992, -0.00036893, -887.62219974, -0.00122977, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 267.59153868, 0.01847982, 267.59153868, 0.05543945, 187.31407708, -2137.58196972, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 66.89788467, 9.268e-05, 200.69365401, 0.00027805, 668.9788467, 0.00092685, -66.89788467, -9.268e-05, -200.69365401, -0.00027805, -668.9788467, -0.00092685, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.7, 15.45, 0.0)
    ops.node(121015, 7.7, 15.45, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.3825, 29411701.51323947, 12254875.63051645, 0.01726381, 0.00710016, 0.02533266, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 1228.24521603, 0.00063713, 1473.89200288, 0.00850495, 147.38920029, 0.03062332, -1228.24521603, -0.00063713, -1473.89200288, -0.00850495, -147.38920029, -0.03062332, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 805.60794954, 0.00090539, 966.7280595, 0.00773044, 96.67280595, 0.0235167, -805.60794954, -0.00090539, -966.7280595, -0.00773044, -96.67280595, -0.0235167, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 557.51519537, 0.01274266, 557.51519537, 0.03822797, 390.26063676, -3345.84055383, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 139.37879884, 0.00013202, 418.13639653, 0.00039606, 1393.78798843, 0.0013202, -139.37879884, -0.00013202, -418.13639653, -0.00039606, -1393.78798843, -0.0013202, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 338.65291723, 0.01810788, 338.65291723, 0.05432364, 237.05704206, -2491.78065267, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 84.66322931, 8.019e-05, 253.98968793, 0.00024058, 846.63229309, 0.00080193, -84.66322931, -8.019e-05, -253.98968793, -0.00024058, -846.63229309, -0.00080193, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.45, 15.45, 0.0)
    ops.node(121016, 12.45, 15.45, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.165, 27811112.37580542, 11587963.48991892, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 330.44532957, 0.00079155, 392.01100623, 0.00784232, 39.20110062, 0.03040623, -330.44532957, -0.00079155, -392.01100623, -0.00784232, -39.20110062, -0.03040623, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 211.51655144, 0.00125461, 250.92446086, 0.0071465, 25.09244609, 0.0218844, -211.51655144, -0.00125461, -250.92446086, -0.0071465, -25.09244609, -0.0218844, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 217.69476788, 0.01583102, 217.69476788, 0.04749306, 152.38633752, -2280.43013026, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 54.42369197, 0.00012638, 163.27107591, 0.00037914, 544.2369197, 0.0012638, -54.42369197, -0.00012638, -163.27107591, -0.00037914, -544.2369197, -0.0012638, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 184.71470092, 0.02509212, 184.71470092, 0.07527636, 129.30029065, -1742.40220535, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 46.17867523, 0.00010723, 138.53602569, 0.0003217, 461.78675231, 0.00107234, -46.17867523, -0.00010723, -138.53602569, -0.0003217, -461.78675231, -0.00107234, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 20.6, 0.0)
    ops.node(121017, 0.0, 20.6, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.0875, 30777085.77421134, 12823785.73925472, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 128.21577678, 0.00107502, 151.55470918, 0.01021617, 15.15547092, 0.04012154, -128.21577678, -0.00107502, -151.55470918, -0.01021617, -15.15547092, -0.04012154, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 85.33640586, 0.00145564, 100.87006839, 0.00965303, 10.08700684, 0.03274645, -85.33640586, -0.00145564, -100.87006839, -0.00965303, -10.08700684, -0.03274645, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 147.43107458, 0.02150042, 147.43107458, 0.06450126, 103.20175221, -1624.81762494, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 36.85776864, 0.00014584, 110.57330593, 0.00043753, 368.57768645, 0.00145844, -36.85776864, -0.00014584, -110.57330593, -0.00043753, -368.57768645, -0.00145844, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 131.4366313, 0.02911289, 131.4366313, 0.08733868, 92.00564191, -1343.04486984, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 32.85915783, 0.00013002, 98.57747348, 0.00039006, 328.59157826, 0.00130021, -32.85915783, -0.00013002, -98.57747348, -0.00039006, -328.59157826, -0.00130021, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 2.95, 20.6, 0.0)
    ops.node(121018, 2.95, 20.6, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.28, 31267157.87698254, 13027982.44874272, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 608.25049746, 0.00064521, 727.32415987, 0.01074574, 72.73241599, 0.03810002, -608.25049746, -0.00064521, -727.32415987, -0.01074574, -72.73241599, -0.03810002, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 430.80563638, 0.00090594, 515.14195032, 0.0096758, 51.51419503, 0.02924142, -430.80563638, -0.00090594, -515.14195032, -0.0096758, -51.51419503, -0.02924142, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 385.77257821, 0.01290426, 385.77257821, 0.03871277, 270.04080475, -2691.25089705, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 96.44314455, 0.00011739, 289.32943366, 0.00035216, 964.43144552, 0.00117387, -96.44314455, -0.00011739, -289.32943366, -0.00035216, -964.43144552, -0.00117387, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 295.68835361, 0.01811886, 295.68835361, 0.05435657, 206.98184753, -2040.51236596, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 73.9220884, 8.998e-05, 221.76626521, 0.00026993, 739.22088403, 0.00089975, -73.9220884, -8.998e-05, -221.76626521, -0.00026993, -739.22088403, -0.00089975, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 7.7, 20.6, 0.0)
    ops.node(121019, 7.7, 20.6, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.3825, 29326258.13271105, 12219274.22196294, 0.01726381, 0.00710016, 0.02533266, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 1179.56253659, 0.00061727, 1415.59132065, 0.00710981, 141.55913207, 0.02912562, -1179.56253659, -0.00061727, -1415.59132065, -0.00710981, -141.55913207, -0.02912562, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 770.95860982, 0.00087089, 925.22632992, 0.00650293, 92.52263299, 0.02221599, -770.95860982, -0.00087089, -925.22632992, -0.00650293, -92.52263299, -0.02221599, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 532.74605887, 0.01234534, 532.74605887, 0.03703603, 372.92224121, -2945.92848835, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 133.18651472, 0.00012652, 399.55954415, 0.00037957, 1331.86514716, 0.00126522, -133.18651472, -0.00012652, -399.55954415, -0.00037957, -1331.86514716, -0.00126522, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 303.52744536, 0.01741775, 303.52744536, 0.05225324, 212.46921175, -2306.82475375, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 75.88186134, 7.208e-05, 227.64558402, 0.00021625, 758.81861341, 0.00072085, -75.88186134, -7.208e-05, -227.64558402, -0.00021625, -758.81861341, -0.00072085, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 12.45, 20.6, 0.0)
    ops.node(121020, 12.45, 20.6, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.165, 31207483.07457853, 13003117.94774106, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 339.50744145, 0.00078812, 402.94744411, 0.00820299, 40.29474441, 0.03870093, -339.50744145, -0.00078812, -402.94744411, -0.00820299, -40.29474441, -0.03870093, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 217.28224378, 0.00124161, 257.88337483, 0.00743777, 25.78833748, 0.02735787, -217.28224378, -0.00124161, -257.88337483, -0.00743777, -25.78833748, -0.02735787, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 242.5857267, 0.01576247, 242.5857267, 0.04728741, 169.81000869, -2378.23263547, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 60.64643168, 0.0001255, 181.93929503, 0.00037651, 606.46431675, 0.00125504, -60.64643168, -0.0001255, -181.93929503, -0.00037651, -606.46431675, -0.00125504, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 207.07894829, 0.02483228, 207.07894829, 0.07449683, 144.9552638, -1788.84910808, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 51.76973707, 0.00010713, 155.30921122, 0.0003214, 517.69737073, 0.00107134, -51.76973707, -0.00010713, -155.30921122, -0.0003214, -517.69737073, -0.00107134, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 0.0, 25.75, 0.0)
    ops.node(121021, 0.0, 25.75, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.12, 26974783.30074484, 11239493.04197701, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 165.45938076, 0.00097622, 196.80101368, 0.0080483, 19.68010137, 0.03103668, -165.45938076, -0.00097622, -196.80101368, -0.0080483, -19.68010137, -0.03103668, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 111.47735895, 0.00125314, 132.59361388, 0.00772032, 13.25936139, 0.02631518, -111.47735895, -0.00125314, -132.59361388, -0.00772032, -13.25936139, -0.02631518, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 151.7429333, 0.01952432, 151.7429333, 0.05857297, 106.22005331, -1596.38849196, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 37.93573333, 0.00012488, 113.80719998, 0.00037465, 379.35733326, 0.00124883, -37.93573333, -0.00012488, -113.80719998, -0.00037465, -379.35733326, -0.00124883, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 138.26375875, 0.02506284, 138.26375875, 0.07518853, 96.78463113, -1361.08803476, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 34.56593969, 0.00011379, 103.69781906, 0.00034137, 345.65939688, 0.0011379, -34.56593969, -0.00011379, -103.69781906, -0.00034137, -345.65939688, -0.0011379, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 2.95, 25.75, 0.0)
    ops.node(121022, 2.95, 25.75, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.28, 29374857.33694636, 12239523.89039432, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 617.22550374, 0.00066162, 739.87313378, 0.00925044, 73.98731338, 0.03407155, -617.22550374, -0.00066162, -739.87313378, -0.00925044, -73.98731338, -0.03407155, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 440.69136822, 0.00093205, 528.26025766, 0.00838935, 52.82602577, 0.02614308, -440.69136822, -0.00093205, -528.26025766, -0.00838935, -52.82602577, -0.02614308, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 354.934157, 0.01323234, 354.934157, 0.03969703, 248.4539099, -2515.0227931, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 88.73353925, 0.00011496, 266.20061775, 0.00034488, 887.3353925, 0.0011496, -88.73353925, -0.00011496, -266.20061775, -0.00034488, -887.3353925, -0.0011496, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 272.78783879, 0.01864092, 272.78783879, 0.05592276, 190.95148715, -1953.93078212, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 68.1969597, 8.835e-05, 204.59087909, 0.00026506, 681.96959698, 0.00088354, -68.1969597, -8.835e-05, -204.59087909, -0.00026506, -681.96959698, -0.00088354, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 7.7, 25.75, 0.0)
    ops.node(121023, 7.7, 25.75, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.3825, 26806364.07744209, 11169318.36560087, 0.01726381, 0.00710016, 0.02533266, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 1140.08249329, 0.00060761, 1369.13199082, 0.00684459, 136.91319908, 0.02542577, -1140.08249329, -0.00060761, -1369.13199082, -0.00684459, -136.91319908, -0.02542577, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 751.11530319, 0.000851, 902.01892972, 0.00626135, 90.20189297, 0.01952306, -751.11530319, -0.000851, -902.01892972, -0.00626135, -90.20189297, -0.01952306, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 489.48343809, 0.01215218, 489.48343809, 0.03645655, 342.63840666, -2961.71411658, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 122.37085952, 0.00012718, 367.11257856, 0.00038153, 1223.70859521, 0.00127175, -122.37085952, -0.00012718, -367.11257856, -0.00038153, -1223.70859521, -0.00127175, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 273.59778043, 0.01702002, 273.59778043, 0.05106007, 191.5184463, -2316.32048899, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 68.39944511, 7.108e-05, 205.19833532, 0.00021325, 683.99445106, 0.00071085, -68.39944511, -7.108e-05, -205.19833532, -0.00021325, -683.99445106, -0.00071085, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 12.45, 25.75, 0.0)
    ops.node(121024, 12.45, 25.75, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.165, 29034381.50609666, 12097658.96087361, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 339.69897951, 0.00076923, 403.39436593, 0.00959286, 40.33943659, 0.03515439, -339.69897951, -0.00076923, -403.39436593, -0.00959286, -40.33943659, -0.03515439, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 223.0520243, 0.0012035, 264.875479, 0.00857688, 26.4875479, 0.0252727, -223.0520243, -0.0012035, -264.875479, -0.00857688, -26.4875479, -0.0252727, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 240.30257646, 0.0153845, 240.30257646, 0.04615351, 168.21180352, -2562.51555348, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 60.07564412, 0.00013363, 180.22693235, 0.00040088, 600.75644116, 0.00133628, -60.07564412, -0.00013363, -180.22693235, -0.00040088, -600.75644116, -0.00133628, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 200.2157296, 0.02407, 200.2157296, 0.07221, 140.15101072, -1876.70697577, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 50.0539324, 0.00011134, 150.1617972, 0.00033401, 500.539324, 0.00111336, -50.0539324, -0.00011134, -150.1617972, -0.00033401, -500.539324, -0.00111336, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170025, 0.0, 30.9, 0.0)
    ops.node(121025, 0.0, 30.9, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 25, 170025, 121025, 0.075, 27146703.3221064, 11311126.384211, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20025, 79.40509194, 0.00120176, 94.62541026, 0.00970594, 9.46254103, 0.03809816, -79.40509194, -0.00120176, -94.62541026, -0.00970594, -9.46254103, -0.03809816, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10025, 61.12045069, 0.00143303, 72.83598042, 0.0094406, 7.28359804, 0.03405624, -61.12045069, -0.00143303, -72.83598042, -0.0094406, -7.28359804, -0.03405624, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20025, 25, 0.0, 102.40171224, 0.02403513, 102.40171224, 0.0721054, 71.68119856, -1136.83937533, 0.05, 2, 0, 70025, 21025, 2, 3)
    ops.uniaxialMaterial('LimitState', 40025, 25.60042806, 0.00013399, 76.80128418, 0.00040196, 256.00428059, 0.00133987, -25.60042806, -0.00013399, -76.80128418, -0.00040196, -256.00428059, -0.00133987, 0.4, 0.3, 0.003, 0.0, 0.0, 20025, 2)
    ops.limitCurve('ThreePoint', 10025, 25, 0.0, 95.39911615, 0.02866067, 95.39911615, 0.08598202, 66.7793813, -1001.61490678, 0.05, 2, 0, 70025, 21025, 1, 3)
    ops.uniaxialMaterial('LimitState', 30025, 23.84977904, 0.00012482, 71.54933711, 0.00037447, 238.49779037, 0.00124825, -23.84977904, -0.00012482, -71.54933711, -0.00037447, -238.49779037, -0.00124825, 0.4, 0.3, 0.003, 0.0, 0.0, 10025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 25, 99999, 'P', 40025, 'Vy', 30025, 'Vz', 20025, 'My', 10025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170025, 70025, 170025, 25, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121025, 121025, 21025, 25, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170026, 2.95, 30.9, 0.0)
    ops.node(121026, 2.95, 30.9, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 26, 170026, 121026, 0.16, 27411289.06153249, 11421370.4423052, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20026, 247.70115775, 0.00092634, 295.55395907, 0.00846082, 29.55539591, 0.02952553, -247.70115775, -0.00092634, -295.55395907, -0.00846082, -29.55539591, -0.02952553, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10026, 214.71424423, 0.00092634, 256.19438168, 0.00846082, 25.61943817, 0.02952553, -214.71424423, -0.00092634, -256.19438168, -0.00846082, -25.61943817, -0.02952553, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20026, 26, 0.0, 185.30254016, 0.01852688, 185.30254016, 0.05558065, 129.71177811, -1784.01411351, 0.05, 2, 0, 70026, 21026, 2, 3)
    ops.uniaxialMaterial('LimitState', 40026, 46.32563504, 0.00011256, 138.97690512, 0.00033767, 463.2563504, 0.00112555, -46.32563504, -0.00011256, -138.97690512, -0.00033767, -463.2563504, -0.00112555, 0.4, 0.3, 0.003, 0.0, 0.0, 20026, 2)
    ops.limitCurve('ThreePoint', 10026, 26, 0.0, 185.30254016, 0.01852688, 185.30254016, 0.05558065, 129.71177811, -1784.01411351, 0.05, 2, 0, 70026, 21026, 1, 3)
    ops.uniaxialMaterial('LimitState', 30026, 46.32563504, 0.00011256, 138.97690512, 0.00033767, 463.2563504, 0.00112555, -46.32563504, -0.00011256, -138.97690512, -0.00033767, -463.2563504, -0.00112555, 0.4, 0.3, 0.003, 0.0, 0.0, 10026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 26, 99999, 'P', 40026, 'Vy', 30026, 'Vz', 20026, 'My', 10026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170026, 70026, 170026, 26, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121026, 121026, 21026, 26, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170027, 7.7, 30.9, 0.0)
    ops.node(121027, 7.7, 30.9, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 27, 170027, 121027, 0.2475, 29786223.56417813, 12410926.48507422, 0.00841652, 0.00686297, 0.00459422, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20027, 506.98926646, 0.00089124, 607.19505267, 0.01189377, 60.71950527, 0.03238778, -506.98926646, -0.00089124, -607.19505267, -0.01189377, -60.71950527, -0.03238778, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10027, 499.64795716, 0.00077581, 598.40274289, 0.01236536, 59.84027429, 0.03554868, -499.64795716, -0.00077581, -598.40274289, -0.01236536, -59.84027429, -0.03554868, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20027, 27, 0.0, 263.67913424, 0.01782483, 263.67913424, 0.05347449, 184.57539397, -2036.77500692, 0.05, 2, 0, 70027, 21027, 2, 3)
    ops.uniaxialMaterial('LimitState', 40027, 65.91978356, 9.528e-05, 197.75935068, 0.00028585, 659.19783561, 0.00095284, -65.91978356, -9.528e-05, -197.75935068, -0.00028585, -659.19783561, -0.00095284, 0.4, 0.3, 0.003, 0.0, 0.0, 20027, 2)
    ops.limitCurve('ThreePoint', 10027, 27, 0.0, 276.53598912, 0.01551618, 276.53598912, 0.04654853, 193.57519238, -2253.28260522, 0.05, 2, 0, 70027, 21027, 1, 3)
    ops.uniaxialMaterial('LimitState', 30027, 69.13399728, 9.993e-05, 207.40199184, 0.00029979, 691.33997279, 0.0009993, -69.13399728, -9.993e-05, -207.40199184, -0.00029979, -691.33997279, -0.0009993, 0.4, 0.3, 0.003, 0.0, 0.0, 10027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 27, 99999, 'P', 40027, 'Vy', 30027, 'Vz', 20027, 'My', 10027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170027, 70027, 170027, 27, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121027, 121027, 21027, 27, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170028, 12.45, 30.9, 0.0)
    ops.node(121028, 12.45, 30.9, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 28, 170028, 121028, 0.1225, 28056698.06312323, 11690290.85963468, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20028, 151.47953597, 0.00103566, 180.86676265, 0.00916854, 18.08667627, 0.03398398, -151.47953597, -0.00103566, -180.86676265, -0.00916854, -18.08667627, -0.03398398, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10028, 132.19496686, 0.00103566, 157.84096209, 0.00916854, 15.78409621, 0.03398398, -132.19496686, -0.00103566, -157.84096209, -0.00916854, -15.78409621, -0.03398398, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20028, 28, 0.0, 150.64643257, 0.02071317, 150.64643257, 0.06213951, 105.4525028, -1476.38775736, 0.05, 2, 0, 70028, 21028, 2, 3)
    ops.uniaxialMaterial('LimitState', 40028, 37.66160814, 0.00011677, 112.98482442, 0.0003503, 376.61608141, 0.00116767, -37.66160814, -0.00011677, -112.98482442, -0.0003503, -376.61608141, -0.00116767, 0.4, 0.3, 0.003, 0.0, 0.0, 20028, 2)
    ops.limitCurve('ThreePoint', 10028, 28, 0.0, 150.64643257, 0.02071317, 150.64643257, 0.06213951, 105.4525028, -1476.38775736, 0.05, 2, 0, 70028, 21028, 1, 3)
    ops.uniaxialMaterial('LimitState', 30028, 37.66160814, 0.00011677, 112.98482442, 0.0003503, 376.61608141, 0.00116767, -37.66160814, -0.00011677, -112.98482442, -0.0003503, -376.61608141, -0.00116767, 0.4, 0.3, 0.003, 0.0, 0.0, 10028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 28, 99999, 'P', 40028, 'Vy', 30028, 'Vz', 20028, 'My', 10028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170028, 70028, 170028, 28, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121028, 121028, 21028, 28, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.7, 0.0, 3.975)
    ops.node(122003, 7.7, 0.0, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.22, 27242382.07450357, 11350992.53104316, 0.00648267, 0.00610042, 0.00322667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 206.7832247, 0.00078111, 248.83899733, 0.00842854, 24.88389973, 0.02779992, -206.7832247, -0.00078111, -248.83899733, -0.00842854, -24.88389973, -0.02779992, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 324.54692957, 0.0006504, 390.55359863, 0.00897119, 39.05535986, 0.03263558, -324.54692957, -0.0006504, -390.55359863, -0.00897119, -39.05535986, -0.03263558, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 200.9124557, 0.01562226, 200.9124557, 0.04686677, 140.63871899, -2000.64102747, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 50.22811392, 6.879e-05, 150.68434177, 0.00020637, 502.28113925, 0.00068789, -50.22811392, -6.879e-05, -150.68434177, -0.00020637, -502.28113925, -0.00068789, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 254.47577444, 0.01300806, 254.47577444, 0.03902419, 178.13304211, -2384.64144019, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 63.61894361, 8.713e-05, 190.85683083, 0.00026138, 636.18943611, 0.00087128, -63.61894361, -8.713e-05, -190.85683083, -0.00026138, -636.18943611, -0.00087128, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.45, 0.0, 3.95)
    ops.node(122004, 12.45, 0.0, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.105, 28024539.16208893, 11676891.31753705, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 98.22373258, 0.00094879, 117.72489502, 0.01028223, 11.7724895, 0.03800087, -98.22373258, -0.00094879, -117.72489502, -0.01028223, -11.7724895, -0.03800087, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 103.47532489, 0.00084426, 124.01912898, 0.01064446, 12.4019129, 0.04176483, -103.47532489, -0.00084426, -124.01912898, -0.01064446, -12.4019129, -0.04176483, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 129.21583296, 0.01897586, 129.21583296, 0.05692759, 90.45108307, -1670.50185326, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 32.30395824, 9.011e-05, 96.91187472, 0.00027033, 323.03958239, 0.00090108, -32.30395824, -9.011e-05, -96.91187472, -0.00027033, -323.03958239, -0.00090108, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 137.14356822, 0.01688529, 137.14356822, 0.05065587, 96.00049776, -1881.90075388, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 34.28589206, 9.564e-05, 102.85767617, 0.00028691, 342.85892056, 0.00095637, -34.28589206, -9.564e-05, -102.85767617, -0.00028691, -342.85892056, -0.00095637, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 5.15, 3.95)
    ops.node(122005, 0.0, 5.15, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.0875, 28680077.64586187, 11950032.35244245, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 96.53915257, 0.00088239, 115.20543961, 0.00902724, 11.52054396, 0.0422045, -96.53915257, -0.00088239, -115.20543961, -0.00902724, -11.52054396, -0.0422045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 71.55948888, 0.00116762, 85.39584361, 0.00847156, 8.53958436, 0.03409159, -71.55948888, -0.00116762, -85.39584361, -0.00847156, -8.53958436, -0.03409159, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 123.19260409, 0.01764788, 123.19260409, 0.05294364, 86.23482286, -1707.96967831, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 30.79815102, 0.00010073, 92.39445306, 0.0003022, 307.98151021, 0.00100733, -30.79815102, -0.00010073, -92.39445306, -0.0003022, -307.98151021, -0.00100733, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 102.62211156, 0.02335246, 102.62211156, 0.07005738, 71.83547809, -1365.06312506, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 25.65552789, 8.391e-05, 76.96658367, 0.00025174, 256.5552789, 0.00083913, -25.65552789, -8.391e-05, -76.96658367, -0.00025174, -256.5552789, -0.00083913, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 2.95, 5.15, 3.975)
    ops.node(122006, 2.95, 5.15, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.28, 29209679.05183822, 12170699.60493259, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 514.38490252, 0.00057796, 619.17414465, 0.00927937, 61.91741447, 0.03700313, -514.38490252, -0.00057796, -619.17414465, -0.00927937, -61.91741447, -0.03700313, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 246.49703635, 0.00074849, 296.71281349, 0.00830355, 29.67128135, 0.02813345, -246.49703635, -0.00074849, -296.71281349, -0.00830355, -29.67128135, -0.02813345, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 406.91945982, 0.01155918, 406.91945982, 0.03467754, 284.84362187, -2895.57003649, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 101.72986496, 0.00010209, 305.18959487, 0.00030628, 1017.29864955, 0.00102094, -101.72986496, -0.00010209, -305.18959487, -0.00030628, -1017.29864955, -0.00102094, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 253.82383562, 0.01496973, 253.82383562, 0.04490918, 177.67668494, -2142.43234515, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 63.45595891, 6.368e-05, 190.36787672, 0.00019105, 634.55958906, 0.00063683, -63.45595891, -6.368e-05, -190.36787672, -0.00019105, -634.55958906, -0.00063683, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 7.7, 5.15, 3.975)
    ops.node(122007, 7.7, 5.15, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.3825, 27916710.31017665, 11631962.62924027, 0.01726381, 0.00710016, 0.02533266, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 827.3609324, 0.00057887, 998.41773719, 0.00704494, 99.84177372, 0.03027728, -827.3609324, -0.00057887, -998.41773719, -0.00704494, -99.84177372, -0.03027728, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 395.97125524, 0.00075364, 477.83827973, 0.00636272, 47.78382797, 0.02294404, -395.97125524, -0.00075364, -477.83827973, -0.00636272, -47.78382797, -0.02294404, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 596.24404018, 0.01157736, 596.24404018, 0.03473207, 417.37082812, -3486.37264125, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 149.06101004, 0.00011458, 447.18303013, 0.00034374, 1490.61010044, 0.00114579, -149.06101004, -0.00011458, -447.18303013, -0.00034374, -1490.61010044, -0.00114579, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 270.95368247, 0.01507281, 270.95368247, 0.04521843, 189.66757773, -2534.80586341, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 67.73842062, 5.207e-05, 203.21526185, 0.00015621, 677.38420616, 0.00052069, -67.73842062, -5.207e-05, -203.21526185, -0.00015621, -677.38420616, -0.00052069, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 12.45, 5.15, 3.95)
    ops.node(122008, 12.45, 5.15, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.165, 29991765.57221067, 12496568.98842111, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 247.13016636, 0.00064714, 295.38829594, 0.0088345, 29.53882959, 0.04249813, -247.13016636, -0.00064714, -295.38829594, -0.0088345, -29.53882959, -0.04249813, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 148.90318602, 0.00093629, 177.98012694, 0.00777796, 17.79801269, 0.02976578, -148.90318602, -0.00093629, -177.98012694, -0.00777796, -17.79801269, -0.02976578, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 250.31271001, 0.01294288, 250.31271001, 0.03882865, 175.21889701, -2677.36494219, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 62.5781775, 0.00010379, 187.73453251, 0.00031138, 625.78177503, 0.00103794, -62.5781775, -0.00010379, -187.73453251, -0.00031138, -625.78177503, -0.00103794, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 183.09760474, 0.01872571, 183.09760474, 0.05617714, 128.16832332, -1902.90653831, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 45.77440118, 7.592e-05, 137.32320355, 0.00022777, 457.74401184, 0.00075923, -45.77440118, -7.592e-05, -137.32320355, -0.00022777, -457.74401184, -0.00075923, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 10.3, 3.95)
    ops.node(122009, 0.0, 10.3, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.12, 29277024.7654951, 12198760.31895629, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 143.40326224, 0.00077742, 171.92648781, 0.00957774, 17.19264878, 0.0442434, -143.40326224, -0.00077742, -171.92648781, -0.00957774, -17.19264878, -0.0442434, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 95.0061198, 0.00095708, 113.90304686, 0.00900466, 11.39030469, 0.03704506, -95.0061198, -0.00095708, -113.90304686, -0.00900466, -11.39030469, -0.03704506, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 152.60919832, 0.01554841, 152.60919832, 0.04664522, 106.82643882, -1925.83228754, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 38.15229958, 8.914e-05, 114.45689874, 0.00026741, 381.52299579, 0.00089135, -38.15229958, -8.914e-05, -114.45689874, -0.00026741, -381.52299579, -0.00089135, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 138.65964388, 0.01914162, 138.65964388, 0.05742487, 97.06175072, -1573.06599426, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 34.66491097, 8.099e-05, 103.99473291, 0.00024296, 346.6491097, 0.00080988, -34.66491097, -8.099e-05, -103.99473291, -0.00024296, -346.6491097, -0.00080988, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 2.95, 10.3, 3.975)
    ops.node(122010, 2.95, 10.3, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.28, 29374815.93712174, 12239506.64046739, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 523.62109037, 0.00058131, 630.35276424, 0.00979361, 63.03527642, 0.03798134, -523.62109037, -0.00058131, -630.35276424, -0.00979361, -63.03527642, -0.03798134, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 249.48998854, 0.00074713, 300.34447965, 0.00874578, 30.03444797, 0.02890755, -249.48998854, -0.00074713, -300.34447965, -0.00874578, -30.03444797, -0.02890755, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 415.76616433, 0.01162618, 415.76616433, 0.03487853, 291.03631503, -3087.69743838, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 103.94154108, 0.00010373, 311.82462325, 0.00031118, 1039.41541084, 0.00103727, -103.94154108, -0.00010373, -311.82462325, -0.00031118, -1039.41541084, -0.00103727, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 258.8920072, 0.01494267, 258.8920072, 0.04482802, 181.22440504, -2219.27842639, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 64.7230018, 6.459e-05, 194.1690054, 0.00019377, 647.23001799, 0.0006459, -64.7230018, -6.459e-05, -194.1690054, -0.00019377, -647.23001799, -0.0006459, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.7, 10.3, 3.975)
    ops.node(122011, 7.7, 10.3, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.3825, 28849840.55794065, 12020766.89914194, 0.01726381, 0.00710016, 0.02533266, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 803.2681385, 0.00056361, 968.4457593, 0.00842358, 96.84457593, 0.03271079, -803.2681385, -0.00056361, -968.4457593, -0.00842358, -96.84457593, -0.03271079, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 385.34537775, 0.00072757, 464.58471221, 0.00754581, 46.45847122, 0.02488, -385.34537775, -0.00072757, -464.58471221, -0.00754581, -46.45847122, -0.02488, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 633.24652939, 0.01127216, 633.24652939, 0.03381647, 443.27257058, -3884.08904391, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 158.31163235, 0.00011775, 474.93489705, 0.00035326, 1583.11632349, 0.00117754, -158.31163235, -0.00011775, -474.93489705, -0.00035326, -1583.11632349, -0.00117754, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 309.71446624, 0.01455137, 309.71446624, 0.04365411, 216.80012637, -2712.50449357, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 77.42861656, 5.759e-05, 232.28584968, 0.00017278, 774.28616559, 0.00057592, -77.42861656, -5.759e-05, -232.28584968, -0.00017278, -774.28616559, -0.00057592, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 12.45, 10.3, 3.95)
    ops.node(122012, 12.45, 10.3, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.165, 30830255.90546865, 12845939.96061194, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 247.27347218, 0.00066136, 295.28013635, 0.00927606, 29.52801364, 0.04458909, -247.27347218, -0.00066136, -295.28013635, -0.00927606, -29.52801364, -0.04458909, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 146.49382006, 0.00098497, 174.93471815, 0.00818375, 17.49347182, 0.03124889, -146.49382006, -0.00098497, -174.93471815, -0.00818375, -17.49347182, -0.03124889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 259.20641932, 0.01322726, 259.20641932, 0.03968179, 181.44449352, -2758.12130661, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 64.80160483, 0.00010456, 194.40481449, 0.00031368, 648.01604829, 0.00104559, -64.80160483, -0.00010456, -194.40481449, -0.00031368, -648.01604829, -0.00104559, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 189.45003145, 0.01969931, 189.45003145, 0.05909794, 132.61502201, -1939.94473666, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 47.36250786, 7.642e-05, 142.08752359, 0.00022926, 473.62507862, 0.00076421, -47.36250786, -7.642e-05, -142.08752359, -0.00022926, -473.62507862, -0.00076421, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 15.45, 3.95)
    ops.node(122013, 0.0, 15.45, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0875, 29709425.23400282, 12378927.18083451, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 106.04970262, 0.00087084, 126.34886312, 0.01103354, 12.63488631, 0.04543707, -106.04970262, -0.00087084, -126.34886312, -0.01103354, -12.63488631, -0.04543707, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 69.91056082, 0.00114919, 83.2922645, 0.01026266, 8.32922645, 0.03682963, -69.91056082, -0.00114919, -83.2922645, -0.01026266, -8.32922645, -0.03682963, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 136.58926899, 0.01741672, 136.58926899, 0.05225017, 95.61248829, -1967.25402829, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 34.14731725, 0.00010782, 102.44195174, 0.00032345, 341.47317248, 0.00107818, -34.14731725, -0.00010782, -102.44195174, -0.00032345, -341.47317248, -0.00107818, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 120.15451757, 0.02298378, 120.15451757, 0.06895133, 84.1081623, -1548.54375346, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 30.03862939, 9.485e-05, 90.11588818, 0.00028454, 300.38629393, 0.00094845, -30.03862939, -9.485e-05, -90.11588818, -0.00028454, -300.38629393, -0.00094845, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 2.95, 15.45, 3.975)
    ops.node(122014, 2.95, 15.45, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.28, 27667178.2657157, 11527990.94404821, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 513.51835971, 0.00058839, 619.1784121, 0.0096091, 61.91784121, 0.03547985, -513.51835971, -0.00058839, -619.1784121, -0.0096091, -61.91784121, -0.03547985, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 245.06292466, 0.00076808, 295.48636322, 0.00860038, 29.54863632, 0.02710488, -245.06292466, -0.00076808, -295.48636322, -0.00860038, -29.54863632, -0.02710488, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 386.26932343, 0.01176771, 386.26932343, 0.03530314, 270.3885264, -2925.34767618, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 96.56733086, 0.00010232, 289.70199257, 0.00030695, 965.67330856, 0.00102316, -96.56733086, -0.00010232, -289.70199257, -0.00030695, -965.67330856, -0.00102316, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 240.55146295, 0.0153615, 240.55146295, 0.04608451, 168.38602407, -2141.39135741, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 60.13786574, 6.372e-05, 180.41359721, 0.00019115, 601.37865738, 0.00063718, -60.13786574, -6.372e-05, -180.41359721, -0.00019115, -601.37865738, -0.00063718, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.7, 15.45, 3.975)
    ops.node(122015, 7.7, 15.45, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.3825, 30293828.9700036, 12622428.7375015, 0.01726381, 0.00710016, 0.02533266, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 804.90870894, 0.00055321, 968.29111096, 0.00864774, 96.8291111, 0.03436227, -804.90870894, -0.00055321, -968.29111096, -0.00864774, -96.8291111, -0.03436227, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 387.81925419, 0.000702, 466.5397856, 0.00772372, 46.65397856, 0.02607661, -387.81925419, -0.000702, -466.5397856, -0.00772372, -46.65397856, -0.02607661, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 666.26406033, 0.01106415, 666.26406033, 0.03319246, 466.38484223, -3886.74197214, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 166.56601508, 0.00011799, 499.69804525, 0.00035396, 1665.66015082, 0.00117988, -166.56601508, -0.00011799, -499.69804525, -0.00035396, -1665.66015082, -0.00117988, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 330.23885093, 0.01404008, 330.23885093, 0.04212025, 231.16719565, -2715.17362168, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 82.55971273, 5.848e-05, 247.6791382, 0.00017545, 825.59712732, 0.00058482, -82.55971273, -5.848e-05, -247.6791382, -0.00017545, -825.59712732, -0.00058482, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.45, 15.45, 3.95)
    ops.node(122016, 12.45, 15.45, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.165, 32711214.44554438, 13629672.68564349, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 251.95455224, 0.00066108, 299.85775109, 0.00889113, 29.98577511, 0.0474715, -251.95455224, -0.00066108, -299.85775109, -0.00889113, -29.98577511, -0.0474715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 149.99098985, 0.00097536, 178.50822896, 0.00785271, 17.8508229, 0.03305196, -149.99098985, -0.00097536, -178.50822896, -0.00785271, -17.8508229, -0.03305196, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 271.81465349, 0.01322156, 271.81465349, 0.03966468, 190.27025744, -2747.45851791, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 67.95366337, 0.00010334, 203.86099012, 0.00031002, 679.53663372, 0.0010334, -67.95366337, -0.00010334, -203.86099012, -0.00031002, -679.53663372, -0.0010334, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 199.78042711, 0.01950723, 199.78042711, 0.05852169, 139.84629898, -1935.92838554, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 49.94510678, 7.595e-05, 149.83532033, 0.00022786, 499.45106777, 0.00075954, -49.94510678, -7.595e-05, -149.83532033, -0.00022786, -499.45106777, -0.00075954, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 20.6, 3.95)
    ops.node(122017, 0.0, 20.6, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.0875, 29351725.96147385, 12229885.81728077, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 105.87340418, 0.00091517, 126.15089944, 0.01082997, 12.61508994, 0.04430267, -105.87340418, -0.00091517, -126.15089944, -0.01082997, -12.61508994, -0.04430267, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 70.02787157, 0.00123208, 83.44002021, 0.01012323, 8.34400202, 0.0359714, -70.02787157, -0.00123208, -83.44002021, -0.01012323, -8.34400202, -0.0359714, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 134.52204321, 0.0183035, 134.52204321, 0.0549105, 94.16543024, -1940.02719802, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 33.6305108, 0.00010748, 100.89153241, 0.00032244, 336.30510802, 0.0010748, -33.6305108, -0.00010748, -100.89153241, -0.00032244, -336.30510802, -0.0010748, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 118.37641417, 0.02464154, 118.37641417, 0.07392461, 82.86348992, -1531.27760757, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 29.59410354, 9.458e-05, 88.78231063, 0.00028374, 295.94103542, 0.0009458, -29.59410354, -9.458e-05, -88.78231063, -0.00028374, -295.94103542, -0.0009458, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 2.95, 20.6, 3.975)
    ops.node(122018, 2.95, 20.6, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.28, 31588365.65630184, 13161819.0234591, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 509.52546186, 0.00059118, 610.92749448, 0.00950666, 61.09274945, 0.04011251, -509.52546186, -0.00059118, -610.92749448, -0.00950666, -61.09274945, -0.04011251, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 246.15782672, 0.00078618, 295.1463579, 0.00852711, 29.51463579, 0.03041847, -246.15782672, -0.00078618, -295.1463579, -0.00852711, -29.51463579, -0.03041847, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 440.5993121, 0.01182355, 440.5993121, 0.03547066, 308.41951847, -2932.87198333, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 110.14982803, 0.00010222, 330.44948408, 0.00030666, 1101.49828025, 0.0010222, -110.14982803, -0.00010222, -330.44948408, -0.00030666, -1101.49828025, -0.0010222, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 275.0943194, 0.01572353, 275.0943194, 0.04717058, 192.56602358, -2145.06921668, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 68.77357985, 6.382e-05, 206.32073955, 0.00019147, 687.7357985, 0.00063822, -68.77357985, -6.382e-05, -206.32073955, -0.00019147, -687.7357985, -0.00063822, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 7.7, 20.6, 3.975)
    ops.node(122019, 7.7, 20.6, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.3825, 28641774.63244529, 11934072.76351887, 0.01726381, 0.00710016, 0.02533266, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 837.7606342, 0.00056763, 1010.25430541, 0.0064708, 101.02543054, 0.03051748, -837.7606342, -0.00056763, -1010.25430541, -0.0064708, -101.02543054, -0.03051748, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 403.59010487, 0.00072045, 486.68870846, 0.00584123, 48.66887085, 0.02300376, -403.59010487, -0.00072045, -486.68870846, -0.00584123, -48.66887085, -0.02300376, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 607.97297775, 0.01135264, 607.97297775, 0.03405793, 425.58108443, -3380.76490739, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 151.99324444, 0.00011388, 455.97973331, 0.00034163, 1519.93244438, 0.00113875, -151.99324444, -0.00011388, -455.97973331, -0.00034163, -1519.93244438, -0.00113875, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 275.70439893, 0.01440895, 275.70439893, 0.04322686, 192.99307925, -2488.42530776, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 68.92609973, 5.164e-05, 206.7782992, 0.00015492, 689.26099733, 0.0005164, -68.92609973, -5.164e-05, -206.7782992, -0.00015492, -689.26099733, -0.0005164, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 12.45, 20.6, 3.95)
    ops.node(122020, 12.45, 20.6, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.165, 29651021.27614199, 12354592.1983925, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 247.55586155, 0.00066076, 295.97303834, 0.01083536, 29.59730383, 0.04377083, -247.55586155, -0.00066076, -295.97303834, -0.01083536, -29.59730383, -0.04377083, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 147.75394858, 0.0009742, 176.65178604, 0.00947649, 17.6651786, 0.0309887, -147.75394858, -0.0009742, -176.65178604, -0.00947649, -17.6651786, -0.0309887, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 266.382152, 0.01321514, 266.382152, 0.03964541, 186.4675064, -3154.17232811, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 66.595538, 0.00011173, 199.786614, 0.00033518, 665.95538, 0.00111727, -66.595538, -0.00011173, -199.786614, -0.00033518, -665.95538, -0.00111727, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 191.27620453, 0.01948394, 191.27620453, 0.05845181, 133.89334317, -2119.89867226, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 47.81905113, 8.023e-05, 143.4571534, 0.00024068, 478.19051132, 0.00080226, -47.81905113, -8.023e-05, -143.4571534, -0.00024068, -478.19051132, -0.00080226, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 0.0, 25.75, 3.95)
    ops.node(122021, 0.0, 25.75, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.12, 29031822.8264651, 12096592.84436046, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 141.50198532, 0.00080567, 169.67455346, 0.01123859, 16.96745535, 0.04537744, -141.50198532, -0.00080567, -169.67455346, -0.01123859, -16.96745535, -0.04537744, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 94.48656768, 0.00100753, 113.29852471, 0.01054807, 11.32985247, 0.03816234, -94.48656768, -0.00100753, -113.29852471, -0.01054807, -11.32985247, -0.03816234, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 163.27124089, 0.0161134, 163.27124089, 0.04834021, 114.28986862, -2245.83447056, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 40.81781022, 9.617e-05, 122.45343067, 0.0002885, 408.17810222, 0.00096168, -40.81781022, -9.617e-05, -122.45343067, -0.0002885, -408.17810222, -0.00096168, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 146.42945955, 0.02015062, 146.42945955, 0.06045187, 102.50062169, -1788.91340615, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 36.60736489, 8.625e-05, 109.82209466, 0.00025874, 366.07364888, 0.00086248, -36.60736489, -8.625e-05, -109.82209466, -0.00025874, -366.07364888, -0.00086248, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 2.95, 25.75, 3.975)
    ops.node(122022, 2.95, 25.75, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.28, 29072619.35094796, 12113591.39622832, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 522.2824496, 0.00058769, 628.97012364, 0.00916681, 62.89701236, 0.03695933, -522.2824496, -0.00058769, -628.97012364, -0.00916681, -62.89701236, -0.03695933, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 249.1348107, 0.00076268, 300.02607365, 0.00821157, 30.00260736, 0.02809065, -249.1348107, -0.00076268, -300.02607365, -0.00821157, -30.00260736, -0.02809065, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 401.95818262, 0.01175382, 401.95818262, 0.03526146, 281.37072784, -2845.61649021, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 100.48954566, 0.00010132, 301.46863697, 0.00030397, 1004.89545656, 0.00101325, -100.48954566, -0.00010132, -301.46863697, -0.00030397, -1004.89545656, -0.00101325, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 250.74293867, 0.01525367, 250.74293867, 0.04576101, 175.52005707, -2102.32123877, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 62.68573467, 6.321e-05, 188.057204, 0.00018962, 626.85734668, 0.00063207, -62.68573467, -6.321e-05, -188.057204, -0.00018962, -626.85734668, -0.00063207, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 7.7, 25.75, 3.975)
    ops.node(122023, 7.7, 25.75, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.3825, 30722261.99766035, 12800942.49902515, 0.01726381, 0.00710016, 0.02533266, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 817.56234677, 0.00055537, 982.71459985, 0.00647994, 98.27145998, 0.03258102, -817.56234677, -0.00055537, -982.71459985, -0.00647994, -98.27145998, -0.03258102, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 394.39305171, 0.00070221, 474.06269567, 0.00584156, 47.40626957, 0.02447034, -394.39305171, -0.00070221, -474.06269567, -0.00584156, -47.40626957, -0.02447034, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 654.29076925, 0.01110737, 654.29076925, 0.03332212, 458.00353847, -3357.4806688, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 163.57269231, 0.00011425, 490.71807694, 0.00034276, 1635.72692312, 0.00114252, -163.57269231, -0.00011425, -490.71807694, -0.00034276, -1635.72692312, -0.00114252, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 300.75308392, 0.01404414, 300.75308392, 0.04213243, 210.52715875, -2477.84257853, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 75.18827098, 5.252e-05, 225.56481294, 0.00015755, 751.88270981, 0.00052517, -75.18827098, -5.252e-05, -225.56481294, -0.00015755, -751.88270981, -0.00052517, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 12.45, 25.75, 3.95)
    ops.node(122024, 12.45, 25.75, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.165, 29509492.97083487, 12295622.07118119, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 253.2491176, 0.00067, 302.80945116, 0.01062233, 30.28094512, 0.04325917, -253.2491176, -0.00067, -302.80945116, -0.01062233, -30.28094512, -0.04325917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 152.92894095, 0.00097679, 182.85682143, 0.00929334, 18.28568214, 0.0306105, -152.92894095, -0.00097679, -182.85682143, -0.00929334, -18.28568214, -0.0306105, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 263.1251733, 0.01340009, 263.1251733, 0.04020026, 184.18762131, -3091.96483893, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 65.78129332, 0.00011089, 197.34387997, 0.00033267, 657.81293325, 0.0011089, -65.78129332, -0.00011089, -197.34387997, -0.00033267, -657.81293325, -0.0011089, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 189.24922337, 0.0195358, 189.24922337, 0.05860741, 132.47445636, -2092.03494265, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 47.31230584, 7.976e-05, 141.93691752, 0.00023927, 473.12305842, 0.00079756, -47.31230584, -7.976e-05, -141.93691752, -0.00023927, -473.12305842, -0.00079756, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171025, 0.0, 30.9, 3.95)
    ops.node(122025, 0.0, 30.9, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1025, 171025, 122025, 0.075, 32469025.9492538, 13528760.81218908, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21025, 65.77533655, 0.0009762, 78.52286545, 0.01082734, 7.85228654, 0.05837078, -65.77533655, -0.0009762, -78.52286545, -0.01082734, -7.85228654, -0.05837078, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11025, 57.62518432, 0.00114762, 68.79318042, 0.01042349, 6.87931804, 0.05164296, -57.62518432, -0.00114762, -68.79318042, -0.01042349, -6.87931804, -0.05164296, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21025, 1025, 0.0, 110.862316, 0.019524, 110.862316, 0.05857201, 77.6036212, -1439.28313437, 0.05, 2, 0, 71025, 22025, 2, 3)
    ops.uniaxialMaterial('LimitState', 41025, 27.715579, 9.342e-05, 83.146737, 0.00028025, 277.15579, 0.00093418, -27.715579, -9.342e-05, -83.146737, -0.00028025, -277.15579, -0.00093418, 0.4, 0.3, 0.003, 0.0, 0.0, 21025, 2)
    ops.limitCurve('ThreePoint', 11025, 1025, 0.0, 103.58156724, 0.02295249, 103.58156724, 0.06885747, 72.50709707, -1229.1242787, 0.05, 2, 0, 71025, 22025, 1, 3)
    ops.uniaxialMaterial('LimitState', 31025, 25.89539181, 8.728e-05, 77.68617543, 0.00026185, 258.95391811, 0.00087283, -25.89539181, -8.728e-05, -77.68617543, -0.00026185, -258.95391811, -0.00087283, 0.4, 0.3, 0.003, 0.0, 0.0, 11025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1025, 99999, 'P', 41025, 'Vy', 31025, 'Vz', 21025, 'My', 11025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171025, 71025, 171025, 1025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122025, 122025, 22025, 1025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171026, 2.95, 30.9, 3.975)
    ops.node(122026, 2.95, 30.9, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1026, 171026, 122026, 0.16, 29547896.73788899, 12311623.64078708, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21026, 191.72428849, 0.0007811, 230.10847939, 0.00988906, 23.01084794, 0.03951777, -191.72428849, -0.0007811, -230.10847939, -0.00988906, -23.01084794, -0.03951777, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11026, 175.82935502, 0.0007811, 211.0312983, 0.00988906, 21.10312983, 0.03951777, -175.82935502, -0.0007811, -211.0312983, -0.00988906, -21.10312983, -0.03951777, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21026, 1026, 0.0, 189.05585112, 0.01562193, 189.05585112, 0.0468658, 132.33909579, -2187.21065672, 0.05, 2, 0, 71026, 22026, 2, 3)
    ops.uniaxialMaterial('LimitState', 41026, 47.26396278, 8.206e-05, 141.79188834, 0.00024617, 472.63962781, 0.00082058, -47.26396278, -8.206e-05, -141.79188834, -0.00024617, -472.63962781, -0.00082058, 0.4, 0.3, 0.003, 0.0, 0.0, 21026, 2)
    ops.limitCurve('ThreePoint', 11026, 1026, 0.0, 189.05585112, 0.01562193, 189.05585112, 0.0468658, 132.33909579, -2187.21065672, 0.05, 2, 0, 71026, 22026, 1, 3)
    ops.uniaxialMaterial('LimitState', 31026, 47.26396278, 8.206e-05, 141.79188834, 0.00024617, 472.63962781, 0.00082058, -47.26396278, -8.206e-05, -141.79188834, -0.00024617, -472.63962781, -0.00082058, 0.4, 0.3, 0.003, 0.0, 0.0, 11026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1026, 99999, 'P', 41026, 'Vy', 31026, 'Vz', 21026, 'My', 11026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171026, 71026, 171026, 1026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122026, 122026, 22026, 1026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171027, 7.7, 30.9, 3.975)
    ops.node(122027, 7.7, 30.9, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1027, 171027, 122027, 0.2475, 27001247.05718, 11250519.60715833, 0.00841652, 0.00686297, 0.00459422, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21027, 268.70941775, 0.00073709, 324.02568918, 0.00898016, 32.40256892, 0.02625283, -268.70941775, -0.00073709, -324.02568918, -0.00898016, -32.40256892, -0.02625283, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11027, 352.4024217, 0.00066381, 424.94765728, 0.00929407, 42.49476573, 0.02855365, -352.4024217, -0.00066381, -424.94765728, -0.00929407, -42.49476573, -0.02855365, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21027, 1027, 0.0, 216.00540518, 0.0147417, 216.00540518, 0.04422511, 151.20378362, -2033.6376961, 0.05, 2, 0, 71027, 22027, 2, 3)
    ops.uniaxialMaterial('LimitState', 41027, 54.00135129, 6.633e-05, 162.00405388, 0.00019898, 540.01351294, 0.00066326, -54.00135129, -6.633e-05, -162.00405388, -0.00019898, -540.01351294, -0.00066326, 0.4, 0.3, 0.003, 0.0, 0.0, 21027, 2)
    ops.limitCurve('ThreePoint', 11027, 1027, 0.0, 264.00660633, 0.01327621, 264.00660633, 0.03982863, 184.80462443, -2264.83652857, 0.05, 2, 0, 71027, 22027, 1, 3)
    ops.uniaxialMaterial('LimitState', 31027, 66.00165158, 8.106e-05, 198.00495474, 0.00024319, 660.01651581, 0.00081065, -66.00165158, -8.106e-05, -198.00495474, -0.00024319, -660.01651581, -0.00081065, 0.4, 0.3, 0.003, 0.0, 0.0, 11027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1027, 99999, 'P', 41027, 'Vy', 31027, 'Vz', 21027, 'My', 11027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171027, 71027, 171027, 1027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122027, 122027, 22027, 1027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171028, 12.45, 30.9, 3.95)
    ops.node(122028, 12.45, 30.9, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1028, 171028, 122028, 0.1225, 28756295.38523661, 11981789.74384859, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21028, 122.57487997, 0.00081291, 147.27602232, 0.0095723, 14.72760223, 0.04115666, -122.57487997, -0.00081291, -147.27602232, -0.0095723, -14.72760223, -0.04115666, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11028, 116.62562376, 0.00081291, 140.12787916, 0.0095723, 14.01278792, 0.04115666, -116.62562376, -0.00081291, -140.12787916, -0.0095723, -14.01278792, -0.04115666, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21028, 1028, 0.0, 143.53796846, 0.01625825, 143.53796846, 0.04877474, 100.47657792, -1728.99801535, 0.05, 2, 0, 71028, 22028, 2, 3)
    ops.uniaxialMaterial('LimitState', 41028, 35.88449212, 8.361e-05, 107.65347635, 0.00025084, 358.84492115, 0.00083613, -35.88449212, -8.361e-05, -107.65347635, -0.00025084, -358.84492115, -0.00083613, 0.4, 0.3, 0.003, 0.0, 0.0, 21028, 2)
    ops.limitCurve('ThreePoint', 11028, 1028, 0.0, 143.53796846, 0.01625825, 143.53796846, 0.04877474, 100.47657792, -1728.99801535, 0.05, 2, 0, 71028, 22028, 1, 3)
    ops.uniaxialMaterial('LimitState', 31028, 35.88449212, 8.361e-05, 107.65347635, 0.00025084, 358.84492115, 0.00083613, -35.88449212, -8.361e-05, -107.65347635, -0.00025084, -358.84492115, -0.00083613, 0.4, 0.3, 0.003, 0.0, 0.0, 11028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1028, 99999, 'P', 41028, 'Vy', 31028, 'Vz', 21028, 'My', 11028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171028, 71028, 171028, 1028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122028, 122028, 22028, 1028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.7, 0.0, 6.825)
    ops.node(123003, 7.7, 0.0, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.175, 31241751.10258349, 13017396.29274312, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 137.55369086, 0.00082954, 165.16264166, 0.00968079, 16.51626417, 0.03643569, -137.55369086, -0.00082954, -165.16264166, -0.00968079, -16.51626417, -0.03643569, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 217.12437017, 0.00066601, 260.7042699, 0.01043435, 26.07042699, 0.0442383, -217.12437017, -0.00066601, -260.7042699, -0.01043435, -26.07042699, -0.0442383, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 180.41383615, 0.01659089, 180.41383615, 0.04977268, 126.2896853, -1581.19835584, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 45.10345904, 6.771e-05, 135.31037711, 0.00020314, 451.03459037, 0.00067713, -45.10345904, -6.771e-05, -135.31037711, -0.00020314, -451.03459037, -0.00067713, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 215.22138815, 0.01332024, 215.22138815, 0.03996072, 150.65497171, -2028.92665436, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 53.80534704, 8.078e-05, 161.41604111, 0.00024233, 538.05347038, 0.00080777, -53.80534704, -8.078e-05, -161.41604111, -0.00024233, -538.05347038, -0.00080777, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.45, 0.0, 6.8)
    ops.node(123004, 12.45, 0.0, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 28937022.7861094, 12057092.82754558, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 46.35408173, 0.00126293, 55.46170286, 0.0119218, 5.54617029, 0.04853286, -46.35408173, -0.00126293, -55.46170286, -0.0119218, -5.54617029, -0.04853286, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 46.35408173, 0.00126293, 55.46170286, 0.0119218, 5.54617029, 0.04853286, -46.35408173, -0.00126293, -55.46170286, -0.0119218, -5.54617029, -0.04853286, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 94.18367217, 0.02525852, 94.18367217, 0.07577555, 65.92857052, -1406.27145767, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 23.54591804, 0.00010686, 70.63775413, 0.00032058, 235.45918042, 0.00106861, -23.54591804, -0.00010686, -70.63775413, -0.00032058, -235.45918042, -0.00106861, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 94.18367217, 0.02525852, 94.18367217, 0.07577555, 65.92857052, -1406.27145767, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 23.54591804, 0.00010686, 70.63775413, 0.00032058, 235.45918042, 0.00106861, -23.54591804, -0.00010686, -70.63775413, -0.00032058, -235.45918042, -0.00106861, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 5.15, 6.8)
    ops.node(123005, 0.0, 5.15, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 26152220.18426416, 10896758.41011007, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 44.65307726, 0.00126893, 53.32272127, 0.01025543, 5.33227213, 0.03852314, -44.65307726, -0.00126893, -53.32272127, -0.01025543, -5.33227213, -0.03852314, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 44.65307726, 0.00126893, 53.32272127, 0.01025543, 5.33227213, 0.03852314, -44.65307726, -0.00126893, -53.32272127, -0.01025543, -5.33227213, -0.03852314, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 84.87912057, 0.02537866, 84.87912057, 0.07613598, 59.4153844, -1292.21261177, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 21.21978014, 0.00010656, 63.65934043, 0.00031968, 212.19780142, 0.00106559, -21.21978014, -0.00010656, -63.65934043, -0.00031968, -212.19780142, -0.00106559, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 84.87912057, 0.02537866, 84.87912057, 0.07613598, 59.4153844, -1292.21261177, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 21.21978014, 0.00010656, 63.65934043, 0.00031968, 212.19780142, 0.00106559, -21.21978014, -0.00010656, -63.65934043, -0.00031968, -212.19780142, -0.00106559, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 2.95, 5.15, 6.825)
    ops.node(123006, 2.95, 5.15, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.21, 28172494.4326057, 11738539.34691904, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 330.81961083, 0.00061135, 399.20363474, 0.01116139, 39.92036347, 0.04128288, -330.81961083, -0.00061135, -399.20363474, -0.01116139, -39.92036347, -0.04128288, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 163.9087169, 0.00082025, 197.79043748, 0.00995545, 19.77904375, 0.03136145, -163.9087169, -0.00082025, -197.79043748, -0.00995545, -19.77904375, -0.03136145, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 273.24241655, 0.01222699, 273.24241655, 0.03668097, 191.26969158, -2572.48508538, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 68.31060414, 9.477e-05, 204.93181241, 0.00028432, 683.10604137, 0.00094772, -68.31060414, -9.477e-05, -204.93181241, -0.00028432, -683.10604137, -0.00094772, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 190.68728688, 0.01640498, 190.68728688, 0.04921493, 133.48110082, -1766.25424122, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 47.67182172, 6.614e-05, 143.01546516, 0.00019842, 476.71821721, 0.00066139, -47.67182172, -6.614e-05, -143.01546516, -0.00019842, -476.71821721, -0.00066139, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 7.7, 5.15, 6.825)
    ops.node(123007, 7.7, 5.15, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.2625, 26829606.16751771, 11179002.56979905, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 519.30275128, 0.00058152, 627.03004529, 0.00670698, 62.70300453, 0.03240923, -519.30275128, -0.00058152, -627.03004529, -0.00670698, -62.70300453, -0.03240923, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 228.239198, 0.00085179, 275.58651347, 0.00594025, 27.55865135, 0.02249394, -228.239198, -0.00085179, -275.58651347, -0.00594025, -27.55865135, -0.02249394, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 365.41854195, 0.01163046, 365.41854195, 0.03489137, 255.79297937, -2671.23720751, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 91.35463549, 0.00010647, 274.06390646, 0.00031941, 913.54635488, 0.00106469, -91.35463549, -0.00010647, -274.06390646, -0.00031941, -913.54635488, -0.00106469, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 172.79147307, 0.01703578, 172.79147307, 0.05110733, 120.95403115, -1766.38544944, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 43.19786827, 5.034e-05, 129.59360481, 0.00015103, 431.97868269, 0.00050345, -43.19786827, -5.034e-05, -129.59360481, -0.00015103, -431.97868269, -0.00050345, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 12.45, 5.15, 6.8)
    ops.node(123008, 12.45, 5.15, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.125, 34109029.68749252, 14212095.70312188, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 167.95611232, 0.00068342, 199.49716926, 0.00931547, 19.94971693, 0.05846468, -167.95611232, -0.00068342, -199.49716926, -0.00931547, -19.94971693, -0.05846468, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 88.5307443, 0.00113323, 105.15623775, 0.00810379, 10.51562378, 0.03770281, -88.5307443, -0.00113323, -105.15623775, -0.00810379, -10.51562378, -0.03770281, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 202.76357697, 0.01366848, 202.76357697, 0.04100545, 141.93450388, -2248.72606903, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 50.69089424, 9.759e-05, 152.07268273, 0.00029276, 506.90894242, 0.00097586, -50.69089424, -9.759e-05, -152.07268273, -0.00029276, -506.90894242, -0.00097586, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 146.16271202, 0.02266454, 146.16271202, 0.06799363, 102.31389841, -1403.98401329, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 36.540678, 7.035e-05, 109.62203401, 0.00021104, 365.40678004, 0.00070345, -36.540678, -7.035e-05, -109.62203401, -0.00021104, -365.40678004, -0.00070345, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 10.3, 6.8)
    ops.node(123009, 0.0, 10.3, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0875, 32875036.15571297, 13697931.73154707, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 86.08774138, 0.00083592, 102.73558719, 0.01209748, 10.27355872, 0.06123526, -86.08774138, -0.00083592, -102.73558719, -0.01209748, -10.27355872, -0.06123526, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 56.15606651, 0.00110642, 67.01565606, 0.01120529, 6.70156561, 0.0491503, -56.15606651, -0.00110642, -67.01565606, -0.01120529, -6.70156561, -0.0491503, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 135.0443725, 0.01671841, 135.0443725, 0.05015523, 94.53106075, -1854.36286258, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 33.76109312, 9.633e-05, 101.28327937, 0.000289, 337.61093125, 0.00096334, -33.76109312, -9.633e-05, -101.28327937, -0.000289, -337.61093125, -0.00096334, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 118.83474689, 0.02212832, 118.83474689, 0.06638496, 83.18432282, -1365.12028037, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 29.70868672, 8.477e-05, 89.12606017, 0.00025431, 297.08686723, 0.00084771, -29.70868672, -8.477e-05, -89.12606017, -0.00025431, -297.08686723, -0.00084771, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 2.95, 10.3, 6.825)
    ops.node(123010, 2.95, 10.3, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.21, 30873640.36597519, 12864016.81915633, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 331.58281538, 0.00060656, 398.56048601, 0.01030782, 39.8560486, 0.04400039, -331.58281538, -0.00060656, -398.56048601, -0.01030782, -39.8560486, -0.04400039, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 164.68035332, 0.00081147, 197.94476255, 0.00921171, 19.79447625, 0.03315552, -164.68035332, -0.00081147, -197.94476255, -0.00921171, -19.79447625, -0.03315552, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 290.00420746, 0.01213122, 290.00420746, 0.03639365, 203.00294522, -2396.63881468, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 72.50105187, 9.179e-05, 217.5031556, 0.00027536, 725.01051866, 0.00091786, -72.50105187, -9.179e-05, -217.5031556, -0.00027536, -725.01051866, -0.00091786, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 204.1077103, 0.0162293, 204.1077103, 0.0486879, 142.87539721, -1673.48794802, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 51.02692757, 6.46e-05, 153.08078272, 0.0001938, 510.26927575, 0.000646, -51.02692757, -6.46e-05, -153.08078272, -0.0001938, -510.26927575, -0.000646, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.7, 10.3, 6.825)
    ops.node(123011, 7.7, 10.3, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.2625, 29809683.56008601, 12420701.48336917, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 518.98486103, 0.00059066, 624.86729451, 0.0074924, 62.48672945, 0.03718735, -518.98486103, -0.00059066, -624.86729451, -0.0074924, -62.48672945, -0.03718735, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 225.22830912, 0.00089553, 271.17901645, 0.00662886, 27.11790165, 0.02575407, -225.22830912, -0.00089553, -271.17901645, -0.00662886, -27.11790165, -0.02575407, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 410.26268072, 0.01181311, 410.26268072, 0.03543932, 287.1838765, -2793.17373104, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 102.56567018, 0.00010759, 307.69701054, 0.00032276, 1025.6567018, 0.00107585, -102.56567018, -0.00010759, -307.69701054, -0.00032276, -1025.6567018, -0.00107585, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 196.57140571, 0.01791062, 196.57140571, 0.05373185, 137.599984, -1812.43836394, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 49.14285143, 5.155e-05, 147.42855428, 0.00015464, 491.42851428, 0.00051548, -49.14285143, -5.155e-05, -147.42855428, -0.00015464, -491.42851428, -0.00051548, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 12.45, 10.3, 6.8)
    ops.node(123012, 12.45, 10.3, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.125, 30651788.08610618, 12771578.36921091, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 170.93323087, 0.00067117, 204.61411837, 0.01122278, 20.46141184, 0.05428408, -170.93323087, -0.00067117, -204.61411837, -0.01122278, -20.46141184, -0.05428408, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 81.9029686, 0.00111613, 98.04122714, 0.00963678, 9.80412271, 0.0355695, -81.9029686, -0.00111613, -98.04122714, -0.00963678, -9.80412271, -0.0355695, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 198.82760926, 0.01342333, 198.82760926, 0.04026998, 139.17932648, -2611.25885831, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 49.70690232, 0.00010648, 149.12070695, 0.00031945, 497.06902316, 0.00106485, -49.70690232, -0.00010648, -149.12070695, -0.00031945, -497.06902316, -0.00106485, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 146.05766855, 0.02232268, 146.05766855, 0.06696803, 102.24036799, -1545.24830007, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 36.51441714, 7.822e-05, 109.54325141, 0.00023467, 365.14417138, 0.00078223, -36.51441714, -7.822e-05, -109.54325141, -0.00023467, -365.14417138, -0.00078223, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 15.45, 6.8)
    ops.node(123013, 0.0, 15.45, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 27713405.78159033, 11547252.40899597, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 49.49404594, 0.0011565, 59.10214333, 0.00989328, 5.91021433, 0.04131983, -49.49404594, -0.0011565, -59.10214333, -0.00989328, -5.91021433, -0.04131983, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 49.49404594, 0.0011565, 59.10214333, 0.00989328, 5.91021433, 0.04131983, -49.49404594, -0.0011565, -59.10214333, -0.00989328, -5.91021433, -0.04131983, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 87.54483333, 0.02312997, 87.54483333, 0.0693899, 61.28138333, -1266.99659044, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 21.88620833, 0.00010371, 65.658625, 0.00031114, 218.86208333, 0.00103714, -21.88620833, -0.00010371, -65.658625, -0.00031114, -218.86208333, -0.00103714, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 87.54483333, 0.02312997, 87.54483333, 0.0693899, 61.28138333, -1266.99659044, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 21.88620833, 0.00010371, 65.658625, 0.00031114, 218.86208333, 0.00103714, -21.88620833, -0.00010371, -65.658625, -0.00031114, -218.86208333, -0.00103714, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 2.95, 15.45, 6.825)
    ops.node(123014, 2.95, 15.45, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.21, 28408137.80361635, 11836724.08484015, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 330.30931934, 0.00061723, 398.57276749, 0.01114649, 39.85727675, 0.04178199, -330.30931934, -0.00061723, -398.57276749, -0.01114649, -39.85727675, -0.04178199, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 163.60201472, 0.00083344, 197.41286108, 0.00995065, 19.74128611, 0.03172193, -163.60201472, -0.00083344, -197.41286108, -0.00995065, -19.74128611, -0.03172193, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 276.65142581, 0.01234463, 276.65142581, 0.0370339, 193.65599806, -2626.07181325, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 69.16285645, 9.516e-05, 207.48856935, 0.00028548, 691.62856452, 0.00095159, -69.16285645, -9.516e-05, -207.48856935, -0.00028548, -691.62856452, -0.00095159, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 192.87792109, 0.01666888, 192.87792109, 0.05000665, 135.01454477, -1784.55263065, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 48.21948027, 6.634e-05, 144.65844082, 0.00019903, 482.19480273, 0.00066343, -48.21948027, -6.634e-05, -144.65844082, -0.00019903, -482.19480273, -0.00066343, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.7, 15.45, 6.825)
    ops.node(123015, 7.7, 15.45, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.2625, 29458187.76720933, 12274244.90300389, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 526.22555565, 0.000577, 633.92872109, 0.0091045, 63.39287211, 0.03839115, -526.22555565, -0.000577, -633.92872109, -0.0091045, -63.39287211, -0.03839115, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 232.40299954, 0.00083671, 279.96917804, 0.00792057, 27.9969178, 0.02678281, -232.40299954, -0.00083671, -279.96917804, -0.00792057, -27.9969178, -0.02678281, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 421.82338726, 0.01153999, 421.82338726, 0.03461998, 295.27637108, -3230.80162401, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 105.45584682, 0.00011194, 316.36754045, 0.00033581, 1054.55846816, 0.00111937, -105.45584682, -0.00011194, -316.36754045, -0.00033581, -1054.55846816, -0.00111937, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 193.70052648, 0.01673422, 193.70052648, 0.05020265, 135.59036854, -1974.43204421, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 48.42513162, 5.14e-05, 145.27539486, 0.0001542, 484.2513162, 0.00051401, -48.42513162, -5.14e-05, -145.27539486, -0.0001542, -484.2513162, -0.00051401, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.45, 15.45, 6.8)
    ops.node(123016, 12.45, 15.45, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.125, 28711573.28921484, 11963155.53717285, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 176.27009023, 0.00069391, 211.41958555, 0.00983328, 21.14195856, 0.04850707, -176.27009023, -0.00069391, -211.41958555, -0.00983328, -21.14195856, -0.04850707, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 84.45565526, 0.00114545, 101.29670671, 0.00852569, 10.12967067, 0.03181612, -84.45565526, -0.00114545, -101.29670671, -0.00852569, -10.12967067, -0.03181612, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 180.4398728, 0.0138781, 180.4398728, 0.04163431, 126.30791096, -2328.29268448, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 45.1099682, 0.00010317, 135.3299046, 0.0003095, 451.099682, 0.00103167, -45.1099682, -0.00010317, -135.3299046, -0.0003095, -451.099682, -0.00103167, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 131.11820118, 0.02290897, 131.11820118, 0.06872692, 91.78274083, -1435.31868768, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 32.7795503, 7.497e-05, 98.33865089, 0.0002249, 327.79550295, 0.00074968, -32.7795503, -7.497e-05, -98.33865089, -0.0002249, -327.79550295, -0.00074968, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 20.6, 6.8)
    ops.node(123017, 0.0, 20.6, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 26524091.41939091, 11051704.75807955, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 47.54136619, 0.00115853, 56.70092503, 0.00924445, 5.6700925, 0.0371436, -47.54136619, -0.00115853, -56.70092503, -0.00924445, -5.6700925, -0.0371436, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 47.54136619, 0.00115853, 56.70092503, 0.00924445, 5.6700925, 0.0371436, -47.54136619, -0.00115853, -56.70092503, -0.00924445, -5.6700925, -0.0371436, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 79.73236128, 0.02317058, 79.73236128, 0.06951174, 55.8126529, -1212.45964637, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 19.93309032, 9.869e-05, 59.79927096, 0.00029608, 199.3309032, 0.00098694, -19.93309032, -9.869e-05, -59.79927096, -0.00029608, -199.3309032, -0.00098694, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 79.73236128, 0.02317058, 79.73236128, 0.06951174, 55.8126529, -1212.45964637, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 19.93309032, 9.869e-05, 59.79927096, 0.00029608, 199.3309032, 0.00098694, -19.93309032, -9.869e-05, -59.79927096, -0.00029608, -199.3309032, -0.00098694, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 2.95, 20.6, 6.825)
    ops.node(123018, 2.95, 20.6, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.21, 33340524.8414375, 13891885.35059896, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 343.04269949, 0.00061647, 409.75923451, 0.00949315, 40.97592345, 0.04552936, -343.04269949, -0.00061647, -409.75923451, -0.00949315, -40.97592345, -0.04552936, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 170.39393446, 0.00082553, 203.53293701, 0.00851178, 20.3532937, 0.03412111, -170.39393446, -0.00082553, -203.53293701, -0.00851178, -20.3532937, -0.03412111, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 311.98112477, 0.01232947, 311.98112477, 0.03698842, 218.38678734, -2379.359507, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 77.99528119, 9.144e-05, 233.98584358, 0.00027431, 779.95281192, 0.00091435, -77.99528119, -9.144e-05, -233.98584358, -0.00027431, -779.95281192, -0.00091435, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 220.52058886, 0.01651062, 220.52058886, 0.04953187, 154.3644122, -1665.06061294, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 55.13014721, 6.463e-05, 165.39044164, 0.00019389, 551.30147214, 0.0006463, -55.13014721, -6.463e-05, -165.39044164, -0.00019389, -551.30147214, -0.0006463, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 7.7, 20.6, 6.825)
    ops.node(123019, 7.7, 20.6, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.2625, 29093011.75661206, 12122088.23192169, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 531.09883265, 0.0005817, 640.12432867, 0.0077804, 64.01243287, 0.03662633, -531.09883265, -0.0005817, -640.12432867, -0.0077804, -64.01243287, -0.03662633, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 234.58715835, 0.00084522, 282.74388498, 0.00682524, 28.2743885, 0.02540363, -234.58715835, -0.00084522, -282.74388498, -0.00682524, -28.2743885, -0.02540363, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 407.1486713, 0.01163391, 407.1486713, 0.03490174, 285.00406991, -2968.50187924, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 101.78716782, 0.0001094, 305.36150347, 0.0003282, 1017.87167825, 0.00109399, -101.78716782, -0.0001094, -305.36150347, -0.0003282, -1017.87167825, -0.00109399, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 190.73666556, 0.01690445, 190.73666556, 0.05071336, 133.51566589, -1877.92486277, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 47.68416639, 5.125e-05, 143.05249917, 0.00015375, 476.84166391, 0.0005125, -47.68416639, -5.125e-05, -143.05249917, -0.00015375, -476.84166391, -0.0005125, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 12.45, 20.6, 6.8)
    ops.node(123020, 12.45, 20.6, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.125, 29369354.30670407, 12237230.96112669, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 175.72452977, 0.00067624, 210.66871257, 0.01202857, 21.06687126, 0.05227681, -175.72452977, -0.00067624, -210.66871257, -0.01202857, -21.06687126, -0.05227681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 84.53369805, 0.00109253, 101.34387818, 0.01025978, 10.13438782, 0.03449838, -84.53369805, -0.00109253, -101.34387818, -0.01025978, -10.13438782, -0.03449838, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 202.11267693, 0.01352478, 202.11267693, 0.04057435, 141.47887385, -2895.61185447, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 50.52816923, 0.00011297, 151.58450769, 0.00033891, 505.28169231, 0.00112971, -50.52816923, -0.00011297, -151.58450769, -0.00033891, -505.28169231, -0.00112971, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 145.4177138, 0.02185061, 145.4177138, 0.06555182, 101.79239966, -1653.63020749, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 36.35442845, 8.128e-05, 109.06328535, 0.00024384, 363.54428449, 0.00081281, -36.35442845, -8.128e-05, -109.06328535, -0.00024384, -363.54428449, -0.00081281, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 0.0, 25.75, 6.8)
    ops.node(123021, 0.0, 25.75, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0875, 28556396.76498147, 11898498.65207561, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 85.40591285, 0.00083674, 102.66498473, 0.01004479, 10.26649847, 0.0508727, -85.40591285, -0.00083674, -102.66498473, -0.01004479, -10.26649847, -0.0508727, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 55.43432039, 0.0011022, 66.63664688, 0.00935958, 6.66366469, 0.04088757, -55.43432039, -0.0011022, -66.63664688, -0.00935958, -6.66366469, -0.04088757, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 112.72797731, 0.01673478, 112.72797731, 0.05020434, 78.90958412, -1541.20883056, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 28.18199433, 9.258e-05, 84.54598298, 0.00027773, 281.81994327, 0.00092576, -28.18199433, -9.258e-05, -84.54598298, -0.00027773, -281.81994327, -0.00092576, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 92.90208333, 0.02204404, 92.90208333, 0.06613212, 65.03145833, -1171.7157243, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 23.22552083, 7.629e-05, 69.6765625, 0.00022888, 232.25520833, 0.00076294, -23.22552083, -7.629e-05, -69.6765625, -0.00022888, -232.25520833, -0.00076294, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 2.95, 25.75, 6.825)
    ops.node(123022, 2.95, 25.75, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.21, 28238947.50153174, 11766228.12563823, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 327.25868356, 0.00059916, 394.95922212, 0.01172013, 39.49592221, 0.04211469, -327.25868356, -0.00059916, -394.95922212, -0.01172013, -39.49592221, -0.04211469, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 162.0500941, 0.0007944, 195.57366184, 0.01042397, 19.55736618, 0.03202403, -162.0500941, -0.0007944, -195.57366184, -0.01042397, -19.55736618, -0.03202403, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 276.80499452, 0.01198313, 276.80499452, 0.0359494, 193.76349617, -2671.62001158, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 69.20124863, 9.578e-05, 207.60374589, 0.00028735, 692.01248631, 0.00095782, -69.20124863, -9.578e-05, -207.60374589, -0.00028735, -692.01248631, -0.00095782, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 192.73689317, 0.01588798, 192.73689317, 0.04766394, 134.91582522, -1806.42788818, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 48.18422329, 6.669e-05, 144.55266988, 0.00020008, 481.84223292, 0.00066692, -48.18422329, -6.669e-05, -144.55266988, -0.00020008, -481.84223292, -0.00066692, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 7.7, 25.75, 6.825)
    ops.node(123023, 7.7, 25.75, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.2625, 28849828.05117931, 12020761.68799138, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 517.96398816, 0.00057312, 624.48427644, 0.00892061, 62.44842764, 0.0374634, -517.96398816, -0.00057312, -624.48427644, -0.00892061, -62.44842764, -0.0374634, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 228.32784434, 0.00083206, 275.28390375, 0.00776639, 27.52839038, 0.02614954, -228.32784434, -0.00083206, -275.28390375, -0.00776639, -27.52839038, -0.02614954, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 408.07295359, 0.01146235, 408.07295359, 0.03438705, 285.65106751, -3081.739017, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 102.0182384, 0.00011057, 306.05471519, 0.00033171, 1020.18238398, 0.00110571, -102.0182384, -0.00011057, -306.05471519, -0.00033171, -1020.18238398, -0.00110571, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 188.77351841, 0.01664127, 188.77351841, 0.04992382, 132.14146289, -1919.79294776, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 47.1933796, 5.115e-05, 141.58013881, 0.00015345, 471.93379604, 0.0005115, -47.1933796, -5.115e-05, -141.58013881, -0.00015345, -471.93379604, -0.0005115, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 12.45, 25.75, 6.8)
    ops.node(123024, 12.45, 25.75, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.125, 31096026.82304648, 12956677.84293604, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 167.92094402, 0.00068084, 200.86632276, 0.01180263, 20.08663228, 0.055763, -167.92094402, -0.00068084, -200.86632276, -0.01180263, -20.08663228, -0.055763, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 89.77462479, 0.00110177, 107.38802633, 0.01008285, 10.73880263, 0.03655701, -89.77462479, -0.00110177, -107.38802633, -0.01008285, -10.73880263, -0.03655701, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 209.54071296, 0.01361671, 209.54071296, 0.04085013, 146.67849907, -2880.73752729, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 52.38517824, 0.00011062, 157.15553472, 0.00033186, 523.85178239, 0.00110619, -52.38517824, -0.00011062, -157.15553472, -0.00033186, -523.85178239, -0.00110619, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 152.21536553, 0.02203538, 152.21536553, 0.06610615, 106.55075587, -1648.00749964, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 38.05384138, 8.036e-05, 114.16152415, 0.00024107, 380.53841382, 0.00080356, -38.05384138, -8.036e-05, -114.16152415, -0.00024107, -380.53841382, -0.00080356, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172025, 0.0, 30.9, 6.8)
    ops.node(123025, 0.0, 30.9, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2025, 172025, 123025, 0.0625, 30488544.4621688, 12703560.19257033, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22025, 38.1562546, 0.00109442, 45.88526058, 0.01150204, 4.58852606, 0.06015957, -38.1562546, -0.00109442, -45.88526058, -0.01150204, -4.58852606, -0.06015957, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12025, 38.1562546, 0.00109442, 45.88526058, 0.01150204, 4.58852606, 0.06015957, -38.1562546, -0.00109442, -45.88526058, -0.01150204, -4.58852606, -0.06015957, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22025, 2025, 0.0, 85.35388074, 0.02188835, 85.35388074, 0.06566504, 59.74771652, -1220.31016601, 0.05, 2, 0, 72025, 23025, 2, 3)
    ops.uniaxialMaterial('LimitState', 42025, 21.33847018, 9.191e-05, 64.01541055, 0.00027574, 213.38470184, 0.00091914, -21.33847018, -9.191e-05, -64.01541055, -0.00027574, -213.38470184, -0.00091914, 0.4, 0.3, 0.003, 0.0, 0.0, 22025, 2)
    ops.limitCurve('ThreePoint', 12025, 2025, 0.0, 85.35388074, 0.02188835, 85.35388074, 0.06566504, 59.74771652, -1220.31016601, 0.05, 2, 0, 72025, 23025, 1, 3)
    ops.uniaxialMaterial('LimitState', 32025, 21.33847018, 9.191e-05, 64.01541055, 0.00027574, 213.38470184, 0.00091914, -21.33847018, -9.191e-05, -64.01541055, -0.00027574, -213.38470184, -0.00091914, 0.4, 0.3, 0.003, 0.0, 0.0, 12025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2025, 99999, 'P', 42025, 'Vy', 32025, 'Vz', 22025, 'My', 12025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172025, 72025, 172025, 2025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123025, 123025, 23025, 2025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172026, 2.95, 30.9, 6.825)
    ops.node(123026, 2.95, 30.9, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2026, 172026, 123026, 0.1225, 28815020.79176477, 12006258.66323532, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22026, 111.54428779, 0.00083286, 134.29109838, 0.01064786, 13.42910984, 0.04433158, -111.54428779, -0.00083286, -134.29109838, -0.01064786, -13.42910984, -0.04433158, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12026, 99.62887963, 0.00083286, 119.94582547, 0.01064786, 11.99458255, 0.04433158, -99.62887963, -0.00083286, -119.94582547, -0.01064786, -11.99458255, -0.04433158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22026, 2026, 0.0, 145.71454835, 0.01665726, 145.71454835, 0.04997177, 102.00018384, -1834.20928722, 0.05, 2, 0, 72026, 23026, 2, 3)
    ops.uniaxialMaterial('LimitState', 42026, 36.42863709, 8.471e-05, 109.28591126, 0.00025412, 364.28637087, 0.00084708, -36.42863709, -8.471e-05, -109.28591126, -0.00025412, -364.28637087, -0.00084708, 0.4, 0.3, 0.003, 0.0, 0.0, 22026, 2)
    ops.limitCurve('ThreePoint', 12026, 2026, 0.0, 145.71454835, 0.01665726, 145.71454835, 0.04997177, 102.00018384, -1834.20928722, 0.05, 2, 0, 72026, 23026, 1, 3)
    ops.uniaxialMaterial('LimitState', 32026, 36.42863709, 8.471e-05, 109.28591126, 0.00025412, 364.28637087, 0.00084708, -36.42863709, -8.471e-05, -109.28591126, -0.00025412, -364.28637087, -0.00084708, 0.4, 0.3, 0.003, 0.0, 0.0, 12026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2026, 99999, 'P', 42026, 'Vy', 32026, 'Vz', 22026, 'My', 12026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172026, 72026, 172026, 2026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123026, 123026, 23026, 2026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172027, 7.7, 30.9, 6.825)
    ops.node(123027, 7.7, 30.9, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2027, 172027, 123027, 0.175, 25682464.47562659, 10701026.86484441, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22027, 147.90589857, 0.00083596, 178.56569648, 0.00803349, 17.85656965, 0.02531151, -147.90589857, -0.00083596, -178.56569648, -0.00803349, -17.85656965, -0.02531151, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12027, 217.85963249, 0.0006712, 263.02032162, 0.00853181, 26.30203216, 0.02982693, -217.85963249, -0.0006712, -263.02032162, -0.00853181, -26.30203216, -0.02982693, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22027, 2027, 0.0, 126.10625837, 0.01671913, 126.10625837, 0.05015739, 88.27438086, -1349.57450097, 0.05, 2, 0, 72027, 23027, 2, 3)
    ops.uniaxialMaterial('LimitState', 42027, 31.52656459, 5.758e-05, 94.57969378, 0.00017273, 315.26564592, 0.00057576, -31.52656459, -5.758e-05, -94.57969378, -0.00017273, -315.26564592, -0.00057576, 0.4, 0.3, 0.003, 0.0, 0.0, 22027, 2)
    ops.limitCurve('ThreePoint', 12027, 2027, 0.0, 167.39415766, 0.01342393, 167.39415766, 0.04027178, 117.17591036, -1657.97836142, 0.05, 2, 0, 72027, 23027, 1, 3)
    ops.uniaxialMaterial('LimitState', 32027, 41.84853942, 7.643e-05, 125.54561825, 0.00022928, 418.48539416, 0.00076426, -41.84853942, -7.643e-05, -125.54561825, -0.00022928, -418.48539416, -0.00076426, 0.4, 0.3, 0.003, 0.0, 0.0, 12027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2027, 99999, 'P', 42027, 'Vy', 32027, 'Vz', 22027, 'My', 12027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172027, 72027, 172027, 2027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123027, 123027, 23027, 2027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172028, 12.45, 30.9, 6.8)
    ops.node(123028, 12.45, 30.9, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2028, 172028, 123028, 0.0625, 30854831.70625789, 12856179.87760746, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22028, 46.38880428, 0.00114048, 55.40845039, 0.01226024, 5.54084504, 0.0533834, -46.38880428, -0.00114048, -55.40845039, -0.01226024, -5.54084504, -0.0533834, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12028, 46.38880428, 0.00114048, 55.40845039, 0.01226024, 5.54084504, 0.0533834, -46.38880428, -0.00114048, -55.40845039, -0.01226024, -5.54084504, -0.0533834, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22028, 2028, 0.0, 97.19850809, 0.02280962, 97.19850809, 0.06842887, 68.03895566, -1378.76751905, 0.05, 2, 0, 72028, 23028, 2, 3)
    ops.uniaxialMaterial('LimitState', 42028, 24.29962702, 0.00010343, 72.89888106, 0.00031028, 242.99627022, 0.00103427, -24.29962702, -0.00010343, -72.89888106, -0.00031028, -242.99627022, -0.00103427, 0.4, 0.3, 0.003, 0.0, 0.0, 22028, 2)
    ops.limitCurve('ThreePoint', 12028, 2028, 0.0, 97.19850809, 0.02280962, 97.19850809, 0.06842887, 68.03895566, -1378.76751905, 0.05, 2, 0, 72028, 23028, 1, 3)
    ops.uniaxialMaterial('LimitState', 32028, 24.29962702, 0.00010343, 72.89888106, 0.00031028, 242.99627022, 0.00103427, -24.29962702, -0.00010343, -72.89888106, -0.00031028, -242.99627022, -0.00103427, 0.4, 0.3, 0.003, 0.0, 0.0, 12028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2028, 99999, 'P', 42028, 'Vy', 32028, 'Vz', 22028, 'My', 12028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172028, 72028, 172028, 2028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123028, 123028, 23028, 2028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.7, 0.0, 9.675)
    ops.node(124003, 7.7, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.175, 28288923.7208566, 11787051.55035692, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 102.05135927, 0.00084408, 124.09231719, 0.01239163, 12.40923172, 0.0426063, -102.05135927, -0.00084408, -124.09231719, -0.01239163, -12.40923172, -0.0426063, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 165.75489359, 0.00067079, 201.55448178, 0.0134148, 20.15544818, 0.05159006, -165.75489359, -0.00067079, -201.55448178, -0.0134148, -20.15544818, -0.05159006, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 152.3486132, 0.01688152, 152.3486132, 0.05064457, 106.64402924, -1662.58828393, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 38.0871533, 6.315e-05, 114.2614599, 0.00018944, 380.871533, 0.00063148, -38.0871533, -6.315e-05, -114.2614599, -0.00018944, -380.871533, -0.00063148, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 186.36425823, 0.01341581, 186.36425823, 0.04024744, 130.45498076, -2561.83529011, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 46.59106456, 7.725e-05, 139.77319367, 0.00023174, 465.91064558, 0.00077248, -46.59106456, -7.725e-05, -139.77319367, -0.00023174, -465.91064558, -0.00077248, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.45, 0.0, 9.65)
    ops.node(124004, 12.45, 0.0, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 29721660.9941299, 12384025.41422079, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 36.59405354, 0.00102361, 44.27433587, 0.01176256, 4.42743359, 0.06623462, -36.59405354, -0.00102361, -44.27433587, -0.01176256, -4.42743359, -0.06623462, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 40.16298143, 0.00102361, 48.59230277, 0.01176256, 4.85923028, 0.06623462, -40.16298143, -0.00102361, -48.59230277, -0.01176256, -4.85923028, -0.06623462, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 67.45764024, 0.02047223, 67.45764024, 0.0614167, 47.22034817, -1165.36313159, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 16.86441006, 7.452e-05, 50.59323018, 0.00022355, 168.64410059, 0.00074517, -16.86441006, -7.452e-05, -50.59323018, -0.00022355, -168.64410059, -0.00074517, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 67.45764024, 0.02047223, 67.45764024, 0.0614167, 47.22034817, -1165.36313159, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 16.86441006, 7.452e-05, 50.59323018, 0.00022355, 168.64410059, 0.00074517, -16.86441006, -7.452e-05, -50.59323018, -0.00022355, -168.64410059, -0.00074517, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 5.15, 9.65)
    ops.node(124005, 0.0, 5.15, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 26109851.63553866, 10879104.84814111, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 28.89896004, 0.00115063, 35.14106551, 0.01435041, 3.51410655, 0.0627421, -28.89896004, -0.00115063, -35.14106551, -0.01435041, -3.51410655, -0.0627421, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 28.89896004, 0.00115063, 35.14106551, 0.01435041, 3.51410655, 0.0627421, -28.89896004, -0.00115063, -35.14106551, -0.01435041, -3.51410655, -0.0627421, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 77.50356471, 0.02301266, 77.50356471, 0.06903797, 54.2524953, -1589.83223818, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 19.37589118, 9.746e-05, 58.12767353, 0.00029237, 193.75891177, 0.00097457, -19.37589118, -9.746e-05, -58.12767353, -0.00029237, -193.75891177, -0.00097457, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 77.50356471, 0.02301266, 77.50356471, 0.06903797, 54.2524953, -1589.83223818, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 19.37589118, 9.746e-05, 58.12767353, 0.00029237, 193.75891177, 0.00097457, -19.37589118, -9.746e-05, -58.12767353, -0.00029237, -193.75891177, -0.00097457, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 2.95, 5.15, 9.675)
    ops.node(124006, 2.95, 5.15, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.21, 30098005.68731456, 12540835.70304773, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 266.23188918, 0.00059486, 322.36985016, 0.01230313, 32.23698502, 0.05138438, -266.23188918, -0.00059486, -322.36985016, -0.01230313, -32.23698502, -0.05138438, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 127.41865581, 0.00079301, 154.28629947, 0.01093112, 15.42862995, 0.03870442, -127.41865581, -0.00079301, -154.28629947, -0.01093112, -15.42862995, -0.03870442, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 262.6337038, 0.01189721, 262.6337038, 0.03569163, 183.84359266, -2789.04852045, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 65.65842595, 8.527e-05, 196.97527785, 0.0002558, 656.58425951, 0.00085265, -65.65842595, -8.527e-05, -196.97527785, -0.0002558, -656.58425951, -0.00085265, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 182.13705433, 0.01586024, 182.13705433, 0.04758071, 127.49593803, -1535.7212262, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 45.53426358, 5.913e-05, 136.60279074, 0.00017739, 455.34263581, 0.00059131, -45.53426358, -5.913e-05, -136.60279074, -0.00017739, -455.34263581, -0.00059131, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 7.7, 5.15, 9.675)
    ops.node(124007, 7.7, 5.15, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.2625, 28852692.34581239, 12021955.1440885, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 401.63618806, 0.00055314, 487.5027346, 0.01025748, 48.75027346, 0.04514794, -401.63618806, -0.00055314, -487.5027346, -0.01025748, -48.75027346, -0.04514794, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 173.36592607, 0.00080163, 210.43014937, 0.0088631, 21.04301494, 0.0313345, -173.36592607, -0.00080163, -210.43014937, -0.0088631, -21.04301494, -0.0313345, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 369.22511179, 0.01106284, 369.22511179, 0.03318853, 258.45757825, -3345.72914326, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 92.30627795, 0.00010004, 276.91883384, 0.00030011, 923.06277947, 0.00100035, -92.30627795, -0.00010004, -276.91883384, -0.00030011, -923.06277947, -0.00100035, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 160.8600031, 0.01603252, 160.8600031, 0.04809757, 112.60200217, -1548.02465192, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 40.21500078, 4.358e-05, 120.64500233, 0.00013075, 402.15000776, 0.00043582, -40.21500078, -4.358e-05, -120.64500233, -0.00013075, -402.15000776, -0.00043582, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 12.45, 5.15, 9.65)
    ops.node(124008, 12.45, 5.15, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.125, 29338774.27776011, 12224489.28240005, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 131.63726085, 0.00063677, 159.40906205, 0.01122596, 15.94090621, 0.06540111, -131.63726085, -0.00063677, -159.40906205, -0.01122596, -15.94090621, -0.06540111, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 54.43591933, 0.0010209, 65.92038445, 0.00957189, 6.59203844, 0.04219767, -54.43591933, -0.0010209, -65.92038445, -0.00957189, -6.59203844, -0.04219767, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 159.04343663, 0.01273546, 159.04343663, 0.03820638, 111.33040564, -2395.04506283, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 39.76085916, 8.899e-05, 119.28257747, 0.00026697, 397.60859156, 0.0008899, -39.76085916, -8.899e-05, -119.28257747, -0.00026697, -397.60859156, -0.0008899, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 109.69935456, 0.02041799, 109.69935456, 0.06125398, 76.78954819, -1110.77895446, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 27.42483864, 6.138e-05, 82.27451592, 0.00018414, 274.24838641, 0.0006138, -27.42483864, -6.138e-05, -82.27451592, -0.00018414, -274.24838641, -0.0006138, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 10.3, 9.65)
    ops.node(124009, 0.0, 10.3, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0875, 28975582.9105846, 12073159.54607692, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 62.31590558, 0.00081163, 75.62899107, 0.01159301, 7.56289911, 0.06773804, -62.31590558, -0.00081163, -75.62899107, -0.01159301, -7.56289911, -0.06773804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 39.26675989, 0.00107087, 47.65565719, 0.01073913, 4.76556572, 0.05409526, -39.26675989, -0.00107087, -47.65565719, -0.01073913, -4.76556572, -0.05409526, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 101.12804639, 0.01623267, 101.12804639, 0.04869802, 70.78963248, -1804.65499062, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 25.2820116, 8.185e-05, 75.8460348, 0.00024554, 252.82011599, 0.00081848, -25.2820116, -8.185e-05, -75.8460348, -0.00024554, -252.82011599, -0.00081848, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 83.01926087, 0.0214174, 83.01926087, 0.0642522, 58.11348261, -1164.57155026, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 20.75481522, 6.719e-05, 62.26444565, 0.00020158, 207.54815217, 0.00067192, -20.75481522, -6.719e-05, -62.26444565, -0.00020158, -207.54815217, -0.00067192, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 2.95, 10.3, 9.675)
    ops.node(124010, 2.95, 10.3, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.21, 28684934.03595847, 11952055.84831603, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 257.4487762, 0.00059649, 312.6660286, 0.01185419, 31.26660286, 0.04980189, -257.4487762, -0.00059649, -312.6660286, -0.01185419, -31.26660286, -0.04980189, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 123.54060674, 0.00080708, 150.03742279, 0.01055504, 15.00374228, 0.03752277, -123.54060674, -0.00080708, -150.03742279, -0.01055504, -15.00374228, -0.03752277, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 245.79220203, 0.01192987, 245.79220203, 0.03578961, 172.05454142, -2545.25517583, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 61.44805051, 8.373e-05, 184.34415152, 0.00025118, 614.48050508, 0.00083728, -61.44805051, -8.373e-05, -184.34415152, -0.00025118, -614.48050508, -0.00083728, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 170.52174715, 0.01614162, 170.52174715, 0.04842485, 119.36522301, -1436.0018582, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 42.63043679, 5.809e-05, 127.89131037, 0.00017426, 426.30436789, 0.00058088, -42.63043679, -5.809e-05, -127.89131037, -0.00017426, -426.30436789, -0.00058088, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.7, 10.3, 9.675)
    ops.node(124011, 7.7, 10.3, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.2625, 29578212.84340128, 12324255.3514172, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 410.0231416, 0.00056384, 496.92460482, 0.00961574, 49.69246048, 0.04501455, -410.0231416, -0.00056384, -496.92460482, -0.00961574, -49.69246048, -0.04501455, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 176.17329229, 0.00082905, 213.51195766, 0.00834853, 21.35119577, 0.03114735, -176.17329229, -0.00082905, -213.51195766, -0.00834853, -21.35119577, -0.03114735, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 372.0481559, 0.01127686, 372.0481559, 0.03383058, 260.43370913, -3079.47563699, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 93.01203898, 9.833e-05, 279.03611693, 0.00029498, 930.12038975, 0.00098328, -93.01203898, -9.833e-05, -279.03611693, -0.00029498, -930.12038975, -0.00098328, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 166.48976187, 0.01658104, 166.48976187, 0.04974313, 116.54283331, -1462.95735249, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 41.62244047, 4.4e-05, 124.8673214, 0.000132, 416.22440467, 0.00044001, -41.62244047, -4.4e-05, -124.8673214, -0.000132, -416.22440467, -0.00044001, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 12.45, 10.3, 9.65)
    ops.node(124012, 12.45, 10.3, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.125, 32946150.86175956, 13727562.85906648, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 133.16065679, 0.00064289, 159.75445868, 0.01093138, 15.97544587, 0.06891, -133.16065679, -0.00064289, -159.75445868, -0.01093138, -15.97544587, -0.06891, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 55.38647289, 0.00104363, 66.44782481, 0.0093518, 6.64478248, 0.04426814, -55.38647289, -0.00104363, -66.44782481, -0.0093518, -6.64478248, -0.04426814, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 175.46922768, 0.01285775, 175.46922768, 0.03857326, 122.82845938, -2429.08211462, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 43.86730692, 8.743e-05, 131.60192076, 0.00026229, 438.6730692, 0.00087431, -43.86730692, -8.743e-05, -131.60192076, -0.00026229, -438.6730692, -0.00087431, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 126.0774794, 0.02087261, 126.0774794, 0.06261782, 88.25423558, -1122.35796594, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 31.51936985, 6.282e-05, 94.55810955, 0.00018846, 315.1936985, 0.0006282, -31.51936985, -6.282e-05, -94.55810955, -0.00018846, -315.1936985, -0.0006282, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 15.45, 9.65)
    ops.node(124013, 0.0, 15.45, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 27293166.79645327, 11372152.83185553, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 31.1129414, 0.00105315, 37.76897505, 0.01425153, 3.77689751, 0.06404353, -31.1129414, -0.00105315, -37.76897505, -0.01425153, -3.77689751, -0.06404353, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 31.1129414, 0.00105315, 37.76897505, 0.01425153, 3.77689751, 0.06404353, -31.1129414, -0.00105315, -37.76897505, -0.01425153, -3.77689751, -0.06404353, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 80.53211539, 0.02106293, 80.53211539, 0.0631888, 56.37248077, -1583.25707017, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 20.13302885, 9.688e-05, 60.39908654, 0.00029063, 201.33028847, 0.00096875, -20.13302885, -9.688e-05, -60.39908654, -0.00029063, -201.33028847, -0.00096875, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 80.53211539, 0.02106293, 80.53211539, 0.0631888, 56.37248077, -1583.25707017, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 20.13302885, 9.688e-05, 60.39908654, 0.00029063, 201.33028847, 0.00096875, -20.13302885, -9.688e-05, -60.39908654, -0.00029063, -201.33028847, -0.00096875, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 2.95, 15.45, 9.675)
    ops.node(124014, 2.95, 15.45, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.21, 28507066.29469013, 11877944.28945422, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 262.36494032, 0.00058516, 318.74596235, 0.01226016, 31.87459623, 0.05006617, -262.36494032, -0.00058516, -318.74596235, -0.01226016, -31.87459623, -0.05006617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 125.4794198, 0.00077397, 152.44437146, 0.01088327, 15.24443715, 0.03775031, -125.4794198, -0.00077397, -152.44437146, -0.01088327, -15.24443715, -0.03775031, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 243.50282732, 0.01170313, 243.50282732, 0.03510939, 170.45197912, -2511.96867159, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 60.87570683, 8.347e-05, 182.62712049, 0.0002504, 608.7570683, 0.00083466, -60.87570683, -8.347e-05, -182.62712049, -0.0002504, -608.7570683, -0.00083466, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 168.95332897, 0.01547935, 168.95332897, 0.04643805, 118.26733028, -1421.4064589, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 42.23833224, 5.791e-05, 126.71499672, 0.00017374, 422.38332241, 0.00057912, -42.23833224, -5.791e-05, -126.71499672, -0.00017374, -422.38332241, -0.00057912, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.7, 15.45, 9.675)
    ops.node(124015, 7.7, 15.45, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.2625, 26457465.97396301, 11023944.15581792, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 401.87769787, 0.0005628, 489.65152402, 0.00936267, 48.9651524, 0.04218908, -401.87769787, -0.0005628, -489.65152402, -0.00936267, -48.9651524, -0.04218908, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 172.27325129, 0.00082873, 209.89933129, 0.00813885, 20.98993313, 0.02928089, -172.27325129, -0.00082873, -209.89933129, -0.00813885, -20.98993313, -0.02928089, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 325.96518799, 0.01125609, 325.96518799, 0.03376828, 228.17563159, -2836.88182588, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 81.491297, 9.631e-05, 244.47389099, 0.00028893, 814.91296998, 0.0009631, -81.491297, -9.631e-05, -244.47389099, -0.00028893, -814.91296998, -0.0009631, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 142.88195278, 0.01657457, 142.88195278, 0.04972372, 100.01736695, -1384.41008876, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 35.72048819, 4.222e-05, 107.16146458, 0.00012665, 357.20488195, 0.00042216, -35.72048819, -4.222e-05, -107.16146458, -0.00012665, -357.20488195, -0.00042216, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.45, 15.45, 9.65)
    ops.node(124016, 12.45, 15.45, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.125, 30497822.19991756, 12707425.91663232, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 131.50988327, 0.00067484, 158.85177345, 0.01056585, 15.88517735, 0.06614813, -131.50988327, -0.00067484, -158.85177345, -0.01056585, -15.88517735, -0.06614813, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 55.19803148, 0.00115876, 66.67411584, 0.00914596, 6.66741158, 0.04261915, -55.19803148, -0.00115876, -66.67411584, -0.00914596, -6.66741158, -0.04261915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 159.45476808, 0.0134968, 159.45476808, 0.04049041, 111.61833766, -2195.96938479, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 39.86369202, 8.583e-05, 119.59107606, 0.00025749, 398.6369202, 0.00085829, -39.86369202, -8.583e-05, -119.59107606, -0.00025749, -398.6369202, -0.00085829, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 109.4984147, 0.02317512, 109.4984147, 0.06952537, 76.64889029, -1042.60131648, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 27.37460368, 5.894e-05, 82.12381103, 0.00017682, 273.74603676, 0.00058939, -27.37460368, -5.894e-05, -82.12381103, -0.00017682, -273.74603676, -0.00058939, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 20.6, 9.65)
    ops.node(124017, 0.0, 20.6, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 30074904.86349335, 12531210.3597889, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 30.45789607, 0.00101766, 36.80240128, 0.01139876, 3.68024013, 0.06543585, -30.45789607, -0.00101766, -36.80240128, -0.01139876, -3.68024013, -0.06543585, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 30.45789607, 0.00101766, 36.80240128, 0.01139876, 3.68024013, 0.06543585, -30.45789607, -0.00101766, -36.80240128, -0.01139876, -3.68024013, -0.06543585, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 68.06003619, 0.02035325, 68.06003619, 0.06105974, 47.64202533, -1129.11277018, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 17.01500905, 7.43e-05, 51.04502714, 0.0002229, 170.15009047, 0.00074299, -17.01500905, -7.43e-05, -51.04502714, -0.0002229, -170.15009047, -0.00074299, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 68.06003619, 0.02035325, 68.06003619, 0.06105974, 47.64202533, -1129.11277018, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 17.01500905, 7.43e-05, 51.04502714, 0.0002229, 170.15009047, 0.00074299, -17.01500905, -7.43e-05, -51.04502714, -0.0002229, -170.15009047, -0.00074299, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 2.95, 20.6, 9.675)
    ops.node(124018, 2.95, 20.6, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.21, 27992140.07958784, 11663391.69982827, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 255.84659621, 0.000586, 311.11780372, 0.0113229, 31.11178037, 0.04869959, -255.84659621, -0.000586, -311.11780372, -0.0113229, -31.11178037, -0.04869959, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 122.52339123, 0.00078297, 148.99243902, 0.01007997, 14.8992439, 0.03664192, -122.52339123, -0.00078297, -148.99243902, -0.01007997, -14.8992439, -0.03664192, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 234.6199774, 0.01172007, 234.6199774, 0.03516021, 164.23398418, -2327.26630431, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 58.65499435, 8.19e-05, 175.96498305, 0.0002457, 586.54994351, 0.00081901, -58.65499435, -8.19e-05, -175.96498305, -0.0002457, -586.54994351, -0.00081901, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 163.10226514, 0.01565943, 163.10226514, 0.0469783, 114.1715856, -1340.01123953, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 40.77556628, 5.694e-05, 122.32669885, 0.00017081, 407.75566285, 0.00056935, -40.77556628, -5.694e-05, -122.32669885, -0.00017081, -407.75566285, -0.00056935, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 7.7, 20.6, 9.675)
    ops.node(124019, 7.7, 20.6, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.2625, 28983819.67279368, 12076591.5303307, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 410.90995742, 0.00055387, 498.6279928, 0.00889841, 49.86279928, 0.04388429, -410.90995742, -0.00055387, -498.6279928, -0.00889841, -49.86279928, -0.04388429, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 178.96743311, 0.0007924, 217.17208439, 0.00772428, 21.71720844, 0.03025714, -178.96743311, -0.0007924, -217.17208439, -0.00772428, -21.71720844, -0.03025714, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 355.56421665, 0.01107738, 355.56421665, 0.03323213, 248.89495165, -2748.03359834, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 88.89105416, 9.59e-05, 266.67316249, 0.00028769, 888.91054162, 0.00095898, -88.89105416, -9.59e-05, -266.67316249, -0.00028769, -888.91054162, -0.00095898, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 161.87118958, 0.01584809, 161.87118958, 0.04754426, 113.30983271, -1355.36901537, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 40.46779739, 4.366e-05, 121.40339218, 0.00013097, 404.67797395, 0.00043658, -40.46779739, -4.366e-05, -121.40339218, -0.00013097, -404.67797395, -0.00043658, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 12.45, 20.6, 9.65)
    ops.node(124020, 12.45, 20.6, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.125, 30008327.53956894, 12503469.80815372, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 131.73889828, 0.00063262, 159.3075461, 0.01239457, 15.93075461, 0.06740689, -131.73889828, -0.00063262, -159.3075461, -0.01239457, -15.93075461, -0.06740689, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 54.51305652, 0.00100887, 65.92085844, 0.0105069, 6.59208584, 0.04363684, -54.51305652, -0.00100887, -65.92085844, -0.0105069, -6.59208584, -0.04363684, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 166.8976082, 0.01265232, 166.8976082, 0.03795695, 116.82832574, -2627.36032479, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 41.72440205, 9.13e-05, 125.17320615, 0.0002739, 417.2440205, 0.00091301, -41.72440205, -9.13e-05, -125.17320615, -0.0002739, -417.2440205, -0.00091301, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 120.23449061, 0.02017743, 120.23449061, 0.0605323, 84.16414343, -1189.39754303, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 30.05862265, 6.577e-05, 90.17586796, 0.00019732, 300.58622654, 0.00065774, -30.05862265, -6.577e-05, -90.17586796, -0.00019732, -300.58622654, -0.00065774, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 0.0, 25.75, 9.65)
    ops.node(124021, 0.0, 25.75, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0875, 30094446.48642823, 12539352.70267843, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 62.49139424, 0.00078608, 75.65417682, 0.0125215, 7.56541768, 0.06985069, -62.49139424, -0.00078608, -75.65417682, -0.0125215, -7.56541768, -0.06985069, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 39.32930248, 0.00102488, 47.61337205, 0.01154869, 4.76133721, 0.05581924, -39.32930248, -0.00102488, -47.61337205, -0.01154869, -4.76133721, -0.05581924, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 108.80742185, 0.0157216, 108.80742185, 0.0471648, 76.1651953, -2063.37950269, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 27.20185546, 8.479e-05, 81.60556639, 0.00025437, 272.01855464, 0.00084789, -27.20185546, -8.479e-05, -81.60556639, -0.00025437, -272.01855464, -0.00084789, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 93.90916269, 0.02049759, 93.90916269, 0.06149276, 65.73641388, -1312.475924, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 23.47729067, 7.318e-05, 70.43187202, 0.00021954, 234.77290672, 0.0007318, -23.47729067, -7.318e-05, -70.43187202, -0.00021954, -234.77290672, -0.0007318, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 2.95, 25.75, 9.675)
    ops.node(124022, 2.95, 25.75, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.21, 27721636.42604771, 11550681.84418655, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 265.6765766, 0.00059365, 323.21895285, 0.01190193, 32.32189528, 0.04904117, -265.6765766, -0.00059365, -323.21895285, -0.01190193, -32.32189528, -0.04904117, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 126.84393946, 0.00078877, 154.31682316, 0.01058053, 15.43168232, 0.03697373, -126.84393946, -0.00078877, -154.31682316, -0.01058053, -15.43168232, -0.03697373, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 239.83241946, 0.011873, 239.83241946, 0.035619, 167.88269363, -2623.58453859, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 59.95810487, 8.454e-05, 179.8743146, 0.00025361, 599.58104866, 0.00084537, -59.95810487, -8.454e-05, -179.8743146, -0.00025361, -599.58104866, -0.00084537, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 165.7941782, 0.01577546, 165.7941782, 0.04732638, 116.05592474, -1470.26423326, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 41.44854455, 5.844e-05, 124.34563365, 0.00017532, 414.48544549, 0.0005844, -41.44854455, -5.844e-05, -124.34563365, -0.00017532, -414.48544549, -0.0005844, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 7.7, 25.75, 9.675)
    ops.node(124023, 7.7, 25.75, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.2625, 31511334.20911921, 13129722.58713301, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 402.11891098, 0.00056661, 484.97572493, 0.0093861, 48.49757249, 0.04593182, -402.11891098, -0.00056661, -484.97572493, -0.0093861, -48.49757249, -0.04593182, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 170.85578911, 0.00085585, 206.06071467, 0.00818227, 20.60607147, 0.03171976, -170.85578911, -0.00085585, -206.06071467, -0.00818227, -20.60607147, -0.03171976, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 392.81986323, 0.01133222, 392.81986323, 0.03399666, 274.97390426, -2879.62313359, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 98.20496581, 9.745e-05, 294.61489742, 0.00029235, 982.04965808, 0.00097448, -98.20496581, -9.745e-05, -294.61489742, -0.00029235, -982.04965808, -0.00097448, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 181.90420208, 0.01711708, 181.90420208, 0.05135124, 127.33294146, -1398.3264925, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 45.47605052, 4.513e-05, 136.42815156, 0.00013538, 454.7605052, 0.00045126, -45.47605052, -4.513e-05, -136.42815156, -0.00013538, -454.7605052, -0.00045126, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 12.45, 25.75, 9.65)
    ops.node(124024, 12.45, 25.75, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.125, 30731220.86119926, 12804675.35883303, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 129.1689282, 0.0006493, 155.93606899, 0.01333204, 15.5936069, 0.06917433, -129.1689282, -0.0006493, -155.93606899, -0.01333204, -15.5936069, -0.06917433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 53.95522216, 0.00108309, 65.13613887, 0.01132467, 6.51361389, 0.04495445, -53.95522216, -0.00108309, -65.13613887, -0.01132467, -6.51361389, -0.04495445, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 177.66627038, 0.01298598, 177.66627038, 0.03895795, 124.36638927, -3002.72088418, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 44.4165676, 9.491e-05, 133.24970279, 0.00028472, 444.16567595, 0.00094906, -44.4165676, -9.491e-05, -133.24970279, -0.00028472, -444.16567595, -0.00094906, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 126.82753094, 0.02166173, 126.82753094, 0.0649852, 88.77927166, -1314.59150936, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 31.70688273, 6.775e-05, 95.1206482, 0.00020325, 317.06882734, 0.00067749, -31.70688273, -6.775e-05, -95.1206482, -0.00020325, -317.06882734, -0.00067749, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173025, 0.0, 30.9, 9.65)
    ops.node(124025, 0.0, 30.9, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3025, 173025, 124025, 0.0625, 27464014.03053401, 11443339.17938917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23025, 26.80003731, 0.00101446, 32.67607684, 0.01275493, 3.26760768, 0.07017626, -26.80003731, -0.00101446, -32.67607684, -0.01275493, -3.26760768, -0.07017626, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13025, 26.80003731, 0.00101446, 32.67607684, 0.01275493, 3.26760768, 0.07017626, -26.80003731, -0.00101446, -32.67607684, -0.01275493, -3.26760768, -0.07017626, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23025, 3025, 0.0, 69.81454574, 0.02028925, 69.81454574, 0.06086775, 48.87018202, -1697.73132228, 0.05, 2, 0, 73025, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 43025, 17.45363643, 8.346e-05, 52.3609093, 0.00025038, 174.53636434, 0.0008346, -17.45363643, -8.346e-05, -52.3609093, -0.00025038, -174.53636434, -0.0008346, 0.4, 0.3, 0.003, 0.0, 0.0, 23025, 2)
    ops.limitCurve('ThreePoint', 13025, 3025, 0.0, 69.81454574, 0.02028925, 69.81454574, 0.06086775, 48.87018202, -1697.73132228, 0.05, 2, 0, 73025, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 33025, 17.45363643, 8.346e-05, 52.3609093, 0.00025038, 174.53636434, 0.0008346, -17.45363643, -8.346e-05, -52.3609093, -0.00025038, -174.53636434, -0.0008346, 0.4, 0.3, 0.003, 0.0, 0.0, 13025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3025, 99999, 'P', 43025, 'Vy', 33025, 'Vz', 23025, 'My', 13025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173025, 73025, 173025, 3025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 3025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173026, 2.95, 30.9, 9.675)
    ops.node(124026, 2.95, 30.9, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3026, 173026, 124026, 0.1225, 31394325.75117134, 13080969.06298806, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23026, 74.34065466, 0.00078059, 89.70066635, 0.01019435, 8.97006664, 0.05544281, -74.34065466, -0.00078059, -89.70066635, -0.01019435, -8.97006664, -0.05544281, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13026, 86.34523202, 0.00078059, 104.18558842, 0.01019435, 10.41855884, 0.05544281, -86.34523202, -0.00078059, -104.18558842, -0.01019435, -10.41855884, -0.05544281, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23026, 3026, 0.0, 132.95114941, 0.01561171, 132.95114941, 0.04683512, 93.06580459, -1700.13395609, 0.05, 2, 0, 73026, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 43026, 33.23778735, 7.094e-05, 99.71336206, 0.00021282, 332.37787353, 0.00070939, -33.23778735, -7.094e-05, -99.71336206, -0.00021282, -332.37787353, -0.00070939, 0.4, 0.3, 0.003, 0.0, 0.0, 23026, 2)
    ops.limitCurve('ThreePoint', 13026, 3026, 0.0, 132.95114941, 0.01561171, 132.95114941, 0.04683512, 93.06580459, -1700.13395609, 0.05, 2, 0, 73026, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 33026, 33.23778735, 7.094e-05, 99.71336206, 0.00021282, 332.37787353, 0.00070939, -33.23778735, -7.094e-05, -99.71336206, -0.00021282, -332.37787353, -0.00070939, 0.4, 0.3, 0.003, 0.0, 0.0, 13026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3026, 99999, 'P', 43026, 'Vy', 33026, 'Vz', 23026, 'My', 13026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173026, 73026, 173026, 3026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 3026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173027, 7.7, 30.9, 9.675)
    ops.node(124027, 7.7, 30.9, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3027, 173027, 124027, 0.175, 30556854.34638626, 12732022.64432761, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23027, 115.73524266, 0.00079959, 140.01867751, 0.0084002, 14.00186775, 0.03501052, -115.73524266, -0.00079959, -140.01867751, -0.0084002, -14.00186775, -0.03501052, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13027, 171.72026078, 0.00064585, 207.75040742, 0.00894667, 20.77504074, 0.04174384, -171.72026078, -0.00064585, -207.75040742, -0.00894667, -20.77504074, -0.04174384, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23027, 3027, 0.0, 123.71245908, 0.01599173, 123.71245908, 0.0479752, 86.59872136, -1003.38169578, 0.05, 2, 0, 73027, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 43027, 30.92811477, 4.747e-05, 92.78434431, 0.00014242, 309.28114771, 0.00047473, -30.92811477, -4.747e-05, -92.78434431, -0.00014242, -309.28114771, -0.00047473, 0.4, 0.3, 0.003, 0.0, 0.0, 23027, 2)
    ops.limitCurve('ThreePoint', 13027, 3027, 0.0, 171.20523377, 0.0129171, 171.20523377, 0.03875129, 119.84366364, -1415.00163293, 0.05, 2, 0, 73027, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 33027, 42.80130844, 6.57e-05, 128.40392533, 0.00019709, 428.01308442, 0.00065697, -42.80130844, -6.57e-05, -128.40392533, -0.00019709, -428.01308442, -0.00065697, 0.4, 0.3, 0.003, 0.0, 0.0, 13027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3027, 99999, 'P', 43027, 'Vy', 33027, 'Vz', 23027, 'My', 13027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173027, 73027, 173027, 3027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 3027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173028, 12.45, 30.9, 9.65)
    ops.node(124028, 12.45, 30.9, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3028, 173028, 124028, 0.0625, 30862593.77642816, 12859414.07351173, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23028, 37.79853988, 0.00103974, 45.61181196, 0.01206314, 4.5611812, 0.06787667, -37.79853988, -0.00103974, -45.61181196, -0.01206314, -4.5611812, -0.06787667, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13028, 41.54087696, 0.00103974, 50.12772118, 0.01206314, 5.01277212, 0.06787667, -41.54087696, -0.00103974, -50.12772118, -0.01206314, -5.01277212, -0.06787667, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23028, 3028, 0.0, 77.67994056, 0.02079482, 77.67994056, 0.06238445, 54.37595839, -1316.09059531, 0.05, 2, 0, 73028, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 43028, 19.41998514, 8.264e-05, 58.25995542, 0.00024791, 194.1998514, 0.00082637, -19.41998514, -8.264e-05, -58.25995542, -0.00024791, -194.1998514, -0.00082637, 0.4, 0.3, 0.003, 0.0, 0.0, 23028, 2)
    ops.limitCurve('ThreePoint', 13028, 3028, 0.0, 77.67994056, 0.02079482, 77.67994056, 0.06238445, 54.37595839, -1316.09059531, 0.05, 2, 0, 73028, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 33028, 19.41998514, 8.264e-05, 58.25995542, 0.00024791, 194.1998514, 0.00082637, -19.41998514, -8.264e-05, -58.25995542, -0.00024791, -194.1998514, -0.00082637, 0.4, 0.3, 0.003, 0.0, 0.0, 13028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3028, 99999, 'P', 43028, 'Vy', 33028, 'Vz', 23028, 'My', 13028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173028, 73028, 173028, 3028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 3028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124029, 0.0, 0.0, 1.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 170001, 124029, 0.075, 29544038.93459187, 12310016.22274661, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 96.05303909, 0.00080494, 114.76451488, 0.01070377, 11.47645149, 0.04271414, -96.05303909, -0.00080494, -114.76451488, -0.01070377, -11.47645149, -0.04271414, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 74.20419863, 0.00092319, 88.6594421, 0.0102689, 8.86594421, 0.03819789, -74.20419863, -0.00092319, -88.6594421, -0.0102689, -8.86594421, -0.03819789, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 103.49212252, 0.01609882, 103.49212252, 0.04829646, 72.44448577, -2007.37238764, 0.05, 2, 0, 70001, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 25.87303063, 6.221e-05, 77.61909189, 0.00018664, 258.73030631, 0.00062213, -25.87303063, -6.221e-05, -77.61909189, -0.00018664, -258.73030631, -0.00062213, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 79.76883722, 0.01846388, 79.76883722, 0.05539165, 55.83818605, -1776.83484337, 0.05, 2, 0, 70001, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 19.9422093, 4.795e-05, 59.82662791, 0.00014386, 199.42209305, 0.00047952, -19.9422093, -4.795e-05, -59.82662791, -0.00014386, -199.42209305, -0.00047952, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 0.0, 0.0, 2.1)
    ops.node(121001, 0.0, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 174029, 121001, 0.075, 28027554.32497219, 11678147.63540508, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 88.27411728, 0.0007491, 105.85328784, 0.01865429, 10.58532878, 0.06239664, -88.27411728, -0.0007491, -105.85328784, -0.01865429, -10.58532878, -0.06239664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 67.85858125, 0.00085035, 81.37214119, 0.01766054, 8.13721412, 0.05532159, -67.85858125, -0.00085035, -81.37214119, -0.01766054, -8.13721412, -0.05532159, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 124.61450333, 0.01498202, 124.61450333, 0.04494607, 87.23015233, -3262.78943508, 0.05, 2, 0, 74029, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 31.15362583, 7.896e-05, 93.46087749, 0.00023689, 311.53625832, 0.00078963, -31.15362583, -7.896e-05, -93.46087749, -0.00023689, -311.53625832, -0.00078963, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 111.66749679, 0.0170069, 111.66749679, 0.05102071, 78.16724776, -2710.19620968, 0.05, 2, 0, 74029, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 27.9168742, 7.076e-05, 83.7506226, 0.00021228, 279.16874199, 0.00070759, -27.9168742, -7.076e-05, -83.7506226, -0.00021228, -279.16874199, -0.00070759, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 2.95, 0.0, 0.0)
    ops.node(124030, 2.95, 0.0, 1.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 170002, 124030, 0.18, 31913744.87390431, 13297393.69746013, 0.00450368, 0.00334125, 0.00264, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 343.10847663, 0.00064965, 408.84671092, 0.01779402, 40.88467109, 0.04992548, -343.10847663, -0.00064965, -408.84671092, -0.01779402, -40.88467109, -0.04992548, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 323.91274994, 0.00062059, 385.97315852, 0.01840813, 38.59731585, 0.05347281, -323.91274994, -0.00062059, -385.97315852, -0.01840813, -38.59731585, -0.05347281, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 316.67623077, 0.01299298, 316.67623077, 0.03897894, 221.67336154, -4634.92939364, 0.05, 2, 0, 70002, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 79.16905769, 7.343e-05, 237.50717308, 0.00022029, 791.69057692, 0.00073429, -79.16905769, -7.343e-05, -237.50717308, -0.00022029, -791.69057692, -0.00073429, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 356.26075961, 0.01241186, 356.26075961, 0.03723558, 249.38253173, -5044.75223257, 0.05, 2, 0, 70002, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 89.0651899, 8.261e-05, 267.19556971, 0.00024782, 890.65189903, 0.00082608, -89.0651899, -8.261e-05, -267.19556971, -0.00024782, -890.65189903, -0.00082608, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 2.95, 0.0, 2.1)
    ops.node(121002, 2.95, 0.0, 3.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4077, 174030, 121002, 0.18, 29764747.63168217, 12401978.17986757, 0.00450368, 0.00334125, 0.00264, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24077, 217.35254398, 0.00066496, 260.0435298, 0.01365643, 26.00435298, 0.03896603, -217.35254398, -0.00066496, -260.0435298, -0.01365643, -26.00435298, -0.03896603, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14077, 246.60400289, 0.000633, 295.04037175, 0.01408018, 29.50403717, 0.04154664, -246.60400289, -0.000633, -295.04037175, -0.01408018, -29.50403717, -0.04154664, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24077, 4077, 0.0, 279.86950764, 0.01329924, 279.86950764, 0.03989773, 195.90865535, -3997.50531217, 0.05, 2, 0, 74030, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44077, 69.96737691, 6.958e-05, 209.90213073, 0.00020874, 699.67376911, 0.0006958, -69.96737691, -6.958e-05, -209.90213073, -0.00020874, -699.67376911, -0.0006958, 0.4, 0.3, 0.003, 0.0, 0.0, 24077, 2)
    ops.limitCurve('ThreePoint', 14077, 4077, 0.0, 314.8531961, 0.01266009, 314.8531961, 0.03798026, 220.39723727, -4323.28062858, 0.05, 2, 0, 74030, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34077, 78.71329902, 7.828e-05, 236.13989707, 0.00023483, 787.13299025, 0.00078278, -78.71329902, -7.828e-05, -236.13989707, -0.00023483, -787.13299025, -0.00078278, 0.4, 0.3, 0.003, 0.0, 0.0, 14077, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4077, 99999, 'P', 44077, 'Vy', 34077, 'Vz', 24077, 'My', 14077, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4077, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4077, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.95)
    ops.node(124031, 0.0, 0.0, 4.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 171001, 124031, 0.075, 28663377.06654114, 11943073.77772548, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 73.32179358, 0.00067564, 88.15571, 0.02234611, 8.815571, 0.08591503, -73.32179358, -0.00067564, -88.15571, -0.02234611, -8.815571, -0.08591503, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 59.65424, 0.00075121, 71.7230393, 0.02103074, 7.17230393, 0.07534368, -59.65424, -0.00075121, -71.7230393, -0.02103074, -7.17230393, -0.07534368, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 151.10785858, 0.01351285, 151.10785858, 0.04053854, 105.775501, -5126.3143472, 0.05, 2, 0, 71001, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 37.77696464, 7.212e-05, 113.33089393, 0.00021636, 377.76964644, 0.00072118, -37.77696464, -7.212e-05, -113.33089393, -0.00021636, -377.76964644, -0.00072118, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 125.92321548, 0.0150243, 125.92321548, 0.04507289, 88.14625084, -4141.33234922, 0.05, 2, 0, 71001, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 31.48080387, 6.01e-05, 94.44241161, 0.0001803, 314.8080387, 0.00060099, -31.48080387, -6.01e-05, -94.44241161, -0.0001803, -314.8080387, -0.00060099, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 0.0, 0.0, 5.375)
    ops.node(122001, 0.0, 0.0, 6.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 174031, 122001, 0.075, 28259953.11707816, 11774980.46544923, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 66.90839479, 0.000676, 80.72276868, 0.0125658, 8.07227687, 0.05112611, -66.90839479, -0.000676, -80.72276868, -0.0125658, -8.07227687, -0.05112611, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 54.26873276, 0.00075509, 65.47343386, 0.01198051, 6.54734339, 0.04562431, -54.26873276, -0.00075509, -65.47343386, -0.01198051, -6.54734339, -0.04562431, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 109.89408143, 0.01352004, 109.89408143, 0.04056012, 76.925857, -2555.98576508, 0.05, 2, 0, 74031, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 27.47352036, 5.32e-05, 82.42056107, 0.00015959, 274.73520357, 0.00053197, -27.47352036, -5.32e-05, -82.42056107, -0.00015959, -274.73520357, -0.00053197, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 83.42106829, 0.01510176, 83.42106829, 0.04530527, 58.39474781, -2148.76378434, 0.05, 2, 0, 74031, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 20.85526707, 4.038e-05, 62.56580122, 0.00012115, 208.55267073, 0.00040382, -20.85526707, -4.038e-05, -62.56580122, -0.00012115, -208.55267073, -0.00040382, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 2.95, 0.0, 3.975)
    ops.node(124032, 2.95, 0.0, 4.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 171002, 124032, 0.18, 31857286.53821601, 13273869.39092334, 0.00450368, 0.00334125, 0.00264, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 193.42010851, 0.00059725, 231.44575146, 0.01670514, 23.14457515, 0.05290079, -193.42010851, -0.00059725, -231.44575146, -0.01670514, -23.14457515, -0.05290079, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 219.57182355, 0.00058039, 262.73879221, 0.01729255, 26.27387922, 0.05679244, -219.57182355, -0.00058039, -262.73879221, -0.01729255, -26.27387922, -0.05679244, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 355.61013323, 0.01194508, 355.61013323, 0.03583523, 248.92709326, -5341.57202536, 0.05, 2, 0, 71002, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 88.90253331, 6.363e-05, 266.70759992, 0.00019088, 889.02533306, 0.00063627, -88.90253331, -6.363e-05, -266.70759992, -0.00019088, -889.02533306, -0.00063627, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 396.81752061, 0.01160787, 396.81752061, 0.03482362, 277.77226443, -5896.86958506, 0.05, 2, 0, 71002, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 99.20438015, 7.1e-05, 297.61314046, 0.000213, 992.04380154, 0.00071, -99.20438015, -7.1e-05, -297.61314046, -0.000213, -992.04380154, -0.00071, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4081, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 2.95, 0.0, 5.375)
    ops.node(122002, 2.95, 0.0, 6.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4082, 174032, 122002, 0.18, 28997101.49415643, 12082125.62256518, 0.00450368, 0.00334125, 0.00264, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24082, 182.90462891, 0.00059726, 220.15351703, 0.01757132, 22.0153517, 0.05082781, -182.90462891, -0.00059726, -220.15351703, -0.01757132, -22.0153517, -0.05082781, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14082, 207.79627098, 0.00058012, 250.11439105, 0.01819095, 25.01143911, 0.05448336, -207.79627098, -0.00058012, -250.11439105, -0.01819095, -25.01143911, -0.05448336, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24082, 4082, 0.0, 320.69047096, 0.0119452, 320.69047096, 0.03583559, 224.48332967, -5311.96708717, 0.05, 2, 0, 74032, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44082, 80.17261774, 6.304e-05, 240.51785322, 0.00018912, 801.7261774, 0.00063039, -80.17261774, -6.304e-05, -240.51785322, -0.00018912, -801.7261774, -0.00063039, 0.4, 0.3, 0.003, 0.0, 0.0, 24082, 2)
    ops.limitCurve('ThreePoint', 14082, 4082, 0.0, 357.95217647, 0.01160238, 357.95217647, 0.03480715, 250.56652353, -5897.99438551, 0.05, 2, 0, 74032, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34082, 89.48804412, 7.036e-05, 268.46413236, 0.00021109, 894.88044118, 0.00070363, -89.48804412, -7.036e-05, -268.46413236, -0.00021109, -894.88044118, -0.00070363, 0.4, 0.3, 0.003, 0.0, 0.0, 14082, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4082, 99999, 'P', 44082, 'Vy', 34082, 'Vz', 24082, 'My', 14082, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4082, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4082, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.8)
    ops.node(124033, 0.0, 0.0, 7.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4084, 172001, 124033, 0.0625, 29529951.88257354, 12304146.61773898, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24084, 52.77724437, 0.00075846, 63.6072926, 0.01282359, 6.36072926, 0.05422019, -52.77724437, -0.00075846, -63.6072926, -0.01282359, -6.36072926, -0.05422019, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14084, 52.77724437, 0.00075846, 63.6072926, 0.01282359, 6.36072926, 0.05422019, -52.77724437, -0.00075846, -63.6072926, -0.01282359, -6.36072926, -0.05422019, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24084, 4084, 0.0, 78.07767839, 0.01516916, 78.07767839, 0.04550749, 54.65437488, -2226.47094989, 0.05, 2, 0, 72001, 24033, 2, 3)
    ops.uniaxialMaterial('LimitState', 44084, 19.5194196, 4.34e-05, 58.5582588, 0.00013021, 195.19419599, 0.00043404, -19.5194196, -4.34e-05, -58.5582588, -0.00013021, -195.19419599, -0.00043404, 0.4, 0.3, 0.003, 0.0, 0.0, 24084, 2)
    ops.limitCurve('ThreePoint', 14084, 4084, 0.0, 78.07767839, 0.01516916, 78.07767839, 0.04550749, 54.65437488, -2226.47094989, 0.05, 2, 0, 72001, 24033, 1, 3)
    ops.uniaxialMaterial('LimitState', 34084, 19.5194196, 4.34e-05, 58.5582588, 0.00013021, 195.19419599, 0.00043404, -19.5194196, -4.34e-05, -58.5582588, -0.00013021, -195.19419599, -0.00043404, 0.4, 0.3, 0.003, 0.0, 0.0, 14084, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4084, 99999, 'P', 44084, 'Vy', 34084, 'Vz', 24084, 'My', 14084, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4084, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124033, 124033, 24033, 4084, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174033, 0.0, 0.0, 8.175)
    ops.node(123001, 0.0, 0.0, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4085, 174033, 123001, 0.0625, 29840476.87872986, 12433532.03280411, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24085, 45.7438631, 0.00073564, 55.29742617, 0.01329575, 5.52974262, 0.05981449, -45.7438631, -0.00073564, -55.29742617, -0.01329575, -5.52974262, -0.05981449, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14085, 45.7438631, 0.00073564, 55.29742617, 0.01329575, 5.52974262, 0.05981449, -45.7438631, -0.00073564, -55.29742617, -0.01329575, -5.52974262, -0.05981449, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24085, 4085, 0.0, 69.33003624, 0.01471285, 69.33003624, 0.04413854, 48.53102537, -2224.34287481, 0.05, 2, 0, 74033, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44085, 17.33250906, 3.814e-05, 51.99752718, 0.00011442, 173.3250906, 0.0003814, -17.33250906, -3.814e-05, -51.99752718, -0.00011442, -173.3250906, -0.0003814, 0.4, 0.3, 0.003, 0.0, 0.0, 24085, 2)
    ops.limitCurve('ThreePoint', 14085, 4085, 0.0, 69.33003624, 0.01471285, 69.33003624, 0.04413854, 48.53102537, -2224.34287481, 0.05, 2, 0, 74033, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34085, 17.33250906, 3.814e-05, 51.99752718, 0.00011442, 173.3250906, 0.0003814, -17.33250906, -3.814e-05, -51.99752718, -0.00011442, -173.3250906, -0.0003814, 0.4, 0.3, 0.003, 0.0, 0.0, 14085, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4085, 99999, 'P', 44085, 'Vy', 34085, 'Vz', 24085, 'My', 14085, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174033, 74033, 174033, 4085, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4085, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 2.95, 0.0, 6.825)
    ops.node(124034, 2.95, 0.0, 7.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4086, 172002, 124034, 0.1225, 31053670.81572603, 12939029.50655251, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24086, 138.41792014, 0.0006392, 165.9855148, 0.00882168, 16.59855148, 0.03521269, -138.41792014, -0.0006392, -165.9855148, -0.00882168, -16.59855148, -0.03521269, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14086, 138.41792014, 0.0006392, 165.9855148, 0.00882168, 16.59855148, 0.03521269, -138.41792014, -0.0006392, -165.9855148, -0.00882168, -16.59855148, -0.03521269, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24086, 4086, 0.0, 177.94049098, 0.01278399, 177.94049098, 0.03835198, 124.55834369, -2514.03915765, 0.05, 2, 0, 72002, 24034, 2, 3)
    ops.uniaxialMaterial('LimitState', 44086, 44.48512275, 4.799e-05, 133.45536824, 0.00014398, 444.85122746, 0.00047992, -44.48512275, -4.799e-05, -133.45536824, -0.00014398, -444.85122746, -0.00047992, 0.4, 0.3, 0.003, 0.0, 0.0, 24086, 2)
    ops.limitCurve('ThreePoint', 14086, 4086, 0.0, 177.94049098, 0.01278399, 177.94049098, 0.03835198, 124.55834369, -2514.03915765, 0.05, 2, 0, 72002, 24034, 1, 3)
    ops.uniaxialMaterial('LimitState', 34086, 44.48512275, 4.799e-05, 133.45536824, 0.00014398, 444.85122746, 0.00047992, -44.48512275, -4.799e-05, -133.45536824, -0.00014398, -444.85122746, -0.00047992, 0.4, 0.3, 0.003, 0.0, 0.0, 14086, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4086, 99999, 'P', 44086, 'Vy', 34086, 'Vz', 24086, 'My', 14086, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4086, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124034, 124034, 24034, 4086, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174034, 2.95, 0.0, 8.175)
    ops.node(123002, 2.95, 0.0, 9.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4087, 174034, 123002, 0.1225, 29911446.83995828, 12463102.84998262, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24087, 129.00698163, 0.00063191, 155.28654269, 0.00831751, 15.52865427, 0.03493655, -129.00698163, -0.00063191, -155.28654269, -0.00831751, -15.52865427, -0.03493655, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14087, 129.00698163, 0.00063191, 155.28654269, 0.00831751, 15.52865427, 0.03493655, -129.00698163, -0.00063191, -155.28654269, -0.00831751, -15.52865427, -0.03493655, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24087, 4087, 0.0, 154.22475833, 0.01263819, 154.22475833, 0.03791458, 107.95733083, -2263.54184277, 0.05, 2, 0, 74034, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44087, 38.55618958, 4.318e-05, 115.66856875, 0.00012955, 385.56189583, 0.00043185, -38.55618958, -4.318e-05, -115.66856875, -0.00012955, -385.56189583, -0.00043185, 0.4, 0.3, 0.003, 0.0, 0.0, 24087, 2)
    ops.limitCurve('ThreePoint', 14087, 4087, 0.0, 154.22475833, 0.01263819, 154.22475833, 0.03791458, 107.95733083, -2263.54184277, 0.05, 2, 0, 74034, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34087, 38.55618958, 4.318e-05, 115.66856875, 0.00012955, 385.56189583, 0.00043185, -38.55618958, -4.318e-05, -115.66856875, -0.00012955, -385.56189583, -0.00043185, 0.4, 0.3, 0.003, 0.0, 0.0, 14087, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4087, 99999, 'P', 44087, 'Vy', 34087, 'Vz', 24087, 'My', 14087, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174034, 74034, 174034, 4087, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4087, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.65)
    ops.node(124035, 0.0, 0.0, 10.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4089, 173001, 124035, 0.0625, 27762106.93672669, 11567544.55696946, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24089, 45.40518921, 0.0007046, 55.30168713, 0.01473539, 5.53016871, 0.06401822, -45.40518921, -0.0007046, -55.30168713, -0.01473539, -5.53016871, -0.06401822, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14089, 45.40518921, 0.0007046, 55.30168713, 0.01473539, 5.53016871, 0.06401822, -45.40518921, -0.0007046, -55.30168713, -0.01473539, -5.53016871, -0.06401822, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24089, 4089, 0.0, 70.97782021, 0.01409192, 70.97782021, 0.04227576, 49.68447415, -3075.33282947, 0.05, 2, 0, 73001, 24035, 2, 3)
    ops.uniaxialMaterial('LimitState', 44089, 17.74445505, 4.197e-05, 53.23336516, 0.00012591, 177.44455053, 0.0004197, -17.74445505, -4.197e-05, -53.23336516, -0.00012591, -177.44455053, -0.0004197, 0.4, 0.3, 0.003, 0.0, 0.0, 24089, 2)
    ops.limitCurve('ThreePoint', 14089, 4089, 0.0, 70.97782021, 0.01409192, 70.97782021, 0.04227576, 49.68447415, -3075.33282947, 0.05, 2, 0, 73001, 24035, 1, 3)
    ops.uniaxialMaterial('LimitState', 34089, 17.74445505, 4.197e-05, 53.23336516, 0.00012591, 177.44455053, 0.0004197, -17.74445505, -4.197e-05, -53.23336516, -0.00012591, -177.44455053, -0.0004197, 0.4, 0.3, 0.003, 0.0, 0.0, 14089, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4089, 99999, 'P', 44089, 'Vy', 34089, 'Vz', 24089, 'My', 14089, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4089, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124035, 124035, 24035, 4089, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174035, 0.0, 0.0, 11.025)
    ops.node(124001, 0.0, 0.0, 12.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4090, 174035, 124001, 0.0625, 29760943.88531344, 12400393.28554727, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24090, 34.97864591, 0.00074888, 42.57182522, 0.01493197, 4.25718252, 0.07149, -34.97864591, -0.00074888, -42.57182522, -0.01493197, -4.25718252, -0.07149, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14090, 34.97864591, 0.00074888, 42.57182522, 0.01493197, 4.25718252, 0.07149, -34.97864591, -0.00074888, -42.57182522, -0.01493197, -4.25718252, -0.07149, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24090, 4090, 0.0, 62.61165089, 0.01497764, 62.61165089, 0.04493291, 43.82815563, -8476.02988696, 0.05, 2, 0, 74035, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44090, 15.65291272, 3.454e-05, 46.95873817, 0.00010361, 156.52912723, 0.00034536, -15.65291272, -3.454e-05, -46.95873817, -0.00010361, -156.52912723, -0.00034536, 0.4, 0.3, 0.003, 0.0, 0.0, 24090, 2)
    ops.limitCurve('ThreePoint', 14090, 4090, 0.0, 62.61165089, 0.01497764, 62.61165089, 0.04493291, 43.82815563, -8476.02988696, 0.05, 2, 0, 74035, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34090, 15.65291272, 3.454e-05, 46.95873817, 0.00010361, 156.52912723, 0.00034536, -15.65291272, -3.454e-05, -46.95873817, -0.00010361, -156.52912723, -0.00034536, 0.4, 0.3, 0.003, 0.0, 0.0, 14090, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4090, 99999, 'P', 44090, 'Vy', 34090, 'Vz', 24090, 'My', 14090, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174035, 74035, 174035, 4090, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4090, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 2.95, 0.0, 9.675)
    ops.node(124036, 2.95, 0.0, 10.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4091, 173002, 124036, 0.1225, 29304337.85267856, 12210140.7719494, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24091, 110.72279622, 0.00061593, 134.26362537, 0.00888096, 13.42636254, 0.04036882, -110.72279622, -0.00061593, -134.26362537, -0.00888096, -13.42636254, -0.04036882, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14091, 110.72279622, 0.00061593, 134.26362537, 0.00888096, 13.42636254, 0.04036882, -110.72279622, -0.00061593, -134.26362537, -0.00888096, -13.42636254, -0.04036882, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24091, 4091, 0.0, 128.86394527, 0.01231863, 128.86394527, 0.0369559, 90.20476169, -1847.99964641, 0.05, 2, 0, 73002, 24036, 2, 3)
    ops.uniaxialMaterial('LimitState', 44091, 32.21598632, 3.683e-05, 96.64795895, 0.00011049, 322.15986317, 0.00036831, -32.21598632, -3.683e-05, -96.64795895, -0.00011049, -322.15986317, -0.00036831, 0.4, 0.3, 0.003, 0.0, 0.0, 24091, 2)
    ops.limitCurve('ThreePoint', 14091, 4091, 0.0, 128.86394527, 0.01231863, 128.86394527, 0.0369559, 90.20476169, -1847.99964641, 0.05, 2, 0, 73002, 24036, 1, 3)
    ops.uniaxialMaterial('LimitState', 34091, 32.21598632, 3.683e-05, 96.64795895, 0.00011049, 322.15986317, 0.00036831, -32.21598632, -3.683e-05, -96.64795895, -0.00011049, -322.15986317, -0.00036831, 0.4, 0.3, 0.003, 0.0, 0.0, 14091, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4091, 99999, 'P', 44091, 'Vy', 34091, 'Vz', 24091, 'My', 14091, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4091, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124036, 124036, 24036, 4091, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174036, 2.95, 0.0, 11.025)
    ops.node(124002, 2.95, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4092, 174036, 124002, 0.1225, 29564452.73588933, 12318521.97328722, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24092, 101.34363428, 0.0005904, 123.05350094, 0.00955914, 12.30535009, 0.04304101, -101.34363428, -0.0005904, -123.05350094, -0.00955914, -12.30535009, -0.04304101, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14092, 101.34363428, 0.0005904, 123.05350094, 0.00955914, 12.30535009, 0.04304101, -101.34363428, -0.0005904, -123.05350094, -0.00955914, -12.30535009, -0.04304101, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24092, 4092, 0.0, 127.18107283, 0.01180807, 127.18107283, 0.0354242, 89.02675098, -2119.38717349, 0.05, 2, 0, 74036, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44092, 31.79526821, 3.603e-05, 95.38580462, 0.00010809, 317.95268208, 0.0003603, -31.79526821, -3.603e-05, -95.38580462, -0.00010809, -317.95268208, -0.0003603, 0.4, 0.3, 0.003, 0.0, 0.0, 24092, 2)
    ops.limitCurve('ThreePoint', 14092, 4092, 0.0, 127.18107283, 0.01180807, 127.18107283, 0.0354242, 89.02675098, -2119.38717349, 0.05, 2, 0, 74036, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34092, 31.79526821, 3.603e-05, 95.38580462, 0.00010809, 317.95268208, 0.0003603, -31.79526821, -3.603e-05, -95.38580462, -0.00010809, -317.95268208, -0.0003603, 0.4, 0.3, 0.003, 0.0, 0.0, 14092, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4092, 99999, 'P', 44092, 'Vy', 34092, 'Vz', 24092, 'My', 14092, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174036, 74036, 174036, 4092, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4092, '-orient', 0, 0, 1, 0, 1, 0)
