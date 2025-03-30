import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 26119670.70288791, 10883196.1262033, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 52.01123518, 0.0007811, 60.83998278, 0.00829131, 6.08399828, 0.02150563, -52.01123518, -0.0007811, -60.83998278, -0.00829131, -6.08399828, -0.02150563, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 50.36773167, 0.0007811, 58.91749959, 0.00829131, 5.89174996, 0.02150563, -50.36773167, -0.0007811, -58.91749959, -0.00829131, -5.89174996, -0.02150563, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 84.35857105, 0.01562202, 84.35857105, 0.04686606, 59.05099974, -1243.77438751, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 21.08964276, 0.00011906, 63.26892829, 0.00035718, 210.89642763, 0.00119059, -21.08964276, -0.00011906, -63.26892829, -0.00035718, -210.89642763, -0.00119059, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 84.35857105, 0.01562202, 84.35857105, 0.04686606, 59.05099974, -1243.77438751, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 21.08964276, 0.00011906, 63.26892829, 0.00035718, 210.89642763, 0.00119059, -21.08964276, -0.00011906, -63.26892829, -0.00035718, -210.89642763, -0.00119059, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 7.4, 0.0, 0.0)
    ops.node(121002, 7.4, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.16, 29572314.77056647, 12321797.82106936, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 249.63104889, 0.00090232, 297.41738742, 0.00775704, 29.74173874, 0.02530323, -249.63104889, -0.00090232, -297.41738742, -0.00775704, -29.74173874, -0.02530323, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 270.76565027, 0.00090232, 322.5977404, 0.00775704, 32.25977404, 0.02530323, -270.76565027, -0.00090232, -322.5977404, -0.00775704, -32.25977404, -0.02530323, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 175.28358726, 0.01804634, 175.28358726, 0.05413903, 122.69851108, -1731.33072527, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 43.82089681, 8.535e-05, 131.46269044, 0.00025606, 438.20896815, 0.00085353, -43.82089681, -8.535e-05, -131.46269044, -0.00025606, -438.20896815, -0.00085353, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 175.28358726, 0.01804634, 175.28358726, 0.05413903, 122.69851108, -1731.33072527, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 43.82089681, 8.535e-05, 131.46269044, 0.00025606, 438.20896815, 0.00085353, -43.82089681, -8.535e-05, -131.46269044, -0.00025606, -438.20896815, -0.00085353, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 25.2, 0.0, 0.0)
    ops.node(121005, 25.2, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.16, 29066308.54822284, 12110961.89509285, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 243.38537753, 0.00087601, 289.99595041, 0.00794627, 28.99959504, 0.02480293, -243.38537753, -0.00087601, -289.99595041, -0.00794627, -28.99959504, -0.02480293, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 263.90231978, 0.00087601, 314.44207872, 0.00794627, 31.44420787, 0.02480293, -263.90231978, -0.00087601, -314.44207872, -0.00794627, -31.44420787, -0.02480293, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 175.75613662, 0.01752011, 175.75613662, 0.05256032, 123.02929563, -1760.08947932, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 43.93903415, 8.707e-05, 131.81710246, 0.00026122, 439.39034155, 0.00087073, -43.93903415, -8.707e-05, -131.81710246, -0.00026122, -439.39034155, -0.00087073, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 175.75613662, 0.01752011, 175.75613662, 0.05256032, 123.02929563, -1760.08947932, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 43.93903415, 8.707e-05, 131.81710246, 0.00026122, 439.39034155, 0.00087073, -43.93903415, -8.707e-05, -131.81710246, -0.00026122, -439.39034155, -0.00087073, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 32.6, 0.0, 0.0)
    ops.node(121006, 32.6, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.0625, 28999916.03559846, 12083298.34816602, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 86.2259254, 0.00138401, 101.63622464, 0.01049773, 10.16362246, 0.03092631, -86.2259254, -0.00138401, -101.63622464, -0.01049773, -10.16362246, -0.03092631, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 82.06107929, 0.00138401, 96.72703715, 0.01049773, 9.67270371, 0.03092631, -82.06107929, -0.00138401, -96.72703715, -0.01049773, -9.67270371, -0.03092631, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 93.74624606, 0.02768011, 93.74624606, 0.08304034, 65.62237224, -1273.76984883, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 23.43656151, 0.00011917, 70.30968454, 0.0003575, 234.36561514, 0.00119168, -23.43656151, -0.00011917, -70.30968454, -0.0003575, -234.36561514, -0.00119168, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 93.74624606, 0.02768011, 93.74624606, 0.08304034, 65.62237224, -1273.76984883, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 23.43656151, 0.00011917, 70.30968454, 0.0003575, 234.36561514, 0.00119168, -23.43656151, -0.00011917, -70.30968454, -0.0003575, -234.36561514, -0.00119168, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 3.5, 0.0)
    ops.node(121007, 0.0, 3.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.09, 28588677.97429515, 11911949.15595631, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 149.81034221, 0.00120406, 176.88380322, 0.00872349, 17.68838032, 0.02686507, -149.81034221, -0.00120406, -176.88380322, -0.00872349, -17.68838032, -0.02686507, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 133.35100556, 0.00120406, 157.44996425, 0.00872349, 15.74499643, 0.02686507, -133.35100556, -0.00120406, -157.44996425, -0.00872349, -15.74499643, -0.02686507, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 120.296853, 0.02408117, 120.296853, 0.07224351, 84.2077971, -1467.78185062, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 30.07421325, 0.00010772, 90.22263975, 0.00032316, 300.7421325, 0.00107721, -30.07421325, -0.00010772, -90.22263975, -0.00032316, -300.7421325, -0.00107721, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 120.296853, 0.02408117, 120.296853, 0.07224351, 84.2077971, -1467.78185062, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 30.07421325, 0.00010772, 90.22263975, 0.00032316, 300.7421325, 0.00107721, -30.07421325, -0.00010772, -90.22263975, -0.00032316, -300.7421325, -0.00107721, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 7.4, 3.5, 0.0)
    ops.node(121008, 7.4, 3.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.2025, 27933934.44590719, 11639139.35246133, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 415.90952933, 0.00083382, 497.27327252, 0.00781361, 49.72732725, 0.02378377, -415.90952933, -0.00083382, -497.27327252, -0.00781361, -49.72732725, -0.02378377, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 450.68139216, 0.00083382, 538.84750153, 0.00781361, 53.88475015, 0.02378377, -450.68139216, -0.00083382, -538.84750153, -0.00781361, -53.88475015, -0.02378377, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 203.13708409, 0.0166764, 203.13708409, 0.05002921, 142.19595886, -1936.91294029, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 50.78427102, 8.274e-05, 152.35281307, 0.00024822, 507.84271022, 0.0008274, -50.78427102, -8.274e-05, -152.35281307, -0.00024822, -507.84271022, -0.0008274, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 203.13708409, 0.0166764, 203.13708409, 0.05002921, 142.19595886, -1936.91294029, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 50.78427102, 8.274e-05, 152.35281307, 0.00024822, 507.84271022, 0.0008274, -50.78427102, -8.274e-05, -152.35281307, -0.00024822, -507.84271022, -0.0008274, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 14.8, 3.5, 0.0)
    ops.node(121009, 14.8, 3.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 29891199.07830913, 12454666.28262881, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 298.40981058, 0.00089654, 356.63283178, 0.01083567, 35.66328318, 0.03455241, -298.40981058, -0.00089654, -356.63283178, -0.01083567, -35.66328318, -0.03455241, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 307.1293847, 0.00089654, 367.05369028, 0.01083567, 36.70536903, 0.03455241, -307.1293847, -0.00089654, -367.05369028, -0.01083567, -36.70536903, -0.03455241, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 191.67608367, 0.01793081, 191.67608367, 0.05379244, 134.17325857, -1929.23280254, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 47.91902092, 9.234e-05, 143.75706276, 0.00027702, 479.19020918, 0.00092339, -47.91902092, -9.234e-05, -143.75706276, -0.00027702, -479.19020918, -0.00092339, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 191.67608367, 0.01793081, 191.67608367, 0.05379244, 134.17325857, -1929.23280254, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 47.91902092, 9.234e-05, 143.75706276, 0.00027702, 479.19020918, 0.00092339, -47.91902092, -9.234e-05, -143.75706276, -0.00027702, -479.19020918, -0.00092339, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 17.8, 3.5, 0.0)
    ops.node(121010, 17.8, 3.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 28440848.95627252, 11850353.73178022, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 287.1844366, 0.00088364, 343.4334674, 0.00960655, 34.34334674, 0.03105462, -287.1844366, -0.00088364, -343.4334674, -0.00960655, -34.34334674, -0.03105462, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 295.46802127, 0.00088364, 353.33950632, 0.00960655, 35.33395063, 0.03105462, -295.46802127, -0.00088364, -353.33950632, -0.00960655, -35.33395063, -0.03105462, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 178.13541703, 0.01767277, 178.13541703, 0.05301832, 124.69479192, -1811.07555634, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 44.53385426, 9.019e-05, 133.60156277, 0.00027058, 445.33854256, 0.00090192, -44.53385426, -9.019e-05, -133.60156277, -0.00027058, -445.33854256, -0.00090192, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 178.13541703, 0.01767277, 178.13541703, 0.05301832, 124.69479192, -1811.07555634, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 44.53385426, 9.019e-05, 133.60156277, 0.00027058, 445.33854256, 0.00090192, -44.53385426, -9.019e-05, -133.60156277, -0.00027058, -445.33854256, -0.00090192, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 25.2, 3.5, 0.0)
    ops.node(121011, 25.2, 3.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 28275730.93428167, 11781554.55595069, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 405.44416043, 0.00082176, 484.79516638, 0.00872287, 48.47951664, 0.02514501, -405.44416043, -0.00082176, -484.79516638, -0.00872287, -48.47951664, -0.02514501, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 438.40906705, 0.00082176, 524.21175922, 0.00872287, 52.42117592, 0.02514501, -438.40906705, -0.00082176, -524.21175922, -0.00872287, -52.42117592, -0.02514501, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 205.93525358, 0.01643511, 205.93525358, 0.04930532, 144.15467751, -1947.06606672, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 51.4838134, 8.287e-05, 154.45144019, 0.0002486, 514.83813395, 0.00082866, -51.4838134, -8.287e-05, -154.45144019, -0.0002486, -514.83813395, -0.00082866, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 205.93525358, 0.01643511, 205.93525358, 0.04930532, 144.15467751, -1947.06606672, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 51.4838134, 8.287e-05, 154.45144019, 0.0002486, 514.83813395, 0.00082866, -51.4838134, -8.287e-05, -154.45144019, -0.0002486, -514.83813395, -0.00082866, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 32.6, 3.5, 0.0)
    ops.node(121012, 32.6, 3.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.09, 29899976.45938116, 12458323.52474215, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 147.95204818, 0.00113341, 174.88897129, 0.01065305, 17.48889713, 0.03157383, -147.95204818, -0.00113341, -174.88897129, -0.01065305, -17.48889713, -0.03157383, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 131.46996935, 0.00113341, 155.40607905, 0.01065305, 15.5406079, 0.03157383, -131.46996935, -0.00113341, -155.40607905, -0.01065305, -15.5406079, -0.03157383, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 133.60081743, 0.02266814, 133.60081743, 0.06800441, 93.5205722, -1621.18177255, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 33.40020436, 0.00011439, 100.20061307, 0.00034316, 334.00204357, 0.00114387, -33.40020436, -0.00011439, -100.20061307, -0.00034316, -334.00204357, -0.00114387, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 133.60081743, 0.02266814, 133.60081743, 0.06800441, 93.5205722, -1621.18177255, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 33.40020436, 0.00011439, 100.20061307, 0.00034316, 334.00204357, 0.00114387, -33.40020436, -0.00011439, -100.20061307, -0.00034316, -334.00204357, -0.00114387, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 7.0, 0.0)
    ops.node(121013, 0.0, 7.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.09, 29480732.14386581, 12283638.39327742, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 148.47594713, 0.00119838, 175.46904839, 0.00943504, 17.54690484, 0.02948323, -148.47594713, -0.00119838, -175.46904839, -0.00943504, -17.54690484, -0.02948323, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 132.6639312, 0.00119838, 156.78238943, 0.00943504, 15.67823894, 0.02948323, -132.6639312, -0.00119838, -156.78238943, -0.00943504, -15.67823894, -0.02948323, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 128.3244916, 0.02396758, 128.3244916, 0.07190274, 89.82714412, -1545.21230517, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 32.0811229, 0.00011143, 96.2433687, 0.0003343, 320.81122901, 0.00111432, -32.0811229, -0.00011143, -96.2433687, -0.0003343, -320.81122901, -0.00111432, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 128.3244916, 0.02396758, 128.3244916, 0.07190274, 89.82714412, -1545.21230517, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 32.0811229, 0.00011143, 96.2433687, 0.0003343, 320.81122901, 0.00111432, -32.0811229, -0.00011143, -96.2433687, -0.0003343, -320.81122901, -0.00111432, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 7.4, 7.0, 0.0)
    ops.node(121014, 7.4, 7.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.2025, 27468781.31711004, 11445325.54879585, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 399.42392102, 0.00081166, 477.45818151, 0.0084364, 47.74581815, 0.02377358, -399.42392102, -0.00081166, -477.45818151, -0.0084364, -47.74581815, -0.02377358, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 432.19433672, 0.00081166, 516.63085562, 0.0084364, 51.66308556, 0.02377358, -432.19433672, -0.00081166, -516.63085562, -0.0084364, -51.66308556, -0.02377358, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 203.62037086, 0.01623314, 203.62037086, 0.04869941, 142.5342596, -2000.24671193, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 50.90509271, 8.434e-05, 152.71527814, 0.00025302, 509.05092715, 0.00084341, -50.90509271, -8.434e-05, -152.71527814, -0.00025302, -509.05092715, -0.00084341, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 203.62037086, 0.01623314, 203.62037086, 0.04869941, 142.5342596, -2000.24671193, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 50.90509271, 8.434e-05, 152.71527814, 0.00025302, 509.05092715, 0.00084341, -50.90509271, -8.434e-05, -152.71527814, -0.00025302, -509.05092715, -0.00084341, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 14.8, 7.0, 0.0)
    ops.node(121015, 14.8, 7.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.1225, 29411701.51323947, 12254875.63051645, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 189.43118698, 0.00098872, 225.73853301, 0.00917232, 22.5738533, 0.03204961, -189.43118698, -0.00098872, -225.73853301, -0.00917232, -22.5738533, -0.03204961, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 196.04161886, 0.00098872, 233.61595393, 0.00917232, 23.36159539, 0.03204961, -196.04161886, -0.00098872, -233.61595393, -0.00917232, -23.36159539, -0.03204961, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 149.23659737, 0.01977433, 149.23659737, 0.05932299, 104.46561816, -1570.19335992, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 37.30914934, 9.543e-05, 111.92744803, 0.0002863, 373.09149343, 0.00095434, -37.30914934, -9.543e-05, -111.92744803, -0.0002863, -373.09149343, -0.00095434, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 149.23659737, 0.01977433, 149.23659737, 0.05932299, 104.46561816, -1570.19335992, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 37.30914934, 9.543e-05, 111.92744803, 0.0002863, 373.09149343, 0.00095434, -37.30914934, -9.543e-05, -111.92744803, -0.0002863, -373.09149343, -0.00095434, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 17.8, 7.0, 0.0)
    ops.node(121016, 17.8, 7.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1225, 27811112.37580542, 11587963.48991892, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 190.47448758, 0.00099036, 226.87167614, 0.00944806, 22.68716761, 0.02932897, -190.47448758, -0.00099036, -226.87167614, -0.00944806, -22.68716761, -0.02932897, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 197.42649859, 0.00099036, 235.15212572, 0.00944806, 23.51521257, 0.02932897, -197.42649859, -0.00099036, -235.15212572, -0.00944806, -23.51521257, -0.02932897, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 144.76227069, 0.01980718, 144.76227069, 0.05942153, 101.33358949, -1610.01916551, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 36.19056767, 9.79e-05, 108.57170302, 0.0002937, 361.90567673, 0.000979, -36.19056767, -9.79e-05, -108.57170302, -0.0002937, -361.90567673, -0.000979, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 144.76227069, 0.01980718, 144.76227069, 0.05942153, 101.33358949, -1610.01916551, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 36.19056767, 9.79e-05, 108.57170302, 0.0002937, 361.90567673, 0.000979, -36.19056767, -9.79e-05, -108.57170302, -0.0002937, -361.90567673, -0.000979, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 25.2, 7.0, 0.0)
    ops.node(121017, 25.2, 7.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.2025, 30777085.77421134, 12823785.73925472, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 419.89384327, 0.0008125, 501.30121054, 0.00801825, 50.13012105, 0.02740664, -419.89384327, -0.0008125, -501.30121054, -0.00801825, -50.13012105, -0.02740664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 454.67825415, 0.0008125, 542.82948622, 0.00801825, 54.28294862, 0.02740664, -454.67825415, -0.0008125, -542.82948622, -0.00801825, -54.28294862, -0.02740664, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 220.34189853, 0.01624998, 220.34189853, 0.04874993, 154.23932897, -1906.5095272, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 55.08547463, 8.146e-05, 165.2564239, 0.00024437, 550.85474634, 0.00081457, -55.08547463, -8.146e-05, -165.2564239, -0.00024437, -550.85474634, -0.00081457, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 220.34189853, 0.01624998, 220.34189853, 0.04874993, 154.23932897, -1906.5095272, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 55.08547463, 8.146e-05, 165.2564239, 0.00024437, 550.85474634, 0.00081457, -55.08547463, -8.146e-05, -165.2564239, -0.00024437, -550.85474634, -0.00081457, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 32.6, 7.0, 0.0)
    ops.node(121018, 32.6, 7.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.09, 31267157.87698254, 13027982.44874272, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 147.73231077, 0.00117375, 174.61024645, 0.01005566, 17.46102465, 0.03370042, -147.73231077, -0.00117375, -174.61024645, -0.01005566, -17.46102465, -0.03370042, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 132.38951845, 0.00117375, 156.47603645, 0.01005566, 15.64760364, 0.03370042, -132.38951845, -0.00117375, -156.47603645, -0.01005566, -15.64760364, -0.03370042, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 133.24303942, 0.02347493, 133.24303942, 0.0704248, 93.27012759, -1528.48534392, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 33.31075985, 0.00010909, 99.93227956, 0.00032728, 333.10759854, 0.00109093, -33.31075985, -0.00010909, -99.93227956, -0.00032728, -333.10759854, -0.00109093, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 133.24303942, 0.02347493, 133.24303942, 0.0704248, 93.27012759, -1528.48534392, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 33.31075985, 0.00010909, 99.93227956, 0.00032728, 333.10759854, 0.00109093, -33.31075985, -0.00010909, -99.93227956, -0.00032728, -333.10759854, -0.00109093, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 10.5, 0.0)
    ops.node(121019, 0.0, 10.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.0625, 29326258.13271105, 12219274.22196294, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 90.9798402, 0.00144121, 107.28077586, 0.00908673, 10.72807759, 0.03031146, -90.9798402, -0.00144121, -107.28077586, -0.00908673, -10.72807759, -0.03031146, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 86.35575617, 0.00144121, 101.82819074, 0.00908673, 10.18281907, 0.03031146, -86.35575617, -0.00144121, -101.82819074, -0.00908673, -10.18281907, -0.03031146, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 73.95475673, 0.02882417, 73.95475673, 0.08647252, 51.76832971, -1160.91202389, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 18.48868918, 9.296e-05, 55.46606754, 0.00027889, 184.88689182, 0.00092963, -18.48868918, -9.296e-05, -55.46606754, -0.00027889, -184.88689182, -0.00092963, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 73.95475673, 0.02882417, 73.95475673, 0.08647252, 51.76832971, -1160.91202389, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 18.48868918, 9.296e-05, 55.46606754, 0.00027889, 184.88689182, 0.00092963, -18.48868918, -9.296e-05, -55.46606754, -0.00027889, -184.88689182, -0.00092963, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 7.4, 10.5, 0.0)
    ops.node(121020, 7.4, 10.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.16, 31207483.07457853, 13003117.94774106, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 297.45462325, 0.00092375, 353.95742822, 0.00863676, 35.39574282, 0.03215857, -297.45462325, -0.00092375, -353.95742822, -0.00863676, -35.39574282, -0.03215857, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 314.30278105, 0.00092375, 374.00596718, 0.00863676, 37.40059672, 0.03215857, -314.30278105, -0.00092375, -374.00596718, -0.00863676, -37.40059672, -0.03215857, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 196.91200512, 0.01847508, 196.91200512, 0.05542523, 137.83840359, -1904.52210307, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 49.22800128, 9.086e-05, 147.68400384, 0.00027258, 492.28001281, 0.00090861, -49.22800128, -9.086e-05, -147.68400384, -0.00027258, -492.28001281, -0.00090861, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 196.91200512, 0.01847508, 196.91200512, 0.05542523, 137.83840359, -1904.52210307, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 49.22800128, 9.086e-05, 147.68400384, 0.00027258, 492.28001281, 0.00090861, -49.22800128, -9.086e-05, -147.68400384, -0.00027258, -492.28001281, -0.00090861, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 14.8, 10.5, 0.0)
    ops.node(121021, 14.8, 10.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.09, 26974783.30074484, 11239493.04197701, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 127.71882844, 0.00119278, 150.82491133, 0.00967653, 15.08249113, 0.02823619, -127.71882844, -0.00119278, -150.82491133, -0.00967653, -15.08249113, -0.02823619, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 127.71882844, 0.00119278, 150.82491133, 0.00967653, 15.08249113, 0.02823619, -127.71882844, -0.00119278, -150.82491133, -0.00967653, -15.08249113, -0.02823619, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 133.11652782, 0.02385557, 133.11652782, 0.07156671, 93.18156947, -1794.17834598, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 33.27913196, 0.00012633, 99.83739587, 0.000379, 332.79131955, 0.00126332, -33.27913196, -0.00012633, -99.83739587, -0.000379, -332.79131955, -0.00126332, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 133.11652782, 0.02385557, 133.11652782, 0.07156671, 93.18156947, -1794.17834598, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 33.27913196, 0.00012633, 99.83739587, 0.000379, 332.79131955, 0.00126332, -33.27913196, -0.00012633, -99.83739587, -0.000379, -332.79131955, -0.00126332, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 17.8, 10.5, 0.0)
    ops.node(121022, 17.8, 10.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.09, 29374857.33694636, 12239523.89039432, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 127.64966287, 0.00117196, 151.24838901, 0.0095784, 15.1248389, 0.03418402, -127.64966287, -0.00117196, -151.24838901, -0.0095784, -15.1248389, -0.03418402, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 127.64966287, 0.00117196, 151.24838901, 0.0095784, 15.1248389, 0.03418402, -127.64966287, -0.00117196, -151.24838901, -0.0095784, -15.1248389, -0.03418402, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 132.17164871, 0.02343917, 132.17164871, 0.07031752, 92.52015409, -1617.68547863, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 33.04291218, 0.00011519, 99.12873653, 0.00034556, 330.42912177, 0.00115187, -33.04291218, -0.00011519, -99.12873653, -0.00034556, -330.42912177, -0.00115187, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 132.17164871, 0.02343917, 132.17164871, 0.07031752, 92.52015409, -1617.68547863, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 33.04291218, 0.00011519, 99.12873653, 0.00034556, 330.42912177, 0.00115187, -33.04291218, -0.00011519, -99.12873653, -0.00034556, -330.42912177, -0.00115187, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 25.2, 10.5, 0.0)
    ops.node(121023, 25.2, 10.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.16, 26806364.07744209, 11169318.36560087, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 285.15506448, 0.00091317, 339.15161054, 0.00900799, 33.91516105, 0.02520078, -285.15506448, -0.00091317, -339.15161054, -0.00900799, -33.91516105, -0.02520078, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 301.91871695, 0.00091317, 359.08960374, 0.00900799, 35.90896037, 0.02520078, -301.91871695, -0.00091317, -359.08960374, -0.00900799, -35.90896037, -0.02520078, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 177.19751772, 0.01826347, 177.19751772, 0.05479042, 124.03826241, -1976.99759687, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 44.29937943, 9.519e-05, 132.89813829, 0.00028556, 442.99379431, 0.00095188, -44.29937943, -9.519e-05, -132.89813829, -0.00028556, -442.99379431, -0.00095188, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 177.19751772, 0.01826347, 177.19751772, 0.05479042, 124.03826241, -1976.99759687, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 44.29937943, 9.519e-05, 132.89813829, 0.00028556, 442.99379431, 0.00095188, -44.29937943, -9.519e-05, -132.89813829, -0.00028556, -442.99379431, -0.00095188, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 32.6, 10.5, 0.0)
    ops.node(121024, 32.6, 10.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.0625, 29034381.50609666, 12097658.96087361, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 89.20208878, 0.00142271, 105.14896224, 0.00895838, 10.51489622, 0.02947142, -89.20208878, -0.00142271, -105.14896224, -0.00895838, -10.51489622, -0.02947142, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 84.74188906, 0.00142271, 99.89140182, 0.00895838, 9.98914018, 0.02947142, -84.74188906, -0.00142271, -99.89140182, -0.00895838, -9.98914018, -0.02947142, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 71.55503246, 0.02845426, 71.55503246, 0.08536278, 50.08852272, -1158.8375016, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 17.88875811, 9.085e-05, 53.66627434, 0.00027255, 178.88758114, 0.00090851, -17.88875811, -9.085e-05, -53.66627434, -0.00027255, -178.88758114, -0.00090851, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 71.55503246, 0.02845426, 71.55503246, 0.08536278, 50.08852272, -1158.8375016, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 17.88875811, 9.085e-05, 53.66627434, 0.00027255, 178.88758114, 0.00090851, -17.88875811, -9.085e-05, -53.66627434, -0.00027255, -178.88758114, -0.00090851, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.5)
    ops.node(122001, 0.0, 0.0, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 27146703.3221064, 11311126.384211, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 75.28741632, 0.0014981, 89.44515955, 0.01138591, 8.94451595, 0.0338617, -75.28741632, -0.0014981, -89.44515955, -0.01138591, -8.94451595, -0.0338617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 71.7863952, 0.0014981, 85.28577398, 0.01138591, 8.5285774, 0.0338617, -71.7863952, -0.0014981, -85.28577398, -0.01138591, -8.5285774, -0.0338617, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 87.98581928, 0.02996206, 87.98581928, 0.08988617, 61.5900735, -1160.05991861, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 21.99645482, 0.00011948, 65.98936446, 0.00035844, 219.9645482, 0.00119481, -21.99645482, -0.00011948, -65.98936446, -0.00035844, -219.9645482, -0.00119481, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 87.98581928, 0.02996206, 87.98581928, 0.08988617, 61.5900735, -1160.05991861, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 21.99645482, 0.00011948, 65.98936446, 0.00035844, 219.9645482, 0.00119481, -21.99645482, -0.00011948, -65.98936446, -0.00035844, -219.9645482, -0.00119481, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 7.4, 0.0, 3.5)
    ops.node(122002, 7.4, 0.0, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.16, 27411289.06153249, 11421370.4423052, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 193.81121894, 0.00087233, 232.52237455, 0.00826776, 23.25223745, 0.02650706, -193.81121894, -0.00087233, -232.52237455, -0.00826776, -23.25223745, -0.02650706, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 193.81121894, 0.00087233, 232.52237455, 0.00826776, 23.25223745, 0.02650706, -193.81121894, -0.00087233, -232.52237455, -0.00826776, -23.25223745, -0.02650706, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 157.2552634, 0.01744663, 157.2552634, 0.05233988, 110.07868438, -1499.2300488, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 39.31381585, 8.261e-05, 117.94144755, 0.00024783, 393.1381585, 0.00082611, -39.31381585, -8.261e-05, -117.94144755, -0.00024783, -393.1381585, -0.00082611, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 157.2552634, 0.01744663, 157.2552634, 0.05233988, 110.07868438, -1499.2300488, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 39.31381585, 8.261e-05, 117.94144755, 0.00024783, 393.1381585, 0.00082611, -39.31381585, -8.261e-05, -117.94144755, -0.00024783, -393.1381585, -0.00082611, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 25.2, 0.0, 3.5)
    ops.node(122005, 25.2, 0.0, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.16, 29786223.56417813, 12410926.48507422, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 195.21627137, 0.00083767, 233.95422987, 0.0092796, 23.39542299, 0.03056434, -195.21627137, -0.00083767, -233.95422987, -0.0092796, -23.39542299, -0.03056434, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 195.21627137, 0.00083767, 233.95422987, 0.0092796, 23.39542299, 0.03056434, -195.21627137, -0.00083767, -233.95422987, -0.0092796, -23.39542299, -0.03056434, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 172.25658982, 0.01675342, 172.25658982, 0.05026026, 120.57961287, -1556.16609212, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 43.06414745, 8.328e-05, 129.19244236, 0.00024983, 430.64147454, 0.00083277, -43.06414745, -8.328e-05, -129.19244236, -0.00024983, -430.64147454, -0.00083277, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 172.25658982, 0.01675342, 172.25658982, 0.05026026, 120.57961287, -1556.16609212, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 43.06414745, 8.328e-05, 129.19244236, 0.00024983, 430.64147454, 0.00083277, -43.06414745, -8.328e-05, -129.19244236, -0.00024983, -430.64147454, -0.00083277, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 32.6, 0.0, 3.5)
    ops.node(122006, 32.6, 0.0, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.0625, 28056698.06312323, 11690290.85963468, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 72.93397568, 0.00137089, 86.74491671, 0.01083217, 8.67449167, 0.03564051, -72.93397568, -0.00137089, -86.74491671, -0.01083217, -8.67449167, -0.03564051, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 69.43599379, 0.00137089, 82.58454914, 0.01083217, 8.25845491, 0.03564051, -69.43599379, -0.00137089, -82.58454914, -0.01083217, -8.25845491, -0.03564051, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 72.34073512, 0.02741789, 72.34073512, 0.08225367, 50.63851459, -1063.44462614, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 18.08518378, 9.505e-05, 54.25555134, 0.00028515, 180.8518378, 0.00095049, -18.08518378, -9.505e-05, -54.25555134, -0.00028515, -180.8518378, -0.00095049, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 72.34073512, 0.02741789, 72.34073512, 0.08225367, 50.63851459, -1063.44462614, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 18.08518378, 9.505e-05, 54.25555134, 0.00028515, 180.8518378, 0.00095049, -18.08518378, -9.505e-05, -54.25555134, -0.00028515, -180.8518378, -0.00095049, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 3.5, 3.525)
    ops.node(122007, 0.0, 3.5, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.09, 27242382.07450357, 11350992.53104316, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 132.57781809, 0.00115623, 157.75128068, 0.00939669, 15.77512807, 0.0300639, -132.57781809, -0.00115623, -157.75128068, -0.00939669, -15.77512807, -0.0300639, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 116.58293766, 0.00115623, 138.71934224, 0.00939669, 13.87193422, 0.0300639, -116.58293766, -0.00115623, -138.71934224, -0.00939669, -13.87193422, -0.0300639, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 107.81989967, 0.02312451, 107.81989967, 0.06937354, 75.47392977, -1272.39057587, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 26.95497492, 0.00010132, 80.86492475, 0.00030396, 269.54974917, 0.0010132, -26.95497492, -0.00010132, -80.86492475, -0.00030396, -269.54974917, -0.0010132, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 107.81989967, 0.02312451, 107.81989967, 0.06937354, 75.47392977, -1272.39057587, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 26.95497492, 0.00010132, 80.86492475, 0.00030396, 269.54974917, 0.0010132, -26.95497492, -0.00010132, -80.86492475, -0.00030396, -269.54974917, -0.0010132, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 7.4, 3.5, 3.525)
    ops.node(122008, 7.4, 3.5, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.2025, 28024539.16208893, 11676891.31753705, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 266.46240019, 0.00076873, 320.42145384, 0.00824607, 32.04214538, 0.02732058, -266.46240019, -0.00076873, -320.42145384, -0.00824607, -32.04214538, -0.02732058, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 251.3179675, 0.00076873, 302.2102498, 0.00824607, 30.22102498, 0.02732058, -251.3179675, -0.00076873, -302.2102498, -0.00824607, -30.22102498, -0.02732058, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 190.1361467, 0.01537458, 190.1361467, 0.04612375, 133.09530269, -1647.43377412, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 47.53403668, 7.719e-05, 142.60211003, 0.00023158, 475.34036675, 0.00077194, -47.53403668, -7.719e-05, -142.60211003, -0.00023158, -475.34036675, -0.00077194, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 190.1361467, 0.01537458, 190.1361467, 0.04612375, 133.09530269, -1647.43377412, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 47.53403668, 7.719e-05, 142.60211003, 0.00023158, 475.34036675, 0.00077194, -47.53403668, -7.719e-05, -142.60211003, -0.00023158, -475.34036675, -0.00077194, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 14.8, 3.5, 3.525)
    ops.node(122009, 14.8, 3.5, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 28680077.64586187, 11950032.35244245, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 182.09060514, 0.00080169, 218.91194139, 0.01076326, 21.89119414, 0.03635452, -182.09060514, -0.00080169, -218.91194139, -0.01076326, -21.89119414, -0.03635452, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 166.89522341, 0.00080169, 200.64383518, 0.01076326, 20.06438352, 0.03635452, -166.89522341, -0.00080169, -200.64383518, -0.01076326, -20.06438352, -0.03635452, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 174.80608344, 0.01603387, 174.80608344, 0.04810161, 122.36425841, -1740.63157252, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 43.70152086, 8.777e-05, 131.10456258, 0.00026331, 437.0152086, 0.00087769, -43.70152086, -8.777e-05, -131.10456258, -0.00026331, -437.0152086, -0.00087769, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 174.80608344, 0.01603387, 174.80608344, 0.04810161, 122.36425841, -1740.63157252, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 43.70152086, 8.777e-05, 131.10456258, 0.00026331, 437.0152086, 0.00087769, -43.70152086, -8.777e-05, -131.10456258, -0.00026331, -437.0152086, -0.00087769, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 17.8, 3.5, 3.525)
    ops.node(122010, 17.8, 3.5, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 29209679.05183822, 12170699.60493259, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 187.18011195, 0.00083594, 224.92268904, 0.01070628, 22.4922689, 0.03703711, -187.18011195, -0.00083594, -224.92268904, -0.01070628, -22.4922689, -0.03703711, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 171.63822087, 0.00083594, 206.24696597, 0.01070628, 20.6246966, 0.03703711, -171.63822087, -0.00083594, -206.24696597, -0.01070628, -20.6246966, -0.03703711, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 176.75464021, 0.01671885, 176.75464021, 0.05015655, 123.72824815, -1724.90614915, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 44.18866005, 8.714e-05, 132.56598016, 0.00026141, 441.88660053, 0.00087138, -44.18866005, -8.714e-05, -132.56598016, -0.00026141, -441.88660053, -0.00087138, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 176.75464021, 0.01671885, 176.75464021, 0.05015655, 123.72824815, -1724.90614915, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 44.18866005, 8.714e-05, 132.56598016, 0.00026141, 441.88660053, 0.00087138, -44.18866005, -8.714e-05, -132.56598016, -0.00026141, -441.88660053, -0.00087138, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 25.2, 3.5, 3.525)
    ops.node(122011, 25.2, 3.5, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 27916710.31017665, 11631962.62924027, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 274.24069003, 0.00077565, 329.7887437, 0.00767387, 32.97887437, 0.02661934, -274.24069003, -0.00077565, -329.7887437, -0.00767387, -32.97887437, -0.02661934, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 257.97081381, 0.00077565, 310.22336834, 0.00767387, 31.02233683, 0.02661934, -257.97081381, -0.00077565, -310.22336834, -0.00767387, -31.02233683, -0.02661934, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 187.5081942, 0.015513, 187.5081942, 0.046539, 131.25573594, -1610.49929858, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 46.87704855, 7.642e-05, 140.63114565, 0.00022926, 468.7704855, 0.00076421, -46.87704855, -7.642e-05, -140.63114565, -0.00022926, -468.7704855, -0.00076421, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 187.5081942, 0.015513, 187.5081942, 0.046539, 131.25573594, -1610.49929858, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 46.87704855, 7.642e-05, 140.63114565, 0.00022926, 468.7704855, 0.00076421, -46.87704855, -7.642e-05, -140.63114565, -0.00022926, -468.7704855, -0.00076421, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 32.6, 3.5, 3.525)
    ops.node(122012, 32.6, 3.5, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.09, 29991765.57221067, 12496568.98842111, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 131.74546041, 0.00114595, 156.91438936, 0.01061652, 15.69143894, 0.03704105, -131.74546041, -0.00114595, -156.91438936, -0.01061652, -15.69143894, -0.03704105, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 116.72043393, 0.00114595, 139.01895032, 0.01061652, 13.90189503, 0.03704105, -116.72043393, -0.00114595, -139.01895032, -0.01061652, -13.90189503, -0.03704105, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 118.92472774, 0.02291897, 118.92472774, 0.06875691, 83.24730942, -1303.17489984, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 29.73118193, 0.00010151, 89.1935458, 0.00030453, 297.31181934, 0.0010151, -29.73118193, -0.00010151, -89.1935458, -0.00030453, -297.31181934, -0.0010151, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 118.92472774, 0.02291897, 118.92472774, 0.06875691, 83.24730942, -1303.17489984, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 29.73118193, 0.00010151, 89.1935458, 0.00030453, 297.31181934, 0.0010151, -29.73118193, -0.00010151, -89.1935458, -0.00030453, -297.31181934, -0.0010151, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 7.0, 3.525)
    ops.node(122013, 0.0, 7.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.09, 29277024.7654951, 12198760.31895629, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 130.77737558, 0.00115319, 155.79562902, 0.00943504, 15.5795629, 0.03445911, -130.77737558, -0.00115319, -155.79562902, -0.00943504, -15.5795629, -0.03445911, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 115.9380254, 0.00115319, 138.11744971, 0.00943504, 13.81174497, 0.03445911, -115.9380254, -0.00115319, -138.11744971, -0.00943504, -13.81174497, -0.03445911, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 105.07128448, 0.02306384, 105.07128448, 0.06919152, 73.54989914, -1221.7198352, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 26.26782112, 9.187e-05, 78.80346336, 0.00027562, 262.6782112, 0.00091875, -26.26782112, -9.187e-05, -78.80346336, -0.00027562, -262.6782112, -0.00091875, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 105.07128448, 0.02306384, 105.07128448, 0.06919152, 73.54989914, -1221.7198352, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 26.26782112, 9.187e-05, 78.80346336, 0.00027562, 262.6782112, 0.00091875, -26.26782112, -9.187e-05, -78.80346336, -0.00027562, -262.6782112, -0.00091875, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 7.4, 7.0, 3.525)
    ops.node(122014, 7.4, 7.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.2025, 29374815.93712174, 12239506.64046739, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 268.4207104, 0.00076885, 322.44314623, 0.00826752, 32.24431462, 0.02885222, -268.4207104, -0.00076885, -322.44314623, -0.00826752, -32.24431462, -0.02885222, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 253.31256263, 0.00076885, 304.29432793, 0.00826752, 30.42943279, 0.02885222, -253.31256263, -0.00076885, -304.29432793, -0.00826752, -30.42943279, -0.02885222, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 199.75706603, 0.01537707, 199.75706603, 0.0461312, 139.82994622, -1667.61418812, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 49.93926651, 7.737e-05, 149.81779952, 0.00023212, 499.39266506, 0.00077372, -49.93926651, -7.737e-05, -149.81779952, -0.00023212, -499.39266506, -0.00077372, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 199.75706603, 0.01537707, 199.75706603, 0.0461312, 139.82994622, -1667.61418812, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 49.93926651, 7.737e-05, 149.81779952, 0.00023212, 499.39266506, 0.00077372, -49.93926651, -7.737e-05, -149.81779952, -0.00023212, -499.39266506, -0.00077372, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 14.8, 7.0, 3.525)
    ops.node(122015, 14.8, 7.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.1225, 28849840.55794065, 12020766.89914194, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 156.9283763, 0.00091118, 188.13908028, 0.01117288, 18.81390803, 0.03733006, -156.9283763, -0.00091118, -188.13908028, -0.01117288, -18.81390803, -0.03733006, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 150.17443765, 0.00091118, 180.04188437, 0.01117288, 18.00418844, 0.03733006, -150.17443765, -0.00091118, -180.04188437, -0.01117288, -18.00418844, -0.03733006, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 143.99536789, 0.01822352, 143.99536789, 0.05467057, 100.79675752, -1517.02974477, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 35.99884197, 9.388e-05, 107.99652592, 0.00028163, 359.98841972, 0.00093875, -35.99884197, -9.388e-05, -107.99652592, -0.00028163, -359.98841972, -0.00093875, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 143.99536789, 0.01822352, 143.99536789, 0.05467057, 100.79675752, -1517.02974477, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 35.99884197, 9.388e-05, 107.99652592, 0.00028163, 359.98841972, 0.00093875, -35.99884197, -9.388e-05, -107.99652592, -0.00028163, -359.98841972, -0.00093875, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 17.8, 7.0, 3.525)
    ops.node(122016, 17.8, 7.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1225, 30830255.90546865, 12845939.96061194, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 157.43355422, 0.00091803, 188.34897386, 0.0114912, 18.83489739, 0.04067005, -157.43355422, -0.00091803, -188.34897386, -0.0114912, -18.83489739, -0.04067005, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 150.90858799, 0.00091803, 180.54269202, 0.0114912, 18.0542692, 0.04067005, -150.90858799, -0.00091803, -180.54269202, -0.0114912, -18.0542692, -0.04067005, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 153.67442362, 0.01836052, 153.67442362, 0.05508156, 107.57209653, -1556.68427716, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 38.4186059, 9.375e-05, 115.25581771, 0.00028125, 384.18605904, 0.0009375, -38.4186059, -9.375e-05, -115.25581771, -0.00028125, -384.18605904, -0.0009375, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 153.67442362, 0.01836052, 153.67442362, 0.05508156, 107.57209653, -1556.68427716, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 38.4186059, 9.375e-05, 115.25581771, 0.00028125, 384.18605904, 0.0009375, -38.4186059, -9.375e-05, -115.25581771, -0.00028125, -384.18605904, -0.0009375, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 25.2, 7.0, 3.525)
    ops.node(122017, 25.2, 7.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.2025, 29709425.23400282, 12378927.18083451, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 262.46723296, 0.00078905, 315.16741624, 0.00905013, 31.51674162, 0.02997988, -262.46723296, -0.00078905, -315.16741624, -0.00905013, -31.51674162, -0.02997988, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 248.88046464, 0.00078905, 298.85259241, 0.00905013, 29.88525924, 0.02997988, -248.88046464, -0.00078905, -298.85259241, -0.00905013, -29.88525924, -0.02997988, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 205.03434883, 0.01578093, 205.03434883, 0.0473428, 143.52404418, -1727.98679328, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 51.25858721, 7.852e-05, 153.77576162, 0.00023557, 512.58587208, 0.00078522, -51.25858721, -7.852e-05, -153.77576162, -0.00023557, -512.58587208, -0.00078522, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 205.03434883, 0.01578093, 205.03434883, 0.0473428, 143.52404418, -1727.98679328, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 51.25858721, 7.852e-05, 153.77576162, 0.00023557, 512.58587208, 0.00078522, -51.25858721, -7.852e-05, -153.77576162, -0.00023557, -512.58587208, -0.00078522, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 32.6, 7.0, 3.525)
    ops.node(122018, 32.6, 7.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.09, 27667178.2657157, 11527990.94404821, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 124.50770236, 0.00114543, 148.22196307, 0.00969963, 14.82219631, 0.03131919, -124.50770236, -0.00114543, -148.22196307, -0.00969963, -14.82219631, -0.03131919, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 110.95987318, 0.00114543, 132.09375736, 0.00969963, 13.20937574, 0.03131919, -110.95987318, -0.00114543, -132.09375736, -0.00969963, -13.20937574, -0.03131919, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 109.46914672, 0.02290858, 109.46914672, 0.06872573, 76.62840271, -1307.59405957, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 27.36728668, 0.00010129, 82.10186004, 0.00030387, 273.67286681, 0.0010129, -27.36728668, -0.00010129, -82.10186004, -0.00030387, -273.67286681, -0.0010129, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 109.46914672, 0.02290858, 109.46914672, 0.06872573, 76.62840271, -1307.59405957, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 27.36728668, 0.00010129, 82.10186004, 0.00030387, 273.67286681, 0.0010129, -27.36728668, -0.00010129, -82.10186004, -0.00030387, -273.67286681, -0.0010129, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 10.5, 3.5)
    ops.node(122019, 0.0, 10.5, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.0625, 30293828.9700036, 12622428.7375015, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 78.1565888, 0.0013662, 92.97995733, 0.01113752, 9.29799573, 0.0411906, -78.1565888, -0.0013662, -92.97995733, -0.01113752, -9.29799573, -0.0411906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 74.0786638, 0.0013662, 88.12860316, 0.01113752, 8.81286032, 0.0411906, -74.0786638, -0.0013662, -88.12860316, -0.01113752, -8.81286032, -0.0411906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 77.14655792, 0.02732398, 77.14655792, 0.08197193, 54.00259054, -1048.67876627, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 19.28663948, 9.388e-05, 57.85991844, 0.00028163, 192.86639479, 0.00093878, -19.28663948, -9.388e-05, -57.85991844, -0.00028163, -192.86639479, -0.00093878, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 77.14655792, 0.02732398, 77.14655792, 0.08197193, 54.00259054, -1048.67876627, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 19.28663948, 9.388e-05, 57.85991844, 0.00028163, 192.86639479, 0.00093878, -19.28663948, -9.388e-05, -57.85991844, -0.00028163, -192.86639479, -0.00093878, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 7.4, 10.5, 3.5)
    ops.node(122020, 7.4, 10.5, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.16, 32711214.44554438, 13629672.68564349, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 191.87112187, 0.0007883, 228.76719346, 0.0099386, 22.87671935, 0.03900742, -191.87112187, -0.0007883, -228.76719346, -0.0099386, -22.87671935, -0.03900742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 177.20150241, 0.0007883, 211.27666316, 0.0099386, 21.12766632, 0.03900742, -177.20150241, -0.0007883, -211.27666316, -0.0099386, -21.12766632, -0.03900742, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 195.32592146, 0.01576607, 195.32592146, 0.04729822, 136.72814503, -1708.32295326, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 48.83148037, 8.599e-05, 146.4944411, 0.00025796, 488.31480366, 0.00085986, -48.83148037, -8.599e-05, -146.4944411, -0.00025796, -488.31480366, -0.00085986, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 195.32592146, 0.01576607, 195.32592146, 0.04729822, 136.72814503, -1708.32295326, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 48.83148037, 8.599e-05, 146.4944411, 0.00025796, 488.31480366, 0.00085986, -48.83148037, -8.599e-05, -146.4944411, -0.00025796, -488.31480366, -0.00085986, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 14.8, 10.5, 3.5)
    ops.node(122021, 14.8, 10.5, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.09, 29351725.96147385, 12229885.81728077, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 98.77308808, 0.00106996, 117.94322515, 0.0099111, 11.79432251, 0.04084621, -98.77308808, -0.00106996, -117.94322515, -0.0099111, -11.79432251, -0.04084621, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 88.41429008, 0.00106996, 105.57396477, 0.0099111, 10.55739648, 0.04084621, -88.41429008, -0.00106996, -105.57396477, -0.0099111, -10.55739648, -0.04084621, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 123.23147293, 0.02139927, 123.23147293, 0.06419782, 86.26203105, -1444.7952075, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 30.80786823, 0.00010748, 92.42360469, 0.00032244, 308.07868231, 0.0010748, -30.80786823, -0.00010748, -92.42360469, -0.00032244, -308.07868231, -0.0010748, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 123.23147293, 0.02139927, 123.23147293, 0.06419782, 86.26203105, -1444.7952075, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 30.80786823, 0.00010748, 92.42360469, 0.00032244, 308.07868231, 0.0010748, -30.80786823, -0.00010748, -92.42360469, -0.00032244, -308.07868231, -0.0010748, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 17.8, 10.5, 3.5)
    ops.node(122022, 17.8, 10.5, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.09, 31588365.65630184, 13161819.0234591, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 98.01255424, 0.00103823, 116.77144808, 0.01139988, 11.67714481, 0.04686393, -98.01255424, -0.00103823, -116.77144808, -0.01139988, -11.67714481, -0.04686393, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 87.99584949, 0.00103823, 104.83761851, 0.01139988, 10.48376185, 0.04686393, -87.99584949, -0.00103823, -104.83761851, -0.01139988, -10.48376185, -0.04686393, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 133.37859014, 0.02076468, 133.37859014, 0.06229403, 93.3650131, -1522.12786101, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 33.34464753, 0.00010809, 100.0339426, 0.00032428, 333.44647534, 0.00108093, -33.34464753, -0.00010809, -100.0339426, -0.00032428, -333.44647534, -0.00108093, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 133.37859014, 0.02076468, 133.37859014, 0.06229403, 93.3650131, -1522.12786101, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 33.34464753, 0.00010809, 100.0339426, 0.00032428, 333.44647534, 0.00108093, -33.34464753, -0.00010809, -100.0339426, -0.00032428, -333.44647534, -0.00108093, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 25.2, 10.5, 3.5)
    ops.node(122023, 25.2, 10.5, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.16, 28641774.63244529, 11934072.76351887, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 194.59176797, 0.00080692, 233.41711946, 0.0101683, 23.34171195, 0.03403288, -194.59176797, -0.00080692, -233.41711946, -0.0101683, -23.34171195, -0.03403288, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 178.64040856, 0.00080692, 214.28311187, 0.0101683, 21.42831119, 0.03403288, -178.64040856, -0.00080692, -214.28311187, -0.0101683, -21.42831119, -0.03403288, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 177.3498472, 0.01613833, 177.3498472, 0.04841499, 124.14489304, -1778.14139023, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 44.3374618, 8.916e-05, 133.0123854, 0.00026749, 443.374618, 0.00089165, -44.3374618, -8.916e-05, -133.0123854, -0.00026749, -443.374618, -0.00089165, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 177.3498472, 0.01613833, 177.3498472, 0.04841499, 124.14489304, -1778.14139023, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 44.3374618, 8.916e-05, 133.0123854, 0.00026749, 443.374618, 0.00089165, -44.3374618, -8.916e-05, -133.0123854, -0.00026749, -443.374618, -0.00089165, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 32.6, 10.5, 3.5)
    ops.node(122024, 32.6, 10.5, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.0625, 29651021.27614199, 12354592.1983925, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 76.9867378, 0.00142516, 91.61148133, 0.01145169, 9.16114813, 0.04007407, -76.9867378, -0.00142516, -91.61148133, -0.01145169, -9.16114813, -0.04007407, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 73.22942279, 0.00142516, 87.14041004, 0.01145169, 8.714041, 0.04007407, -73.22942279, -0.00142516, -87.14041004, -0.01145169, -8.714041, -0.04007407, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 81.19304931, 0.02850328, 81.19304931, 0.08550985, 56.83513452, -1070.27968531, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 20.29826233, 0.00010094, 60.89478698, 0.00030283, 202.98262328, 0.00100944, -20.29826233, -0.00010094, -60.89478698, -0.00030283, -202.98262328, -0.00100944, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 81.19304931, 0.02850328, 81.19304931, 0.08550985, 56.83513452, -1070.27968531, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 20.29826233, 0.00010094, 60.89478698, 0.00030283, 202.98262328, 0.00100944, -20.29826233, -0.00010094, -60.89478698, -0.00030283, -202.98262328, -0.00100944, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.7)
    ops.node(123001, 0.0, 0.0, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 29031822.8264651, 12096592.84436046, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 55.05646233, 0.00127876, 66.13536638, 0.01092363, 6.61353664, 0.04691845, -55.05646233, -0.00127876, -66.13536638, -0.01092363, -6.61353664, -0.04691845, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 55.05646233, 0.00127876, 66.13536638, 0.01092363, 6.61353664, 0.04691845, -55.05646233, -0.00127876, -66.13536638, -0.01092363, -6.61353664, -0.04691845, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 52.84876236, 0.02557516, 52.84876236, 0.07672548, 36.99413365, -852.30052711, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 13.21219059, 6.711e-05, 39.63657177, 0.00020132, 132.12190591, 0.00067106, -13.21219059, -6.711e-05, -39.63657177, -0.00020132, -132.12190591, -0.00067106, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 52.84876236, 0.02557516, 52.84876236, 0.07672548, 36.99413365, -852.30052711, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 13.21219059, 6.711e-05, 39.63657177, 0.00020132, 132.12190591, 0.00067106, -13.21219059, -6.711e-05, -39.63657177, -0.00020132, -132.12190591, -0.00067106, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 7.4, 0.0, 6.7)
    ops.node(123002, 7.4, 0.0, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1225, 29072619.35094796, 12113591.39622832, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 136.3689597, 0.00094164, 164.02604308, 0.01089444, 16.40260431, 0.03514955, -136.3689597, -0.00094164, -164.02604308, -0.01089444, -16.40260431, -0.03514955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 136.3689597, 0.00094164, 164.02604308, 0.01089444, 16.40260431, 0.03514955, -136.3689597, -0.00094164, -164.02604308, -0.01089444, -16.40260431, -0.03514955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 129.91740893, 0.01883281, 129.91740893, 0.05649844, 90.94218625, -1222.60561633, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 32.47935223, 8.405e-05, 97.4380567, 0.00025215, 324.79352234, 0.00084048, -32.47935223, -8.405e-05, -97.4380567, -0.00025215, -324.79352234, -0.00084048, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 129.91740893, 0.01883281, 129.91740893, 0.05649844, 90.94218625, -1222.60561633, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 32.47935223, 8.405e-05, 97.4380567, 0.00025215, 324.79352234, 0.00084048, -32.47935223, -8.405e-05, -97.4380567, -0.00025215, -324.79352234, -0.00084048, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 25.2, 0.0, 6.7)
    ops.node(123005, 25.2, 0.0, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 30722261.99766035, 12800942.49902515, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 131.7093766, 0.00091963, 158.04630767, 0.00884022, 15.80463077, 0.0349355, -131.7093766, -0.00091963, -158.04630767, -0.00884022, -15.80463077, -0.0349355, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 131.7093766, 0.00091963, 158.04630767, 0.00884022, 15.80463077, 0.0349355, -131.7093766, -0.00091963, -158.04630767, -0.00884022, -15.80463077, -0.0349355, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 108.56155381, 0.01839258, 108.56155381, 0.05517775, 75.99308767, -1055.43971675, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 27.14038845, 6.646e-05, 81.42116536, 0.00019938, 271.40388453, 0.00066461, -27.14038845, -6.646e-05, -81.42116536, -0.00019938, -271.40388453, -0.00066461, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 108.56155381, 0.01839258, 108.56155381, 0.05517775, 75.99308767, -1055.43971675, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 27.14038845, 6.646e-05, 81.42116536, 0.00019938, 271.40388453, 0.00066461, -27.14038845, -6.646e-05, -81.42116536, -0.00019938, -271.40388453, -0.00066461, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 32.6, 0.0, 6.7)
    ops.node(123006, 32.6, 0.0, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 29509492.97083487, 12295622.07118119, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 54.18536017, 0.00129384, 65.05771168, 0.01320655, 6.50577117, 0.05012346, -54.18536017, -0.00129384, -65.05771168, -0.01320655, -6.50577117, -0.05012346, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 54.18536017, 0.00129384, 65.05771168, 0.01320655, 6.50577117, 0.05012346, -54.18536017, -0.00129384, -65.05771168, -0.01320655, -6.50577117, -0.05012346, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 79.34958201, 0.02587671, 79.34958201, 0.07763014, 55.54470741, -1009.71549092, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 19.8373955, 9.913e-05, 59.51218651, 0.00029738, 198.37395502, 0.00099125, -19.8373955, -9.913e-05, -59.51218651, -0.00029738, -198.37395502, -0.00099125, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 79.34958201, 0.02587671, 79.34958201, 0.07763014, 55.54470741, -1009.71549092, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 19.8373955, 9.913e-05, 59.51218651, 0.00029738, 198.37395502, 0.00099125, -19.8373955, -9.913e-05, -59.51218651, -0.00029738, -198.37395502, -0.00099125, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 3.5, 6.725)
    ops.node(123007, 0.0, 3.5, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 32469025.9492538, 13528760.81218908, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 66.76090557, 0.00129027, 79.35221476, 0.01106903, 7.93522148, 0.04725812, -66.76090557, -0.00129027, -79.35221476, -0.01106903, -7.93522148, -0.04725812, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 66.76090557, 0.00129027, 79.35221476, 0.01106903, 7.93522148, 0.04725812, -66.76090557, -0.00129027, -79.35221476, -0.01106903, -7.93522148, -0.04725812, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 77.50154401, 0.02580547, 77.50154401, 0.07741642, 54.25108081, -1012.95686774, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 19.375386, 8.799e-05, 58.12615801, 0.00026398, 193.75386003, 0.00087992, -19.375386, -8.799e-05, -58.12615801, -0.00026398, -193.75386003, -0.00087992, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 77.50154401, 0.02580547, 77.50154401, 0.07741642, 54.25108081, -1012.95686774, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 19.375386, 8.799e-05, 58.12615801, 0.00026398, 193.75386003, 0.00087992, -19.375386, -8.799e-05, -58.12615801, -0.00026398, -193.75386003, -0.00087992, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 7.4, 3.5, 6.725)
    ops.node(123008, 7.4, 3.5, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 29547896.73788899, 12311623.64078708, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 151.00325242, 0.0009375, 181.03718114, 0.00952022, 18.10371811, 0.03241688, -151.00325242, -0.0009375, -181.03718114, -0.00952022, -18.10371811, -0.03241688, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 151.00325242, 0.0009375, 181.03718114, 0.00952022, 18.10371811, 0.03241688, -151.00325242, -0.0009375, -181.03718114, -0.00952022, -18.10371811, -0.03241688, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 131.69803536, 0.01874998, 131.69803536, 0.05624995, 92.18862475, -1264.14377919, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 32.92450884, 8.383e-05, 98.77352652, 0.00025149, 329.2450884, 0.0008383, -32.92450884, -8.383e-05, -98.77352652, -0.00025149, -329.2450884, -0.0008383, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 131.69803536, 0.01874998, 131.69803536, 0.05624995, 92.18862475, -1264.14377919, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 32.92450884, 8.383e-05, 98.77352652, 0.00025149, 329.2450884, 0.0008383, -32.92450884, -8.383e-05, -98.77352652, -0.00025149, -329.2450884, -0.0008383, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 14.8, 3.5, 6.725)
    ops.node(123009, 14.8, 3.5, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 27001247.05718, 11250519.60715833, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 117.55820086, 0.00090033, 141.74767793, 0.01112522, 14.17476779, 0.03816406, -117.55820086, -0.00090033, -141.74767793, -0.01112522, -14.17476779, -0.03816406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 111.49288075, 0.00090033, 134.43432135, 0.01112522, 13.44343214, 0.03816406, -111.49288075, -0.00090033, -134.43432135, -0.01112522, -13.44343214, -0.03816406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 130.0803401, 0.01800654, 130.0803401, 0.05401961, 91.05623807, -1421.5447311, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 32.52008503, 9.061e-05, 97.56025508, 0.00027183, 325.20085026, 0.0009061, -32.52008503, -9.061e-05, -97.56025508, -0.00027183, -325.20085026, -0.0009061, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 130.0803401, 0.01800654, 130.0803401, 0.05401961, 91.05623807, -1421.5447311, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 32.52008503, 9.061e-05, 97.56025508, 0.00027183, 325.20085026, 0.0009061, -32.52008503, -9.061e-05, -97.56025508, -0.00027183, -325.20085026, -0.0009061, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 17.8, 3.5, 6.725)
    ops.node(123010, 17.8, 3.5, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 28756295.38523661, 11981789.74384859, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 119.5862311, 0.00096387, 144.03834828, 0.00998709, 14.40383483, 0.03980951, -119.5862311, -0.00096387, -144.03834828, -0.00998709, -14.40383483, -0.03980951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 113.93228071, 0.00096387, 137.22831951, 0.00998709, 13.72283195, 0.03980951, -113.93228071, -0.00096387, -137.22831951, -0.00998709, -13.72283195, -0.03980951, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 130.35020643, 0.01927734, 130.35020643, 0.05783203, 91.2451445, -1273.02826035, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 32.58755161, 8.526e-05, 97.76265483, 0.00025577, 325.87551609, 0.00085256, -32.58755161, -8.526e-05, -97.76265483, -0.00025577, -325.87551609, -0.00085256, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 130.35020643, 0.01927734, 130.35020643, 0.05783203, 91.2451445, -1273.02826035, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 32.58755161, 8.526e-05, 97.76265483, 0.00025577, 325.87551609, 0.00085256, -32.58755161, -8.526e-05, -97.76265483, -0.00025577, -325.87551609, -0.00085256, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 25.2, 3.5, 6.725)
    ops.node(123011, 25.2, 3.5, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 31241751.10258349, 13017396.29274312, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 145.1248755, 0.00095679, 173.58220689, 0.00875026, 17.35822069, 0.03364252, -145.1248755, -0.00095679, -173.58220689, -0.00875026, -17.35822069, -0.03364252, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 145.1248755, 0.00095679, 173.58220689, 0.00875026, 17.35822069, 0.03364252, -145.1248755, -0.00095679, -173.58220689, -0.00875026, -17.35822069, -0.03364252, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 123.3730809, 0.01913581, 123.3730809, 0.05740744, 86.36115663, -1184.62303675, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 30.84327023, 7.427e-05, 92.52981068, 0.00022282, 308.43270226, 0.00074273, -30.84327023, -7.427e-05, -92.52981068, -0.00022282, -308.43270226, -0.00074273, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 123.3730809, 0.01913581, 123.3730809, 0.05740744, 86.36115663, -1184.62303675, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 30.84327023, 7.427e-05, 92.52981068, 0.00022282, 308.43270226, 0.00074273, -30.84327023, -7.427e-05, -92.52981068, -0.00022282, -308.43270226, -0.00074273, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 32.6, 3.5, 6.725)
    ops.node(123012, 32.6, 3.5, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 28937022.7861094, 12057092.82754558, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 64.93859377, 0.00129371, 77.4636729, 0.0102603, 7.74636729, 0.03927204, -64.93859377, -0.00129371, -77.4636729, -0.0102603, -7.74636729, -0.03927204, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 64.93859377, 0.00129371, 77.4636729, 0.0102603, 7.74636729, 0.03927204, -64.93859377, -0.00129371, -77.4636729, -0.0102603, -7.74636729, -0.03927204, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 63.84783531, 0.02587413, 63.84783531, 0.07762238, 44.69348472, -1019.72398585, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 15.96195883, 8.134e-05, 47.88587648, 0.00024401, 159.61958828, 0.00081338, -15.96195883, -8.134e-05, -47.88587648, -0.00024401, -159.61958828, -0.00081338, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 63.84783531, 0.02587413, 63.84783531, 0.07762238, 44.69348472, -1019.72398585, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 15.96195883, 8.134e-05, 47.88587648, 0.00024401, 159.61958828, 0.00081338, -15.96195883, -8.134e-05, -47.88587648, -0.00024401, -159.61958828, -0.00081338, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 7.0, 6.725)
    ops.node(123013, 0.0, 7.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 26152220.18426416, 10896758.41011007, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 62.57492875, 0.00137238, 74.45032776, 0.01078362, 7.44503278, 0.03275043, -62.57492875, -0.00137238, -74.45032776, -0.01078362, -7.44503278, -0.03275043, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 62.57492875, 0.00137238, 74.45032776, 0.01078362, 7.44503278, 0.03275043, -62.57492875, -0.00137238, -74.45032776, -0.01078362, -7.44503278, -0.03275043, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 76.24549865, 0.02744768, 76.24549865, 0.08234304, 53.37184906, -1064.16777009, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 19.06137466, 0.00010748, 57.18412399, 0.00032243, 190.61374663, 0.00107475, -19.06137466, -0.00010748, -57.18412399, -0.00032243, -190.61374663, -0.00107475, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 76.24549865, 0.02744768, 76.24549865, 0.08234304, 53.37184906, -1064.16777009, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 19.06137466, 0.00010748, 57.18412399, 0.00032243, 190.61374663, 0.00107475, -19.06137466, -0.00010748, -57.18412399, -0.00032243, -190.61374663, -0.00107475, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 7.4, 7.0, 6.725)
    ops.node(123014, 7.4, 7.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1225, 28172494.4326057, 11738539.34691904, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 143.63555118, 0.00094415, 172.35164166, 0.00967319, 17.23516417, 0.03070686, -143.63555118, -0.00094415, -172.35164166, -0.00967319, -17.23516417, -0.03070686, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 143.63555118, 0.00094415, 172.35164166, 0.00967319, 17.23516417, 0.03070686, -143.63555118, -0.00094415, -172.35164166, -0.00967319, -17.23516417, -0.03070686, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 129.45203881, 0.01888294, 129.45203881, 0.05664881, 90.61642717, -1291.8755526, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 32.3630097, 8.642e-05, 97.08902911, 0.00025927, 323.63009703, 0.00086423, -32.3630097, -8.642e-05, -97.08902911, -0.00025927, -323.63009703, -0.00086423, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 129.45203881, 0.01888294, 129.45203881, 0.05664881, 90.61642717, -1291.8755526, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 32.3630097, 8.642e-05, 97.08902911, 0.00025927, 323.63009703, 0.00086423, -32.3630097, -8.642e-05, -97.08902911, -0.00025927, -323.63009703, -0.00086423, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 14.8, 7.0, 6.725)
    ops.node(123015, 14.8, 7.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 26829606.16751771, 11179002.56979905, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 67.2409249, 0.00136284, 79.993778, 0.00939078, 7.9993778, 0.03228865, -67.2409249, -0.00136284, -79.993778, -0.00939078, -7.9993778, -0.03228865, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 67.2409249, 0.00136284, 79.993778, 0.00939078, 7.9993778, 0.03228865, -67.2409249, -0.00136284, -79.993778, -0.00939078, -7.9993778, -0.03228865, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 59.91325848, 0.02725679, 59.91325848, 0.08177036, 41.93928094, -994.51056142, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 14.97831462, 8.232e-05, 44.93494386, 0.00024696, 149.78314621, 0.00082321, -14.97831462, -8.232e-05, -44.93494386, -0.00024696, -149.78314621, -0.00082321, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 59.91325848, 0.02725679, 59.91325848, 0.08177036, 41.93928094, -994.51056142, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 14.97831462, 8.232e-05, 44.93494386, 0.00024696, 149.78314621, 0.00082321, -14.97831462, -8.232e-05, -44.93494386, -0.00024696, -149.78314621, -0.00082321, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 17.8, 7.0, 6.725)
    ops.node(123016, 17.8, 7.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 34109029.68749252, 14212095.70312188, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 65.90503902, 0.00133025, 77.99628412, 0.0122018, 7.79962841, 0.05041928, -65.90503902, -0.00133025, -77.99628412, -0.0122018, -7.79962841, -0.05041928, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 65.90503902, 0.00133025, 77.99628412, 0.0122018, 7.79962841, 0.05041928, -65.90503902, -0.00133025, -77.99628412, -0.0122018, -7.79962841, -0.05041928, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 97.33748894, 0.02660503, 97.33748894, 0.07981508, 68.13624226, -1113.44514146, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 24.33437223, 0.0001052, 73.0031167, 0.0003156, 243.34372234, 0.00105199, -24.33437223, -0.0001052, -73.0031167, -0.0003156, -243.34372234, -0.00105199, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 97.33748894, 0.02660503, 97.33748894, 0.07981508, 68.13624226, -1113.44514146, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 24.33437223, 0.0001052, 73.0031167, 0.0003156, 243.34372234, 0.00105199, -24.33437223, -0.0001052, -73.0031167, -0.0003156, -243.34372234, -0.00105199, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 25.2, 7.0, 6.725)
    ops.node(123017, 25.2, 7.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.1225, 32875036.15571297, 13697931.73154707, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 147.60538077, 0.00091753, 175.936543, 0.00827716, 17.5936543, 0.03481282, -147.60538077, -0.00091753, -175.936543, -0.00827716, -17.5936543, -0.03481282, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 147.60538077, 0.00091753, 175.936543, 0.00827716, 17.5936543, 0.03481282, -147.60538077, -0.00091753, -175.936543, -0.00827716, -17.5936543, -0.03481282, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 123.53226121, 0.01835062, 123.53226121, 0.05505185, 86.47258285, -1143.7700687, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 30.8830653, 7.067e-05, 92.64919591, 0.00021202, 308.83065304, 0.00070674, -30.8830653, -7.067e-05, -92.64919591, -0.00021202, -308.83065304, -0.00070674, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 123.53226121, 0.01835062, 123.53226121, 0.05505185, 86.47258285, -1143.7700687, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 30.8830653, 7.067e-05, 92.64919591, 0.00021202, 308.83065304, 0.00070674, -30.8830653, -7.067e-05, -92.64919591, -0.00021202, -308.83065304, -0.00070674, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 32.6, 7.0, 6.725)
    ops.node(123018, 32.6, 7.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 30873640.36597519, 12864016.81915633, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 63.37879481, 0.00124833, 75.51616053, 0.01036546, 7.55161605, 0.04355962, -63.37879481, -0.00124833, -75.51616053, -0.01036546, -7.55161605, -0.04355962, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 63.37879481, 0.00124833, 75.51616053, 0.01036546, 7.55161605, 0.04355962, -63.37879481, -0.00124833, -75.51616053, -0.01036546, -7.55161605, -0.04355962, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 62.55055398, 0.02496666, 62.55055398, 0.07489997, 43.78538779, -910.16623037, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 15.6376385, 7.469e-05, 46.91291549, 0.00022406, 156.37638496, 0.00074687, -15.6376385, -7.469e-05, -46.91291549, -0.00022406, -156.37638496, -0.00074687, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 62.55055398, 0.02496666, 62.55055398, 0.07489997, 43.78538779, -910.16623037, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 15.6376385, 7.469e-05, 46.91291549, 0.00022406, 156.37638496, 0.00074687, -15.6376385, -7.469e-05, -46.91291549, -0.00022406, -156.37638496, -0.00074687, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 10.5, 6.7)
    ops.node(123019, 0.0, 10.5, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 29809683.56008601, 12420701.48336917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 56.25159848, 0.00121381, 67.51438546, 0.01210148, 6.75143855, 0.04957671, -56.25159848, -0.00121381, -67.51438546, -0.01210148, -6.75143855, -0.04957671, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 56.25159848, 0.00121381, 67.51438546, 0.01210148, 6.75143855, 0.04957671, -56.25159848, -0.00121381, -67.51438546, -0.01210148, -6.75143855, -0.04957671, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 67.38866649, 0.02427624, 67.38866649, 0.07282873, 47.17206655, -947.18491379, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 16.84716662, 8.334e-05, 50.54149987, 0.00025001, 168.47166623, 0.00083336, -16.84716662, -8.334e-05, -50.54149987, -0.00025001, -168.47166623, -0.00083336, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 67.38866649, 0.02427624, 67.38866649, 0.07282873, 47.17206655, -947.18491379, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 16.84716662, 8.334e-05, 50.54149987, 0.00025001, 168.47166623, 0.00083336, -16.84716662, -8.334e-05, -50.54149987, -0.00025001, -168.47166623, -0.00083336, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 7.4, 10.5, 6.7)
    ops.node(123020, 7.4, 10.5, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1225, 30651788.08610618, 12771578.36921091, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 125.12543493, 0.00093401, 150.16468234, 0.01006736, 15.01646823, 0.04156586, -125.12543493, -0.00093401, -150.16468234, -0.01006736, -15.01646823, -0.04156586, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 119.04171789, 0.00093401, 142.86353341, 0.01006736, 14.28635334, 0.04156586, -119.04171789, -0.00093401, -142.86353341, -0.01006736, -14.28635334, -0.04156586, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 139.23973755, 0.01868025, 139.23973755, 0.05604074, 97.46781629, -1293.04907308, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 34.80993439, 8.544e-05, 104.42980317, 0.00025632, 348.09934389, 0.00085439, -34.80993439, -8.544e-05, -104.42980317, -0.00025632, -348.09934389, -0.00085439, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 139.23973755, 0.01868025, 139.23973755, 0.05604074, 97.46781629, -1293.04907308, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 34.80993439, 8.544e-05, 104.42980317, 0.00025632, 348.09934389, 0.00085439, -34.80993439, -8.544e-05, -104.42980317, -0.00025632, -348.09934389, -0.00085439, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 14.8, 10.5, 6.7)
    ops.node(123021, 14.8, 10.5, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 27713405.78159033, 11547252.40899597, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 46.59915903, 0.00125522, 55.75793824, 0.01100442, 5.57579382, 0.0443839, -46.59915903, -0.00125522, -55.75793824, -0.01100442, -5.57579382, -0.0443839, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 46.59915903, 0.00125522, 55.75793824, 0.01100442, 5.57579382, 0.0443839, -46.59915903, -0.00125522, -55.75793824, -0.01100442, -5.57579382, -0.0443839, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 87.9113299, 0.02510432, 87.9113299, 0.07531296, 61.53793093, -1154.24423136, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 21.97783247, 0.00011694, 65.93349742, 0.00035082, 219.77832474, 0.00116938, -21.97783247, -0.00011694, -65.93349742, -0.00035082, -219.77832474, -0.00116938, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 87.9113299, 0.02510432, 87.9113299, 0.07531296, 61.53793093, -1154.24423136, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 21.97783247, 0.00011694, 65.93349742, 0.00035082, 219.77832474, 0.00116938, -21.97783247, -0.00011694, -65.93349742, -0.00035082, -219.77832474, -0.00116938, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 17.8, 10.5, 6.7)
    ops.node(123022, 17.8, 10.5, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0625, 28408137.80361635, 11836724.08484015, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 46.11549775, 0.00125793, 55.18461025, 0.01042703, 5.51846102, 0.04569835, -46.11549775, -0.00125793, -55.18461025, -0.01042703, -5.51846102, -0.04569835, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 46.11549775, 0.00125793, 55.18461025, 0.01042703, 5.51846102, 0.04569835, -46.11549775, -0.00125793, -55.18461025, -0.01042703, -5.51846102, -0.04569835, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 89.13689482, 0.02515863, 89.13689482, 0.07547588, 62.39582637, -1150.02927122, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 22.2842237, 0.00011567, 66.85267111, 0.00034701, 222.84223705, 0.00115669, -22.2842237, -0.00011567, -66.85267111, -0.00034701, -222.84223705, -0.00115669, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 89.13689482, 0.02515863, 89.13689482, 0.07547588, 62.39582637, -1150.02927122, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 22.2842237, 0.00011567, 66.85267111, 0.00034701, 222.84223705, 0.00115669, -22.2842237, -0.00011567, -66.85267111, -0.00034701, -222.84223705, -0.00115669, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 25.2, 10.5, 6.7)
    ops.node(123023, 25.2, 10.5, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 29458187.76720933, 12274244.90300389, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 121.10962847, 0.000843, 145.60714662, 0.01216712, 14.56071466, 0.04208012, -121.10962847, -0.000843, -145.60714662, -0.01216712, -14.56071466, -0.04208012, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 114.73711451, 0.000843, 137.94562882, 0.01216712, 13.79456288, 0.04208012, -114.73711451, -0.000843, -137.94562882, -0.01216712, -13.79456288, -0.04208012, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 146.81408547, 0.01686, 146.81408547, 0.05058, 102.76985983, -1581.18928467, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 36.70352137, 9.374e-05, 110.1105641, 0.00028121, 367.03521368, 0.00093736, -36.70352137, -9.374e-05, -110.1105641, -0.00028121, -367.03521368, -0.00093736, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 146.81408547, 0.01686, 146.81408547, 0.05058, 102.76985983, -1581.18928467, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 36.70352137, 9.374e-05, 110.1105641, 0.00028121, 367.03521368, 0.00093736, -36.70352137, -9.374e-05, -110.1105641, -0.00028121, -367.03521368, -0.00093736, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 32.6, 10.5, 6.7)
    ops.node(123024, 32.6, 10.5, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 28711573.28921484, 11963155.53717285, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 55.47468307, 0.00124411, 66.65502091, 0.01282296, 6.66550209, 0.04817584, -55.47468307, -0.00124411, -66.65502091, -0.01282296, -6.66550209, -0.04817584, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 55.47468307, 0.00124411, 66.65502091, 0.01282296, 6.66550209, 0.04817584, -55.47468307, -0.00124411, -66.65502091, -0.01282296, -6.66550209, -0.04817584, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 76.02447256, 0.02488228, 76.02447256, 0.07464685, 53.21713079, -1031.81995223, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 19.00611814, 9.761e-05, 57.01835442, 0.00029283, 190.06118139, 0.00097611, -19.00611814, -9.761e-05, -57.01835442, -0.00029283, -190.06118139, -0.00097611, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 76.02447256, 0.02488228, 76.02447256, 0.07464685, 53.21713079, -1031.81995223, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 19.00611814, 9.761e-05, 57.01835442, 0.00029283, 190.06118139, 0.00097611, -19.00611814, -9.761e-05, -57.01835442, -0.00029283, -190.06118139, -0.00097611, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.9)
    ops.node(124001, 0.0, 0.0, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26524091.41939091, 11051704.75807955, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 43.52271848, 0.00112013, 53.07594199, 0.01423919, 5.3075942, 0.06119123, -43.52271848, -0.00112013, -53.07594199, -0.01423919, -5.3075942, -0.06119123, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 43.52271848, 0.00112013, 53.07594199, 0.01423919, 5.3075942, 0.06119123, -43.52271848, -0.00112013, -53.07594199, -0.01423919, -5.3075942, -0.06119123, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 52.30363164, 0.02240266, 52.30363164, 0.06720798, 36.61254215, -1108.9656974, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 13.07590791, 7.269e-05, 39.22772373, 0.00021808, 130.7590791, 0.00072693, -13.07590791, -7.269e-05, -39.22772373, -0.00021808, -130.7590791, -0.00072693, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 52.30363164, 0.02240266, 52.30363164, 0.06720798, 36.61254215, -1108.9656974, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 13.07590791, 7.269e-05, 39.22772373, 0.00021808, 130.7590791, 0.00072693, -13.07590791, -7.269e-05, -39.22772373, -0.00021808, -130.7590791, -0.00072693, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 7.4, 0.0, 9.9)
    ops.node(124002, 7.4, 0.0, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1225, 33340524.8414375, 13891885.35059896, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 102.27177523, 0.00083422, 122.7048029, 0.01054158, 12.27048029, 0.04451907, -102.27177523, -0.00083422, -122.7048029, -0.01054158, -12.27048029, -0.04451907, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 102.27177523, 0.00083422, 122.7048029, 0.01054158, 12.27048029, 0.04451907, -102.27177523, -0.00083422, -122.7048029, -0.01054158, -12.27048029, -0.04451907, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 114.10874353, 0.01668432, 114.10874353, 0.05005296, 79.87612047, -972.54592985, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 28.52718588, 6.437e-05, 85.58155765, 0.00019311, 285.27185883, 0.00064371, -28.52718588, -6.437e-05, -85.58155765, -0.00019311, -285.27185883, -0.00064371, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 114.10874353, 0.01668432, 114.10874353, 0.05005296, 79.87612047, -972.54592985, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 28.52718588, 6.437e-05, 85.58155765, 0.00019311, 285.27185883, 0.00064371, -28.52718588, -6.437e-05, -85.58155765, -0.00019311, -285.27185883, -0.00064371, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 25.2, 0.0, 9.9)
    ops.node(124005, 25.2, 0.0, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 29093011.75661206, 12122088.23192169, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 104.22121501, 0.00084309, 126.53716606, 0.00978951, 12.65371661, 0.0419033, -104.22121501, -0.00084309, -126.53716606, -0.00978951, -12.65371661, -0.0419033, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 104.22121501, 0.00084309, 126.53716606, 0.00978951, 12.65371661, 0.0419033, -104.22121501, -0.00084309, -126.53716606, -0.00978951, -12.65371661, -0.0419033, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 82.99044758, 0.01686178, 82.99044758, 0.05058534, 58.09331331, -853.44399077, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 20.7476119, 5.365e-05, 62.24283569, 0.00016096, 207.47611896, 0.00053652, -20.7476119, -5.365e-05, -62.24283569, -0.00016096, -207.47611896, -0.00053652, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 82.99044758, 0.01686178, 82.99044758, 0.05058534, 58.09331331, -853.44399077, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 20.7476119, 5.365e-05, 62.24283569, 0.00016096, 207.47611896, 0.00053652, -20.7476119, -5.365e-05, -62.24283569, -0.00016096, -207.47611896, -0.00053652, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 32.6, 0.0, 9.9)
    ops.node(124006, 32.6, 0.0, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 29369354.30670407, 12237230.96112669, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 41.71601097, 0.00116216, 50.61555173, 0.01244967, 5.06155517, 0.06235765, -41.71601097, -0.00116216, -50.61555173, -0.01244967, -5.06155517, -0.06235765, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 41.71601097, 0.00116216, 50.61555173, 0.01244967, 5.06155517, 0.06235765, -41.71601097, -0.00116216, -50.61555173, -0.01244967, -5.06155517, -0.06235765, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 41.23406133, 0.02324314, 41.23406133, 0.06972942, 28.86384293, -903.25038202, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 10.30851533, 5.176e-05, 30.925546, 0.00015527, 103.08515333, 0.00051756, -10.30851533, -5.176e-05, -30.925546, -0.00015527, -103.08515333, -0.00051756, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 41.23406133, 0.02324314, 41.23406133, 0.06972942, 28.86384293, -903.25038202, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 10.30851533, 5.176e-05, 30.925546, 0.00015527, 103.08515333, 0.00051756, -10.30851533, -5.176e-05, -30.925546, -0.00015527, -103.08515333, -0.00051756, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 3.5, 9.925)
    ops.node(124007, 0.0, 3.5, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 28556396.76498147, 11898498.65207561, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 44.76641034, 0.00125237, 54.16773749, 0.01457885, 5.41677375, 0.05763593, -44.76641034, -0.00125237, -54.16773749, -0.01457885, -5.41677375, -0.05763593, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 44.76641034, 0.00125237, 54.16773749, 0.01457885, 5.41677375, 0.05763593, -44.76641034, -0.00125237, -54.16773749, -0.01457885, -5.41677375, -0.05763593, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 73.90428687, 0.02504735, 73.90428687, 0.07514206, 51.73300081, -1104.68262713, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 18.47607172, 9.54e-05, 55.42821515, 0.00028621, 184.76071717, 0.00095404, -18.47607172, -9.54e-05, -55.42821515, -0.00028621, -184.76071717, -0.00095404, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 73.90428687, 0.02504735, 73.90428687, 0.07514206, 51.73300081, -1104.68262713, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 18.47607172, 9.54e-05, 55.42821515, 0.00028621, 184.76071717, 0.00095404, -18.47607172, -9.54e-05, -55.42821515, -0.00028621, -184.76071717, -0.00095404, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 7.4, 3.5, 9.925)
    ops.node(124008, 7.4, 3.5, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 28238947.50153174, 11766228.12563823, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 108.07005928, 0.00089262, 131.01061212, 0.01106801, 13.10106121, 0.0397553, -108.07005928, -0.00089262, -131.01061212, -0.01106801, -13.10106121, -0.0397553, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 108.07005928, 0.00089262, 131.01061212, 0.01106801, 13.10106121, 0.0397553, -108.07005928, -0.00089262, -131.01061212, -0.01106801, -13.10106121, -0.0397553, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 109.94562604, 0.01785238, 109.94562604, 0.05355715, 76.96193823, -1051.01096577, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 27.48640651, 7.323e-05, 82.45921953, 0.00021968, 274.86406509, 0.00073228, -27.48640651, -7.323e-05, -82.45921953, -0.00021968, -274.86406509, -0.00073228, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 109.94562604, 0.01785238, 109.94562604, 0.05355715, 76.96193823, -1051.01096577, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 27.48640651, 7.323e-05, 82.45921953, 0.00021968, 274.86406509, 0.00073228, -27.48640651, -7.323e-05, -82.45921953, -0.00021968, -274.86406509, -0.00073228, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 14.8, 3.5, 9.925)
    ops.node(124009, 14.8, 3.5, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 28849828.05117931, 12020761.68799138, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 92.13934379, 0.00085908, 111.82288764, 0.01328519, 11.18228876, 0.05093985, -92.13934379, -0.00085908, -111.82288764, -0.01328519, -11.18228876, -0.05093985, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 86.57903732, 0.00085908, 105.07474401, 0.01328519, 10.5074744, 0.05093985, -86.57903732, -0.00085908, -105.07474401, -0.01328519, -10.5074744, -0.05093985, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 127.86035437, 0.01718169, 127.86035437, 0.05154506, 89.50224806, -1632.50687098, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 31.96508859, 8.336e-05, 95.89526578, 0.00025007, 319.65088593, 0.00083356, -31.96508859, -8.336e-05, -95.89526578, -0.00025007, -319.65088593, -0.00083356, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 127.86035437, 0.01718169, 127.86035437, 0.05154506, 89.50224806, -1632.50687098, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 31.96508859, 8.336e-05, 95.89526578, 0.00025007, 319.65088593, 0.00083356, -31.96508859, -8.336e-05, -95.89526578, -0.00025007, -319.65088593, -0.00083356, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 17.8, 3.5, 9.925)
    ops.node(124010, 17.8, 3.5, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 31096026.82304648, 12956677.84293604, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 90.48999336, 0.00082381, 109.24862844, 0.01240312, 10.92486284, 0.05164163, -90.48999336, -0.00082381, -109.24862844, -0.01240312, -10.92486284, -0.05164163, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 85.04432127, 0.00082381, 102.67406495, 0.01240312, 10.2674065, 0.05164163, -85.04432127, -0.00082381, -102.67406495, -0.01240312, -10.2674065, -0.05164163, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 128.98560276, 0.01647619, 128.98560276, 0.04942857, 90.28992193, -1366.20900226, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 32.24640069, 7.802e-05, 96.73920207, 0.00023405, 322.4640069, 0.00078016, -32.24640069, -7.802e-05, -96.73920207, -0.00023405, -322.4640069, -0.00078016, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 128.98560276, 0.01647619, 128.98560276, 0.04942857, 90.28992193, -1366.20900226, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 32.24640069, 7.802e-05, 96.73920207, 0.00023405, 322.4640069, 0.00078016, -32.24640069, -7.802e-05, -96.73920207, -0.00023405, -322.4640069, -0.00078016, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 25.2, 3.5, 9.925)
    ops.node(124011, 25.2, 3.5, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 30488544.4621688, 12703560.19257033, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 121.34933955, 0.00087033, 146.47933369, 0.00894427, 14.64793337, 0.039414, -121.34933955, -0.00087033, -146.47933369, -0.00894427, -14.64793337, -0.039414, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 121.34933955, 0.00087033, 146.47933369, 0.00894427, 14.64793337, 0.039414, -121.34933955, -0.00087033, -146.47933369, -0.00894427, -14.64793337, -0.039414, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 95.49873135, 0.01740664, 95.49873135, 0.05221993, 66.84911194, -891.03240179, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 23.87468284, 5.891e-05, 71.62404851, 0.00017674, 238.74682837, 0.00058912, -23.87468284, -5.891e-05, -71.62404851, -0.00017674, -238.74682837, -0.00058912, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 95.49873135, 0.01740664, 95.49873135, 0.05221993, 66.84911194, -891.03240179, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 23.87468284, 5.891e-05, 71.62404851, 0.00017674, 238.74682837, 0.00058912, -23.87468284, -5.891e-05, -71.62404851, -0.00017674, -238.74682837, -0.00058912, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 32.6, 3.5, 9.925)
    ops.node(124012, 32.6, 3.5, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 28815020.79176477, 12006258.66323532, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 46.65029083, 0.00121298, 56.42524691, 0.0130234, 5.64252469, 0.05646281, -46.65029083, -0.00121298, -56.42524691, -0.0130234, -5.64252469, -0.05646281, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 46.65029083, 0.00121298, 56.42524691, 0.0130234, 5.64252469, 0.05646281, -46.65029083, -0.00121298, -56.42524691, -0.0130234, -5.64252469, -0.05646281, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 57.12624195, 0.02425955, 57.12624195, 0.07277864, 39.98836937, -922.87413205, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 14.28156049, 7.308e-05, 42.84468146, 0.00021925, 142.81560488, 0.00073083, -14.28156049, -7.308e-05, -42.84468146, -0.00021925, -142.81560488, -0.00073083, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 57.12624195, 0.02425955, 57.12624195, 0.07277864, 39.98836937, -922.87413205, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 14.28156049, 7.308e-05, 42.84468146, 0.00021925, 142.81560488, 0.00073083, -14.28156049, -7.308e-05, -42.84468146, -0.00021925, -142.81560488, -0.00073083, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 7.0, 9.925)
    ops.node(124013, 0.0, 7.0, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 25682464.47562659, 10701026.86484441, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 47.90276089, 0.00121659, 58.10504913, 0.01431121, 5.81050491, 0.05224623, -47.90276089, -0.00121659, -58.10504913, -0.01431121, -5.81050491, -0.05224623, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 47.90276089, 0.00121659, 58.10504913, 0.01431121, 5.81050491, 0.05224623, -47.90276089, -0.00121659, -58.10504913, -0.01431121, -5.81050491, -0.05224623, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 70.41699497, 0.02433181, 70.41699497, 0.07299542, 49.29189648, -1067.1951391, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 17.60424874, 0.00010107, 52.81274623, 0.00030322, 176.04248742, 0.00101075, -17.60424874, -0.00010107, -52.81274623, -0.00030322, -176.04248742, -0.00101075, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 70.41699497, 0.02433181, 70.41699497, 0.07299542, 49.29189648, -1067.1951391, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 17.60424874, 0.00010107, 52.81274623, 0.00030322, 176.04248742, 0.00101075, -17.60424874, -0.00010107, -52.81274623, -0.00030322, -176.04248742, -0.00101075, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 7.4, 7.0, 9.925)
    ops.node(124014, 7.4, 7.0, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1225, 30854831.70625789, 12856179.87760746, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 113.56332981, 0.00087415, 136.96235174, 0.01015211, 13.69623517, 0.04086907, -113.56332981, -0.00087415, -136.96235174, -0.01015211, -13.69623517, -0.04086907, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 113.56332981, 0.00087415, 136.96235174, 0.01015211, 13.69623517, 0.04086907, -113.56332981, -0.00087415, -136.96235174, -0.01015211, -13.69623517, -0.04086907, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 110.10335602, 0.01748309, 110.10335602, 0.05244926, 77.07234922, -975.39403882, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 27.52583901, 6.712e-05, 82.57751702, 0.00020135, 275.25839006, 0.00067116, -27.52583901, -6.712e-05, -82.57751702, -0.00020135, -275.25839006, -0.00067116, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 110.10335602, 0.01748309, 110.10335602, 0.05244926, 77.07234922, -975.39403882, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 27.52583901, 6.712e-05, 82.57751702, 0.00020135, 275.25839006, 0.00067116, -27.52583901, -6.712e-05, -82.57751702, -0.00020135, -275.25839006, -0.00067116, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 14.8, 7.0, 9.925)
    ops.node(124015, 14.8, 7.0, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 28288923.7208566, 11787051.55035692, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 48.94289418, 0.00123424, 59.13629832, 0.011658, 5.91362983, 0.05206444, -48.94289418, -0.00123424, -59.13629832, -0.011658, -5.91362983, -0.05206444, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 48.94289418, 0.00123424, 59.13629832, 0.011658, 5.91362983, 0.05206444, -48.94289418, -0.00123424, -59.13629832, -0.011658, -5.91362983, -0.05206444, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 46.96083044, 0.0246847, 46.96083044, 0.0740541, 32.87258131, -806.21579951, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 11.74020761, 6.12e-05, 35.22062283, 0.00018359, 117.40207611, 0.00061196, -11.74020761, -6.12e-05, -35.22062283, -0.00018359, -117.40207611, -0.00061196, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 46.96083044, 0.0246847, 46.96083044, 0.0740541, 32.87258131, -806.21579951, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 11.74020761, 6.12e-05, 35.22062283, 0.00018359, 117.40207611, 0.00061196, -11.74020761, -6.12e-05, -35.22062283, -0.00018359, -117.40207611, -0.00061196, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 17.8, 7.0, 9.925)
    ops.node(124016, 17.8, 7.0, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 29721660.9941299, 12384025.41422079, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 50.52390419, 0.0011804, 60.92103412, 0.01152272, 6.09210341, 0.05421322, -50.52390419, -0.0011804, -60.92103412, -0.01152272, -6.09210341, -0.05421322, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 50.52390419, 0.0011804, 60.92103412, 0.01152272, 6.09210341, 0.05421322, -50.52390419, -0.0011804, -60.92103412, -0.01152272, -6.09210341, -0.05421322, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 48.69895474, 0.02360791, 48.69895474, 0.07082372, 34.08926832, -806.19138625, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 12.17473869, 6.04e-05, 36.52421606, 0.00018121, 121.74738686, 0.00060402, -12.17473869, -6.04e-05, -36.52421606, -0.00018121, -121.74738686, -0.00060402, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 48.69895474, 0.02360791, 48.69895474, 0.07082372, 34.08926832, -806.19138625, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 12.17473869, 6.04e-05, 36.52421606, 0.00018121, 121.74738686, 0.00060402, -12.17473869, -6.04e-05, -36.52421606, -0.00018121, -121.74738686, -0.00060402, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 25.2, 7.0, 9.925)
    ops.node(124017, 25.2, 7.0, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.1225, 26109851.63553866, 10879104.84814111, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 110.53125072, 0.00089026, 134.3036188, 0.0093266, 13.43036188, 0.03581265, -110.53125072, -0.00089026, -134.3036188, -0.0093266, -13.43036188, -0.03581265, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 110.53125072, 0.00089026, 134.3036188, 0.0093266, 13.43036188, 0.03581265, -110.53125072, -0.00089026, -134.3036188, -0.0093266, -13.43036188, -0.03581265, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 80.41012871, 0.01780522, 80.41012871, 0.05341565, 56.2870901, -873.62323701, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 20.10253218, 5.792e-05, 60.30759654, 0.00017377, 201.02532178, 0.00057923, -20.10253218, -5.792e-05, -60.30759654, -0.00017377, -201.02532178, -0.00057923, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 80.41012871, 0.01780522, 80.41012871, 0.05341565, 56.2870901, -873.62323701, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 20.10253218, 5.792e-05, 60.30759654, 0.00017377, 201.02532178, 0.00057923, -20.10253218, -5.792e-05, -60.30759654, -0.00017377, -201.02532178, -0.00057923, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 32.6, 7.0, 9.925)
    ops.node(124018, 32.6, 7.0, 12.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 30098005.68731456, 12540835.70304773, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 47.56139848, 0.00118989, 57.39455413, 0.0123781, 5.73945541, 0.05755249, -47.56139848, -0.00118989, -57.39455413, -0.0123781, -5.73945541, -0.05755249, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 47.56139848, 0.00118989, 57.39455413, 0.0123781, 5.73945541, 0.05755249, -47.56139848, -0.00118989, -57.39455413, -0.0123781, -5.73945541, -0.05755249, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 53.74341422, 0.02379782, 53.74341422, 0.07139346, 37.62038995, -873.23106267, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 13.43585355, 6.582e-05, 40.30756066, 0.00019747, 134.35853555, 0.00065825, -13.43585355, -6.582e-05, -40.30756066, -0.00019747, -134.35853555, -0.00065825, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 53.74341422, 0.02379782, 53.74341422, 0.07139346, 37.62038995, -873.23106267, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 13.43585355, 6.582e-05, 40.30756066, 0.00019747, 134.35853555, 0.00065825, -13.43585355, -6.582e-05, -40.30756066, -0.00019747, -134.35853555, -0.00065825, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 10.5, 9.9)
    ops.node(124019, 0.0, 10.5, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 28852692.34581239, 12021955.1440885, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 41.82003886, 0.00114013, 50.7981585, 0.01489689, 5.07981585, 0.06434783, -41.82003886, -0.00114013, -50.7981585, -0.01489689, -5.07981585, -0.06434783, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 41.82003886, 0.00114013, 50.7981585, 0.01489689, 5.07981585, 0.06434783, -41.82003886, -0.00114013, -50.7981585, -0.01489689, -5.07981585, -0.06434783, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 63.25732367, 0.02280262, 63.25732367, 0.06840785, 44.28012657, -1171.34991875, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 15.81433092, 8.082e-05, 47.44299275, 0.00024246, 158.14330917, 0.00080822, -15.81433092, -8.082e-05, -47.44299275, -0.00024246, -158.14330917, -0.00080822, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 63.25732367, 0.02280262, 63.25732367, 0.06840785, 44.28012657, -1171.34991875, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 15.81433092, 8.082e-05, 47.44299275, 0.00024246, 158.14330917, 0.00080822, -15.81433092, -8.082e-05, -47.44299275, -0.00024246, -158.14330917, -0.00080822, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 7.4, 10.5, 9.9)
    ops.node(124020, 7.4, 10.5, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1225, 29338774.27776011, 12224489.28240005, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 88.12650234, 0.00087874, 106.93874999, 0.01099187, 10.693875, 0.0500295, -88.12650234, -0.00087874, -106.93874999, -0.01099187, -10.693875, -0.0500295, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 82.97086086, 0.00087874, 100.68254055, 0.01099187, 10.06825406, 0.0500295, -82.97086086, -0.00087874, -100.68254055, -0.01099187, -10.06825406, -0.0500295, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 114.86114833, 0.01757484, 114.86114833, 0.05272451, 80.40280383, -1201.5269242, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 28.71528708, 7.363e-05, 86.14586124, 0.0002209, 287.15287082, 0.00073634, -28.71528708, -7.363e-05, -86.14586124, -0.0002209, -287.15287082, -0.00073634, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 114.86114833, 0.01757484, 114.86114833, 0.05272451, 80.40280383, -1201.5269242, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 28.71528708, 7.363e-05, 86.14586124, 0.0002209, 287.15287082, 0.00073634, -28.71528708, -7.363e-05, -86.14586124, -0.0002209, -287.15287082, -0.00073634, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 14.8, 10.5, 9.9)
    ops.node(124021, 14.8, 10.5, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 28975582.9105846, 12073159.54607692, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 30.15084991, 0.00116471, 36.54807304, 0.01357984, 3.6548073, 0.06773967, -30.15084991, -0.00116471, -36.54807304, -0.01357984, -3.6548073, -0.06773967, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 30.15084991, 0.00116471, 36.54807304, 0.01357984, 3.6548073, 0.06773967, -30.15084991, -0.00116471, -36.54807304, -0.01357984, -3.6548073, -0.06773967, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 79.26643384, 0.02329421, 79.26643384, 0.06988264, 55.48650369, -1327.86447903, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 19.81660846, 0.00010085, 59.44982538, 0.00030254, 198.16608459, 0.00100846, -19.81660846, -0.00010085, -59.44982538, -0.00030254, -198.16608459, -0.00100846, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 79.26643384, 0.02329421, 79.26643384, 0.06988264, 55.48650369, -1327.86447903, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 19.81660846, 0.00010085, 59.44982538, 0.00030254, 198.16608459, 0.00100846, -19.81660846, -0.00010085, -59.44982538, -0.00030254, -198.16608459, -0.00100846, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 17.8, 10.5, 9.9)
    ops.node(124022, 17.8, 10.5, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0625, 28684934.03595847, 11952055.84831603, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 30.61735385, 0.00109194, 37.13351284, 0.01175938, 3.71335128, 0.06552837, -30.61735385, -0.00109194, -37.13351284, -0.01175938, -3.71335128, -0.06552837, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 30.61735385, 0.00109194, 37.13351284, 0.01175938, 3.71335128, 0.06552837, -30.61735385, -0.00109194, -37.13351284, -0.01175938, -3.71335128, -0.06552837, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 66.94854394, 0.02183878, 66.94854394, 0.06551635, 46.86398076, -1044.67099712, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 16.73713598, 8.604e-05, 50.21140795, 0.00025811, 167.37135985, 0.00086038, -16.73713598, -8.604e-05, -50.21140795, -0.00025811, -167.37135985, -0.00086038, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 66.94854394, 0.02183878, 66.94854394, 0.06551635, 46.86398076, -1044.67099712, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 16.73713598, 8.604e-05, 50.21140795, 0.00025811, 167.37135985, 0.00086038, -16.73713598, -8.604e-05, -50.21140795, -0.00025811, -167.37135985, -0.00086038, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 25.2, 10.5, 9.9)
    ops.node(124023, 25.2, 10.5, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 29578212.84340128, 12324255.3514172, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 88.6591939, 0.00089774, 107.52691971, 0.01339389, 10.75269197, 0.05258861, -88.6591939, -0.00089774, -107.52691971, -0.01339389, -10.75269197, -0.05258861, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 83.59540099, 0.00089774, 101.38549173, 0.01339389, 10.13854917, 0.05258861, -83.59540099, -0.00089774, -101.38549173, -0.01339389, -10.13854917, -0.05258861, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 127.67240742, 0.01795475, 127.67240742, 0.05386426, 89.37068519, -1672.40860037, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 31.91810185, 8.118e-05, 95.75430556, 0.00024355, 319.18101855, 0.00081184, -31.91810185, -8.118e-05, -95.75430556, -0.00024355, -319.18101855, -0.00081184, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 127.67240742, 0.01795475, 127.67240742, 0.05386426, 89.37068519, -1672.40860037, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 31.91810185, 8.118e-05, 95.75430556, 0.00024355, 319.18101855, 0.00081184, -31.91810185, -8.118e-05, -95.75430556, -0.00024355, -319.18101855, -0.00081184, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 32.6, 10.5, 9.9)
    ops.node(124024, 32.6, 10.5, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 32946150.86175956, 13727562.85906648, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 45.20655191, 0.00107539, 54.30927271, 0.01462898, 5.43092727, 0.06699293, -45.20655191, -0.00107539, -54.30927271, -0.01462898, -5.43092727, -0.06699293, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 45.20655191, 0.00107539, 54.30927271, 0.01462898, 5.43092727, 0.06699293, -45.20655191, -0.00107539, -54.30927271, -0.01462898, -5.43092727, -0.06699293, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 79.59840455, 0.02150788, 79.59840455, 0.06452365, 55.71888318, -1316.97544259, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 19.89960114, 8.906e-05, 59.69880341, 0.00026719, 198.99601137, 0.00089064, -19.89960114, -8.906e-05, -59.69880341, -0.00026719, -198.99601137, -0.00089064, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 79.59840455, 0.02150788, 79.59840455, 0.06452365, 55.71888318, -1316.97544259, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 19.89960114, 8.906e-05, 59.69880341, 0.00026719, 198.99601137, 0.00089064, -19.89960114, -8.906e-05, -59.69880341, -0.00026719, -198.99601137, -0.00089064, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 14.8, 0.0, 0.0)
    ops.node(124025, 14.8, 0.0, 1.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.09, 27293166.79645327, 11372152.83185553, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 159.1235583, 0.00079167, 187.15910028, 0.00766146, 18.71591003, 0.02235156, -159.1235583, -0.00079167, -187.15910028, -0.00766146, -18.71591003, -0.02235156, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 147.11833125, 0.00079167, 173.03870529, 0.00766146, 17.30387053, 0.02235156, -147.11833125, -0.00079167, -173.03870529, -0.00766146, -17.30387053, -0.02235156, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 131.63764614, 0.01583344, 131.63764614, 0.04750032, 92.1463523, -2994.39335783, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 32.90941154, 6.174e-05, 98.72823461, 0.00018521, 329.09411536, 0.00061736, -32.90941154, -6.174e-05, -98.72823461, -0.00018521, -329.09411536, -0.00061736, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 131.63764614, 0.01583344, 131.63764614, 0.04750032, 92.1463523, -2994.39335783, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 32.90941154, 6.174e-05, 98.72823461, 0.00018521, 329.09411536, 0.00061736, -32.90941154, -6.174e-05, -98.72823461, -0.00018521, -329.09411536, -0.00061736, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 14.8, 0.0, 1.8)
    ops.node(121003, 14.8, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.09, 28507066.29469013, 11877944.28945422, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 138.71290312, 0.00076292, 163.89829958, 0.00949361, 16.38982996, 0.02790906, -138.71290312, -0.00076292, -163.89829958, -0.00949361, -16.38982996, -0.02790906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 126.89253597, 0.00076292, 149.93176847, 0.00949361, 14.99317685, 0.02790906, -126.89253597, -0.00076292, -149.93176847, -0.00949361, -14.99317685, -0.02790906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 146.46727778, 0.01525837, 146.46727778, 0.04577511, 102.52709445, -3241.64014741, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 36.61681945, 6.577e-05, 109.85045834, 0.0001973, 366.16819445, 0.00065765, -36.61681945, -6.577e-05, -109.85045834, -0.0001973, -366.16819445, -0.00065765, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 146.46727778, 0.01525837, 146.46727778, 0.04577511, 102.52709445, -3241.64014741, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 36.61681945, 6.577e-05, 109.85045834, 0.0001973, 366.16819445, 0.00065765, -36.61681945, -6.577e-05, -109.85045834, -0.0001973, -366.16819445, -0.00065765, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 17.8, 0.0, 0.0)
    ops.node(124026, 17.8, 0.0, 1.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.09, 26457465.97396301, 11023944.15581792, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 105.0734253, 0.00053412, 123.26151221, 0.00770953, 12.32615122, 0.02054232, -105.0734253, -0.00053412, -123.26151221, -0.00770953, -12.32615122, -0.02054232, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 98.64944051, 0.00053412, 115.72554317, 0.00770953, 11.57255432, 0.02054232, -98.64944051, -0.00053412, -115.72554317, -0.00770953, -11.57255432, -0.02054232, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 136.23215169, 0.0106824, 136.23215169, 0.0320472, 95.36250618, -3152.43848915, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 34.05803792, 6.591e-05, 102.17411377, 0.00019773, 340.58037923, 0.00065908, -34.05803792, -6.591e-05, -102.17411377, -0.00019773, -340.58037923, -0.00065908, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 136.23215169, 0.0106824, 136.23215169, 0.0320472, 95.36250618, -3152.43848915, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 34.05803792, 6.591e-05, 102.17411377, 0.00019773, 340.58037923, 0.00065908, -34.05803792, -6.591e-05, -102.17411377, -0.00019773, -340.58037923, -0.00065908, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 17.8, 0.0, 1.8)
    ops.node(121004, 17.8, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.09, 30497822.19991756, 12707425.91663232, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 141.97009929, 0.00077133, 167.94709131, 0.00944318, 16.79470913, 0.03202192, -141.97009929, -0.00077133, -167.94709131, -0.00944318, -16.79470913, -0.03202192, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 130.01745162, 0.00077133, 153.80740683, 0.00944318, 15.38074068, 0.03202192, -130.01745162, -0.00077133, -153.80740683, -0.00944318, -15.38074068, -0.03202192, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 152.46742656, 0.01542651, 152.46742656, 0.04627953, 106.72719859, -3176.97037097, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 38.11685664, 6.399e-05, 114.35056992, 0.00019197, 381.16856639, 0.00063991, -38.11685664, -6.399e-05, -114.35056992, -0.00019197, -381.16856639, -0.00063991, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 152.46742656, 0.01542651, 152.46742656, 0.04627953, 106.72719859, -3176.97037097, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 38.11685664, 6.399e-05, 114.35056992, 0.00019197, 381.16856639, 0.00063991, -38.11685664, -6.399e-05, -114.35056992, -0.00019197, -381.16856639, -0.00063991, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 14.8, 0.0, 3.5)
    ops.node(124027, 14.8, 0.0, 4.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.09, 30074904.86349335, 12531210.3597889, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 113.6814466, 0.00074718, 135.33088071, 0.01022476, 13.53308807, 0.0364449, -113.6814466, -0.00074718, -135.33088071, -0.01022476, -13.53308807, -0.0364449, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 108.2069597, 0.00074718, 128.81383544, 0.01022476, 12.88138354, 0.0364449, -108.2069597, -0.00074718, -128.81383544, -0.01022476, -12.88138354, -0.0364449, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 139.89740186, 0.01494355, 139.89740186, 0.04483066, 97.92818131, -2773.284723, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 34.97435047, 5.954e-05, 104.9230514, 0.00017862, 349.74350466, 0.00059541, -34.97435047, -5.954e-05, -104.9230514, -0.00017862, -349.74350466, -0.00059541, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 139.89740186, 0.01494355, 139.89740186, 0.04483066, 97.92818131, -2773.284723, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 34.97435047, 5.954e-05, 104.9230514, 0.00017862, 349.74350466, 0.00059541, -34.97435047, -5.954e-05, -104.9230514, -0.00017862, -349.74350466, -0.00059541, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 14.8, 0.0, 5.0)
    ops.node(122003, 14.8, 0.0, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.09, 27992140.07958784, 11663391.69982827, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 108.73296605, 0.00075348, 129.67606877, 0.00981301, 12.96760688, 0.03317819, -108.73296605, -0.00075348, -129.67606877, -0.00981301, -12.96760688, -0.03317819, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 103.37485545, 0.00075348, 123.28593022, 0.00981301, 12.32859302, 0.03317819, -103.37485545, -0.00075348, -123.28593022, -0.00981301, -12.32859302, -0.03317819, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 127.88492474, 0.0150696, 127.88492474, 0.0452088, 89.51944732, -2606.91763753, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 31.97123118, 5.848e-05, 95.91369355, 0.00017543, 319.71231185, 0.00058478, -31.97123118, -5.848e-05, -95.91369355, -0.00017543, -319.71231185, -0.00058478, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 127.88492474, 0.0150696, 127.88492474, 0.0452088, 89.51944732, -2606.91763753, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 31.97123118, 5.848e-05, 95.91369355, 0.00017543, 319.71231185, 0.00058478, -31.97123118, -5.848e-05, -95.91369355, -0.00017543, -319.71231185, -0.00058478, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 17.8, 0.0, 3.5)
    ops.node(124028, 17.8, 0.0, 4.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.09, 28983819.67279368, 12076591.5303307, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 113.56444622, 0.000767, 135.21925708, 0.00945188, 13.52192571, 0.03350456, -113.56444622, -0.000767, -135.21925708, -0.00945188, -13.52192571, -0.03350456, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 108.18049142, 0.000767, 128.80867356, 0.00945188, 12.88086736, 0.03350456, -108.18049142, -0.000767, -128.80867356, -0.00945188, -12.88086736, -0.03350456, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 132.72608575, 0.01533996, 132.72608575, 0.04601989, 92.90826003, -2642.73693692, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 33.18152144, 5.862e-05, 99.54456431, 0.00017585, 331.81521438, 0.00058615, -33.18152144, -5.862e-05, -99.54456431, -0.00017585, -331.81521438, -0.00058615, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 132.72608575, 0.01533996, 132.72608575, 0.04601989, 92.90826003, -2642.73693692, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 33.18152144, 5.862e-05, 99.54456431, 0.00017585, 331.81521438, 0.00058615, -33.18152144, -5.862e-05, -99.54456431, -0.00017585, -331.81521438, -0.00058615, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 17.8, 0.0, 5.0)
    ops.node(122004, 17.8, 0.0, 6.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.09, 30008327.53956894, 12503469.80815372, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 104.16076687, 0.00069994, 124.2079114, 0.00954306, 12.42079114, 0.03696382, -104.16076687, -0.00069994, -124.2079114, -0.00954306, -12.42079114, -0.03696382, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 99.15915283, 0.00069994, 118.24366927, 0.00954306, 11.82436693, 0.03696382, -99.15915283, -0.00069994, -118.24366927, -0.00954306, -11.82436693, -0.03696382, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 127.93132401, 0.01399883, 127.93132401, 0.0419965, 89.55192681, -2495.36894012, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 31.982831, 5.457e-05, 95.94849301, 0.00016371, 319.82831003, 0.00054569, -31.982831, -5.457e-05, -95.94849301, -0.00016371, -319.82831003, -0.00054569, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 127.93132401, 0.01399883, 127.93132401, 0.0419965, 89.55192681, -2495.36894012, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 31.982831, 5.457e-05, 95.94849301, 0.00016371, 319.82831003, 0.00054569, -31.982831, -5.457e-05, -95.94849301, -0.00016371, -319.82831003, -0.00054569, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 14.8, 0.0, 6.7)
    ops.node(124029, 14.8, 0.0, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.0625, 30094446.48642823, 12539352.70267843, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 65.87547183, 0.00080723, 78.5533047, 0.01035584, 7.85533047, 0.0420138, -65.87547183, -0.00080723, -78.5533047, -0.01035584, -7.85533047, -0.0420138, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 65.87547183, 0.00080723, 78.5533047, 0.01035584, 7.85533047, 0.0420138, -65.87547183, -0.00080723, -78.5533047, -0.01035584, -7.85533047, -0.0420138, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 69.98743125, 0.01614458, 69.98743125, 0.04843373, 48.99120188, -1993.80645336, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 17.49685781, 4.287e-05, 52.49057344, 0.0001286, 174.96857814, 0.00042865, -17.49685781, -4.287e-05, -52.49057344, -0.0001286, -174.96857814, -0.00042865, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 69.98743125, 0.01614458, 69.98743125, 0.04843373, 48.99120188, -1993.80645336, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 17.49685781, 4.287e-05, 52.49057344, 0.0001286, 174.96857814, 0.00042865, -17.49685781, -4.287e-05, -52.49057344, -0.0001286, -174.96857814, -0.00042865, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 14.8, 0.0, 8.175)
    ops.node(123003, 14.8, 0.0, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.0625, 27721636.42604771, 11550681.84418655, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 61.69482039, 0.00086167, 73.82126494, 0.00949658, 7.38212649, 0.03846176, -61.69482039, -0.00086167, -73.82126494, -0.00949658, -7.38212649, -0.03846176, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 61.69482039, 0.00086167, 73.82126494, 0.00949658, 7.38212649, 0.03846176, -61.69482039, -0.00086167, -73.82126494, -0.00949658, -7.38212649, -0.03846176, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 54.25197304, 0.01723343, 54.25197304, 0.0517003, 37.97638113, -1788.96666486, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 13.56299326, 3.607e-05, 40.68897978, 0.00010822, 135.6299326, 0.00036072, -13.56299326, -3.607e-05, -40.68897978, -0.00010822, -135.6299326, -0.00036072, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 54.25197304, 0.01723343, 54.25197304, 0.0517003, 37.97638113, -1788.96666486, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 13.56299326, 3.607e-05, 40.68897978, 0.00010822, 135.6299326, 0.00036072, -13.56299326, -3.607e-05, -40.68897978, -0.00010822, -135.6299326, -0.00036072, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 17.8, 0.0, 6.7)
    ops.node(124030, 17.8, 0.0, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.0625, 31511334.20911921, 13129722.58713301, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 63.05776687, 0.00082701, 75.07682927, 0.01013654, 7.50768293, 0.04464373, -63.05776687, -0.00082701, -75.07682927, -0.01013654, -7.50768293, -0.04464373, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 63.05776687, 0.00082701, 75.07682927, 0.01013654, 7.50768293, 0.04464373, -63.05776687, -0.00082701, -75.07682927, -0.01013654, -7.50768293, -0.04464373, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 66.52309292, 0.01654013, 66.52309292, 0.04962038, 46.56616504, -1920.82692198, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 16.63077323, 3.891e-05, 49.89231969, 0.00011673, 166.30773229, 0.00038912, -16.63077323, -3.891e-05, -49.89231969, -0.00011673, -166.30773229, -0.00038912, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 66.52309292, 0.01654013, 66.52309292, 0.04962038, 46.56616504, -1920.82692198, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 16.63077323, 3.891e-05, 49.89231969, 0.00011673, 166.30773229, 0.00038912, -16.63077323, -3.891e-05, -49.89231969, -0.00011673, -166.30773229, -0.00038912, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 17.8, 0.0, 8.175)
    ops.node(123004, 17.8, 0.0, 9.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.0625, 30731220.86119926, 12804675.35883303, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 59.7421614, 0.00082561, 71.37225275, 0.01220111, 7.13722527, 0.04765306, -59.7421614, -0.00082561, -71.37225275, -0.01220111, -7.13722527, -0.04765306, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 59.7421614, 0.00082561, 71.37225275, 0.01220111, 7.13722527, 0.04765306, -59.7421614, -0.00082561, -71.37225275, -0.01220111, -7.13722527, -0.04765306, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 85.43753429, 0.01651218, 85.43753429, 0.04953654, 59.806274, -2107.48375498, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 21.35938357, 5.124e-05, 64.07815072, 0.00015373, 213.59383573, 0.00051244, -21.35938357, -5.124e-05, -64.07815072, -0.00015373, -213.59383573, -0.00051244, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 85.43753429, 0.01651218, 85.43753429, 0.04953654, 59.806274, -2107.48375498, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 21.35938357, 5.124e-05, 64.07815072, 0.00015373, 213.59383573, 0.00051244, -21.35938357, -5.124e-05, -64.07815072, -0.00015373, -213.59383573, -0.00051244, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 14.8, 0.0, 9.9)
    ops.node(124031, 14.8, 0.0, 11.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.0625, 27464014.03053401, 11443339.17938917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 48.43545408, 0.00075159, 58.7546779, 0.01306119, 5.87546779, 0.0558219, -48.43545408, -0.00075159, -58.7546779, -0.01306119, -5.87546779, -0.0558219, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 48.43545408, 0.00075159, 58.7546779, 0.01306119, 5.87546779, 0.0558219, -48.43545408, -0.00075159, -58.7546779, -0.01306119, -5.87546779, -0.0558219, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 58.86896699, 0.01503172, 58.86896699, 0.04509516, 41.20827689, -1995.99848259, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 14.71724175, 3.951e-05, 44.15172524, 0.00011853, 147.17241746, 0.00039509, -14.71724175, -3.951e-05, -44.15172524, -0.00011853, -147.17241746, -0.00039509, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 58.86896699, 0.01503172, 58.86896699, 0.04509516, 41.20827689, -1995.99848259, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 14.71724175, 3.951e-05, 44.15172524, 0.00011853, 147.17241746, 0.00039509, -14.71724175, -3.951e-05, -44.15172524, -0.00011853, -147.17241746, -0.00039509, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 14.8, 0.0, 11.375)
    ops.node(124003, 14.8, 0.0, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.0625, 31394325.75117134, 13080969.06298806, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 44.86927087, 0.00074285, 54.14899141, 0.01289553, 5.41489914, 0.06394895, -44.86927087, -0.00074285, -54.14899141, -0.01289553, -5.41489914, -0.06394895, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 44.86927087, 0.00074285, 54.14899141, 0.01289553, 5.41489914, 0.06394895, -44.86927087, -0.00074285, -54.14899141, -0.01289553, -5.41489914, -0.06394895, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 58.22630241, 0.01485691, 58.22630241, 0.04457074, 40.75841169, -1980.55931516, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 14.5565756, 3.419e-05, 43.66972681, 0.00010256, 145.56575603, 0.00034185, -14.5565756, -3.419e-05, -43.66972681, -0.00010256, -145.56575603, -0.00034185, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 58.22630241, 0.01485691, 58.22630241, 0.04457074, 40.75841169, -1980.55931516, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 14.5565756, 3.419e-05, 43.66972681, 0.00010256, 145.56575603, 0.00034185, -14.5565756, -3.419e-05, -43.66972681, -0.00010256, -145.56575603, -0.00034185, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 17.8, 0.0, 9.9)
    ops.node(124032, 17.8, 0.0, 11.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.0625, 30556854.34638626, 12732022.64432761, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 45.90135178, 0.00078069, 55.38237566, 0.01360504, 5.53823757, 0.06046041, -45.90135178, -0.00078069, -55.38237566, -0.01360504, -5.53823757, -0.06046041, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 45.90135178, 0.00078069, 55.38237566, 0.01360504, 5.53823757, 0.06046041, -45.90135178, -0.00078069, -55.38237566, -0.01360504, -5.53823757, -0.06046041, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 69.31715849, 0.01561387, 69.31715849, 0.04684162, 48.52201094, -1968.73985736, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 17.32928962, 4.181e-05, 51.98786887, 0.00012544, 173.29289622, 0.00041812, -17.32928962, -4.181e-05, -51.98786887, -0.00012544, -173.29289622, -0.00041812, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 69.31715849, 0.01561387, 69.31715849, 0.04684162, 48.52201094, -1968.73985736, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 17.32928962, 4.181e-05, 51.98786887, 0.00012544, 173.29289622, 0.00041812, -17.32928962, -4.181e-05, -51.98786887, -0.00012544, -173.29289622, -0.00041812, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 17.8, 0.0, 11.375)
    ops.node(124004, 17.8, 0.0, 12.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.0625, 30862593.77642816, 12859414.07351173, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 43.94419637, 0.00073161, 53.10985237, 0.01301528, 5.31098524, 0.06368648, -43.94419637, -0.00073161, -53.10985237, -0.01301528, -5.31098524, -0.06368648, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 43.94419637, 0.00073161, 53.10985237, 0.01301528, 5.31098524, 0.06368648, -43.94419637, -0.00073161, -53.10985237, -0.01301528, -5.31098524, -0.06368648, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 56.72999754, 0.01463219, 56.72999754, 0.04389658, 39.71099828, -2057.53193467, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 14.18249939, 3.388e-05, 42.54749816, 0.00010164, 141.82499386, 0.00033881, -14.18249939, -3.388e-05, -42.54749816, -0.00010164, -141.82499386, -0.00033881, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 56.72999754, 0.01463219, 56.72999754, 0.04389658, 39.71099828, -2057.53193467, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 14.18249939, 3.388e-05, 42.54749816, 0.00010164, 141.82499386, 0.00033881, -14.18249939, -3.388e-05, -42.54749816, -0.00010164, -141.82499386, -0.00033881, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
