import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 7.65, 0.0, 0.0)
    ops.node(121003, 7.65, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.1225, 27740401.98307873, 11558500.8262828, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 185.72507696, 0.00096555, 218.49578376, 0.00776036, 21.84957838, 0.02144014, -185.72507696, -0.00096555, -218.49578376, -0.00776036, -21.84957838, -0.02144014, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 200.28398879, 0.00096555, 235.62357772, 0.00776036, 23.56235777, 0.02144014, -200.28398879, -0.00096555, -235.62357772, -0.00776036, -23.56235777, -0.02144014, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 161.10300393, 0.01931098, 161.10300393, 0.05793293, 112.77210275, -2108.25591449, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 40.27575098, 0.00010411, 120.82725295, 0.00031233, 402.75750983, 0.00104109, -40.27575098, -0.00010411, -120.82725295, -0.00031233, -402.75750983, -0.00104109, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 161.10300393, 0.01931098, 161.10300393, 0.05793293, 112.77210275, -2108.25591449, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 40.27575098, 0.00010411, 120.82725295, 0.00031233, 402.75750983, 0.00104109, -40.27575098, -0.00010411, -120.82725295, -0.00031233, -402.75750983, -0.00104109, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.3, 0.0, 0.0)
    ops.node(121004, 12.3, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.0625, 31407283.37034314, 13086368.07097631, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 76.2415878, 0.00131964, 89.56511686, 0.00857226, 8.95651169, 0.03499413, -76.2415878, -0.00131964, -89.56511686, -0.00857226, -8.95651169, -0.03499413, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 80.66697303, 0.00131964, 94.76385624, 0.00857226, 9.47638562, 0.03499413, -80.66697303, -0.00131964, -94.76385624, -0.00857226, -9.47638562, -0.03499413, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 102.70898391, 0.02639286, 102.70898391, 0.07917857, 71.89628874, -1420.35934298, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 25.67724598, 0.0001149, 77.03173793, 0.00034471, 256.77245978, 0.00114903, -25.67724598, -0.0001149, -77.03173793, -0.00034471, -256.77245978, -0.00114903, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 102.70898391, 0.02639286, 102.70898391, 0.07917857, 71.89628874, -1420.35934298, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 25.67724598, 0.0001149, 77.03173793, 0.00034471, 256.77245978, 0.00114903, -25.67724598, -0.0001149, -77.03173793, -0.00034471, -256.77245978, -0.00114903, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 5.2, 0.0)
    ops.node(121005, 0.0, 5.2, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.0625, 30869879.35122587, 12862449.72967745, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 82.36672805, 0.00140392, 96.58760195, 0.00824488, 9.65876019, 0.03203671, -82.36672805, -0.00140392, -96.58760195, -0.00824488, -9.65876019, -0.03203671, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 78.29665262, 0.00140392, 91.81481523, 0.00824488, 9.18148152, 0.03203671, -78.29665262, -0.00140392, -91.81481523, -0.00824488, -9.18148152, -0.03203671, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 103.54363703, 0.02807849, 103.54363703, 0.08423546, 72.48054592, -1483.90966686, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 25.88590926, 0.00011785, 77.65772777, 0.00035356, 258.85909257, 0.00117853, -25.88590926, -0.00011785, -77.65772777, -0.00035356, -258.85909257, -0.00117853, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 103.54363703, 0.02807849, 103.54363703, 0.08423546, 72.48054592, -1483.90966686, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 25.88590926, 0.00011785, 77.65772777, 0.00035356, 258.85909257, 0.00117853, -25.88590926, -0.00011785, -77.65772777, -0.00035356, -258.85909257, -0.00117853, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 3.0, 5.2, 0.0)
    ops.node(121006, 3.0, 5.2, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.16, 30799367.16867132, 12833069.65361305, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 309.6582828, 0.00089196, 366.75573972, 0.00945798, 36.67557397, 0.02913531, -309.6582828, -0.00089196, -366.75573972, -0.00945798, -36.67557397, -0.02913531, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 318.04229689, 0.00089196, 376.68567043, 0.00945798, 37.66856704, 0.02913531, -318.04229689, -0.00089196, -376.68567043, -0.00945798, -37.66856704, -0.02913531, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 215.77225422, 0.01783922, 215.77225422, 0.05351766, 151.04057795, -2466.23809401, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 53.94306355, 9.615e-05, 161.82919066, 0.00028846, 539.43063554, 0.00096154, -53.94306355, -9.615e-05, -161.82919066, -0.00028846, -539.43063554, -0.00096154, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 215.77225422, 0.01783922, 215.77225422, 0.05351766, 151.04057795, -2466.23809401, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 53.94306355, 9.615e-05, 161.82919066, 0.00028846, 539.43063554, 0.00096154, -53.94306355, -9.615e-05, -161.82919066, -0.00028846, -539.43063554, -0.00096154, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 7.65, 5.2, 0.0)
    ops.node(121007, 7.65, 5.2, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.2025, 30362611.69571528, 12651088.20654804, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 458.58236746, 0.00082292, 543.50631565, 0.01306201, 54.35063157, 0.03320689, -458.58236746, -0.00082292, -543.50631565, -0.01306201, -54.35063157, -0.03320689, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 476.29741854, 0.00082292, 564.50198149, 0.01306201, 56.45019815, 0.03320689, -476.29741854, -0.00082292, -564.50198149, -0.01306201, -56.45019815, -0.03320689, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 276.17001732, 0.01645832, 276.17001732, 0.04937497, 193.31901212, -3234.57851989, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 69.04250433, 9.864e-05, 207.12751299, 0.00029591, 690.4250433, 0.00098638, -69.04250433, -9.864e-05, -207.12751299, -0.00029591, -690.4250433, -0.00098638, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 276.17001732, 0.01645832, 276.17001732, 0.04937497, 193.31901212, -3234.57851989, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 69.04250433, 9.864e-05, 207.12751299, 0.00029591, 690.4250433, 0.00098638, -69.04250433, -9.864e-05, -207.12751299, -0.00029591, -690.4250433, -0.00098638, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 12.3, 5.2, 0.0)
    ops.node(121008, 12.3, 5.2, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.1225, 29667241.18818079, 12361350.49507533, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 204.11332177, 0.0009774, 240.69754483, 0.00782986, 24.06975448, 0.02731826, -204.11332177, -0.0009774, -240.69754483, -0.00782986, -24.06975448, -0.02731826, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 211.52096065, 0.0009774, 249.43289084, 0.00782986, 24.94328908, 0.02731826, -211.52096065, -0.0009774, -249.43289084, -0.00782986, -24.94328908, -0.02731826, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 176.33329889, 0.01954794, 176.33329889, 0.05864382, 123.43330922, -2245.33181168, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 44.08332472, 0.00010655, 132.24997417, 0.00031965, 440.83324723, 0.0010655, -44.08332472, -0.00010655, -132.24997417, -0.00031965, -440.83324723, -0.0010655, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 176.33329889, 0.01954794, 176.33329889, 0.05864382, 123.43330922, -2245.33181168, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 44.08332472, 0.00010655, 132.24997417, 0.00031965, 440.83324723, 0.0010655, -44.08332472, -0.00010655, -132.24997417, -0.00031965, -440.83324723, -0.0010655, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 10.4, 0.0)
    ops.node(121009, 0.0, 10.4, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.09, 31745954.51912984, 13227481.04963744, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 127.91064783, 0.00114323, 151.2401339, 0.00960894, 15.12401339, 0.03834313, -127.91064783, -0.00114323, -151.2401339, -0.00960894, -15.12401339, -0.03834313, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 122.50280326, 0.00114323, 144.84595835, 0.00960894, 14.48459584, 0.03834313, -122.50280326, -0.00114323, -144.84595835, -0.00960894, -14.48459584, -0.03834313, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 141.90689145, 0.02286455, 141.90689145, 0.06859365, 99.33482402, -1745.83493279, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 35.47672286, 0.00010907, 106.43016859, 0.00032721, 354.76722863, 0.0010907, -35.47672286, -0.00010907, -106.43016859, -0.00032721, -354.76722863, -0.0010907, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 141.90689145, 0.02286455, 141.90689145, 0.06859365, 99.33482402, -1745.83493279, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 35.47672286, 0.00010907, 106.43016859, 0.00032721, 354.76722863, 0.0010907, -35.47672286, -0.00010907, -106.43016859, -0.00032721, -354.76722863, -0.0010907, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 3.0, 10.4, 0.0)
    ops.node(121010, 3.0, 10.4, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 30205609.85479016, 12585670.77282923, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 314.49551777, 0.00088598, 372.82560378, 0.00988863, 37.28256038, 0.02904249, -314.49551777, -0.00088598, -372.82560378, -0.00988863, -37.28256038, -0.02904249, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 314.49551777, 0.00088598, 372.82560378, 0.00988863, 37.28256038, 0.02904249, -314.49551777, -0.00088598, -372.82560378, -0.00988863, -37.28256038, -0.02904249, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 214.77540516, 0.01771954, 214.77540516, 0.05315861, 150.34278361, -2503.14064237, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 53.69385129, 9.759e-05, 161.08155387, 0.00029277, 536.9385129, 0.00097591, -53.69385129, -9.759e-05, -161.08155387, -0.00029277, -536.9385129, -0.00097591, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 214.77540516, 0.01771954, 214.77540516, 0.05315861, 150.34278361, -2503.14064237, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 53.69385129, 9.759e-05, 161.08155387, 0.00029277, 536.9385129, 0.00097591, -53.69385129, -9.759e-05, -161.08155387, -0.00029277, -536.9385129, -0.00097591, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.65, 10.4, 0.0)
    ops.node(121011, 7.65, 10.4, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 30030246.22341901, 12512602.59309125, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 489.82155369, 0.00080958, 580.55163733, 0.01234737, 58.05516373, 0.031925, -489.82155369, -0.00080958, -580.55163733, -0.01234737, -58.05516373, -0.031925, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 489.82155369, 0.00080958, 580.55163733, 0.01234737, 58.05516373, 0.031925, -489.82155369, -0.00080958, -580.55163733, -0.01234737, -58.05516373, -0.031925, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 266.94838695, 0.01619168, 266.94838695, 0.04857504, 186.86387087, -3100.46208844, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 66.73709674, 9.64e-05, 200.21129021, 0.0002892, 667.37096738, 0.000964, -66.73709674, -9.64e-05, -200.21129021, -0.0002892, -667.37096738, -0.000964, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 266.94838695, 0.01619168, 266.94838695, 0.04857504, 186.86387087, -3100.46208844, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 66.73709674, 9.64e-05, 200.21129021, 0.0002892, 667.37096738, 0.000964, -66.73709674, -9.64e-05, -200.21129021, -0.0002892, -667.37096738, -0.000964, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 12.3, 10.4, 0.0)
    ops.node(121012, 12.3, 10.4, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 31755276.53861723, 13231365.22442385, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 218.2432808, 0.00101622, 257.39524645, 0.00975027, 25.73952465, 0.03350341, -218.2432808, -0.00101622, -257.39524645, -0.00975027, -25.73952465, -0.03350341, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 218.2432808, 0.00101622, 257.39524645, 0.00975027, 25.73952465, 0.03350341, -218.2432808, -0.00101622, -257.39524645, -0.00975027, -25.73952465, -0.03350341, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 195.99579256, 0.0203244, 195.99579256, 0.06097319, 137.19705479, -2450.15871352, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 48.99894814, 0.00011064, 146.99684442, 0.00033193, 489.98948141, 0.00110644, -48.99894814, -0.00011064, -146.99684442, -0.00033193, -489.98948141, -0.00110644, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 195.99579256, 0.0203244, 195.99579256, 0.06097319, 137.19705479, -2450.15871352, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 48.99894814, 0.00011064, 146.99684442, 0.00033193, 489.98948141, 0.00110644, -48.99894814, -0.00011064, -146.99684442, -0.00033193, -489.98948141, -0.00110644, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 15.6, 0.0)
    ops.node(121013, 0.0, 15.6, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0625, 31310018.02162411, 13045840.84234338, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 56.79132253, 0.00122544, 67.41403121, 0.0112249, 6.74140312, 0.04692149, -56.79132253, -0.00122544, -67.41403121, -0.0112249, -6.74140312, -0.04692149, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 56.79132253, 0.00122544, 67.41403121, 0.0112249, 6.74140312, 0.04692149, -56.79132253, -0.00122544, -67.41403121, -0.0112249, -6.74140312, -0.04692149, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 106.30956269, 0.02450876, 106.30956269, 0.07352627, 74.41669388, -1422.63182805, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 26.57739067, 0.0001193, 79.73217202, 0.0003579, 265.77390672, 0.001193, -26.57739067, -0.0001193, -79.73217202, -0.0003579, -265.77390672, -0.001193, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 106.30956269, 0.02450876, 106.30956269, 0.07352627, 74.41669388, -1422.63182805, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 26.57739067, 0.0001193, 79.73217202, 0.0003579, 265.77390672, 0.001193, -26.57739067, -0.0001193, -79.73217202, -0.0003579, -265.77390672, -0.001193, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 3.0, 15.6, 0.0)
    ops.node(121014, 3.0, 15.6, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.09, 29173225.20600023, 12155510.50250009, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 136.51246838, 0.00112303, 160.575553, 0.00944799, 16.0575553, 0.02643902, -136.51246838, -0.00112303, -160.575553, -0.00944799, -16.0575553, -0.02643902, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 130.68725339, 0.00112303, 153.72352601, 0.00944799, 15.3723526, 0.02643902, -130.68725339, -0.00112303, -153.72352601, -0.00944799, -15.3723526, -0.02643902, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 133.49592215, 0.02246053, 133.49592215, 0.06738158, 93.4471455, -1774.0740038, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 33.37398054, 0.00011165, 100.12194161, 0.00033496, 333.73980537, 0.00111654, -33.37398054, -0.00011165, -100.12194161, -0.00033496, -333.73980537, -0.00111654, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 133.49592215, 0.02246053, 133.49592215, 0.06738158, 93.4471455, -1774.0740038, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 33.37398054, 0.00011165, 100.12194161, 0.00033496, 333.73980537, 0.00111654, -33.37398054, -0.00011165, -100.12194161, -0.00033496, -333.73980537, -0.00111654, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.65, 15.6, 0.0)
    ops.node(121015, 7.65, 15.6, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.1225, 31236704.02526855, 13015293.3438619, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 223.68872602, 0.00096889, 263.9860532, 0.00952381, 26.39860532, 0.02971247, -223.68872602, -0.00096889, -263.9860532, -0.00952381, -26.39860532, -0.02971247, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 223.68872602, 0.00096889, 263.9860532, 0.00952381, 26.39860532, 0.02971247, -223.68872602, -0.00096889, -263.9860532, -0.00952381, -26.39860532, -0.02971247, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 180.31738212, 0.0193778, 180.31738212, 0.0581334, 126.22216748, -2181.15561775, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 45.07934553, 0.00010348, 135.23803659, 0.00031045, 450.79345529, 0.00103483, -45.07934553, -0.00010348, -135.23803659, -0.00031045, -450.79345529, -0.00103483, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 180.31738212, 0.0193778, 180.31738212, 0.0581334, 126.22216748, -2181.15561775, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 45.07934553, 0.00010348, 135.23803659, 0.00031045, 450.79345529, 0.00103483, -45.07934553, -0.00010348, -135.23803659, -0.00031045, -450.79345529, -0.00103483, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.3, 15.6, 0.0)
    ops.node(121016, 12.3, 15.6, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.0625, 29536797.98176469, 12306999.15906862, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 84.48193114, 0.00137539, 99.10009415, 0.00900002, 9.91000941, 0.03032795, -84.48193114, -0.00137539, -99.10009415, -0.00900002, -9.91000941, -0.03032795, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 84.48193114, 0.00137539, 99.10009415, 0.00900002, 9.91000941, 0.03032795, -84.48193114, -0.00137539, -99.10009415, -0.00900002, -9.91000941, -0.03032795, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 107.22113349, 0.02750785, 107.22113349, 0.08252356, 75.05479344, -1525.20386721, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 26.80528337, 0.00012755, 80.41585012, 0.00038264, 268.05283373, 0.00127547, -26.80528337, -0.00012755, -80.41585012, -0.00038264, -268.05283373, -0.00127547, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 107.22113349, 0.02750785, 107.22113349, 0.08252356, 75.05479344, -1525.20386721, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 26.80528337, 0.00012755, 80.41585012, 0.00038264, 268.05283373, 0.00127547, -26.80528337, -0.00012755, -80.41585012, -0.00038264, -268.05283373, -0.00127547, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.65, 0.0, 3.3)
    ops.node(122003, 7.65, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.1225, 32686810.6782801, 13619504.44928337, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 153.80942287, 0.00089942, 182.39780203, 0.01028795, 18.2397802, 0.03731777, -153.80942287, -0.00089942, -182.39780203, -0.01028795, -18.2397802, -0.03731777, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 159.73696588, 0.00089942, 189.42709058, 0.01028795, 18.94270906, 0.03731777, -159.73696588, -0.00089942, -189.42709058, -0.01028795, -18.94270906, -0.03731777, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 172.93225792, 0.01798834, 172.93225792, 0.05396503, 121.05258055, -2055.94038771, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 43.23306448, 8.551e-05, 129.69919344, 0.00025654, 432.33064481, 0.00085513, -43.23306448, -8.551e-05, -129.69919344, -0.00025654, -432.33064481, -0.00085513, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 172.93225792, 0.01798834, 172.93225792, 0.05396503, 121.05258055, -2055.94038771, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 43.23306448, 8.551e-05, 129.69919344, 0.00025654, 432.33064481, 0.00085513, -43.23306448, -8.551e-05, -129.69919344, -0.00025654, -432.33064481, -0.00085513, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.3, 0.0, 3.275)
    ops.node(122004, 12.3, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.0625, 33207291.86222024, 13836371.60925843, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 66.70239099, 0.00121071, 78.80954995, 0.01221715, 7.880955, 0.05004896, -66.70239099, -0.00121071, -78.80954995, -0.01221715, -7.880955, -0.05004896, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 72.96509448, 0.00121071, 86.20899751, 0.01221715, 8.62089975, 0.05004896, -72.96509448, -0.00121071, -86.20899751, -0.01221715, -8.62089975, -0.05004896, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 110.53555771, 0.02421429, 110.53555771, 0.07264287, 77.3748904, -1560.44575285, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 27.63388943, 0.00010545, 82.90166828, 0.00031636, 276.33889427, 0.00105452, -27.63388943, -0.00010545, -82.90166828, -0.00031636, -276.33889427, -0.00105452, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 110.53555771, 0.02421429, 110.53555771, 0.07264287, 77.3748904, -1560.44575285, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 27.63388943, 0.00010545, 82.90166828, 0.00031636, 276.33889427, 0.00105452, -27.63388943, -0.00010545, -82.90166828, -0.00031636, -276.33889427, -0.00105452, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 5.2, 3.275)
    ops.node(122005, 0.0, 5.2, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.0625, 31145958.86428956, 12977482.86012065, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 59.49174431, 0.00113788, 70.39266417, 0.00992726, 7.03926642, 0.04184945, -59.49174431, -0.00113788, -70.39266417, -0.00992726, -7.03926642, -0.04184945, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 59.49174431, 0.00113788, 70.39266417, 0.00992726, 7.03926642, 0.04184945, -59.49174431, -0.00113788, -70.39266417, -0.00992726, -7.03926642, -0.04184945, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 102.96522109, 0.02275758, 102.96522109, 0.06827275, 72.07565476, -1483.62013419, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 25.74130527, 0.00010473, 77.22391582, 0.00031419, 257.41305273, 0.00104731, -25.74130527, -0.00010473, -77.22391582, -0.00031419, -257.41305273, -0.00104731, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 102.96522109, 0.02275758, 102.96522109, 0.06827275, 72.07565476, -1483.62013419, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 25.74130527, 0.00010473, 77.22391582, 0.00031419, 257.41305273, 0.00104731, -25.74130527, -0.00010473, -77.22391582, -0.00031419, -257.41305273, -0.00104731, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 3.0, 5.2, 3.3)
    ops.node(122006, 3.0, 5.2, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.16, 33143914.22527458, 13809964.26053108, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 228.4822155, 0.00078562, 271.19802631, 0.0083785, 27.11980263, 0.03503548, -228.4822155, -0.00078562, -271.19802631, -0.0083785, -27.11980263, -0.03503548, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 211.99991047, 0.00078562, 251.63427785, 0.0083785, 25.16342778, 0.03503548, -211.99991047, -0.00078562, -251.63427785, -0.0083785, -25.16342778, -0.03503548, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 207.2629314, 0.0157124, 207.2629314, 0.0471372, 145.08405198, -2199.65517188, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 51.81573285, 7.739e-05, 155.44719855, 0.00023216, 518.15732851, 0.00077386, -51.81573285, -7.739e-05, -155.44719855, -0.00023216, -518.15732851, -0.00077386, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 207.2629314, 0.0157124, 207.2629314, 0.0471372, 145.08405198, -2199.65517188, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 51.81573285, 7.739e-05, 155.44719855, 0.00023216, 518.15732851, 0.00077386, -51.81573285, -7.739e-05, -155.44719855, -0.00023216, -518.15732851, -0.00077386, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 7.65, 5.2, 3.3)
    ops.node(122007, 7.65, 5.2, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.2025, 28648574.50466887, 11936906.04361203, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 312.44216308, 0.00072961, 372.85424283, 0.00877242, 37.28542428, 0.02471063, -312.44216308, -0.00072961, -372.85424283, -0.00877242, -37.28542428, -0.02471063, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 296.94316389, 0.00072961, 354.35844332, 0.00877242, 35.43584433, 0.02471063, -296.94316389, -0.00072961, -354.35844332, -0.00877242, -35.43584433, -0.02471063, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 228.29505497, 0.01459219, 228.29505497, 0.04377658, 159.80653848, -2538.92296352, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 57.07376374, 7.792e-05, 171.22129123, 0.00023375, 570.73763743, 0.00077917, -57.07376374, -7.792e-05, -171.22129123, -0.00023375, -570.73763743, -0.00077917, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 228.29505497, 0.01459219, 228.29505497, 0.04377658, 159.80653848, -2538.92296352, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 57.07376374, 7.792e-05, 171.22129123, 0.00023375, 570.73763743, 0.00077917, -57.07376374, -7.792e-05, -171.22129123, -0.00023375, -570.73763743, -0.00077917, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 12.3, 5.2, 3.275)
    ops.node(122008, 12.3, 5.2, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.1225, 31197573.65977765, 12998989.02490735, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 155.39778989, 0.00086638, 184.62699482, 0.0096719, 18.46269948, 0.03766397, -155.39778989, -0.00086638, -184.62699482, -0.0096719, -18.46269948, -0.03766397, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 141.79062558, 0.00086638, 168.46042092, 0.0096719, 16.84604209, 0.03766397, -141.79062558, -0.00086638, -168.46042092, -0.0096719, -16.84604209, -0.03766397, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 176.26969375, 0.01732754, 176.26969375, 0.05198261, 123.38878563, -2285.44398712, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 44.06742344, 9.132e-05, 132.20227032, 0.00027397, 440.67423438, 0.00091324, -44.06742344, -9.132e-05, -132.20227032, -0.00027397, -440.67423438, -0.00091324, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 176.26969375, 0.01732754, 176.26969375, 0.05198261, 123.38878563, -2285.44398712, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 44.06742344, 9.132e-05, 132.20227032, 0.00027397, 440.67423438, 0.00091324, -44.06742344, -9.132e-05, -132.20227032, -0.00027397, -440.67423438, -0.00091324, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 10.4, 3.275)
    ops.node(122009, 0.0, 10.4, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.09, 28469704.83172237, 11862377.01321765, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 90.07137269, 0.00095851, 107.39734761, 0.00858148, 10.73973476, 0.0361794, -90.07137269, -0.00095851, -107.39734761, -0.00858148, -10.73973476, -0.0361794, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 84.76283387, 0.00095851, 101.06766736, 0.00858148, 10.10676674, 0.0361794, -84.76283387, -0.00095851, -101.06766736, -0.00858148, -10.10676674, -0.0361794, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 118.56372318, 0.01917017, 118.56372318, 0.0575105, 82.99460622, -1620.75923644, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 29.64093079, 9.162e-05, 88.92279238, 0.00027486, 296.40930794, 0.0009162, -29.64093079, -9.162e-05, -88.92279238, -0.00027486, -296.40930794, -0.0009162, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 118.56372318, 0.01917017, 118.56372318, 0.0575105, 82.99460622, -1620.75923644, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 29.64093079, 9.162e-05, 88.92279238, 0.00027486, 296.40930794, 0.0009162, -29.64093079, -9.162e-05, -88.92279238, -0.00027486, -296.40930794, -0.0009162, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 3.0, 10.4, 3.3)
    ops.node(122010, 3.0, 10.4, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 30835971.22915247, 12848321.34548019, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 217.08244242, 0.00076782, 258.78708303, 0.00912849, 25.8787083, 0.03309607, -217.08244242, -0.00076782, -258.78708303, -0.00912849, -25.8787083, -0.03309607, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 201.64894314, 0.00076782, 240.38858789, 0.00912849, 24.03885879, 0.03309607, -201.64894314, -0.00076782, -240.38858789, -0.00912849, -24.03885879, -0.03309607, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 193.71129218, 0.01535637, 193.71129218, 0.0460691, 135.59790452, -2179.32824486, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 48.42782304, 7.774e-05, 145.28346913, 0.00023322, 484.27823044, 0.0007774, -48.42782304, -7.774e-05, -145.28346913, -0.00023322, -484.27823044, -0.0007774, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 193.71129218, 0.01535637, 193.71129218, 0.0460691, 135.59790452, -2179.32824486, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 48.42782304, 7.774e-05, 145.28346913, 0.00023322, 484.27823044, 0.0007774, -48.42782304, -7.774e-05, -145.28346913, -0.00023322, -484.27823044, -0.0007774, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.65, 10.4, 3.3)
    ops.node(122011, 7.65, 10.4, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 28831162.20095946, 12012984.25039978, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 310.6661671, 0.00076196, 370.73799335, 0.00715599, 37.07379934, 0.02333122, -310.6661671, -0.00076196, -370.73799335, -0.00715599, -37.07379934, -0.02333122, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 296.39830282, 0.00076196, 353.71122979, 0.00715599, 35.37112298, 0.02333122, -296.39830282, -0.00076196, -353.71122979, -0.00715599, -35.37112298, -0.02333122, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 221.30181207, 0.0152391, 221.30181207, 0.04571731, 154.91126845, -2366.60472425, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 55.32545302, 7.505e-05, 165.97635905, 0.00022516, 553.25453018, 0.00075052, -55.32545302, -7.505e-05, -165.97635905, -0.00022516, -553.25453018, -0.00075052, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 221.30181207, 0.0152391, 221.30181207, 0.04571731, 154.91126845, -2366.60472425, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 55.32545302, 7.505e-05, 165.97635905, 0.00022516, 553.25453018, 0.00075052, -55.32545302, -7.505e-05, -165.97635905, -0.00022516, -553.25453018, -0.00075052, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 12.3, 10.4, 3.275)
    ops.node(122012, 12.3, 10.4, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 29112165.54338898, 12130068.97641208, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 155.99479314, 0.00089545, 185.50041628, 0.00772727, 18.55004163, 0.03160171, -155.99479314, -0.00089545, -185.50041628, -0.00772727, -18.55004163, -0.03160171, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 142.13466912, 0.00089545, 169.01872017, 0.00772727, 16.90187202, 0.03160171, -142.13466912, -0.00089545, -169.01872017, -0.00772727, -16.90187202, -0.03160171, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 158.82900416, 0.01790898, 158.82900416, 0.05372693, 111.18030291, -2082.51876738, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 39.70725104, 8.818e-05, 119.12175312, 0.00026455, 397.07251039, 0.00088183, -39.70725104, -8.818e-05, -119.12175312, -0.00026455, -397.07251039, -0.00088183, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 158.82900416, 0.01790898, 158.82900416, 0.05372693, 111.18030291, -2082.51876738, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 39.70725104, 8.818e-05, 119.12175312, 0.00026455, 397.07251039, 0.00088183, -39.70725104, -8.818e-05, -119.12175312, -0.00026455, -397.07251039, -0.00088183, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 15.6, 3.275)
    ops.node(122013, 0.0, 15.6, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0625, 31634465.25138603, 13181027.18807751, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 48.17601683, 0.00103777, 57.48243686, 0.01172628, 5.74824369, 0.0546917, -48.17601683, -0.00103777, -57.48243686, -0.01172628, -5.74824369, -0.0546917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 48.17601683, 0.00103777, 57.48243686, 0.01172628, 5.74824369, 0.0546917, -48.17601683, -0.00103777, -57.48243686, -0.01172628, -5.74824369, -0.0546917, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 98.09763903, 0.02075547, 98.09763903, 0.06226642, 68.66834732, -1410.44431393, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 24.52440976, 9.824e-05, 73.57322927, 0.00029472, 245.24409756, 0.00098239, -24.52440976, -9.824e-05, -73.57322927, -0.00029472, -245.24409756, -0.00098239, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 98.09763903, 0.02075547, 98.09763903, 0.06226642, 68.66834732, -1410.44431393, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 24.52440976, 9.824e-05, 73.57322927, 0.00029472, 245.24409756, 0.00098239, -24.52440976, -9.824e-05, -73.57322927, -0.00029472, -245.24409756, -0.00098239, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 3.0, 15.6, 3.3)
    ops.node(122014, 3.0, 15.6, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.09, 29797622.31469679, 12415675.96445699, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 113.68561408, 0.00104224, 134.99660656, 0.00902731, 13.49966066, 0.03277487, -113.68561408, -0.00104224, -134.99660656, -0.00902731, -13.49966066, -0.03277487, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 119.07384813, 0.00104224, 141.39489467, 0.00902731, 14.13948947, 0.03277487, -119.07384813, -0.00104224, -141.39489467, -0.00902731, -14.13948947, -0.03277487, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 119.59866438, 0.02084481, 119.59866438, 0.06253442, 83.71906506, -1598.21574164, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 29.89966609, 8.83e-05, 89.69899828, 0.0002649, 298.99666095, 0.00088301, -29.89966609, -8.83e-05, -89.69899828, -0.0002649, -298.99666095, -0.00088301, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 119.59866438, 0.02084481, 119.59866438, 0.06253442, 83.71906506, -1598.21574164, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 29.89966609, 8.83e-05, 89.69899828, 0.0002649, 298.99666095, 0.00088301, -29.89966609, -8.83e-05, -89.69899828, -0.0002649, -298.99666095, -0.00088301, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.65, 15.6, 3.3)
    ops.node(122015, 7.65, 15.6, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.1225, 28932777.84087041, 12055324.10036267, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 152.84066734, 0.00090557, 181.80745199, 0.00952885, 18.1807452, 0.03037352, -152.84066734, -0.00090557, -181.80745199, -0.00952885, -18.1807452, -0.03037352, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 159.17377309, 0.00090557, 189.3408254, 0.00952885, 18.93408254, 0.03037352, -159.17377309, -0.00090557, -189.3408254, -0.00952885, -18.93408254, -0.03037352, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 155.48906374, 0.01811144, 155.48906374, 0.05433433, 108.84234462, -2021.61403223, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 38.87226593, 8.686e-05, 116.6167978, 0.00026059, 388.72265934, 0.00086864, -38.87226593, -8.686e-05, -116.6167978, -0.00026059, -388.72265934, -0.00086864, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 155.48906374, 0.01811144, 155.48906374, 0.05433433, 108.84234462, -2021.61403223, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 38.87226593, 8.686e-05, 116.6167978, 0.00026059, 388.72265934, 0.00086864, -38.87226593, -8.686e-05, -116.6167978, -0.00026059, -388.72265934, -0.00086864, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.3, 15.6, 3.275)
    ops.node(122016, 12.3, 15.6, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.0625, 29763467.94681929, 12401444.97784137, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 68.16102628, 0.0012571, 80.77033878, 0.00913647, 8.07703388, 0.03855949, -68.16102628, -0.0012571, -80.77033878, -0.00913647, -8.07703388, -0.03855949, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 75.51827919, 0.0012571, 89.48863196, 0.00913647, 8.9488632, 0.03855949, -75.51827919, -0.0012571, -89.48863196, -0.00913647, -8.9488632, -0.03855949, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 88.86358146, 0.02514191, 88.86358146, 0.07542573, 62.20450702, -1388.42629877, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 22.21589536, 9.459e-05, 66.64768609, 0.00028376, 222.15895365, 0.00094586, -22.21589536, -9.459e-05, -66.64768609, -0.00028376, -222.15895365, -0.00094586, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 88.86358146, 0.02514191, 88.86358146, 0.07542573, 62.20450702, -1388.42629877, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 22.21589536, 9.459e-05, 66.64768609, 0.00028376, 222.15895365, 0.00094586, -22.21589536, -9.459e-05, -66.64768609, -0.00028376, -222.15895365, -0.00094586, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.65, 0.0, 6.05)
    ops.node(123003, 7.65, 0.0, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0625, 30459682.73689429, 12691534.47370596, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 75.73009615, 0.00126921, 89.47203304, 0.00890897, 8.9472033, 0.03373045, -75.73009615, -0.00126921, -89.47203304, -0.00890897, -8.9472033, -0.03373045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 75.73009615, 0.00126921, 89.47203304, 0.00890897, 8.9472033, 0.03373045, -75.73009615, -0.00126921, -89.47203304, -0.00890897, -8.9472033, -0.03373045, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 69.01746109, 0.02538421, 69.01746109, 0.07615262, 48.31222276, -1307.35814193, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 17.25436527, 7.178e-05, 51.76309582, 0.00021535, 172.54365273, 0.00071783, -17.25436527, -7.178e-05, -51.76309582, -0.00021535, -172.54365273, -0.00071783, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 69.01746109, 0.02538421, 69.01746109, 0.07615262, 48.31222276, -1307.35814193, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 17.25436527, 7.178e-05, 51.76309582, 0.00021535, 172.54365273, 0.00071783, -17.25436527, -7.178e-05, -51.76309582, -0.00021535, -172.54365273, -0.00071783, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.3, 0.0, 6.025)
    ops.node(123004, 12.3, 0.0, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 31022146.02594959, 12925894.177479, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 50.86536981, 0.00112794, 60.77023335, 0.01248015, 6.07702333, 0.05456255, -50.86536981, -0.00112794, -60.77023335, -0.01248015, -6.07702333, -0.05456255, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 54.32046411, 0.00112794, 64.89812798, 0.01248015, 6.4898128, 0.05456255, -54.32046411, -0.00112794, -64.89812798, -0.01248015, -6.4898128, -0.05456255, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 96.50685712, 0.02255875, 96.50685712, 0.06767626, 67.55479999, -1408.00177669, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 24.12671428, 9.855e-05, 72.38014284, 0.00029566, 241.26714281, 0.00098553, -24.12671428, -9.855e-05, -72.38014284, -0.00029566, -241.26714281, -0.00098553, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 96.50685712, 0.02255875, 96.50685712, 0.06767626, 67.55479999, -1408.00177669, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 24.12671428, 9.855e-05, 72.38014284, 0.00029566, 241.26714281, 0.00098553, -24.12671428, -9.855e-05, -72.38014284, -0.00029566, -241.26714281, -0.00098553, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 5.2, 6.025)
    ops.node(123005, 0.0, 5.2, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 29648948.29106077, 12353728.45460865, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 46.14389994, 0.00104114, 55.17239364, 0.01021585, 5.51723936, 0.04827223, -46.14389994, -0.00104114, -55.17239364, -0.01021585, -5.51723936, -0.04827223, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 46.14389994, 0.00104114, 55.17239364, 0.01021585, 5.51723936, 0.04827223, -46.14389994, -0.00104114, -55.17239364, -0.01021585, -5.51723936, -0.04827223, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 83.75417362, 0.02082286, 83.75417362, 0.06246858, 58.62792154, -1214.72681793, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 20.93854341, 8.949e-05, 62.81563022, 0.00026847, 209.38543406, 0.00089492, -20.93854341, -8.949e-05, -62.81563022, -0.00026847, -209.38543406, -0.00089492, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 83.75417362, 0.02082286, 83.75417362, 0.06246858, 58.62792154, -1214.72681793, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 20.93854341, 8.949e-05, 62.81563022, 0.00026847, 209.38543406, 0.00089492, -20.93854341, -8.949e-05, -62.81563022, -0.00026847, -209.38543406, -0.00089492, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 3.0, 5.2, 6.05)
    ops.node(123006, 3.0, 5.2, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1225, 31852761.18597458, 13271983.82748941, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 142.75397622, 0.00084121, 170.1805877, 0.01115606, 17.01805877, 0.04014553, -142.75397622, -0.00084121, -170.1805877, -0.01115606, -17.01805877, -0.04014553, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 136.48202725, 0.00084121, 162.70364037, 0.01115606, 16.27036404, 0.04014553, -136.48202725, -0.00084121, -162.70364037, -0.01115606, -16.27036404, -0.04014553, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 161.82682946, 0.01682428, 161.82682946, 0.05047285, 113.27878062, -1888.56354122, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 40.45670737, 8.212e-05, 121.3701221, 0.00024635, 404.56707366, 0.00082117, -40.45670737, -8.212e-05, -121.3701221, -0.00024635, -404.56707366, -0.00082117, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 161.82682946, 0.01682428, 161.82682946, 0.05047285, 113.27878062, -1888.56354122, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 40.45670737, 8.212e-05, 121.3701221, 0.00024635, 404.56707366, 0.00082117, -40.45670737, -8.212e-05, -121.3701221, -0.00024635, -404.56707366, -0.00082117, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 7.65, 5.2, 6.05)
    ops.node(123007, 7.65, 5.2, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 31093670.5558692, 12955696.0649455, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 173.42377818, 0.00088913, 206.14258595, 0.00813083, 20.61425859, 0.02851427, -173.42377818, -0.00088913, -206.14258595, -0.00813083, -20.61425859, -0.02851427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 173.42377818, 0.00088913, 206.14258595, 0.00813083, 20.61425859, 0.02851427, -173.42377818, -0.00088913, -206.14258595, -0.00813083, -20.61425859, -0.02851427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 138.9193571, 0.01778265, 138.9193571, 0.05334794, 97.24354997, -1717.47121365, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 34.72983928, 7.221e-05, 104.18951783, 0.00021664, 347.29839276, 0.00072214, -34.72983928, -7.221e-05, -104.18951783, -0.00021664, -347.29839276, -0.00072214, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 138.9193571, 0.01778265, 138.9193571, 0.05334794, 97.24354997, -1717.47121365, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 34.72983928, 7.221e-05, 104.18951783, 0.00021664, 347.29839276, 0.00072214, -34.72983928, -7.221e-05, -104.18951783, -0.00021664, -347.29839276, -0.00072214, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 12.3, 5.2, 6.025)
    ops.node(123008, 12.3, 5.2, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 31197529.69108484, 12998970.70461868, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 64.67758705, 0.00117985, 76.38451395, 0.00939763, 7.6384514, 0.03972429, -64.67758705, -0.00117985, -76.38451395, -0.00939763, -7.6384514, -0.03972429, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 64.67758705, 0.00117985, 76.38451395, 0.00939763, 7.6384514, 0.03972429, -64.67758705, -0.00117985, -76.38451395, -0.00939763, -7.6384514, -0.03972429, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 105.41980778, 0.0235971, 105.41980778, 0.07079129, 73.79386544, -1540.78765744, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 26.35495194, 0.00010705, 79.06485583, 0.00032115, 263.54951944, 0.0010705, -26.35495194, -0.00010705, -79.06485583, -0.00032115, -263.54951944, -0.0010705, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 105.41980778, 0.0235971, 105.41980778, 0.07079129, 73.79386544, -1540.78765744, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 26.35495194, 0.00010705, 79.06485583, 0.00032115, 263.54951944, 0.0010705, -26.35495194, -0.00010705, -79.06485583, -0.00032115, -263.54951944, -0.0010705, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 10.4, 6.025)
    ops.node(123009, 0.0, 10.4, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 30639979.47479929, 12766658.1144997, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 49.207896, 0.00112268, 58.71226931, 0.01039329, 5.87122693, 0.04942641, -49.207896, -0.00112268, -58.71226931, -0.01039329, -5.87122693, -0.04942641, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 49.207896, 0.00112268, 58.71226931, 0.01039329, 5.87122693, 0.04942641, -49.207896, -0.00112268, -58.71226931, -0.01039329, -5.87122693, -0.04942641, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 94.10582262, 0.02245352, 94.10582262, 0.06736055, 65.87407583, -1328.56297056, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 23.52645565, 9.73e-05, 70.57936696, 0.0002919, 235.26455654, 0.000973, -23.52645565, -9.73e-05, -70.57936696, -0.0002919, -235.26455654, -0.000973, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 94.10582262, 0.02245352, 94.10582262, 0.06736055, 65.87407583, -1328.56297056, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 23.52645565, 9.73e-05, 70.57936696, 0.0002919, 235.26455654, 0.000973, -23.52645565, -9.73e-05, -70.57936696, -0.0002919, -235.26455654, -0.000973, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 3.0, 10.4, 6.05)
    ops.node(123010, 3.0, 10.4, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 32743280.02781167, 13643033.34492153, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 145.58614264, 0.00084131, 173.28012827, 0.00933367, 17.32801283, 0.03966823, -145.58614264, -0.00084131, -173.28012827, -0.00933367, -17.32801283, -0.03966823, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 138.88038038, 0.00084131, 165.29876876, 0.00933367, 16.52987688, 0.03966823, -138.88038038, -0.00084131, -165.29876876, -0.00933367, -16.52987688, -0.03966823, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 157.75837303, 0.01682618, 157.75837303, 0.05047854, 110.43086112, -1701.79465265, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 39.43959326, 7.788e-05, 118.31877977, 0.00023363, 394.39593258, 0.00077875, -39.43959326, -7.788e-05, -118.31877977, -0.00023363, -394.39593258, -0.00077875, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 157.75837303, 0.01682618, 157.75837303, 0.05047854, 110.43086112, -1701.79465265, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 39.43959326, 7.788e-05, 118.31877977, 0.00023363, 394.39593258, 0.00077875, -39.43959326, -7.788e-05, -118.31877977, -0.00023363, -394.39593258, -0.00077875, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.65, 10.4, 6.05)
    ops.node(123011, 7.65, 10.4, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 31552901.56802548, 13147042.32001062, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 178.95779864, 0.00088632, 212.60966348, 0.00752341, 21.26096635, 0.0285077, -178.95779864, -0.00088632, -212.60966348, -0.00752341, -21.26096635, -0.0285077, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 178.95779864, 0.00088632, 212.60966348, 0.00752341, 21.26096635, 0.0285077, -178.95779864, -0.00088632, -212.60966348, -0.00752341, -21.26096635, -0.0285077, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 132.60886783, 0.01772638, 132.60886783, 0.05317915, 92.82620748, -1670.48897548, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 33.15221696, 6.793e-05, 99.45665087, 0.00020379, 331.52216958, 0.0006793, -33.15221696, -6.793e-05, -99.45665087, -0.00020379, -331.52216958, -0.0006793, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 132.60886783, 0.01772638, 132.60886783, 0.05317915, 92.82620748, -1670.48897548, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 33.15221696, 6.793e-05, 99.45665087, 0.00020379, 331.52216958, 0.0006793, -33.15221696, -6.793e-05, -99.45665087, -0.00020379, -331.52216958, -0.0006793, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 12.3, 10.4, 6.025)
    ops.node(123012, 12.3, 10.4, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 29383932.72866164, 12243305.30360902, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 63.32929671, 0.00128733, 74.76215925, 0.00896256, 7.47621593, 0.03442143, -63.32929671, -0.00128733, -74.76215925, -0.00896256, -7.47621593, -0.03442143, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 63.32929671, 0.00128733, 74.76215925, 0.00896256, 7.47621593, 0.03442143, -63.32929671, -0.00128733, -74.76215925, -0.00896256, -7.47621593, -0.03442143, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 100.14484222, 0.02574656, 100.14484222, 0.07723968, 70.10138955, -1512.56299326, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 25.03621055, 0.00010797, 75.10863166, 0.00032391, 250.36210554, 0.0010797, -25.03621055, -0.00010797, -75.10863166, -0.00032391, -250.36210554, -0.0010797, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 100.14484222, 0.02574656, 100.14484222, 0.07723968, 70.10138955, -1512.56299326, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 25.03621055, 0.00010797, 75.10863166, 0.00032391, 250.36210554, 0.0010797, -25.03621055, -0.00010797, -75.10863166, -0.00032391, -250.36210554, -0.0010797, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 15.6, 6.025)
    ops.node(123013, 0.0, 15.6, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 32173567.68366997, 13405653.20152915, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 38.71845128, 0.00103781, 46.38824546, 0.01301771, 4.63882455, 0.0643144, -38.71845128, -0.00103781, -46.38824546, -0.01301771, -4.63882455, -0.0643144, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 38.71845128, 0.00103781, 46.38824546, 0.01301771, 4.63882455, 0.0643144, -38.71845128, -0.00103781, -46.38824546, -0.01301771, -4.63882455, -0.0643144, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 95.96152725, 0.02075626, 95.96152725, 0.06226878, 67.17306908, -1540.26147241, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 23.99038181, 9.449e-05, 71.97114544, 0.00028347, 239.90381814, 0.00094489, -23.99038181, -9.449e-05, -71.97114544, -0.00028347, -239.90381814, -0.00094489, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 95.96152725, 0.02075626, 95.96152725, 0.06226878, 67.17306908, -1540.26147241, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 23.99038181, 9.449e-05, 71.97114544, 0.00028347, 239.90381814, 0.00094489, -23.99038181, -9.449e-05, -71.97114544, -0.00028347, -239.90381814, -0.00094489, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 3.0, 15.6, 6.05)
    ops.node(123014, 3.0, 15.6, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 34740952.45671548, 14475396.85696478, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 68.15923878, 0.00113974, 80.41729387, 0.00998058, 8.04172939, 0.04763628, -68.15923878, -0.00113974, -80.41729387, -0.00998058, -8.04172939, -0.04763628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 68.15923878, 0.00113974, 80.41729387, 0.00998058, 8.04172939, 0.04763628, -68.15923878, -0.00113974, -80.41729387, -0.00998058, -8.04172939, -0.04763628, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 74.25684171, 0.02279478, 74.25684171, 0.06838434, 51.9797892, -1142.53981036, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 18.56421043, 6.771e-05, 55.69263128, 0.00020314, 185.64210428, 0.00067714, -18.56421043, -6.771e-05, -55.69263128, -0.00020314, -185.64210428, -0.00067714, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 74.25684171, 0.02279478, 74.25684171, 0.06838434, 51.9797892, -1142.53981036, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 18.56421043, 6.771e-05, 55.69263128, 0.00020314, 185.64210428, 0.00067714, -18.56421043, -6.771e-05, -55.69263128, -0.00020314, -185.64210428, -0.00067714, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.65, 15.6, 6.05)
    ops.node(123015, 7.65, 15.6, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 31173006.9773976, 12988752.907249, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 75.96523297, 0.00123611, 89.73890556, 0.0110717, 8.97389056, 0.03750931, -75.96523297, -0.00123611, -89.73890556, -0.0110717, -8.97389056, -0.03750931, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 75.96523297, 0.00123611, 89.73890556, 0.0110717, 8.97389056, 0.03750931, -75.96523297, -0.00123611, -89.73890556, -0.0110717, -8.97389056, -0.03750931, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 99.43326845, 0.02472219, 99.43326845, 0.07416657, 69.60328792, -1443.65188601, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 24.85831711, 0.00010105, 74.57495134, 0.00030315, 248.58317113, 0.0010105, -24.85831711, -0.00010105, -74.57495134, -0.00030315, -248.58317113, -0.0010105, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 99.43326845, 0.02472219, 99.43326845, 0.07416657, 69.60328792, -1443.65188601, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 24.85831711, 0.00010105, 74.57495134, 0.00030315, 248.58317113, 0.0010105, -24.85831711, -0.00010105, -74.57495134, -0.00030315, -248.58317113, -0.0010105, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.3, 15.6, 6.025)
    ops.node(123016, 12.3, 15.6, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 33548430.65450311, 13978512.77270963, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 50.63403998, 0.00116117, 60.17621819, 0.01064624, 6.01762182, 0.05746383, -50.63403998, -0.00116117, -60.17621819, -0.01064624, -6.01762182, -0.05746383, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 53.56720105, 0.00116117, 63.66214467, 0.01064624, 6.36621447, 0.05746383, -53.56720105, -0.00116117, -63.66214467, -0.01064624, -6.36621447, -0.05746383, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 92.87245438, 0.02322342, 92.87245438, 0.06967027, 65.01071807, -1241.80983193, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 23.21811359, 8.77e-05, 69.65434078, 0.0002631, 232.18113595, 0.000877, -23.21811359, -8.77e-05, -69.65434078, -0.0002631, -232.18113595, -0.000877, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 92.87245438, 0.02322342, 92.87245438, 0.06967027, 65.01071807, -1241.80983193, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 23.21811359, 8.77e-05, 69.65434078, 0.0002631, 232.18113595, 0.000877, -23.21811359, -8.77e-05, -69.65434078, -0.0002631, -232.18113595, -0.000877, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.65, 0.0, 8.8)
    ops.node(124003, 7.65, 0.0, 11.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0625, 30419003.01311731, 12674584.58879888, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 55.26920347, 0.0011206, 66.38923753, 0.01323761, 6.63892375, 0.05376224, -55.26920347, -0.0011206, -66.38923753, -0.01323761, -6.63892375, -0.05376224, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 55.26920347, 0.0011206, 66.38923753, 0.01323761, 6.63892375, 0.05376224, -55.26920347, -0.0011206, -66.38923753, -0.01323761, -6.63892375, -0.05376224, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 79.69197186, 0.02241207, 79.69197186, 0.06723621, 55.7843803, -1153.11175105, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 19.92299296, 8.3e-05, 59.76897889, 0.00024899, 199.22992964, 0.00082996, -19.92299296, -8.3e-05, -59.76897889, -0.00024899, -199.22992964, -0.00082996, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 79.69197186, 0.02241207, 79.69197186, 0.06723621, 55.7843803, -1153.11175105, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 19.92299296, 8.3e-05, 59.76897889, 0.00024899, 199.22992964, 0.00082996, -19.92299296, -8.3e-05, -59.76897889, -0.00024899, -199.22992964, -0.00082996, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.3, 0.0, 8.775)
    ops.node(124004, 12.3, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 31490873.63180486, 13121197.34658536, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 31.76737995, 0.00100071, 38.27642315, 0.01111428, 3.82764231, 0.06780503, -31.76737995, -0.00100071, -38.27642315, -0.01111428, -3.82764231, -0.06780503, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 31.76737995, 0.00100071, 38.27642315, 0.01111428, 3.82764231, 0.06780503, -31.76737995, -0.00100071, -38.27642315, -0.01111428, -3.82764231, -0.06780503, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 72.43175689, 0.02001412, 72.43175689, 0.06004236, 50.70222982, -1233.45007955, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 18.10793922, 7.287e-05, 54.32381767, 0.0002186, 181.07939223, 0.00072867, -18.10793922, -7.287e-05, -54.32381767, -0.0002186, -181.07939223, -0.00072867, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 72.43175689, 0.02001412, 72.43175689, 0.06004236, 50.70222982, -1233.45007955, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 18.10793922, 7.287e-05, 54.32381767, 0.0002186, 181.07939223, 0.00072867, -18.10793922, -7.287e-05, -54.32381767, -0.0002186, -181.07939223, -0.00072867, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 5.2, 8.775)
    ops.node(124005, 0.0, 5.2, 11.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 30833253.78289012, 12847189.07620422, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 30.27222833, 0.00104914, 36.52804733, 0.01219863, 3.65280473, 0.06778162, -30.27222833, -0.00104914, -36.52804733, -0.01219863, -3.65280473, -0.06778162, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 30.27222833, 0.00104914, 36.52804733, 0.01219863, 3.65280473, 0.06778162, -30.27222833, -0.00104914, -36.52804733, -0.01219863, -3.65280473, -0.06778162, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 81.07396282, 0.02098275, 81.07396282, 0.06294826, 56.75177397, -1390.46635973, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 20.2684907, 8.33e-05, 60.80547211, 0.0002499, 202.68490704, 0.000833, -20.2684907, -8.33e-05, -60.80547211, -0.0002499, -202.68490704, -0.000833, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 81.07396282, 0.02098275, 81.07396282, 0.06294826, 56.75177397, -1390.46635973, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 20.2684907, 8.33e-05, 60.80547211, 0.0002499, 202.68490704, 0.000833, -20.2684907, -8.33e-05, -60.80547211, -0.0002499, -202.68490704, -0.000833, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 3.0, 5.2, 8.8)
    ops.node(124006, 3.0, 5.2, 11.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1225, 30876581.74064044, 12865242.39193352, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 105.1576069, 0.00079413, 126.69460061, 0.01180664, 12.66946006, 0.04794063, -105.1576069, -0.00079413, -126.69460061, -0.01180664, -12.66946006, -0.04794063, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 99.27956716, 0.00079413, 119.61269831, 0.01180664, 11.96126983, 0.04794063, -99.27956716, -0.00079413, -119.61269831, -0.01180664, -11.96126983, -0.04794063, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 135.36286174, 0.01588263, 135.36286174, 0.04764788, 94.75400322, -1550.64750803, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 33.84071543, 7.086e-05, 101.5221463, 0.00021258, 338.40715434, 0.0007086, -33.84071543, -7.086e-05, -101.5221463, -0.00021258, -338.40715434, -0.0007086, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 135.36286174, 0.01588263, 135.36286174, 0.04764788, 94.75400322, -1550.64750803, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 33.84071543, 7.086e-05, 101.5221463, 0.00021258, 338.40715434, 0.0007086, -33.84071543, -7.086e-05, -101.5221463, -0.00021258, -338.40715434, -0.0007086, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 7.65, 5.2, 8.8)
    ops.node(124007, 7.65, 5.2, 11.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 32628585.07440268, 13595243.78100112, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 130.97694502, 0.00082493, 156.77374737, 0.00862566, 15.67737474, 0.03791317, -130.97694502, -0.00082493, -156.77374737, -0.00862566, -15.67737474, -0.03791317, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 130.97694502, 0.00082493, 156.77374737, 0.00862566, 15.67737474, 0.03791317, -130.97694502, -0.00082493, -156.77374737, -0.00862566, -15.67737474, -0.03791317, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 114.25316763, 0.01649851, 114.25316763, 0.04949552, 79.97721734, -1168.42788215, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 28.56329191, 5.66e-05, 85.68987572, 0.00016979, 285.63291906, 0.00056598, -28.56329191, -5.66e-05, -85.68987572, -0.00016979, -285.63291906, -0.00056598, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 114.25316763, 0.01649851, 114.25316763, 0.04949552, 79.97721734, -1168.42788215, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 28.56329191, 5.66e-05, 85.68987572, 0.00016979, 285.63291906, 0.00056598, -28.56329191, -5.66e-05, -85.68987572, -0.00016979, -285.63291906, -0.00056598, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 12.3, 5.2, 8.775)
    ops.node(124008, 12.3, 5.2, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 31340563.46419737, 13058568.11008224, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 40.55766125, 0.00105096, 48.63443658, 0.01252069, 4.86344366, 0.06095523, -40.55766125, -0.00105096, -48.63443658, -0.01252069, -4.86344366, -0.06095523, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 40.55766125, 0.00105096, 48.63443658, 0.01252069, 4.86344366, 0.06095523, -40.55766125, -0.00105096, -48.63443658, -0.01252069, -4.86344366, -0.06095523, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 92.58650451, 0.02101922, 92.58650451, 0.06305765, 64.81055316, -1407.26491604, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 23.14662613, 9.359e-05, 69.43987839, 0.00028077, 231.46626128, 0.00093589, -23.14662613, -9.359e-05, -69.43987839, -0.00028077, -231.46626128, -0.00093589, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 92.58650451, 0.02101922, 92.58650451, 0.06305765, 64.81055316, -1407.26491604, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 23.14662613, 9.359e-05, 69.43987839, 0.00028077, 231.46626128, 0.00093589, -23.14662613, -9.359e-05, -69.43987839, -0.00028077, -231.46626128, -0.00093589, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 10.4, 8.775)
    ops.node(124009, 0.0, 10.4, 11.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 34483736.1112569, 14368223.37969038, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 31.62243244, 0.00098564, 37.72311851, 0.0128814, 3.77231185, 0.07133809, -31.62243244, -0.00098564, -37.72311851, -0.0128814, -3.77231185, -0.07133809, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 31.62243244, 0.00098564, 37.72311851, 0.0128814, 3.77231185, 0.07133809, -31.62243244, -0.00098564, -37.72311851, -0.0128814, -3.77231185, -0.07133809, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 91.72967943, 0.01971274, 91.72967943, 0.05913822, 64.2107756, -1506.31068869, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 22.93241986, 8.427e-05, 68.79725957, 0.00025281, 229.32419857, 0.00084272, -22.93241986, -8.427e-05, -68.79725957, -0.00025281, -229.32419857, -0.00084272, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 91.72967943, 0.01971274, 91.72967943, 0.05913822, 64.2107756, -1506.31068869, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 22.93241986, 8.427e-05, 68.79725957, 0.00025281, 229.32419857, 0.00084272, -22.93241986, -8.427e-05, -68.79725957, -0.00025281, -229.32419857, -0.00084272, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 3.0, 10.4, 8.8)
    ops.node(124010, 3.0, 10.4, 11.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 31381350.19339714, 13075562.58058214, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 107.06790833, 0.00079692, 128.81931031, 0.01163584, 12.88193103, 0.04803955, -107.06790833, -0.00079692, -128.81931031, -0.01163584, -12.88193103, -0.04803955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 101.05941081, 0.00079692, 121.59015528, 0.01163584, 12.15901553, 0.04803955, -101.05941081, -0.00079692, -121.59015528, -0.01163584, -12.15901553, -0.04803955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 137.32400147, 0.01593845, 137.32400147, 0.04781534, 96.12680103, -1539.37504735, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 34.33100037, 7.073e-05, 102.99300111, 0.00021219, 343.31000368, 0.0007073, -34.33100037, -7.073e-05, -102.99300111, -0.00021219, -343.31000368, -0.0007073, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 137.32400147, 0.01593845, 137.32400147, 0.04781534, 96.12680103, -1539.37504735, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 34.33100037, 7.073e-05, 102.99300111, 0.00021219, 343.31000368, 0.0007073, -34.33100037, -7.073e-05, -102.99300111, -0.00021219, -343.31000368, -0.0007073, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.65, 10.4, 8.8)
    ops.node(124011, 7.65, 10.4, 11.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 28676680.34297918, 11948616.80957466, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 129.60816339, 0.00084166, 156.35340137, 0.00976864, 15.63534014, 0.03541794, -129.60816339, -0.00084166, -156.35340137, -0.00976864, -15.63534014, -0.03541794, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 129.60816339, 0.00084166, 156.35340137, 0.00976864, 15.63534014, 0.03541794, -129.60816339, -0.00084166, -156.35340137, -0.00976864, -15.63534014, -0.03541794, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 113.05068062, 0.01683311, 113.05068062, 0.05049934, 79.13547643, -1244.67091428, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 28.26267015, 6.372e-05, 84.78801046, 0.00019116, 282.62670154, 0.0006372, -28.26267015, -6.372e-05, -84.78801046, -0.00019116, -282.62670154, -0.0006372, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 113.05068062, 0.01683311, 113.05068062, 0.05049934, 79.13547643, -1244.67091428, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 28.26267015, 6.372e-05, 84.78801046, 0.00019116, 282.62670154, 0.0006372, -28.26267015, -6.372e-05, -84.78801046, -0.00019116, -282.62670154, -0.0006372, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 12.3, 10.4, 8.775)
    ops.node(124012, 12.3, 10.4, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 30540629.80366812, 12725262.41819505, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 38.68506579, 0.00102028, 46.46116748, 0.01276725, 4.64611675, 0.0598112, -38.68506579, -0.00102028, -46.46116748, -0.01276725, -4.64611675, -0.0598112, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 38.68506579, 0.00102028, 46.46116748, 0.01276725, 4.64611675, 0.0598112, -38.68506579, -0.00102028, -46.46116748, -0.01276725, -4.64611675, -0.0598112, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 91.54070843, 0.02040553, 91.54070843, 0.06121659, 64.0784959, -1427.56072976, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 22.88517711, 9.496e-05, 68.65553132, 0.00028487, 228.85177107, 0.00094956, -22.88517711, -9.496e-05, -68.65553132, -0.00028487, -228.85177107, -0.00094956, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 91.54070843, 0.02040553, 91.54070843, 0.06121659, 64.0784959, -1427.56072976, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 22.88517711, 9.496e-05, 68.65553132, 0.00028487, 228.85177107, 0.00094956, -22.88517711, -9.496e-05, -68.65553132, -0.00028487, -228.85177107, -0.00094956, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 15.6, 8.775)
    ops.node(124013, 0.0, 15.6, 11.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 33180308.59191259, 13825128.57996358, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 26.05921781, 0.00096518, 31.30142774, 0.01140607, 3.13014277, 0.07308626, -26.05921781, -0.00096518, -31.30142774, -0.01140607, -3.13014277, -0.07308626, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 26.05921781, 0.00096518, 31.30142774, 0.01140607, 3.13014277, 0.07308626, -26.05921781, -0.00096518, -31.30142774, -0.01140607, -3.13014277, -0.07308626, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 70.80493516, 0.01930353, 70.80493516, 0.0579106, 49.56345461, -1431.4223213, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 17.70123379, 6.76e-05, 53.10370137, 0.00020281, 177.0123379, 0.00067603, -17.70123379, -6.76e-05, -53.10370137, -0.00020281, -177.0123379, -0.00067603, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 70.80493516, 0.01930353, 70.80493516, 0.0579106, 49.56345461, -1431.4223213, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 17.70123379, 6.76e-05, 53.10370137, 0.00020281, 177.0123379, 0.00067603, -17.70123379, -6.76e-05, -53.10370137, -0.00020281, -177.0123379, -0.00067603, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 3.0, 15.6, 8.8)
    ops.node(124014, 3.0, 15.6, 11.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 30732571.37929501, 12805238.07470626, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 49.94858156, 0.00108425, 60.11556763, 0.01287009, 6.01155676, 0.05708211, -49.94858156, -0.00108425, -60.11556763, -0.01287009, -6.01155676, -0.05708211, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 49.94858156, 0.00108425, 60.11556763, 0.01287009, 6.01155676, 0.05708211, -49.94858156, -0.00108425, -60.11556763, -0.01287009, -6.01155676, -0.05708211, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 65.78115355, 0.02168508, 65.78115355, 0.06505523, 46.04680748, -1048.67717463, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 16.44528839, 6.781e-05, 49.33586516, 0.00020343, 164.45288387, 0.00067809, -16.44528839, -6.781e-05, -49.33586516, -0.00020343, -164.45288387, -0.00067809, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 65.78115355, 0.02168508, 65.78115355, 0.06505523, 46.04680748, -1048.67717463, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 16.44528839, 6.781e-05, 49.33586516, 0.00020343, 164.45288387, 0.00067809, -16.44528839, -6.781e-05, -49.33586516, -0.00020343, -164.45288387, -0.00067809, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.65, 15.6, 8.8)
    ops.node(124015, 7.65, 15.6, 11.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 27774971.16689382, 11572904.65287242, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 52.07277991, 0.00113348, 62.73735862, 0.01096118, 6.27373586, 0.04664598, -52.07277991, -0.00113348, -62.73735862, -0.01096118, -6.27373586, -0.04664598, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 52.07277991, 0.00113348, 62.73735862, 0.01096118, 6.27373586, 0.04664598, -52.07277991, -0.00113348, -62.73735862, -0.01096118, -6.27373586, -0.04664598, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 48.25647515, 0.02266955, 48.25647515, 0.06800866, 33.7795326, -962.18366922, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 12.06411879, 5.504e-05, 36.19235636, 0.00016512, 120.64118787, 0.00055041, -12.06411879, -5.504e-05, -36.19235636, -0.00016512, -120.64118787, -0.00055041, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 48.25647515, 0.02266955, 48.25647515, 0.06800866, 33.7795326, -962.18366922, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 12.06411879, 5.504e-05, 36.19235636, 0.00016512, 120.64118787, 0.00055041, -12.06411879, -5.504e-05, -36.19235636, -0.00016512, -120.64118787, -0.00055041, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.3, 15.6, 8.775)
    ops.node(124016, 12.3, 15.6, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 29920603.87423344, 12466918.2809306, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 38.03479803, 0.00105184, 46.0047811, 0.01374551, 4.60047811, 0.06871098, -38.03479803, -0.00105184, -46.0047811, -0.01374551, -4.60047811, -0.06871098, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 41.73859392, 0.00105184, 50.48468708, 0.01374551, 5.04846871, 0.06871098, -41.73859392, -0.00105184, -50.48468708, -0.01374551, -5.04846871, -0.06871098, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 81.31936301, 0.02103684, 81.31936301, 0.06311053, 56.9235541, -1527.13939297, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 20.32984075, 8.61e-05, 60.98952225, 0.0002583, 203.29840751, 0.00086101, -20.32984075, -8.61e-05, -60.98952225, -0.0002583, -203.29840751, -0.00086101, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 81.31936301, 0.02103684, 81.31936301, 0.06311053, 56.9235541, -1527.13939297, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 20.32984075, 8.61e-05, 60.98952225, 0.0002583, 203.29840751, 0.00086101, -20.32984075, -8.61e-05, -60.98952225, -0.0002583, -203.29840751, -0.00086101, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124017, 0.0, 0.0, 1.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 170001, 124017, 0.0625, 28494389.09857085, 11872662.12440452, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 71.3387793, 0.00082399, 84.97836461, 0.01822544, 8.49783646, 0.06578291, -71.3387793, -0.00082399, -84.97836461, -0.01822544, -8.49783646, -0.06578291, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 62.87833174, 0.00082399, 74.90032565, 0.01822544, 7.49003256, 0.06578291, -62.87833174, -0.00082399, -74.90032565, -0.01822544, -7.49003256, -0.06578291, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 120.4336909, 0.0164797, 120.4336909, 0.04943911, 84.30358363, -3891.74781175, 0.05, 2, 0, 70001, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 30.10842273, 7.425e-05, 90.32526818, 0.00022276, 301.08422726, 0.00074252, -30.10842273, -7.425e-05, -90.32526818, -0.00022276, -301.08422726, -0.00074252, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 120.4336909, 0.0164797, 120.4336909, 0.04943911, 84.30358363, -3891.74781175, 0.05, 2, 0, 70001, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 30.10842273, 7.425e-05, 90.32526818, 0.00022276, 301.08422726, 0.00074252, -30.10842273, -7.425e-05, -90.32526818, -0.00022276, -301.08422726, -0.00074252, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 0.0, 0.0, 1.725)
    ops.node(121001, 0.0, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 174017, 121001, 0.0625, 36225502.4401664, 15093959.35006933, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 47.09456169, 0.00086685, 55.45588876, 0.01748649, 5.54558888, 0.09378359, -47.09456169, -0.00086685, -55.45588876, -0.01748649, -5.54558888, -0.09378359, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 47.09456169, 0.00086685, 55.45588876, 0.01748649, 5.54558888, 0.09378359, -47.09456169, -0.00086685, -55.45588876, -0.01748649, -5.54558888, -0.09378359, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 129.83749024, 0.01733708, 129.83749024, 0.05201124, 90.88624317, -3577.23002517, 0.05, 2, 0, 74017, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 32.45937256, 6.297e-05, 97.37811768, 0.0001889, 324.5937256, 0.00062966, -32.45937256, -6.297e-05, -97.37811768, -0.0001889, -324.5937256, -0.00062966, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 129.83749024, 0.01733708, 129.83749024, 0.05201124, 90.88624317, -3577.23002517, 0.05, 2, 0, 74017, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 32.45937256, 6.297e-05, 97.37811768, 0.0001889, 324.5937256, 0.00062966, -32.45937256, -6.297e-05, -97.37811768, -0.0001889, -324.5937256, -0.00062966, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.0, 0.0, 0.0)
    ops.node(124018, 3.0, 0.0, 1.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 170002, 124018, 0.09, 34914939.33983225, 14547891.39159677, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 161.682286, 0.00075486, 189.37168397, 0.00805024, 18.9371684, 0.03900117, -161.682286, -0.00075486, -189.37168397, -0.00805024, -18.9371684, -0.03900117, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 155.67673706, 0.00075486, 182.33763625, 0.00805024, 18.23376362, 0.03900117, -155.67673706, -0.00075486, -182.33763625, -0.00805024, -18.23376362, -0.03900117, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 184.34179789, 0.01509715, 184.34179789, 0.04529146, 129.03925852, -3636.12228041, 0.05, 2, 0, 70002, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 46.08544947, 6.441e-05, 138.25634842, 0.00019324, 460.85449472, 0.00064413, -46.08544947, -6.441e-05, -138.25634842, -0.00019324, -460.85449472, -0.00064413, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 184.34179789, 0.01509715, 184.34179789, 0.04529146, 129.03925852, -3636.12228041, 0.05, 2, 0, 70002, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 46.08544947, 6.441e-05, 138.25634842, 0.00019324, 460.85449472, 0.00064413, -46.08544947, -6.441e-05, -138.25634842, -0.00019324, -460.85449472, -0.00064413, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 3.0, 0.0, 1.725)
    ops.node(121002, 3.0, 0.0, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4044, 174018, 121002, 0.09, 32789356.50358199, 13662231.87649249, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24044, 123.07088297, 0.00075518, 144.86993943, 0.00890866, 14.48699394, 0.03695212, -123.07088297, -0.00075518, -144.86993943, -0.00890866, -14.48699394, -0.03695212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14044, 123.07088297, 0.00075518, 144.86993943, 0.00890866, 14.48699394, 0.03695212, -123.07088297, -0.00075518, -144.86993943, -0.00890866, -14.48699394, -0.03695212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24044, 4044, 0.0, 177.08410784, 0.01510356, 177.08410784, 0.04531069, 123.95887549, -3715.03941625, 0.05, 2, 0, 74018, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44044, 44.27102696, 6.589e-05, 132.81308088, 0.00019766, 442.71026961, 0.00065888, -44.27102696, -6.589e-05, -132.81308088, -0.00019766, -442.71026961, -0.00065888, 0.4, 0.3, 0.003, 0.0, 0.0, 24044, 2)
    ops.limitCurve('ThreePoint', 14044, 4044, 0.0, 177.08410784, 0.01510356, 177.08410784, 0.04531069, 123.95887549, -3715.03941625, 0.05, 2, 0, 74018, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34044, 44.27102696, 6.589e-05, 132.81308088, 0.00019766, 442.71026961, 0.00065888, -44.27102696, -6.589e-05, -132.81308088, -0.00019766, -442.71026961, -0.00065888, 0.4, 0.3, 0.003, 0.0, 0.0, 14044, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4044, 99999, 'P', 44044, 'Vy', 34044, 'Vz', 24044, 'My', 14044, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4044, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4044, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.275)
    ops.node(124019, 0.0, 0.0, 4.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 171001, 124019, 0.0625, 31659380.94517132, 13191408.72715472, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 43.76229928, 0.00073278, 52.28334243, 0.01102039, 5.22833424, 0.05577697, -43.76229928, -0.00073278, -52.28334243, -0.01102039, -5.22833424, -0.05577697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 43.76229928, 0.00073278, 52.28334243, 0.01102039, 5.22833424, 0.05577697, -43.76229928, -0.00073278, -52.28334243, -0.01102039, -5.22833424, -0.05577697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 102.68469446, 0.01465559, 102.68469446, 0.04396677, 71.87928612, -2609.58895357, 0.05, 2, 0, 71001, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 25.67117362, 5.138e-05, 77.01352085, 0.00015413, 256.71173616, 0.00051376, -25.67117362, -5.138e-05, -77.01352085, -0.00015413, -256.71173616, -0.00051376, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 102.68469446, 0.01465559, 102.68469446, 0.04396677, 71.87928612, -2609.58895357, 0.05, 2, 0, 71001, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 25.67117362, 5.138e-05, 77.01352085, 0.00015413, 256.71173616, 0.00051376, -25.67117362, -5.138e-05, -77.01352085, -0.00015413, -256.71173616, -0.00051376, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 0.0, 0.0, 4.625)
    ops.node(122001, 0.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 122001, 0.0625, 32553738.24122203, 13564057.60050918, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 40.28725915, 0.00072546, 48.15151713, 0.00990517, 4.81515171, 0.05958355, -40.28725915, -0.00072546, -48.15151713, -0.00990517, -4.81515171, -0.05958355, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 40.28725915, 0.00072546, 48.15151713, 0.00990517, 4.81515171, 0.05958355, -40.28725915, -0.00072546, -48.15151713, -0.00990517, -4.81515171, -0.05958355, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 90.62045719, 0.01450925, 90.62045719, 0.04352775, 63.43432003, -2346.75687326, 0.05, 2, 0, 74019, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 22.6551143, 4.409e-05, 67.96534289, 0.00013228, 226.55114298, 0.00044094, -22.6551143, -4.409e-05, -67.96534289, -0.00013228, -226.55114298, -0.00044094, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 90.62045719, 0.01450925, 90.62045719, 0.04352775, 63.43432003, -2346.75687326, 0.05, 2, 0, 74019, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 22.6551143, 4.409e-05, 67.96534289, 0.00013228, 226.55114298, 0.00044094, -22.6551143, -4.409e-05, -67.96534289, -0.00013228, -226.55114298, -0.00044094, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.0, 0.0, 3.3)
    ops.node(124020, 3.0, 0.0, 4.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 171002, 124020, 0.09, 29433028.67200749, 12263761.94666979, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 109.21880707, 0.00069063, 129.51832384, 0.01177194, 12.95183238, 0.04198415, -109.21880707, -0.00069063, -129.51832384, -0.01177194, -12.95183238, -0.04198415, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 109.21880707, 0.00069063, 129.51832384, 0.01177194, 12.95183238, 0.04198415, -109.21880707, -0.00069063, -129.51832384, -0.01177194, -12.95183238, -0.04198415, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 178.86350621, 0.01381267, 178.86350621, 0.04143801, 125.20445435, -4388.51495608, 0.05, 2, 0, 71002, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 44.71587655, 6.685e-05, 134.14762966, 0.00020054, 447.15876553, 0.00066847, -44.71587655, -6.685e-05, -134.14762966, -0.00020054, -447.15876553, -0.00066847, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 178.86350621, 0.01381267, 178.86350621, 0.04143801, 125.20445435, -4388.51495608, 0.05, 2, 0, 71002, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 44.71587655, 6.685e-05, 134.14762966, 0.00020054, 447.15876553, 0.00066847, -44.71587655, -6.685e-05, -134.14762966, -0.00020054, -447.15876553, -0.00066847, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 3.0, 0.0, 4.625)
    ops.node(122002, 3.0, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 122002, 0.09, 30170868.96795686, 12571195.40331536, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 108.11281171, 0.00068511, 128.48416402, 0.00923, 12.8484164, 0.03804777, -108.11281171, -0.00068511, -128.48416402, -0.00923, -12.8484164, -0.03804777, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 108.11281171, 0.00068511, 128.48416402, 0.00923, 12.8484164, 0.03804777, -108.11281171, -0.00068511, -128.48416402, -0.00923, -12.8484164, -0.03804777, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 165.67651804, 0.01370227, 165.67651804, 0.04110682, 115.97356263, -3622.42457046, 0.05, 2, 0, 74020, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 41.41912951, 6.04e-05, 124.25738853, 0.00018121, 414.19129511, 0.00060404, -41.41912951, -6.04e-05, -124.25738853, -0.00018121, -414.19129511, -0.00060404, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 165.67651804, 0.01370227, 165.67651804, 0.04110682, 115.97356263, -3622.42457046, 0.05, 2, 0, 74020, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 41.41912951, 6.04e-05, 124.25738853, 0.00018121, 414.19129511, 0.00060404, -41.41912951, -6.04e-05, -124.25738853, -0.00018121, -414.19129511, -0.00060404, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.025)
    ops.node(124021, 0.0, 0.0, 7.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 172001, 124021, 0.0625, 31286074.76146504, 13035864.48394377, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 36.39569685, 0.00072325, 43.72386739, 0.01024614, 4.37238674, 0.0611361, -36.39569685, -0.00072325, -43.72386739, -0.01024614, -4.37238674, -0.0611361, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 36.39569685, 0.00072325, 43.72386739, 0.01024614, 4.37238674, 0.0611361, -36.39569685, -0.00072325, -43.72386739, -0.01024614, -4.37238674, -0.0611361, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 84.07250507, 0.01446496, 84.07250507, 0.04339488, 58.85075355, -2345.34254298, 0.05, 2, 0, 72001, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 21.01812627, 4.257e-05, 63.05437881, 0.0001277, 210.18126268, 0.00042566, -21.01812627, -4.257e-05, -63.05437881, -0.0001277, -210.18126268, -0.00042566, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 84.07250507, 0.01446496, 84.07250507, 0.04339488, 58.85075355, -2345.34254298, 0.05, 2, 0, 72001, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 21.01812627, 4.257e-05, 63.05437881, 0.0001277, 210.18126268, 0.00042566, -21.01812627, -4.257e-05, -63.05437881, -0.0001277, -210.18126268, -0.00042566, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 0.0, 0.0, 7.35)
    ops.node(123001, 0.0, 0.0, 8.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 123001, 0.0625, 30493132.69180626, 12705471.95491927, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 32.21813268, 0.00066763, 38.8964219, 0.01222709, 3.88964219, 0.06693645, -32.21813268, -0.00066763, -38.8964219, -0.01222709, -3.88964219, -0.06693645, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 32.21813268, 0.00066763, 38.8964219, 0.01222709, 3.88964219, 0.06693645, -32.21813268, -0.00066763, -38.8964219, -0.01222709, -3.88964219, -0.06693645, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 86.75482105, 0.0133527, 86.75482105, 0.0400581, 60.72837473, -2636.3055467, 0.05, 2, 0, 74021, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 21.68870526, 4.507e-05, 65.06611579, 0.0001352, 216.88705262, 0.00045066, -21.68870526, -4.507e-05, -65.06611579, -0.0001352, -216.88705262, -0.00045066, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 86.75482105, 0.0133527, 86.75482105, 0.0400581, 60.72837473, -2636.3055467, 0.05, 2, 0, 74021, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 21.68870526, 4.507e-05, 65.06611579, 0.0001352, 216.88705262, 0.00045066, -21.68870526, -4.507e-05, -65.06611579, -0.0001352, -216.88705262, -0.00045066, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.0, 0.0, 6.05)
    ops.node(124022, 3.0, 0.0, 7.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 172002, 124022, 0.0625, 28169917.09349846, 11737465.45562436, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 56.69068066, 0.0007787, 67.26804919, 0.00984141, 6.72680492, 0.03675564, -56.69068066, -0.0007787, -67.26804919, -0.00984141, -6.72680492, -0.03675564, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 56.69068066, 0.0007787, 67.26804919, 0.00984141, 6.72680492, 0.03675564, -56.69068066, -0.0007787, -67.26804919, -0.00984141, -6.72680492, -0.03675564, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 105.80068443, 0.01557402, 105.80068443, 0.04672205, 74.0604791, -2995.1144853, 0.05, 2, 0, 72002, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 26.45017111, 5.949e-05, 79.35051332, 0.00017848, 264.50171108, 0.00059492, -26.45017111, -5.949e-05, -79.35051332, -0.00017848, -264.50171108, -0.00059492, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 105.80068443, 0.01557402, 105.80068443, 0.04672205, 74.0604791, -2995.1144853, 0.05, 2, 0, 72002, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 26.45017111, 5.949e-05, 79.35051332, 0.00017848, 264.50171108, 0.00059492, -26.45017111, -5.949e-05, -79.35051332, -0.00017848, -264.50171108, -0.00059492, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 3.0, 0.0, 7.35)
    ops.node(123002, 3.0, 0.0, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 123002, 0.0625, 35409311.70032092, 14753879.87513372, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 50.49713264, 0.00080037, 59.54246937, 0.00910514, 5.95424694, 0.05551901, -50.49713264, -0.00080037, -59.54246937, -0.00910514, -5.95424694, -0.05551901, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 50.49713264, 0.00080037, 59.54246937, 0.00910514, 5.95424694, 0.05551901, -50.49713264, -0.00080037, -59.54246937, -0.00910514, -5.95424694, -0.05551901, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 107.30258669, 0.01600741, 107.30258669, 0.04802223, 75.11181069, -2543.01851929, 0.05, 2, 0, 74022, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 26.82564667, 4.8e-05, 80.47694002, 0.000144, 268.25646673, 0.00048001, -26.82564667, -4.8e-05, -80.47694002, -0.000144, -268.25646673, -0.00048001, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 107.30258669, 0.01600741, 107.30258669, 0.04802223, 75.11181069, -2543.01851929, 0.05, 2, 0, 74022, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 26.82564667, 4.8e-05, 80.47694002, 0.000144, 268.25646673, 0.00048001, -26.82564667, -4.8e-05, -80.47694002, -0.000144, -268.25646673, -0.00048001, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.775)
    ops.node(124023, 0.0, 0.0, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 173001, 124023, 0.0625, 30898239.49953636, 12874266.45814015, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 25.75901409, 0.00070392, 31.15101166, 0.01280058, 3.11510117, 0.07253617, -25.75901409, -0.00070392, -31.15101166, -0.01280058, -3.11510117, -0.07253617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 25.75901409, 0.00070392, 31.15101166, 0.01280058, 3.11510117, 0.07253617, -25.75901409, -0.00070392, -31.15101166, -0.01280058, -3.11510117, -0.07253617, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 84.80904038, 0.01407833, 84.80904038, 0.042235, 59.36632826, -3412.93099055, 0.05, 2, 0, 73001, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 21.20226009, 4.348e-05, 63.60678028, 0.00013043, 212.02260095, 0.00043477, -21.20226009, -4.348e-05, -63.60678028, -0.00013043, -212.02260095, -0.00043477, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 84.80904038, 0.01407833, 84.80904038, 0.042235, 59.36632826, -3412.93099055, 0.05, 2, 0, 73001, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 21.20226009, 4.348e-05, 63.60678028, 0.00013043, 212.02260095, 0.00043477, -21.20226009, -4.348e-05, -63.60678028, -0.00013043, -212.02260095, -0.00043477, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 0.0, 0.0, 10.1)
    ops.node(124001, 0.0, 0.0, 11.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 124001, 0.0625, 31191729.16530515, 12996553.81887715, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 21.75271026, 0.00069085, 26.36389652, 0.0135408, 2.63638965, 0.07912163, -21.75271026, -0.00069085, -26.36389652, -0.0135408, -2.63638965, -0.07912163, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 21.75271026, 0.00069085, 26.36389652, 0.0135408, 2.63638965, 0.07912163, -21.75271026, -0.00069085, -26.36389652, -0.0135408, -2.63638965, -0.07912163, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 81.23660145, 0.01381694, 81.23660145, 0.04145081, 56.86562101, -12439.41590258, 0.05, 2, 0, 74023, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 20.30915036, 4.125e-05, 60.92745108, 0.00012376, 203.09150362, 0.00041254, -20.30915036, -4.125e-05, -60.92745108, -0.00012376, -203.09150362, -0.00041254, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 81.23660145, 0.01381694, 81.23660145, 0.04145081, 56.86562101, -12439.41590258, 0.05, 2, 0, 74023, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 20.30915036, 4.125e-05, 60.92745108, 0.00012376, 203.09150362, 0.00041254, -20.30915036, -4.125e-05, -60.92745108, -0.00012376, -203.09150362, -0.00041254, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.0, 0.0, 8.8)
    ops.node(124024, 3.0, 0.0, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 173002, 124024, 0.0625, 30328327.43030292, 12636803.09595955, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 35.92323552, 0.00071012, 43.25566759, 0.01052421, 4.32556676, 0.06035972, -35.92323552, -0.00071012, -43.25566759, -0.01052421, -4.32556676, -0.06035972, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 35.92323552, 0.00071012, 43.25566759, 0.01052421, 4.32556676, 0.06035972, -35.92323552, -0.00071012, -43.25566759, -0.01052421, -4.32556676, -0.06035972, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 82.69847974, 0.01420247, 82.69847974, 0.04260741, 57.88893582, -2337.89673539, 0.05, 2, 0, 73002, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 20.67461994, 4.319e-05, 62.02385981, 0.00012958, 206.74619935, 0.00043192, -20.67461994, -4.319e-05, -62.02385981, -0.00012958, -206.74619935, -0.00043192, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 82.69847974, 0.01420247, 82.69847974, 0.04260741, 57.88893582, -2337.89673539, 0.05, 2, 0, 73002, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 20.67461994, 4.319e-05, 62.02385981, 0.00012958, 206.74619935, 0.00043192, -20.67461994, -4.319e-05, -62.02385981, -0.00012958, -206.74619935, -0.00043192, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 3.0, 0.0, 10.1)
    ops.node(124002, 3.0, 0.0, 11.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 124002, 0.0625, 29991180.37062142, 12496325.15442559, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 30.85513762, 0.00068156, 37.30440992, 0.01409758, 3.73044099, 0.06869021, -30.85513762, -0.00068156, -37.30440992, -0.01409758, -3.73044099, -0.06869021, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 30.85513762, 0.00068156, 37.30440992, 0.01409758, 3.73044099, 0.06869021, -30.85513762, -0.00068156, -37.30440992, -0.01409758, -3.73044099, -0.06869021, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 91.95469063, 0.01363122, 91.95469063, 0.04089367, 64.36828344, -3350.67747578, 0.05, 2, 0, 74024, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 22.98867266, 4.857e-05, 68.96601797, 0.0001457, 229.88672658, 0.00048566, -22.98867266, -4.857e-05, -68.96601797, -0.0001457, -229.88672658, -0.00048566, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 91.95469063, 0.01363122, 91.95469063, 0.04089367, 64.36828344, -3350.67747578, 0.05, 2, 0, 74024, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 22.98867266, 4.857e-05, 68.96601797, 0.0001457, 229.88672658, 0.00048566, -22.98867266, -4.857e-05, -68.96601797, -0.0001457, -229.88672658, -0.00048566, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4059, '-orient', 0, 0, 1, 0, 1, 0)
