import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.1225, 26205772.19626042, 10919071.74844184, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 111.36430461, 0.00072991, 133.35630653, 0.01627345, 13.33563065, 0.04006841, -111.36430461, -0.00072991, -133.35630653, -0.01627345, -13.33563065, -0.04006841, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 115.3897947, 0.00072991, 138.17674242, 0.01627345, 13.81767424, 0.04006841, -115.3897947, -0.00072991, -138.17674242, -0.01627345, -13.81767424, -0.04006841, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 124.70267055, 0.01459812, 124.70267055, 0.04379437, 87.29186938, -1366.51996099, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 31.17566764, 8.67e-05, 93.52700291, 0.00026011, 311.75667637, 0.00086704, -31.17566764, -8.67e-05, -93.52700291, -0.00026011, -311.75667637, -0.00086704, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 124.70267055, 0.01459812, 124.70267055, 0.04379437, 87.29186938, -1366.51996099, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 31.17566764, 8.67e-05, 93.52700291, 0.00026011, 311.75667637, 0.00086704, -31.17566764, -8.67e-05, -93.52700291, -0.00026011, -311.75667637, -0.00086704, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.5, 0.0, 0.0)
    ops.node(121002, 4.5, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.2025, 28042426.02505859, 11684344.17710775, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 262.6700671, 0.00062831, 314.84485695, 0.01835186, 31.48448569, 0.03899325, -262.6700671, -0.00062831, -314.84485695, -0.01835186, -31.48448569, -0.03899325, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 294.17195829, 0.00062831, 352.60404487, 0.01835186, 35.26040449, 0.03899325, -294.17195829, -0.00062831, -352.60404487, -0.01835186, -35.26040449, -0.03899325, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 194.89230466, 0.01256628, 194.89230466, 0.03769883, 136.42461326, -1808.08563471, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 48.72307617, 7.66e-05, 146.1692285, 0.00022981, 487.23076166, 0.00076603, -48.72307617, -7.66e-05, -146.1692285, -0.00022981, -487.23076166, -0.00076603, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 194.89230466, 0.01256628, 194.89230466, 0.03769883, 136.42461326, -1808.08563471, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 48.72307617, 7.66e-05, 146.1692285, 0.00022981, 487.23076166, 0.00076603, -48.72307617, -7.66e-05, -146.1692285, -0.00022981, -487.23076166, -0.00076603, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.5, 0.0, 0.0)
    ops.node(121005, 16.5, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.2025, 26472866.54226427, 11030361.05927678, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 260.47146533, 0.00064282, 311.99107173, 0.01748615, 31.19910717, 0.03559055, -260.47146533, -0.00064282, -311.99107173, -0.01748615, -31.19910717, -0.03559055, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 291.79162598, 0.00064282, 349.50616181, 0.01748615, 34.95061618, 0.03559055, -291.79162598, -0.00064282, -349.50616181, -0.01748615, -34.95061618, -0.03559055, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 185.0474396, 0.01285635, 185.0474396, 0.03856904, 129.53320772, -1810.04883393, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 46.2618599, 7.705e-05, 138.7855797, 0.00023114, 462.618599, 0.00077046, -46.2618599, -7.705e-05, -138.7855797, -0.00023114, -462.618599, -0.00077046, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 185.0474396, 0.01285635, 185.0474396, 0.03856904, 129.53320772, -1810.04883393, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 46.2618599, 7.705e-05, 138.7855797, 0.00023114, 462.618599, 0.00077046, -46.2618599, -7.705e-05, -138.7855797, -0.00023114, -462.618599, -0.00077046, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 21.0, 0.0, 0.0)
    ops.node(121006, 21.0, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.1225, 26165474.20814762, 10902280.92006151, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 111.53819319, 0.00070922, 133.55820215, 0.01614161, 13.35582021, 0.03984181, -111.53819319, -0.00070922, -133.55820215, -0.01614161, -13.35582021, -0.03984181, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 115.78340858, 0.00070922, 138.64151325, 0.01614161, 13.86415132, 0.03984181, -115.78340858, -0.00070922, -138.64151325, -0.01614161, -13.86415132, -0.03984181, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 124.42100682, 0.01418437, 124.42100682, 0.04255311, 87.09470478, -1363.82183948, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 31.10525171, 8.664e-05, 93.31575512, 0.00025992, 311.05251706, 0.00086641, -31.10525171, -8.664e-05, -93.31575512, -0.00025992, -311.05251706, -0.00086641, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 124.42100682, 0.01418437, 124.42100682, 0.04255311, 87.09470478, -1363.82183948, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 31.10525171, 8.664e-05, 93.31575512, 0.00025992, 311.05251706, 0.00086641, -31.10525171, -8.664e-05, -93.31575512, -0.00025992, -311.05251706, -0.00086641, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.5, 0.0)
    ops.node(121007, 0.0, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.2025, 26059655.72111316, 10858189.88379715, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 290.1278297, 0.00064274, 347.3224976, 0.01746578, 34.73224976, 0.03480842, -290.1278297, -0.00064274, -347.3224976, -0.01746578, -34.73224976, -0.03480842, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 290.1278297, 0.00064274, 347.3224976, 0.01746578, 34.73224976, 0.03480842, -290.1278297, -0.00064274, -347.3224976, -0.01746578, -34.73224976, -0.03480842, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 182.22126236, 0.01285473, 182.22126236, 0.03856419, 127.55488365, -1806.20544502, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 45.55531559, 7.707e-05, 136.66594677, 0.00023122, 455.55315589, 0.00077073, -45.55531559, -7.707e-05, -136.66594677, -0.00023122, -455.55315589, -0.00077073, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 182.22126236, 0.01285473, 182.22126236, 0.03856419, 127.55488365, -1806.20544502, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 45.55531559, 7.707e-05, 136.66594677, 0.00023122, 455.55315589, 0.00077073, -45.55531559, -7.707e-05, -136.66594677, -0.00023122, -455.55315589, -0.00077073, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.5, 4.5, 0.0)
    ops.node(121008, 4.5, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.3025, 26835964.15260701, 11181651.73025292, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 576.01790272, 0.00060315, 691.33213427, 0.03150951, 69.13321343, 0.06614956, -576.01790272, -0.00060315, -691.33213427, -0.03150951, -69.13321343, -0.06614956, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 608.93512988, 0.00060315, 730.83913014, 0.03150951, 73.08391301, 0.06614956, -608.93512988, -0.00060315, -730.83913014, -0.03150951, -73.08391301, -0.06614956, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 370.78113683, 0.01206296, 370.78113683, 0.03618888, 259.54679578, -3996.8879989, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 92.69528421, 0.00010195, 278.08585262, 0.00030584, 926.95284208, 0.00101946, -92.69528421, -0.00010195, -278.08585262, -0.00030584, -926.95284208, -0.00101946, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 370.78113683, 0.01206296, 370.78113683, 0.03618888, 259.54679578, -3996.8879989, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 92.69528421, 0.00010195, 278.08585262, 0.00030584, 926.95284208, 0.00101946, -92.69528421, -0.00010195, -278.08585262, -0.00030584, -926.95284208, -0.00101946, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.0, 4.5, 0.0)
    ops.node(121009, 9.0, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.3025, 27308667.9774602, 11378611.65727508, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 589.94785472, 0.00058643, 709.88033951, 0.03311568, 70.98803395, 0.07176818, -589.94785472, -0.00058643, -709.88033951, -0.03311568, -70.98803395, -0.07176818, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 610.79268514, 0.00058643, 734.96278566, 0.03311568, 73.49627857, 0.07176818, -610.79268514, -0.00058643, -734.96278566, -0.03311568, -73.49627857, -0.07176818, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 366.55516997, 0.01172856, 366.55516997, 0.03518567, 256.58861898, -3874.96344252, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 91.63879249, 9.904e-05, 274.91637748, 0.00029712, 916.38792492, 0.00099039, -91.63879249, -9.904e-05, -274.91637748, -0.00029712, -916.38792492, -0.00099039, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 366.55516997, 0.01172856, 366.55516997, 0.03518567, 256.58861898, -3874.96344252, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 91.63879249, 9.904e-05, 274.91637748, 0.00029712, 916.38792492, 0.00099039, -91.63879249, -9.904e-05, -274.91637748, -0.00029712, -916.38792492, -0.00099039, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.0, 4.5, 0.0)
    ops.node(121010, 12.0, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.3025, 26965580.46831044, 11235658.52846268, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 587.54271717, 0.00059116, 706.98292436, 0.03320072, 70.69829244, 0.07093707, -587.54271717, -0.00059116, -706.98292436, -0.03320072, -70.69829244, -0.07093707, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 608.19115398, 0.00059116, 731.82893438, 0.03320072, 73.18289344, 0.07093707, -608.19115398, -0.00059116, -731.82893438, -0.03320072, -73.18289344, -0.07093707, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 365.77748387, 0.01182316, 365.77748387, 0.03546948, 256.04423871, -3944.25893019, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 91.44437097, 0.00010009, 274.3331129, 0.00030026, 914.44370968, 0.00100087, -91.44437097, -0.00010009, -274.3331129, -0.00030026, -914.44370968, -0.00100087, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 365.77748387, 0.01182316, 365.77748387, 0.03546948, 256.04423871, -3944.25893019, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 91.44437097, 0.00010009, 274.3331129, 0.00030026, 914.44370968, 0.00100087, -91.44437097, -0.00010009, -274.3331129, -0.00030026, -914.44370968, -0.00100087, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 16.5, 4.5, 0.0)
    ops.node(121011, 16.5, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.3025, 26108754.02658393, 10878647.51107664, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 571.86598753, 0.00059956, 685.97510237, 0.03072321, 68.59751024, 0.06321725, -571.86598753, -0.00059956, -685.97510237, -0.03072321, -68.59751024, -0.06321725, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 605.09313247, 0.00059956, 725.83233229, 0.03072321, 72.58323323, 0.06321725, -605.09313247, -0.00059956, -725.83233229, -0.03072321, -72.58323323, -0.06321725, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 361.67492643, 0.01199112, 361.67492643, 0.03597337, 253.1724485, -3962.54697727, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 90.41873161, 0.00010221, 271.25619482, 0.00030664, 904.18731606, 0.00102212, -90.41873161, -0.00010221, -271.25619482, -0.00030664, -904.18731606, -0.00102212, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 361.67492643, 0.01199112, 361.67492643, 0.03597337, 253.1724485, -3962.54697727, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 90.41873161, 0.00010221, 271.25619482, 0.00030664, 904.18731606, 0.00102212, -90.41873161, -0.00010221, -271.25619482, -0.00030664, -904.18731606, -0.00102212, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 21.0, 4.5, 0.0)
    ops.node(121012, 21.0, 4.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.2025, 28258902.30848132, 11774542.62853388, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 295.28184139, 0.00064484, 353.90267483, 0.01887292, 35.39026748, 0.03979945, -295.28184139, -0.00064484, -353.90267483, -0.01887292, -35.39026748, -0.03979945, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 295.28184139, 0.00064484, 353.90267483, 0.01887292, 35.39026748, 0.03979945, -295.28184139, -0.00064484, -353.90267483, -0.01887292, -35.39026748, -0.03979945, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 197.70917907, 0.01289674, 197.70917907, 0.03869021, 138.39642535, -1835.29763598, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 49.42729477, 7.712e-05, 148.2818843, 0.00023135, 494.27294767, 0.00077115, -49.42729477, -7.712e-05, -148.2818843, -0.00023135, -494.27294767, -0.00077115, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 197.70917907, 0.01289674, 197.70917907, 0.03869021, 138.39642535, -1835.29763598, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 49.42729477, 7.712e-05, 148.2818843, 0.00023135, 494.27294767, 0.00077115, -49.42729477, -7.712e-05, -148.2818843, -0.00023135, -494.27294767, -0.00077115, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.2025, 26941623.67242133, 11225676.53017555, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 292.37306405, 0.00063573, 350.32881034, 0.01813512, 35.03288103, 0.03701859, -292.37306405, -0.00063573, -350.32881034, -0.01813512, -35.03288103, -0.03701859, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 292.37306405, 0.00063573, 350.32881034, 0.01813512, 35.03288103, 0.03701859, -292.37306405, -0.00063573, -350.32881034, -0.01813512, -35.03288103, -0.03701859, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 187.58585803, 0.01271463, 187.58585803, 0.03814389, 131.31010062, -1802.60833451, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 46.89646451, 7.674e-05, 140.68939352, 0.00023023, 468.96464506, 0.00076744, -46.89646451, -7.674e-05, -140.68939352, -0.00023023, -468.96464506, -0.00076744, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 187.58585803, 0.01271463, 187.58585803, 0.03814389, 131.31010062, -1802.60833451, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 46.89646451, 7.674e-05, 140.68939352, 0.00023023, 468.96464506, 0.00076744, -46.89646451, -7.674e-05, -140.68939352, -0.00023023, -468.96464506, -0.00076744, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.5, 9.0, 0.0)
    ops.node(121014, 4.5, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.3025, 27629569.84973869, 11512320.77072446, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 606.3763351, 0.00058503, 727.9634815, 0.03249808, 72.79634815, 0.06941369, -606.3763351, -0.00058503, -727.9634815, -0.03249808, -72.79634815, -0.06941369, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 627.23498414, 0.00058503, 753.00458865, 0.03249808, 75.30045886, 0.06941369, -627.23498414, -0.00058503, -753.00458865, -0.03249808, -75.30045886, -0.06941369, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 381.16725631, 0.01170067, 381.16725631, 0.03510201, 266.81707942, -4045.14825573, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 95.29181408, 0.00010179, 285.87544224, 0.00030537, 952.91814078, 0.00101791, -95.29181408, -0.00010179, -285.87544224, -0.00030537, -952.91814078, -0.00101791, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 381.16725631, 0.01170067, 381.16725631, 0.03510201, 266.81707942, -4045.14825573, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 95.29181408, 0.00010179, 285.87544224, 0.00030537, 952.91814078, 0.00101791, -95.29181408, -0.00010179, -285.87544224, -0.00030537, -952.91814078, -0.00101791, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 9.0, 0.0)
    ops.node(121015, 9.0, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.3025, 26975146.87914767, 11239644.5329782, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 584.57131686, 0.00059114, 703.41285167, 0.03312634, 70.34128517, 0.07089604, -584.57131686, -0.00059114, -703.41285167, -0.03312634, -70.34128517, -0.07089604, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 604.9853917, 0.00059114, 727.97704458, 0.03312634, 72.79770446, 0.07089604, -604.9853917, -0.00059114, -727.97704458, -0.03312634, -72.79770446, -0.07089604, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 367.45685439, 0.01182286, 367.45685439, 0.03546857, 257.21979807, -3983.85501652, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 91.8642136, 0.00010051, 275.59264079, 0.00030153, 918.64213597, 0.0010051, -91.8642136, -0.00010051, -275.59264079, -0.00030153, -918.64213597, -0.0010051, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 367.45685439, 0.01182286, 367.45685439, 0.03546857, 257.21979807, -3983.85501652, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 91.8642136, 0.00010051, 275.59264079, 0.00030153, 918.64213597, 0.0010051, -91.8642136, -0.00010051, -275.59264079, -0.00030153, -918.64213597, -0.0010051, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.0, 9.0, 0.0)
    ops.node(121016, 12.0, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.3025, 26930419.02995164, 11221007.92914652, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 582.16160004, 0.00058535, 700.50949664, 0.03296384, 70.05094966, 0.07061213, -582.16160004, -0.00058535, -700.50949664, -0.03296384, -70.05094966, -0.07061213, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 602.62897181, 0.00058535, 725.13768973, 0.03296384, 72.51376897, 0.07061213, -602.62897181, -0.00058535, -725.13768973, -0.03296384, -72.51376897, -0.07061213, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 363.95175178, 0.01170708, 363.95175178, 0.03512123, 254.76622624, -3908.46389488, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 90.98793794, 9.972e-05, 272.96381383, 0.00029915, 909.87937945, 0.00099717, -90.98793794, -9.972e-05, -272.96381383, -0.00029915, -909.87937945, -0.00099717, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 363.95175178, 0.01170708, 363.95175178, 0.03512123, 254.76622624, -3908.46389488, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 90.98793794, 9.972e-05, 272.96381383, 0.00029915, 909.87937945, 0.00099717, -90.98793794, -9.972e-05, -272.96381383, -0.00029915, -909.87937945, -0.00099717, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 16.5, 9.0, 0.0)
    ops.node(121017, 16.5, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.3025, 25843266.05910226, 10768027.52462594, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 618.25912241, 0.00060258, 741.46852476, 0.03078556, 74.14685248, 0.06254167, -618.25912241, -0.00060258, -741.46852476, -0.03078556, -74.14685248, -0.06254167, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 640.33900426, 0.00060258, 767.94858276, 0.03078556, 76.79485828, 0.06254167, -640.33900426, -0.00060258, -767.94858276, -0.03078556, -76.79485828, -0.06254167, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 361.83897549, 0.01205152, 361.83897549, 0.03615456, 253.28728284, -4033.61423826, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 90.45974387, 0.00010331, 271.37923162, 0.00030993, 904.59743872, 0.00103309, -90.45974387, -0.00010331, -271.37923162, -0.00030993, -904.59743872, -0.00103309, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 361.83897549, 0.01205152, 361.83897549, 0.03615456, 253.28728284, -4033.61423826, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 90.45974387, 0.00010331, 271.37923162, 0.00030993, 904.59743872, 0.00103309, -90.45974387, -0.00010331, -271.37923162, -0.00030993, -904.59743872, -0.00103309, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.2025, 26417473.66669993, 11007280.6944583, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 288.57796937, 0.00066369, 345.63134019, 0.01788042, 34.56313402, 0.03587964, -288.57796937, -0.00066369, -345.63134019, -0.01788042, -34.56313402, -0.03587964, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 288.57796937, 0.00066369, 345.63134019, 0.01788042, 34.56313402, 0.03587964, -288.57796937, -0.00066369, -345.63134019, -0.01788042, -34.56313402, -0.03587964, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 185.57200061, 0.0132737, 185.57200061, 0.0398211, 129.90040043, -1826.4760232, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 46.39300015, 7.743e-05, 139.17900046, 0.00023228, 463.93000153, 0.00077427, -46.39300015, -7.743e-05, -139.17900046, -0.00023228, -463.93000153, -0.00077427, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 185.57200061, 0.0132737, 185.57200061, 0.0398211, 129.90040043, -1826.4760232, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 46.39300015, 7.743e-05, 139.17900046, 0.00023228, 463.93000153, 0.00077427, -46.39300015, -7.743e-05, -139.17900046, -0.00023228, -463.93000153, -0.00077427, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.1225, 26570602.29628523, 11071084.29011885, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 121.6092127, 0.00071952, 145.67903764, 0.01629959, 14.56790376, 0.0409408, -121.6092127, -0.00071952, -145.67903764, -0.01629959, -14.56790376, -0.0409408, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 121.6092127, 0.00071952, 145.67903764, 0.01629959, 14.56790376, 0.0409408, -121.6092127, -0.00071952, -145.67903764, -0.01629959, -14.56790376, -0.0409408, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 124.12148499, 0.01439048, 124.12148499, 0.04317143, 86.88503949, -1325.98404692, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 31.03037125, 8.511e-05, 93.09111374, 0.00025534, 310.30371247, 0.00085115, -31.03037125, -8.511e-05, -93.09111374, -0.00025534, -310.30371247, -0.00085115, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 124.12148499, 0.01439048, 124.12148499, 0.04317143, 86.88503949, -1325.98404692, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 31.03037125, 8.511e-05, 93.09111374, 0.00025534, 310.30371247, 0.00085115, -31.03037125, -8.511e-05, -93.09111374, -0.00025534, -310.30371247, -0.00085115, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 4.5, 13.5, 0.0)
    ops.node(121020, 4.5, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.25, 27287013.83597505, 11369589.09832294, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 393.01933259, 0.00060495, 472.9358804, 0.02599464, 47.29358804, 0.05287413, -393.01933259, -0.00060495, -472.9358804, -0.02599464, -47.29358804, -0.05287413, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 416.77154314, 0.00060495, 501.51786524, 0.02599464, 50.15178652, 0.05287413, -416.77154314, -0.00060495, -501.51786524, -0.02599464, -50.15178652, -0.05287413, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 246.68778101, 0.01209893, 246.68778101, 0.03629678, 172.68144671, -2342.15284229, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 61.67194525, 8.071e-05, 185.01583576, 0.00024214, 616.71945253, 0.00080713, -61.67194525, -8.071e-05, -185.01583576, -0.00024214, -616.71945253, -0.00080713, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 246.68778101, 0.01209893, 246.68778101, 0.03629678, 172.68144671, -2342.15284229, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 61.67194525, 8.071e-05, 185.01583576, 0.00024214, 616.71945253, 0.00080713, -61.67194525, -8.071e-05, -185.01583576, -0.00024214, -616.71945253, -0.00080713, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 9.0, 13.5, 0.0)
    ops.node(121021, 9.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.2025, 27893067.31273017, 11622111.38030424, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 288.99287435, 0.00063772, 347.29328142, 0.01938504, 34.72932814, 0.04143379, -288.99287435, -0.00063772, -347.29328142, -0.01938504, -34.72932814, -0.04143379, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 299.2812198, 0.00063772, 359.65716152, 0.01938504, 35.96571615, 0.04143379, -299.2812198, -0.00063772, -359.65716152, -0.01938504, -35.96571615, -0.04143379, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 186.91263054, 0.01275442, 186.91263054, 0.03826326, 130.83884138, -1656.88620523, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 46.72815763, 7.386e-05, 140.1844729, 0.00022158, 467.28157634, 0.0007386, -46.72815763, -7.386e-05, -140.1844729, -0.00022158, -467.28157634, -0.0007386, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 186.91263054, 0.01275442, 186.91263054, 0.03826326, 130.83884138, -1656.88620523, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 46.72815763, 7.386e-05, 140.1844729, 0.00022158, 467.28157634, 0.0007386, -46.72815763, -7.386e-05, -140.1844729, -0.00022158, -467.28157634, -0.0007386, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 12.0, 13.5, 0.0)
    ops.node(121022, 12.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.2025, 26854750.92851087, 11189479.5535462, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 292.21129425, 0.0006392, 351.14962383, 0.01911419, 35.11496238, 0.03957744, -292.21129425, -0.0006392, -351.14962383, -0.01911419, -35.11496238, -0.03957744, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 303.06209618, 0.0006392, 364.18900695, 0.01911419, 36.41890069, 0.03957744, -303.06209618, -0.0006392, -364.18900695, -0.01911419, -36.41890069, -0.03957744, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 181.741209, 0.01278405, 181.741209, 0.03835214, 127.2188463, -1681.76392774, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 45.43530225, 7.459e-05, 136.30590675, 0.00022378, 454.35302249, 0.00074594, -45.43530225, -7.459e-05, -136.30590675, -0.00022378, -454.35302249, -0.00074594, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 181.741209, 0.01278405, 181.741209, 0.03835214, 127.2188463, -1681.76392774, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 45.43530225, 7.459e-05, 136.30590675, 0.00022378, 454.35302249, 0.00074594, -45.43530225, -7.459e-05, -136.30590675, -0.00022378, -454.35302249, -0.00074594, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 16.5, 13.5, 0.0)
    ops.node(121023, 16.5, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.25, 26926101.26402185, 11219208.86000911, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 388.54950282, 0.00059298, 467.55264885, 0.02594774, 46.75526488, 0.0521555, -388.54950282, -0.00059298, -467.55264885, -0.02594774, -46.75526488, -0.0521555, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 412.43423815, 0.00059298, 496.29382903, 0.02594774, 49.6293829, 0.0521555, -412.43423815, -0.00059298, -496.29382903, -0.02594774, -49.6293829, -0.0521555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 244.64510138, 0.01185952, 244.64510138, 0.03557855, 171.25157097, -2358.7677103, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 61.16127535, 8.112e-05, 183.48382604, 0.00024335, 611.61275346, 0.00081118, -61.16127535, -8.112e-05, -183.48382604, -0.00024335, -611.61275346, -0.00081118, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 244.64510138, 0.01185952, 244.64510138, 0.03557855, 171.25157097, -2358.7677103, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 61.16127535, 8.112e-05, 183.48382604, 0.00024335, 611.61275346, 0.00081118, -61.16127535, -8.112e-05, -183.48382604, -0.00024335, -611.61275346, -0.00081118, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.1225, 25940069.81257878, 10808362.42190783, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 120.41430939, 0.00072519, 144.14518643, 0.01643148, 14.41451864, 0.03959698, -120.41430939, -0.00072519, -144.14518643, -0.01643148, -14.41451864, -0.03959698, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 120.41430939, 0.00072519, 144.14518643, 0.01643148, 14.41451864, 0.03959698, -120.41430939, -0.00072519, -144.14518643, -0.01643148, -14.41451864, -0.03959698, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 123.6056109, 0.01450371, 123.6056109, 0.04351113, 86.52392763, -1364.51068727, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 30.90140273, 8.682e-05, 92.70420818, 0.00026046, 309.01402725, 0.00086821, -30.90140273, -8.682e-05, -92.70420818, -0.00026046, -309.01402725, -0.00086821, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 123.6056109, 0.01450371, 123.6056109, 0.04351113, 86.52392763, -1364.51068727, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 30.90140273, 8.682e-05, 92.70420818, 0.00026046, 309.01402725, 0.00086821, -30.90140273, -8.682e-05, -92.70420818, -0.00026046, -309.01402725, -0.00086821, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.375)
    ops.node(122001, 0.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.1225, 27233604.07736643, 11347335.03223602, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 76.38555172, 0.00063847, 92.12175006, 0.0176531, 9.21217501, 0.04915443, -76.38555172, -0.00063847, -92.12175006, -0.0176531, -9.21217501, -0.04915443, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 84.37234158, 0.00063847, 101.75389962, 0.0176531, 10.17538996, 0.04915443, -84.37234158, -0.00063847, -101.75389962, -0.0176531, -10.17538996, -0.04915443, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 119.83580083, 0.01276937, 119.83580083, 0.03830812, 83.88506058, -1333.17582266, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 29.95895021, 7.242e-05, 89.87685062, 0.00021725, 299.58950208, 0.00072416, -29.95895021, -7.242e-05, -89.87685062, -0.00021725, -299.58950208, -0.00072416, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 119.83580083, 0.01276937, 119.83580083, 0.03830812, 83.88506058, -1333.17582266, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 29.95895021, 7.242e-05, 89.87685062, 0.00021725, 299.58950208, 0.00072416, -29.95895021, -7.242e-05, -89.87685062, -0.00021725, -299.58950208, -0.00072416, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.5, 0.0, 3.425)
    ops.node(122002, 4.5, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.2025, 27891106.0640154, 11621294.19333975, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 178.25274569, 0.00058574, 214.87601732, 0.01448506, 21.48760173, 0.03480461, -178.25274569, -0.00058574, -214.87601732, -0.01448506, -21.48760173, -0.03480461, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 187.1985666, 0.00058574, 225.65981962, 0.01448506, 22.56598196, 0.03480461, -187.1985666, -0.00058574, -225.65981962, -0.01448506, -22.56598196, -0.03480461, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 174.642869, 0.01171476, 174.642869, 0.03514428, 122.2500083, -1476.05435151, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 43.66071725, 6.234e-05, 130.98215175, 0.00018701, 436.6071725, 0.00062338, -43.66071725, -6.234e-05, -130.98215175, -0.00018701, -436.6071725, -0.00062338, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 174.642869, 0.01171476, 174.642869, 0.03514428, 122.2500083, -1476.05435151, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 43.66071725, 6.234e-05, 130.98215175, 0.00018701, 436.6071725, 0.00062338, -43.66071725, -6.234e-05, -130.98215175, -0.00018701, -436.6071725, -0.00062338, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.5, 0.0, 3.425)
    ops.node(122005, 16.5, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.2025, 26347241.14219429, 10978017.14258096, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 180.60812257, 0.000588, 217.79346891, 0.01430032, 21.77934689, 0.03275083, -180.60812257, -0.000588, -217.79346891, -0.01430032, -21.77934689, -0.03275083, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 190.4754626, 0.000588, 229.69239229, 0.01430032, 22.96923923, 0.03275083, -190.4754626, -0.000588, -229.69239229, -0.01430032, -22.96923923, -0.03275083, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 165.53187036, 0.01176006, 165.53187036, 0.03528017, 115.87230925, -1487.06966482, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 41.38296759, 6.255e-05, 124.14890277, 0.00018764, 413.8296759, 0.00062548, -41.38296759, -6.255e-05, -124.14890277, -0.00018764, -413.8296759, -0.00062548, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 165.53187036, 0.01176006, 165.53187036, 0.03528017, 115.87230925, -1487.06966482, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 41.38296759, 6.255e-05, 124.14890277, 0.00018764, 413.8296759, 0.00062548, -41.38296759, -6.255e-05, -124.14890277, -0.00018764, -413.8296759, -0.00062548, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 21.0, 0.0, 3.375)
    ops.node(122006, 21.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.1225, 24854749.48823403, 10356145.62009751, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 75.33065916, 0.00065426, 90.77018856, 0.01615835, 9.07701886, 0.04256447, -75.33065916, -0.00065426, -90.77018856, -0.01615835, -9.07701886, -0.04256447, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 83.24823519, 0.00065426, 100.31052549, 0.01615835, 10.03105255, 0.04256447, -83.24823519, -0.00065426, -100.31052549, -0.01615835, -10.03105255, -0.04256447, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 110.32560686, 0.01308511, 110.32560686, 0.03925532, 77.2279248, -1309.23483257, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 27.58140172, 7.305e-05, 82.74420515, 0.00021915, 275.81401715, 0.0007305, -27.58140172, -7.305e-05, -82.74420515, -0.00021915, -275.81401715, -0.0007305, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 110.32560686, 0.01308511, 110.32560686, 0.03925532, 77.2279248, -1309.23483257, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 27.58140172, 7.305e-05, 82.74420515, 0.00021915, 275.81401715, 0.0007305, -27.58140172, -7.305e-05, -82.74420515, -0.00021915, -275.81401715, -0.0007305, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.425)
    ops.node(122007, 0.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.2025, 26337233.32473681, 10973847.21864034, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 187.86824561, 0.00059033, 226.52909515, 0.01449302, 22.65290951, 0.03288484, -187.86824561, -0.00059033, -226.52909515, -0.01449302, -22.65290951, -0.03288484, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 178.54235825, 0.00059033, 215.28406107, 0.01449302, 21.52840611, 0.03288484, -178.54235825, -0.00059033, -215.28406107, -0.01449302, -21.52840611, -0.03288484, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 165.94242386, 0.01180657, 165.94242386, 0.03541971, 116.1596967, -1497.20029303, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 41.48560597, 6.273e-05, 124.4568179, 0.00018818, 414.85605966, 0.00062727, -41.48560597, -6.273e-05, -124.4568179, -0.00018818, -414.85605966, -0.00062727, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 165.94242386, 0.01180657, 165.94242386, 0.03541971, 116.1596967, -1497.20029303, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 41.48560597, 6.273e-05, 124.4568179, 0.00018818, 414.85605966, 0.00062727, -41.48560597, -6.273e-05, -124.4568179, -0.00018818, -414.85605966, -0.00062727, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.5, 4.5, 3.425)
    ops.node(122008, 4.5, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.3025, 27355811.43813358, 11398254.76588899, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 368.722086, 0.00054291, 444.96234614, 0.01570846, 44.49623461, 0.0377775, -368.722086, -0.00054291, -444.96234614, -0.01570846, -44.49623461, -0.0377775, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 339.04350919, 0.00054291, 409.14716264, 0.01570846, 40.91471626, 0.0377775, -339.04350919, -0.00054291, -409.14716264, -0.01570846, -40.91471626, -0.0377775, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 306.71428079, 0.01085814, 306.71428079, 0.03257442, 214.69999655, -2287.1682371, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 76.6785702, 7.472e-05, 230.03571059, 0.00022417, 766.78570198, 0.00074722, -76.6785702, -7.472e-05, -230.03571059, -0.00022417, -766.78570198, -0.00074722, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 306.71428079, 0.01085814, 306.71428079, 0.03257442, 214.69999655, -2287.1682371, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 76.6785702, 7.472e-05, 230.03571059, 0.00022417, 766.78570198, 0.00074722, -76.6785702, -7.472e-05, -230.03571059, -0.00022417, -766.78570198, -0.00074722, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.0, 4.5, 3.425)
    ops.node(122009, 9.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.3025, 26854801.90912285, 11189500.79546786, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 323.53038603, 0.0005378, 391.26968974, 0.01592177, 39.12696897, 0.03865349, -323.53038603, -0.0005378, -391.26968974, -0.01592177, -39.12696897, -0.03865349, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 305.47009943, 0.0005378, 369.42802342, 0.01592177, 36.94280234, 0.03865349, -305.47009943, -0.0005378, -369.42802342, -0.01592177, -36.94280234, -0.03865349, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 293.87551206, 0.0107559, 293.87551206, 0.03226771, 205.71285844, -2173.03695149, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 73.46887801, 7.293e-05, 220.40663404, 0.00021879, 734.68878015, 0.0007293, -73.46887801, -7.293e-05, -220.40663404, -0.00021879, -734.68878015, -0.0007293, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 293.87551206, 0.0107559, 293.87551206, 0.03226771, 205.71285844, -2173.03695149, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 73.46887801, 7.293e-05, 220.40663404, 0.00021879, 734.68878015, 0.0007293, -73.46887801, -7.293e-05, -220.40663404, -0.00021879, -734.68878015, -0.0007293, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.0, 4.5, 3.425)
    ops.node(122010, 12.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.3025, 28040559.15407874, 11683566.31419948, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 328.69988453, 0.00053496, 397.17694521, 0.01557505, 39.71769452, 0.03968356, -328.69988453, -0.00053496, -397.17694521, -0.01557505, -39.71769452, -0.03968356, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 310.1929559, 0.00053496, 374.81452367, 0.01557505, 37.48145237, 0.03968356, -310.1929559, -0.00053496, -374.81452367, -0.01557505, -37.48145237, -0.03968356, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 305.75078079, 0.01069923, 305.75078079, 0.03209768, 214.02554655, -2139.81662545, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 76.4376952, 7.267e-05, 229.31308559, 0.00021801, 764.37695196, 0.00072668, -76.4376952, -7.267e-05, -229.31308559, -0.00021801, -764.37695196, -0.00072668, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 305.75078079, 0.01069923, 305.75078079, 0.03209768, 214.02554655, -2139.81662545, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 76.4376952, 7.267e-05, 229.31308559, 0.00021801, 764.37695196, 0.00072668, -76.4376952, -7.267e-05, -229.31308559, -0.00021801, -764.37695196, -0.00072668, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 16.5, 4.5, 3.425)
    ops.node(122011, 16.5, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.3025, 26102572.60291864, 10876071.91788276, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 369.53681122, 0.00055164, 446.01923943, 0.01549155, 44.60192394, 0.03588053, -369.53681122, -0.00055164, -446.01923943, -0.01549155, -44.60192394, -0.03588053, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 339.30082116, 0.00055164, 409.52535607, 0.01549155, 40.95253561, 0.03588053, -339.30082116, -0.00055164, -409.52535607, -0.01549155, -40.95253561, -0.03588053, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 293.18046446, 0.0110329, 293.18046446, 0.0330987, 205.22632512, -2299.67670487, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 73.29511612, 7.485e-05, 219.88534835, 0.00022456, 732.95116116, 0.00074854, -73.29511612, -7.485e-05, -219.88534835, -0.00022456, -732.95116116, -0.00074854, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 293.18046446, 0.0110329, 293.18046446, 0.0330987, 205.22632512, -2299.67670487, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 73.29511612, 7.485e-05, 219.88534835, 0.00022456, 732.95116116, 0.00074854, -73.29511612, -7.485e-05, -219.88534835, -0.00022456, -732.95116116, -0.00074854, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.425)
    ops.node(122012, 21.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.2025, 28112536.06001035, 11713556.69167098, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 190.63070694, 0.00057958, 229.74666655, 0.0145429, 22.97466665, 0.03506696, -190.63070694, -0.00057958, -229.74666655, -0.0145429, -22.97466665, -0.03506696, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 181.08840508, 0.00057958, 218.2463575, 0.0145429, 21.82463575, 0.03506696, -181.08840508, -0.00057958, -218.2463575, -0.0145429, -21.82463575, -0.03506696, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 176.38906383, 0.01159151, 176.38906383, 0.03477454, 123.47234468, -1483.35367347, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 44.09726596, 6.247e-05, 132.29179787, 0.0001874, 440.97265958, 0.00062465, -44.09726596, -6.247e-05, -132.29179787, -0.0001874, -440.97265958, -0.00062465, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 176.38906383, 0.01159151, 176.38906383, 0.03477454, 123.47234468, -1483.35367347, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 44.09726596, 6.247e-05, 132.29179787, 0.0001874, 440.97265958, 0.00062465, -44.09726596, -6.247e-05, -132.29179787, -0.0001874, -440.97265958, -0.00062465, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.425)
    ops.node(122013, 0.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.2025, 27235374.89790257, 11348072.87412607, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 189.62045634, 0.0005825, 228.64570219, 0.01476644, 22.86457022, 0.03431638, -189.62045634, -0.0005825, -228.64570219, -0.01476644, -22.86457022, -0.03431638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 180.03583819, 0.0005825, 217.08850108, 0.01476644, 21.70885011, 0.03431638, -180.03583819, -0.0005825, -217.08850108, -0.01476644, -21.70885011, -0.03431638, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 171.35978164, 0.01165003, 171.35978164, 0.03495009, 119.95184715, -1493.63903501, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 42.83994541, 6.264e-05, 128.51983623, 0.00018792, 428.39945411, 0.00062638, -42.83994541, -6.264e-05, -128.51983623, -0.00018792, -428.39945411, -0.00062638, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 171.35978164, 0.01165003, 171.35978164, 0.03495009, 119.95184715, -1493.63903501, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 42.83994541, 6.264e-05, 128.51983623, 0.00018792, 428.39945411, 0.00062638, -42.83994541, -6.264e-05, -128.51983623, -0.00018792, -428.39945411, -0.00062638, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.5, 9.0, 3.425)
    ops.node(122014, 4.5, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.3025, 28261072.16301993, 11775446.73459164, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 348.67550193, 0.00053725, 420.53443306, 0.01520967, 42.05344331, 0.03840735, -348.67550193, -0.00053725, -420.53443306, -0.01520967, -42.05344331, -0.03840735, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 329.6372301, 0.00053725, 397.57254212, 0.01520967, 39.75725421, 0.03840735, -329.6372301, -0.00053725, -397.57254212, -0.01520967, -39.75725421, -0.03840735, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 316.95093313, 0.01074496, 316.95093313, 0.03223487, 221.86565319, -2285.14317886, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 79.23773328, 7.474e-05, 237.71319985, 0.00022423, 792.37733283, 0.00074743, -79.23773328, -7.474e-05, -237.71319985, -0.00022423, -792.37733283, -0.00074743, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 316.95093313, 0.01074496, 316.95093313, 0.03223487, 221.86565319, -2285.14317886, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 79.23773328, 7.474e-05, 237.71319985, 0.00022423, 792.37733283, 0.00074743, -79.23773328, -7.474e-05, -237.71319985, -0.00022423, -792.37733283, -0.00074743, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 9.0, 3.425)
    ops.node(122015, 9.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.3025, 28281314.79391966, 11783881.16413319, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 330.82760634, 0.00052996, 399.62792448, 0.01929824, 39.96279245, 0.04732211, -330.82760634, -0.00052996, -399.62792448, -0.01929824, -39.96279245, -0.04732211, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 311.91286385, 0.00052996, 376.77959157, 0.01929824, 37.67795916, 0.04732211, -311.91286385, -0.00052996, -376.77959157, -0.01929824, -37.67795916, -0.04732211, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 322.70585319, 0.0105992, 322.70585319, 0.03179759, 225.89409723, -2465.79973702, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 80.6764633, 7.605e-05, 242.02938989, 0.00022814, 806.76463298, 0.00076045, -80.6764633, -7.605e-05, -242.02938989, -0.00022814, -806.76463298, -0.00076045, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 322.70585319, 0.0105992, 322.70585319, 0.03179759, 225.89409723, -2465.79973702, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 80.6764633, 7.605e-05, 242.02938989, 0.00022814, 806.76463298, 0.00076045, -80.6764633, -7.605e-05, -242.02938989, -0.00022814, -806.76463298, -0.00076045, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.0, 9.0, 3.425)
    ops.node(122016, 12.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.3025, 26726912.51378809, 11136213.5474117, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 328.85658775, 0.00053667, 397.71027695, 0.01874983, 39.7710277, 0.04470244, -328.85658775, -0.00053667, -397.71027695, -0.01874983, -39.7710277, -0.04470244, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 309.86427469, 0.00053667, 374.74148641, 0.01874983, 37.47414864, 0.04470244, -309.86427469, -0.00053667, -374.74148641, -0.01874983, -37.47414864, -0.04470244, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 303.27169865, 0.01073342, 303.27169865, 0.03220027, 212.29018906, -2420.75698302, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 75.81792466, 7.562e-05, 227.45377399, 0.00022687, 758.17924663, 0.00075622, -75.81792466, -7.562e-05, -227.45377399, -0.00022687, -758.17924663, -0.00075622, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 303.27169865, 0.01073342, 303.27169865, 0.03220027, 212.29018906, -2420.75698302, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 75.81792466, 7.562e-05, 227.45377399, 0.00022687, 758.17924663, 0.00075622, -75.81792466, -7.562e-05, -227.45377399, -0.00022687, -758.17924663, -0.00075622, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 16.5, 9.0, 3.425)
    ops.node(122017, 16.5, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.3025, 27053243.33385048, 11272184.7224377, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 348.92859722, 0.00053845, 421.15389, 0.01534629, 42.115389, 0.03707259, -348.92859722, -0.00053845, -421.15389, -0.01534629, -42.115389, -0.03707259, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 329.3146054, 0.00053845, 397.4799664, 0.01534629, 39.74799664, 0.03707259, -329.3146054, -0.00053845, -397.4799664, -0.01534629, -39.74799664, -0.03707259, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 304.35984531, 0.01076908, 304.35984531, 0.03230724, 213.05189172, -2311.9174758, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 76.08996133, 7.498e-05, 228.26988398, 0.00022493, 760.89961328, 0.00074978, -76.08996133, -7.498e-05, -228.26988398, -0.00022493, -760.89961328, -0.00074978, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 304.35984531, 0.01076908, 304.35984531, 0.03230724, 213.05189172, -2311.9174758, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 76.08996133, 7.498e-05, 228.26988398, 0.00022493, 760.89961328, 0.00074978, -76.08996133, -7.498e-05, -228.26988398, -0.00022493, -760.89961328, -0.00074978, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.425)
    ops.node(122018, 21.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.2025, 25624750.62083347, 10676979.42534728, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 186.89197873, 0.00058963, 225.29978087, 0.01408289, 22.52997809, 0.03154903, -186.89197873, -0.00058963, -225.29978087, -0.01408289, -22.52997809, -0.03154903, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 177.46469866, 0.00058963, 213.93511905, 0.01408289, 21.39351191, 0.03154903, -177.46469866, -0.00058963, -213.93511905, -0.01408289, -21.39351191, -0.03154903, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 161.26703036, 0.01179263, 161.26703036, 0.03537788, 112.88692125, -1490.42259285, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 40.31675759, 6.265e-05, 120.95027277, 0.00018796, 403.1675759, 0.00062654, -40.31675759, -6.265e-05, -120.95027277, -0.00018796, -403.1675759, -0.00062654, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 161.26703036, 0.01179263, 161.26703036, 0.03537788, 112.88692125, -1490.42259285, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 40.31675759, 6.265e-05, 120.95027277, 0.00018796, 403.1675759, 0.00062654, -40.31675759, -6.265e-05, -120.95027277, -0.00018796, -403.1675759, -0.00062654, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.375)
    ops.node(122019, 0.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.1225, 26463191.30196878, 11026329.70915366, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 79.03138902, 0.00064458, 95.32068836, 0.01735506, 9.53206884, 0.04732835, -79.03138902, -0.00064458, -95.32068836, -0.01735506, -9.53206884, -0.04732835, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 79.03138902, 0.00064458, 95.32068836, 0.01735506, 9.53206884, 0.04732835, -79.03138902, -0.00064458, -95.32068836, -0.01735506, -9.53206884, -0.04732835, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 117.10585548, 0.01289157, 117.10585548, 0.03867471, 81.97409883, -1335.29780653, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 29.27646387, 7.283e-05, 87.82939161, 0.00021848, 292.76463869, 0.00072827, -29.27646387, -7.283e-05, -87.82939161, -0.00021848, -292.76463869, -0.00072827, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 117.10585548, 0.01289157, 117.10585548, 0.03867471, 81.97409883, -1335.29780653, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 29.27646387, 7.283e-05, 87.82939161, 0.00021848, 292.76463869, 0.00072827, -29.27646387, -7.283e-05, -87.82939161, -0.00021848, -292.76463869, -0.00072827, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 4.5, 13.5, 3.425)
    ops.node(122020, 4.5, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.25, 26821208.68327714, 11175503.61803214, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 216.00904184, 0.00055088, 261.3129389, 0.01454354, 26.13129389, 0.03428788, -216.00904184, -0.00055088, -261.3129389, -0.01454354, -26.13129389, -0.03428788, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 205.61481865, 0.00055088, 248.73871986, 0.01454354, 24.87387199, 0.03428788, -205.61481865, -0.00055088, -248.73871986, -0.01454354, -24.87387199, -0.03428788, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 213.77685977, 0.01101761, 213.77685977, 0.03305284, 149.64380184, -1569.75903928, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 53.44421494, 6.427e-05, 160.33264483, 0.00019282, 534.44214943, 0.00064274, -53.44421494, -6.427e-05, -160.33264483, -0.00019282, -534.44214943, -0.00064274, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 213.77685977, 0.01101761, 213.77685977, 0.03305284, 149.64380184, -1569.75903928, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 53.44421494, 6.427e-05, 160.33264483, 0.00019282, 534.44214943, 0.00064274, -53.44421494, -6.427e-05, -160.33264483, -0.00019282, -534.44214943, -0.00064274, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.425)
    ops.node(122021, 9.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.2025, 26533323.29096138, 11055551.37123391, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 168.88843974, 0.00057808, 204.1220678, 0.01463235, 20.41220678, 0.03461169, -168.88843974, -0.00057808, -204.1220678, -0.01463235, -20.41220678, -0.03461169, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 178.48698525, 0.00057808, 215.7230688, 0.01463235, 21.57230688, 0.03461169, -178.48698525, -0.00057808, -215.7230688, -0.01463235, -21.57230688, -0.03461169, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 160.85075022, 0.01156165, 160.85075022, 0.03468494, 112.59552516, -1359.97610944, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 40.21268756, 6.035e-05, 120.63806267, 0.00018106, 402.12687555, 0.00060353, -40.21268756, -6.035e-05, -120.63806267, -0.00018106, -402.12687555, -0.00060353, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 160.85075022, 0.01156165, 160.85075022, 0.03468494, 112.59552516, -1359.97610944, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 40.21268756, 6.035e-05, 120.63806267, 0.00018106, 402.12687555, 0.00060353, -40.21268756, -6.035e-05, -120.63806267, -0.00018106, -402.12687555, -0.00060353, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.425)
    ops.node(122022, 12.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.2025, 26487986.70970289, 11036661.12904287, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 166.65259009, 0.00057698, 201.42145322, 0.01482003, 20.14214532, 0.03474478, -166.65259009, -0.00057698, -201.42145322, -0.01482003, -20.14214532, -0.03474478, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 175.84398448, 0.00057698, 212.53045558, 0.01482003, 21.25304556, 0.03474478, -175.84398448, -0.00057698, -212.53045558, -0.01482003, -21.25304556, -0.03474478, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 161.55910847, 0.01153968, 161.55910847, 0.03461904, 113.09137593, -1380.92908536, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 40.38977712, 6.072e-05, 121.16933135, 0.00018217, 403.89777117, 0.00060722, -40.38977712, -6.072e-05, -121.16933135, -0.00018217, -403.89777117, -0.00060722, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 161.55910847, 0.01153968, 161.55910847, 0.03461904, 113.09137593, -1380.92908536, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 40.38977712, 6.072e-05, 121.16933135, 0.00018217, 403.89777117, 0.00060722, -40.38977712, -6.072e-05, -121.16933135, -0.00018217, -403.89777117, -0.00060722, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 16.5, 13.5, 3.425)
    ops.node(122023, 16.5, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.25, 26546988.5390944, 11061245.22462267, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 213.6315946, 0.00054024, 258.46526175, 0.01460838, 25.84652617, 0.03405777, -213.6315946, -0.00054024, -258.46526175, -0.01460838, -25.84652617, -0.03405777, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 203.25646601, 0.00054024, 245.91276299, 0.01460838, 24.5912763, 0.03405777, -203.25646601, -0.00054024, -245.91276299, -0.01460838, -24.5912763, -0.03405777, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 211.27512161, 0.0108048, 211.27512161, 0.0324144, 147.89258513, -1565.14741048, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 52.8187804, 6.418e-05, 158.45634121, 0.00019253, 528.18780403, 0.00064178, -52.8187804, -6.418e-05, -158.45634121, -0.00019253, -528.18780403, -0.00064178, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 211.27512161, 0.0108048, 211.27512161, 0.0324144, 147.89258513, -1565.14741048, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 52.8187804, 6.418e-05, 158.45634121, 0.00019253, 528.18780403, 0.00064178, -52.8187804, -6.418e-05, -158.45634121, -0.00019253, -528.18780403, -0.00064178, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.375)
    ops.node(122024, 21.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.1225, 26532703.90003129, 11055293.29167971, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 80.50266662, 0.00063362, 97.09578445, 0.01715997, 9.70957844, 0.04727584, -80.50266662, -0.00063362, -97.09578445, -0.01715997, -9.70957844, -0.04727584, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 80.50266662, 0.00063362, 97.09578445, 0.01715997, 9.70957844, 0.04727584, -80.50266662, -0.00063362, -97.09578445, -0.01715997, -9.70957844, -0.04727584, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 116.80445124, 0.01267241, 116.80445124, 0.03801722, 81.76311587, -1321.26087723, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 29.20111281, 7.245e-05, 87.60333843, 0.00021735, 292.0111281, 0.00072449, -29.20111281, -7.245e-05, -87.60333843, -0.00021735, -292.0111281, -0.00072449, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 116.80445124, 0.01267241, 116.80445124, 0.03801722, 81.76311587, -1321.26087723, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 29.20111281, 7.245e-05, 87.60333843, 0.00021735, 292.0111281, 0.00072449, -29.20111281, -7.245e-05, -87.60333843, -0.00021735, -292.0111281, -0.00072449, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.15)
    ops.node(123001, 0.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.09, 26688861.56221139, 11120358.98425475, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 45.12312763, 0.00070754, 54.56134985, 0.01911758, 5.45613498, 0.05595051, -45.12312763, -0.00070754, -54.56134985, -0.01911758, -5.45613498, -0.05595051, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 47.98467478, 0.00070754, 58.02143525, 0.01911758, 5.80214352, 0.05595051, -47.98467478, -0.00070754, -58.02143525, -0.01911758, -5.80214352, -0.05595051, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 88.96155739, 0.01415076, 88.96155739, 0.04245228, 62.27309017, -1074.24716102, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 22.24038935, 7.467e-05, 66.72116804, 0.000224, 222.40389347, 0.00074666, -22.24038935, -7.467e-05, -66.72116804, -0.000224, -222.40389347, -0.00074666, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 88.96155739, 0.01415076, 88.96155739, 0.04245228, 62.27309017, -1074.24716102, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 22.24038935, 7.467e-05, 66.72116804, 0.000224, 222.40389347, 0.00074666, -22.24038935, -7.467e-05, -66.72116804, -0.000224, -222.40389347, -0.00074666, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.5, 0.0, 6.225)
    ops.node(123002, 4.5, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1225, 26897834.17970275, 11207430.90820948, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 98.50065663, 0.00068617, 118.65185539, 0.01544374, 11.86518554, 0.03698313, -98.50065663, -0.00068617, -118.65185539, -0.01544374, -11.86518554, -0.03698313, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 98.50065663, 0.00068617, 118.65185539, 0.01544374, 11.86518554, 0.03698313, -98.50065663, -0.00068617, -118.65185539, -0.01544374, -11.86518554, -0.03698313, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 106.79646036, 0.0137235, 106.79646036, 0.04117049, 74.75752226, -1049.85685857, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 26.69911509, 6.534e-05, 80.09734527, 0.00019603, 266.99115091, 0.00065342, -26.69911509, -6.534e-05, -80.09734527, -0.00019603, -266.99115091, -0.00065342, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 106.79646036, 0.0137235, 106.79646036, 0.04117049, 74.75752226, -1049.85685857, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 26.69911509, 6.534e-05, 80.09734527, 0.00019603, 266.99115091, 0.00065342, -26.69911509, -6.534e-05, -80.09734527, -0.00019603, -266.99115091, -0.00065342, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.5, 0.0, 6.225)
    ops.node(123005, 16.5, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 25788174.79244663, 10745072.8301861, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 101.04075261, 0.00069599, 121.66451659, 0.01463429, 12.16645166, 0.03444787, -101.04075261, -0.00069599, -121.66451659, -0.01463429, -12.16645166, -0.03444787, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 101.04075261, 0.00069599, 121.66451659, 0.01463429, 12.16645166, 0.03444787, -101.04075261, -0.00069599, -121.66451659, -0.01463429, -12.16645166, -0.03444787, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 101.86092047, 0.0139199, 101.86092047, 0.04175969, 71.30264433, -1030.68205085, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 25.46523012, 6.5e-05, 76.39569035, 0.00019501, 254.65230118, 0.00065004, -25.46523012, -6.5e-05, -76.39569035, -0.00019501, -254.65230118, -0.00065004, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 101.86092047, 0.0139199, 101.86092047, 0.04175969, 71.30264433, -1030.68205085, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 25.46523012, 6.5e-05, 76.39569035, 0.00019501, 254.65230118, 0.00065004, -25.46523012, -6.5e-05, -76.39569035, -0.00019501, -254.65230118, -0.00065004, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 21.0, 0.0, 6.15)
    ops.node(123006, 21.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.09, 27697873.8242552, 11540780.76010633, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 46.07522798, 0.00068814, 55.67975851, 0.01872359, 5.56797585, 0.05755784, -46.07522798, -0.00068814, -55.67975851, -0.01872359, -5.56797585, -0.05755784, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 49.25943006, 0.00068814, 59.52771784, 0.01872359, 5.95277178, 0.05755784, -49.25943006, -0.00068814, -59.52771784, -0.01872359, -5.95277178, -0.05755784, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 89.82905076, 0.01376287, 89.82905076, 0.0412886, 62.88033553, -1022.78667451, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 22.45726269, 7.265e-05, 67.37178807, 0.00021794, 224.57262689, 0.00072647, -22.45726269, -7.265e-05, -67.37178807, -0.00021794, -224.57262689, -0.00072647, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 89.82905076, 0.01376287, 89.82905076, 0.0412886, 62.88033553, -1022.78667451, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 22.45726269, 7.265e-05, 67.37178807, 0.00021794, 224.57262689, 0.00072647, -22.45726269, -7.265e-05, -67.37178807, -0.00021794, -224.57262689, -0.00072647, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.225)
    ops.node(123007, 0.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 26230690.76793905, 10929454.48664127, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 99.66634186, 0.00068459, 120.02218496, 0.01516122, 12.0022185, 0.03559848, -99.66634186, -0.00068459, -120.02218496, -0.01516122, -12.0022185, -0.03559848, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 99.66634186, 0.00068459, 120.02218496, 0.01516122, 12.0022185, 0.03559848, -99.66634186, -0.00068459, -120.02218496, -0.01516122, -12.0022185, -0.03559848, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 104.20456496, 0.01369172, 104.20456496, 0.04107515, 72.94319547, -1046.86138517, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 26.05114124, 6.538e-05, 78.15342372, 0.00019613, 260.5114124, 0.00065378, -26.05114124, -6.538e-05, -78.15342372, -0.00019613, -260.5114124, -0.00065378, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 104.20456496, 0.01369172, 104.20456496, 0.04107515, 72.94319547, -1046.86138517, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 26.05114124, 6.538e-05, 78.15342372, 0.00019613, 260.5114124, 0.00065378, -26.05114124, -6.538e-05, -78.15342372, -0.00019613, -260.5114124, -0.00065378, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.5, 4.5, 6.225)
    ops.node(123008, 4.5, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.25, 26383840.34136065, 10993266.80890027, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 225.09952758, 0.00056002, 272.58149774, 0.01367309, 27.25814977, 0.03541355, -225.09952758, -0.00056002, -272.58149774, -0.01367309, -27.25814977, -0.03541355, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 225.09952758, 0.00056002, 272.58149774, 0.01367309, 27.25814977, 0.03541355, -225.09952758, -0.00056002, -272.58149774, -0.01367309, -27.25814977, -0.03541355, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 210.38331795, 0.01120049, 210.38331795, 0.03360147, 147.26832257, -1636.52158573, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 52.59582949, 6.43e-05, 157.78748846, 0.00019291, 525.95829488, 0.00064302, -52.59582949, -6.43e-05, -157.78748846, -0.00019291, -525.95829488, -0.00064302, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 210.38331795, 0.01120049, 210.38331795, 0.03360147, 147.26832257, -1636.52158573, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 52.59582949, 6.43e-05, 157.78748846, 0.00019291, 525.95829488, 0.00064302, -52.59582949, -6.43e-05, -157.78748846, -0.00019291, -525.95829488, -0.00064302, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.225)
    ops.node(123009, 9.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.25, 26877483.53855051, 11198951.47439605, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 215.56773788, 0.00055387, 261.43254547, 0.01369582, 26.14325455, 0.03719366, -215.56773788, -0.00055387, -261.43254547, -0.01369582, -26.14325455, -0.03719366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 215.56773788, 0.00055387, 261.43254547, 0.01369582, 26.14325455, 0.03719366, -215.56773788, -0.00055387, -261.43254547, -0.01369582, -26.14325455, -0.03719366, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 208.75702671, 0.01107744, 208.75702671, 0.03323232, 146.1299187, -1542.2166952, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 52.18925668, 6.263e-05, 156.56777003, 0.0001879, 521.89256678, 0.00062633, -52.18925668, -6.263e-05, -156.56777003, -0.0001879, -521.89256678, -0.00062633, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 208.75702671, 0.01107744, 208.75702671, 0.03323232, 146.1299187, -1542.2166952, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 52.18925668, 6.263e-05, 156.56777003, 0.0001879, 521.89256678, 0.00062633, -52.18925668, -6.263e-05, -156.56777003, -0.0001879, -521.89256678, -0.00062633, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.225)
    ops.node(123010, 12.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.25, 25906703.05202293, 10794459.60500956, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 212.17007802, 0.00055564, 257.45988752, 0.01362156, 25.74598875, 0.03606041, -212.17007802, -0.00055564, -257.45988752, -0.01362156, -25.74598875, -0.03606041, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 212.17007802, 0.00055564, 257.45988752, 0.01362156, 25.74598875, 0.03606041, -212.17007802, -0.00055564, -257.45988752, -0.01362156, -25.74598875, -0.03606041, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 201.36595275, 0.01111282, 201.36595275, 0.03333847, 140.95616692, -1564.4624803, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 50.34148819, 6.268e-05, 151.02446456, 0.00018804, 503.41488187, 0.00062679, -50.34148819, -6.268e-05, -151.02446456, -0.00018804, -503.41488187, -0.00062679, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 201.36595275, 0.01111282, 201.36595275, 0.03333847, 140.95616692, -1564.4624803, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 50.34148819, 6.268e-05, 151.02446456, 0.00018804, 503.41488187, 0.00062679, -50.34148819, -6.268e-05, -151.02446456, -0.00018804, -503.41488187, -0.00062679, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 16.5, 4.5, 6.225)
    ops.node(123011, 16.5, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.25, 25088271.5882031, 10453446.49508462, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 226.71658227, 0.00056311, 274.54700239, 0.013398, 27.45470024, 0.03349104, -226.71658227, -0.00056311, -274.54700239, -0.013398, -27.45470024, -0.03349104, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 226.71658227, 0.00056311, 274.54700239, 0.013398, 27.45470024, 0.03349104, -226.71658227, -0.00056311, -274.54700239, -0.013398, -27.45470024, -0.03349104, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 201.35392919, 0.01126225, 201.35392919, 0.03378676, 140.94775043, -1659.99950897, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 50.3384823, 6.472e-05, 151.01544689, 0.00019416, 503.38482297, 0.0006472, -50.3384823, -6.472e-05, -151.01544689, -0.00019416, -503.38482297, -0.0006472, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 201.35392919, 0.01126225, 201.35392919, 0.03378676, 140.94775043, -1659.99950897, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 50.3384823, 6.472e-05, 151.01544689, 0.00019416, 503.38482297, 0.0006472, -50.3384823, -6.472e-05, -151.01544689, -0.00019416, -503.38482297, -0.0006472, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.225)
    ops.node(123012, 21.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 26375445.95798659, 10989769.14916108, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 98.97270727, 0.00069172, 119.19355556, 0.01502998, 11.91935556, 0.03569378, -98.97270727, -0.00069172, -119.19355556, -0.01502998, -11.91935556, -0.03569378, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 98.97270727, 0.00069172, 119.19355556, 0.01502998, 11.91935556, 0.03569378, -98.97270727, -0.00069172, -119.19355556, -0.01502998, -11.91935556, -0.03569378, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 104.34523387, 0.01383438, 104.34523387, 0.04150314, 73.04166371, -1038.48138515, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 26.08630847, 6.511e-05, 78.2589254, 0.00019532, 260.86308468, 0.00065107, -26.08630847, -6.511e-05, -78.2589254, -0.00019532, -260.86308468, -0.00065107, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 104.34523387, 0.01383438, 104.34523387, 0.04150314, 73.04166371, -1038.48138515, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 26.08630847, 6.511e-05, 78.2589254, 0.00019532, 260.86308468, 0.00065107, -26.08630847, -6.511e-05, -78.2589254, -0.00019532, -260.86308468, -0.00065107, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.225)
    ops.node(123013, 0.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.1225, 27143234.15025897, 11309680.89594124, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 98.40204774, 0.00069387, 118.5282062, 0.01531431, 11.85282062, 0.03719372, -98.40204774, -0.00069387, -118.5282062, -0.01531431, -11.85282062, -0.03719372, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 98.40204774, 0.00069387, 118.5282062, 0.01531431, 11.85282062, 0.03719372, -98.40204774, -0.00069387, -118.5282062, -0.01531431, -11.85282062, -0.03719372, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 107.14556004, 0.01387748, 107.14556004, 0.04163243, 75.00189203, -1037.80641689, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 26.78639001, 6.496e-05, 80.35917003, 0.00019489, 267.8639001, 0.00064963, -26.78639001, -6.496e-05, -80.35917003, -0.00019489, -267.8639001, -0.00064963, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 107.14556004, 0.01387748, 107.14556004, 0.04163243, 75.00189203, -1037.80641689, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 26.78639001, 6.496e-05, 80.35917003, 0.00019489, 267.8639001, 0.00064963, -26.78639001, -6.496e-05, -80.35917003, -0.00019489, -267.8639001, -0.00064963, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.5, 9.0, 6.225)
    ops.node(123014, 4.5, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.25, 27452161.96860532, 11438400.82025222, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 226.54844508, 0.00055545, 274.1786569, 0.01347515, 27.41786569, 0.03646259, -226.54844508, -0.00055545, -274.1786569, -0.01347515, -27.41786569, -0.03646259, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 226.54844508, 0.00055545, 274.1786569, 0.01347515, 27.41786569, 0.03646259, -226.54844508, -0.00055545, -274.1786569, -0.01347515, -27.41786569, -0.03646259, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 219.59754332, 0.01110903, 219.59754332, 0.03332709, 153.71828033, -1650.64902684, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 54.89938583, 6.451e-05, 164.69815749, 0.00019352, 548.99385831, 0.00064506, -54.89938583, -6.451e-05, -164.69815749, -0.00019352, -548.99385831, -0.00064506, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 219.59754332, 0.01110903, 219.59754332, 0.03332709, 153.71828033, -1650.64902684, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 54.89938583, 6.451e-05, 164.69815749, 0.00019352, 548.99385831, 0.00064506, -54.89938583, -6.451e-05, -164.69815749, -0.00019352, -548.99385831, -0.00064506, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.225)
    ops.node(123015, 9.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.25, 26789130.55022599, 11162137.72926083, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 211.62197127, 0.00054395, 256.62888487, 0.01373915, 25.66288849, 0.03704703, -211.62197127, -0.00054395, -256.62888487, -0.01373915, -25.66288849, -0.03704703, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 211.62197127, 0.00054395, 256.62888487, 0.01373915, 25.66288849, 0.03704703, -211.62197127, -0.00054395, -256.62888487, -0.01373915, -25.66288849, -0.03704703, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 207.18443733, 0.01087892, 207.18443733, 0.03263676, 145.02910613, -1546.07755177, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 51.79610933, 6.237e-05, 155.38832799, 0.0001871, 517.96109331, 0.00062366, -51.79610933, -6.237e-05, -155.38832799, -0.0001871, -517.96109331, -0.00062366, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 207.18443733, 0.01087892, 207.18443733, 0.03263676, 145.02910613, -1546.07755177, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 51.79610933, 6.237e-05, 155.38832799, 0.0001871, 517.96109331, 0.00062366, -51.79610933, -6.237e-05, -155.38832799, -0.0001871, -517.96109331, -0.00062366, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.225)
    ops.node(123016, 12.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.25, 26687389.72910357, 11119745.72045982, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 215.08900883, 0.0005529, 260.85266911, 0.01381077, 26.08526691, 0.03701132, -215.08900883, -0.0005529, -260.85266911, -0.01381077, -26.08526691, -0.03701132, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 215.08900883, 0.0005529, 260.85266911, 0.01381077, 26.08526691, 0.03701132, -215.08900883, -0.0005529, -260.85266911, -0.01381077, -26.08526691, -0.03701132, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 209.13384722, 0.01105803, 209.13384722, 0.03317408, 146.39369305, -1557.92694201, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 52.2834618, 6.319e-05, 156.85038541, 0.00018958, 522.83461805, 0.00063193, -52.2834618, -6.319e-05, -156.85038541, -0.00018958, -522.83461805, -0.00063193, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 209.13384722, 0.01105803, 209.13384722, 0.03317408, 146.39369305, -1557.92694201, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 52.2834618, 6.319e-05, 156.85038541, 0.00018958, 522.83461805, 0.00063193, -52.2834618, -6.319e-05, -156.85038541, -0.00018958, -522.83461805, -0.00063193, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 16.5, 9.0, 6.225)
    ops.node(123017, 16.5, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.25, 27361088.28677649, 11400453.45282354, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 228.1456578, 0.00054917, 276.13294115, 0.01323696, 27.61329412, 0.03612846, -228.1456578, -0.00054917, -276.13294115, -0.01323696, -27.61329412, -0.03612846, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 228.1456578, 0.00054917, 276.13294115, 0.01323696, 27.61329412, 0.03612846, -228.1456578, -0.00054917, -276.13294115, -0.01323696, -27.61329412, -0.03612846, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 215.52281703, 0.01098332, 215.52281703, 0.03294995, 150.86597192, -1630.15623164, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 53.88070426, 6.352e-05, 161.64211277, 0.00019056, 538.80704257, 0.0006352, -53.88070426, -6.352e-05, -161.64211277, -0.00019056, -538.80704257, -0.0006352, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 215.52281703, 0.01098332, 215.52281703, 0.03294995, 150.86597192, -1630.15623164, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 53.88070426, 6.352e-05, 161.64211277, 0.00019056, 538.80704257, 0.0006352, -53.88070426, -6.352e-05, -161.64211277, -0.00019056, -538.80704257, -0.0006352, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.225)
    ops.node(123018, 21.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1225, 26680509.41510691, 11116878.92296121, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 98.6927581, 0.00068542, 118.87754851, 0.01538372, 11.88775485, 0.03657934, -98.6927581, -0.00068542, -118.87754851, -0.01538372, -11.88775485, -0.03657934, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 98.6927581, 0.00068542, 118.87754851, 0.01538372, 11.88775485, 0.03657934, -98.6927581, -0.00068542, -118.87754851, -0.01538372, -11.88775485, -0.03657934, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 106.29967525, 0.0137085, 106.29967525, 0.04112549, 74.40977267, -1056.48299511, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 26.57491881, 6.557e-05, 79.72475643, 0.0001967, 265.74918811, 0.00065568, -26.57491881, -6.557e-05, -79.72475643, -0.0001967, -265.74918811, -0.00065568, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 106.29967525, 0.0137085, 106.29967525, 0.04112549, 74.40977267, -1056.48299511, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 26.57491881, 6.557e-05, 79.72475643, 0.0001967, 265.74918811, 0.00065568, -26.57491881, -6.557e-05, -79.72475643, -0.0001967, -265.74918811, -0.00065568, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.15)
    ops.node(123019, 0.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.09, 27707894.89182694, 11544956.20492789, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 45.53251034, 0.00069757, 55.0234543, 0.01938404, 5.50234543, 0.05823709, -45.53251034, -0.00069757, -55.0234543, -0.01938404, -5.50234543, -0.05823709, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 48.47691214, 0.00069757, 58.58159676, 0.01938404, 5.85815968, 0.05823709, -48.47691214, -0.00069757, -58.58159676, -0.01938404, -5.85815968, -0.05823709, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 90.79935893, 0.01395145, 90.79935893, 0.04185435, 63.55955125, -1049.38873055, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 22.69983973, 7.341e-05, 68.09951919, 0.00022022, 226.99839731, 0.00073405, -22.69983973, -7.341e-05, -68.09951919, -0.00022022, -226.99839731, -0.00073405, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 90.79935893, 0.01395145, 90.79935893, 0.04185435, 63.55955125, -1049.38873055, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 22.69983973, 7.341e-05, 68.09951919, 0.00022022, 226.99839731, 0.00073405, -22.69983973, -7.341e-05, -68.09951919, -0.00022022, -226.99839731, -0.00073405, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 4.5, 13.5, 6.225)
    ops.node(123020, 4.5, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.16, 27552701.81754821, 11480292.42397842, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 117.2129584, 0.000614, 141.72127435, 0.01565416, 14.17212743, 0.03887981, -117.2129584, -0.000614, -141.72127435, -0.01565416, -14.17212743, -0.03887981, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 117.2129584, 0.000614, 141.72127435, 0.01565416, 14.17212743, 0.03887981, -117.2129584, -0.000614, -141.72127435, -0.01565416, -14.17212743, -0.03887981, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 130.93721567, 0.01228009, 130.93721567, 0.03684028, 91.65605097, -1118.25500132, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 32.73430392, 5.988e-05, 98.20291175, 0.00017963, 327.34303917, 0.00059878, -32.73430392, -5.988e-05, -98.20291175, -0.00017963, -327.34303917, -0.00059878, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 130.93721567, 0.01228009, 130.93721567, 0.03684028, 91.65605097, -1118.25500132, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 32.73430392, 5.988e-05, 98.20291175, 0.00017963, 327.34303917, 0.00059878, -32.73430392, -5.988e-05, -98.20291175, -0.00017963, -327.34303917, -0.00059878, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.225)
    ops.node(123021, 9.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.1225, 27406442.89243533, 11419351.20518139, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 93.68742425, 0.00067001, 113.08639664, 0.01601345, 11.30863966, 0.03974064, -93.68742425, -0.00067001, -113.08639664, -0.01601345, -11.30863966, -0.03974064, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 93.68742425, 0.00067001, 113.08639664, 0.01601345, 11.30863966, 0.03974064, -93.68742425, -0.00067001, -113.08639664, -0.01601345, -11.30863966, -0.03974064, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 105.47946108, 0.01340027, 105.47946108, 0.0402008, 73.83562276, -980.45692363, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 26.36986527, 6.334e-05, 79.10959581, 0.00019002, 263.6986527, 0.00063339, -26.36986527, -6.334e-05, -79.10959581, -0.00019002, -263.6986527, -0.00063339, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 105.47946108, 0.01340027, 105.47946108, 0.0402008, 73.83562276, -980.45692363, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 26.36986527, 6.334e-05, 79.10959581, 0.00019002, 263.6986527, 0.00063339, -26.36986527, -6.334e-05, -79.10959581, -0.00019002, -263.6986527, -0.00063339, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.225)
    ops.node(123022, 12.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.1225, 26232237.80671642, 10930099.08613184, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 92.78080874, 0.00068211, 112.02051538, 0.01549361, 11.20205154, 0.03757584, -92.78080874, -0.00068211, -112.02051538, -0.01549361, -11.20205154, -0.03757584, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 92.78080874, 0.00068211, 112.02051538, 0.01549361, 11.20205154, 0.03757584, -92.78080874, -0.00068211, -112.02051538, -0.01549361, -11.20205154, -0.03757584, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 100.55032118, 0.01364229, 100.55032118, 0.04092688, 70.38522483, -965.46159045, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 25.1375803, 6.308e-05, 75.41274089, 0.00018924, 251.37580296, 0.00063082, -25.1375803, -6.308e-05, -75.41274089, -0.00018924, -251.37580296, -0.00063082, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 100.55032118, 0.01364229, 100.55032118, 0.04092688, 70.38522483, -965.46159045, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 25.1375803, 6.308e-05, 75.41274089, 0.00018924, 251.37580296, 0.00063082, -25.1375803, -6.308e-05, -75.41274089, -0.00018924, -251.37580296, -0.00063082, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 16.5, 13.5, 6.225)
    ops.node(123023, 16.5, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.16, 26956901.5582561, 11232042.31594004, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 118.17108137, 0.00060624, 142.93657403, 0.01542938, 14.2936574, 0.0379691, -118.17108137, -0.00060624, -142.93657403, -0.01542938, -14.2936574, -0.0379691, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 118.17108137, 0.00060624, 142.93657403, 0.01542938, 14.2936574, 0.0379691, -118.17108137, -0.00060624, -142.93657403, -0.01542938, -14.2936574, -0.0379691, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 127.88747541, 0.01212483, 127.88747541, 0.03637448, 89.52123279, -1112.92331098, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 31.97186885, 5.978e-05, 95.91560656, 0.00017933, 319.71868852, 0.00059776, -31.97186885, -5.978e-05, -95.91560656, -0.00017933, -319.71868852, -0.00059776, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 127.88747541, 0.01212483, 127.88747541, 0.03637448, 89.52123279, -1112.92331098, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 31.97186885, 5.978e-05, 95.91560656, 0.00017933, 319.71868852, 0.00059776, -31.97186885, -5.978e-05, -95.91560656, -0.00017933, -319.71868852, -0.00059776, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.15)
    ops.node(123024, 21.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.09, 28020785.52828126, 11675327.30345052, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 46.09846967, 0.00068288, 55.69171094, 0.01917511, 5.56917109, 0.05860529, -46.09846967, -0.00068288, -55.69171094, -0.01917511, -5.56917109, -0.05860529, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 49.2969419, 0.00068288, 59.55579562, 0.01917511, 5.95557956, 0.05860529, -49.2969419, -0.00068288, -59.55579562, -0.01917511, -5.95557956, -0.05860529, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 91.51423107, 0.01365764, 91.51423107, 0.04097292, 64.05996175, -1045.78176274, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 22.87855777, 7.316e-05, 68.6356733, 0.00021947, 228.78557767, 0.00073157, -22.87855777, -7.316e-05, -68.6356733, -0.00021947, -228.78557767, -0.00073157, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 91.51423107, 0.01365764, 91.51423107, 0.04097292, 64.05996175, -1045.78176274, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 22.87855777, 7.316e-05, 68.6356733, 0.00021947, 228.78557767, 0.00073157, -22.87855777, -7.316e-05, -68.6356733, -0.00021947, -228.78557767, -0.00073157, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.95)
    ops.node(124001, 0.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.09, 26106585.30467727, 10877743.87694887, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 32.39985555, 0.00068493, 39.59376149, 0.02184362, 3.95937615, 0.07046319, -32.39985555, -0.00068493, -39.59376149, -0.02184362, -3.95937615, -0.07046319, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 29.93959752, 0.00068493, 36.58723976, 0.02184362, 3.65872398, 0.07046319, -29.93959752, -0.00068493, -36.58723976, -0.02184362, -3.65872398, -0.07046319, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 76.47710753, 0.01369852, 76.47710753, 0.04109557, 53.53397527, -1166.91543264, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 19.11927688, 6.562e-05, 57.35783065, 0.00019686, 191.19276882, 0.00065619, -19.11927688, -6.562e-05, -57.35783065, -0.00019686, -191.19276882, -0.00065619, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 76.47710753, 0.01369852, 76.47710753, 0.04109557, 53.53397527, -1166.91543264, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 19.11927688, 6.562e-05, 57.35783065, 0.00019686, 191.19276882, 0.00065619, -19.11927688, -6.562e-05, -57.35783065, -0.00019686, -191.19276882, -0.00065619, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.5, 0.0, 8.95)
    ops.node(124002, 4.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1225, 26842956.52266024, 11184565.2177751, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 70.78961652, 0.00062966, 86.22595187, 0.01794484, 8.62259519, 0.04784565, -70.78961652, -0.00062966, -86.22595187, -0.01794484, -8.62259519, -0.04784565, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 70.78961652, 0.00062966, 86.22595187, 0.01794484, 8.62259519, 0.04784565, -70.78961652, -0.00062966, -86.22595187, -0.01794484, -8.62259519, -0.04784565, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 90.1755546, 0.01259317, 90.1755546, 0.0377795, 63.12288822, -763.28529196, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 22.54388865, 5.529e-05, 67.63166595, 0.00016586, 225.4388865, 0.00055286, -22.54388865, -5.529e-05, -67.63166595, -0.00016586, -225.4388865, -0.00055286, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 90.1755546, 0.01259317, 90.1755546, 0.0377795, 63.12288822, -763.28529196, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 22.54388865, 5.529e-05, 67.63166595, 0.00016586, 225.4388865, 0.00055286, -22.54388865, -5.529e-05, -67.63166595, -0.00016586, -225.4388865, -0.00055286, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.5, 0.0, 8.95)
    ops.node(124005, 16.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 27388082.48513245, 11411701.03547185, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 72.00351856, 0.00062576, 87.63638961, 0.01777487, 8.76363896, 0.04811677, -72.00351856, -0.00062576, -87.63638961, -0.01777487, -8.76363896, -0.04811677, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 72.00351856, 0.00062576, 87.63638961, 0.01777487, 8.76363896, 0.04811677, -72.00351856, -0.00062576, -87.63638961, -0.01777487, -8.76363896, -0.04811677, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 91.43021566, 0.01251519, 91.43021566, 0.03754557, 64.00115096, -745.0170536, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 22.85755392, 5.494e-05, 68.57266175, 0.00016482, 228.57553915, 0.00054939, -22.85755392, -5.494e-05, -68.57266175, -0.00016482, -228.57553915, -0.00054939, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 91.43021566, 0.01251519, 91.43021566, 0.03754557, 64.00115096, -745.0170536, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 22.85755392, 5.494e-05, 68.57266175, 0.00016482, 228.57553915, 0.00054939, -22.85755392, -5.494e-05, -68.57266175, -0.00016482, -228.57553915, -0.00054939, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 21.0, 0.0, 8.95)
    ops.node(124006, 21.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.09, 27951067.20068721, 11646278.00028634, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 33.03238042, 0.00065886, 40.24362553, 0.02175027, 4.02436255, 0.0721543, -33.03238042, -0.00065886, -40.24362553, -0.02175027, -4.02436255, -0.0721543, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 30.38377838, 0.00065886, 37.01681148, 0.02175027, 3.70168115, 0.0721543, -30.38377838, -0.00065886, -37.01681148, -0.02175027, -3.70168115, -0.0721543, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 80.78826147, 0.01317713, 80.78826147, 0.03953138, 56.55178303, -1151.21543497, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 20.19706537, 6.474e-05, 60.5911961, 0.00019423, 201.97065367, 0.00064744, -20.19706537, -6.474e-05, -60.5911961, -0.00019423, -201.97065367, -0.00064744, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 80.78826147, 0.01317713, 80.78826147, 0.03953138, 56.55178303, -1151.21543497, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 20.19706537, 6.474e-05, 60.5911961, 0.00019423, 201.97065367, 0.00064744, -20.19706537, -6.474e-05, -60.5911961, -0.00019423, -201.97065367, -0.00064744, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 8.95)
    ops.node(124007, 0.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 26591556.82590693, 11079815.34412789, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 71.20940084, 0.00062882, 86.76269614, 0.01801599, 8.67626961, 0.04767516, -71.20940084, -0.00062882, -86.76269614, -0.01801599, -8.67626961, -0.04767516, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 71.20940084, 0.00062882, 86.76269614, 0.01801599, 8.67626961, 0.04767516, -71.20940084, -0.00062882, -86.76269614, -0.01801599, -8.67626961, -0.04767516, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 88.99909857, 0.01257643, 88.99909857, 0.03772928, 62.299369, -753.1826182, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 22.24977464, 5.508e-05, 66.74932392, 0.00016524, 222.49774641, 0.0005508, -22.24977464, -5.508e-05, -66.74932392, -0.00016524, -222.49774641, -0.0005508, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 88.99909857, 0.01257643, 88.99909857, 0.03772928, 62.299369, -753.1826182, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 22.24977464, 5.508e-05, 66.74932392, 0.00016524, 222.49774641, 0.0005508, -22.24977464, -5.508e-05, -66.74932392, -0.00016524, -222.49774641, -0.0005508, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.5, 4.5, 8.95)
    ops.node(124008, 4.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.25, 25090835.0619092, 10454514.60912883, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 167.88366364, 0.00054137, 205.16794795, 0.01520254, 20.5167948, 0.04158907, -167.88366364, -0.00054137, -205.16794795, -0.01520254, -20.5167948, -0.04158907, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 167.88366364, 0.00054137, 205.16794795, 0.01520254, 20.5167948, 0.04158907, -167.88366364, -0.00054137, -205.16794795, -0.01520254, -20.5167948, -0.04158907, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 173.74265895, 0.01082738, 173.74265895, 0.03248215, 121.61986127, -1283.51121944, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 43.43566474, 5.584e-05, 130.30699422, 0.00016752, 434.35664738, 0.0005584, -43.43566474, -5.584e-05, -130.30699422, -0.00016752, -434.35664738, -0.0005584, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 173.74265895, 0.01082738, 173.74265895, 0.03248215, 121.61986127, -1283.51121944, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 43.43566474, 5.584e-05, 130.30699422, 0.00016752, 434.35664738, 0.0005584, -43.43566474, -5.584e-05, -130.30699422, -0.00016752, -434.35664738, -0.0005584, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.0, 4.5, 8.95)
    ops.node(124009, 9.0, 4.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.25, 27715689.11378571, 11548203.79741071, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 163.45066442, 0.00052223, 199.229839, 0.01518746, 19.9229839, 0.04416208, -163.45066442, -0.00052223, -199.229839, -0.01518746, -19.9229839, -0.04416208, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 163.45066442, 0.00052223, 199.229839, 0.01518746, 19.9229839, 0.04416208, -163.45066442, -0.00052223, -199.229839, -0.01518746, -19.9229839, -0.04416208, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 192.90107101, 0.01044459, 192.90107101, 0.03133378, 135.03074971, -1274.22682644, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 48.22526775, 5.613e-05, 144.67580326, 0.00016838, 482.25267753, 0.00056125, -48.22526775, -5.613e-05, -144.67580326, -0.00016838, -482.25267753, -0.00056125, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 192.90107101, 0.01044459, 192.90107101, 0.03133378, 135.03074971, -1274.22682644, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 48.22526775, 5.613e-05, 144.67580326, 0.00016838, 482.25267753, 0.00056125, -48.22526775, -5.613e-05, -144.67580326, -0.00016838, -482.25267753, -0.00056125, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.0, 4.5, 8.95)
    ops.node(124010, 12.0, 4.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.25, 27581499.36750476, 11492291.40312698, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 161.2111691, 0.00051726, 196.54887033, 0.01538671, 19.65488703, 0.04429337, -161.2111691, -0.00051726, -196.54887033, -0.01538671, -19.65488703, -0.04429337, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 161.2111691, 0.00051726, 196.54887033, 0.01538671, 19.65488703, 0.04429337, -161.2111691, -0.00051726, -196.54887033, -0.01538671, -19.65488703, -0.04429337, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 192.47422148, 0.0103453, 192.47422148, 0.0310359, 134.73195504, -1271.98847715, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 48.11855537, 5.627e-05, 144.35566611, 0.00016882, 481.1855537, 0.00056274, -48.11855537, -5.627e-05, -144.35566611, -0.00016882, -481.1855537, -0.00056274, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 192.47422148, 0.0103453, 192.47422148, 0.0310359, 134.73195504, -1271.98847715, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 48.11855537, 5.627e-05, 144.35566611, 0.00016882, 481.1855537, 0.00056274, -48.11855537, -5.627e-05, -144.35566611, -0.00016882, -481.1855537, -0.00056274, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 16.5, 4.5, 8.95)
    ops.node(124011, 16.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.25, 27348439.74072105, 11395183.22530044, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 172.57179895, 0.00052297, 210.29206574, 0.01490977, 21.02920657, 0.04290823, -172.57179895, -0.00052297, -210.29206574, -0.01490977, -21.02920657, -0.04290823, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 172.57179895, 0.00052297, 210.29206574, 0.01490977, 21.02920657, 0.04290823, -172.57179895, -0.00052297, -210.29206574, -0.01490977, -21.02920657, -0.04290823, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 188.86538212, 0.01045943, 188.86538212, 0.03137828, 132.20576748, -1268.5429835, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 47.21634553, 5.569e-05, 141.64903659, 0.00016707, 472.1634553, 0.00055689, -47.21634553, -5.569e-05, -141.64903659, -0.00016707, -472.1634553, -0.00055689, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 188.86538212, 0.01045943, 188.86538212, 0.03137828, 132.20576748, -1268.5429835, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 47.21634553, 5.569e-05, 141.64903659, 0.00016707, 472.1634553, 0.00055689, -47.21634553, -5.569e-05, -141.64903659, -0.00016707, -472.1634553, -0.00055689, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 8.95)
    ops.node(124012, 21.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 26522495.82934444, 11051039.92889352, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 69.96889008, 0.00063228, 85.25846398, 0.01817446, 8.5258464, 0.04777326, -69.96889008, -0.00063228, -85.25846398, -0.01817446, -8.5258464, -0.04777326, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 69.96889008, 0.00063228, 85.25846398, 0.01817446, 8.5258464, 0.04777326, -69.96889008, -0.00063228, -85.25846398, -0.01817446, -8.5258464, -0.04777326, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 89.23801105, 0.01264563, 89.23801105, 0.0379369, 62.46660774, -766.96759586, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 22.30950276, 5.537e-05, 66.92850829, 0.00016612, 223.09502763, 0.00055372, -22.30950276, -5.537e-05, -66.92850829, -0.00016612, -223.09502763, -0.00055372, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 89.23801105, 0.01264563, 89.23801105, 0.0379369, 62.46660774, -766.96759586, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 22.30950276, 5.537e-05, 66.92850829, 0.00016612, 223.09502763, 0.00055372, -22.30950276, -5.537e-05, -66.92850829, -0.00016612, -223.09502763, -0.00055372, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.0, 8.95)
    ops.node(124013, 0.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.1225, 28278733.56870843, 11782805.65362851, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 70.58319764, 0.00062498, 85.77795572, 0.01801262, 8.57779557, 0.04898701, -70.58319764, -0.00062498, -85.77795572, -0.01801262, -8.57779557, -0.04898701, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 70.58319764, 0.00062498, 85.77795572, 0.01801262, 8.57779557, 0.04898701, -70.58319764, -0.00062498, -85.77795572, -0.01801262, -8.57779557, -0.04898701, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 95.1973556, 0.01249958, 95.1973556, 0.03749873, 66.63814892, -762.50643398, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 23.7993389, 5.54e-05, 71.3980167, 0.0001662, 237.99338899, 0.00055401, -23.7993389, -5.54e-05, -71.3980167, -0.0001662, -237.99338899, -0.00055401, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 95.1973556, 0.01249958, 95.1973556, 0.03749873, 66.63814892, -762.50643398, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 23.7993389, 5.54e-05, 71.3980167, 0.0001662, 237.99338899, 0.00055401, -23.7993389, -5.54e-05, -71.3980167, -0.0001662, -237.99338899, -0.00055401, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.5, 9.0, 8.95)
    ops.node(124014, 4.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.25, 26899858.36208466, 11208274.31753528, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 165.13883188, 0.00053087, 201.37653447, 0.01510227, 20.13765345, 0.04281932, -165.13883188, -0.00053087, -201.37653447, -0.01510227, -20.13765345, -0.04281932, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 165.13883188, 0.00053087, 201.37653447, 0.01510227, 20.13765345, 0.04281932, -165.13883188, -0.00053087, -201.37653447, -0.01510227, -20.13765345, -0.04281932, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 189.22789, 0.01061737, 189.22789, 0.03185211, 132.459523, -1288.31436141, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 47.3069725, 5.673e-05, 141.9209175, 0.00017018, 473.06972499, 0.00056726, -47.3069725, -5.673e-05, -141.9209175, -0.00017018, -473.06972499, -0.00056726, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 189.22789, 0.01061737, 189.22789, 0.03185211, 132.459523, -1288.31436141, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 47.3069725, 5.673e-05, 141.9209175, 0.00017018, 473.06972499, 0.00056726, -47.3069725, -5.673e-05, -141.9209175, -0.00017018, -473.06972499, -0.00056726, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 9.0, 8.95)
    ops.node(124015, 9.0, 9.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.25, 27678370.32265912, 11532654.30110797, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 163.00310518, 0.00052195, 198.64457217, 0.0149741, 19.86445722, 0.04369822, -163.00310518, -0.00052195, -198.64457217, -0.0149741, -19.86445722, -0.04369822, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 163.00310518, 0.00052195, 198.64457217, 0.0149741, 19.86445722, 0.04369822, -163.00310518, -0.00052195, -198.64457217, -0.0149741, -19.86445722, -0.04369822, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 190.61355336, 0.01043899, 190.61355336, 0.03131697, 133.42948735, -1248.69301126, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 47.65338834, 5.553e-05, 142.96016502, 0.0001666, 476.5338834, 0.00055535, -47.65338834, -5.553e-05, -142.96016502, -0.0001666, -476.5338834, -0.00055535, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 190.61355336, 0.01043899, 190.61355336, 0.03131697, 133.42948735, -1248.69301126, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 47.65338834, 5.553e-05, 142.96016502, 0.0001666, 476.5338834, 0.00055535, -47.65338834, -5.553e-05, -142.96016502, -0.0001666, -476.5338834, -0.00055535, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.0, 9.0, 8.95)
    ops.node(124016, 12.0, 9.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.25, 25783029.20447534, 10742928.83519806, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 166.19070228, 0.00052732, 203.11801729, 0.01489927, 20.31180173, 0.04247727, -166.19070228, -0.00052732, -203.11801729, -0.01489927, -20.31180173, -0.04247727, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 166.19070228, 0.00052732, 203.11801729, 0.01489927, 20.31180173, 0.04247727, -166.19070228, -0.00052732, -203.11801729, -0.01489927, -20.31180173, -0.04247727, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 175.13451234, 0.01054637, 175.13451234, 0.03163911, 122.59415864, -1266.33198118, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 43.78362808, 5.478e-05, 131.35088425, 0.00016433, 437.83628084, 0.00054776, -43.78362808, -5.478e-05, -131.35088425, -0.00016433, -437.83628084, -0.00054776, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 175.13451234, 0.01054637, 175.13451234, 0.03163911, 122.59415864, -1266.33198118, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 43.78362808, 5.478e-05, 131.35088425, 0.00016433, 437.83628084, 0.00054776, -43.78362808, -5.478e-05, -131.35088425, -0.00016433, -437.83628084, -0.00054776, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 16.5, 9.0, 8.95)
    ops.node(124017, 16.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.25, 27249964.79293175, 11354151.9970549, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 171.51668759, 0.00053324, 209.03987927, 0.0149161, 20.90398793, 0.04285426, -171.51668759, -0.00053324, -209.03987927, -0.0149161, -20.90398793, -0.04285426, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 171.51668759, 0.00053324, 209.03987927, 0.0149161, 20.90398793, 0.04285426, -171.51668759, -0.00053324, -209.03987927, -0.0149161, -20.90398793, -0.04285426, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 192.1487906, 0.01066473, 192.1487906, 0.0319942, 134.50415342, -1283.47318734, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 48.03719765, 5.686e-05, 144.11159295, 0.00017059, 480.37197651, 0.00056862, -48.03719765, -5.686e-05, -144.11159295, -0.00017059, -480.37197651, -0.00056862, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 192.1487906, 0.01066473, 192.1487906, 0.0319942, 134.50415342, -1283.47318734, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 48.03719765, 5.686e-05, 144.11159295, 0.00017059, 480.37197651, 0.00056862, -48.03719765, -5.686e-05, -144.11159295, -0.00017059, -480.37197651, -0.00056862, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 21.0, 9.0, 8.95)
    ops.node(124018, 21.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1225, 26303059.90471404, 10959608.29363085, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 70.96577237, 0.00063756, 86.49549632, 0.01822689, 8.64954963, 0.04763012, -70.96577237, -0.00063756, -86.49549632, -0.01822689, -8.64954963, -0.04763012, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 70.96577237, 0.00063756, 86.49549632, 0.01822689, 8.64954963, 0.04763012, -70.96577237, -0.00063756, -86.49549632, -0.01822689, -8.64954963, -0.04763012, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 88.38754485, 0.01275122, 88.38754485, 0.03825365, 61.87128139, -763.95707721, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 22.09688621, 5.53e-05, 66.29065864, 0.00016591, 220.96886212, 0.00055302, -22.09688621, -5.53e-05, -66.29065864, -0.00016591, -220.96886212, -0.00055302, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 88.38754485, 0.01275122, 88.38754485, 0.03825365, 61.87128139, -763.95707721, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 22.09688621, 5.53e-05, 66.29065864, 0.00016591, 220.96886212, 0.00055302, -22.09688621, -5.53e-05, -66.29065864, -0.00016591, -220.96886212, -0.00055302, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 13.5, 8.95)
    ops.node(124019, 0.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.09, 27031581.40423301, 11263158.91843042, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 32.3290847, 0.00067994, 39.45191644, 0.02199566, 3.94519164, 0.071568, -32.3290847, -0.00067994, -39.45191644, -0.02199566, -3.94519164, -0.071568, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 29.91419608, 0.00067994, 36.504973, 0.02199566, 3.6504973, 0.071568, -29.91419608, -0.00067994, -36.504973, -0.02199566, -3.6504973, -0.071568, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 78.21217278, 0.01359883, 78.21217278, 0.04079649, 54.74852095, -1139.17213852, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 19.55304319, 6.481e-05, 58.65912958, 0.00019443, 195.53043195, 0.00064811, -19.55304319, -6.481e-05, -58.65912958, -0.00019443, -195.53043195, -0.00064811, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 78.21217278, 0.01359883, 78.21217278, 0.04079649, 54.74852095, -1139.17213852, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 19.55304319, 6.481e-05, 58.65912958, 0.00019443, 195.53043195, 0.00064811, -19.55304319, -6.481e-05, -58.65912958, -0.00019443, -195.53043195, -0.00064811, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 4.5, 13.5, 8.95)
    ops.node(124020, 4.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.16, 26984222.45498868, 11243426.02291195, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 83.76726807, 0.00056235, 102.18267557, 0.01733684, 10.21826756, 0.04638934, -83.76726807, -0.00056235, -102.18267557, -0.01733684, -10.21826756, -0.04638934, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 83.76726807, 0.00056235, 102.18267557, 0.01733684, 10.21826756, 0.04638934, -83.76726807, -0.00056235, -102.18267557, -0.01733684, -10.21826756, -0.04638934, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 110.83024584, 0.011247, 110.83024584, 0.033741, 77.58117209, -852.93429454, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 27.70756146, 5.175e-05, 83.12268438, 0.00015525, 277.07561461, 0.00051751, -27.70756146, -5.175e-05, -83.12268438, -0.00015525, -277.07561461, -0.00051751, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 110.83024584, 0.011247, 110.83024584, 0.033741, 77.58117209, -852.93429454, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 27.70756146, 5.175e-05, 83.12268438, 0.00015525, 277.07561461, 0.00051751, -27.70756146, -5.175e-05, -83.12268438, -0.00015525, -277.07561461, -0.00051751, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 8.95)
    ops.node(124021, 9.0, 13.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.1225, 27376815.42528432, 11407006.4272018, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 69.58891453, 0.00063114, 84.76566889, 0.01833788, 8.47656689, 0.0493909, -69.58891453, -0.00063114, -84.76566889, -0.01833788, -8.47656689, -0.0493909, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 69.58891453, 0.00063114, 84.76566889, 0.01833788, 8.47656689, 0.0493909, -69.58891453, -0.00063114, -84.76566889, -0.01833788, -8.47656689, -0.0493909, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 91.15753746, 0.0126228, 91.15753746, 0.0378684, 63.81027622, -769.48919033, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 22.78938436, 5.48e-05, 68.36815309, 0.00016439, 227.89384364, 0.00054798, -22.78938436, -5.48e-05, -68.36815309, -0.00016439, -227.89384364, -0.00054798, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 91.15753746, 0.0126228, 91.15753746, 0.0378684, 63.81027622, -769.48919033, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 22.78938436, 5.48e-05, 68.36815309, 0.00016439, 227.89384364, 0.00054798, -22.78938436, -5.48e-05, -68.36815309, -0.00016439, -227.89384364, -0.00054798, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 8.95)
    ops.node(124022, 12.0, 13.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.1225, 27988215.76168216, 11661756.56736757, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 69.73914747, 0.00062992, 84.8598941, 0.0181431, 8.48598941, 0.04961352, -69.73914747, -0.00062992, -84.8598941, -0.0181431, -8.48598941, -0.04961352, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 69.73914747, 0.00062992, 84.8598941, 0.0181431, 8.48598941, 0.04961352, -69.73914747, -0.00062992, -84.8598941, -0.0181431, -8.48598941, -0.04961352, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 92.55348065, 0.01259838, 92.55348065, 0.03779515, 64.78743645, -746.80726673, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 23.13837016, 5.442e-05, 69.41511049, 0.00016327, 231.38370162, 0.00054422, -23.13837016, -5.442e-05, -69.41511049, -0.00016327, -231.38370162, -0.00054422, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 92.55348065, 0.01259838, 92.55348065, 0.03779515, 64.78743645, -746.80726673, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 23.13837016, 5.442e-05, 69.41511049, 0.00016327, 231.38370162, 0.00054422, -23.13837016, -5.442e-05, -69.41511049, -0.00016327, -231.38370162, -0.00054422, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 16.5, 13.5, 8.95)
    ops.node(124023, 16.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.16, 27822591.95492088, 11592746.6478837, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 83.06973206, 0.00055902, 101.18615408, 0.01729163, 10.11861541, 0.04683481, -83.06973206, -0.00055902, -101.18615408, -0.01729163, -10.11861541, -0.04683481, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 83.06973206, 0.00055902, 101.18615408, 0.01729163, 10.11861541, 0.04683481, -83.06973206, -0.00055902, -101.18615408, -0.01729163, -10.11861541, -0.04683481, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 113.02923805, 0.01118033, 113.02923805, 0.03354098, 79.12046664, -805.29050995, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 28.25730951, 5.119e-05, 84.77192854, 0.00015356, 282.57309514, 0.00051187, -28.25730951, -5.119e-05, -84.77192854, -0.00015356, -282.57309514, -0.00051187, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 113.02923805, 0.01118033, 113.02923805, 0.03354098, 79.12046664, -805.29050995, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 28.25730951, 5.119e-05, 84.77192854, 0.00015356, 282.57309514, 0.00051187, -28.25730951, -5.119e-05, -84.77192854, -0.00015356, -282.57309514, -0.00051187, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 21.0, 13.5, 8.95)
    ops.node(124024, 21.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.09, 26362405.82806616, 10984335.76169423, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 33.03500606, 0.00064216, 40.35535761, 0.02211064, 4.03553576, 0.07100639, -33.03500606, -0.00064216, -40.35535761, -0.02211064, -4.03553576, -0.07100639, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 30.19153007, 0.00064216, 36.88178505, 0.02211064, 3.6881785, 0.07100639, -30.19153007, -0.00064216, -36.88178505, -0.02211064, -3.6881785, -0.07100639, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 76.91938326, 0.01284317, 76.91938326, 0.03852952, 53.84356828, -1157.59416128, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 19.22984581, 6.536e-05, 57.68953744, 0.00019607, 192.29845814, 0.00065358, -19.22984581, -6.536e-05, -57.68953744, -0.00019607, -192.29845814, -0.00065358, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 76.91938326, 0.01284317, 76.91938326, 0.03852952, 53.84356828, -1157.59416128, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 19.22984581, 6.536e-05, 57.68953744, 0.00019607, 192.29845814, 0.00065358, -19.22984581, -6.536e-05, -57.68953744, -0.00019607, -192.29845814, -0.00065358, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(124025, 9.0, 0.0, 1.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.2025, 26405404.39190637, 11002251.82996099, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 363.66821031, 0.00055265, 436.70932833, 0.04755103, 43.67093283, 0.11107424, -363.66821031, -0.00055265, -436.70932833, -0.04755103, -43.67093283, -0.11107424, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 346.61250625, 0.00055265, 416.22806312, 0.04100925, 41.62280631, 0.08552612, -346.61250625, -0.00055265, -416.22806312, -0.04100925, -41.62280631, -0.08552612, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 381.54604777, 0.01105305, 381.54604777, 0.03315915, 267.08223344, -7128.30916336, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 95.38651194, 7.963e-05, 286.15953583, 0.0002389, 953.86511943, 0.00079633, -95.38651194, -7.963e-05, -286.15953583, -0.0002389, -953.86511943, -0.00079633, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 440.38573128, 0.01105305, 440.38573128, 0.03315915, 308.2700119, -10746.05148544, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 110.09643282, 9.191e-05, 330.28929846, 0.00027574, 1100.96432821, 0.00091914, -110.09643282, -9.191e-05, -330.28929846, -0.00027574, -1100.96432821, -0.00091914, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.875)
    ops.node(121003, 9.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.2025, 25422002.01762319, 10592500.84067633, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 262.1090075, 0.00054042, 315.03219882, 0.04275068, 31.50321988, 0.10409491, -262.1090075, -0.00054042, -315.03219882, -0.04275068, -31.50321988, -0.10409491, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 245.50401768, 0.00054042, 295.07444725, 0.03687537, 29.50744473, 0.07986522, -245.50401768, -0.00054042, -295.07444725, -0.03687537, -29.50744473, -0.07986522, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 362.16406056, 0.01080835, 362.16406056, 0.03242506, 253.51484239, -6965.57605446, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 90.54101514, 7.851e-05, 271.62304542, 0.00023554, 905.4101514, 0.00078512, -90.54101514, -7.851e-05, -271.62304542, -0.00023554, -905.4101514, -0.00078512, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 419.90757893, 0.01080835, 419.90757893, 0.03242506, 293.93530525, -10623.54839737, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 104.97689473, 9.103e-05, 314.9306842, 0.00027309, 1049.76894732, 0.0009103, -104.97689473, -9.103e-05, -314.9306842, -0.00027309, -1049.76894732, -0.0009103, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.0, 0.0, 0.0)
    ops.node(124026, 12.0, 0.0, 1.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.2025, 27150015.24173502, 11312506.35072293, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 366.29066894, 0.00054698, 440.00551178, 0.04834416, 44.00055118, 0.11580466, -366.29066894, -0.00054698, -440.00551178, -0.04834416, -44.00055118, -0.11580466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 349.08043567, 0.00054698, 419.3317733, 0.04169119, 41.93317733, 0.08896731, -349.08043567, -0.00054698, -419.3317733, -0.04169119, -41.93317733, -0.08896731, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 387.29442731, 0.01093952, 387.29442731, 0.03281856, 271.10609911, -6973.46660056, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 96.82360683, 7.862e-05, 290.47082048, 0.00023585, 968.23606827, 0.00078616, -96.82360683, -7.862e-05, -290.47082048, -0.00023585, -968.23606827, -0.00078616, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 444.72378607, 0.01093952, 444.72378607, 0.03281856, 311.30665025, -10461.22269502, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 111.18094652, 9.027e-05, 333.54283955, 0.00027082, 1111.80946517, 0.00090273, -111.18094652, -9.027e-05, -333.54283955, -0.00027082, -1111.80946517, -0.00090273, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.875)
    ops.node(121004, 12.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.2025, 26657018.3080194, 11107090.96167475, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 261.97867403, 0.00053603, 315.15531995, 0.04408976, 31.51553199, 0.11218833, -261.97867403, -0.00053603, -315.15531995, -0.04408976, -31.51553199, -0.11218833, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 245.79268688, 0.00053603, 295.68388787, 0.03802745, 29.56838879, 0.08575071, -245.79268688, -0.00053603, -295.68388787, -0.03802745, -29.56838879, -0.08575071, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 372.4459396, 0.01072062, 372.4459396, 0.03216186, 260.71215772, -6762.36499734, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 93.1114849, 7.7e-05, 279.3344547, 0.000231, 931.11484901, 0.00077, -93.1114849, -7.7e-05, -279.3344547, -0.000231, -931.11484901, -0.00077, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 428.38384566, 0.01072062, 428.38384566, 0.03216186, 299.86869196, -10247.70712534, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 107.09596142, 8.856e-05, 321.28788425, 0.00026569, 1070.95961415, 0.00088565, -107.09596142, -8.856e-05, -321.28788425, -0.00026569, -1070.95961415, -0.00088565, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.425)
    ops.node(124027, 9.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.2025, 26711388.59547016, 11129745.24811256, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 190.26269895, 0.0005154, 229.88834221, 0.03888477, 22.98883422, 0.09347091, -190.26269895, -0.0005154, -229.88834221, -0.03888477, -22.98883422, -0.09347091, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 175.27595753, 0.0005154, 211.78034123, 0.03888477, 21.17803412, 0.09347091, -175.27595753, -0.0005154, -211.78034123, -0.03888477, -21.17803412, -0.09347091, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 375.81640641, 0.01030799, 375.81640641, 0.03092397, 263.07148449, -7576.67876692, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 93.9541016, 7.003e-05, 281.86230481, 0.0002101, 939.54101603, 0.00070035, -93.9541016, -7.003e-05, -281.86230481, -0.0002101, -939.54101603, -0.00070035, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 375.81640641, 0.01030799, 375.81640641, 0.03092397, 263.07148449, -7576.67876692, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 93.9541016, 7.003e-05, 281.86230481, 0.0002101, 939.54101603, 0.00070035, -93.9541016, -7.003e-05, -281.86230481, -0.0002101, -939.54101603, -0.00070035, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.825)
    ops.node(122003, 9.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.2025, 27446671.3110828, 11436113.0462845, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 183.50145452, 0.00051387, 221.95976272, 0.04020651, 22.19597627, 0.09952947, -183.50145452, -0.00051387, -221.95976272, -0.04020651, -22.19597627, -0.09952947, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 168.77291503, 0.00051387, 204.14441003, 0.04020651, 20.414441, 0.09952947, -168.77291503, -0.00051387, -204.14441003, -0.04020651, -20.414441, -0.09952947, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 379.78034083, 0.01027737, 379.78034083, 0.0308321, 265.84623858, -7804.53006463, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 94.94508521, 6.888e-05, 284.83525562, 0.00020663, 949.45085207, 0.00068878, -94.94508521, -6.888e-05, -284.83525562, -0.00020663, -949.45085207, -0.00068878, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 379.78034083, 0.01027737, 379.78034083, 0.0308321, 265.84623858, -7804.53006463, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 94.94508521, 6.888e-05, 284.83525562, 0.00020663, 949.45085207, 0.00068878, -94.94508521, -6.888e-05, -284.83525562, -0.00020663, -949.45085207, -0.00068878, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.425)
    ops.node(124028, 12.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.2025, 26581815.53040947, 11075756.47100395, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 190.01150205, 0.00051507, 229.59147532, 0.03895155, 22.95914753, 0.0931153, -190.01150205, -0.00051507, -229.59147532, -0.03895155, -22.95914753, -0.0931153, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 175.01243863, 0.00051507, 211.46806141, 0.03895155, 21.14680614, 0.0931153, -175.01243863, -0.00051507, -211.46806141, -0.03895155, -21.14680614, -0.0931153, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 378.04599648, 0.01030144, 378.04599648, 0.03090431, 264.63219753, -7843.75054389, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 94.51149912, 7.079e-05, 283.53449736, 0.00021238, 945.11499119, 0.00070794, -94.51149912, -7.079e-05, -283.53449736, -0.00021238, -945.11499119, -0.00070794, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 378.04599648, 0.01030144, 378.04599648, 0.03090431, 264.63219753, -7843.75054389, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 94.51149912, 7.079e-05, 283.53449736, 0.00021238, 945.11499119, 0.00070794, -94.51149912, -7.079e-05, -283.53449736, -0.00021238, -945.11499119, -0.00070794, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.825)
    ops.node(122004, 12.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.2025, 27660153.34724265, 11525063.89468444, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 182.17306239, 0.0005126, 220.31322329, 0.040414, 22.03132233, 0.10033307, -182.17306239, -0.0005126, -220.31322329, -0.040414, -22.03132233, -0.10033307, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 167.77713656, 0.0005126, 202.90333415, 0.040414, 20.29033341, 0.10033307, -167.77713656, -0.0005126, -202.90333415, -0.040414, -20.29033341, -0.10033307, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 384.70369532, 0.01025208, 384.70369532, 0.03075624, 269.29258672, -7982.90824608, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 96.17592383, 6.923e-05, 288.52777149, 0.0002077, 961.75923829, 0.00069232, -96.17592383, -6.923e-05, -288.52777149, -0.0002077, -961.75923829, -0.00069232, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 384.70369532, 0.01025208, 384.70369532, 0.03075624, 269.29258672, -7982.90824608, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 96.17592383, 6.923e-05, 288.52777149, 0.0002077, 961.75923829, 0.00069232, -96.17592383, -6.923e-05, -288.52777149, -0.0002077, -961.75923829, -0.00069232, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.225)
    ops.node(124029, 9.0, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.1225, 26881539.53745082, 11200641.47393784, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 93.98244198, 0.00055815, 113.45288892, 0.03348706, 11.34528889, 0.08070529, -93.98244198, -0.00055815, -113.45288892, -0.03348706, -11.34528889, -0.08070529, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 93.98244198, 0.00055815, 113.45288892, 0.03348706, 11.34528889, 0.08070529, -93.98244198, -0.00055815, -113.45288892, -0.03348706, -11.34528889, -0.08070529, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 188.3049017, 0.01116307, 188.3049017, 0.03348922, 131.81343119, -3904.93253121, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 47.07622542, 5.764e-05, 141.22867627, 0.00017292, 470.76225424, 0.00057641, -47.07622542, -5.764e-05, -141.22867627, -0.00017292, -470.76225424, -0.00057641, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 188.3049017, 0.01116307, 188.3049017, 0.03348922, 131.81343119, -3904.93253121, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 47.07622542, 5.764e-05, 141.22867627, 0.00017292, 470.76225424, 0.00057641, -47.07622542, -5.764e-05, -141.22867627, -0.00017292, -470.76225424, -0.00057641, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.55)
    ops.node(123003, 9.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.1225, 26242168.98445798, 10934237.07685749, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 88.32107303, 0.00054439, 106.92221607, 0.03487865, 10.69222161, 0.08414573, -88.32107303, -0.00054439, -106.92221607, -0.03487865, -10.69222161, -0.08414573, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 88.32107303, 0.00054439, 106.92221607, 0.03487865, 10.69222161, 0.08414573, -88.32107303, -0.00054439, -106.92221607, -0.03487865, -10.69222161, -0.08414573, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 180.22174279, 0.01088783, 180.22174279, 0.03266349, 126.15521995, -3989.19418743, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 45.0554357, 5.651e-05, 135.16630709, 0.00016953, 450.55435698, 0.00056511, -45.0554357, -5.651e-05, -135.16630709, -0.00016953, -450.55435698, -0.00056511, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 180.22174279, 0.01088783, 180.22174279, 0.03266349, 126.15521995, -3989.19418743, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 45.0554357, 5.651e-05, 135.16630709, 0.00016953, 450.55435698, 0.00056511, -45.0554357, -5.651e-05, -135.16630709, -0.00016953, -450.55435698, -0.00056511, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.225)
    ops.node(124030, 12.0, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.1225, 27188326.80541951, 11328469.50225813, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 92.75198737, 0.00055992, 111.95657953, 0.03394253, 11.19565795, 0.08202918, -92.75198737, -0.00055992, -111.95657953, -0.03394253, -11.19565795, -0.08202918, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 92.75198737, 0.00055992, 111.95657953, 0.03394253, 11.19565795, 0.08202918, -92.75198737, -0.00055992, -111.95657953, -0.03394253, -11.19565795, -0.08202918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 191.48834998, 0.01119842, 191.48834998, 0.03359527, 134.04184498, -3993.46273858, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 47.87208749, 5.795e-05, 143.61626248, 0.00017386, 478.72087494, 0.00057954, -47.87208749, -5.795e-05, -143.61626248, -0.00017386, -478.72087494, -0.00057954, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 191.48834998, 0.01119842, 191.48834998, 0.03359527, 134.04184498, -3993.46273858, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 47.87208749, 5.795e-05, 143.61626248, 0.00017386, 478.72087494, 0.00057954, -47.87208749, -5.795e-05, -143.61626248, -0.00017386, -478.72087494, -0.00057954, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.55)
    ops.node(123004, 12.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.1225, 25947705.68861183, 10811544.0369216, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 86.20158748, 0.00054437, 104.36156289, 0.03468173, 10.43615629, 0.0831091, -86.20158748, -0.00054437, -104.36156289, -0.03468173, -10.43615629, -0.0831091, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 86.20158748, 0.00054437, 104.36156289, 0.03468173, 10.43615629, 0.0831091, -86.20158748, -0.00054437, -104.36156289, -0.03468173, -10.43615629, -0.0831091, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 179.31263211, 0.01088734, 179.31263211, 0.03266201, 125.51884248, -4041.38030032, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 44.82815803, 5.686e-05, 134.48447409, 0.00017059, 448.28158028, 0.00056864, -44.82815803, -5.686e-05, -134.48447409, -0.00017059, -448.28158028, -0.00056864, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 179.31263211, 0.01088734, 179.31263211, 0.03266201, 125.51884248, -4041.38030032, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 44.82815803, 5.686e-05, 134.48447409, 0.00017059, 448.28158028, 0.00056864, -44.82815803, -5.686e-05, -134.48447409, -0.00017059, -448.28158028, -0.00056864, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 8.95)
    ops.node(124031, 9.0, 0.0, 9.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.1225, 27143555.57800379, 11309814.82416824, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 68.47909533, 0.00052714, 83.45290156, 0.01834752, 8.34529016, 0.04932555, -68.47909533, -0.00052714, -83.45290156, -0.01834752, -8.34529016, -0.04932555, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 68.47909533, 0.00052714, 83.45290156, 0.01834752, 8.34529016, 0.04932555, -68.47909533, -0.00052714, -83.45290156, -0.01834752, -8.34529016, -0.04932555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 129.4739189, 0.01054277, 129.4739189, 0.0316283, 90.63174323, -1475.361036, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 32.36847973, 3.925e-05, 97.10543918, 0.00011775, 323.68479725, 0.0003925, -32.36847973, -3.925e-05, -97.10543918, -0.00011775, -323.68479725, -0.0003925, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 129.4739189, 0.01054277, 129.4739189, 0.0316283, 90.63174323, -1475.361036, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 32.36847973, 3.925e-05, 97.10543918, 0.00011775, 323.68479725, 0.0003925, -32.36847973, -3.925e-05, -97.10543918, -0.00011775, -323.68479725, -0.0003925, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 9.0, 0.0, 10.3)
    ops.node(124003, 9.0, 0.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.1225, 26277960.01272812, 10949150.00530338, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 63.56740668, 0.00051248, 77.7625852, 0.01968547, 7.77625852, 0.05242984, -63.56740668, -0.00051248, -77.7625852, -0.01968547, -7.77625852, -0.05242984, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 63.56740668, 0.00051248, 77.7625852, 0.01968547, 7.77625852, 0.05242984, -63.56740668, -0.00051248, -77.7625852, -0.01968547, -7.77625852, -0.05242984, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 118.40537802, 0.01024965, 118.40537802, 0.03074894, 82.88376461, -1512.93201064, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 29.60134451, 3.708e-05, 88.80403352, 0.00011123, 296.01344505, 0.00037077, -29.60134451, -3.708e-05, -88.80403352, -0.00011123, -296.01344505, -0.00037077, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 118.40537802, 0.01024965, 118.40537802, 0.03074894, 82.88376461, -1512.93201064, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 29.60134451, 3.708e-05, 88.80403352, 0.00011123, 296.01344505, 0.00037077, -29.60134451, -3.708e-05, -88.80403352, -0.00011123, -296.01344505, -0.00037077, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 8.95)
    ops.node(124032, 12.0, 0.0, 9.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.1225, 26868556.6169318, 11195231.92372158, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 68.25941918, 0.00052193, 83.21958247, 0.01856871, 8.32195825, 0.04934364, -68.25941918, -0.00052193, -83.21958247, -0.01856871, -8.32195825, -0.04934364, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 68.25941918, 0.00052193, 83.21958247, 0.01856871, 8.32195825, 0.04934364, -68.25941918, -0.00052193, -83.21958247, -0.01856871, -8.32195825, -0.04934364, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 127.94684562, 0.01043856, 127.94684562, 0.03131567, 89.56279194, -1474.34909224, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 31.98671141, 3.918e-05, 95.96013422, 0.00011755, 319.86711405, 0.00039184, -31.98671141, -3.918e-05, -95.96013422, -0.00011755, -319.86711405, -0.00039184, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 127.94684562, 0.01043856, 127.94684562, 0.03131567, 89.56279194, -1474.34909224, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 31.98671141, 3.918e-05, 95.96013422, 0.00011755, 319.86711405, 0.00039184, -31.98671141, -3.918e-05, -95.96013422, -0.00011755, -319.86711405, -0.00039184, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 12.0, 0.0, 10.3)
    ops.node(124004, 12.0, 0.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.1225, 26349437.50196258, 10978932.29248441, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 62.57742314, 0.00051846, 76.54278308, 0.01955658, 7.65427831, 0.05234084, -62.57742314, -0.00051846, -76.54278308, -0.01955658, -7.65427831, -0.05234084, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 62.57742314, 0.00051846, 76.54278308, 0.01955658, 7.65427831, 0.05234084, -62.57742314, -0.00051846, -76.54278308, -0.01955658, -7.65427831, -0.05234084, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 119.49269349, 0.01036913, 119.49269349, 0.03110739, 83.64488545, -1568.28060479, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 29.87317337, 3.732e-05, 89.61952012, 0.00011195, 298.73173373, 0.00037316, -29.87317337, -3.732e-05, -89.61952012, -0.00011195, -298.73173373, -0.00037316, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 119.49269349, 0.01036913, 119.49269349, 0.03110739, 83.64488545, -1568.28060479, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 29.87317337, 3.732e-05, 89.61952012, 0.00011195, 298.73173373, 0.00037316, -29.87317337, -3.732e-05, -89.61952012, -0.00011195, -298.73173373, -0.00037316, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
