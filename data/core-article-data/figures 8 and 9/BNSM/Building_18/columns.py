import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 27740401.98307873, 11558500.8262828, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 65.52539044, 0.00081611, 78.41133627, 0.01132507, 7.84113363, 0.04040268, -65.52539044, -0.00081611, -78.41133627, -0.01132507, -7.84113363, -0.04040268, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 71.89527901, 0.00081611, 86.03390016, 0.01132507, 8.60339002, 0.04040268, -71.89527901, -0.00081611, -86.03390016, -0.01132507, -8.60339002, -0.04040268, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 94.52395129, 0.01632211, 94.52395129, 0.04896632, 66.1667659, -865.47339466, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 23.63098782, 9.541e-05, 70.89296346, 0.00028623, 236.30987822, 0.00095409, -23.63098782, -9.541e-05, -70.89296346, -0.00028623, -236.30987822, -0.00095409, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 94.52395129, 0.01632211, 94.52395129, 0.04896632, 66.1667659, -865.47339466, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 23.63098782, 9.541e-05, 70.89296346, 0.00028623, 236.30987822, 0.00095409, -23.63098782, -9.541e-05, -70.89296346, -0.00028623, -236.30987822, -0.00095409, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.95, 0.0, 0.0)
    ops.node(121002, 4.95, 0.0, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.09, 31407283.37034314, 13086368.07097631, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 87.23440733, 0.00085388, 103.23587808, 0.01167917, 10.32358781, 0.04020521, -87.23440733, -0.00085388, -103.23587808, -0.01167917, -10.32358781, -0.04020521, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 94.10242549, 0.00085388, 111.3637018, 0.01167917, 11.13637018, 0.04020521, -94.10242549, -0.00085388, -111.3637018, -0.01167917, -11.13637018, -0.04020521, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 121.98746032, 0.01707769, 121.98746032, 0.05123308, 85.39122222, -1189.77038348, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 30.49686508, 0.00010875, 91.49059524, 0.00032626, 304.96865079, 0.00108753, -30.49686508, -0.00010875, -91.49059524, -0.00032626, -304.96865079, -0.00108753, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 121.98746032, 0.01707769, 121.98746032, 0.05123308, 85.39122222, -1189.77038348, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 30.49686508, 0.00010875, 91.49059524, 0.00032626, 304.96865079, 0.00108753, -30.49686508, -0.00010875, -91.49059524, -0.00032626, -304.96865079, -0.00108753, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 17.85, 0.0, 0.0)
    ops.node(121005, 17.85, 0.0, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.09, 30869879.35122587, 12862449.72967745, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 87.91323555, 0.00083338, 104.07213596, 0.011696, 10.4072136, 0.03904705, -87.91323555, -0.00083338, -104.07213596, -0.011696, -10.4072136, -0.03904705, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 95.7036732, 0.00083338, 113.29449572, 0.011696, 11.32944957, 0.03904705, -95.7036732, -0.00083338, -113.29449572, -0.011696, -11.32944957, -0.03904705, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 119.82577489, 0.01666757, 119.82577489, 0.0500027, 83.87804242, -1182.81538979, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 29.95644372, 0.00010869, 89.86933117, 0.00032606, 299.56443723, 0.00108686, -29.95644372, -0.00010869, -89.86933117, -0.00032606, -299.56443723, -0.00108686, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 119.82577489, 0.01666757, 119.82577489, 0.0500027, 83.87804242, -1182.81538979, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 29.95644372, 0.00010869, 89.86933117, 0.00032606, 299.56443723, 0.00108686, -29.95644372, -0.00010869, -89.86933117, -0.00032606, -299.56443723, -0.00108686, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 22.8, 0.0, 0.0)
    ops.node(121006, 22.8, 0.0, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.09, 30799367.16867132, 12833069.65361305, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 68.7796584, 0.00077748, 82.1660799, 0.01251223, 8.21660799, 0.04815098, -68.7796584, -0.00077748, -82.1660799, -0.01251223, -8.21660799, -0.04815098, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 76.63617133, 0.00077748, 91.55168728, 0.01251223, 9.15516873, 0.04815098, -76.63617133, -0.00077748, -91.55168728, -0.01251223, -9.15516873, -0.04815098, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 105.97991846, 0.01554956, 105.97991846, 0.04664869, 74.18594292, -909.45976861, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 26.49497962, 9.635e-05, 79.48493885, 0.00028904, 264.94979615, 0.00096347, -26.49497962, -9.635e-05, -79.48493885, -0.00028904, -264.94979615, -0.00096347, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 105.97991846, 0.01554956, 105.97991846, 0.04664869, 74.18594292, -909.45976861, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 26.49497962, 9.635e-05, 79.48493885, 0.00028904, 264.94979615, 0.00096347, -26.49497962, -9.635e-05, -79.48493885, -0.00028904, -264.94979615, -0.00096347, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.6, 0.0)
    ops.node(121007, 0.0, 4.6, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.09, 30362611.69571528, 12651088.20654804, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 92.95279578, 0.00088123, 110.11742432, 0.01064176, 11.01174243, 0.03731187, -92.95279578, -0.00088123, -110.11742432, -0.01064176, -11.01174243, -0.03731187, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 96.39987423, 0.00088123, 114.20103898, 0.01064176, 11.4201039, 0.03731187, -96.39987423, -0.00088123, -114.20103898, -0.01064176, -11.4201039, -0.03731187, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 115.15878621, 0.01762464, 115.15878621, 0.05287391, 80.61115035, -1128.72591629, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 28.78969655, 0.0001062, 86.36908966, 0.00031859, 287.89696553, 0.00106198, -28.78969655, -0.0001062, -86.36908966, -0.00031859, -287.89696553, -0.00106198, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 115.15878621, 0.01762464, 115.15878621, 0.05287391, 80.61115035, -1128.72591629, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 28.78969655, 0.0001062, 86.36908966, 0.00031859, 287.89696553, 0.00106198, -28.78969655, -0.0001062, -86.36908966, -0.00031859, -287.89696553, -0.00106198, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.95, 4.6, 0.0)
    ops.node(121008, 4.95, 4.6, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.1225, 29667241.18818079, 12361350.49507533, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 150.15370711, 0.00075977, 178.26038983, 0.01018901, 17.82603898, 0.03108469, -150.15370711, -0.00075977, -178.26038983, -0.01018901, -17.82603898, -0.03108469, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 159.98177192, 0.00075977, 189.92813149, 0.01018901, 18.99281315, 0.03108469, -159.98177192, -0.00075977, -189.92813149, -0.01018901, -18.99281315, -0.03108469, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 139.42340519, 0.01519546, 139.42340519, 0.04558639, 97.59638364, -1285.83437101, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 34.8558513, 9.668e-05, 104.56755389, 0.00029003, 348.55851298, 0.00096677, -34.8558513, -9.668e-05, -104.56755389, -0.00029003, -348.55851298, -0.00096677, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 139.42340519, 0.01519546, 139.42340519, 0.04558639, 97.59638364, -1285.83437101, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 34.8558513, 9.668e-05, 104.56755389, 0.00029003, 348.55851298, 0.00096677, -34.8558513, -9.668e-05, -104.56755389, -0.00029003, -348.55851298, -0.00096677, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.9, 4.6, 0.0)
    ops.node(121009, 9.9, 4.6, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.1225, 31745954.51912984, 13227481.04963744, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 141.51026936, 0.00073795, 168.11209628, 0.01154147, 16.81120963, 0.03739604, -141.51026936, -0.00073795, -168.11209628, -0.01154147, -16.81120963, -0.03739604, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 150.51416299, 0.00073795, 178.80858806, 0.01154147, 17.88085881, 0.03739604, -150.51416299, -0.00073795, -178.80858806, -0.01154147, -17.88085881, -0.03739604, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 146.57683591, 0.01475899, 146.57683591, 0.04427698, 102.60378514, -1235.11691543, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 36.64420898, 9.498e-05, 109.93262694, 0.00028495, 366.44208979, 0.00094982, -36.64420898, -9.498e-05, -109.93262694, -0.00028495, -366.44208979, -0.00094982, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 146.57683591, 0.01475899, 146.57683591, 0.04427698, 102.60378514, -1235.11691543, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 36.64420898, 9.498e-05, 109.93262694, 0.00028495, 366.44208979, 0.00094982, -36.64420898, -9.498e-05, -109.93262694, -0.00028495, -366.44208979, -0.00094982, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.9, 4.6, 0.0)
    ops.node(121010, 12.9, 4.6, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.1225, 30205609.85479016, 12585670.77282923, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 136.4366448, 0.00079815, 162.32650666, 0.01214083, 16.23265067, 0.03550238, -136.4366448, -0.00079815, -162.32650666, -0.01214083, -16.23265067, -0.03550238, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 143.49918274, 0.00079815, 170.72921337, 0.01214083, 17.07292134, 0.03550238, -143.49918274, -0.00079815, -170.72921337, -0.01214083, -17.07292134, -0.03550238, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 142.23425658, 0.01596302, 142.23425658, 0.04788907, 99.5639796, -1270.26489041, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 35.55856414, 9.687e-05, 106.67569243, 0.0002906, 355.58564144, 0.00096868, -35.55856414, -9.687e-05, -106.67569243, -0.0002906, -355.58564144, -0.00096868, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 142.23425658, 0.01596302, 142.23425658, 0.04788907, 99.5639796, -1270.26489041, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 35.55856414, 9.687e-05, 106.67569243, 0.0002906, 355.58564144, 0.00096868, -35.55856414, -9.687e-05, -106.67569243, -0.0002906, -355.58564144, -0.00096868, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 17.85, 4.6, 0.0)
    ops.node(121011, 17.85, 4.6, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.1225, 30030246.22341901, 12512602.59309125, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 144.51193736, 0.0007992, 171.55845934, 0.01068423, 17.15584593, 0.03223348, -144.51193736, -0.0007992, -171.55845934, -0.01068423, -17.15584593, -0.03223348, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 152.12985194, 0.0007992, 180.60212531, 0.01068423, 18.06021253, 0.03223348, -152.12985194, -0.0007992, -180.60212531, -0.01068423, -18.06021253, -0.03223348, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 141.5503254, 0.01598406, 141.5503254, 0.04795218, 99.08522778, -1294.84547069, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 35.38758135, 9.697e-05, 106.16274405, 0.0002909, 353.87581349, 0.00096965, -35.38758135, -9.697e-05, -106.16274405, -0.0002909, -353.87581349, -0.00096965, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 141.5503254, 0.01598406, 141.5503254, 0.04795218, 99.08522778, -1294.84547069, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 35.38758135, 9.697e-05, 106.16274405, 0.0002909, 353.87581349, 0.00096965, -35.38758135, -9.697e-05, -106.16274405, -0.0002909, -353.87581349, -0.00096965, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 22.8, 4.6, 0.0)
    ops.node(121012, 22.8, 4.6, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.09, 31755276.53861723, 13231365.22442385, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 92.08543376, 0.00088204, 108.99953765, 0.01100006, 10.89995377, 0.04071093, -92.08543376, -0.00088204, -108.99953765, -0.01100006, -10.89995377, -0.04071093, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 95.17599131, 0.00088204, 112.65776383, 0.01100006, 11.26577638, 0.04071093, -95.17599131, -0.00088204, -112.65776383, -0.01100006, -11.26577638, -0.04071093, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 118.62217405, 0.01764074, 118.62217405, 0.05292222, 83.03552184, -1112.21292161, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 29.65554351, 0.00010459, 88.96663054, 0.00031378, 296.55543514, 0.00104594, -29.65554351, -0.00010459, -88.96663054, -0.00031378, -296.55543514, -0.00104594, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 118.62217405, 0.01764074, 118.62217405, 0.05292222, 83.03552184, -1112.21292161, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 29.65554351, 0.00010459, 88.96663054, 0.00031378, 296.55543514, 0.00104594, -29.65554351, -0.00010459, -88.96663054, -0.00031378, -296.55543514, -0.00104594, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.2, 0.0)
    ops.node(121013, 0.0, 9.2, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.09, 31310018.02162411, 13045840.84234338, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 71.53244735, 0.00077211, 85.38985302, 0.01340041, 8.5389853, 0.04997839, -71.53244735, -0.00077211, -85.38985302, -0.01340041, -8.5389853, -0.04997839, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 74.61413259, 0.00077211, 89.06852835, 0.01340041, 8.90685284, 0.04997839, -74.61413259, -0.00077211, -89.06852835, -0.01340041, -8.90685284, -0.04997839, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 107.76948821, 0.0154423, 107.76948821, 0.0463269, 75.43864175, -913.98720516, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 26.94237205, 9.638e-05, 80.82711616, 0.00028913, 269.42372052, 0.00096376, -26.94237205, -9.638e-05, -80.82711616, -0.00028913, -269.42372052, -0.00096376, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 107.76948821, 0.0154423, 107.76948821, 0.0463269, 75.43864175, -913.98720516, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 26.94237205, 9.638e-05, 80.82711616, 0.00028913, 269.42372052, 0.00096376, -26.94237205, -9.638e-05, -80.82711616, -0.00028913, -269.42372052, -0.00096376, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.95, 9.2, 0.0)
    ops.node(121014, 4.95, 9.2, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.09, 29173225.20600023, 12155510.50250009, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 93.91521322, 0.00086862, 111.15242312, 0.01064591, 11.11524231, 0.03404616, -93.91521322, -0.00086862, -111.15242312, -0.01064591, -11.11524231, -0.03404616, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 97.62722683, 0.00086862, 115.54574017, 0.01064591, 11.55457402, 0.03404616, -97.62722683, -0.00086862, -115.54574017, -0.01064591, -11.55457402, -0.03404616, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 113.51645951, 0.01737243, 113.51645951, 0.05211729, 79.46152166, -1168.29117818, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 28.37911488, 0.00010895, 85.13734463, 0.00032685, 283.79114877, 0.00108951, -28.37911488, -0.00010895, -85.13734463, -0.00032685, -283.79114877, -0.00108951, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 113.51645951, 0.01737243, 113.51645951, 0.05211729, 79.46152166, -1168.29117818, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 28.37911488, 0.00010895, 85.13734463, 0.00032685, 283.79114877, 0.00108951, -28.37911488, -0.00010895, -85.13734463, -0.00032685, -283.79114877, -0.00108951, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.9, 9.2, 0.0)
    ops.node(121015, 9.9, 9.2, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.09, 31236704.02526855, 13015293.3438619, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 83.4290517, 0.00082793, 99.22242287, 0.01156672, 9.92224229, 0.04408487, -83.4290517, -0.00082793, -99.22242287, -0.01156672, -9.92224229, -0.04408487, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 86.91716639, 0.00082793, 103.37084819, 0.01156672, 10.33708482, 0.04408487, -86.91716639, -0.00082793, -103.37084819, -0.01156672, -10.33708482, -0.04408487, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 110.34222058, 0.01655858, 110.34222058, 0.04967575, 77.2395544, -973.48354008, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 27.58555514, 9.891e-05, 82.75666543, 0.00029673, 275.85555144, 0.00098909, -27.58555514, -9.891e-05, -82.75666543, -0.00029673, -275.85555144, -0.00098909, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 110.34222058, 0.01655858, 110.34222058, 0.04967575, 77.2395544, -973.48354008, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 27.58555514, 9.891e-05, 82.75666543, 0.00029673, 275.85555144, 0.00098909, -27.58555514, -9.891e-05, -82.75666543, -0.00029673, -275.85555144, -0.00098909, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.9, 9.2, 0.0)
    ops.node(121016, 12.9, 9.2, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.09, 29536797.98176469, 12306999.15906862, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 84.05604252, 0.0008436, 100.08591509, 0.01159546, 10.00859151, 0.0404713, -84.05604252, -0.0008436, -100.08591509, -0.01159546, -10.00859151, -0.0404713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 87.74862227, 0.0008436, 104.48268673, 0.01159546, 10.44826867, 0.0404713, -87.74862227, -0.0008436, -104.48268673, -0.01159546, -10.44826867, -0.0404713, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 106.66262045, 0.01687208, 106.66262045, 0.05061623, 74.66383432, -999.6695584, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 26.66565511, 0.00010111, 79.99696534, 0.00030334, 266.65655113, 0.00101113, -26.66565511, -0.00010111, -79.99696534, -0.00030334, -266.65655113, -0.00101113, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 106.66262045, 0.01687208, 106.66262045, 0.05061623, 74.66383432, -999.6695584, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 26.66565511, 0.00010111, 79.99696534, 0.00030334, 266.65655113, 0.00101113, -26.66565511, -0.00010111, -79.99696534, -0.00030334, -266.65655113, -0.00101113, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 17.85, 9.2, 0.0)
    ops.node(121017, 17.85, 9.2, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.09, 32686810.6782801, 13619504.44928337, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 94.52562675, 0.00091198, 111.70477276, 0.01155159, 11.17047728, 0.04271804, -94.52562675, -0.00091198, -111.70477276, -0.01155159, -11.17047728, -0.04271804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 97.51738416, 0.00091198, 115.24025402, 0.01155159, 11.5240254, 0.04271804, -97.51738416, -0.00091198, -115.24025402, -0.01155159, -11.5240254, -0.04271804, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 124.23621814, 0.01823956, 124.23621814, 0.05471867, 86.9653527, -1158.09015369, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 31.05905453, 0.00010642, 93.1771636, 0.00031927, 310.59054535, 0.00106423, -31.05905453, -0.00010642, -93.1771636, -0.00031927, -310.59054535, -0.00106423, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 124.23621814, 0.01823956, 124.23621814, 0.05471867, 86.9653527, -1158.09015369, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 31.05905453, 0.00010642, 93.1771636, 0.00031927, 310.59054535, 0.00106423, -31.05905453, -0.00010642, -93.1771636, -0.00031927, -310.59054535, -0.00106423, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 22.8, 9.2, 0.0)
    ops.node(121018, 22.8, 9.2, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.09, 33207291.86222024, 13836371.60925843, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 74.62177421, 0.00082516, 88.73383785, 0.01343049, 8.87338378, 0.05314274, -74.62177421, -0.00082516, -88.73383785, -0.01343049, -8.87338378, -0.05314274, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 77.69281443, 0.00082516, 92.38565647, 0.01343049, 9.23856565, 0.05314274, -77.69281443, -0.00082516, -92.38565647, -0.01343049, -9.23856565, -0.05314274, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 114.5918278, 0.01650311, 114.5918278, 0.04950932, 80.21427946, -932.24762328, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 28.64795695, 9.662e-05, 85.94387085, 0.00028987, 286.47956949, 0.00096622, -28.64795695, -9.662e-05, -85.94387085, -0.00028987, -286.47956949, -0.00096622, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 114.5918278, 0.01650311, 114.5918278, 0.04950932, 80.21427946, -932.24762328, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 28.64795695, 9.662e-05, 85.94387085, 0.00028987, 286.47956949, 0.00096622, -28.64795695, -9.662e-05, -85.94387085, -0.00028987, -286.47956949, -0.00096622, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.725)
    ops.node(122001, 0.0, 0.0, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 31145958.86428956, 12977482.86012065, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 54.54981657, 0.0007124, 65.41700023, 0.01297129, 6.54170002, 0.05425618, -54.54981657, -0.0007124, -65.41700023, -0.01297129, -6.54170002, -0.05425618, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 52.15985292, 0.0007124, 62.55091813, 0.01297129, 6.25509181, 0.05425618, -52.15985292, -0.0007124, -62.55091813, -0.01297129, -6.25509181, -0.05425618, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 100.34207336, 0.01424801, 100.34207336, 0.04274403, 70.23945135, -1039.84601968, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 25.08551834, 6.959e-05, 75.25655502, 0.00020876, 250.85518339, 0.00069588, -25.08551834, -6.959e-05, -75.25655502, -0.00020876, -250.85518339, -0.00069588, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 100.34207336, 0.01424801, 100.34207336, 0.04274403, 70.23945135, -1039.84601968, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 25.08551834, 6.959e-05, 75.25655502, 0.00020876, 250.85518339, 0.00069588, -25.08551834, -6.959e-05, -75.25655502, -0.00020876, -250.85518339, -0.00069588, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.95, 0.0, 3.725)
    ops.node(122002, 4.95, 0.0, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.09, 33143914.22527458, 13809964.26053108, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 74.13986151, 0.00069105, 88.01092196, 0.01274111, 8.8010922, 0.05022472, -74.13986151, -0.00069105, -88.01092196, -0.01274111, -8.8010922, -0.05022472, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 70.61189144, 0.00069105, 83.82289284, 0.01274111, 8.38228928, 0.05022472, -70.61189144, -0.00069105, -83.82289284, -0.01274111, -8.38228928, -0.05022472, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 119.6540916, 0.01382101, 119.6540916, 0.04146302, 83.75786412, -1329.81969922, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 29.9135229, 7.798e-05, 89.7405687, 0.00023394, 299.13522899, 0.00077979, -29.9135229, -7.798e-05, -89.7405687, -0.00023394, -299.13522899, -0.00077979, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 119.6540916, 0.01382101, 119.6540916, 0.04146302, 83.75786412, -1329.81969922, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 29.9135229, 7.798e-05, 89.7405687, 0.00023394, 299.13522899, 0.00077979, -29.9135229, -7.798e-05, -89.7405687, -0.00023394, -299.13522899, -0.00077979, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 17.85, 0.0, 3.725)
    ops.node(122005, 17.85, 0.0, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.09, 28648574.50466887, 11936906.04361203, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 72.31422362, 0.00071346, 86.27841893, 0.0125578, 8.62784189, 0.04107176, -72.31422362, -0.00071346, -86.27841893, -0.0125578, -8.62784189, -0.04107176, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 68.90356043, 0.00071346, 82.20914165, 0.0125578, 8.22091416, 0.04107176, -68.90356043, -0.00071346, -82.20914165, -0.0125578, -8.22091416, -0.04107176, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 106.84350891, 0.0142693, 106.84350891, 0.0428079, 74.79045623, -1352.10024006, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 26.71087723, 8.056e-05, 80.13263168, 0.00024167, 267.10877226, 0.00080556, -26.71087723, -8.056e-05, -80.13263168, -0.00024167, -267.10877226, -0.00080556, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 106.84350891, 0.0142693, 106.84350891, 0.0428079, 74.79045623, -1352.10024006, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 26.71087723, 8.056e-05, 80.13263168, 0.00024167, 267.10877226, 0.00080556, -26.71087723, -8.056e-05, -80.13263168, -0.00024167, -267.10877226, -0.00080556, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 22.8, 0.0, 3.725)
    ops.node(122006, 22.8, 0.0, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.09, 31197573.65977765, 12998989.02490735, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 54.37459566, 0.0006451, 65.20012975, 0.01422136, 6.52001298, 0.05558372, -54.37459566, -0.0006451, -65.20012975, -0.01422136, -6.52001298, -0.05558372, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 51.50281618, 0.0006451, 61.75660263, 0.01422136, 6.17566026, 0.05558372, -51.50281618, -0.0006451, -61.75660263, -0.01422136, -6.17566026, -0.05558372, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 102.53285439, 0.01290206, 102.53285439, 0.03870617, 71.77299807, -1092.93953092, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 25.6332136, 7.099e-05, 76.89964079, 0.00021297, 256.33213597, 0.0007099, -25.6332136, -7.099e-05, -76.89964079, -0.00021297, -256.33213597, -0.0007099, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 102.53285439, 0.01290206, 102.53285439, 0.03870617, 71.77299807, -1092.93953092, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 25.6332136, 7.099e-05, 76.89964079, 0.00021297, 256.33213597, 0.0007099, -25.6332136, -7.099e-05, -76.89964079, -0.00021297, -256.33213597, -0.0007099, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.6, 3.75)
    ops.node(122007, 0.0, 4.6, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.09, 28469704.83172237, 11862377.01321765, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 70.75875503, 0.0006909, 84.4629564, 0.01189009, 8.44629564, 0.04041107, -70.75875503, -0.0006909, -84.4629564, -0.01189009, -8.44629564, -0.04041107, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 67.31081385, 0.0006909, 80.34723524, 0.01189009, 8.03472352, 0.04041107, -67.31081385, -0.0006909, -80.34723524, -0.01189009, -8.03472352, -0.04041107, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 103.19743916, 0.01381792, 103.19743916, 0.04145376, 72.23820741, -1278.76633363, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 25.79935979, 7.83e-05, 77.39807937, 0.00023489, 257.9935979, 0.00078296, -25.79935979, -7.83e-05, -77.39807937, -0.00023489, -257.9935979, -0.00078296, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 103.19743916, 0.01381792, 103.19743916, 0.04145376, 72.23820741, -1278.76633363, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 25.79935979, 7.83e-05, 77.39807937, 0.00023489, 257.9935979, 0.00078296, -25.79935979, -7.83e-05, -77.39807937, -0.00023489, -257.9935979, -0.00078296, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.95, 4.6, 3.75)
    ops.node(122008, 4.95, 4.6, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.1225, 30835971.22915247, 12848321.34548019, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 113.02023941, 0.00061879, 134.87520329, 0.01233227, 13.48752033, 0.03942212, -113.02023941, -0.00061879, -134.87520329, -0.01233227, -13.48752033, -0.03942212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 109.06655122, 0.00061879, 130.15698202, 0.01233227, 13.0156982, 0.03942212, -109.06655122, -0.00061879, -130.15698202, -0.01233227, -13.0156982, -0.03942212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 138.76267574, 0.0123758, 138.76267574, 0.03712741, 97.13387302, -1481.60622474, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 34.69066894, 7.141e-05, 104.07200681, 0.00021424, 346.90668936, 0.00071413, -34.69066894, -7.141e-05, -104.07200681, -0.00021424, -346.90668936, -0.00071413, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 138.76267574, 0.0123758, 138.76267574, 0.03712741, 97.13387302, -1481.60622474, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 34.69066894, 7.141e-05, 104.07200681, 0.00021424, 346.90668936, 0.00071413, -34.69066894, -7.141e-05, -104.07200681, -0.00021424, -346.90668936, -0.00071413, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.9, 4.6, 3.75)
    ops.node(122009, 9.9, 4.6, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.1225, 28831162.20095946, 12012984.25039978, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 109.10359914, 0.0006219, 130.67462453, 0.01136987, 13.06746245, 0.03673643, -109.10359914, -0.0006219, -130.67462453, -0.01136987, -13.06746245, -0.03673643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 104.74301315, 0.0006219, 125.45190097, 0.01136987, 12.5451901, 0.03673643, -104.74301315, -0.0006219, -125.45190097, -0.01136987, -12.5451901, -0.03673643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 124.84954355, 0.01243802, 124.84954355, 0.03731406, 87.39468048, -1342.72645103, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 31.21238589, 6.872e-05, 93.63715766, 0.00020616, 312.12385887, 0.0006872, -31.21238589, -6.872e-05, -93.63715766, -0.00020616, -312.12385887, -0.0006872, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 124.84954355, 0.01243802, 124.84954355, 0.03731406, 87.39468048, -1342.72645103, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 31.21238589, 6.872e-05, 93.63715766, 0.00020616, 312.12385887, 0.0006872, -31.21238589, -6.872e-05, -93.63715766, -0.00020616, -312.12385887, -0.0006872, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.9, 4.6, 3.75)
    ops.node(122010, 12.9, 4.6, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.1225, 29112165.54338898, 12130068.97641208, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 108.4746882, 0.00062195, 129.90281429, 0.01217007, 12.99028143, 0.03801014, -108.4746882, -0.00062195, -129.90281429, -0.01217007, -12.99028143, -0.03801014, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 104.23731349, 0.00062195, 124.82838716, 0.01217007, 12.48283872, 0.03801014, -104.23731349, -0.00062195, -124.82838716, -0.01217007, -12.48283872, -0.03801014, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 127.61199454, 0.01243892, 127.61199454, 0.03731676, 89.32839618, -1378.96183601, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 31.90299864, 6.956e-05, 95.70899591, 0.00020869, 319.02998636, 0.00069563, -31.90299864, -6.956e-05, -95.70899591, -0.00020869, -319.02998636, -0.00069563, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 127.61199454, 0.01243892, 127.61199454, 0.03731676, 89.32839618, -1378.96183601, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 31.90299864, 6.956e-05, 95.70899591, 0.00020869, 319.02998636, 0.00069563, -31.90299864, -6.956e-05, -95.70899591, -0.00020869, -319.02998636, -0.00069563, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 17.85, 4.6, 3.75)
    ops.node(122011, 17.85, 4.6, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.1225, 31634465.25138603, 13181027.18807751, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 114.96546823, 0.00060676, 137.03584128, 0.01197244, 13.70358413, 0.04022768, -114.96546823, -0.00060676, -137.03584128, -0.01197244, -13.70358413, -0.04022768, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 110.6828015, 0.00060676, 131.93101418, 0.01197244, 13.19310142, 0.04022768, -110.6828015, -0.00060676, -131.93101418, -0.01197244, -13.19310142, -0.04022768, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 140.94496485, 0.01213517, 140.94496485, 0.03640551, 98.66147539, -1457.24517402, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 35.23624121, 7.07e-05, 105.70872364, 0.00021211, 352.36241212, 0.00070705, -35.23624121, -7.07e-05, -105.70872364, -0.00021211, -352.36241212, -0.00070705, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 140.94496485, 0.01213517, 140.94496485, 0.03640551, 98.66147539, -1457.24517402, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 35.23624121, 7.07e-05, 105.70872364, 0.00021211, 352.36241212, 0.00070705, -35.23624121, -7.07e-05, -105.70872364, -0.00021211, -352.36241212, -0.00070705, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 22.8, 4.6, 3.75)
    ops.node(122012, 22.8, 4.6, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.09, 29797622.31469679, 12415675.96445699, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 71.02091248, 0.00070147, 84.75088045, 0.01256186, 8.47508804, 0.04408755, -71.02091248, -0.00070147, -84.75088045, -0.01256186, -8.47508804, -0.04408755, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 67.7527818, 0.00070147, 80.8509453, 0.01256186, 8.08509453, 0.04408755, -67.7527818, -0.00070147, -80.8509453, -0.01256186, -8.08509453, -0.04408755, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 107.03771943, 0.01402936, 107.03771943, 0.04208808, 74.9264036, -1276.07175778, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 26.75942986, 7.759e-05, 80.27828957, 0.00023277, 267.59429856, 0.00077591, -26.75942986, -7.759e-05, -80.27828957, -0.00023277, -267.59429856, -0.00077591, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 107.03771943, 0.01402936, 107.03771943, 0.04208808, 74.9264036, -1276.07175778, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 26.75942986, 7.759e-05, 80.27828957, 0.00023277, 267.59429856, 0.00077591, -26.75942986, -7.759e-05, -80.27828957, -0.00023277, -267.59429856, -0.00077591, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.2, 3.725)
    ops.node(122013, 0.0, 9.2, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.09, 28932777.84087041, 12055324.10036267, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 55.86183306, 0.00065863, 67.21607421, 0.01438525, 6.72160742, 0.05193347, -55.86183306, -0.00065863, -67.21607421, -0.01438525, -6.72160742, -0.05193347, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 52.59087572, 0.00065863, 63.28027584, 0.01438525, 6.32802758, 0.05193347, -52.59087572, -0.00065863, -63.28027584, -0.01438525, -6.32802758, -0.05193347, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 97.10769637, 0.01317258, 97.10769637, 0.03951774, 67.97538746, -1120.70776871, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 24.27692409, 7.25e-05, 72.83077228, 0.00021749, 242.76924092, 0.00072497, -24.27692409, -7.25e-05, -72.83077228, -0.00021749, -242.76924092, -0.00072497, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 97.10769637, 0.01317258, 97.10769637, 0.03951774, 67.97538746, -1120.70776871, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 24.27692409, 7.25e-05, 72.83077228, 0.00021749, 242.76924092, 0.00072497, -24.27692409, -7.25e-05, -72.83077228, -0.00021749, -242.76924092, -0.00072497, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.95, 9.2, 3.725)
    ops.node(122014, 4.95, 9.2, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.09, 29763467.94681929, 12401444.97784137, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 72.84719444, 0.00070287, 86.89369032, 0.01132261, 8.68936903, 0.04236406, -72.84719444, -0.00070287, -86.89369032, -0.01132261, -8.68936903, -0.04236406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 69.3564147, 0.00070287, 82.72981364, 0.01132261, 8.27298136, 0.04236406, -69.3564147, -0.00070287, -82.72981364, -0.01132261, -8.27298136, -0.04236406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 106.17536059, 0.01405737, 106.17536059, 0.04217211, 74.32275241, -1260.3117072, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 26.54384015, 7.705e-05, 79.63152044, 0.00023116, 265.43840147, 0.00077054, -26.54384015, -7.705e-05, -79.63152044, -0.00023116, -265.43840147, -0.00077054, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 106.17536059, 0.01405737, 106.17536059, 0.04217211, 74.32275241, -1260.3117072, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 26.54384015, 7.705e-05, 79.63152044, 0.00023116, 265.43840147, 0.00077054, -26.54384015, -7.705e-05, -79.63152044, -0.00023116, -265.43840147, -0.00077054, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.9, 9.2, 3.725)
    ops.node(122015, 9.9, 9.2, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.09, 30459682.73689429, 12691534.47370596, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 62.68187175, 0.00065842, 75.02248509, 0.01362709, 7.50224851, 0.0501591, -62.68187175, -0.00065842, -75.02248509, -0.01362709, -7.50224851, -0.0501591, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 59.4533268, 0.00065842, 71.15831419, 0.01362709, 7.11583142, 0.0501591, -59.4533268, -0.00065842, -71.15831419, -0.01362709, -7.11583142, -0.0501591, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 105.69779949, 0.01316842, 105.69779949, 0.03950526, 73.98845965, -1199.47668581, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 26.42444987, 7.495e-05, 79.27334962, 0.00022486, 264.24449873, 0.00074954, -26.42444987, -7.495e-05, -79.27334962, -0.00022486, -264.24449873, -0.00074954, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 105.69779949, 0.01316842, 105.69779949, 0.03950526, 73.98845965, -1199.47668581, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 26.42444987, 7.495e-05, 79.27334962, 0.00022486, 264.24449873, 0.00074954, -26.42444987, -7.495e-05, -79.27334962, -0.00022486, -264.24449873, -0.00074954, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.9, 9.2, 3.725)
    ops.node(122016, 12.9, 9.2, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.09, 31022146.02594959, 12925894.177479, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 64.43152571, 0.00065488, 77.05219489, 0.01281159, 7.70521949, 0.05035809, -64.43152571, -0.00065488, -77.05219489, -0.01281159, -7.70521949, -0.05035809, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 60.83477347, 0.00065488, 72.75092076, 0.01281159, 7.27509208, 0.05035809, -60.83477347, -0.00065488, -72.75092076, -0.01281159, -7.27509208, -0.05035809, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 105.39438252, 0.01309765, 105.39438252, 0.03929296, 73.77606776, -1151.54985778, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 26.34859563, 7.338e-05, 79.04578689, 0.00022015, 263.48595629, 0.00073384, -26.34859563, -7.338e-05, -79.04578689, -0.00022015, -263.48595629, -0.00073384, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 105.39438252, 0.01309765, 105.39438252, 0.03929296, 73.77606776, -1151.54985778, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 26.34859563, 7.338e-05, 79.04578689, 0.00022015, 263.48595629, 0.00073384, -26.34859563, -7.338e-05, -79.04578689, -0.00022015, -263.48595629, -0.00073384, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 17.85, 9.2, 3.725)
    ops.node(122017, 17.85, 9.2, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.09, 29648948.29106077, 12353728.45460865, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 71.79274498, 0.00072939, 85.6409099, 0.0116345, 8.56409099, 0.04242573, -71.79274498, -0.00072939, -85.6409099, -0.0116345, -8.56409099, -0.04242573, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 68.74618455, 0.00072939, 82.00669578, 0.0116345, 8.20066958, 0.04242573, -68.74618455, -0.00072939, -82.00669578, -0.0116345, -8.20066958, -0.04242573, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 106.32193965, 0.01458773, 106.32193965, 0.04376318, 74.42535776, -1271.40568748, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 26.58048491, 7.746e-05, 79.74145474, 0.00023237, 265.80484913, 0.00077458, -26.58048491, -7.746e-05, -79.74145474, -0.00023237, -265.80484913, -0.00077458, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 106.32193965, 0.01458773, 106.32193965, 0.04376318, 74.42535776, -1271.40568748, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 26.58048491, 7.746e-05, 79.74145474, 0.00023237, 265.80484913, 0.00077458, -26.58048491, -7.746e-05, -79.74145474, -0.00023237, -265.80484913, -0.00077458, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 22.8, 9.2, 3.725)
    ops.node(122018, 22.8, 9.2, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.09, 31852761.18597458, 13271983.82748941, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 54.02017343, 0.00063956, 64.68408171, 0.0131005, 6.46840817, 0.05541145, -54.02017343, -0.00063956, -64.68408171, -0.0131005, -6.46840817, -0.05541145, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 51.23048509, 0.00063956, 61.34369206, 0.0131005, 6.13436921, 0.05541145, -51.23048509, -0.00063956, -61.34369206, -0.0131005, -6.13436921, -0.05541145, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 101.61686481, 0.01279117, 101.61686481, 0.03837351, 71.13180537, -1019.55710331, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 25.4042162, 6.891e-05, 76.21264861, 0.00020673, 254.04216202, 0.00068908, -25.4042162, -6.891e-05, -76.21264861, -0.00020673, -254.04216202, -0.00068908, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 101.61686481, 0.01279117, 101.61686481, 0.03837351, 71.13180537, -1019.55710331, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 25.4042162, 6.891e-05, 76.21264861, 0.00020673, 254.04216202, 0.00068908, -25.4042162, -6.891e-05, -76.21264861, -0.00020673, -254.04216202, -0.00068908, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.425)
    ops.node(123001, 0.0, 0.0, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 31093670.5558692, 12955696.0649455, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 29.1962274, 0.00071086, 35.05392363, 0.01487101, 3.50539236, 0.0639489, -29.1962274, -0.00071086, -35.05392363, -0.01487101, -3.50539236, -0.0639489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 29.1962274, 0.00071086, 35.05392363, 0.01487101, 3.50539236, 0.0639489, -29.1962274, -0.00071086, -35.05392363, -0.01487101, -3.50539236, -0.0639489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 73.79024725, 0.01421728, 73.79024725, 0.04265183, 51.65317308, -853.12538814, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 18.44756181, 7.381e-05, 55.34268544, 0.00022144, 184.47561814, 0.00073815, -18.44756181, -7.381e-05, -55.34268544, -0.00022144, -184.47561814, -0.00073815, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 73.79024725, 0.01421728, 73.79024725, 0.04265183, 51.65317308, -853.12538814, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 18.44756181, 7.381e-05, 55.34268544, 0.00022144, 184.47561814, 0.00073815, -18.44756181, -7.381e-05, -55.34268544, -0.00022144, -184.47561814, -0.00073815, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.95, 0.0, 6.425)
    ops.node(123002, 4.95, 0.0, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 31197529.69108484, 12998970.70461868, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 38.6787335, 0.00081858, 46.13076948, 0.01385306, 4.61307695, 0.0544991, -38.6787335, -0.00081858, -46.13076948, -0.01385306, -4.61307695, -0.0544991, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 38.6787335, 0.00081858, 46.13076948, 0.01385306, 4.61307695, 0.0544991, -38.6787335, -0.00081858, -46.13076948, -0.01385306, -4.61307695, -0.0544991, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 81.19917246, 0.01637159, 81.19917246, 0.04911478, 56.83942072, -979.58943395, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 20.29979312, 8.096e-05, 60.89937935, 0.00024287, 202.99793116, 0.00080956, -20.29979312, -8.096e-05, -60.89937935, -0.00024287, -202.99793116, -0.00080956, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 81.19917246, 0.01637159, 81.19917246, 0.04911478, 56.83942072, -979.58943395, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 20.29979312, 8.096e-05, 60.89937935, 0.00024287, 202.99793116, 0.00080956, -20.29979312, -8.096e-05, -60.89937935, -0.00024287, -202.99793116, -0.00080956, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 17.85, 0.0, 6.425)
    ops.node(123005, 17.85, 0.0, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 30639979.47479929, 12766658.1144997, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 38.69533928, 0.00078955, 46.18407832, 0.01220381, 4.61840783, 0.0516126, -38.69533928, -0.00078955, -46.18407832, -0.01220381, -4.61840783, -0.0516126, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 38.69533928, 0.00078955, 46.18407832, 0.01220381, 4.61840783, 0.0516126, -38.69533928, -0.00078955, -46.18407832, -0.01220381, -4.61840783, -0.0516126, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 73.64290129, 0.01579101, 73.64290129, 0.04737303, 51.5500309, -911.51783018, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 18.41072532, 7.476e-05, 55.23217597, 0.00022427, 184.10725323, 0.00074758, -18.41072532, -7.476e-05, -55.23217597, -0.00022427, -184.10725323, -0.00074758, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 73.64290129, 0.01579101, 73.64290129, 0.04737303, 51.5500309, -911.51783018, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 18.41072532, 7.476e-05, 55.23217597, 0.00022427, 184.10725323, 0.00074758, -18.41072532, -7.476e-05, -55.23217597, -0.00022427, -184.10725323, -0.00074758, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 22.8, 0.0, 6.425)
    ops.node(123006, 22.8, 0.0, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 32743280.02781167, 13643033.34492153, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 29.05248644, 0.00081519, 34.74312032, 0.01379429, 3.47431203, 0.06534408, -29.05248644, -0.00081519, -34.74312032, -0.01379429, -3.47431203, -0.06534408, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 29.05248644, 0.00081519, 34.74312032, 0.01379429, 3.47431203, 0.06534408, -29.05248644, -0.00081519, -34.74312032, -0.01379429, -3.47431203, -0.06534408, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 75.15320161, 0.01630383, 75.15320161, 0.0489115, 52.60724113, -795.90648738, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 18.7883004, 7.139e-05, 56.36490121, 0.00021417, 187.88300403, 0.00071391, -18.7883004, -7.139e-05, -56.36490121, -0.00021417, -187.88300403, -0.00071391, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 75.15320161, 0.01630383, 75.15320161, 0.0489115, 52.60724113, -795.90648738, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 18.7883004, 7.139e-05, 56.36490121, 0.00021417, 187.88300403, 0.00071391, -18.7883004, -7.139e-05, -56.36490121, -0.00021417, -187.88300403, -0.00071391, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.6, 6.45)
    ops.node(123007, 0.0, 4.6, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 31552901.56802548, 13147042.32001062, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 39.07705712, 0.00078598, 46.59271447, 0.01389522, 4.65927145, 0.05562284, -39.07705712, -0.00078598, -46.59271447, -0.01389522, -4.65927145, -0.05562284, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 39.07705712, 0.00078598, 46.59271447, 0.01389522, 4.65927145, 0.05562284, -39.07705712, -0.00078598, -46.59271447, -0.01389522, -4.65927145, -0.05562284, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 82.87807454, 0.01571951, 82.87807454, 0.04715854, 58.01465218, -1003.63546322, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 20.71951864, 8.17e-05, 62.15855591, 0.0002451, 207.19518635, 0.00081699, -20.71951864, -8.17e-05, -62.15855591, -0.0002451, -207.19518635, -0.00081699, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 82.87807454, 0.01571951, 82.87807454, 0.04715854, 58.01465218, -1003.63546322, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 20.71951864, 8.17e-05, 62.15855591, 0.0002451, 207.19518635, 0.00081699, -20.71951864, -8.17e-05, -62.15855591, -0.0002451, -207.19518635, -0.00081699, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.95, 4.6, 6.45)
    ops.node(123008, 4.95, 4.6, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 29383932.72866164, 12243305.30360902, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 56.35950378, 0.00083446, 66.87943472, 0.01135172, 6.68794347, 0.0371072, -56.35950378, -0.00083446, -66.87943472, -0.01135172, -6.68794347, -0.0371072, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 56.35950378, 0.00083446, 66.87943472, 0.01135172, 6.68794347, 0.0371072, -56.35950378, -0.00083446, -66.87943472, -0.01135172, -6.68794347, -0.0371072, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 64.44317126, 0.01668926, 64.44317126, 0.05006777, 45.11021988, -979.58638593, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 16.11079281, 6.822e-05, 48.33237844, 0.00020465, 161.10792814, 0.00068216, -16.11079281, -6.822e-05, -48.33237844, -0.00020465, -161.10792814, -0.00068216, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 64.44317126, 0.01668926, 64.44317126, 0.05006777, 45.11021988, -979.58638593, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 16.11079281, 6.822e-05, 48.33237844, 0.00020465, 161.10792814, 0.00068216, -16.11079281, -6.822e-05, -48.33237844, -0.00020465, -161.10792814, -0.00068216, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.9, 4.6, 6.45)
    ops.node(123009, 9.9, 4.6, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 32173567.68366997, 13405653.20152915, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 53.24212291, 0.00080627, 63.22155867, 0.01284469, 6.32215587, 0.04691985, -53.24212291, -0.00080627, -63.22155867, -0.01284469, -6.32215587, -0.04691985, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 53.24212291, 0.00080627, 63.22155867, 0.01284469, 6.32215587, 0.04691985, -53.24212291, -0.00080627, -63.22155867, -0.01284469, -6.32215587, -0.04691985, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 72.70838612, 0.01612532, 72.70838612, 0.04837595, 50.89587029, -953.92481134, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 18.17709653, 7.029e-05, 54.53128959, 0.00021087, 181.77096531, 0.00070291, -18.17709653, -7.029e-05, -54.53128959, -0.00021087, -181.77096531, -0.00070291, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 72.70838612, 0.01612532, 72.70838612, 0.04837595, 50.89587029, -953.92481134, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 18.17709653, 7.029e-05, 54.53128959, 0.00021087, 181.77096531, 0.00070291, -18.17709653, -7.029e-05, -54.53128959, -0.00021087, -181.77096531, -0.00070291, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.9, 4.6, 6.45)
    ops.node(123010, 12.9, 4.6, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0625, 34740952.45671548, 14475396.85696478, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 51.60806444, 0.00082441, 60.93102828, 0.01327954, 6.09310283, 0.05170867, -51.60806444, -0.00082441, -60.93102828, -0.01327954, -6.09310283, -0.05170867, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 51.60806444, 0.00082441, 60.93102828, 0.01327954, 6.09310283, 0.05170867, -51.60806444, -0.00082441, -60.93102828, -0.01327954, -6.09310283, -0.05170867, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 80.40072306, 0.0164883, 80.40072306, 0.04946489, 56.28050614, -950.53372606, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 20.10018077, 7.198e-05, 60.3005423, 0.00021595, 201.00180765, 0.00071984, -20.10018077, -7.198e-05, -60.3005423, -0.00021595, -201.00180765, -0.00071984, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 80.40072306, 0.0164883, 80.40072306, 0.04946489, 56.28050614, -950.53372606, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 20.10018077, 7.198e-05, 60.3005423, 0.00021595, 201.00180765, 0.00071984, -20.10018077, -7.198e-05, -60.3005423, -0.00021595, -201.00180765, -0.00071984, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 17.85, 4.6, 6.45)
    ops.node(123011, 17.85, 4.6, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.0625, 31173006.9773976, 12988752.907249, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 54.86104745, 0.00084234, 65.06776674, 0.0135157, 6.50677667, 0.04329868, -54.86104745, -0.00084234, -65.06776674, -0.0135157, -6.50677667, -0.04329868, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 54.86104745, 0.00084234, 65.06776674, 0.0135157, 6.50677667, 0.04329868, -54.86104745, -0.00084234, -65.06776674, -0.0135157, -6.50677667, -0.04329868, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 81.2657666, 0.01684681, 81.2657666, 0.05054043, 56.88603662, -1033.29097547, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 20.31644165, 8.109e-05, 60.94932495, 0.00024326, 203.16441649, 0.00081086, -20.31644165, -8.109e-05, -60.94932495, -0.00024326, -203.16441649, -0.00081086, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 81.2657666, 0.01684681, 81.2657666, 0.05054043, 56.88603662, -1033.29097547, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 20.31644165, 8.109e-05, 60.94932495, 0.00024326, 203.16441649, 0.00081086, -20.31644165, -8.109e-05, -60.94932495, -0.00024326, -203.16441649, -0.00081086, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 22.8, 4.6, 6.45)
    ops.node(123012, 22.8, 4.6, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 33548430.65450311, 13978512.77270963, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 39.4249115, 0.00076023, 46.81115927, 0.01397352, 4.68111593, 0.05951183, -39.4249115, -0.00076023, -46.81115927, -0.01397352, -4.68111593, -0.05951183, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 39.4249115, 0.00076023, 46.81115927, 0.01397352, 4.68111593, 0.05951183, -39.4249115, -0.00076023, -46.81115927, -0.01397352, -4.68111593, -0.05951183, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 86.90436747, 0.0152046, 86.90436747, 0.04561381, 60.83305723, -996.99803286, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 21.72609187, 8.057e-05, 65.17827561, 0.00024172, 217.26091869, 0.00080572, -21.72609187, -8.057e-05, -65.17827561, -0.00024172, -217.26091869, -0.00080572, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 86.90436747, 0.0152046, 86.90436747, 0.04561381, 60.83305723, -996.99803286, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 21.72609187, 8.057e-05, 65.17827561, 0.00024172, 217.26091869, 0.00080572, -21.72609187, -8.057e-05, -65.17827561, -0.00024172, -217.26091869, -0.00080572, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.2, 6.425)
    ops.node(123013, 0.0, 9.2, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 30419003.01311731, 12674584.58879888, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 29.28451721, 0.00073643, 35.20625981, 0.01575456, 3.52062598, 0.06369008, -29.28451721, -0.00073643, -35.20625981, -0.01575456, -3.52062598, -0.06369008, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 29.28451721, 0.00073643, 35.20625981, 0.01575456, 3.52062598, 0.06369008, -29.28451721, -0.00073643, -35.20625981, -0.01575456, -3.52062598, -0.06369008, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 74.4397917, 0.01472853, 74.4397917, 0.04418559, 52.10785419, -912.56303228, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 18.60994792, 7.612e-05, 55.82984377, 0.00022835, 186.09947924, 0.00076116, -18.60994792, -7.612e-05, -55.82984377, -0.00022835, -186.09947924, -0.00076116, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 74.4397917, 0.01472853, 74.4397917, 0.04418559, 52.10785419, -912.56303228, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 18.60994792, 7.612e-05, 55.82984377, 0.00022835, 186.09947924, 0.00076116, -18.60994792, -7.612e-05, -55.82984377, -0.00022835, -186.09947924, -0.00076116, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.95, 9.2, 6.425)
    ops.node(123014, 4.95, 9.2, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 31490873.63180486, 13121197.34658536, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 39.76174195, 0.00080386, 47.4014168, 0.01249151, 4.74014168, 0.05376527, -39.76174195, -0.00080386, -47.4014168, -0.01249151, -4.74014168, -0.05376527, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 39.76174195, 0.00080386, 47.4014168, 0.01249151, 4.74014168, 0.05376527, -39.76174195, -0.00080386, -47.4014168, -0.01249151, -4.74014168, -0.05376527, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 78.33624433, 0.01607721, 78.33624433, 0.04823163, 54.83537103, -906.86159618, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 19.58406108, 7.737e-05, 58.75218325, 0.00023212, 195.84061083, 0.00077374, -19.58406108, -7.737e-05, -58.75218325, -0.00023212, -195.84061083, -0.00077374, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 78.33624433, 0.01607721, 78.33624433, 0.04823163, 54.83537103, -906.86159618, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 19.58406108, 7.737e-05, 58.75218325, 0.00023212, 195.84061083, 0.00077374, -19.58406108, -7.737e-05, -58.75218325, -0.00023212, -195.84061083, -0.00077374, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.9, 9.2, 6.425)
    ops.node(123015, 9.9, 9.2, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 30833253.78289012, 12847189.07620422, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 33.80014986, 0.00079212, 40.47503992, 0.01311338, 4.04750399, 0.05738978, -33.80014986, -0.00079212, -40.47503992, -0.01311338, -4.04750399, -0.05738978, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 33.80014986, 0.00079212, 40.47503992, 0.01311338, 4.04750399, 0.05738978, -33.80014986, -0.00079212, -40.47503992, -0.01311338, -4.04750399, -0.05738978, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 73.7587792, 0.01584239, 73.7587792, 0.04752718, 51.63114544, -862.39323613, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 18.4396948, 7.441e-05, 55.3190844, 0.00022322, 184.396948, 0.00074406, -18.4396948, -7.441e-05, -55.3190844, -0.00022322, -184.396948, -0.00074406, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 73.7587792, 0.01584239, 73.7587792, 0.04752718, 51.63114544, -862.39323613, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 18.4396948, 7.441e-05, 55.3190844, 0.00022322, 184.396948, 0.00074406, -18.4396948, -7.441e-05, -55.3190844, -0.00022322, -184.396948, -0.00074406, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.9, 9.2, 6.425)
    ops.node(123016, 12.9, 9.2, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 30876581.74064044, 12865242.39193352, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 34.51029889, 0.00072736, 41.32247305, 0.01402082, 4.1322473, 0.05838278, -34.51029889, -0.00072736, -41.32247305, -0.01402082, -4.1322473, -0.05838278, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 34.51029889, 0.00072736, 41.32247305, 0.01402082, 4.1322473, 0.05838278, -34.51029889, -0.00072736, -41.32247305, -0.01402082, -4.1322473, -0.05838278, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 76.077112, 0.01454728, 76.077112, 0.04364184, 53.2539784, -885.30514611, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 19.019278, 7.664e-05, 57.057834, 0.00022991, 190.19278001, 0.00076637, -19.019278, -7.664e-05, -57.057834, -0.00022991, -190.19278001, -0.00076637, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 76.077112, 0.01454728, 76.077112, 0.04364184, 53.2539784, -885.30514611, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 19.019278, 7.664e-05, 57.057834, 0.00022991, 190.19278001, 0.00076637, -19.019278, -7.664e-05, -57.057834, -0.00022991, -190.19278001, -0.00076637, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 17.85, 9.2, 6.425)
    ops.node(123017, 17.85, 9.2, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 32628585.07440268, 13595243.78100112, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 40.14629711, 0.00076688, 47.75924088, 0.01436982, 4.77592409, 0.05793193, -40.14629711, -0.00076688, -47.75924088, -0.01436982, -4.77592409, -0.05793193, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 40.14629711, 0.00076688, 47.75924088, 0.01436982, 4.77592409, 0.05793193, -40.14629711, -0.00076688, -47.75924088, -0.01436982, -4.77592409, -0.05793193, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 86.44009682, 0.01533756, 86.44009682, 0.04601267, 60.50806778, -1034.20552105, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 21.61002421, 8.24e-05, 64.83007262, 0.0002472, 216.10024206, 0.00082401, -21.61002421, -8.24e-05, -64.83007262, -0.0002472, -216.10024206, -0.00082401, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 86.44009682, 0.01533756, 86.44009682, 0.04601267, 60.50806778, -1034.20552105, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 21.61002421, 8.24e-05, 64.83007262, 0.0002472, 216.10024206, 0.00082401, -21.61002421, -8.24e-05, -64.83007262, -0.0002472, -216.10024206, -0.00082401, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 22.8, 9.2, 6.425)
    ops.node(123018, 22.8, 9.2, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 31340563.46419737, 13058568.11008224, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 29.41965127, 0.0007266, 35.30355478, 0.01551178, 3.53035548, 0.06498771, -29.41965127, -0.0007266, -35.30355478, -0.01551178, -3.53035548, -0.06498771, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 29.41965127, 0.0007266, 35.30355478, 0.01551178, 3.53035548, 0.06498771, -29.41965127, -0.0007266, -35.30355478, -0.01551178, -3.53035548, -0.06498771, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 74.65066151, 0.01453202, 74.65066151, 0.04359605, 52.25546306, -863.87657081, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 18.66266538, 7.409e-05, 55.98799613, 0.00022226, 186.62665378, 0.00074087, -18.66266538, -7.409e-05, -55.98799613, -0.00022226, -186.62665378, -0.00074087, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 74.65066151, 0.01453202, 74.65066151, 0.04359605, 52.25546306, -863.87657081, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 18.66266538, 7.409e-05, 55.98799613, 0.00022226, 186.62665378, 0.00074087, -18.66266538, -7.409e-05, -55.98799613, -0.00022226, -186.62665378, -0.00074087, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.125)
    ops.node(124001, 0.0, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 34483736.1112569, 14368223.37969038, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 18.64834064, 0.00063735, 22.2921704, 0.01378323, 2.22921704, 0.07596425, -18.64834064, -0.00063735, -22.2921704, -0.01378323, -2.22921704, -0.07596425, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 18.64834064, 0.00063735, 22.2921704, 0.01378323, 2.22921704, 0.07596425, -18.64834064, -0.00063735, -22.2921704, -0.01378323, -2.22921704, -0.07596425, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 64.07867695, 0.01274693, 64.07867695, 0.0382408, 44.85507387, -798.09018511, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 16.01966924, 5.78e-05, 48.05900771, 0.0001734, 160.19669238, 0.00057798, -16.01966924, -5.78e-05, -48.05900771, -0.0001734, -160.19669238, -0.00057798, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 64.07867695, 0.01274693, 64.07867695, 0.0382408, 44.85507387, -798.09018511, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 16.01966924, 5.78e-05, 48.05900771, 0.0001734, 160.19669238, 0.00057798, -16.01966924, -5.78e-05, -48.05900771, -0.0001734, -160.19669238, -0.00057798, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.95, 0.0, 9.125)
    ops.node(124002, 4.95, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 31381350.19339714, 13075562.58058214, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 22.66452025, 0.0007712, 27.29942843, 0.01400293, 2.72994284, 0.06954118, -22.66452025, -0.0007712, -27.29942843, -0.01400293, -2.72994284, -0.06954118, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 22.66452025, 0.0007712, 27.29942843, 0.01400293, 2.72994284, 0.06954118, -22.66452025, -0.0007712, -27.29942843, -0.01400293, -2.72994284, -0.06954118, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 62.63683216, 0.01542406, 62.63683216, 0.04627217, 43.84578251, -715.85262347, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 15.65920804, 6.208e-05, 46.97762412, 0.00018625, 156.5920804, 0.00062083, -15.65920804, -6.208e-05, -46.97762412, -0.00018625, -156.5920804, -0.00062083, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 62.63683216, 0.01542406, 62.63683216, 0.04627217, 43.84578251, -715.85262347, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 15.65920804, 6.208e-05, 46.97762412, 0.00018625, 156.5920804, 0.00062083, -15.65920804, -6.208e-05, -46.97762412, -0.00018625, -156.5920804, -0.00062083, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 17.85, 0.0, 9.125)
    ops.node(124005, 17.85, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 28676680.34297918, 11948616.80957466, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 23.42533496, 0.00069107, 28.37995458, 0.01585502, 2.83799546, 0.06787423, -23.42533496, -0.00069107, -28.37995458, -0.01585502, -2.83799546, -0.06787423, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 23.42533496, 0.00069107, 28.37995458, 0.01585502, 2.83799546, 0.06787423, -23.42533496, -0.00069107, -28.37995458, -0.01585502, -2.83799546, -0.06787423, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 63.59051553, 0.01382141, 63.59051553, 0.04146423, 44.51336087, -807.06142658, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 15.89762888, 6.897e-05, 47.69288664, 0.00020692, 158.97628881, 0.00068973, -15.89762888, -6.897e-05, -47.69288664, -0.00020692, -158.97628881, -0.00068973, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 63.59051553, 0.01382141, 63.59051553, 0.04146423, 44.51336087, -807.06142658, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 15.89762888, 6.897e-05, 47.69288664, 0.00020692, 158.97628881, 0.00068973, -15.89762888, -6.897e-05, -47.69288664, -0.00020692, -158.97628881, -0.00068973, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 22.8, 0.0, 9.125)
    ops.node(124006, 22.8, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 30540629.80366812, 12725262.41819505, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 18.15141113, 0.00067065, 21.97783649, 0.01746148, 2.19778365, 0.07739411, -18.15141113, -0.00067065, -21.97783649, -0.01746148, -2.19778365, -0.07739411, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 18.15141113, 0.00067065, 21.97783649, 0.01746148, 2.19778365, 0.07739411, -18.15141113, -0.00067065, -21.97783649, -0.01746148, -2.19778365, -0.07739411, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 65.7674537, 0.01341294, 65.7674537, 0.04023881, 46.03721759, -1062.51255413, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 16.44186343, 6.698e-05, 49.32559028, 0.00020094, 164.41863426, 0.00066981, -16.44186343, -6.698e-05, -49.32559028, -0.00020094, -164.41863426, -0.00066981, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 65.7674537, 0.01341294, 65.7674537, 0.04023881, 46.03721759, -1062.51255413, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 16.44186343, 6.698e-05, 49.32559028, 0.00020094, 164.41863426, 0.00066981, -16.44186343, -6.698e-05, -49.32559028, -0.00020094, -164.41863426, -0.00066981, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.6, 9.15)
    ops.node(124007, 0.0, 4.6, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 33180308.59191259, 13825128.57996358, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 23.66829169, 0.00069737, 28.35879842, 0.01499854, 2.83587984, 0.0722645, -23.66829169, -0.00069737, -28.35879842, -0.01499854, -2.83587984, -0.0722645, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 23.66829169, 0.00069737, 28.35879842, 0.01499854, 2.83587984, 0.0722645, -23.66829169, -0.00069737, -28.35879842, -0.01499854, -2.83587984, -0.0722645, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 72.10537625, 0.01394744, 72.10537625, 0.04184233, 50.47376338, -797.47254147, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 18.02634406, 6.759e-05, 54.07903219, 0.00020278, 180.26344064, 0.00067593, -18.02634406, -6.759e-05, -54.07903219, -0.00020278, -180.26344064, -0.00067593, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 72.10537625, 0.01394744, 72.10537625, 0.04184233, 50.47376338, -797.47254147, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 18.02634406, 6.759e-05, 54.07903219, 0.00020278, 180.26344064, 0.00067593, -18.02634406, -6.759e-05, -54.07903219, -0.00020278, -180.26344064, -0.00067593, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.95, 4.6, 9.15)
    ops.node(124008, 4.95, 4.6, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 30732571.37929501, 12805238.07470626, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 38.65979076, 0.00080994, 46.44133016, 0.01475205, 4.64413302, 0.05654831, -38.65979076, -0.00080994, -46.44133016, -0.01475205, -4.64413302, -0.05654831, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 38.65979076, 0.00080994, 46.44133016, 0.01475205, 4.64413302, 0.05654831, -38.65979076, -0.00080994, -46.44133016, -0.01475205, -4.64413302, -0.05654831, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 61.06196442, 0.01619881, 61.06196442, 0.04859642, 42.74337509, -724.06495072, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 15.2654911, 6.18e-05, 45.79647331, 0.0001854, 152.65491105, 0.000618, -15.2654911, -6.18e-05, -45.79647331, -0.0001854, -152.65491105, -0.000618, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 61.06196442, 0.01619881, 61.06196442, 0.04859642, 42.74337509, -724.06495072, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 15.2654911, 6.18e-05, 45.79647331, 0.0001854, 152.65491105, 0.000618, -15.2654911, -6.18e-05, -45.79647331, -0.0001854, -152.65491105, -0.000618, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.9, 4.6, 9.15)
    ops.node(124009, 9.9, 4.6, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 27774971.16689382, 11572904.65287242, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 35.92046477, 0.000721, 43.42396904, 0.01661415, 4.3423969, 0.05609308, -35.92046477, -0.000721, -43.42396904, -0.01661415, -4.3423969, -0.05609308, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 35.92046477, 0.000721, 43.42396904, 0.01661415, 4.3423969, 0.05609308, -35.92046477, -0.000721, -43.42396904, -0.01661415, -4.3423969, -0.05609308, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 61.90372897, 0.01441997, 61.90372897, 0.04325991, 43.33261028, -734.96360914, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 15.47593224, 6.932e-05, 46.42779673, 0.00020797, 154.75932242, 0.00069323, -15.47593224, -6.932e-05, -46.42779673, -0.00020797, -154.75932242, -0.00069323, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 61.90372897, 0.01441997, 61.90372897, 0.04325991, 43.33261028, -734.96360914, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 15.47593224, 6.932e-05, 46.42779673, 0.00020797, 154.75932242, 0.00069323, -15.47593224, -6.932e-05, -46.42779673, -0.00020797, -154.75932242, -0.00069323, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.9, 4.6, 9.15)
    ops.node(124010, 12.9, 4.6, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0625, 29920603.87423344, 12466918.2809306, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 36.20557837, 0.00075171, 43.64039506, 0.01449115, 4.36403951, 0.05745762, -36.20557837, -0.00075171, -43.64039506, -0.01449115, -4.36403951, -0.05745762, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 36.20557837, 0.00075171, 43.64039506, 0.01449115, 4.36403951, 0.05745762, -36.20557837, -0.00075171, -43.64039506, -0.01449115, -4.36403951, -0.05745762, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 51.97113698, 0.01503411, 51.97113698, 0.04510234, 36.37979589, -655.32943811, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 12.99278424, 5.403e-05, 38.97835273, 0.00016208, 129.92784245, 0.00054027, -12.99278424, -5.403e-05, -38.97835273, -0.00016208, -129.92784245, -0.00054027, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 51.97113698, 0.01503411, 51.97113698, 0.04510234, 36.37979589, -655.32943811, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 12.99278424, 5.403e-05, 38.97835273, 0.00016208, 129.92784245, 0.00054027, -12.99278424, -5.403e-05, -38.97835273, -0.00016208, -129.92784245, -0.00054027, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 17.85, 4.6, 9.15)
    ops.node(124011, 17.85, 4.6, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.0625, 28494389.09857085, 11872662.12440452, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 38.32721972, 0.00077865, 46.19150041, 0.01417683, 4.61915004, 0.05221876, -38.32721972, -0.00077865, -46.19150041, -0.01417683, -4.61915004, -0.05221876, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 38.32721972, 0.00077865, 46.19150041, 0.01417683, 4.61915004, 0.05221876, -38.32721972, -0.00077865, -46.19150041, -0.01417683, -4.61915004, -0.05221876, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 52.47505118, 0.01557306, 52.47505118, 0.04671918, 36.73253582, -702.36109811, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 13.11876279, 5.728e-05, 39.35628838, 0.00017184, 131.18762794, 0.00057281, -13.11876279, -5.728e-05, -39.35628838, -0.00017184, -131.18762794, -0.00057281, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 52.47505118, 0.01557306, 52.47505118, 0.04671918, 36.73253582, -702.36109811, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 13.11876279, 5.728e-05, 39.35628838, 0.00017184, 131.18762794, 0.00057281, -13.11876279, -5.728e-05, -39.35628838, -0.00017184, -131.18762794, -0.00057281, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 22.8, 4.6, 9.15)
    ops.node(124012, 22.8, 4.6, 11.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 36225502.4401664, 15093959.35006933, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 23.59776207, 0.00065506, 27.95695216, 0.0139199, 2.79569522, 0.07350051, -23.59776207, -0.00065506, -27.95695216, -0.0139199, -2.79569522, -0.07350051, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 23.59776207, 0.00065506, 27.95695216, 0.0139199, 2.79569522, 0.07350051, -23.59776207, -0.00065506, -27.95695216, -0.0139199, -2.79569522, -0.07350051, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 77.31343437, 0.01310128, 77.31343437, 0.03930383, 54.11940406, -758.21754827, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 19.32835859, 6.638e-05, 57.98507578, 0.00019915, 193.28358593, 0.00066383, -19.32835859, -6.638e-05, -57.98507578, -0.00019915, -193.28358593, -0.00066383, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 77.31343437, 0.01310128, 77.31343437, 0.03930383, 54.11940406, -758.21754827, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 19.32835859, 6.638e-05, 57.98507578, 0.00019915, 193.28358593, 0.00066383, -19.32835859, -6.638e-05, -57.98507578, -0.00019915, -193.28358593, -0.00066383, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.2, 9.125)
    ops.node(124013, 0.0, 9.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 34914939.33983225, 14547891.39159677, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 18.79852303, 0.00068119, 22.43389115, 0.01380294, 2.24338912, 0.07617048, -18.79852303, -0.00068119, -22.43389115, -0.01380294, -2.24338912, -0.07617048, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 18.79852303, 0.00068119, 22.43389115, 0.01380294, 2.24338912, 0.07617048, -18.79852303, -0.00068119, -22.43389115, -0.01380294, -2.24338912, -0.07617048, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 67.24526125, 0.0136238, 67.24526125, 0.0408714, 47.07168287, -803.5993865, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 16.81131531, 5.991e-05, 50.43394594, 0.00017972, 168.11315312, 0.00059905, -16.81131531, -5.991e-05, -50.43394594, -0.00017972, -168.11315312, -0.00059905, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 67.24526125, 0.0136238, 67.24526125, 0.0408714, 47.07168287, -803.5993865, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 16.81131531, 5.991e-05, 50.43394594, 0.00017972, 168.11315312, 0.00059905, -16.81131531, -5.991e-05, -50.43394594, -0.00017972, -168.11315312, -0.00059905, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.95, 9.2, 9.125)
    ops.node(124014, 4.95, 9.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 32789356.50358199, 13662231.87649249, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 23.30258254, 0.00069544, 27.95588659, 0.01402755, 2.79558866, 0.07099582, -23.30258254, -0.00069544, -27.95588659, -0.01402755, -2.79558866, -0.07099582, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 23.30258254, 0.00069544, 27.95588659, 0.01402755, 2.79558866, 0.07099582, -23.30258254, -0.00069544, -27.95588659, -0.01402755, -2.79558866, -0.07099582, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 66.74619484, 0.01390877, 66.74619484, 0.04172632, 46.72233639, -724.29401942, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 16.68654871, 6.332e-05, 50.05964613, 0.00018995, 166.86548711, 0.00063315, -16.68654871, -6.332e-05, -50.05964613, -0.00018995, -166.86548711, -0.00063315, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 66.74619484, 0.01390877, 66.74619484, 0.04172632, 46.72233639, -724.29401942, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 16.68654871, 6.332e-05, 50.05964613, 0.00018995, 166.86548711, 0.00063315, -16.68654871, -6.332e-05, -50.05964613, -0.00018995, -166.86548711, -0.00063315, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.9, 9.2, 9.125)
    ops.node(124015, 9.9, 9.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 31659380.94517132, 13191408.72715472, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 20.43578507, 0.00069212, 24.62805795, 0.01663539, 2.46280579, 0.07463232, -20.43578507, -0.00069212, -24.62805795, -0.01663539, -2.46280579, -0.07463232, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 20.43578507, 0.00069212, 24.62805795, 0.01663539, 2.46280579, 0.07463232, -20.43578507, -0.00069212, -24.62805795, -0.01663539, -2.46280579, -0.07463232, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 68.08282202, 0.01384248, 68.08282202, 0.04152745, 47.65797541, -854.42084682, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 17.02070551, 6.689e-05, 51.06211652, 0.00020067, 170.20705505, 0.00066888, -17.02070551, -6.689e-05, -51.06211652, -0.00020067, -170.20705505, -0.00066888, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 68.08282202, 0.01384248, 68.08282202, 0.04152745, 47.65797541, -854.42084682, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 17.02070551, 6.689e-05, 51.06211652, 0.00020067, 170.20705505, 0.00066888, -17.02070551, -6.689e-05, -51.06211652, -0.00020067, -170.20705505, -0.00066888, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.9, 9.2, 9.125)
    ops.node(124016, 12.9, 9.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 32553738.24122203, 13564057.60050918, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 21.25836948, 0.00068164, 25.55131016, 0.01672512, 2.55513102, 0.07546465, -21.25836948, -0.00068164, -25.55131016, -0.01672512, -2.55513102, -0.07546465, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 21.25836948, 0.00068164, 25.55131016, 0.01672512, 2.55513102, 0.07546465, -21.25836948, -0.00068164, -25.55131016, -0.01672512, -2.55513102, -0.07546465, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 71.4407404, 0.01363284, 71.4407404, 0.04089851, 50.00851828, -922.92916782, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 17.8601851, 6.826e-05, 53.5805553, 0.00020478, 178.60185101, 0.00068259, -17.8601851, -6.826e-05, -53.5805553, -0.00020478, -178.60185101, -0.00068259, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 71.4407404, 0.01363284, 71.4407404, 0.04089851, 50.00851828, -922.92916782, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 17.8601851, 6.826e-05, 53.5805553, 0.00020478, 178.60185101, 0.00068259, -17.8601851, -6.826e-05, -53.5805553, -0.00020478, -178.60185101, -0.00068259, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 17.85, 9.2, 9.125)
    ops.node(124017, 17.85, 9.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 29433028.67200749, 12263761.94666979, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 23.20915147, 0.00068857, 28.07969086, 0.01598593, 2.80796909, 0.06910732, -23.20915147, -0.00068857, -28.07969086, -0.01598593, -2.80796909, -0.06910732, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 23.20915147, 0.00068857, 28.07969086, 0.01598593, 2.80796909, 0.06910732, -23.20915147, -0.00068857, -28.07969086, -0.01598593, -2.80796909, -0.06910732, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 65.08853796, 0.01377132, 65.08853796, 0.04131395, 45.56197657, -810.20469291, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 16.27213449, 6.878e-05, 48.81640347, 0.00020635, 162.72134489, 0.00068784, -16.27213449, -6.878e-05, -48.81640347, -0.00020635, -162.72134489, -0.00068784, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 65.08853796, 0.01377132, 65.08853796, 0.04131395, 45.56197657, -810.20469291, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 16.27213449, 6.878e-05, 48.81640347, 0.00020635, 162.72134489, 0.00068784, -16.27213449, -6.878e-05, -48.81640347, -0.00020635, -162.72134489, -0.00068784, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 22.8, 9.2, 9.125)
    ops.node(124018, 22.8, 9.2, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 30170868.96795686, 12571195.40331536, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 18.31856632, 0.00065458, 22.20166804, 0.01505565, 2.2201668, 0.07471412, -18.31856632, -0.00065458, -22.20166804, -0.01505565, -2.2201668, -0.07471412, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 18.31856632, 0.00065458, 22.20166804, 0.01505565, 2.2201668, 0.07471412, -18.31856632, -0.00065458, -22.20166804, -0.01505565, -2.2201668, -0.07471412, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 56.0588533, 0.01309161, 56.0588533, 0.03927482, 39.24119731, -763.3076955, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 14.01471333, 5.779e-05, 42.04413998, 0.00017338, 140.14713326, 0.00057793, -14.01471333, -5.779e-05, -42.04413998, -0.00017338, -140.14713326, -0.00057793, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 56.0588533, 0.01309161, 56.0588533, 0.03927482, 39.24119731, -763.3076955, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 14.01471333, 5.779e-05, 42.04413998, 0.00017338, 140.14713326, 0.00057793, -14.01471333, -5.779e-05, -42.04413998, -0.00017338, -140.14713326, -0.00057793, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.9, 0.0, 0.0)
    ops.node(124019, 9.9, 0.0, 1.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 170003, 124019, 0.09, 31286074.76146504, 13035864.48394377, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 105.34350954, 0.00057839, 124.79203911, 0.01918843, 12.47920391, 0.06313569, -105.34350954, -0.00057839, -124.79203911, -0.01918843, -12.47920391, -0.06313569, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 101.62237543, 0.00057839, 120.38390883, 0.01918843, 12.03839088, 0.06313569, -101.62237543, -0.00057839, -120.38390883, -0.01918843, -12.03839088, -0.06313569, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 144.21270507, 0.01156779, 144.21270507, 0.03470336, 100.94889355, -2845.20069916, 0.05, 2, 0, 70003, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 36.05317627, 6.453e-05, 108.1595288, 0.0001936, 360.53176267, 0.00064533, -36.05317627, -6.453e-05, -108.1595288, -0.0001936, -360.53176267, -0.00064533, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 144.21270507, 0.01156779, 144.21270507, 0.03470336, 100.94889355, -2845.20069916, 0.05, 2, 0, 70003, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 36.05317627, 6.453e-05, 108.1595288, 0.0001936, 360.53176267, 0.00064533, -36.05317627, -6.453e-05, -108.1595288, -0.0001936, -360.53176267, -0.00064533, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 9.9, 0.0, 1.95)
    ops.node(121003, 9.9, 0.0, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 121003, 0.09, 30493132.69180626, 12705471.95491927, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 86.16353069, 0.00060148, 102.31274414, 0.01952411, 10.23127441, 0.06329301, -86.16353069, -0.00060148, -102.31274414, -0.01952411, -10.23127441, -0.06329301, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 80.1687162, 0.00060148, 95.19435059, 0.01952411, 9.51943506, 0.06329301, -80.1687162, -0.00060148, -95.19435059, -0.01952411, -9.51943506, -0.06329301, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 142.57904039, 0.01202956, 142.57904039, 0.03608867, 99.80532828, -2895.50656098, 0.05, 2, 0, 74019, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 35.6447601, 6.546e-05, 106.93428029, 0.00019638, 356.44760098, 0.00065461, -35.6447601, -6.546e-05, -106.93428029, -0.00019638, -356.44760098, -0.00065461, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 142.57904039, 0.01202956, 142.57904039, 0.03608867, 99.80532828, -2895.50656098, 0.05, 2, 0, 74019, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 35.6447601, 6.546e-05, 106.93428029, 0.00019638, 356.44760098, 0.00065461, -35.6447601, -6.546e-05, -106.93428029, -0.00019638, -356.44760098, -0.00065461, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.9, 0.0, 0.0)
    ops.node(124020, 12.9, 0.0, 1.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 170004, 124020, 0.09, 28169917.09349846, 11737465.45562436, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 103.86497466, 0.00061912, 122.95196795, 0.01751203, 12.29519679, 0.05040287, -103.86497466, -0.00061912, -122.95196795, -0.01751203, -12.29519679, -0.05040287, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 100.40116584, 0.00061912, 118.85162409, 0.01751203, 11.88516241, 0.05040287, -100.40116584, -0.00061912, -118.85162409, -0.01751203, -11.88516241, -0.05040287, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 133.05008303, 0.01238247, 133.05008303, 0.03714742, 93.13505812, -2832.21314139, 0.05, 2, 0, 70004, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 33.26252076, 6.612e-05, 99.78756227, 0.00019837, 332.62520757, 0.00066124, -33.26252076, -6.612e-05, -99.78756227, -0.00019837, -332.62520757, -0.00066124, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 133.05008303, 0.01238247, 133.05008303, 0.03714742, 93.13505812, -2832.21314139, 0.05, 2, 0, 70004, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 33.26252076, 6.612e-05, 99.78756227, 0.00019837, 332.62520757, 0.00066124, -33.26252076, -6.612e-05, -99.78756227, -0.00019837, -332.62520757, -0.00066124, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 12.9, 0.0, 1.95)
    ops.node(121004, 12.9, 0.0, 3.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 121004, 0.09, 35409311.70032092, 14753879.87513372, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 90.1111295, 0.00056998, 106.05021898, 0.01907135, 10.6050219, 0.07659098, -90.1111295, -0.00056998, -106.05021898, -0.01907135, -10.6050219, -0.07659098, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 83.0588905, 0.00056998, 97.75056173, 0.01907135, 9.77505617, 0.07659098, -83.0588905, -0.00056998, -97.75056173, -0.01907135, -9.77505617, -0.07659098, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 157.82837945, 0.01139965, 157.82837945, 0.03419894, 110.47986561, -2810.69798517, 0.05, 2, 0, 74020, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 39.45709486, 6.24e-05, 118.37128458, 0.0001872, 394.57094862, 0.00062402, -39.45709486, -6.24e-05, -118.37128458, -0.0001872, -394.57094862, -0.00062402, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 157.82837945, 0.01139965, 157.82837945, 0.03419894, 110.47986561, -2810.69798517, 0.05, 2, 0, 74020, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 39.45709486, 6.24e-05, 118.37128458, 0.0001872, 394.57094862, 0.00062402, -39.45709486, -6.24e-05, -118.37128458, -0.0001872, -394.57094862, -0.00062402, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.9, 0.0, 3.725)
    ops.node(124021, 9.9, 0.0, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 171003, 124021, 0.09, 30898239.49953636, 12874266.45814015, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 69.70872693, 0.00051311, 83.12969695, 0.01283844, 8.31296969, 0.04697252, -69.70872693, -0.00051311, -83.12969695, -0.01283844, -8.31296969, -0.04697252, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 66.44778616, 0.00051311, 79.24092965, 0.01283844, 7.92409297, 0.04697252, -66.44778616, -0.00051311, -79.24092965, -0.01283844, -7.92409297, -0.04697252, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 147.51016193, 0.01026216, 147.51016193, 0.03078648, 103.25711335, -2660.15659859, 0.05, 2, 0, 71003, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 36.87754048, 5.156e-05, 110.63262145, 0.00015468, 368.77540482, 0.0005156, -36.87754048, -5.156e-05, -110.63262145, -0.00015468, -368.77540482, -0.0005156, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 147.51016193, 0.01026216, 147.51016193, 0.03078648, 103.25711335, -2660.15659859, 0.05, 2, 0, 71003, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 36.87754048, 5.156e-05, 110.63262145, 0.00015468, 368.77540482, 0.0005156, -36.87754048, -5.156e-05, -110.63262145, -0.00015468, -368.77540482, -0.0005156, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 9.9, 0.0, 5.0)
    ops.node(122003, 9.9, 0.0, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 122003, 0.09, 31191729.16530515, 12996553.81887715, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 67.39865859, 0.00050888, 80.47960066, 0.01178965, 8.04796007, 0.04827953, -67.39865859, -0.00050888, -80.47960066, -0.01178965, -8.04796007, -0.04827953, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 63.82247167, 0.00050888, 76.20933622, 0.01178965, 7.62093362, 0.04827953, -63.82247167, -0.00050888, -76.20933622, -0.01178965, -7.62093362, -0.04827953, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 140.83756547, 0.0101775, 140.83756547, 0.0305325, 98.58629583, -2339.18268679, 0.05, 2, 0, 74021, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 35.20939137, 4.876e-05, 105.6281741, 0.00014629, 352.09391366, 0.00048764, -35.20939137, -4.876e-05, -105.6281741, -0.00014629, -352.09391366, -0.00048764, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 140.83756547, 0.0101775, 140.83756547, 0.0305325, 98.58629583, -2339.18268679, 0.05, 2, 0, 74021, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 35.20939137, 4.876e-05, 105.6281741, 0.00014629, 352.09391366, 0.00048764, -35.20939137, -4.876e-05, -105.6281741, -0.00014629, -352.09391366, -0.00048764, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.9, 0.0, 3.725)
    ops.node(124022, 12.9, 0.0, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 171004, 124022, 0.09, 30328327.43030292, 12636803.09595955, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 69.44499662, 0.00051798, 82.86658927, 0.01273543, 8.28665893, 0.04572895, -69.44499662, -0.00051798, -82.86658927, -0.01273543, -8.28665893, -0.04572895, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 66.25615208, 0.00051798, 79.06143867, 0.01273543, 7.90614387, 0.04572895, -66.25615208, -0.00051798, -79.06143867, -0.01273543, -7.90614387, -0.04572895, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 143.79180819, 0.01035967, 143.79180819, 0.03107902, 100.65426573, -2601.0417564, 0.05, 2, 0, 71004, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 35.94795205, 5.12e-05, 107.84385614, 0.00015361, 359.47952048, 0.00051205, -35.94795205, -5.12e-05, -107.84385614, -0.00015361, -359.47952048, -0.00051205, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 143.79180819, 0.01035967, 143.79180819, 0.03107902, 100.65426573, -2601.0417564, 0.05, 2, 0, 71004, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 35.94795205, 5.12e-05, 107.84385614, 0.00015361, 359.47952048, 0.00051205, -35.94795205, -5.12e-05, -107.84385614, -0.00015361, -359.47952048, -0.00051205, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 12.9, 0.0, 5.0)
    ops.node(122004, 12.9, 0.0, 5.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 122004, 0.09, 29991180.37062142, 12496325.15442559, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 65.09289291, 0.00051822, 77.84509799, 0.01285246, 7.7845098, 0.0470504, -65.09289291, -0.00051822, -77.84509799, -0.01285246, -7.7845098, -0.0470504, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 62.04944924, 0.00051822, 74.20541998, 0.01285246, 7.420542, 0.0470504, -62.04944924, -0.00051822, -74.20541998, -0.01285246, -7.420542, -0.0470504, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 137.34261973, 0.01036444, 137.34261973, 0.03109331, 96.13983381, -2414.68872756, 0.05, 2, 0, 74022, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 34.33565493, 4.946e-05, 103.0069648, 0.00014837, 343.35654932, 0.00049458, -34.33565493, -4.946e-05, -103.0069648, -0.00014837, -343.35654932, -0.00049458, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 137.34261973, 0.01036444, 137.34261973, 0.03109331, 96.13983381, -2414.68872756, 0.05, 2, 0, 74022, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 34.33565493, 4.946e-05, 103.0069648, 0.00014837, 343.35654932, 0.00049458, -34.33565493, -4.946e-05, -103.0069648, -0.00014837, -343.35654932, -0.00049458, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.9, 0.0, 6.425)
    ops.node(124023, 9.9, 0.0, 7.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 172003, 124023, 0.0625, 30639966.19199067, 12766652.57999611, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 38.74079349, 0.00055408, 46.26665582, 0.01378035, 4.62666558, 0.05391515, -38.74079349, -0.00055408, -46.26665582, -0.01378035, -4.62666558, -0.05391515, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 38.74079349, 0.00055408, 46.26665582, 0.01378035, 4.62666558, 0.05391515, -38.74079349, -0.00055408, -46.26665582, -0.01378035, -4.62666558, -0.05391515, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 90.29485971, 0.01108158, 90.29485971, 0.03324474, 63.2064018, -1962.1481867, 0.05, 2, 0, 72003, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 22.57371493, 4.583e-05, 67.72114478, 0.00013749, 225.73714927, 0.00045831, -22.57371493, -4.583e-05, -67.72114478, -0.00013749, -225.73714927, -0.00045831, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 90.29485971, 0.01108158, 90.29485971, 0.03324474, 63.2064018, -1962.1481867, 0.05, 2, 0, 72003, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 22.57371493, 4.583e-05, 67.72114478, 0.00013749, 225.73714927, 0.00045831, -22.57371493, -4.583e-05, -67.72114478, -0.00013749, -225.73714927, -0.00045831, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 9.9, 0.0, 7.7)
    ops.node(123003, 9.9, 0.0, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 123003, 0.0625, 33025542.08895647, 13760642.5370652, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 34.90883058, 0.00054804, 41.60570024, 0.01321154, 4.16057002, 0.06127411, -34.90883058, -0.00054804, -41.60570024, -0.01321154, -4.16057002, -0.06127411, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 34.90883058, 0.00054804, 41.60570024, 0.01321154, 4.16057002, 0.06127411, -34.90883058, -0.00054804, -41.60570024, -0.01321154, -4.16057002, -0.06127411, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 90.32116693, 0.0109608, 90.32116693, 0.03288241, 63.22481685, -1723.02679343, 0.05, 2, 0, 74023, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 22.58029173, 4.253e-05, 67.7408752, 0.0001276, 225.80291732, 0.00042533, -22.58029173, -4.253e-05, -67.7408752, -0.0001276, -225.80291732, -0.00042533, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 90.32116693, 0.0109608, 90.32116693, 0.03288241, 63.22481685, -1723.02679343, 0.05, 2, 0, 74023, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 22.58029173, 4.253e-05, 67.7408752, 0.0001276, 225.80291732, 0.00042533, -22.58029173, -4.253e-05, -67.7408752, -0.0001276, -225.80291732, -0.00042533, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.9, 0.0, 6.425)
    ops.node(124024, 12.9, 0.0, 7.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 172004, 124024, 0.0625, 32380365.31471355, 13491818.88113065, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 39.07902048, 0.00057594, 46.53700414, 0.01299101, 4.65370041, 0.05673242, -39.07902048, -0.00057594, -46.53700414, -0.01299101, -4.65370041, -0.05673242, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 39.07902048, 0.00057594, 46.53700414, 0.01299101, 4.65370041, 0.05673242, -39.07902048, -0.00057594, -46.53700414, -0.01299101, -4.65370041, -0.05673242, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 94.06975215, 0.01151872, 94.06975215, 0.03455615, 65.84882651, -1932.87437062, 0.05, 2, 0, 72004, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 23.51743804, 4.518e-05, 70.55231412, 0.00013554, 235.17438039, 0.00045181, -23.51743804, -4.518e-05, -70.55231412, -0.00013554, -235.17438039, -0.00045181, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 94.06975215, 0.01151872, 94.06975215, 0.03455615, 65.84882651, -1932.87437062, 0.05, 2, 0, 72004, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 23.51743804, 4.518e-05, 70.55231412, 0.00013554, 235.17438039, 0.00045181, -23.51743804, -4.518e-05, -70.55231412, -0.00013554, -235.17438039, -0.00045181, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 12.9, 0.0, 7.7)
    ops.node(123004, 12.9, 0.0, 8.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 123004, 0.0625, 30602999.13451618, 12751249.63938174, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 34.3998852, 0.00054804, 41.20375473, 0.0131516, 4.12037547, 0.05682364, -34.3998852, -0.00054804, -41.20375473, -0.0131516, -4.12037547, -0.05682364, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 34.3998852, 0.00054804, 41.20375473, 0.0131516, 4.12037547, 0.05682364, -34.3998852, -0.00054804, -41.20375473, -0.0131516, -4.12037547, -0.05682364, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 84.05726229, 0.0109608, 84.05726229, 0.0328824, 58.8400836, -1707.51143857, 0.05, 2, 0, 74024, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 21.01431557, 4.272e-05, 63.04294671, 0.00012815, 210.14315571, 0.00042717, -21.01431557, -4.272e-05, -63.04294671, -0.00012815, -210.14315571, -0.00042717, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 84.05726229, 0.0109608, 84.05726229, 0.0328824, 58.8400836, -1707.51143857, 0.05, 2, 0, 74024, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 21.01431557, 4.272e-05, 63.04294671, 0.00012815, 210.14315571, 0.00042717, -21.01431557, -4.272e-05, -63.04294671, -0.00012815, -210.14315571, -0.00042717, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.9, 0.0, 9.125)
    ops.node(124025, 9.9, 0.0, 10.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4061, 173003, 124025, 0.0625, 27276067.01378705, 11365027.92241127, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24061, 22.88136906, 0.00051952, 27.77894361, 0.01704319, 2.77789436, 0.06691062, -22.88136906, -0.00051952, -27.77894361, -0.01704319, -2.77789436, -0.06691062, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14061, 22.88136906, 0.00051952, 27.77894361, 0.01704319, 2.77789436, 0.06691062, -22.88136906, -0.00051952, -27.77894361, -0.01704319, -2.77789436, -0.06691062, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24061, 4061, 0.0, 71.2283421, 0.01039038, 71.2283421, 0.03117114, 49.85983947, -1867.21757876, 0.05, 2, 0, 73003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44061, 17.80708553, 4.061e-05, 53.42125658, 0.00012184, 178.07085525, 0.00040612, -17.80708553, -4.061e-05, -53.42125658, -0.00012184, -178.07085525, -0.00040612, 0.4, 0.3, 0.003, 0.0, 0.0, 24061, 2)
    ops.limitCurve('ThreePoint', 14061, 4061, 0.0, 71.2283421, 0.01039038, 71.2283421, 0.03117114, 49.85983947, -1867.21757876, 0.05, 2, 0, 73003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34061, 17.80708553, 4.061e-05, 53.42125658, 0.00012184, 178.07085525, 0.00040612, -17.80708553, -4.061e-05, -53.42125658, -0.00012184, -178.07085525, -0.00040612, 0.4, 0.3, 0.003, 0.0, 0.0, 14061, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4061, 99999, 'P', 44061, 'Vy', 34061, 'Vz', 24061, 'My', 14061, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4061, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4061, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.9, 0.0, 10.4)
    ops.node(124003, 9.9, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 174025, 124003, 0.0625, 32769380.76241527, 13653908.65100636, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 18.61556888, 0.00047852, 22.38742196, 0.01584276, 2.2387422, 0.07697224, -18.61556888, -0.00047852, -22.38742196, -0.01584276, -2.2387422, -0.07697224, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 18.61556888, 0.00047852, 22.38742196, 0.01584276, 2.2387422, 0.07697224, -18.61556888, -0.00047852, -22.38742196, -0.01584276, -2.2387422, -0.07697224, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 75.77163594, 0.00957032, 75.77163594, 0.02871097, 53.04014516, -1811.35997103, 0.05, 2, 0, 74025, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 18.94290898, 3.596e-05, 56.82872695, 0.00010788, 189.42908984, 0.0003596, -18.94290898, -3.596e-05, -56.82872695, -0.00010788, -189.42908984, -0.0003596, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 75.77163594, 0.00957032, 75.77163594, 0.02871097, 53.04014516, -1811.35997103, 0.05, 2, 0, 74025, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 18.94290898, 3.596e-05, 56.82872695, 0.00010788, 189.42908984, 0.0003596, -18.94290898, -3.596e-05, -56.82872695, -0.00010788, -189.42908984, -0.0003596, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.9, 0.0, 9.125)
    ops.node(124026, 12.9, 0.0, 10.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 173004, 124026, 0.0625, 30044257.62528654, 12518440.67720272, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 22.83811904, 0.00052459, 27.59865259, 0.01683455, 2.75986526, 0.07091577, -22.83811904, -0.00052459, -27.59865259, -0.01683455, -2.75986526, -0.07091577, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 22.83811904, 0.00052459, 27.59865259, 0.01683455, 2.75986526, 0.07091577, -22.83811904, -0.00052459, -27.59865259, -0.01683455, -2.75986526, -0.07091577, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 77.15895468, 0.01049179, 77.15895468, 0.03147537, 54.01126828, -1856.32175455, 0.05, 2, 0, 73004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 19.28973867, 3.994e-05, 57.86921601, 0.00011982, 192.8973867, 0.0003994, -19.28973867, -3.994e-05, -57.86921601, -0.00011982, -192.8973867, -0.0003994, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 77.15895468, 0.01049179, 77.15895468, 0.03147537, 54.01126828, -1856.32175455, 0.05, 2, 0, 73004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 19.28973867, 3.994e-05, 57.86921601, 0.00011982, 192.8973867, 0.0003994, -19.28973867, -3.994e-05, -57.86921601, -0.00011982, -192.8973867, -0.0003994, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.9, 0.0, 10.4)
    ops.node(124004, 12.9, 0.0, 11.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174026, 124004, 0.0625, 31565896.55974474, 13152456.89989364, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 18.82947863, 0.0004798, 22.73017883, 0.01644444, 2.27301788, 0.07684049, -18.82947863, -0.0004798, -22.73017883, -0.01644444, -2.27301788, -0.07684049, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 18.82947863, 0.0004798, 22.73017883, 0.01644444, 2.27301788, 0.07684049, -18.82947863, -0.0004798, -22.73017883, -0.01644444, -2.27301788, -0.07684049, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 71.83900697, 0.00959606, 71.83900697, 0.02878817, 50.28730488, -1695.21921451, 0.05, 2, 0, 74026, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 17.95975174, 3.539e-05, 53.87925522, 0.00010618, 179.59751742, 0.00035394, -17.95975174, -3.539e-05, -53.87925522, -0.00010618, -179.59751742, -0.00035394, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 71.83900697, 0.00959606, 71.83900697, 0.02878817, 50.28730488, -1695.21921451, 0.05, 2, 0, 74026, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 17.95975174, 3.539e-05, 53.87925522, 0.00010618, 179.59751742, 0.00035394, -17.95975174, -3.539e-05, -53.87925522, -0.00010618, -179.59751742, -0.00035394, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4064, '-orient', 0, 0, 1, 0, 1, 0)
