import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 29549137.33101903, 12312140.55459126, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 61.85658309, 0.00092166, 72.99319753, 0.01516198, 7.29931975, 0.03726786, -61.85658309, -0.00092166, -72.99319753, -0.01516198, -7.29931975, -0.03726786, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 61.85658309, 0.00092166, 72.99319753, 0.01516198, 7.29931975, 0.03726786, -61.85658309, -0.00092166, -72.99319753, -0.01516198, -7.29931975, -0.03726786, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 83.13697386, 0.01843317, 83.13697386, 0.05529952, 58.1958817, -1228.91464113, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 20.78424347, 8.427e-05, 62.3527304, 0.00025281, 207.84243465, 0.0008427, -20.78424347, -8.427e-05, -62.3527304, -0.00025281, -207.84243465, -0.0008427, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 83.13697386, 0.01843317, 83.13697386, 0.05529952, 58.1958817, -1228.91464113, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 20.78424347, 8.427e-05, 62.3527304, 0.00025281, 207.84243465, 0.0008427, -20.78424347, -8.427e-05, -62.3527304, -0.00025281, -207.84243465, -0.0008427, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 7.45, 0.0, 0.0)
    ops.node(121002, 7.45, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.0625, 31441526.12307622, 13100635.88461509, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 76.89776581, 0.00093298, 90.30409898, 0.01616507, 9.0304099, 0.04239829, -76.89776581, -0.00093298, -90.30409898, -0.01616507, -9.0304099, -0.04239829, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 76.89776581, 0.00093298, 90.30409898, 0.01616507, 9.0304099, 0.04239829, -76.89776581, -0.00093298, -90.30409898, -0.01616507, -9.0304099, -0.04239829, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 97.41711692, 0.01865968, 97.41711692, 0.05597904, 68.19198184, -1457.40870789, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 24.35427923, 9.28e-05, 73.06283769, 0.00027841, 243.5427923, 0.00092802, -24.35427923, -9.28e-05, -73.06283769, -0.00027841, -243.5427923, -0.00092802, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 97.41711692, 0.01865968, 97.41711692, 0.05597904, 68.19198184, -1457.40870789, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 24.35427923, 9.28e-05, 73.06283769, 0.00027841, 243.5427923, 0.00092802, -24.35427923, -9.28e-05, -73.06283769, -0.00027841, -243.5427923, -0.00092802, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 10.3, 0.0, 0.0)
    ops.node(121003, 10.3, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.0625, 31171370.52145547, 12988071.05060645, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 76.55963645, 0.00095764, 89.90361621, 0.01601067, 8.99036162, 0.04153641, -76.55963645, -0.00095764, -89.90361621, -0.01601067, -8.99036162, -0.04153641, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 76.55963645, 0.00095764, 89.90361621, 0.01601067, 8.99036162, 0.04153641, -76.55963645, -0.00095764, -89.90361621, -0.01601067, -8.99036162, -0.04153641, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 97.17202613, 0.01915279, 97.17202613, 0.05745838, 68.02041829, -1466.25681355, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 24.29300653, 9.337e-05, 72.8790196, 0.00028011, 242.93006533, 0.00093371, -24.29300653, -9.337e-05, -72.8790196, -0.00028011, -242.93006533, -0.00093371, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 97.17202613, 0.01915279, 97.17202613, 0.05745838, 68.02041829, -1466.25681355, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 24.29300653, 9.337e-05, 72.8790196, 0.00028011, 242.93006533, 0.00093371, -24.29300653, -9.337e-05, -72.8790196, -0.00028011, -242.93006533, -0.00093371, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 17.75, 0.0, 0.0)
    ops.node(121004, 17.75, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.0625, 31135749.74835729, 12973229.06181554, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 62.25311743, 0.00092877, 73.48894182, 0.01593461, 7.34889418, 0.04173214, -62.25311743, -0.00092877, -73.48894182, -0.01593461, -7.34889418, -0.04173214, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 62.25311743, 0.00092877, 73.48894182, 0.01593461, 7.34889418, 0.04173214, -62.25311743, -0.00092877, -73.48894182, -0.01593461, -7.34889418, -0.04173214, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 87.6423257, 0.01857549, 87.6423257, 0.05572648, 61.34962799, -1231.49501282, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 21.91058143, 8.431e-05, 65.73174428, 0.00025293, 219.10581426, 0.0008431, -21.91058143, -8.431e-05, -65.73174428, -0.00025293, -219.10581426, -0.0008431, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 87.6423257, 0.01857549, 87.6423257, 0.05572648, 61.34962799, -1231.49501282, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 21.91058143, 8.431e-05, 65.73174428, 0.00025293, 219.10581426, 0.0008431, -21.91058143, -8.431e-05, -65.73174428, -0.00025293, -219.10581426, -0.0008431, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 3.5, 0.0)
    ops.node(121005, 0.0, 3.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.0625, 30914198.70810824, 12880916.12837843, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 86.06651368, 0.00102862, 100.58340286, 0.01272721, 10.05834029, 0.02786606, -86.06651368, -0.00102862, -100.58340286, -0.01272721, -10.05834029, -0.02786606, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 86.06651368, 0.00102862, 100.58340286, 0.01272721, 10.05834029, 0.02786606, -86.06651368, -0.00102862, -100.58340286, -0.01272721, -10.05834029, -0.02786606, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 74.99196665, 0.02057233, 74.99196665, 0.06171699, 52.49437666, -1404.46035096, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 18.74799166, 7.266e-05, 56.24397499, 0.00021797, 187.47991664, 0.00072658, -18.74799166, -7.266e-05, -56.24397499, -0.00021797, -187.47991664, -0.00072658, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 74.99196665, 0.02057233, 74.99196665, 0.06171699, 52.49437666, -1404.46035096, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 18.74799166, 7.266e-05, 56.24397499, 0.00021797, 187.47991664, 0.00072658, -18.74799166, -7.266e-05, -56.24397499, -0.00021797, -187.47991664, -0.00072658, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 17.75, 3.5, 0.0)
    ops.node(121008, 17.75, 3.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.0625, 30558146.77667942, 12732561.15694976, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 85.68791693, 0.00102857, 100.10244737, 0.01234973, 10.01024474, 0.02682886, -85.68791693, -0.00102857, -100.10244737, -0.01234973, -10.01024474, -0.02682886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 85.68791693, 0.00102857, 100.10244737, 0.01234973, 10.01024474, 0.02682886, -85.68791693, -0.00102857, -100.10244737, -0.01234973, -10.01024474, -0.02682886, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 74.11806534, 0.02057146, 74.11806534, 0.06171439, 51.88264574, -1395.11573238, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 18.52951633, 7.265e-05, 55.588549, 0.00021794, 185.29516334, 0.00072648, -18.52951633, -7.265e-05, -55.588549, -0.00021794, -185.29516334, -0.00072648, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 74.11806534, 0.02057146, 74.11806534, 0.06171439, 51.88264574, -1395.11573238, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 18.52951633, 7.265e-05, 55.588549, 0.00021794, 185.29516334, 0.00072648, -18.52951633, -7.265e-05, -55.588549, -0.00021794, -185.29516334, -0.00072648, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 7.0, 0.0)
    ops.node(121009, 0.0, 7.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.0625, 31610591.77548276, 13171079.90645115, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 85.05154434, 0.00101617, 99.44275995, 0.01535619, 9.944276, 0.03565096, -85.05154434, -0.00101617, -99.44275995, -0.01535619, -9.944276, -0.03565096, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 79.92270853, 0.00101617, 93.44609531, 0.01535619, 9.34460953, 0.03565096, -79.92270853, -0.00101617, -93.44609531, -0.01535619, -9.34460953, -0.03565096, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 96.55869116, 0.02032338, 96.55869116, 0.06097015, 67.59108381, -1507.4340185, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 24.13967279, 9.149e-05, 72.41901837, 0.00027448, 241.39672791, 0.00091492, -24.13967279, -9.149e-05, -72.41901837, -0.00027448, -241.39672791, -0.00091492, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 96.55869116, 0.02032338, 96.55869116, 0.06097015, 67.59108381, -1507.4340185, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 24.13967279, 9.149e-05, 72.41901837, 0.00027448, 241.39672791, 0.00091492, -24.13967279, -9.149e-05, -72.41901837, -0.00027448, -241.39672791, -0.00091492, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 7.45, 7.0, 0.0)
    ops.node(121010, 7.45, 7.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.1225, 30834168.09717469, 12847570.04048946, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 147.9404694, 0.00068318, 175.91407138, 0.02916526, 17.59140714, 0.07054229, -147.9404694, -0.00068318, -175.91407138, -0.02916526, -17.59140714, -0.07054229, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 155.53115995, 0.00068318, 184.94006193, 0.02916526, 18.49400619, 0.07054229, -155.53115995, -0.00068318, -184.94006193, -0.02916526, -18.49400619, -0.07054229, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 178.74484079, 0.01366368, 178.74484079, 0.04099104, 125.12138855, -2522.98256327, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 44.6862102, 8.859e-05, 134.05863059, 0.00026576, 446.86210197, 0.00088587, -44.6862102, -8.859e-05, -134.05863059, -0.00026576, -446.86210197, -0.00088587, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 178.74484079, 0.01366368, 178.74484079, 0.04099104, 125.12138855, -2522.98256327, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 44.6862102, 8.859e-05, 134.05863059, 0.00026576, 446.86210197, 0.00088587, -44.6862102, -8.859e-05, -134.05863059, -0.00026576, -446.86210197, -0.00088587, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 10.3, 7.0, 0.0)
    ops.node(121011, 10.3, 7.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.1225, 30744531.39287541, 12810221.41369809, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 149.40618999, 0.0006734, 177.67058681, 0.02890035, 17.76705868, 0.07002676, -149.40618999, -0.0006734, -177.67058681, -0.02890035, -17.76705868, -0.07002676, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 157.46920025, 0.0006734, 187.25894298, 0.02890035, 18.7258943, 0.07002676, -157.46920025, -0.0006734, -187.25894298, -0.02890035, -18.7258943, -0.07002676, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 176.84515213, 0.01346805, 176.84515213, 0.04040416, 123.79160649, -2483.18964143, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 44.21128803, 8.79e-05, 132.6338641, 0.0002637, 442.11288032, 0.00087901, -44.21128803, -8.79e-05, -132.6338641, -0.0002637, -442.11288032, -0.00087901, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 176.84515213, 0.01346805, 176.84515213, 0.04040416, 123.79160649, -2483.18964143, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 44.21128803, 8.79e-05, 132.6338641, 0.0002637, 442.11288032, 0.00087901, -44.21128803, -8.79e-05, -132.6338641, -0.0002637, -442.11288032, -0.00087901, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 17.75, 7.0, 0.0)
    ops.node(121012, 17.75, 7.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.0625, 31615232.57031474, 13173013.57096447, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 84.4267502, 0.00101672, 98.71242402, 0.01555622, 9.8712424, 0.03586143, -84.4267502, -0.00101672, -98.71242402, -0.01555622, -9.8712424, -0.03586143, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 79.44732101, 0.00101672, 92.89043603, 0.01555622, 9.2890436, 0.03586143, -79.44732101, -0.00101672, -92.89043603, -0.01555622, -9.2890436, -0.03586143, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 98.16169073, 0.02033443, 98.16169073, 0.0610033, 68.71318351, -1520.81073838, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 24.54042268, 9.3e-05, 73.62126805, 0.00027899, 245.40422683, 0.00092998, -24.54042268, -9.3e-05, -73.62126805, -0.00027899, -245.40422683, -0.00092998, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 98.16169073, 0.02033443, 98.16169073, 0.0610033, 68.71318351, -1520.81073838, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 24.54042268, 9.3e-05, 73.62126805, 0.00027899, 245.40422683, 0.00092998, -24.54042268, -9.3e-05, -73.62126805, -0.00027899, -245.40422683, -0.00092998, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 10.5, 0.0)
    ops.node(121013, 0.0, 10.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0625, 31392802.67323792, 13080334.44718247, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 62.71412785, 0.00091438, 74.0258566, 0.01609257, 7.40258566, 0.04246185, -62.71412785, -0.00091438, -74.0258566, -0.01609257, -7.40258566, -0.04246185, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 62.71412785, 0.00091438, 74.0258566, 0.01609257, 7.40258566, 0.04246185, -62.71412785, -0.00091438, -74.0258566, -0.01609257, -7.40258566, -0.04246185, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 89.46712446, 0.01828763, 89.46712446, 0.0548629, 62.62698712, -1245.56712441, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 22.36678112, 8.536e-05, 67.10034335, 0.00025608, 223.66781115, 0.00085361, -22.36678112, -8.536e-05, -67.10034335, -0.00025608, -223.66781115, -0.00085361, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 89.46712446, 0.01828763, 89.46712446, 0.0548629, 62.62698712, -1245.56712441, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 22.36678112, 8.536e-05, 67.10034335, 0.00025608, 223.66781115, 0.00085361, -22.36678112, -8.536e-05, -67.10034335, -0.00025608, -223.66781115, -0.00085361, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 7.45, 10.5, 0.0)
    ops.node(121014, 7.45, 10.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.0625, 30302653.07040482, 12626105.44600201, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 76.64711525, 0.00094086, 89.96256931, 0.01600058, 8.99625693, 0.03920702, -76.64711525, -0.00094086, -89.96256931, -0.01600058, -8.99625693, -0.03920702, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 76.64711525, 0.00094086, 89.96256931, 0.01600058, 8.99625693, 0.03920702, -76.64711525, -0.00094086, -89.96256931, -0.01600058, -8.99625693, -0.03920702, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 95.11515147, 0.01881728, 95.11515147, 0.05645185, 66.58060603, -1466.4179345, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 23.77878787, 9.401e-05, 71.3363636, 0.00028204, 237.78787866, 0.00094015, -23.77878787, -9.401e-05, -71.3363636, -0.00028204, -237.78787866, -0.00094015, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 95.11515147, 0.01881728, 95.11515147, 0.05645185, 66.58060603, -1466.4179345, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 23.77878787, 9.401e-05, 71.3363636, 0.00028204, 237.78787866, 0.00094015, -23.77878787, -9.401e-05, -71.3363636, -0.00028204, -237.78787866, -0.00094015, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 10.3, 10.5, 0.0)
    ops.node(121015, 10.3, 10.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.0625, 31356027.21230935, 13065011.33846223, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 78.03107249, 0.00091731, 91.63440251, 0.01638552, 9.16344025, 0.04239561, -78.03107249, -0.00091731, -91.63440251, -0.01638552, -9.16344025, -0.04239561, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 78.03107249, 0.00091731, 91.63440251, 0.01638552, 9.16344025, 0.04239561, -78.03107249, -0.00091731, -91.63440251, -0.01638552, -9.16344025, -0.04239561, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 98.08510902, 0.0183463, 98.08510902, 0.05503889, 68.65957632, -1476.73451229, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 24.52127726, 9.369e-05, 73.56383177, 0.00028108, 245.21277256, 0.00093693, -24.52127726, -9.369e-05, -73.56383177, -0.00028108, -245.21277256, -0.00093693, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 98.08510902, 0.0183463, 98.08510902, 0.05503889, 68.65957632, -1476.73451229, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 24.52127726, 9.369e-05, 73.56383177, 0.00028108, 245.21277256, 0.00093693, -24.52127726, -9.369e-05, -73.56383177, -0.00028108, -245.21277256, -0.00093693, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 17.75, 10.5, 0.0)
    ops.node(121016, 17.75, 10.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.0625, 30490892.56382168, 12704538.56825903, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 61.85285766, 0.00093244, 73.02061785, 0.01562605, 7.30206179, 0.03995561, -61.85285766, -0.00093244, -73.02061785, -0.01562605, -7.30206179, -0.03995561, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 61.85285766, 0.00093244, 73.02061785, 0.01562605, 7.30206179, 0.03995561, -61.85285766, -0.00093244, -73.02061785, -0.01562605, -7.30206179, -0.03995561, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 85.72587937, 0.01864872, 85.72587937, 0.05594616, 60.00811556, -1235.68457877, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 21.43146984, 8.421e-05, 64.29440953, 0.00025263, 214.31469843, 0.00084211, -21.43146984, -8.421e-05, -64.29440953, -0.00025263, -214.31469843, -0.00084211, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 85.72587937, 0.01864872, 85.72587937, 0.05594616, 60.00811556, -1235.68457877, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 21.43146984, 8.421e-05, 64.29440953, 0.00025263, 214.31469843, 0.00084211, -21.43146984, -8.421e-05, -64.29440953, -0.00025263, -214.31469843, -0.00084211, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 2.9)
    ops.node(122001, 0.0, 0.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 32075593.81419361, 13364830.755914, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 56.86689225, 0.00089294, 67.5390329, 0.01847735, 6.75390329, 0.05240881, -56.86689225, -0.00089294, -67.5390329, -0.01847735, -6.75390329, -0.05240881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 54.50599884, 0.00089294, 64.73507349, 0.01847735, 6.47350735, 0.05240881, -54.50599884, -0.00089294, -64.73507349, -0.01847735, -6.47350735, -0.05240881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 83.13701716, 0.0178587, 83.13701716, 0.05357611, 58.19591201, -1031.02193793, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 20.78425429, 7.763e-05, 62.35276287, 0.0002329, 207.8425429, 0.00077633, -20.78425429, -7.763e-05, -62.35276287, -0.0002329, -207.8425429, -0.00077633, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 83.13701716, 0.0178587, 83.13701716, 0.05357611, 58.19591201, -1031.02193793, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 20.78425429, 7.763e-05, 62.35276287, 0.0002329, 207.8425429, 0.00077633, -20.78425429, -7.763e-05, -62.35276287, -0.0002329, -207.8425429, -0.00077633, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 7.45, 0.0, 2.9)
    ops.node(122002, 7.45, 0.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.0625, 32329959.53314506, 13470816.47214377, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 53.95642613, 0.00087129, 63.82884586, 0.01753145, 6.38288459, 0.05323579, -53.95642613, -0.00087129, -63.82884586, -0.01753145, -6.38288459, -0.05323579, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 51.57666694, 0.00087129, 61.01366159, 0.01753145, 6.10136616, 0.05323579, -51.57666694, -0.00087129, -61.01366159, -0.01753145, -6.10136616, -0.05323579, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 92.67224372, 0.01742577, 92.67224372, 0.05227731, 64.87057061, -1243.78788823, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 23.16806093, 8.586e-05, 69.50418279, 0.00025757, 231.68060931, 0.00085856, -23.16806093, -8.586e-05, -69.50418279, -0.00025757, -231.68060931, -0.00085856, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 92.67224372, 0.01742577, 92.67224372, 0.05227731, 64.87057061, -1243.78788823, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 23.16806093, 8.586e-05, 69.50418279, 0.00025757, 231.68060931, 0.00085856, -23.16806093, -8.586e-05, -69.50418279, -0.00025757, -231.68060931, -0.00085856, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 10.3, 0.0, 2.9)
    ops.node(122003, 10.3, 0.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.0625, 31310448.18327602, 13046020.07636501, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 54.34659366, 0.00085867, 64.3592387, 0.01699659, 6.43592387, 0.05025864, -54.34659366, -0.00085867, -64.3592387, -0.01699659, -6.43592387, -0.05025864, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 51.70993181, 0.00085867, 61.23680658, 0.01699659, 6.12368066, 0.05025864, -51.70993181, -0.00085867, -61.23680658, -0.01699659, -6.12368066, -0.05025864, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 90.01908341, 0.01717335, 90.01908341, 0.05152005, 63.01335839, -1235.35828878, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 22.50477085, 8.611e-05, 67.51431256, 0.00025834, 225.04770853, 0.00086113, -22.50477085, -8.611e-05, -67.51431256, -0.00025834, -225.04770853, -0.00086113, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 90.01908341, 0.01717335, 90.01908341, 0.05152005, 63.01335839, -1235.35828878, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 22.50477085, 8.611e-05, 67.51431256, 0.00025834, 225.04770853, 0.00086113, -22.50477085, -8.611e-05, -67.51431256, -0.00025834, -225.04770853, -0.00086113, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 17.75, 0.0, 2.9)
    ops.node(122004, 17.75, 0.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.0625, 32299093.1946432, 13457955.497768, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 58.34684307, 0.0008637, 69.27149982, 0.01798685, 6.92714998, 0.05233761, -58.34684307, -0.0008637, -69.27149982, -0.01798685, -6.92714998, -0.05233761, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 55.66525289, 0.0008637, 66.08781817, 0.01798685, 6.60878182, 0.05233761, -55.66525289, -0.0008637, -66.08781817, -0.01798685, -6.60878182, -0.05233761, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 80.88849809, 0.01727393, 80.88849809, 0.05182179, 56.62194866, -1020.8408413, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 20.22212452, 7.501e-05, 60.66637357, 0.00022503, 202.22124522, 0.00075011, -20.22212452, -7.501e-05, -60.66637357, -0.00022503, -202.22124522, -0.00075011, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 80.88849809, 0.01727393, 80.88849809, 0.05182179, 56.62194866, -1020.8408413, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 20.22212452, 7.501e-05, 60.66637357, 0.00022503, 202.22124522, 0.00075011, -20.22212452, -7.501e-05, -60.66637357, -0.00022503, -202.22124522, -0.00075011, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 3.5, 2.9)
    ops.node(122005, 0.0, 3.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.0625, 30028935.70045829, 12512056.54185762, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 81.16514353, 0.00098408, 95.75737543, 0.01512714, 9.57573754, 0.03364543, -81.16514353, -0.00098408, -95.75737543, -0.01512714, -9.57573754, -0.03364543, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 76.40523608, 0.00098408, 90.14171056, 0.01512714, 9.01417106, 0.03364543, -76.40523608, -0.00098408, -90.14171056, -0.01512714, -9.01417106, -0.03364543, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 65.08863241, 0.01968167, 65.08863241, 0.05904502, 45.56204268, -1133.27647286, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 16.2721581, 6.492e-05, 48.81647431, 0.00019477, 162.72158102, 0.00064922, -16.2721581, -6.492e-05, -48.81647431, -0.00019477, -162.72158102, -0.00064922, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 65.08863241, 0.01968167, 65.08863241, 0.05904502, 45.56204268, -1133.27647286, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 16.2721581, 6.492e-05, 48.81647431, 0.00019477, 162.72158102, 0.00064922, -16.2721581, -6.492e-05, -48.81647431, -0.00019477, -162.72158102, -0.00064922, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 17.75, 3.5, 2.9)
    ops.node(122008, 17.75, 3.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.0625, 31336381.13659529, 13056825.47358137, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 82.63134116, 0.00097155, 97.494172, 0.01547072, 9.7494172, 0.03641687, -82.63134116, -0.00097155, -97.494172, -0.01547072, -9.7494172, -0.03641687, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 77.74596556, 0.00097155, 91.73006794, 0.01547072, 9.17300679, 0.03641687, -77.74596556, -0.00097155, -91.73006794, -0.01547072, -9.17300679, -0.03641687, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 68.08440535, 0.01943092, 68.08440535, 0.05829275, 47.65908375, -1129.36961686, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 17.02110134, 6.508e-05, 51.06330401, 0.00019523, 170.21101338, 0.00065077, -17.02110134, -6.508e-05, -51.06330401, -0.00019523, -170.21101338, -0.00065077, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 68.08440535, 0.01943092, 68.08440535, 0.05829275, 47.65908375, -1129.36961686, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 17.02110134, 6.508e-05, 51.06330401, 0.00019523, 170.21101338, 0.00065077, -17.02110134, -6.508e-05, -51.06330401, -0.00019523, -170.21101338, -0.00065077, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 7.0, 2.9)
    ops.node(122009, 0.0, 7.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.0625, 29935044.88287506, 12472935.36786461, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 81.3059503, 0.00095059, 95.91858576, 0.01739916, 9.59185858, 0.04007047, -81.3059503, -0.00095059, -95.91858576, -0.01739916, -9.59185858, -0.04007047, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 71.18862124, 0.00095059, 83.98292926, 0.01739916, 8.39829293, 0.04007047, -71.18862124, -0.00095059, -83.98292926, -0.01739916, -8.39829293, -0.04007047, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 82.98087751, 0.01901184, 82.98087751, 0.05703553, 58.08661426, -1235.25357262, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 20.74521938, 8.303e-05, 62.23565813, 0.00024908, 207.45219378, 0.00083028, -20.74521938, -8.303e-05, -62.23565813, -0.00024908, -207.45219378, -0.00083028, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 82.98087751, 0.01901184, 82.98087751, 0.05703553, 58.08661426, -1235.25357262, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 20.74521938, 8.303e-05, 62.23565813, 0.00024908, 207.45219378, 0.00083028, -20.74521938, -8.303e-05, -62.23565813, -0.00024908, -207.45219378, -0.00083028, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 7.45, 7.0, 2.9)
    ops.node(122010, 7.45, 7.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.1225, 31154246.17458325, 12980935.90607635, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 114.75089496, 0.00063828, 137.08470277, 0.02975044, 13.70847028, 0.07874282, -114.75089496, -0.00063828, -137.08470277, -0.02975044, -13.70847028, -0.07874282, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 107.50547606, 0.00063828, 128.42911802, 0.02975044, 12.8429118, 0.07874282, -107.50547606, -0.00063828, -128.42911802, -0.02975044, -12.8429118, -0.07874282, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 166.71684585, 0.01276562, 166.71684585, 0.03829687, 116.7017921, -2224.08623262, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 41.67921146, 8.178e-05, 125.03763439, 0.00024533, 416.79211464, 0.00081777, -41.67921146, -8.178e-05, -125.03763439, -0.00024533, -416.79211464, -0.00081777, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 166.71684585, 0.01276562, 166.71684585, 0.03829687, 116.7017921, -2224.08623262, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 41.67921146, 8.178e-05, 125.03763439, 0.00024533, 416.79211464, 0.00081777, -41.67921146, -8.178e-05, -125.03763439, -0.00024533, -416.79211464, -0.00081777, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 10.3, 7.0, 2.9)
    ops.node(122011, 10.3, 7.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.1225, 30124476.33149886, 12551865.13812453, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 113.23985192, 0.00066135, 135.46662061, 0.02943329, 13.54666206, 0.07585787, -113.23985192, -0.00066135, -135.46662061, -0.02943329, -13.54666206, -0.07585787, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 106.49045814, 0.00066135, 127.39245281, 0.02943329, 12.73924528, 0.07585787, -106.49045814, -0.00066135, -127.39245281, -0.02943329, -12.73924528, -0.07585787, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 163.52272192, 0.01322702, 163.52272192, 0.03968107, 114.46590534, -2252.12615162, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 40.88068048, 8.295e-05, 122.64204144, 0.00024886, 408.8068048, 0.00082952, -40.88068048, -8.295e-05, -122.64204144, -0.00024886, -408.8068048, -0.00082952, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 163.52272192, 0.01322702, 163.52272192, 0.03968107, 114.46590534, -2252.12615162, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 40.88068048, 8.295e-05, 122.64204144, 0.00024886, 408.8068048, 0.00082952, -40.88068048, -8.295e-05, -122.64204144, -0.00024886, -408.8068048, -0.00082952, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 17.75, 7.0, 2.9)
    ops.node(122012, 17.75, 7.0, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.0625, 30270924.68025571, 12612885.28343988, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 82.05272187, 0.00096442, 96.81444736, 0.01748438, 9.68144474, 0.04094728, -82.05272187, -0.00096442, -96.81444736, -0.01748438, -9.68144474, -0.04094728, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 71.92597803, 0.00096442, 84.8658479, 0.01748438, 8.48658479, 0.04094728, -71.92597803, -0.00096442, -84.8658479, -0.01748438, -8.48658479, -0.04094728, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 83.5451756, 0.01928843, 83.5451756, 0.05786528, 58.48162292, -1230.77735996, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 20.8862939, 8.266e-05, 62.6588817, 0.00024799, 208.862939, 0.00082665, -20.8862939, -8.266e-05, -62.6588817, -0.00024799, -208.862939, -0.00082665, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 83.5451756, 0.01928843, 83.5451756, 0.05786528, 58.48162292, -1230.77735996, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 20.8862939, 8.266e-05, 62.6588817, 0.00024799, 208.862939, 0.00082665, -20.8862939, -8.266e-05, -62.6588817, -0.00024799, -208.862939, -0.00082665, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 10.5, 2.9)
    ops.node(122013, 0.0, 10.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0625, 31555036.01345144, 13147931.67227143, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 58.46473706, 0.0008456, 69.48883013, 0.01834347, 6.94888301, 0.05126914, -58.46473706, -0.0008456, -69.48883013, -0.01834347, -6.94888301, -0.05126914, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 55.63945698, 0.0008456, 66.13081609, 0.01834347, 6.61308161, 0.05126914, -55.63945698, -0.0008456, -66.13081609, -0.01834347, -6.61308161, -0.05126914, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 82.05886981, 0.01691195, 82.05886981, 0.05073584, 57.44120887, -1036.905524, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 20.51471745, 7.789e-05, 61.54415236, 0.00023367, 205.14717453, 0.0007789, -20.51471745, -7.789e-05, -61.54415236, -0.00023367, -205.14717453, -0.0007789, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 82.05886981, 0.01691195, 82.05886981, 0.05073584, 57.44120887, -1036.905524, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 20.51471745, 7.789e-05, 61.54415236, 0.00023367, 205.14717453, 0.0007789, -20.51471745, -7.789e-05, -61.54415236, -0.00023367, -205.14717453, -0.0007789, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 7.45, 10.5, 2.9)
    ops.node(122014, 7.45, 10.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.0625, 30625221.39506496, 12760508.9146104, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 54.91904418, 0.0008849, 65.06176522, 0.01645649, 6.50617652, 0.04798448, -54.91904418, -0.0008849, -65.06176522, -0.01645649, -6.50617652, -0.04798448, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 52.20976571, 0.0008849, 61.85212379, 0.01645649, 6.18521238, 0.04798448, -52.20976571, -0.0008849, -61.85212379, -0.01645649, -6.18521238, -0.04798448, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 88.31953084, 0.01769803, 88.31953084, 0.05309409, 61.82367159, -1231.33402814, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 22.07988271, 8.638e-05, 66.23964813, 0.00025913, 220.79882711, 0.00086378, -22.07988271, -8.638e-05, -66.23964813, -0.00025913, -220.79882711, -0.00086378, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 88.31953084, 0.01769803, 88.31953084, 0.05309409, 61.82367159, -1231.33402814, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 22.07988271, 8.638e-05, 66.23964813, 0.00025913, 220.79882711, 0.00086378, -22.07988271, -8.638e-05, -66.23964813, -0.00025913, -220.79882711, -0.00086378, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 10.3, 10.5, 2.9)
    ops.node(122015, 10.3, 10.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.0625, 30177516.60486295, 12573965.25202623, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 54.49649225, 0.00089201, 64.56697392, 0.01661675, 6.45669739, 0.04697262, -54.49649225, -0.00089201, -64.56697392, -0.01661675, -6.45669739, -0.04697262, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 51.87083568, 0.00089201, 61.45611866, 0.01661675, 6.14561187, 0.04697262, -51.87083568, -0.00089201, -61.45611866, -0.01661675, -6.14561187, -0.04697262, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 87.45415964, 0.01784029, 87.45415964, 0.05352087, 61.21791175, -1234.35343555, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 21.86353991, 8.68e-05, 65.59061973, 0.0002604, 218.63539909, 0.00086801, -21.86353991, -8.68e-05, -65.59061973, -0.0002604, -218.63539909, -0.00086801, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 87.45415964, 0.01784029, 87.45415964, 0.05352087, 61.21791175, -1234.35343555, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 21.86353991, 8.68e-05, 65.59061973, 0.0002604, 218.63539909, 0.00086801, -21.86353991, -8.68e-05, -65.59061973, -0.0002604, -218.63539909, -0.00086801, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 17.75, 10.5, 2.9)
    ops.node(122016, 17.75, 10.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.0625, 30607664.87715465, 12753193.69881444, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 56.54920088, 0.00090062, 67.27923991, 0.01779024, 6.72792399, 0.04877901, -56.54920088, -0.00090062, -67.27923991, -0.01779024, -6.72792399, -0.04877901, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 54.14976876, 0.00090062, 64.42452284, 0.01779024, 6.44245228, 0.04877901, -54.14976876, -0.00090062, -64.42452284, -0.01779024, -6.44245228, -0.04877901, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 77.22067611, 0.0180123, 77.22067611, 0.05403691, 54.05447328, -1024.16617491, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 19.30516903, 7.557e-05, 57.91550708, 0.0002267, 193.05169027, 0.00075566, -19.30516903, -7.557e-05, -57.91550708, -0.0002267, -193.05169027, -0.00075566, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 77.22067611, 0.0180123, 77.22067611, 0.05403691, 54.05447328, -1024.16617491, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 19.30516903, 7.557e-05, 57.91550708, 0.0002267, 193.05169027, 0.00075566, -19.30516903, -7.557e-05, -57.91550708, -0.0002267, -193.05169027, -0.00075566, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.5)
    ops.node(123001, 0.0, 0.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 30963576.5221842, 12901490.21757675, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 40.92909716, 0.000828, 49.04239363, 0.01933802, 4.90423936, 0.0589278, -40.92909716, -0.000828, -49.04239363, -0.01933802, -4.90423936, -0.0589278, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 40.92909716, 0.000828, 49.04239363, 0.01933802, 4.90423936, 0.0589278, -40.92909716, -0.000828, -49.04239363, -0.01933802, -4.90423936, -0.0589278, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 70.09489768, 0.01655995, 70.09489768, 0.04967984, 49.06642837, -841.15426643, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 17.52372442, 6.78e-05, 52.57117326, 0.00020341, 175.23724419, 0.00067805, -17.52372442, -6.78e-05, -52.57117326, -0.00020341, -175.23724419, -0.00067805, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 70.09489768, 0.01655995, 70.09489768, 0.04967984, 49.06642837, -841.15426643, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 17.52372442, 6.78e-05, 52.57117326, 0.00020341, 175.23724419, 0.00067805, -17.52372442, -6.78e-05, -52.57117326, -0.00020341, -175.23724419, -0.00067805, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 7.45, 0.0, 5.5)
    ops.node(123002, 7.45, 0.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 31248152.84991597, 13020063.68746499, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 36.82174654, 0.00080175, 43.9767901, 0.01880697, 4.39767901, 0.06137113, -36.82174654, -0.00080175, -43.9767901, -0.01880697, -4.39767901, -0.06137113, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 36.82174654, 0.00080175, 43.9767901, 0.01880697, 4.39767901, 0.06137113, -36.82174654, -0.00080175, -43.9767901, -0.01880697, -4.39767901, -0.06137113, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 81.62664985, 0.01603502, 81.62664985, 0.04810507, 57.1386549, -1033.11039689, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 20.40666246, 7.824e-05, 61.21998739, 0.00023472, 204.06662463, 0.00078241, -20.40666246, -7.824e-05, -61.21998739, -0.00023472, -204.06662463, -0.00078241, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 81.62664985, 0.01603502, 81.62664985, 0.04810507, 57.1386549, -1033.11039689, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 20.40666246, 7.824e-05, 61.21998739, 0.00023472, 204.06662463, 0.00078241, -20.40666246, -7.824e-05, -61.21998739, -0.00023472, -204.06662463, -0.00078241, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 10.3, 0.0, 5.5)
    ops.node(123003, 10.3, 0.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0625, 30548724.20806331, 12728635.08669305, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 36.72988169, 0.00078101, 43.91172128, 0.0184078, 4.39117213, 0.05948771, -36.72988169, -0.00078101, -43.91172128, -0.0184078, -4.39117213, -0.05948771, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 36.72988169, 0.00078101, 43.91172128, 0.0184078, 4.39117213, 0.05948771, -36.72988169, -0.00078101, -43.91172128, -0.0184078, -4.39117213, -0.05948771, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 79.22960202, 0.01562029, 79.22960202, 0.04686086, 55.46072141, -1007.80707535, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 19.8074005, 7.768e-05, 59.42220151, 0.00023305, 198.07400505, 0.00077682, -19.8074005, -7.768e-05, -59.42220151, -0.00023305, -198.07400505, -0.00077682, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 79.22960202, 0.01562029, 79.22960202, 0.04686086, 55.46072141, -1007.80707535, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 19.8074005, 7.768e-05, 59.42220151, 0.00023305, 198.07400505, 0.00077682, -19.8074005, -7.768e-05, -59.42220151, -0.00023305, -198.07400505, -0.00077682, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 17.75, 0.0, 5.5)
    ops.node(123004, 17.75, 0.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 31663722.74928774, 13193217.81220322, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 41.34059489, 0.00080733, 49.46821983, 0.01988904, 4.94682198, 0.06058169, -41.34059489, -0.00080733, -49.46821983, -0.01988904, -4.94682198, -0.06058169, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 41.34059489, 0.00080733, 49.46821983, 0.01988904, 4.94682198, 0.06058169, -41.34059489, -0.00080733, -49.46821983, -0.01988904, -4.94682198, -0.06058169, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 74.79786581, 0.01614669, 74.79786581, 0.04844006, 52.35850607, -852.47569617, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 18.69946645, 7.075e-05, 56.09839936, 0.00021226, 186.99466453, 0.00070754, -18.69946645, -7.075e-05, -56.09839936, -0.00021226, -186.99466453, -0.00070754, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 74.79786581, 0.01614669, 74.79786581, 0.04844006, 52.35850607, -852.47569617, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 18.69946645, 7.075e-05, 56.09839936, 0.00021226, 186.99466453, 0.00070754, -18.69946645, -7.075e-05, -56.09839936, -0.00021226, -186.99466453, -0.00070754, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 3.5, 5.5)
    ops.node(123005, 0.0, 3.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 31284154.91546357, 13035064.54810982, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 59.90114013, 0.0009025, 71.33025021, 0.01658613, 7.13302502, 0.04401973, -59.90114013, -0.0009025, -71.33025021, -0.01658613, -7.13302502, -0.04401973, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 59.90114013, 0.0009025, 71.33025021, 0.01658613, 7.13302502, 0.04401973, -59.90114013, -0.0009025, -71.33025021, -0.01658613, -7.13302502, -0.04401973, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 59.03183178, 0.01804998, 59.03183178, 0.05414994, 41.32228224, -859.51585118, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 14.75795794, 5.652e-05, 44.27387383, 0.00016955, 147.57957944, 0.00056518, -14.75795794, -5.652e-05, -44.27387383, -0.00016955, -147.57957944, -0.00056518, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 59.03183178, 0.01804998, 59.03183178, 0.05414994, 41.32228224, -859.51585118, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 14.75795794, 5.652e-05, 44.27387383, 0.00016955, 147.57957944, 0.00056518, -14.75795794, -5.652e-05, -44.27387383, -0.00016955, -147.57957944, -0.00056518, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 17.75, 3.5, 5.5)
    ops.node(123008, 17.75, 3.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 31336359.05442608, 13056816.27267753, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 60.85315083, 0.0008942, 72.45882703, 0.01659334, 7.2458827, 0.04410875, -60.85315083, -0.0008942, -72.45882703, -0.01659334, -7.2458827, -0.04410875, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 60.85315083, 0.0008942, 72.45882703, 0.01659334, 7.2458827, 0.04410875, -60.85315083, -0.0008942, -72.45882703, -0.01659334, -7.2458827, -0.04410875, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 59.14371391, 0.01788395, 59.14371391, 0.05365186, 41.40059974, -865.37991148, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 14.78592848, 5.653e-05, 44.35778543, 0.00016959, 147.85928478, 0.00056531, -14.78592848, -5.653e-05, -44.35778543, -0.00016959, -147.85928478, -0.00056531, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 59.14371391, 0.01788395, 59.14371391, 0.05365186, 41.40059974, -865.37991148, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 14.78592848, 5.653e-05, 44.35778543, 0.00016959, 147.85928478, 0.00056531, -14.78592848, -5.653e-05, -44.35778543, -0.00016959, -147.85928478, -0.00056531, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 7.0, 5.5)
    ops.node(123009, 0.0, 7.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 31055081.00501032, 12939617.08542097, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 59.25374557, 0.00087721, 70.57986938, 0.01973576, 7.05798694, 0.05320236, -59.25374557, -0.00087721, -70.57986938, -0.01973576, -7.05798694, -0.05320236, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 54.75591512, 0.00087721, 65.22229607, 0.01973576, 6.52222961, 0.05320236, -54.75591512, -0.00087721, -65.22229607, -0.01973576, -6.52222961, -0.05320236, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 77.89981545, 0.01754428, 77.89981545, 0.05263285, 54.52987081, -989.10512673, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 19.47495386, 7.513e-05, 58.42486159, 0.0002254, 194.74953862, 0.00075133, -19.47495386, -7.513e-05, -58.42486159, -0.0002254, -194.74953862, -0.00075133, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 77.89981545, 0.01754428, 77.89981545, 0.05263285, 54.52987081, -989.10512673, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 19.47495386, 7.513e-05, 58.42486159, 0.0002254, 194.74953862, 0.00075133, -19.47495386, -7.513e-05, -58.42486159, -0.0002254, -194.74953862, -0.00075133, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 7.45, 7.0, 5.5)
    ops.node(123010, 7.45, 7.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0625, 32103288.56730719, 13376370.236378, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 53.10141898, 0.00085675, 63.04451061, 0.01827444, 6.30445106, 0.05194438, -53.10141898, -0.00085675, -63.04451061, -0.01827444, -6.30445106, -0.05194438, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 53.10141898, 0.00085675, 63.04451061, 0.01827444, 6.30445106, 0.05194438, -53.10141898, -0.00085675, -63.04451061, -0.01827444, -6.30445106, -0.05194438, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 81.21429957, 0.01713509, 81.21429957, 0.05140526, 56.8500097, -1028.90740468, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 20.30357489, 7.577e-05, 60.91072467, 0.00022732, 203.03574891, 0.00075772, -20.30357489, -7.577e-05, -60.91072467, -0.00022732, -203.03574891, -0.00075772, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 81.21429957, 0.01713509, 81.21429957, 0.05140526, 56.8500097, -1028.90740468, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 20.30357489, 7.577e-05, 60.91072467, 0.00022732, 203.03574891, 0.00075772, -20.30357489, -7.577e-05, -60.91072467, -0.00022732, -203.03574891, -0.00075772, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 10.3, 7.0, 5.5)
    ops.node(123011, 10.3, 7.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.0625, 31514330.31366819, 13130970.96402841, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 53.15535951, 0.00086345, 63.16073456, 0.01809942, 6.31607346, 0.05062213, -53.15535951, -0.00086345, -63.16073456, -0.01809942, -6.31607346, -0.05062213, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 53.15535951, 0.00086345, 63.16073456, 0.01809942, 6.31607346, 0.05062213, -53.15535951, -0.00086345, -63.16073456, -0.01809942, -6.31607346, -0.05062213, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 79.42685136, 0.01726904, 79.42685136, 0.05180712, 55.59879595, -1024.76428869, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 19.85671284, 7.549e-05, 59.57013852, 0.00022647, 198.5671284, 0.00075489, -19.85671284, -7.549e-05, -59.57013852, -0.00022647, -198.5671284, -0.00075489, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 79.42685136, 0.01726904, 79.42685136, 0.05180712, 55.59879595, -1024.76428869, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 19.85671284, 7.549e-05, 59.57013852, 0.00022647, 198.5671284, 0.00075489, -19.85671284, -7.549e-05, -59.57013852, -0.00022647, -198.5671284, -0.00075489, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 17.75, 7.0, 5.5)
    ops.node(123012, 17.75, 7.0, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 30411888.6663686, 12671620.27765358, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 58.78419614, 0.00090906, 70.06754266, 0.01960904, 7.00675427, 0.05177042, -58.78419614, -0.00090906, -70.06754266, -0.01960904, -7.00675427, -0.05177042, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 54.50889797, 0.00090906, 64.97162136, 0.01960904, 6.49716214, 0.05177042, -54.50889797, -0.00090906, -64.97162136, -0.01960904, -6.49716214, -0.05177042, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 76.6702596, 0.01818123, 76.6702596, 0.05454369, 53.66918172, -984.66255484, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 19.1675649, 7.551e-05, 57.5026947, 0.00022653, 191.675649, 0.00075511, -19.1675649, -7.551e-05, -57.5026947, -0.00022653, -191.675649, -0.00075511, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 76.6702596, 0.01818123, 76.6702596, 0.05454369, 53.66918172, -984.66255484, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 19.1675649, 7.551e-05, 57.5026947, 0.00022653, 191.675649, 0.00075511, -19.1675649, -7.551e-05, -57.5026947, -0.00022653, -191.675649, -0.00075511, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 10.5, 5.5)
    ops.node(123013, 0.0, 10.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 31822774.57256261, 13259489.40523442, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 41.80860046, 0.00080598, 50.01136048, 0.0197935, 5.00113605, 0.06072618, -41.80860046, -0.00080598, -50.01136048, -0.0197935, -5.00113605, -0.06072618, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 41.80860046, 0.00080598, 50.01136048, 0.0197935, 5.00113605, 0.06072618, -41.80860046, -0.00080598, -50.01136048, -0.0197935, -5.00113605, -0.06072618, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 75.72722312, 0.01611951, 75.72722312, 0.04835852, 53.00905618, -871.40590929, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 18.93180578, 7.128e-05, 56.79541734, 0.00021383, 189.3180578, 0.00071275, -18.93180578, -7.128e-05, -56.79541734, -0.00021383, -189.3180578, -0.00071275, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 75.72722312, 0.01611951, 75.72722312, 0.04835852, 53.00905618, -871.40590929, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 18.93180578, 7.128e-05, 56.79541734, 0.00021383, 189.3180578, 0.00071275, -18.93180578, -7.128e-05, -56.79541734, -0.00021383, -189.3180578, -0.00071275, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 7.45, 10.5, 5.5)
    ops.node(123014, 7.45, 10.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 33068103.77205007, 13778376.57168753, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 37.06255455, 0.0007809, 44.10107208, 0.01831714, 4.41010721, 0.06432837, -37.06255455, -0.0007809, -44.10107208, -0.01831714, -4.41010721, -0.06432837, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 37.06255455, 0.0007809, 44.10107208, 0.01831714, 4.41010721, 0.06432837, -37.06255455, -0.0007809, -44.10107208, -0.01831714, -4.41010721, -0.06432837, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 84.30930161, 0.01561795, 84.30930161, 0.04685386, 59.01651113, -1001.68212659, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 21.0773254, 7.636e-05, 63.23197621, 0.00022909, 210.77325402, 0.00076365, -21.0773254, -7.636e-05, -63.23197621, -0.00022909, -210.77325402, -0.00076365, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 84.30930161, 0.01561795, 84.30930161, 0.04685386, 59.01651113, -1001.68212659, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 21.0773254, 7.636e-05, 63.23197621, 0.00022909, 210.77325402, 0.00076365, -21.0773254, -7.636e-05, -63.23197621, -0.00022909, -210.77325402, -0.00076365, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 10.3, 10.5, 5.5)
    ops.node(123015, 10.3, 10.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 31324040.71323092, 13051683.63051288, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 36.92132302, 0.00080063, 44.09023589, 0.01885179, 4.40902359, 0.06157145, -36.92132302, -0.00080063, -44.09023589, -0.01885179, -4.40902359, -0.06157145, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 36.92132302, 0.00080063, 44.09023589, 0.01885179, 4.40902359, 0.06157145, -36.92132302, -0.00080063, -44.09023589, -0.01885179, -4.40902359, -0.06157145, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 81.74070904, 0.01601259, 81.74070904, 0.04803777, 57.21849633, -1031.90419575, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 20.43517726, 7.816e-05, 61.30553178, 0.00023448, 204.3517726, 0.0007816, -20.43517726, -7.816e-05, -61.30553178, -0.00023448, -204.3517726, -0.0007816, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 81.74070904, 0.01601259, 81.74070904, 0.04803777, 57.21849633, -1031.90419575, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 20.43517726, 7.816e-05, 61.30553178, 0.00023448, 204.3517726, 0.0007816, -20.43517726, -7.816e-05, -61.30553178, -0.00023448, -204.3517726, -0.0007816, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 17.75, 10.5, 5.5)
    ops.node(123016, 17.75, 10.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 32495598.19316168, 13539832.58048403, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 40.58567129, 0.00082434, 48.47366559, 0.01941965, 4.84736656, 0.06132664, -40.58567129, -0.00082434, -48.47366559, -0.01941965, -4.84736656, -0.06132664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 40.58567129, 0.00082434, 48.47366559, 0.01941965, 4.84736656, 0.06132664, -40.58567129, -0.00082434, -48.47366559, -0.01941965, -4.84736656, -0.06132664, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 73.82612922, 0.01648673, 73.82612922, 0.0494602, 51.67829045, -843.20356195, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 18.4565323, 6.805e-05, 55.36959691, 0.00020414, 184.56532304, 0.00068047, -18.4565323, -6.805e-05, -55.36959691, -0.00020414, -184.56532304, -0.00068047, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 73.82612922, 0.01648673, 73.82612922, 0.0494602, 51.67829045, -843.20356195, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 18.4565323, 6.805e-05, 55.36959691, 0.00020414, 184.56532304, 0.00068047, -18.4565323, -6.805e-05, -55.36959691, -0.00020414, -184.56532304, -0.00068047, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.1)
    ops.node(124001, 0.0, 0.0, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 30942893.27039208, 12892872.1959967, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 28.79210068, 0.00074759, 34.79689592, 0.02243335, 3.47968959, 0.07346651, -28.79210068, -0.00074759, -34.79689592, -0.02243335, -3.47968959, -0.07346651, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 28.79210068, 0.00074759, 34.79689592, 0.02243335, 3.47968959, 0.07346651, -28.79210068, -0.00074759, -34.79689592, -0.02243335, -3.47968959, -0.07346651, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 62.45265347, 0.01495187, 62.45265347, 0.04485561, 43.71685743, -800.21439688, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 15.61316337, 6.045e-05, 46.8394901, 0.00018136, 156.13163368, 0.00060453, -15.61316337, -6.045e-05, -46.8394901, -0.00018136, -156.13163368, -0.00060453, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 62.45265347, 0.01495187, 62.45265347, 0.04485561, 43.71685743, -800.21439688, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 15.61316337, 6.045e-05, 46.8394901, 0.00018136, 156.13163368, 0.00060453, -15.61316337, -6.045e-05, -46.8394901, -0.00018136, -156.13163368, -0.00060453, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 7.45, 0.0, 8.1)
    ops.node(124002, 7.45, 0.0, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 31483339.01953378, 13118057.92480574, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 22.17509062, 0.00070831, 26.72503372, 0.02093294, 2.67250337, 0.07798326, -22.17509062, -0.00070831, -26.72503372, -0.02093294, -2.67250337, -0.07798326, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 22.17509062, 0.00070831, 26.72503372, 0.02093294, 2.67250337, 0.07798326, -22.17509062, -0.00070831, -26.72503372, -0.02093294, -2.67250337, -0.07798326, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 69.19321061, 0.01416624, 69.19321061, 0.04249872, 48.43524743, -907.76857471, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 17.29830265, 6.583e-05, 51.89490796, 0.00019748, 172.98302653, 0.00065828, -17.29830265, -6.583e-05, -51.89490796, -0.00019748, -172.98302653, -0.00065828, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 69.19321061, 0.01416624, 69.19321061, 0.04249872, 48.43524743, -907.76857471, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 17.29830265, 6.583e-05, 51.89490796, 0.00019748, 172.98302653, 0.00065828, -17.29830265, -6.583e-05, -51.89490796, -0.00019748, -172.98302653, -0.00065828, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 10.3, 0.0, 8.1)
    ops.node(124003, 10.3, 0.0, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0625, 31152873.39708161, 12980363.91545067, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 21.63138669, 0.00072447, 26.09283873, 0.02132601, 2.60928387, 0.07805063, -21.63138669, -0.00072447, -26.09283873, -0.02132601, -2.60928387, -0.07805063, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 21.63138669, 0.00072447, 26.09283873, 0.02132601, 2.60928387, 0.07805063, -21.63138669, -0.00072447, -26.09283873, -0.02132601, -2.60928387, -0.07805063, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 69.24795933, 0.01448946, 69.24795933, 0.04346837, 48.47357153, -937.26430849, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 17.31198983, 6.658e-05, 51.9359695, 0.00019974, 173.11989833, 0.00066579, -17.31198983, -6.658e-05, -51.9359695, -0.00019974, -173.11989833, -0.00066579, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 69.24795933, 0.01448946, 69.24795933, 0.04346837, 48.47357153, -937.26430849, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 17.31198983, 6.658e-05, 51.9359695, 0.00019974, 173.11989833, 0.00066579, -17.31198983, -6.658e-05, -51.9359695, -0.00019974, -173.11989833, -0.00066579, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 17.75, 0.0, 8.1)
    ops.node(124004, 17.75, 0.0, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 31174754.26200213, 12989480.94250089, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 28.60107482, 0.00074074, 34.54409769, 0.0222906, 3.45440977, 0.07348537, -28.60107482, -0.00074074, -34.54409769, -0.0222906, -3.45440977, -0.07348537, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 28.60107482, 0.00074074, 34.54409769, 0.0222906, 3.45440977, 0.07348537, -28.60107482, -0.00074074, -34.54409769, -0.0222906, -3.45440977, -0.07348537, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 62.21454362, 0.01481486, 62.21454362, 0.04444458, 43.55018053, -796.58634826, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 15.5536359, 5.977e-05, 46.66090771, 0.00017932, 155.53635905, 0.00059774, -15.5536359, -5.977e-05, -46.66090771, -0.00017932, -155.53635905, -0.00059774, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 62.21454362, 0.01481486, 62.21454362, 0.04444458, 43.55018053, -796.58634826, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 15.5536359, 5.977e-05, 46.66090771, 0.00017932, 155.53635905, 0.00059774, -15.5536359, -5.977e-05, -46.66090771, -0.00017932, -155.53635905, -0.00059774, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 3.5, 8.1)
    ops.node(124005, 0.0, 3.5, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 32047012.6643503, 13352921.94347929, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 44.84745925, 0.00081343, 53.86599906, 0.01897773, 5.38659991, 0.05723625, -44.84745925, -0.00081343, -53.86599906, -0.01897773, -5.38659991, -0.05723625, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 44.84745925, 0.00081343, 53.86599906, 0.01897773, 5.38659991, 0.05723625, -44.84745925, -0.00081343, -53.86599906, -0.01897773, -5.38659991, -0.05723625, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 48.20120818, 0.01626869, 48.20120818, 0.04880606, 33.74084573, -591.61487214, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 12.05030204, 4.505e-05, 36.15090613, 0.00013515, 120.50302045, 0.0004505, -12.05030204, -4.505e-05, -36.15090613, -0.00013515, -120.50302045, -0.0004505, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 48.20120818, 0.01626869, 48.20120818, 0.04880606, 33.74084573, -591.61487214, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 12.05030204, 4.505e-05, 36.15090613, 0.00013515, 120.50302045, 0.0004505, -12.05030204, -4.505e-05, -36.15090613, -0.00013515, -120.50302045, -0.0004505, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 17.75, 3.5, 8.1)
    ops.node(124008, 17.75, 3.5, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 31408112.04309945, 13086713.35129144, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 45.06979551, 0.00081344, 54.22345317, 0.01953815, 5.42234532, 0.05725688, -45.06979551, -0.00081344, -54.22345317, -0.01953815, -5.42234532, -0.05725688, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 45.06979551, 0.00081344, 54.22345317, 0.01953815, 5.42234532, 0.05725688, -45.06979551, -0.00081344, -54.22345317, -0.01953815, -5.42234532, -0.05725688, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 46.93599402, 0.01626877, 46.93599402, 0.04880631, 32.85519582, -606.90214303, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 11.73399851, 4.476e-05, 35.20199552, 0.00013428, 117.33998506, 0.0004476, -11.73399851, -4.476e-05, -35.20199552, -0.00013428, -117.33998506, -0.0004476, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 46.93599402, 0.01626877, 46.93599402, 0.04880631, 32.85519582, -606.90214303, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 11.73399851, 4.476e-05, 35.20199552, 0.00013428, 117.33998506, 0.0004476, -11.73399851, -4.476e-05, -35.20199552, -0.00013428, -117.33998506, -0.0004476, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 7.0, 8.1)
    ops.node(124009, 0.0, 7.0, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 32945460.92006255, 13727275.3833594, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 43.2994235, 0.00077846, 51.8723528, 0.0230573, 5.18723528, 0.07121539, -43.2994235, -0.00077846, -51.8723528, -0.0230573, -5.18723528, -0.07121539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 39.41312763, 0.00077846, 47.21660235, 0.0230573, 4.72166024, 0.07121539, -39.41312763, -0.00077846, -47.21660235, -0.0230573, -4.72166024, -0.07121539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 70.66382121, 0.01556918, 70.66382121, 0.04670753, 49.46467485, -769.47767042, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 17.6659553, 6.424e-05, 52.99786591, 0.00019273, 176.65955302, 0.00064243, -17.6659553, -6.424e-05, -52.99786591, -0.00019273, -176.65955302, -0.00064243, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 70.66382121, 0.01556918, 70.66382121, 0.04670753, 49.46467485, -769.47767042, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 17.6659553, 6.424e-05, 52.99786591, 0.00019273, 176.65955302, 0.00064243, -17.6659553, -6.424e-05, -52.99786591, -0.00019273, -176.65955302, -0.00064243, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 7.45, 7.0, 8.1)
    ops.node(124010, 7.45, 7.0, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0625, 31428542.7167109, 13095226.13196287, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 36.32874208, 0.0007815, 43.64040682, 0.0216221, 4.36404068, 0.06626706, -36.32874208, -0.0007815, -43.64040682, -0.0216221, -4.36404068, -0.06626706, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 36.32874208, 0.0007815, 43.64040682, 0.0216221, 4.36404068, 0.06626706, -36.32874208, -0.0007815, -43.64040682, -0.0216221, -4.36404068, -0.06626706, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 69.10214619, 0.01563003, 69.10214619, 0.0468901, 48.37150233, -783.1187305, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 17.27553655, 6.586e-05, 51.82660964, 0.00019757, 172.75536547, 0.00065856, -17.27553655, -6.586e-05, -51.82660964, -0.00019757, -172.75536547, -0.00065856, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 69.10214619, 0.01563003, 69.10214619, 0.0468901, 48.37150233, -783.1187305, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 17.27553655, 6.586e-05, 51.82660964, 0.00019757, 172.75536547, 0.00065856, -17.27553655, -6.586e-05, -51.82660964, -0.00019757, -172.75536547, -0.00065856, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 10.3, 7.0, 8.1)
    ops.node(124011, 10.3, 7.0, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.0625, 30043662.11403469, 12518192.54751446, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 36.13646929, 0.00079692, 43.53517981, 0.02168047, 4.35351798, 0.06446652, -36.13646929, -0.00079692, -43.53517981, -0.02168047, -4.35351798, -0.06446652, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 36.13646929, 0.00079692, 43.53517981, 0.02168047, 4.35351798, 0.06446652, -36.13646929, -0.00079692, -43.53517981, -0.02168047, -4.35351798, -0.06446652, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 66.03541116, 0.01593838, 66.03541116, 0.04781515, 46.22478781, -781.1252515, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 16.50885279, 6.583e-05, 49.52655837, 0.0001975, 165.0885279, 0.00065834, -16.50885279, -6.583e-05, -49.52655837, -0.0001975, -165.0885279, -0.00065834, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 66.03541116, 0.01593838, 66.03541116, 0.04781515, 46.22478781, -781.1252515, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 16.50885279, 6.583e-05, 49.52655837, 0.0001975, 165.0885279, 0.00065834, -16.50885279, -6.583e-05, -49.52655837, -0.0001975, -165.0885279, -0.00065834, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 17.75, 7.0, 8.1)
    ops.node(124012, 17.75, 7.0, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 31004692.3099101, 12918621.79579588, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 43.00133907, 0.0007819, 51.78561653, 0.0236055, 5.17856165, 0.06978899, -43.00133907, -0.0007819, -51.78561653, -0.0236055, -5.17856165, -0.06978899, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 39.04310861, 0.0007819, 47.01880207, 0.0236055, 4.70188021, 0.06978899, -39.04310861, -0.0007819, -47.01880207, -0.0236055, -4.70188021, -0.06978899, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 67.16127942, 0.01563792, 67.16127942, 0.04691375, 47.0128956, -782.17970572, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 16.79031986, 6.488e-05, 50.37095957, 0.00019464, 167.90319856, 0.00064881, -16.79031986, -6.488e-05, -50.37095957, -0.00019464, -167.90319856, -0.00064881, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 67.16127942, 0.01563792, 67.16127942, 0.04691375, 47.0128956, -782.17970572, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 16.79031986, 6.488e-05, 50.37095957, 0.00019464, 167.90319856, 0.00064881, -16.79031986, -6.488e-05, -50.37095957, -0.00019464, -167.90319856, -0.00064881, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 10.5, 8.1)
    ops.node(124013, 0.0, 10.5, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 32316821.6758344, 13465342.364931, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 28.08207294, 0.00073551, 33.80331981, 0.02158804, 3.38033198, 0.07351408, -28.08207294, -0.00073551, -33.80331981, -0.02158804, -3.38033198, -0.07351408, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 28.08207294, 0.00073551, 33.80331981, 0.02158804, 3.38033198, 0.07351408, -28.08207294, -0.00073551, -33.80331981, -0.02158804, -3.38033198, -0.07351408, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 61.67433951, 0.01471023, 61.67433951, 0.04413068, 43.17203766, -754.67438022, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 15.41858488, 5.716e-05, 46.25575463, 0.00017148, 154.18584878, 0.00057161, -15.41858488, -5.716e-05, -46.25575463, -0.00017148, -154.18584878, -0.00057161, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 61.67433951, 0.01471023, 61.67433951, 0.04413068, 43.17203766, -754.67438022, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 15.41858488, 5.716e-05, 46.25575463, 0.00017148, 154.18584878, 0.00057161, -15.41858488, -5.716e-05, -46.25575463, -0.00017148, -154.18584878, -0.00057161, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 7.45, 10.5, 8.1)
    ops.node(124014, 7.45, 10.5, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 31101968.76518072, 12959153.65215863, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 21.89425267, 0.00071224, 26.41343597, 0.02145561, 2.6413436, 0.07812889, -21.89425267, -0.00071224, -26.41343597, -0.02145561, -2.6413436, -0.07812889, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 21.89425267, 0.00071224, 26.41343597, 0.02145561, 2.6413436, 0.07812889, -21.89425267, -0.00071224, -26.41343597, -0.02145561, -2.6413436, -0.07812889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 68.83599161, 0.01424477, 68.83599161, 0.0427343, 48.18519413, -923.89934303, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 17.2089979, 6.629e-05, 51.62699371, 0.00019887, 172.08997903, 0.00066291, -17.2089979, -6.629e-05, -51.62699371, -0.00019887, -172.08997903, -0.00066291, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 68.83599161, 0.01424477, 68.83599161, 0.0427343, 48.18519413, -923.89934303, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 17.2089979, 6.629e-05, 51.62699371, 0.00019887, 172.08997903, 0.00066291, -17.2089979, -6.629e-05, -51.62699371, -0.00019887, -172.08997903, -0.00066291, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 10.3, 10.5, 8.1)
    ops.node(124015, 10.3, 10.5, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 29567543.18400541, 12319809.66000226, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 21.63425276, 0.000723, 26.19428987, 0.02141957, 2.61942899, 0.07638507, -21.63425276, -0.000723, -26.19428987, -0.02141957, -2.61942899, -0.07638507, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 21.63425276, 0.000723, 26.19428987, 0.02141957, 2.61942899, 0.07638507, -21.63425276, -0.000723, -26.19428987, -0.02141957, -2.61942899, -0.07638507, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 65.53171506, 0.01445995, 65.53171506, 0.04337984, 45.87220054, -907.54770525, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 16.38292876, 6.638e-05, 49.14878629, 0.00019915, 163.82928764, 0.00066384, -16.38292876, -6.638e-05, -49.14878629, -0.00019915, -163.82928764, -0.00066384, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 65.53171506, 0.01445995, 65.53171506, 0.04337984, 45.87220054, -907.54770525, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 16.38292876, 6.638e-05, 49.14878629, 0.00019915, 163.82928764, 0.00066384, -16.38292876, -6.638e-05, -49.14878629, -0.00019915, -163.82928764, -0.00066384, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 17.75, 10.5, 8.1)
    ops.node(124016, 17.75, 10.5, 10.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 30688354.94502965, 12786814.56042902, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 28.79680214, 0.00074931, 34.82618122, 0.0224073, 3.48261812, 0.0732575, -28.79680214, -0.00074931, -34.82618122, -0.0224073, -3.48261812, -0.0732575, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 28.79680214, 0.00074931, 34.82618122, 0.0224073, 3.48261812, 0.0732575, -28.79680214, -0.00074931, -34.82618122, -0.0224073, -3.48261812, -0.0732575, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 61.47500417, 0.01498618, 61.47500417, 0.04495853, 43.03250292, -796.89566466, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 15.36875104, 6e-05, 46.10625313, 0.00018, 153.68751042, 0.0006, -15.36875104, -6e-05, -46.10625313, -0.00018, -153.68751042, -0.0006, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 61.47500417, 0.01498618, 61.47500417, 0.04495853, 43.03250292, -796.89566466, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 15.36875104, 6e-05, 46.10625313, 0.00018, 153.68751042, 0.0006, -15.36875104, -6e-05, -46.10625313, -0.00018, -153.68751042, -0.0006, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 7.45, 3.5, 0.0)
    ops.node(124017, 7.45, 3.5, 1.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 170006, 124017, 0.1225, 29948019.45604256, 12478341.44001773, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 172.93642221, 0.00056812, 205.50950536, 0.04264306, 20.55095054, 0.11923428, -172.93642221, -0.00056812, -205.50950536, -0.04264306, -20.55095054, -0.11923428, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 172.93642221, 0.00056812, 205.50950536, 0.03661251, 20.55095054, 0.08967746, -172.93642221, -0.00056812, -205.50950536, -0.03661251, -20.55095054, -0.08967746, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 288.80171865, 0.01136231, 288.80171865, 0.03408694, 202.16120306, -6698.49568623, 0.05, 2, 0, 70006, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 72.20042966, 7.368e-05, 216.60128899, 0.00022105, 722.00429663, 0.00073684, -72.20042966, -7.368e-05, -216.60128899, -0.00022105, -722.00429663, -0.00073684, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 333.42925258, 0.01136231, 333.42925258, 0.03408694, 233.40047681, -9594.88944405, 0.05, 2, 0, 70006, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 83.35731315, 8.507e-05, 250.07193944, 0.00025521, 833.57313146, 0.0008507, -83.35731315, -8.507e-05, -250.07193944, -0.00025521, -833.57313146, -0.0008507, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 7.45, 3.5, 1.5)
    ops.node(121006, 7.45, 3.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 174017, 121006, 0.1225, 33767245.88513639, 14069685.7854735, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 151.7856357, 0.00055889, 179.60082118, 0.04710198, 17.96008212, 0.14710198, -151.7856357, -0.00055889, -179.60082118, -0.04710198, -17.96008212, -0.14710198, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 136.66237331, 0.00055889, 161.70617435, 0.03615177, 16.17061744, 0.10486719, -136.66237331, -0.00055889, -161.70617435, -0.03615177, -16.17061744, -0.10486719, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 312.69663873, 0.01117779, 312.69663873, 0.03353336, 218.88764711, -6551.33829732, 0.05, 2, 0, 74017, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 78.17415968, 7.076e-05, 234.52247905, 0.00021227, 781.74159682, 0.00070757, -78.17415968, -7.076e-05, -234.52247905, -0.00021227, -781.74159682, -0.00070757, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 400.4707402, 0.01117779, 400.4707402, 0.03353336, 280.32951814, -12840.85826973, 0.05, 2, 0, 74017, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 100.11768505, 9.062e-05, 300.35305515, 0.00027185, 1001.17685049, 0.00090618, -100.11768505, -9.062e-05, -300.35305515, -0.00027185, -1001.17685049, -0.00090618, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 10.3, 3.5, 0.0)
    ops.node(124018, 10.3, 3.5, 1.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 170007, 124018, 0.1225, 33150804.88457468, 13812835.36857278, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 174.94821282, 0.00055278, 207.1380154, 0.04408279, 20.71380154, 0.13831912, -174.94821282, -0.00055278, -207.1380154, -0.04408279, -20.71380154, -0.13831912, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 174.94821282, 0.00055278, 207.1380154, 0.03784368, 20.71380154, 0.10313376, -174.94821282, -0.00055278, -207.1380154, -0.03784368, -20.71380154, -0.10313376, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 310.25075172, 0.01105556, 310.25075172, 0.03316669, 217.1755262, -6559.64354954, 0.05, 2, 0, 70007, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 77.56268793, 7.151e-05, 232.68806379, 0.00021453, 775.6268793, 0.00071509, -77.56268793, -7.151e-05, -232.68806379, -0.00021453, -775.6268793, -0.00071509, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 353.69714394, 0.01105556, 353.69714394, 0.03316669, 247.58800076, -9345.94714652, 0.05, 2, 0, 70007, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 88.42428598, 8.152e-05, 265.27285795, 0.00024457, 884.24285984, 0.00081522, -88.42428598, -8.152e-05, -265.27285795, -0.00024457, -884.24285984, -0.00081522, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 10.3, 3.5, 1.5)
    ops.node(121007, 10.3, 3.5, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4044, 174018, 121007, 0.1225, 32125868.56503624, 13385778.5687651, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24044, 152.82464422, 0.00055182, 181.41205963, 0.04710394, 18.14120596, 0.14710394, -152.82464422, -0.00055182, -181.41205963, -0.04710394, -18.14120596, -0.14710394, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14044, 136.19619383, 0.00055182, 161.67308724, 0.03615161, 16.16730872, 0.09934998, -136.19619383, -0.00055182, -161.67308724, -0.03615161, -16.16730872, -0.09934998, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24044, 4044, 0.0, 301.32350572, 0.01103642, 301.32350572, 0.03310927, 210.926454, -6608.6220193, 0.05, 2, 0, 74018, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 44044, 75.33087643, 7.167e-05, 225.99262929, 0.000215, 753.30876429, 0.00071667, -75.33087643, -7.167e-05, -225.99262929, -0.000215, -753.30876429, -0.00071667, 0.4, 0.3, 0.003, 0.0, 0.0, 24044, 2)
    ops.limitCurve('ThreePoint', 14044, 4044, 0.0, 390.05483968, 0.01103642, 390.05483968, 0.03310927, 273.03838778, -13001.40376727, 0.05, 2, 0, 74018, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 34044, 97.51370992, 9.277e-05, 292.54112976, 0.00027831, 975.13709921, 0.00092771, -97.51370992, -9.277e-05, -292.54112976, -0.00027831, -975.13709921, -0.00092771, 0.4, 0.3, 0.003, 0.0, 0.0, 14044, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4044, 99999, 'P', 44044, 'Vy', 34044, 'Vz', 24044, 'My', 14044, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4044, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 4044, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 7.45, 3.5, 2.9)
    ops.node(124019, 7.45, 3.5, 3.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 171006, 124019, 0.1225, 31567460.13475573, 13153108.38948155, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 110.94546936, 0.00053349, 132.34799332, 0.03665797, 13.23479933, 0.10581899, -110.94546936, -0.00053349, -132.34799332, -0.03665797, -13.23479933, -0.10581899, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 107.0201837, 0.00053349, 127.66547962, 0.03665797, 12.76654796, 0.10581899, -107.0201837, -0.00053349, -127.66547962, -0.03665797, -12.76654796, -0.10581899, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 282.47460198, 0.01066971, 282.47460198, 0.03200913, 197.73222139, -6423.42759193, 0.05, 2, 0, 71006, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 70.61865049, 6.837e-05, 211.85595148, 0.00020512, 706.18650495, 0.00068372, -70.61865049, -6.837e-05, -211.85595148, -0.00020512, -706.18650495, -0.00068372, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 282.47460198, 0.01066971, 282.47460198, 0.03200913, 197.73222139, -6423.42759193, 0.05, 2, 0, 71006, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 70.61865049, 6.837e-05, 211.85595148, 0.00020512, 706.18650495, 0.00068372, -70.61865049, -6.837e-05, -211.85595148, -0.00020512, -706.18650495, -0.00068372, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 7.45, 3.5, 4.05)
    ops.node(122006, 7.45, 3.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 122006, 0.1225, 32010235.18021073, 13337597.99175447, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 116.39606559, 0.00053299, 138.85045432, 0.03748004, 13.88504543, 0.10979565, -116.39606559, -0.00053299, -138.85045432, -0.03748004, -13.88504543, -0.10979565, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 108.49117839, 0.00053299, 129.42060655, 0.03748004, 12.94206066, 0.10979565, -108.49117839, -0.00053299, -129.42060655, -0.03748004, -12.94206066, -0.10979565, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 281.06640425, 0.01065974, 281.06640425, 0.03197921, 196.74648297, -6310.23345837, 0.05, 2, 0, 74019, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 70.26660106, 6.709e-05, 210.79980319, 0.00020127, 702.66601062, 0.0006709, -70.26660106, -6.709e-05, -210.79980319, -0.00020127, -702.66601062, -0.0006709, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 281.06640425, 0.01065974, 281.06640425, 0.03197921, 196.74648297, -6310.23345837, 0.05, 2, 0, 74019, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 70.26660106, 6.709e-05, 210.79980319, 0.00020127, 702.66601062, 0.0006709, -70.26660106, -6.709e-05, -210.79980319, -0.00020127, -702.66601062, -0.0006709, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 10.3, 3.5, 2.9)
    ops.node(124020, 10.3, 3.5, 3.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 171007, 124020, 0.1225, 30437284.81080484, 12682202.00450202, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 111.69310472, 0.00053364, 133.45537669, 0.03637684, 13.34553767, 0.1015741, -111.69310472, -0.00053364, -133.45537669, -0.03637684, -13.34553767, -0.1015741, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 107.50076016, 0.00053364, 128.4461962, 0.03637684, 12.84461962, 0.1015741, -107.50076016, -0.00053364, -128.4461962, -0.03637684, -12.84461962, -0.1015741, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 275.41492794, 0.01067287, 275.41492794, 0.03201862, 192.79044956, -6485.85527236, 0.05, 2, 0, 71007, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 68.85373198, 6.914e-05, 206.56119595, 0.00020742, 688.53731985, 0.00069139, -68.85373198, -6.914e-05, -206.56119595, -0.00020742, -688.53731985, -0.00069139, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 275.41492794, 0.01067287, 275.41492794, 0.03201862, 192.79044956, -6485.85527236, 0.05, 2, 0, 71007, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 68.85373198, 6.914e-05, 206.56119595, 0.00020742, 688.53731985, 0.00069139, -68.85373198, -6.914e-05, -206.56119595, -0.00020742, -688.53731985, -0.00069139, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 10.3, 3.5, 4.05)
    ops.node(122007, 10.3, 3.5, 4.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 122007, 0.1225, 30816431.0851094, 12840179.61879558, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 118.49239176, 0.00053147, 141.64123141, 0.03749267, 14.16412314, 0.10589278, -118.49239176, -0.00053147, -141.64123141, -0.03749267, -14.16412314, -0.10589278, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 109.73964022, 0.00053147, 131.17853007, 0.03749267, 13.11785301, 0.10589278, -109.73964022, -0.00053147, -131.17853007, -0.03749267, -13.11785301, -0.10589278, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 274.14429903, 0.01062932, 274.14429903, 0.03188797, 191.90100932, -6413.29730158, 0.05, 2, 0, 74020, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 68.53607476, 6.797e-05, 205.60822427, 0.00020392, 685.36074758, 0.00067973, -68.53607476, -6.797e-05, -205.60822427, -0.00020392, -685.36074758, -0.00067973, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 274.14429903, 0.01062932, 274.14429903, 0.03188797, 191.90100932, -6413.29730158, 0.05, 2, 0, 74020, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 68.53607476, 6.797e-05, 205.60822427, 0.00020392, 685.36074758, 0.00067973, -68.53607476, -6.797e-05, -205.60822427, -0.00020392, -685.36074758, -0.00067973, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 7.45, 3.5, 5.5)
    ops.node(124021, 7.45, 3.5, 6.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 172006, 124021, 0.0625, 31380797.09414742, 13075332.12256142, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 53.66711672, 0.00065383, 63.71257621, 0.01994692, 6.37125762, 0.05601026, -53.66711672, -0.00065383, -63.71257621, -0.01994692, -6.37125762, -0.05601026, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 53.66711672, 0.00065383, 63.71257621, 0.01994692, 6.37125762, 0.05601026, -53.66711672, -0.00065383, -63.71257621, -0.01994692, -6.37125762, -0.05601026, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 101.69187184, 0.01307667, 101.69187184, 0.03923002, 71.18431029, -2317.90476444, 0.05, 2, 0, 72006, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 25.42296796, 4.853e-05, 76.26890388, 0.00014559, 254.22967961, 0.00048531, -25.42296796, -4.853e-05, -76.26890388, -0.00014559, -254.22967961, -0.00048531, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 101.69187184, 0.01307667, 101.69187184, 0.03923002, 71.18431029, -2317.90476444, 0.05, 2, 0, 72006, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 25.42296796, 4.853e-05, 76.26890388, 0.00014559, 254.22967961, 0.00048531, -25.42296796, -4.853e-05, -76.26890388, -0.00014559, -254.22967961, -0.00048531, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 7.45, 3.5, 6.65)
    ops.node(123006, 7.45, 3.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 123006, 0.0625, 30980573.51540961, 12908572.29808734, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 51.51335457, 0.00062861, 61.29648078, 0.02068372, 6.12964808, 0.05784865, -51.51335457, -0.00062861, -61.29648078, -0.02068372, -6.12964808, -0.05784865, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 51.51335457, 0.00062861, 61.29648078, 0.02068372, 6.12964808, 0.05784865, -51.51335457, -0.00062861, -61.29648078, -0.02068372, -6.12964808, -0.05784865, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 98.19976862, 0.01257221, 98.19976862, 0.03771663, 68.73983803, -2216.0745936, 0.05, 2, 0, 74021, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 24.54994215, 4.747e-05, 73.64982646, 0.00014241, 245.49942155, 0.0004747, -24.54994215, -4.747e-05, -73.64982646, -0.00014241, -245.49942155, -0.0004747, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 98.19976862, 0.01257221, 98.19976862, 0.03771663, 68.73983803, -2216.0745936, 0.05, 2, 0, 74021, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 24.54994215, 4.747e-05, 73.64982646, 0.00014241, 245.49942155, 0.0004747, -24.54994215, -4.747e-05, -73.64982646, -0.00014241, -245.49942155, -0.0004747, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 10.3, 3.5, 5.5)
    ops.node(124022, 10.3, 3.5, 6.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 172007, 124022, 0.0625, 29777018.84654119, 12407091.18605883, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 54.08540171, 0.00065641, 64.27195732, 0.01977333, 6.42719573, 0.05181621, -54.08540171, -0.00065641, -64.27195732, -0.01977333, -6.42719573, -0.05181621, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 54.08540171, 0.00065641, 64.27195732, 0.01977333, 6.42719573, 0.05181621, -54.08540171, -0.00065641, -64.27195732, -0.01977333, -6.42719573, -0.05181621, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 97.94041158, 0.01312823, 97.94041158, 0.0393847, 68.55828811, -2344.40053141, 0.05, 2, 0, 72007, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 24.4851029, 4.926e-05, 73.45530869, 0.00014777, 244.85102896, 0.00049258, -24.4851029, -4.926e-05, -73.45530869, -0.00014777, -244.85102896, -0.00049258, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 97.94041158, 0.01312823, 97.94041158, 0.0393847, 68.55828811, -2344.40053141, 0.05, 2, 0, 72007, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 24.4851029, 4.926e-05, 73.45530869, 0.00014777, 244.85102896, 0.00049258, -24.4851029, -4.926e-05, -73.45530869, -0.00014777, -244.85102896, -0.00049258, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 10.3, 3.5, 6.65)
    ops.node(123007, 10.3, 3.5, 7.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 123007, 0.0625, 33384676.62131044, 13910281.92554602, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 50.4943498, 0.00064667, 59.84423248, 0.02073623, 5.98442325, 0.06305107, -50.4943498, -0.00064667, -59.84423248, -0.02073623, -5.98442325, -0.06305107, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 50.4943498, 0.00064667, 59.84423248, 0.02073623, 5.98442325, 0.06305107, -50.4943498, -0.00064667, -59.84423248, -0.02073623, -5.98442325, -0.06305107, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 104.75713708, 0.01293331, 104.75713708, 0.03879992, 73.32999596, -2220.36551761, 0.05, 2, 0, 74022, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 26.18928427, 4.699e-05, 78.56785281, 0.00014098, 261.8928427, 0.00046993, -26.18928427, -4.699e-05, -78.56785281, -0.00014098, -261.8928427, -0.00046993, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 104.75713708, 0.01293331, 104.75713708, 0.03879992, 73.32999596, -2220.36551761, 0.05, 2, 0, 74022, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 26.18928427, 4.699e-05, 78.56785281, 0.00014098, 261.8928427, 0.00046993, -26.18928427, -4.699e-05, -78.56785281, -0.00014098, -261.8928427, -0.00046993, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 7.45, 3.5, 8.1)
    ops.node(124023, 7.45, 3.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 173006, 124023, 0.0625, 31185685.79842636, 12994035.74934432, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 35.85728752, 0.00060451, 43.07521228, 0.02035711, 4.30752123, 0.06399701, -35.85728752, -0.00060451, -43.07521228, -0.02035711, -4.30752123, -0.06399701, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 35.85728752, 0.00060451, 43.07521228, 0.02035711, 4.30752123, 0.06399701, -35.85728752, -0.00060451, -43.07521228, -0.02035711, -4.30752123, -0.06399701, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 79.96128581, 0.01209015, 79.96128581, 0.03627045, 55.97290007, -1576.90076303, 0.05, 2, 0, 73006, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 19.99032145, 3.84e-05, 59.97096436, 0.0001152, 199.90321453, 0.00038399, -19.99032145, -3.84e-05, -59.97096436, -0.0001152, -199.90321453, -0.00038399, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 79.96128581, 0.01209015, 79.96128581, 0.03627045, 55.97290007, -1576.90076303, 0.05, 2, 0, 73006, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 19.99032145, 3.84e-05, 59.97096436, 0.0001152, 199.90321453, 0.00038399, -19.99032145, -3.84e-05, -59.97096436, -0.0001152, -199.90321453, -0.00038399, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 7.45, 3.5, 9.25)
    ops.node(124006, 7.45, 3.5, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 124006, 0.0625, 31333445.74991001, 13055602.39579584, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 33.52300457, 0.00059641, 40.33213817, 0.02089279, 4.03321382, 0.06720673, -33.52300457, -0.00059641, -40.33213817, -0.02089279, -4.03321382, -0.06720673, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 33.52300457, 0.00059641, 40.33213817, 0.02089279, 4.03321382, 0.06720673, -33.52300457, -0.00059641, -40.33213817, -0.02089279, -4.03321382, -0.06720673, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 77.94463219, 0.01192828, 77.94463219, 0.03578485, 54.56124253, -1533.99574173, 0.05, 2, 0, 74023, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 19.48615805, 3.725e-05, 58.45847414, 0.00011176, 194.86158047, 0.00037254, -19.48615805, -3.725e-05, -58.45847414, -0.00011176, -194.86158047, -0.00037254, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 77.94463219, 0.01192828, 77.94463219, 0.03578485, 54.56124253, -1533.99574173, 0.05, 2, 0, 74023, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 19.48615805, 3.725e-05, 58.45847414, 0.00011176, 194.86158047, 0.00037254, -19.48615805, -3.725e-05, -58.45847414, -0.00011176, -194.86158047, -0.00037254, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 10.3, 3.5, 8.1)
    ops.node(124024, 10.3, 3.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 173007, 124024, 0.0625, 30896740.23048757, 12873641.76270315, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 36.61430118, 0.00059546, 44.01190965, 0.0200581, 4.40119097, 0.06330758, -36.61430118, -0.00059546, -44.01190965, -0.0200581, -4.40119097, -0.06330758, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 36.61430118, 0.00059546, 44.01190965, 0.0200581, 4.40119097, 0.06330758, -36.61430118, -0.00059546, -44.01190965, -0.0200581, -4.40119097, -0.06330758, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 77.7259754, 0.01190927, 77.7259754, 0.03572782, 54.40818278, -1558.75265199, 0.05, 2, 0, 73007, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 19.43149385, 3.767e-05, 58.29448155, 0.00011302, 194.3149385, 0.00037675, -19.43149385, -3.767e-05, -58.29448155, -0.00011302, -194.3149385, -0.00037675, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 77.7259754, 0.01190927, 77.7259754, 0.03572782, 54.40818278, -1558.75265199, 0.05, 2, 0, 73007, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 19.43149385, 3.767e-05, 58.29448155, 0.00011302, 194.3149385, 0.00037675, -19.43149385, -3.767e-05, -58.29448155, -0.00011302, -194.3149385, -0.00037675, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 10.3, 3.5, 9.25)
    ops.node(124007, 10.3, 3.5, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 124007, 0.0625, 30724527.35772214, 12801886.39905089, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 33.71610443, 0.00058201, 40.62248317, 0.0213038, 4.06224832, 0.06691648, -33.71610443, -0.00058201, -40.62248317, -0.0213038, -4.06224832, -0.06691648, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 33.71610443, 0.00058201, 40.62248317, 0.0213038, 4.06224832, 0.06691648, -33.71610443, -0.00058201, -40.62248317, -0.0213038, -4.06224832, -0.06691648, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 77.96683834, 0.0116403, 77.96683834, 0.03492089, 54.57678684, -1560.12752914, 0.05, 2, 0, 74024, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 19.49170958, 3.8e-05, 58.47512875, 0.00011401, 194.91709585, 0.00038003, -19.49170958, -3.8e-05, -58.47512875, -0.00011401, -194.91709585, -0.00038003, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 77.96683834, 0.0116403, 77.96683834, 0.03492089, 54.57678684, -1560.12752914, 0.05, 2, 0, 74024, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 19.49170958, 3.8e-05, 58.47512875, 0.00011401, 194.91709585, 0.00038003, -19.49170958, -3.8e-05, -58.47512875, -0.00011401, -194.91709585, -0.00038003, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 4059, '-orient', 0, 0, 1, 0, 1, 0)
