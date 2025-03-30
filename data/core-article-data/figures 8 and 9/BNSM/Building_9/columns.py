import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 6.6, 0.0, 0.0)
    ops.node(121003, 6.6, 0.0, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.105, 29549137.33101903, 12312140.55459126, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 139.88052119, 0.00115966, 165.30984066, 0.0117682, 16.53098407, 0.02982933, -139.88052119, -0.00115966, -165.30984066, -0.0117682, -16.53098407, -0.02982933, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 158.28065411, 0.0010205, 187.05499155, 0.01213238, 18.70549915, 0.03229278, -158.28065411, -0.0010205, -187.05499155, -0.01213238, -18.70549915, -0.03229278, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 147.57691384, 0.02319321, 147.57691384, 0.06957963, 103.30383969, -2083.20062362, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 36.89422846, 9.247e-05, 110.68268538, 0.0002774, 368.94228461, 0.00092466, -36.89422846, -9.247e-05, -110.68268538, -0.0002774, -368.94228461, -0.00092466, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 154.67000983, 0.02041001, 154.67000983, 0.06123003, 108.26900688, -2244.78091377, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 38.66750246, 9.691e-05, 116.00250738, 0.00029073, 386.67502458, 0.0009691, -38.66750246, -9.691e-05, -116.00250738, -0.00029073, -386.67502458, -0.0009691, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 10.3, 0.0, 0.0)
    ops.node(121004, 10.3, 0.0, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.0625, 31441526.12307622, 13100635.88461509, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 69.92904433, 0.00132146, 82.49958526, 0.01367887, 8.24995853, 0.04377306, -69.92904433, -0.00132146, -82.49958526, -0.01367887, -8.24995853, -0.04377306, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 74.06213421, 0.00132146, 87.37564505, 0.01367887, 8.7375645, 0.04377306, -74.06213421, -0.00132146, -87.37564505, -0.01367887, -8.7375645, -0.04377306, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 111.61841782, 0.02642925, 111.61841782, 0.07928776, 78.13289247, -1710.82573443, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 27.90460446, 0.00011042, 83.71381337, 0.00033126, 279.04604455, 0.0011042, -27.90460446, -0.00011042, -83.71381337, -0.00033126, -279.04604455, -0.0011042, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 111.61841782, 0.02642925, 111.61841782, 0.07928776, 78.13289247, -1710.82573443, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 27.90460446, 0.00011042, 83.71381337, 0.00033126, 279.04604455, 0.0011042, -27.90460446, -0.00011042, -83.71381337, -0.00033126, -279.04604455, -0.0011042, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 5.7, 0.0)
    ops.node(121005, 0.0, 5.7, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.075, 31171370.52145547, 12988071.05060645, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 107.58792603, 0.00115012, 126.56545444, 0.01225274, 12.65654544, 0.03917187, -107.58792603, -0.00115012, -126.56545444, -0.01225274, -12.65654544, -0.03917187, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 84.36892947, 0.00136293, 99.25083876, 0.01181718, 9.92508388, 0.03515567, -84.36892947, -0.00136293, -99.25083876, -0.01181718, -9.92508388, -0.03515567, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 134.30657894, 0.02300241, 134.30657894, 0.06900723, 94.01460526, -2084.90867191, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 33.57664474, 0.00011168, 100.72993421, 0.00033504, 335.76644736, 0.0011168, -33.57664474, -0.00011168, -100.72993421, -0.00033504, -335.76644736, -0.0011168, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 125.99031535, 0.02725853, 125.99031535, 0.0817756, 88.19322074, -1887.4170463, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 31.49757884, 0.00010477, 94.49273651, 0.0003143, 314.97578837, 0.00104765, -31.49757884, -0.00010477, -94.49273651, -0.0003143, -314.97578837, -0.00104765, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 2.9, 5.7, 0.0)
    ops.node(121006, 2.9, 5.7, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.15, 31135749.74835729, 12973229.06181554, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 361.90789663, 0.00080576, 428.6390487, 0.01746899, 42.86390487, 0.04593247, -361.90789663, -0.00080576, -428.6390487, -0.01746899, -42.86390487, -0.04593247, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 261.14025955, 0.00117567, 309.29115798, 0.0154661, 30.9291158, 0.03523749, -261.14025955, -0.00117567, -309.29115798, -0.0154661, -30.9291158, -0.03523749, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 270.98384146, 0.01611515, 270.98384146, 0.04834546, 189.68868902, -3513.06603083, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 67.74596036, 0.00011279, 203.23788109, 0.00033838, 677.45960364, 0.00112795, -67.74596036, -0.00011279, -203.23788109, -0.00033838, -677.45960364, -0.00112795, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 207.09542584, 0.02351338, 207.09542584, 0.07054013, 144.96679809, -2675.14720051, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 51.77385646, 8.62e-05, 155.32156938, 0.00025861, 517.73856459, 0.00086202, -51.77385646, -8.62e-05, -155.32156938, -0.00025861, -517.73856459, -0.00086202, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 6.6, 5.7, 0.0)
    ops.node(121007, 6.6, 5.7, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1925, 30914198.70810824, 12880916.12837843, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 443.56005389, 0.00074242, 527.26657446, 0.02104816, 52.72665745, 0.05382118, -443.56005389, -0.00074242, -527.26657446, -0.02104816, -52.72665745, -0.05382118, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 347.83701786, 0.00099791, 413.47914734, 0.01865292, 41.34791473, 0.04217142, -347.83701786, -0.00099791, -413.47914734, -0.01865292, -41.34791473, -0.04217142, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 360.70867384, 0.01484845, 360.70867384, 0.04454534, 252.49607169, -4410.96367242, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 90.17716846, 0.00011783, 270.53150538, 0.0003535, 901.7716846, 0.00117832, -90.17716846, -0.00011783, -270.53150538, -0.0003535, -901.7716846, -0.00117832, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 261.23789853, 0.01995823, 261.23789853, 0.05987468, 182.86652897, -3325.11033142, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 65.30947463, 8.534e-05, 195.9284239, 0.00025601, 653.09474633, 0.00085338, -65.30947463, -8.534e-05, -195.9284239, -0.00025601, -653.09474633, -0.00085338, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 10.3, 5.7, 0.0)
    ops.node(121008, 10.3, 5.7, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.12, 30558146.77667942, 12732561.15694976, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 179.11456597, 0.00087919, 211.93459035, 0.01242335, 21.19345903, 0.03861566, -179.11456597, -0.00087919, -211.93459035, -0.01242335, -21.19345903, -0.03861566, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 144.51926071, 0.00109361, 171.00022072, 0.01165034, 17.10002207, 0.0328368, -144.51926071, -0.00109361, -171.00022072, -0.01165034, -17.10002207, -0.0328368, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 191.91534964, 0.01758378, 191.91534964, 0.05275133, 134.34074475, -2820.26829341, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 47.97883741, 0.00010174, 143.93651223, 0.00030522, 479.7883741, 0.00101741, -47.97883741, -0.00010174, -143.93651223, -0.00030522, -479.7883741, -0.00101741, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 174.64813054, 0.02187223, 174.64813054, 0.0656167, 122.25369138, -2409.05877365, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 43.66203263, 9.259e-05, 130.9860979, 0.00027776, 436.62032634, 0.00092587, -43.66203263, -9.259e-05, -130.9860979, -0.00027776, -436.62032634, -0.00092587, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 11.4, 0.0)
    ops.node(121009, 0.0, 11.4, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.075, 31610591.77548276, 13171079.90645115, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 111.8808844, 0.00116424, 131.34644516, 0.01235838, 13.13464452, 0.03879331, -111.8808844, -0.00116424, -131.34644516, -0.01235838, -13.13464452, -0.03879331, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 87.99301597, 0.00138223, 103.3024534, 0.01192267, 10.33024534, 0.03484137, -87.99301597, -0.00138223, -103.3024534, -0.01192267, -10.33024534, -0.03484137, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 138.18806056, 0.02328473, 138.18806056, 0.06985419, 96.73164239, -2156.9098577, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 34.54701514, 0.00011331, 103.64104542, 0.00033993, 345.4701514, 0.00113311, -34.54701514, -0.00011331, -103.64104542, -0.00033993, -345.4701514, -0.00113311, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 129.79172851, 0.02764461, 129.79172851, 0.08293384, 90.85420996, -1960.52853319, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 32.44793213, 0.00010643, 97.34379638, 0.00031928, 324.47932127, 0.00106426, -32.44793213, -0.00010643, -97.34379638, -0.00031928, -324.47932127, -0.00106426, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 2.9, 11.4, 0.0)
    ops.node(121010, 2.9, 11.4, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.135, 30834168.09717469, 12847570.04048946, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 276.82628695, 0.00083771, 327.38088491, 0.01336683, 32.73808849, 0.03645242, -276.82628695, -0.00083771, -327.38088491, -0.01336683, -32.73808849, -0.03645242, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 209.12002137, 0.00113434, 247.3099589, 0.01227856, 24.73099589, 0.02976375, -209.12002137, -0.00113434, -247.3099589, -0.01227856, -24.73099589, -0.02976375, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 214.49849733, 0.01675416, 214.49849733, 0.05026247, 150.14894813, -2883.30223225, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 53.62462433, 0.00010017, 160.87387299, 0.00030052, 536.24624331, 0.00100174, -53.62462433, -0.00010017, -160.87387299, -0.00030052, -536.24624331, -0.00100174, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 183.55832519, 0.02268672, 183.55832519, 0.06806016, 128.49082763, -2400.54125774, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 45.8895813, 8.572e-05, 137.66874389, 0.00025717, 458.89581298, 0.00085724, -45.8895813, -8.572e-05, -137.66874389, -0.00025717, -458.89581298, -0.00085724, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 6.6, 11.4, 0.0)
    ops.node(121011, 6.6, 11.4, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.1925, 30744531.39287541, 12810221.41369809, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 447.5378056, 0.00075608, 532.11697555, 0.02273693, 53.21169756, 0.05521478, -447.5378056, -0.00075608, -532.11697555, -0.02273693, -53.21169756, -0.05521478, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 323.75662754, 0.00102283, 384.94266921, 0.02013427, 38.49426692, 0.04344096, -323.75662754, -0.00102283, -384.94266921, -0.02013427, -38.49426692, -0.04344096, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 359.29800675, 0.01512157, 359.29800675, 0.04536471, 251.50860473, -4416.62453468, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 89.82450169, 0.00011802, 269.47350506, 0.00035406, 898.24501688, 0.00118019, -89.82450169, -0.00011802, -269.47350506, -0.00035406, -898.24501688, -0.00118019, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 260.10541972, 0.02045651, 260.10541972, 0.06136954, 182.0737938, -3324.71607325, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 65.02635493, 8.544e-05, 195.07906479, 0.00025631, 650.26354929, 0.00085437, -65.02635493, -8.544e-05, -195.07906479, -0.00025631, -650.26354929, -0.00085437, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 10.3, 11.4, 0.0)
    ops.node(121012, 10.3, 11.4, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.0875, 31615232.57031474, 13173013.57096447, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 149.81939216, 0.00101018, 175.68661619, 0.01214901, 17.56866162, 0.03771829, -149.81939216, -0.00101018, -175.68661619, -0.01214901, -17.56866162, -0.03771829, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 114.67860661, 0.00135322, 134.47856152, 0.01134203, 13.44785615, 0.03108705, -114.67860661, -0.00135322, -134.47856152, -0.01134203, -13.44785615, -0.03108705, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 163.26575231, 0.02020365, 163.26575231, 0.06061095, 114.28602662, -2571.98218125, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 40.81643808, 0.00011473, 122.44931423, 0.0003442, 408.16438077, 0.00114733, -40.81643808, -0.00011473, -122.44931423, -0.0003442, -408.16438077, -0.00114733, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 146.29214511, 0.02706438, 146.29214511, 0.08119313, 102.40450158, -2184.157173, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 36.57303628, 0.0001028, 109.71910883, 0.00030841, 365.73036277, 0.00102805, -36.57303628, -0.0001028, -109.71910883, -0.00030841, -365.73036277, -0.00102805, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 17.1, 0.0)
    ops.node(121013, 0.0, 17.1, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.075, 31392802.67323792, 13080334.44718247, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 112.22028645, 0.0011228, 131.74108073, 0.01225585, 13.17410807, 0.03810774, -112.22028645, -0.0011228, -131.74108073, -0.01225585, -13.17410807, -0.03810774, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 87.95153367, 0.0013221, 103.25076209, 0.01180501, 10.32507621, 0.03421822, -87.95153367, -0.0013221, -103.25076209, -0.01180501, -10.32507621, -0.03421822, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 138.35361005, 0.02245594, 138.35361005, 0.06736783, 96.84752704, -2176.02422933, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 34.58840251, 0.00011423, 103.76520754, 0.0003427, 345.88402513, 0.00114234, -34.58840251, -0.00011423, -103.76520754, -0.0003427, -345.88402513, -0.00114234, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 129.82895285, 0.02644193, 129.82895285, 0.07932578, 90.88026699, -1975.87746537, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 32.45723821, 0.0001072, 97.37171464, 0.00032159, 324.57238212, 0.00107195, -32.45723821, -0.0001072, -97.37171464, -0.00032159, -324.57238212, -0.00107195, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 2.9, 17.1, 0.0)
    ops.node(121014, 2.9, 17.1, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.135, 30302653.07040482, 12626105.44600201, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 278.71403677, 0.00087563, 329.62588814, 0.01300898, 32.96258881, 0.03502043, -278.71403677, -0.00087563, -329.62588814, -0.01300898, -32.96258881, -0.03502043, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 208.39038892, 0.00120659, 246.45643192, 0.01199879, 24.64564319, 0.02867042, -208.39038892, -0.00120659, -246.45643192, -0.01199879, -24.64564319, -0.02867042, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 211.4311085, 0.01751265, 211.4311085, 0.05253796, 148.00177595, -2876.14824844, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 52.85777713, 0.00010047, 158.57333138, 0.00030142, 528.57777125, 0.00100473, -52.85777713, -0.00010047, -158.57333138, -0.00030142, -528.57777125, -0.00100473, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 180.78024203, 0.02413187, 180.78024203, 0.07239562, 126.54616942, -2396.78704756, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 45.19506051, 8.591e-05, 135.58518152, 0.00025772, 451.95060508, 0.00085908, -45.19506051, -8.591e-05, -135.58518152, -0.00025772, -451.95060508, -0.00085908, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 6.6, 17.1, 0.0)
    ops.node(121015, 6.6, 17.1, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.1925, 31356027.21230935, 13065011.33846223, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 448.21084111, 0.00074244, 532.58713279, 0.0212087, 53.25871328, 0.05500303, -448.21084111, -0.00074244, -532.58713279, -0.0212087, -53.25871328, -0.05500303, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 353.60110144, 0.0009936, 420.1669828, 0.01878818, 42.01669828, 0.0430396, -353.60110144, -0.0009936, -420.1669828, -0.01878818, -42.01669828, -0.0430396, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 364.21674901, 0.01484883, 364.21674901, 0.04454648, 254.95172431, -4404.46326916, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 91.05418725, 0.0001173, 273.16256176, 0.00035191, 910.54187253, 0.00117302, -91.05418725, -0.0001173, -273.16256176, -0.00035191, -910.54187253, -0.00117302, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 263.94225611, 0.01987201, 263.94225611, 0.05961602, 184.75957927, -3318.80699064, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 65.98556403, 8.501e-05, 197.95669208, 0.00025502, 659.85564027, 0.00085007, -65.98556403, -8.501e-05, -197.95669208, -0.00025502, -659.85564027, -0.00085007, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 10.3, 17.1, 0.0)
    ops.node(121016, 10.3, 17.1, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.12, 30490892.56382168, 12704538.56825903, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 178.53484351, 0.00088471, 211.26386482, 0.01220372, 21.12638648, 0.03829139, -178.53484351, -0.00088471, -211.26386482, -0.01220372, -21.12638648, -0.03829139, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 143.74353597, 0.00110402, 170.0946121, 0.01145485, 17.00946121, 0.03255668, -143.74353597, -0.00110402, -170.0946121, -0.01145485, -17.00946121, -0.03255668, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 190.19306416, 0.01769428, 190.19306416, 0.05308284, 133.13514491, -2784.81959235, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 47.54826604, 0.00010105, 142.64479812, 0.00030315, 475.48266041, 0.00101051, -47.54826604, -0.00010105, -142.64479812, -0.00030315, -475.48266041, -0.00101051, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 173.25857402, 0.02208035, 173.25857402, 0.06624105, 121.28100181, -2383.4220734, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 43.3146435, 9.205e-05, 129.94393051, 0.00027616, 433.14643505, 0.00092053, -43.3146435, -9.205e-05, -129.94393051, -0.00027616, -433.14643505, -0.00092053, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 22.8, 0.0)
    ops.node(121017, 0.0, 22.8, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.0625, 32075593.81419361, 13364830.755914, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 67.10720455, 0.00128896, 79.48151199, 0.01435754, 7.9481512, 0.05040448, -67.10720455, -0.00128896, -79.48151199, -0.01435754, -7.9481512, -0.05040448, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 63.20493657, 0.00128896, 74.85968098, 0.01435754, 7.4859681, 0.05040448, -63.20493657, -0.00128896, -74.85968098, -0.01435754, -7.4859681, -0.05040448, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 107.4409493, 0.02577914, 107.4409493, 0.07733742, 75.20866451, -1579.91606645, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 26.86023732, 0.00010419, 80.58071197, 0.00031256, 268.60237324, 0.00104186, -26.86023732, -0.00010419, -80.58071197, -0.00031256, -268.60237324, -0.00104186, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 107.4409493, 0.02577914, 107.4409493, 0.07733742, 75.20866451, -1579.91606645, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 26.86023732, 0.00010419, 80.58071197, 0.00031256, 268.60237324, 0.00104186, -26.86023732, -0.00010419, -80.58071197, -0.00031256, -268.60237324, -0.00104186, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 2.9, 22.8, 0.0)
    ops.node(121018, 2.9, 22.8, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.09, 32329959.53314506, 13470816.47214377, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 130.60257916, 0.00113381, 154.08755207, 0.01301565, 15.40875521, 0.03796033, -130.60257916, -0.00113381, -154.08755207, -0.01301565, -15.40875521, -0.03796033, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 125.16712094, 0.00113381, 147.67468904, 0.01301565, 14.7674689, 0.03796033, -125.16712094, -0.00113381, -147.67468904, -0.01301565, -14.7674689, -0.03796033, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 142.26930225, 0.02267618, 142.26930225, 0.06802854, 99.58851158, -1943.75199384, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 35.56732556, 9.505e-05, 106.70197669, 0.00028516, 355.67325563, 0.00095052, -35.56732556, -9.505e-05, -106.70197669, -0.00028516, -355.67325563, -0.00095052, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 142.26930225, 0.02267618, 142.26930225, 0.06802854, 99.58851158, -1943.75199384, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 35.56732556, 9.505e-05, 106.70197669, 0.00028516, 355.67325563, 0.00095052, -35.56732556, -9.505e-05, -106.70197669, -0.00028516, -355.67325563, -0.00095052, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 6.6, 22.8, 0.0)
    ops.node(121019, 6.6, 22.8, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.1225, 31310448.18327602, 13046020.07636501, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 195.62014304, 0.00095839, 232.00711584, 0.01328599, 23.20071158, 0.04014185, -195.62014304, -0.00095839, -232.00711584, -0.01328599, -23.20071158, -0.04014185, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 175.43937633, 0.00095839, 208.07255876, 0.01328599, 20.80725588, 0.04014185, -175.43937633, -0.00095839, -208.07255876, -0.01328599, -20.80725588, -0.04014185, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 184.71553518, 0.0191679, 184.71553518, 0.05750369, 129.30087462, -2521.35961316, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 46.17888379, 9.362e-05, 138.53665138, 0.00028086, 461.78883794, 0.00093621, -46.17888379, -9.362e-05, -138.53665138, -0.00028086, -461.78883794, -0.00093621, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 184.71553518, 0.0191679, 184.71553518, 0.05750369, 129.30087462, -2521.35961316, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 46.17888379, 9.362e-05, 138.53665138, 0.00028086, 461.78883794, 0.00093621, -46.17888379, -9.362e-05, -138.53665138, -0.00028086, -461.78883794, -0.00093621, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 10.3, 22.8, 0.0)
    ops.node(121020, 10.3, 22.8, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.0625, 32299093.1946432, 13457955.497768, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 79.24962214, 0.00133155, 93.43313232, 0.01429238, 9.34331323, 0.04646587, -79.24962214, -0.00133155, -93.43313232, -0.01429238, -9.34331323, -0.04646587, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 79.24962214, 0.00133155, 93.43313232, 0.01429238, 9.34331323, 0.04646587, -79.24962214, -0.00133155, -93.43313232, -0.01429238, -9.34331323, -0.04646587, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 112.96071002, 0.02663109, 112.96071002, 0.07989328, 79.07249701, -1694.36565089, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 28.2401775, 0.00010878, 84.72053251, 0.00032634, 282.40177505, 0.00108781, -28.2401775, -0.00010878, -84.72053251, -0.00032634, -282.40177505, -0.00108781, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 112.96071002, 0.02663109, 112.96071002, 0.07989328, 79.07249701, -1694.36565089, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 28.2401775, 0.00010878, 84.72053251, 0.00032634, 282.40177505, 0.00108781, -28.2401775, -0.00010878, -84.72053251, -0.00032634, -282.40177505, -0.00108781, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 6.6, 0.0, 2.975)
    ops.node(122003, 6.6, 0.0, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.105, 30028935.70045829, 12512056.54185762, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 108.45900013, 0.00110353, 129.16219706, 0.0130355, 12.91621971, 0.03669275, -108.45900013, -0.00110353, -129.16219706, -0.0130355, -12.91621971, -0.03669275, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 128.04994892, 0.00097253, 152.49276423, 0.01347063, 15.24927642, 0.03987761, -128.04994892, -0.00097253, -152.49276423, -0.01347063, -15.24927642, -0.03987761, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 138.33732884, 0.02207058, 138.33732884, 0.06621174, 96.83613019, -1788.95103765, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 34.58433221, 8.529e-05, 103.75299663, 0.00025587, 345.84332209, 0.00085292, -34.58433221, -8.529e-05, -103.75299663, -0.00025587, -345.84332209, -0.00085292, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 145.31883253, 0.01945067, 145.31883253, 0.058352, 101.72318277, -1960.32441629, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 36.32970813, 8.96e-05, 108.9891244, 0.00026879, 363.29708132, 0.00089596, -36.32970813, -8.96e-05, -108.9891244, -0.00026879, -363.29708132, -0.00089596, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 10.3, 0.0, 2.95)
    ops.node(122004, 10.3, 0.0, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.0625, 31336381.13659529, 13056825.47358137, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 59.77125116, 0.00127235, 71.02576939, 0.01501581, 7.10257694, 0.05193996, -59.77125116, -0.00127235, -71.02576939, -0.01501581, -7.10257694, -0.05193996, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 63.77515629, 0.00127235, 75.7835825, 0.01501581, 7.57835825, 0.05193996, -63.77515629, -0.00127235, -75.7835825, -0.01501581, -7.57835825, -0.05193996, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 104.38295317, 0.02544697, 104.38295317, 0.0763409, 73.06806722, -1562.83480946, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 26.09573829, 0.00010361, 78.28721488, 0.00031083, 260.95738294, 0.00103609, -26.09573829, -0.00010361, -78.28721488, -0.00031083, -260.95738294, -0.00103609, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 104.38295317, 0.02544697, 104.38295317, 0.0763409, 73.06806722, -1562.83480946, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 26.09573829, 0.00010361, 78.28721488, 0.00031083, 260.95738294, 0.00103609, -26.09573829, -0.00010361, -78.28721488, -0.00031083, -260.95738294, -0.00103609, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 5.7, 2.95)
    ops.node(122005, 0.0, 5.7, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.075, 29935044.88287506, 12472935.36786461, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 90.72338168, 0.00109046, 107.64130437, 0.01388604, 10.76413044, 0.04488664, -90.72338168, -0.00109046, -107.64130437, -0.01388604, -10.76413044, -0.04488664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 70.31787975, 0.00128455, 83.43062347, 0.0133329, 8.34306235, 0.04020997, -70.31787975, -0.00128455, -83.43062347, -0.0133329, -8.34306235, -0.04020997, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 125.4016401, 0.0218093, 125.4016401, 0.06542789, 87.78114807, -1956.71642187, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 31.35041002, 0.00010858, 94.05123007, 0.00032575, 313.50410024, 0.00108582, -31.35041002, -0.00010858, -94.05123007, -0.00032575, -313.50410024, -0.00108582, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 116.57491865, 0.02569108, 116.57491865, 0.07707325, 81.60244305, -1722.01626912, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 29.14372966, 0.00010094, 87.43118899, 0.00030282, 291.43729662, 0.00100939, -29.14372966, -0.00010094, -87.43118899, -0.00030282, -291.43729662, -0.00100939, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 2.9, 5.7, 2.975)
    ops.node(122006, 2.9, 5.7, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.15, 31154246.17458325, 12980935.90607635, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 244.59616344, 0.00076005, 291.38599082, 0.01426476, 29.13859908, 0.04385178, -244.59616344, -0.00076005, -291.38599082, -0.01426476, -29.13859908, -0.04385178, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 151.20928401, 0.00110163, 180.13474301, 0.01278416, 18.0134743, 0.03376306, -151.20928401, -0.00110163, -180.13474301, -0.01278416, -18.0134743, -0.03376306, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 237.55062197, 0.01520109, 237.55062197, 0.04560328, 166.28543538, -2766.07812592, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 59.38765549, 9.882e-05, 178.16296648, 0.00029646, 593.87655493, 0.0009882, -59.38765549, -9.882e-05, -178.16296648, -0.00029646, -593.87655493, -0.0009882, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 183.08999411, 0.02203255, 183.08999411, 0.06609764, 128.16299587, -2079.69857081, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 45.77249853, 7.616e-05, 137.31749558, 0.00022849, 457.72498526, 0.00076164, -45.77249853, -7.616e-05, -137.31749558, -0.00022849, -457.72498526, -0.00076164, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 6.6, 5.7, 2.975)
    ops.node(122007, 6.6, 5.7, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1925, 30124476.33149886, 12551865.13812453, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 356.43202429, 0.0007201, 426.25228263, 0.01402723, 42.62522826, 0.04105987, -356.43202429, -0.0007201, -426.25228263, -0.01402723, -42.62522826, -0.04105987, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 197.16996884, 0.00095974, 235.7929242, 0.01272959, 23.57929242, 0.03293295, -197.16996884, -0.00095974, -235.7929242, -0.01272959, -23.57929242, -0.03293295, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 294.16374936, 0.01440206, 294.16374936, 0.04320619, 205.91462455, -3052.2302789, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 73.54093734, 9.861e-05, 220.62281202, 0.00029584, 735.4093734, 0.00098613, -73.54093734, -9.861e-05, -220.62281202, -0.00029584, -735.4093734, -0.00098613, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 215.38554361, 0.01919482, 215.38554361, 0.05758445, 150.76988053, -2360.34561247, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 53.8463859, 7.22e-05, 161.53915771, 0.00021661, 538.46385903, 0.00072204, -53.8463859, -7.22e-05, -161.53915771, -0.00021661, -538.46385903, -0.00072204, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 10.3, 5.7, 2.95)
    ops.node(122008, 10.3, 5.7, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.12, 30270924.68025571, 12612885.28343988, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 164.23397442, 0.00085101, 195.71938014, 0.01339689, 19.57193801, 0.04496625, -164.23397442, -0.00085101, -195.71938014, -0.01339689, -19.57193801, -0.04496625, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 110.59126327, 0.00106053, 131.79278875, 0.0125333, 13.17927887, 0.03806916, -110.59126327, -0.00106053, -131.79278875, -0.0125333, -13.17927887, -0.03806916, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 176.30184168, 0.01702016, 176.30184168, 0.05106047, 123.41128918, -2488.07222977, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 44.07546042, 9.435e-05, 132.22638126, 0.00028305, 440.7546042, 0.00094351, -44.07546042, -9.435e-05, -132.22638126, -0.00028305, -440.7546042, -0.00094351, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 159.66499544, 0.02121063, 159.66499544, 0.06363188, 111.76549681, -2059.19948793, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 39.91624886, 8.545e-05, 119.74874658, 0.00025634, 399.16248859, 0.00085447, -39.91624886, -8.545e-05, -119.74874658, -0.00025634, -399.16248859, -0.00085447, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 11.4, 2.95)
    ops.node(122009, 0.0, 11.4, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.075, 31555036.01345144, 13147931.67227143, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 93.46564195, 0.00108146, 110.63230366, 0.0140905, 11.06323037, 0.0476746, -93.46564195, -0.00108146, -110.63230366, -0.0140905, -11.06323037, -0.0476746, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 72.80094799, 0.00127618, 86.17216356, 0.01352553, 8.61721636, 0.04264245, -72.80094799, -0.00127618, -86.17216356, -0.01352553, -8.61721636, -0.04264245, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 130.41386675, 0.02162916, 130.41386675, 0.06488747, 91.28970673, -1964.55879135, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 32.60346669, 0.00010712, 97.81040006, 0.00032137, 326.03466688, 0.00107125, -32.60346669, -0.00010712, -97.81040006, -0.00032137, -326.03466688, -0.00107125, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 121.75961779, 0.02552353, 121.75961779, 0.07657058, 85.23173245, -1741.07742933, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 30.43990445, 0.00010002, 91.31971334, 0.00030005, 304.39904447, 0.00100016, -30.43990445, -0.00010002, -91.31971334, -0.00030005, -304.39904447, -0.00100016, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 2.9, 11.4, 2.975)
    ops.node(122010, 2.9, 11.4, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.135, 30625221.39506496, 12760508.9146104, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 207.62126817, 0.00081438, 247.14128521, 0.01369218, 24.71412852, 0.04118346, -207.62126817, -0.00081438, -247.14128521, -0.01369218, -24.71412852, -0.04118346, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 140.56239574, 0.00109877, 167.31797971, 0.01255312, 16.73179797, 0.03337522, -140.56239574, -0.00109877, -167.31797971, -0.01255312, -16.73179797, -0.03337522, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 199.4886157, 0.01628768, 199.4886157, 0.04886303, 139.64203099, -2556.64980532, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 49.87215392, 9.38e-05, 149.61646177, 0.0002814, 498.72153925, 0.000938, -49.87215392, -9.38e-05, -149.61646177, -0.0002814, -498.72153925, -0.000938, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 169.63117229, 0.02197536, 169.63117229, 0.06592607, 118.74182061, -2044.49472735, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 42.40779307, 7.976e-05, 127.22337922, 0.00023928, 424.07793073, 0.00079761, -42.40779307, -7.976e-05, -127.22337922, -0.00023928, -424.07793073, -0.00079761, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 6.6, 11.4, 2.975)
    ops.node(122011, 6.6, 11.4, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.1925, 30177516.60486295, 12573965.25202623, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 358.08096163, 0.00073282, 428.22969648, 0.01223969, 42.82296965, 0.03468702, -358.08096163, -0.00073282, -428.22969648, -0.01223969, -42.82296965, -0.03468702, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 209.19395679, 0.00098395, 250.17544697, 0.01129849, 25.0175447, 0.02861549, -209.19395679, -0.00098395, -250.17544697, -0.01129849, -25.0175447, -0.02861549, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 275.69081388, 0.01465648, 275.69081388, 0.04396943, 192.98356972, -2585.25153053, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 68.92270347, 9.226e-05, 206.76811041, 0.00027677, 689.2270347, 0.00092258, -68.92270347, -9.226e-05, -206.76811041, -0.00027677, -689.2270347, -0.00092258, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 203.65255974, 0.01967901, 203.65255974, 0.05903704, 142.55679182, -2093.55309713, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 50.91313993, 6.815e-05, 152.7394198, 0.00020445, 509.13139935, 0.00068151, -50.91313993, -6.815e-05, -152.7394198, -0.00020445, -509.13139935, -0.00068151, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 10.3, 11.4, 2.95)
    ops.node(122012, 10.3, 11.4, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.0875, 30607664.87715465, 12753193.69881444, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 117.4842325, 0.00097714, 138.99189409, 0.01321371, 13.89918941, 0.04343533, -117.4842325, -0.00097714, -138.99189409, -0.01321371, -13.89918941, -0.04343533, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 86.53227119, 0.00131443, 102.37360381, 0.01228765, 10.23736038, 0.03562529, -86.53227119, -0.00131443, -102.37360381, -0.01228765, -10.23736038, -0.03562529, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 149.64703401, 0.01954281, 149.64703401, 0.05862843, 104.75292381, -2299.19454026, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 37.4117585, 0.00010862, 112.23527551, 0.00032587, 374.11758503, 0.00108624, -37.4117585, -0.00010862, -112.23527551, -0.00032587, -374.11758503, -0.00108624, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 132.57353774, 0.02628859, 132.57353774, 0.07886576, 92.80147642, -1875.04840168, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 33.14338443, 9.623e-05, 99.4301533, 0.00028869, 331.43384435, 0.00096231, -33.14338443, -9.623e-05, -99.4301533, -0.00028869, -331.43384435, -0.00096231, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 17.1, 2.95)
    ops.node(122013, 0.0, 17.1, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.075, 30963576.5221842, 12901490.21757675, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 93.32381006, 0.00111665, 110.50991948, 0.01391435, 11.05099195, 0.04602358, -93.32381006, -0.00111665, -110.50991948, -0.01391435, -11.05099195, -0.04602358, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 72.80425011, 0.00132475, 86.21156607, 0.0133751, 8.62115661, 0.04121333, -72.80425011, -0.00132475, -86.21156607, -0.0133751, -8.62115661, -0.04121333, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 129.54418416, 0.02233303, 129.54418416, 0.06699908, 90.68092891, -1983.85230372, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 32.38604604, 0.00010844, 97.15813812, 0.00032533, 323.8604604, 0.00108443, -32.38604604, -0.00010844, -97.15813812, -0.00032533, -323.8604604, -0.00108443, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 120.76935613, 0.02649505, 120.76935613, 0.07948516, 84.53854929, -1756.20902587, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 30.19233903, 0.0001011, 90.5770171, 0.00030329, 301.92339033, 0.00101098, -30.19233903, -0.0001011, -90.5770171, -0.00030329, -301.92339033, -0.00101098, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 2.9, 17.1, 2.975)
    ops.node(122014, 2.9, 17.1, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.135, 31248152.84991597, 13020063.68746499, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 207.65153181, 0.00083005, 247.01872774, 0.01355944, 24.70187277, 0.04216283, -207.65153181, -0.00083005, -247.01872774, -0.01355944, -24.70187277, -0.04216283, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 139.90330914, 0.00113444, 166.42659521, 0.01245679, 16.64265952, 0.03412121, -139.90330914, -0.00113444, -166.42659521, -0.01245679, -16.64265952, -0.03412121, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 202.01847535, 0.01660091, 202.01847535, 0.04980272, 141.41293275, -2542.56503638, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 50.50461884, 9.31e-05, 151.51385652, 0.00027929, 505.04618839, 0.00093096, -50.50461884, -9.31e-05, -151.51385652, -0.00027929, -505.04618839, -0.00093096, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 172.15410383, 0.02268873, 172.15410383, 0.06806618, 120.50787268, -2036.09493675, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 43.03852596, 7.933e-05, 129.11557787, 0.000238, 430.38525958, 0.00079333, -43.03852596, -7.933e-05, -129.11557787, -0.000238, -430.38525958, -0.00079333, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 6.6, 17.1, 2.975)
    ops.node(122015, 6.6, 17.1, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.1925, 30548724.20806331, 12728635.08669305, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 353.86149253, 0.00070581, 422.99822781, 0.01438604, 42.29982278, 0.04211869, -353.86149253, -0.00070581, -422.99822781, -0.01438604, -42.29982278, -0.04211869, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 195.81252508, 0.00093428, 234.06997607, 0.01303412, 23.40699761, 0.03376066, -195.81252508, -0.00093428, -234.06997607, -0.01303412, -23.40699761, -0.03376066, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 299.47572011, 0.01411623, 299.47572011, 0.04234868, 209.63300408, -3101.60188835, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 74.86893003, 9.9e-05, 224.60679008, 0.000297, 748.68930028, 0.00099, -74.86893003, -9.9e-05, -224.60679008, -0.000297, -748.68930028, -0.00099, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 219.19077105, 0.01868566, 219.19077105, 0.05605699, 153.43353973, -2385.30638391, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 54.79769276, 7.246e-05, 164.39307829, 0.00021738, 547.97692762, 0.00072459, -54.79769276, -7.246e-05, -164.39307829, -0.00021738, -547.97692762, -0.00072459, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 10.3, 17.1, 2.95)
    ops.node(122016, 10.3, 17.1, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.12, 31663722.74928774, 13193217.81220322, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 166.05279792, 0.00084028, 197.58614876, 0.01375548, 19.75861488, 0.04817493, -166.05279792, -0.00084028, -197.58614876, -0.01375548, -19.75861488, -0.04817493, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 111.67532909, 0.0010421, 132.88242331, 0.0128526, 13.28824233, 0.04069383, -111.67532909, -0.0010421, -132.88242331, -0.0128526, -13.28824233, -0.04069383, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 181.98383124, 0.01680558, 181.98383124, 0.05041673, 127.38868187, -2488.03462421, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 45.49595781, 9.311e-05, 136.48787343, 0.00027932, 454.95957811, 0.00093108, -45.49595781, -9.311e-05, -136.48787343, -0.00027932, -454.95957811, -0.00093108, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 165.32733046, 0.02084193, 165.32733046, 0.06252579, 115.72913132, -2058.04049047, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 41.33183261, 8.459e-05, 123.99549784, 0.00025376, 413.31832614, 0.00084586, -41.33183261, -8.459e-05, -123.99549784, -0.00025376, -413.31832614, -0.00084586, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 22.8, 2.95)
    ops.node(122017, 0.0, 22.8, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.0625, 31284154.91546357, 13035064.54810982, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 48.86562581, 0.00119705, 58.27629604, 0.01481634, 5.8276296, 0.05571949, -48.86562581, -0.00119705, -58.27629604, -0.01481634, -5.8276296, -0.05571949, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 48.86562581, 0.00119705, 58.27629604, 0.01481634, 5.8276296, 0.05571949, -48.86562581, -0.00119705, -58.27629604, -0.01481634, -5.8276296, -0.05571949, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 99.58974723, 0.0239411, 99.58974723, 0.07182329, 69.71282306, -1481.18678174, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 24.89743681, 9.902e-05, 74.69231042, 0.00029705, 248.97436806, 0.00099016, -24.89743681, -9.902e-05, -74.69231042, -0.00029705, -248.97436806, -0.00099016, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 99.58974723, 0.0239411, 99.58974723, 0.07182329, 69.71282306, -1481.18678174, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 24.89743681, 9.902e-05, 74.69231042, 0.00029705, 248.97436806, 0.00099016, -24.89743681, -9.902e-05, -74.69231042, -0.00029705, -248.97436806, -0.00099016, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 2.9, 22.8, 2.975)
    ops.node(122018, 2.9, 22.8, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.09, 31336359.05442608, 13056816.27267753, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 98.96205273, 0.00112834, 117.63305071, 0.01413348, 11.76330507, 0.04232845, -98.96205273, -0.00112834, -117.63305071, -0.01413348, -11.76330507, -0.04232845, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 98.96205273, 0.00112834, 117.63305071, 0.01413348, 11.76330507, 0.04232845, -98.96205273, -0.00112834, -117.63305071, -0.01413348, -11.76330507, -0.04232845, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 131.54169257, 0.02256688, 131.54169257, 0.06770064, 92.0791848, -1751.53505798, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 32.88542314, 9.067e-05, 98.65626943, 0.00027201, 328.85423143, 0.00090671, -32.88542314, -9.067e-05, -98.65626943, -0.00027201, -328.85423143, -0.00090671, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 131.54169257, 0.02256688, 131.54169257, 0.06770064, 92.0791848, -1751.53505798, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 32.88542314, 9.067e-05, 98.65626943, 0.00027201, 328.85423143, 0.00090671, -32.88542314, -9.067e-05, -98.65626943, -0.00027201, -328.85423143, -0.00090671, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 6.6, 22.8, 2.975)
    ops.node(122019, 6.6, 22.8, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.1225, 31055081.00501032, 12939617.08542097, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 124.70339966, 0.0009237, 148.78717679, 0.01329895, 14.87871768, 0.04462215, -124.70339966, -0.0009237, -148.78717679, -0.01329895, -14.87871768, -0.04462215, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 137.27997593, 0.0009237, 163.79264803, 0.01329895, 16.3792648, 0.04462215, -137.27997593, -0.0009237, -163.79264803, -0.01329895, -16.3792648, -0.04462215, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 169.71052873, 0.01847394, 169.71052873, 0.05542182, 118.79737011, -2207.59077477, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 42.42763218, 8.672e-05, 127.28289655, 0.00026017, 424.27632182, 0.00086723, -42.42763218, -8.672e-05, -127.28289655, -0.00026017, -424.27632182, -0.00086723, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 169.71052873, 0.01847394, 169.71052873, 0.05542182, 118.79737011, -2207.59077477, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 42.42763218, 8.672e-05, 127.28289655, 0.00026017, 424.27632182, 0.00086723, -42.42763218, -8.672e-05, -127.28289655, -0.00026017, -424.27632182, -0.00086723, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 10.3, 22.8, 2.95)
    ops.node(122020, 10.3, 22.8, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.0625, 32103288.56730719, 13376370.236378, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 59.21563958, 0.00126471, 70.29107841, 0.01498075, 7.02910784, 0.05361071, -59.21563958, -0.00126471, -70.29107841, -0.01498075, -7.02910784, -0.05361071, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 62.96364562, 0.00126471, 74.7400954, 0.01498075, 7.47400954, 0.05361071, -62.96364562, -0.00126471, -74.7400954, -0.01498075, -7.47400954, -0.05361071, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 104.78537748, 0.02529413, 104.78537748, 0.07588238, 73.34976424, -1526.50758592, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 26.19634437, 0.00010152, 78.58903311, 0.00030457, 261.96344371, 0.00101524, -26.19634437, -0.00010152, -78.58903311, -0.00030457, -261.96344371, -0.00101524, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 104.78537748, 0.02529413, 104.78537748, 0.07588238, 73.34976424, -1526.50758592, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 26.19634437, 0.00010152, 78.58903311, 0.00030457, 261.96344371, 0.00101524, -26.19634437, -0.00010152, -78.58903311, -0.00030457, -261.96344371, -0.00101524, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 6.6, 0.0, 5.675)
    ops.node(123003, 6.6, 0.0, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0625, 31514330.31366819, 13130970.96402841, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 69.16775502, 0.00131919, 82.08567493, 0.01462841, 8.20856749, 0.04597545, -69.16775502, -0.00131919, -82.08567493, -0.01462841, -8.20856749, -0.04597545, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 69.16775502, 0.00131919, 82.08567493, 0.01462841, 8.20856749, 0.04597545, -69.16775502, -0.00131919, -82.08567493, -0.01462841, -8.20856749, -0.04597545, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 92.39450677, 0.02638386, 92.39450677, 0.07915159, 64.67615474, -1349.99486737, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 23.09862669, 9.119e-05, 69.29588008, 0.00027357, 230.98626692, 0.00091191, -23.09862669, -9.119e-05, -69.29588008, -0.00027357, -230.98626692, -0.00091191, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 92.39450677, 0.02638386, 92.39450677, 0.07915159, 64.67615474, -1349.99486737, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 23.09862669, 9.119e-05, 69.29588008, 0.00027357, 230.98626692, 0.00091191, -23.09862669, -9.119e-05, -69.29588008, -0.00027357, -230.98626692, -0.00091191, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 10.3, 0.0, 5.65)
    ops.node(123004, 10.3, 0.0, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 30411888.6663686, 12671620.27765358, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 42.74889136, 0.00117463, 51.24187584, 0.0159314, 5.12418758, 0.05980186, -42.74889136, -0.00117463, -51.24187584, -0.0159314, -5.12418758, -0.05980186, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 42.74889136, 0.00117463, 51.24187584, 0.0159314, 5.12418758, 0.05980186, -42.74889136, -0.00117463, -51.24187584, -0.0159314, -5.12418758, -0.05980186, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 94.2247851, 0.02349268, 94.2247851, 0.07047805, 65.95734957, -1469.26702366, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 23.55619627, 9.637e-05, 70.66858882, 0.00028911, 235.56196274, 0.00096369, -23.55619627, -9.637e-05, -70.66858882, -0.00028911, -235.56196274, -0.00096369, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 94.2247851, 0.02349268, 94.2247851, 0.07047805, 65.95734957, -1469.26702366, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 23.55619627, 9.637e-05, 70.66858882, 0.00028911, 235.56196274, 0.00096369, -23.55619627, -9.637e-05, -70.66858882, -0.00028911, -235.56196274, -0.00096369, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 5.7, 5.65)
    ops.node(123005, 0.0, 5.7, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 31822774.57256261, 13259489.40523442, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 49.56240329, 0.00120108, 59.01394059, 0.01525193, 5.90139406, 0.05640639, -49.56240329, -0.00120108, -59.01394059, -0.01525193, -5.90139406, -0.05640639, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 49.56240329, 0.00120108, 59.01394059, 0.01525193, 5.90139406, 0.05640639, -49.56240329, -0.00120108, -59.01394059, -0.01525193, -5.90139406, -0.05640639, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 102.41848645, 0.02402151, 102.41848645, 0.07206454, 71.69294051, -1517.15772943, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 25.60462161, 0.00010011, 76.81386483, 0.00030032, 256.04621612, 0.00100105, -25.60462161, -0.00010011, -76.81386483, -0.00030032, -256.04621612, -0.00100105, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 102.41848645, 0.02402151, 102.41848645, 0.07206454, 71.69294051, -1517.15772943, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 25.60462161, 0.00010011, 76.81386483, 0.00030032, 256.04621612, 0.00100105, -25.60462161, -0.00010011, -76.81386483, -0.00030032, -256.04621612, -0.00100105, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 2.9, 5.7, 5.675)
    ops.node(123006, 2.9, 5.7, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1, 33068103.77205007, 13778376.57168753, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 140.19934717, 0.00084354, 166.42063308, 0.01492144, 16.64206331, 0.05203204, -140.19934717, -0.00084354, -166.42063308, -0.01492144, -16.64206331, -0.05203204, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 84.41047425, 0.00123618, 100.19764605, 0.0134477, 10.0197646, 0.03993137, -84.41047425, -0.00123618, -100.19764605, -0.0134477, -10.0197646, -0.03993137, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 155.75400508, 0.01687072, 155.75400508, 0.05061215, 109.02780356, -2054.93462684, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 38.93850127, 9.156e-05, 116.81550381, 0.00027469, 389.3850127, 0.00091564, -38.93850127, -9.156e-05, -116.81550381, -0.00027469, -389.3850127, -0.00091564, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 129.96246089, 0.02472355, 129.96246089, 0.07417065, 90.97372262, -1533.99977553, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 32.49061522, 7.64e-05, 97.47184567, 0.00022921, 324.90615222, 0.00076402, -32.49061522, -7.64e-05, -97.47184567, -0.00022921, -324.90615222, -0.00076402, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 6.6, 5.7, 5.675)
    ops.node(123007, 6.6, 5.7, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.125, 31324040.71323092, 13051683.63051288, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 228.57474814, 0.00075099, 272.68284518, 0.01594043, 27.26828452, 0.05188678, -228.57474814, -0.00075099, -272.68284518, -0.01594043, -27.26828452, -0.05188678, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 122.463172, 0.00128008, 146.09490525, 0.01368581, 14.60949052, 0.03592407, -122.463172, -0.00128008, -146.09490525, -0.01368581, -14.60949052, -0.03592407, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 206.19604521, 0.01501976, 206.19604521, 0.04505928, 144.33723165, -2554.23867538, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 51.5490113, 0.00010237, 154.64703391, 0.00030712, 515.49011303, 0.00102374, -51.5490113, -0.00010237, -154.64703391, -0.00030712, -515.49011303, -0.00102374, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 145.79290435, 0.02560166, 145.79290435, 0.07680497, 102.05503305, -1643.70489463, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 36.44822609, 7.238e-05, 109.34467827, 0.00021715, 364.48226088, 0.00072384, -36.44822609, -7.238e-05, -109.34467827, -0.00021715, -364.48226088, -0.00072384, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 10.3, 5.7, 5.65)
    ops.node(123008, 10.3, 5.7, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0875, 32495598.19316168, 13539832.58048403, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 99.04684237, 0.00090603, 117.88534004, 0.01529778, 11.788534, 0.0588635, -99.04684237, -0.00090603, -117.88534004, -0.01529778, -11.788534, -0.0588635, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 65.23039495, 0.00120853, 77.63707662, 0.01411442, 7.76370766, 0.04775659, -65.23039495, -0.00120853, -77.63707662, -0.01411442, -7.76370766, -0.04775659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 144.30247416, 0.01812058, 144.30247416, 0.05436175, 101.01173191, -2117.38999223, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 36.07561854, 9.866e-05, 108.22685562, 0.00029598, 360.75618539, 0.00098659, -36.07561854, -9.866e-05, -108.22685562, -0.00029598, -360.75618539, -0.00098659, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 127.01216927, 0.02417057, 127.01216927, 0.0725117, 88.90851849, -1617.53243638, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 31.75304232, 8.684e-05, 95.25912695, 0.00026051, 317.53042317, 0.00086838, -31.75304232, -8.684e-05, -95.25912695, -0.00026051, -317.53042317, -0.00086838, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 11.4, 5.65)
    ops.node(123009, 0.0, 11.4, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 30942893.27039208, 12892872.1959967, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 50.95436459, 0.00125256, 60.67620156, 0.01472081, 6.06762016, 0.05257931, -50.95436459, -0.00125256, -60.67620156, -0.01472081, -6.06762016, -0.05257931, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 50.95436459, 0.00125256, 60.67620156, 0.01472081, 6.06762016, 0.05257931, -50.95436459, -0.00125256, -60.67620156, -0.01472081, -6.06762016, -0.05257931, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 101.6831337, 0.02505125, 101.6831337, 0.07515376, 71.17819359, -1531.4045873, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 25.42078343, 0.00010221, 76.26235028, 0.00030664, 254.20783426, 0.00102213, -25.42078343, -0.00010221, -76.26235028, -0.00030664, -254.20783426, -0.00102213, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 101.6831337, 0.02505125, 101.6831337, 0.07515376, 71.17819359, -1531.4045873, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 25.42078343, 0.00010221, 76.26235028, 0.00030664, 254.20783426, 0.00102213, -25.42078343, -0.00010221, -76.26235028, -0.00030664, -254.20783426, -0.00102213, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 2.9, 11.4, 5.675)
    ops.node(123010, 2.9, 11.4, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0875, 31483339.01953378, 13118057.92480574, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 119.32032079, 0.0009697, 141.75037383, 0.01452039, 14.17503738, 0.04674368, -119.32032079, -0.0009697, -141.75037383, -0.01452039, -14.17503738, -0.04674368, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 82.70404855, 0.00129884, 98.25090749, 0.01351284, 9.82509075, 0.03870005, -82.70404855, -0.00129884, -98.25090749, -0.01351284, -9.82509075, -0.03870005, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 136.32242122, 0.01939398, 136.32242122, 0.05818195, 95.42569485, -1906.2987275, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 34.08060531, 9.62e-05, 102.24181592, 0.0002886, 340.80605305, 0.000962, -34.08060531, -9.62e-05, -102.24181592, -0.0002886, -340.80605305, -0.000962, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 120.39625418, 0.02597683, 120.39625418, 0.07793048, 84.27737792, -1548.22678136, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 30.09906354, 8.496e-05, 90.29719063, 0.00025488, 300.99063544, 0.00084961, -30.09906354, -8.496e-05, -90.29719063, -0.00025488, -300.99063544, -0.00084961, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 6.6, 11.4, 5.675)
    ops.node(123011, 6.6, 11.4, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.125, 31152873.39708161, 12980363.91545067, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 231.79550922, 0.00076065, 276.61514969, 0.01309678, 27.66151497, 0.0419755, -231.79550922, -0.00076065, -276.61514969, -0.01309678, -27.66151497, -0.0419755, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 108.53083565, 0.00129686, 129.51619921, 0.01156927, 12.95161992, 0.03027528, -108.53083565, -0.00129686, -129.51619921, -0.01156927, -12.95161992, -0.03027528, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 185.89246828, 0.01521309, 185.89246828, 0.04563927, 130.1247278, -2030.68207724, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 46.47311707, 9.28e-05, 139.41935121, 0.0002784, 464.7311707, 0.000928, -46.47311707, -9.28e-05, -139.41935121, -0.0002784, -464.7311707, -0.000928, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 113.36804989, 0.02593729, 113.36804989, 0.07781188, 79.35763492, -1426.79281432, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 28.34201247, 5.66e-05, 85.02603742, 0.00016979, 283.42012473, 0.00056595, -28.34201247, -5.66e-05, -85.02603742, -0.00016979, -283.42012473, -0.00056595, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 10.3, 11.4, 5.65)
    ops.node(123012, 10.3, 11.4, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 31174754.26200213, 12989480.94250089, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 57.73536227, 0.00128793, 68.44084948, 0.01409333, 6.84408495, 0.04791721, -57.73536227, -0.00128793, -68.44084948, -0.01409333, -6.84408495, -0.04791721, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 57.73536227, 0.00128793, 68.44084948, 0.01409333, 6.84408495, 0.04791721, -57.73536227, -0.00128793, -68.44084948, -0.01409333, -6.84408495, -0.04791721, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 107.41952304, 0.02575852, 107.41952304, 0.07727557, 75.19366613, -1633.2941247, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 26.85488076, 0.00010718, 80.56464228, 0.00032153, 268.54880761, 0.00107176, -26.85488076, -0.00010718, -80.56464228, -0.00032153, -268.54880761, -0.00107176, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 107.41952304, 0.02575852, 107.41952304, 0.07727557, 75.19366613, -1633.2941247, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 26.85488076, 0.00010718, 80.56464228, 0.00032153, 268.54880761, 0.00107176, -26.85488076, -0.00010718, -80.56464228, -0.00032153, -268.54880761, -0.00107176, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 17.1, 5.65)
    ops.node(123013, 0.0, 17.1, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 32047012.6643503, 13352921.94347929, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 51.21016587, 0.0012033, 60.88723026, 0.01479615, 6.08872303, 0.05511125, -51.21016587, -0.0012033, -60.88723026, -0.01479615, -6.08872303, -0.05511125, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 51.21016587, 0.0012033, 60.88723026, 0.01479615, 6.08872303, 0.05511125, -51.21016587, -0.0012033, -60.88723026, -0.01479615, -6.08872303, -0.05511125, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 104.45126949, 0.02406592, 104.45126949, 0.07219776, 73.11588864, -1542.77068941, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 26.11281737, 0.00010138, 78.33845212, 0.00030413, 261.12817373, 0.00101378, -26.11281737, -0.00010138, -78.33845212, -0.00030413, -261.12817373, -0.00101378, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 104.45126949, 0.02406592, 104.45126949, 0.07219776, 73.11588864, -1542.77068941, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 26.11281737, 0.00010138, 78.33845212, 0.00030413, 261.12817373, 0.00101378, -26.11281737, -0.00010138, -78.33845212, -0.00030413, -261.12817373, -0.00101378, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 2.9, 17.1, 5.675)
    ops.node(123014, 2.9, 17.1, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0875, 31408112.04309945, 13086713.35129144, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 118.75848345, 0.00095767, 141.09552707, 0.0142012, 14.10955271, 0.04627304, -118.75848345, -0.00095767, -141.09552707, -0.0142012, -14.10955271, -0.04627304, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 82.36133282, 0.0012792, 97.8525098, 0.01321633, 9.78525098, 0.03828516, -82.36133282, -0.0012792, -97.8525098, -0.01321633, -9.78525098, -0.03828516, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 134.38042806, 0.01915335, 134.38042806, 0.05746005, 94.06629964, -1861.42697195, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 33.59510701, 9.506e-05, 100.78532104, 0.00028517, 335.95107014, 0.00095057, -33.59510701, -9.506e-05, -100.78532104, -0.00028517, -335.95107014, -0.00095057, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 115.62979769, 0.0255839, 115.62979769, 0.0767517, 80.94085838, -1519.3064742, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 28.90744942, 8.179e-05, 86.72234826, 0.00024538, 289.07449422, 0.00081793, -28.90744942, -8.179e-05, -86.72234826, -0.00024538, -289.07449422, -0.00081793, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 6.6, 17.1, 5.675)
    ops.node(123015, 6.6, 17.1, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.125, 32945460.92006255, 13727275.3833594, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 231.71054646, 0.00075166, 275.57753717, 0.01574102, 27.55775372, 0.05452006, -231.71054646, -0.00075166, -275.57753717, -0.01574102, -27.55775372, -0.05452006, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 123.95806781, 0.00128178, 147.42556849, 0.01352409, 14.74255685, 0.0375148, -123.95806781, -0.00128178, -147.42556849, -0.01352409, -14.74255685, -0.0375148, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 213.14883711, 0.01503326, 213.14883711, 0.04509977, 149.20418598, -2521.37435608, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 53.28720928, 0.00010062, 159.86162784, 0.00030185, 532.87209278, 0.00100618, -53.28720928, -0.00010062, -159.86162784, -0.00030185, -532.87209278, -0.00100618, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 151.12074055, 0.02563567, 151.12074055, 0.076907, 105.78451839, -1627.96194771, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 37.78018514, 7.134e-05, 113.34055541, 0.00021401, 377.80185138, 0.00071337, -37.78018514, -7.134e-05, -113.34055541, -0.00021401, -377.80185138, -0.00071337, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 10.3, 17.1, 5.65)
    ops.node(123016, 10.3, 17.1, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0875, 31428542.7167109, 13095226.13196287, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 100.81295203, 0.00090943, 120.22793624, 0.01461904, 12.02279362, 0.05610305, -100.81295203, -0.00090943, -120.22793624, -0.01461904, -12.02279362, -0.05610305, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 66.08428258, 0.00120057, 78.81107291, 0.01349474, 7.88110729, 0.04552938, -66.08428258, -0.00120057, -78.81107291, -0.01349474, -7.88110729, -0.04552938, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 138.90197553, 0.01818863, 138.90197553, 0.0545659, 97.23138287, -2051.22315646, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 34.72549388, 9.819e-05, 104.17648165, 0.00029457, 347.25493882, 0.00098191, -34.72549388, -9.819e-05, -104.17648165, -0.00029457, -347.25493882, -0.00098191, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 122.22051692, 0.02401131, 122.22051692, 0.07203393, 85.55436184, -1575.18464383, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 30.55512923, 8.64e-05, 91.66538769, 0.0002592, 305.55129229, 0.00086399, -30.55512923, -8.64e-05, -91.66538769, -0.0002592, -305.55129229, -0.00086399, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 22.8, 5.65)
    ops.node(123017, 0.0, 22.8, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 30043662.11403469, 12518192.54751446, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 39.49518453, 0.00116423, 47.49608516, 0.01622585, 4.74960852, 0.06300052, -39.49518453, -0.00116423, -47.49608516, -0.01622585, -4.74960852, -0.06300052, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 39.49518453, 0.00116423, 47.49608516, 0.01622585, 4.74960852, 0.06300052, -39.49518453, -0.00116423, -47.49608516, -0.01622585, -4.74960852, -0.06300052, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 89.77178663, 0.0232845, 89.77178663, 0.06985351, 62.84025064, -1447.42532936, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 22.44294666, 9.294e-05, 67.32883997, 0.00027882, 224.42946658, 0.0009294, -22.44294666, -9.294e-05, -67.32883997, -0.00027882, -224.42946658, -0.0009294, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 89.77178663, 0.0232845, 89.77178663, 0.06985351, 62.84025064, -1447.42532936, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 22.44294666, 9.294e-05, 67.32883997, 0.00027882, 224.42946658, 0.0009294, -22.44294666, -9.294e-05, -67.32883997, -0.00027882, -224.42946658, -0.0009294, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 2.9, 22.8, 5.675)
    ops.node(123018, 2.9, 22.8, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 31004692.3099101, 12918621.79579588, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 67.20652776, 0.00128267, 79.99491478, 0.01529029, 7.99949148, 0.04788659, -67.20652776, -0.00128267, -79.99491478, -0.01529029, -7.99949148, -0.04788659, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 67.20652776, 0.00128267, 79.99491478, 0.01529029, 7.99949148, 0.04788659, -67.20652776, -0.00128267, -79.99491478, -0.01529029, -7.99949148, -0.04788659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 93.31771631, 0.02565338, 93.31771631, 0.07696014, 65.32240142, -1333.9753062, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 23.32942908, 9.362e-05, 69.98828723, 0.00028085, 233.29429077, 0.00093617, -23.32942908, -9.362e-05, -69.98828723, -0.00028085, -233.29429077, -0.00093617, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 93.31771631, 0.02565338, 93.31771631, 0.07696014, 65.32240142, -1333.9753062, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 23.32942908, 9.362e-05, 69.98828723, 0.00028085, 233.29429077, 0.00093617, -23.32942908, -9.362e-05, -69.98828723, -0.00028085, -233.29429077, -0.00093617, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 6.6, 22.8, 5.675)
    ops.node(123019, 6.6, 22.8, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 32316821.6758344, 13465342.364931, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 61.26552528, 0.0012433, 72.62980205, 0.0150179, 7.2629802, 0.05301011, -61.26552528, -0.0012433, -72.62980205, -0.0150179, -7.2629802, -0.05301011, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 65.31551548, 0.0012433, 77.43103382, 0.0150179, 7.74310338, 0.05301011, -65.31551548, -0.0012433, -77.43103382, -0.0150179, -7.74310338, -0.05301011, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 107.96082234, 0.02486596, 107.96082234, 0.07459789, 75.57257564, -1590.74002348, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 26.99020558, 0.00010391, 80.97061675, 0.00031173, 269.90205584, 0.00103909, -26.99020558, -0.00010391, -80.97061675, -0.00031173, -269.90205584, -0.00103909, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 107.96082234, 0.02486596, 107.96082234, 0.07459789, 75.57257564, -1590.74002348, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 26.99020558, 0.00010391, 80.97061675, 0.00031173, 269.90205584, 0.00103909, -26.99020558, -0.00010391, -80.97061675, -0.00031173, -269.90205584, -0.00103909, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 10.3, 22.8, 5.65)
    ops.node(123020, 10.3, 22.8, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 31101968.76518072, 12959153.65215863, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 42.31050712, 0.00116383, 50.65894069, 0.01624326, 5.06589407, 0.06147037, -42.31050712, -0.00116383, -50.65894069, -0.01624326, -5.06589407, -0.06147037, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 42.31050712, 0.00116383, 50.65894069, 0.01624326, 5.06589407, 0.06147037, -42.31050712, -0.00116383, -50.65894069, -0.01624326, -5.06589407, -0.06147037, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 96.20638451, 0.0232766, 96.20638451, 0.0698298, 67.34446916, -1489.07715339, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 24.05159613, 9.621e-05, 72.15478839, 0.00028864, 240.51596129, 0.00096213, -24.05159613, -9.621e-05, -72.15478839, -0.00028864, -240.51596129, -0.00096213, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 96.20638451, 0.0232766, 96.20638451, 0.0698298, 67.34446916, -1489.07715339, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 24.05159613, 9.621e-05, 72.15478839, 0.00028864, 240.51596129, 0.00096213, -24.05159613, -9.621e-05, -72.15478839, -0.00028864, -240.51596129, -0.00096213, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 6.6, 0.0, 8.375)
    ops.node(124003, 6.6, 0.0, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0625, 29567543.18400541, 12319809.66000226, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 50.87865758, 0.00123208, 61.34965693, 0.01734042, 6.13496569, 0.0594903, -50.87865758, -0.00123208, -61.34965693, -0.01734042, -6.13496569, -0.0594903, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 50.87865758, 0.00123208, 61.34965693, 0.01734042, 6.13496569, 0.0594903, -50.87865758, -0.00123208, -61.34965693, -0.01734042, -6.13496569, -0.0594903, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 75.24277767, 0.02464162, 75.24277767, 0.07392487, 52.66994437, -1203.34304193, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 18.81069442, 7.915e-05, 56.43208326, 0.00023746, 188.10694418, 0.00079153, -18.81069442, -7.915e-05, -56.43208326, -0.00023746, -188.10694418, -0.00079153, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 75.24277767, 0.02464162, 75.24277767, 0.07392487, 52.66994437, -1203.34304193, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 18.81069442, 7.915e-05, 56.43208326, 0.00023746, 188.10694418, 0.00079153, -18.81069442, -7.915e-05, -56.43208326, -0.00023746, -188.10694418, -0.00079153, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 10.3, 0.0, 8.35)
    ops.node(124004, 10.3, 0.0, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 30688354.94502965, 12786814.56042902, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 29.2433698, 0.00106091, 35.34721364, 0.01788992, 3.53472136, 0.07560784, -29.2433698, -0.00106091, -35.34721364, -0.01788992, -3.53472136, -0.07560784, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 29.2433698, 0.00106091, 35.34721364, 0.01788992, 3.53472136, 0.07560784, -29.2433698, -0.00106091, -35.34721364, -0.01788992, -3.53472136, -0.07560784, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 83.77579919, 0.02121817, 83.77579919, 0.0636545, 58.64305944, -1835.08689293, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 20.9439498, 8.491e-05, 62.8318494, 0.00025473, 209.43949799, 0.0008491, -20.9439498, -8.491e-05, -62.8318494, -0.00025473, -209.43949799, -0.0008491, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 83.77579919, 0.02121817, 83.77579919, 0.0636545, 58.64305944, -1835.08689293, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 20.9439498, 8.491e-05, 62.8318494, 0.00025473, 209.43949799, 0.0008491, -20.9439498, -8.491e-05, -62.8318494, -0.00025473, -209.43949799, -0.0008491, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 5.7, 8.35)
    ops.node(124005, 0.0, 5.7, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 29948019.45604256, 12478341.44001773, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 32.00019709, 0.00112099, 38.66938823, 0.01793878, 3.86693882, 0.07151745, -32.00019709, -0.00112099, -38.66938823, -0.01793878, -3.86693882, -0.07151745, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 32.00019709, 0.00112099, 38.66938823, 0.01793878, 3.86693882, 0.07151745, -32.00019709, -0.00112099, -38.66938823, -0.01793878, -3.86693882, -0.07151745, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 86.24943581, 0.02241989, 86.24943581, 0.06725966, 60.37460507, -1688.04031969, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 21.56235895, 8.958e-05, 64.68707686, 0.00026874, 215.62358954, 0.00089579, -21.56235895, -8.958e-05, -64.68707686, -0.00026874, -215.62358954, -0.00089579, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 86.24943581, 0.02241989, 86.24943581, 0.06725966, 60.37460507, -1688.04031969, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 21.56235895, 8.958e-05, 64.68707686, 0.00026874, 215.62358954, 0.00089579, -21.56235895, -8.958e-05, -64.68707686, -0.00026874, -215.62358954, -0.00089579, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 2.9, 5.7, 8.375)
    ops.node(124006, 2.9, 5.7, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1, 33767245.88513639, 14069685.7854735, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 98.76413923, 0.00080087, 117.95196633, 0.01660601, 11.79519663, 0.06476091, -98.76413923, -0.00080087, -117.95196633, -0.01660601, -11.79519663, -0.06476091, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 58.38616619, 0.00117914, 69.72938925, 0.01488891, 6.97293893, 0.04925425, -58.38616619, -0.00117914, -69.72938925, -0.01488891, -6.97293893, -0.04925425, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 139.6970635, 0.01601734, 139.6970635, 0.04805202, 97.78794445, -1949.53333336, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 34.92426588, 8.042e-05, 104.77279763, 0.00024127, 349.24265876, 0.00080424, -34.92426588, -8.042e-05, -104.77279763, -0.00024127, -349.24265876, -0.00080424, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 113.76483238, 0.02358279, 113.76483238, 0.07074837, 79.63538266, -1214.14495799, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 28.44120809, 6.55e-05, 85.32362428, 0.00019649, 284.41208094, 0.00065495, -28.44120809, -6.55e-05, -85.32362428, -0.00019649, -284.41208094, -0.00065495, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 6.6, 5.7, 8.375)
    ops.node(124007, 6.6, 5.7, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.125, 33150804.88457468, 13812835.36857278, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 177.68241768, 0.00069592, 212.70509369, 0.01723799, 21.27050937, 0.06542563, -177.68241768, -0.00069592, -212.70509369, -0.01723799, -21.27050937, -0.06542563, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 76.05591064, 0.00113748, 91.04716049, 0.01464794, 9.10471605, 0.04445929, -76.05591064, -0.00113748, -91.04716049, -0.01464794, -9.10471605, -0.04445929, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 189.57299266, 0.01391845, 189.57299266, 0.04175536, 132.70109486, -2463.25181518, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 47.39324816, 8.893e-05, 142.17974449, 0.0002668, 473.93248164, 0.00088934, -47.39324816, -8.893e-05, -142.17974449, -0.0002668, -473.93248164, -0.00088934, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 133.35079215, 0.02274961, 133.35079215, 0.06824882, 93.34555451, -1244.34988217, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 33.33769804, 6.256e-05, 100.01309411, 0.00018768, 333.37698038, 0.00062559, -33.33769804, -6.256e-05, -100.01309411, -0.00018768, -333.37698038, -0.00062559, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 10.3, 5.7, 8.35)
    ops.node(124008, 10.3, 5.7, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0875, 32125868.56503624, 13385778.5687651, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 68.4574715, 0.00082943, 82.28222806, 0.01736279, 8.22822281, 0.07353754, -68.4574715, -0.00082943, -82.28222806, -0.01736279, -8.22822281, -0.07353754, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 43.57590971, 0.00108695, 52.3759184, 0.01591334, 5.23759184, 0.05929242, -43.57590971, -0.00108695, -52.3759184, -0.01591334, -5.23759184, -0.05929242, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 126.89873695, 0.0165886, 126.89873695, 0.0497658, 88.82911586, -2382.26787644, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 31.72468424, 8.776e-05, 95.17405271, 0.00026328, 317.24684236, 0.00087759, -31.72468424, -8.776e-05, -95.17405271, -0.00026328, -317.24684236, -0.00087759, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 109.43864547, 0.02173905, 109.43864547, 0.06521716, 76.60705183, -1557.98349263, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 27.35966137, 7.568e-05, 82.0789841, 0.00022705, 273.59661368, 0.00075684, -27.35966137, -7.568e-05, -82.0789841, -0.00022705, -273.59661368, -0.00075684, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 11.4, 8.35)
    ops.node(124009, 0.0, 11.4, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 31567460.13475573, 13153108.38948155, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 32.83693055, 0.00115568, 39.51273531, 0.01717083, 3.95127353, 0.07207946, -32.83693055, -0.00115568, -39.51273531, -0.01717083, -3.95127353, -0.07207946, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 32.83693055, 0.00115568, 39.51273531, 0.01717083, 3.95127353, 0.07207946, -32.83693055, -0.00115568, -39.51273531, -0.01717083, -3.95127353, -0.07207946, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 88.82336798, 0.0231137, 88.82336798, 0.06934109, 62.17635758, -1602.72894654, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 22.20584199, 8.752e-05, 66.61752598, 0.00026256, 222.05841994, 0.00087519, -22.20584199, -8.752e-05, -66.61752598, -0.00026256, -222.05841994, -0.00087519, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 88.82336798, 0.0231137, 88.82336798, 0.06934109, 62.17635758, -1602.72894654, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 22.20584199, 8.752e-05, 66.61752598, 0.00026256, 222.05841994, 0.00087519, -22.20584199, -8.752e-05, -66.61752598, -0.00026256, -222.05841994, -0.00087519, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 2.9, 11.4, 8.375)
    ops.node(124010, 2.9, 11.4, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0875, 32010235.18021073, 13337597.99175447, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 86.80931384, 0.00091794, 104.08550806, 0.01662982, 10.40855081, 0.06137692, -86.80931384, -0.00091794, -104.08550806, -0.01662982, -10.40855081, -0.06137692, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 59.44890081, 0.0012283, 71.2800133, 0.0153903, 7.12800133, 0.0503667, -59.44890081, -0.0012283, -71.2800133, -0.0153903, -7.12800133, -0.0503667, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 120.90293775, 0.01835884, 120.90293775, 0.05507651, 84.63205643, -1729.10507587, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 30.22573444, 8.391e-05, 90.67720331, 0.00025174, 302.25734438, 0.00083914, -30.22573444, -8.391e-05, -90.67720331, -0.00025174, -302.25734438, -0.00083914, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 104.50093283, 0.02456603, 104.50093283, 0.0736981, 73.15065298, -1244.66116713, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 26.12523321, 7.253e-05, 78.37569962, 0.00021759, 261.25233206, 0.0007253, -26.12523321, -7.253e-05, -78.37569962, -0.00021759, -261.25233206, -0.0007253, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 6.6, 11.4, 8.375)
    ops.node(124011, 6.6, 11.4, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.125, 30437284.81080484, 12682202.00450202, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 177.63499275, 0.00074406, 214.17334165, 0.0152316, 21.41733417, 0.05193339, -177.63499275, -0.00074406, -214.17334165, -0.0152316, -21.41733417, -0.05193339, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 81.06865999, 0.00128484, 97.74394979, 0.01334875, 9.77439498, 0.0371221, -81.06865999, -0.00128484, -97.74394979, -0.01334875, -9.77439498, -0.0371221, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 160.62595679, 0.01488112, 160.62595679, 0.04464335, 112.43816976, -1849.37346287, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 40.1564892, 8.207e-05, 120.4694676, 0.00024622, 401.56489199, 0.00082072, -40.1564892, -8.207e-05, -120.4694676, -0.00024622, -401.56489199, -0.00082072, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 90.3375731, 0.02569678, 90.3375731, 0.07709035, 63.23630117, -1020.0944808, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 22.58439327, 4.616e-05, 67.75317982, 0.00013847, 225.84393274, 0.00046158, -22.58439327, -4.616e-05, -67.75317982, -0.00013847, -225.84393274, -0.00046158, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 10.3, 11.4, 8.35)
    ops.node(124012, 10.3, 11.4, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 30816431.0851094, 12840179.61879558, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 35.72218579, 0.00117005, 42.97373106, 0.01679227, 4.29737311, 0.06749121, -35.72218579, -0.00117005, -42.97373106, -0.01679227, -4.29737311, -0.06749121, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 35.72218579, 0.00117005, 42.97373106, 0.01679227, 4.29737311, 0.06749121, -35.72218579, -0.00117005, -42.97373106, -0.01679227, -4.29737311, -0.06749121, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 89.03020737, 0.023401, 89.03020737, 0.070203, 62.32114516, -1468.51279508, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 22.25755184, 8.986e-05, 66.77265553, 0.00026958, 222.57551842, 0.00089861, -22.25755184, -8.986e-05, -66.77265553, -0.00026958, -222.57551842, -0.00089861, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 89.03020737, 0.023401, 89.03020737, 0.070203, 62.32114516, -1468.51279508, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 22.25755184, 8.986e-05, 66.77265553, 0.00026958, 222.57551842, 0.00089861, -22.25755184, -8.986e-05, -66.77265553, -0.00026958, -222.57551842, -0.00089861, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 17.1, 8.35)
    ops.node(124013, 0.0, 17.1, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 31380797.09414742, 13075332.12256142, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 33.09257586, 0.00110397, 39.83956801, 0.01724529, 3.9839568, 0.07193707, -33.09257586, -0.00110397, -39.83956801, -0.01724529, -3.9839568, -0.07193707, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 33.09257586, 0.00110397, 39.83956801, 0.01724529, 3.9839568, 0.07193707, -33.09257586, -0.00110397, -39.83956801, -0.01724529, -3.9839568, -0.07193707, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 88.59373926, 0.02207949, 88.59373926, 0.06623848, 62.01561748, -1609.44609126, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 22.14843482, 8.781e-05, 66.44530445, 0.00026344, 221.48434815, 0.00087812, -22.14843482, -8.781e-05, -66.44530445, -0.00026344, -221.48434815, -0.00087812, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 88.59373926, 0.02207949, 88.59373926, 0.06623848, 62.01561748, -1609.44609126, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 22.14843482, 8.781e-05, 66.44530445, 0.00026344, 221.48434815, 0.00087812, -22.14843482, -8.781e-05, -66.44530445, -0.00026344, -221.48434815, -0.00087812, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 2.9, 17.1, 8.375)
    ops.node(124014, 2.9, 17.1, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0875, 30980573.51540961, 12908572.29808734, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 85.64880566, 0.00091927, 102.94022628, 0.0169168, 10.29402263, 0.06034362, -85.64880566, -0.00091927, -102.94022628, -0.0169168, -10.29402263, -0.06034362, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 58.6138594, 0.00123299, 70.44726315, 0.01565247, 7.04472631, 0.04959687, -58.6138594, -0.00123299, -70.44726315, -0.01565247, -7.04472631, -0.04959687, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 117.89553013, 0.01838534, 117.89553013, 0.05515602, 82.52687109, -1724.6534432, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 29.47388253, 8.455e-05, 88.4216476, 0.00025364, 294.73882533, 0.00084547, -29.47388253, -8.455e-05, -88.4216476, -0.00025364, -294.73882533, -0.00084547, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 102.20081035, 0.02465984, 102.20081035, 0.07397953, 71.54056724, -1241.96311453, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 25.55020259, 7.329e-05, 76.65060776, 0.00021987, 255.50202587, 0.00073291, -25.55020259, -7.329e-05, -76.65060776, -0.00021987, -255.50202587, -0.00073291, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 6.6, 17.1, 8.375)
    ops.node(124015, 6.6, 17.1, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.125, 29777018.84654119, 12407091.18605883, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 176.00765769, 0.0007239, 212.49486656, 0.01752348, 21.24948666, 0.06205763, -176.00765769, -0.0007239, -212.49486656, -0.01752348, -21.24948666, -0.06205763, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 74.907913, 0.00121274, 90.43667295, 0.01493351, 9.0436673, 0.04248463, -74.907913, -0.00121274, -90.43667295, -0.01493351, -9.0436673, -0.04248463, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 173.7378775, 0.01447808, 173.7378775, 0.04343424, 121.61651425, -2466.72389929, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 43.43446938, 9.074e-05, 130.30340813, 0.00027222, 434.34469375, 0.0009074, -43.43446938, -9.074e-05, -130.30340813, -0.00027222, -434.34469375, -0.0009074, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 118.44294722, 0.0242547, 118.44294722, 0.07276411, 82.91006305, -1243.95942059, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 29.6107368, 6.186e-05, 88.83221041, 0.00018558, 296.10736805, 0.00061861, -29.6107368, -6.186e-05, -88.83221041, -0.00018558, -296.10736805, -0.00061861, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 10.3, 17.1, 8.35)
    ops.node(124016, 10.3, 17.1, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0875, 33384676.62131044, 13910281.92554602, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 67.97068611, 0.00085066, 81.38529226, 0.01668858, 8.13852923, 0.07409851, -67.97068611, -0.00085066, -81.38529226, -0.01668858, -8.13852923, -0.07409851, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 43.46352976, 0.00113089, 52.04143542, 0.01533364, 5.20414354, 0.05966654, -43.46352976, -0.00113089, -52.04143542, -0.01533364, -5.20414354, -0.05966654, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 128.10464088, 0.0170132, 128.10464088, 0.0510396, 89.67324862, -2268.27033471, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 32.02616022, 8.525e-05, 96.07848066, 0.00025576, 320.2616022, 0.00085252, -32.02616022, -8.525e-05, -96.07848066, -0.00025576, -320.2616022, -0.00085252, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 111.29370158, 0.0226177, 111.29370158, 0.0678531, 77.9055911, -1491.27932593, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 27.82342539, 7.406e-05, 83.47027618, 0.00022219, 278.23425395, 0.00074065, -27.82342539, -7.406e-05, -83.47027618, -0.00022219, -278.23425395, -0.00074065, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 22.8, 8.35)
    ops.node(124017, 0.0, 22.8, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 31185685.79842636, 12994035.74934432, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 26.85071363, 0.00111009, 32.44635764, 0.01830449, 3.24463576, 0.07830941, -26.85071363, -0.00111009, -32.44635764, -0.01830449, -3.24463576, -0.07830941, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 26.85071363, 0.00111009, 32.44635764, 0.01830449, 3.24463576, 0.07830941, -26.85071363, -0.00111009, -32.44635764, -0.01830449, -3.24463576, -0.07830941, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 83.52707001, 0.02220179, 83.52707001, 0.06660536, 58.46894901, -2106.39780148, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 20.8817675, 8.331e-05, 62.64530251, 0.00024992, 208.81767503, 0.00083308, -20.8817675, -8.331e-05, -62.64530251, -0.00024992, -208.81767503, -0.00083308, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 83.52707001, 0.02220179, 83.52707001, 0.06660536, 58.46894901, -2106.39780148, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 20.8817675, 8.331e-05, 62.64530251, 0.00024992, 208.81767503, 0.00083308, -20.8817675, -8.331e-05, -62.64530251, -0.00024992, -208.81767503, -0.00083308, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 2.9, 22.8, 8.375)
    ops.node(124018, 2.9, 22.8, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 31333445.74991001, 13055602.39579584, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 48.83310092, 0.00117955, 58.73754357, 0.01809502, 5.87375436, 0.06407059, -48.83310092, -0.00117955, -58.73754357, -0.01809502, -5.87375436, -0.06407059, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 48.83310092, 0.00117955, 58.73754357, 0.01809502, 5.87375436, 0.06407059, -48.83310092, -0.00117955, -58.73754357, -0.01809502, -5.87375436, -0.06407059, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 82.20906942, 0.02359091, 82.20906942, 0.07077272, 57.5463486, -1261.03732936, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 20.55226736, 8.161e-05, 61.65680207, 0.00024482, 205.52267356, 0.00081607, -20.55226736, -8.161e-05, -61.65680207, -0.00024482, -205.52267356, -0.00081607, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 82.20906942, 0.02359091, 82.20906942, 0.07077272, 57.5463486, -1261.03732936, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 20.55226736, 8.161e-05, 61.65680207, 0.00024482, 205.52267356, 0.00081607, -20.55226736, -8.161e-05, -61.65680207, -0.00024482, -205.52267356, -0.00081607, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 6.6, 22.8, 8.375)
    ops.node(124019, 6.6, 22.8, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 30896740.23048757, 12873641.76270315, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 41.86995845, 0.00118697, 50.35959489, 0.01738487, 5.03595949, 0.06816882, -41.86995845, -0.00118697, -50.35959489, -0.01738487, -5.03595949, -0.06816882, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 45.22967169, 0.00118697, 54.4005303, 0.01738487, 5.44005303, 0.06816882, -45.22967169, -0.00118697, -54.4005303, -0.01738487, -5.44005303, -0.06816882, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 90.60145152, 0.02373934, 90.60145152, 0.07121801, 63.42101607, -1525.46871956, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 22.65036288, 9.121e-05, 67.95108864, 0.00027363, 226.50362881, 0.00091209, -22.65036288, -9.121e-05, -67.95108864, -0.00027363, -226.50362881, -0.00091209, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 90.60145152, 0.02373934, 90.60145152, 0.07121801, 63.42101607, -1525.46871956, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 22.65036288, 9.121e-05, 67.95108864, 0.00027363, 226.50362881, 0.00091209, -22.65036288, -9.121e-05, -67.95108864, -0.00027363, -226.50362881, -0.00091209, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 10.3, 22.8, 8.35)
    ops.node(124020, 10.3, 22.8, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 30724527.35772214, 12801886.39905089, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 29.40945595, 0.00106299, 35.54465916, 0.01828652, 3.55446592, 0.076038, -29.40945595, -0.00106299, -35.54465916, -0.01828652, -3.55446592, -0.076038, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 29.40945595, 0.00106299, 35.54465916, 0.01828652, 3.55446592, 0.076038, -29.40945595, -0.00106299, -35.54465916, -0.01828652, -3.55446592, -0.076038, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 85.52185907, 0.02125987, 85.52185907, 0.0637796, 59.86530135, -1943.35886824, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 21.38046477, 8.658e-05, 64.1413943, 0.00025973, 213.80464767, 0.00086578, -21.38046477, -8.658e-05, -64.1413943, -0.00025973, -213.80464767, -0.00086578, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 85.52185907, 0.02125987, 85.52185907, 0.0637796, 59.86530135, -1943.35886824, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 21.38046477, 8.658e-05, 64.1413943, 0.00025973, 213.80464767, 0.00086578, -21.38046477, -8.658e-05, -64.1413943, -0.00025973, -213.80464767, -0.00086578, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124021, 0.0, 0.0, 1.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 170001, 124021, 0.0625, 31055074.27362947, 12939614.28067895, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 71.6047959, 0.00089334, 85.11486194, 0.03559628, 8.51148619, 0.11576057, -71.6047959, -0.00089334, -85.11486194, -0.03559628, -8.51148619, -0.11576057, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 63.86343894, 0.00089334, 75.91290109, 0.03559628, 7.59129011, 0.11576057, -63.86343894, -0.00089334, -75.91290109, -0.03559628, -7.59129011, -0.11576057, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 177.78166121, 0.01786672, 177.78166121, 0.05360015, 124.44716285, -7695.84508565, 0.05, 2, 0, 70001, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 44.4454153, 8.903e-05, 133.33624591, 0.00026709, 444.45415303, 0.00089031, -44.4454153, -8.903e-05, -133.33624591, -0.00026709, -444.45415303, -0.00089031, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 177.78166121, 0.01786672, 177.78166121, 0.05360015, 124.44716285, -7695.84508565, 0.05, 2, 0, 70001, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 44.4454153, 8.903e-05, 133.33624591, 0.00026709, 444.45415303, 0.00089031, -44.4454153, -8.903e-05, -133.33624591, -0.00026709, -444.45415303, -0.00089031, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 0.0, 0.0, 1.55)
    ops.node(121001, 0.0, 0.0, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 174021, 121001, 0.0625, 32241364.15806303, 13433901.73252626, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 59.36704506, 0.00086592, 70.63589142, 0.01504006, 7.06358914, 0.05705627, -59.36704506, -0.00086592, -70.63589142, -0.01504006, -7.06358914, -0.05705627, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 55.54476574, 0.00086592, 66.08808032, 0.01504006, 6.60880803, 0.05705627, -55.54476574, -0.00086592, -66.08808032, -0.01504006, -6.60880803, -0.05705627, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 113.75532881, 0.01731834, 113.75532881, 0.05195503, 79.62873017, -2990.54519935, 0.05, 2, 0, 74021, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 28.4388322, 5.487e-05, 85.31649661, 0.00016461, 284.38832202, 0.00054871, -28.4388322, -5.487e-05, -85.31649661, -0.00016461, -284.38832202, -0.00054871, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 113.75532881, 0.01731834, 113.75532881, 0.05195503, 79.62873017, -2990.54519935, 0.05, 2, 0, 74021, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 28.4388322, 5.487e-05, 85.31649661, 0.00016461, 284.38832202, 0.00054871, -28.4388322, -5.487e-05, -85.31649661, -0.00016461, -284.38832202, -0.00054871, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 2.9, 0.0, 0.0)
    ops.node(124022, 2.9, 0.0, 1.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 170002, 124022, 0.09, 31924882.2026888, 13302034.25112033, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 140.12243142, 0.00082188, 165.15386418, 0.0157261, 16.51538642, 0.04744678, -140.12243142, -0.00082188, -165.15386418, -0.0157261, -16.51538642, -0.04744678, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 123.47307021, 0.00082188, 145.53026564, 0.0157261, 14.55302656, 0.04744678, -123.47307021, -0.00082188, -145.53026564, -0.0157261, -14.55302656, -0.04744678, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 206.41328412, 0.01643762, 206.41328412, 0.04931286, 144.48929888, -4998.26930726, 0.05, 2, 0, 70002, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 51.60332103, 6.983e-05, 154.80996309, 0.00020949, 516.03321029, 0.00069828, -51.60332103, -6.983e-05, -154.80996309, -0.00020949, -516.03321029, -0.00069828, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 206.41328412, 0.01643762, 206.41328412, 0.04931286, 144.48929888, -4998.26930726, 0.05, 2, 0, 70002, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 51.60332103, 6.983e-05, 154.80996309, 0.00020949, 516.03321029, 0.00069828, -51.60332103, -6.983e-05, -154.80996309, -0.00020949, -516.03321029, -0.00069828, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 2.9, 0.0, 1.55)
    ops.node(121002, 2.9, 0.0, 2.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4055, 174022, 121002, 0.09, 31036334.67733297, 12931806.1155554, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24055, 117.05769478, 0.00081642, 138.29519891, 0.01595438, 13.82951989, 0.04714312, -117.05769478, -0.00081642, -138.29519891, -0.01595438, -13.82951989, -0.04714312, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14055, 117.05769478, 0.00081642, 138.29519891, 0.01595438, 13.82951989, 0.04714312, -117.05769478, -0.00081642, -138.29519891, -0.01595438, -13.82951989, -0.04714312, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24055, 4055, 0.0, 199.28606535, 0.01632833, 199.28606535, 0.048985, 139.50024575, -4911.11544067, 0.05, 2, 0, 74022, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44055, 49.82151634, 6.935e-05, 149.46454901, 0.00020804, 498.21516338, 0.00069347, -49.82151634, -6.935e-05, -149.46454901, -0.00020804, -498.21516338, -0.00069347, 0.4, 0.3, 0.003, 0.0, 0.0, 24055, 2)
    ops.limitCurve('ThreePoint', 14055, 4055, 0.0, 199.28606535, 0.01632833, 199.28606535, 0.048985, 139.50024575, -4911.11544067, 0.05, 2, 0, 74022, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34055, 49.82151634, 6.935e-05, 149.46454901, 0.00020804, 498.21516338, 0.00069347, -49.82151634, -6.935e-05, -149.46454901, -0.00020804, -498.21516338, -0.00069347, 0.4, 0.3, 0.003, 0.0, 0.0, 14055, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4055, 99999, 'P', 44055, 'Vy', 34055, 'Vz', 24055, 'My', 14055, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4055, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4055, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 2.95)
    ops.node(124023, 0.0, 0.0, 3.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 171001, 124023, 0.0625, 29300788.37672226, 12208661.82363428, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 45.09612071, 0.00087531, 53.99883353, 0.01496471, 5.39988335, 0.0535739, -45.09612071, -0.00087531, -53.99883353, -0.01496471, -5.39988335, -0.0535739, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 45.09612071, 0.00087531, 53.99883353, 0.01496471, 5.39988335, 0.0535739, -45.09612071, -0.00087531, -53.99883353, -0.01496471, -5.39988335, -0.0535739, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 103.80842143, 0.01750622, 103.80842143, 0.05251865, 72.665895, -2965.5307197, 0.05, 2, 0, 71001, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 25.95210536, 5.51e-05, 77.85631607, 0.0001653, 259.52105358, 0.00055098, -25.95210536, -5.51e-05, -77.85631607, -0.0001653, -259.52105358, -0.00055098, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 103.80842143, 0.01750622, 103.80842143, 0.05251865, 72.665895, -2965.5307197, 0.05, 2, 0, 71001, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 25.95210536, 5.51e-05, 77.85631607, 0.0001653, 259.52105358, 0.00055098, -25.95210536, -5.51e-05, -77.85631607, -0.0001653, -259.52105358, -0.00055098, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 0.0, 0.0, 4.25)
    ops.node(122001, 0.0, 0.0, 5.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 174023, 122001, 0.0625, 32116081.30672419, 13381700.54446841, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 41.42489233, 0.0008162, 49.53280438, 0.01570484, 4.95328044, 0.06378033, -41.42489233, -0.0008162, -49.53280438, -0.01570484, -4.95328044, -0.06378033, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 41.42489233, 0.0008162, 49.53280438, 0.01570484, 4.95328044, 0.06378033, -41.42489233, -0.0008162, -49.53280438, -0.01570484, -4.95328044, -0.06378033, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 106.50445196, 0.01632402, 106.50445196, 0.04897207, 74.55311637, -2916.0340164, 0.05, 2, 0, 74023, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 26.62611299, 5.157e-05, 79.87833897, 0.00015472, 266.26112991, 0.00051574, -26.62611299, -5.157e-05, -79.87833897, -0.00015472, -266.26112991, -0.00051574, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 106.50445196, 0.01632402, 106.50445196, 0.04897207, 74.55311637, -2916.0340164, 0.05, 2, 0, 74023, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 26.62611299, 5.157e-05, 79.87833897, 0.00015472, 266.26112991, 0.00051574, -26.62611299, -5.157e-05, -79.87833897, -0.00015472, -266.26112991, -0.00051574, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 2.9, 0.0, 2.975)
    ops.node(124024, 2.9, 0.0, 3.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 171002, 124024, 0.09, 30751702.89166789, 12813209.53819495, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 98.00477163, 0.0007683, 116.43554629, 0.01277791, 11.64355463, 0.04288191, -98.00477163, -0.0007683, -116.43554629, -0.01277791, -11.64355463, -0.04288191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 92.54105045, 0.0007683, 109.94431785, 0.01277791, 10.99443179, 0.04288191, -92.54105045, -0.0007683, -109.94431785, -0.01277791, -10.99443179, -0.04288191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 174.69077913, 0.01536598, 174.69077913, 0.04609794, 122.28354539, -3905.70751846, 0.05, 2, 0, 71002, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 43.67269478, 6.135e-05, 131.01808435, 0.00018405, 436.72694782, 0.00061351, -43.67269478, -6.135e-05, -131.01808435, -0.00018405, -436.72694782, -0.00061351, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 174.69077913, 0.01536598, 174.69077913, 0.04609794, 122.28354539, -3905.70751846, 0.05, 2, 0, 71002, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 43.67269478, 6.135e-05, 131.01808435, 0.00018405, 436.72694782, 0.00061351, -43.67269478, -6.135e-05, -131.01808435, -0.00018405, -436.72694782, -0.00061351, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 2.9, 0.0, 4.25)
    ops.node(122002, 2.9, 0.0, 5.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4060, 174024, 122002, 0.09, 31520819.19874612, 13133674.66614422, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24060, 91.80293951, 0.00077809, 109.19239743, 0.01372711, 10.91923974, 0.04725856, -91.80293951, -0.00077809, -109.19239743, -0.01372711, -10.91923974, -0.04725856, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14060, 87.01459643, 0.00077809, 103.49703883, 0.01372711, 10.34970388, 0.04725856, -87.01459643, -0.00077809, -103.49703883, -0.01372711, -10.34970388, -0.04725856, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24060, 4060, 0.0, 175.09619477, 0.01556172, 175.09619477, 0.04668515, 122.56733634, -3841.9005441, 0.05, 2, 0, 74024, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44060, 43.77404869, 5.999e-05, 131.32214608, 0.00017998, 437.74048693, 0.00059993, -43.77404869, -5.999e-05, -131.32214608, -0.00017998, -437.74048693, -0.00059993, 0.4, 0.3, 0.003, 0.0, 0.0, 24060, 2)
    ops.limitCurve('ThreePoint', 14060, 4060, 0.0, 175.09619477, 0.01556172, 175.09619477, 0.04668515, 122.56733634, -3841.9005441, 0.05, 2, 0, 74024, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34060, 43.77404869, 5.999e-05, 131.32214608, 0.00017998, 437.74048693, 0.00059993, -43.77404869, -5.999e-05, -131.32214608, -0.00017998, -437.74048693, -0.00059993, 0.4, 0.3, 0.003, 0.0, 0.0, 14060, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4060, 99999, 'P', 44060, 'Vy', 34060, 'Vz', 24060, 'My', 14060, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4060, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4060, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.65)
    ops.node(124025, 0.0, 0.0, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 172001, 124025, 0.0625, 29543582.66215923, 12309826.10923301, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 37.72032946, 0.00080783, 45.4398844, 0.01644576, 4.54398844, 0.06360191, -37.72032946, -0.00080783, -45.4398844, -0.01644576, -4.54398844, -0.06360191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 37.72032946, 0.00080783, 45.4398844, 0.01644576, 4.54398844, 0.06360191, -37.72032946, -0.00080783, -45.4398844, -0.01644576, -4.54398844, -0.06360191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 97.69442793, 0.01615657, 97.69442793, 0.0484697, 68.38609955, -3022.52724201, 0.05, 2, 0, 72001, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 24.42360698, 5.143e-05, 73.27082095, 0.00015428, 244.23606983, 0.00051427, -24.42360698, -5.143e-05, -73.27082095, -0.00015428, -244.23606983, -0.00051427, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 97.69442793, 0.01615657, 97.69442793, 0.0484697, 68.38609955, -3022.52724201, 0.05, 2, 0, 72001, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 24.42360698, 5.143e-05, 73.27082095, 0.00015428, 244.23606983, 0.00051427, -24.42360698, -5.143e-05, -73.27082095, -0.00015428, -244.23606983, -0.00051427, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 0.0, 0.0, 6.925)
    ops.node(123001, 0.0, 0.0, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 174025, 123001, 0.0625, 31719754.5251003, 13216564.38545846, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 31.67376645, 0.00077974, 38.10608127, 0.01748095, 3.81060813, 0.07292263, -31.67376645, -0.00077974, -38.10608127, -0.01748095, -3.81060813, -0.07292263, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 31.67376645, 0.00077974, 38.10608127, 0.01748095, 3.81060813, 0.07292263, -31.67376645, -0.00077974, -38.10608127, -0.01748095, -3.81060813, -0.07292263, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 97.67875277, 0.01559479, 97.67875277, 0.04678438, 68.37512694, -3265.11571062, 0.05, 2, 0, 74025, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 24.41968819, 4.789e-05, 73.25906458, 0.00014367, 244.19688193, 0.00047891, -24.41968819, -4.789e-05, -73.25906458, -0.00014367, -244.19688193, -0.00047891, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 97.67875277, 0.01559479, 97.67875277, 0.04678438, 68.37512694, -3265.11571062, 0.05, 2, 0, 74025, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 24.41968819, 4.789e-05, 73.25906458, 0.00014367, 244.19688193, 0.00047891, -24.41968819, -4.789e-05, -73.25906458, -0.00014367, -244.19688193, -0.00047891, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 2.9, 0.0, 5.675)
    ops.node(124026, 2.9, 0.0, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 172002, 124026, 0.0625, 31056615.85430542, 12940256.60596059, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 53.91591699, 0.00086566, 64.11056161, 0.01374599, 6.41105616, 0.05040943, -53.91591699, -0.00086566, -64.11056161, -0.01374599, -6.41105616, -0.05040943, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 53.91591699, 0.00086566, 64.11056161, 0.01374599, 6.41105616, 0.05040943, -53.91591699, -0.00086566, -64.11056161, -0.01374599, -6.41105616, -0.05040943, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 113.3949442, 0.01731323, 113.3949442, 0.05193969, 79.37646094, -3046.69024096, 0.05, 2, 0, 72002, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 28.34873605, 5.678e-05, 85.04620815, 0.00017035, 283.4873605, 0.00056784, -28.34873605, -5.678e-05, -85.04620815, -0.00017035, -283.4873605, -0.00056784, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 113.3949442, 0.01731323, 113.3949442, 0.05193969, 79.37646094, -3046.69024096, 0.05, 2, 0, 72002, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 28.34873605, 5.678e-05, 85.04620815, 0.00017035, 283.4873605, 0.00056784, -28.34873605, -5.678e-05, -85.04620815, -0.00017035, -283.4873605, -0.00056784, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 2.9, 0.0, 6.925)
    ops.node(123002, 2.9, 0.0, 7.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 174026, 123002, 0.0625, 31317128.95899792, 13048803.7329158, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 47.6929482, 0.00085497, 56.86955719, 0.01469362, 5.68695572, 0.0555513, -47.6929482, -0.00085497, -56.86955719, -0.01469362, -5.68695572, -0.0555513, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 47.6929482, 0.00085497, 56.86955719, 0.01469362, 5.68695572, 0.0555513, -47.6929482, -0.00085497, -56.86955719, -0.01469362, -5.68695572, -0.0555513, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 109.93673475, 0.01709931, 109.93673475, 0.05129792, 76.95571432, -2934.74794242, 0.05, 2, 0, 74026, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 27.48418369, 5.459e-05, 82.45255106, 0.00016378, 274.84183686, 0.00054594, -27.48418369, -5.459e-05, -82.45255106, -0.00016378, -274.84183686, -0.00054594, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 109.93673475, 0.01709931, 109.93673475, 0.05129792, 76.95571432, -2934.74794242, 0.05, 2, 0, 74026, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 27.48418369, 5.459e-05, 82.45255106, 0.00016378, 274.84183686, 0.00054594, -27.48418369, -5.459e-05, -82.45255106, -0.00016378, -274.84183686, -0.00054594, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.35)
    ops.node(124027, 0.0, 0.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4067, 173001, 124027, 0.0625, 31122684.38147728, 12967785.15894887, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24067, 27.50787645, 0.00077048, 33.23868735, 0.01792542, 3.32386874, 0.07747344, -27.50787645, -0.00077048, -33.23868735, -0.01792542, -3.32386874, -0.07747344, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14067, 27.50787645, 0.00077048, 33.23868735, 0.01792542, 3.32386874, 0.07747344, -27.50787645, -0.00077048, -33.23868735, -0.01792542, -3.32386874, -0.07747344, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24067, 4067, 0.0, 91.17728434, 0.0154097, 91.17728434, 0.0462291, 63.82409904, -4041.95498983, 0.05, 2, 0, 73001, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44067, 22.79432109, 4.556e-05, 68.38296326, 0.00013668, 227.94321086, 0.00045561, -22.79432109, -4.556e-05, -68.38296326, -0.00013668, -227.94321086, -0.00045561, 0.4, 0.3, 0.003, 0.0, 0.0, 24067, 2)
    ops.limitCurve('ThreePoint', 14067, 4067, 0.0, 91.17728434, 0.0154097, 91.17728434, 0.0462291, 63.82409904, -4041.95498983, 0.05, 2, 0, 73001, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34067, 22.79432109, 4.556e-05, 68.38296326, 0.00013668, 227.94321086, 0.00045561, -22.79432109, -4.556e-05, -68.38296326, -0.00013668, -227.94321086, -0.00045561, 0.4, 0.3, 0.003, 0.0, 0.0, 14067, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4067, 99999, 'P', 44067, 'Vy', 34067, 'Vz', 24067, 'My', 14067, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4067, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4067, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 0.0, 0.0, 9.625)
    ops.node(124001, 0.0, 0.0, 10.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 174027, 124001, 0.0625, 30966197.938402, 12902582.47433417, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 22.1931472, 0.00073297, 26.91423554, 0.01866994, 2.69142355, 0.0840419, -22.1931472, -0.00073297, -26.91423554, -0.01866994, -2.69142355, -0.0840419, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 22.1931472, 0.00073297, 26.91423554, 0.01866994, 2.69142355, 0.0840419, -22.1931472, -0.00073297, -26.91423554, -0.01866994, -2.69142355, -0.0840419, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 84.77639493, 0.01465946, 84.77639493, 0.04397839, 59.34347645, -13163.67643164, 0.05, 2, 0, 74027, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 21.19409873, 4.258e-05, 63.5822962, 0.00012773, 211.94098732, 0.00042577, -21.19409873, -4.258e-05, -63.5822962, -0.00012773, -211.94098732, -0.00042577, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 84.77639493, 0.01465946, 84.77639493, 0.04397839, 59.34347645, -13163.67643164, 0.05, 2, 0, 74027, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 21.19409873, 4.258e-05, 63.5822962, 0.00012773, 211.94098732, 0.00042577, -21.19409873, -4.258e-05, -63.5822962, -0.00012773, -211.94098732, -0.00042577, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 2.9, 0.0, 8.375)
    ops.node(124028, 2.9, 0.0, 9.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 173002, 124028, 0.0625, 31444661.40631235, 13101942.25263015, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 34.27032848, 0.00080357, 41.20066668, 0.01673083, 4.12006667, 0.0695518, -34.27032848, -0.00080357, -41.20066668, -0.01673083, -4.12006667, -0.0695518, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 34.27032848, 0.00080357, 41.20066668, 0.01673083, 4.12006667, 0.0695518, -34.27032848, -0.00080357, -41.20066668, -0.01673083, -4.12006667, -0.0695518, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 99.23179106, 0.01607131, 99.23179106, 0.04821394, 69.46225375, -3084.89400052, 0.05, 2, 0, 73002, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 24.80794777, 4.908e-05, 74.4238433, 0.00014724, 248.07947766, 0.00049078, -24.80794777, -4.908e-05, -74.4238433, -0.00014724, -248.07947766, -0.00049078, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 99.23179106, 0.01607131, 99.23179106, 0.04821394, 69.46225375, -3084.89400052, 0.05, 2, 0, 73002, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 24.80794777, 4.908e-05, 74.4238433, 0.00014724, 248.07947766, 0.00049078, -24.80794777, -4.908e-05, -74.4238433, -0.00014724, -248.07947766, -0.00049078, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 2.9, 0.0, 9.625)
    ops.node(124002, 2.9, 0.0, 10.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 174028, 124002, 0.0625, 33186641.13703529, 13827767.14043137, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 30.31065501, 0.0007632, 36.35790864, 0.01677731, 3.63579086, 0.07601386, -30.31065501, -0.0007632, -36.35790864, -0.01677731, -3.63579086, -0.07601386, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 30.31065501, 0.0007632, 36.35790864, 0.01677731, 3.63579086, 0.07601386, -30.31065501, -0.0007632, -36.35790864, -0.01677731, -3.63579086, -0.07601386, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 97.89175659, 0.01526401, 97.89175659, 0.04579203, 68.52422961, -3565.41335446, 0.05, 2, 0, 74028, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 24.47293915, 4.587e-05, 73.41881744, 0.00013762, 244.72939147, 0.00045874, -24.47293915, -4.587e-05, -73.41881744, -0.00013762, -244.72939147, -0.00045874, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 97.89175659, 0.01526401, 97.89175659, 0.04579203, 68.52422961, -3565.41335446, 0.05, 2, 0, 74028, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 24.47293915, 4.587e-05, 73.41881744, 0.00013762, 244.72939147, 0.00045874, -24.47293915, -4.587e-05, -73.41881744, -0.00013762, -244.72939147, -0.00045874, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4070, '-orient', 0, 0, 1, 0, 1, 0)
