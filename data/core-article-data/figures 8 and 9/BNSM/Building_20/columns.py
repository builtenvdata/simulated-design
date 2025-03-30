import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 8.15, 0.0, 0.0)
    ops.node(121003, 8.15, 0.0, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.1225, 27822730.79933828, 11592804.49972428, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 167.11077144, 0.00110759, 199.43796515, 0.01365241, 19.94379652, 0.0377048, -167.11077144, -0.00110759, -199.43796515, -0.01365241, -19.94379652, -0.0377048, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 179.91222039, 0.00110759, 214.71582491, 0.01365241, 21.47158249, 0.0377048, -179.91222039, -0.00110759, -214.71582491, -0.01365241, -21.47158249, -0.0377048, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 160.02868468, 0.02215176, 160.02868468, 0.06645528, 112.02007927, -1842.23023177, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 40.00717117, 0.00011325, 120.02151351, 0.00033975, 400.07171169, 0.0011325, -40.00717117, -0.00011325, -120.02151351, -0.00033975, -400.07171169, -0.0011325, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 160.02868468, 0.02215176, 160.02868468, 0.06645528, 112.02007927, -1842.23023177, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 40.00717117, 0.00011325, 120.02151351, 0.00033975, 400.07171169, 0.0011325, -40.00717117, -0.00011325, -120.02151351, -0.00033975, -400.07171169, -0.0011325, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.45, 0.0, 0.0)
    ops.node(121004, 13.45, 0.0, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.0625, 29604556.89257659, 12335232.03857358, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 60.26230399, 0.00151649, 71.61115796, 0.01425109, 7.1611158, 0.04580957, -60.26230399, -0.00151649, -71.61115796, -0.01425109, -7.1611158, -0.04580957, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 64.13826462, 0.00151649, 76.21705601, 0.01425109, 7.6217056, 0.04580957, -64.13826462, -0.00151649, -76.21705601, -0.01425109, -7.6217056, -0.04580957, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 99.88980523, 0.03032984, 99.88980523, 0.09098952, 69.92286366, -1235.86521893, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 24.97245131, 0.00013021, 74.91735392, 0.00039064, 249.72451308, 0.00130215, -24.97245131, -0.00013021, -74.91735392, -0.00039064, -249.72451308, -0.00130215, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 99.88980523, 0.03032984, 99.88980523, 0.09098952, 69.92286366, -1235.86521893, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 24.97245131, 0.00013021, 74.91735392, 0.00039064, 249.72451308, 0.00130215, -24.97245131, -0.00013021, -74.91735392, -0.00039064, -249.72451308, -0.00130215, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 3.85, 0.0)
    ops.node(121005, 0.0, 3.85, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.0625, 29350185.11536952, 12229243.79807063, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 61.62778583, 0.00150965, 73.11393068, 0.01398811, 7.31139307, 0.04340499, -61.62778583, -0.00150965, -73.11393068, -0.01398811, -7.31139307, -0.04340499, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 65.51345856, 0.00150965, 77.72381245, 0.01398811, 7.77238124, 0.04340499, -65.51345856, -0.00150965, -77.72381245, -0.01398811, -7.77238124, -0.04340499, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 101.22155742, 0.03019308, 101.22155742, 0.09057924, 70.85509019, -1270.18576243, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 25.30538936, 0.00013309, 75.91616807, 0.00039928, 253.05389355, 0.00133094, -25.30538936, -0.00013309, -75.91616807, -0.00039928, -253.05389355, -0.00133094, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 101.22155742, 0.03019308, 101.22155742, 0.09057924, 70.85509019, -1270.18576243, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 25.30538936, 0.00013309, 75.91616807, 0.00039928, 253.05389355, 0.00133094, -25.30538936, -0.00013309, -75.91616807, -0.00039928, -253.05389355, -0.00133094, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 2.85, 3.85, 0.0)
    ops.node(121006, 2.85, 3.85, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.16, 29316645.48374938, 12215268.95156224, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 270.29462132, 0.00101955, 323.86398448, 0.01318704, 32.38639845, 0.03351538, -270.29462132, -0.00101955, -323.86398448, -0.01318704, -32.38639845, -0.03351538, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 297.55389317, 0.00101955, 356.52573835, 0.01318704, 35.65257383, 0.03351538, -297.55389317, -0.00101955, -356.52573835, -0.01318704, -35.65257383, -0.03351538, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 173.85932967, 0.02039091, 173.85932967, 0.06117272, 121.70153077, -1561.94861994, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 43.46483242, 8.94e-05, 130.39449726, 0.0002682, 434.64832419, 0.00089401, -43.46483242, -8.94e-05, -130.39449726, -0.0002682, -434.64832419, -0.00089401, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 173.85932967, 0.02039091, 173.85932967, 0.06117272, 121.70153077, -1561.94861994, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 43.46483242, 8.94e-05, 130.39449726, 0.0002682, 434.64832419, 0.00089401, -43.46483242, -8.94e-05, -130.39449726, -0.0002682, -434.64832419, -0.00089401, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 8.15, 3.85, 0.0)
    ops.node(121007, 8.15, 3.85, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.16, 29108038.54940441, 12128349.39558517, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 282.34476223, 0.00105222, 337.60874399, 0.01238843, 33.7608744, 0.03118396, -282.34476223, -0.00105222, -337.60874399, -0.01238843, -33.7608744, -0.03118396, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 309.95828442, 0.00105222, 370.62712361, 0.01238843, 37.06271236, 0.03118396, -309.95828442, -0.00105222, -370.62712361, -0.01238843, -37.06271236, -0.03118396, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 175.48869258, 0.02104433, 175.48869258, 0.06313299, 122.84208481, -1617.39336086, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 43.87217314, 9.089e-05, 131.61651943, 0.00027266, 438.72173145, 0.00090885, -43.87217314, -9.089e-05, -131.61651943, -0.00027266, -438.72173145, -0.00090885, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 175.48869258, 0.02104433, 175.48869258, 0.06313299, 122.84208481, -1617.39336086, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 43.87217314, 9.089e-05, 131.61651943, 0.00027266, 438.72173145, 0.00090885, -43.87217314, -9.089e-05, -131.61651943, -0.00027266, -438.72173145, -0.00090885, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 13.45, 3.85, 0.0)
    ops.node(121008, 13.45, 3.85, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.09, 28772788.93017679, 11988662.05424033, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 117.62804341, 0.00133447, 139.61023146, 0.0135707, 13.96102315, 0.03506732, -117.62804341, -0.00133447, -139.61023146, -0.0135707, -13.96102315, -0.03506732, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 127.44040065, 0.00133447, 151.25631029, 0.0135707, 15.12563103, 0.03506732, -127.44040065, -0.00133447, -151.25631029, -0.0135707, -15.12563103, -0.03506732, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 124.77230448, 0.02668945, 124.77230448, 0.08006835, 87.34061314, -1434.36137673, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 31.19307612, 0.00011622, 93.57922836, 0.00034865, 311.93076121, 0.00116217, -31.19307612, -0.00011622, -93.57922836, -0.00034865, -311.93076121, -0.00116217, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 124.77230448, 0.02668945, 124.77230448, 0.08006835, 87.34061314, -1434.36137673, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 31.19307612, 0.00011622, 93.57922836, 0.00034865, 311.93076121, 0.00116217, -31.19307612, -0.00011622, -93.57922836, -0.00034865, -311.93076121, -0.00116217, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 7.7, 0.0)
    ops.node(121009, 0.0, 7.7, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.0625, 29763744.8946366, 12401560.37276525, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 61.1131773, 0.00149006, 72.63006627, 0.01457046, 7.26300663, 0.0466649, -61.1131773, -0.00149006, -72.63006627, -0.01457046, -7.26300663, -0.0466649, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 65.37110405, 0.00149006, 77.69040703, 0.01457046, 7.7690407, 0.0466649, -65.37110405, -0.00149006, -77.69040703, -0.01457046, -7.7690407, -0.0466649, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 101.20499049, 0.02980123, 101.20499049, 0.08940369, 70.84349334, -1258.1373968, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 25.30124762, 0.00013122, 75.90374287, 0.00039367, 253.01247622, 0.00131224, -25.30124762, -0.00013122, -75.90374287, -0.00039367, -253.01247622, -0.00131224, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 101.20499049, 0.02980123, 101.20499049, 0.08940369, 70.84349334, -1258.1373968, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 25.30124762, 0.00013122, 75.90374287, 0.00039367, 253.01247622, 0.00131224, -25.30124762, -0.00013122, -75.90374287, -0.00039367, -253.01247622, -0.00131224, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 2.85, 7.7, 0.0)
    ops.node(121010, 2.85, 7.7, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.1225, 29032683.72199382, 12096951.55083076, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 187.95558712, 0.00112745, 224.68046429, 0.0145319, 22.46804643, 0.03886642, -187.95558712, -0.00112745, -224.68046429, -0.0145319, -22.46804643, -0.03886642, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 201.37663073, 0.00112745, 240.72386239, 0.0145319, 24.07238624, 0.03886642, -201.37663073, -0.00112745, -240.72386239, -0.0145319, -24.07238624, -0.03886642, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 151.60726612, 0.02254908, 151.60726612, 0.06764723, 106.12508628, -1574.54320637, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 37.90181653, 0.00010282, 113.70544959, 0.00030846, 379.01816529, 0.00102819, -37.90181653, -0.00010282, -113.70544959, -0.00030846, -379.01816529, -0.00102819, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 151.60726612, 0.02254908, 151.60726612, 0.06764723, 106.12508628, -1574.54320637, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 37.90181653, 0.00010282, 113.70544959, 0.00030846, 379.01816529, 0.00102819, -37.90181653, -0.00010282, -113.70544959, -0.00030846, -379.01816529, -0.00102819, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.15, 7.7, 0.0)
    ops.node(121011, 8.15, 7.7, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 28948284.03663175, 12061785.01526323, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 281.68657474, 0.00104484, 336.84131382, 0.01253622, 33.68413138, 0.03112128, -281.68657474, -0.00104484, -336.84131382, -0.01253622, -33.68413138, -0.03112128, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 309.47299696, 0.00104484, 370.0683676, 0.01253622, 37.00683676, 0.03112128, -309.47299696, -0.00104484, -370.0683676, -0.01253622, -37.00683676, -0.03112128, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 174.98354083, 0.02089683, 174.98354083, 0.06269048, 122.48847858, -1623.35381007, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 43.74588521, 9.112e-05, 131.23765562, 0.00027337, 437.45885207, 0.00091124, -43.74588521, -9.112e-05, -131.23765562, -0.00027337, -437.45885207, -0.00091124, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 174.98354083, 0.02089683, 174.98354083, 0.06269048, 122.48847858, -1623.35381007, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 43.74588521, 9.112e-05, 131.23765562, 0.00027337, 437.45885207, 0.00091124, -43.74588521, -9.112e-05, -131.23765562, -0.00027337, -437.45885207, -0.00091124, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 13.45, 7.7, 0.0)
    ops.node(121012, 13.45, 7.7, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.09, 29768114.55131588, 12403381.06304828, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 117.54110887, 0.00129736, 139.55045084, 0.01407599, 13.95504508, 0.03764006, -117.54110887, -0.00129736, -139.55045084, -0.01407599, -13.95504508, -0.03764006, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 128.17195673, 0.00129736, 152.1719041, 0.01407599, 15.21719041, 0.03764006, -128.17195673, -0.00129736, -152.1719041, -0.01407599, -15.21719041, -0.03764006, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 128.93114849, 0.02594722, 128.93114849, 0.07784167, 90.25180394, -1455.2695718, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 32.23278712, 0.00011608, 96.69836137, 0.00034823, 322.32787122, 0.00116076, -32.23278712, -0.00011608, -96.69836137, -0.00034823, -322.32787122, -0.00116076, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 128.93114849, 0.02594722, 128.93114849, 0.07784167, 90.25180394, -1455.2695718, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 32.23278712, 0.00011608, 96.69836137, 0.00034823, 322.32787122, 0.00116076, -32.23278712, -0.00011608, -96.69836137, -0.00034823, -322.32787122, -0.00116076, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 11.55, 0.0)
    ops.node(121013, 0.0, 11.55, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0625, 29558680.10729924, 12316116.71137469, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 59.96683876, 0.00151235, 71.26865819, 0.01444724, 7.12686582, 0.0459963, -59.96683876, -0.00151235, -71.26865819, -0.01444724, -7.12686582, -0.0459963, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 63.81660133, 0.00151235, 75.84397713, 0.01444724, 7.58439771, 0.0459963, -63.81660133, -0.00151235, -75.84397713, -0.01444724, -7.58439771, -0.0459963, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 100.98396695, 0.03024698, 100.98396695, 0.09074093, 70.68877687, -1263.05762345, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 25.24599174, 0.00013185, 75.73797521, 0.00039554, 252.45991738, 0.00131845, -25.24599174, -0.00013185, -75.73797521, -0.00039554, -252.45991738, -0.00131845, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 100.98396695, 0.03024698, 100.98396695, 0.09074093, 70.68877687, -1263.05762345, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 25.24599174, 0.00013185, 75.73797521, 0.00039554, 252.45991738, 0.00131845, -25.24599174, -0.00013185, -75.73797521, -0.00039554, -252.45991738, -0.00131845, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 2.85, 11.55, 0.0)
    ops.node(121014, 2.85, 11.55, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.1225, 28532222.42798179, 11888426.01165908, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 199.37192948, 0.00113309, 238.3493618, 0.01477537, 23.83493618, 0.03822199, -199.37192948, -0.00113309, -238.3493618, -0.01477537, -23.83493618, -0.03822199, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 206.007781, 0.00113309, 246.28252963, 0.01477537, 24.62825296, 0.03822199, -206.007781, -0.00113309, -246.28252963, -0.01477537, -24.62825296, -0.03822199, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 151.11239103, 0.02266181, 151.11239103, 0.06798543, 105.77867372, -1605.12342311, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 37.77809776, 0.00010428, 113.33429327, 0.00031284, 377.78097758, 0.00104281, -37.77809776, -0.00010428, -113.33429327, -0.00031284, -377.78097758, -0.00104281, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 151.11239103, 0.02266181, 151.11239103, 0.06798543, 105.77867372, -1605.12342311, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 37.77809776, 0.00010428, 113.33429327, 0.00031284, 377.78097758, 0.00104281, -37.77809776, -0.00010428, -113.33429327, -0.00031284, -377.78097758, -0.00104281, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 8.15, 11.55, 0.0)
    ops.node(121015, 8.15, 11.55, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.16, 29524053.25041422, 12301688.85433926, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 300.00746338, 0.00104542, 358.6500835, 0.0128343, 35.86500835, 0.03216549, -300.00746338, -0.00104542, -358.6500835, -0.0128343, -35.86500835, -0.03216549, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 321.71081135, 0.00104542, 384.59579656, 0.0128343, 38.45957966, 0.03216549, -321.71081135, -0.00104542, -384.59579656, -0.0128343, -38.45957966, -0.03216549, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 177.91752331, 0.02090836, 177.91752331, 0.06272508, 124.54226632, -1621.85143785, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 44.47938083, 9.084e-05, 133.43814248, 0.00027253, 444.79380827, 0.00090845, -44.47938083, -9.084e-05, -133.43814248, -0.00027253, -444.79380827, -0.00090845, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 177.91752331, 0.02090836, 177.91752331, 0.06272508, 124.54226632, -1621.85143785, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 44.47938083, 9.084e-05, 133.43814248, 0.00027253, 444.79380827, 0.00090845, -44.47938083, -9.084e-05, -133.43814248, -0.00027253, -444.79380827, -0.00090845, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 13.45, 11.55, 0.0)
    ops.node(121016, 13.45, 11.55, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.09, 28709464.04057002, 11962276.68357084, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 129.82726423, 0.00129511, 154.08259414, 0.0135892, 15.40825941, 0.03807209, -129.82726423, -0.00129511, -154.08259414, -0.0135892, -15.40825941, -0.03807209, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 135.50940794, 0.00129511, 160.82631973, 0.0135892, 16.08263197, 0.03807209, -135.50940794, -0.00129511, -160.82631973, -0.0135892, -16.08263197, -0.03807209, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 132.42573605, 0.02590212, 132.42573605, 0.07770635, 92.69801524, -1591.45242328, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 33.10643401, 0.00012362, 99.31930204, 0.00037085, 331.06434013, 0.00123618, -33.10643401, -0.00012362, -99.31930204, -0.00037085, -331.06434013, -0.00123618, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 132.42573605, 0.02590212, 132.42573605, 0.07770635, 92.69801524, -1591.45242328, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 33.10643401, 0.00012362, 99.31930204, 0.00037085, 331.06434013, 0.00123618, -33.10643401, -0.00012362, -99.31930204, -0.00037085, -331.06434013, -0.00123618, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 15.4, 0.0)
    ops.node(121017, 0.0, 15.4, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.0625, 30201579.21782729, 12583991.34076137, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 60.90094974, 0.00146488, 72.36940352, 0.014346, 7.23694035, 0.04758129, -60.90094974, -0.00146488, -72.36940352, -0.014346, -7.23694035, -0.04758129, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 65.13656708, 0.00146488, 77.40264359, 0.014346, 7.74026436, 0.04758129, -65.13656708, -0.00146488, -77.40264359, -0.014346, -7.74026436, -0.04758129, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 101.24463578, 0.02929758, 101.24463578, 0.08789275, 70.87124504, -1237.97744127, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 25.31115894, 0.00012937, 75.93347683, 0.00038812, 253.11158944, 0.00129372, -25.31115894, -0.00012937, -75.93347683, -0.00038812, -253.11158944, -0.00129372, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 101.24463578, 0.02929758, 101.24463578, 0.08789275, 70.87124504, -1237.97744127, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 25.31115894, 0.00012937, 75.93347683, 0.00038812, 253.11158944, 0.00129372, -25.31115894, -0.00012937, -75.93347683, -0.00038812, -253.11158944, -0.00129372, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 2.85, 15.4, 0.0)
    ops.node(121018, 2.85, 15.4, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.1225, 30441083.63528915, 12683784.84803715, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 216.83837841, 0.00113687, 258.94386859, 0.01597645, 25.89438686, 0.04262883, -216.83837841, -0.00113687, -258.94386859, -0.01597645, -25.89438686, -0.04262883, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 228.35760842, 0.00113687, 272.69989279, 0.01597645, 27.26998928, 0.04262883, -228.35760842, -0.00113687, -272.69989279, -0.01597645, -27.26998928, -0.04262883, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 157.90333524, 0.02273733, 157.90333524, 0.06821198, 110.53233467, -1586.55265533, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 39.47583381, 0.00010213, 118.42750143, 0.0003064, 394.75833811, 0.00102134, -39.47583381, -0.00010213, -118.42750143, -0.0003064, -394.75833811, -0.00102134, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 157.90333524, 0.02273733, 157.90333524, 0.06821198, 110.53233467, -1586.55265533, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 39.47583381, 0.00010213, 118.42750143, 0.0003064, 394.75833811, 0.00102134, -39.47583381, -0.00010213, -118.42750143, -0.0003064, -394.75833811, -0.00102134, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 8.15, 15.4, 0.0)
    ops.node(121019, 8.15, 15.4, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.16, 29481137.17334965, 12283807.15556235, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 317.0930568, 0.0010609, 379.08565046, 0.01261026, 37.90856505, 0.03188702, -317.0930568, -0.0010609, -379.08565046, -0.01261026, -37.90856505, -0.03188702, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 331.59239902, 0.0010609, 396.41965529, 0.01261026, 39.64196553, 0.03188702, -331.59239902, -0.0010609, -396.41965529, -0.01261026, -39.64196553, -0.03188702, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 177.85603151, 0.02121792, 177.85603151, 0.06365377, 124.49922206, -1624.82564723, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 44.46400788, 9.095e-05, 133.39202364, 0.00027284, 444.64007879, 0.00090946, -44.46400788, -9.095e-05, -133.39202364, -0.00027284, -444.64007879, -0.00090946, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 177.85603151, 0.02121792, 177.85603151, 0.06365377, 124.49922206, -1624.82564723, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 44.46400788, 9.095e-05, 133.39202364, 0.00027284, 444.64007879, 0.00090946, -44.46400788, -9.095e-05, -133.39202364, -0.00027284, -444.64007879, -0.00090946, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 13.45, 15.4, 0.0)
    ops.node(121020, 13.45, 15.4, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.09, 30412020.66071639, 12671675.27529849, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 131.74491146, 0.00134731, 156.39139435, 0.01387649, 15.63913943, 0.03871495, -131.74491146, -0.00134731, -156.39139435, -0.01387649, -15.63913943, -0.03871495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 137.2003642, 0.00134731, 162.86743848, 0.01387649, 16.28674385, 0.03871495, -137.2003642, -0.00134731, -162.86743848, -0.01387649, -16.28674385, -0.03871495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 128.80573373, 0.02694623, 128.80573373, 0.08083869, 90.16401361, -1413.46967106, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 32.20143343, 0.00011351, 96.6043003, 0.00034052, 322.01433433, 0.00113508, -32.20143343, -0.00011351, -96.6043003, -0.00034052, -322.01433433, -0.00113508, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 128.80573373, 0.02694623, 128.80573373, 0.08083869, 90.16401361, -1413.46967106, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 32.20143343, 0.00011351, 96.6043003, 0.00034052, 322.01433433, 0.00113508, -32.20143343, -0.00011351, -96.6043003, -0.00034052, -322.01433433, -0.00113508, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 0.0, 19.25, 0.0)
    ops.node(121021, 0.0, 19.25, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.0625, 28274496.97854435, 11781040.40772681, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 49.16468167, 0.00145343, 58.99695832, 0.01632525, 5.89969583, 0.05424685, -49.16468167, -0.00145343, -58.99695832, -0.01632525, -5.89969583, -0.05424685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 52.89628786, 0.00145343, 63.47483568, 0.01632525, 6.34748357, 0.05424685, -52.89628786, -0.00145343, -63.47483568, -0.01632525, -6.34748357, -0.05424685, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 92.27393657, 0.02906856, 92.27393657, 0.08720567, 64.5917556, -1227.11797336, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 23.06848414, 0.00012595, 69.20545243, 0.00037784, 230.68484144, 0.00125945, -23.06848414, -0.00012595, -69.20545243, -0.00037784, -230.68484144, -0.00125945, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 92.27393657, 0.02906856, 92.27393657, 0.08720567, 64.5917556, -1227.11797336, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 23.06848414, 0.00012595, 69.20545243, 0.00037784, 230.68484144, 0.00125945, -23.06848414, -0.00012595, -69.20545243, -0.00037784, -230.68484144, -0.00125945, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 2.85, 19.25, 0.0)
    ops.node(121022, 2.85, 19.25, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.09, 29505554.99546578, 12293981.24811074, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 121.46280426, 0.00127794, 144.77977786, 0.0147582, 14.47797779, 0.0444828, -121.46280426, -0.00127794, -144.77977786, -0.0147582, -14.47797779, -0.0444828, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 126.78071852, 0.00127794, 151.11856157, 0.0147582, 15.11185616, 0.0444828, -126.78071852, -0.00127794, -151.11856157, -0.0147582, -15.11185616, -0.0444828, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 131.06291998, 0.02555872, 131.06291998, 0.07667615, 91.74404399, -1527.817801, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 32.76573, 0.00011904, 98.29718999, 0.00035713, 327.65729996, 0.00119045, -32.76573, -0.00011904, -98.29718999, -0.00035713, -327.65729996, -0.00119045, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 131.06291998, 0.02555872, 131.06291998, 0.07667615, 91.74404399, -1527.817801, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 32.76573, 0.00011904, 98.29718999, 0.00035713, 327.65729996, 0.00119045, -32.76573, -0.00011904, -98.29718999, -0.00035713, -327.65729996, -0.00119045, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 8.15, 19.25, 0.0)
    ops.node(121023, 8.15, 19.25, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.1225, 28186091.72620538, 11744204.88591891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 198.54363168, 0.00111658, 236.99283492, 0.0139194, 23.69928349, 0.03876355, -198.54363168, -0.00111658, -236.99283492, -0.0139194, -23.69928349, -0.03876355, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 198.54363168, 0.00111658, 236.99283492, 0.0139194, 23.69928349, 0.03876355, -198.54363168, -0.00111658, -236.99283492, -0.0139194, -23.69928349, -0.03876355, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 159.6187886, 0.02233152, 159.6187886, 0.06699457, 111.73315202, -1803.00658872, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 39.90469715, 0.0001115, 119.71409145, 0.00033451, 399.04697151, 0.00111504, -39.90469715, -0.0001115, -119.71409145, -0.00033451, -399.04697151, -0.00111504, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 159.6187886, 0.02233152, 159.6187886, 0.06699457, 111.73315202, -1803.00658872, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 39.90469715, 0.0001115, 119.71409145, 0.00033451, 399.04697151, 0.00111504, -39.90469715, -0.0001115, -119.71409145, -0.00033451, -399.04697151, -0.00111504, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 13.45, 19.25, 0.0)
    ops.node(121024, 13.45, 19.25, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.0625, 29334061.25741038, 12222525.52392099, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 70.00727198, 0.00152218, 83.18973521, 0.01451179, 8.31897352, 0.04534146, -70.00727198, -0.00152218, -83.18973521, -0.01451179, -8.31897352, -0.04534146, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 70.00727198, 0.00152218, 83.18973521, 0.01451179, 8.31897352, 0.04534146, -70.00727198, -0.00152218, -83.18973521, -0.01451179, -8.31897352, -0.04534146, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 99.61531921, 0.03044367, 99.61531921, 0.09133102, 69.73072345, -1242.64349035, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 24.9038298, 0.00013105, 74.71148941, 0.00039316, 249.03829804, 0.00131054, -24.9038298, -0.00013105, -74.71148941, -0.00039316, -249.03829804, -0.00131054, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 99.61531921, 0.03044367, 99.61531921, 0.09133102, 69.73072345, -1242.64349035, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 24.9038298, 0.00013105, 74.71148941, 0.00039316, 249.03829804, 0.00131054, -24.9038298, -0.00013105, -74.71148941, -0.00039316, -249.03829804, -0.00131054, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.15, 0.0, 3.6)
    ops.node(122003, 8.15, 0.0, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.1225, 28364455.65409087, 11818523.18920453, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 120.07378693, 0.00095416, 144.2688946, 0.01416049, 14.42688946, 0.04477759, -120.07378693, -0.00095416, -144.2688946, -0.01416049, -14.42688946, -0.04477759, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 108.06447132, 0.00095416, 129.83967793, 0.01416049, 12.98396779, 0.04477759, -108.06447132, -0.00095416, -129.83967793, -0.01416049, -12.98396779, -0.04477759, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 153.79416672, 0.01908323, 153.79416672, 0.05724968, 107.6559167, -2080.70017937, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 38.44854168, 8.923e-05, 115.34562504, 0.0002677, 384.48541679, 0.00089232, -38.44854168, -8.923e-05, -115.34562504, -0.0002677, -384.48541679, -0.00089232, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 153.79416672, 0.01908323, 153.79416672, 0.05724968, 107.6559167, -2080.70017937, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 38.44854168, 8.923e-05, 115.34562504, 0.0002677, 384.48541679, 0.00089232, -38.44854168, -8.923e-05, -115.34562504, -0.0002677, -384.48541679, -0.00089232, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.45, 0.0, 3.6)
    ops.node(122004, 13.45, 0.0, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.0625, 28502347.76707625, 11875978.23628177, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 46.08932397, 0.00128392, 55.1800988, 0.0149113, 5.51800988, 0.05096002, -46.08932397, -0.00128392, -55.1800988, -0.0149113, -5.51800988, -0.05096002, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 46.08932397, 0.00128392, 55.1800988, 0.0149113, 5.51800988, 0.05096002, -46.08932397, -0.00128392, -55.1800988, -0.0149113, -5.51800988, -0.05096002, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 92.91338456, 0.0256785, 92.91338456, 0.07703549, 65.03936919, -1428.3389605, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 23.22834614, 0.00010515, 69.68503842, 0.00031545, 232.2834614, 0.0010515, -23.22834614, -0.00010515, -69.68503842, -0.00031545, -232.2834614, -0.0010515, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 92.91338456, 0.0256785, 92.91338456, 0.07703549, 65.03936919, -1428.3389605, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 23.22834614, 0.00010515, 69.68503842, 0.00031545, 232.2834614, 0.0010515, -23.22834614, -0.00010515, -69.68503842, -0.00031545, -232.2834614, -0.0010515, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 3.85, 3.55)
    ops.node(122005, 0.0, 3.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.0625, 29711434.97458602, 12379764.57274417, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 53.58876516, 0.00127153, 64.03587276, 0.01556471, 6.40358728, 0.0531539, -53.58876516, -0.00127153, -64.03587276, -0.01556471, -6.40358728, -0.0531539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 57.5370969, 0.00127153, 68.75393014, 0.01556471, 6.87539301, 0.0531539, -57.5370969, -0.00127153, -68.75393014, -0.01556471, -6.87539301, -0.0531539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 97.04927581, 0.02543064, 97.04927581, 0.07629193, 67.93449306, -1454.88965189, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 24.26231895, 0.00010536, 72.78695685, 0.00031608, 242.62318951, 0.00105361, -24.26231895, -0.00010536, -72.78695685, -0.00031608, -242.62318951, -0.00105361, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 97.04927581, 0.02543064, 97.04927581, 0.07629193, 67.93449306, -1454.88965189, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 24.26231895, 0.00010536, 72.78695685, 0.00031608, 242.62318951, 0.00105361, -24.26231895, -0.00010536, -72.78695685, -0.00031608, -242.62318951, -0.00105361, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 2.85, 3.85, 3.55)
    ops.node(122006, 2.85, 3.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.16, 28835944.71810736, 12014976.96587807, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 169.70101975, 0.00088068, 204.38215577, 0.01272521, 20.43821558, 0.03550905, -169.70101975, -0.00088068, -204.38215577, -0.01272521, -20.43821558, -0.03550905, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 169.70101975, 0.00088068, 204.38215577, 0.01272521, 20.43821558, 0.03550905, -169.70101975, -0.00088068, -204.38215577, -0.01272521, -20.43821558, -0.03550905, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 160.14358191, 0.01761354, 160.14358191, 0.05284063, 112.10050733, -1633.68700374, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 40.03589548, 6.998e-05, 120.10768643, 0.00020993, 400.35895476, 0.00069975, -40.03589548, -6.998e-05, -120.10768643, -0.00020993, -400.35895476, -0.00069975, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 160.14358191, 0.01761354, 160.14358191, 0.05284063, 112.10050733, -1633.68700374, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 40.03589548, 6.998e-05, 120.10768643, 0.00020993, 400.35895476, 0.00069975, -40.03589548, -6.998e-05, -120.10768643, -0.00020993, -400.35895476, -0.00069975, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 8.15, 3.85, 3.55)
    ops.node(122007, 8.15, 3.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.16, 28414397.05274494, 11839332.10531039, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 181.55354379, 0.0009039, 218.30890924, 0.01212067, 21.83089092, 0.03313868, -181.55354379, -0.0009039, -218.30890924, -0.01212067, -21.83089092, -0.03313868, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 181.55354379, 0.0009039, 218.30890924, 0.01212067, 21.83089092, 0.03313868, -181.55354379, -0.0009039, -218.30890924, -0.01212067, -21.83089092, -0.03313868, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 161.2503571, 0.01807793, 161.2503571, 0.0542338, 112.87524997, -1692.41620569, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 40.31258928, 7.15e-05, 120.93776783, 0.00021451, 403.12589276, 0.00071504, -40.31258928, -7.15e-05, -120.93776783, -0.00021451, -403.12589276, -0.00071504, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 161.2503571, 0.01807793, 161.2503571, 0.0542338, 112.87524997, -1692.41620569, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 40.31258928, 7.15e-05, 120.93776783, 0.00021451, 403.12589276, 0.00071504, -40.31258928, -7.15e-05, -120.93776783, -0.00021451, -403.12589276, -0.00071504, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 13.45, 3.85, 3.55)
    ops.node(122008, 13.45, 3.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.09, 28819413.93867648, 12008089.1411152, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 110.80486437, 0.00114389, 132.51633956, 0.01512654, 13.25163396, 0.0421962, -110.80486437, -0.00114389, -132.51633956, -0.01512654, -13.25163396, -0.0421962, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 101.73404738, 0.00114389, 121.6681564, 0.01512654, 12.16681564, 0.0421962, -101.73404738, -0.00114389, -121.6681564, -0.01512654, -12.16681564, -0.0421962, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 116.47599801, 0.02287772, 116.47599801, 0.06863315, 81.53319861, -1528.80273448, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 29.1189995, 9.053e-05, 87.35699851, 0.00027159, 291.18999503, 0.00090531, -29.1189995, -9.053e-05, -87.35699851, -0.00027159, -291.18999503, -0.00090531, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 116.47599801, 0.02287772, 116.47599801, 0.06863315, 81.53319861, -1528.80273448, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 29.1189995, 9.053e-05, 87.35699851, 0.00027159, 291.18999503, 0.00090531, -29.1189995, -9.053e-05, -87.35699851, -0.00027159, -291.18999503, -0.00090531, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 7.7, 3.55)
    ops.node(122009, 0.0, 7.7, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.0625, 29154531.46772906, 12147721.44488711, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 51.60992965, 0.00124315, 61.7774842, 0.01583362, 6.17774842, 0.05359276, -51.60992965, -0.00124315, -61.7774842, -0.01583362, -6.17774842, -0.05359276, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 55.60044408, 0.00124315, 66.55416078, 0.01583362, 6.65541608, 0.05359276, -55.60044408, -0.00124315, -66.55416078, -0.01583362, -6.65541608, -0.05359276, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 94.46241739, 0.02486299, 94.46241739, 0.07458898, 66.12369217, -1436.33318474, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 23.61560435, 0.00010451, 70.84681304, 0.00031353, 236.15604348, 0.00104511, -23.61560435, -0.00010451, -70.84681304, -0.00031353, -236.15604348, -0.00104511, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 94.46241739, 0.02486299, 94.46241739, 0.07458898, 66.12369217, -1436.33318474, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 23.61560435, 0.00010451, 70.84681304, 0.00031353, 236.15604348, 0.00104511, -23.61560435, -0.00010451, -70.84681304, -0.00031353, -236.15604348, -0.00104511, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 2.85, 7.7, 3.55)
    ops.node(122010, 2.85, 7.7, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.1225, 29422481.4410108, 12259367.26708784, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 126.76047752, 0.0009561, 152.27726891, 0.01474108, 15.22772689, 0.04385091, -126.76047752, -0.0009561, -152.27726891, -0.01474108, -15.22772689, -0.04385091, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 120.52943294, 0.0009561, 144.79191961, 0.01474108, 14.47919196, 0.04385091, -120.52943294, -0.0009561, -144.79191961, -0.01474108, -14.47919196, -0.04385091, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 145.21706507, 0.01912205, 145.21706507, 0.05736616, 101.65194555, -1744.73186167, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 36.30426627, 8.123e-05, 108.9127988, 0.00024368, 363.04266268, 0.00081226, -36.30426627, -8.123e-05, -108.9127988, -0.00024368, -363.04266268, -0.00081226, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 145.21706507, 0.01912205, 145.21706507, 0.05736616, 101.65194555, -1744.73186167, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 36.30426627, 8.123e-05, 108.9127988, 0.00024368, 363.04266268, 0.00081226, -36.30426627, -8.123e-05, -108.9127988, -0.00024368, -363.04266268, -0.00081226, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.15, 7.7, 3.55)
    ops.node(122011, 8.15, 7.7, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 28763916.87455272, 11984965.36439697, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 183.67677196, 0.00089478, 220.80559883, 0.01206022, 22.08055988, 0.03349909, -183.67677196, -0.00089478, -220.80559883, -0.01206022, -22.08055988, -0.03349909, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 183.67677196, 0.00089478, 220.80559883, 0.01206022, 22.08055988, 0.03349909, -183.67677196, -0.00089478, -220.80559883, -0.01206022, -22.08055988, -0.03349909, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 163.00642377, 0.01789557, 163.00642377, 0.05368671, 114.10449664, -1692.64424204, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 40.75160594, 7.14e-05, 122.25481783, 0.00021421, 407.51605943, 0.00071405, -40.75160594, -7.14e-05, -122.25481783, -0.00021421, -407.51605943, -0.00071405, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 163.00642377, 0.01789557, 163.00642377, 0.05368671, 114.10449664, -1692.64424204, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 40.75160594, 7.14e-05, 122.25481783, 0.00021421, 407.51605943, 0.00071405, -40.75160594, -7.14e-05, -122.25481783, -0.00021421, -407.51605943, -0.00071405, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 13.45, 7.7, 3.55)
    ops.node(122012, 13.45, 7.7, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.09, 29813771.69456388, 12422404.87273495, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 101.74295827, 0.00113553, 121.61426552, 0.01473727, 12.16142655, 0.04368162, -101.74295827, -0.00113553, -121.61426552, -0.01473727, -12.16142655, -0.04368162, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 96.85376073, 0.00113553, 115.77016409, 0.01473727, 11.57701641, 0.04368162, -96.85376073, -0.00113553, -115.77016409, -0.01473727, -11.57701641, -0.04368162, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 119.28571186, 0.02271052, 119.28571186, 0.06813156, 83.4999983, -1525.65118507, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 29.82142797, 8.962e-05, 89.4642839, 0.00026887, 298.21427965, 0.00089623, -29.82142797, -8.962e-05, -89.4642839, -0.00026887, -298.21427965, -0.00089623, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 119.28571186, 0.02271052, 119.28571186, 0.06813156, 83.4999983, -1525.65118507, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 29.82142797, 8.962e-05, 89.4642839, 0.00026887, 298.21427965, 0.00089623, -29.82142797, -8.962e-05, -89.4642839, -0.00026887, -298.21427965, -0.00089623, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 11.55, 3.55)
    ops.node(122013, 0.0, 11.55, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0625, 29456380.08809245, 12273491.70337186, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 51.31992253, 0.00128864, 61.41844221, 0.01538729, 6.14184422, 0.05388329, -51.31992253, -0.00128864, -61.41844221, -0.01538729, -6.14184422, -0.05388329, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 54.95330633, 0.00128864, 65.76678809, 0.01538729, 6.57667881, 0.05388329, -54.95330633, -0.00128864, -65.76678809, -0.01538729, -6.57667881, -0.05388329, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 93.06156992, 0.0257728, 93.06156992, 0.07731841, 65.14309894, -1375.27199938, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 23.26539248, 0.00010191, 69.79617744, 0.00030572, 232.65392479, 0.00101906, -23.26539248, -0.00010191, -69.79617744, -0.00030572, -232.65392479, -0.00101906, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 93.06156992, 0.0257728, 93.06156992, 0.07731841, 65.14309894, -1375.27199938, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 23.26539248, 0.00010191, 69.79617744, 0.00030572, 232.65392479, 0.00101906, -23.26539248, -0.00010191, -69.79617744, -0.00030572, -232.65392479, -0.00101906, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 2.85, 11.55, 3.55)
    ops.node(122014, 2.85, 11.55, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.1225, 29505534.20344594, 12293972.58476914, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 125.36698457, 0.0009509, 150.58889435, 0.01455242, 15.05888943, 0.0437833, -125.36698457, -0.0009509, -150.58889435, -0.01455242, -15.05888943, -0.0437833, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 119.32287821, 0.0009509, 143.32880671, 0.01455242, 14.33288067, 0.0437833, -119.32287821, -0.0009509, -143.32880671, -0.01455242, -14.33288067, -0.0437833, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 145.45572563, 0.0190179, 145.45572563, 0.05705371, 101.81900794, -1742.47189377, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 36.36393141, 8.113e-05, 109.09179422, 0.00024339, 363.63931408, 0.0008113, -36.36393141, -8.113e-05, -109.09179422, -0.00024339, -363.63931408, -0.0008113, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 145.45572563, 0.0190179, 145.45572563, 0.05705371, 101.81900794, -1742.47189377, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 36.36393141, 8.113e-05, 109.09179422, 0.00024339, 363.63931408, 0.0008113, -36.36393141, -8.113e-05, -109.09179422, -0.00024339, -363.63931408, -0.0008113, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 8.15, 11.55, 3.55)
    ops.node(122015, 8.15, 11.55, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.16, 29240689.8067724, 12183620.75282183, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 182.54372227, 0.000876, 219.34574181, 0.01277871, 21.93457418, 0.03476945, -182.54372227, -0.000876, -219.34574181, -0.01277871, -21.93457418, -0.03476945, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 182.54372227, 0.000876, 219.34574181, 0.01277871, 21.93457418, 0.03476945, -182.54372227, -0.000876, -219.34574181, -0.01277871, -21.93457418, -0.03476945, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 166.35855813, 0.01752002, 166.35855813, 0.05256007, 116.45099069, -1714.94668227, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 41.58963953, 7.168e-05, 124.7689186, 0.00021505, 415.89639533, 0.00071685, -41.58963953, -7.168e-05, -124.7689186, -0.00021505, -415.89639533, -0.00071685, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 166.35855813, 0.01752002, 166.35855813, 0.05256007, 116.45099069, -1714.94668227, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 41.58963953, 7.168e-05, 124.7689186, 0.00021505, 415.89639533, 0.00071685, -41.58963953, -7.168e-05, -124.7689186, -0.00021505, -415.89639533, -0.00071685, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 13.45, 11.55, 3.55)
    ops.node(122016, 13.45, 11.55, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.09, 30227655.90669308, 12594856.62778878, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 115.16319576, 0.00107952, 137.6034766, 0.01530523, 13.76034766, 0.04932337, -115.16319576, -0.00107952, -137.6034766, -0.01530523, -13.76034766, -0.04932337, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 104.39789395, 0.00107952, 124.74048728, 0.01530523, 12.47404873, 0.04932337, -104.39789395, -0.00107952, -124.74048728, -0.01530523, -12.47404873, -0.04932337, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 130.3424184, 0.02159035, 130.3424184, 0.06477106, 91.23969288, -1788.06634769, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 32.5856046, 9.659e-05, 97.7568138, 0.00028977, 325.856046, 0.00096589, -32.5856046, -9.659e-05, -97.7568138, -0.00028977, -325.856046, -0.00096589, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 130.3424184, 0.02159035, 130.3424184, 0.06477106, 91.23969288, -1788.06634769, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 32.5856046, 9.659e-05, 97.7568138, 0.00028977, 325.856046, 0.00096589, -32.5856046, -9.659e-05, -97.7568138, -0.00028977, -325.856046, -0.00096589, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 15.4, 3.55)
    ops.node(122017, 0.0, 15.4, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.0625, 29673107.50280973, 12363794.79283739, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 51.04740878, 0.00130809, 61.08197297, 0.0159001, 6.1081973, 0.05491373, -51.04740878, -0.00130809, -61.08197297, -0.0159001, -6.1081973, -0.05491373, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 54.46932434, 0.00130809, 65.1765462, 0.0159001, 6.51765462, 0.05491373, -54.46932434, -0.00130809, -65.1765462, -0.0159001, -6.51765462, -0.05491373, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 95.53332564, 0.02616172, 95.53332564, 0.07848517, 66.87332795, -1436.79726771, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 23.88333141, 0.00010385, 71.64999423, 0.00031155, 238.83331411, 0.00103849, -23.88333141, -0.00010385, -71.64999423, -0.00031155, -238.83331411, -0.00103849, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 95.53332564, 0.02616172, 95.53332564, 0.07848517, 66.87332795, -1436.79726771, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 23.88333141, 0.00010385, 71.64999423, 0.00031155, 238.83331411, 0.00103849, -23.88333141, -0.00010385, -71.64999423, -0.00031155, -238.83331411, -0.00103849, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 2.85, 15.4, 3.55)
    ops.node(122018, 2.85, 15.4, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.1225, 28635075.94096793, 11931281.64206997, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 132.92217982, 0.00096528, 159.79755678, 0.01500509, 15.97975568, 0.0429179, -132.92217982, -0.00096528, -159.79755678, -0.01500509, -15.97975568, -0.0429179, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 122.74063263, 0.00096528, 147.55741471, 0.01500509, 14.75574147, 0.0429179, -122.74063263, -0.00096528, -147.55741471, -0.01500509, -14.75574147, -0.0429179, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 142.13958203, 0.01930565, 142.13958203, 0.05791694, 99.49770742, -1743.5906087, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 35.53489551, 8.169e-05, 106.60468652, 0.00024507, 355.34895507, 0.0008169, -35.53489551, -8.169e-05, -106.60468652, -0.00024507, -355.34895507, -0.0008169, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 142.13958203, 0.01930565, 142.13958203, 0.05791694, 99.49770742, -1743.5906087, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 35.53489551, 8.169e-05, 106.60468652, 0.00024507, 355.34895507, 0.0008169, -35.53489551, -8.169e-05, -106.60468652, -0.00024507, -355.34895507, -0.0008169, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 8.15, 15.4, 3.55)
    ops.node(122019, 8.15, 15.4, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.16, 29963530.92484351, 12484804.55201813, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 183.46372501, 0.00089099, 220.25700808, 0.01235577, 22.02570081, 0.03513606, -183.46372501, -0.00089099, -220.25700808, -0.01235577, -22.02570081, -0.03513606, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 183.46372501, 0.00089099, 220.25700808, 0.01235577, 22.02570081, 0.03513606, -183.46372501, -0.00089099, -220.25700808, -0.01235577, -22.02570081, -0.03513606, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 169.73326963, 0.01781976, 169.73326963, 0.05345928, 118.81328874, -1707.98225797, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 42.43331741, 7.137e-05, 127.29995222, 0.00021412, 424.33317408, 0.00071375, -42.43331741, -7.137e-05, -127.29995222, -0.00021412, -424.33317408, -0.00071375, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 169.73326963, 0.01781976, 169.73326963, 0.05345928, 118.81328874, -1707.98225797, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 42.43331741, 7.137e-05, 127.29995222, 0.00021412, 424.33317408, 0.00071375, -42.43331741, -7.137e-05, -127.29995222, -0.00021412, -424.33317408, -0.00071375, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 13.45, 15.4, 3.55)
    ops.node(122020, 13.45, 15.4, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.09, 31136101.84242232, 12973375.76767597, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 102.16563787, 0.00107792, 121.93456979, 0.01494494, 12.19345698, 0.04615407, -102.16563787, -0.00107792, -121.93456979, -0.01494494, -12.19345698, -0.04615407, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 97.091208, 0.00107792, 115.87824365, 0.01494494, 11.58782436, 0.04615407, -97.091208, -0.00107792, -115.87824365, -0.01494494, -11.58782436, -0.04615407, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 123.27907967, 0.02155837, 123.27907967, 0.06467512, 86.29535577, -1526.3805573, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 30.81976992, 8.869e-05, 92.45930975, 0.00026607, 308.19769918, 0.0008869, -30.81976992, -8.869e-05, -92.45930975, -0.00026607, -308.19769918, -0.0008869, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 123.27907967, 0.02155837, 123.27907967, 0.06467512, 86.29535577, -1526.3805573, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 30.81976992, 8.869e-05, 92.45930975, 0.00026607, 308.19769918, 0.0008869, -30.81976992, -8.869e-05, -92.45930975, -0.00026607, -308.19769918, -0.0008869, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 0.0, 19.25, 3.6)
    ops.node(122021, 0.0, 19.25, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.0625, 29493935.56057769, 12289139.81690737, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 43.23293382, 0.00121286, 52.07975773, 0.01716021, 5.20797577, 0.06409461, -43.23293382, -0.00121286, -52.07975773, -0.01716021, -5.20797577, -0.06409461, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 46.83214924, 0.00121286, 56.41548632, 0.01716021, 5.64154863, 0.06409461, -46.83214924, -0.00121286, -56.41548632, -0.01716021, -5.64154863, -0.06409461, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 88.83175113, 0.02425717, 88.83175113, 0.07277152, 62.18222579, -1443.96505071, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 22.20793778, 9.715e-05, 66.62381334, 0.00029145, 222.07937782, 0.00097151, -22.20793778, -9.715e-05, -66.62381334, -0.00029145, -222.07937782, -0.00097151, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 88.83175113, 0.02425717, 88.83175113, 0.07277152, 62.18222579, -1443.96505071, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 22.20793778, 9.715e-05, 66.62381334, 0.00029145, 222.07937782, 0.00097151, -22.20793778, -9.715e-05, -66.62381334, -0.00029145, -222.07937782, -0.00097151, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 2.85, 19.25, 3.6)
    ops.node(122022, 2.85, 19.25, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.09, 30597044.86677891, 12748768.69449121, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 77.23633817, 0.00102233, 92.50221037, 0.01510735, 9.25022104, 0.05282164, -77.23633817, -0.00102233, -92.50221037, -0.01510735, -9.25022104, -0.05282164, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 72.38294753, 0.00102233, 86.68954015, 0.01510735, 8.66895401, 0.05282164, -72.38294753, -0.00102233, -86.68954015, -0.01510735, -8.66895401, -0.05282164, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 127.16383563, 0.0204465, 127.16383563, 0.0613395, 89.01468494, -1733.01730507, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 31.79095891, 9.31e-05, 95.37287672, 0.00027929, 317.90958908, 0.00093096, -31.79095891, -9.31e-05, -95.37287672, -0.00027929, -317.90958908, -0.00093096, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 127.16383563, 0.0204465, 127.16383563, 0.0613395, 89.01468494, -1733.01730507, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 31.79095891, 9.31e-05, 95.37287672, 0.00027929, 317.90958908, 0.00093096, -31.79095891, -9.31e-05, -95.37287672, -0.00027929, -317.90958908, -0.00093096, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 8.15, 19.25, 3.6)
    ops.node(122023, 8.15, 19.25, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.1225, 29135056.63365114, 12139606.93068798, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 121.00482387, 0.00089944, 145.3069984, 0.01419596, 14.53069984, 0.04621504, -121.00482387, -0.00089944, -145.3069984, -0.01419596, -14.53069984, -0.04621504, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 108.04172772, 0.00089944, 129.74044055, 0.01419596, 12.97404405, 0.04621504, -108.04172772, -0.00089944, -129.74044055, -0.01419596, -12.97404405, -0.04621504, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 155.125976, 0.01798882, 155.125976, 0.05396646, 108.5881832, -2033.66445646, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 38.781494, 8.762e-05, 116.344482, 0.00026287, 387.81494, 0.00087624, -38.781494, -8.762e-05, -116.344482, -0.00026287, -387.81494, -0.00087624, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 155.125976, 0.01798882, 155.125976, 0.05396646, 108.5881832, -2033.66445646, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 38.781494, 8.762e-05, 116.344482, 0.00026287, 387.81494, 0.00087624, -38.781494, -8.762e-05, -116.344482, -0.00026287, -387.81494, -0.00087624, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 13.45, 19.25, 3.6)
    ops.node(122024, 13.45, 19.25, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.0625, 29643926.87312956, 12351636.19713732, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 46.28138017, 0.00127703, 55.37796287, 0.0153289, 5.53779629, 0.05422211, -46.28138017, -0.00127703, -55.37796287, -0.0153289, -5.53779629, -0.05422211, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 46.28138017, 0.00127703, 55.37796287, 0.0153289, 5.53779629, 0.05422211, -46.28138017, -0.00127703, -55.37796287, -0.0153289, -5.53779629, -0.05422211, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 94.99856383, 0.02554065, 94.99856383, 0.07662196, 66.49899468, -1421.38521118, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 23.74964096, 0.00010337, 71.24892287, 0.00031011, 237.49640957, 0.00103369, -23.74964096, -0.00010337, -71.24892287, -0.00031011, -237.49640957, -0.00103369, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 94.99856383, 0.02554065, 94.99856383, 0.07662196, 66.49899468, -1421.38521118, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 23.74964096, 0.00010337, 71.24892287, 0.00031011, 237.49640957, 0.00103369, -23.74964096, -0.00010337, -71.24892287, -0.00031011, -237.49640957, -0.00103369, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.15, 0.0, 6.4)
    ops.node(123003, 8.15, 0.0, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0625, 29332768.68434987, 12221986.95181245, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 46.75773444, 0.00126362, 55.92172772, 0.01480971, 5.59217277, 0.05216941, -46.75773444, -0.00126362, -55.92172772, -0.01480971, -5.59217277, -0.05216941, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 46.75773444, 0.00126362, 55.92172772, 0.01480971, 5.59217277, 0.05216941, -46.75773444, -0.00126362, -55.92172772, -0.01480971, -5.59217277, -0.05216941, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 94.03106607, 0.02527234, 94.03106607, 0.07581703, 65.82174625, -1398.96381904, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 23.50776652, 0.0001034, 70.52329955, 0.00031021, 235.07766517, 0.00103402, -23.50776652, -0.0001034, -70.52329955, -0.00031021, -235.07766517, -0.00103402, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 94.03106607, 0.02527234, 94.03106607, 0.07581703, 65.82174625, -1398.96381904, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 23.50776652, 0.0001034, 70.52329955, 0.00031021, 235.07766517, 0.00103402, -23.50776652, -0.0001034, -70.52329955, -0.00031021, -235.07766517, -0.00103402, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.45, 0.0, 6.4)
    ops.node(123004, 13.45, 0.0, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 29353371.1610828, 12230571.31711783, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 37.07202739, 0.00120022, 44.6809584, 0.01711749, 4.46809584, 0.06421317, -37.07202739, -0.00120022, -44.6809584, -0.01711749, -4.46809584, -0.06421317, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 37.07202739, 0.00120022, 44.6809584, 0.01711749, 4.46809584, 0.06421317, -37.07202739, -0.00120022, -44.6809584, -0.01711749, -4.46809584, -0.06421317, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 88.6917485, 0.02400442, 88.6917485, 0.07201327, 62.08422395, -1465.88218503, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 22.17293713, 9.746e-05, 66.51881138, 0.00029239, 221.72937126, 0.00097462, -22.17293713, -9.746e-05, -66.51881138, -0.00029239, -221.72937126, -0.00097462, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 88.6917485, 0.02400442, 88.6917485, 0.07201327, 62.08422395, -1465.88218503, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 22.17293713, 9.746e-05, 66.51881138, 0.00029239, 221.72937126, 0.00097462, -22.17293713, -9.746e-05, -66.51881138, -0.00029239, -221.72937126, -0.00097462, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 3.85, 6.35)
    ops.node(123005, 0.0, 3.85, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 30174667.91990622, 12572778.29996092, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 37.88715871, 0.00119459, 45.56047372, 0.01633475, 4.55604737, 0.06359867, -37.88715871, -0.00119459, -45.56047372, -0.01633475, -4.55604737, -0.06359867, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 37.88715871, 0.00119459, 45.56047372, 0.01633475, 4.55604737, 0.06359867, -37.88715871, -0.00119459, -45.56047372, -0.01633475, -4.55604737, -0.06359867, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 89.48111456, 0.02389171, 89.48111456, 0.07167513, 62.63678019, -1384.34952829, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 22.37027864, 9.565e-05, 67.11083592, 0.00028696, 223.70278641, 0.00095653, -22.37027864, -9.565e-05, -67.11083592, -0.00028696, -223.70278641, -0.00095653, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 89.48111456, 0.02389171, 89.48111456, 0.07167513, 62.63678019, -1384.34952829, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 22.37027864, 9.565e-05, 67.11083592, 0.00028696, 223.70278641, 0.00095653, -22.37027864, -9.565e-05, -67.11083592, -0.00028696, -223.70278641, -0.00095653, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 2.85, 3.85, 6.35)
    ops.node(123006, 2.85, 3.85, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1225, 29573095.02816795, 12322122.92840331, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 124.53595081, 0.00097631, 150.09976264, 0.01392791, 15.00997626, 0.04080452, -124.53595081, -0.00097631, -150.09976264, -0.01392791, -15.00997626, -0.04080452, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 124.53595081, 0.00097631, 150.09976264, 0.01392791, 15.00997626, 0.04080452, -124.53595081, -0.00097631, -150.09976264, -0.01392791, -15.00997626, -0.04080452, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 127.07381075, 0.01952615, 127.07381075, 0.05857844, 88.95166752, -1323.4894654, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 31.76845269, 7.072e-05, 95.30535806, 0.00021215, 317.68452687, 0.00070715, -31.76845269, -7.072e-05, -95.30535806, -0.00021215, -317.68452687, -0.00070715, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 127.07381075, 0.01952615, 127.07381075, 0.05857844, 88.95166752, -1323.4894654, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 31.76845269, 7.072e-05, 95.30535806, 0.00021215, 317.68452687, 0.00070715, -31.76845269, -7.072e-05, -95.30535806, -0.00021215, -317.68452687, -0.00070715, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 8.15, 3.85, 6.35)
    ops.node(123007, 8.15, 3.85, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 31020624.39152125, 12925260.16313385, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 134.64649828, 0.00096902, 161.60227412, 0.01324977, 16.16022741, 0.04024307, -134.64649828, -0.00096902, -161.60227412, -0.01324977, -16.16022741, -0.04024307, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 134.64649828, 0.00096902, 161.60227412, 0.01324977, 16.16022741, 0.04024307, -134.64649828, -0.00096902, -161.60227412, -0.01324977, -16.16022741, -0.04024307, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 135.67917429, 0.01938046, 135.67917429, 0.05814137, 94.975422, -1365.00772823, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 33.91979357, 7.198e-05, 101.75938072, 0.00021594, 339.19793573, 0.00071981, -33.91979357, -7.198e-05, -101.75938072, -0.00021594, -339.19793573, -0.00071981, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 135.67917429, 0.01938046, 135.67917429, 0.05814137, 94.975422, -1365.00772823, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 33.91979357, 7.198e-05, 101.75938072, 0.00021594, 339.19793573, 0.00071981, -33.91979357, -7.198e-05, -101.75938072, -0.00021594, -339.19793573, -0.00071981, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 13.45, 3.85, 6.35)
    ops.node(123008, 13.45, 3.85, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 29592332.04092986, 12330138.35038744, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 60.89723039, 0.00132345, 72.90222057, 0.01672751, 7.29022206, 0.05079272, -60.89723039, -0.00132345, -72.90222057, -0.01672751, -7.29022206, -0.05079272, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 60.89723039, 0.00132345, 72.90222057, 0.01672751, 7.29022206, 0.05079272, -60.89723039, -0.00132345, -72.90222057, -0.01672751, -7.29022206, -0.05079272, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 86.40409453, 0.02646892, 86.40409453, 0.07940677, 60.48286617, -1219.98423227, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 21.60102363, 9.418e-05, 64.8030709, 0.00028254, 216.01023634, 0.00094182, -21.60102363, -9.418e-05, -64.8030709, -0.00028254, -216.01023634, -0.00094182, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 86.40409453, 0.02646892, 86.40409453, 0.07940677, 60.48286617, -1219.98423227, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 21.60102363, 9.418e-05, 64.8030709, 0.00028254, 216.01023634, 0.00094182, -21.60102363, -9.418e-05, -64.8030709, -0.00028254, -216.01023634, -0.00094182, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 7.7, 6.35)
    ops.node(123009, 0.0, 7.7, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 28288363.00231304, 11786817.91763043, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 36.88249799, 0.00119151, 44.51140665, 0.01688836, 4.45114067, 0.06187808, -36.88249799, -0.00119151, -44.51140665, -0.01688836, -4.45114067, -0.06187808, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 36.88249799, 0.00119151, 44.51140665, 0.01688836, 4.45114067, 0.06187808, -36.88249799, -0.00119151, -44.51140665, -0.01688836, -4.45114067, -0.06187808, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 86.52584271, 0.02383027, 86.52584271, 0.07149082, 60.5680899, -1461.42517748, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 21.63146068, 9.866e-05, 64.89438203, 0.00029599, 216.31460677, 0.00098662, -21.63146068, -9.866e-05, -64.89438203, -0.00029599, -216.31460677, -0.00098662, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 86.52584271, 0.02383027, 86.52584271, 0.07149082, 60.5680899, -1461.42517748, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 21.63146068, 9.866e-05, 64.89438203, 0.00029599, 216.31460677, 0.00098662, -21.63146068, -9.866e-05, -64.89438203, -0.00029599, -216.31460677, -0.00098662, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 2.85, 7.7, 6.35)
    ops.node(123010, 2.85, 7.7, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0625, 29193245.06808516, 12163852.11170215, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 61.10522578, 0.00141141, 73.07244178, 0.0153874, 7.30724418, 0.04729156, -61.10522578, -0.00141141, -73.07244178, -0.0153874, -7.30724418, -0.04729156, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 61.10522578, 0.00141141, 73.07244178, 0.0153874, 7.30724418, 0.04729156, -61.10522578, -0.00141141, -73.07244178, -0.0153874, -7.30724418, -0.04729156, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 83.19076244, 0.02822816, 83.19076244, 0.08468447, 58.23353371, -1208.40336503, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 20.79769061, 9.192e-05, 62.39307183, 0.00027576, 207.97690611, 0.00091919, -20.79769061, -9.192e-05, -62.39307183, -0.00027576, -207.97690611, -0.00091919, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 83.19076244, 0.02822816, 83.19076244, 0.08468447, 58.23353371, -1208.40336503, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 20.79769061, 9.192e-05, 62.39307183, 0.00027576, 207.97690611, 0.00091919, -20.79769061, -9.192e-05, -62.39307183, -0.00027576, -207.97690611, -0.00091919, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.15, 7.7, 6.35)
    ops.node(123011, 8.15, 7.7, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 30428713.35648407, 12678630.5652017, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 132.26891213, 0.00098528, 158.92561307, 0.01323373, 15.89256131, 0.03964575, -132.26891213, -0.00098528, -158.92561307, -0.01323373, -15.89256131, -0.03964575, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 132.26891213, 0.00098528, 158.92561307, 0.01323373, 15.89256131, 0.03964575, -132.26891213, -0.00098528, -158.92561307, -0.01323373, -15.89256131, -0.03964575, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 132.8127485, 0.01970562, 132.8127485, 0.05911685, 92.96892395, -1351.07580896, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 33.20318712, 7.183e-05, 99.60956137, 0.00021549, 332.03187124, 0.00071831, -33.20318712, -7.183e-05, -99.60956137, -0.00021549, -332.03187124, -0.00071831, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 132.8127485, 0.01970562, 132.8127485, 0.05911685, 92.96892395, -1351.07580896, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 33.20318712, 7.183e-05, 99.60956137, 0.00021549, 332.03187124, 0.00071831, -33.20318712, -7.183e-05, -99.60956137, -0.00021549, -332.03187124, -0.00071831, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 13.45, 7.7, 6.35)
    ops.node(123012, 13.45, 7.7, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 29284838.15243782, 12202015.89684909, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 59.90499194, 0.00133035, 71.73113418, 0.01574629, 7.17311342, 0.04917439, -59.90499194, -0.00133035, -71.73113418, -0.01574629, -7.17311342, -0.04917439, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 59.90499194, 0.00133035, 71.73113418, 0.01574629, 7.17311342, 0.04917439, -59.90499194, -0.00133035, -71.73113418, -0.01574629, -7.17311342, -0.04917439, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 83.28245568, 0.02660695, 83.28245568, 0.07982085, 58.29771898, -1226.23078123, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 20.82061392, 9.173e-05, 62.46184176, 0.0002752, 208.20613921, 0.00091732, -20.82061392, -9.173e-05, -62.46184176, -0.0002752, -208.20613921, -0.00091732, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 83.28245568, 0.02660695, 83.28245568, 0.07982085, 58.29771898, -1226.23078123, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 20.82061392, 9.173e-05, 62.46184176, 0.0002752, 208.20613921, 0.00091732, -20.82061392, -9.173e-05, -62.46184176, -0.0002752, -208.20613921, -0.00091732, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 11.55, 6.35)
    ops.node(123013, 0.0, 11.55, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 27840061.29149565, 11600025.53812319, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 36.60000776, 0.00121913, 44.1882196, 0.01691885, 4.41882196, 0.06094123, -36.60000776, -0.00121913, -44.1882196, -0.01691885, -4.41882196, -0.06094123, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 36.60000776, 0.00121913, 44.1882196, 0.01691885, 4.41882196, 0.06094123, -36.60000776, -0.00121913, -44.1882196, -0.01691885, -4.41882196, -0.06094123, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 85.42151346, 0.02438255, 85.42151346, 0.07314765, 59.79505942, -1451.34619509, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 21.35537837, 9.897e-05, 64.0661351, 0.00029691, 213.55378366, 0.00098971, -21.35537837, -9.897e-05, -64.0661351, -0.00029691, -213.55378366, -0.00098971, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 85.42151346, 0.02438255, 85.42151346, 0.07314765, 59.79505942, -1451.34619509, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 21.35537837, 9.897e-05, 64.0661351, 0.00029691, 213.55378366, 0.00098971, -21.35537837, -9.897e-05, -64.0661351, -0.00029691, -213.55378366, -0.00098971, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 2.85, 11.55, 6.35)
    ops.node(123014, 2.85, 11.55, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 28895389.69429726, 12039745.70595719, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 60.86443752, 0.00136238, 72.7929189, 0.0157385, 7.27929189, 0.04698562, -60.86443752, -0.00136238, -72.7929189, -0.0157385, -7.27929189, -0.04698562, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 60.86443752, 0.00136238, 72.7929189, 0.0157385, 7.27929189, 0.04698562, -60.86443752, -0.00136238, -72.7929189, -0.0157385, -7.27929189, -0.04698562, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 86.85821873, 0.02724767, 86.85821873, 0.08174301, 60.80075311, -1247.25227841, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 21.71455468, 9.696e-05, 65.14366405, 0.00029088, 217.14554682, 0.0009696, -21.71455468, -9.696e-05, -65.14366405, -0.00029088, -217.14554682, -0.0009696, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 86.85821873, 0.02724767, 86.85821873, 0.08174301, 60.80075311, -1247.25227841, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 21.71455468, 9.696e-05, 65.14366405, 0.00029088, 217.14554682, 0.0009696, -21.71455468, -9.696e-05, -65.14366405, -0.00029088, -217.14554682, -0.0009696, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 8.15, 11.55, 6.35)
    ops.node(123015, 8.15, 11.55, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 28198308.26073333, 11749295.10863889, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 134.14090255, 0.00100995, 161.63321824, 0.01336632, 16.16332182, 0.03723878, -134.14090255, -0.00100995, -161.63321824, -0.01336632, -16.16332182, -0.03723878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 134.14090255, 0.00100995, 161.63321824, 0.01336632, 16.16332182, 0.03723878, -134.14090255, -0.00100995, -161.63321824, -0.01336632, -16.16332182, -0.03723878, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 124.53192591, 0.02019908, 124.53192591, 0.06059724, 87.17234814, -1357.22868414, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 31.13298148, 7.268e-05, 93.39894443, 0.00021804, 311.32981478, 0.0007268, -31.13298148, -7.268e-05, -93.39894443, -0.00021804, -311.32981478, -0.0007268, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 124.53192591, 0.02019908, 124.53192591, 0.06059724, 87.17234814, -1357.22868414, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 31.13298148, 7.268e-05, 93.39894443, 0.00021804, 311.32981478, 0.0007268, -31.13298148, -7.268e-05, -93.39894443, -0.00021804, -311.32981478, -0.0007268, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 13.45, 11.55, 6.35)
    ops.node(123016, 13.45, 11.55, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 31794396.62053964, 13247665.25855818, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 45.70177166, 0.00123373, 54.54486997, 0.01578348, 5.454487, 0.05979233, -45.70177166, -0.00123373, -54.54486997, -0.01578348, -5.454487, -0.05979233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 45.70177166, 0.00123373, 54.54486997, 0.01578348, 5.454487, 0.05979233, -45.70177166, -0.00123373, -54.54486997, -0.01578348, -5.454487, -0.05979233, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 100.02229242, 0.02467461, 100.02229242, 0.07402384, 70.0156047, -1448.47978346, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 25.00557311, 0.00010147, 75.01671932, 0.00030442, 250.05573106, 0.00101474, -25.00557311, -0.00010147, -75.01671932, -0.00030442, -250.05573106, -0.00101474, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 100.02229242, 0.02467461, 100.02229242, 0.07402384, 70.0156047, -1448.47978346, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 25.00557311, 0.00010147, 75.01671932, 0.00030442, 250.05573106, 0.00101474, -25.00557311, -0.00010147, -75.01671932, -0.00030442, -250.05573106, -0.00101474, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 15.4, 6.35)
    ops.node(123017, 0.0, 15.4, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 31213971.14753272, 13005821.31147197, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 37.33507228, 0.00115872, 44.84468704, 0.01641653, 4.4844687, 0.06669536, -37.33507228, -0.00115872, -44.84468704, -0.01641653, -4.4844687, -0.06669536, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 37.33507228, 0.00115872, 44.84468704, 0.01641653, 4.4844687, 0.06669536, -37.33507228, -0.00115872, -44.84468704, -0.01641653, -4.4844687, -0.06669536, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 90.2996241, 0.02317431, 90.2996241, 0.06952294, 63.20973687, -1387.72557674, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 22.57490603, 9.331e-05, 67.72471808, 0.00027994, 225.74906026, 0.00093314, -22.57490603, -9.331e-05, -67.72471808, -0.00027994, -225.74906026, -0.00093314, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 90.2996241, 0.02317431, 90.2996241, 0.06952294, 63.20973687, -1387.72557674, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 22.57490603, 9.331e-05, 67.72471808, 0.00027994, 225.74906026, 0.00093314, -22.57490603, -9.331e-05, -67.72471808, -0.00027994, -225.74906026, -0.00093314, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 2.85, 15.4, 6.35)
    ops.node(123018, 2.85, 15.4, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 30248916.66944319, 12603715.27893466, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 60.94036215, 0.0013101, 72.81684031, 0.01630603, 7.28168403, 0.05041492, -60.94036215, -0.0013101, -72.81684031, -0.01630603, -7.28168403, -0.05041492, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 60.94036215, 0.0013101, 72.81684031, 0.01630603, 7.28168403, 0.05041492, -60.94036215, -0.0013101, -72.81684031, -0.01630603, -7.28168403, -0.05041492, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 83.70499771, 0.0262019, 83.70499771, 0.07860571, 58.5934984, -1182.37805188, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 20.92624943, 8.926e-05, 62.77874828, 0.00026778, 209.26249427, 0.00089259, -20.92624943, -8.926e-05, -62.77874828, -0.00026778, -209.26249427, -0.00089259, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 83.70499771, 0.0262019, 83.70499771, 0.07860571, 58.5934984, -1182.37805188, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 20.92624943, 8.926e-05, 62.77874828, 0.00026778, 209.26249427, 0.00089259, -20.92624943, -8.926e-05, -62.77874828, -0.00026778, -209.26249427, -0.00089259, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 8.15, 15.4, 6.35)
    ops.node(123019, 8.15, 15.4, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1225, 29723133.21736702, 12384638.84056959, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 132.74611476, 0.00096806, 159.68035052, 0.01336854, 15.96803505, 0.03903923, -132.74611476, -0.00096806, -159.68035052, -0.01336854, -15.96803505, -0.03903923, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 132.74611476, 0.00096806, 159.68035052, 0.01336854, 15.96803505, 0.03903923, -132.74611476, -0.00096806, -159.68035052, -0.01336854, -15.96803505, -0.03903923, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 130.82868088, 0.01936121, 130.82868088, 0.05808362, 91.58007661, -1370.0450428, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 32.70717022, 7.244e-05, 98.12151066, 0.00021731, 327.07170219, 0.00072437, -32.70717022, -7.244e-05, -98.12151066, -0.00021731, -327.07170219, -0.00072437, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 130.82868088, 0.01936121, 130.82868088, 0.05808362, 91.58007661, -1370.0450428, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 32.70717022, 7.244e-05, 98.12151066, 0.00021731, 327.07170219, 0.00072437, -32.70717022, -7.244e-05, -98.12151066, -0.00021731, -327.07170219, -0.00072437, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 13.45, 15.4, 6.35)
    ops.node(123020, 13.45, 15.4, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 30140039.15801616, 12558349.6491734, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 60.13883687, 0.00135242, 71.95565914, 0.01585797, 7.19556591, 0.05101676, -60.13883687, -0.00135242, -71.95565914, -0.01585797, -7.19556591, -0.05101676, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 60.13883687, 0.00135242, 71.95565914, 0.01585797, 7.19556591, 0.05101676, -60.13883687, -0.00135242, -71.95565914, -0.01585797, -7.19556591, -0.05101676, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 84.09803657, 0.0270483, 84.09803657, 0.08114491, 58.8686256, -1186.16514069, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 21.02450914, 9e-05, 63.07352743, 0.00027001, 210.24509143, 0.00090002, -21.02450914, -9e-05, -63.07352743, -0.00027001, -210.24509143, -0.00090002, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 84.09803657, 0.0270483, 84.09803657, 0.08114491, 58.8686256, -1186.16514069, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 21.02450914, 9e-05, 63.07352743, 0.00027001, 210.24509143, 0.00090002, -21.02450914, -9e-05, -63.07352743, -0.00027001, -210.24509143, -0.00090002, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 0.0, 19.25, 6.4)
    ops.node(123021, 0.0, 19.25, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 28658988.31722701, 11941245.13217792, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 31.23185885, 0.00115477, 37.85475028, 0.0180209, 3.78547503, 0.07067342, -31.23185885, -0.00115477, -37.85475028, -0.0180209, -3.78547503, -0.07067342, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 31.23185885, 0.00115477, 37.85475028, 0.0180209, 3.78547503, 0.07067342, -31.23185885, -0.00115477, -37.85475028, -0.0180209, -3.78547503, -0.07067342, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 82.2150226, 0.02309543, 82.2150226, 0.0692863, 57.55051582, -1615.60733709, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 20.55375565, 9.253e-05, 61.66126695, 0.0002776, 205.53755649, 0.00092534, -20.55375565, -9.253e-05, -61.66126695, -0.0002776, -205.53755649, -0.00092534, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 82.2150226, 0.02309543, 82.2150226, 0.0692863, 57.55051582, -1615.60733709, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 20.55375565, 9.253e-05, 61.66126695, 0.0002776, 205.53755649, 0.00092534, -20.55375565, -9.253e-05, -61.66126695, -0.0002776, -205.53755649, -0.00092534, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 2.85, 19.25, 6.4)
    ops.node(123022, 2.85, 19.25, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0625, 29015982.99376784, 12089992.91406994, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 41.20189073, 0.00122822, 49.50709181, 0.01589629, 4.95070918, 0.05771679, -41.20189073, -0.00122822, -49.50709181, -0.01589629, -4.95070918, -0.05771679, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 41.20189073, 0.00122822, 49.50709181, 0.01589629, 4.95070918, 0.05771679, -41.20189073, -0.00122822, -49.50709181, -0.01589629, -4.95070918, -0.05771679, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 91.21539169, 0.02456437, 91.21539169, 0.07369312, 63.85077419, -1433.51470045, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 22.80384792, 0.0001014, 68.41154377, 0.0003042, 228.03847924, 0.00101401, -22.80384792, -0.0001014, -68.41154377, -0.0003042, -228.03847924, -0.00101401, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 91.21539169, 0.02456437, 91.21539169, 0.07369312, 63.85077419, -1433.51470045, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 22.80384792, 0.0001014, 68.41154377, 0.0003042, 228.03847924, 0.00101401, -22.80384792, -0.0001014, -68.41154377, -0.0003042, -228.03847924, -0.00101401, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 8.15, 19.25, 6.4)
    ops.node(123023, 8.15, 19.25, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.0625, 29547375.95342891, 12311406.64726205, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 47.11707721, 0.00119181, 56.34386614, 0.0155194, 5.63438661, 0.0534059, -47.11707721, -0.00119181, -56.34386614, -0.0155194, -5.63438661, -0.0534059, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 47.11707721, 0.00119181, 56.34386614, 0.0155194, 5.63438661, 0.0534059, -47.11707721, -0.00119181, -56.34386614, -0.0155194, -5.63438661, -0.0534059, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 97.21569643, 0.02383617, 97.21569643, 0.0715085, 68.0509875, -1481.5705596, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 24.30392411, 0.00010613, 72.91177232, 0.00031838, 243.03924107, 0.00106128, -24.30392411, -0.00010613, -72.91177232, -0.00031838, -243.03924107, -0.00106128, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 97.21569643, 0.02383617, 97.21569643, 0.0715085, 68.0509875, -1481.5705596, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 24.30392411, 0.00010613, 72.91177232, 0.00031838, 243.03924107, 0.00106128, -24.30392411, -0.00010613, -72.91177232, -0.00031838, -243.03924107, -0.00106128, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 13.45, 19.25, 6.4)
    ops.node(123024, 13.45, 19.25, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 29170535.41267037, 12154389.75527932, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 36.92177316, 0.00118089, 44.51143736, 0.01702588, 4.45114374, 0.06377427, -36.92177316, -0.00118089, -44.51143736, -0.01702588, -4.45114374, -0.06377427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 36.92177316, 0.00118089, 44.51143736, 0.01702588, 4.45114374, 0.06377427, -36.92177316, -0.00118089, -44.51143736, -0.01702588, -4.45114374, -0.06377427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 88.81401711, 0.02361777, 88.81401711, 0.07085331, 62.16981198, -1484.47824295, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 22.20350428, 9.821e-05, 66.61051283, 0.00029462, 222.03504277, 0.00098208, -22.20350428, -9.821e-05, -66.61051283, -0.00029462, -222.03504277, -0.00098208, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 88.81401711, 0.02361777, 88.81401711, 0.07085331, 62.16981198, -1484.47824295, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 22.20350428, 9.821e-05, 66.61051283, 0.00029462, 222.03504277, 0.00098208, -22.20350428, -9.821e-05, -66.61051283, -0.00029462, -222.03504277, -0.00098208, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.15, 0.0, 9.2)
    ops.node(124003, 8.15, 0.0, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0625, 28037298.35132778, 11682207.64638657, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 30.86183996, 0.00112297, 37.46378246, 0.01811852, 3.74637825, 0.07066322, -30.86183996, -0.00112297, -37.46378246, -0.01811852, -3.74637825, -0.07066322, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 30.86183996, 0.00112297, 37.46378246, 0.01811852, 3.74637825, 0.07066322, -30.86183996, -0.00112297, -37.46378246, -0.01811852, -3.74637825, -0.07066322, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 80.70865802, 0.02245936, 80.70865802, 0.06737809, 56.49606062, -1662.08438205, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 20.17716451, 9.285e-05, 60.53149352, 0.00027856, 201.77164506, 0.00092853, -20.17716451, -9.285e-05, -60.53149352, -0.00027856, -201.77164506, -0.00092853, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 80.70865802, 0.02245936, 80.70865802, 0.06737809, 56.49606062, -1662.08438205, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 20.17716451, 9.285e-05, 60.53149352, 0.00027856, 201.77164506, 0.00092853, -20.17716451, -9.285e-05, -60.53149352, -0.00027856, -201.77164506, -0.00092853, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.45, 0.0, 9.2)
    ops.node(124004, 13.45, 0.0, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 31434178.94242973, 13097574.55934572, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 26.26435799, 0.00107218, 31.73305311, 0.01834041, 3.17330531, 0.07953611, -26.26435799, -0.00107218, -31.73305311, -0.01834041, -3.17330531, -0.07953611, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 26.26435799, 0.00107218, 31.73305311, 0.01834041, 3.17330531, 0.07953611, -26.26435799, -0.00107218, -31.73305311, -0.01834041, -3.17330531, -0.07953611, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 83.13173261, 0.02144363, 83.13173261, 0.06433089, 58.19221283, -2243.66855031, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 20.78293315, 8.531e-05, 62.34879946, 0.00025592, 207.82933153, 0.00085305, -20.78293315, -8.531e-05, -62.34879946, -0.00025592, -207.82933153, -0.00085305, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 83.13173261, 0.02144363, 83.13173261, 0.06433089, 58.19221283, -2243.66855031, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 20.78293315, 8.531e-05, 62.34879946, 0.00025592, 207.82933153, 0.00085305, -20.78293315, -8.531e-05, -62.34879946, -0.00025592, -207.82933153, -0.00085305, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 3.85, 9.175)
    ops.node(124005, 0.0, 3.85, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 29363664.02316358, 12234860.00965149, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 27.77895961, 0.00109348, 33.71835001, 0.01816626, 3.371835, 0.0763757, -27.77895961, -0.00109348, -33.71835001, -0.01816626, -3.371835, -0.0763757, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 27.77895961, 0.00109348, 33.71835001, 0.01816626, 3.371835, 0.0763757, -27.77895961, -0.00109348, -33.71835001, -0.01816626, -3.371835, -0.0763757, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 79.34796972, 0.0218695, 79.34796972, 0.06560851, 55.5435788, -1911.14469702, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 19.83699243, 8.716e-05, 59.51097729, 0.00026149, 198.36992429, 0.00087164, -19.83699243, -8.716e-05, -59.51097729, -0.00026149, -198.36992429, -0.00087164, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 79.34796972, 0.0218695, 79.34796972, 0.06560851, 55.5435788, -1911.14469702, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 19.83699243, 8.716e-05, 59.51097729, 0.00026149, 198.36992429, 0.00087164, -19.83699243, -8.716e-05, -59.51097729, -0.00026149, -198.36992429, -0.00087164, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 2.85, 3.85, 9.175)
    ops.node(124006, 2.85, 3.85, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1225, 29502791.1085671, 12292829.62856962, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 102.22284266, 0.00092387, 123.98933197, 0.01467141, 12.3989332, 0.04694119, -102.22284266, -0.00092387, -123.98933197, -0.01467141, -12.3989332, -0.04694119, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 102.22284266, 0.00092387, 123.98933197, 0.01467141, 12.3989332, 0.04694119, -102.22284266, -0.00092387, -123.98933197, -0.01467141, -12.3989332, -0.04694119, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 111.96833739, 0.01847747, 111.96833739, 0.05543242, 78.37783617, -1223.48574595, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 27.99208435, 6.246e-05, 83.97625304, 0.00018737, 279.92084347, 0.00062458, -27.99208435, -6.246e-05, -83.97625304, -0.00018737, -279.92084347, -0.00062458, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 111.96833739, 0.01847747, 111.96833739, 0.05543242, 78.37783617, -1223.48574595, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 27.99208435, 6.246e-05, 83.97625304, 0.00018737, 279.92084347, 0.00062458, -27.99208435, -6.246e-05, -83.97625304, -0.00018737, -279.92084347, -0.00062458, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 8.15, 3.85, 9.175)
    ops.node(124007, 8.15, 3.85, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 29091600.08226525, 12121500.03427719, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 104.27787179, 0.00094403, 126.45392645, 0.01509407, 12.64539265, 0.04607444, -104.27787179, -0.00094403, -126.45392645, -0.01509407, -12.64539265, -0.04607444, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 104.27787179, 0.00094403, 126.45392645, 0.01509407, 12.64539265, 0.04607444, -104.27787179, -0.00094403, -126.45392645, -0.01509407, -12.64539265, -0.04607444, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 115.36279445, 0.0188806, 115.36279445, 0.05664181, 80.75395612, -1287.57268561, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 28.84069861, 6.526e-05, 86.52209584, 0.00019578, 288.40698613, 0.00065261, -28.84069861, -6.526e-05, -86.52209584, -0.00019578, -288.40698613, -0.00065261, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 115.36279445, 0.0188806, 115.36279445, 0.05664181, 80.75395612, -1287.57268561, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 28.84069861, 6.526e-05, 86.52209584, 0.00019578, 288.40698613, 0.00065261, -28.84069861, -6.526e-05, -86.52209584, -0.00019578, -288.40698613, -0.00065261, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 13.45, 3.85, 9.175)
    ops.node(124008, 13.45, 3.85, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 28929448.73600231, 12053936.9733343, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 44.33686721, 0.00126365, 53.72270579, 0.01977563, 5.37227058, 0.06600742, -44.33686721, -0.00126365, -53.72270579, -0.01977563, -5.37227058, -0.06600742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 44.33686721, 0.00126365, 53.72270579, 0.01977563, 5.37227058, 0.06600742, -44.33686721, -0.00126365, -53.72270579, -0.01977563, -5.37227058, -0.06600742, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 74.64283638, 0.02527305, 74.64283638, 0.07581916, 52.24998547, -1310.79927198, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 18.6607091, 8.323e-05, 55.98212729, 0.00024968, 186.60709096, 0.00083226, -18.6607091, -8.323e-05, -55.98212729, -0.00024968, -186.60709096, -0.00083226, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 74.64283638, 0.02527305, 74.64283638, 0.07581916, 52.24998547, -1310.79927198, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 18.6607091, 8.323e-05, 55.98212729, 0.00024968, 186.60709096, 0.00083226, -18.6607091, -8.323e-05, -55.98212729, -0.00024968, -186.60709096, -0.00083226, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 7.7, 9.175)
    ops.node(124009, 0.0, 7.7, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 29240683.46867206, 12183618.11194669, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 26.65907545, 0.00111337, 32.38753606, 0.01908979, 3.23875361, 0.07823976, -26.65907545, -0.00111337, -32.38753606, -0.01908979, -3.23875361, -0.07823976, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 26.65907545, 0.00111337, 32.38753606, 0.01908979, 3.23875361, 0.07823976, -26.65907545, -0.00111337, -32.38753606, -0.01908979, -3.23875361, -0.07823976, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 81.36570772, 0.02226741, 81.36570772, 0.06680222, 56.95599541, -2298.69353791, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 20.34142693, 8.976e-05, 61.02428079, 0.00026927, 203.41426931, 0.00089756, -20.34142693, -8.976e-05, -61.02428079, -0.00026927, -203.41426931, -0.00089756, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 81.36570772, 0.02226741, 81.36570772, 0.06680222, 56.95599541, -2298.69353791, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 20.34142693, 8.976e-05, 61.02428079, 0.00026927, 203.41426931, 0.00089756, -20.34142693, -8.976e-05, -61.02428079, -0.00026927, -203.41426931, -0.00089756, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 2.85, 7.7, 9.175)
    ops.node(124010, 2.85, 7.7, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0625, 30357664.43954884, 12649026.84981202, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 47.74661352, 0.0012256, 57.58345422, 0.01824139, 5.75834542, 0.063656, -47.74661352, -0.0012256, -57.58345422, -0.01824139, -5.75834542, -0.063656, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 47.74661352, 0.0012256, 57.58345422, 0.01824139, 5.75834542, 0.063656, -47.74661352, -0.0012256, -57.58345422, -0.01824139, -5.75834542, -0.063656, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 78.47919833, 0.024512, 78.47919833, 0.07353599, 54.93543883, -1214.05262959, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 19.61979958, 8.339e-05, 58.85939875, 0.00025016, 196.19799584, 0.00083387, -19.61979958, -8.339e-05, -58.85939875, -0.00025016, -196.19799584, -0.00083387, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 78.47919833, 0.024512, 78.47919833, 0.07353599, 54.93543883, -1214.05262959, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 19.61979958, 8.339e-05, 58.85939875, 0.00025016, 196.19799584, 0.00083387, -19.61979958, -8.339e-05, -58.85939875, -0.00025016, -196.19799584, -0.00083387, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.15, 7.7, 9.175)
    ops.node(124011, 8.15, 7.7, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 30059672.92295786, 12524863.71789911, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 110.98414351, 0.00092078, 134.30415759, 0.01425386, 13.43041576, 0.04585022, -110.98414351, -0.00092078, -134.30415759, -0.01425386, -13.43041576, -0.04585022, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 110.98414351, 0.00092078, 134.30415759, 0.01425386, 13.43041576, 0.04585022, -110.98414351, -0.00092078, -134.30415759, -0.01425386, -13.43041576, -0.04585022, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 116.78537016, 0.01841562, 116.78537016, 0.05524687, 81.74975911, -1212.3162068, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 29.19634254, 6.394e-05, 87.58902762, 0.00019181, 291.96342541, 0.00063938, -29.19634254, -6.394e-05, -87.58902762, -0.00019181, -291.96342541, -0.00063938, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 116.78537016, 0.01841562, 116.78537016, 0.05524687, 81.74975911, -1212.3162068, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 29.19634254, 6.394e-05, 87.58902762, 0.00019181, 291.96342541, 0.00063938, -29.19634254, -6.394e-05, -87.58902762, -0.00019181, -291.96342541, -0.00063938, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 13.45, 7.7, 9.175)
    ops.node(124012, 13.45, 7.7, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 29223038.73213694, 12176266.13839039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 44.93056675, 0.00124857, 54.4120631, 0.01864855, 5.44120631, 0.0652297, -44.93056675, -0.00124857, -54.4120631, -0.01864855, -5.44120631, -0.0652297, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 44.93056675, 0.00124857, 54.4120631, 0.01864855, 5.44120631, 0.0652297, -44.93056675, -0.00124857, -54.4120631, -0.01864855, -5.44120631, -0.0652297, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 72.99384454, 0.02497142, 72.99384454, 0.07491427, 51.09569118, -1279.68194113, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 18.24846113, 8.057e-05, 54.7453834, 0.00024171, 182.48461134, 0.0008057, -18.24846113, -8.057e-05, -54.7453834, -0.00024171, -182.48461134, -0.0008057, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 72.99384454, 0.02497142, 72.99384454, 0.07491427, 51.09569118, -1279.68194113, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 18.24846113, 8.057e-05, 54.7453834, 0.00024171, 182.48461134, 0.0008057, -18.24846113, -8.057e-05, -54.7453834, -0.00024171, -182.48461134, -0.0008057, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 11.55, 9.175)
    ops.node(124013, 0.0, 11.55, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 27588891.6174261, 11495371.50726088, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 26.68501275, 0.00112351, 32.52951466, 0.01939845, 3.25295147, 0.07700291, -26.68501275, -0.00112351, -32.52951466, -0.01939845, -3.25295147, -0.07700291, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 26.68501275, 0.00112351, 32.52951466, 0.01939845, 3.25295147, 0.07700291, -26.68501275, -0.00112351, -32.52951466, -0.01939845, -3.25295147, -0.07700291, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 77.30537305, 0.02247017, 77.30537305, 0.06741052, 54.11376113, -2209.22513301, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 19.32634326, 9.038e-05, 57.97902978, 0.00027115, 193.26343262, 0.00090383, -19.32634326, -9.038e-05, -57.97902978, -0.00027115, -193.26343262, -0.00090383, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 77.30537305, 0.02247017, 77.30537305, 0.06741052, 54.11376113, -2209.22513301, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 19.32634326, 9.038e-05, 57.97902978, 0.00027115, 193.26343262, 0.00090383, -19.32634326, -9.038e-05, -57.97902978, -0.00027115, -193.26343262, -0.00090383, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 2.85, 11.55, 9.175)
    ops.node(124014, 2.85, 11.55, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 30239701.23109622, 12599875.51295676, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 48.12100235, 0.00124402, 58.04938278, 0.01804906, 5.80493828, 0.06331839, -48.12100235, -0.00124402, -58.04938278, -0.01804906, -5.80493828, -0.06331839, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 48.12100235, 0.00124402, 58.04938278, 0.01804906, 5.80493828, 0.06331839, -48.12100235, -0.00124402, -58.04938278, -0.01804906, -5.80493828, -0.06331839, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 77.25353246, 0.02488042, 77.25353246, 0.07464127, 54.07747272, -1212.02223131, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 19.31338312, 8.24e-05, 57.94014935, 0.00024721, 193.13383116, 0.00082405, -19.31338312, -8.24e-05, -57.94014935, -0.00024721, -193.13383116, -0.00082405, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 77.25353246, 0.02488042, 77.25353246, 0.07464127, 54.07747272, -1212.02223131, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 19.31338312, 8.24e-05, 57.94014935, 0.00024721, 193.13383116, 0.00082405, -19.31338312, -8.24e-05, -57.94014935, -0.00024721, -193.13383116, -0.00082405, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 8.15, 11.55, 9.175)
    ops.node(124015, 8.15, 11.55, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 28955036.54104822, 12064598.55877009, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 106.20046792, 0.00094201, 128.82035606, 0.01494958, 12.88203561, 0.04583682, -106.20046792, -0.00094201, -128.82035606, -0.01494958, -12.88203561, -0.04583682, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 106.20046792, 0.00094201, 128.82035606, 0.01494958, 12.88203561, 0.04583682, -106.20046792, -0.00094201, -128.82035606, -0.01494958, -12.88203561, -0.04583682, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 112.39610996, 0.01884015, 112.39610996, 0.05652044, 78.67727697, -1199.94154429, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 28.09902749, 6.388e-05, 84.29708247, 0.00019165, 280.99027489, 0.00063882, -28.09902749, -6.388e-05, -84.29708247, -0.00019165, -280.99027489, -0.00063882, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 112.39610996, 0.01884015, 112.39610996, 0.05652044, 78.67727697, -1199.94154429, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 28.09902749, 6.388e-05, 84.29708247, 0.00019165, 280.99027489, 0.00063882, -28.09902749, -6.388e-05, -84.29708247, -0.00019165, -280.99027489, -0.00063882, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 13.45, 11.55, 9.175)
    ops.node(124016, 13.45, 11.55, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 29679217.27517597, 12366340.53132332, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 40.86102273, 0.00115348, 49.43842363, 0.01802758, 4.94384236, 0.07235324, -40.86102273, -0.00115348, -49.43842363, -0.01802758, -4.94384236, -0.07235324, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 37.28594321, 0.00115348, 45.1128761, 0.01802758, 4.51128761, 0.07235324, -37.28594321, -0.00115348, -45.1128761, -0.01802758, -4.51128761, -0.07235324, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 82.72936844, 0.02306955, 82.72936844, 0.06920866, 57.91055791, -1566.53844082, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 20.68234211, 8.991e-05, 62.04702633, 0.00026974, 206.8234211, 0.00089912, -20.68234211, -8.991e-05, -62.04702633, -0.00026974, -206.8234211, -0.00089912, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 82.72936844, 0.02306955, 82.72936844, 0.06920866, 57.91055791, -1566.53844082, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 20.68234211, 8.991e-05, 62.04702633, 0.00026974, 206.8234211, 0.00089912, -20.68234211, -8.991e-05, -62.04702633, -0.00026974, -206.8234211, -0.00089912, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 15.4, 9.175)
    ops.node(124017, 0.0, 15.4, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 27817500.66166507, 11590625.27569378, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 26.36948293, 0.00112418, 32.13129655, 0.01869469, 3.21312965, 0.07653448, -26.36948293, -0.00112418, -32.13129655, -0.01869469, -3.21312965, -0.07653448, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 26.36948293, 0.00112418, 32.13129655, 0.01869469, 3.21312965, 0.07653448, -26.36948293, -0.00112418, -32.13129655, -0.01869469, -3.21312965, -0.07653448, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 75.57529082, 0.02248355, 75.57529082, 0.06745064, 52.90270357, -2039.00510053, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 18.8938227, 8.763e-05, 56.68146811, 0.0002629, 188.93822705, 0.00087634, -18.8938227, -8.763e-05, -56.68146811, -0.0002629, -188.93822705, -0.00087634, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 75.57529082, 0.02248355, 75.57529082, 0.06745064, 52.90270357, -2039.00510053, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 18.8938227, 8.763e-05, 56.68146811, 0.0002629, 188.93822705, 0.00087634, -18.8938227, -8.763e-05, -56.68146811, -0.0002629, -188.93822705, -0.00087634, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 2.85, 15.4, 9.175)
    ops.node(124018, 2.85, 15.4, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 29866529.81731981, 12444387.42388326, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 47.86631825, 0.00124838, 57.78558168, 0.01872655, 5.77855817, 0.06352297, -47.86631825, -0.00124838, -57.78558168, -0.01872655, -5.77855817, -0.06352297, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 47.86631825, 0.00124838, 57.78558168, 0.01872655, 5.77855817, 0.06352297, -47.86631825, -0.00124838, -57.78558168, -0.01872655, -5.77855817, -0.06352297, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 74.95920026, 0.02496768, 74.95920026, 0.07490303, 52.47144018, -1197.88299188, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 18.73980006, 8.096e-05, 56.21940019, 0.00024287, 187.39800064, 0.00080956, -18.73980006, -8.096e-05, -56.21940019, -0.00024287, -187.39800064, -0.00080956, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 74.95920026, 0.02496768, 74.95920026, 0.07490303, 52.47144018, -1197.88299188, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 18.73980006, 8.096e-05, 56.21940019, 0.00024287, 187.39800064, 0.00080956, -18.73980006, -8.096e-05, -56.21940019, -0.00024287, -187.39800064, -0.00080956, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 8.15, 15.4, 9.175)
    ops.node(124019, 8.15, 15.4, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1225, 29242134.9825918, 12184222.90941325, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 106.32795354, 0.00092751, 128.90048761, 0.01495968, 12.89004876, 0.04604086, -106.32795354, -0.00092751, -128.90048761, -0.01495968, -12.89004876, -0.04604086, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 106.32795354, 0.00092751, 128.90048761, 0.01495968, 12.89004876, 0.04604086, -106.32795354, -0.00092751, -128.90048761, -0.01495968, -12.89004876, -0.04604086, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 114.80612271, 0.01855027, 114.80612271, 0.05565081, 80.36428589, -1248.11535801, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 28.70153068, 6.461e-05, 86.10459203, 0.00019383, 287.01530677, 0.00064612, -28.70153068, -6.461e-05, -86.10459203, -0.00019383, -287.01530677, -0.00064612, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 114.80612271, 0.01855027, 114.80612271, 0.05565081, 80.36428589, -1248.11535801, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 28.70153068, 6.461e-05, 86.10459203, 0.00019383, 287.01530677, 0.00064612, -28.70153068, -6.461e-05, -86.10459203, -0.00019383, -287.01530677, -0.00064612, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 13.45, 15.4, 9.175)
    ops.node(124020, 13.45, 15.4, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 29487427.62516078, 12286428.17715032, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 45.06562026, 0.00127446, 54.54711777, 0.01830743, 5.45471178, 0.06519257, -45.06562026, -0.00127446, -54.54711777, -0.01830743, -5.45471178, -0.06519257, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 45.06562026, 0.00127446, 54.54711777, 0.01830743, 5.45471178, 0.06519257, -45.06562026, -0.00127446, -54.54711777, -0.01830743, -5.45471178, -0.06519257, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 71.05127464, 0.02548924, 71.05127464, 0.07646772, 49.73589225, -1243.24451407, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 17.76281866, 7.772e-05, 53.28845598, 0.00023317, 177.62818661, 0.00077722, -17.76281866, -7.772e-05, -53.28845598, -0.00023317, -177.62818661, -0.00077722, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 71.05127464, 0.02548924, 71.05127464, 0.07646772, 49.73589225, -1243.24451407, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 17.76281866, 7.772e-05, 53.28845598, 0.00023317, 177.62818661, 0.00077722, -17.76281866, -7.772e-05, -53.28845598, -0.00023317, -177.62818661, -0.00077722, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 0.0, 19.25, 9.2)
    ops.node(124021, 0.0, 19.25, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 29304343.46012599, 12210143.10838583, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 23.9210071, 0.00110645, 29.1124132, 0.01939773, 2.91124132, 0.08207053, -23.9210071, -0.00110645, -29.1124132, -0.01939773, -2.91124132, -0.08207053, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 23.9210071, 0.00110645, 29.1124132, 0.01939773, 2.91124132, 0.08207053, -23.9210071, -0.00110645, -29.1124132, -0.01939773, -2.91124132, -0.08207053, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 77.48302031, 0.022129, 77.48302031, 0.066387, 54.23811422, -3298.85337902, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 19.37075508, 8.529e-05, 58.11226523, 0.00025586, 193.70755078, 0.00085287, -19.37075508, -8.529e-05, -58.11226523, -0.00025586, -193.70755078, -0.00085287, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 77.48302031, 0.022129, 77.48302031, 0.066387, 54.23811422, -3298.85337902, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 19.37075508, 8.529e-05, 58.11226523, 0.00025586, 193.70755078, 0.00085287, -19.37075508, -8.529e-05, -58.11226523, -0.00025586, -193.70755078, -0.00085287, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 2.85, 19.25, 9.2)
    ops.node(124022, 2.85, 19.25, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0625, 29156999.72786552, 12148749.88661063, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 28.66622815, 0.00110779, 34.78503679, 0.01810633, 3.47850368, 0.07482524, -28.66622815, -0.00110779, -34.78503679, -0.01810633, -3.47850368, -0.07482524, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 28.66622815, 0.00110779, 34.78503679, 0.01810633, 3.47850368, 0.07482524, -28.66622815, -0.00110779, -34.78503679, -0.01810633, -3.47850368, -0.07482524, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 79.41744136, 0.02215578, 79.41744136, 0.06646734, 55.59220895, -1749.28187338, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 19.85436034, 8.786e-05, 59.56308102, 0.00026358, 198.54360339, 0.00087858, -19.85436034, -8.786e-05, -59.56308102, -0.00026358, -198.54360339, -0.00087858, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 79.41744136, 0.02215578, 79.41744136, 0.06646734, 55.59220895, -1749.28187338, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 19.85436034, 8.786e-05, 59.56308102, 0.00026358, 198.54360339, 0.00087858, -19.85436034, -8.786e-05, -59.56308102, -0.00026358, -198.54360339, -0.00087858, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 8.15, 19.25, 9.2)
    ops.node(124023, 8.15, 19.25, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.0625, 29607508.99708243, 12336462.08211768, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 30.42850585, 0.00117866, 36.83203598, 0.01824952, 3.6832036, 0.07295114, -30.42850585, -0.00117866, -36.83203598, -0.01824952, -3.6832036, -0.07295114, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 30.42850585, 0.00117866, 36.83203598, 0.01824952, 3.6832036, 0.07295114, -30.42850585, -0.00117866, -36.83203598, -0.01824952, -3.6832036, -0.07295114, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 84.9412185, 0.02357312, 84.9412185, 0.07071937, 59.45885295, -1734.9760924, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 21.23530463, 9.254e-05, 63.70591388, 0.00027762, 212.35304626, 0.00092539, -21.23530463, -9.254e-05, -63.70591388, -0.00027762, -212.35304626, -0.00092539, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 84.9412185, 0.02357312, 84.9412185, 0.07071937, 59.45885295, -1734.9760924, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 21.23530463, 9.254e-05, 63.70591388, 0.00027762, 212.35304626, 0.00092539, -21.23530463, -9.254e-05, -63.70591388, -0.00027762, -212.35304626, -0.00092539, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 13.45, 19.25, 9.2)
    ops.node(124024, 13.45, 19.25, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 31247713.66914677, 13019880.69547782, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 27.01231304, 0.00104835, 32.65463917, 0.01867169, 3.26546392, 0.07975744, -27.01231304, -0.00104835, -32.65463917, -0.01867169, -3.26546392, -0.07975744, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 27.01231304, 0.00104835, 32.65463917, 0.01867169, 3.26546392, 0.07975744, -27.01231304, -0.00104835, -32.65463917, -0.01867169, -3.26546392, -0.07975744, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 84.00158514, 0.02096691, 84.00158514, 0.06290073, 58.8011096, -2349.50848067, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 21.00039628, 8.671e-05, 63.00118885, 0.00026014, 210.00396284, 0.00086712, -21.00039628, -8.671e-05, -63.00118885, -0.00026014, -210.00396284, -0.00086712, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 84.00158514, 0.02096691, 84.00158514, 0.06290073, 58.8011096, -2349.50848067, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 21.00039628, 8.671e-05, 63.00118885, 0.00026014, 210.00396284, 0.00086712, -21.00039628, -8.671e-05, -63.00118885, -0.00026014, -210.00396284, -0.00086712, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124025, 0.0, 0.0, 1.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170001, 124025, 0.0625, 28440869.5059365, 11850362.29414021, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 70.08904134, 0.00099248, 83.93211706, 0.01581613, 8.39321171, 0.05192995, -70.08904134, -0.00099248, -83.93211706, -0.01581613, -8.39321171, -0.05192995, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 66.00038235, 0.00099248, 79.03591934, 0.01581613, 7.90359193, 0.05192995, -66.00038235, -0.00099248, -79.03591934, -0.01581613, -7.90359193, -0.05192995, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 91.60545984, 0.01984954, 91.60545984, 0.05954861, 64.12382189, -2333.37846359, 0.05, 2, 0, 70001, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 22.90136496, 6.215e-05, 68.70409488, 0.00018645, 229.0136496, 0.00062151, -22.90136496, -6.215e-05, -68.70409488, -0.00018645, -229.0136496, -0.00062151, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 91.60545984, 0.01984954, 91.60545984, 0.05954861, 64.12382189, -2333.37846359, 0.05, 2, 0, 70001, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 22.90136496, 6.215e-05, 68.70409488, 0.00018645, 229.0136496, 0.00062151, -22.90136496, -6.215e-05, -68.70409488, -0.00018645, -229.0136496, -0.00062151, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 0.0, 0.0, 1.875)
    ops.node(121001, 0.0, 0.0, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121001, 0.0625, 29066461.71069028, 12111025.71278762, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 52.44179372, 0.00093463, 62.95103801, 0.01618028, 6.2951038, 0.05696599, -52.44179372, -0.00093463, -62.95103801, -0.01618028, -6.2951038, -0.05696599, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 48.5286591, 0.00093463, 58.25371802, 0.01618028, 5.8253718, 0.05696599, -48.5286591, -0.00093463, -58.25371802, -0.01618028, -5.8253718, -0.05696599, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 92.81695817, 0.0186926, 92.81695817, 0.05607779, 64.97187072, -2433.18811512, 0.05, 2, 0, 74025, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 23.20423954, 6.162e-05, 69.61271863, 0.00018485, 232.04239543, 0.00061617, -23.20423954, -6.162e-05, -69.61271863, -0.00018485, -232.04239543, -0.00061617, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 92.81695817, 0.0186926, 92.81695817, 0.05607779, 64.97187072, -2433.18811512, 0.05, 2, 0, 74025, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 23.20423954, 6.162e-05, 69.61271863, 0.00018485, 232.04239543, 0.00061617, -23.20423954, -6.162e-05, -69.61271863, -0.00018485, -232.04239543, -0.00061617, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 2.85, 0.0, 0.0)
    ops.node(124026, 2.85, 0.0, 1.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170002, 124026, 0.09, 28002062.98764221, 11667526.24485092, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 140.16148241, 0.00090563, 166.24623191, 0.01324288, 16.62462319, 0.03601042, -140.16148241, -0.00090563, -166.24623191, -0.01324288, -16.62462319, -0.03601042, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 140.16148241, 0.00090563, 166.24623191, 0.01324288, 16.62462319, 0.03601042, -140.16148241, -0.00090563, -166.24623191, -0.01324288, -16.62462319, -0.03601042, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 143.07605003, 0.01811254, 143.07605003, 0.05433761, 100.15323502, -3228.5454286, 0.05, 2, 0, 70002, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 35.76901251, 6.847e-05, 107.30703752, 0.0002054, 357.69012507, 0.00068467, -35.76901251, -6.847e-05, -107.30703752, -0.0002054, -357.69012507, -0.00068467, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 143.07605003, 0.01811254, 143.07605003, 0.05433761, 100.15323502, -3228.5454286, 0.05, 2, 0, 70002, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 35.76901251, 6.847e-05, 107.30703752, 0.0002054, 357.69012507, 0.00068467, -35.76901251, -6.847e-05, -107.30703752, -0.0002054, -357.69012507, -0.00068467, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 2.85, 0.0, 1.875)
    ops.node(121002, 2.85, 0.0, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121002, 0.09, 30064246.19062177, 12526769.24609241, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 109.07611621, 0.00085574, 129.7218995, 0.0132748, 12.97218995, 0.0424378, -109.07611621, -0.00085574, -129.7218995, -0.0132748, -12.97218995, -0.0424378, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 97.98000304, 0.00085574, 116.52552868, 0.0132748, 11.65255287, 0.0424378, -97.98000304, -0.00085574, -116.52552868, -0.0132748, -11.65255287, -0.0424378, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 149.27467128, 0.01711475, 149.27467128, 0.05134424, 104.49226989, -3208.20446617, 0.05, 2, 0, 74026, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 37.31866782, 6.653e-05, 111.95600346, 0.0001996, 373.18667819, 0.00066534, -37.31866782, -6.653e-05, -111.95600346, -0.0001996, -373.18667819, -0.00066534, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 149.27467128, 0.01711475, 149.27467128, 0.05134424, 104.49226989, -3208.20446617, 0.05, 2, 0, 74026, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 37.31866782, 6.653e-05, 111.95600346, 0.0001996, 373.18667819, 0.00066534, -37.31866782, -6.653e-05, -111.95600346, -0.0001996, -373.18667819, -0.00066534, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.6)
    ops.node(124027, 0.0, 0.0, 4.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171001, 124027, 0.0625, 29855066.03650594, 12439610.84854414, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 45.86575361, 0.00085906, 55.1340545, 0.01656307, 5.51340545, 0.06200028, -45.86575361, -0.00085906, -55.1340545, -0.01656307, -5.51340545, -0.06200028, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 49.63121701, 0.00085906, 59.66042217, 0.01656307, 5.96604222, 0.06200028, -49.63121701, -0.00085906, -59.66042217, -0.01656307, -5.96604222, -0.06200028, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 98.18779897, 0.01718119, 98.18779897, 0.05154357, 68.73145928, -2860.94874919, 0.05, 2, 0, 71001, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 24.54694974, 5.304e-05, 73.64084923, 0.00015913, 245.46949742, 0.00053042, -24.54694974, -5.304e-05, -73.64084923, -0.00015913, -245.46949742, -0.00053042, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 98.18779897, 0.01718119, 98.18779897, 0.05154357, 68.73145928, -2860.94874919, 0.05, 2, 0, 71001, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 24.54694974, 5.304e-05, 73.64084923, 0.00015913, 245.46949742, 0.00053042, -24.54694974, -5.304e-05, -73.64084923, -0.00015913, -245.46949742, -0.00053042, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 0.0, 0.0, 4.925)
    ops.node(122001, 0.0, 0.0, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122001, 0.0625, 28802750.10365355, 12001145.87652231, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 36.55866073, 0.00084318, 44.1196696, 0.01656863, 4.41196696, 0.06337646, -36.55866073, -0.00084318, -44.1196696, -0.01656863, -4.41196696, -0.06337646, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 36.55866073, 0.00084318, 44.1196696, 0.01656863, 4.41196696, 0.06337646, -36.55866073, -0.00084318, -44.1196696, -0.01656863, -4.41196696, -0.06337646, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 92.44494025, 0.01686363, 92.44494025, 0.05059089, 64.71145817, -2876.81937554, 0.05, 2, 0, 74027, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 23.11123506, 5.176e-05, 69.33370519, 0.00015529, 231.11235062, 0.00051764, -23.11123506, -5.176e-05, -69.33370519, -0.00015529, -231.11235062, -0.00051764, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 92.44494025, 0.01686363, 92.44494025, 0.05059089, 64.71145817, -2876.81937554, 0.05, 2, 0, 74027, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 23.11123506, 5.176e-05, 69.33370519, 0.00015529, 231.11235062, 0.00051764, -23.11123506, -5.176e-05, -69.33370519, -0.00015529, -231.11235062, -0.00051764, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 2.85, 0.0, 3.6)
    ops.node(124028, 2.85, 0.0, 4.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171002, 124028, 0.09, 29308508.27293496, 12211878.44705623, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 84.81724979, 0.00078983, 101.43154217, 0.01369843, 10.14315422, 0.04593857, -84.81724979, -0.00078983, -101.43154217, -0.01369843, -10.14315422, -0.04593857, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 79.69794427, 0.00078983, 95.30944961, 0.01369843, 9.53094496, 0.04593857, -79.69794427, -0.00078983, -95.30944961, -0.01369843, -9.53094496, -0.04593857, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 154.24211522, 0.01579658, 154.24211522, 0.04738974, 107.96948065, -3496.12335243, 0.05, 2, 0, 71002, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 38.56052881, 5.894e-05, 115.68158642, 0.00017683, 385.60528805, 0.00058942, -38.56052881, -5.894e-05, -115.68158642, -0.00017683, -385.60528805, -0.00058942, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 154.24211522, 0.01579658, 154.24211522, 0.04738974, 107.96948065, -3496.12335243, 0.05, 2, 0, 71002, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 38.56052881, 5.894e-05, 115.68158642, 0.00017683, 385.60528805, 0.00058942, -38.56052881, -5.894e-05, -115.68158642, -0.00017683, -385.60528805, -0.00058942, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 2.85, 0.0, 4.925)
    ops.node(122002, 2.85, 0.0, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122002, 0.09, 29822002.39648008, 12425834.3318667, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 79.46030708, 0.00074842, 95.15159124, 0.01418001, 9.51515912, 0.04921714, -79.46030708, -0.00074842, -95.15159124, -0.01418001, -9.51515912, -0.04921714, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 74.51427659, 0.00074842, 89.22885209, 0.01418001, 8.92288521, 0.04921714, -74.51427659, -0.00074842, -89.22885209, -0.01418001, -8.92288521, -0.04921714, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 153.34668486, 0.01496833, 153.34668486, 0.04490499, 107.3426794, -3439.43899641, 0.05, 2, 0, 74028, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 38.33667122, 5.759e-05, 115.01001365, 0.00017277, 383.36671216, 0.00057591, -38.33667122, -5.759e-05, -115.01001365, -0.00017277, -383.36671216, -0.00057591, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 153.34668486, 0.01496833, 153.34668486, 0.04490499, 107.3426794, -3439.43899641, 0.05, 2, 0, 74028, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 38.33667122, 5.759e-05, 115.01001365, 0.00017277, 383.36671216, 0.00057591, -38.33667122, -5.759e-05, -115.01001365, -0.00017277, -383.36671216, -0.00057591, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.4)
    ops.node(124029, 0.0, 0.0, 7.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172001, 124029, 0.0625, 29864763.85110749, 12443651.60462812, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 33.71930147, 0.00079997, 40.7162194, 0.01698935, 4.07162194, 0.0690043, -33.71930147, -0.00079997, -40.7162194, -0.01698935, -4.07162194, -0.0690043, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 33.71930147, 0.00079997, 40.7162194, 0.01698935, 4.07162194, 0.0690043, -33.71930147, -0.00079997, -40.7162194, -0.01698935, -4.07162194, -0.0690043, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 92.14990786, 0.01599931, 92.14990786, 0.04799793, 64.5049355, -3028.3504847, 0.05, 2, 0, 72001, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 23.03747696, 4.976e-05, 69.11243089, 0.00014929, 230.37476964, 0.00049764, -23.03747696, -4.976e-05, -69.11243089, -0.00014929, -230.37476964, -0.00049764, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 92.14990786, 0.01599931, 92.14990786, 0.04799793, 64.5049355, -3028.3504847, 0.05, 2, 0, 72001, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 23.03747696, 4.976e-05, 69.11243089, 0.00014929, 230.37476964, 0.00049764, -23.03747696, -4.976e-05, -69.11243089, -0.00014929, -230.37476964, -0.00049764, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 0.0, 0.0, 7.725)
    ops.node(123001, 0.0, 0.0, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123001, 0.0625, 28663243.73848553, 11943018.22436897, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 29.67942176, 0.00082048, 36.02421331, 0.0174905, 3.60242133, 0.07243737, -29.67942176, -0.00082048, -36.02421331, -0.0174905, -3.60242133, -0.07243737, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 29.67942176, 0.00082048, 36.02421331, 0.0174905, 3.60242133, 0.07243737, -29.67942176, -0.00082048, -36.02421331, -0.0174905, -3.60242133, -0.07243737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 85.05117125, 0.01640955, 85.05117125, 0.04922865, 59.53581987, -3351.27400716, 0.05, 2, 0, 74029, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 21.26279281, 4.786e-05, 63.78837843, 0.00014357, 212.62792811, 0.00047856, -21.26279281, -4.786e-05, -63.78837843, -0.00014357, -212.62792811, -0.00047856, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 85.05117125, 0.01640955, 85.05117125, 0.04922865, 59.53581987, -3351.27400716, 0.05, 2, 0, 74029, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 21.26279281, 4.786e-05, 63.78837843, 0.00014357, 212.62792811, 0.00047856, -21.26279281, -4.786e-05, -63.78837843, -0.00014357, -212.62792811, -0.00047856, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 2.85, 0.0, 6.4)
    ops.node(124030, 2.85, 0.0, 7.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172002, 124030, 0.0625, 30559715.08953976, 12733214.62064156, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 45.01775186, 0.00085522, 53.84562538, 0.01499748, 5.38456254, 0.05670348, -45.01775186, -0.00085522, -53.84562538, -0.01499748, -5.38456254, -0.05670348, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 45.01775186, 0.00085522, 53.84562538, 0.01499748, 5.38456254, 0.05670348, -45.01775186, -0.00085522, -53.84562538, -0.01499748, -5.38456254, -0.05670348, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 103.37263951, 0.01710446, 103.37263951, 0.05131337, 72.36084766, -2795.73893534, 0.05, 2, 0, 72002, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 25.84315988, 5.456e-05, 77.52947964, 0.00016367, 258.43159879, 0.00054555, -25.84315988, -5.456e-05, -77.52947964, -0.00016367, -258.43159879, -0.00054555, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 103.37263951, 0.01710446, 103.37263951, 0.05131337, 72.36084766, -2795.73893534, 0.05, 2, 0, 72002, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 25.84315988, 5.456e-05, 77.52947964, 0.00016367, 258.43159879, 0.00054555, -25.84315988, -5.456e-05, -77.52947964, -0.00016367, -258.43159879, -0.00054555, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 2.85, 0.0, 7.725)
    ops.node(123002, 2.85, 0.0, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123002, 0.0625, 30179067.18952144, 12574611.32896727, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 41.3899828, 0.00084777, 49.65876421, 0.01598946, 4.96587642, 0.06014894, -41.3899828, -0.00084777, -49.65876421, -0.01598946, -4.96587642, -0.06014894, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 41.3899828, 0.00084777, 49.65876421, 0.01598946, 4.96587642, 0.06014894, -41.3899828, -0.00084777, -49.65876421, -0.01598946, -4.96587642, -0.06014894, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 100.94534079, 0.01695535, 100.94534079, 0.05086606, 70.66173856, -2871.89265842, 0.05, 2, 0, 74030, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 25.2363352, 5.395e-05, 75.70900559, 0.00016184, 252.36335198, 0.00053946, -25.2363352, -5.395e-05, -75.70900559, -0.00016184, -252.36335198, -0.00053946, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 100.94534079, 0.01695535, 100.94534079, 0.05086606, 70.66173856, -2871.89265842, 0.05, 2, 0, 74030, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 25.2363352, 5.395e-05, 75.70900559, 0.00016184, 252.36335198, 0.00053946, -25.2363352, -5.395e-05, -75.70900559, -0.00016184, -252.36335198, -0.00053946, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.2)
    ops.node(124031, 0.0, 0.0, 10.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173001, 124031, 0.0625, 28529746.39561564, 11887394.33150652, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 26.43743989, 0.00077533, 32.1867111, 0.0187448, 3.21867111, 0.07826735, -26.43743989, -0.00077533, -32.1867111, -0.0187448, -3.21867111, -0.07826735, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 26.43743989, 0.00077533, 32.1867111, 0.0187448, 3.21867111, 0.07826735, -26.43743989, -0.00077533, -32.1867111, -0.0187448, -3.21867111, -0.07826735, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 83.15890966, 0.01550667, 83.15890966, 0.04652002, 58.21123676, -4755.52386766, 0.05, 2, 0, 73001, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 20.78972742, 4.701e-05, 62.36918225, 0.00014103, 207.89727415, 0.0004701, -20.78972742, -4.701e-05, -62.36918225, -0.00014103, -207.89727415, -0.0004701, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 83.15890966, 0.01550667, 83.15890966, 0.04652002, 58.21123676, -4755.52386766, 0.05, 2, 0, 73001, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 20.78972742, 4.701e-05, 62.36918225, 0.00014103, 207.89727415, 0.0004701, -20.78972742, -4.701e-05, -62.36918225, -0.00014103, -207.89727415, -0.0004701, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 0.0, 0.0, 10.525)
    ops.node(124001, 0.0, 0.0, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124001, 0.0625, 30502924.87761529, 12709552.03233971, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 22.44693666, 0.00074834, 27.26537592, 0.01885761, 2.72653759, 0.08451725, -22.44693666, -0.00074834, -27.26537592, -0.01885761, -2.72653759, -0.08451725, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 22.44693666, 0.00074834, 27.26537592, 0.01885761, 2.72653759, 0.08451725, -22.44693666, -0.00074834, -27.26537592, -0.01885761, -2.72653759, -0.08451725, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 81.73141534, 0.01496686, 81.73141534, 0.04490057, 57.21199074, -15810.98261861, 0.05, 2, 0, 74031, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 20.43285384, 4.321e-05, 61.29856151, 0.00012964, 204.32853835, 0.00043214, -20.43285384, -4.321e-05, -61.29856151, -0.00012964, -204.32853835, -0.00043214, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 81.73141534, 0.01496686, 81.73141534, 0.04490057, 57.21199074, -15810.98261861, 0.05, 2, 0, 74031, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 20.43285384, 4.321e-05, 61.29856151, 0.00012964, 204.32853835, 0.00043214, -20.43285384, -4.321e-05, -61.29856151, -0.00012964, -204.32853835, -0.00043214, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 2.85, 0.0, 9.2)
    ops.node(124032, 2.85, 0.0, 10.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173002, 124032, 0.0625, 30093328.57870268, 12538886.90779278, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 30.2018447, 0.00080216, 36.52408461, 0.01780602, 3.65240846, 0.0733219, -30.2018447, -0.00080216, -36.52408461, -0.01780602, -3.65240846, -0.0733219, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 30.2018447, 0.00080216, 36.52408461, 0.01780602, 3.65240846, 0.0733219, -30.2018447, -0.00080216, -36.52408461, -0.01780602, -3.65240846, -0.0733219, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 90.13831895, 0.0160433, 90.13831895, 0.04812989, 63.09682326, -3331.55124236, 0.05, 2, 0, 73002, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 22.53457974, 4.831e-05, 67.60373921, 0.00014492, 225.34579737, 0.00048308, -22.53457974, -4.831e-05, -67.60373921, -0.00014492, -225.34579737, -0.00048308, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 90.13831895, 0.0160433, 90.13831895, 0.04812989, 63.09682326, -3331.55124236, 0.05, 2, 0, 73002, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 22.53457974, 4.831e-05, 67.60373921, 0.00014492, 225.34579737, 0.00048308, -22.53457974, -4.831e-05, -67.60373921, -0.00014492, -225.34579737, -0.00048308, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 2.85, 0.0, 10.525)
    ops.node(124002, 2.85, 0.0, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124002, 0.0625, 30243504.65360117, 12601460.27233382, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 26.77890842, 0.00076565, 32.45696454, 0.0181979, 3.24569645, 0.07833064, -26.77890842, -0.00076565, -32.45696454, -0.0181979, -3.24569645, -0.07833064, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 26.77890842, 0.00076565, 32.45696454, 0.0181979, 3.24569645, 0.07833064, -26.77890842, -0.00076565, -32.45696454, -0.0181979, -3.24569645, -0.07833064, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 86.48061566, 0.01531306, 86.48061566, 0.04593917, 60.53643096, -4327.35768413, 0.05, 2, 0, 74032, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 21.62015391, 4.612e-05, 64.86046174, 0.00013835, 216.20153915, 0.00046118, -21.62015391, -4.612e-05, -64.86046174, -0.00013835, -216.20153915, -0.00046118, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 86.48061566, 0.01531306, 86.48061566, 0.04593917, 60.53643096, -4327.35768413, 0.05, 2, 0, 74032, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 21.62015391, 4.612e-05, 64.86046174, 0.00013835, 216.20153915, 0.00046118, -21.62015391, -4.612e-05, -64.86046174, -0.00013835, -216.20153915, -0.00046118, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4081, '-orient', 0, 0, 1, 0, 1, 0)
