import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 26898838.63976858, 11207849.43323691, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 54.02055861, 0.00110181, 63.36565256, 0.01588972, 6.33656526, 0.03680212, -54.02055861, -0.00110181, -63.36565256, -0.01588972, -6.33656526, -0.03680212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 54.02055861, 0.00110181, 63.36565256, 0.01588972, 6.33656526, 0.03680212, -54.02055861, -0.00110181, -63.36565256, -0.01588972, -6.33656526, -0.03680212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 110.94636784, 0.02203623, 110.94636784, 0.06610868, 77.66245749, -1746.93924931, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 27.73659196, 0.0001473, 83.20977588, 0.00044189, 277.3659196, 0.00147297, -27.73659196, -0.0001473, -83.20977588, -0.00044189, -277.3659196, -0.00147297, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 110.94636784, 0.02203623, 110.94636784, 0.06610868, 77.66245749, -1746.93924931, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 27.73659196, 0.0001473, 83.20977588, 0.00044189, 277.3659196, 0.00147297, -27.73659196, -0.0001473, -83.20977588, -0.00044189, -277.3659196, -0.00147297, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.5, 0.0, 0.0)
    ops.node(121002, 4.5, 0.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.09, 28784066.61961821, 11993361.09150759, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 140.92810059, 0.00148352, 165.22830412, 0.0149759, 16.52283041, 0.03537657, -140.92810059, -0.00148352, -165.22830412, -0.0149759, -16.52283041, -0.03537657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 135.14710958, 0.00148352, 158.45049802, 0.0149759, 15.8450498, 0.03537657, -135.14710958, -0.00148352, -158.45049802, -0.0149759, -15.8450498, -0.03537657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 156.77539777, 0.02967033, 156.77539777, 0.089011, 109.74277844, -2259.86797879, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 39.19384944, 0.00013508, 117.58154832, 0.00040523, 391.93849441, 0.00135076, -39.19384944, -0.00013508, -117.58154832, -0.00040523, -391.93849441, -0.00135076, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 156.77539777, 0.02967033, 156.77539777, 0.089011, 109.74277844, -2259.86797879, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 39.19384944, 0.00013508, 117.58154832, 0.00040523, 391.93849441, 0.00135076, -39.19384944, -0.00013508, -117.58154832, -0.00040523, -391.93849441, -0.00135076, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.5, 0.0, 0.0)
    ops.node(121005, 16.5, 0.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.09, 27172996.85426216, 11322082.02260923, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 101.44775974, 0.00093437, 118.39041397, 0.01290653, 11.8390414, 0.02866083, -101.44775974, -0.00093437, -118.39041397, -0.01290653, -11.8390414, -0.02866083, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 98.33720368, 0.00093437, 114.76036811, 0.01290653, 11.47603681, 0.02866083, -98.33720368, -0.00093437, -114.76036811, -0.01290653, -11.47603681, -0.02866083, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 151.60998456, 0.01868743, 151.60998456, 0.05606228, 106.12698919, -2263.61067628, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 37.90249614, 0.00013837, 113.70748842, 0.00041511, 379.0249614, 0.0013837, -37.90249614, -0.00013837, -113.70748842, -0.00041511, -379.0249614, -0.0013837, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 151.60998456, 0.01868743, 151.60998456, 0.05606228, 106.12698919, -2263.61067628, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 37.90249614, 0.00013837, 113.70748842, 0.00041511, 379.0249614, 0.0013837, -37.90249614, -0.00013837, -113.70748842, -0.00041511, -379.0249614, -0.0013837, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 21.0, 0.0, 0.0)
    ops.node(121006, 21.0, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.0625, 26857474.88709472, 11190614.53628947, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 55.54078274, 0.00109263, 65.13987863, 0.01573948, 6.51398786, 0.03650761, -55.54078274, -0.00109263, -65.13987863, -0.01573948, -6.51398786, -0.03650761, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 55.54078274, 0.00109263, 65.13987863, 0.01573948, 6.51398786, 0.03650761, -55.54078274, -0.00109263, -65.13987863, -0.01573948, -6.51398786, -0.03650761, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 108.28750595, 0.02185253, 108.28750595, 0.0655576, 75.80125417, -1742.3200412, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 27.07187649, 0.00014399, 81.21562946, 0.00043197, 270.71876488, 0.00143988, -27.07187649, -0.00014399, -81.21562946, -0.00043197, -270.71876488, -0.00143988, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 108.28750595, 0.02185253, 108.28750595, 0.0655576, 75.80125417, -1742.3200412, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 27.07187649, 0.00014399, 81.21562946, 0.00043197, 270.71876488, 0.00143988, -27.07187649, -0.00014399, -81.21562946, -0.00043197, -270.71876488, -0.00143988, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.5, 0.0)
    ops.node(121007, 0.0, 4.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.09, 26748857.80889811, 11145357.42037421, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 92.97883144, 0.00083828, 108.34408013, 0.01223937, 10.83440801, 0.02923487, -92.97883144, -0.00083828, -108.34408013, -0.01223937, -10.83440801, -0.02923487, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 92.97883144, 0.00083828, 108.34408013, 0.01223937, 10.83440801, 0.02923487, -92.97883144, -0.00083828, -108.34408013, -0.01223937, -10.83440801, -0.02923487, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 161.82042437, 0.01676563, 161.82042437, 0.05029688, 113.27429706, -2517.45053286, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 40.45510609, 0.00015003, 121.36531827, 0.00045009, 404.55106091, 0.00150031, -40.45510609, -0.00015003, -121.36531827, -0.00045009, -404.55106091, -0.00150031, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 161.82042437, 0.01676563, 161.82042437, 0.05029688, 113.27429706, -2517.45053286, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 40.45510609, 0.00015003, 121.36531827, 0.00045009, 404.55106091, 0.00150031, -40.45510609, -0.00015003, -121.36531827, -0.00045009, -404.55106091, -0.00150031, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
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
    ops.uniaxialMaterial('Hysteretic', 20008, 285.46601537, 0.00122838, 337.29773022, 0.01381912, 33.72977302, 0.03252041, -285.46601537, -0.00122838, -337.29773022, -0.01381912, -33.72977302, -0.03252041, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 270.96704083, 0.00122838, 320.16619463, 0.01381912, 32.01661946, 0.03252041, -270.96704083, -0.00122838, -320.16619463, -0.01381912, -32.01661946, -0.03252041, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 228.38898144, 0.02456751, 228.38898144, 0.07370254, 159.87228701, -3046.55192702, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 57.09724536, 0.00011566, 171.29173608, 0.00034699, 570.9724536, 0.00115663, -57.09724536, -0.00011566, -171.29173608, -0.00034699, -570.9724536, -0.00115663, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 228.38898144, 0.02456751, 228.38898144, 0.07370254, 159.87228701, -3046.55192702, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 57.09724536, 0.00011566, 171.29173608, 0.00034699, 570.9724536, 0.00115663, -57.09724536, -0.00011566, -171.29173608, -0.00034699, -570.9724536, -0.00115663, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.0, 4.5, 0.0)
    ops.node(121009, 9.0, 4.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 28030902.80612075, 11679542.83588365, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 266.93824027, 0.00116126, 317.01436991, 0.01492706, 31.70143699, 0.03748008, -266.93824027, -0.00116126, -317.01436991, -0.01492706, -31.70143699, -0.03748008, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 252.63767494, 0.00116126, 300.03109804, 0.01492706, 30.0031098, 0.03748008, -252.63767494, -0.00116126, -300.03109804, -0.01492706, -30.0031098, -0.03748008, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 224.16474475, 0.02322513, 224.16474475, 0.06967539, 156.91532133, -2892.53948856, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 56.04118619, 0.00011156, 168.12355856, 0.00033468, 560.41186188, 0.00111559, -56.04118619, -0.00011156, -168.12355856, -0.00033468, -560.41186188, -0.00111559, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 224.16474475, 0.02322513, 224.16474475, 0.06967539, 156.91532133, -2892.53948856, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 56.04118619, 0.00011156, 168.12355856, 0.00033468, 560.41186188, 0.00111559, -56.04118619, -0.00011156, -168.12355856, -0.00033468, -560.41186188, -0.00111559, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.0, 4.5, 0.0)
    ops.node(121010, 12.0, 4.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 27678741.63037581, 11532809.01265659, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 265.7619899, 0.001179, 315.48449064, 0.01518479, 31.54844906, 0.03688435, -265.7619899, -0.001179, -315.48449064, -0.01518479, -31.54844906, -0.03688435, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 251.69132875, 0.001179, 298.78129178, 0.01518479, 29.87812918, 0.03688435, -251.69132875, -0.001179, -298.78129178, -0.01518479, -29.87812918, -0.03688435, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 224.18324465, 0.02358007, 224.18324465, 0.07074022, 156.92827126, -2934.88159428, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 56.04581116, 0.00011299, 168.13743349, 0.00033896, 560.45811163, 0.00112988, -56.04581116, -0.00011299, -168.13743349, -0.00033896, -560.45811163, -0.00112988, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 224.18324465, 0.02358007, 224.18324465, 0.07074022, 156.92827126, -2934.88159428, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 56.04581116, 0.00011299, 168.13743349, 0.00033896, 560.45811163, 0.00112988, -56.04581116, -0.00011299, -168.13743349, -0.00033896, -560.45811163, -0.00112988, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
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
    ops.uniaxialMaterial('Hysteretic', 20011, 284.27483718, 0.00122277, 335.30642046, 0.01318682, 33.53064205, 0.03004248, -284.27483718, -0.00122277, -335.30642046, -0.01318682, -33.53064205, -0.03004248, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 269.50481323, 0.00122277, 317.88495639, 0.01318682, 31.78849564, 0.03004248, -269.50481323, -0.00122277, -317.88495639, -0.01318682, -31.78849564, -0.03004248, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 223.29301289, 0.0244554, 223.29301289, 0.07336621, 156.30510902, -3025.43027299, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 55.82325322, 0.00011623, 167.46975967, 0.0003487, 558.23253223, 0.00116232, -55.82325322, -0.00011623, -167.46975967, -0.0003487, -558.23253223, -0.00116232, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 223.29301289, 0.0244554, 223.29301289, 0.07336621, 156.30510902, -3025.43027299, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 55.82325322, 0.00011623, 167.46975967, 0.0003487, 558.23253223, 0.00116232, -55.82325322, -0.00011623, -167.46975967, -0.0003487, -558.23253223, -0.00116232, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 21.0, 4.5, 0.0)
    ops.node(121012, 21.0, 4.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.09, 29006268.07102041, 12085945.02959184, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 129.39148012, 0.00143184, 151.79124986, 0.01513167, 15.17912499, 0.03967862, -129.39148012, -0.00143184, -151.79124986, -0.01513167, -15.17912499, -0.03967862, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 129.39148012, 0.00143184, 151.79124986, 0.01513167, 15.17912499, 0.03967862, -129.39148012, -0.00143184, -151.79124986, -0.01513167, -15.17912499, -0.03967862, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 172.41002882, 0.02863688, 172.41002882, 0.08591065, 120.68702018, -2588.17575686, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 43.10250721, 0.00014741, 129.30752162, 0.00044223, 431.02507206, 0.00147408, -43.10250721, -0.00014741, -129.30752162, -0.00044223, -431.02507206, -0.00147408, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 172.41002882, 0.02863688, 172.41002882, 0.08591065, 120.68702018, -2588.17575686, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 43.10250721, 0.00014741, 129.30752162, 0.00044223, 431.02507206, 0.00147408, -43.10250721, -0.00014741, -129.30752162, -0.00044223, -431.02507206, -0.00147408, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.09, 27654151.24692437, 11522563.01955182, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 101.63160524, 0.00094464, 118.82409692, 0.01335898, 11.88240969, 0.03336581, -101.63160524, -0.00094464, -118.82409692, -0.01335898, -11.88240969, -0.03336581, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 101.63160524, 0.00094464, 118.82409692, 0.01335898, 11.88240969, 0.03336581, -101.63160524, -0.00094464, -118.82409692, -0.01335898, -11.88240969, -0.03336581, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 164.71013482, 0.01889271, 164.71013482, 0.05667814, 115.29709437, -2515.45775545, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 41.1775337, 0.00014771, 123.53260111, 0.00044313, 411.77533704, 0.00147711, -41.1775337, -0.00014771, -123.53260111, -0.00044313, -411.77533704, -0.00147711, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 164.71013482, 0.01889271, 164.71013482, 0.05667814, 115.29709437, -2515.45775545, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 41.1775337, 0.00014771, 123.53260111, 0.00044313, 411.77533704, 0.00147711, -41.1775337, -0.00014771, -123.53260111, -0.00044313, -411.77533704, -0.00147711, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
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
    ops.uniaxialMaterial('Hysteretic', 20014, 283.00236491, 0.0011598, 334.83158134, 0.01467225, 33.48315813, 0.03534669, -283.00236491, -0.0011598, -334.83158134, -0.01467225, -33.48315813, -0.03534669, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 268.58164446, 0.0011598, 317.76984182, 0.01467225, 31.77698418, 0.03534669, -268.58164446, -0.0011598, -317.76984182, -0.01467225, -31.77698418, -0.03534669, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 234.39361195, 0.02319607, 234.39361195, 0.06958822, 164.07552836, -3078.30100044, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 58.59840299, 0.00011529, 175.79520896, 0.00034588, 585.98402987, 0.00115295, -58.59840299, -0.00011529, -175.79520896, -0.00034588, -585.98402987, -0.00115295, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 234.39361195, 0.02319607, 234.39361195, 0.06958822, 164.07552836, -3078.30100044, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 58.59840299, 0.00011529, 175.79520896, 0.00034588, 585.98402987, 0.00115295, -58.59840299, -0.00011529, -175.79520896, -0.00034588, -585.98402987, -0.00115295, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 9.0, 0.0)
    ops.node(121015, 9.0, 9.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.16, 27688561.04495154, 11536900.43539647, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 265.17038754, 0.00118039, 314.7415027, 0.01504375, 31.47415027, 0.03667529, -265.17038754, -0.00118039, -314.7415027, -0.01504375, -31.47415027, -0.03667529, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 251.30612902, 0.00118039, 298.28545117, 0.01504375, 29.82854512, 0.03667529, -251.30612902, -0.00118039, -298.28545117, -0.01504375, -29.82854512, -0.03667529, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 225.55453803, 0.0236078, 225.55453803, 0.0708234, 157.88817662, -2963.89864278, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 56.38863451, 0.00011364, 169.16590352, 0.00034092, 563.88634508, 0.00113638, -56.38863451, -0.00011364, -169.16590352, -0.00034092, -563.88634508, -0.00113638, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 225.55453803, 0.0236078, 225.55453803, 0.0708234, 157.88817662, -2963.89864278, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 56.38863451, 0.00011364, 169.16590352, 0.00034092, 563.88634508, 0.00113638, -56.38863451, -0.00011364, -169.16590352, -0.00034092, -563.88634508, -0.00113638, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.0, 9.0, 0.0)
    ops.node(121016, 12.0, 9.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.16, 27642650.27425501, 11517770.94760625, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 264.64644712, 0.00116284, 314.09996742, 0.01482963, 31.40999674, 0.03634893, -264.64644712, -0.00116284, -314.09996742, -0.01482963, -31.40999674, -0.03634893, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 250.65338969, 0.00116284, 297.49207818, 0.01482963, 29.74920782, 0.03634893, -250.65338969, -0.00116284, -297.49207818, -0.01482963, -29.74920782, -0.03634893, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 223.23557858, 0.02325676, 223.23557858, 0.06977029, 156.264905, -2917.94418434, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 55.80889464, 0.00011266, 167.42668393, 0.00033797, 558.08894645, 0.00112657, -55.80889464, -0.00011266, -167.42668393, -0.00033797, -558.08894645, -0.00112657, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 223.23557858, 0.02325676, 223.23557858, 0.06977029, 156.264905, -2917.94418434, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 55.80889464, 0.00011266, 167.42668393, 0.00033797, 558.08894645, 0.00112657, -55.80889464, -0.00011266, -167.42668393, -0.00033797, -558.08894645, -0.00112657, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
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
    ops.uniaxialMaterial('Hysteretic', 20017, 287.28734869, 0.00122562, 338.59868567, 0.01334035, 33.85986857, 0.02951646, -287.28734869, -0.00122562, -338.59868567, -0.01334035, -33.85986857, -0.02951646, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 271.86493493, 0.00122562, 320.4217313, 0.01334035, 32.04217313, 0.02951646, -271.86493493, -0.00122562, -320.4217313, -0.01334035, -32.04217313, -0.02951646, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 223.96686971, 0.02451236, 223.96686971, 0.07353708, 156.7768088, -3071.22575529, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 55.99171743, 0.00011778, 167.97515228, 0.00035334, 559.91717428, 0.00117781, -55.99171743, -0.00011778, -167.97515228, -0.00035334, -559.91717428, -0.00117781, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 223.96686971, 0.02451236, 223.96686971, 0.07353708, 156.7768088, -3071.22575529, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 55.99171743, 0.00011778, 167.97515228, 0.00035334, 559.91717428, 0.00117781, -55.99171743, -0.00011778, -167.97515228, -0.00035334, -559.91717428, -0.00117781, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.09, 27116138.99827383, 11298391.24928076, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 93.45468061, 0.00088284, 109.05924052, 0.012824, 10.90592405, 0.03103417, -93.45468061, -0.00088284, -109.05924052, -0.012824, -10.90592405, -0.03103417, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 93.45468061, 0.00088284, 109.05924052, 0.012824, 10.90592405, 0.03103417, -93.45468061, -0.00088284, -109.05924052, -0.012824, -10.90592405, -0.03103417, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 165.49758573, 0.01765685, 165.49758573, 0.05297054, 115.84831001, -2573.41362923, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 41.37439643, 0.00015136, 124.12318929, 0.00045408, 413.74396431, 0.00151362, -41.37439643, -0.00015136, -124.12318929, -0.00045408, -413.74396431, -0.00151362, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 165.49758573, 0.01765685, 165.49758573, 0.05297054, 115.84831001, -2573.41362923, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 41.37439643, 0.00015136, 124.12318929, 0.00045408, 413.74396431, 0.00151362, -41.37439643, -0.00015136, -124.12318929, -0.00045408, -413.74396431, -0.00151362, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.0625, 27273317.43466929, 11363882.26444554, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 58.00872919, 0.00115801, 68.12301327, 0.01588792, 6.81230133, 0.0381073, -58.00872919, -0.00115801, -68.12301327, -0.01588792, -6.81230133, -0.0381073, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 58.00872919, 0.00115801, 68.12301327, 0.01588792, 6.81230133, 0.0381073, -58.00872919, -0.00115801, -68.12301327, -0.01588792, -6.81230133, -0.0381073, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 104.29168226, 0.02316029, 104.29168226, 0.06948086, 73.00417759, -1677.70711363, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 26.07292057, 0.00013656, 78.2187617, 0.00040968, 260.72920566, 0.00136561, -26.07292057, -0.00013656, -78.2187617, -0.00040968, -260.72920566, -0.00136561, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 104.29168226, 0.02316029, 104.29168226, 0.06948086, 73.00417759, -1677.70711363, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 26.07292057, 0.00013656, 78.2187617, 0.00040968, 260.72920566, 0.00136561, -26.07292057, -0.00013656, -78.2187617, -0.00040968, -260.72920566, -0.00136561, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 4.5, 13.5, 0.0)
    ops.node(121020, 4.5, 13.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.09, 28008675.97558397, 11670281.65649332, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 109.2305268, 0.00104281, 127.82285272, 0.01400851, 12.78228527, 0.0321682, -109.2305268, -0.00104281, -127.82285272, -0.01400851, -12.78228527, -0.0321682, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 105.72581811, 0.00104281, 123.72160121, 0.01400851, 12.37216012, 0.0321682, -105.72581811, -0.00104281, -123.72160121, -0.01400851, -12.37216012, -0.0321682, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 155.35066681, 0.02085622, 155.35066681, 0.06256866, 108.74546676, -2284.53567707, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 38.8376667, 0.00013755, 116.5130001, 0.00041266, 388.37666702, 0.00137554, -38.8376667, -0.00013755, -116.5130001, -0.00041266, -388.37666702, -0.00137554, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 155.35066681, 0.02085622, 155.35066681, 0.06256866, 108.74546676, -2284.53567707, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 38.8376667, 0.00013755, 116.5130001, 0.00041266, 388.37666702, 0.00137554, -38.8376667, -0.00013755, -116.5130001, -0.00041266, -388.37666702, -0.00137554, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 9.0, 13.5, 0.0)
    ops.node(121021, 9.0, 13.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.09, 28630757.80382459, 11929482.41826025, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 119.39479786, 0.00139653, 140.69306941, 0.01540324, 14.06930694, 0.04262842, -119.39479786, -0.00139653, -140.69306941, -0.01540324, -14.06930694, -0.04262842, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 119.39479786, 0.00139653, 140.69306941, 0.01540324, 14.06930694, 0.04262842, -119.39479786, -0.00139653, -140.69306941, -0.01540324, -14.06930694, -0.04262842, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 162.16677866, 0.02793061, 162.16677866, 0.08379182, 113.51674506, -2389.01180833, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 40.54169466, 0.00014047, 121.62508399, 0.00042141, 405.41694664, 0.00140469, -40.54169466, -0.00014047, -121.62508399, -0.00042141, -405.41694664, -0.00140469, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 162.16677866, 0.02793061, 162.16677866, 0.08379182, 113.51674506, -2389.01180833, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 40.54169466, 0.00014047, 121.62508399, 0.00042141, 405.41694664, 0.00140469, -40.54169466, -0.00014047, -121.62508399, -0.00042141, -405.41694664, -0.00140469, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 12.0, 13.5, 0.0)
    ops.node(121022, 12.0, 13.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.09, 27564980.97164528, 11485408.73818554, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 120.2895697, 0.00139853, 141.43627205, 0.01480313, 14.1436272, 0.03833301, -120.2895697, -0.00139853, -141.43627205, -0.01480313, -14.1436272, -0.03833301, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 120.2895697, 0.00139853, 141.43627205, 0.01480313, 14.1436272, 0.03833301, -120.2895697, -0.00139853, -141.43627205, -0.01480313, -14.1436272, -0.03833301, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 161.35229553, 0.02797065, 161.35229553, 0.08391195, 112.94660687, -2450.54471921, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 40.33807388, 0.00014517, 121.01422165, 0.0004355, 403.38073883, 0.00145167, -40.33807388, -0.00014517, -121.01422165, -0.0004355, -403.38073883, -0.00145167, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 161.35229553, 0.02797065, 161.35229553, 0.08391195, 112.94660687, -2450.54471921, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 40.33807388, 0.00014517, 121.01422165, 0.0004355, 403.38073883, 0.00145167, -40.33807388, -0.00014517, -121.01422165, -0.0004355, -403.38073883, -0.00145167, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 16.5, 13.5, 0.0)
    ops.node(121023, 16.5, 13.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.09, 27638218.3159765, 11515924.29832354, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 107.13740547, 0.00099045, 125.23305932, 0.01382295, 12.52330593, 0.03091322, -107.13740547, -0.00099045, -125.23305932, -0.01382295, -12.52330593, -0.03091322, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 103.60780528, 0.00099045, 121.10730484, 0.01382295, 12.11073048, 0.03091322, -103.60780528, -0.00099045, -121.10730484, -0.01382295, -12.11073048, -0.03091322, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 154.91251452, 0.019809, 154.91251452, 0.05942699, 108.43876017, -2301.44502467, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 38.72812863, 0.000139, 116.18438589, 0.00041701, 387.28128631, 0.00139004, -38.72812863, -0.000139, -116.18438589, -0.00041701, -387.28128631, -0.00139004, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 154.91251452, 0.019809, 154.91251452, 0.05942699, 108.43876017, -2301.44502467, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 38.72812863, 0.000139, 116.18438589, 0.00041701, 387.28128631, 0.00139004, -38.72812863, -0.000139, -116.18438589, -0.00041701, -387.28128631, -0.00139004, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.0625, 26626109.20095151, 11094212.16706313, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 53.89479213, 0.00106453, 63.15844602, 0.01564905, 6.3158446, 0.03561113, -53.89479213, -0.00106453, -63.15844602, -0.01564905, -6.3158446, -0.03561113, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 53.89479213, 0.00106453, 63.15844602, 0.01564905, 6.3158446, 0.03561113, -53.89479213, -0.00106453, -63.15844602, -0.01564905, -6.3158446, -0.03561113, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 111.69811047, 0.02129059, 111.69811047, 0.06387176, 78.18867733, -1743.49920735, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 27.92452762, 0.00014981, 83.77358285, 0.00044944, 279.24527618, 0.00149814, -27.92452762, -0.00014981, -83.77358285, -0.00044944, -279.24527618, -0.00149814, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 111.69811047, 0.02129059, 111.69811047, 0.06387176, 78.18867733, -1743.49920735, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 27.92452762, 0.00014981, 83.77358285, 0.00044944, 279.24527618, 0.00149814, -27.92452762, -0.00014981, -83.77358285, -0.00044944, -279.24527618, -0.00149814, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.3)
    ops.node(122001, 0.0, 0.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 27953853.68422607, 11647439.0350942, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 67.800194, 0.00161595, 80.58924249, 0.02031852, 8.05892425, 0.0537762, -67.800194, -0.00161595, -80.58924249, -0.02031852, -8.05892425, -0.0537762, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 67.800194, 0.00161595, 80.58924249, 0.02031852, 8.05892425, 0.0537762, -67.800194, -0.00161595, -80.58924249, -0.02031852, -8.05892425, -0.0537762, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 107.77734954, 0.03231894, 107.77734954, 0.09695683, 75.44414468, -1816.76875034, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 26.94433739, 0.00012436, 80.83301216, 0.00037309, 269.44337386, 0.00124364, -26.94433739, -0.00012436, -80.83301216, -0.00037309, -269.44337386, -0.00124364, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 107.77734954, 0.03231894, 107.77734954, 0.09695683, 75.44414468, -1816.76875034, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 26.94433739, 0.00012436, 80.83301216, 0.00037309, 269.44337386, 0.00124364, -26.94433739, -0.00012436, -80.83301216, -0.00037309, -269.44337386, -0.00124364, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.5, 0.0, 3.325)
    ops.node(122002, 4.5, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.09, 28628744.68578647, 11928643.6190777, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 118.21437971, 0.00140189, 140.02238538, 0.01702116, 14.00223854, 0.04435248, -118.21437971, -0.00140189, -140.02238538, -0.01702116, -14.00223854, -0.04435248, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 113.44723461, 0.00140189, 134.37580474, 0.01702116, 13.43758047, 0.04435248, -113.44723461, -0.00140189, -134.37580474, -0.01702116, -13.43758047, -0.04435248, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 146.20455028, 0.02803776, 146.20455028, 0.08411329, 102.3431852, -2252.20942042, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 36.55113757, 0.00011439, 109.65341271, 0.00034318, 365.51137571, 0.00114395, -36.55113757, -0.00011439, -109.65341271, -0.00034318, -365.51137571, -0.00114395, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 146.20455028, 0.02803776, 146.20455028, 0.08411329, 102.3431852, -2252.20942042, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 36.55113757, 0.00011439, 109.65341271, 0.00034318, 365.51137571, 0.00114395, -36.55113757, -0.00011439, -109.65341271, -0.00034318, -365.51137571, -0.00114395, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.5, 0.0, 3.325)
    ops.node(122005, 16.5, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.09, 27044049.02779739, 11268353.76158225, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 121.11190552, 0.00140618, 143.08356334, 0.01611603, 14.30835633, 0.03862544, -121.11190552, -0.00140618, -143.08356334, -0.01611603, -14.30835633, -0.03862544, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 115.5525118, 0.00140618, 136.51560571, 0.01611603, 13.65156057, 0.03862544, -115.5525118, -0.00140618, -136.51560571, -0.01611603, -13.65156057, -0.03862544, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 142.48376626, 0.02812351, 142.48376626, 0.08437054, 99.73863638, -2282.8734006, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 35.62094156, 0.00011802, 106.86282469, 0.00035405, 356.20941565, 0.00118016, -35.62094156, -0.00011802, -106.86282469, -0.00035405, -356.20941565, -0.00118016, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 142.48376626, 0.02812351, 142.48376626, 0.08437054, 99.73863638, -2282.8734006, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 35.62094156, 0.00011802, 106.86282469, 0.00035405, 356.20941565, 0.00118016, -35.62094156, -0.00011802, -106.86282469, -0.00035405, -356.20941565, -0.00118016, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 21.0, 0.0, 3.3)
    ops.node(122006, 21.0, 0.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.0625, 25512085.31116219, 10630035.54631758, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 66.63731888, 0.00172368, 78.81480158, 0.01755254, 7.88148016, 0.04204216, -66.63731888, -0.00172368, -78.81480158, -0.01755254, -7.88148016, -0.04204216, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 66.63731888, 0.00172368, 78.81480158, 0.01755254, 7.88148016, 0.04204216, -66.63731888, -0.00172368, -78.81480158, -0.01755254, -7.88148016, -0.04204216, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 93.77760491, 0.03447366, 93.77760491, 0.10342098, 65.64432344, -1774.90451839, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 23.44440123, 0.00011857, 70.33320368, 0.0003557, 234.44401227, 0.00118567, -23.44440123, -0.00011857, -70.33320368, -0.0003557, -234.44401227, -0.00118567, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 93.77760491, 0.03447366, 93.77760491, 0.10342098, 65.64432344, -1774.90451839, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 23.44440123, 0.00011857, 70.33320368, 0.0003557, 234.44401227, 0.00118567, -23.44440123, -0.00011857, -70.33320368, -0.0003557, -234.44401227, -0.00118567, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.3)
    ops.node(122007, 0.0, 4.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.09, 27033776.53268033, 11264073.55528347, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 107.57661567, 0.0013185, 127.10600872, 0.01615621, 12.71060087, 0.04236316, -107.57661567, -0.0013185, -127.10600872, -0.01615621, -12.71060087, -0.04236316, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 107.57661567, 0.0013185, 127.10600872, 0.01615621, 12.71060087, 0.04236316, -107.57661567, -0.0013185, -127.10600872, -0.01615621, -12.71060087, -0.04236316, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 155.8166865, 0.02636997, 155.8166865, 0.07910992, 109.07168055, -2645.54273059, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 38.95417162, 0.00012911, 116.86251487, 0.00038733, 389.54171624, 0.00129109, -38.95417162, -0.00012911, -116.86251487, -0.00038733, -389.54171624, -0.00129109, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 155.8166865, 0.02636997, 155.8166865, 0.07910992, 109.07168055, -2645.54273059, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 38.95417162, 0.00012911, 116.86251487, 0.00038733, 389.54171624, 0.00129109, -38.95417162, -0.00012911, -116.86251487, -0.00038733, -389.54171624, -0.00129109, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
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
    ops.uniaxialMaterial('Hysteretic', 21008, 248.49596519, 0.00108872, 296.28006427, 0.01600349, 29.62800643, 0.04146616, -248.49596519, -0.00108872, -296.28006427, -0.01600349, -29.62800643, -0.04146616, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 234.77961024, 0.00108872, 279.92614672, 0.01600349, 27.99261467, 0.04146616, -234.77961024, -0.00108872, -279.92614672, -0.01600349, -27.99261467, -0.04146616, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 217.34823615, 0.0217744, 217.34823615, 0.06532321, 152.14376531, -3046.72705549, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 54.33705904, 9.753e-05, 163.01117711, 0.00029259, 543.37059038, 0.00097531, -54.33705904, -9.753e-05, -163.01117711, -0.00029259, -543.37059038, -0.00097531, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 217.34823615, 0.0217744, 217.34823615, 0.06532321, 152.14376531, -3046.72705549, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 54.33705904, 9.753e-05, 163.01117711, 0.00029259, 543.37059038, 0.00097531, -54.33705904, -9.753e-05, -163.01117711, -0.00029259, -543.37059038, -0.00097531, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.0, 4.5, 3.325)
    ops.node(122009, 9.0, 4.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 27565033.30054616, 11485430.54189423, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 230.76406493, 0.00108489, 276.01124111, 0.01698071, 27.60112411, 0.04392409, -230.76406493, -0.00108489, -276.01124111, -0.01698071, -27.60112411, -0.04392409, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 217.80525909, 0.00108489, 260.51153112, 0.01698071, 26.05115311, 0.04392409, -217.80525909, -0.00108489, -260.51153112, -0.01698071, -26.05115311, -0.04392409, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 211.07814322, 0.02169783, 211.07814322, 0.0650935, 147.75470025, -2998.47508965, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 52.7695358, 9.648e-05, 158.30860741, 0.00028945, 527.69535804, 0.00096484, -52.7695358, -9.648e-05, -158.30860741, -0.00028945, -527.69535804, -0.00096484, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 211.07814322, 0.02169783, 211.07814322, 0.0650935, 147.75470025, -2998.47508965, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 52.7695358, 9.648e-05, 158.30860741, 0.00028945, 527.69535804, 0.00096484, -52.7695358, -9.648e-05, -158.30860741, -0.00028945, -527.69535804, -0.00096484, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.0, 4.5, 3.325)
    ops.node(122010, 12.0, 4.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 28782150.37533155, 11992562.65638815, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 234.99695806, 0.00106571, 281.11184828, 0.01672972, 28.11118483, 0.04639843, -234.99695806, -0.00106571, -281.11184828, -0.01672972, -28.11118483, -0.04639843, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 221.60737259, 0.00106571, 265.09474257, 0.01672972, 26.50947426, 0.04639843, -221.60737259, -0.00106571, -265.09474257, -0.01672972, -26.50947426, -0.04639843, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 214.81273253, 0.02131414, 214.81273253, 0.06394241, 150.36891277, -2930.19748929, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 53.70318313, 9.404e-05, 161.1095494, 0.00028212, 537.03183132, 0.00094039, -53.70318313, -9.404e-05, -161.1095494, -0.00028212, -537.03183132, -0.00094039, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 214.81273253, 0.02131414, 214.81273253, 0.06394241, 150.36891277, -2930.19748929, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 53.70318313, 9.404e-05, 161.1095494, 0.00028212, 537.03183132, 0.00094039, -53.70318313, -9.404e-05, -161.1095494, -0.00028212, -537.03183132, -0.00094039, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
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
    ops.uniaxialMaterial('Hysteretic', 21011, 249.01530596, 0.00112624, 296.50757239, 0.01548089, 29.65075724, 0.0378148, -249.01530596, -0.00112624, -296.50757239, -0.01548089, -29.65075724, -0.0378148, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 235.01836579, 0.00112624, 279.84113201, 0.01548089, 27.9841132, 0.0378148, -235.01836579, -0.00112624, -279.84113201, -0.01548089, -27.9841132, -0.0378148, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 211.62540155, 0.0225249, 211.62540155, 0.06757469, 148.13778109, -3071.9206199, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 52.90635039, 9.952e-05, 158.71905116, 0.00029857, 529.06350388, 0.00099522, -52.90635039, -9.952e-05, -158.71905116, -0.00029857, -529.06350388, -0.00099522, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 211.62540155, 0.0225249, 211.62540155, 0.06757469, 148.13778109, -3071.9206199, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 52.90635039, 9.952e-05, 158.71905116, 0.00029857, 529.06350388, 0.00099522, -52.90635039, -9.952e-05, -158.71905116, -0.00029857, -529.06350388, -0.00099522, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.3)
    ops.node(122012, 21.0, 4.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.09, 28856030.86104837, 12023346.19210349, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 109.32588862, 0.00126597, 129.53399377, 0.01687148, 12.95339938, 0.04949251, -109.32588862, -0.00126597, -129.53399377, -0.01687148, -12.95339938, -0.04949251, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 109.32588862, 0.00126597, 129.53399377, 0.01687148, 12.95339938, 0.04949251, -109.32588862, -0.00126597, -129.53399377, -0.01687148, -12.95339938, -0.04949251, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 159.67606849, 0.02531948, 159.67606849, 0.07595845, 111.77324794, -2595.76794353, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 39.91901712, 0.00012395, 119.75705137, 0.00037185, 399.19017123, 0.00123951, -39.91901712, -0.00012395, -119.75705137, -0.00037185, -399.19017123, -0.00123951, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 159.67606849, 0.02531948, 159.67606849, 0.07595845, 111.77324794, -2595.76794353, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 39.91901712, 0.00012395, 119.75705137, 0.00037185, 399.19017123, 0.00123951, -39.91901712, -0.00012395, -119.75705137, -0.00037185, -399.19017123, -0.00123951, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.3)
    ops.node(122013, 0.0, 9.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.09, 27955671.33781418, 11648196.39075591, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 108.86005517, 0.00128081, 128.84875287, 0.01687123, 12.88487529, 0.04637454, -108.86005517, -0.00128081, -128.84875287, -0.01687123, -12.88487529, -0.04637454, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 108.86005517, 0.00128081, 128.84875287, 0.01687123, 12.88487529, 0.04637454, -108.86005517, -0.00128081, -128.84875287, -0.01687123, -12.88487529, -0.04637454, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 158.58959309, 0.02561621, 158.58959309, 0.07684864, 111.01271516, -2643.70240515, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 39.64739827, 0.00012707, 118.94219482, 0.00038122, 396.47398273, 0.00127073, -39.64739827, -0.00012707, -118.94219482, -0.00038122, -396.47398273, -0.00127073, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 158.58959309, 0.02561621, 158.58959309, 0.07684864, 111.01271516, -2643.70240515, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 39.64739827, 0.00012707, 118.94219482, 0.00038122, 396.47398273, 0.00127073, -39.64739827, -0.00012707, -118.94219482, -0.00038122, -396.47398273, -0.00127073, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
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
    ops.uniaxialMaterial('Hysteretic', 21014, 250.61162591, 0.00106972, 298.8728167, 0.01606543, 29.88728167, 0.04364022, -250.61162591, -0.00106972, -298.8728167, -0.01606543, -29.88728167, -0.04364022, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 236.72106591, 0.00106972, 282.30730112, 0.01606543, 28.23073011, 0.04364022, -236.72106591, -0.00106972, -282.30730112, -0.01606543, -28.23073011, -0.04364022, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 222.51040827, 0.02139438, 222.51040827, 0.06418313, 155.75728579, -3052.97626485, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 55.62760207, 9.665e-05, 166.8828062, 0.00028995, 556.27602067, 0.00096649, -55.62760207, -9.665e-05, -166.8828062, -0.00028995, -556.27602067, -0.00096649, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 222.51040827, 0.02139438, 222.51040827, 0.06418313, 155.75728579, -3052.97626485, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 55.62760207, 9.665e-05, 166.8828062, 0.00028995, 556.27602067, 0.00096649, -55.62760207, -9.665e-05, -166.8828062, -0.00028995, -556.27602067, -0.00096649, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 9.0, 3.325)
    ops.node(122015, 9.0, 9.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.16, 29029273.30150197, 12095530.54229249, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 237.73196677, 0.00104627, 284.30345054, 0.0170831, 28.43034505, 0.04709511, -237.73196677, -0.00104627, -284.30345054, -0.0170831, -28.43034505, -0.04709511, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 223.87729116, 0.00104627, 267.73465612, 0.0170831, 26.77346561, 0.04709511, -223.87729116, -0.00104627, -267.73465612, -0.0170831, -26.77346561, -0.04709511, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 218.96032854, 0.02092546, 218.96032854, 0.06277639, 153.27222998, -3002.86489753, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 54.74008213, 9.504e-05, 164.2202464, 0.00028512, 547.40082134, 0.00095039, -54.74008213, -9.504e-05, -164.2202464, -0.00028512, -547.40082134, -0.00095039, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 218.96032854, 0.02092546, 218.96032854, 0.06277639, 153.27222998, -3002.86489753, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 54.74008213, 9.504e-05, 164.2202464, 0.00028512, 547.40082134, 0.00095039, -54.74008213, -9.504e-05, -164.2202464, -0.00028512, -547.40082134, -0.00095039, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.0, 9.0, 3.325)
    ops.node(122016, 12.0, 9.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.16, 27433761.60272768, 11430734.00113653, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 236.18088614, 0.00107881, 282.40186118, 0.01614182, 28.24018612, 0.04258523, -236.18088614, -0.00107881, -282.40186118, -0.01614182, -28.24018612, -0.04258523, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 222.28596863, 0.00107881, 265.7876862, 0.01614182, 26.57876862, 0.04258523, -222.28596863, -0.00107881, -265.7876862, -0.01614182, -26.57876862, -0.04258523, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 208.14170666, 0.02157614, 208.14170666, 0.06472842, 145.69919466, -2933.45489685, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 52.03542667, 9.56e-05, 156.10628, 0.00028679, 520.35426665, 0.00095597, -52.03542667, -9.56e-05, -156.10628, -0.00028679, -520.35426665, -0.00095597, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 208.14170666, 0.02157614, 208.14170666, 0.06472842, 145.69919466, -2933.45489685, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 52.03542667, 9.56e-05, 156.10628, 0.00028679, 520.35426665, 0.00095597, -52.03542667, -9.56e-05, -156.10628, -0.00028679, -520.35426665, -0.00095597, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
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
    ops.uniaxialMaterial('Hysteretic', 21017, 251.39014961, 0.00107927, 299.66853923, 0.01600258, 29.96685392, 0.04073084, -251.39014961, -0.00107927, -299.66853923, -0.01600258, -29.96685392, -0.04073084, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 236.91338384, 0.00107927, 282.41157329, 0.01600258, 28.24115733, 0.04073084, -236.91338384, -0.00107927, -282.41157329, -0.01600258, -28.24115733, -0.04073084, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 218.06435548, 0.02158536, 218.06435548, 0.06475607, 152.64504883, -3106.91128078, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 54.51608887, 9.895e-05, 163.54826661, 0.00029684, 545.16088869, 0.00098946, -54.51608887, -9.895e-05, -163.54826661, -0.00029684, -545.16088869, -0.00098946, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 218.06435548, 0.02158536, 218.06435548, 0.06475607, 152.64504883, -3106.91128078, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 54.51608887, 9.895e-05, 163.54826661, 0.00029684, 545.16088869, 0.00098946, -54.51608887, -9.895e-05, -163.54826661, -0.00029684, -545.16088869, -0.00098946, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.3)
    ops.node(122018, 21.0, 9.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.09, 26302450.73382991, 10959354.47242913, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 107.162898, 0.00131891, 126.36924126, 0.01525589, 12.63692413, 0.03879784, -107.162898, -0.00131891, -126.36924126, -0.01525589, -12.63692413, -0.03879784, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 107.162898, 0.00131891, 126.36924126, 0.01525589, 12.63692413, 0.03879784, -107.162898, -0.00131891, -126.36924126, -0.01525589, -12.63692413, -0.03879784, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 153.10774302, 0.02637815, 153.10774302, 0.07913444, 107.17542011, -2632.1286024, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 38.27693575, 0.00013039, 114.83080726, 0.00039117, 382.76935755, 0.00130391, -38.27693575, -0.00013039, -114.83080726, -0.00039117, -382.76935755, -0.00130391, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 153.10774302, 0.02637815, 153.10774302, 0.07913444, 107.17542011, -2632.1286024, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 38.27693575, 0.00013039, 114.83080726, 0.00039117, 382.76935755, 0.00130391, -38.27693575, -0.00013039, -114.83080726, -0.00039117, -382.76935755, -0.00130391, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.3)
    ops.node(122019, 0.0, 13.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.0625, 27163065.73200557, 11317944.05500232, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 66.02834202, 0.00166341, 78.40171314, 0.01967431, 7.84017131, 0.05031547, -66.02834202, -0.00166341, -78.40171314, -0.01967431, -7.84017131, -0.05031547, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 66.02834202, 0.00166341, 78.40171314, 0.01967431, 7.84017131, 0.05031547, -66.02834202, -0.00166341, -78.40171314, -0.01967431, -7.84017131, -0.05031547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 104.0741278, 0.03326829, 104.0741278, 0.09980486, 72.85188946, -1820.48455657, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 26.01853195, 0.00012359, 78.05559585, 0.00037076, 260.18531949, 0.00123587, -26.01853195, -0.00012359, -78.05559585, -0.00037076, -260.18531949, -0.00123587, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 104.0741278, 0.03326829, 104.0741278, 0.09980486, 72.85188946, -1820.48455657, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 26.01853195, 0.00012359, 78.05559585, 0.00037076, 260.18531949, 0.00123587, -26.01853195, -0.00012359, -78.05559585, -0.00037076, -260.18531949, -0.00123587, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 4.5, 13.5, 3.325)
    ops.node(122020, 4.5, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.09, 27530551.63159758, 11471063.17983233, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 119.46535346, 0.00143867, 141.28289823, 0.01644495, 14.12828982, 0.04046077, -119.46535346, -0.00143867, -141.28289823, -0.01644495, -14.12828982, -0.04046077, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 114.40802849, 0.00143867, 135.30197147, 0.01644495, 13.53019715, 0.04046077, -114.40802849, -0.00143867, -135.30197147, -0.01644495, -13.53019715, -0.04046077, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 144.34939898, 0.02877341, 144.34939898, 0.08632022, 101.04457929, -2292.5285238, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 36.08734975, 0.00011745, 108.26204924, 0.00035235, 360.87349746, 0.00117449, -36.08734975, -0.00011745, -108.26204924, -0.00035235, -360.87349746, -0.00117449, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 144.34939898, 0.02877341, 144.34939898, 0.08632022, 101.04457929, -2292.5285238, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 36.08734975, 0.00011745, 108.26204924, 0.00035235, 360.87349746, 0.00117449, -36.08734975, -0.00011745, -108.26204924, -0.00035235, -360.87349746, -0.00117449, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.325)
    ops.node(122021, 9.0, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.09, 27235052.5080971, 11347938.54504046, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 101.71808402, 0.00126604, 120.79534966, 0.01676715, 12.07953497, 0.0476833, -101.71808402, -0.00126604, -120.79534966, -0.01676715, -12.07953497, -0.0476833, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 101.71808402, 0.00126604, 120.79534966, 0.01676715, 12.07953497, 0.0476833, -101.71808402, -0.00126604, -120.79534966, -0.01676715, -12.07953497, -0.0476833, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 149.4968037, 0.02532071, 149.4968037, 0.07596214, 104.64776259, -2499.81147408, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 37.37420092, 0.00012296, 112.12260277, 0.00036887, 373.74200924, 0.00122957, -37.37420092, -0.00012296, -112.12260277, -0.00036887, -373.74200924, -0.00122957, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 149.4968037, 0.02532071, 149.4968037, 0.07596214, 104.64776259, -2499.81147408, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 37.37420092, 0.00012296, 112.12260277, 0.00036887, 373.74200924, 0.00122957, -37.37420092, -0.00012296, -112.12260277, -0.00036887, -373.74200924, -0.00122957, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.325)
    ops.node(122022, 12.0, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.09, 27188516.90614583, 11328548.7108941, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 100.22508873, 0.00127004, 119.01354136, 0.01703435, 11.90135414, 0.04778217, -100.22508873, -0.00127004, -119.01354136, -0.01703435, -11.90135414, -0.04778217, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 100.22508873, 0.00127004, 119.01354136, 0.01703435, 11.90135414, 0.04778217, -100.22508873, -0.00127004, -119.01354136, -0.01703435, -11.90135414, -0.04778217, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 151.9832892, 0.02540079, 151.9832892, 0.07620236, 106.38830244, -2577.11329487, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 37.9958223, 0.00012522, 113.9874669, 0.00037565, 379.95822299, 0.00125216, -37.9958223, -0.00012522, -113.9874669, -0.00037565, -379.95822299, -0.00125216, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 151.9832892, 0.02540079, 151.9832892, 0.07620236, 106.38830244, -2577.11329487, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 37.9958223, 0.00012522, 113.9874669, 0.00037565, 379.95822299, 0.00125216, -37.9958223, -0.00012522, -113.9874669, -0.00037565, -379.95822299, -0.00125216, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 16.5, 13.5, 3.325)
    ops.node(122023, 16.5, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.09, 27249079.16229182, 11353782.98428826, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 118.45467812, 0.00138919, 140.00836554, 0.01633844, 14.00083655, 0.03948498, -118.45467812, -0.00138919, -140.00836554, -0.01633844, -14.00083655, -0.03948498, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 113.29686223, 0.00138919, 133.91204766, 0.01633844, 13.39120477, 0.03948498, -113.29686223, -0.00138919, -133.91204766, -0.01633844, -13.39120477, -0.03948498, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 143.04764893, 0.02778373, 143.04764893, 0.08335118, 100.13335425, -2281.16991321, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 35.76191223, 0.00011759, 107.2857367, 0.00035278, 357.61912232, 0.00117592, -35.76191223, -0.00011759, -107.2857367, -0.00035278, -357.61912232, -0.00117592, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 143.04764893, 0.02778373, 143.04764893, 0.08335118, 100.13335425, -2281.16991321, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 35.76191223, 0.00011759, 107.2857367, 0.00035278, 357.61912232, 0.00117592, -35.76191223, -0.00011759, -107.2857367, -0.00035278, -357.61912232, -0.00117592, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.3)
    ops.node(122024, 21.0, 13.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.0625, 27234416.73607869, 11347673.64003279, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 68.3774794, 0.00159856, 81.20034676, 0.01940736, 8.12003468, 0.05030676, -68.3774794, -0.00159856, -81.20034676, -0.01940736, -8.12003468, -0.05030676, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 68.3774794, 0.00159856, 81.20034676, 0.01940736, 8.12003468, 0.05030676, -68.3774794, -0.00159856, -81.20034676, -0.01940736, -8.12003468, -0.05030676, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 101.84540764, 0.03197121, 101.84540764, 0.09591362, 71.29178535, -1795.92018732, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 25.46135191, 0.00012062, 76.38405573, 0.00036187, 254.6135191, 0.00120624, -25.46135191, -0.00012062, -76.38405573, -0.00036187, -254.6135191, -0.00120624, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 101.84540764, 0.03197121, 101.84540764, 0.09591362, 71.29178535, -1795.92018732, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 25.46135191, 0.00012062, 76.38405573, 0.00036187, 254.6135191, 0.00120624, -25.46135191, -0.00012062, -76.38405573, -0.00036187, -254.6135191, -0.00120624, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.1)
    ops.node(123001, 0.0, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 27394704.3141698, 11414460.13090408, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 55.40764535, 0.00157741, 66.54265342, 0.02328194, 6.65426534, 0.06698368, -55.40764535, -0.00157741, -66.54265342, -0.02328194, -6.65426534, -0.06698368, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 55.40764535, 0.00157741, 66.54265342, 0.02328194, 6.65426534, 0.06698368, -55.40764535, -0.00157741, -66.54265342, -0.02328194, -6.65426534, -0.06698368, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 98.89405817, 0.03154815, 98.89405817, 0.09464445, 69.22584072, -1839.61657385, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 24.72351454, 0.00011644, 74.17054363, 0.00034933, 247.23514543, 0.00116443, -24.72351454, -0.00011644, -74.17054363, -0.00034933, -247.23514543, -0.00116443, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 98.89405817, 0.03154815, 98.89405817, 0.09464445, 69.22584072, -1839.61657385, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 24.72351454, 0.00011644, 74.17054363, 0.00034933, 247.23514543, 0.00116443, -24.72351454, -0.00011644, -74.17054363, -0.00034933, -247.23514543, -0.00116443, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
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
    ops.uniaxialMaterial('Hysteretic', 22002, 69.39078833, 0.00166293, 82.20907931, 0.01841516, 8.22090793, 0.04799077, -69.39078833, -0.00166293, -82.20907931, -0.01841516, -8.22090793, -0.04799077, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 69.39078833, 0.00166293, 82.20907931, 0.01841516, 8.22090793, 0.04799077, -69.39078833, -0.00166293, -82.20907931, -0.01841516, -8.22090793, -0.04799077, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 107.09917858, 0.03325868, 107.09917858, 0.09977604, 74.96942501, -1845.15052452, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 26.77479465, 0.00012512, 80.32438394, 0.00037537, 267.74794646, 0.00125125, -26.77479465, -0.00012512, -80.32438394, -0.00037537, -267.74794646, -0.00125125, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 107.09917858, 0.03325868, 107.09917858, 0.09977604, 74.96942501, -1845.15052452, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 26.77479465, 0.00012512, 80.32438394, 0.00037537, 267.74794646, 0.00125125, -26.77479465, -0.00012512, -80.32438394, -0.00037537, -267.74794646, -0.00125125, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
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
    ops.uniaxialMaterial('Hysteretic', 22005, 71.50551727, 0.00169552, 84.50965637, 0.01689644, 8.45096564, 0.04233519, -71.50551727, -0.00169552, -84.50965637, -0.01689644, -8.45096564, -0.04233519, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 71.50551727, 0.00169552, 84.50965637, 0.01689644, 8.45096564, 0.04233519, -71.50551727, -0.00169552, -84.50965637, -0.01689644, -8.45096564, -0.04233519, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 98.61170286, 0.03391038, 98.61170286, 0.10173113, 69.028192, -1784.97219477, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 24.65292571, 0.00012017, 73.95877714, 0.0003605, 246.52925715, 0.00120166, -24.65292571, -0.00012017, -73.95877714, -0.0003605, -246.52925715, -0.00120166, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 98.61170286, 0.03391038, 98.61170286, 0.10173113, 69.028192, -1784.97219477, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 24.65292571, 0.00012017, 73.95877714, 0.0003605, 246.52925715, 0.00120166, -24.65292571, -0.00012017, -73.95877714, -0.0003605, -246.52925715, -0.00120166, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 21.0, 0.0, 6.1)
    ops.node(123006, 21.0, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 28430402.01538608, 11846000.8397442, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 57.58707625, 0.00149656, 69.14605684, 0.02281725, 6.91460568, 0.06972764, -57.58707625, -0.00149656, -69.14605684, -0.02281725, -6.91460568, -0.06972764, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 57.58707625, 0.00149656, 69.14605684, 0.02281725, 6.91460568, 0.06972764, -57.58707625, -0.00149656, -69.14605684, -0.02281725, -6.91460568, -0.06972764, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 92.02650968, 0.0299311, 92.02650968, 0.08979331, 64.41855677, -1723.99153939, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 23.00662742, 0.00010441, 69.01988226, 0.00031323, 230.0662742, 0.0010441, -23.00662742, -0.00010441, -69.01988226, -0.00031323, -230.0662742, -0.0010441, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 92.02650968, 0.0299311, 92.02650968, 0.08979331, 64.41855677, -1723.99153939, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 23.00662742, 0.00010441, 69.01988226, 0.00031323, 230.0662742, 0.0010441, -23.00662742, -0.00010441, -69.01988226, -0.00031323, -230.0662742, -0.0010441, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.1)
    ops.node(123007, 0.0, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 26924416.23518142, 11218506.76465893, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 70.34438128, 0.00153709, 83.23783619, 0.01817959, 8.32378362, 0.04991365, -70.34438128, -0.00153709, -83.23783619, -0.01817959, -8.32378362, -0.04991365, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 70.34438128, 0.00153709, 83.23783619, 0.01817959, 8.32378362, 0.04991365, -70.34438128, -0.00153709, -83.23783619, -0.01817959, -8.32378362, -0.04991365, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 117.72658009, 0.03074187, 117.72658009, 0.09222562, 82.40860606, -2141.48262697, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 29.43164502, 0.00014104, 88.29493507, 0.00042312, 294.31645022, 0.00141039, -29.43164502, -0.00014104, -88.29493507, -0.00042312, -294.31645022, -0.00141039, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 117.72658009, 0.03074187, 117.72658009, 0.09222562, 82.40860606, -2141.48262697, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 29.43164502, 0.00014104, 88.29493507, 0.00042312, 294.31645022, 0.00141039, -29.43164502, -0.00014104, -88.29493507, -0.00042312, -294.31645022, -0.00141039, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
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
    ops.uniaxialMaterial('Hysteretic', 22008, 155.12106915, 0.00123931, 185.31783156, 0.01686875, 18.53178316, 0.04471712, -155.12106915, -0.00123931, -185.31783156, -0.01686875, -18.53178316, -0.04471712, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 155.12106915, 0.00123931, 185.31783156, 0.01686875, 18.53178316, 0.04471712, -155.12106915, -0.00123931, -185.31783156, -0.01686875, -18.53178316, -0.04471712, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 168.45418873, 0.0247863, 168.45418873, 0.0743589, 117.91793211, -2523.97769323, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 42.11354718, 0.00010237, 126.34064154, 0.0003071, 421.13547181, 0.00102367, -42.11354718, -0.00010237, -126.34064154, -0.0003071, -421.13547181, -0.00102367, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 168.45418873, 0.0247863, 168.45418873, 0.0743589, 117.91793211, -2523.97769323, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 42.11354718, 0.00010237, 126.34064154, 0.0003071, 421.13547181, 0.00102367, -42.11354718, -0.00010237, -126.34064154, -0.0003071, -421.13547181, -0.00102367, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.125)
    ops.node(123009, 9.0, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 27588314.79309262, 11495131.16378859, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 148.63302739, 0.00120969, 178.24320757, 0.01783492, 17.82432076, 0.05016298, -148.63302739, -0.00120969, -178.24320757, -0.01783492, -17.82432076, -0.05016298, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 148.63302739, 0.00120969, 178.24320757, 0.01783492, 17.82432076, 0.05016298, -148.63302739, -0.00120969, -178.24320757, -0.01783492, -17.82432076, -0.05016298, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 166.51890259, 0.02419371, 166.51890259, 0.07258112, 116.56323182, -2486.03724151, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 41.62972565, 9.933e-05, 124.88917695, 0.000298, 416.29725649, 0.00099333, -41.62972565, -9.933e-05, -124.88917695, -0.000298, -416.29725649, -0.00099333, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 166.51890259, 0.02419371, 166.51890259, 0.07258112, 116.56323182, -2486.03724151, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 41.62972565, 9.933e-05, 124.88917695, 0.000298, 416.29725649, 0.00099333, -41.62972565, -9.933e-05, -124.88917695, -0.000298, -416.29725649, -0.00099333, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.125)
    ops.node(123010, 12.0, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 26591859.98664095, 11079941.6611004, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 145.93206747, 0.00122747, 174.92021407, 0.01746164, 17.49202141, 0.04720596, -145.93206747, -0.00122747, -174.92021407, -0.01746164, -17.49202141, -0.04720596, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 145.93206747, 0.00122747, 174.92021407, 0.01746164, 17.49202141, 0.04720596, -145.93206747, -0.00122747, -174.92021407, -0.01746164, -17.49202141, -0.04720596, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 164.60715139, 0.02454931, 164.60715139, 0.07364794, 115.22500597, -2542.74337068, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 41.15178785, 0.00010187, 123.45536354, 0.00030562, 411.51787848, 0.00101872, -41.15178785, -0.00010187, -123.45536354, -0.00030562, -411.51787848, -0.00101872, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 164.60715139, 0.02454931, 164.60715139, 0.07364794, 115.22500597, -2542.74337068, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 41.15178785, 0.00010187, 123.45536354, 0.00030562, 411.51787848, 0.00101872, -41.15178785, -0.00010187, -123.45536354, -0.00030562, -411.51787848, -0.00101872, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
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
    ops.uniaxialMaterial('Hysteretic', 22011, 156.88373572, 0.00125679, 187.06494257, 0.01606439, 18.70649426, 0.04017942, -156.88373572, -0.00125679, -187.06494257, -0.01606439, -18.70649426, -0.04017942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 156.88373572, 0.00125679, 187.06494257, 0.01606439, 18.70649426, 0.04017942, -156.88373572, -0.00125679, -187.06494257, -0.01606439, -18.70649426, -0.04017942, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 165.38431293, 0.02513578, 165.38431293, 0.07540733, 115.76901905, -2582.19503843, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 41.34607823, 0.00010569, 124.0382347, 0.00031708, 413.46078233, 0.00105692, -41.34607823, -0.00010569, -124.0382347, -0.00031708, -413.46078233, -0.00105692, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 165.38431293, 0.02513578, 165.38431293, 0.07540733, 115.76901905, -2582.19503843, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 41.34607823, 0.00010569, 124.0382347, 0.00031708, 413.46078233, 0.00105692, -41.34607823, -0.00010569, -124.0382347, -0.00031708, -413.46078233, -0.00105692, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.1)
    ops.node(123012, 21.0, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 27072999.7789212, 11280416.5745505, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 69.773225, 0.00156736, 82.58828841, 0.01804716, 8.25882884, 0.05041251, -69.773225, -0.00156736, -82.58828841, -0.01804716, -8.25882884, -0.05041251, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 69.773225, 0.00156736, 82.58828841, 0.01804716, 8.25882884, 0.05041251, -69.773225, -0.00156736, -82.58828841, -0.01804716, -8.25882884, -0.05041251, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 116.93140636, 0.03134719, 116.93140636, 0.09404158, 81.85198445, -2107.21381739, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 29.23285159, 0.00013932, 87.69855477, 0.00041795, 292.32851591, 0.00139317, -29.23285159, -0.00013932, -87.69855477, -0.00041795, -292.32851591, -0.00139317, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 116.93140636, 0.03134719, 116.93140636, 0.09404158, 81.85198445, -2107.21381739, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 29.23285159, 0.00013932, 87.69855477, 0.00041795, 292.32851591, 0.00139317, -29.23285159, -0.00013932, -87.69855477, -0.00041795, -292.32851591, -0.00139317, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.1)
    ops.node(123013, 0.0, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 27861093.73542754, 11608789.05642814, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 69.54096195, 0.00157881, 82.42582595, 0.01872647, 8.24258259, 0.05439031, -69.54096195, -0.00157881, -82.42582595, -0.01872647, -8.24258259, -0.05439031, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 69.54096195, 0.00157881, 82.42582595, 0.01872647, 8.24258259, 0.05439031, -69.54096195, -0.00157881, -82.42582595, -0.01872647, -8.24258259, -0.05439031, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 118.90240183, 0.03157614, 118.90240183, 0.09472841, 83.23168128, -2116.5604124, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 29.72560046, 0.00013766, 89.17680137, 0.00041298, 297.25600457, 0.00137658, -29.72560046, -0.00013766, -89.17680137, -0.00041298, -297.25600457, -0.00137658, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 118.90240183, 0.03157614, 118.90240183, 0.09472841, 83.23168128, -2116.5604124, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 29.72560046, 0.00013766, 89.17680137, 0.00041298, 297.25600457, 0.00137658, -29.72560046, -0.00013766, -89.17680137, -0.00041298, -297.25600457, -0.00137658, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
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
    ops.uniaxialMaterial('Hysteretic', 22014, 156.78030573, 0.00121314, 187.41389145, 0.01729531, 18.74138915, 0.0479992, -156.78030573, -0.00121314, -187.41389145, -0.01729531, -18.74138915, -0.0479992, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 156.78030573, 0.00121314, 187.41389145, 0.01729531, 18.74138915, 0.0479992, -156.78030573, -0.00121314, -187.41389145, -0.01729531, -18.74138915, -0.0479992, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 174.44930336, 0.02426271, 174.44930336, 0.07278812, 122.11451235, -2571.29411937, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 43.61232584, 0.00010189, 130.83697752, 0.00030566, 436.12325839, 0.00101885, -43.61232584, -0.00010189, -130.83697752, -0.00030566, -436.12325839, -0.00101885, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 174.44930336, 0.02426271, 174.44930336, 0.07278812, 122.11451235, -2571.29411937, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 43.61232584, 0.00010189, 130.83697752, 0.00030566, 436.12325839, 0.00101885, -43.61232584, -0.00010189, -130.83697752, -0.00030566, -436.12325839, -0.00101885, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.125)
    ops.node(123015, 9.0, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 27497625.12524068, 11457343.80218362, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 146.11206904, 0.00117842, 175.14049519, 0.017777, 17.51404952, 0.04946301, -146.11206904, -0.00117842, -175.14049519, -0.017777, -17.51404952, -0.04946301, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 146.11206904, 0.00117842, 175.14049519, 0.017777, 17.51404952, 0.04946301, -146.11206904, -0.00117842, -175.14049519, -0.017777, -17.51404952, -0.04946301, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 166.40400872, 0.02356847, 166.40400872, 0.0707054, 116.48280611, -2481.46305147, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 41.60100218, 9.959e-05, 124.80300654, 0.00029878, 416.01002181, 0.00099592, -41.60100218, -9.959e-05, -124.80300654, -0.00029878, -416.01002181, -0.00099592, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 166.40400872, 0.02356847, 166.40400872, 0.0707054, 116.48280611, -2481.46305147, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 41.60100218, 9.959e-05, 124.80300654, 0.00029878, 416.01002181, 0.00099592, -41.60100218, -9.959e-05, -124.80300654, -0.00029878, -416.01002181, -0.00099592, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.125)
    ops.node(123016, 12.0, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1225, 27393193.55535775, 11413830.64806573, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 148.64707346, 0.00120982, 178.17343631, 0.01786334, 17.81734363, 0.04928412, -148.64707346, -0.00120982, -178.17343631, -0.01786334, -17.81734363, -0.04928412, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 148.64707346, 0.00120982, 178.17343631, 0.01786334, 17.81734363, 0.04928412, -148.64707346, -0.00120982, -178.17343631, -0.01786334, -17.81734363, -0.04928412, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 167.01354742, 0.02419638, 167.01354742, 0.07258915, 116.9094832, -2511.44960564, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 41.75338686, 0.00010034, 125.26016057, 0.00030101, 417.53386856, 0.00100338, -41.75338686, -0.00010034, -125.26016057, -0.00030101, -417.53386856, -0.00100338, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 167.01354742, 0.02419638, 167.01354742, 0.07258915, 116.9094832, -2511.44960564, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 41.75338686, 0.00010034, 125.26016057, 0.00030101, 417.53386856, 0.00100338, -41.75338686, -0.00010034, -125.26016057, -0.00030101, -417.53386856, -0.00100338, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
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
    ops.uniaxialMaterial('Hysteretic', 22017, 158.58852723, 0.00118597, 189.57148733, 0.01693164, 18.95714873, 0.04740045, -158.58852723, -0.00118597, -189.57148733, -0.01693164, -18.95714873, -0.04740045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 158.58852723, 0.00118597, 189.57148733, 0.01693164, 18.95714873, 0.04740045, -158.58852723, -0.00118597, -189.57148733, -0.01693164, -18.95714873, -0.04740045, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 172.27423927, 0.02371948, 172.27423927, 0.07115843, 120.59196749, -2520.585755, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 43.06855982, 0.00010095, 129.20567946, 0.00030285, 430.68559819, 0.0010095, -43.06855982, -0.00010095, -129.20567946, -0.00030285, -430.68559819, -0.0010095, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 172.27423927, 0.02371948, 172.27423927, 0.07115843, 120.59196749, -2520.585755, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 43.06855982, 0.00010095, 129.20567946, 0.00030285, 430.68559819, 0.0010095, -43.06855982, -0.00010095, -129.20567946, -0.00030285, -430.68559819, -0.0010095, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.1)
    ops.node(123018, 21.0, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 27386131.27707032, 11410888.03211263, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 69.77689948, 0.00154566, 82.64273013, 0.01865604, 8.26427301, 0.05234265, -69.77689948, -0.00154566, -82.64273013, -0.01865604, -8.26427301, -0.05234265, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 69.77689948, 0.00154566, 82.64273013, 0.01865604, 8.26427301, 0.05234265, -69.77689948, -0.00154566, -82.64273013, -0.01865604, -8.26427301, -0.05234265, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 120.35284755, 0.03091319, 120.35284755, 0.09273958, 84.24699329, -2193.11299217, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 30.08821189, 0.00014175, 90.26463566, 0.00042526, 300.88211888, 0.00141754, -30.08821189, -0.00014175, -90.26463566, -0.00042526, -300.88211888, -0.00141754, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 120.35284755, 0.03091319, 120.35284755, 0.09273958, 84.24699329, -2193.11299217, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 30.08821189, 0.00014175, 90.26463566, 0.00042526, 300.88211888, 0.00141754, -30.08821189, -0.00014175, -90.26463566, -0.00042526, -300.88211888, -0.00141754, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.1)
    ops.node(123019, 0.0, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 28440688.11104437, 11850286.71293516, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 56.18731224, 0.0015303, 67.46499266, 0.02374903, 6.74649927, 0.07068984, -56.18731224, -0.0015303, -67.46499266, -0.02374903, -6.74649927, -0.07068984, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 56.18731224, 0.0015303, 67.46499266, 0.02374903, 6.74649927, 0.07068984, -56.18731224, -0.0015303, -67.46499266, -0.02374903, -6.74649927, -0.07068984, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 100.40648761, 0.0306059, 100.40648761, 0.0918177, 70.28454133, -1783.64874749, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 25.1016219, 0.00011388, 75.30486571, 0.00034163, 251.01621904, 0.00113876, -25.1016219, -0.00011388, -75.30486571, -0.00034163, -251.01621904, -0.00113876, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 100.40648761, 0.0306059, 100.40648761, 0.0918177, 70.28454133, -1783.64874749, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 25.1016219, 0.00011388, 75.30486571, 0.00034163, 251.01621904, 0.00113876, -25.1016219, -0.00011388, -75.30486571, -0.00034163, -251.01621904, -0.00113876, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
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
    ops.uniaxialMaterial('Hysteretic', 22020, 69.43037192, 0.00169238, 82.33042215, 0.01880712, 8.23304221, 0.05075014, -69.43037192, -0.00169238, -82.33042215, -0.01880712, -8.23304221, -0.05075014, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 69.43037192, 0.00169238, 82.33042215, 0.01880712, 8.23304221, 0.05075014, -69.43037192, -0.00169238, -82.33042215, -0.01880712, -8.23304221, -0.05075014, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 107.13794266, 0.03384762, 107.13794266, 0.10154285, 74.99655986, -1816.94957695, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 26.78448567, 0.00012219, 80.353457, 0.00036658, 267.84485665, 0.00122195, -26.78448567, -0.00012219, -80.353457, -0.00036658, -267.84485665, -0.00122195, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 107.13794266, 0.03384762, 107.13794266, 0.10154285, 74.99655986, -1816.94957695, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 26.78448567, 0.00012219, 80.353457, 0.00036658, 267.84485665, 0.00122195, -26.78448567, -0.00012219, -80.353457, -0.00036658, -267.84485665, -0.00122195, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.125)
    ops.node(123021, 9.0, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 28131263.58317538, 11721359.82632308, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 66.36825827, 0.00149163, 79.00487745, 0.0201946, 7.90048774, 0.06157244, -66.36825827, -0.00149163, -79.00487745, -0.0201946, -7.90048774, -0.06157244, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 66.36825827, 0.00149163, 79.00487745, 0.0201946, 7.90048774, 0.06157244, -66.36825827, -0.00149163, -79.00487745, -0.0201946, -7.90048774, -0.06157244, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 118.19719033, 0.02983262, 118.19719033, 0.08949786, 82.73803323, -2148.10478908, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 29.54929758, 0.00013553, 88.64789275, 0.00040658, 295.49297582, 0.00135528, -29.54929758, -0.00013553, -88.64789275, -0.00040658, -295.49297582, -0.00135528, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 118.19719033, 0.02983262, 118.19719033, 0.08949786, 82.73803323, -2148.10478908, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 29.54929758, 0.00013553, 88.64789275, 0.00040658, 295.49297582, 0.00135528, -29.54929758, -0.00013553, -88.64789275, -0.00040658, -295.49297582, -0.00135528, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.125)
    ops.node(123022, 12.0, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0625, 26926004.18863422, 11219168.41193092, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 65.59924815, 0.00154261, 77.97961611, 0.01900314, 7.79796161, 0.05538781, -65.59924815, -0.00154261, -77.97961611, -0.01900314, -7.79796161, -0.05538781, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 65.59924815, 0.00154261, 77.97961611, 0.01900314, 7.79796161, 0.05538781, -65.59924815, -0.00154261, -77.97961611, -0.01900314, -7.79796161, -0.05538781, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 113.79455275, 0.03085214, 113.79455275, 0.09255642, 79.65618692, -2084.79630085, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 28.44863819, 0.00013632, 85.34591456, 0.00040896, 284.48638187, 0.0013632, -28.44863819, -0.00013632, -85.34591456, -0.00040896, -284.48638187, -0.0013632, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 113.79455275, 0.03085214, 113.79455275, 0.09255642, 79.65618692, -2084.79630085, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 28.44863819, 0.00013632, 85.34591456, 0.00040896, 284.48638187, 0.0013632, -28.44863819, -0.00013632, -85.34591456, -0.00040896, -284.48638187, -0.0013632, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
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
    ops.uniaxialMaterial('Hysteretic', 22023, 70.4718371, 0.00164231, 83.49789895, 0.01814648, 8.34978989, 0.04793821, -70.4718371, -0.00164231, -83.49789895, -0.01814648, -8.34978989, -0.04793821, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 70.4718371, 0.00164231, 83.49789895, 0.01814648, 8.34978989, 0.04793821, -70.4718371, -0.00164231, -83.49789895, -0.01814648, -8.34978989, -0.04793821, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 103.29851323, 0.0328461, 103.29851323, 0.09853831, 72.30895926, -1802.73821445, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 25.82462831, 0.00012042, 77.47388492, 0.00036126, 258.24628306, 0.0012042, -25.82462831, -0.00012042, -77.47388492, -0.00036126, -258.24628306, -0.0012042, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 103.29851323, 0.0328461, 103.29851323, 0.09853831, 72.30895926, -1802.73821445, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 25.82462831, 0.00012042, 77.47388492, 0.00036126, 258.24628306, 0.0012042, -25.82462831, -0.00012042, -77.47388492, -0.00036126, -258.24628306, -0.0012042, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.1)
    ops.node(123024, 21.0, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 28761853.79465206, 11984105.74777169, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 57.66477058, 0.00147547, 69.22624699, 0.02346428, 6.9226247, 0.07134113, -57.66477058, -0.00147547, -69.22624699, -0.02346428, -6.9226247, -0.07134113, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 57.66477058, 0.00147547, 69.22624699, 0.02346428, 6.9226247, 0.07134113, -57.66477058, -0.00147547, -69.22624699, -0.02346428, -6.9226247, -0.07134113, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 98.41765273, 0.02950946, 98.41765273, 0.08852838, 68.89235691, -1775.54532453, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 24.60441318, 0.00011037, 73.81323954, 0.00033112, 246.04413182, 0.00110374, -24.60441318, -0.00011037, -73.81323954, -0.00033112, -246.04413182, -0.00110374, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 98.41765273, 0.02950946, 98.41765273, 0.08852838, 68.89235691, -1775.54532453, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 24.60441318, 0.00011037, 73.81323954, 0.00033112, 246.04413182, 0.00110374, -24.60441318, -0.00011037, -73.81323954, -0.00033112, -246.04413182, -0.00110374, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.9)
    ops.node(124001, 0.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26797028.54343202, 11165428.55976334, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 42.99162485, 0.0015905, 52.32984002, 0.02758502, 5.232984, 0.09016849, -42.99162485, -0.0015905, -52.32984002, -0.02758502, -5.232984, -0.09016849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 42.99162485, 0.0015905, 52.32984002, 0.02758502, 5.232984, 0.09016849, -42.99162485, -0.0015905, -52.32984002, -0.02758502, -5.232984, -0.09016849, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 87.02258903, 0.03181005, 87.02258903, 0.09543014, 60.91581232, -2499.48476818, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 21.75564726, 0.00010475, 65.26694177, 0.00031425, 217.55647258, 0.0010475, -21.75564726, -0.00010475, -65.26694177, -0.00031425, -217.55647258, -0.0010475, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 87.02258903, 0.03181005, 87.02258903, 0.09543014, 60.91581232, -2499.48476818, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 21.75564726, 0.00010475, 65.26694177, 0.00031425, 217.55647258, 0.0010475, -21.75564726, -0.00010475, -65.26694177, -0.00031425, -217.55647258, -0.0010475, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
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
    ops.uniaxialMaterial('Hysteretic', 23002, 50.67588557, 0.00147893, 61.22007057, 0.02383645, 6.12200706, 0.07653339, -50.67588557, -0.00147893, -61.22007057, -0.02383645, -6.12200706, -0.07653339, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 50.67588557, 0.00147893, 61.22007057, 0.02383645, 6.12200706, 0.07653339, -50.67588557, -0.00147893, -61.22007057, -0.02383645, -6.12200706, -0.07653339, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 90.26322676, 0.02957854, 90.26322676, 0.08873561, 63.18425873, -1916.56774815, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 22.56580669, 0.00010567, 67.69742007, 0.00031701, 225.65806689, 0.00105671, -22.56580669, -0.00010567, -67.69742007, -0.00031701, -225.65806689, -0.00105671, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 90.26322676, 0.02957854, 90.26322676, 0.08873561, 63.18425873, -1916.56774815, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 22.56580669, 0.00010567, 67.69742007, 0.00031701, 225.65806689, 0.00105671, -22.56580669, -0.00010567, -67.69742007, -0.00031701, -225.65806689, -0.00105671, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
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
    ops.uniaxialMaterial('Hysteretic', 23005, 51.71636919, 0.00145379, 62.44787657, 0.02368642, 6.24478766, 0.07784387, -51.71636919, -0.00145379, -62.44787657, -0.02368642, -6.24478766, -0.07784387, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 51.71636919, 0.00145379, 62.44787657, 0.02368642, 6.24478766, 0.07784387, -51.71636919, -0.00145379, -62.44787657, -0.02368642, -6.24478766, -0.07784387, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 88.79265284, 0.02907583, 88.79265284, 0.0872275, 62.15485699, -1849.14644493, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 22.19816321, 0.00010188, 66.59448963, 0.00030564, 221.9816321, 0.0010188, -22.19816321, -0.00010188, -66.59448963, -0.00030564, -221.9816321, -0.0010188, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 88.79265284, 0.02907583, 88.79265284, 0.0872275, 62.15485699, -1849.14644493, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 22.19816321, 0.00010188, 66.59448963, 0.00030564, 221.9816321, 0.0010188, -22.19816321, -0.00010188, -66.59448963, -0.00030564, -221.9816321, -0.0010188, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 21.0, 0.0, 8.9)
    ops.node(124006, 21.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 28690291.62009976, 11954288.17504157, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 44.12925249, 0.00146983, 53.55659347, 0.0275426, 5.35565935, 0.09339037, -44.12925249, -0.00146983, -53.55659347, -0.0275426, -5.35565935, -0.09339037, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 44.12925249, 0.00146983, 53.55659347, 0.0275426, 5.35565935, 0.09339037, -44.12925249, -0.00146983, -53.55659347, -0.0275426, -5.35565935, -0.09339037, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 90.86829738, 0.02939653, 90.86829738, 0.08818959, 63.60780816, -2460.9144541, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 22.71707434, 0.00010216, 68.15122303, 0.00030648, 227.17074344, 0.00102162, -22.71707434, -0.00010216, -68.15122303, -0.00030648, -227.17074344, -0.00102162, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 90.86829738, 0.02939653, 90.86829738, 0.08818959, 63.60780816, -2460.9144541, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 22.71707434, 0.00010216, 68.15122303, 0.00030648, 227.17074344, 0.00102162, -22.71707434, -0.00010216, -68.15122303, -0.00030648, -227.17074344, -0.00102162, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 8.9)
    ops.node(124007, 0.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 27294826.15064396, 11372844.22943499, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 51.73902498, 0.00137964, 62.51478434, 0.02442615, 6.25147843, 0.08511971, -51.73902498, -0.00137964, -62.51478434, -0.02442615, -6.25147843, -0.08511971, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 51.73902498, 0.00137964, 62.51478434, 0.02442615, 6.25147843, 0.08511971, -51.73902498, -0.00137964, -62.51478434, -0.02442615, -6.25147843, -0.08511971, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 104.57791186, 0.02759286, 104.57791186, 0.08277859, 73.2045383, -2379.83785893, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 26.14447797, 0.00012359, 78.4334339, 0.00037076, 261.44477966, 0.00123586, -26.14447797, -0.00012359, -78.4334339, -0.00037076, -261.44477966, -0.00123586, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 104.57791186, 0.02759286, 104.57791186, 0.08277859, 73.2045383, -2379.83785893, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 26.14447797, 0.00012359, 78.4334339, 0.00037076, 261.44477966, 0.00123586, -26.14447797, -0.00012359, -78.4334339, -0.00037076, -261.44477966, -0.00123586, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
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
    ops.uniaxialMaterial('Hysteretic', 23008, 117.43893953, 0.0011991, 142.33923139, 0.02012856, 14.23392314, 0.05938795, -117.43893953, -0.0011991, -142.33923139, -0.02012856, -14.23392314, -0.05938795, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 117.43893953, 0.0011991, 142.33923139, 0.02012856, 14.23392314, 0.05938795, -117.43893953, -0.0011991, -142.33923139, -0.02012856, -14.23392314, -0.05938795, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 146.35295793, 0.02398194, 146.35295793, 0.07194583, 102.44707055, -2554.63790287, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 36.58823948, 9.352e-05, 109.76471845, 0.00028056, 365.88239483, 0.0009352, -36.58823948, -9.352e-05, -109.76471845, -0.00028056, -365.88239483, -0.0009352, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 146.35295793, 0.02398194, 146.35295793, 0.07194583, 102.44707055, -2554.63790287, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 36.58823948, 9.352e-05, 109.76471845, 0.00028056, 365.88239483, 0.0009352, -36.58823948, -9.352e-05, -109.76471845, -0.00028056, -365.88239483, -0.0009352, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
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
    ops.node(173011, 16.5, 4.5, 8.925)
    ops.node(124011, 16.5, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 28071726.41682608, 11696552.67367753, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 121.93154128, 0.00110407, 147.55037086, 0.02011026, 14.75503709, 0.0639739, -121.93154128, -0.00110407, -147.55037086, -0.02011026, -14.75503709, -0.0639739, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 121.93154128, 0.00110407, 147.55037086, 0.02011026, 14.75503709, 0.0639739, -121.93154128, -0.00110407, -147.55037086, -0.02011026, -14.75503709, -0.0639739, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 153.56459318, 0.02208132, 153.56459318, 0.06624397, 107.49521523, -2513.1055602, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 38.3911483, 9.003e-05, 115.17344489, 0.00027008, 383.91148295, 0.00090028, -38.3911483, -9.003e-05, -115.17344489, -0.00027008, -383.91148295, -0.00090028, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 153.56459318, 0.02208132, 153.56459318, 0.06624397, 107.49521523, -2513.1055602, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 38.3911483, 9.003e-05, 115.17344489, 0.00027008, 383.91148295, 0.00090028, -38.3911483, -9.003e-05, -115.17344489, -0.00027008, -383.91148295, -0.00090028, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 8.9)
    ops.node(124012, 21.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 27223938.69161687, 11343307.78817369, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 50.74599058, 0.00139945, 61.31737767, 0.02470386, 6.13173777, 0.08516789, -50.74599058, -0.00139945, -61.31737767, -0.02470386, -6.13173777, -0.08516789, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 50.74599058, 0.00139945, 61.31737767, 0.02470386, 6.13173777, 0.08516789, -50.74599058, -0.00139945, -61.31737767, -0.02470386, -6.13173777, -0.08516789, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 105.80314909, 0.02798904, 105.80314909, 0.08396711, 74.06220436, -2448.8353302, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 26.45078727, 0.00012536, 79.35236181, 0.00037608, 264.50787272, 0.0012536, -26.45078727, -0.00012536, -79.35236181, -0.00037608, -264.50787272, -0.0012536, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 105.80314909, 0.02798904, 105.80314909, 0.08396711, 74.06220436, -2448.8353302, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 26.45078727, 0.00012536, 79.35236181, 0.00037608, 264.50787272, 0.0012536, -26.45078727, -0.00012536, -79.35236181, -0.00037608, -264.50787272, -0.0012536, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.0, 8.9)
    ops.node(124013, 0.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 29026623.81039253, 12094426.58766356, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 51.28802248, 0.00136583, 61.86472086, 0.02484303, 6.18647209, 0.09063663, -51.28802248, -0.00136583, -61.86472086, -0.02484303, -6.18647209, -0.09063663, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 51.28802248, 0.00136583, 61.86472086, 0.02484303, 6.18647209, 0.09063663, -51.28802248, -0.00136583, -61.86472086, -0.02484303, -6.18647209, -0.09063663, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 108.76033738, 0.02731651, 108.76033738, 0.08194952, 76.13223617, -2426.46666425, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 27.19008435, 0.00012086, 81.57025304, 0.00036258, 271.90084346, 0.00120861, -27.19008435, -0.00012086, -81.57025304, -0.00036258, -271.90084346, -0.00120861, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 108.76033738, 0.02731651, 108.76033738, 0.08194952, 76.13223617, -2426.46666425, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 27.19008435, 0.00012086, 81.57025304, 0.00036258, 271.90084346, 0.00120861, -27.19008435, -0.00012086, -81.57025304, -0.00036258, -271.90084346, -0.00120861, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
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
    ops.uniaxialMaterial('Hysteretic', 23014, 115.14531185, 0.0011499, 139.40882795, 0.0208237, 13.94088279, 0.06386642, -115.14531185, -0.0011499, -139.40882795, -0.0208237, -13.94088279, -0.06386642, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 115.14531185, 0.0011499, 139.40882795, 0.0208237, 13.94088279, 0.06386642, -115.14531185, -0.0011499, -139.40882795, -0.0208237, -13.94088279, -0.06386642, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 153.24885752, 0.02299793, 153.24885752, 0.06899378, 107.27420026, -2567.98558729, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 38.31221438, 9.134e-05, 114.93664314, 0.00027402, 383.1221438, 0.00091341, -38.31221438, -9.134e-05, -114.93664314, -0.00027402, -383.1221438, -0.00091341, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 153.24885752, 0.02299793, 153.24885752, 0.06899378, 107.27420026, -2567.98558729, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 38.31221438, 9.134e-05, 114.93664314, 0.00027402, 383.1221438, 0.00091341, -38.31221438, -9.134e-05, -114.93664314, -0.00027402, -383.1221438, -0.00091341, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
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
    ops.node(173017, 16.5, 9.0, 8.925)
    ops.node(124017, 16.5, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.1225, 27970647.0931257, 11654436.28880238, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 120.41551469, 0.00114703, 145.73311561, 0.02061025, 14.57331156, 0.06429736, -120.41551469, -0.00114703, -145.73311561, -0.02061025, -14.57331156, -0.06429736, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 120.41551469, 0.00114703, 145.73311561, 0.02061025, 14.57331156, 0.06429736, -120.41551469, -0.00114703, -145.73311561, -0.02061025, -14.57331156, -0.06429736, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 154.21835023, 0.02294053, 154.21835023, 0.0688216, 107.95284516, -2554.53225297, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 38.55458756, 9.074e-05, 115.66376267, 0.00027221, 385.54587557, 0.00090738, -38.55458756, -9.074e-05, -115.66376267, -0.00027221, -385.54587557, -0.00090738, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 154.21835023, 0.02294053, 154.21835023, 0.0688216, 107.95284516, -2554.53225297, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 38.55458756, 9.074e-05, 115.66376267, 0.00027221, 385.54587557, 0.00090738, -38.55458756, -9.074e-05, -115.66376267, -0.00027221, -385.54587557, -0.00090738, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 21.0, 9.0, 8.9)
    ops.node(124018, 21.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 26998699.32510646, 11249458.05212769, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 51.49533605, 0.00141351, 62.22970306, 0.02474152, 6.22297031, 0.0844648, -51.49533605, -0.00141351, -62.22970306, -0.02474152, -6.22297031, -0.0844648, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 51.49533605, 0.00141351, 62.22970306, 0.02474152, 6.22297031, 0.0844648, -51.49533605, -0.00141351, -62.22970306, -0.02474152, -6.22297031, -0.0844648, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 105.09161031, 0.02827014, 105.09161031, 0.08481043, 73.56412722, -2433.73621552, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 26.27290258, 0.00012556, 78.81870773, 0.00037667, 262.72902578, 0.00125555, -26.27290258, -0.00012556, -78.81870773, -0.00037667, -262.72902578, -0.00125555, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 105.09161031, 0.02827014, 105.09161031, 0.08481043, 73.56412722, -2433.73621552, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 26.27290258, 0.00012556, 78.81870773, 0.00037667, 262.72902578, 0.00125555, -26.27290258, -0.00012556, -78.81870773, -0.00037667, -262.72902578, -0.00125555, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 13.5, 8.9)
    ops.node(124019, 0.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 27746488.0990606, 11561036.70794192, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 42.87370061, 0.00155987, 52.11737669, 0.02787056, 5.21173767, 0.09219091, -42.87370061, -0.00155987, -52.11737669, -0.02787056, -5.21173767, -0.09219091, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 42.87370061, 0.00155987, 52.11737669, 0.02787056, 5.21173767, 0.09219091, -42.87370061, -0.00155987, -52.11737669, -0.02787056, -5.21173767, -0.09219091, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 89.78292759, 0.03119733, 89.78292759, 0.093592, 62.84804931, -2431.35403499, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 22.4457319, 0.00010437, 67.33719569, 0.00031312, 224.45731898, 0.00104375, -22.4457319, -0.00010437, -67.33719569, -0.00031312, -224.45731898, -0.00104375, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 89.78292759, 0.03119733, 89.78292759, 0.093592, 62.84804931, -2431.35403499, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 22.4457319, 0.00010437, 67.33719569, 0.00031312, 224.45731898, 0.00104375, -22.4457319, -0.00010437, -67.33719569, -0.00031312, -224.45731898, -0.00104375, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
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
    ops.uniaxialMaterial('Hysteretic', 23020, 50.83584874, 0.0014553, 61.40674198, 0.02356483, 6.1406742, 0.07664867, -50.83584874, -0.0014553, -61.40674198, -0.02356483, -6.1406742, -0.07664867, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 50.83584874, 0.0014553, 61.40674198, 0.02356483, 6.1406742, 0.07664867, -50.83584874, -0.0014553, -61.40674198, -0.02356483, -6.1406742, -0.07664867, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 87.30965062, 0.02910598, 87.30965062, 0.08731794, 61.11675543, -1892.09903627, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 21.82741265, 0.00010168, 65.48223796, 0.00030503, 218.27412655, 0.00101678, -21.82741265, -0.00010168, -65.48223796, -0.00030503, -218.27412655, -0.00101678, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 87.30965062, 0.02910598, 87.30965062, 0.08731794, 61.11675543, -1892.09903627, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 21.82741265, 0.00010168, 65.48223796, 0.00030503, 218.27412655, 0.00101678, -21.82741265, -0.00010168, -65.48223796, -0.00030503, -218.27412655, -0.00101678, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 8.925)
    ops.node(124021, 9.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 28100852.55570283, 11708688.56487618, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 50.51374614, 0.00138484, 61.09601494, 0.02541514, 6.10960149, 0.09175068, -50.51374614, -0.00138484, -61.09601494, -0.02541514, -6.10960149, -0.09175068, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 50.51374614, 0.00138484, 61.09601494, 0.02541514, 6.10960149, 0.09175068, -50.51374614, -0.00138484, -61.09601494, -0.02541514, -6.10960149, -0.09175068, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 107.22658608, 0.0276969, 107.22658608, 0.08309069, 75.05861025, -2640.53831951, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 26.80664652, 0.00012308, 80.41993956, 0.00036925, 268.0664652, 0.00123082, -26.80664652, -0.00012308, -80.41993956, -0.00036925, -268.0664652, -0.00123082, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 107.22658608, 0.0276969, 107.22658608, 0.08309069, 75.05861025, -2640.53831951, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 26.80664652, 0.00012308, 80.41993956, 0.00036925, 268.0664652, 0.00123082, -26.80664652, -0.00012308, -80.41993956, -0.00036925, -268.0664652, -0.00123082, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 8.925)
    ops.node(124022, 12.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0625, 28728422.65247, 11970176.10519583, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 50.64510336, 0.00137829, 61.20562259, 0.02519783, 6.12056226, 0.09318416, -50.64510336, -0.00137829, -61.20562259, -0.02519783, -6.12056226, -0.09318416, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 50.64510336, 0.00137829, 61.20562259, 0.02519783, 6.12056226, 0.09318416, -50.64510336, -0.00137829, -61.20562259, -0.02519783, -6.12056226, -0.09318416, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 106.29844246, 0.0275658, 106.29844246, 0.08269739, 74.40890972, -2522.40838618, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 26.57461061, 0.00011935, 79.72383184, 0.00035805, 265.74610615, 0.00119351, -26.57461061, -0.00011935, -79.72383184, -0.00035805, -265.74610615, -0.00119351, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 106.29844246, 0.0275658, 106.29844246, 0.08269739, 74.40890972, -2522.40838618, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 26.57461061, 0.00011935, 79.72383184, 0.00035805, 265.74610615, 0.00119351, -26.57461061, -0.00011935, -79.72383184, -0.00035805, -265.74610615, -0.00119351, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
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
    ops.uniaxialMaterial('Hysteretic', 23023, 50.27209283, 0.00143977, 60.67513756, 0.02375007, 6.06751376, 0.07901048, -50.27209283, -0.00143977, -60.67513756, -0.02375007, -6.06751376, -0.07901048, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 50.27209283, 0.00143977, 60.67513756, 0.02375007, 6.06751376, 0.07901048, -50.27209283, -0.00143977, -60.67513756, -0.02375007, -6.06751376, -0.07901048, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 85.99340295, 0.02879547, 85.99340295, 0.08638642, 60.19538206, -1746.69712937, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 21.49835074, 9.713e-05, 64.49505221, 0.00029138, 214.98350736, 0.00097127, -21.49835074, -9.713e-05, -64.49505221, -0.00029138, -214.98350736, -0.00097127, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 85.99340295, 0.02879547, 85.99340295, 0.08638642, 60.19538206, -1746.69712937, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 21.49835074, 9.713e-05, 64.49505221, 0.00029138, 214.98350736, 0.00097127, -21.49835074, -9.713e-05, -64.49505221, -0.00029138, -214.98350736, -0.00097127, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 21.0, 13.5, 8.9)
    ops.node(124024, 21.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 27059614.77549736, 11274839.48979057, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 44.35025065, 0.00143059, 53.96558201, 0.02789426, 5.3965582, 0.09097976, -44.35025065, -0.00143059, -53.96558201, -0.02789426, -5.3965582, -0.09097976, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 44.35025065, 0.00143059, 53.96558201, 0.02789426, 5.3965582, 0.09097976, -44.35025065, -0.00143059, -53.96558201, -0.02789426, -5.3965582, -0.09097976, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 88.46490258, 0.02861175, 88.46490258, 0.08583526, 61.92543181, -2476.58045496, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 22.11622565, 0.00010545, 66.34867694, 0.00031636, 221.16225646, 0.00105453, -22.11622565, -0.00010545, -66.34867694, -0.00031636, -221.16225646, -0.00105453, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 88.46490258, 0.02861175, 88.46490258, 0.08583526, 61.92543181, -2476.58045496, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 22.11622565, 0.00010545, 66.34867694, 0.00031636, 221.16225646, 0.00105453, -22.11622565, -0.00010545, -66.34867694, -0.00031636, -221.16225646, -0.00105453, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(124025, 9.0, 0.0, 1.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.09, 27103750.5262708, 11293229.38594617, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 93.6924599, 0.00073271, 110.03993738, 0.01417768, 11.00399374, 0.03620379, -93.6924599, -0.00073271, -110.03993738, -0.01417768, -11.00399374, -0.03620379, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 93.6924599, 0.00073271, 110.03993738, 0.01417768, 11.00399374, 0.03620379, -93.6924599, -0.00073271, -110.03993738, -0.01417768, -11.00399374, -0.03620379, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 182.3874335, 0.01465414, 182.3874335, 0.04396243, 127.67120345, -5020.6365586, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 45.59685838, 8.344e-05, 136.79057513, 0.00025033, 455.96858376, 0.00083442, -45.59685838, -8.344e-05, -136.79057513, -0.00025033, -455.96858376, -0.00083442, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 182.3874335, 0.01465414, 182.3874335, 0.04396243, 127.67120345, -5020.6365586, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 45.59685838, 8.344e-05, 136.79057513, 0.00025033, 455.96858376, 0.00083442, -45.59685838, -8.344e-05, -136.79057513, -0.00025033, -455.96858376, -0.00083442, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.7)
    ops.node(121003, 9.0, 0.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.09, 26094340.01984873, 10872641.67493697, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 84.87087719, 0.00067825, 99.63477989, 0.01370407, 9.96347799, 0.03403173, -84.87087719, -0.00067825, -99.63477989, -0.01370407, -9.96347799, -0.03403173, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 84.87087719, 0.00067825, 99.63477989, 0.01370407, 9.96347799, 0.03403173, -84.87087719, -0.00067825, -99.63477989, -0.01370407, -9.96347799, -0.03403173, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 174.43903041, 0.01356492, 174.43903041, 0.04069476, 122.10732129, -4872.21685302, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 43.6097576, 8.289e-05, 130.82927281, 0.00024868, 436.09757602, 0.00082893, -43.6097576, -8.289e-05, -130.82927281, -0.00024868, -436.09757602, -0.00082893, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 174.43903041, 0.01356492, 174.43903041, 0.04069476, 122.10732129, -4872.21685302, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 43.6097576, 8.289e-05, 130.82927281, 0.00024868, 436.09757602, 0.00082893, -43.6097576, -8.289e-05, -130.82927281, -0.00024868, -436.09757602, -0.00082893, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.0, 0.0, 0.0)
    ops.node(124026, 12.0, 0.0, 1.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.09, 27868054.16704732, 11611689.23626972, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 119.76747493, 0.00101165, 140.9471323, 0.01483291, 14.09471323, 0.03953268, -119.76747493, -0.00101165, -140.9471323, -0.01483291, -14.09471323, -0.03953268, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 119.76747493, 0.00101165, 140.9471323, 0.01483291, 14.09471323, 0.03953268, -119.76747493, -0.00101165, -140.9471323, -0.01483291, -14.09471323, -0.03953268, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 183.52404205, 0.02023297, 183.52404205, 0.06069892, 128.46682944, -4930.40902334, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 45.88101051, 8.166e-05, 137.64303154, 0.00024498, 458.81010514, 0.0008166, -45.88101051, -8.166e-05, -137.64303154, -0.00024498, -458.81010514, -0.0008166, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 183.52404205, 0.02023297, 183.52404205, 0.06069892, 128.46682944, -4930.40902334, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 45.88101051, 8.166e-05, 137.64303154, 0.00024498, 458.81010514, 0.0008166, -45.88101051, -8.166e-05, -137.64303154, -0.00024498, -458.81010514, -0.0008166, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.7)
    ops.node(121004, 12.0, 0.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.09, 27362018.89853462, 11400841.20772276, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 114.62904145, 0.00101348, 135.09399005, 0.0147271, 13.509399, 0.03958036, -114.62904145, -0.00101348, -135.09399005, -0.0147271, -13.509399, -0.03958036, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 114.62904145, 0.00101348, 135.09399005, 0.0147271, 13.509399, 0.03958036, -114.62904145, -0.00101348, -135.09399005, -0.0147271, -13.509399, -0.03958036, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 176.92048241, 0.02026962, 176.92048241, 0.06080887, 123.84433768, -4754.76520096, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 44.2301206, 8.018e-05, 132.6903618, 0.00024053, 442.30120601, 0.00080177, -44.2301206, -8.018e-05, -132.6903618, -0.00024053, -442.30120601, -0.00080177, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 176.92048241, 0.02026962, 176.92048241, 0.06080887, 123.84433768, -4754.76520096, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 44.2301206, 8.018e-05, 132.6903618, 0.00024053, 442.30120601, 0.00080177, -44.2301206, -8.018e-05, -132.6903618, -0.00024053, -442.30120601, -0.00080177, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.325)
    ops.node(124027, 9.0, 0.0, 4.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.09, 27417827.12192842, 11424094.63413684, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 101.02909613, 0.00094151, 120.02970949, 0.01686098, 12.00297095, 0.04859053, -101.02909613, -0.00094151, -120.02970949, -0.01686098, -12.00297095, -0.04859053, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 101.02909613, 0.00094151, 120.02970949, 0.01686098, 12.00297095, 0.04859053, -101.02909613, -0.00094151, -120.02970949, -0.01686098, -12.00297095, -0.04859053, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 180.21069894, 0.01883011, 180.21069894, 0.05649033, 126.14748926, -5114.27886167, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 45.05267474, 7.361e-05, 135.15802421, 0.00022084, 450.52674735, 0.00073615, -45.05267474, -7.361e-05, -135.15802421, -0.00022084, -450.52674735, -0.00073615, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 180.21069894, 0.01883011, 180.21069894, 0.05649033, 126.14748926, -5114.27886167, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 45.05267474, 7.361e-05, 135.15802421, 0.00022084, 450.52674735, 0.00073615, -45.05267474, -7.361e-05, -135.15802421, -0.00022084, -450.52674735, -0.00073615, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.65)
    ops.node(122003, 9.0, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.09, 28172555.92647392, 11738564.96936413, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 97.39425033, 0.00093516, 116.0898678, 0.01808902, 11.60898678, 0.05505901, -97.39425033, -0.00093516, -116.0898678, -0.01808902, -11.60898678, -0.05505901, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 97.39425033, 0.00093516, 116.0898678, 0.01808902, 11.60898678, 0.05505901, -97.39425033, -0.00093516, -116.0898678, -0.01808902, -11.60898678, -0.05505901, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 181.55167554, 0.01870318, 181.55167554, 0.05610954, 127.08617287, -5161.34291412, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 45.38791888, 7.218e-05, 136.16375665, 0.00021653, 453.87918884, 0.00072176, -45.38791888, -7.218e-05, -136.16375665, -0.00021653, -453.87918884, -0.00072176, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 181.55167554, 0.01870318, 181.55167554, 0.05610954, 127.08617287, -5161.34291412, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 45.38791888, 7.218e-05, 136.16375665, 0.00021653, 453.87918884, 0.00072176, -45.38791888, -7.218e-05, -136.16375665, -0.00021653, -453.87918884, -0.00072176, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.325)
    ops.node(124028, 12.0, 0.0, 4.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.09, 27284827.22621747, 11368678.01092395, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 100.89985551, 0.00094081, 119.85297586, 0.01710607, 11.98529759, 0.04835755, -100.89985551, -0.00094081, -119.85297586, -0.01710607, -11.98529759, -0.04835755, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 100.89985551, 0.00094081, 119.85297586, 0.01710607, 11.98529759, 0.04835755, -100.89985551, -0.00094081, -119.85297586, -0.01710607, -11.98529759, -0.04835755, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 182.17970737, 0.01881617, 182.17970737, 0.0564485, 127.52579516, -5264.33467646, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 45.54492684, 7.478e-05, 136.63478053, 0.00022435, 455.44926843, 0.00074782, -45.54492684, -7.478e-05, -136.63478053, -0.00022435, -455.44926843, -0.00074782, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 182.17970737, 0.01881617, 182.17970737, 0.0564485, 127.52579516, -5264.33467646, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 45.54492684, 7.478e-05, 136.63478053, 0.00022435, 455.44926843, 0.00074782, -45.54492684, -7.478e-05, -136.63478053, -0.00022435, -455.44926843, -0.00074782, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.65)
    ops.node(122004, 12.0, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.09, 28391683.94148324, 11829868.30895135, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 96.7605762, 0.00093203, 115.34622979, 0.01851547, 11.53462298, 0.0562244, -96.7605762, -0.00093203, -115.34622979, -0.01851547, -11.53462298, -0.0562244, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 96.7605762, 0.00093203, 115.34622979, 0.01851547, 11.53462298, 0.0562244, -96.7605762, -0.00093203, -115.34622979, -0.01851547, -11.53462298, -0.0562244, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 184.02196107, 0.01864052, 184.02196107, 0.05592155, 128.81537275, -5259.96954318, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 46.00549027, 7.259e-05, 138.0164708, 0.00021778, 460.05490267, 0.00072593, -46.00549027, -7.259e-05, -138.0164708, -0.00021778, -460.05490267, -0.00072593, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 184.02196107, 0.01864052, 184.02196107, 0.05592155, 128.81537275, -5259.96954318, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 46.00549027, 7.259e-05, 138.0164708, 0.00021778, 460.05490267, 0.00072593, -46.00549027, -7.259e-05, -138.0164708, -0.00021778, -460.05490267, -0.00072593, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.125)
    ops.node(124029, 9.0, 0.0, 7.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.0625, 27592478.06136518, 11496865.85890216, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 66.08399086, 0.00111736, 78.646417, 0.01897712, 7.8646417, 0.05843815, -66.08399086, -0.00111736, -78.646417, -0.01897712, -7.8646417, -0.05843815, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 66.08399086, 0.00111736, 78.646417, 0.01897712, 7.8646417, 0.05843815, -66.08399086, -0.00111736, -78.646417, -0.01897712, -7.8646417, -0.05843815, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 122.53850599, 0.02234721, 122.53850599, 0.06704164, 85.7769542, -4171.93774536, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 30.6346265, 7.162e-05, 91.90387949, 0.00021487, 306.34626498, 0.00071625, -30.6346265, -7.162e-05, -91.90387949, -0.00021487, -306.34626498, -0.00071625, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 122.53850599, 0.02234721, 122.53850599, 0.06704164, 85.7769542, -4171.93774536, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 30.6346265, 7.162e-05, 91.90387949, 0.00021487, 306.34626498, 0.00071625, -30.6346265, -7.162e-05, -91.90387949, -0.00021487, -306.34626498, -0.00071625, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.45)
    ops.node(123003, 9.0, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.0625, 26936198.01713781, 11223415.84047409, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 62.80835008, 0.00107116, 75.02318711, 0.02041518, 7.50231871, 0.06245855, -62.80835008, -0.00107116, -75.02318711, -0.02041518, -7.50231871, -0.06245855, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 62.80835008, 0.00107116, 75.02318711, 0.02041518, 7.50231871, 0.06245855, -62.80835008, -0.00107116, -75.02318711, -0.02041518, -7.50231871, -0.06245855, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 119.37357491, 0.02142318, 119.37357491, 0.06426954, 83.56150244, -4293.09850724, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 29.84339373, 7.147e-05, 89.53018118, 0.00021442, 298.43393727, 0.00071475, -29.84339373, -7.147e-05, -89.53018118, -0.00021442, -298.43393727, -0.00071475, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 119.37357491, 0.02142318, 119.37357491, 0.06426954, 83.56150244, -4293.09850724, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 29.84339373, 7.147e-05, 89.53018118, 0.00021442, 298.43393727, 0.00071475, -29.84339373, -7.147e-05, -89.53018118, -0.00021442, -298.43393727, -0.00071475, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.125)
    ops.node(124030, 12.0, 0.0, 7.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.0625, 27907378.96014513, 11628074.56672714, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 65.15426588, 0.00112875, 77.56356754, 0.01977525, 7.75635675, 0.06052497, -65.15426588, -0.00112875, -77.56356754, -0.01977525, -7.75635675, -0.06052497, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 65.15426588, 0.00112875, 77.56356754, 0.01977525, 7.75635675, 0.06052497, -65.15426588, -0.00112875, -77.56356754, -0.01977525, -7.75635675, -0.06052497, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 124.77642138, 0.02257504, 124.77642138, 0.06772512, 87.34349497, -4270.92939223, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 31.19410535, 7.211e-05, 93.58231604, 0.00021633, 311.94105346, 0.0007211, -31.19410535, -7.211e-05, -93.58231604, -0.00021633, -311.94105346, -0.0007211, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 124.77642138, 0.02257504, 124.77642138, 0.06772512, 87.34349497, -4270.92939223, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 31.19410535, 7.211e-05, 93.58231604, 0.00021633, 311.94105346, 0.0007211, -31.19410535, -7.211e-05, -93.58231604, -0.00021633, -311.94105346, -0.0007211, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.45)
    ops.node(123004, 12.0, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.0625, 26633947.02369331, 11097477.92653888, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 61.14028437, 0.00107905, 73.00530313, 0.02014381, 7.30053031, 0.06091384, -61.14028437, -0.00107905, -73.00530313, -0.02014381, -7.30053031, -0.06091384, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 61.14028437, 0.00107905, 73.00530313, 0.02014381, 7.30053031, 0.06091384, -61.14028437, -0.00107905, -73.00530313, -0.02014381, -7.30053031, -0.06091384, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 119.49119241, 0.02158108, 119.49119241, 0.06474325, 83.64383469, -4351.23402158, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 29.8727981, 7.236e-05, 89.61839431, 0.00021707, 298.72798103, 0.00072357, -29.8727981, -7.236e-05, -89.61839431, -0.00021707, -298.72798103, -0.00072357, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 119.49119241, 0.02158108, 119.49119241, 0.06474325, 83.64383469, -4351.23402158, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 29.8727981, 7.236e-05, 89.61839431, 0.00021707, 298.72798103, 0.00072357, -29.8727981, -7.236e-05, -89.61839431, -0.00021707, -298.72798103, -0.00072357, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 8.925)
    ops.node(124031, 9.0, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.0625, 27861423.66400119, 11608926.52666716, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 49.59743315, 0.00102805, 60.01758437, 0.02428028, 6.00175844, 0.09041389, -49.59743315, -0.00102805, -60.01758437, -0.02428028, -6.00175844, -0.09041389, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 49.59743315, 0.00102805, 60.01758437, 0.02428028, 6.00175844, 0.09041389, -49.59743315, -0.00102805, -60.01758437, -0.02428028, -6.00175844, -0.09041389, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 109.55828372, 0.02056096, 109.55828372, 0.06168289, 76.69079861, -5000.45594414, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 27.38957093, 6.342e-05, 82.16871279, 0.00019026, 273.89570931, 0.00063419, -27.38957093, -6.342e-05, -82.16871279, -0.00019026, -273.89570931, -0.00063419, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 109.55828372, 0.02056096, 109.55828372, 0.06168289, 76.69079861, -5000.45594414, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 27.38957093, 6.342e-05, 82.16871279, 0.00019026, 273.89570931, 0.00063419, -27.38957093, -6.342e-05, -82.16871279, -0.00019026, -273.89570931, -0.00063419, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 9.0, 0.0, 10.25)
    ops.node(124003, 9.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.0625, 26972935.61399165, 11238723.17249652, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 46.66467132, 0.00097724, 56.7697348, 0.02683124, 5.67697348, 0.09957358, -46.66467132, -0.00097724, -56.7697348, -0.02683124, -5.67697348, -0.09957358, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 46.66467132, 0.00097724, 56.7697348, 0.02683124, 5.67697348, 0.09957358, -46.66467132, -0.00097724, -56.7697348, -0.02683124, -5.67697348, -0.09957358, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 104.35851103, 0.01954477, 104.35851103, 0.05863432, 73.05095772, -6268.43700864, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 26.08962776, 6.24e-05, 78.26888327, 0.0001872, 260.89627757, 0.00062399, -26.08962776, -6.24e-05, -78.26888327, -0.0001872, -260.89627757, -0.00062399, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 104.35851103, 0.01954477, 104.35851103, 0.05863432, 73.05095772, -6268.43700864, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 26.08962776, 6.24e-05, 78.26888327, 0.0001872, 260.89627757, 0.00062399, -26.08962776, -6.24e-05, -78.26888327, -0.0001872, -260.89627757, -0.00062399, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 8.925)
    ops.node(124032, 12.0, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.0625, 27579151.78036499, 11491313.24181875, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 49.45925031, 0.00100953, 59.86755131, 0.024595, 5.98675513, 0.08993569, -49.45925031, -0.00100953, -59.86755131, -0.024595, -5.98675513, -0.08993569, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 49.45925031, 0.00100953, 59.86755131, 0.024595, 5.98675513, 0.08993569, -49.45925031, -0.00100953, -59.86755131, -0.024595, -5.98675513, -0.08993569, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 108.91584486, 0.0201906, 108.91584486, 0.06057179, 76.2410914, -4995.18750949, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 27.22896121, 6.369e-05, 81.68688364, 0.00019108, 272.28961214, 0.00063693, -27.22896121, -6.369e-05, -81.68688364, -0.00019108, -272.28961214, -0.00063693, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 108.91584486, 0.0201906, 108.91584486, 0.06057179, 76.2410914, -4995.18750949, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 27.22896121, 6.369e-05, 81.68688364, 0.00019108, 272.28961214, 0.00063693, -27.22896121, -6.369e-05, -81.68688364, -0.00019108, -272.28961214, -0.00063693, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 12.0, 0.0, 10.25)
    ops.node(124004, 12.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.0625, 27046303.47489247, 11269293.11453853, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 45.80624156, 0.00100292, 55.72026834, 0.02662808, 5.57202683, 0.09953722, -45.80624156, -0.00100292, -55.72026834, -0.02662808, -5.57202683, -0.09953722, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 45.80624156, 0.00100292, 55.72026834, 0.02662808, 5.57202683, 0.09953722, -45.80624156, -0.00100292, -55.72026834, -0.02662808, -5.57202683, -0.09953722, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 106.52209562, 0.02005849, 106.52209562, 0.06017547, 74.56546693, -6584.05800408, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 26.6305239, 6.352e-05, 79.89157171, 0.00019056, 266.30523904, 0.0006352, -26.6305239, -6.352e-05, -79.89157171, -0.00019056, -266.30523904, -0.0006352, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 106.52209562, 0.02005849, 106.52209562, 0.06017547, 74.56546693, -6584.05800408, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 26.6305239, 6.352e-05, 79.89157171, 0.00019056, 266.30523904, 0.0006352, -26.6305239, -6.352e-05, -79.89157171, -0.00019056, -266.30523904, -0.0006352, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
