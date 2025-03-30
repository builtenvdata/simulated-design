import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 3.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.075, 27822730.79933828, 11592804.49972428, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 83.01541551, 0.00158617, 97.86944918, 0.01215048, 9.78694492, 0.03090025, -83.01541551, -0.00158617, -97.86944918, -0.01215048, -9.78694492, -0.03090025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 101.1318833, 0.00131755, 119.22751519, 0.01253706, 11.92275152, 0.03416345, -101.1318833, -0.00131755, -119.22751519, -0.01253706, -11.92275152, -0.03416345, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 113.66689481, 0.03172331, 113.66689481, 0.09516993, 79.56682637, -1486.42478138, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 28.4167237, 0.00012746, 85.25017111, 0.00038239, 284.16723702, 0.00127464, -28.4167237, -0.00012746, -85.25017111, -0.00038239, -284.16723702, -0.00127464, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 122.29488358, 0.026351, 122.29488358, 0.07905301, 85.6064185, -1666.97142283, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 30.57372089, 0.00013714, 91.72116268, 0.00041142, 305.73720894, 0.0013714, -30.57372089, -0.00013714, -91.72116268, -0.00041142, -305.73720894, -0.0013714, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.45, 0.0, 0.0)
    ops.node(121002, 4.45, 0.0, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.175, 29604556.89257659, 12335232.03857358, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 244.30937154, 0.00104973, 291.31385116, 0.01215456, 29.13138512, 0.0332008, -244.30937154, -0.00104973, -291.31385116, -0.01215456, -29.13138512, -0.0332008, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 305.68343378, 0.00081126, 364.49612133, 0.01314323, 36.44961213, 0.04013012, -305.68343378, -0.00081126, -364.49612133, -0.01314323, -36.44961213, -0.04013012, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 213.88907493, 0.02099463, 213.88907493, 0.0629839, 149.72235245, -2196.89477575, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 53.47226873, 9.661e-05, 160.4168062, 0.00028982, 534.72268733, 0.00096607, -53.47226873, -9.661e-05, -160.4168062, -0.00028982, -534.72268733, -0.00096607, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 238.8429191, 0.01622521, 238.8429191, 0.04867562, 167.19004337, -2703.02829671, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 59.71072977, 0.00010788, 179.13218932, 0.00032363, 597.10729775, 0.00107878, -59.71072977, -0.00010788, -179.13218932, -0.00032363, -597.10729775, -0.00107878, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.9, 0.0, 0.0)
    ops.node(121003, 8.9, 0.0, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.175, 29350185.11536952, 12229243.79807063, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 252.11461036, 0.00105534, 300.64576626, 0.01211135, 30.06457663, 0.03276212, -252.11461036, -0.00105534, -300.64576626, -0.01211135, -30.06457663, -0.03276212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 295.84496553, 0.00081572, 352.79405755, 0.01309347, 35.27940575, 0.03957326, -295.84496553, -0.00081572, -352.79405755, -0.01309347, -35.27940575, -0.03957326, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 214.11452645, 0.02110685, 214.11452645, 0.06332054, 149.88016851, -2230.03080117, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 53.52863161, 9.755e-05, 160.58589484, 0.00029264, 535.28631612, 0.00097547, -53.52863161, -9.755e-05, -160.58589484, -0.00029264, -535.28631612, -0.00097547, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 239.80400326, 0.01631442, 239.80400326, 0.04894325, 167.86280228, -2755.59257884, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 59.95100082, 0.00010925, 179.85300245, 0.00032775, 599.51000815, 0.0010925, -59.95100082, -0.00010925, -179.85300245, -0.00032775, -599.51000815, -0.0010925, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 20.8, 0.0, 0.0)
    ops.node(121006, 20.8, 0.0, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.175, 29316645.48374938, 12215268.95156224, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 251.93036488, 0.00106618, 300.42848156, 0.01203298, 30.04284816, 0.03263106, -251.93036488, -0.00106618, -300.42848156, -0.01203298, -30.04284816, -0.03263106, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 296.3826495, 0.0008219, 353.43809941, 0.01300058, 35.34380994, 0.03941282, -296.3826495, -0.0008219, -353.43809941, -0.01300058, -35.34380994, -0.03941282, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 212.90911171, 0.02132358, 212.90911171, 0.06397073, 149.0363782, -2210.51852821, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 53.22727793, 9.711e-05, 159.68183379, 0.00029133, 532.27277929, 0.00097109, -53.22727793, -9.711e-05, -159.68183379, -0.00029133, -532.27277929, -0.00097109, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 238.16607548, 0.01643791, 238.16607548, 0.04931374, 166.71625284, -2724.6262488, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 59.54151887, 0.00010863, 178.62455661, 0.00032589, 595.41518871, 0.00108628, -59.54151887, -0.00010863, -178.62455661, -0.00032589, -595.41518871, -0.00108628, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 25.25, 0.0, 0.0)
    ops.node(121007, 25.25, 0.0, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.175, 29108038.54940441, 12128349.39558517, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 240.92657796, 0.00106881, 287.31645224, 0.01238369, 28.73164522, 0.03265123, -240.92657796, -0.00106881, -287.31645224, -0.01238369, -28.73164522, -0.03265123, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 303.31171873, 0.00082023, 361.71371247, 0.01338545, 36.17137125, 0.03937385, -303.31171873, -0.00082023, -361.71371247, -0.01338545, -36.17137125, -0.03937385, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 212.8844692, 0.02137627, 212.8844692, 0.06412881, 149.01912844, -2233.60929574, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 53.2211173, 9.779e-05, 159.6633519, 0.00029338, 532.211173, 0.00097793, -53.2211173, -9.779e-05, -159.6633519, -0.00029338, -532.211173, -0.00097793, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 238.65306204, 0.01640468, 238.65306204, 0.04921404, 167.05714343, -2761.27592399, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 59.66326551, 0.00010963, 178.98979653, 0.00032889, 596.6326551, 0.00109631, -59.66326551, -0.00010963, -178.98979653, -0.00032889, -596.6326551, -0.00109631, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 29.7, 0.0, 0.0)
    ops.node(121008, 29.7, 0.0, 3.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.075, 28772788.93017679, 11988662.05424033, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 83.82705825, 0.00160909, 98.98166825, 0.01224657, 9.89816682, 0.03337939, -83.82705825, -0.00160909, -98.98166825, -0.01224657, -9.89816682, -0.03337939, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 102.11716313, 0.00133346, 120.57833561, 0.01263066, 12.05783356, 0.03700573, -102.11716313, -0.00133346, -120.57833561, -0.01263066, -12.05783356, -0.03700573, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 114.26354536, 0.0321817, 114.26354536, 0.09654511, 79.98448175, -1447.67298044, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 28.56588634, 0.0001239, 85.69765902, 0.00037171, 285.6588634, 0.00123903, -28.56588634, -0.0001239, -85.69765902, -0.00037171, -285.6588634, -0.00123903, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 122.50771615, 0.02666915, 122.50771615, 0.08000745, 85.7554013, -1617.76931778, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 30.62692904, 0.00013284, 91.88078711, 0.00039853, 306.26929037, 0.00132842, -30.62692904, -0.00013284, -91.88078711, -0.00039853, -306.26929037, -0.00132842, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 5.15, 0.0)
    ops.node(121009, 0.0, 5.15, 3.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.15, 29763744.8946366, 12401560.37276525, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 283.84304929, 0.00083035, 336.92716305, 0.01321015, 33.69271631, 0.04005291, -283.84304929, -0.00083035, -336.92716305, -0.01321015, -33.69271631, -0.04005291, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 199.72558508, 0.00123663, 237.0781139, 0.01185359, 23.70781139, 0.03049918, -199.72558508, -0.00123663, -237.0781139, -0.01185359, -23.70781139, -0.03049918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 229.43126499, 0.01660694, 229.43126499, 0.04982082, 160.60188549, -2802.79252635, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 57.35781625, 0.00012025, 172.07344874, 0.00036075, 573.57816247, 0.00120251, -57.35781625, -0.00012025, -172.07344874, -0.00036075, -573.57816247, -0.00120251, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 194.90152631, 0.02473266, 194.90152631, 0.07419798, 136.43106841, -2114.03280471, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 48.72538158, 0.00010215, 146.17614473, 0.00030646, 487.25381577, 0.00102153, -48.72538158, -0.00010215, -146.17614473, -0.00030646, -487.25381577, -0.00102153, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 4.45, 5.15, 0.0)
    ops.node(121010, 4.45, 5.15, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.4, 29032683.72199382, 12096951.55083076, 0.02037523, 0.00916667, 0.02346667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 947.49012133, 0.00064138, 1139.55434649, 0.01435397, 113.95543465, 0.03745658, -947.49012133, -0.00064138, -1139.55434649, -0.01435397, -113.95543465, -0.03745658, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 801.9264097, 0.00080835, 964.48364492, 0.01309418, 96.44836449, 0.03089649, -801.9264097, -0.00080835, -964.48364492, -0.01309418, -96.44836449, -0.03089649, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 592.39567436, 0.01282768, 592.39567436, 0.03848303, 414.67697206, -3807.97423519, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 148.09891859, 0.00011937, 444.29675577, 0.0003581, 1480.98918591, 0.00119366, -148.09891859, -0.00011937, -444.29675577, -0.0003581, -1480.98918591, -0.00119366, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 374.90727759, 0.01616704, 374.90727759, 0.04850112, 262.43509431, -2954.48326697, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 93.7268194, 7.554e-05, 281.18045819, 0.00022663, 937.26819397, 0.00075543, -93.7268194, -7.554e-05, -281.18045819, -0.00022663, -937.26819397, -0.00075543, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.9, 5.15, 0.0)
    ops.node(121011, 8.9, 5.15, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.4, 28948284.03663175, 12061785.01526323, 0.02037523, 0.00916667, 0.02346667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 954.49350121, 0.00065107, 1148.07534534, 0.01413922, 114.80753453, 0.0371427, -954.49350121, -0.00065107, -1148.07534534, -0.01413922, -114.80753453, -0.0371427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 802.38941496, 0.00082652, 965.12286726, 0.01291126, 96.51228673, 0.03063719, -802.38941496, -0.00082652, -965.12286726, -0.01291126, -96.51228673, -0.03063719, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 588.8203244, 0.01302139, 588.8203244, 0.03906417, 412.17422708, -3767.90971312, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 147.2050811, 0.00011899, 441.6152433, 0.00035697, 1472.05081101, 0.00118991, -147.2050811, -0.00011899, -441.6152433, -0.00035697, -1472.05081101, -0.00118991, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 372.65644345, 0.01653048, 372.65644345, 0.04959144, 260.85951042, -2932.40997224, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 93.16411086, 7.531e-05, 279.49233259, 0.00022592, 931.64110863, 0.00075308, -93.16411086, -7.531e-05, -279.49233259, -0.00022592, -931.64110863, -0.00075308, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 13.35, 5.15, 0.0)
    ops.node(121012, 13.35, 5.15, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.28, 29768114.55131588, 12403381.06304828, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 673.08490025, 0.00069807, 806.85042043, 0.01448913, 80.68504204, 0.04017057, -673.08490025, -0.00069807, -806.85042043, -0.01448913, -80.68504204, -0.04017057, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 497.07434315, 0.00099012, 595.86040721, 0.01296431, 59.58604072, 0.0313334, -497.07434315, -0.00099012, -595.86040721, -0.01296431, -59.58604072, -0.0313334, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 412.87759624, 0.0139615, 412.87759624, 0.0418845, 289.01431737, -3187.55377813, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 103.21939906, 0.00011591, 309.65819718, 0.00034774, 1032.1939906, 0.00115912, -103.21939906, -0.00011591, -309.65819718, -0.00034774, -1032.1939906, -0.00115912, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 284.54254867, 0.01980247, 284.54254867, 0.05940741, 199.17978407, -2366.5584746, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 71.13563717, 7.988e-05, 213.40691151, 0.00023965, 711.35637169, 0.00079883, -71.13563717, -7.988e-05, -213.40691151, -0.00023965, -711.35637169, -0.00079883, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 16.35, 5.15, 0.0)
    ops.node(121013, 16.35, 5.15, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.28, 29558680.10729924, 12316116.71137469, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 678.14895661, 0.00069944, 813.09911452, 0.01426449, 81.30991145, 0.03965527, -678.14895661, -0.00069944, -813.09911452, -0.01426449, -81.30991145, -0.03965527, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 506.02856417, 0.0009864, 606.72714075, 0.01276437, 60.67271407, 0.03092555, -506.02856417, -0.0009864, -606.72714075, -0.01276437, -60.67271407, -0.03092555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 410.33431973, 0.0139887, 410.33431973, 0.0419661, 287.23402381, -3188.85012389, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 102.58357993, 0.00011601, 307.7507398, 0.00034804, 1025.83579933, 0.00116014, -102.58357993, -0.00011601, -307.7507398, -0.00034804, -1025.83579933, -0.00116014, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 282.68810413, 0.01972809, 282.68810413, 0.05918427, 197.88167289, -2367.19673484, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 70.67202603, 7.992e-05, 212.0160781, 0.00023977, 706.72026032, 0.00079925, -70.67202603, -7.992e-05, -212.0160781, -0.00023977, -706.72026032, -0.00079925, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 20.8, 5.15, 0.0)
    ops.node(121014, 20.8, 5.15, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.4, 28532222.42798179, 11888426.01165908, 0.02037523, 0.00916667, 0.02346667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 952.55141685, 0.00065121, 1146.16419656, 0.01377852, 114.61641966, 0.03628114, -952.55141685, -0.00065121, -1146.16419656, -0.01377852, -114.61641966, -0.03628114, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 804.02475034, 0.00082563, 967.44843972, 0.01258708, 96.74484397, 0.02992705, -804.02475034, -0.00082563, -967.44843972, -0.01258708, -96.74484397, -0.02992705, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 578.89898516, 0.01302412, 578.89898516, 0.03907236, 405.22928961, -3731.2762524, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 144.72474629, 0.00011869, 434.17423887, 0.00035608, 1447.2474629, 0.00118692, -144.72474629, -0.00011869, -434.17423887, -0.00035608, -1447.2474629, -0.00118692, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 366.37588125, 0.01651265, 366.37588125, 0.04953795, 256.46311687, -2912.19704525, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 91.59397031, 7.512e-05, 274.78191093, 0.00022536, 915.93970312, 0.00075119, -91.59397031, -7.512e-05, -274.78191093, -0.00022536, -915.93970312, -0.00075119, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 25.25, 5.15, 0.0)
    ops.node(121015, 25.25, 5.15, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.4, 29524053.25041422, 12301688.85433926, 0.02037523, 0.00916667, 0.02346667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 952.83468621, 0.00064582, 1145.33720993, 0.01421259, 114.53372099, 0.03787618, -952.83468621, -0.00064582, -1145.33720993, -0.01421259, -114.53372099, -0.03787618, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 799.3769465, 0.00081826, 960.87618854, 0.01297344, 96.08761885, 0.03120803, -799.3769465, -0.00081826, -960.87618854, -0.01297344, -96.08761885, -0.03120803, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 599.13908894, 0.01291643, 599.13908894, 0.0387493, 419.39736226, -3745.52558755, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 149.78477224, 0.00011872, 449.35431671, 0.00035615, 1497.84772236, 0.00118716, -149.78477224, -0.00011872, -449.35431671, -0.00035615, -1497.84772236, -0.00118716, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 379.21691754, 0.0163652, 379.21691754, 0.0490956, 265.45184228, -2920.062706, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 94.80422939, 7.514e-05, 284.41268816, 0.00022542, 948.04229386, 0.00075139, -94.80422939, -7.514e-05, -284.41268816, -0.00022542, -948.04229386, -0.00075139, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 29.7, 5.15, 0.0)
    ops.node(121016, 29.7, 5.15, 3.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.15, 28709464.04057002, 11962276.68357084, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 282.5141473, 0.000838, 335.22272068, 0.01249017, 33.52227207, 0.03681489, -282.5141473, -0.000838, -335.22272068, -0.01249017, -33.52227207, -0.03681489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 199.16154653, 0.00125021, 236.31905207, 0.01124315, 23.63190521, 0.02813964, -199.16154653, -0.00125021, -236.31905207, -0.01124315, -23.63190521, -0.02813964, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 221.77804122, 0.01675999, 221.77804122, 0.05027996, 155.24462885, -2756.18337118, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 55.4445103, 0.00012051, 166.33353091, 0.00036153, 554.44510304, 0.00120509, -55.4445103, -0.00012051, -166.33353091, -0.00036153, -554.44510304, -0.00120509, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 188.12516683, 0.02500416, 188.12516683, 0.07501249, 131.68761678, -2089.71382494, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 47.03129171, 0.00010222, 141.09387512, 0.00030667, 470.31291707, 0.00102222, -47.03129171, -0.00010222, -141.09387512, -0.00030667, -470.31291707, -0.00102222, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 10.3, 0.0)
    ops.node(121017, 0.0, 10.3, 3.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.075, 30201579.21782729, 12583991.34076137, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 84.92085142, 0.00152149, 100.37459156, 0.0132587, 10.03745916, 0.03782898, -84.92085142, -0.00152149, -100.37459156, -0.0132587, -10.03745916, -0.03782898, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 103.38173304, 0.00127239, 122.19495041, 0.01373753, 12.21949504, 0.04207743, -103.38173304, -0.00127239, -122.19495041, -0.01373753, -12.21949504, -0.04207743, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 119.72026052, 0.03042981, 119.72026052, 0.09128944, 83.80418236, -1480.46714882, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 29.93006513, 0.00012368, 89.79019539, 0.00037103, 299.30065129, 0.00123678, -29.93006513, -0.00012368, -89.79019539, -0.00037103, -299.30065129, -0.00123678, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 128.28957007, 0.02544771, 128.28957007, 0.07634313, 89.80269905, -1659.40153394, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 32.07239252, 0.00013253, 96.21717755, 0.00039759, 320.72392517, 0.00132531, -32.07239252, -0.00013253, -96.21717755, -0.00039759, -320.72392517, -0.00132531, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 4.45, 10.3, 0.0)
    ops.node(121018, 4.45, 10.3, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.175, 30441083.63528915, 12683784.84803715, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 248.85505174, 0.00107212, 296.57531, 0.01313229, 29.657531, 0.03298919, -248.85505174, -0.00107212, -296.57531, -0.01313229, -29.657531, -0.03298919, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 310.83359114, 0.00082496, 370.43880768, 0.0141347, 37.04388077, 0.03922326, -310.83359114, -0.00082496, -370.43880768, -0.0141347, -37.04388077, -0.03922326, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 210.68218798, 0.02144244, 210.68218798, 0.06432732, 147.47753159, -2043.01737812, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 52.670547, 9.254e-05, 158.01164099, 0.00027763, 526.70546995, 0.00092543, -52.670547, -9.254e-05, -158.01164099, -0.00027763, -526.70546995, -0.00092543, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 232.14481718, 0.01649921, 232.14481718, 0.04949764, 162.50137202, -2460.46678575, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 58.03620429, 0.00010197, 174.10861288, 0.00030591, 580.36204294, 0.00101971, -58.03620429, -0.00010197, -174.10861288, -0.00030591, -580.36204294, -0.00101971, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 8.9, 10.3, 0.0)
    ops.node(121019, 8.9, 10.3, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.175, 29481137.17334965, 12283807.15556235, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 248.68978115, 0.00109886, 296.55040759, 0.01286313, 29.65504076, 0.03143745, -248.68978115, -0.00109886, -296.55040759, -0.01286313, -29.65504076, -0.03143745, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 310.9378961, 0.00084169, 370.77824186, 0.01382487, 37.07782419, 0.03729292, -310.9378961, -0.00084169, -370.77824186, -0.01382487, -37.07782419, -0.03729292, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 204.04691156, 0.02197722, 204.04691156, 0.06593166, 142.83283809, -2025.03117832, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 51.01172789, 9.255e-05, 153.03518367, 0.00027764, 510.11727889, 0.00092547, -51.01172789, -9.255e-05, -153.03518367, -0.00027764, -510.11727889, -0.00092547, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 225.09300138, 0.01683377, 225.09300138, 0.0505013, 157.56510097, -2432.28786929, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 56.27325034, 0.00010209, 168.81975103, 0.00030628, 562.73250345, 0.00102093, -56.27325034, -0.00010209, -168.81975103, -0.00030628, -562.73250345, -0.00102093, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 13.35, 10.3, 0.0)
    ops.node(121020, 13.35, 10.3, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.12, 30412020.66071639, 12671675.27529849, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 150.64196713, 0.00125714, 178.87790449, 0.01255964, 17.88779045, 0.03306024, -150.64196713, -0.00125714, -178.87790449, -0.01255964, -17.88779045, -0.03306024, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 189.71988152, 0.00098741, 225.28048121, 0.01328927, 22.52804812, 0.03835331, -189.71988152, -0.00098741, -225.28048121, -0.01328927, -22.52804812, -0.03835331, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 158.17404404, 0.02514285, 158.17404404, 0.07542856, 110.72183083, -1679.36746825, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 39.54351101, 0.00010142, 118.63053303, 0.00030426, 395.4351101, 0.0010142, -39.54351101, -0.00010142, -118.63053303, -0.00030426, -395.4351101, -0.0010142, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 172.10409182, 0.01974822, 172.10409182, 0.05924466, 120.47286427, -1949.44723078, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 43.02602295, 0.00011035, 129.07806886, 0.00033106, 430.26022954, 0.00110352, -43.02602295, -0.00011035, -129.07806886, -0.00033106, -430.26022954, -0.00110352, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 16.35, 10.3, 0.0)
    ops.node(121021, 16.35, 10.3, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.12, 28274496.97854435, 11781040.40772681, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 150.82367094, 0.00129178, 179.00374979, 0.01190138, 17.90037498, 0.02879718, -150.82367094, -0.00129178, -179.00374979, -0.01190138, -17.90037498, -0.02879718, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 189.43984591, 0.00101371, 224.83501804, 0.01256141, 22.4835018, 0.03321822, -189.43984591, -0.00101371, -224.83501804, -0.01256141, -22.4835018, -0.03321822, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 149.89876426, 0.02583556, 149.89876426, 0.07750667, 104.92913498, -1689.83399107, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 37.47469106, 0.00010338, 112.42407319, 0.00031014, 374.74691064, 0.0010338, -37.47469106, -0.00010338, -112.42407319, -0.00031014, -374.74691064, -0.0010338, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 164.01543274, 0.02027417, 164.01543274, 0.06082252, 114.81080292, -1964.48849145, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 41.00385818, 0.00011312, 123.01157455, 0.00033935, 410.03858184, 0.00113116, -41.00385818, -0.00011312, -123.01157455, -0.00033935, -410.03858184, -0.00113116, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 20.8, 10.3, 0.0)
    ops.node(121022, 20.8, 10.3, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.175, 29505554.99546578, 12293981.24811074, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 249.56727273, 0.00108358, 297.59433108, 0.01290658, 29.75943311, 0.03151467, -249.56727273, -0.00108358, -297.59433108, -0.01290658, -29.75943311, -0.03151467, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 310.84812886, 0.00083353, 370.66815677, 0.01388153, 37.06681568, 0.03739225, -310.84812886, -0.00083353, -370.66815677, -0.01388153, -37.06681568, -0.03739225, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 206.16746187, 0.02167155, 206.16746187, 0.06501464, 144.31722331, -2061.70798463, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 51.54186547, 9.343e-05, 154.6255964, 0.0002803, 515.41865467, 0.00093432, -51.54186547, -9.343e-05, -154.6255964, -0.0002803, -515.41865467, -0.00093432, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 228.06100557, 0.01667059, 228.06100557, 0.05001178, 159.6427039, -2489.78897156, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 57.01525139, 0.00010335, 171.04575418, 0.00031006, 570.15251393, 0.00103353, -57.01525139, -0.00010335, -171.04575418, -0.00031006, -570.15251393, -0.00103353, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 25.25, 10.3, 0.0)
    ops.node(121023, 25.25, 10.3, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.175, 28186091.72620538, 11744204.88591891, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 251.84283143, 0.00113237, 300.28257827, 0.01214855, 30.02825783, 0.02884688, -251.84283143, -0.00113237, -300.28257827, -0.01214855, -30.02825783, -0.02884688, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 313.52614198, 0.00086559, 373.83012942, 0.01302318, 37.38301294, 0.03412097, -313.52614198, -0.00086559, -373.83012942, -0.01302318, -37.38301294, -0.03412097, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 196.30325917, 0.02264741, 196.30325917, 0.06794224, 137.41228142, -2021.01526226, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 49.07581479, 9.313e-05, 147.22744437, 0.00027938, 490.75814791, 0.00093126, -49.07581479, -9.313e-05, -147.22744437, -0.00027938, -490.75814791, -0.00093126, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 217.25609275, 0.0173118, 217.25609275, 0.05193539, 152.07926493, -2426.00131315, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 54.31402319, 0.00010307, 162.94206956, 0.0003092, 543.14023188, 0.00103066, -54.31402319, -0.00010307, -162.94206956, -0.0003092, -543.14023188, -0.00103066, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 29.7, 10.3, 0.0)
    ops.node(121024, 29.7, 10.3, 3.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.075, 29334061.25741038, 12222525.52392099, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 86.05829447, 0.00154633, 101.67514045, 0.01243065, 10.16751404, 0.03493791, -86.05829447, -0.00154633, -101.67514045, -0.01243065, -10.16751404, -0.03493791, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 104.77372715, 0.00129578, 123.78682947, 0.01285514, 12.37868295, 0.0388155, -104.77372715, -0.00129578, -123.78682947, -0.01285514, -12.37868295, -0.0388155, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 115.85031086, 0.03092666, 115.85031086, 0.09277998, 81.0952176, -1449.45317613, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 28.96257771, 0.00012322, 86.88773314, 0.00036966, 289.62577715, 0.0012322, -28.96257771, -0.00012322, -86.88773314, -0.00036966, -289.62577715, -0.0012322, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 124.11222539, 0.0259156, 124.11222539, 0.07774679, 86.87855777, -1620.02766175, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 31.02805635, 0.00013201, 93.08416904, 0.00039602, 310.28056348, 0.00132007, -31.02805635, -0.00013201, -93.08416904, -0.00039602, -310.28056348, -0.00132007, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.5)
    ops.node(122001, 0.0, 0.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.075, 28364455.65409087, 11818523.18920453, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 72.69257927, 0.0013272, 86.59855458, 0.01386763, 8.65985546, 0.04052552, -72.69257927, -0.0013272, -86.59855458, -0.01386763, -8.65985546, -0.04052552, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 88.74797756, 0.00111958, 105.72532515, 0.01443775, 10.57253251, 0.04518555, -88.74797756, -0.00111958, -105.72532515, -0.01443775, -10.57253251, -0.04518555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 107.41745695, 0.02654402, 107.41745695, 0.07963205, 75.19221987, -1605.190534, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 26.85436424, 9.816e-05, 80.56309271, 0.00029448, 268.54364238, 0.0009816, -26.85436424, -9.816e-05, -80.56309271, -0.00029448, -268.54364238, -0.0009816, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 116.01568283, 0.02239156, 116.01568283, 0.06717468, 81.21097798, -1846.14516996, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 29.00392071, 0.00010602, 87.01176212, 0.00031805, 290.03920707, 0.00106017, -29.00392071, -0.00010602, -87.01176212, -0.00031805, -290.03920707, -0.00106017, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.45, 0.0, 3.525)
    ops.node(122002, 4.45, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.175, 28502347.76707625, 11875978.23628177, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 155.81644678, 0.00091893, 187.0018977, 0.0123793, 18.70018977, 0.03571213, -155.81644678, -0.00091893, -187.0018977, -0.0123793, -18.70018977, -0.03571213, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 265.70475907, 0.00073148, 318.8835017, 0.01345827, 31.88835017, 0.04337718, -265.70475907, -0.00073148, -318.8835017, -0.01345827, -31.88835017, -0.04337718, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 194.11346197, 0.01837867, 194.11346197, 0.05513602, 135.87942338, -2331.6422296, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 48.52836549, 7.565e-05, 145.58509648, 0.00022696, 485.28365493, 0.00075654, -48.52836549, -7.565e-05, -145.58509648, -0.00022696, -485.28365493, -0.00075654, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 244.29958085, 0.0146296, 244.29958085, 0.04388881, 171.00970659, -3007.61965019, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 61.07489521, 9.521e-05, 183.22468563, 0.00028564, 610.74895212, 0.00095214, -61.07489521, -9.521e-05, -183.22468563, -0.00028564, -610.74895212, -0.00095214, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.9, 0.0, 3.525)
    ops.node(122003, 8.9, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.175, 29711434.97458602, 12379764.57274417, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 156.48111406, 0.00091131, 187.62160397, 0.01269298, 18.7621604, 0.03773578, -156.48111406, -0.00091131, -187.62160397, -0.01269298, -18.7621604, -0.03773578, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 266.12888165, 0.00072578, 319.08980161, 0.01380939, 31.90898016, 0.04592093, -266.12888165, -0.00072578, -319.08980161, -0.01380939, -31.90898016, -0.04592093, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 201.65590246, 0.01822612, 201.65590246, 0.05467837, 141.15913172, -2351.68925731, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 50.41397561, 7.54e-05, 151.24192684, 0.00022619, 504.13975615, 0.00075396, -50.41397561, -7.54e-05, -151.24192684, -0.00022619, -504.13975615, -0.00075396, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 253.4316174, 0.01451564, 253.4316174, 0.04354693, 177.40213218, -3040.16373311, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 63.35790435, 9.475e-05, 190.07371305, 0.00028426, 633.57904351, 0.00094754, -63.35790435, -9.475e-05, -190.07371305, -0.00028426, -633.57904351, -0.00094754, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 20.8, 0.0, 3.525)
    ops.node(122006, 20.8, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.175, 28835944.71810736, 12014976.96587807, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 156.57160986, 0.00091812, 187.87320655, 0.01273357, 18.78732065, 0.03655695, -156.57160986, -0.00091812, -187.87320655, -0.01273357, -18.78732065, -0.03655695, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 267.12547915, 0.00073151, 320.52886447, 0.01385262, 32.05288645, 0.04440055, -267.12547915, -0.00073151, -320.52886447, -0.01385262, -32.05288645, -0.04440055, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 197.6167885, 0.01836248, 197.6167885, 0.05508745, 138.33175195, -2373.57822975, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 49.40419712, 7.613e-05, 148.21259137, 0.00022839, 494.04197124, 0.00076129, -49.40419712, -7.613e-05, -148.21259137, -0.00022839, -494.04197124, -0.00076129, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 248.85414992, 0.01463022, 248.85414992, 0.04389067, 174.19790495, -3075.73863702, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 62.21353748, 9.587e-05, 186.64061244, 0.0002876, 622.13537481, 0.00095867, -62.21353748, -9.587e-05, -186.64061244, -0.0002876, -622.13537481, -0.00095867, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 25.25, 0.0, 3.525)
    ops.node(122007, 25.25, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.175, 28414397.05274494, 11839332.10531039, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 156.96251445, 0.00091927, 188.38471959, 0.01238146, 18.83847196, 0.03558254, -156.96251445, -0.00091927, -188.38471959, -0.01238146, -18.83847196, -0.03558254, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 268.56440938, 0.00073372, 322.3281121, 0.01346254, 32.23281121, 0.04321251, -268.56440938, -0.00073372, -322.3281121, -0.01346254, -32.23281121, -0.04321251, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 195.39583312, 0.01838531, 195.39583312, 0.05515594, 136.77708319, -2376.50211734, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 48.84895828, 7.639e-05, 146.54687484, 0.00022917, 488.48958281, 0.0007639, -48.84895828, -7.639e-05, -146.54687484, -0.00022917, -488.48958281, -0.0007639, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 246.24983526, 0.0146744, 246.24983526, 0.04402319, 172.37488468, -3080.49384645, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 61.56245882, 9.627e-05, 184.68737645, 0.00028881, 615.62458816, 0.00096271, -61.56245882, -9.627e-05, -184.68737645, -0.00028881, -615.62458816, -0.00096271, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 29.7, 0.0, 3.5)
    ops.node(122008, 29.7, 0.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.075, 28819413.93867648, 12008089.1411152, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 72.82084795, 0.00132168, 86.76437467, 0.01384305, 8.67643747, 0.04159424, -72.82084795, -0.00132168, -86.76437467, -0.01384305, -8.67643747, -0.04159424, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 88.8970841, 0.00111508, 105.91884233, 0.01441301, 10.59188423, 0.04642184, -88.8970841, -0.00111508, -105.91884233, -0.01441301, -10.59188423, -0.04642184, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 107.83847929, 0.02643365, 107.83847929, 0.07930095, 75.4869355, -1585.8927058, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 26.95961982, 9.699e-05, 80.87885947, 0.00029097, 269.59619822, 0.00096989, -26.95961982, -9.699e-05, -80.87885947, -0.00029097, -269.59619822, -0.00096989, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 116.29356107, 0.02230161, 116.29356107, 0.06690484, 81.40549275, -1821.31938007, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 29.07339027, 0.00010459, 87.22017081, 0.00031378, 290.73390269, 0.00104594, -29.07339027, -0.00010459, -87.22017081, -0.00031378, -290.73390269, -0.00104594, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 5.15, 3.5)
    ops.node(122009, 0.0, 5.15, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.15, 29154531.46772906, 12147721.44488711, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 235.84639323, 0.00073785, 281.92784665, 0.01335558, 28.19278467, 0.04479681, -235.84639323, -0.00073785, -281.92784665, -0.01335558, -28.19278467, -0.04479681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 132.27776608, 0.00104579, 158.12319722, 0.01186679, 15.81231972, 0.03370659, -132.27776608, -0.00104579, -158.12319722, -0.01186679, -15.81231972, -0.03370659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 230.96891176, 0.01475699, 230.96891176, 0.04427096, 161.67823823, -2957.30639157, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 57.74222794, 0.00010267, 173.22668382, 0.00030802, 577.4222794, 0.00102672, -57.74222794, -0.00010267, -173.22668382, -0.00030802, -577.4222794, -0.00102672, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 175.14053342, 0.02091579, 175.14053342, 0.06274736, 122.59837339, -2121.66502314, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 43.78513336, 7.785e-05, 131.35540007, 0.00023356, 437.85133355, 0.00077855, -43.78513336, -7.785e-05, -131.35540007, -0.00023356, -437.85133355, -0.00077855, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 4.45, 5.15, 3.525)
    ops.node(122010, 4.45, 5.15, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.4, 29422481.4410108, 12259367.26708784, 0.02037523, 0.00916667, 0.02346667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 781.07911121, 0.00059366, 942.24283455, 0.01405234, 94.22428345, 0.04015153, -781.07911121, -0.00059366, -942.24283455, -0.01405234, -94.22428345, -0.04015153, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 391.85605285, 0.00070955, 472.70955358, 0.01276789, 47.27095536, 0.03287929, -391.85605285, -0.00070955, -472.70955358, -0.01276789, -47.27095536, -0.03287929, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 655.4162443, 0.0118731, 655.4162443, 0.0356193, 458.79137101, -4141.59172748, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 163.85406107, 0.00010826, 491.56218322, 0.00032478, 1638.54061074, 0.00108262, -163.85406107, -0.00010826, -491.56218322, -0.00032478, -1638.54061074, -0.00108262, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 409.63515268, 0.01419091, 409.63515268, 0.04257272, 286.74460688, -3056.44923862, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 102.40878817, 6.766e-05, 307.22636451, 0.00020299, 1024.08788171, 0.00067663, -102.40878817, -6.766e-05, -307.22636451, -0.00020299, -1024.08788171, -0.00067663, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.9, 5.15, 3.525)
    ops.node(122011, 8.9, 5.15, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.4, 28763916.87455272, 11984965.36439697, 0.02037523, 0.00916667, 0.02346667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 788.07997995, 0.00060292, 951.60866678, 0.01378092, 95.16086668, 0.03923563, -788.07997995, -0.00060292, -951.60866678, -0.01378092, -95.16086668, -0.03923563, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 394.64830382, 0.00072439, 476.53887397, 0.01253125, 47.6538874, 0.03214604, -394.64830382, -0.00072439, -476.53887397, -0.01253125, -47.6538874, -0.03214604, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 639.25794647, 0.0120584, 639.25794647, 0.03617519, 447.48056253, -4116.32806264, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 159.81448662, 0.00010801, 479.44345985, 0.00032403, 1598.14486618, 0.0010801, -159.81448662, -0.00010801, -479.44345985, -0.00032403, -1598.14486618, -0.0010801, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 399.53621654, 0.01448788, 399.53621654, 0.04346364, 279.67535158, -3042.87916242, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 99.88405414, 6.751e-05, 299.65216241, 0.00020252, 998.84054136, 0.00067506, -99.88405414, -6.751e-05, -299.65216241, -0.00020252, -998.84054136, -0.00067506, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 13.35, 5.15, 3.525)
    ops.node(122012, 13.35, 5.15, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.28, 29813771.69456388, 12422404.87273495, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 514.18214519, 0.00062552, 618.77839057, 0.01454325, 61.87783906, 0.04350722, -514.18214519, -0.00062552, -618.77839057, -0.01454325, -61.87783906, -0.04350722, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 245.50099697, 0.00082913, 295.44143688, 0.01291329, 29.54414369, 0.03363027, -245.50099697, -0.00082913, -295.44143688, -0.01291329, -29.54414369, -0.03363027, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 451.68637396, 0.01251047, 451.68637396, 0.03753142, 316.18046177, -3610.05932491, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 112.92159349, 0.00010519, 338.76478047, 0.00031556, 1129.21593489, 0.00105186, -112.92159349, -0.00010519, -338.76478047, -0.00031556, -1129.21593489, -0.00105186, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 269.09723356, 0.01658252, 269.09723356, 0.04974756, 188.36806349, -2492.47558504, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 67.27430839, 6.267e-05, 201.82292517, 0.000188, 672.74308391, 0.00062666, -67.27430839, -6.267e-05, -201.82292517, -0.000188, -672.74308391, -0.00062666, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 16.35, 5.15, 3.525)
    ops.node(122013, 16.35, 5.15, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.28, 29456380.08809245, 12273491.70337186, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 513.27838331, 0.00062345, 618.01900658, 0.01440835, 61.80190066, 0.04295045, -513.27838331, -0.00062345, -618.01900658, -0.01440835, -61.80190066, -0.04295045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 244.84568573, 0.00082379, 294.80939073, 0.01279263, 29.48093907, 0.03320786, -244.84568573, -0.00082379, -294.80939073, -0.01279263, -29.48093907, -0.03320786, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 445.02532865, 0.01246901, 445.02532865, 0.03740702, 311.51773005, -3568.15168152, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 111.25633216, 0.00010489, 333.76899649, 0.00031468, 1112.56332162, 0.00104892, -111.25633216, -0.00010489, -333.76899649, -0.00031468, -1112.56332162, -0.00104892, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 265.12886599, 0.01647581, 265.12886599, 0.04942742, 185.59020619, -2472.55925989, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 66.2822165, 6.249e-05, 198.84664949, 0.00018747, 662.82216497, 0.00062491, -66.2822165, -6.249e-05, -198.84664949, -0.00018747, -662.82216497, -0.00062491, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 20.8, 5.15, 3.525)
    ops.node(122014, 20.8, 5.15, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.4, 29505534.20344594, 12293972.58476914, 0.02037523, 0.00916667, 0.02346667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 795.69655826, 0.00060172, 959.74722007, 0.01367099, 95.97472201, 0.03984816, -795.69655826, -0.00060172, -959.74722007, -0.01367099, -95.97472201, -0.03984816, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 398.19287914, 0.00072093, 480.28925705, 0.01243038, 48.02892571, 0.03260187, -398.19287914, -0.00072093, -480.28925705, -0.01243038, -48.02892571, -0.03260187, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 655.75179226, 0.01203435, 655.75179226, 0.03610304, 459.02625458, -4097.49544043, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 163.93794807, 0.00010801, 491.8138442, 0.00032404, 1639.37948065, 0.00108012, -163.93794807, -0.00010801, -491.8138442, -0.00032404, -1639.37948065, -0.00108012, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 409.84487016, 0.0144186, 409.84487016, 0.0432558, 286.89140911, -3032.75604887, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 102.46121754, 6.751e-05, 307.38365262, 0.00020252, 1024.61217541, 0.00067508, -102.46121754, -6.751e-05, -307.38365262, -0.00020252, -1024.61217541, -0.00067508, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 25.25, 5.15, 3.525)
    ops.node(122015, 25.25, 5.15, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.4, 29240689.8067724, 12183620.75282183, 0.02037523, 0.00916667, 0.02346667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 788.91834525, 0.00060491, 951.97068782, 0.01423251, 95.19706878, 0.04015848, -788.91834525, -0.00060491, -951.97068782, -0.01423251, -95.19706878, -0.04015848, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 395.91967636, 0.00072902, 477.74770214, 0.0129387, 47.77477021, 0.03291663, -395.91967636, -0.00072902, -477.74770214, -0.0129387, -47.77477021, -0.03291663, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 653.25946208, 0.01209812, 653.25946208, 0.03629435, 457.28162345, -4198.97750749, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 163.31486552, 0.00010858, 489.94459656, 0.00032573, 1633.14865519, 0.00108576, -163.31486552, -0.00010858, -489.94459656, -0.00032573, -1633.14865519, -0.00108576, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 408.2871638, 0.01458037, 408.2871638, 0.04374112, 285.80101466, -3087.23160414, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 102.07179095, 6.786e-05, 306.21537285, 0.00020358, 1020.71790949, 0.0006786, -102.07179095, -6.786e-05, -306.21537285, -0.00020358, -1020.71790949, -0.0006786, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 29.7, 5.15, 3.5)
    ops.node(122016, 29.7, 5.15, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.15, 30227655.90669308, 12594856.62778878, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 235.23797171, 0.00073442, 280.98895757, 0.01384636, 28.09889576, 0.04755335, -235.23797171, -0.00073442, -280.98895757, -0.01384636, -28.09889576, -0.04755335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 132.0296328, 0.00104572, 157.70782506, 0.01229056, 15.77078251, 0.0357042, -132.0296328, -0.00104572, -157.70782506, -0.01229056, -15.77078251, -0.0357042, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 240.90276134, 0.01468831, 240.90276134, 0.04406493, 168.63193293, -3059.6623361, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 60.22569033, 0.00010329, 180.677071, 0.00030986, 602.25690334, 0.00103286, -60.22569033, -0.00010329, -180.677071, -0.00030986, -602.25690334, -0.00103286, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 182.63665695, 0.02091432, 182.63665695, 0.06274297, 127.84565987, -2173.55409393, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 45.65916424, 7.83e-05, 136.97749272, 0.00023491, 456.59164238, 0.00078305, -45.65916424, -7.83e-05, -136.97749272, -0.00023491, -456.59164238, -0.00078305, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 10.3, 3.5)
    ops.node(122017, 0.0, 10.3, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.075, 29673107.50280973, 12363794.79283739, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 73.18643497, 0.00126811, 87.19337072, 0.01415941, 8.71933707, 0.04387565, -73.18643497, -0.00126811, -87.19337072, -0.01415941, -8.71933707, -0.04387565, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 89.26463612, 0.00107631, 106.34873132, 0.01476712, 10.63487313, 0.04904248, -89.26463612, -0.00107631, -106.34873132, -0.01476712, -10.63487313, -0.04904248, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 110.18677073, 0.02536218, 110.18677073, 0.07608653, 77.13073951, -1591.1913577, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 27.54669268, 9.625e-05, 82.64007805, 0.00028875, 275.46692682, 0.0009625, -27.54669268, -9.625e-05, -82.64007805, -0.00028875, -275.46692682, -0.0009625, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 118.68124227, 0.02152617, 118.68124227, 0.06457851, 83.07686959, -1828.13407091, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 29.67031057, 0.00010367, 89.0109317, 0.00031101, 296.70310566, 0.0010367, -29.67031057, -0.00010367, -89.0109317, -0.00031101, -296.70310566, -0.0010367, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 4.45, 10.3, 3.525)
    ops.node(122018, 4.45, 10.3, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.175, 28635075.94096793, 11931281.64206997, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 158.97260354, 0.00095467, 190.77695149, 0.01290915, 19.07769515, 0.03386544, -158.97260354, -0.00095467, -190.77695149, -0.01290915, -19.07769515, -0.03386544, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 248.67356754, 0.00075196, 298.42365335, 0.01394506, 29.84236534, 0.04042265, -248.67356754, -0.00075196, -298.42365335, -0.01394506, -29.84236534, -0.04042265, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 184.57872238, 0.0190935, 184.57872238, 0.0572805, 129.20510566, -2079.58080253, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 46.14468059, 7.16e-05, 138.43404178, 0.00021481, 461.44680594, 0.00071605, -46.14468059, -7.16e-05, -138.43404178, -0.00021481, -461.44680594, -0.00071605, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 230.49969224, 0.0150391, 230.49969224, 0.04511731, 161.34978457, -2601.66713287, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 57.62492306, 8.942e-05, 172.87476918, 0.00026826, 576.24923061, 0.00089419, -57.62492306, -8.942e-05, -172.87476918, -0.00026826, -576.24923061, -0.00089419, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 8.9, 10.3, 3.525)
    ops.node(122019, 8.9, 10.3, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.175, 29963530.92484351, 12484804.55201813, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 159.49557067, 0.00092925, 191.18052602, 0.01350614, 19.1180526, 0.03610689, -159.49557067, -0.00092925, -191.18052602, -0.01350614, -19.1180526, -0.03610689, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 249.26110605, 0.00073606, 298.778638, 0.01461607, 29.8778638, 0.04317138, -249.26110605, -0.00073606, -298.778638, -0.01461607, -29.8778638, -0.04317138, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 194.3107019, 0.01858494, 194.3107019, 0.05575482, 136.01749133, -2134.61531957, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 48.57767548, 7.204e-05, 145.73302643, 0.00021611, 485.77675476, 0.00072038, -48.57767548, -7.204e-05, -145.73302643, -0.00021611, -485.77675476, -0.00072038, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 242.59201109, 0.01472124, 242.59201109, 0.04416371, 169.81440776, -2689.76401379, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 60.64800277, 8.994e-05, 181.94400832, 0.00026981, 606.48002772, 0.00089938, -60.64800277, -8.994e-05, -181.94400832, -0.00026981, -606.48002772, -0.00089938, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 13.35, 10.3, 3.525)
    ops.node(122020, 13.35, 10.3, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.12, 31136101.84242232, 12973375.76767597, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 118.78335165, 0.00106761, 141.77703896, 0.01352934, 14.1777039, 0.03910588, -118.78335165, -0.00106761, -141.77703896, -0.01352934, -14.1777039, -0.03910588, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 154.87576826, 0.0008556, 184.85610589, 0.01441919, 18.48561059, 0.04568906, -154.87576826, -0.0008556, -184.85610589, -0.01441919, -18.48561059, -0.04568906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 150.11429456, 0.02135214, 150.11429456, 0.06405643, 105.08000619, -1748.46378553, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 37.52857364, 7.81e-05, 112.58572092, 0.00023431, 375.2857364, 0.00078104, -37.52857364, -7.81e-05, -112.58572092, -0.00023431, -375.2857364, -0.00078104, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 164.0048942, 0.0171119, 164.0048942, 0.0513357, 114.80342594, -2101.81457708, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 41.00122355, 8.533e-05, 123.00367065, 0.00025599, 410.01223549, 0.00085331, -41.00122355, -8.533e-05, -123.00367065, -0.00025599, -410.01223549, -0.00085331, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 16.35, 10.3, 3.525)
    ops.node(122021, 16.35, 10.3, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.12, 29493935.56057769, 12289139.81690737, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 119.20139557, 0.00107538, 142.52645008, 0.01346898, 14.25264501, 0.03671765, -119.20139557, -0.00107538, -142.52645008, -0.01346898, -14.25264501, -0.03671765, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 155.00492209, 0.00086373, 185.3359282, 0.01435316, 18.53359282, 0.04277699, -155.00492209, -0.00086373, -185.3359282, -0.01435316, -18.53359282, -0.04277699, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 144.15042995, 0.0215076, 144.15042995, 0.06452279, 100.90530097, -1762.63545844, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 36.03760749, 7.918e-05, 108.11282246, 0.00023753, 360.37607488, 0.00079177, -36.03760749, -7.918e-05, -108.11282246, -0.00023753, -360.37607488, -0.00079177, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 158.23528875, 0.01727454, 158.23528875, 0.05182362, 110.76470213, -2122.54070145, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 39.55882219, 8.691e-05, 118.67646656, 0.00026074, 395.58822188, 0.00086913, -39.55882219, -8.691e-05, -118.67646656, -0.00026074, -395.58822188, -0.00086913, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 20.8, 10.3, 3.525)
    ops.node(122022, 20.8, 10.3, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.175, 30597044.86677891, 12748768.69449121, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 159.08561424, 0.00090448, 190.52490915, 0.01337033, 19.05249091, 0.03668699, -159.08561424, -0.00090448, -190.52490915, -0.01337033, -19.05249091, -0.03668699, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 248.46626484, 0.00072059, 297.56941105, 0.01447804, 29.7569411, 0.04393789, -248.46626484, -0.00072059, -297.56941105, -0.01447804, -29.7569411, -0.04393789, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 197.35968066, 0.01808956, 197.35968066, 0.05426869, 138.15177646, -2121.27943194, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 49.33992016, 7.165e-05, 148.01976049, 0.00021496, 493.39920165, 0.00071653, -49.33992016, -7.165e-05, -148.01976049, -0.00021496, -493.39920165, -0.00071653, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 246.07103934, 0.01441172, 246.07103934, 0.04323517, 172.24972754, -2668.38756227, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 61.51775984, 8.934e-05, 184.55327951, 0.00026802, 615.17759836, 0.00089339, -61.51775984, -8.934e-05, -184.55327951, -0.00026802, -615.17759836, -0.00089339, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 25.25, 10.3, 3.525)
    ops.node(122023, 25.25, 10.3, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.175, 29135056.63365114, 12139606.93068798, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 161.3602988, 0.00094037, 193.57730367, 0.01294479, 19.35773037, 0.03454341, -161.3602988, -0.00094037, -193.57730367, -0.01294479, -19.35773037, -0.03454341, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 252.65354586, 0.00074634, 303.09805159, 0.01399455, 30.30980516, 0.04128371, -252.65354586, -0.00074634, -303.09805159, -0.01399455, -30.30980516, -0.04128371, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 187.57228907, 0.01880738, 187.57228907, 0.05642213, 131.30060235, -2084.63773967, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 46.89307227, 7.152e-05, 140.67921681, 0.00021455, 468.93072269, 0.00071517, -46.89307227, -7.152e-05, -140.67921681, -0.00021455, -468.93072269, -0.00071517, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 234.09921274, 0.01492671, 234.09921274, 0.04478014, 163.86944892, -2609.74879287, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 58.52480318, 8.926e-05, 175.57440955, 0.00026777, 585.24803184, 0.00089257, -58.52480318, -8.926e-05, -175.57440955, -0.00026777, -585.24803184, -0.00089257, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 29.7, 10.3, 3.5)
    ops.node(122024, 29.7, 10.3, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.075, 29643926.87312956, 12351636.19713732, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 71.89960691, 0.00127544, 85.66111216, 0.01414967, 8.56611122, 0.04380063, -71.89960691, -0.00127544, -85.66111216, -0.01414967, -8.56611122, -0.04380063, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 87.73475977, 0.00107804, 104.52709576, 0.01475071, 10.45270958, 0.04895078, -87.73475977, -0.00107804, -104.52709576, -0.01475071, -10.45270958, -0.04895078, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 109.71517361, 0.0255088, 109.71517361, 0.0765264, 76.80062153, -1580.50182592, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 27.4287934, 9.593e-05, 82.28638021, 0.0002878, 274.28793404, 0.00095933, -27.4287934, -9.593e-05, -82.28638021, -0.0002878, -274.28793404, -0.00095933, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 118.13011244, 0.02156073, 118.13011244, 0.0646822, 82.69107871, -1814.38747228, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 29.53252811, 0.00010329, 88.59758433, 0.00030987, 295.3252811, 0.0010329, -29.53252811, -0.00010329, -88.59758433, -0.00030987, -295.3252811, -0.0010329, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.2)
    ops.node(123001, 0.0, 0.0, 8.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 29332768.68434987, 12221986.95181245, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 44.69748008, 0.00122753, 53.54132038, 0.01557146, 5.35413204, 0.05471331, -44.69748008, -0.00122753, -53.54132038, -0.01557146, -5.35413204, -0.05471331, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 44.69748008, 0.00122753, 53.54132038, 0.01557146, 5.35413204, 0.05471331, -44.69748008, -0.00122753, -53.54132038, -0.01557146, -5.35413204, -0.05471331, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 94.29507387, 0.02455065, 94.29507387, 0.07365195, 66.00655171, -1490.44540564, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 23.57376847, 9.999e-05, 70.7213054, 0.00029997, 235.73768468, 0.00099989, -23.57376847, -9.999e-05, -70.7213054, -0.00029997, -235.73768468, -0.00099989, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 94.29507387, 0.02455065, 94.29507387, 0.07365195, 66.00655171, -1490.44540564, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 23.57376847, 9.999e-05, 70.7213054, 0.00029997, 235.73768468, 0.00099989, -23.57376847, -9.999e-05, -70.7213054, -0.00029997, -235.73768468, -0.00099989, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.45, 0.0, 6.225)
    ops.node(123002, 4.45, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1, 29353371.1610828, 12230571.31711783, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 72.12029528, 0.00120734, 86.28749611, 0.01337157, 8.62874961, 0.03991228, -72.12029528, -0.00120734, -86.28749611, -0.01337157, -8.62874961, -0.03991228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 112.06383817, 0.00082823, 134.07748767, 0.01495523, 13.40774877, 0.05280089, -112.06383817, -0.00082823, -134.07748767, -0.01495523, -13.40774877, -0.05280089, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 127.35763938, 0.02414676, 127.35763938, 0.07244027, 89.15034756, -1666.7949052, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 31.83940984, 8.435e-05, 95.51822953, 0.00025304, 318.39409844, 0.00084346, -31.83940984, -8.435e-05, -95.51822953, -0.00025304, -318.39409844, -0.00084346, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 153.55226623, 0.01656463, 153.55226623, 0.04969388, 107.48658636, -2427.77256858, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 38.38806656, 0.00010169, 115.16419967, 0.00030508, 383.88066558, 0.00101694, -38.38806656, -0.00010169, -115.16419967, -0.00030508, -383.88066558, -0.00101694, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.9, 0.0, 6.225)
    ops.node(123003, 8.9, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.1, 30174667.91990622, 12572778.29996092, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 73.04307954, 0.00117608, 87.33087007, 0.01307915, 8.73308701, 0.04098405, -73.04307954, -0.00117608, -87.33087007, -0.01307915, -8.73308701, -0.04098405, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 113.03461638, 0.00081592, 135.14506041, 0.01463962, 13.51450604, 0.05443054, -113.03461638, -0.00081592, -135.14506041, -0.01463962, -13.51450604, -0.05443054, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 127.84321722, 0.02352166, 127.84321722, 0.07056499, 89.49025206, -1609.10499393, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 31.96080431, 8.236e-05, 95.88241292, 0.00024709, 319.60804306, 0.00082363, -31.96080431, -8.236e-05, -95.88241292, -0.00024709, -319.60804306, -0.00082363, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 152.71152775, 0.01631845, 152.71152775, 0.04895535, 106.89806943, -2316.69272643, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 38.17788194, 9.838e-05, 114.53364581, 0.00029515, 381.77881938, 0.00098384, -38.17788194, -9.838e-05, -114.53364581, -0.00029515, -381.77881938, -0.00098384, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 20.8, 0.0, 6.225)
    ops.node(123006, 20.8, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1, 29573095.02816795, 12322122.92840331, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 73.48933702, 0.00121866, 87.91219813, 0.01308356, 8.79121981, 0.03999855, -73.48933702, -0.00121866, -87.91219813, -0.01308356, -8.79121981, -0.03999855, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 113.90259559, 0.00083894, 136.25687694, 0.0146183, 13.62568769, 0.05299766, -113.90259559, -0.00083894, -136.25687694, -0.0146183, -13.62568769, -0.05299766, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 126.38848321, 0.02437327, 126.38848321, 0.0731198, 88.47193825, -1622.66839491, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 31.5971208, 8.308e-05, 94.79136241, 0.00024925, 315.97120802, 0.00083082, -31.5971208, -8.308e-05, -94.79136241, -0.00024925, -315.97120802, -0.00083082, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 151.57073242, 0.01677872, 151.57073242, 0.05033617, 106.09951269, -2342.75032539, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 37.8926831, 9.964e-05, 113.67804931, 0.00029891, 378.92683104, 0.00099636, -37.8926831, -9.964e-05, -113.67804931, -0.00029891, -378.92683104, -0.00099636, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 25.25, 0.0, 6.225)
    ops.node(123007, 25.25, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1, 31020624.39152125, 12925260.16313385, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 71.94798454, 0.00123231, 85.92924851, 0.01311664, 8.59292485, 0.0423294, -71.94798454, -0.00123231, -85.92924851, -0.01311664, -8.59292485, -0.0423294, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 112.43241077, 0.00083432, 134.28079505, 0.01463625, 13.4280795, 0.05629211, -112.43241077, -0.00083432, -134.28079505, -0.01463625, -13.4280795, -0.05629211, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 131.08839424, 0.02464623, 131.08839424, 0.07393868, 91.76187597, -1620.35896815, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 32.77209856, 8.215e-05, 98.31629568, 0.00024645, 327.7209856, 0.0008215, -32.77209856, -8.215e-05, -98.31629568, -0.00024645, -327.7209856, -0.0008215, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 156.21728236, 0.01668636, 156.21728236, 0.05005908, 109.35209765, -2338.31095879, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 39.05432059, 9.79e-05, 117.16296177, 0.00029369, 390.5432059, 0.00097898, -39.05432059, -9.79e-05, -117.16296177, -0.00029369, -390.5432059, -0.00097898, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 29.7, 0.0, 6.2)
    ops.node(123008, 29.7, 0.0, 8.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 29592332.04092986, 12330138.35038744, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 44.74958588, 0.00124622, 53.5923614, 0.01529304, 5.35923614, 0.05504755, -44.74958588, -0.00124622, -53.5923614, -0.01529304, -5.35923614, -0.05504755, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 44.74958588, 0.00124622, 53.5923614, 0.01529304, 5.35923614, 0.05504755, -44.74958588, -0.00124622, -53.5923614, -0.01529304, -5.35923614, -0.05504755, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 93.60186581, 0.02492445, 93.60186581, 0.07477334, 65.52130607, -1451.09454565, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 23.40046645, 9.838e-05, 70.20139936, 0.00029515, 234.00466453, 0.00098383, -23.40046645, -9.838e-05, -70.20139936, -0.00029515, -234.00466453, -0.00098383, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 93.60186581, 0.02492445, 93.60186581, 0.07477334, 65.52130607, -1451.09454565, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 23.40046645, 9.838e-05, 70.20139936, 0.00029515, 234.00466453, 0.00098383, -23.40046645, -9.838e-05, -70.20139936, -0.00029515, -234.00466453, -0.00098383, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 5.15, 6.2)
    ops.node(123009, 0.0, 5.15, 8.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1, 28288363.00231304, 11786817.91763043, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 121.61163532, 0.00084075, 145.44257996, 0.01449151, 14.544258, 0.0488337, -121.61163532, -0.00084075, -145.44257996, -0.01449151, -14.544258, -0.0488337, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 69.59431511, 0.00122815, 83.23197622, 0.01298232, 8.32319762, 0.03706608, -69.59431511, -0.00122815, -83.23197622, -0.01298232, -8.32319762, -0.03706608, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 149.44621956, 0.01681504, 149.44621956, 0.05044513, 104.61235369, -2387.49309512, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 37.36155489, 0.0001027, 112.08466467, 0.0003081, 373.61554889, 0.00102701, -37.36155489, -0.0001027, -112.08466467, -0.0003081, -373.61554889, -0.00102701, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 123.83086904, 0.02456306, 123.83086904, 0.07368919, 86.68160833, -1659.93553006, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 30.95771726, 8.51e-05, 92.87315178, 0.00025529, 309.57717259, 0.00085098, -30.95771726, -8.51e-05, -92.87315178, -0.00025529, -309.57717259, -0.00085098, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 4.45, 5.15, 6.225)
    ops.node(123010, 4.45, 5.15, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.3, 29193245.06808516, 12163852.11170215, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 518.36730398, 0.00060138, 626.14558474, 0.01526061, 62.61455847, 0.04597687, -518.36730398, -0.00060138, -626.14558474, -0.01526061, -62.61455847, -0.04597687, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 227.8481034, 0.00080456, 275.22199575, 0.01334143, 27.52219957, 0.03453731, -227.8481034, -0.00080456, -275.22199575, -0.01334143, -27.52219957, -0.03453731, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 476.32935081, 0.01202765, 476.32935081, 0.03608294, 333.43054557, -3707.32236131, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 119.0823377, 0.00010573, 357.24701311, 0.00031719, 1190.82337703, 0.0010573, -119.0823377, -0.00010573, -357.24701311, -0.00031719, -1190.82337703, -0.0010573, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 264.82748557, 0.01609111, 264.82748557, 0.04827334, 185.3792399, -2302.5998016, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 66.20687139, 5.878e-05, 198.62061417, 0.00017635, 662.06871391, 0.00058784, -66.20687139, -5.878e-05, -198.62061417, -0.00017635, -662.06871391, -0.00058784, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.9, 5.15, 6.225)
    ops.node(123011, 8.9, 5.15, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.3, 30428713.35648407, 12678630.5652017, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 523.81543469, 0.0006046, 631.27689141, 0.01500639, 63.12768914, 0.04693083, -523.81543469, -0.0006046, -631.27689141, -0.01500639, -63.12768914, -0.04693083, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 230.55840866, 0.00081226, 277.85778323, 0.01312897, 27.78577832, 0.03515856, -230.55840866, -0.00081226, -277.85778323, -0.01312897, -27.78577832, -0.03515856, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 496.70854538, 0.01209193, 496.70854538, 0.03627579, 347.69598177, -3711.76097601, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 124.17713635, 0.00010578, 372.53140904, 0.00031733, 1241.77136346, 0.00105777, -124.17713635, -0.00010578, -372.53140904, -0.00031733, -1241.77136346, -0.00105777, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 276.28668666, 0.01624515, 276.28668666, 0.04873545, 193.40068066, -2304.46524997, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 69.07167167, 5.884e-05, 207.215015, 0.00017651, 690.71671666, 0.00058837, -69.07167167, -5.884e-05, -207.215015, -0.00017651, -690.71671666, -0.00058837, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 13.35, 5.15, 6.225)
    ops.node(123012, 13.35, 5.15, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.21, 29284838.15243782, 12202015.89684909, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 330.29340911, 0.00066791, 398.28263125, 0.01514522, 39.82826313, 0.04735172, -330.29340911, -0.00066791, -398.28263125, -0.01514522, -39.82826313, -0.04735172, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 163.33141328, 0.00091948, 196.95235585, 0.01345527, 19.69523558, 0.036343, -163.33141328, -0.00091948, -196.95235585, -0.01345527, -19.69523558, -0.036343, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 298.45478808, 0.01335816, 298.45478808, 0.04007447, 208.91835166, -2901.20122878, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 74.61369702, 9.434e-05, 223.84109106, 0.00028303, 746.1369702, 0.00094344, -74.61369702, -9.434e-05, -223.84109106, -0.00028303, -746.1369702, -0.00094344, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 199.90205457, 0.01838956, 199.90205457, 0.05516868, 139.9314382, -1926.29852387, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 49.97551364, 6.319e-05, 149.92654093, 0.00018957, 499.75513642, 0.0006319, -49.97551364, -6.319e-05, -149.92654093, -0.00018957, -499.75513642, -0.0006319, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 16.35, 5.15, 6.225)
    ops.node(123013, 16.35, 5.15, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.21, 27840061.29149565, 11600025.53812319, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 328.15354546, 0.00066301, 396.3700654, 0.01532653, 39.63700654, 0.04556851, -328.15354546, -0.00066301, -396.3700654, -0.01532653, -39.63700654, -0.04556851, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 161.92158466, 0.00090541, 195.58182439, 0.01360244, 19.55818244, 0.03509407, -161.92158466, -0.00090541, -195.58182439, -0.01360244, -19.55818244, -0.03509407, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 286.90021402, 0.01326029, 286.90021402, 0.03978088, 200.83014981, -2949.40413796, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 71.7250535, 9.54e-05, 215.17516051, 0.00028619, 717.25053504, 0.00095398, -71.7250535, -9.54e-05, -215.17516051, -0.00028619, -717.25053504, -0.00095398, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 191.59252182, 0.01810824, 191.59252182, 0.05432472, 134.11476528, -1949.18370258, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 47.89813046, 6.371e-05, 143.69439137, 0.00019112, 478.98130456, 0.00063707, -47.89813046, -6.371e-05, -143.69439137, -0.00019112, -478.98130456, -0.00063707, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 20.8, 5.15, 6.225)
    ops.node(123014, 20.8, 5.15, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.3, 28895389.69429726, 12039745.70595719, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 523.45529191, 0.00061479, 632.5855644, 0.01486686, 63.25855644, 0.04526544, -523.45529191, -0.00061479, -632.5855644, -0.01486686, -63.25855644, -0.04526544, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 229.96718733, 0.00083389, 277.91088415, 0.01302256, 27.79108842, 0.03399922, -229.96718733, -0.00083389, -277.91088415, -0.01302256, -27.79108842, -0.03399922, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 470.08990231, 0.01229578, 470.08990231, 0.03688735, 329.06293162, -3662.28599426, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 117.52247558, 0.00010542, 352.56742673, 0.00031626, 1175.22475578, 0.00105421, -117.52247558, -0.00010542, -352.56742673, -0.00031626, -1175.22475578, -0.00105421, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 261.35949375, 0.01667785, 261.35949375, 0.05003356, 182.95164562, -2283.651517, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 65.33987344, 5.861e-05, 196.01962031, 0.00017584, 653.39873437, 0.00058612, -65.33987344, -5.861e-05, -196.01962031, -0.00017584, -653.39873437, -0.00058612, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 25.25, 5.15, 6.225)
    ops.node(123015, 25.25, 5.15, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.3, 28198308.26073333, 11749295.10863889, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 518.58420263, 0.00061242, 627.29417303, 0.01490943, 62.7294173, 0.04452086, -518.58420263, -0.00061242, -627.29417303, -0.01490943, -62.7294173, -0.04452086, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 227.74067743, 0.00082953, 275.4815885, 0.01305663, 27.54815885, 0.03349012, -227.74067743, -0.00082953, -275.4815885, -0.01305663, -27.54815885, -0.03349012, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 459.58812923, 0.01224839, 459.58812923, 0.03674517, 321.71169046, -3682.70322907, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 114.89703231, 0.00010561, 344.69109693, 0.00031684, 1148.97032308, 0.00105614, -114.89703231, -0.00010561, -344.69109693, -0.00031684, -1148.97032308, -0.00105614, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 255.43331104, 0.01659069, 255.43331104, 0.04977208, 178.80331773, -2292.24637013, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 63.85832776, 5.87e-05, 191.57498328, 0.0001761, 638.58327759, 0.00058699, -63.85832776, -5.87e-05, -191.57498328, -0.0001761, -638.58327759, -0.00058699, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 29.7, 5.15, 6.2)
    ops.node(123016, 29.7, 5.15, 8.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1, 31794396.62053964, 13247665.25855818, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 122.98085681, 0.00082379, 146.61621762, 0.01506966, 14.66162176, 0.0576628, -122.98085681, -0.00082379, -146.61621762, -0.01506966, -14.66162176, -0.0576628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 70.58491055, 0.00120153, 84.15043507, 0.01346812, 8.41504351, 0.04333818, -70.58491055, -0.00120153, -84.15043507, -0.01346812, -8.41504351, -0.04333818, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 161.54243007, 0.01647587, 161.54243007, 0.04942762, 113.07970105, -2402.5147879, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 40.38560752, 9.877e-05, 121.15682256, 0.00029631, 403.85607518, 0.00098772, -40.38560752, -9.877e-05, -121.15682256, -0.00029631, -403.85607518, -0.00098772, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 135.74551574, 0.02403065, 135.74551574, 0.07209195, 95.02186102, -1667.76086365, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 33.93637894, 8.3e-05, 101.80913681, 0.000249, 339.36378936, 0.00082999, -33.93637894, -8.3e-05, -101.80913681, -0.000249, -339.36378936, -0.00082999, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 10.3, 6.2)
    ops.node(123017, 0.0, 10.3, 8.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 31213971.14753272, 13005821.31147197, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 50.46887269, 0.00123133, 60.31604406, 0.01617541, 6.03160441, 0.05945265, -50.46887269, -0.00123133, -60.31604406, -0.01617541, -6.03160441, -0.05945265, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 53.99104935, 0.00123133, 64.52544585, 0.01617541, 6.45254458, 0.05945265, -53.99104935, -0.00123133, -64.52544585, -0.01617541, -6.45254458, -0.05945265, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 98.00748543, 0.02462652, 98.00748543, 0.07387956, 68.6052398, -1485.7808943, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 24.50187136, 9.766e-05, 73.50561408, 0.00029299, 245.01871359, 0.00097662, -24.50187136, -9.766e-05, -73.50561408, -0.00029299, -245.01871359, -0.00097662, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 98.00748543, 0.02462652, 98.00748543, 0.07387956, 68.6052398, -1485.7808943, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 24.50187136, 9.766e-05, 73.50561408, 0.00029299, 245.01871359, 0.00097662, -24.50187136, -9.766e-05, -73.50561408, -0.00029299, -245.01871359, -0.00097662, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 4.45, 10.3, 6.225)
    ops.node(123018, 4.45, 10.3, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1, 30248916.66944319, 12603715.27893466, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 76.80885676, 0.00128924, 91.8259145, 0.01416411, 9.18259145, 0.03888814, -76.80885676, -0.00128924, -91.8259145, -0.01416411, -9.18259145, -0.03888814, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 128.41510931, 0.00086613, 153.52181176, 0.01570877, 15.35218118, 0.05035365, -128.41510931, -0.00086613, -153.52181176, -0.01570877, -15.35218118, -0.05035365, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 120.55429266, 0.02578481, 120.55429266, 0.07735444, 84.38800486, -1458.454932, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 30.13857317, 7.748e-05, 90.4157195, 0.00023243, 301.38573165, 0.00077476, -30.13857317, -7.748e-05, -90.4157195, -0.00023243, -301.38573165, -0.00077476, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 143.40982835, 0.01732251, 143.40982835, 0.05196753, 100.38687985, -2029.84032883, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 35.85245709, 9.216e-05, 107.55737126, 0.00027649, 358.52457088, 0.00092165, -35.85245709, -9.216e-05, -107.55737126, -0.00027649, -358.52457088, -0.00092165, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 8.9, 10.3, 6.225)
    ops.node(123019, 8.9, 10.3, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1, 29723133.21736702, 12384638.84056959, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 78.44187954, 0.00128426, 93.82565338, 0.01361797, 9.38256534, 0.03758594, -78.44187954, -0.00128426, -93.82565338, -0.01361797, -9.38256534, -0.03758594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 130.85100726, 0.00087234, 156.51309382, 0.01509111, 15.65130938, 0.04867655, -130.85100726, -0.00087234, -156.51309382, -0.01509111, -15.65130938, -0.04867655, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 114.49027974, 0.02568526, 114.49027974, 0.07705577, 80.14319582, -1432.30427047, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 28.62256993, 7.488e-05, 85.8677098, 0.00022464, 286.22569935, 0.00074881, -28.62256993, -7.488e-05, -85.8677098, -0.00022464, -286.22569935, -0.00074881, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 139.97158221, 0.01744679, 139.97158221, 0.05234036, 97.98010755, -1980.55850961, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 34.99289555, 9.155e-05, 104.97868666, 0.00027464, 349.92895553, 0.00091546, -34.99289555, -9.155e-05, -104.97868666, -0.00027464, -349.92895553, -0.00091546, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 13.35, 10.3, 6.225)
    ops.node(123020, 13.35, 10.3, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0875, 30140039.15801616, 12558349.6491734, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 70.35294773, 0.00124847, 84.2254728, 0.01467678, 8.42254728, 0.04263651, -70.35294773, -0.00124847, -84.2254728, -0.01467678, -8.42254728, -0.04263651, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 101.91659267, 0.00093873, 122.01298568, 0.01583663, 12.20129857, 0.05160694, -101.91659267, -0.00093873, -122.01298568, -0.01583663, -12.20129857, -0.05160694, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 110.98372853, 0.02496946, 110.98372853, 0.07490837, 77.68860997, -1400.77275659, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 27.74593213, 8.181e-05, 83.2377964, 0.00024543, 277.45932132, 0.00081809, -27.74593213, -8.181e-05, -83.2377964, -0.00024543, -277.45932132, -0.00081809, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 125.92651169, 0.01877459, 125.92651169, 0.05632378, 88.14855818, -1828.58370584, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 31.48162792, 9.282e-05, 94.44488377, 0.00027847, 314.81627923, 0.00092824, -31.48162792, -9.282e-05, -94.44488377, -0.00027847, -314.81627923, -0.00092824, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 16.35, 10.3, 6.225)
    ops.node(123021, 16.35, 10.3, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0875, 28658988.31722701, 11941245.13217792, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 69.32668406, 0.00129033, 83.09606277, 0.0139595, 8.30960628, 0.03955063, -69.32668406, -0.00129033, -83.09606277, -0.0139595, -8.30960628, -0.03955063, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 100.64658396, 0.00096197, 120.63659141, 0.01501764, 12.06365914, 0.04775769, -100.64658396, -0.00096197, -120.63659141, -0.01501764, -12.06365914, -0.04775769, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 98.96294875, 0.02580656, 98.96294875, 0.07741969, 69.27406413, -1322.65409537, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 24.74073719, 7.672e-05, 74.22221156, 0.00023016, 247.40737188, 0.00076718, -24.74073719, -7.672e-05, -74.22221156, -0.00023016, -247.40737188, -0.00076718, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 117.5996793, 0.01923932, 117.5996793, 0.05771796, 82.31977551, -1704.03181644, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 29.39991982, 9.117e-05, 88.19975947, 0.0002735, 293.99919825, 0.00091166, -29.39991982, -9.117e-05, -88.19975947, -0.0002735, -293.99919825, -0.00091166, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 20.8, 10.3, 6.225)
    ops.node(123022, 20.8, 10.3, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.1, 29015982.99376784, 12089992.91406994, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 75.91894067, 0.00130229, 90.84874262, 0.01410805, 9.08487426, 0.03700495, -75.91894067, -0.00130229, -90.84874262, -0.01410805, -9.08487426, -0.03700495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 127.01837444, 0.00087149, 151.9971104, 0.01563445, 15.19971104, 0.04771904, -127.01837444, -0.00087149, -151.9971104, -0.01563445, -15.19971104, -0.04771904, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 118.03069544, 0.0260458, 118.03069544, 0.0781374, 82.62148681, -1476.12252808, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 29.50767386, 7.908e-05, 88.52302158, 0.00023723, 295.0767386, 0.00079078, -29.50767386, -7.908e-05, -88.52302158, -0.00023723, -295.0767386, -0.00079078, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 140.51453688, 0.01742984, 140.51453688, 0.05228953, 98.36017582, -2063.22501908, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 35.12863422, 9.414e-05, 105.38590266, 0.00028242, 351.2863422, 0.00094141, -35.12863422, -9.414e-05, -105.38590266, -0.00028242, -351.2863422, -0.00094141, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 25.25, 10.3, 6.225)
    ops.node(123023, 25.25, 10.3, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1, 29547375.95342891, 12311406.64726205, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 76.65460633, 0.00129423, 91.70041963, 0.01393654, 9.17004196, 0.03764415, -76.65460633, -0.00129423, -91.70041963, -0.01393654, -9.17004196, -0.03764415, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 128.15862474, 0.00086968, 153.31367845, 0.01544421, 15.33136785, 0.04866483, -128.15862474, -0.00086968, -153.31367845, -0.01544421, -15.33136785, -0.04866483, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 116.86053764, 0.02588452, 116.86053764, 0.07765356, 81.80237635, -1456.90681935, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 29.21513441, 7.689e-05, 87.64540323, 0.00023066, 292.1513441, 0.00076886, -29.21513441, -7.689e-05, -87.64540323, -0.00023066, -292.1513441, -0.00076886, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 141.00174877, 0.01739358, 141.00174877, 0.05218074, 98.70122414, -2026.91842516, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 35.25043719, 9.277e-05, 105.75131157, 0.00027831, 352.50437191, 0.00092769, -35.25043719, -9.277e-05, -105.75131157, -0.00027831, -352.50437191, -0.00092769, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 29.7, 10.3, 6.2)
    ops.node(123024, 29.7, 10.3, 8.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 29170535.41267037, 12154389.75527932, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 51.16035729, 0.00124694, 61.28997393, 0.01584221, 6.12899739, 0.05459406, -51.16035729, -0.00124694, -61.28997393, -0.01584221, -6.12899739, -0.05459406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 55.0980729, 0.00124694, 66.00734691, 0.01584221, 6.60073469, 0.05459406, -55.0980729, -0.00124694, -66.00734691, -0.01584221, -6.60073469, -0.05459406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 93.9591276, 0.0249389, 93.9591276, 0.07481669, 65.77138932, -1490.17006952, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 23.4897819, 0.00010019, 70.4693457, 0.00030056, 234.89781899, 0.00100187, -23.4897819, -0.00010019, -70.4693457, -0.00030056, -234.89781899, -0.00100187, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 93.9591276, 0.0249389, 93.9591276, 0.07481669, 65.77138932, -1490.17006952, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 23.4897819, 0.00010019, 70.4693457, 0.00030056, 234.89781899, 0.00100187, -23.4897819, -0.00010019, -70.4693457, -0.00030056, -234.89781899, -0.00100187, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.9)
    ops.node(124001, 0.0, 0.0, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 28037298.35132778, 11682207.64638657, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 36.07238937, 0.00117693, 43.80426337, 0.01883691, 4.38042634, 0.07193145, -36.07238937, -0.00117693, -43.80426337, -0.01883691, -4.38042634, -0.07193145, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 39.40513061, 0.00117693, 47.85135526, 0.01883691, 4.78513553, 0.07193145, -39.40513061, -0.00117693, -47.85135526, -0.01883691, -4.78513553, -0.07193145, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 80.10753298, 0.02353864, 80.10753298, 0.07061592, 56.07527309, -1737.97337374, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 20.02688325, 8.887e-05, 60.08064974, 0.00026661, 200.26883245, 0.0008887, -20.02688325, -8.887e-05, -60.08064974, -0.00026661, -200.26883245, -0.0008887, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 80.10753298, 0.02353864, 80.10753298, 0.07061592, 56.07527309, -1737.97337374, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 20.02688325, 8.887e-05, 60.08064974, 0.00026661, 200.26883245, 0.0008887, -20.02688325, -8.887e-05, -60.08064974, -0.00026661, -200.26883245, -0.0008887, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.45, 0.0, 8.925)
    ops.node(124002, 4.45, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1, 31434178.94242973, 13097574.55934572, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 46.10275088, 0.00110185, 55.51279621, 0.01492426, 5.55127962, 0.05369781, -46.10275088, -0.00110185, -55.51279621, -0.01492426, -5.55127962, -0.05369781, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 83.13231561, 0.00076452, 100.10047572, 0.01681725, 10.01004757, 0.07210629, -83.13231561, -0.00076452, -100.10047572, -0.01681725, -10.01004757, -0.07210629, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 113.99422461, 0.02203705, 113.99422461, 0.06611116, 79.79595723, -1415.47791272, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 28.49855615, 7.05e-05, 85.49566846, 0.00021149, 284.98556153, 0.00070498, -28.49855615, -7.05e-05, -85.49566846, -0.00021149, -284.98556153, -0.00070498, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 138.46562309, 0.01529033, 138.46562309, 0.04587098, 96.92593616, -2477.82410846, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 34.61640577, 8.563e-05, 103.84921732, 0.0002569, 346.16405773, 0.00085632, -34.61640577, -8.563e-05, -103.84921732, -0.0002569, -346.16405773, -0.00085632, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.9, 0.0, 8.925)
    ops.node(124003, 8.9, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.1, 29363664.02316358, 12234860.00965149, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 45.49253147, 0.00109164, 55.03385036, 0.01531293, 5.50338504, 0.05224064, -45.49253147, -0.00109164, -55.03385036, -0.01531293, -5.50338504, -0.05224064, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 82.17661279, 0.0007608, 99.41182137, 0.01727677, 9.94118214, 0.06993375, -82.17661279, -0.0007608, -99.41182137, -0.01727677, -9.94118214, -0.06993375, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 109.10993882, 0.02183286, 109.10993882, 0.06549858, 76.37695717, -1471.0062766, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 27.2774847, 7.224e-05, 81.83245411, 0.00021671, 272.77484704, 0.00072235, -27.2774847, -7.224e-05, -81.83245411, -0.00021671, -272.77484704, -0.00072235, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 134.46420106, 0.01521606, 134.46420106, 0.04564817, 94.12494074, -2595.60968012, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 33.61605027, 8.902e-05, 100.8481508, 0.00026706, 336.16050265, 0.00089021, -33.61605027, -8.902e-05, -100.8481508, -0.00026706, -336.16050265, -0.00089021, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 20.8, 0.0, 8.925)
    ops.node(124006, 20.8, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1, 29502791.1085671, 12292829.62856962, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 45.68311843, 0.00112648, 55.24970013, 0.015174, 5.52497001, 0.05224056, -45.68311843, -0.00112648, -55.24970013, -0.015174, -5.52497001, -0.05224056, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 82.47592996, 0.00077675, 99.74735863, 0.01709091, 9.97473586, 0.06994587, -82.47592996, -0.00077675, -99.74735863, -0.01709091, -9.97473586, -0.06994587, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 108.52526304, 0.02252966, 108.52526304, 0.06758899, 75.96768413, -1433.00864234, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 27.13131576, 7.151e-05, 81.39394728, 0.00021453, 271.3131576, 0.0007151, -27.13131576, -7.151e-05, -81.39394728, -0.00021453, -271.3131576, -0.0007151, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 133.27722961, 0.01553494, 133.27722961, 0.04660481, 93.29406073, -2514.95909703, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 33.3193074, 8.782e-05, 99.95792221, 0.00026346, 333.19307402, 0.00087819, -33.3193074, -8.782e-05, -99.95792221, -0.00026346, -333.19307402, -0.00087819, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 25.25, 0.0, 8.925)
    ops.node(124007, 25.25, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1, 29091600.08226525, 12121500.03427719, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 45.93748489, 0.00111106, 55.59994773, 0.01556824, 5.55999477, 0.05221763, -45.93748489, -0.00111106, -55.59994773, -0.01556824, -5.55999477, -0.05221763, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 83.04956612, 0.00077242, 100.51816171, 0.01756235, 10.05181617, 0.06982245, -83.04956612, -0.00077242, -100.51816171, -0.01756235, -10.05181617, -0.06982245, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 108.76012508, 0.02222111, 108.76012508, 0.06666332, 76.13208756, -1488.83510375, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 27.19003127, 7.268e-05, 81.57009381, 0.00021803, 271.90031271, 0.00072677, -27.19003127, -7.268e-05, -81.57009381, -0.00021803, -271.90031271, -0.00072677, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 134.39430727, 0.01544837, 134.39430727, 0.04634512, 94.07601509, -2633.52568726, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 33.59857682, 8.981e-05, 100.79573045, 0.00026942, 335.98576818, 0.00089807, -33.59857682, -8.981e-05, -100.79573045, -0.00026942, -335.98576818, -0.00089807, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 29.7, 0.0, 8.9)
    ops.node(124008, 29.7, 0.0, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 28929448.73600231, 12053936.9733343, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 36.16776262, 0.00113464, 43.85168693, 0.01891795, 4.38516869, 0.07324681, -36.16776262, -0.00113464, -43.85168693, -0.01891795, -4.38516869, -0.07324681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 39.6376491, 0.00113464, 48.05875877, 0.01891795, 4.80587588, 0.07324681, -39.6376491, -0.00113464, -48.05875877, -0.01891795, -4.80587588, -0.07324681, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 83.45144028, 0.02269286, 83.45144028, 0.06807858, 58.41600819, -1837.90389291, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 20.86286007, 8.972e-05, 62.58858021, 0.00026917, 208.62860069, 0.00089724, -20.86286007, -8.972e-05, -62.58858021, -0.00026917, -208.62860069, -0.00089724, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 83.45144028, 0.02269286, 83.45144028, 0.06807858, 58.41600819, -1837.90389291, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 20.86286007, 8.972e-05, 62.58858021, 0.00026917, 208.62860069, 0.00089724, -20.86286007, -8.972e-05, -62.58858021, -0.00026917, -208.62860069, -0.00089724, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 5.15, 8.9)
    ops.node(124009, 0.0, 5.15, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1, 29240683.46867206, 12183618.11194669, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 83.57062913, 0.00077193, 101.11488762, 0.01707122, 10.11148876, 0.06944945, -83.57062913, -0.00077193, -101.11488762, -0.01707122, -10.11148876, -0.06944945, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 46.23369762, 0.00110842, 55.93969062, 0.01514313, 5.59396906, 0.05187536, -46.23369762, -0.00110842, -55.93969062, -0.01514313, -5.59396906, -0.05187536, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 134.7771921, 0.01543853, 134.7771921, 0.0463156, 94.34403447, -2618.08840809, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 33.69429803, 8.96e-05, 101.08289408, 0.00026881, 336.94298025, 0.00089604, -33.69429803, -8.96e-05, -101.08289408, -0.00026881, -336.94298025, -0.00089604, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 109.20795294, 0.02216836, 109.20795294, 0.06650508, 76.44556706, -1483.55810891, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 27.30198824, 7.26e-05, 81.90596471, 0.00021781, 273.01988236, 0.00072604, -27.30198824, -7.26e-05, -81.90596471, -0.00021781, -273.01988236, -0.00072604, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 4.45, 5.15, 8.925)
    ops.node(124010, 4.45, 5.15, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.3, 30357664.43954884, 12649026.84981202, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 414.43784483, 0.00058057, 501.83904653, 0.01634018, 50.18390465, 0.05288609, -414.43784483, -0.00058057, -501.83904653, -0.01634018, -50.18390465, -0.05288609, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 175.495713, 0.00077047, 212.50617525, 0.01424842, 21.25061752, 0.03946707, -175.495713, -0.00077047, -212.50617525, -0.01424842, -21.25061752, -0.03946707, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 449.51416496, 0.01161138, 449.51416496, 0.03483414, 314.65991547, -4106.10405704, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 112.37854124, 9.595e-05, 337.13562372, 0.00028785, 1123.78541241, 0.00095951, -112.37854124, -9.595e-05, -337.13562372, -0.00028785, -1123.78541241, -0.00095951, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 249.65925552, 0.01540941, 249.65925552, 0.04622824, 174.76147886, -2015.04264437, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 62.41481388, 5.329e-05, 187.24444164, 0.00015987, 624.1481388, 0.00053291, -62.41481388, -5.329e-05, -187.24444164, -0.00015987, -624.1481388, -0.00053291, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.9, 5.15, 8.925)
    ops.node(124011, 8.9, 5.15, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.3, 30059672.92295786, 12524863.71789911, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 412.55176777, 0.00057871, 499.9310146, 0.01592346, 49.99310146, 0.05231675, -412.55176777, -0.00057871, -499.9310146, -0.01592346, -49.99310146, -0.05231675, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 174.63827878, 0.00076651, 211.62699744, 0.01388966, 21.16269974, 0.03900301, -174.63827878, -0.00076651, -211.62699744, -0.01388966, -21.16269974, -0.03900301, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 439.37077212, 0.01157411, 439.37077212, 0.03472232, 307.55954048, -3851.39316064, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 109.84269303, 9.472e-05, 329.52807909, 0.00028415, 1098.4269303, 0.00094716, -109.84269303, -9.472e-05, -329.52807909, -0.00028415, -1098.4269303, -0.00094716, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 244.11036783, 0.01533026, 244.11036783, 0.04599078, 170.87725748, -1919.51488563, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 61.02759196, 5.262e-05, 183.08277587, 0.00015787, 610.27591957, 0.00052623, -61.02759196, -5.262e-05, -183.08277587, -0.00015787, -610.27591957, -0.00052623, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 13.35, 5.15, 8.925)
    ops.node(124012, 13.35, 5.15, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.21, 29223038.73213694, 12176266.13839039, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 256.28671023, 0.0006329, 311.02802084, 0.01669472, 31.10280208, 0.05547838, -256.28671023, -0.0006329, -311.02802084, -0.01669472, -31.10280208, -0.05547838, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 122.51379427, 0.00086231, 148.682009, 0.01477012, 14.8682009, 0.04233194, -122.51379427, -0.00086231, -148.682009, -0.01477012, -14.8682009, -0.04233194, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 265.99299834, 0.01265799, 265.99299834, 0.03797397, 186.19509884, -3094.78812548, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 66.49824959, 8.426e-05, 199.49474876, 0.00025278, 664.98249586, 0.0008426, -66.49824959, -8.426e-05, -199.49474876, -0.00025278, -664.98249586, -0.0008426, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 177.09165094, 0.01724624, 177.09165094, 0.05173871, 123.96415566, -1669.28577327, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 44.27291273, 5.61e-05, 132.8187382, 0.00016829, 442.72912734, 0.00056098, -44.27291273, -5.61e-05, -132.8187382, -0.00016829, -442.72912734, -0.00056098, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 16.35, 5.15, 8.925)
    ops.node(124013, 16.35, 5.15, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.21, 27588891.6174261, 11495371.50726088, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 261.69730342, 0.00064026, 318.58955804, 0.01706533, 31.8589558, 0.0545844, -261.69730342, -0.00064026, -318.58955804, -0.01706533, -31.8589558, -0.0545844, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 124.58431705, 0.00086681, 151.6685957, 0.01508916, 15.16685957, 0.04175228, -124.58431705, -0.00086681, -151.6685957, -0.01508916, -15.16685957, -0.04175228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 253.56745116, 0.01280525, 253.56745116, 0.03841575, 177.49721581, -3176.47208562, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 63.39186279, 8.508e-05, 190.17558837, 0.00025525, 633.91862789, 0.00085082, -63.39186279, -8.508e-05, -190.17558837, -0.00025525, -633.91862789, -0.00085082, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 168.15057608, 0.01733624, 168.15057608, 0.05200871, 117.70540325, -1704.23367951, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 42.03764402, 5.642e-05, 126.11293206, 0.00016926, 420.37644019, 0.00056421, -42.03764402, -5.642e-05, -126.11293206, -0.00016926, -420.37644019, -0.00056421, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 20.8, 5.15, 8.925)
    ops.node(124014, 20.8, 5.15, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.3, 30239701.23109622, 12599875.51295676, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 412.98537394, 0.0005781, 500.23073785, 0.01601895, 50.02307379, 0.05250515, -412.98537394, -0.0005781, -500.23073785, -0.01601895, -50.02307379, -0.05250515, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 174.84542513, 0.00076502, 211.78245416, 0.01397036, 21.17824542, 0.03914781, -174.84542513, -0.00076502, -211.78245416, -0.01397036, -21.17824542, -0.03914781, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 442.61988177, 0.011562, 442.61988177, 0.03468599, 309.83391724, -3868.75271788, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 110.65497044, 9.485e-05, 331.96491133, 0.00028454, 1106.54970443, 0.00094848, -110.65497044, -9.485e-05, -331.96491133, -0.00028454, -1106.54970443, -0.00094848, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 245.92714584, 0.01530045, 245.92714584, 0.04590136, 172.14900209, -1926.04927135, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 61.48178646, 5.27e-05, 184.44535938, 0.0001581, 614.81786459, 0.00052699, -61.48178646, -5.27e-05, -184.44535938, -0.0001581, -614.81786459, -0.00052699, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 25.25, 5.15, 8.925)
    ops.node(124015, 25.25, 5.15, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.3, 28955036.54104822, 12064598.55877009, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 424.53385874, 0.00059084, 515.76714113, 0.01628365, 51.57671411, 0.05205646, -424.53385874, -0.00059084, -515.76714113, -0.01628365, -51.57671411, -0.05205646, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 178.96553701, 0.00078432, 217.42563398, 0.01420514, 21.7425634, 0.03889031, -178.96553701, -0.00078432, -217.42563398, -0.01420514, -21.7425634, -0.03889031, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 426.64635402, 0.01181683, 426.64635402, 0.0354505, 298.65244782, -4073.34537745, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 106.66158851, 9.548e-05, 319.98476552, 0.00028644, 1066.61588506, 0.00095481, -106.66158851, -9.548e-05, -319.98476552, -0.00028644, -1066.61588506, -0.00095481, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 236.8159964, 0.01568647, 236.8159964, 0.04705942, 165.77119748, -2002.79761644, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 59.2039991, 5.3e-05, 177.6119973, 0.00015899, 592.039991, 0.00052998, -59.2039991, -5.3e-05, -177.6119973, -0.00015899, -592.039991, -0.00052998, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 29.7, 5.15, 8.9)
    ops.node(124016, 29.7, 5.15, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1, 29679217.27517597, 12366340.53132332, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 83.23215199, 0.00076851, 100.62078628, 0.01716509, 10.06207863, 0.07016919, -83.23215199, -0.00076851, -100.62078628, -0.01716509, -10.06207863, -0.07016919, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 46.08097526, 0.00110468, 55.70808698, 0.01522317, 5.5708087, 0.05239431, -46.08097526, -0.00110468, -55.70808698, -0.01522317, -5.5708087, -0.05239431, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 135.8668075, 0.01537014, 135.8668075, 0.04611042, 95.10676525, -2606.31428565, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 33.96670187, 8.899e-05, 101.90010562, 0.00026698, 339.66701874, 0.00088993, -33.96670187, -8.899e-05, -101.90010562, -0.00026698, -339.66701874, -0.00088993, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 110.38487445, 0.02209368, 110.38487445, 0.06628103, 77.26941211, -1478.01757336, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 27.59621861, 7.23e-05, 82.78865584, 0.00021691, 275.96218612, 0.00072303, -27.59621861, -7.23e-05, -82.78865584, -0.00021691, -275.96218612, -0.00072303, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 10.3, 8.9)
    ops.node(124017, 0.0, 10.3, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 27817500.66166507, 11590625.27569378, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 36.56939151, 0.00114105, 44.42295469, 0.01906241, 4.44229547, 0.07183083, -36.56939151, -0.00114105, -44.42295469, -0.01906241, -4.44229547, -0.07183083, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 40.24954453, 0.00114105, 48.89344938, 0.01906241, 4.88934494, 0.07183083, -40.24954453, -0.00114105, -48.89344938, -0.01906241, -4.88934494, -0.07183083, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 81.85925864, 0.02282109, 81.85925864, 0.06846328, 57.30148105, -1863.93621362, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 20.46481466, 9.153e-05, 61.39444398, 0.00027459, 204.6481466, 0.00091531, -20.46481466, -9.153e-05, -61.39444398, -0.00027459, -204.6481466, -0.00091531, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 81.85925864, 0.02282109, 81.85925864, 0.06846328, 57.30148105, -1863.93621362, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 20.46481466, 9.153e-05, 61.39444398, 0.00027459, 204.6481466, 0.00091531, -20.46481466, -9.153e-05, -61.39444398, -0.00027459, -204.6481466, -0.00091531, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 4.45, 10.3, 8.925)
    ops.node(124018, 4.45, 10.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1, 29866529.81731981, 12444387.42388326, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 54.25759342, 0.00117905, 65.57198983, 0.01632184, 6.55719898, 0.04933485, -54.25759342, -0.00117905, -65.57198983, -0.01632184, -6.55719898, -0.04933485, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 92.01201374, 0.00080549, 111.19938148, 0.01826267, 11.11993815, 0.06452261, -92.01201374, -0.00080549, -111.19938148, -0.01826267, -11.11993815, -0.06452261, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 102.81417596, 0.02358094, 102.81417596, 0.07074282, 71.96992317, -1228.72980059, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 25.70354399, 6.692e-05, 77.11063197, 0.00020076, 257.0354399, 0.00066921, -25.70354399, -6.692e-05, -77.11063197, -0.00020076, -257.0354399, -0.00066921, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 125.35292969, 0.01610978, 125.35292969, 0.04832934, 87.74705078, -2085.41960254, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 31.33823242, 8.159e-05, 94.01469726, 0.00024478, 313.38232422, 0.00081592, -31.33823242, -8.159e-05, -94.01469726, -0.00024478, -313.38232422, -0.00081592, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 8.9, 10.3, 8.925)
    ops.node(124019, 8.9, 10.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1, 29242134.9825918, 12184222.90941325, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 53.36550673, 0.00121151, 64.57270214, 0.01626881, 6.45727021, 0.04873988, -53.36550673, -0.00121151, -64.57270214, -0.01626881, -6.45727021, -0.04873988, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 90.80833977, 0.00081746, 109.87883814, 0.01817608, 10.98788381, 0.06367661, -90.80833977, -0.00081746, -109.87883814, -0.01817608, -10.98788381, -0.06367661, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 99.53411238, 0.02423022, 99.53411238, 0.07269066, 69.67387867, -1223.42230356, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 24.88352809, 6.617e-05, 74.65058428, 0.00019851, 248.83528095, 0.0006617, -24.88352809, -6.617e-05, -74.65058428, -0.00019851, -248.83528095, -0.0006617, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 123.22320817, 0.01634919, 123.22320817, 0.04904757, 86.25624572, -2074.35919757, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 30.80580204, 8.192e-05, 92.41740613, 0.00024575, 308.05802042, 0.00081918, -30.80580204, -8.192e-05, -92.41740613, -0.00024575, -308.05802042, -0.00081918, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 13.35, 10.3, 8.925)
    ops.node(124020, 13.35, 10.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0875, 29487427.62516078, 12286428.17715032, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 49.69776651, 0.00120503, 60.14901623, 0.01661164, 6.01490162, 0.0531718, -49.69776651, -0.00120503, -60.14901623, -0.01661164, -6.01490162, -0.0531718, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 73.10382642, 0.00089764, 88.47728079, 0.01799034, 8.84772808, 0.06476363, -73.10382642, -0.00089764, -88.47728079, -0.01799034, -8.84772808, -0.06476363, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 90.62407974, 0.02410063, 90.62407974, 0.07230189, 63.43685582, -1242.3895438, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 22.65601994, 6.828e-05, 67.96805981, 0.00020484, 226.56019935, 0.0006828, -22.65601994, -6.828e-05, -67.96805981, -0.00020484, -226.56019935, -0.0006828, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 107.43115426, 0.01795277, 107.43115426, 0.0538583, 75.20180798, -1861.30260887, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 26.85778856, 8.094e-05, 80.57336569, 0.00024283, 268.57788564, 0.00080943, -26.85778856, -8.094e-05, -80.57336569, -0.00024283, -268.57788564, -0.00080943, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 16.35, 10.3, 8.925)
    ops.node(124021, 16.35, 10.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0875, 29304343.46012599, 12210143.10838583, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 50.13734807, 0.00118153, 60.70304596, 0.01630433, 6.0703046, 0.05269935, -50.13734807, -0.00118153, -60.70304596, -0.01630433, -6.0703046, -0.05269935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 73.60076178, 0.00088663, 89.11102396, 0.01766447, 8.9111024, 0.06422648, -73.60076178, -0.00088663, -89.11102396, -0.01766447, -8.9111024, -0.06422648, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 86.56547655, 0.02363052, 86.56547655, 0.07089156, 60.59583358, -1199.49799334, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 21.64136914, 6.563e-05, 64.92410741, 0.00019689, 216.41369136, 0.0006563, -21.64136914, -6.563e-05, -64.92410741, -0.00019689, -216.41369136, -0.0006563, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 105.4059717, 0.01773264, 105.4059717, 0.05319792, 73.78418019, -1787.89678286, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 26.35149293, 7.991e-05, 79.05447878, 0.00023974, 263.51492926, 0.00079914, -26.35149293, -7.991e-05, -79.05447878, -0.00023974, -263.51492926, -0.00079914, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 20.8, 10.3, 8.925)
    ops.node(124022, 20.8, 10.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.1, 29156999.72786552, 12148749.88661063, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 54.30579886, 0.00117533, 65.72069986, 0.01589364, 6.57206999, 0.04828761, -54.30579886, -0.00117533, -65.72069986, -0.01589364, -6.57206999, -0.04828761, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 92.00061132, 0.00080538, 111.33883841, 0.0177732, 11.13388384, 0.0631657, -92.00061132, -0.00080538, -111.33883841, -0.0177732, -11.13388384, -0.0631657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 95.59949968, 0.02350666, 95.59949968, 0.07051999, 66.91964978, -1191.77370745, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 23.89987492, 6.374e-05, 71.69962476, 0.00019122, 238.99874921, 0.0006374, -23.89987492, -6.374e-05, -71.69962476, -0.00019122, -238.99874921, -0.0006374, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 121.50099798, 0.0161077, 121.50099798, 0.04832309, 85.05069859, -2008.52117569, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 30.3752495, 8.101e-05, 91.12574849, 0.00024303, 303.75249496, 0.00081009, -30.3752495, -8.101e-05, -91.12574849, -0.00024303, -303.75249496, -0.00081009, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 25.25, 10.3, 8.925)
    ops.node(124023, 25.25, 10.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1, 29607508.99708243, 12336462.08211768, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 55.28682981, 0.00112558, 66.85084168, 0.01641485, 6.68508417, 0.04920797, -55.28682981, -0.00112558, -66.85084168, -0.01641485, -6.68508417, -0.04920797, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 93.06160146, 0.00078501, 112.5267339, 0.01841106, 11.25267339, 0.06436287, -93.06160146, -0.00078501, -112.5267339, -0.01841106, -11.25267339, -0.06436287, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 102.593545, 0.02251162, 102.593545, 0.06753485, 71.8154815, -1230.52461487, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 25.64838625, 6.736e-05, 76.94515875, 0.00020209, 256.48386251, 0.00067362, -25.64838625, -6.736e-05, -76.94515875, -0.00020209, -256.48386251, -0.00067362, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 124.65036704, 0.01570024, 124.65036704, 0.04710071, 87.25525693, -2089.16108907, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 31.16259176, 8.184e-05, 93.48777528, 0.00024553, 311.62591759, 0.00081844, -31.16259176, -8.184e-05, -93.48777528, -0.00024553, -311.62591759, -0.00081844, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 29.7, 10.3, 8.9)
    ops.node(124024, 29.7, 10.3, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 31247713.66914677, 13019880.69547782, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 36.56320982, 0.00113806, 44.09698756, 0.01838865, 4.40969876, 0.07534985, -36.56320982, -0.00113806, -44.09698756, -0.01838865, -4.40969876, -0.07534985, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 39.89880607, 0.00113806, 48.11987688, 0.01838865, 4.81198769, 0.07534985, -39.89880607, -0.00113806, -48.11987688, -0.01838865, -4.81198769, -0.07534985, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 86.47253142, 0.02276129, 86.47253142, 0.06828386, 60.530772, -1758.1163669, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 21.61813286, 8.607e-05, 64.85439857, 0.00025822, 216.18132855, 0.00086075, -21.61813286, -8.607e-05, -64.85439857, -0.00025822, -216.18132855, -0.00086075, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 86.47253142, 0.02276129, 86.47253142, 0.06828386, 60.530772, -1758.1163669, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 21.61813286, 8.607e-05, 64.85439857, 0.00025822, 216.18132855, 0.00086075, -21.61813286, -8.607e-05, -64.85439857, -0.00025822, -216.18132855, -0.00086075, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.35, 0.0, 0.0)
    ops.node(124025, 13.35, 0.0, 1.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 170004, 124025, 0.1575, 28440869.5059365, 11850362.29414021, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 259.16699126, 0.0008197, 309.30801452, 0.0193251, 30.93080145, 0.04402713, -259.16699126, -0.0008197, -309.30801452, -0.0193251, -30.93080145, -0.04402713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 275.19980625, 0.00072123, 328.44269732, 0.02076726, 32.84426973, 0.050629, -275.19980625, -0.00072123, -328.44269732, -0.02076726, -32.84426973, -0.050629, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 257.44518459, 0.01639398, 257.44518459, 0.04918193, 180.21162921, -4809.39274456, 0.05, 2, 0, 70004, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 64.36129615, 6.724e-05, 193.08388844, 0.00020173, 643.61296148, 0.00067243, -64.36129615, -6.724e-05, -193.08388844, -0.00020173, -643.61296148, -0.00067243, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 331.00095162, 0.01442462, 331.00095162, 0.04327385, 231.70066613, -5776.70605411, 0.05, 2, 0, 70004, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 82.7502379, 8.646e-05, 248.25071371, 0.00025937, 827.50237905, 0.00086455, -82.7502379, -8.646e-05, -248.25071371, -0.00025937, -827.50237905, -0.00086455, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 13.35, 0.0, 1.875)
    ops.node(121004, 13.35, 0.0, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 174025, 121004, 0.1575, 29066461.71069028, 12111025.71278762, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 176.63225199, 0.00078232, 211.13306018, 0.01877867, 21.11330602, 0.04597197, -176.63225199, -0.00078232, -211.13306018, -0.01877867, -21.11330602, -0.04597197, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 215.39456751, 0.00069289, 257.46664989, 0.02018749, 25.74666499, 0.05306087, -215.39456751, -0.00069289, -257.46664989, -0.02018749, -25.74666499, -0.05306087, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 257.78180534, 0.01564649, 257.78180534, 0.04693946, 180.44726374, -4709.93196638, 0.05, 2, 0, 74025, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 64.44545134, 6.588e-05, 193.33635401, 0.00019765, 644.45451335, 0.00065882, -64.44545134, -6.588e-05, -193.33635401, -0.00019765, -644.45451335, -0.00065882, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 331.43374972, 0.01385781, 331.43374972, 0.04157343, 232.00362481, -5705.97562527, 0.05, 2, 0, 74025, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 82.85843743, 8.471e-05, 248.57531229, 0.00025412, 828.58437431, 0.00084705, -82.85843743, -8.471e-05, -248.57531229, -0.00025412, -828.58437431, -0.00084705, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.35, 0.0, 0.0)
    ops.node(124026, 16.35, 0.0, 1.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 170005, 124026, 0.1575, 28002062.98764221, 11667526.24485092, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 258.54065474, 0.00083641, 308.51116831, 0.01861758, 30.85111683, 0.04239409, -258.54065474, -0.00083641, -308.51116831, -0.01861758, -30.85111683, -0.04239409, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 275.38911723, 0.00073291, 328.61608702, 0.01999442, 32.8616087, 0.04873732, -275.38911723, -0.00073291, -328.61608702, -0.01999442, -32.8616087, -0.04873732, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 251.71593108, 0.01672819, 251.71593108, 0.05018458, 176.20115175, -4697.42199654, 0.05, 2, 0, 70005, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 62.92898277, 6.678e-05, 188.78694831, 0.00020033, 629.2898277, 0.00066777, -62.92898277, -6.678e-05, -188.78694831, -0.00020033, -629.2898277, -0.00066777, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 323.63476853, 0.01465818, 323.63476853, 0.04397454, 226.54433797, -5619.08979741, 0.05, 2, 0, 70005, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 80.90869213, 8.586e-05, 242.7260764, 0.00025757, 809.08692132, 0.00085856, -80.90869213, -8.586e-05, -242.7260764, -0.00025757, -809.08692132, -0.00085856, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 16.35, 0.0, 1.875)
    ops.node(121005, 16.35, 0.0, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 174026, 121005, 0.1575, 30064246.19062177, 12526769.24609241, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 177.79832189, 0.00076967, 212.39462815, 0.01893347, 21.23946281, 0.04798673, -177.79832189, -0.00076967, -212.39462815, -0.01893347, -21.23946281, -0.04798673, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 216.60730184, 0.000684, 258.75512681, 0.02035999, 25.87551268, 0.05548184, -216.60730184, -0.000684, -258.75512681, -0.02035999, -25.87551268, -0.05548184, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 263.68440413, 0.01539343, 263.68440413, 0.04618028, 184.57908289, -4655.06415807, 0.05, 2, 0, 74026, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 65.92110103, 6.515e-05, 197.7633031, 0.00019546, 659.21101033, 0.00065154, -65.92110103, -6.515e-05, -197.7633031, -0.00019546, -659.21101033, -0.00065154, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 339.02280531, 0.01367999, 339.02280531, 0.04103998, 237.31596372, -5628.36775205, 0.05, 2, 0, 74026, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 84.75570133, 8.377e-05, 254.26710398, 0.00025131, 847.55701328, 0.00083769, -84.75570133, -8.377e-05, -254.26710398, -0.00025131, -847.55701328, -0.00083769, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.35, 0.0, 3.525)
    ops.node(124027, 13.35, 0.0, 4.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4067, 171004, 124027, 0.1575, 29855066.03650594, 12439610.84854414, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24067, 147.63493871, 0.00072909, 177.09511939, 0.02543717, 17.70951194, 0.06558681, -147.63493871, -0.00072909, -177.09511939, -0.02543717, -17.70951194, -0.06558681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14067, 207.77548929, 0.00066206, 249.23656557, 0.02757624, 24.92365656, 0.07675598, -207.77548929, -0.00066206, -249.23656557, -0.02757624, -24.92365656, -0.07675598, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24067, 4067, 0.0, 312.1625582, 0.01458188, 312.1625582, 0.04374565, 218.51379074, -6967.95588039, 0.05, 2, 0, 71004, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44067, 78.04063955, 6.453e-05, 234.12191865, 0.00019358, 780.40639549, 0.00064528, -78.04063955, -6.453e-05, -234.12191865, -0.00019358, -780.40639549, -0.00064528, 0.4, 0.3, 0.003, 0.0, 0.0, 24067, 2)
    ops.limitCurve('ThreePoint', 14067, 4067, 0.0, 384.36947537, 0.01324126, 384.36947537, 0.03972377, 269.05863276, -9011.04235874, 0.05, 2, 0, 71004, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34067, 96.09236884, 7.945e-05, 288.27710653, 0.00023836, 960.92368843, 0.00079454, -96.09236884, -7.945e-05, -288.27710653, -0.00023836, -960.92368843, -0.00079454, 0.4, 0.3, 0.003, 0.0, 0.0, 14067, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4067, 99999, 'P', 44067, 'Vy', 34067, 'Vz', 24067, 'My', 14067, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4067, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4067, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 13.35, 0.0, 4.85)
    ops.node(122004, 13.35, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 174027, 122004, 0.1575, 28802750.10365355, 12001145.87652231, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 151.38640006, 0.00072997, 182.06380516, 0.02552987, 18.20638052, 0.06524569, -151.38640006, -0.00072997, -182.06380516, -0.02552987, -18.20638052, -0.06524569, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 183.5968242, 0.00066278, 220.80144858, 0.02767697, 22.08014486, 0.07632533, -183.5968242, -0.00066278, -220.80144858, -0.02767697, -22.08014486, -0.07632533, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 294.20707913, 0.01459938, 294.20707913, 0.04379814, 205.94495539, -6706.00311944, 0.05, 2, 0, 74027, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 73.55176978, 6.304e-05, 220.65530935, 0.00018912, 735.51769782, 0.00063038, -73.55176978, -6.304e-05, -220.65530935, -0.00018912, -735.51769782, -0.00063038, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 362.43357842, 0.01325552, 362.43357842, 0.03976656, 253.70350489, -8736.5458384, 0.05, 2, 0, 74027, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 90.6083946, 7.766e-05, 271.82518381, 0.00023297, 906.08394604, 0.00077657, -90.6083946, -7.766e-05, -271.82518381, -0.00023297, -906.08394604, -0.00077657, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.35, 0.0, 3.525)
    ops.node(124028, 16.35, 0.0, 4.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 171005, 124028, 0.1575, 29308508.27293496, 12211878.44705623, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 147.13348809, 0.00072731, 176.59937297, 0.02488936, 17.6599373, 0.06390687, -147.13348809, -0.00072731, -176.59937297, -0.02488936, -17.6599373, -0.06390687, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 207.19351978, 0.00066105, 248.68740727, 0.02698045, 24.86874073, 0.07477344, -207.19351978, -0.00066105, -248.68740727, -0.02698045, -24.86874073, -0.07477344, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 304.81206132, 0.01454629, 304.81206132, 0.04363887, 213.36844293, -6784.53308043, 0.05, 2, 0, 71005, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 76.20301533, 6.418e-05, 228.60904599, 0.00019255, 762.03015331, 0.00064184, -76.20301533, -6.418e-05, -228.60904599, -0.00019255, -762.03015331, -0.00064184, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 375.28593985, 0.01322108, 375.28593985, 0.03966324, 262.70015789, -8743.09210098, 0.05, 2, 0, 71005, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 93.82148496, 7.902e-05, 281.46445489, 0.00023707, 938.21484962, 0.00079023, -93.82148496, -7.902e-05, -281.46445489, -0.00023707, -938.21484962, -0.00079023, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 16.35, 0.0, 4.85)
    ops.node(122005, 16.35, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 174028, 122005, 0.1575, 29822002.39648008, 12425834.3318667, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 151.81556414, 0.00073535, 182.36965311, 0.02541658, 18.23696531, 0.06718836, -151.81556414, -0.00073535, -182.36965311, -0.02541658, -18.23696531, -0.06718836, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 184.72082309, 0.00066592, 221.89735697, 0.02755085, 22.1897357, 0.07871757, -184.72082309, -0.00066592, -221.89735697, -0.02755085, -22.1897357, -0.07871757, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 302.6404979, 0.01470699, 302.6404979, 0.04412098, 211.84834853, -6708.95256184, 0.05, 2, 0, 74028, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 75.66012448, 6.263e-05, 226.98037343, 0.00018789, 756.60124476, 0.00062629, -75.66012448, -6.263e-05, -226.98037343, -0.00018789, -756.60124476, -0.00062629, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 372.60232953, 0.01331832, 372.60232953, 0.03995496, 260.82163067, -8740.87424879, 0.05, 2, 0, 74028, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 93.15058238, 7.711e-05, 279.45174715, 0.00023132, 931.50582383, 0.00077107, -93.15058238, -7.711e-05, -279.45174715, -0.00023132, -931.50582383, -0.00077107, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.35, 0.0, 6.225)
    ops.node(124029, 13.35, 0.0, 7.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4072, 172004, 124029, 0.0875, 29864763.85110749, 12443651.60462812, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24072, 71.07858012, 0.0009311, 85.04252303, 0.01402689, 8.5042523, 0.04082892, -71.07858012, -0.0009311, -85.04252303, -0.01402689, -8.5042523, -0.04082892, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14072, 103.21141505, 0.00075082, 123.48810467, 0.01527981, 12.34881047, 0.04956902, -103.21141505, -0.00075082, -123.48810467, -0.01527981, -12.34881047, -0.04956902, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24072, 4072, 0.0, 117.65867698, 0.01862193, 117.65867698, 0.05586578, 82.36107389, -2701.30277427, 0.05, 2, 0, 72004, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44072, 29.41466924, 4.376e-05, 88.24400773, 0.00013129, 294.14669245, 0.00043765, -29.41466924, -4.376e-05, -88.24400773, -0.00013129, -294.14669245, -0.00043765, 0.4, 0.3, 0.003, 0.0, 0.0, 24072, 2)
    ops.limitCurve('ThreePoint', 14072, 4072, 0.0, 171.32002286, 0.01501645, 171.32002286, 0.04504936, 119.924016, -3453.8586808, 0.05, 2, 0, 72004, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34072, 42.83000572, 6.372e-05, 128.49001715, 0.00019117, 428.30005716, 0.00063725, -42.83000572, -6.372e-05, -128.49001715, -0.00019117, -428.30005716, -0.00063725, 0.4, 0.3, 0.003, 0.0, 0.0, 14072, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4072, 99999, 'P', 44072, 'Vy', 34072, 'Vz', 24072, 'My', 14072, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4072, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4072, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 13.35, 0.0, 7.5)
    ops.node(123004, 13.35, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 174029, 123004, 0.0875, 28663243.73848553, 11943018.22436897, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 83.68968715, 0.00093157, 100.50400471, 0.01500614, 10.05040047, 0.04210923, -83.68968715, -0.00093157, -100.50400471, -0.01500614, -10.05040047, -0.04210923, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 111.19387923, 0.00075429, 133.53413715, 0.01636916, 13.35341372, 0.05104355, -111.19387923, -0.00075429, -133.53413715, -0.01636916, -13.35341372, -0.05104355, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 111.19457222, 0.01863141, 111.19457222, 0.05589422, 77.83620055, -2618.30008481, 0.05, 2, 0, 74029, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 27.79864305, 4.309e-05, 83.39592916, 0.00012928, 277.98643054, 0.00043094, -27.79864305, -4.309e-05, -83.39592916, -0.00012928, -277.98643054, -0.00043094, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 161.30314125, 0.01508573, 161.30314125, 0.0452572, 112.91219887, -3446.63610483, 0.05, 2, 0, 74029, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 40.32578531, 6.251e-05, 120.97735594, 0.00018754, 403.25785312, 0.00062514, -40.32578531, -6.251e-05, -120.97735594, -0.00018754, -403.25785312, -0.00062514, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.35, 0.0, 6.225)
    ops.node(124030, 16.35, 0.0, 7.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 172005, 124030, 0.0875, 30559715.08953976, 12733214.62064156, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 71.02815082, 0.00093803, 84.9160434, 0.01446434, 8.49160434, 0.04232804, -71.02815082, -0.00093803, -84.9160434, -0.01446434, -8.49160434, -0.04232804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 103.21315586, 0.00075329, 123.39407294, 0.01575992, 12.33940729, 0.05140737, -103.21315586, -0.00075329, -123.39407294, -0.01575992, -12.33940729, -0.05140737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 124.83991108, 0.01876052, 124.83991108, 0.05628155, 87.38793775, -2776.09692295, 0.05, 2, 0, 72005, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 31.20997777, 4.538e-05, 93.62993331, 0.00013614, 312.09977769, 0.0004538, -31.20997777, -4.538e-05, -93.62993331, -0.00013614, -312.09977769, -0.0004538, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 176.67266731, 0.01506583, 176.67266731, 0.04519749, 123.67086712, -3572.45380332, 0.05, 2, 0, 72005, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 44.16816683, 6.422e-05, 132.50450048, 0.00019266, 441.68166827, 0.00064221, -44.16816683, -6.422e-05, -132.50450048, -0.00019266, -441.68166827, -0.00064221, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 16.35, 0.0, 7.5)
    ops.node(123005, 16.35, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 174030, 123005, 0.0875, 30179067.18952144, 12574611.32896727, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 83.35175362, 0.00086109, 99.94395129, 0.01530415, 9.99439513, 0.04470289, -83.35175362, -0.00086109, -99.94395129, -0.01530415, -9.99439513, -0.04470289, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 110.00808793, 0.00071014, 131.9065587, 0.01673384, 13.19065587, 0.05434516, -110.00808793, -0.00071014, -131.9065587, -0.01673384, -13.19065587, -0.05434516, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 115.59562148, 0.01722187, 115.59562148, 0.0516656, 80.91693504, -2626.84485016, 0.05, 2, 0, 74030, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 28.89890537, 4.255e-05, 86.69671611, 0.00012765, 288.9890537, 0.00042549, -28.89890537, -4.255e-05, -86.69671611, -0.00012765, -288.9890537, -0.00042549, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 168.54201033, 0.01420285, 168.54201033, 0.04260855, 117.97940723, -3460.36368793, 0.05, 2, 0, 74030, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 42.13550258, 6.204e-05, 126.40650775, 0.00018612, 421.35502583, 0.00062038, -42.13550258, -6.204e-05, -126.40650775, -0.00018612, -421.35502583, -0.00062038, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.35, 0.0, 8.925)
    ops.node(124031, 13.35, 0.0, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4077, 173004, 124031, 0.0875, 28529746.39561564, 11887394.33150652, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24077, 51.2883105, 0.00086072, 62.16191873, 0.01685683, 6.21619187, 0.0521378, -51.2883105, -0.00086072, -62.16191873, -0.01685683, -6.21619187, -0.0521378, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14077, 75.18516501, 0.00070512, 91.12513303, 0.01845183, 9.1125133, 0.06358858, -75.18516501, -0.00070512, -91.12513303, -0.01845183, -9.1125133, -0.06358858, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24077, 4077, 0.0, 100.09481303, 0.01721445, 100.09481303, 0.05164334, 70.06636912, -2483.57714374, 0.05, 2, 0, 73004, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44077, 25.02370326, 3.897e-05, 75.07110977, 0.00011692, 250.23703258, 0.00038974, -25.02370326, -3.897e-05, -75.07110977, -0.00011692, -250.23703258, -0.00038974, 0.4, 0.3, 0.003, 0.0, 0.0, 24077, 2)
    ops.limitCurve('ThreePoint', 14077, 4077, 0.0, 142.35615678, 0.01410238, 142.35615678, 0.04230715, 99.64930975, -3697.49133253, 0.05, 2, 0, 73004, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34077, 35.5890392, 5.543e-05, 106.76711759, 0.00016629, 355.89039196, 0.00055429, -35.5890392, -5.543e-05, -106.76711759, -0.00016629, -355.89039196, -0.00055429, 0.4, 0.3, 0.003, 0.0, 0.0, 14077, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4077, 99999, 'P', 44077, 'Vy', 34077, 'Vz', 24077, 'My', 14077, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4077, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4077, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 13.35, 0.0, 10.2)
    ops.node(124004, 13.35, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 174031, 124004, 0.0875, 30502924.87761529, 12709552.03233971, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 47.23358894, 0.00082824, 57.1586373, 0.0167495, 5.71586373, 0.05655341, -47.23358894, -0.00082824, -57.1586373, -0.0167495, -5.71586373, -0.05655341, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 69.40101845, 0.00068407, 83.98404039, 0.01834774, 8.39840404, 0.06927093, -69.40101845, -0.00068407, -83.98404039, -0.01834774, -8.39840404, -0.06927093, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 96.88488428, 0.01656489, 96.88488428, 0.04969467, 67.819419, -2577.0304475, 0.05, 2, 0, 74031, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 24.22122107, 3.528e-05, 72.66366321, 0.00010585, 242.21221071, 0.00035284, -24.22122107, -3.528e-05, -72.66366321, -0.00010585, -242.21221071, -0.00035284, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 141.95052645, 0.01368147, 141.95052645, 0.04104441, 99.36536852, -4075.96456287, 0.05, 2, 0, 74031, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 35.48763161, 5.17e-05, 106.46289484, 0.00015509, 354.87631613, 0.00051696, -35.48763161, -5.17e-05, -106.46289484, -0.00015509, -354.87631613, -0.00051696, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.35, 0.0, 8.925)
    ops.node(124032, 16.35, 0.0, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 173005, 124032, 0.0875, 30093328.57870268, 12538886.90779278, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 50.90731769, 0.00083713, 61.51585009, 0.01697191, 6.15158501, 0.05372826, -50.90731769, -0.00083713, -61.51585009, -0.01697191, -6.15158501, -0.05372826, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 74.61474113, 0.00068851, 90.16364323, 0.01858907, 9.01636432, 0.06561334, -74.61474113, -0.00068851, -90.16364323, -0.01858907, -9.01636432, -0.06561334, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 106.39097202, 0.01674265, 106.39097202, 0.05022795, 74.47368041, -2488.87390031, 0.05, 2, 0, 73005, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 26.597743, 3.927e-05, 79.79322901, 0.00011782, 265.97743005, 0.00039273, -26.597743, -3.927e-05, -79.79322901, -0.00011782, -265.97743005, -0.00039273, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 149.25769863, 0.01377011, 149.25769863, 0.04131032, 104.48038904, -3706.54004727, 0.05, 2, 0, 73005, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 37.31442466, 5.51e-05, 111.94327397, 0.00016529, 373.14424658, 0.00055097, -37.31442466, -5.51e-05, -111.94327397, -0.00016529, -373.14424658, -0.00055097, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 16.35, 0.0, 10.2)
    ops.node(124005, 16.35, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 174032, 124005, 0.0875, 30243504.65360117, 12601460.27233382, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 46.35575098, 0.00081555, 56.13338016, 0.01751991, 5.61333802, 0.05717374, -46.35575098, -0.00081555, -56.13338016, -0.01751991, -5.61333802, -0.05717374, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 68.11349443, 0.00067493, 82.48039556, 0.01920741, 8.24803956, 0.06993858, -68.11349443, -0.00067493, -82.48039556, -0.01920741, -8.24803956, -0.06993858, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 102.3578713, 0.01631091, 102.3578713, 0.04893274, 71.65050991, -2782.91678425, 0.05, 2, 0, 74032, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 25.58946783, 3.76e-05, 76.76840348, 0.00011279, 255.89467825, 0.00037596, -25.58946783, -3.76e-05, -76.76840348, -0.00011279, -255.89467825, -0.00037596, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 143.73139244, 0.01349851, 143.73139244, 0.04049553, 100.61197471, -4439.25545123, 0.05, 2, 0, 74032, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 35.93284811, 5.279e-05, 107.79854433, 0.00015838, 359.3284811, 0.00052793, -35.93284811, -5.279e-05, -107.79854433, -0.00015838, -359.3284811, -0.00052793, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 4080, '-orient', 0, 0, 1, 0, 1, 0)
