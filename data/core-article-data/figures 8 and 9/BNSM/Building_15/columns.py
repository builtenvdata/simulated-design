import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.1225, 24563224.2069678, 10234676.75290325, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 152.96613385, 0.0010231, 181.43198294, 0.007765, 18.14319829, 0.02200916, -152.96613385, -0.0010231, -181.43198294, -0.007765, -18.14319829, -0.02200916, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 152.96613385, 0.0010231, 181.43198294, 0.007765, 18.14319829, 0.02200916, -152.96613385, -0.0010231, -181.43198294, -0.007765, -18.14319829, -0.02200916, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 126.77690615, 0.02046195, 126.77690615, 0.06138586, 88.7438343, -1351.59613, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 31.69422654, 0.00010769, 95.08267961, 0.00032307, 316.94226536, 0.00107691, -31.69422654, -0.00010769, -95.08267961, -0.00032307, -316.94226536, -0.00107691, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 126.77690615, 0.02046195, 126.77690615, 0.06138586, 88.7438343, -1351.59613, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 31.69422654, 0.00010769, 95.08267961, 0.00032307, 316.94226536, 0.00107691, -31.69422654, -0.00010769, -95.08267961, -0.00032307, -316.94226536, -0.00107691, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 14.45, 0.0, 0.0)
    ops.node(121004, 14.45, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.1225, 27810128.47716095, 11587553.5321504, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 151.08361738, 0.00102568, 180.31169477, 0.01064149, 18.03116948, 0.03173416, -151.08361738, -0.00102568, -180.31169477, -0.01064149, -18.03116948, -0.03173416, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 151.08361738, 0.00102568, 180.31169477, 0.01064149, 18.03116948, 0.03173416, -151.08361738, -0.00102568, -180.31169477, -0.01064149, -18.03116948, -0.03173416, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 148.71044354, 0.02051361, 148.71044354, 0.06154084, 104.09731048, -1520.40386554, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 37.17761088, 0.00011157, 111.53283265, 0.00033472, 371.77610885, 0.00111574, -37.17761088, -0.00011157, -111.53283265, -0.00033472, -371.77610885, -0.00111574, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 148.71044354, 0.02051361, 148.71044354, 0.06154084, 104.09731048, -1520.40386554, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 37.17761088, 0.00011157, 111.53283265, 0.00033472, 371.77610885, 0.00111574, -37.17761088, -0.00011157, -111.53283265, -0.00033472, -371.77610885, -0.00111574, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.15, 0.0)
    ops.node(121005, 0.0, 4.15, 3.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.2025, 27334274.68746622, 11389281.11977759, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 343.81419861, 0.00084485, 410.50978799, 0.00727627, 41.0509788, 0.0219534, -343.81419861, -0.00084485, -410.50978799, -0.00727627, -41.0509788, -0.0219534, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 360.55068842, 0.00084485, 430.49294433, 0.00727627, 43.04929443, 0.0219534, -360.55068842, -0.00084485, -430.49294433, -0.00727627, -43.04929443, -0.0219534, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 199.57607775, 0.01689706, 199.57607775, 0.05069119, 139.70325443, -1761.99097952, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 49.89401944, 9.216e-05, 149.68205831, 0.00027648, 498.94019438, 0.00092159, -49.89401944, -9.216e-05, -149.68205831, -0.00027648, -498.94019438, -0.00092159, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 199.57607775, 0.01689706, 199.57607775, 0.05069119, 139.70325443, -1761.99097952, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 49.89401944, 9.216e-05, 149.68205831, 0.00027648, 498.94019438, 0.00092159, -49.89401944, -9.216e-05, -149.68205831, -0.00027648, -498.94019438, -0.00092159, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 5.8, 4.15, 0.0)
    ops.node(121006, 5.8, 4.15, 3.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.25, 27271838.44193284, 11363266.01747202, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 551.91474251, 0.00079793, 660.95711544, 0.00866986, 66.09571154, 0.02374104, -551.91474251, -0.00079793, -660.95711544, -0.00866986, -66.09571154, -0.02374104, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 608.98985304, 0.00079793, 729.30861525, 0.00866986, 72.93086153, 0.02374104, -608.98985304, -0.00079793, -729.30861525, -0.00866986, -72.93086153, -0.02374104, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 238.794315, 0.01595861, 238.794315, 0.04787584, 167.1560205, -2025.70773103, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 59.69857875, 8.952e-05, 179.09573625, 0.00026857, 596.9857875, 0.00089522, -59.69857875, -8.952e-05, -179.09573625, -0.00026857, -596.9857875, -0.00089522, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 238.794315, 0.01595861, 238.794315, 0.04787584, 167.1560205, -2025.70773103, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 59.69857875, 8.952e-05, 179.09573625, 0.00026857, 596.9857875, 0.00089522, -59.69857875, -8.952e-05, -179.09573625, -0.00026857, -596.9857875, -0.00089522, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 8.65, 4.15, 0.0)
    ops.node(121007, 8.65, 4.15, 3.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.25, 26885105.66811134, 11202127.36171306, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 545.35606208, 0.00081999, 652.93872961, 0.0091928, 65.29387296, 0.02375685, -545.35606208, -0.00081999, -652.93872961, -0.0091928, -65.29387296, -0.02375685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 599.46043929, 0.00081999, 717.71630481, 0.0091928, 71.77163048, 0.02375685, -599.46043929, -0.00081999, -717.71630481, -0.0091928, -71.77163048, -0.02375685, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 237.50626034, 0.0163999, 237.50626034, 0.04919969, 166.25438224, -2054.27676568, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 59.37656509, 9.032e-05, 178.12969526, 0.00027096, 593.76565086, 0.0009032, -59.37656509, -9.032e-05, -178.12969526, -0.00027096, -593.76565086, -0.0009032, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 237.50626034, 0.0163999, 237.50626034, 0.04919969, 166.25438224, -2054.27676568, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 59.37656509, 9.032e-05, 178.12969526, 0.00027096, 593.76565086, 0.0009032, -59.37656509, -9.032e-05, -178.12969526, -0.00027096, -593.76565086, -0.0009032, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 14.45, 4.15, 0.0)
    ops.node(121008, 14.45, 4.15, 3.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.2025, 26269377.68789311, 10945574.03662213, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 343.69251067, 0.00086338, 409.82058462, 0.00795173, 40.98205846, 0.02108092, -343.69251067, -0.00086338, -409.82058462, -0.00795173, -40.98205846, -0.02108092, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 360.3769134, 0.00086338, 429.7151458, 0.00795173, 42.97151458, 0.02108092, -360.3769134, -0.00086338, -429.7151458, -0.00795173, -42.97151458, -0.02108092, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 199.29925628, 0.01726765, 199.29925628, 0.05180296, 139.5094794, -1868.506744, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 49.82481407, 9.576e-05, 149.47444221, 0.00028729, 498.2481407, 0.00095762, -49.82481407, -9.576e-05, -149.47444221, -0.00028729, -498.2481407, -0.00095762, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 199.29925628, 0.01726765, 199.29925628, 0.05180296, 139.5094794, -1868.506744, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 49.82481407, 9.576e-05, 149.47444221, 0.00028729, 498.2481407, 0.00095762, -49.82481407, -9.576e-05, -149.47444221, -0.00028729, -498.2481407, -0.00095762, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.3, 0.0)
    ops.node(121009, 0.0, 8.3, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.1225, 28110010.77032863, 11712504.48763693, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 154.59646442, 0.0010432, 184.5322741, 0.00915918, 18.45322741, 0.03082687, -154.59646442, -0.0010432, -184.5322741, -0.00915918, -18.45322741, -0.03082687, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 154.59646442, 0.0010432, 184.5322741, 0.00915918, 18.45322741, 0.03082687, -154.59646442, -0.0010432, -184.5322741, -0.00915918, -18.45322741, -0.03082687, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 141.82249687, 0.02086402, 141.82249687, 0.06259207, 99.27574781, -1372.9172779, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 35.45562422, 0.00010527, 106.36687265, 0.00031581, 354.55624217, 0.00105271, -35.45562422, -0.00010527, -106.36687265, -0.00031581, -354.55624217, -0.00105271, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 141.82249687, 0.02086402, 141.82249687, 0.06259207, 99.27574781, -1372.9172779, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 35.45562422, 0.00010527, 106.36687265, 0.00031581, 354.55624217, 0.00105271, -35.45562422, -0.00010527, -106.36687265, -0.00031581, -354.55624217, -0.00105271, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 5.8, 8.3, 0.0)
    ops.node(121010, 5.8, 8.3, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 26746085.64158459, 11144202.35066025, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 250.10993169, 0.00096767, 298.34005723, 0.00916389, 29.83400572, 0.02675734, -250.10993169, -0.00096767, -298.34005723, -0.00916389, -29.83400572, -0.02675734, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 266.24705355, 0.00096767, 317.5889924, 0.00916389, 31.75889924, 0.02675734, -266.24705355, -0.00096767, -317.5889924, -0.00916389, -31.75889924, -0.02675734, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 174.42308175, 0.01935332, 174.42308175, 0.05805996, 122.09615722, -1725.00254094, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 43.60577044, 0.00010418, 130.81731131, 0.00031254, 436.05770437, 0.0010418, -43.60577044, -0.00010418, -130.81731131, -0.00031254, -436.05770437, -0.0010418, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 174.42308175, 0.01935332, 174.42308175, 0.05805996, 122.09615722, -1725.00254094, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 43.60577044, 0.00010418, 130.81731131, 0.00031254, 436.05770437, 0.0010418, -43.60577044, -0.00010418, -130.81731131, -0.00031254, -436.05770437, -0.0010418, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.65, 8.3, 0.0)
    ops.node(121011, 8.65, 8.3, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 26590806.84649917, 11079502.85270799, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 256.69837259, 0.00097571, 306.13307194, 0.00945538, 30.61330719, 0.02675607, -256.69837259, -0.00097571, -306.13307194, -0.00945538, -30.61330719, -0.02675607, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 273.99679912, 0.00097571, 326.76281104, 0.00945538, 32.6762811, 0.02675607, -273.99679912, -0.00097571, -326.76281104, -0.00945538, -32.6762811, -0.02675607, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 178.62459892, 0.01951428, 178.62459892, 0.05854283, 125.03721924, -1814.00709692, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 44.65614973, 0.00010731, 133.96844919, 0.00032194, 446.56149729, 0.00107313, -44.65614973, -0.00010731, -133.96844919, -0.00032194, -446.56149729, -0.00107313, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 178.62459892, 0.01951428, 178.62459892, 0.05854283, 125.03721924, -1814.00709692, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 44.65614973, 0.00010731, 133.96844919, 0.00032194, 446.56149729, 0.00107313, -44.65614973, -0.00010731, -133.96844919, -0.00032194, -446.56149729, -0.00107313, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 14.45, 8.3, 0.0)
    ops.node(121012, 14.45, 8.3, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 28118265.11555659, 11715943.79814858, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 152.49978198, 0.00099224, 182.03020256, 0.01033793, 18.20302026, 0.03202129, -152.49978198, -0.00099224, -182.03020256, -0.01033793, -18.20302026, -0.03202129, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 152.49978198, 0.00099224, 182.03020256, 0.01033793, 18.20302026, 0.03202129, -152.49978198, -0.00099224, -182.03020256, -0.01033793, -18.20302026, -0.03202129, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 150.10859852, 0.01984475, 150.10859852, 0.05953426, 105.07601897, -1523.56030149, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 37.52714963, 0.00011139, 112.58144889, 0.00033417, 375.27149631, 0.00111389, -37.52714963, -0.00011139, -112.58144889, -0.00033417, -375.27149631, -0.00111389, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 150.10859852, 0.01984475, 150.10859852, 0.05953426, 105.07601897, -1523.56030149, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 37.52714963, 0.00011139, 112.58144889, 0.00033417, 375.27149631, 0.00111389, -37.52714963, -0.00011139, -112.58144889, -0.00033417, -375.27149631, -0.00111389, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.85)
    ops.node(122001, 0.0, 0.0, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.1225, 27724003.17264619, 11551667.98860258, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 168.81984381, 0.00081229, 202.87876697, 0.01017638, 20.2878767, 0.03594031, -168.81984381, -0.00081229, -202.87876697, -0.01017638, -20.2878767, -0.03594031, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 143.13446331, 0.00081229, 172.01143403, 0.01017638, 17.2011434, 0.03594031, -143.13446331, -0.00081229, -172.01143403, -0.01017638, -17.2011434, -0.03594031, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 134.54565041, 0.01624573, 134.54565041, 0.04873719, 94.18195529, -1783.37405693, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 33.6364126, 7.274e-05, 100.90923781, 0.00021821, 336.36412603, 0.00072736, -33.6364126, -7.274e-05, -100.90923781, -0.00021821, -336.36412603, -0.00072736, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 134.54565041, 0.01624573, 134.54565041, 0.04873719, 94.18195529, -1783.37405693, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 33.6364126, 7.274e-05, 100.90923781, 0.00021821, 336.36412603, 0.00072736, -33.6364126, -7.274e-05, -100.90923781, -0.00021821, -336.36412603, -0.00072736, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 14.45, 0.0, 3.85)
    ops.node(122004, 14.45, 0.0, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.1225, 25831942.59450376, 10763309.41437657, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 165.79806152, 0.00086865, 199.09525876, 0.00974226, 19.90952588, 0.03191014, -165.79806152, -0.00086865, -199.09525876, -0.00974226, -19.90952588, -0.03191014, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 142.14566542, 0.00086865, 170.69275587, 0.00974226, 17.06927559, 0.03191014, -142.14566542, -0.00086865, -170.69275587, -0.00974226, -17.06927559, -0.03191014, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 126.08705964, 0.017373, 126.08705964, 0.05211901, 88.26094175, -1744.74203933, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 31.52176491, 7.316e-05, 94.56529473, 0.00021947, 315.21764911, 0.00073156, -31.52176491, -7.316e-05, -94.56529473, -0.00021947, -315.21764911, -0.00073156, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 126.08705964, 0.017373, 126.08705964, 0.05211901, 88.26094175, -1744.74203933, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 31.52176491, 7.316e-05, 94.56529473, 0.00021947, 315.21764911, 0.00073156, -31.52176491, -7.316e-05, -94.56529473, -0.00021947, -315.21764911, -0.00073156, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.15, 3.9)
    ops.node(122005, 0.0, 4.15, 5.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.2025, 27659086.01206975, 11524619.17169573, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 304.97223116, 0.00067741, 366.62078108, 0.00948886, 36.66207811, 0.02789234, -304.97223116, -0.00067741, -366.62078108, -0.00948886, -36.66207811, -0.02789234, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 272.42750614, 0.00067741, 327.49730921, 0.00948886, 32.74973092, 0.02789234, -272.42750614, -0.00067741, -327.49730921, -0.00948886, -32.74973092, -0.02789234, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 215.17354448, 0.01354818, 215.17354448, 0.04064453, 150.62148114, -2265.91696284, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 53.79338612, 7.053e-05, 161.38015836, 0.0002116, 537.93386121, 0.00070534, -53.79338612, -7.053e-05, -161.38015836, -0.0002116, -537.93386121, -0.00070534, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 215.17354448, 0.01354818, 215.17354448, 0.04064453, 150.62148114, -2265.91696284, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 53.79338612, 7.053e-05, 161.38015836, 0.0002116, 537.93386121, 0.00070534, -53.79338612, -7.053e-05, -161.38015836, -0.0002116, -537.93386121, -0.00070534, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 5.8, 4.15, 3.9)
    ops.node(122006, 5.8, 4.15, 5.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.25, 26153874.46889042, 10897447.69537101, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 326.90917332, 0.00065791, 393.76617183, 0.00729887, 39.37661718, 0.02391124, -326.90917332, -0.00065791, -393.76617183, -0.00729887, -39.37661718, -0.02391124, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 308.3414161, 0.00065791, 371.40107695, 0.00729887, 37.14010769, 0.02391124, -308.3414161, -0.00065791, -371.40107695, -0.00729887, -37.14010769, -0.02391124, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 250.14598798, 0.01315813, 250.14598798, 0.0394744, 175.10219159, -2245.99717529, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 62.53649699, 7.024e-05, 187.60949098, 0.00021072, 625.36496995, 0.00070241, -62.53649699, -7.024e-05, -187.60949098, -0.00021072, -625.36496995, -0.00070241, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 250.14598798, 0.01315813, 250.14598798, 0.0394744, 175.10219159, -2245.99717529, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 62.53649699, 7.024e-05, 187.60949098, 0.00021072, 625.36496995, 0.00070241, -62.53649699, -7.024e-05, -187.60949098, -0.00021072, -625.36496995, -0.00070241, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 8.65, 4.15, 3.9)
    ops.node(122007, 8.65, 4.15, 5.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.25, 28943108.3151231, 12059628.46463462, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 317.93571056, 0.00063837, 382.60116842, 0.00921909, 38.26011684, 0.02897516, -317.93571056, -0.00063837, -382.60116842, -0.00921909, -38.26011684, -0.02897516, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 300.9742592, 0.00063837, 362.18990007, 0.00921909, 36.21899001, 0.02897516, -300.9742592, -0.00063837, -362.18990007, -0.00921909, -36.21899001, -0.02897516, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 286.84554762, 0.01276744, 286.84554762, 0.03830232, 200.79188333, -2488.58827353, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 71.7113869, 7.278e-05, 215.13416071, 0.00021835, 717.11386905, 0.00072784, -71.7113869, -7.278e-05, -215.13416071, -0.00021835, -717.11386905, -0.00072784, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 286.84554762, 0.01276744, 286.84554762, 0.03830232, 200.79188333, -2488.58827353, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 71.7113869, 7.278e-05, 215.13416071, 0.00021835, 717.11386905, 0.00072784, -71.7113869, -7.278e-05, -215.13416071, -0.00021835, -717.11386905, -0.00072784, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 14.45, 4.15, 3.9)
    ops.node(122008, 14.45, 4.15, 5.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.2025, 29403977.48437407, 12251657.28515586, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 310.04253605, 0.00069836, 372.3040994, 0.00913969, 37.23040994, 0.0295485, -310.04253605, -0.00069836, -372.3040994, -0.00913969, -37.23040994, -0.0295485, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 278.12223693, 0.00069836, 333.97368717, 0.00913969, 33.39736872, 0.0295485, -278.12223693, -0.00069836, -333.97368717, -0.00913969, -33.39736872, -0.0295485, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 224.34229122, 0.01396716, 224.34229122, 0.04190148, 157.03960386, -2184.38248948, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 56.08557281, 6.918e-05, 168.25671842, 0.00020753, 560.85572806, 0.00069176, -56.08557281, -6.918e-05, -168.25671842, -0.00020753, -560.85572806, -0.00069176, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 224.34229122, 0.01396716, 224.34229122, 0.04190148, 157.03960386, -2184.38248948, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 56.08557281, 6.918e-05, 168.25671842, 0.00020753, 560.85572806, 0.00069176, -56.08557281, -6.918e-05, -168.25671842, -0.00020753, -560.85572806, -0.00069176, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.3, 3.85)
    ops.node(122009, 0.0, 8.3, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.1225, 27578734.12184899, 11491139.21743708, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 169.92376498, 0.00084015, 204.20919486, 0.01179985, 20.42091949, 0.03730754, -169.92376498, -0.00084015, -204.20919486, -0.01179985, -20.42091949, -0.03730754, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 144.69489297, 0.00084015, 173.88990644, 0.01179985, 17.38899064, 0.03730754, -144.69489297, -0.00084015, -173.88990644, -0.01179985, -17.38899064, -0.03730754, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 140.26599782, 0.0168031, 140.26599782, 0.05040929, 98.18619847, -1963.00593705, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 35.06649945, 7.623e-05, 105.19949836, 0.00022868, 350.66499455, 0.00076228, -35.06649945, -7.623e-05, -105.19949836, -0.00022868, -350.66499455, -0.00076228, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 140.26599782, 0.0168031, 140.26599782, 0.05040929, 98.18619847, -1963.00593705, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 35.06649945, 7.623e-05, 105.19949836, 0.00022868, 350.66499455, 0.00076228, -35.06649945, -7.623e-05, -105.19949836, -0.00022868, -350.66499455, -0.00076228, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 5.8, 8.3, 3.85)
    ops.node(122010, 5.8, 8.3, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 29347858.64705681, 12228274.43627367, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 187.35183713, 0.00074723, 224.96972246, 0.00985161, 22.49697225, 0.03592995, -187.35183713, -0.00074723, -224.96972246, -0.00985161, -22.49697225, -0.03592995, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 172.55726993, 0.00074723, 207.2045928, 0.00985161, 20.72045928, 0.03592995, -172.55726993, -0.00074723, -207.2045928, -0.00985161, -20.72045928, -0.03592995, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 176.80780727, 0.01494466, 176.80780727, 0.04483397, 123.76546509, -2124.717333, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 44.20195182, 6.913e-05, 132.60585545, 0.0002074, 442.01951818, 0.00069132, -44.20195182, -6.913e-05, -132.60585545, -0.0002074, -442.01951818, -0.00069132, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 176.80780727, 0.01494466, 176.80780727, 0.04483397, 123.76546509, -2124.717333, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 44.20195182, 6.913e-05, 132.60585545, 0.0002074, 442.01951818, 0.00069132, -44.20195182, -6.913e-05, -132.60585545, -0.0002074, -442.01951818, -0.00069132, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.65, 8.3, 3.85)
    ops.node(122011, 8.65, 8.3, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 25367381.45314012, 10569742.27214172, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 179.06380574, 0.00072879, 214.96926481, 0.00861249, 21.49692648, 0.02813738, -179.06380574, -0.00072879, -214.96926481, -0.00861249, -21.49692648, -0.02813738, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 164.64966165, 0.00072879, 197.66482997, 0.00861249, 19.766483, 0.02813738, -164.64966165, -0.00072879, -197.66482997, -0.00861249, -19.766483, -0.02813738, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 153.78886593, 0.01457587, 153.78886593, 0.04372761, 107.65220615, -2035.40873033, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 38.44721648, 6.957e-05, 115.34164945, 0.0002087, 384.47216484, 0.00069567, -38.44721648, -6.957e-05, -115.34164945, -0.0002087, -384.47216484, -0.00069567, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 153.78886593, 0.01457587, 153.78886593, 0.04372761, 107.65220615, -2035.40873033, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 38.44721648, 6.957e-05, 115.34164945, 0.0002087, 384.47216484, 0.00069567, -38.44721648, -6.957e-05, -115.34164945, -0.0002087, -384.47216484, -0.00069567, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 14.45, 8.3, 3.85)
    ops.node(122012, 14.45, 8.3, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 27624437.34542678, 11510182.22726116, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 168.67564445, 0.00081306, 202.7083188, 0.00961493, 20.27083188, 0.03520359, -168.67564445, -0.00081306, -202.7083188, -0.00961493, -20.27083188, -0.03520359, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 143.02439128, 0.00081306, 171.88156594, 0.00961493, 17.18815659, 0.03520359, -143.02439128, -0.00081306, -171.88156594, -0.00961493, -17.18815659, -0.03520359, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 129.1035268, 0.01626111, 129.1035268, 0.04878332, 90.37246876, -1644.58607558, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 32.2758817, 7.005e-05, 96.8276451, 0.00021014, 322.75881701, 0.00070046, -32.2758817, -7.005e-05, -96.8276451, -0.00021014, -322.75881701, -0.00070046, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 129.1035268, 0.01626111, 129.1035268, 0.04878332, 90.37246876, -1644.58607558, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 32.2758817, 7.005e-05, 96.8276451, 0.00021014, 322.75881701, 0.00070046, -32.2758817, -7.005e-05, -96.8276451, -0.00021014, -322.75881701, -0.00070046, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.4)
    ops.node(123001, 0.0, 0.0, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.09, 25208998.17220958, 10503749.23842066, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 88.69601703, 0.00093427, 106.78008552, 0.01065457, 10.67800855, 0.03636522, -88.69601703, -0.00093427, -106.78008552, -0.01065457, -10.67800855, -0.03636522, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 83.7239046, 0.00093427, 100.7942182, 0.01065457, 10.07942182, 0.03636522, -83.7239046, -0.00093427, -100.7942182, -0.01065457, -10.07942182, -0.03636522, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 97.38006739, 0.01868545, 97.38006739, 0.05605634, 68.16604718, -1503.8927508, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 24.34501685, 7.88e-05, 73.03505055, 0.00023641, 243.45016848, 0.00078803, -24.34501685, -7.88e-05, -73.03505055, -0.00023641, -243.45016848, -0.00078803, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 97.38006739, 0.01868545, 97.38006739, 0.05605634, 68.16604718, -1503.8927508, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 24.34501685, 7.88e-05, 73.03505055, 0.00023641, 243.45016848, 0.00078803, -24.34501685, -7.88e-05, -73.03505055, -0.00023641, -243.45016848, -0.00078803, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 14.45, 0.0, 6.4)
    ops.node(123004, 14.45, 0.0, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.09, 27304250.14761152, 11376770.89483813, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 85.10229881, 0.00091229, 102.5342047, 0.01240659, 10.25342047, 0.04252965, -85.10229881, -0.00091229, -102.5342047, -0.01240659, -10.25342047, -0.04252965, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 80.72090097, 0.00091229, 97.25534444, 0.01240659, 9.72553444, 0.04252965, -80.72090097, -0.00091229, -97.25534444, -0.01240659, -9.72553444, -0.04252965, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 107.53775092, 0.01824586, 107.53775092, 0.05473759, 75.27642564, -1653.57938349, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 26.88443773, 8.035e-05, 80.65331319, 0.00024104, 268.84437729, 0.00080345, -26.88443773, -8.035e-05, -80.65331319, -0.00024104, -268.84437729, -0.00080345, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 107.53775092, 0.01824586, 107.53775092, 0.05473759, 75.27642564, -1653.57938349, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 26.88443773, 8.035e-05, 80.65331319, 0.00024104, 268.84437729, 0.00080345, -26.88443773, -8.035e-05, -80.65331319, -0.00024104, -268.84437729, -0.00080345, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.15, 6.45)
    ops.node(123005, 0.0, 4.15, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 25529056.92288116, 10637107.05120048, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 160.55297197, 0.00084225, 192.38174457, 0.00869646, 19.23817446, 0.02555612, -160.55297197, -0.00084225, -192.38174457, -0.00869646, -19.23817446, -0.02555612, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 150.45924294, 0.00084225, 180.28698744, 0.00869646, 18.02869874, 0.02555612, -150.45924294, -0.00084225, -180.28698744, -0.00869646, -18.02869874, -0.02555612, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 109.0796563, 0.01684492, 109.0796563, 0.05053477, 76.35575941, -1556.87610004, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 27.26991408, 6.404e-05, 81.80974223, 0.00019212, 272.69914076, 0.00064039, -27.26991408, -6.404e-05, -81.80974223, -0.00019212, -272.69914076, -0.00064039, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 109.0796563, 0.01684492, 109.0796563, 0.05053477, 76.35575941, -1556.87610004, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 27.26991408, 6.404e-05, 81.80974223, 0.00019212, 272.69914076, 0.00064039, -27.26991408, -6.404e-05, -81.80974223, -0.00019212, -272.69914076, -0.00064039, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 5.8, 4.15, 6.45)
    ops.node(123006, 5.8, 4.15, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.16, 25777876.2481099, 10740781.77004579, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 177.2975171, 0.00074506, 213.25336423, 0.00876547, 21.32533642, 0.02642415, -177.2975171, -0.00074506, -213.25336423, -0.00876547, -21.32533642, -0.02642415, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 177.2975171, 0.00074506, 213.25336423, 0.00876547, 21.32533642, 0.02642415, -177.2975171, -0.00074506, -213.25336423, -0.00876547, -21.32533642, -0.02642415, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 146.91744158, 0.01490122, 146.91744158, 0.04470365, 102.84220911, -1811.08586829, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 36.7293604, 6.54e-05, 110.18808119, 0.0001962, 367.29360396, 0.000654, -36.7293604, -6.54e-05, -110.18808119, -0.0001962, -367.29360396, -0.000654, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 146.91744158, 0.01490122, 146.91744158, 0.04470365, 102.84220911, -1811.08586829, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 36.7293604, 6.54e-05, 110.18808119, 0.0001962, 367.29360396, 0.000654, -36.7293604, -6.54e-05, -110.18808119, -0.0001962, -367.29360396, -0.000654, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 8.65, 4.15, 6.45)
    ops.node(123007, 8.65, 4.15, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.16, 28011290.64789016, 11671371.10328757, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 177.94193919, 0.00075442, 214.10087786, 0.00909982, 21.41008779, 0.0298689, -177.94193919, -0.00075442, -214.10087786, -0.00909982, -21.41008779, -0.0298689, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 177.94193919, 0.00075442, 214.10087786, 0.00909982, 21.41008779, 0.0298689, -177.94193919, -0.00075442, -214.10087786, -0.00909982, -21.41008779, -0.0298689, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 157.68277743, 0.01508842, 157.68277743, 0.04526526, 110.3779442, -1808.70496859, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 39.42069436, 6.46e-05, 118.26208307, 0.00019379, 394.20694357, 0.00064596, -39.42069436, -6.46e-05, -118.26208307, -0.00019379, -394.20694357, -0.00064596, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 157.68277743, 0.01508842, 157.68277743, 0.04526526, 110.3779442, -1808.70496859, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 39.42069436, 6.46e-05, 118.26208307, 0.00019379, 394.20694357, 0.00064596, -39.42069436, -6.46e-05, -118.26208307, -0.00019379, -394.20694357, -0.00064596, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 14.45, 4.15, 6.45)
    ops.node(123008, 14.45, 4.15, 8.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 26384825.93716229, 10993677.47381762, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 168.70011021, 0.00079917, 202.34430215, 0.00940046, 20.23443021, 0.02772193, -168.70011021, -0.00079917, -202.34430215, -0.00940046, -20.23443021, -0.02772193, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 156.84996073, 0.00079917, 188.13085425, 0.00940046, 18.81308543, 0.02772193, -156.84996073, -0.00079917, -188.13085425, -0.00940046, -18.81308543, -0.02772193, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 121.26030035, 0.01598341, 121.26030035, 0.04795024, 84.88221024, -1617.90757758, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 30.31507509, 6.888e-05, 90.94522526, 0.00020664, 303.15075087, 0.00068881, -30.31507509, -6.888e-05, -90.94522526, -0.00020664, -303.15075087, -0.00068881, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 121.26030035, 0.01598341, 121.26030035, 0.04795024, 84.88221024, -1617.90757758, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 30.31507509, 6.888e-05, 90.94522526, 0.00020664, 303.15075087, 0.00068881, -30.31507509, -6.888e-05, -90.94522526, -0.00020664, -303.15075087, -0.00068881, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.3, 6.4)
    ops.node(123009, 0.0, 8.3, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.09, 25619034.26883273, 10674597.61201364, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 87.43353647, 0.00087807, 105.29917678, 0.00980515, 10.52991768, 0.03644471, -87.43353647, -0.00087807, -105.29917678, -0.00980515, -10.52991768, -0.03644471, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 82.32762127, 0.00087807, 99.14994973, 0.00980515, 9.91499497, 0.03644471, -82.32762127, -0.00087807, -99.14994973, -0.00980515, -9.91499497, -0.03644471, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 85.70955263, 0.01756142, 85.70955263, 0.05268425, 59.99668684, -1342.5822287, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 21.42738816, 6.825e-05, 64.28216447, 0.00020475, 214.27388157, 0.00068249, -21.42738816, -6.825e-05, -64.28216447, -0.00020475, -214.27388157, -0.00068249, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 85.70955263, 0.01756142, 85.70955263, 0.05268425, 59.99668684, -1342.5822287, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 21.42738816, 6.825e-05, 64.28216447, 0.00020475, 214.27388157, 0.00068249, -21.42738816, -6.825e-05, -64.28216447, -0.00020475, -214.27388157, -0.00068249, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 5.8, 8.3, 6.4)
    ops.node(123010, 5.8, 8.3, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 26354583.35465271, 10981076.39777196, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 113.90758255, 0.00079255, 137.33244697, 0.01076547, 13.7332447, 0.03658577, -113.90758255, -0.00079255, -137.33244697, -0.01076547, -13.7332447, -0.03658577, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 108.3628486, 0.00079255, 130.64744967, 0.01076547, 13.06474497, 0.03658577, -108.3628486, -0.00079255, -130.64744967, -0.01076547, -13.06474497, -0.03658577, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 127.33177649, 0.01585103, 127.33177649, 0.04755309, 89.13224355, -1770.3754036, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 31.83294412, 7.241e-05, 95.49883237, 0.00021724, 318.32944124, 0.00072413, -31.83294412, -7.241e-05, -95.49883237, -0.00021724, -318.32944124, -0.00072413, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 127.33177649, 0.01585103, 127.33177649, 0.04755309, 89.13224355, -1770.3754036, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 31.83294412, 7.241e-05, 95.49883237, 0.00021724, 318.32944124, 0.00072413, -31.83294412, -7.241e-05, -95.49883237, -0.00021724, -318.32944124, -0.00072413, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.65, 8.3, 6.4)
    ops.node(123011, 8.65, 8.3, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 26971058.91961571, 11237941.21650655, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 118.21982718, 0.00079366, 142.5347624, 0.01177688, 14.25347624, 0.03869957, -118.21982718, -0.00079366, -142.5347624, -0.01177688, -14.25347624, -0.03869957, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 112.12627014, 0.00079366, 135.18790929, 0.01177688, 13.51879093, 0.03869957, -112.12627014, -0.00079366, -135.18790929, -0.01177688, -13.51879093, -0.03869957, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 134.18292612, 0.01587318, 134.18292612, 0.04761955, 93.92804828, -1912.89634129, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 33.54573153, 7.457e-05, 100.63719459, 0.0002237, 335.45731529, 0.00074565, -33.54573153, -7.457e-05, -100.63719459, -0.0002237, -335.45731529, -0.00074565, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 134.18292612, 0.01587318, 134.18292612, 0.04761955, 93.92804828, -1912.89634129, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 33.54573153, 7.457e-05, 100.63719459, 0.0002237, 335.45731529, 0.00074565, -33.54573153, -7.457e-05, -100.63719459, -0.0002237, -335.45731529, -0.00074565, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 14.45, 8.3, 6.4)
    ops.node(123012, 14.45, 8.3, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.09, 27469101.87824628, 11445459.11593595, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 89.83835655, 0.00090988, 108.2353348, 0.0111273, 10.82353348, 0.0415628, -89.83835655, -0.00090988, -108.2353348, -0.0111273, -10.82353348, -0.0415628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 84.76339742, 0.00090988, 102.12113234, 0.0111273, 10.21211323, 0.0415628, -84.76339742, -0.00090988, -102.12113234, -0.0111273, -10.21211323, -0.0415628, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 99.52305623, 0.01819758, 99.52305623, 0.05459275, 69.66613936, -1381.22662324, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 24.88076406, 7.391e-05, 74.64229217, 0.00022173, 248.80764057, 0.00073911, -24.88076406, -7.391e-05, -74.64229217, -0.00022173, -248.80764057, -0.00073911, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 99.52305623, 0.01819758, 99.52305623, 0.05459275, 69.66613936, -1381.22662324, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 24.88076406, 7.391e-05, 74.64229217, 0.00022173, 248.80764057, 0.00073911, -24.88076406, -7.391e-05, -74.64229217, -0.00022173, -248.80764057, -0.00073911, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.95)
    ops.node(124001, 0.0, 0.0, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.09, 26253179.92213515, 10938824.96755631, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 67.48190068, 0.00085536, 82.32223043, 0.01254577, 8.23222304, 0.05320631, -67.48190068, -0.00085536, -82.32223043, -0.01254577, -8.23222304, -0.05320631, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 63.11485661, 0.00085536, 76.99480478, 0.01254577, 7.69948048, 0.05320631, -63.11485661, -0.00085536, -76.99480478, -0.01254577, -7.69948048, -0.05320631, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 82.62655856, 0.01710719, 82.62655856, 0.05132157, 57.83859099, -1444.93291909, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 20.65663964, 6.42e-05, 61.96991892, 0.00019261, 206.5663964, 0.00064205, -20.65663964, -6.42e-05, -61.96991892, -0.00019261, -206.5663964, -0.00064205, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 82.62655856, 0.01710719, 82.62655856, 0.05132157, 57.83859099, -1444.93291909, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 20.65663964, 6.42e-05, 61.96991892, 0.00019261, 206.5663964, 0.00064205, -20.65663964, -6.42e-05, -61.96991892, -0.00019261, -206.5663964, -0.00064205, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 14.45, 0.0, 8.95)
    ops.node(124004, 14.45, 0.0, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.09, 28204584.60188689, 11751910.25078621, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 71.4264832, 0.00086971, 86.87118901, 0.01186614, 8.6871189, 0.05446868, -71.4264832, -0.00086971, -86.87118901, -0.01186614, -8.6871189, -0.05446868, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 66.70657614, 0.00086971, 81.13068605, 0.01186614, 8.11306861, 0.05446868, -66.70657614, -0.00086971, -81.13068605, -0.01186614, -8.11306861, -0.05446868, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 83.02948148, 0.01739411, 83.02948148, 0.05218233, 58.12063704, -1363.22628058, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 20.75737037, 6.005e-05, 62.27211111, 0.00018016, 207.57370371, 0.00060054, -20.75737037, -6.005e-05, -62.27211111, -0.00018016, -207.57370371, -0.00060054, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 83.02948148, 0.01739411, 83.02948148, 0.05218233, 58.12063704, -1363.22628058, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 20.75737037, 6.005e-05, 62.27211111, 0.00018016, 207.57370371, 0.00060054, -20.75737037, -6.005e-05, -62.27211111, -0.00018016, -207.57370371, -0.00060054, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.15, 9.0)
    ops.node(124005, 0.0, 4.15, 10.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 27532434.52446334, 11471847.71852639, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 130.80454934, 0.00081798, 158.86292759, 0.0099876, 15.88629276, 0.03874626, -130.80454934, -0.00081798, -158.86292759, -0.0099876, -15.88629276, -0.03874626, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 121.61646342, 0.00081798, 147.70394087, 0.0099876, 14.77039409, 0.03874626, -121.61646342, -0.00081798, -147.70394087, -0.0099876, -14.77039409, -0.03874626, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 88.46097838, 0.01635961, 88.46097838, 0.04907882, 61.92268486, -1119.8294068, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 22.11524459, 4.816e-05, 66.34573378, 0.00014447, 221.15244594, 0.00048155, -22.11524459, -4.816e-05, -66.34573378, -0.00014447, -221.15244594, -0.00048155, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 88.46097838, 0.01635961, 88.46097838, 0.04907882, 61.92268486, -1119.8294068, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 22.11524459, 4.816e-05, 66.34573378, 0.00014447, 221.15244594, 0.00048155, -22.11524459, -4.816e-05, -66.34573378, -0.00014447, -221.15244594, -0.00048155, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 5.8, 4.15, 9.0)
    ops.node(124006, 5.8, 4.15, 10.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.16, 27624398.41257858, 11510166.00524108, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 137.69205766, 0.00070349, 167.31241585, 0.00936794, 16.73124159, 0.03644495, -137.69205766, -0.00070349, -167.31241585, -0.00936794, -16.73124159, -0.03644495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 137.69205766, 0.00070349, 167.31241585, 0.00936794, 16.73124159, 0.03644495, -137.69205766, -0.00070349, -167.31241585, -0.00936794, -16.73124159, -0.03644495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 131.28920865, 0.01406983, 131.28920865, 0.04220949, 91.90244606, -1368.58168204, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 32.82230216, 5.454e-05, 98.46690649, 0.00016361, 328.22302163, 0.00054537, -32.82230216, -5.454e-05, -98.46690649, -0.00016361, -328.22302163, -0.00054537, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 131.28920865, 0.01406983, 131.28920865, 0.04220949, 91.90244606, -1368.58168204, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 32.82230216, 5.454e-05, 98.46690649, 0.00016361, 328.22302163, 0.00054537, -32.82230216, -5.454e-05, -98.46690649, -0.00016361, -328.22302163, -0.00054537, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 8.65, 4.15, 9.0)
    ops.node(124007, 8.65, 4.15, 10.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.16, 27130705.82017782, 11304460.75840742, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 132.77448943, 0.00070973, 161.44507394, 0.01075859, 16.14450739, 0.03743074, -132.77448943, -0.00070973, -161.44507394, -0.01075859, -16.14450739, -0.03743074, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 132.77448943, 0.00070973, 161.44507394, 0.01075859, 16.14450739, 0.03743074, -132.77448943, -0.00070973, -161.44507394, -0.01075859, -16.14450739, -0.03743074, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 134.96227842, 0.01419463, 134.96227842, 0.04258388, 94.47359489, -1536.43047183, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 33.7405696, 5.708e-05, 101.22170881, 0.00017125, 337.40569604, 0.00057083, -33.7405696, -5.708e-05, -101.22170881, -0.00017125, -337.40569604, -0.00057083, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 134.96227842, 0.01419463, 134.96227842, 0.04258388, 94.47359489, -1536.43047183, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 33.7405696, 5.708e-05, 101.22170881, 0.00017125, 337.40569604, 0.00057083, -33.7405696, -5.708e-05, -101.22170881, -0.00017125, -337.40569604, -0.00057083, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 14.45, 4.15, 9.0)
    ops.node(124008, 14.45, 4.15, 10.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 28993110.08850084, 12080462.53687535, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 135.74857741, 0.00079827, 164.48220922, 0.01094966, 16.44822092, 0.04093964, -135.74857741, -0.00079827, -164.48220922, -0.01094966, -16.44822092, -0.04093964, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 125.68539282, 0.00079827, 152.28897032, 0.01094966, 15.22889703, 0.04093964, -125.68539282, -0.00079827, -152.28897032, -0.01094966, -15.22889703, -0.04093964, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 107.68806648, 0.01596541, 107.68806648, 0.04789624, 75.38164653, -1261.54232736, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 26.92201662, 5.567e-05, 80.76604986, 0.00016701, 269.22016619, 0.00055668, -26.92201662, -5.567e-05, -80.76604986, -0.00016701, -269.22016619, -0.00055668, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 107.68806648, 0.01596541, 107.68806648, 0.04789624, 75.38164653, -1261.54232736, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 26.92201662, 5.567e-05, 80.76604986, 0.00016701, 269.22016619, 0.00055668, -26.92201662, -5.567e-05, -80.76604986, -0.00016701, -269.22016619, -0.00055668, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.3, 8.95)
    ops.node(124009, 0.0, 8.3, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.09, 27939068.65764095, 11641278.60735039, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 69.26126151, 0.00092183, 84.27858503, 0.01292254, 8.4278585, 0.05528991, -69.26126151, -0.00092183, -84.27858503, -0.01292254, -8.4278585, -0.05528991, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 65.18124329, 0.00092183, 79.31393156, 0.01292254, 7.93139316, 0.05528991, -65.18124329, -0.00092183, -79.31393156, -0.01292254, -7.93139316, -0.05528991, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 89.70872991, 0.01843668, 89.70872991, 0.05531004, 62.79611094, -1545.07231675, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 22.42718248, 6.55e-05, 67.28154744, 0.00019651, 224.27182479, 0.00065502, -22.42718248, -6.55e-05, -67.28154744, -0.00019651, -224.27182479, -0.00065502, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 89.70872991, 0.01843668, 89.70872991, 0.05531004, 62.79611094, -1545.07231675, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 22.42718248, 6.55e-05, 67.28154744, 0.00019651, 224.27182479, 0.00065502, -22.42718248, -6.55e-05, -67.28154744, -0.00019651, -224.27182479, -0.00065502, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 5.8, 8.3, 8.95)
    ops.node(124010, 5.8, 8.3, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 26018517.25641327, 10841048.85683887, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 89.14649776, 0.00075701, 108.75055975, 0.01326133, 10.87505597, 0.04914132, -89.14649776, -0.00075701, -108.75055975, -0.01326133, -10.87505597, -0.04914132, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 83.55338753, 0.00075701, 101.92747771, 0.01326133, 10.19274777, 0.04914132, -83.55338753, -0.00075701, -101.92747771, -0.01326133, -10.19274777, -0.04914132, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 112.72887358, 0.01514017, 112.72887358, 0.0454205, 78.9102115, -1916.14928979, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 28.18221839, 6.494e-05, 84.54665518, 0.00019481, 281.82218394, 0.00064937, -28.18221839, -6.494e-05, -84.54665518, -0.00019481, -281.82218394, -0.00064937, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 112.72887358, 0.01514017, 112.72887358, 0.0454205, 78.9102115, -1916.14928979, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 28.18221839, 6.494e-05, 84.54665518, 0.00019481, 281.82218394, 0.00064937, -28.18221839, -6.494e-05, -84.54665518, -0.00019481, -281.82218394, -0.00064937, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.65, 8.3, 8.95)
    ops.node(124011, 8.65, 8.3, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 28488648.32723416, 11870270.13634757, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 85.22262858, 0.0007717, 103.57254676, 0.01240983, 10.35725468, 0.0505545, -85.22262858, -0.0007717, -103.57254676, -0.01240983, -10.35725468, -0.0505545, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 80.53763942, 0.0007717, 97.87879774, 0.01240983, 9.78787977, 0.0505545, -80.53763942, -0.0007717, -97.87879774, -0.01240983, -9.78787977, -0.0505545, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 116.83589637, 0.01543391, 116.83589637, 0.04630174, 81.78512746, -1700.46530616, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 29.20897409, 6.147e-05, 87.62692228, 0.0001844, 292.08974094, 0.00061467, -29.20897409, -6.147e-05, -87.62692228, -0.0001844, -292.08974094, -0.00061467, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 116.83589637, 0.01543391, 116.83589637, 0.04630174, 81.78512746, -1700.46530616, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 29.20897409, 6.147e-05, 87.62692228, 0.0001844, 292.08974094, 0.00061467, -29.20897409, -6.147e-05, -87.62692228, -0.0001844, -292.08974094, -0.00061467, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 14.45, 8.3, 8.95)
    ops.node(124012, 14.45, 8.3, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.09, 30761984.08654795, 12817493.36939498, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 68.96386772, 0.00085056, 83.39211352, 0.01396139, 8.33921135, 0.05845434, -68.96386772, -0.00085056, -83.39211352, -0.01396139, -8.33921135, -0.05845434, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 64.63446355, 0.00085056, 78.15693492, 0.01396139, 7.81569349, 0.05845434, -64.63446355, -0.00085056, -78.15693492, -0.01396139, -7.81569349, -0.05845434, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 101.01649444, 0.01701122, 101.01649444, 0.05103366, 70.7115461, -1754.95412394, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 25.25412361, 6.699e-05, 75.76237083, 0.00020097, 252.54123609, 0.0006699, -25.25412361, -6.699e-05, -75.76237083, -0.00020097, -252.54123609, -0.0006699, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 101.01649444, 0.01701122, 101.01649444, 0.05103366, 70.7115461, -1754.95412394, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 25.25412361, 6.699e-05, 75.76237083, 0.00020097, 252.54123609, 0.0006699, -25.25412361, -6.699e-05, -75.76237083, -0.00020097, -252.54123609, -0.0006699, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 5.8, 0.0, 0.0)
    ops.node(124013, 5.8, 0.0, 1.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4030, 170002, 124013, 0.16, 27602684.34676113, 11501118.47781714, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24030, 298.18705291, 0.00066343, 355.54065896, 0.01020973, 35.5540659, 0.0286567, -298.18705291, -0.00066343, -355.54065896, -0.01020973, -35.5540659, -0.0286567, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14030, 306.96288233, 0.00066343, 366.00444048, 0.01020973, 36.60044405, 0.0286567, -306.96288233, -0.00066343, -366.00444048, -0.01020973, -36.60044405, -0.0286567, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24030, 4030, 0.0, 245.21598646, 0.01326853, 245.21598646, 0.0398056, 171.65119052, -3757.03218142, 0.05, 2, 0, 70002, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 44030, 61.30399661, 7.096e-05, 183.91198984, 0.00021288, 613.03996615, 0.00070959, -61.30399661, -7.096e-05, -183.91198984, -0.00021288, -613.03996615, -0.00070959, 0.4, 0.3, 0.003, 0.0, 0.0, 24030, 2)
    ops.limitCurve('ThreePoint', 14030, 4030, 0.0, 245.21598646, 0.01326853, 245.21598646, 0.0398056, 171.65119052, -3757.03218142, 0.05, 2, 0, 70002, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 34030, 61.30399661, 7.096e-05, 183.91198984, 0.00021288, 613.03996615, 0.00070959, -61.30399661, -7.096e-05, -183.91198984, -0.00021288, -613.03996615, -0.00070959, 0.4, 0.3, 0.003, 0.0, 0.0, 14030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4030, 99999, 'P', 44030, 'Vy', 34030, 'Vz', 24030, 'My', 14030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 4030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174013, 5.8, 0.0, 2.025)
    ops.node(121002, 5.8, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4031, 174013, 121002, 0.16, 29706044.79564267, 12377518.66485111, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24031, 244.52845261, 0.00066522, 291.99696361, 0.00866469, 29.19969636, 0.03143621, -244.52845261, -0.00066522, -291.99696361, -0.00866469, -29.19969636, -0.03143621, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14031, 214.8482858, 0.00066522, 256.5552042, 0.00866469, 25.65552042, 0.03143621, -214.8482858, -0.00066522, -256.5552042, -0.00866469, -25.65552042, -0.03143621, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24031, 4031, 0.0, 245.15545648, 0.01330443, 245.15545648, 0.03991328, 171.60881953, -3225.5839335, 0.05, 2, 0, 74013, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44031, 61.28886412, 6.592e-05, 183.86659236, 0.00019776, 612.88864119, 0.00065919, -61.28886412, -6.592e-05, -183.86659236, -0.00019776, -612.88864119, -0.00065919, 0.4, 0.3, 0.003, 0.0, 0.0, 24031, 2)
    ops.limitCurve('ThreePoint', 14031, 4031, 0.0, 245.15545648, 0.01330443, 245.15545648, 0.03991328, 171.60881953, -3225.5839335, 0.05, 2, 0, 74013, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34031, 61.28886412, 6.592e-05, 183.86659236, 0.00019776, 612.88864119, 0.00065919, -61.28886412, -6.592e-05, -183.86659236, -0.00019776, -612.88864119, -0.00065919, 0.4, 0.3, 0.003, 0.0, 0.0, 14031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4031, 99999, 'P', 44031, 'Vy', 34031, 'Vz', 24031, 'My', 14031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174013, 74013, 174013, 4031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.65, 0.0, 0.0)
    ops.node(124014, 8.65, 0.0, 1.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4032, 170003, 124014, 0.16, 26935038.34657495, 11222932.64440623, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24032, 288.79969654, 0.00069736, 344.09543973, 0.00978567, 34.40954397, 0.02700643, -288.79969654, -0.00069736, -344.09543973, -0.00978567, -34.40954397, -0.02700643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14032, 296.44249416, 0.00069736, 353.20158437, 0.00978567, 35.32015844, 0.02700643, -296.44249416, -0.00069736, -353.20158437, -0.00978567, -35.32015844, -0.02700643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24032, 4032, 0.0, 240.86549288, 0.01394717, 240.86549288, 0.0418415, 168.60584502, -3780.24876822, 0.05, 2, 0, 70003, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 44032, 60.21637322, 7.143e-05, 180.64911966, 0.00021428, 602.16373221, 0.00071428, -60.21637322, -7.143e-05, -180.64911966, -0.00021428, -602.16373221, -0.00071428, 0.4, 0.3, 0.003, 0.0, 0.0, 24032, 2)
    ops.limitCurve('ThreePoint', 14032, 4032, 0.0, 240.86549288, 0.01394717, 240.86549288, 0.0418415, 168.60584502, -3780.24876822, 0.05, 2, 0, 70003, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 34032, 60.21637322, 7.143e-05, 180.64911966, 0.00021428, 602.16373221, 0.00071428, -60.21637322, -7.143e-05, -180.64911966, -0.00021428, -602.16373221, -0.00071428, 0.4, 0.3, 0.003, 0.0, 0.0, 14032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4032, 99999, 'P', 44032, 'Vy', 34032, 'Vz', 24032, 'My', 14032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 4032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174014, 8.65, 0.0, 2.025)
    ops.node(121003, 8.65, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4033, 174014, 121003, 0.16, 27884144.93644137, 11618393.72351724, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24033, 243.12732607, 0.00063794, 290.37242336, 0.00923295, 29.03724234, 0.02901934, -243.12732607, -0.00063794, -290.37242336, -0.00923295, -29.03724234, -0.02901934, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14033, 211.18814725, 0.00063794, 252.22674511, 0.00923295, 25.22267451, 0.02901934, -211.18814725, -0.00063794, -252.22674511, -0.00923295, -25.22267451, -0.02901934, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24033, 4033, 0.0, 235.88116763, 0.01275883, 235.88116763, 0.03827649, 165.11681734, -3381.83478755, 0.05, 2, 0, 74014, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44033, 58.97029191, 6.757e-05, 176.91087573, 0.00020271, 589.70291908, 0.00067569, -58.97029191, -6.757e-05, -176.91087573, -0.00020271, -589.70291908, -0.00067569, 0.4, 0.3, 0.003, 0.0, 0.0, 24033, 2)
    ops.limitCurve('ThreePoint', 14033, 4033, 0.0, 235.88116763, 0.01275883, 235.88116763, 0.03827649, 165.11681734, -3381.83478755, 0.05, 2, 0, 74014, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34033, 58.97029191, 6.757e-05, 176.91087573, 0.00020271, 589.70291908, 0.00067569, -58.97029191, -6.757e-05, -176.91087573, -0.00020271, -589.70291908, -0.00067569, 0.4, 0.3, 0.003, 0.0, 0.0, 14033, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4033, 99999, 'P', 44033, 'Vy', 34033, 'Vz', 24033, 'My', 14033, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174014, 74014, 174014, 4033, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4033, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 5.8, 0.0, 3.85)
    ops.node(124015, 5.8, 0.0, 4.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4035, 171002, 124015, 0.16, 27301843.93728144, 11375768.3072006, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24035, 181.57113873, 0.00060579, 218.05422391, 0.0092284, 21.80542239, 0.03159071, -181.57113873, -0.00060579, -218.05422391, -0.0092284, -21.80542239, -0.03159071, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14035, 168.70377765, 0.00060579, 202.60142422, 0.0092284, 20.26014242, 0.03159071, -168.70377765, -0.00060579, -202.60142422, -0.0092284, -20.26014242, -0.03159071, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24035, 4035, 0.0, 282.58176895, 0.01211585, 282.58176895, 0.03634754, 197.80723826, -4204.14834611, 0.05, 2, 0, 71002, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 44035, 70.64544224, 5.938e-05, 211.93632671, 0.00017815, 706.45442237, 0.00059385, -70.64544224, -5.938e-05, -211.93632671, -0.00017815, -706.45442237, -0.00059385, 0.4, 0.3, 0.003, 0.0, 0.0, 24035, 2)
    ops.limitCurve('ThreePoint', 14035, 4035, 0.0, 282.58176895, 0.01211585, 282.58176895, 0.03634754, 197.80723826, -4204.14834611, 0.05, 2, 0, 71002, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 34035, 70.64544224, 5.938e-05, 211.93632671, 0.00017815, 706.45442237, 0.00059385, -70.64544224, -5.938e-05, -211.93632671, -0.00017815, -706.45442237, -0.00059385, 0.4, 0.3, 0.003, 0.0, 0.0, 14035, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4035, 99999, 'P', 44035, 'Vy', 34035, 'Vz', 24035, 'My', 14035, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4035, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 4035, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174015, 5.8, 0.0, 5.0)
    ops.node(122002, 5.8, 0.0, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4036, 174015, 122002, 0.16, 27340209.43542022, 11391753.93142509, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24036, 181.97741033, 0.00059398, 218.8481065, 0.00864848, 21.88481065, 0.0320264, -181.97741033, -0.00059398, -218.8481065, -0.00864848, -21.88481065, -0.0320264, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14036, 167.40319802, 0.00059398, 201.32099276, 0.00864848, 20.13209928, 0.0320264, -167.40319802, -0.00059398, -201.32099276, -0.00864848, -20.13209928, -0.0320264, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24036, 4036, 0.0, 273.37520271, 0.01187965, 273.37520271, 0.03563896, 191.3626419, -3848.47203627, 0.05, 2, 0, 74015, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44036, 68.34380068, 5.737e-05, 205.03140203, 0.00017211, 683.43800678, 0.00057369, -68.34380068, -5.737e-05, -205.03140203, -0.00017211, -683.43800678, -0.00057369, 0.4, 0.3, 0.003, 0.0, 0.0, 24036, 2)
    ops.limitCurve('ThreePoint', 14036, 4036, 0.0, 273.37520271, 0.01187965, 273.37520271, 0.03563896, 191.3626419, -3848.47203627, 0.05, 2, 0, 74015, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34036, 68.34380068, 5.737e-05, 205.03140203, 0.00017211, 683.43800678, 0.00057369, -68.34380068, -5.737e-05, -205.03140203, -0.00017211, -683.43800678, -0.00057369, 0.4, 0.3, 0.003, 0.0, 0.0, 14036, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4036, 99999, 'P', 44036, 'Vy', 34036, 'Vz', 24036, 'My', 14036, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174015, 74015, 174015, 4036, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4036, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.65, 0.0, 3.85)
    ops.node(124016, 8.65, 0.0, 4.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4037, 171003, 124016, 0.16, 28891551.43561214, 12038146.43150506, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24037, 189.01621007, 0.00060229, 226.88934902, 0.0100606, 22.6889349, 0.03492275, -189.01621007, -0.00060229, -226.88934902, -0.0100606, -22.6889349, -0.03492275, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14037, 174.66976462, 0.00060229, 209.66830926, 0.0100606, 20.96683093, 0.03492275, -174.66976462, -0.00060229, -209.66830926, -0.0100606, -20.96683093, -0.03492275, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24037, 4037, 0.0, 302.04845472, 0.01204575, 302.04845472, 0.03613724, 211.4339183, -4391.20881421, 0.05, 2, 0, 71003, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 44037, 75.51211368, 5.998e-05, 226.53634104, 0.00017995, 755.12113679, 0.00059983, -75.51211368, -5.998e-05, -226.53634104, -0.00017995, -755.12113679, -0.00059983, 0.4, 0.3, 0.003, 0.0, 0.0, 24037, 2)
    ops.limitCurve('ThreePoint', 14037, 4037, 0.0, 302.04845472, 0.01204575, 302.04845472, 0.03613724, 211.4339183, -4391.20881421, 0.05, 2, 0, 71003, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 34037, 75.51211368, 5.998e-05, 226.53634104, 0.00017995, 755.12113679, 0.00059983, -75.51211368, -5.998e-05, -226.53634104, -0.00017995, -755.12113679, -0.00059983, 0.4, 0.3, 0.003, 0.0, 0.0, 14037, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4037, 99999, 'P', 44037, 'Vy', 34037, 'Vz', 24037, 'My', 14037, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4037, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 4037, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174016, 8.65, 0.0, 5.0)
    ops.node(122003, 8.65, 0.0, 5.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4038, 174016, 122003, 0.16, 27751050.16911313, 11562937.57046381, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24038, 186.34459724, 0.00059332, 224.08638442, 0.0103512, 22.40863844, 0.03438673, -186.34459724, -0.00059332, -224.08638442, -0.0103512, -22.40863844, -0.03438673, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14038, 170.808941, 0.00059332, 205.40417368, 0.0103512, 20.54041737, 0.03438673, -170.808941, -0.00059332, -205.40417368, -0.0103512, -20.54041737, -0.03438673, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24038, 4038, 0.0, 290.816142, 0.01186634, 290.816142, 0.03559903, 203.5712994, -4572.91583937, 0.05, 2, 0, 74016, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44038, 72.7040355, 6.013e-05, 218.1121065, 0.00018038, 727.04035499, 0.00060126, -72.7040355, -6.013e-05, -218.1121065, -0.00018038, -727.04035499, -0.00060126, 0.4, 0.3, 0.003, 0.0, 0.0, 24038, 2)
    ops.limitCurve('ThreePoint', 14038, 4038, 0.0, 290.816142, 0.01186634, 290.816142, 0.03559903, 203.5712994, -4572.91583937, 0.05, 2, 0, 74016, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34038, 72.7040355, 6.013e-05, 218.1121065, 0.00018038, 727.04035499, 0.00060126, -72.7040355, -6.013e-05, -218.1121065, -0.00018038, -727.04035499, -0.00060126, 0.4, 0.3, 0.003, 0.0, 0.0, 14038, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4038, 99999, 'P', 44038, 'Vy', 34038, 'Vz', 24038, 'My', 14038, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174016, 74016, 174016, 4038, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4038, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 5.8, 0.0, 6.4)
    ops.node(124017, 5.8, 0.0, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4040, 172002, 124017, 0.1225, 30534227.3739001, 12722594.73912504, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24040, 119.83035304, 0.00062996, 143.87705159, 0.00949559, 14.38770516, 0.04109157, -119.83035304, -0.00062996, -143.87705159, -0.00949559, -14.38770516, -0.04109157, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14040, 114.53229007, 0.00062996, 137.51581121, 0.00949559, 13.75158112, 0.04109157, -114.53229007, -0.00062996, -137.51581121, -0.00949559, -13.75158112, -0.04109157, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24040, 4040, 0.0, 211.62650315, 0.0125992, 211.62650315, 0.03779761, 148.1385522, -3190.18366709, 0.05, 2, 0, 72002, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44040, 52.90662579, 5.194e-05, 158.71987736, 0.00015582, 529.06625787, 0.00051939, -52.90662579, -5.194e-05, -158.71987736, -0.00015582, -529.06625787, -0.00051939, 0.4, 0.3, 0.003, 0.0, 0.0, 24040, 2)
    ops.limitCurve('ThreePoint', 14040, 4040, 0.0, 211.62650315, 0.0125992, 211.62650315, 0.03779761, 148.1385522, -3190.18366709, 0.05, 2, 0, 72002, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34040, 52.90662579, 5.194e-05, 158.71987736, 0.00015582, 529.06625787, 0.00051939, -52.90662579, -5.194e-05, -158.71987736, -0.00015582, -529.06625787, -0.00051939, 0.4, 0.3, 0.003, 0.0, 0.0, 14040, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4040, 99999, 'P', 44040, 'Vy', 34040, 'Vz', 24040, 'My', 14040, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4040, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4040, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 5.8, 0.0, 7.55)
    ops.node(123002, 5.8, 0.0, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 174017, 123002, 0.1225, 27787165.49197738, 11577985.62165724, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 114.43009213, 0.00061089, 138.08320512, 0.01107448, 13.80832051, 0.0403366, -114.43009213, -0.00061089, -138.08320512, -0.01107448, -13.80832051, -0.0403366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 108.64271106, 0.00061089, 131.0995515, 0.01107448, 13.10995515, 0.0403366, -108.64271106, -0.00061089, -131.0995515, -0.01107448, -13.10995515, -0.0403366, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 195.38911154, 0.01221779, 195.38911154, 0.03665336, 136.77237808, -3535.04913684, 0.05, 2, 0, 74017, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 48.84727788, 5.269e-05, 146.54183365, 0.00015808, 488.47277885, 0.00052694, -48.84727788, -5.269e-05, -146.54183365, -0.00015808, -488.47277885, -0.00052694, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 195.38911154, 0.01221779, 195.38911154, 0.03665336, 136.77237808, -3535.04913684, 0.05, 2, 0, 74017, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 48.84727788, 5.269e-05, 146.54183365, 0.00015808, 488.47277885, 0.00052694, -48.84727788, -5.269e-05, -146.54183365, -0.00015808, -488.47277885, -0.00052694, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.65, 0.0, 6.4)
    ops.node(124018, 8.65, 0.0, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 172003, 124018, 0.1225, 25392268.25933572, 10580111.77472322, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 122.95830242, 0.00063306, 148.01871796, 0.01010066, 14.8018718, 0.0333409, -122.95830242, -0.00063306, -148.01871796, -0.01010066, -14.8018718, -0.0333409, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 116.65369236, 0.00063306, 140.42915076, 0.01010066, 14.04291508, 0.0333409, -116.65369236, -0.00063306, -140.42915076, -0.01010066, -14.04291508, -0.0333409, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 183.38052166, 0.01266115, 183.38052166, 0.03798344, 128.36636516, -3516.34025235, 0.05, 2, 0, 72003, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 45.84513041, 5.412e-05, 137.53539124, 0.00016236, 458.45130414, 0.0005412, -45.84513041, -5.412e-05, -137.53539124, -0.00016236, -458.45130414, -0.0005412, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 183.38052166, 0.01266115, 183.38052166, 0.03798344, 128.36636516, -3516.34025235, 0.05, 2, 0, 72003, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 45.84513041, 5.412e-05, 137.53539124, 0.00016236, 458.45130414, 0.0005412, -45.84513041, -5.412e-05, -137.53539124, -0.00016236, -458.45130414, -0.0005412, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 8.65, 0.0, 7.55)
    ops.node(123003, 8.65, 0.0, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 174018, 123003, 0.1225, 27042734.91592156, 11267806.21496732, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 110.76407259, 0.00062571, 133.71075444, 0.01145014, 13.37107544, 0.03952153, -110.76407259, -0.00062571, -133.71075444, -0.01145014, -13.37107544, -0.03952153, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 105.67300461, 0.00062571, 127.56498421, 0.01145014, 12.75649842, 0.03952153, -105.67300461, -0.00062571, -127.56498421, -0.01145014, -12.75649842, -0.03952153, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 191.11907585, 0.01251412, 191.11907585, 0.03754236, 133.7833531, -3568.29406164, 0.05, 2, 0, 74018, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 47.77976896, 5.296e-05, 143.33930689, 0.00015888, 477.79768963, 0.00052961, -47.77976896, -5.296e-05, -143.33930689, -0.00015888, -477.79768963, -0.00052961, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 191.11907585, 0.01251412, 191.11907585, 0.03754236, 133.7833531, -3568.29406164, 0.05, 2, 0, 74018, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 47.77976896, 5.296e-05, 143.33930689, 0.00015888, 477.79768963, 0.00052961, -47.77976896, -5.296e-05, -143.33930689, -0.00015888, -477.79768963, -0.00052961, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 5.8, 0.0, 8.95)
    ops.node(124019, 5.8, 0.0, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4045, 173002, 124019, 0.1225, 29380084.67565384, 12241701.9481891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24045, 90.54603057, 0.00058349, 109.80898677, 0.01193639, 10.98089868, 0.0504158, -90.54603057, -0.00058349, -109.80898677, -0.01193639, -10.98089868, -0.0504158, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14045, 85.0864872, 0.00058349, 103.18796847, 0.01193639, 10.31879685, 0.0504158, -85.0864872, -0.00058349, -103.18796847, -0.01193639, -10.31879685, -0.0504158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24045, 4045, 0.0, 180.37983636, 0.0116698, 180.37983636, 0.0350094, 126.26588545, -3535.24742295, 0.05, 2, 0, 73002, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44045, 45.09495909, 4.601e-05, 135.28487727, 0.00013803, 450.94959089, 0.00046009, -45.09495909, -4.601e-05, -135.28487727, -0.00013803, -450.94959089, -0.00046009, 0.4, 0.3, 0.003, 0.0, 0.0, 24045, 2)
    ops.limitCurve('ThreePoint', 14045, 4045, 0.0, 180.37983636, 0.0116698, 180.37983636, 0.0350094, 126.26588545, -3535.24742295, 0.05, 2, 0, 73002, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34045, 45.09495909, 4.601e-05, 135.28487727, 0.00013803, 450.94959089, 0.00046009, -45.09495909, -4.601e-05, -135.28487727, -0.00013803, -450.94959089, -0.00046009, 0.4, 0.3, 0.003, 0.0, 0.0, 14045, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4045, 99999, 'P', 44045, 'Vy', 34045, 'Vz', 24045, 'My', 14045, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4045, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4045, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 5.8, 0.0, 10.1)
    ops.node(124002, 5.8, 0.0, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 174019, 124002, 0.1225, 27212692.94175111, 11338622.05906296, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 85.64613282, 0.00058627, 104.49306366, 0.01300401, 10.44930637, 0.05198726, -85.64613282, -0.00058627, -104.49306366, -0.01300401, -10.44930637, -0.05198726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 80.10720346, 0.00058627, 97.73526061, 0.01300401, 9.77352606, 0.05198726, -80.10720346, -0.00058627, -97.73526061, -0.01300401, -9.77352606, -0.05198726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 163.45388204, 0.01172535, 163.45388204, 0.03517604, 114.41771743, -4255.42033126, 0.05, 2, 0, 74019, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 40.86347051, 4.501e-05, 122.59041153, 0.00013504, 408.63470511, 0.00045012, -40.86347051, -4.501e-05, -122.59041153, -0.00013504, -408.63470511, -0.00045012, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 163.45388204, 0.01172535, 163.45388204, 0.03517604, 114.41771743, -4255.42033126, 0.05, 2, 0, 74019, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 40.86347051, 4.501e-05, 122.59041153, 0.00013504, 408.63470511, 0.00045012, -40.86347051, -4.501e-05, -122.59041153, -0.00013504, -408.63470511, -0.00045012, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.65, 0.0, 8.95)
    ops.node(124020, 8.65, 0.0, 9.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 173003, 124020, 0.1225, 24593834.09550582, 10247430.87312743, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 94.47057359, 0.0005872, 115.32634015, 0.01206201, 11.53263402, 0.04574289, -94.47057359, -0.0005872, -115.32634015, -0.01206201, -11.53263402, -0.04574289, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 88.11273613, 0.0005872, 107.5649167, 0.01206201, 10.75649167, 0.04574289, -88.11273613, -0.0005872, -107.5649167, -0.01206201, -10.75649167, -0.04574289, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 150.46747145, 0.01174409, 150.46747145, 0.03523228, 105.32723001, -3448.01271615, 0.05, 2, 0, 73003, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 37.61686786, 4.585e-05, 112.85060358, 0.00013754, 376.16867861, 0.00045848, -37.61686786, -4.585e-05, -112.85060358, -0.00013754, -376.16867861, -0.00045848, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 150.46747145, 0.01174409, 150.46747145, 0.03523228, 105.32723001, -3448.01271615, 0.05, 2, 0, 73003, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 37.61686786, 4.585e-05, 112.85060358, 0.00013754, 376.16867861, 0.00045848, -37.61686786, -4.585e-05, -112.85060358, -0.00013754, -376.16867861, -0.00045848, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 8.65, 0.0, 10.1)
    ops.node(124003, 8.65, 0.0, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 174020, 124003, 0.1225, 26493722.11040679, 11039050.87933616, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 83.93393299, 0.0005808, 102.52304887, 0.01284137, 10.25230489, 0.05127663, -83.93393299, -0.0005808, -102.52304887, -0.01284137, -10.25230489, -0.05127663, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 78.50534772, 0.0005808, 95.8921775, 0.01284137, 9.58921775, 0.05127663, -78.50534772, -0.0005808, -95.8921775, -0.01284137, -9.58921775, -0.05127663, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 158.44173953, 0.01161609, 158.44173953, 0.03484827, 110.90921767, -4168.52441189, 0.05, 2, 0, 74020, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 39.61043488, 4.482e-05, 118.83130465, 0.00013445, 396.10434882, 0.00044816, -39.61043488, -4.482e-05, -118.83130465, -0.00013445, -396.10434882, -0.00044816, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 158.44173953, 0.01161609, 158.44173953, 0.03484827, 110.90921767, -4168.52441189, 0.05, 2, 0, 74020, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 39.61043488, 4.482e-05, 118.83130465, 0.00013445, 396.10434882, 0.00044816, -39.61043488, -4.482e-05, -118.83130465, -0.00013445, -396.10434882, -0.00044816, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4048, '-orient', 0, 0, 1, 0, 1, 0)
