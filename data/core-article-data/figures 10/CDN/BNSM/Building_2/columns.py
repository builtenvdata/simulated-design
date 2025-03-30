import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 26898838.63976858, 11207849.43323691, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 57.19641259, 0.00100734, 67.19946187, 0.01105522, 6.71994619, 0.02934019, -57.19641259, -0.00100734, -67.19946187, -0.01105522, -6.71994619, -0.02934019, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 54.60385258, 0.00100734, 64.15349045, 0.01105522, 6.41534905, 0.02934019, -54.60385258, -0.00100734, -64.15349045, -0.01105522, -6.41534905, -0.02934019, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 83.42081584, 0.02014674, 83.42081584, 0.06044022, 58.39457109, -1112.66541023, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 20.85520396, 0.00011075, 62.56561188, 0.00033226, 208.5520396, 0.00110753, -20.85520396, -0.00011075, -62.56561188, -0.00033226, -208.5520396, -0.00110753, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 83.42081584, 0.02014674, 83.42081584, 0.06044022, 58.39457109, -1112.66541023, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 20.85520396, 0.00011075, 62.56561188, 0.00033226, 208.5520396, 0.00110753, -20.85520396, -0.00011075, -62.56561188, -0.00033226, -208.5520396, -0.00110753, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.5, 0.0, 0.0)
    ops.node(121002, 4.5, 0.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.1225, 28784066.61961821, 11993361.09150759, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 131.01086066, 0.00069811, 155.44997731, 0.01118996, 15.54499773, 0.0329699, -131.01086066, -0.00069811, -155.44997731, -0.01118996, -15.54499773, -0.0329699, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 121.84151025, 0.00069811, 144.57015173, 0.01118996, 14.45701517, 0.0329699, -121.84151025, -0.00069811, -144.57015173, -0.01118996, -14.45701517, -0.0329699, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 147.82751075, 0.01396222, 147.82751075, 0.04188665, 103.47925752, -1673.51014487, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 36.95687769, 9.358e-05, 110.87063306, 0.00028073, 369.56877686, 0.00093575, -36.95687769, -9.358e-05, -110.87063306, -0.00028073, -369.56877686, -0.00093575, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 147.82751075, 0.01396222, 147.82751075, 0.04188665, 103.47925752, -1673.51014487, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 36.95687769, 9.358e-05, 110.87063306, 0.00028073, 369.56877686, 0.00093575, -36.95687769, -9.358e-05, -110.87063306, -0.00028073, -369.56877686, -0.00093575, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.5, 0.0, 0.0)
    ops.node(121005, 16.5, 0.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.1225, 27172996.85426216, 11322082.02260923, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 130.01540153, 0.00071246, 153.94490125, 0.01041335, 15.39449013, 0.02855174, -130.01540153, -0.00071246, -153.94490125, -0.01041335, -15.39449013, -0.02855174, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 120.94136604, 0.00071246, 143.20077801, 0.01041335, 14.3200778, 0.02855174, -120.94136604, -0.00071246, -143.20077801, -0.01041335, -14.3200778, -0.02855174, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 141.2074889, 0.0142493, 141.2074889, 0.0427479, 98.84524223, -1675.34733333, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 35.30187223, 9.468e-05, 105.90561668, 0.00028405, 353.01872225, 0.00094684, -35.30187223, -9.468e-05, -105.90561668, -0.00028405, -353.01872225, -0.00094684, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 141.2074889, 0.0142493, 141.2074889, 0.0427479, 98.84524223, -1675.34733333, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 35.30187223, 9.468e-05, 105.90561668, 0.00028405, 353.01872225, 0.00094684, -35.30187223, -9.468e-05, -105.90561668, -0.00028405, -353.01872225, -0.00094684, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 21.0, 0.0, 0.0)
    ops.node(121006, 21.0, 0.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.0625, 26857474.88709472, 11190614.53628947, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 57.48087731, 0.00096567, 67.52492527, 0.01092809, 6.75249253, 0.02909143, -57.48087731, -0.00096567, -67.52492527, -0.01092809, -6.75249253, -0.02909143, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 54.62565586, 0.00096567, 64.1707904, 0.01092809, 6.41707904, 0.02909143, -54.62565586, -0.00096567, -64.1707904, -0.01092809, -6.41707904, -0.02909143, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 83.23770142, 0.01931336, 83.23770142, 0.05794009, 58.266391, -1110.86288439, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 20.80942536, 0.00011068, 62.42827607, 0.00033204, 208.09425356, 0.0011068, -20.80942536, -0.00011068, -62.42827607, -0.00033204, -208.09425356, -0.0011068, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 83.23770142, 0.01931336, 83.23770142, 0.05794009, 58.266391, -1110.86288439, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 20.80942536, 0.00011068, 62.42827607, 0.00033204, 208.09425356, 0.0011068, -20.80942536, -0.00011068, -62.42827607, -0.00033204, -208.09425356, -0.0011068, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.5, 0.0)
    ops.node(121007, 0.0, 4.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 26748857.80889811, 11145357.42037421, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 130.41183442, 0.0007091, 154.22384009, 0.01013032, 15.42238401, 0.02711317, -130.41183442, -0.0007091, -154.22384009, -0.01013032, -15.42238401, -0.02711317, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 121.17766868, 0.0007091, 143.30360033, 0.01013032, 14.33036003, 0.02711317, -121.17766868, -0.0007091, -143.30360033, -0.01013032, -14.33036003, -0.02711317, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 139.41382956, 0.01418209, 139.41382956, 0.04254627, 97.58968069, -1677.11247551, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 34.85345739, 9.496e-05, 104.56037217, 0.00028489, 348.53457389, 0.00094964, -34.85345739, -9.496e-05, -104.56037217, -0.00028489, -348.53457389, -0.00094964, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 139.41382956, 0.01418209, 139.41382956, 0.04254627, 97.58968069, -1677.11247551, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 34.85345739, 9.496e-05, 104.56037217, 0.00028489, 348.53457389, 0.00094964, -34.85345739, -9.496e-05, -104.56037217, -0.00028489, -348.53457389, -0.00094964, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.5, 4.5, 0.0)
    ops.node(121008, 4.5, 4.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.16, 27545697.34016842, 11477373.89173684, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 194.35106969, 0.0006647, 229.95393033, 0.00993347, 22.99539303, 0.02648299, -194.35106969, -0.0006647, -229.95393033, -0.00993347, -22.99539303, -0.02648299, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 188.7775194, 0.0006647, 223.3593703, 0.00993347, 22.33593703, 0.02648299, -188.7775194, -0.0006647, -223.3593703, -0.00993347, -22.33593703, -0.02648299, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 182.86594078, 0.01329392, 182.86594078, 0.03988176, 128.00615855, -2139.60405317, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 45.7164852, 9.261e-05, 137.14945559, 0.00027783, 457.16485195, 0.00092609, -45.7164852, -9.261e-05, -137.14945559, -0.00027783, -457.16485195, -0.00092609, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 182.86594078, 0.01329392, 182.86594078, 0.03988176, 128.00615855, -2139.60405317, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 45.7164852, 9.261e-05, 137.14945559, 0.00027783, 457.16485195, 0.00092609, -45.7164852, -9.261e-05, -137.14945559, -0.00027783, -457.16485195, -0.00092609, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.0, 4.5, 0.0)
    ops.node(121009, 9.0, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 28030902.80612075, 11679542.83588365, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 178.92934006, 0.00063744, 212.67868795, 0.01069402, 21.26786879, 0.03035212, -178.92934006, -0.00063744, -212.67868795, -0.01069402, -21.26786879, -0.03035212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 173.471991, 0.00063744, 206.19198298, 0.01069402, 20.6191983, 0.03035212, -173.471991, -0.00063744, -206.19198298, -0.01069402, -20.6191983, -0.03035212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 179.27206665, 0.0127489, 179.27206665, 0.03824669, 125.49044665, -1977.41513678, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 44.81801666, 8.922e-05, 134.45404999, 0.00026765, 448.18016662, 0.00089217, -44.81801666, -8.922e-05, -134.45404999, -0.00026765, -448.18016662, -0.00089217, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 179.27206665, 0.0127489, 179.27206665, 0.03824669, 125.49044665, -1977.41513678, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 44.81801666, 8.922e-05, 134.45404999, 0.00026765, 448.18016662, 0.00089217, -44.81801666, -8.922e-05, -134.45404999, -0.00026765, -448.18016662, -0.00089217, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.0, 4.5, 0.0)
    ops.node(121010, 12.0, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 27678741.63037581, 11532809.01265659, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 178.47011323, 0.00064286, 212.05133565, 0.01081778, 21.20513356, 0.0297529, -178.47011323, -0.00064286, -212.05133565, -0.01081778, -21.20513356, -0.0297529, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 173.0946565, 0.00064286, 205.66442437, 0.01081778, 20.56644244, 0.0297529, -173.0946565, -0.00064286, -205.66442437, -0.01081778, -20.56644244, -0.0297529, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 178.30604765, 0.01285716, 178.30604765, 0.03857147, 124.81423335, -1994.44021202, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 44.57651191, 8.987e-05, 133.72953573, 0.0002696, 445.76511912, 0.00089866, -44.57651191, -8.987e-05, -133.72953573, -0.0002696, -445.76511912, -0.00089866, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 178.30604765, 0.01285716, 178.30604765, 0.03857147, 124.81423335, -1994.44021202, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 44.57651191, 8.987e-05, 133.72953573, 0.0002696, 445.76511912, 0.00089866, -44.57651191, -8.987e-05, -133.72953573, -0.0002696, -445.76511912, -0.00089866, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 16.5, 4.5, 0.0)
    ops.node(121011, 16.5, 4.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 26799254.62172442, 11166356.09238518, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 193.24826162, 0.00065879, 228.2816438, 0.00949748, 22.82816438, 0.02447225, -193.24826162, -0.00065879, -228.2816438, -0.00949748, -22.82816438, -0.02447225, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 187.56148779, 0.00065879, 221.56393226, 0.00949748, 22.15639323, 0.02447225, -187.56148779, -0.00065879, -221.56393226, -0.00949748, -22.15639323, -0.02447225, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 178.32370427, 0.01317589, 178.32370427, 0.03952768, 124.82659299, -2130.93668376, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 44.58092607, 9.282e-05, 133.7427782, 0.00027847, 445.80926067, 0.00092824, -44.58092607, -9.282e-05, -133.7427782, -0.00027847, -445.80926067, -0.00092824, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 178.32370427, 0.01317589, 178.32370427, 0.03952768, 124.82659299, -2130.93668376, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 44.58092607, 9.282e-05, 133.7427782, 0.00027847, 445.80926067, 0.00092824, -44.58092607, -9.282e-05, -133.7427782, -0.00027847, -445.80926067, -0.00092824, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 21.0, 4.5, 0.0)
    ops.node(121012, 21.0, 4.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 29006268.07102041, 12085945.02959184, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 132.2414426, 0.0007159, 156.89321685, 0.01136772, 15.68932168, 0.03346953, -132.2414426, -0.0007159, -156.89321685, -0.01136772, -15.68932168, -0.03346953, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 123.32186775, 0.0007159, 146.31090041, 0.01136772, 14.63109004, 0.03346953, -123.32186775, -0.0007159, -146.31090041, -0.01136772, -14.63109004, -0.03346953, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 150.28868457, 0.01431802, 150.28868457, 0.04295405, 105.2020792, -1704.30964426, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 37.57217114, 9.44e-05, 112.71651343, 0.00028321, 375.72171143, 0.00094404, -37.57217114, -9.44e-05, -112.71651343, -0.00028321, -375.72171143, -0.00094404, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 150.28868457, 0.01431802, 150.28868457, 0.04295405, 105.2020792, -1704.30964426, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 37.57217114, 9.44e-05, 112.71651343, 0.00028321, 375.72171143, 0.00094404, -37.57217114, -9.44e-05, -112.71651343, -0.00028321, -375.72171143, -0.00094404, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.1225, 27654151.24692437, 11522563.01955182, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 131.28691836, 0.00070211, 155.53821174, 0.01068428, 15.55382117, 0.02977308, -131.28691836, -0.00070211, -155.53821174, -0.01068428, -15.55382117, -0.02977308, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 121.93025703, 0.00070211, 144.45318979, 0.01068428, 14.44531898, 0.02977308, -121.93025703, -0.00070211, -144.45318979, -0.01068428, -14.44531898, -0.02977308, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 143.12025543, 0.01404216, 143.12025543, 0.04212648, 100.1841788, -1676.34385337, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 35.78006386, 9.43e-05, 107.34019157, 0.00028289, 357.80063858, 0.00094297, -35.78006386, -9.43e-05, -107.34019157, -0.00028289, -357.80063858, -0.00094297, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 143.12025543, 0.01404216, 143.12025543, 0.04212648, 100.1841788, -1676.34385337, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 35.78006386, 9.43e-05, 107.34019157, 0.00028289, 357.80063858, 0.00094297, -35.78006386, -9.43e-05, -107.34019157, -0.00028289, -357.80063858, -0.00094297, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.5, 9.0, 0.0)
    ops.node(121014, 4.5, 9.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.16, 28360291.59943594, 11816788.16643164, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 193.22167565, 0.00064449, 228.89273902, 0.01051264, 22.8892739, 0.02873925, -193.22167565, -0.00064449, -228.89273902, -0.01051264, -22.8892739, -0.02873925, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 187.67790755, 0.00064449, 222.32552414, 0.01051264, 22.23255241, 0.02873925, -187.67790755, -0.00064449, -222.32552414, -0.01051264, -22.23255241, -0.02873925, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 188.05660163, 0.01288973, 188.05660163, 0.03866918, 131.63962114, -2152.60896991, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 47.01415041, 9.25e-05, 141.04245122, 0.00027751, 470.14150408, 0.00092502, -47.01415041, -9.25e-05, -141.04245122, -0.00027751, -470.14150408, -0.00092502, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 188.05660163, 0.01288973, 188.05660163, 0.03866918, 131.63962114, -2152.60896991, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 47.01415041, 9.25e-05, 141.04245122, 0.00027751, 470.14150408, 0.00092502, -47.01415041, -9.25e-05, -141.04245122, -0.00027751, -470.14150408, -0.00092502, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 9.0, 0.0)
    ops.node(121015, 9.0, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.16, 27688561.04495154, 11536900.43539647, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 178.39805257, 0.0006441, 211.94970269, 0.01074045, 21.19497027, 0.02964649, -178.39805257, -0.0006441, -211.94970269, -0.01074045, -21.19497027, -0.02964649, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 173.09864756, 0.0006441, 205.65362882, 0.01074045, 20.56536288, 0.02964649, -173.09864756, -0.0006441, -205.65362882, -0.01074045, -20.56536288, -0.02964649, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 179.02322909, 0.01288209, 179.02322909, 0.03864627, 125.31626037, -2007.74342942, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 44.75580727, 9.02e-05, 134.26742182, 0.00027059, 447.55807274, 0.00090195, -44.75580727, -9.02e-05, -134.26742182, -0.00027059, -447.55807274, -0.00090195, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 179.02322909, 0.01288209, 179.02322909, 0.03864627, 125.31626037, -2007.74342942, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 44.75580727, 9.02e-05, 134.26742182, 0.00027059, 447.55807274, 0.00090195, -44.75580727, -9.02e-05, -134.26742182, -0.00027059, -447.55807274, -0.00090195, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.0, 9.0, 0.0)
    ops.node(121016, 12.0, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.16, 27642650.27425501, 11517770.94760625, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 177.97564611, 0.00063751, 211.43574402, 0.01061515, 21.1435744, 0.02942604, -177.97564611, -0.00063751, -211.43574402, -0.01061515, -21.1435744, -0.02942604, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 172.62551109, 0.00063751, 205.07976328, 0.01061515, 20.50797633, 0.02942604, -172.62551109, -0.00063751, -205.07976328, -0.01061515, -20.50797633, -0.02942604, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 177.78330603, 0.01275018, 177.78330603, 0.03825055, 124.44831422, -1989.27804605, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 44.44582651, 8.972e-05, 133.33747952, 0.00026916, 444.45826506, 0.00089719, -44.44582651, -8.972e-05, -133.33747952, -0.00026916, -444.45826506, -0.00089719, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 177.78330603, 0.01275018, 177.78330603, 0.03825055, 124.44831422, -1989.27804605, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 44.44582651, 8.972e-05, 133.33747952, 0.00026916, 444.45826506, 0.00089719, -44.44582651, -8.972e-05, -133.33747952, -0.00026916, -444.45826506, -0.00089719, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 16.5, 9.0, 0.0)
    ops.node(121017, 16.5, 9.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.16, 26526745.26979208, 11052810.52908003, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 194.13126129, 0.00065643, 229.15998322, 0.00956159, 22.91599832, 0.02395496, -194.13126129, -0.00065643, -229.15998322, -0.00956159, -22.91599832, -0.02395496, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 188.20016105, 0.00065643, 222.15868512, 0.00956159, 22.21586851, 0.02395496, -188.20016105, -0.00065643, -222.15868512, -0.00956159, -22.21586851, -0.02395496, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 177.88639022, 0.01312852, 177.88639022, 0.03938557, 124.52047316, -2149.71326089, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 44.47159756, 9.355e-05, 133.41479267, 0.00028064, 444.71597556, 0.00093548, -44.47159756, -9.355e-05, -133.41479267, -0.00028064, -444.71597556, -0.00093548, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 177.88639022, 0.01312852, 177.88639022, 0.03938557, 124.52047316, -2149.71326089, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 44.47159756, 9.355e-05, 133.41479267, 0.00028064, 444.71597556, 0.00093548, -44.47159756, -9.355e-05, -133.41479267, -0.00028064, -444.71597556, -0.00093548, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.1225, 27116138.99827383, 11298391.24928076, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 130.1586019, 0.00073773, 154.05034684, 0.01047016, 15.40503468, 0.02831426, -130.1586019, -0.00073773, -154.05034684, -0.01047016, -15.40503468, -0.02831426, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 121.75106775, 0.00073773, 144.09953657, 0.01047016, 14.40995366, 0.02831426, -121.75106775, -0.00073773, -144.09953657, -0.01047016, -14.40995366, -0.02831426, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 142.0830198, 0.01475451, 142.0830198, 0.04426354, 99.45811386, -1698.6459091, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 35.52075495, 9.547e-05, 106.56226485, 0.00028641, 355.20754951, 0.00095471, -35.52075495, -9.547e-05, -106.56226485, -0.00028641, -355.20754951, -0.00095471, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 142.0830198, 0.01475451, 142.0830198, 0.04426354, 99.45811386, -1698.6459091, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 35.52075495, 9.547e-05, 106.56226485, 0.00028641, 355.20754951, 0.00095471, -35.52075495, -9.547e-05, -106.56226485, -0.00028641, -355.20754951, -0.00095471, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.0625, 27273317.43466929, 11363882.26444554, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 58.14206193, 0.00097275, 68.38509685, 0.01101196, 6.83850968, 0.03039759, -58.14206193, -0.00097275, -68.38509685, -0.01101196, -6.83850968, -0.03039759, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 55.22257711, 0.00097275, 64.95127896, 0.01101196, 6.4951279, 0.03039759, -55.22257711, -0.00097275, -64.95127896, -0.01101196, -6.4951279, -0.03039759, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 82.84070065, 0.01945504, 82.84070065, 0.05836512, 57.98849045, -1085.55050022, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 20.71017516, 0.00010847, 62.13052549, 0.00032542, 207.10175162, 0.00108473, -20.71017516, -0.00010847, -62.13052549, -0.00032542, -207.10175162, -0.00108473, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 82.84070065, 0.01945504, 82.84070065, 0.05836512, 57.98849045, -1085.55050022, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 20.71017516, 0.00010847, 62.13052549, 0.00032542, 207.10175162, 0.00108473, -20.71017516, -0.00010847, -62.13052549, -0.00032542, -207.10175162, -0.00108473, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 4.5, 13.5, 0.0)
    ops.node(121020, 4.5, 13.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.1225, 28008675.97558397, 11670281.65649332, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 131.18379448, 0.0007193, 155.53795887, 0.01097196, 15.55379589, 0.03102972, -131.18379448, -0.0007193, -155.53795887, -0.01097196, -15.55379589, -0.03102972, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 122.15620359, 0.0007193, 144.8344031, 0.01097196, 14.48344031, 0.03102972, -122.15620359, -0.0007193, -144.8344031, -0.01097196, -14.48344031, -0.03102972, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 145.22511285, 0.01438595, 145.22511285, 0.04315786, 101.65757899, -1685.60945781, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 36.30627821, 9.447e-05, 108.91883464, 0.00028342, 363.06278212, 0.00094473, -36.30627821, -9.447e-05, -108.91883464, -0.00028342, -363.06278212, -0.00094473, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 145.22511285, 0.01438595, 145.22511285, 0.04315786, 101.65757899, -1685.60945781, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 36.30627821, 9.447e-05, 108.91883464, 0.00028342, 363.06278212, 0.00094473, -36.30627821, -9.447e-05, -108.91883464, -0.00028342, -363.06278212, -0.00094473, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 9.0, 13.5, 0.0)
    ops.node(121021, 9.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.09, 28630757.80382459, 11929482.41826025, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 99.19724654, 0.0008328, 117.04652021, 0.01091511, 11.70465202, 0.03136924, -99.19724654, -0.0008328, -117.04652021, -0.01091511, -11.70465202, -0.03136924, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 91.75395647, 0.0008328, 108.26390545, 0.01091511, 10.82639054, 0.03136924, -91.75395647, -0.0008328, -108.26390545, -0.01091511, -10.82639054, -0.03136924, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 116.9955151, 0.01665594, 116.9955151, 0.04996781, 81.89686057, -1435.40380201, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 29.24887877, 0.00010134, 87.74663632, 0.00030403, 292.48878775, 0.00101342, -29.24887877, -0.00010134, -87.74663632, -0.00030403, -292.48878775, -0.00101342, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 116.9955151, 0.01665594, 116.9955151, 0.04996781, 81.89686057, -1435.40380201, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 29.24887877, 0.00010134, 87.74663632, 0.00030403, 292.48878775, 0.00101342, -29.24887877, -0.00010134, -87.74663632, -0.00030403, -292.48878775, -0.00101342, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 12.0, 13.5, 0.0)
    ops.node(121022, 12.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.09, 27564980.97164528, 11485408.73818554, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 99.90598041, 0.00082493, 117.64485853, 0.01046726, 11.76448585, 0.02823886, -99.90598041, -0.00082493, -117.64485853, -0.01046726, -11.76448585, -0.02823886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 91.81686761, 0.00082493, 108.1194775, 0.01046726, 10.81194775, 0.02823886, -91.81686761, -0.00082493, -108.1194775, -0.01046726, -10.81194775, -0.02823886, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 114.64651687, 0.01649862, 114.64651687, 0.04949586, 80.25256181, -1454.77927356, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 28.66162922, 0.00010315, 85.98488766, 0.00030944, 286.61629218, 0.00103147, -28.66162922, -0.00010315, -85.98488766, -0.00030944, -286.61629218, -0.00103147, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 114.64651687, 0.01649862, 114.64651687, 0.04949586, 80.25256181, -1454.77927356, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 28.66162922, 0.00010315, 85.98488766, 0.00030944, 286.61629218, 0.00103147, -28.66162922, -0.00010315, -85.98488766, -0.00030944, -286.61629218, -0.00103147, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 16.5, 13.5, 0.0)
    ops.node(121023, 16.5, 13.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.1225, 27638218.3159765, 11515924.29832354, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 130.40276021, 0.00070297, 154.53066796, 0.01092326, 15.4530668, 0.03013747, -130.40276021, -0.00070297, -154.53066796, -0.01092326, -15.4530668, -0.03013747, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 121.15721353, 0.00070297, 143.57445429, 0.01092326, 14.35744543, 0.03013747, -121.15721353, -0.00070297, -143.57445429, -0.01092326, -14.35744543, -0.03013747, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 144.12454653, 0.01405949, 144.12454653, 0.04217847, 100.88718257, -1693.89067719, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 36.03113663, 9.501e-05, 108.0934099, 0.00028504, 360.31136632, 0.00095014, -36.03113663, -9.501e-05, -108.0934099, -0.00028504, -360.31136632, -0.00095014, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 144.12454653, 0.01405949, 144.12454653, 0.04217847, 100.88718257, -1693.89067719, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 36.03113663, 9.501e-05, 108.0934099, 0.00028504, 360.31136632, 0.00095014, -36.03113663, -9.501e-05, -108.0934099, -0.00028504, -360.31136632, -0.00095014, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.0625, 26626109.20095151, 11094212.16706313, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 57.64139893, 0.00098486, 67.66211562, 0.01089405, 6.76621156, 0.0283772, -57.64139893, -0.00098486, -67.66211562, -0.01089405, -6.76621156, -0.0283772, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 54.81254872, 0.00098486, 64.34148161, 0.01089405, 6.43414816, 0.0283772, -54.81254872, -0.00098486, -64.34148161, -0.01089405, -6.43414816, -0.0283772, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 82.75582207, 0.01969729, 82.75582207, 0.05909186, 57.92907545, -1111.32311127, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 20.68895552, 0.000111, 62.06686655, 0.00033299, 206.88955517, 0.00110995, -20.68895552, -0.000111, -62.06686655, -0.00033299, -206.88955517, -0.00110995, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 82.75582207, 0.01969729, 82.75582207, 0.05909186, 57.92907545, -1111.32311127, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 20.68895552, 0.000111, 62.06686655, 0.00033299, 206.88955517, 0.00110995, -20.68895552, -0.000111, -62.06686655, -0.00033299, -206.88955517, -0.00110995, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.325)
    ops.node(122001, 0.0, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 27953853.68422607, 11647439.0350942, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 48.49565672, 0.00084676, 57.71186391, 0.01346319, 5.77118639, 0.04234608, -48.49565672, -0.00084676, -57.71186391, -0.01346319, -5.77118639, -0.04234608, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 45.79842508, 0.00084676, 54.50204523, 0.01346319, 5.45020452, 0.04234608, -45.79842508, -0.00084676, -54.50204523, -0.01346319, -5.45020452, -0.04234608, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 79.24379822, 0.01693517, 79.24379822, 0.05080551, 55.47065875, -1056.28201061, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 19.81094956, 9.144e-05, 59.43284867, 0.00027432, 198.10949555, 0.0009144, -19.81094956, -9.144e-05, -59.43284867, -0.00027432, -198.10949555, -0.0009144, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 79.24379822, 0.01693517, 79.24379822, 0.05080551, 55.47065875, -1056.28201061, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 19.81094956, 9.144e-05, 59.43284867, 0.00027432, 198.10949555, 0.0009144, -19.81094956, -9.144e-05, -59.43284867, -0.00027432, -198.10949555, -0.0009144, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.5, 0.0, 3.325)
    ops.node(122002, 4.5, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.1225, 28628744.68578647, 11928643.6190777, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 107.24384459, 0.00064952, 128.20242042, 0.01229609, 12.82024204, 0.03916851, -107.24384459, -0.00064952, -128.20242042, -0.01229609, -12.82024204, -0.03916851, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 99.54326219, 0.00064952, 118.99691957, 0.01229609, 11.89969196, 0.03916851, -99.54326219, -0.00064952, -118.99691957, -0.01229609, -11.89969196, -0.03916851, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 136.21873186, 0.01299044, 136.21873186, 0.03897132, 95.3531123, -1565.40739258, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 34.05468297, 7.83e-05, 102.1640489, 0.00023491, 340.54682966, 0.00078305, -34.05468297, -7.83e-05, -102.1640489, -0.00023491, -340.54682966, -0.00078305, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 136.21873186, 0.01299044, 136.21873186, 0.03897132, 95.3531123, -1565.40739258, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 34.05468297, 7.83e-05, 102.1640489, 0.00023491, 340.54682966, 0.00078305, -34.05468297, -7.83e-05, -102.1640489, -0.00023491, -340.54682966, -0.00078305, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.5, 0.0, 3.325)
    ops.node(122005, 16.5, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.1225, 27044049.02779739, 11268353.76158225, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 108.63538285, 0.00064231, 129.77956155, 0.01192123, 12.97795616, 0.03535882, -108.63538285, -0.00064231, -129.77956155, -0.01192123, -12.97795616, -0.03535882, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 99.89560106, 0.00064231, 119.33871789, 0.01192123, 11.93387179, 0.03535882, -99.89560106, -0.00064231, -119.33871789, -0.01192123, -11.93387179, -0.03535882, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 130.63116372, 0.0128462, 130.63116372, 0.03853859, 91.44181461, -1580.01072759, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 32.65779093, 7.949e-05, 97.97337279, 0.00023848, 326.57790931, 0.00079493, -32.65779093, -7.949e-05, -97.97337279, -0.00023848, -326.57790931, -0.00079493, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 130.63116372, 0.0128462, 130.63116372, 0.03853859, 91.44181461, -1580.01072759, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 32.65779093, 7.949e-05, 97.97337279, 0.00023848, 326.57790931, 0.00079493, -32.65779093, -7.949e-05, -97.97337279, -0.00023848, -326.57790931, -0.00079493, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 21.0, 0.0, 3.325)
    ops.node(122006, 21.0, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.0625, 25512085.31116219, 10630035.54631758, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 47.74985265, 0.00086964, 56.56688454, 0.01167615, 5.65668845, 0.03308567, -47.74985265, -0.00086964, -56.56688454, -0.01167615, -5.65668845, -0.03308567, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 45.09612898, 0.00086964, 53.42314959, 0.01167615, 5.34231496, 0.03308567, -45.09612898, -0.00086964, -53.42314959, -0.01167615, -5.34231496, -0.03308567, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 73.57704066, 0.01739275, 73.57704066, 0.05217826, 51.50392847, -1040.60758644, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 18.39426017, 9.303e-05, 55.1827805, 0.00027908, 183.94260166, 0.00093027, -18.39426017, -9.303e-05, -55.1827805, -0.00027908, -183.94260166, -0.00093027, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 73.57704066, 0.01739275, 73.57704066, 0.05217826, 51.50392847, -1040.60758644, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 18.39426017, 9.303e-05, 55.1827805, 0.00027908, 183.94260166, 0.00093027, -18.39426017, -9.303e-05, -55.1827805, -0.00027908, -183.94260166, -0.00093027, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.325)
    ops.node(122007, 0.0, 4.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 27033776.53268033, 11264073.55528347, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 107.68090386, 0.00064941, 128.6127698, 0.01207023, 12.86127698, 0.03534764, -107.68090386, -0.00064941, -128.6127698, -0.01207023, -12.86127698, -0.03534764, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 99.54015882, 0.00064941, 118.88956234, 0.01207023, 11.88895623, 0.03534764, -99.54015882, -0.00064941, -118.88956234, -0.01207023, -11.88895623, -0.03534764, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 131.19551853, 0.01298825, 131.19551853, 0.03896476, 91.83686297, -1594.05479541, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 32.79887963, 7.987e-05, 98.3966389, 0.0002396, 327.98879632, 0.00079867, -32.79887963, -7.987e-05, -98.3966389, -0.0002396, -327.98879632, -0.00079867, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 131.19551853, 0.01298825, 131.19551853, 0.03896476, 91.83686297, -1594.05479541, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 32.79887963, 7.987e-05, 98.3966389, 0.0002396, 327.98879632, 0.00079867, -32.79887963, -7.987e-05, -98.3966389, -0.0002396, -327.98879632, -0.00079867, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.5, 4.5, 3.325)
    ops.node(122008, 4.5, 4.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.16, 28079293.07419134, 11699705.44757972, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 161.97833758, 0.00059397, 193.31820009, 0.01147734, 19.33182001, 0.03376084, -161.97833758, -0.00059397, -193.31820009, -0.01147734, -19.33182001, -0.03376084, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 156.8006005, 0.00059397, 187.13866504, 0.01147734, 18.7138665, 0.03376084, -156.8006005, -0.00059397, -187.13866504, -0.01147734, -18.7138665, -0.03376084, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 172.3461334, 0.01187939, 172.3461334, 0.03563816, 120.64229338, -1996.64439838, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 43.08653335, 7.734e-05, 129.25960005, 0.00023201, 430.8653335, 0.00077337, -43.08653335, -7.734e-05, -129.25960005, -0.00023201, -430.8653335, -0.00077337, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 172.3461334, 0.01187939, 172.3461334, 0.03563816, 120.64229338, -1996.64439838, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 43.08653335, 7.734e-05, 129.25960005, 0.00023201, 430.8653335, 0.00077337, -43.08653335, -7.734e-05, -129.25960005, -0.00023201, -430.8653335, -0.00077337, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.0, 4.5, 3.35)
    ops.node(122009, 9.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 27565033.30054616, 11485430.54189423, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 148.31204295, 0.00058736, 177.51783564, 0.01207701, 17.75178356, 0.03545373, -148.31204295, -0.00058736, -177.51783564, -0.01207701, -17.75178356, -0.03545373, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 143.44296274, 0.00058736, 171.68993007, 0.01207701, 17.16899301, 0.03545373, -143.44296274, -0.00058736, -171.68993007, -0.01207701, -17.16899301, -0.03545373, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 165.4005822, 0.01174713, 165.4005822, 0.03524139, 115.78040754, -1883.73233092, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 41.35014555, 7.56e-05, 124.05043665, 0.00022681, 413.50145551, 0.00075605, -41.35014555, -7.56e-05, -124.05043665, -0.00022681, -413.50145551, -0.00075605, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 165.4005822, 0.01174713, 165.4005822, 0.03524139, 115.78040754, -1883.73233092, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 41.35014555, 7.56e-05, 124.05043665, 0.00022681, 413.50145551, 0.00075605, -41.35014555, -7.56e-05, -124.05043665, -0.00022681, -413.50145551, -0.00075605, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.0, 4.5, 3.35)
    ops.node(122010, 12.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 28782150.37533155, 11992562.65638815, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 150.26823728, 0.00058446, 179.8663461, 0.01198898, 17.98663461, 0.03765763, -150.26823728, -0.00058446, -179.8663461, -0.01198898, -17.98663461, -0.03765763, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 145.25416981, 0.00058446, 173.86466529, 0.01198898, 17.38646653, 0.03765763, -145.25416981, -0.00058446, -173.86466529, -0.01198898, -17.38646653, -0.03765763, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 170.42317633, 0.01168921, 170.42317633, 0.03506764, 119.29622343, -1857.30786982, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 42.60579408, 7.461e-05, 127.81738225, 0.00022382, 426.05794082, 0.00074606, -42.60579408, -7.461e-05, -127.81738225, -0.00022382, -426.05794082, -0.00074606, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 170.42317633, 0.01168921, 170.42317633, 0.03506764, 119.29622343, -1857.30786982, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 42.60579408, 7.461e-05, 127.81738225, 0.00022382, 426.05794082, 0.00074606, -42.60579408, -7.461e-05, -127.81738225, -0.00022382, -426.05794082, -0.00074606, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 16.5, 4.5, 3.325)
    ops.node(122011, 16.5, 4.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 26792909.71738459, 11163712.38224358, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 161.78447403, 0.00060025, 192.86459935, 0.01108086, 19.28645993, 0.03072472, -161.78447403, -0.00060025, -192.86459935, -0.01108086, -19.28645993, -0.03072472, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 156.49408893, 0.00060025, 186.55788784, 0.01108086, 18.65578878, 0.03072472, -156.49408893, -0.00060025, -186.55788784, -0.01108086, -18.65578878, -0.03072472, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 166.15750749, 0.01200505, 166.15750749, 0.03601514, 116.31025524, -2006.61904844, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 41.53937687, 7.814e-05, 124.61813062, 0.00023442, 415.39376872, 0.0007814, -41.53937687, -7.814e-05, -124.61813062, -0.00023442, -415.39376872, -0.0007814, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 166.15750749, 0.01200505, 166.15750749, 0.03601514, 116.31025524, -2006.61904844, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 41.53937687, 7.814e-05, 124.61813062, 0.00023442, 415.39376872, 0.0007814, -41.53937687, -7.814e-05, -124.61813062, -0.00023442, -415.39376872, -0.0007814, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.325)
    ops.node(122012, 21.0, 4.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 28856030.86104837, 12023346.19210349, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 109.19069659, 0.00063878, 130.50454196, 0.01235072, 13.0504542, 0.03955596, -109.19069659, -0.00063878, -130.50454196, -0.01235072, -13.0504542, -0.03955596, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 100.80206935, 0.00063878, 120.4784684, 0.01235072, 12.04784684, 0.03955596, -100.80206935, -0.00063878, -120.4784684, -0.01235072, -12.04784684, -0.03955596, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 137.57020813, 0.01277563, 137.57020813, 0.0383269, 96.29914569, -1575.70797238, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 34.39255203, 7.846e-05, 103.1776561, 0.00023538, 343.92552032, 0.00078459, -34.39255203, -7.846e-05, -103.1776561, -0.00023538, -343.92552032, -0.00078459, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 137.57020813, 0.01277563, 137.57020813, 0.0383269, 96.29914569, -1575.70797238, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 34.39255203, 7.846e-05, 103.1776561, 0.00023538, 343.92552032, 0.00078459, -34.39255203, -7.846e-05, -103.1776561, -0.00023538, -343.92552032, -0.00078459, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.325)
    ops.node(122013, 0.0, 9.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.1225, 27955671.33781418, 11648196.39075591, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 108.77585544, 0.00064048, 130.00037778, 0.01242286, 13.00003778, 0.0377497, -108.77585544, -0.00064048, -130.00037778, -0.01242286, -13.00003778, -0.0377497, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 100.32855853, 0.00064048, 119.90483052, 0.01242286, 11.99048305, 0.0377497, -100.32855853, -0.00064048, -119.90483052, -0.01242286, -11.99048305, -0.0377497, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 134.78689274, 0.01280969, 134.78689274, 0.03842908, 94.35082492, -1593.37766357, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 33.69672318, 7.935e-05, 101.09016955, 0.00023804, 336.96723185, 0.00079347, -33.69672318, -7.935e-05, -101.09016955, -0.00023804, -336.96723185, -0.00079347, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 134.78689274, 0.01280969, 134.78689274, 0.03842908, 94.35082492, -1593.37766357, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 33.69672318, 7.935e-05, 101.09016955, 0.00023804, 336.96723185, 0.00079347, -33.69672318, -7.935e-05, -101.09016955, -0.00023804, -336.96723185, -0.00079347, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.5, 9.0, 3.325)
    ops.node(122014, 4.5, 9.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.16, 29008495.31189958, 12086873.04662483, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 163.06114621, 0.00059053, 194.63633108, 0.0115591, 19.46363311, 0.03561741, -163.06114621, -0.00059053, -194.63633108, -0.0115591, -19.46363311, -0.03561741, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 157.82848149, 0.00059053, 188.39041238, 0.0115591, 18.83904124, 0.03561741, -157.82848149, -0.00059053, -188.39041238, -0.0115591, -18.83904124, -0.03561741, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 177.34885568, 0.01181065, 177.34885568, 0.03543195, 124.14419898, -1999.12010286, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 44.33721392, 7.703e-05, 133.01164176, 0.0002311, 443.37213921, 0.00077032, -44.33721392, -7.703e-05, -133.01164176, -0.0002311, -443.37213921, -0.00077032, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 177.34885568, 0.01181065, 177.34885568, 0.03543195, 124.14419898, -1999.12010286, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 44.33721392, 7.703e-05, 133.01164176, 0.0002311, 443.37213921, 0.00077032, -44.33721392, -7.703e-05, -133.01164176, -0.0002311, -443.37213921, -0.00077032, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 9.0, 3.35)
    ops.node(122015, 9.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.16, 29029273.30150197, 12095530.54229249, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 151.58463916, 0.0005779, 181.39435137, 0.01220823, 18.13943514, 0.03818852, -151.58463916, -0.0005779, -181.39435137, -0.01220823, -18.13943514, -0.03818852, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 146.40065123, 0.0005779, 175.19091194, 0.01220823, 17.51909119, 0.03818852, -146.40065123, -0.0005779, -175.19091194, -0.01220823, -17.51909119, -0.03818852, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 173.22221917, 0.01155806, 173.22221917, 0.03467418, 121.25555342, -1891.06870243, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 43.30555479, 7.519e-05, 129.91666438, 0.00022556, 433.05554793, 0.00075186, -43.30555479, -7.519e-05, -129.91666438, -0.00022556, -433.05554793, -0.00075186, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 173.22221917, 0.01155806, 173.22221917, 0.03467418, 121.25555342, -1891.06870243, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 43.30555479, 7.519e-05, 129.91666438, 0.00022556, 433.05554793, 0.00075186, -43.30555479, -7.519e-05, -129.91666438, -0.00022556, -433.05554793, -0.00075186, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.0, 9.0, 3.35)
    ops.node(122016, 12.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.16, 27433761.60272768, 11430734.00113653, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 150.53336279, 0.00058261, 180.13014865, 0.01157694, 18.01301486, 0.03455747, -150.53336279, -0.00058261, -180.13014865, -0.01157694, -18.01301486, -0.03455747, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 145.32166772, 0.00058261, 173.89376763, 0.01157694, 17.38937676, 0.03455747, -145.32166772, -0.00058261, -173.89376763, -0.01157694, -17.38937676, -0.03455747, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 163.78715223, 0.01165229, 163.78715223, 0.03495686, 114.65100656, -1864.15198819, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 40.94678806, 7.523e-05, 122.84036418, 0.00022568, 409.46788059, 0.00075225, -40.94678806, -7.523e-05, -122.84036418, -0.00022568, -409.46788059, -0.00075225, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 163.78715223, 0.01165229, 163.78715223, 0.03495686, 114.65100656, -1864.15198819, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 40.94678806, 7.523e-05, 122.84036418, 0.00022568, 409.46788059, 0.00075225, -40.94678806, -7.523e-05, -122.84036418, -0.00022568, -409.46788059, -0.00075225, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 16.5, 9.0, 3.325)
    ops.node(122017, 16.5, 9.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.16, 27768722.92370315, 11570301.21820965, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 162.73719968, 0.0005876, 194.19086368, 0.01146062, 19.41908637, 0.0331257, -162.73719968, -0.0005876, -194.19086368, -0.01146062, -19.41908637, -0.0331257, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 157.27822502, 0.0005876, 187.67678449, 0.01146062, 18.76767845, 0.0331257, -157.27822502, -0.0005876, -187.67678449, -0.01146062, -18.76767845, -0.0331257, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 171.85326783, 0.01175208, 171.85326783, 0.03525623, 120.29728748, -2020.44587383, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 42.96331696, 7.798e-05, 128.88995087, 0.00023393, 429.63316956, 0.00077978, -42.96331696, -7.798e-05, -128.88995087, -0.00023393, -429.63316956, -0.00077978, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 171.85326783, 0.01175208, 171.85326783, 0.03525623, 120.29728748, -2020.44587383, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 42.96331696, 7.798e-05, 128.88995087, 0.00023393, 429.63316956, 0.00077978, -42.96331696, -7.798e-05, -128.88995087, -0.00023393, -429.63316956, -0.00077978, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.325)
    ops.node(122018, 21.0, 9.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.1225, 26302450.73382991, 10959354.47242913, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 107.31045276, 0.00064658, 128.05183033, 0.01159143, 12.80518303, 0.03315714, -107.31045276, -0.00064658, -128.05183033, -0.01159143, -12.80518303, -0.03315714, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 99.02686659, 0.00064658, 118.16716072, 0.01159143, 11.81671607, 0.03315714, -99.02686659, -0.00064658, -118.16716072, -0.01159143, -11.81671607, -0.03315714, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 128.13271363, 0.01293162, 128.13271363, 0.03879485, 89.69289954, -1589.11707493, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 32.03317841, 8.017e-05, 96.09953522, 0.00024051, 320.33178407, 0.00080171, -32.03317841, -8.017e-05, -96.09953522, -0.00024051, -320.33178407, -0.00080171, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 128.13271363, 0.01293162, 128.13271363, 0.03879485, 89.69289954, -1589.11707493, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 32.03317841, 8.017e-05, 96.09953522, 0.00024051, 320.33178407, 0.00080171, -32.03317841, -8.017e-05, -96.09953522, -0.00024051, -320.33178407, -0.00080171, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.325)
    ops.node(122019, 0.0, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.0625, 27163065.73200557, 11317944.05500232, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 47.52377703, 0.00086442, 56.5033292, 0.0130435, 5.65033292, 0.0395892, -47.52377703, -0.00086442, -56.5033292, -0.0130435, -5.65033292, -0.0395892, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 45.05554331, 0.00086442, 53.56872611, 0.0130435, 5.35687261, 0.0395892, -45.05554331, -0.00086442, -53.56872611, -0.0130435, -5.35687261, -0.0395892, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 77.67024046, 0.0172884, 77.67024046, 0.05186521, 54.36916832, -1057.67010387, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 19.41756012, 9.223e-05, 58.25268035, 0.0002767, 194.17560115, 0.00092233, -19.41756012, -9.223e-05, -58.25268035, -0.0002767, -194.17560115, -0.00092233, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 77.67024046, 0.0172884, 77.67024046, 0.05186521, 54.36916832, -1057.67010387, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 19.41756012, 9.223e-05, 58.25268035, 0.0002767, 194.17560115, 0.00092233, -19.41756012, -9.223e-05, -58.25268035, -0.0002767, -194.17560115, -0.00092233, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 4.5, 13.5, 3.325)
    ops.node(122020, 4.5, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.1225, 27530551.63159758, 11471063.17983233, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 107.89572262, 0.00065441, 128.94518631, 0.0120557, 12.89451863, 0.03658783, -107.89572262, -0.00065441, -128.94518631, -0.0120557, -12.89451863, -0.03658783, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 99.79285084, 0.00065441, 119.26151873, 0.0120557, 11.92615187, 0.03658783, -99.79285084, -0.00065441, -119.26151873, -0.0120557, -11.92615187, -0.03658783, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 132.74184017, 0.01308815, 132.74184017, 0.03926444, 92.91928812, -1584.60248854, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 33.18546004, 7.935e-05, 99.55638013, 0.00023805, 331.85460042, 0.0007935, -33.18546004, -7.935e-05, -99.55638013, -0.00023805, -331.85460042, -0.0007935, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 132.74184017, 0.01308815, 132.74184017, 0.03926444, 92.91928812, -1584.60248854, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 33.18546004, 7.935e-05, 99.55638013, 0.00023805, 331.85460042, 0.0007935, -33.18546004, -7.935e-05, -99.55638013, -0.00023805, -331.85460042, -0.0007935, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.35)
    ops.node(122021, 9.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.09, 27235052.5080971, 11347938.54504046, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 82.79790468, 0.00073633, 98.44752988, 0.01184997, 9.84475299, 0.03501634, -82.79790468, -0.00073633, -98.44752988, -0.01184997, -9.84475299, -0.03501634, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 75.56228948, 0.00073633, 89.84431164, 0.01184997, 8.98443116, 0.03501634, -75.56228948, -0.00073633, -89.84431164, -0.01184997, -8.98443116, -0.03501634, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 104.23404794, 0.01472656, 104.23404794, 0.04417969, 72.96383356, -1346.57258018, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 26.05851198, 8.573e-05, 78.17553595, 0.00025719, 260.58511984, 0.00085729, -26.05851198, -8.573e-05, -78.17553595, -0.00025719, -260.58511984, -0.00085729, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 104.23404794, 0.01472656, 104.23404794, 0.04417969, 72.96383356, -1346.57258018, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 26.05851198, 8.573e-05, 78.17553595, 0.00025719, 260.58511984, 0.00085729, -26.05851198, -8.573e-05, -78.17553595, -0.00025719, -260.58511984, -0.00085729, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.35)
    ops.node(122022, 12.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.09, 27188516.90614583, 11328548.7108941, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 81.66100974, 0.00074086, 97.08925246, 0.01199614, 9.70892525, 0.0350412, -81.66100974, -0.00074086, -97.08925246, -0.01199614, -9.70892525, -0.0350412, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 74.85820077, 0.00074086, 89.00118644, 0.01199614, 8.90011864, 0.0350412, -74.85820077, -0.00074086, -89.00118644, -0.01199614, -8.90011864, -0.0350412, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 105.14636508, 0.01481726, 105.14636508, 0.04445179, 73.60245556, -1369.63624075, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 26.28659127, 8.663e-05, 78.85977381, 0.00025988, 262.86591271, 0.00086628, -26.28659127, -8.663e-05, -78.85977381, -0.00025988, -262.86591271, -0.00086628, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 105.14636508, 0.01481726, 105.14636508, 0.04445179, 73.60245556, -1369.63624075, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 26.28659127, 8.663e-05, 78.85977381, 0.00025988, 262.86591271, 0.00086628, -26.28659127, -8.663e-05, -78.85977381, -0.00025988, -262.86591271, -0.00086628, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 16.5, 13.5, 3.325)
    ops.node(122023, 16.5, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.1225, 27249079.16229182, 11353782.98428826, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 107.0065752, 0.00063949, 127.85690671, 0.012045, 12.78569067, 0.03594808, -107.0065752, -0.00063949, -127.85690671, -0.012045, -12.78569067, -0.03594808, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 98.80546223, 0.00063949, 118.05779918, 0.012045, 11.80577992, 0.03594808, -98.80546223, -0.00063949, -118.05779918, -0.012045, -11.80577992, -0.03594808, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 131.39510397, 0.01278988, 131.39510397, 0.03836965, 91.97657278, -1579.20027242, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 32.84877599, 7.936e-05, 98.54632798, 0.00023807, 328.48775993, 0.00079356, -32.84877599, -7.936e-05, -98.54632798, -0.00023807, -328.48775993, -0.00079356, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 131.39510397, 0.01278988, 131.39510397, 0.03836965, 91.97657278, -1579.20027242, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 32.84877599, 7.936e-05, 98.54632798, 0.00023807, 328.48775993, 0.00079356, -32.84877599, -7.936e-05, -98.54632798, -0.00023807, -328.48775993, -0.00079356, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.325)
    ops.node(122024, 21.0, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.0625, 27234416.73607869, 11347673.64003279, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 48.74147358, 0.00083231, 57.95707168, 0.01289712, 5.79570717, 0.03965747, -48.74147358, -0.00083231, -57.95707168, -0.01289712, -5.79570717, -0.03965747, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 45.85414236, 0.00083231, 54.52382992, 0.01289712, 5.45238299, 0.03965747, -45.85414236, -0.00083231, -54.52382992, -0.01289712, -5.45238299, -0.03965747, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 77.42144509, 0.01664615, 77.42144509, 0.04993845, 54.19501157, -1048.48427336, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 19.35536127, 9.17e-05, 58.06608382, 0.00027509, 193.55361274, 0.00091697, -19.35536127, -9.17e-05, -58.06608382, -0.00027509, -193.55361274, -0.00091697, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 77.42144509, 0.01664615, 77.42144509, 0.04993845, 54.19501157, -1048.48427336, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 19.35536127, 9.17e-05, 58.06608382, 0.00027509, 193.55361274, 0.00091697, -19.35536127, -9.17e-05, -58.06608382, -0.00027509, -193.55361274, -0.00091697, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.125)
    ops.node(123001, 0.0, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 27394704.3141698, 11414460.13090408, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 37.47861648, 0.00080856, 45.05657454, 0.01541396, 4.50565745, 0.05295443, -37.47861648, -0.00080856, -45.05657454, -0.01541396, -4.50565745, -0.05295443, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 35.25034356, 0.00080856, 42.37775781, 0.01541396, 4.23777578, 0.05295443, -35.25034356, -0.00080856, -42.37775781, -0.01541396, -4.23777578, -0.05295443, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 71.43139741, 0.01617127, 71.43139741, 0.0485138, 50.00197819, -920.76917425, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 17.85784935, 8.411e-05, 53.57354806, 0.00025232, 178.57849352, 0.00084107, -17.85784935, -8.411e-05, -53.57354806, -0.00025232, -178.57849352, -0.00084107, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 71.43139741, 0.01617127, 71.43139741, 0.0485138, 50.00197819, -920.76917425, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 17.85784935, 8.411e-05, 53.57354806, 0.00025232, 178.57849352, 0.00084107, -17.85784935, -8.411e-05, -53.57354806, -0.00025232, -178.57849352, -0.00084107, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.5, 0.0, 6.125)
    ops.node(123002, 4.5, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 27609203.64950449, 11503834.8539602, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 50.15026325, 0.00087047, 59.51299008, 0.01280037, 5.95129901, 0.03869284, -50.15026325, -0.00087047, -59.51299008, -0.01280037, -5.95129901, -0.03869284, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 47.5729469, 0.00087047, 56.45450558, 0.01280037, 5.64545056, 0.03869284, -47.5729469, -0.00087047, -56.45450558, -0.01280037, -5.64545056, -0.03869284, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 80.1597361, 0.01740942, 80.1597361, 0.05222827, 56.11181527, -1097.4010947, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 20.03993402, 9.365e-05, 60.11980207, 0.00028095, 200.39934024, 0.00093651, -20.03993402, -9.365e-05, -60.11980207, -0.00028095, -200.39934024, -0.00093651, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 80.1597361, 0.01740942, 80.1597361, 0.05222827, 56.11181527, -1097.4010947, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 20.03993402, 9.365e-05, 60.11980207, 0.00028095, 200.39934024, 0.00093651, -20.03993402, -9.365e-05, -60.11980207, -0.00028095, -200.39934024, -0.00093651, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.5, 0.0, 6.125)
    ops.node(123005, 16.5, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 26470196.99939074, 11029248.74974614, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 51.19593369, 0.00086589, 60.62217112, 0.01178668, 6.06221711, 0.03422417, -51.19593369, -0.00086589, -60.62217112, -0.01178668, -6.06221711, -0.03422417, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 48.25061759, 0.00086589, 57.134561, 0.01178668, 5.7134561, 0.03422417, -48.25061759, -0.00086589, -57.134561, -0.01178668, -5.7134561, -0.03422417, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 76.77319013, 0.01731773, 76.77319013, 0.0519532, 53.74123309, -1074.48345627, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 19.19329753, 9.355e-05, 57.5798926, 0.00028066, 191.93297533, 0.00093554, -19.19329753, -9.355e-05, -57.5798926, -0.00028066, -191.93297533, -0.00093554, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 76.77319013, 0.01731773, 76.77319013, 0.0519532, 53.74123309, -1074.48345627, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 19.19329753, 9.355e-05, 57.5798926, 0.00028066, 191.93297533, 0.00093554, -19.19329753, -9.355e-05, -57.5798926, -0.00028066, -191.93297533, -0.00093554, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 21.0, 0.0, 6.125)
    ops.node(123006, 21.0, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 28430402.01538608, 11846000.8397442, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 38.6515544, 0.00077949, 46.45172748, 0.01517654, 4.64517275, 0.05533058, -38.6515544, -0.00077949, -46.45172748, -0.01517654, -4.64517275, -0.05533058, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 36.09811842, 0.00077949, 43.38298901, 0.01517654, 4.3382989, 0.05533058, -36.09811842, -0.00077949, -43.38298901, -0.01517654, -4.3382989, -0.05533058, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 71.92609552, 0.01558989, 71.92609552, 0.04676968, 50.34826686, -880.28406803, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 17.98152388, 8.16e-05, 53.94457164, 0.00024481, 179.8152388, 0.00081604, -17.98152388, -8.16e-05, -53.94457164, -0.00024481, -179.8152388, -0.00081604, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 71.92609552, 0.01558989, 71.92609552, 0.04676968, 50.34826686, -880.28406803, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 17.98152388, 8.16e-05, 53.94457164, 0.00024481, 179.8152388, 0.00081604, -17.98152388, -8.16e-05, -53.94457164, -0.00024481, -179.8152388, -0.00081604, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.125)
    ops.node(123007, 0.0, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 26924416.23518142, 11218506.76465893, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 50.66293776, 0.00085879, 60.04079387, 0.01235344, 6.00407939, 0.03606202, -50.66293776, -0.00085879, -60.04079387, -0.01235344, -6.00407939, -0.03606202, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 47.8726557, 0.00085879, 56.73402254, 0.01235344, 5.67340225, 0.03606202, -47.8726557, -0.00085879, -56.73402254, -0.01235344, -5.67340225, -0.03606202, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 78.46385475, 0.01717576, 78.46385475, 0.05152727, 54.92469833, -1091.76768969, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 19.61596369, 9.4e-05, 58.84789107, 0.000282, 196.15963688, 0.00094001, -19.61596369, -9.4e-05, -58.84789107, -0.000282, -196.15963688, -0.00094001, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 78.46385475, 0.01717576, 78.46385475, 0.05152727, 54.92469833, -1091.76768969, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 19.61596369, 9.4e-05, 58.84789107, 0.000282, 196.15963688, 0.00094001, -19.61596369, -9.4e-05, -58.84789107, -0.000282, -196.15963688, -0.00094001, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.5, 4.5, 6.125)
    ops.node(123008, 4.5, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 27081616.16931673, 11284006.7372153, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 105.16861663, 0.00064105, 125.77274005, 0.01214133, 12.57727401, 0.0364025, -105.16861663, -0.00064105, -125.77274005, -0.01214133, -12.57727401, -0.0364025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 96.86490027, 0.00064105, 115.84220001, 0.01214133, 11.58422, 0.0364025, -96.86490027, -0.00064105, -115.84220001, -0.01214133, -11.58422, -0.0364025, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 129.1446132, 0.012821, 129.1446132, 0.03846299, 90.40122924, -1540.66915099, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 32.2861533, 7.848e-05, 96.8584599, 0.00023544, 322.86153301, 0.00078479, -32.2861533, -7.848e-05, -96.8584599, -0.00023544, -322.86153301, -0.00078479, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 129.1446132, 0.012821, 129.1446132, 0.03846299, 90.40122924, -1540.66915099, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 32.2861533, 7.848e-05, 96.8584599, 0.00023544, 322.86153301, 0.00078479, -32.2861533, -7.848e-05, -96.8584599, -0.00023544, -322.86153301, -0.00078479, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.15)
    ops.node(123009, 9.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 27588314.79309262, 11495131.16378859, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 98.34534411, 0.00062644, 118.01483871, 0.01280623, 11.80148387, 0.04064563, -98.34534411, -0.00062644, -118.01483871, -0.01280623, -11.80148387, -0.04064563, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 89.87150548, 0.00062644, 107.84619566, 0.01280623, 10.78461957, 0.04064563, -89.87150548, -0.00062644, -107.84619566, -0.01280623, -10.78461957, -0.04064563, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 127.25575213, 0.01252881, 127.25575213, 0.03758643, 89.07902649, -1451.29746454, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 31.81393803, 7.591e-05, 95.4418141, 0.00022773, 318.13938033, 0.00075911, -31.81393803, -7.591e-05, -95.4418141, -0.00022773, -318.13938033, -0.00075911, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 127.25575213, 0.01252881, 127.25575213, 0.03758643, 89.07902649, -1451.29746454, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 31.81393803, 7.591e-05, 95.4418141, 0.00022773, 318.13938033, 0.00075911, -31.81393803, -7.591e-05, -95.4418141, -0.00022773, -318.13938033, -0.00075911, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.15)
    ops.node(123010, 12.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 26591859.98664095, 11079941.6611004, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 96.98405585, 0.00062858, 116.33541809, 0.01252636, 11.63354181, 0.03820626, -96.98405585, -0.00062858, -116.33541809, -0.01252636, -11.63354181, -0.03820626, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 88.77119108, 0.00062858, 106.4838291, 0.01252636, 10.64838291, 0.03820626, -88.77119108, -0.00062858, -106.4838291, -0.01252636, -10.64838291, -0.03820626, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 124.38054565, 0.0125716, 124.38054565, 0.03771481, 87.06638195, -1472.37738538, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 31.09513641, 7.698e-05, 93.28540923, 0.00023093, 310.95136412, 0.00076977, -31.09513641, -7.698e-05, -93.28540923, -0.00023093, -310.95136412, -0.00076977, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 124.38054565, 0.0125716, 124.38054565, 0.03771481, 87.06638195, -1472.37738538, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 31.09513641, 7.698e-05, 93.28540923, 0.00023093, 310.95136412, 0.00076977, -31.09513641, -7.698e-05, -93.28540923, -0.00023093, -310.95136412, -0.00076977, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 16.5, 4.5, 6.125)
    ops.node(123011, 16.5, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 25751783.39137309, 10729909.74640545, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 105.6995268, 0.00063656, 126.18984929, 0.01155881, 12.61898493, 0.0326875, -105.6995268, -0.00063656, -126.18984929, -0.01155881, -12.61898493, -0.0326875, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 96.76037772, 0.00063656, 115.51780647, 0.01155881, 11.55178065, 0.0326875, -96.76037772, -0.00063656, -115.51780647, -0.01155881, -11.55178065, -0.0326875, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 125.03418784, 0.01273112, 125.03418784, 0.03819336, 87.52393149, -1562.89944204, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 31.25854696, 7.991e-05, 93.77564088, 0.00023972, 312.58546961, 0.00079905, -31.25854696, -7.991e-05, -93.77564088, -0.00023972, -312.58546961, -0.00079905, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 125.03418784, 0.01273112, 125.03418784, 0.03819336, 87.52393149, -1562.89944204, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 31.25854696, 7.991e-05, 93.77564088, 0.00023972, 312.58546961, 0.00079905, -31.25854696, -7.991e-05, -93.77564088, -0.00023972, -312.58546961, -0.00079905, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.125)
    ops.node(123012, 21.0, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 27072999.7789212, 11280416.5745505, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 50.32891664, 0.00087496, 59.66228154, 0.01229846, 5.96622815, 0.03645864, -50.32891664, -0.00087496, -59.66228154, -0.01229846, -5.96622815, -0.03645864, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 47.70680419, 0.00087496, 56.55390525, 0.01229846, 5.65539053, 0.03645864, -47.70680419, -0.00087496, -56.55390525, -0.01229846, -5.65539053, -0.03645864, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 78.33063738, 0.0174992, 78.33063738, 0.05249759, 54.83144617, -1081.75028211, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 19.58265935, 9.333e-05, 58.74797804, 0.00027998, 195.82659346, 0.00093327, -19.58265935, -9.333e-05, -58.74797804, -0.00027998, -195.82659346, -0.00093327, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 78.33063738, 0.0174992, 78.33063738, 0.05249759, 54.83144617, -1081.75028211, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 19.58265935, 9.333e-05, 58.74797804, 0.00027998, 195.82659346, 0.00093327, -19.58265935, -9.333e-05, -58.74797804, -0.00027998, -195.82659346, -0.00093327, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.125)
    ops.node(123013, 0.0, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 27861093.73542754, 11608789.05642814, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 50.20467927, 0.00088672, 59.58814819, 0.01274522, 5.95881482, 0.03925912, -50.20467927, -0.00088672, -59.58814819, -0.01274522, -5.95881482, -0.03925912, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 47.74526779, 0.00088672, 56.6690622, 0.01274522, 5.66690622, 0.03925912, -47.74526779, -0.00088672, -56.6690622, -0.01274522, -5.66690622, -0.03925912, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 80.10515131, 0.01773436, 80.10515131, 0.05320309, 56.07360592, -1084.48590571, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 20.02628783, 9.274e-05, 60.07886349, 0.00027822, 200.26287828, 0.00092741, -20.02628783, -9.274e-05, -60.07886349, -0.00027822, -200.26287828, -0.00092741, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 80.10515131, 0.01773436, 80.10515131, 0.05320309, 56.07360592, -1084.48590571, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 20.02628783, 9.274e-05, 60.07886349, 0.00027822, 200.26287828, 0.00092741, -20.02628783, -9.274e-05, -60.07886349, -0.00027822, -200.26287828, -0.00092741, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.5, 9.0, 6.125)
    ops.node(123014, 4.5, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1225, 28178191.79591591, 11740913.2482983, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 106.08379011, 0.00063709, 126.92786712, 0.01245901, 12.69278671, 0.03910478, -106.08379011, -0.00063709, -126.92786712, -0.01245901, -12.69278671, -0.03910478, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 97.67482556, 0.00063709, 116.86665104, 0.01245901, 11.6866651, 0.03910478, -97.67482556, -0.00063709, -116.86665104, -0.01245901, -11.6866651, -0.03910478, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 134.23630764, 0.01274175, 134.23630764, 0.03822525, 93.96541535, -1558.7440712, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 33.55907691, 7.84e-05, 100.67723073, 0.0002352, 335.59076909, 0.00078399, -33.55907691, -7.84e-05, -100.67723073, -0.0002352, -335.59076909, -0.00078399, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 134.23630764, 0.01274175, 134.23630764, 0.03822525, 93.96541535, -1558.7440712, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 33.55907691, 7.84e-05, 100.67723073, 0.0002352, 335.59076909, 0.00078399, -33.55907691, -7.84e-05, -100.67723073, -0.0002352, -335.59076909, -0.00078399, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.15)
    ops.node(123015, 9.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 27497625.12524068, 11457343.80218362, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 97.63473297, 0.00061855, 117.11441574, 0.01277006, 11.71144157, 0.04009476, -97.63473297, -0.00061855, -117.11441574, -0.01277006, -11.71144157, -0.04009476, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 89.50305311, 0.00061855, 107.36033635, 0.01277006, 10.73603364, 0.04009476, -89.50305311, -0.00061855, -107.36033635, -0.01277006, -10.73603364, -0.04009476, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 127.27754255, 0.01237099, 127.27754255, 0.03711297, 89.09427979, -1459.34614765, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 31.81938564, 7.617e-05, 95.45815691, 0.00022852, 318.19385638, 0.00076175, -31.81938564, -7.617e-05, -95.45815691, -0.00022852, -318.19385638, -0.00076175, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 127.27754255, 0.01237099, 127.27754255, 0.03711297, 89.09427979, -1459.34614765, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 31.81938564, 7.617e-05, 95.45815691, 0.00022852, 318.19385638, 0.00076175, -31.81938564, -7.617e-05, -95.45815691, -0.00022852, -318.19385638, -0.00076175, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.15)
    ops.node(123016, 12.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1225, 27393193.55535775, 11413830.64806573, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 98.82426041, 0.00062689, 118.53854608, 0.01280598, 11.85385461, 0.03990921, -98.82426041, -0.00062689, -118.53854608, -0.01280598, -11.85385461, -0.03990921, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 90.44423915, 0.00062689, 108.48680846, 0.01280598, 10.84868085, 0.03990921, -90.44423915, -0.00062689, -108.48680846, -0.01280598, -10.84868085, -0.03990921, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 127.3632951, 0.01253785, 127.3632951, 0.03761355, 89.15430657, -1470.55201828, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 31.84082378, 7.652e-05, 95.52247133, 0.00022955, 318.40823775, 0.00076517, -31.84082378, -7.652e-05, -95.52247133, -0.00022955, -318.40823775, -0.00076517, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 127.3632951, 0.01253785, 127.3632951, 0.03761355, 89.15430657, -1470.55201828, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 31.84082378, 7.652e-05, 95.52247133, 0.00022955, 318.40823775, 0.00076517, -31.84082378, -7.652e-05, -95.52247133, -0.00022955, -318.40823775, -0.00076517, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 16.5, 9.0, 6.125)
    ops.node(123017, 16.5, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.1225, 28084709.4801308, 11701962.28338783, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 106.80318712, 0.00062531, 127.78726556, 0.01224347, 12.77872656, 0.03869327, -106.80318712, -0.00062531, -127.78726556, -0.01224347, -12.77872656, -0.03869327, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 97.87874381, 0.00062531, 117.10939876, 0.01224347, 11.71093988, 0.03869327, -97.87874381, -0.00062531, -117.10939876, -0.01224347, -11.71093988, -0.03869327, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 133.00211994, 0.01250628, 133.00211994, 0.03751884, 93.10148396, -1539.37101587, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 33.25052998, 7.794e-05, 99.75158995, 0.00023381, 332.50529985, 0.00077937, -33.25052998, -7.794e-05, -99.75158995, -0.00023381, -332.50529985, -0.00077937, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 133.00211994, 0.01250628, 133.00211994, 0.03751884, 93.10148396, -1539.37101587, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 33.25052998, 7.794e-05, 99.75158995, 0.00023381, 332.50529985, 0.00077937, -33.25052998, -7.794e-05, -99.75158995, -0.00023381, -332.50529985, -0.00077937, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.125)
    ops.node(123018, 21.0, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 27386131.27707032, 11410888.03211263, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 50.34799528, 0.00086769, 59.71772226, 0.01266113, 5.97177223, 0.03776529, -50.34799528, -0.00086769, -59.71772226, -0.01266113, -5.97177223, -0.03776529, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 47.71708241, 0.00086769, 56.59719833, 0.01266113, 5.65971983, 0.03776529, -47.71708241, -0.00086769, -56.59719833, -0.01266113, -5.65971983, -0.03776529, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 80.08988279, 0.01735375, 80.08988279, 0.05206125, 56.06291795, -1106.79584797, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 20.0224707, 9.433e-05, 60.06741209, 0.00028299, 200.22470698, 0.00094332, -20.0224707, -9.433e-05, -60.06741209, -0.00028299, -200.22470698, -0.00094332, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 80.08988279, 0.01735375, 80.08988279, 0.05206125, 56.06291795, -1106.79584797, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 20.0224707, 9.433e-05, 60.06741209, 0.00028299, 200.22470698, 0.00094332, -20.0224707, -9.433e-05, -60.06741209, -0.00028299, -200.22470698, -0.00094332, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.125)
    ops.node(123019, 0.0, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 28440688.11104437, 11850286.71293516, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 37.9208711, 0.00079635, 45.57330952, 0.01571389, 4.55733095, 0.05589268, -37.9208711, -0.00079635, -45.57330952, -0.01571389, -4.55733095, -0.05589268, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 35.60822908, 0.00079635, 42.79397594, 0.01571389, 4.27939759, 0.05589268, -35.60822908, -0.00079635, -42.79397594, -0.01571389, -4.27939759, -0.05589268, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 72.73237733, 0.01592699, 72.73237733, 0.04778097, 50.91266413, -901.22291361, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 18.18309433, 8.249e-05, 54.549283, 0.00024747, 181.83094334, 0.00082489, -18.18309433, -8.249e-05, -54.549283, -0.00024747, -181.83094334, -0.00082489, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 72.73237733, 0.01592699, 72.73237733, 0.04778097, 50.91266413, -901.22291361, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 18.18309433, 8.249e-05, 54.549283, 0.00024747, 181.83094334, 0.00082489, -18.18309433, -8.249e-05, -54.549283, -0.00024747, -181.83094334, -0.00082489, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 4.5, 13.5, 6.125)
    ops.node(123020, 4.5, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 28281390.6313987, 11783912.76308279, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 50.24017527, 0.00088794, 59.66601926, 0.0130655, 5.96660193, 0.04092419, -50.24017527, -0.00088794, -59.66601926, -0.0130655, -5.96660193, -0.04092419, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 47.79316943, 0.00088794, 56.75991679, 0.0130655, 5.67599168, 0.04092419, -47.79316943, -0.00088794, -56.75991679, -0.0130655, -5.67599168, -0.04092419, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 81.10457909, 0.01775875, 81.10457909, 0.05327626, 56.77320536, -1086.6785495, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 20.27614477, 9.25e-05, 60.82843432, 0.00027751, 202.76144773, 0.00092503, -20.27614477, -9.25e-05, -60.82843432, -0.00027751, -202.76144773, -0.00092503, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 81.10457909, 0.01775875, 81.10457909, 0.05327626, 56.77320536, -1086.6785495, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 20.27614477, 9.25e-05, 60.82843432, 0.00027751, 202.76144773, 0.00092503, -20.27614477, -9.25e-05, -60.82843432, -0.00027751, -202.76144773, -0.00092503, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.15)
    ops.node(123021, 9.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 28131263.58317538, 11721359.82632308, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 46.9080526, 0.0008389, 55.904678, 0.01369557, 5.5904678, 0.04427681, -46.9080526, -0.0008389, -55.904678, -0.01369557, -5.5904678, -0.04427681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 44.30813186, 0.0008389, 52.80611126, 0.01369557, 5.28061113, 0.04427681, -44.30813186, -0.0008389, -52.80611126, -0.01369557, -5.28061113, -0.04427681, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 78.66007676, 0.01677808, 78.66007676, 0.05033423, 55.06205373, -1033.47682781, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 19.66501919, 9.019e-05, 58.99505757, 0.00027058, 196.65019191, 0.00090194, -19.66501919, -9.019e-05, -58.99505757, -0.00027058, -196.65019191, -0.00090194, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 78.66007676, 0.01677808, 78.66007676, 0.05033423, 55.06205373, -1033.47682781, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 19.66501919, 9.019e-05, 58.99505757, 0.00027058, 196.65019191, 0.00090194, -19.66501919, -9.019e-05, -58.99505757, -0.00027058, -196.65019191, -0.00090194, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.15)
    ops.node(123022, 12.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0625, 26926004.18863422, 11219168.41193092, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 46.43528659, 0.00085502, 55.27354807, 0.01294639, 5.52735481, 0.03998486, -46.43528659, -0.00085502, -55.27354807, -0.01294639, -5.52735481, -0.03998486, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 43.91127607, 0.00085502, 52.26912995, 0.01294639, 5.22691299, 0.03998486, -43.91127607, -0.00085502, -52.26912995, -0.01294639, -5.22691299, -0.03998486, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 75.42759731, 0.01710037, 75.42759731, 0.05130112, 52.79931812, -1015.47079741, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 18.85689933, 9.036e-05, 56.57069798, 0.00027108, 188.56899327, 0.00090358, -18.85689933, -9.036e-05, -56.57069798, -0.00027108, -188.56899327, -0.00090358, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 75.42759731, 0.01710037, 75.42759731, 0.05130112, 52.79931812, -1015.47079741, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 18.85689933, 9.036e-05, 56.57069798, 0.00027108, 188.56899327, 0.00090358, -18.85689933, -9.036e-05, -56.57069798, -0.00027108, -188.56899327, -0.00090358, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 16.5, 13.5, 6.125)
    ops.node(123023, 16.5, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.0625, 27669833.18839698, 11529097.16183207, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 50.71547404, 0.00085931, 60.18881386, 0.0126395, 6.01888139, 0.03871178, -50.71547404, -0.00085931, -60.18881386, -0.0126395, -6.01888139, -0.03871178, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 47.96352681, 0.00085931, 56.92281975, 0.0126395, 5.69228197, 0.03871178, -47.96352681, -0.00085931, -56.92281975, -0.0126395, -5.69228197, -0.03871178, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 79.57575907, 0.01718611, 79.57575907, 0.05155834, 55.70303135, -1081.26368422, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 19.89393977, 9.277e-05, 59.68181931, 0.0002783, 198.93939769, 0.00092765, -19.89393977, -9.277e-05, -59.68181931, -0.0002783, -198.93939769, -0.00092765, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 79.57575907, 0.01718611, 79.57575907, 0.05155834, 55.70303135, -1081.26368422, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 19.89393977, 9.277e-05, 59.68181931, 0.0002783, 198.93939769, 0.00092765, -19.89393977, -9.277e-05, -59.68181931, -0.0002783, -198.93939769, -0.00092765, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.125)
    ops.node(123024, 21.0, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 28761853.79465206, 11984105.74777169, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 38.70061652, 0.00077345, 46.50029869, 0.01556039, 4.65002987, 0.05649988, -38.70061652, -0.00077345, -46.50029869, -0.01556039, -4.65002987, -0.05649988, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 36.12940989, 0.00077345, 43.41089375, 0.01556039, 4.34108937, 0.05649988, -36.12940989, -0.00077345, -43.41089375, -0.01556039, -4.34108937, -0.05649988, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 73.25561989, 0.01546905, 73.25561989, 0.04640716, 51.27893393, -898.3851439, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 18.31390497, 8.216e-05, 54.94171492, 0.00024647, 183.13904973, 0.00082155, -18.31390497, -8.216e-05, -54.94171492, -0.00024647, -183.13904973, -0.00082155, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 73.25561989, 0.01546905, 73.25561989, 0.04640716, 51.27893393, -898.3851439, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 18.31390497, 8.216e-05, 54.94171492, 0.00024647, 183.13904973, 0.00082155, -18.31390497, -8.216e-05, -54.94171492, -0.00024647, -183.13904973, -0.00082155, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.925)
    ops.node(124001, 0.0, 0.0, 11.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26797028.54343202, 11165428.55976334, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 25.39287052, 0.00077303, 30.93303957, 0.01824684, 3.09330396, 0.07164312, -25.39287052, -0.00077303, -30.93303957, -0.01824684, -3.09330396, -0.07164312, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 23.55337039, 0.00077303, 28.69220074, 0.01824684, 2.86922007, 0.07164312, -23.55337039, -0.00077303, -28.69220074, -0.01824684, -2.86922007, -0.07164312, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 60.4472334, 0.0154606, 60.4472334, 0.04638179, 42.31306338, -930.24653811, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 15.11180835, 7.276e-05, 45.33542505, 0.00021828, 151.11808349, 0.00072761, -15.11180835, -7.276e-05, -45.33542505, -0.00021828, -151.11808349, -0.00072761, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 60.4472334, 0.0154606, 60.4472334, 0.04638179, 42.31306338, -930.24653811, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 15.11180835, 7.276e-05, 45.33542505, 0.00021828, 151.11808349, 0.00072761, -15.11180835, -7.276e-05, -45.33542505, -0.00021828, -151.11808349, -0.00072761, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.5, 0.0, 8.925)
    ops.node(124002, 4.5, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 27552874.63806916, 11480364.43252882, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 32.31216795, 0.00075374, 39.07351475, 0.01654255, 3.90735148, 0.06174701, -32.31216795, -0.00075374, -39.07351475, -0.01654255, -3.90735148, -0.06174701, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 29.98791697, 0.00075374, 36.26291241, 0.01654255, 3.62629124, 0.06174701, -29.98791697, -0.00075374, -36.26291241, -0.01654255, -3.62629124, -0.06174701, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 66.77864347, 0.01507477, 66.77864347, 0.04522432, 46.74505043, -857.88890698, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 16.69466087, 7.818e-05, 50.0839826, 0.00023453, 166.94660868, 0.00078177, -16.69466087, -7.818e-05, -50.0839826, -0.00023453, -166.94660868, -0.00078177, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 66.77864347, 0.01507477, 66.77864347, 0.04522432, 46.74505043, -857.88890698, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 16.69466087, 7.818e-05, 50.0839826, 0.00023453, 166.94660868, 0.00078177, -16.69466087, -7.818e-05, -50.0839826, -0.00023453, -166.94660868, -0.00078177, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.5, 0.0, 8.925)
    ops.node(124005, 16.5, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 28112417.5965087, 11713507.33187863, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 32.86740873, 0.00074601, 39.72386885, 0.01645503, 3.97238688, 0.0628248, -32.86740873, -0.00074601, -39.72386885, -0.01645503, -3.97238688, -0.0628248, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 30.41502606, 0.00074601, 36.75989537, 0.01645503, 3.67598954, 0.0628248, -30.41502606, -0.00074601, -36.75989537, -0.01645503, -3.67598954, -0.0628248, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 67.09954299, 0.01492024, 67.09954299, 0.04476071, 46.9696801, -835.39785675, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 16.77488575, 7.699e-05, 50.32465725, 0.00023097, 167.74885748, 0.0007699, -16.77488575, -7.699e-05, -50.32465725, -0.00023097, -167.74885748, -0.0007699, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 67.09954299, 0.01492024, 67.09954299, 0.04476071, 46.9696801, -835.39785675, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 16.77488575, 7.699e-05, 50.32465725, 0.00023097, 167.74885748, 0.0007699, -16.77488575, -7.699e-05, -50.32465725, -0.00023097, -167.74885748, -0.0007699, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 21.0, 0.0, 8.925)
    ops.node(124006, 21.0, 0.0, 11.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 28690291.62009976, 11954288.17504157, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 25.99972942, 0.00074104, 31.57404233, 0.01820692, 3.15740423, 0.07411799, -25.99972942, -0.00074104, -31.57404233, -0.01820692, -3.15740423, -0.07411799, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 23.96545687, 0.00074104, 29.10362403, 0.01820692, 2.9103624, 0.07411799, -23.96545687, -0.00074104, -29.10362403, -0.01820692, -2.9103624, -0.07411799, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 63.56950526, 0.01482082, 63.56950526, 0.04446247, 44.49865368, -918.36693513, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 15.89237632, 7.147e-05, 47.67712895, 0.00021441, 158.92376315, 0.0007147, -15.89237632, -7.147e-05, -47.67712895, -0.00021441, -158.92376315, -0.0007147, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 63.56950526, 0.01482082, 63.56950526, 0.04446247, 44.49865368, -918.36693513, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 15.89237632, 7.147e-05, 47.67712895, 0.00021441, 158.92376315, 0.0007147, -15.89237632, -7.147e-05, -47.67712895, -0.00021441, -158.92376315, -0.0007147, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 8.925)
    ops.node(124007, 0.0, 4.5, 11.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 27294826.15064396, 11372844.22943499, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 32.40315994, 0.00074904, 39.19414849, 0.01659352, 3.91941485, 0.06133398, -32.40315994, -0.00074904, -39.19414849, -0.01659352, -3.91941485, -0.06133398, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 30.01142572, 0.00074904, 36.30115946, 0.01659352, 3.63011595, 0.06133398, -30.01142572, -0.00074904, -36.30115946, -0.01659352, -3.63011595, -0.06133398, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 65.83063774, 0.01498074, 65.83063774, 0.04494221, 46.08144642, -844.6014504, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 16.45765943, 7.78e-05, 49.3729783, 0.00023339, 164.57659434, 0.00077796, -16.45765943, -7.78e-05, -49.3729783, -0.00023339, -164.57659434, -0.00077796, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 65.83063774, 0.01498074, 65.83063774, 0.04494221, 46.08144642, -844.6014504, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 16.45765943, 7.78e-05, 49.3729783, 0.00023339, 164.57659434, 0.00077796, -16.45765943, -7.78e-05, -49.3729783, -0.00023339, -164.57659434, -0.00077796, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.5, 4.5, 8.925)
    ops.node(124008, 4.5, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 25754414.66150172, 10731006.10895905, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 70.31115954, 0.00059524, 85.27493003, 0.0144616, 8.527493, 0.0482687, -70.31115954, -0.00059524, -85.27493003, -0.0144616, -8.527493, -0.0482687, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 63.08764425, 0.00059524, 76.51409086, 0.0144616, 7.65140909, 0.0482687, -63.08764425, -0.00059524, -76.51409086, -0.0144616, -7.65140909, -0.0482687, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 106.95001038, 0.01190483, 106.95001038, 0.03571448, 74.86500727, -1215.04098627, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 26.7375026, 6.834e-05, 80.21250779, 0.00020502, 267.37502596, 0.00068341, -26.7375026, -6.834e-05, -80.21250779, -0.00020502, -267.37502596, -0.00068341, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 106.95001038, 0.01190483, 106.95001038, 0.03571448, 74.86500727, -1215.04098627, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 26.7375026, 6.834e-05, 80.21250779, 0.00020502, 267.37502596, 0.00068341, -26.7375026, -6.834e-05, -80.21250779, -0.00020502, -267.37502596, -0.00068341, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.0, 4.5, 8.95)
    ops.node(124009, 9.0, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 28448688.46750101, 11853620.19479209, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 66.56252669, 0.00057292, 80.680499, 0.01527329, 8.0680499, 0.05531322, -66.56252669, -0.00057292, -80.680499, -0.01527329, -8.0680499, -0.05531322, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 59.13436948, 0.00057292, 71.6768229, 0.01527329, 7.16768229, 0.05531322, -59.13436948, -0.00057292, -71.6768229, -0.01527329, -7.16768229, -0.05531322, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 113.8943004, 0.01145842, 113.8943004, 0.03437527, 79.72601028, -1204.43737034, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 28.4735751, 6.589e-05, 85.4207253, 0.00019766, 284.73575099, 0.00065886, -28.4735751, -6.589e-05, -85.4207253, -0.00019766, -284.73575099, -0.00065886, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 113.8943004, 0.01145842, 113.8943004, 0.03437527, 79.72601028, -1204.43737034, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 28.4735751, 6.589e-05, 85.4207253, 0.00019766, 284.73575099, 0.00065886, -28.4735751, -6.589e-05, -85.4207253, -0.00019766, -284.73575099, -0.00065886, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.0, 4.5, 8.95)
    ops.node(124010, 12.0, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 28310949.79278119, 11796229.08032549, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 65.81785601, 0.00056777, 79.79517684, 0.01543605, 7.97951768, 0.05530948, -65.81785601, -0.00056777, -79.79517684, -0.01543605, -7.97951768, -0.05530948, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 58.52240974, 0.00056777, 70.95044289, 0.01543605, 7.09504429, 0.05530948, -58.52240974, -0.00056777, -70.95044289, -0.01543605, -7.09504429, -0.05530948, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 113.33011135, 0.01135546, 113.33011135, 0.03406637, 79.33107794, -1202.32592601, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 28.33252784, 6.588e-05, 84.99758351, 0.00019764, 283.32527837, 0.00065879, -28.33252784, -6.588e-05, -84.99758351, -0.00019764, -283.32527837, -0.00065879, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 113.33011135, 0.01135546, 113.33011135, 0.03406637, 79.33107794, -1202.32592601, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 28.33252784, 6.588e-05, 84.99758351, 0.00019764, 283.32527837, 0.00065879, -28.33252784, -6.588e-05, -84.99758351, -0.00019764, -283.32527837, -0.00065879, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 16.5, 4.5, 8.925)
    ops.node(124011, 16.5, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 28071726.41682608, 11696552.67367753, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 72.42797446, 0.00057407, 87.68880445, 0.01451406, 8.76888044, 0.05210222, -72.42797446, -0.00057407, -87.68880445, -0.01451406, -8.76888044, -0.05210222, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 64.46221605, 0.00057407, 78.04463261, 0.01451406, 7.80446326, 0.05210222, -64.46221605, -0.00057407, -78.04463261, -0.01451406, -7.80446326, -0.05210222, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 114.66459553, 0.01148134, 114.66459553, 0.03444402, 80.26521687, -1200.96313209, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 28.66614888, 6.722e-05, 85.99844665, 0.00020167, 286.66148883, 0.00067223, -28.66614888, -6.722e-05, -85.99844665, -0.00020167, -286.66148883, -0.00067223, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 114.66459553, 0.01148134, 114.66459553, 0.03444402, 80.26521687, -1200.96313209, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 28.66614888, 6.722e-05, 85.99844665, 0.00020167, 286.66148883, 0.00067223, -28.66614888, -6.722e-05, -85.99844665, -0.00020167, -286.66148883, -0.00067223, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 8.925)
    ops.node(124012, 21.0, 4.5, 11.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 27223938.69161687, 11343307.78817369, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 31.8352227, 0.00075899, 38.50908409, 0.01673974, 3.85090841, 0.0613235, -31.8352227, -0.00075899, -38.50908409, -0.01673974, -3.85090841, -0.0613235, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 29.60998476, 0.00075899, 35.81735248, 0.01673974, 3.58173525, 0.0613235, -29.60998476, -0.00075899, -35.81735248, -0.01673974, -3.58173525, -0.0613235, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 66.24283366, 0.01517979, 66.24283366, 0.04553936, 46.36998356, -861.65078583, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 16.56070842, 7.849e-05, 49.68212525, 0.00023546, 165.60708416, 0.00078487, -16.56070842, -7.849e-05, -49.68212525, -0.00023546, -165.60708416, -0.00078487, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 66.24283366, 0.01517979, 66.24283366, 0.04553936, 46.36998356, -861.65078583, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 16.56070842, 7.849e-05, 49.68212525, 0.00023546, 165.60708416, 0.00078487, -16.56070842, -7.849e-05, -49.68212525, -0.00023546, -165.60708416, -0.00078487, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.0, 8.925)
    ops.node(124013, 0.0, 9.0, 11.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 29026623.81039253, 12094426.58766356, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 32.12620581, 0.00075463, 38.78545517, 0.01682731, 3.87854552, 0.06503845, -32.12620581, -0.00075463, -38.78545517, -0.01682731, -3.87854552, -0.06503845, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 29.91204107, 0.00075463, 36.11232945, 0.01682731, 3.61123294, 0.06503845, -29.91204107, -0.00075463, -36.11232945, -0.01682731, -3.61123294, -0.06503845, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 69.4399555, 0.01509269, 69.4399555, 0.04527807, 48.60796885, -856.13147481, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 17.35998888, 7.717e-05, 52.07996663, 0.0002315, 173.59988875, 0.00077166, -17.35998888, -7.717e-05, -52.07996663, -0.0002315, -173.59988875, -0.00077166, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 69.4399555, 0.01509269, 69.4399555, 0.04527807, 48.60796885, -856.13147481, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 17.35998888, 7.717e-05, 52.07996663, 0.0002315, 173.59988875, 0.00077166, -17.35998888, -7.717e-05, -52.07996663, -0.0002315, -173.59988875, -0.00077166, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.5, 9.0, 8.925)
    ops.node(124014, 4.5, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1225, 27611281.36562218, 11504700.56900924, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 69.40063735, 0.00059204, 84.06847046, 0.0149251, 8.40684705, 0.05184045, -69.40063735, -0.00059204, -84.06847046, -0.0149251, -8.40684705, -0.05184045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 62.71721941, 0.00059204, 75.97251133, 0.0149251, 7.59725113, 0.05184045, -62.71721941, -0.00059204, -75.97251133, -0.0149251, -7.59725113, -0.05184045, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 113.65209307, 0.01184075, 113.65209307, 0.03552224, 79.55646515, -1219.55830095, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 28.41302327, 6.774e-05, 85.23906981, 0.00020322, 284.13023269, 0.0006774, -28.41302327, -6.774e-05, -85.23906981, -0.00020322, -284.13023269, -0.0006774, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 113.65209307, 0.01184075, 113.65209307, 0.03552224, 79.55646515, -1219.55830095, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 28.41302327, 6.774e-05, 85.23906981, 0.00020322, 284.13023269, 0.0006774, -28.41302327, -6.774e-05, -85.23906981, -0.00020322, -284.13023269, -0.0006774, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 9.0, 8.95)
    ops.node(124015, 9.0, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 28410382.70290735, 11837659.45954473, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 67.11324053, 0.00057635, 81.31196824, 0.01502702, 8.13119682, 0.05442425, -67.11324053, -0.00057635, -81.31196824, -0.01502702, -8.13119682, -0.05442425, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 60.00332185, 0.00057635, 72.69784862, 0.01502702, 7.26978486, 0.05442425, -60.00332185, -0.00057635, -72.69784862, -0.01502702, -7.26978486, -0.05442425, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 113.74137595, 0.01152696, 113.74137595, 0.03458089, 79.61896316, -1180.83793757, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 28.43534399, 6.589e-05, 85.30603196, 0.00019766, 284.35343986, 0.00065886, -28.43534399, -6.589e-05, -85.30603196, -0.00019766, -284.35343986, -0.00065886, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 113.74137595, 0.01152696, 113.74137595, 0.03458089, 79.61896316, -1180.83793757, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 28.43534399, 6.589e-05, 85.30603196, 0.00019766, 284.35343986, 0.00065886, -28.43534399, -6.589e-05, -85.30603196, -0.00019766, -284.35343986, -0.00065886, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.0, 9.0, 8.95)
    ops.node(124016, 12.0, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1225, 26464915.32558582, 11027048.05232743, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 68.34263749, 0.00057264, 82.98601343, 0.01476272, 8.29860134, 0.05140592, -68.34263749, -0.00057264, -82.98601343, -0.01476272, -8.29860134, -0.05140592, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 60.47744468, 0.00057264, 73.4355919, 0.01476272, 7.34355919, 0.05140592, -60.47744468, -0.00057264, -73.4355919, -0.01476272, -7.34355919, -0.05140592, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 107.38761367, 0.0114528, 107.38761367, 0.03435841, 75.17132957, -1197.45673323, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 26.84690342, 6.678e-05, 80.54071025, 0.00020034, 268.46903418, 0.00066779, -26.84690342, -6.678e-05, -80.54071025, -0.00020034, -268.46903418, -0.00066779, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 107.38761367, 0.0114528, 107.38761367, 0.03435841, 75.17132957, -1197.45673323, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 26.84690342, 6.678e-05, 80.54071025, 0.00020034, 268.46903418, 0.00066779, -26.84690342, -6.678e-05, -80.54071025, -0.00020034, -268.46903418, -0.00066779, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 16.5, 9.0, 8.925)
    ops.node(124017, 16.5, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.1225, 27970647.0931257, 11654436.28880238, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 71.78013767, 0.00058932, 86.91530152, 0.0147992, 8.69153015, 0.05224274, -71.78013767, -0.00058932, -86.91530152, -0.0147992, -8.69153015, -0.05224274, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 64.30645751, 0.00058932, 77.8657624, 0.0147992, 7.78657624, 0.05224274, -64.30645751, -0.00058932, -77.8657624, -0.0147992, -7.78657624, -0.05224274, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 114.788724, 0.01178647, 114.788724, 0.03535941, 80.3521068, -1215.00521718, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 28.697181, 6.754e-05, 86.091543, 0.00020262, 286.97181001, 0.00067538, -28.697181, -6.754e-05, -86.091543, -0.00020262, -286.97181001, -0.00067538, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 114.788724, 0.01178647, 114.788724, 0.03535941, 80.3521068, -1215.00521718, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 28.697181, 6.754e-05, 86.091543, 0.00020262, 286.97181001, 0.00067538, -28.697181, -6.754e-05, -86.091543, -0.00020262, -286.97181001, -0.00067538, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 21.0, 9.0, 8.925)
    ops.node(124018, 21.0, 9.0, 11.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 26998699.32510646, 11249458.05212769, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 32.23874413, 0.0007617, 39.00270252, 0.01675158, 3.90027025, 0.06082934, -32.23874413, -0.0007617, -39.00270252, -0.01675158, -3.90027025, -0.06082934, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 29.92336835, 0.0007617, 36.20154152, 0.01675158, 3.62015415, 0.06082934, -29.92336835, -0.0007617, -36.20154152, -0.01675158, -3.62015415, -0.06082934, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 65.71141028, 0.01523391, 65.71141028, 0.04570172, 45.9979872, -857.92601862, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 16.42785257, 7.851e-05, 49.28355771, 0.00023552, 164.27852571, 0.00078507, -16.42785257, -7.851e-05, -49.28355771, -0.00023552, -164.27852571, -0.00078507, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 65.71141028, 0.01523391, 65.71141028, 0.04570172, 45.9979872, -857.92601862, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 16.42785257, 7.851e-05, 49.28355771, 0.00023552, 164.27852571, 0.00078507, -16.42785257, -7.851e-05, -49.28355771, -0.00023552, -164.27852571, -0.00078507, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 13.5, 8.925)
    ops.node(124019, 0.0, 13.5, 11.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 27746488.0990606, 11561036.70794192, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 25.33984381, 0.00077036, 30.82498894, 0.01840229, 3.08249889, 0.07313816, -25.33984381, -0.00077036, -30.82498894, -0.01840229, -3.08249889, -0.07313816, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 23.54217656, 0.00077036, 28.63819277, 0.01840229, 2.86381928, 0.07313816, -23.54217656, -0.00077036, -28.63819277, -0.01840229, -2.86381928, -0.07313816, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 61.66037932, 0.01540717, 61.66037932, 0.04622152, 43.16226552, -909.25140773, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 15.41509483, 7.168e-05, 46.24528449, 0.00021505, 154.1509483, 0.00071682, -15.41509483, -7.168e-05, -46.24528449, -0.00021505, -154.1509483, -0.00071682, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 61.66037932, 0.01540717, 61.66037932, 0.04622152, 43.16226552, -909.25140773, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 15.41509483, 7.168e-05, 46.24528449, 0.00021505, 154.1509483, 0.00071682, -15.41509483, -7.168e-05, -46.24528449, -0.00021505, -154.1509483, -0.00071682, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 4.5, 13.5, 8.925)
    ops.node(124020, 4.5, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 27697876.64337321, 11540781.93473884, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 32.39762555, 0.00074551, 39.17199664, 0.01638271, 3.91719966, 0.06189608, -32.39762555, -0.00074551, -39.17199664, -0.01638271, -3.91719966, -0.06189608, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 30.02549076, 0.00074551, 36.30384644, 0.01638271, 3.63038464, 0.06189608, -30.02549076, -0.00074551, -36.30384644, -0.01638271, -3.63038464, -0.06189608, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 66.78745997, 0.01491026, 66.78745997, 0.04473079, 46.75122198, -849.73838631, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 16.69686499, 7.778e-05, 50.09059498, 0.00023334, 166.96864993, 0.00077778, -16.69686499, -7.778e-05, -50.09059498, -0.00023334, -166.96864993, -0.00077778, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 66.78745997, 0.01491026, 66.78745997, 0.04473079, 46.75122198, -849.73838631, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 16.69686499, 7.778e-05, 50.09059498, 0.00023334, 166.96864993, 0.00077778, -16.69686499, -7.778e-05, -50.09059498, -0.00023334, -166.96864993, -0.00077778, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 8.95)
    ops.node(124021, 9.0, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 28100852.55570283, 11708688.56487618, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 31.18590052, 0.00075228, 37.74537417, 0.01714457, 3.77453742, 0.06548595, -31.18590052, -0.00075228, -37.74537417, -0.01714457, -3.77453742, -0.06548595, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 28.86974207, 0.00075228, 34.94204748, 0.01714457, 3.49420475, 0.06548595, -28.86974207, -0.00075228, -34.94204748, -0.01714457, -3.49420475, -0.06548595, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 67.170242, 0.01504557, 67.170242, 0.04513671, 47.0191694, -875.04841193, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 16.7925605, 7.71e-05, 50.3776815, 0.00023131, 167.92560501, 0.00077102, -16.7925605, -7.71e-05, -50.3776815, -0.00023131, -167.92560501, -0.00077102, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 67.170242, 0.01504557, 67.170242, 0.04513671, 47.0191694, -875.04841193, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 16.7925605, 7.71e-05, 50.3776815, 0.00023131, 167.92560501, 0.00077102, -16.7925605, -7.71e-05, -50.3776815, -0.00023131, -167.92560501, -0.00077102, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 8.95)
    ops.node(124022, 12.0, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0625, 28728422.65247, 11970176.10519583, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 31.24832267, 0.00075308, 37.78864003, 0.01702979, 3.778864, 0.06650129, -31.24832267, -0.00075308, -37.78864003, -0.01702979, -3.778864, -0.06650129, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 28.95289113, 0.00075308, 35.01277148, 0.01702979, 3.50127715, 0.06650129, -28.95289113, -0.00075308, -35.01277148, -0.01702979, -3.50127715, -0.06650129, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 67.49879797, 0.01506169, 67.49879797, 0.04518507, 47.24915858, -846.90319716, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 16.87469949, 7.579e-05, 50.62409847, 0.00022736, 168.74699491, 0.00075787, -16.87469949, -7.579e-05, -50.62409847, -0.00022736, -168.74699491, -0.00075787, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 67.49879797, 0.01506169, 67.49879797, 0.04518507, 47.24915858, -846.90319716, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 16.87469949, 7.579e-05, 50.62409847, 0.00022736, 168.74699491, 0.00075787, -16.87469949, -7.579e-05, -50.62409847, -0.00022736, -168.74699491, -0.00075787, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 16.5, 13.5, 8.925)
    ops.node(124023, 16.5, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.0625, 28558418.57781001, 11899341.0740875, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 32.12050063, 0.00074703, 38.80094221, 0.01649856, 3.88009422, 0.06374693, -32.12050063, -0.00074703, -38.80094221, -0.01649856, -3.88009422, -0.06374693, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 29.86188086, 0.00074703, 36.0725733, 0.01649856, 3.60725733, 0.06374693, -29.86188086, -0.00074703, -36.0725733, -0.01649856, -3.60725733, -0.06374693, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 66.81699272, 0.01494068, 66.81699272, 0.04482204, 46.77189491, -801.0152783, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 16.70424818, 7.547e-05, 50.11274454, 0.0002264, 167.0424818, 0.00075468, -16.70424818, -7.547e-05, -50.11274454, -0.0002264, -167.0424818, -0.00075468, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 66.81699272, 0.01494068, 66.81699272, 0.04482204, 46.77189491, -801.0152783, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 16.70424818, 7.547e-05, 50.11274454, 0.0002264, 167.0424818, 0.00075468, -16.70424818, -7.547e-05, -50.11274454, -0.0002264, -167.0424818, -0.00075468, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 21.0, 13.5, 8.925)
    ops.node(124024, 21.0, 13.5, 11.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 27059614.77549736, 11274839.48979057, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 26.09872569, 0.0007137, 31.78149326, 0.01845221, 3.17814933, 0.07223605, -26.09872569, -0.0007137, -31.78149326, -0.01845221, -3.17814933, -0.07223605, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 23.85636279, 0.0007137, 29.0508756, 0.01845221, 2.90508756, 0.07223605, -23.85636279, -0.0007137, -29.0508756, -0.01845221, -2.90508756, -0.07223605, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 60.75206699, 0.01427406, 60.75206699, 0.04282217, 42.52644689, -923.19397629, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 15.18801675, 7.242e-05, 45.56405024, 0.00021726, 151.88016748, 0.00072419, -15.18801675, -7.242e-05, -45.56405024, -0.00021726, -151.88016748, -0.00072419, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 60.75206699, 0.01427406, 60.75206699, 0.04282217, 42.52644689, -923.19397629, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 15.18801675, 7.242e-05, 45.56405024, 0.00021726, 151.88016748, 0.00072419, -15.18801675, -7.242e-05, -45.56405024, -0.00021726, -151.88016748, -0.00072419, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(124025, 9.0, 0.0, 1.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.09, 27103750.5262708, 11293229.38594617, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 91.87139335, 0.00058876, 108.06998533, 0.01000795, 10.80699853, 0.0266786, -91.87139335, -0.00058876, -108.06998533, -0.01000795, -10.80699853, -0.0266786, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 87.95999557, 0.00058876, 103.46893722, 0.01000795, 10.34689372, 0.0266786, -87.95999557, -0.00058876, -103.46893722, -0.01000795, -10.34689372, -0.0266786, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 133.86546807, 0.01177518, 133.86546807, 0.03532554, 93.70582765, -2942.08683143, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 33.46636702, 6.124e-05, 100.39910105, 0.00018373, 334.66367017, 0.00061244, -33.46636702, -6.124e-05, -100.39910105, -0.00018373, -334.66367017, -0.00061244, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 133.86546807, 0.01177518, 133.86546807, 0.03532554, 93.70582765, -2942.08683143, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 33.46636702, 6.124e-05, 100.39910105, 0.00018373, 334.66367017, 0.00061244, -33.46636702, -6.124e-05, -100.39910105, -0.00018373, -334.66367017, -0.00061244, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.725)
    ops.node(121003, 9.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.09, 26094340.01984873, 10872641.67493697, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 87.59844083, 0.00057971, 103.0105804, 0.00973143, 10.30105804, 0.02517381, -87.59844083, -0.00057971, -103.0105804, -0.00973143, -10.30105804, -0.02517381, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 83.61124618, 0.00057971, 98.32187554, 0.00973143, 9.83218755, 0.02517381, -83.61124618, -0.00057971, -98.32187554, -0.00973143, -9.83218755, -0.02517381, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 126.86276216, 0.01159412, 126.86276216, 0.03478235, 88.80393351, -2806.19912125, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 31.71569054, 6.029e-05, 95.14707162, 0.00018086, 317.1569054, 0.00060285, -31.71569054, -6.029e-05, -95.14707162, -0.00018086, -317.1569054, -0.00060285, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 126.86276216, 0.01159412, 126.86276216, 0.03478235, 88.80393351, -2806.19912125, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 31.71569054, 6.029e-05, 95.14707162, 0.00018086, 317.1569054, 0.00060285, -31.71569054, -6.029e-05, -95.14707162, -0.00018086, -317.1569054, -0.00060285, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.0, 0.0, 0.0)
    ops.node(124026, 12.0, 0.0, 1.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.09, 27868054.16704732, 11611689.23626972, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 92.34034586, 0.00058247, 108.8247865, 0.01028971, 10.88247865, 0.02890697, -92.34034586, -0.00058247, -108.8247865, -0.01028971, -10.88247865, -0.02890697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 88.36341715, 0.00058247, 104.13790328, 0.01028971, 10.41379033, 0.02890697, -88.36341715, -0.00058247, -104.13790328, -0.01028971, -10.41379033, -0.02890697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 136.104503, 0.0116494, 136.104503, 0.03494819, 95.2731521, -2913.88785909, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 34.02612575, 6.056e-05, 102.07837725, 0.00018168, 340.2612575, 0.0006056, -34.02612575, -6.056e-05, -102.07837725, -0.00018168, -340.2612575, -0.0006056, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 136.104503, 0.0116494, 136.104503, 0.03494819, 95.2731521, -2913.88785909, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 34.02612575, 6.056e-05, 102.07837725, 0.00018168, 340.2612575, 0.0006056, -34.02612575, -6.056e-05, -102.07837725, -0.00018168, -340.2612575, -0.0006056, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.725)
    ops.node(121004, 12.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.09, 27362018.89853462, 11400841.20772276, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 87.80790622, 0.00057929, 103.63368469, 0.01025497, 10.36336847, 0.02899687, -87.80790622, -0.00057929, -103.63368469, -0.01025497, -10.36336847, -0.02899687, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 83.98011678, 0.00057929, 99.11600581, 0.01025497, 9.91160058, 0.02899687, -83.98011678, -0.00057929, -99.11600581, -0.01025497, -9.91160058, -0.02899687, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 130.74666619, 0.01158573, 130.74666619, 0.03475718, 91.52266633, -2769.77068409, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 32.68666655, 5.925e-05, 98.05999964, 0.00017776, 326.86666547, 0.00059252, -32.68666655, -5.925e-05, -98.05999964, -0.00017776, -326.86666547, -0.00059252, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 130.74666619, 0.01158573, 130.74666619, 0.03475718, 91.52266633, -2769.77068409, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 32.68666655, 5.925e-05, 98.05999964, 0.00017776, 326.86666547, 0.00059252, -32.68666655, -5.925e-05, -98.05999964, -0.00017776, -326.86666547, -0.00059252, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.35)
    ops.node(124027, 9.0, 0.0, 4.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.09, 27417827.12192842, 11424094.63413684, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 68.43257477, 0.00053796, 81.39947731, 0.01144524, 8.13994773, 0.03519342, -68.43257477, -0.00053796, -81.39947731, -0.01144524, -8.13994773, -0.03519342, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 68.43257477, 0.00053796, 81.39947731, 0.01144524, 8.13994773, 0.03519342, -68.43257477, -0.00053796, -81.39947731, -0.01144524, -8.13994773, -0.03519342, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 133.36228334, 0.0107593, 133.36228334, 0.03227789, 93.35359834, -2721.31010318, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 33.34057084, 5.448e-05, 100.02171251, 0.00016343, 333.40570835, 0.00054478, -33.34057084, -5.448e-05, -100.02171251, -0.00016343, -333.40570835, -0.00054478, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 133.36228334, 0.0107593, 133.36228334, 0.03227789, 93.35359834, -2721.31010318, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 33.34057084, 5.448e-05, 100.02171251, 0.00016343, 333.40570835, 0.00054478, -33.34057084, -5.448e-05, -100.02171251, -0.00016343, -333.40570835, -0.00054478, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.675)
    ops.node(122003, 9.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.09, 28172555.92647392, 11738564.96936413, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 64.68257338, 0.00053525, 77.17761066, 0.0122407, 7.71776107, 0.03977206, -64.68257338, -0.00053525, -77.17761066, -0.0122407, -7.71776107, -0.03977206, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 64.68257338, 0.00053525, 77.17761066, 0.0122407, 7.71776107, 0.03977206, -64.68257338, -0.00053525, -77.17761066, -0.0122407, -7.71776107, -0.03977206, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 133.82744436, 0.01070493, 133.82744436, 0.03211478, 93.67921105, -2630.01281224, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 33.45686109, 5.32e-05, 100.37058327, 0.00015961, 334.56861091, 0.00053203, -33.45686109, -5.32e-05, -100.37058327, -0.00015961, -334.56861091, -0.00053203, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 133.82744436, 0.01070493, 133.82744436, 0.03211478, 93.67921105, -2630.01281224, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 33.45686109, 5.32e-05, 100.37058327, 0.00015961, 334.56861091, 0.00053203, -33.45686109, -5.32e-05, -100.37058327, -0.00015961, -334.56861091, -0.00053203, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.35)
    ops.node(124028, 12.0, 0.0, 4.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.09, 27284827.22621747, 11368678.01092395, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 68.35783922, 0.00053726, 81.29643307, 0.01156335, 8.12964331, 0.03496726, -68.35783922, -0.00053726, -81.29643307, -0.01156335, -8.12964331, -0.03496726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 68.35783922, 0.00053726, 81.29643307, 0.01156335, 8.12964331, 0.03496726, -68.35783922, -0.00053726, -81.29643307, -0.01156335, -8.12964331, -0.03496726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 133.82710874, 0.01074525, 133.82710874, 0.03223576, 93.67897612, -2765.81117607, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 33.45677718, 5.493e-05, 100.37033155, 0.0001648, 334.56777185, 0.00054934, -33.45677718, -5.493e-05, -100.37033155, -0.0001648, -334.56777185, -0.00054934, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 133.82710874, 0.01074525, 133.82710874, 0.03223576, 93.67897612, -2765.81117607, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 33.45677718, 5.493e-05, 100.37033155, 0.0001648, 334.56777185, 0.00054934, -33.45677718, -5.493e-05, -100.37033155, -0.0001648, -334.56777185, -0.00054934, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.675)
    ops.node(122004, 12.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.09, 28391683.94148324, 11829868.30895135, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 64.48123956, 0.00053589, 76.94317114, 0.01248109, 7.69431711, 0.04054096, -64.48123956, -0.00053589, -76.94317114, -0.01248109, -7.69431711, -0.04054096, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 64.48123956, 0.00053589, 76.94317114, 0.01248109, 7.69431711, 0.04054096, -64.48123956, -0.00053589, -76.94317114, -0.01248109, -7.69431711, -0.04054096, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 135.34550446, 0.01071782, 135.34550446, 0.03215346, 94.74185312, -2658.6842075, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 33.83637612, 5.339e-05, 101.50912835, 0.00016017, 338.36376115, 0.00053391, -33.83637612, -5.339e-05, -101.50912835, -0.00016017, -338.36376115, -0.00053391, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 135.34550446, 0.01071782, 135.34550446, 0.03215346, 94.74185312, -2658.6842075, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 33.83637612, 5.339e-05, 101.50912835, 0.00016017, 338.36376115, 0.00053391, -33.83637612, -5.339e-05, -101.50912835, -0.00016017, -338.36376115, -0.00053391, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.15)
    ops.node(124029, 9.0, 0.0, 7.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.0625, 27592478.06136518, 11496865.85890216, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 41.25106151, 0.00059197, 49.15341644, 0.01260298, 4.91534164, 0.04182494, -41.25106151, -0.00059197, -49.15341644, -0.01260298, -4.91534164, -0.04182494, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 41.25106151, 0.00059197, 49.15341644, 0.01260298, 4.91534164, 0.04182494, -41.25106151, -0.00059197, -49.15341644, -0.01260298, -4.91534164, -0.04182494, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 84.02877209, 0.01183933, 84.02877209, 0.03551799, 58.82014046, -2024.85596333, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 21.00719302, 4.912e-05, 63.02157907, 0.00014735, 210.07193023, 0.00049115, -21.00719302, -4.912e-05, -63.02157907, -0.00014735, -210.07193023, -0.00049115, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 84.02877209, 0.01183933, 84.02877209, 0.03551799, 58.82014046, -2024.85596333, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 21.00719302, 4.912e-05, 63.02157907, 0.00014735, 210.07193023, 0.00049115, -21.00719302, -4.912e-05, -63.02157907, -0.00014735, -210.07193023, -0.00049115, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.475)
    ops.node(123003, 9.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.0625, 26936198.01713781, 11223415.84047409, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 37.54102761, 0.00056499, 44.89644329, 0.01346438, 4.48964433, 0.04458102, -37.54102761, -0.00056499, -44.89644329, -0.01346438, -4.48964433, -0.04458102, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 37.54102761, 0.00056499, 44.89644329, 0.01346438, 4.48964433, 0.04458102, -37.54102761, -0.00056499, -44.89644329, -0.01346438, -4.48964433, -0.04458102, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 80.05491493, 0.01129971, 80.05491493, 0.03389912, 56.03844045, -1932.52304874, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 20.01372873, 4.793e-05, 60.0411862, 0.0001438, 200.13728733, 0.00047933, -20.01372873, -4.793e-05, -60.0411862, -0.0001438, -200.13728733, -0.00047933, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 80.05491493, 0.01129971, 80.05491493, 0.03389912, 56.03844045, -1932.52304874, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 20.01372873, 4.793e-05, 60.0411862, 0.0001438, 200.13728733, 0.00047933, -20.01372873, -4.793e-05, -60.0411862, -0.0001438, -200.13728733, -0.00047933, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.15)
    ops.node(124030, 12.0, 0.0, 7.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.0625, 27907378.96014513, 11628074.56672714, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 40.94824788, 0.00059974, 48.80521753, 0.01304298, 4.88052175, 0.04317808, -40.94824788, -0.00059974, -48.80521753, -0.01304298, -4.88052175, -0.04317808, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 40.94824788, 0.00059974, 48.80521753, 0.01304298, 4.88052175, 0.04317808, -40.94824788, -0.00059974, -48.80521753, -0.01304298, -4.88052175, -0.04317808, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 85.36398933, 0.01199488, 85.36398933, 0.03598464, 59.75479253, -2052.97893573, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 21.34099733, 4.933e-05, 64.02299199, 0.000148, 213.40997331, 0.00049333, -21.34099733, -4.933e-05, -64.02299199, -0.000148, -213.40997331, -0.00049333, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 85.36398933, 0.01199488, 85.36398933, 0.03598464, 59.75479253, -2052.97893573, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 21.34099733, 4.933e-05, 64.02299199, 0.000148, 213.40997331, 0.00049333, -21.34099733, -4.933e-05, -64.02299199, -0.000148, -213.40997331, -0.00049333, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.475)
    ops.node(123004, 12.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.0625, 26633947.02369331, 11097477.92653888, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 36.91872324, 0.00056902, 44.13890039, 0.01329949, 4.41389004, 0.04351564, -36.91872324, -0.00056902, -44.13890039, -0.01329949, -4.41389004, -0.04351564, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 36.91872324, 0.00056902, 44.13890039, 0.01329949, 4.41389004, 0.04351564, -36.91872324, -0.00056902, -44.13890039, -0.01329949, -4.41389004, -0.04351564, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 79.69642883, 0.01138045, 79.69642883, 0.03414134, 55.78750018, -1948.46857143, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 19.92410721, 4.826e-05, 59.77232162, 0.00014478, 199.24107208, 0.0004826, -19.92410721, -4.826e-05, -59.77232162, -0.00014478, -199.24107208, -0.0004826, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 79.69642883, 0.01138045, 79.69642883, 0.03414134, 55.78750018, -1948.46857143, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 19.92410721, 4.826e-05, 59.77232162, 0.00014478, 199.24107208, 0.0004826, -19.92410721, -4.826e-05, -59.77232162, -0.00014478, -199.24107208, -0.0004826, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 8.95)
    ops.node(124031, 9.0, 0.0, 9.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.0625, 27861423.66400119, 11608926.52666716, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 24.96059728, 0.00053524, 30.22613921, 0.01605935, 3.02261392, 0.06427426, -24.96059728, -0.00053524, -30.22613921, -0.01605935, -3.02261392, -0.06427426, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 24.96059728, 0.00053524, 30.22613921, 0.01605935, 3.02261392, 0.06427426, -24.96059728, -0.00053524, -30.22613921, -0.01605935, -3.02261392, -0.06427426, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 71.13583722, 0.01070472, 71.13583722, 0.03211415, 49.79508606, -1673.6491994, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 17.78395931, 4.118e-05, 53.35187792, 0.00012353, 177.83959306, 0.00041178, -17.78395931, -4.118e-05, -53.35187792, -0.00012353, -177.83959306, -0.00041178, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 71.13583722, 0.01070472, 71.13583722, 0.03211415, 49.79508606, -1673.6491994, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 17.78395931, 4.118e-05, 53.35187792, 0.00012353, 177.83959306, 0.00041178, -17.78395931, -4.118e-05, -53.35187792, -0.00012353, -177.83959306, -0.00041178, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 9.0, 0.0, 10.275)
    ops.node(124003, 9.0, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.0625, 26972935.61399165, 11238723.17249652, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 21.13096354, 0.00050431, 25.72401493, 0.01759213, 2.57240149, 0.07056115, -21.13096354, -0.00050431, -25.72401493, -0.01759213, -2.57240149, -0.07056115, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 21.13096354, 0.00050431, 25.72401493, 0.01759213, 2.57240149, 0.07056115, -21.13096354, -0.00050431, -25.72401493, -0.01759213, -2.57240149, -0.07056115, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 65.55631581, 0.01008627, 65.55631581, 0.0302588, 45.88942107, -1784.24743571, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 16.38907895, 3.92e-05, 49.16723686, 0.00011759, 163.89078953, 0.00039198, -16.38907895, -3.92e-05, -49.16723686, -0.00011759, -163.89078953, -0.00039198, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 65.55631581, 0.01008627, 65.55631581, 0.0302588, 45.88942107, -1784.24743571, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 16.38907895, 3.92e-05, 49.16723686, 0.00011759, 163.89078953, 0.00039198, -16.38907895, -3.92e-05, -49.16723686, -0.00011759, -163.89078953, -0.00039198, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 8.95)
    ops.node(124032, 12.0, 0.0, 9.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.0625, 27579151.78036499, 11491313.24181875, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 24.91607652, 0.00052802, 30.1816281, 0.01622372, 3.01816281, 0.06389538, -24.91607652, -0.00052802, -30.1816281, -0.01622372, -3.01816281, -0.06389538, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 24.91607652, 0.00052802, 30.1816281, 0.01622372, 3.01816281, 0.06389538, -24.91607652, -0.00052802, -30.1816281, -0.01622372, -3.01816281, -0.06389538, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 70.52452742, 0.01056038, 70.52452742, 0.03168113, 49.36716919, -1672.39121851, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 17.63113185, 4.124e-05, 52.89339556, 0.00012373, 176.31131854, 0.00041242, -17.63113185, -4.124e-05, -52.89339556, -0.00012373, -176.31131854, -0.00041242, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 70.52452742, 0.01056038, 70.52452742, 0.03168113, 49.36716919, -1672.39121851, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 17.63113185, 4.124e-05, 52.89339556, 0.00012373, 176.31131854, 0.00041242, -17.63113185, -4.124e-05, -52.89339556, -0.00012373, -176.31131854, -0.00041242, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 12.0, 0.0, 10.275)
    ops.node(124004, 12.0, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.0625, 27046303.47489247, 11269293.11453853, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 20.81004221, 0.00051368, 25.33084504, 0.017483, 2.5330845, 0.07056393, -20.81004221, -0.00051368, -25.33084504, -0.017483, -2.5330845, -0.07056393, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 20.81004221, 0.00051368, 25.33084504, 0.017483, 2.5330845, 0.07056393, -20.81004221, -0.00051368, -25.33084504, -0.017483, -2.5330845, -0.07056393, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 66.51027591, 0.01027361, 66.51027591, 0.03082084, 46.55719314, -1854.22643098, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 16.62756898, 3.966e-05, 49.88270693, 0.00011898, 166.27568978, 0.00039661, -16.62756898, -3.966e-05, -49.88270693, -0.00011898, -166.27568978, -0.00039661, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 66.51027591, 0.01027361, 66.51027591, 0.03082084, 46.55719314, -1854.22643098, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 16.62756898, 3.966e-05, 49.88270693, 0.00011898, 166.27568978, 0.00039661, -16.62756898, -3.966e-05, -49.88270693, -0.00011898, -166.27568978, -0.00039661, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
