import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 26119670.70288791, 10883196.1262033, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 46.41648077, 0.00078574, 54.55300202, 0.00686474, 5.4553002, 0.02441472, -46.41648077, -0.00078574, -54.55300202, -0.00686474, -5.4553002, -0.02441472, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 48.49775059, 0.00078574, 56.99910553, 0.00686474, 5.69991055, 0.02441472, -48.49775059, -0.00078574, -56.99910553, -0.00686474, -5.69991055, -0.02441472, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 79.98768887, 0.01571483, 79.98768887, 0.04714448, 55.99138221, -1293.41756172, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 19.99692222, 0.00010407, 59.99076665, 0.00031221, 199.96922216, 0.00104071, -19.99692222, -0.00010407, -59.99076665, -0.00031221, -199.96922216, -0.00104071, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 79.98768887, 0.01571483, 79.98768887, 0.04714448, 55.99138221, -1293.41756172, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 19.99692222, 0.00010407, 59.99076665, 0.00031221, 199.96922216, 0.00104071, -19.99692222, -0.00010407, -59.99076665, -0.00031221, -199.96922216, -0.00104071, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.85, 0.0, 0.0)
    ops.node(121002, 3.85, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.1225, 29572314.77056647, 12321797.82106936, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 151.51543445, 0.00093741, 180.26945683, 0.00936591, 18.02694568, 0.03148439, -151.51543445, -0.00093741, -180.26945683, -0.00936591, -18.02694568, -0.03148439, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 157.66169877, 0.00093741, 187.5821358, 0.00936591, 18.75821358, 0.03148439, -157.66169877, -0.00093741, -187.5821358, -0.00936591, -18.75821358, -0.03148439, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 155.73431787, 0.01874821, 155.73431787, 0.05624464, 109.01402251, -1832.79344672, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 38.93357947, 9.131e-05, 116.8007384, 0.00027393, 389.33579468, 0.0009131, -38.93357947, -9.131e-05, -116.8007384, -0.00027393, -389.33579468, -0.0009131, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 155.73431787, 0.01874821, 155.73431787, 0.05624464, 109.01402251, -1832.79344672, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 38.93357947, 9.131e-05, 116.8007384, 0.00027393, 389.33579468, 0.0009131, -38.93357947, -9.131e-05, -116.8007384, -0.00027393, -389.33579468, -0.0009131, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 7.7, 0.0, 0.0)
    ops.node(121003, 7.7, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.1225, 29066308.54822284, 12110961.89509285, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 152.3935696, 0.00090263, 181.31174507, 0.0086919, 18.13117451, 0.02988921, -152.3935696, -0.00090263, -181.31174507, -0.0086919, -18.13117451, -0.02988921, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 159.15847578, 0.00090263, 189.3603586, 0.0086919, 18.93603586, 0.02988921, -159.15847578, -0.00090263, -189.3603586, -0.0086919, -18.93603586, -0.02988921, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 150.52437706, 0.01805258, 150.52437706, 0.05415774, 105.36706394, -1768.19281916, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 37.63109426, 8.979e-05, 112.89328279, 0.00026937, 376.31094264, 0.00089792, -37.63109426, -8.979e-05, -112.89328279, -0.00026937, -376.31094264, -0.00089792, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 150.52437706, 0.01805258, 150.52437706, 0.05415774, 105.36706394, -1768.19281916, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 37.63109426, 8.979e-05, 112.89328279, 0.00026937, 376.31094264, 0.00089792, -37.63109426, -8.979e-05, -112.89328279, -0.00026937, -376.31094264, -0.00089792, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 18.45, 0.0, 0.0)
    ops.node(121006, 18.45, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.1225, 28999916.03559846, 12083298.34816602, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 154.12024003, 0.00095675, 183.36348546, 0.00981647, 18.33634855, 0.03089073, -154.12024003, -0.00095675, -183.36348546, -0.00981647, -18.33634855, -0.03089073, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 160.60835414, 0.00095675, 191.08267417, 0.00981647, 19.10826742, 0.03089073, -160.60835414, -0.00095675, -191.08267417, -0.00981647, -19.10826742, -0.03089073, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 156.08119092, 0.01913503, 156.08119092, 0.0574051, 109.25683364, -1890.54541985, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 39.02029773, 9.332e-05, 117.06089319, 0.00027996, 390.20297729, 0.00093319, -39.02029773, -9.332e-05, -117.06089319, -0.00027996, -390.20297729, -0.00093319, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 156.08119092, 0.01913503, 156.08119092, 0.0574051, 109.25683364, -1890.54541985, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 39.02029773, 9.332e-05, 117.06089319, 0.00027996, 390.20297729, 0.00093319, -39.02029773, -9.332e-05, -117.06089319, -0.00027996, -390.20297729, -0.00093319, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 22.3, 0.0, 0.0)
    ops.node(121007, 22.3, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 28588677.97429515, 11911949.15595631, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 154.04928287, 0.00093829, 183.2510311, 0.0089188, 18.32510311, 0.02921975, -154.04928287, -0.00093829, -183.2510311, -0.0089188, -18.32510311, -0.02921975, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 160.79982289, 0.00093829, 191.28121077, 0.0089188, 19.12812108, 0.02921975, -160.79982289, -0.00093829, -191.28121077, -0.0089188, -19.12812108, -0.02921975, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 151.41742792, 0.0187657, 151.41742792, 0.0562971, 105.99219955, -1827.86938322, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 37.85435698, 9.183e-05, 113.56307094, 0.0002755, 378.54356981, 0.00091833, -37.85435698, -9.183e-05, -113.56307094, -0.0002755, -378.54356981, -0.00091833, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 151.41742792, 0.0187657, 151.41742792, 0.0562971, 105.99219955, -1827.86938322, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 37.85435698, 9.183e-05, 113.56307094, 0.0002755, 378.54356981, 0.00091833, -37.85435698, -9.183e-05, -113.56307094, -0.0002755, -378.54356981, -0.00091833, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 26.15, 0.0, 0.0)
    ops.node(121008, 26.15, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.0625, 27933934.44590719, 11639139.35246133, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 66.77584795, 0.00125528, 78.86003383, 0.00995822, 7.88600338, 0.0329139, -66.77584795, -0.00125528, -78.86003383, -0.00995822, -7.88600338, -0.0329139, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 71.55128762, 0.00125528, 84.49966771, 0.00995822, 8.44996677, 0.0329139, -71.55128762, -0.00125528, -84.49966771, -0.00995822, -8.44996677, -0.0329139, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 100.29643452, 0.02510566, 100.29643452, 0.07531699, 70.20750417, -1487.25292338, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 25.07410863, 0.00012202, 75.22232589, 0.00036606, 250.74108631, 0.00122019, -25.07410863, -0.00012202, -75.22232589, -0.00036606, -250.74108631, -0.00122019, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 100.29643452, 0.02510566, 100.29643452, 0.07531699, 70.20750417, -1487.25292338, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 25.07410863, 0.00012202, 75.22232589, 0.00036606, 250.74108631, 0.00122019, -25.07410863, -0.00012202, -75.22232589, -0.00036606, -250.74108631, -0.00122019, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 4.8, 0.0)
    ops.node(121009, 0.0, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.1225, 29891199.07830913, 12454666.28262881, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 189.79665473, 0.00096299, 225.47166493, 0.00903175, 22.54716649, 0.0337863, -189.79665473, -0.00096299, -225.47166493, -0.00903175, -22.54716649, -0.0337863, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 182.78778528, 0.00096299, 217.14537769, 0.00903175, 21.71453777, 0.0337863, -182.78778528, -0.00096299, -217.14537769, -0.00903175, -21.71453777, -0.0337863, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 167.7573871, 0.01925979, 167.7573871, 0.05777938, 117.43017097, -2066.64541358, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 41.93934677, 9.731e-05, 125.81804032, 0.00029193, 419.39346774, 0.0009731, -41.93934677, -9.731e-05, -125.81804032, -0.00029193, -419.39346774, -0.0009731, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 167.7573871, 0.01925979, 167.7573871, 0.05777938, 117.43017097, -2066.64541358, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 41.93934677, 9.731e-05, 125.81804032, 0.00029193, 419.39346774, 0.0009731, -41.93934677, -9.731e-05, -125.81804032, -0.00029193, -419.39346774, -0.0009731, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 3.85, 4.8, 0.0)
    ops.node(121010, 3.85, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.2025, 28440848.95627252, 11850353.73178022, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 384.96626815, 0.00074993, 459.79651574, 0.01081822, 45.97965157, 0.02995829, -384.96626815, -0.00074993, -459.79651574, -0.01081822, -45.97965157, -0.02995829, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 376.15951045, 0.00074993, 449.27788895, 0.01081822, 44.9277889, 0.02995829, -376.15951045, -0.00074993, -449.27788895, -0.01081822, -44.9277889, -0.02995829, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 231.07559875, 0.01499855, 231.07559875, 0.04499565, 161.75291913, -2610.63761049, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 57.76889969, 8.522e-05, 173.30669906, 0.00025566, 577.68899688, 0.0008522, -57.76889969, -8.522e-05, -173.30669906, -0.00025566, -577.68899688, -0.0008522, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 231.07559875, 0.01499855, 231.07559875, 0.04499565, 161.75291913, -2610.63761049, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 57.76889969, 8.522e-05, 173.30669906, 0.00025566, 577.68899688, 0.0008522, -57.76889969, -8.522e-05, -173.30669906, -0.00025566, -577.68899688, -0.0008522, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.7, 4.8, 0.0)
    ops.node(121011, 7.7, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 28275730.93428167, 11781554.55595069, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 396.37180025, 0.00080112, 473.40470831, 0.0104562, 47.34047083, 0.0293373, -396.37180025, -0.00080112, -473.40470831, -0.0104562, -47.34047083, -0.0293373, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 387.58473221, 0.00080112, 462.90991686, 0.0104562, 46.29099169, 0.0293373, -387.58473221, -0.00080112, -462.90991686, -0.0104562, -46.29099169, -0.0293373, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 231.70737964, 0.01602233, 231.70737964, 0.048067, 162.19516575, -2647.20221901, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 57.92684491, 8.595e-05, 173.78053473, 0.00025786, 579.2684491, 0.00085952, -57.92684491, -8.595e-05, -173.78053473, -0.00025786, -579.2684491, -0.00085952, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 231.70737964, 0.01602233, 231.70737964, 0.048067, 162.19516575, -2647.20221901, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 57.92684491, 8.595e-05, 173.78053473, 0.00025786, 579.2684491, 0.00085952, -57.92684491, -8.595e-05, -173.78053473, -0.00025786, -579.2684491, -0.00085952, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 11.55, 4.8, 0.0)
    ops.node(121012, 11.55, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 29899976.45938116, 12458323.52474215, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 294.44199342, 0.0008745, 350.49295969, 0.00848056, 35.04929597, 0.02955988, -294.44199342, -0.0008745, -350.49295969, -0.00848056, -35.04929597, -0.02955988, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 286.24703316, 0.0008745, 340.73797929, 0.00848056, 34.07379793, 0.02955988, -286.24703316, -0.0008745, -340.73797929, -0.00848056, -34.07379793, -0.02955988, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 194.312919, 0.0174899, 194.312919, 0.05246971, 136.0190433, -2164.92888482, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 48.57822975, 8.627e-05, 145.73468925, 0.00025881, 485.78229751, 0.00086271, -48.57822975, -8.627e-05, -145.73468925, -0.00025881, -485.78229751, -0.00086271, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 194.312919, 0.0174899, 194.312919, 0.05246971, 136.0190433, -2164.92888482, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 48.57822975, 8.627e-05, 145.73468925, 0.00025881, 485.78229751, 0.00086271, -48.57822975, -8.627e-05, -145.73468925, -0.00025881, -485.78229751, -0.00086271, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 14.6, 4.8, 0.0)
    ops.node(121013, 14.6, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.16, 29480732.14386581, 12283638.39327742, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 279.89705498, 0.00085374, 333.21709503, 0.00871431, 33.3217095, 0.02911848, -279.89705498, -0.00085374, -333.21709503, -0.00871431, -33.3217095, -0.02911848, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 272.52507127, 0.00085374, 324.44075761, 0.00871431, 32.44407576, 0.02911848, -272.52507127, -0.00085374, -324.44075761, -0.00871431, -32.44407576, -0.02911848, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 188.26989261, 0.01707471, 188.26989261, 0.05122414, 131.78892482, -2089.50770254, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 47.06747315, 8.478e-05, 141.20241945, 0.00025433, 470.67473151, 0.00084777, -47.06747315, -8.478e-05, -141.20241945, -0.00025433, -470.67473151, -0.00084777, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 188.26989261, 0.01707471, 188.26989261, 0.05122414, 131.78892482, -2089.50770254, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 47.06747315, 8.478e-05, 141.20241945, 0.00025433, 470.67473151, 0.00084777, -47.06747315, -8.478e-05, -141.20241945, -0.00025433, -470.67473151, -0.00084777, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 18.45, 4.8, 0.0)
    ops.node(121014, 18.45, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.2025, 27468781.31711004, 11445325.54879585, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 397.39442772, 0.00077825, 474.43337796, 0.00865882, 47.4433378, 0.02623161, -397.39442772, -0.00077825, -474.43337796, -0.00865882, -47.4433378, -0.02623161, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 388.07080693, 0.00077825, 463.30227847, 0.00865882, 46.33022785, 0.02623161, -388.07080693, -0.00077825, -463.30227847, -0.00865882, -46.33022785, -0.02623161, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 214.01429114, 0.01556499, 214.01429114, 0.04669497, 149.8100038, -2389.76119143, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 53.50357279, 8.172e-05, 160.51071836, 0.00024516, 535.03572785, 0.00081721, -53.50357279, -8.172e-05, -160.51071836, -0.00024516, -535.03572785, -0.00081721, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 214.01429114, 0.01556499, 214.01429114, 0.04669497, 149.8100038, -2389.76119143, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 53.50357279, 8.172e-05, 160.51071836, 0.00024516, 535.03572785, 0.00081721, -53.50357279, -8.172e-05, -160.51071836, -0.00024516, -535.03572785, -0.00081721, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 22.3, 4.8, 0.0)
    ops.node(121015, 22.3, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.2025, 29411701.51323947, 12254875.63051645, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 400.89613486, 0.00078791, 478.74649666, 0.00953113, 47.87464967, 0.03013262, -400.89613486, -0.00078791, -478.74649666, -0.00953113, -47.87464967, -0.03013262, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 391.86077926, 0.00078791, 467.95655765, 0.00953113, 46.79565577, 0.03013262, -391.86077926, -0.00078791, -467.95655765, -0.00953113, -46.79565577, -0.03013262, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 233.01201837, 0.01575816, 233.01201837, 0.04727449, 163.10841286, -2515.71700978, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 58.25300459, 8.31e-05, 174.75901377, 0.00024929, 582.53004591, 0.00083097, -58.25300459, -8.31e-05, -174.75901377, -0.00024929, -582.53004591, -0.00083097, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 233.01201837, 0.01575816, 233.01201837, 0.04727449, 163.10841286, -2515.71700978, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 58.25300459, 8.31e-05, 174.75901377, 0.00024929, 582.53004591, 0.00083097, -58.25300459, -8.31e-05, -174.75901377, -0.00024929, -582.53004591, -0.00083097, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 26.15, 4.8, 0.0)
    ops.node(121016, 26.15, 4.8, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1225, 27811112.37580542, 11587963.48991892, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 181.18397617, 0.00100397, 215.000272, 0.00942107, 21.5000272, 0.02968558, -181.18397617, -0.00100397, -215.000272, -0.00942107, -21.5000272, -0.02968558, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 175.22043642, 0.00100397, 207.92369329, 0.00942107, 20.79236933, 0.02968558, -175.22043642, -0.00100397, -207.92369329, -0.00942107, -20.79236933, -0.02968558, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 165.82507944, 0.0200794, 165.82507944, 0.06023821, 116.07755561, -2215.79633526, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 41.45626986, 0.00010338, 124.36880958, 0.00031015, 414.5626986, 0.00103383, -41.45626986, -0.00010338, -124.36880958, -0.00031015, -414.5626986, -0.00103383, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 165.82507944, 0.0200794, 165.82507944, 0.06023821, 116.07755561, -2215.79633526, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 41.45626986, 0.00010338, 124.36880958, 0.00031015, 414.5626986, 0.00103383, -41.45626986, -0.00010338, -124.36880958, -0.00031015, -414.5626986, -0.00103383, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 9.6, 0.0)
    ops.node(121017, 0.0, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.1225, 30777085.77421134, 12823785.73925472, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 173.14274897, 0.0008871, 205.64272494, 0.00869143, 20.56427249, 0.03533075, -173.14274897, -0.0008871, -205.64272494, -0.00869143, -20.56427249, -0.03533075, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 173.14274897, 0.0008871, 205.64272494, 0.00869143, 20.56427249, 0.03533075, -173.14274897, -0.0008871, -205.64272494, -0.00869143, -20.56427249, -0.03533075, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 170.56715856, 0.01774208, 170.56715856, 0.05322625, 119.39701099, -2045.2694737, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 42.64178964, 9.609e-05, 127.92536892, 0.00028828, 426.4178964, 0.00096092, -42.64178964, -9.609e-05, -127.92536892, -0.00028828, -426.4178964, -0.00096092, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 170.56715856, 0.01774208, 170.56715856, 0.05322625, 119.39701099, -2045.2694737, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 42.64178964, 9.609e-05, 127.92536892, 0.00028828, 426.4178964, 0.00096092, -42.64178964, -9.609e-05, -127.92536892, -0.00028828, -426.4178964, -0.00096092, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 3.85, 9.6, 0.0)
    ops.node(121018, 3.85, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.2025, 31267157.87698254, 13027982.44874272, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 382.49352891, 0.00076305, 456.03915479, 0.01046375, 45.60391548, 0.03368343, -382.49352891, -0.00076305, -456.03915479, -0.01046375, -45.60391548, -0.03368343, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 382.49352891, 0.00076305, 456.03915479, 0.01046375, 45.60391548, 0.03368343, -382.49352891, -0.00076305, -456.03915479, -0.01046375, -45.60391548, -0.03368343, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 250.27558619, 0.01526109, 250.27558619, 0.04578328, 175.19291033, -2613.02574282, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 62.56889655, 8.396e-05, 187.70668964, 0.00025187, 625.68896548, 0.00083958, -62.56889655, -8.396e-05, -187.70668964, -0.00025187, -625.68896548, -0.00083958, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 250.27558619, 0.01526109, 250.27558619, 0.04578328, 175.19291033, -2613.02574282, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 62.56889655, 8.396e-05, 187.70668964, 0.00025187, 625.68896548, 0.00083958, -62.56889655, -8.396e-05, -187.70668964, -0.00025187, -625.68896548, -0.00083958, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 7.7, 9.6, 0.0)
    ops.node(121019, 7.7, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.2025, 29326258.13271105, 12219274.22196294, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 388.34084676, 0.00078507, 463.86599578, 0.0104971, 46.38659958, 0.03110096, -388.34084676, -0.00078507, -463.86599578, -0.0104971, -46.38659958, -0.03110096, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 388.34084676, 0.00078507, 463.86599578, 0.0104971, 46.38659958, 0.03110096, -388.34084676, -0.00078507, -463.86599578, -0.0104971, -46.38659958, -0.03110096, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 236.6263214, 0.01570149, 236.6263214, 0.04710448, 165.63842498, -2602.54255293, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 59.15658035, 8.463e-05, 177.46974105, 0.0002539, 591.56580349, 0.00084632, -59.15658035, -8.463e-05, -177.46974105, -0.0002539, -591.56580349, -0.00084632, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 236.6263214, 0.01570149, 236.6263214, 0.04710448, 165.63842498, -2602.54255293, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 59.15658035, 8.463e-05, 177.46974105, 0.0002539, 591.56580349, 0.00084632, -59.15658035, -8.463e-05, -177.46974105, -0.0002539, -591.56580349, -0.00084632, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 11.55, 9.6, 0.0)
    ops.node(121020, 11.55, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.16, 31207483.07457853, 13003117.94774106, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 282.10108598, 0.00082766, 335.75708206, 0.01027239, 33.57570821, 0.03709874, -282.10108598, -0.00082766, -335.75708206, -0.01027239, -33.57570821, -0.03709874, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 282.10108598, 0.00082766, 335.75708206, 0.01027239, 33.57570821, 0.03709874, -282.10108598, -0.00082766, -335.75708206, -0.01027239, -33.57570821, -0.03709874, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 216.79150892, 0.01655314, 216.79150892, 0.04965941, 151.75405625, -2485.04066327, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 54.19787723, 9.222e-05, 162.59363169, 0.00027666, 541.97877231, 0.00092219, -54.19787723, -9.222e-05, -162.59363169, -0.00027666, -541.97877231, -0.00092219, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 216.79150892, 0.01655314, 216.79150892, 0.04965941, 151.75405625, -2485.04066327, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 54.19787723, 9.222e-05, 162.59363169, 0.00027666, 541.97877231, 0.00092219, -54.19787723, -9.222e-05, -162.59363169, -0.00027666, -541.97877231, -0.00092219, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 14.6, 9.6, 0.0)
    ops.node(121021, 14.6, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.16, 26974783.30074484, 11239493.04197701, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 298.4886401, 0.00084477, 355.22444003, 0.00842355, 35.522444, 0.02732609, -298.4886401, -0.00084477, -355.22444003, -0.00842355, -35.522444, -0.02732609, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 298.4886401, 0.00084477, 355.22444003, 0.00842355, 35.522444, 0.02732609, -298.4886401, -0.00084477, -355.22444003, -0.00842355, -35.522444, -0.02732609, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 187.7861903, 0.01689543, 187.7861903, 0.0506863, 131.45033321, -2346.59693399, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 46.94654757, 9.241e-05, 140.83964272, 0.00027724, 469.46547574, 0.00092415, -46.94654757, -9.241e-05, -140.83964272, -0.00027724, -469.46547574, -0.00092415, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 187.7861903, 0.01689543, 187.7861903, 0.0506863, 131.45033321, -2346.59693399, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 46.94654757, 9.241e-05, 140.83964272, 0.00027724, 469.46547574, 0.00092415, -46.94654757, -9.241e-05, -140.83964272, -0.00027724, -469.46547574, -0.00092415, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 18.45, 9.6, 0.0)
    ops.node(121022, 18.45, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.2025, 29374857.33694636, 12239523.89039432, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 381.3025106, 0.00077757, 455.44911786, 0.00936833, 45.54491179, 0.03004278, -381.3025106, -0.00077757, -455.44911786, -0.00936833, -45.54491179, -0.03004278, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 381.3025106, 0.00077757, 455.44911786, 0.00936833, 45.54491179, 0.03004278, -381.3025106, -0.00077757, -455.44911786, -0.00936833, -45.54491179, -0.03004278, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 231.79520472, 0.01555149, 231.79520472, 0.04665446, 162.2566433, -2494.26941925, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 57.94880118, 8.277e-05, 173.84640354, 0.0002483, 579.4880118, 0.00082767, -57.94880118, -8.277e-05, -173.84640354, -0.0002483, -579.4880118, -0.00082767, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 231.79520472, 0.01555149, 231.79520472, 0.04665446, 162.2566433, -2494.26941925, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 57.94880118, 8.277e-05, 173.84640354, 0.0002483, 579.4880118, 0.00082767, -57.94880118, -8.277e-05, -173.84640354, -0.0002483, -579.4880118, -0.00082767, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 22.3, 9.6, 0.0)
    ops.node(121023, 22.3, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.2025, 26806364.07744209, 11169318.36560087, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 384.53319235, 0.00078531, 458.89729131, 0.00822158, 45.88972913, 0.02480679, -384.53319235, -0.00078531, -458.89729131, -0.00822158, -45.88972913, -0.02480679, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 384.53319235, 0.00078531, 458.89729131, 0.00822158, 45.88972913, 0.02480679, -384.53319235, -0.00078531, -458.89729131, -0.00822158, -45.88972913, -0.02480679, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 211.70103263, 0.01570625, 211.70103263, 0.04711876, 148.19072284, -2427.9796003, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 52.92525816, 8.284e-05, 158.77577447, 0.00024851, 529.25258157, 0.00082835, -52.92525816, -8.284e-05, -158.77577447, -0.00024851, -529.25258157, -0.00082835, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 211.70103263, 0.01570625, 211.70103263, 0.04711876, 148.19072284, -2427.9796003, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 52.92525816, 8.284e-05, 158.77577447, 0.00024851, 529.25258157, 0.00082835, -52.92525816, -8.284e-05, -158.77577447, -0.00024851, -529.25258157, -0.00082835, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 26.15, 9.6, 0.0)
    ops.node(121024, 26.15, 9.6, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.1225, 29034381.50609666, 12097658.96087361, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 171.7652451, 0.0009406, 204.0739572, 0.00909101, 20.40739572, 0.03219963, -171.7652451, -0.0009406, -204.0739572, -0.00909101, -20.40739572, -0.03219963, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 171.7652451, 0.0009406, 204.0739572, 0.00909101, 20.40739572, 0.03219963, -171.7652451, -0.0009406, -204.0739572, -0.00909101, -20.40739572, -0.03219963, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 165.2779219, 0.01881191, 165.2779219, 0.05643572, 115.69454533, -2090.63075176, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 41.31948048, 9.87e-05, 123.95844143, 0.0002961, 413.19480475, 0.00098701, -41.31948048, -9.87e-05, -123.95844143, -0.0002961, -413.19480475, -0.00098701, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 165.2779219, 0.01881191, 165.2779219, 0.05643572, 115.69454533, -2090.63075176, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 41.31948048, 9.87e-05, 123.95844143, 0.0002961, 413.19480475, 0.00098701, -41.31948048, -9.87e-05, -123.95844143, -0.0002961, -413.19480475, -0.00098701, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170025, 0.0, 14.4, 0.0)
    ops.node(121025, 0.0, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 25, 170025, 121025, 0.0625, 27146703.3221064, 11311126.384211, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20025, 63.6746641, 0.00129364, 75.07069541, 0.00972592, 7.50706954, 0.0303521, -63.6746641, -0.00129364, -75.07069541, -0.00972592, -7.50706954, -0.0303521, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10025, 67.47119859, 0.00129364, 79.54670621, 0.00972592, 7.95467062, 0.0303521, -67.47119859, -0.00129364, -79.54670621, -0.00972592, -7.95467062, -0.0303521, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20025, 25, 0.0, 98.90781047, 0.02587279, 98.90781047, 0.07761837, 69.23546733, -1494.87456841, 0.05, 2, 0, 70025, 21025, 2, 3)
    ops.uniaxialMaterial('LimitState', 40025, 24.72695262, 0.00012382, 74.18085785, 0.00037146, 247.26952618, 0.00123819, -24.72695262, -0.00012382, -74.18085785, -0.00037146, -247.26952618, -0.00123819, 0.4, 0.3, 0.003, 0.0, 0.0, 20025, 2)
    ops.limitCurve('ThreePoint', 10025, 25, 0.0, 98.90781047, 0.02587279, 98.90781047, 0.07761837, 69.23546733, -1494.87456841, 0.05, 2, 0, 70025, 21025, 1, 3)
    ops.uniaxialMaterial('LimitState', 30025, 24.72695262, 0.00012382, 74.18085785, 0.00037146, 247.26952618, 0.00123819, -24.72695262, -0.00012382, -74.18085785, -0.00037146, -247.26952618, -0.00123819, 0.4, 0.3, 0.003, 0.0, 0.0, 10025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 25, 99999, 'P', 40025, 'Vy', 30025, 'Vz', 20025, 'My', 10025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170025, 70025, 170025, 25, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121025, 121025, 21025, 25, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170026, 3.85, 14.4, 0.0)
    ops.node(121026, 3.85, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 26, 170026, 121026, 0.1225, 27411289.06153249, 11421370.4423052, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20026, 153.22441264, 0.00096078, 182.06842857, 0.00955062, 18.20684286, 0.0275378, -153.22441264, -0.00096078, -182.06842857, -0.00955062, -18.20684286, -0.0275378, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10026, 159.81954043, 0.00096078, 189.90506852, 0.00955062, 18.99050685, 0.0275378, -159.81954043, -0.00096078, -189.90506852, -0.00955062, -18.99050685, -0.0275378, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20026, 26, 0.0, 151.52395045, 0.01921564, 151.52395045, 0.05764693, 106.06676531, -1932.66418623, 0.05, 2, 0, 70026, 21026, 2, 3)
    ops.uniaxialMaterial('LimitState', 40026, 37.88098761, 9.585e-05, 113.64296283, 0.00028754, 378.80987612, 0.00095845, -37.88098761, -9.585e-05, -113.64296283, -0.00028754, -378.80987612, -0.00095845, 0.4, 0.3, 0.003, 0.0, 0.0, 20026, 2)
    ops.limitCurve('ThreePoint', 10026, 26, 0.0, 151.52395045, 0.01921564, 151.52395045, 0.05764693, 106.06676531, -1932.66418623, 0.05, 2, 0, 70026, 21026, 1, 3)
    ops.uniaxialMaterial('LimitState', 30026, 37.88098761, 9.585e-05, 113.64296283, 0.00028754, 378.80987612, 0.00095845, -37.88098761, -9.585e-05, -113.64296283, -0.00028754, -378.80987612, -0.00095845, 0.4, 0.3, 0.003, 0.0, 0.0, 10026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 26, 99999, 'P', 40026, 'Vy', 30026, 'Vz', 20026, 'My', 10026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170026, 70026, 170026, 26, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121026, 121026, 21026, 26, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170027, 7.7, 14.4, 0.0)
    ops.node(121027, 7.7, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 27, 170027, 121027, 0.1225, 29786223.56417813, 12410926.48507422, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20027, 154.94088215, 0.00092263, 184.33711599, 0.00986571, 18.4337116, 0.03236461, -154.94088215, -0.00092263, -184.33711599, -0.00986571, -18.4337116, -0.03236461, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10027, 161.79699932, 0.00092263, 192.49401331, 0.00986571, 19.24940133, 0.03236461, -161.79699932, -0.00092263, -192.49401331, -0.00986571, -19.24940133, -0.03236461, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20027, 27, 0.0, 161.43045763, 0.01845257, 161.43045763, 0.0553577, 113.00132034, -1935.02218554, 0.05, 2, 0, 70027, 21027, 2, 3)
    ops.uniaxialMaterial('LimitState', 40027, 40.35761441, 9.397e-05, 121.07284322, 0.00028191, 403.57614408, 0.0009397, -40.35761441, -9.397e-05, -121.07284322, -0.00028191, -403.57614408, -0.0009397, 0.4, 0.3, 0.003, 0.0, 0.0, 20027, 2)
    ops.limitCurve('ThreePoint', 10027, 27, 0.0, 161.43045763, 0.01845257, 161.43045763, 0.0553577, 113.00132034, -1935.02218554, 0.05, 2, 0, 70027, 21027, 1, 3)
    ops.uniaxialMaterial('LimitState', 30027, 40.35761441, 9.397e-05, 121.07284322, 0.00028191, 403.57614408, 0.0009397, -40.35761441, -9.397e-05, -121.07284322, -0.00028191, -403.57614408, -0.0009397, 0.4, 0.3, 0.003, 0.0, 0.0, 10027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 27, 99999, 'P', 40027, 'Vy', 30027, 'Vz', 20027, 'My', 10027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170027, 70027, 170027, 27, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121027, 121027, 21027, 27, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170028, 11.55, 14.4, 0.0)
    ops.node(121028, 11.55, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 28, 170028, 121028, 0.09, 28056698.06312323, 11690290.85963468, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20028, 117.21070022, 0.00106125, 138.60064225, 0.00787414, 13.86006422, 0.02874754, -117.21070022, -0.00106125, -138.60064225, -0.00787414, -13.86006422, -0.02874754, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10028, 123.07171561, 0.00106125, 145.5312424, 0.00787414, 14.55312424, 0.02874754, -123.07171561, -0.00106125, -145.5312424, -0.00787414, -14.55312424, -0.02874754, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20028, 28, 0.0, 123.78402223, 0.02122499, 123.78402223, 0.06367497, 86.64881556, -1664.37264815, 0.05, 2, 0, 70028, 21028, 2, 3)
    ops.uniaxialMaterial('LimitState', 40028, 30.94600556, 0.00010412, 92.83801667, 0.00031236, 309.46005558, 0.00104121, -30.94600556, -0.00010412, -92.83801667, -0.00031236, -309.46005558, -0.00104121, 0.4, 0.3, 0.003, 0.0, 0.0, 20028, 2)
    ops.limitCurve('ThreePoint', 10028, 28, 0.0, 123.78402223, 0.02122499, 123.78402223, 0.06367497, 86.64881556, -1664.37264815, 0.05, 2, 0, 70028, 21028, 1, 3)
    ops.uniaxialMaterial('LimitState', 30028, 30.94600556, 0.00010412, 92.83801667, 0.00031236, 309.46005558, 0.00104121, -30.94600556, -0.00010412, -92.83801667, -0.00031236, -309.46005558, -0.00104121, 0.4, 0.3, 0.003, 0.0, 0.0, 10028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 28, 99999, 'P', 40028, 'Vy', 30028, 'Vz', 20028, 'My', 10028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170028, 70028, 170028, 28, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121028, 121028, 21028, 28, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170029, 14.6, 14.4, 0.0)
    ops.node(121029, 14.6, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 29, 170029, 121029, 0.09, 27242382.07450357, 11350992.53104316, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20029, 114.02810444, 0.00111398, 134.62769321, 0.00958585, 13.46276932, 0.02836936, -114.02810444, -0.00111398, -134.62769321, -0.00958585, -13.46276932, -0.02836936, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10029, 119.03803339, 0.00111398, 140.5426839, 0.00958585, 14.05426839, 0.02836936, -119.03803339, -0.00111398, -140.5426839, -0.00958585, -14.05426839, -0.02836936, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20029, 29, 0.0, 132.46006523, 0.02227963, 132.46006523, 0.06683888, 92.72204566, -1912.3534939, 0.05, 2, 0, 70029, 21029, 2, 3)
    ops.uniaxialMaterial('LimitState', 40029, 33.11501631, 0.00011475, 99.34504893, 0.00034425, 331.15016309, 0.0011475, -33.11501631, -0.00011475, -99.34504893, -0.00034425, -331.15016309, -0.0011475, 0.4, 0.3, 0.003, 0.0, 0.0, 20029, 2)
    ops.limitCurve('ThreePoint', 10029, 29, 0.0, 132.46006523, 0.02227963, 132.46006523, 0.06683888, 92.72204566, -1912.3534939, 0.05, 2, 0, 70029, 21029, 1, 3)
    ops.uniaxialMaterial('LimitState', 30029, 33.11501631, 0.00011475, 99.34504893, 0.00034425, 331.15016309, 0.0011475, -33.11501631, -0.00011475, -99.34504893, -0.00034425, -331.15016309, -0.0011475, 0.4, 0.3, 0.003, 0.0, 0.0, 10029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 29, 99999, 'P', 40029, 'Vy', 30029, 'Vz', 20029, 'My', 10029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170029, 70029, 170029, 29, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121029, 121029, 21029, 29, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170030, 18.45, 14.4, 0.0)
    ops.node(121030, 18.45, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 30, 170030, 121030, 0.1225, 28024539.16208893, 11676891.31753705, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20030, 149.01659952, 0.00090743, 177.19321506, 0.00871968, 17.71932151, 0.02792972, -149.01659952, -0.00090743, -177.19321506, -0.00871968, -17.71932151, -0.02792972, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10030, 155.3417889, 0.00090743, 184.71439489, 0.00871968, 18.47143949, 0.02792972, -155.3417889, -0.00090743, -184.71439489, -0.00871968, -18.47143949, -0.02792972, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20030, 30, 0.0, 149.28885732, 0.01814867, 149.28885732, 0.054446, 104.50220013, -1831.85661627, 0.05, 2, 0, 70030, 21030, 2, 3)
    ops.uniaxialMaterial('LimitState', 40030, 37.32221433, 9.236e-05, 111.96664299, 0.00027709, 373.22214331, 0.00092365, -37.32221433, -9.236e-05, -111.96664299, -0.00027709, -373.22214331, -0.00092365, 0.4, 0.3, 0.003, 0.0, 0.0, 20030, 2)
    ops.limitCurve('ThreePoint', 10030, 30, 0.0, 149.28885732, 0.01814867, 149.28885732, 0.054446, 104.50220013, -1831.85661627, 0.05, 2, 0, 70030, 21030, 1, 3)
    ops.uniaxialMaterial('LimitState', 30030, 37.32221433, 9.236e-05, 111.96664299, 0.00027709, 373.22214331, 0.00092365, -37.32221433, -9.236e-05, -111.96664299, -0.00027709, -373.22214331, -0.00092365, 0.4, 0.3, 0.003, 0.0, 0.0, 10030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 30, 99999, 'P', 40030, 'Vy', 30030, 'Vz', 20030, 'My', 10030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170030, 70030, 170030, 30, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121030, 121030, 21030, 30, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170031, 22.3, 14.4, 0.0)
    ops.node(121031, 22.3, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 31, 170031, 121031, 0.1225, 28680077.64586187, 11950032.35244245, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20031, 148.18284379, 0.00097007, 176.28028541, 0.00927338, 17.62802854, 0.02974784, -148.18284379, -0.00097007, -176.28028541, -0.00927338, -17.62802854, -0.02974784, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10031, 153.57008991, 0.00097007, 182.68902517, 0.00927338, 18.26890252, 0.02974784, -153.57008991, -0.00097007, -182.68902517, -0.00927338, -18.26890252, -0.02974784, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20031, 31, 0.0, 154.78339844, 0.01940139, 154.78339844, 0.05820416, 108.34837891, -1891.09087548, 0.05, 2, 0, 70031, 21031, 2, 3)
    ops.uniaxialMaterial('LimitState', 40031, 38.69584961, 9.358e-05, 116.08754883, 0.00028073, 386.9584961, 0.00093576, -38.69584961, -9.358e-05, -116.08754883, -0.00028073, -386.9584961, -0.00093576, 0.4, 0.3, 0.003, 0.0, 0.0, 20031, 2)
    ops.limitCurve('ThreePoint', 10031, 31, 0.0, 154.78339844, 0.01940139, 154.78339844, 0.05820416, 108.34837891, -1891.09087548, 0.05, 2, 0, 70031, 21031, 1, 3)
    ops.uniaxialMaterial('LimitState', 30031, 38.69584961, 9.358e-05, 116.08754883, 0.00028073, 386.9584961, 0.00093576, -38.69584961, -9.358e-05, -116.08754883, -0.00028073, -386.9584961, -0.00093576, 0.4, 0.3, 0.003, 0.0, 0.0, 10031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 31, 99999, 'P', 40031, 'Vy', 30031, 'Vz', 20031, 'My', 10031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170031, 70031, 170031, 31, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121031, 121031, 21031, 31, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170032, 26.15, 14.4, 0.0)
    ops.node(121032, 26.15, 14.4, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 32, 170032, 121032, 0.0625, 29209679.05183822, 12170699.60493259, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20032, 65.61931782, 0.00130798, 77.61911488, 0.0103213, 7.76191149, 0.03693958, -65.61931782, -0.00130798, -77.61911488, -0.0103213, -7.76191149, -0.03693958, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10032, 69.56321809, 0.00130798, 82.28423574, 0.0103213, 8.22842357, 0.03693958, -69.56321809, -0.00130798, -82.28423574, -0.0103213, -8.22842357, -0.03693958, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20032, 32, 0.0, 102.04838218, 0.02615953, 102.04838218, 0.07847859, 71.43386753, -1462.39360464, 0.05, 2, 0, 70032, 21032, 2, 3)
    ops.uniaxialMaterial('LimitState', 40032, 25.51209555, 0.00011873, 76.53628664, 0.00035618, 255.12095546, 0.00118728, -25.51209555, -0.00011873, -76.53628664, -0.00035618, -255.12095546, -0.00118728, 0.4, 0.3, 0.003, 0.0, 0.0, 20032, 2)
    ops.limitCurve('ThreePoint', 10032, 32, 0.0, 102.04838218, 0.02615953, 102.04838218, 0.07847859, 71.43386753, -1462.39360464, 0.05, 2, 0, 70032, 21032, 1, 3)
    ops.uniaxialMaterial('LimitState', 30032, 25.51209555, 0.00011873, 76.53628664, 0.00035618, 255.12095546, 0.00118728, -25.51209555, -0.00011873, -76.53628664, -0.00035618, -255.12095546, -0.00118728, 0.4, 0.3, 0.003, 0.0, 0.0, 10032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 32, 99999, 'P', 40032, 'Vy', 30032, 'Vz', 20032, 'My', 10032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170032, 70032, 170032, 32, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121032, 121032, 21032, 32, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.2)
    ops.node(122001, 0.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 27916710.31017665, 11631962.62924027, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 56.75971273, 0.00122018, 67.67002035, 0.00978061, 6.76700204, 0.04019683, -56.75971273, -0.00122018, -67.67002035, -0.00978061, -6.76700204, -0.04019683, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 61.04331333, 0.00122018, 72.77701131, 0.00978061, 7.27770113, 0.04019683, -61.04331333, -0.00122018, -72.77701131, -0.00978061, -7.27770113, -0.04019683, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 86.7165196, 0.02440359, 86.7165196, 0.07321077, 60.70156372, -1186.99694316, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 21.6791299, 0.00010556, 65.0373897, 0.00031669, 216.791299, 0.00105563, -21.6791299, -0.00010556, -65.0373897, -0.00031669, -216.791299, -0.00105563, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 86.7165196, 0.02440359, 86.7165196, 0.07321077, 60.70156372, -1186.99694316, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 21.6791299, 0.00010556, 65.0373897, 0.00031669, 216.791299, 0.00105563, -21.6791299, -0.00010556, -65.0373897, -0.00031669, -216.791299, -0.00105563, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.85, 0.0, 3.2)
    ops.node(122002, 3.85, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.1225, 29991765.57221067, 12496568.98842111, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 131.38779195, 0.00086526, 157.23076015, 0.00991522, 15.72307602, 0.03717499, -131.38779195, -0.00086526, -157.23076015, -0.00991522, -15.72307602, -0.03717499, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 137.8367856, 0.00086526, 164.94822125, 0.00991522, 16.49482213, 0.03717499, -137.8367856, -0.00086526, -164.94822125, -0.00991522, -16.49482213, -0.03717499, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 148.25833399, 0.01730526, 148.25833399, 0.05191579, 103.78083379, -1632.3398671, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 37.0645835, 8.571e-05, 111.19375049, 0.00025713, 370.64583496, 0.00085711, -37.0645835, -8.571e-05, -111.19375049, -0.00025713, -370.64583496, -0.00085711, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 148.25833399, 0.01730526, 148.25833399, 0.05191579, 103.78083379, -1632.3398671, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 37.0645835, 8.571e-05, 111.19375049, 0.00025713, 370.64583496, 0.00085711, -37.0645835, -8.571e-05, -111.19375049, -0.00025713, -370.64583496, -0.00085711, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.7, 0.0, 3.2)
    ops.node(122003, 7.7, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.1225, 29277024.7654951, 12198760.31895629, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 130.03276598, 0.00087108, 155.70512837, 0.01116482, 15.57051284, 0.03728657, -130.03276598, -0.00087108, -155.70512837, -0.01116482, -15.57051284, -0.03728657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 136.29041425, 0.00087108, 163.19822382, 0.01116482, 16.31982238, 0.03728657, -136.29041425, -0.00087108, -163.19822382, -0.01116482, -16.31982238, -0.03728657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 148.70454816, 0.01742165, 148.70454816, 0.05226495, 104.09318371, -1709.06066489, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 37.17613704, 8.807e-05, 111.52841112, 0.0002642, 371.7613704, 0.00088068, -37.17613704, -8.807e-05, -111.52841112, -0.0002642, -371.7613704, -0.00088068, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 148.70454816, 0.01742165, 148.70454816, 0.05226495, 104.09318371, -1709.06066489, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 37.17613704, 8.807e-05, 111.52841112, 0.0002642, 371.7613704, 0.00088068, -37.17613704, -8.807e-05, -111.52841112, -0.0002642, -371.7613704, -0.00088068, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 18.45, 0.0, 3.2)
    ops.node(122006, 18.45, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.1225, 29374815.93712174, 12239506.64046739, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 129.10259511, 0.00089709, 154.5807142, 0.00972088, 15.45807142, 0.03600251, -129.10259511, -0.00089709, -154.5807142, -0.00972088, -15.45807142, -0.03600251, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 134.91340848, 0.00089709, 161.53827908, 0.00972088, 16.15382791, 0.03600251, -134.91340848, -0.00089709, -161.53827908, -0.00972088, -16.15382791, -0.03600251, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 144.43679886, 0.01794175, 144.43679886, 0.05382524, 101.1057592, -1601.27690898, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 36.10919971, 8.526e-05, 108.32759914, 0.00025577, 361.09199715, 0.00085255, -36.10919971, -8.526e-05, -108.32759914, -0.00025577, -361.09199715, -0.00085255, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 144.43679886, 0.01794175, 144.43679886, 0.05382524, 101.1057592, -1601.27690898, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 36.10919971, 8.526e-05, 108.32759914, 0.00025577, 361.09199715, 0.00085255, -36.10919971, -8.526e-05, -108.32759914, -0.00025577, -361.09199715, -0.00085255, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 22.3, 0.0, 3.2)
    ops.node(122007, 22.3, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 28849840.55794065, 12020766.89914194, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 133.87679851, 0.00091809, 160.34641726, 0.01083106, 16.03464173, 0.03623868, -133.87679851, -0.00091809, -160.34641726, -0.01083106, -16.03464173, -0.03623868, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 140.36538399, 0.00091809, 168.11790153, 0.01083106, 16.81179015, 0.03623868, -140.36538399, -0.00091809, -168.11790153, -0.01083106, -16.81179015, -0.03623868, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 147.33440959, 0.0183618, 147.33440959, 0.05508539, 103.13408671, -1716.60317895, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 36.8336024, 8.855e-05, 110.50080719, 0.00026564, 368.33602398, 0.00088548, -36.8336024, -8.855e-05, -110.50080719, -0.00026564, -368.33602398, -0.00088548, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 147.33440959, 0.0183618, 147.33440959, 0.05508539, 103.13408671, -1716.60317895, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 36.8336024, 8.855e-05, 110.50080719, 0.00026564, 368.33602398, 0.00088548, -36.8336024, -8.855e-05, -110.50080719, -0.00026564, -368.33602398, -0.00088548, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 26.15, 0.0, 3.2)
    ops.node(122008, 26.15, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.0625, 30830255.90546865, 12845939.96061194, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 55.14955863, 0.00118612, 65.7025776, 0.01186268, 6.57025776, 0.04984898, -55.14955863, -0.00118612, -65.7025776, -0.01186268, -6.57025776, -0.04984898, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 58.81045169, 0.00118612, 70.06399257, 0.01186268, 7.00639926, 0.04984898, -58.81045169, -0.00118612, -70.06399257, -0.01186268, -7.00639926, -0.04984898, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 100.18556668, 0.02372249, 100.18556668, 0.07116748, 70.12989668, -1372.59776641, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 25.04639167, 0.00011043, 75.13917501, 0.0003313, 250.4639167, 0.00110434, -25.04639167, -0.00011043, -75.13917501, -0.0003313, -250.4639167, -0.00110434, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 100.18556668, 0.02372249, 100.18556668, 0.07116748, 70.12989668, -1372.59776641, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 25.04639167, 0.00011043, 75.13917501, 0.0003313, 250.4639167, 0.00110434, -25.04639167, -0.00011043, -75.13917501, -0.0003313, -250.4639167, -0.00110434, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 4.8, 3.2)
    ops.node(122009, 0.0, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.1225, 29709425.23400282, 12378927.18083451, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 119.31551947, 0.00087382, 142.67821467, 0.00952002, 14.26782147, 0.03916849, -119.31551947, -0.00087382, -142.67821467, -0.00952002, -14.26782147, -0.03916849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 131.49006707, 0.00087382, 157.23661181, 0.00952002, 15.72366118, 0.03916849, -131.49006707, -0.00087382, -157.23661181, -0.00952002, -15.72366118, -0.03916849, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 156.81066093, 0.01747632, 156.81066093, 0.05242895, 109.76746265, -1850.98558886, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 39.20266523, 9.152e-05, 117.6079957, 0.00027455, 392.02665232, 0.00091517, -39.20266523, -9.152e-05, -117.6079957, -0.00027455, -392.02665232, -0.00091517, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 156.81066093, 0.01747632, 156.81066093, 0.05242895, 109.76746265, -1850.98558886, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 39.20266523, 9.152e-05, 117.6079957, 0.00027455, 392.02665232, 0.00091517, -39.20266523, -9.152e-05, -117.6079957, -0.00027455, -392.02665232, -0.00091517, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 3.85, 4.8, 3.2)
    ops.node(122010, 3.85, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.2025, 27667178.2657157, 11527990.94404821, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 263.49945733, 0.00073986, 316.57744486, 0.00885541, 31.65774449, 0.0303799, -263.49945733, -0.00073986, -316.57744486, -0.00885541, -31.65774449, -0.0303799, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 236.11165175, 0.00073986, 283.67277933, 0.00885541, 28.36727793, 0.0303799, -236.11165175, -0.00073986, -283.67277933, -0.00885541, -28.36727793, -0.0303799, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 202.52900223, 0.01479712, 202.52900223, 0.04439135, 141.77030156, -2097.49558702, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 50.63225056, 7.678e-05, 151.89675167, 0.00023034, 506.32250557, 0.00076781, -50.63225056, -7.678e-05, -151.89675167, -0.00023034, -506.32250557, -0.00076781, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 202.52900223, 0.01479712, 202.52900223, 0.04439135, 141.77030156, -2097.49558702, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 50.63225056, 7.678e-05, 151.89675167, 0.00023034, 506.32250557, 0.00076781, -50.63225056, -7.678e-05, -151.89675167, -0.00023034, -506.32250557, -0.00076781, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.7, 4.8, 3.2)
    ops.node(122011, 7.7, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 30293828.9700036, 12622428.7375015, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 258.07029586, 0.00071801, 309.40697123, 0.00958187, 30.94069712, 0.03460777, -258.07029586, -0.00071801, -309.40697123, -0.00958187, -30.94069712, -0.03460777, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 232.58224155, 0.00071801, 278.84870159, 0.00958187, 27.88487016, 0.03460777, -232.58224155, -0.00071801, -278.84870159, -0.00958187, -27.88487016, -0.03460777, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 223.47548027, 0.01436026, 223.47548027, 0.04308077, 156.43283619, -2187.82322018, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 55.86887007, 7.738e-05, 167.60661021, 0.00023213, 558.68870069, 0.00077376, -55.86887007, -7.738e-05, -167.60661021, -0.00023213, -558.68870069, -0.00077376, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 223.47548027, 0.01436026, 223.47548027, 0.04308077, 156.43283619, -2187.82322018, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 55.86887007, 7.738e-05, 167.60661021, 0.00023213, 558.68870069, 0.00077376, -55.86887007, -7.738e-05, -167.60661021, -0.00023213, -558.68870069, -0.00077376, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 11.55, 4.8, 3.2)
    ops.node(122012, 11.55, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 32711214.44554438, 13629672.68564349, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 200.2567415, 0.00078019, 238.57455935, 0.00896133, 23.85745594, 0.0373457, -200.2567415, -0.00078019, -238.57455935, -0.00896133, -23.85745594, -0.0373457, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 185.41173731, 0.00078019, 220.88906069, 0.00896133, 22.08890607, 0.0373457, -185.41173731, -0.00078019, -220.88906069, -0.00896133, -22.08890607, -0.0373457, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 194.27441858, 0.0156038, 194.27441858, 0.04681141, 135.99209301, -1824.57325396, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 48.56860465, 7.884e-05, 145.70581394, 0.00023652, 485.68604646, 0.00078841, -48.56860465, -7.884e-05, -145.70581394, -0.00023652, -485.68604646, -0.00078841, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 194.27441858, 0.0156038, 194.27441858, 0.04681141, 135.99209301, -1824.57325396, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 48.56860465, 7.884e-05, 145.70581394, 0.00023652, 485.68604646, 0.00078841, -48.56860465, -7.884e-05, -145.70581394, -0.00023652, -485.68604646, -0.00078841, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 14.6, 4.8, 3.2)
    ops.node(122013, 14.6, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.16, 29351725.96147385, 12229885.81728077, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 197.97496097, 0.00084288, 237.08858781, 0.00914257, 23.70885878, 0.03322335, -197.97496097, -0.00084288, -237.08858781, -0.00914257, -23.70885878, -0.03322335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 184.25665588, 0.00084288, 220.65997701, 0.00914257, 22.0659977, 0.03322335, -184.25665588, -0.00084288, -220.65997701, -0.00914257, -22.0659977, -0.03322335, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 178.74602411, 0.01685759, 178.74602411, 0.05057276, 125.12221688, -1874.67986431, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 44.68650603, 8.084e-05, 134.05951808, 0.00024253, 446.86506028, 0.00080842, -44.68650603, -8.084e-05, -134.05951808, -0.00024253, -446.86506028, -0.00080842, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 178.74602411, 0.01685759, 178.74602411, 0.05057276, 125.12221688, -1874.67986431, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 44.68650603, 8.084e-05, 134.05951808, 0.00024253, 446.86506028, 0.00080842, -44.68650603, -8.084e-05, -134.05951808, -0.00024253, -446.86506028, -0.00080842, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 18.45, 4.8, 3.2)
    ops.node(122014, 18.45, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.2025, 31588365.65630184, 13161819.0234591, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 264.60097042, 0.00070621, 316.52833623, 0.00869431, 31.65283362, 0.03515074, -264.60097042, -0.00070621, -316.52833623, -0.00869431, -31.65283362, -0.03515074, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 237.13090905, 0.00070621, 283.66733497, 0.00869431, 28.3667335, 0.03515074, -237.13090905, -0.00070621, -283.66733497, -0.00869431, -28.3667335, -0.03515074, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 224.86478794, 0.01412414, 224.86478794, 0.04237242, 157.40535156, -2031.24093947, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 56.21619699, 7.467e-05, 168.64859096, 0.000224, 562.16196986, 0.00074666, -56.21619699, -7.467e-05, -168.64859096, -0.000224, -562.16196986, -0.00074666, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 224.86478794, 0.01412414, 224.86478794, 0.04237242, 157.40535156, -2031.24093947, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 56.21619699, 7.467e-05, 168.64859096, 0.000224, 562.16196986, 0.00074666, -56.21619699, -7.467e-05, -168.64859096, -0.000224, -562.16196986, -0.00074666, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 22.3, 4.8, 3.2)
    ops.node(122015, 22.3, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.2025, 28641774.63244529, 11934072.76351887, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 255.80904258, 0.00076374, 307.22590707, 0.01004266, 30.72259071, 0.03296594, -255.80904258, -0.00076374, -307.22590707, -0.01004266, -30.72259071, -0.03296594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 232.28245059, 0.00076374, 278.97053936, 0.01004266, 27.89705394, 0.03296594, -232.28245059, -0.00076374, -278.97053936, -0.01004266, -27.89705394, -0.03296594, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 215.5982739, 0.01527472, 215.5982739, 0.04582417, 150.91879173, -2250.48123692, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 53.89956847, 7.895e-05, 161.69870542, 0.00023686, 538.99568474, 0.00078954, -53.89956847, -7.895e-05, -161.69870542, -0.00023686, -538.99568474, -0.00078954, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 215.5982739, 0.01527472, 215.5982739, 0.04582417, 150.91879173, -2250.48123692, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 53.89956847, 7.895e-05, 161.69870542, 0.00023686, 538.99568474, 0.00078954, -53.89956847, -7.895e-05, -161.69870542, -0.00023686, -538.99568474, -0.00078954, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 26.15, 4.8, 3.2)
    ops.node(122016, 26.15, 4.8, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1225, 29651021.27614199, 12354592.1983925, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 121.70323362, 0.00087032, 145.54002181, 0.00842188, 14.55400218, 0.03796207, -121.70323362, -0.00087032, -145.54002181, -0.00842188, -14.55400218, -0.03796207, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 135.19460121, 0.00087032, 161.67380787, 0.00842188, 16.16738079, 0.03796207, -135.19460121, -0.00087032, -161.67380787, -0.00842188, -16.16738079, -0.03796207, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 150.23214234, 0.01740644, 150.23214234, 0.05221933, 105.16249964, -1703.05067387, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 37.55803559, 8.785e-05, 112.67410676, 0.00026355, 375.58035585, 0.0008785, -37.55803559, -8.785e-05, -112.67410676, -0.00026355, -375.58035585, -0.0008785, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 150.23214234, 0.01740644, 150.23214234, 0.05221933, 105.16249964, -1703.05067387, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 37.55803559, 8.785e-05, 112.67410676, 0.00026355, 375.58035585, 0.0008785, -37.55803559, -8.785e-05, -112.67410676, -0.00026355, -375.58035585, -0.0008785, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 9.6, 3.2)
    ops.node(122017, 0.0, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.1225, 29031822.8264651, 12096592.84436046, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 119.03923909, 0.00087882, 142.43151712, 0.01036497, 14.24315171, 0.03887572, -119.03923909, -0.00087882, -142.43151712, -0.01036497, -14.24315171, -0.03887572, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 131.4541986, 0.00087882, 157.2861275, 0.01036497, 15.72861275, 0.03887572, -131.4541986, -0.00087882, -157.2861275, -0.01036497, -15.72861275, -0.03887572, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 160.93324882, 0.01757649, 160.93324882, 0.05272946, 112.65327417, -2019.67219362, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 40.2333122, 9.611e-05, 120.69993661, 0.00028834, 402.33312205, 0.00096115, -40.2333122, -9.611e-05, -120.69993661, -0.00028834, -402.33312205, -0.00096115, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 160.93324882, 0.01757649, 160.93324882, 0.05272946, 112.65327417, -2019.67219362, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 40.2333122, 9.611e-05, 120.69993661, 0.00028834, 402.33312205, 0.00096115, -40.2333122, -9.611e-05, -120.69993661, -0.00028834, -402.33312205, -0.00096115, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 3.85, 9.6, 3.2)
    ops.node(122018, 3.85, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.2025, 29072619.35094796, 12113591.39622832, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 258.02772458, 0.00072345, 309.84809673, 0.01037992, 30.98480967, 0.03401272, -258.02772458, -0.00072345, -309.84809673, -0.01037992, -30.98480967, -0.03401272, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 231.91685543, 0.00072345, 278.49331451, 0.01037992, 27.84933145, 0.03401272, -231.91685543, -0.00072345, -278.49331451, -0.01037992, -27.84933145, -0.03401272, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 219.32372088, 0.01446897, 219.32372088, 0.0434069, 153.52660461, -2274.27002888, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 54.83093022, 7.913e-05, 164.49279066, 0.00023738, 548.30930219, 0.00079128, -54.83093022, -7.913e-05, -164.49279066, -0.00023738, -548.30930219, -0.00079128, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 219.32372088, 0.01446897, 219.32372088, 0.0434069, 153.52660461, -2274.27002888, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 54.83093022, 7.913e-05, 164.49279066, 0.00023738, 548.30930219, 0.00079128, -54.83093022, -7.913e-05, -164.49279066, -0.00023738, -548.30930219, -0.00079128, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 7.7, 9.6, 3.2)
    ops.node(122019, 7.7, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.2025, 30722261.99766035, 12800942.49902515, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 259.01711811, 0.00072099, 310.3854995, 0.01048181, 31.03854995, 0.03611806, -259.01711811, -0.00072099, -310.3854995, -0.01048181, -31.03854995, -0.03611806, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 233.21606376, 0.00072099, 279.46756944, 0.01048181, 27.94675694, 0.03611806, -233.21606376, -0.00072099, -279.46756944, -0.01048181, -27.94675694, -0.03611806, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 232.93876276, 0.01441974, 232.93876276, 0.04325922, 163.05713393, -2340.79536212, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 58.23469069, 7.953e-05, 174.70407207, 0.00023858, 582.3469069, 0.00079528, -58.23469069, -7.953e-05, -174.70407207, -0.00023858, -582.3469069, -0.00079528, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 232.93876276, 0.01441974, 232.93876276, 0.04325922, 163.05713393, -2340.79536212, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 58.23469069, 7.953e-05, 174.70407207, 0.00023858, 582.3469069, 0.00079528, -58.23469069, -7.953e-05, -174.70407207, -0.00023858, -582.3469069, -0.00079528, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 11.55, 9.6, 3.2)
    ops.node(122020, 11.55, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.16, 29509492.97083487, 12295622.07118119, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 188.39799067, 0.00082068, 225.75558687, 0.01023176, 22.57555869, 0.03839196, -188.39799067, -0.00082068, -225.75558687, -0.01023176, -22.57555869, -0.03839196, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 166.25593172, 0.00082068, 199.2229604, 0.01023176, 19.92229604, 0.03839196, -166.25593172, -0.00082068, -199.2229604, -0.01023176, -19.92229604, -0.03839196, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 196.99106411, 0.01641363, 196.99106411, 0.04924089, 137.89374488, -2281.92604658, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 49.24776603, 8.862e-05, 147.74329808, 0.00026585, 492.47766027, 0.00088617, -49.24776603, -8.862e-05, -147.74329808, -0.00026585, -492.47766027, -0.00088617, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 196.99106411, 0.01641363, 196.99106411, 0.04924089, 137.89374488, -2281.92604658, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 49.24776603, 8.862e-05, 147.74329808, 0.00026585, 492.47766027, 0.00088617, -49.24776603, -8.862e-05, -147.74329808, -0.00026585, -492.47766027, -0.00088617, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 14.6, 9.6, 3.2)
    ops.node(122021, 14.6, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.16, 32469025.9492538, 13528760.81218908, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 182.44148826, 0.00076575, 217.58428967, 0.00937412, 21.75842897, 0.04174802, -182.44148826, -0.00076575, -217.58428967, -0.00937412, -21.75842897, -0.04174802, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 161.86211958, 0.00076575, 193.040819, 0.00937412, 19.3040819, 0.04174802, -161.86211958, -0.00076575, -193.040819, -0.00937412, -19.3040819, -0.04174802, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 205.02024849, 0.01531507, 205.02024849, 0.04594522, 143.51417395, -2099.99016978, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 51.25506212, 8.382e-05, 153.76518637, 0.00025147, 512.55062123, 0.00083823, -51.25506212, -8.382e-05, -153.76518637, -0.00025147, -512.55062123, -0.00083823, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 205.02024849, 0.01531507, 205.02024849, 0.04594522, 143.51417395, -2099.99016978, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 51.25506212, 8.382e-05, 153.76518637, 0.00025147, 512.55062123, 0.00083823, -51.25506212, -8.382e-05, -153.76518637, -0.00025147, -512.55062123, -0.00083823, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 18.45, 9.6, 3.2)
    ops.node(122022, 18.45, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.2025, 29547896.73788899, 12311623.64078708, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 252.63968874, 0.00072817, 303.23488979, 0.01097576, 30.32348898, 0.03521845, -252.63968874, -0.00072817, -303.23488979, -0.01097576, -30.32348898, -0.03521845, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 228.59502123, 0.00072817, 274.37488707, 0.01097576, 27.43748871, 0.03521845, -228.59502123, -0.00072817, -274.37488707, -0.01097576, -27.43748871, -0.03521845, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 227.4770515, 0.01456339, 227.4770515, 0.04369017, 159.23393605, -2391.90021159, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 56.86926288, 8.075e-05, 170.60778863, 0.00024225, 568.69262875, 0.0008075, -56.86926288, -8.075e-05, -170.60778863, -0.00024225, -568.69262875, -0.0008075, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 227.4770515, 0.01456339, 227.4770515, 0.04369017, 159.23393605, -2391.90021159, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 56.86926288, 8.075e-05, 170.60778863, 0.00024225, 568.69262875, 0.0008075, -56.86926288, -8.075e-05, -170.60778863, -0.00024225, -568.69262875, -0.0008075, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 22.3, 9.6, 3.2)
    ops.node(122023, 22.3, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.2025, 27001247.05718, 11250519.60715833, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 258.40496613, 0.00073125, 310.51124289, 0.00866141, 31.05112429, 0.02930377, -258.40496613, -0.00073125, -310.51124289, -0.00866141, -31.05112429, -0.02930377, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 231.53667082, 0.00073125, 278.22506861, 0.00866141, 27.82250686, 0.02930377, -231.53667082, -0.00073125, -278.22506861, -0.00866141, -27.82250686, -0.02930377, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 200.45249547, 0.01462493, 200.45249547, 0.04387479, 140.31674683, -2143.76384216, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 50.11312387, 7.787e-05, 150.3393716, 0.0002336, 501.13123868, 0.00077868, -50.11312387, -7.787e-05, -150.3393716, -0.0002336, -501.13123868, -0.00077868, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 200.45249547, 0.01462493, 200.45249547, 0.04387479, 140.31674683, -2143.76384216, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 50.11312387, 7.787e-05, 150.3393716, 0.0002336, 501.13123868, 0.00077868, -50.11312387, -7.787e-05, -150.3393716, -0.0002336, -501.13123868, -0.00077868, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 26.15, 9.6, 3.2)
    ops.node(122024, 26.15, 9.6, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.1225, 28756295.38523661, 11981789.74384859, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 119.31431253, 0.00086297, 142.77477697, 0.00929793, 14.2774777, 0.03726594, -119.31431253, -0.00086297, -142.77477697, -0.00929793, -14.2774777, -0.03726594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 132.42890456, 0.00086297, 158.4680573, 0.00929793, 15.84680573, 0.03726594, -132.42890456, -0.00086297, -158.4680573, -0.00929793, -15.84680573, -0.03726594, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 151.71582522, 0.01725931, 151.71582522, 0.05177792, 106.20107765, -1821.88104502, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 37.9289563, 9.148e-05, 113.78686891, 0.00027443, 379.28956305, 0.00091478, -37.9289563, -9.148e-05, -113.78686891, -0.00027443, -379.28956305, -0.00091478, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 151.71582522, 0.01725931, 151.71582522, 0.05177792, 106.20107765, -1821.88104502, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 37.9289563, 9.148e-05, 113.78686891, 0.00027443, 379.28956305, 0.00091478, -37.9289563, -9.148e-05, -113.78686891, -0.00027443, -379.28956305, -0.00091478, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171025, 0.0, 14.4, 3.2)
    ops.node(122025, 0.0, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1025, 171025, 122025, 0.0625, 31241751.10258349, 13017396.29274312, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21025, 55.9411022, 0.00123916, 66.61289318, 0.0115323, 6.66128932, 0.05046067, -55.9411022, -0.00123916, -66.61289318, -0.0115323, -6.66128932, -0.05046067, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11025, 59.47597376, 0.00123916, 70.8221063, 0.0115323, 7.08221063, 0.05046067, -59.47597376, -0.00123916, -70.8221063, -0.0115323, -7.08221063, -0.05046067, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21025, 1025, 0.0, 98.76344572, 0.02478329, 98.76344572, 0.07434987, 69.13441201, -1311.77632587, 0.05, 2, 0, 71025, 22025, 2, 3)
    ops.uniaxialMaterial('LimitState', 41025, 24.69086143, 0.00010743, 74.07258429, 0.0003223, 246.90861431, 0.00107432, -24.69086143, -0.00010743, -74.07258429, -0.0003223, -246.90861431, -0.00107432, 0.4, 0.3, 0.003, 0.0, 0.0, 21025, 2)
    ops.limitCurve('ThreePoint', 11025, 1025, 0.0, 98.76344572, 0.02478329, 98.76344572, 0.07434987, 69.13441201, -1311.77632587, 0.05, 2, 0, 71025, 22025, 1, 3)
    ops.uniaxialMaterial('LimitState', 31025, 24.69086143, 0.00010743, 74.07258429, 0.0003223, 246.90861431, 0.00107432, -24.69086143, -0.00010743, -74.07258429, -0.0003223, -246.90861431, -0.00107432, 0.4, 0.3, 0.003, 0.0, 0.0, 11025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1025, 99999, 'P', 41025, 'Vy', 31025, 'Vz', 21025, 'My', 11025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171025, 71025, 171025, 1025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122025, 122025, 22025, 1025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171026, 3.85, 14.4, 3.2)
    ops.node(122026, 3.85, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1026, 171026, 122026, 0.1225, 28937022.7861094, 12057092.82754558, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21026, 132.20529471, 0.00087489, 158.33798656, 0.00908531, 15.83379866, 0.03464076, -132.20529471, -0.00087489, -158.33798656, -0.00908531, -15.83379866, -0.03464076, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11026, 138.84530298, 0.00087489, 166.29050876, 0.00908531, 16.62905088, 0.03464076, -138.84530298, -0.00087489, -166.29050876, -0.00908531, -16.62905088, -0.03464076, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21026, 1026, 0.0, 141.14521034, 0.01749781, 141.14521034, 0.05249343, 98.80164724, -1566.02234819, 0.05, 2, 0, 71026, 22026, 2, 3)
    ops.uniaxialMaterial('LimitState', 41026, 35.28630258, 8.457e-05, 105.85890775, 0.00025372, 352.86302584, 0.00084573, -35.28630258, -8.457e-05, -105.85890775, -0.00025372, -352.86302584, -0.00084573, 0.4, 0.3, 0.003, 0.0, 0.0, 21026, 2)
    ops.limitCurve('ThreePoint', 11026, 1026, 0.0, 141.14521034, 0.01749781, 141.14521034, 0.05249343, 98.80164724, -1566.02234819, 0.05, 2, 0, 71026, 22026, 1, 3)
    ops.uniaxialMaterial('LimitState', 31026, 35.28630258, 8.457e-05, 105.85890775, 0.00025372, 352.86302584, 0.00084573, -35.28630258, -8.457e-05, -105.85890775, -0.00025372, -352.86302584, -0.00084573, 0.4, 0.3, 0.003, 0.0, 0.0, 11026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1026, 99999, 'P', 41026, 'Vy', 31026, 'Vz', 21026, 'My', 11026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171026, 71026, 171026, 1026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122026, 122026, 22026, 1026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171027, 7.7, 14.4, 3.2)
    ops.node(122027, 7.7, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1027, 171027, 122027, 0.1225, 26152220.18426416, 10896758.41011007, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21027, 127.69406141, 0.00093476, 152.78349509, 0.00863865, 15.27834951, 0.02893866, -127.69406141, -0.00093476, -152.78349509, -0.00863865, -15.27834951, -0.02893866, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11027, 133.39009183, 0.00093476, 159.59868624, 0.00863865, 15.95986862, 0.02893866, -133.39009183, -0.00093476, -159.59868624, -0.00863865, -15.95986862, -0.02893866, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21027, 1027, 0.0, 129.06991218, 0.01869516, 129.06991218, 0.05608547, 90.34893853, -1536.81877187, 0.05, 2, 0, 71027, 22027, 2, 3)
    ops.uniaxialMaterial('LimitState', 41027, 32.26747805, 8.557e-05, 96.80243414, 0.00025672, 322.67478046, 0.00085573, -32.26747805, -8.557e-05, -96.80243414, -0.00025672, -322.67478046, -0.00085573, 0.4, 0.3, 0.003, 0.0, 0.0, 21027, 2)
    ops.limitCurve('ThreePoint', 11027, 1027, 0.0, 129.06991218, 0.01869516, 129.06991218, 0.05608547, 90.34893853, -1536.81877187, 0.05, 2, 0, 71027, 22027, 1, 3)
    ops.uniaxialMaterial('LimitState', 31027, 32.26747805, 8.557e-05, 96.80243414, 0.00025672, 322.67478046, 0.00085573, -32.26747805, -8.557e-05, -96.80243414, -0.00025672, -322.67478046, -0.00085573, 0.4, 0.3, 0.003, 0.0, 0.0, 11027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1027, 99999, 'P', 41027, 'Vy', 31027, 'Vz', 21027, 'My', 11027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171027, 71027, 171027, 1027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122027, 122027, 22027, 1027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171028, 11.55, 14.4, 3.2)
    ops.node(122028, 11.55, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1028, 171028, 122028, 0.09, 28172494.4326057, 11738539.34691904, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21028, 88.53309939, 0.00107129, 105.61888671, 0.00947325, 10.56188867, 0.03687605, -88.53309939, -0.00107129, -105.61888671, -0.00947325, -10.56188867, -0.03687605, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11028, 97.5333005, 0.00107129, 116.35601472, 0.00947325, 11.63560147, 0.03687605, -97.5333005, -0.00107129, -116.35601472, -0.00947325, -11.63560147, -0.03687605, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21028, 1028, 0.0, 118.8705052, 0.02142589, 118.8705052, 0.06427767, 83.20935364, -1541.02400059, 0.05, 2, 0, 71028, 22028, 2, 3)
    ops.uniaxialMaterial('LimitState', 41028, 29.7176263, 9.958e-05, 89.1528789, 0.00029873, 297.176263, 0.00099577, -29.7176263, -9.958e-05, -89.1528789, -0.00029873, -297.176263, -0.00099577, 0.4, 0.3, 0.003, 0.0, 0.0, 21028, 2)
    ops.limitCurve('ThreePoint', 11028, 1028, 0.0, 118.8705052, 0.02142589, 118.8705052, 0.06427767, 83.20935364, -1541.02400059, 0.05, 2, 0, 71028, 22028, 1, 3)
    ops.uniaxialMaterial('LimitState', 31028, 29.7176263, 9.958e-05, 89.1528789, 0.00029873, 297.176263, 0.00099577, -29.7176263, -9.958e-05, -89.1528789, -0.00029873, -297.176263, -0.00099577, 0.4, 0.3, 0.003, 0.0, 0.0, 11028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1028, 99999, 'P', 41028, 'Vy', 31028, 'Vz', 21028, 'My', 11028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171028, 71028, 171028, 1028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122028, 122028, 22028, 1028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171029, 14.6, 14.4, 3.2)
    ops.node(122029, 14.6, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1029, 171029, 122029, 0.09, 26829606.16751771, 11179002.56979905, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21029, 89.6397034, 0.00104407, 106.80865442, 0.0103447, 10.68086544, 0.0343424, -89.6397034, -0.00104407, -106.80865442, -0.0103447, -10.68086544, -0.0343424, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11029, 100.20677611, 0.00104407, 119.39966905, 0.0103447, 11.93996691, 0.0343424, -100.20677611, -0.00104407, -119.39966905, -0.0103447, -11.93996691, -0.0343424, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21029, 1029, 0.0, 124.4341007, 0.0208813, 124.4341007, 0.06264391, 87.10387049, -1775.50883946, 0.05, 2, 0, 71029, 22029, 2, 3)
    ops.uniaxialMaterial('LimitState', 41029, 31.10852517, 0.00010946, 93.32557552, 0.00032837, 311.08525175, 0.00109455, -31.10852517, -0.00010946, -93.32557552, -0.00032837, -311.08525175, -0.00109455, 0.4, 0.3, 0.003, 0.0, 0.0, 21029, 2)
    ops.limitCurve('ThreePoint', 11029, 1029, 0.0, 124.4341007, 0.0208813, 124.4341007, 0.06264391, 87.10387049, -1775.50883946, 0.05, 2, 0, 71029, 22029, 1, 3)
    ops.uniaxialMaterial('LimitState', 31029, 31.10852517, 0.00010946, 93.32557552, 0.00032837, 311.08525175, 0.00109455, -31.10852517, -0.00010946, -93.32557552, -0.00032837, -311.08525175, -0.00109455, 0.4, 0.3, 0.003, 0.0, 0.0, 11029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1029, 99999, 'P', 41029, 'Vy', 31029, 'Vz', 21029, 'My', 11029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171029, 71029, 171029, 1029, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122029, 122029, 22029, 1029, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171030, 18.45, 14.4, 3.2)
    ops.node(122030, 18.45, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1030, 171030, 122030, 0.1225, 34109029.68749252, 14212095.70312188, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21030, 132.99884164, 0.00089268, 157.85466973, 0.00899737, 15.78546697, 0.04155564, -132.99884164, -0.00089268, -157.85466973, -0.00899737, -15.78546697, -0.04155564, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11030, 138.88859845, 0.00089268, 164.84514878, 0.00899737, 16.48451488, 0.04155564, -138.88859845, -0.00089268, -164.84514878, -0.00899737, -16.48451488, -0.04155564, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21030, 1030, 0.0, 160.08571432, 0.01785367, 160.08571432, 0.05356101, 112.06000003, -1514.95926395, 0.05, 2, 0, 71030, 22030, 2, 3)
    ops.uniaxialMaterial('LimitState', 41030, 40.02142858, 8.138e-05, 120.06428574, 0.00024413, 400.2142858, 0.00081377, -40.02142858, -8.138e-05, -120.06428574, -0.00024413, -400.2142858, -0.00081377, 0.4, 0.3, 0.003, 0.0, 0.0, 21030, 2)
    ops.limitCurve('ThreePoint', 11030, 1030, 0.0, 160.08571432, 0.01785367, 160.08571432, 0.05356101, 112.06000003, -1514.95926395, 0.05, 2, 0, 71030, 22030, 1, 3)
    ops.uniaxialMaterial('LimitState', 31030, 40.02142858, 8.138e-05, 120.06428574, 0.00024413, 400.2142858, 0.00081377, -40.02142858, -8.138e-05, -120.06428574, -0.00024413, -400.2142858, -0.00081377, 0.4, 0.3, 0.003, 0.0, 0.0, 11030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1030, 99999, 'P', 41030, 'Vy', 31030, 'Vz', 21030, 'My', 11030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171030, 71030, 171030, 1030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122030, 122030, 22030, 1030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171031, 22.3, 14.4, 3.2)
    ops.node(122031, 22.3, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1031, 171031, 122031, 0.1225, 32875036.15571297, 13697931.73154707, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21031, 134.01037923, 0.00088151, 159.57263211, 0.00980436, 15.95726321, 0.0409812, -134.01037923, -0.00088151, -159.57263211, -0.00980436, -15.95726321, -0.0409812, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11031, 140.34902094, 0.00088151, 167.12035899, 0.00980436, 16.7120359, 0.0409812, -140.34902094, -0.00088151, -167.12035899, -0.00980436, -16.7120359, -0.0409812, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21031, 1031, 0.0, 157.11926278, 0.01763012, 157.11926278, 0.05289036, 109.98348395, -1565.08208423, 0.05, 2, 0, 71031, 22031, 2, 3)
    ops.uniaxialMaterial('LimitState', 41031, 39.2798157, 8.287e-05, 117.83944709, 0.0002486, 392.79815695, 0.00082867, -39.2798157, -8.287e-05, -117.83944709, -0.0002486, -392.79815695, -0.00082867, 0.4, 0.3, 0.003, 0.0, 0.0, 21031, 2)
    ops.limitCurve('ThreePoint', 11031, 1031, 0.0, 157.11926278, 0.01763012, 157.11926278, 0.05289036, 109.98348395, -1565.08208423, 0.05, 2, 0, 71031, 22031, 1, 3)
    ops.uniaxialMaterial('LimitState', 31031, 39.2798157, 8.287e-05, 117.83944709, 0.0002486, 392.79815695, 0.00082867, -39.2798157, -8.287e-05, -117.83944709, -0.0002486, -392.79815695, -0.00082867, 0.4, 0.3, 0.003, 0.0, 0.0, 11031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1031, 99999, 'P', 41031, 'Vy', 31031, 'Vz', 21031, 'My', 11031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171031, 71031, 171031, 1031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122031, 122031, 22031, 1031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171032, 26.15, 14.4, 3.2)
    ops.node(122032, 26.15, 14.4, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1032, 171032, 122032, 0.0625, 30873640.36597519, 12864016.81915633, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21032, 56.03554502, 0.00122372, 66.75492412, 0.00989729, 6.67549241, 0.04798438, -56.03554502, -0.00122372, -66.75492412, -0.00989729, -6.67549241, -0.04798438, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11032, 59.72867015, 0.00122372, 71.15452954, 0.00989729, 7.11545295, 0.04798438, -59.72867015, -0.00122372, -71.15452954, -0.00989729, -7.11545295, -0.04798438, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21032, 1032, 0.0, 87.78112004, 0.02447444, 87.78112004, 0.07342332, 61.44678403, -1206.23698238, 0.05, 2, 0, 71032, 22032, 2, 3)
    ops.uniaxialMaterial('LimitState', 41032, 21.94528001, 9.662e-05, 65.83584003, 0.00028987, 219.45280011, 0.00096625, -21.94528001, -9.662e-05, -65.83584003, -0.00028987, -219.45280011, -0.00096625, 0.4, 0.3, 0.003, 0.0, 0.0, 21032, 2)
    ops.limitCurve('ThreePoint', 11032, 1032, 0.0, 87.78112004, 0.02447444, 87.78112004, 0.07342332, 61.44678403, -1206.23698238, 0.05, 2, 0, 71032, 22032, 1, 3)
    ops.uniaxialMaterial('LimitState', 31032, 21.94528001, 9.662e-05, 65.83584003, 0.00028987, 219.45280011, 0.00096625, -21.94528001, -9.662e-05, -65.83584003, -0.00028987, -219.45280011, -0.00096625, 0.4, 0.3, 0.003, 0.0, 0.0, 11032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1032, 99999, 'P', 41032, 'Vy', 31032, 'Vz', 21032, 'My', 11032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171032, 71032, 171032, 1032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122032, 122032, 22032, 1032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.15)
    ops.node(123001, 0.0, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 29809683.56008601, 12420701.48336917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 47.84587846, 0.00111512, 57.48623427, 0.01285557, 5.74862343, 0.05746034, -47.84587846, -0.00111512, -57.48623427, -0.01285557, -5.74862343, -0.05746034, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 52.20304811, 0.00111512, 62.72131999, 0.01285557, 6.272132, 0.05746034, -52.20304811, -0.00111512, -62.72131999, -0.01285557, -6.272132, -0.05746034, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 90.33956932, 0.02230242, 90.33956932, 0.06690725, 63.23769852, -1308.85217025, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 22.58489233, 0.00010299, 67.75467699, 0.00030897, 225.84892329, 0.0010299, -22.58489233, -0.00010299, -67.75467699, -0.00030897, -225.84892329, -0.0010299, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 90.33956932, 0.02230242, 90.33956932, 0.06690725, 63.23769852, -1308.85217025, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 22.58489233, 0.00010299, 67.75467699, 0.00030897, 225.84892329, 0.0010299, -22.58489233, -0.00010299, -67.75467699, -0.00030897, -225.84892329, -0.0010299, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.85, 0.0, 6.15)
    ops.node(123002, 3.85, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 30651788.08610618, 12771578.36921091, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 65.31311768, 0.00117188, 77.7474657, 0.0123592, 7.77474657, 0.04397205, -65.31311768, -0.00117188, -77.7474657, -0.0123592, -7.77474657, -0.04397205, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 65.31311768, 0.00117188, 77.7474657, 0.0123592, 7.77474657, 0.04397205, -65.31311768, -0.00117188, -77.7474657, -0.0123592, -7.77474657, -0.04397205, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 93.43394876, 0.02343767, 93.43394876, 0.07031302, 65.40376413, -1222.05945046, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 23.35848719, 0.00010359, 70.07546157, 0.00031077, 233.5848719, 0.00103591, -23.35848719, -0.00010359, -70.07546157, -0.00031077, -233.5848719, -0.00103591, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 93.43394876, 0.02343767, 93.43394876, 0.07031302, 65.40376413, -1222.05945046, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 23.35848719, 0.00010359, 70.07546157, 0.00031077, 233.5848719, 0.00103591, -23.35848719, -0.00010359, -70.07546157, -0.00031077, -233.5848719, -0.00103591, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.7, 0.0, 6.15)
    ops.node(123003, 7.7, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0625, 27713405.78159033, 11547252.40899597, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 64.80812544, 0.00123667, 77.14566918, 0.01084551, 7.71456692, 0.03564965, -64.80812544, -0.00123667, -77.14566918, -0.01084551, -7.71456692, -0.03564965, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 64.80812544, 0.00123667, 77.14566918, 0.01084551, 7.71456692, 0.03564965, -64.80812544, -0.00123667, -77.14566918, -0.01084551, -7.71456692, -0.03564965, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 77.60588219, 0.0247334, 77.60588219, 0.07420021, 54.32411753, -1190.65933718, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 19.40147055, 9.517e-05, 58.20441164, 0.0002855, 194.01470547, 0.00095165, -19.40147055, -9.517e-05, -58.20441164, -0.0002855, -194.01470547, -0.00095165, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 77.60588219, 0.0247334, 77.60588219, 0.07420021, 54.32411753, -1190.65933718, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 19.40147055, 9.517e-05, 58.20441164, 0.0002855, 194.01470547, 0.00095165, -19.40147055, -9.517e-05, -58.20441164, -0.0002855, -194.01470547, -0.00095165, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 18.45, 0.0, 6.15)
    ops.node(123006, 18.45, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 28408137.80361635, 11836724.08484015, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 66.38524758, 0.00127316, 79.06314511, 0.00979043, 7.90631451, 0.03632251, -66.38524758, -0.00127316, -79.06314511, -0.00979043, -7.90631451, -0.03632251, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 66.38524758, 0.00127316, 79.06314511, 0.00979043, 7.90631451, 0.03632251, -66.38524758, -0.00127316, -79.06314511, -0.00979043, -7.90631451, -0.03632251, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 62.17504342, 0.02546312, 62.17504342, 0.07638937, 43.5225304, -1038.03563586, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 15.54376086, 7.438e-05, 46.63128257, 0.00022314, 155.43760856, 0.00074379, -15.54376086, -7.438e-05, -46.63128257, -0.00022314, -155.43760856, -0.00074379, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 62.17504342, 0.02546312, 62.17504342, 0.07638937, 43.5225304, -1038.03563586, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 15.54376086, 7.438e-05, 46.63128257, 0.00022314, 155.43760856, 0.00074379, -15.54376086, -7.438e-05, -46.63128257, -0.00022314, -155.43760856, -0.00074379, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 22.3, 0.0, 6.15)
    ops.node(123007, 22.3, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 29458187.76720933, 12274244.90300389, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 62.82119223, 0.00137779, 74.82956215, 0.01016374, 7.48295621, 0.03917127, -62.82119223, -0.00137779, -74.82956215, -0.01016374, -7.48295621, -0.03917127, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 62.82119223, 0.00137779, 74.82956215, 0.01016374, 7.48295621, 0.03917127, -62.82119223, -0.00137779, -74.82956215, -0.01016374, -7.48295621, -0.03917127, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 64.01299651, 0.02755586, 64.01299651, 0.08266758, 44.80909756, -1093.88540107, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 16.00324913, 7.385e-05, 48.00974738, 0.00022154, 160.03249128, 0.00073848, -16.00324913, -7.385e-05, -48.00974738, -0.00022154, -160.03249128, -0.00073848, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 64.01299651, 0.02755586, 64.01299651, 0.08266758, 44.80909756, -1093.88540107, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 16.00324913, 7.385e-05, 48.00974738, 0.00022154, 160.03249128, 0.00073848, -16.00324913, -7.385e-05, -48.00974738, -0.00022154, -160.03249128, -0.00073848, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 26.15, 0.0, 6.15)
    ops.node(123008, 26.15, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 28711573.28921484, 11963155.53717285, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 43.96919, 0.00134464, 52.89387738, 0.01098224, 5.28938774, 0.05323751, -43.96919, -0.00134464, -52.89387738, -0.01098224, -5.28938774, -0.05323751, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 46.06495413, 0.00134464, 55.41503118, 0.01098224, 5.54150312, 0.05323751, -46.06495413, -0.00134464, -55.41503118, -0.01098224, -5.54150312, -0.05323751, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 74.37581305, 0.0268928, 74.37581305, 0.0806784, 52.06306913, -1053.0522562, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 18.59395326, 8.803e-05, 55.78185978, 0.0002641, 185.93953262, 0.00088034, -18.59395326, -8.803e-05, -55.78185978, -0.0002641, -185.93953262, -0.00088034, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 74.37581305, 0.0268928, 74.37581305, 0.0806784, 52.06306913, -1053.0522562, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 18.59395326, 8.803e-05, 55.78185978, 0.0002641, 185.93953262, 0.00088034, -18.59395326, -8.803e-05, -55.78185978, -0.0002641, -185.93953262, -0.00088034, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 4.8, 6.15)
    ops.node(123009, 0.0, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 26524091.41939091, 11051704.75807955, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 53.74335368, 0.00120093, 63.76380105, 0.00947269, 6.37638011, 0.0333482, -53.74335368, -0.00120093, -63.76380105, -0.00947269, -6.37638011, -0.0333482, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 53.74335368, 0.00120093, 63.76380105, 0.00947269, 6.37638011, 0.0333482, -53.74335368, -0.00120093, -63.76380105, -0.00947269, -6.37638011, -0.0333482, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 88.84552865, 0.02401869, 88.84552865, 0.07205607, 62.19187006, -1295.51420084, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 22.21138216, 0.00011383, 66.63414649, 0.0003415, 222.11382163, 0.00113833, -22.21138216, -0.00011383, -66.63414649, -0.0003415, -222.11382163, -0.00113833, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 88.84552865, 0.02401869, 88.84552865, 0.07205607, 62.19187006, -1295.51420084, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 22.21138216, 0.00011383, 66.63414649, 0.0003415, 222.11382163, 0.00113833, -22.21138216, -0.00011383, -66.63414649, -0.0003415, -222.11382163, -0.00113833, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 3.85, 4.8, 6.15)
    ops.node(123010, 3.85, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 33340524.8414375, 13891885.35059896, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 136.88198495, 0.00085715, 162.85243256, 0.0094897, 16.28524326, 0.04148539, -136.88198495, -0.00085715, -162.85243256, -0.0094897, -16.28524326, -0.04148539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 130.68349738, 0.00085715, 155.4779137, 0.0094897, 15.54779137, 0.04148539, -130.68349738, -0.00085715, -155.4779137, -0.0094897, -15.54779137, -0.04148539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 159.0429481, 0.01714296, 159.0429481, 0.05142888, 111.33006367, -1567.60992301, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 39.76073703, 8.271e-05, 119.28221108, 0.00024813, 397.60737025, 0.0008271, -39.76073703, -8.271e-05, -119.28221108, -0.00024813, -397.60737025, -0.0008271, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 159.0429481, 0.01714296, 159.0429481, 0.05142888, 111.33006367, -1567.60992301, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 39.76073703, 8.271e-05, 119.28221108, 0.00024813, 397.60737025, 0.0008271, -39.76073703, -8.271e-05, -119.28221108, -0.00024813, -397.60737025, -0.0008271, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.7, 4.8, 6.15)
    ops.node(123011, 7.7, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 29093011.75661206, 12122088.23192169, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 139.9924891, 0.00088738, 167.72803997, 0.01076187, 16.772804, 0.03693746, -139.9924891, -0.00088738, -167.72803997, -0.01076187, -16.772804, -0.03693746, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 133.13064714, 0.00088738, 159.50671816, 0.01076187, 15.95067182, 0.03693746, -133.13064714, -0.00088738, -159.50671816, -0.01076187, -15.95067182, -0.03693746, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 147.77560468, 0.01774761, 147.77560468, 0.05324284, 103.44292328, -1708.26464198, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 36.94390117, 8.807e-05, 110.83170351, 0.00026421, 369.43901171, 0.00088071, -36.94390117, -8.807e-05, -110.83170351, -0.00026421, -369.43901171, -0.00088071, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 147.77560468, 0.01774761, 147.77560468, 0.05324284, 103.44292328, -1708.26464198, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 36.94390117, 8.807e-05, 110.83170351, 0.00026421, 369.43901171, 0.00088071, -36.94390117, -8.807e-05, -110.83170351, -0.00026421, -369.43901171, -0.00088071, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 11.55, 4.8, 6.15)
    ops.node(123012, 11.55, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 29369354.30670407, 12237230.96112669, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 129.03371761, 0.00086616, 154.85609945, 0.01026726, 15.48560994, 0.03841251, -129.03371761, -0.00086616, -154.85609945, -0.01026726, -15.48560994, -0.03841251, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 122.84546237, 0.00086616, 147.42944317, 0.01026726, 14.74294432, 0.03841251, -122.84546237, -0.00086616, -147.42944317, -0.01026726, -14.74294432, -0.03841251, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 139.78003428, 0.01732311, 139.78003428, 0.05196934, 97.84602399, -1511.30761868, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 34.94500857, 8.252e-05, 104.83502571, 0.00024757, 349.45008569, 0.00082522, -34.94500857, -8.252e-05, -104.83502571, -0.00024757, -349.45008569, -0.00082522, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 139.78003428, 0.01732311, 139.78003428, 0.05196934, 97.84602399, -1511.30761868, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 34.94500857, 8.252e-05, 104.83502571, 0.00024757, 349.45008569, 0.00082522, -34.94500857, -8.252e-05, -104.83502571, -0.00024757, -349.45008569, -0.00082522, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 14.6, 4.8, 6.15)
    ops.node(123013, 14.6, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.1225, 28556396.76498147, 11898498.65207561, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 127.29081853, 0.00093237, 152.86159539, 0.01135577, 15.28615954, 0.03821347, -127.29081853, -0.00093237, -152.86159539, -0.01135577, -15.28615954, -0.03821347, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 121.84417264, 0.00093237, 146.32080172, 0.01135577, 14.63208017, 0.03821347, -121.84417264, -0.00093237, -146.32080172, -0.01135577, -14.63208017, -0.03821347, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 146.71694511, 0.0186473, 146.71694511, 0.05594191, 102.70186158, -1759.56847668, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 36.67923628, 8.908e-05, 110.03770883, 0.00026725, 366.79236277, 0.00089083, -36.67923628, -8.908e-05, -110.03770883, -0.00026725, -366.79236277, -0.00089083, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 146.71694511, 0.0186473, 146.71694511, 0.05594191, 102.70186158, -1759.56847668, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 36.67923628, 8.908e-05, 110.03770883, 0.00026725, 366.79236277, 0.00089083, -36.67923628, -8.908e-05, -110.03770883, -0.00026725, -366.79236277, -0.00089083, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 18.45, 4.8, 6.15)
    ops.node(123014, 18.45, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1225, 28238947.50153174, 11766228.12563823, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 135.24070815, 0.00089972, 162.08943736, 0.00941193, 16.20894374, 0.03412674, -135.24070815, -0.00089972, -162.08943736, -0.00941193, -16.20894374, -0.03412674, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 129.07493471, 0.00089972, 154.69960066, 0.00941193, 15.46996007, 0.03412674, -129.07493471, -0.00089972, -154.69960066, -0.00941193, -15.46996007, -0.03412674, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 137.30500289, 0.01799449, 137.30500289, 0.05398346, 96.11350202, -1542.86380784, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 34.32625072, 8.431e-05, 102.97875216, 0.00025292, 343.26250721, 0.00084306, -34.32625072, -8.431e-05, -102.97875216, -0.00025292, -343.26250721, -0.00084306, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 137.30500289, 0.01799449, 137.30500289, 0.05398346, 96.11350202, -1542.86380784, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 34.32625072, 8.431e-05, 102.97875216, 0.00025292, 343.26250721, 0.00084306, -34.32625072, -8.431e-05, -102.97875216, -0.00025292, -343.26250721, -0.00084306, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 22.3, 4.8, 6.15)
    ops.node(123015, 22.3, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 28849828.05117931, 12020761.68799138, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 140.44421434, 0.00088409, 168.29232439, 0.01020222, 16.82923244, 0.03597252, -140.44421434, -0.00088409, -168.29232439, -0.01020222, -16.82923244, -0.03597252, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 133.45647808, 0.00088409, 159.91901843, 0.01020222, 15.99190184, 0.03597252, -133.45647808, -0.00088409, -159.91901843, -0.01020222, -15.99190184, -0.03597252, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 145.99776188, 0.01768178, 145.99776188, 0.05304535, 102.19843332, -1688.79013159, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 36.49944047, 8.774e-05, 109.49832141, 0.00026323, 364.9944047, 0.00087745, -36.49944047, -8.774e-05, -109.49832141, -0.00026323, -364.9944047, -0.00087745, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 145.99776188, 0.01768178, 145.99776188, 0.05304535, 102.19843332, -1688.79013159, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 36.49944047, 8.774e-05, 109.49832141, 0.00026323, 364.9944047, 0.00087745, -36.49944047, -8.774e-05, -109.49832141, -0.00026323, -364.9944047, -0.00087745, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 26.15, 4.8, 6.15)
    ops.node(123016, 26.15, 4.8, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 31096026.82304648, 12956677.84293604, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 53.60255461, 0.00120291, 63.71981912, 0.01146822, 6.37198191, 0.04795898, -53.60255461, -0.00120291, -63.71981912, -0.01146822, -6.37198191, -0.04795898, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 53.60255461, 0.00120291, 63.71981912, 0.01146822, 6.37198191, 0.04795898, -53.60255461, -0.00120291, -63.71981912, -0.01146822, -6.37198191, -0.04795898, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 102.56351948, 0.02405826, 102.56351948, 0.07217478, 71.79446364, -1398.16463973, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 25.64087987, 0.00011209, 76.92263961, 0.00033627, 256.4087987, 0.00112089, -25.64087987, -0.00011209, -76.92263961, -0.00033627, -256.4087987, -0.00112089, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 102.56351948, 0.02405826, 102.56351948, 0.07217478, 71.79446364, -1398.16463973, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 25.64087987, 0.00011209, 76.92263961, 0.00033627, 256.4087987, 0.00112089, -25.64087987, -0.00011209, -76.92263961, -0.00033627, -256.4087987, -0.00112089, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 9.6, 6.15)
    ops.node(123017, 0.0, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 30488544.4621688, 12703560.19257033, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 53.33909266, 0.00131794, 63.45057291, 0.0098029, 6.34505729, 0.04500142, -53.33909266, -0.00131794, -63.45057291, -0.0098029, -6.34505729, -0.04500142, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 53.33909266, 0.00131794, 63.45057291, 0.0098029, 6.34505729, 0.04500142, -53.33909266, -0.00131794, -63.45057291, -0.0098029, -6.34505729, -0.04500142, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 95.03167355, 0.02635881, 95.03167355, 0.07907644, 66.52217148, -1243.81799541, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 23.75791839, 0.00010593, 71.27375516, 0.00031778, 237.57918387, 0.00105927, -23.75791839, -0.00010593, -71.27375516, -0.00031778, -237.57918387, -0.00105927, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 95.03167355, 0.02635881, 95.03167355, 0.07907644, 66.52217148, -1243.81799541, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 23.75791839, 0.00010593, 71.27375516, 0.00031778, 237.57918387, 0.00105927, -23.75791839, -0.00010593, -71.27375516, -0.00031778, -237.57918387, -0.00105927, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 3.85, 9.6, 6.15)
    ops.node(123018, 3.85, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1225, 28815020.79176477, 12006258.66323532, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 131.26716864, 0.00093679, 157.32752016, 0.01025266, 15.73275202, 0.03610715, -131.26716864, -0.00093679, -157.32752016, -0.01025266, -15.73275202, -0.03610715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 126.0129598, 0.00093679, 151.03019802, 0.01025266, 15.1030198, 0.03610715, -126.0129598, -0.00093679, -151.03019802, -0.01025266, -15.1030198, -0.03610715, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 143.16890587, 0.01873579, 143.16890587, 0.05620736, 100.21823411, -1626.90155641, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 35.79222647, 8.615e-05, 107.3766794, 0.00025845, 357.92226467, 0.00086149, -35.79222647, -8.615e-05, -107.3766794, -0.00025845, -357.92226467, -0.00086149, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 143.16890587, 0.01873579, 143.16890587, 0.05620736, 100.21823411, -1626.90155641, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 35.79222647, 8.615e-05, 107.3766794, 0.00025845, 357.92226467, 0.00086149, -35.79222647, -8.615e-05, -107.3766794, -0.00025845, -357.92226467, -0.00086149, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 7.7, 9.6, 6.15)
    ops.node(123019, 7.7, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1225, 25682464.47562659, 10701026.86484441, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 127.75061305, 0.00090488, 152.8935517, 0.00986743, 15.28935517, 0.02974431, -127.75061305, -0.00090488, -152.8935517, -0.00986743, -15.28935517, -0.02974431, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 122.30312467, 0.00090488, 146.37392861, 0.00986743, 14.63739286, 0.02974431, -122.30312467, -0.00090488, -146.37392861, -0.00986743, -14.63739286, -0.02974431, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 133.85258871, 0.0180976, 133.85258871, 0.05429279, 93.6968121, -1690.19756959, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 33.46314718, 9.037e-05, 100.38944153, 0.0002711, 334.63147178, 0.00090367, -33.46314718, -9.037e-05, -100.38944153, -0.0002711, -334.63147178, -0.00090367, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 133.85258871, 0.0180976, 133.85258871, 0.05429279, 93.6968121, -1690.19756959, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 33.46314718, 9.037e-05, 100.38944153, 0.0002711, 334.63147178, 0.00090367, -33.46314718, -9.037e-05, -100.38944153, -0.0002711, -334.63147178, -0.00090367, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 11.55, 9.6, 6.15)
    ops.node(123020, 11.55, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1225, 30854831.70625789, 12856179.87760746, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 108.48352822, 0.00088116, 129.98591604, 0.01043149, 12.9985916, 0.04531774, -108.48352822, -0.00088116, -129.98591604, -0.01043149, -12.9985916, -0.04531774, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 120.22389676, 0.00088116, 144.05332871, 0.01043149, 14.40533287, 0.04531774, -120.22389676, -0.00088116, -144.05332871, -0.01043149, -14.40533287, -0.04531774, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 159.98561275, 0.01762318, 159.98561275, 0.05286955, 111.98992892, -1881.57420072, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 39.99640319, 8.99e-05, 119.98920956, 0.00026971, 399.96403187, 0.00089903, -39.99640319, -8.99e-05, -119.98920956, -0.00026971, -399.96403187, -0.00089903, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 159.98561275, 0.01762318, 159.98561275, 0.05286955, 111.98992892, -1881.57420072, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 39.99640319, 8.99e-05, 119.98920956, 0.00026971, 399.96403187, 0.00089903, -39.99640319, -8.99e-05, -119.98920956, -0.00026971, -399.96403187, -0.00089903, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 14.6, 9.6, 6.15)
    ops.node(123021, 14.6, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.1225, 28288923.7208566, 11787051.55035692, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 109.1721465, 0.00087448, 131.18963736, 0.00915144, 13.11896374, 0.0397237, -109.1721465, -0.00087448, -131.18963736, -0.00915144, -13.11896374, -0.0397237, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 122.34909522, 0.00087448, 147.02407114, 0.00915144, 14.70240711, 0.0397237, -122.34909522, -0.00087448, -147.02407114, -0.00915144, -14.70240711, -0.0397237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 142.36306888, 0.01748953, 142.36306888, 0.0524686, 99.65414822, -1683.43147532, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 35.59076722, 8.726e-05, 106.77230166, 0.00026177, 355.9076722, 0.00087257, -35.59076722, -8.726e-05, -106.77230166, -0.00026177, -355.9076722, -0.00087257, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 142.36306888, 0.01748953, 142.36306888, 0.0524686, 99.65414822, -1683.43147532, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 35.59076722, 8.726e-05, 106.77230166, 0.00026177, 355.9076722, 0.00087257, -35.59076722, -8.726e-05, -106.77230166, -0.00026177, -355.9076722, -0.00087257, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 18.45, 9.6, 6.15)
    ops.node(123022, 18.45, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.1225, 29721660.9941299, 12384025.41422079, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 130.31012961, 0.00089218, 156.07563642, 0.01053897, 15.60756364, 0.03785986, -130.31012961, -0.00089218, -156.07563642, -0.01053897, -15.60756364, -0.03785986, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 124.91289632, 0.00089218, 149.61123782, 0.01053897, 14.96112378, 0.03785986, -124.91289632, -0.00089218, -149.61123782, -0.01053897, -14.96112378, -0.03785986, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 146.38173554, 0.01784356, 146.38173554, 0.05353069, 102.46721488, -1618.29754064, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 36.59543388, 8.539e-05, 109.78630165, 0.00025618, 365.95433884, 0.00085395, -36.59543388, -8.539e-05, -109.78630165, -0.00025618, -365.95433884, -0.00085395, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 146.38173554, 0.01784356, 146.38173554, 0.05353069, 102.46721488, -1618.29754064, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 36.59543388, 8.539e-05, 109.78630165, 0.00025618, 365.95433884, 0.00085395, -36.59543388, -8.539e-05, -109.78630165, -0.00025618, -365.95433884, -0.00085395, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 22.3, 9.6, 6.15)
    ops.node(123023, 22.3, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 26109851.63553866, 10879104.84814111, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 138.01984761, 0.00092052, 165.28111959, 0.00846035, 16.52811196, 0.02923493, -138.01984761, -0.00092052, -165.28111959, -0.00846035, -16.52811196, -0.02923493, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 131.26608808, 0.00092052, 157.19337746, 0.00846035, 15.71933775, 0.02923493, -131.26608808, -0.00092052, -157.19337746, -0.00846035, -15.71933775, -0.02923493, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 128.82938756, 0.01841047, 128.82938756, 0.0552314, 90.18057129, -1536.14231536, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 32.20734689, 8.555e-05, 96.62204067, 0.00025666, 322.0734689, 0.00085552, -32.20734689, -8.555e-05, -96.62204067, -0.00025666, -322.0734689, -0.00085552, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 128.82938756, 0.01841047, 128.82938756, 0.0552314, 90.18057129, -1536.14231536, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 32.20734689, 8.555e-05, 96.62204067, 0.00025666, 322.0734689, 0.00085552, -32.20734689, -8.555e-05, -96.62204067, -0.00025666, -322.0734689, -0.00085552, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 26.15, 9.6, 6.15)
    ops.node(123024, 26.15, 9.6, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 30098005.68731456, 12540835.70304773, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 52.61947314, 0.00126513, 62.60894756, 0.01123692, 6.26089476, 0.04545574, -52.61947314, -0.00126513, -62.60894756, -0.01123692, -6.26089476, -0.04545574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 52.61947314, 0.00126513, 62.60894756, 0.01123692, 6.26089476, 0.04545574, -52.61947314, -0.00126513, -62.60894756, -0.01123692, -6.26089476, -0.04545574, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 101.33432659, 0.02530259, 101.33432659, 0.07590776, 70.93402861, -1423.66205953, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 25.33358165, 0.00011442, 76.00074494, 0.00034325, 253.33581647, 0.00114418, -25.33358165, -0.00011442, -76.00074494, -0.00034325, -253.33581647, -0.00114418, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 101.33432659, 0.02530259, 101.33432659, 0.07590776, 70.93402861, -1423.66205953, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 25.33358165, 0.00011442, 76.00074494, 0.00034325, 253.33581647, 0.00114418, -25.33358165, -0.00011442, -76.00074494, -0.00034325, -253.33581647, -0.00114418, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172025, 0.0, 14.4, 6.15)
    ops.node(123025, 0.0, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2025, 172025, 123025, 0.0625, 28852692.34581239, 12021955.1440885, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22025, 47.44309198, 0.00112134, 57.06563504, 0.01208316, 5.7065635, 0.05465479, -47.44309198, -0.00112134, -57.06563504, -0.01208316, -5.7065635, -0.05465479, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12025, 51.74131417, 0.00112134, 62.2356349, 0.01208316, 6.22356349, 0.05465479, -51.74131417, -0.00112134, -62.2356349, -0.01208316, -6.22356349, -0.05465479, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22025, 2025, 0.0, 86.0657774, 0.02242683, 86.0657774, 0.06728049, 60.24604418, -1232.01368676, 0.05, 2, 0, 72025, 23025, 2, 3)
    ops.uniaxialMaterial('LimitState', 42025, 21.51644435, 0.00010137, 64.54933305, 0.00030412, 215.16444349, 0.00101372, -21.51644435, -0.00010137, -64.54933305, -0.00030412, -215.16444349, -0.00101372, 0.4, 0.3, 0.003, 0.0, 0.0, 22025, 2)
    ops.limitCurve('ThreePoint', 12025, 2025, 0.0, 86.0657774, 0.02242683, 86.0657774, 0.06728049, 60.24604418, -1232.01368676, 0.05, 2, 0, 72025, 23025, 1, 3)
    ops.uniaxialMaterial('LimitState', 32025, 21.51644435, 0.00010137, 64.54933305, 0.00030412, 215.16444349, 0.00101372, -21.51644435, -0.00010137, -64.54933305, -0.00030412, -215.16444349, -0.00101372, 0.4, 0.3, 0.003, 0.0, 0.0, 12025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2025, 99999, 'P', 42025, 'Vy', 32025, 'Vz', 22025, 'My', 12025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172025, 72025, 172025, 2025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123025, 123025, 23025, 2025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172026, 3.85, 14.4, 6.15)
    ops.node(123026, 3.85, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2026, 172026, 123026, 0.0625, 29338774.27776011, 12224489.28240005, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22026, 66.92367665, 0.0011786, 79.71771325, 0.00989246, 7.97177133, 0.03862704, -66.92367665, -0.0011786, -79.71771325, -0.00989246, -7.97177133, -0.03862704, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12026, 66.92367665, 0.0011786, 79.71771325, 0.00989246, 7.97177133, 0.03862704, -66.92367665, -0.0011786, -79.71771325, -0.00989246, -7.97177133, -0.03862704, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22026, 2026, 0.0, 62.27422286, 0.02357209, 62.27422286, 0.07071626, 43.591956, -1068.12086656, 0.05, 2, 0, 72026, 23026, 2, 3)
    ops.uniaxialMaterial('LimitState', 42026, 15.56855572, 7.213e-05, 46.70566715, 0.0002164, 155.68555715, 0.00072134, -15.56855572, -7.213e-05, -46.70566715, -0.0002164, -155.68555715, -0.00072134, 0.4, 0.3, 0.003, 0.0, 0.0, 22026, 2)
    ops.limitCurve('ThreePoint', 12026, 2026, 0.0, 62.27422286, 0.02357209, 62.27422286, 0.07071626, 43.591956, -1068.12086656, 0.05, 2, 0, 72026, 23026, 1, 3)
    ops.uniaxialMaterial('LimitState', 32026, 15.56855572, 7.213e-05, 46.70566715, 0.0002164, 155.68555715, 0.00072134, -15.56855572, -7.213e-05, -46.70566715, -0.0002164, -155.68555715, -0.00072134, 0.4, 0.3, 0.003, 0.0, 0.0, 12026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2026, 99999, 'P', 42026, 'Vy', 32026, 'Vz', 22026, 'My', 12026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172026, 72026, 172026, 2026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123026, 123026, 23026, 2026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172027, 7.7, 14.4, 6.15)
    ops.node(123027, 7.7, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2027, 172027, 123027, 0.0625, 28975582.9105846, 12073159.54607692, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22027, 66.18633412, 0.00133438, 78.83952577, 0.0103173, 7.88395258, 0.03820806, -66.18633412, -0.00133438, -78.83952577, -0.0103173, -7.88395258, -0.03820806, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12027, 66.18633412, 0.00133438, 78.83952577, 0.0103173, 7.88395258, 0.03820806, -66.18633412, -0.00133438, -78.83952577, -0.0103173, -7.88395258, -0.03820806, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22027, 2027, 0.0, 69.77554633, 0.02668758, 69.77554633, 0.08006274, 48.84288243, -1125.54697186, 0.05, 2, 0, 72027, 23027, 2, 3)
    ops.uniaxialMaterial('LimitState', 42027, 17.44388658, 8.184e-05, 52.33165975, 0.00024551, 174.43886583, 0.00081836, -17.44388658, -8.184e-05, -52.33165975, -0.00024551, -174.43886583, -0.00081836, 0.4, 0.3, 0.003, 0.0, 0.0, 22027, 2)
    ops.limitCurve('ThreePoint', 12027, 2027, 0.0, 69.77554633, 0.02668758, 69.77554633, 0.08006274, 48.84288243, -1125.54697186, 0.05, 2, 0, 72027, 23027, 1, 3)
    ops.uniaxialMaterial('LimitState', 32027, 17.44388658, 8.184e-05, 52.33165975, 0.00024551, 174.43886583, 0.00081836, -17.44388658, -8.184e-05, -52.33165975, -0.00024551, -174.43886583, -0.00081836, 0.4, 0.3, 0.003, 0.0, 0.0, 12027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2027, 99999, 'P', 42027, 'Vy', 32027, 'Vz', 22027, 'My', 12027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172027, 72027, 172027, 2027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123027, 123027, 23027, 2027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172028, 11.55, 14.4, 6.15)
    ops.node(123028, 11.55, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2028, 172028, 123028, 0.0625, 28684934.03595847, 11952055.84831603, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22028, 54.80432216, 0.00117566, 65.47584449, 0.0101211, 6.54758445, 0.04446237, -54.80432216, -0.00117566, -65.47584449, -0.0101211, -6.54758445, -0.04446237, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12028, 59.13556071, 0.00117566, 70.65046377, 0.0101211, 7.06504638, 0.04446237, -59.13556071, -0.00117566, -70.65046377, -0.0101211, -7.06504638, -0.04446237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22028, 2028, 0.0, 86.82332078, 0.02351321, 86.82332078, 0.07053964, 60.77632455, -1196.72657251, 0.05, 2, 0, 72028, 23028, 2, 3)
    ops.uniaxialMaterial('LimitState', 42028, 21.7058302, 0.00010286, 65.11749059, 0.00030859, 217.05830195, 0.00102862, -21.7058302, -0.00010286, -65.11749059, -0.00030859, -217.05830195, -0.00102862, 0.4, 0.3, 0.003, 0.0, 0.0, 22028, 2)
    ops.limitCurve('ThreePoint', 12028, 2028, 0.0, 86.82332078, 0.02351321, 86.82332078, 0.07053964, 60.77632455, -1196.72657251, 0.05, 2, 0, 72028, 23028, 1, 3)
    ops.uniaxialMaterial('LimitState', 32028, 21.7058302, 0.00010286, 65.11749059, 0.00030859, 217.05830195, 0.00102862, -21.7058302, -0.00010286, -65.11749059, -0.00030859, -217.05830195, -0.00102862, 0.4, 0.3, 0.003, 0.0, 0.0, 12028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2028, 99999, 'P', 42028, 'Vy', 32028, 'Vz', 22028, 'My', 12028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172028, 72028, 172028, 2028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123028, 123028, 23028, 2028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172029, 14.6, 14.4, 6.15)
    ops.node(123029, 14.6, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2029, 172029, 123029, 0.0625, 29578212.84340128, 12324255.3514172, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22029, 54.13065691, 0.00120078, 64.65276034, 0.010048, 6.46527603, 0.04669052, -54.13065691, -0.00120078, -64.65276034, -0.010048, -6.46527603, -0.04669052, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12029, 58.02333652, 0.00120078, 69.30211241, 0.010048, 6.93021124, 0.04669052, -58.02333652, -0.00120078, -69.30211241, -0.010048, -6.93021124, -0.04669052, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22029, 2029, 0.0, 84.58881215, 0.02401563, 84.58881215, 0.0720469, 59.21216851, -1168.8224387, 0.05, 2, 0, 72029, 23029, 2, 3)
    ops.uniaxialMaterial('LimitState', 42029, 21.14720304, 9.719e-05, 63.44160911, 0.00029157, 211.47203038, 0.00097189, -21.14720304, -9.719e-05, -63.44160911, -0.00029157, -211.47203038, -0.00097189, 0.4, 0.3, 0.003, 0.0, 0.0, 22029, 2)
    ops.limitCurve('ThreePoint', 12029, 2029, 0.0, 84.58881215, 0.02401563, 84.58881215, 0.0720469, 59.21216851, -1168.8224387, 0.05, 2, 0, 72029, 23029, 1, 3)
    ops.uniaxialMaterial('LimitState', 32029, 21.14720304, 9.719e-05, 63.44160911, 0.00029157, 211.47203038, 0.00097189, -21.14720304, -9.719e-05, -63.44160911, -0.00029157, -211.47203038, -0.00097189, 0.4, 0.3, 0.003, 0.0, 0.0, 12029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2029, 99999, 'P', 42029, 'Vy', 32029, 'Vz', 22029, 'My', 12029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172029, 72029, 172029, 2029, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123029, 123029, 23029, 2029, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172030, 18.45, 14.4, 6.15)
    ops.node(123030, 18.45, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2030, 172030, 123030, 0.0625, 32946150.86175956, 13727562.85906648, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22030, 68.66029494, 0.00124882, 81.45520211, 0.01086816, 8.14552021, 0.04686723, -68.66029494, -0.00124882, -81.45520211, -0.01086816, -8.14552021, -0.04686723, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12030, 68.66029494, 0.00124882, 81.45520211, 0.01086816, 8.14552021, 0.04686723, -68.66029494, -0.00124882, -81.45520211, -0.01086816, -8.14552021, -0.04686723, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22030, 2030, 0.0, 80.07978447, 0.02497637, 80.07978447, 0.07492911, 56.05584913, -1112.71740457, 0.05, 2, 0, 72030, 23030, 2, 3)
    ops.uniaxialMaterial('LimitState', 42030, 20.01994612, 8.26e-05, 60.05983835, 0.00024781, 200.19946118, 0.00082602, -20.01994612, -8.26e-05, -60.05983835, -0.00024781, -200.19946118, -0.00082602, 0.4, 0.3, 0.003, 0.0, 0.0, 22030, 2)
    ops.limitCurve('ThreePoint', 12030, 2030, 0.0, 80.07978447, 0.02497637, 80.07978447, 0.07492911, 56.05584913, -1112.71740457, 0.05, 2, 0, 72030, 23030, 1, 3)
    ops.uniaxialMaterial('LimitState', 32030, 20.01994612, 8.26e-05, 60.05983835, 0.00024781, 200.19946118, 0.00082602, -20.01994612, -8.26e-05, -60.05983835, -0.00024781, -200.19946118, -0.00082602, 0.4, 0.3, 0.003, 0.0, 0.0, 12030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2030, 99999, 'P', 42030, 'Vy', 32030, 'Vz', 22030, 'My', 12030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172030, 72030, 172030, 2030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123030, 123030, 23030, 2030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172031, 22.3, 14.4, 6.15)
    ops.node(123031, 22.3, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2031, 172031, 123031, 0.0625, 27293166.79645327, 11372152.83185553, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22031, 66.3688384, 0.00124727, 78.96565196, 0.01099999, 7.8965652, 0.03472643, -66.3688384, -0.00124727, -78.96565196, -0.01099999, -7.8965652, -0.03472643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12031, 66.3688384, 0.00124727, 78.96565196, 0.01099999, 7.8965652, 0.03472643, -66.3688384, -0.00124727, -78.96565196, -0.01099999, -7.8965652, -0.03472643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22031, 2031, 0.0, 82.90904213, 0.02494542, 82.90904213, 0.07483626, 58.03632949, -1210.85690131, 0.05, 2, 0, 72031, 23031, 2, 3)
    ops.uniaxialMaterial('LimitState', 42031, 20.72726053, 0.00010323, 62.1817816, 0.0003097, 207.27260533, 0.00103234, -20.72726053, -0.00010323, -62.1817816, -0.0003097, -207.27260533, -0.00103234, 0.4, 0.3, 0.003, 0.0, 0.0, 22031, 2)
    ops.limitCurve('ThreePoint', 12031, 2031, 0.0, 82.90904213, 0.02494542, 82.90904213, 0.07483626, 58.03632949, -1210.85690131, 0.05, 2, 0, 72031, 23031, 1, 3)
    ops.uniaxialMaterial('LimitState', 32031, 20.72726053, 0.00010323, 62.1817816, 0.0003097, 207.27260533, 0.00103234, -20.72726053, -0.00010323, -62.1817816, -0.0003097, -207.27260533, -0.00103234, 0.4, 0.3, 0.003, 0.0, 0.0, 12031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2031, 99999, 'P', 42031, 'Vy', 32031, 'Vz', 22031, 'My', 12031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172031, 72031, 172031, 2031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123031, 123031, 23031, 2031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172032, 26.15, 14.4, 6.15)
    ops.node(123032, 26.15, 14.4, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2032, 172032, 123032, 0.0625, 28507066.29469013, 11877944.28945422, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22032, 46.2087999, 0.00115222, 55.59736919, 0.01235652, 5.55973692, 0.05414554, -46.2087999, -0.00115222, -55.59736919, -0.01235652, -5.55973692, -0.05414554, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12032, 50.01863523, 0.00115222, 60.18127576, 0.01235652, 6.01812758, 0.05414554, -50.01863523, -0.00115222, -60.18127576, -0.01235652, -6.01812758, -0.05414554, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22032, 2032, 0.0, 85.28381207, 0.02304447, 85.28381207, 0.06913342, 59.69866845, -1228.54826874, 0.05, 2, 0, 72032, 23032, 2, 3)
    ops.uniaxialMaterial('LimitState', 42032, 21.32095302, 0.00010167, 63.96285905, 0.00030501, 213.20953018, 0.00101669, -21.32095302, -0.00010167, -63.96285905, -0.00030501, -213.20953018, -0.00101669, 0.4, 0.3, 0.003, 0.0, 0.0, 22032, 2)
    ops.limitCurve('ThreePoint', 12032, 2032, 0.0, 85.28381207, 0.02304447, 85.28381207, 0.06913342, 59.69866845, -1228.54826874, 0.05, 2, 0, 72032, 23032, 1, 3)
    ops.uniaxialMaterial('LimitState', 32032, 21.32095302, 0.00010167, 63.96285905, 0.00030501, 213.20953018, 0.00101669, -21.32095302, -0.00010167, -63.96285905, -0.00030501, -213.20953018, -0.00101669, 0.4, 0.3, 0.003, 0.0, 0.0, 12032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2032, 99999, 'P', 42032, 'Vy', 32032, 'Vz', 22032, 'My', 12032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172032, 72032, 172032, 2032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123032, 123032, 23032, 2032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.1)
    ops.node(124001, 0.0, 0.0, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26457465.97396301, 11023944.15581792, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 27.08504883, 0.00102794, 33.02947486, 0.01438431, 3.30294749, 0.06826755, -27.08504883, -0.00102794, -33.02947486, -0.01438431, -3.30294749, -0.06826755, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 27.08504883, 0.00102794, 33.02947486, 0.01438431, 3.30294749, 0.06826755, -27.08504883, -0.00102794, -33.02947486, -0.01438431, -3.30294749, -0.06826755, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 72.39422719, 0.02055889, 72.39422719, 0.06167667, 50.67595903, -1590.10266964, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 18.0985568, 9.299e-05, 54.29567039, 0.00027897, 180.98556798, 0.00092989, -18.0985568, -9.299e-05, -54.29567039, -0.00027897, -180.98556798, -0.00092989, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 72.39422719, 0.02055889, 72.39422719, 0.06167667, 50.67595903, -1590.10266964, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 18.0985568, 9.299e-05, 54.29567039, 0.00027897, 180.98556798, 0.00092989, -18.0985568, -9.299e-05, -54.29567039, -0.00027897, -180.98556798, -0.00092989, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.85, 0.0, 9.1)
    ops.node(124002, 3.85, 0.0, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 30497822.19991756, 12707425.91663232, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 47.63495899, 0.00118818, 57.40686371, 0.01400481, 5.74068637, 0.05901064, -47.63495899, -0.00118818, -57.40686371, -0.01400481, -5.74068637, -0.05901064, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 47.63495899, 0.00118818, 57.40686371, 0.01400481, 5.74068637, 0.05901064, -47.63495899, -0.00118818, -57.40686371, -0.01400481, -5.74068637, -0.05901064, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 74.94494144, 0.0237635, 74.94494144, 0.0712905, 52.46145901, -1092.44907979, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 18.73623536, 8.351e-05, 56.20870608, 0.00025054, 187.36235359, 0.00083512, -18.73623536, -8.351e-05, -56.20870608, -0.00025054, -187.36235359, -0.00083512, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 74.94494144, 0.0237635, 74.94494144, 0.0712905, 52.46145901, -1092.44907979, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 18.73623536, 8.351e-05, 56.20870608, 0.00025054, 187.36235359, 0.00083512, -18.73623536, -8.351e-05, -56.20870608, -0.00025054, -187.36235359, -0.00083512, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.7, 0.0, 9.1)
    ops.node(124003, 7.7, 0.0, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0625, 30074904.86349335, 12531210.3597889, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 48.90191973, 0.00117119, 58.98488204, 0.01253491, 5.8984882, 0.05699862, -48.90191973, -0.00117119, -58.98488204, -0.01253491, -5.8984882, -0.05699862, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 48.90191973, 0.00117119, 58.98488204, 0.01253491, 5.8984882, 0.05699862, -48.90191973, -0.00117119, -58.98488204, -0.01253491, -5.8984882, -0.05699862, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 58.75165228, 0.02342382, 58.75165228, 0.07027147, 41.1261566, -969.31835113, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 14.68791307, 6.639e-05, 44.06373921, 0.00019916, 146.8791307, 0.00066388, -14.68791307, -6.639e-05, -44.06373921, -0.00019916, -146.8791307, -0.00066388, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 58.75165228, 0.02342382, 58.75165228, 0.07027147, 41.1261566, -969.31835113, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 14.68791307, 6.639e-05, 44.06373921, 0.00019916, 146.8791307, 0.00066388, -14.68791307, -6.639e-05, -44.06373921, -0.00019916, -146.8791307, -0.00066388, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 18.45, 0.0, 9.1)
    ops.node(124006, 18.45, 0.0, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 27992140.07958784, 11663391.69982827, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 46.50881835, 0.00121206, 56.28229192, 0.01391725, 5.62822919, 0.05529155, -46.50881835, -0.00121206, -56.28229192, -0.01391725, -5.62822919, -0.05529155, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 46.50881835, 0.00121206, 56.28229192, 0.01391725, 5.62822919, 0.05529155, -46.50881835, -0.00121206, -56.28229192, -0.01391725, -5.62822919, -0.05529155, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 68.1173564, 0.02424126, 68.1173564, 0.07272377, 47.68214948, -1079.71794587, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 17.0293391, 8.27e-05, 51.0880173, 0.00024809, 170.29339099, 0.00082698, -17.0293391, -8.27e-05, -51.0880173, -0.00024809, -170.29339099, -0.00082698, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 68.1173564, 0.02424126, 68.1173564, 0.07272377, 47.68214948, -1079.71794587, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 17.0293391, 8.27e-05, 51.0880173, 0.00024809, 170.29339099, 0.00082698, -17.0293391, -8.27e-05, -51.0880173, -0.00024809, -170.29339099, -0.00082698, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 22.3, 0.0, 9.1)
    ops.node(124007, 22.3, 0.0, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 28983819.67279368, 12076591.5303307, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 47.76489887, 0.00120564, 57.72456655, 0.01188871, 5.77245665, 0.05482617, -47.76489887, -0.00120564, -57.72456655, -0.01188871, -5.77245665, -0.05482617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 47.76489887, 0.00120564, 57.72456655, 0.01188871, 5.77245665, 0.05482617, -47.76489887, -0.00120564, -57.72456655, -0.01188871, -5.77245665, -0.05482617, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 49.31761162, 0.02411281, 49.31761162, 0.07233843, 34.52232813, -922.63310234, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 12.32940291, 5.783e-05, 36.98820872, 0.00017348, 123.29402905, 0.00057826, -12.32940291, -5.783e-05, -36.98820872, -0.00017348, -123.29402905, -0.00057826, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 49.31761162, 0.02411281, 49.31761162, 0.07233843, 34.52232813, -922.63310234, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 12.32940291, 5.783e-05, 36.98820872, 0.00017348, 123.29402905, 0.00057826, -12.32940291, -5.783e-05, -36.98820872, -0.00017348, -123.29402905, -0.00057826, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 26.15, 0.0, 9.1)
    ops.node(124008, 26.15, 0.0, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 30008327.53956894, 12503469.80815372, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 28.80457381, 0.00102207, 34.89519818, 0.01313233, 3.48951982, 0.07117769, -28.80457381, -0.00102207, -34.89519818, -0.01313233, -3.48951982, -0.07117769, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 28.80457381, 0.00102207, 34.89519818, 0.01313233, 3.48951982, 0.07117769, -28.80457381, -0.00102207, -34.89519818, -0.01313233, -3.48951982, -0.07117769, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 77.65682295, 0.02044135, 77.65682295, 0.06132404, 54.35977606, -1522.60889982, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 19.41420574, 8.795e-05, 58.24261721, 0.00026384, 194.14205737, 0.00087945, -19.41420574, -8.795e-05, -58.24261721, -0.00026384, -194.14205737, -0.00087945, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 77.65682295, 0.02044135, 77.65682295, 0.06132404, 54.35977606, -1522.60889982, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 19.41420574, 8.795e-05, 58.24261721, 0.00026384, 194.14205737, 0.00087945, -19.41420574, -8.795e-05, -58.24261721, -0.00026384, -194.14205737, -0.00087945, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 4.8, 9.1)
    ops.node(124009, 0.0, 4.8, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 30094446.48642823, 12539352.70267843, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 34.0900874, 0.00106755, 41.11385377, 0.01146163, 4.11138538, 0.06264309, -34.0900874, -0.00106755, -41.11385377, -0.01146163, -4.11138538, -0.06264309, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 34.0900874, 0.00106755, 41.11385377, 0.01146163, 4.11138538, 0.06264309, -34.0900874, -0.00106755, -41.11385377, -0.01146163, -4.11138538, -0.06264309, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 76.44024323, 0.02135108, 76.44024323, 0.06405324, 53.50817026, -1127.02720815, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 19.11006081, 8.632e-05, 57.33018242, 0.00025896, 191.10060808, 0.0008632, -19.11006081, -8.632e-05, -57.33018242, -0.00025896, -191.10060808, -0.0008632, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 76.44024323, 0.02135108, 76.44024323, 0.06405324, 53.50817026, -1127.02720815, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 19.11006081, 8.632e-05, 57.33018242, 0.00025896, 191.10060808, 0.0008632, -19.11006081, -8.632e-05, -57.33018242, -0.00025896, -191.10060808, -0.0008632, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 3.85, 4.8, 9.1)
    ops.node(124010, 3.85, 4.8, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 27721636.42604771, 11550681.84418655, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 101.32843223, 0.00084192, 122.84527913, 0.01061216, 12.28452791, 0.0440802, -101.32843223, -0.00084192, -122.84527913, -0.01061216, -12.28452791, -0.0440802, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 95.61472591, 0.00084192, 115.91828112, 0.01061216, 11.59182811, 0.0440802, -95.61472591, -0.00084192, -115.91828112, -0.01061216, -11.59182811, -0.0440802, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 116.55546157, 0.01683833, 116.55546157, 0.050515, 81.5888231, -1262.77452836, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 29.13886539, 7.29e-05, 87.41659618, 0.0002187, 291.38865392, 0.00072901, -29.13886539, -7.29e-05, -87.41659618, -0.0002187, -291.38865392, -0.00072901, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 116.55546157, 0.01683833, 116.55546157, 0.050515, 81.5888231, -1262.77452836, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 29.13886539, 7.29e-05, 87.41659618, 0.0002187, 291.38865392, 0.00072901, -29.13886539, -7.29e-05, -87.41659618, -0.0002187, -291.38865392, -0.00072901, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.7, 4.8, 9.1)
    ops.node(124011, 7.7, 4.8, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 31511334.20911921, 13129722.58713301, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 102.83071792, 0.00081598, 123.75832054, 0.01093254, 12.37583205, 0.04813329, -102.83071792, -0.00081598, -123.75832054, -0.01093254, -12.37583205, -0.04813329, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 96.98608543, 0.00081598, 116.72421716, 0.01093254, 11.67242172, 0.04813329, -96.98608543, -0.00081598, -116.72421716, -0.01093254, -11.67242172, -0.04813329, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 131.6618354, 0.01631961, 131.6618354, 0.04895883, 92.16328478, -1293.86800704, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 32.91545885, 7.245e-05, 98.74637655, 0.00021734, 329.1545885, 0.00072446, -32.91545885, -7.245e-05, -98.74637655, -0.00021734, -329.1545885, -0.00072446, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 131.6618354, 0.01631961, 131.6618354, 0.04895883, 92.16328478, -1293.86800704, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 32.91545885, 7.245e-05, 98.74637655, 0.00021734, 329.1545885, 0.00072446, -32.91545885, -7.245e-05, -98.74637655, -0.00021734, -329.1545885, -0.00072446, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 11.55, 4.8, 9.1)
    ops.node(124012, 11.55, 4.8, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 30731220.86119926, 12804675.35883303, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 96.34119138, 0.00081811, 116.29183979, 0.01081077, 11.62918398, 0.04852074, -96.34119138, -0.00081811, -116.29183979, -0.01081077, -11.62918398, -0.04852074, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 90.879611, 0.00081811, 109.69925752, 0.01081077, 10.96992575, 0.04852074, -90.879611, -0.00081811, -109.69925752, -0.01081077, -10.96992575, -0.04852074, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 126.4572909, 0.01636226, 126.4572909, 0.04908679, 88.52010363, -1304.60261911, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 31.61432272, 7.135e-05, 94.84296817, 0.00021404, 316.14322724, 0.00071348, -31.61432272, -7.135e-05, -94.84296817, -0.00021404, -316.14322724, -0.00071348, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 126.4572909, 0.01636226, 126.4572909, 0.04908679, 88.52010363, -1304.60261911, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 31.61432272, 7.135e-05, 94.84296817, 0.00021404, 316.14322724, 0.00071348, -31.61432272, -7.135e-05, -94.84296817, -0.00021404, -316.14322724, -0.00071348, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 14.6, 4.8, 9.1)
    ops.node(124013, 14.6, 4.8, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.1225, 27464014.03053401, 11443339.17938917, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 93.86515427, 0.00087981, 114.00326192, 0.01098082, 11.40032619, 0.04565189, -93.86515427, -0.00087981, -114.00326192, -0.01098082, -11.40032619, -0.04565189, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 89.02879194, 0.00087981, 108.12929212, 0.01098082, 10.81292921, 0.04565189, -89.02879194, -0.00087981, -108.12929212, -0.01098082, -10.81292921, -0.04565189, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 113.48040866, 0.01759621, 113.48040866, 0.05278863, 79.43628606, -1269.91262259, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 28.37010217, 7.164e-05, 85.1103065, 0.00021493, 283.70102166, 0.00071643, -28.37010217, -7.164e-05, -85.1103065, -0.00021493, -283.70102166, -0.00071643, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 113.48040866, 0.01759621, 113.48040866, 0.05278863, 79.43628606, -1269.91262259, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 28.37010217, 7.164e-05, 85.1103065, 0.00021493, 283.70102166, 0.00071643, -28.37010217, -7.164e-05, -85.1103065, -0.00021493, -283.70102166, -0.00071643, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 18.45, 4.8, 9.1)
    ops.node(124014, 18.45, 4.8, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1225, 31394325.75117134, 13080969.06298806, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 100.33608354, 0.00079399, 120.79245552, 0.01132687, 12.07924555, 0.04843562, -100.33608354, -0.00079399, -120.79245552, -0.01132687, -12.07924555, -0.04843562, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 94.65382391, 0.00079399, 113.95170522, 0.01132687, 11.39517052, 0.04843562, -94.65382391, -0.00079399, -113.95170522, -0.01132687, -11.39517052, -0.04843562, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 133.39366186, 0.01587973, 133.39366186, 0.04763918, 93.3755633, -1360.59463313, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 33.34841546, 7.367e-05, 100.04524639, 0.00022102, 333.48415464, 0.00073672, -33.34841546, -7.367e-05, -100.04524639, -0.00022102, -333.48415464, -0.00073672, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 133.39366186, 0.01587973, 133.39366186, 0.04763918, 93.3755633, -1360.59463313, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 33.34841546, 7.367e-05, 100.04524639, 0.00022102, 333.48415464, 0.00073672, -33.34841546, -7.367e-05, -100.04524639, -0.00022102, -333.48415464, -0.00073672, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 22.3, 4.8, 9.1)
    ops.node(124015, 22.3, 4.8, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 30556854.34638626, 12732022.64432761, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 99.87647319, 0.00083853, 120.48269268, 0.01198403, 12.04826927, 0.0483962, -99.87647319, -0.00083853, -120.48269268, -0.01198403, -12.04826927, -0.0483962, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 94.58760928, 0.00083853, 114.10264597, 0.01198403, 11.4102646, 0.0483962, -94.58760928, -0.00083853, -114.10264597, -0.01198403, -11.4102646, -0.0483962, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 133.54298068, 0.01677051, 133.54298068, 0.05031154, 93.48008648, -1466.01177883, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 33.38574517, 7.578e-05, 100.15723551, 0.00022733, 333.85745171, 0.00075776, -33.38574517, -7.578e-05, -100.15723551, -0.00022733, -333.85745171, -0.00075776, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 133.54298068, 0.01677051, 133.54298068, 0.05031154, 93.48008648, -1466.01177883, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 33.38574517, 7.578e-05, 100.15723551, 0.00022733, 333.85745171, 0.00075776, -33.38574517, -7.578e-05, -100.15723551, -0.00022733, -333.85745171, -0.00075776, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 26.15, 4.8, 9.1)
    ops.node(124016, 26.15, 4.8, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 30862593.77642816, 12859414.07351173, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 32.76443359, 0.00121227, 39.45099016, 0.01266962, 3.94509902, 0.06497045, -32.76443359, -0.00121227, -39.45099016, -0.01266962, -3.94509902, -0.06497045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 32.76443359, 0.00121227, 39.45099016, 0.01266962, 3.94509902, 0.06497045, -32.76443359, -0.00121227, -39.45099016, -0.01266962, -3.94509902, -0.06497045, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 85.57100132, 0.02424531, 85.57100132, 0.07273594, 59.89970092, -1281.06958964, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 21.39275033, 9.423e-05, 64.17825099, 0.00028268, 213.92750329, 0.00094226, -21.39275033, -9.423e-05, -64.17825099, -0.00028268, -213.92750329, -0.00094226, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 85.57100132, 0.02424531, 85.57100132, 0.07273594, 59.89970092, -1281.06958964, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 21.39275033, 9.423e-05, 64.17825099, 0.00028268, 213.92750329, 0.00094226, -21.39275033, -9.423e-05, -64.17825099, -0.00028268, -213.92750329, -0.00094226, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 9.6, 9.1)
    ops.node(124017, 0.0, 9.6, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 29544038.93459187, 12310016.22274661, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 35.69798773, 0.00111211, 43.10147031, 0.01268714, 4.31014703, 0.06314921, -35.69798773, -0.00111211, -43.10147031, -0.01268714, -4.31014703, -0.06314921, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 35.69798773, 0.00111211, 43.10147031, 0.01268714, 4.31014703, 0.06314921, -35.69798773, -0.00111211, -43.10147031, -0.01268714, -4.31014703, -0.06314921, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 83.42721825, 0.02224227, 83.42721825, 0.06672681, 58.39905278, -1303.58552962, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 20.85680456, 9.596e-05, 62.57041369, 0.00028789, 208.56804563, 0.00095965, -20.85680456, -9.596e-05, -62.57041369, -0.00028789, -208.56804563, -0.00095965, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 83.42721825, 0.02224227, 83.42721825, 0.06672681, 58.39905278, -1303.58552962, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 20.85680456, 9.596e-05, 62.57041369, 0.00028789, 208.56804563, 0.00095965, -20.85680456, -9.596e-05, -62.57041369, -0.00028789, -208.56804563, -0.00095965, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 3.85, 9.6, 9.1)
    ops.node(124018, 3.85, 9.6, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1225, 28027554.32497219, 11678147.63540508, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 100.02097153, 0.00086518, 121.22491708, 0.01155989, 12.12249171, 0.04549863, -100.02097153, -0.00086518, -121.22491708, -0.01155989, -12.12249171, -0.04549863, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 94.68717525, 0.00086518, 114.76038267, 0.01155989, 11.47603827, 0.04549863, -94.68717525, -0.00086518, -114.76038267, -0.01155989, -11.47603827, -0.04549863, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 121.21978851, 0.01730364, 121.21978851, 0.05191092, 84.85385196, -1376.85890191, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 30.30494713, 7.499e-05, 90.91484138, 0.00022497, 303.04947127, 0.00074991, -30.30494713, -7.499e-05, -90.91484138, -0.00022497, -303.04947127, -0.00074991, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 121.21978851, 0.01730364, 121.21978851, 0.05191092, 84.85385196, -1376.85890191, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 30.30494713, 7.499e-05, 90.91484138, 0.00022497, 303.04947127, 0.00074991, -30.30494713, -7.499e-05, -90.91484138, -0.00022497, -303.04947127, -0.00074991, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 7.7, 9.6, 9.1)
    ops.node(124019, 7.7, 9.6, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1225, 31913744.87390431, 13297393.69746013, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 103.65746691, 0.00081614, 124.62765253, 0.01153546, 12.46276525, 0.04911724, -103.65746691, -0.00081614, -124.62765253, -0.01153546, -12.46276525, -0.04911724, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 97.68523857, 0.00081614, 117.44722626, 0.01153546, 11.74472263, 0.04911724, -97.68523857, -0.00081614, -117.44722626, -0.01153546, -11.74472263, -0.04911724, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 138.76879692, 0.01632286, 138.76879692, 0.04896859, 97.13815784, -1473.3750251, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 34.69219923, 7.539e-05, 104.07659769, 0.00022618, 346.92199229, 0.00075393, -34.69219923, -7.539e-05, -104.07659769, -0.00022618, -346.92199229, -0.00075393, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 138.76879692, 0.01632286, 138.76879692, 0.04896859, 97.13815784, -1473.3750251, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 34.69219923, 7.539e-05, 104.07659769, 0.00022618, 346.92199229, 0.00075393, -34.69219923, -7.539e-05, -104.07659769, -0.00022618, -346.92199229, -0.00075393, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 11.55, 9.6, 9.1)
    ops.node(124020, 11.55, 9.6, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1225, 29764747.63168217, 12401978.17986757, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 86.2132667, 0.00082532, 104.28870823, 0.01192248, 10.42887082, 0.05391659, -86.2132667, -0.00082532, -104.28870823, -0.01192248, -10.42887082, -0.05391659, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 76.29449397, 0.00082532, 92.29036929, 0.01192248, 9.22903693, 0.05391659, -76.29449397, -0.00082532, -92.29036929, -0.01192248, -9.22903693, -0.05391659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 137.55810341, 0.01650637, 137.55810341, 0.04951912, 96.29067239, -1820.80242629, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 34.38952585, 8.013e-05, 103.16857756, 0.00024039, 343.89525853, 0.00080131, -34.38952585, -8.013e-05, -103.16857756, -0.00024039, -343.89525853, -0.00080131, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 137.55810341, 0.01650637, 137.55810341, 0.04951912, 96.29067239, -1820.80242629, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 34.38952585, 8.013e-05, 103.16857756, 0.00024039, 343.89525853, 0.00080131, -34.38952585, -8.013e-05, -103.16857756, -0.00024039, -343.89525853, -0.00080131, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 14.6, 9.6, 9.1)
    ops.node(124021, 14.6, 9.6, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.1225, 28663377.06654114, 11943073.77772548, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 90.205454, 0.00080758, 109.34915677, 0.01255489, 10.93491568, 0.05339623, -90.205454, -0.00080758, -109.34915677, -0.01255489, -10.93491568, -0.05339623, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 78.46138042, 0.00080758, 95.11271667, 0.01255489, 9.51127167, 0.05339623, -78.46138042, -0.00080758, -95.11271667, -0.01255489, -9.51127167, -0.05339623, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 135.56676835, 0.01615157, 135.56676835, 0.04845471, 94.89673784, -1900.00371515, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 33.89169209, 8.201e-05, 101.67507626, 0.00024602, 338.91692087, 0.00082006, -33.89169209, -8.201e-05, -101.67507626, -0.00024602, -338.91692087, -0.00082006, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 135.56676835, 0.01615157, 135.56676835, 0.04845471, 94.89673784, -1900.00371515, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 33.89169209, 8.201e-05, 101.67507626, 0.00024602, 338.91692087, 0.00082006, -33.89169209, -8.201e-05, -101.67507626, -0.00024602, -338.91692087, -0.00082006, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 18.45, 9.6, 9.1)
    ops.node(124022, 18.45, 9.6, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.1225, 28259953.11707816, 11774980.46544923, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 101.37381191, 0.00082257, 122.82455031, 0.01182817, 12.28245503, 0.04603538, -101.37381191, -0.00082257, -122.82455031, -0.01182817, -12.28245503, -0.04603538, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 95.49906084, 0.00082257, 115.70669961, 0.01182817, 11.57066996, 0.04603538, -95.49906084, -0.00082257, -115.70669961, -0.01182817, -11.57066996, -0.04603538, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 124.3663885, 0.01645146, 124.3663885, 0.04935439, 87.05647195, -1450.11514043, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 31.09159713, 7.63e-05, 93.27479138, 0.00022891, 310.91597126, 0.00076304, -31.09159713, -7.63e-05, -93.27479138, -0.00022891, -310.91597126, -0.00076304, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 124.3663885, 0.01645146, 124.3663885, 0.04935439, 87.05647195, -1450.11514043, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 31.09159713, 7.63e-05, 93.27479138, 0.00022891, 310.91597126, 0.00076304, -31.09159713, -7.63e-05, -93.27479138, -0.00022891, -310.91597126, -0.00076304, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 22.3, 9.6, 9.1)
    ops.node(124023, 22.3, 9.6, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 31857286.53821601, 13273869.39092334, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 102.11055612, 0.00087386, 122.7867541, 0.01219196, 12.27867541, 0.04973189, -102.11055612, -0.00087386, -122.7867541, -0.01219196, -12.27867541, -0.04973189, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 96.87036174, 0.00087386, 116.4854814, 0.01219196, 11.64854814, 0.04973189, -96.87036174, -0.00087386, -116.4854814, -0.01219196, -11.64854814, -0.04973189, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 140.66084438, 0.01747711, 140.66084438, 0.05243132, 98.46259107, -1542.54778928, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 35.16521109, 7.656e-05, 105.49563328, 0.00022967, 351.65211095, 0.00076557, -35.16521109, -7.656e-05, -105.49563328, -0.00022967, -351.65211095, -0.00076557, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 140.66084438, 0.01747711, 140.66084438, 0.05243132, 98.46259107, -1542.54778928, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 35.16521109, 7.656e-05, 105.49563328, 0.00022967, 351.65211095, 0.00076557, -35.16521109, -7.656e-05, -105.49563328, -0.00022967, -351.65211095, -0.00076557, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 26.15, 9.6, 9.1)
    ops.node(124024, 26.15, 9.6, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 28997101.49415643, 12082125.62256518, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 34.4523656, 0.00107521, 41.63548382, 0.01276854, 4.16354838, 0.06232225, -34.4523656, -0.00107521, -41.63548382, -0.01276854, -4.16354838, -0.06232225, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 34.4523656, 0.00107521, 41.63548382, 0.01276854, 4.16354838, 0.06232225, -34.4523656, -0.00107521, -41.63548382, -0.01276854, -4.16354838, -0.06232225, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 81.75568207, 0.02150428, 81.75568207, 0.06451283, 57.22897745, -1278.63072558, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 20.43892052, 9.582e-05, 61.31676155, 0.00028745, 204.38920518, 0.00095816, -20.43892052, -9.582e-05, -61.31676155, -0.00028745, -204.38920518, -0.00095816, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 81.75568207, 0.02150428, 81.75568207, 0.06451283, 57.22897745, -1278.63072558, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 20.43892052, 9.582e-05, 61.31676155, 0.00028745, 204.38920518, 0.00095816, -20.43892052, -9.582e-05, -61.31676155, -0.00028745, -204.38920518, -0.00095816, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173025, 0.0, 14.4, 9.1)
    ops.node(124025, 0.0, 14.4, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3025, 173025, 124025, 0.0625, 29529951.88257354, 12304146.61773898, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23025, 29.11740563, 0.00104949, 35.3137459, 0.0143387, 3.53137459, 0.07193025, -29.11740563, -0.00104949, -35.3137459, -0.0143387, -3.53137459, -0.07193025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13025, 29.11740563, 0.00104949, 35.3137459, 0.0143387, 3.53137459, 0.07193025, -29.11740563, -0.00104949, -35.3137459, -0.0143387, -3.53137459, -0.07193025, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23025, 3025, 0.0, 79.56747742, 0.02098982, 79.56747742, 0.06296945, 55.69723419, -1691.47904046, 0.05, 2, 0, 73025, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 43025, 19.89186936, 9.157e-05, 59.67560807, 0.00027471, 198.91869355, 0.00091569, -19.89186936, -9.157e-05, -59.67560807, -0.00027471, -198.91869355, -0.00091569, 0.4, 0.3, 0.003, 0.0, 0.0, 23025, 2)
    ops.limitCurve('ThreePoint', 13025, 3025, 0.0, 79.56747742, 0.02098982, 79.56747742, 0.06296945, 55.69723419, -1691.47904046, 0.05, 2, 0, 73025, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 33025, 19.89186936, 9.157e-05, 59.67560807, 0.00027471, 198.91869355, 0.00091569, -19.89186936, -9.157e-05, -59.67560807, -0.00027471, -198.91869355, -0.00091569, 0.4, 0.3, 0.003, 0.0, 0.0, 13025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3025, 99999, 'P', 43025, 'Vy', 33025, 'Vz', 23025, 'My', 13025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173025, 73025, 173025, 3025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 3025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173026, 3.85, 14.4, 9.1)
    ops.node(124026, 3.85, 14.4, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3026, 173026, 124026, 0.0625, 29840476.87872986, 12433532.03280411, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23026, 49.54742423, 0.00113618, 59.7905161, 0.01321792, 5.97905161, 0.05736962, -49.54742423, -0.00113618, -59.7905161, -0.01321792, -5.97905161, -0.05736962, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13026, 49.54742423, 0.00113618, 59.7905161, 0.01321792, 5.97905161, 0.05736962, -49.54742423, -0.00113618, -59.7905161, -0.01321792, -5.97905161, -0.05736962, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23026, 3026, 0.0, 65.26867445, 0.02272365, 65.26867445, 0.06817094, 45.68807211, -1014.8805853, 0.05, 2, 0, 73026, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 43026, 16.31716861, 7.433e-05, 48.95150584, 0.00022299, 163.17168612, 0.00074332, -16.31716861, -7.433e-05, -48.95150584, -0.00022299, -163.17168612, -0.00074332, 0.4, 0.3, 0.003, 0.0, 0.0, 23026, 2)
    ops.limitCurve('ThreePoint', 13026, 3026, 0.0, 65.26867445, 0.02272365, 65.26867445, 0.06817094, 45.68807211, -1014.8805853, 0.05, 2, 0, 73026, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 33026, 16.31716861, 7.433e-05, 48.95150584, 0.00022299, 163.17168612, 0.00074332, -16.31716861, -7.433e-05, -48.95150584, -0.00022299, -163.17168612, -0.00074332, 0.4, 0.3, 0.003, 0.0, 0.0, 13026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3026, 99999, 'P', 43026, 'Vy', 33026, 'Vz', 23026, 'My', 13026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173026, 73026, 173026, 3026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 3026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173027, 7.7, 14.4, 9.1)
    ops.node(124027, 7.7, 14.4, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3027, 173027, 124027, 0.0625, 31053670.81572603, 12939029.50655251, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23027, 49.29620253, 0.00118423, 59.33528133, 0.01261155, 5.93352813, 0.05829119, -49.29620253, -0.00118423, -59.33528133, -0.01261155, -5.93352813, -0.05829119, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13027, 49.29620253, 0.00118423, 59.33528133, 0.01261155, 5.93352813, 0.05829119, -49.29620253, -0.00118423, -59.33528133, -0.01261155, -5.93352813, -0.05829119, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23027, 3027, 0.0, 62.34965501, 0.02368467, 62.34965501, 0.071054, 43.6447585, -958.40264339, 0.05, 2, 0, 73027, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 43027, 15.58741375, 6.823e-05, 46.76224125, 0.0002047, 155.87413751, 0.00068233, -15.58741375, -6.823e-05, -46.76224125, -0.0002047, -155.87413751, -0.00068233, 0.4, 0.3, 0.003, 0.0, 0.0, 23027, 2)
    ops.limitCurve('ThreePoint', 13027, 3027, 0.0, 62.34965501, 0.02368467, 62.34965501, 0.071054, 43.6447585, -958.40264339, 0.05, 2, 0, 73027, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 33027, 15.58741375, 6.823e-05, 46.76224125, 0.0002047, 155.87413751, 0.00068233, -15.58741375, -6.823e-05, -46.76224125, -0.0002047, -155.87413751, -0.00068233, 0.4, 0.3, 0.003, 0.0, 0.0, 13027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3027, 99999, 'P', 43027, 'Vy', 33027, 'Vz', 23027, 'My', 13027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173027, 73027, 173027, 3027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 3027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173028, 11.55, 14.4, 9.1)
    ops.node(124028, 11.55, 14.4, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3028, 173028, 124028, 0.0625, 29911446.83995828, 12463102.84998262, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23028, 32.2587241, 0.00097618, 38.96665644, 0.01428788, 3.89666564, 0.06708083, -32.2587241, -0.00097618, -38.96665644, -0.01428788, -3.89666564, -0.06708083, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13028, 32.2587241, 0.00097618, 38.96665644, 0.01428788, 3.89666564, 0.06708083, -32.2587241, -0.00097618, -38.96665644, -0.01428788, -3.89666564, -0.06708083, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23028, 3028, 0.0, 86.30193477, 0.01952368, 86.30193477, 0.05857104, 60.41135434, -1496.72509608, 0.05, 2, 0, 73028, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 43028, 21.57548369, 9.805e-05, 64.72645108, 0.00029416, 215.75483692, 0.00098052, -21.57548369, -9.805e-05, -64.72645108, -0.00029416, -215.75483692, -0.00098052, 0.4, 0.3, 0.003, 0.0, 0.0, 23028, 2)
    ops.limitCurve('ThreePoint', 13028, 3028, 0.0, 86.30193477, 0.01952368, 86.30193477, 0.05857104, 60.41135434, -1496.72509608, 0.05, 2, 0, 73028, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 33028, 21.57548369, 9.805e-05, 64.72645108, 0.00029416, 215.75483692, 0.00098052, -21.57548369, -9.805e-05, -64.72645108, -0.00029416, -215.75483692, -0.00098052, 0.4, 0.3, 0.003, 0.0, 0.0, 13028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3028, 99999, 'P', 43028, 'Vy', 33028, 'Vz', 23028, 'My', 13028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173028, 73028, 173028, 3028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 3028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173029, 14.6, 14.4, 9.1)
    ops.node(124029, 14.6, 14.4, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3029, 173029, 124029, 0.0625, 27762106.93672669, 11567544.55696946, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23029, 33.87867967, 0.00108941, 41.06822259, 0.01313052, 4.10682226, 0.06250154, -33.87867967, -0.00108941, -41.06822259, -0.01313052, -4.10682226, -0.06250154, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13029, 33.87867967, 0.00108941, 41.06822259, 0.01313052, 4.10682226, 0.06250154, -33.87867967, -0.00108941, -41.06822259, -0.01313052, -4.10682226, -0.06250154, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23029, 3029, 0.0, 80.25896807, 0.02178829, 80.25896807, 0.06536488, 56.18127765, -1406.0359339, 0.05, 2, 0, 73029, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 43029, 20.06474202, 9.825e-05, 60.19422605, 0.00029474, 200.64742017, 0.00098246, -20.06474202, -9.825e-05, -60.19422605, -0.00029474, -200.64742017, -0.00098246, 0.4, 0.3, 0.003, 0.0, 0.0, 23029, 2)
    ops.limitCurve('ThreePoint', 13029, 3029, 0.0, 80.25896807, 0.02178829, 80.25896807, 0.06536488, 56.18127765, -1406.0359339, 0.05, 2, 0, 73029, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 33029, 20.06474202, 9.825e-05, 60.19422605, 0.00029474, 200.64742017, 0.00098246, -20.06474202, -9.825e-05, -60.19422605, -0.00029474, -200.64742017, -0.00098246, 0.4, 0.3, 0.003, 0.0, 0.0, 13029, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3029, 99999, 'P', 43029, 'Vy', 33029, 'Vz', 23029, 'My', 13029, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173029, 73029, 173029, 3029, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 3029, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173030, 18.45, 14.4, 9.1)
    ops.node(124030, 18.45, 14.4, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3030, 173030, 124030, 0.0625, 29760943.88531344, 12400393.28554727, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23030, 51.50359099, 0.0011419, 62.16033267, 0.01290988, 6.21603327, 0.05695381, -51.50359099, -0.0011419, -62.16033267, -0.01290988, -6.21603327, -0.05695381, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13030, 51.50359099, 0.0011419, 62.16033267, 0.01290988, 6.21603327, 0.05695381, -51.50359099, -0.0011419, -62.16033267, -0.01290988, -6.21603327, -0.05695381, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23030, 3030, 0.0, 63.94360057, 0.02283804, 63.94360057, 0.06851413, 44.7605204, -1018.77657508, 0.05, 2, 0, 73030, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 43030, 15.98590014, 7.302e-05, 47.95770043, 0.00021905, 159.85900142, 0.00073017, -15.98590014, -7.302e-05, -47.95770043, -0.00021905, -159.85900142, -0.00073017, 0.4, 0.3, 0.003, 0.0, 0.0, 23030, 2)
    ops.limitCurve('ThreePoint', 13030, 3030, 0.0, 63.94360057, 0.02283804, 63.94360057, 0.06851413, 44.7605204, -1018.77657508, 0.05, 2, 0, 73030, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 33030, 15.98590014, 7.302e-05, 47.95770043, 0.00021905, 159.85900142, 0.00073017, -15.98590014, -7.302e-05, -47.95770043, -0.00021905, -159.85900142, -0.00073017, 0.4, 0.3, 0.003, 0.0, 0.0, 13030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3030, 99999, 'P', 43030, 'Vy', 33030, 'Vz', 23030, 'My', 13030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173030, 73030, 173030, 3030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 3030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173031, 22.3, 14.4, 9.1)
    ops.node(124031, 22.3, 14.4, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3031, 173031, 124031, 0.0625, 29304337.85267856, 12210140.7719494, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23031, 47.60062847, 0.0011283, 57.49620526, 0.01377456, 5.74962053, 0.05718037, -47.60062847, -0.0011283, -57.49620526, -0.01377456, -5.74962053, -0.05718037, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13031, 47.60062847, 0.0011283, 57.49620526, 0.01377456, 5.74962053, 0.05718037, -47.60062847, -0.0011283, -57.49620526, -0.01377456, -5.74962053, -0.05718037, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23031, 3031, 0.0, 67.6374189, 0.02256594, 67.6374189, 0.06769783, 47.34619323, -1025.20793006, 0.05, 2, 0, 73031, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 43031, 16.90935473, 7.844e-05, 50.72806418, 0.00023532, 169.09354726, 0.00078439, -16.90935473, -7.844e-05, -50.72806418, -0.00023532, -169.09354726, -0.00078439, 0.4, 0.3, 0.003, 0.0, 0.0, 23031, 2)
    ops.limitCurve('ThreePoint', 13031, 3031, 0.0, 67.6374189, 0.02256594, 67.6374189, 0.06769783, 47.34619323, -1025.20793006, 0.05, 2, 0, 73031, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 33031, 16.90935473, 7.844e-05, 50.72806418, 0.00023532, 169.09354726, 0.00078439, -16.90935473, -7.844e-05, -50.72806418, -0.00023532, -169.09354726, -0.00078439, 0.4, 0.3, 0.003, 0.0, 0.0, 13031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3031, 99999, 'P', 43031, 'Vy', 33031, 'Vz', 23031, 'My', 13031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173031, 73031, 173031, 3031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 3031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173032, 26.15, 14.4, 9.1)
    ops.node(124032, 26.15, 14.4, 11.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3032, 173032, 124032, 0.0625, 29564452.73588933, 12318521.97328722, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23032, 28.17249026, 0.00097836, 34.16506528, 0.01304895, 3.41650653, 0.07067419, -28.17249026, -0.00097836, -34.16506528, -0.01304895, -3.41650653, -0.07067419, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13032, 28.17249026, 0.00097836, 34.16506528, 0.01304895, 3.41650653, 0.07067419, -28.17249026, -0.00097836, -34.16506528, -0.01304895, -3.41650653, -0.07067419, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23032, 3032, 0.0, 75.17873245, 0.01956721, 75.17873245, 0.05870164, 52.62511272, -1427.24569144, 0.05, 2, 0, 73032, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 43032, 18.79468311, 8.642e-05, 56.38404934, 0.00025925, 187.94683113, 0.00086417, -18.79468311, -8.642e-05, -56.38404934, -0.00025925, -187.94683113, -0.00086417, 0.4, 0.3, 0.003, 0.0, 0.0, 23032, 2)
    ops.limitCurve('ThreePoint', 13032, 3032, 0.0, 75.17873245, 0.01956721, 75.17873245, 0.05870164, 52.62511272, -1427.24569144, 0.05, 2, 0, 73032, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 33032, 18.79468311, 8.642e-05, 56.38404934, 0.00025925, 187.94683113, 0.00086417, -18.79468311, -8.642e-05, -56.38404934, -0.00025925, -187.94683113, -0.00086417, 0.4, 0.3, 0.003, 0.0, 0.0, 13032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3032, 99999, 'P', 43032, 'Vy', 33032, 'Vz', 23032, 'My', 13032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173032, 73032, 173032, 3032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 3032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 11.55, 0.0, 0.0)
    ops.node(124033, 11.55, 0.0, 1.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4085, 170004, 124033, 0.09, 30287389.23523812, 12619745.51468255, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24085, 144.90386465, 0.00077737, 171.2987911, 0.00868537, 17.12987911, 0.03038461, -144.90386465, -0.00077737, -171.2987911, -0.00868537, -17.12987911, -0.03038461, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14085, 130.75431019, 0.00077737, 154.57182816, 0.00868537, 15.45718282, 0.03038461, -130.75431019, -0.00077737, -154.57182816, -0.00868537, -15.45718282, -0.03038461, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24085, 4085, 0.0, 152.64769904, 0.0155474, 152.64769904, 0.04664219, 106.85338933, -3261.65947049, 0.05, 2, 0, 70004, 24033, 2, 3)
    ops.uniaxialMaterial('LimitState', 44085, 38.16192476, 5.947e-05, 114.48577428, 0.00017842, 381.61924759, 0.00059472, -38.16192476, -5.947e-05, -114.48577428, -0.00017842, -381.61924759, -0.00059472, 0.4, 0.3, 0.003, 0.0, 0.0, 24085, 2)
    ops.limitCurve('ThreePoint', 14085, 4085, 0.0, 152.64769904, 0.0155474, 152.64769904, 0.04664219, 106.85338933, -3261.65947049, 0.05, 2, 0, 70004, 24033, 1, 3)
    ops.uniaxialMaterial('LimitState', 34085, 38.16192476, 5.947e-05, 114.48577428, 0.00017842, 381.61924759, 0.00059472, -38.16192476, -5.947e-05, -114.48577428, -0.00017842, -381.61924759, -0.00059472, 0.4, 0.3, 0.003, 0.0, 0.0, 14085, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4085, 99999, 'P', 44085, 'Vy', 34085, 'Vz', 24085, 'My', 14085, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4085, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124033, 124033, 24033, 4085, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174033, 11.55, 0.0, 1.675)
    ops.node(121004, 11.55, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4086, 174033, 121004, 0.09, 28165173.87929891, 11735489.11637455, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24086, 110.76472708, 0.00074024, 131.03292993, 0.00784792, 13.10329299, 0.02643915, -110.76472708, -0.00074024, -131.03292993, -0.00784792, -13.10329299, -0.02643915, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14086, 110.76472708, 0.00074024, 131.03292993, 0.00784792, 13.10329299, 0.02643915, -110.76472708, -0.00074024, -131.03292993, -0.00784792, -13.10329299, -0.02643915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24086, 4086, 0.0, 141.46952665, 0.01480478, 141.46952665, 0.04441433, 99.02866865, -3131.8821354, 0.05, 2, 0, 74033, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44086, 35.36738166, 5.927e-05, 106.10214499, 0.00017781, 353.67381662, 0.0005927, -35.36738166, -5.927e-05, -106.10214499, -0.00017781, -353.67381662, -0.0005927, 0.4, 0.3, 0.003, 0.0, 0.0, 24086, 2)
    ops.limitCurve('ThreePoint', 14086, 4086, 0.0, 141.46952665, 0.01480478, 141.46952665, 0.04441433, 99.02866865, -3131.8821354, 0.05, 2, 0, 74033, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34086, 35.36738166, 5.927e-05, 106.10214499, 0.00017781, 353.67381662, 0.0005927, -35.36738166, -5.927e-05, -106.10214499, -0.00017781, -353.67381662, -0.0005927, 0.4, 0.3, 0.003, 0.0, 0.0, 14086, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4086, 99999, 'P', 44086, 'Vy', 34086, 'Vz', 24086, 'My', 14086, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174033, 74033, 174033, 4086, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4086, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 14.6, 0.0, 0.0)
    ops.node(124034, 14.6, 0.0, 1.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4087, 170005, 124034, 0.09, 27824764.82519826, 11593652.01049927, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24087, 148.39376866, 0.00076921, 174.97823767, 0.0090437, 17.49782377, 0.02549535, -148.39376866, -0.00076921, -174.97823767, -0.0090437, -17.49782377, -0.02549535, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14087, 132.05205656, 0.00076921, 155.70893809, 0.0090437, 15.57089381, 0.02549535, -132.05205656, -0.00076921, -155.70893809, -0.0090437, -15.57089381, -0.02549535, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24087, 4087, 0.0, 150.5864076, 0.01538426, 150.5864076, 0.04615277, 105.41048532, -3438.0787104, 0.05, 2, 0, 70005, 24034, 2, 3)
    ops.uniaxialMaterial('LimitState', 44087, 37.6466019, 6.386e-05, 112.9398057, 0.00019158, 376.46601899, 0.00063861, -37.6466019, -6.386e-05, -112.9398057, -0.00019158, -376.46601899, -0.00063861, 0.4, 0.3, 0.003, 0.0, 0.0, 24087, 2)
    ops.limitCurve('ThreePoint', 14087, 4087, 0.0, 150.5864076, 0.01538426, 150.5864076, 0.04615277, 105.41048532, -3438.0787104, 0.05, 2, 0, 70005, 24034, 1, 3)
    ops.uniaxialMaterial('LimitState', 34087, 37.6466019, 6.386e-05, 112.9398057, 0.00019158, 376.46601899, 0.00063861, -37.6466019, -6.386e-05, -112.9398057, -0.00019158, -376.46601899, -0.00063861, 0.4, 0.3, 0.003, 0.0, 0.0, 14087, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4087, 99999, 'P', 44087, 'Vy', 34087, 'Vz', 24087, 'My', 14087, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 4087, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124034, 124034, 24034, 4087, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174034, 14.6, 0.0, 1.675)
    ops.node(121005, 14.6, 0.0, 2.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4088, 174034, 121005, 0.09, 27274279.87850375, 11364283.2827099, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24088, 110.92077381, 0.00072902, 131.00533953, 0.00865253, 13.10053395, 0.02525195, -110.92077381, -0.00072902, -131.00533953, -0.00865253, -13.10053395, -0.02525195, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14088, 110.92077381, 0.00072902, 131.00533953, 0.00865253, 13.10053395, 0.02525195, -110.92077381, -0.00072902, -131.00533953, -0.00865253, -13.10053395, -0.02525195, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24088, 4088, 0.0, 144.64567829, 0.01458043, 144.64567829, 0.04374128, 101.2519748, -3284.43448382, 0.05, 2, 0, 74034, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44088, 36.16141957, 6.258e-05, 108.48425872, 0.00018774, 361.61419573, 0.0006258, -36.16141957, -6.258e-05, -108.48425872, -0.00018774, -361.61419573, -0.0006258, 0.4, 0.3, 0.003, 0.0, 0.0, 24088, 2)
    ops.limitCurve('ThreePoint', 14088, 4088, 0.0, 144.64567829, 0.01458043, 144.64567829, 0.04374128, 101.2519748, -3284.43448382, 0.05, 2, 0, 74034, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34088, 36.16141957, 6.258e-05, 108.48425872, 0.00018774, 361.61419573, 0.0006258, -36.16141957, -6.258e-05, -108.48425872, -0.00018774, -361.61419573, -0.0006258, 0.4, 0.3, 0.003, 0.0, 0.0, 14088, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4088, 99999, 'P', 44088, 'Vy', 34088, 'Vz', 24088, 'My', 14088, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174034, 74034, 174034, 4088, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 4088, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 11.55, 0.0, 3.2)
    ops.node(124035, 11.55, 0.0, 4.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4090, 171004, 124035, 0.09, 28312833.43157547, 11797013.92982311, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24090, 99.19153648, 0.00074162, 118.13735385, 0.00902402, 11.81373539, 0.03201983, -99.19153648, -0.00074162, -118.13735385, -0.00902402, -11.81373539, -0.03201983, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14090, 99.19153648, 0.00074162, 118.13735385, 0.00902402, 11.81373539, 0.03201983, -99.19153648, -0.00074162, -118.13735385, -0.00902402, -11.81373539, -0.03201983, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24090, 4090, 0.0, 137.79546444, 0.01483239, 137.79546444, 0.04449718, 96.45682511, -2853.94512328, 0.05, 2, 0, 71004, 24035, 2, 3)
    ops.uniaxialMaterial('LimitState', 44090, 34.44886611, 5.743e-05, 103.34659833, 0.00017229, 344.4886611, 0.00057429, -34.44886611, -5.743e-05, -103.34659833, -0.00017229, -344.4886611, -0.00057429, 0.4, 0.3, 0.003, 0.0, 0.0, 24090, 2)
    ops.limitCurve('ThreePoint', 14090, 4090, 0.0, 137.79546444, 0.01483239, 137.79546444, 0.04449718, 96.45682511, -2853.94512328, 0.05, 2, 0, 71004, 24035, 1, 3)
    ops.uniaxialMaterial('LimitState', 34090, 34.44886611, 5.743e-05, 103.34659833, 0.00017229, 344.4886611, 0.00057429, -34.44886611, -5.743e-05, -103.34659833, -0.00017229, -344.4886611, -0.00057429, 0.4, 0.3, 0.003, 0.0, 0.0, 14090, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4090, 99999, 'P', 44090, 'Vy', 34090, 'Vz', 24090, 'My', 14090, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4090, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124035, 124035, 24035, 4090, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174035, 11.55, 0.0, 4.65)
    ops.node(122004, 11.55, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4091, 174035, 122004, 0.09, 25542048.86927399, 10642520.3621975, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24091, 95.05182911, 0.00069842, 113.11186597, 0.00891758, 11.3111866, 0.027475, -95.05182911, -0.00069842, -113.11186597, -0.00891758, -11.3111866, -0.027475, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14091, 95.05182911, 0.00069842, 113.11186597, 0.00891758, 11.3111866, 0.027475, -95.05182911, -0.00069842, -113.11186597, -0.00891758, -11.3111866, -0.027475, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24091, 4091, 0.0, 125.84562428, 0.01396834, 125.84562428, 0.04190503, 88.091937, -2825.29359383, 0.05, 2, 0, 74035, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44091, 31.46140607, 5.814e-05, 94.38421821, 0.00017442, 314.6140607, 0.00058139, -31.46140607, -5.814e-05, -94.38421821, -0.00017442, -314.6140607, -0.00058139, 0.4, 0.3, 0.003, 0.0, 0.0, 24091, 2)
    ops.limitCurve('ThreePoint', 14091, 4091, 0.0, 125.84562428, 0.01396834, 125.84562428, 0.04190503, 88.091937, -2825.29359383, 0.05, 2, 0, 74035, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34091, 31.46140607, 5.814e-05, 94.38421821, 0.00017442, 314.6140607, 0.00058139, -31.46140607, -5.814e-05, -94.38421821, -0.00017442, -314.6140607, -0.00058139, 0.4, 0.3, 0.003, 0.0, 0.0, 14091, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4091, 99999, 'P', 44091, 'Vy', 34091, 'Vz', 24091, 'My', 14091, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174035, 74035, 174035, 4091, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4091, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 14.6, 0.0, 3.2)
    ops.node(124036, 14.6, 0.0, 4.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4092, 171005, 124036, 0.09, 29938928.05613865, 12474553.35672444, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24092, 102.15294788, 0.00070998, 121.66736071, 0.01055653, 12.16673607, 0.03685195, -102.15294788, -0.00070998, -121.66736071, -0.01055653, -12.16673607, -0.03685195, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14092, 102.15294788, 0.00070998, 121.66736071, 0.01055653, 12.16673607, 0.03685195, -102.15294788, -0.00070998, -121.66736071, -0.01055653, -12.16673607, -0.03685195, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24092, 4092, 0.0, 147.80094219, 0.0141995, 147.80094219, 0.04259851, 103.46065953, -3016.07711671, 0.05, 2, 0, 71005, 24036, 2, 3)
    ops.uniaxialMaterial('LimitState', 44092, 36.95023555, 5.825e-05, 110.85070664, 0.00017476, 369.50235546, 0.00058254, -36.95023555, -5.825e-05, -110.85070664, -0.00017476, -369.50235546, -0.00058254, 0.4, 0.3, 0.003, 0.0, 0.0, 24092, 2)
    ops.limitCurve('ThreePoint', 14092, 4092, 0.0, 147.80094219, 0.0141995, 147.80094219, 0.04259851, 103.46065953, -3016.07711671, 0.05, 2, 0, 71005, 24036, 1, 3)
    ops.uniaxialMaterial('LimitState', 34092, 36.95023555, 5.825e-05, 110.85070664, 0.00017476, 369.50235546, 0.00058254, -36.95023555, -5.825e-05, -110.85070664, -0.00017476, -369.50235546, -0.00058254, 0.4, 0.3, 0.003, 0.0, 0.0, 14092, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4092, 99999, 'P', 44092, 'Vy', 34092, 'Vz', 24092, 'My', 14092, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 4092, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124036, 124036, 24036, 4092, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174036, 14.6, 0.0, 4.65)
    ops.node(122005, 14.6, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4093, 174036, 122005, 0.09, 28418771.36843697, 11841154.73684874, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24093, 91.70112045, 0.00073709, 109.50203492, 0.01028369, 10.95020349, 0.03534628, -91.70112045, -0.00073709, -109.50203492, -0.01028369, -10.95020349, -0.03534628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14093, 91.70112045, 0.00073709, 109.50203492, 0.01028369, 10.95020349, 0.03534628, -91.70112045, -0.00073709, -109.50203492, -0.01028369, -10.95020349, -0.03534628, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24093, 4093, 0.0, 138.89097823, 0.01474189, 138.89097823, 0.04422566, 97.22368476, -2930.27322269, 0.05, 2, 0, 74036, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44093, 34.72274456, 5.767e-05, 104.16823367, 0.00017301, 347.22744558, 0.0005767, -34.72274456, -5.767e-05, -104.16823367, -0.00017301, -347.22744558, -0.0005767, 0.4, 0.3, 0.003, 0.0, 0.0, 24093, 2)
    ops.limitCurve('ThreePoint', 14093, 4093, 0.0, 138.89097823, 0.01474189, 138.89097823, 0.04422566, 97.22368476, -2930.27322269, 0.05, 2, 0, 74036, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34093, 34.72274456, 5.767e-05, 104.16823367, 0.00017301, 347.22744558, 0.0005767, -34.72274456, -5.767e-05, -104.16823367, -0.00017301, -347.22744558, -0.0005767, 0.4, 0.3, 0.003, 0.0, 0.0, 14093, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4093, 99999, 'P', 44093, 'Vy', 34093, 'Vz', 24093, 'My', 14093, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174036, 74036, 174036, 4093, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 4093, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 11.55, 0.0, 6.15)
    ops.node(124037, 11.55, 0.0, 7.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4095, 172004, 124037, 0.0625, 27828862.46290033, 11595359.3595418, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24095, 64.00610867, 0.00078662, 76.32743214, 0.00914762, 7.63274321, 0.03553328, -64.00610867, -0.00078662, -76.32743214, -0.00914762, -7.63274321, -0.03553328, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14095, 64.00610867, 0.00078662, 76.32743214, 0.00914762, 7.63274321, 0.03553328, -64.00610867, -0.00078662, -76.32743214, -0.00914762, -7.63274321, -0.03553328, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24095, 4095, 0.0, 59.80094234, 0.01573235, 59.80094234, 0.04719706, 41.86065964, -2054.13612971, 0.05, 2, 0, 72004, 24037, 2, 3)
    ops.uniaxialMaterial('LimitState', 44095, 14.95023558, 3.651e-05, 44.85070675, 0.00010954, 149.50235585, 0.00036514, -14.95023558, -3.651e-05, -44.85070675, -0.00010954, -149.50235585, -0.00036514, 0.4, 0.3, 0.003, 0.0, 0.0, 24095, 2)
    ops.limitCurve('ThreePoint', 14095, 4095, 0.0, 59.80094234, 0.01573235, 59.80094234, 0.04719706, 41.86065964, -2054.13612971, 0.05, 2, 0, 72004, 24037, 1, 3)
    ops.uniaxialMaterial('LimitState', 34095, 14.95023558, 3.651e-05, 44.85070675, 0.00010954, 149.50235585, 0.00036514, -14.95023558, -3.651e-05, -44.85070675, -0.00010954, -149.50235585, -0.00036514, 0.4, 0.3, 0.003, 0.0, 0.0, 14095, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4095, 99999, 'P', 44095, 'Vy', 34095, 'Vz', 24095, 'My', 14095, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4095, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124037, 124037, 24037, 4095, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174037, 11.55, 0.0, 7.575)
    ops.node(123004, 11.55, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4096, 174037, 123004, 0.0625, 27134812.25109316, 11306171.77128882, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24096, 61.31445763, 0.00082994, 73.41848751, 0.00924362, 7.34184875, 0.03761942, -61.31445763, -0.00082994, -73.41848751, -0.00924362, -7.34184875, -0.03761942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14096, 61.31445763, 0.00082994, 73.41848751, 0.00924362, 7.34184875, 0.03761942, -61.31445763, -0.00082994, -73.41848751, -0.00924362, -7.34184875, -0.03761942, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24096, 4096, 0.0, 54.90276748, 0.01659873, 54.90276748, 0.04979618, 38.43193723, -1930.98273453, 0.05, 2, 0, 74037, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44096, 13.72569187, 3.438e-05, 41.17707561, 0.00010314, 137.25691869, 0.0003438, -13.72569187, -3.438e-05, -41.17707561, -0.00010314, -137.25691869, -0.0003438, 0.4, 0.3, 0.003, 0.0, 0.0, 24096, 2)
    ops.limitCurve('ThreePoint', 14096, 4096, 0.0, 54.90276748, 0.01659873, 54.90276748, 0.04979618, 38.43193723, -1930.98273453, 0.05, 2, 0, 74037, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34096, 13.72569187, 3.438e-05, 41.17707561, 0.00010314, 137.25691869, 0.0003438, -13.72569187, -3.438e-05, -41.17707561, -0.00010314, -137.25691869, -0.0003438, 0.4, 0.3, 0.003, 0.0, 0.0, 14096, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4096, 99999, 'P', 44096, 'Vy', 34096, 'Vz', 24096, 'My', 14096, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174037, 74037, 174037, 4096, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4096, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 14.6, 0.0, 6.15)
    ops.node(124038, 14.6, 0.0, 7.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4097, 172005, 124038, 0.0625, 28361905.44655066, 11817460.60272944, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24097, 66.77602856, 0.00085361, 79.65230227, 0.01032133, 7.96523023, 0.03801303, -66.77602856, -0.00085361, -79.65230227, -0.01032133, -7.96523023, -0.03801303, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14097, 66.77602856, 0.00085361, 79.65230227, 0.01032133, 7.96523023, 0.03801303, -66.77602856, -0.00085361, -79.65230227, -0.01032133, -7.96523023, -0.03801303, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24097, 4097, 0.0, 79.92574699, 0.01707212, 79.92574699, 0.05121636, 55.94802289, -2295.81178137, 0.05, 2, 0, 72005, 24038, 2, 3)
    ops.uniaxialMaterial('LimitState', 44097, 19.98143675, 4.788e-05, 59.94431024, 0.00014365, 199.81436747, 0.00047885, -19.98143675, -4.788e-05, -59.94431024, -0.00014365, -199.81436747, -0.00047885, 0.4, 0.3, 0.003, 0.0, 0.0, 24097, 2)
    ops.limitCurve('ThreePoint', 14097, 4097, 0.0, 79.92574699, 0.01707212, 79.92574699, 0.05121636, 55.94802289, -2295.81178137, 0.05, 2, 0, 72005, 24038, 1, 3)
    ops.uniaxialMaterial('LimitState', 34097, 19.98143675, 4.788e-05, 59.94431024, 0.00014365, 199.81436747, 0.00047885, -19.98143675, -4.788e-05, -59.94431024, -0.00014365, -199.81436747, -0.00047885, 0.4, 0.3, 0.003, 0.0, 0.0, 14097, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4097, 99999, 'P', 44097, 'Vy', 34097, 'Vz', 24097, 'My', 14097, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 4097, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124038, 124038, 24038, 4097, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174038, 14.6, 0.0, 7.575)
    ops.node(123005, 14.6, 0.0, 8.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4098, 174038, 123005, 0.0625, 27993800.22407941, 11664083.42669975, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24098, 60.35716861, 0.00077853, 72.29326602, 0.0120464, 7.2293266, 0.0424982, -60.35716861, -0.00077853, -72.29326602, -0.0120464, -7.2293266, -0.0424982, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14098, 60.35716861, 0.00077853, 72.29326602, 0.0120464, 7.2293266, 0.0424982, -60.35716861, -0.00077853, -72.29326602, -0.0120464, -7.2293266, -0.0424982, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24098, 4098, 0.0, 88.36469985, 0.01557066, 88.36469985, 0.04671198, 61.85528989, -2367.0923544, 0.05, 2, 0, 74038, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44098, 22.09117496, 5.364e-05, 66.27352489, 0.00016091, 220.91174962, 0.00053637, -22.09117496, -5.364e-05, -66.27352489, -0.00016091, -220.91174962, -0.00053637, 0.4, 0.3, 0.003, 0.0, 0.0, 24098, 2)
    ops.limitCurve('ThreePoint', 14098, 4098, 0.0, 88.36469985, 0.01557066, 88.36469985, 0.04671198, 61.85528989, -2367.0923544, 0.05, 2, 0, 74038, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34098, 22.09117496, 5.364e-05, 66.27352489, 0.00016091, 220.91174962, 0.00053637, -22.09117496, -5.364e-05, -66.27352489, -0.00016091, -220.91174962, -0.00053637, 0.4, 0.3, 0.003, 0.0, 0.0, 14098, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4098, 99999, 'P', 44098, 'Vy', 34098, 'Vz', 24098, 'My', 14098, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174038, 74038, 174038, 4098, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 4098, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 11.55, 0.0, 9.1)
    ops.node(124039, 11.55, 0.0, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4100, 173004, 124039, 0.0625, 28371174.50627796, 11821322.71094915, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24100, 47.98029726, 0.00077061, 58.07997588, 0.01170719, 5.80799759, 0.05466215, -47.98029726, -0.00077061, -58.07997588, -0.01170719, -5.80799759, -0.05466215, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14100, 47.98029726, 0.00077061, 58.07997588, 0.01170719, 5.80799759, 0.05466215, -47.98029726, -0.00077061, -58.07997588, -0.01170719, -5.80799759, -0.05466215, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24100, 4100, 0.0, 52.41541308, 0.0154123, 52.41541308, 0.04623689, 36.69078916, -1818.44092311, 0.05, 2, 0, 73004, 24039, 2, 3)
    ops.uniaxialMaterial('LimitState', 44100, 13.10385327, 3.139e-05, 39.31155981, 9.418e-05, 131.03853271, 0.00031393, -13.10385327, -3.139e-05, -39.31155981, -9.418e-05, -131.03853271, -0.00031393, 0.4, 0.3, 0.003, 0.0, 0.0, 24100, 2)
    ops.limitCurve('ThreePoint', 14100, 4100, 0.0, 52.41541308, 0.0154123, 52.41541308, 0.04623689, 36.69078916, -1818.44092311, 0.05, 2, 0, 73004, 24039, 1, 3)
    ops.uniaxialMaterial('LimitState', 34100, 13.10385327, 3.139e-05, 39.31155981, 9.418e-05, 131.03853271, 0.00031393, -13.10385327, -3.139e-05, -39.31155981, -9.418e-05, -131.03853271, -0.00031393, 0.4, 0.3, 0.003, 0.0, 0.0, 14100, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4100, 99999, 'P', 44100, 'Vy', 34100, 'Vz', 24100, 'My', 14100, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4100, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124039, 124039, 24039, 4100, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174039, 11.55, 0.0, 10.525)
    ops.node(124004, 11.55, 0.0, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4101, 174039, 124004, 0.0625, 29225643.16337052, 12177351.31807105, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24101, 44.04309787, 0.00072909, 53.43681539, 0.0140284, 5.34368154, 0.06328128, -44.04309787, -0.00072909, -53.43681539, -0.0140284, -5.34368154, -0.06328128, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14101, 44.04309787, 0.00072909, 53.43681539, 0.0140284, 5.34368154, 0.06328128, -44.04309787, -0.00072909, -53.43681539, -0.0140284, -5.34368154, -0.06328128, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24101, 4101, 0.0, 65.91407228, 0.01458173, 65.91407228, 0.04374518, 46.1398506, -2359.18405356, 0.05, 2, 0, 74039, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44101, 16.47851807, 3.832e-05, 49.43555421, 0.00011497, 164.78518071, 0.00038323, -16.47851807, -3.832e-05, -49.43555421, -0.00011497, -164.78518071, -0.00038323, 0.4, 0.3, 0.003, 0.0, 0.0, 24101, 2)
    ops.limitCurve('ThreePoint', 14101, 4101, 0.0, 65.91407228, 0.01458173, 65.91407228, 0.04374518, 46.1398506, -2359.18405356, 0.05, 2, 0, 74039, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34101, 16.47851807, 3.832e-05, 49.43555421, 0.00011497, 164.78518071, 0.00038323, -16.47851807, -3.832e-05, -49.43555421, -0.00011497, -164.78518071, -0.00038323, 0.4, 0.3, 0.003, 0.0, 0.0, 14101, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4101, 99999, 'P', 44101, 'Vy', 34101, 'Vz', 24101, 'My', 14101, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174039, 74039, 174039, 4101, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4101, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 14.6, 0.0, 9.1)
    ops.node(124040, 14.6, 0.0, 10.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4102, 173005, 124040, 0.0625, 29571572.26192649, 12321488.44246937, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24102, 46.47052425, 0.00075041, 56.14233521, 0.01424051, 5.61423352, 0.05889626, -46.47052425, -0.00075041, -56.14233521, -0.01424051, -5.61423352, -0.05889626, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14102, 46.47052425, 0.00075041, 56.14233521, 0.01424051, 5.61423352, 0.05889626, -46.47052425, -0.00075041, -56.14233521, -0.01424051, -5.61423352, -0.05889626, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24102, 4102, 0.0, 80.53742289, 0.01500823, 80.53742289, 0.04502468, 56.37619602, -2308.75636473, 0.05, 2, 0, 73005, 24040, 2, 3)
    ops.uniaxialMaterial('LimitState', 44102, 20.13435572, 4.628e-05, 60.40306717, 0.00013883, 201.34355723, 0.00046277, -20.13435572, -4.628e-05, -60.40306717, -0.00013883, -201.34355723, -0.00046277, 0.4, 0.3, 0.003, 0.0, 0.0, 24102, 2)
    ops.limitCurve('ThreePoint', 14102, 4102, 0.0, 80.53742289, 0.01500823, 80.53742289, 0.04502468, 56.37619602, -2308.75636473, 0.05, 2, 0, 73005, 24040, 1, 3)
    ops.uniaxialMaterial('LimitState', 34102, 20.13435572, 4.628e-05, 60.40306717, 0.00013883, 201.34355723, 0.00046277, -20.13435572, -4.628e-05, -60.40306717, -0.00013883, -201.34355723, -0.00046277, 0.4, 0.3, 0.003, 0.0, 0.0, 14102, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4102, 99999, 'P', 44102, 'Vy', 34102, 'Vz', 24102, 'My', 14102, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 4102, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124040, 124040, 24040, 4102, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174040, 14.6, 0.0, 10.525)
    ops.node(124005, 14.6, 0.0, 11.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4103, 174040, 124005, 0.0625, 31196063.10076448, 12998359.62531853, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24103, 44.07741542, 0.00072199, 53.22085728, 0.0138805, 5.32208573, 0.06473938, -44.07741542, -0.00072199, -53.22085728, -0.0138805, -5.32208573, -0.06473938, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14103, 44.07741542, 0.00072199, 53.22085728, 0.0138805, 5.32208573, 0.06473938, -44.07741542, -0.00072199, -53.22085728, -0.0138805, -5.32208573, -0.06473938, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24103, 4103, 0.0, 72.97667739, 0.01443971, 72.97667739, 0.04331913, 51.08367417, -2623.38793356, 0.05, 2, 0, 74040, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44103, 18.24416935, 3.975e-05, 54.73250804, 0.00011925, 182.44169347, 0.00039749, -18.24416935, -3.975e-05, -54.73250804, -0.00011925, -182.44169347, -0.00039749, 0.4, 0.3, 0.003, 0.0, 0.0, 24103, 2)
    ops.limitCurve('ThreePoint', 14103, 4103, 0.0, 72.97667739, 0.01443971, 72.97667739, 0.04331913, 51.08367417, -2623.38793356, 0.05, 2, 0, 74040, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34103, 18.24416935, 3.975e-05, 54.73250804, 0.00011925, 182.44169347, 0.00039749, -18.24416935, -3.975e-05, -54.73250804, -0.00011925, -182.44169347, -0.00039749, 0.4, 0.3, 0.003, 0.0, 0.0, 14103, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4103, 99999, 'P', 44103, 'Vy', 34103, 'Vz', 24103, 'My', 14103, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174040, 74040, 174040, 4103, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 4103, '-orient', 0, 0, 1, 0, 1, 0)
