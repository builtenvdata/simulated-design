import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 7.9, 0.0, 0.0)
    ops.node(121003, 7.9, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.09, 24520856.79682912, 10217023.66534547, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 91.29370322, 0.00086484, 107.03280049, 0.00789347, 10.70328005, 0.02075531, -91.29370322, -0.00086484, -107.03280049, -0.00789347, -10.70328005, -0.02075531, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 99.42372741, 0.00086484, 116.56444645, 0.00789347, 11.65644465, 0.02075531, -99.42372741, -0.00086484, -116.56444645, -0.00789347, -11.65644465, -0.02075531, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 95.36957967, 0.01729681, 95.36957967, 0.05189043, 66.75870577, -1087.79742968, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 23.84239492, 0.0001089, 71.52718475, 0.0003267, 238.42394918, 0.00108901, -23.84239492, -0.0001089, -71.52718475, -0.0003267, -238.42394918, -0.00108901, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 95.36957967, 0.01729681, 95.36957967, 0.05189043, 66.75870577, -1087.79742968, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 23.84239492, 0.0001089, 71.52718475, 0.0003267, 238.42394918, 0.00108901, -23.84239492, -0.0001089, -71.52718475, -0.0003267, -238.42394918, -0.00108901, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.9, 0.0, 0.0)
    ops.node(121004, 12.9, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.0625, 29540107.76323263, 12308378.23468026, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 44.71071626, 0.00097762, 53.17187817, 0.01285383, 5.31718782, 0.04497097, -44.71071626, -0.00097762, -53.17187817, -0.01285383, -5.31718782, -0.04497097, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 44.71071626, 0.00097762, 53.17187817, 0.01285383, 5.31718782, 0.04497097, -44.71071626, -0.00097762, -53.17187817, -0.01285383, -5.31718782, -0.04497097, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 82.24253651, 0.01955246, 82.24253651, 0.05865737, 57.56977556, -840.08622053, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 20.56063413, 0.00011225, 61.68190239, 0.00033676, 205.60634129, 0.00112255, -20.56063413, -0.00011225, -61.68190239, -0.00033676, -205.60634129, -0.00112255, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 82.24253651, 0.01955246, 82.24253651, 0.05865737, 57.56977556, -840.08622053, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 20.56063413, 0.00011225, 61.68190239, 0.00033676, 205.60634129, 0.00112255, -20.56063413, -0.00011225, -61.68190239, -0.00033676, -205.60634129, -0.00112255, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.05, 0.0)
    ops.node(121005, 0.0, 4.05, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.0625, 28785177.65048363, 11993824.02103484, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 48.11830252, 0.00105974, 57.04302364, 0.00929955, 5.70430236, 0.03675932, -48.11830252, -0.00105974, -57.04302364, -0.00929955, -5.70430236, -0.03675932, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 48.11830252, 0.00105974, 57.04302364, 0.00929955, 5.70430236, 0.03675932, -48.11830252, -0.00105974, -57.04302364, -0.00929955, -5.70430236, -0.03675932, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 64.68802629, 0.02119483, 64.68802629, 0.06358448, 45.2816184, -772.91176661, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 16.17200657, 9.061e-05, 48.51601972, 0.00027183, 161.72006572, 0.0009061, -16.17200657, -9.061e-05, -48.51601972, -0.00027183, -161.72006572, -0.0009061, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 64.68802629, 0.02119483, 64.68802629, 0.06358448, 45.2816184, -772.91176661, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 16.17200657, 9.061e-05, 48.51601972, 0.00027183, 161.72006572, 0.0009061, -16.17200657, -9.061e-05, -48.51601972, -0.00027183, -161.72006572, -0.0009061, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 2.9, 4.05, 0.0)
    ops.node(121006, 2.9, 4.05, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.14, 28686608.45040868, 11952753.52100362, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 184.78813906, 0.00069037, 221.11839484, 0.01428491, 22.11183948, 0.03867984, -184.78813906, -0.00069037, -221.11839484, -0.01428491, -22.11183948, -0.03867984, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 184.22629484, 0.0007591, 220.44608929, 0.01384187, 22.04460893, 0.03611441, -184.22629484, -0.0007591, -220.44608929, -0.01384187, -22.04460893, -0.03611441, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 152.33901541, 0.01380734, 152.33901541, 0.04142201, 106.63731079, -1364.9300553, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 38.08475385, 9.559e-05, 114.25426156, 0.00028676, 380.84753854, 0.00095588, -38.08475385, -9.559e-05, -114.25426156, -0.00028676, -380.84753854, -0.00095588, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 147.599466, 0.01518196, 147.599466, 0.04554589, 103.3196262, -1282.70251401, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 36.8998665, 9.261e-05, 110.6995995, 0.00027784, 368.99866501, 0.00092614, -36.8998665, -9.261e-05, -110.6995995, -0.00027784, -368.99866501, -0.00092614, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 7.9, 4.05, 0.0)
    ops.node(121007, 7.9, 4.05, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.18, 28078584.09733596, 11699410.04055665, 0.00450368, 0.00264, 0.00334125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 243.30913752, 0.00060812, 291.98564394, 0.01520259, 29.19856439, 0.03836151, -243.30913752, -0.00060812, -291.98564394, -0.01520259, -29.19856439, -0.03836151, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 248.31321989, 0.00065481, 297.99084468, 0.01478388, 29.79908447, 0.03622918, -248.31321989, -0.00065481, -297.99084468, -0.01478388, -29.79908447, -0.03622918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 172.65321156, 0.01216236, 172.65321156, 0.03648708, 120.8572481, -1402.98582794, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 43.16330289, 8.609e-05, 129.48990867, 0.00025826, 431.63302891, 0.00086085, -43.16330289, -8.609e-05, -129.48990867, -0.00025826, -431.63302891, -0.00086085, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 168.75324885, 0.01309611, 168.75324885, 0.03928833, 118.1272742, -1337.98361651, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 42.18831221, 8.414e-05, 126.56493664, 0.00025242, 421.88312213, 0.0008414, -42.18831221, -8.414e-05, -126.56493664, -0.00025242, -421.88312213, -0.0008414, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 12.9, 4.05, 0.0)
    ops.node(121008, 12.9, 4.05, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.09, 27119536.29249544, 11299806.78853977, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 95.28183441, 0.00085921, 112.98389888, 0.01160492, 11.29838989, 0.03279893, -95.28183441, -0.00085921, -112.98389888, -0.01160492, -11.29838989, -0.03279893, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 95.28183441, 0.00085921, 112.98389888, 0.01160492, 11.29838989, 0.03279893, -95.28183441, -0.00085921, -112.98389888, -0.01160492, -11.29838989, -0.03279893, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 105.90243551, 0.01718424, 105.90243551, 0.05155273, 74.13170486, -1121.65810639, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 26.47560888, 0.00010934, 79.42682663, 0.00032802, 264.75608877, 0.00109341, -26.47560888, -0.00010934, -79.42682663, -0.00032802, -264.75608877, -0.00109341, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 105.90243551, 0.01718424, 105.90243551, 0.05155273, 74.13170486, -1121.65810639, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 26.47560888, 0.00010934, 79.42682663, 0.00032802, 264.75608877, 0.00109341, -26.47560888, -0.00010934, -79.42682663, -0.00032802, -264.75608877, -0.00109341, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.1, 0.0)
    ops.node(121009, 0.0, 8.1, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.0625, 30019199.04575292, 12507999.60239705, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 45.93273347, 0.00105854, 54.57015575, 0.01196179, 5.45701557, 0.04444511, -45.93273347, -0.00105854, -54.57015575, -0.01196179, -5.45701557, -0.04444511, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 45.93273347, 0.00105854, 54.57015575, 0.01196179, 5.45701557, 0.04444511, -45.93273347, -0.00105854, -54.57015575, -0.01196179, -5.45701557, -0.04444511, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 79.88959529, 0.02117081, 79.88959529, 0.06351243, 55.9227167, -782.72569971, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 19.97239882, 0.0001073, 59.91719647, 0.00032191, 199.72398822, 0.00107303, -19.97239882, -0.0001073, -59.91719647, -0.00032191, -199.72398822, -0.00107303, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 79.88959529, 0.02117081, 79.88959529, 0.06351243, 55.9227167, -782.72569971, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 19.97239882, 0.0001073, 59.91719647, 0.00032191, 199.72398822, 0.00107303, -19.97239882, -0.0001073, -59.91719647, -0.00032191, -199.72398822, -0.00107303, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 2.9, 8.1, 0.0)
    ops.node(121010, 2.9, 8.1, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.105, 27861078.81376244, 11608782.83906768, 0.00152551, 0.00086625, 0.00117906, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 111.77401131, 0.00069261, 133.27297984, 0.01311236, 13.32729798, 0.036097, -111.77401131, -0.00069261, -133.27297984, -0.01311236, -13.32729798, -0.036097, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 109.52012655, 0.00077551, 130.58557573, 0.01263268, 13.05855757, 0.03322396, -109.52012655, -0.00077551, -130.58557573, -0.01263268, -13.05855757, -0.03322396, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 115.57812309, 0.01385221, 115.57812309, 0.04155662, 80.90468616, -1106.64324056, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 28.89453077, 9.956e-05, 86.68359232, 0.00029868, 288.94530773, 0.00099561, -28.89453077, -9.956e-05, -86.68359232, -0.00029868, -288.94530773, -0.00099561, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 111.51076684, 0.01551017, 111.51076684, 0.04653052, 78.05753679, -1038.40434155, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 27.87769171, 9.606e-05, 83.63307513, 0.00028817, 278.7769171, 0.00096057, -27.87769171, -9.606e-05, -83.63307513, -0.00028817, -278.7769171, -0.00096057, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.9, 8.1, 0.0)
    ops.node(121011, 7.9, 8.1, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.18, 27618803.2028485, 11507834.66785354, 0.00450368, 0.00264, 0.00334125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 240.47776077, 0.00059968, 288.59804738, 0.0149974, 28.85980474, 0.03740695, -240.47776077, -0.00059968, -288.59804738, -0.0149974, -28.85980474, -0.03740695, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 245.93486743, 0.00064488, 295.14713667, 0.01458348, 29.51471367, 0.03533486, -245.93486743, -0.00064488, -295.14713667, -0.01458348, -29.51471367, -0.03533486, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 170.37392709, 0.01199356, 170.37392709, 0.03598067, 119.26174896, -1408.27296722, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 42.59348177, 8.636e-05, 127.78044532, 0.00025909, 425.93481772, 0.00086363, -42.59348177, -8.636e-05, -127.78044532, -0.00025909, -425.93481772, -0.00086363, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 166.43916416, 0.01289757, 166.43916416, 0.03869272, 116.50741491, -1342.57274607, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 41.60979104, 8.437e-05, 124.82937312, 0.0002531, 416.09791041, 0.00084368, -41.60979104, -8.437e-05, -124.82937312, -0.0002531, -416.09791041, -0.00084368, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 12.9, 8.1, 0.0)
    ops.node(121012, 12.9, 8.1, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.09, 30032422.4676846, 12513509.36153525, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 94.08439568, 0.00082974, 111.79518193, 0.0118156, 11.17951819, 0.04015179, -94.08439568, -0.00082974, -111.79518193, -0.0118156, -11.17951819, -0.04015179, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 94.08439568, 0.00082974, 111.79518193, 0.0118156, 11.17951819, 0.04015179, -94.08439568, -0.00082974, -111.79518193, -0.0118156, -11.17951819, -0.04015179, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 111.04955974, 0.01659489, 111.04955974, 0.04978468, 77.73469182, -1058.0148678, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 27.76238993, 0.00010353, 83.2871698, 0.0003106, 277.62389935, 0.00103534, -27.76238993, -0.00010353, -83.2871698, -0.0003106, -277.62389935, -0.00103534, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 111.04955974, 0.01659489, 111.04955974, 0.04978468, 77.73469182, -1058.0148678, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 27.76238993, 0.00010353, 83.2871698, 0.0003106, 277.62389935, 0.00103534, -27.76238993, -0.00010353, -83.2871698, -0.0003106, -277.62389935, -0.00103534, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 12.15, 0.0)
    ops.node(121013, 0.0, 12.15, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0625, 29402989.7337582, 12251245.72239925, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 51.22940276, 0.00092511, 60.86519622, 0.01184289, 6.08651962, 0.04268755, -51.22940276, -0.00092511, -60.86519622, -0.01184289, -6.08651962, -0.04268755, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 48.24253805, 0.00092511, 57.31652892, 0.01184289, 5.73165289, 0.04268755, -48.24253805, -0.00092511, -57.31652892, -0.01184289, -5.73165289, -0.04268755, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 77.70271004, 0.0185023, 77.70271004, 0.0555069, 54.39189703, -802.05073814, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 19.42567751, 0.00010655, 58.27703253, 0.00031966, 194.25677509, 0.00106553, -19.42567751, -0.00010655, -58.27703253, -0.00031966, -194.25677509, -0.00106553, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 77.70271004, 0.0185023, 77.70271004, 0.0555069, 54.39189703, -802.05073814, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 19.42567751, 0.00010655, 58.27703253, 0.00031966, 194.25677509, 0.00106553, -19.42567751, -0.00010655, -58.27703253, -0.00031966, -194.25677509, -0.00106553, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 2.9, 12.15, 0.0)
    ops.node(121014, 2.9, 12.15, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.105, 26444976.34040719, 11018740.14183633, 0.00152551, 0.00086625, 0.00117906, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 124.36146124, 0.00082569, 148.02599436, 0.01170548, 14.80259944, 0.03148824, -124.36146124, -0.00082569, -148.02599436, -0.01170548, -14.80259944, -0.03148824, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 114.64921513, 0.0009477, 136.46562128, 0.01133466, 13.64656213, 0.02905747, -114.64921513, -0.0009477, -136.46562128, -0.01133466, -13.64656213, -0.02905747, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 109.28846604, 0.0165139, 109.28846604, 0.04954169, 76.50192622, -1081.76317249, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 27.32211651, 9.918e-05, 81.96634953, 0.00029755, 273.22116509, 0.00099184, -27.32211651, -9.918e-05, -81.96634953, -0.00029755, -273.22116509, -0.00099184, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 105.43082998, 0.01895393, 105.43082998, 0.05686179, 73.80158099, -1017.73301362, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 26.3577075, 9.568e-05, 79.07312249, 0.00028705, 263.57707496, 0.00095683, -26.3577075, -9.568e-05, -79.07312249, -0.00028705, -263.57707496, -0.00095683, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.9, 12.15, 0.0)
    ops.node(121015, 7.9, 12.15, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.18, 29299777.32280904, 12208240.55117043, 0.00450368, 0.00264, 0.00334125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 278.96262204, 0.00062034, 334.55024235, 0.01617889, 33.45502424, 0.04118939, -278.96262204, -0.00062034, -334.55024235, -0.01617889, -33.45502424, -0.04118939, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 274.62010525, 0.00066667, 329.34241188, 0.01572908, 32.93424119, 0.03888896, -274.62010525, -0.00066667, -329.34241188, -0.01572908, -32.93424119, -0.03888896, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 180.82544583, 0.01240671, 180.82544583, 0.03722012, 126.57781208, -1423.21641091, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 45.20636146, 8.64e-05, 135.61908437, 0.00025921, 452.06361456, 0.00086402, -45.20636146, -8.64e-05, -135.61908437, -0.00025921, -452.06361456, -0.00086402, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 176.79267612, 0.01333334, 176.79267612, 0.04000002, 123.75487329, -1355.53919162, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 44.19816903, 8.447e-05, 132.59450709, 0.00025342, 441.98169031, 0.00084475, -44.19816903, -8.447e-05, -132.59450709, -0.00025342, -441.98169031, -0.00084475, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.9, 12.15, 0.0)
    ops.node(121016, 12.9, 12.15, 3.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.09, 26940871.1526863, 11225362.98028596, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 101.09864409, 0.00088669, 119.84062888, 0.01024936, 11.98406289, 0.03097302, -101.09864409, -0.00088669, -119.84062888, -0.01024936, -11.98406289, -0.03097302, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 97.28744031, 0.00088669, 115.32289215, 0.01024936, 11.53228922, 0.03097302, -97.28744031, -0.00088669, -115.32289215, -0.01024936, -11.53228922, -0.03097302, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 100.74726726, 0.01773378, 100.74726726, 0.05320135, 70.52308708, -1043.76799494, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 25.18681681, 0.00010471, 75.56045044, 0.00031412, 251.86816814, 0.00104708, -25.18681681, -0.00010471, -75.56045044, -0.00031412, -251.86816814, -0.00104708, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 100.74726726, 0.01773378, 100.74726726, 0.05320135, 70.52308708, -1043.76799494, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 25.18681681, 0.00010471, 75.56045044, 0.00031412, 251.86816814, 0.00104708, -25.18681681, -0.00010471, -75.56045044, -0.00031412, -251.86816814, -0.00104708, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 16.2, 0.0)
    ops.node(121017, 0.0, 16.2, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.075, 31363558.90270912, 13068149.54279547, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 52.10143522, 0.00079747, 62.4274207, 0.01290749, 6.24274207, 0.06031366, -52.10143522, -0.00079747, -62.4274207, -0.01290749, -6.24274207, -0.06031366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 47.55815856, 0.00093712, 56.98371186, 0.01233995, 5.69837119, 0.05344041, -47.55815856, -0.00093712, -56.98371186, -0.01233995, -5.69837119, -0.05344041, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 86.25094693, 0.01594938, 86.25094693, 0.04784813, 60.37566285, -706.90913764, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 21.56273673, 9.24e-05, 64.6882102, 0.0002772, 215.62736733, 0.00092401, -21.56273673, -9.24e-05, -64.6882102, -0.0002772, -215.62736733, -0.00092401, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 76.54874716, 0.01874242, 76.54874716, 0.05622725, 53.58412301, -630.12312911, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 19.13718679, 8.201e-05, 57.41156037, 0.00024602, 191.37186791, 0.00082007, -19.13718679, -8.201e-05, -57.41156037, -0.00024602, -191.37186791, -0.00082007, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 2.9, 16.2, 0.0)
    ops.node(121018, 2.9, 16.2, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.075, 32115649.147615, 13381520.47817292, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 81.20642701, 0.00081702, 96.28315689, 0.01208249, 9.62831569, 0.04944681, -81.20642701, -0.00081702, -96.28315689, -0.01208249, -9.62831569, -0.04944681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 72.58953007, 0.00095509, 86.06645273, 0.01156269, 8.60664527, 0.04395701, -72.58953007, -0.00095509, -86.06645273, -0.01156269, -8.60664527, -0.04395701, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 100.15710238, 0.01634041, 100.15710238, 0.04902122, 70.10997167, -919.30399402, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 25.0392756, 0.00010479, 75.11782679, 0.00031436, 250.39275595, 0.00104786, -25.0392756, -0.00010479, -75.11782679, -0.00031436, -250.39275595, -0.00104786, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 90.16626608, 0.01910179, 90.16626608, 0.05730538, 63.11638626, -855.57266484, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 22.54156652, 9.433e-05, 67.62469956, 0.000283, 225.41566521, 0.00094334, -22.54156652, -9.433e-05, -67.62469956, -0.000283, -225.41566521, -0.00094334, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 7.9, 16.2, 0.0)
    ops.node(121019, 7.9, 16.2, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.09, 29172192.74851615, 12155080.31188173, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 104.98682098, 0.00085182, 124.5228004, 0.01344604, 12.45228004, 0.03838848, -104.98682098, -0.00085182, -124.5228004, -0.01344604, -12.45228004, -0.03838848, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 104.98682098, 0.00085182, 124.5228004, 0.01344604, 12.45228004, 0.03838848, -104.98682098, -0.00085182, -124.5228004, -0.01344604, -12.45228004, -0.03838848, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 116.2199465, 0.01703648, 116.2199465, 0.05110944, 81.35396255, -1200.41814854, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 29.05498663, 0.00011155, 87.16495988, 0.00033465, 290.54986626, 0.0011155, -29.05498663, -0.00011155, -87.16495988, -0.00033465, -290.54986626, -0.0011155, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 116.2199465, 0.01703648, 116.2199465, 0.05110944, 81.35396255, -1200.41814854, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 29.05498663, 0.00011155, 87.16495988, 0.00033465, 290.54986626, 0.0011155, -29.05498663, -0.00011155, -87.16495988, -0.00033465, -290.54986626, -0.0011155, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 12.9, 16.2, 0.0)
    ops.node(121020, 12.9, 16.2, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.075, 32023751.7498505, 13343229.89577104, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 63.00463781, 0.00081744, 75.00934359, 0.01454081, 7.50093436, 0.0563728, -63.00463781, -0.00081744, -75.00934359, -0.01454081, -7.50093436, -0.0563728, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 57.04685742, 0.00096006, 67.91638643, 0.01388202, 6.79163864, 0.05014974, -57.04685742, -0.00096006, -67.91638643, -0.01388202, -6.79163864, -0.05014974, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 98.99499297, 0.01634885, 98.99499297, 0.04904654, 69.29649508, -895.36127414, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 24.74874824, 0.00010387, 74.24624473, 0.0003116, 247.48748242, 0.00103868, -24.74874824, -0.00010387, -74.24624473, -0.0003116, -247.48748242, -0.00103868, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 94.41344675, 0.01920118, 94.41344675, 0.05760355, 66.08941273, -811.98924797, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 23.60336169, 9.906e-05, 70.81008506, 0.00029718, 236.03361688, 0.00099061, -23.60336169, -9.906e-05, -70.81008506, -0.00029718, -236.03361688, -0.00099061, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.9, 0.0, 3.75)
    ops.node(122003, 7.9, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.09, 25734814.47518941, 10722839.36466226, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 67.58170663, 0.00072691, 80.56823039, 0.00967498, 8.05682304, 0.03238977, -67.58170663, -0.00072691, -80.56823039, -0.00967498, -8.05682304, -0.03238977, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 64.11687181, 0.00072691, 76.43759172, 0.00967498, 7.64375917, 0.03238977, -64.11687181, -0.00072691, -76.43759172, -0.00967498, -7.64375917, -0.03238977, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 89.36458182, 0.01453815, 89.36458182, 0.04361444, 62.55520728, -1060.34422767, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 22.34114546, 8.056e-05, 67.02343637, 0.00024169, 223.41145456, 0.00080562, -22.34114546, -8.056e-05, -67.02343637, -0.00024169, -223.41145456, -0.00080562, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 89.36458182, 0.01453815, 89.36458182, 0.04361444, 62.55520728, -1060.34422767, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 22.34114546, 8.056e-05, 67.02343637, 0.00024169, 223.41145456, 0.00080562, -22.34114546, -8.056e-05, -67.02343637, -0.00024169, -223.41145456, -0.00080562, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.9, 0.0, 3.75)
    ops.node(122004, 12.9, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.0625, 29244738.61612004, 12185307.75671668, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 37.61454675, 0.00084356, 45.04491983, 0.01390993, 4.50449198, 0.05245837, -37.61454675, -0.00084356, -45.04491983, -0.01390993, -4.50449198, -0.05245837, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 37.61454675, 0.00084356, 45.04491983, 0.01390993, 4.50449198, 0.05245837, -37.61454675, -0.00084356, -45.04491983, -0.01390993, -4.50449198, -0.05245837, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 75.94536329, 0.01687116, 75.94536329, 0.05061348, 53.1617543, -890.6855889, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 18.98634082, 8.676e-05, 56.95902247, 0.00026027, 189.86340823, 0.00086757, -18.98634082, -8.676e-05, -56.95902247, -0.00026027, -189.86340823, -0.00086757, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 75.94536329, 0.01687116, 75.94536329, 0.05061348, 53.1617543, -890.6855889, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 18.98634082, 8.676e-05, 56.95902247, 0.00026027, 189.86340823, 0.00086757, -18.98634082, -8.676e-05, -56.95902247, -0.00026027, -189.86340823, -0.00086757, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.05, 3.775)
    ops.node(122005, 0.0, 4.05, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.0625, 25494175.00065444, 10622572.91693935, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 39.20873506, 0.00084139, 46.69627069, 0.012287, 4.66962707, 0.0373465, -39.20873506, -0.00084139, -46.69627069, -0.012287, -4.66962707, -0.0373465, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 39.20873506, 0.00084139, 46.69627069, 0.012287, 4.66962707, 0.0373465, -39.20873506, -0.00084139, -46.69627069, -0.012287, -4.66962707, -0.0373465, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 73.60127596, 0.01682778, 73.60127596, 0.05048333, 51.52089317, -1005.73251449, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 18.40031899, 9.645e-05, 55.20095697, 0.00028935, 184.0031899, 0.00096448, -18.40031899, -9.645e-05, -55.20095697, -0.00028935, -184.0031899, -0.00096448, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 73.60127596, 0.01682778, 73.60127596, 0.05048333, 51.52089317, -1005.73251449, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 18.40031899, 9.645e-05, 55.20095697, 0.00028935, 184.0031899, 0.00096448, -18.40031899, -9.645e-05, -55.20095697, -0.00028935, -184.0031899, -0.00096448, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 2.9, 4.05, 3.775)
    ops.node(122006, 2.9, 4.05, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.14, 28737763.31358175, 11974068.04732573, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 121.11405062, 0.00059416, 145.68466471, 0.01244264, 14.56846647, 0.04106358, -121.11405062, -0.00059416, -145.68466471, -0.01244264, -14.56846647, -0.04106358, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 98.91385385, 0.00064814, 118.98067614, 0.01205059, 11.89806761, 0.03818146, -98.91385385, -0.00064814, -118.98067614, -0.01205059, -11.89806761, -0.03818146, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 134.09853481, 0.01188311, 134.09853481, 0.03564934, 93.86897437, -1246.7852912, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 33.5246337, 6.959e-05, 100.57390111, 0.00020878, 335.24633703, 0.00069594, -33.5246337, -6.959e-05, -100.57390111, -0.00020878, -335.24633703, -0.00069594, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 130.46253769, 0.01296279, 130.46253769, 0.03888837, 91.32377639, -1170.17112482, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 32.61563442, 6.771e-05, 97.84690327, 0.00020312, 326.15634423, 0.00067707, -32.61563442, -6.771e-05, -97.84690327, -0.00020312, -326.15634423, -0.00067707, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 7.9, 4.05, 3.775)
    ops.node(122007, 7.9, 4.05, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.18, 25981231.94203364, 10825513.30918068, 0.00450368, 0.00264, 0.00334125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 158.36470819, 0.00055863, 191.07057414, 0.0101317, 19.10705741, 0.029741, -158.36470819, -0.00055863, -191.07057414, -0.0101317, -19.10705741, -0.029741, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 139.60853003, 0.00059407, 168.4408243, 0.00989411, 16.84408243, 0.02820263, -139.60853003, -0.00059407, -168.4408243, -0.00989411, -16.84408243, -0.02820263, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 140.55539943, 0.0111725, 140.55539943, 0.03351751, 98.3887796, -1248.38367708, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 35.13884986, 6.275e-05, 105.41654958, 0.00018826, 351.38849859, 0.00062755, -35.13884986, -6.275e-05, -105.41654958, -0.00018826, -351.38849859, -0.00062755, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 137.75606021, 0.01188148, 137.75606021, 0.03564443, 96.42924214, -1192.58010388, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 34.43901505, 6.15e-05, 103.31704516, 0.00018451, 344.39015052, 0.00061505, -34.43901505, -6.15e-05, -103.31704516, -0.00018451, -344.39015052, -0.00061505, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 12.9, 4.05, 3.775)
    ops.node(122008, 12.9, 4.05, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.09, 26361995.65576933, 10984164.85657055, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 64.59007689, 0.00073313, 77.21483739, 0.01019618, 7.72148374, 0.03585856, -64.59007689, -0.00073313, -77.21483739, -0.01019618, -7.72148374, -0.03585856, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 61.48270378, 0.00073313, 73.50009789, 0.01019618, 7.35000979, 0.03585856, -61.48270378, -0.00073313, -73.50009789, -0.01019618, -7.35000979, -0.03585856, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 88.97475307, 0.01466269, 88.97475307, 0.04398807, 62.28232715, -1009.96190423, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 22.24368827, 7.83e-05, 66.7310648, 0.00023491, 222.43688268, 0.00078303, -22.24368827, -7.83e-05, -66.7310648, -0.00023491, -222.43688268, -0.00078303, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 88.97475307, 0.01466269, 88.97475307, 0.04398807, 62.28232715, -1009.96190423, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 22.24368827, 7.83e-05, 66.7310648, 0.00023491, 222.43688268, 0.00078303, -22.24368827, -7.83e-05, -66.7310648, -0.00023491, -222.43688268, -0.00078303, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.1, 3.775)
    ops.node(122009, 0.0, 8.1, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.0625, 29861200.40900388, 12442166.83708495, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 36.68889559, 0.00079868, 43.87921416, 0.01475162, 4.38792142, 0.05382208, -36.68889559, -0.00079868, -43.87921416, -0.01475162, -4.38792142, -0.05382208, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 36.68889559, 0.00079868, 43.87921416, 0.01475162, 4.38792142, 0.05382208, -36.68889559, -0.00079868, -43.87921416, -0.01475162, -4.38792142, -0.05382208, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 78.68215687, 0.0159736, 78.68215687, 0.0479208, 55.07750981, -922.57420305, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 19.67053922, 8.803e-05, 59.01161765, 0.00026408, 196.70539218, 0.00088028, -19.67053922, -8.803e-05, -59.01161765, -0.00026408, -196.70539218, -0.00088028, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 78.68215687, 0.0159736, 78.68215687, 0.0479208, 55.07750981, -922.57420305, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 19.67053922, 8.803e-05, 59.01161765, 0.00026408, 196.70539218, 0.00088028, -19.67053922, -8.803e-05, -59.01161765, -0.00026408, -196.70539218, -0.00088028, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 2.9, 8.1, 3.775)
    ops.node(122010, 2.9, 8.1, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.105, 27298509.3396631, 11374378.89152629, 0.00152551, 0.00086625, 0.00117906, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 90.37776917, 0.00064869, 108.46751481, 0.01267021, 10.84675148, 0.03948435, -90.37776917, -0.00064869, -108.46751481, -0.01267021, -10.84675148, -0.03948435, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 80.17796589, 0.00072058, 96.22614922, 0.01219756, 9.62261492, 0.03621957, -80.17796589, -0.00072058, -96.22614922, -0.01219756, -9.62261492, -0.03621957, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 104.45040979, 0.01297381, 104.45040979, 0.03892143, 73.11528685, -1119.97489138, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 26.11260245, 7.609e-05, 78.33780734, 0.00022826, 261.12602446, 0.00076087, -26.11260245, -7.609e-05, -78.33780734, -0.00022826, -261.12602446, -0.00076087, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 100.61079534, 0.01441155, 100.61079534, 0.04323464, 70.42755674, -1038.12319406, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 25.15269883, 7.329e-05, 75.4580965, 0.00021987, 251.52698835, 0.0007329, -25.15269883, -7.329e-05, -75.4580965, -0.00021987, -251.52698835, -0.0007329, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.9, 8.1, 3.775)
    ops.node(122011, 7.9, 8.1, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.18, 26118709.45970115, 10882795.60820881, 0.00450368, 0.00264, 0.00334125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 154.34950292, 0.00054123, 186.23351581, 0.01065673, 18.62335158, 0.03046048, -154.34950292, -0.00054123, -186.23351581, -0.01065673, -18.62335158, -0.03046048, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 136.11507654, 0.00057447, 164.23239971, 0.01040147, 16.42323997, 0.02889153, -136.11507654, -0.00057447, -164.23239971, -0.01040147, -16.42323997, -0.02889153, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 143.82166951, 0.01082464, 143.82166951, 0.03247391, 100.67516866, -1300.14350807, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 35.95541738, 6.387e-05, 107.86625213, 0.00019162, 359.55417378, 0.00063875, -35.95541738, -6.387e-05, -107.86625213, -0.00019162, -359.55417378, -0.00063875, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 140.73998931, 0.01148939, 140.73998931, 0.03446818, 98.51799252, -1237.5074213, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 35.18499733, 6.251e-05, 105.55499198, 0.00018752, 351.84997327, 0.00062506, -35.18499733, -6.251e-05, -105.55499198, -0.00018752, -351.84997327, -0.00062506, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 12.9, 8.1, 3.775)
    ops.node(122012, 12.9, 8.1, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.09, 27251588.00656459, 11354828.33606858, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 63.93969035, 0.00073459, 76.50240746, 0.01190634, 7.65024075, 0.03985851, -63.93969035, -0.00073459, -76.50240746, -0.01190634, -7.65024075, -0.03985851, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 61.08928406, 0.00073459, 73.09196018, 0.01190634, 7.30919602, 0.03985851, -61.08928406, -0.00073459, -73.09196018, -0.01190634, -7.30919602, -0.03985851, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 95.98788832, 0.01469188, 95.98788832, 0.04407565, 67.19152182, -1105.8567322, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 23.99697208, 8.172e-05, 71.99091624, 0.00024515, 239.9697208, 0.00081717, -23.99697208, -8.172e-05, -71.99091624, -0.00024515, -239.9697208, -0.00081717, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 95.98788832, 0.01469188, 95.98788832, 0.04407565, 67.19152182, -1105.8567322, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 23.99697208, 8.172e-05, 71.99091624, 0.00024515, 239.9697208, 0.00081717, -23.99697208, -8.172e-05, -71.99091624, -0.00024515, -239.9697208, -0.00081717, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 12.15, 3.775)
    ops.node(122013, 0.0, 12.15, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0625, 28213344.97119724, 11755560.40466552, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 36.87927881, 0.00089841, 44.13949833, 0.01424713, 4.41394983, 0.04917191, -36.87927881, -0.00089841, -44.13949833, -0.01424713, -4.41394983, -0.04917191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 36.87927881, 0.00089841, 44.13949833, 0.01424713, 4.41394983, 0.04917191, -36.87927881, -0.00089841, -44.13949833, -0.01424713, -4.41394983, -0.04917191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 77.36744787, 0.01796815, 77.36744787, 0.05390445, 54.15721351, -971.76106634, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 19.34186197, 9.161e-05, 58.0255859, 0.00027484, 193.41861968, 0.00091612, -19.34186197, -9.161e-05, -58.0255859, -0.00027484, -193.41861968, -0.00091612, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 77.36744787, 0.01796815, 77.36744787, 0.05390445, 54.15721351, -971.76106634, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 19.34186197, 9.161e-05, 58.0255859, 0.00027484, 193.41861968, 0.00091612, -19.34186197, -9.161e-05, -58.0255859, -0.00027484, -193.41861968, -0.00091612, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 2.9, 12.15, 3.775)
    ops.node(122014, 2.9, 12.15, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.105, 28998415.78698892, 12082673.24457872, 0.00152551, 0.00086625, 0.00117906, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 90.62285005, 0.00071868, 108.71501002, 0.01154344, 10.871501, 0.04165444, -90.62285005, -0.00071868, -108.71501002, -0.01154344, -10.871501, -0.04165444, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 79.35836846, 0.00081595, 95.20166071, 0.01115039, 9.52016607, 0.03812597, -79.35836846, -0.00081595, -95.20166071, -0.01115039, -9.52016607, -0.03812597, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 107.49828387, 0.01437354, 107.49828387, 0.04312062, 75.24879871, -1064.92023224, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 26.87457097, 7.372e-05, 80.62371291, 0.00022115, 268.74570968, 0.00073717, -26.87457097, -7.372e-05, -80.62371291, -0.00022115, -268.74570968, -0.00073717, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 100.09520394, 0.01631908, 100.09520394, 0.04895724, 70.06664276, -992.62778739, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 25.02380098, 6.864e-05, 75.07140295, 0.00020592, 250.23800985, 0.0006864, -25.02380098, -6.864e-05, -75.07140295, -0.00020592, -250.23800985, -0.0006864, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.9, 12.15, 3.775)
    ops.node(122015, 7.9, 12.15, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.18, 27094457.19584191, 11289357.16493413, 0.00450368, 0.00264, 0.00334125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 153.75677809, 0.0005243, 185.51338776, 0.01200033, 18.55133878, 0.03311257, -153.75677809, -0.0005243, -185.51338776, -0.01200033, -18.55133878, -0.03311257, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 135.72962127, 0.00055453, 163.76293893, 0.01170325, 16.37629389, 0.031415, -135.72962127, -0.00055453, -163.76293893, -0.01170325, -16.37629389, -0.031415, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 152.1681866, 0.01048608, 152.1681866, 0.03145823, 106.51773062, -1365.70797701, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 38.04204665, 6.515e-05, 114.12613995, 0.00019544, 380.42046649, 0.00065148, -38.04204665, -6.515e-05, -114.12613995, -0.00019544, -380.42046649, -0.00065148, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 148.73681357, 0.01109066, 148.73681357, 0.03327198, 104.1157695, -1294.30361264, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 37.18420339, 6.368e-05, 111.55261018, 0.00019104, 371.84203392, 0.00063679, -37.18420339, -6.368e-05, -111.55261018, -0.00019104, -371.84203392, -0.00063679, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.9, 12.15, 3.775)
    ops.node(122016, 12.9, 12.15, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.09, 30170822.10710206, 12571175.87795919, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 67.71062324, 0.00071561, 80.95564828, 0.01232323, 8.09556483, 0.04681343, -67.71062324, -0.00071561, -80.95564828, -0.01232323, -8.09556483, -0.04681343, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 64.18260356, 0.00071561, 76.73750484, 0.01232323, 7.67375048, 0.04681343, -64.18260356, -0.00071561, -76.73750484, -0.01232323, -7.67375048, -0.04681343, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 101.48119337, 0.01431217, 101.48119337, 0.0429365, 71.03683536, -1041.38321472, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 25.37029834, 7.803e-05, 76.11089503, 0.0002341, 253.70298343, 0.00078034, -25.37029834, -7.803e-05, -76.11089503, -0.0002341, -253.70298343, -0.00078034, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 101.48119337, 0.01431217, 101.48119337, 0.0429365, 71.03683536, -1041.38321472, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 25.37029834, 7.803e-05, 76.11089503, 0.0002341, 253.70298343, 0.00078034, -25.37029834, -7.803e-05, -76.11089503, -0.0002341, -253.70298343, -0.00078034, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 16.2, 3.75)
    ops.node(122017, 0.0, 16.2, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.075, 29098761.50959595, 12124483.96233165, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 41.48101276, 0.00065771, 50.08488755, 0.01195655, 5.00848875, 0.06061188, -41.48101276, -0.00065771, -50.08488755, -0.01195655, -5.00848875, -0.06061188, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 36.80790511, 0.00075029, 44.44249707, 0.01138931, 4.44424971, 0.05357278, -36.80790511, -0.00075029, -44.44249707, -0.01138931, -4.44424971, -0.05357278, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 74.83351351, 0.01315417, 74.83351351, 0.03946251, 52.38345946, -769.10229249, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 18.70837838, 7.16e-05, 56.12513513, 0.00021479, 187.08378378, 0.00071596, -18.70837838, -7.16e-05, -56.12513513, -0.00021479, -187.08378378, -0.00071596, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 59.43728404, 0.01500585, 59.43728404, 0.04501756, 41.60609883, -668.58526546, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 14.85932101, 5.687e-05, 44.57796303, 0.0001706, 148.59321011, 0.00056866, -14.85932101, -5.687e-05, -44.57796303, -0.0001706, -148.59321011, -0.00056866, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 2.9, 16.2, 3.75)
    ops.node(122018, 2.9, 16.2, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.075, 29244676.79148157, 12185281.99645066, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 53.01575814, 0.00078286, 63.42217964, 0.01426047, 6.34221796, 0.05162652, -53.01575814, -0.00078286, -63.42217964, -0.01426047, -6.34221796, -0.05162652, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 45.34197376, 0.00094535, 54.24211415, 0.0136359, 5.42421142, 0.04603172, -45.34197376, -0.00094535, -54.24211415, -0.0136359, -5.42421142, -0.04603172, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 94.18216687, 0.01565719, 94.18216687, 0.04697157, 65.92751681, -1136.80062513, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 23.54554172, 8.966e-05, 70.63662515, 0.00026898, 235.45541718, 0.00089658, -23.54554172, -8.966e-05, -70.63662515, -0.00026898, -235.45541718, -0.00089658, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 88.93533796, 0.01890692, 88.93533796, 0.05672076, 62.25473658, -1013.83231947, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 22.23383449, 8.466e-05, 66.70150347, 0.00025399, 222.33834491, 0.00084664, -22.23383449, -8.466e-05, -66.70150347, -0.00025399, -222.33834491, -0.00084664, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 7.9, 16.2, 3.75)
    ops.node(122019, 7.9, 16.2, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.09, 28464215.64329259, 11860089.85137191, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 69.34224549, 0.00075224, 82.88470947, 0.01045681, 8.28847095, 0.04014468, -69.34224549, -0.00075224, -82.88470947, -0.01045681, -8.28847095, -0.04014468, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 66.00154387, 0.00075224, 78.8915725, 0.01045681, 7.88915725, 0.04014468, -66.00154387, -0.00075224, -78.8915725, -0.01045681, -7.88915725, -0.04014468, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 96.66572529, 0.01504489, 96.66572529, 0.04513468, 67.66600771, -1049.3697229, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 24.16643132, 7.879e-05, 72.49929397, 0.00023636, 241.66431323, 0.00078788, -24.16643132, -7.879e-05, -72.49929397, -0.00023636, -241.66431323, -0.00078788, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 96.66572529, 0.01504489, 96.66572529, 0.04513468, 67.66600771, -1049.3697229, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 24.16643132, 7.879e-05, 72.49929397, 0.00023636, 241.66431323, 0.00078788, -24.16643132, -7.879e-05, -72.49929397, -0.00023636, -241.66431323, -0.00078788, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 12.9, 16.2, 3.75)
    ops.node(122020, 12.9, 16.2, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.075, 31444868.96803074, 13102028.73667948, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 51.45746055, 0.00069713, 61.60365565, 0.01342231, 6.16036556, 0.06001619, -51.45746055, -0.00069713, -61.60365565, -0.01342231, -6.16036556, -0.06001619, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 40.05049774, 0.00080944, 47.94750937, 0.0127915, 4.79475094, 0.05318772, -40.05049774, -0.00080944, -47.94750937, -0.0127915, -4.79475094, -0.05318772, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 87.35877761, 0.01394256, 87.35877761, 0.04182767, 61.15114433, -868.49822036, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 21.8396944, 7.734e-05, 65.51908321, 0.00023203, 218.39694402, 0.00077344, -21.8396944, -7.734e-05, -65.51908321, -0.00023203, -218.39694402, -0.00077344, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 82.03362714, 0.01618881, 82.03362714, 0.04856644, 57.423539, -777.80571529, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 20.50840679, 7.263e-05, 61.52522036, 0.00021789, 205.08406786, 0.00072629, -20.50840679, -7.263e-05, -61.52522036, -0.00021789, -205.08406786, -0.00072629, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.9, 0.0, 6.65)
    ops.node(123003, 7.9, 0.0, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0625, 29745787.41546452, 12394078.08977688, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 36.21757937, 0.00078221, 43.33489166, 0.01103992, 4.33348917, 0.05024106, -36.21757937, -0.00078221, -43.33489166, -0.01103992, -4.33348917, -0.05024106, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 36.21757937, 0.00078221, 43.33489166, 0.01103992, 4.33348917, 0.05024106, -36.21757937, -0.00078221, -43.33489166, -0.01103992, -4.33348917, -0.05024106, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 58.77902841, 0.01564411, 58.77902841, 0.04693233, 41.14531989, -735.60540135, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 14.6947571, 6.602e-05, 44.08427131, 0.00019805, 146.94757102, 0.00066016, -14.6947571, -6.602e-05, -44.08427131, -0.00019805, -146.94757102, -0.00066016, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 58.77902841, 0.01564411, 58.77902841, 0.04693233, 41.14531989, -735.60540135, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 14.6947571, 6.602e-05, 44.08427131, 0.00019805, 146.94757102, 0.00066016, -14.6947571, -6.602e-05, -44.08427131, -0.00019805, -146.94757102, -0.00066016, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.9, 0.0, 6.65)
    ops.node(123004, 12.9, 0.0, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 26731996.61718854, 11138331.92382856, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 28.16495773, 0.00075811, 34.03641473, 0.0136782, 3.40364147, 0.05555669, -28.16495773, -0.00075811, -34.03641473, -0.0136782, -3.40364147, -0.05555669, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 28.16495773, 0.00075811, 34.03641473, 0.0136782, 3.40364147, 0.05555669, -28.16495773, -0.00075811, -34.03641473, -0.0136782, -3.40364147, -0.05555669, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 60.87815726, 0.01516223, 60.87815726, 0.0454867, 42.61471008, -717.19912039, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 15.21953932, 7.608e-05, 45.65861795, 0.00022825, 152.19539316, 0.00076082, -15.21953932, -7.608e-05, -45.65861795, -0.00022825, -152.19539316, -0.00076082, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 60.87815726, 0.01516223, 60.87815726, 0.0454867, 42.61471008, -717.19912039, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 15.21953932, 7.608e-05, 45.65861795, 0.00022825, 152.19539316, 0.00076082, -15.21953932, -7.608e-05, -45.65861795, -0.00022825, -152.19539316, -0.00076082, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.05, 6.675)
    ops.node(123005, 0.0, 4.05, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 30627768.00123139, 12761570.00051308, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 30.02249298, 0.00075138, 36.05923836, 0.01501517, 3.60592384, 0.06251226, -30.02249298, -0.00075138, -36.05923836, -0.01501517, -3.60592384, -0.06251226, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 30.02249298, 0.00075138, 36.05923836, 0.01501517, 3.60592384, 0.06251226, -30.02249298, -0.00075138, -36.05923836, -0.01501517, -3.60592384, -0.06251226, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 73.26280161, 0.01502769, 73.26280161, 0.04508308, 51.28396113, -795.62606669, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 18.3157004, 7.991e-05, 54.94710121, 0.00023974, 183.15700403, 0.00079913, -18.3157004, -7.991e-05, -54.94710121, -0.00023974, -183.15700403, -0.00079913, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 73.26280161, 0.01502769, 73.26280161, 0.04508308, 51.28396113, -795.62606669, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 18.3157004, 7.991e-05, 54.94710121, 0.00023974, 183.15700403, 0.00079913, -18.3157004, -7.991e-05, -54.94710121, -0.00023974, -183.15700403, -0.00079913, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 2.9, 4.05, 6.675)
    ops.node(123006, 2.9, 4.05, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0875, 34366008.81888516, 14319170.34120215, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 71.99452816, 0.00059088, 85.52939118, 0.01155346, 8.55293912, 0.05572124, -71.99452816, -0.00059088, -85.52939118, -0.01155346, -8.55293912, -0.05572124, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 50.06504991, 0.00074816, 59.477204, 0.01062936, 5.9477204, 0.04515293, -50.06504991, -0.00074816, -59.477204, -0.01062936, -5.9477204, -0.04515293, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 99.14185249, 0.01181761, 99.14185249, 0.03545283, 69.39929674, -850.8204039, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 24.78546312, 6.884e-05, 74.35638937, 0.00020652, 247.85463123, 0.00068842, -24.78546312, -6.884e-05, -74.35638937, -0.00020652, -247.85463123, -0.00068842, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 83.23070288, 0.01496328, 83.23070288, 0.04488984, 58.26149201, -731.33464275, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 20.80767572, 5.779e-05, 62.42302716, 0.00017338, 208.07675719, 0.00057793, -20.80767572, -5.779e-05, -62.42302716, -0.00017338, -208.07675719, -0.00057793, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 7.9, 4.05, 6.675)
    ops.node(123007, 7.9, 4.05, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 29210202.04807768, 12170917.52003237, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 92.13300357, 0.00059788, 110.96676939, 0.01041712, 11.09667694, 0.03594471, -92.13300357, -0.00059788, -110.96676939, -0.01041712, -11.09667694, -0.03594471, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 92.13300357, 0.00059788, 110.96676939, 0.01041712, 11.09667694, 0.03594471, -92.13300357, -0.00059788, -110.96676939, -0.01041712, -11.09667694, -0.03594471, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 92.44583652, 0.01195756, 92.44583652, 0.03587268, 64.71208557, -866.67037787, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 23.11145913, 5.394e-05, 69.33437739, 0.00016183, 231.11459131, 0.00053945, -23.11145913, -5.394e-05, -69.33437739, -0.00016183, -231.11459131, -0.00053945, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 92.44583652, 0.01195756, 92.44583652, 0.03587268, 64.71208557, -866.67037787, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 23.11145913, 5.394e-05, 69.33437739, 0.00016183, 231.11459131, 0.00053945, -23.11145913, -5.394e-05, -69.33437739, -0.00016183, -231.11459131, -0.00053945, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 12.9, 4.05, 6.675)
    ops.node(123008, 12.9, 4.05, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 32611804.47918451, 13588251.86632688, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 35.11916137, 0.00081437, 41.85684743, 0.01468434, 4.18568474, 0.06065595, -35.11916137, -0.00081437, -41.85684743, -0.01468434, -4.18568474, -0.06065595, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 35.11916137, 0.00081437, 41.85684743, 0.01468434, 4.18568474, 0.06065595, -35.11916137, -0.00081437, -41.85684743, -0.01468434, -4.18568474, -0.06065595, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 82.68715923, 0.01628746, 82.68715923, 0.04886238, 57.88101146, -887.04777969, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 20.67178981, 8.471e-05, 62.01536942, 0.00025412, 206.71789806, 0.00084706, -20.67178981, -8.471e-05, -62.01536942, -0.00025412, -206.71789806, -0.00084706, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 82.68715923, 0.01628746, 82.68715923, 0.04886238, 57.88101146, -887.04777969, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 20.67178981, 8.471e-05, 62.01536942, 0.00025412, 206.71789806, 0.00084706, -20.67178981, -8.471e-05, -62.01536942, -0.00025412, -206.71789806, -0.00084706, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.1, 6.675)
    ops.node(123009, 0.0, 8.1, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 28156844.32712845, 11732018.46963686, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 27.99019224, 0.0008116, 33.76893766, 0.01346564, 3.37689377, 0.05758255, -27.99019224, -0.0008116, -33.76893766, -0.01346564, -3.37689377, -0.05758255, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 27.99019224, 0.0008116, 33.76893766, 0.01346564, 3.37689377, 0.05758255, -27.99019224, -0.0008116, -33.76893766, -0.01346564, -3.37689377, -0.05758255, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 62.34120188, 0.01623201, 62.34120188, 0.04869603, 43.63884132, -742.19650182, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 15.58530047, 7.397e-05, 46.75590141, 0.0002219, 155.8530047, 0.00073968, -15.58530047, -7.397e-05, -46.75590141, -0.0002219, -155.8530047, -0.00073968, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 62.34120188, 0.01623201, 62.34120188, 0.04869603, 43.63884132, -742.19650182, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 15.58530047, 7.397e-05, 46.75590141, 0.0002219, 155.8530047, 0.00073968, -15.58530047, -7.397e-05, -46.75590141, -0.0002219, -155.8530047, -0.00073968, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 2.9, 8.1, 6.675)
    ops.node(123010, 2.9, 8.1, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0625, 29658117.37699134, 12357548.90707973, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 46.69813287, 0.00083336, 55.85620038, 0.01344788, 5.58562004, 0.04684266, -46.69813287, -0.00083336, -55.85620038, -0.01344788, -5.58562004, -0.04684266, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 46.69813287, 0.00083336, 55.85620038, 0.01344788, 5.58562004, 0.04684266, -46.69813287, -0.00083336, -55.85620038, -0.01344788, -5.58562004, -0.04684266, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 63.26444511, 0.01666713, 63.26444511, 0.05000138, 44.28511157, -778.81265902, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 15.81611128, 7.126e-05, 47.44833383, 0.00021379, 158.16111277, 0.00071263, -15.81611128, -7.126e-05, -47.44833383, -0.00021379, -158.16111277, -0.00071263, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 63.26444511, 0.01666713, 63.26444511, 0.05000138, 44.28511157, -778.81265902, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 15.81611128, 7.126e-05, 47.44833383, 0.00021379, 158.16111277, 0.00071263, -15.81611128, -7.126e-05, -47.44833383, -0.00021379, -158.16111277, -0.00071263, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.9, 8.1, 6.675)
    ops.node(123011, 7.9, 8.1, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 28733964.58742575, 11972485.24476073, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 93.79353455, 0.0005861, 113.0309311, 0.00985176, 11.30309311, 0.0348331, -93.79353455, -0.0005861, -113.0309311, -0.00985176, -11.30309311, -0.0348331, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 93.79353455, 0.0005861, 113.0309311, 0.00985176, 11.30309311, 0.0348331, -93.79353455, -0.0005861, -113.0309311, -0.00985176, -11.30309311, -0.0348331, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 88.69753274, 0.01172208, 88.69753274, 0.03516624, 62.08827292, -810.93793884, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 22.17438318, 5.262e-05, 66.52314955, 0.00015785, 221.74383185, 0.00052615, -22.17438318, -5.262e-05, -66.52314955, -0.00015785, -221.74383185, -0.00052615, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 88.69753274, 0.01172208, 88.69753274, 0.03516624, 62.08827292, -810.93793884, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 22.17438318, 5.262e-05, 66.52314955, 0.00015785, 221.74383185, 0.00052615, -22.17438318, -5.262e-05, -66.52314955, -0.00015785, -221.74383185, -0.00052615, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 12.9, 8.1, 6.675)
    ops.node(123012, 12.9, 8.1, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 28794552.80576825, 11997730.33573677, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 35.8486842, 0.00085576, 42.95818334, 0.01387244, 4.29581833, 0.05176393, -35.8486842, -0.00085576, -42.95818334, -0.01387244, -4.29581833, -0.05176393, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 35.8486842, 0.00085576, 42.95818334, 0.01387244, 4.29581833, 0.05176393, -35.8486842, -0.00085576, -42.95818334, -0.01387244, -4.29581833, -0.05176393, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 76.91218809, 0.0171151, 76.91218809, 0.05134531, 53.83853167, -938.59407663, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 19.22804702, 8.924e-05, 57.68414107, 0.00026771, 192.28047024, 0.00089235, -19.22804702, -8.924e-05, -57.68414107, -0.00026771, -192.28047024, -0.00089235, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 76.91218809, 0.0171151, 76.91218809, 0.05134531, 53.83853167, -938.59407663, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 19.22804702, 8.924e-05, 57.68414107, 0.00026771, 192.28047024, 0.00089235, -19.22804702, -8.924e-05, -57.68414107, -0.00026771, -192.28047024, -0.00089235, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 12.15, 6.675)
    ops.node(123013, 0.0, 12.15, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 31279793.52608627, 13033247.30253595, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 28.1804916, 0.00072608, 33.83311217, 0.01325362, 3.38331122, 0.06316115, -28.1804916, -0.00072608, -33.83311217, -0.01325362, -3.38331122, -0.06316115, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 28.1804916, 0.00072608, 33.83311217, 0.01325362, 3.38331122, 0.06316115, -28.1804916, -0.00072608, -33.83311217, -0.01325362, -3.38331122, -0.06316115, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 65.65516122, 0.01452169, 65.65516122, 0.04356507, 45.95861286, -759.45078904, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 16.41379031, 7.012e-05, 49.24137092, 0.00021037, 164.13790306, 0.00070122, -16.41379031, -7.012e-05, -49.24137092, -0.00021037, -164.13790306, -0.00070122, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 65.65516122, 0.01452169, 65.65516122, 0.04356507, 45.95861286, -759.45078904, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 16.41379031, 7.012e-05, 49.24137092, 0.00021037, 164.13790306, 0.00070122, -16.41379031, -7.012e-05, -49.24137092, -0.00021037, -164.13790306, -0.00070122, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 2.9, 12.15, 6.675)
    ops.node(123014, 2.9, 12.15, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 29446027.70072994, 12269178.20863747, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 45.4957722, 0.00079062, 54.4264477, 0.01123347, 5.44264477, 0.04418433, -45.4957722, -0.00079062, -54.4264477, -0.01123347, -5.44264477, -0.04418433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 45.4957722, 0.00079062, 54.4264477, 0.01123347, 5.44264477, 0.04418433, -45.4957722, -0.00079062, -54.4264477, -0.01123347, -5.44264477, -0.04418433, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 52.5517549, 0.01581238, 52.5517549, 0.04743714, 36.78622843, -684.74319153, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 13.13793873, 5.962e-05, 39.41381618, 0.00017887, 131.37938726, 0.00059623, -13.13793873, -5.962e-05, -39.41381618, -0.00017887, -131.37938726, -0.00059623, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 52.5517549, 0.01581238, 52.5517549, 0.04743714, 36.78622843, -684.74319153, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 13.13793873, 5.962e-05, 39.41381618, 0.00017887, 131.37938726, 0.00059623, -13.13793873, -5.962e-05, -39.41381618, -0.00017887, -131.37938726, -0.00059623, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.9, 12.15, 6.675)
    ops.node(123015, 7.9, 12.15, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 33985055.64515547, 14160439.85214812, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 97.84104199, 0.00062396, 116.57331886, 0.00918806, 11.65733189, 0.03891215, -97.84104199, -0.00062396, -116.57331886, -0.00918806, -11.65733189, -0.03891215, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 97.84104199, 0.00062396, 116.57331886, 0.00918806, 11.65733189, 0.03891215, -97.84104199, -0.00062396, -116.57331886, -0.00918806, -11.65733189, -0.03891215, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 109.39405079, 0.01247912, 109.39405079, 0.03743737, 76.57583555, -833.04843484, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 27.3485127, 5.487e-05, 82.04553809, 0.0001646, 273.48512698, 0.00054866, -27.3485127, -5.487e-05, -82.04553809, -0.0001646, -273.48512698, -0.00054866, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 109.39405079, 0.01247912, 109.39405079, 0.03743737, 76.57583555, -833.04843484, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 27.3485127, 5.487e-05, 82.04553809, 0.0001646, 273.48512698, 0.00054866, -27.3485127, -5.487e-05, -82.04553809, -0.0001646, -273.48512698, -0.00054866, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.9, 12.15, 6.675)
    ops.node(123016, 12.9, 12.15, 9.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 29503528.15808418, 12293136.73253507, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 37.36893296, 0.0008064, 44.75903767, 0.01062373, 4.47590377, 0.05023249, -37.36893296, -0.0008064, -44.75903767, -0.01062373, -4.47590377, -0.05023249, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 37.36893296, 0.0008064, 44.75903767, 0.01062373, 4.47590377, 0.05023249, -37.36893296, -0.0008064, -44.75903767, -0.01062373, -4.47590377, -0.05023249, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 58.40083662, 0.01612793, 58.40083662, 0.04838379, 40.88058563, -738.6745059, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 14.60020915, 6.613e-05, 43.80062746, 0.00019839, 146.00209155, 0.0006613, -14.60020915, -6.613e-05, -43.80062746, -0.00019839, -146.00209155, -0.0006613, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 58.40083662, 0.01612793, 58.40083662, 0.04838379, 40.88058563, -738.6745059, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 14.60020915, 6.613e-05, 43.80062746, 0.00019839, 146.00209155, 0.0006613, -14.60020915, -6.613e-05, -43.80062746, -0.00019839, -146.00209155, -0.0006613, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 16.2, 6.65)
    ops.node(123017, 0.0, 16.2, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 25772694.67954928, 10738622.78314553, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 24.98983473, 0.00076772, 30.37854109, 0.01294556, 3.03785411, 0.05990881, -24.98983473, -0.00076772, -30.37854109, -0.01294556, -3.03785411, -0.05990881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 24.98983473, 0.00076772, 30.37854109, 0.01294556, 3.03785411, 0.05990881, -24.98983473, -0.00076772, -30.37854109, -0.01294556, -3.03785411, -0.05990881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 47.44897333, 0.01535432, 47.44897333, 0.04606297, 33.21428133, -602.77226805, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 11.86224333, 6.151e-05, 35.58672999, 0.00018452, 118.62243331, 0.00061506, -11.86224333, -6.151e-05, -35.58672999, -0.00018452, -118.62243331, -0.00061506, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 47.44897333, 0.01535432, 47.44897333, 0.04606297, 33.21428133, -602.77226805, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 11.86224333, 6.151e-05, 35.58672999, 0.00018452, 118.62243331, 0.00061506, -11.86224333, -6.151e-05, -35.58672999, -0.00018452, -118.62243331, -0.00061506, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 2.9, 16.2, 6.65)
    ops.node(123018, 2.9, 16.2, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 28325885.74358239, 11802452.39315933, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 33.38301413, 0.0007515, 40.14556332, 0.01370682, 4.01455633, 0.05430322, -33.38301413, -0.0007515, -40.14556332, -0.01370682, -4.01455633, -0.05430322, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 33.38301413, 0.0007515, 40.14556332, 0.01370682, 4.01455633, 0.05430322, -33.38301413, -0.0007515, -40.14556332, -0.01370682, -4.01455633, -0.05430322, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 69.39365877, 0.01502998, 69.39365877, 0.04508994, 48.57556114, -795.22260599, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 17.34841469, 8.184e-05, 52.04524407, 0.00024553, 173.48414692, 0.00081844, -17.34841469, -8.184e-05, -52.04524407, -0.00024553, -173.48414692, -0.00081844, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 69.39365877, 0.01502998, 69.39365877, 0.04508994, 48.57556114, -795.22260599, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 17.34841469, 8.184e-05, 52.04524407, 0.00024553, 173.48414692, 0.00081844, -17.34841469, -8.184e-05, -52.04524407, -0.00024553, -173.48414692, -0.00081844, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 7.9, 16.2, 6.65)
    ops.node(123019, 7.9, 16.2, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 32076512.75034245, 13365213.64597602, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 37.5381617, 0.00077901, 44.76351629, 0.01459112, 4.47635163, 0.05874532, -37.5381617, -0.00077901, -44.76351629, -0.01459112, -4.47635163, -0.05874532, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 37.5381617, 0.00077901, 44.76351629, 0.01459112, 4.47635163, 0.05874532, -37.5381617, -0.00077901, -44.76351629, -0.01459112, -4.47635163, -0.05874532, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 83.26694872, 0.01558013, 83.26694872, 0.04674038, 58.2868641, -923.48599364, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 20.81673718, 8.672e-05, 62.45021154, 0.00026017, 208.1673718, 0.00086723, -20.81673718, -8.672e-05, -62.45021154, -0.00026017, -208.1673718, -0.00086723, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 83.26694872, 0.01558013, 83.26694872, 0.04674038, 58.2868641, -923.48599364, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 20.81673718, 8.672e-05, 62.45021154, 0.00026017, 208.1673718, 0.00086723, -20.81673718, -8.672e-05, -62.45021154, -0.00026017, -208.1673718, -0.00086723, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 12.9, 16.2, 6.65)
    ops.node(123020, 12.9, 16.2, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 28593338.41509072, 11913891.0062878, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 27.02759386, 0.00073406, 32.61694846, 0.01570617, 3.26169485, 0.06172507, -27.02759386, -0.00073406, -32.61694846, -0.01570617, -3.26169485, -0.06172507, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 27.02759386, 0.00073406, 32.61694846, 0.01570617, 3.26169485, 0.06172507, -27.02759386, -0.00073406, -32.61694846, -0.01570617, -3.26169485, -0.06172507, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 68.15096614, 0.01468122, 68.15096614, 0.04404367, 47.7056763, -792.33977216, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 17.03774154, 7.963e-05, 51.11322461, 0.00023888, 170.37741535, 0.00079627, -17.03774154, -7.963e-05, -51.11322461, -0.00023888, -170.37741535, -0.00079627, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 68.15096614, 0.01468122, 68.15096614, 0.04404367, 47.7056763, -792.33977216, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 17.03774154, 7.963e-05, 51.11322461, 0.00023888, 170.37741535, 0.00079627, -17.03774154, -7.963e-05, -51.11322461, -0.00023888, -170.37741535, -0.00079627, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.9, 0.0, 9.55)
    ops.node(124003, 7.9, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0625, 24566706.71106451, 10236127.79627688, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 22.31424253, 0.00072247, 27.17397884, 0.01255238, 2.71739788, 0.05869345, -22.31424253, -0.00072247, -27.17397884, -0.01255238, -2.71739788, -0.05869345, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 22.31424253, 0.00072247, 27.17397884, 0.01255238, 2.71739788, 0.05869345, -22.31424253, -0.00072247, -27.17397884, -0.01255238, -2.71739788, -0.05869345, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 38.93191149, 0.01444932, 38.93191149, 0.04334796, 27.25233804, -581.68032745, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 9.73297787, 5.294e-05, 29.19893362, 0.00015883, 97.32977873, 0.00052943, -9.73297787, -5.294e-05, -29.19893362, -0.00015883, -97.32977873, -0.00052943, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 38.93191149, 0.01444932, 38.93191149, 0.04334796, 27.25233804, -581.68032745, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 9.73297787, 5.294e-05, 29.19893362, 0.00015883, 97.32977873, 0.00052943, -9.73297787, -5.294e-05, -29.19893362, -0.00015883, -97.32977873, -0.00052943, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.9, 0.0, 9.55)
    ops.node(124004, 12.9, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 27467684.32445956, 11444868.46852482, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 17.81219198, 0.0006513, 21.72732979, 0.01477155, 2.17273298, 0.07297979, -17.81219198, -0.0006513, -21.72732979, -0.01477155, -2.17273298, -0.07297979, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 17.81219198, 0.0006513, 21.72732979, 0.01477155, 2.17273298, 0.07297979, -17.81219198, -0.0006513, -21.72732979, -0.01477155, -2.17273298, -0.07297979, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 45.44827239, 0.01302609, 45.44827239, 0.03907826, 31.81379067, -693.30637054, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 11.3620681, 5.528e-05, 34.08620429, 0.00016583, 113.62068098, 0.00055277, -11.3620681, -5.528e-05, -34.08620429, -0.00016583, -113.62068098, -0.00055277, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 45.44827239, 0.01302609, 45.44827239, 0.03907826, 31.81379067, -693.30637054, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 11.3620681, 5.528e-05, 34.08620429, 0.00016583, 113.62068098, 0.00055277, -11.3620681, -5.528e-05, -34.08620429, -0.00016583, -113.62068098, -0.00055277, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.05, 9.575)
    ops.node(124005, 0.0, 4.05, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 25527338.74841982, 10636391.14517492, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 19.10276357, 0.00072206, 23.33089962, 0.01760998, 2.33308996, 0.07079986, -19.10276357, -0.00072206, -23.33089962, -0.01760998, -2.33308996, -0.07079986, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 19.10276357, 0.00072206, 23.33089962, 0.01760998, 2.33308996, 0.07079986, -19.10276357, -0.00072206, -23.33089962, -0.01760998, -2.33308996, -0.07079986, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 56.84611764, 0.01444126, 56.84611764, 0.04332377, 39.79228235, -910.67325055, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 14.21152941, 7.44e-05, 42.63458823, 0.00022319, 142.1152941, 0.00074395, -14.21152941, -7.44e-05, -42.63458823, -0.00022319, -142.1152941, -0.00074395, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 56.84611764, 0.01444126, 56.84611764, 0.04332377, 39.79228235, -910.67325055, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 14.21152941, 7.44e-05, 42.63458823, 0.00022319, 142.1152941, 0.00074395, -14.21152941, -7.44e-05, -42.63458823, -0.00022319, -142.1152941, -0.00074395, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 2.9, 4.05, 9.575)
    ops.node(124006, 2.9, 4.05, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0875, 36592168.11400838, 15246736.71417016, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 50.18370631, 0.00059982, 59.38994554, 0.01164059, 5.93899455, 0.06425643, -50.18370631, -0.00059982, -59.38994554, -0.01164059, -5.93899455, -0.06425643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 34.30196023, 0.00078488, 40.59468102, 0.01073654, 4.0594681, 0.05186351, -34.30196023, -0.00078488, -40.59468102, -0.01073654, -4.0594681, -0.05186351, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 94.2275647, 0.01199646, 94.2275647, 0.03598939, 65.95929529, -689.07640191, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 23.55689118, 6.145e-05, 70.67067353, 0.00018435, 235.56891176, 0.00061449, -23.55689118, -6.145e-05, -70.67067353, -0.00018435, -235.56891176, -0.00061449, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 76.9098419, 0.01569752, 76.9098419, 0.04709255, 53.83688933, -523.55913855, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 19.22746048, 5.016e-05, 57.68238143, 0.00015047, 192.27460476, 0.00050155, -19.22746048, -5.016e-05, -57.68238143, -0.00015047, -192.27460476, -0.00050155, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 7.9, 4.05, 9.575)
    ops.node(124007, 7.9, 4.05, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 34624495.45849802, 14426873.10770751, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 78.67653504, 0.00056886, 93.90646054, 0.01087526, 9.39064605, 0.04471909, -78.67653504, -0.00056886, -93.90646054, -0.01087526, -9.39064605, -0.04471909, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 78.67653504, 0.00056886, 93.90646054, 0.01087526, 9.39064605, 0.04471909, -78.67653504, -0.00056886, -93.90646054, -0.01087526, -9.39064605, -0.04471909, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 104.49193855, 0.01137724, 104.49193855, 0.03413173, 73.14435698, -599.48349341, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 26.12298464, 5.144e-05, 78.36895391, 0.00015432, 261.22984637, 0.00051439, -26.12298464, -5.144e-05, -78.36895391, -0.00015432, -261.22984637, -0.00051439, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 104.49193855, 0.01137724, 104.49193855, 0.03413173, 73.14435698, -599.48349341, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 26.12298464, 5.144e-05, 78.36895391, 0.00015432, 261.22984637, 0.00051439, -26.12298464, -5.144e-05, -78.36895391, -0.00015432, -261.22984637, -0.00051439, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 12.9, 4.05, 9.575)
    ops.node(124008, 12.9, 4.05, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 31511266.33273635, 13129694.30530681, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 22.2632915, 0.00069212, 26.82487131, 0.01622977, 2.68248713, 0.0730279, -22.2632915, -0.00069212, -26.82487131, -0.01622977, -2.68248713, -0.0730279, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 22.2632915, 0.00069212, 26.82487131, 0.01622977, 2.68248713, 0.0730279, -22.2632915, -0.00069212, -26.82487131, -0.01622977, -2.68248713, -0.0730279, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 70.39382374, 0.0138423, 70.39382374, 0.04152691, 49.27567661, -844.5080642, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 17.59845593, 7.463e-05, 52.7953678, 0.00022389, 175.98455934, 0.00074631, -17.59845593, -7.463e-05, -52.7953678, -0.00022389, -175.98455934, -0.00074631, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 70.39382374, 0.0138423, 70.39382374, 0.04152691, 49.27567661, -844.5080642, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 17.59845593, 7.463e-05, 52.7953678, 0.00022389, 175.98455934, 0.00074631, -17.59845593, -7.463e-05, -52.7953678, -0.00022389, -175.98455934, -0.00074631, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.1, 9.575)
    ops.node(124009, 0.0, 8.1, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 29896485.92744083, 12456869.13643368, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 19.11974736, 0.00081757, 23.18936122, 0.01462104, 2.31893612, 0.07411785, -19.11974736, -0.00081757, -23.18936122, -0.01462104, -2.31893612, -0.07411785, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 19.11974736, 0.00081757, 23.18936122, 0.01462104, 2.31893612, 0.07411785, -19.11974736, -0.00081757, -23.18936122, -0.01462104, -2.31893612, -0.07411785, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 57.20629038, 0.01635143, 57.20629038, 0.04905428, 40.04440327, -734.25211947, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 14.3015726, 6.393e-05, 42.90471779, 0.00019178, 143.01572596, 0.00063925, -14.3015726, -6.393e-05, -42.90471779, -0.00019178, -143.01572596, -0.00063925, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 57.20629038, 0.01635143, 57.20629038, 0.04905428, 40.04440327, -734.25211947, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 14.3015726, 6.393e-05, 42.90471779, 0.00019178, 143.01572596, 0.00063925, -14.3015726, -6.393e-05, -42.90471779, -0.00019178, -143.01572596, -0.00063925, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 2.9, 8.1, 9.575)
    ops.node(124010, 2.9, 8.1, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0625, 31172226.01967587, 12988427.50819828, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 35.83587396, 0.00085513, 43.14865856, 0.01438586, 4.31486586, 0.06106366, -35.83587396, -0.00085513, -43.14865856, -0.01438586, -4.31486586, -0.06106366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 35.83587396, 0.00085513, 43.14865856, 0.01438586, 4.31486586, 0.06106366, -35.83587396, -0.00085513, -43.14865856, -0.01438586, -4.31486586, -0.06106366, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 53.63645977, 0.0171026, 53.63645977, 0.05130781, 37.54552184, -607.10531037, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 13.40911494, 5.748e-05, 40.22734483, 0.00017245, 134.09114942, 0.00057483, -13.40911494, -5.748e-05, -40.22734483, -0.00017245, -134.09114942, -0.00057483, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 53.63645977, 0.0171026, 53.63645977, 0.05130781, 37.54552184, -607.10531037, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 13.40911494, 5.748e-05, 40.22734483, 0.00017245, 134.09114942, 0.00057483, -13.40911494, -5.748e-05, -40.22734483, -0.00017245, -134.09114942, -0.00057483, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.9, 8.1, 9.575)
    ops.node(124011, 7.9, 8.1, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 26799022.0559676, 11166259.1899865, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 72.32045296, 0.00062762, 88.05861992, 0.01315704, 8.80586199, 0.04264818, -72.32045296, -0.00062762, -88.05861992, -0.01315704, -8.80586199, -0.04264818, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 72.32045296, 0.00062762, 88.05861992, 0.01315704, 8.80586199, 0.04264818, -72.32045296, -0.00062762, -88.05861992, -0.01315704, -8.80586199, -0.04264818, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 85.21886357, 0.01255232, 85.21886357, 0.03765695, 59.6532045, -684.34074822, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 21.30471589, 5.42e-05, 63.91414768, 0.0001626, 213.04715893, 0.00054201, -21.30471589, -5.42e-05, -63.91414768, -0.0001626, -213.04715893, -0.00054201, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 85.21886357, 0.01255232, 85.21886357, 0.03765695, 59.6532045, -684.34074822, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 21.30471589, 5.42e-05, 63.91414768, 0.0001626, 213.04715893, 0.00054201, -21.30471589, -5.42e-05, -63.91414768, -0.0001626, -213.04715893, -0.00054201, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 12.9, 8.1, 9.575)
    ops.node(124012, 12.9, 8.1, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 27813026.13951048, 11588760.8914627, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 21.52496757, 0.00080467, 26.13805989, 0.0139652, 2.61380599, 0.06614416, -21.52496757, -0.00080467, -26.13805989, -0.0139652, -2.61380599, -0.06614416, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 21.52496757, 0.00080467, 26.13805989, 0.0139652, 2.61380599, 0.06614416, -21.52496757, -0.00080467, -26.13805989, -0.0139652, -2.61380599, -0.06614416, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 50.68843418, 0.01609346, 50.68843418, 0.04828039, 35.48190393, -586.08582758, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 12.67210855, 6.089e-05, 38.01632564, 0.00018266, 126.72108546, 0.00060885, -12.67210855, -6.089e-05, -38.01632564, -0.00018266, -126.72108546, -0.00060885, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 50.68843418, 0.01609346, 50.68843418, 0.04828039, 35.48190393, -586.08582758, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 12.67210855, 6.089e-05, 38.01632564, 0.00018266, 126.72108546, 0.00060885, -12.67210855, -6.089e-05, -38.01632564, -0.00018266, -126.72108546, -0.00060885, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 12.15, 9.575)
    ops.node(124013, 0.0, 12.15, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 29369268.79381506, 12237195.33075627, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 19.18152591, 0.00069948, 23.29380222, 0.01489425, 2.32938022, 0.07396387, -19.18152591, -0.00069948, -23.29380222, -0.01489425, -2.32938022, -0.07396387, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 19.18152591, 0.00069948, 23.29380222, 0.01489425, 2.32938022, 0.07396387, -19.18152591, -0.00069948, -23.29380222, -0.01489425, -2.32938022, -0.07396387, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 55.17511357, 0.01398969, 55.17511357, 0.04196907, 38.6225795, -742.74685568, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 13.79377839, 6.276e-05, 41.38133518, 0.00018829, 137.93778393, 0.00062763, -13.79377839, -6.276e-05, -41.38133518, -0.00018829, -137.93778393, -0.00062763, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 55.17511357, 0.01398969, 55.17511357, 0.04196907, 38.6225795, -742.74685568, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 13.79377839, 6.276e-05, 41.38133518, 0.00018829, 137.93778393, 0.00062763, -13.79377839, -6.276e-05, -41.38133518, -0.00018829, -137.93778393, -0.00062763, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 2.9, 12.15, 9.575)
    ops.node(124014, 2.9, 12.15, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 28259832.3644033, 11774930.15183471, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 33.55003308, 0.00083929, 40.62228727, 0.01553387, 4.06222873, 0.05843996, -33.55003308, -0.00083929, -40.62228727, -0.01553387, -4.06222873, -0.05843996, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 33.55003308, 0.00083929, 40.62228727, 0.01553387, 4.06222873, 0.05843996, -33.55003308, -0.00083929, -40.62228727, -0.01553387, -4.06222873, -0.05843996, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 51.69163824, 0.01678587, 51.69163824, 0.05035761, 36.18414677, -612.75392878, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 12.92290956, 6.111e-05, 38.76872868, 0.00018333, 129.22909559, 0.00061108, -12.92290956, -6.111e-05, -38.76872868, -0.00018333, -129.22909559, -0.00061108, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 51.69163824, 0.01678587, 51.69163824, 0.05035761, 36.18414677, -612.75392878, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 12.92290956, 6.111e-05, 38.76872868, 0.00018333, 129.22909559, 0.00061108, -12.92290956, -6.111e-05, -38.76872868, -0.00018333, -129.22909559, -0.00061108, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.9, 12.15, 9.575)
    ops.node(124015, 7.9, 12.15, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 25092554.09734902, 10455230.87389543, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 77.24718437, 0.00061736, 94.20935761, 0.01048777, 9.42093576, 0.03829526, -77.24718437, -0.00061736, -94.20935761, -0.01048777, -9.42093576, -0.03829526, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 77.24718437, 0.00061736, 94.20935761, 0.01048777, 9.42093576, 0.03829526, -77.24718437, -0.00061736, -94.20935761, -0.01048777, -9.42093576, -0.03829526, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 62.45458179, 0.01234716, 62.45458179, 0.03704147, 43.71820725, -584.57267202, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 15.61364545, 4.242e-05, 46.84093634, 0.00012727, 156.13645448, 0.00042424, -15.61364545, -4.242e-05, -46.84093634, -0.00012727, -156.13645448, -0.00042424, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 62.45458179, 0.01234716, 62.45458179, 0.03704147, 43.71820725, -584.57267202, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 15.61364545, 4.242e-05, 46.84093634, 0.00012727, 156.13645448, 0.00042424, -15.61364545, -4.242e-05, -46.84093634, -0.00012727, -156.13645448, -0.00042424, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.9, 12.15, 9.575)
    ops.node(124016, 12.9, 12.15, 11.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 35362482.30750161, 14734367.62812567, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 22.15442946, 0.00080579, 26.35205643, 0.01307036, 2.63520564, 0.07292698, -22.15442946, -0.00080579, -26.35205643, -0.01307036, -2.63520564, -0.07292698, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 22.15442946, 0.00080579, 26.35205643, 0.01307036, 2.63520564, 0.07292698, -22.15442946, -0.00080579, -26.35205643, -0.01307036, -2.63520564, -0.07292698, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 68.9268805, 0.01611585, 68.9268805, 0.04834756, 48.24881635, -639.5270343, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 17.23172012, 6.512e-05, 51.69516037, 0.00019535, 172.31720124, 0.00065117, -17.23172012, -6.512e-05, -51.69516037, -0.00019535, -172.31720124, -0.00065117, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 68.9268805, 0.01611585, 68.9268805, 0.04834756, 48.24881635, -639.5270343, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 17.23172012, 6.512e-05, 51.69516037, 0.00019535, 172.31720124, 0.00065117, -17.23172012, -6.512e-05, -51.69516037, -0.00019535, -172.31720124, -0.00065117, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 16.2, 9.55)
    ops.node(124017, 0.0, 16.2, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 28824854.15998087, 12010355.89999203, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 15.05074537, 0.00077001, 18.33645357, 0.01665207, 1.83364536, 0.07884789, -15.05074537, -0.00077001, -18.33645357, -0.01665207, -1.83364536, -0.07884789, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 15.05074537, 0.00077001, 18.33645357, 0.01665207, 1.83364536, 0.07884789, -15.05074537, -0.00077001, -18.33645357, -0.01665207, -1.83364536, -0.07884789, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 55.48293858, 0.01540024, 55.48293858, 0.04620072, 38.83805701, -976.5105271, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 13.87073465, 6.43e-05, 41.61220394, 0.00019291, 138.70734646, 0.00064305, -13.87073465, -6.43e-05, -41.61220394, -0.00019291, -138.70734646, -0.00064305, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 55.48293858, 0.01540024, 55.48293858, 0.04620072, 38.83805701, -976.5105271, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 13.87073465, 6.43e-05, 41.61220394, 0.00019291, 138.70734646, 0.00064305, -13.87073465, -6.43e-05, -41.61220394, -0.00019291, -138.70734646, -0.00064305, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 2.9, 16.2, 9.55)
    ops.node(124018, 2.9, 16.2, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 29236521.01994664, 12181883.7583111, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 19.62458318, 0.00065838, 23.80885127, 0.01730738, 2.38088513, 0.07407148, -19.62458318, -0.00065838, -23.80885127, -0.01730738, -2.38088513, -0.07407148, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 19.62458318, 0.00065838, 23.80885127, 0.01730738, 2.38088513, 0.07407148, -19.62458318, -0.00065838, -23.80885127, -0.01730738, -2.38088513, -0.07407148, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 62.16905199, 0.01316759, 62.16905199, 0.03950277, 43.51833639, -796.50286479, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 15.542263, 7.104e-05, 46.62678899, 0.00021312, 155.42262997, 0.00071039, -15.542263, -7.104e-05, -46.62678899, -0.00021312, -155.42262997, -0.00071039, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 62.16905199, 0.01316759, 62.16905199, 0.03950277, 43.51833639, -796.50286479, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 15.542263, 7.104e-05, 46.62678899, 0.00021312, 155.42262997, 0.00071039, -15.542263, -7.104e-05, -46.62678899, -0.00021312, -155.42262997, -0.00071039, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 7.9, 16.2, 9.55)
    ops.node(124019, 7.9, 16.2, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 28031039.67788171, 11679599.86578405, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 21.57806701, 0.0007743, 26.19659729, 0.01468669, 2.61965973, 0.06736031, -21.57806701, -0.0007743, -26.19659729, -0.01468669, -2.61965973, -0.06736031, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 21.57806701, 0.0007743, 26.19659729, 0.01468669, 2.61965973, 0.06736031, -21.57806701, -0.0007743, -26.19659729, -0.01468669, -2.61965973, -0.06736031, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 57.25608703, 0.01548601, 57.25608703, 0.04645803, 40.07926092, -708.63435803, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 14.31402176, 6.824e-05, 42.94206527, 0.00020472, 143.14021758, 0.00068239, -14.31402176, -6.824e-05, -42.94206527, -0.00020472, -143.14021758, -0.00068239, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 57.25608703, 0.01548601, 57.25608703, 0.04645803, 40.07926092, -708.63435803, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 14.31402176, 6.824e-05, 42.94206527, 0.00020472, 143.14021758, 0.00068239, -14.31402176, -6.824e-05, -42.94206527, -0.00020472, -143.14021758, -0.00068239, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 12.9, 16.2, 9.55)
    ops.node(124020, 12.9, 16.2, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 27564927.46444438, 11485386.44351849, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 18.23201081, 0.00066004, 22.23543869, 0.01769743, 2.22354387, 0.07600106, -18.23201081, -0.00066004, -22.23543869, -0.01769743, -2.22354387, -0.07600106, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 18.23201081, 0.00066004, 22.23543869, 0.01769743, 2.22354387, 0.07600106, -18.23201081, -0.00066004, -22.23543869, -0.01769743, -2.22354387, -0.07600106, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 59.63454618, 0.0132009, 59.63454618, 0.03960269, 41.74418232, -1031.70246729, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 14.90863654, 7.228e-05, 44.72590963, 0.00021683, 149.08636544, 0.00072276, -14.90863654, -7.228e-05, -44.72590963, -0.00021683, -149.08636544, -0.00072276, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 59.63454618, 0.0132009, 59.63454618, 0.03960269, 41.74418232, -1031.70246729, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 14.90863654, 7.228e-05, 44.72590963, 0.00021683, 149.08636544, 0.00072276, -14.90863654, -7.228e-05, -44.72590963, -0.00021683, -149.08636544, -0.00072276, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124021, 0.0, 0.0, 1.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 170001, 124021, 0.075, 28464197.13391232, 11860082.13913013, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 58.5653578, 0.00055265, 70.32939471, 0.01175317, 7.03293947, 0.05108716, -58.5653578, -0.00055265, -70.32939471, -0.01175317, -7.03293947, -0.05108716, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 50.32958295, 0.00061434, 60.43929787, 0.01116077, 6.04392979, 0.04526277, -50.32958295, -0.00061434, -60.43929787, -0.01116077, -6.04392979, -0.04526277, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 85.90159895, 0.01105306, 85.90159895, 0.03315919, 60.13111926, -1471.64891815, 0.05, 2, 0, 70001, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 21.47539974, 5.07e-05, 64.42619921, 0.0001521, 214.75399737, 0.000507, -21.47539974, -5.07e-05, -64.42619921, -0.0001521, -214.75399737, -0.000507, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 64.49566488, 0.01228672, 64.49566488, 0.03686015, 45.14696542, -1322.61402018, 0.05, 2, 0, 70001, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 16.12391622, 3.807e-05, 48.37174866, 0.0001142, 161.2391622, 0.00038066, -16.12391622, -3.807e-05, -48.37174866, -0.0001142, -161.2391622, -0.00038066, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 0.0, 0.0, 1.95)
    ops.node(121001, 0.0, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 174021, 121001, 0.075, 31852347.73594449, 13271811.55664354, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 51.07833454, 0.00055387, 61.16832177, 0.01292866, 6.11683218, 0.06189136, -51.07833454, -0.00055387, -61.16832177, -0.01292866, -6.11683218, -0.06189136, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 39.40387711, 0.00061286, 47.18769817, 0.012265, 4.71876982, 0.05471495, -39.40387711, -0.00061286, -47.18769817, -0.012265, -4.71876982, -0.05471495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 93.91967591, 0.01107739, 93.91967591, 0.03323218, 65.74377314, -1438.80543481, 0.05, 2, 0, 74021, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 23.47991898, 4.954e-05, 70.43975693, 0.00014861, 234.79918977, 0.00049536, -23.47991898, -4.954e-05, -70.43975693, -0.00014861, -234.79918977, -0.00049536, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 81.21486544, 0.01225724, 81.21486544, 0.03677171, 56.85040581, -1273.01928358, 0.05, 2, 0, 74021, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 20.30371636, 4.284e-05, 60.91114908, 0.00012851, 203.03716361, 0.00042835, -20.30371636, -4.284e-05, -60.91114908, -0.00012851, -203.03716361, -0.00042835, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 2.9, 0.0, 0.0)
    ops.node(124022, 2.9, 0.0, 1.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 170002, 124022, 0.09, 30923534.85695134, 12884806.19039639, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 103.5517373, 0.00061416, 122.94080596, 0.01213907, 12.2940806, 0.04210861, -103.5517373, -0.00061416, -122.94080596, -0.01213907, -12.2940806, -0.04210861, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 100.0557635, 0.00061416, 118.79024462, 0.01213907, 11.87902446, 0.04210861, -100.0557635, -0.00061416, -118.79024462, -0.01213907, -11.87902446, -0.04210861, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 118.84962784, 0.01228322, 118.84962784, 0.03684965, 83.19473949, -2027.31794536, 0.05, 2, 0, 70002, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 29.71240696, 5.381e-05, 89.13722088, 0.00016142, 297.12406959, 0.00053807, -29.71240696, -5.381e-05, -89.13722088, -0.00016142, -297.12406959, -0.00053807, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 118.84962784, 0.01228322, 118.84962784, 0.03684965, 83.19473949, -2027.31794536, 0.05, 2, 0, 70002, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 29.71240696, 5.381e-05, 89.13722088, 0.00016142, 297.12406959, 0.00053807, -29.71240696, -5.381e-05, -89.13722088, -0.00016142, -297.12406959, -0.00053807, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 2.9, 0.0, 1.95)
    ops.node(121002, 2.9, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4055, 174022, 121002, 0.09, 28412699.67988437, 11838624.86661849, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24055, 85.9816291, 0.00060733, 102.30324058, 0.01344509, 10.23032406, 0.03923448, -85.9816291, -0.00060733, -102.30324058, -0.01344509, -10.23032406, -0.03923448, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14055, 82.85082761, 0.00060733, 98.57812928, 0.01344509, 9.85781293, 0.03923448, -82.85082761, -0.00060733, -98.57812928, -0.01344509, -9.85781293, -0.03923448, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24055, 4055, 0.0, 112.06836314, 0.01214669, 112.06836314, 0.03644006, 78.44785419, -2043.6947178, 0.05, 2, 0, 74022, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44055, 28.01709078, 5.522e-05, 84.05127235, 0.00016566, 280.17090784, 0.0005522, -28.01709078, -5.522e-05, -84.05127235, -0.00016566, -280.17090784, -0.0005522, 0.4, 0.3, 0.003, 0.0, 0.0, 24055, 2)
    ops.limitCurve('ThreePoint', 14055, 4055, 0.0, 112.06836314, 0.01214669, 112.06836314, 0.03644006, 78.44785419, -2043.6947178, 0.05, 2, 0, 74022, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34055, 28.01709078, 5.522e-05, 84.05127235, 0.00016566, 280.17090784, 0.0005522, -28.01709078, -5.522e-05, -84.05127235, -0.00016566, -280.17090784, -0.0005522, 0.4, 0.3, 0.003, 0.0, 0.0, 14055, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4055, 99999, 'P', 44055, 'Vy', 34055, 'Vz', 24055, 'My', 14055, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4055, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4055, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.75)
    ops.node(124023, 0.0, 0.0, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 171001, 124023, 0.075, 23907773.84928371, 9961572.43720154, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 43.67668123, 0.00053698, 52.66810311, 0.01253879, 5.26681031, 0.04576115, -43.67668123, -0.00053698, -52.66810311, -0.01253879, -5.26681031, -0.04576115, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 33.7314553, 0.00059194, 40.67552102, 0.01189288, 4.0675521, 0.04069618, -33.7314553, -0.00059194, -40.67552102, -0.01189288, -4.0675521, -0.04069618, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 82.90738725, 0.01073964, 82.90738725, 0.03221892, 58.03517108, -1750.48050594, 0.05, 2, 0, 71001, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 20.72684681, 4.827e-05, 62.18054044, 0.00014482, 207.26846813, 0.00048272, -20.72684681, -4.827e-05, -62.18054044, -0.00014482, -207.26846813, -0.00048272, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 67.44078068, 0.01183887, 67.44078068, 0.0355166, 47.20854648, -1522.06530815, 0.05, 2, 0, 71001, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 16.86019517, 3.927e-05, 50.58058551, 0.0001178, 168.60195171, 0.00039267, -16.86019517, -3.927e-05, -50.58058551, -0.0001178, -168.60195171, -0.00039267, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 0.0, 0.0, 5.125)
    ops.node(122001, 0.0, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 174023, 122001, 0.075, 31482475.05311035, 13117697.93879598, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 41.83989682, 0.00049508, 50.31020786, 0.01380401, 5.03102079, 0.06711161, -41.83989682, -0.00049508, -50.31020786, -0.01380401, -5.03102079, -0.06711161, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 32.00457715, 0.0005345, 38.48376912, 0.01306622, 3.84837691, 0.05928313, -32.00457715, -0.0005345, -38.48376912, -0.01306622, -3.84837691, -0.05928313, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 100.14177812, 0.00990166, 100.14177812, 0.02970499, 70.09924469, -1602.0163376, 0.05, 2, 0, 74023, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 25.03544453, 4.428e-05, 75.10633359, 0.00013283, 250.3544453, 0.00044278, -25.03544453, -4.428e-05, -75.10633359, -0.00013283, -250.3544453, -0.00044278, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 80.34560822, 0.01068995, 80.34560822, 0.03206986, 56.24192576, -1376.11766087, 0.05, 2, 0, 74023, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 20.08640206, 3.552e-05, 60.25920617, 0.00010657, 200.86402056, 0.00035525, -20.08640206, -3.552e-05, -60.25920617, -0.00010657, -200.86402056, -0.00035525, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 2.9, 0.0, 3.75)
    ops.node(124024, 2.9, 0.0, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 171002, 124024, 0.09, 27638134.87680968, 11515889.53200403, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 70.20645286, 0.00051444, 83.99640954, 0.00991325, 8.39964095, 0.03494767, -70.20645286, -0.00051444, -83.99640954, -0.00991325, -8.39964095, -0.03494767, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 70.20645286, 0.00051444, 83.99640954, 0.00991325, 8.39964095, 0.03494767, -70.20645286, -0.00051444, -83.99640954, -0.00991325, -8.39964095, -0.03494767, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 100.61140998, 0.01028873, 100.61140998, 0.03086618, 70.42798699, -1895.49857468, 0.05, 2, 0, 71002, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 25.1528525, 4.223e-05, 75.45855749, 0.00012668, 251.52852495, 0.00042228, -25.1528525, -4.223e-05, -75.45855749, -0.00012668, -251.52852495, -0.00042228, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 100.61140998, 0.01028873, 100.61140998, 0.03086618, 70.42798699, -1895.49857468, 0.05, 2, 0, 71002, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 25.1528525, 4.223e-05, 75.45855749, 0.00012668, 251.52852495, 0.00042228, -25.1528525, -4.223e-05, -75.45855749, -0.00012668, -251.52852495, -0.00042228, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 2.9, 0.0, 5.125)
    ops.node(122002, 2.9, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4060, 174024, 122002, 0.09, 29764165.41108885, 12401735.58795369, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24060, 64.25804511, 0.00054983, 76.97975606, 0.01344803, 7.69797561, 0.04425034, -64.25804511, -0.00054983, -76.97975606, -0.01344803, -7.69797561, -0.04425034, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14060, 64.25804511, 0.00054983, 76.97975606, 0.01344803, 7.69797561, 0.04425034, -64.25804511, -0.00054983, -76.97975606, -0.01344803, -7.69797561, -0.04425034, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24060, 4060, 0.0, 122.05188065, 0.0109965, 122.05188065, 0.03298951, 85.43631646, -1978.89668974, 0.05, 2, 0, 74024, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44060, 30.51297016, 4.757e-05, 91.53891049, 0.0001427, 305.12970163, 0.00047567, -30.51297016, -4.757e-05, -91.53891049, -0.0001427, -305.12970163, -0.00047567, 0.4, 0.3, 0.003, 0.0, 0.0, 24060, 2)
    ops.limitCurve('ThreePoint', 14060, 4060, 0.0, 122.05188065, 0.0109965, 122.05188065, 0.03298951, 85.43631646, -1978.89668974, 0.05, 2, 0, 74024, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34060, 30.51297016, 4.757e-05, 91.53891049, 0.0001427, 305.12970163, 0.00047567, -30.51297016, -4.757e-05, -91.53891049, -0.0001427, -305.12970163, -0.00047567, 0.4, 0.3, 0.003, 0.0, 0.0, 14060, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4060, 99999, 'P', 44060, 'Vy', 34060, 'Vz', 24060, 'My', 14060, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4060, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4060, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.65)
    ops.node(124025, 0.0, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 172001, 124025, 0.0625, 24507031.04931766, 10211262.93721569, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 25.45140098, 0.0005204, 30.85808476, 0.01384428, 3.08580848, 0.05417302, -25.45140098, -0.0005204, -30.85808476, -0.01384428, -3.08580848, -0.05417302, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 25.45140098, 0.0005204, 30.85808476, 0.01384428, 3.08580848, 0.05417302, -25.45140098, -0.0005204, -30.85808476, -0.01384428, -3.08580848, -0.05417302, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 60.61237174, 0.01040792, 60.61237174, 0.03122376, 42.42866022, -1464.84888294, 0.05, 2, 0, 72001, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 15.15309294, 4.131e-05, 45.45927881, 0.00012394, 151.53092936, 0.00041313, -15.15309294, -4.131e-05, -45.45927881, -0.00012394, -151.53092936, -0.00041313, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 60.61237174, 0.01040792, 60.61237174, 0.03122376, 42.42866022, -1464.84888294, 0.05, 2, 0, 72001, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 15.15309294, 4.131e-05, 45.45927881, 0.00012394, 151.53092936, 0.00041313, -15.15309294, -4.131e-05, -45.45927881, -0.00012394, -151.53092936, -0.00041313, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 0.0, 0.0, 8.025)
    ops.node(123001, 0.0, 0.0, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 174025, 123001, 0.0625, 30331275.57485059, 12638031.48952108, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 19.5013216, 0.00050458, 23.58132091, 0.01742874, 2.35813209, 0.07397436, -19.5013216, -0.00050458, -23.58132091, -0.01742874, -2.35813209, -0.07397436, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 19.5013216, 0.00050458, 23.58132091, 0.01742874, 2.35813209, 0.07397436, -19.5013216, -0.00050458, -23.58132091, -0.01742874, -2.35813209, -0.07397436, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 69.23818276, 0.01009154, 69.23818276, 0.03027461, 48.46672793, -1528.44250923, 0.05, 2, 0, 74025, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 17.30954569, 3.813e-05, 51.92863707, 0.00011439, 173.0954569, 0.00038131, -17.30954569, -3.813e-05, -51.92863707, -0.00011439, -173.0954569, -0.00038131, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 69.23818276, 0.01009154, 69.23818276, 0.03027461, 48.46672793, -1528.44250923, 0.05, 2, 0, 74025, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 17.30954569, 3.813e-05, 51.92863707, 0.00011439, 173.0954569, 0.00038131, -17.30954569, -3.813e-05, -51.92863707, -0.00011439, -173.0954569, -0.00038131, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 2.9, 0.0, 6.65)
    ops.node(124026, 2.9, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 172002, 124026, 0.0625, 28468436.25124107, 11861848.43801711, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 46.83340471, 0.00058372, 56.120982, 0.01065188, 5.6120982, 0.04266317, -46.83340471, -0.00058372, -56.120982, -0.01065188, -5.6120982, -0.04266317, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 46.83340471, 0.00058372, 56.120982, 0.01065188, 5.6120982, 0.04266317, -46.83340471, -0.00058372, -56.120982, -0.01065188, -5.6120982, -0.04266317, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 54.70497065, 0.01167442, 54.70497065, 0.03502325, 38.29347946, -1369.0787629, 0.05, 2, 0, 72002, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 13.67624266, 3.21e-05, 41.02872799, 9.63e-05, 136.76242663, 0.00032098, -13.67624266, -3.21e-05, -41.02872799, -9.63e-05, -136.76242663, -0.00032098, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 54.70497065, 0.01167442, 54.70497065, 0.03502325, 38.29347946, -1369.0787629, 0.05, 2, 0, 72002, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 13.67624266, 3.21e-05, 41.02872799, 9.63e-05, 136.76242663, 0.00032098, -13.67624266, -3.21e-05, -41.02872799, -9.63e-05, -136.76242663, -0.00032098, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 2.9, 0.0, 8.025)
    ops.node(123002, 2.9, 0.0, 9.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 174026, 123002, 0.0625, 29190870.3283054, 12162862.63679392, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 37.19040834, 0.0005816, 44.68685453, 0.01247115, 4.46868545, 0.04924793, -37.19040834, -0.0005816, -44.68685453, -0.01247115, -4.46868545, -0.04924793, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 37.19040834, 0.0005816, 44.68685453, 0.01247115, 4.46868545, 0.04924793, -37.19040834, -0.0005816, -44.68685453, -0.01247115, -4.46868545, -0.04924793, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 53.34610273, 0.01163195, 53.34610273, 0.03489586, 37.34227191, -1236.48240343, 0.05, 2, 0, 74026, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 13.33652568, 3.053e-05, 40.00957705, 9.158e-05, 133.36525682, 0.00030526, -13.33652568, -3.053e-05, -40.00957705, -9.158e-05, -133.36525682, -0.00030526, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 53.34610273, 0.01163195, 53.34610273, 0.03489586, 37.34227191, -1236.48240343, 0.05, 2, 0, 74026, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 13.33652568, 3.053e-05, 40.00957705, 9.158e-05, 133.36525682, 0.00030526, -13.33652568, -3.053e-05, -40.00957705, -9.158e-05, -133.36525682, -0.00030526, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.55)
    ops.node(124027, 0.0, 0.0, 10.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4067, 173001, 124027, 0.0625, 28650510.67090354, 11937712.77954314, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24067, 17.36591069, 0.00050899, 21.13275603, 0.01592357, 2.1132756, 0.07519943, -17.36591069, -0.00050899, -21.13275603, -0.01592357, -2.1132756, -0.07519943, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14067, 17.36591069, 0.00050899, 21.13275603, 0.01592357, 2.1132756, 0.07519943, -17.36591069, -0.00050899, -21.13275603, -0.01592357, -2.1132756, -0.07519943, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24067, 4067, 0.0, 59.82279674, 0.01017973, 59.82279674, 0.03053919, 41.87595771, -1490.8136109, 0.05, 2, 0, 73001, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44067, 14.95569918, 3.488e-05, 44.86709755, 0.00010463, 149.55699184, 0.00034878, -14.95569918, -3.488e-05, -44.86709755, -0.00010463, -149.55699184, -0.00034878, 0.4, 0.3, 0.003, 0.0, 0.0, 24067, 2)
    ops.limitCurve('ThreePoint', 14067, 4067, 0.0, 59.82279674, 0.01017973, 59.82279674, 0.03053919, 41.87595771, -1490.8136109, 0.05, 2, 0, 73001, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34067, 14.95569918, 3.488e-05, 44.86709755, 0.00010463, 149.55699184, 0.00034878, -14.95569918, -3.488e-05, -44.86709755, -0.00010463, -149.55699184, -0.00034878, 0.4, 0.3, 0.003, 0.0, 0.0, 14067, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4067, 99999, 'P', 44067, 'Vy', 34067, 'Vz', 24067, 'My', 14067, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4067, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4067, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 0.0, 0.0, 10.925)
    ops.node(124001, 0.0, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 174027, 124001, 0.0625, 28220511.31210559, 11758546.380044, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 13.04647173, 0.00046701, 15.94524082, 0.01563088, 1.59452408, 0.08085764, -13.04647173, -0.00046701, -15.94524082, -0.01563088, -1.59452408, -0.08085764, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 13.04647173, 0.00046701, 15.94524082, 0.01563088, 1.59452408, 0.08085764, -13.04647173, -0.00046701, -15.94524082, -0.01563088, -1.59452408, -0.08085764, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 46.83029947, 0.00934027, 46.83029947, 0.02802082, 32.78120963, -3453.55683192, 0.05, 2, 0, 74027, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 11.70757487, 2.772e-05, 35.1227246, 8.316e-05, 117.07574868, 0.00027719, -11.70757487, -2.772e-05, -35.1227246, -8.316e-05, -117.07574868, -0.00027719, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 46.83029947, 0.00934027, 46.83029947, 0.02802082, 32.78120963, -3453.55683192, 0.05, 2, 0, 74027, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 11.70757487, 2.772e-05, 35.1227246, 8.316e-05, 117.07574868, 0.00027719, -11.70757487, -2.772e-05, -35.1227246, -8.316e-05, -117.07574868, -0.00027719, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 2.9, 0.0, 9.55)
    ops.node(124028, 2.9, 0.0, 10.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 173002, 124028, 0.0625, 29548945.67779272, 12312060.6990803, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 28.46433952, 0.00055386, 34.46111311, 0.01497545, 3.44611131, 0.06243543, -28.46433952, -0.00055386, -34.46111311, -0.01497545, -3.44611131, -0.06243543, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 28.46433952, 0.00055386, 34.46111311, 0.01497545, 3.44611131, 0.06243543, -28.46433952, -0.00055386, -34.46111311, -0.01497545, -3.44611131, -0.06243543, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 48.34737324, 0.01107718, 48.34737324, 0.03323153, 33.84316127, -1128.90742297, 0.05, 2, 0, 73002, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 12.08684331, 2.733e-05, 36.26052993, 8.199e-05, 120.86843309, 0.00027331, -12.08684331, -2.733e-05, -36.26052993, -8.199e-05, -120.86843309, -0.00027331, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 48.34737324, 0.01107718, 48.34737324, 0.03323153, 33.84316127, -1128.90742297, 0.05, 2, 0, 73002, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 12.08684331, 2.733e-05, 36.26052993, 8.199e-05, 120.86843309, 0.00027331, -12.08684331, -2.733e-05, -36.26052993, -8.199e-05, -120.86843309, -0.00027331, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 2.9, 0.0, 10.925)
    ops.node(124002, 2.9, 0.0, 12.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 174028, 124002, 0.0625, 34736904.85322023, 14473710.35550843, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 29.6155346, 0.00052743, 35.3743189, 0.01329666, 3.53743189, 0.06761003, -29.6155346, -0.00052743, -35.3743189, -0.01329666, -3.53743189, -0.06761003, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 29.6155346, 0.00052743, 35.3743189, 0.01329666, 3.53743189, 0.06761003, -29.6155346, -0.00052743, -35.3743189, -0.01329666, -3.53743189, -0.06761003, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 53.74400827, 0.0105486, 53.74400827, 0.03164579, 37.62080579, -1114.63421323, 0.05, 2, 0, 74028, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 13.43600207, 2.584e-05, 40.3080062, 7.753e-05, 134.36002066, 0.00025844, -13.43600207, -2.584e-05, -40.3080062, -7.753e-05, -134.36002066, -0.00025844, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 53.74400827, 0.0105486, 53.74400827, 0.03164579, 37.62080579, -1114.63421323, 0.05, 2, 0, 74028, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 13.43600207, 2.584e-05, 40.3080062, 7.753e-05, 134.36002066, 0.00025844, -13.43600207, -2.584e-05, -40.3080062, -7.753e-05, -134.36002066, -0.00025844, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4070, '-orient', 0, 0, 1, 0, 1, 0)
