import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 23059682.11080355, 9608200.87950148, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 61.01421674, 0.00052149, 71.4872788, 0.00879409, 7.14872788, 0.01901079, -61.01421674, -0.00052149, -71.4872788, -0.00879409, -7.14872788, -0.01901079, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 57.83190508, 0.00052149, 67.75872483, 0.00879409, 6.77587248, 0.01901079, -57.83190508, -0.00052149, -67.75872483, -0.00879409, -6.77587248, -0.01901079, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 85.70716904, 0.01042971, 85.70716904, 0.03128912, 59.99501833, -1167.17651667, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 21.42679226, 8.623e-05, 64.28037678, 0.00025869, 214.2679226, 0.00086229, -21.42679226, -8.623e-05, -64.28037678, -0.00025869, -214.2679226, -0.00086229, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 85.70716904, 0.01042971, 85.70716904, 0.03128912, 59.99501833, -1167.17651667, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 21.42679226, 8.623e-05, 64.28037678, 0.00025869, 214.2679226, 0.00086229, -21.42679226, -8.623e-05, -64.28037678, -0.00025869, -214.2679226, -0.00086229, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 7.25, 0.0, 0.0)
    ops.node(121002, 7.25, 0.0, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.2025, 27779840.65496076, 11574933.60623365, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 212.57782105, 0.00057748, 254.48733592, 0.00923163, 25.44873359, 0.02874101, -212.57782105, -0.00057748, -254.48733592, -0.00923163, -25.44873359, -0.02874101, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 235.67170833, 0.00057748, 282.13416108, 0.00923163, 28.21341611, 0.02874101, -235.67170833, -0.00057748, -282.13416108, -0.00923163, -28.21341611, -0.02874101, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 185.57158457, 0.01154952, 185.57158457, 0.03464856, 129.9001092, -1800.79018578, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 46.39289614, 6.888e-05, 139.17868843, 0.00020664, 463.92896143, 0.00068879, -46.39289614, -6.888e-05, -139.17868843, -0.00020664, -463.92896143, -0.00068879, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 185.57158457, 0.01154952, 185.57158457, 0.03464856, 129.9001092, -1800.79018578, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 46.39289614, 6.888e-05, 139.17868843, 0.00020664, 463.92896143, 0.00068879, -46.39289614, -6.888e-05, -139.17868843, -0.00020664, -463.92896143, -0.00068879, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 24.9, 0.0, 0.0)
    ops.node(121005, 24.9, 0.0, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.2025, 27069896.11427422, 11279123.38094759, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 204.51248492, 0.00055215, 244.74697719, 0.00957165, 24.47469772, 0.02792791, -204.51248492, -0.00055215, -244.74697719, -0.00957165, -24.47469772, -0.02792791, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 226.27086389, 0.00055215, 270.78596197, 0.00957165, 27.0785962, 0.02792791, -226.27086389, -0.00055215, -270.78596197, -0.00957165, -27.0785962, -0.02792791, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 183.3866952, 0.01104306, 183.3866952, 0.03312918, 128.37068664, -1845.26278013, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 45.8466738, 6.985e-05, 137.5400214, 0.00020956, 458.46673799, 0.00069853, -45.8466738, -6.985e-05, -137.5400214, -0.00020956, -458.46673799, -0.00069853, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 183.3866952, 0.01104306, 183.3866952, 0.03312918, 128.37068664, -1845.26278013, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 45.8466738, 6.985e-05, 137.5400214, 0.00020956, 458.46673799, 0.00069853, -45.8466738, -6.985e-05, -137.5400214, -0.00020956, -458.46673799, -0.00069853, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 32.15, 0.0, 0.0)
    ops.node(121006, 32.15, 0.0, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.09, 26977200.55969074, 11240500.23320447, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 91.20389083, 0.00073842, 108.39693113, 0.0119586, 10.83969311, 0.03156685, -91.20389083, -0.00073842, -108.39693113, -0.0119586, -10.83969311, -0.03156685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 84.20648645, 0.00073842, 100.0804311, 0.0119586, 10.00804311, 0.03156685, -84.20648645, -0.00073842, -100.0804311, -0.0119586, -10.00804311, -0.03156685, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 98.93500869, 0.01476835, 98.93500869, 0.04430504, 69.25450608, -1206.25317402, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 24.73375217, 8.508e-05, 74.20125652, 0.00025525, 247.33752172, 0.00085083, -24.73375217, -8.508e-05, -74.20125652, -0.00025525, -247.33752172, -0.00085083, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 98.93500869, 0.01476835, 98.93500869, 0.04430504, 69.25450608, -1206.25317402, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 24.73375217, 8.508e-05, 74.20125652, 0.00025525, 247.33752172, 0.00085083, -24.73375217, -8.508e-05, -74.20125652, -0.00025525, -247.33752172, -0.00085083, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 3.55, 0.0)
    ops.node(121007, 0.0, 3.55, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 26405407.80327706, 11002253.25136544, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 148.31740775, 0.00070626, 175.96693, 0.00918421, 17.596693, 0.0252271, -148.31740775, -0.00070626, -175.96693, -0.00918421, -17.596693, -0.0252271, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 132.48911251, 0.00070626, 157.18790357, 0.00918421, 15.71879036, 0.0252271, -132.48911251, -0.00070626, -157.18790357, -0.00918421, -15.71879036, -0.0252271, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 119.96046653, 0.01412517, 119.96046653, 0.0423755, 83.97232657, -1406.08066289, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 29.99011663, 7.744e-05, 89.9703499, 0.00023231, 299.90116632, 0.00077435, -29.99011663, -7.744e-05, -89.9703499, -0.00023231, -299.90116632, -0.00077435, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 119.96046653, 0.01412517, 119.96046653, 0.0423755, 83.97232657, -1406.08066289, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 29.99011663, 7.744e-05, 89.9703499, 0.00023231, 299.90116632, 0.00077435, -29.99011663, -7.744e-05, -89.9703499, -0.00023231, -299.90116632, -0.00077435, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 7.25, 3.55, 0.0)
    ops.node(121008, 7.25, 3.55, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.25, 25503508.75089377, 10626461.97953907, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 334.74163872, 0.00055611, 400.80016073, 0.00783196, 40.08001607, 0.02118674, -334.74163872, -0.00055611, -400.80016073, -0.00783196, -40.08001607, -0.02118674, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 374.04008234, 0.00055611, 447.85383048, 0.00783196, 44.78538305, 0.02118674, -374.04008234, -0.00055611, -447.85383048, -0.00783196, -44.78538305, -0.02118674, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 215.24464085, 0.01112215, 215.24464085, 0.03336646, 150.67124859, -1925.98469971, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 53.81116021, 7.049e-05, 161.43348063, 0.00021147, 538.11160212, 0.00070489, -53.81116021, -7.049e-05, -161.43348063, -0.00021147, -538.11160212, -0.00070489, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 215.24464085, 0.01112215, 215.24464085, 0.03336646, 150.67124859, -1925.98469971, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 53.81116021, 7.049e-05, 161.43348063, 0.00021147, 538.11160212, 0.00070489, -53.81116021, -7.049e-05, -161.43348063, -0.00021147, -538.11160212, -0.00070489, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 14.5, 3.55, 0.0)
    ops.node(121009, 14.5, 3.55, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.2025, 28230383.34066348, 11762659.72527645, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 246.95413655, 0.00058027, 296.34220184, 0.01164999, 29.63422018, 0.03330476, -246.95413655, -0.00058027, -296.34220184, -0.01164999, -29.63422018, -0.03330476, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 253.70014833, 0.00058027, 304.43734053, 0.01164999, 30.44373405, 0.03330476, -253.70014833, -0.00058027, -304.43734053, -0.01164999, -30.44373405, -0.03330476, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 189.57471239, 0.01160532, 189.57471239, 0.03481595, 132.70229867, -1792.29432025, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 47.3936781, 6.924e-05, 142.18103429, 0.00020773, 473.93678098, 0.00069242, -47.3936781, -6.924e-05, -142.18103429, -0.00020773, -473.93678098, -0.00069242, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 189.57471239, 0.01160532, 189.57471239, 0.03481595, 132.70229867, -1792.29432025, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 47.3936781, 6.924e-05, 142.18103429, 0.00020773, 473.93678098, 0.00069242, -47.3936781, -6.924e-05, -142.18103429, -0.00020773, -473.93678098, -0.00069242, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 17.65, 3.55, 0.0)
    ops.node(121010, 17.65, 3.55, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.2025, 26200863.45402438, 10917026.43917683, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 233.42589281, 0.00056406, 279.92735169, 0.00979325, 27.99273517, 0.02822039, -233.42589281, -0.00056406, -279.92735169, -0.00979325, -27.99273517, -0.02822039, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 239.63701527, 0.00056406, 287.37581013, 0.00979325, 28.73758101, 0.02822039, -239.63701527, -0.00056406, -287.37581013, -0.00979325, -28.73758101, -0.02822039, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 171.27695948, 0.01128127, 171.27695948, 0.03384381, 119.89387164, -1684.47017863, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 42.81923987, 6.74e-05, 128.45771961, 0.00020221, 428.1923987, 0.00067404, -42.81923987, -6.74e-05, -128.45771961, -0.00020221, -428.1923987, -0.00067404, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 171.27695948, 0.01128127, 171.27695948, 0.03384381, 119.89387164, -1684.47017863, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 42.81923987, 6.74e-05, 128.45771961, 0.00020221, 428.1923987, 0.00067404, -42.81923987, -6.74e-05, -128.45771961, -0.00020221, -428.1923987, -0.00067404, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 24.9, 3.55, 0.0)
    ops.node(121011, 24.9, 3.55, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.25, 25973024.81783127, 10822093.67409636, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 322.90441394, 0.00054189, 386.88258758, 0.00921573, 38.68825876, 0.02323484, -322.90441394, -0.00054189, -386.88258758, -0.00921573, -38.68825876, -0.02323484, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 358.9905209, 0.00054189, 430.11856031, 0.00921573, 43.01185603, 0.02323484, -358.9905209, -0.00054189, -430.11856031, -0.00921573, -43.01185603, -0.02323484, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 218.78718476, 0.01083775, 218.78718476, 0.03251326, 153.15102933, -1918.75252418, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 54.69679619, 7.035e-05, 164.09038857, 0.00021106, 546.9679619, 0.00070354, -54.69679619, -7.035e-05, -164.09038857, -0.00021106, -546.9679619, -0.00070354, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 218.78718476, 0.01083775, 218.78718476, 0.03251326, 153.15102933, -1918.75252418, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 54.69679619, 7.035e-05, 164.09038857, 0.00021106, 546.9679619, 0.00070354, -54.69679619, -7.035e-05, -164.09038857, -0.00021106, -546.9679619, -0.00070354, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 32.15, 3.55, 0.0)
    ops.node(121012, 32.15, 3.55, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 28242818.79137745, 11767841.16307394, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 144.17329061, 0.00064873, 171.50393277, 0.01240605, 17.15039328, 0.03217425, -144.17329061, -0.00064873, -171.50393277, -0.01240605, -17.15039328, -0.03217425, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 128.82083098, 0.00064873, 153.24113811, 0.01240605, 15.32411381, 0.03217425, -128.82083098, -0.00064873, -153.24113811, -0.01240605, -15.32411381, -0.03217425, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 135.94998398, 0.01297453, 135.94998398, 0.0389236, 95.16498879, -1569.69236289, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 33.987496, 8.205e-05, 101.96248799, 0.00024614, 339.87495996, 0.00082048, -33.987496, -8.205e-05, -101.96248799, -0.00024614, -339.87495996, -0.00082048, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 135.94998398, 0.01297453, 135.94998398, 0.0389236, 95.16498879, -1569.69236289, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 33.987496, 8.205e-05, 101.96248799, 0.00024614, 339.87495996, 0.00082048, -33.987496, -8.205e-05, -101.96248799, -0.00024614, -339.87495996, -0.00082048, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 7.1, 0.0)
    ops.node(121013, 0.0, 7.1, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.1225, 27650893.35929574, 11521205.56637323, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 146.54416591, 0.00069864, 174.22659398, 0.01037214, 17.4226594, 0.02897478, -146.54416591, -0.00069864, -174.22659398, -0.01037214, -17.4226594, -0.02897478, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 131.6192841, 0.00069864, 156.48237804, 0.01037214, 15.6482378, 0.02897478, -131.6192841, -0.00069864, -156.48237804, -0.01037214, -15.6482378, -0.02897478, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 129.6261066, 0.01397288, 129.6261066, 0.04191863, 90.73827462, -1493.76312937, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 32.40652665, 7.991e-05, 97.21957995, 0.00023972, 324.06526651, 0.00079906, -32.40652665, -7.991e-05, -97.21957995, -0.00023972, -324.06526651, -0.00079906, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 129.6261066, 0.01397288, 129.6261066, 0.04191863, 90.73827462, -1493.76312937, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 32.40652665, 7.991e-05, 97.21957995, 0.00023972, 324.06526651, 0.00079906, -32.40652665, -7.991e-05, -97.21957995, -0.00023972, -324.06526651, -0.00079906, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 7.25, 7.1, 0.0)
    ops.node(121014, 7.25, 7.1, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.25, 24869145.18893842, 10362143.82872434, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 315.02237729, 0.00053238, 376.74656992, 0.00869091, 37.67465699, 0.02111702, -315.02237729, -0.00053238, -376.74656992, -0.00869091, -37.67465699, -0.02111702, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 350.53988291, 0.00053238, 419.22322992, 0.00869091, 41.92232299, 0.02111702, -350.53988291, -0.00053238, -419.22322992, -0.00869091, -41.92232299, -0.02111702, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 213.44228496, 0.01064754, 213.44228496, 0.03194261, 149.40959947, -1989.68562409, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 53.36057124, 7.168e-05, 160.08171372, 0.00021505, 533.60571239, 0.00071682, -53.36057124, -7.168e-05, -160.08171372, -0.00021505, -533.60571239, -0.00071682, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 213.44228496, 0.01064754, 213.44228496, 0.03194261, 149.40959947, -1989.68562409, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 53.36057124, 7.168e-05, 160.08171372, 0.00021505, 533.60571239, 0.00071682, -53.36057124, -7.168e-05, -160.08171372, -0.00021505, -533.60571239, -0.00071682, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 14.5, 7.1, 0.0)
    ops.node(121015, 14.5, 7.1, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.16, 27553831.27838653, 11480763.03266105, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 175.61881982, 0.00060776, 210.11153524, 0.00948117, 21.01115352, 0.02982639, -175.61881982, -0.00060776, -210.11153524, -0.00948117, -21.01115352, -0.02982639, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 180.69835811, 0.00060776, 216.18872896, 0.00948117, 21.6188729, 0.02982639, -180.69835811, -0.00060776, -216.18872896, -0.00948117, -21.6188729, -0.02982639, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 149.03098741, 0.01215512, 149.03098741, 0.03646535, 104.32169119, -1495.97957015, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 37.25774685, 7.058e-05, 111.77324056, 0.00021175, 372.57746854, 0.00070584, -37.25774685, -7.058e-05, -111.77324056, -0.00021175, -372.57746854, -0.00070584, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 149.03098741, 0.01215512, 149.03098741, 0.03646535, 104.32169119, -1495.97957015, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 37.25774685, 7.058e-05, 111.77324056, 0.00021175, 372.57746854, 0.00070584, -37.25774685, -7.058e-05, -111.77324056, -0.00021175, -372.57746854, -0.00070584, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 17.65, 7.1, 0.0)
    ops.node(121016, 17.65, 7.1, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.16, 25335490.09793978, 10556454.20747491, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 176.42097098, 0.00061235, 210.47576553, 0.00959376, 21.04757655, 0.02576659, -176.42097098, -0.00061235, -210.47576553, -0.00959376, -21.04757655, -0.02576659, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 181.87044054, 0.00061235, 216.97715406, 0.00959376, 21.69771541, 0.02576659, -181.87044054, -0.00061235, -216.97715406, -0.00959376, -21.69771541, -0.02576659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 139.39059588, 0.01224695, 139.39059588, 0.03674085, 97.57341712, -1524.05738054, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 34.84764897, 7.18e-05, 104.54294691, 0.0002154, 348.47648971, 0.00071798, -34.84764897, -7.18e-05, -104.54294691, -0.0002154, -348.47648971, -0.00071798, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 139.39059588, 0.01224695, 139.39059588, 0.03674085, 97.57341712, -1524.05738054, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 34.84764897, 7.18e-05, 104.54294691, 0.0002154, 348.47648971, 0.00071798, -34.84764897, -7.18e-05, -104.54294691, -0.0002154, -348.47648971, -0.00071798, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 24.9, 7.1, 0.0)
    ops.node(121017, 24.9, 7.1, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.25, 29494634.06406985, 12289430.8600291, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 338.84763253, 0.00053827, 406.11344582, 0.008431, 40.61134458, 0.02674987, -338.84763253, -0.00053827, -406.11344582, -0.008431, -40.61134458, -0.02674987, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 377.65652412, 0.00053827, 452.62642445, 0.008431, 45.26264244, 0.02674987, -377.65652412, -0.00053827, -452.62642445, -0.008431, -45.26264244, -0.02674987, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 247.88371638, 0.01076535, 247.88371638, 0.03229606, 173.51860146, -1893.49177507, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 61.97092909, 7.019e-05, 185.91278728, 0.00021058, 619.70929094, 0.00070193, -61.97092909, -7.019e-05, -185.91278728, -0.00021058, -619.70929094, -0.00070193, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 247.88371638, 0.01076535, 247.88371638, 0.03229606, 173.51860146, -1893.49177507, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 61.97092909, 7.019e-05, 185.91278728, 0.00021058, 619.70929094, 0.00070193, -61.97092909, -7.019e-05, -185.91278728, -0.00021058, -619.70929094, -0.00070193, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 32.15, 7.1, 0.0)
    ops.node(121018, 32.15, 7.1, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.1225, 30201907.96195455, 12584128.31748106, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 145.36750664, 0.00067676, 172.95047609, 0.01145592, 17.29504761, 0.03480335, -145.36750664, -0.00067676, -172.95047609, -0.01145592, -17.29504761, -0.03480335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 131.18961518, 0.00067676, 156.08237994, 0.01145592, 15.60823799, 0.03480335, -131.18961518, -0.00067676, -156.08237994, -0.01145592, -15.60823799, -0.03480335, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 138.84547234, 0.01353526, 138.84547234, 0.04060578, 97.19183064, -1468.29124074, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 34.71136808, 7.836e-05, 104.13410425, 0.00023508, 347.11368084, 0.0007836, -34.71136808, -7.836e-05, -104.13410425, -0.00023508, -347.11368084, -0.0007836, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 138.84547234, 0.01353526, 138.84547234, 0.04060578, 97.19183064, -1468.29124074, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 34.71136808, 7.836e-05, 104.13410425, 0.00023508, 347.11368084, 0.0007836, -34.71136808, -7.836e-05, -104.13410425, -0.00023508, -347.11368084, -0.0007836, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 10.65, 0.0)
    ops.node(121019, 0.0, 10.65, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.09, 27433849.34831724, 11430770.56179885, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 99.79812071, 0.00079878, 118.68969023, 0.00960778, 11.86896902, 0.03025495, -99.79812071, -0.00079878, -118.68969023, -0.00960778, -11.86896902, -0.03025495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 91.53255011, 0.00079878, 108.8594649, 0.00960778, 10.88594649, 0.03025495, -91.53255011, -0.00079878, -108.8594649, -0.00960778, -10.88594649, -0.03025495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 86.70156752, 0.01597562, 86.70156752, 0.04792685, 60.69109727, -1083.4521598, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 21.67539188, 7.332e-05, 65.02617564, 0.00021996, 216.75391881, 0.00073321, -21.67539188, -7.332e-05, -65.02617564, -0.00021996, -216.75391881, -0.00073321, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 86.70156752, 0.01597562, 86.70156752, 0.04792685, 60.69109727, -1083.4521598, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 21.67539188, 7.332e-05, 65.02617564, 0.00021996, 216.75391881, 0.00073321, -21.67539188, -7.332e-05, -65.02617564, -0.00021996, -216.75391881, -0.00073321, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 7.25, 10.65, 0.0)
    ops.node(121020, 7.25, 10.65, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.2025, 30115486.64328622, 12548119.43470259, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 242.9388037, 0.00059637, 290.54703292, 0.00843964, 29.05470329, 0.03424918, -242.9388037, -0.00059637, -290.54703292, -0.00843964, -29.05470329, -0.03424918, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 269.28942358, 0.00059637, 322.06153082, 0.00843964, 32.20615308, 0.03424918, -269.28942358, -0.00059637, -322.06153082, -0.00843964, -32.20615308, -0.03424918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 204.32586281, 0.01192736, 204.32586281, 0.03578207, 143.02810397, -1865.67001122, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 51.0814657, 6.996e-05, 153.24439711, 0.00020987, 510.81465702, 0.00069958, -51.0814657, -6.996e-05, -153.24439711, -0.00020987, -510.81465702, -0.00069958, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 204.32586281, 0.01192736, 204.32586281, 0.03578207, 143.02810397, -1865.67001122, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 51.0814657, 6.996e-05, 153.24439711, 0.00020987, 510.81465702, 0.00069958, -51.0814657, -6.996e-05, -153.24439711, -0.00020987, -510.81465702, -0.00069958, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 14.5, 10.65, 0.0)
    ops.node(121021, 14.5, 10.65, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.1225, 24201301.1982156, 10083875.4992565, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 123.07072846, 0.00070547, 145.59546465, 0.01008324, 14.55954647, 0.02481633, -123.07072846, -0.00070547, -145.59546465, -0.01008324, -14.55954647, -0.02481633, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 123.07072846, 0.00070547, 145.59546465, 0.01008324, 14.55954647, 0.02481633, -123.07072846, -0.00070547, -145.59546465, -0.01008324, -14.55954647, -0.02481633, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 126.36990769, 0.01410942, 126.36990769, 0.04232826, 88.45893538, -1679.8961572, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 31.59247692, 8.9e-05, 94.77743077, 0.00026701, 315.92476923, 0.00089002, -31.59247692, -8.9e-05, -94.77743077, -0.00026701, -315.92476923, -0.00089002, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 126.36990769, 0.01410942, 126.36990769, 0.04232826, 88.45893538, -1679.8961572, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 31.59247692, 8.9e-05, 94.77743077, 0.00026701, 315.92476923, 0.00089002, -31.59247692, -8.9e-05, -94.77743077, -0.00026701, -315.92476923, -0.00089002, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 17.65, 10.65, 0.0)
    ops.node(121022, 17.65, 10.65, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.1225, 27502072.27622139, 11459196.78175891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 123.14129083, 0.0006856, 146.80872443, 0.01037736, 14.68087244, 0.03315275, -123.14129083, -0.0006856, -146.80872443, -0.01037736, -14.68087244, -0.03315275, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 123.14129083, 0.0006856, 146.80872443, 0.01037736, 14.68087244, 0.03315275, -123.14129083, -0.0006856, -146.80872443, -0.01037736, -14.68087244, -0.03315275, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 129.35482801, 0.013712, 129.35482801, 0.041136, 90.54837961, -1474.75130533, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 32.338707, 8.017e-05, 97.01612101, 0.00024051, 323.38707004, 0.0008017, -32.338707, -8.017e-05, -97.01612101, -0.00024051, -323.38707004, -0.0008017, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 129.35482801, 0.013712, 129.35482801, 0.041136, 90.54837961, -1474.75130533, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 32.338707, 8.017e-05, 97.01612101, 0.00024051, 323.38707004, 0.0008017, -32.338707, -8.017e-05, -97.01612101, -0.00024051, -323.38707004, -0.0008017, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 24.9, 10.65, 0.0)
    ops.node(121023, 24.9, 10.65, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.2025, 23975001.20258065, 9989583.83440861, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 226.55784164, 0.00058385, 269.48964818, 0.00874695, 26.94896482, 0.02308222, -226.55784164, -0.00058385, -269.48964818, -0.00874695, -26.94896482, -0.02308222, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 252.37326382, 0.00058385, 300.19698981, 0.00874695, 30.01969898, 0.02308222, -252.37326382, -0.00058385, -300.19698981, -0.00874695, -30.01969898, -0.02308222, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 168.41765306, 0.01167698, 168.41765306, 0.03503093, 117.89235714, -1927.85055841, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 42.10441326, 7.243e-05, 126.31323979, 0.0002173, 421.04413265, 0.00072433, -42.10441326, -7.243e-05, -126.31323979, -0.0002173, -421.04413265, -0.00072433, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 168.41765306, 0.01167698, 168.41765306, 0.03503093, 117.89235714, -1927.85055841, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 42.10441326, 7.243e-05, 126.31323979, 0.0002173, 421.04413265, 0.00072433, -42.10441326, -7.243e-05, -126.31323979, -0.0002173, -421.04413265, -0.00072433, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 32.15, 10.65, 0.0)
    ops.node(121024, 32.15, 10.65, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.09, 27025307.15290509, 11260544.64704379, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 96.5374818, 0.00077796, 114.74487241, 0.00946981, 11.47448724, 0.02918852, -96.5374818, -0.00077796, -114.74487241, -0.00946981, -11.47448724, -0.02918852, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 88.73179867, 0.00077796, 105.46700336, 0.00946981, 10.54670034, 0.02918852, -88.73179867, -0.00077796, -105.46700336, -0.00946981, -10.54670034, -0.02918852, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 83.98891548, 0.01555916, 83.98891548, 0.04667749, 58.79224083, -1083.74038381, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 20.99722887, 7.21e-05, 62.99168661, 0.0002163, 209.97228869, 0.00072101, -20.99722887, -7.21e-05, -62.99168661, -0.0002163, -209.97228869, -0.00072101, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 83.98891548, 0.01555916, 83.98891548, 0.04667749, 58.79224083, -1083.74038381, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 20.99722887, 7.21e-05, 62.99168661, 0.0002163, 209.97228869, 0.00072101, -20.99722887, -7.21e-05, -62.99168661, -0.0002163, -209.97228869, -0.00072101, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.225)
    ops.node(122001, 0.0, 0.0, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 24433034.88105787, 10180431.20044078, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 86.3315715, 0.0008405, 103.09732545, 0.01252232, 10.30973254, 0.03186456, -86.3315715, -0.0008405, -103.09732545, -0.01252232, -10.30973254, -0.03186456, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 77.32549138, 0.0008405, 92.34224759, 0.01252232, 9.23422476, 0.03186456, -77.32549138, -0.0008405, -92.34224759, -0.01252232, -9.23422476, -0.03186456, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 86.06261876, 0.01681003, 86.06261876, 0.05043009, 60.24383313, -1057.09508064, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 21.51565469, 8.172e-05, 64.54696407, 0.00024516, 215.15654691, 0.00081719, -21.51565469, -8.172e-05, -64.54696407, -0.00024516, -215.15654691, -0.00081719, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 86.06261876, 0.01681003, 86.06261876, 0.05043009, 60.24383313, -1057.09508064, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 21.51565469, 8.172e-05, 64.54696407, 0.00024516, 215.15654691, 0.00081719, -21.51565469, -8.172e-05, -64.54696407, -0.00024516, -215.15654691, -0.00081719, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 7.25, 0.0, 3.225)
    ops.node(122002, 7.25, 0.0, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.2025, 24791109.24488717, 10329628.85203632, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 189.31798253, 0.00056942, 227.75127263, 0.00982718, 22.77512726, 0.0284296, -189.31798253, -0.00056942, -227.75127263, -0.00982718, -22.77512726, -0.0284296, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 172.1549536, 0.00056942, 207.10399112, 0.00982718, 20.71039911, 0.0284296, -172.1549536, -0.00056942, -207.10399112, -0.00982718, -20.71039911, -0.0284296, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 157.87491422, 0.01138834, 157.87491422, 0.03416501, 110.51243995, -1550.07047348, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 39.46872855, 6.566e-05, 118.40618566, 0.00019699, 394.68728554, 0.00065663, -39.46872855, -6.566e-05, -118.40618566, -0.00019699, -394.68728554, -0.00065663, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 157.87491422, 0.01138834, 157.87491422, 0.03416501, 110.51243995, -1550.07047348, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 39.46872855, 6.566e-05, 118.40618566, 0.00019699, 394.68728554, 0.00065663, -39.46872855, -6.566e-05, -118.40618566, -0.00019699, -394.68728554, -0.00065663, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 24.9, 0.0, 3.225)
    ops.node(122005, 24.9, 0.0, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.2025, 28081799.69338064, 11700749.87224193, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 190.31530863, 0.00054036, 229.18449343, 0.01182281, 22.91844934, 0.03561323, -190.31530863, -0.00054036, -229.18449343, -0.01182281, -22.91844934, -0.03561323, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 172.86714708, 0.00054036, 208.17279398, 0.01182281, 20.8172794, 0.03561323, -172.86714708, -0.00054036, -208.17279398, -0.01182281, -20.8172794, -0.03561323, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 181.55929864, 0.01080728, 181.55929864, 0.03242183, 127.09150905, -1628.14907905, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 45.38982466, 6.667e-05, 136.16947398, 0.0002, 453.89824659, 0.00066665, -45.38982466, -6.667e-05, -136.16947398, -0.0002, -453.89824659, -0.00066665, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 181.55929864, 0.01080728, 181.55929864, 0.03242183, 127.09150905, -1628.14907905, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 45.38982466, 6.667e-05, 136.16947398, 0.0002, 453.89824659, 0.00066665, -45.38982466, -6.667e-05, -136.16947398, -0.0002, -453.89824659, -0.00066665, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 32.15, 0.0, 3.225)
    ops.node(122006, 32.15, 0.0, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.09, 25671816.96329775, 10696590.40137406, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 80.70023804, 0.00073394, 96.61451473, 0.01204239, 9.66145147, 0.03443139, -80.70023804, -0.00073394, -96.61451473, -0.01204239, -9.66145147, -0.03443139, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 72.1151526, 0.00073394, 86.33643027, 0.01204239, 8.63364303, 0.03443139, -72.1151526, -0.00073394, -86.33643027, -0.01204239, -8.63364303, -0.03443139, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 82.46191396, 0.01467889, 82.46191396, 0.04403666, 57.72333977, -950.79014616, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 20.61547849, 7.452e-05, 61.84643547, 0.00022357, 206.1547849, 0.00074522, -20.61547849, -7.452e-05, -61.84643547, -0.00022357, -206.1547849, -0.00074522, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 82.46191396, 0.01467889, 82.46191396, 0.04403666, 57.72333977, -950.79014616, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 20.61547849, 7.452e-05, 61.84643547, 0.00022357, 206.1547849, 0.00074522, -20.61547849, -7.452e-05, -61.84643547, -0.00022357, -206.1547849, -0.00074522, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 3.55, 3.25)
    ops.node(122007, 0.0, 3.55, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 24562320.24335422, 10234300.10139759, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 142.06868969, 0.00068132, 169.50051396, 0.00989743, 16.9500514, 0.02687011, -142.06868969, -0.00068132, -169.50051396, -0.00989743, -16.9500514, -0.02687011, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 118.93185214, 0.00068132, 141.89622012, 0.00989743, 14.18962201, 0.02687011, -118.93185214, -0.00068132, -141.89622012, -0.00989743, -14.18962201, -0.02687011, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 104.06785117, 0.01362637, 104.06785117, 0.04087911, 72.84749582, -1159.35072798, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 26.01696279, 7.222e-05, 78.05088838, 0.00021665, 260.16962792, 0.00072217, -26.01696279, -7.222e-05, -78.05088838, -0.00021665, -260.16962792, -0.00072217, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 104.06785117, 0.01362637, 104.06785117, 0.04087911, 72.84749582, -1159.35072798, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 26.01696279, 7.222e-05, 78.05088838, 0.00021665, 260.16962792, 0.00072217, -26.01696279, -7.222e-05, -78.05088838, -0.00021665, -260.16962792, -0.00072217, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 7.25, 3.55, 3.25)
    ops.node(122008, 7.25, 3.55, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.25, 25627691.6281012, 10678204.84504217, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 237.41023249, 0.00051449, 286.20779687, 0.00889863, 28.62077969, 0.02538969, -237.41023249, -0.00051449, -286.20779687, -0.00889863, -28.62077969, -0.02538969, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 226.31969279, 0.00051449, 272.83769526, 0.00889863, 27.28376953, 0.02538969, -226.31969279, -0.00051449, -272.83769526, -0.00889863, -27.28376953, -0.02538969, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 199.92360123, 0.01028986, 199.92360123, 0.03086957, 139.94652086, -1560.37437878, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 49.98090031, 6.515e-05, 149.94270092, 0.00019546, 499.80900308, 0.00065155, -49.98090031, -6.515e-05, -149.94270092, -0.00019546, -499.80900308, -0.00065155, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 199.92360123, 0.01028986, 199.92360123, 0.03086957, 139.94652086, -1560.37437878, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 49.98090031, 6.515e-05, 149.94270092, 0.00019546, 499.80900308, 0.00065155, -49.98090031, -6.515e-05, -149.94270092, -0.00019546, -499.80900308, -0.00065155, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 14.5, 3.55, 3.25)
    ops.node(122009, 14.5, 3.55, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.2025, 26532138.40400457, 11055057.66833524, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 176.50814564, 0.00051713, 212.97297108, 0.01217216, 21.29729711, 0.03477705, -176.50814564, -0.00051713, -212.97297108, -0.01217216, -21.29729711, -0.03477705, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 159.54322686, 0.00051713, 192.503269, 0.01217216, 19.2503269, 0.03477705, -159.54322686, -0.00051713, -192.503269, -0.01217216, -19.2503269, -0.03477705, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 167.76721722, 0.01034256, 167.76721722, 0.03102767, 117.43705205, -1535.62674491, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 41.9418043, 6.52e-05, 125.82541291, 0.0001956, 419.41804304, 0.00065199, -41.9418043, -6.52e-05, -125.82541291, -0.0001956, -419.41804304, -0.00065199, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 167.76721722, 0.01034256, 167.76721722, 0.03102767, 117.43705205, -1535.62674491, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 41.9418043, 6.52e-05, 125.82541291, 0.0001956, 419.41804304, 0.00065199, -41.9418043, -6.52e-05, -125.82541291, -0.0001956, -419.41804304, -0.00065199, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 17.65, 3.55, 3.25)
    ops.node(122010, 17.65, 3.55, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.2025, 27270427.59172032, 11362678.1632168, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 185.74637308, 0.00054948, 224.08918036, 0.0120419, 22.40891804, 0.03571619, -185.74637308, -0.00054948, -224.08918036, -0.0120419, -22.40891804, -0.03571619, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 167.70601416, 0.00054948, 202.32482945, 0.0120419, 20.23248295, 0.03571619, -167.70601416, -0.00054948, -202.32482945, -0.0120419, -20.23248295, -0.03571619, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 171.15089321, 0.01098969, 171.15089321, 0.03296906, 119.80562525, -1513.24457921, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 42.7877233, 6.471e-05, 128.36316991, 0.00019414, 427.87723302, 0.00064713, -42.7877233, -6.471e-05, -128.36316991, -0.00019414, -427.87723302, -0.00064713, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 171.15089321, 0.01098969, 171.15089321, 0.03296906, 119.80562525, -1513.24457921, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 42.7877233, 6.471e-05, 128.36316991, 0.00019414, 427.87723302, 0.00064713, -42.7877233, -6.471e-05, -128.36316991, -0.00019414, -427.87723302, -0.00064713, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 24.9, 3.55, 3.25)
    ops.node(122011, 24.9, 3.55, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.25, 25479924.09391183, 10616635.03912993, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 247.06478642, 0.00052495, 297.81695207, 0.00800127, 29.78169521, 0.0242971, -247.06478642, -0.00052495, -297.81695207, -0.00800127, -29.78169521, -0.0242971, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 234.72450149, 0.00052495, 282.94171996, 0.00800127, 28.294172, 0.0242971, -234.72450149, -0.00052495, -282.94171996, -0.00800127, -28.294172, -0.0242971, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 197.0808505, 0.01049907, 197.0808505, 0.03149722, 137.95659535, -1529.40254177, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 49.27021263, 6.46e-05, 147.81063788, 0.0001938, 492.70212626, 0.00064601, -49.27021263, -6.46e-05, -147.81063788, -0.0001938, -492.70212626, -0.00064601, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 197.0808505, 0.01049907, 197.0808505, 0.03149722, 137.95659535, -1529.40254177, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 49.27021263, 6.46e-05, 147.81063788, 0.0001938, 492.70212626, 0.00064601, -49.27021263, -6.46e-05, -147.81063788, -0.0001938, -492.70212626, -0.00064601, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 32.15, 3.55, 3.25)
    ops.node(122012, 32.15, 3.55, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 28372971.32706002, 11822071.38627501, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 140.72998376, 0.00066987, 168.60724901, 0.01213175, 16.8607249, 0.03683312, -140.72998376, -0.00066987, -168.60724901, -0.01213175, -16.8607249, -0.03683312, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 119.56242211, 0.00066987, 143.24659564, 0.01213175, 14.32465956, 0.03683312, -119.56242211, -0.00066987, -143.24659564, -0.01213175, -14.32465956, -0.03683312, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 119.85904553, 0.01339746, 119.85904553, 0.04019238, 83.90133187, -1185.1062459, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 29.96476138, 7.2e-05, 89.89428414, 0.00021601, 299.64761381, 0.00072005, -29.96476138, -7.2e-05, -89.89428414, -0.00021601, -299.64761381, -0.00072005, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 119.85904553, 0.01339746, 119.85904553, 0.04019238, 83.90133187, -1185.1062459, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 29.96476138, 7.2e-05, 89.89428414, 0.00021601, 299.64761381, 0.00072005, -29.96476138, -7.2e-05, -89.89428414, -0.00021601, -299.64761381, -0.00072005, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 7.1, 3.25)
    ops.node(122013, 0.0, 7.1, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.1225, 27364793.8075369, 11401997.41980704, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 139.14690298, 0.00067446, 166.69188784, 0.01027563, 16.66918878, 0.03312539, -139.14690298, -0.00067446, -166.69188784, -0.01027563, -16.66918878, -0.03312539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 118.32264711, 0.00067446, 141.7453425, 0.01027563, 14.17453425, 0.03312539, -118.32264711, -0.00067446, -141.7453425, -0.01027563, -14.17453425, -0.03312539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 108.59150235, 0.01348911, 108.59150235, 0.04046732, 76.01405164, -1113.12378952, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 27.14787559, 6.764e-05, 81.44362676, 0.00020292, 271.47875587, 0.00067639, -27.14787559, -6.764e-05, -81.44362676, -0.00020292, -271.47875587, -0.00067639, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 108.59150235, 0.01348911, 108.59150235, 0.04046732, 76.01405164, -1113.12378952, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 27.14787559, 6.764e-05, 81.44362676, 0.00020292, 271.47875587, 0.00067639, -27.14787559, -6.764e-05, -81.44362676, -0.00020292, -271.47875587, -0.00067639, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 7.25, 7.1, 3.25)
    ops.node(122014, 7.25, 7.1, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.25, 27502014.1356547, 11459172.55652279, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 240.38947703, 0.00051486, 289.84081478, 0.00907333, 28.98408148, 0.02782188, -240.38947703, -0.00051486, -289.84081478, -0.00907333, -28.98408148, -0.02782188, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 229.32286559, 0.00051486, 276.49765302, 0.00907333, 27.6497653, 0.02782188, -229.32286559, -0.00051486, -276.49765302, -0.00907333, -27.6497653, -0.02782188, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 216.66214437, 0.01029721, 216.66214437, 0.03089162, 151.66350106, -1586.57331101, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 54.16553609, 6.58e-05, 162.49660828, 0.00019739, 541.65536093, 0.00065797, -54.16553609, -6.58e-05, -162.49660828, -0.00019739, -541.65536093, -0.00065797, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 216.66214437, 0.01029721, 216.66214437, 0.03089162, 151.66350106, -1586.57331101, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 54.16553609, 6.58e-05, 162.49660828, 0.00019739, 541.65536093, 0.00065797, -54.16553609, -6.58e-05, -162.49660828, -0.00019739, -541.65536093, -0.00065797, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 14.5, 7.1, 3.25)
    ops.node(122015, 14.5, 7.1, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.16, 26768059.92980502, 11153358.30408542, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 138.26557977, 0.00055732, 166.38432949, 0.01217021, 16.63843295, 0.03506809, -138.26557977, -0.00055732, -166.38432949, -0.01217021, -16.63843295, -0.03506809, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 127.9849363, 0.00055732, 154.01293544, 0.01217021, 15.40129354, 0.03506809, -127.9849363, -0.00055732, -154.01293544, -0.01217021, -15.40129354, -0.03506809, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 140.61914986, 0.01114648, 140.61914986, 0.03343943, 98.43340491, -1362.68486296, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 35.15478747, 6.855e-05, 105.4643624, 0.00020566, 351.54787466, 0.00068555, -35.15478747, -6.855e-05, -105.4643624, -0.00020566, -351.54787466, -0.00068555, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 140.61914986, 0.01114648, 140.61914986, 0.03343943, 98.43340491, -1362.68486296, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 35.15478747, 6.855e-05, 105.4643624, 0.00020566, 351.54787466, 0.00068555, -35.15478747, -6.855e-05, -105.4643624, -0.00020566, -351.54787466, -0.00068555, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 17.65, 7.1, 3.25)
    ops.node(122016, 17.65, 7.1, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.16, 29571098.93943129, 12321291.22476304, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 139.59774507, 0.00056092, 167.73171053, 0.01280587, 16.77317105, 0.03987722, -139.59774507, -0.00056092, -167.73171053, -0.01280587, -16.77317105, -0.03987722, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 129.70338947, 0.00056092, 155.84328648, 0.01280587, 15.58432865, 0.03987722, -129.70338947, -0.00056092, -155.84328648, -0.01280587, -15.58432865, -0.03987722, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 156.65387783, 0.01121844, 156.65387783, 0.03365531, 109.65771448, -1407.96975886, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 39.16346946, 6.913e-05, 117.49040837, 0.0002074, 391.63469456, 0.00069133, -39.16346946, -6.913e-05, -117.49040837, -0.0002074, -391.63469456, -0.00069133, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 156.65387783, 0.01121844, 156.65387783, 0.03365531, 109.65771448, -1407.96975886, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 39.16346946, 6.913e-05, 117.49040837, 0.0002074, 391.63469456, 0.00069133, -39.16346946, -6.913e-05, -117.49040837, -0.0002074, -391.63469456, -0.00069133, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 24.9, 7.1, 3.25)
    ops.node(122017, 24.9, 7.1, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.25, 27973264.05106907, 11655526.68794545, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 234.51505408, 0.00053001, 282.68355509, 0.01026434, 28.26835551, 0.02951886, -234.51505408, -0.00053001, -282.68355509, -0.01026434, -28.26835551, -0.02951886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 225.03289826, 0.00053001, 271.25380051, 0.01026434, 27.12538005, 0.02951886, -225.03289826, -0.00053001, -271.25380051, -0.01026434, -27.12538005, -0.02951886, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 223.39576232, 0.01060026, 223.39576232, 0.03180079, 156.37703362, -1640.00967447, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 55.84894058, 6.67e-05, 167.54682174, 0.0002001, 558.4894058, 0.00066699, -55.84894058, -6.67e-05, -167.54682174, -0.0002001, -558.4894058, -0.00066699, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 223.39576232, 0.01060026, 223.39576232, 0.03180079, 156.37703362, -1640.00967447, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 55.84894058, 6.67e-05, 167.54682174, 0.0002001, 558.4894058, 0.00066699, -55.84894058, -6.67e-05, -167.54682174, -0.0002001, -558.4894058, -0.00066699, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 32.15, 7.1, 3.25)
    ops.node(122018, 32.15, 7.1, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.1225, 25139062.19864048, 10474609.24943353, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 128.15541525, 0.00066, 153.10886886, 0.01055826, 15.31088689, 0.02881984, -128.15541525, -0.00066, -153.10886886, -0.01055826, -15.31088689, -0.02881984, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 110.11171599, 0.00066, 131.55183689, 0.01055826, 13.15518369, 0.02881984, -110.11171599, -0.00066, -131.55183689, -0.01055826, -13.15518369, -0.02881984, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 108.52868085, 0.01320005, 108.52868085, 0.03960014, 75.9700766, -1205.35358479, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 27.13217021, 7.359e-05, 81.39651064, 0.00022076, 271.32170213, 0.00073585, -27.13217021, -7.359e-05, -81.39651064, -0.00022076, -271.32170213, -0.00073585, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 108.52868085, 0.01320005, 108.52868085, 0.03960014, 75.9700766, -1205.35358479, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 27.13217021, 7.359e-05, 81.39651064, 0.00022076, 271.32170213, 0.00073585, -27.13217021, -7.359e-05, -81.39651064, -0.00022076, -271.32170213, -0.00073585, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 10.65, 3.225)
    ops.node(122019, 0.0, 10.65, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.09, 28802688.24714015, 12001120.10297506, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 90.63155166, 0.00075056, 108.65053532, 0.01251554, 10.86505353, 0.04155301, -90.63155166, -0.00075056, -108.65053532, -0.01251554, -10.86505353, -0.04155301, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 79.98048224, 0.00075056, 95.88186511, 0.01251554, 9.58818651, 0.04155301, -79.98048224, -0.00075056, -95.88186511, -0.01251554, -9.58818651, -0.04155301, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 90.81343926, 0.01501112, 90.81343926, 0.04503337, 63.56940748, -930.69611484, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 22.70335981, 7.315e-05, 68.11007944, 0.00021945, 227.03359815, 0.00073148, -22.70335981, -7.315e-05, -68.11007944, -0.00021945, -227.03359815, -0.00073148, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 90.81343926, 0.01501112, 90.81343926, 0.04503337, 63.56940748, -930.69611484, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 22.70335981, 7.315e-05, 68.11007944, 0.00021945, 227.03359815, 0.00073148, -22.70335981, -7.315e-05, -68.11007944, -0.00021945, -227.03359815, -0.00073148, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 7.25, 10.65, 3.225)
    ops.node(122020, 7.25, 10.65, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.2025, 32318170.82684648, 13465904.51118603, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 177.52744138, 0.00049683, 212.3534279, 0.01103378, 21.23534279, 0.04311447, -177.52744138, -0.00049683, -212.3534279, -0.01103378, -21.23534279, -0.04311447, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 156.24698324, 0.00049683, 186.89833094, 0.01103378, 18.68983309, 0.04311447, -156.24698324, -0.00049683, -186.89833094, -0.01103378, -18.68983309, -0.04311447, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 208.24701824, 0.00993662, 208.24701824, 0.02980987, 145.77291277, -1615.80002639, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 52.06175456, 6.644e-05, 156.18526368, 0.00019932, 520.61754561, 0.00066441, -52.06175456, -6.644e-05, -156.18526368, -0.00019932, -520.61754561, -0.00066441, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 208.24701824, 0.00993662, 208.24701824, 0.02980987, 145.77291277, -1615.80002639, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 52.06175456, 6.644e-05, 156.18526368, 0.00019932, 520.61754561, 0.00066441, -52.06175456, -6.644e-05, -156.18526368, -0.00019932, -520.61754561, -0.00066441, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 14.5, 10.65, 3.225)
    ops.node(122021, 14.5, 10.65, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.1225, 27469593.70963404, 11445664.04568085, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 94.57187934, 0.00062358, 113.58198389, 0.01082445, 11.35819839, 0.03912683, -94.57187934, -0.00062358, -113.58198389, -0.01082445, -11.35819839, -0.03912683, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 86.42723558, 0.00062358, 103.80016712, 0.01082445, 10.38001671, 0.03912683, -86.42723558, -0.00062358, -103.80016712, -0.01082445, -10.38001671, -0.03912683, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 120.00778714, 0.0124716, 120.00778714, 0.0374148, 84.005451, -1252.0773744, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 30.00194679, 7.446e-05, 90.00584036, 0.00022339, 300.01946786, 0.00074465, -30.00194679, -7.446e-05, -90.00584036, -0.00022339, -300.01946786, -0.00074465, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 120.00778714, 0.0124716, 120.00778714, 0.0374148, 84.005451, -1252.0773744, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 30.00194679, 7.446e-05, 90.00584036, 0.00022339, 300.01946786, 0.00074465, -30.00194679, -7.446e-05, -90.00584036, -0.00022339, -300.01946786, -0.00074465, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 17.65, 10.65, 3.225)
    ops.node(122022, 17.65, 10.65, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.1225, 30668497.86614798, 12778540.77756166, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 93.44601245, 0.00059636, 111.94283262, 0.01321624, 11.19428326, 0.04727488, -93.44601245, -0.00059636, -111.94283262, -0.01321624, -11.19428326, -0.04727488, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 85.78880831, 0.00059636, 102.76995195, 0.01321624, 10.27699519, 0.04727488, -85.78880831, -0.00059636, -102.76995195, -0.01321624, -10.27699519, -0.04727488, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 135.38017838, 0.01192722, 135.38017838, 0.03578165, 94.76612487, -1315.98362532, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 33.8450446, 7.524e-05, 101.53513379, 0.00022572, 338.45044595, 0.00075241, -33.8450446, -7.524e-05, -101.53513379, -0.00022572, -338.45044595, -0.00075241, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 135.38017838, 0.01192722, 135.38017838, 0.03578165, 94.76612487, -1315.98362532, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 33.8450446, 7.524e-05, 101.53513379, 0.00022572, 338.45044595, 0.00075241, -33.8450446, -7.524e-05, -101.53513379, -0.00022572, -338.45044595, -0.00075241, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 24.9, 10.65, 3.225)
    ops.node(122023, 24.9, 10.65, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.2025, 26479004.57992667, 11032918.57496945, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 180.51659593, 0.00051673, 217.45367468, 0.01122486, 21.74536747, 0.03542341, -180.51659593, -0.00051673, -217.45367468, -0.01122486, -21.74536747, -0.03542341, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 156.43800154, 0.00051673, 188.4481486, 0.01122486, 18.84481486, 0.03542341, -156.43800154, -0.00051673, -188.4481486, -0.01122486, -18.84481486, -0.03542341, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 175.107113, 0.01033454, 175.107113, 0.03100361, 122.5749791, -1698.88325486, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 43.77677825, 6.819e-05, 131.33033475, 0.00020456, 437.76778251, 0.00068188, -43.77677825, -6.819e-05, -131.33033475, -0.00020456, -437.76778251, -0.00068188, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 175.107113, 0.01033454, 175.107113, 0.03100361, 122.5749791, -1698.88325486, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 43.77677825, 6.819e-05, 131.33033475, 0.00020456, 437.76778251, 0.00068188, -43.77677825, -6.819e-05, -131.33033475, -0.00020456, -437.76778251, -0.00068188, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 32.15, 10.65, 3.225)
    ops.node(122024, 32.15, 10.65, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.09, 27890818.18734644, 11621174.24472768, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 89.09661584, 0.00078919, 106.8363207, 0.01293846, 10.68363207, 0.04020423, -89.09661584, -0.00078919, -106.8363207, -0.01293846, -10.68363207, -0.04020423, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 79.32656423, 0.00078919, 95.12098946, 0.01293846, 9.51209895, 0.04020423, -79.32656423, -0.00078919, -95.12098946, -0.01293846, -9.51209895, -0.04020423, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 90.67708689, 0.01578383, 90.67708689, 0.0473515, 63.47396082, -949.89401051, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 22.66927172, 7.543e-05, 68.00781517, 0.00022628, 226.69271723, 0.00075427, -22.66927172, -7.543e-05, -68.00781517, -0.00022628, -226.69271723, -0.00075427, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 90.67708689, 0.01578383, 90.67708689, 0.0473515, 63.47396082, -949.89401051, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 22.66927172, 7.543e-05, 68.00781517, 0.00022628, 226.69271723, 0.00075427, -22.66927172, -7.543e-05, -68.00781517, -0.00022628, -226.69271723, -0.00075427, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.125)
    ops.node(123001, 0.0, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 27021734.7892512, 11259056.162188, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 40.52635996, 0.00084506, 48.69088467, 0.01132098, 4.86908847, 0.04245947, -40.52635996, -0.00084506, -48.69088467, -0.01132098, -4.86908847, -0.04245947, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 40.52635996, 0.00084506, 48.69088467, 0.01132098, 4.86908847, 0.04245947, -40.52635996, -0.00084506, -48.69088467, -0.01132098, -4.86908847, -0.04245947, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 44.86798683, 0.01690123, 44.86798683, 0.0507037, 31.40759078, -621.20392646, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 11.21699671, 5.547e-05, 33.65099012, 0.00016642, 112.16996708, 0.00055472, -11.21699671, -5.547e-05, -33.65099012, -0.00016642, -112.16996708, -0.00055472, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 44.86798683, 0.01690123, 44.86798683, 0.0507037, 31.40759078, -621.20392646, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 11.21699671, 5.547e-05, 33.65099012, 0.00016642, 112.16996708, 0.00055472, -11.21699671, -5.547e-05, -33.65099012, -0.00016642, -112.16996708, -0.00055472, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 7.25, 0.0, 6.125)
    ops.node(123002, 7.25, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1225, 27078712.61291431, 11282796.92204763, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 94.72546286, 0.00064547, 114.00804226, 0.01343762, 11.40080423, 0.03917893, -94.72546286, -0.00064547, -114.00804226, -0.01343762, -11.40080423, -0.03917893, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 90.77760967, 0.00064547, 109.25655307, 0.01343762, 10.92565531, 0.03917893, -90.77760967, -0.00064547, -109.25655307, -0.01343762, -10.92565531, -0.03917893, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 115.05938548, 0.01290933, 115.05938548, 0.038728, 80.54156984, -1177.25727871, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 28.76484637, 7.242e-05, 86.29453911, 0.00021727, 287.64846371, 0.00072425, -28.76484637, -7.242e-05, -86.29453911, -0.00021727, -287.64846371, -0.00072425, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 115.05938548, 0.01290933, 115.05938548, 0.038728, 80.54156984, -1177.25727871, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 28.76484637, 7.242e-05, 86.29453911, 0.00021727, 287.64846371, 0.00072425, -28.76484637, -7.242e-05, -86.29453911, -0.00021727, -287.64846371, -0.00072425, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 24.9, 0.0, 6.125)
    ops.node(123005, 24.9, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 29415860.18708752, 12256608.41128647, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 90.38093267, 0.00061908, 108.62639924, 0.01065324, 10.86263992, 0.04016393, -90.38093267, -0.00061908, -108.62639924, -0.01065324, -10.86263992, -0.04016393, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 87.04793791, 0.00061908, 104.62056295, 0.01065324, 10.4620563, 0.04016393, -87.04793791, -0.00061908, -104.62056295, -0.01065324, -10.4620563, -0.04016393, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 111.54409166, 0.01238166, 111.54409166, 0.03714497, 78.08086416, -986.54536657, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 27.88602291, 6.463e-05, 83.65806874, 0.0001939, 278.86022915, 0.00064634, -27.88602291, -6.463e-05, -83.65806874, -0.0001939, -278.86022915, -0.00064634, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 111.54409166, 0.01238166, 111.54409166, 0.03714497, 78.08086416, -986.54536657, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 27.88602291, 6.463e-05, 83.65806874, 0.0001939, 278.86022915, 0.00064634, -27.88602291, -6.463e-05, -83.65806874, -0.0001939, -278.86022915, -0.00064634, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 32.15, 0.0, 6.125)
    ops.node(123006, 32.15, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 27691366.73448351, 11538069.47270146, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 39.6406122, 0.000859, 47.62886678, 0.01474751, 4.76288668, 0.04744297, -39.6406122, -0.000859, -47.62886678, -0.01474751, -4.76288668, -0.04744297, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 39.6406122, 0.000859, 47.62886678, 0.01474751, 4.76288668, 0.04744297, -39.6406122, -0.000859, -47.62886678, -0.01474751, -4.76288668, -0.04744297, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 61.80590198, 0.0171801, 61.80590198, 0.0515403, 43.26413138, -737.46800369, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 15.45147549, 7.457e-05, 46.35442648, 0.0002237, 154.51475495, 0.00074565, -15.45147549, -7.457e-05, -46.35442648, -0.0002237, -154.51475495, -0.00074565, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 61.80590198, 0.0171801, 61.80590198, 0.0515403, 43.26413138, -737.46800369, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 15.45147549, 7.457e-05, 46.35442648, 0.0002237, 154.51475495, 0.00074565, -15.45147549, -7.457e-05, -46.35442648, -0.0002237, -154.51475495, -0.00074565, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 3.55, 6.15)
    ops.node(123007, 0.0, 3.55, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 31959918.2927652, 13316632.6219855, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 63.8019475, 0.00087517, 75.83750704, 0.01311506, 7.5837507, 0.04747414, -63.8019475, -0.00087517, -75.83750704, -0.01311506, -7.5837507, -0.04747414, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 58.61143573, 0.00087517, 69.66786037, 0.01311506, 6.96678604, 0.04747414, -58.61143573, -0.00087517, -69.66786037, -0.01311506, -6.96678604, -0.04747414, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 64.57817237, 0.01750336, 64.57817237, 0.05251008, 45.20472066, -824.94520189, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 16.14454309, 6.75e-05, 48.43362928, 0.00020251, 161.44543092, 0.00067504, -16.14454309, -6.75e-05, -48.43362928, -0.00020251, -161.44543092, -0.00067504, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 64.57817237, 0.01750336, 64.57817237, 0.05251008, 45.20472066, -824.94520189, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 16.14454309, 6.75e-05, 48.43362928, 0.00020251, 161.44543092, 0.00067504, -16.14454309, -6.75e-05, -48.43362928, -0.00020251, -161.44543092, -0.00067504, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 7.25, 3.55, 6.15)
    ops.node(123008, 7.25, 3.55, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.16, 27745440.79391793, 11560600.33079914, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 140.58092984, 0.00058486, 169.31914255, 0.01061046, 16.93191426, 0.03159855, -140.58092984, -0.00058486, -169.31914255, -0.01061046, -16.93191426, -0.03159855, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 140.58092984, 0.00058486, 169.31914255, 0.01061046, 16.93191426, 0.03159855, -140.58092984, -0.00058486, -169.31914255, -0.01061046, -16.93191426, -0.03159855, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 136.68255499, 0.01169719, 136.68255499, 0.03509158, 95.6777885, -1182.36986342, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 34.17063875, 6.429e-05, 102.51191625, 0.00019286, 341.70638748, 0.00064288, -34.17063875, -6.429e-05, -102.51191625, -0.00019286, -341.70638748, -0.00064288, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 136.68255499, 0.01169719, 136.68255499, 0.03509158, 95.6777885, -1182.36986342, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 34.17063875, 6.429e-05, 102.51191625, 0.00019286, 341.70638748, 0.00064288, -34.17063875, -6.429e-05, -102.51191625, -0.00019286, -341.70638748, -0.00064288, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 14.5, 3.55, 6.15)
    ops.node(123009, 14.5, 3.55, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 24236924.1569918, 10098718.39874659, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 90.5653326, 0.00062256, 108.81145416, 0.01154249, 10.88114542, 0.03208744, -90.5653326, -0.00062256, -108.81145416, -0.01154249, -10.88114542, -0.03208744, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 86.52578895, 0.00062256, 103.95806704, 0.01154249, 10.3958067, 0.03208744, -86.52578895, -0.00062256, -103.95806704, -0.01154249, -10.3958067, -0.03208744, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 101.73123205, 0.01245118, 101.73123205, 0.03735353, 71.21186243, -1110.79586597, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 25.43280801, 7.154e-05, 76.29842403, 0.00021463, 254.32808012, 0.00071544, -25.43280801, -7.154e-05, -76.29842403, -0.00021463, -254.32808012, -0.00071544, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 101.73123205, 0.01245118, 101.73123205, 0.03735353, 71.21186243, -1110.79586597, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 25.43280801, 7.154e-05, 76.29842403, 0.00021463, 254.32808012, 0.00071544, -25.43280801, -7.154e-05, -76.29842403, -0.00021463, -254.32808012, -0.00071544, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 17.65, 3.55, 6.15)
    ops.node(123010, 17.65, 3.55, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 26637972.97810646, 11099155.40754436, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 93.92907973, 0.0006918, 113.11934351, 0.01034153, 11.31193435, 0.03578832, -93.92907973, -0.0006918, -113.11934351, -0.01034153, -11.31193435, -0.03578832, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 90.27254426, 0.0006918, 108.71575632, 0.01034153, 10.87157563, 0.03578832, -90.27254426, -0.0006918, -108.71575632, -0.01034153, -10.87157563, -0.03578832, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 104.81007078, 0.01383603, 104.81007078, 0.0415081, 73.36704955, -992.4888223, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 26.2025177, 6.707e-05, 78.60755309, 0.0002012, 262.02517696, 0.00067065, -26.2025177, -6.707e-05, -78.60755309, -0.0002012, -262.02517696, -0.00067065, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 104.81007078, 0.01383603, 104.81007078, 0.0415081, 73.36704955, -992.4888223, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 26.2025177, 6.707e-05, 78.60755309, 0.0002012, 262.02517696, 0.00067065, -26.2025177, -6.707e-05, -78.60755309, -0.0002012, -262.02517696, -0.00067065, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 24.9, 3.55, 6.15)
    ops.node(123011, 24.9, 3.55, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.16, 30165103.66561431, 12568793.19400596, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 134.39152023, 0.00059052, 161.4592033, 0.00953492, 16.14592033, 0.03322518, -134.39152023, -0.00059052, -161.4592033, -0.00953492, -16.14592033, -0.03322518, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 134.39152023, 0.00059052, 161.4592033, 0.00953492, 16.14592033, 0.03322518, -134.39152023, -0.00059052, -161.4592033, -0.00953492, -16.14592033, -0.03322518, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 137.90489967, 0.01181032, 137.90489967, 0.03543097, 96.53342977, -1105.07991157, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 34.47622492, 5.966e-05, 103.42867476, 0.00017898, 344.76224919, 0.0005966, -34.47622492, -5.966e-05, -103.42867476, -0.00017898, -344.76224919, -0.0005966, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 137.90489967, 0.01181032, 137.90489967, 0.03543097, 96.53342977, -1105.07991157, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 34.47622492, 5.966e-05, 103.42867476, 0.00017898, 344.76224919, 0.0005966, -34.47622492, -5.966e-05, -103.42867476, -0.00017898, -344.76224919, -0.0005966, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 32.15, 3.55, 6.15)
    ops.node(123012, 32.15, 3.55, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 26889488.3976437, 11203953.49901821, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 60.75310155, 0.00087617, 72.25989327, 0.01120476, 7.22598933, 0.03404852, -60.75310155, -0.00087617, -72.25989327, -0.01120476, -7.22598933, -0.03404852, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 55.67037621, 0.00087617, 66.21448684, 0.01120476, 6.62144868, 0.03404852, -55.67037621, -0.00087617, -66.21448684, -0.01120476, -6.62144868, -0.03404852, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 50.70988689, 0.01752336, 50.70988689, 0.05257009, 35.49692082, -842.09485974, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 12.67747172, 6.3e-05, 38.03241517, 0.00018901, 126.77471723, 0.00063003, -12.67747172, -6.3e-05, -38.03241517, -0.00018901, -126.77471723, -0.00063003, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 50.70988689, 0.01752336, 50.70988689, 0.05257009, 35.49692082, -842.09485974, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 12.67747172, 6.3e-05, 38.03241517, 0.00018901, 126.77471723, 0.00063003, -12.67747172, -6.3e-05, -38.03241517, -0.00018901, -126.77471723, -0.00063003, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 7.1, 6.15)
    ops.node(123013, 0.0, 7.1, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 23102799.87197462, 9626166.61332276, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 37.47549121, 0.00058294, 43.98502118, 0.01011835, 4.39850212, 0.02248027, -37.47549121, -0.00058294, -43.98502118, -0.01011835, -4.39850212, -0.02248027, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 35.25854837, 0.00058294, 41.38299318, 0.01011835, 4.13829932, 0.02248027, -35.25854837, -0.00058294, -41.38299318, -0.01011835, -4.13829932, -0.02248027, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 56.89514382, 0.01165872, 56.89514382, 0.03497615, 39.82660067, -862.21610556, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 14.22378595, 8.227e-05, 42.67135786, 0.00024682, 142.23785955, 0.00082274, -14.22378595, -8.227e-05, -42.67135786, -0.00024682, -142.23785955, -0.00082274, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 56.89514382, 0.01165872, 56.89514382, 0.03497615, 39.82660067, -862.21610556, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 14.22378595, 8.227e-05, 42.67135786, 0.00024682, 142.23785955, 0.00082274, -14.22378595, -8.227e-05, -42.67135786, -0.00024682, -142.23785955, -0.00082274, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 7.25, 7.1, 6.15)
    ops.node(123014, 7.25, 7.1, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.16, 25830910.97060874, 10762879.57108697, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 131.45214394, 0.00058036, 158.29872863, 0.01073896, 15.82987286, 0.02909499, -131.45214394, -0.00058036, -158.29872863, -0.01073896, -15.82987286, -0.02909499, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 131.45214394, 0.00058036, 158.29872863, 0.01073896, 15.82987286, 0.02909499, -131.45214394, -0.00058036, -158.29872863, -0.01073896, -15.82987286, -0.02909499, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 129.13179495, 0.01160712, 129.13179495, 0.03482135, 90.39225647, -1215.28346842, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 32.28294874, 6.524e-05, 96.84884621, 0.00019572, 322.82948738, 0.00065239, -32.28294874, -6.524e-05, -96.84884621, -0.00019572, -322.82948738, -0.00065239, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 129.13179495, 0.01160712, 129.13179495, 0.03482135, 90.39225647, -1215.28346842, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 32.28294874, 6.524e-05, 96.84884621, 0.00019572, 322.82948738, 0.00065239, -32.28294874, -6.524e-05, -96.84884621, -0.00019572, -322.82948738, -0.00065239, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 14.5, 7.1, 6.15)
    ops.node(123015, 14.5, 7.1, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 24006188.75395412, 10002578.64748088, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 92.4761964, 0.00065474, 111.28821094, 0.00980017, 11.12882109, 0.0311049, -92.4761964, -0.00065474, -111.28821094, -0.00980017, -11.12882109, -0.0311049, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 88.00349647, 0.00065474, 105.90564988, 0.00980017, 10.59056499, 0.0311049, -88.00349647, -0.00065474, -105.90564988, -0.00980017, -10.59056499, -0.0311049, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 94.7571697, 0.01309485, 94.7571697, 0.03928455, 66.33001879, -976.4255208, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 23.68929243, 6.728e-05, 71.06787728, 0.00020184, 236.89292426, 0.0006728, -23.68929243, -6.728e-05, -71.06787728, -0.00020184, -236.89292426, -0.0006728, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 94.7571697, 0.01309485, 94.7571697, 0.03928455, 66.33001879, -976.4255208, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 23.68929243, 6.728e-05, 71.06787728, 0.00020184, 236.89292426, 0.0006728, -23.68929243, -6.728e-05, -71.06787728, -0.00020184, -236.89292426, -0.0006728, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 17.65, 7.1, 6.15)
    ops.node(123016, 17.65, 7.1, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1225, 34411675.39313839, 14338198.08047433, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 90.13181533, 0.00062147, 107.22032986, 0.01331146, 10.72203299, 0.04944361, -90.13181533, -0.00062147, -107.22032986, -0.01331146, -10.72203299, -0.04944361, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 86.6047425, 0.00062147, 103.02454272, 0.01331146, 10.30245427, 0.04944361, -86.6047425, -0.00062147, -103.02454272, -0.01331146, -10.30245427, -0.04944361, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 140.96256116, 0.01242947, 140.96256116, 0.03728841, 98.67379281, -1121.85002947, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 35.24064029, 6.982e-05, 105.72192087, 0.00020947, 352.40640289, 0.00069822, -35.24064029, -6.982e-05, -105.72192087, -0.00020947, -352.40640289, -0.00069822, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 140.96256116, 0.01242947, 140.96256116, 0.03728841, 98.67379281, -1121.85002947, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 35.24064029, 6.982e-05, 105.72192087, 0.00020947, 352.40640289, 0.00069822, -35.24064029, -6.982e-05, -105.72192087, -0.00020947, -352.40640289, -0.00069822, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 24.9, 7.1, 6.15)
    ops.node(123017, 24.9, 7.1, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.16, 32561254.49185663, 13567189.37160693, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 136.57566614, 0.00056199, 163.26575336, 0.00886395, 16.32657534, 0.0346494, -136.57566614, -0.00056199, -163.26575336, -0.00886395, -16.32657534, -0.0346494, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 136.57566614, 0.00056199, 163.26575336, 0.00886395, 16.32657534, 0.0346494, -136.57566614, -0.00056199, -163.26575336, -0.00886395, -16.32657534, -0.0346494, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 144.48545447, 0.01123985, 144.48545447, 0.03371956, 101.13981813, -1066.68545645, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 36.12136362, 5.791e-05, 108.36409085, 0.00017372, 361.21363617, 0.00057907, -36.12136362, -5.791e-05, -108.36409085, -0.00017372, -361.21363617, -0.00057907, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 144.48545447, 0.01123985, 144.48545447, 0.03371956, 101.13981813, -1066.68545645, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 36.12136362, 5.791e-05, 108.36409085, 0.00017372, 361.21363617, 0.00057907, -36.12136362, -5.791e-05, -108.36409085, -0.00017372, -361.21363617, -0.00057907, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 32.15, 7.1, 6.15)
    ops.node(123018, 32.15, 7.1, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 29633539.74791497, 12347308.2282979, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 57.96861528, 0.00082258, 69.05925369, 0.01199357, 6.90592537, 0.04156088, -57.96861528, -0.00082258, -69.05925369, -0.01199357, -6.90592537, -0.04156088, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 53.48078703, 0.00082258, 63.71280772, 0.01199357, 6.37128077, 0.04156088, -53.48078703, -0.00082258, -63.71280772, -0.01199357, -6.37128077, -0.04156088, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 56.4022009, 0.01645151, 56.4022009, 0.04935452, 39.48154063, -740.07028383, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 14.10055022, 6.359e-05, 42.30165067, 0.00019076, 141.00550224, 0.00063586, -14.10055022, -6.359e-05, -42.30165067, -0.00019076, -141.00550224, -0.00063586, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 56.4022009, 0.01645151, 56.4022009, 0.04935452, 39.48154063, -740.07028383, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 14.10055022, 6.359e-05, 42.30165067, 0.00019076, 141.00550224, 0.00063586, -14.10055022, -6.359e-05, -42.30165067, -0.00019076, -141.00550224, -0.00063586, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 10.65, 6.125)
    ops.node(123019, 0.0, 10.65, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 28114982.58111627, 11714576.07546511, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 41.57487328, 0.00078422, 49.94771761, 0.01322587, 4.99477176, 0.0468605, -41.57487328, -0.00078422, -49.94771761, -0.01322587, -4.99477176, -0.0468605, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 41.57487328, 0.00078422, 49.94771761, 0.01322587, 4.99477176, 0.0468605, -41.57487328, -0.00078422, -49.94771761, -0.01322587, -4.99477176, -0.0468605, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 51.32315121, 0.01568436, 51.32315121, 0.04705307, 35.92620584, -692.76759743, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 12.8307878, 6.099e-05, 38.4923634, 0.00018296, 128.30787801, 0.00060985, -12.8307878, -6.099e-05, -38.4923634, -0.00018296, -128.30787801, -0.00060985, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 51.32315121, 0.01568436, 51.32315121, 0.04705307, 35.92620584, -692.76759743, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 12.8307878, 6.099e-05, 38.4923634, 0.00018296, 128.30787801, 0.00060985, -12.8307878, -6.099e-05, -38.4923634, -0.00018296, -128.30787801, -0.00060985, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 7.25, 10.65, 6.125)
    ops.node(123020, 7.25, 10.65, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1225, 29314702.52674033, 12214459.38614181, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 92.9886632, 0.00064874, 111.77363188, 0.01054449, 11.17736319, 0.04400555, -92.9886632, -0.00064874, -111.77363188, -0.01054449, -11.17736319, -0.04400555, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 84.70018642, 0.00064874, 101.81077059, 0.01054449, 10.18107706, 0.04400555, -84.70018642, -0.00064874, -101.81077059, -0.01054449, -10.18107706, -0.04400555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 119.5183664, 0.01297477, 119.5183664, 0.0389243, 83.66285648, -1090.14713369, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 29.8795916, 6.949e-05, 89.6387748, 0.00020848, 298.79591599, 0.00069493, -29.8795916, -6.949e-05, -89.6387748, -0.00020848, -298.79591599, -0.00069493, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 119.5183664, 0.01297477, 119.5183664, 0.0389243, 83.66285648, -1090.14713369, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 29.8795916, 6.949e-05, 89.6387748, 0.00020848, 298.79591599, 0.00069493, -29.8795916, -6.949e-05, -89.6387748, -0.00020848, -298.79591599, -0.00069493, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 14.5, 10.65, 6.125)
    ops.node(123021, 14.5, 10.65, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 25202093.65485706, 10500872.35619044, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 38.16744109, 0.00085231, 45.45968094, 0.01122311, 4.54596809, 0.03590993, -38.16744109, -0.00085231, -45.45968094, -0.01122311, -4.54596809, -0.03590993, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 38.16744109, 0.00085231, 45.45968094, 0.01122311, 4.54596809, 0.03590993, -38.16744109, -0.00085231, -45.45968094, -0.01122311, -4.54596809, -0.03590993, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 66.43709243, 0.01704624, 66.43709243, 0.05113872, 46.5059647, -852.74239937, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 16.60927311, 8.807e-05, 49.82781932, 0.00026421, 166.09273108, 0.00088069, -16.60927311, -8.807e-05, -49.82781932, -0.00026421, -166.09273108, -0.00088069, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 66.43709243, 0.01704624, 66.43709243, 0.05113872, 46.5059647, -852.74239937, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 16.60927311, 8.807e-05, 49.82781932, 0.00026421, 166.09273108, 0.00088069, -16.60927311, -8.807e-05, -49.82781932, -0.00026421, -166.09273108, -0.00088069, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 17.65, 10.65, 6.125)
    ops.node(123022, 17.65, 10.65, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0625, 26155674.19322466, 10898197.58051028, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 37.67574181, 0.00085201, 44.96126025, 0.01071069, 4.49612602, 0.03843833, -37.67574181, -0.00085201, -44.96126025, -0.01071069, -4.49612602, -0.03843833, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 37.67574181, 0.00085201, 44.96126025, 0.01071069, 4.49612602, 0.03843833, -37.67574181, -0.00085201, -44.96126025, -0.01071069, -4.49612602, -0.03843833, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 62.34724813, 0.01704024, 62.34724813, 0.05112072, 43.64307369, -866.53017951, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 15.58681203, 7.963e-05, 46.76043609, 0.0002389, 155.86812032, 0.00079635, -15.58681203, -7.963e-05, -46.76043609, -0.0002389, -155.86812032, -0.00079635, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 62.34724813, 0.01704024, 62.34724813, 0.05112072, 43.64307369, -866.53017951, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 15.58681203, 7.963e-05, 46.76043609, 0.0002389, 155.86812032, 0.00079635, -15.58681203, -7.963e-05, -46.76043609, -0.0002389, -155.86812032, -0.00079635, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 24.9, 10.65, 6.125)
    ops.node(123023, 24.9, 10.65, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 27619181.81829989, 11507992.42429162, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 87.07518072, 0.0005592, 104.792963, 0.01405175, 10.4792963, 0.04446323, -87.07518072, -0.0005592, -104.792963, -0.01405175, -10.4792963, -0.04446323, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 78.65064521, 0.0005592, 94.65422967, 0.01405175, 9.46542297, 0.04446323, -78.65064521, -0.0005592, -94.65422967, -0.01405175, -9.46542297, -0.04446323, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 127.35816841, 0.01118404, 127.35816841, 0.03355211, 89.15071788, -1415.82785188, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 31.8395421, 7.86e-05, 95.5186263, 0.00023579, 318.39542102, 0.00078598, -31.8395421, -7.86e-05, -95.5186263, -0.00023579, -318.39542102, -0.00078598, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 127.35816841, 0.01118404, 127.35816841, 0.03355211, 89.15071788, -1415.82785188, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 31.8395421, 7.86e-05, 95.5186263, 0.00023579, 318.39542102, 0.00078598, -31.8395421, -7.86e-05, -95.5186263, -0.00023579, -318.39542102, -0.00078598, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 32.15, 10.65, 6.125)
    ops.node(123024, 32.15, 10.65, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 26575855.65737681, 11073273.19057367, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 40.82890537, 0.00081168, 49.04547647, 0.01398334, 4.90454765, 0.04403548, -40.82890537, -0.00081168, -49.04547647, -0.01398334, -4.90454765, -0.04403548, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 40.82890537, 0.00081168, 49.04547647, 0.01398334, 4.90454765, 0.04403548, -40.82890537, -0.00081168, -49.04547647, -0.01398334, -4.90454765, -0.04403548, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 58.11107088, 0.01623358, 58.11107088, 0.04870074, 40.67774961, -764.74722605, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 14.52776772, 7.305e-05, 43.58330316, 0.00021915, 145.27767719, 0.0007305, -14.52776772, -7.305e-05, -43.58330316, -0.00021915, -145.27767719, -0.0007305, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 58.11107088, 0.01623358, 58.11107088, 0.04870074, 40.67774961, -764.74722605, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 14.52776772, 7.305e-05, 43.58330316, 0.00021915, 145.27767719, 0.0007305, -14.52776772, -7.305e-05, -43.58330316, -0.00021915, -145.27767719, -0.0007305, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.025)
    ops.node(124001, 0.0, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 23597312.5093995, 9832213.54558312, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 29.00823481, 0.00070654, 35.43714311, 0.01578282, 3.54371431, 0.05753492, -29.00823481, -0.00070654, -35.43714311, -0.01578282, -3.54371431, -0.05753492, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 29.00823481, 0.00070654, 35.43714311, 0.01578282, 3.54371431, 0.05753492, -29.00823481, -0.00070654, -35.43714311, -0.01578282, -3.54371431, -0.05753492, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 34.45388095, 0.01413076, 34.45388095, 0.04239228, 24.11771667, -581.02499543, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 8.61347024, 4.878e-05, 25.84041072, 0.00014633, 86.13470238, 0.00048778, -8.61347024, -4.878e-05, -25.84041072, -0.00014633, -86.13470238, -0.00048778, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 34.45388095, 0.01413076, 34.45388095, 0.04239228, 24.11771667, -581.02499543, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 8.61347024, 4.878e-05, 25.84041072, 0.00014633, 86.13470238, 0.00048778, -8.61347024, -4.878e-05, -25.84041072, -0.00014633, -86.13470238, -0.00048778, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 7.25, 0.0, 9.025)
    ops.node(124002, 7.25, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1225, 33255265.40187414, 13856360.58411422, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 60.90605353, 0.00054341, 73.08295701, 0.01324442, 7.3082957, 0.05412021, -60.90605353, -0.00054341, -73.08295701, -0.01324442, -7.3082957, -0.05412021, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 57.5381792, 0.00054341, 69.04174599, 0.01324442, 6.9041746, 0.05412021, -57.5381792, -0.00054341, -69.04174599, -0.01324442, -6.9041746, -0.05412021, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 114.81365929, 0.01086815, 114.81365929, 0.03260445, 80.3695615, -784.24003417, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 28.70341482, 5.885e-05, 86.11024447, 0.00017654, 287.03414823, 0.00058847, -28.70341482, -5.885e-05, -86.11024447, -0.00017654, -287.03414823, -0.00058847, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 114.81365929, 0.01086815, 114.81365929, 0.03260445, 80.3695615, -784.24003417, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 28.70341482, 5.885e-05, 86.11024447, 0.00017654, 287.03414823, 0.00058847, -28.70341482, -5.885e-05, -86.11024447, -0.00017654, -287.03414823, -0.00058847, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 24.9, 0.0, 9.025)
    ops.node(124005, 24.9, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 27107208.33806206, 11294670.14085919, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 62.41531222, 0.00055481, 76.03007472, 0.01197424, 7.60300747, 0.04889371, -62.41531222, -0.00055481, -76.03007472, -0.01197424, -7.60300747, -0.04889371, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 58.6329127, 0.00055481, 71.42261371, 0.01197424, 7.14226137, 0.04889371, -58.6329127, -0.00055481, -71.42261371, -0.01197424, -7.14226137, -0.04889371, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 84.11725297, 0.01109624, 84.11725297, 0.03328872, 58.88207708, -668.76502991, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 21.02931324, 5.289e-05, 63.08793973, 0.00015868, 210.29313242, 0.00052893, -21.02931324, -5.289e-05, -63.08793973, -0.00015868, -210.29313242, -0.00052893, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 84.11725297, 0.01109624, 84.11725297, 0.03328872, 58.88207708, -668.76502991, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 21.02931324, 5.289e-05, 63.08793973, 0.00015868, 210.29313242, 0.00052893, -21.02931324, -5.289e-05, -63.08793973, -0.00015868, -210.29313242, -0.00052893, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 32.15, 0.0, 9.025)
    ops.node(124006, 32.15, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 27494344.3588389, 11455976.81618288, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 27.41604042, 0.00073594, 33.37490871, 0.01364173, 3.33749087, 0.06126101, -27.41604042, -0.00073594, -33.37490871, -0.01364173, -3.33749087, -0.06126101, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 27.41604042, 0.00073594, 33.37490871, 0.01364173, 3.33749087, 0.06126101, -27.41604042, -0.00073594, -33.37490871, -0.01364173, -3.33749087, -0.06126101, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 35.36028795, 0.01471887, 35.36028795, 0.04415662, 24.75220156, -455.69650504, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 8.84007199, 4.297e-05, 26.52021596, 0.0001289, 88.40071986, 0.00042966, -8.84007199, -4.297e-05, -26.52021596, -0.0001289, -88.40071986, -0.00042966, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 35.36028795, 0.01471887, 35.36028795, 0.04415662, 24.75220156, -455.69650504, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 8.84007199, 4.297e-05, 26.52021596, 0.0001289, 88.40071986, 0.00042966, -8.84007199, -4.297e-05, -26.52021596, -0.0001289, -88.40071986, -0.00042966, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 3.55, 9.05)
    ops.node(124007, 0.0, 3.55, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 26360696.51085193, 10983623.5461883, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 30.63827724, 0.00082303, 37.12508635, 0.01730927, 3.71250863, 0.05569636, -30.63827724, -0.00082303, -37.12508635, -0.01730927, -3.71250863, -0.05569636, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 30.63827724, 0.00082303, 37.12508635, 0.01730927, 3.71250863, 0.05569636, -30.63827724, -0.00082303, -37.12508635, -0.01730927, -3.71250863, -0.05569636, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 56.23498418, 0.01646067, 56.23498418, 0.049382, 39.36448892, -724.97245432, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 14.05874604, 7.127e-05, 42.17623813, 0.00021381, 140.58746044, 0.00071269, -14.05874604, -7.127e-05, -42.17623813, -0.00021381, -140.58746044, -0.00071269, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 56.23498418, 0.01646067, 56.23498418, 0.049382, 39.36448892, -724.97245432, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 14.05874604, 7.127e-05, 42.17623813, 0.00021381, 140.58746044, 0.00071269, -14.05874604, -7.127e-05, -42.17623813, -0.00021381, -140.58746044, -0.00071269, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 7.25, 3.55, 9.05)
    ops.node(124008, 7.25, 3.55, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.16, 25922359.48376984, 10800983.11823743, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 89.12210242, 0.00054076, 108.53297605, 0.01257602, 10.8532976, 0.038358, -89.12210242, -0.00054076, -108.53297605, -0.01257602, -10.8532976, -0.038358, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 89.12210242, 0.00054076, 108.53297605, 0.01257602, 10.8532976, 0.038358, -89.12210242, -0.00054076, -108.53297605, -0.01257602, -10.8532976, -0.038358, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 110.6461808, 0.01081511, 110.6461808, 0.03244532, 77.45232656, -847.97305187, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 27.6615452, 5.57e-05, 82.9846356, 0.00016711, 276.615452, 0.00055702, -27.6615452, -5.57e-05, -82.9846356, -0.00016711, -276.615452, -0.00055702, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 110.6461808, 0.01081511, 110.6461808, 0.03244532, 77.45232656, -847.97305187, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 27.6615452, 5.57e-05, 82.9846356, 0.00016711, 276.615452, 0.00055702, -27.6615452, -5.57e-05, -82.9846356, -0.00016711, -276.615452, -0.00055702, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 14.5, 3.55, 9.05)
    ops.node(124009, 14.5, 3.55, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 26768042.52338123, 11153351.05140885, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 65.15844287, 0.00058396, 79.30131632, 0.01551018, 7.93013163, 0.05064422, -65.15844287, -0.00058396, -79.30131632, -0.01551018, -7.93013163, -0.05064422, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 61.62531267, 0.00058396, 75.00130755, 0.01551018, 7.50013076, 0.05064422, -61.62531267, -0.00058396, -75.00130755, -0.01551018, -7.50013076, -0.05064422, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 101.83187832, 0.01167928, 101.83187832, 0.03503785, 71.28231483, -1057.69522942, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 25.45796958, 6.484e-05, 76.37390874, 0.00019453, 254.5796958, 0.00064843, -25.45796958, -6.484e-05, -76.37390874, -0.00019453, -254.5796958, -0.00064843, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 101.83187832, 0.01167928, 101.83187832, 0.03503785, 71.28231483, -1057.69522942, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 25.45796958, 6.484e-05, 76.37390874, 0.00019453, 254.5796958, 0.00064843, -25.45796958, -6.484e-05, -76.37390874, -0.00019453, -254.5796958, -0.00064843, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 17.65, 3.55, 9.05)
    ops.node(124010, 17.65, 3.55, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 29954296.43260404, 12480956.84691835, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 63.03666032, 0.00054731, 76.29302143, 0.01447346, 7.62930214, 0.05253027, -63.03666032, -0.00054731, -76.29302143, -0.01447346, -7.62930214, -0.05253027, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 59.67443373, 0.00054731, 72.22373185, 0.01447346, 7.22237319, 0.05253027, -59.67443373, -0.00054731, -72.22373185, -0.01447346, -7.22237319, -0.05253027, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 105.5755964, 0.01094617, 105.5755964, 0.0328385, 73.90291748, -828.72014375, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 26.3938991, 6.008e-05, 79.1816973, 0.00018023, 263.938991, 0.00060076, -26.3938991, -6.008e-05, -79.1816973, -0.00018023, -263.938991, -0.00060076, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 105.5755964, 0.01094617, 105.5755964, 0.0328385, 73.90291748, -828.72014375, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 26.3938991, 6.008e-05, 79.1816973, 0.00018023, 263.938991, 0.00060076, -26.3938991, -6.008e-05, -79.1816973, -0.00018023, -263.938991, -0.00060076, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 24.9, 3.55, 9.05)
    ops.node(124011, 24.9, 3.55, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.16, 29080830.63540678, 12117012.76475282, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 104.37427909, 0.00054264, 126.53762432, 0.00942716, 12.65376243, 0.03772227, -104.37427909, -0.00054264, -126.53762432, -0.00942716, -12.65376243, -0.03772227, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 104.37427909, 0.00054264, 126.53762432, 0.00942716, 12.65376243, 0.03772227, -104.37427909, -0.00054264, -126.53762432, -0.00942716, -12.65376243, -0.03772227, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 106.77238972, 0.01085271, 106.77238972, 0.03255814, 74.7406728, -704.46615582, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 26.69309743, 4.791e-05, 80.07929229, 0.00014374, 266.9309743, 0.00047914, -26.69309743, -4.791e-05, -80.07929229, -0.00014374, -266.9309743, -0.00047914, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 106.77238972, 0.01085271, 106.77238972, 0.03255814, 74.7406728, -704.46615582, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 26.69309743, 4.791e-05, 80.07929229, 0.00014374, 266.9309743, 0.00047914, -26.69309743, -4.791e-05, -80.07929229, -0.00014374, -266.9309743, -0.00047914, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 32.15, 3.55, 9.05)
    ops.node(124012, 32.15, 3.55, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 26719613.75397731, 11133172.39749055, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 32.55031882, 0.00078459, 39.43472123, 0.01494127, 3.94347212, 0.05403427, -32.55031882, -0.00078459, -39.43472123, -0.01494127, -3.94347212, -0.05403427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 32.55031882, 0.00078459, 39.43472123, 0.01494127, 3.94347212, 0.05403427, -32.55031882, -0.00078459, -39.43472123, -0.01494127, -3.94347212, -0.05403427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 41.10729707, 0.01569186, 41.10729707, 0.04707559, 28.77510795, -580.37718696, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 10.27682427, 5.14e-05, 30.8304728, 0.00015419, 102.76824267, 0.00051397, -10.27682427, -5.14e-05, -30.8304728, -0.00015419, -102.76824267, -0.00051397, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 41.10729707, 0.01569186, 41.10729707, 0.04707559, 28.77510795, -580.37718696, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 10.27682427, 5.14e-05, 30.8304728, 0.00015419, 102.76824267, 0.00051397, -10.27682427, -5.14e-05, -30.8304728, -0.00015419, -102.76824267, -0.00051397, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 7.1, 9.05)
    ops.node(124013, 0.0, 7.1, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 22483132.19678178, 9367971.74865908, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 33.82016139, 0.00079465, 40.87387702, 0.01565871, 4.0873877, 0.04440539, -33.82016139, -0.00079465, -40.87387702, -0.01565871, -4.0873877, -0.04440539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 33.82016139, 0.00079465, 40.87387702, 0.01565871, 4.0873877, 0.04440539, -33.82016139, -0.00079465, -40.87387702, -0.01565871, -4.0873877, -0.04440539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 50.97622945, 0.01589296, 50.97622945, 0.04767888, 35.68336062, -682.32686481, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 12.74405736, 7.575e-05, 38.23217209, 0.00022724, 127.44057363, 0.00075746, -12.74405736, -7.575e-05, -38.23217209, -0.00022724, -127.44057363, -0.00075746, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 50.97622945, 0.01589296, 50.97622945, 0.04767888, 35.68336062, -682.32686481, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 12.74405736, 7.575e-05, 38.23217209, 0.00022724, 127.44057363, 0.00075746, -12.74405736, -7.575e-05, -38.23217209, -0.00022724, -127.44057363, -0.00075746, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 7.25, 7.1, 9.05)
    ops.node(124014, 7.25, 7.1, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.16, 29606464.11343613, 12336026.71393172, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 95.55281608, 0.00053272, 115.71749895, 0.01130218, 11.57174989, 0.03992582, -95.55281608, -0.00053272, -115.71749895, -0.01130218, -11.57174989, -0.03992582, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 95.55281608, 0.00053272, 115.71749895, 0.01130218, 11.57174989, 0.03992582, -95.55281608, -0.00053272, -115.71749895, -0.01130218, -11.57174989, -0.03992582, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 121.41852271, 0.01065449, 121.41852271, 0.03196347, 84.9929659, -774.45192886, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 30.35463068, 5.352e-05, 91.06389204, 0.00016056, 303.54630679, 0.00053519, -30.35463068, -5.352e-05, -91.06389204, -0.00016056, -303.54630679, -0.00053519, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 121.41852271, 0.01065449, 121.41852271, 0.03196347, 84.9929659, -774.45192886, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 30.35463068, 5.352e-05, 91.06389204, 0.00016056, 303.54630679, 0.00053519, -30.35463068, -5.352e-05, -91.06389204, -0.00016056, -303.54630679, -0.00053519, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 14.5, 7.1, 9.05)
    ops.node(124015, 14.5, 7.1, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 25991204.53560818, 10829668.55650341, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 62.41698469, 0.00057984, 76.05814213, 0.01203909, 7.60581421, 0.04668641, -62.41698469, -0.00057984, -76.05814213, -0.01203909, -7.60581421, -0.04668641, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 59.08586318, 0.00057984, 71.99900799, 0.01203909, 7.1999008, 0.04668641, -59.08586318, -0.00057984, -71.99900799, -0.01203909, -7.1999008, -0.04668641, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 82.68743146, 0.0115968, 82.68743146, 0.03479041, 57.88120202, -675.06853572, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 20.67185786, 5.423e-05, 62.01557359, 0.00016268, 206.71857864, 0.00054226, -20.67185786, -5.423e-05, -62.01557359, -0.00016268, -206.71857864, -0.00054226, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 82.68743146, 0.0115968, 82.68743146, 0.03479041, 57.88120202, -675.06853572, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 20.67185786, 5.423e-05, 62.01557359, 0.00016268, 206.71857864, 0.00054226, -20.67185786, -5.423e-05, -62.01557359, -0.00016268, -206.71857864, -0.00054226, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 17.65, 7.1, 9.05)
    ops.node(124016, 17.65, 7.1, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1225, 27990546.91930006, 11662727.88304169, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 64.51781756, 0.00056081, 78.4118104, 0.01185918, 7.84118104, 0.04861223, -64.51781756, -0.00056081, -78.4118104, -0.01185918, -7.84118104, -0.04861223, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 60.83428181, 0.00056081, 73.93502061, 0.01185918, 7.39350206, 0.04861223, -60.83428181, -0.00056081, -73.93502061, -0.01185918, -7.39350206, -0.04861223, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 88.83897046, 0.01121615, 88.83897046, 0.03364844, 62.18727932, -677.67096974, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 22.20974261, 5.41e-05, 66.62922784, 0.0001623, 222.09742614, 0.00054099, -22.20974261, -5.41e-05, -66.62922784, -0.0001623, -222.09742614, -0.00054099, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 88.83897046, 0.01121615, 88.83897046, 0.03364844, 62.18727932, -677.67096974, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 22.20974261, 5.41e-05, 66.62922784, 0.0001623, 222.09742614, 0.00054099, -22.20974261, -5.41e-05, -66.62922784, -0.0001623, -222.09742614, -0.00054099, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 24.9, 7.1, 9.05)
    ops.node(124017, 24.9, 7.1, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.16, 23046680.22652193, 9602783.42771747, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 91.74593286, 0.0005426, 111.79317675, 0.00974153, 11.17931768, 0.0321508, -91.74593286, -0.0005426, -111.79317675, -0.00974153, -11.17931768, -0.0321508, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 91.74593286, 0.0005426, 111.79317675, 0.00974153, 11.17931768, 0.0321508, -91.74593286, -0.0005426, -111.79317675, -0.00974153, -11.17931768, -0.0321508, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 80.47410939, 0.010852, 80.47410939, 0.032556, 56.33187658, -684.09027209, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 20.11852735, 4.557e-05, 60.35558205, 0.0001367, 201.18527349, 0.00045568, -20.11852735, -4.557e-05, -60.35558205, -0.0001367, -201.18527349, -0.00045568, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 80.47410939, 0.010852, 80.47410939, 0.032556, 56.33187658, -684.09027209, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 20.11852735, 4.557e-05, 60.35558205, 0.0001367, 201.18527349, 0.00045568, -20.11852735, -4.557e-05, -60.35558205, -0.0001367, -201.18527349, -0.00045568, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 32.15, 7.1, 9.05)
    ops.node(124018, 32.15, 7.1, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 28523863.52428275, 11884943.13511781, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 33.49215632, 0.00076397, 40.50310603, 0.01416909, 4.0503106, 0.05640581, -33.49215632, -0.00076397, -40.50310603, -0.01416909, -4.0503106, -0.05640581, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 33.49215632, 0.00076397, 40.50310603, 0.01416909, 4.0503106, 0.05640581, -33.49215632, -0.00076397, -40.50310603, -0.01416909, -4.0503106, -0.05640581, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 41.91099088, 0.01527941, 41.91099088, 0.04583824, 29.33769362, -546.90943743, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 10.47774772, 4.909e-05, 31.43324316, 0.00014726, 104.7774772, 0.00049087, -10.47774772, -4.909e-05, -31.43324316, -0.00014726, -104.7774772, -0.00049087, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 41.91099088, 0.01527941, 41.91099088, 0.04583824, 29.33769362, -546.90943743, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 10.47774772, 4.909e-05, 31.43324316, 0.00014726, 104.7774772, 0.00049087, -10.47774772, -4.909e-05, -31.43324316, -0.00014726, -104.7774772, -0.00049087, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 10.65, 9.025)
    ops.node(124019, 0.0, 10.65, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 26772029.03571403, 11155012.09821418, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 27.4226476, 0.00071563, 33.41861654, 0.01728263, 3.34186165, 0.06403539, -27.4226476, -0.00071563, -33.41861654, -0.01728263, -3.34186165, -0.06403539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 27.4226476, 0.00071563, 33.41861654, 0.01728263, 3.34186165, 0.06403539, -27.4226476, -0.00071563, -33.41861654, -0.01728263, -3.34186165, -0.06403539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 45.84341597, 0.01431267, 45.84341597, 0.04293802, 32.09039118, -617.24514896, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 11.46085399, 5.721e-05, 34.38256198, 0.00017162, 114.60853993, 0.00057207, -11.46085399, -5.721e-05, -34.38256198, -0.00017162, -114.60853993, -0.00057207, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 45.84341597, 0.01431267, 45.84341597, 0.04293802, 32.09039118, -617.24514896, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 11.46085399, 5.721e-05, 34.38256198, 0.00017162, 114.60853993, 0.00057207, -11.46085399, -5.721e-05, -34.38256198, -0.00017162, -114.60853993, -0.00057207, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 7.25, 10.65, 9.025)
    ops.node(124020, 7.25, 10.65, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1225, 27451413.94877585, 11438089.14532327, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 56.60865262, 0.00059613, 68.92041405, 0.01165551, 6.89204141, 0.05408406, -56.60865262, -0.00059613, -68.92041405, -0.01165551, -6.89204141, -0.05408406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 50.23871744, 0.00059613, 61.1650878, 0.01165551, 6.11650878, 0.05408406, -50.23871744, -0.00059613, -61.1650878, -0.01165551, -6.11650878, -0.05408406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 93.99166658, 0.01192258, 93.99166658, 0.03576775, 65.79416661, -803.34432142, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 23.49791664, 5.836e-05, 70.49374993, 0.00017508, 234.97916645, 0.00058361, -23.49791664, -5.836e-05, -70.49374993, -0.00017508, -234.97916645, -0.00058361, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 93.99166658, 0.01192258, 93.99166658, 0.03576775, 65.79416661, -803.34432142, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 23.49791664, 5.836e-05, 70.49374993, 0.00017508, 234.97916645, 0.00058361, -23.49791664, -5.836e-05, -70.49374993, -0.00017508, -234.97916645, -0.00058361, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 14.5, 10.65, 9.025)
    ops.node(124021, 14.5, 10.65, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 26943253.81275643, 11226355.75531518, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 22.18673641, 0.00077147, 26.96241696, 0.01562321, 2.6962417, 0.06581838, -22.18673641, -0.00077147, -26.96241696, -0.01562321, -2.6962417, -0.06581838, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 22.18673641, 0.00077147, 26.96241696, 0.01562321, 2.6962417, 0.06581838, -22.18673641, -0.00077147, -26.96241696, -0.01562321, -2.6962417, -0.06581838, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 58.83952299, 0.01542949, 58.83952299, 0.04628848, 41.1876661, -720.63037461, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 14.70988075, 7.296e-05, 44.12964225, 0.00021887, 147.09880748, 0.00072957, -14.70988075, -7.296e-05, -44.12964225, -0.00021887, -147.09880748, -0.00072957, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 58.83952299, 0.01542949, 58.83952299, 0.04628848, 41.1876661, -720.63037461, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 14.70988075, 7.296e-05, 44.12964225, 0.00021887, 147.09880748, 0.00072957, -14.70988075, -7.296e-05, -44.12964225, -0.00021887, -147.09880748, -0.00072957, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 17.65, 10.65, 9.025)
    ops.node(124022, 17.65, 10.65, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0625, 26538877.70942988, 11057865.71226245, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 22.47860492, 0.00070293, 27.32835966, 0.01293172, 2.73283597, 0.06238519, -22.47860492, -0.00070293, -27.32835966, -0.01293172, -2.73283597, -0.06238519, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 22.47860492, 0.00070293, 27.32835966, 0.01293172, 2.73283597, 0.06238519, -22.47860492, -0.00070293, -27.32835966, -0.01293172, -2.73283597, -0.06238519, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 42.50905801, 0.01405863, 42.50905801, 0.0421759, 29.75634061, -540.09799933, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 10.6272645, 5.351e-05, 31.88179351, 0.00016054, 106.27264502, 0.00053512, -10.6272645, -5.351e-05, -31.88179351, -0.00016054, -106.27264502, -0.00053512, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 42.50905801, 0.01405863, 42.50905801, 0.0421759, 29.75634061, -540.09799933, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 10.6272645, 5.351e-05, 31.88179351, 0.00016054, 106.27264502, 0.00053512, -10.6272645, -5.351e-05, -31.88179351, -0.00016054, -106.27264502, -0.00053512, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 24.9, 10.65, 9.025)
    ops.node(124023, 24.9, 10.65, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 27788151.92654342, 11578396.63605976, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 57.31206022, 0.00061679, 69.73814259, 0.01562318, 6.97381426, 0.05838685, -57.31206022, -0.00061679, -69.73814259, -0.01562318, -6.97381426, -0.05838685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 51.11772696, 0.00061679, 62.20078841, 0.01562318, 6.22007884, 0.05838685, -51.11772696, -0.00061679, -62.20078841, -0.01562318, -6.22007884, -0.05838685, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 108.31130991, 0.01233581, 108.31130991, 0.03700743, 75.81791694, -1250.55083723, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 27.07782748, 6.644e-05, 81.23348244, 0.00019931, 270.77827478, 0.00066437, -27.07782748, -6.644e-05, -81.23348244, -0.00019931, -270.77827478, -0.00066437, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 108.31130991, 0.01233581, 108.31130991, 0.03700743, 75.81791694, -1250.55083723, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 27.07782748, 6.644e-05, 81.23348244, 0.00019931, 270.77827478, 0.00066437, -27.07782748, -6.644e-05, -81.23348244, -0.00019931, -270.77827478, -0.00066437, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 32.15, 10.65, 9.025)
    ops.node(124024, 32.15, 10.65, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 32666965.51696637, 13611235.63206932, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 30.56810066, 0.00067295, 36.75002012, 0.01709667, 3.67500201, 0.06901809, -30.56810066, -0.00067295, -36.75002012, -0.01709667, -3.67500201, -0.06901809, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 30.56810066, 0.00067295, 36.75002012, 0.01709667, 3.67500201, 0.06901809, -30.56810066, -0.00067295, -36.75002012, -0.01709667, -3.67500201, -0.06901809, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 64.99075319, 0.0134591, 64.99075319, 0.04037729, 45.49352724, -728.80014285, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 16.2476883, 6.647e-05, 48.74306489, 0.0001994, 162.47688298, 0.00066465, -16.2476883, -6.647e-05, -48.74306489, -0.0001994, -162.47688298, -0.00066465, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 64.99075319, 0.0134591, 64.99075319, 0.04037729, 45.49352724, -728.80014285, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 16.2476883, 6.647e-05, 48.74306489, 0.0001994, 162.47688298, 0.00066465, -16.2476883, -6.647e-05, -48.74306489, -0.0001994, -162.47688298, -0.00066465, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 14.5, 0.0, 0.0)
    ops.node(124025, 14.5, 0.0, 1.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.1225, 24631035.14650325, 10262931.31104302, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 140.5760438, 0.00053115, 165.70033549, 0.00739697, 16.57003355, 0.02092715, -140.5760438, -0.00053115, -165.70033549, -0.00739697, -16.57003355, -0.02092715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 135.57817209, 0.00053115, 159.80922491, 0.00739697, 15.98092249, 0.02092715, -135.57817209, -0.00053115, -159.80922491, -0.00739697, -15.98092249, -0.02092715, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 168.94571075, 0.01062299, 168.94571075, 0.03186897, 118.26199753, -3033.05616132, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 42.23642769, 5.846e-05, 126.70928306, 0.00017537, 422.36427688, 0.00058456, -42.23642769, -5.846e-05, -126.70928306, -0.00017537, -422.36427688, -0.00058456, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 168.94571075, 0.01062299, 168.94571075, 0.03186897, 118.26199753, -3033.05616132, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 42.23642769, 5.846e-05, 126.70928306, 0.00017537, 422.36427688, 0.00058456, -42.23642769, -5.846e-05, -126.70928306, -0.00017537, -422.36427688, -0.00058456, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 14.5, 0.0, 1.65)
    ops.node(121003, 14.5, 0.0, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.1225, 26292419.84018135, 10955174.9334089, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 137.83851272, 0.00051551, 163.70504666, 0.01071991, 16.37050467, 0.02943992, -137.83851272, -0.00051551, -163.70504666, -0.01071991, -16.37050467, -0.02943992, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 118.17238146, 0.00051551, 140.34840364, 0.01071991, 14.03484036, 0.02943992, -118.17238146, -0.00051551, -140.34840364, -0.01071991, -14.03484036, -0.02943992, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 187.35881259, 0.01031012, 187.35881259, 0.03093035, 131.15116882, -3373.86700806, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 46.83970315, 6.073e-05, 140.51910945, 0.00018219, 468.39703148, 0.00060731, -46.83970315, -6.073e-05, -140.51910945, -0.00018219, -468.39703148, -0.00060731, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 187.35881259, 0.01031012, 187.35881259, 0.03093035, 131.15116882, -3373.86700806, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 46.83970315, 6.073e-05, 140.51910945, 0.00018219, 468.39703148, 0.00060731, -46.83970315, -6.073e-05, -140.51910945, -0.00018219, -468.39703148, -0.00060731, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 17.65, 0.0, 0.0)
    ops.node(124026, 17.65, 0.0, 1.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.1225, 23508457.79235074, 9795190.74681281, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 137.15396693, 0.00052951, 160.76612704, 0.00771152, 16.0766127, 0.01851014, -137.15396693, -0.00052951, -160.76612704, -0.00771152, -16.0766127, -0.01851014, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 132.34032168, 0.00052951, 155.12377399, 0.00771152, 15.5123774, 0.01851014, -132.34032168, -0.00052951, -155.12377399, -0.00771152, -15.5123774, -0.01851014, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 167.31986701, 0.01059014, 167.31986701, 0.03177041, 117.12390691, -3233.68984537, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 41.82996675, 6.066e-05, 125.48990026, 0.00018197, 418.29966753, 0.00060658, -41.82996675, -6.066e-05, -125.48990026, -0.00018197, -418.29966753, -0.00060658, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 167.31986701, 0.01059014, 167.31986701, 0.03177041, 117.12390691, -3233.68984537, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 41.82996675, 6.066e-05, 125.48990026, 0.00018197, 418.29966753, 0.00060658, -41.82996675, -6.066e-05, -125.48990026, -0.00018197, -418.29966753, -0.00060658, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 17.65, 0.0, 1.65)
    ops.node(121004, 17.65, 0.0, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.1225, 29094105.69573174, 12122544.03988823, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 143.37026811, 0.00052448, 170.76988935, 0.01063414, 17.07698893, 0.0356766, -143.37026811, -0.00052448, -170.76988935, -0.01063414, -17.07698893, -0.0356766, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 123.15086271, 0.00052448, 146.68633515, 0.01063414, 14.66863351, 0.0356766, -123.15086271, -0.00052448, -146.68633515, -0.01063414, -14.66863351, -0.0356766, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 203.04819782, 0.01048968, 203.04819782, 0.03146905, 142.13373847, -3298.90103179, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 50.76204945, 5.948e-05, 152.28614836, 0.00017843, 507.62049454, 0.00059478, -50.76204945, -5.948e-05, -152.28614836, -0.00017843, -507.62049454, -0.00059478, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 203.04819782, 0.01048968, 203.04819782, 0.03146905, 142.13373847, -3298.90103179, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 50.76204945, 5.948e-05, 152.28614836, 0.00017843, 507.62049454, 0.00059478, -50.76204945, -5.948e-05, -152.28614836, -0.00017843, -507.62049454, -0.00059478, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 14.5, 0.0, 3.225)
    ops.node(124027, 14.5, 0.0, 4.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.1225, 28491030.86908226, 11871262.86211761, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 105.67172848, 0.00050779, 126.5707277, 0.01142741, 12.65707277, 0.0396099, -105.67172848, -0.00050779, -126.5707277, -0.01142741, -12.65707277, -0.0396099, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 96.59641233, 0.00050779, 115.70056038, 0.01142741, 11.57005604, 0.0396099, -96.59641233, -0.00050779, -115.70056038, -0.01142741, -11.57005604, -0.0396099, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 183.16939199, 0.01015582, 183.16939199, 0.03046747, 128.21857439, -2762.76102434, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 45.792348, 5.479e-05, 137.37704399, 0.00016437, 457.92347996, 0.00054791, -45.792348, -5.479e-05, -137.37704399, -0.00016437, -457.92347996, -0.00054791, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 183.16939199, 0.01015582, 183.16939199, 0.03046747, 128.21857439, -2762.76102434, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 45.792348, 5.479e-05, 137.37704399, 0.00016437, 457.92347996, 0.00054791, -45.792348, -5.479e-05, -137.37704399, -0.00016437, -457.92347996, -0.00054791, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 14.5, 0.0, 4.55)
    ops.node(122003, 14.5, 0.0, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.1225, 25583262.33364213, 10659692.63901755, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 99.64483175, 0.00051277, 119.37449824, 0.01049304, 11.93744982, 0.03368193, -99.64483175, -0.00051277, -119.37449824, -0.01049304, -11.93744982, -0.03368193, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 90.74567166, 0.00051277, 108.71330536, 0.01049304, 10.87133054, 0.03368193, -90.74567166, -0.00051277, -108.71330536, -0.01049304, -10.87133054, -0.03368193, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 159.57770608, 0.01025534, 159.57770608, 0.03076602, 111.70439426, -2533.96292646, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 39.89442652, 5.316e-05, 119.68327956, 0.00015948, 398.9442652, 0.00053159, -39.89442652, -5.316e-05, -119.68327956, -0.00015948, -398.9442652, -0.00053159, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 159.57770608, 0.01025534, 159.57770608, 0.03076602, 111.70439426, -2533.96292646, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 39.89442652, 5.316e-05, 119.68327956, 0.00015948, 398.9442652, 0.00053159, -39.89442652, -5.316e-05, -119.68327956, -0.00015948, -398.9442652, -0.00053159, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 17.65, 0.0, 3.225)
    ops.node(124028, 17.65, 0.0, 4.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.1225, 26954743.1905279, 11231142.99605329, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 106.01108922, 0.00052338, 126.93106621, 0.01007173, 12.69310662, 0.03498957, -106.01108922, -0.00052338, -126.93106621, -0.01007173, -12.69310662, -0.03498957, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 96.98028677, 0.00052338, 116.11814663, 0.01007173, 11.61181466, 0.03498957, -96.98028677, -0.00052338, -116.11814663, -0.01007173, -11.61181466, -0.03498957, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 169.76609324, 0.0104676, 169.76609324, 0.03140281, 118.83626527, -2587.07724315, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 42.44152331, 5.368e-05, 127.32456993, 0.00016103, 424.41523311, 0.00053676, -42.44152331, -5.368e-05, -127.32456993, -0.00016103, -424.41523311, -0.00053676, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 169.76609324, 0.0104676, 169.76609324, 0.03140281, 118.83626527, -2587.07724315, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 42.44152331, 5.368e-05, 127.32456993, 0.00016103, 424.41523311, 0.00053676, -42.44152331, -5.368e-05, -127.32456993, -0.00016103, -424.41523311, -0.00053676, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 17.65, 0.0, 4.55)
    ops.node(122004, 17.65, 0.0, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.1225, 28396476.63343848, 11831865.2639327, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 93.1499785, 0.00046618, 111.75152766, 0.01044865, 11.17515277, 0.03979462, -93.1499785, -0.00046618, -111.75152766, -0.01044865, -11.17515277, -0.03979462, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 85.46388184, 0.00046618, 102.53055887, 0.01044865, 10.25305589, 0.03979462, -85.46388184, -0.00046618, -102.53055887, -0.01044865, -10.25305589, -0.03979462, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 173.59996892, 0.00932352, 173.59996892, 0.02797057, 121.51997824, -2430.69567722, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 43.39999223, 5.21e-05, 130.19997669, 0.0001563, 433.99992229, 0.00052101, -43.39999223, -5.21e-05, -130.19997669, -0.0001563, -433.99992229, -0.00052101, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 173.59996892, 0.00932352, 173.59996892, 0.02797057, 121.51997824, -2430.69567722, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 43.39999223, 5.21e-05, 130.19997669, 0.0001563, 433.99992229, 0.00052101, -43.39999223, -5.21e-05, -130.19997669, -0.0001563, -433.99992229, -0.00052101, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 14.5, 0.0, 6.125)
    ops.node(124029, 14.5, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.0625, 28518804.09476491, 11882835.03948538, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 48.65352357, 0.00057129, 57.97108641, 0.01099269, 5.79710864, 0.04227476, -48.65352357, -0.00057129, -57.97108641, -0.01099269, -5.79710864, -0.04227476, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 45.57206443, 0.00057129, 54.29950168, 0.01099269, 5.42995017, 0.04227476, -45.57206443, -0.00057129, -54.29950168, -0.01099269, -5.42995017, -0.04227476, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 74.16092901, 0.01142574, 74.16092901, 0.03427723, 51.9126503, -1758.41063369, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 18.54023225, 4.344e-05, 55.62069675, 0.00013031, 185.40232252, 0.00043437, -18.54023225, -4.344e-05, -55.62069675, -0.00013031, -185.40232252, -0.00043437, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 74.16092901, 0.01142574, 74.16092901, 0.03427723, 51.9126503, -1758.41063369, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 18.54023225, 4.344e-05, 55.62069675, 0.00013031, 185.40232252, 0.00043437, -18.54023225, -4.344e-05, -55.62069675, -0.00013031, -185.40232252, -0.00043437, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 14.5, 0.0, 7.45)
    ops.node(123003, 14.5, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.0625, 25213321.69776824, 10505550.70740344, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 44.9342824, 0.00062515, 53.51726402, 0.00894854, 5.3517264, 0.03362236, -44.9342824, -0.00062515, -53.51726402, -0.00894854, -5.3517264, -0.03362236, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 42.22245523, 0.00062515, 50.28744566, 0.00894854, 5.02874457, 0.03362236, -42.22245523, -0.00062515, -50.28744566, -0.00894854, -5.02874457, -0.03362236, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 55.88460504, 0.012503, 55.88460504, 0.03750899, 39.11922353, -1518.89400962, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 13.97115126, 3.702e-05, 41.91345378, 0.00011107, 139.71151259, 0.00037024, -13.97115126, -3.702e-05, -41.91345378, -0.00011107, -139.71151259, -0.00037024, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 55.88460504, 0.012503, 55.88460504, 0.03750899, 39.11922353, -1518.89400962, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 13.97115126, 3.702e-05, 41.91345378, 0.00011107, 139.71151259, 0.00037024, -13.97115126, -3.702e-05, -41.91345378, -0.00011107, -139.71151259, -0.00037024, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 17.65, 0.0, 6.125)
    ops.node(124030, 17.65, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.0625, 30556383.90219208, 12731826.62591337, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 46.33545514, 0.00058308, 55.17879231, 0.01092072, 5.51787923, 0.04749655, -46.33545514, -0.00058308, -55.17879231, -0.01092072, -5.51787923, -0.04749655, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 44.03455081, 0.00058308, 52.43874968, 0.01092072, 5.24387497, 0.04749655, -44.03455081, -0.00058308, -52.43874968, -0.01092072, -5.24387497, -0.04749655, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 72.63850506, 0.0116617, 72.63850506, 0.03498509, 50.84695354, -1689.98880823, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 18.15962627, 3.971e-05, 54.4788788, 0.00011913, 181.59626265, 0.00039709, -18.15962627, -3.971e-05, -54.4788788, -0.00011913, -181.59626265, -0.00039709, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 72.63850506, 0.0116617, 72.63850506, 0.03498509, 50.84695354, -1689.98880823, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 18.15962627, 3.971e-05, 54.4788788, 0.00011913, 181.59626265, 0.00039709, -18.15962627, -3.971e-05, -54.4788788, -0.00011913, -181.59626265, -0.00039709, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 17.65, 0.0, 7.45)
    ops.node(123004, 17.65, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.0625, 29428727.98414889, 12261969.99339537, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 42.98061411, 0.00058318, 51.36823823, 0.01405467, 5.13682382, 0.05093513, -42.98061411, -0.00058318, -51.36823823, -0.01405467, -5.13682382, -0.05093513, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 40.71417658, 0.00058318, 48.65950768, 0.01405467, 4.86595077, 0.05093513, -40.71417658, -0.00058318, -48.65950768, -0.01405467, -4.86595077, -0.05093513, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 83.24286089, 0.01166355, 83.24286089, 0.03499064, 58.27000262, -1835.40434768, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 20.81071522, 4.725e-05, 62.43214566, 0.00014175, 208.10715222, 0.00047249, -20.81071522, -4.725e-05, -62.43214566, -0.00014175, -208.10715222, -0.00047249, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 83.24286089, 0.01166355, 83.24286089, 0.03499064, 58.27000262, -1835.40434768, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 20.81071522, 4.725e-05, 62.43214566, 0.00014175, 208.10715222, 0.00047249, -20.81071522, -4.725e-05, -62.43214566, -0.00014175, -208.10715222, -0.00047249, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 14.5, 0.0, 9.025)
    ops.node(124031, 14.5, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.0625, 24862671.30155714, 10359446.37564881, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 25.08086305, 0.000516, 30.44015354, 0.01396907, 3.04401535, 0.05638696, -25.08086305, -0.000516, -30.44015354, -0.01396907, -3.04401535, -0.05638696, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 25.08086305, 0.000516, 30.44015354, 0.01396907, 3.04401535, 0.05638696, -25.08086305, -0.000516, -30.44015354, -0.01396907, -3.04401535, -0.05638696, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 60.04032645, 0.0103201, 60.04032645, 0.03096029, 42.02822852, -1458.74740384, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 15.01008161, 4.034e-05, 45.03024484, 0.00012101, 150.10081614, 0.00040338, -15.01008161, -4.034e-05, -45.03024484, -0.00012101, -150.10081614, -0.00040338, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 60.04032645, 0.0103201, 60.04032645, 0.03096029, 42.02822852, -1458.74740384, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 15.01008161, 4.034e-05, 45.03024484, 0.00012101, 150.10081614, 0.00040338, -15.01008161, -4.034e-05, -45.03024484, -0.00012101, -150.10081614, -0.00040338, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 14.5, 0.0, 10.35)
    ops.node(124003, 14.5, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.0625, 30386348.21305013, 12660978.42210422, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 21.46301169, 0.00050462, 25.96219125, 0.01423453, 2.59621912, 0.07163677, -21.46301169, -0.00050462, -25.96219125, -0.01423453, -2.59621912, -0.07163677, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 21.46301169, 0.00050462, 25.96219125, 0.01423453, 2.59621912, 0.07163677, -21.46301169, -0.00050462, -25.96219125, -0.01423453, -2.59621912, -0.07163677, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 61.26507776, 0.01009238, 61.26507776, 0.03027715, 42.88555443, -1230.22385828, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 15.31626944, 3.368e-05, 45.94880832, 0.00010104, 153.1626944, 0.00033679, -15.31626944, -3.368e-05, -45.94880832, -0.00010104, -153.1626944, -0.00033679, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 61.26507776, 0.01009238, 61.26507776, 0.03027715, 42.88555443, -1230.22385828, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 15.31626944, 3.368e-05, 45.94880832, 0.00010104, 153.1626944, 0.00033679, -15.31626944, -3.368e-05, -45.94880832, -0.00010104, -153.1626944, -0.00033679, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 17.65, 0.0, 9.025)
    ops.node(124032, 17.65, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.0625, 29178619.189666, 12157757.99569417, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 23.9183215, 0.00053386, 28.92295065, 0.01547254, 2.89229506, 0.06669824, -23.9183215, -0.00053386, -28.92295065, -0.01547254, -2.89229506, -0.06669824, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 23.9183215, 0.00053386, 28.92295065, 0.01547254, 2.89229506, 0.06669824, -23.9183215, -0.00053386, -28.92295065, -0.01547254, -2.89229506, -0.06669824, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 68.33269271, 0.01067713, 68.33269271, 0.03203138, 47.8328849, -1400.00027729, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 17.08317318, 3.912e-05, 51.24951953, 0.00011736, 170.83173177, 0.00039119, -17.08317318, -3.912e-05, -51.24951953, -0.00011736, -170.83173177, -0.00039119, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 68.33269271, 0.01067713, 68.33269271, 0.03203138, 47.8328849, -1400.00027729, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 17.08317318, 3.912e-05, 51.24951953, 0.00011736, 170.83173177, 0.00039119, -17.08317318, -3.912e-05, -51.24951953, -0.00011736, -170.83173177, -0.00039119, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 17.65, 0.0, 10.35)
    ops.node(124004, 17.65, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.0625, 29617636.84838444, 12340682.02016018, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 20.79158558, 0.00049295, 25.19546961, 0.01447277, 2.51954696, 0.07109329, -20.79158558, -0.00049295, -25.19546961, -0.01447277, -2.51954696, -0.07109329, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 20.79158558, 0.00049295, 25.19546961, 0.01447277, 2.51954696, 0.07109329, -20.79158558, -0.00049295, -25.19546961, -0.01447277, -2.51954696, -0.07109329, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 59.82063652, 0.00985891, 59.82063652, 0.02957673, 41.87444556, -1315.68931466, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 14.95515913, 3.374e-05, 44.86547739, 0.00010121, 149.5515913, 0.00033738, -14.95515913, -3.374e-05, -44.86547739, -0.00010121, -149.5515913, -0.00033738, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 59.82063652, 0.00985891, 59.82063652, 0.02957673, 41.87444556, -1315.68931466, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 14.95515913, 3.374e-05, 44.86547739, 0.00010121, 149.5515913, 0.00033738, -14.95515913, -3.374e-05, -44.86547739, -0.00010121, -149.5515913, -0.00033738, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
