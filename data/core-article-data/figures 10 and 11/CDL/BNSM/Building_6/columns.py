import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.16, 26205772.19626042, 10919071.74844184, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 124.78635084, 0.00063855, 150.22700902, 0.01628701, 15.0227009, 0.04161509, -124.78635084, -0.00063855, -150.22700902, -0.01628701, -15.0227009, -0.04161509, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 134.02917014, 0.00063855, 161.35419632, 0.01628701, 16.13541963, 0.04161509, -134.02917014, -0.00063855, -161.35419632, -0.01628701, -16.13541963, -0.04161509, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 148.92743099, 0.01277093, 148.92743099, 0.0383128, 104.2492017, -1499.82822392, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 37.23185775, 7.928e-05, 111.69557325, 0.00023783, 372.31857749, 0.00079278, -37.23185775, -7.928e-05, -111.69557325, -0.00023783, -372.31857749, -0.00079278, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 148.92743099, 0.01277093, 148.92743099, 0.0383128, 104.2492017, -1499.82822392, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 37.23185775, 7.928e-05, 111.69557325, 0.00023783, 372.31857749, 0.00079278, -37.23185775, -7.928e-05, -111.69557325, -0.00023783, -372.31857749, -0.00079278, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.5, 0.0, 0.0)
    ops.node(121002, 4.5, 0.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.25, 28042426.02505859, 11684344.17710775, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 292.43593811, 0.00057645, 351.73651755, 0.0181534, 35.17365176, 0.03957369, -292.43593811, -0.00057645, -351.73651755, -0.0181534, -35.17365176, -0.03957369, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 315.47459741, 0.00057645, 379.44698927, 0.0181534, 37.94469893, 0.03957369, -315.47459741, -0.00057645, -379.44698927, -0.0181534, -37.94469893, -0.03957369, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 231.48173522, 0.01152895, 231.48173522, 0.03458685, 162.03721465, -1918.64565001, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 57.8704338, 7.37e-05, 173.61130141, 0.00022109, 578.70433805, 0.00073698, -57.8704338, -7.37e-05, -173.61130141, -0.00022109, -578.70433805, -0.00073698, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 231.48173522, 0.01152895, 231.48173522, 0.03458685, 162.03721465, -1918.64565001, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 57.8704338, 7.37e-05, 173.61130141, 0.00022109, 578.70433805, 0.00073698, -57.8704338, -7.37e-05, -173.61130141, -0.00022109, -578.70433805, -0.00073698, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.5, 0.0, 0.0)
    ops.node(121005, 16.5, 0.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.25, 26472866.54226427, 11030361.05927678, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 290.28005958, 0.00058812, 349.1544306, 0.01748537, 34.91544306, 0.03668706, -290.28005958, -0.00058812, -349.1544306, -0.01748537, -34.91544306, -0.03668706, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 313.21932179, 0.00058812, 376.74621574, 0.01748537, 37.67462157, 0.03668706, -313.21932179, -0.00058812, -376.74621574, -0.01748537, -37.67462157, -0.03668706, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 219.23321519, 0.01176241, 219.23321519, 0.03528724, 153.46325064, -1920.86048568, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 54.8083038, 7.394e-05, 164.4249114, 0.00022181, 548.08303799, 0.00073937, -54.8083038, -7.394e-05, -164.4249114, -0.00022181, -548.08303799, -0.00073937, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 219.23321519, 0.01176241, 219.23321519, 0.03528724, 153.46325064, -1920.86048568, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 54.8083038, 7.394e-05, 164.4249114, 0.00022181, 548.08303799, 0.00073937, -54.8083038, -7.394e-05, -164.4249114, -0.00022181, -548.08303799, -0.00073937, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 21.0, 0.0, 0.0)
    ops.node(121006, 21.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.16, 26165474.20814762, 10902280.92006151, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 124.64647733, 0.00062366, 150.05561565, 0.01616692, 15.00556156, 0.04141474, -124.64647733, -0.00062366, -150.05561565, -0.01616692, -15.00556156, -0.04141474, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 134.29815488, 0.00062366, 161.6747841, 0.01616692, 16.16747841, 0.04141474, -134.29815488, -0.00062366, -161.6747841, -0.01616692, -16.16747841, -0.04141474, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 148.58714549, 0.01247324, 148.58714549, 0.03741973, 104.01100185, -1496.65880554, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 37.14678637, 7.922e-05, 111.44035912, 0.00023766, 371.46786374, 0.00079219, -37.14678637, -7.922e-05, -111.44035912, -0.00023766, -371.46786374, -0.00079219, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 148.58714549, 0.01247324, 148.58714549, 0.03741973, 104.01100185, -1496.65880554, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 37.14678637, 7.922e-05, 111.44035912, 0.00023766, 371.46786374, 0.00079219, -37.14678637, -7.922e-05, -111.44035912, -0.00023766, -371.46786374, -0.00079219, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.5, 0.0)
    ops.node(121007, 0.0, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.25, 26059655.72111316, 10858189.88379715, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 301.91116764, 0.0005864, 362.99151709, 0.01349223, 36.29915171, 0.02912963, -301.91116764, -0.0005864, -362.99151709, -0.01349223, -36.29915171, -0.02912963, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 301.91116764, 0.0005864, 362.99151709, 0.01349223, 36.29915171, 0.02912963, -301.91116764, -0.0005864, -362.99151709, -0.01349223, -36.29915171, -0.02912963, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 205.69653126, 0.01172806, 205.69653126, 0.03518418, 143.98757188, -1732.07786883, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 51.42413281, 7.047e-05, 154.27239844, 0.00021141, 514.24132815, 0.00070471, -51.42413281, -7.047e-05, -154.27239844, -0.00021141, -514.24132815, -0.00070471, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 205.69653126, 0.01172806, 205.69653126, 0.03518418, 143.98757188, -1732.07786883, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 51.42413281, 7.047e-05, 154.27239844, 0.00021141, 514.24132815, 0.00070471, -51.42413281, -7.047e-05, -154.27239844, -0.00021141, -514.24132815, -0.00070471, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.5, 4.5, 0.0)
    ops.node(121008, 4.5, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.4225, 26835964.15260701, 11181651.73025292, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 756.50357858, 0.00053154, 913.21193251, 0.03603404, 91.32119325, 0.07560236, -756.50357858, -0.00053154, -913.21193251, -0.03603404, -91.32119325, -0.07560236, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 788.84555674, 0.00053154, 952.25349322, 0.03603404, 95.22534932, 0.07560236, -788.84555674, -0.00053154, -952.25349322, -0.03603404, -95.22534932, -0.07560236, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 537.93124748, 0.0106309, 537.93124748, 0.03189269, 376.55187324, -5029.68619414, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 134.48281187, 0.0001059, 403.44843561, 0.00031769, 1344.8281187, 0.00105895, -134.48281187, -0.0001059, -403.44843561, -0.00031769, -1344.8281187, -0.00105895, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 537.93124748, 0.0106309, 537.93124748, 0.03189269, 376.55187324, -5029.68619414, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 134.48281187, 0.0001059, 403.44843561, 0.00031769, 1344.8281187, 0.00105895, -134.48281187, -0.0001059, -403.44843561, -0.00031769, -1344.8281187, -0.00105895, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.0, 4.5, 0.0)
    ops.node(121009, 9.0, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.4225, 27308667.9774602, 11378611.65727508, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 753.56760848, 0.00051912, 911.14243163, 0.03758188, 91.11424316, 0.08048685, -753.56760848, -0.00051912, -911.14243163, -0.03758188, -91.11424316, -0.08048685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 769.4976208, 0.00051912, 930.40349063, 0.03758188, 93.04034906, 0.08048685, -769.4976208, -0.00051912, -930.40349063, -0.03758188, -93.04034906, -0.08048685, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 533.66582233, 0.01038242, 533.66582233, 0.03114725, 373.56607563, -4947.77541799, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 133.41645558, 0.00010324, 400.24936674, 0.00030971, 1334.16455582, 0.00103237, -133.41645558, -0.00010324, -400.24936674, -0.00030971, -1334.16455582, -0.00103237, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 533.66582233, 0.01038242, 533.66582233, 0.03114725, 373.56607563, -4947.77541799, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 133.41645558, 0.00010324, 400.24936674, 0.00030971, 1334.16455582, 0.00103237, -133.41645558, -0.00010324, -400.24936674, -0.00030971, -1334.16455582, -0.00103237, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.0, 4.5, 0.0)
    ops.node(121010, 12.0, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.4225, 26965580.46831044, 11235658.52846268, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 751.17224962, 0.00052219, 908.43029757, 0.03765979, 90.84302976, 0.07980757, -751.17224962, -0.00052219, -908.43029757, -0.03765979, -90.84302976, -0.07980757, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 766.98710584, 0.00052219, 927.55599683, 0.03765979, 92.75559968, 0.07980757, -766.98710584, -0.00052219, -927.55599683, -0.03765979, -92.75559968, -0.07980757, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 531.66925232, 0.01044389, 531.66925232, 0.03133168, 372.16847662, -5050.09176453, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 132.91731308, 0.00010416, 398.75193924, 0.00031248, 1329.17313079, 0.0010416, -132.91731308, -0.00010416, -398.75193924, -0.00031248, -1329.17313079, -0.0010416, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 531.66925232, 0.01044389, 531.66925232, 0.03133168, 372.16847662, -5050.09176453, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 132.91731308, 0.00010416, 398.75193924, 0.00031248, 1329.17313079, 0.0010416, -132.91731308, -0.00010416, -398.75193924, -0.00031248, -1329.17313079, -0.0010416, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 16.5, 4.5, 0.0)
    ops.node(121011, 16.5, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.4225, 26108754.02658393, 10878647.51107664, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 750.29832195, 0.00052869, 905.72963403, 0.035466, 90.5729634, 0.07320128, -750.29832195, -0.00052869, -905.72963403, -0.035466, -90.5729634, -0.07320128, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 782.82201272, 0.00052869, 944.99091141, 0.035466, 94.49909114, 0.07320128, -782.82201272, -0.00052869, -944.99091141, -0.035466, -94.49909114, -0.07320128, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 523.84369668, 0.01057378, 523.84369668, 0.03172134, 366.69058767, -4979.38111411, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 130.96092417, 0.00010599, 392.88277251, 0.00031798, 1309.60924169, 0.00105994, -130.96092417, -0.00010599, -392.88277251, -0.00031798, -1309.60924169, -0.00105994, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 523.84369668, 0.01057378, 523.84369668, 0.03172134, 366.69058767, -4979.38111411, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 130.96092417, 0.00010599, 392.88277251, 0.00031798, 1309.60924169, 0.00105994, -130.96092417, -0.00010599, -392.88277251, -0.00031798, -1309.60924169, -0.00105994, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 21.0, 4.5, 0.0)
    ops.node(121012, 21.0, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.25, 28258902.30848132, 11774542.62853388, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 307.16520778, 0.00058797, 369.35963276, 0.01441657, 36.93596328, 0.03271977, -307.16520778, -0.00058797, -369.35963276, -0.01441657, -36.93596328, -0.03271977, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 307.16520778, 0.00058797, 369.35963276, 0.01441657, 36.93596328, 0.03271977, -307.16520778, -0.00058797, -369.35963276, -0.01441657, -36.93596328, -0.03271977, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 224.31286714, 0.01175949, 224.31286714, 0.03527847, 157.019007, -1755.40398186, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 56.07821678, 7.087e-05, 168.23465035, 0.00021261, 560.78216785, 0.00070868, -56.07821678, -7.087e-05, -168.23465035, -0.00021261, -560.78216785, -0.00070868, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 224.31286714, 0.01175949, 224.31286714, 0.03527847, 157.019007, -1755.40398186, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 56.07821678, 7.087e-05, 168.23465035, 0.00021261, 560.78216785, 0.00070868, -56.07821678, -7.087e-05, -168.23465035, -0.00021261, -560.78216785, -0.00070868, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.25, 26941623.67242133, 11225676.53017555, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 303.61217529, 0.00058083, 365.21192148, 0.01394732, 36.52119215, 0.03075747, -303.61217529, -0.00058083, -365.21192148, -0.01394732, -36.52119215, -0.03075747, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 303.61217529, 0.00058083, 365.21192148, 0.01394732, 36.52119215, 0.03075747, -303.61217529, -0.00058083, -365.21192148, -0.01394732, -36.52119215, -0.03075747, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 212.30049142, 0.01161669, 212.30049142, 0.03485006, 148.61034399, -1726.52735236, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 53.07512285, 7.035e-05, 159.22536856, 0.00021106, 530.75122855, 0.00070353, -53.07512285, -7.035e-05, -159.22536856, -0.00021106, -530.75122855, -0.00070353, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 212.30049142, 0.01161669, 212.30049142, 0.03485006, 148.61034399, -1726.52735236, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 53.07512285, 7.035e-05, 159.22536856, 0.00021106, 530.75122855, 0.00070353, -53.07512285, -7.035e-05, -159.22536856, -0.00021106, -530.75122855, -0.00070353, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.5, 9.0, 0.0)
    ops.node(121014, 4.5, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.4225, 27629569.84973869, 11512320.77072446, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 773.59487735, 0.00051757, 933.60760395, 0.03699126, 93.3607604, 0.07850874, -773.59487735, -0.00051757, -933.60760395, -0.03699126, -93.3607604, -0.07850874, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 789.49553267, 0.00051757, 952.79719937, 0.03699126, 95.27971994, 0.07850874, -789.49553267, -0.00051757, -952.79719937, -0.03699126, -95.27971994, -0.07850874, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 553.73807597, 0.01035139, 553.73807597, 0.03105416, 387.61665318, -5101.50570611, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 138.43451899, 0.00010588, 415.30355698, 0.00031763, 1384.34518993, 0.00105876, -138.43451899, -0.00010588, -415.30355698, -0.00031763, -1384.34518993, -0.00105876, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 553.73807597, 0.01035139, 553.73807597, 0.03105416, 387.61665318, -5101.50570611, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 138.43451899, 0.00010588, 415.30355698, 0.00031763, 1384.34518993, 0.00105876, -138.43451899, -0.00010588, -415.30355698, -0.00031763, -1384.34518993, -0.00105876, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 9.0, 0.0)
    ops.node(121015, 9.0, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.4225, 26975146.87914767, 11239644.5329782, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 747.32825415, 0.00052189, 903.80727981, 0.03762316, 90.38072798, 0.07983436, -747.32825415, -0.00052189, -903.80727981, -0.03762316, -90.38072798, -0.07983436, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 762.98291161, 0.00052189, 922.73978143, 0.03762316, 92.27397814, 0.07983436, -762.98291161, -0.00052189, -922.73978143, -0.03762316, -92.27397814, -0.07983436, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 533.74027476, 0.01043783, 533.74027476, 0.0313135, 373.61819233, -5108.04300278, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 133.43506869, 0.00010453, 400.30520607, 0.00031358, 1334.35068689, 0.00104528, -133.43506869, -0.00010453, -400.30520607, -0.00031358, -1334.35068689, -0.00104528, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 533.74027476, 0.01043783, 533.74027476, 0.0313135, 373.61819233, -5108.04300278, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 133.43506869, 0.00010453, 400.30520607, 0.00031358, 1334.35068689, 0.00104528, -133.43506869, -0.00010453, -400.30520607, -0.00031358, -1334.35068689, -0.00104528, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.0, 9.0, 0.0)
    ops.node(121016, 12.0, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.4225, 26930419.02995164, 11221007.92914652, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 743.65479574, 0.00051772, 899.3850165, 0.03750922, 89.93850165, 0.07961987, -743.65479574, -0.00051772, -899.3850165, -0.03750922, -89.93850165, -0.07961987, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 759.31322477, 0.00051772, 918.32250812, 0.03750922, 91.83225081, 0.07961987, -759.31322477, -0.00051772, -918.32250812, -0.03750922, -91.83225081, -0.07961987, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 528.9553988, 0.0103544, 528.9553988, 0.0310632, 370.26877916, -4996.54348917, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 132.2388497, 0.00010376, 396.7165491, 0.00031129, 1322.388497, 0.00103763, -132.2388497, -0.00010376, -396.7165491, -0.00031129, -1322.388497, -0.00103763, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 528.9553988, 0.0103544, 528.9553988, 0.0310632, 370.26877916, -4996.54348917, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 132.2388497, 0.00010376, 396.7165491, 0.00031129, 1322.388497, 0.00103763, -132.2388497, -0.00010376, -396.7165491, -0.00031129, -1322.388497, -0.00103763, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 16.5, 9.0, 0.0)
    ops.node(121017, 16.5, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.4225, 25843266.05910226, 10768027.52462594, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 787.81200864, 0.00053053, 951.03845221, 0.03578066, 95.10384522, 0.07292007, -787.81200864, -0.00053053, -951.03845221, -0.03578066, -95.10384522, -0.07292007, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 804.57218764, 0.00053053, 971.27116574, 0.03578066, 97.12711657, 0.07292007, -804.57218764, -0.00053053, -971.27116574, -0.03578066, -97.12711657, -0.07292007, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 523.14213014, 0.01061068, 523.14213014, 0.03183203, 366.1994911, -5084.57049711, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 130.78553254, 0.00010694, 392.35659761, 0.00032082, 1307.85532536, 0.0010694, -130.78553254, -0.00010694, -392.35659761, -0.00032082, -1307.85532536, -0.0010694, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 523.14213014, 0.01061068, 523.14213014, 0.03183203, 366.1994911, -5084.57049711, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 130.78553254, 0.00010694, 392.35659761, 0.00032082, 1307.85532536, 0.0010694, -130.78553254, -0.00010694, -392.35659761, -0.00032082, -1307.85532536, -0.0010694, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.25, 26417473.66669993, 11007280.6944583, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 300.98329987, 0.00060218, 361.98769253, 0.01381317, 36.19876925, 0.02996224, -300.98329987, -0.00060218, -361.98769253, -0.01381317, -36.19876925, -0.02996224, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 300.98329987, 0.00060218, 361.98769253, 0.01381317, 36.19876925, 0.02996224, -300.98329987, -0.00060218, -361.98769253, -0.01381317, -36.19876925, -0.02996224, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 209.27540082, 0.01204365, 209.27540082, 0.03613094, 146.49278057, -1745.67109525, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 52.3188502, 7.073e-05, 156.95655061, 0.00021218, 523.18850205, 0.00070726, -52.3188502, -7.073e-05, -156.95655061, -0.00021218, -523.18850205, -0.00070726, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 209.27540082, 0.01204365, 209.27540082, 0.03613094, 146.49278057, -1745.67109525, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 52.3188502, 7.073e-05, 156.95655061, 0.00021218, 523.18850205, 0.00070726, -52.3188502, -7.073e-05, -156.95655061, -0.00021218, -523.18850205, -0.00070726, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.16, 26570602.29628523, 11071084.29011885, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 136.23545114, 0.00063262, 164.0325035, 0.01620345, 16.40325035, 0.04224539, -136.23545114, -0.00063262, -164.0325035, -0.01620345, -16.40325035, -0.04224539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 141.19740754, 0.00063262, 170.00688186, 0.01620345, 17.00068819, 0.04224539, -141.19740754, -0.00063262, -170.00688186, -0.01620345, -17.00068819, -0.04224539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 148.43084495, 0.01265243, 148.43084495, 0.03795729, 103.90159146, -1452.23520954, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 37.10771124, 7.793e-05, 111.32313371, 0.00023379, 371.07711237, 0.00077929, -37.10771124, -7.793e-05, -111.32313371, -0.00023379, -371.07711237, -0.00077929, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 148.43084495, 0.01265243, 148.43084495, 0.03795729, 103.90159146, -1452.23520954, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 37.10771124, 7.793e-05, 111.32313371, 0.00023379, 371.07711237, 0.00077929, -37.10771124, -7.793e-05, -111.32313371, -0.00023379, -371.07711237, -0.00077929, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 4.5, 13.5, 0.0)
    ops.node(121020, 4.5, 13.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.3025, 27287013.83597505, 11369589.09832294, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 397.76365229, 0.00056022, 479.91694209, 0.02479833, 47.99169421, 0.05202132, -397.76365229, -0.00056022, -479.91694209, -0.02479833, -47.99169421, -0.05202132, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 410.57874254, 0.00056022, 495.37883482, 0.02479833, 49.53788348, 0.05202132, -410.57874254, -0.00056022, -495.37883482, -0.02479833, -49.53788348, -0.05202132, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 303.1745312, 0.01120445, 303.1745312, 0.03361336, 212.22217184, -2515.22750595, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 75.7936328, 8.198e-05, 227.3808984, 0.00024594, 757.93632799, 0.0008198, -75.7936328, -8.198e-05, -227.3808984, -0.00024594, -757.93632799, -0.0008198, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 303.1745312, 0.01120445, 303.1745312, 0.03361336, 212.22217184, -2515.22750595, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 75.7936328, 8.198e-05, 227.3808984, 0.00024594, 757.93632799, 0.0008198, -75.7936328, -8.198e-05, -227.3808984, -0.00024594, -757.93632799, -0.0008198, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 9.0, 13.5, 0.0)
    ops.node(121021, 9.0, 13.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.25, 27893067.31273017, 11622111.38030424, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 299.1327699, 0.00058193, 360.58812235, 0.01871047, 36.05881223, 0.04133742, -299.1327699, -0.00058193, -360.58812235, -0.01871047, -36.05881223, -0.04133742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 310.39512087, 0.00058193, 374.16426778, 0.01871047, 37.41642678, 0.04133742, -310.39512087, -0.00058193, -374.16426778, -0.01871047, -37.41642678, -0.04133742, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 222.44555225, 0.01163853, 222.44555225, 0.03491559, 155.71188657, -1763.3315663, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 55.61138806, 7.12e-05, 166.83416418, 0.0002136, 556.11388061, 0.000712, -55.61138806, -7.12e-05, -166.83416418, -0.0002136, -556.11388061, -0.000712, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 222.44555225, 0.01163853, 222.44555225, 0.03491559, 155.71188657, -1763.3315663, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 55.61138806, 7.12e-05, 166.83416418, 0.0002136, 556.11388061, 0.000712, -55.61138806, -7.12e-05, -166.83416418, -0.0002136, -556.11388061, -0.000712, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 12.0, 13.5, 0.0)
    ops.node(121022, 12.0, 13.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.25, 26854750.92851087, 11189479.5535462, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 301.63605012, 0.00058408, 363.74498221, 0.01856635, 36.37449822, 0.03982783, -301.63605012, -0.00058408, -363.74498221, -0.01856635, -36.37449822, -0.03982783, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 313.46024573, 0.00058408, 378.00386082, 0.01856635, 37.80038608, 0.03982783, -313.46024573, -0.00058408, -378.00386082, -0.01856635, -37.80038608, -0.03982783, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 215.82170984, 0.01168159, 215.82170984, 0.03504477, 151.07519689, -1791.43912963, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 53.95542746, 7.175e-05, 161.86628238, 0.00021525, 539.55427459, 0.00071751, -53.95542746, -7.175e-05, -161.86628238, -0.00021525, -539.55427459, -0.00071751, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 215.82170984, 0.01168159, 215.82170984, 0.03504477, 151.07519689, -1791.43912963, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 53.95542746, 7.175e-05, 161.86628238, 0.00021525, 539.55427459, 0.00071751, -53.95542746, -7.175e-05, -161.86628238, -0.00021525, -539.55427459, -0.00071751, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 16.5, 13.5, 0.0)
    ops.node(121023, 16.5, 13.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.3025, 26926101.26402185, 11219208.86000911, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 393.32370427, 0.00055036, 474.61256415, 0.02480102, 47.46125641, 0.05143916, -393.32370427, -0.00055036, -474.61256415, -0.02480102, -47.46125641, -0.05143916, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 406.18125291, 0.00055036, 490.12740362, 0.02480102, 49.01274036, 0.05143916, -406.18125291, -0.00055036, -490.12740362, -0.02480102, -49.01274036, -0.05143916, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 300.34038178, 0.01100726, 300.34038178, 0.03302179, 210.23826725, -2533.81551988, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 75.08509545, 8.23e-05, 225.25528634, 0.00024691, 750.85095445, 0.00082302, -75.08509545, -8.23e-05, -225.25528634, -0.00024691, -750.85095445, -0.00082302, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 300.34038178, 0.01100726, 300.34038178, 0.03302179, 210.23826725, -2533.81551988, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 75.08509545, 8.23e-05, 225.25528634, 0.00024691, 750.85095445, 0.00082302, -75.08509545, -8.23e-05, -225.25528634, -0.00024691, -750.85095445, -0.00082302, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.16, 25940069.81257878, 10808362.42190783, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 135.09801755, 0.00063632, 162.61639998, 0.0164383, 16.26164, 0.04123203, -135.09801755, -0.00063632, -162.61639998, -0.0164383, -16.26164, -0.04123203, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 139.96886065, 0.00063632, 168.47939474, 0.0164383, 16.84793947, 0.04123203, -139.96886065, -0.00063632, -168.47939474, -0.0164383, -16.84793947, -0.04123203, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 147.55291701, 0.01272642, 147.55291701, 0.03817926, 103.28704191, -1497.46795751, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 36.88822925, 7.935e-05, 110.66468776, 0.00023805, 368.88229252, 0.00079351, -36.88822925, -7.935e-05, -110.66468776, -0.00023805, -368.88229252, -0.00079351, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 147.55291701, 0.01272642, 147.55291701, 0.03817926, 103.28704191, -1497.46795751, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 36.88822925, 7.935e-05, 110.66468776, 0.00023805, 368.88229252, 0.00079351, -36.88822925, -7.935e-05, -110.66468776, -0.00023805, -368.88229252, -0.00079351, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.425)
    ops.node(122001, 0.0, 0.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.16, 27233604.07736643, 11347335.03223602, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 97.05726704, 0.00057614, 117.45826735, 0.01778348, 11.74582673, 0.04950369, -97.05726704, -0.00057614, -117.45826735, -0.01778348, -11.74582673, -0.04950369, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 110.95943617, 0.00057614, 134.28260981, 0.01778348, 13.42826098, 0.04950369, -110.95943617, -0.00057614, -134.28260981, -0.01778348, -13.42826098, -0.04950369, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 143.99951048, 0.01152286, 143.99951048, 0.03456857, 100.79965734, -1480.42026203, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 35.99987762, 6.662e-05, 107.99963286, 0.00019987, 359.99877621, 0.00066623, -35.99987762, -6.662e-05, -107.99963286, -0.00019987, -359.99877621, -0.00066623, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 143.99951048, 0.01152286, 143.99951048, 0.03456857, 100.79965734, -1480.42026203, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 35.99987762, 6.662e-05, 107.99963286, 0.00019987, 359.99877621, 0.00066623, -35.99987762, -6.662e-05, -107.99963286, -0.00019987, -359.99877621, -0.00066623, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.5, 0.0, 3.475)
    ops.node(122002, 4.5, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.25, 27891106.0640154, 11621294.19333975, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 215.13168852, 0.00054367, 260.0215302, 0.01455241, 26.00215302, 0.03529718, -215.13168852, -0.00054367, -260.0215302, -0.01455241, -26.00215302, -0.03529718, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 205.12535681, 0.00054367, 247.92725575, 0.01455241, 24.79272558, 0.03529718, -205.12535681, -0.00054367, -247.92725575, -0.01455241, -24.79272558, -0.03529718, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 222.45632425, 0.0108735, 222.45632425, 0.03262049, 155.71942697, -1561.35080871, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 55.61408106, 6.432e-05, 166.84224319, 0.00019295, 556.14081062, 0.00064318, -55.61408106, -6.432e-05, -166.84224319, -0.00019295, -556.14081062, -0.00064318, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 222.45632425, 0.0108735, 222.45632425, 0.03262049, 155.71942697, -1561.35080871, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 55.61408106, 6.432e-05, 166.84224319, 0.00019295, 556.14081062, 0.00064318, -55.61408106, -6.432e-05, -166.84224319, -0.00019295, -556.14081062, -0.00064318, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.5, 0.0, 3.475)
    ops.node(122005, 16.5, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.25, 26347241.14219429, 10978017.14258096, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 218.46534019, 0.00054667, 264.29221734, 0.01448807, 26.42922173, 0.03363894, -218.46534019, -0.00054667, -264.29221734, -0.01448807, -26.42922173, -0.03363894, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 207.53530562, 0.00054667, 251.0694193, 0.01448807, 25.10694193, 0.03363894, -207.53530562, -0.00054667, -251.0694193, -0.01448807, -25.10694193, -0.03363894, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 210.07009874, 0.01093334, 210.07009874, 0.03280003, 147.04906912, -1573.79871266, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 52.51752468, 6.43e-05, 157.55257405, 0.00019289, 525.17524685, 0.00064295, -52.51752468, -6.43e-05, -157.55257405, -0.00019289, -525.17524685, -0.00064295, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 210.07009874, 0.01093334, 210.07009874, 0.03280003, 147.04906912, -1573.79871266, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 52.51752468, 6.43e-05, 157.55257405, 0.00019289, 525.17524685, 0.00064295, -52.51752468, -6.43e-05, -157.55257405, -0.00019289, -525.17524685, -0.00064295, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 21.0, 0.0, 3.425)
    ops.node(122006, 21.0, 0.0, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.16, 24854749.48823403, 10356145.62009751, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 95.73540832, 0.00058808, 115.90029537, 0.01657501, 11.59002954, 0.04416088, -95.73540832, -0.00058808, -115.90029537, -0.01657501, -11.59002954, -0.04416088, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 109.5396657, 0.00058808, 132.61216338, 0.01657501, 13.26121634, 0.04416088, -109.5396657, -0.00058808, -132.61216338, -0.01657501, -13.26121634, -0.04416088, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 132.00530946, 0.01176155, 132.00530946, 0.03528465, 92.40371662, -1452.07177891, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 33.00132736, 6.692e-05, 99.00398209, 0.00020076, 330.01327364, 0.00066919, -33.00132736, -6.692e-05, -99.00398209, -0.00020076, -330.01327364, -0.00066919, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 132.00530946, 0.01176155, 132.00530946, 0.03528465, 92.40371662, -1452.07177891, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 33.00132736, 6.692e-05, 99.00398209, 0.00020076, 330.01327364, 0.00066919, -33.00132736, -6.692e-05, -99.00398209, -0.00020076, -330.01327364, -0.00066919, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.475)
    ops.node(122007, 0.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.25, 26337233.32473681, 10973847.21864034, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 216.54154245, 0.00054814, 261.91891622, 0.01466304, 26.19189162, 0.03370166, -216.54154245, -0.00054814, -261.91891622, -0.01466304, -26.19189162, -0.03370166, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 206.14659137, 0.00054814, 249.34565065, 0.01466304, 24.93456506, 0.03370166, -206.14659137, -0.00054814, -249.34565065, -0.01466304, -24.93456506, -0.03370166, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 210.85827889, 0.01096288, 210.85827889, 0.03288865, 147.60079522, -1591.09839133, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 52.71456972, 6.456e-05, 158.14370917, 0.00019368, 527.14569723, 0.00064561, -52.71456972, -6.456e-05, -158.14370917, -0.00019368, -527.14569723, -0.00064561, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 210.85827889, 0.01096288, 210.85827889, 0.03288865, 147.60079522, -1591.09839133, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 52.71456972, 6.456e-05, 158.14370917, 0.00019368, 527.14569723, 0.00064561, -52.71456972, -6.456e-05, -158.14370917, -0.00019368, -527.14569723, -0.00064561, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.5, 4.5, 3.475)
    ops.node(122008, 4.5, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.4225, 27355811.43813358, 11398254.76588899, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 451.0087357, 0.00048818, 546.52646401, 0.01822278, 54.6526464, 0.04007414, -451.0087357, -0.00048818, -546.52646401, -0.01822278, -54.6526464, -0.04007414, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 392.86928343, 0.00048818, 476.07383914, 0.01822278, 47.60738391, 0.04007414, -392.86928343, -0.00048818, -476.07383914, -0.01822278, -47.60738391, -0.04007414, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 447.60231385, 0.00976362, 447.60231385, 0.02929087, 313.32161969, -2435.72243443, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 111.90057846, 7.807e-05, 335.70173538, 0.00023422, 1119.00578462, 0.00078074, -111.90057846, -7.807e-05, -335.70173538, -0.00023422, -1119.00578462, -0.00078074, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 447.60231385, 0.00976362, 447.60231385, 0.02929087, 313.32161969, -2435.72243443, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 111.90057846, 7.807e-05, 335.70173538, 0.00023422, 1119.00578462, 0.00078074, -111.90057846, -7.807e-05, -335.70173538, -0.00023422, -1119.00578462, -0.00078074, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.0, 4.5, 3.475)
    ops.node(122009, 9.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.4225, 26854801.90912285, 11189500.79546786, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 421.82742907, 0.00048547, 512.13708082, 0.02141625, 51.21370808, 0.04620108, -421.82742907, -0.00048547, -512.13708082, -0.02141625, -51.21370808, -0.04620108, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 365.87984224, 0.00048547, 444.21159324, 0.02141625, 44.42115932, 0.04620108, -365.87984224, -0.00048547, -444.21159324, -0.02141625, -44.42115932, -0.04620108, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 439.88721582, 0.00970943, 439.88721582, 0.02912829, 307.92105107, -2585.55812524, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 109.97180395, 7.816e-05, 329.91541186, 0.00023448, 1099.71803954, 0.0007816, -109.97180395, -7.816e-05, -329.91541186, -0.00023448, -1099.71803954, -0.0007816, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 439.88721582, 0.00970943, 439.88721582, 0.02912829, 307.92105107, -2585.55812524, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 109.97180395, 7.816e-05, 329.91541186, 0.00023448, 1099.71803954, 0.0007816, -109.97180395, -7.816e-05, -329.91541186, -0.00023448, -1099.71803954, -0.0007816, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.0, 4.5, 3.475)
    ops.node(122010, 12.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.4225, 28040559.15407874, 11683566.31419948, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 428.29575546, 0.00048434, 519.26829082, 0.02104864, 51.92682908, 0.04692873, -428.29575546, -0.00048434, -519.26829082, -0.02104864, -51.92682908, -0.04692873, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 371.09119792, 0.00048434, 449.91314909, 0.02104864, 44.99131491, 0.04692873, -371.09119792, -0.00048434, -449.91314909, -0.02104864, -44.99131491, -0.04692873, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 459.45790844, 0.0096868, 459.45790844, 0.02906039, 321.62053591, -2538.05629734, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 114.86447711, 7.818e-05, 344.59343133, 0.00023455, 1148.6447711, 0.00078185, -114.86447711, -7.818e-05, -344.59343133, -0.00023455, -1148.6447711, -0.00078185, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 459.45790844, 0.0096868, 459.45790844, 0.02906039, 321.62053591, -2538.05629734, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 114.86447711, 7.818e-05, 344.59343133, 0.00023455, 1148.6447711, 0.00078185, -114.86447711, -7.818e-05, -344.59343133, -0.00023455, -1148.6447711, -0.00078185, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 16.5, 4.5, 3.475)
    ops.node(122011, 16.5, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.4225, 26102572.60291864, 10876071.91788276, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 451.95794381, 0.00049418, 548.15194354, 0.01812205, 54.81519435, 0.03873687, -451.95794381, -0.00049418, -548.15194354, -0.01812205, -54.81519435, -0.03873687, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 392.81575457, 0.00049418, 476.42202613, 0.01812205, 47.64220261, 0.03873687, -392.81575457, -0.00049418, -476.42202613, -0.01812205, -47.64220261, -0.03873687, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 425.60132726, 0.00988352, 425.60132726, 0.02965055, 297.92092908, -2449.83250053, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 106.40033182, 7.78e-05, 319.20099545, 0.0002334, 1064.00331815, 0.00077801, -106.40033182, -7.78e-05, -319.20099545, -0.0002334, -1064.00331815, -0.00077801, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 425.60132726, 0.00988352, 425.60132726, 0.02965055, 297.92092908, -2449.83250053, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 106.40033182, 7.78e-05, 319.20099545, 0.0002334, 1064.00331815, 0.00077801, -106.40033182, -7.78e-05, -319.20099545, -0.0002334, -1064.00331815, -0.00077801, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.475)
    ops.node(122012, 21.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.25, 28112536.06001035, 11713556.69167098, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 219.50291789, 0.00053972, 265.20815952, 0.01458089, 26.52081595, 0.03544407, -219.50291789, -0.00053972, -265.20815952, -0.01458089, -26.52081595, -0.03544407, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 208.89097997, 0.00053972, 252.38658725, 0.01458089, 25.23865872, 0.03544407, -208.89097997, -0.00053972, -252.38658725, -0.01458089, -25.23865872, -0.03544407, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 225.08406107, 0.01079432, 225.08406107, 0.03238295, 157.55884275, -1575.47310386, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 56.27101527, 6.456e-05, 168.8130458, 0.00019369, 562.71015268, 0.00064565, -56.27101527, -6.456e-05, -168.8130458, -0.00019369, -562.71015268, -0.00064565, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 225.08406107, 0.01079432, 225.08406107, 0.03238295, 157.55884275, -1575.47310386, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 56.27101527, 6.456e-05, 168.8130458, 0.00019369, 562.71015268, 0.00064565, -56.27101527, -6.456e-05, -168.8130458, -0.00019369, -562.71015268, -0.00064565, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.475)
    ops.node(122013, 0.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.25, 27235374.89790257, 11348072.87412607, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 218.09038538, 0.00054199, 263.71571065, 0.01487305, 26.37157106, 0.03492606, -218.09038538, -0.00054199, -263.71571065, -0.01487305, -26.37157106, -0.03492606, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 207.44223822, 0.00054199, 250.83993122, 0.01487305, 25.08399312, 0.03492606, -207.44223822, -0.00054199, -250.83993122, -0.01487305, -25.08399312, -0.03492606, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 218.06373865, 0.01083986, 218.06373865, 0.03251958, 152.64461706, -1585.31334573, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 54.51593466, 6.457e-05, 163.54780399, 0.0001937, 545.15934664, 0.00064566, -54.51593466, -6.457e-05, -163.54780399, -0.0001937, -545.15934664, -0.00064566, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 218.06373865, 0.01083986, 218.06373865, 0.03251958, 152.64461706, -1585.31334573, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 54.51593466, 6.457e-05, 163.54780399, 0.0001937, 545.15934664, 0.00064566, -54.51593466, -6.457e-05, -163.54780399, -0.0001937, -545.15934664, -0.00064566, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.5, 9.0, 3.475)
    ops.node(122014, 4.5, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.4225, 28261072.16301993, 11775446.73459164, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 452.69876038, 0.00048581, 548.03938151, 0.01809978, 54.80393815, 0.04078694, -452.69876038, -0.00048581, -548.03938151, -0.01809978, -54.80393815, -0.04078694, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 394.17220873, 0.00048581, 477.18684563, 0.01809978, 47.71868456, 0.04078694, -394.17220873, -0.00048581, -477.18684563, -0.01809978, -47.71868456, -0.04078694, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 463.81962213, 0.00971628, 463.81962213, 0.02914885, 324.67373549, -2430.64835754, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 115.95490553, 7.831e-05, 347.8647166, 0.00023493, 1159.54905532, 0.00078311, -115.95490553, -7.831e-05, -347.8647166, -0.00023493, -1159.54905532, -0.00078311, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 463.81962213, 0.00971628, 463.81962213, 0.02914885, 324.67373549, -2430.64835754, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 115.95490553, 7.831e-05, 347.8647166, 0.00023493, 1159.54905532, 0.00078311, -115.95490553, -7.831e-05, -347.8647166, -0.00023493, -1159.54905532, -0.00078311, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 9.0, 3.475)
    ops.node(122015, 9.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.4225, 28281314.79391966, 11783881.16413319, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 430.09943074, 0.00048094, 521.26873157, 0.02126369, 52.12687316, 0.04734096, -430.09943074, -0.00048094, -521.26873157, -0.02126369, -52.12687316, -0.04734096, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 371.93288978, 0.00048094, 450.77247685, 0.02126369, 45.07724768, 0.04734096, -371.93288978, -0.00048094, -450.77247685, -0.02126369, -45.07724768, -0.04734096, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 465.88253444, 0.00961886, 465.88253444, 0.02885659, 326.11777411, -2584.81719875, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 116.47063361, 7.86e-05, 349.41190083, 0.00023581, 1164.70633611, 0.00078603, -116.47063361, -7.86e-05, -349.41190083, -0.00023581, -1164.70633611, -0.00078603, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 465.88253444, 0.00961886, 465.88253444, 0.02885659, 326.11777411, -2584.81719875, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 116.47063361, 7.86e-05, 349.41190083, 0.00023581, 1164.70633611, 0.00078603, -116.47063361, -7.86e-05, -349.41190083, -0.00023581, -1164.70633611, -0.00078603, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.0, 9.0, 3.475)
    ops.node(122016, 12.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.4225, 26726912.51378809, 11136213.5474117, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 427.71413646, 0.0004852, 519.33898387, 0.02093465, 51.93389839, 0.04558414, -427.71413646, -0.0004852, -519.33898387, -0.02093465, -51.93389839, -0.04558414, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 369.34923032, 0.0004852, 448.47115777, 0.02093465, 44.84711578, 0.04558414, -369.34923032, -0.0004852, -448.47115777, -0.02093465, -44.84711578, -0.04558414, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 435.58846154, 0.00970402, 435.58846154, 0.02911205, 304.91192308, -2536.35500144, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 108.89711539, 7.777e-05, 326.69134616, 0.0002333, 1088.97115385, 0.00077766, -108.89711539, -7.777e-05, -326.69134616, -0.0002333, -1088.97115385, -0.00077766, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 435.58846154, 0.00970402, 435.58846154, 0.02911205, 304.91192308, -2536.35500144, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 108.89711539, 7.777e-05, 326.69134616, 0.0002333, 1088.97115385, 0.00077766, -108.89711539, -7.777e-05, -326.69134616, -0.0002333, -1088.97115385, -0.00077766, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 16.5, 9.0, 3.475)
    ops.node(122017, 16.5, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.4225, 27053243.33385048, 11272184.7224377, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 452.72775515, 0.00048651, 548.80488992, 0.01831784, 54.88048899, 0.03994007, -452.72775515, -0.00048651, -548.80488992, -0.01831784, -54.88048899, -0.03994007, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 392.78391052, 0.00048651, 476.13986182, 0.01831784, 47.61398618, 0.03994007, -392.78391052, -0.00048651, -476.13986182, -0.01831784, -47.61398618, -0.03994007, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 442.96812344, 0.0097303, 442.96812344, 0.0291909, 310.07768641, -2460.87711514, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 110.74203086, 7.813e-05, 332.22609258, 0.00023439, 1107.42030861, 0.0007813, -110.74203086, -7.813e-05, -332.22609258, -0.00023439, -1107.42030861, -0.0007813, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 442.96812344, 0.0097303, 442.96812344, 0.0291909, 310.07768641, -2460.87711514, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 110.74203086, 7.813e-05, 332.22609258, 0.00023439, 1107.42030861, 0.0007813, -110.74203086, -7.813e-05, -332.22609258, -0.00023439, -1107.42030861, -0.0007813, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.475)
    ops.node(122018, 21.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.25, 25624750.62083347, 10676979.42534728, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 215.10980163, 0.00054745, 260.21191533, 0.01431721, 26.02119153, 0.03257449, -215.10980163, -0.00054745, -260.21191533, -0.01431721, -26.02119153, -0.03257449, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 204.62633929, 0.00054745, 247.53038342, 0.01431721, 24.75303834, 0.03257449, -204.62633929, -0.00054745, -247.53038342, -0.01431721, -24.75303834, -0.03257449, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 204.52361721, 0.01094904, 204.52361721, 0.03284713, 143.16653205, -1581.68143645, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 51.1309043, 6.436e-05, 153.39271291, 0.00019309, 511.30904302, 0.00064363, -51.1309043, -6.436e-05, -153.39271291, -0.00019309, -511.30904302, -0.00064363, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 204.52361721, 0.01094904, 204.52361721, 0.03284713, 143.16653205, -1581.68143645, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 51.1309043, 6.436e-05, 153.39271291, 0.00019309, 511.30904302, 0.00064363, -51.1309043, -6.436e-05, -153.39271291, -0.00019309, -511.30904302, -0.00064363, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.425)
    ops.node(122019, 0.0, 13.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.16, 26463191.30196878, 11026329.70915366, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 104.44787592, 0.00057973, 126.45696946, 0.01757214, 12.64569695, 0.0480682, -104.44787592, -0.00057973, -126.45696946, -0.01757214, -12.64569695, -0.0480682, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 100.05230654, 0.00057973, 121.13517254, 0.01757214, 12.11351725, 0.0480682, -100.05230654, -0.00057973, -121.13517254, -0.01757214, -12.11351725, -0.0480682, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 140.50507565, 0.01159455, 140.50507565, 0.03478364, 98.35355295, -1482.93372478, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 35.12626891, 6.69e-05, 105.37880673, 0.0002007, 351.26268912, 0.00066899, -35.12626891, -6.69e-05, -105.37880673, -0.0002007, -351.26268912, -0.00066899, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 140.50507565, 0.01159455, 140.50507565, 0.03478364, 98.35355295, -1482.93372478, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 35.12626891, 6.69e-05, 105.37880673, 0.0002007, 351.26268912, 0.00066899, -35.12626891, -6.69e-05, -105.37880673, -0.0002007, -351.26268912, -0.00066899, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 4.5, 13.5, 3.475)
    ops.node(122020, 4.5, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.3025, 26821208.68327714, 11175503.61803214, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 271.58077983, 0.00052341, 329.22957795, 0.01473819, 32.9229578, 0.03472244, -271.58077983, -0.00052341, -329.22957795, -0.01473819, -32.9229578, -0.03472244, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 248.43315386, 0.00052341, 301.16837592, 0.01473819, 30.11683759, 0.03472244, -248.43315386, -0.00052341, -301.16837592, -0.01473819, -30.11683759, -0.03472244, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 267.84005965, 0.01046826, 267.84005965, 0.03140479, 187.48804176, -1668.76747593, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 66.96001491, 6.655e-05, 200.88004474, 0.00019966, 669.60014913, 0.00066552, -66.96001491, -6.655e-05, -200.88004474, -0.00019966, -669.60014913, -0.00066552, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 267.84005965, 0.01046826, 267.84005965, 0.03140479, 187.48804176, -1668.76747593, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 66.96001491, 6.655e-05, 200.88004474, 0.00019966, 669.60014913, 0.00066552, -66.96001491, -6.655e-05, -200.88004474, -0.00019966, -669.60014913, -0.00066552, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.475)
    ops.node(122021, 9.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.25, 26533323.29096138, 11055551.37123391, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 204.51314362, 0.00053853, 247.86161914, 0.01472644, 24.78616191, 0.03518672, -204.51314362, -0.00053853, -247.86161914, -0.01472644, -24.78616191, -0.03518672, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 193.86020919, 0.00053853, 234.95069552, 0.01472644, 23.49506955, 0.03518672, -193.86020919, -0.00053853, -234.95069552, -0.01472644, -23.49506955, -0.03518672, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 204.70013012, 0.01077068, 204.70013012, 0.03231204, 143.29009108, -1442.91514224, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 51.17503253, 6.221e-05, 153.52509759, 0.00018664, 511.75032529, 0.00062212, -51.17503253, -6.221e-05, -153.52509759, -0.00018664, -511.75032529, -0.00062212, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 204.70013012, 0.01077068, 204.70013012, 0.03231204, 143.29009108, -1442.91514224, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 51.17503253, 6.221e-05, 153.52509759, 0.00018664, 511.75032529, 0.00062212, -51.17503253, -6.221e-05, -153.52509759, -0.00018664, -511.75032529, -0.00062212, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.475)
    ops.node(122022, 12.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.25, 26487986.70970289, 11036661.12904287, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 201.68439884, 0.00053699, 244.43918848, 0.01491903, 24.44391885, 0.03533301, -201.68439884, -0.00053699, -244.43918848, -0.01491903, -24.44391885, -0.03533301, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 191.44936847, 0.00053699, 232.03444853, 0.01491903, 23.20344485, 0.03533301, -191.44936847, -0.00053699, -232.03444853, -0.01491903, -23.20344485, -0.03533301, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 205.42170769, 0.01073981, 205.42170769, 0.03221944, 143.79519538, -1466.63738532, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 51.35542692, 6.254e-05, 154.06628077, 0.00018762, 513.55426923, 0.00062539, -51.35542692, -6.254e-05, -154.06628077, -0.00018762, -513.55426923, -0.00062539, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 205.42170769, 0.01073981, 205.42170769, 0.03221944, 143.79519538, -1466.63738532, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 51.35542692, 6.254e-05, 154.06628077, 0.00018762, 513.55426923, 0.00062539, -51.35542692, -6.254e-05, -154.06628077, -0.00018762, -513.55426923, -0.00062539, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 16.5, 13.5, 3.475)
    ops.node(122023, 16.5, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.3025, 26546988.5390944, 11061245.22462267, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 268.30444737, 0.00051398, 325.31728748, 0.01482187, 32.53172875, 0.03455052, -268.30444737, -0.00051398, -325.31728748, -0.01482187, -32.53172875, -0.03455052, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 245.26641676, 0.00051398, 297.38383464, 0.01482187, 29.73838346, 0.03455052, -245.26641676, -0.00051398, -297.38383464, -0.01482187, -29.73838346, -0.03455052, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 264.60086916, 0.01027955, 264.60086916, 0.03083866, 185.22060841, -1663.62616592, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 66.15021729, 6.643e-05, 198.45065187, 0.00019928, 661.50217291, 0.00066426, -66.15021729, -6.643e-05, -198.45065187, -0.00019928, -661.50217291, -0.00066426, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 264.60086916, 0.01027955, 264.60086916, 0.03083866, 185.22060841, -1663.62616592, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 66.15021729, 6.643e-05, 198.45065187, 0.00019928, 661.50217291, 0.00066426, -66.15021729, -6.643e-05, -198.45065187, -0.00019928, -661.50217291, -0.00066426, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.425)
    ops.node(122024, 21.0, 13.5, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.16, 26532703.90003129, 11055293.29167971, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 106.53022459, 0.00057274, 128.97458498, 0.01736914, 12.8974585, 0.04797997, -106.53022459, -0.00057274, -128.97458498, -0.01736914, -12.8974585, -0.04797997, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 101.72664762, 0.00057274, 123.15896458, 0.01736914, 12.31589646, 0.04797997, -101.72664762, -0.00057274, -123.15896458, -0.01736914, -12.31589646, -0.04797997, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 140.19401294, 0.01145475, 140.19401294, 0.03436425, 98.13580906, -1466.30964659, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 35.04850324, 6.658e-05, 105.14550971, 0.00019973, 350.48503235, 0.00066576, -35.04850324, -6.658e-05, -105.14550971, -0.00019973, -350.48503235, -0.00066576, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 140.19401294, 0.01145475, 140.19401294, 0.03436425, 98.13580906, -1466.30964659, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 35.04850324, 6.658e-05, 105.14550971, 0.00019973, 350.48503235, 0.00066576, -35.04850324, -6.658e-05, -105.14550971, -0.00019973, -350.48503235, -0.00066576, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.175)
    ops.node(123001, 0.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.1225, 26688861.56221139, 11120358.98425475, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 60.25278653, 0.00061823, 73.12402017, 0.01917182, 7.31240202, 0.05577923, -60.25278653, -0.00061823, -73.12402017, -0.01917182, -7.31240202, -0.05577923, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 67.26595465, 0.00061823, 81.63534516, 0.01917182, 8.16353452, 0.05577923, -67.26595465, -0.00061823, -81.63534516, -0.01917182, -8.16353452, -0.05577923, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 109.76435744, 0.01236468, 109.76435744, 0.03709403, 76.83505021, -1233.79732155, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 27.44108936, 6.768e-05, 82.32326808, 0.00020305, 274.41089361, 0.00067684, -27.44108936, -6.768e-05, -82.32326808, -0.00020305, -274.41089361, -0.00067684, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 109.76435744, 0.01236468, 109.76435744, 0.03709403, 76.83505021, -1233.79732155, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 27.44108936, 6.768e-05, 82.32326808, 0.00020305, 274.41089361, 0.00067684, -27.44108936, -6.768e-05, -82.32326808, -0.00020305, -274.41089361, -0.00067684, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.5, 0.0, 6.225)
    ops.node(123002, 4.5, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.16, 26897834.17970275, 11207430.90820948, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 117.29262496, 0.00060829, 141.86117614, 0.01561092, 14.18611761, 0.03799945, -117.29262496, -0.00060829, -141.86117614, -0.01561092, -14.18611761, -0.03799945, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 117.29262496, 0.00060829, 141.86117614, 0.01561092, 14.18611761, 0.03799945, -117.29262496, -0.00060829, -141.86117614, -0.01561092, -14.18611761, -0.03799945, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 128.54555334, 0.01216579, 128.54555334, 0.03649737, 89.98188734, -1133.39447431, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 32.13638833, 6.022e-05, 96.409165, 0.00018065, 321.36388335, 0.00060216, -32.13638833, -6.022e-05, -96.409165, -0.00018065, -321.36388335, -0.00060216, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 128.54555334, 0.01216579, 128.54555334, 0.03649737, 89.98188734, -1133.39447431, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 32.13638833, 6.022e-05, 96.409165, 0.00018065, 321.36388335, 0.00060216, -32.13638833, -6.022e-05, -96.409165, -0.00018065, -321.36388335, -0.00060216, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.5, 0.0, 6.225)
    ops.node(123005, 16.5, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.16, 25788174.79244663, 10745072.8301861, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 120.04643954, 0.00061803, 145.22422262, 0.01492439, 14.52242226, 0.03589706, -120.04643954, -0.00061803, -145.22422262, -0.01492439, -14.52242226, -0.03589706, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 120.04643954, 0.00061803, 145.22422262, 0.01492439, 14.52242226, 0.03589706, -120.04643954, -0.00061803, -145.22422262, -0.01492439, -14.52242226, -0.03589706, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 122.38557354, 0.01236051, 122.38557354, 0.03708154, 85.66990148, -1110.87738138, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 30.59639339, 5.98e-05, 91.78918016, 0.00017939, 305.96393385, 0.00059797, -30.59639339, -5.98e-05, -91.78918016, -0.00017939, -305.96393385, -0.00059797, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 122.38557354, 0.01236051, 122.38557354, 0.03708154, 85.66990148, -1110.87738138, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 30.59639339, 5.98e-05, 91.78918016, 0.00017939, 305.96393385, 0.00059797, -30.59639339, -5.98e-05, -91.78918016, -0.00017939, -305.96393385, -0.00059797, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 21.0, 0.0, 6.175)
    ops.node(123006, 21.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1225, 27697873.8242552, 11540780.76010633, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 61.42260981, 0.00060574, 74.46793477, 0.01865993, 7.44679348, 0.05676726, -61.42260981, -0.00060574, -74.46793477, -0.01865993, -7.44679348, -0.05676726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 69.08307563, 0.00060574, 83.75537908, 0.01865993, 8.37553791, 0.05676726, -69.08307563, -0.00060574, -83.75537908, -0.01865993, -8.37553791, -0.05676726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 111.21809142, 0.01211484, 111.21809142, 0.03634453, 77.852664, -1170.54755269, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 27.80452286, 6.608e-05, 83.41356857, 0.00019825, 278.04522856, 0.00066082, -27.80452286, -6.608e-05, -83.41356857, -0.00019825, -278.04522856, -0.00066082, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 111.21809142, 0.01211484, 111.21809142, 0.03634453, 77.852664, -1170.54755269, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 27.80452286, 6.608e-05, 83.41356857, 0.00019825, 278.04522856, 0.00066082, -27.80452286, -6.608e-05, -83.41356857, -0.00019825, -278.04522856, -0.00066082, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.225)
    ops.node(123007, 0.0, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.16, 26230690.76793905, 10929454.48664127, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 118.79755466, 0.00060825, 143.68451403, 0.0153958, 14.3684514, 0.0368321, -118.79755466, -0.00060825, -143.68451403, -0.0153958, -14.3684514, -0.0368321, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 118.79755466, 0.00060825, 143.68451403, 0.0153958, 14.3684514, 0.0368321, -118.79755466, -0.00060825, -143.68451403, -0.0153958, -14.3684514, -0.0368321, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 125.39461423, 0.01216492, 125.39461423, 0.03649477, 87.77622996, -1131.99276193, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 31.34865356, 6.023e-05, 94.04596067, 0.0001807, 313.48653558, 0.00060234, -31.34865356, -6.023e-05, -94.04596067, -0.0001807, -313.48653558, -0.00060234, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 125.39461423, 0.01216492, 125.39461423, 0.03649477, 87.77622996, -1131.99276193, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 31.34865356, 6.023e-05, 94.04596067, 0.0001807, 313.48653558, 0.00060234, -31.34865356, -6.023e-05, -94.04596067, -0.0001807, -313.48653558, -0.00060234, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.5, 4.5, 6.225)
    ops.node(123008, 4.5, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.3025, 26383840.34136065, 10993266.80890027, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 262.22465959, 0.00051631, 318.26053318, 0.01497132, 31.82605332, 0.03507473, -262.22465959, -0.00051631, -318.26053318, -0.01497132, -31.82605332, -0.03507473, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 238.95683045, 0.00051631, 290.02050526, 0.01497132, 29.00205053, 0.03507473, -238.95683045, -0.00051631, -290.02050526, -0.01497132, -29.00205053, -0.03507473, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 258.62862973, 0.01032619, 258.62862973, 0.03097858, 181.04004081, -1593.97947418, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 64.65715743, 6.533e-05, 193.9714723, 0.00019599, 646.57157433, 0.00065329, -64.65715743, -6.533e-05, -193.9714723, -0.00019599, -646.57157433, -0.00065329, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 258.62862973, 0.01032619, 258.62862973, 0.03097858, 181.04004081, -1593.97947418, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 64.65715743, 6.533e-05, 193.9714723, 0.00019599, 646.57157433, 0.00065329, -64.65715743, -6.533e-05, -193.9714723, -0.00019599, -646.57157433, -0.00065329, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.225)
    ops.node(123009, 9.0, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.3025, 26877483.53855051, 11198951.47439605, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 251.08483527, 0.00051208, 305.08056115, 0.01526874, 30.50805611, 0.03674616, -251.08483527, -0.00051208, -305.08056115, -0.01526874, -30.50805611, -0.03674616, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 227.39401676, 0.00051208, 276.29503853, 0.01526874, 27.62950385, 0.03674616, -227.39401676, -0.00051208, -276.29503853, -0.01526874, -27.62950385, -0.03674616, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 257.26047754, 0.0102415, 257.26047754, 0.03072451, 180.08233427, -1492.84903091, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 64.31511938, 6.379e-05, 192.94535815, 0.00019137, 643.15119384, 0.0006379, -64.31511938, -6.379e-05, -192.94535815, -0.00019137, -643.15119384, -0.0006379, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 257.26047754, 0.0102415, 257.26047754, 0.03072451, 180.08233427, -1492.84903091, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 64.31511938, 6.379e-05, 192.94535815, 0.00019137, 643.15119384, 0.0006379, -64.31511938, -6.379e-05, -192.94535815, -0.00019137, -643.15119384, -0.0006379, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.225)
    ops.node(123010, 12.0, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.3025, 25906703.05202293, 10794459.60500956, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 247.21948155, 0.00051276, 300.6304961, 0.01522943, 30.06304961, 0.03588973, -247.21948155, -0.00051276, -300.6304961, -0.01522943, -30.06304961, -0.03588973, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 224.09149078, 0.00051276, 272.5057735, 0.01522943, 27.25057735, 0.03588973, -224.09149078, -0.00051276, -272.5057735, -0.01522943, -27.25057735, -0.03588973, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 247.74723681, 0.01025529, 247.74723681, 0.03076588, 173.42306577, -1512.97997441, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 61.9368092, 6.373e-05, 185.81042761, 0.0001912, 619.36809202, 0.00063733, -61.9368092, -6.373e-05, -185.81042761, -0.0001912, -619.36809202, -0.00063733, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 247.74723681, 0.01025529, 247.74723681, 0.03076588, 173.42306577, -1512.97997441, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 61.9368092, 6.373e-05, 185.81042761, 0.0001912, 619.36809202, 0.00063733, -61.9368092, -6.373e-05, -185.81042761, -0.0001912, -619.36809202, -0.00063733, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 16.5, 4.5, 6.225)
    ops.node(123011, 16.5, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.3025, 25088271.5882031, 10453446.49508462, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 263.96767181, 0.0005186, 320.51774737, 0.01475335, 32.05177474, 0.03356495, -263.96767181, -0.0005186, -320.51774737, -0.01475335, -32.05177474, -0.03356495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 239.61039321, 0.0005186, 290.94238303, 0.01475335, 29.0942383, 0.03356495, -239.61039321, -0.0005186, -290.94238303, -0.01475335, -29.0942383, -0.03356495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 245.78125621, 0.01037194, 245.78125621, 0.03111583, 172.04687934, -1615.2696818, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 61.44531405, 6.529e-05, 184.33594215, 0.00019587, 614.45314051, 0.00065289, -61.44531405, -6.529e-05, -184.33594215, -0.00019587, -614.45314051, -0.00065289, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 245.78125621, 0.01037194, 245.78125621, 0.03111583, 172.04687934, -1615.2696818, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 61.44531405, 6.529e-05, 184.33594215, 0.00019587, 614.45314051, 0.00065289, -61.44531405, -6.529e-05, -184.33594215, -0.00019587, -614.45314051, -0.00065289, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.225)
    ops.node(123012, 21.0, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.16, 26375445.95798659, 10989769.14916108, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 118.12925893, 0.00061309, 142.87291682, 0.0152411, 14.28729168, 0.03686398, -118.12925893, -0.00061309, -142.87291682, -0.0152411, -14.28729168, -0.03686398, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 118.12925893, 0.00061309, 142.87291682, 0.0152411, 14.28729168, 0.03686398, -118.12925893, -0.00061309, -142.87291682, -0.0152411, -14.28729168, -0.03686398, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 125.6232933, 0.01226185, 125.6232933, 0.03678554, 87.93630531, -1122.16636405, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 31.40582333, 6.001e-05, 94.21746998, 0.00018004, 314.05823326, 0.00060012, -31.40582333, -6.001e-05, -94.21746998, -0.00018004, -314.05823326, -0.00060012, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 125.6232933, 0.01226185, 125.6232933, 0.03678554, 87.93630531, -1122.16636405, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 31.40582333, 6.001e-05, 94.21746998, 0.00018004, 314.05823326, 0.00060012, -31.40582333, -6.001e-05, -94.21746998, -0.00018004, -314.05823326, -0.00060012, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.225)
    ops.node(123013, 0.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.16, 27143234.15025897, 11309680.89594124, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 117.69015091, 0.00061431, 142.30531893, 0.01542703, 14.23053189, 0.03802272, -117.69015091, -0.00061431, -142.30531893, -0.01542703, -14.23053189, -0.03802272, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 117.69015091, 0.00061431, 142.30531893, 0.01542703, 14.23053189, 0.03802272, -117.69015091, -0.00061431, -142.30531893, -0.01542703, -14.23053189, -0.03802272, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 129.25525615, 0.01228625, 129.25525615, 0.03685875, 90.4786793, -1123.11286674, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 32.31381404, 6e-05, 96.94144211, 0.00018, 323.13814036, 0.00060001, -32.31381404, -6e-05, -96.94144211, -0.00018, -323.13814036, -0.00060001, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 129.25525615, 0.01228625, 129.25525615, 0.03685875, 90.4786793, -1123.11286674, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 32.31381404, 6e-05, 96.94144211, 0.00018, 323.13814036, 0.00060001, -32.31381404, -6e-05, -96.94144211, -0.00018, -323.13814036, -0.00060001, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.5, 9.0, 6.225)
    ops.node(123014, 4.5, 9.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.3025, 27452161.96860532, 11438400.82025222, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 264.14523186, 0.00051334, 320.30468957, 0.01502812, 32.03046896, 0.03608203, -264.14523186, -0.00051334, -320.30468957, -0.01502812, -32.03046896, -0.03608203, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 240.66672926, 0.00051334, 291.83446342, 0.01502812, 29.18344634, 0.03608203, -240.66672926, -0.00051334, -291.83446342, -0.01502812, -29.18344634, -0.03608203, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 270.90723945, 0.01026675, 270.90723945, 0.03080025, 189.63506761, -1608.24287141, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 67.72680986, 6.577e-05, 203.18042959, 0.0001973, 677.26809862, 0.00065767, -67.72680986, -6.577e-05, -203.18042959, -0.0001973, -677.26809862, -0.00065767, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 270.90723945, 0.01026675, 270.90723945, 0.03080025, 189.63506761, -1608.24287141, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 67.72680986, 6.577e-05, 203.18042959, 0.0001973, 677.26809862, 0.00065767, -67.72680986, -6.577e-05, -203.18042959, -0.0001973, -677.26809862, -0.00065767, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.225)
    ops.node(123015, 9.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.3025, 26789130.55022599, 11162137.72926083, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 246.66323708, 0.00050358, 299.69321502, 0.01530785, 29.9693215, 0.0366256, -246.66323708, -0.00050358, -299.69321502, -0.01530785, -29.9693215, -0.0366256, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 223.88913756, 0.00050358, 272.02292582, 0.01530785, 27.20229258, 0.0366256, -223.88913756, -0.00050358, -272.02292582, -0.01530785, -27.20229258, -0.0366256, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 256.80313792, 0.01007167, 256.80313792, 0.03021501, 179.76219654, -1498.98800589, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 64.20078448, 6.389e-05, 192.60235344, 0.00019166, 642.0078448, 0.00063886, -64.20078448, -6.389e-05, -192.60235344, -0.00019166, -642.0078448, -0.00063886, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 256.80313792, 0.01007167, 256.80313792, 0.03021501, 179.76219654, -1498.98800589, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 64.20078448, 6.389e-05, 192.60235344, 0.00019166, 642.0078448, 0.00063886, -64.20078448, -6.389e-05, -192.60235344, -0.00019166, -642.0078448, -0.00063886, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.225)
    ops.node(123016, 12.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.3025, 26687389.72910357, 11119745.72045982, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 250.73811943, 0.00051112, 304.67421359, 0.01537731, 30.46742136, 0.03661228, -250.73811943, -0.00051112, -304.67421359, -0.01537731, -30.46742136, -0.03661228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 227.2993677, 0.00051112, 276.19356906, 0.01537731, 27.61935691, 0.03661228, -227.2993677, -0.00051112, -276.19356906, -0.01537731, -27.61935691, -0.03661228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 256.18053225, 0.01022232, 256.18053225, 0.03066695, 179.32637257, -1509.70945429, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 64.04513306, 6.397e-05, 192.13539919, 0.00019192, 640.45133062, 0.00063974, -64.04513306, -6.397e-05, -192.13539919, -0.00019192, -640.45133062, -0.00063974, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 256.18053225, 0.01022232, 256.18053225, 0.03066695, 179.32637257, -1509.70945429, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 64.04513306, 6.397e-05, 192.13539919, 0.00019192, 640.45133062, 0.00063974, -64.04513306, -6.397e-05, -192.13539919, -0.00019192, -640.45133062, -0.00063974, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 16.5, 9.0, 6.225)
    ops.node(123017, 16.5, 9.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.3025, 27361088.28677649, 11400453.45282354, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 265.78852672, 0.00050853, 322.32919888, 0.01480888, 32.23291989, 0.03578853, -265.78852672, -0.00050853, -322.32919888, -0.01480888, -32.23291989, -0.03578853, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 241.50777055, 0.00050853, 292.88324506, 0.01480888, 29.28832451, 0.03578853, -241.50777055, -0.00050853, -292.88324506, -0.01480888, -29.28832451, -0.03578853, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 269.05094431, 0.01017055, 269.05094431, 0.03051165, 188.33566102, -1589.67182686, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 67.26273608, 6.553e-05, 201.78820823, 0.0001966, 672.62736077, 0.00065534, -67.26273608, -6.553e-05, -201.78820823, -0.0001966, -672.62736077, -0.00065534, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 269.05094431, 0.01017055, 269.05094431, 0.03051165, 188.33566102, -1589.67182686, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 67.26273608, 6.553e-05, 201.78820823, 0.0001966, 672.62736077, 0.00065534, -67.26273608, -6.553e-05, -201.78820823, -0.0001966, -672.62736077, -0.00065534, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.225)
    ops.node(123018, 21.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.16, 26680509.41510691, 11116878.92296121, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 117.88781521, 0.00060832, 142.57554362, 0.01555293, 14.25755436, 0.03759037, -117.88781521, -0.00060832, -142.57554362, -0.01555293, -14.25755436, -0.03759037, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 117.88781521, 0.00060832, 142.57554362, 0.01555293, 14.25755436, 0.03759037, -117.88781521, -0.00060832, -142.57554362, -0.01555293, -14.25755436, -0.03759037, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 128.06623122, 0.01216649, 128.06623122, 0.03649946, 89.64636185, -1145.0096784, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 32.01655781, 6.048e-05, 96.04967342, 0.00018144, 320.16557805, 0.0006048, -32.01655781, -6.048e-05, -96.04967342, -0.00018144, -320.16557805, -0.0006048, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 128.06623122, 0.01216649, 128.06623122, 0.03649946, 89.64636185, -1145.0096784, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 32.01655781, 6.048e-05, 96.04967342, 0.00018144, 320.16557805, 0.0006048, -32.01655781, -6.048e-05, -96.04967342, -0.00018144, -320.16557805, -0.0006048, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.175)
    ops.node(123019, 0.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1225, 27707894.89182694, 11544956.20492789, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 60.77596061, 0.00061142, 73.68304784, 0.01931615, 7.36830478, 0.05743749, -60.77596061, -0.00061142, -73.68304784, -0.01931615, -7.36830478, -0.05743749, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 67.95426119, 0.00061142, 82.38581551, 0.01931615, 8.23858155, 0.05743749, -67.95426119, -0.00061142, -82.38581551, -0.01931615, -8.23858155, -0.05743749, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 112.35457461, 0.01222849, 112.35457461, 0.03668547, 78.64820223, -1203.23002382, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 28.08864365, 6.673e-05, 84.26593096, 0.0002002, 280.88643654, 0.00066733, -28.08864365, -6.673e-05, -84.26593096, -0.0002002, -280.88643654, -0.00066733, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 112.35457461, 0.01222849, 112.35457461, 0.03668547, 78.64820223, -1203.23002382, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 28.08864365, 6.673e-05, 84.26593096, 0.0002002, 280.88643654, 0.00066733, -28.08864365, -6.673e-05, -84.26593096, -0.0002002, -280.88643654, -0.00066733, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 4.5, 13.5, 6.225)
    ops.node(123020, 4.5, 13.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.25, 27552701.81754821, 11480292.42397842, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 178.91578651, 0.00052792, 217.2908958, 0.01579214, 21.72908958, 0.03914887, -178.91578651, -0.00052792, -217.2908958, -0.01579214, -21.72908958, -0.03914887, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 169.13716191, 0.00052792, 205.4148834, 0.01579214, 20.54148834, 0.03914887, -169.13716191, -0.00052792, -205.4148834, -0.01579214, -20.54148834, -0.03914887, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 203.25531181, 0.01055839, 203.25531181, 0.03167516, 142.27871827, -1285.37102106, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 50.81382795, 5.949e-05, 152.44148386, 0.00017846, 508.13827953, 0.00059488, -50.81382795, -5.949e-05, -152.44148386, -0.00017846, -508.13827953, -0.00059488, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 203.25531181, 0.01055839, 203.25531181, 0.03167516, 142.27871827, -1285.37102106, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 50.81382795, 5.949e-05, 152.44148386, 0.00017846, 508.13827953, 0.00059488, -50.81382795, -5.949e-05, -152.44148386, -0.00017846, -508.13827953, -0.00059488, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.225)
    ops.node(123021, 9.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.16, 27406442.89243533, 11419351.20518139, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 111.30080884, 0.00059661, 134.79886094, 0.0160271, 13.47988609, 0.04018934, -111.30080884, -0.00059661, -134.79886094, -0.0160271, -13.47988609, -0.04018934, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 111.30080884, 0.00059661, 134.79886094, 0.0160271, 13.47988609, 0.04018934, -111.30080884, -0.00059661, -134.79886094, -0.0160271, -13.47988609, -0.04018934, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 127.40635427, 0.01193211, 127.40635427, 0.03579633, 89.18444799, -1063.3530404, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 31.85158857, 5.857e-05, 95.5547657, 0.00017572, 318.51588566, 0.00058575, -31.85158857, -5.857e-05, -95.5547657, -0.00017572, -318.51588566, -0.00058575, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 127.40635427, 0.01193211, 127.40635427, 0.03579633, 89.18444799, -1063.3530404, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 31.85158857, 5.857e-05, 95.5547657, 0.00017572, 318.51588566, 0.00058575, -31.85158857, -5.857e-05, -95.5547657, -0.00017572, -318.51588566, -0.00058575, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.225)
    ops.node(123022, 12.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.16, 26232237.80671642, 10930099.08613184, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 110.34077883, 0.00060552, 133.74068836, 0.01562521, 13.37406884, 0.03846898, -110.34077883, -0.00060552, -133.74068836, -0.01562521, -13.37406884, -0.03846898, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 110.34077883, 0.00060552, 133.74068836, 0.01562521, 13.37406884, 0.03846898, -110.34077883, -0.00060552, -133.74068836, -0.01562521, -13.37406884, -0.03846898, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 121.20441622, 0.01211031, 121.20441622, 0.03633093, 84.84309136, -1045.68799045, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 30.30110406, 5.822e-05, 90.90331217, 0.00017465, 303.01104056, 0.00058218, -30.30110406, -5.822e-05, -90.90331217, -0.00017465, -303.01104056, -0.00058218, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 121.20441622, 0.01211031, 121.20441622, 0.03633093, 84.84309136, -1045.68799045, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 30.30110406, 5.822e-05, 90.90331217, 0.00017465, 303.01104056, 0.00058218, -30.30110406, -5.822e-05, -90.90331217, -0.00017465, -303.01104056, -0.00058218, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 16.5, 13.5, 6.225)
    ops.node(123023, 16.5, 13.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.25, 26956901.5582561, 11232042.31594004, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 180.13803196, 0.00052358, 218.93599632, 0.01564739, 21.89359963, 0.03854282, -180.13803196, -0.00052358, -218.93599632, -0.01564739, -21.89359963, -0.03854282, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 169.89999258, 0.00052358, 206.49289739, 0.01564739, 20.64928974, 0.03854282, -169.89999258, -0.00052358, -206.49289739, -0.01564739, -20.64928974, -0.03854282, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 198.08121883, 0.01047157, 198.08121883, 0.03141472, 138.65685318, -1278.36452889, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 49.52030471, 5.925e-05, 148.56091412, 0.00017776, 495.20304707, 0.00059255, -49.52030471, -5.925e-05, -148.56091412, -0.00017776, -495.20304707, -0.00059255, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 198.08121883, 0.01047157, 198.08121883, 0.03141472, 138.65685318, -1278.36452889, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 49.52030471, 5.925e-05, 148.56091412, 0.00017776, 495.20304707, 0.00059255, -49.52030471, -5.925e-05, -148.56091412, -0.00017776, -495.20304707, -0.00059255, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.175)
    ops.node(123024, 21.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.1225, 28020785.52828126, 11675327.30345052, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 61.43092025, 0.00060176, 74.44727116, 0.01907738, 7.44472712, 0.05762772, -61.43092025, -0.00060176, -74.44727116, -0.01907738, -7.44472712, -0.05762772, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 69.11324604, 0.00060176, 83.7573741, 0.01907738, 8.37573741, 0.05762772, -69.11324604, -0.00060176, -83.7573741, -0.01907738, -8.37573741, -0.05762772, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 113.32844775, 0.0120352, 113.32844775, 0.03610561, 79.32991343, -1198.79683979, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 28.33211194, 6.656e-05, 84.99633582, 0.00019968, 283.32111939, 0.0006656, -28.33211194, -6.656e-05, -84.99633582, -0.00019968, -283.32111939, -0.0006656, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 113.32844775, 0.0120352, 113.32844775, 0.03610561, 79.32991343, -1198.79683979, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 28.33211194, 6.656e-05, 84.99633582, 0.00019968, 283.32111939, 0.0006656, -28.33211194, -6.656e-05, -84.99633582, -0.00019968, -283.32111939, -0.0006656, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.95)
    ops.node(124001, 0.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.1225, 26106585.30467727, 10877743.87694887, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 48.21078756, 0.00060618, 59.00128445, 0.02119875, 5.90012844, 0.06642849, -48.21078756, -0.00060618, -59.00128445, -0.02119875, -5.90012844, -0.06642849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 41.96280516, 0.00060618, 51.35488401, 0.02119875, 5.1354884, 0.06642849, -41.96280516, -0.00060618, -51.35488401, -0.02119875, -5.1354884, -0.06642849, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 95.70891737, 0.01212351, 95.70891737, 0.03637054, 66.99624216, -1425.26318667, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 23.92722934, 6.033e-05, 71.78168802, 0.000181, 239.27229342, 0.00060333, -23.92722934, -6.033e-05, -71.78168802, -0.000181, -239.27229342, -0.00060333, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 95.70891737, 0.01212351, 95.70891737, 0.03637054, 66.99624216, -1425.26318667, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 23.92722934, 6.033e-05, 71.78168802, 0.000181, 239.27229342, 0.00060333, -23.92722934, -6.033e-05, -71.78168802, -0.000181, -239.27229342, -0.00060333, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.5, 0.0, 8.975)
    ops.node(124002, 4.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.16, 26842956.52266024, 11184565.2177751, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 83.69982374, 0.0005666, 102.12295236, 0.01752671, 10.21229524, 0.04649076, -83.69982374, -0.0005666, -102.12295236, -0.01752671, -10.21229524, -0.04649076, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 83.69982374, 0.0005666, 102.12295236, 0.01752671, 10.21229524, 0.04649076, -83.69982374, -0.0005666, -102.12295236, -0.01752671, -10.21229524, -0.04649076, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 110.4604115, 0.0113321, 110.4604115, 0.03399629, 77.32228805, -860.90068511, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 27.61510288, 5.185e-05, 82.84530863, 0.00015555, 276.15102875, 0.0005185, -27.61510288, -5.185e-05, -82.84530863, -0.00015555, -276.15102875, -0.0005185, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 110.4604115, 0.0113321, 110.4604115, 0.03399629, 77.32228805, -860.90068511, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 27.61510288, 5.185e-05, 82.84530863, 0.00015555, 276.15102875, 0.0005185, -27.61510288, -5.185e-05, -82.84530863, -0.00015555, -276.15102875, -0.0005185, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.5, 0.0, 8.975)
    ops.node(124005, 16.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.16, 27388082.48513245, 11411701.03547185, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 85.00912203, 0.00056428, 103.62852748, 0.01733295, 10.36285275, 0.04662892, -85.00912203, -0.00056428, -103.62852748, -0.01733295, -10.36285275, -0.04662892, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 85.00912203, 0.00056428, 103.62852748, 0.01733295, 10.36285275, 0.04662892, -85.00912203, -0.00056428, -103.62852748, -0.01733295, -10.36285275, -0.04662892, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 112.18166121, 0.01128555, 112.18166121, 0.03385665, 78.52716285, -838.91529639, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 28.0454153, 5.161e-05, 84.13624591, 0.00015483, 280.45415302, 0.0005161, -28.0454153, -5.161e-05, -84.13624591, -0.00015483, -280.45415302, -0.0005161, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 112.18166121, 0.01128555, 112.18166121, 0.03385665, 78.52716285, -838.91529639, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 28.0454153, 5.161e-05, 84.13624591, 0.00015483, 280.45415302, 0.0005161, -28.0454153, -5.161e-05, -84.13624591, -0.00015483, -280.45415302, -0.0005161, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 21.0, 0.0, 8.95)
    ops.node(124006, 21.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1225, 27951067.20068721, 11646278.00028634, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 49.07754733, 0.00058714, 59.86109907, 0.02101862, 5.98610991, 0.06749523, -49.07754733, -0.00058714, -59.86109907, -0.02101862, -5.98610991, -0.06749523, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 42.4641926, 0.00058714, 51.79462664, 0.02101862, 5.17946266, 0.06749523, -42.4641926, -0.00058714, -51.79462664, -0.02101862, -5.17946266, -0.06749523, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 101.60374631, 0.01174282, 101.60374631, 0.03522846, 71.12262241, -1405.28998056, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 25.40093658, 5.982e-05, 76.20280973, 0.00017947, 254.00936577, 0.00059823, -25.40093658, -5.982e-05, -76.20280973, -0.00017947, -254.00936577, -0.00059823, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 101.60374631, 0.01174282, 101.60374631, 0.03522846, 71.12262241, -1405.28998056, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 25.40093658, 5.982e-05, 76.20280973, 0.00017947, 254.00936577, 0.00059823, -25.40093658, -5.982e-05, -76.20280973, -0.00017947, -254.00936577, -0.00059823, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 8.975)
    ops.node(124007, 0.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.16, 26591556.82590693, 11079815.34412789, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 84.13663276, 0.00056624, 102.692237, 0.01761315, 10.2692237, 0.04639523, -84.13663276, -0.00056624, -102.692237, -0.01761315, -10.2692237, -0.04639523, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 84.13663276, 0.00056624, 102.692237, 0.01761315, 10.2692237, 0.04639523, -84.13663276, -0.00056624, -102.692237, -0.01761315, -10.2692237, -0.04639523, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 108.9800873, 0.01132485, 108.9800873, 0.03397456, 76.28606111, -848.50887981, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 27.24502183, 5.164e-05, 81.73506548, 0.00015492, 272.45021825, 0.00051639, -27.24502183, -5.164e-05, -81.73506548, -0.00015492, -272.45021825, -0.00051639, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 108.9800873, 0.01132485, 108.9800873, 0.03397456, 76.28606111, -848.50887981, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 27.24502183, 5.164e-05, 81.73506548, 0.00015492, 272.45021825, 0.00051639, -27.24502183, -5.164e-05, -81.73506548, -0.00015492, -272.45021825, -0.00051639, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.5, 4.5, 8.975)
    ops.node(124008, 4.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.3025, 25090835.0619092, 10454514.60912883, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 196.55390845, 0.00050127, 240.5167322, 0.01643727, 24.05167322, 0.04013552, -196.55390845, -0.00050127, -240.5167322, -0.01643727, -24.05167322, -0.04013552, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 175.10439666, 0.00050127, 214.26965055, 0.01643727, 21.42696505, 0.04013552, -175.10439666, -0.00050127, -214.26965055, -0.01643727, -21.42696505, -0.04013552, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 215.31653939, 0.01002542, 215.31653939, 0.03007625, 150.72157757, -1209.5294915, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 53.82913485, 5.719e-05, 161.48740454, 0.00017157, 538.29134847, 0.00057191, -53.82913485, -5.719e-05, -161.48740454, -0.00017157, -538.29134847, -0.00057191, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 215.31653939, 0.01002542, 215.31653939, 0.03007625, 150.72157757, -1209.5294915, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 53.82913485, 5.719e-05, 161.48740454, 0.00017157, 538.29134847, 0.00057191, -53.82913485, -5.719e-05, -161.48740454, -0.00017157, -538.29134847, -0.00057191, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.0, 4.5, 8.975)
    ops.node(124009, 9.0, 4.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.3025, 27715689.11378571, 11548203.79741071, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 191.49447303, 0.00048731, 233.59343573, 0.01663725, 23.35934357, 0.04225964, -191.49447303, -0.00048731, -233.59343573, -0.01663725, -23.35934357, -0.04225964, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 169.67789708, 0.00048731, 206.98061056, 0.01663725, 20.69806106, 0.04225964, -169.67789708, -0.00048731, -206.98061056, -0.01663725, -20.69806106, -0.04225964, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 238.70216342, 0.00974615, 238.70216342, 0.02923846, 167.09151439, -1191.73368739, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 59.67554085, 5.74e-05, 179.02662256, 0.00017219, 596.75540854, 0.00057398, -59.67554085, -5.74e-05, -179.02662256, -0.00017219, -596.75540854, -0.00057398, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 238.70216342, 0.00974615, 238.70216342, 0.02923846, 167.09151439, -1191.73368739, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 59.67554085, 5.74e-05, 179.02662256, 0.00017219, 596.75540854, 0.00057398, -59.67554085, -5.74e-05, -179.02662256, -0.00017219, -596.75540854, -0.00057398, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.0, 4.5, 8.975)
    ops.node(124010, 12.0, 4.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.3025, 27581499.36750476, 11492291.40312698, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 188.85870559, 0.00048303, 230.43827824, 0.01682585, 23.04382782, 0.04239779, -188.85870559, -0.00048303, -230.43827824, -0.01682585, -23.04382782, -0.04239779, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 167.42689681, 0.00048303, 204.28799251, 0.01682585, 20.42879925, 0.04239779, -167.42689681, -0.00048303, -204.28799251, -0.01682585, -20.42879925, -0.04239779, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 237.19798403, 0.00966052, 237.19798403, 0.02898155, 166.03858882, -1189.74020496, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 59.29949601, 5.731e-05, 177.89848802, 0.00017194, 592.99496008, 0.00057314, -59.29949601, -5.731e-05, -177.89848802, -0.00017194, -592.99496008, -0.00057314, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 237.19798403, 0.00966052, 237.19798403, 0.02898155, 166.03858882, -1189.74020496, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 59.29949601, 5.731e-05, 177.89848802, 0.00017194, 592.99496008, 0.00057314, -59.29949601, -5.731e-05, -177.89848802, -0.00017194, -592.99496008, -0.00057314, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 16.5, 4.5, 8.975)
    ops.node(124011, 16.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.3025, 27348439.74072105, 11395183.22530044, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 201.60590262, 0.00048783, 245.91125844, 0.01609407, 24.59112584, 0.04099883, -201.60590262, -0.00048783, -245.91125844, -0.01609407, -24.59112584, -0.04099883, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 178.92116791, 0.00048783, 218.24127661, 0.01609407, 21.82412766, 0.04099883, -178.92116791, -0.00048783, -218.24127661, -0.01609407, -21.82412766, -0.04099883, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 238.30793277, 0.00975665, 238.30793277, 0.02926994, 166.81555294, -1196.13034543, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 59.57698319, 5.807e-05, 178.73094957, 0.00017422, 595.76983191, 0.00058073, -59.57698319, -5.807e-05, -178.73094957, -0.00017422, -595.76983191, -0.00058073, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 238.30793277, 0.00975665, 238.30793277, 0.02926994, 166.81555294, -1196.13034543, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 59.57698319, 5.807e-05, 178.73094957, 0.00017422, 595.76983191, 0.00058073, -59.57698319, -5.807e-05, -178.73094957, -0.00017422, -595.76983191, -0.00058073, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 8.975)
    ops.node(124012, 21.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.16, 26522495.82934444, 11051039.92889352, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 82.81953917, 0.00056807, 101.09477204, 0.01777106, 10.1094772, 0.04650754, -82.81953917, -0.00056807, -101.09477204, -0.01777106, -10.1094772, -0.04650754, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 82.81953917, 0.00056807, 101.09477204, 0.01777106, 10.1094772, 0.04650754, -82.81953917, -0.00056807, -101.09477204, -0.01777106, -10.1094772, -0.04650754, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 109.21731894, 0.01136144, 109.21731894, 0.03408433, 76.45212326, -865.10145124, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 27.30432974, 5.189e-05, 81.91298921, 0.00015566, 273.04329736, 0.00051886, -27.30432974, -5.189e-05, -81.91298921, -0.00015566, -273.04329736, -0.00051886, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 109.21731894, 0.01136144, 109.21731894, 0.03408433, 76.45212326, -865.10145124, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 27.30432974, 5.189e-05, 81.91298921, 0.00015566, 273.04329736, 0.00051886, -27.30432974, -5.189e-05, -81.91298921, -0.00015566, -273.04329736, -0.00051886, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.0, 8.95)
    ops.node(124013, 0.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.16, 28278733.56870843, 11782805.65362851, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 83.51423582, 0.00056249, 101.63688569, 0.01752347, 10.16368857, 0.0472938, -83.51423582, -0.00056249, -101.63688569, -0.01752347, -10.16368857, -0.0472938, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 83.51423582, 0.00056249, 101.63688569, 0.01752347, 10.16368857, 0.0472938, -83.51423582, -0.00056249, -101.63688569, -0.01752347, -10.16368857, -0.0472938, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 116.96097057, 0.01124979, 116.96097057, 0.03374937, 81.8726794, -859.73056766, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 29.24024264, 5.211e-05, 87.72072793, 0.00015634, 292.40242642, 0.00052114, -29.24024264, -5.211e-05, -87.72072793, -0.00015634, -292.40242642, -0.00052114, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 116.96097057, 0.01124979, 116.96097057, 0.03374937, 81.8726794, -859.73056766, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 29.24024264, 5.211e-05, 87.72072793, 0.00015634, 292.40242642, 0.00052114, -29.24024264, -5.211e-05, -87.72072793, -0.00015634, -292.40242642, -0.00052114, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.5, 9.0, 8.975)
    ops.node(124014, 4.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.3025, 26899858.36208466, 11208274.31753528, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 193.3849343, 0.00049307, 236.06321815, 0.01659159, 23.60632182, 0.04128655, -193.3849343, -0.00049307, -236.06321815, -0.01659159, -23.60632182, -0.04128655, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 173.04989121, 0.00049307, 211.2404173, 0.01659159, 21.12404173, 0.04128655, -173.04989121, -0.00049307, -211.2404173, -0.01659159, -21.12404173, -0.04128655, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 234.18017701, 0.00986147, 234.18017701, 0.0295844, 163.9261239, -1213.82829518, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 58.54504425, 5.802e-05, 175.63513275, 0.00017406, 585.45044252, 0.00058018, -58.54504425, -5.802e-05, -175.63513275, -0.00017406, -585.45044252, -0.00058018, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 234.18017701, 0.00986147, 234.18017701, 0.0295844, 163.9261239, -1213.82829518, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 58.54504425, 5.802e-05, 175.63513275, 0.00017406, 585.45044252, 0.00058018, -58.54504425, -5.802e-05, -175.63513275, -0.00017406, -585.45044252, -0.00058018, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 9.0, 8.95)
    ops.node(124015, 9.0, 9.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.3025, 27678370.32265912, 11532654.30110797, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 190.94487102, 0.00048669, 232.88812883, 0.01644287, 23.28881288, 0.04188184, -190.94487102, -0.00048669, -232.88812883, -0.01644287, -23.28881288, -0.04188184, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 169.80795656, 0.00048669, 207.10824571, 0.01644287, 20.71082457, 0.04188184, -169.80795656, -0.00048669, -207.10824571, -0.01644287, -20.71082457, -0.04188184, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 238.71453473, 0.00973371, 238.71453473, 0.02920113, 167.10017431, -1171.93964849, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 59.67863368, 5.748e-05, 179.03590105, 0.00017243, 596.78633682, 0.00057478, -59.67863368, -5.748e-05, -179.03590105, -0.00017243, -596.78633682, -0.00057478, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 238.71453473, 0.00973371, 238.71453473, 0.02920113, 167.10017431, -1171.93964849, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 59.67863368, 5.748e-05, 179.03590105, 0.00017243, 596.78633682, 0.00057478, -59.67863368, -5.748e-05, -179.03590105, -0.00017243, -596.78633682, -0.00057478, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.0, 9.0, 8.95)
    ops.node(124016, 12.0, 9.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.3025, 25783029.20447534, 10742928.83519806, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 194.48833853, 0.00049086, 237.95205304, 0.01644536, 23.7952053, 0.04103014, -194.48833853, -0.00049086, -237.95205304, -0.01644536, -23.7952053, -0.04103014, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 171.92770274, 0.00049086, 210.34962893, 0.01644536, 21.03496289, 0.04103014, -171.92770274, -0.00049086, -210.34962893, -0.01644536, -21.03496289, -0.04103014, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 219.35908833, 0.00981729, 219.35908833, 0.02945188, 153.55136183, -1187.67983982, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 54.83977208, 5.67e-05, 164.51931625, 0.0001701, 548.39772084, 0.000567, -54.83977208, -5.67e-05, -164.51931625, -0.0001701, -548.39772084, -0.000567, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 219.35908833, 0.00981729, 219.35908833, 0.02945188, 153.55136183, -1187.67983982, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 54.83977208, 5.67e-05, 164.51931625, 0.0001701, 548.39772084, 0.000567, -54.83977208, -5.67e-05, -164.51931625, -0.0001701, -548.39772084, -0.000567, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 16.5, 9.0, 8.975)
    ops.node(124017, 16.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.3025, 27249964.79293175, 11354151.9970549, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 200.64559447, 0.00049589, 244.78207273, 0.01640683, 24.47820727, 0.04126666, -200.64559447, -0.00049589, -244.78207273, -0.01640683, -24.47820727, -0.04126666, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 178.68373888, 0.00049589, 217.98921667, 0.01640683, 21.79892167, 0.04126666, -178.68373888, -0.00049589, -217.98921667, -0.01640683, -21.79892167, -0.04126666, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 237.73902774, 0.00991775, 237.73902774, 0.02975324, 166.41731942, -1209.49545123, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 59.43475694, 5.814e-05, 178.30427081, 0.00017443, 594.34756935, 0.00058143, -59.43475694, -5.814e-05, -178.30427081, -0.00017443, -594.34756935, -0.00058143, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 237.73902774, 0.00991775, 237.73902774, 0.02975324, 166.41731942, -1209.49545123, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 59.43475694, 5.814e-05, 178.30427081, 0.00017443, 594.34756935, 0.00058143, -59.43475694, -5.814e-05, -178.30427081, -0.00017443, -594.34756935, -0.00058143, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 21.0, 9.0, 8.95)
    ops.node(124018, 21.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.16, 26303059.90471404, 10959608.29363085, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 83.94280415, 0.00057287, 102.49739741, 0.01783548, 10.24973974, 0.04642414, -83.94280415, -0.00057287, -102.49739741, -0.01783548, -10.24973974, -0.04642414, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 83.94280415, 0.00057287, 102.49739741, 0.01783548, 10.24973974, 0.04642414, -83.94280415, -0.00057287, -102.49739741, -0.01783548, -10.24973974, -0.04642414, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 108.13205234, 0.0114574, 108.13205234, 0.03437221, 75.69243663, -861.47691038, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 27.03301308, 5.18e-05, 81.09903925, 0.0001554, 270.33013084, 0.00051799, -27.03301308, -5.18e-05, -81.09903925, -0.0001554, -270.33013084, -0.00051799, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 108.13205234, 0.0114574, 108.13205234, 0.03437221, 75.69243663, -861.47691038, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 27.03301308, 5.18e-05, 81.09903925, 0.0001554, 270.33013084, 0.00051799, -27.03301308, -5.18e-05, -81.09903925, -0.0001554, -270.33013084, -0.00051799, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 13.5, 8.95)
    ops.node(124019, 0.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1225, 27031581.40423301, 11263158.91843042, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 48.08551664, 0.00060201, 58.75612009, 0.02129533, 5.87561201, 0.06719218, -48.08551664, -0.00060201, -58.75612009, -0.02129533, -5.87561201, -0.06719218, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 41.93695891, 0.00060201, 51.24314276, 0.02129533, 5.12431428, 0.06719218, -41.93695891, -0.00060201, -51.24314276, -0.02129533, -5.12431428, -0.06719218, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 98.16162511, 0.01204014, 98.16162511, 0.03612042, 68.71313758, -1389.97262509, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 24.54040628, 5.976e-05, 73.62121883, 0.00017929, 245.40406277, 0.00059762, -24.54040628, -5.976e-05, -73.62121883, -0.00017929, -245.40406277, -0.00059762, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 98.16162511, 0.01204014, 98.16162511, 0.03612042, 68.71313758, -1389.97262509, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 24.54040628, 5.976e-05, 73.62121883, 0.00017929, 245.40406277, 0.00059762, -24.54040628, -5.976e-05, -73.62121883, -0.00017929, -245.40406277, -0.00059762, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 4.5, 13.5, 8.975)
    ops.node(124020, 4.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.25, 26984222.45498868, 11243426.02291195, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 133.53240944, 0.00049671, 163.20506545, 0.01686261, 16.32050655, 0.04397406, -133.53240944, -0.00049671, -163.20506545, -0.01686261, -16.32050655, -0.04397406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 124.03918239, 0.00049671, 151.60231862, 0.01686261, 15.16023186, 0.04397406, -124.03918239, -0.00049671, -151.60231862, -0.01686261, -15.16023186, -0.04397406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 176.23324487, 0.00993413, 176.23324487, 0.0298024, 123.36327141, -1057.86294288, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 44.05831122, 5.267e-05, 132.17493365, 0.000158, 440.58311217, 0.00052666, -44.05831122, -5.267e-05, -132.17493365, -0.000158, -440.58311217, -0.00052666, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 176.23324487, 0.00993413, 176.23324487, 0.0298024, 123.36327141, -1057.86294288, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 44.05831122, 5.267e-05, 132.17493365, 0.000158, 440.58311217, 0.00052666, -44.05831122, -5.267e-05, -132.17493365, -0.000158, -440.58311217, -0.00052666, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 8.95)
    ops.node(124021, 9.0, 13.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.16, 27376815.42528432, 11407006.4272018, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 82.28524294, 0.00056846, 100.37042562, 0.01783283, 10.03704256, 0.04765295, -82.28524294, -0.00056846, -100.37042562, -0.01783283, -10.03704256, -0.04765295, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 82.28524294, 0.00056846, 100.37042562, 0.01783283, 10.03704256, 0.04765295, -82.28524294, -0.00056846, -100.37042562, -0.01783283, -10.03704256, -0.04765295, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 112.00647787, 0.01136921, 112.00647787, 0.03410762, 78.40453451, -875.06378927, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 28.00161947, 5.155e-05, 84.0048584, 0.00015465, 280.01619466, 0.0005155, -28.00161947, -5.155e-05, -84.0048584, -0.00015465, -280.01619466, -0.0005155, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 112.00647787, 0.01136921, 112.00647787, 0.03410762, 78.40453451, -875.06378927, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 28.00161947, 5.155e-05, 84.0048584, 0.00015465, 280.01619466, 0.0005155, -28.00161947, -5.155e-05, -84.0048584, -0.00015465, -280.01619466, -0.0005155, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 8.95)
    ops.node(124022, 12.0, 13.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.16, 27988215.76168216, 11661756.56736757, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 82.47055048, 0.00056749, 100.48141942, 0.01761665, 10.04814194, 0.04774881, -82.47055048, -0.00056749, -100.48141942, -0.01761665, -10.04814194, -0.04774881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 82.47055048, 0.00056749, 100.48141942, 0.01761665, 10.04814194, 0.04774881, -82.47055048, -0.00056749, -100.48141942, -0.01761665, -10.04814194, -0.04774881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 113.93163962, 0.0113497, 113.93163962, 0.03404911, 79.75214773, -847.68305493, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 28.4829099, 5.129e-05, 85.44872971, 0.00015387, 284.82909904, 0.00051291, -28.4829099, -5.129e-05, -85.44872971, -0.00015387, -284.82909904, -0.00051291, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 113.93163962, 0.0113497, 113.93163962, 0.03404911, 79.75214773, -847.68305493, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 28.4829099, 5.129e-05, 85.44872971, 0.00015387, 284.82909904, 0.00051291, -28.4829099, -5.129e-05, -85.44872971, -0.00015387, -284.82909904, -0.00051291, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 16.5, 13.5, 8.975)
    ops.node(124023, 16.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.25, 27822591.95492088, 11592746.6478837, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 132.46068981, 0.00049379, 161.632052, 0.01677053, 16.1632052, 0.04418547, -132.46068981, -0.00049379, -161.632052, -0.01677053, -16.1632052, -0.04418547, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 123.20317362, 0.00049379, 150.33578485, 0.01677053, 15.03357848, 0.04418547, -123.20317362, -0.00049379, -150.33578485, -0.01677053, -15.03357848, -0.04418547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 180.95286076, 0.00987589, 180.95286076, 0.02962768, 126.66700254, -992.87390899, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 45.23821519, 5.245e-05, 135.71464557, 0.00015734, 452.38215191, 0.00052447, -45.23821519, -5.245e-05, -135.71464557, -0.00015734, -452.38215191, -0.00052447, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 180.95286076, 0.00987589, 180.95286076, 0.02962768, 126.66700254, -992.87390899, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 45.23821519, 5.245e-05, 135.71464557, 0.00015734, 452.38215191, 0.00052447, -45.23821519, -5.245e-05, -135.71464557, -0.00015734, -452.38215191, -0.00052447, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 21.0, 13.5, 8.95)
    ops.node(124024, 21.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.1225, 26362405.82806616, 10984335.76169423, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 48.99257857, 0.00057478, 59.93360433, 0.02145354, 5.99336043, 0.06687697, -48.99257857, -0.00057478, -59.93360433, -0.02145354, -5.99336043, -0.06687697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 42.01277744, 0.00057478, 51.39507357, 0.02145354, 5.13950736, 0.06687697, -42.01277744, -0.00057478, -51.39507357, -0.02145354, -5.13950736, -0.06687697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 96.34230618, 0.01149562, 96.34230618, 0.03448686, 67.43961433, -1413.40417809, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 24.08557655, 6.014e-05, 72.25672964, 0.00018043, 240.85576545, 0.00060143, -24.08557655, -6.014e-05, -72.25672964, -0.00018043, -240.85576545, -0.00060143, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 96.34230618, 0.01149562, 96.34230618, 0.03448686, 67.43961433, -1413.40417809, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 24.08557655, 6.014e-05, 72.25672964, 0.00018043, 240.85576545, 0.00060143, -24.08557655, -6.014e-05, -72.25672964, -0.00018043, -240.85576545, -0.00060143, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(124025, 9.0, 0.0, 1.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.25, 26405404.39190637, 11002251.82996099, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 393.87679842, 0.00052795, 474.75149311, 0.04456825, 47.47514931, 0.10916959, -393.87679842, -0.00052795, -474.75149311, -0.04456825, -47.47514931, -0.10916959, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 358.05204099, 0.00052795, 431.57084081, 0.0385254, 43.15708408, 0.08404517, -358.05204099, -0.00052795, -431.57084081, -0.0385254, -43.15708408, -0.08404517, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 462.95230267, 0.01055905, 462.95230267, 0.03167715, 324.06661187, -7879.51318803, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 115.73807567, 7.827e-05, 347.214227, 0.0002348, 1157.38075666, 0.00078265, -115.73807567, -7.827e-05, -347.214227, -0.0002348, -1157.38075666, -0.00078265, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 528.32972879, 0.01055905, 528.32972879, 0.03167715, 369.83081015, -12055.43256949, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 132.0824322, 8.932e-05, 396.24729659, 0.00026795, 1320.82432197, 0.00089317, -132.0824322, -8.932e-05, -396.24729659, -0.00026795, -1320.82432197, -0.00089317, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.875)
    ops.node(121003, 9.0, 0.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.25, 25422002.01762319, 10592500.84067633, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 234.28566255, 0.00051356, 282.69684414, 0.04003853, 28.26968441, 0.10278222, -234.28566255, -0.00051356, -282.69684414, -0.04003853, -28.26968441, -0.10278222, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 222.87468314, 0.00051356, 268.92797826, 0.03461523, 26.89279783, 0.07882606, -222.87468314, -0.00051356, -268.92797826, -0.03461523, -26.89279783, -0.07882606, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 438.95983476, 0.01027112, 438.95983476, 0.03081336, 307.27188433, -7715.83212973, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 109.73995869, 7.708e-05, 329.21987607, 0.00023124, 1097.39958691, 0.0007708, -109.73995869, -7.708e-05, -329.21987607, -0.00023124, -1097.39958691, -0.0007708, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 503.11929962, 0.01027112, 503.11929962, 0.03081336, 352.18350973, -11942.69876101, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 125.7798249, 8.835e-05, 377.33947471, 0.00026504, 1257.79824905, 0.00088346, -125.7798249, -8.835e-05, -377.33947471, -0.00026504, -1257.79824905, -0.00088346, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.0, 0.0, 0.0)
    ops.node(124026, 12.0, 0.0, 1.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.25, 27150015.24173502, 11312506.35072293, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 396.34971935, 0.00052339, 477.7341796, 0.0450804, 47.77341796, 0.11301431, -396.34971935, -0.00052339, -477.7341796, -0.0450804, -47.77341796, -0.11301431, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 360.24541685, 0.00052339, 434.21640101, 0.03896664, 43.4216401, 0.08683464, -360.24541685, -0.00052339, -434.21640101, -0.03896664, -43.4216401, -0.08683464, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 470.94707668, 0.01046779, 470.94707668, 0.03140338, 329.66295368, -7701.54715411, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 117.73676917, 7.743e-05, 353.21030751, 0.0002323, 1177.36769171, 0.00077433, -117.73676917, -7.743e-05, -353.21030751, -0.0002323, -1177.36769171, -0.00077433, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 534.75747531, 0.01046779, 534.75747531, 0.03140338, 374.33023272, -11725.63896638, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 133.68936883, 8.792e-05, 401.06810648, 0.00026377, 1336.89368827, 0.00087925, -133.68936883, -8.792e-05, -401.06810648, -0.00026377, -1336.89368827, -0.00087925, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.875)
    ops.node(121004, 12.0, 0.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.25, 26657018.3080194, 11107090.96167475, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 234.49930939, 0.00050971, 283.04374058, 0.04092667, 28.30437406, 0.10939864, -234.49930939, -0.00050971, -283.04374058, -0.04092667, -28.30437406, -0.10939864, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 223.35289196, 0.00050971, 269.58986862, 0.03538098, 26.95898686, 0.08362811, -223.35289196, -0.00050971, -269.58986862, -0.03538098, -26.95898686, -0.08362811, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 453.0025165, 0.01019418, 453.0025165, 0.03058254, 317.10176155, -7482.04142071, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 113.25062912, 7.586e-05, 339.75188737, 0.00022758, 1132.50629125, 0.0007586, -113.25062912, -7.586e-05, -339.75188737, -0.00022758, -1132.50629125, -0.0007586, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 515.15574545, 0.01019418, 515.15574545, 0.03058254, 360.60902182, -11507.09589517, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 128.78893636, 8.627e-05, 386.36680909, 0.0002588, 1287.88936363, 0.00086268, -128.78893636, -8.627e-05, -386.36680909, -0.0002588, -1287.88936363, -0.00086268, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.475)
    ops.node(124027, 9.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.25, 26711388.59547016, 11129745.24811256, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 205.53437119, 0.00050099, 249.00765019, 0.03766134, 24.90076502, 0.0917652, -205.53437119, -0.00050099, -249.00765019, -0.03766134, -24.90076502, -0.0917652, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 194.94682422, 0.00050099, 236.18069489, 0.03766134, 23.61806949, 0.0917652, -194.94682422, -0.00050099, -236.18069489, -0.03766134, -23.61806949, -0.0917652, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 434.76505879, 0.01001986, 434.76505879, 0.03005958, 304.33554115, -8466.45435713, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 108.6912647, 6.563e-05, 326.07379409, 0.00019688, 1086.91264697, 0.00065626, -108.6912647, -6.563e-05, -326.07379409, -0.00019688, -1086.91264697, -0.00065626, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 434.76505879, 0.01001986, 434.76505879, 0.03005958, 304.33554115, -8466.45435713, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 108.6912647, 6.563e-05, 326.07379409, 0.00019688, 1086.91264697, 0.00065626, -108.6912647, -6.563e-05, -326.07379409, -0.00019688, -1086.91264697, -0.00065626, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.825)
    ops.node(122003, 9.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.25, 27446671.3110828, 11436113.0462845, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 197.45716402, 0.00049981, 239.37056124, 0.0386618, 23.93705612, 0.09665168, -197.45716402, -0.00049981, -239.37056124, -0.0386618, -23.93705612, -0.09665168, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 187.02498802, 0.00049981, 226.72399135, 0.0386618, 22.67239914, 0.09665168, -187.02498802, -0.00049981, -226.72399135, -0.0386618, -22.67239914, -0.09665168, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 440.30320921, 0.00999615, 440.30320921, 0.02998844, 308.21224645, -8763.04880611, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 110.0758023, 6.468e-05, 330.22740691, 0.00019405, 1100.75802303, 0.00064682, -110.0758023, -6.468e-05, -330.22740691, -0.00019405, -1100.75802303, -0.00064682, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 440.30320921, 0.00999615, 440.30320921, 0.02998844, 308.21224645, -8763.04880611, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 110.0758023, 6.468e-05, 330.22740691, 0.00019405, 1100.75802303, 0.00064682, -110.0758023, -6.468e-05, -330.22740691, -0.00019405, -1100.75802303, -0.00064682, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.475)
    ops.node(124028, 12.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.25, 26581815.53040947, 11075756.47100395, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 205.25995917, 0.00050071, 248.69329586, 0.03775171, 24.86932959, 0.09150711, -205.25995917, -0.00050071, -248.69329586, -0.03775171, -24.86932959, -0.09150711, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 194.66741832, 0.00050071, 235.85935637, 0.03775171, 23.58593564, 0.09150711, -194.66741832, -0.00050071, -235.85935637, -0.03775171, -23.58593564, -0.09150711, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 437.0842922, 0.01001414, 437.0842922, 0.03004242, 305.95900454, -8776.10398445, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 109.27107305, 6.63e-05, 327.81321915, 0.00019889, 1092.71073051, 0.00066298, -109.27107305, -6.63e-05, -327.81321915, -0.00019889, -1092.71073051, -0.00066298, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 437.0842922, 0.01001414, 437.0842922, 0.03004242, 305.95900454, -8776.10398445, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 109.27107305, 6.63e-05, 327.81321915, 0.00019889, 1092.71073051, 0.00066298, -109.27107305, -6.63e-05, -327.81321915, -0.00019889, -1092.71073051, -0.00066298, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.825)
    ops.node(122004, 12.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.25, 27660153.34724265, 11525063.89468444, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 196.22419435, 0.00049855, 237.81952479, 0.03882716, 23.78195248, 0.09730111, -196.22419435, -0.00049855, -237.81952479, -0.03882716, -23.78195248, -0.09730111, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 186.00922095, 0.00049855, 225.43919561, 0.03882716, 22.54391956, 0.09730111, -186.00922095, -0.00049855, -225.43919561, -0.03882716, -22.54391956, -0.09730111, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 446.04478938, 0.00997101, 446.04478938, 0.02991302, 312.23135257, -8970.38190846, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 111.51119734, 6.502e-05, 334.53359203, 0.00019506, 1115.11197345, 0.0006502, -111.51119734, -6.502e-05, -334.53359203, -0.00019506, -1115.11197345, -0.0006502, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 446.04478938, 0.00997101, 446.04478938, 0.02991302, 312.23135257, -8970.38190846, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 111.51119734, 6.502e-05, 334.53359203, 0.00019506, 1115.11197345, 0.0006502, -111.51119734, -6.502e-05, -334.53359203, -0.00019506, -1115.11197345, -0.0006502, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.225)
    ops.node(124029, 9.0, 0.0, 7.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.16, 26881539.53745082, 11200641.47393784, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 112.11258027, 0.00052287, 135.81537771, 0.04081351, 13.58153777, 0.10684099, -112.11258027, -0.00052287, -135.81537771, -0.04081351, -13.58153777, -0.10684099, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 112.11258027, 0.00052287, 135.81537771, 0.04081351, 13.58153777, 0.10684099, -112.11258027, -0.00052287, -135.81537771, -0.04081351, -13.58153777, -0.10684099, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 282.21650838, 0.01045743, 282.21650838, 0.03137228, 197.55155586, -6948.91489506, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 70.55412709, 6.614e-05, 211.66238128, 0.00019842, 705.54127094, 0.00066141, -70.55412709, -6.614e-05, -211.66238128, -0.00019842, -705.54127094, -0.00066141, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 282.21650838, 0.01045743, 282.21650838, 0.03137228, 197.55155586, -6948.91489506, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 70.55412709, 6.614e-05, 211.66238128, 0.00019842, 705.54127094, 0.00066141, -70.55412709, -6.614e-05, -211.66238128, -0.00019842, -705.54127094, -0.00066141, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.575)
    ops.node(123003, 9.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.16, 26242168.98445798, 10934237.07685749, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 104.89929902, 0.00051288, 127.40330932, 0.03356588, 12.74033093, 0.0822106, -104.89929902, -0.00051288, -127.40330932, -0.03356588, -12.74033093, -0.0822106, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 104.89929902, 0.00051288, 127.40330932, 0.03356588, 12.74033093, 0.0822106, -104.89929902, -0.00051288, -127.40330932, -0.03356588, -12.74033093, -0.0822106, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 237.68413768, 0.01025759, 237.68413768, 0.03077277, 166.37889637, -4593.41002548, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 59.42103442, 5.706e-05, 178.26310326, 0.00017118, 594.21034419, 0.00057061, -59.42103442, -5.706e-05, -178.26310326, -0.00017118, -594.21034419, -0.00057061, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 237.68413768, 0.01025759, 237.68413768, 0.03077277, 166.37889637, -4593.41002548, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 59.42103442, 5.706e-05, 178.26310326, 0.00017118, 594.21034419, 0.00057061, -59.42103442, -5.706e-05, -178.26310326, -0.00017118, -594.21034419, -0.00057061, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.225)
    ops.node(124030, 12.0, 0.0, 7.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.16, 27188326.80541951, 11328469.50225813, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 110.82492312, 0.00052352, 134.22486138, 0.04116754, 13.42248614, 0.10814849, -110.82492312, -0.00052352, -134.22486138, -0.04116754, -13.42248614, -0.10814849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 110.82492312, 0.00052352, 134.22486138, 0.04116754, 13.42248614, 0.10814849, -110.82492312, -0.00052352, -134.22486138, -0.04116754, -13.42248614, -0.10814849, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 287.21881842, 0.01047048, 287.21881842, 0.03141144, 201.05317289, -7148.93911859, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 71.8047046, 6.655e-05, 215.41411381, 0.00019966, 718.04704604, 0.00066554, -71.8047046, -6.655e-05, -215.41411381, -0.00019966, -718.04704604, -0.00066554, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 287.21881842, 0.01047048, 287.21881842, 0.03141144, 201.05317289, -7148.93911859, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 71.8047046, 6.655e-05, 215.41411381, 0.00019966, 718.04704604, 0.00066554, -71.8047046, -6.655e-05, -215.41411381, -0.00019966, -718.04704604, -0.00066554, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.575)
    ops.node(123004, 12.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.16, 25947705.68861183, 10811544.0369216, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 102.57928313, 0.00051196, 124.60725097, 0.03343954, 12.4607251, 0.08143217, -102.57928313, -0.00051196, -124.60725097, -0.03343954, -12.4607251, -0.08143217, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 102.57928313, 0.00051196, 124.60725097, 0.03343954, 12.4607251, 0.08143217, -102.57928313, -0.00051196, -124.60725097, -0.03343954, -12.4607251, -0.08143217, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 236.11347477, 0.01023913, 236.11347477, 0.03071738, 165.27943234, -4656.62273199, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 59.02836869, 5.733e-05, 177.08510607, 0.00017198, 590.28368692, 0.00057327, -59.02836869, -5.733e-05, -177.08510607, -0.00017198, -590.28368692, -0.00057327, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 236.11347477, 0.01023913, 236.11347477, 0.03071738, 165.27943234, -4656.62273199, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 59.02836869, 5.733e-05, 177.08510607, 0.00017198, 590.28368692, 0.00057327, -59.02836869, -5.733e-05, -177.08510607, -0.00017198, -590.28368692, -0.00057327, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 8.95)
    ops.node(124031, 9.0, 0.0, 9.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.16, 27143555.57800379, 11309814.82416824, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 81.3601039, 0.00049946, 99.28379882, 0.01734404, 9.92837988, 0.04705049, -81.3601039, -0.00049946, -99.28379882, -0.01734404, -9.92837988, -0.04705049, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 81.3601039, 0.00049946, 99.28379882, 0.01734404, 9.92837988, 0.04705049, -81.3601039, -0.00049946, -99.28379882, -0.01734404, -9.92837988, -0.04705049, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 179.9051449, 0.00998926, 179.9051449, 0.02996777, 125.93360143, -1675.70018054, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 44.97628623, 4.176e-05, 134.92885868, 0.00012527, 449.76286225, 0.00041756, -44.97628623, -4.176e-05, -134.92885868, -0.00012527, -449.76286225, -0.00041756, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 179.9051449, 0.00998926, 179.9051449, 0.02996777, 125.93360143, -1675.70018054, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 44.97628623, 4.176e-05, 134.92885868, 0.00012527, 449.76286225, 0.00041756, -44.97628623, -4.176e-05, -134.92885868, -0.00012527, -449.76286225, -0.00041756, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 9.0, 0.0, 10.325)
    ops.node(124003, 9.0, 0.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.16, 26277960.01272812, 10949150.00530338, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 74.80553867, 0.00048875, 91.60288461, 0.01851745, 9.16028846, 0.04960833, -74.80553867, -0.00048875, -91.60288461, -0.01851745, -9.16028846, -0.04960833, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 74.80553867, 0.00048875, 91.60288461, 0.01851745, 9.16028846, 0.04960833, -74.80553867, -0.00048875, -91.60288461, -0.01851745, -9.16028846, -0.04960833, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 164.91943252, 0.00977507, 164.91943252, 0.02932521, 115.44360277, -1765.12037229, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 41.22985813, 3.954e-05, 123.68957439, 0.00011862, 412.29858131, 0.00039539, -41.22985813, -3.954e-05, -123.68957439, -0.00011862, -412.29858131, -0.00039539, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 164.91943252, 0.00977507, 164.91943252, 0.02932521, 115.44360277, -1765.12037229, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 41.22985813, 3.954e-05, 123.68957439, 0.00011862, 412.29858131, 0.00039539, -41.22985813, -3.954e-05, -123.68957439, -0.00011862, -412.29858131, -0.00039539, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 8.95)
    ops.node(124032, 12.0, 0.0, 9.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.16, 26868556.6169318, 11195231.92372158, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 81.02333786, 0.00049536, 98.91830903, 0.0175664, 9.8918309, 0.04711891, -81.02333786, -0.00049536, -98.91830903, -0.0175664, -9.8918309, -0.04711891, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 81.02333786, 0.00049536, 98.91830903, 0.0175664, 9.8918309, 0.04711891, -81.02333786, -0.00049536, -98.91830903, -0.0175664, -9.8918309, -0.04711891, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 177.64618503, 0.00990726, 177.64618503, 0.02972178, 124.35232952, -1674.48667855, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 44.41154626, 4.165e-05, 133.23463877, 0.00012496, 444.11546258, 0.00041654, -44.41154626, -4.165e-05, -133.23463877, -0.00012496, -444.11546258, -0.00041654, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 177.64618503, 0.00990726, 177.64618503, 0.02972178, 124.35232952, -1674.48667855, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 44.41154626, 4.165e-05, 133.23463877, 0.00012496, 444.11546258, 0.00041654, -44.41154626, -4.165e-05, -133.23463877, -0.00012496, -444.11546258, -0.00041654, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 12.0, 0.0, 10.325)
    ops.node(124004, 12.0, 0.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.16, 26349437.50196258, 10978932.29248441, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 73.83670861, 0.00049302, 90.40535235, 0.01839233, 9.04053523, 0.04951263, -73.83670861, -0.00049302, -90.40535235, -0.01839233, -9.04053523, -0.04951263, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 73.83670861, 0.00049302, 90.40535235, 0.01839233, 9.04053523, 0.04951263, -73.83670861, -0.00049302, -90.40535235, -0.01839233, -9.04053523, -0.04951263, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 166.29366234, 0.00986034, 166.29366234, 0.02958103, 116.40556364, -1832.98116381, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 41.57341559, 3.976e-05, 124.72024676, 0.00011928, 415.73415586, 0.0003976, -41.57341559, -3.976e-05, -124.72024676, -0.00011928, -415.73415586, -0.0003976, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 166.29366234, 0.00986034, 166.29366234, 0.02958103, 116.40556364, -1832.98116381, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 41.57341559, 3.976e-05, 124.72024676, 0.00011928, 415.73415586, 0.0003976, -41.57341559, -3.976e-05, -124.72024676, -0.00011928, -415.73415586, -0.0003976, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
