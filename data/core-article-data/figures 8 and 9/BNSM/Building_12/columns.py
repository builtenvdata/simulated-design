import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 27740401.98307873, 11558500.8262828, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 68.22695531, 0.00135818, 80.2212369, 0.00784874, 8.02212369, 0.02770641, -68.22695531, -0.00135818, -80.2212369, -0.00784874, -8.02212369, -0.02770641, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 72.16425954, 0.00135818, 84.85071823, 0.00784874, 8.48507182, 0.02770641, -72.16425954, -0.00135818, -84.85071823, -0.00784874, -8.48507182, -0.02770641, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 86.24302278, 0.02716355, 86.24302278, 0.08149066, 60.37011595, -1294.36130027, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 21.5607557, 0.00010924, 64.68226709, 0.00032771, 215.60755696, 0.00109235, -21.5607557, -0.00010924, -64.68226709, -0.00032771, -215.60755696, -0.00109235, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 86.24302278, 0.02716355, 86.24302278, 0.08149066, 60.37011595, -1294.36130027, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 21.5607557, 0.00010924, 64.68226709, 0.00032771, 215.60755696, 0.00109235, -21.5607557, -0.00010924, -64.68226709, -0.00032771, -215.60755696, -0.00109235, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.9, 0.0, 0.0)
    ops.node(121002, 3.9, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.09, 31407283.37034314, 13086368.07097631, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 126.3562815, 0.00112617, 148.66925544, 0.00905591, 14.86692554, 0.03305346, -126.3562815, -0.00112617, -148.66925544, -0.00905591, -14.86692554, -0.03305346, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 142.54304718, 0.00112617, 167.71440597, 0.00905591, 16.7714406, 0.03305346, -142.54304718, -0.00112617, -167.71440597, -0.00905591, -16.7714406, -0.03305346, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 148.25401172, 0.02252346, 148.25401172, 0.06757038, 103.7778082, -1927.78242397, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 37.06350293, 0.00011518, 111.19050879, 0.00034553, 370.6350293, 0.00115177, -37.06350293, -0.00011518, -111.19050879, -0.00034553, -370.6350293, -0.00115177, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 148.25401172, 0.02252346, 148.25401172, 0.06757038, 103.7778082, -1927.78242397, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 37.06350293, 0.00011518, 111.19050879, 0.00034553, 370.6350293, 0.00115177, -37.06350293, -0.00011518, -111.19050879, -0.00034553, -370.6350293, -0.00115177, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 14.7, 0.0, 0.0)
    ops.node(121005, 14.7, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.09, 30869879.35122587, 12862449.72967745, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 127.76203003, 0.00109766, 150.31916629, 0.009045, 15.03191663, 0.03181976, -127.76203003, -0.00109766, -150.31916629, -0.009045, -15.03191663, -0.03181976, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 146.12415107, 0.00109766, 171.92322756, 0.009045, 17.19232276, 0.03181976, -146.12415107, -0.00109766, -171.92322756, -0.009045, -17.19232276, -0.03181976, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 145.73054258, 0.02195317, 145.73054258, 0.06585952, 102.0113798, -1913.61263491, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 36.43263564, 0.00011519, 109.29790693, 0.00034556, 364.32635644, 0.00115188, -36.43263564, -0.00011519, -109.29790693, -0.00034556, -364.32635644, -0.00115188, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 145.73054258, 0.02195317, 145.73054258, 0.06585952, 102.0113798, -1913.61263491, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 36.43263564, 0.00011519, 109.29790693, 0.00034556, 364.32635644, 0.00115188, -36.43263564, -0.00011519, -109.29790693, -0.00034556, -364.32635644, -0.00115188, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 18.6, 0.0, 0.0)
    ops.node(121006, 18.6, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.0625, 30799367.16867132, 12833069.65361305, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 72.23683223, 0.00126302, 85.23210856, 0.00926063, 8.52321086, 0.03765935, -72.23683223, -0.00126302, -85.23210856, -0.00926063, -8.52321086, -0.03765935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 77.37622071, 0.00126302, 91.29606379, 0.00926063, 9.12960638, 0.03765935, -77.37622071, -0.00126302, -91.29606379, -0.00926063, -9.12960638, -0.03765935, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 103.40587792, 0.02526048, 103.40587792, 0.07578145, 72.38411454, -1366.87965085, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 25.85146948, 0.00011797, 77.55440844, 0.0003539, 258.5146948, 0.00117966, -25.85146948, -0.00011797, -77.55440844, -0.0003539, -258.5146948, -0.00117966, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 103.40587792, 0.02526048, 103.40587792, 0.07578145, 72.38411454, -1366.87965085, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 25.85146948, 0.00011797, 77.55440844, 0.0003539, 258.5146948, 0.00117966, -25.85146948, -0.00011797, -77.55440844, -0.0003539, -258.5146948, -0.00117966, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 5.35, 0.0)
    ops.node(121007, 0.0, 5.35, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 30362611.69571528, 12651088.20654804, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 203.05816808, 0.00099126, 240.4513221, 0.00814851, 24.04513221, 0.03160059, -203.05816808, -0.00099126, -240.4513221, -0.00814851, -24.04513221, -0.03160059, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 203.05816808, 0.00099126, 240.4513221, 0.00814851, 24.04513221, 0.03160059, -203.05816808, -0.00099126, -240.4513221, -0.00814851, -24.04513221, -0.03160059, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 172.09317369, 0.01982513, 172.09317369, 0.0594754, 120.46522158, -2063.87756183, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 43.02329342, 0.00010161, 129.06988027, 0.00030482, 430.23293422, 0.00101606, -43.02329342, -0.00010161, -129.06988027, -0.00030482, -430.23293422, -0.00101606, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 172.09317369, 0.01982513, 172.09317369, 0.0594754, 120.46522158, -2063.87756183, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 43.02329342, 0.00010161, 129.06988027, 0.00030482, 430.23293422, 0.00101606, -43.02329342, -0.00010161, -129.06988027, -0.00030482, -430.23293422, -0.00101606, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 3.9, 5.35, 0.0)
    ops.node(121008, 3.9, 5.35, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.16, 29667241.18818079, 12361350.49507533, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 361.30126409, 0.00090103, 427.64827437, 0.00795288, 42.76482744, 0.02540018, -361.30126409, -0.00090103, -427.64827437, -0.00795288, -42.76482744, -0.02540018, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 361.30126409, 0.00090103, 427.64827437, 0.00795288, 42.76482744, 0.02540018, -361.30126409, -0.00090103, -427.64827437, -0.00795288, -42.76482744, -0.02540018, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 201.98214062, 0.01802068, 201.98214062, 0.05406205, 141.38749843, -2337.67734008, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 50.49553515, 9.344e-05, 151.48660546, 0.00028033, 504.95535155, 0.00093443, -50.49553515, -9.344e-05, -151.48660546, -0.00028033, -504.95535155, -0.00093443, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 201.98214062, 0.01802068, 201.98214062, 0.05406205, 141.38749843, -2337.67734008, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 50.49553515, 9.344e-05, 151.48660546, 0.00028033, 504.95535155, 0.00093443, -50.49553515, -9.344e-05, -151.48660546, -0.00028033, -504.95535155, -0.00093443, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 7.8, 5.35, 0.0)
    ops.node(121009, 7.8, 5.35, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 31745954.51912984, 13227481.04963744, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 318.11594139, 0.00087413, 377.19846362, 0.01108181, 37.71984636, 0.03338512, -318.11594139, -0.00087413, -377.19846362, -0.01108181, -37.71984636, -0.03338512, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 318.11594139, 0.00087413, 377.19846362, 0.01108181, 37.71984636, 0.03338512, -318.11594139, -0.00087413, -377.19846362, -0.01108181, -37.71984636, -0.03338512, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 211.73523522, 0.01748268, 211.73523522, 0.05244803, 148.21466465, -2259.20625523, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 52.9338088, 9.154e-05, 158.80142641, 0.00027462, 529.33808805, 0.00091541, -52.9338088, -9.154e-05, -158.80142641, -0.00027462, -529.33808805, -0.00091541, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 211.73523522, 0.01748268, 211.73523522, 0.05244803, 148.21466465, -2259.20625523, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 52.9338088, 9.154e-05, 158.80142641, 0.00027462, 529.33808805, 0.00091541, -52.9338088, -9.154e-05, -158.80142641, -0.00027462, -529.33808805, -0.00091541, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 10.8, 5.35, 0.0)
    ops.node(121010, 10.8, 5.35, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 30205609.85479016, 12585670.77282923, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 302.40293773, 0.00093479, 358.9788389, 0.01161879, 35.89788389, 0.03156639, -302.40293773, -0.00093479, -358.9788389, -0.01161879, -35.89788389, -0.03156639, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 302.40293773, 0.00093479, 358.9788389, 0.01161879, 35.89788389, 0.03156639, -302.40293773, -0.00093479, -358.9788389, -0.01161879, -35.89788389, -0.03156639, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 207.2362238, 0.01869589, 207.2362238, 0.05608766, 145.06535666, -2340.24082041, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 51.80905595, 9.417e-05, 155.42716785, 0.0002825, 518.0905595, 0.00094165, -51.80905595, -9.417e-05, -155.42716785, -0.0002825, -518.0905595, -0.00094165, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 207.2362238, 0.01869589, 207.2362238, 0.05608766, 145.06535666, -2340.24082041, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 51.80905595, 9.417e-05, 155.42716785, 0.0002825, 518.0905595, 0.00094165, -51.80905595, -9.417e-05, -155.42716785, -0.0002825, -518.0905595, -0.00094165, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 14.7, 5.35, 0.0)
    ops.node(121011, 14.7, 5.35, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 30030246.22341901, 12512602.59309125, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 341.12708725, 0.00093836, 403.80786924, 0.00842699, 40.38078692, 0.02648398, -341.12708725, -0.00093836, -403.80786924, -0.00842699, -40.38078692, -0.02648398, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 341.12708725, 0.00093836, 403.80786924, 0.00842699, 40.38078692, 0.02648398, -341.12708725, -0.00093836, -403.80786924, -0.00842699, -40.38078692, -0.02648398, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 205.15161617, 0.01876713, 205.15161617, 0.0563014, 143.60613132, -2358.22769037, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 51.28790404, 9.376e-05, 153.86371213, 0.00028129, 512.87904043, 0.00093762, -51.28790404, -9.376e-05, -153.86371213, -0.00028129, -512.87904043, -0.00093762, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 205.15161617, 0.01876713, 205.15161617, 0.0563014, 143.60613132, -2358.22769037, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 51.28790404, 9.376e-05, 153.86371213, 0.00028129, 512.87904043, 0.00093762, -51.28790404, -9.376e-05, -153.86371213, -0.00028129, -512.87904043, -0.00093762, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 18.6, 5.35, 0.0)
    ops.node(121012, 18.6, 5.35, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 31755276.53861723, 13231365.22442385, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 199.64478353, 0.00098811, 236.22766198, 0.00843198, 23.6227662, 0.0346045, -199.64478353, -0.00098811, -236.22766198, -0.00843198, -23.6227662, -0.0346045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 199.64478353, 0.00098811, 236.22766198, 0.00843198, 23.6227662, 0.0346045, -199.64478353, -0.00098811, -236.22766198, -0.00843198, -23.6227662, -0.0346045, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 176.23077185, 0.01976221, 176.23077185, 0.05928663, 123.3615403, -2024.381129, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 44.05769296, 9.949e-05, 132.17307889, 0.00029846, 440.57692964, 0.00099486, -44.05769296, -9.949e-05, -132.17307889, -0.00029846, -440.57692964, -0.00099486, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 176.23077185, 0.01976221, 176.23077185, 0.05928663, 123.3615403, -2024.381129, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 44.05769296, 9.949e-05, 132.17307889, 0.00029846, 440.57692964, 0.00099486, -44.05769296, -9.949e-05, -132.17307889, -0.00029846, -440.57692964, -0.00099486, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 10.7, 0.0)
    ops.node(121013, 0.0, 10.7, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0625, 31310018.02162411, 13045840.84234338, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 67.82695674, 0.00126277, 80.0211681, 0.00990618, 8.00211681, 0.03963397, -67.82695674, -0.00126277, -80.0211681, -0.00990618, -8.00211681, -0.03963397, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 71.63285726, 0.00126277, 84.51130919, 0.00990618, 8.45113092, 0.03963397, -71.63285726, -0.00126277, -84.51130919, -0.00990618, -8.45113092, -0.03963397, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 104.93059406, 0.02525539, 104.93059406, 0.07576616, 73.45141584, -1374.35384513, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 26.23264851, 0.00011775, 78.69794554, 0.00035326, 262.32648514, 0.00117753, -26.23264851, -0.00011775, -78.69794554, -0.00035326, -262.32648514, -0.00117753, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 104.93059406, 0.02525539, 104.93059406, 0.07576616, 73.45141584, -1374.35384513, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 26.23264851, 0.00011775, 78.69794554, 0.00035326, 262.32648514, 0.00117753, -26.23264851, -0.00011775, -78.69794554, -0.00035326, -262.32648514, -0.00117753, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 3.9, 10.7, 0.0)
    ops.node(121014, 3.9, 10.7, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.09, 29173225.20600023, 12155510.50250009, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 137.7488478, 0.00114693, 161.82669375, 0.00800441, 16.18266938, 0.02676348, -137.7488478, -0.00114693, -161.82669375, -0.00800441, -16.18266938, -0.02676348, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 149.41628649, 0.00114693, 175.53354544, 0.00800441, 17.55335454, 0.02676348, -149.41628649, -0.00114693, -175.53354544, -0.00800441, -17.55335454, -0.02676348, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 138.56952284, 0.02293866, 138.56952284, 0.06881597, 96.99866599, -1884.05653341, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 34.64238071, 0.0001159, 103.92714213, 0.00034769, 346.4238071, 0.00115897, -34.64238071, -0.0001159, -103.92714213, -0.00034769, -346.4238071, -0.00115897, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 138.56952284, 0.02293866, 138.56952284, 0.06881597, 96.99866599, -1884.05653341, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 34.64238071, 0.0001159, 103.92714213, 0.00034769, 346.4238071, 0.00115897, -34.64238071, -0.0001159, -103.92714213, -0.00034769, -346.4238071, -0.00115897, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.8, 10.7, 0.0)
    ops.node(121015, 7.8, 10.7, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.09, 31236704.02526855, 13015293.3438619, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 124.11940908, 0.00110664, 146.60754218, 0.00846575, 14.66075422, 0.03497618, -124.11940908, -0.00110664, -146.60754218, -0.00846575, -14.66075422, -0.03497618, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 129.70042888, 0.00110664, 153.19973919, 0.00846575, 15.31997392, 0.03497618, -129.70042888, -0.00110664, -153.19973919, -0.00846575, -15.31997392, -0.03497618, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 135.52307054, 0.0221329, 135.52307054, 0.06639869, 94.86614938, -1655.61846337, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 33.88076764, 0.00010586, 101.64230291, 0.00031758, 338.80767636, 0.00105861, -33.88076764, -0.00010586, -101.64230291, -0.00031758, -338.80767636, -0.00105861, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 135.52307054, 0.0221329, 135.52307054, 0.06639869, 94.86614938, -1655.61846337, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 33.88076764, 0.00010586, 101.64230291, 0.00031758, 338.80767636, 0.00105861, -33.88076764, -0.00010586, -101.64230291, -0.00031758, -338.80767636, -0.00105861, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 10.8, 10.7, 0.0)
    ops.node(121016, 10.8, 10.7, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.09, 29536797.98176469, 12306999.15906862, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 125.25106094, 0.00112863, 147.91060545, 0.00839918, 14.79106054, 0.03097458, -125.25106094, -0.00112863, -147.91060545, -0.00839918, -14.79106054, -0.03097458, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 131.15756631, 0.00112863, 154.88567439, 0.00839918, 15.48856744, 0.03097458, -131.15756631, -0.00112863, -154.88567439, -0.00839918, -15.48856744, -0.03097458, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 132.58012116, 0.02257254, 132.58012116, 0.06771761, 92.80608481, -1708.10488571, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 33.14503029, 0.00010952, 99.43509087, 0.00032857, 331.4503029, 0.00109523, -33.14503029, -0.00010952, -99.43509087, -0.00032857, -331.4503029, -0.00109523, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 132.58012116, 0.02257254, 132.58012116, 0.06771761, 92.80608481, -1708.10488571, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 33.14503029, 0.00010952, 99.43509087, 0.00032857, 331.4503029, 0.00109523, -33.14503029, -0.00010952, -99.43509087, -0.00032857, -331.4503029, -0.00109523, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 14.7, 10.7, 0.0)
    ops.node(121017, 14.7, 10.7, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.09, 32686810.6782801, 13619504.44928337, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 138.42249553, 0.00121185, 162.7512015, 0.00896756, 16.27512015, 0.03575733, -138.42249553, -0.00121185, -162.7512015, -0.00896756, -16.27512015, -0.03575733, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 147.86706456, 0.00121185, 173.85571852, 0.00896756, 17.38557185, 0.03575733, -147.86706456, -0.00121185, -173.85571852, -0.00896756, -17.38557185, -0.03575733, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 149.3991501, 0.02423706, 149.3991501, 0.07271118, 104.57940507, -1863.32649273, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 37.34978752, 0.00011152, 112.04936257, 0.00033457, 373.49787524, 0.00111523, -37.34978752, -0.00011152, -112.04936257, -0.00033457, -373.49787524, -0.00111523, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 149.3991501, 0.02423706, 149.3991501, 0.07271118, 104.57940507, -1863.32649273, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 37.34978752, 0.00011152, 112.04936257, 0.00033457, 373.49787524, 0.00111523, -37.34978752, -0.00011152, -112.04936257, -0.00033457, -373.49787524, -0.00111523, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 18.6, 10.7, 0.0)
    ops.node(121018, 18.6, 10.7, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.0625, 33207291.86222024, 13836371.60925843, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 70.51700599, 0.00136466, 83.04724322, 0.01027588, 8.30472432, 0.04462715, -70.51700599, -0.00136466, -83.04724322, -0.01027588, -8.30472432, -0.04462715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 74.22097261, 0.00136466, 87.40937136, 0.01027588, 8.74093714, 0.04462715, -74.22097261, -0.00136466, -87.40937136, -0.01027588, -8.74093714, -0.04462715, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 110.75236074, 0.0272932, 110.75236074, 0.08187959, 77.52665252, -1404.51764332, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 27.68809019, 0.00011718, 83.06427056, 0.00035155, 276.88090186, 0.00117185, -27.68809019, -0.00011718, -83.06427056, -0.00035155, -276.88090186, -0.00117185, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 110.75236074, 0.0272932, 110.75236074, 0.08187959, 77.52665252, -1404.51764332, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 27.68809019, 0.00011718, 83.06427056, 0.00035155, 276.88090186, 0.00117185, -27.68809019, -0.00011718, -83.06427056, -0.00035155, -276.88090186, -0.00117185, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.3)
    ops.node(122001, 0.0, 0.0, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 31145958.86428956, 12977482.86012065, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 58.8996015, 0.00143817, 70.00162632, 0.01042259, 7.00016263, 0.04685412, -58.8996015, -0.00143817, -70.00162632, -0.01042259, -7.00016263, -0.04685412, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 61.65015585, 0.00143817, 73.27063448, 0.01042259, 7.32706345, 0.04685412, -61.65015585, -0.00143817, -73.27063448, -0.01042259, -7.32706345, -0.04685412, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 97.81920813, 0.02876336, 97.81920813, 0.08629009, 68.47344569, -1233.42871061, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 24.45480203, 0.00011035, 73.3644061, 0.00033105, 244.54802032, 0.00110351, -24.45480203, -0.00011035, -73.3644061, -0.00033105, -244.54802032, -0.00110351, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 97.81920813, 0.02876336, 97.81920813, 0.08629009, 68.47344569, -1233.42871061, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 24.45480203, 0.00011035, 73.3644061, 0.00033105, 244.54802032, 0.00110351, -24.45480203, -0.00011035, -73.3644061, -0.00033105, -244.54802032, -0.00110351, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.9, 0.0, 3.3)
    ops.node(122002, 3.9, 0.0, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.09, 33143914.22527458, 13809964.26053108, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 105.73580919, 0.00107662, 125.03984748, 0.01024494, 12.50398475, 0.04369556, -105.73580919, -0.00107662, -125.03984748, -0.01024494, -12.50398475, -0.04369556, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 117.02082603, 0.00107662, 138.38515401, 0.01024494, 13.8385154, 0.04369556, -117.02082603, -0.00107662, -138.38515401, -0.01024494, -13.8385154, -0.04369556, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 146.06777355, 0.02153249, 146.06777355, 0.06459747, 102.24744149, -1736.64853374, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 36.51694339, 0.00010753, 109.55083016, 0.0003226, 365.16943388, 0.00107533, -36.51694339, -0.00010753, -109.55083016, -0.0003226, -365.16943388, -0.00107533, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 146.06777355, 0.02153249, 146.06777355, 0.06459747, 102.24744149, -1736.64853374, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 36.51694339, 0.00010753, 109.55083016, 0.0003226, 365.16943388, 0.00107533, -36.51694339, -0.00010753, -109.55083016, -0.0003226, -365.16943388, -0.00107533, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 14.7, 0.0, 3.3)
    ops.node(122005, 14.7, 0.0, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.09, 28648574.50466887, 11936906.04361203, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 102.8933222, 0.00111255, 122.00277797, 0.00987868, 12.2002778, 0.03357575, -102.8933222, -0.00111255, -122.00277797, -0.00987868, -12.2002778, -0.03357575, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 113.75806375, 0.00111255, 134.88533071, 0.00987868, 13.48853307, 0.03357575, -113.75806375, -0.00111255, -134.88533071, -0.00987868, -13.48853307, -0.03357575, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 133.35725842, 0.02225102, 133.35725842, 0.06675307, 93.35008089, -1772.24612715, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 33.3393146, 0.00011358, 100.01794381, 0.00034074, 333.39314605, 0.0011358, -33.3393146, -0.00011358, -100.01794381, -0.00034074, -333.39314605, -0.0011358, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 133.35725842, 0.02225102, 133.35725842, 0.06675307, 93.35008089, -1772.24612715, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 33.3393146, 0.00011358, 100.01794381, 0.00034074, 333.39314605, 0.0011358, -33.3393146, -0.00011358, -100.01794381, -0.00034074, -333.39314605, -0.0011358, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 18.6, 0.0, 3.3)
    ops.node(122006, 18.6, 0.0, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.0625, 31197573.65977765, 12998989.02490735, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 58.16318461, 0.00124776, 69.12267151, 0.01150589, 6.91226715, 0.04805963, -58.16318461, -0.00124776, -69.12267151, -0.01150589, -6.91226715, -0.04805963, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 61.76280889, 0.00124776, 73.40056049, 0.01150589, 7.34005605, 0.04805963, -61.76280889, -0.00124776, -73.40056049, -0.01150589, -7.34005605, -0.04805963, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 100.76564247, 0.02495514, 100.76564247, 0.07486542, 70.53594973, -1301.34143181, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 25.19141062, 0.00011349, 75.57423185, 0.00034046, 251.91410617, 0.00113486, -25.19141062, -0.00011349, -75.57423185, -0.00034046, -251.91410617, -0.00113486, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 100.76564247, 0.02495514, 100.76564247, 0.07486542, 70.53594973, -1301.34143181, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 25.19141062, 0.00011349, 75.57423185, 0.00034046, 251.91410617, 0.00113486, -25.19141062, -0.00011349, -75.57423185, -0.00034046, -251.91410617, -0.00113486, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 5.35, 3.3)
    ops.node(122007, 0.0, 5.35, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 28469704.83172237, 11862377.01321765, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 141.57064922, 0.00091067, 168.9086233, 0.00921767, 16.89086233, 0.03426183, -141.57064922, -0.00091067, -168.9086233, -0.00921767, -16.89086233, -0.03426183, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 128.4497275, 0.00091067, 153.25398842, 0.00921767, 15.32539884, 0.03426183, -128.4497275, -0.00091067, -153.25398842, -0.00921767, -15.32539884, -0.03426183, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 157.24540799, 0.01821331, 157.24540799, 0.05463992, 110.07178559, -1898.42704096, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 39.311352, 9.901e-05, 117.93405599, 0.00029704, 393.11351996, 0.00099013, -39.311352, -9.901e-05, -117.93405599, -0.00029704, -393.11351996, -0.00099013, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 157.24540799, 0.01821331, 157.24540799, 0.05463992, 110.07178559, -1898.42704096, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 39.311352, 9.901e-05, 117.93405599, 0.00029704, 393.11351996, 0.00099013, -39.311352, -9.901e-05, -117.93405599, -0.00029704, -393.11351996, -0.00099013, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 3.9, 5.35, 3.3)
    ops.node(122008, 3.9, 5.35, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.16, 30835971.22915247, 12848321.34548019, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 221.51344834, 0.00082939, 263.79993939, 0.0096807, 26.37999394, 0.03293, -221.51344834, -0.00082939, -263.79993939, -0.0096807, -26.37999394, -0.03293, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 206.65744573, 0.00082939, 246.10795446, 0.0096807, 24.61079545, 0.03293, -206.65744573, -0.00082939, -246.10795446, -0.0096807, -24.61079545, -0.03293, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 203.36441845, 0.01658788, 203.36441845, 0.04976365, 142.35509291, -2164.95571704, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 50.84110461, 9.052e-05, 152.52331383, 0.00027155, 508.41104612, 0.00090517, -50.84110461, -9.052e-05, -152.52331383, -0.00027155, -508.41104612, -0.00090517, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 203.36441845, 0.01658788, 203.36441845, 0.04976365, 142.35509291, -2164.95571704, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 50.84110461, 9.052e-05, 152.52331383, 0.00027155, 508.41104612, 0.00090517, -50.84110461, -9.052e-05, -152.52331383, -0.00027155, -508.41104612, -0.00090517, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 7.8, 5.35, 3.3)
    ops.node(122009, 7.8, 5.35, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 28831162.20095946, 12012984.25039978, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 214.32269234, 0.00084297, 256.15961634, 0.00779962, 25.61596163, 0.02593861, -214.32269234, -0.00084297, -256.15961634, -0.00779962, -25.61596163, -0.02593861, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 214.32269234, 0.00084297, 256.15961634, 0.00779962, 25.61596163, 0.02593861, -214.32269234, -0.00084297, -256.15961634, -0.00779962, -25.61596163, -0.02593861, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 169.5130511, 0.01685933, 169.5130511, 0.05057799, 118.65913577, -1710.4382018, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 42.37826278, 8.07e-05, 127.13478833, 0.00024209, 423.78262775, 0.00080696, -42.37826278, -8.07e-05, -127.13478833, -0.00024209, -423.78262775, -0.00080696, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 169.5130511, 0.01685933, 169.5130511, 0.05057799, 118.65913577, -1710.4382018, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 42.37826278, 8.07e-05, 127.13478833, 0.00024209, 423.78262775, 0.00080696, -42.37826278, -8.07e-05, -127.13478833, -0.00024209, -423.78262775, -0.00080696, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 10.8, 5.35, 3.3)
    ops.node(122010, 10.8, 5.35, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 29112165.54338898, 12130068.97641208, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 212.92994422, 0.0008422, 254.4756045, 0.00851614, 25.44756045, 0.02703047, -212.92994422, -0.0008422, -254.4756045, -0.00851614, -25.44756045, -0.02703047, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 212.92994422, 0.0008422, 254.4756045, 0.00851614, 25.44756045, 0.02703047, -212.92994422, -0.0008422, -254.4756045, -0.00851614, -25.44756045, -0.02703047, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 174.31675568, 0.01684404, 174.31675568, 0.05053212, 122.02172897, -1756.14213404, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 43.57918892, 8.218e-05, 130.73756676, 0.00024655, 435.7918892, 0.00082182, -43.57918892, -8.218e-05, -130.73756676, -0.00024655, -435.7918892, -0.00082182, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 174.31675568, 0.01684404, 174.31675568, 0.05053212, 122.02172897, -1756.14213404, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 43.57918892, 8.218e-05, 130.73756676, 0.00024655, 435.7918892, 0.00082182, -43.57918892, -8.218e-05, -130.73756676, -0.00024655, -435.7918892, -0.00082182, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 14.7, 5.35, 3.3)
    ops.node(122011, 14.7, 5.35, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 31634465.25138603, 13181027.18807751, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 225.57916282, 0.00081539, 268.37253427, 0.00933839, 26.83725343, 0.0337107, -225.57916282, -0.00081539, -268.37253427, -0.00933839, -26.83725343, -0.0337107, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 209.65880715, 0.00081539, 249.43201626, 0.00933839, 24.94320163, 0.0337107, -209.65880715, -0.00081539, -249.43201626, -0.00933839, -24.94320163, -0.0337107, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 205.61245899, 0.01630779, 205.61245899, 0.04892338, 143.92872129, -2121.36206148, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 51.40311475, 8.921e-05, 154.20934424, 0.00026762, 514.03114747, 0.00089207, -51.40311475, -8.921e-05, -154.20934424, -0.00026762, -514.03114747, -0.00089207, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 205.61245899, 0.01630779, 205.61245899, 0.04892338, 143.92872129, -2121.36206148, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 51.40311475, 8.921e-05, 154.20934424, 0.00026762, 514.03114747, 0.00089207, -51.40311475, -8.921e-05, -154.20934424, -0.00026762, -514.03114747, -0.00089207, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 18.6, 5.35, 3.3)
    ops.node(122012, 18.6, 5.35, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 29797622.31469679, 12415675.96445699, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 142.00074577, 0.00092505, 169.38320707, 0.00980492, 16.93832071, 0.03754314, -142.00074577, -0.00092505, -169.38320707, -0.00980492, -16.93832071, -0.03754314, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 129.40173979, 0.00092505, 154.35469417, 0.00980492, 15.43546942, 0.03754314, -129.40173979, -0.00092505, -154.35469417, -0.00980492, -15.43546942, -0.03754314, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 162.42117053, 0.01850107, 162.42117053, 0.05550321, 113.69481937, -1893.33021426, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 40.60529263, 9.771e-05, 121.8158779, 0.00029314, 406.05292632, 0.00097714, -40.60529263, -9.771e-05, -121.8158779, -0.00029314, -406.05292632, -0.00097714, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 162.42117053, 0.01850107, 162.42117053, 0.05550321, 113.69481937, -1893.33021426, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 40.60529263, 9.771e-05, 121.8158779, 0.00029314, 406.05292632, 0.00097714, -40.60529263, -9.771e-05, -121.8158779, -0.00029314, -406.05292632, -0.00097714, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 10.7, 3.3)
    ops.node(122013, 0.0, 10.7, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0625, 28932777.84087041, 12055324.10036267, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 59.71107527, 0.00127153, 71.02719443, 0.01128827, 7.10271944, 0.04204102, -59.71107527, -0.00127153, -71.02719443, -0.01128827, -7.10271944, -0.04204102, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 63.90807469, 0.00127153, 76.01958642, 0.01128827, 7.60195864, 0.04204102, -63.90807469, -0.00127153, -76.01958642, -0.01128827, -7.60195864, -0.04204102, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 97.35921406, 0.02543066, 97.35921406, 0.07629199, 68.15144984, -1336.91031398, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 24.33980352, 0.00011823, 73.01941055, 0.0003547, 243.39803515, 0.00118233, -24.33980352, -0.00011823, -73.01941055, -0.0003547, -243.39803515, -0.00118233, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 97.35921406, 0.02543066, 97.35921406, 0.07629199, 68.15144984, -1336.91031398, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 24.33980352, 0.00011823, 73.01941055, 0.0003547, 243.39803515, 0.00118233, -24.33980352, -0.00011823, -73.01941055, -0.0003547, -243.39803515, -0.00118233, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 3.9, 10.7, 3.3)
    ops.node(122014, 3.9, 10.7, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.09, 29763467.94681929, 12401444.97784137, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 103.64647817, 0.0010947, 122.95783021, 0.00874311, 12.29578302, 0.03511747, -103.64647817, -0.0010947, -122.95783021, -0.00874311, -12.29578302, -0.03511747, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 114.77714058, 0.0010947, 136.16235122, 0.00874311, 13.61623512, 0.03511747, -114.77714058, -0.0010947, -136.16235122, -0.00874311, -13.61623512, -0.03511747, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 130.15980639, 0.02189396, 130.15980639, 0.06568188, 91.11186447, -1626.02913654, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 32.5399516, 0.0001067, 97.61985479, 0.00032011, 325.39951597, 0.00106705, -32.5399516, -0.0001067, -97.61985479, -0.00032011, -325.39951597, -0.00106705, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 130.15980639, 0.02189396, 130.15980639, 0.06568188, 91.11186447, -1626.02913654, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 32.5399516, 0.0001067, 97.61985479, 0.00032011, 325.39951597, 0.00106705, -32.5399516, -0.0001067, -97.61985479, -0.00032011, -325.39951597, -0.00106705, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.8, 10.7, 3.3)
    ops.node(122015, 7.8, 10.7, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.09, 30459682.73689429, 12691534.47370596, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 94.51280891, 0.00103386, 112.46837553, 0.0106792, 11.24683755, 0.04143029, -94.51280891, -0.00103386, -112.46837553, -0.0106792, -11.24683755, -0.04143029, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 105.0268822, 0.00103386, 124.97991504, 0.0106792, 12.4979915, 0.04143029, -105.0268822, -0.00103386, -124.97991504, -0.0106792, -12.4979915, -0.04143029, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 133.10403861, 0.0206771, 133.10403861, 0.0620313, 93.17282703, -1649.23705473, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 33.27600965, 0.00010662, 99.82802896, 0.00031987, 332.76009653, 0.00106624, -33.27600965, -0.00010662, -99.82802896, -0.00031987, -332.76009653, -0.00106624, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 133.10403861, 0.0206771, 133.10403861, 0.0620313, 93.17282703, -1649.23705473, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 33.27600965, 0.00010662, 99.82802896, 0.00031987, 332.76009653, 0.00106624, -33.27600965, -0.00010662, -99.82802896, -0.00031987, -332.76009653, -0.00106624, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 10.8, 10.7, 3.3)
    ops.node(122016, 10.8, 10.7, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.09, 31022146.02594959, 12925894.177479, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 97.09835204, 0.00102824, 115.48809517, 0.00994126, 11.54880952, 0.0418701, -97.09835204, -0.00102824, -115.48809517, -0.00994126, -11.54880952, -0.0418701, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 108.82231578, 0.00102824, 129.43249496, 0.00994126, 12.9432495, 0.0418701, -108.82231578, -0.00102824, -129.43249496, -0.00994126, -12.9432495, -0.0418701, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 131.56384001, 0.02056479, 131.56384001, 0.06169438, 92.09468801, -1574.11224396, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 32.89096, 0.00010348, 98.67288001, 0.00031044, 328.90960003, 0.0010348, -32.89096, -0.00010348, -98.67288001, -0.00031044, -328.90960003, -0.0010348, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 131.56384001, 0.02056479, 131.56384001, 0.06169438, 92.09468801, -1574.11224396, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 32.89096, 0.00010348, 98.67288001, 0.00031044, 328.90960003, 0.0010348, -32.89096, -0.00010348, -98.67288001, -0.00031044, -328.90960003, -0.0010348, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 14.7, 10.7, 3.3)
    ops.node(122017, 14.7, 10.7, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.09, 29648948.29106077, 12353728.45460865, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 102.51974583, 0.0011418, 121.61965418, 0.00905265, 12.16196542, 0.03515935, -102.51974583, -0.0011418, -121.61965418, -0.00905265, -12.16196542, -0.03515935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 112.23580668, 0.0011418, 133.14586261, 0.00905265, 13.31458626, 0.03515935, -112.23580668, -0.0011418, -133.14586261, -0.00905265, -13.31458626, -0.03515935, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 130.61994056, 0.02283601, 130.61994056, 0.06850804, 91.43395839, -1643.63938961, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 32.65498514, 0.0001075, 97.96495542, 0.00032249, 326.54985141, 0.00107495, -32.65498514, -0.0001075, -97.96495542, -0.00032249, -326.54985141, -0.00107495, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 130.61994056, 0.02283601, 130.61994056, 0.06850804, 91.43395839, -1643.63938961, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 32.65498514, 0.0001075, 97.96495542, 0.00032249, 326.54985141, 0.00107495, -32.65498514, -0.0001075, -97.96495542, -0.00032249, -326.54985141, -0.00107495, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 18.6, 10.7, 3.3)
    ops.node(122018, 18.6, 10.7, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.0625, 31852761.18597458, 13271983.82748941, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 57.79012728, 0.00123591, 68.62379325, 0.01051207, 6.86237933, 0.04857663, -57.79012728, -0.00123591, -68.62379325, -0.01051207, -6.86237933, -0.04857663, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 61.27212567, 0.00123591, 72.75854686, 0.01051207, 7.27585469, 0.04857663, -61.27212567, -0.00123591, -72.75854686, -0.01051207, -7.27585469, -0.04857663, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 98.10169714, 0.02471817, 98.10169714, 0.07415451, 68.671188, -1207.51168113, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 24.52542428, 0.00010821, 73.57627285, 0.00032464, 245.25424285, 0.00108214, -24.52542428, -0.00010821, -73.57627285, -0.00032464, -245.25424285, -0.00108214, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 98.10169714, 0.02471817, 98.10169714, 0.07415451, 68.671188, -1207.51168113, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 24.52542428, 0.00010821, 73.57627285, 0.00032464, 245.25424285, 0.00108214, -24.52542428, -0.00010821, -73.57627285, -0.00032464, -245.25424285, -0.00108214, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.35)
    ops.node(123001, 0.0, 0.0, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 31093670.5558692, 12955696.0649455, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 42.25818385, 0.00112262, 50.59453139, 0.01181701, 5.05945314, 0.0569614, -42.25818385, -0.00112262, -50.59453139, -0.01181701, -5.05945314, -0.0569614, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 42.25818385, 0.00112262, 50.59453139, 0.01181701, 5.05945314, 0.0569614, -42.25818385, -0.00112262, -50.59453139, -0.01181701, -5.05945314, -0.0569614, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 93.0211651, 0.02245239, 93.0211651, 0.06735716, 65.11481557, -1221.83652341, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 23.25529127, 0.00010511, 69.76587382, 0.00031534, 232.55291274, 0.00105114, -23.25529127, -0.00010511, -69.76587382, -0.00031534, -232.55291274, -0.00105114, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 93.0211651, 0.02245239, 93.0211651, 0.06735716, 65.11481557, -1221.83652341, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 23.25529127, 0.00010511, 69.76587382, 0.00031534, 232.55291274, 0.00105114, -23.25529127, -0.00010511, -69.76587382, -0.00031534, -232.55291274, -0.00105114, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.9, 0.0, 6.35)
    ops.node(123002, 3.9, 0.0, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 31197529.69108484, 12998970.70461868, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 60.26210025, 0.0013246, 71.52508251, 0.01119854, 7.15250825, 0.04637803, -60.26210025, -0.0013246, -71.52508251, -0.01119854, -7.15250825, -0.04637803, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 63.58698589, 0.0013246, 75.47138904, 0.01119854, 7.5471389, 0.04637803, -63.58698589, -0.0013246, -75.47138904, -0.01119854, -7.5471389, -0.04637803, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 102.04016038, 0.02649192, 102.04016038, 0.07947577, 71.42811226, -1323.40813496, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 25.51004009, 0.00011492, 76.53012028, 0.00034477, 255.10040094, 0.00114922, -25.51004009, -0.00011492, -76.53012028, -0.00034477, -255.10040094, -0.00114922, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 102.04016038, 0.02649192, 102.04016038, 0.07947577, 71.42811226, -1323.40813496, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 25.51004009, 0.00011492, 76.53012028, 0.00034477, 255.10040094, 0.00114922, -25.51004009, -0.00011492, -76.53012028, -0.00034477, -255.10040094, -0.00114922, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 14.7, 0.0, 6.35)
    ops.node(123005, 14.7, 0.0, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 30639979.47479929, 12766658.1144997, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 60.20406374, 0.00127033, 71.48661048, 0.00956168, 7.14866105, 0.04336645, -60.20406374, -0.00127033, -71.48661048, -0.00956168, -7.14866105, -0.04336645, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 63.89029621, 0.00127033, 75.8636616, 0.00956168, 7.58636616, 0.04336645, -63.89029621, -0.00127033, -75.8636616, -0.00956168, -7.58636616, -0.04336645, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 90.1811646, 0.02540668, 90.1811646, 0.07622005, 63.12681522, -1214.51729393, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 22.54529115, 0.00010341, 67.63587345, 0.00031024, 225.45291151, 0.00103414, -22.54529115, -0.00010341, -67.63587345, -0.00031024, -225.45291151, -0.00103414, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 90.1811646, 0.02540668, 90.1811646, 0.07622005, 63.12681522, -1214.51729393, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 22.54529115, 0.00010341, 67.63587345, 0.00031024, 225.45291151, 0.00103414, -22.54529115, -0.00010341, -67.63587345, -0.00031024, -225.45291151, -0.00103414, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 18.6, 0.0, 6.35)
    ops.node(123006, 18.6, 0.0, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 32743280.02781167, 13643033.34492153, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 41.93688702, 0.00130998, 50.03307648, 0.01096425, 5.00330765, 0.05901361, -41.93688702, -0.00130998, -50.03307648, -0.01096425, -5.00330765, -0.05901361, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 41.93688702, 0.00130998, 50.03307648, 0.01096425, 5.00330765, 0.05901361, -41.93688702, -0.00130998, -50.03307648, -0.01096425, -5.00330765, -0.05901361, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 93.13524836, 0.02619958, 93.13524836, 0.07859875, 65.19467386, -1126.78889249, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 23.28381209, 9.994e-05, 69.85143627, 0.00029982, 232.83812091, 0.00099941, -23.28381209, -9.994e-05, -69.85143627, -0.00029982, -232.83812091, -0.00099941, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 93.13524836, 0.02619958, 93.13524836, 0.07859875, 65.19467386, -1126.78889249, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 23.28381209, 9.994e-05, 69.85143627, 0.00029982, 232.83812091, 0.00099941, -23.28381209, -9.994e-05, -69.85143627, -0.00029982, -232.83812091, -0.00099941, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 5.35, 6.35)
    ops.node(123007, 0.0, 5.35, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 31552901.56802548, 13147042.32001062, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 58.19545179, 0.00126071, 68.96511128, 0.01070892, 6.89651113, 0.04548316, -58.19545179, -0.00126071, -68.96511128, -0.01070892, -6.89651113, -0.04548316, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 58.19545179, 0.00126071, 68.96511128, 0.01070892, 6.89651113, 0.04548316, -58.19545179, -0.00126071, -68.96511128, -0.01070892, -6.89651113, -0.04548316, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 106.05025575, 0.02521417, 106.05025575, 0.07564252, 74.23517902, -1393.15680619, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 26.51256394, 0.00011809, 79.53769181, 0.00035428, 265.12563936, 0.00118093, -26.51256394, -0.00011809, -79.53769181, -0.00035428, -265.12563936, -0.00118093, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 106.05025575, 0.02521417, 106.05025575, 0.07564252, 74.23517902, -1393.15680619, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 26.51256394, 0.00011809, 79.53769181, 0.00035428, 265.12563936, 0.00118093, -26.51256394, -0.00011809, -79.53769181, -0.00035428, -265.12563936, -0.00118093, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 3.9, 5.35, 6.35)
    ops.node(123008, 3.9, 5.35, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 29383932.72866164, 12243305.30360902, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 147.15213781, 0.00090792, 175.82647466, 0.00911681, 17.58264747, 0.0338384, -147.15213781, -0.00090792, -175.82647466, -0.00911681, -17.58264747, -0.0338384, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 140.34099803, 0.00090792, 167.68810362, 0.00911681, 16.76881036, 0.0338384, -140.34099803, -0.00090792, -167.68810362, -0.00911681, -16.76881036, -0.0338384, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 145.95997795, 0.01815835, 145.95997795, 0.05447506, 102.17198457, -1576.0530323, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 36.48999449, 8.905e-05, 109.46998347, 0.00026714, 364.89994488, 0.00089047, -36.48999449, -8.905e-05, -109.46998347, -0.00026714, -364.89994488, -0.00089047, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 145.95997795, 0.01815835, 145.95997795, 0.05447506, 102.17198457, -1576.0530323, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 36.48999449, 8.905e-05, 109.46998347, 0.00026714, 364.89994488, 0.00089047, -36.48999449, -8.905e-05, -109.46998347, -0.00026714, -364.89994488, -0.00089047, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 7.8, 5.35, 6.35)
    ops.node(123009, 7.8, 5.35, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 32173567.68366997, 13405653.20152915, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 153.674059, 0.00089978, 183.32584987, 0.00914231, 18.33258499, 0.03440775, -153.674059, -0.00089978, -183.32584987, -0.00914231, -18.33258499, -0.03440775, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 153.674059, 0.00089978, 183.32584987, 0.00914231, 18.33258499, 0.03440775, -153.674059, -0.00089978, -183.32584987, -0.00914231, -18.33258499, -0.03440775, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 135.29595151, 0.01799557, 135.29595151, 0.05398671, 94.70716606, -1343.89437694, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 33.82398788, 7.538e-05, 101.47196363, 0.00022615, 338.23987878, 0.00075384, -33.82398788, -7.538e-05, -101.47196363, -0.00022615, -338.23987878, -0.00075384, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 135.29595151, 0.01799557, 135.29595151, 0.05398671, 94.70716606, -1343.89437694, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 33.82398788, 7.538e-05, 101.47196363, 0.00022615, 338.23987878, 0.00075384, -33.82398788, -7.538e-05, -101.47196363, -0.00022615, -338.23987878, -0.00075384, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 10.8, 5.35, 6.35)
    ops.node(123010, 10.8, 5.35, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 34740952.45671548, 14475396.85696478, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 148.22664143, 0.00090378, 175.63292224, 0.00940189, 17.56329222, 0.0370203, -148.22664143, -0.00090378, -175.63292224, -0.00940189, -17.56329222, -0.0370203, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 148.22664143, 0.00090378, 175.63292224, 0.00940189, 17.56329222, 0.0370203, -148.22664143, -0.00090378, -175.63292224, -0.00940189, -17.56329222, -0.0370203, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 149.32759254, 0.01807557, 149.32759254, 0.05422671, 104.52931478, -1338.39416256, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 37.33189814, 7.705e-05, 111.99569441, 0.00023116, 373.31898135, 0.00077054, -37.33189814, -7.705e-05, -111.99569441, -0.00023116, -373.31898135, -0.00077054, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 149.32759254, 0.01807557, 149.32759254, 0.05422671, 104.52931478, -1338.39416256, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 37.33189814, 7.705e-05, 111.99569441, 0.00023116, 373.31898135, 0.00077054, -37.33189814, -7.705e-05, -111.99569441, -0.00023116, -373.31898135, -0.00077054, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 14.7, 5.35, 6.35)
    ops.node(123011, 14.7, 5.35, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 31173006.9773976, 12988752.907249, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 143.08274907, 0.00090335, 170.66570535, 0.01102357, 17.06657053, 0.03858011, -143.08274907, -0.00090335, -170.66570535, -0.01102357, -17.06657053, -0.03858011, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 137.05623702, 0.00090335, 163.47742488, 0.01102357, 16.34774249, 0.03858011, -137.05623702, -0.00090335, -163.47742488, -0.01102357, -16.34774249, -0.03858011, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 159.06627933, 0.01806706, 159.06627933, 0.05420117, 111.34639553, -1700.3380754, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 39.76656983, 9.147e-05, 119.2997095, 0.00027442, 397.66569832, 0.00091474, -39.76656983, -9.147e-05, -119.2997095, -0.00027442, -397.66569832, -0.00091474, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 159.06627933, 0.01806706, 159.06627933, 0.05420117, 111.34639553, -1700.3380754, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 39.76656983, 9.147e-05, 119.2997095, 0.00027442, 397.66569832, 0.00091474, -39.76656983, -9.147e-05, -119.2997095, -0.00027442, -397.66569832, -0.00091474, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 18.6, 5.35, 6.35)
    ops.node(123012, 18.6, 5.35, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 33548430.65450311, 13978512.77270963, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 58.73373264, 0.00121576, 69.39073584, 0.01093323, 6.93907358, 0.05018388, -58.73373264, -0.00121576, -69.39073584, -0.01093323, -6.93907358, -0.05018388, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 58.73373264, 0.00121576, 69.39073584, 0.01093323, 6.93907358, 0.05018388, -58.73373264, -0.00121576, -69.39073584, -0.01093323, -6.93907358, -0.05018388, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 110.11415806, 0.02431528, 110.11415806, 0.07294585, 77.07991064, -1382.74142865, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 27.52853951, 0.00011532, 82.58561854, 0.00034597, 275.28539515, 0.00115325, -27.52853951, -0.00011532, -82.58561854, -0.00034597, -275.28539515, -0.00115325, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 110.11415806, 0.02431528, 110.11415806, 0.07294585, 77.07991064, -1382.74142865, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 27.52853951, 0.00011532, 82.58561854, 0.00034597, 275.28539515, 0.00115325, -27.52853951, -0.00011532, -82.58561854, -0.00034597, -275.28539515, -0.00115325, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 10.7, 6.35)
    ops.node(123013, 0.0, 10.7, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 30419003.01311731, 12674584.58879888, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 42.40806413, 0.00116824, 50.83007896, 0.01266346, 5.0830079, 0.05647847, -42.40806413, -0.00116824, -50.83007896, -0.01266346, -5.0830079, -0.05647847, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 42.40806413, 0.00116824, 50.83007896, 0.01266346, 5.0830079, 0.05647847, -42.40806413, -0.00116824, -50.83007896, -0.01266346, -5.0830079, -0.05647847, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 94.96686484, 0.02336483, 94.96686484, 0.0700945, 66.47680539, -1321.12205026, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 23.74171621, 0.00010969, 71.22514863, 0.00032908, 237.4171621, 0.00109693, -23.74171621, -0.00010969, -71.22514863, -0.00032908, -237.4171621, -0.00109693, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 94.96686484, 0.02336483, 94.96686484, 0.0700945, 66.47680539, -1321.12205026, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 23.74171621, 0.00010969, 71.22514863, 0.00032908, 237.4171621, 0.00109693, -23.74171621, -0.00010969, -71.22514863, -0.00032908, -237.4171621, -0.00109693, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 3.9, 10.7, 6.35)
    ops.node(123014, 3.9, 10.7, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 31490873.63180486, 13121197.34658536, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 62.29821433, 0.00129903, 73.91997359, 0.00989166, 7.39199736, 0.04577327, -62.29821433, -0.00129903, -73.91997359, -0.00989166, -7.39199736, -0.04577327, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 66.31185151, 0.00129903, 78.68235654, 0.00989166, 7.86823565, 0.04577327, -66.31185151, -0.00129903, -78.68235654, -0.00989166, -7.86823565, -0.04577327, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 96.87920857, 0.02598068, 96.87920857, 0.07794203, 67.815446, -1207.09704402, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 24.21980214, 0.00010809, 72.65940643, 0.00032428, 242.19802143, 0.00108093, -24.21980214, -0.00010809, -72.65940643, -0.00032428, -242.19802143, -0.00108093, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 96.87920857, 0.02598068, 96.87920857, 0.07794203, 67.815446, -1207.09704402, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 24.21980214, 0.00010809, 72.65940643, 0.00032428, 242.19802143, 0.00108093, -24.21980214, -0.00010809, -72.65940643, -0.00032428, -242.19802143, -0.00108093, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.8, 10.7, 6.35)
    ops.node(123015, 7.8, 10.7, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 30833253.78289012, 12847189.07620422, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 56.44551541, 0.00130173, 67.21542381, 0.01023831, 6.72154238, 0.04771499, -56.44551541, -0.00130173, -67.21542381, -0.01023831, -6.72154238, -0.04771499, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 59.84134751, 0.00130173, 71.25918694, 0.01023831, 7.12591869, 0.04771499, -59.84134751, -0.00130173, -71.25918694, -0.01023831, -7.12591869, -0.04771499, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 93.45008081, 0.02603469, 93.45008081, 0.07810407, 65.41505657, -1210.06832267, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 23.3625202, 0.00010649, 70.08756061, 0.00031947, 233.62520203, 0.00106491, -23.3625202, -0.00010649, -70.08756061, -0.00031947, -233.62520203, -0.00106491, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 93.45008081, 0.02603469, 93.45008081, 0.07810407, 65.41505657, -1210.06832267, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 23.3625202, 0.00010649, 70.08756061, 0.00031947, 233.62520203, 0.00106491, -23.3625202, -0.00010649, -70.08756061, -0.00031947, -233.62520203, -0.00106491, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 10.8, 10.7, 6.35)
    ops.node(123016, 10.8, 10.7, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 30876581.74064044, 12865242.39193352, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 57.54204289, 0.00117954, 68.51805766, 0.01104039, 6.85180577, 0.04861874, -57.54204289, -0.00117954, -68.51805766, -0.01104039, -6.85180577, -0.04861874, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 61.92866695, 0.00117954, 73.74142036, 0.01104039, 7.37414204, 0.04861874, -61.92866695, -0.00117954, -73.74142036, -0.01104039, -7.37414204, -0.04861874, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 97.25902873, 0.02359089, 97.25902873, 0.07077267, 68.08132011, -1246.02270223, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 24.31475718, 0.00011068, 72.94427154, 0.00033203, 243.14757181, 0.00110676, -24.31475718, -0.00011068, -72.94427154, -0.00033203, -243.14757181, -0.00110676, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 97.25902873, 0.02359089, 97.25902873, 0.07077267, 68.08132011, -1246.02270223, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 24.31475718, 0.00011068, 72.94427154, 0.00033203, 243.14757181, 0.00110676, -24.31475718, -0.00011068, -72.94427154, -0.00033203, -243.14757181, -0.00110676, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 14.7, 10.7, 6.35)
    ops.node(123017, 14.7, 10.7, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 32628585.07440268, 13595243.78100112, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 62.90422749, 0.00123187, 74.52116168, 0.01176175, 7.45211617, 0.05022897, -62.90422749, -0.00123187, -74.52116168, -0.01176175, -7.45211617, -0.05022897, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 67.33570403, 0.00123187, 79.77102792, 0.01176175, 7.97710279, 0.05022897, -67.33570403, -0.00123187, -79.77102792, -0.01176175, -7.97710279, -0.05022897, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 108.85699347, 0.02463747, 108.85699347, 0.07391242, 76.19989543, -1411.29532569, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 27.21424837, 0.00011722, 81.6427451, 0.00035167, 272.14248366, 0.00117222, -27.21424837, -0.00011722, -81.6427451, -0.00035167, -272.14248366, -0.00117222, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 108.85699347, 0.02463747, 108.85699347, 0.07391242, 76.19989543, -1411.29532569, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 27.21424837, 0.00011722, 81.6427451, 0.00035167, 272.14248366, 0.00117222, -27.21424837, -0.00011722, -81.6427451, -0.00035167, -272.14248366, -0.00117222, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 18.6, 10.7, 6.35)
    ops.node(123018, 18.6, 10.7, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 31340563.46419737, 13058568.11008224, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 42.61190363, 0.0011513, 50.99485637, 0.0124751, 5.09948564, 0.05808465, -42.61190363, -0.0011513, -50.99485637, -0.0124751, -5.09948564, -0.05808465, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 42.61190363, 0.0011513, 50.99485637, 0.0124751, 5.09948564, 0.05808465, -42.61190363, -0.0011513, -50.99485637, -0.0124751, -5.09948564, -0.05808465, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 94.13653101, 0.02302591, 94.13653101, 0.06907774, 65.8955717, -1239.75541473, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 23.53413275, 0.00010554, 70.60239826, 0.00031661, 235.34132752, 0.00105537, -23.53413275, -0.00010554, -70.60239826, -0.00031661, -235.34132752, -0.00105537, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 94.13653101, 0.02302591, 94.13653101, 0.06907774, 65.8955717, -1239.75541473, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 23.53413275, 0.00010554, 70.60239826, 0.00031661, 235.34132752, 0.00105537, -23.53413275, -0.00010554, -70.60239826, -0.00031661, -235.34132752, -0.00105537, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.4)
    ops.node(124001, 0.0, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 34483736.1112569, 14368223.37969038, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 29.40747137, 0.00101435, 35.1205005, 0.01089028, 3.51205005, 0.07134936, -29.40747137, -0.00101435, -35.1205005, -0.01089028, -3.51205005, -0.07134936, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 29.40747137, 0.00101435, 35.1205005, 0.01089028, 3.51205005, 0.07134936, -29.40747137, -0.00101435, -35.1205005, -0.01089028, -3.51205005, -0.07134936, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 77.17068771, 0.02028706, 77.17068771, 0.06086119, 54.0194814, -1254.86121597, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 19.29267193, 7.863e-05, 57.87801578, 0.00023589, 192.92671928, 0.0007863, -19.29267193, -7.863e-05, -57.87801578, -0.00023589, -192.92671928, -0.0007863, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 77.17068771, 0.02028706, 77.17068771, 0.06086119, 54.0194814, -1254.86121597, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 19.29267193, 7.863e-05, 57.87801578, 0.00023589, 192.92671928, 0.0007863, -19.29267193, -7.863e-05, -57.87801578, -0.00023589, -192.92671928, -0.0007863, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.9, 0.0, 9.4)
    ops.node(124002, 3.9, 0.0, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 31381350.19339714, 13075562.58058214, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 35.24037474, 0.00125418, 42.33509403, 0.0109094, 4.2335094, 0.06224289, -35.24037474, -0.00125418, -42.33509403, -0.0109094, -4.2335094, -0.06224289, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 35.24037474, 0.00125418, 42.33509403, 0.0109094, 4.2335094, 0.06224289, -35.24037474, -0.00125418, -42.33509403, -0.0109094, -4.2335094, -0.06224289, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 77.63788593, 0.02508367, 77.63788593, 0.075251, 54.34652015, -1060.9851297, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 19.40947148, 8.693e-05, 58.22841445, 0.00026078, 194.09471483, 0.00086927, -19.40947148, -8.693e-05, -58.22841445, -0.00026078, -194.09471483, -0.00086927, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 77.63788593, 0.02508367, 77.63788593, 0.075251, 54.34652015, -1060.9851297, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 19.40947148, 8.693e-05, 58.22841445, 0.00026078, 194.09471483, 0.00086927, -19.40947148, -8.693e-05, -58.22841445, -0.00026078, -194.09471483, -0.00086927, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 14.7, 0.0, 9.4)
    ops.node(124005, 14.7, 0.0, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 28676680.34297918, 11948616.80957466, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 36.5273184, 0.00110764, 44.09554378, 0.01239584, 4.40955438, 0.05916829, -36.5273184, -0.00110764, -44.09554378, -0.01239584, -4.40955438, -0.05916829, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 36.5273184, 0.00110764, 44.09554378, 0.01239584, 4.40955438, 0.05916829, -36.5273184, -0.00110764, -44.09554378, -0.01239584, -4.40955438, -0.05916829, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 82.54210598, 0.02215271, 82.54210598, 0.06645813, 57.77947419, -1207.38286353, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 20.6355265, 0.00010113, 61.90657949, 0.0003034, 206.35526496, 0.00101134, -20.6355265, -0.00010113, -61.90657949, -0.0003034, -206.35526496, -0.00101134, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 82.54210598, 0.02215271, 82.54210598, 0.06645813, 57.77947419, -1207.38286353, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 20.6355265, 0.00010113, 61.90657949, 0.0003034, 206.35526496, 0.00101134, -20.6355265, -0.00010113, -61.90657949, -0.0003034, -206.35526496, -0.00101134, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 18.6, 0.0, 9.4)
    ops.node(124006, 18.6, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 30540629.80366812, 12725262.41819505, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 28.60433628, 0.00107469, 34.58542586, 0.01424019, 3.45854259, 0.07170231, -28.60433628, -0.00107469, -34.58542586, -0.01424019, -3.45854259, -0.07170231, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 28.60433628, 0.00107469, 34.58542586, 0.01424019, 3.45854259, 0.07170231, -28.60433628, -0.00107469, -34.58542586, -0.01424019, -3.45854259, -0.07170231, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 85.08599166, 0.02149377, 85.08599166, 0.0644813, 59.56019416, -1699.42108988, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 21.27149792, 9.789e-05, 63.81449375, 0.00029367, 212.71497915, 0.00097889, -21.27149792, -9.789e-05, -63.81449375, -0.00029367, -212.71497915, -0.00097889, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 85.08599166, 0.02149377, 85.08599166, 0.0644813, 59.56019416, -1699.42108988, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 21.27149792, 9.789e-05, 63.81449375, 0.00029367, 212.71497915, 0.00097889, -21.27149792, -9.789e-05, -63.81449375, -0.00029367, -212.71497915, -0.00097889, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 5.35, 9.4)
    ops.node(124007, 0.0, 5.35, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 33180308.59191259, 13825128.57996358, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 36.76363792, 0.00111953, 43.95465661, 0.01195467, 4.39546566, 0.06566278, -36.76363792, -0.00111953, -43.95465661, -0.01195467, -4.39546566, -0.06566278, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 36.76363792, 0.00111953, 43.95465661, 0.01195467, 4.39546566, 0.06566278, -36.76363792, -0.00111953, -43.95465661, -0.01195467, -4.39546566, -0.06566278, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 90.99762085, 0.02239067, 90.99762085, 0.06717202, 63.6983346, -1192.43587751, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 22.74940521, 9.636e-05, 68.24821564, 0.00028908, 227.49405213, 0.00096361, -22.74940521, -9.636e-05, -68.24821564, -0.00028908, -227.49405213, -0.00096361, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 90.99762085, 0.02239067, 90.99762085, 0.06717202, 63.6983346, -1192.43587751, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 22.74940521, 9.636e-05, 68.24821564, 0.00028908, 227.49405213, 0.00096361, -22.74940521, -9.636e-05, -68.24821564, -0.00028908, -227.49405213, -0.00096361, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 3.9, 5.35, 9.4)
    ops.node(124008, 3.9, 5.35, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 30732571.37929501, 12805238.07470626, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 108.66537837, 0.00089998, 130.8942035, 0.01124946, 13.08942035, 0.04668537, -108.66537837, -0.00089998, -130.8942035, -0.01124946, -13.08942035, -0.04668537, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 103.01638653, 0.00089998, 124.08964165, 0.01124946, 12.40896416, 0.04668537, -103.01638653, -0.00089998, -124.08964165, -0.01124946, -12.40896416, -0.04668537, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 135.27767002, 0.01799965, 135.27767002, 0.05399895, 94.69436901, -1378.11935416, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 33.8194175, 7.891e-05, 101.45825251, 0.00023673, 338.19417504, 0.00078908, -33.8194175, -7.891e-05, -101.45825251, -0.00023673, -338.19417504, -0.00078908, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 135.27767002, 0.01799965, 135.27767002, 0.05399895, 94.69436901, -1378.11935416, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 33.8194175, 7.891e-05, 101.45825251, 0.00023673, 338.19417504, 0.00078908, -33.8194175, -7.891e-05, -101.45825251, -0.00023673, -338.19417504, -0.00078908, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 7.8, 5.35, 9.4)
    ops.node(124009, 7.8, 5.35, 11.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 27774971.16689382, 11572904.65287242, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 114.99367787, 0.00083487, 139.46158766, 0.01194816, 13.94615877, 0.04000026, -114.99367787, -0.00083487, -139.46158766, -0.01194816, -13.94615877, -0.04000026, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 114.99367787, 0.00083487, 139.46158766, 0.01194816, 13.94615877, 0.04000026, -114.99367787, -0.00083487, -139.46158766, -0.01194816, -13.94615877, -0.04000026, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 112.38491873, 0.01669747, 112.38491873, 0.0500924, 78.66944311, -1113.92372138, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 28.09622968, 7.254e-05, 84.28868904, 0.00021761, 280.96229681, 0.00072536, -28.09622968, -7.254e-05, -84.28868904, -0.00021761, -280.96229681, -0.00072536, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 112.38491873, 0.01669747, 112.38491873, 0.0500924, 78.66944311, -1113.92372138, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 28.09622968, 7.254e-05, 84.28868904, 0.00021761, 280.96229681, 0.00072536, -28.09622968, -7.254e-05, -84.28868904, -0.00021761, -280.96229681, -0.00072536, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 10.8, 5.35, 9.4)
    ops.node(124010, 10.8, 5.35, 11.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 29920603.87423344, 12466918.2809306, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 116.65473076, 0.00086632, 140.96217532, 0.00983666, 14.09621753, 0.03973228, -116.65473076, -0.00086632, -140.96217532, -0.00983666, -14.09621753, -0.03973228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 116.65473076, 0.00086632, 140.96217532, 0.00983666, 14.09621753, 0.03973228, -116.65473076, -0.00086632, -140.96217532, -0.00983666, -14.09621753, -0.03973228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 100.51250594, 0.01732649, 100.51250594, 0.05197946, 70.35875416, -981.33853553, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 25.12812649, 6.022e-05, 75.38437946, 0.00018066, 251.28126486, 0.00060221, -25.12812649, -6.022e-05, -75.38437946, -0.00018066, -251.28126486, -0.00060221, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 100.51250594, 0.01732649, 100.51250594, 0.05197946, 70.35875416, -981.33853553, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 25.12812649, 6.022e-05, 75.38437946, 0.00018066, 251.28126486, 0.00060221, -25.12812649, -6.022e-05, -75.38437946, -0.00018066, -251.28126486, -0.00060221, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 14.7, 5.35, 9.4)
    ops.node(124011, 14.7, 5.35, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 28494389.09857085, 11872662.12440452, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 107.27035078, 0.00087033, 129.73523725, 0.01084577, 12.97352372, 0.04385891, -107.27035078, -0.00087033, -129.73523725, -0.01084577, -12.97352372, -0.04385891, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 101.37345695, 0.00087033, 122.60339779, 0.01084577, 12.26033978, 0.04385891, -101.37345695, -0.00087033, -122.60339779, -0.01084577, -12.26033978, -0.04385891, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 124.9940791, 0.01740655, 124.9940791, 0.05221965, 87.49585537, -1324.11819292, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 31.24851978, 7.864e-05, 93.74555933, 0.00023591, 312.48519775, 0.00078637, -31.24851978, -7.864e-05, -93.74555933, -0.00023591, -312.48519775, -0.00078637, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 124.9940791, 0.01740655, 124.9940791, 0.05221965, 87.49585537, -1324.11819292, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 31.24851978, 7.864e-05, 93.74555933, 0.00023591, 312.48519775, 0.00078637, -31.24851978, -7.864e-05, -93.74555933, -0.00023591, -312.48519775, -0.00078637, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 18.6, 5.35, 9.4)
    ops.node(124012, 18.6, 5.35, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 36225502.4401664, 15093959.35006933, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 36.62502874, 0.0010427, 43.32111283, 0.011139, 4.33211128, 0.06793488, -36.62502874, -0.0010427, -43.32111283, -0.011139, -4.33211128, -0.06793488, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 36.62502874, 0.0010427, 43.32111283, 0.011139, 4.33211128, 0.06793488, -36.62502874, -0.0010427, -43.32111283, -0.011139, -4.33211128, -0.06793488, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 95.56769122, 0.02085391, 95.56769122, 0.06256173, 66.89738386, -1129.12590772, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 23.89192281, 9.269e-05, 71.67576842, 0.00027808, 238.91922806, 0.00092693, -23.89192281, -9.269e-05, -71.67576842, -0.00027808, -238.91922806, -0.00092693, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 95.56769122, 0.02085391, 95.56769122, 0.06256173, 66.89738386, -1129.12590772, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 23.89192281, 9.269e-05, 71.67576842, 0.00027808, 238.91922806, 0.00092693, -23.89192281, -9.269e-05, -71.67576842, -0.00027808, -238.91922806, -0.00092693, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 10.7, 9.4)
    ops.node(124013, 0.0, 10.7, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 34914939.33983225, 14547891.39159677, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 29.65871182, 0.00109508, 35.36230932, 0.01098248, 3.53623093, 0.07169206, -29.65871182, -0.00109508, -35.36230932, -0.01098248, -3.53623093, -0.07169206, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 29.65871182, 0.00109508, 35.36230932, 0.01098248, 3.53623093, 0.07169206, -29.65871182, -0.00109508, -35.36230932, -0.01098248, -3.53623093, -0.07169206, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 81.86569898, 0.02190151, 81.86569898, 0.06570452, 57.30598929, -1264.0821839, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 20.46642474, 8.238e-05, 61.39927423, 0.00024715, 204.66424745, 0.00082384, -20.46642474, -8.238e-05, -61.39927423, -0.00024715, -204.66424745, -0.00082384, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 81.86569898, 0.02190151, 81.86569898, 0.06570452, 57.30598929, -1264.0821839, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 20.46642474, 8.238e-05, 61.39927423, 0.00024715, 204.66424745, 0.00082384, -20.46642474, -8.238e-05, -61.39927423, -0.00024715, -204.66424745, -0.00082384, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 3.9, 10.7, 9.4)
    ops.node(124014, 3.9, 10.7, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 32789356.50358199, 13662231.87649249, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 36.28957224, 0.0011165, 43.43703392, 0.01097403, 4.34370339, 0.06419651, -36.28957224, -0.0011165, -43.43703392, -0.01097403, -4.34370339, -0.06419651, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 36.28957224, 0.0011165, 43.43703392, 0.01097403, 4.34370339, 0.06419651, -36.28957224, -0.0011165, -43.43703392, -0.01097403, -4.34370339, -0.06419651, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 82.68401295, 0.02232999, 82.68401295, 0.06698996, 57.87880906, -1074.50490279, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 20.67100324, 8.86e-05, 62.01300971, 0.0002658, 206.71003237, 0.00088601, -20.67100324, -8.86e-05, -62.01300971, -0.0002658, -206.71003237, -0.00088601, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 82.68401295, 0.02232999, 82.68401295, 0.06698996, 57.87880906, -1074.50490279, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 20.67100324, 8.86e-05, 62.01300971, 0.0002658, 206.71003237, 0.00088601, -20.67100324, -8.86e-05, -62.01300971, -0.0002658, -206.71003237, -0.00088601, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.8, 10.7, 9.4)
    ops.node(124015, 7.8, 10.7, 11.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 31659380.94517132, 13191408.72715472, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 38.94775344, 0.00114892, 46.81536769, 0.01374576, 4.68153677, 0.06740405, -38.94775344, -0.00114892, -46.81536769, -0.01374576, -4.68153677, -0.06740405, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 41.95683817, 0.00114892, 50.43230051, 0.01374576, 5.04323005, 0.06740405, -41.95683817, -0.00114892, -50.43230051, -0.01374576, -5.04323005, -0.06740405, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 87.79107236, 0.02297834, 87.79107236, 0.06893502, 61.45375065, -1279.94067481, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 21.94776809, 9.743e-05, 65.84330427, 0.0002923, 219.4776809, 0.00097432, -21.94776809, -9.743e-05, -65.84330427, -0.0002923, -219.4776809, -0.00097432, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 87.79107236, 0.02297834, 87.79107236, 0.06893502, 61.45375065, -1279.94067481, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 21.94776809, 9.743e-05, 65.84330427, 0.0002923, 219.4776809, 0.00097432, -21.94776809, -9.743e-05, -65.84330427, -0.0002923, -219.4776809, -0.00097432, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 10.8, 10.7, 9.4)
    ops.node(124016, 10.8, 10.7, 11.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 32553738.24122203, 13564057.60050918, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 40.52531385, 0.00112764, 48.59339605, 0.01392309, 4.8593396, 0.06864444, -40.52531385, -0.00112764, -48.59339605, -0.01392309, -4.8593396, -0.06864444, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 44.03612859, 0.00112764, 52.80317001, 0.01392309, 5.280317, 0.06864444, -44.03612859, -0.00112764, -52.80317001, -0.01392309, -5.280317, -0.06864444, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 92.24989308, 0.02255274, 92.24989308, 0.06765822, 64.57492515, -1385.89397094, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 23.06247327, 9.957e-05, 69.18741981, 0.0002987, 230.62473269, 0.00099567, -23.06247327, -9.957e-05, -69.18741981, -0.0002987, -230.62473269, -0.00099567, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 92.24989308, 0.02255274, 92.24989308, 0.06765822, 64.57492515, -1385.89397094, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 23.06247327, 9.957e-05, 69.18741981, 0.0002987, 230.62473269, 0.00099567, -23.06247327, -9.957e-05, -69.18741981, -0.0002987, -230.62473269, -0.00099567, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 14.7, 10.7, 9.4)
    ops.node(124017, 14.7, 10.7, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 29433028.67200749, 12263761.94666979, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 36.16306278, 0.0011031, 43.60919193, 0.01258122, 4.36091919, 0.06076866, -36.16306278, -0.0011031, -43.60919193, -0.01258122, -4.36091919, -0.06076866, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 36.16306278, 0.0011031, 43.60919193, 0.01258122, 4.36091919, 0.06076866, -36.16306278, -0.0011031, -43.60919193, -0.01258122, -4.36091919, -0.06076866, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 84.13168439, 0.02206208, 84.13168439, 0.06618625, 58.89217907, -1212.43985483, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 21.0329211, 0.00010043, 63.09876329, 0.0003013, 210.32921098, 0.00100433, -21.0329211, -0.00010043, -63.09876329, -0.0003013, -210.32921098, -0.00100433, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 84.13168439, 0.02206208, 84.13168439, 0.06618625, 58.89217907, -1212.43985483, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 21.0329211, 0.00010043, 63.09876329, 0.0003013, 210.32921098, 0.00100433, -21.0329211, -0.00010043, -63.09876329, -0.0003013, -210.32921098, -0.00100433, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 18.6, 10.7, 9.4)
    ops.node(124018, 18.6, 10.7, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 30170868.96795686, 12571195.40331536, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 28.88168478, 0.0010452, 34.95247561, 0.01181824, 3.49524756, 0.06891781, -28.88168478, -0.0010452, -34.95247561, -0.01181824, -3.49524756, -0.06891781, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 28.88168478, 0.0010452, 34.95247561, 0.01181824, 3.49524756, 0.06891781, -28.88168478, -0.0010452, -34.95247561, -0.01181824, -3.49524756, -0.06891781, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 69.36197452, 0.02090391, 69.36197452, 0.06271174, 48.55338217, -1196.69258032, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 17.34049363, 8.078e-05, 52.02148089, 0.00024233, 173.40493631, 0.00080777, -17.34049363, -8.078e-05, -52.02148089, -0.00024233, -173.40493631, -0.00080777, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 69.36197452, 0.02090391, 69.36197452, 0.06271174, 48.55338217, -1196.69258032, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 17.34049363, 8.078e-05, 52.02148089, 0.00024233, 173.40493631, 0.00080777, -17.34049363, -8.078e-05, -52.02148089, -0.00024233, -173.40493631, -0.00080777, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 7.8, 0.0, 0.0)
    ops.node(124019, 7.8, 0.0, 1.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 170003, 124019, 0.09, 31286074.76146504, 13035864.48394377, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 149.09518727, 0.0007401, 175.82525859, 0.01361904, 17.58252586, 0.04387932, -149.09518727, -0.0007401, -175.82525859, -0.01361904, -17.58252586, -0.04387932, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 143.45838201, 0.0007401, 169.17787607, 0.01361904, 16.91778761, 0.04387932, -143.45838201, -0.0007401, -169.17787607, -0.01361904, -16.91778761, -0.04387932, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 177.47757082, 0.01480192, 177.47757082, 0.04440577, 124.23429958, -4000.70282984, 0.05, 2, 0, 70003, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 44.36939271, 6.921e-05, 133.10817812, 0.00020762, 443.69392706, 0.00069207, -44.36939271, -6.921e-05, -133.10817812, -0.00020762, -443.69392706, -0.00069207, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 177.47757082, 0.01480192, 177.47757082, 0.04440577, 124.23429958, -4000.70282984, 0.05, 2, 0, 70003, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 44.36939271, 6.921e-05, 133.10817812, 0.00020762, 443.69392706, 0.00069207, -44.36939271, -6.921e-05, -133.10817812, -0.00020762, -443.69392706, -0.00069207, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 7.8, 0.0, 1.725)
    ops.node(121003, 7.8, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 121003, 0.09, 30493132.69180626, 12705471.95491927, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 113.51823046, 0.00076991, 134.15781813, 0.01406686, 13.41578181, 0.04400966, -113.51823046, -0.00076991, -134.15781813, -0.01406686, -13.41578181, -0.04400966, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 113.51823046, 0.00076991, 134.15781813, 0.01406686, 13.41578181, 0.04400966, -113.51823046, -0.00076991, -134.15781813, -0.01406686, -13.41578181, -0.04400966, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 175.79628276, 0.01539828, 175.79628276, 0.04619485, 123.05739793, -4094.35124999, 0.05, 2, 0, 74019, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 43.94907069, 7.033e-05, 131.84721207, 0.000211, 439.49070689, 0.00070334, -43.94907069, -7.033e-05, -131.84721207, -0.000211, -439.49070689, -0.00070334, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 175.79628276, 0.01539828, 175.79628276, 0.04619485, 123.05739793, -4094.35124999, 0.05, 2, 0, 74019, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 43.94907069, 7.033e-05, 131.84721207, 0.000211, 439.49070689, 0.00070334, -43.94907069, -7.033e-05, -131.84721207, -0.000211, -439.49070689, -0.00070334, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 10.8, 0.0, 0.0)
    ops.node(124020, 10.8, 0.0, 1.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 170004, 124020, 0.09, 28169917.09349846, 11737465.45562436, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 146.78285021, 0.00079646, 172.64698401, 0.01213551, 17.2646984, 0.03354154, -146.78285021, -0.00079646, -172.64698401, -0.01213551, -17.2646984, -0.03354154, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 141.56410729, 0.00079646, 166.50866319, 0.01213551, 16.65086632, 0.03354154, -141.56410729, -0.00079646, -166.50866319, -0.01213551, -16.65086632, -0.03354154, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 164.16118762, 0.0159292, 164.16118762, 0.04778761, 114.91283133, -3981.83497878, 0.05, 2, 0, 70004, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 41.0402969, 7.11e-05, 123.12089071, 0.00021329, 410.40296905, 0.00071096, -41.0402969, -7.11e-05, -123.12089071, -0.00021329, -410.40296905, -0.00071096, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 164.16118762, 0.0159292, 164.16118762, 0.04778761, 114.91283133, -3981.83497878, 0.05, 2, 0, 70004, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 41.0402969, 7.11e-05, 123.12089071, 0.00021329, 410.40296905, 0.00071096, -41.0402969, -7.11e-05, -123.12089071, -0.00021329, -410.40296905, -0.00071096, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 10.8, 0.0, 1.725)
    ops.node(121004, 10.8, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 121004, 0.09, 35409311.70032092, 14753879.87513372, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 118.91119503, 0.00072892, 139.54257702, 0.01392764, 13.9542577, 0.05551783, -118.91119503, -0.00072892, -139.54257702, -0.01392764, -13.9542577, -0.05551783, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 118.91119503, 0.00072892, 139.54257702, 0.01392764, 13.9542577, 0.05551783, -118.91119503, -0.00072892, -139.54257702, -0.01392764, -13.9542577, -0.05551783, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 193.72264462, 0.01457831, 193.72264462, 0.04373493, 135.60585123, -3971.23856638, 0.05, 2, 0, 74020, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 48.43066115, 6.675e-05, 145.29198346, 0.00020024, 484.30661154, 0.00066746, -48.43066115, -6.675e-05, -145.29198346, -0.00020024, -484.30661154, -0.00066746, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 193.72264462, 0.01457831, 193.72264462, 0.04373493, 135.60585123, -3971.23856638, 0.05, 2, 0, 74020, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 48.43066115, 6.675e-05, 145.29198346, 0.00020024, 484.30661154, 0.00066746, -48.43066115, -6.675e-05, -145.29198346, -0.00020024, -484.30661154, -0.00066746, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.8, 0.0, 3.3)
    ops.node(124021, 7.8, 0.0, 4.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 171003, 124021, 0.09, 30898239.49953636, 12874266.45814015, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 101.73829111, 0.00071031, 120.87844343, 0.01018699, 12.08784434, 0.03686297, -101.73829111, -0.00071031, -120.87844343, -0.01018699, -12.08784434, -0.03686297, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 101.73829111, 0.00071031, 120.87844343, 0.01018699, 12.08784434, 0.03686297, -101.73829111, -0.00071031, -120.87844343, -0.01018699, -12.08784434, -0.03686297, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 152.42016268, 0.01420614, 152.42016268, 0.04261843, 106.69411387, -3077.78584798, 0.05, 2, 0, 71003, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 38.10504067, 6.018e-05, 114.31512201, 0.00018055, 381.0504067, 0.00060182, -38.10504067, -6.018e-05, -114.31512201, -0.00018055, -381.0504067, -0.00060182, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 152.42016268, 0.01420614, 152.42016268, 0.04261843, 106.69411387, -3077.78584798, 0.05, 2, 0, 71003, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 38.10504067, 6.018e-05, 114.31512201, 0.00018055, 381.0504067, 0.00060182, -38.10504067, -6.018e-05, -114.31512201, -0.00018055, -381.0504067, -0.00060182, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 7.8, 0.0, 4.775)
    ops.node(122003, 7.8, 0.0, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 122003, 0.09, 31191729.16530515, 12996553.81887715, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 100.27851215, 0.00070615, 119.34674828, 0.00926947, 11.93467483, 0.03812671, -100.27851215, -0.00070615, -119.34674828, -0.00926947, -11.93467483, -0.03812671, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 100.27851215, 0.00070615, 119.34674828, 0.00926947, 11.93467483, 0.03812671, -100.27851215, -0.00070615, -119.34674828, -0.00926947, -11.93467483, -0.03812671, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 142.61149592, 0.01412292, 142.61149592, 0.04236876, 99.82804714, -2703.10369263, 0.05, 2, 0, 74021, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 35.65287398, 5.578e-05, 106.95862194, 0.00016734, 356.52873979, 0.0005578, -35.65287398, -5.578e-05, -106.95862194, -0.00016734, -356.52873979, -0.0005578, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 142.61149592, 0.01412292, 142.61149592, 0.04236876, 99.82804714, -2703.10369263, 0.05, 2, 0, 74021, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 35.65287398, 5.578e-05, 106.95862194, 0.00016734, 356.52873979, 0.0005578, -35.65287398, -5.578e-05, -106.95862194, -0.00016734, -356.52873979, -0.0005578, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 10.8, 0.0, 3.3)
    ops.node(124022, 10.8, 0.0, 4.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 171004, 124022, 0.09, 30328327.43030292, 12636803.09595955, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 101.26562353, 0.00071863, 120.36305046, 0.01007391, 12.03630505, 0.03567735, -101.26562353, -0.00071863, -120.36305046, -0.01007391, -12.03630505, -0.03567735, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 101.26562353, 0.00071863, 120.36305046, 0.01007391, 12.03630505, 0.03567735, -101.26562353, -0.00071863, -120.36305046, -0.01007391, -12.03630505, -0.03567735, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 148.42745203, 0.01437255, 148.42745203, 0.04311766, 103.89921642, -3002.21339217, 0.05, 2, 0, 71004, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 37.10686301, 5.971e-05, 111.32058902, 0.00017912, 371.06863008, 0.00059707, -37.10686301, -5.971e-05, -111.32058902, -0.00017912, -371.06863008, -0.00059707, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 148.42745203, 0.01437255, 148.42745203, 0.04311766, 103.89921642, -3002.21339217, 0.05, 2, 0, 71004, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 37.10686301, 5.971e-05, 111.32058902, 0.00017912, 371.06863008, 0.00059707, -37.10686301, -5.971e-05, -111.32058902, -0.00017912, -371.06863008, -0.00059707, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 10.8, 0.0, 4.775)
    ops.node(122004, 10.8, 0.0, 5.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 122004, 0.09, 29991180.37062142, 12496325.15442559, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 95.94730271, 0.00072153, 114.31375142, 0.01016759, 11.43137514, 0.03684332, -95.94730271, -0.00072153, -114.31375142, -0.01016759, -11.43137514, -0.03684332, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 95.94730271, 0.00072153, 114.31375142, 0.01016759, 11.43137514, 0.03684332, -95.94730271, -0.00072153, -114.31375142, -0.01016759, -11.43137514, -0.03684332, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 141.66347097, 0.01443055, 141.66347097, 0.04329165, 99.16442968, -2799.53780838, 0.05, 2, 0, 74022, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 35.41586774, 5.763e-05, 106.24760323, 0.00017288, 354.15867742, 0.00057627, -35.41586774, -5.763e-05, -106.24760323, -0.00017288, -354.15867742, -0.00057627, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 141.66347097, 0.01443055, 141.66347097, 0.04329165, 99.16442968, -2799.53780838, 0.05, 2, 0, 74022, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 35.41586774, 5.763e-05, 106.24760323, 0.00017288, 354.15867742, 0.00057627, -35.41586774, -5.763e-05, -106.24760323, -0.00017288, -354.15867742, -0.00057627, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.8, 0.0, 6.35)
    ops.node(124023, 7.8, 0.0, 7.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 172003, 124023, 0.0625, 30639966.19199067, 12766652.57999611, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 68.261624, 0.00081465, 81.21546328, 0.01115145, 8.12154633, 0.04224862, -68.261624, -0.00081465, -81.21546328, -0.01115145, -8.12154633, -0.04224862, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 68.261624, 0.00081465, 81.21546328, 0.01115145, 8.12154633, 0.04224862, -68.261624, -0.00081465, -81.21546328, -0.01115145, -8.12154633, -0.04224862, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 89.89460847, 0.01629306, 89.89460847, 0.04887918, 62.92622593, -2306.6421008, 0.05, 2, 0, 72003, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 22.47365212, 5.154e-05, 67.42095635, 0.00015463, 224.73652118, 0.00051543, -22.47365212, -5.154e-05, -67.42095635, -0.00015463, -224.73652118, -0.00051543, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 89.89460847, 0.01629306, 89.89460847, 0.04887918, 62.92622593, -2306.6421008, 0.05, 2, 0, 72003, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 22.47365212, 5.154e-05, 67.42095635, 0.00015463, 224.73652118, 0.00051543, -22.47365212, -5.154e-05, -67.42095635, -0.00015463, -224.73652118, -0.00051543, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 7.8, 0.0, 7.825)
    ops.node(123003, 7.8, 0.0, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 123003, 0.0625, 33025542.08895647, 13760642.5370652, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 63.80771924, 0.00081228, 75.85043895, 0.01075279, 7.58504389, 0.04930554, -63.80771924, -0.00081228, -75.85043895, -0.01075279, -7.58504389, -0.04930554, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 63.80771924, 0.00081228, 75.85043895, 0.01075279, 7.58504389, 0.04930554, -63.80771924, -0.00081228, -75.85043895, -0.01075279, -7.58504389, -0.04930554, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 79.39678111, 0.01624559, 79.39678111, 0.04873677, 55.57774678, -2042.46425843, 0.05, 2, 0, 74023, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 19.84919528, 4.224e-05, 59.54758583, 0.00012671, 198.49195278, 0.00042235, -19.84919528, -4.224e-05, -59.54758583, -0.00012671, -198.49195278, -0.00042235, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 79.39678111, 0.01624559, 79.39678111, 0.04873677, 55.57774678, -2042.46425843, 0.05, 2, 0, 74023, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 19.84919528, 4.224e-05, 59.54758583, 0.00012671, 198.49195278, 0.00042235, -19.84919528, -4.224e-05, -59.54758583, -0.00012671, -198.49195278, -0.00042235, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 10.8, 0.0, 6.35)
    ops.node(124024, 10.8, 0.0, 7.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 172004, 124024, 0.0625, 32380365.31471355, 13491818.88113065, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 68.60440511, 0.00085756, 81.44129736, 0.01054546, 8.14412974, 0.04508388, -68.60440511, -0.00085756, -81.44129736, -0.01054546, -8.14412974, -0.04508388, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 68.60440511, 0.00085756, 81.44129736, 0.01054546, 8.14412974, 0.04508388, -68.60440511, -0.00085756, -81.44129736, -0.01054546, -8.14412974, -0.04508388, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 85.86170152, 0.01715114, 85.86170152, 0.05145341, 60.10319106, -2269.09897285, 0.05, 2, 0, 72004, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 21.46542538, 4.658e-05, 64.39627614, 0.00013975, 214.6542538, 0.00046584, -21.46542538, -4.658e-05, -64.39627614, -0.00013975, -214.6542538, -0.00046584, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 85.86170152, 0.01715114, 85.86170152, 0.05145341, 60.10319106, -2269.09897285, 0.05, 2, 0, 72004, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 21.46542538, 4.658e-05, 64.39627614, 0.00013975, 214.6542538, 0.00046584, -21.46542538, -4.658e-05, -64.39627614, -0.00013975, -214.6542538, -0.00046584, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 10.8, 0.0, 7.825)
    ops.node(123004, 10.8, 0.0, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 123004, 0.0625, 30602999.13451618, 12751249.63938174, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 62.68611742, 0.00081092, 74.83263923, 0.01057553, 7.48326392, 0.04482792, -62.68611742, -0.00081092, -74.83263923, -0.01057553, -7.48326392, -0.04482792, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 62.68611742, 0.00081092, 74.83263923, 0.01057553, 7.48326392, 0.04482792, -62.68611742, -0.00081092, -74.83263923, -0.01057553, -7.48326392, -0.04482792, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 71.74184239, 0.01621845, 71.74184239, 0.04865535, 50.21928967, -2022.6011629, 0.05, 2, 0, 74024, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 17.9354606, 4.118e-05, 53.80638179, 0.00012355, 179.35460598, 0.00041184, -17.9354606, -4.118e-05, -53.80638179, -0.00012355, -179.35460598, -0.00041184, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 71.74184239, 0.01621845, 71.74184239, 0.04865535, 50.21928967, -2022.6011629, 0.05, 2, 0, 74024, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 17.9354606, 4.118e-05, 53.80638179, 0.00012355, 179.35460598, 0.00041184, -17.9354606, -4.118e-05, -53.80638179, -0.00012355, -179.35460598, -0.00041184, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.8, 0.0, 9.4)
    ops.node(124025, 7.8, 0.0, 10.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4061, 173003, 124025, 0.0625, 27276067.01378705, 11365027.92241127, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24061, 48.43857188, 0.00077889, 58.64240092, 0.01399557, 5.86424009, 0.05377524, -48.43857188, -0.00077889, -58.64240092, -0.01399557, -5.86424009, -0.05377524, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14061, 48.43857188, 0.00077889, 58.64240092, 0.01399557, 5.86424009, 0.05377524, -48.43857188, -0.00077889, -58.64240092, -0.01399557, -5.86424009, -0.05377524, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24061, 4061, 0.0, 78.48850731, 0.0155779, 78.48850731, 0.04673369, 54.94195512, -2321.32983827, 0.05, 2, 0, 73003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44061, 19.62212683, 5.055e-05, 58.86638048, 0.00015166, 196.22126827, 0.00050553, -19.62212683, -5.055e-05, -58.86638048, -0.00015166, -196.22126827, -0.00050553, 0.4, 0.3, 0.003, 0.0, 0.0, 24061, 2)
    ops.limitCurve('ThreePoint', 14061, 4061, 0.0, 78.48850731, 0.0155779, 78.48850731, 0.04673369, 54.94195512, -2321.32983827, 0.05, 2, 0, 73003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34061, 19.62212683, 5.055e-05, 58.86638048, 0.00015166, 196.22126827, 0.00050553, -19.62212683, -5.055e-05, -58.86638048, -0.00015166, -196.22126827, -0.00050553, 0.4, 0.3, 0.003, 0.0, 0.0, 14061, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4061, 99999, 'P', 44061, 'Vy', 34061, 'Vz', 24061, 'My', 14061, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4061, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4061, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 7.8, 0.0, 10.85)
    ops.node(124003, 7.8, 0.0, 11.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 174025, 124003, 0.0625, 32769380.76241527, 13653908.65100636, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 43.93280554, 0.00071015, 52.77076757, 0.01316076, 5.27707676, 0.06428931, -43.93280554, -0.00071015, -52.77076757, -0.01316076, -5.27707676, -0.06428931, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 43.93280554, 0.00071015, 52.77076757, 0.01316076, 5.27707676, 0.06428931, -43.93280554, -0.00071015, -52.77076757, -0.01316076, -5.27707676, -0.06428931, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 69.16885817, 0.01420299, 69.16885817, 0.04260898, 48.41820072, -2223.76117457, 0.05, 2, 0, 74025, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 17.29221454, 3.708e-05, 51.87664363, 0.00011125, 172.92214543, 0.00037082, -17.29221454, -3.708e-05, -51.87664363, -0.00011125, -172.92214543, -0.00037082, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 69.16885817, 0.01420299, 69.16885817, 0.04260898, 48.41820072, -2223.76117457, 0.05, 2, 0, 74025, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 17.29221454, 3.708e-05, 51.87664363, 0.00011125, 172.92214543, 0.00037082, -17.29221454, -3.708e-05, -51.87664363, -0.00011125, -172.92214543, -0.00037082, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 10.8, 0.0, 9.4)
    ops.node(124026, 10.8, 0.0, 10.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 173004, 124026, 0.0625, 30044257.62528654, 12518440.67720272, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 48.0990597, 0.00078987, 58.00761812, 0.01397767, 5.80076181, 0.05811978, -48.0990597, -0.00078987, -58.00761812, -0.01397767, -5.80076181, -0.05811978, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 48.0990597, 0.00078987, 58.00761812, 0.01397767, 5.80076181, 0.05811978, -48.0990597, -0.00078987, -58.00761812, -0.01397767, -5.80076181, -0.05811978, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 82.85950284, 0.01579746, 82.85950284, 0.04739237, 58.00165199, -2307.31360939, 0.05, 2, 0, 73004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 20.71487571, 4.845e-05, 62.14462713, 0.00014535, 207.14875711, 0.00048451, -20.71487571, -4.845e-05, -62.14462713, -0.00014535, -207.14875711, -0.00048451, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 82.85950284, 0.01579746, 82.85950284, 0.04739237, 58.00165199, -2307.31360939, 0.05, 2, 0, 73004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 20.71487571, 4.845e-05, 62.14462713, 0.00014535, 207.14875711, 0.00048451, -20.71487571, -4.845e-05, -62.14462713, -0.00014535, -207.14875711, -0.00048451, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 10.8, 0.0, 10.85)
    ops.node(124004, 10.8, 0.0, 11.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174026, 124004, 0.0625, 31565896.55974474, 13152456.89989364, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 44.59127099, 0.00071252, 53.75533798, 0.01365361, 5.3755338, 0.06392828, -44.59127099, -0.00071252, -53.75533798, -0.01365361, -5.3755338, -0.06392828, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 44.59127099, 0.00071252, 53.75533798, 0.01365361, 5.3755338, 0.06392828, -44.59127099, -0.00071252, -53.75533798, -0.01365361, -5.3755338, -0.06392828, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 68.47987012, 0.0142504, 68.47987012, 0.04275119, 47.93590908, -2081.3951708, 0.05, 2, 0, 74026, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 17.11996753, 3.811e-05, 51.35990259, 0.00011434, 171.19967529, 0.00038112, -17.11996753, -3.811e-05, -51.35990259, -0.00011434, -171.19967529, -0.00038112, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 68.47987012, 0.0142504, 68.47987012, 0.04275119, 47.93590908, -2081.3951708, 0.05, 2, 0, 74026, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 17.11996753, 3.811e-05, 51.35990259, 0.00011434, 171.19967529, 0.00038112, -17.11996753, -3.811e-05, -51.35990259, -0.00011434, -171.19967529, -0.00038112, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4064, '-orient', 0, 0, 1, 0, 1, 0)
