import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 7.35, 0.0, 0.0)
    ops.node(121003, 7.35, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.14, 26119670.70288791, 10883196.1262033, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 142.46438254, 0.00070869, 169.47947864, 0.01087446, 16.94794786, 0.02853887, -142.46438254, -0.00070869, -169.47947864, -0.01087446, -16.94794786, -0.02853887, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 149.80129517, 0.00064684, 178.20766813, 0.01123401, 17.82076681, 0.030685, -149.80129517, -0.00064684, -178.20766813, -0.01123401, -17.82076681, -0.030685, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 142.10028888, 0.01417375, 142.10028888, 0.04252126, 99.47020222, -1561.97845365, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 35.52507222, 8.813e-05, 106.57521666, 0.0002644, 355.25072221, 0.00088134, -35.52507222, -8.813e-05, -106.57521666, -0.0002644, -355.25072221, -0.00088134, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 146.94686053, 0.0129368, 146.94686053, 0.0388104, 102.86280237, -1652.94782388, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 36.73671513, 9.114e-05, 110.2101454, 0.00027342, 367.36715132, 0.0009114, -36.73671513, -9.114e-05, -110.2101454, -0.00027342, -367.36715132, -0.0009114, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 11.6, 0.0, 0.0)
    ops.node(121004, 11.6, 0.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.0625, 29572314.77056647, 12321797.82106936, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 53.38111412, 0.00097876, 63.15570802, 0.01100487, 6.3155708, 0.03861002, -53.38111412, -0.00097876, -63.15570802, -0.01100487, -6.3155708, -0.03861002, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 56.00335423, 0.00097876, 66.25810543, 0.01100487, 6.62581054, 0.03861002, -56.00335423, -0.00097876, -66.25810543, -0.01100487, -6.62581054, -0.03861002, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 80.56545592, 0.01957521, 80.56545592, 0.05872562, 56.39581914, -954.85654022, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 20.14136398, 9.886e-05, 60.42409194, 0.00029658, 201.41363979, 0.00098861, -20.14136398, -9.886e-05, -60.42409194, -0.00029658, -201.41363979, -0.00098861, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 80.56545592, 0.01957521, 80.56545592, 0.05872562, 56.39581914, -954.85654022, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 20.14136398, 9.886e-05, 60.42409194, 0.00029658, 201.41363979, 0.00098861, -20.14136398, -9.886e-05, -60.42409194, -0.00029658, -201.41363979, -0.00098861, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.4, 0.0)
    ops.node(121005, 0.0, 4.4, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.075, 29066308.54822284, 12110961.89509285, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 75.3110383, 0.00080526, 89.12921339, 0.01094947, 8.91292134, 0.03766487, -75.3110383, -0.00080526, -89.12921339, -0.01094947, -8.91292134, -0.03766487, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 59.53520483, 0.0009442, 70.45880783, 0.01049601, 7.04588078, 0.03365788, -59.53520483, -0.0009442, -70.45880783, -0.01049601, -7.04588078, -0.03365788, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 98.19945037, 0.01610527, 98.19945037, 0.04831581, 68.73961526, -1153.22898551, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 24.54986259, 0.00010216, 73.64958778, 0.00030649, 245.49862592, 0.00102165, -24.54986259, -0.00010216, -73.64958778, -0.00030649, -245.49862592, -0.00102165, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 92.92762183, 0.01888397, 92.92762183, 0.05665192, 65.04933528, -1073.36071944, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 23.23190546, 9.668e-05, 69.69571637, 0.00029004, 232.31905456, 0.0009668, -23.23190546, -9.668e-05, -69.69571637, -0.00029004, -232.31905456, -0.0009668, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 3.1, 4.4, 0.0)
    ops.node(121006, 3.1, 4.4, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.1925, 28999916.03559846, 12083298.34816602, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 309.88471083, 0.00053137, 370.81315742, 0.01206889, 37.08131574, 0.03274137, -309.88471083, -0.00053137, -370.81315742, -0.01206889, -37.08131574, -0.03274137, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 229.66095442, 0.00068088, 274.81608698, 0.0110229, 27.4816087, 0.0269707, -229.66095442, -0.00068088, -274.81608698, -0.0110229, -27.4816087, -0.0269707, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 212.4837945, 0.01062739, 212.4837945, 0.03188218, 148.73865615, -1753.4699935, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 53.12094862, 8.633e-05, 159.36284587, 0.00025898, 531.20948624, 0.00086326, -53.12094862, -8.633e-05, -159.36284587, -0.00025898, -531.20948624, -0.00086326, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 181.15187909, 0.01361766, 181.15187909, 0.04085299, 126.80631536, -1533.058898, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 45.28796977, 7.36e-05, 135.86390932, 0.00022079, 452.87969773, 0.00073597, -45.28796977, -7.36e-05, -135.86390932, -0.00022079, -452.87969773, -0.00073597, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 7.35, 4.4, 0.0)
    ops.node(121007, 7.35, 4.4, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.24, 28588677.97429515, 11911949.15595631, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 371.89110054, 0.00051985, 445.78784446, 0.01183352, 44.57878445, 0.03512098, -371.89110054, -0.00051985, -445.78784446, -0.01183352, -44.57878445, -0.03512098, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 307.37683099, 0.00063262, 368.45424567, 0.01081225, 36.84542457, 0.02893864, -307.37683099, -0.00063262, -368.45424567, -0.01081225, -36.84542457, -0.02893864, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 273.22338849, 0.01039694, 273.22338849, 0.03119082, 191.25637194, -2041.54615199, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 68.30584712, 9.031e-05, 204.91754137, 0.00027094, 683.05847123, 0.00090314, -68.30584712, -9.031e-05, -204.91754137, -0.00027094, -683.05847123, -0.00090314, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 217.7709479, 0.01265233, 217.7709479, 0.037957, 152.43966353, -1799.41138137, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 54.44273697, 7.198e-05, 163.32821092, 0.00021595, 544.42736974, 0.00071984, -54.44273697, -7.198e-05, -163.32821092, -0.00021595, -544.42736974, -0.00071984, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 11.6, 4.4, 0.0)
    ops.node(121008, 11.6, 4.4, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.12, 27933934.44590719, 11639139.35246133, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 139.49622435, 0.00065579, 165.57895019, 0.01007704, 16.55789502, 0.03323151, -139.49622435, -0.00065579, -165.57895019, -0.01007704, -16.55789502, -0.03323151, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 115.63653484, 0.00079996, 137.25802352, 0.00941537, 13.72580235, 0.02814458, -115.63653484, -0.00079996, -137.25802352, -0.00941537, -13.72580235, -0.02814458, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 140.25844113, 0.01311574, 140.25844113, 0.03934723, 98.18090879, -1583.72389109, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 35.06461028, 9.49e-05, 105.19383085, 0.0002847, 350.64610282, 0.00094898, -35.06461028, -9.49e-05, -105.19383085, -0.0002847, -350.64610282, -0.00094898, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 131.5840173, 0.01599925, 131.5840173, 0.04799775, 92.10881211, -1426.82879826, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 32.89600433, 8.903e-05, 98.68801298, 0.00026709, 328.96004326, 0.00089029, -32.89600433, -8.903e-05, -98.68801298, -0.00026709, -328.96004326, -0.00089029, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.8, 0.0)
    ops.node(121009, 0.0, 8.8, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.105, 29891199.07830913, 12454666.28262881, 0.00152551, 0.00086625, 0.00117906, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 108.14504668, 0.00069213, 128.91682169, 0.01252581, 12.89168217, 0.04333127, -108.14504668, -0.00069213, -128.91682169, -0.01252581, -12.89168217, -0.04333127, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 84.1641721, 0.00077183, 100.32986161, 0.01204189, 10.03298616, 0.03948005, -84.1641721, -0.00077183, -100.32986161, -0.01204189, -10.03298616, -0.03948005, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 128.19093188, 0.01384259, 128.19093188, 0.04152777, 89.73365232, -1337.58630988, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 32.04773297, 9.263e-05, 96.14319891, 0.0002779, 320.47732971, 0.00092633, -32.04773297, -9.263e-05, -96.14319891, -0.0002779, -320.47732971, -0.00092633, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 123.39289734, 0.01543652, 123.39289734, 0.04630957, 86.37502814, -1245.11785059, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 30.84822433, 8.917e-05, 92.544673, 0.0002675, 308.48224335, 0.00089166, -30.84822433, -8.917e-05, -92.544673, -0.0002675, -308.48224335, -0.00089166, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 3.1, 8.8, 0.0)
    ops.node(121010, 3.1, 8.8, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.1925, 28440848.95627252, 11850353.73178022, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 297.5169794, 0.00053558, 356.39028062, 0.01055595, 35.63902806, 0.03096457, -297.5169794, -0.00053558, -356.39028062, -0.01055595, -35.63902806, -0.03096457, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 215.73444316, 0.00068523, 258.42443982, 0.00966729, 25.84244398, 0.02541153, -215.73444316, -0.00068523, -258.42443982, -0.00966729, -25.84244398, -0.02541153, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 200.71688, 0.01071162, 200.71688, 0.03213485, 140.501816, -1607.33287115, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 50.17922, 8.315e-05, 150.53766, 0.00024945, 501.7922, 0.00083148, -50.17922, -8.315e-05, -150.53766, -0.00024945, -501.7922, -0.00083148, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 163.9850731, 0.01370458, 163.9850731, 0.04111374, 114.78955117, -1425.09741901, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 40.99626827, 6.793e-05, 122.98880482, 0.0002038, 409.96268275, 0.00067932, -40.99626827, -6.793e-05, -122.98880482, -0.0002038, -409.96268275, -0.00067932, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.35, 8.8, 0.0)
    ops.node(121011, 7.35, 8.8, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.24, 28275730.93428167, 11781554.55595069, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 367.71354084, 0.00051464, 440.87899276, 0.01255466, 44.08789928, 0.03543653, -367.71354084, -0.00051464, -440.87899276, -0.01255466, -44.08789928, -0.03543653, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 305.26772857, 0.00062355, 366.00808441, 0.01145673, 36.60080844, 0.02926741, -305.26772857, -0.00062355, -366.00808441, -0.01145673, -36.60080844, -0.02926741, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 272.43403241, 0.0102928, 272.43403241, 0.0308784, 190.70382269, -2080.36576791, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 68.1085081, 9.105e-05, 204.32552431, 0.00027315, 681.08508103, 0.0009105, -68.1085081, -9.105e-05, -204.32552431, -0.00027315, -681.08508103, -0.0009105, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 216.72440644, 0.01247104, 216.72440644, 0.03741312, 151.70708451, -1820.19883211, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 54.18110161, 7.243e-05, 162.54330483, 0.00021729, 541.8110161, 0.00072431, -54.18110161, -7.243e-05, -162.54330483, -0.00021729, -541.8110161, -0.00072431, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 11.6, 8.8, 0.0)
    ops.node(121012, 11.6, 8.8, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.12, 29899976.45938116, 12458323.52474215, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 136.86919712, 0.00062816, 162.63339326, 0.0126476, 16.26333933, 0.04065406, -136.86919712, -0.00062816, -162.63339326, -0.0126476, -16.26333933, -0.04065406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 112.7663629, 0.00076417, 133.99345236, 0.01175553, 13.39934524, 0.03440943, -112.7663629, -0.00076417, -133.99345236, -0.01175553, -13.39934524, -0.03440943, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 154.2255252, 0.01256316, 154.2255252, 0.03768948, 107.95786764, -1694.40090677, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 38.5563813, 9.749e-05, 115.6691439, 0.00029246, 385.56381299, 0.00097487, -38.5563813, -9.749e-05, -115.6691439, -0.00029246, -385.56381299, -0.00097487, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 144.0230708, 0.0152834, 144.0230708, 0.04585021, 100.81614956, -1503.72641836, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 36.0057677, 9.104e-05, 108.0173031, 0.00027311, 360.05767701, 0.00091038, -36.0057677, -9.104e-05, -108.0173031, -0.00027311, -360.05767701, -0.00091038, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 13.2, 0.0)
    ops.node(121013, 0.0, 13.2, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.075, 29480732.14386581, 12283638.39327742, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 78.84532598, 0.00083129, 93.19257709, 0.01118414, 9.31925771, 0.03779849, -78.84532598, -0.00083129, -93.19257709, -0.01118414, -9.31925771, -0.03779849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 62.41231182, 0.00097732, 73.76929588, 0.01072559, 7.37692959, 0.03379984, -62.41231182, -0.00097732, -73.76929588, -0.01072559, -7.37692959, -0.03379984, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 102.44032219, 0.01662588, 102.44032219, 0.04987764, 71.70822554, -1221.39659648, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 25.61008055, 0.00010508, 76.83024165, 0.00031524, 256.10080549, 0.00105079, -25.61008055, -0.00010508, -76.83024165, -0.00031524, -256.10080549, -0.00105079, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 97.81022165, 0.0195464, 97.81022165, 0.05863919, 68.46715516, -1135.86100823, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 24.45255541, 0.00010033, 73.35766624, 0.00030099, 244.52555413, 0.00100329, -24.45255541, -0.00010033, -73.35766624, -0.00030099, -244.52555413, -0.00100329, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 3.1, 13.2, 0.0)
    ops.node(121014, 3.1, 13.2, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.1925, 27468781.31711004, 11445325.54879585, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 286.17813561, 0.00053105, 342.76218022, 0.01266475, 34.27621802, 0.03555121, -286.17813561, -0.00053105, -342.76218022, -0.01266475, -34.27621802, -0.03555121, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 224.43319075, 0.0006787, 268.8088299, 0.01141068, 26.88088299, 0.02851531, -224.43319075, -0.0006787, -268.8088299, -0.01141068, -26.88088299, -0.02851531, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 208.08032873, 0.01062099, 208.08032873, 0.03186297, 145.65623011, -1863.61373483, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 52.02008218, 8.925e-05, 156.06024655, 0.00026775, 520.20082183, 0.00089249, -52.02008218, -8.925e-05, -156.06024655, -0.00026775, -520.20082183, -0.00089249, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 175.0441916, 0.013574, 175.0441916, 0.04072201, 122.53093412, -1578.01048033, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 43.7610479, 7.508e-05, 131.2831437, 0.00022524, 437.610479, 0.00075079, -43.7610479, -7.508e-05, -131.2831437, -0.00022524, -437.610479, -0.00075079, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.35, 13.2, 0.0)
    ops.node(121015, 7.35, 13.2, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.24, 29411701.51323947, 12254875.63051645, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 370.20243153, 0.0005135, 443.57624867, 0.01165625, 44.35762487, 0.03624097, -370.20243153, -0.0005135, -443.57624867, -0.01165625, -44.35762487, -0.03624097, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 306.07642937, 0.00062231, 366.74052567, 0.01064815, 36.67405257, 0.02978429, -306.07642937, -0.00062231, -366.74052567, -0.01064815, -36.67405257, -0.02978429, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 280.38347867, 0.01027003, 280.38347867, 0.0308101, 196.26843507, -2031.31338684, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 70.09586967, 9.009e-05, 210.287609, 0.00027026, 700.95869667, 0.00090087, -70.09586967, -9.009e-05, -210.287609, -0.00027026, -700.95869667, -0.00090087, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 223.68462093, 0.01244621, 223.68462093, 0.03733864, 156.57923465, -1790.78677408, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 55.92115523, 7.187e-05, 167.7634657, 0.00021561, 559.21155233, 0.0007187, -55.92115523, -7.187e-05, -167.7634657, -0.00021561, -559.21155233, -0.0007187, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 11.6, 13.2, 0.0)
    ops.node(121016, 11.6, 13.2, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.12, 27811112.37580542, 11587963.48991892, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 137.90080224, 0.00064916, 163.67761424, 0.01056907, 16.36776142, 0.03348234, -137.90080224, -0.00064916, -163.67761424, -0.01056907, -16.36776142, -0.03348234, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 114.15112571, 0.00079183, 135.48858031, 0.00986325, 13.54885803, 0.02839736, -114.15112571, -0.00079183, -135.48858031, -0.00986325, -13.54885803, -0.02839736, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 139.51912164, 0.01298317, 139.51912164, 0.03894951, 97.66338515, -1578.4185816, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 34.87978041, 9.482e-05, 104.63934123, 0.00028445, 348.7978041, 0.00094815, -34.87978041, -9.482e-05, -104.63934123, -0.00028445, -348.7978041, -0.00094815, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 130.87372845, 0.01583665, 130.87372845, 0.04750996, 91.61160991, -1422.04841393, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 32.71843211, 8.894e-05, 98.15529634, 0.00026682, 327.18432112, 0.0008894, -32.71843211, -8.894e-05, -98.15529634, -0.00026682, -327.18432112, -0.0008894, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 17.6, 0.0)
    ops.node(121017, 0.0, 17.6, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.105, 30777085.77421134, 12823785.73925472, 0.00152551, 0.00086625, 0.00117906, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 107.41382455, 0.00067596, 127.94727746, 0.01116316, 12.79472775, 0.04377759, -107.41382455, -0.00067596, -127.94727746, -0.01116316, -12.79472775, -0.04377759, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 83.72814862, 0.00075249, 99.73379783, 0.0107402, 9.97337978, 0.0397896, -83.72814862, -0.00075249, -99.73379783, -0.0107402, -9.97337978, -0.0397896, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 126.94196371, 0.01351912, 126.94196371, 0.04055735, 88.8593746, -1252.88865375, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 31.73549093, 8.909e-05, 95.20647279, 0.00026727, 317.35490928, 0.00089091, -31.73549093, -8.909e-05, -95.20647279, -0.00026727, -317.35490928, -0.00089091, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 122.78635305, 0.01504975, 122.78635305, 0.04514925, 85.95044714, -1175.34494981, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 30.69658826, 8.617e-05, 92.08976479, 0.00025852, 306.96588263, 0.00086174, -30.69658826, -8.617e-05, -92.08976479, -0.00025852, -306.96588263, -0.00086174, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 3.1, 17.6, 0.0)
    ops.node(121018, 3.1, 17.6, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.1925, 31267157.87698254, 13027982.44874272, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 291.7108954, 0.00052996, 348.46508491, 0.01341339, 34.84650849, 0.04248517, -291.7108954, -0.00052996, -348.46508491, -0.01341339, -34.84650849, -0.04248517, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 224.66090196, 0.00068142, 268.37009351, 0.01207651, 26.83700935, 0.03380386, -224.66090196, -0.00068142, -268.37009351, -0.01207651, -26.83700935, -0.03380386, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 232.98422348, 0.01059929, 232.98422348, 0.03179787, 163.08895644, -1833.03316915, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 58.24605587, 8.779e-05, 174.73816761, 0.00026337, 582.4605587, 0.00087791, -58.24605587, -8.779e-05, -174.73816761, -0.00026337, -582.4605587, -0.00087791, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 197.77151793, 0.01362839, 197.77151793, 0.04088518, 138.44006255, -1560.81873568, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 49.44287948, 7.452e-05, 148.32863845, 0.00022357, 494.42879484, 0.00074523, -49.44287948, -7.452e-05, -148.32863845, -0.00022357, -494.42879484, -0.00074523, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 7.35, 17.6, 0.0)
    ops.node(121019, 7.35, 17.6, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.24, 29326258.13271105, 12219274.22196294, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 382.26355534, 0.00052467, 458.04754122, 0.01176335, 45.80475412, 0.03620438, -382.26355534, -0.00052467, -458.04754122, -0.01176335, -45.80475412, -0.03620438, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 319.58719479, 0.00063589, 382.94555349, 0.01074805, 38.29455535, 0.02977235, -319.58719479, -0.00063589, -382.94555349, -0.01074805, -38.29455535, -0.02977235, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 280.94165542, 0.01049339, 280.94165542, 0.03148017, 196.65915879, -2056.04258462, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 70.23541386, 9.053e-05, 210.70624157, 0.00027159, 702.35413855, 0.0009053, -70.23541386, -9.053e-05, -210.70624157, -0.00027159, -702.35413855, -0.0009053, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 223.94924626, 0.01271785, 223.94924626, 0.03815356, 156.76447238, -1807.0233592, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 55.98731156, 7.216e-05, 167.96193469, 0.00021649, 559.87311565, 0.00072165, -55.98731156, -7.216e-05, -167.96193469, -0.00021649, -559.87311565, -0.00072165, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 11.6, 17.6, 0.0)
    ops.node(121020, 11.6, 17.6, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.12, 31207483.07457853, 13003117.94774106, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 142.71950909, 0.00066094, 169.44314869, 0.01033262, 16.94431487, 0.04112834, -142.71950909, -0.00066094, -169.44314869, -0.01033262, -16.94431487, -0.04112834, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 117.53007046, 0.00080954, 139.53709154, 0.00965396, 13.95370915, 0.03456404, -117.53007046, -0.00080954, -139.53709154, -0.00965396, -13.95370915, -0.03456404, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 150.73975905, 0.01321871, 150.73975905, 0.03965613, 105.51783134, -1527.20187689, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 37.68493976, 9.129e-05, 113.05481929, 0.00027387, 376.84939764, 0.00091292, -37.68493976, -9.129e-05, -113.05481929, -0.00027387, -376.84939764, -0.00091292, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 142.8053106, 0.01619089, 142.8053106, 0.04857267, 99.96371742, -1385.87311696, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 35.70132765, 8.649e-05, 107.10398295, 0.00025946, 357.0132765, 0.00086486, -35.70132765, -8.649e-05, -107.10398295, -0.00025946, -357.0132765, -0.00086486, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 0.0, 22.0, 0.0)
    ops.node(121021, 0.0, 22.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.075, 26974783.30074484, 11239493.04197701, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 59.27031915, 0.00077953, 70.86389353, 0.01372762, 7.08638935, 0.04467478, -59.27031915, -0.00077953, -70.86389353, -0.01372762, -7.08638935, -0.04467478, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 46.12706637, 0.00091086, 55.149754, 0.01310282, 5.5149754, 0.03993356, -46.12706637, -0.00091086, -55.149754, -0.01310282, -5.5149754, -0.03993356, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 89.84883951, 0.0155906, 89.84883951, 0.04677179, 62.89418765, -1070.92677396, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 22.46220988, 0.00010072, 67.38662963, 0.00030217, 224.62209877, 0.00100725, -22.46220988, -0.00010072, -67.38662963, -0.00030217, -224.62209877, -0.00100725, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 84.44774465, 0.01821728, 84.44774465, 0.05465185, 59.11342126, -953.71525284, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 21.11193616, 9.467e-05, 63.33580849, 0.00028401, 211.11936163, 0.0009467, -21.11193616, -9.467e-05, -63.33580849, -0.00028401, -211.11936163, -0.0009467, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 3.1, 22.0, 0.0)
    ops.node(121022, 3.1, 22.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.1225, 29374857.33694636, 12239523.89039432, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 130.056232, 0.00069722, 155.22915941, 0.01179178, 15.52291594, 0.03903685, -130.056232, -0.00069722, -155.22915941, -0.01179178, -15.52291594, -0.03903685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 113.20384262, 0.00069722, 135.11491962, 0.01179178, 13.51149196, 0.03903685, -113.20384262, -0.00069722, -135.11491962, -0.01179178, -13.51149196, -0.03903685, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 138.50578516, 0.01394447, 138.50578516, 0.0418334, 96.95404961, -1383.6385988, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 34.62644629, 8.73e-05, 103.87933887, 0.00026189, 346.26446289, 0.00087297, -34.62644629, -8.73e-05, -103.87933887, -0.00026189, -346.26446289, -0.00087297, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 138.50578516, 0.01394447, 138.50578516, 0.0418334, 96.95404961, -1383.6385988, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 34.62644629, 8.73e-05, 103.87933887, 0.00026189, 346.26446289, 0.00087297, -34.62644629, -8.73e-05, -103.87933887, -0.00026189, -346.26446289, -0.00087297, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 7.35, 22.0, 0.0)
    ops.node(121023, 7.35, 22.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.14, 26806364.07744209, 11169318.36560087, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 183.48615978, 0.00071777, 218.52816326, 0.01127594, 21.85281633, 0.02813946, -183.48615978, -0.00071777, -218.52816326, -0.01127594, -21.85281633, -0.02813946, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 173.96105733, 0.00065653, 207.18396626, 0.01162771, 20.71839663, 0.03009818, -173.96105733, -0.00065653, -207.18396626, -0.01162771, -20.71839663, -0.03009818, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 136.53018457, 0.01435546, 136.53018457, 0.04306638, 95.5711292, -1406.5603958, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 34.13254614, 8.251e-05, 102.39763843, 0.00024753, 341.32546142, 0.0008251, -34.13254614, -8.251e-05, -102.39763843, -0.00024753, -341.32546142, -0.0008251, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 140.12685805, 0.01313057, 140.12685805, 0.0393917, 98.08880064, -1470.34868344, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 35.03171451, 8.468e-05, 105.09514354, 0.00025405, 350.31714513, 0.00084683, -35.03171451, -8.468e-05, -105.09514354, -0.00025405, -350.31714513, -0.00084683, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 11.6, 22.0, 0.0)
    ops.node(121024, 11.6, 22.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.075, 29034381.50609666, 12097658.96087361, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 66.74991079, 0.00079117, 79.34634536, 0.01123373, 7.93463454, 0.04162231, -66.74991079, -0.00079117, -79.34634536, -0.01123373, -7.93463454, -0.04162231, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 58.05648747, 0.00092061, 69.01237845, 0.01075335, 6.90123785, 0.0370998, -58.05648747, -0.00092061, -69.01237845, -0.01075335, -6.90123785, -0.0370998, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 93.57062603, 0.0158234, 93.57062603, 0.04747019, 65.49943822, -1045.84871567, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 23.39265651, 9.746e-05, 70.17796952, 0.00029237, 233.92656507, 0.00097456, -23.39265651, -9.746e-05, -70.17796952, -0.00029237, -233.92656507, -0.00097456, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 87.5532355, 0.01841215, 87.5532355, 0.05523644, 61.28726485, -965.97659678, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 21.88830887, 9.119e-05, 65.66492662, 0.00027357, 218.88308875, 0.00091189, -21.88830887, -9.119e-05, -65.66492662, -0.00027357, -218.88308875, -0.00091189, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.35, 0.0, 3.4)
    ops.node(122003, 7.35, 0.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.14, 27146703.3221064, 11311126.384211, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 102.04540074, 0.00069862, 122.51053279, 0.01247132, 12.25105328, 0.03730827, -102.04540074, -0.00069862, -122.51053279, -0.01247132, -12.25105328, -0.03730827, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 131.25247241, 0.00063846, 157.57506176, 0.01289918, 15.75750618, 0.04024814, -131.25247241, -0.00063846, -157.57506176, -0.01289918, -15.75750618, -0.04024814, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 138.98036633, 0.01397236, 138.98036633, 0.04191709, 97.28625643, -1382.17369602, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 34.74509158, 8.294e-05, 104.23527475, 0.00024881, 347.45091583, 0.00082938, -34.74509158, -8.294e-05, -104.23527475, -0.00024881, -347.45091583, -0.00082938, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 144.23153499, 0.01276926, 144.23153499, 0.03830779, 100.9620745, -1490.41824639, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 36.05788375, 8.607e-05, 108.17365125, 0.00025821, 360.57883748, 0.00086071, -36.05788375, -8.607e-05, -108.17365125, -0.00025821, -360.57883748, -0.00086071, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 11.6, 0.0, 3.375)
    ops.node(122004, 11.6, 0.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.0625, 27411289.06153249, 11421370.4423052, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 41.18882593, 0.00093016, 49.0856587, 0.01172017, 4.90856587, 0.04067726, -41.18882593, -0.00093016, -49.0856587, -0.01172017, -4.90856587, -0.04067726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 41.18882593, 0.00093016, 49.0856587, 0.01172017, 4.90856587, 0.04067726, -41.18882593, -0.00093016, -49.0856587, -0.01172017, -4.90856587, -0.04067726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 73.71767011, 0.01860318, 73.71767011, 0.05580954, 51.60236908, -846.79146104, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 18.42941753, 9.759e-05, 55.28825258, 0.00029277, 184.29417528, 0.0009759, -18.42941753, -9.759e-05, -55.28825258, -0.00029277, -184.29417528, -0.0009759, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 73.71767011, 0.01860318, 73.71767011, 0.05580954, 51.60236908, -846.79146104, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 18.42941753, 9.759e-05, 55.28825258, 0.00029277, 184.29417528, 0.0009759, -18.42941753, -9.759e-05, -55.28825258, -0.00029277, -184.29417528, -0.0009759, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.4, 3.375)
    ops.node(122005, 0.0, 4.4, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.075, 29786223.56417813, 12410926.48507422, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 60.58401635, 0.00075696, 72.26523541, 0.0134299, 7.22652354, 0.0492942, -60.58401635, -0.00075696, -72.26523541, -0.0134299, -7.22652354, -0.0492942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 52.78580116, 0.00087802, 62.96344443, 0.0128109, 6.29634444, 0.04390473, -52.78580116, -0.00087802, -62.96344443, -0.0128109, -6.29634444, -0.04390473, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 96.07990899, 0.01513911, 96.07990899, 0.04541733, 67.2559363, -1051.65579545, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 24.01997725, 9.754e-05, 72.05993174, 0.00029263, 240.19977248, 0.00097544, -24.01997725, -9.754e-05, -72.05993174, -0.00029263, -240.19977248, -0.00097544, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 91.18757375, 0.01756036, 91.18757375, 0.05268108, 63.83130163, -952.09356201, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 22.79689344, 9.258e-05, 68.39068031, 0.00027773, 227.96893438, 0.00092577, -22.79689344, -9.258e-05, -68.39068031, -0.00027773, -227.96893438, -0.00092577, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 3.1, 4.4, 3.4)
    ops.node(122006, 3.1, 4.4, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.1925, 28056698.06312323, 11690290.85963468, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 234.50149276, 0.00051196, 282.20359088, 0.01127848, 28.22035909, 0.03401798, -234.50149276, -0.00051196, -282.20359088, -0.01127848, -28.22035909, -0.03401798, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 137.9329729, 0.00065406, 165.99118323, 0.01030497, 16.59911832, 0.02784737, -137.9329729, -0.00065406, -165.99118323, -0.01030497, -16.59911832, -0.02784737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 188.64087392, 0.01023921, 188.64087392, 0.03071762, 132.04861174, -1421.46228334, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 47.16021848, 7.922e-05, 141.48065544, 0.00023765, 471.60218479, 0.00079216, -47.16021848, -7.922e-05, -141.48065544, -0.00023765, -471.60218479, -0.00079216, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 155.230096, 0.01308125, 155.230096, 0.03924374, 108.6610672, -1213.78720658, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 38.807524, 6.519e-05, 116.422572, 0.00019556, 388.07524001, 0.00065186, -38.807524, -6.519e-05, -116.422572, -0.00019556, -388.07524001, -0.00065186, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 7.35, 4.4, 3.4)
    ops.node(122007, 7.35, 4.4, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.24, 27242382.07450357, 11350992.53104316, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 285.49843128, 0.00049813, 344.11323599, 0.01167178, 34.4113236, 0.03649156, -285.49843128, -0.00049813, -344.11323599, -0.01167178, -34.4113236, -0.03649156, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 169.53495414, 0.00059868, 204.34165407, 0.01065232, 20.43416541, 0.02997143, -169.53495414, -0.00059868, -204.34165407, -0.01065232, -20.43416541, -0.02997143, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 243.70350684, 0.00996269, 243.70350684, 0.02988807, 170.59245479, -1744.88769679, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 60.92587671, 8.454e-05, 182.77763013, 0.00025361, 609.2587671, 0.00084537, -60.92587671, -8.454e-05, -182.77763013, -0.00025361, -609.2587671, -0.00084537, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 193.46192251, 0.01197362, 193.46192251, 0.03592087, 135.42334576, -1486.01339503, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 48.36548063, 6.711e-05, 145.09644189, 0.00020133, 483.65480629, 0.00067109, -48.36548063, -6.711e-05, -145.09644189, -0.00020133, -483.65480629, -0.00067109, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 11.6, 4.4, 3.375)
    ops.node(122008, 11.6, 4.4, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.12, 28024539.16208893, 11676891.31753705, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 109.55756153, 0.00061481, 131.0853839, 0.01166054, 13.10853839, 0.04123978, -109.55756153, -0.00061481, -131.0853839, -0.01166054, -13.10853839, -0.04123978, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 88.29942818, 0.00074646, 105.65007363, 0.0108474, 10.56500736, 0.03477348, -88.29942818, -0.00074646, -105.65007363, -0.0108474, -10.56500736, -0.03477348, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 130.40678657, 0.01229622, 130.40678657, 0.03688865, 91.2847506, -1347.30815329, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 32.60169664, 8.795e-05, 97.80508993, 0.00026384, 326.01696643, 0.00087948, -32.60169664, -8.795e-05, -97.80508993, -0.00026384, -326.01696643, -0.00087948, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 121.72430437, 0.01492929, 121.72430437, 0.04478787, 85.20701306, -1180.23725268, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 30.43107609, 8.209e-05, 91.29322828, 0.00024628, 304.31076093, 0.00082092, -30.43107609, -8.209e-05, -91.29322828, -0.00024628, -304.31076093, -0.00082092, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.8, 3.375)
    ops.node(122009, 0.0, 8.8, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.105, 28680077.64586187, 11950032.35244245, 0.00152551, 0.00086625, 0.00117906, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 87.73163151, 0.0006368, 105.28691436, 0.01362112, 10.52869144, 0.04764984, -87.73163151, -0.0006368, -105.28691436, -0.01362112, -10.52869144, -0.04764984, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 67.50522231, 0.0007067, 81.0131584, 0.01307261, 8.10131584, 0.0433817, -67.50522231, -0.0007067, -81.0131584, -0.01307261, -8.10131584, -0.0433817, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 115.76086747, 0.01273597, 115.76086747, 0.03820791, 81.03260723, -1171.47594328, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 28.94021687, 8.718e-05, 86.8206506, 0.00026155, 289.40216867, 0.00087184, -28.94021687, -8.718e-05, -86.8206506, -0.00026155, -289.40216867, -0.00087184, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 110.92011666, 0.01413409, 110.92011666, 0.04240228, 77.64408166, -1070.06434544, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 27.73002916, 8.354e-05, 83.19008749, 0.00025061, 277.30029165, 0.00083538, -27.73002916, -8.354e-05, -83.19008749, -0.00025061, -277.30029165, -0.00083538, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 3.1, 8.8, 3.4)
    ops.node(122010, 3.1, 8.8, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.1925, 29209679.05183822, 12170699.60493259, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 241.32841762, 0.00051751, 290.30729849, 0.01187131, 29.03072985, 0.03648889, -241.32841762, -0.00051751, -290.30729849, -0.01187131, -29.03072985, -0.03648889, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 141.7348557, 0.00065492, 170.50069555, 0.01083225, 17.05006956, 0.02982349, -141.7348557, -0.00065492, -170.50069555, -0.01083225, -17.05006956, -0.02982349, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 195.67191817, 0.01035014, 195.67191817, 0.03105043, 136.97034272, -1410.42586917, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 48.91797954, 7.892e-05, 146.75393863, 0.00023677, 489.17979543, 0.00078925, -48.91797954, -7.892e-05, -146.75393863, -0.00023677, -489.17979543, -0.00078925, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 165.92061652, 0.01309831, 165.92061652, 0.03929494, 116.14443157, -1192.89365003, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 41.48015413, 6.692e-05, 124.44046239, 0.00020077, 414.80154131, 0.00066925, -41.48015413, -6.692e-05, -124.44046239, -0.00020077, -414.80154131, -0.00066925, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.35, 8.8, 3.4)
    ops.node(122011, 7.35, 8.8, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.24, 27916710.31017665, 11631962.62924027, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 289.1653132, 0.00049549, 348.46994995, 0.01143833, 34.846995, 0.0373561, -289.1653132, -0.00049549, -348.46994995, -0.01143833, -34.846995, -0.0373561, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 171.26337718, 0.00059099, 206.38761896, 0.01043696, 20.6387619, 0.03061071, -171.26337718, -0.00059099, -206.38761896, -0.01043696, -20.6387619, -0.03061071, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 248.6315651, 0.00990984, 248.6315651, 0.02972951, 174.04209557, -1725.89754812, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 62.15789127, 8.416e-05, 186.47367382, 0.00025249, 621.57891274, 0.00084164, -62.15789127, -8.416e-05, -186.47367382, -0.00025249, -621.57891274, -0.00084164, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 197.60539728, 0.01181976, 197.60539728, 0.03545929, 138.3237781, -1471.52929244, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 49.40134932, 6.689e-05, 148.20404796, 0.00020067, 494.0134932, 0.00066891, -49.40134932, -6.689e-05, -148.20404796, -0.00020067, -494.0134932, -0.00066891, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 11.6, 8.8, 3.375)
    ops.node(122012, 11.6, 8.8, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.12, 29991765.57221067, 12496568.98842111, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 110.15763226, 0.00061845, 131.7128469, 0.01235474, 13.17128469, 0.04635747, -110.15763226, -0.00061845, -131.7128469, -0.01235474, -13.17128469, -0.04635747, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 88.30529953, 0.0007549, 105.58453517, 0.01148733, 10.55845352, 0.03899149, -88.30529953, -0.0007549, -105.58453517, -0.01148733, -10.55845352, -0.03899149, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 138.22928122, 0.01236904, 138.22928122, 0.03710711, 96.76049686, -1350.08350015, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 34.55732031, 8.711e-05, 103.67196092, 0.00026133, 345.57320306, 0.00087108, -34.55732031, -8.711e-05, -103.67196092, -0.00026133, -345.57320306, -0.00087108, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 129.46691472, 0.01509803, 129.46691472, 0.04529408, 90.6268403, -1180.89924517, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 32.36672868, 8.159e-05, 97.10018604, 0.00024476, 323.6672868, 0.00081587, -32.36672868, -8.159e-05, -97.10018604, -0.00024476, -323.6672868, -0.00081587, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 13.2, 3.375)
    ops.node(122013, 0.0, 13.2, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.075, 29277024.7654951, 12198760.31895629, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 64.85366982, 0.00078611, 77.28463757, 0.011393, 7.72846376, 0.0447844, -64.85366982, -0.00078611, -77.28463757, -0.011393, -7.72846376, -0.0447844, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 50.94911, 0.00092185, 60.71489111, 0.01090932, 6.07148911, 0.03985918, -50.94911, -0.00092185, -60.71489111, -0.01090932, -6.07148911, -0.03985918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 89.92825861, 0.01572217, 89.92825861, 0.0471665, 62.94978102, -955.168164, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 22.48206465, 9.289e-05, 67.44619395, 0.00027866, 224.82064651, 0.00092886, -22.48206465, -9.289e-05, -67.44619395, -0.00027866, -224.82064651, -0.00092886, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 81.46647641, 0.01843691, 81.46647641, 0.05531072, 57.02653349, -881.21396527, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 20.3666191, 8.415e-05, 61.09985731, 0.00025244, 203.66619102, 0.00084146, -20.3666191, -8.415e-05, -61.09985731, -0.00025244, -203.66619102, -0.00084146, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 3.1, 13.2, 3.4)
    ops.node(122014, 3.1, 13.2, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.1925, 29374815.93712174, 12239506.64046739, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 234.29686395, 0.00050997, 281.78030891, 0.01263809, 28.17803089, 0.0426297, -234.29686395, -0.00050997, -281.78030891, -0.01263809, -28.17803089, -0.0426297, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 130.8696553, 0.00064429, 157.39217024, 0.01137133, 15.73921702, 0.03378614, -130.8696553, -0.00064429, -157.39217024, -0.01137133, -15.73921702, -0.03378614, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 204.92032847, 0.0101994, 204.92032847, 0.03059819, 143.44422993, -1568.56703803, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 51.23008212, 8.219e-05, 153.69024635, 0.00024657, 512.30082116, 0.00082191, -51.23008212, -8.219e-05, -153.69024635, -0.00024657, -512.30082116, -0.00082191, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 172.82527342, 0.01288582, 172.82527342, 0.03865745, 120.97769139, -1285.92046999, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 43.20631835, 6.932e-05, 129.61895506, 0.00020795, 432.06318355, 0.00069318, -43.20631835, -6.932e-05, -129.61895506, -0.00020795, -432.06318355, -0.00069318, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.35, 13.2, 3.4)
    ops.node(122015, 7.35, 13.2, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.24, 28849840.55794065, 12020766.89914194, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 285.44114851, 0.00048405, 343.69729856, 0.01317903, 34.36972986, 0.04035353, -285.44114851, -0.00048405, -343.69729856, -0.01317903, -34.36972986, -0.04035353, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 169.51180266, 0.00057367, 204.10774323, 0.01199616, 20.41077432, 0.03314812, -169.51180266, -0.00057367, -204.10774323, -0.01199616, -20.41077432, -0.03314812, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 263.5271934, 0.009681, 263.5271934, 0.02904301, 184.46903538, -1852.29955408, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 65.88179835, 8.632e-05, 197.64539505, 0.00025896, 658.81798349, 0.0008632, -65.88179835, -8.632e-05, -197.64539505, -0.00025896, -658.81798349, -0.0008632, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 208.85263231, 0.01147347, 208.85263231, 0.03442041, 146.19684262, -1550.27159517, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 52.21315808, 6.841e-05, 156.63947423, 0.00020523, 522.13158077, 0.00068411, -52.21315808, -6.841e-05, -156.63947423, -0.00020523, -522.13158077, -0.00068411, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 11.6, 13.2, 3.375)
    ops.node(122016, 11.6, 13.2, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.12, 30830255.90546865, 12845939.96061194, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 110.87322591, 0.00060053, 132.4336748, 0.01337867, 13.24336748, 0.04897164, -110.87322591, -0.00060053, -132.4336748, -0.01337867, -13.24336748, -0.04897164, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 89.53119411, 0.0007238, 106.94146353, 0.01240897, 10.69414635, 0.04119944, -89.53119411, -0.0007238, -106.94146353, -0.01240897, -10.69414635, -0.04119944, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 146.20904552, 0.01201055, 146.20904552, 0.03603165, 102.34633186, -1444.19428257, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 36.55226138, 8.963e-05, 109.65678414, 0.00026889, 365.5226138, 0.00089631, -36.55226138, -8.963e-05, -109.65678414, -0.00026889, -365.5226138, -0.00089631, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 136.30683037, 0.01447605, 136.30683037, 0.04342816, 95.41478126, -1247.3054175, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 34.07670759, 8.356e-05, 102.23012278, 0.00025068, 340.76707594, 0.00083561, -34.07670759, -8.356e-05, -102.23012278, -0.00025068, -340.76707594, -0.00083561, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 17.6, 3.375)
    ops.node(122017, 0.0, 17.6, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.105, 29709425.23400282, 12378927.18083451, 0.00152551, 0.00086625, 0.00117906, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 86.20520445, 0.00067844, 103.36197081, 0.01349329, 10.33619708, 0.04955524, -86.20520445, -0.00067844, -103.36197081, -0.01349329, -10.33619708, -0.04955524, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 67.46260777, 0.00076468, 80.88917763, 0.01296919, 8.08891776, 0.04508926, -67.46260777, -0.00076468, -80.88917763, -0.01296919, -8.08891776, -0.04508926, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 118.90118767, 0.01356887, 118.90118767, 0.04070661, 83.23083137, -1164.60743773, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 29.72529692, 8.645e-05, 89.17589075, 0.00025934, 297.25296917, 0.00086446, -29.72529692, -8.645e-05, -89.17589075, -0.00025934, -297.25296917, -0.00086446, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 114.11372986, 0.0152936, 114.11372986, 0.04588081, 79.8796109, -1064.70926646, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 28.52843247, 8.297e-05, 85.5852974, 0.0002489, 285.28432466, 0.00082965, -28.52843247, -8.297e-05, -85.5852974, -0.0002489, -285.28432466, -0.00082965, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 3.1, 17.6, 3.4)
    ops.node(122018, 3.1, 17.6, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.1925, 27667178.2657157, 11527990.94404821, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 224.65565405, 0.0005076, 270.56535726, 0.01242636, 27.05653573, 0.03979704, -224.65565405, -0.0005076, -270.56535726, -0.01242636, -27.05653573, -0.03979704, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 126.05499619, 0.00064862, 151.81507549, 0.01119049, 15.18150755, 0.03164649, -126.05499619, -0.00064862, -151.81507549, -0.01119049, -15.18150755, -0.03164649, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 193.12578783, 0.01015199, 193.12578783, 0.03045597, 135.18805148, -1560.00052558, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 48.28144696, 8.224e-05, 144.84434087, 0.00024672, 482.81446957, 0.00082241, -48.28144696, -8.224e-05, -144.84434087, -0.00024672, -482.81446957, -0.00082241, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 162.3814809, 0.01297238, 162.3814809, 0.03891713, 113.66703663, -1280.98257813, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 40.59537022, 6.915e-05, 121.78611067, 0.00020745, 405.95370225, 0.00069149, -40.59537022, -6.915e-05, -121.78611067, -0.00020745, -405.95370225, -0.00069149, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 7.35, 17.6, 3.4)
    ops.node(122019, 7.35, 17.6, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.24, 30293828.9700036, 12622428.7375015, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 290.65624165, 0.00049634, 349.28047211, 0.01248295, 34.92804721, 0.04143383, -290.65624165, -0.00049634, -349.28047211, -0.01248295, -34.92804721, -0.04143383, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 172.84260861, 0.00059471, 207.70428872, 0.01137983, 20.77042887, 0.03391448, -172.84260861, -0.00059471, -207.70428872, -0.01137983, -20.77042887, -0.03391448, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 274.33726655, 0.00992679, 274.33726655, 0.02978038, 192.03608658, -1804.18477119, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 68.58431664, 8.558e-05, 205.75294991, 0.00025673, 685.84316637, 0.00085578, -68.58431664, -8.558e-05, -205.75294991, -0.00025673, -685.84316637, -0.00085578, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 218.09497856, 0.01189419, 218.09497856, 0.03568256, 152.66648499, -1520.87411874, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 54.52374464, 6.803e-05, 163.57123392, 0.0002041, 545.23744639, 0.00068034, -54.52374464, -6.803e-05, -163.57123392, -0.0002041, -545.23744639, -0.00068034, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 11.6, 17.6, 3.375)
    ops.node(122020, 11.6, 17.6, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.12, 32711214.44554438, 13629672.68564349, 0.00194385, 0.00099, 0.00176, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 109.91208365, 0.00058131, 130.83999406, 0.01255172, 13.08399941, 0.05140315, -109.91208365, -0.00058131, -130.83999406, -0.01255172, -13.08399941, -0.05140315, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 88.58954559, 0.00069761, 105.45751871, 0.01164413, 10.54575187, 0.04307032, -88.58954559, -0.00069761, -105.45751871, -0.01164413, -10.54575187, -0.04307032, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 149.05816023, 0.01162619, 149.05816023, 0.03487858, 104.34071216, -1347.18707807, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 37.26454006, 8.612e-05, 111.79362017, 0.00025837, 372.64540057, 0.00086123, -37.26454006, -8.612e-05, -111.79362017, -0.00025837, -372.64540057, -0.00086123, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 140.35300886, 0.0139522, 140.35300886, 0.04185659, 98.2471062, -1179.46428274, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 35.08825222, 8.109e-05, 105.26475665, 0.00024328, 350.88252215, 0.00081094, -35.08825222, -8.109e-05, -105.26475665, -0.00024328, -350.88252215, -0.00081094, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 0.0, 22.0, 3.375)
    ops.node(122021, 0.0, 22.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.075, 29351725.96147385, 12229885.81728077, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 46.67962222, 0.0007141, 56.12488142, 0.01405244, 5.61248814, 0.05787325, -46.67962222, -0.0007141, -56.12488142, -0.01405244, -5.61248814, -0.05787325, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 40.81199891, 0.0008277, 49.06999008, 0.01338712, 4.90699901, 0.05137912, -40.81199891, -0.0008277, -49.06999008, -0.01338712, -4.90699901, -0.05137912, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 84.79711877, 0.01428209, 84.79711877, 0.04284627, 59.35798314, -864.72536649, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 21.19927969, 8.736e-05, 63.59783908, 0.00026209, 211.99279692, 0.00087363, -21.19927969, -8.736e-05, -63.59783908, -0.00026209, -211.99279692, -0.00087363, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 80.24593354, 0.01655396, 80.24593354, 0.04966188, 56.17215348, -760.98927291, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 20.06148338, 8.267e-05, 60.18445015, 0.00024802, 200.61483385, 0.00082674, -20.06148338, -8.267e-05, -60.18445015, -0.00024802, -200.61483385, -0.00082674, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 3.1, 22.0, 3.4)
    ops.node(122022, 3.1, 22.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.1225, 31588365.65630184, 13161819.0234591, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 98.12073216, 0.00063329, 117.37990413, 0.01367646, 11.73799041, 0.04936399, -98.12073216, -0.00063329, -117.37990413, -0.01367646, -11.73799041, -0.04936399, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 94.21722798, 0.00063329, 112.71021877, 0.01367646, 11.27102188, 0.04936399, -94.21722798, -0.00063329, -112.71021877, -0.01367646, -11.27102188, -0.04936399, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 140.00539073, 0.01266585, 140.00539073, 0.03799756, 98.00377351, -1232.11215288, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 35.00134768, 8.206e-05, 105.00404305, 0.00024618, 350.01347684, 0.00082059, -35.00134768, -8.206e-05, -105.00404305, -0.00024618, -350.01347684, -0.00082059, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 140.00539073, 0.01266585, 140.00539073, 0.03799756, 98.00377351, -1232.11215288, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 35.00134768, 8.206e-05, 105.00404305, 0.00024618, 350.01347684, 0.00082059, -35.00134768, -8.206e-05, -105.00404305, -0.00024618, -350.01347684, -0.00082059, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 7.35, 22.0, 3.4)
    ops.node(122023, 7.35, 22.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.14, 28641774.63244529, 11934072.76351887, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 109.22702183, 0.00063502, 131.10313459, 0.01258525, 13.11031346, 0.03690413, -109.22702183, -0.00063502, -131.10313459, -0.01258525, -13.11031346, -0.03690413, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 134.7149655, 0.0005872, 161.69583275, 0.01300489, 16.16958327, 0.03964118, -134.7149655, -0.0005872, -161.69583275, -0.01300489, -16.16958327, -0.03964118, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 135.92385364, 0.01270048, 135.92385364, 0.03810143, 95.14669755, -1194.85769058, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 33.98096341, 7.688e-05, 101.94289023, 0.00023064, 339.8096341, 0.0007688, -33.98096341, -7.688e-05, -101.94289023, -0.00023064, -339.8096341, -0.0007688, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 139.80378016, 0.01174408, 139.80378016, 0.03523225, 97.86264611, -1268.93180039, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 34.95094504, 7.907e-05, 104.85283512, 0.00023722, 349.50945039, 0.00079074, -34.95094504, -7.907e-05, -104.85283512, -0.00023722, -349.50945039, -0.00079074, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 11.6, 22.0, 3.375)
    ops.node(122024, 11.6, 22.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.075, 29651021.27614199, 12354592.1983925, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 55.24643662, 0.00077581, 66.11243258, 0.013856, 6.61124326, 0.05290173, -55.24643662, -0.00077581, -66.11243258, -0.013856, -6.61124326, -0.05290173, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 47.95420419, 0.00090799, 57.38594714, 0.01322433, 5.73859471, 0.04707641, -47.95420419, -0.00090799, -57.38594714, -0.01322433, -5.73859471, -0.04707641, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 91.05665175, 0.01551629, 91.05665175, 0.04654886, 63.73965622, -958.89343174, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 22.76416294, 9.287e-05, 68.29248881, 0.0002786, 227.64162937, 0.00092865, -22.76416294, -9.287e-05, -68.29248881, -0.0002786, -227.64162937, -0.00092865, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 86.39060761, 0.01815986, 86.39060761, 0.05447957, 60.47342533, -860.7952182, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 21.5976519, 8.811e-05, 64.79295571, 0.00026432, 215.97651902, 0.00088107, -21.5976519, -8.811e-05, -64.79295571, -0.00026432, -215.97651902, -0.00088107, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.35, 0.0, 6.525)
    ops.node(123003, 7.35, 0.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0875, 29031822.8264651, 12096592.84436046, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 49.56631085, 0.00086243, 59.4347555, 0.0113022, 5.94347555, 0.04170876, -49.56631085, -0.00086243, -59.4347555, -0.0113022, -5.94347555, -0.04170876, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 67.2157888, 0.00066159, 80.59817049, 0.01230328, 8.05981705, 0.05167897, -67.2157888, -0.00066159, -80.59817049, -0.01230328, -8.05981705, -0.05167897, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 86.10435492, 0.01724865, 86.10435492, 0.05174595, 60.27304844, -827.77738092, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 21.52608873, 7.688e-05, 64.57826619, 0.00023063, 215.26088729, 0.00076875, -21.52608873, -7.688e-05, -64.57826619, -0.00023063, -215.26088729, -0.00076875, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 98.31287512, 0.01323172, 98.31287512, 0.03969516, 68.81901259, -992.47389223, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 24.57821878, 8.778e-05, 73.73465634, 0.00026333, 245.78218781, 0.00087775, -24.57821878, -8.778e-05, -73.73465634, -0.00026333, -245.78218781, -0.00087775, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 11.6, 0.0, 6.525)
    ops.node(123004, 11.6, 0.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 29072619.35094796, 12113591.39622832, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 31.51131411, 0.00084523, 37.89609584, 0.01561644, 3.78960958, 0.05873369, -31.51131411, -0.00084523, -37.89609584, -0.01561644, -3.78960958, -0.05873369, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 31.51131411, 0.00084523, 37.89609584, 0.01561644, 3.78960958, 0.05873369, -31.51131411, -0.00084523, -37.89609584, -0.01561644, -3.78960958, -0.05873369, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 72.96179868, 0.01690467, 72.96179868, 0.05071401, 51.07325907, -788.13861658, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 18.24044967, 9.107e-05, 54.72134901, 0.00027321, 182.40449669, 0.0009107, -18.24044967, -9.107e-05, -54.72134901, -0.00027321, -182.40449669, -0.0009107, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 72.96179868, 0.01690467, 72.96179868, 0.05071401, 51.07325907, -788.13861658, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 18.24044967, 9.107e-05, 54.72134901, 0.00027321, 182.40449669, 0.0009107, -18.24044967, -9.107e-05, -54.72134901, -0.00027321, -182.40449669, -0.0009107, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.4, 6.525)
    ops.node(123005, 0.0, 4.4, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 30722261.99766035, 12800942.49902515, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 34.19163614, 0.0008534, 40.92736392, 0.01271603, 4.09273639, 0.05601406, -34.19163614, -0.0008534, -40.92736392, -0.01271603, -4.09273639, -0.05601406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 34.19163614, 0.0008534, 40.92736392, 0.01271603, 4.09273639, 0.05601406, -34.19163614, -0.0008534, -40.92736392, -0.01271603, -4.09273639, -0.05601406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 68.9531406, 0.01706809, 68.9531406, 0.05120427, 48.26719842, -702.18320539, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 17.23828515, 8.144e-05, 51.71485545, 0.00024433, 172.38285151, 0.00081445, -17.23828515, -8.144e-05, -51.71485545, -0.00024433, -172.38285151, -0.00081445, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 68.9531406, 0.01706809, 68.9531406, 0.05120427, 48.26719842, -702.18320539, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 17.23828515, 8.144e-05, 51.71485545, 0.00024433, 172.38285151, 0.00081445, -17.23828515, -8.144e-05, -51.71485545, -0.00024433, -172.38285151, -0.00081445, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 3.1, 4.4, 6.525)
    ops.node(123006, 3.1, 4.4, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.125, 29509492.97083487, 12295622.07118119, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 151.61857714, 0.00054024, 182.12399806, 0.01324599, 18.21239981, 0.04351585, -151.61857714, -0.00054024, -182.12399806, -0.01324599, -18.21239981, -0.04351585, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 70.8614231, 0.00088155, 85.11863075, 0.01146174, 8.51186308, 0.03106885, -70.8614231, -0.00088155, -85.11863075, -0.01146174, -8.51186308, -0.03106885, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 130.34392409, 0.01080484, 130.34392409, 0.03241453, 91.24074686, -1144.53758281, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 32.58598102, 8.014e-05, 97.75794307, 0.00024043, 325.85981023, 0.00080142, -32.58598102, -8.014e-05, -97.75794307, -0.00024043, -325.85981023, -0.00080142, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 97.87584421, 0.01763096, 97.87584421, 0.05289287, 68.51309094, -850.74874797, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 24.46896105, 6.018e-05, 73.40688315, 0.00018054, 244.68961052, 0.00060179, -24.46896105, -6.018e-05, -73.40688315, -0.00018054, -244.68961052, -0.00060179, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 7.35, 4.4, 6.525)
    ops.node(123007, 7.35, 4.4, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.175, 32469025.9492538, 13528760.81218908, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 172.73692113, 0.00052179, 206.73245636, 0.01281172, 20.67324564, 0.04753473, -172.73692113, -0.00052179, -206.73245636, -0.01281172, -20.67324564, -0.04753473, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 111.40380313, 0.00062988, 133.32865793, 0.01176598, 13.33286579, 0.03924829, -111.40380313, -0.00062988, -133.32865793, -0.01176598, -13.33286579, -0.03924829, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 187.100779, 0.01043581, 187.100779, 0.03130742, 130.9705453, -1370.6196995, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 46.77519475, 7.468e-05, 140.32558425, 0.00022404, 467.75194751, 0.00074681, -46.77519475, -7.468e-05, -140.32558425, -0.00022404, -467.75194751, -0.00074681, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 173.47539799, 0.01259753, 173.47539799, 0.0377926, 121.43277859, -1147.63781307, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 43.3688495, 6.924e-05, 130.10654849, 0.00020773, 433.68849498, 0.00069243, -43.3688495, -6.924e-05, -130.10654849, -0.00020773, -433.68849498, -0.00069243, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 11.6, 4.4, 6.525)
    ops.node(123008, 11.6, 4.4, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0875, 29547896.73788899, 12311623.64078708, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 69.64062735, 0.00065591, 83.45509376, 0.01398412, 8.34550938, 0.05434715, -69.64062735, -0.00065591, -83.45509376, -0.01398412, -8.34550938, -0.05434715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 51.83488546, 0.00083962, 62.11726389, 0.01279176, 6.21172639, 0.04396077, -51.83488546, -0.00083962, -62.11726389, -0.01279176, -6.21172639, -0.04396077, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 105.3177696, 0.01311825, 105.3177696, 0.03935476, 73.72243872, -1112.52384281, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 26.3294424, 9.239e-05, 78.9883272, 0.00027716, 263.29442399, 0.00092387, -26.3294424, -9.239e-05, -78.9883272, -0.00027716, -263.29442399, -0.00092387, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 95.68868872, 0.01679232, 95.68868872, 0.05037697, 66.9820821, -907.67435269, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 23.92217218, 8.394e-05, 71.76651654, 0.00025182, 239.2217218, 0.0008394, -23.92217218, -8.394e-05, -71.76651654, -0.00025182, -239.2217218, -0.0008394, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.8, 6.525)
    ops.node(123009, 0.0, 8.8, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 27001247.05718, 11250519.60715833, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 35.43146188, 0.00085479, 42.45743445, 0.01345789, 4.24574344, 0.0466115, -35.43146188, -0.00085479, -42.45743445, -0.01345789, -4.24574344, -0.0466115, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 35.43146188, 0.00085479, 42.45743445, 0.01345789, 4.24574344, 0.0466115, -35.43146188, -0.00085479, -42.45743445, -0.01345789, -4.24574344, -0.0466115, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 70.68387913, 0.01709576, 70.68387913, 0.05128729, 49.47871539, -803.84684324, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 17.67096978, 9.499e-05, 53.01290935, 0.00028498, 176.70969783, 0.00094995, -17.67096978, -9.499e-05, -53.01290935, -0.00028498, -176.70969783, -0.00094995, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 70.68387913, 0.01709576, 70.68387913, 0.05128729, 49.47871539, -803.84684324, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 17.67096978, 9.499e-05, 53.01290935, 0.00028498, 176.70969783, 0.00094995, -17.67096978, -9.499e-05, -53.01290935, -0.00028498, -176.70969783, -0.00094995, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 3.1, 8.8, 6.525)
    ops.node(123010, 3.1, 8.8, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.125, 28756295.38523661, 11981789.74384859, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 165.78538443, 0.00056546, 199.37592551, 0.01170094, 19.93759255, 0.0411744, -165.78538443, -0.00056546, -199.37592551, -0.01170094, -19.93759255, -0.0411744, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 80.98139693, 0.00094492, 97.38941112, 0.01021755, 9.73894111, 0.02930879, -80.98139693, -0.00094492, -97.38941112, -0.01021755, -9.73894111, -0.02930879, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 121.82989355, 0.01130916, 121.82989355, 0.03392748, 85.28092548, -1035.21168342, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 30.45747339, 7.687e-05, 91.37242016, 0.00023061, 304.57473387, 0.00076869, -30.45747339, -7.687e-05, -91.37242016, -0.00023061, -304.57473387, -0.00076869, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 94.17153817, 0.01889847, 94.17153817, 0.05669542, 65.92007672, -793.76894845, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 23.54288454, 5.942e-05, 70.62865363, 0.00017825, 235.42884542, 0.00059418, -23.54288454, -5.942e-05, -70.62865363, -0.00017825, -235.42884542, -0.00059418, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.35, 8.8, 6.525)
    ops.node(123011, 7.35, 8.8, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.175, 31241751.10258349, 13017396.29274312, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 168.34293699, 0.00052697, 202.0762382, 0.01265412, 20.20762382, 0.04618257, -168.34293699, -0.00052697, -202.0762382, -0.01265412, -20.20762382, -0.04618257, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 108.71578243, 0.00064322, 130.50073106, 0.01163182, 13.05007311, 0.03816867, -108.71578243, -0.00064322, -130.50073106, -0.01163182, -13.05007311, -0.03816867, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 177.76324349, 0.01053949, 177.76324349, 0.03161847, 124.43427044, -1324.92447933, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 44.44081087, 7.374e-05, 133.32243262, 0.00022122, 444.40810872, 0.00073741, -44.44081087, -7.374e-05, -133.32243262, -0.00022122, -444.40810872, -0.00073741, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 164.87343734, 0.01286433, 164.87343734, 0.038593, 115.41140613, -1116.87650088, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 41.21835933, 6.839e-05, 123.655078, 0.00020518, 412.18359334, 0.00068394, -41.21835933, -6.839e-05, -123.655078, -0.00020518, -412.18359334, -0.00068394, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 11.6, 8.8, 6.525)
    ops.node(123012, 11.6, 8.8, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0875, 28937022.7861094, 12057092.82754558, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 68.11037833, 0.00065312, 81.66648006, 0.01265538, 8.16664801, 0.05166713, -68.11037833, -0.00065312, -81.66648006, -0.01265538, -8.16664801, -0.05166713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 50.5009298, 0.00084118, 60.55219891, 0.01160427, 6.05521989, 0.04172979, -50.5009298, -0.00084118, -60.55219891, -0.01160427, -6.05521989, -0.04172979, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 101.72149287, 0.01306248, 101.72149287, 0.03918744, 71.20504501, -1071.36355399, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 25.43037322, 9.112e-05, 76.29111965, 0.00027335, 254.30373217, 0.00091116, -25.43037322, -9.112e-05, -76.29111965, -0.00027335, -254.30373217, -0.00091116, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 90.91344754, 0.01682355, 90.91344754, 0.05047065, 63.63941328, -880.2251012, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 22.72836189, 8.143e-05, 68.18508566, 0.0002443, 227.28361886, 0.00081435, -22.72836189, -8.143e-05, -68.18508566, -0.0002443, -227.28361886, -0.00081435, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 13.2, 6.525)
    ops.node(123013, 0.0, 13.2, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 26152220.18426416, 10896758.41011007, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 35.06072553, 0.00089084, 41.98112997, 0.01341229, 4.198113, 0.04404858, -35.06072553, -0.00089084, -41.98112997, -0.01341229, -4.198113, -0.04404858, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 35.06072553, 0.00089084, 41.98112997, 0.01341229, 4.198113, 0.04404858, -35.06072553, -0.00089084, -41.98112997, -0.01341229, -4.198113, -0.04404858, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 69.10965472, 0.01781682, 69.10965472, 0.05345047, 48.3767583, -805.39366167, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 17.27741368, 9.589e-05, 51.83224104, 0.00028768, 172.77413679, 0.00095894, -17.27741368, -9.589e-05, -51.83224104, -0.00028768, -172.77413679, -0.00095894, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 69.10965472, 0.01781682, 69.10965472, 0.05345047, 48.3767583, -805.39366167, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 17.27741368, 9.589e-05, 51.83224104, 0.00028768, 172.77413679, 0.00095894, -17.27741368, -9.589e-05, -51.83224104, -0.00028768, -172.77413679, -0.00095894, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 3.1, 13.2, 6.525)
    ops.node(123014, 3.1, 13.2, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.125, 28172494.4326057, 11738539.34691904, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 148.24206166, 0.0005404, 178.35237744, 0.01553241, 17.83523774, 0.05078899, -148.24206166, -0.0005404, -178.35237744, -0.01553241, -17.83523774, -0.05078899, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 79.21401204, 0.00086553, 95.30363526, 0.01311, 9.53036353, 0.03492153, -79.21401204, -0.00086553, -95.30363526, -0.01311, -9.53036353, -0.03492153, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 135.04079856, 0.01080807, 135.04079856, 0.03242421, 94.52855899, -1363.04919885, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 33.76019964, 8.697e-05, 101.28059892, 0.00026091, 337.6019964, 0.00086971, -33.76019964, -8.697e-05, -101.28059892, -0.00026091, -337.6019964, -0.00086971, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 108.94017688, 0.01731062, 108.94017688, 0.05193187, 76.25812381, -933.07648792, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 27.23504422, 7.016e-05, 81.70513266, 0.00021048, 272.3504422, 0.00070161, -27.23504422, -7.016e-05, -81.70513266, -0.00021048, -272.3504422, -0.00070161, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.35, 13.2, 6.525)
    ops.node(123015, 7.35, 13.2, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.175, 26829606.16751771, 11179002.56979905, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 170.94547189, 0.00053726, 206.30639523, 0.01204469, 20.63063952, 0.03949784, -170.94547189, -0.00053726, -206.30639523, -0.01204469, -20.63063952, -0.03949784, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 109.7192537, 0.00065275, 132.41522848, 0.01107981, 13.24152285, 0.03280823, -109.7192537, -0.00065275, -132.41522848, -0.01107981, -13.24152285, -0.03280823, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 153.83836593, 0.01074529, 153.83836593, 0.03223587, 107.68685615, -1330.86926127, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 38.45959148, 7.431e-05, 115.37877445, 0.00022293, 384.59591483, 0.00074311, -38.45959148, -7.431e-05, -115.37877445, -0.00022293, -384.59591483, -0.00074311, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 141.23934266, 0.013055, 141.23934266, 0.03916501, 98.86753986, -1120.69616773, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 35.30983566, 6.823e-05, 105.92950699, 0.00020468, 353.09835664, 0.00068225, -35.30983566, -6.823e-05, -105.92950699, -0.00020468, -353.09835664, -0.00068225, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 11.6, 13.2, 6.525)
    ops.node(123016, 11.6, 13.2, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0875, 34109029.68749252, 14212095.70312188, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 69.02122879, 0.00065612, 81.97434717, 0.0145347, 8.19743472, 0.06353017, -69.02122879, -0.00065612, -81.97434717, -0.0145347, -8.19743472, -0.06353017, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 50.7866208, 0.0008552, 60.31767556, 0.01330091, 6.03176756, 0.05113602, -50.7866208, -0.0008552, -60.31767556, -0.01330091, -6.03176756, -0.05113602, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 120.38986554, 0.01312232, 120.38986554, 0.03936695, 84.27290588, -1152.34801012, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 30.09746639, 9.149e-05, 90.29239916, 0.00027446, 300.97466385, 0.00091486, -30.09746639, -9.149e-05, -90.29239916, -0.00027446, -300.97466385, -0.00091486, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 110.23687902, 0.01710396, 110.23687902, 0.05131189, 77.16581531, -932.4553366, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 27.55921975, 8.377e-05, 82.67765926, 0.00025131, 275.59219754, 0.00083771, -27.55921975, -8.377e-05, -82.67765926, -0.00025131, -275.59219754, -0.00083771, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 17.6, 6.525)
    ops.node(123017, 0.0, 17.6, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 32875036.15571297, 13697931.73154707, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 36.34974938, 0.00082768, 43.29862943, 0.01252994, 4.32986294, 0.05902038, -36.34974938, -0.00082768, -43.29862943, -0.01252994, -4.32986294, -0.05902038, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 36.34974938, 0.00082768, 43.29862943, 0.01252994, 4.32986294, 0.05902038, -36.34974938, -0.00082768, -43.29862943, -0.01252994, -4.32986294, -0.05902038, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 74.80576971, 0.01655361, 74.80576971, 0.04966082, 52.36403879, -712.16314065, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 18.70144243, 8.257e-05, 56.10432728, 0.00024772, 187.01442426, 0.00082572, -18.70144243, -8.257e-05, -56.10432728, -0.00024772, -187.01442426, -0.00082572, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 74.80576971, 0.01655361, 74.80576971, 0.04966082, 52.36403879, -712.16314065, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 18.70144243, 8.257e-05, 56.10432728, 0.00024772, 187.01442426, 0.00082572, -18.70144243, -8.257e-05, -56.10432728, -0.00024772, -187.01442426, -0.00082572, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 3.1, 17.6, 6.525)
    ops.node(123018, 3.1, 17.6, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.125, 30873640.36597519, 12864016.81915633, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 147.47145736, 0.00052228, 176.84477466, 0.01395579, 17.68447747, 0.05415147, -147.47145736, -0.00052228, -176.84477466, -0.01395579, -17.68447747, -0.05415147, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 79.17750617, 0.00081866, 94.94805631, 0.01179025, 9.49480563, 0.03665737, -79.17750617, -0.00081866, -94.94805631, -0.01179025, -9.49480563, -0.03665737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 136.12474817, 0.01044569, 136.12474817, 0.03133706, 95.28732372, -1151.49391316, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 34.03118704, 8e-05, 102.09356113, 0.00024, 340.31187044, 0.00079999, -34.03118704, -8e-05, -102.09356113, -0.00024, -340.31187044, -0.00079999, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 105.27260917, 0.01637325, 105.27260917, 0.04911974, 73.69082642, -844.09931284, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 26.31815229, 6.187e-05, 78.95445687, 0.0001856, 263.18152292, 0.00061867, -26.31815229, -6.187e-05, -78.95445687, -0.0001856, -263.18152292, -0.00061867, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 7.35, 17.6, 6.525)
    ops.node(123019, 7.35, 17.6, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.175, 29809683.56008601, 12420701.48336917, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 167.5885853, 0.00051396, 201.71019965, 0.01325516, 20.17101997, 0.04511036, -167.5885853, -0.00051396, -201.71019965, -0.01325516, -20.17101997, -0.04511036, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 108.03282452, 0.00061896, 130.02868045, 0.01216396, 13.00286804, 0.03737648, -108.03282452, -0.00061896, -130.02868045, -0.01216396, -13.00286804, -0.03737648, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 172.4800528, 0.01027926, 172.4800528, 0.03083778, 120.73603696, -1382.10890473, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 43.1200132, 7.499e-05, 129.3600396, 0.00022496, 431.20013199, 0.00074987, -43.1200132, -7.499e-05, -129.3600396, -0.00022496, -431.20013199, -0.00074987, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 158.88153336, 0.01237924, 158.88153336, 0.03713771, 111.21707335, -1153.53641933, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 39.72038334, 6.908e-05, 119.16115002, 0.00020723, 397.20383341, 0.00069075, -39.72038334, -6.908e-05, -119.16115002, -0.00020723, -397.20383341, -0.00069075, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 11.6, 17.6, 6.525)
    ops.node(123020, 11.6, 17.6, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0875, 30651788.08610618, 12771578.36921091, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 69.27083479, 0.0006717, 82.90759916, 0.012834, 8.29075992, 0.05570309, -69.27083479, -0.0006717, -82.90759916, -0.012834, -8.29075992, -0.05570309, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 51.14114964, 0.00087411, 61.20887597, 0.01178073, 6.1208876, 0.04488496, -51.14114964, -0.00087411, -61.20887597, -0.01178073, -6.1208876, -0.04488496, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 103.76268828, 0.01343395, 103.76268828, 0.04030185, 72.6338818, -1010.26005803, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 25.94067207, 8.774e-05, 77.82201621, 0.00026323, 259.40672071, 0.00087745, -25.94067207, -8.774e-05, -77.82201621, -0.00026323, -259.40672071, -0.00087745, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 94.87755594, 0.01748226, 94.87755594, 0.05244678, 66.41428916, -840.54107176, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 23.71938898, 8.023e-05, 71.15816695, 0.00024069, 237.19388984, 0.00080231, -23.71938898, -8.023e-05, -71.15816695, -0.00024069, -237.19388984, -0.00080231, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 0.0, 22.0, 6.525)
    ops.node(123021, 0.0, 22.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 27713405.78159033, 11547252.40899597, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 26.89115096, 0.00080644, 32.51164061, 0.01533005, 3.25116406, 0.06079182, -26.89115096, -0.00080644, -32.51164061, -0.01533005, -3.25116406, -0.06079182, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 26.89115096, 0.00080644, 32.51164061, 0.01533005, 3.25116406, 0.06079182, -26.89115096, -0.00080644, -32.51164061, -0.01533005, -3.25116406, -0.06079182, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 64.70045452, 0.01612871, 64.70045452, 0.04838612, 45.29031817, -696.66994024, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 16.17511363, 8.472e-05, 48.52534089, 0.00025416, 161.75113631, 0.00084719, -16.17511363, -8.472e-05, -48.52534089, -0.00025416, -161.75113631, -0.00084719, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 64.70045452, 0.01612871, 64.70045452, 0.04838612, 45.29031817, -696.66994024, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 16.17511363, 8.472e-05, 48.52534089, 0.00025416, 161.75113631, 0.00084719, -16.17511363, -8.472e-05, -48.52534089, -0.00025416, -161.75113631, -0.00084719, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 3.1, 22.0, 6.525)
    ops.node(123022, 3.1, 22.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0625, 28408137.80361635, 11836724.08484015, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 43.51814203, 0.0008962, 52.02376891, 0.01287344, 5.20237689, 0.04709638, -43.51814203, -0.0008962, -52.02376891, -0.01287344, -5.20237689, -0.04709638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 41.10984114, 0.0008962, 49.14476527, 0.01287344, 4.91447653, 0.04709638, -41.10984114, -0.0008962, -49.14476527, -0.01287344, -4.91447653, -0.04709638, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 74.44570524, 0.01792404, 74.44570524, 0.05377212, 52.11199367, -819.53566514, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 18.61142631, 9.51e-05, 55.83427893, 0.00028529, 186.1142631, 0.00095095, -18.61142631, -9.51e-05, -55.83427893, -0.00028529, -186.1142631, -0.00095095, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 74.44570524, 0.01792404, 74.44570524, 0.05377212, 52.11199367, -819.53566514, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 18.61142631, 9.51e-05, 55.83427893, 0.00028529, 186.1142631, 0.00095095, -18.61142631, -9.51e-05, -55.83427893, -0.00028529, -186.1142631, -0.00095095, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 7.35, 22.0, 6.525)
    ops.node(123023, 7.35, 22.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.0875, 29458187.76720933, 12274244.90300389, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 62.63200362, 0.00080019, 75.07629782, 0.01475433, 7.50762978, 0.04211858, -62.63200362, -0.00080019, -75.07629782, -0.01475433, -7.50762978, -0.04211858, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 82.81947044, 0.00062816, 99.27479354, 0.01610944, 9.92747935, 0.05111792, -82.81947044, -0.00062816, -99.27479354, -0.01610944, -9.92747935, -0.05111792, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 93.18028279, 0.01600388, 93.18028279, 0.04801163, 65.22619795, -872.71560772, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 23.2950707, 8.199e-05, 69.88521209, 0.00024597, 232.95070697, 0.00081989, -23.2950707, -8.199e-05, -69.88521209, -0.00024597, -232.95070697, -0.00081989, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 102.712261, 0.01256329, 102.712261, 0.03768988, 71.8985827, -1061.61600634, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 25.67806525, 9.038e-05, 77.03419575, 0.00027113, 256.78065251, 0.00090376, -25.67806525, -9.038e-05, -77.03419575, -0.00027113, -256.78065251, -0.00090376, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 11.6, 22.0, 6.525)
    ops.node(123024, 11.6, 22.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 28711573.28921484, 11963155.53717285, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 36.69232668, 0.00083045, 44.14217918, 0.01547818, 4.41421792, 0.05779608, -36.69232668, -0.00083045, -44.14217918, -0.01547818, -4.41421792, -0.05779608, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 34.30981945, 0.00083045, 41.27593791, 0.01547818, 4.12759379, 0.05779608, -34.30981945, -0.00083045, -41.27593791, -0.01547818, -4.12759379, -0.05779608, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 72.06023162, 0.01660897, 72.06023162, 0.0498269, 50.44216214, -783.31462898, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 18.01505791, 9.108e-05, 54.04517372, 0.00027323, 180.15057906, 0.00091076, -18.01505791, -9.108e-05, -54.04517372, -0.00027323, -180.15057906, -0.00091076, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 72.06023162, 0.01660897, 72.06023162, 0.0498269, 50.44216214, -783.31462898, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 18.01505791, 9.108e-05, 54.04517372, 0.00027323, 180.15057906, 0.00091076, -18.01505791, -9.108e-05, -54.04517372, -0.00027323, -180.15057906, -0.00091076, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.35, 0.0, 9.675)
    ops.node(124003, 7.35, 0.0, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0875, 26524091.41939091, 11051704.75807955, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 30.03097071, 0.00073996, 36.5231235, 0.01448468, 3.65231235, 0.05304254, -30.03097071, -0.00073996, -36.5231235, -0.01448468, -3.65231235, -0.05304254, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 46.93180713, 0.00058716, 57.07761512, 0.01591432, 5.70776151, 0.06584573, -46.93180713, -0.00058716, -57.07761512, -0.01591432, -5.70776151, -0.06584573, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 72.74772401, 0.01479919, 72.74772401, 0.04439758, 50.92340681, -685.3440947, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 18.186931, 7.109e-05, 54.56079301, 0.00021327, 181.86931003, 0.00071091, -18.186931, -7.109e-05, -54.56079301, -0.00021327, -181.86931003, -0.00071091, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 81.97038549, 0.01174328, 81.97038549, 0.03522983, 57.37926984, -963.44093313, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 20.49259637, 8.01e-05, 61.47778911, 0.00024031, 204.92596371, 0.00080103, -20.49259637, -8.01e-05, -61.47778911, -0.00024031, -204.92596371, -0.00080103, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 11.6, 0.0, 9.675)
    ops.node(124004, 11.6, 0.0, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 33340524.8414375, 13891885.35059896, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 19.63828358, 0.00071739, 23.56040609, 0.01546359, 2.35604061, 0.07604159, -19.63828358, -0.00071739, -23.56040609, -0.01546359, -2.35604061, -0.07604159, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 19.63828358, 0.00071739, 23.56040609, 0.01546359, 2.35604061, 0.07604159, -19.63828358, -0.00071739, -23.56040609, -0.01546359, -2.35604061, -0.07604159, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 68.80413599, 0.01434785, 68.80413599, 0.04304355, 48.1628952, -710.80941803, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 17.201034, 7.489e-05, 51.603102, 0.00022466, 172.01033998, 0.00074887, -17.201034, -7.489e-05, -51.603102, -0.00022466, -172.01033998, -0.00074887, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 68.80413599, 0.01434785, 68.80413599, 0.04304355, 48.1628952, -710.80941803, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 17.201034, 7.489e-05, 51.603102, 0.00022466, 172.01033998, 0.00074887, -17.201034, -7.489e-05, -51.603102, -0.00022466, -172.01033998, -0.00074887, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.4, 9.675)
    ops.node(124005, 0.0, 4.4, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 29093011.75661206, 12122088.23192169, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 21.65377734, 0.00073318, 26.25271499, 0.01440313, 2.6252715, 0.06936759, -21.65377734, -0.00073318, -26.25271499, -0.01440313, -2.6252715, -0.06936759, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 21.65377734, 0.00073318, 26.25271499, 0.01440313, 2.6252715, 0.06936759, -21.65377734, -0.00073318, -26.25271499, -0.01440313, -2.6252715, -0.06936759, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 54.74189681, 0.01466357, 54.74189681, 0.04399071, 38.31932777, -596.30423128, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 13.6854742, 6.828e-05, 41.05642261, 0.00020484, 136.85474203, 0.0006828, -13.6854742, -6.828e-05, -41.05642261, -0.00020484, -136.85474203, -0.0006828, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 54.74189681, 0.01466357, 54.74189681, 0.04399071, 38.31932777, -596.30423128, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 13.6854742, 6.828e-05, 41.05642261, 0.00020484, 136.85474203, 0.0006828, -13.6854742, -6.828e-05, -41.05642261, -0.00020484, -136.85474203, -0.0006828, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 3.1, 4.4, 9.675)
    ops.node(124006, 3.1, 4.4, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.125, 29369354.30670407, 12237230.96112669, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 111.04337659, 0.00050251, 134.49963578, 0.01257798, 13.44996358, 0.05091476, -111.04337659, -0.00050251, -134.49963578, -0.01257798, -13.44996358, -0.05091476, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 51.03094981, 0.00078664, 61.81047779, 0.010842, 6.18104778, 0.03567441, -51.03094981, -0.00078664, -61.81047779, -0.010842, -6.18104778, -0.03567441, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 106.93960528, 0.01005015, 106.93960528, 0.03015045, 74.8577237, -762.83797207, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 26.73490132, 6.607e-05, 80.20470396, 0.0001982, 267.3490132, 0.00066066, -26.73490132, -6.607e-05, -80.20470396, -0.0001982, -267.3490132, -0.00066066, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 80.85201671, 0.01573283, 80.85201671, 0.04719848, 56.59641169, -487.03368424, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 20.21300418, 4.995e-05, 60.63901253, 0.00014985, 202.13004177, 0.00049949, -20.21300418, -4.995e-05, -60.63901253, -0.00014985, -202.13004177, -0.00049949, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 7.35, 4.4, 9.675)
    ops.node(124007, 7.35, 4.4, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.175, 28556396.76498147, 11898498.65207561, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 115.44521016, 0.00049477, 140.17775456, 0.0158832, 14.01777546, 0.05322612, -115.44521016, -0.00049477, -140.17775456, -0.0158832, -14.01777546, -0.05322612, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 72.69417996, 0.00059998, 88.26790563, 0.01454368, 8.82679056, 0.04409958, -72.69417996, -0.00059998, -88.26790563, -0.01454368, -8.82679056, -0.04409958, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 151.86923564, 0.00989547, 151.86923564, 0.0296864, 106.30846495, -1297.23396453, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 37.96730891, 6.892e-05, 113.90192673, 0.00020677, 379.67308909, 0.00068924, -37.96730891, -6.892e-05, -113.90192673, -0.00020677, -379.67308909, -0.00068924, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 137.024205, 0.01199961, 137.024205, 0.03599883, 95.9169435, -942.24589859, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 34.25605125, 6.219e-05, 102.76815375, 0.00018656, 342.5605125, 0.00062187, -34.25605125, -6.219e-05, -102.76815375, -0.00018656, -342.5605125, -0.00062187, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 11.6, 4.4, 9.675)
    ops.node(124008, 11.6, 4.4, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0875, 28238947.50153174, 11766228.12563823, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 44.82669463, 0.00060436, 54.3979724, 0.0166863, 5.43979724, 0.06951453, -44.82669463, -0.00060436, -54.3979724, -0.0166863, -5.43979724, -0.06951453, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 28.96291641, 0.00078418, 35.14700203, 0.01520576, 3.5147002, 0.05600059, -28.96291641, -0.00078418, -35.14700203, -0.01520576, -3.5147002, -0.05600059, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 88.40003715, 0.01208717, 88.40003715, 0.03626152, 61.88002601, -1036.62011694, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 22.10000929, 8.114e-05, 66.30002787, 0.00024342, 221.00009289, 0.00081141, -22.10000929, -8.114e-05, -66.30002787, -0.00024342, -221.00009289, -0.00081141, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 78.55536716, 0.01568359, 78.55536716, 0.04705078, 54.98875701, -728.7898762, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 19.63884179, 7.21e-05, 58.91652537, 0.00021631, 196.38841789, 0.00072104, -19.63884179, -7.21e-05, -58.91652537, -0.00021631, -196.38841789, -0.00072104, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.8, 9.675)
    ops.node(124009, 0.0, 8.8, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 28849828.05117931, 12020761.68799138, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 21.62706412, 0.00076578, 26.22623416, 0.01732645, 2.62262342, 0.07158227, -21.62706412, -0.00076578, -26.22623416, -0.01732645, -2.62262342, -0.07158227, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 21.62706412, 0.00076578, 26.22623416, 0.01732645, 2.62262342, 0.07158227, -21.62706412, -0.00076578, -26.22623416, -0.01732645, -2.62262342, -0.07158227, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 66.29473787, 0.01531561, 66.29473787, 0.04594682, 46.40631651, -831.51612984, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 16.57368447, 8.339e-05, 49.72105341, 0.00025016, 165.73684468, 0.00083387, -16.57368447, -8.339e-05, -49.72105341, -0.00025016, -165.73684468, -0.00083387, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 66.29473787, 0.01531561, 66.29473787, 0.04594682, 46.40631651, -831.51612984, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 16.57368447, 8.339e-05, 49.72105341, 0.00025016, 165.73684468, 0.00083387, -16.57368447, -8.339e-05, -49.72105341, -0.00025016, -165.73684468, -0.00083387, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 3.1, 8.8, 9.675)
    ops.node(124010, 3.1, 8.8, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.125, 31096026.82304648, 12956677.84293604, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 111.19271876, 0.00049344, 134.13376157, 0.01421104, 13.41337616, 0.05384286, -111.19271876, -0.00049344, -134.13376157, -0.01421104, -13.41337616, -0.05384286, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 51.3871533, 0.00076081, 61.98924035, 0.01218358, 6.19892404, 0.03785484, -51.3871533, -0.00076081, -61.98924035, -0.01218358, -6.19892404, -0.03785484, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 118.13407163, 0.00986881, 118.13407163, 0.02960643, 82.69385014, -875.59089454, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 29.53351791, 6.893e-05, 88.60055372, 0.00020679, 295.33517906, 0.00068929, -29.53351791, -6.893e-05, -88.60055372, -0.00020679, -295.33517906, -0.00068929, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 87.58106461, 0.0152161, 87.58106461, 0.0456483, 61.30674523, -533.66693072, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 21.89526615, 5.11e-05, 65.68579846, 0.00015331, 218.95266153, 0.00051102, -21.89526615, -5.11e-05, -65.68579846, -0.00015331, -218.95266153, -0.00051102, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.35, 8.8, 9.675)
    ops.node(124011, 7.35, 8.8, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.175, 30488544.4621688, 12703560.19257033, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 126.06914708, 0.00049373, 152.43963689, 0.01298904, 15.24396369, 0.05181893, -126.06914708, -0.00049373, -152.43963689, -0.01298904, -15.24396369, -0.05181893, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 79.06428301, 0.00058561, 95.60253934, 0.0119078, 9.56025393, 0.0426406, -79.06428301, -0.00058561, -95.60253934, -0.0119078, -9.56025393, -0.0426406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 152.10742645, 0.0098747, 152.10742645, 0.02962409, 106.47519852, -1024.51977637, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 38.02685661, 6.466e-05, 114.08056984, 0.00019397, 380.26856613, 0.00064657, -38.02685661, -6.466e-05, -114.08056984, -0.00019397, -380.26856613, -0.00064657, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 140.06869329, 0.01171228, 140.06869329, 0.03513685, 98.0480853, -776.96815647, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 35.01717332, 5.954e-05, 105.05151997, 0.00017862, 350.17173322, 0.0005954, -35.01717332, -5.954e-05, -105.05151997, -0.00017862, -350.17173322, -0.0005954, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 11.6, 8.8, 9.675)
    ops.node(124012, 11.6, 8.8, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0875, 28815020.79176477, 12006258.66323532, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 45.59228809, 0.00059872, 55.27445656, 0.01559696, 5.52744566, 0.06931225, -45.59228809, -0.00059872, -55.27445656, -0.01559696, -5.52744566, -0.06931225, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 29.36648686, 0.00076953, 35.60287649, 0.0142193, 3.56028765, 0.05569914, -29.36648686, -0.00076953, -35.60287649, -0.0142193, -3.56028765, -0.05569914, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 86.89030977, 0.01197435, 86.89030977, 0.03592305, 60.82321684, -939.80646002, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 21.72257744, 7.816e-05, 65.16773233, 0.00023448, 217.22577442, 0.00078161, -21.72257744, -7.816e-05, -65.16773233, -0.00023448, -217.22577442, -0.00078161, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 77.88283664, 0.01539061, 77.88283664, 0.04617182, 54.51798564, -670.01805225, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 19.47070916, 7.006e-05, 58.41212748, 0.00021017, 194.70709159, 0.00070058, -19.47070916, -7.006e-05, -58.41212748, -0.00021017, -194.70709159, -0.00070058, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 13.2, 9.675)
    ops.node(124013, 0.0, 13.2, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 25682464.47562659, 10701026.86484441, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 21.59237899, 0.00076713, 26.2928647, 0.01743632, 2.62928647, 0.06655305, -21.59237899, -0.00076713, -26.2928647, -0.01743632, -2.62928647, -0.06655305, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 21.59237899, 0.00076713, 26.2928647, 0.01743632, 2.62928647, 0.06655305, -21.59237899, -0.00076713, -26.2928647, -0.01743632, -2.62928647, -0.06655305, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 59.20166459, 0.01534268, 59.20166459, 0.04602805, 41.44116521, -779.03206124, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 14.80041615, 8.365e-05, 44.40124844, 0.00025095, 148.00416148, 0.00083649, -14.80041615, -8.365e-05, -44.40124844, -0.00025095, -148.00416148, -0.00083649, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 59.20166459, 0.01534268, 59.20166459, 0.04602805, 41.44116521, -779.03206124, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 14.80041615, 8.365e-05, 44.40124844, 0.00025095, 148.00416148, 0.00083649, -14.80041615, -8.365e-05, -44.40124844, -0.00025095, -148.00416148, -0.00083649, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 3.1, 13.2, 9.675)
    ops.node(124014, 3.1, 13.2, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.125, 30854831.70625789, 12856179.87760746, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 110.95290499, 0.0005003, 133.92699221, 0.01595616, 13.39269922, 0.06473426, -110.95290499, -0.0005003, -133.92699221, -0.01595616, -13.39269922, -0.06473426, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 47.71163284, 0.00077177, 57.59088039, 0.01339509, 5.75908804, 0.04357173, -47.71163284, -0.00077177, -57.59088039, -0.01339509, -5.75908804, -0.04357173, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 125.78979798, 0.01000592, 125.78979798, 0.03001775, 88.05285858, -1116.73390868, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 31.44744949, 7.397e-05, 94.34234848, 0.00022191, 314.47449494, 0.0007397, -31.44744949, -7.397e-05, -94.34234848, -0.00022191, -314.47449494, -0.0007397, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 96.68584074, 0.01543534, 96.68584074, 0.04630603, 67.68008852, -625.74142374, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 24.17146019, 5.686e-05, 72.51438056, 0.00017057, 241.71460186, 0.00056856, -24.17146019, -5.686e-05, -72.51438056, -0.00017057, -241.71460186, -0.00056856, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.35, 13.2, 9.675)
    ops.node(124015, 7.35, 13.2, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.175, 28288923.7208566, 11787051.55035692, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 118.45064845, 0.00049507, 143.90258714, 0.0135301, 14.39025871, 0.0506844, -118.45064845, -0.00049507, -143.90258714, -0.0135301, -14.39025871, -0.0506844, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 74.36962194, 0.00059573, 90.34970379, 0.01240698, 9.03497038, 0.04181359, -74.36962194, -0.00059573, -90.34970379, -0.01240698, -9.03497038, -0.04181359, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 139.73356451, 0.00990132, 139.73356451, 0.02970395, 97.81349515, -1004.82530729, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 34.93339113, 6.402e-05, 104.80017338, 0.00019205, 349.33391127, 0.00064016, -34.93339113, -6.402e-05, -104.80017338, -0.00019205, -349.33391127, -0.00064016, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 128.10493319, 0.01191459, 128.10493319, 0.03574377, 89.67345324, -764.95113044, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 32.0262333, 5.869e-05, 96.0786999, 0.00017607, 320.26233299, 0.00058689, -32.0262333, -5.869e-05, -96.0786999, -0.00017607, -320.26233299, -0.00058689, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 11.6, 13.2, 9.675)
    ops.node(124016, 11.6, 13.2, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0875, 29721660.9941299, 12384025.41422079, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 46.71454729, 0.00058778, 56.53332876, 0.01419616, 5.65333288, 0.06908436, -46.71454729, -0.00058778, -56.53332876, -0.01419616, -5.65333288, -0.06908436, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 30.00374128, 0.00074494, 36.31013182, 0.01294833, 3.63101318, 0.05533391, -30.00374128, -0.00074494, -36.31013182, -0.01294833, -3.63101318, -0.05533391, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 85.62801001, 0.01175558, 85.62801001, 0.03526675, 59.93960701, -825.69338045, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 21.4070025, 7.468e-05, 64.22100751, 0.00022403, 214.07002503, 0.00074675, -21.4070025, -7.468e-05, -64.22100751, -0.00022403, -214.07002503, -0.00074675, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 73.08148769, 0.01489874, 73.08148769, 0.04469621, 51.15704138, -600.85241727, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 18.27037192, 6.373e-05, 54.81111577, 0.0001912, 182.70371923, 0.00063734, -18.27037192, -6.373e-05, -54.81111577, -0.0001912, -182.70371923, -0.00063734, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 17.6, 9.675)
    ops.node(124017, 0.0, 17.6, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 26109851.63553866, 10879104.84814111, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 21.16546822, 0.0007694, 25.76432418, 0.01468234, 2.57643242, 0.06462, -21.16546822, -0.0007694, -25.76432418, -0.01468234, -2.57643242, -0.06462, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 21.16546822, 0.0007694, 25.76432418, 0.01468234, 2.57643242, 0.06462, -21.16546822, -0.0007694, -25.76432418, -0.01468234, -2.57643242, -0.06462, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 50.62592053, 0.01538792, 50.62592053, 0.04616375, 35.43814437, -590.01803327, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 12.65648013, 7.036e-05, 37.9694404, 0.00021108, 126.56480133, 0.00070361, -12.65648013, -7.036e-05, -37.9694404, -0.00021108, -126.56480133, -0.00070361, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 50.62592053, 0.01538792, 50.62592053, 0.04616375, 35.43814437, -590.01803327, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 12.65648013, 7.036e-05, 37.9694404, 0.00021108, 126.56480133, 0.00070361, -12.65648013, -7.036e-05, -37.9694404, -0.00021108, -126.56480133, -0.00070361, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 3.1, 17.6, 9.675)
    ops.node(124018, 3.1, 17.6, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.125, 30098005.68731456, 12540835.70304773, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 109.96075456, 0.00049972, 132.96991505, 0.01540463, 13.29699151, 0.06345634, -109.96075456, -0.00049972, -132.96991505, -0.01540463, -13.29699151, -0.06345634, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 47.25093467, 0.00077267, 57.138138, 0.01294601, 5.7138138, 0.04267327, -47.25093467, -0.00077267, -57.138138, -0.01294601, -5.7138138, -0.04267327, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 120.79077391, 0.00999438, 120.79077391, 0.02998313, 84.55354174, -1056.14866072, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 30.19769348, 7.282e-05, 90.59308043, 0.00021845, 301.97693478, 0.00072816, -30.19769348, -7.282e-05, -90.59308043, -0.00021845, -301.97693478, -0.00072816, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 89.41585339, 0.01545349, 89.41585339, 0.04636047, 62.59109737, -602.96079843, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 22.35396335, 5.39e-05, 67.06189004, 0.00016171, 223.53963347, 0.00053903, -22.35396335, -5.39e-05, -67.06189004, -0.00016171, -223.53963347, -0.00053903, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 7.35, 17.6, 9.675)
    ops.node(124019, 7.35, 17.6, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.175, 28852692.34581239, 12021955.1440885, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 118.14197564, 0.00048717, 143.37610979, 0.01543443, 14.33761098, 0.05306408, -118.14197564, -0.00048717, -143.37610979, -0.01543443, -14.33761098, -0.05306408, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 74.21215399, 0.00058241, 90.06324704, 0.01412636, 9.0063247, 0.0439092, -74.21215399, -0.00058241, -90.06324704, -0.01412636, -9.0063247, -0.0439092, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 149.39653524, 0.00974332, 149.39653524, 0.02922996, 104.57757467, -1185.52389527, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 37.34913381, 6.711e-05, 112.04740143, 0.00020132, 373.49133811, 0.00067106, -37.34913381, -6.711e-05, -112.04740143, -0.00020132, -373.49133811, -0.00067106, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 135.70100291, 0.01164819, 135.70100291, 0.03494458, 94.99070204, -874.41272685, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 33.92525073, 6.095e-05, 101.77575218, 0.00018286, 339.25250727, 0.00060954, -33.92525073, -6.095e-05, -101.77575218, -0.00018286, -339.25250727, -0.00060954, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 11.6, 17.6, 9.675)
    ops.node(124020, 11.6, 17.6, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0875, 29338774.27776011, 12224489.28240005, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 46.11793494, 0.00061741, 55.85560426, 0.0143242, 5.58556043, 0.06873313, -46.11793494, -0.00061741, -55.85560426, -0.0143242, -5.58556043, -0.06873313, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 29.76802136, 0.00080224, 36.05345345, 0.01309389, 3.60534534, 0.05510937, -29.76802136, -0.00080224, -36.05345345, -0.01309389, -3.60534534, -0.05510937, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 85.31036047, 0.01234827, 85.31036047, 0.03704482, 59.71725233, -846.71969384, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 21.32759012, 7.537e-05, 63.98277035, 0.00022611, 213.27590117, 0.00075369, -21.32759012, -7.537e-05, -63.98277035, -0.00022611, -213.27590117, -0.00075369, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 73.56141882, 0.01604488, 73.56141882, 0.04813465, 51.49299317, -613.65109965, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 18.3903547, 6.499e-05, 55.17106411, 0.00019497, 183.90354704, 0.00064989, -18.3903547, -6.499e-05, -55.17106411, -0.00019497, -183.90354704, -0.00064989, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 0.0, 22.0, 9.675)
    ops.node(124021, 0.0, 22.0, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 28975582.9105846, 12073159.54607692, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 17.45466629, 0.00075529, 21.22876178, 0.01728628, 2.12287618, 0.07710629, -17.45466629, -0.00075529, -21.22876178, -0.01728628, -2.12287618, -0.07710629, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 17.45466629, 0.00075529, 21.22876178, 0.01728628, 2.12287618, 0.07710629, -17.45466629, -0.00075529, -21.22876178, -0.01728628, -2.12287618, -0.07710629, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 59.73559564, 0.01510589, 59.73559564, 0.04531767, 41.81491695, -848.89825275, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 14.93389891, 7.481e-05, 44.80169673, 0.00022443, 149.33898911, 0.00074811, -14.93389891, -7.481e-05, -44.80169673, -0.00022443, -149.33898911, -0.00074811, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 59.73559564, 0.01510589, 59.73559564, 0.04531767, 41.81491695, -848.89825275, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 14.93389891, 7.481e-05, 44.80169673, 0.00022443, 149.33898911, 0.00074811, -14.93389891, -7.481e-05, -44.80169673, -0.00022443, -149.33898911, -0.00074811, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 3.1, 22.0, 9.675)
    ops.node(124022, 3.1, 22.0, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0625, 28684934.03595847, 11952055.84831603, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 23.79092162, 0.00075461, 28.81161924, 0.01438523, 2.88116192, 0.06583637, -23.79092162, -0.00075461, -28.81161924, -0.01438523, -2.88116192, -0.06583637, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 23.79092162, 0.00075461, 28.81161924, 0.01438523, 2.88116192, 0.06583637, -23.79092162, -0.00075461, -28.81161924, -0.01438523, -2.88116192, -0.06583637, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 57.31214465, 0.01509225, 57.31214465, 0.04527675, 40.11850126, -587.61991254, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 14.32803616, 7.25e-05, 42.98410849, 0.00021751, 143.28036163, 0.00072503, -14.32803616, -7.25e-05, -42.98410849, -0.00021751, -143.28036163, -0.00072503, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 57.31214465, 0.01509225, 57.31214465, 0.04527675, 40.11850126, -587.61991254, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 14.32803616, 7.25e-05, 42.98410849, 0.00021751, 143.28036163, 0.00072503, -14.32803616, -7.25e-05, -42.98410849, -0.00021751, -143.28036163, -0.00072503, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 7.35, 22.0, 9.675)
    ops.node(124023, 7.35, 22.0, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.0875, 29578212.84340128, 12324255.3514172, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 34.77331034, 0.00084062, 42.09198062, 0.01606022, 4.20919806, 0.05305878, -34.77331034, -0.00084062, -42.09198062, -0.01606022, -4.20919806, -0.05305878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 50.99435402, 0.000638, 61.72703548, 0.01752323, 6.17270355, 0.06485739, -50.99435402, -0.000638, -61.72703548, -0.01752323, -6.17270355, -0.06485739, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 78.77320794, 0.01681233, 78.77320794, 0.050437, 55.14124556, -660.1151614, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 19.69330199, 6.903e-05, 59.07990596, 0.00020709, 196.93301986, 0.00069031, -19.69330199, -6.903e-05, -59.07990596, -0.00020709, -196.93301986, -0.00069031, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 88.45136484, 0.01276007, 88.45136484, 0.0382802, 61.91595539, -921.63399694, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 22.11284121, 7.751e-05, 66.33852363, 0.00023254, 221.12841209, 0.00077512, -22.11284121, -7.751e-05, -66.33852363, -0.00023254, -221.12841209, -0.00077512, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 11.6, 22.0, 9.675)
    ops.node(124024, 11.6, 22.0, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 32946150.86175956, 13727562.85906648, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 20.50893724, 0.00069458, 24.63770626, 0.01692287, 2.46377063, 0.07725643, -20.50893724, -0.00069458, -24.63770626, -0.01692287, -2.46377063, -0.07725643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 20.50893724, 0.00069458, 24.63770626, 0.01692287, 2.46377063, 0.07725643, -20.50893724, -0.00069458, -24.63770626, -0.01692287, -2.46377063, -0.07725643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 71.37880746, 0.01389159, 71.37880746, 0.04167476, 49.96516522, -847.53450554, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 17.84470187, 7.862e-05, 53.5341056, 0.00023586, 178.44701866, 0.00078619, -17.84470187, -7.862e-05, -53.5341056, -0.00023586, -178.44701866, -0.00078619, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 71.37880746, 0.01389159, 71.37880746, 0.04167476, 49.96516522, -847.53450554, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 17.84470187, 7.862e-05, 53.5341056, 0.00023586, 178.44701866, 0.00078619, -17.84470187, -7.862e-05, -53.5341056, -0.00023586, -178.44701866, -0.00078619, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124025, 0.0, 0.0, 1.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170001, 124025, 0.075, 27293166.79645327, 11372152.83185553, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 64.32901025, 0.00054413, 77.06575275, 0.02876539, 7.70657527, 0.10295276, -64.32901025, -0.00054413, -77.06575275, -0.02876539, -7.70657527, -0.10295276, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 47.21612623, 0.00059603, 56.56462451, 0.02691138, 5.65646245, 0.08976002, -47.21612623, -0.00059603, -56.56462451, -0.02691138, -5.65646245, -0.08976002, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 131.56795217, 0.01088259, 131.56795217, 0.03264778, 92.09756652, -3686.00037214, 0.05, 2, 0, 70001, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 32.89198804, 7.289e-05, 98.67596413, 0.00021866, 328.91988042, 0.00072887, -32.89198804, -7.289e-05, -98.67596413, -0.00021866, -328.91988042, -0.00072887, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 109.63996014, 0.01192051, 109.63996014, 0.03576152, 76.7479721, -3082.32974124, 0.05, 2, 0, 70001, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 27.40999003, 6.074e-05, 82.2299701, 0.00018222, 274.09990035, 0.00060739, -27.40999003, -6.074e-05, -82.2299701, -0.00018222, -274.09990035, -0.00060739, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 0.0, 0.0, 1.8)
    ops.node(121001, 0.0, 0.0, 2.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121001, 0.075, 28507066.29469013, 11877944.28945422, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 52.87080203, 0.00052381, 63.52896912, 0.03210917, 6.35289691, 0.12087059, -52.87080203, -0.00052381, -63.52896912, -0.03210917, -6.35289691, -0.12087059, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 40.75642091, 0.00057017, 48.97246318, 0.03002243, 4.89724632, 0.10521766, -40.75642091, -0.00057017, -48.97246318, -0.03002243, -4.89724632, -0.10521766, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 147.63650421, 0.0104761, 147.63650421, 0.03142831, 103.34555295, -4849.025079, 0.05, 2, 0, 74025, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 36.90912605, 7.831e-05, 110.72737816, 0.00023492, 369.09126053, 0.00078306, -36.90912605, -7.831e-05, -110.72737816, -0.00023492, -369.09126053, -0.00078306, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 123.03042018, 0.01140346, 123.03042018, 0.03421039, 86.12129412, -3916.83438858, 0.05, 2, 0, 74025, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 30.75760504, 6.525e-05, 92.27281513, 0.00019576, 307.57605044, 0.00065255, -30.75760504, -6.525e-05, -92.27281513, -0.00019576, -307.57605044, -0.00065255, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.1, 0.0, 0.0)
    ops.node(124026, 3.1, 0.0, 1.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170002, 124026, 0.1225, 26457465.97396301, 11023944.15581792, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 145.87637092, 0.00053171, 173.46727577, 0.01902447, 17.34672758, 0.0483319, -145.87637092, -0.00053171, -173.46727577, -0.01902447, -17.34672758, -0.0483319, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 127.94578116, 0.00053171, 152.14531294, 0.01902447, 15.21453129, 0.0483319, -127.94578116, -0.00053171, -152.14531294, -0.01902447, -15.21453129, -0.0483319, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 192.43066632, 0.0106342, 192.43066632, 0.03190259, 134.70146643, -3768.48231051, 0.05, 2, 0, 70002, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 48.10766658, 6.733e-05, 144.32299974, 0.00020199, 481.07666581, 0.00067329, -48.10766658, -6.733e-05, -144.32299974, -0.00020199, -481.07666581, -0.00067329, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 192.43066632, 0.0106342, 192.43066632, 0.03190259, 134.70146643, -3768.48231051, 0.05, 2, 0, 70002, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 48.10766658, 6.733e-05, 144.32299974, 0.00020199, 481.07666581, 0.00067329, -48.10766658, -6.733e-05, -144.32299974, -0.00020199, -481.07666581, -0.00067329, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 3.1, 0.0, 1.8)
    ops.node(121002, 3.1, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121002, 0.1225, 30497822.19991756, 12707425.91663232, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 119.85043087, 0.00051912, 142.96880163, 0.01693151, 14.29688016, 0.0519399, -119.85043087, -0.00051912, -142.96880163, -0.01693151, -14.29688016, -0.0519399, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 115.34151957, 0.00051912, 137.59015058, 0.01693151, 13.75901506, 0.0519399, -115.34151957, -0.00051912, -137.59015058, -0.01693151, -13.75901506, -0.0519399, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 201.4609032, 0.01038244, 201.4609032, 0.03114731, 141.02263224, -3222.41008363, 0.05, 2, 0, 74026, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 50.3652258, 6.115e-05, 151.0956774, 0.00018345, 503.65225799, 0.0006115, -50.3652258, -6.115e-05, -151.0956774, -0.00018345, -503.65225799, -0.0006115, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 201.4609032, 0.01038244, 201.4609032, 0.03114731, 141.02263224, -3222.41008363, 0.05, 2, 0, 74026, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 50.3652258, 6.115e-05, 151.0956774, 0.00018345, 503.65225799, 0.0006115, -50.3652258, -6.115e-05, -151.0956774, -0.00018345, -503.65225799, -0.0006115, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.375)
    ops.node(124027, 0.0, 0.0, 4.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171001, 124027, 0.075, 30074904.86349335, 12531210.3597889, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 49.63967018, 0.00052335, 59.66853489, 0.01484648, 5.96685349, 0.06111976, -49.63967018, -0.00052335, -59.66853489, -0.01484648, -5.96685349, -0.06111976, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 38.18149135, 0.00057063, 45.89542277, 0.01405733, 4.58954228, 0.05417559, -38.18149135, -0.00057063, -45.89542277, -0.01405733, -4.58954228, -0.05417559, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 99.88395208, 0.01046709, 99.88395208, 0.03140127, 69.91876645, -1778.11994706, 0.05, 2, 0, 71001, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 24.97098802, 5.022e-05, 74.91296406, 0.00015065, 249.70988019, 0.00050216, -24.97098802, -5.022e-05, -74.91296406, -0.00015065, -249.70988019, -0.00050216, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 83.23662673, 0.0114126, 83.23662673, 0.03423779, 58.26563871, -1550.43805316, 0.05, 2, 0, 71001, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 20.80915668, 4.185e-05, 62.42747005, 0.00012554, 208.09156682, 0.00041847, -20.80915668, -4.185e-05, -62.42747005, -0.00012554, -208.09156682, -0.00041847, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 0.0, 0.0, 4.95)
    ops.node(122001, 0.0, 0.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122001, 0.075, 27992140.07958784, 11663391.69982827, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 44.44327409, 0.00052061, 53.71230119, 0.01505096, 5.37123012, 0.0609459, -44.44327409, -0.00052061, -53.71230119, -0.01505096, -5.37123012, -0.0609459, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 33.9479155, 0.00056818, 41.02804529, 0.01425, 4.10280453, 0.05404025, -33.9479155, -0.00056818, -41.02804529, -0.01425, -4.10280453, -0.05404025, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 88.84875118, 0.01041216, 88.84875118, 0.03123648, 62.19412583, -1643.30523301, 0.05, 2, 0, 74027, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 22.2121878, 4.799e-05, 66.63656339, 0.00014398, 222.12187796, 0.00047992, -22.2121878, -4.799e-05, -66.63656339, -0.00014398, -222.12187796, -0.00047992, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 74.04062599, 0.01136365, 74.04062599, 0.03409096, 51.82843819, -1412.34962126, 0.05, 2, 0, 74027, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 18.5101565, 3.999e-05, 55.53046949, 0.00011998, 185.10156497, 0.00039993, -18.5101565, -3.999e-05, -55.53046949, -0.00011998, -185.10156497, -0.00039993, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.1, 0.0, 3.4)
    ops.node(124028, 3.1, 0.0, 4.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171002, 124028, 0.1225, 28983819.67279368, 12076591.5303307, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 104.39277453, 0.00051763, 125.20633095, 0.01733671, 12.5206331, 0.05345553, -104.39277453, -0.00051763, -125.20633095, -0.01733671, -12.5206331, -0.05345553, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 100.24608833, 0.00051763, 120.23288938, 0.01733671, 12.02328894, 0.05345553, -100.24608833, -0.00051763, -120.23288938, -0.01733671, -12.02328894, -0.05345553, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 177.1528898, 0.0103526, 177.1528898, 0.03105779, 124.00702286, -2720.89264774, 0.05, 2, 0, 71002, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 44.28822245, 5.658e-05, 132.86466735, 0.00016974, 442.88222451, 0.00056581, -44.28822245, -5.658e-05, -132.86466735, -0.00016974, -442.88222451, -0.00056581, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 177.1528898, 0.0103526, 177.1528898, 0.03105779, 124.00702286, -2720.89264774, 0.05, 2, 0, 71002, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 44.28822245, 5.658e-05, 132.86466735, 0.00016974, 442.88222451, 0.00056581, -44.28822245, -5.658e-05, -132.86466735, -0.00016974, -442.88222451, -0.00056581, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 3.1, 0.0, 4.95)
    ops.node(122002, 3.1, 0.0, 6.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122002, 0.1225, 30008327.53956894, 12503469.80815372, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 94.47497748, 0.00048258, 113.37754117, 0.01762947, 11.33775412, 0.05770586, -94.47497748, -0.00048258, -113.37754117, -0.01762947, -11.33775412, -0.05770586, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 90.6678807, 0.00048258, 108.80872005, 0.01762947, 10.88087201, 0.05770586, -90.6678807, -0.00048258, -108.80872005, -0.01762947, -10.88087201, -0.05770586, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 177.05288123, 0.00965168, 177.05288123, 0.02895503, 123.93701686, -2547.32108842, 0.05, 2, 0, 74028, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 44.26322031, 5.462e-05, 132.78966092, 0.00016385, 442.63220307, 0.00054618, -44.26322031, -5.462e-05, -132.78966092, -0.00016385, -442.63220307, -0.00054618, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 177.05288123, 0.00965168, 177.05288123, 0.02895503, 123.93701686, -2547.32108842, 0.05, 2, 0, 74028, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 44.26322031, 5.462e-05, 132.78966092, 0.00016385, 442.63220307, 0.00054618, -44.26322031, -5.462e-05, -132.78966092, -0.00016385, -442.63220307, -0.00054618, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.525)
    ops.node(124029, 0.0, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172001, 124029, 0.0625, 30094446.48642823, 12539352.70267843, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 27.11386438, 0.00053688, 32.68043127, 0.01435593, 3.26804313, 0.0646193, -27.11386438, -0.00053688, -32.68043127, -0.01435593, -3.26804313, -0.0646193, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 27.11386438, 0.00053688, 32.68043127, 0.01435593, 3.26804313, 0.0646193, -27.11386438, -0.00053688, -32.68043127, -0.01435593, -3.26804313, -0.0646193, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 68.49618807, 0.01073757, 68.49618807, 0.03221271, 47.94733165, -1327.00733623, 0.05, 2, 0, 72001, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 17.12404702, 4.13e-05, 51.37214105, 0.00012389, 171.24047017, 0.00041296, -17.12404702, -4.13e-05, -51.37214105, -0.00012389, -171.24047017, -0.00041296, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 68.49618807, 0.01073757, 68.49618807, 0.03221271, 47.94733165, -1327.00733623, 0.05, 2, 0, 72001, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 17.12404702, 4.13e-05, 51.37214105, 0.00012389, 171.24047017, 0.00041296, -17.12404702, -4.13e-05, -51.37214105, -0.00012389, -171.24047017, -0.00041296, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 0.0, 0.0, 8.075)
    ops.node(123001, 0.0, 0.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123001, 0.0625, 27721636.42604771, 11550681.84418655, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 22.49259844, 0.00055406, 27.31586464, 0.01406491, 2.73158646, 0.06605382, -22.49259844, -0.00055406, -27.31586464, -0.01406491, -2.73158646, -0.06605382, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 22.49259844, 0.00055406, 27.31586464, 0.01406491, 2.73158646, 0.06605382, -22.49259844, -0.00055406, -27.31586464, -0.01406491, -2.73158646, -0.06605382, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 54.6776164, 0.01108123, 54.6776164, 0.0332437, 38.27433148, -1188.81522014, 0.05, 2, 0, 74029, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 13.6694041, 3.579e-05, 41.0082123, 0.00010736, 136.694041, 0.00035787, -13.6694041, -3.579e-05, -41.0082123, -0.00010736, -136.694041, -0.00035787, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 54.6776164, 0.01108123, 54.6776164, 0.0332437, 38.27433148, -1188.81522014, 0.05, 2, 0, 74029, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 13.6694041, 3.579e-05, 41.0082123, 0.00010736, 136.694041, 0.00035787, -13.6694041, -3.579e-05, -41.0082123, -0.00010736, -136.694041, -0.00035787, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.1, 0.0, 6.525)
    ops.node(124030, 3.1, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172002, 124030, 0.0625, 31511334.20911921, 13129722.58713301, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 47.84096249, 0.00060704, 56.98383634, 0.0124896, 5.69838363, 0.04743642, -47.84096249, -0.00060704, -56.98383634, -0.0124896, -5.69838363, -0.04743642, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 47.84096249, 0.00060704, 56.98383634, 0.0124896, 5.69838363, 0.04743642, -47.84096249, -0.00060704, -56.98383634, -0.0124896, -5.69838363, -0.04743642, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 64.13264926, 0.01214078, 64.13264926, 0.03642234, 44.89285448, -1455.35888768, 0.05, 2, 0, 72002, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 16.03316232, 3.693e-05, 48.09948695, 0.00011078, 160.33162315, 0.00036927, -16.03316232, -3.693e-05, -48.09948695, -0.00011078, -160.33162315, -0.00036927, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 64.13264926, 0.01214078, 64.13264926, 0.03642234, 44.89285448, -1455.35888768, 0.05, 2, 0, 72002, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 16.03316232, 3.693e-05, 48.09948695, 0.00011078, 160.33162315, 0.00036927, -16.03316232, -3.693e-05, -48.09948695, -0.00011078, -160.33162315, -0.00036927, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 3.1, 0.0, 8.075)
    ops.node(123002, 3.1, 0.0, 9.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123002, 0.0625, 30731220.86119926, 12804675.35883303, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 43.83789116, 0.00060069, 52.42352383, 0.01469882, 5.24235238, 0.0512079, -43.83789116, -0.00060069, -52.42352383, -0.01469882, -5.24235238, -0.0512079, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 43.83789116, 0.00060069, 52.42352383, 0.01469882, 5.24235238, 0.0512079, -43.83789116, -0.00060069, -52.42352383, -0.01469882, -5.24235238, -0.0512079, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 73.21693289, 0.01201387, 73.21693289, 0.0360416, 51.25185302, -1473.17986643, 0.05, 2, 0, 74030, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 18.30423322, 4.323e-05, 54.91269967, 0.00012968, 183.04233223, 0.00043228, -18.30423322, -4.323e-05, -54.91269967, -0.00012968, -183.04233223, -0.00043228, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 73.21693289, 0.01201387, 73.21693289, 0.0360416, 51.25185302, -1473.17986643, 0.05, 2, 0, 74030, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 18.30423322, 4.323e-05, 54.91269967, 0.00012968, 183.04233223, 0.00043228, -18.30423322, -4.323e-05, -54.91269967, -0.00012968, -183.04233223, -0.00043228, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.675)
    ops.node(124031, 0.0, 0.0, 10.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173001, 124031, 0.0625, 27464014.03053401, 11443339.17938917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 18.96885398, 0.00050859, 23.12450611, 0.01666806, 2.31245061, 0.07384109, -18.96885398, -0.00050859, -23.12450611, -0.01666806, -2.31245061, -0.07384109, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 18.96885398, 0.00050859, 23.12450611, 0.01666806, 2.31245061, 0.07384109, -18.96885398, -0.00050859, -23.12450611, -0.01666806, -2.31245061, -0.07384109, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 58.32864567, 0.01017172, 58.32864567, 0.03051517, 40.83005197, -1598.18636445, 0.05, 2, 0, 73001, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 14.58216142, 3.853e-05, 43.74648425, 0.0001156, 145.82161418, 0.00038535, -14.58216142, -3.853e-05, -43.74648425, -0.0001156, -145.82161418, -0.00038535, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 58.32864567, 0.01017172, 58.32864567, 0.03051517, 40.83005197, -1598.18636445, 0.05, 2, 0, 73001, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 14.58216142, 3.853e-05, 43.74648425, 0.0001156, 145.82161418, 0.00038535, -14.58216142, -3.853e-05, -43.74648425, -0.0001156, -145.82161418, -0.00038535, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 0.0, 0.0, 11.225)
    ops.node(124001, 0.0, 0.0, 12.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124001, 0.0625, 31394325.75117134, 13080969.06298806, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 14.27488185, 0.00049229, 17.2903551, 0.01619809, 1.72903551, 0.08187466, -14.27488185, -0.00049229, -17.2903551, -0.01619809, -1.72903551, -0.08187466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 14.27488185, 0.00049229, 17.2903551, 0.01619809, 1.72903551, 0.08187466, -14.27488185, -0.00049229, -17.2903551, -0.01619809, -1.72903551, -0.08187466, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 59.01801526, 0.00984577, 59.01801526, 0.02953732, 41.31261068, -3835.13860794, 0.05, 2, 0, 74031, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 14.75450381, 3.411e-05, 44.26351144, 0.00010233, 147.54503814, 0.00034109, -14.75450381, -3.411e-05, -44.26351144, -0.00010233, -147.54503814, -0.00034109, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 59.01801526, 0.00984577, 59.01801526, 0.02953732, 41.31261068, -3835.13860794, 0.05, 2, 0, 74031, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 14.75450381, 3.411e-05, 44.26351144, 0.00010233, 147.54503814, 0.00034109, -14.75450381, -3.411e-05, -44.26351144, -0.00010233, -147.54503814, -0.00034109, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.1, 0.0, 9.675)
    ops.node(124032, 3.1, 0.0, 10.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173002, 124032, 0.0625, 30556854.34638626, 12732022.64432761, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 32.49407413, 0.00056512, 39.185484, 0.01619541, 3.9185484, 0.06233255, -32.49407413, -0.00056512, -39.185484, -0.01619541, -3.9185484, -0.06233255, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 32.49407413, 0.00056512, 39.185484, 0.01619541, 3.9185484, 0.06233255, -32.49407413, -0.00056512, -39.185484, -0.01619541, -3.9185484, -0.06233255, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 60.62512881, 0.01130231, 60.62512881, 0.03390692, 42.43759016, -1168.60261107, 0.05, 2, 0, 73002, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 15.1562822, 3.6e-05, 45.46884661, 0.00010799, 151.56282202, 0.00035998, -15.1562822, -3.6e-05, -45.46884661, -0.00010799, -151.56282202, -0.00035998, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 60.62512881, 0.01130231, 60.62512881, 0.03390692, 42.43759016, -1168.60261107, 0.05, 2, 0, 73002, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 15.1562822, 3.6e-05, 45.46884661, 0.00010799, 151.56282202, 0.00035998, -15.1562822, -3.6e-05, -45.46884661, -0.00010799, -151.56282202, -0.00035998, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 3.1, 0.0, 11.225)
    ops.node(124002, 3.1, 0.0, 12.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124002, 0.0625, 30862593.77642816, 12859414.07351173, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 29.17388704, 0.00052784, 35.25936685, 0.01589364, 3.52593669, 0.06658795, -29.17388704, -0.00052784, -35.25936685, -0.01589364, -3.52593669, -0.06658795, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 29.17388704, 0.00052784, 35.25936685, 0.01589364, 3.52593669, 0.06658795, -29.17388704, -0.00052784, -35.25936685, -0.01589364, -3.52593669, -0.06658795, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 51.32328966, 0.01055683, 51.32328966, 0.03167048, 35.92630276, -1109.72473667, 0.05, 2, 0, 74032, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 12.83082242, 3.017e-05, 38.49246725, 9.052e-05, 128.30822415, 0.00030173, -12.83082242, -3.017e-05, -38.49246725, -9.052e-05, -128.30822415, -0.00030173, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 51.32328966, 0.01055683, 51.32328966, 0.03167048, 35.92630276, -1109.72473667, 0.05, 2, 0, 74032, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 12.83082242, 3.017e-05, 38.49246725, 9.052e-05, 128.30822415, 0.00030173, -12.83082242, -3.017e-05, -38.49246725, -9.052e-05, -128.30822415, -0.00030173, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4081, '-orient', 0, 0, 1, 0, 1, 0)
