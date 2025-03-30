import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 9.6, 0.0, 0.0)
    ops.node(121003, 9.6, 0.0, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.16, 26164800.56154356, 10902000.23397648, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 177.16660515, 0.0006556, 211.05967753, 0.01414565, 21.10596775, 0.03262167, -177.16660515, -0.0006556, -211.05967753, -0.01414565, -21.10596775, -0.03262167, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 192.56584807, 0.0006556, 229.40489132, 0.01414565, 22.94048913, 0.03262167, -192.56584807, -0.0006556, -229.40489132, -0.01414565, -22.94048913, -0.03262167, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 162.27831291, 0.0131119, 162.27831291, 0.03933571, 113.59481903, -1954.82219517, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 40.56957823, 7.954e-05, 121.70873468, 0.00023863, 405.69578226, 0.00079543, -40.56957823, -7.954e-05, -121.70873468, -0.00023863, -405.69578226, -0.00079543, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 162.27831291, 0.0131119, 162.27831291, 0.03933571, 113.59481903, -1954.82219517, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 40.56957823, 7.954e-05, 121.70873468, 0.00023863, 405.69578226, 0.00079543, -40.56957823, -7.954e-05, -121.70873468, -0.00023863, -405.69578226, -0.00079543, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 16.25, 0.0, 0.0)
    ops.node(121004, 16.25, 0.0, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.09, 27840449.32158704, 11600187.21732793, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 81.57812687, 0.00081896, 97.29862595, 0.01621922, 9.7298626, 0.03937728, -81.57812687, -0.00081896, -97.29862595, -0.01621922, -9.7298626, -0.03937728, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 78.36176822, 0.00081896, 93.46245946, 0.01621922, 9.34624595, 0.03937728, -78.36176822, -0.00081896, -93.46245946, -0.01621922, -9.34624595, -0.03937728, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 100.48837589, 0.01637924, 100.48837589, 0.04913771, 70.34186312, -1194.87221991, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 25.12209397, 8.23e-05, 75.36628192, 0.00024689, 251.22093973, 0.00082295, -25.12209397, -8.23e-05, -75.36628192, -0.00024689, -251.22093973, -0.00082295, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 100.48837589, 0.01637924, 100.48837589, 0.04913771, 70.34186312, -1194.87221991, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 25.12209397, 8.23e-05, 75.36628192, 0.00024689, 251.22093973, 0.00082295, -25.12209397, -8.23e-05, -75.36628192, -0.00024689, -251.22093973, -0.00082295, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 3.65, 0.0)
    ops.node(121005, 0.0, 3.65, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.0625, 27601235.31822017, 11500514.71592507, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 46.19950832, 0.00093656, 54.74850861, 0.01531661, 5.47485086, 0.04014395, -46.19950832, -0.00093656, -54.74850861, -0.01531661, -5.47485086, -0.04014395, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 46.19950832, 0.00093656, 54.74850861, 0.01531661, 5.47485086, 0.04014395, -46.19950832, -0.00093656, -54.74850861, -0.01531661, -5.47485086, -0.04014395, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 80.65151468, 0.01873117, 80.65151468, 0.05619351, 56.45606028, -1092.61950674, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 20.16287867, 9.594e-05, 60.48863601, 0.00028781, 201.6287867, 0.00095936, -20.16287867, -9.594e-05, -60.48863601, -0.00028781, -201.6287867, -0.00095936, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 80.65151468, 0.01873117, 80.65151468, 0.05619351, 56.45606028, -1092.61950674, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 20.16287867, 9.594e-05, 60.48863601, 0.00028781, 201.6287867, 0.00095936, -20.16287867, -9.594e-05, -60.48863601, -0.00028781, -201.6287867, -0.00095936, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 2.95, 3.65, 0.0)
    ops.node(121006, 2.95, 3.65, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.16, 27569694.28155567, 11487372.61731486, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 173.52820684, 0.00065357, 207.62604215, 0.0143204, 20.76260421, 0.03133954, -173.52820684, -0.00065357, -207.62604215, -0.0143204, -20.76260421, -0.03133954, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 187.46976692, 0.00065357, 224.30708203, 0.0143204, 22.4307082, 0.03133954, -187.46976692, -0.00065357, -224.30708203, -0.0143204, -22.4307082, -0.03133954, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 151.60699794, 0.01307134, 151.60699794, 0.03921403, 106.12489856, -1569.96303154, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 37.90174949, 7.053e-05, 113.70524846, 0.00021158, 379.01749485, 0.00070525, -37.90174949, -7.053e-05, -113.70524846, -0.00021158, -379.01749485, -0.00070525, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 151.60699794, 0.01307134, 151.60699794, 0.03921403, 106.12489856, -1569.96303154, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 37.90174949, 7.053e-05, 113.70524846, 0.00021158, 379.01749485, 0.00070525, -37.90174949, -7.053e-05, -113.70524846, -0.00021158, -379.01749485, -0.00070525, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 9.6, 3.65, 0.0)
    ops.node(121007, 9.6, 3.65, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.2025, 27373518.03730932, 11405632.51554555, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 261.20676227, 0.00061645, 312.71541768, 0.01350784, 31.27154177, 0.02945123, -261.20676227, -0.00061645, -312.71541768, -0.01350784, -31.27154177, -0.02945123, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 282.98278504, 0.00061645, 338.78556225, 0.01350784, 33.87855623, 0.02945123, -282.98278504, -0.00061645, -338.78556225, -0.01350784, -33.87855623, -0.02945123, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 185.1826409, 0.01232891, 185.1826409, 0.03698673, 129.62784863, -1840.66864119, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 46.29566023, 6.855e-05, 138.88698068, 0.00020566, 462.95660226, 0.00068552, -46.29566023, -6.855e-05, -138.88698068, -0.00020566, -462.95660226, -0.00068552, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 185.1826409, 0.01232891, 185.1826409, 0.03698673, 129.62784863, -1840.66864119, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 46.29566023, 6.855e-05, 138.88698068, 0.00020566, 462.95660226, 0.00068552, -46.29566023, -6.855e-05, -138.88698068, -0.00020566, -462.95660226, -0.00068552, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 16.25, 3.65, 0.0)
    ops.node(121008, 16.25, 3.65, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.1225, 27058245.626104, 11274269.01087667, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 133.14472117, 0.00072303, 158.6014594, 0.01508006, 15.86014594, 0.03397332, -133.14472117, -0.00072303, -158.6014594, -0.01508006, -15.86014594, -0.03397332, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 128.63094266, 0.00072303, 153.22466449, 0.01508006, 15.32246645, 0.03397332, -128.63094266, -0.00072303, -153.22466449, -0.01508006, -15.32246645, -0.03397332, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 128.50468975, 0.01446054, 128.50468975, 0.04338163, 89.95328283, -1521.86459019, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 32.12617244, 7.955e-05, 96.37851731, 0.00023866, 321.26172438, 0.00079554, -32.12617244, -7.955e-05, -96.37851731, -0.00023866, -321.26172438, -0.00079554, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 128.50468975, 0.01446054, 128.50468975, 0.04338163, 89.95328283, -1521.86459019, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 32.12617244, 7.955e-05, 96.37851731, 0.00023866, 321.26172438, 0.00079554, -32.12617244, -7.955e-05, -96.37851731, -0.00023866, -321.26172438, -0.00079554, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 7.3, 0.0)
    ops.node(121009, 0.0, 7.3, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.0625, 27990151.46102585, 11662563.10876077, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 44.23573356, 0.0009369, 52.55587266, 0.01611235, 5.25558727, 0.043688, -44.23573356, -0.0009369, -52.55587266, -0.01611235, -5.25558727, -0.043688, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 44.23573356, 0.0009369, 52.55587266, 0.01611235, 5.25558727, 0.043688, -44.23573356, -0.0009369, -52.55587266, -0.01611235, -5.25558727, -0.043688, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 80.01466408, 0.01873795, 80.01466408, 0.05621385, 56.01026485, -1055.66802943, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 20.00366602, 9.386e-05, 60.01099806, 0.00028157, 200.03666019, 0.00093856, -20.00366602, -9.386e-05, -60.01099806, -0.00028157, -200.03666019, -0.00093856, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 80.01466408, 0.01873795, 80.01466408, 0.05621385, 56.01026485, -1055.66802943, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 20.00366602, 9.386e-05, 60.01099806, 0.00028157, 200.03666019, 0.00093856, -20.00366602, -9.386e-05, -60.01099806, -0.00028157, -200.03666019, -0.00093856, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 2.95, 7.3, 0.0)
    ops.node(121010, 2.95, 7.3, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 27302653.53285908, 11376105.63869128, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 172.47646216, 0.00065135, 206.81634552, 0.01598483, 20.68163455, 0.03735402, -172.47646216, -0.00065135, -206.81634552, -0.01598483, -20.68163455, -0.03735402, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 182.50835759, 0.00065135, 218.84558085, 0.01598483, 21.88455809, 0.03735402, -182.50835759, -0.00065135, -218.84558085, -0.01598483, -21.88455809, -0.03735402, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 153.52270849, 0.01302693, 153.52270849, 0.03908079, 107.46589594, -1617.66341958, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 38.38067712, 7.211e-05, 115.14203137, 0.00021634, 383.80677122, 0.00072115, -38.38067712, -7.211e-05, -115.14203137, -0.00021634, -383.80677122, -0.00072115, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 153.52270849, 0.01302693, 153.52270849, 0.03908079, 107.46589594, -1617.66341958, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 38.38067712, 7.211e-05, 115.14203137, 0.00021634, 383.80677122, 0.00072115, -38.38067712, -7.211e-05, -115.14203137, -0.00021634, -383.80677122, -0.00072115, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 9.6, 7.3, 0.0)
    ops.node(121011, 9.6, 7.3, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 27223283.14499593, 11343034.6437483, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 259.89112417, 0.0006152, 311.1147795, 0.01353333, 31.11147795, 0.02927022, -259.89112417, -0.0006152, -311.1147795, -0.01353333, -31.11147795, -0.02927022, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 281.48306906, 0.0006152, 336.96242317, 0.01353333, 33.69624232, 0.02927022, -281.48306906, -0.0006152, -336.96242317, -0.01353333, -33.69624232, -0.02927022, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 184.44291952, 0.01230406, 184.44291952, 0.03691217, 129.11004367, -1845.07818438, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 46.11072988, 6.866e-05, 138.33218964, 0.00020597, 461.10729881, 0.00068655, -46.11072988, -6.866e-05, -138.33218964, -0.00020597, -461.10729881, -0.00068655, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 184.44291952, 0.01230406, 184.44291952, 0.03691217, 129.11004367, -1845.07818438, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 46.11072988, 6.866e-05, 138.33218964, 0.00020597, 461.10729881, 0.00068655, -46.11072988, -6.866e-05, -138.33218964, -0.00020597, -461.10729881, -0.00068655, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 16.25, 7.3, 0.0)
    ops.node(121012, 16.25, 7.3, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 27994260.73399261, 11664275.30583026, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 130.70585447, 0.00073158, 155.83534268, 0.01560342, 15.58353427, 0.03635626, -130.70585447, -0.00073158, -155.83534268, -0.01560342, -15.58353427, -0.03635626, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 126.69014348, 0.00073158, 151.0475717, 0.01560342, 15.10475717, 0.03635626, -126.69014348, -0.00073158, -151.0475717, -0.01560342, -15.10475717, -0.03635626, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 132.20546157, 0.0146317, 132.20546157, 0.04389509, 92.5438231, -1521.04734106, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 33.05136539, 7.911e-05, 99.15409618, 0.00023732, 330.51365394, 0.00079108, -33.05136539, -7.911e-05, -99.15409618, -0.00023732, -330.51365394, -0.00079108, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 132.20546157, 0.0146317, 132.20546157, 0.04389509, 92.5438231, -1521.04734106, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 33.05136539, 7.911e-05, 99.15409618, 0.00023732, 330.51365394, 0.00079108, -33.05136539, -7.911e-05, -99.15409618, -0.00023732, -330.51365394, -0.00079108, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 10.95, 0.0)
    ops.node(121013, 0.0, 10.95, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0625, 27797306.29059401, 11582210.95441417, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 44.45436003, 0.00092092, 52.80430906, 0.01600026, 5.28043091, 0.04301159, -44.45436003, -0.00092092, -52.80430906, -0.01600026, -5.28043091, -0.04301159, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 44.45436003, 0.00092092, 52.80430906, 0.01600026, 5.28043091, 0.04301159, -44.45436003, -0.00092092, -52.80430906, -0.01600026, -5.28043091, -0.04301159, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 80.02209767, 0.01841839, 80.02209767, 0.05525516, 56.01546837, -1064.91050556, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 20.00552442, 9.452e-05, 60.01657325, 0.00028355, 200.05524418, 0.00094516, -20.00552442, -9.452e-05, -60.01657325, -0.00028355, -200.05524418, -0.00094516, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 80.02209767, 0.01841839, 80.02209767, 0.05525516, 56.01546837, -1064.91050556, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 20.00552442, 9.452e-05, 60.01657325, 0.00028355, 200.05524418, 0.00094516, -20.00552442, -9.452e-05, -60.01657325, -0.00028355, -200.05524418, -0.00094516, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 2.95, 10.95, 0.0)
    ops.node(121014, 2.95, 10.95, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.16, 26832014.25445624, 11180005.93935677, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 181.0712134, 0.00063944, 217.07151209, 0.01641131, 21.70715121, 0.03695304, -181.0712134, -0.00063944, -217.07151209, -0.01641131, -21.70715121, -0.03695304, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 186.23420435, 0.00063944, 223.26100091, 0.01641131, 22.32610009, 0.03695304, -186.23420435, -0.00063944, -223.26100091, -0.01641131, -22.32610009, -0.03695304, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 152.12822626, 0.01278876, 152.12822626, 0.03836628, 106.48975838, -1637.53950435, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 38.03205657, 7.271e-05, 114.0961697, 0.00021814, 380.32056565, 0.00072713, -38.03205657, -7.271e-05, -114.0961697, -0.00021814, -380.32056565, -0.00072713, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 152.12822626, 0.01278876, 152.12822626, 0.03836628, 106.48975838, -1637.53950435, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 38.03205657, 7.271e-05, 114.0961697, 0.00021814, 380.32056565, 0.00072713, -38.03205657, -7.271e-05, -114.0961697, -0.00021814, -380.32056565, -0.00072713, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.6, 10.95, 0.0)
    ops.node(121015, 9.6, 10.95, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.2025, 27764742.8153908, 11568642.83974617, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 260.89600382, 0.00062133, 312.38863919, 0.0140026, 31.23886392, 0.03047322, -260.89600382, -0.00062133, -312.38863919, -0.0140026, -31.23886392, -0.03047322, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 282.05576176, 0.00062133, 337.72466538, 0.0140026, 33.77246654, 0.03047322, -282.05576176, -0.00062133, -337.72466538, -0.0140026, -33.77246654, -0.03047322, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 189.16517431, 0.01242658, 189.16517431, 0.03727974, 132.41562202, -1868.44350599, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 47.29129358, 6.904e-05, 141.87388073, 0.00020712, 472.91293578, 0.0006904, -47.29129358, -6.904e-05, -141.87388073, -0.00020712, -472.91293578, -0.0006904, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 189.16517431, 0.01242658, 189.16517431, 0.03727974, 132.41562202, -1868.44350599, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 47.29129358, 6.904e-05, 141.87388073, 0.00020712, 472.91293578, 0.0006904, -47.29129358, -6.904e-05, -141.87388073, -0.00020712, -472.91293578, -0.0006904, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 16.25, 10.95, 0.0)
    ops.node(121016, 16.25, 10.95, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1225, 26998694.20683129, 11249455.91951304, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 132.16782604, 0.00072447, 157.42534099, 0.01471623, 15.7425341, 0.03348788, -132.16782604, -0.00072447, -157.42534099, -0.01471623, -15.7425341, -0.03348788, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 127.7711112, 0.00072447, 152.18840585, 0.01471623, 15.21884058, 0.03348788, -127.7711112, -0.00072447, -152.18840585, -0.01471623, -15.21884058, -0.03348788, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 127.03803076, 0.01448949, 127.03803076, 0.04346847, 88.92662153, -1496.81518718, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 31.75950769, 7.882e-05, 95.27852307, 0.00023646, 317.5950769, 0.00078819, -31.75950769, -7.882e-05, -95.27852307, -0.00023646, -317.5950769, -0.00078819, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 127.03803076, 0.01448949, 127.03803076, 0.04346847, 88.92662153, -1496.81518718, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 31.75950769, 7.882e-05, 95.27852307, 0.00023646, 317.5950769, 0.00078819, -31.75950769, -7.882e-05, -95.27852307, -0.00023646, -317.5950769, -0.00078819, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 14.6, 0.0)
    ops.node(121017, 0.0, 14.6, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.0625, 28401895.65062046, 11834123.18775853, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 44.74492095, 0.0009056, 53.18017655, 0.01630195, 5.31801766, 0.04506446, -44.74492095, -0.0009056, -53.18017655, -0.01630195, -5.31801766, -0.04506446, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 44.74492095, 0.0009056, 53.18017655, 0.01630195, 5.31801766, 0.04506446, -44.74492095, -0.0009056, -53.18017655, -0.01630195, -5.31801766, -0.04506446, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 80.92097441, 0.01811201, 80.92097441, 0.05433603, 56.64468208, -1056.5552651, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 20.2302436, 9.354e-05, 60.69073081, 0.00028063, 202.30243602, 0.00093543, -20.2302436, -9.354e-05, -60.69073081, -0.00028063, -202.30243602, -0.00093543, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 80.92097441, 0.01811201, 80.92097441, 0.05433603, 56.64468208, -1056.5552651, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 20.2302436, 9.354e-05, 60.69073081, 0.00028063, 202.30243602, 0.00093543, -20.2302436, -9.354e-05, -60.69073081, -0.00028063, -202.30243602, -0.00093543, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 2.95, 14.6, 0.0)
    ops.node(121018, 2.95, 14.6, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.16, 28627128.22616072, 11927970.09423363, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 179.76648006, 0.00062993, 215.54256376, 0.01696206, 21.55425638, 0.04050011, -179.76648006, -0.00062993, -215.54256376, -0.01696206, -21.55425638, -0.04050011, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 184.63804233, 0.00062993, 221.38363613, 0.01696206, 22.13836361, 0.04050011, -184.63804233, -0.00062993, -221.38363613, -0.01696206, -22.13836361, -0.04050011, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 160.4359959, 0.0125986, 160.4359959, 0.03779581, 112.30519713, -1622.45967581, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 40.10899897, 7.188e-05, 120.32699692, 0.00021563, 401.08998975, 0.00071876, -40.10899897, -7.188e-05, -120.32699692, -0.00021563, -401.08998975, -0.00071876, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 160.4359959, 0.0125986, 160.4359959, 0.03779581, 112.30519713, -1622.45967581, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 40.10899897, 7.188e-05, 120.32699692, 0.00021563, 401.08998975, 0.00071876, -40.10899897, -7.188e-05, -120.32699692, -0.00021563, -401.08998975, -0.00071876, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 9.6, 14.6, 0.0)
    ops.node(121019, 9.6, 14.6, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.2025, 27724384.06680581, 11551826.69450242, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 277.23469995, 0.00061548, 331.94861914, 0.01398715, 33.19486191, 0.03040409, -277.23469995, -0.00061548, -331.94861914, -0.01398715, -33.19486191, -0.03040409, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 287.65001388, 0.00061548, 344.41945731, 0.01398715, 34.44194573, 0.03040409, -287.65001388, -0.00061548, -344.41945731, -0.01398715, -34.44194573, -0.03040409, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 187.31439045, 0.01230963, 187.31439045, 0.03692888, 131.12007331, -1837.94857251, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 46.82859761, 6.846e-05, 140.48579284, 0.00020539, 468.28597612, 0.00068464, -46.82859761, -6.846e-05, -140.48579284, -0.00020539, -468.28597612, -0.00068464, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 187.31439045, 0.01230963, 187.31439045, 0.03692888, 131.12007331, -1837.94857251, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 46.82859761, 6.846e-05, 140.48579284, 0.00020539, 468.28597612, 0.00068464, -46.82859761, -6.846e-05, -140.48579284, -0.00020539, -468.28597612, -0.00068464, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 16.25, 14.6, 0.0)
    ops.node(121020, 16.25, 14.6, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.1225, 28599797.08678026, 11916582.11949178, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 133.71237446, 0.00071468, 159.45967213, 0.01540076, 15.94596721, 0.0373017, -133.71237446, -0.00071468, -159.45967213, -0.01540076, -15.94596721, -0.0373017, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 129.29425771, 0.00071468, 154.19081463, 0.01540076, 15.41908146, 0.0373017, -129.29425771, -0.00071468, -154.19081463, -0.01540076, -15.41908146, -0.0373017, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 134.45586309, 0.01429357, 134.45586309, 0.0428807, 94.11910416, -1517.070942, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 33.61396577, 7.875e-05, 100.84189731, 0.00023625, 336.13965771, 0.00078751, -33.61396577, -7.875e-05, -100.84189731, -0.00023625, -336.13965771, -0.00078751, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 134.45586309, 0.01429357, 134.45586309, 0.0428807, 94.11910416, -1517.070942, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 33.61396577, 7.875e-05, 100.84189731, 0.00023625, 336.13965771, 0.00078751, -33.61396577, -7.875e-05, -100.84189731, -0.00023625, -336.13965771, -0.00078751, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 0.0, 18.25, 0.0)
    ops.node(121021, 0.0, 18.25, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.0625, 26589646.42101824, 11079019.34209093, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 44.18431415, 0.00095082, 52.37718886, 0.01478817, 5.23771889, 0.03815742, -44.18431415, -0.00095082, -52.37718886, -0.01478817, -5.23771889, -0.03815742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 44.18431415, 0.00095082, 52.37718886, 0.01478817, 5.23771889, 0.03815742, -44.18431415, -0.00095082, -52.37718886, -0.01478817, -5.23771889, -0.03815742, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 76.3808678, 0.01901643, 76.3808678, 0.0570493, 53.46660746, -1039.64227569, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 19.09521695, 9.431e-05, 57.28565085, 0.00028294, 190.95216951, 0.00094313, -19.09521695, -9.431e-05, -57.28565085, -0.00028294, -190.95216951, -0.00094313, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 76.3808678, 0.01901643, 76.3808678, 0.0570493, 53.46660746, -1039.64227569, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 19.09521695, 9.431e-05, 57.28565085, 0.00028294, 190.95216951, 0.00094313, -19.09521695, -9.431e-05, -57.28565085, -0.00028294, -190.95216951, -0.00094313, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 2.95, 18.25, 0.0)
    ops.node(121022, 2.95, 18.25, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.16, 27747346.85397518, 11561394.52248966, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 180.78693236, 0.00063916, 216.8014021, 0.01633572, 21.68014021, 0.0384594, -180.78693236, -0.00063916, -216.8014021, -0.01633572, -21.68014021, -0.0384594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 185.78024234, 0.00063916, 222.78942674, 0.01633572, 22.27894267, 0.0384594, -185.78024234, -0.00063916, -222.78942674, -0.01633572, -22.27894267, -0.0384594, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 155.28625189, 0.0127833, 155.28625189, 0.03834989, 108.70037633, -1607.94862246, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 38.82156297, 7.177e-05, 116.46468892, 0.00021532, 388.21562973, 0.00071774, -38.82156297, -7.177e-05, -116.46468892, -0.00021532, -388.21562973, -0.00071774, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 155.28625189, 0.0127833, 155.28625189, 0.03834989, 108.70037633, -1607.94862246, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 38.82156297, 7.177e-05, 116.46468892, 0.00021532, 388.21562973, 0.00071774, -38.82156297, -7.177e-05, -116.46468892, -0.00021532, -388.21562973, -0.00071774, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 9.6, 18.25, 0.0)
    ops.node(121023, 9.6, 18.25, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.2025, 26506509.15412935, 11044378.81422056, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 274.21798255, 0.00061482, 328.06676483, 0.01352535, 32.80667648, 0.02824666, -274.21798255, -0.00061482, -328.06676483, -0.01352535, -32.80667648, -0.02824666, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 284.70975974, 0.00061482, 340.61883516, 0.01352535, 34.06188352, 0.02824666, -284.70975974, -0.00061482, -340.61883516, -0.01352535, -34.06188352, -0.02824666, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 179.65222855, 0.01229643, 179.65222855, 0.0368893, 125.75655999, -1841.39607732, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 44.91305714, 6.868e-05, 134.73917141, 0.00020604, 449.13057138, 0.0006868, -44.91305714, -6.868e-05, -134.73917141, -0.00020604, -449.13057138, -0.0006868, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 179.65222855, 0.01229643, 179.65222855, 0.0368893, 125.75655999, -1841.39607732, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 44.91305714, 6.868e-05, 134.73917141, 0.00020604, 449.13057138, 0.0006868, -44.91305714, -6.868e-05, -134.73917141, -0.00020604, -449.13057138, -0.0006868, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 16.25, 18.25, 0.0)
    ops.node(121024, 16.25, 18.25, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.1225, 27586072.2657209, 11494196.77738371, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 132.17685994, 0.00070931, 157.54024888, 0.01534166, 15.75402489, 0.03529581, -132.17685994, -0.00070931, -157.54024888, -0.01534166, -15.75402489, -0.03529581, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 127.74638556, 0.00070931, 152.25961173, 0.01534166, 15.22596117, 0.03529581, -127.74638556, -0.00070931, -152.25961173, -0.01534166, -15.22596117, -0.03529581, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 130.84146644, 0.01418625, 130.84146644, 0.04255874, 91.58902651, -1526.63408923, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 32.71036661, 7.945e-05, 98.13109983, 0.00023835, 327.10366611, 0.00079451, -32.71036661, -7.945e-05, -98.13109983, -0.00023835, -327.10366611, -0.00079451, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 130.84146644, 0.01418625, 130.84146644, 0.04255874, 91.58902651, -1526.63408923, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 32.71036661, 7.945e-05, 98.13109983, 0.00023835, 327.10366611, 0.00079451, -32.71036661, -7.945e-05, -98.13109983, -0.00023835, -327.10366611, -0.00079451, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170025, 0.0, 21.9, 0.0)
    ops.node(121025, 0.0, 21.9, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 25, 170025, 121025, 0.0625, 26674244.54409361, 11114268.560039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20025, 34.79696357, 0.00086816, 41.71504259, 0.01760153, 4.17150426, 0.05044706, -34.79696357, -0.00086816, -41.71504259, -0.01760153, -4.17150426, -0.05044706, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10025, 34.79696357, 0.00086816, 41.71504259, 0.01760153, 4.17150426, 0.05044706, -34.79696357, -0.00086816, -41.71504259, -0.01760153, -4.17150426, -0.05044706, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20025, 25, 0.0, 70.33748957, 0.0173631, 70.33748957, 0.05208931, 49.2362427, -897.73619182, 0.05, 2, 0, 70025, 21025, 2, 3)
    ops.uniaxialMaterial('LimitState', 40025, 17.58437239, 8.657e-05, 52.75311718, 0.00025972, 175.84372393, 0.00086575, -17.58437239, -8.657e-05, -52.75311718, -0.00025972, -175.84372393, -0.00086575, 0.4, 0.3, 0.003, 0.0, 0.0, 20025, 2)
    ops.limitCurve('ThreePoint', 10025, 25, 0.0, 70.33748957, 0.0173631, 70.33748957, 0.05208931, 49.2362427, -897.73619182, 0.05, 2, 0, 70025, 21025, 1, 3)
    ops.uniaxialMaterial('LimitState', 30025, 17.58437239, 8.657e-05, 52.75311718, 0.00025972, 175.84372393, 0.00086575, -17.58437239, -8.657e-05, -52.75311718, -0.00025972, -175.84372393, -0.00086575, 0.4, 0.3, 0.003, 0.0, 0.0, 10025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 25, 99999, 'P', 40025, 'Vy', 30025, 'Vz', 20025, 'My', 10025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170025, 70025, 170025, 25, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121025, 121025, 21025, 25, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170026, 2.95, 21.9, 0.0)
    ops.node(121026, 2.95, 21.9, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 26, 170026, 121026, 0.1225, 26803919.79636461, 11168299.91515192, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20026, 119.82928146, 0.00068627, 143.12855737, 0.01554775, 14.31285574, 0.03849127, -119.82928146, -0.00068627, -143.12855737, -0.01554775, -14.31285574, -0.03849127, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10026, 124.28712905, 0.00068627, 148.45317658, 0.01554775, 14.84531766, 0.03849127, -124.28712905, -0.00068627, -148.45317658, -0.01554775, -14.84531766, -0.03849127, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20026, 26, 0.0, 129.185193, 0.01372531, 129.185193, 0.04117593, 90.4296351, -1540.89323035, 0.05, 2, 0, 70026, 21026, 2, 3)
    ops.uniaxialMaterial('LimitState', 40026, 32.29629825, 8.073e-05, 96.88889475, 0.0002422, 322.96298249, 0.00080734, -32.29629825, -8.073e-05, -96.88889475, -0.0002422, -322.96298249, -0.00080734, 0.4, 0.3, 0.003, 0.0, 0.0, 20026, 2)
    ops.limitCurve('ThreePoint', 10026, 26, 0.0, 129.185193, 0.01372531, 129.185193, 0.04117593, 90.4296351, -1540.89323035, 0.05, 2, 0, 70026, 21026, 1, 3)
    ops.uniaxialMaterial('LimitState', 30026, 32.29629825, 8.073e-05, 96.88889475, 0.0002422, 322.96298249, 0.00080734, -32.29629825, -8.073e-05, -96.88889475, -0.0002422, -322.96298249, -0.00080734, 0.4, 0.3, 0.003, 0.0, 0.0, 10026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 26, 99999, 'P', 40026, 'Vy', 30026, 'Vz', 20026, 'My', 10026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170026, 70026, 170026, 26, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121026, 121026, 21026, 26, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170027, 9.6, 21.9, 0.0)
    ops.node(121027, 9.6, 21.9, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 27, 170027, 121027, 0.16, 27940958.63968185, 11642066.09986744, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20027, 187.9765779, 0.00064643, 224.39434198, 0.01541384, 22.4394342, 0.03760809, -187.9765779, -0.00064643, -224.39434198, -0.01541384, -22.4394342, -0.03760809, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10027, 198.10270173, 0.00064643, 236.48225697, 0.01541384, 23.6482257, 0.03760809, -198.10270173, -0.00064643, -236.48225697, -0.01541384, -23.6482257, -0.03760809, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20027, 27, 0.0, 172.0357213, 0.01292866, 172.0357213, 0.03878598, 120.42500491, -1967.84785763, 0.05, 2, 0, 70027, 21027, 2, 3)
    ops.uniaxialMaterial('LimitState', 40027, 43.00893033, 7.897e-05, 129.02679098, 0.0002369, 430.08930326, 0.00078965, -43.00893033, -7.897e-05, -129.02679098, -0.0002369, -430.08930326, -0.00078965, 0.4, 0.3, 0.003, 0.0, 0.0, 20027, 2)
    ops.limitCurve('ThreePoint', 10027, 27, 0.0, 172.0357213, 0.01292866, 172.0357213, 0.03878598, 120.42500491, -1967.84785763, 0.05, 2, 0, 70027, 21027, 1, 3)
    ops.uniaxialMaterial('LimitState', 30027, 43.00893033, 7.897e-05, 129.02679098, 0.0002369, 430.08930326, 0.00078965, -43.00893033, -7.897e-05, -129.02679098, -0.0002369, -430.08930326, -0.00078965, 0.4, 0.3, 0.003, 0.0, 0.0, 10027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 27, 99999, 'P', 40027, 'Vy', 30027, 'Vz', 20027, 'My', 10027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170027, 70027, 170027, 27, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121027, 121027, 21027, 27, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170028, 16.25, 21.9, 0.0)
    ops.node(121028, 16.25, 21.9, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 28, 170028, 121028, 0.09, 27117638.0203096, 11299015.84179567, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20028, 81.48027406, 0.00078313, 97.11684159, 0.01598231, 9.71168416, 0.04068805, -81.48027406, -0.00078313, -97.11684159, -0.01598231, -9.71168416, -0.04068805, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10028, 77.98850779, 0.00078313, 92.95498382, 0.01598231, 9.29549838, 0.04068805, -77.98850779, -0.00078313, -92.95498382, -0.01598231, -9.29549838, -0.04068805, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20028, 28, 0.0, 102.17266502, 0.01566251, 102.17266502, 0.04698752, 71.52086551, -1277.25476446, 0.05, 2, 0, 70028, 21028, 2, 3)
    ops.uniaxialMaterial('LimitState', 40028, 25.54316625, 8.59e-05, 76.62949876, 0.00025771, 255.43166254, 0.00085905, -25.54316625, -8.59e-05, -76.62949876, -0.00025771, -255.43166254, -0.00085905, 0.4, 0.3, 0.003, 0.0, 0.0, 20028, 2)
    ops.limitCurve('ThreePoint', 10028, 28, 0.0, 102.17266502, 0.01566251, 102.17266502, 0.04698752, 71.52086551, -1277.25476446, 0.05, 2, 0, 70028, 21028, 1, 3)
    ops.uniaxialMaterial('LimitState', 30028, 25.54316625, 8.59e-05, 76.62949876, 0.00025771, 255.43166254, 0.00085905, -25.54316625, -8.59e-05, -76.62949876, -0.00025771, -255.43166254, -0.00085905, 0.4, 0.3, 0.003, 0.0, 0.0, 10028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 28, 99999, 'P', 40028, 'Vy', 30028, 'Vz', 20028, 'My', 10028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170028, 70028, 170028, 28, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121028, 121028, 21028, 28, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.6, 0.0, 3.15)
    ops.node(122003, 9.6, 0.0, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.16, 26721209.98199302, 11133837.49249709, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 135.93482841, 0.00061207, 163.35487628, 0.0154403, 16.33548763, 0.04027377, -135.93482841, -0.00061207, -163.35487628, -0.0154403, -16.33548763, -0.04027377, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 121.96659097, 0.00061207, 146.56904055, 0.0154403, 14.65690406, 0.04027377, -121.96659097, -0.00061207, -146.56904055, -0.0154403, -14.65690406, -0.04027377, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 152.77980875, 0.01224147, 152.77980875, 0.03672442, 106.94586612, -1657.666967, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 38.19495219, 7.333e-05, 114.58485656, 0.00021998, 381.94952187, 0.00073328, -38.19495219, -7.333e-05, -114.58485656, -0.00021998, -381.94952187, -0.00073328, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 152.77980875, 0.01224147, 152.77980875, 0.03672442, 106.94586612, -1657.666967, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 38.19495219, 7.333e-05, 114.58485656, 0.00021998, 381.94952187, 0.00073328, -38.19495219, -7.333e-05, -114.58485656, -0.00021998, -381.94952187, -0.00073328, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 16.25, 0.0, 3.15)
    ops.node(122004, 16.25, 0.0, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.09, 27102092.29440457, 11292538.4560019, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 76.17517069, 0.00076532, 91.50678941, 0.01808505, 9.15067894, 0.04527322, -76.17517069, -0.00076532, -91.50678941, -0.01808505, -9.15067894, -0.04527322, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 69.65226331, 0.00076532, 83.67102999, 0.01808505, 8.367103, 0.04527322, -69.65226331, -0.00076532, -83.67102999, -0.01808505, -8.367103, -0.04527322, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 90.66681076, 0.01530631, 90.66681076, 0.04591894, 63.46676753, -1015.4903708, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 22.66670269, 7.627e-05, 68.00010807, 0.00022882, 226.66702689, 0.00076275, -22.66670269, -7.627e-05, -68.00010807, -0.00022882, -226.66702689, -0.00076275, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 90.66681076, 0.01530631, 90.66681076, 0.04591894, 63.46676753, -1015.4903708, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 22.66670269, 7.627e-05, 68.00010807, 0.00022882, 226.66702689, 0.00076275, -22.66670269, -7.627e-05, -68.00010807, -0.00022882, -226.66702689, -0.00076275, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 3.65, 3.2)
    ops.node(122005, 0.0, 3.65, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.0625, 27417240.48656357, 11423850.20273482, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 38.0632244, 0.00088386, 45.50083747, 0.01693082, 4.55008375, 0.04868796, -38.0632244, -0.00088386, -45.50083747, -0.01693082, -4.55008375, -0.04868796, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 38.0632244, 0.00088386, 45.50083747, 0.01693082, 4.55008375, 0.04868796, -38.0632244, -0.00088386, -45.50083747, -0.01693082, -4.55008375, -0.04868796, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 74.21801048, 0.01767717, 74.21801048, 0.05303152, 51.95260734, -947.90149455, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 18.55450262, 8.888e-05, 55.66350786, 0.00026663, 185.54502621, 0.00088876, -18.55450262, -8.888e-05, -55.66350786, -0.00026663, -185.54502621, -0.00088876, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 74.21801048, 0.01767717, 74.21801048, 0.05303152, 51.95260734, -947.90149455, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 18.55450262, 8.888e-05, 55.66350786, 0.00026663, 185.54502621, 0.00088876, -18.55450262, -8.888e-05, -55.66350786, -0.00026663, -185.54502621, -0.00088876, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 2.95, 3.65, 3.2)
    ops.node(122006, 2.95, 3.65, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.16, 27669223.57413147, 11528843.15588811, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 136.06743683, 0.00062265, 163.75841661, 0.01473666, 16.37584166, 0.03514061, -136.06743683, -0.00062265, -163.75841661, -0.01473666, -16.37584166, -0.03514061, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 136.06743683, 0.00062265, 163.75841661, 0.01473666, 16.37584166, 0.03514061, -136.06743683, -0.00062265, -163.75841661, -0.01473666, -16.37584166, -0.03514061, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 139.74753363, 0.01245297, 139.74753363, 0.03735891, 97.82327354, -1276.81944406, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 34.93688341, 6.477e-05, 104.81065022, 0.00019432, 349.36883408, 0.00064775, -34.93688341, -6.477e-05, -104.81065022, -0.00019432, -349.36883408, -0.00064775, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 139.74753363, 0.01245297, 139.74753363, 0.03735891, 97.82327354, -1276.81944406, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 34.93688341, 6.477e-05, 104.81065022, 0.00019432, 349.36883408, 0.00064775, -34.93688341, -6.477e-05, -104.81065022, -0.00019432, -349.36883408, -0.00064775, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 9.6, 3.65, 3.2)
    ops.node(122007, 9.6, 3.65, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.2025, 27049902.24789109, 11270792.60328796, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 197.39536027, 0.00060172, 237.70407168, 0.01408381, 23.77040717, 0.03263233, -197.39536027, -0.00060172, -237.70407168, -0.01408381, -23.77040717, -0.03263233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 187.8327455, 0.00060172, 226.18874294, 0.01408381, 22.61887429, 0.03263233, -187.8327455, -0.00060172, -226.18874294, -0.01408381, -22.61887429, -0.03263233, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 170.3886764, 0.01203434, 170.3886764, 0.03610303, 119.27207348, -1529.02958827, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 42.5971691, 6.383e-05, 127.7915073, 0.00019149, 425.97169101, 0.0006383, -42.5971691, -6.383e-05, -127.7915073, -0.00019149, -425.97169101, -0.0006383, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 170.3886764, 0.01203434, 170.3886764, 0.03610303, 119.27207348, -1529.02958827, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 42.5971691, 6.383e-05, 127.7915073, 0.00019149, 425.97169101, 0.0006383, -42.5971691, -6.383e-05, -127.7915073, -0.00019149, -425.97169101, -0.0006383, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 16.25, 3.65, 3.2)
    ops.node(122008, 16.25, 3.65, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.1225, 28037197.21121729, 11682165.50467387, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 117.8166203, 0.00067542, 141.42869228, 0.01691458, 14.14286923, 0.04242455, -117.8166203, -0.00067542, -141.42869228, -0.01691458, -14.14286923, -0.04242455, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 105.29163024, 0.00067542, 126.39352186, 0.01691458, 12.63935219, 0.04242455, -105.29163024, -0.00067542, -126.39352186, -0.01691458, -12.63935219, -0.04242455, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 121.96473799, 0.0135085, 121.96473799, 0.04052549, 85.37531659, -1269.84641269, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 30.4911845, 7.287e-05, 91.47355349, 0.00021861, 304.91184497, 0.00072869, -30.4911845, -7.287e-05, -91.47355349, -0.00021861, -304.91184497, -0.00072869, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 121.96473799, 0.0135085, 121.96473799, 0.04052549, 85.37531659, -1269.84641269, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 30.4911845, 7.287e-05, 91.47355349, 0.00021861, 304.91184497, 0.00072869, -30.4911845, -7.287e-05, -91.47355349, -0.00021861, -304.91184497, -0.00072869, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 7.3, 3.2)
    ops.node(122009, 0.0, 7.3, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.0625, 27701102.23286538, 11542125.93036058, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 36.49760616, 0.00086804, 43.70794744, 0.01759392, 4.37079474, 0.05179515, -36.49760616, -0.00086804, -43.70794744, -0.01759392, -4.37079474, -0.05179515, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 36.49760616, 0.00086804, 43.70794744, 0.01759392, 4.37079474, 0.05179515, -36.49760616, -0.00086804, -43.70794744, -0.01759392, -4.37079474, -0.05179515, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 73.45888549, 0.01736086, 73.45888549, 0.05208259, 51.42121984, -919.90394567, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 18.36472137, 8.707e-05, 55.09416412, 0.0002612, 183.64721372, 0.00087065, -18.36472137, -8.707e-05, -55.09416412, -0.0002612, -183.64721372, -0.00087065, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 73.45888549, 0.01736086, 73.45888549, 0.05208259, 51.42121984, -919.90394567, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 18.36472137, 8.707e-05, 55.09416412, 0.0002612, 183.64721372, 0.00087065, -18.36472137, -8.707e-05, -55.09416412, -0.0002612, -183.64721372, -0.00087065, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 2.95, 7.3, 3.2)
    ops.node(122010, 2.95, 7.3, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 27747327.30093216, 11561386.3753884, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 131.58231426, 0.00060157, 158.60676691, 0.01675984, 15.86067669, 0.04254117, -131.58231426, -0.00060157, -158.60676691, -0.01675984, -15.86067669, -0.04254117, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 121.95636162, 0.00060157, 147.00383049, 0.01675984, 14.70038305, 0.04254117, -121.95636162, -0.00060157, -147.00383049, -0.01675984, -14.70038305, -0.04254117, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 146.30152447, 0.01203147, 146.30152447, 0.03609442, 102.41106713, -1407.30057946, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 36.57538112, 6.762e-05, 109.72614335, 0.00020286, 365.75381118, 0.00067622, -36.57538112, -6.762e-05, -109.72614335, -0.00020286, -365.75381118, -0.00067622, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 146.30152447, 0.01203147, 146.30152447, 0.03609442, 102.41106713, -1407.30057946, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 36.57538112, 6.762e-05, 109.72614335, 0.00020286, 365.75381118, 0.00067622, -36.57538112, -6.762e-05, -109.72614335, -0.00020286, -365.75381118, -0.00067622, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 9.6, 7.3, 3.2)
    ops.node(122011, 9.6, 7.3, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 27498264.73159692, 11457610.30483205, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 195.56107921, 0.00059189, 235.47898953, 0.01452369, 23.54789895, 0.03362712, -195.56107921, -0.00059189, -235.47898953, -0.01452369, -23.54789895, -0.03362712, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 186.2180695, 0.00059189, 224.22888549, 0.01452369, 22.42288855, 0.03362712, -186.2180695, -0.00059189, -224.22888549, -0.01452369, -22.42288855, -0.03362712, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 174.24130921, 0.01183786, 174.24130921, 0.03551358, 121.96891645, -1550.56359547, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 43.5603273, 6.421e-05, 130.68098191, 0.00019263, 435.60327303, 0.00064209, -43.5603273, -6.421e-05, -130.68098191, -0.00019263, -435.60327303, -0.00064209, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 174.24130921, 0.01183786, 174.24130921, 0.03551358, 121.96891645, -1550.56359547, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 43.5603273, 6.421e-05, 130.68098191, 0.00019263, 435.60327303, 0.00064209, -43.5603273, -6.421e-05, -130.68098191, -0.00019263, -435.60327303, -0.00064209, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 16.25, 7.3, 3.2)
    ops.node(122012, 16.25, 7.3, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 28426418.45423739, 11844341.02259891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 116.53540828, 0.00068786, 139.87282433, 0.01711413, 13.98728243, 0.04329235, -116.53540828, -0.00068786, -139.87282433, -0.01711413, -13.98728243, -0.04329235, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 104.80221296, 0.00068786, 125.78993577, 0.01711413, 12.57899358, 0.04329235, -104.80221296, -0.00068786, -125.78993577, -0.01711413, -12.57899358, -0.04329235, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 123.72193091, 0.01375713, 123.72193091, 0.04127139, 86.60535164, -1275.44529707, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 30.93048273, 7.291e-05, 92.79144819, 0.00021872, 309.30482728, 0.00072906, -30.93048273, -7.291e-05, -92.79144819, -0.00021872, -309.30482728, -0.00072906, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 123.72193091, 0.01375713, 123.72193091, 0.04127139, 86.60535164, -1275.44529707, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 30.93048273, 7.291e-05, 92.79144819, 0.00021872, 309.30482728, 0.00072906, -30.93048273, -7.291e-05, -92.79144819, -0.00021872, -309.30482728, -0.00072906, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 10.95, 3.2)
    ops.node(122013, 0.0, 10.95, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0625, 27904915.06573193, 11627047.94405497, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 36.41965213, 0.00086198, 43.6163797, 0.01807358, 4.36163797, 0.05283379, -36.41965213, -0.00086198, -43.6163797, -0.01807358, -4.36163797, -0.05283379, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 36.41965213, 0.00086198, 43.6163797, 0.01807358, 4.36163797, 0.05283379, -36.41965213, -0.00086198, -43.6163797, -0.01807358, -4.36163797, -0.05283379, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 74.71425436, 0.01723954, 74.71425436, 0.05171862, 52.29997805, -940.81718447, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 18.67856359, 8.791e-05, 56.03569077, 0.00026372, 186.78563591, 0.00087906, -18.67856359, -8.791e-05, -56.03569077, -0.00026372, -186.78563591, -0.00087906, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 74.71425436, 0.01723954, 74.71425436, 0.05171862, 52.29997805, -940.81718447, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 18.67856359, 8.791e-05, 56.03569077, 0.00026372, 186.78563591, 0.00087906, -18.67856359, -8.791e-05, -56.03569077, -0.00026372, -186.78563591, -0.00087906, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 2.95, 10.95, 3.2)
    ops.node(122014, 2.95, 10.95, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.16, 26928738.82379294, 11220307.84324706, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 129.94763607, 0.00061245, 156.67905961, 0.01655286, 15.66790596, 0.04108255, -129.94763607, -0.00061245, -156.67905961, -0.01655286, -15.66790596, -0.04108255, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 120.7356562, 0.00061245, 145.57209078, 0.01655286, 14.55720908, 0.04108255, -120.7356562, -0.00061245, -145.57209078, -0.01655286, -14.55720908, -0.04108255, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 141.36251128, 0.01224901, 141.36251128, 0.03674704, 98.9537579, -1385.13574471, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 35.34062782, 6.732e-05, 106.02188346, 0.00020197, 353.4062782, 0.00067325, -35.34062782, -6.732e-05, -106.02188346, -0.00020197, -353.4062782, -0.00067325, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 141.36251128, 0.01224901, 141.36251128, 0.03674704, 98.9537579, -1385.13574471, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 35.34062782, 6.732e-05, 106.02188346, 0.00020197, 353.4062782, 0.00067325, -35.34062782, -6.732e-05, -106.02188346, -0.00020197, -353.4062782, -0.00067325, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.6, 10.95, 3.2)
    ops.node(122015, 9.6, 10.95, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.2025, 28178032.43047657, 11740846.84603191, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 196.45915613, 0.00058084, 236.48708327, 0.01471924, 23.64870833, 0.03462044, -196.45915613, -0.00058084, -236.48708327, -0.01471924, -23.64870833, -0.03462044, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 186.90500548, 0.00058084, 224.98630486, 0.01471924, 22.49863049, 0.03462044, -186.90500548, -0.00058084, -224.98630486, -0.01471924, -22.49863049, -0.03462044, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 178.40115323, 0.01161672, 178.40115323, 0.03485015, 124.88080726, -1548.51524892, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 44.60028831, 6.416e-05, 133.80086492, 0.00019247, 446.00288307, 0.00064156, -44.60028831, -6.416e-05, -133.80086492, -0.00019247, -446.00288307, -0.00064156, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 178.40115323, 0.01161672, 178.40115323, 0.03485015, 124.88080726, -1548.51524892, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 44.60028831, 6.416e-05, 133.80086492, 0.00019247, 446.00288307, 0.00064156, -44.60028831, -6.416e-05, -133.80086492, -0.00019247, -446.00288307, -0.00064156, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 16.25, 10.95, 3.2)
    ops.node(122016, 16.25, 10.95, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1225, 29280730.9550745, 12200304.56461438, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 117.88671399, 0.00068232, 141.41480559, 0.01718567, 14.14148056, 0.04475233, -117.88671399, -0.00068232, -141.41480559, -0.01718567, -14.14148056, -0.04475233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 105.88112591, 0.00068232, 127.01311563, 0.01718567, 12.70131156, 0.04475233, -105.88112591, -0.00068232, -127.01311563, -0.01718567, -12.70131156, -0.04475233, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 127.15963799, 0.01364641, 127.15963799, 0.04093922, 89.01174659, -1277.92284063, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 31.7899095, 7.275e-05, 95.36972849, 0.00021824, 317.89909498, 0.00072746, -31.7899095, -7.275e-05, -95.36972849, -0.00021824, -317.89909498, -0.00072746, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 127.15963799, 0.01364641, 127.15963799, 0.04093922, 89.01174659, -1277.92284063, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 31.7899095, 7.275e-05, 95.36972849, 0.00021824, 317.89909498, 0.00072746, -31.7899095, -7.275e-05, -95.36972849, -0.00021824, -317.89909498, -0.00072746, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 14.6, 3.2)
    ops.node(122017, 0.0, 14.6, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.0625, 27736419.81023252, 11556841.58759688, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 36.32435946, 0.00088918, 43.50086433, 0.01794726, 4.35008643, 0.05224597, -36.32435946, -0.00088918, -43.50086433, -0.01794726, -4.35008643, -0.05224597, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 36.32435946, 0.00088918, 43.50086433, 0.01794726, 4.35008643, 0.05224597, -36.32435946, -0.00088918, -43.50086433, -0.01794726, -4.35008643, -0.05224597, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 74.21036198, 0.01778352, 74.21036198, 0.05335057, 51.94725338, -936.6348243, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 18.55259049, 8.784e-05, 55.65777148, 0.00026353, 185.52590494, 0.00087844, -18.55259049, -8.784e-05, -55.65777148, -0.00026353, -185.52590494, -0.00087844, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 74.21036198, 0.01778352, 74.21036198, 0.05335057, 51.94725338, -936.6348243, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 18.55259049, 8.784e-05, 55.65777148, 0.00026353, 185.52590494, 0.00087844, -18.55259049, -8.784e-05, -55.65777148, -0.00026353, -185.52590494, -0.00087844, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 2.95, 14.6, 3.2)
    ops.node(122018, 2.95, 14.6, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.16, 28773795.87523847, 11989081.6146827, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 129.34873295, 0.00061228, 155.78700904, 0.01689506, 15.5787009, 0.0441087, -129.34873295, -0.00061228, -155.78700904, -0.01689506, -15.5787009, -0.0441087, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 120.76190682, 0.00061228, 145.44507581, 0.01689506, 14.54450758, 0.0441087, -120.76190682, -0.00061228, -145.44507581, -0.01689506, -14.54450758, -0.0441087, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 150.55188602, 0.01224551, 150.55188602, 0.03673654, 105.38632021, -1389.88515683, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 37.6379715, 6.71e-05, 112.91391451, 0.00020131, 376.37971504, 0.00067104, -37.6379715, -6.71e-05, -112.91391451, -0.00020131, -376.37971504, -0.00067104, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 150.55188602, 0.01224551, 150.55188602, 0.03673654, 105.38632021, -1389.88515683, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 37.6379715, 6.71e-05, 112.91391451, 0.00020131, 376.37971504, 0.00067104, -37.6379715, -6.71e-05, -112.91391451, -0.00020131, -376.37971504, -0.00067104, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 9.6, 14.6, 3.2)
    ops.node(122019, 9.6, 14.6, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.2025, 27398926.139446, 11416219.22476917, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 199.62920523, 0.0005883, 240.38346416, 0.01403186, 24.03834642, 0.03301434, -199.62920523, -0.0005883, -240.38346416, -0.01403186, -24.03834642, -0.03301434, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 189.49825656, 0.0005883, 228.18428452, 0.01403186, 22.81842845, 0.03301434, -189.49825656, -0.0005883, -228.18428452, -0.01403186, -22.81842845, -0.03301434, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 172.41374031, 0.01176606, 172.41374031, 0.03529819, 120.68961822, -1526.21938135, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 43.10343508, 6.377e-05, 129.31030523, 0.0001913, 431.03435078, 0.00063766, -43.10343508, -6.377e-05, -129.31030523, -0.0001913, -431.03435078, -0.00063766, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 172.41374031, 0.01176606, 172.41374031, 0.03529819, 120.68961822, -1526.21938135, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 43.10343508, 6.377e-05, 129.31030523, 0.0001913, 431.03435078, 0.00063766, -43.10343508, -6.377e-05, -129.31030523, -0.0001913, -431.03435078, -0.00063766, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 16.25, 14.6, 3.2)
    ops.node(122020, 16.25, 14.6, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.1225, 27877473.28220074, 11615613.86758364, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 117.091816, 0.00068711, 140.56255064, 0.01728349, 14.05625506, 0.04251266, -117.091816, -0.00068711, -140.56255064, -0.01728349, -14.05625506, -0.04251266, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 104.98867038, 0.00068711, 126.03336254, 0.01728349, 12.60333625, 0.04251266, -104.98867038, -0.00068711, -126.03336254, -0.01728349, -12.60333625, -0.04251266, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 122.62251229, 0.01374227, 122.62251229, 0.04122681, 85.8357586, -1297.58222287, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 30.65562807, 7.368e-05, 91.96688422, 0.00022104, 306.55628073, 0.00073681, -30.65562807, -7.368e-05, -91.96688422, -0.00022104, -306.55628073, -0.00073681, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 122.62251229, 0.01374227, 122.62251229, 0.04122681, 85.8357586, -1297.58222287, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 30.65562807, 7.368e-05, 91.96688422, 0.00022104, 306.55628073, 0.00073681, -30.65562807, -7.368e-05, -91.96688422, -0.00022104, -306.55628073, -0.00073681, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 0.0, 18.25, 3.2)
    ops.node(122021, 0.0, 18.25, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.0625, 27584856.71586768, 11493690.2982782, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 36.24509846, 0.00089418, 43.40403394, 0.01793272, 4.34040339, 0.05181123, -36.24509846, -0.00089418, -43.40403394, -0.01793272, -4.34040339, -0.05181123, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 36.24509846, 0.00089418, 43.40403394, 0.01793272, 4.34040339, 0.05181123, -36.24509846, -0.00089418, -43.40403394, -0.01793272, -4.34040339, -0.05181123, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 74.22612496, 0.01788352, 74.22612496, 0.05365057, 51.95828747, -944.4422633, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 18.55653124, 8.835e-05, 55.66959372, 0.00026504, 185.5653124, 0.00088345, -18.55653124, -8.835e-05, -55.66959372, -0.00026504, -185.5653124, -0.00088345, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 74.22612496, 0.01788352, 74.22612496, 0.05365057, 51.95828747, -944.4422633, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 18.55653124, 8.835e-05, 55.66959372, 0.00026504, 185.5653124, 0.00088345, -18.55653124, -8.835e-05, -55.66959372, -0.00026504, -185.5653124, -0.00088345, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 2.95, 18.25, 3.2)
    ops.node(122022, 2.95, 18.25, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.16, 27604231.51047998, 11501763.12936666, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 131.03611377, 0.00060794, 157.95989151, 0.01658179, 15.79598915, 0.04215151, -131.03611377, -0.00060794, -157.95989151, -0.01658179, -15.79598915, -0.04215151, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 121.64139056, 0.00060794, 146.63484976, 0.01658179, 14.66348498, 0.04215151, -121.64139056, -0.00060794, -146.63484976, -0.01658179, -14.66348498, -0.04215151, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 144.4075426, 0.01215884, 144.4075426, 0.03647653, 101.08527982, -1380.52035353, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 36.10188565, 6.709e-05, 108.30565695, 0.00020128, 361.0188565, 0.00067092, -36.10188565, -6.709e-05, -108.30565695, -0.00020128, -361.0188565, -0.00067092, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 144.4075426, 0.01215884, 144.4075426, 0.03647653, 101.08527982, -1380.52035353, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 36.10188565, 6.709e-05, 108.30565695, 0.00020128, 361.0188565, 0.00067092, -36.10188565, -6.709e-05, -108.30565695, -0.00020128, -361.0188565, -0.00067092, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 9.6, 18.25, 3.2)
    ops.node(122023, 9.6, 18.25, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.2025, 28376587.9715132, 11823578.32146383, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 197.91146695, 0.00057968, 238.2030789, 0.01426524, 23.82030789, 0.03438979, -197.91146695, -0.00057968, -238.2030789, -0.01426524, -23.82030789, -0.03438979, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 188.14144743, 0.00057968, 226.44403954, 0.01426524, 22.64440395, 0.03438979, -188.14144743, -0.00057968, -226.44403954, -0.01426524, -22.64440395, -0.03438979, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 178.53256799, 0.01159368, 178.53256799, 0.03478105, 124.97279759, -1525.91979911, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 44.633142, 6.375e-05, 133.89942599, 0.00019126, 446.33141998, 0.00063754, -44.633142, -6.375e-05, -133.89942599, -0.00019126, -446.33141998, -0.00063754, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 178.53256799, 0.01159368, 178.53256799, 0.03478105, 124.97279759, -1525.91979911, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 44.633142, 6.375e-05, 133.89942599, 0.00019126, 446.33141998, 0.00063754, -44.633142, -6.375e-05, -133.89942599, -0.00019126, -446.33141998, -0.00063754, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 16.25, 18.25, 3.2)
    ops.node(122024, 16.25, 18.25, 5.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.1225, 27810862.23994924, 11587859.26664552, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 119.19896183, 0.00068744, 143.09311696, 0.01716688, 14.3093117, 0.0422778, -119.19896183, -0.00068744, -143.09311696, -0.01716688, -14.3093117, -0.0422778, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 106.41877183, 0.00068744, 127.75106033, 0.01716688, 12.77510603, 0.0422778, -106.41877183, -0.00068744, -127.75106033, -0.01716688, -12.77510603, -0.0422778, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 122.05085447, 0.01374872, 122.05085447, 0.04124617, 85.43559813, -1290.64305522, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 30.51271362, 7.351e-05, 91.53814085, 0.00022054, 305.12713616, 0.00073514, -30.51271362, -7.351e-05, -91.53814085, -0.00022054, -305.12713616, -0.00073514, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 122.05085447, 0.01374872, 122.05085447, 0.04124617, 85.43559813, -1290.64305522, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 30.51271362, 7.351e-05, 91.53814085, 0.00022054, 305.12713616, 0.00073514, -30.51271362, -7.351e-05, -91.53814085, -0.00022054, -305.12713616, -0.00073514, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171025, 0.0, 21.9, 3.15)
    ops.node(122025, 0.0, 21.9, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1025, 171025, 122025, 0.0625, 29172134.69635449, 12155056.12348104, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21025, 29.30384059, 0.00082212, 35.30013206, 0.01982104, 3.53001321, 0.06550563, -29.30384059, -0.00082212, -35.30013206, -0.01982104, -3.53001321, -0.06550563, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11025, 29.30384059, 0.00082212, 35.30013206, 0.01982104, 3.53001321, 0.06550563, -29.30384059, -0.00082212, -35.30013206, -0.01982104, -3.53001321, -0.06550563, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21025, 1025, 0.0, 71.22064121, 0.01644249, 71.22064121, 0.04932747, 49.85444884, -843.37836564, 0.05, 2, 0, 71025, 22025, 2, 3)
    ops.uniaxialMaterial('LimitState', 41025, 17.8051603, 8.016e-05, 53.4154809, 0.00024047, 178.05160301, 0.00080156, -17.8051603, -8.016e-05, -53.4154809, -0.00024047, -178.05160301, -0.00080156, 0.4, 0.3, 0.003, 0.0, 0.0, 21025, 2)
    ops.limitCurve('ThreePoint', 11025, 1025, 0.0, 71.22064121, 0.01644249, 71.22064121, 0.04932747, 49.85444884, -843.37836564, 0.05, 2, 0, 71025, 22025, 1, 3)
    ops.uniaxialMaterial('LimitState', 31025, 17.8051603, 8.016e-05, 53.4154809, 0.00024047, 178.05160301, 0.00080156, -17.8051603, -8.016e-05, -53.4154809, -0.00024047, -178.05160301, -0.00080156, 0.4, 0.3, 0.003, 0.0, 0.0, 11025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1025, 99999, 'P', 41025, 'Vy', 31025, 'Vz', 21025, 'My', 11025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171025, 71025, 171025, 1025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122025, 122025, 22025, 1025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171026, 2.95, 21.9, 3.15)
    ops.node(122026, 2.95, 21.9, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1026, 171026, 122026, 0.1225, 27828952.93729831, 11595397.05720763, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21026, 90.90983699, 0.00065152, 109.37626557, 0.01701012, 10.93762656, 0.04762639, -90.90983699, -0.00065152, -109.37626557, -0.01701012, -10.93762656, -0.04762639, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11026, 82.66530223, 0.00065152, 99.45702631, 0.01701012, 9.94570263, 0.04762639, -82.66530223, -0.00065152, -99.45702631, -0.01701012, -9.94570263, -0.04762639, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21026, 1026, 0.0, 124.61776931, 0.01303033, 124.61776931, 0.039091, 87.23243851, -1353.33125782, 0.05, 2, 0, 71026, 22026, 2, 3)
    ops.uniaxialMaterial('LimitState', 41026, 31.15444233, 7.501e-05, 93.46332698, 0.00022503, 311.54442327, 0.00075011, -31.15444233, -7.501e-05, -93.46332698, -0.00022503, -311.54442327, -0.00075011, 0.4, 0.3, 0.003, 0.0, 0.0, 21026, 2)
    ops.limitCurve('ThreePoint', 11026, 1026, 0.0, 124.61776931, 0.01303033, 124.61776931, 0.039091, 87.23243851, -1353.33125782, 0.05, 2, 0, 71026, 22026, 1, 3)
    ops.uniaxialMaterial('LimitState', 31026, 31.15444233, 7.501e-05, 93.46332698, 0.00022503, 311.54442327, 0.00075011, -31.15444233, -7.501e-05, -93.46332698, -0.00022503, -311.54442327, -0.00075011, 0.4, 0.3, 0.003, 0.0, 0.0, 11026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1026, 99999, 'P', 41026, 'Vy', 31026, 'Vz', 21026, 'My', 11026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171026, 71026, 171026, 1026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122026, 122026, 22026, 1026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171027, 9.6, 21.9, 3.15)
    ops.node(122027, 9.6, 21.9, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1027, 171027, 122027, 0.16, 26602686.18153297, 11084452.57563874, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21027, 138.82452126, 0.00061652, 166.81850078, 0.01571545, 16.68185008, 0.04031395, -138.82452126, -0.00061652, -166.81850078, -0.01571545, -16.68185008, -0.04031395, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11027, 123.76621411, 0.00061652, 148.72368439, 0.01571545, 14.87236844, 0.04031395, -123.76621411, -0.00061652, -148.72368439, -0.01571545, -14.87236844, -0.04031395, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21027, 1027, 0.0, 153.34947181, 0.01233032, 153.34947181, 0.03699096, 107.34463027, -1683.40423912, 0.05, 2, 0, 71027, 22027, 2, 3)
    ops.uniaxialMaterial('LimitState', 41027, 38.33736795, 7.393e-05, 115.01210386, 0.00022179, 383.37367953, 0.00073929, -38.33736795, -7.393e-05, -115.01210386, -0.00022179, -383.37367953, -0.00073929, 0.4, 0.3, 0.003, 0.0, 0.0, 21027, 2)
    ops.limitCurve('ThreePoint', 11027, 1027, 0.0, 153.34947181, 0.01233032, 153.34947181, 0.03699096, 107.34463027, -1683.40423912, 0.05, 2, 0, 71027, 22027, 1, 3)
    ops.uniaxialMaterial('LimitState', 31027, 38.33736795, 7.393e-05, 115.01210386, 0.00022179, 383.37367953, 0.00073929, -38.33736795, -7.393e-05, -115.01210386, -0.00022179, -383.37367953, -0.00073929, 0.4, 0.3, 0.003, 0.0, 0.0, 11027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1027, 99999, 'P', 41027, 'Vy', 31027, 'Vz', 21027, 'My', 11027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171027, 71027, 171027, 1027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122027, 122027, 22027, 1027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171028, 16.25, 21.9, 3.15)
    ops.node(122028, 16.25, 21.9, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1028, 171028, 122028, 0.09, 27453647.18005611, 11439019.65835671, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21028, 72.13051097, 0.00073302, 86.65219909, 0.01803354, 8.66521991, 0.05002056, -72.13051097, -0.00073302, -86.65219909, -0.01803354, -8.66521991, -0.05002056, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11028, 62.37584569, 0.00073302, 74.93367407, 0.01803354, 7.49336741, 0.05002056, -62.37584569, -0.00073302, -74.93367407, -0.01803354, -7.49336741, -0.05002056, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21028, 1028, 0.0, 96.29286507, 0.01466032, 96.29286507, 0.04398096, 67.40500555, -1125.57540794, 0.05, 2, 0, 71028, 22028, 2, 3)
    ops.uniaxialMaterial('LimitState', 41028, 24.07321627, 7.997e-05, 72.2196488, 0.00023991, 240.73216268, 0.0007997, -24.07321627, -7.997e-05, -72.2196488, -0.00023991, -240.73216268, -0.0007997, 0.4, 0.3, 0.003, 0.0, 0.0, 21028, 2)
    ops.limitCurve('ThreePoint', 11028, 1028, 0.0, 96.29286507, 0.01466032, 96.29286507, 0.04398096, 67.40500555, -1125.57540794, 0.05, 2, 0, 71028, 22028, 1, 3)
    ops.uniaxialMaterial('LimitState', 31028, 24.07321627, 7.997e-05, 72.2196488, 0.00023991, 240.73216268, 0.0007997, -24.07321627, -7.997e-05, -72.2196488, -0.00023991, -240.73216268, -0.0007997, 0.4, 0.3, 0.003, 0.0, 0.0, 11028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1028, 99999, 'P', 41028, 'Vy', 31028, 'Vz', 21028, 'My', 11028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171028, 71028, 171028, 1028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122028, 122028, 22028, 1028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.6, 0.0, 6.0)
    ops.node(123003, 9.6, 0.0, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.1225, 28615495.08058058, 11923122.95024191, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 84.41010491, 0.00064009, 101.6982385, 0.01755531, 10.16982385, 0.0514444, -84.41010491, -0.00064009, -101.6982385, -0.01755531, -10.16982385, -0.0514444, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 76.7235421, 0.00064009, 92.43738165, 0.01755531, 9.24373816, 0.0514444, -76.7235421, -0.00064009, -92.43738165, -0.01755531, -9.24373816, -0.0514444, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 123.89533937, 0.01280181, 123.89533937, 0.03840543, 86.72673756, -1281.9176478, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 30.97383484, 7.253e-05, 92.92150453, 0.00021758, 309.73834843, 0.00072526, -30.97383484, -7.253e-05, -92.92150453, -0.00021758, -309.73834843, -0.00072526, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 123.89533937, 0.01280181, 123.89533937, 0.03840543, 86.72673756, -1281.9176478, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 30.97383484, 7.253e-05, 92.92150453, 0.00021758, 309.73834843, 0.00072526, -30.97383484, -7.253e-05, -92.92150453, -0.00021758, -309.73834843, -0.00072526, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 16.25, 0.0, 6.0)
    ops.node(123004, 16.25, 0.0, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 27539782.31906125, 11474909.29960885, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 39.3644168, 0.00092616, 47.38191689, 0.01959045, 4.73819169, 0.05370501, -39.3644168, -0.00092616, -47.38191689, -0.01959045, -4.73819169, -0.05370501, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 39.3644168, 0.00092616, 47.38191689, 0.01959045, 4.73819169, 0.05370501, -39.3644168, -0.00092616, -47.38191689, -0.01959045, -4.73819169, -0.05370501, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 66.01791235, 0.01852322, 66.01791235, 0.05556965, 46.21253865, -770.56957146, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 16.50447809, 7.87e-05, 49.51343427, 0.00023611, 165.04478088, 0.00078704, -16.50447809, -7.87e-05, -49.51343427, -0.00023611, -165.04478088, -0.00078704, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 66.01791235, 0.01852322, 66.01791235, 0.05556965, 46.21253865, -770.56957146, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 16.50447809, 7.87e-05, 49.51343427, 0.00023611, 165.04478088, 0.00078704, -16.50447809, -7.87e-05, -49.51343427, -0.00023611, -165.04478088, -0.00078704, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 3.65, 6.05)
    ops.node(123005, 0.0, 3.65, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 26181098.34604938, 10908790.97752057, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 28.62102486, 0.00086495, 34.52801695, 0.0193119, 3.45280169, 0.05768375, -28.62102486, -0.00086495, -34.52801695, -0.0193119, -3.45280169, -0.05768375, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 28.62102486, 0.00086495, 34.52801695, 0.0193119, 3.45280169, 0.05768375, -28.62102486, -0.00086495, -34.52801695, -0.0193119, -3.45280169, -0.05768375, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 66.07968525, 0.01729904, 66.07968525, 0.05189713, 46.25577967, -854.35864881, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 16.51992131, 8.287e-05, 49.55976394, 0.0002486, 165.19921312, 0.00082866, -16.51992131, -8.287e-05, -49.55976394, -0.0002486, -165.19921312, -0.00082866, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 66.07968525, 0.01729904, 66.07968525, 0.05189713, 46.25577967, -854.35864881, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 16.51992131, 8.287e-05, 49.55976394, 0.0002486, 165.19921312, 0.00082866, -16.51992131, -8.287e-05, -49.55976394, -0.0002486, -165.19921312, -0.00082866, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 2.95, 3.65, 6.05)
    ops.node(123006, 2.95, 3.65, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1225, 27173540.72653969, 11322308.6360582, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 95.48299342, 0.00067665, 115.19054921, 0.01625296, 11.51905492, 0.03921557, -95.48299342, -0.00067665, -115.19054921, -0.01625296, -11.51905492, -0.03921557, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 95.48299342, 0.00067665, 115.19054921, 0.01625296, 11.51905492, 0.03921557, -95.48299342, -0.00067665, -115.19054921, -0.01625296, -11.51905492, -0.03921557, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 105.16851207, 0.01353309, 105.16851207, 0.04059926, 73.61795845, -974.21010554, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 26.29212802, 6.483e-05, 78.87638406, 0.00019449, 262.92128019, 0.00064831, -26.29212802, -6.483e-05, -78.87638406, -0.00019449, -262.92128019, -0.00064831, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 105.16851207, 0.01353309, 105.16851207, 0.04059926, 73.61795845, -974.21010554, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 26.29212802, 6.483e-05, 78.87638406, 0.00019449, 262.92128019, 0.00064831, -26.29212802, -6.483e-05, -78.87638406, -0.00019449, -262.92128019, -0.00064831, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 9.6, 3.65, 6.05)
    ops.node(123007, 9.6, 3.65, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 26517997.71690856, 11049165.71537857, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 106.28587892, 0.00070289, 127.67025837, 0.01431431, 12.76702584, 0.0336243, -106.28587892, -0.00070289, -127.67025837, -0.01431431, -12.76702584, -0.0336243, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 106.28587892, 0.00070289, 127.67025837, 0.01431431, 12.76702584, 0.0336243, -106.28587892, -0.00070289, -127.67025837, -0.01431431, -12.76702584, -0.0336243, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 107.78366096, 0.01405784, 107.78366096, 0.04217351, 75.44856267, -1088.92578913, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 26.94591524, 6.809e-05, 80.83774572, 0.00020426, 269.4591524, 0.00068085, -26.94591524, -6.809e-05, -80.83774572, -0.00020426, -269.4591524, -0.00068085, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 107.78366096, 0.01405784, 107.78366096, 0.04217351, 75.44856267, -1088.92578913, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 26.94591524, 6.809e-05, 80.83774572, 0.00020426, 269.4591524, 0.00068085, -26.94591524, -6.809e-05, -80.83774572, -0.00020426, -269.4591524, -0.00068085, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 16.25, 3.65, 6.05)
    ops.node(123008, 16.25, 3.65, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 29899798.5694064, 12458249.40391933, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 47.90259796, 0.00092578, 57.17994578, 0.0178003, 5.71799458, 0.04988466, -47.90259796, -0.00092578, -57.17994578, -0.0178003, -5.71799458, -0.04988466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 47.90259796, 0.00092578, 57.17994578, 0.0178003, 5.71799458, 0.04988466, -47.90259796, -0.00092578, -57.17994578, -0.0178003, -5.71799458, -0.04988466, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 72.75855051, 0.01851562, 72.75855051, 0.05554686, 50.93098535, -867.66957801, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 18.18963763, 7.989e-05, 54.56891288, 0.00023968, 181.89637627, 0.00079894, -18.18963763, -7.989e-05, -54.56891288, -0.00023968, -181.89637627, -0.00079894, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 72.75855051, 0.01851562, 72.75855051, 0.05554686, 50.93098535, -867.66957801, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 18.18963763, 7.989e-05, 54.56891288, 0.00023968, 181.89637627, 0.00079894, -18.18963763, -7.989e-05, -54.56891288, -0.00023968, -181.89637627, -0.00079894, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 7.3, 6.05)
    ops.node(123009, 0.0, 7.3, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 29353960.10187443, 12230816.70911434, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 28.07910949, 0.00080793, 33.84369189, 0.02046353, 3.38436919, 0.06762059, -28.07910949, -0.00080793, -33.84369189, -0.02046353, -3.38436919, -0.06762059, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 28.07910949, 0.00080793, 33.84369189, 0.02046353, 3.38436919, 0.06762059, -28.07910949, -0.00080793, -33.84369189, -0.02046353, -3.38436919, -0.06762059, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 71.28515566, 0.01615851, 71.28515566, 0.04847552, 49.89960896, -850.58843615, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 17.82128891, 7.973e-05, 53.46386674, 0.00023919, 178.21288914, 0.00079731, -17.82128891, -7.973e-05, -53.46386674, -0.00023919, -178.21288914, -0.00079731, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 71.28515566, 0.01615851, 71.28515566, 0.04847552, 49.89960896, -850.58843615, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 17.82128891, 7.973e-05, 53.46386674, 0.00023919, 178.21288914, 0.00079731, -17.82128891, -7.973e-05, -53.46386674, -0.00023919, -178.21288914, -0.00079731, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 2.95, 7.3, 6.05)
    ops.node(123010, 2.95, 7.3, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 28446412.30822515, 11852671.79509382, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 84.33954253, 0.00064303, 101.78201145, 0.01800548, 10.17820115, 0.04884391, -84.33954253, -0.00064303, -101.78201145, -0.01800548, -10.17820115, -0.04884391, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 80.52093853, 0.00064303, 97.17367253, 0.01800548, 9.71736725, 0.04884391, -80.52093853, -0.00064303, -97.17367253, -0.01800548, -9.71736725, -0.04884391, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 114.88956783, 0.01286057, 114.88956783, 0.03858171, 80.42269748, -1095.39236915, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 28.72239196, 6.765e-05, 86.16717587, 0.00020296, 287.22391957, 0.00067654, -28.72239196, -6.765e-05, -86.16717587, -0.00020296, -287.22391957, -0.00067654, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 114.88956783, 0.01286057, 114.88956783, 0.03858171, 80.42269748, -1095.39236915, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 28.72239196, 6.765e-05, 86.16717587, 0.00020296, 287.22391957, 0.00067654, -28.72239196, -6.765e-05, -86.16717587, -0.00020296, -287.22391957, -0.00067654, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 9.6, 7.3, 6.05)
    ops.node(123011, 9.6, 7.3, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 27951959.79522955, 11646649.91467898, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 105.57571087, 0.00071134, 126.8436982, 0.01491986, 12.68436982, 0.03640573, -105.57571087, -0.00071134, -126.8436982, -0.01491986, -12.68436982, -0.03640573, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 105.57571087, 0.00071134, 126.8436982, 0.01491986, 12.68436982, 0.03640573, -105.57571087, -0.00071134, -126.8436982, -0.01491986, -12.68436982, -0.03640573, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 113.39483413, 0.0142268, 113.39483413, 0.04268039, 79.37638389, -1093.15950822, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 28.34870853, 6.796e-05, 85.0461256, 0.00020387, 283.48708532, 0.00067955, -28.34870853, -6.796e-05, -85.0461256, -0.00020387, -283.48708532, -0.00067955, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 113.39483413, 0.0142268, 113.39483413, 0.04268039, 79.37638389, -1093.15950822, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 28.34870853, 6.796e-05, 85.0461256, 0.00020387, 283.48708532, 0.00067955, -28.34870853, -6.796e-05, -85.0461256, -0.00020387, -283.48708532, -0.00067955, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 16.25, 7.3, 6.05)
    ops.node(123012, 16.25, 7.3, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 28344022.70482242, 11810009.46034267, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 47.05709948, 0.00093124, 56.19327262, 0.01769311, 5.61932726, 0.04627576, -47.05709948, -0.00093124, -56.19327262, -0.01769311, -5.61932726, -0.04627576, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 47.05709948, 0.00093124, 56.19327262, 0.01769311, 5.61932726, 0.04627576, -47.05709948, -0.00093124, -56.19327262, -0.01769311, -5.61932726, -0.04627576, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 72.06655462, 0.01862479, 72.06655462, 0.05587438, 50.44658823, -886.30329803, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 18.01663865, 8.348e-05, 54.04991596, 0.00025043, 180.16638654, 0.00083478, -18.01663865, -8.348e-05, -54.04991596, -0.00025043, -180.16638654, -0.00083478, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 72.06655462, 0.01862479, 72.06655462, 0.05587438, 50.44658823, -886.30329803, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 18.01663865, 8.348e-05, 54.04991596, 0.00025043, 180.16638654, 0.00083478, -18.01663865, -8.348e-05, -54.04991596, -0.00025043, -180.16638654, -0.00083478, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 10.95, 6.05)
    ops.node(123013, 0.0, 10.95, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 26951226.28414627, 11229677.61839428, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 28.30416554, 0.00081718, 34.19141937, 0.01973273, 3.41914194, 0.06175079, -28.30416554, -0.00081718, -34.19141937, -0.01973273, -3.41914194, -0.06175079, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 28.30416554, 0.00081718, 34.19141937, 0.01973273, 3.41914194, 0.06175079, -28.30416554, -0.00081718, -34.19141937, -0.01973273, -3.41914194, -0.06175079, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 66.35175116, 0.0163435, 66.35175116, 0.04903051, 46.44622581, -838.94513188, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 16.58793779, 8.083e-05, 49.76381337, 0.00024249, 165.8793779, 0.0008083, -16.58793779, -8.083e-05, -49.76381337, -0.00024249, -165.8793779, -0.0008083, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 66.35175116, 0.0163435, 66.35175116, 0.04903051, 46.44622581, -838.94513188, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 16.58793779, 8.083e-05, 49.76381337, 0.00024249, 165.8793779, 0.0008083, -16.58793779, -8.083e-05, -49.76381337, -0.00024249, -165.8793779, -0.0008083, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 2.95, 10.95, 6.05)
    ops.node(123014, 2.95, 10.95, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1225, 27286947.98524707, 11369561.66051961, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 83.94687663, 0.00065468, 101.40443109, 0.01800033, 10.14044311, 0.04711743, -83.94687663, -0.00065468, -101.40443109, -0.01800033, -10.14044311, -0.04711743, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 80.15888926, 0.00065468, 96.82869558, 0.01800033, 9.68286956, 0.04711743, -80.15888926, -0.00065468, -96.82869558, -0.01800033, -9.68286956, -0.04711743, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 111.38938882, 0.01309351, 111.38938882, 0.03928053, 77.97257218, -1113.89397471, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 27.84734721, 6.838e-05, 83.54204162, 0.00020514, 278.47347206, 0.0006838, -27.84734721, -6.838e-05, -83.54204162, -0.00020514, -278.47347206, -0.0006838, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 111.38938882, 0.01309351, 111.38938882, 0.03928053, 77.97257218, -1113.89397471, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 27.84734721, 6.838e-05, 83.54204162, 0.00020514, 278.47347206, 0.0006838, -27.84734721, -6.838e-05, -83.54204162, -0.00020514, -278.47347206, -0.0006838, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.6, 10.95, 6.05)
    ops.node(123015, 9.6, 10.95, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 27786675.74057118, 11577781.55857133, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 107.23246369, 0.0006901, 128.83902183, 0.01519152, 12.88390218, 0.03644003, -107.23246369, -0.0006901, -128.83902183, -0.01519152, -12.88390218, -0.03644003, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 107.23246369, 0.0006901, 128.83902183, 0.01519152, 12.88390218, 0.03644003, -107.23246369, -0.0006901, -128.83902183, -0.01519152, -12.88390218, -0.03644003, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 113.61568752, 0.01380206, 113.61568752, 0.04140618, 79.53098127, -1110.74298533, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 28.40392188, 6.849e-05, 85.21176564, 0.00020548, 284.03921881, 0.00068492, -28.40392188, -6.849e-05, -85.21176564, -0.00020548, -284.03921881, -0.00068492, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 113.61568752, 0.01380206, 113.61568752, 0.04140618, 79.53098127, -1110.74298533, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 28.40392188, 6.849e-05, 85.21176564, 0.00020548, 284.03921881, 0.00068492, -28.40392188, -6.849e-05, -85.21176564, -0.00020548, -284.03921881, -0.00068492, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 16.25, 10.95, 6.05)
    ops.node(123016, 16.25, 10.95, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 27432290.77154844, 11430121.15481185, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 47.76478094, 0.00094486, 57.01154697, 0.01693939, 5.7011547, 0.04328336, -47.76478094, -0.00094486, -57.01154697, -0.01693939, -5.7011547, -0.04328336, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 47.76478094, 0.00094486, 57.01154697, 0.01693939, 5.7011547, 0.04328336, -47.76478094, -0.00094486, -57.01154697, -0.01693939, -5.7011547, -0.04328336, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 68.53594118, 0.01889724, 68.53594118, 0.05669173, 47.97515883, -870.0110727, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 17.1339853, 8.203e-05, 51.40195589, 0.00024608, 171.33985296, 0.00082026, -17.1339853, -8.203e-05, -51.40195589, -0.00024608, -171.33985296, -0.00082026, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 68.53594118, 0.01889724, 68.53594118, 0.05669173, 47.97515883, -870.0110727, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 17.1339853, 8.203e-05, 51.40195589, 0.00024608, 171.33985296, 0.00082026, -17.1339853, -8.203e-05, -51.40195589, -0.00024608, -171.33985296, -0.00082026, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 14.6, 6.05)
    ops.node(123017, 0.0, 14.6, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 26366582.23586136, 10986075.9316089, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 27.7881896, 0.00082178, 33.57224586, 0.01954431, 3.35722459, 0.060104, -27.7881896, -0.00082178, -33.57224586, -0.01954431, -3.35722459, -0.060104, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 27.7881896, 0.00082178, 33.57224586, 0.01954431, 3.35722459, 0.060104, -27.7881896, -0.00082178, -33.57224586, -0.01954431, -3.35722459, -0.060104, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 64.99014667, 0.01643566, 64.99014667, 0.04930699, 45.49310267, -830.53776029, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 16.24753667, 8.093e-05, 48.74261001, 0.00024278, 162.47536668, 0.00080927, -16.24753667, -8.093e-05, -48.74261001, -0.00024278, -162.47536668, -0.00080927, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 64.99014667, 0.01643566, 64.99014667, 0.04930699, 45.49310267, -830.53776029, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 16.24753667, 8.093e-05, 48.74261001, 0.00024278, 162.47536668, 0.00080927, -16.24753667, -8.093e-05, -48.74261001, -0.00024278, -162.47536668, -0.00080927, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 2.95, 14.6, 6.05)
    ops.node(123018, 2.95, 14.6, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1225, 29561045.92235452, 12317102.46764771, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 85.50835842, 0.00064316, 103.04006128, 0.0178794, 10.30400613, 0.05018305, -85.50835842, -0.00064316, -103.04006128, -0.0178794, -10.30400613, -0.05018305, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 81.62387193, 0.00064316, 98.35914198, 0.0178794, 9.8359142, 0.05018305, -81.62387193, -0.00064316, -98.35914198, -0.0178794, -9.8359142, -0.05018305, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 119.20888223, 0.01286315, 119.20888223, 0.03858944, 83.44621756, -1098.57653913, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 29.80222056, 6.755e-05, 89.40666167, 0.00020265, 298.02220556, 0.00067551, -29.80222056, -6.755e-05, -89.40666167, -0.00020265, -298.02220556, -0.00067551, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 119.20888223, 0.01286315, 119.20888223, 0.03858944, 83.44621756, -1098.57653913, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 29.80222056, 6.755e-05, 89.40666167, 0.00020265, 298.02220556, 0.00067551, -29.80222056, -6.755e-05, -89.40666167, -0.00020265, -298.02220556, -0.00067551, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 9.6, 14.6, 6.05)
    ops.node(123019, 9.6, 14.6, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1225, 27613911.03063542, 11505796.26276476, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 107.57874933, 0.00069356, 129.25801181, 0.01486944, 12.92580118, 0.03586612, -107.57874933, -0.00069356, -129.25801181, -0.01486944, -12.92580118, -0.03586612, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 107.57874933, 0.00069356, 129.25801181, 0.01486944, 12.92580118, 0.03586612, -107.57874933, -0.00069356, -129.25801181, -0.01486944, -12.92580118, -0.03586612, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 112.66394806, 0.01387115, 112.66394806, 0.04161345, 78.86476364, -1104.61505991, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 28.16598701, 6.834e-05, 84.49796104, 0.00020503, 281.65987014, 0.00068344, -28.16598701, -6.834e-05, -84.49796104, -0.00020503, -281.65987014, -0.00068344, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 112.66394806, 0.01387115, 112.66394806, 0.04161345, 78.86476364, -1104.61505991, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 28.16598701, 6.834e-05, 84.49796104, 0.00020503, 281.65987014, 0.00068344, -28.16598701, -6.834e-05, -84.49796104, -0.00020503, -281.65987014, -0.00068344, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 16.25, 14.6, 6.05)
    ops.node(123020, 16.25, 14.6, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 27744747.66448511, 11560311.5268688, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 47.97622686, 0.00092078, 57.276787, 0.01750409, 5.7276787, 0.04463039, -47.97622686, -0.00092078, -57.276787, -0.01750409, -5.7276787, -0.04463039, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 47.97622686, 0.00092078, 57.276787, 0.01750409, 5.7276787, 0.04463039, -47.97622686, -0.00092078, -57.276787, -0.01750409, -5.7276787, -0.04463039, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 72.47979277, 0.0184156, 72.47979277, 0.05524679, 50.73585494, -896.40896674, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 18.11994819, 8.577e-05, 54.35984458, 0.00025731, 181.19948193, 0.0008577, -18.11994819, -8.577e-05, -54.35984458, -0.00025731, -181.19948193, -0.0008577, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 72.47979277, 0.0184156, 72.47979277, 0.05524679, 50.73585494, -896.40896674, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 18.11994819, 8.577e-05, 54.35984458, 0.00025731, 181.19948193, 0.0008577, -18.11994819, -8.577e-05, -54.35984458, -0.00025731, -181.19948193, -0.0008577, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 0.0, 18.25, 6.05)
    ops.node(123021, 0.0, 18.25, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 27358059.12289379, 11399191.30120574, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 27.96509628, 0.00081364, 33.77544219, 0.01971355, 3.37754422, 0.06269588, -27.96509628, -0.00081364, -33.77544219, -0.01971355, -3.37754422, -0.06269588, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 27.96509628, 0.00081364, 33.77544219, 0.01971355, 3.37754422, 0.06269588, -27.96509628, -0.00081364, -33.77544219, -0.01971355, -3.37754422, -0.06269588, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 66.48050846, 0.01627279, 66.48050846, 0.04881837, 46.53635592, -820.68808218, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 16.62012711, 7.978e-05, 49.86038134, 0.00023935, 166.20127114, 0.00079782, -16.62012711, -7.978e-05, -49.86038134, -0.00023935, -166.20127114, -0.00079782, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 66.48050846, 0.01627279, 66.48050846, 0.04881837, 46.53635592, -820.68808218, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 16.62012711, 7.978e-05, 49.86038134, 0.00023935, 166.20127114, 0.00079782, -16.62012711, -7.978e-05, -49.86038134, -0.00023935, -166.20127114, -0.00079782, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 2.95, 18.25, 6.05)
    ops.node(123022, 2.95, 18.25, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.1225, 27205570.22213296, 11335654.25922207, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 84.09611534, 0.00064076, 101.58904226, 0.01813746, 10.15890423, 0.04712565, -84.09611534, -0.00064076, -101.58904226, -0.01813746, -10.15890423, -0.04712565, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 80.16862401, 0.00064076, 96.84458907, 0.01813746, 9.68445891, 0.04712565, -80.16862401, -0.00064076, -96.84458907, -0.01813746, -9.68445891, -0.04712565, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 111.05029958, 0.01281522, 111.05029958, 0.03844566, 77.73520971, -1112.85110566, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 27.7625749, 6.838e-05, 83.28772469, 0.00020513, 277.62574896, 0.00068376, -27.7625749, -6.838e-05, -83.28772469, -0.00020513, -277.62574896, -0.00068376, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 111.05029958, 0.01281522, 111.05029958, 0.03844566, 77.73520971, -1112.85110566, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 27.7625749, 6.838e-05, 83.28772469, 0.00020513, 277.62574896, 0.00068376, -27.7625749, -6.838e-05, -83.28772469, -0.00020513, -277.62574896, -0.00068376, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 9.6, 18.25, 6.05)
    ops.node(123023, 9.6, 18.25, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 27498258.771178, 11457607.82132417, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 106.47405183, 0.00069067, 127.93141619, 0.01510046, 12.79314162, 0.03592644, -106.47405183, -0.00069067, -127.93141619, -0.01510046, -12.79314162, -0.03592644, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 106.47405183, 0.00069067, 127.93141619, 0.01510046, 12.79314162, 0.03592644, -106.47405183, -0.00069067, -127.93141619, -0.01510046, -12.79314162, -0.03592644, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 112.13141145, 0.01381341, 112.13141145, 0.04144022, 78.49198802, -1102.66338335, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 28.03285286, 6.831e-05, 84.09855859, 0.00020492, 280.32852863, 0.00068307, -28.03285286, -6.831e-05, -84.09855859, -0.00020492, -280.32852863, -0.00068307, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 112.13141145, 0.01381341, 112.13141145, 0.04144022, 78.49198802, -1102.66338335, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 28.03285286, 6.831e-05, 84.09855859, 0.00020492, 280.32852863, 0.00068307, -28.03285286, -6.831e-05, -84.09855859, -0.00020492, -280.32852863, -0.00068307, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 16.25, 18.25, 6.05)
    ops.node(123024, 16.25, 18.25, 8.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 28548679.90146926, 11895283.29227886, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 48.27661248, 0.00091854, 57.65130835, 0.01779589, 5.76513083, 0.04686235, -48.27661248, -0.00091854, -57.65130835, -0.01779589, -5.76513083, -0.04686235, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 48.27661248, 0.00091854, 57.65130835, 0.01779589, 5.76513083, 0.04686235, -48.27661248, -0.00091854, -57.65130835, -0.01779589, -5.76513083, -0.04686235, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 73.92446767, 0.0183707, 73.92446767, 0.05511211, 51.74712737, -897.96600678, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 18.48111692, 8.502e-05, 55.44335075, 0.00025505, 184.81116917, 0.00085016, -18.48111692, -8.502e-05, -55.44335075, -0.00025505, -184.81116917, -0.00085016, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 73.92446767, 0.0183707, 73.92446767, 0.05511211, 51.74712737, -897.96600678, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 18.48111692, 8.502e-05, 55.44335075, 0.00025505, 184.81116917, 0.00085016, -18.48111692, -8.502e-05, -55.44335075, -0.00025505, -184.81116917, -0.00085016, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172025, 0.0, 21.9, 6.0)
    ops.node(123025, 0.0, 21.9, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2025, 172025, 123025, 0.0625, 28268445.41777076, 11778518.92407115, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22025, 23.17305558, 0.00078015, 28.09509588, 0.02138807, 2.80950959, 0.07290584, -23.17305558, -0.00078015, -28.09509588, -0.02138807, -2.80950959, -0.07290584, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12025, 23.17305558, 0.00078015, 28.09509588, 0.02138807, 2.80950959, 0.07290584, -23.17305558, -0.00078015, -28.09509588, -0.02138807, -2.80950959, -0.07290584, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22025, 2025, 0.0, 64.8078876, 0.01560294, 64.8078876, 0.04680882, 45.36552132, -837.49362661, 0.05, 2, 0, 72025, 23025, 2, 3)
    ops.uniaxialMaterial('LimitState', 42025, 16.2019719, 7.527e-05, 48.6059157, 0.00022581, 162.01971901, 0.0007527, -16.2019719, -7.527e-05, -48.6059157, -0.00022581, -162.01971901, -0.0007527, 0.4, 0.3, 0.003, 0.0, 0.0, 22025, 2)
    ops.limitCurve('ThreePoint', 12025, 2025, 0.0, 64.8078876, 0.01560294, 64.8078876, 0.04680882, 45.36552132, -837.49362661, 0.05, 2, 0, 72025, 23025, 1, 3)
    ops.uniaxialMaterial('LimitState', 32025, 16.2019719, 7.527e-05, 48.6059157, 0.00022581, 162.01971901, 0.0007527, -16.2019719, -7.527e-05, -48.6059157, -0.00022581, -162.01971901, -0.0007527, 0.4, 0.3, 0.003, 0.0, 0.0, 12025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2025, 99999, 'P', 42025, 'Vy', 32025, 'Vz', 22025, 'My', 12025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172025, 72025, 172025, 2025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123025, 123025, 23025, 2025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172026, 2.95, 21.9, 6.0)
    ops.node(123026, 2.95, 21.9, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2026, 172026, 123026, 0.0625, 27481665.46781997, 11450693.94492499, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22026, 35.92382563, 0.00086974, 43.03703388, 0.01785415, 4.30370339, 0.05189782, -35.92382563, -0.00086974, -43.03703388, -0.01785415, -4.30370339, -0.05189782, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12026, 35.92382563, 0.00086974, 43.03703388, 0.01785415, 4.30370339, 0.05189782, -35.92382563, -0.00086974, -43.03703388, -0.01785415, -4.30370339, -0.05189782, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22026, 2026, 0.0, 73.47494546, 0.01739479, 73.47494546, 0.05218438, 51.43246182, -932.52491041, 0.05, 2, 0, 72026, 23026, 2, 3)
    ops.uniaxialMaterial('LimitState', 42026, 18.36873636, 8.778e-05, 55.10620909, 0.00026334, 183.68736364, 0.0008778, -18.36873636, -8.778e-05, -55.10620909, -0.00026334, -183.68736364, -0.0008778, 0.4, 0.3, 0.003, 0.0, 0.0, 22026, 2)
    ops.limitCurve('ThreePoint', 12026, 2026, 0.0, 73.47494546, 0.01739479, 73.47494546, 0.05218438, 51.43246182, -932.52491041, 0.05, 2, 0, 72026, 23026, 1, 3)
    ops.uniaxialMaterial('LimitState', 32026, 18.36873636, 8.778e-05, 55.10620909, 0.00026334, 183.68736364, 0.0008778, -18.36873636, -8.778e-05, -55.10620909, -0.00026334, -183.68736364, -0.0008778, 0.4, 0.3, 0.003, 0.0, 0.0, 12026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2026, 99999, 'P', 42026, 'Vy', 32026, 'Vz', 22026, 'My', 12026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172026, 72026, 172026, 2026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123026, 123026, 23026, 2026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172027, 9.6, 21.9, 6.0)
    ops.node(123027, 9.6, 21.9, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2027, 172027, 123027, 0.1225, 25944895.63551983, 10810373.1814666, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22027, 83.81177207, 0.00064799, 101.06228331, 0.01684187, 10.10622833, 0.04563112, -83.81177207, -0.00064799, -101.06228331, -0.01684187, -10.10622833, -0.04563112, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12027, 75.85170317, 0.00064799, 91.46383767, 0.01684187, 9.14638377, 0.04563112, -75.85170317, -0.00064799, -91.46383767, -0.01684187, -9.14638377, -0.04563112, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22027, 2027, 0.0, 114.21982504, 0.0129597, 114.21982504, 0.03887911, 79.95387753, -1285.82159203, 0.05, 2, 0, 72027, 23027, 2, 3)
    ops.uniaxialMaterial('LimitState', 42027, 28.55495626, 7.374e-05, 85.66486878, 0.00022123, 285.54956261, 0.00073745, -28.55495626, -7.374e-05, -85.66486878, -0.00022123, -285.54956261, -0.00073745, 0.4, 0.3, 0.003, 0.0, 0.0, 22027, 2)
    ops.limitCurve('ThreePoint', 12027, 2027, 0.0, 114.21982504, 0.0129597, 114.21982504, 0.03887911, 79.95387753, -1285.82159203, 0.05, 2, 0, 72027, 23027, 1, 3)
    ops.uniaxialMaterial('LimitState', 32027, 28.55495626, 7.374e-05, 85.66486878, 0.00022123, 285.54956261, 0.00073745, -28.55495626, -7.374e-05, -85.66486878, -0.00022123, -285.54956261, -0.00073745, 0.4, 0.3, 0.003, 0.0, 0.0, 12027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2027, 99999, 'P', 42027, 'Vy', 32027, 'Vz', 22027, 'My', 12027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172027, 72027, 172027, 2027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123027, 123027, 23027, 2027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172028, 16.25, 21.9, 6.0)
    ops.node(123028, 16.25, 21.9, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2028, 172028, 123028, 0.0625, 28437746.00914134, 11849060.83714222, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22028, 42.19648463, 0.00085952, 50.76833571, 0.02078705, 5.07683357, 0.06231466, -42.19648463, -0.00085952, -50.76833571, -0.02078705, -5.07683357, -0.06231466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12028, 37.49431539, 0.00085952, 45.11096143, 0.02078705, 4.51109614, 0.06231466, -37.49431539, -0.00085952, -45.11096143, -0.02078705, -4.51109614, -0.06231466, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22028, 2028, 0.0, 72.07939917, 0.01719042, 72.07939917, 0.05157127, 50.45557942, -879.20890371, 0.05, 2, 0, 72028, 23028, 2, 3)
    ops.uniaxialMaterial('LimitState', 42028, 18.01984979, 8.322e-05, 54.05954938, 0.00024965, 180.19849794, 0.00083217, -18.01984979, -8.322e-05, -54.05954938, -0.00024965, -180.19849794, -0.00083217, 0.4, 0.3, 0.003, 0.0, 0.0, 22028, 2)
    ops.limitCurve('ThreePoint', 12028, 2028, 0.0, 72.07939917, 0.01719042, 72.07939917, 0.05157127, 50.45557942, -879.20890371, 0.05, 2, 0, 72028, 23028, 1, 3)
    ops.uniaxialMaterial('LimitState', 32028, 18.01984979, 8.322e-05, 54.05954938, 0.00024965, 180.19849794, 0.00083217, -18.01984979, -8.322e-05, -54.05954938, -0.00024965, -180.19849794, -0.00083217, 0.4, 0.3, 0.003, 0.0, 0.0, 12028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2028, 99999, 'P', 42028, 'Vy', 32028, 'Vz', 22028, 'My', 12028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172028, 72028, 172028, 2028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123028, 123028, 23028, 2028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.6, 0.0, 8.85)
    ops.node(124003, 9.6, 0.0, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.1225, 27229633.27405487, 11345680.5308562, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 54.76848121, 0.00060874, 66.75727339, 0.02062022, 6.67572734, 0.06385513, -54.76848121, -0.00060874, -66.75727339, -0.02062022, -6.67572734, -0.06385513, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 48.08194716, 0.00060874, 58.6070605, 0.02062022, 5.86070605, 0.06385513, -48.08194716, -0.00060874, -58.6070605, -0.02062022, -5.86070605, -0.06385513, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 103.22890936, 0.01217473, 103.22890936, 0.03652418, 72.26023656, -1231.93941393, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 25.80722734, 6.35e-05, 77.42168202, 0.00019051, 258.07227341, 0.00063504, -25.80722734, -6.35e-05, -77.42168202, -0.00019051, -258.07227341, -0.00063504, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 103.22890936, 0.01217473, 103.22890936, 0.03652418, 72.26023656, -1231.93941393, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 25.80722734, 6.35e-05, 77.42168202, 0.00019051, 258.07227341, 0.00063504, -25.80722734, -6.35e-05, -77.42168202, -0.00019051, -258.07227341, -0.00063504, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 16.25, 0.0, 8.85)
    ops.node(124004, 16.25, 0.0, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 27910660.76253617, 11629441.98439007, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 27.61036219, 0.00078572, 33.6126524, 0.02283038, 3.36126524, 0.07196941, -27.61036219, -0.00078572, -33.6126524, -0.02283038, -3.36126524, -0.07196941, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 27.61036219, 0.00078572, 33.6126524, 0.02283038, 3.36126524, 0.07196941, -27.61036219, -0.00078572, -33.6126524, -0.02283038, -3.36126524, -0.07196941, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 53.02880886, 0.0157144, 53.02880886, 0.04714319, 37.1201662, -712.41086216, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 13.25720222, 6.238e-05, 39.77160665, 0.00018714, 132.57202215, 0.00062379, -13.25720222, -6.238e-05, -39.77160665, -0.00018714, -132.57202215, -0.00062379, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 53.02880886, 0.0157144, 53.02880886, 0.04714319, 37.1201662, -712.41086216, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 13.25720222, 6.238e-05, 39.77160665, 0.00018714, 132.57202215, 0.00062379, -13.25720222, -6.238e-05, -39.77160665, -0.00018714, -132.57202215, -0.00062379, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 3.65, 8.9)
    ops.node(124005, 0.0, 3.65, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 26159882.08283219, 10899950.86784675, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 18.34773747, 0.00078524, 22.39733369, 0.02327233, 2.23973337, 0.07775594, -18.34773747, -0.00078524, -22.39733369, -0.02327233, -2.23973337, -0.07775594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 18.34773747, 0.00078524, 22.39733369, 0.02327233, 2.23973337, 0.07775594, -18.34773747, -0.00078524, -22.39733369, -0.02327233, -2.23973337, -0.07775594, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 58.27177565, 0.01570483, 58.27177565, 0.04711449, 40.79024296, -960.24604859, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 14.56794391, 7.313e-05, 43.70383174, 0.0002194, 145.67943914, 0.00073134, -14.56794391, -7.313e-05, -43.70383174, -0.0002194, -145.67943914, -0.00073134, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 58.27177565, 0.01570483, 58.27177565, 0.04711449, 40.79024296, -960.24604859, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 14.56794391, 7.313e-05, 43.70383174, 0.0002194, 145.67943914, 0.00073134, -14.56794391, -7.313e-05, -43.70383174, -0.0002194, -145.67943914, -0.00073134, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 2.95, 3.65, 8.9)
    ops.node(124006, 2.95, 3.65, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1225, 28086811.52729093, 11702838.13637122, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 71.57853406, 0.00063321, 87.0177163, 0.01853227, 8.70177163, 0.04937564, -71.57853406, -0.00063321, -87.0177163, -0.01853227, -8.70177163, -0.04937564, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 71.57853406, 0.00063321, 87.0177163, 0.01853227, 8.70177163, 0.04937564, -71.57853406, -0.00063321, -87.0177163, -0.01853227, -8.70177163, -0.04937564, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 94.6804111, 0.01266424, 94.6804111, 0.03799272, 66.27628777, -753.95833936, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 23.67010278, 5.647e-05, 71.01030833, 0.0001694, 236.70102775, 0.00056468, -23.67010278, -5.647e-05, -71.01030833, -0.0001694, -236.70102775, -0.00056468, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 94.6804111, 0.01266424, 94.6804111, 0.03799272, 66.27628777, -753.95833936, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 23.67010278, 5.647e-05, 71.01030833, 0.0001694, 236.70102775, 0.00056468, -23.67010278, -5.647e-05, -71.01030833, -0.0001694, -236.70102775, -0.00056468, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 9.6, 3.65, 8.9)
    ops.node(124007, 9.6, 3.65, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 27499623.79075484, 11458176.57948118, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 76.31100476, 0.00064435, 92.66562778, 0.01776789, 9.26656278, 0.04632487, -76.31100476, -0.00064435, -92.66562778, -0.01776789, -9.26656278, -0.04632487, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 76.31100476, 0.00064435, 92.66562778, 0.01776789, 9.26656278, 0.04632487, -76.31100476, -0.00064435, -92.66562778, -0.01776789, -9.26656278, -0.04632487, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 96.64704835, 0.01288691, 96.64704835, 0.03866074, 67.65293385, -805.24887904, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 24.16176209, 5.887e-05, 72.48528627, 0.00017661, 241.61762088, 0.00058871, -24.16176209, -5.887e-05, -72.48528627, -0.00017661, -241.61762088, -0.00058871, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 96.64704835, 0.01288691, 96.64704835, 0.03866074, 67.65293385, -805.24887904, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 24.16176209, 5.887e-05, 72.48528627, 0.00017661, 241.61762088, 0.00058871, -24.16176209, -5.887e-05, -72.48528627, -0.00017661, -241.61762088, -0.00058871, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 16.25, 3.65, 8.9)
    ops.node(124008, 16.25, 3.65, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 27730299.67653756, 11554291.53189065, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 32.47634299, 0.00082877, 39.3671205, 0.02135401, 3.93671205, 0.06402062, -32.47634299, -0.00082877, -39.3671205, -0.02135401, -3.93671205, -0.06402062, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 32.47634299, 0.00082877, 39.3671205, 0.02135401, 3.93671205, 0.06402062, -32.47634299, -0.00082877, -39.3671205, -0.02135401, -3.93671205, -0.06402062, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 57.19820397, 0.0165754, 57.19820397, 0.04972619, 40.03874278, -678.02054318, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 14.29955099, 6.772e-05, 42.89865298, 0.00020316, 142.99550993, 0.00067721, -14.29955099, -6.772e-05, -42.89865298, -0.00020316, -142.99550993, -0.00067721, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 57.19820397, 0.0165754, 57.19820397, 0.04972619, 40.03874278, -678.02054318, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 14.29955099, 6.772e-05, 42.89865298, 0.00020316, 142.99550993, 0.00067721, -14.29955099, -6.772e-05, -42.89865298, -0.00020316, -142.99550993, -0.00067721, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 7.3, 8.9)
    ops.node(124009, 0.0, 7.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 27558125.32389544, 11482552.21828977, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 18.21688814, 0.00075629, 22.20735556, 0.02264864, 2.22073556, 0.08017467, -18.21688814, -0.00075629, -22.20735556, -0.02264864, -2.22073556, -0.08017467, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 18.21688814, 0.00075629, 22.20735556, 0.02264864, 2.22073556, 0.08017467, -18.21688814, -0.00075629, -22.20735556, -0.02264864, -2.22073556, -0.08017467, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 58.83124701, 0.01512586, 58.83124701, 0.04537758, 41.18187291, -944.85862776, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 14.70781175, 7.009e-05, 44.12343526, 0.00021027, 147.07811754, 0.0007009, -14.70781175, -7.009e-05, -44.12343526, -0.00021027, -147.07811754, -0.0007009, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 58.83124701, 0.01512586, 58.83124701, 0.04537758, 41.18187291, -944.85862776, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 14.70781175, 7.009e-05, 44.12343526, 0.00021027, 147.07811754, 0.0007009, -14.70781175, -7.009e-05, -44.12343526, -0.00021027, -147.07811754, -0.0007009, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 2.95, 7.3, 8.9)
    ops.node(124010, 2.95, 7.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 27419561.66541083, 11424817.36058785, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 61.14592657, 0.00061851, 74.44037538, 0.02019273, 7.44403754, 0.05728113, -61.14592657, -0.00061851, -74.44037538, -0.02019273, -7.44403754, -0.05728113, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 57.82611302, 0.00061851, 70.39876245, 0.02019273, 7.03987625, 0.05728113, -57.82611302, -0.00061851, -70.39876245, -0.02019273, -7.03987625, -0.05728113, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 98.85857296, 0.01237028, 98.85857296, 0.03711083, 69.20100107, -971.29437518, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 24.71464324, 6.039e-05, 74.14392972, 0.00018118, 247.14643239, 0.00060394, -24.71464324, -6.039e-05, -74.14392972, -0.00018118, -247.14643239, -0.00060394, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 98.85857296, 0.01237028, 98.85857296, 0.03711083, 69.20100107, -971.29437518, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 24.71464324, 6.039e-05, 74.14392972, 0.00018118, 247.14643239, 0.00060394, -24.71464324, -6.039e-05, -74.14392972, -0.00018118, -247.14643239, -0.00060394, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 9.6, 7.3, 8.9)
    ops.node(124011, 9.6, 7.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 27843225.51297492, 11601343.96373955, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 76.67422099, 0.000652, 93.0630626, 0.0176175, 9.30630626, 0.04649106, -76.67422099, -0.000652, -93.0630626, -0.0176175, -9.30630626, -0.04649106, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 76.67422099, 0.000652, 93.0630626, 0.0176175, 9.30630626, 0.04649106, -76.67422099, -0.000652, -93.0630626, -0.0176175, -9.30630626, -0.04649106, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 97.43921663, 0.01303997, 97.43921663, 0.0391199, 68.20745164, -794.23379773, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 24.35980416, 5.862e-05, 73.07941247, 0.00017586, 243.59804158, 0.00058621, -24.35980416, -5.862e-05, -73.07941247, -0.00017586, -243.59804158, -0.00058621, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 97.43921663, 0.01303997, 97.43921663, 0.0391199, 68.20745164, -794.23379773, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 24.35980416, 5.862e-05, 73.07941247, 0.00017586, 243.59804158, 0.00058621, -24.35980416, -5.862e-05, -73.07941247, -0.00017586, -243.59804158, -0.00058621, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 16.25, 7.3, 8.9)
    ops.node(124012, 16.25, 7.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 29385691.93850982, 12244038.30771242, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 32.54570873, 0.00082946, 39.35129062, 0.0213555, 3.93512906, 0.06639299, -32.54570873, -0.00082946, -39.35129062, -0.0213555, -3.93512906, -0.06639299, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 32.54570873, 0.00082946, 39.35129062, 0.0213555, 3.93512906, 0.06639299, -32.54570873, -0.00082946, -39.35129062, -0.0213555, -3.93512906, -0.06639299, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 60.53543435, 0.01658922, 60.53543435, 0.04976766, 42.37480405, -678.33858511, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 15.13385859, 6.763e-05, 45.40157576, 0.0002029, 151.33858588, 0.00067635, -15.13385859, -6.763e-05, -45.40157576, -0.0002029, -151.33858588, -0.00067635, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 60.53543435, 0.01658922, 60.53543435, 0.04976766, 42.37480405, -678.33858511, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 15.13385859, 6.763e-05, 45.40157576, 0.0002029, 151.33858588, 0.00067635, -15.13385859, -6.763e-05, -45.40157576, -0.0002029, -151.33858588, -0.00067635, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 10.95, 8.9)
    ops.node(124013, 0.0, 10.95, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 26746104.96671351, 11144210.40279729, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 18.05288411, 0.00074927, 22.03743894, 0.02349405, 2.20374389, 0.0801129, -18.05288411, -0.00074927, -22.03743894, -0.02349405, -2.20374389, -0.0801129, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 18.05288411, 0.00074927, 22.03743894, 0.02349405, 2.20374389, 0.0801129, -18.05288411, -0.00074927, -22.03743894, -0.02349405, -2.20374389, -0.0801129, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 58.68104884, 0.01498547, 58.68104884, 0.04495642, 41.07673419, -1012.79468856, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 14.67026221, 7.203e-05, 44.01078663, 0.0002161, 146.70262209, 0.00072034, -14.67026221, -7.203e-05, -44.01078663, -0.0002161, -146.70262209, -0.00072034, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 58.68104884, 0.01498547, 58.68104884, 0.04495642, 41.07673419, -1012.79468856, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 14.67026221, 7.203e-05, 44.01078663, 0.0002161, 146.70262209, 0.00072034, -14.67026221, -7.203e-05, -44.01078663, -0.0002161, -146.70262209, -0.00072034, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 2.95, 10.95, 8.9)
    ops.node(124014, 2.95, 10.95, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1225, 27334418.72312696, 11389341.13463623, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 62.08987595, 0.0006071, 75.59955487, 0.02028091, 7.55995549, 0.05729153, -62.08987595, -0.0006071, -75.59955487, -0.02028091, -7.55995549, -0.05729153, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 58.5362567, 0.0006071, 71.27272978, 0.02028091, 7.12727298, 0.05729153, -58.5362567, -0.0006071, -71.27272978, -0.02028091, -7.12727298, -0.05729153, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 98.21887952, 0.01214208, 98.21887952, 0.03642625, 68.75321567, -959.86693003, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 24.55471988, 6.019e-05, 73.66415964, 0.00018057, 245.54719881, 0.0006019, -24.55471988, -6.019e-05, -73.66415964, -0.00018057, -245.54719881, -0.0006019, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 98.21887952, 0.01214208, 98.21887952, 0.03642625, 68.75321567, -959.86693003, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 24.55471988, 6.019e-05, 73.66415964, 0.00018057, 245.54719881, 0.0006019, -24.55471988, -6.019e-05, -73.66415964, -0.00018057, -245.54719881, -0.0006019, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.6, 10.95, 8.9)
    ops.node(124015, 9.6, 10.95, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 26333446.51420285, 10972269.38091785, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 75.96658737, 0.00065858, 92.36288206, 0.01749093, 9.23628821, 0.04486644, -75.96658737, -0.00065858, -92.36288206, -0.01749093, -9.23628821, -0.04486644, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 75.96658737, 0.00065858, 92.36288206, 0.01749093, 9.23628821, 0.04486644, -75.96658737, -0.00065858, -92.36288206, -0.01749093, -9.23628821, -0.04486644, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 91.73506866, 0.01317153, 91.73506866, 0.03951458, 64.21454806, -783.45113688, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 22.93376716, 5.835e-05, 68.80130149, 0.00017506, 229.33767164, 0.00058354, -22.93376716, -5.835e-05, -68.80130149, -0.00017506, -229.33767164, -0.00058354, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 91.73506866, 0.01317153, 91.73506866, 0.03951458, 64.21454806, -783.45113688, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 22.93376716, 5.835e-05, 68.80130149, 0.00017506, 229.33767164, 0.00058354, -22.93376716, -5.835e-05, -68.80130149, -0.00017506, -229.33767164, -0.00058354, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 16.25, 10.95, 8.9)
    ops.node(124016, 16.25, 10.95, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 28272746.168736, 11780310.90364, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 31.97564219, 0.00087398, 38.73246311, 0.02122216, 3.87324631, 0.06471774, -31.97564219, -0.00087398, -38.73246311, -0.02122216, -3.87324631, -0.06471774, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 31.97564219, 0.00087398, 38.73246311, 0.02122216, 3.87324631, 0.06471774, -31.97564219, -0.00087398, -38.73246311, -0.02122216, -3.87324631, -0.06471774, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 57.45336324, 0.01747966, 57.45336324, 0.05243899, 40.21735427, -663.95826315, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 14.36334081, 6.672e-05, 43.09002243, 0.00020015, 143.63340811, 0.00066718, -14.36334081, -6.672e-05, -43.09002243, -0.00020015, -143.63340811, -0.00066718, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 57.45336324, 0.01747966, 57.45336324, 0.05243899, 40.21735427, -663.95826315, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 14.36334081, 6.672e-05, 43.09002243, 0.00020015, 143.63340811, 0.00066718, -14.36334081, -6.672e-05, -43.09002243, -0.00020015, -143.63340811, -0.00066718, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 14.6, 8.9)
    ops.node(124017, 0.0, 14.6, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 28076030.86234329, 11698346.19264304, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 17.89378611, 0.00073517, 21.79225462, 0.0226909, 2.17922546, 0.0807442, -17.89378611, -0.00073517, -21.79225462, -0.0226909, -2.17922546, -0.0807442, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 17.89378611, 0.00073517, 21.79225462, 0.0226909, 2.17922546, 0.0807442, -17.89378611, -0.00073517, -21.79225462, -0.0226909, -2.17922546, -0.0807442, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 59.62266053, 0.01470348, 59.62266053, 0.04411045, 41.73586237, -938.14286827, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 14.90566513, 6.972e-05, 44.71699539, 0.00020917, 149.05665131, 0.00069723, -14.90566513, -6.972e-05, -44.71699539, -0.00020917, -149.05665131, -0.00069723, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 59.62266053, 0.01470348, 59.62266053, 0.04411045, 41.73586237, -938.14286827, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 14.90566513, 6.972e-05, 44.71699539, 0.00020917, 149.05665131, 0.00069723, -14.90566513, -6.972e-05, -44.71699539, -0.00020917, -149.05665131, -0.00069723, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 2.95, 14.6, 8.9)
    ops.node(124018, 2.95, 14.6, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1225, 27086421.4415645, 11286008.93398521, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 61.20136818, 0.00061183, 74.54539423, 0.02009776, 7.45453942, 0.0568767, -61.20136818, -0.00061183, -74.54539423, -0.02009776, -7.45453942, -0.0568767, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 57.79805153, 0.00061183, 70.40003623, 0.02009776, 7.04000362, 0.0568767, -57.79805153, -0.00061183, -70.40003623, -0.02009776, -7.04000362, -0.0568767, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 97.17034749, 0.01223668, 97.17034749, 0.03671004, 68.01924325, -953.56701132, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 24.29258687, 6.009e-05, 72.87776062, 0.00018028, 242.92586874, 0.00060093, -24.29258687, -6.009e-05, -72.87776062, -0.00018028, -242.92586874, -0.00060093, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 97.17034749, 0.01223668, 97.17034749, 0.03671004, 68.01924325, -953.56701132, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 24.29258687, 6.009e-05, 72.87776062, 0.00018028, 242.92586874, 0.00060093, -24.29258687, -6.009e-05, -72.87776062, -0.00018028, -242.92586874, -0.00060093, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 9.6, 14.6, 8.9)
    ops.node(124019, 9.6, 14.6, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1225, 27562041.95944459, 11484184.14976858, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 77.43550426, 0.00063972, 94.02342944, 0.0174666, 9.40234294, 0.0460821, -77.43550426, -0.00063972, -94.02342944, -0.0174666, -9.40234294, -0.0460821, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 77.43550426, 0.00063972, 94.02342944, 0.0174666, 9.40234294, 0.0460821, -77.43550426, -0.00063972, -94.02342944, -0.0174666, -9.40234294, -0.0460821, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 95.94752946, 0.01279436, 95.94752946, 0.03838308, 67.16327062, -781.51981145, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 23.98688236, 5.831e-05, 71.96064709, 0.00017494, 239.86882365, 0.00058313, -23.98688236, -5.831e-05, -71.96064709, -0.00017494, -239.86882365, -0.00058313, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 95.94752946, 0.01279436, 95.94752946, 0.03838308, 67.16327062, -781.51981145, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 23.98688236, 5.831e-05, 71.96064709, 0.00017494, 239.86882365, 0.00058313, -23.98688236, -5.831e-05, -71.96064709, -0.00017494, -239.86882365, -0.00058313, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 16.25, 14.6, 8.9)
    ops.node(124020, 16.25, 14.6, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 28044937.45338374, 11685390.60557656, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 32.54933284, 0.00082232, 39.43978374, 0.02163555, 3.94397837, 0.06478951, -32.54933284, -0.00082232, -39.43978374, -0.02163555, -3.94397837, -0.06478951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 32.54933284, 0.00082232, 39.43978374, 0.02163555, 3.94397837, 0.06478951, -32.54933284, -0.00082232, -39.43978374, -0.02163555, -3.94397837, -0.06478951, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 59.1327346, 0.01644644, 59.1327346, 0.04933932, 41.39291422, -683.94390416, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 14.78318365, 6.923e-05, 44.34955095, 0.00020768, 147.8318365, 0.00069226, -14.78318365, -6.923e-05, -44.34955095, -0.00020768, -147.8318365, -0.00069226, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 59.1327346, 0.01644644, 59.1327346, 0.04933932, 41.39291422, -683.94390416, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 14.78318365, 6.923e-05, 44.34955095, 0.00020768, 147.8318365, 0.00069226, -14.78318365, -6.923e-05, -44.34955095, -0.00020768, -147.8318365, -0.00069226, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 0.0, 18.25, 8.9)
    ops.node(124021, 0.0, 18.25, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 28085150.79333648, 11702146.1638902, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 18.29940983, 0.00074043, 22.28585244, 0.02285067, 2.22858524, 0.08091292, -18.29940983, -0.00074043, -22.28585244, -0.02285067, -2.22858524, -0.08091292, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 18.29940983, 0.00074043, 22.28585244, 0.02285067, 2.22858524, 0.08091292, -18.29940983, -0.00074043, -22.28585244, -0.02285067, -2.22858524, -0.08091292, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 60.35135511, 0.01480857, 60.35135511, 0.04442572, 42.24594857, -975.84077299, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 15.08783878, 7.055e-05, 45.26351633, 0.00021166, 150.87838776, 0.00070552, -15.08783878, -7.055e-05, -45.26351633, -0.00021166, -150.87838776, -0.00070552, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 60.35135511, 0.01480857, 60.35135511, 0.04442572, 42.24594857, -975.84077299, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 15.08783878, 7.055e-05, 45.26351633, 0.00021166, 150.87838776, 0.00070552, -15.08783878, -7.055e-05, -45.26351633, -0.00021166, -150.87838776, -0.00070552, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 2.95, 18.25, 8.9)
    ops.node(124022, 2.95, 18.25, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.1225, 26955228.12887306, 11231345.05369711, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 62.30574386, 0.00061303, 75.90483081, 0.02018218, 7.59048308, 0.05683541, -62.30574386, -0.00061303, -75.90483081, -0.02018218, -7.59048308, -0.05683541, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 58.73518831, 0.00061303, 71.55495232, 0.02018218, 7.15549523, 0.05683541, -58.73518831, -0.00061303, -71.55495232, -0.02018218, -7.15549523, -0.05683541, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 97.50684891, 0.01226054, 97.50684891, 0.03678163, 68.25479423, -979.77109754, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 24.37671223, 6.059e-05, 73.13013668, 0.00018178, 243.76712227, 0.00060595, -24.37671223, -6.059e-05, -73.13013668, -0.00018178, -243.76712227, -0.00060595, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 97.50684891, 0.01226054, 97.50684891, 0.03678163, 68.25479423, -979.77109754, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 24.37671223, 6.059e-05, 73.13013668, 0.00018178, 243.76712227, 0.00060595, -24.37671223, -6.059e-05, -73.13013668, -0.00018178, -243.76712227, -0.00060595, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 9.6, 18.25, 8.9)
    ops.node(124023, 9.6, 18.25, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 28738690.54415097, 11974454.39339624, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 75.63904772, 0.00065649, 91.67589878, 0.01760222, 9.16758988, 0.04724003, -75.63904772, -0.00065649, -91.67589878, -0.01760222, -9.16758988, -0.04724003, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 75.63904772, 0.00065649, 91.67589878, 0.01760222, 9.16758988, 0.04724003, -75.63904772, -0.00065649, -91.67589878, -0.01760222, -9.16758988, -0.04724003, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 100.16632923, 0.01312986, 100.16632923, 0.03938957, 70.11643046, -781.72069886, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 25.04158231, 5.838e-05, 75.12474692, 0.00017515, 250.41582307, 0.00058384, -25.04158231, -5.838e-05, -75.12474692, -0.00017515, -250.41582307, -0.00058384, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 100.16632923, 0.01312986, 100.16632923, 0.03938957, 70.11643046, -781.72069886, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 25.04158231, 5.838e-05, 75.12474692, 0.00017515, 250.41582307, 0.00058384, -25.04158231, -5.838e-05, -75.12474692, -0.00017515, -250.41582307, -0.00058384, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 16.25, 18.25, 8.9)
    ops.node(124024, 16.25, 18.25, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 28380725.09280906, 11825302.12200378, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 31.89970547, 0.00084955, 38.63444862, 0.02186297, 3.86344486, 0.06551726, -31.89970547, -0.00084955, -38.63444862, -0.02186297, -3.86344486, -0.06551726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 31.89970547, 0.00084955, 38.63444862, 0.02186297, 3.86344486, 0.06551726, -31.89970547, -0.00084955, -38.63444862, -0.02186297, -3.86344486, -0.06551726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 61.14986975, 0.01699095, 61.14986975, 0.05097286, 42.80490882, -698.58860424, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 15.28746744, 7.074e-05, 45.86240231, 0.00021222, 152.87467437, 0.00070741, -15.28746744, -7.074e-05, -45.86240231, -0.00021222, -152.87467437, -0.00070741, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 61.14986975, 0.01699095, 61.14986975, 0.05097286, 42.80490882, -698.58860424, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 15.28746744, 7.074e-05, 45.86240231, 0.00021222, 152.87467437, 0.00070741, -15.28746744, -7.074e-05, -45.86240231, -0.00021222, -152.87467437, -0.00070741, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173025, 0.0, 21.9, 8.85)
    ops.node(124025, 0.0, 21.9, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3025, 173025, 124025, 0.0625, 26829685.76651913, 11179035.73604964, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23025, 15.82215276, 0.0007281, 19.35815401, 0.02373591, 1.9358154, 0.0846526, -15.82215276, -0.0007281, -19.35815401, -0.02373591, -1.9358154, -0.0846526, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13025, 15.82215276, 0.0007281, 19.35815401, 0.02373591, 1.9358154, 0.0846526, -15.82215276, -0.0007281, -19.35815401, -0.02373591, -1.9358154, -0.0846526, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23025, 3025, 0.0, 56.12185064, 0.01456198, 56.12185064, 0.04368594, 39.28529545, -1304.12684147, 0.05, 2, 0, 73025, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 43025, 14.03046266, 6.868e-05, 42.09138798, 0.00020603, 140.30462659, 0.00068677, -14.03046266, -6.868e-05, -42.09138798, -0.00020603, -140.30462659, -0.00068677, 0.4, 0.3, 0.003, 0.0, 0.0, 23025, 2)
    ops.limitCurve('ThreePoint', 13025, 3025, 0.0, 56.12185064, 0.01456198, 56.12185064, 0.04368594, 39.28529545, -1304.12684147, 0.05, 2, 0, 73025, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 33025, 14.03046266, 6.868e-05, 42.09138798, 0.00020603, 140.30462659, 0.00068677, -14.03046266, -6.868e-05, -42.09138798, -0.00020603, -140.30462659, -0.00068677, 0.4, 0.3, 0.003, 0.0, 0.0, 13025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3025, 99999, 'P', 43025, 'Vy', 33025, 'Vz', 23025, 'My', 13025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173025, 73025, 173025, 3025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 3025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173026, 2.95, 21.9, 8.85)
    ops.node(124026, 2.95, 21.9, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3026, 173026, 124026, 0.0625, 28685284.4072923, 11952201.83637179, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23026, 21.67614127, 0.00075639, 26.29867654, 0.02161299, 2.62986765, 0.07595313, -21.67614127, -0.00075639, -26.29867654, -0.02161299, -2.62986765, -0.07595313, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13026, 21.67614127, 0.00075639, 26.29867654, 0.02161299, 2.62986765, 0.07595313, -21.67614127, -0.00075639, -26.29867654, -0.02161299, -2.62986765, -0.07595313, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23026, 3026, 0.0, 63.88110313, 0.01512783, 63.88110313, 0.0453835, 44.71677219, -846.23942847, 0.05, 2, 0, 73026, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 43026, 15.97027578, 7.312e-05, 47.91082735, 0.00021935, 159.70275782, 0.00073116, -15.97027578, -7.312e-05, -47.91082735, -0.00021935, -159.70275782, -0.00073116, 0.4, 0.3, 0.003, 0.0, 0.0, 23026, 2)
    ops.limitCurve('ThreePoint', 13026, 3026, 0.0, 63.88110313, 0.01512783, 63.88110313, 0.0453835, 44.71677219, -846.23942847, 0.05, 2, 0, 73026, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 33026, 15.97027578, 7.312e-05, 47.91082735, 0.00021935, 159.70275782, 0.00073116, -15.97027578, -7.312e-05, -47.91082735, -0.00021935, -159.70275782, -0.00073116, 0.4, 0.3, 0.003, 0.0, 0.0, 13026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3026, 99999, 'P', 43026, 'Vy', 33026, 'Vz', 23026, 'My', 13026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173026, 73026, 173026, 3026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 3026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173027, 9.6, 21.9, 8.85)
    ops.node(124027, 9.6, 21.9, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3027, 173027, 124027, 0.1225, 28300095.56479199, 11791706.48532999, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23027, 55.33099917, 0.00059114, 67.31421987, 0.01987129, 6.73142199, 0.06404831, -55.33099917, -0.00059114, -67.31421987, -0.01987129, -6.73142199, -0.06404831, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13027, 48.31462293, 0.00059114, 58.77828342, 0.01987129, 5.87782834, 0.06404831, -48.31462293, -0.00059114, -58.77828342, -0.01987129, -5.87782834, -0.06404831, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23027, 3027, 0.0, 105.75962075, 0.01182278, 105.75962075, 0.03546834, 74.03173453, -1184.00154063, 0.05, 2, 0, 73027, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 43027, 26.43990519, 6.26e-05, 79.31971557, 0.0001878, 264.39905188, 0.000626, -26.43990519, -6.26e-05, -79.31971557, -0.0001878, -264.39905188, -0.000626, 0.4, 0.3, 0.003, 0.0, 0.0, 23027, 2)
    ops.limitCurve('ThreePoint', 13027, 3027, 0.0, 105.75962075, 0.01182278, 105.75962075, 0.03546834, 74.03173453, -1184.00154063, 0.05, 2, 0, 73027, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 33027, 26.43990519, 6.26e-05, 79.31971557, 0.0001878, 264.39905188, 0.000626, -26.43990519, -6.26e-05, -79.31971557, -0.0001878, -264.39905188, -0.000626, 0.4, 0.3, 0.003, 0.0, 0.0, 13027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3027, 99999, 'P', 43027, 'Vy', 33027, 'Vz', 23027, 'My', 13027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173027, 73027, 173027, 3027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 3027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173028, 16.25, 21.9, 8.85)
    ops.node(124028, 16.25, 21.9, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3028, 173028, 124028, 0.0625, 28441322.78929318, 11850551.16220549, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23028, 25.05157038, 0.00075605, 30.46678205, 0.02306429, 3.0466782, 0.0803194, -25.05157038, -0.00075605, -30.46678205, -0.02306429, -3.0466782, -0.0803194, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13028, 22.86143761, 0.00075605, 27.80322456, 0.02306429, 2.78032246, 0.0803194, -22.86143761, -0.00075605, -27.80322456, -0.02306429, -2.78032246, -0.0803194, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23028, 3028, 0.0, 61.7852734, 0.01512103, 61.7852734, 0.0453631, 43.24969138, -933.63954845, 0.05, 2, 0, 73028, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 43028, 15.44631835, 7.132e-05, 46.33895505, 0.00021397, 154.4631835, 0.00071323, -15.44631835, -7.132e-05, -46.33895505, -0.00021397, -154.4631835, -0.00071323, 0.4, 0.3, 0.003, 0.0, 0.0, 23028, 2)
    ops.limitCurve('ThreePoint', 13028, 3028, 0.0, 61.7852734, 0.01512103, 61.7852734, 0.0453631, 43.24969138, -933.63954845, 0.05, 2, 0, 73028, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 33028, 15.44631835, 7.132e-05, 46.33895505, 0.00021397, 154.4631835, 0.00071323, -15.44631835, -7.132e-05, -46.33895505, -0.00021397, -154.4631835, -0.00071323, 0.4, 0.3, 0.003, 0.0, 0.0, 13028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3028, 99999, 'P', 43028, 'Vy', 33028, 'Vz', 23028, 'My', 13028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173028, 73028, 173028, 3028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 3028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124029, 0.0, 0.0, 1.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 170001, 124029, 0.0625, 27827136.18986971, 11594640.07911238, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 42.74458219, 0.00064105, 51.15591985, 0.01780164, 5.11559198, 0.05166047, -42.74458219, -0.00064105, -51.15591985, -0.01780164, -5.11559198, -0.05166047, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 40.23655521, 0.00064105, 48.15435988, 0.01780164, 4.81543599, 0.05166047, -40.23655521, -0.00064105, -48.15435988, -0.01780164, -4.81543599, -0.05166047, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 80.44418455, 0.01282105, 80.44418455, 0.03846314, 56.31092919, -1869.31303738, 0.05, 2, 0, 70001, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 20.11104614, 4.746e-05, 60.33313842, 0.00014237, 201.11046139, 0.00047456, -20.11104614, -4.746e-05, -60.33313842, -0.00014237, -201.11046139, -0.00047456, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 80.44418455, 0.01282105, 80.44418455, 0.03846314, 56.31092919, -1869.31303738, 0.05, 2, 0, 70001, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 20.11104614, 4.746e-05, 60.33313842, 0.00014237, 201.11046139, 0.00047456, -20.11104614, -4.746e-05, -60.33313842, -0.00014237, -201.11046139, -0.00047456, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 0.0, 0.0, 1.625)
    ops.node(121001, 0.0, 0.0, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 174029, 121001, 0.0625, 27103550.21355891, 11293145.92231621, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 33.95922609, 0.00060971, 40.76051698, 0.01824792, 4.0760517, 0.0533212, -33.95922609, -0.00060971, -40.76051698, -0.01824792, -4.0760517, -0.0533212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 33.95922609, 0.00060971, 40.76051698, 0.01824792, 4.0760517, 0.0533212, -33.95922609, -0.00060971, -40.76051698, -0.01824792, -4.0760517, -0.0533212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 77.41695396, 0.01219425, 77.41695396, 0.03658274, 54.19186777, -1837.0914553, 0.05, 2, 0, 74029, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 19.35423849, 4.689e-05, 58.06271547, 0.00014067, 193.54238491, 0.0004689, -19.35423849, -4.689e-05, -58.06271547, -0.00014067, -193.54238491, -0.0004689, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 77.41695396, 0.01219425, 77.41695396, 0.03658274, 54.19186777, -1837.0914553, 0.05, 2, 0, 74029, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 19.35423849, 4.689e-05, 58.06271547, 0.00014067, 193.54238491, 0.0004689, -19.35423849, -4.689e-05, -58.06271547, -0.00014067, -193.54238491, -0.0004689, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 2.95, 0.0, 0.0)
    ops.node(124030, 2.95, 0.0, 1.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 170002, 124030, 0.1225, 28921609.93262925, 12050670.80526219, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 138.21285579, 0.00054468, 164.73888101, 0.01621922, 16.4738881, 0.04141926, -138.21285579, -0.00054468, -164.73888101, -0.01621922, -16.4738881, -0.04141926, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 138.21285579, 0.00054468, 164.73888101, 0.01621922, 16.4738881, 0.04141926, -138.21285579, -0.00054468, -164.73888101, -0.01621922, -16.4738881, -0.04141926, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 204.24485984, 0.01089365, 204.24485984, 0.03268095, 142.97140189, -3345.86502883, 0.05, 2, 0, 70002, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 51.06121496, 5.915e-05, 153.18364488, 0.00017744, 510.6121496, 0.00059148, -51.06121496, -5.915e-05, -153.18364488, -0.00017744, -510.6121496, -0.00059148, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 204.24485984, 0.01089365, 204.24485984, 0.03268095, 142.97140189, -3345.86502883, 0.05, 2, 0, 70002, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 51.06121496, 5.915e-05, 153.18364488, 0.00017744, 510.6121496, 0.00059148, -51.06121496, -5.915e-05, -153.18364488, -0.00017744, -510.6121496, -0.00059148, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 2.95, 0.0, 1.625)
    ops.node(121002, 2.95, 0.0, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4077, 174030, 121002, 0.1225, 27930884.07718916, 11637868.36549548, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24077, 121.39526977, 0.00055276, 144.86846448, 0.0153325, 14.48684645, 0.03952616, -121.39526977, -0.00055276, -144.86846448, -0.0153325, -14.48684645, -0.03952616, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14077, 108.46706449, 0.00055276, 129.44043955, 0.0153325, 12.94404396, 0.03952616, -108.46706449, -0.00055276, -129.44043955, -0.0153325, -12.94404396, -0.03952616, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24077, 4077, 0.0, 195.27212097, 0.01105521, 195.27212097, 0.03316564, 136.69048468, -3267.98304109, 0.05, 2, 0, 74030, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44077, 48.81803024, 5.856e-05, 146.45409073, 0.00017567, 488.18030243, 0.00058555, -48.81803024, -5.856e-05, -146.45409073, -0.00017567, -488.18030243, -0.00058555, 0.4, 0.3, 0.003, 0.0, 0.0, 24077, 2)
    ops.limitCurve('ThreePoint', 14077, 4077, 0.0, 195.27212097, 0.01105521, 195.27212097, 0.03316564, 136.69048468, -3267.98304109, 0.05, 2, 0, 74030, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34077, 48.81803024, 5.856e-05, 146.45409073, 0.00017567, 488.18030243, 0.00058555, -48.81803024, -5.856e-05, -146.45409073, -0.00017567, -488.18030243, -0.00058555, 0.4, 0.3, 0.003, 0.0, 0.0, 14077, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4077, 99999, 'P', 44077, 'Vy', 34077, 'Vz', 24077, 'My', 14077, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4077, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4077, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.15)
    ops.node(124031, 0.0, 0.0, 4.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 171001, 124031, 0.0625, 27409256.71326834, 11420523.63052847, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 31.12347876, 0.00060607, 37.47399265, 0.01873597, 3.74739927, 0.0580763, -31.12347876, -0.00060607, -37.47399265, -0.01873597, -3.74739927, -0.0580763, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 31.12347876, 0.00060607, 37.47399265, 0.01873597, 3.74739927, 0.0580763, -31.12347876, -0.00060607, -37.47399265, -0.01873597, -3.74739927, -0.0580763, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 75.15833423, 0.01212136, 75.15833423, 0.03636409, 52.61083396, -1743.9888767, 0.05, 2, 0, 71001, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 18.78958356, 4.501e-05, 56.36875067, 0.00013504, 187.89583557, 0.00045014, -18.78958356, -4.501e-05, -56.36875067, -0.00013504, -187.89583557, -0.00045014, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 75.15833423, 0.01212136, 75.15833423, 0.03636409, 52.61083396, -1743.9888767, 0.05, 2, 0, 71001, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 18.78958356, 4.501e-05, 56.36875067, 0.00013504, 187.89583557, 0.00045014, -18.78958356, -4.501e-05, -56.36875067, -0.00013504, -187.89583557, -0.00045014, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 0.0, 0.0, 4.45)
    ops.node(122001, 0.0, 0.0, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 174031, 122001, 0.0625, 27215686.80873668, 11339869.50364028, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 27.85172256, 0.00059985, 33.64302016, 0.01990656, 3.36430202, 0.0626305, -27.85172256, -0.00059985, -33.64302016, -0.01990656, -3.36430202, -0.0626305, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 27.85172256, 0.00059985, 33.64302016, 0.01990656, 3.36430202, 0.0626305, -27.85172256, -0.00059985, -33.64302016, -0.01990656, -3.36430202, -0.0626305, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 72.0019058, 0.01199707, 72.0019058, 0.03599121, 50.40133406, -1683.72264284, 0.05, 2, 0, 74031, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 18.00047645, 4.343e-05, 54.00142935, 0.00013029, 180.00476451, 0.0004343, -18.00047645, -4.343e-05, -54.00142935, -0.00013029, -180.00476451, -0.0004343, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 72.0019058, 0.01199707, 72.0019058, 0.03599121, 50.40133406, -1683.72264284, 0.05, 2, 0, 74031, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 18.00047645, 4.343e-05, 54.00142935, 0.00013029, 180.00476451, 0.0004343, -18.00047645, -4.343e-05, -54.00142935, -0.00013029, -180.00476451, -0.0004343, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 2.95, 0.0, 3.15)
    ops.node(124032, 2.95, 0.0, 4.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 171002, 124032, 0.1225, 28896016.12061324, 12040006.71692218, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 97.63177847, 0.00052922, 117.11904445, 0.01656778, 11.71190445, 0.04702098, -97.63177847, -0.00052922, -117.11904445, -0.01656778, -11.71190445, -0.04702098, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 89.52286837, 0.00052922, 107.39159898, 0.01656778, 10.7391599, 0.04702098, -89.52286837, -0.00052922, -107.39159898, -0.01656778, -10.7391599, -0.04702098, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 188.24870309, 0.01058436, 188.24870309, 0.03175309, 131.77409216, -2877.63089293, 0.05, 2, 0, 71002, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 47.06217577, 5.456e-05, 141.18652732, 0.00016369, 470.62175772, 0.00054564, -47.06217577, -5.456e-05, -141.18652732, -0.00016369, -470.62175772, -0.00054564, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 188.24870309, 0.01058436, 188.24870309, 0.03175309, 131.77409216, -2877.63089293, 0.05, 2, 0, 71002, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 47.06217577, 5.456e-05, 141.18652732, 0.00016369, 470.62175772, 0.00054564, -47.06217577, -5.456e-05, -141.18652732, -0.00016369, -470.62175772, -0.00054564, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4081, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 2.95, 0.0, 4.45)
    ops.node(122002, 2.95, 0.0, 5.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4082, 174032, 122002, 0.1225, 27568356.38233837, 11486815.15930765, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24082, 92.47403142, 0.00053008, 111.15790408, 0.01677253, 11.11579041, 0.04601579, -92.47403142, -0.00053008, -111.15790408, -0.01677253, -11.11579041, -0.04601579, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14082, 84.51115612, 0.00053008, 101.58617334, 0.01677253, 10.15861733, 0.04601579, -84.51115612, -0.00053008, -101.58617334, -0.01677253, -10.15861733, -0.04601579, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24082, 4082, 0.0, 176.14035955, 0.01060167, 176.14035955, 0.03180502, 123.29825169, -2761.15137208, 0.05, 2, 0, 74032, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44082, 44.03508989, 5.351e-05, 132.10526966, 0.00016054, 440.35089888, 0.00053513, -44.03508989, -5.351e-05, -132.10526966, -0.00016054, -440.35089888, -0.00053513, 0.4, 0.3, 0.003, 0.0, 0.0, 24082, 2)
    ops.limitCurve('ThreePoint', 14082, 4082, 0.0, 176.14035955, 0.01060167, 176.14035955, 0.03180502, 123.29825169, -2761.15137208, 0.05, 2, 0, 74032, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34082, 44.03508989, 5.351e-05, 132.10526966, 0.00016054, 440.35089888, 0.00053513, -44.03508989, -5.351e-05, -132.10526966, -0.00016054, -440.35089888, -0.00053513, 0.4, 0.3, 0.003, 0.0, 0.0, 14082, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4082, 99999, 'P', 44082, 'Vy', 34082, 'Vz', 24082, 'My', 14082, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4082, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4082, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.0)
    ops.node(124033, 0.0, 0.0, 6.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4084, 172001, 124033, 0.0625, 27820501.19566289, 11591875.49819287, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24084, 25.23244712, 0.00058349, 30.55586576, 0.02083372, 3.05558658, 0.06892807, -25.23244712, -0.00058349, -30.55586576, -0.02083372, -3.05558658, -0.06892807, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14084, 25.23244712, 0.00058349, 30.55586576, 0.02083372, 3.05558658, 0.06892807, -25.23244712, -0.00058349, -30.55586576, -0.02083372, -3.05558658, -0.06892807, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24084, 4084, 0.0, 70.93674451, 0.01166973, 70.93674451, 0.03500918, 49.65572116, -1687.95289475, 0.05, 2, 0, 72001, 24033, 2, 3)
    ops.uniaxialMaterial('LimitState', 44084, 17.73418613, 4.186e-05, 53.20255838, 0.00012557, 177.34186127, 0.00041858, -17.73418613, -4.186e-05, -53.20255838, -0.00012557, -177.34186127, -0.00041858, 0.4, 0.3, 0.003, 0.0, 0.0, 24084, 2)
    ops.limitCurve('ThreePoint', 14084, 4084, 0.0, 70.93674451, 0.01166973, 70.93674451, 0.03500918, 49.65572116, -1687.95289475, 0.05, 2, 0, 72001, 24033, 1, 3)
    ops.uniaxialMaterial('LimitState', 34084, 17.73418613, 4.186e-05, 53.20255838, 0.00012557, 177.34186127, 0.00041858, -17.73418613, -4.186e-05, -53.20255838, -0.00012557, -177.34186127, -0.00041858, 0.4, 0.3, 0.003, 0.0, 0.0, 14084, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4084, 99999, 'P', 44084, 'Vy', 34084, 'Vz', 24084, 'My', 14084, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4084, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124033, 124033, 24033, 4084, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174033, 0.0, 0.0, 7.3)
    ops.node(123001, 0.0, 0.0, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4085, 174033, 123001, 0.0625, 27966393.21640042, 11652663.84016684, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24085, 21.21492997, 0.00056574, 25.77225836, 0.02194566, 2.57722584, 0.07537708, -21.21492997, -0.00056574, -25.77225836, -0.02194566, -2.57722584, -0.07537708, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14085, 21.21492997, 0.00056574, 25.77225836, 0.02194566, 2.57722584, 0.07537708, -21.21492997, -0.00056574, -25.77225836, -0.02194566, -2.57722584, -0.07537708, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24085, 4085, 0.0, 67.60591255, 0.01131485, 67.60591255, 0.03394454, 47.32413879, -1733.48149438, 0.05, 2, 0, 74033, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44085, 16.90147814, 3.968e-05, 50.70443441, 0.00011905, 169.01478138, 0.00039684, -16.90147814, -3.968e-05, -50.70443441, -0.00011905, -169.01478138, -0.00039684, 0.4, 0.3, 0.003, 0.0, 0.0, 24085, 2)
    ops.limitCurve('ThreePoint', 14085, 4085, 0.0, 67.60591255, 0.01131485, 67.60591255, 0.03394454, 47.32413879, -1733.48149438, 0.05, 2, 0, 74033, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34085, 16.90147814, 3.968e-05, 50.70443441, 0.00011905, 169.01478138, 0.00039684, -16.90147814, -3.968e-05, -50.70443441, -0.00011905, -169.01478138, -0.00039684, 0.4, 0.3, 0.003, 0.0, 0.0, 14085, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4085, 99999, 'P', 44085, 'Vy', 34085, 'Vz', 24085, 'My', 14085, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174033, 74033, 174033, 4085, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4085, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 2.95, 0.0, 6.0)
    ops.node(124034, 2.95, 0.0, 6.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4086, 172002, 124034, 0.0625, 28529230.14750068, 11887179.22812529, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24086, 39.73216387, 0.00063798, 47.4496749, 0.0169733, 4.74496749, 0.05049112, -39.73216387, -0.00063798, -47.4496749, -0.0169733, -4.74496749, -0.05049112, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14086, 39.73216387, 0.00063798, 47.4496749, 0.0169733, 4.74496749, 0.05049112, -39.73216387, -0.00063798, -47.4496749, -0.0169733, -4.74496749, -0.05049112, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24086, 4086, 0.0, 84.04624977, 0.01275955, 84.04624977, 0.03827866, 58.83237484, -1946.66979575, 0.05, 2, 0, 72002, 24034, 2, 3)
    ops.uniaxialMaterial('LimitState', 44086, 21.01156244, 4.836e-05, 63.03468732, 0.00014508, 210.11562442, 0.00048361, -21.01156244, -4.836e-05, -63.03468732, -0.00014508, -210.11562442, -0.00048361, 0.4, 0.3, 0.003, 0.0, 0.0, 24086, 2)
    ops.limitCurve('ThreePoint', 14086, 4086, 0.0, 84.04624977, 0.01275955, 84.04624977, 0.03827866, 58.83237484, -1946.66979575, 0.05, 2, 0, 72002, 24034, 1, 3)
    ops.uniaxialMaterial('LimitState', 34086, 21.01156244, 4.836e-05, 63.03468732, 0.00014508, 210.11562442, 0.00048361, -21.01156244, -4.836e-05, -63.03468732, -0.00014508, -210.11562442, -0.00048361, 0.4, 0.3, 0.003, 0.0, 0.0, 14086, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4086, 99999, 'P', 44086, 'Vy', 34086, 'Vz', 24086, 'My', 14086, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4086, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124034, 124034, 24034, 4086, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174034, 2.95, 0.0, 7.3)
    ops.node(123002, 2.95, 0.0, 8.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4087, 174034, 123002, 0.0625, 27999629.86923208, 11666512.44551337, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24087, 36.11946408, 0.000628, 43.27296677, 0.01741017, 4.32729668, 0.05280678, -36.11946408, -0.000628, -43.27296677, -0.01741017, -4.32729668, -0.05280678, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14087, 36.11946408, 0.000628, 43.27296677, 0.01741017, 4.32729668, 0.05280678, -36.11946408, -0.000628, -43.27296677, -0.01741017, -4.32729668, -0.05280678, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24087, 4087, 0.0, 79.86523024, 0.01255999, 79.86523024, 0.03767998, 55.90566117, -1833.28060382, 0.05, 2, 0, 74034, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44087, 19.96630756, 4.682e-05, 59.89892268, 0.00014047, 199.6630756, 0.00046824, -19.96630756, -4.682e-05, -59.89892268, -0.00014047, -199.6630756, -0.00046824, 0.4, 0.3, 0.003, 0.0, 0.0, 24087, 2)
    ops.limitCurve('ThreePoint', 14087, 4087, 0.0, 79.86523024, 0.01255999, 79.86523024, 0.03767998, 55.90566117, -1833.28060382, 0.05, 2, 0, 74034, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34087, 19.96630756, 4.682e-05, 59.89892268, 0.00014047, 199.6630756, 0.00046824, -19.96630756, -4.682e-05, -59.89892268, -0.00014047, -199.6630756, -0.00046824, 0.4, 0.3, 0.003, 0.0, 0.0, 14087, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4087, 99999, 'P', 44087, 'Vy', 34087, 'Vz', 24087, 'My', 14087, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174034, 74034, 174034, 4087, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4087, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.85)
    ops.node(124035, 0.0, 0.0, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4089, 173001, 124035, 0.0625, 26974896.77281971, 11239540.32200821, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24089, 18.25467643, 0.00054565, 22.28670436, 0.02323017, 2.22867044, 0.08096117, -18.25467643, -0.00054565, -22.28670436, -0.02323017, -2.22867044, -0.08096117, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14089, 18.25467643, 0.00054565, 22.28670436, 0.02323017, 2.22867044, 0.08096117, -18.25467643, -0.00054565, -22.28670436, -0.02323017, -2.22867044, -0.08096117, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24089, 4089, 0.0, 62.7858661, 0.01091302, 62.7858661, 0.03273907, 43.95010627, -2125.1840541, 0.05, 2, 0, 73001, 24035, 2, 3)
    ops.uniaxialMaterial('LimitState', 44089, 15.69646653, 3.821e-05, 47.08939958, 0.00011463, 156.96466525, 0.00038209, -15.69646653, -3.821e-05, -47.08939958, -0.00011463, -156.96466525, -0.00038209, 0.4, 0.3, 0.003, 0.0, 0.0, 24089, 2)
    ops.limitCurve('ThreePoint', 14089, 4089, 0.0, 62.7858661, 0.01091302, 62.7858661, 0.03273907, 43.95010627, -2125.1840541, 0.05, 2, 0, 73001, 24035, 1, 3)
    ops.uniaxialMaterial('LimitState', 34089, 15.69646653, 3.821e-05, 47.08939958, 0.00011463, 156.96466525, 0.00038209, -15.69646653, -3.821e-05, -47.08939958, -0.00011463, -156.96466525, -0.00038209, 0.4, 0.3, 0.003, 0.0, 0.0, 14089, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4089, 99999, 'P', 44089, 'Vy', 34089, 'Vz', 24089, 'My', 14089, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4089, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124035, 124035, 24035, 4089, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174035, 0.0, 0.0, 10.15)
    ops.node(124001, 0.0, 0.0, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4090, 174035, 124001, 0.0625, 27929099.32506092, 11637124.71877538, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24090, 13.47480274, 0.00054294, 16.47759132, 0.0242814, 1.64775913, 0.08912363, -13.47480274, -0.00054294, -16.47759132, -0.0242814, -1.64775913, -0.08912363, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14090, 13.47480274, 0.00054294, 16.47759132, 0.0242814, 1.64775913, 0.08912363, -13.47480274, -0.00054294, -16.47759132, -0.0242814, -1.64775913, -0.08912363, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24090, 4090, 0.0, 60.11129007, 0.01085872, 60.11129007, 0.03257616, 42.07790305, -5266.15493406, 0.05, 2, 0, 74035, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44090, 15.02782252, 3.533e-05, 45.08346756, 0.000106, 150.27822519, 0.00035332, -15.02782252, -3.533e-05, -45.08346756, -0.000106, -150.27822519, -0.00035332, 0.4, 0.3, 0.003, 0.0, 0.0, 24090, 2)
    ops.limitCurve('ThreePoint', 14090, 4090, 0.0, 60.11129007, 0.01085872, 60.11129007, 0.03257616, 42.07790305, -5266.15493406, 0.05, 2, 0, 74035, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34090, 15.02782252, 3.533e-05, 45.08346756, 0.000106, 150.27822519, 0.00035332, -15.02782252, -3.533e-05, -45.08346756, -0.000106, -150.27822519, -0.00035332, 0.4, 0.3, 0.003, 0.0, 0.0, 14090, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4090, 99999, 'P', 44090, 'Vy', 34090, 'Vz', 24090, 'My', 14090, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174035, 74035, 174035, 4090, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4090, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 2.95, 0.0, 8.85)
    ops.node(124036, 2.95, 0.0, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4091, 173002, 124036, 0.0625, 27714020.66030947, 11547508.60846228, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24091, 23.52456646, 0.0005764, 28.53922587, 0.02075385, 2.85392259, 0.07111704, -23.52456646, -0.0005764, -28.53922587, -0.02075385, -2.85392259, -0.07111704, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14091, 23.52456646, 0.0005764, 28.53922587, 0.02075385, 2.85392259, 0.07111704, -23.52456646, -0.0005764, -28.53922587, -0.02075385, -2.85392259, -0.07111704, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24091, 4091, 0.0, 67.7388497, 0.01152801, 67.7388497, 0.03458403, 47.41719479, -1606.50987717, 0.05, 2, 0, 73002, 24036, 2, 3)
    ops.uniaxialMaterial('LimitState', 44091, 16.93471243, 4.012e-05, 50.80413728, 0.00012037, 169.34712426, 0.00040124, -16.93471243, -4.012e-05, -50.80413728, -0.00012037, -169.34712426, -0.00040124, 0.4, 0.3, 0.003, 0.0, 0.0, 24091, 2)
    ops.limitCurve('ThreePoint', 14091, 4091, 0.0, 67.7388497, 0.01152801, 67.7388497, 0.03458403, 47.41719479, -1606.50987717, 0.05, 2, 0, 73002, 24036, 1, 3)
    ops.uniaxialMaterial('LimitState', 34091, 16.93471243, 4.012e-05, 50.80413728, 0.00012037, 169.34712426, 0.00040124, -16.93471243, -4.012e-05, -50.80413728, -0.00012037, -169.34712426, -0.00040124, 0.4, 0.3, 0.003, 0.0, 0.0, 14091, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4091, 99999, 'P', 44091, 'Vy', 34091, 'Vz', 24091, 'My', 14091, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4091, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124036, 124036, 24036, 4091, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174036, 2.95, 0.0, 10.15)
    ops.node(124002, 2.95, 0.0, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4092, 174036, 124002, 0.0625, 27836748.27333391, 11598645.11388913, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24092, 19.71302456, 0.00055026, 23.99251506, 0.02205442, 2.39925151, 0.07800639, -19.71302456, -0.00055026, -23.99251506, -0.02205442, -2.39925151, -0.07800639, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14092, 19.71302456, 0.00055026, 23.99251506, 0.02205442, 2.39925151, 0.07800639, -19.71302456, -0.00055026, -23.99251506, -0.02205442, -2.39925151, -0.07800639, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24092, 4092, 0.0, 65.3058329, 0.01100524, 65.3058329, 0.03301571, 45.71408303, -1815.6252925, 0.05, 2, 0, 74036, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44092, 16.32645823, 3.851e-05, 48.97937468, 0.00011554, 163.26458225, 0.00038512, -16.32645823, -3.851e-05, -48.97937468, -0.00011554, -163.26458225, -0.00038512, 0.4, 0.3, 0.003, 0.0, 0.0, 24092, 2)
    ops.limitCurve('ThreePoint', 14092, 4092, 0.0, 65.3058329, 0.01100524, 65.3058329, 0.03301571, 45.71408303, -1815.6252925, 0.05, 2, 0, 74036, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34092, 16.32645823, 3.851e-05, 48.97937468, 0.00011554, 163.26458225, 0.00038512, -16.32645823, -3.851e-05, -48.97937468, -0.00011554, -163.26458225, -0.00038512, 0.4, 0.3, 0.003, 0.0, 0.0, 14092, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4092, 99999, 'P', 44092, 'Vy', 34092, 'Vz', 24092, 'My', 14092, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174036, 74036, 174036, 4092, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4092, '-orient', 0, 0, 1, 0, 1, 0)
