import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 26119670.70288791, 10883196.1262033, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 45.22918462, 0.00082591, 53.42893325, 0.00652037, 5.34289332, 0.02694684, -45.22918462, -0.00082591, -53.42893325, -0.00652037, -5.34289332, -0.02694684, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 47.4788962, 0.00082591, 56.08650249, 0.00652037, 5.60865025, 0.02694684, -47.4788962, -0.00082591, -56.08650249, -0.00652037, -5.60865025, -0.02694684, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 84.03098093, 0.01651813, 84.03098093, 0.04955439, 58.82168665, -1460.83763073, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 21.00774523, 0.00010748, 63.0232357, 0.00032244, 210.07745233, 0.00107479, -21.00774523, -0.00010748, -63.0232357, -0.00032244, -210.07745233, -0.00107479, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 84.03098093, 0.01651813, 84.03098093, 0.04955439, 58.82168665, -1460.83763073, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 21.00774523, 0.00010748, 63.0232357, 0.00032244, 210.07745233, 0.00107479, -21.00774523, -0.00010748, -63.0232357, -0.00032244, -210.07745233, -0.00107479, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.2, 0.0, 0.0)
    ops.node(121002, 4.2, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.09, 29572314.77056647, 12321797.82106936, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 122.23095589, 0.0012675, 144.91726716, 0.00867932, 14.49172672, 0.03416205, -122.23095589, -0.0012675, -144.91726716, -0.00867932, -14.49172672, -0.03416205, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 140.81632828, 0.0012675, 166.95212204, 0.00867932, 16.6952122, 0.03416205, -140.81632828, -0.0012675, -166.95212204, -0.00867932, -16.6952122, -0.03416205, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 142.29879852, 0.02535005, 142.29879852, 0.07605015, 99.60915896, -2007.26550089, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 35.57469963, 0.00011164, 106.72409889, 0.00033491, 355.7469963, 0.00111636, -35.57469963, -0.00011164, -106.72409889, -0.00033491, -355.7469963, -0.00111636, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 142.29879852, 0.02535005, 142.29879852, 0.07605015, 99.60915896, -2007.26550089, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 35.57469963, 0.00011164, 106.72409889, 0.00033491, 355.7469963, 0.00111636, -35.57469963, -0.00011164, -106.72409889, -0.00033491, -355.7469963, -0.00111636, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.4, 0.0, 0.0)
    ops.node(121003, 8.4, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.09, 29066308.54822284, 12110961.89509285, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 129.28238766, 0.00121267, 153.24345248, 0.00813561, 15.32434525, 0.0293115, -129.28238766, -0.00121267, -153.24345248, -0.00813561, -15.32434525, -0.0293115, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 136.03683794, 0.00121267, 161.24976563, 0.00813561, 16.12497656, 0.0293115, -136.03683794, -0.00121267, -161.24976563, -0.00813561, -16.12497656, -0.0293115, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 126.03840125, 0.02425336, 126.03840125, 0.07276007, 88.22688087, -1714.18014019, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 31.50960031, 0.0001006, 94.52880093, 0.0003018, 315.09600311, 0.00100601, -31.50960031, -0.0001006, -94.52880093, -0.0003018, -315.09600311, -0.00100601, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 126.03840125, 0.02425336, 126.03840125, 0.07276007, 88.22688087, -1714.18014019, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 31.50960031, 0.0001006, 94.52880093, 0.0003018, 315.09600311, 0.00100601, -31.50960031, -0.0001006, -94.52880093, -0.0003018, -315.09600311, -0.00100601, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 19.7, 0.0, 0.0)
    ops.node(121006, 19.7, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.09, 28999916.03559846, 12083298.34816602, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 130.58758328, 0.00130015, 154.78396243, 0.00929329, 15.47839624, 0.03032838, -130.58758328, -0.00130015, -154.78396243, -0.00929329, -15.47839624, -0.03032838, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 136.94707009, 0.00130015, 162.32178911, 0.00929329, 16.23217891, 0.03032838, -136.94707009, -0.00130015, -162.32178911, -0.00929329, -16.23217891, -0.03032838, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 134.14269893, 0.0260031, 134.14269893, 0.07800929, 93.89988925, -1856.53079604, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 33.53567473, 0.00010731, 100.6070242, 0.00032194, 335.35674734, 0.00107314, -33.53567473, -0.00010731, -100.6070242, -0.00032194, -335.35674734, -0.00107314, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 134.14269893, 0.0260031, 134.14269893, 0.07800929, 93.89988925, -1856.53079604, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 33.53567473, 0.00010731, 100.6070242, 0.00032194, 335.35674734, 0.00107314, -33.53567473, -0.00010731, -100.6070242, -0.00032194, -335.35674734, -0.00107314, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 23.9, 0.0, 0.0)
    ops.node(121007, 23.9, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.09, 28588677.97429515, 11911949.15595631, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 124.1875706, 0.00126266, 147.14867003, 0.00818894, 14.714867, 0.03128704, -124.1875706, -0.00126266, -147.14867003, -0.00818894, -14.714867, -0.03128704, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 144.89584533, 0.00126266, 171.68570759, 0.00818894, 17.16857076, 0.03128704, -144.89584533, -0.00126266, -171.68570759, -0.00818894, -17.16857076, -0.03128704, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 138.91935976, 0.02525317, 138.91935976, 0.07575952, 97.24355183, -1999.9842108, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 34.72983994, 0.00011273, 104.18951982, 0.0003382, 347.29839939, 0.00112734, -34.72983994, -0.00011273, -104.18951982, -0.0003382, -347.29839939, -0.00112734, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 138.91935976, 0.02525317, 138.91935976, 0.07575952, 97.24355183, -1999.9842108, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 34.72983994, 0.00011273, 104.18951982, 0.0003382, 347.29839939, 0.00112734, -34.72983994, -0.00011273, -104.18951982, -0.0003382, -347.29839939, -0.00112734, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 28.1, 0.0, 0.0)
    ops.node(121008, 28.1, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.0625, 27933934.44590719, 11639139.35246133, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 70.36085227, 0.00143106, 83.43272687, 0.00968855, 8.34327269, 0.03560567, -70.36085227, -0.00143106, -83.43272687, -0.00968855, -8.34327269, -0.03560567, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 75.9949795, 0.00143106, 90.11358112, 0.00968855, 9.01135811, 0.03560567, -75.9949795, -0.00143106, -90.11358112, -0.00968855, -9.01135811, -0.03560567, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 108.33641584, 0.02862111, 108.33641584, 0.08586332, 75.83549109, -1739.15190905, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 27.08410396, 0.00012957, 81.25231188, 0.0003887, 270.84103961, 0.00129567, -27.08410396, -0.00012957, -81.25231188, -0.0003887, -270.84103961, -0.00129567, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 108.33641584, 0.02862111, 108.33641584, 0.08586332, 75.83549109, -1739.15190905, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 27.08410396, 0.00012957, 81.25231188, 0.0003887, 270.84103961, 0.00129567, -27.08410396, -0.00012957, -81.25231188, -0.0003887, -270.84103961, -0.00129567, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 5.1, 0.0)
    ops.node(121009, 0.0, 5.1, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.1225, 29891199.07830913, 12454666.28262881, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 213.55096192, 0.00110416, 254.54180255, 0.00867619, 25.45418025, 0.03602902, -213.55096192, -0.00110416, -254.54180255, -0.00867619, -25.45418025, -0.03602902, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 213.55096192, 0.00110416, 254.54180255, 0.00867619, 25.45418025, 0.03602902, -213.55096192, -0.00110416, -254.54180255, -0.00867619, -25.45418025, -0.03602902, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 175.09611786, 0.0220832, 175.09611786, 0.06624959, 122.5672825, -2281.90561047, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 43.77402947, 9.985e-05, 131.3220884, 0.00029954, 437.74029465, 0.00099845, -43.77402947, -9.985e-05, -131.3220884, -0.00029954, -437.74029465, -0.00099845, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 175.09611786, 0.0220832, 175.09611786, 0.06624959, 122.5672825, -2281.90561047, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 43.77402947, 9.985e-05, 131.3220884, 0.00029954, 437.74029465, 0.00099845, -43.77402947, -9.985e-05, -131.3220884, -0.00029954, -437.74029465, -0.00099845, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 4.2, 5.1, 0.0)
    ops.node(121010, 4.2, 5.1, 2.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 28440848.95627252, 11850353.73178022, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 330.96945614, 0.00093746, 395.10950709, 0.01037755, 39.51095071, 0.03074644, -330.96945614, -0.00093746, -395.10950709, -0.01037755, -39.51095071, -0.03074644, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 321.77733308, 0.00093746, 384.1360014, 0.01037755, 38.41360014, 0.03074644, -321.77733308, -0.00093746, -384.1360014, -0.01037755, -38.41360014, -0.03074644, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 203.58987645, 0.01874926, 203.58987645, 0.05624777, 142.51291351, -2571.8873206, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 50.89746911, 9.342e-05, 152.69240733, 0.00028025, 508.97469111, 0.00093417, -50.89746911, -9.342e-05, -152.69240733, -0.00028025, -508.97469111, -0.00093417, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 203.58987645, 0.01874926, 203.58987645, 0.05624777, 142.51291351, -2571.8873206, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 50.89746911, 9.342e-05, 152.69240733, 0.00028025, 508.97469111, 0.00093417, -50.89746911, -9.342e-05, -152.69240733, -0.00028025, -508.97469111, -0.00093417, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.4, 5.1, 0.0)
    ops.node(121011, 8.4, 5.1, 2.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 28275730.93428167, 11781554.55595069, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 340.95092845, 0.00101156, 407.00906573, 0.01002287, 40.70090657, 0.0301104, -340.95092845, -0.00101156, -407.00906573, -0.01002287, -40.70090657, -0.0301104, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 331.86390313, 0.00101156, 396.16145871, 0.01002287, 39.61614587, 0.0301104, -331.86390313, -0.00101156, -396.16145871, -0.01002287, -39.61614587, -0.0301104, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 204.63909997, 0.02023123, 204.63909997, 0.0606937, 143.24736998, -2617.20780694, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 51.15977499, 9.445e-05, 153.47932498, 0.00028334, 511.59774992, 0.00094446, -51.15977499, -9.445e-05, -153.47932498, -0.00028334, -511.59774992, -0.00094446, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 204.63909997, 0.02023123, 204.63909997, 0.0606937, 143.24736998, -2617.20780694, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 51.15977499, 9.445e-05, 153.47932498, 0.00028334, 511.59774992, 0.00094446, -51.15977499, -9.445e-05, -153.47932498, -0.00028334, -511.59774992, -0.00094446, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 12.6, 5.1, 0.0)
    ops.node(121012, 12.6, 5.1, 2.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 29899976.45938116, 12458323.52474215, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 338.44494297, 0.00100261, 404.18246277, 0.00698334, 40.41824628, 0.02634231, -338.44494297, -0.00100261, -404.18246277, -0.00698334, -40.41824628, -0.02634231, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 321.34829401, 0.00100261, 383.76506306, 0.00698334, 38.37650631, 0.02634231, -321.34829401, -0.00100261, -383.76506306, -0.00698334, -38.37650631, -0.02634231, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 175.93706561, 0.02005221, 175.93706561, 0.06015662, 123.15594593, -1965.54474037, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 43.9842664, 7.679e-05, 131.95279921, 0.00023037, 439.84266403, 0.00076789, -43.9842664, -7.679e-05, -131.95279921, -0.00023037, -439.84266403, -0.00076789, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 175.93706561, 0.02005221, 175.93706561, 0.06015662, 123.15594593, -1965.54474037, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 43.9842664, 7.679e-05, 131.95279921, 0.00023037, 439.84266403, 0.00076789, -43.9842664, -7.679e-05, -131.95279921, -0.00023037, -439.84266403, -0.00076789, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 15.5, 5.1, 0.0)
    ops.node(121013, 15.5, 5.1, 2.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.16, 29480732.14386581, 12283638.39327742, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 318.94481627, 0.00097592, 380.99767824, 0.00722258, 38.09976782, 0.02604909, -318.94481627, -0.00097592, -380.99767824, -0.00722258, -38.09976782, -0.02604909, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 303.62038612, 0.00097592, 362.69177701, 0.00722258, 36.2691777, 0.02604909, -303.62038612, -0.00097592, -362.69177701, -0.00722258, -36.2691777, -0.02604909, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 171.58301861, 0.01951849, 171.58301861, 0.05855548, 120.10811302, -1892.17855175, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 42.89575465, 7.595e-05, 128.68726395, 0.00022786, 428.95754651, 0.00075953, -42.89575465, -7.595e-05, -128.68726395, -0.00022786, -428.95754651, -0.00075953, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 171.58301861, 0.01951849, 171.58301861, 0.05855548, 120.10811302, -1892.17855175, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 42.89575465, 7.595e-05, 128.68726395, 0.00022786, 428.95754651, 0.00075953, -42.89575465, -7.595e-05, -128.68726395, -0.00022786, -428.95754651, -0.00075953, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 19.7, 5.1, 0.0)
    ops.node(121014, 19.7, 5.1, 2.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.16, 27468781.31711004, 11445325.54879585, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 342.84641467, 0.00097626, 409.08485955, 0.00817246, 40.90848596, 0.0268398, -342.84641467, -0.00097626, -409.08485955, -0.00817246, -40.90848596, -0.0268398, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 333.0994873, 0.00097626, 397.4548111, 0.00817246, 39.74548111, 0.0268398, -333.0994873, -0.00097626, -397.4548111, -0.00817246, -39.74548111, -0.0268398, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 186.66535199, 0.01952512, 186.66535199, 0.05857535, 130.66574639, -2299.91696162, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 46.666338, 8.868e-05, 139.99901399, 0.00026605, 466.66337997, 0.00088682, -46.666338, -8.868e-05, -139.99901399, -0.00026605, -466.66337997, -0.00088682, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 186.66535199, 0.01952512, 186.66535199, 0.05857535, 130.66574639, -2299.91696162, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 46.666338, 8.868e-05, 139.99901399, 0.00026605, 466.66337997, 0.00088682, -46.666338, -8.868e-05, -139.99901399, -0.00026605, -466.66337997, -0.00088682, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 23.9, 5.1, 0.0)
    ops.node(121015, 23.9, 5.1, 2.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.16, 29411701.51323947, 12254875.63051645, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 345.48338781, 0.00099191, 412.39184368, 0.0090402, 41.23918437, 0.03099836, -345.48338781, -0.00099191, -412.39184368, -0.0090402, -41.23918437, -0.03099836, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 336.08070391, 0.00099191, 401.16817769, 0.0090402, 40.11681777, 0.03099836, -336.08070391, -0.00099191, -401.16817769, -0.0090402, -40.11681777, -0.03099836, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 203.68304791, 0.01983816, 203.68304791, 0.05951449, 142.57813354, -2454.62149893, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 50.92076198, 9.037e-05, 152.76228593, 0.00027112, 509.20761977, 0.00090374, -50.92076198, -9.037e-05, -152.76228593, -0.00027112, -509.20761977, -0.00090374, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 203.68304791, 0.01983816, 203.68304791, 0.05951449, 142.57813354, -2454.62149893, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 50.92076198, 9.037e-05, 152.76228593, 0.00027112, 509.20761977, 0.00090374, -50.92076198, -9.037e-05, -152.76228593, -0.00027112, -509.20761977, -0.00090374, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 28.1, 5.1, 0.0)
    ops.node(121016, 28.1, 5.1, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1225, 27811112.37580542, 11587963.48991892, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 202.67679968, 0.00115007, 241.53087721, 0.00926878, 24.15308772, 0.03227604, -202.67679968, -0.00115007, -241.53087721, -0.00926878, -24.15308772, -0.03227604, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 202.67679968, 0.00115007, 241.53087721, 0.00926878, 24.15308772, 0.03227604, -202.67679968, -0.00115007, -241.53087721, -0.00926878, -24.15308772, -0.03227604, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 175.0828963, 0.02300145, 175.0828963, 0.06900435, 122.55802741, -2495.49737183, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 43.77072408, 0.0001073, 131.31217223, 0.00032191, 437.70724076, 0.00107305, -43.77072408, -0.0001073, -131.31217223, -0.00032191, -437.70724076, -0.00107305, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 175.0828963, 0.02300145, 175.0828963, 0.06900435, 122.55802741, -2495.49737183, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 43.77072408, 0.0001073, 131.31217223, 0.00032191, 437.70724076, 0.00107305, -43.77072408, -0.0001073, -131.31217223, -0.00032191, -437.70724076, -0.00107305, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 10.2, 0.0)
    ops.node(121017, 0.0, 10.2, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.1225, 30777085.77421134, 12823785.73925472, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 172.74611815, 0.00100316, 205.87033628, 0.00818934, 20.58703363, 0.03766981, -172.74611815, -0.00100316, -205.87033628, -0.00818934, -20.58703363, -0.03766981, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 190.09310518, 0.00100316, 226.54362313, 0.00818934, 22.65436231, 0.03766981, -190.09310518, -0.00100316, -226.54362313, -0.00818934, -22.65436231, -0.03766981, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 176.93980409, 0.02006324, 176.93980409, 0.06018971, 123.85786287, -2242.8239708, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 44.23495102, 9.799e-05, 132.70485307, 0.00029398, 442.34951024, 0.00097992, -44.23495102, -9.799e-05, -132.70485307, -0.00029398, -442.34951024, -0.00097992, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 176.93980409, 0.02006324, 176.93980409, 0.06018971, 123.85786287, -2242.8239708, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 44.23495102, 9.799e-05, 132.70485307, 0.00029398, 442.34951024, 0.00097992, -44.23495102, -9.799e-05, -132.70485307, -0.00029398, -442.34951024, -0.00097992, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 4.2, 10.2, 0.0)
    ops.node(121018, 4.2, 10.2, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.16, 31267157.87698254, 13027982.44874272, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 303.35852222, 0.00094464, 361.73681052, 0.00960263, 36.17368105, 0.0381384, -303.35852222, -0.00094464, -361.73681052, -0.00960263, -36.17368105, -0.0381384, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 312.95324282, 0.00094464, 373.17793834, 0.00960263, 37.31779383, 0.0381384, -312.95324282, -0.00094464, -373.17793834, -0.00960263, -37.31779383, -0.0381384, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 231.76207343, 0.01889281, 231.76207343, 0.05667842, 162.2334514, -2903.68066924, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 57.94051836, 9.673e-05, 173.82155507, 0.00029019, 579.40518358, 0.00096731, -57.94051836, -9.673e-05, -173.82155507, -0.00029019, -579.40518358, -0.00096731, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 231.76207343, 0.01889281, 231.76207343, 0.05667842, 162.2334514, -2903.68066924, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 57.94051836, 9.673e-05, 173.82155507, 0.00029019, 579.40518358, 0.00096731, -57.94051836, -9.673e-05, -173.82155507, -0.00029019, -579.40518358, -0.00096731, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 8.4, 10.2, 0.0)
    ops.node(121019, 8.4, 10.2, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.16, 29326258.13271105, 12219274.22196294, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 308.33784066, 0.00097392, 368.36527119, 0.00970112, 36.83652712, 0.03504639, -308.33784066, -0.00097392, -368.36527119, -0.00970112, -36.83652712, -0.03504639, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 318.34858024, 0.00097392, 380.32490868, 0.00970112, 38.03249087, 0.03504639, -318.34858024, -0.00097392, -380.32490868, -0.00970112, -38.03249087, -0.03504639, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 220.7216165, 0.01947835, 220.7216165, 0.05843504, 154.50513155, -2886.90228838, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 55.18040412, 9.822e-05, 165.54121237, 0.00029466, 551.80404124, 0.0009822, -55.18040412, -9.822e-05, -165.54121237, -0.00029466, -551.80404124, -0.0009822, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 220.7216165, 0.01947835, 220.7216165, 0.05843504, 154.50513155, -2886.90228838, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 55.18040412, 9.822e-05, 165.54121237, 0.00029466, 551.80404124, 0.0009822, -55.18040412, -9.822e-05, -165.54121237, -0.00029466, -551.80404124, -0.0009822, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 12.6, 10.2, 0.0)
    ops.node(121020, 12.6, 10.2, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.1225, 31207483.07457853, 13003117.94774106, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 183.08164213, 0.00103764, 218.03868468, 0.00956206, 21.80386847, 0.03965072, -183.08164213, -0.00103764, -218.03868468, -0.00956206, -21.80386847, -0.03965072, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 190.3229461, 0.00103764, 226.66262083, 0.00956206, 22.66626208, 0.03965072, -190.3229461, -0.00103764, -226.66262083, -0.00956206, -22.66626208, -0.03965072, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 185.89983815, 0.0207528, 185.89983815, 0.0622584, 130.12988671, -2420.7847987, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 46.47495954, 0.00010153, 139.42487862, 0.0003046, 464.74959538, 0.00101535, -46.47495954, -0.00010153, -139.42487862, -0.0003046, -464.74959538, -0.00101535, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 185.89983815, 0.0207528, 185.89983815, 0.0622584, 130.12988671, -2420.7847987, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 46.47495954, 0.00010153, 139.42487862, 0.0003046, 464.74959538, 0.00101535, -46.47495954, -0.00010153, -139.42487862, -0.0003046, -464.74959538, -0.00101535, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 15.5, 10.2, 0.0)
    ops.node(121021, 15.5, 10.2, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.1225, 26974783.30074484, 11239493.04197701, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 193.34587225, 0.00105333, 230.32767437, 0.00784537, 23.03276744, 0.0292923, -193.34587225, -0.00105333, -230.32767437, -0.00784537, -23.03276744, -0.0292923, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 202.58246784, 0.00105333, 241.33097926, 0.00784537, 24.13309793, 0.0292923, -202.58246784, -0.00105333, -241.33097926, -0.00784537, -24.13309793, -0.0292923, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 161.71089468, 0.02106666, 161.71089468, 0.06319998, 113.19762628, -2246.35969883, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 40.42772367, 0.00010218, 121.28317101, 0.00030655, 404.27723671, 0.00102182, -40.42772367, -0.00010218, -121.28317101, -0.00030655, -404.27723671, -0.00102182, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 161.71089468, 0.02106666, 161.71089468, 0.06319998, 113.19762628, -2246.35969883, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 40.42772367, 0.00010218, 121.28317101, 0.00030655, 404.27723671, 0.00102182, -40.42772367, -0.00010218, -121.28317101, -0.00030655, -404.27723671, -0.00102182, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 19.7, 10.2, 0.0)
    ops.node(121022, 19.7, 10.2, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.16, 29374857.33694636, 12239523.89039432, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 302.34615518, 0.00096433, 361.19908423, 0.00845614, 36.11990842, 0.03388756, -302.34615518, -0.00096433, -361.19908423, -0.00845614, -36.11990842, -0.03388756, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 311.95229022, 0.00096433, 372.67509317, 0.00845614, 37.26750932, 0.03388756, -311.95229022, -0.00096433, -372.67509317, -0.00845614, -37.26750932, -0.03388756, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 214.10321919, 0.01928661, 214.10321919, 0.05785982, 149.87225343, -2714.50143807, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 53.5258048, 9.512e-05, 160.57741439, 0.00028535, 535.25804798, 0.00095117, -53.5258048, -9.512e-05, -160.57741439, -0.00028535, -535.25804798, -0.00095117, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 214.10321919, 0.01928661, 214.10321919, 0.05785982, 149.87225343, -2714.50143807, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 53.5258048, 9.512e-05, 160.57741439, 0.00028535, 535.25804798, 0.00095117, -53.5258048, -9.512e-05, -160.57741439, -0.00028535, -535.25804798, -0.00095117, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 23.9, 10.2, 0.0)
    ops.node(121023, 23.9, 10.2, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.16, 26806364.07744209, 11169318.36560087, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 305.11079231, 0.00097247, 364.19744412, 0.00735357, 36.41974441, 0.02779085, -305.11079231, -0.00097247, -364.19744412, -0.00735357, -36.41974441, -0.02779085, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 315.39116512, 0.00097247, 376.46867672, 0.00735357, 37.64686767, 0.02779085, -315.39116512, -0.00097247, -376.46867672, -0.00735357, -37.64686767, -0.02779085, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 196.49891834, 0.0194495, 196.49891834, 0.05834849, 137.54924284, -2609.78112317, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 49.12472958, 9.566e-05, 147.37418875, 0.00028698, 491.24729585, 0.00095661, -49.12472958, -9.566e-05, -147.37418875, -0.00028698, -491.24729585, -0.00095661, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 196.49891834, 0.0194495, 196.49891834, 0.05834849, 137.54924284, -2609.78112317, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 49.12472958, 9.566e-05, 147.37418875, 0.00028698, 491.24729585, 0.00095661, -49.12472958, -9.566e-05, -147.37418875, -0.00028698, -491.24729585, -0.00095661, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 28.1, 10.2, 0.0)
    ops.node(121024, 28.1, 10.2, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.1225, 29034381.50609666, 12097658.96087361, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 171.81325915, 0.00106457, 204.97554026, 0.00873258, 20.49755403, 0.03486766, -171.81325915, -0.00106457, -204.97554026, -0.00873258, -20.49755403, -0.03486766, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 188.03465775, 0.00106457, 224.32788803, 0.00873258, 22.4327888, 0.03486766, -188.03465775, -0.00106457, -224.32788803, -0.00873258, -22.4327888, -0.03486766, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 172.37701767, 0.02129137, 172.37701767, 0.0638741, 120.66391237, -2307.99933798, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 43.09425442, 0.0001012, 129.28276326, 0.00030359, 430.94254419, 0.00101195, -43.09425442, -0.0001012, -129.28276326, -0.00030359, -430.94254419, -0.00101195, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 172.37701767, 0.02129137, 172.37701767, 0.0638741, 120.66391237, -2307.99933798, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 43.09425442, 0.0001012, 129.28276326, 0.00030359, 430.94254419, 0.00101195, -43.09425442, -0.0001012, -129.28276326, -0.00030359, -430.94254419, -0.00101195, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170025, 0.0, 15.3, 0.0)
    ops.node(121025, 0.0, 15.3, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 25, 170025, 121025, 0.0625, 27146703.3221064, 11311126.384211, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20025, 66.53291926, 0.0014702, 78.79727904, 0.00954178, 7.8797279, 0.03315573, -66.53291926, -0.0014702, -78.79727904, -0.00954178, -7.8797279, -0.03315573, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10025, 70.99338609, 0.0014702, 84.07996697, 0.00954178, 8.4079967, 0.03315573, -70.99338609, -0.0014702, -84.07996697, -0.00954178, -8.4079967, -0.03315573, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20025, 25, 0.0, 107.03702662, 0.02940398, 107.03702662, 0.08821195, 74.92591863, -1749.71094607, 0.05, 2, 0, 70025, 21025, 2, 3)
    ops.uniaxialMaterial('LimitState', 40025, 26.75925665, 0.00013172, 80.27776996, 0.00039517, 267.59256654, 0.00131725, -26.75925665, -0.00013172, -80.27776996, -0.00039517, -267.59256654, -0.00131725, 0.4, 0.3, 0.003, 0.0, 0.0, 20025, 2)
    ops.limitCurve('ThreePoint', 10025, 25, 0.0, 107.03702662, 0.02940398, 107.03702662, 0.08821195, 74.92591863, -1749.71094607, 0.05, 2, 0, 70025, 21025, 1, 3)
    ops.uniaxialMaterial('LimitState', 30025, 26.75925665, 0.00013172, 80.27776996, 0.00039517, 267.59256654, 0.00131725, -26.75925665, -0.00013172, -80.27776996, -0.00039517, -267.59256654, -0.00131725, 0.4, 0.3, 0.003, 0.0, 0.0, 10025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 25, 99999, 'P', 40025, 'Vy', 30025, 'Vz', 20025, 'My', 10025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170025, 70025, 170025, 25, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121025, 121025, 21025, 25, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170026, 4.2, 15.3, 0.0)
    ops.node(121026, 4.2, 15.3, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 26, 170026, 121026, 0.09, 27411289.06153249, 11421370.4423052, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20026, 137.97188177, 0.00131156, 163.21761187, 0.00908016, 16.32176119, 0.0292366, -137.97188177, -0.00131156, -163.21761187, -0.00908016, -16.32176119, -0.0292366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10026, 151.50548938, 0.00131156, 179.22756321, 0.00908016, 17.92275632, 0.0292366, -151.50548938, -0.00131156, -179.22756321, -0.00908016, -17.92275632, -0.0292366, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20026, 26, 0.0, 141.54781473, 0.02623124, 141.54781473, 0.07869373, 99.08347031, -2154.27078113, 0.05, 2, 0, 70026, 21026, 2, 3)
    ops.uniaxialMaterial('LimitState', 40026, 35.38695368, 0.0001198, 106.16086105, 0.0003594, 353.86953682, 0.00119801, -35.38695368, -0.0001198, -106.16086105, -0.0003594, -353.86953682, -0.00119801, 0.4, 0.3, 0.003, 0.0, 0.0, 20026, 2)
    ops.limitCurve('ThreePoint', 10026, 26, 0.0, 141.54781473, 0.02623124, 141.54781473, 0.07869373, 99.08347031, -2154.27078113, 0.05, 2, 0, 70026, 21026, 1, 3)
    ops.uniaxialMaterial('LimitState', 30026, 35.38695368, 0.0001198, 106.16086105, 0.0003594, 353.86953682, 0.00119801, -35.38695368, -0.0001198, -106.16086105, -0.0003594, -353.86953682, -0.00119801, 0.4, 0.3, 0.003, 0.0, 0.0, 10026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 26, 99999, 'P', 40026, 'Vy', 30026, 'Vz', 20026, 'My', 10026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170026, 70026, 170026, 26, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121026, 121026, 21026, 26, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170027, 8.4, 15.3, 0.0)
    ops.node(121027, 8.4, 15.3, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 27, 170027, 121027, 0.09, 29786223.56417813, 12410926.48507422, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20027, 139.84386355, 0.00124885, 165.8161786, 0.00940175, 16.58161786, 0.03543522, -139.84386355, -0.00124885, -165.8161786, -0.00940175, -16.58161786, -0.03543522, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10027, 154.08977443, 0.00124885, 182.70789228, 0.00940175, 18.27078923, 0.03543522, -154.08977443, -0.00124885, -182.70789228, -0.00940175, -18.27078923, -0.03543522, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20027, 27, 0.0, 149.07545492, 0.02497695, 149.07545492, 0.07493084, 104.35281845, -2157.79368214, 0.05, 2, 0, 70027, 21027, 2, 3)
    ops.uniaxialMaterial('LimitState', 40027, 37.26886373, 0.00011611, 111.80659119, 0.00034834, 372.68863731, 0.00116112, -37.26886373, -0.00011611, -111.80659119, -0.00034834, -372.68863731, -0.00116112, 0.4, 0.3, 0.003, 0.0, 0.0, 20027, 2)
    ops.limitCurve('ThreePoint', 10027, 27, 0.0, 149.07545492, 0.02497695, 149.07545492, 0.07493084, 104.35281845, -2157.79368214, 0.05, 2, 0, 70027, 21027, 1, 3)
    ops.uniaxialMaterial('LimitState', 30027, 37.26886373, 0.00011611, 111.80659119, 0.00034834, 372.68863731, 0.00116112, -37.26886373, -0.00011611, -111.80659119, -0.00034834, -372.68863731, -0.00116112, 0.4, 0.3, 0.003, 0.0, 0.0, 10027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 27, 99999, 'P', 40027, 'Vy', 30027, 'Vz', 20027, 'My', 10027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170027, 70027, 170027, 27, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121027, 121027, 21027, 27, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170028, 12.6, 15.3, 0.0)
    ops.node(121028, 12.6, 15.3, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 28, 170028, 121028, 0.0625, 28056698.06312323, 11690290.85963468, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20028, 66.84392286, 0.00092295, 78.62300982, 0.00749513, 7.86230098, 0.02530771, -66.84392286, -0.00092295, -78.62300982, -0.00749513, -7.86230098, -0.02530771, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10028, 72.1636735, 0.00092295, 84.88019505, 0.00749513, 8.48801951, 0.02530771, -72.1636735, -0.00092295, -84.88019505, -0.00749513, -8.48801951, -0.02530771, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20028, 28, 0.0, 66.55006468, 0.01845896, 66.55006468, 0.05537687, 46.58504528, -1416.93182474, 0.05, 2, 0, 70028, 21028, 2, 3)
    ops.uniaxialMaterial('LimitState', 40028, 16.63751617, 7.924e-05, 49.91254851, 0.00023773, 166.3751617, 0.00079243, -16.63751617, -7.924e-05, -49.91254851, -0.00023773, -166.3751617, -0.00079243, 0.4, 0.3, 0.003, 0.0, 0.0, 20028, 2)
    ops.limitCurve('ThreePoint', 10028, 28, 0.0, 66.55006468, 0.01845896, 66.55006468, 0.05537687, 46.58504528, -1416.93182474, 0.05, 2, 0, 70028, 21028, 1, 3)
    ops.uniaxialMaterial('LimitState', 30028, 16.63751617, 7.924e-05, 49.91254851, 0.00023773, 166.3751617, 0.00079243, -16.63751617, -7.924e-05, -49.91254851, -0.00023773, -166.3751617, -0.00079243, 0.4, 0.3, 0.003, 0.0, 0.0, 10028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 28, 99999, 'P', 40028, 'Vy', 30028, 'Vz', 20028, 'My', 10028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170028, 70028, 170028, 28, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121028, 121028, 21028, 28, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170029, 15.5, 15.3, 0.0)
    ops.node(121029, 15.5, 15.3, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 29, 170029, 121029, 0.0625, 27242382.07450357, 11350992.53104316, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20029, 57.45845131, 0.00083732, 67.44159702, 0.00895281, 6.7441597, 0.02472188, -57.45845131, -0.00083732, -67.44159702, -0.00895281, -6.7441597, -0.02472188, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10029, 60.98887809, 0.00083732, 71.58541947, 0.00895281, 7.15854195, 0.02472188, -60.98887809, -0.00083732, -71.58541947, -0.00895281, -7.15854195, -0.02472188, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20029, 29, 0.0, 102.629888, 0.01674636, 102.629888, 0.05023908, 71.8409216, -1641.06271967, 0.05, 2, 0, 70029, 21029, 2, 3)
    ops.uniaxialMaterial('LimitState', 40029, 25.657472, 0.00012586, 76.972416, 0.00037757, 256.57472, 0.00125858, -25.657472, -0.00012586, -76.972416, -0.00037757, -256.57472, -0.00125858, 0.4, 0.3, 0.003, 0.0, 0.0, 20029, 2)
    ops.limitCurve('ThreePoint', 10029, 29, 0.0, 102.629888, 0.01674636, 102.629888, 0.05023908, 71.8409216, -1641.06271967, 0.05, 2, 0, 70029, 21029, 1, 3)
    ops.uniaxialMaterial('LimitState', 30029, 25.657472, 0.00012586, 76.972416, 0.00037757, 256.57472, 0.00125858, -25.657472, -0.00012586, -76.972416, -0.00037757, -256.57472, -0.00125858, 0.4, 0.3, 0.003, 0.0, 0.0, 10029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 29, 99999, 'P', 40029, 'Vy', 30029, 'Vz', 20029, 'My', 10029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170029, 70029, 170029, 29, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121029, 121029, 21029, 29, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170030, 19.7, 15.3, 0.0)
    ops.node(121030, 19.7, 15.3, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 30, 170030, 121030, 0.09, 28024539.16208893, 11676891.31753705, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20030, 133.13411649, 0.00122913, 157.65537776, 0.00812661, 15.76553778, 0.02985713, -133.13411649, -0.00122913, -157.65537776, -0.00812661, -15.76553778, -0.02985713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10030, 146.14324492, 0.00122913, 173.06058802, 0.00812661, 17.3060588, 0.02985713, -146.14324492, -0.00122913, -173.06058802, -0.00812661, -17.3060588, -0.02985713, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20030, 30, 0.0, 137.34574146, 0.02458258, 137.34574146, 0.07374773, 96.14201902, -2004.36381112, 0.05, 2, 0, 70030, 21030, 2, 3)
    ops.uniaxialMaterial('LimitState', 40030, 34.33643537, 0.0001137, 103.0093061, 0.0003411, 343.36435366, 0.00113701, -34.33643537, -0.0001137, -103.0093061, -0.0003411, -343.36435366, -0.00113701, 0.4, 0.3, 0.003, 0.0, 0.0, 20030, 2)
    ops.limitCurve('ThreePoint', 10030, 30, 0.0, 137.34574146, 0.02458258, 137.34574146, 0.07374773, 96.14201902, -2004.36381112, 0.05, 2, 0, 70030, 21030, 1, 3)
    ops.uniaxialMaterial('LimitState', 30030, 34.33643537, 0.0001137, 103.0093061, 0.0003411, 343.36435366, 0.00113701, -34.33643537, -0.0001137, -103.0093061, -0.0003411, -343.36435366, -0.00113701, 0.4, 0.3, 0.003, 0.0, 0.0, 10030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 30, 99999, 'P', 40030, 'Vy', 30030, 'Vz', 20030, 'My', 10030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170030, 70030, 170030, 30, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121030, 121030, 21030, 30, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170031, 23.9, 15.3, 0.0)
    ops.node(121031, 23.9, 15.3, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 31, 170031, 121031, 0.09, 28680077.64586187, 11950032.35244245, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20031, 132.44786467, 0.00134194, 156.96064457, 0.00877722, 15.69606446, 0.03215045, -132.44786467, -0.00134194, -156.96064457, -0.00877722, -15.69606446, -0.03215045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10031, 143.1213545, 0.00134194, 169.60952983, 0.00877722, 16.96095298, 0.03215045, -143.1213545, -0.00134194, -169.60952983, -0.00877722, -16.96095298, -0.03215045, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20031, 31, 0.0, 142.97733033, 0.02683881, 142.97733033, 0.08051642, 100.08413123, -2092.28067088, 0.05, 2, 0, 70031, 21031, 2, 3)
    ops.uniaxialMaterial('LimitState', 40031, 35.74433258, 0.00011566, 107.23299775, 0.00034697, 357.44332583, 0.00115658, -35.74433258, -0.00011566, -107.23299775, -0.00034697, -357.44332583, -0.00115658, 0.4, 0.3, 0.003, 0.0, 0.0, 20031, 2)
    ops.limitCurve('ThreePoint', 10031, 31, 0.0, 142.97733033, 0.02683881, 142.97733033, 0.08051642, 100.08413123, -2092.28067088, 0.05, 2, 0, 70031, 21031, 1, 3)
    ops.uniaxialMaterial('LimitState', 30031, 35.74433258, 0.00011566, 107.23299775, 0.00034697, 357.44332583, 0.00115658, -35.74433258, -0.00011566, -107.23299775, -0.00034697, -357.44332583, -0.00115658, 0.4, 0.3, 0.003, 0.0, 0.0, 10031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 31, 99999, 'P', 40031, 'Vy', 30031, 'Vz', 20031, 'My', 10031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170031, 70031, 170031, 31, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121031, 121031, 21031, 31, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170032, 28.1, 15.3, 0.0)
    ops.node(121032, 28.1, 15.3, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 32, 170032, 121032, 0.0625, 29209679.05183822, 12170699.60493259, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20032, 68.77874189, 0.00149186, 81.64603932, 0.00995369, 8.16460393, 0.03954763, -68.77874189, -0.00149186, -81.64603932, -0.00995369, -8.16460393, -0.03954763, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10032, 73.43027856, 0.00149186, 87.16779699, 0.00995369, 8.7167797, 0.03954763, -73.43027856, -0.00149186, -87.16779699, -0.00995369, -8.7167797, -0.03954763, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20032, 32, 0.0, 109.72274216, 0.02983729, 109.72274216, 0.08951187, 76.80591951, -1702.68182256, 0.05, 2, 0, 70032, 21032, 2, 3)
    ops.uniaxialMaterial('LimitState', 40032, 27.43068554, 0.00012549, 82.29205662, 0.00037648, 274.3068554, 0.00125493, -27.43068554, -0.00012549, -82.29205662, -0.00037648, -274.3068554, -0.00125493, 0.4, 0.3, 0.003, 0.0, 0.0, 20032, 2)
    ops.limitCurve('ThreePoint', 10032, 32, 0.0, 109.72274216, 0.02983729, 109.72274216, 0.08951187, 76.80591951, -1702.68182256, 0.05, 2, 0, 70032, 21032, 1, 3)
    ops.uniaxialMaterial('LimitState', 30032, 27.43068554, 0.00012549, 82.29205662, 0.00037648, 274.3068554, 0.00125493, -27.43068554, -0.00012549, -82.29205662, -0.00037648, -274.3068554, -0.00125493, 0.4, 0.3, 0.003, 0.0, 0.0, 10032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 32, 99999, 'P', 40032, 'Vy', 30032, 'Vz', 20032, 'My', 10032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170032, 70032, 170032, 32, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121032, 121032, 21032, 32, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.15)
    ops.node(122001, 0.0, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 27916710.31017665, 11631962.62924027, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 60.84592997, 0.00140178, 72.77474404, 0.00925981, 7.2774744, 0.04272786, -60.84592997, -0.00140178, -72.77474404, -0.00925981, -7.2774744, -0.04272786, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 65.94773862, 0.00140178, 78.87675972, 0.00925981, 7.88767597, 0.04272786, -65.94773862, -0.00140178, -78.87675972, -0.00925981, -7.88767597, -0.04272786, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 93.18605747, 0.02803556, 93.18605747, 0.08410667, 65.23024023, -1413.31221844, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 23.29651437, 0.00011152, 69.8895431, 0.00033455, 232.96514366, 0.00111516, -23.29651437, -0.00011152, -69.8895431, -0.00033455, -232.96514366, -0.00111516, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 93.18605747, 0.02803556, 93.18605747, 0.08410667, 65.23024023, -1413.31221844, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 23.29651437, 0.00011152, 69.8895431, 0.00033455, 232.96514366, 0.00111516, -23.29651437, -0.00011152, -69.8895431, -0.00033455, -232.96514366, -0.00111516, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.2, 0.0, 3.1)
    ops.node(122002, 4.2, 0.0, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.09, 29991765.57221067, 12496568.98842111, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 107.77714265, 0.00115823, 128.6731205, 0.00920242, 12.86731205, 0.04171617, -107.77714265, -0.00115823, -128.6731205, -0.00920242, -12.86731205, -0.04171617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 127.81245181, 0.00115823, 152.59290244, 0.00920242, 15.25929024, 0.04171617, -127.81245181, -0.00115823, -152.59290244, -0.00920242, -15.25929024, -0.04171617, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 136.56603166, 0.02316468, 136.56603166, 0.06949405, 95.59622216, -1895.41711238, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 34.14150791, 0.00010564, 102.42452374, 0.00031692, 341.41507915, 0.0010564, -34.14150791, -0.00010564, -102.42452374, -0.00031692, -341.41507915, -0.0010564, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 136.56603166, 0.02316468, 136.56603166, 0.06949405, 95.59622216, -1895.41711238, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 34.14150791, 0.00010564, 102.42452374, 0.00031692, 341.41507915, 0.0010564, -34.14150791, -0.00010564, -102.42452374, -0.00031692, -341.41507915, -0.0010564, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.4, 0.0, 3.1)
    ops.node(122003, 8.4, 0.0, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.09, 29277024.7654951, 12198760.31895629, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 112.49793508, 0.00117327, 134.36551758, 0.01068419, 13.43655176, 0.03770901, -112.49793508, -0.00117327, -134.36551758, -0.01068419, -13.43655176, -0.03770901, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 118.73836573, 0.00117327, 141.8189761, 0.01068419, 14.18189761, 0.03770901, -118.73836573, -0.00117327, -141.8189761, -0.01068419, -14.18189761, -0.03770901, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 128.43242998, 0.02346546, 128.43242998, 0.07039637, 89.90270099, -1735.0094723, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 32.1081075, 0.00010177, 96.32432249, 0.00030532, 321.08107496, 0.00101774, -32.1081075, -0.00010177, -96.32432249, -0.00030532, -321.08107496, -0.00101774, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 128.43242998, 0.02346546, 128.43242998, 0.07039637, 89.90270099, -1735.0094723, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 32.1081075, 0.00010177, 96.32432249, 0.00030532, 321.08107496, 0.00101774, -32.1081075, -0.00010177, -96.32432249, -0.00030532, -321.08107496, -0.00101774, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 19.7, 0.0, 3.1)
    ops.node(122006, 19.7, 0.0, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.09, 29374815.93712174, 12239506.64046739, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 111.22455884, 0.00121879, 132.83925346, 0.00922681, 13.28392535, 0.03643987, -111.22455884, -0.00121879, -132.83925346, -0.00922681, -13.28392535, -0.03643987, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 116.90986581, 0.00121879, 139.62940792, 0.00922681, 13.96294079, 0.03643987, -116.90986581, -0.00121879, -139.62940792, -0.00922681, -13.96294079, -0.03643987, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 123.73446108, 0.02437585, 123.73446108, 0.07312755, 86.61412276, -1607.00610752, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 30.93361527, 9.772e-05, 92.80084581, 0.00029317, 309.3361527, 0.00097725, -30.93361527, -9.772e-05, -92.80084581, -0.00029317, -309.3361527, -0.00097725, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 123.73446108, 0.02437585, 123.73446108, 0.07312755, 86.61412276, -1607.00610752, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 30.93361527, 9.772e-05, 92.80084581, 0.00029317, 309.3361527, 0.00097725, -30.93361527, -9.772e-05, -92.80084581, -0.00029317, -309.3361527, -0.00097725, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 23.9, 0.0, 3.1)
    ops.node(122007, 23.9, 0.0, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.09, 28849840.55794065, 12020766.89914194, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 110.33627427, 0.00124041, 131.79830931, 0.01023744, 13.17983093, 0.04025, -110.33627427, -0.00124041, -131.79830931, -0.01023744, -13.17983093, -0.04025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 130.3195653, 0.00124041, 155.6686456, 0.01023744, 15.56686456, 0.04025, -130.3195653, -0.00124041, -155.6686456, -0.01023744, -15.56686456, -0.04025, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 137.8180727, 0.02480817, 137.8180727, 0.0744245, 96.47265089, -2024.72171646, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 34.45451818, 0.00011083, 103.36355453, 0.00033248, 344.54518175, 0.00110828, -34.45451818, -0.00011083, -103.36355453, -0.00033248, -344.54518175, -0.00110828, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 137.8180727, 0.02480817, 137.8180727, 0.0744245, 96.47265089, -2024.72171646, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 34.45451818, 0.00011083, 103.36355453, 0.00033248, 344.54518175, 0.00110828, -34.45451818, -0.00011083, -103.36355453, -0.00033248, -344.54518175, -0.00110828, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 28.1, 0.0, 3.15)
    ops.node(122008, 28.1, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.0625, 30830255.90546865, 12845939.96061194, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 58.74454889, 0.00136184, 70.14690617, 0.01120494, 7.01469062, 0.05189172, -58.74454889, -0.00136184, -70.14690617, -0.01120494, -7.01469062, -0.05189172, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 63.10476484, 0.00136184, 75.35344303, 0.01120494, 7.5353443, 0.05189172, -63.10476484, -0.00136184, -75.35344303, -0.01120494, -7.5353443, -0.05189172, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 108.37911824, 0.02723677, 108.37911824, 0.0817103, 75.86538277, -1687.9763761, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 27.09477956, 0.00011744, 81.28433868, 0.00035232, 270.94779559, 0.00117441, -27.09477956, -0.00011744, -81.28433868, -0.00035232, -270.94779559, -0.00117441, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 108.37911824, 0.02723677, 108.37911824, 0.0817103, 75.86538277, -1687.9763761, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 27.09477956, 0.00011744, 81.28433868, 0.00035232, 270.94779559, 0.00117441, -27.09477956, -0.00011744, -81.28433868, -0.00035232, -270.94779559, -0.00117441, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 5.1, 3.15)
    ops.node(122009, 0.0, 5.1, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.1225, 29709425.23400282, 12378927.18083451, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 122.96780938, 0.00099196, 147.43986928, 0.00891498, 14.74398693, 0.04102668, -122.96780938, -0.00099196, -147.43986928, -0.00891498, -14.74398693, -0.04102668, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 137.4356691, 0.00099196, 164.78700554, 0.00891498, 16.47870055, 0.04102668, -137.4356691, -0.00099196, -164.78700554, -0.00891498, -16.47870055, -0.04102668, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 165.10566767, 0.01983922, 165.10566767, 0.05951767, 115.57396737, -2150.40166704, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 41.27641692, 9.472e-05, 123.82925075, 0.00028417, 412.76416918, 0.00094724, -41.27641692, -9.472e-05, -123.82925075, -0.00028417, -412.76416918, -0.00094724, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 165.10566767, 0.01983922, 165.10566767, 0.05951767, 115.57396737, -2150.40166704, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 41.27641692, 9.472e-05, 123.82925075, 0.00028417, 412.76416918, 0.00094724, -41.27641692, -9.472e-05, -123.82925075, -0.00028417, -412.76416918, -0.00094724, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 4.2, 5.1, 3.125)
    ops.node(122010, 4.2, 5.1, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 27667178.2657157, 11527990.94404821, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 217.78430463, 0.00091961, 261.5741796, 0.00829995, 26.15741796, 0.03133483, -217.78430463, -0.00091961, -261.5741796, -0.00829995, -26.15741796, -0.03133483, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 198.67362303, 0.00091961, 238.62091458, 0.00829995, 23.86209146, 0.03133483, -198.67362303, -0.00091961, -238.62091458, -0.00829995, -23.86209146, -0.03133483, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 177.58327042, 0.01839213, 177.58327042, 0.05517639, 124.30828929, -2093.4106574, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 44.39581761, 8.376e-05, 133.18745282, 0.00025129, 443.95817605, 0.00083762, -44.39581761, -8.376e-05, -133.18745282, -0.00025129, -443.95817605, -0.00083762, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 177.58327042, 0.01839213, 177.58327042, 0.05517639, 124.30828929, -2093.4106574, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 44.39581761, 8.376e-05, 133.18745282, 0.00025129, 443.95817605, 0.00083762, -44.39581761, -8.376e-05, -133.18745282, -0.00025129, -443.95817605, -0.00083762, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.4, 5.1, 3.125)
    ops.node(122011, 8.4, 5.1, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 30293828.9700036, 12622428.7375015, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 212.51072156, 0.00089114, 254.72724385, 0.00901499, 25.47272438, 0.03586032, -212.51072156, -0.00089114, -254.72724385, -0.00901499, -25.47272438, -0.03586032, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 194.78534986, 0.00089114, 233.48062135, 0.00901499, 23.34806213, 0.03586032, -194.78534986, -0.00089114, -233.48062135, -0.00901499, -23.34806213, -0.03586032, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 195.4767392, 0.01782275, 195.4767392, 0.05346826, 136.83371744, -2206.59705991, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 48.8691848, 8.421e-05, 146.6075544, 0.00025262, 488.691848, 0.00084208, -48.8691848, -8.421e-05, -146.6075544, -0.00025262, -488.691848, -0.00084208, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 195.4767392, 0.01782275, 195.4767392, 0.05346826, 136.83371744, -2206.59705991, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 48.8691848, 8.421e-05, 146.6075544, 0.00025262, 488.691848, 0.00084208, -48.8691848, -8.421e-05, -146.6075544, -0.00025262, -488.691848, -0.00084208, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 12.6, 5.1, 3.125)
    ops.node(122012, 12.6, 5.1, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 32711214.44554438, 13629672.68564349, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 210.51065029, 0.00088945, 251.26922277, 0.00720488, 25.12692228, 0.03225249, -210.51065029, -0.00088945, -251.26922277, -0.00720488, -25.12692228, -0.03225249, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 210.51065029, 0.00088945, 251.26922277, 0.00720488, 25.12692228, 0.03225249, -210.51065029, -0.00088945, -251.26922277, -0.00720488, -25.12692228, -0.03225249, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 177.66858803, 0.01778907, 177.66858803, 0.05336722, 124.36801162, -1663.20114184, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 44.41714701, 7.088e-05, 133.25144102, 0.00021264, 444.17147007, 0.0007088, -44.41714701, -7.088e-05, -133.25144102, -0.00021264, -444.17147007, -0.0007088, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 177.66858803, 0.01778907, 177.66858803, 0.05336722, 124.36801162, -1663.20114184, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 44.41714701, 7.088e-05, 133.25144102, 0.00021264, 444.17147007, 0.0007088, -44.41714701, -7.088e-05, -133.25144102, -0.00021264, -444.17147007, -0.0007088, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 15.5, 5.1, 3.125)
    ops.node(122013, 15.5, 5.1, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.16, 29351725.96147385, 12229885.81728077, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 208.13638979, 0.0009628, 249.94070542, 0.0074928, 24.99407054, 0.02927489, -208.13638979, -0.0009628, -249.94070542, -0.0074928, -24.99407054, -0.02927489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 208.13638979, 0.0009628, 249.94070542, 0.0074928, 24.99407054, 0.02927489, -208.13638979, -0.0009628, -249.94070542, -0.0074928, -24.99407054, -0.02927489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 168.45699168, 0.01925609, 168.45699168, 0.05776827, 117.91989418, -1712.30194003, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 42.11424792, 7.49e-05, 126.34274376, 0.00022469, 421.14247921, 0.00074897, -42.11424792, -7.49e-05, -126.34274376, -0.00022469, -421.14247921, -0.00074897, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 168.45699168, 0.01925609, 168.45699168, 0.05776827, 117.91989418, -1712.30194003, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 42.11424792, 7.49e-05, 126.34274376, 0.00022469, 421.14247921, 0.00074897, -42.11424792, -7.49e-05, -126.34274376, -0.00022469, -421.14247921, -0.00074897, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 19.7, 5.1, 3.125)
    ops.node(122014, 19.7, 5.1, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.16, 31588365.65630184, 13161819.0234591, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 218.86040315, 0.00087297, 261.76014944, 0.008106, 26.17601494, 0.03651061, -218.86040315, -0.00087297, -261.76014944, -0.008106, -26.17601494, -0.03651061, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 199.53090285, 0.00087297, 238.64179265, 0.008106, 23.86417927, 0.03651061, -199.53090285, -0.00087297, -238.64179265, -0.008106, -23.86417927, -0.03651061, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 194.28390481, 0.01745946, 194.28390481, 0.05237837, 135.99873337, -2010.77691701, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 48.5709762, 8.026e-05, 145.71292861, 0.00024079, 485.70976204, 0.00080264, -48.5709762, -8.026e-05, -145.71292861, -0.00024079, -485.70976204, -0.00080264, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 194.28390481, 0.01745946, 194.28390481, 0.05237837, 135.99873337, -2010.77691701, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 48.5709762, 8.026e-05, 145.71292861, 0.00024079, 485.70976204, 0.00080264, -48.5709762, -8.026e-05, -145.71292861, -0.00024079, -485.70976204, -0.00080264, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 23.9, 5.1, 3.125)
    ops.node(122015, 23.9, 5.1, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.16, 28641774.63244529, 11934072.76351887, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 209.89526589, 0.00095806, 252.01536342, 0.00951811, 25.20153634, 0.03407415, -209.89526589, -0.00095806, -252.01536342, -0.00951811, -25.20153634, -0.03407415, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 193.86542183, 0.00095806, 232.76877889, 0.00951811, 23.27687789, 0.03407415, -193.86542183, -0.00095806, -232.76877889, -0.00951811, -23.27687789, -0.03407415, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 190.1350864, 0.0191612, 190.1350864, 0.0574836, 133.09456048, -2285.45192763, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 47.5337716, 8.663e-05, 142.6013148, 0.00025989, 475.33771601, 0.00086631, -47.5337716, -8.663e-05, -142.6013148, -0.00025989, -475.33771601, -0.00086631, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 190.1350864, 0.0191612, 190.1350864, 0.0574836, 133.09456048, -2285.45192763, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 47.5337716, 8.663e-05, 142.6013148, 0.00025989, 475.33771601, 0.00086631, -47.5337716, -8.663e-05, -142.6013148, -0.00025989, -475.33771601, -0.00086631, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 28.1, 5.1, 3.15)
    ops.node(122016, 28.1, 5.1, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1225, 29651021.27614199, 12354592.1983925, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 125.92061686, 0.00098889, 150.98979086, 0.00780168, 15.09897909, 0.03981293, -125.92061686, -0.00098889, -150.98979086, -0.00780168, -15.09897909, -0.03981293, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 141.97382155, 0.00098889, 170.23898197, 0.00780168, 17.0238982, 0.03981293, -141.97382155, -0.00098889, -170.23898197, -0.00780168, -17.0238982, -0.03981293, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 156.94606585, 0.01977773, 156.94606585, 0.0593332, 109.8622461, -1934.3747155, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 39.23651646, 9.022e-05, 117.70954939, 0.00027066, 392.36516463, 0.0009022, -39.23651646, -9.022e-05, -117.70954939, -0.00027066, -392.36516463, -0.0009022, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 156.94606585, 0.01977773, 156.94606585, 0.0593332, 109.8622461, -1934.3747155, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 39.23651646, 9.022e-05, 117.70954939, 0.00027066, 392.36516463, 0.0009022, -39.23651646, -9.022e-05, -117.70954939, -0.00027066, -392.36516463, -0.0009022, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 10.2, 3.15)
    ops.node(122017, 0.0, 10.2, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.1225, 29031822.8264651, 12096592.84436046, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 122.05366654, 0.00099651, 146.49440548, 0.0098546, 14.64944055, 0.04114259, -122.05366654, -0.00099651, -146.49440548, -0.0098546, -14.64944055, -0.04114259, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 136.7830846, 0.00099651, 164.17332823, 0.0098546, 16.41733282, 0.04114259, -136.7830846, -0.00099651, -164.17332823, -0.0098546, -16.41733282, -0.04114259, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 170.6680986, 0.01993016, 170.6680986, 0.05979047, 119.46766902, -2402.06343359, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 42.66702465, 0.0001002, 128.00107395, 0.0003006, 426.67024651, 0.00100201, -42.66702465, -0.0001002, -128.00107395, -0.0003006, -426.67024651, -0.00100201, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 170.6680986, 0.01993016, 170.6680986, 0.05979047, 119.46766902, -2402.06343359, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 42.66702465, 0.0001002, 128.00107395, 0.0003006, 426.67024651, 0.00100201, -42.66702465, -0.0001002, -128.00107395, -0.0003006, -426.67024651, -0.00100201, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 4.2, 10.2, 3.1)
    ops.node(122018, 4.2, 10.2, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.16, 29072619.35094796, 12113591.39622832, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 200.30669928, 0.00088783, 240.55614683, 0.00946877, 24.05561468, 0.03847252, -200.30669928, -0.00088783, -240.55614683, -0.00946877, -24.05561468, -0.03847252, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 172.74707788, 0.00088783, 207.45871996, 0.00946877, 20.745872, 0.03847252, -172.74707788, -0.00088783, -207.45871996, -0.00946877, -20.745872, -0.03847252, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 206.42203321, 0.01775659, 206.42203321, 0.05326977, 144.49542325, -2680.5777595, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 51.6055083, 9.266e-05, 154.81652491, 0.00027797, 516.05508303, 0.00092658, -51.6055083, -9.266e-05, -154.81652491, -0.00027797, -516.05508303, -0.00092658, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 206.42203321, 0.01775659, 206.42203321, 0.05326977, 144.49542325, -2680.5777595, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 51.6055083, 9.266e-05, 154.81652491, 0.00027797, 516.05508303, 0.00092658, -51.6055083, -9.266e-05, -154.81652491, -0.00027797, -516.05508303, -0.00092658, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 8.4, 10.2, 3.1)
    ops.node(122019, 8.4, 10.2, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.16, 30722261.99766035, 12800942.49902515, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 201.02087729, 0.00088524, 240.90519821, 0.00955548, 24.09051982, 0.04100403, -201.02087729, -0.00088524, -240.90519821, -0.00955548, -24.09051982, -0.04100403, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 173.7892921, 0.00088524, 208.27062555, 0.00955548, 20.82706256, 0.04100403, -173.7892921, -0.00088524, -208.27062555, -0.00955548, -20.82706256, -0.04100403, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 218.74780176, 0.01770476, 218.74780176, 0.05311428, 153.12346123, -2790.4567041, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 54.68695044, 9.292e-05, 164.06085132, 0.00027875, 546.8695044, 0.00092918, -54.68695044, -9.292e-05, -164.06085132, -0.00027875, -546.8695044, -0.00092918, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 218.74780176, 0.01770476, 218.74780176, 0.05311428, 153.12346123, -2790.4567041, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 54.68695044, 9.292e-05, 164.06085132, 0.00027875, 546.8695044, 0.00092918, -54.68695044, -9.292e-05, -164.06085132, -0.00027875, -546.8695044, -0.00092918, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 12.6, 10.2, 3.075)
    ops.node(122020, 12.6, 10.2, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.1225, 29509492.97083487, 12295622.07118119, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 126.78896363, 0.00104414, 152.02102956, 0.00986343, 15.20210296, 0.04143005, -126.78896363, -0.00104414, -152.02102956, -0.00986343, -15.20210296, -0.04143005, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 141.47425666, 0.00104414, 169.62881893, 0.00986343, 16.96288189, 0.04143005, -141.47425666, -0.00104414, -169.62881893, -0.00986343, -16.96288189, -0.04143005, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 171.41809346, 0.02088286, 171.41809346, 0.06264859, 119.99266542, -2345.65314603, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 42.85452336, 9.901e-05, 128.56357009, 0.00029704, 428.54523365, 0.00099012, -42.85452336, -9.901e-05, -128.56357009, -0.00029704, -428.54523365, -0.00099012, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 171.41809346, 0.02088286, 171.41809346, 0.06264859, 119.99266542, -2345.65314603, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 42.85452336, 9.901e-05, 128.56357009, 0.00029704, 428.54523365, 0.00099012, -42.85452336, -9.901e-05, -128.56357009, -0.00029704, -428.54523365, -0.00099012, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 15.5, 10.2, 3.075)
    ops.node(122021, 15.5, 10.2, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.1225, 32469025.9492538, 13528760.81218908, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 122.70832771, 0.00096783, 146.40874435, 0.00891866, 14.64087444, 0.04503245, -122.70832771, -0.00096783, -146.40874435, -0.00891866, -14.64087444, -0.04503245, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 136.38717942, 0.00096783, 162.72958859, 0.00891866, 16.27295886, 0.04503245, -136.38717942, -0.00096783, -162.72958859, -0.00891866, -16.27295886, -0.04503245, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 175.0173886, 0.01935663, 175.0173886, 0.05806989, 122.51217202, -2110.23809087, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 43.75434715, 9.188e-05, 131.26304145, 0.00027563, 437.5434715, 0.00091877, -43.75434715, -9.188e-05, -131.26304145, -0.00027563, -437.5434715, -0.00091877, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 175.0173886, 0.01935663, 175.0173886, 0.05806989, 122.51217202, -2110.23809087, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 43.75434715, 9.188e-05, 131.26304145, 0.00027563, 437.5434715, 0.00091877, -43.75434715, -9.188e-05, -131.26304145, -0.00027563, -437.5434715, -0.00091877, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 19.7, 10.2, 3.1)
    ops.node(122022, 19.7, 10.2, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.16, 29547896.73788899, 12311623.64078708, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 195.50176571, 0.00089633, 234.67389015, 0.01012321, 23.46738902, 0.03987133, -195.50176571, -0.00089633, -234.67389015, -0.01012321, -23.46738902, -0.03987133, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 170.37983415, 0.00089633, 204.51834968, 0.01012321, 20.45183497, 0.03987133, -170.37983415, -0.00089633, -204.51834968, -0.01012321, -20.45183497, -0.03987133, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 215.62976071, 0.01792661, 215.62976071, 0.05377982, 150.9408325, -2875.28143349, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 53.90744018, 9.523e-05, 161.72232053, 0.0002857, 539.07440177, 0.00095234, -53.90744018, -9.523e-05, -161.72232053, -0.0002857, -539.07440177, -0.00095234, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 215.62976071, 0.01792661, 215.62976071, 0.05377982, 150.9408325, -2875.28143349, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 53.90744018, 9.523e-05, 161.72232053, 0.0002857, 539.07440177, 0.00095234, -53.90744018, -9.523e-05, -161.72232053, -0.0002857, -539.07440177, -0.00095234, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 23.9, 10.2, 3.1)
    ops.node(122023, 23.9, 10.2, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.16, 27001247.05718, 11250519.60715833, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 200.77955499, 0.00089728, 241.29329166, 0.00767947, 24.12932917, 0.03303187, -200.77955499, -0.00089728, -241.29329166, -0.00767947, -24.12932917, -0.03303187, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 172.40224071, 0.00089728, 207.18994099, 0.00767947, 20.7189941, 0.03303187, -172.40224071, -0.00089728, -207.18994099, -0.00767947, -20.7189941, -0.03303187, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 188.36345325, 0.01794558, 188.36345325, 0.05383674, 131.85441727, -2466.89974913, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 47.09086331, 9.104e-05, 141.27258993, 0.00027311, 470.90863312, 0.00091038, -47.09086331, -9.104e-05, -141.27258993, -0.00027311, -470.90863312, -0.00091038, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 188.36345325, 0.01794558, 188.36345325, 0.05383674, 131.85441727, -2466.89974913, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 47.09086331, 9.104e-05, 141.27258993, 0.00027311, 470.90863312, 0.00091038, -47.09086331, -9.104e-05, -141.27258993, -0.00027311, -470.90863312, -0.00091038, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 28.1, 10.2, 3.15)
    ops.node(122024, 28.1, 10.2, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.1225, 28756295.38523661, 11981789.74384859, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 122.45733969, 0.00097789, 147.00826661, 0.00876312, 14.70082666, 0.03954779, -122.45733969, -0.00097789, -147.00826661, -0.00876312, -14.70082666, -0.03954779, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 138.01540694, 0.00097789, 165.6855015, 0.00876312, 16.56855015, 0.03954779, -138.01540694, -0.00097789, -165.6855015, -0.00876312, -16.56855015, -0.03954779, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 159.44509701, 0.01955777, 159.44509701, 0.05867331, 111.61156791, -2107.98766187, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 39.86127425, 9.451e-05, 119.58382276, 0.00028353, 398.61274254, 0.00094509, -39.86127425, -9.451e-05, -119.58382276, -0.00028353, -398.61274254, -0.00094509, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 159.44509701, 0.01955777, 159.44509701, 0.05867331, 111.61156791, -2107.98766187, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 39.86127425, 9.451e-05, 119.58382276, 0.00028353, 398.61274254, 0.00094509, -39.86127425, -9.451e-05, -119.58382276, -0.00028353, -398.61274254, -0.00094509, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171025, 0.0, 15.3, 3.15)
    ops.node(122025, 0.0, 15.3, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1025, 171025, 122025, 0.0625, 31241751.10258349, 13017396.29274312, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21025, 59.68929263, 0.00142568, 71.23296673, 0.01085479, 7.12329667, 0.052427, -59.68929263, -0.00142568, -71.23296673, -0.01085479, -7.12329667, -0.052427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11025, 63.90486156, 0.00142568, 76.26381009, 0.01085479, 7.62638101, 0.052427, -63.90486156, -0.00142568, -76.26381009, -0.01085479, -7.62638101, -0.052427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21025, 1025, 0.0, 106.36555059, 0.02851367, 106.36555059, 0.085541, 74.45588541, -1597.48694823, 0.05, 2, 0, 71025, 22025, 2, 3)
    ops.uniaxialMaterial('LimitState', 41025, 26.59138765, 0.00011374, 79.77416294, 0.00034122, 265.91387648, 0.00113741, -26.59138765, -0.00011374, -79.77416294, -0.00034122, -265.91387648, -0.00113741, 0.4, 0.3, 0.003, 0.0, 0.0, 21025, 2)
    ops.limitCurve('ThreePoint', 11025, 1025, 0.0, 106.36555059, 0.02851367, 106.36555059, 0.085541, 74.45588541, -1597.48694823, 0.05, 2, 0, 71025, 22025, 1, 3)
    ops.uniaxialMaterial('LimitState', 31025, 26.59138765, 0.00011374, 79.77416294, 0.00034122, 265.91387648, 0.00113741, -26.59138765, -0.00011374, -79.77416294, -0.00034122, -265.91387648, -0.00113741, 0.4, 0.3, 0.003, 0.0, 0.0, 11025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1025, 99999, 'P', 41025, 'Vy', 31025, 'Vz', 21025, 'My', 11025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171025, 71025, 171025, 1025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122025, 122025, 22025, 1025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171026, 4.2, 15.3, 3.1)
    ops.node(122026, 4.2, 15.3, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1026, 171026, 122026, 0.09, 28937022.7861094, 12057092.82754558, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21026, 108.43431909, 0.00117139, 129.52459438, 0.00829101, 12.95245944, 0.03850231, -108.43431909, -0.00117139, -129.52459438, -0.00829101, -12.95245944, -0.03850231, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11026, 129.11036335, 0.00117139, 154.22209114, 0.00829101, 15.42220911, 0.03850231, -129.11036335, -0.00117139, -154.22209114, -0.00829101, -15.42220911, -0.03850231, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21026, 1026, 0.0, 129.67584242, 0.02342774, 129.67584242, 0.07028321, 90.77308969, -1794.38671748, 0.05, 2, 0, 71026, 22026, 2, 3)
    ops.uniaxialMaterial('LimitState', 41026, 32.4189606, 0.00010397, 97.25688181, 0.0003119, 324.18960605, 0.00103966, -32.4189606, -0.00010397, -97.25688181, -0.0003119, -324.18960605, -0.00103966, 0.4, 0.3, 0.003, 0.0, 0.0, 21026, 2)
    ops.limitCurve('ThreePoint', 11026, 1026, 0.0, 129.67584242, 0.02342774, 129.67584242, 0.07028321, 90.77308969, -1794.38671748, 0.05, 2, 0, 71026, 22026, 1, 3)
    ops.uniaxialMaterial('LimitState', 31026, 32.4189606, 0.00010397, 97.25688181, 0.0003119, 324.18960605, 0.00103966, -32.4189606, -0.00010397, -97.25688181, -0.0003119, -324.18960605, -0.00103966, 0.4, 0.3, 0.003, 0.0, 0.0, 11026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1026, 99999, 'P', 41026, 'Vy', 31026, 'Vz', 21026, 'My', 11026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171026, 71026, 171026, 1026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122026, 122026, 22026, 1026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171027, 8.4, 15.3, 3.1)
    ops.node(122027, 8.4, 15.3, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1027, 171027, 122027, 0.09, 26152220.18426416, 10896758.41011007, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21027, 104.92998402, 0.0012747, 125.08145537, 0.00786634, 12.50814554, 0.03111624, -104.92998402, -0.0012747, -125.08145537, -0.00786634, -12.50814554, -0.03111624, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11027, 122.04533494, 0.0012747, 145.48375528, 0.00786634, 14.54837553, 0.03111624, -122.04533494, -0.0012747, -145.48375528, -0.00786634, -14.54837553, -0.03111624, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21027, 1027, 0.0, 119.92080597, 0.02549394, 119.92080597, 0.07648181, 83.94456418, -1750.11427389, 0.05, 2, 0, 71027, 22027, 2, 3)
    ops.uniaxialMaterial('LimitState', 41027, 29.98020149, 0.00010638, 89.94060448, 0.00031915, 299.80201492, 0.00106383, -29.98020149, -0.00010638, -89.94060448, -0.00031915, -299.80201492, -0.00106383, 0.4, 0.3, 0.003, 0.0, 0.0, 21027, 2)
    ops.limitCurve('ThreePoint', 11027, 1027, 0.0, 119.92080597, 0.02549394, 119.92080597, 0.07648181, 83.94456418, -1750.11427389, 0.05, 2, 0, 71027, 22027, 1, 3)
    ops.uniaxialMaterial('LimitState', 31027, 29.98020149, 0.00010638, 89.94060448, 0.00031915, 299.80201492, 0.00106383, -29.98020149, -0.00010638, -89.94060448, -0.00031915, -299.80201492, -0.00106383, 0.4, 0.3, 0.003, 0.0, 0.0, 11027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1027, 99999, 'P', 41027, 'Vy', 31027, 'Vz', 21027, 'My', 11027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171027, 71027, 171027, 1027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122027, 122027, 22027, 1027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171028, 12.6, 15.3, 3.075)
    ops.node(122028, 12.6, 15.3, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1028, 171028, 122028, 0.0625, 28172494.4326057, 11738539.34691904, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21028, 85.33599928, 0.00161055, 101.42309619, 0.01009498, 10.14230962, 0.034595, -85.33599928, -0.00161055, -101.42309619, -0.01009498, -10.14230962, -0.034595, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11028, 92.38637164, 0.00161055, 109.80256794, 0.01009498, 10.98025679, 0.034595, -92.38637164, -0.00161055, -109.80256794, -0.01009498, -10.98025679, -0.034595, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21028, 1028, 0.0, 71.14694685, 0.03221105, 71.14694685, 0.09663314, 49.80286279, -1326.19112533, 0.05, 2, 0, 71028, 22028, 2, 3)
    ops.uniaxialMaterial('LimitState', 41028, 17.78673671, 8.437e-05, 53.36021014, 0.00025311, 177.86736712, 0.00084369, -17.78673671, -8.437e-05, -53.36021014, -0.00025311, -177.86736712, -0.00084369, 0.4, 0.3, 0.003, 0.0, 0.0, 21028, 2)
    ops.limitCurve('ThreePoint', 11028, 1028, 0.0, 71.14694685, 0.03221105, 71.14694685, 0.09663314, 49.80286279, -1326.19112533, 0.05, 2, 0, 71028, 22028, 1, 3)
    ops.uniaxialMaterial('LimitState', 31028, 17.78673671, 8.437e-05, 53.36021014, 0.00025311, 177.86736712, 0.00084369, -17.78673671, -8.437e-05, -53.36021014, -0.00025311, -177.86736712, -0.00084369, 0.4, 0.3, 0.003, 0.0, 0.0, 11028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1028, 99999, 'P', 41028, 'Vy', 31028, 'Vz', 21028, 'My', 11028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171028, 71028, 171028, 1028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122028, 122028, 22028, 1028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171029, 15.5, 15.3, 3.075)
    ops.node(122029, 15.5, 15.3, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1029, 171029, 122029, 0.0625, 26829606.16751771, 11179002.56979905, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21029, 87.99427916, 0.0015398, 104.38563017, 0.01084286, 10.43856302, 0.03187791, -87.99427916, -0.0015398, -104.38563017, -0.01084286, -10.43856302, -0.03187791, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11029, 96.68589342, 0.0015398, 114.69629628, 0.01084286, 11.46962963, 0.03187791, -96.68589342, -0.0015398, -114.69629628, -0.01084286, -11.46962963, -0.03187791, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21029, 1029, 0.0, 94.98778954, 0.0307959, 94.98778954, 0.0923877, 66.49145268, -1539.8018484, 0.05, 2, 0, 71029, 22029, 2, 3)
    ops.uniaxialMaterial('LimitState', 41029, 23.74694738, 0.00011828, 71.24084215, 0.00035483, 237.46947385, 0.00118278, -23.74694738, -0.00011828, -71.24084215, -0.00035483, -237.46947385, -0.00118278, 0.4, 0.3, 0.003, 0.0, 0.0, 21029, 2)
    ops.limitCurve('ThreePoint', 11029, 1029, 0.0, 94.98778954, 0.0307959, 94.98778954, 0.0923877, 66.49145268, -1539.8018484, 0.05, 2, 0, 71029, 22029, 1, 3)
    ops.uniaxialMaterial('LimitState', 31029, 23.74694738, 0.00011828, 71.24084215, 0.00035483, 237.46947385, 0.00118278, -23.74694738, -0.00011828, -71.24084215, -0.00035483, -237.46947385, -0.00118278, 0.4, 0.3, 0.003, 0.0, 0.0, 11029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1029, 99999, 'P', 41029, 'Vy', 31029, 'Vz', 21029, 'My', 11029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171029, 71029, 171029, 1029, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122029, 122029, 22029, 1029, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171030, 19.7, 15.3, 3.1)
    ops.node(122030, 19.7, 15.3, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1030, 171030, 122030, 0.09, 34109029.68749252, 14212095.70312188, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21030, 110.04576855, 0.00120699, 130.41205489, 0.00831027, 13.04120549, 0.04810472, -110.04576855, -0.00120699, -130.41205489, -0.00831027, -13.04120549, -0.04810472, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11030, 128.00706841, 0.00120699, 151.69747144, 0.00831027, 15.16974714, 0.04810472, -128.00706841, -0.00120699, -151.69747144, -0.00831027, -15.16974714, -0.04810472, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21030, 1030, 0.0, 142.59708803, 0.02413988, 142.59708803, 0.07241964, 99.81796162, -1717.06565723, 0.05, 2, 0, 71030, 22030, 2, 3)
    ops.uniaxialMaterial('LimitState', 41030, 35.64927201, 9.699e-05, 106.94781602, 0.00029097, 356.49272007, 0.00096991, -35.64927201, -9.699e-05, -106.94781602, -0.00029097, -356.49272007, -0.00096991, 0.4, 0.3, 0.003, 0.0, 0.0, 21030, 2)
    ops.limitCurve('ThreePoint', 11030, 1030, 0.0, 142.59708803, 0.02413988, 142.59708803, 0.07241964, 99.81796162, -1717.06565723, 0.05, 2, 0, 71030, 22030, 1, 3)
    ops.uniaxialMaterial('LimitState', 31030, 35.64927201, 9.699e-05, 106.94781602, 0.00029097, 356.49272007, 0.00096991, -35.64927201, -9.699e-05, -106.94781602, -0.00029097, -356.49272007, -0.00096991, 0.4, 0.3, 0.003, 0.0, 0.0, 11030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1030, 99999, 'P', 41030, 'Vy', 31030, 'Vz', 21030, 'My', 11030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171030, 71030, 171030, 1030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122030, 122030, 22030, 1030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171031, 23.9, 15.3, 3.1)
    ops.node(122031, 23.9, 15.3, 5.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1031, 171031, 122031, 0.09, 32875036.15571297, 13697931.73154707, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21031, 110.5743258, 0.00118502, 131.43836676, 0.0091494, 13.14383668, 0.04702871, -110.5743258, -0.00118502, -131.43836676, -0.0091494, -13.14383668, -0.04702871, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11031, 130.16685208, 0.00118502, 154.72776632, 0.0091494, 15.47277663, 0.04702871, -130.16685208, -0.00118502, -154.72776632, -0.0091494, -15.47277663, -0.04702871, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21031, 1031, 0.0, 141.59557462, 0.02370048, 141.59557462, 0.07110145, 99.11690224, -1792.95916866, 0.05, 2, 0, 71031, 22031, 2, 3)
    ops.uniaxialMaterial('LimitState', 41031, 35.39889366, 9.992e-05, 106.19668097, 0.00029977, 353.98893656, 0.00099924, -35.39889366, -9.992e-05, -106.19668097, -0.00029977, -353.98893656, -0.00099924, 0.4, 0.3, 0.003, 0.0, 0.0, 21031, 2)
    ops.limitCurve('ThreePoint', 11031, 1031, 0.0, 141.59557462, 0.02370048, 141.59557462, 0.07110145, 99.11690224, -1792.95916866, 0.05, 2, 0, 71031, 22031, 1, 3)
    ops.uniaxialMaterial('LimitState', 31031, 35.39889366, 9.992e-05, 106.19668097, 0.00029977, 353.98893656, 0.00099924, -35.39889366, -9.992e-05, -106.19668097, -0.00029977, -353.98893656, -0.00099924, 0.4, 0.3, 0.003, 0.0, 0.0, 11031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1031, 99999, 'P', 41031, 'Vy', 31031, 'Vz', 21031, 'My', 11031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171031, 71031, 171031, 1031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122031, 122031, 22031, 1031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171032, 28.1, 15.3, 3.15)
    ops.node(122032, 28.1, 15.3, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1032, 171032, 122032, 0.0625, 30873640.36597519, 12864016.81915633, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21032, 59.82490323, 0.00140732, 71.43279003, 0.00920829, 7.143279, 0.04998993, -59.82490323, -0.00140732, -71.43279003, -0.00920829, -7.143279, -0.04998993, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11032, 64.22841773, 0.00140732, 76.69072293, 0.00920829, 7.66907229, 0.04998993, -64.22841773, -0.00140732, -76.69072293, -0.00920829, -7.66907229, -0.04998993, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21032, 1032, 0.0, 92.84873276, 0.02814646, 92.84873276, 0.08443938, 64.99411294, -1441.57296014, 0.05, 2, 0, 71032, 22032, 2, 3)
    ops.uniaxialMaterial('LimitState', 41032, 23.21218319, 0.00010047, 69.63654957, 0.00030141, 232.12183191, 0.00100471, -23.21218319, -0.00010047, -69.63654957, -0.00030141, -232.12183191, -0.00100471, 0.4, 0.3, 0.003, 0.0, 0.0, 21032, 2)
    ops.limitCurve('ThreePoint', 11032, 1032, 0.0, 92.84873276, 0.02814646, 92.84873276, 0.08443938, 64.99411294, -1441.57296014, 0.05, 2, 0, 71032, 22032, 1, 3)
    ops.uniaxialMaterial('LimitState', 31032, 23.21218319, 0.00010047, 69.63654957, 0.00030141, 232.12183191, 0.00100471, -23.21218319, -0.00010047, -69.63654957, -0.00030141, -232.12183191, -0.00100471, 0.4, 0.3, 0.003, 0.0, 0.0, 11032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1032, 99999, 'P', 41032, 'Vy', 31032, 'Vz', 21032, 'My', 11032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171032, 71032, 171032, 1032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122032, 122032, 22032, 1032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.05)
    ops.node(123001, 0.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 29809683.56008601, 12420701.48336917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 45.14095972, 0.00126303, 54.33581301, 0.01168086, 5.4335813, 0.05879062, -45.14095972, -0.00126303, -54.33581301, -0.01168086, -5.4335813, -0.05879062, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 45.14095972, 0.00126303, 54.33581301, 0.01168086, 5.4335813, 0.05879062, -45.14095972, -0.00126303, -54.33581301, -0.01168086, -5.4335813, -0.05879062, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 98.8431616, 0.02526051, 98.8431616, 0.07578153, 69.19021312, -1741.08585131, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 24.7107904, 0.00011077, 74.1323712, 0.00033232, 247.107904, 0.00110774, -24.7107904, -0.00011077, -74.1323712, -0.00033232, -247.107904, -0.00110774, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 98.8431616, 0.02526051, 98.8431616, 0.07578153, 69.19021312, -1741.08585131, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 24.7107904, 0.00011077, 74.1323712, 0.00033232, 247.107904, 0.00110774, -24.7107904, -0.00011077, -74.1323712, -0.00033232, -247.107904, -0.00110774, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.2, 0.0, 6.0)
    ops.node(123002, 4.2, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 30651788.08610618, 12771578.36921091, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 58.69725054, 0.00130879, 70.11834732, 0.0118596, 7.01183473, 0.05235471, -58.69725054, -0.00130879, -70.11834732, -0.0118596, -7.01183473, -0.05235471, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 63.42390026, 0.00130879, 75.76469129, 0.0118596, 7.57646913, 0.05235471, -63.42390026, -0.00130879, -75.76469129, -0.0118596, -7.57646913, -0.05235471, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 108.65910272, 0.0261757, 108.65910272, 0.0785271, 76.0613719, -1714.32907903, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 27.16477568, 0.00011843, 81.49432704, 0.00035529, 271.6477568, 0.0011843, -27.16477568, -0.00011843, -81.49432704, -0.00035529, -271.6477568, -0.0011843, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 108.65910272, 0.0261757, 108.65910272, 0.0785271, 76.0613719, -1714.32907903, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 27.16477568, 0.00011843, 81.49432704, 0.00035529, 271.6477568, 0.0011843, -27.16477568, -0.00011843, -81.49432704, -0.00035529, -271.6477568, -0.0011843, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.4, 0.0, 6.0)
    ops.node(123003, 8.4, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0625, 27713405.78159033, 11547252.40899597, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 68.80747189, 0.00140982, 82.31061047, 0.01072566, 8.23106105, 0.03945065, -68.80747189, -0.00140982, -82.31061047, -0.01072566, -8.23106105, -0.03945065, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 68.80747189, 0.00140982, 82.31061047, 0.01072566, 8.23106105, 0.03945065, -68.80747189, -0.00140982, -82.31061047, -0.01072566, -8.23106105, -0.03945065, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 80.61992324, 0.02819647, 80.61992324, 0.08458942, 56.43394627, -1391.94528924, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 20.15498081, 9.719e-05, 60.46494243, 0.00029156, 201.54980811, 0.00097186, -20.15498081, -9.719e-05, -60.46494243, -0.00029156, -201.54980811, -0.00097186, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 80.61992324, 0.02819647, 80.61992324, 0.08458942, 56.43394627, -1391.94528924, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 20.15498081, 9.719e-05, 60.46494243, 0.00029156, 201.54980811, 0.00097186, -20.15498081, -9.719e-05, -60.46494243, -0.00029156, -201.54980811, -0.00097186, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 19.7, 0.0, 6.0)
    ops.node(123006, 19.7, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 28408137.80361635, 11836724.08484015, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 70.71161193, 0.00145516, 84.59837054, 0.00952327, 8.45983705, 0.0398942, -70.71161193, -0.00145516, -84.59837054, -0.00952327, -8.45983705, -0.0398942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 70.71161193, 0.00145516, 84.59837054, 0.00952327, 8.45983705, 0.0398942, -70.71161193, -0.00145516, -84.59837054, -0.00952327, -8.45983705, -0.0398942, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 60.92626952, 0.0291032, 60.92626952, 0.08730961, 42.64838866, -1165.43164039, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 15.23156738, 7.165e-05, 45.69470214, 0.00021495, 152.3156738, 0.00071649, -15.23156738, -7.165e-05, -45.69470214, -0.00021495, -152.3156738, -0.00071649, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 60.92626952, 0.0291032, 60.92626952, 0.08730961, 42.64838866, -1165.43164039, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 15.23156738, 7.165e-05, 45.69470214, 0.00021495, 152.3156738, 0.00071649, -15.23156738, -7.165e-05, -45.69470214, -0.00021495, -152.3156738, -0.00071649, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 23.9, 0.0, 6.0)
    ops.node(123007, 23.9, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 29458187.76720933, 12274244.90300389, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 57.63460875, 0.00153475, 68.92785812, 0.0094538, 6.89278581, 0.04716741, -57.63460875, -0.00153475, -68.92785812, -0.0094538, -6.89278581, -0.04716741, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 60.92532544, 0.00153475, 72.86337635, 0.0094538, 7.28633763, 0.04716741, -60.92532544, -0.00153475, -72.86337635, -0.0094538, -7.28633763, -0.04716741, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 92.83083162, 0.03069491, 92.83083162, 0.09208473, 64.98158213, -1464.65983537, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 23.2077079, 0.00010528, 69.62312371, 0.00031583, 232.07707904, 0.00105278, -23.2077079, -0.00010528, -69.62312371, -0.00031583, -232.07707904, -0.00105278, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 92.83083162, 0.03069491, 92.83083162, 0.09208473, 64.98158213, -1464.65983537, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 23.2077079, 0.00010528, 69.62312371, 0.00031583, 232.07707904, 0.00105278, -23.2077079, -0.00010528, -69.62312371, -0.00031583, -232.07707904, -0.00105278, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 28.1, 0.0, 6.05)
    ops.node(123008, 28.1, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 28711573.28921484, 11963155.53717285, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 40.42640609, 0.00151067, 48.73312031, 0.0099063, 4.87331203, 0.05486079, -40.42640609, -0.00151067, -48.73312031, -0.0099063, -4.87331203, -0.05486079, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 40.42640609, 0.00151067, 48.73312031, 0.0099063, 4.87331203, 0.05486079, -40.42640609, -0.00151067, -48.73312031, -0.0099063, -4.87331203, -0.05486079, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 79.45873368, 0.0302134, 79.45873368, 0.0906402, 55.62111358, -1345.05931644, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 19.86468342, 9.246e-05, 59.59405026, 0.00027737, 198.6468342, 0.00092456, -19.86468342, -9.246e-05, -59.59405026, -0.00027737, -198.6468342, -0.00092456, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 79.45873368, 0.0302134, 79.45873368, 0.0906402, 55.62111358, -1345.05931644, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 19.86468342, 9.246e-05, 59.59405026, 0.00027737, 198.6468342, 0.00092456, -19.86468342, -9.246e-05, -59.59405026, -0.00027737, -198.6468342, -0.00092456, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 5.1, 6.05)
    ops.node(123009, 0.0, 5.1, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 26524091.41939091, 11051704.75807955, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 54.80680202, 0.00136129, 65.37087856, 0.00930274, 6.53708786, 0.03726204, -54.80680202, -0.00136129, -65.37087856, -0.00930274, -6.53708786, -0.03726204, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 54.80680202, 0.00136129, 65.37087856, 0.00930274, 6.53708786, 0.03726204, -54.80680202, -0.00136129, -65.37087856, -0.00930274, -6.53708786, -0.03726204, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 95.42927147, 0.02722572, 95.42927147, 0.08167717, 66.80049003, -1533.47874114, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 23.85731787, 0.0001202, 71.5719536, 0.00036059, 238.57317868, 0.00120196, -23.85731787, -0.0001202, -71.5719536, -0.00036059, -238.57317868, -0.00120196, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 95.42927147, 0.02722572, 95.42927147, 0.08167717, 66.80049003, -1533.47874114, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 23.85731787, 0.0001202, 71.5719536, 0.00036059, 238.57317868, 0.00120196, -23.85731787, -0.0001202, -71.5719536, -0.00036059, -238.57317868, -0.00120196, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 4.2, 5.1, 6.0)
    ops.node(123010, 4.2, 5.1, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 33340524.8414375, 13891885.35059896, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 142.32413671, 0.00097296, 169.71891519, 0.00887352, 16.97189152, 0.04315123, -142.32413671, -0.00097296, -169.71891519, -0.00887352, -16.97189152, -0.04315123, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 134.95314306, 0.00097296, 160.92914084, 0.00887352, 16.09291408, 0.04315123, -134.95314306, -0.00097296, -160.92914084, -0.00887352, -16.09291408, -0.04315123, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 162.9882324, 0.01945911, 162.9882324, 0.05837732, 114.09176268, -1756.89953395, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 40.7470581, 8.333e-05, 122.2411743, 0.00024998, 407.470581, 0.00083326, -40.7470581, -8.333e-05, -122.2411743, -0.00024998, -407.470581, -0.00083326, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 162.9882324, 0.01945911, 162.9882324, 0.05837732, 114.09176268, -1756.89953395, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 40.7470581, 8.333e-05, 122.2411743, 0.00024998, 407.470581, 0.00083326, -40.7470581, -8.333e-05, -122.2411743, -0.00024998, -407.470581, -0.00083326, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.4, 5.1, 6.0)
    ops.node(123011, 8.4, 5.1, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 29093011.75661206, 12122088.23192169, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 146.50184482, 0.00100711, 176.16714041, 0.01040043, 17.61671404, 0.03957611, -146.50184482, -0.00100711, -176.16714041, -0.01040043, -17.61671404, -0.03957611, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 138.35488157, 0.00100711, 166.37049095, 0.01040043, 16.6370491, 0.03957611, -138.35488157, -0.00100711, -166.37049095, -0.01040043, -16.6370491, -0.03957611, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 153.63885274, 0.02014213, 153.63885274, 0.06042639, 107.54719692, -1967.91570405, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 38.40971319, 9.001e-05, 115.22913956, 0.00027004, 384.09713185, 0.00090013, -38.40971319, -9.001e-05, -115.22913956, -0.00027004, -384.09713185, -0.00090013, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 153.63885274, 0.02014213, 153.63885274, 0.06042639, 107.54719692, -1967.91570405, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 38.40971319, 9.001e-05, 115.22913956, 0.00027004, 384.09713185, 0.00090013, -38.40971319, -9.001e-05, -115.22913956, -0.00027004, -384.09713185, -0.00090013, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 12.6, 5.1, 6.0)
    ops.node(123012, 12.6, 5.1, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 29369354.30670407, 12237230.96112669, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 155.02257882, 0.00100534, 186.51277048, 0.00852399, 18.65127705, 0.03358026, -155.02257882, -0.00100534, -186.51277048, -0.00852399, -18.65127705, -0.03358026, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 155.02257882, 0.00100534, 186.51277048, 0.00852399, 18.65127705, 0.03358026, -155.02257882, -0.00100534, -186.51277048, -0.00852399, -18.65127705, -0.03358026, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 119.48719665, 0.02010687, 119.48719665, 0.06032061, 83.64103766, -1394.74231729, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 29.87179916, 6.935e-05, 89.61539749, 0.00020804, 298.71799163, 0.00069346, -29.87179916, -6.935e-05, -89.61539749, -0.00020804, -298.71799163, -0.00069346, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 119.48719665, 0.02010687, 119.48719665, 0.06032061, 83.64103766, -1394.74231729, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 29.87179916, 6.935e-05, 89.61539749, 0.00020804, 298.71799163, 0.00069346, -29.87179916, -6.935e-05, -89.61539749, -0.00020804, -298.71799163, -0.00069346, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 15.5, 5.1, 6.0)
    ops.node(123013, 15.5, 5.1, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.1225, 28556396.76498147, 11898498.65207561, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 152.39493727, 0.00108679, 183.51312326, 0.00964027, 18.35131233, 0.03372616, -152.39493727, -0.00108679, -183.51312326, -0.00964027, -18.35131233, -0.03372616, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 152.39493727, 0.00108679, 183.51312326, 0.00964027, 18.35131233, 0.03372616, -152.39493727, -0.00108679, -183.51312326, -0.00964027, -18.35131233, -0.03372616, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 138.93397177, 0.02173585, 138.93397177, 0.06520756, 97.25378024, -1640.94995883, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 34.73349294, 8.293e-05, 104.20047882, 0.00024878, 347.33492941, 0.00082928, -34.73349294, -8.293e-05, -104.20047882, -0.00024878, -347.33492941, -0.00082928, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 138.93397177, 0.02173585, 138.93397177, 0.06520756, 97.25378024, -1640.94995883, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 34.73349294, 8.293e-05, 104.20047882, 0.00024878, 347.33492941, 0.00082928, -34.73349294, -8.293e-05, -104.20047882, -0.00024878, -347.33492941, -0.00082928, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 19.7, 5.1, 6.0)
    ops.node(123014, 19.7, 5.1, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1225, 28238947.50153174, 11766228.12563823, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 140.78423704, 0.00101981, 169.41320497, 0.00903895, 16.9413205, 0.03690031, -140.78423704, -0.00101981, -169.41320497, -0.00903895, -16.9413205, -0.03690031, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 133.47904281, 0.00101981, 160.62247388, 0.00903895, 16.06224739, 0.03690031, -133.47904281, -0.00101981, -160.62247388, -0.00903895, -16.06224739, -0.03690031, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 141.47883686, 0.02039626, 141.47883686, 0.06118877, 99.03518581, -1720.08329968, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 35.36970922, 8.54e-05, 106.10912765, 0.00025619, 353.69709216, 0.00085396, -35.36970922, -8.54e-05, -106.10912765, -0.00025619, -353.69709216, -0.00085396, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 141.47883686, 0.02039626, 141.47883686, 0.06118877, 99.03518581, -1720.08329968, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 35.36970922, 8.54e-05, 106.10912765, 0.00025619, 353.69709216, 0.00085396, -35.36970922, -8.54e-05, -106.10912765, -0.00025619, -353.69709216, -0.00085396, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 23.9, 5.1, 6.0)
    ops.node(123015, 23.9, 5.1, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 28849828.05117931, 12020761.68799138, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 147.07568345, 0.00100316, 176.89968646, 0.00982515, 17.68996865, 0.03863766, -147.07568345, -0.00100316, -176.89968646, -0.00982515, -17.68996865, -0.03863766, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 138.78021197, 0.00100316, 166.92205951, 0.00982515, 16.69220595, 0.03863766, -138.78021197, -0.00100316, -166.92205951, -0.00982515, -16.69220595, -0.03863766, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 151.68162997, 0.02006319, 151.68162997, 0.06018958, 106.17714098, -1938.52893746, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 37.92040749, 8.962e-05, 113.76122248, 0.00026885, 379.20407492, 0.00089616, -37.92040749, -8.962e-05, -113.76122248, -0.00026885, -379.20407492, -0.00089616, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 151.68162997, 0.02006319, 151.68162997, 0.06018958, 106.17714098, -1938.52893746, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 37.92040749, 8.962e-05, 113.76122248, 0.00026885, 379.20407492, 0.00089616, -37.92040749, -8.962e-05, -113.76122248, -0.00026885, -379.20407492, -0.00089616, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 28.1, 5.1, 6.05)
    ops.node(123016, 28.1, 5.1, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 31096026.82304648, 12956677.84293604, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 54.3970469, 0.00136796, 64.86617534, 0.01097313, 6.48661753, 0.05101755, -54.3970469, -0.00136796, -64.86617534, -0.01097313, -6.48661753, -0.05101755, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 54.3970469, 0.00136796, 64.86617534, 0.01097313, 6.48661753, 0.05101755, -54.3970469, -0.00136796, -64.86617534, -0.01097313, -6.48661753, -0.05101755, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 109.89509923, 0.02735917, 109.89509923, 0.08207752, 76.92656946, -1687.23658933, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 27.47377481, 0.00011807, 82.42132442, 0.0003542, 274.73774806, 0.00118066, -27.47377481, -0.00011807, -82.42132442, -0.0003542, -274.73774806, -0.00118066, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 109.89509923, 0.02735917, 109.89509923, 0.08207752, 76.92656946, -1687.23658933, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 27.47377481, 0.00011807, 82.42132442, 0.0003542, 274.73774806, 0.00118066, -27.47377481, -0.00011807, -82.42132442, -0.0003542, -274.73774806, -0.00118066, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 10.2, 6.05)
    ops.node(123017, 0.0, 10.2, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 30488544.4621688, 12703560.19257033, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 53.72002449, 0.00149939, 64.13308122, 0.00932529, 6.41330812, 0.04849107, -53.72002449, -0.00149939, -64.13308122, -0.00932529, -6.41330812, -0.04849107, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 53.72002449, 0.00149939, 64.13308122, 0.00932529, 6.41330812, 0.04849107, -53.72002449, -0.00149939, -64.13308122, -0.00932529, -6.41330812, -0.04849107, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 100.62755468, 0.02998783, 100.62755468, 0.08996348, 70.43928827, -1457.30849627, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 25.15688867, 0.00011026, 75.47066601, 0.00033079, 251.56888669, 0.00110263, -25.15688867, -0.00011026, -75.47066601, -0.00033079, -251.56888669, -0.00110263, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 100.62755468, 0.02998783, 100.62755468, 0.08996348, 70.43928827, -1457.30849627, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 25.15688867, 0.00011026, 75.47066601, 0.00033079, 251.56888669, 0.00110263, -25.15688867, -0.00011026, -75.47066601, -0.00033079, -251.56888669, -0.00110263, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 4.2, 10.2, 6.0)
    ops.node(123018, 4.2, 10.2, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1225, 28815020.79176477, 12006258.66323532, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 113.65996066, 0.0010465, 136.77471452, 0.00947419, 13.67747145, 0.04269508, -113.65996066, -0.0010465, -136.77471452, -0.00947419, -13.67747145, -0.04269508, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 126.29470771, 0.0010465, 151.97895981, 0.00947419, 15.19789598, 0.04269508, -126.29470771, -0.0010465, -151.97895981, -0.00947419, -15.19789598, -0.04269508, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 159.05776443, 0.02092993, 159.05776443, 0.06278979, 111.3404351, -2179.01709674, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 39.76444111, 9.409e-05, 119.29332332, 0.00028226, 397.64441108, 0.00094087, -39.76444111, -9.409e-05, -119.29332332, -0.00028226, -397.64441108, -0.00094087, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 159.05776443, 0.02092993, 159.05776443, 0.06278979, 111.3404351, -2179.01709674, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 39.76444111, 9.409e-05, 119.29332332, 0.00028226, 397.64441108, 0.00094087, -39.76444111, -9.409e-05, -119.29332332, -0.00028226, -397.64441108, -0.00094087, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 8.4, 10.2, 6.0)
    ops.node(123019, 8.4, 10.2, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1225, 25682464.47562659, 10701026.86484441, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 109.69056114, 0.00100614, 132.05758356, 0.00946342, 13.20575836, 0.03647889, -109.69056114, -0.00100614, -132.05758356, -0.00946342, -13.20575836, -0.03647889, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 122.71217471, 0.00100614, 147.73443674, 0.00946342, 14.77344367, 0.03647889, -122.71217471, -0.00100614, -147.73443674, -0.00946342, -14.77344367, -0.03647889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 151.46380686, 0.02012273, 151.46380686, 0.0603682, 106.02466481, -2304.55194506, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 37.86595172, 0.00010052, 113.59785515, 0.00030157, 378.65951716, 0.00100523, -37.86595172, -0.00010052, -113.59785515, -0.00030157, -378.65951716, -0.00100523, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 151.46380686, 0.02012273, 151.46380686, 0.0603682, 106.02466481, -2304.55194506, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 37.86595172, 0.00010052, 113.59785515, 0.00030157, 378.65951716, 0.00100523, -37.86595172, -0.00010052, -113.59785515, -0.00030157, -378.65951716, -0.00100523, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 12.6, 10.2, 5.975)
    ops.node(123020, 12.6, 10.2, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 30854831.70625789, 12856179.87760746, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 56.2264185, 0.00143198, 66.9843242, 0.01000516, 6.69843242, 0.04805916, -56.2264185, -0.00143198, -66.9843242, -0.01000516, -6.69843242, -0.04805916, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 56.2264185, 0.00143198, 66.9843242, 0.01000516, 6.69843242, 0.04805916, -56.2264185, -0.00143198, -66.9843242, -0.01000516, -6.69843242, -0.04805916, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 109.69936399, 0.0286397, 109.69936399, 0.08591909, 76.78955479, -1665.55771918, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 27.424841, 0.00011878, 82.27452299, 0.00035633, 274.24840997, 0.00118777, -27.424841, -0.00011878, -82.27452299, -0.00035633, -274.24840997, -0.00118777, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 109.69936399, 0.0286397, 109.69936399, 0.08591909, 76.78955479, -1665.55771918, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 27.424841, 0.00011878, 82.27452299, 0.00035633, 274.24840997, 0.00118777, -27.424841, -0.00011878, -82.27452299, -0.00035633, -274.24840997, -0.00118777, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 15.5, 10.2, 5.975)
    ops.node(123021, 15.5, 10.2, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 28288923.7208566, 11787051.55035692, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 57.24601209, 0.00139975, 68.26438334, 0.00850507, 6.82643833, 0.03998714, -57.24601209, -0.00139975, -68.26438334, -0.00850507, -6.82643833, -0.03998714, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 57.24601209, 0.00139975, 68.26438334, 0.00850507, 6.82643833, 0.03998714, -57.24601209, -0.00139975, -68.26438334, -0.00850507, -6.82643833, -0.03998714, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 94.24012581, 0.02799497, 94.24012581, 0.0839849, 65.96808806, -1470.09140839, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 23.56003145, 0.00011129, 70.68009435, 0.00033388, 235.60031451, 0.00111294, -23.56003145, -0.00011129, -70.68009435, -0.00033388, -235.60031451, -0.00111294, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 94.24012581, 0.02799497, 94.24012581, 0.0839849, 65.96808806, -1470.09140839, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 23.56003145, 0.00011129, 70.68009435, 0.00033388, 235.60031451, 0.00111294, -23.56003145, -0.00011129, -70.68009435, -0.00033388, -235.60031451, -0.00111294, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 19.7, 10.2, 6.0)
    ops.node(123022, 19.7, 10.2, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.1225, 29721660.9941299, 12384025.41422079, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 112.19490113, 0.00099563, 134.86775396, 0.00971557, 13.4867754, 0.04440944, -112.19490113, -0.00099563, -134.86775396, -0.00971557, -13.4867754, -0.04440944, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 125.15867411, 0.00099563, 150.45130479, 0.00971557, 15.04513048, 0.04440944, -125.15867411, -0.00099563, -150.45130479, -0.00971557, -15.04513048, -0.04440944, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 161.98506587, 0.01991262, 161.98506587, 0.05973787, 113.38954611, -2162.04029486, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 40.49626647, 9.29e-05, 121.4887994, 0.00027869, 404.96266468, 0.00092896, -40.49626647, -9.29e-05, -121.4887994, -0.00027869, -404.96266468, -0.00092896, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 161.98506587, 0.01991262, 161.98506587, 0.05973787, 113.38954611, -2162.04029486, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 40.49626647, 9.29e-05, 121.4887994, 0.00027869, 404.96266468, 0.00092896, -40.49626647, -9.29e-05, -121.4887994, -0.00027869, -404.96266468, -0.00092896, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 23.9, 10.2, 6.0)
    ops.node(123023, 23.9, 10.2, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 26109851.63553866, 10879104.84814111, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 117.5920463, 0.00102868, 141.60875545, 0.00778913, 14.16087554, 0.03575955, -117.5920463, -0.00102868, -141.60875545, -0.00778913, -14.16087554, -0.03575955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 133.77894267, 0.00102868, 161.10162356, 0.00778913, 16.11016236, 0.03575955, -133.77894267, -0.00102868, -161.10162356, -0.00778913, -16.11016236, -0.03575955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 143.07239273, 0.0205736, 143.07239273, 0.0617208, 100.15067491, -2001.04420895, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 35.76809818, 9.34e-05, 107.30429455, 0.0002802, 357.68098183, 0.000934, -35.76809818, -9.34e-05, -107.30429455, -0.0002802, -357.68098183, -0.000934, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 143.07239273, 0.0205736, 143.07239273, 0.0617208, 100.15067491, -2001.04420895, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 35.76809818, 9.34e-05, 107.30429455, 0.0002802, 357.68098183, 0.000934, -35.76809818, -9.34e-05, -107.30429455, -0.0002802, -357.68098183, -0.000934, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 28.1, 10.2, 6.05)
    ops.node(123024, 28.1, 10.2, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 30098005.68731456, 12540835.70304773, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 52.88655389, 0.00143608, 63.16252465, 0.01084149, 6.31625247, 0.04909613, -52.88655389, -0.00143608, -63.16252465, -0.01084149, -6.31625247, -0.04909613, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 52.88655389, 0.00143608, 63.16252465, 0.01084149, 6.31625247, 0.04909613, -52.88655389, -0.00143608, -63.16252465, -0.01084149, -6.31625247, -0.04909613, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 108.73900706, 0.02872156, 108.73900706, 0.08616469, 76.11730494, -1728.56862647, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 27.18475176, 0.0001207, 81.55425529, 0.00036209, 271.84751765, 0.00120697, -27.18475176, -0.0001207, -81.55425529, -0.00036209, -271.84751765, -0.00120697, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 108.73900706, 0.02872156, 108.73900706, 0.08616469, 76.11730494, -1728.56862647, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 27.18475176, 0.0001207, 81.55425529, 0.00036209, 271.84751765, 0.00120697, -27.18475176, -0.0001207, -81.55425529, -0.00036209, -271.84751765, -0.00120697, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172025, 0.0, 15.3, 6.05)
    ops.node(123025, 0.0, 15.3, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2025, 172025, 123025, 0.0625, 28852692.34581239, 12021955.1440885, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22025, 44.7652665, 0.00126905, 53.95483461, 0.01095766, 5.39548346, 0.05620328, -44.7652665, -0.00126905, -53.95483461, -0.01095766, -5.39548346, -0.05620328, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12025, 44.7652665, 0.00126905, 53.95483461, 0.01095766, 5.39548346, 0.05620328, -44.7652665, -0.00126905, -53.95483461, -0.01095766, -5.39548346, -0.05620328, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22025, 2025, 0.0, 93.99836809, 0.02538097, 93.99836809, 0.07614291, 65.79885766, -1621.30170146, 0.05, 2, 0, 72025, 23025, 2, 3)
    ops.uniaxialMaterial('LimitState', 42025, 23.49959202, 0.00010884, 70.49877607, 0.00032652, 234.99592022, 0.00108839, -23.49959202, -0.00010884, -70.49877607, -0.00032652, -234.99592022, -0.00108839, 0.4, 0.3, 0.003, 0.0, 0.0, 22025, 2)
    ops.limitCurve('ThreePoint', 12025, 2025, 0.0, 93.99836809, 0.02538097, 93.99836809, 0.07614291, 65.79885766, -1621.30170146, 0.05, 2, 0, 72025, 23025, 1, 3)
    ops.uniaxialMaterial('LimitState', 32025, 23.49959202, 0.00010884, 70.49877607, 0.00032652, 234.99592022, 0.00108839, -23.49959202, -0.00010884, -70.49877607, -0.00032652, -234.99592022, -0.00108839, 0.4, 0.3, 0.003, 0.0, 0.0, 12025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2025, 99999, 'P', 42025, 'Vy', 32025, 'Vz', 22025, 'My', 12025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172025, 72025, 172025, 2025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123025, 123025, 23025, 2025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172026, 4.2, 15.3, 6.0)
    ops.node(123026, 4.2, 15.3, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2026, 172026, 123026, 0.0625, 29338774.27776011, 12224489.28240005, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22026, 59.94538715, 0.00131718, 71.69667131, 0.00916767, 7.16966713, 0.04658742, -59.94538715, -0.00131718, -71.69667131, -0.00916767, -7.16966713, -0.04658742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12026, 65.1359919, 0.00131718, 77.90480676, 0.00916767, 7.79048068, 0.04658742, -65.1359919, -0.00131718, -77.90480676, -0.00916767, -7.79048068, -0.04658742, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22026, 2026, 0.0, 89.61375318, 0.02634366, 89.61375318, 0.07903098, 62.72962722, -1415.20313592, 0.05, 2, 0, 72026, 23026, 2, 3)
    ops.uniaxialMaterial('LimitState', 42026, 22.40343829, 0.00010204, 67.21031488, 0.00030613, 224.03438294, 0.00102043, -22.40343829, -0.00010204, -67.21031488, -0.00030613, -224.03438294, -0.00102043, 0.4, 0.3, 0.003, 0.0, 0.0, 22026, 2)
    ops.limitCurve('ThreePoint', 12026, 2026, 0.0, 89.61375318, 0.02634366, 89.61375318, 0.07903098, 62.72962722, -1415.20313592, 0.05, 2, 0, 72026, 23026, 1, 3)
    ops.uniaxialMaterial('LimitState', 32026, 22.40343829, 0.00010204, 67.21031488, 0.00030613, 224.03438294, 0.00102043, -22.40343829, -0.00010204, -67.21031488, -0.00030613, -224.03438294, -0.00102043, 0.4, 0.3, 0.003, 0.0, 0.0, 12026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2026, 99999, 'P', 42026, 'Vy', 32026, 'Vz', 22026, 'My', 12026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172026, 72026, 172026, 2026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123026, 123026, 23026, 2026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172027, 8.4, 15.3, 6.0)
    ops.node(123027, 8.4, 15.3, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2027, 172027, 123027, 0.0625, 28975582.9105846, 12073159.54607692, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22027, 60.15483439, 0.00149162, 71.95970235, 0.00968471, 7.19597023, 0.04619298, -60.15483439, -0.00149162, -71.95970235, -0.00968471, -7.19597023, -0.04619298, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12027, 64.47169799, 0.00149162, 77.12371324, 0.00968471, 7.71237132, 0.04619298, -64.47169799, -0.00149162, -77.12371324, -0.00968471, -7.71237132, -0.04619298, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22027, 2027, 0.0, 99.20082431, 0.02983247, 99.20082431, 0.08949741, 69.44057702, -1525.78520091, 0.05, 2, 0, 72027, 23027, 2, 3)
    ops.uniaxialMaterial('LimitState', 42027, 24.80020608, 0.00011438, 74.40061823, 0.00034313, 248.00206078, 0.00114376, -24.80020608, -0.00011438, -74.40061823, -0.00034313, -248.00206078, -0.00114376, 0.4, 0.3, 0.003, 0.0, 0.0, 22027, 2)
    ops.limitCurve('ThreePoint', 12027, 2027, 0.0, 99.20082431, 0.02983247, 99.20082431, 0.08949741, 69.44057702, -1525.78520091, 0.05, 2, 0, 72027, 23027, 1, 3)
    ops.uniaxialMaterial('LimitState', 32027, 24.80020608, 0.00011438, 74.40061823, 0.00034313, 248.00206078, 0.00114376, -24.80020608, -0.00011438, -74.40061823, -0.00034313, -248.00206078, -0.00114376, 0.4, 0.3, 0.003, 0.0, 0.0, 12027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2027, 99999, 'P', 42027, 'Vy', 32027, 'Vz', 22027, 'My', 12027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172027, 72027, 172027, 2027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123027, 123027, 23027, 2027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172028, 12.6, 15.3, 5.975)
    ops.node(123028, 12.6, 15.3, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2028, 172028, 123028, 0.0625, 28684934.03595847, 11952055.84831603, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22028, 68.18829623, 0.00136907, 81.85046876, 0.01052388, 8.18504688, 0.04478399, -68.18829623, -0.00136907, -81.85046876, -0.01052388, -8.18504688, -0.04478399, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12028, 68.18829623, 0.00136907, 81.85046876, 0.01052388, 8.18504688, 0.04478399, -68.18829623, -0.00136907, -81.85046876, -0.01052388, -8.18504688, -0.04478399, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22028, 2028, 0.0, 61.63952152, 0.02738139, 61.63952152, 0.08214418, 43.14766507, -1216.27394891, 0.05, 2, 0, 72028, 23028, 2, 3)
    ops.uniaxialMaterial('LimitState', 42028, 15.40988038, 7.179e-05, 46.22964114, 0.00021537, 154.0988038, 0.00071789, -15.40988038, -7.179e-05, -46.22964114, -0.00021537, -154.0988038, -0.00071789, 0.4, 0.3, 0.003, 0.0, 0.0, 22028, 2)
    ops.limitCurve('ThreePoint', 12028, 2028, 0.0, 61.63952152, 0.02738139, 61.63952152, 0.08214418, 43.14766507, -1216.27394891, 0.05, 2, 0, 72028, 23028, 1, 3)
    ops.uniaxialMaterial('LimitState', 32028, 15.40988038, 7.179e-05, 46.22964114, 0.00021537, 154.0988038, 0.00071789, -15.40988038, -7.179e-05, -46.22964114, -0.00021537, -154.0988038, -0.00071789, 0.4, 0.3, 0.003, 0.0, 0.0, 12028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2028, 99999, 'P', 42028, 'Vy', 32028, 'Vz', 22028, 'My', 12028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172028, 72028, 172028, 2028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123028, 123028, 23028, 2028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172029, 15.5, 15.3, 5.975)
    ops.node(123029, 15.5, 15.3, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2029, 172029, 123029, 0.0625, 29578212.84340128, 12324255.3514172, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22029, 66.53846079, 0.00140045, 79.81101687, 0.01038818, 7.98110169, 0.0464489, -66.53846079, -0.00140045, -79.81101687, -0.01038818, -7.98110169, -0.0464489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12029, 66.53846079, 0.00140045, 79.81101687, 0.01038818, 7.98110169, 0.0464489, -66.53846079, -0.00140045, -79.81101687, -0.01038818, -7.98110169, -0.0464489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22029, 2029, 0.0, 59.22921619, 0.02800903, 59.22921619, 0.08402708, 41.46045133, -1183.05015351, 0.05, 2, 0, 72029, 23029, 2, 3)
    ops.uniaxialMaterial('LimitState', 42029, 14.80730405, 6.69e-05, 44.42191214, 0.00020069, 148.07304046, 0.00066898, -14.80730405, -6.69e-05, -44.42191214, -0.00020069, -148.07304046, -0.00066898, 0.4, 0.3, 0.003, 0.0, 0.0, 22029, 2)
    ops.limitCurve('ThreePoint', 12029, 2029, 0.0, 59.22921619, 0.02800903, 59.22921619, 0.08402708, 41.46045133, -1183.05015351, 0.05, 2, 0, 72029, 23029, 1, 3)
    ops.uniaxialMaterial('LimitState', 32029, 14.80730405, 6.69e-05, 44.42191214, 0.00020069, 148.07304046, 0.00066898, -14.80730405, -6.69e-05, -44.42191214, -0.00020069, -148.07304046, -0.00066898, 0.4, 0.3, 0.003, 0.0, 0.0, 12029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2029, 99999, 'P', 42029, 'Vy', 32029, 'Vz', 22029, 'My', 12029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172029, 72029, 172029, 2029, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123029, 123029, 23029, 2029, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172030, 19.7, 15.3, 6.0)
    ops.node(123030, 19.7, 15.3, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2030, 172030, 123030, 0.0625, 32946150.86175956, 13727562.85906648, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22030, 62.03425034, 0.00140164, 73.79823916, 0.0100075, 7.37982392, 0.05509843, -62.03425034, -0.00140164, -73.79823916, -0.0100075, -7.37982392, -0.05509843, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12030, 66.91936226, 0.00140164, 79.60974903, 0.0100075, 7.9609749, 0.05509843, -66.91936226, -0.00140164, -79.60974903, -0.0100075, -7.9609749, -0.05509843, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22030, 2030, 0.0, 106.69260886, 0.0280329, 106.69260886, 0.0840987, 74.6848262, -1500.97119501, 0.05, 2, 0, 72030, 23030, 2, 3)
    ops.uniaxialMaterial('LimitState', 42030, 26.67315222, 0.00010819, 80.01945665, 0.00032456, 266.73152216, 0.00108188, -26.67315222, -0.00010819, -80.01945665, -0.00032456, -266.73152216, -0.00108188, 0.4, 0.3, 0.003, 0.0, 0.0, 22030, 2)
    ops.limitCurve('ThreePoint', 12030, 2030, 0.0, 106.69260886, 0.0280329, 106.69260886, 0.0840987, 74.6848262, -1500.97119501, 0.05, 2, 0, 72030, 23030, 1, 3)
    ops.uniaxialMaterial('LimitState', 32030, 26.67315222, 0.00010819, 80.01945665, 0.00032456, 266.73152216, 0.00108188, -26.67315222, -0.00010819, -80.01945665, -0.00032456, -266.73152216, -0.00108188, 0.4, 0.3, 0.003, 0.0, 0.0, 12030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2030, 99999, 'P', 42030, 'Vy', 32030, 'Vz', 22030, 'My', 12030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172030, 72030, 172030, 2030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123030, 123030, 23030, 2030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172031, 23.9, 15.3, 6.0)
    ops.node(123031, 23.9, 15.3, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2031, 172031, 123031, 0.0625, 27293166.79645327, 11372152.83185553, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22031, 59.69005656, 0.00139225, 71.38810473, 0.01073001, 7.13881047, 0.04266647, -59.69005656, -0.00139225, -71.38810473, -0.01073001, -7.13881047, -0.04266647, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12031, 64.65271053, 0.00139225, 77.32333887, 0.01073001, 7.73233389, 0.04266647, -64.65271053, -0.00139225, -77.32333887, -0.01073001, -7.73233389, -0.04266647, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22031, 2031, 0.0, 101.14390238, 0.02784494, 101.14390238, 0.08353481, 70.80073167, -1692.28118738, 0.05, 2, 0, 72031, 23031, 2, 3)
    ops.uniaxialMaterial('LimitState', 42031, 25.2859756, 0.0001238, 75.85792679, 0.00037141, 252.85975595, 0.00123804, -25.2859756, -0.0001238, -75.85792679, -0.00037141, -252.85975595, -0.00123804, 0.4, 0.3, 0.003, 0.0, 0.0, 22031, 2)
    ops.limitCurve('ThreePoint', 12031, 2031, 0.0, 101.14390238, 0.02784494, 101.14390238, 0.08353481, 70.80073167, -1692.28118738, 0.05, 2, 0, 72031, 23031, 1, 3)
    ops.uniaxialMaterial('LimitState', 32031, 25.2859756, 0.0001238, 75.85792679, 0.00037141, 252.85975595, 0.00123804, -25.2859756, -0.0001238, -75.85792679, -0.00037141, -252.85975595, -0.00123804, 0.4, 0.3, 0.003, 0.0, 0.0, 12031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2031, 99999, 'P', 42031, 'Vy', 32031, 'Vz', 22031, 'My', 12031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172031, 72031, 172031, 2031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123031, 123031, 23031, 2031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172032, 28.1, 15.3, 6.05)
    ops.node(123032, 28.1, 15.3, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2032, 172032, 123032, 0.0625, 28507066.29469013, 11877944.28945422, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22032, 43.40732219, 0.00130199, 52.33791863, 0.01124807, 5.23379186, 0.05577295, -43.40732219, -0.00130199, -52.33791863, -0.01124807, -5.23379186, -0.05577295, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12032, 43.40732219, 0.00130199, 52.33791863, 0.01124807, 5.23379186, 0.05577295, -43.40732219, -0.00130199, -52.33791863, -0.01124807, -5.23379186, -0.05577295, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22032, 2032, 0.0, 93.19902182, 0.02603985, 93.19902182, 0.07811954, 65.23931527, -1615.91489797, 0.05, 2, 0, 72032, 23032, 2, 3)
    ops.uniaxialMaterial('LimitState', 42032, 23.29975546, 0.00010922, 69.89926637, 0.00032767, 232.99755455, 0.00109222, -23.29975546, -0.00010922, -69.89926637, -0.00032767, -232.99755455, -0.00109222, 0.4, 0.3, 0.003, 0.0, 0.0, 22032, 2)
    ops.limitCurve('ThreePoint', 12032, 2032, 0.0, 93.19902182, 0.02603985, 93.19902182, 0.07811954, 65.23931527, -1615.91489797, 0.05, 2, 0, 72032, 23032, 1, 3)
    ops.uniaxialMaterial('LimitState', 32032, 23.29975546, 0.00010922, 69.89926637, 0.00032767, 232.99755455, 0.00109222, -23.29975546, -0.00010922, -69.89926637, -0.00032767, -232.99755455, -0.00109222, 0.4, 0.3, 0.003, 0.0, 0.0, 12032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2032, 99999, 'P', 42032, 'Vy', 32032, 'Vz', 22032, 'My', 12032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172032, 72032, 172032, 2032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123032, 123032, 23032, 2032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.95)
    ops.node(124001, 0.0, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26457465.97396301, 11023944.15581792, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 30.71268986, 0.0012016, 37.50741665, 0.01334049, 3.75074167, 0.06959425, -30.71268986, -0.0012016, -37.50741665, -0.01334049, -3.75074167, -0.06959425, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 30.71268986, 0.0012016, 37.50741665, 0.01334049, 3.75074167, 0.06959425, -30.71268986, -0.0012016, -37.50741665, -0.01334049, -3.75074167, -0.06959425, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 80.98432042, 0.02403206, 80.98432042, 0.07209618, 56.6890243, -2585.51340269, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 20.24608011, 0.00010226, 60.73824032, 0.00030678, 202.46080106, 0.00102259, -20.24608011, -0.00010226, -60.73824032, -0.00030678, -202.46080106, -0.00102259, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 80.98432042, 0.02403206, 80.98432042, 0.07209618, 56.6890243, -2585.51340269, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 20.24608011, 0.00010226, 60.73824032, 0.00030678, 202.46080106, 0.00102259, -20.24608011, -0.00010226, -60.73824032, -0.00030678, -202.46080106, -0.00102259, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.2, 0.0, 8.925)
    ops.node(124002, 4.2, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 30497822.19991756, 12707425.91663232, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 44.10350529, 0.00134961, 53.24495533, 0.01295725, 5.32449553, 0.06767527, -44.10350529, -0.00134961, -53.24495533, -0.01295725, -5.32449553, -0.06767527, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 47.86384744, 0.00134961, 57.78471352, 0.01295725, 5.77847135, 0.06767527, -47.86384744, -0.00134961, -57.78471352, -0.01295725, -5.77847135, -0.06767527, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 94.56349304, 0.02699222, 94.56349304, 0.08097665, 66.19444513, -1991.19449607, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 23.64087326, 0.00010359, 70.92261978, 0.00031076, 236.40873261, 0.00103587, -23.64087326, -0.00010359, -70.92261978, -0.00031076, -236.40873261, -0.00103587, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 94.56349304, 0.02699222, 94.56349304, 0.08097665, 66.19444513, -1991.19449607, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 23.64087326, 0.00010359, 70.92261978, 0.00031076, 236.40873261, 0.00103587, -23.64087326, -0.00010359, -70.92261978, -0.00031076, -236.40873261, -0.00103587, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.4, 0.0, 8.925)
    ops.node(124003, 8.4, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0625, 30074904.86349335, 12531210.3597889, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 55.3818554, 0.00136678, 66.92466463, 0.01174305, 6.69246646, 0.05872911, -55.3818554, -0.00136678, -66.92466463, -0.01174305, -6.69246646, -0.05872911, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 55.3818554, 0.00136678, 66.92466463, 0.01174305, 6.69246646, 0.05872911, -55.3818554, -0.00136678, -66.92466463, -0.01174305, -6.69246646, -0.05872911, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 60.08564584, 0.02733562, 60.08564584, 0.08200685, 42.05995209, -1341.39329304, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 15.02141146, 6.674e-05, 45.06423438, 0.00020023, 150.21411461, 0.00066745, -15.02141146, -6.674e-05, -45.06423438, -0.00020023, -150.21411461, -0.00066745, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 60.08564584, 0.02733562, 60.08564584, 0.08200685, 42.05995209, -1341.39329304, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 15.02141146, 6.674e-05, 45.06423438, 0.00020023, 150.21411461, 0.00066745, -15.02141146, -6.674e-05, -45.06423438, -0.00020023, -150.21411461, -0.00066745, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 19.7, 0.0, 8.925)
    ops.node(124006, 19.7, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 27992140.07958784, 11663391.69982827, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 52.47707351, 0.00141347, 63.6542251, 0.01326243, 6.36542251, 0.05764072, -52.47707351, -0.00141347, -63.6542251, -0.01326243, -6.36542251, -0.05764072, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 52.47707351, 0.00141347, 63.6542251, 0.01326243, 6.36542251, 0.05764072, -52.47707351, -0.00141347, -63.6542251, -0.01326243, -6.36542251, -0.05764072, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 72.83194444, 0.02826942, 72.83194444, 0.08480825, 50.98236111, -1526.27604391, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 18.20798611, 8.692e-05, 54.62395833, 0.00026077, 182.07986111, 0.00086923, -18.20798611, -8.692e-05, -54.62395833, -0.00026077, -182.07986111, -0.00086923, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 72.83194444, 0.02826942, 72.83194444, 0.08480825, 50.98236111, -1526.27604391, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 18.20798611, 8.692e-05, 54.62395833, 0.00026077, 182.07986111, 0.00086923, -18.20798611, -8.692e-05, -54.62395833, -0.00026077, -182.07986111, -0.00086923, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 23.9, 0.0, 8.925)
    ops.node(124007, 23.9, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 28983819.67279368, 12076591.5303307, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 44.21087649, 0.00136885, 53.54146095, 0.0106659, 5.3541461, 0.0633803, -44.21087649, -0.00136885, -53.54146095, -0.0106659, -5.3541461, -0.0633803, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 48.03204412, 0.00136885, 58.16907556, 0.0106659, 5.81690756, 0.0633803, -48.03204412, -0.00136885, -58.16907556, -0.0106659, -5.81690756, -0.0633803, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 77.98210137, 0.02737695, 77.98210137, 0.08213085, 54.58747096, -1605.92937813, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 19.49552534, 8.989e-05, 58.48657603, 0.00026966, 194.95525342, 0.00089886, -19.49552534, -8.989e-05, -58.48657603, -0.00026966, -194.95525342, -0.00089886, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 77.98210137, 0.02737695, 77.98210137, 0.08213085, 54.58747096, -1605.92937813, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 19.49552534, 8.989e-05, 58.48657603, 0.00026966, 194.95525342, 0.00089886, -19.49552534, -8.989e-05, -58.48657603, -0.00026966, -194.95525342, -0.00089886, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 28.1, 0.0, 8.95)
    ops.node(124008, 28.1, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 30008327.53956894, 12503469.80815372, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 32.80830581, 0.00119684, 39.78324838, 0.0120181, 3.97832484, 0.07172925, -32.80830581, -0.00119684, -39.78324838, -0.0120181, -3.97832484, -0.07172925, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 32.80830581, 0.00119684, 39.78324838, 0.0120181, 3.97832484, 0.07172925, -32.80830581, -0.00119684, -39.78324838, -0.0120181, -3.97832484, -0.07172925, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 85.92449236, 0.02393689, 85.92449236, 0.07181067, 60.14714465, -2464.46290508, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 21.48112309, 9.566e-05, 64.44336927, 0.00028698, 214.81123091, 0.00095659, -21.48112309, -9.566e-05, -64.44336927, -0.00028698, -214.81123091, -0.00095659, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 85.92449236, 0.02393689, 85.92449236, 0.07181067, 60.14714465, -2464.46290508, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 21.48112309, 9.566e-05, 64.44336927, 0.00028698, 214.81123091, 0.00095659, -21.48112309, -9.566e-05, -64.44336927, -0.00028698, -214.81123091, -0.00095659, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 5.1, 8.95)
    ops.node(124009, 0.0, 5.1, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 30094446.48642823, 12539352.70267843, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 36.73524089, 0.00123595, 44.38239687, 0.01055038, 4.43823969, 0.06450141, -36.73524089, -0.00123595, -44.38239687, -0.01055038, -4.43823969, -0.06450141, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 36.73524089, 0.00123595, 44.38239687, 0.01055038, 4.43823969, 0.06450141, -36.73524089, -0.00123595, -44.38239687, -0.01055038, -4.43823969, -0.06450141, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 82.26036782, 0.02471891, 82.26036782, 0.07415673, 57.58225748, -1595.63214216, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 20.56509196, 9.132e-05, 61.69527587, 0.00027395, 205.65091956, 0.00091318, -20.56509196, -9.132e-05, -61.69527587, -0.00027395, -205.65091956, -0.00091318, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 82.26036782, 0.02471891, 82.26036782, 0.07415673, 57.58225748, -1595.63214216, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 20.56509196, 9.132e-05, 61.69527587, 0.00027395, 205.65091956, 0.00091318, -20.56509196, -9.132e-05, -61.69527587, -0.00027395, -205.65091956, -0.00091318, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 4.2, 5.1, 8.925)
    ops.node(124010, 4.2, 5.1, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 27721636.42604771, 11550681.84418655, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 112.73467276, 0.00096974, 136.95045404, 0.0098574, 13.6950454, 0.04540638, -112.73467276, -0.00096974, -136.95045404, -0.0098574, -13.6950454, -0.04540638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 105.81003562, 0.00096974, 128.5383819, 0.0098574, 12.85383819, 0.04540638, -105.81003562, -0.00096974, -128.5383819, -0.0098574, -12.85383819, -0.04540638, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 123.02686892, 0.0193948, 123.02686892, 0.05818441, 86.11880825, -1643.47156767, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 30.75671723, 7.564e-05, 92.27015169, 0.00022693, 307.56717231, 0.00075644, -30.75671723, -7.564e-05, -92.27015169, -0.00022693, -307.56717231, -0.00075644, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 123.02686892, 0.0193948, 123.02686892, 0.05818441, 86.11880825, -1643.47156767, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 30.75671723, 7.564e-05, 92.27015169, 0.00022693, 307.56717231, 0.00075644, -30.75671723, -7.564e-05, -92.27015169, -0.00022693, -307.56717231, -0.00075644, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.4, 5.1, 8.925)
    ops.node(124011, 8.4, 5.1, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 31511334.20911921, 13129722.58713301, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 114.41561489, 0.00094008, 137.88282436, 0.01009541, 13.78828244, 0.04878929, -114.41561489, -0.00094008, -137.88282436, -0.01009541, -13.78828244, -0.04878929, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 107.31970503, 0.00094008, 129.33150824, 0.01009541, 12.93315082, 0.04878929, -107.31970503, -0.00094008, -129.33150824, -0.01009541, -12.93315082, -0.04878929, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 138.24105119, 0.01880169, 138.24105119, 0.05640508, 96.76873584, -1693.48910113, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 34.5602628, 7.478e-05, 103.6807884, 0.00022433, 345.60262799, 0.00074776, -34.5602628, -7.478e-05, -103.6807884, -0.00022433, -345.60262799, -0.00074776, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 138.24105119, 0.01880169, 138.24105119, 0.05640508, 96.76873584, -1693.48910113, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 34.5602628, 7.478e-05, 103.6807884, 0.00022433, 345.60262799, 0.00074776, -34.5602628, -7.478e-05, -103.6807884, -0.00022433, -345.60262799, -0.00074776, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 12.6, 5.1, 8.9)
    ops.node(124012, 12.6, 5.1, 11.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 30731220.86119926, 12804675.35883303, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 126.39068188, 0.00096592, 152.7148152, 0.00866905, 15.27148152, 0.04075423, -126.39068188, -0.00096592, -152.7148152, -0.00866905, -15.27148152, -0.04075423, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 126.39068188, 0.00096592, 152.7148152, 0.00866905, 15.27148152, 0.04075423, -126.39068188, -0.00096592, -152.7148152, -0.00866905, -15.27148152, -0.04075423, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 99.70262725, 0.01931836, 99.70262725, 0.05795509, 69.79183908, -1252.76441729, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 24.92565681, 5.53e-05, 74.77697044, 0.0001659, 249.25656813, 0.00055299, -24.92565681, -5.53e-05, -74.77697044, -0.0001659, -249.25656813, -0.00055299, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 99.70262725, 0.01931836, 99.70262725, 0.05795509, 69.79183908, -1252.76441729, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 24.92565681, 5.53e-05, 74.77697044, 0.0001659, 249.25656813, 0.00055299, -24.92565681, -5.53e-05, -74.77697044, -0.0001659, -249.25656813, -0.00055299, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 15.5, 5.1, 8.9)
    ops.node(124013, 15.5, 5.1, 11.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.1225, 27464014.03053401, 11443339.17938917, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 122.77451115, 0.00104331, 149.32926069, 0.00887974, 14.93292607, 0.03877667, -122.77451115, -0.00104331, -149.32926069, -0.00887974, -14.93292607, -0.03877667, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 122.77451115, 0.00104331, 149.32926069, 0.00887974, 14.93292607, 0.03877667, -122.77451115, -0.00104331, -149.32926069, -0.00887974, -14.93292607, -0.03877667, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 88.3898486, 0.02086615, 88.3898486, 0.06259846, 61.87289402, -1217.72177619, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 22.09746215, 5.486e-05, 66.29238645, 0.00016457, 220.9746215, 0.00054857, -22.09746215, -5.486e-05, -66.29238645, -0.00016457, -220.9746215, -0.00054857, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 88.3898486, 0.02086615, 88.3898486, 0.06259846, 61.87289402, -1217.72177619, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 22.09746215, 5.486e-05, 66.29238645, 0.00016457, 220.9746215, 0.00054857, -22.09746215, -5.486e-05, -66.29238645, -0.00016457, -220.9746215, -0.00054857, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 19.7, 5.1, 8.925)
    ops.node(124014, 19.7, 5.1, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1225, 31394325.75117134, 13080969.06298806, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 111.32214952, 0.0009131, 134.19759566, 0.01049179, 13.41975957, 0.04910893, -111.32214952, -0.0009131, -134.19759566, -0.01049179, -13.41975957, -0.04910893, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 104.42966798, 0.0009131, 125.8887869, 0.01049179, 12.58887869, 0.04910893, -104.42966798, -0.0009131, -125.8887869, -0.01049179, -12.58887869, -0.04910893, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 140.52249546, 0.01826203, 140.52249546, 0.0547861, 98.36574682, -1801.28938686, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 35.13062386, 7.629e-05, 105.39187159, 0.00022888, 351.30623864, 0.00076294, -35.13062386, -7.629e-05, -105.39187159, -0.00022888, -351.30623864, -0.00076294, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 140.52249546, 0.01826203, 140.52249546, 0.0547861, 98.36574682, -1801.28938686, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 35.13062386, 7.629e-05, 105.39187159, 0.00022888, 351.30623864, 0.00076294, -35.13062386, -7.629e-05, -105.39187159, -0.00022888, -351.30623864, -0.00076294, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 23.9, 5.1, 8.925)
    ops.node(124015, 23.9, 5.1, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 30556854.34638626, 12732022.64432761, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 110.82843604, 0.00096649, 133.88992728, 0.01118152, 13.38899273, 0.04921642, -110.82843604, -0.00096649, -133.88992728, -0.01118152, -13.38899273, -0.04921642, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 104.4120485, 0.00096649, 126.13839985, 0.01118152, 12.61383999, 0.04921642, -104.4120485, -0.00096649, -126.13839985, -0.01118152, -12.61383999, -0.04921642, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 141.53779277, 0.01932981, 141.53779277, 0.05798944, 99.07645494, -1972.78934115, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 35.38444819, 7.895e-05, 106.15334458, 0.00023685, 353.84448192, 0.00078951, -35.38444819, -7.895e-05, -106.15334458, -0.00023685, -353.84448192, -0.00078951, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 141.53779277, 0.01932981, 141.53779277, 0.05798944, 99.07645494, -1972.78934115, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 35.38444819, 7.895e-05, 106.15334458, 0.00023685, 353.84448192, 0.00078951, -35.38444819, -7.895e-05, -106.15334458, -0.00023685, -353.84448192, -0.00078951, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 28.1, 5.1, 8.95)
    ops.node(124016, 28.1, 5.1, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 30862593.77642816, 12859414.07351173, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 35.09401372, 0.00140794, 42.32473069, 0.01177549, 4.23247307, 0.06667284, -35.09401372, -0.00140794, -42.32473069, -0.01177549, -4.23247307, -0.06667284, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 35.09401372, 0.00140794, 42.32473069, 0.01177549, 4.23247307, 0.06667284, -35.09401372, -0.00140794, -42.32473069, -0.01177549, -4.23247307, -0.06667284, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 93.28262931, 0.02815877, 93.28262931, 0.08447631, 65.29784052, -1854.88998392, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 23.32065733, 0.00010098, 69.96197199, 0.00030293, 233.20657328, 0.00100976, -23.32065733, -0.00010098, -69.96197199, -0.00030293, -233.20657328, -0.00100976, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 93.28262931, 0.02815877, 93.28262931, 0.08447631, 65.29784052, -1854.88998392, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 23.32065733, 0.00010098, 69.96197199, 0.00030293, 233.20657328, 0.00100976, -23.32065733, -0.00010098, -69.96197199, -0.00030293, -233.20657328, -0.00100976, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 10.2, 8.95)
    ops.node(124017, 0.0, 10.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 29544038.93459187, 12310016.22274661, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 38.56330322, 0.00128949, 46.65521416, 0.01183295, 4.66552142, 0.06542815, -38.56330322, -0.00128949, -46.65521416, -0.01183295, -4.66552142, -0.06542815, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 38.56330322, 0.00128949, 46.65521416, 0.01183295, 4.66552142, 0.06542815, -38.56330322, -0.00128949, -46.65521416, -0.01183295, -4.66552142, -0.06542815, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 91.13607878, 0.02578982, 91.13607878, 0.07736945, 63.79525515, -1912.61405499, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 22.78401969, 0.00010306, 68.35205908, 0.00030917, 227.84019695, 0.00103055, -22.78401969, -0.00010306, -68.35205908, -0.00030917, -227.84019695, -0.00103055, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 91.13607878, 0.02578982, 91.13607878, 0.07736945, 63.79525515, -1912.61405499, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 22.78401969, 0.00010306, 68.35205908, 0.00030917, 227.84019695, 0.00103055, -22.78401969, -0.00010306, -68.35205908, -0.00030917, -227.84019695, -0.00103055, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 4.2, 10.2, 8.925)
    ops.node(124018, 4.2, 10.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1225, 28027554.32497219, 11678147.63540508, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 101.42388541, 0.00098177, 123.18355355, 0.01032485, 12.31835535, 0.05149558, -101.42388541, -0.00098177, -123.18355355, -0.01032485, -12.31835535, -0.05149558, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 88.33559524, 0.00098177, 107.28727738, 0.01032485, 10.72872774, 0.05149558, -88.33559524, -0.00098177, -107.28727738, -0.01032485, -10.72872774, -0.05149558, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 139.23210713, 0.01963532, 139.23210713, 0.05890596, 97.46247499, -2317.42609577, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 34.80802678, 8.467e-05, 104.42408035, 0.00025402, 348.08026783, 0.00084674, -34.80802678, -8.467e-05, -104.42408035, -0.00025402, -348.08026783, -0.00084674, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 139.23210713, 0.01963532, 139.23210713, 0.05890596, 97.46247499, -2317.42609577, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 34.80802678, 8.467e-05, 104.42408035, 0.00025402, 348.08026783, 0.00084674, -34.80802678, -8.467e-05, -104.42408035, -0.00025402, -348.08026783, -0.00084674, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 8.4, 10.2, 8.925)
    ops.node(124019, 8.4, 10.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1225, 31913744.87390431, 13297393.69746013, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 105.19145429, 0.00092692, 126.64430021, 0.01023595, 12.66443002, 0.05483469, -105.19145429, -0.00092692, -126.64430021, -0.01023595, -12.66443002, -0.05483469, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 90.52662672, 0.00092692, 108.98871366, 0.01023595, 10.89887137, 0.05483469, -90.52662672, -0.00092692, -108.98871366, -0.01023595, -10.89887137, -0.05483469, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 158.13387411, 0.01853846, 158.13387411, 0.05561538, 110.69371188, -2532.46579522, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 39.53346853, 8.446e-05, 118.60040558, 0.00025337, 395.33468528, 0.00084458, -39.53346853, -8.446e-05, -118.60040558, -0.00025337, -395.33468528, -0.00084458, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 158.13387411, 0.01853846, 158.13387411, 0.05561538, 110.69371188, -2532.46579522, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 39.53346853, 8.446e-05, 118.60040558, 0.00025337, 395.33468528, 0.00084458, -39.53346853, -8.446e-05, -118.60040558, -0.00025337, -395.33468528, -0.00084458, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 12.6, 10.2, 8.9)
    ops.node(124020, 12.6, 10.2, 11.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 29764747.63168217, 12401978.17986757, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 38.98257972, 0.00133498, 47.0093937, 0.01175835, 4.70093937, 0.06133, -38.98257972, -0.00133498, -47.0093937, -0.01175835, -4.70093937, -0.06133, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 38.98257972, 0.00133498, 47.0093937, 0.01175835, 4.70093937, 0.06133, -38.98257972, -0.00133498, -47.0093937, -0.01175835, -4.70093937, -0.06133, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 94.9715251, 0.02669965, 94.9715251, 0.08009896, 66.48006757, -1726.56199642, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 23.74288127, 0.0001066, 71.22864382, 0.00031979, 237.42881275, 0.00106596, -23.74288127, -0.0001066, -71.22864382, -0.00031979, -237.42881275, -0.00106596, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 94.9715251, 0.02669965, 94.9715251, 0.08009896, 66.48006757, -1726.56199642, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 23.74288127, 0.0001066, 71.22864382, 0.00031979, 237.42881275, 0.00106596, -23.74288127, -0.0001066, -71.22864382, -0.00031979, -237.42881275, -0.00106596, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 15.5, 10.2, 8.9)
    ops.node(124021, 15.5, 10.2, 11.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 28663377.06654114, 11943073.77772548, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 40.90795875, 0.00127253, 49.41521211, 0.0123017, 4.94152121, 0.0599184, -40.90795875, -0.00127253, -49.41521211, -0.0123017, -4.94152121, -0.0599184, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 40.90795875, 0.00127253, 49.41521211, 0.0123017, 4.94152121, 0.0599184, -40.90795875, -0.00127253, -49.41521211, -0.0123017, -4.94152121, -0.0599184, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 94.68724852, 0.02545068, 94.68724852, 0.07635204, 66.28107397, -1807.50051276, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 23.67181213, 0.00011036, 71.01543639, 0.00033108, 236.71812131, 0.00110361, -23.67181213, -0.00011036, -71.01543639, -0.00033108, -236.71812131, -0.00110361, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 94.68724852, 0.02545068, 94.68724852, 0.07635204, 66.28107397, -1807.50051276, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 23.67181213, 0.00011036, 71.01543639, 0.00033108, 236.71812131, 0.00110361, -23.67181213, -0.00011036, -71.01543639, -0.00033108, -236.71812131, -0.00110361, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 19.7, 10.2, 8.925)
    ops.node(124022, 19.7, 10.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.1225, 28259953.11707816, 11774980.46544923, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 102.81859704, 0.00093245, 124.82971672, 0.01060472, 12.48297167, 0.0520307, -102.81859704, -0.00093245, -124.82971672, -0.01060472, -12.48297167, -0.0520307, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 88.42693694, 0.00093245, 107.35713, 0.01060472, 10.735713, 0.0520307, -88.42693694, -0.00093245, -107.35713, -0.01060472, -10.735713, -0.0520307, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 143.52240639, 0.018649, 143.52240639, 0.05594699, 100.46568447, -2480.43786688, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 35.8806016, 8.657e-05, 107.64180479, 0.0002597, 358.80601597, 0.00086565, -35.8806016, -8.657e-05, -107.64180479, -0.0002597, -358.80601597, -0.00086565, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 143.52240639, 0.018649, 143.52240639, 0.05594699, 100.46568447, -2480.43786688, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 35.8806016, 8.657e-05, 107.64180479, 0.0002597, 358.80601597, 0.00086565, -35.8806016, -8.657e-05, -107.64180479, -0.0002597, -358.80601597, -0.00086565, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 23.9, 10.2, 8.925)
    ops.node(124023, 23.9, 10.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 31857286.53821601, 13273869.39092334, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 103.5955916, 0.0009941, 124.74323974, 0.01095309, 12.47432397, 0.05551286, -103.5955916, -0.0009941, -124.74323974, -0.01095309, -12.47432397, -0.05551286, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 90.69583687, 0.0009941, 109.21017339, 0.01095309, 10.92101734, 0.05551286, -90.69583687, -0.0009941, -109.21017339, -0.01095309, -10.92101734, -0.05551286, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 161.08340053, 0.01988195, 161.08340053, 0.05964586, 112.75838037, -2687.91701444, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 40.27085013, 8.619e-05, 120.81255039, 0.00025856, 402.70850132, 0.00086186, -40.27085013, -8.619e-05, -120.81255039, -0.00025856, -402.70850132, -0.00086186, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 161.08340053, 0.01988195, 161.08340053, 0.05964586, 112.75838037, -2687.91701444, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 40.27085013, 8.619e-05, 120.81255039, 0.00025856, 402.70850132, 0.00086186, -40.27085013, -8.619e-05, -120.81255039, -0.00025856, -402.70850132, -0.00086186, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 28.1, 10.2, 8.95)
    ops.node(124024, 28.1, 10.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 28997101.49415643, 12082125.62256518, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 37.03450038, 0.00124374, 44.85233645, 0.0119291, 4.48523364, 0.06476368, -37.03450038, -0.00124374, -44.85233645, -0.0119291, -4.48523364, -0.06476368, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 37.03450038, 0.00124374, 44.85233645, 0.0119291, 4.48523364, 0.06476368, -37.03450038, -0.00124374, -44.85233645, -0.0119291, -4.48523364, -0.06476368, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 89.32089609, 0.0248748, 89.32089609, 0.0746244, 62.52462726, -1869.68977315, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 22.33022402, 0.00010291, 66.99067207, 0.00030872, 223.30224022, 0.00102908, -22.33022402, -0.00010291, -66.99067207, -0.00030872, -223.30224022, -0.00102908, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 89.32089609, 0.0248748, 89.32089609, 0.0746244, 62.52462726, -1869.68977315, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 22.33022402, 0.00010291, 66.99067207, 0.00030872, 223.30224022, 0.00102908, -22.33022402, -0.00010291, -66.99067207, -0.00030872, -223.30224022, -0.00102908, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173025, 0.0, 15.3, 8.95)
    ops.node(124025, 0.0, 15.3, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3025, 173025, 124025, 0.0625, 29529951.88257354, 12304146.61773898, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23025, 33.20499808, 0.00123014, 40.31154795, 0.01323868, 4.0311548, 0.07257532, -33.20499808, -0.00123014, -40.31154795, -0.01323868, -4.0311548, -0.07257532, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13025, 33.20499808, 0.00123014, 40.31154795, 0.01323868, 4.0311548, 0.07257532, -33.20499808, -0.00123014, -40.31154795, -0.01323868, -4.0311548, -0.07257532, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23025, 3025, 0.0, 88.5401629, 0.02460272, 88.5401629, 0.07380816, 61.97811403, -2767.83155501, 0.05, 2, 0, 73025, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 43025, 22.13504072, 0.00010017, 66.40512217, 0.0003005, 221.35040724, 0.00100168, -22.13504072, -0.00010017, -66.40512217, -0.0003005, -221.35040724, -0.00100168, 0.4, 0.3, 0.003, 0.0, 0.0, 23025, 2)
    ops.limitCurve('ThreePoint', 13025, 3025, 0.0, 88.5401629, 0.02460272, 88.5401629, 0.07380816, 61.97811403, -2767.83155501, 0.05, 2, 0, 73025, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 33025, 22.13504072, 0.00010017, 66.40512217, 0.0003005, 221.35040724, 0.00100168, -22.13504072, -0.00010017, -66.40512217, -0.0003005, -221.35040724, -0.00100168, 0.4, 0.3, 0.003, 0.0, 0.0, 13025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3025, 99999, 'P', 43025, 'Vy', 33025, 'Vz', 23025, 'My', 13025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173025, 73025, 173025, 3025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 3025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173026, 4.2, 15.3, 8.925)
    ops.node(124026, 4.2, 15.3, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3026, 173026, 124026, 0.0625, 29840476.87872986, 12433532.03280411, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23026, 45.35749113, 0.0012916, 54.83847699, 0.01209374, 5.4838477, 0.06598673, -45.35749113, -0.0012916, -54.83847699, -0.01209374, -5.4838477, -0.06598673, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13026, 49.85772131, 0.0012916, 60.2793813, 0.01209374, 6.02793813, 0.06598673, -49.85772131, -0.0012916, -60.2793813, -0.01209374, -6.02793813, -0.06598673, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23026, 3026, 0.0, 90.04110021, 0.02583202, 90.04110021, 0.07749606, 63.02877015, -1814.1187985, 0.05, 2, 0, 73026, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 43026, 22.51027505, 0.00010081, 67.53082516, 0.00030242, 225.10275053, 0.00100806, -22.51027505, -0.00010081, -67.53082516, -0.00030242, -225.10275053, -0.00100806, 0.4, 0.3, 0.003, 0.0, 0.0, 23026, 2)
    ops.limitCurve('ThreePoint', 13026, 3026, 0.0, 90.04110021, 0.02583202, 90.04110021, 0.07749606, 63.02877015, -1814.1187985, 0.05, 2, 0, 73026, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 33026, 22.51027505, 0.00010081, 67.53082516, 0.00030242, 225.10275053, 0.00100806, -22.51027505, -0.00010081, -67.53082516, -0.00030242, -225.10275053, -0.00100806, 0.4, 0.3, 0.003, 0.0, 0.0, 13026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3026, 99999, 'P', 43026, 'Vy', 33026, 'Vz', 23026, 'My', 13026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173026, 73026, 173026, 3026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 3026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173027, 8.4, 15.3, 8.925)
    ops.node(124027, 8.4, 15.3, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3027, 173027, 124027, 0.0625, 31053670.81572603, 12939029.50655251, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23027, 45.48832642, 0.00134718, 54.84310039, 0.01140509, 5.48431004, 0.06677169, -45.48832642, -0.00134718, -54.84310039, -0.01140509, -5.48431004, -0.06677169, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13027, 49.60987456, 0.00134718, 59.81225394, 0.01140509, 5.98122539, 0.06677169, -49.60987456, -0.00134718, -59.81225394, -0.01140509, -5.98122539, -0.06677169, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23027, 3027, 0.0, 89.90530563, 0.02694369, 89.90530563, 0.08083106, 62.93371394, -1686.32595147, 0.05, 2, 0, 73027, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 43027, 22.47632641, 9.672e-05, 67.42897922, 0.00029016, 224.76326407, 0.00096721, -22.47632641, -9.672e-05, -67.42897922, -0.00029016, -224.76326407, -0.00096721, 0.4, 0.3, 0.003, 0.0, 0.0, 23027, 2)
    ops.limitCurve('ThreePoint', 13027, 3027, 0.0, 89.90530563, 0.02694369, 89.90530563, 0.08083106, 62.93371394, -1686.32595147, 0.05, 2, 0, 73027, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 33027, 22.47632641, 9.672e-05, 67.42897922, 0.00029016, 224.76326407, 0.00096721, -22.47632641, -9.672e-05, -67.42897922, -0.00029016, -224.76326407, -0.00096721, 0.4, 0.3, 0.003, 0.0, 0.0, 13027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3027, 99999, 'P', 43027, 'Vy', 33027, 'Vz', 23027, 'My', 13027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173027, 73027, 173027, 3027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 3027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173028, 12.6, 15.3, 8.9)
    ops.node(124028, 12.6, 15.3, 11.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3028, 173028, 124028, 0.0625, 29911446.83995828, 12463102.84998262, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23028, 52.85786567, 0.00118664, 63.96851112, 0.01462533, 6.39685111, 0.06301502, -52.85786567, -0.00118664, -63.96851112, -0.01462533, -6.39685111, -0.06301502, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13028, 52.85786567, 0.00118664, 63.96851112, 0.01462533, 6.39685111, 0.06301502, -52.85786567, -0.00118664, -63.96851112, -0.01462533, -6.39685111, -0.06301502, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23028, 3028, 0.0, 82.90944159, 0.02373276, 82.90944159, 0.07119827, 58.03660911, -1777.85746942, 0.05, 2, 0, 73028, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 43028, 20.7273604, 9.26e-05, 62.18208119, 0.0002778, 207.27360397, 0.00092601, -20.7273604, -9.26e-05, -62.18208119, -0.0002778, -207.27360397, -0.00092601, 0.4, 0.3, 0.003, 0.0, 0.0, 23028, 2)
    ops.limitCurve('ThreePoint', 13028, 3028, 0.0, 82.90944159, 0.02373276, 82.90944159, 0.07119827, 58.03660911, -1777.85746942, 0.05, 2, 0, 73028, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 33028, 20.7273604, 9.26e-05, 62.18208119, 0.0002778, 207.27360397, 0.00092601, -20.7273604, -9.26e-05, -62.18208119, -0.0002778, -207.27360397, -0.00092601, 0.4, 0.3, 0.003, 0.0, 0.0, 13028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3028, 99999, 'P', 43028, 'Vy', 33028, 'Vz', 23028, 'My', 13028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173028, 73028, 173028, 3028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 3028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173029, 15.5, 15.3, 8.9)
    ops.node(124029, 15.5, 15.3, 11.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3029, 173029, 124029, 0.0625, 27762106.93672669, 11567544.55696946, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23029, 56.28997371, 0.00133626, 68.39902246, 0.01358551, 6.83990225, 0.05955482, -56.28997371, -0.00133626, -68.39902246, -0.01358551, -6.83990225, -0.05955482, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13029, 56.28997371, 0.00133626, 68.39902246, 0.01358551, 6.83990225, 0.05955482, -56.28997371, -0.00133626, -68.39902246, -0.01358551, -6.83990225, -0.05955482, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23029, 3029, 0.0, 69.96899512, 0.02672526, 69.96899512, 0.08017579, 48.97829658, -1659.37509751, 0.05, 2, 0, 73029, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 43029, 17.49224878, 8.42e-05, 52.47674634, 0.0002526, 174.92248779, 0.00084198, -17.49224878, -8.42e-05, -52.47674634, -0.0002526, -174.92248779, -0.00084198, 0.4, 0.3, 0.003, 0.0, 0.0, 23029, 2)
    ops.limitCurve('ThreePoint', 13029, 3029, 0.0, 69.96899512, 0.02672526, 69.96899512, 0.08017579, 48.97829658, -1659.37509751, 0.05, 2, 0, 73029, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 33029, 17.49224878, 8.42e-05, 52.47674634, 0.0002526, 174.92248779, 0.00084198, -17.49224878, -8.42e-05, -52.47674634, -0.0002526, -174.92248779, -0.00084198, 0.4, 0.3, 0.003, 0.0, 0.0, 13029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3029, 99999, 'P', 43029, 'Vy', 33029, 'Vz', 23029, 'My', 13029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173029, 73029, 173029, 3029, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 3029, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173030, 19.7, 15.3, 8.925)
    ops.node(124030, 19.7, 15.3, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3030, 173030, 124030, 0.0625, 29760943.88531344, 12400393.28554727, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23030, 46.99288289, 0.00129985, 56.82512791, 0.01175684, 5.68251279, 0.06554551, -46.99288289, -0.00129985, -56.82512791, -0.01175684, -5.68251279, -0.06554551, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13030, 51.9212679, 0.00129985, 62.78467096, 0.01175684, 6.2784671, 0.06554551, -51.9212679, -0.00129985, -62.78467096, -0.01175684, -6.2784671, -0.06554551, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23030, 3030, 0.0, 90.05778119, 0.02599708, 90.05778119, 0.07799125, 63.04044684, -1822.97086175, 0.05, 2, 0, 73030, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 43030, 22.5144453, 0.00010109, 67.5433359, 0.00030328, 225.14445299, 0.00101094, -22.5144453, -0.00010109, -67.5433359, -0.00030328, -225.14445299, -0.00101094, 0.4, 0.3, 0.003, 0.0, 0.0, 23030, 2)
    ops.limitCurve('ThreePoint', 13030, 3030, 0.0, 90.05778119, 0.02599708, 90.05778119, 0.07799125, 63.04044684, -1822.97086175, 0.05, 2, 0, 73030, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 33030, 22.5144453, 0.00010109, 67.5433359, 0.00030328, 225.14445299, 0.00101094, -22.5144453, -0.00010109, -67.5433359, -0.00030328, -225.14445299, -0.00101094, 0.4, 0.3, 0.003, 0.0, 0.0, 13030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3030, 99999, 'P', 43030, 'Vy', 33030, 'Vz', 23030, 'My', 13030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173030, 73030, 173030, 3030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 3030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173031, 23.9, 15.3, 8.925)
    ops.node(124031, 23.9, 15.3, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3031, 173031, 124031, 0.0625, 29304337.85267856, 12210140.7719494, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23031, 43.67847387, 0.00128038, 52.86527502, 0.01273158, 5.2865275, 0.06590139, -43.67847387, -0.00128038, -52.86527502, -0.01273158, -5.2865275, -0.06590139, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13031, 47.80791239, 0.00128038, 57.86324962, 0.01273158, 5.78632496, 0.06590139, -47.80791239, -0.00128038, -57.86324962, -0.01273158, -5.78632496, -0.06590139, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23031, 3031, 0.0, 89.47370236, 0.02560757, 89.47370236, 0.07682272, 62.63159165, -1837.59351105, 0.05, 2, 0, 73031, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 43031, 22.36842559, 0.000102, 67.10527677, 0.00030601, 223.6842559, 0.00102003, -22.36842559, -0.000102, -67.10527677, -0.00030601, -223.6842559, -0.00102003, 0.4, 0.3, 0.003, 0.0, 0.0, 23031, 2)
    ops.limitCurve('ThreePoint', 13031, 3031, 0.0, 89.47370236, 0.02560757, 89.47370236, 0.07682272, 62.63159165, -1837.59351105, 0.05, 2, 0, 73031, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 33031, 22.36842559, 0.000102, 67.10527677, 0.00030601, 223.6842559, 0.00102003, -22.36842559, -0.000102, -67.10527677, -0.00030601, -223.6842559, -0.00102003, 0.4, 0.3, 0.003, 0.0, 0.0, 13031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3031, 99999, 'P', 43031, 'Vy', 33031, 'Vz', 23031, 'My', 13031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173031, 73031, 173031, 3031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 3031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173032, 28.1, 15.3, 8.95)
    ops.node(124032, 28.1, 15.3, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3032, 173032, 124032, 0.0625, 29564452.73588933, 12318521.97328722, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23032, 32.02082322, 0.00114331, 38.87073258, 0.01192732, 3.88707326, 0.07129177, -32.02082322, -0.00114331, -38.87073258, -0.01192732, -3.88707326, -0.07129177, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13032, 32.02082322, 0.00114331, 38.87073258, 0.01192732, 3.88707326, 0.07129177, -32.02082322, -0.00114331, -38.87073258, -0.01192732, -3.88707326, -0.07129177, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23032, 3032, 0.0, 83.0379043, 0.02286625, 83.0379043, 0.06859876, 58.12653301, -2293.92119153, 0.05, 2, 0, 73032, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 43032, 20.75947608, 9.383e-05, 62.27842823, 0.0002815, 207.59476076, 0.00093833, -20.75947608, -9.383e-05, -62.27842823, -0.0002815, -207.59476076, -0.00093833, 0.4, 0.3, 0.003, 0.0, 0.0, 23032, 2)
    ops.limitCurve('ThreePoint', 13032, 3032, 0.0, 83.0379043, 0.02286625, 83.0379043, 0.06859876, 58.12653301, -2293.92119153, 0.05, 2, 0, 73032, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 33032, 20.75947608, 9.383e-05, 62.27842823, 0.0002815, 207.59476076, 0.00093833, -20.75947608, -9.383e-05, -62.27842823, -0.0002815, -207.59476076, -0.00093833, 0.4, 0.3, 0.003, 0.0, 0.0, 13032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3032, 99999, 'P', 43032, 'Vy', 33032, 'Vz', 23032, 'My', 13032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173032, 73032, 173032, 3032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 3032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.6, 0.0, 0.0)
    ops.node(124033, 12.6, 0.0, 1.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4085, 170004, 124033, 0.1225, 30287389.23523812, 12619745.51468255, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24085, 251.14419856, 0.00078428, 299.49804229, 0.01121279, 29.94980423, 0.03995881, -251.14419856, -0.00078428, -299.49804229, -0.01121279, -29.94980423, -0.03995881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14085, 225.69220659, 0.00078428, 269.14567177, 0.01121279, 26.91456718, 0.03995881, -225.69220659, -0.00078428, -269.14567177, -0.01121279, -26.91456718, -0.03995881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24085, 4085, 0.0, 234.84384596, 0.0156856, 234.84384596, 0.0470568, 164.39069217, -4467.68106651, 0.05, 2, 0, 70004, 24033, 2, 3)
    ops.uniaxialMaterial('LimitState', 44085, 58.71096149, 6.608e-05, 176.13288447, 0.00019825, 587.1096149, 0.00066082, -58.71096149, -6.608e-05, -176.13288447, -0.00019825, -587.1096149, -0.00066082, 0.4, 0.3, 0.003, 0.0, 0.0, 24085, 2)
    ops.limitCurve('ThreePoint', 14085, 4085, 0.0, 234.84384596, 0.0156856, 234.84384596, 0.0470568, 164.39069217, -4467.68106651, 0.05, 2, 0, 70004, 24033, 1, 3)
    ops.uniaxialMaterial('LimitState', 34085, 58.71096149, 6.608e-05, 176.13288447, 0.00019825, 587.1096149, 0.00066082, -58.71096149, -6.608e-05, -176.13288447, -0.00019825, -587.1096149, -0.00066082, 0.4, 0.3, 0.003, 0.0, 0.0, 14085, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4085, 99999, 'P', 44085, 'Vy', 34085, 'Vz', 24085, 'My', 14085, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4085, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124033, 124033, 24033, 4085, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174033, 12.6, 0.0, 1.7)
    ops.node(121004, 12.6, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4086, 174033, 121004, 0.1225, 28165173.87929891, 11735489.11637455, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24086, 175.3524877, 0.00074377, 209.6346126, 0.01020432, 20.96346126, 0.03617962, -175.3524877, -0.00074377, -209.6346126, -0.01020432, -20.96346126, -0.03617962, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14086, 161.50210888, 0.00074377, 193.07642836, 0.01020432, 19.30764284, 0.03617962, -161.50210888, -0.00074377, -193.07642836, -0.01020432, -19.30764284, -0.03617962, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24086, 4086, 0.0, 217.08257516, 0.01487542, 217.08257516, 0.04462627, 151.95780261, -4361.05996297, 0.05, 2, 0, 74033, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44086, 54.27064379, 6.569e-05, 162.81193137, 0.00019706, 542.7064379, 0.00065687, -54.27064379, -6.569e-05, -162.81193137, -0.00019706, -542.7064379, -0.00065687, 0.4, 0.3, 0.003, 0.0, 0.0, 24086, 2)
    ops.limitCurve('ThreePoint', 14086, 4086, 0.0, 217.08257516, 0.01487542, 217.08257516, 0.04462627, 151.95780261, -4361.05996297, 0.05, 2, 0, 74033, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34086, 54.27064379, 6.569e-05, 162.81193137, 0.00019706, 542.7064379, 0.00065687, -54.27064379, -6.569e-05, -162.81193137, -0.00019706, -542.7064379, -0.00065687, 0.4, 0.3, 0.003, 0.0, 0.0, 14086, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4086, 99999, 'P', 44086, 'Vy', 34086, 'Vz', 24086, 'My', 14086, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174033, 74033, 174033, 4086, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4086, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 15.5, 0.0, 0.0)
    ops.node(124034, 15.5, 0.0, 1.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4087, 170005, 124034, 0.1225, 27824764.82519826, 11593652.01049927, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24087, 258.01596568, 0.00077899, 307.78802846, 0.01207775, 30.77880285, 0.03580863, -258.01596568, -0.00077899, -307.78802846, -0.01207775, -30.77880285, -0.03580863, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14087, 229.39395666, 0.00077899, 273.64474703, 0.01207775, 27.3644747, 0.03580863, -229.39395666, -0.00077899, -273.64474703, -0.01207775, -27.3644747, -0.03580863, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24087, 4087, 0.0, 226.83784195, 0.01557983, 226.83784195, 0.0467395, 158.78648937, -4845.78491661, 0.05, 2, 0, 70005, 24034, 2, 3)
    ops.uniaxialMaterial('LimitState', 44087, 56.70946049, 6.948e-05, 170.12838147, 0.00020843, 567.09460488, 0.00069478, -56.70946049, -6.948e-05, -170.12838147, -0.00020843, -567.09460488, -0.00069478, 0.4, 0.3, 0.003, 0.0, 0.0, 24087, 2)
    ops.limitCurve('ThreePoint', 14087, 4087, 0.0, 226.83784195, 0.01557983, 226.83784195, 0.0467395, 158.78648937, -4845.78491661, 0.05, 2, 0, 70005, 24034, 1, 3)
    ops.uniaxialMaterial('LimitState', 34087, 56.70946049, 6.948e-05, 170.12838147, 0.00020843, 567.09460488, 0.00069478, -56.70946049, -6.948e-05, -170.12838147, -0.00020843, -567.09460488, -0.00069478, 0.4, 0.3, 0.003, 0.0, 0.0, 14087, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4087, 99999, 'P', 44087, 'Vy', 34087, 'Vz', 24087, 'My', 14087, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 4087, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124034, 124034, 24034, 4087, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174034, 15.5, 0.0, 1.7)
    ops.node(121005, 15.5, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4088, 174034, 121005, 0.1225, 27274279.87850375, 11364283.2827099, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24088, 175.81700631, 0.00073369, 210.10004019, 0.01136687, 21.01000402, 0.03539714, -175.81700631, -0.00073369, -210.10004019, -0.01136687, -21.01000402, -0.03539714, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14088, 161.3717043, 0.00073369, 192.83800965, 0.01136687, 19.28380096, 0.03539714, -161.3717043, -0.00073369, -192.83800965, -0.01136687, -19.28380096, -0.03539714, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24088, 4088, 0.0, 218.00954966, 0.01467374, 218.00954966, 0.04402123, 152.60668476, -4691.81683271, 0.05, 2, 0, 74034, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44088, 54.50238741, 6.812e-05, 163.50716224, 0.00020437, 545.02387414, 0.00068122, -54.50238741, -6.812e-05, -163.50716224, -0.00020437, -545.02387414, -0.00068122, 0.4, 0.3, 0.003, 0.0, 0.0, 24088, 2)
    ops.limitCurve('ThreePoint', 14088, 4088, 0.0, 218.00954966, 0.01467374, 218.00954966, 0.04402123, 152.60668476, -4691.81683271, 0.05, 2, 0, 74034, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34088, 54.50238741, 6.812e-05, 163.50716224, 0.00020437, 545.02387414, 0.00068122, -54.50238741, -6.812e-05, -163.50716224, -0.00020437, -545.02387414, -0.00068122, 0.4, 0.3, 0.003, 0.0, 0.0, 14088, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4088, 99999, 'P', 44088, 'Vy', 34088, 'Vz', 24088, 'My', 14088, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174034, 74034, 174034, 4088, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 4088, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.6, 0.0, 3.1)
    ops.node(124035, 12.6, 0.0, 4.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4090, 171004, 124035, 0.1225, 28312833.43157547, 11797013.92982311, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24090, 162.66764176, 0.0007512, 195.36045131, 0.01137143, 19.53604513, 0.04147414, -162.66764176, -0.0007512, -195.36045131, -0.01137143, -19.53604513, -0.04147414, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14090, 149.39477031, 0.0007512, 179.42000901, 0.01137143, 17.9420009, 0.04147414, -149.39477031, -0.0007512, -179.42000901, -0.01137143, -17.9420009, -0.04147414, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24090, 4090, 0.0, 208.91946577, 0.01502404, 208.91946577, 0.04507211, 146.24362604, -4246.87151407, 0.05, 2, 0, 71004, 24035, 2, 3)
    ops.uniaxialMaterial('LimitState', 44090, 52.22986644, 6.289e-05, 156.68959933, 0.00018866, 522.29866444, 0.00062887, -52.22986644, -6.289e-05, -156.68959933, -0.00018866, -522.29866444, -0.00062887, 0.4, 0.3, 0.003, 0.0, 0.0, 24090, 2)
    ops.limitCurve('ThreePoint', 14090, 4090, 0.0, 208.91946577, 0.01502404, 208.91946577, 0.04507211, 146.24362604, -4246.87151407, 0.05, 2, 0, 71004, 24035, 1, 3)
    ops.uniaxialMaterial('LimitState', 34090, 52.22986644, 6.289e-05, 156.68959933, 0.00018866, 522.29866444, 0.00062887, -52.22986644, -6.289e-05, -156.68959933, -0.00018866, -522.29866444, -0.00062887, 0.4, 0.3, 0.003, 0.0, 0.0, 14090, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4090, 99999, 'P', 44090, 'Vy', 34090, 'Vz', 24090, 'My', 14090, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4090, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124035, 124035, 24035, 4090, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174035, 12.6, 0.0, 4.6)
    ops.node(122004, 12.6, 0.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4091, 174035, 122004, 0.1225, 25542048.86927399, 10642520.3621975, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24091, 158.02593456, 0.00071346, 190.11847403, 0.0116431, 19.0118474, 0.03788661, -158.02593456, -0.00071346, -190.11847403, -0.0116431, -19.0118474, -0.03788661, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14091, 143.09916724, 0.00071346, 172.16031905, 0.0116431, 17.2160319, 0.03788661, -143.09916724, -0.00071346, -172.16031905, -0.0116431, -17.2160319, -0.03788661, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24091, 4091, 0.0, 191.53121373, 0.01426912, 191.53121373, 0.04280735, 134.07184961, -4393.01341013, 0.05, 2, 0, 74035, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44091, 47.88280343, 6.391e-05, 143.6484103, 0.00019172, 478.82803434, 0.00063907, -47.88280343, -6.391e-05, -143.6484103, -0.00019172, -478.82803434, -0.00063907, 0.4, 0.3, 0.003, 0.0, 0.0, 24091, 2)
    ops.limitCurve('ThreePoint', 14091, 4091, 0.0, 191.53121373, 0.01426912, 191.53121373, 0.04280735, 134.07184961, -4393.01341013, 0.05, 2, 0, 74035, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34091, 47.88280343, 6.391e-05, 143.6484103, 0.00019172, 478.82803434, 0.00063907, -47.88280343, -6.391e-05, -143.6484103, -0.00019172, -478.82803434, -0.00063907, 0.4, 0.3, 0.003, 0.0, 0.0, 14091, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4091, 99999, 'P', 44091, 'Vy', 34091, 'Vz', 24091, 'My', 14091, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174035, 74035, 174035, 4091, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4091, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 15.5, 0.0, 3.1)
    ops.node(124036, 15.5, 0.0, 4.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4092, 171005, 124036, 0.1225, 29938928.05613865, 12474553.35672444, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24092, 168.21207285, 0.0007257, 201.73807112, 0.01296297, 20.17380711, 0.04596148, -168.21207285, -0.0007257, -201.73807112, -0.01296297, -20.17380711, -0.04596148, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14092, 153.41706771, 0.0007257, 183.99430428, 0.01296297, 18.39943043, 0.04596148, -153.41706771, -0.0007257, -183.99430428, -0.01296297, -18.39943043, -0.04596148, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24092, 4092, 0.0, 225.0075407, 0.01451393, 225.0075407, 0.04354178, 157.50527849, -4610.88496493, 0.05, 2, 0, 71005, 24036, 2, 3)
    ops.uniaxialMaterial('LimitState', 44092, 56.25188517, 6.405e-05, 168.75565552, 0.00019215, 562.51885175, 0.00064051, -56.25188517, -6.405e-05, -168.75565552, -0.00019215, -562.51885175, -0.00064051, 0.4, 0.3, 0.003, 0.0, 0.0, 24092, 2)
    ops.limitCurve('ThreePoint', 14092, 4092, 0.0, 225.0075407, 0.01451393, 225.0075407, 0.04354178, 157.50527849, -4610.88496493, 0.05, 2, 0, 71005, 24036, 1, 3)
    ops.uniaxialMaterial('LimitState', 34092, 56.25188517, 6.405e-05, 168.75565552, 0.00019215, 562.51885175, 0.00064051, -56.25188517, -6.405e-05, -168.75565552, -0.00019215, -562.51885175, -0.00064051, 0.4, 0.3, 0.003, 0.0, 0.0, 14092, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4092, 99999, 'P', 44092, 'Vy', 34092, 'Vz', 24092, 'My', 14092, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 4092, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124036, 124036, 24036, 4092, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174036, 15.5, 0.0, 4.6)
    ops.node(122005, 15.5, 0.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4093, 174036, 122005, 0.1225, 28418771.36843697, 11841154.73684874, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24093, 150.94415915, 0.00074529, 181.63131781, 0.01277491, 18.16313178, 0.04492333, -150.94415915, -0.00074529, -181.63131781, -0.01277491, -18.16313178, -0.04492333, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14093, 139.05125434, 0.00074529, 167.32056882, 0.01277491, 16.73205688, 0.04492333, -139.05125434, -0.00074529, -167.32056882, -0.01277491, -16.73205688, -0.04492333, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24093, 4093, 0.0, 211.91056204, 0.01490581, 211.91056204, 0.04471744, 148.33739343, -4635.04842961, 0.05, 2, 0, 74036, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44093, 52.97764051, 6.355e-05, 158.93292153, 0.00019065, 529.77640511, 0.00063549, -52.97764051, -6.355e-05, -158.93292153, -0.00019065, -529.77640511, -0.00063549, 0.4, 0.3, 0.003, 0.0, 0.0, 24093, 2)
    ops.limitCurve('ThreePoint', 14093, 4093, 0.0, 211.91056204, 0.01490581, 211.91056204, 0.04471744, 148.33739343, -4635.04842961, 0.05, 2, 0, 74036, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34093, 52.97764051, 6.355e-05, 158.93292153, 0.00019065, 529.77640511, 0.00063549, -52.97764051, -6.355e-05, -158.93292153, -0.00019065, -529.77640511, -0.00063549, 0.4, 0.3, 0.003, 0.0, 0.0, 14093, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4093, 99999, 'P', 44093, 'Vy', 34093, 'Vz', 24093, 'My', 14093, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174036, 74036, 174036, 4093, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 4093, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.6, 0.0, 5.975)
    ops.node(124037, 12.6, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4095, 172004, 124037, 0.0625, 27828862.46290033, 11595359.3595418, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24095, 70.82016677, 0.0008923, 84.64751313, 0.00887623, 8.46475131, 0.03713273, -70.82016677, -0.0008923, -84.64751313, -0.00887623, -8.46475131, -0.03713273, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14095, 70.82016677, 0.0008923, 84.64751313, 0.00887623, 8.46475131, 0.03713273, -70.82016677, -0.0008923, -84.64751313, -0.00887623, -8.46475131, -0.03713273, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24095, 4095, 0.0, 59.9927681, 0.01784609, 59.9927681, 0.05353827, 41.99493767, -2386.59801365, 0.05, 2, 0, 72004, 24037, 2, 3)
    ops.uniaxialMaterial('LimitState', 44095, 14.99819202, 3.601e-05, 44.99457607, 0.00010803, 149.98192024, 0.0003601, -14.99819202, -3.601e-05, -44.99457607, -0.00010803, -149.98192024, -0.0003601, 0.4, 0.3, 0.003, 0.0, 0.0, 24095, 2)
    ops.limitCurve('ThreePoint', 14095, 4095, 0.0, 59.9927681, 0.01784609, 59.9927681, 0.05353827, 41.99493767, -2386.59801365, 0.05, 2, 0, 72004, 24037, 1, 3)
    ops.uniaxialMaterial('LimitState', 34095, 14.99819202, 3.601e-05, 44.99457607, 0.00010803, 149.98192024, 0.0003601, -14.99819202, -3.601e-05, -44.99457607, -0.00010803, -149.98192024, -0.0003601, 0.4, 0.3, 0.003, 0.0, 0.0, 14095, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4095, 99999, 'P', 44095, 'Vy', 34095, 'Vz', 24095, 'My', 14095, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4095, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124037, 124037, 24037, 4095, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174037, 12.6, 0.0, 7.45)
    ops.node(123004, 12.6, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4096, 174037, 123004, 0.0625, 27134812.25109316, 11306171.77128882, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24096, 68.61470712, 0.00094746, 82.35499192, 0.00895036, 8.23549919, 0.03940522, -68.61470712, -0.00094746, -82.35499192, -0.00895036, -8.23549919, -0.03940522, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14096, 68.61470712, 0.00094746, 82.35499192, 0.00895036, 8.23549919, 0.03940522, -68.61470712, -0.00094746, -82.35499192, -0.00895036, -8.23549919, -0.03940522, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24096, 4096, 0.0, 54.98058931, 0.01894929, 54.98058931, 0.05684786, 38.48641252, -2298.20492618, 0.05, 2, 0, 74037, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44096, 13.74514733, 3.385e-05, 41.23544199, 0.00010154, 137.45147329, 0.00033846, -13.74514733, -3.385e-05, -41.23544199, -0.00010154, -137.45147329, -0.00033846, 0.4, 0.3, 0.003, 0.0, 0.0, 24096, 2)
    ops.limitCurve('ThreePoint', 14096, 4096, 0.0, 54.98058931, 0.01894929, 54.98058931, 0.05684786, 38.48641252, -2298.20492618, 0.05, 2, 0, 74037, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34096, 13.74514733, 3.385e-05, 41.23544199, 0.00010154, 137.45147329, 0.00033846, -13.74514733, -3.385e-05, -41.23544199, -0.00010154, -137.45147329, -0.00033846, 0.4, 0.3, 0.003, 0.0, 0.0, 14096, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4096, 99999, 'P', 44096, 'Vy', 34096, 'Vz', 24096, 'My', 14096, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174037, 74037, 174037, 4096, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4096, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 15.5, 0.0, 5.975)
    ops.node(124038, 15.5, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4097, 172005, 124038, 0.0625, 28361905.44655066, 11817460.60272944, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24097, 74.23011901, 0.00097374, 88.73496249, 0.01010981, 8.87349625, 0.03964071, -74.23011901, -0.00097374, -88.73496249, -0.01010981, -8.87349625, -0.03964071, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14097, 74.23011901, 0.00097374, 88.73496249, 0.01010981, 8.87349625, 0.03964071, -74.23011901, -0.00097374, -88.73496249, -0.01010981, -8.87349625, -0.03964071, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24097, 4097, 0.0, 84.85471221, 0.01947487, 84.85471221, 0.05842461, 59.39829855, -2732.43126883, 0.05, 2, 0, 72005, 24038, 2, 3)
    ops.uniaxialMaterial('LimitState', 44097, 21.21367805, 4.998e-05, 63.64103416, 0.00014993, 212.13678053, 0.00049976, -21.21367805, -4.998e-05, -63.64103416, -0.00014993, -212.13678053, -0.00049976, 0.4, 0.3, 0.003, 0.0, 0.0, 24097, 2)
    ops.limitCurve('ThreePoint', 14097, 4097, 0.0, 84.85471221, 0.01947487, 84.85471221, 0.05842461, 59.39829855, -2732.43126883, 0.05, 2, 0, 72005, 24038, 1, 3)
    ops.uniaxialMaterial('LimitState', 34097, 21.21367805, 4.998e-05, 63.64103416, 0.00014993, 212.13678053, 0.00049976, -21.21367805, -4.998e-05, -63.64103416, -0.00014993, -212.13678053, -0.00049976, 0.4, 0.3, 0.003, 0.0, 0.0, 14097, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4097, 99999, 'P', 44097, 'Vy', 34097, 'Vz', 24097, 'My', 14097, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 4097, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124038, 124038, 24038, 4097, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174038, 15.5, 0.0, 7.45)
    ops.node(123005, 15.5, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4098, 174038, 123005, 0.0625, 27993800.22407941, 11664083.42669975, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24098, 67.38771378, 0.00088582, 80.88690787, 0.0119079, 8.08869079, 0.04436363, -67.38771378, -0.00088582, -80.88690787, -0.0119079, -8.08869079, -0.04436363, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14098, 67.38771378, 0.00088582, 80.88690787, 0.0119079, 8.08869079, 0.04436363, -67.38771378, -0.00088582, -80.88690787, -0.0119079, -8.08869079, -0.04436363, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24098, 4098, 0.0, 96.35133914, 0.01771634, 96.35133914, 0.05314903, 67.4459374, -2937.04135291, 0.05, 2, 0, 74038, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44098, 24.08783479, 5.749e-05, 72.26350436, 0.00017248, 240.87834786, 0.00057493, -24.08783479, -5.749e-05, -72.26350436, -0.00017248, -240.87834786, -0.00057493, 0.4, 0.3, 0.003, 0.0, 0.0, 24098, 2)
    ops.limitCurve('ThreePoint', 14098, 4098, 0.0, 96.35133914, 0.01771634, 96.35133914, 0.05314903, 67.4459374, -2937.04135291, 0.05, 2, 0, 74038, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34098, 24.08783479, 5.749e-05, 72.26350436, 0.00017248, 240.87834786, 0.00057493, -24.08783479, -5.749e-05, -72.26350436, -0.00017248, -240.87834786, -0.00057493, 0.4, 0.3, 0.003, 0.0, 0.0, 14098, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4098, 99999, 'P', 44098, 'Vy', 34098, 'Vz', 24098, 'My', 14098, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174038, 74038, 174038, 4098, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 4098, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.6, 0.0, 8.9)
    ops.node(124039, 12.6, 0.0, 9.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4100, 173004, 124039, 0.0625, 28371174.50627796, 11821322.71094915, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24100, 55.89085931, 0.00088771, 67.72480546, 0.01114813, 6.77248055, 0.05543074, -55.89085931, -0.00088771, -67.72480546, -0.01114813, -6.77248055, -0.05543074, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14100, 55.89085931, 0.00088771, 67.72480546, 0.01114813, 6.77248055, 0.05543074, -55.89085931, -0.00088771, -67.72480546, -0.01114813, -6.77248055, -0.05543074, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24100, 4100, 0.0, 54.1316936, 0.01775421, 54.1316936, 0.05326263, 37.89218552, -2437.36016492, 0.05, 2, 0, 73004, 24039, 2, 3)
    ops.uniaxialMaterial('LimitState', 44100, 13.5329234, 3.187e-05, 40.5987702, 9.561e-05, 135.32923401, 0.00031871, -13.5329234, -3.187e-05, -40.5987702, -9.561e-05, -135.32923401, -0.00031871, 0.4, 0.3, 0.003, 0.0, 0.0, 24100, 2)
    ops.limitCurve('ThreePoint', 14100, 4100, 0.0, 54.1316936, 0.01775421, 54.1316936, 0.05326263, 37.89218552, -2437.36016492, 0.05, 2, 0, 73004, 24039, 1, 3)
    ops.uniaxialMaterial('LimitState', 34100, 13.5329234, 3.187e-05, 40.5987702, 9.561e-05, 135.32923401, 0.00031871, -13.5329234, -3.187e-05, -40.5987702, -9.561e-05, -135.32923401, -0.00031871, 0.4, 0.3, 0.003, 0.0, 0.0, 14100, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4100, 99999, 'P', 44100, 'Vy', 34100, 'Vz', 24100, 'My', 14100, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4100, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124039, 124039, 24039, 4100, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174039, 12.6, 0.0, 10.325)
    ops.node(124004, 12.6, 0.0, 11.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4101, 174039, 124004, 0.0625, 29225643.16337052, 12177351.31807105, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24101, 52.13269624, 0.00084103, 63.30665496, 0.01349283, 6.3306655, 0.064035, -52.13269624, -0.00084103, -63.30665496, -0.01349283, -6.3306655, -0.064035, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14101, 52.13269624, 0.00084103, 63.30665496, 0.01349283, 6.3306655, 0.064035, -52.13269624, -0.00084103, -63.30665496, -0.01349283, -6.3306655, -0.064035, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24101, 4101, 0.0, 71.54644227, 0.0168206, 71.54644227, 0.05046179, 50.08250959, -3586.67811048, 0.05, 2, 0, 74039, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44101, 17.88661057, 4.089e-05, 53.6598317, 0.00012268, 178.86610567, 0.00040893, -17.88661057, -4.089e-05, -53.6598317, -0.00012268, -178.86610567, -0.00040893, 0.4, 0.3, 0.003, 0.0, 0.0, 24101, 2)
    ops.limitCurve('ThreePoint', 14101, 4101, 0.0, 71.54644227, 0.0168206, 71.54644227, 0.05046179, 50.08250959, -3586.67811048, 0.05, 2, 0, 74039, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34101, 17.88661057, 4.089e-05, 53.6598317, 0.00012268, 178.86610567, 0.00040893, -17.88661057, -4.089e-05, -53.6598317, -0.00012268, -178.86610567, -0.00040893, 0.4, 0.3, 0.003, 0.0, 0.0, 14101, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4101, 99999, 'P', 44101, 'Vy', 34101, 'Vz', 24101, 'My', 14101, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174039, 74039, 174039, 4101, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4101, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 15.5, 0.0, 8.9)
    ops.node(124040, 15.5, 0.0, 9.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4102, 173005, 124040, 0.0625, 29571572.26192649, 12321488.44246937, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24102, 53.99568812, 0.0008631, 65.29174114, 0.01381096, 6.52917411, 0.0596665, -53.99568812, -0.0008631, -65.29174114, -0.01381096, -6.52917411, -0.0596665, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14102, 53.99568812, 0.0008631, 65.29174114, 0.01381096, 6.52917411, 0.0596665, -53.99568812, -0.0008631, -65.29174114, -0.01381096, -6.52917411, -0.0596665, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24102, 4102, 0.0, 88.69898615, 0.01726204, 88.69898615, 0.05178611, 62.0892903, -3198.8972993, 0.05, 2, 0, 73005, 24040, 2, 3)
    ops.uniaxialMaterial('LimitState', 44102, 22.17474654, 5.01e-05, 66.52423961, 0.00015031, 221.74746537, 0.00050103, -22.17474654, -5.01e-05, -66.52423961, -0.00015031, -221.74746537, -0.00050103, 0.4, 0.3, 0.003, 0.0, 0.0, 24102, 2)
    ops.limitCurve('ThreePoint', 14102, 4102, 0.0, 88.69898615, 0.01726204, 88.69898615, 0.05178611, 62.0892903, -3198.8972993, 0.05, 2, 0, 73005, 24040, 1, 3)
    ops.uniaxialMaterial('LimitState', 34102, 22.17474654, 5.01e-05, 66.52423961, 0.00015031, 221.74746537, 0.00050103, -22.17474654, -5.01e-05, -66.52423961, -0.00015031, -221.74746537, -0.00050103, 0.4, 0.3, 0.003, 0.0, 0.0, 14102, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4102, 99999, 'P', 44102, 'Vy', 34102, 'Vz', 24102, 'My', 14102, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 4102, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124040, 124040, 24040, 4102, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174040, 15.5, 0.0, 10.325)
    ops.node(124005, 15.5, 0.0, 11.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4103, 174040, 124005, 0.0625, 31196063.10076448, 12998359.62531853, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24103, 52.15703743, 0.00083267, 63.02045661, 0.01333346, 6.30204566, 0.06526073, -52.15703743, -0.00083267, -63.02045661, -0.01333346, -6.30204566, -0.06526073, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14103, 52.15703743, 0.00083267, 63.02045661, 0.01333346, 6.30204566, 0.06526073, -52.15703743, -0.00083267, -63.02045661, -0.01333346, -6.30204566, -0.06526073, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24103, 4103, 0.0, 79.42046158, 0.01665344, 79.42046158, 0.04996031, 55.59432311, -4035.45252844, 0.05, 2, 0, 74040, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44103, 19.8551154, 4.253e-05, 59.56534619, 0.00012758, 198.55115396, 0.00042526, -19.8551154, -4.253e-05, -59.56534619, -0.00012758, -198.55115396, -0.00042526, 0.4, 0.3, 0.003, 0.0, 0.0, 24103, 2)
    ops.limitCurve('ThreePoint', 14103, 4103, 0.0, 79.42046158, 0.01665344, 79.42046158, 0.04996031, 55.59432311, -4035.45252844, 0.05, 2, 0, 74040, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34103, 19.8551154, 4.253e-05, 59.56534619, 0.00012758, 198.55115396, 0.00042526, -19.8551154, -4.253e-05, -59.56534619, -0.00012758, -198.55115396, -0.00042526, 0.4, 0.3, 0.003, 0.0, 0.0, 14103, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4103, 99999, 'P', 44103, 'Vy', 34103, 'Vz', 24103, 'My', 14103, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174040, 74040, 174040, 4103, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 4103, '-orient', 0, 0, 1, 0, 1, 0)
