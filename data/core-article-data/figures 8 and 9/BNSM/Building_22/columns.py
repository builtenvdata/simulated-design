import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.075, 24563224.2069678, 10234676.75290325, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 56.17241102, 0.00065471, 66.08813386, 0.00711487, 6.60881339, 0.01960362, -56.17241102, -0.00065471, -66.08813386, -0.00711487, -6.60881339, -0.01960362, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 64.91034778, 0.00059312, 76.36851748, 0.00743563, 7.63685175, 0.0217494, -64.91034778, -0.00059312, -76.36851748, -0.00743563, -7.63685175, -0.0217494, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 64.81878889, 0.01309426, 64.81878889, 0.03928278, 45.37315222, -1268.14130501, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 16.20469722, 6.967e-05, 48.61409167, 0.000209, 162.04697223, 0.00069666, -16.20469722, -6.967e-05, -48.61409167, -0.000209, -162.04697223, -0.00069666, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 87.25639388, 0.01186245, 87.25639388, 0.03558736, 61.07947572, -1397.89973881, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 21.81409847, 9.378e-05, 65.44229541, 0.00028134, 218.14098471, 0.00093781, -21.81409847, -9.378e-05, -65.44229541, -0.00028134, -218.14098471, -0.00093781, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 14.65, 0.0, 0.0)
    ops.node(121004, 14.65, 0.0, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.075, 27810128.47716095, 11587553.5321504, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 90.85925381, 0.00123089, 107.85736572, 0.01085134, 10.78573657, 0.03092162, -90.85925381, -0.00123089, -107.85736572, -0.01085134, -10.78573657, -0.03092162, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 102.15162071, 0.00103715, 121.26232885, 0.01122698, 12.12623288, 0.03423022, -102.15162071, -0.00103715, -121.26232885, -0.01122698, -12.12623288, -0.03423022, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 97.90597969, 0.02461774, 97.90597969, 0.07385321, 68.53418578, -1422.29838863, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 24.47649492, 9.294e-05, 73.42948476, 0.00027882, 244.76494921, 0.00092942, -24.47649492, -9.294e-05, -73.42948476, -0.00027882, -244.76494921, -0.00092942, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 107.09982822, 0.02074293, 107.09982822, 0.06222878, 74.96987976, -1592.91802679, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 26.77495706, 0.00010167, 80.32487117, 0.00030501, 267.74957056, 0.00101669, -26.77495706, -0.00010167, -80.32487117, -0.00030501, -267.74957056, -0.00101669, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.15, 0.0)
    ops.node(121005, 0.0, 4.15, 2.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.14, 27334274.68746622, 11389281.11977759, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 233.2659833, 0.0007985, 278.33720092, 0.00888706, 27.83372009, 0.02914707, -233.2659833, -0.0007985, -278.33720092, -0.00888706, -27.83372009, -0.02914707, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 216.03908789, 0.00087417, 257.78175695, 0.00865824, 25.77817569, 0.02715559, -216.03908789, -0.00087417, -257.78175695, -0.00865824, -25.77817569, -0.02715559, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 158.0455514, 0.01597006, 158.0455514, 0.04791019, 110.63188598, -2013.21353489, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 39.51138785, 8.177e-05, 118.53416355, 0.00024532, 395.11387849, 0.00081773, -39.51138785, -8.177e-05, -118.53416355, -0.00024532, -395.11387849, -0.00081773, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 152.29821578, 0.01748346, 152.29821578, 0.05245038, 106.60875105, -1883.46215094, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 38.07455394, 7.88e-05, 114.22366183, 0.0002364, 380.74553945, 0.000788, -38.07455394, -7.88e-05, -114.22366183, -0.0002364, -380.74553945, -0.000788, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 5.9, 4.15, 0.0)
    ops.node(121006, 5.9, 4.15, 2.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.2475, 27271838.44193284, 11363266.01747202, 0.00841652, 0.00459422, 0.00686297, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 460.26787315, 0.00065471, 554.34286012, 0.00925745, 55.43428601, 0.02818318, -460.26787315, -0.00065471, -554.34286012, -0.00925745, -55.43428601, -0.02818318, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 484.27428081, 0.00072496, 583.25598105, 0.00894174, 58.32559811, 0.02591502, -484.27428081, -0.00072496, -583.25598105, -0.00894174, -58.32559811, -0.02591502, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 274.89155688, 0.0130943, 274.89155688, 0.03928289, 192.42408981, -2337.65985397, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 68.72288922, 8.064e-05, 206.16866766, 0.00024191, 687.2288922, 0.00080637, -68.72288922, -8.064e-05, -206.16866766, -0.00024191, -687.2288922, -0.00080637, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 224.91127381, 0.01449928, 224.91127381, 0.04349784, 157.43789167, -2119.7016635, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 56.22781845, 6.598e-05, 168.68345536, 0.00019793, 562.27818452, 0.00065976, -56.22781845, -6.598e-05, -168.68345536, -0.00019793, -562.27818452, -0.00065976, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 8.75, 4.15, 0.0)
    ops.node(121007, 8.75, 4.15, 2.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.2475, 26885105.66811134, 11202127.36171306, 0.00841652, 0.00459422, 0.00686297, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 457.0680478, 0.00066896, 550.5032909, 0.009859, 55.05032909, 0.02829951, -457.0680478, -0.00066896, -550.5032909, -0.009859, -55.05032909, -0.02829951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 474.38471493, 0.00074552, 571.35988388, 0.00952326, 57.13598839, 0.02606136, -474.38471493, -0.00074552, -571.35988388, -0.00952326, -57.13598839, -0.02606136, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 273.11101443, 0.01337926, 273.11101443, 0.04013779, 191.1777101, -2381.96644889, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 68.27775361, 8.127e-05, 204.83326082, 0.0002438, 682.77753608, 0.00081268, -68.27775361, -8.127e-05, -204.83326082, -0.0002438, -682.77753608, -0.00081268, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 223.45446635, 0.01491043, 223.45446635, 0.04473129, 156.41812645, -2154.19838486, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 55.86361659, 6.649e-05, 167.59084976, 0.00019948, 558.63616588, 0.00066492, -55.86361659, -6.649e-05, -167.59084976, -0.00019948, -558.63616588, -0.00066492, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 14.65, 4.15, 0.0)
    ops.node(121008, 14.65, 4.15, 2.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.14, 26269377.68789311, 10945574.03662213, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 233.06601736, 0.00081654, 277.70465068, 0.00964079, 27.77046507, 0.02771483, -233.06601736, -0.00081654, -277.70465068, -0.00964079, -27.77046507, -0.02771483, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 215.57452572, 0.0008961, 256.86305124, 0.00938817, 25.68630512, 0.02588973, -215.57452572, -0.0008961, -256.86305124, -0.00938817, -25.68630512, -0.02588973, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 161.09260811, 0.01633084, 161.09260811, 0.04899252, 112.76482567, -2196.72260508, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 40.27315203, 8.673e-05, 120.81945608, 0.00026019, 402.73152026, 0.00086729, -40.27315203, -8.673e-05, -120.81945608, -0.00026019, -402.73152026, -0.00086729, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 154.36764256, 0.01792208, 154.36764256, 0.05376623, 108.05734979, -2038.44909182, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 38.59191064, 8.311e-05, 115.77573192, 0.00024932, 385.91910639, 0.00083108, -38.59191064, -8.311e-05, -115.77573192, -0.00024932, -385.91910639, -0.00083108, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.3, 0.0)
    ops.node(121009, 0.0, 8.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.09, 28110010.77032863, 11712504.48763693, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 105.64131823, 0.00100996, 126.06123729, 0.0094833, 12.60612373, 0.0334628, -105.64131823, -0.00100996, -126.06123729, -0.0094833, -12.60612373, -0.0334628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 100.60965156, 0.00100996, 120.05697555, 0.0094833, 12.00569755, 0.0334628, -100.60965156, -0.00100996, -120.05697555, -0.0094833, -12.00569755, -0.0334628, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 108.32966628, 0.02019926, 108.32966628, 0.06059778, 75.8307664, -1425.15475301, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 27.08241657, 8.478e-05, 81.24724971, 0.00025435, 270.82416571, 0.00084783, -27.08241657, -8.478e-05, -81.24724971, -0.00025435, -270.82416571, -0.00084783, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 108.32966628, 0.02019926, 108.32966628, 0.06059778, 75.8307664, -1425.15475301, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 27.08241657, 8.478e-05, 81.24724971, 0.00025435, 270.82416571, 0.00084783, -27.08241657, -8.478e-05, -81.24724971, -0.00025435, -270.82416571, -0.00084783, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 5.9, 8.3, 0.0)
    ops.node(121010, 5.9, 8.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.105, 26746085.64158459, 11144202.35066025, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 143.17266758, 0.00104619, 170.29330088, 0.00900351, 17.02933009, 0.02916581, -143.17266758, -0.00104619, -170.29330088, -0.00900351, -17.02933009, -0.02916581, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 149.26922649, 0.0009245, 177.54470687, 0.00927976, 17.75447069, 0.03191644, -149.26922649, -0.0009245, -177.54470687, -0.00927976, -17.75447069, -0.03191644, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 129.36352488, 0.02092383, 129.36352488, 0.06277149, 90.55446741, -1815.49503149, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 32.34088122, 9.121e-05, 97.02264366, 0.00027362, 323.40881219, 0.00091207, -32.34088122, -9.121e-05, -97.02264366, -0.00027362, -323.40881219, -0.00091207, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 136.84732925, 0.01848998, 136.84732925, 0.05546995, 95.79313047, -2000.70383503, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 34.21183231, 9.648e-05, 102.63549694, 0.00028945, 342.11832312, 0.00096483, -34.21183231, -9.648e-05, -102.63549694, -0.00028945, -342.11832312, -0.00096483, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.75, 8.3, 0.0)
    ops.node(121011, 8.75, 8.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.105, 26590806.84649917, 11079502.85270799, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 147.91857444, 0.00104851, 175.8904656, 0.00931092, 17.58904656, 0.02910458, -147.91857444, -0.00104851, -175.8904656, -0.00931092, -17.58904656, -0.02910458, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 153.02648578, 0.00092961, 181.96429985, 0.00960522, 18.19642999, 0.03182802, -153.02648578, -0.00092961, -181.96429985, -0.00960522, -18.19642999, -0.03182802, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 133.32881858, 0.02097015, 133.32881858, 0.06291046, 93.33017301, -1925.64581565, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 33.33220464, 9.455e-05, 99.99661393, 0.00028365, 333.32204645, 0.00094551, -33.33220464, -9.455e-05, -99.99661393, -0.00028365, -333.32204645, -0.00094551, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 141.56170555, 0.01859221, 141.56170555, 0.05577663, 99.09319389, -2135.83010003, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 35.39042639, 0.00010039, 106.17127917, 0.00030117, 353.90426389, 0.0010039, -35.39042639, -0.00010039, -106.17127917, -0.00030117, -353.90426389, -0.0010039, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 14.65, 8.3, 0.0)
    ops.node(121012, 14.65, 8.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.09, 28118265.11555659, 11715943.79814858, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 104.52070354, 0.00095729, 124.72446606, 0.01071453, 12.47244661, 0.03471157, -104.52070354, -0.00095729, -124.72446606, -0.01071453, -12.47244661, -0.03471157, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 99.31904505, 0.00095729, 118.51733144, 0.01071453, 11.85173314, 0.03471157, -99.31904505, -0.00095729, -118.51733144, -0.01071453, -11.85173314, -0.03471157, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 116.53881821, 0.01914579, 116.53881821, 0.05743738, 81.57717275, -1599.02519231, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 29.13470455, 9.118e-05, 87.40411366, 0.00027354, 291.34704552, 0.00091181, -29.13470455, -9.118e-05, -87.40411366, -0.00027354, -291.34704552, -0.00091181, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 116.53881821, 0.01914579, 116.53881821, 0.05743738, 81.57717275, -1599.02519231, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 29.13470455, 9.118e-05, 87.40411366, 0.00027354, 291.34704552, 0.00091181, -29.13470455, -9.118e-05, -87.40411366, -0.00027354, -291.34704552, -0.00091181, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.05)
    ops.node(122001, 0.0, 0.0, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.075, 27724003.17264619, 11551667.98860258, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 92.62613735, 0.00116611, 110.88521913, 0.01070574, 11.08852191, 0.03634444, -92.62613735, -0.00116611, -110.88521913, -0.01070574, -11.08852191, -0.03634444, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 98.59417942, 0.00099169, 118.02972144, 0.01109593, 11.80297214, 0.04048132, -98.59417942, -0.00099169, -118.02972144, -0.01109593, -11.80297214, -0.04048132, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 70.46034432, 0.02332213, 70.46034432, 0.06996638, 49.32224103, -1192.59205062, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 17.61508608, 6.71e-05, 52.84525824, 0.00020129, 176.1508608, 0.00067095, -17.61508608, -6.71e-05, -52.84525824, -0.00020129, -176.1508608, -0.00067095, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 95.73567305, 0.01983385, 95.73567305, 0.05950155, 67.01497114, -1360.20231059, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 23.93391826, 9.116e-05, 71.80175479, 0.00027349, 239.33918264, 0.00091164, -23.93391826, -9.116e-05, -71.80175479, -0.00027349, -239.33918264, -0.00091164, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 14.65, 0.0, 3.05)
    ops.node(122004, 14.65, 0.0, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.075, 25831942.59450376, 10763309.41437657, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 89.58781145, 0.00129156, 107.05646279, 0.01018718, 10.70564628, 0.03158441, -89.58781145, -0.00129156, -107.05646279, -0.01018718, -10.70564628, -0.03158441, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 97.18961653, 0.00107828, 116.14053739, 0.01050038, 11.61405374, 0.03502448, -97.18961653, -0.00107828, -116.14053739, -0.01050038, -11.61405374, -0.03502448, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 66.88833503, 0.02583128, 66.88833503, 0.07749385, 46.82183452, -1167.26945794, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 16.72208376, 6.836e-05, 50.16625128, 0.00020508, 167.22083759, 0.00068359, -16.72208376, -6.836e-05, -50.16625128, -0.00020508, -167.22083759, -0.00068359, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 90.84929573, 0.02156556, 90.84929573, 0.06469667, 63.59450701, -1327.77155804, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 22.71232393, 9.285e-05, 68.13697179, 0.00027854, 227.12323932, 0.00092847, -22.71232393, -9.285e-05, -68.13697179, -0.00027854, -227.12323932, -0.00092847, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.15, 3.025)
    ops.node(122005, 0.0, 4.15, 5.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.14, 27659086.01206975, 11524619.17169573, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 201.13312795, 0.00075206, 241.69818262, 0.01161795, 24.16981826, 0.03721928, -201.13312795, -0.00075206, -241.69818262, -0.01161795, -24.16981826, -0.03721928, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 160.4373557, 0.00081917, 192.79478071, 0.01127602, 19.27947807, 0.03464999, -160.4373557, -0.00081917, -192.79478071, -0.01127602, -19.27947807, -0.03464999, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 159.77442795, 0.01504123, 159.77442795, 0.0451237, 111.84209956, -2055.42606554, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 39.94360699, 8.17e-05, 119.83082096, 0.00024509, 399.43606987, 0.00081697, -39.94360699, -8.17e-05, -119.83082096, -0.00024509, -399.43606987, -0.00081697, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 152.68230461, 0.01638348, 152.68230461, 0.04915044, 106.87761323, -1868.4557411, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 38.17057615, 7.807e-05, 114.51172846, 0.00023421, 381.70576154, 0.00078071, -38.17057615, -7.807e-05, -114.51172846, -0.00023421, -381.70576154, -0.00078071, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 5.9, 4.15, 3.025)
    ops.node(122006, 5.9, 4.15, 5.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.2475, 26153874.46889042, 10897447.69537101, 0.00841652, 0.00459422, 0.00686297, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 321.85307268, 0.0006361, 389.57230614, 0.00798851, 38.95723061, 0.02835809, -321.85307268, -0.0006361, -389.57230614, -0.00798851, -38.95723061, -0.02835809, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 244.03308314, 0.00070052, 295.37866512, 0.00772307, 29.53786651, 0.02599123, -244.03308314, -0.00070052, -295.37866512, -0.00772307, -29.53786651, -0.02599123, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 240.79687644, 0.01272209, 240.79687644, 0.03816628, 168.55781351, -1901.00844392, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 60.19921911, 7.366e-05, 180.59765733, 0.00022097, 601.99219109, 0.00073655, -60.19921911, -7.366e-05, -180.59765733, -0.00022097, -601.99219109, -0.00073655, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 197.01562618, 0.01401039, 197.01562618, 0.04203117, 137.91093832, -1704.48795211, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 49.25390654, 6.026e-05, 147.76171963, 0.00018079, 492.53906544, 0.00060264, -49.25390654, -6.026e-05, -147.76171963, -0.00018079, -492.53906544, -0.00060264, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 8.75, 4.15, 3.025)
    ops.node(122007, 8.75, 4.15, 5.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.2475, 28943108.3151231, 12059628.46463462, 0.00841652, 0.00459422, 0.00686297, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 311.81344306, 0.0006173, 376.54205763, 0.00991058, 37.65420576, 0.03314564, -311.81344306, -0.0006173, -376.54205763, -0.00991058, -37.65420576, -0.03314564, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 237.13693066, 0.00067933, 286.36362478, 0.00955568, 28.63636248, 0.0303937, -237.13693066, -0.00067933, -286.36362478, -0.00955568, -28.63636248, -0.0303937, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 278.03642567, 0.01234592, 278.03642567, 0.03703777, 194.62549797, -2175.94450115, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 69.50910642, 7.685e-05, 208.52731926, 0.00023055, 695.09106418, 0.0007685, -69.50910642, -7.685e-05, -208.52731926, -0.00023055, -695.09106418, -0.0007685, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 227.48434828, 0.01358655, 227.48434828, 0.04075966, 159.23904379, -1916.51388408, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 56.87108707, 6.288e-05, 170.61326121, 0.00018863, 568.7108707, 0.00062878, -56.87108707, -6.288e-05, -170.61326121, -0.00018863, -568.7108707, -0.00062878, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 14.65, 4.15, 3.025)
    ops.node(122008, 14.65, 4.15, 5.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.14, 29403977.48437407, 12251657.28515586, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 204.50343533, 0.00077864, 245.49403768, 0.01124384, 24.54940377, 0.03969492, -204.50343533, -0.00077864, -245.49403768, -0.01124384, -24.54940377, -0.03969492, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 163.54819633, 0.00085162, 196.32974384, 0.01092285, 19.63297438, 0.03689865, -163.54819633, -0.00085162, -196.32974384, -0.01092285, -19.63297438, -0.03689865, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 163.49862403, 0.01557278, 163.49862403, 0.04671834, 114.44903682, -1950.32356078, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 40.87465601, 7.864e-05, 122.62396802, 0.00023592, 408.74656008, 0.0007864, -40.87465601, -7.864e-05, -122.62396802, -0.00023592, -408.74656008, -0.0007864, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 156.8996254, 0.01703231, 156.8996254, 0.05109692, 109.82973778, -1780.67886406, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 39.22490635, 7.547e-05, 117.67471905, 0.0002264, 392.24906349, 0.00075466, -39.22490635, -7.547e-05, -117.67471905, -0.0002264, -392.24906349, -0.00075466, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.3, 3.05)
    ops.node(122009, 0.0, 8.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.09, 27578734.12184899, 11491139.21743708, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 104.92066688, 0.0009919, 126.07685204, 0.01235616, 12.6076852, 0.04073723, -104.92066688, -0.0009919, -126.07685204, -0.01235616, -12.6076852, -0.04073723, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 94.97474806, 0.0009919, 114.12543986, 0.01235616, 11.41254399, 0.04073723, -94.97474806, -0.0009919, -114.12543986, -0.01235616, -11.41254399, -0.04073723, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 109.34780145, 0.01983799, 109.34780145, 0.05951396, 76.54346101, -1512.26637326, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 27.33695036, 8.723e-05, 82.01085109, 0.00026169, 273.36950362, 0.00087229, -27.33695036, -8.723e-05, -82.01085109, -0.00026169, -273.36950362, -0.00087229, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 109.34780145, 0.01983799, 109.34780145, 0.05951396, 76.54346101, -1512.26637326, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 27.33695036, 8.723e-05, 82.01085109, 0.00026169, 273.36950362, 0.00087229, -27.33695036, -8.723e-05, -82.01085109, -0.00026169, -273.36950362, -0.00087229, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 5.9, 8.3, 3.05)
    ops.node(122010, 5.9, 8.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.105, 29347858.64705681, 12228274.43627367, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 110.18925094, 0.00097294, 132.11847835, 0.01009327, 13.21184783, 0.04123882, -110.18925094, -0.00097294, -132.11847835, -0.01009327, -13.21184783, -0.04123882, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 111.59991977, 0.00086375, 133.80989032, 0.01044019, 13.38098903, 0.04540802, -111.59991977, -0.00086375, -133.80989032, -0.01044019, -13.38098903, -0.04540802, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 130.27910859, 0.01945887, 130.27910859, 0.05837662, 91.19537601, -1653.76709282, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 32.56977715, 8.371e-05, 97.70933144, 0.00025113, 325.69777147, 0.00083709, -32.56977715, -8.371e-05, -97.70933144, -0.00025113, -325.69777147, -0.00083709, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 137.87205088, 0.01727504, 137.87205088, 0.05182512, 96.51043561, -1864.42648925, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 34.46801272, 8.859e-05, 103.40403816, 0.00026576, 344.68012719, 0.00088588, -34.46801272, -8.859e-05, -103.40403816, -0.00026576, -344.68012719, -0.00088588, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.75, 8.3, 3.05)
    ops.node(122011, 8.75, 8.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.105, 25367381.45314012, 10569742.27214172, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 105.00538972, 0.00094671, 125.75836837, 0.00868433, 12.57583684, 0.03136925, -105.00538972, -0.00094671, -125.75836837, -0.00868433, -12.57583684, -0.03136925, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 105.9176172, 0.0008414, 126.85088601, 0.00896598, 12.6850886, 0.03443486, -105.9176172, -0.0008414, -126.85088601, -0.00896598, -12.6850886, -0.03443486, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 114.24284129, 0.01893429, 114.24284129, 0.05680287, 79.9699889, -1573.35869756, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 28.56071032, 8.492e-05, 85.68213097, 0.00025477, 285.60710322, 0.00084924, -28.56071032, -8.492e-05, -85.68213097, -0.00025477, -285.60710322, -0.00084924, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 121.33162154, 0.01682806, 121.33162154, 0.05048418, 84.93213508, -1764.94351259, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 30.33290538, 9.019e-05, 90.99871615, 0.00027058, 303.32905385, 0.00090193, -30.33290538, -9.019e-05, -90.99871615, -0.00027058, -303.32905385, -0.00090193, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 14.65, 8.3, 3.05)
    ops.node(122012, 14.65, 8.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.09, 27624437.34542678, 11510182.22726116, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 104.32524817, 0.00095513, 125.3608769, 0.010082, 12.53608769, 0.03855366, -104.32524817, -0.00095513, -125.3608769, -0.010082, -12.53608769, -0.03855366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 94.10761021, 0.00095513, 113.08300479, 0.010082, 11.30830048, 0.03855366, -94.10761021, -0.00095513, -113.08300479, -0.010082, -11.30830048, -0.03855366, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 93.13504713, 0.01910253, 93.13504713, 0.05730758, 65.19453299, -1245.00409816, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 23.28376178, 7.417e-05, 69.85128535, 0.00022252, 232.83761782, 0.00074172, -23.28376178, -7.417e-05, -69.85128535, -0.00022252, -232.83761782, -0.00074172, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 93.13504713, 0.01910253, 93.13504713, 0.05730758, 65.19453299, -1245.00409816, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 23.28376178, 7.417e-05, 69.85128535, 0.00022252, 232.83761782, 0.00074172, -23.28376178, -7.417e-05, -69.85128535, -0.00022252, -232.83761782, -0.00074172, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.8)
    ops.node(123001, 0.0, 0.0, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 25208998.17220958, 10503749.23842066, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 54.23895217, 0.00116697, 65.23818917, 0.0112911, 6.52381892, 0.03996968, -54.23895217, -0.00116697, -65.23818917, -0.0112911, -6.52381892, -0.03996968, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 54.23895217, 0.00116697, 65.23818917, 0.0112911, 6.52381892, 0.03996968, -54.23895217, -0.00116697, -65.23818917, -0.0112911, -6.52381892, -0.03996968, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 59.68258033, 0.02333933, 59.68258033, 0.07001799, 41.77780623, -1144.95299718, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 14.92064508, 7.5e-05, 44.76193525, 0.00022501, 149.20645083, 0.00075003, -14.92064508, -7.5e-05, -44.76193525, -0.00022501, -149.20645083, -0.00075003, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 59.68258033, 0.02333933, 59.68258033, 0.07001799, 41.77780623, -1144.95299718, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 14.92064508, 7.5e-05, 44.76193525, 0.00022501, 149.20645083, 0.00075003, -14.92064508, -7.5e-05, -44.76193525, -0.00022501, -149.20645083, -0.00075003, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 14.65, 0.0, 5.8)
    ops.node(123004, 14.65, 0.0, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 27304250.14761152, 11376770.89483813, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 51.92139785, 0.00114432, 62.51305691, 0.01315628, 6.25130569, 0.04697047, -51.92139785, -0.00114432, -62.51305691, -0.01315628, -6.25130569, -0.04697047, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 51.92139785, 0.00114432, 62.51305691, 0.01315628, 6.25130569, 0.04697047, -51.92139785, -0.00114432, -62.51305691, -0.01315628, -6.25130569, -0.04697047, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 77.95504068, 0.02288648, 77.95504068, 0.06865943, 54.56852847, -1268.51639687, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 19.48876017, 9.045e-05, 58.46628051, 0.00027134, 194.88760169, 0.00090448, -19.48876017, -9.045e-05, -58.46628051, -0.00027134, -194.88760169, -0.00090448, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 77.95504068, 0.02288648, 77.95504068, 0.06865943, 54.56852847, -1268.51639687, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 19.48876017, 9.045e-05, 58.46628051, 0.00027134, 194.88760169, 0.00090448, -19.48876017, -9.045e-05, -58.46628051, -0.00027134, -194.88760169, -0.00090448, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.15, 5.775)
    ops.node(123005, 0.0, 4.15, 7.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0875, 25529056.92288116, 10637107.05120048, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 92.40070658, 0.00085394, 110.80501665, 0.01065817, 11.08050166, 0.03738018, -92.40070658, -0.00085394, -110.80501665, -0.01065817, -11.08050166, -0.03738018, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 63.33551587, 0.0011438, 75.95064097, 0.00998091, 7.5950641, 0.03086806, -63.33551587, -0.0011438, -75.95064097, -0.00998091, -7.5950641, -0.03086806, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 104.84107263, 0.01707878, 104.84107263, 0.05123633, 73.38875084, -1575.71138539, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 26.21026816, 9.293e-05, 78.63080447, 0.00027879, 262.10268157, 0.0009293, -26.21026816, -9.293e-05, -78.63080447, -0.00027879, -262.10268157, -0.0009293, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 78.0209478, 0.02287604, 78.0209478, 0.06862813, 54.61466346, -1218.00933664, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 19.50523695, 6.916e-05, 58.51571085, 0.00020747, 195.0523695, 0.00069157, -19.50523695, -6.916e-05, -58.51571085, -0.00020747, -195.0523695, -0.00069157, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 5.9, 4.15, 5.775)
    ops.node(123006, 5.9, 4.15, 7.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.175, 25777876.2481099, 10740781.77004579, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 202.31371874, 0.00065863, 245.08328657, 0.00991289, 24.50832866, 0.03361662, -202.31371874, -0.00065863, -245.08328657, -0.00991289, -24.50832866, -0.03361662, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 136.85217621, 0.00081714, 165.78302909, 0.00929076, 16.57830291, 0.02852303, -136.85217621, -0.00081714, -165.78302909, -0.00929076, -16.57830291, -0.02852303, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 171.70445212, 0.01317261, 171.70445212, 0.03951782, 120.19311648, -1783.41738387, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 42.92611303, 7.536e-05, 128.77833909, 0.00022609, 429.2611303, 0.00075364, -42.92611303, -7.536e-05, -128.77833909, -0.00022609, -429.2611303, -0.00075364, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 135.74207344, 0.01634271, 135.74207344, 0.04902812, 95.01945141, -1380.43376366, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 33.93551836, 5.958e-05, 101.80655508, 0.00017874, 339.35518359, 0.00059579, -33.93551836, -5.958e-05, -101.80655508, -0.00017874, -339.35518359, -0.00059579, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 8.75, 4.15, 5.775)
    ops.node(123007, 8.75, 4.15, 7.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.175, 28011290.64789016, 11671371.10328757, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 203.2567275, 0.00066535, 245.88464081, 0.01003702, 24.58846408, 0.0365193, -203.2567275, -0.00066535, -245.88464081, -0.01003702, -24.58846408, -0.0365193, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 137.17769671, 0.00083105, 165.94721905, 0.00941217, 16.59472191, 0.03089885, -137.17769671, -0.00083105, -165.94721905, -0.00941217, -16.59472191, -0.03089885, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 184.81415928, 0.013307, 184.81415928, 0.03992099, 129.36991149, -1780.12798077, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 46.20353982, 7.465e-05, 138.61061946, 0.00022395, 462.0353982, 0.0007465, -46.20353982, -7.465e-05, -138.61061946, -0.00022395, -462.0353982, -0.0007465, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 146.46207624, 0.01662091, 146.46207624, 0.04986274, 102.52345337, -1378.40777325, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 36.61551906, 5.916e-05, 109.84655718, 0.00017748, 366.1551906, 0.00059159, -36.61551906, -5.916e-05, -109.84655718, -0.00017748, -366.1551906, -0.00059159, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 14.65, 4.15, 5.775)
    ops.node(123008, 14.65, 4.15, 7.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0875, 26384825.93716229, 10993677.47381762, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 96.24401242, 0.00081182, 115.51881119, 0.01149562, 11.55188112, 0.04046436, -96.24401242, -0.00081182, -115.51881119, -0.01149562, -11.55188112, -0.04046436, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 66.53817567, 0.00105263, 79.8637833, 0.01068254, 7.98637833, 0.03332585, -66.53817567, -0.00105263, -79.8637833, -0.01068254, -7.98637833, -0.03332585, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 110.30288817, 0.01623634, 110.30288817, 0.04870902, 77.21202172, -1670.8595621, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 27.57572204, 9.46e-05, 82.72716613, 0.0002838, 275.75722043, 0.000946, -27.57572204, -9.46e-05, -82.72716613, -0.0002838, -275.75722043, -0.000946, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 88.8242722, 0.02105269, 88.8242722, 0.06315808, 62.17699054, -1277.59802145, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 22.20606805, 7.618e-05, 66.61820415, 0.00022854, 222.06068051, 0.00076179, -22.20606805, -7.618e-05, -66.61820415, -0.00022854, -222.06068051, -0.00076179, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.3, 5.8)
    ops.node(123009, 0.0, 8.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 25619034.26883273, 10674597.61201364, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 53.63792743, 0.00108477, 64.54224844, 0.01038971, 6.45422484, 0.04014671, -53.63792743, -0.00108477, -64.54224844, -0.01038971, -6.45422484, -0.04014671, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 53.63792743, 0.00108477, 64.54224844, 0.01038971, 6.45422484, 0.04014671, -53.63792743, -0.00108477, -64.54224844, -0.01038971, -6.45422484, -0.04014671, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 44.97742401, 0.02169547, 44.97742401, 0.06508642, 31.4841968, -1012.36289559, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 11.244356, 5.562e-05, 33.733068, 0.00016685, 112.44356001, 0.00055618, -11.244356, -5.562e-05, -33.733068, -0.00016685, -112.44356001, -0.00055618, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 44.97742401, 0.02169547, 44.97742401, 0.06508642, 31.4841968, -1012.36289559, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 11.244356, 5.562e-05, 33.733068, 0.00016685, 112.44356001, 0.00055618, -11.244356, -5.562e-05, -33.733068, -0.00016685, -112.44356001, -0.00055618, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 5.9, 8.3, 5.8)
    ops.node(123010, 5.9, 8.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0625, 26354583.35465271, 10981076.39777196, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 43.70494859, 0.00112149, 52.30864581, 0.01069381, 5.23086458, 0.04132869, -43.70494859, -0.00112149, -52.30864581, -0.01069381, -5.23086458, -0.04132869, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 43.70494859, 0.00112149, 52.30864581, 0.01069381, 5.23086458, 0.04132869, -43.70494859, -0.00112149, -52.30864581, -0.01069381, -5.23086458, -0.04132869, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 85.4902883, 0.02242972, 85.4902883, 0.06728916, 59.84320181, -1365.5542356, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 21.37257208, 0.00010277, 64.11771623, 0.0003083, 213.72572076, 0.00102765, -21.37257208, -0.00010277, -64.11771623, -0.0003083, -213.72572076, -0.00102765, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 85.4902883, 0.02242972, 85.4902883, 0.06728916, 59.84320181, -1365.5542356, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 21.37257208, 0.00010277, 64.11771623, 0.0003083, 213.72572076, 0.00102765, -21.37257208, -0.00010277, -64.11771623, -0.0003083, -213.72572076, -0.00102765, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.75, 8.3, 5.8)
    ops.node(123011, 8.75, 8.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.0625, 26971058.91961571, 11237941.21650655, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 45.16271907, 0.00110951, 54.08397603, 0.01184097, 5.4083976, 0.04430479, -45.16271907, -0.00110951, -54.08397603, -0.01184097, -5.4083976, -0.04430479, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 45.16271907, 0.00110951, 54.08397603, 0.01184097, 5.4083976, 0.04430479, -45.16271907, -0.00110951, -54.08397603, -0.01184097, -5.4083976, -0.04430479, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 90.6350888, 0.02219014, 90.6350888, 0.06657042, 63.44456216, -1488.6474545, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 22.6587722, 0.00010646, 67.9763166, 0.00031938, 226.58772199, 0.00106459, -22.6587722, -0.00010646, -67.9763166, -0.00031938, -226.58772199, -0.00106459, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 90.6350888, 0.02219014, 90.6350888, 0.06657042, 63.44456216, -1488.6474545, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 22.6587722, 0.00010646, 67.9763166, 0.00031938, 226.58772199, 0.00106459, -22.6587722, -0.00010646, -67.9763166, -0.00031938, -226.58772199, -0.00106459, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 14.65, 8.3, 5.8)
    ops.node(123012, 14.65, 8.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 27469101.87824628, 11445459.11593595, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 55.06720116, 0.00112983, 66.2984196, 0.01180974, 6.62984196, 0.04598878, -55.06720116, -0.00112983, -66.2984196, -0.01180974, -6.62984196, -0.04598878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 55.06720116, 0.00112983, 66.2984196, 0.01180974, 6.62984196, 0.04598878, -55.06720116, -0.00112983, -66.2984196, -0.01180974, -6.62984196, -0.04598878, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 61.13265929, 0.02259668, 61.13265929, 0.06779005, 42.7928615, -1044.06800817, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 15.28316482, 7.05e-05, 45.84949447, 0.00021151, 152.83164822, 0.00070504, -15.28316482, -7.05e-05, -45.84949447, -0.00021151, -152.83164822, -0.00070504, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 61.13265929, 0.02259668, 61.13265929, 0.06779005, 42.7928615, -1044.06800817, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 15.28316482, 7.05e-05, 45.84949447, 0.00021151, 152.83164822, 0.00070504, -15.28316482, -7.05e-05, -45.84949447, -0.00021151, -152.83164822, -0.00070504, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.55)
    ops.node(124001, 0.0, 0.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26253179.92213515, 10938824.96755631, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 40.99665206, 0.00105932, 50.03190792, 0.01348681, 5.00319079, 0.06063248, -40.99665206, -0.00105932, -50.03190792, -0.01348681, -5.00319079, -0.06063248, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 40.99665206, 0.00105932, 50.03190792, 0.01348681, 5.00319079, 0.06063248, -40.99665206, -0.00105932, -50.03190792, -0.01348681, -5.00319079, -0.06063248, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 43.73432126, 0.02118648, 43.73432126, 0.06355944, 30.61402488, -1211.53328172, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 10.93358031, 5.277e-05, 32.80074094, 0.00015832, 109.33580315, 0.00052775, -10.93358031, -5.277e-05, -32.80074094, -0.00015832, -109.33580315, -0.00052775, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 43.73432126, 0.02118648, 43.73432126, 0.06355944, 30.61402488, -1211.53328172, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 10.93358031, 5.277e-05, 32.80074094, 0.00015832, 109.33580315, 0.00052775, -10.93358031, -5.277e-05, -32.80074094, -0.00015832, -109.33580315, -0.00052775, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 14.65, 0.0, 8.55)
    ops.node(124004, 14.65, 0.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 28204584.60188689, 11751910.25078621, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 43.55017171, 0.00107409, 52.98333929, 0.01274865, 5.29833393, 0.06202452, -43.55017171, -0.00107409, -52.98333929, -0.01274865, -5.29833393, -0.06202452, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 43.55017171, 0.00107409, 52.98333929, 0.01274865, 5.29833393, 0.06202452, -43.55017171, -0.00107409, -52.98333929, -0.01274865, -5.29833393, -0.06202452, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 43.68868103, 0.02148174, 43.68868103, 0.06444521, 30.58207672, -1137.59385816, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 10.92217026, 4.907e-05, 32.76651077, 0.00014722, 109.22170257, 0.00049072, -10.92217026, -4.907e-05, -32.76651077, -0.00014722, -109.22170257, -0.00049072, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 43.68868103, 0.02148174, 43.68868103, 0.06444521, 30.58207672, -1137.59385816, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 10.92217026, 4.907e-05, 32.76651077, 0.00014722, 109.22170257, 0.00049072, -10.92217026, -4.907e-05, -32.76651077, -0.00014722, -109.22170257, -0.00049072, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.15, 8.525)
    ops.node(124005, 0.0, 4.15, 10.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0875, 27532434.52446334, 11471847.71852639, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 69.73460061, 0.00082132, 84.75302521, 0.01232469, 8.47530252, 0.05780793, -69.73460061, -0.00082132, -84.75302521, -0.01232469, -8.47530252, -0.05780793, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 47.17941532, 0.00110133, 57.34023198, 0.01146996, 5.7340232, 0.04702176, -47.17941532, -0.00110133, -57.34023198, -0.01146996, -5.7340232, -0.04702176, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 91.91050925, 0.01642637, 91.91050925, 0.0492791, 64.33735648, -1444.91355637, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 22.97762731, 7.554e-05, 68.93288194, 0.00022662, 229.77627313, 0.0007554, -22.97762731, -7.554e-05, -68.93288194, -0.00022662, -229.77627313, -0.0007554, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 60.85359094, 0.02202657, 60.85359094, 0.0660797, 42.59751366, -980.55971644, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 15.21339773, 5.001e-05, 45.6401932, 0.00015004, 152.13397735, 0.00050015, -15.21339773, -5.001e-05, -45.6401932, -0.00015004, -152.13397735, -0.00050015, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 5.9, 4.15, 8.525)
    ops.node(124006, 5.9, 4.15, 10.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.175, 27624398.41257858, 11510166.00524108, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 164.0465588, 0.00063294, 199.87544054, 0.00995817, 19.98754405, 0.04181212, -164.0465588, -0.00063294, -199.87544054, -0.00995817, -19.98754405, -0.04181212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 110.38869757, 0.00077853, 134.49833827, 0.00931714, 13.44983383, 0.03516218, -110.38869757, -0.00077853, -134.49833827, -0.00931714, -13.44983383, -0.03516218, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 158.90594991, 0.01265871, 158.90594991, 0.03797614, 111.23416494, -1605.59876232, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 39.72648748, 6.508e-05, 119.17946243, 0.00019525, 397.26487478, 0.00065084, -39.72648748, -6.508e-05, -119.17946243, -0.00019525, -397.26487478, -0.00065084, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 114.32535899, 0.01557058, 114.32535899, 0.04671174, 80.02775129, -1097.31197836, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 28.58133975, 4.682e-05, 85.74401924, 0.00014047, 285.81339747, 0.00046825, -28.58133975, -4.682e-05, -85.74401924, -0.00014047, -285.81339747, -0.00046825, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 8.75, 4.15, 8.525)
    ops.node(124007, 8.75, 4.15, 10.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.175, 27130705.82017782, 11304460.75840742, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 158.43638717, 0.00063491, 193.20163267, 0.01147863, 19.32016327, 0.04301321, -158.43638717, -0.00063491, -193.20163267, -0.01147863, -19.32016327, -0.04301321, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 106.01182131, 0.00078831, 129.27369353, 0.01071732, 12.92736935, 0.03630323, -106.01182131, -0.00078831, -129.27369353, -0.01071732, -12.92736935, -0.03630323, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 162.26850952, 0.01269822, 162.26850952, 0.03809467, 113.58795666, -1863.65960456, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 40.56712738, 6.767e-05, 121.70138214, 0.00020301, 405.6712738, 0.00067671, -40.56712738, -6.767e-05, -121.70138214, -0.00020301, -405.6712738, -0.00067671, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 130.10080426, 0.01576625, 130.10080426, 0.04729875, 91.07056298, -1245.79632581, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 32.52520106, 5.426e-05, 97.57560319, 0.00016277, 325.25201064, 0.00054256, -32.52520106, -5.426e-05, -97.57560319, -0.00016277, -325.25201064, -0.00054256, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 14.65, 4.15, 8.525)
    ops.node(124008, 14.65, 4.15, 10.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0875, 28993110.08850084, 12080462.53687535, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 72.09228627, 0.00080282, 87.4039378, 0.01343301, 8.74039378, 0.06070562, -72.09228627, -0.00080282, -87.4039378, -0.01343301, -8.74039378, -0.06070562, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 48.98988918, 0.00105803, 59.39483193, 0.01244233, 5.93948319, 0.04939279, -48.98988918, -0.00105803, -59.39483193, -0.01244233, -5.93948319, -0.04939279, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 101.23050939, 0.0160564, 101.23050939, 0.04816919, 70.86135657, -1702.80667526, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 25.30762735, 7.901e-05, 75.92288204, 0.00023703, 253.07627347, 0.00079008, -25.30762735, -7.901e-05, -75.92288204, -0.00023703, -253.07627347, -0.00079008, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 77.77111442, 0.02116062, 77.77111442, 0.06348186, 54.43978009, -1131.48168454, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 19.4427786, 6.07e-05, 58.32833581, 0.0001821, 194.42778604, 0.00060699, -19.4427786, -6.07e-05, -58.32833581, -0.0001821, -194.42778604, -0.00060699, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.3, 8.55)
    ops.node(124009, 0.0, 8.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 27939068.65764095, 11641278.60735039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 41.96792458, 0.00115941, 51.08360591, 0.01390216, 5.10836059, 0.06292034, -41.96792458, -0.00115941, -51.08360591, -0.01390216, -5.10836059, -0.06292034, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 41.96792458, 0.00115941, 51.08360591, 0.01390216, 5.10836059, 0.06292034, -41.96792458, -0.00115941, -51.08360591, -0.01390216, -5.10836059, -0.06292034, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 54.15403275, 0.02318829, 54.15403275, 0.06956486, 37.90782293, -1302.38192483, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 13.53850819, 6.141e-05, 40.61552456, 0.00018422, 135.38508188, 0.00061405, -13.53850819, -6.141e-05, -40.61552456, -0.00018422, -135.38508188, -0.00061405, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 54.15403275, 0.02318829, 54.15403275, 0.06956486, 37.90782293, -1302.38192483, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 13.53850819, 6.141e-05, 40.61552456, 0.00018422, 135.38508188, 0.00061405, -13.53850819, -6.141e-05, -40.61552456, -0.00018422, -135.38508188, -0.00061405, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 5.9, 8.3, 8.55)
    ops.node(124010, 5.9, 8.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0625, 26018517.25641327, 10841048.85683887, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 30.13176394, 0.001028, 36.67168943, 0.01407422, 3.66716894, 0.06343699, -30.13176394, -0.001028, -36.67168943, -0.01407422, -3.66716894, -0.06343699, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 30.13176394, 0.001028, 36.67168943, 0.01407422, 3.66716894, 0.06343699, -30.13176394, -0.001028, -36.67168943, -0.01407422, -3.66716894, -0.06343699, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 76.10598024, 0.02055991, 76.10598024, 0.06167972, 53.27418616, -1657.16249734, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 19.02649506, 9.267e-05, 57.07948518, 0.000278, 190.26495059, 0.00092666, -19.02649506, -9.267e-05, -57.07948518, -0.000278, -190.26495059, -0.00092666, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 76.10598024, 0.02055991, 76.10598024, 0.06167972, 53.27418616, -1657.16249734, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 19.02649506, 9.267e-05, 57.07948518, 0.000278, 190.26495059, 0.00092666, -19.02649506, -9.267e-05, -57.07948518, -0.000278, -190.26495059, -0.00092666, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.75, 8.3, 8.55)
    ops.node(124011, 8.75, 8.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.0625, 28488648.32723416, 11870270.13634757, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 28.83656626, 0.00107332, 34.98474912, 0.01324387, 3.49847491, 0.06669054, -28.83656626, -0.00107332, -34.98474912, -0.01324387, -3.49847491, -0.06669054, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 28.83656626, 0.00107332, 34.98474912, 0.01324387, 3.49847491, 0.06669054, -28.83656626, -0.00107332, -34.98474912, -0.01324387, -3.49847491, -0.06669054, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 76.71047023, 0.02146645, 76.71047023, 0.06439935, 53.69732916, -1454.32561029, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 19.17761756, 8.53e-05, 57.53285267, 0.00025591, 191.77617556, 0.00085304, -19.17761756, -8.53e-05, -57.53285267, -0.00025591, -191.77617556, -0.00085304, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 76.71047023, 0.02146645, 76.71047023, 0.06439935, 53.69732916, -1454.32561029, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 19.17761756, 8.53e-05, 57.53285267, 0.00025591, 191.77617556, 0.00085304, -19.17761756, -8.53e-05, -57.53285267, -0.00025591, -191.77617556, -0.00085304, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 14.65, 8.3, 8.55)
    ops.node(124012, 14.65, 8.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 30761984.08654795, 12817493.36939498, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 41.96499962, 0.00105199, 50.75632255, 0.01495451, 5.07563226, 0.06629906, -41.96499962, -0.00105199, -50.75632255, -0.01495451, -5.07563226, -0.06629906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 41.96499962, 0.00105199, 50.75632255, 0.01495451, 5.07563226, 0.06629906, -41.96499962, -0.00105199, -50.75632255, -0.01495451, -5.07563226, -0.06629906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 72.46219043, 0.02103975, 72.46219043, 0.06311926, 50.7235333, -1493.51078405, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 18.11554761, 7.462e-05, 54.34664282, 0.00022387, 181.15547607, 0.00074625, -18.11554761, -7.462e-05, -54.34664282, -0.00022387, -181.15547607, -0.00074625, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 72.46219043, 0.02103975, 72.46219043, 0.06311926, 50.7235333, -1493.51078405, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 18.11554761, 7.462e-05, 54.34664282, 0.00022387, 181.15547607, 0.00074625, -18.11554761, -7.462e-05, -54.34664282, -0.00022387, -181.15547607, -0.00074625, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 5.9, 0.0, 0.0)
    ops.node(124013, 5.9, 0.0, 1.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4030, 170002, 124013, 0.14, 27602684.34676113, 11501118.47781714, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24030, 172.12063783, 0.0006285, 205.64855537, 0.00978037, 20.56485554, 0.02939236, -172.12063783, -0.0006285, -205.64855537, -0.00978037, -20.56485554, -0.02939236, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14030, 181.84695309, 0.00060385, 217.26949001, 0.01011372, 21.726949, 0.03159458, -181.84695309, -0.00060385, -217.26949001, -0.01011372, -21.726949, -0.03159458, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24030, 4030, 0.0, 231.09842999, 0.01257009, 231.09842999, 0.03771026, 161.76890099, -4096.67327432, 0.05, 2, 0, 70002, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 44030, 57.7746075, 5.92e-05, 173.32382249, 0.00017761, 577.74607498, 0.00059204, -57.7746075, -5.92e-05, -173.32382249, -0.00017761, -577.74607498, -0.00059204, 0.4, 0.3, 0.003, 0.0, 0.0, 24030, 2)
    ops.limitCurve('ThreePoint', 14030, 4030, 0.0, 264.11249142, 0.01207704, 264.11249142, 0.03623111, 184.87874399, -4435.74638056, 0.05, 2, 0, 70002, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 34030, 66.02812285, 6.766e-05, 198.08436856, 0.00020299, 660.28122855, 0.00067662, -66.02812285, -6.766e-05, -198.08436856, -0.00020299, -660.28122855, -0.00067662, 0.4, 0.3, 0.003, 0.0, 0.0, 14030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4030, 99999, 'P', 44030, 'Vy', 34030, 'Vz', 24030, 'My', 14030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 4030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174013, 5.9, 0.0, 1.575)
    ops.node(121002, 5.9, 0.0, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4031, 174013, 121002, 0.14, 29706044.79564267, 12377518.66485111, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24031, 190.79005605, 0.0006501, 228.20861378, 0.00894505, 22.82086138, 0.03288228, -190.79005605, -0.0006501, -228.20861378, -0.00894505, -22.82086138, -0.03288228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14031, 191.88279916, 0.00062, 229.51567032, 0.00923943, 22.95156703, 0.0354577, -191.88279916, -0.00062, -229.51567032, -0.00923943, -22.95156703, -0.0354577, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24031, 4031, 0.0, 231.92258541, 0.01300197, 231.92258541, 0.0390059, 162.34580979, -3482.16940754, 0.05, 2, 0, 74013, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44031, 57.98064635, 5.521e-05, 173.94193906, 0.00016563, 579.80646353, 0.00055208, -57.98064635, -5.521e-05, -173.94193906, -0.00016563, -579.80646353, -0.00055208, 0.4, 0.3, 0.003, 0.0, 0.0, 24031, 2)
    ops.limitCurve('ThreePoint', 14031, 4031, 0.0, 265.05438333, 0.01240005, 265.05438333, 0.03720015, 185.53806833, -3733.52141663, 0.05, 2, 0, 74013, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34031, 66.26359583, 6.31e-05, 198.7907875, 0.00018929, 662.63595832, 0.00063095, -66.26359583, -6.31e-05, -198.7907875, -0.00018929, -662.63595832, -0.00063095, 0.4, 0.3, 0.003, 0.0, 0.0, 14031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4031, 99999, 'P', 44031, 'Vy', 34031, 'Vz', 24031, 'My', 14031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174013, 74013, 174013, 4031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.75, 0.0, 0.0)
    ops.node(124014, 8.75, 0.0, 1.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4032, 170003, 124014, 0.14, 26935038.34657495, 11222932.64440623, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24032, 166.29273721, 0.00066118, 198.57454094, 0.00939795, 19.85745409, 0.02780188, -166.29273721, -0.00066118, -198.57454094, -0.00939795, -19.85745409, -0.02780188, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14032, 178.04384173, 0.0006292, 212.6068446, 0.00970774, 21.26068446, 0.02986542, -178.04384173, -0.0006292, -212.6068446, -0.00970774, -21.26068446, -0.02986542, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24032, 4032, 0.0, 226.7925564, 0.01322352, 226.7925564, 0.03967057, 158.75478948, -4123.47601427, 0.05, 2, 0, 70003, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 44032, 56.6981391, 5.954e-05, 170.0944173, 0.00017862, 566.98139101, 0.00059541, -56.6981391, -5.954e-05, -170.0944173, -0.00017862, -566.98139101, -0.00059541, 0.4, 0.3, 0.003, 0.0, 0.0, 24032, 2)
    ops.limitCurve('ThreePoint', 14032, 4032, 0.0, 259.19149303, 0.01258408, 259.19149303, 0.03775223, 181.43404512, -4467.62565503, 0.05, 2, 0, 70003, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 34032, 64.79787326, 6.805e-05, 194.39361977, 0.00020414, 647.97873258, 0.00068047, -64.79787326, -6.805e-05, -194.39361977, -0.00020414, -647.97873258, -0.00068047, 0.4, 0.3, 0.003, 0.0, 0.0, 14032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4032, 99999, 'P', 44032, 'Vy', 34032, 'Vz', 24032, 'My', 14032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 4032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174014, 8.75, 0.0, 1.575)
    ops.node(121003, 8.75, 0.0, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4033, 174014, 121003, 0.14, 27884144.93644137, 11618393.72351724, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24033, 190.41788003, 0.00062152, 227.89118458, 0.00958931, 22.78911846, 0.03063394, -190.41788003, -0.00062152, -227.89118458, -0.00958931, -22.78911846, -0.03063394, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14033, 188.60741911, 0.0005969, 225.72443384, 0.00991548, 22.57244338, 0.0329655, -188.60741911, -0.0005969, -225.72443384, -0.00991548, -22.57244338, -0.0329655, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24033, 4033, 0.0, 222.4250136, 0.0124304, 222.4250136, 0.0372912, 155.69750952, -3662.5412751, 0.05, 2, 0, 74014, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44033, 55.6062534, 5.641e-05, 166.8187602, 0.00016922, 556.06253399, 0.00056407, -55.6062534, -5.641e-05, -166.8187602, -0.00016922, -556.06253399, -0.00056407, 0.4, 0.3, 0.003, 0.0, 0.0, 24033, 2)
    ops.limitCurve('ThreePoint', 14033, 4033, 0.0, 254.20001554, 0.01193791, 254.20001554, 0.03581374, 177.94001088, -3947.25039843, 0.05, 2, 0, 74014, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34033, 63.55000388, 6.447e-05, 190.65001165, 0.0001934, 635.50003885, 0.00064465, -63.55000388, -6.447e-05, -190.65001165, -0.0001934, -635.50003885, -0.00064465, 0.4, 0.3, 0.003, 0.0, 0.0, 14033, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4033, 99999, 'P', 44033, 'Vy', 34033, 'Vz', 24033, 'My', 14033, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174014, 74014, 174014, 4033, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4033, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 5.9, 0.0, 3.05)
    ops.node(124015, 5.9, 0.0, 3.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4035, 171002, 124015, 0.14, 27301843.93728144, 11375768.3072006, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24035, 128.27565508, 0.00063919, 154.29101251, 0.009418, 15.42910125, 0.03284669, -128.27565508, -0.00063919, -154.29101251, -0.009418, -15.42910125, -0.03284669, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14035, 142.26511384, 0.00060869, 171.11764851, 0.00973091, 17.11176485, 0.03539217, -142.26511384, -0.00060869, -171.11764851, -0.00973091, -17.11176485, -0.03539217, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24035, 4035, 0.0, 205.31691158, 0.01278375, 205.31691158, 0.03835126, 143.72183811, -3310.05622114, 0.05, 2, 0, 71002, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 44035, 51.32922789, 5.318e-05, 153.98768368, 0.00015954, 513.29227895, 0.00053179, -51.32922789, -5.318e-05, -153.98768368, -0.00015954, -513.29227895, -0.00053179, 0.4, 0.3, 0.003, 0.0, 0.0, 24035, 2)
    ops.limitCurve('ThreePoint', 14035, 4035, 0.0, 234.64789895, 0.01217383, 234.64789895, 0.03652149, 164.25352926, -3616.76391181, 0.05, 2, 0, 71002, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 34035, 58.66197474, 6.078e-05, 175.98592421, 0.00018233, 586.61974737, 0.00060776, -58.66197474, -6.078e-05, -175.98592421, -0.00018233, -586.61974737, -0.00060776, 0.4, 0.3, 0.003, 0.0, 0.0, 14035, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4035, 99999, 'P', 44035, 'Vy', 34035, 'Vz', 24035, 'My', 14035, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4035, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 4035, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174015, 5.9, 0.0, 4.325)
    ops.node(122002, 5.9, 0.0, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4036, 174015, 122002, 0.14, 27340209.43542022, 11391753.93142509, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24036, 127.74343409, 0.00062187, 153.89653325, 0.00884791, 15.38965332, 0.03348606, -127.74343409, -0.00062187, -153.89653325, -0.00884791, -15.38965332, -0.03348606, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14036, 140.60690313, 0.00059598, 169.39355903, 0.00914382, 16.9393559, 0.03612978, -140.60690313, -0.00059598, -169.39355903, -0.00914382, -16.9393559, -0.03612978, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24036, 4036, 0.0, 197.37178556, 0.01243731, 197.37178556, 0.03731193, 138.16024989, -3006.87906966, 0.05, 2, 0, 74015, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44036, 49.34294639, 5.105e-05, 148.02883917, 0.00015315, 493.42946391, 0.00051049, -49.34294639, -5.105e-05, -148.02883917, -0.00015315, -493.42946391, -0.00051049, 0.4, 0.3, 0.003, 0.0, 0.0, 24036, 2)
    ops.limitCurve('ThreePoint', 14036, 4036, 0.0, 225.56775493, 0.01191969, 225.56775493, 0.03575908, 157.89742845, -3282.95789565, 0.05, 2, 0, 74015, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34036, 56.39193873, 5.834e-05, 169.1758162, 0.00017503, 563.91938732, 0.00058342, -56.39193873, -5.834e-05, -169.1758162, -0.00017503, -563.91938732, -0.00058342, 0.4, 0.3, 0.003, 0.0, 0.0, 14036, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4036, 99999, 'P', 44036, 'Vy', 34036, 'Vz', 24036, 'My', 14036, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174015, 74015, 174015, 4036, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4036, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.75, 0.0, 3.05)
    ops.node(124016, 8.75, 0.0, 3.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4037, 171003, 124016, 0.14, 28891551.43561214, 12038146.43150506, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24037, 133.69050015, 0.00063306, 160.68584564, 0.01022211, 16.06858456, 0.03606208, -133.69050015, -0.00063306, -160.68584564, -0.01022211, -16.06858456, -0.03606208, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14037, 147.594737, 0.00060531, 177.39768421, 0.01056946, 17.73976842, 0.03887177, -147.594737, -0.00060531, -177.39768421, -0.01056946, -17.73976842, -0.03887177, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24037, 4037, 0.0, 219.65419414, 0.01266123, 219.65419414, 0.0379837, 153.7579359, -3465.65176047, 0.05, 2, 0, 71003, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 44037, 54.91354853, 5.376e-05, 164.7406456, 0.00016129, 549.13548534, 0.00053762, -54.91354853, -5.376e-05, -164.7406456, -0.00016129, -549.13548534, -0.00053762, 0.4, 0.3, 0.003, 0.0, 0.0, 24037, 2)
    ops.limitCurve('ThreePoint', 14037, 4037, 0.0, 251.03336473, 0.01210625, 251.03336473, 0.03631875, 175.72335531, -3802.84261304, 0.05, 2, 0, 71003, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 34037, 62.75834118, 6.144e-05, 188.27502355, 0.00018433, 627.58341182, 0.00061442, -62.75834118, -6.144e-05, -188.27502355, -0.00018433, -627.58341182, -0.00061442, 0.4, 0.3, 0.003, 0.0, 0.0, 14037, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4037, 99999, 'P', 44037, 'Vy', 34037, 'Vz', 24037, 'My', 14037, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4037, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 4037, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174016, 8.75, 0.0, 4.325)
    ops.node(122003, 8.75, 0.0, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4038, 174016, 122003, 0.14, 27751050.16911313, 11562937.57046381, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24038, 130.9545009, 0.00062005, 157.7418499, 0.01057238, 15.77418499, 0.03583916, -130.9545009, -0.00062005, -157.7418499, -0.01057238, -15.77418499, -0.03583916, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14038, 143.68491679, 0.00059542, 173.07633125, 0.01093707, 17.30763313, 0.03861157, -143.68491679, -0.00059542, -173.07633125, -0.01093707, -17.30763313, -0.03861157, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24038, 4038, 0.0, 211.94344292, 0.01240092, 211.94344292, 0.03720277, 148.36041004, -3613.93628491, 0.05, 2, 0, 74016, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44038, 52.98586073, 5.401e-05, 158.95758219, 0.00016202, 529.85860729, 0.00054007, -52.98586073, -5.401e-05, -158.95758219, -0.00016202, -529.85860729, -0.00054007, 0.4, 0.3, 0.003, 0.0, 0.0, 24038, 2)
    ops.limitCurve('ThreePoint', 14038, 4038, 0.0, 242.22107762, 0.01190844, 242.22107762, 0.03572531, 169.55475433, -4011.01039757, 0.05, 2, 0, 74016, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34038, 60.5552694, 6.172e-05, 181.66580821, 0.00018517, 605.55269405, 0.00061722, -60.5552694, -6.172e-05, -181.66580821, -0.00018517, -605.55269405, -0.00061722, 0.4, 0.3, 0.003, 0.0, 0.0, 14038, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4038, 99999, 'P', 44038, 'Vy', 34038, 'Vz', 24038, 'My', 14038, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174016, 74016, 174016, 4038, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4038, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 5.9, 0.0, 5.8)
    ops.node(124017, 5.9, 0.0, 6.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4040, 172002, 124017, 0.0875, 30534227.3739001, 12722594.73912504, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24040, 73.09656667, 0.00080008, 87.63708295, 0.0096234, 8.7637083, 0.03987443, -73.09656667, -0.00080008, -87.63708295, -0.0096234, -8.7637083, -0.03987443, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14040, 102.04704857, 0.00065595, 122.34645303, 0.01044489, 12.2346453, 0.04914658, -102.04704857, -0.00065595, -122.34645303, -0.01044489, -12.2346453, -0.04914658, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24040, 4040, 0.0, 89.88148458, 0.01600154, 89.88148458, 0.04800462, 62.91703921, -2191.94053585, 0.05, 2, 0, 72002, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44040, 22.47037115, 3.331e-05, 67.41111344, 9.992e-05, 224.70371146, 0.00033305, -22.47037115, -3.331e-05, -67.41111344, -9.992e-05, -224.70371146, -0.00033305, 0.4, 0.3, 0.003, 0.0, 0.0, 24040, 2)
    ops.limitCurve('ThreePoint', 14040, 4040, 0.0, 157.19209912, 0.01311895, 157.19209912, 0.03935685, 110.03446938, -2800.51039093, 0.05, 2, 0, 72002, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34040, 39.29802478, 5.825e-05, 117.89407434, 0.00017474, 392.98024779, 0.00058247, -39.29802478, -5.825e-05, -117.89407434, -0.00017474, -392.98024779, -0.00058247, 0.4, 0.3, 0.003, 0.0, 0.0, 14040, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4040, 99999, 'P', 44040, 'Vy', 34040, 'Vz', 24040, 'My', 14040, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4040, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4040, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 5.9, 0.0, 7.05)
    ops.node(123002, 5.9, 0.0, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 174017, 123002, 0.0875, 27787165.49197738, 11577985.62165724, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 78.79664461, 0.00076665, 94.96179255, 0.01143201, 9.49617926, 0.03959182, -78.79664461, -0.00076665, -94.96179255, -0.01143201, -9.49617926, -0.03959182, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 104.39602979, 0.00063962, 125.8128969, 0.0124722, 12.58128969, 0.04849848, -104.39602979, -0.00063962, -125.8128969, -0.0124722, -12.58128969, -0.04849848, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 96.25016403, 0.01533295, 96.25016403, 0.04599885, 67.37511482, -2377.06429476, 0.05, 2, 0, 74017, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 24.06254101, 3.919e-05, 72.18762302, 0.00011757, 240.62541006, 0.00039191, -24.06254101, -3.919e-05, -72.18762302, -0.00011757, -240.62541006, -0.00039191, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 147.63332438, 0.01279248, 147.63332438, 0.03837745, 103.34332707, -3198.18925182, 0.05, 2, 0, 74017, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 36.9083311, 6.011e-05, 110.72499329, 0.00018034, 369.08331096, 0.00060113, -36.9083311, -6.011e-05, -110.72499329, -0.00018034, -369.08331096, -0.00060113, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.75, 0.0, 5.8)
    ops.node(124018, 8.75, 0.0, 6.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 172003, 124018, 0.0875, 25392268.25933572, 10580111.77472322, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 75.56568452, 0.00079162, 90.72177663, 0.01003222, 9.07217766, 0.03147637, -75.56568452, -0.00079162, -90.72177663, -0.01003222, -9.07217766, -0.03147637, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 104.46199614, 0.00065936, 125.41377665, 0.01091125, 12.54137766, 0.03834584, -104.46199614, -0.00065936, -125.41377665, -0.01091125, -12.54137766, -0.03834584, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 91.94745099, 0.0158323, 91.94745099, 0.04749691, 64.36321569, -2399.45562721, 0.05, 2, 0, 72003, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 22.98686275, 4.097e-05, 68.96058824, 0.00012291, 229.86862747, 0.0004097, -22.98686275, -4.097e-05, -68.96058824, -0.00012291, -229.86862747, -0.0004097, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 140.08436964, 0.01318716, 140.08436964, 0.03956147, 98.05905875, -3130.66572736, 0.05, 2, 0, 72003, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 35.02109241, 6.242e-05, 105.06327723, 0.00018726, 350.2109241, 0.00062419, -35.02109241, -6.242e-05, -105.06327723, -0.00018726, -350.2109241, -0.00062419, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 8.75, 0.0, 7.05)
    ops.node(123003, 8.75, 0.0, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 174018, 123003, 0.0875, 27042734.91592156, 11267806.21496732, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 75.15657436, 0.00080704, 90.59870007, 0.01181905, 9.05987001, 0.03873488, -75.15657436, -0.00080704, -90.59870007, -0.01181905, -9.05987001, -0.03873488, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 101.1195679, 0.0006572, 121.89620776, 0.01287436, 12.18962078, 0.04730916, -101.1195679, -0.0006572, -121.89620776, -0.01287436, -12.18962078, -0.04730916, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 98.93720001, 0.01614075, 98.93720001, 0.04842225, 69.25604001, -2398.33637225, 0.05, 2, 0, 74018, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 24.7343, 4.139e-05, 74.20290001, 0.00012418, 247.34300002, 0.00041394, -24.7343, -4.139e-05, -74.20290001, -0.00012418, -247.34300002, -0.00041394, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 144.9541087, 0.01314397, 144.9541087, 0.03943191, 101.46787609, -3232.74893171, 0.05, 2, 0, 74018, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 36.23852717, 6.065e-05, 108.71558152, 0.00018194, 362.38527175, 0.00060647, -36.23852717, -6.065e-05, -108.71558152, -0.00018194, -362.38527175, -0.00060647, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 5.9, 0.0, 8.55)
    ops.node(124019, 5.9, 0.0, 9.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4045, 173002, 124019, 0.0875, 29380084.67565384, 12241701.9481891, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24045, 47.69405485, 0.00070259, 57.81462153, 0.01194152, 5.78146215, 0.04990927, -47.69405485, -0.00070259, -57.81462153, -0.01194152, -5.78146215, -0.04990927, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14045, 70.20039395, 0.00059697, 85.09675305, 0.01306589, 8.50967531, 0.06163997, -70.20039395, -0.00059697, -85.09675305, -0.01306589, -8.50967531, -0.06163997, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24045, 4045, 0.0, 84.11899815, 0.01405174, 84.11899815, 0.04215523, 58.8832987, -2304.94412583, 0.05, 2, 0, 73002, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44045, 21.02974954, 3.239e-05, 63.08924861, 9.718e-05, 210.29749537, 0.00032394, -21.02974954, -3.239e-05, -63.08924861, -9.718e-05, -210.29749537, -0.00032394, 0.4, 0.3, 0.003, 0.0, 0.0, 24045, 2)
    ops.limitCurve('ThreePoint', 14045, 4045, 0.0, 136.19390442, 0.01193947, 136.19390442, 0.03581841, 95.3357331, -3524.2924338, 0.05, 2, 0, 73002, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34045, 34.04847611, 5.245e-05, 102.14542832, 0.00015735, 340.48476106, 0.00052448, -34.04847611, -5.245e-05, -102.14542832, -0.00015735, -340.48476106, -0.00052448, 0.4, 0.3, 0.003, 0.0, 0.0, 14045, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4045, 99999, 'P', 44045, 'Vy', 34045, 'Vz', 24045, 'My', 14045, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4045, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4045, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 5.9, 0.0, 9.8)
    ops.node(124002, 5.9, 0.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 174019, 124002, 0.0875, 27212692.94175111, 11338622.05906296, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 44.11694701, 0.00070394, 53.834902, 0.0131195, 5.3834902, 0.0523141, -44.11694701, -0.00070394, -53.834902, -0.0131195, -5.3834902, -0.0523141, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 65.2253845, 0.00059807, 79.59304577, 0.01437239, 7.95930458, 0.06451605, -65.2253845, -0.00059807, -79.59304577, -0.01437239, -7.95930458, -0.06451605, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 81.57783384, 0.01407878, 81.57783384, 0.04223633, 57.10448369, -2860.50651739, 0.05, 2, 0, 74019, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 20.39445846, 3.392e-05, 61.18337538, 0.00010175, 203.94458461, 0.00033918, -20.39445846, -3.392e-05, -61.18337538, -0.00010175, -203.94458461, -0.00033918, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 124.40520071, 0.01196139, 124.40520071, 0.03588417, 87.0836405, -4708.34293387, 0.05, 2, 0, 74019, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 31.10130018, 5.172e-05, 93.30390053, 0.00015517, 311.01300177, 0.00051724, -31.10130018, -5.172e-05, -93.30390053, -0.00015517, -311.01300177, -0.00051724, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.75, 0.0, 8.55)
    ops.node(124020, 8.75, 0.0, 9.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 173003, 124020, 0.0875, 24593834.09550582, 10247430.87312743, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 50.08422955, 0.00069917, 61.09141192, 0.01199408, 6.10914119, 0.04486917, -50.08422955, -0.00069917, -61.09141192, -0.01199408, -6.10914119, -0.04486917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 73.2917682, 0.00060103, 89.39935069, 0.01313204, 8.93993507, 0.05519084, -73.2917682, -0.00060103, -89.39935069, -0.01313204, -8.93993507, -0.05519084, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 72.45320872, 0.01398349, 72.45320872, 0.04195046, 50.7172461, -2249.80505074, 0.05, 2, 0, 73003, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 18.11330218, 3.333e-05, 54.33990654, 0.0001, 181.13302179, 0.00033332, -18.11330218, -3.333e-05, -54.33990654, -0.0001, -181.13302179, -0.00033332, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 116.00284859, 0.01202064, 116.00284859, 0.03606193, 81.20199401, -3428.91500428, 0.05, 2, 0, 73003, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 29.00071215, 5.337e-05, 87.00213644, 0.0001601, 290.00712148, 0.00053367, -29.00071215, -5.337e-05, -87.00213644, -0.0001601, -290.00712148, -0.00053367, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 8.75, 0.0, 9.8)
    ops.node(124003, 8.75, 0.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 174020, 124003, 0.0875, 26493722.11040679, 11039050.87933616, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 43.20123969, 0.00069625, 52.77962181, 0.01295793, 5.27796218, 0.05162108, -43.20123969, -0.00069625, -52.77962181, -0.01295793, -5.27796218, -0.05162108, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 63.89608187, 0.00059227, 78.06283014, 0.01419586, 7.80628301, 0.06365961, -63.89608187, -0.00059227, -78.06283014, -0.01419586, -7.80628301, -0.06365961, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 75.97446421, 0.01392492, 75.97446421, 0.04177477, 53.18212494, -2801.46619664, 0.05, 2, 0, 74020, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 18.99361605, 3.245e-05, 56.98084815, 9.734e-05, 189.93616052, 0.00032445, -18.99361605, -3.245e-05, -56.98084815, -9.734e-05, -189.93616052, -0.00032445, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 120.84552901, 0.01184537, 120.84552901, 0.0355361, 84.5918703, -4602.34858922, 0.05, 2, 0, 74020, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 30.21138225, 5.161e-05, 90.63414675, 0.00015482, 302.11382251, 0.00051608, -30.21138225, -5.161e-05, -90.63414675, -0.00015482, -302.11382251, -0.00051608, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4048, '-orient', 0, 0, 1, 0, 1, 0)
