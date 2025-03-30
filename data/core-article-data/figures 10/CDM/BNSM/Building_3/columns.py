import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 26898838.63976858, 11207849.43323691, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 97.9309931, 0.00136747, 116.38593926, 0.01750404, 11.63859393, 0.04839874, -97.9309931, -0.00136747, -116.38593926, -0.01750404, -11.63859393, -0.04839874, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 97.9309931, 0.00136747, 116.38593926, 0.01750404, 11.63859393, 0.04839874, -97.9309931, -0.00136747, -116.38593926, -0.01750404, -11.63859393, -0.04839874, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 152.02377721, 0.02734939, 152.02377721, 0.08204817, 106.41664405, -2371.53884085, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 38.0059443, 0.00014016, 114.01783291, 0.00042049, 380.05944303, 0.00140162, -38.0059443, -0.00014016, -114.01783291, -0.00042049, -380.05944303, -0.00140162, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 152.02377721, 0.02734939, 152.02377721, 0.08204817, 106.41664405, -2371.53884085, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 38.0059443, 0.00014016, 114.01783291, 0.00042049, 380.05944303, 0.00140162, -38.0059443, -0.00014016, -114.01783291, -0.00042049, -380.05944303, -0.00140162, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.5, 0.0, 0.0)
    ops.node(121002, 4.5, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.1225, 28784066.61961821, 11993361.09150759, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 172.98754887, 0.00122287, 204.88777929, 0.01777818, 20.48877793, 0.04858316, -172.98754887, -0.00122287, -204.88777929, -0.01777818, -20.48877793, -0.04858316, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 186.69473972, 0.00122287, 221.12268123, 0.01777818, 22.11226812, 0.04858316, -186.69473972, -0.00122287, -221.12268123, -0.01777818, -22.11226812, -0.04858316, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 212.51321091, 0.02445734, 212.51321091, 0.07337201, 148.75924764, -3075.17901562, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 53.12830273, 0.00013452, 159.38490819, 0.00040356, 531.28302729, 0.00134522, -53.12830273, -0.00013452, -159.38490819, -0.00040356, -531.28302729, -0.00134522, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 212.51321091, 0.02445734, 212.51321091, 0.07337201, 148.75924764, -3075.17901562, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 53.12830273, 0.00013452, 159.38490819, 0.00040356, 531.28302729, 0.00134522, -53.12830273, -0.00013452, -159.38490819, -0.00040356, -531.28302729, -0.00134522, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.5, 0.0, 0.0)
    ops.node(121005, 16.5, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.1225, 27172996.85426216, 11322082.02260923, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 171.55967836, 0.00127539, 202.69266128, 0.01647087, 20.26926613, 0.04183548, -171.55967836, -0.00127539, -202.69266128, -0.01647087, -20.26926613, -0.04183548, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 185.08304342, 0.00127539, 218.67011519, 0.01647087, 21.86701152, 0.04183548, -185.08304342, -0.00127539, -218.67011519, -0.01647087, -21.86701152, -0.04183548, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 205.98355619, 0.02550776, 205.98355619, 0.07652329, 144.18848933, -3081.89338982, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 51.49588905, 0.00013812, 154.48766714, 0.00041436, 514.95889047, 0.00138119, -51.49588905, -0.00013812, -154.48766714, -0.00041436, -514.95889047, -0.00138119, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 205.98355619, 0.02550776, 205.98355619, 0.07652329, 144.18848933, -3081.89338982, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 51.49588905, 0.00013812, 154.48766714, 0.00041436, 514.95889047, 0.00138119, -51.49588905, -0.00013812, -154.48766714, -0.00041436, -514.95889047, -0.00138119, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 21.0, 0.0, 0.0)
    ops.node(121006, 21.0, 0.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.09, 26857474.88709472, 11190614.53628947, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 98.28867935, 0.00131512, 116.80278699, 0.01730306, 11.6802787, 0.04804627, -98.28867935, -0.00131512, -116.80278699, -0.01730306, -11.6802787, -0.04804627, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 98.28867935, 0.00131512, 116.80278699, 0.01730306, 11.6802787, 0.04804627, -98.28867935, -0.00131512, -116.80278699, -0.01730306, -11.6802787, -0.04804627, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 151.62398531, 0.02630234, 151.62398531, 0.07890702, 106.13678971, -2363.8756218, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 37.90599633, 0.00014001, 113.71798898, 0.00042003, 379.05996326, 0.00140009, -37.90599633, -0.00014001, -113.71798898, -0.00042003, -379.05996326, -0.00140009, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 151.62398531, 0.02630234, 151.62398531, 0.07890702, 106.13678971, -2363.8756218, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 37.90599633, 0.00014001, 113.71798898, 0.00042003, 379.05996326, 0.00140009, -37.90599633, -0.00014001, -113.71798898, -0.00042003, -379.05996326, -0.00140009, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.5, 0.0)
    ops.node(121007, 0.0, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 26748857.80889811, 11145357.42037421, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 177.39626093, 0.0011925, 209.39393183, 0.01595982, 20.93939318, 0.04390026, -177.39626093, -0.0011925, -209.39393183, -0.01595982, -20.93939318, -0.04390026, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 177.39626093, 0.0011925, 209.39393183, 0.01595982, 20.93939318, 0.04390026, -177.39626093, -0.0011925, -209.39393183, -0.01595982, -20.93939318, -0.04390026, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 222.35770709, 0.02384997, 222.35770709, 0.07154992, 155.65039496, -3545.59017506, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 55.58942677, 0.00015146, 166.76828031, 0.00045439, 555.89426771, 0.00151462, -55.58942677, -0.00015146, -166.76828031, -0.00045439, -555.89426771, -0.00151462, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 222.35770709, 0.02384997, 222.35770709, 0.07154992, 155.65039496, -3545.59017506, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 55.58942677, 0.00015146, 166.76828031, 0.00045439, 555.89426771, 0.00151462, -55.58942677, -0.00015146, -166.76828031, -0.00045439, -555.89426771, -0.00151462, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.5, 4.5, 0.0)
    ops.node(121008, 4.5, 4.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.2025, 27545697.34016842, 11477373.89173684, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 369.49772571, 0.00109074, 439.50452261, 0.02892598, 43.95045226, 0.06516702, -369.49772571, -0.00109074, -439.50452261, -0.02892598, -43.95045226, -0.06516702, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 386.14088128, 0.00109074, 459.30096961, 0.02892598, 45.93009696, 0.06516702, -386.14088128, -0.00109074, -459.30096961, -0.02892598, -45.93009696, -0.06516702, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 358.47283869, 0.02181485, 358.47283869, 0.06544456, 250.93098709, -5672.33175632, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 89.61820967, 0.00014344, 268.85462902, 0.00043032, 896.18209673, 0.0014344, -89.61820967, -0.00014344, -268.85462902, -0.00043032, -896.18209673, -0.0014344, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 358.47283869, 0.02181485, 358.47283869, 0.06544456, 250.93098709, -5672.33175632, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 89.61820967, 0.00014344, 268.85462902, 0.00043032, 896.18209673, 0.0014344, -89.61820967, -0.00014344, -268.85462902, -0.00043032, -896.18209673, -0.0014344, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
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
    ops.uniaxialMaterial('Hysteretic', 20009, 255.16225405, 0.00116456, 302.84685984, 0.02016984, 30.28468598, 0.04789819, -255.16225405, -0.00116456, -302.84685984, -0.02016984, -30.28468598, -0.04789819, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 269.51164673, 0.00116456, 319.87786048, 0.02016984, 31.98778605, 0.04789819, -269.51164673, -0.00116456, -319.87786048, -0.02016984, -31.98778605, -0.04789819, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 253.01639853, 0.02329117, 253.01639853, 0.0698735, 177.11147897, -3555.84728914, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 63.25409963, 0.00012592, 189.7622989, 0.00037775, 632.54099633, 0.00125917, -63.25409963, -0.00012592, -189.7622989, -0.00037775, -632.54099633, -0.00125917, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 253.01639853, 0.02329117, 253.01639853, 0.0698735, 177.11147897, -3555.84728914, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 63.25409963, 0.00012592, 189.7622989, 0.00037775, 632.54099633, 0.00125917, -63.25409963, -0.00012592, -189.7622989, -0.00037775, -632.54099633, -0.00125917, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
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
    ops.uniaxialMaterial('Hysteretic', 20010, 254.2117766, 0.00118239, 301.58382552, 0.02035743, 30.15838255, 0.04701587, -254.2117766, -0.00118239, -301.58382552, -0.02035743, -30.15838255, -0.04701587, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 268.33081275, 0.00118239, 318.33392653, 0.02035743, 31.83339265, 0.04701587, -268.33081275, -0.00118239, -318.33392653, -0.02035743, -31.83339265, -0.04701587, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 253.66539531, 0.02364779, 253.66539531, 0.07094337, 177.56577672, -3617.86815529, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 63.41634883, 0.00012785, 190.24904648, 0.00038354, 634.16348827, 0.00127847, -63.41634883, -0.00012785, -190.24904648, -0.00038354, -634.16348827, -0.00127847, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 253.66539531, 0.02364779, 253.66539531, 0.07094337, 177.56577672, -3617.86815529, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 63.41634883, 0.00012785, 190.24904648, 0.00038354, 634.16348827, 0.00127847, -63.41634883, -0.00012785, -190.24904648, -0.00038354, -634.16348827, -0.00127847, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 16.5, 4.5, 0.0)
    ops.node(121011, 16.5, 4.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 26799254.62172442, 11166356.09238518, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 367.21610637, 0.00108605, 436.30996984, 0.02790518, 43.63099698, 0.06119748, -367.21610637, -0.00108605, -436.30996984, -0.02790518, -43.63099698, -0.06119748, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 384.09598153, 0.00108605, 456.36589248, 0.02790518, 45.63658925, 0.06119748, -384.09598153, -0.00108605, -456.36589248, -0.02790518, -45.63658925, -0.06119748, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 351.25282518, 0.02172106, 351.25282518, 0.06516319, 245.87697763, -5608.62035438, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 87.8132063, 0.00014447, 263.43961889, 0.0004334, 878.13206295, 0.00144466, -87.8132063, -0.00014447, -263.43961889, -0.0004334, -878.13206295, -0.00144466, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 351.25282518, 0.02172106, 351.25282518, 0.06516319, 245.87697763, -5608.62035438, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 87.8132063, 0.00014447, 263.43961889, 0.0004334, 878.13206295, 0.00144466, -87.8132063, -0.00014447, -263.43961889, -0.0004334, -878.13206295, -0.00144466, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 21.0, 4.5, 0.0)
    ops.node(121012, 21.0, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 29006268.07102041, 12085945.02959184, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 180.35347046, 0.0011898, 213.66779745, 0.0181033, 21.36677974, 0.05495009, -180.35347046, -0.0011898, -213.66779745, -0.0181033, -21.36677974, -0.05495009, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 180.35347046, 0.0011898, 213.66779745, 0.0181033, 21.36677974, 0.05495009, -180.35347046, -0.0011898, -213.66779745, -0.0181033, -21.36677974, -0.05495009, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 236.72592057, 0.02379598, 236.72592057, 0.07138794, 165.7081444, -3674.85352126, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 59.18148014, 0.0001487, 177.54444042, 0.0004461, 591.81480142, 0.001487, -59.18148014, -0.0001487, -177.54444042, -0.0004461, -591.81480142, -0.001487, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 236.72592057, 0.02379598, 236.72592057, 0.07138794, 165.7081444, -3674.85352126, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 59.18148014, 0.0001487, 177.54444042, 0.0004461, 591.81480142, 0.001487, -59.18148014, -0.0001487, -177.54444042, -0.0004461, -591.81480142, -0.001487, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.1225, 27654151.24692437, 11522563.01955182, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 178.83691668, 0.00117063, 211.51614148, 0.01691168, 21.15161415, 0.04850188, -178.83691668, -0.00117063, -211.51614148, -0.01691168, -21.15161415, -0.04850188, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 178.83691668, 0.00117063, 211.51614148, 0.01691168, 21.15161415, 0.04850188, -178.83691668, -0.00117063, -211.51614148, -0.01691168, -21.15161415, -0.04850188, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 226.00741795, 0.02341264, 226.00741795, 0.07023793, 158.20519256, -3541.95564862, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 56.50185449, 0.00014891, 169.50556346, 0.00044673, 565.01854487, 0.00148909, -56.50185449, -0.00014891, -169.50556346, -0.00044673, -565.01854487, -0.00148909, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 226.00741795, 0.02341264, 226.00741795, 0.07023793, 158.20519256, -3541.95564862, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 56.50185449, 0.00014891, 169.50556346, 0.00044673, 565.01854487, 0.00148909, -56.50185449, -0.00014891, -169.50556346, -0.00044673, -565.01854487, -0.00148909, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.5, 9.0, 0.0)
    ops.node(121014, 4.5, 9.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.2025, 28360291.59943594, 11816788.16643164, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 365.38789911, 0.0010329, 434.92592907, 0.03016204, 43.49259291, 0.06949718, -365.38789911, -0.0010329, -434.92592907, -0.03016204, -43.49259291, -0.06949718, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 381.86703781, 0.0010329, 454.54126042, 0.03016204, 45.45412604, 0.06949718, -381.86703781, -0.0010329, -454.54126042, -0.03016204, -45.45412604, -0.06949718, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 367.31738129, 0.02065792, 367.31738129, 0.06197375, 257.1221669, -5768.35793323, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 91.82934532, 0.00014276, 275.48803597, 0.00042827, 918.29345323, 0.00142758, -91.82934532, -0.00014276, -275.48803597, -0.00042827, -918.29345323, -0.00142758, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 367.31738129, 0.02065792, 367.31738129, 0.06197375, 257.1221669, -5768.35793323, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 91.82934532, 0.00014276, 275.48803597, 0.00042827, 918.29345323, 0.00142758, -91.82934532, -0.00014276, -275.48803597, -0.00042827, -918.29345323, -0.00142758, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
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
    ops.uniaxialMaterial('Hysteretic', 20015, 282.28929181, 0.00119372, 334.85049874, 0.02060987, 33.48504987, 0.04718534, -282.28929181, -0.00119372, -334.85049874, -0.02060987, -33.48504987, -0.04718534, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 282.28929181, 0.00119372, 334.85049874, 0.02060987, 33.48504987, 0.04718534, -282.28929181, -0.00119372, -334.85049874, -0.02060987, -33.48504987, -0.04718534, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 255.39985754, 0.02387438, 255.39985754, 0.07162313, 178.77990028, -3657.22329452, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 63.84996438, 0.00012868, 191.54989315, 0.00038603, 638.49964385, 0.00128675, -63.84996438, -0.00012868, -191.54989315, -0.00038603, -638.49964385, -0.00128675, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 255.39985754, 0.02387438, 255.39985754, 0.07162313, 178.77990028, -3657.22329452, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 63.84996438, 0.00012868, 191.54989315, 0.00038603, 638.49964385, 0.00128675, -63.84996438, -0.00012868, -191.54989315, -0.00038603, -638.49964385, -0.00128675, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
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
    ops.uniaxialMaterial('Hysteretic', 20016, 281.60612765, 0.00117573, 334.01807448, 0.02037433, 33.40180745, 0.04680915, -281.60612765, -0.00117573, -334.01807448, -0.02037433, -33.40180745, -0.04680915, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 281.60612765, 0.00117573, 334.01807448, 0.02037433, 33.40180745, 0.04680915, -281.60612765, -0.00117573, -334.01807448, -0.02037433, -33.40180745, -0.04680915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 252.38918381, 0.02351457, 252.38918381, 0.07054371, 176.67242866, -3589.87854529, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 63.09729595, 0.00012737, 189.29188785, 0.00038211, 630.97295951, 0.00127369, -63.09729595, -0.00012737, -189.29188785, -0.00038211, -630.97295951, -0.00127369, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 252.38918381, 0.02351457, 252.38918381, 0.07054371, 176.67242866, -3589.87854529, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 63.09729595, 0.00012737, 189.29188785, 0.00038211, 630.97295951, 0.00127369, -63.09729595, -0.00012737, -189.29188785, -0.00038211, -630.97295951, -0.00127369, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 16.5, 9.0, 0.0)
    ops.node(121017, 16.5, 9.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.2025, 26526745.26979208, 11052810.52908003, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 370.74829742, 0.00109001, 440.27878027, 0.027946, 44.02787803, 0.06013793, -370.74829742, -0.00109001, -440.27878027, -0.027946, -44.02787803, -0.06013793, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 388.28885031, 0.00109001, 461.10890488, 0.027946, 46.11089049, 0.06013793, -388.28885031, -0.00109001, -461.10890488, -0.027946, -46.11089049, -0.06013793, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 354.312183, 0.02180021, 354.312183, 0.06540062, 248.0185281, -5746.93195572, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 88.57804575, 0.00014722, 265.73413725, 0.00044166, 885.78045749, 0.00147222, -88.57804575, -0.00014722, -265.73413725, -0.00044166, -885.78045749, -0.00147222, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 354.312183, 0.02180021, 354.312183, 0.06540062, 248.0185281, -5746.93195572, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 88.57804575, 0.00014722, 265.73413725, 0.00044166, 885.78045749, 0.00147222, -88.57804575, -0.00014722, -265.73413725, -0.00044166, -885.78045749, -0.00147222, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.1225, 27116138.99827383, 11298391.24928076, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 176.85868559, 0.00124923, 208.94767019, 0.01657737, 20.89476702, 0.04600783, -176.85868559, -0.00124923, -208.94767019, -0.01657737, -20.89476702, -0.04600783, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 176.85868559, 0.00124923, 208.94767019, 0.01657737, 20.89476702, 0.04600783, -176.85868559, -0.00124923, -208.94767019, -0.01657737, -20.89476702, -0.04600783, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 227.73450146, 0.02498462, 227.73450146, 0.07495386, 159.41415102, -3647.82995388, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 56.93362536, 0.00015302, 170.80087609, 0.00045907, 569.33625365, 0.00153024, -56.93362536, -0.00015302, -170.80087609, -0.00045907, -569.33625365, -0.00153024, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 227.73450146, 0.02498462, 227.73450146, 0.07495386, 159.41415102, -3647.82995388, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 56.93362536, 0.00015302, 170.80087609, 0.00045907, 569.33625365, 0.00153024, -56.93362536, -0.00015302, -170.80087609, -0.00045907, -569.33625365, -0.00153024, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.09, 27273317.43466929, 11363882.26444554, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 99.8036681, 0.00133069, 118.672838, 0.01718779, 11.8672838, 0.04938587, -99.8036681, -0.00133069, -118.672838, -0.01718779, -11.8672838, -0.04938587, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 99.8036681, 0.00133069, 118.672838, 0.01718779, 11.8672838, 0.04938587, -99.8036681, -0.00133069, -118.672838, -0.01718779, -11.8672838, -0.04938587, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 148.97703636, 0.02661383, 148.97703636, 0.0798415, 104.28392545, -2257.41998904, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 37.24425909, 0.00013547, 111.73277727, 0.0004064, 372.44259091, 0.00135467, -37.24425909, -0.00013547, -111.73277727, -0.0004064, -372.44259091, -0.00135467, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 148.97703636, 0.02661383, 148.97703636, 0.0798415, 104.28392545, -2257.41998904, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 37.24425909, 0.00013547, 111.73277727, 0.0004064, 372.44259091, 0.00135467, -37.24425909, -0.00013547, -111.73277727, -0.0004064, -372.44259091, -0.00135467, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 4.5, 13.5, 0.0)
    ops.node(121020, 4.5, 13.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.1225, 28008675.97558397, 11670281.65649332, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 173.71864095, 0.00128489, 205.54748592, 0.01741841, 20.55474859, 0.04557748, -173.71864095, -0.00128489, -205.54748592, -0.01741841, -20.55474859, -0.04557748, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 187.21278589, 0.00128489, 221.51403708, 0.01741841, 22.15140371, 0.04557748, -187.21278589, -0.00128489, -221.51403708, -0.01741841, -22.15140371, -0.04557748, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 211.11528385, 0.02569783, 211.11528385, 0.07709348, 147.78069869, -3121.01352432, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 52.77882096, 0.00013734, 158.33646288, 0.00041201, 527.78820961, 0.00137336, -52.77882096, -0.00013734, -158.33646288, -0.00041201, -527.78820961, -0.00137336, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 211.11528385, 0.02569783, 211.11528385, 0.07709348, 147.78069869, -3121.01352432, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 52.77882096, 0.00013734, 158.33646288, 0.00041201, 527.78820961, 0.00137336, -52.77882096, -0.00013734, -158.33646288, -0.00041201, -527.78820961, -0.00137336, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 9.0, 13.5, 0.0)
    ops.node(121021, 9.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.1225, 28630757.80382459, 11929482.41826025, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 168.01681279, 0.00123604, 199.76900551, 0.01837871, 19.97690055, 0.05251757, -168.01681279, -0.00123604, -199.76900551, -0.01837871, -19.97690055, -0.05251757, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 168.01681279, 0.00123604, 199.76900551, 0.01837871, 19.97690055, 0.05251757, -168.01681279, -0.00123604, -199.76900551, -0.01837871, -19.97690055, -0.05251757, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 204.15792245, 0.02472075, 204.15792245, 0.07416226, 142.91054571, -2937.44694563, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 51.03948061, 0.00012992, 153.11844184, 0.00038977, 510.39480612, 0.00129925, -51.03948061, -0.00012992, -153.11844184, -0.00038977, -510.39480612, -0.00129925, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 204.15792245, 0.02472075, 204.15792245, 0.07416226, 142.91054571, -2937.44694563, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 51.03948061, 0.00012992, 153.11844184, 0.00038977, 510.39480612, 0.00129925, -51.03948061, -0.00012992, -153.11844184, -0.00038977, -510.39480612, -0.00129925, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 12.0, 13.5, 0.0)
    ops.node(121022, 12.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.1225, 27564980.97164528, 11485408.73818554, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 169.66914552, 0.00124532, 201.53378293, 0.01793966, 20.15337829, 0.04852551, -169.66914552, -0.00124532, -201.53378293, -0.01793966, -20.15337829, -0.04852551, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 169.66914552, 0.00124532, 201.53378293, 0.01793966, 20.15337829, 0.04852551, -169.66914552, -0.00124532, -201.53378293, -0.01793966, -20.15337829, -0.04852551, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 203.15121653, 0.02490645, 203.15121653, 0.07471935, 142.20585157, -3024.87590268, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 50.78780413, 0.00013428, 152.3634124, 0.00040285, 507.87804134, 0.00134283, -50.78780413, -0.00013428, -152.3634124, -0.00040285, -507.87804134, -0.00134283, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 203.15121653, 0.02490645, 203.15121653, 0.07471935, 142.20585157, -3024.87590268, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 50.78780413, 0.00013428, 152.3634124, 0.00040285, 507.87804134, 0.00134283, -50.78780413, -0.00013428, -152.3634124, -0.00040285, -507.87804134, -0.00134283, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 16.5, 13.5, 0.0)
    ops.node(121023, 16.5, 13.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.1225, 27638218.3159765, 11515924.29832354, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 172.3177964, 0.00124801, 203.76385963, 0.01734227, 20.37638596, 0.04424236, -172.3177964, -0.00124801, -203.76385963, -0.01734227, -20.37638596, -0.04424236, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 186.11704172, 0.00124801, 220.08131229, 0.01734227, 22.00813123, 0.04424236, -186.11704172, -0.00124801, -220.08131229, -0.01734227, -22.00813123, -0.04424236, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 210.77923177, 0.02496027, 210.77923177, 0.07488082, 147.54546224, -3151.3871831, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 52.69480794, 0.00013896, 158.08442383, 0.00041687, 526.94807942, 0.00138956, -52.69480794, -0.00013896, -158.08442383, -0.00041687, -526.94807942, -0.00138956, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 210.77923177, 0.02496027, 210.77923177, 0.07488082, 147.54546224, -3151.3871831, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 52.69480794, 0.00013896, 158.08442383, 0.00041687, 526.94807942, 0.00138956, -52.69480794, -0.00013896, -158.08442383, -0.00041687, -526.94807942, -0.00138956, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.09, 26626109.20095151, 11094212.16706313, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 98.85891449, 0.00134919, 117.42355717, 0.01737352, 11.74235572, 0.04720886, -98.85891449, -0.00134919, -117.42355717, -0.01737352, -11.74235572, -0.04720886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 98.85891449, 0.00134919, 117.42355717, 0.01737352, 11.74235572, 0.04720886, -98.85891449, -0.00134919, -117.42355717, -0.01737352, -11.74235572, -0.04720886, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 151.06299937, 0.02698388, 151.06299937, 0.08095165, 105.74409956, -2366.23490464, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 37.76574984, 0.0001407, 113.29724953, 0.00042211, 377.65749842, 0.00140703, -37.76574984, -0.0001407, -113.29724953, -0.00042211, -377.65749842, -0.00140703, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 151.06299937, 0.02698388, 151.06299937, 0.08095165, 105.74409956, -2366.23490464, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 37.76574984, 0.0001407, 113.29724953, 0.00042211, 377.65749842, 0.00140703, -37.76574984, -0.0001407, -113.29724953, -0.00042211, -377.65749842, -0.00140703, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.325)
    ops.node(122001, 0.0, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 27953853.68422607, 11647439.0350942, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 86.61003734, 0.00119158, 103.83527812, 0.02021232, 10.38352781, 0.06343391, -86.61003734, -0.00119158, -103.83527812, -0.02021232, -10.38352781, -0.06343391, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 86.61003734, 0.00119158, 103.83527812, 0.02021232, 10.38352781, 0.06343391, -86.61003734, -0.00119158, -103.83527812, -0.02021232, -10.38352781, -0.06343391, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 147.11480284, 0.02383153, 147.11480284, 0.07149459, 102.98036198, -2591.67619072, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 36.77870071, 0.00011789, 110.33610213, 0.00035366, 367.78700709, 0.00117886, -36.77870071, -0.00011789, -110.33610213, -0.00035366, -367.78700709, -0.00117886, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 147.11480284, 0.02383153, 147.11480284, 0.07149459, 102.98036198, -2591.67619072, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 36.77870071, 0.00011789, 110.33610213, 0.00035366, 367.78700709, 0.00117886, -36.77870071, -0.00011789, -110.33610213, -0.00035366, -367.78700709, -0.00117886, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.5, 0.0, 3.375)
    ops.node(122002, 4.5, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.1225, 28628744.68578647, 11928643.6190777, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 158.14233698, 0.00115854, 188.79662693, 0.01964507, 18.87966269, 0.05818967, -158.14233698, -0.00115854, -188.79662693, -0.01964507, -18.87966269, -0.05818967, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 146.44196529, 0.00115854, 174.82825672, 0.01964507, 17.48282567, 0.05818967, -146.44196529, -0.00115854, -174.82825672, -0.01964507, -17.48282567, -0.05818967, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 200.1039604, 0.02317076, 200.1039604, 0.06951229, 140.07277228, -3239.37949814, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 50.0259901, 0.00011503, 150.0779703, 0.00034509, 500.259901, 0.00115029, -50.0259901, -0.00011503, -150.0779703, -0.00034509, -500.259901, -0.00115029, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 200.1039604, 0.02317076, 200.1039604, 0.06951229, 140.07277228, -3239.37949814, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 50.0259901, 0.00011503, 150.0779703, 0.00034509, 500.259901, 0.00115029, -50.0259901, -0.00011503, -150.0779703, -0.00034509, -500.259901, -0.00115029, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.5, 0.0, 3.375)
    ops.node(122005, 16.5, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.1225, 27044049.02779739, 11268353.76158225, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 162.00724485, 0.00116971, 193.22837405, 0.01903628, 19.32283741, 0.0523766, -162.00724485, -0.00116971, -193.22837405, -0.01903628, -19.32283741, -0.0523766, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 148.72229049, 0.00116971, 177.38321767, 0.01903628, 17.73832177, 0.0523766, -148.72229049, -0.00116971, -177.38321767, -0.01903628, -17.73832177, -0.0523766, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 195.63043878, 0.02339412, 195.63043878, 0.07018237, 136.94130715, -3296.15613172, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 48.9076097, 0.00011905, 146.72282909, 0.00035714, 489.07609695, 0.00119047, -48.9076097, -0.00011905, -146.72282909, -0.00035714, -489.07609695, -0.00119047, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 195.63043878, 0.02339412, 195.63043878, 0.07018237, 136.94130715, -3296.15613172, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 48.9076097, 0.00011905, 146.72282909, 0.00035714, 489.07609695, 0.00119047, -48.9076097, -0.00011905, -146.72282909, -0.00035714, -489.07609695, -0.00119047, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 21.0, 0.0, 3.325)
    ops.node(122006, 21.0, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.09, 25512085.31116219, 10630035.54631758, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 85.27469293, 0.00125057, 102.03984198, 0.01807071, 10.2039842, 0.05272815, -85.27469293, -0.00125057, -102.03984198, -0.01807071, -10.2039842, -0.05272815, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 85.27469293, 0.00125057, 102.03984198, 0.01807071, 10.2039842, 0.05272815, -85.27469293, -0.00125057, -102.03984198, -0.01807071, -10.2039842, -0.05272815, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 138.27113777, 0.02501145, 138.27113777, 0.07503435, 96.78979644, -2520.4326185, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 34.56778444, 0.0001214, 103.70335333, 0.00036421, 345.67784444, 0.00121404, -34.56778444, -0.0001214, -103.70335333, -0.00036421, -345.67784444, -0.00121404, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 138.27113777, 0.02501145, 138.27113777, 0.07503435, 96.78979644, -2520.4326185, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 34.56778444, 0.0001214, 103.70335333, 0.00036421, 345.67784444, 0.00121404, -34.56778444, -0.0001214, -103.70335333, -0.00036421, -345.67784444, -0.00121404, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.35)
    ops.node(122007, 0.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 27033776.53268033, 11264073.55528347, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 159.04591649, 0.00110637, 189.70367193, 0.01931325, 18.97036719, 0.05819946, -159.04591649, -0.00110637, -189.70367193, -0.01931325, -18.97036719, -0.05819946, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 146.38857425, 0.00110637, 174.60649526, 0.01931325, 17.46064953, 0.05819946, -146.38857425, -0.00110637, -174.60649526, -0.01931325, -17.46064953, -0.05819946, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 216.47514594, 0.02212731, 216.47514594, 0.06638194, 151.53260216, -3978.66209249, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 54.11878648, 0.00013178, 162.35635945, 0.00039535, 541.18786485, 0.00131782, -54.11878648, -0.00013178, -162.35635945, -0.00039535, -541.18786485, -0.00131782, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 216.47514594, 0.02212731, 216.47514594, 0.06638194, 151.53260216, -3978.66209249, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 54.11878648, 0.00013178, 162.35635945, 0.00039535, 541.18786485, 0.00131782, -54.11878648, -0.00013178, -162.35635945, -0.00039535, -541.18786485, -0.00131782, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.5, 4.5, 3.375)
    ops.node(122008, 4.5, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.2025, 28079293.07419134, 11699705.44757972, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 323.15797411, 0.00097059, 387.21303539, 0.02676036, 38.72130354, 0.06569306, -323.15797411, -0.00097059, -387.21303539, -0.02676036, -38.72130354, -0.06569306, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 291.86011615, 0.00097059, 349.71144313, 0.02676036, 34.97114431, 0.06569306, -291.86011615, -0.00097059, -349.71144313, -0.02676036, -34.97114431, -0.06569306, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 312.66986861, 0.01941184, 312.66986861, 0.05823552, 218.86890803, -4984.69038511, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 78.16746715, 0.00011086, 234.50240146, 0.00033257, 781.67467153, 0.00110858, -78.16746715, -0.00011086, -234.50240146, -0.00033257, -781.67467153, -0.00110858, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 312.66986861, 0.01941184, 312.66986861, 0.05823552, 218.86890803, -4984.69038511, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 78.16746715, 0.00011086, 234.50240146, 0.00033257, 781.67467153, 0.00110858, -78.16746715, -0.00011086, -234.50240146, -0.00033257, -781.67467153, -0.00110858, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
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
    ops.uniaxialMaterial('Hysteretic', 21009, 232.00444153, 0.00108649, 277.41151672, 0.02290376, 27.74115167, 0.05632939, -232.00444153, -0.00108649, -277.41151672, -0.02290376, -27.74115167, -0.05632939, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 219.02219928, 0.00108649, 261.88843669, 0.02290376, 26.18884367, 0.05632939, -219.02219928, -0.00108649, -261.88843669, -0.02290376, -26.18884367, -0.05632939, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 240.09269329, 0.02172984, 240.09269329, 0.06518952, 168.0648853, -3825.66777976, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 60.02317332, 0.00010975, 180.06951997, 0.00032924, 600.23173323, 0.00109747, -60.02317332, -0.00010975, -180.06951997, -0.00032924, -600.23173323, -0.00109747, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 240.09269329, 0.02172984, 240.09269329, 0.06518952, 168.0648853, -3825.66777976, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 60.02317332, 0.00010975, 180.06951997, 0.00032924, 600.23173323, 0.00109747, -60.02317332, -0.00010975, -180.06951997, -0.00032924, -600.23173323, -0.00109747, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
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
    ops.uniaxialMaterial('Hysteretic', 21010, 236.2461368, 0.00106722, 282.53269686, 0.02282486, 28.25326969, 0.05967572, -236.2461368, -0.00106722, -282.53269686, -0.02282486, -28.25326969, -0.05967572, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 222.83312658, 0.00106722, 266.49174058, 0.02282486, 26.64917406, 0.05967572, -222.83312658, -0.00106722, -266.49174058, -0.02282486, -26.64917406, -0.05967572, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 242.99548933, 0.02134443, 242.99548933, 0.06403329, 170.09684253, -3723.57422671, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 60.74887233, 0.00010638, 182.246617, 0.00031913, 607.48872333, 0.00106376, -60.74887233, -0.00010638, -182.246617, -0.00031913, -607.48872333, -0.00106376, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 242.99548933, 0.02134443, 242.99548933, 0.06403329, 170.09684253, -3723.57422671, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 60.74887233, 0.00010638, 182.246617, 0.00031913, 607.48872333, 0.00106376, -60.74887233, -0.00010638, -182.246617, -0.00031913, -607.48872333, -0.00106376, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 16.5, 4.5, 3.375)
    ops.node(122011, 16.5, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 26792909.71738459, 11163712.38224358, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 324.03891442, 0.00100217, 388.08158142, 0.02605139, 38.80815814, 0.06106438, -324.03891442, -0.00100217, -388.08158142, -0.02605139, -38.80815814, -0.06106438, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 292.1388004, 0.00100217, 349.87676667, 0.02605139, 34.98767667, 0.06106438, -292.1388004, -0.00100217, -349.87676667, -0.02605139, -34.98767667, -0.06106438, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 306.010893, 0.02004348, 306.010893, 0.06013045, 214.2076251, -5042.04721797, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 76.50272325, 0.00011371, 229.50816975, 0.00034112, 765.0272325, 0.00113706, -76.50272325, -0.00011371, -229.50816975, -0.00034112, -765.0272325, -0.00113706, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 306.010893, 0.02004348, 306.010893, 0.06013045, 214.2076251, -5042.04721797, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 76.50272325, 0.00011371, 229.50816975, 0.00034112, 765.0272325, 0.00113706, -76.50272325, -0.00011371, -229.50816975, -0.00034112, -765.0272325, -0.00113706, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.35)
    ops.node(122012, 21.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 28856030.86104837, 12023346.19210349, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 161.83491884, 0.00106897, 193.21274328, 0.01966975, 19.32127433, 0.06548008, -161.83491884, -0.00106897, -193.21274328, -0.01966975, -19.32127433, -0.06548008, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 148.75316901, 0.00106897, 177.5946011, 0.01966975, 17.75946011, 0.06548008, -148.75316901, -0.00106897, -177.5946011, -0.01966975, -17.75946011, -0.06548008, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 220.97143188, 0.02137946, 220.97143188, 0.06413837, 154.68000232, -3884.70380521, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 55.24285797, 0.00012602, 165.72857391, 0.00037807, 552.42857971, 0.00126024, -55.24285797, -0.00012602, -165.72857391, -0.00037807, -552.42857971, -0.00126024, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 220.97143188, 0.02137946, 220.97143188, 0.06413837, 154.68000232, -3884.70380521, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 55.24285797, 0.00012602, 165.72857391, 0.00037807, 552.42857971, 0.00126024, -55.24285797, -0.00012602, -165.72857391, -0.00037807, -552.42857971, -0.00126024, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.35)
    ops.node(122013, 0.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.1225, 27955671.33781418, 11648196.39075591, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 161.19381007, 0.00108015, 192.41144892, 0.01991228, 19.24114489, 0.06240445, -161.19381007, -0.00108015, -192.41144892, -0.01991228, -19.24114489, -0.06240445, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 148.03981067, 0.00108015, 176.709977, 0.01991228, 17.6709977, 0.06240445, -148.03981067, -0.00108015, -176.709977, -0.01991228, -17.6709977, -0.06240445, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 220.02582743, 0.02160309, 220.02582743, 0.06480926, 154.0180792, -3975.18408415, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 55.00645686, 0.00012953, 165.01937057, 0.00038858, 550.06456857, 0.00129526, -55.00645686, -0.00012953, -165.01937057, -0.00038858, -550.06456857, -0.00129526, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 220.02582743, 0.02160309, 220.02582743, 0.06480926, 154.0180792, -3975.18408415, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 55.00645686, 0.00012953, 165.01937057, 0.00038858, 550.06456857, 0.00129526, -55.00645686, -0.00012953, -165.01937057, -0.00038858, -550.06456857, -0.00129526, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.5, 9.0, 3.375)
    ops.node(122014, 4.5, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.2025, 29008495.31189958, 12086873.04662483, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 325.89151398, 0.00095552, 390.38124601, 0.0268787, 39.0381246, 0.06840524, -325.89151398, -0.00095552, -390.38124601, -0.0268787, -39.0381246, -0.06840524, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 294.2381208, 0.00095552, 352.46405412, 0.0268787, 35.24640541, 0.06840524, -294.2381208, -0.00095552, -352.46405412, -0.0268787, -35.24640541, -0.06840524, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 319.30355021, 0.01911035, 319.30355021, 0.05733105, 223.51248515, -4998.90904087, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 79.82588755, 0.00010958, 239.47766266, 0.00032875, 798.25887554, 0.00109583, -79.82588755, -0.00010958, -239.47766266, -0.00032875, -798.25887554, -0.00109583, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 319.30355021, 0.01911035, 319.30355021, 0.05733105, 223.51248515, -4998.90904087, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 79.82588755, 0.00010958, 239.47766266, 0.00032875, 798.25887554, 0.00109583, -79.82588755, -0.00010958, -239.47766266, -0.00032875, -798.25887554, -0.00109583, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
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
    ops.uniaxialMaterial('Hysteretic', 21015, 238.98250436, 0.00104774, 285.72676029, 0.02755824, 28.57267603, 0.07086426, -238.98250436, -0.00104774, -285.72676029, -0.02755824, -28.57267603, -0.07086426, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 225.10379183, 0.00104774, 269.13341352, 0.02755824, 26.91334135, 0.07086426, -225.10379183, -0.00104774, -269.13341352, -0.02755824, -26.91334135, -0.07086426, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 270.73740705, 0.02095483, 270.73740705, 0.06286448, 189.51618494, -4547.03746172, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 67.68435176, 0.00011751, 203.05305529, 0.00035254, 676.84351763, 0.00117512, -67.68435176, -0.00011751, -203.05305529, -0.00035254, -676.84351763, -0.00117512, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 270.73740705, 0.02095483, 270.73740705, 0.06286448, 189.51618494, -4547.03746172, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 67.68435176, 0.00011751, 203.05305529, 0.00035254, 676.84351763, 0.00117512, -67.68435176, -0.00011751, -203.05305529, -0.00035254, -676.84351763, -0.00117512, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
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
    ops.uniaxialMaterial('Hysteretic', 21016, 237.42319435, 0.00108038, 283.80069672, 0.02617165, 28.38006967, 0.06426878, -237.42319435, -0.00108038, -283.80069672, -0.02617165, -28.38006967, -0.06426878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 223.50347479, 0.00108038, 267.1619428, 0.02617165, 26.71619428, 0.06426878, -223.50347479, -0.00108038, -267.1619428, -0.02617165, -26.71619428, -0.06426878, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 258.35213662, 0.02160751, 258.35213662, 0.06482254, 180.84649563, -4411.44583414, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 64.58803416, 0.00011866, 193.76410247, 0.00035597, 645.88034155, 0.00118658, -64.58803416, -0.00011866, -193.76410247, -0.00035597, -645.88034155, -0.00118658, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 258.35213662, 0.02160751, 258.35213662, 0.06482254, 180.84649563, -4411.44583414, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 64.58803416, 0.00011866, 193.76410247, 0.00035597, 645.88034155, 0.00118658, -64.58803416, -0.00011866, -193.76410247, -0.00035597, -645.88034155, -0.00118658, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 16.5, 9.0, 3.375)
    ops.node(122017, 16.5, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.2025, 27768722.92370315, 11570301.21820965, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 326.85190397, 0.0009644, 391.63112234, 0.0267389, 39.16311223, 0.0647602, -326.85190397, -0.0009644, -391.63112234, -0.0267389, -39.16311223, -0.0647602, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 294.052531, 0.0009644, 352.33119753, 0.0267389, 35.23311975, 0.0647602, -294.052531, -0.0009644, -352.33119753, -0.0267389, -35.23311975, -0.0647602, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 314.84217544, 0.01928804, 314.84217544, 0.05786412, 220.38952281, -5121.85991621, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 78.71054386, 0.00011288, 236.13163158, 0.00033863, 787.10543859, 0.00112876, -78.71054386, -0.00011288, -236.13163158, -0.00033863, -787.10543859, -0.00112876, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 314.84217544, 0.01928804, 314.84217544, 0.05786412, 220.38952281, -5121.85991621, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 78.71054386, 0.00011288, 236.13163158, 0.00033863, 787.10543859, 0.00112876, -78.71054386, -0.00011288, -236.13163158, -0.00033863, -787.10543859, -0.00112876, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.35)
    ops.node(122018, 21.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.1225, 26302450.73382991, 10959354.47242913, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 158.50051806, 0.0011069, 188.85373461, 0.0184536, 18.88537346, 0.05434044, -158.50051806, -0.0011069, -188.85373461, -0.0184536, -18.88537346, -0.05434044, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 145.64312274, 0.0011069, 173.5341183, 0.0184536, 17.35341183, 0.05434044, -145.64312274, -0.0011069, -173.5341183, -0.0184536, -17.35341183, -0.05434044, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 212.8668308, 0.02213806, 212.8668308, 0.06641419, 149.00678156, -3953.31803575, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 53.2167077, 0.00013319, 159.6501231, 0.00039957, 532.16707701, 0.00133188, -53.2167077, -0.00013319, -159.6501231, -0.00039957, -532.16707701, -0.00133188, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 212.8668308, 0.02213806, 212.8668308, 0.06641419, 149.00678156, -3953.31803575, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 53.2167077, 0.00013319, 159.6501231, 0.00039957, 532.16707701, 0.00133188, -53.2167077, -0.00013319, -159.6501231, -0.00039957, -532.16707701, -0.00133188, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.325)
    ops.node(122019, 0.0, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.09, 27163065.73200557, 11317944.05500232, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 84.81468649, 0.00121378, 101.65899473, 0.01975625, 10.16589947, 0.06029908, -84.81468649, -0.00121378, -101.65899473, -0.01975625, -10.16589947, -0.06029908, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 84.81468649, 0.00121378, 101.65899473, 0.01975625, 10.16589947, 0.06029908, -84.81468649, -0.00121378, -101.65899473, -0.01975625, -10.16589947, -0.06029908, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 145.11363675, 0.02427556, 145.11363675, 0.07282667, 101.57954573, -2597.61133657, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 36.27840919, 0.00011967, 108.83522756, 0.000359, 362.78409188, 0.00119668, -36.27840919, -0.00011967, -108.83522756, -0.000359, -362.78409188, -0.00119668, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 145.11363675, 0.02427556, 145.11363675, 0.07282667, 101.57954573, -2597.61133657, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 36.27840919, 0.00011967, 108.83522756, 0.000359, 362.78409188, 0.00119668, -36.27840919, -0.00011967, -108.83522756, -0.000359, -362.78409188, -0.00119668, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 4.5, 13.5, 3.375)
    ops.node(122020, 4.5, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.1225, 27530551.63159758, 11471063.17983233, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 160.17201965, 0.00118996, 191.11446433, 0.01923645, 19.11144643, 0.05414464, -160.17201965, -0.00118996, -191.11446433, -0.01923645, -19.11144643, -0.05414464, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 147.85430863, 0.00118996, 176.41718606, 0.01923645, 17.64171861, 0.05414464, -147.85430863, -0.00118996, -176.41718606, -0.01923645, -17.64171861, -0.05414464, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 198.23275601, 0.02379919, 198.23275601, 0.07139756, 138.76292921, -3314.76918296, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 49.558189, 0.0001185, 148.67456701, 0.0003555, 495.58189002, 0.00118499, -49.558189, -0.0001185, -148.67456701, -0.0003555, -495.58189002, -0.00118499, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 198.23275601, 0.02379919, 198.23275601, 0.07139756, 138.76292921, -3314.76918296, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 49.558189, 0.0001185, 148.67456701, 0.0003555, 495.58189002, 0.00118499, -49.558189, -0.0001185, -148.67456701, -0.0003555, -495.58189002, -0.00118499, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.35)
    ops.node(122021, 9.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.1225, 27235052.5080971, 11347938.54504046, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 152.3927274, 0.00114276, 182.4303422, 0.0198151, 18.24303422, 0.05751352, -152.3927274, -0.00114276, -182.4303422, -0.0198151, -18.24303422, -0.05751352, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 139.47338337, 0.00114276, 166.96450999, 0.0198151, 16.696451, 0.05751352, -139.47338337, -0.00114276, -166.96450999, -0.0198151, -16.696451, -0.05751352, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 189.05560744, 0.0228552, 189.05560744, 0.06856559, 132.33892521, -3179.56444993, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 47.26390186, 0.00011424, 141.79170558, 0.00034272, 472.63901861, 0.00114239, -47.26390186, -0.00011424, -141.79170558, -0.00034272, -472.63901861, -0.00114239, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 189.05560744, 0.0228552, 189.05560744, 0.06856559, 132.33892521, -3179.56444993, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 47.26390186, 0.00011424, 141.79170558, 0.00034272, 472.63901861, 0.00114239, -47.26390186, -0.00011424, -141.79170558, -0.00034272, -472.63901861, -0.00114239, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.35)
    ops.node(122022, 12.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.1225, 27188516.90614583, 11328548.7108941, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 149.61604598, 0.00114195, 179.10132032, 0.02010895, 17.91013203, 0.05765334, -149.61604598, -0.00114195, -179.10132032, -0.02010895, -17.91013203, -0.05765334, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 137.38430504, 0.00114195, 164.4590342, 0.02010895, 16.44590342, 0.05765334, -137.38430504, -0.00114195, -164.4590342, -0.02010895, -16.44590342, -0.05765334, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 192.27922157, 0.022839, 192.27922157, 0.068517, 134.5954551, -3291.54656333, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 48.06980539, 0.00011639, 144.20941617, 0.00034916, 480.69805392, 0.00116386, -48.06980539, -0.00011639, -144.20941617, -0.00034916, -480.69805392, -0.00116386, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 192.27922157, 0.022839, 192.27922157, 0.068517, 134.5954551, -3291.54656333, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 48.06980539, 0.00011639, 144.20941617, 0.00034916, 480.69805392, 0.00116386, -48.06980539, -0.00011639, -144.20941617, -0.00034916, -480.69805392, -0.00116386, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 16.5, 13.5, 3.375)
    ops.node(122023, 16.5, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.1225, 27249079.16229182, 11353782.98428826, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 158.58372692, 0.00115248, 189.17082742, 0.01921815, 18.91708274, 0.05317483, -158.58372692, -0.00115248, -189.17082742, -0.01921815, -18.91708274, -0.05317483, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 146.13678511, 0.00115248, 174.32316097, 0.01921815, 17.4323161, 0.05317483, -146.13678511, -0.00115248, -174.32316097, -0.01921815, -17.4323161, -0.05317483, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 196.44074659, 0.02304951, 196.44074659, 0.06914852, 137.50852261, -3293.7427996, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 49.11018665, 0.00011864, 147.33055994, 0.00035592, 491.10186647, 0.00118641, -49.11018665, -0.00011864, -147.33055994, -0.00035592, -491.10186647, -0.00118641, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 196.44074659, 0.02304951, 196.44074659, 0.06914852, 137.50852261, -3293.7427996, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 49.11018665, 0.00011864, 147.33055994, 0.00035592, 491.10186647, 0.00118641, -49.11018665, -0.00011864, -147.33055994, -0.00035592, -491.10186647, -0.00118641, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.325)
    ops.node(122024, 21.0, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.09, 27234416.73607869, 11347673.64003279, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 87.07316403, 0.00118266, 104.3694017, 0.01946379, 10.43694017, 0.06024876, -87.07316403, -0.00118266, -104.3694017, -0.01946379, -10.43694017, -0.06024876, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 87.07316403, 0.00118266, 104.3694017, 0.01946379, 10.43694017, 0.06024876, -87.07316403, -0.00118266, -104.3694017, -0.01946379, -10.43694017, -0.06024876, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 144.12782787, 0.02365314, 144.12782787, 0.07095941, 100.88947951, -2555.83660623, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 36.03195697, 0.00011854, 108.0958709, 0.00035563, 360.31956967, 0.00118544, -36.03195697, -0.00011854, -108.0958709, -0.00035563, -360.31956967, -0.00118544, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 144.12782787, 0.02365314, 144.12782787, 0.07095941, 100.88947951, -2555.83660623, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 36.03195697, 0.00011854, 108.0958709, 0.00035563, 360.31956967, 0.00118544, -36.03195697, -0.00011854, -108.0958709, -0.00035563, -360.31956967, -0.00118544, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.125)
    ops.node(123001, 0.0, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.09, 27394704.3141698, 11414460.13090408, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 78.13225263, 0.00118132, 94.39898389, 0.02281358, 9.43989839, 0.07507699, -78.13225263, -0.00118132, -94.39898389, -0.02281358, -9.43989839, -0.07507699, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 82.75704043, 0.00118132, 99.98662862, 0.02281358, 9.99866286, 0.07507699, -82.75704043, -0.00118132, -99.98662862, -0.02281358, -9.99866286, -0.07507699, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 138.5375876, 0.02362647, 138.5375876, 0.0708794, 96.97631132, -2832.69964262, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 34.6343969, 0.00011328, 103.9031907, 0.00033984, 346.343969, 0.00113279, -34.6343969, -0.00011328, -103.9031907, -0.00033984, -346.343969, -0.00113279, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 138.5375876, 0.02362647, 138.5375876, 0.0708794, 96.97631132, -2832.69964262, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 34.6343969, 0.00011328, 103.9031907, 0.00033984, 346.343969, 0.00113279, -34.6343969, -0.00011328, -103.9031907, -0.00033984, -346.343969, -0.00113279, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.5, 0.0, 6.15)
    ops.node(123002, 4.5, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.09, 27609203.64950449, 11503834.8539602, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 99.35111587, 0.00130965, 118.88039328, 0.01974571, 11.88803933, 0.05399763, -99.35111587, -0.00130965, -118.88039328, -0.01974571, -11.88803933, -0.05399763, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 94.46714857, 0.00130965, 113.03639296, 0.01974571, 11.3036393, 0.05399763, -94.46714857, -0.00130965, -113.03639296, -0.01974571, -11.3036393, -0.05399763, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 135.32485563, 0.02619299, 135.32485563, 0.07857896, 94.72739894, -2171.79246531, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 33.83121391, 0.00010979, 101.49364172, 0.00032938, 338.31213907, 0.00109792, -33.83121391, -0.00010979, -101.49364172, -0.00032938, -338.31213907, -0.00109792, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 135.32485563, 0.02619299, 135.32485563, 0.07857896, 94.72739894, -2171.79246531, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 33.83121391, 0.00010979, 101.49364172, 0.00032938, 338.31213907, 0.00109792, -33.83121391, -0.00010979, -101.49364172, -0.00032938, -338.31213907, -0.00109792, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.5, 0.0, 6.15)
    ops.node(123005, 16.5, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.09, 26470196.99939074, 11029248.74974614, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 102.48677901, 0.0013437, 122.5195542, 0.0184717, 12.25195542, 0.0492795, -102.48677901, -0.0013437, -122.5195542, -0.0184717, -12.25195542, -0.0492795, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 97.02503312, 0.0013437, 115.99021765, 0.0184717, 11.59902177, 0.0492795, -97.02503312, -0.0013437, -115.99021765, -0.0184717, -11.59902177, -0.0492795, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 129.55945064, 0.02687393, 129.55945064, 0.08062178, 90.69161545, -2094.00724662, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 32.38986266, 0.00010964, 97.16958798, 0.00032891, 323.8986266, 0.00109638, -32.38986266, -0.00010964, -97.16958798, -0.00032891, -323.8986266, -0.00109638, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 129.55945064, 0.02687393, 129.55945064, 0.08062178, 90.69161545, -2094.00724662, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 32.38986266, 0.00010964, 97.16958798, 0.00032891, 323.8986266, 0.00109638, -32.38986266, -0.00010964, -97.16958798, -0.00032891, -323.8986266, -0.00109638, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 21.0, 0.0, 6.125)
    ops.node(123006, 21.0, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.09, 28430402.01538608, 11846000.8397442, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 80.51630278, 0.00113836, 97.19176895, 0.02206657, 9.71917689, 0.07701148, -80.51630278, -0.00113836, -97.19176895, -0.02206657, -9.71917689, -0.07701148, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 85.66410153, 0.00113836, 103.40571133, 0.02206657, 10.34057113, 0.07701148, -85.66410153, -0.00113836, -103.40571133, -0.02206657, -10.34057113, -0.07701148, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 136.79972724, 0.02276716, 136.79972724, 0.06830149, 95.75980907, -2628.31681713, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 34.19993181, 0.00010778, 102.59979543, 0.00032335, 341.9993181, 0.00107783, -34.19993181, -0.00010778, -102.59979543, -0.00032335, -341.9993181, -0.00107783, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 136.79972724, 0.02276716, 136.79972724, 0.06830149, 95.75980907, -2628.31681713, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 34.19993181, 0.00010778, 102.59979543, 0.00032335, 341.9993181, 0.00107783, -34.19993181, -0.00010778, -102.59979543, -0.00032335, -341.9993181, -0.00107783, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.15)
    ops.node(123007, 0.0, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.09, 26924416.23518142, 11218506.76465893, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 89.14658675, 0.00120998, 106.63002052, 0.0190253, 10.66300205, 0.05651743, -89.14658675, -0.00120998, -106.63002052, -0.0190253, -10.66300205, -0.05651743, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 89.14658675, 0.00120998, 106.63002052, 0.0190253, 10.66300205, 0.05651743, -89.14658675, -0.00120998, -106.63002052, -0.0190253, -10.66300205, -0.05651743, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 145.22083303, 0.02419961, 145.22083303, 0.07259884, 101.65458312, -2557.19492685, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 36.30520826, 0.00012082, 108.91562477, 0.00036245, 363.05208257, 0.00120818, -36.30520826, -0.00012082, -108.91562477, -0.00036245, -363.05208257, -0.00120818, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 145.22083303, 0.02419961, 145.22083303, 0.07259884, 101.65458312, -2557.19492685, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 36.30520826, 0.00012082, 108.91562477, 0.00036245, 363.05208257, 0.00120818, -36.30520826, -0.00012082, -108.91562477, -0.00036245, -363.05208257, -0.00120818, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.5, 4.5, 6.15)
    ops.node(123008, 4.5, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.16, 27081616.16931673, 11284006.7372153, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 212.99020106, 0.00107657, 255.94973565, 0.0240285, 25.59497356, 0.06151235, -212.99020106, -0.00107657, -255.94973565, -0.0240285, -25.59497356, -0.06151235, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 200.06631454, 0.00107657, 240.41913695, 0.0240285, 24.04191369, 0.06151235, -200.06631454, -0.00107657, -240.41913695, -0.0240285, -24.04191369, -0.06151235, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 226.31616646, 0.02153142, 226.31616646, 0.06459427, 158.42131652, -3708.78502179, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 56.57904161, 0.0001053, 169.73712484, 0.00031589, 565.79041614, 0.00105296, -56.57904161, -0.0001053, -169.73712484, -0.00031589, -565.79041614, -0.00105296, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 226.31616646, 0.02153142, 226.31616646, 0.06459427, 158.42131652, -3708.78502179, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 56.57904161, 0.0001053, 169.73712484, 0.00031589, 565.79041614, 0.00105296, -56.57904161, -0.0001053, -169.73712484, -0.00031589, -565.79041614, -0.00105296, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.15)
    ops.node(123009, 9.0, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 27588314.79309262, 11495131.16378859, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 148.82449127, 0.00121011, 178.46065174, 0.01781754, 17.84606517, 0.05007999, -148.82449127, -0.00121011, -178.46065174, -0.01781754, -17.84606517, -0.05007999, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 148.82449127, 0.00121011, 178.46065174, 0.01781754, 17.84606517, 0.05007999, -148.82449127, -0.00121011, -178.46065174, -0.01781754, -17.84606517, -0.05007999, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 166.61165213, 0.02420225, 166.61165213, 0.07260674, 116.62815649, -2486.93377974, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 41.65291303, 9.939e-05, 124.9587391, 0.00029816, 416.52913032, 0.00099388, -41.65291303, -9.939e-05, -124.9587391, -0.00029816, -416.52913032, -0.00099388, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 166.61165213, 0.02420225, 166.61165213, 0.07260674, 116.62815649, -2486.93377974, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 41.65291303, 9.939e-05, 124.9587391, 0.00029816, 416.52913032, 0.00099388, -41.65291303, -9.939e-05, -124.9587391, -0.00029816, -416.52913032, -0.00099388, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.15)
    ops.node(123010, 12.0, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 26591859.98664095, 11079941.6611004, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 146.1223222, 0.00122791, 175.13476823, 0.01744243, 17.51347682, 0.04711852, -146.1223222, -0.00122791, -175.13476823, -0.01744243, -17.51347682, -0.04711852, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 146.1223222, 0.00122791, 175.13476823, 0.01744243, 17.51347682, 0.04711852, -146.1223222, -0.00122791, -175.13476823, -0.01744243, -17.51347682, -0.04711852, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 164.69810882, 0.02455828, 164.69810882, 0.07367483, 115.28867617, -2543.55955629, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 41.1745272, 0.00010193, 123.52358161, 0.00030578, 411.74527205, 0.00101928, -41.1745272, -0.00010193, -123.52358161, -0.00030578, -411.74527205, -0.00101928, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 164.69810882, 0.02455828, 164.69810882, 0.07367483, 115.28867617, -2543.55955629, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 41.1745272, 0.00010193, 123.52358161, 0.00030578, 411.74527205, 0.00101928, -41.1745272, -0.00010193, -123.52358161, -0.00030578, -411.74527205, -0.00101928, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 16.5, 4.5, 6.15)
    ops.node(123011, 16.5, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.16, 25751783.39137309, 10729909.74640545, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 215.50827488, 0.00109337, 258.75742728, 0.02319231, 25.87574273, 0.05670551, -215.50827488, -0.00109337, -258.75742728, -0.02319231, -25.87574273, -0.05670551, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 201.74363203, 0.00109337, 242.23043511, 0.02319231, 24.22304351, 0.05670551, -201.74363203, -0.00109337, -242.23043511, -0.02319231, -24.22304351, -0.05670551, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 223.01668436, 0.02186737, 223.01668436, 0.06560212, 156.11167906, -3815.61970421, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 55.75417109, 0.00010912, 167.26251327, 0.00032736, 557.54171091, 0.00109119, -55.75417109, -0.00010912, -167.26251327, -0.00032736, -557.54171091, -0.00109119, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 223.01668436, 0.02186737, 223.01668436, 0.06560212, 156.11167906, -3815.61970421, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 55.75417109, 0.00010912, 167.26251327, 0.00032736, 557.54171091, 0.00109119, -55.75417109, -0.00010912, -167.26251327, -0.00032736, -557.54171091, -0.00109119, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.15)
    ops.node(123012, 21.0, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.09, 27072999.7789212, 11280416.5745505, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 88.58391943, 0.00122689, 105.96997557, 0.01881375, 10.59699756, 0.05682893, -88.58391943, -0.00122689, -105.96997557, -0.01881375, -10.59699756, -0.05682893, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 88.58391943, 0.00122689, 105.96997557, 0.01881375, 10.59699756, 0.05682893, -88.58391943, -0.00122689, -105.96997557, -0.01881375, -10.59699756, -0.05682893, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 144.31301642, 0.02453778, 144.31301642, 0.07361333, 101.0191115, -2512.55978712, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 36.07825411, 0.0001194, 108.23476232, 0.00035821, 360.78254106, 0.00119404, -36.07825411, -0.0001194, -108.23476232, -0.00035821, -360.78254106, -0.00119404, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 144.31301642, 0.02453778, 144.31301642, 0.07361333, 101.0191115, -2512.55978712, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 36.07825411, 0.0001194, 108.23476232, 0.00035821, 360.78254106, 0.00119404, -36.07825411, -0.0001194, -108.23476232, -0.00035821, -360.78254106, -0.00119404, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.15)
    ops.node(123013, 0.0, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.09, 27861093.73542754, 11608789.05642814, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 88.38827002, 0.00123092, 105.77817883, 0.01925467, 10.57781788, 0.05995539, -88.38827002, -0.00123092, -105.77817883, -0.01925467, -10.57781788, -0.05995539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 88.38827002, 0.00123092, 105.77817883, 0.01925467, 10.57781788, 0.05995539, -88.38827002, -0.00123092, -105.77817883, -0.01925467, -10.57781788, -0.05995539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 146.92884851, 0.0246184, 146.92884851, 0.07385519, 102.85019395, -2524.73045603, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 36.73221213, 0.00011813, 110.19663638, 0.00035439, 367.32212127, 0.00118129, -36.73221213, -0.00011813, -110.19663638, -0.00035439, -367.32212127, -0.00118129, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 146.92884851, 0.0246184, 146.92884851, 0.07385519, 102.85019395, -2524.73045603, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 36.73221213, 0.00011813, 110.19663638, 0.00035439, 367.32212127, 0.00118129, -36.73221213, -0.00011813, -110.19663638, -0.00035439, -367.32212127, -0.00118129, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.5, 9.0, 6.15)
    ops.node(123014, 4.5, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.16, 28178191.79591591, 11740913.2482983, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 215.29467806, 0.00105653, 258.68804041, 0.02443696, 25.86880404, 0.06487801, -215.29467806, -0.00105653, -258.68804041, -0.02443696, -25.86880404, -0.06487801, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 202.19682835, 0.00105653, 242.95027529, 0.02443696, 24.29502753, 0.06487801, -202.19682835, -0.00105653, -242.95027529, -0.02443696, -24.29502753, -0.06487801, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 234.30881234, 0.02113051, 234.30881234, 0.06339154, 164.01616864, -3795.59276163, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 58.57720309, 0.00010477, 175.73160926, 0.00031432, 585.77203085, 0.00104772, -58.57720309, -0.00010477, -175.73160926, -0.00031432, -585.77203085, -0.00104772, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 234.30881234, 0.02113051, 234.30881234, 0.06339154, 164.01616864, -3795.59276163, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 58.57720309, 0.00010477, 175.73160926, 0.00031432, 585.77203085, 0.00104772, -58.57720309, -0.00010477, -175.73160926, -0.00031432, -585.77203085, -0.00104772, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.15)
    ops.node(123015, 9.0, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 27497625.12524068, 11457343.80218362, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 146.30249224, 0.00117885, 175.35666736, 0.02425005, 17.53566674, 0.06410072, -146.30249224, -0.00117885, -175.35666736, -0.02425005, -17.53566674, -0.06410072, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 146.30249224, 0.00117885, 175.35666736, 0.02425005, 17.53566674, 0.06410072, -146.30249224, -0.00117885, -175.35666736, -0.02425005, -17.53566674, -0.06410072, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 190.97151634, 0.02357693, 190.97151634, 0.07073079, 133.68006144, -3257.8995562, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 47.74287908, 0.0001143, 143.22863725, 0.00034289, 477.42879084, 0.00114295, -47.74287908, -0.0001143, -143.22863725, -0.00034289, -477.42879084, -0.00114295, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 190.97151634, 0.02357693, 190.97151634, 0.07073079, 133.68006144, -3257.8995562, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 47.74287908, 0.0001143, 143.22863725, 0.00034289, 477.42879084, 0.00114295, -47.74287908, -0.0001143, -143.22863725, -0.00034289, -477.42879084, -0.00114295, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.15)
    ops.node(123016, 12.0, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1225, 27393193.55535775, 11413830.64806573, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 148.83788101, 0.00121025, 178.38969598, 0.0243222, 17.8389696, 0.06383825, -148.83788101, -0.00121025, -178.38969598, -0.0243222, -17.8389696, -0.06383825, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 148.83788101, 0.00121025, 178.38969598, 0.0243222, 17.8389696, 0.06383825, -148.83788101, -0.00121025, -178.38969598, -0.0243222, -17.8389696, -0.06383825, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 191.91784214, 0.02420496, 191.91784214, 0.07261489, 134.3424895, -3303.6626172, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 47.97946054, 0.0001153, 143.93838161, 0.0003459, 479.79460535, 0.00115299, -47.97946054, -0.0001153, -143.93838161, -0.0003459, -479.79460535, -0.00115299, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 191.91784214, 0.02420496, 191.91784214, 0.07261489, 134.3424895, -3303.6626172, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 47.97946054, 0.0001153, 143.93838161, 0.0003459, 479.79460535, 0.00115299, -47.97946054, -0.0001153, -143.93838161, -0.0003459, -479.79460535, -0.00115299, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 16.5, 9.0, 6.15)
    ops.node(123017, 16.5, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.16, 28084709.4801308, 11701962.28338783, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 217.70206592, 0.0010368, 261.59019204, 0.02405566, 26.1590192, 0.06425563, -217.70206592, -0.0010368, -261.59019204, -0.02405566, -26.1590192, -0.06425563, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 203.92234526, 0.0010368, 245.03251833, 0.02405566, 24.50325183, 0.06425563, -203.92234526, -0.0010368, -245.03251833, -0.02405566, -24.50325183, -0.06425563, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 231.09208263, 0.02073606, 231.09208263, 0.06220817, 161.76445784, -3702.56974664, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 57.77302066, 0.00010368, 173.31906197, 0.00031103, 577.73020657, 0.00103678, -57.77302066, -0.00010368, -173.31906197, -0.00031103, -577.73020657, -0.00103678, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 231.09208263, 0.02073606, 231.09208263, 0.06220817, 161.76445784, -3702.56974664, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 57.77302066, 0.00010368, 173.31906197, 0.00031103, 577.73020657, 0.00103678, -57.77302066, -0.00010368, -173.31906197, -0.00031103, -577.73020657, -0.00103678, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.15)
    ops.node(123018, 21.0, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.09, 27386131.27707032, 11410888.03211263, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 88.55327027, 0.00121195, 105.95536144, 0.01935776, 10.59553614, 0.058458, -88.55327027, -0.00121195, -105.95536144, -0.01935776, -10.59553614, -0.058458, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 88.55327027, 0.00121195, 105.95536144, 0.01935776, 10.59553614, 0.058458, -88.55327027, -0.00121195, -105.95536144, -0.01935776, -10.59553614, -0.058458, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 148.51741094, 0.02423897, 148.51741094, 0.07271691, 103.96218766, -2624.50475765, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 37.12935274, 0.00012148, 111.38805821, 0.00036443, 371.29352736, 0.00121477, -37.12935274, -0.00012148, -111.38805821, -0.00036443, -371.29352736, -0.00121477, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 148.51741094, 0.02423897, 148.51741094, 0.07271691, 103.96218766, -2624.50475765, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 37.12935274, 0.00012148, 111.38805821, 0.00036443, 371.29352736, 0.00121477, -37.12935274, -0.00012148, -111.38805821, -0.00036443, -371.29352736, -0.00121477, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.125)
    ops.node(123019, 0.0, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.09, 28440688.11104437, 11850286.71293516, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 79.06647173, 0.00115543, 95.4405814, 0.02306275, 9.54405814, 0.07803283, -79.06647173, -0.00115543, -95.4405814, -0.02306275, -9.54405814, -0.07803283, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 83.82878628, 0.00115543, 101.18913778, 0.02306275, 10.11891378, 0.07803283, -83.82878628, -0.00115543, -101.18913778, -0.02306275, -10.11891378, -0.07803283, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 139.18632883, 0.02310868, 139.18632883, 0.06932604, 97.43043018, -2733.64183523, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 34.79658221, 0.00010962, 104.38974662, 0.00032887, 347.96582207, 0.00109624, -34.79658221, -0.00010962, -104.38974662, -0.00032887, -347.96582207, -0.00109624, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 139.18632883, 0.02310868, 139.18632883, 0.06932604, 97.43043018, -2733.64183523, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 34.79658221, 0.00010962, 104.38974662, 0.00032887, 347.96582207, 0.00109624, -34.79658221, -0.00010962, -104.38974662, -0.00032887, -347.96582207, -0.00109624, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 4.5, 13.5, 6.15)
    ops.node(123020, 4.5, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.09, 28281390.6313987, 11783912.76308279, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 99.47940716, 0.00132796, 119.05036484, 0.01993733, 11.90503648, 0.05609546, -99.47940716, -0.00132796, -119.05036484, -0.01993733, -11.90503648, -0.05609546, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 94.76921488, 0.00132796, 113.41351872, 0.01993733, 11.34135187, 0.05609546, -94.76921488, -0.00132796, -113.41351872, -0.01993733, -11.34135187, -0.05609546, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 136.0800102, 0.0265592, 136.0800102, 0.07967761, 95.25600714, -2135.32448113, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 34.02000255, 0.00010778, 102.06000765, 0.00032334, 340.2000255, 0.00107781, -34.02000255, -0.00010778, -102.06000765, -0.00032334, -340.2000255, -0.00107781, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 136.0800102, 0.0265592, 136.0800102, 0.07967761, 95.25600714, -2135.32448113, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 34.02000255, 0.00010778, 102.06000765, 0.00032334, 340.2000255, 0.00107781, -34.02000255, -0.00010778, -102.06000765, -0.00032334, -340.2000255, -0.00107781, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.15)
    ops.node(123021, 9.0, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.09, 28131263.58317538, 11721359.82632308, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 95.0470442, 0.00126887, 114.07211326, 0.02072488, 11.40721133, 0.05965709, -95.0470442, -0.00126887, -114.07211326, -0.02072488, -11.40721133, -0.05965709, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 90.09735449, 0.00126887, 108.13167009, 0.02072488, 10.81316701, 0.05965709, -90.09735449, -0.00126887, -108.13167009, -0.02072488, -10.81316701, -0.05965709, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 133.38802795, 0.0253774, 133.38802795, 0.07613219, 93.37161956, -2148.17346088, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 33.34700699, 0.00010621, 100.04102096, 0.00031864, 333.47006987, 0.00106212, -33.34700699, -0.00010621, -100.04102096, -0.00031864, -333.47006987, -0.00106212, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 133.38802795, 0.0253774, 133.38802795, 0.07613219, 93.37161956, -2148.17346088, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 33.34700699, 0.00010621, 100.04102096, 0.00031864, 333.47006987, 0.00106212, -33.34700699, -0.00010621, -100.04102096, -0.00031864, -333.47006987, -0.00106212, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.15)
    ops.node(123022, 12.0, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.09, 26926004.18863422, 11219168.41193092, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 93.97989501, 0.00130951, 112.77739545, 0.01988035, 11.27773955, 0.05544986, -93.97989501, -0.00130951, -112.77739545, -0.01988035, -11.27773955, -0.05544986, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 89.14942372, 0.00130951, 106.98075171, 0.01988035, 10.69807517, 0.05544986, -89.14942372, -0.00130951, -106.98075171, -0.01988035, -10.69807517, -0.05544986, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 128.09244108, 0.02619025, 128.09244108, 0.07857076, 89.66470876, -2085.22291481, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 32.02311027, 0.00010656, 96.06933081, 0.00031968, 320.23110271, 0.00106561, -32.02311027, -0.00010656, -96.06933081, -0.00031968, -320.23110271, -0.00106561, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 128.09244108, 0.02619025, 128.09244108, 0.07857076, 89.66470876, -2085.22291481, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 32.02311027, 0.00010656, 96.06933081, 0.00031968, 320.23110271, 0.00106561, -32.02311027, -0.00010656, -96.06933081, -0.00031968, -320.23110271, -0.00106561, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 16.5, 13.5, 6.15)
    ops.node(123023, 16.5, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.09, 27669833.18839698, 11529097.16183207, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 100.89901881, 0.00130023, 120.73549011, 0.01944262, 12.07354901, 0.05387039, -100.89901881, -0.00130023, -120.73549011, -0.01944262, -12.07354901, -0.05387039, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 95.74445851, 0.00130023, 114.56755734, 0.01944262, 11.45675573, 0.05387039, -95.74445851, -0.00130023, -114.56755734, -0.01944262, -11.45675573, -0.05387039, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 133.72037068, 0.0260046, 133.72037068, 0.07801379, 93.60425948, -2116.95776432, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 33.43009267, 0.00010825, 100.29027801, 0.00032476, 334.30092671, 0.00108253, -33.43009267, -0.00010825, -100.29027801, -0.00032476, -334.30092671, -0.00108253, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 133.72037068, 0.0260046, 133.72037068, 0.07801379, 93.60425948, -2116.95776432, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 33.43009267, 0.00010825, 100.29027801, 0.00032476, 334.30092671, 0.00108253, -33.43009267, -0.00010825, -100.29027801, -0.00032476, -334.30092671, -0.00108253, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.125)
    ops.node(123024, 21.0, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.09, 28761853.79465206, 11984105.74777169, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 80.54642877, 0.00112548, 97.19020287, 0.02270317, 9.71902029, 0.07844509, -80.54642877, -0.00112548, -97.19020287, -0.02270317, -9.71902029, -0.07844509, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 85.71706135, 0.00112548, 103.42927314, 0.02270317, 10.34292731, 0.07844509, -85.71706135, -0.00112548, -103.42927314, -0.02270317, -10.34292731, -0.07844509, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 139.74686165, 0.02250968, 139.74686165, 0.06752904, 97.82280316, -2719.31901879, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 34.93671541, 0.00010884, 104.81014624, 0.00032651, 349.36715413, 0.00108836, -34.93671541, -0.00010884, -104.81014624, -0.00032651, -349.36715413, -0.00108836, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 139.74686165, 0.02250968, 139.74686165, 0.06752904, 97.82280316, -2719.31901879, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 34.93671541, 0.00010884, 104.81014624, 0.00032651, 349.36715413, 0.00108836, -34.93671541, -0.00010884, -104.81014624, -0.00032651, -349.36715413, -0.00108836, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.9)
    ops.node(124001, 0.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.09, 26797028.54343202, 11165428.55976334, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 56.41660324, 0.00117547, 68.83804191, 0.02512108, 6.88380419, 0.09240927, -56.41660324, -0.00117547, -68.83804191, -0.02512108, -6.88380419, -0.09240927, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 56.41660324, 0.00117547, 68.83804191, 0.02512108, 6.88380419, 0.09240927, -56.41660324, -0.00117547, -68.83804191, -0.02512108, -6.88380419, -0.09240927, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 125.65377063, 0.02350947, 125.65377063, 0.07052841, 87.95763944, -4399.33239326, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 31.41344266, 0.00010504, 94.24032797, 0.00031511, 314.13442657, 0.00105036, -31.41344266, -0.00010504, -94.24032797, -0.00031511, -314.13442657, -0.00105036, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 125.65377063, 0.02350947, 125.65377063, 0.07052841, 87.95763944, -4399.33239326, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 31.41344266, 0.00010504, 94.24032797, 0.00031511, 314.13442657, 0.00105036, -31.41344266, -0.00010504, -94.24032797, -0.00031511, -314.13442657, -0.00105036, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.5, 0.0, 8.95)
    ops.node(124002, 4.5, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.09, 27552874.63806916, 11480364.43252882, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 75.92444757, 0.00119913, 92.1086793, 0.02368002, 9.21086793, 0.07511044, -75.92444757, -0.00119913, -92.1086793, -0.02368002, -9.21086793, -0.07511044, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 71.24025363, 0.00119913, 86.42599169, 0.02368002, 8.64259917, 0.07511044, -71.24025363, -0.00119913, -86.42599169, -0.02368002, -8.64259917, -0.07511044, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 119.58070995, 0.02398269, 119.58070995, 0.07194808, 83.70649697, -2422.50748189, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 29.89517749, 9.722e-05, 89.68553246, 0.00029165, 298.95177488, 0.00097217, -29.89517749, -9.722e-05, -89.68553246, -0.00029165, -298.95177488, -0.00097217, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 119.58070995, 0.02398269, 119.58070995, 0.07194808, 83.70649697, -2422.50748189, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 29.89517749, 9.722e-05, 89.68553246, 0.00029165, 298.95177488, 0.00097217, -29.89517749, -9.722e-05, -89.68553246, -0.00029165, -298.95177488, -0.00097217, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.5, 0.0, 8.95)
    ops.node(124005, 16.5, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.09, 28112417.5965087, 11713507.33187863, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 77.41194977, 0.00118439, 93.84382536, 0.02344407, 9.38438254, 0.07587213, -77.41194977, -0.00118439, -93.84382536, -0.02344407, -9.38438254, -0.07587213, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 72.5141154, 0.00118439, 87.9063504, 0.02344407, 8.79063504, 0.07587213, -72.5141154, -0.00118439, -87.9063504, -0.02344407, -8.79063504, -0.07587213, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 119.24870496, 0.02368778, 119.24870496, 0.07106334, 83.47409347, -2332.13722957, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 29.81217624, 9.502e-05, 89.43652872, 0.00028505, 298.1217624, 0.00095017, -29.81217624, -9.502e-05, -89.43652872, -0.00028505, -298.1217624, -0.00095017, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 119.24870496, 0.02368778, 119.24870496, 0.07106334, 83.47409347, -2332.13722957, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 29.81217624, 9.502e-05, 89.43652872, 0.00028505, 298.1217624, 0.00095017, -29.81217624, -9.502e-05, -89.43652872, -0.00028505, -298.1217624, -0.00095017, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 21.0, 0.0, 8.9)
    ops.node(124006, 21.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.09, 28690291.62009976, 11954288.17504157, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 57.47869953, 0.001108, 69.89311665, 0.02495691, 6.98931167, 0.09471803, -57.47869953, -0.001108, -69.89311665, -0.02495691, -6.98931167, -0.09471803, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 57.47869953, 0.001108, 69.89311665, 0.02495691, 6.98931167, 0.09471803, -57.47869953, -0.001108, -69.89311665, -0.02495691, -6.98931167, -0.09471803, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 129.70116129, 0.02215998, 129.70116129, 0.06647993, 90.79081291, -4326.47166489, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 32.42529032, 0.00010126, 97.27587097, 0.00030379, 324.25290323, 0.00101264, -32.42529032, -0.00010126, -97.27587097, -0.00030379, -324.25290323, -0.00101264, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 129.70116129, 0.02215998, 129.70116129, 0.06647993, 90.79081291, -4326.47166489, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 32.42529032, 0.00010126, 97.27587097, 0.00030379, 324.25290323, 0.00101264, -32.42529032, -0.00010126, -97.27587097, -0.00030379, -324.25290323, -0.00101264, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 8.925)
    ops.node(124007, 0.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.09, 27294826.15064396, 11372844.22943499, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 65.36615845, 0.00110803, 79.32354054, 0.02340097, 7.93235405, 0.0825746, -65.36615845, -0.00110803, -79.32354054, -0.02340097, -7.93235405, -0.0825746, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 65.36615845, 0.00110803, 79.32354054, 0.02340097, 7.93235405, 0.0825746, -65.36615845, -0.00110803, -79.32354054, -0.02340097, -7.93235405, -0.0825746, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 130.5131628, 0.02216065, 130.5131628, 0.06648194, 91.35921396, -3045.85551601, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 32.6282907, 0.00010711, 97.8848721, 0.00032132, 326.28290701, 0.00107108, -32.6282907, -0.00010711, -97.8848721, -0.00032132, -326.28290701, -0.00107108, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 130.5131628, 0.02216065, 130.5131628, 0.06648194, 91.35921396, -3045.85551601, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 32.6282907, 0.00010711, 97.8848721, 0.00032132, 326.28290701, 0.00107108, -32.6282907, -0.00010711, -97.8848721, -0.00032132, -326.28290701, -0.00107108, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.5, 4.5, 8.95)
    ops.node(124008, 4.5, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.16, 25754414.66150172, 10731006.10895905, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 168.03888133, 0.00105332, 204.35726575, 0.02032654, 20.43572657, 0.0595237, -168.03888133, -0.00105332, -204.35726575, -0.02032654, -20.43572657, -0.0595237, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 156.13243619, 0.00105332, 189.87747062, 0.02032654, 18.98774706, 0.0595237, -156.13243619, -0.00105332, -189.87747062, -0.02032654, -18.98774706, -0.0595237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 173.39344556, 0.02106637, 173.39344556, 0.06319911, 121.37541189, -2997.59239937, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 43.34836139, 8.483e-05, 130.04508417, 0.00025449, 433.4836139, 0.0008483, -43.34836139, -8.483e-05, -130.04508417, -0.00025449, -433.4836139, -0.0008483, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 173.39344556, 0.02106637, 173.39344556, 0.06319911, 121.37541189, -2997.59239937, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 43.34836139, 8.483e-05, 130.04508417, 0.00025449, 433.4836139, 0.0008483, -43.34836139, -8.483e-05, -130.04508417, -0.00025449, -433.4836139, -0.0008483, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.0, 4.5, 8.925)
    ops.node(124009, 9.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 28448688.46750101, 11853620.19479209, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 114.70920168, 0.00110285, 138.99485156, 0.02132636, 13.89948516, 0.06829304, -114.70920168, -0.00110285, -138.99485156, -0.02132636, -13.89948516, -0.06829304, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 114.70920168, 0.00110285, 138.99485156, 0.02132636, 13.89948516, 0.06829304, -114.70920168, -0.00110285, -138.99485156, -0.02132636, -13.89948516, -0.06829304, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 153.55320641, 0.02205708, 153.55320641, 0.06617125, 107.48724449, -2706.30837717, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 38.3883016, 8.883e-05, 115.16490481, 0.00026648, 383.88301603, 0.00088828, -38.3883016, -8.883e-05, -115.16490481, -0.00026648, -383.88301603, -0.00088828, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 153.55320641, 0.02205708, 153.55320641, 0.06617125, 107.48724449, -2706.30837717, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 38.3883016, 8.883e-05, 115.16490481, 0.00026648, 383.88301603, 0.00088828, -38.3883016, -8.883e-05, -115.16490481, -0.00026648, -383.88301603, -0.00088828, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.0, 4.5, 8.925)
    ops.node(124010, 12.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 28310949.79278119, 11796229.08032549, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 113.07954676, 0.00108722, 137.04916503, 0.02159508, 13.7049165, 0.06835921, -113.07954676, -0.00108722, -137.04916503, -0.02159508, -13.7049165, -0.06835921, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 113.07954676, 0.00108722, 137.04916503, 0.02159508, 13.7049165, 0.06835921, -113.07954676, -0.00108722, -137.04916503, -0.02159508, -13.7049165, -0.06835921, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 152.91477943, 0.02174443, 152.91477943, 0.06523328, 107.0403456, -2699.83482373, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 38.22869486, 8.889e-05, 114.68608457, 0.00026667, 382.28694857, 0.00088889, -38.22869486, -8.889e-05, -114.68608457, -0.00026667, -382.28694857, -0.00088889, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 152.91477943, 0.02174443, 152.91477943, 0.06523328, 107.0403456, -2699.83482373, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 38.22869486, 8.889e-05, 114.68608457, 0.00026667, 382.28694857, 0.00088889, -38.22869486, -8.889e-05, -114.68608457, -0.00026667, -382.28694857, -0.00088889, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 16.5, 4.5, 8.95)
    ops.node(124011, 16.5, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.16, 28071726.41682608, 11696552.67367753, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 174.1437318, 0.00097924, 211.26788559, 0.02007555, 21.12678856, 0.06278198, -174.1437318, -0.00097924, -211.26788559, -0.02007555, -21.12678856, -0.06278198, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 161.18031802, 0.00097924, 195.54091689, 0.02007555, 19.55409169, 0.06278198, -161.18031802, -0.00097924, -195.54091689, -0.02007555, -19.55409169, -0.06278198, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 182.7886565, 0.01958489, 182.7886565, 0.05875467, 127.95205955, -2946.43954479, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 45.69716413, 8.204e-05, 137.09149238, 0.00024613, 456.97164125, 0.00082045, -45.69716413, -8.204e-05, -137.09149238, -0.00024613, -456.97164125, -0.00082045, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 182.7886565, 0.01958489, 182.7886565, 0.05875467, 127.95205955, -2946.43954479, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 45.69716413, 8.204e-05, 137.09149238, 0.00024613, 456.97164125, 0.00082045, -45.69716413, -8.204e-05, -137.09149238, -0.00024613, -456.97164125, -0.00082045, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 8.925)
    ops.node(124012, 21.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.09, 27223938.69161687, 11343307.78817369, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 64.27332123, 0.00111746, 78.00341545, 0.02367326, 7.80034155, 0.08268955, -64.27332123, -0.00111746, -78.00341545, -0.02367326, -7.80034155, -0.08268955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 64.27332123, 0.00111746, 78.00341545, 0.02367326, 7.80034155, 0.08268955, -64.27332123, -0.00111746, -78.00341545, -0.02367326, -7.80034155, -0.08268955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 131.95712661, 0.02234922, 131.95712661, 0.06704765, 92.36998863, -3139.00451252, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 32.98928165, 0.00010858, 98.96784496, 0.00032573, 329.89281653, 0.00108575, -32.98928165, -0.00010858, -98.96784496, -0.00032573, -329.89281653, -0.00108575, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 131.95712661, 0.02234922, 131.95712661, 0.06704765, 92.36998863, -3139.00451252, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 32.98928165, 0.00010858, 98.96784496, 0.00032573, 329.89281653, 0.00108575, -32.98928165, -0.00010858, -98.96784496, -0.00032573, -329.89281653, -0.00108575, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.0, 8.925)
    ops.node(124013, 0.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.09, 29026623.81039253, 12094426.58766356, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 64.90438549, 0.00109389, 78.56631282, 0.02351794, 7.85663128, 0.08614382, -64.90438549, -0.00109389, -78.56631282, -0.02351794, -7.85663128, -0.08614382, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 64.90438549, 0.00109389, 78.56631282, 0.02351794, 7.85663128, 0.08614382, -64.90438549, -0.00109389, -78.56631282, -0.02351794, -7.85663128, -0.08614382, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 136.1938413, 0.02187784, 136.1938413, 0.06563353, 95.33568891, -3108.79817617, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 34.04846033, 0.0001051, 102.14538098, 0.0003153, 340.48460325, 0.00105102, -34.04846033, -0.0001051, -102.14538098, -0.0003153, -340.48460325, -0.00105102, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 136.1938413, 0.02187784, 136.1938413, 0.06563353, 95.33568891, -3108.79817617, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 34.04846033, 0.0001051, 102.14538098, 0.0003153, 340.48460325, 0.00105102, -34.04846033, -0.0001051, -102.14538098, -0.0003153, -340.48460325, -0.00105102, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.5, 9.0, 8.95)
    ops.node(124014, 4.5, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.16, 27611281.36562218, 11504700.56900924, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 164.59510451, 0.00101023, 199.8134643, 0.02082203, 19.98134643, 0.06290915, -164.59510451, -0.00101023, -199.8134643, -0.02082203, -19.98134643, -0.06290915, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 153.48195757, 0.00101023, 186.32244101, 0.02082203, 18.6322441, 0.06290915, -153.48195757, -0.00101023, -186.32244101, -0.02082203, -18.6322441, -0.06290915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 182.19180769, 0.02020451, 182.19180769, 0.06061354, 127.53426538, -3014.03635569, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 45.54795192, 8.314e-05, 136.64385576, 0.00024942, 455.47951922, 0.00083141, -45.54795192, -8.314e-05, -136.64385576, -0.00024942, -455.47951922, -0.00083141, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 182.19180769, 0.02020451, 182.19180769, 0.06061354, 127.53426538, -3014.03635569, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 45.54795192, 8.314e-05, 136.64385576, 0.00024942, 455.47951922, 0.00083141, -45.54795192, -8.314e-05, -136.64385576, -0.00024942, -455.47951922, -0.00083141, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 9.0, 8.925)
    ops.node(124015, 9.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 28410382.70290735, 11837659.45954473, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 114.02016746, 0.00110547, 138.09605361, 0.02093551, 13.80960536, 0.06712183, -114.02016746, -0.00110547, -138.09605361, -0.02093551, -13.80960536, -0.06712183, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 114.02016746, 0.00110547, 138.09605361, 0.02093551, 13.80960536, 0.06712183, -114.02016746, -0.00110547, -138.09605361, -0.02093551, -13.80960536, -0.06712183, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 152.38781419, 0.02210949, 152.38781419, 0.06632848, 106.67146993, -2578.21423132, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 38.09695355, 8.827e-05, 114.29086064, 0.00026482, 380.96953546, 0.00088273, -38.09695355, -8.827e-05, -114.29086064, -0.00026482, -380.96953546, -0.00088273, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 152.38781419, 0.02210949, 152.38781419, 0.06632848, 106.67146993, -2578.21423132, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 38.09695355, 8.827e-05, 114.29086064, 0.00026482, 380.96953546, 0.00088273, -38.09695355, -8.827e-05, -114.29086064, -0.00026482, -380.96953546, -0.00088273, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.0, 9.0, 8.925)
    ops.node(124016, 12.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1225, 26464915.32558582, 11027048.05232743, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 117.03495541, 0.00113269, 142.05056511, 0.02052923, 14.20505651, 0.06337173, -117.03495541, -0.00113269, -142.05056511, -0.02052923, -14.20505651, -0.06337173, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 117.03495541, 0.00113269, 142.05056511, 0.02052923, 14.20505651, 0.06337173, -117.03495541, -0.00113269, -142.05056511, -0.02052923, -14.20505651, -0.06337173, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 146.61406307, 0.02265379, 146.61406307, 0.06796137, 102.62984415, -2628.51847261, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 36.65351577, 9.117e-05, 109.9605473, 0.00027351, 366.53515766, 0.00091172, -36.65351577, -9.117e-05, -109.9605473, -0.00027351, -366.53515766, -0.00091172, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 146.61406307, 0.02265379, 146.61406307, 0.06796137, 102.62984415, -2628.51847261, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 36.65351577, 9.117e-05, 109.9605473, 0.00027351, 366.53515766, 0.00091172, -36.65351577, -9.117e-05, -109.9605473, -0.00027351, -366.53515766, -0.00091172, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 16.5, 9.0, 8.95)
    ops.node(124017, 16.5, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.16, 27970647.0931257, 11654436.28880238, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 172.26163768, 0.00101243, 209.0157898, 0.02057736, 20.90157898, 0.06315085, -172.26163768, -0.00101243, -209.0157898, -0.02057736, -20.90157898, -0.06315085, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 159.96392988, 0.00101243, 194.09421384, 0.02057736, 19.40942138, 0.06315085, -159.96392988, -0.00101243, -194.09421384, -0.02057736, -19.40942138, -0.06315085, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 183.48371096, 0.02024861, 183.48371096, 0.06074582, 128.43859767, -2997.46225031, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 45.87092774, 8.265e-05, 137.61278322, 0.00024796, 458.70927741, 0.00082654, -45.87092774, -8.265e-05, -137.61278322, -0.00024796, -458.70927741, -0.00082654, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 183.48371096, 0.02024861, 183.48371096, 0.06074582, 128.43859767, -2997.46225031, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 45.87092774, 8.265e-05, 137.61278322, 0.00024796, 458.70927741, 0.00082654, -45.87092774, -8.265e-05, -137.61278322, -0.00024796, -458.70927741, -0.00082654, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 21.0, 9.0, 8.925)
    ops.node(124018, 21.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.09, 26998699.32510646, 11249458.05212769, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 65.16694395, 0.00113029, 79.10639747, 0.02375263, 7.91063975, 0.08225986, -65.16694395, -0.00113029, -79.10639747, -0.02375263, -7.91063975, -0.08225986, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 65.16694395, 0.00113029, 79.10639747, 0.02375263, 7.91063975, 0.08225986, -65.16694395, -0.00113029, -79.10639747, -0.02375263, -7.91063975, -0.08225986, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 131.02005288, 0.02260572, 131.02005288, 0.06781716, 91.71403701, -3118.61405985, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 32.75501322, 0.0001087, 98.26503966, 0.00032611, 327.5501322, 0.00108703, -32.75501322, -0.0001087, -98.26503966, -0.00032611, -327.5501322, -0.00108703, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 131.02005288, 0.02260572, 131.02005288, 0.06781716, 91.71403701, -3118.61405985, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 32.75501322, 0.0001087, 98.26503966, 0.00032611, 327.5501322, 0.00108703, -32.75501322, -0.0001087, -98.26503966, -0.00032611, -327.5501322, -0.00108703, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 13.5, 8.9)
    ops.node(124019, 0.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.09, 27746488.0990606, 11561036.70794192, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 56.30122013, 0.00115717, 68.58824514, 0.02532565, 6.85882451, 0.09393419, -56.30122013, -0.00115717, -68.58824514, -0.02532565, -6.85882451, -0.09393419, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 56.30122013, 0.00115717, 68.58824514, 0.02532565, 6.85882451, 0.09393419, -56.30122013, -0.00115717, -68.58824514, -0.02532565, -6.85882451, -0.09393419, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 126.65220673, 0.02314343, 126.65220673, 0.06943029, 88.65654471, -4270.65956785, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 31.66305168, 0.00010225, 94.98915505, 0.00030674, 316.63051682, 0.00102248, -31.66305168, -0.00010225, -94.98915505, -0.00030674, -316.63051682, -0.00102248, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 126.65220673, 0.02314343, 126.65220673, 0.06943029, 88.65654471, -4270.65956785, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 31.66305168, 0.00010225, 94.98915505, 0.00030674, 316.63051682, 0.00102248, -31.66305168, -0.00010225, -94.98915505, -0.00030674, -316.63051682, -0.00102248, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 4.5, 13.5, 8.95)
    ops.node(124020, 4.5, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.09, 27697876.64337321, 11540781.93473884, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 71.34469644, 0.00118294, 86.53711831, 0.02338898, 8.65371183, 0.07508447, -71.34469644, -0.00118294, -86.53711831, -0.02338898, -8.65371183, -0.07508447, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 76.09894879, 0.00118294, 92.30375996, 0.02338898, 9.230376, 0.07508447, -76.09894879, -0.00118294, -92.30375996, -0.02338898, -9.230376, -0.07508447, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 119.30984578, 0.0236587, 119.30984578, 0.07097611, 83.51689204, -2389.69858354, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 29.82746144, 9.649e-05, 89.48238433, 0.00028947, 298.27461444, 0.00096489, -29.82746144, -9.649e-05, -89.48238433, -0.00028947, -298.27461444, -0.00096489, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 119.30984578, 0.0236587, 119.30984578, 0.07097611, 83.51689204, -2389.69858354, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 29.82746144, 9.649e-05, 89.48238433, 0.00028947, 298.27461444, 0.00096489, -29.82746144, -9.649e-05, -89.48238433, -0.00028947, -298.27461444, -0.00096489, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 8.925)
    ops.node(124021, 9.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.09, 28100852.55570283, 11708688.56487618, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 70.17943052, 0.00120156, 85.17398176, 0.02440534, 8.51739818, 0.07861443, -70.17943052, -0.00120156, -85.17398176, -0.02440534, -8.51739818, -0.07861443, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 74.88884381, 0.00120156, 90.88960925, 0.02440534, 9.08896092, 0.07861443, -74.88884381, -0.00120156, -90.88960925, -0.02440534, -9.08896092, -0.07861443, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 121.00742844, 0.02403116, 121.00742844, 0.07209347, 84.70519991, -2625.83261737, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 30.25185711, 9.646e-05, 90.75557133, 0.00028938, 302.5185711, 0.00096459, -30.25185711, -9.646e-05, -90.75557133, -0.00028938, -302.5185711, -0.00096459, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 121.00742844, 0.02403116, 121.00742844, 0.07209347, 84.70519991, -2625.83261737, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 30.25185711, 9.646e-05, 90.75557133, 0.00028938, 302.5185711, 0.00096459, -30.25185711, -9.646e-05, -90.75557133, -0.00028938, -302.5185711, -0.00096459, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 8.925)
    ops.node(124022, 12.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.09, 28728422.65247, 11970176.10519583, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 70.36216825, 0.00119424, 85.30624942, 0.02413191, 8.53062494, 0.07928715, -70.36216825, -0.00119424, -85.30624942, -0.02413191, -8.53062494, -0.07928715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 75.04180454, 0.00119424, 90.97978437, 0.02413191, 9.09797844, 0.07928715, -75.04180454, -0.00119424, -90.97978437, -0.02413191, -9.09797844, -0.07928715, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 120.55999178, 0.02388483, 120.55999178, 0.0716545, 84.39199424, -2508.82338043, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 30.13999794, 9.4e-05, 90.41999383, 0.00028201, 301.39997944, 0.00094003, -30.13999794, -9.4e-05, -90.41999383, -0.00028201, -301.39997944, -0.00094003, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 120.55999178, 0.02388483, 120.55999178, 0.0716545, 84.39199424, -2508.82338043, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 30.13999794, 9.4e-05, 90.41999383, 0.00028201, 301.39997944, 0.00094003, -30.13999794, -9.4e-05, -90.41999383, -0.00028201, -301.39997944, -0.00094003, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 16.5, 13.5, 8.95)
    ops.node(124023, 16.5, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.09, 28558418.57781001, 11899341.0740875, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 70.70249239, 0.00116848, 85.65234719, 0.02343541, 8.56523472, 0.0766116, -70.70249239, -0.00116848, -85.65234719, -0.02343541, -8.56523472, -0.0766116, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 75.27027731, 0.00116848, 91.18597814, 0.02343541, 9.11859781, 0.0766116, -75.27027731, -0.00116848, -91.18597814, -0.02343541, -9.11859781, -0.0766116, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 117.63054243, 0.02336955, 117.63054243, 0.07010864, 82.3413797, -2195.01412525, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 29.40763561, 9.226e-05, 88.22290682, 0.00027679, 294.07635608, 0.00092264, -29.40763561, -9.226e-05, -88.22290682, -0.00027679, -294.07635608, -0.00092264, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 117.63054243, 0.02336955, 117.63054243, 0.07010864, 82.3413797, -2195.01412525, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 29.40763561, 9.226e-05, 88.22290682, 0.00027679, 294.07635608, 0.00092264, -29.40763561, -9.226e-05, -88.22290682, -0.00027679, -294.07635608, -0.00092264, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 21.0, 13.5, 8.9)
    ops.node(124024, 21.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.09, 27059614.77549736, 11274839.48979057, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 57.26769515, 0.00108339, 69.8478019, 0.02547904, 6.98478019, 0.09314995, -57.26769515, -0.00108339, -69.8478019, -0.02547904, -6.98478019, -0.09314995, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 57.26769515, 0.00108339, 69.8478019, 0.02547904, 6.98478019, 0.09314995, -57.26769515, -0.00108339, -69.8478019, -0.02547904, -6.98478019, -0.09314995, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 125.84324137, 0.02166789, 125.84324137, 0.06500367, 88.09026896, -4356.06026029, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 31.46081034, 0.00010417, 94.38243103, 0.00031252, 314.60810342, 0.00104173, -31.46081034, -0.00010417, -94.38243103, -0.00031252, -314.60810342, -0.00104173, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 125.84324137, 0.02166789, 125.84324137, 0.06500367, 88.09026896, -4356.06026029, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 31.46081034, 0.00010417, 94.38243103, 0.00031252, 314.60810342, 0.00104173, -31.46081034, -0.00010417, -94.38243103, -0.00031252, -314.60810342, -0.00104173, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(124025, 9.0, 0.0, 1.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.1225, 27103750.5262708, 11293229.38594617, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 211.31419401, 0.00098913, 250.75243099, 0.02798888, 25.0752431, 0.06867742, -211.31419401, -0.00098913, -250.75243099, -0.02798888, -25.0752431, -0.06867742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 190.31554837, 0.00098913, 225.83474165, 0.02798888, 22.58347416, 0.06867742, -190.31554837, -0.00098913, -225.83474165, -0.02798888, -22.58347416, -0.06867742, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 301.77881686, 0.01978259, 301.77881686, 0.05934776, 211.2451718, -9202.48045244, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 75.44470422, 0.00010143, 226.33411265, 0.0003043, 754.44704216, 0.00101435, -75.44470422, -0.00010143, -226.33411265, -0.0003043, -754.44704216, -0.00101435, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 301.77881686, 0.01978259, 301.77881686, 0.05934776, 211.2451718, -9202.48045244, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 75.44470422, 0.00010143, 226.33411265, 0.0003043, 754.44704216, 0.00101435, -75.44470422, -0.00010143, -226.33411265, -0.0003043, -754.44704216, -0.00101435, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.8)
    ops.node(121003, 9.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.1225, 26094340.01984873, 10872641.67493697, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 184.10785737, 0.00098015, 218.54903366, 0.03414048, 21.85490337, 0.08397182, -184.10785737, -0.00098015, -218.54903366, -0.03414048, -21.85490337, -0.08397182, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 163.05723545, 0.00098015, 193.56045824, 0.03414048, 19.35604582, 0.08397182, -163.05723545, -0.00098015, -193.56045824, -0.03414048, -19.35604582, -0.08397182, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 339.2850981, 0.01960299, 339.2850981, 0.05880896, 237.49956867, -12651.67825626, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 84.82127452, 0.00011845, 254.46382357, 0.00035536, 848.21274524, 0.00118453, -84.82127452, -0.00011845, -254.46382357, -0.00035536, -848.21274524, -0.00118453, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 339.2850981, 0.01960299, 339.2850981, 0.05880896, 237.49956867, -12651.67825626, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 84.82127452, 0.00011845, 254.46382357, 0.00035536, 848.21274524, 0.00118453, -84.82127452, -0.00011845, -254.46382357, -0.00035536, -848.21274524, -0.00118453, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.0, 0.0, 0.0)
    ops.node(124026, 12.0, 0.0, 1.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.1225, 27868054.16704732, 11611689.23626972, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 212.89045751, 0.00096648, 252.89983005, 0.02855596, 25.28998301, 0.07296065, -212.89045751, -0.00096648, -252.89983005, -0.02855596, -25.28998301, -0.07296065, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 191.58421938, 0.00096648, 227.58942363, 0.02855596, 22.75894236, 0.07296065, -191.58421938, -0.00096648, -227.58942363, -0.02855596, -22.75894236, -0.07296065, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 302.6396769, 0.01932967, 302.6396769, 0.057989, 211.84777383, -8969.81692686, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 75.65991922, 9.893e-05, 226.97975767, 0.0002968, 756.59919225, 0.00098934, -75.65991922, -9.893e-05, -226.97975767, -0.0002968, -756.59919225, -0.00098934, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 302.6396769, 0.01932967, 302.6396769, 0.057989, 211.84777383, -8969.81692686, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 75.65991922, 9.893e-05, 226.97975767, 0.0002968, 756.59919225, 0.00098934, -75.65991922, -9.893e-05, -226.97975767, -0.0002968, -756.59919225, -0.00098934, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.8)
    ops.node(121004, 12.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.1225, 27362018.89853462, 11400841.20772276, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 183.76601196, 0.00095864, 218.63780828, 0.03566862, 21.86378083, 0.09371372, -183.76601196, -0.00095864, -218.63780828, -0.03566862, -21.86378083, -0.09371372, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 163.38008681, 0.00095864, 194.38341026, 0.03566862, 19.43834103, 0.09371372, -163.38008681, -0.00095864, -194.38341026, -0.03566862, -19.43834103, -0.09371372, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 340.36199328, 0.01917271, 340.36199328, 0.05751812, 238.25339529, -12170.64868494, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 85.09049832, 0.00011332, 255.27149496, 0.00033997, 850.90498319, 0.00113324, -85.09049832, -0.00011332, -255.27149496, -0.00033997, -850.90498319, -0.00113324, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 340.36199328, 0.01917271, 340.36199328, 0.05751812, 238.25339529, -12170.64868494, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 85.09049832, 0.00011332, 255.27149496, 0.00033997, 850.90498319, 0.00113324, -85.09049832, -0.00011332, -255.27149496, -0.00033997, -850.90498319, -0.00113324, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.35)
    ops.node(124027, 9.0, 0.0, 4.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.1225, 27417827.12192842, 11424094.63413684, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 151.90830784, 0.00089718, 181.84894366, 0.03038581, 18.18489437, 0.0844251, -151.90830784, -0.00089718, -181.84894366, -0.03038581, -18.18489437, -0.0844251, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 139.09080721, 0.00089718, 166.50515514, 0.03038581, 16.65051551, 0.0844251, -139.09080721, -0.00089718, -166.50515514, -0.03038581, -16.65051551, -0.0844251, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 298.18708384, 0.01794354, 298.18708384, 0.05383063, 208.73095869, -10168.19386212, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 74.54677096, 8.949e-05, 223.64031288, 0.00026847, 745.4677096, 0.00089491, -74.54677096, -8.949e-05, -223.64031288, -0.00026847, -745.4677096, -0.00089491, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 298.18708384, 0.01794354, 298.18708384, 0.05383063, 208.73095869, -10168.19386212, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 74.54677096, 8.949e-05, 223.64031288, 0.00026847, 745.4677096, 0.00089491, -74.54677096, -8.949e-05, -223.64031288, -0.00026847, -745.4677096, -0.00089491, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.75)
    ops.node(122003, 9.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.1225, 28172555.92647392, 11738564.96936413, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 147.07563013, 0.00089123, 176.44567376, 0.03204417, 17.64456738, 0.09297766, -147.07563013, -0.00089123, -176.44567376, -0.03204417, -17.64456738, -0.09297766, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 134.51553799, 0.00089123, 161.37741317, 0.03204417, 16.13774132, 0.09297766, -134.51553799, -0.00089123, -161.37741317, -0.03204417, -16.13774132, -0.09297766, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 301.15636248, 0.01782455, 301.15636248, 0.05347364, 210.80945374, -10637.22517062, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 75.28909062, 8.796e-05, 225.86727186, 0.00026388, 752.8909062, 0.00087961, -75.28909062, -8.796e-05, -225.86727186, -0.00026388, -752.8909062, -0.00087961, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 301.15636248, 0.01782455, 301.15636248, 0.05347364, 210.80945374, -10637.22517062, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 75.28909062, 8.796e-05, 225.86727186, 0.00026388, 752.8909062, 0.00087961, -75.28909062, -8.796e-05, -225.86727186, -0.00026388, -752.8909062, -0.00087961, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.35)
    ops.node(124028, 12.0, 0.0, 4.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.1225, 27284827.22621747, 11368678.01092395, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 151.72235705, 0.00089677, 181.61367212, 0.03064486, 18.16136721, 0.0840665, -151.72235705, -0.00089677, -181.61367212, -0.03064486, -18.16136721, -0.0840665, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 138.88376058, 0.00089677, 166.245702, 0.03064486, 16.6245702, 0.0840665, -138.88376058, -0.00089677, -166.245702, -0.03064486, -16.6245702, -0.0840665, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 302.2511835, 0.01793544, 302.2511835, 0.05380632, 211.57582845, -10574.50600173, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 75.56279588, 9.115e-05, 226.68838763, 0.00027346, 755.62795876, 0.00091153, -75.56279588, -9.115e-05, -226.68838763, -0.00027346, -755.62795876, -0.00091153, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 302.2511835, 0.01793544, 302.2511835, 0.05380632, 211.57582845, -10574.50600173, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 75.56279588, 9.115e-05, 226.68838763, 0.00027346, 755.62795876, 0.00091153, -75.56279588, -9.115e-05, -226.68838763, -0.00027346, -755.62795876, -0.00091153, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.75)
    ops.node(122004, 12.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.1225, 28391683.94148324, 11829868.30895135, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 145.83466603, 0.00088653, 174.94575249, 0.0325088, 17.49457525, 0.09435538, -145.83466603, -0.00088653, -174.94575249, -0.0325088, -17.49457525, -0.09435538, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 133.62929858, 0.00088653, 160.30398554, 0.0325088, 16.03039855, 0.09435538, -133.62929858, -0.00088653, -160.30398554, -0.0325088, -16.03039855, -0.09435538, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 305.57967463, 0.01773058, 305.57967463, 0.05319173, 213.90577224, -10909.86151898, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 76.39491866, 8.856e-05, 229.18475597, 0.00026569, 763.94918658, 0.00088564, -76.39491866, -8.856e-05, -229.18475597, -0.00026569, -763.94918658, -0.00088564, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 305.57967463, 0.01773058, 305.57967463, 0.05319173, 213.90577224, -10909.86151898, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 76.39491866, 8.856e-05, 229.18475597, 0.00026569, 763.94918658, 0.00088564, -76.39491866, -8.856e-05, -229.18475597, -0.00026569, -763.94918658, -0.00088564, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.15)
    ops.node(124029, 9.0, 0.0, 7.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.09, 27592478.06136518, 11496865.85890216, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 95.01053226, 0.00100727, 114.03345537, 0.03859126, 11.40334554, 0.10644847, -95.01053226, -0.00100727, -114.03345537, -0.03859126, -11.40334554, -0.10644847, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 90.13255769, 0.00100727, 108.17881714, 0.03859126, 10.81788171, 0.10644847, -90.13255769, -0.00100727, -108.17881714, -0.03859126, -10.81788171, -0.10644847, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 217.69678768, 0.02014538, 217.69678768, 0.06043613, 152.38775137, -9261.56820211, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 54.42419692, 8.836e-05, 163.27259076, 0.00026509, 544.24196919, 0.00088365, -54.42419692, -8.836e-05, -163.27259076, -0.00026509, -544.24196919, -0.00088365, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 217.69678768, 0.02014538, 217.69678768, 0.06043613, 152.38775137, -9261.56820211, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 54.42419692, 8.836e-05, 163.27259076, 0.00026509, 544.24196919, 0.00088365, -54.42419692, -8.836e-05, -163.27259076, -0.00026509, -544.24196919, -0.00088365, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.525)
    ops.node(123003, 9.0, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.09, 26936198.01713781, 11223415.84047409, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 90.8153799, 0.00097755, 109.34689603, 0.04057997, 10.9346896, 0.11184841, -90.8153799, -0.00097755, -109.34689603, -0.04057997, -10.9346896, -0.11184841, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 85.62022033, 0.00097755, 103.09162766, 0.04057997, 10.30916277, 0.11184841, -85.62022033, -0.00097755, -103.09162766, -0.04057997, -10.30916277, -0.11184841, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 213.67412303, 0.01955105, 213.67412303, 0.05865314, 149.57188612, -10121.61000305, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 53.41853076, 8.885e-05, 160.25559227, 0.00026654, 534.18530757, 0.00088845, -53.41853076, -8.885e-05, -160.25559227, -0.00026654, -534.18530757, -0.00088845, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 213.67412303, 0.01955105, 213.67412303, 0.05865314, 149.57188612, -10121.61000305, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 53.41853076, 8.885e-05, 160.25559227, 0.00026654, 534.18530757, 0.00088845, -53.41853076, -8.885e-05, -160.25559227, -0.00026654, -534.18530757, -0.00088845, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.15)
    ops.node(124030, 12.0, 0.0, 7.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.09, 27907378.96014513, 11628074.56672714, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 93.46599842, 0.00101057, 112.17857071, 0.03939216, 11.21785707, 0.10881187, -93.46599842, -0.00101057, -112.17857071, -0.03939216, -11.21785707, -0.10881187, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 88.92051218, 0.00101057, 106.72304508, 0.03939216, 10.67230451, 0.10881187, -88.92051218, -0.00101057, -106.72304508, -0.03939216, -10.67230451, -0.10881187, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 221.90114366, 0.02021149, 221.90114366, 0.06063446, 155.33080056, -9554.19668158, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 55.47528592, 8.906e-05, 166.42585775, 0.00026717, 554.75285915, 0.00089055, -55.47528592, -8.906e-05, -166.42585775, -0.00026717, -554.75285915, -0.00089055, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 221.90114366, 0.02021149, 221.90114366, 0.06063446, 155.33080056, -9554.19668158, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 55.47528592, 8.906e-05, 166.42585775, 0.00026717, 554.75285915, 0.00089055, -55.47528592, -8.906e-05, -166.42585775, -0.00026717, -554.75285915, -0.00089055, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.525)
    ops.node(123004, 12.0, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.09, 26633947.02369331, 11097477.92653888, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 88.26684013, 0.0009791, 106.27385451, 0.04025827, 10.62738545, 0.11000188, -88.26684013, -0.0009791, -106.27385451, -0.04025827, -10.62738545, -0.11000188, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 83.43241842, 0.0009791, 100.45317905, 0.04025827, 10.04531791, 0.11000188, -83.43241842, -0.0009791, -100.45317905, -0.04025827, -10.04531791, -0.11000188, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 214.15543948, 0.01958205, 214.15543948, 0.05874616, 149.90880764, -10299.19535577, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 53.53885987, 9.006e-05, 160.61657961, 0.00027017, 535.3885987, 0.00090056, -53.53885987, -9.006e-05, -160.61657961, -0.00027017, -535.3885987, -0.00090056, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 214.15543948, 0.01958205, 214.15543948, 0.05874616, 149.90880764, -10299.19535577, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 53.53885987, 9.006e-05, 160.61657961, 0.00027017, 535.3885987, 0.00090056, -53.53885987, -9.006e-05, -160.61657961, -0.00027017, -535.3885987, -0.00090056, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 8.925)
    ops.node(124031, 9.0, 0.0, 9.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.09, 27861423.66400119, 11608926.52666716, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 73.61523364, 0.00094242, 89.38713239, 0.0234694, 8.93871324, 0.07749192, -73.61523364, -0.00094242, -89.38713239, -0.0234694, -8.93871324, -0.07749192, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 69.10316388, 0.00094242, 83.9083618, 0.0234694, 8.39083618, 0.07749192, -69.10316388, -0.00094242, -83.9083618, -0.0234694, -8.39083618, -0.07749192, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 137.59628919, 0.0188483, 137.59628919, 0.05654491, 96.31740244, -4962.89013761, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 34.3990723, 5.531e-05, 103.1972169, 0.00016594, 343.99072298, 0.00055312, -34.3990723, -5.531e-05, -103.1972169, -0.00016594, -343.99072298, -0.00055312, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 137.59628919, 0.0188483, 137.59628919, 0.05654491, 96.31740244, -4962.89013761, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 34.3990723, 5.531e-05, 103.1972169, 0.00016594, 343.99072298, 0.00055312, -34.3990723, -5.531e-05, -103.1972169, -0.00016594, -343.99072298, -0.00055312, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 9.0, 0.0, 10.275)
    ops.node(124003, 9.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.09, 26972935.61399165, 11238723.17249652, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 70.15333194, 0.00091119, 85.56196689, 0.02550934, 8.55619669, 0.08338386, -70.15333194, -0.00091119, -85.56196689, -0.02550934, -8.55619669, -0.08338386, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 65.18979586, 0.00091119, 79.50822862, 0.02550934, 7.95082286, 0.08338386, -65.18979586, -0.00091119, -79.50822862, -0.02550934, -7.95082286, -0.08338386, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 129.7591462, 0.01822389, 129.7591462, 0.05467167, 90.83140234, -6230.74457283, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 32.43978655, 5.388e-05, 97.31935965, 0.00016164, 324.39786549, 0.0005388, -32.43978655, -5.388e-05, -97.31935965, -0.00016164, -324.39786549, -0.0005388, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 129.7591462, 0.01822389, 129.7591462, 0.05467167, 90.83140234, -6230.74457283, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 32.43978655, 5.388e-05, 97.31935965, 0.00016164, 324.39786549, 0.0005388, -32.43978655, -5.388e-05, -97.31935965, -0.00016164, -324.39786549, -0.0005388, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 8.925)
    ops.node(124032, 12.0, 0.0, 9.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.09, 27579151.78036499, 11491313.24181875, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 73.44093138, 0.00092839, 89.21163843, 0.02378399, 8.92116384, 0.07734736, -73.44093138, -0.00092839, -89.21163843, -0.02378399, -8.92116384, -0.07734736, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 68.83726113, 0.00092839, 83.61937594, 0.02378399, 8.36193759, 0.07734736, -68.83726113, -0.00092839, -83.61937594, -0.02378399, -8.36193759, -0.07734736, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 136.54297964, 0.01856778, 136.54297964, 0.05570335, 95.58008575, -4957.69075169, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 34.13574491, 5.545e-05, 102.40723473, 0.00016635, 341.35744911, 0.00055451, -34.13574491, -5.545e-05, -102.40723473, -0.00016635, -341.35744911, -0.00055451, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 136.54297964, 0.01856778, 136.54297964, 0.05570335, 95.58008575, -4957.69075169, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 34.13574491, 5.545e-05, 102.40723473, 0.00016635, 341.35744911, 0.00055451, -34.13574491, -5.545e-05, -102.40723473, -0.00016635, -341.35744911, -0.00055451, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 12.0, 0.0, 10.275)
    ops.node(124004, 12.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.09, 27046303.47489247, 11269293.11453853, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 68.82632367, 0.00092902, 83.93381551, 0.02532258, 8.39338155, 0.08329022, -68.82632367, -0.00092902, -83.93381551, -0.02532258, -8.39338155, -0.08329022, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 64.17694639, 0.00092902, 78.26389223, 0.02532258, 7.82638922, 0.08329022, -64.17694639, -0.00092902, -78.26389223, -0.02532258, -7.82638922, -0.08329022, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 132.02739222, 0.01858043, 132.02739222, 0.0557413, 92.41917455, -6543.74054727, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 33.00684806, 5.467e-05, 99.02054417, 0.00016402, 330.06848055, 0.00054673, -33.00684806, -5.467e-05, -99.02054417, -0.00016402, -330.06848055, -0.00054673, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 132.02739222, 0.01858043, 132.02739222, 0.0557413, 92.41917455, -6543.74054727, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 33.00684806, 5.467e-05, 99.02054417, 0.00016402, 330.06848055, 0.00054673, -33.00684806, -5.467e-05, -99.02054417, -0.00016402, -330.06848055, -0.00054673, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
