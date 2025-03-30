import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 26164800.56154356, 10902000.23397648, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 47.20055204, 0.00085011, 55.64449268, 0.01078047, 5.56444927, 0.03006155, -47.20055204, -0.00085011, -55.64449268, -0.01078047, -5.56444927, -0.03006155, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 51.51159849, 0.00085011, 60.7267636, 0.01078047, 6.07267636, 0.03006155, -51.51159849, -0.00085011, -60.7267636, -0.01078047, -6.07267636, -0.03006155, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 106.33508449, 0.01700228, 106.33508449, 0.05100684, 74.43455914, -2057.55027123, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 26.58377112, 0.00011704, 79.75131337, 0.00035113, 265.83771123, 0.00117045, -26.58377112, -0.00011704, -79.75131337, -0.00035113, -265.83771123, -0.00117045, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 106.33508449, 0.01700228, 106.33508449, 0.05100684, 74.43455914, -2057.55027123, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 26.58377112, 0.00011704, 79.75131337, 0.00035113, 265.83771123, 0.00117045, -26.58377112, -0.00011704, -79.75131337, -0.00035113, -265.83771123, -0.00117045, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.85, 0.0, 0.0)
    ops.node(121002, 3.85, 0.0, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.12, 27840449.32158704, 11600187.21732793, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 192.85155174, 0.00139472, 229.80333175, 0.01224633, 22.98033317, 0.03067527, -192.85155174, -0.00139472, -229.80333175, -0.01224633, -22.98033317, -0.03067527, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 249.02810055, 0.00109289, 296.74372173, 0.01290399, 29.67437217, 0.03543521, -249.02810055, -0.00109289, -296.74372173, -0.01290399, -29.67437217, -0.03543521, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 152.09493821, 0.02789448, 152.09493821, 0.08368345, 106.46645675, -2281.37060974, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 38.02373455, 8.195e-05, 114.07120366, 0.00024584, 380.23734552, 0.00081946, -38.02373455, -8.195e-05, -114.07120366, -0.00024584, -380.23734552, -0.00081946, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 171.78719034, 0.02185779, 171.78719034, 0.06557338, 120.25103324, -2767.85353144, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 42.94679759, 9.256e-05, 128.84039276, 0.00027767, 429.46797585, 0.00092556, -42.94679759, -9.256e-05, -128.84039276, -0.00027767, -429.46797585, -0.00092556, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 14.5, 0.0, 0.0)
    ops.node(121005, 14.5, 0.0, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.12, 27601235.31822017, 11500514.71592507, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 190.51991899, 0.0013745, 226.97803728, 0.01226406, 22.69780373, 0.03026257, -190.51991899, -0.0013745, -226.97803728, -0.01226406, -22.69780373, -0.03026257, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 245.95497948, 0.00107839, 293.02121688, 0.0129308, 29.30212169, 0.03493578, -245.95497948, -0.00107839, -293.02121688, -0.0129308, -29.30212169, -0.03493578, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 151.94815122, 0.02749001, 151.94815122, 0.08247003, 106.36370585, -2302.7107735, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 37.98703781, 8.258e-05, 113.96111342, 0.00024773, 379.87037805, 0.00082577, -37.98703781, -8.258e-05, -113.96111342, -0.00024773, -379.87037805, -0.00082577, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 171.88277469, 0.02156776, 171.88277469, 0.06470328, 120.31794228, -2799.20969028, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 42.97069367, 9.341e-05, 128.91208102, 0.00028023, 429.70693673, 0.0009341, -42.97069367, -9.341e-05, -128.91208102, -0.00028023, -429.70693673, -0.0009341, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 18.35, 0.0, 0.0)
    ops.node(121006, 18.35, 0.0, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.0625, 27569694.28155567, 11487372.61731486, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 76.09332083, 0.00156295, 90.01868036, 0.01237208, 9.00186804, 0.03590191, -76.09332083, -0.00156295, -90.01868036, -0.01237208, -9.00186804, -0.03590191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 86.18545891, 0.00156295, 101.95771709, 0.01237208, 10.19577171, 0.03590191, -86.18545891, -0.00156295, -101.95771709, -0.01237208, -10.19577171, -0.03590191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 110.05826425, 0.03125908, 110.05826425, 0.09377725, 77.04078497, -2081.03125868, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 27.51456606, 0.00011497, 82.54369819, 0.00034491, 275.14566062, 0.0011497, -27.51456606, -0.00011497, -82.54369819, -0.00034491, -275.14566062, -0.0011497, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 110.05826425, 0.03125908, 110.05826425, 0.09377725, 77.04078497, -2081.03125868, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 27.51456606, 0.00011497, 82.54369819, 0.00034491, 275.14566062, 0.0011497, -27.51456606, -0.00011497, -82.54369819, -0.00034491, -275.14566062, -0.0011497, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 5.8, 0.0)
    ops.node(121007, 0.0, 5.8, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1575, 27373518.03730932, 11405632.51554555, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 227.87501994, 0.00092071, 272.57773726, 0.01145351, 27.25777373, 0.03637496, -227.87501994, -0.00092071, -272.57773726, -0.01145351, -27.25777373, -0.03637496, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 207.01401743, 0.00110229, 247.62438844, 0.01087311, 24.76243884, 0.03172825, -207.01401743, -0.00110229, -247.62438844, -0.01087311, -24.76243884, -0.03172825, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 233.88359212, 0.01841427, 233.88359212, 0.05524281, 163.71851448, -3572.98280897, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 58.47089803, 9.765e-05, 175.41269409, 0.00029294, 584.70898029, 0.00097647, -58.47089803, -9.765e-05, -175.41269409, -0.00029294, -584.70898029, -0.00097647, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 194.63276448, 0.02204578, 194.63276448, 0.06613735, 136.24293513, -2948.130613, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 48.65819112, 8.126e-05, 145.97457336, 0.00024378, 486.58191119, 0.0008126, -48.65819112, -8.126e-05, -145.97457336, -0.00024378, -486.58191119, -0.0008126, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 3.85, 5.8, 0.0)
    ops.node(121008, 3.85, 5.8, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.1925, 27058245.626104, 11274269.01087667, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 466.93135001, 0.0008814, 558.13122977, 0.01249407, 55.81312298, 0.03343628, -466.93135001, -0.0008814, -558.13122977, -0.01249407, -55.81312298, -0.03343628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 379.85780679, 0.00120585, 454.05069683, 0.01147699, 45.40506968, 0.02712855, -379.85780679, -0.00120585, -454.05069683, -0.01147699, -45.40506968, -0.02712855, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 305.87431263, 0.01762808, 305.87431263, 0.05288424, 214.11201884, -3867.25649952, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 76.46857816, 0.0001057, 229.40573447, 0.00031711, 764.68578156, 0.00105702, -76.46857816, -0.0001057, -229.40573447, -0.00031711, -764.68578156, -0.00105702, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 210.09557399, 0.02411708, 210.09557399, 0.07235125, 147.0669018, -2897.66709421, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 52.5238935, 7.26e-05, 157.5716805, 0.00021781, 525.23893499, 0.00072604, -52.5238935, -7.26e-05, -157.5716805, -0.00021781, -525.23893499, -0.00072604, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 7.7, 5.8, 0.0)
    ops.node(121009, 7.7, 5.8, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.21, 27990151.46102585, 11662563.10876077, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 551.97110831, 0.0008321, 661.31556144, 0.01346737, 66.13155614, 0.03746583, -551.97110831, -0.0008321, -661.31556144, -0.01346737, -66.13155614, -0.03746583, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 419.42309835, 0.0011864, 502.51003647, 0.01212718, 50.25100365, 0.02918182, -419.42309835, -0.0011864, -502.51003647, -0.01212718, -50.25100365, -0.02918182, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 358.24620268, 0.016642, 358.24620268, 0.04992601, 250.77234188, -4163.56362332, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 89.56155067, 0.00010971, 268.68465201, 0.00032912, 895.6155067, 0.00109706, -89.56155067, -0.00010971, -268.68465201, -0.00032912, -895.6155067, -0.00109706, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 226.02955289, 0.02372796, 226.02955289, 0.07118388, 158.22068702, -2918.65313998, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 56.50738822, 6.922e-05, 169.52216466, 0.00020765, 565.07388221, 0.00069217, -56.50738822, -6.922e-05, -169.52216466, -0.00020765, -565.07388221, -0.00069217, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 10.65, 5.8, 0.0)
    ops.node(121010, 10.65, 5.8, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.21, 27302653.53285908, 11376105.63869128, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 543.21051611, 0.00083016, 650.70756151, 0.01305957, 65.07075615, 0.03577293, -543.21051611, -0.00083016, -650.70756151, -0.01305957, -65.07075615, -0.03577293, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 411.55361926, 0.00118685, 492.99681077, 0.01177621, 49.29968108, 0.02791758, -411.55361926, -0.00118685, -492.99681077, -0.01177621, -49.29968108, -0.02791758, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 349.16125226, 0.01660311, 349.16125226, 0.04980934, 244.41287658, -4100.24207618, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 87.29031307, 0.00010962, 261.8709392, 0.00032885, 872.90313065, 0.00109616, -87.29031307, -0.00010962, -261.8709392, -0.00032885, -872.90313065, -0.00109616, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 220.25565632, 0.02373697, 220.25565632, 0.07121091, 154.17895943, -2887.69097702, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 55.06391408, 6.915e-05, 165.19174224, 0.00020744, 550.63914081, 0.00069147, -55.06391408, -6.915e-05, -165.19174224, -0.00020744, -550.63914081, -0.00069147, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 14.5, 5.8, 0.0)
    ops.node(121011, 14.5, 5.8, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.1925, 27223283.14499593, 11343034.6437483, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 462.63535313, 0.00087349, 553.07102349, 0.01282668, 55.30710235, 0.03409625, -462.63535313, -0.00087349, -553.07102349, -0.01282668, -55.30710235, -0.03409625, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 374.55385279, 0.00119616, 447.77140638, 0.01176848, 44.77714064, 0.0276647, -374.55385279, -0.00119616, -447.77140638, -0.01176848, -44.77714064, -0.0276647, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 305.9914132, 0.01746978, 305.9914132, 0.05240933, 214.19398924, -3828.83181643, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 76.4978533, 0.0001051, 229.4935599, 0.00031531, 764.97853301, 0.00105102, -76.4978533, -0.0001051, -229.4935599, -0.00031531, -764.97853301, -0.00105102, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 210.27502465, 0.02392315, 210.27502465, 0.07176944, 147.19251725, -2876.48711937, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 52.56875616, 7.223e-05, 157.70626849, 0.00021668, 525.68756162, 0.00072225, -52.56875616, -7.223e-05, -157.70626849, -0.00021668, -525.68756162, -0.00072225, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 18.35, 5.8, 0.0)
    ops.node(121012, 18.35, 5.8, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1575, 27994260.73399261, 11664275.30583026, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 226.40684963, 0.0008961, 270.88828424, 0.01209967, 27.08882842, 0.03836573, -226.40684963, -0.0008961, -270.88828424, -0.01209967, -27.08882842, -0.03836573, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 205.93728324, 0.00106854, 246.39712715, 0.01146161, 24.63971272, 0.03344197, -205.93728324, -0.00106854, -246.39712715, -0.01146161, -24.63971272, -0.03344197, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 241.90315563, 0.01792202, 241.90315563, 0.05376605, 169.33220894, -3714.66677447, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 60.47578891, 9.876e-05, 181.42736672, 0.00029627, 604.75788906, 0.00098756, -60.47578891, -9.876e-05, -181.42736672, -0.00029627, -604.75788906, -0.00098756, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 201.19466813, 0.0213708, 201.19466813, 0.06411239, 140.83626769, -3048.09072981, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 50.29866703, 8.214e-05, 150.8960011, 0.00024641, 502.98667032, 0.00082137, -50.29866703, -8.214e-05, -150.8960011, -0.00024641, -502.98667032, -0.00082137, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 11.6, 0.0)
    ops.node(121013, 0.0, 11.6, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.1575, 27797306.29059401, 11582210.95441417, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 224.87829058, 0.00091273, 269.20384954, 0.01181141, 26.92038495, 0.03811422, -224.87829058, -0.00091273, -269.20384954, -0.01181141, -26.92038495, -0.03811422, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 204.1003713, 0.00109262, 244.33041316, 0.01120286, 24.43304132, 0.03321397, -204.1003713, -0.00109262, -244.33041316, -0.01120286, -24.43304132, -0.03321397, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 238.44886871, 0.01825455, 238.44886871, 0.05476366, 166.9142081, -3664.06218187, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 59.61221718, 9.804e-05, 178.83665154, 0.00029411, 596.12217179, 0.00098036, -59.61221718, -9.804e-05, -178.83665154, -0.00029411, -596.12217179, -0.00098036, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 198.29781988, 0.02185243, 198.29781988, 0.06555728, 138.80847392, -3001.53192993, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 49.57445497, 8.153e-05, 148.72336491, 0.00024458, 495.7445497, 0.00081528, -49.57445497, -8.153e-05, -148.72336491, -0.00024458, -495.7445497, -0.00081528, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 3.85, 11.6, 0.0)
    ops.node(121014, 3.85, 11.6, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.1925, 26832014.25445624, 11180005.93935677, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 485.68220016, 0.00090402, 580.95629927, 0.01107179, 58.09562993, 0.02847182, -485.68220016, -0.00090402, -580.95629927, -0.01107179, -58.09562993, -0.02847182, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 370.28328414, 0.0012512, 442.92009542, 0.01036538, 44.29200954, 0.02378865, -370.28328414, -0.0012512, -442.92009542, -0.01036538, -44.29200954, -0.02378865, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 278.71660906, 0.01808047, 278.71660906, 0.05424142, 195.10162634, -3180.64139124, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 69.67915226, 9.713e-05, 209.03745679, 0.00029139, 696.79152265, 0.0009713, -69.67915226, -9.713e-05, -209.03745679, -0.00029139, -696.79152265, -0.0009713, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 192.49127252, 0.02502394, 192.49127252, 0.07507181, 134.74389076, -2489.56998666, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 48.12281813, 6.708e-05, 144.36845439, 0.00020124, 481.22818129, 0.00067081, -48.12281813, -6.708e-05, -144.36845439, -0.00020124, -481.22818129, -0.00067081, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.7, 11.6, 0.0)
    ops.node(121015, 7.7, 11.6, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.1925, 27764742.8153908, 11568642.83974617, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 401.12652052, 0.00084913, 481.38823992, 0.0129063, 48.13882399, 0.03770628, -401.12652052, -0.00084913, -481.38823992, -0.0129063, -48.13882399, -0.03770628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 311.96020306, 0.00115667, 374.38056422, 0.01182095, 37.43805642, 0.0303557, -311.96020306, -0.00115667, -374.38056422, -0.01182095, -37.43805642, -0.0303557, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 299.7299607, 0.01698256, 299.7299607, 0.05094769, 209.81097249, -3684.17992693, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 74.93249017, 0.00010094, 224.79747052, 0.00030283, 749.32490174, 0.00100943, -74.93249017, -0.00010094, -224.79747052, -0.00030283, -749.32490174, -0.00100943, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 205.84201695, 0.02313335, 205.84201695, 0.06940005, 144.08941186, -2681.15268289, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 51.46050424, 6.932e-05, 154.38151271, 0.00020797, 514.60504237, 0.00069324, -51.46050424, -6.932e-05, -154.38151271, -0.00020797, -514.60504237, -0.00069324, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 10.65, 11.6, 0.0)
    ops.node(121016, 10.65, 11.6, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1925, 26998694.20683129, 11249455.91951304, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 401.2440896, 0.00085647, 481.45412836, 0.01285287, 48.14541284, 0.03623119, -401.2440896, -0.00085647, -481.45412836, -0.01285287, -48.14541284, -0.03623119, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 313.60989234, 0.00116616, 376.30156126, 0.0117767, 37.63015613, 0.02924894, -313.60989234, -0.00116616, -376.30156126, -0.0117767, -37.63015613, -0.02924894, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 293.63427702, 0.01712932, 293.63427702, 0.05138796, 205.54399392, -3695.48387713, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 73.40856926, 0.0001017, 220.22570777, 0.00030509, 734.08569256, 0.00101696, -73.40856926, -0.0001017, -220.22570777, -0.00030509, -734.08569256, -0.00101696, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 201.48600656, 0.02332325, 201.48600656, 0.06996974, 141.04020459, -2687.28806252, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 50.37150164, 6.978e-05, 151.11450492, 0.00020935, 503.7150164, 0.00069782, -50.37150164, -6.978e-05, -151.11450492, -0.00020935, -503.7150164, -0.00069782, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 14.5, 11.6, 0.0)
    ops.node(121017, 14.5, 11.6, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.1925, 28401895.65062046, 11834123.18775853, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 496.43175369, 0.00089199, 594.18845627, 0.01123815, 59.41884563, 0.0311031, -496.43175369, -0.00089199, -594.18845627, -0.01123815, -59.41884563, -0.0311031, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 380.1016063, 0.0012248, 454.95072585, 0.01049891, 45.49507258, 0.02582373, -380.1016063, -0.0012248, -454.95072585, -0.01049891, -45.49507258, -0.02582373, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 289.9040364, 0.01783975, 289.9040364, 0.05351926, 202.93282548, -3117.04617308, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 72.4760091, 9.544e-05, 217.4280273, 0.00028633, 724.76009101, 0.00095444, -72.4760091, -9.544e-05, -217.4280273, -0.00028633, -724.76009101, -0.00095444, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 200.60996337, 0.02449605, 200.60996337, 0.07348814, 140.42697436, -2453.71498355, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 50.15249084, 6.605e-05, 150.45747253, 0.00019814, 501.52490843, 0.00066046, -50.15249084, -6.605e-05, -150.45747253, -0.00019814, -501.52490843, -0.00066046, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 18.35, 11.6, 0.0)
    ops.node(121018, 18.35, 11.6, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.1575, 28627128.22616072, 11927970.09423363, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 224.79530947, 0.00090016, 269.10406345, 0.01208744, 26.91040634, 0.04010369, -224.79530947, -0.00090016, -269.10406345, -0.01208744, -26.91040634, -0.04010369, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 203.69218606, 0.0010762, 243.84136436, 0.01145416, 24.38413644, 0.03489914, -203.69218606, -0.0010762, -243.84136436, -0.01145416, -24.38413644, -0.03489914, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 242.04857321, 0.01800315, 242.04857321, 0.05400946, 169.43400125, -3624.39024321, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 60.5121433, 9.663e-05, 181.53642991, 0.00028989, 605.12143302, 0.00096631, -60.5121433, -9.663e-05, -181.53642991, -0.00028989, -605.12143302, -0.00096631, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 201.53299724, 0.02152405, 201.53299724, 0.06457215, 141.07309807, -2973.59393442, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 50.38324931, 8.046e-05, 151.14974793, 0.00024137, 503.8324931, 0.00080456, -50.38324931, -8.046e-05, -151.14974793, -0.00024137, -503.8324931, -0.00080456, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 17.4, 0.0)
    ops.node(121019, 0.0, 17.4, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.0625, 27724384.06680581, 11551826.69450242, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 77.78620246, 0.00159299, 92.04157734, 0.01196119, 9.20415773, 0.03591302, -77.78620246, -0.00159299, -92.04157734, -0.01196119, -9.20415773, -0.03591302, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 88.37757353, 0.00159299, 104.57396057, 0.01196119, 10.45739606, 0.03591302, -88.37757353, -0.00159299, -104.57396057, -0.01196119, -10.45739606, -0.03591302, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 108.43375299, 0.0318598, 108.43375299, 0.0955794, 75.90362709, -2019.10809614, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 27.10843825, 0.00011264, 81.32531474, 0.00033792, 271.08438247, 0.00112641, -27.10843825, -0.00011264, -81.32531474, -0.00033792, -271.08438247, -0.00112641, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 108.43375299, 0.0318598, 108.43375299, 0.0955794, 75.90362709, -2019.10809614, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 27.10843825, 0.00011264, 81.32531474, 0.00033792, 271.08438247, 0.00112641, -27.10843825, -0.00011264, -81.32531474, -0.00033792, -271.08438247, -0.00112641, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 3.85, 17.4, 0.0)
    ops.node(121020, 3.85, 17.4, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.14, 28599797.08678026, 11916582.11949178, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 255.35907216, 0.00119292, 305.45045337, 0.01234826, 30.54504534, 0.03422532, -255.35907216, -0.00119292, -305.45045337, -0.01234826, -30.54504534, -0.03422532, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 257.30632688, 0.00107402, 307.77968269, 0.01266573, 30.77796827, 0.0366275, -257.30632688, -0.00107402, -307.77968269, -0.01266573, -30.77796827, -0.0366275, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 174.68836084, 0.02385841, 174.68836084, 0.07157524, 122.28185259, -2509.03272835, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 43.67209021, 7.853e-05, 131.01627063, 0.0002356, 436.7209021, 0.00078532, -43.67209021, -7.853e-05, -131.01627063, -0.0002356, -436.7209021, -0.00078532, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 186.01062386, 0.02148035, 186.01062386, 0.06444105, 130.20743671, -2754.76452786, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 46.50265597, 8.362e-05, 139.5079679, 0.00025087, 465.02655966, 0.00083622, -46.50265597, -8.362e-05, -139.5079679, -0.00025087, -465.02655966, -0.00083622, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 7.7, 17.4, 0.0)
    ops.node(121021, 7.7, 17.4, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.105, 26589646.42101824, 11079019.34209093, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 177.41366707, 0.00143583, 211.04585061, 0.01234873, 21.10458506, 0.02992181, -177.41366707, -0.00143583, -211.04585061, -0.01234873, -21.10458506, -0.02992181, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 202.96900913, 0.0012507, 241.44570081, 0.01268137, 24.14457008, 0.032297, -202.96900913, -0.0012507, -241.44570081, -0.01268137, -24.14457008, -0.032297, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 138.71381079, 0.02871665, 138.71381079, 0.08614995, 97.09966755, -2269.78977898, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 34.6784527, 8.943e-05, 104.03535809, 0.00026829, 346.78452697, 0.00089431, -34.6784527, -8.943e-05, -104.03535809, -0.00026829, -346.78452697, -0.00089431, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 147.90534147, 0.02501398, 147.90534147, 0.07504195, 103.53373903, -2539.23196131, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 36.97633537, 9.536e-05, 110.9290061, 0.00028607, 369.76335367, 0.00095357, -36.97633537, -9.536e-05, -110.9290061, -0.00028607, -369.76335367, -0.00095357, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 10.65, 17.4, 0.0)
    ops.node(121022, 10.65, 17.4, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.105, 27747346.85397518, 11561394.52248966, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 177.12816072, 0.00140544, 211.02379987, 0.01265139, 21.10237999, 0.03257623, -177.12816072, -0.00140544, -211.02379987, -0.01265139, -21.10237999, -0.03257623, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 202.75931594, 0.00122494, 241.55979001, 0.01300446, 24.155979, 0.0352452, -202.75931594, -0.00122494, -241.55979001, -0.01300446, -24.155979, -0.0352452, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 140.47779718, 0.0281088, 140.47779718, 0.0843264, 98.33445803, -2207.58695638, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 35.1194493, 8.679e-05, 105.35834789, 0.00026037, 351.19449296, 0.0008679, -35.1194493, -8.679e-05, -105.35834789, -0.00026037, -351.19449296, -0.0008679, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 149.30294301, 0.02449877, 149.30294301, 0.0734963, 104.51206011, -2462.53038305, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 37.32573575, 9.224e-05, 111.97720726, 0.00027673, 373.25735753, 0.00092242, -37.32573575, -9.224e-05, -111.97720726, -0.00027673, -373.25735753, -0.00092242, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 14.5, 17.4, 0.0)
    ops.node(121023, 14.5, 17.4, 2.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.14, 26506509.15412935, 11044378.81422056, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 251.02669732, 0.0012101, 299.93408768, 0.01205347, 29.99340877, 0.03025269, -251.02669732, -0.0012101, -299.93408768, -0.01205347, -29.99340877, -0.03025269, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 252.3279151, 0.0010886, 301.48882099, 0.01235614, 30.1488821, 0.0322896, -252.3279151, -0.0010886, -301.48882099, -0.01235614, -30.1488821, -0.0322896, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 165.70605863, 0.02420192, 165.70605863, 0.07260577, 115.99424104, -2519.42053836, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 41.42651466, 8.038e-05, 124.27954398, 0.00024113, 414.26514659, 0.00080377, -41.42651466, -8.038e-05, -124.27954398, -0.00024113, -414.26514659, -0.00080377, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 176.85678694, 0.02177192, 176.85678694, 0.06531575, 123.79975086, -2767.20525328, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 44.21419674, 8.579e-05, 132.64259021, 0.00025736, 442.14196736, 0.00085785, -44.21419674, -8.579e-05, -132.64259021, -0.00025736, -442.14196736, -0.00085785, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 18.35, 17.4, 0.0)
    ops.node(121024, 18.35, 17.4, 2.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.0625, 27586072.2657209, 11494196.77738371, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 77.17034664, 0.00158478, 91.29071, 0.01191083, 9.129071, 0.03545237, -77.17034664, -0.00158478, -91.29071, -0.01191083, -9.129071, -0.03545237, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 87.58583755, 0.00158478, 103.61199145, 0.01191083, 10.36119915, 0.03545237, -87.58583755, -0.00158478, -103.61199145, -0.01191083, -10.36119915, -0.03545237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 108.22879269, 0.03169552, 108.22879269, 0.09508657, 75.76015488, -2021.95421216, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 27.05719817, 0.00011299, 81.17159452, 0.00033897, 270.57198172, 0.00112991, -27.05719817, -0.00011299, -81.17159452, -0.00033897, -270.57198172, -0.00112991, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 108.22879269, 0.03169552, 108.22879269, 0.09508657, 75.76015488, -2021.95421216, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 27.05719817, 0.00011299, 81.17159452, 0.00033897, 270.57198172, 0.00112991, -27.05719817, -0.00011299, -81.17159452, -0.00033897, -270.57198172, -0.00112991, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 2.8)
    ops.node(122001, 0.0, 0.0, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 26674244.54409361, 11114268.560039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 67.32378697, 0.00161112, 80.33429948, 0.01366082, 8.03342995, 0.04225617, -67.32378697, -0.00161112, -80.33429948, -0.01366082, -8.03342995, -0.04225617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 76.46399426, 0.00161112, 91.24087771, 0.01366082, 9.12408777, 0.04225617, -76.46399426, -0.00161112, -91.24087771, -0.01366082, -9.12408777, -0.04225617, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 102.76698814, 0.03222244, 102.76698814, 0.09666733, 71.93689169, -2031.95815368, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 25.69174703, 0.00011096, 77.0752411, 0.00033287, 256.91747034, 0.00110957, -25.69174703, -0.00011096, -77.0752411, -0.00033287, -256.91747034, -0.00110957, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 102.76698814, 0.03222244, 102.76698814, 0.09666733, 71.93689169, -2031.95815368, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 25.69174703, 0.00011096, 77.0752411, 0.00033287, 256.91747034, 0.00110957, -25.69174703, -0.00011096, -77.0752411, -0.00033287, -256.91747034, -0.00110957, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.85, 0.0, 2.725)
    ops.node(122002, 3.85, 0.0, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.12, 26803919.79636461, 11168299.91515192, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 125.67927671, 0.00133758, 150.76782577, 0.01258157, 15.07678258, 0.03349877, -125.67927671, -0.00133758, -150.76782577, -0.01258157, -15.07678258, -0.03349877, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 188.09464352, 0.0010537, 225.64277251, 0.01329187, 22.56427725, 0.03886524, -188.09464352, -0.0010537, -225.64277251, -0.01329187, -22.56427725, -0.03886524, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 140.35327266, 0.02675166, 140.35327266, 0.08025497, 98.24729086, -2111.93390313, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 35.08831817, 7.854e-05, 105.2649545, 0.00023563, 350.88318165, 0.00078544, -35.08831817, -7.854e-05, -105.2649545, -0.00023563, -350.88318165, -0.00078544, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 160.18842177, 0.02107405, 160.18842177, 0.06322215, 112.13189524, -2675.57105992, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 40.04710544, 8.964e-05, 120.14131633, 0.00026893, 400.47105443, 0.00089645, -40.04710544, -8.964e-05, -120.14131633, -0.00026893, -400.47105443, -0.00089645, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 14.5, 0.0, 2.725)
    ops.node(122005, 14.5, 0.0, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.12, 27940958.63968185, 11642066.09986744, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 126.3786385, 0.00128622, 151.6459291, 0.01306769, 15.16459291, 0.03591707, -126.3786385, -0.00128622, -151.6459291, -0.01306769, -15.16459291, -0.03591707, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 189.06209049, 0.00102036, 226.8618867, 0.01384354, 22.68618867, 0.04177918, -189.06209049, -0.00102036, -226.8618867, -0.01384354, -22.68618867, -0.04177918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 145.27512403, 0.02572447, 145.27512403, 0.07717342, 101.69258682, -2132.17589208, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 36.31878101, 7.799e-05, 108.95634302, 0.00023397, 363.18781008, 0.0007799, -36.31878101, -7.799e-05, -108.95634302, -0.00023397, -363.18781008, -0.0007799, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 165.43739661, 0.02040721, 165.43739661, 0.06122163, 115.80617763, -2705.96249056, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 41.35934915, 8.881e-05, 124.07804746, 0.00026644, 413.59349152, 0.00088814, -41.35934915, -8.881e-05, -124.07804746, -0.00026644, -413.59349152, -0.00088814, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 18.35, 0.0, 2.8)
    ops.node(122006, 18.35, 0.0, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.0625, 27117638.0203096, 11299015.84179567, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 66.3312621, 0.00153787, 79.19059683, 0.01370602, 7.91905968, 0.04363201, -66.3312621, -0.00153787, -79.19059683, -0.01370602, -7.91905968, -0.04363201, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 75.46932472, 0.00153787, 90.10021335, 0.01370602, 9.01002134, 0.04363201, -75.46932472, -0.00153787, -90.10021335, -0.01370602, -9.01002134, -0.04363201, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 102.4346131, 0.03075744, 102.4346131, 0.09227232, 71.70422917, -1987.55363145, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 25.60865327, 0.00010879, 76.82595982, 0.00032637, 256.08653274, 0.0010879, -25.60865327, -0.00010879, -76.82595982, -0.00032637, -256.08653274, -0.0010879, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 102.4346131, 0.03075744, 102.4346131, 0.09227232, 71.70422917, -1987.55363145, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 25.60865327, 0.00010879, 76.82595982, 0.00032637, 256.08653274, 0.0010879, -25.60865327, -0.00010879, -76.82595982, -0.00032637, -256.08653274, -0.0010879, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 5.8, 2.8)
    ops.node(122007, 0.0, 5.8, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1575, 26721209.98199302, 11133837.49249709, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 185.40943969, 0.00089349, 223.22843235, 0.01227496, 22.32284324, 0.04119597, -185.40943969, -0.00089349, -223.22843235, -0.01227496, -22.32284324, -0.04119597, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 165.32738785, 0.00106648, 199.05013292, 0.01162458, 19.90501329, 0.03582671, -165.32738785, -0.00106648, -199.05013292, -0.01162458, -19.90501329, -0.03582671, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 218.0188859, 0.01786975, 218.0188859, 0.05360926, 152.61322013, -3486.49968552, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 54.50472147, 9.325e-05, 163.51416442, 0.00027974, 545.04721474, 0.00093246, -54.50472147, -9.325e-05, -163.51416442, -0.00027974, -545.04721474, -0.00093246, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 180.80827557, 0.02132969, 180.80827557, 0.06398908, 126.5657929, -2768.30997749, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 45.20206889, 7.733e-05, 135.60620668, 0.00023199, 452.02068892, 0.00077331, -45.20206889, -7.733e-05, -135.60620668, -0.00023199, -452.02068892, -0.00077331, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 3.85, 5.8, 2.725)
    ops.node(122008, 3.85, 5.8, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.1925, 27102092.29440457, 11292538.4560019, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 340.48336824, 0.00082726, 409.51480684, 0.01296191, 40.95148068, 0.03822803, -340.48336824, -0.00082726, -409.51480684, -0.01296191, -40.95148068, -0.03822803, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 209.86997921, 0.00111929, 252.42015327, 0.01185211, 25.24201533, 0.03073523, -209.86997921, -0.00111929, -252.42015327, -0.01185211, -25.24201533, -0.03073523, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 288.30071026, 0.01654514, 288.30071026, 0.04963542, 201.81049718, -3645.8112163, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 72.07517756, 9.947e-05, 216.22553269, 0.0002984, 720.75177564, 0.00099468, -72.07517756, -9.947e-05, -216.22553269, -0.0002984, -720.75177564, -0.00099468, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 197.65954789, 0.02238584, 197.65954789, 0.06715753, 138.36168352, -2587.02487962, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 49.41488697, 6.82e-05, 148.24466091, 0.00020459, 494.14886971, 0.00068196, -49.41488697, -6.82e-05, -148.24466091, -0.00020459, -494.14886971, -0.00068196, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 7.7, 5.8, 2.725)
    ops.node(122009, 7.7, 5.8, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.21, 27417240.48656357, 11423850.20273482, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 402.24177056, 0.0007737, 484.58555999, 0.01350456, 48.458556, 0.0406255, -402.24177056, -0.0007737, -484.58555999, -0.01350456, -48.458556, -0.0406255, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 198.11690641, 0.00108316, 238.67385006, 0.01210673, 23.86738501, 0.03138037, -198.11690641, -0.00108316, -238.67385006, -0.01210673, -23.86738501, -0.03138037, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 332.90521233, 0.01547395, 332.90521233, 0.04642184, 233.03364863, -4016.39700866, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 83.22630308, 0.00010408, 249.67890925, 0.00031223, 832.26303083, 0.00104076, -83.22630308, -0.00010408, -249.67890925, -0.00031223, -832.26303083, -0.00104076, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 209.48061683, 0.02166325, 209.48061683, 0.06498975, 146.63643178, -2621.1284034, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 52.37015421, 6.549e-05, 157.11046262, 0.00019647, 523.70154208, 0.0006549, -52.37015421, -6.549e-05, -157.11046262, -0.00019647, -523.70154208, -0.0006549, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 10.65, 5.8, 2.725)
    ops.node(122010, 10.65, 5.8, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.21, 27669223.57413147, 11528843.15588811, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 407.25481339, 0.00078613, 490.58072288, 0.01345874, 49.05807229, 0.04100201, -407.25481339, -0.00078613, -490.58072288, -0.01345874, -49.05807229, -0.04100201, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 200.49900543, 0.00110629, 241.52187718, 0.01207942, 24.15218772, 0.03165319, -200.49900543, -0.00110629, -241.52187718, -0.01207942, -24.15218772, -0.03165319, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 334.5310904, 0.01572255, 334.5310904, 0.04716764, 234.17176328, -3987.27595265, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 83.6327726, 0.00010363, 250.8983178, 0.0003109, 836.327726, 0.00103632, -83.6327726, -0.00010363, -250.8983178, -0.0003109, -836.327726, -0.00103632, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 210.59626169, 0.02212588, 210.59626169, 0.06637765, 147.41738318, -2607.39844373, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 52.64906542, 6.524e-05, 157.94719627, 0.00019572, 526.49065423, 0.00065239, -52.64906542, -6.524e-05, -157.94719627, -0.00019572, -526.49065423, -0.00065239, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 14.5, 5.8, 2.725)
    ops.node(122011, 14.5, 5.8, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.1925, 27049902.24789109, 11270792.60328796, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 344.58085064, 0.00083188, 414.44075101, 0.01274719, 41.4440751, 0.03791816, -344.58085064, -0.00083188, -414.44075101, -0.01274719, -41.4440751, -0.03791816, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 212.72154247, 0.00112209, 255.84844792, 0.0116609, 25.58484479, 0.03047291, -212.72154247, -0.00112209, -255.84844792, -0.0116609, -25.58484479, -0.03047291, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 287.04418192, 0.01663759, 287.04418192, 0.04991276, 200.93092735, -3618.71934657, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 71.76104548, 9.923e-05, 215.28313644, 0.00029768, 717.6104548, 0.00099226, -71.76104548, -9.923e-05, -215.28313644, -0.00029768, -717.6104548, -0.00099226, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 196.82809219, 0.02244172, 196.82809219, 0.06732517, 137.77966453, -2572.49555093, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 49.20702305, 6.804e-05, 147.62106914, 0.00020412, 492.07023047, 0.0006804, -49.20702305, -6.804e-05, -147.62106914, -0.00020412, -492.07023047, -0.0006804, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 18.35, 5.8, 2.8)
    ops.node(122012, 18.35, 5.8, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1575, 28037197.21121729, 11682165.50467387, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 185.74436076, 0.00088098, 223.5760455, 0.01269589, 22.35760455, 0.04421414, -185.74436076, -0.00088098, -223.5760455, -0.01269589, -22.35760455, -0.04421414, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 165.0534316, 0.001051, 198.67086883, 0.01201118, 19.86708688, 0.03838676, -165.0534316, -0.001051, -198.67086883, -0.01201118, -19.86708688, -0.03838676, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 225.84005664, 0.01761956, 225.84005664, 0.05285867, 158.08803965, -3506.85060503, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 56.46001416, 9.206e-05, 169.38004248, 0.00027617, 564.60014159, 0.00092057, -56.46001416, -9.206e-05, -169.38004248, -0.00027617, -564.60014159, -0.00092057, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 187.54728232, 0.02101991, 187.54728232, 0.06305972, 131.28309763, -2782.41168689, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 46.88682058, 7.645e-05, 140.66046174, 0.00022935, 468.86820581, 0.00076448, -46.88682058, -7.645e-05, -140.66046174, -0.00022935, -468.86820581, -0.00076448, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 11.6, 2.8)
    ops.node(122013, 0.0, 11.6, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.1575, 27701102.23286538, 11542125.93036058, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 183.22166906, 0.00088236, 220.67037978, 0.01243454, 22.06703798, 0.04372733, -183.22166906, -0.00088236, -220.67037978, -0.01243454, -22.06703798, -0.04372733, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 162.91836627, 0.00105332, 196.21728119, 0.01176979, 19.62172812, 0.0379567, -162.91836627, -0.00105332, -196.21728119, -0.01176979, -19.62172812, -0.0379567, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 220.81269645, 0.01764712, 220.81269645, 0.05294136, 154.56888752, -3424.92461263, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 55.20317411, 9.11e-05, 165.60952234, 0.0002733, 552.03174113, 0.000911, -55.20317411, -9.11e-05, -165.60952234, -0.0002733, -552.03174113, -0.000911, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 183.38140545, 0.02106648, 183.38140545, 0.06319943, 128.36698382, -2716.66712732, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 45.84535136, 7.566e-05, 137.53605409, 0.00022697, 458.45351363, 0.00075657, -45.84535136, -7.566e-05, -137.53605409, -0.00022697, -458.45351363, -0.00075657, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 3.85, 11.6, 2.725)
    ops.node(122014, 3.85, 11.6, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.1925, 27747327.30093216, 11561386.3753884, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 367.05225332, 0.00085243, 441.71526492, 0.01136205, 44.17152649, 0.03358206, -367.05225332, -0.00085243, -441.71526492, -0.01136205, -44.17152649, -0.03358206, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 210.90491875, 0.00116478, 253.80561273, 0.0105854, 25.38056127, 0.02772704, -210.90491875, -0.00116478, -253.80561273, -0.0105854, -25.38056127, -0.02772704, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 268.51207165, 0.01704857, 268.51207165, 0.0511457, 187.95845015, -2898.21334001, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 67.12801791, 9.049e-05, 201.38405373, 0.00027146, 671.28017912, 0.00090487, -67.12801791, -9.049e-05, -201.38405373, -0.00027146, -671.28017912, -0.00090487, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 185.31564843, 0.02329553, 185.31564843, 0.06988658, 129.7209539, -2160.83923546, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 46.32891211, 6.245e-05, 138.98673633, 0.00018735, 463.28912109, 0.0006245, -46.32891211, -6.245e-05, -138.98673633, -0.00018735, -463.28912109, -0.0006245, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.7, 11.6, 2.7)
    ops.node(122015, 7.7, 11.6, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.1925, 27498264.73159692, 11457610.30483205, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 329.88771156, 0.00080365, 397.88168797, 0.01359572, 39.7881688, 0.04183526, -329.88771156, -0.00080365, -397.88168797, -0.01359572, -39.7881688, -0.04183526, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 179.57951072, 0.00107605, 216.59309015, 0.01239034, 21.65930902, 0.0334957, -179.57951072, -0.00107605, -216.59309015, -0.01239034, -21.65930902, -0.0334957, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 284.01443539, 0.01607296, 284.01443539, 0.04821889, 198.81010477, -3639.52586655, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 71.00360885, 9.658e-05, 213.01082654, 0.00028973, 710.03608847, 0.00096578, -71.00360885, -9.658e-05, -213.01082654, -0.00028973, -710.03608847, -0.00096578, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 194.51482616, 0.02152101, 194.51482616, 0.06456303, 136.16037832, -2485.94523417, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 48.62870654, 6.614e-05, 145.88611962, 0.00019843, 486.28706541, 0.00066144, -48.62870654, -6.614e-05, -145.88611962, -0.00019843, -486.28706541, -0.00066144, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 10.65, 11.6, 2.7)
    ops.node(122016, 10.65, 11.6, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1925, 28426418.45423739, 11844341.02259891, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 330.28719017, 0.00079989, 398.10251216, 0.01374399, 39.81025122, 0.04342124, -330.28719017, -0.00079989, -398.10251216, -0.01374399, -39.81025122, -0.04342124, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 180.04667194, 0.00107189, 217.0142668, 0.01252064, 21.70142668, 0.0347005, -180.04667194, -0.00107189, -217.0142668, -0.01252064, -21.70142668, -0.0347005, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 292.80020006, 0.01599789, 292.80020006, 0.04799368, 204.96014004, -3680.48948728, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 73.20005001, 9.631e-05, 219.60015004, 0.00028894, 732.00050015, 0.00096314, -73.20005001, -9.631e-05, -219.60015004, -0.00028894, -732.00050015, -0.00096314, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 200.67004918, 0.02143777, 200.67004918, 0.06431332, 140.46903443, -2507.47540432, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 50.1675123, 6.601e-05, 150.50253689, 0.00019803, 501.67512296, 0.00066009, -50.1675123, -6.601e-05, -150.50253689, -0.00019803, -501.67512296, -0.00066009, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 14.5, 11.6, 2.725)
    ops.node(122017, 14.5, 11.6, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.1925, 27904915.06573193, 11627047.94405497, 0.00475217, 0.00216161, 0.00533786, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 363.3472725, 0.00085873, 437.22970769, 0.01158667, 43.72297077, 0.034025, -363.3472725, -0.00085873, -437.22970769, -0.01158667, -43.72297077, -0.034025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 208.57258111, 0.00118423, 250.9833858, 0.01080055, 25.09833858, 0.0281106, -208.57258111, -0.00118423, -250.9833858, -0.01080055, -25.09833858, -0.0281106, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 270.55425723, 0.01717467, 270.55425723, 0.05152401, 189.38798006, -2920.01600053, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 67.63856431, 9.066e-05, 202.91569292, 0.00027198, 676.38564308, 0.0009066, -67.63856431, -9.066e-05, -202.91569292, -0.00027198, -676.38564308, -0.0009066, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 186.71217904, 0.02368451, 186.71217904, 0.07105353, 130.69852533, -2172.81344429, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 46.67804476, 6.257e-05, 140.03413428, 0.0001877, 466.78044759, 0.00062565, -46.67804476, -6.257e-05, -140.03413428, -0.0001877, -466.78044759, -0.00062565, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 18.35, 11.6, 2.8)
    ops.node(122018, 18.35, 11.6, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.1575, 26928738.82379294, 11220307.84324706, 0.00337604, 0.00176859, 0.00292359, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 180.35499705, 0.00087966, 217.2534646, 0.01253135, 21.72534646, 0.04230931, -180.35499705, -0.00087966, -217.2534646, -0.01253135, -21.72534646, -0.04230931, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 159.94219126, 0.00105186, 192.66444377, 0.01186062, 19.26644438, 0.03677987, -159.94219126, -0.00105186, -192.66444377, -0.01186062, -19.26644438, -0.03677987, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 220.25798768, 0.01759327, 220.25798768, 0.05277982, 154.18059138, -3561.69563257, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 55.06449692, 9.348e-05, 165.19349076, 0.00028043, 550.6449692, 0.00093478, -55.06449692, -9.348e-05, -165.19349076, -0.00028043, -550.6449692, -0.00093478, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 182.5666329, 0.02103714, 182.5666329, 0.06311142, 127.79664303, -2811.29157137, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 45.64165823, 7.748e-05, 136.92497468, 0.00023244, 456.41658226, 0.00077481, -45.64165823, -7.748e-05, -136.92497468, -0.00023244, -456.41658226, -0.00077481, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 17.4, 2.8)
    ops.node(122019, 0.0, 17.4, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.0625, 28178032.43047657, 11740846.84603191, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 68.20398862, 0.00152354, 81.47604521, 0.01393252, 8.14760452, 0.04684658, -68.20398862, -0.00152354, -81.47604521, -0.01393252, -8.14760452, -0.04684658, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 78.00065543, 0.00152354, 93.17908025, 0.01393252, 9.31790802, 0.04684658, -78.00065543, -0.00152354, -93.17908025, -0.01393252, -9.31790802, -0.04684658, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 104.09881475, 0.03047087, 104.09881475, 0.09141261, 72.86917032, -1969.29345185, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 26.02470369, 0.0001064, 78.07411106, 0.00031919, 260.24703687, 0.00106397, -26.02470369, -0.0001064, -78.07411106, -0.00031919, -260.24703687, -0.00106397, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 104.09881475, 0.03047087, 104.09881475, 0.09141261, 72.86917032, -1969.29345185, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 26.02470369, 0.0001064, 78.07411106, 0.00031919, 260.24703687, 0.00106397, -26.02470369, -0.0001064, -78.07411106, -0.00031919, -260.24703687, -0.00106397, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 3.85, 17.4, 2.725)
    ops.node(122020, 3.85, 17.4, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.14, 29280730.9550745, 12200304.56461438, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 162.35018547, 0.00107159, 195.14290891, 0.01333889, 19.51429089, 0.04005585, -162.35018547, -0.00107159, -195.14290891, -0.01333889, -19.51429089, -0.04005585, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 214.47795892, 0.00097065, 257.79984594, 0.01371782, 25.77998459, 0.0429807, -214.47795892, -0.00097065, -257.79984594, -0.01371782, -25.77998459, -0.0429807, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 168.81132426, 0.0214317, 168.81132426, 0.0642951, 118.16792698, -2353.57566131, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 42.20283106, 7.412e-05, 126.60849319, 0.00022237, 422.02831064, 0.00074125, -42.20283106, -7.412e-05, -126.60849319, -0.00022237, -422.02831064, -0.00074125, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 180.11630696, 0.01941303, 180.11630696, 0.0582391, 126.08141487, -2635.92194728, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 45.02907674, 7.909e-05, 135.08723022, 0.00023727, 450.2907674, 0.00079089, -45.02907674, -7.909e-05, -135.08723022, -0.00023727, -450.2907674, -0.00079089, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 7.7, 17.4, 2.7)
    ops.node(122021, 7.7, 17.4, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.105, 27736419.81023252, 11556841.58759688, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 128.11773234, 0.0013195, 153.72293905, 0.01342157, 15.37229391, 0.03802677, -128.11773234, -0.0013195, -153.72293905, -0.01342157, -15.37229391, -0.03802677, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 174.87254852, 0.00115522, 209.82202563, 0.0138315, 20.98220256, 0.0412966, -174.87254852, -0.00115522, -209.82202563, -0.0138315, -20.98220256, -0.0412966, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 132.69172037, 0.02639, 132.69172037, 0.07916999, 92.88420426, -2056.57855015, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 33.17293009, 8.201e-05, 99.51879028, 0.00024604, 331.72930092, 0.00082012, -33.17293009, -8.201e-05, -99.51879028, -0.00024604, -331.72930092, -0.00082012, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 141.57986316, 0.02310448, 141.57986316, 0.06931345, 99.10590421, -2345.82261195, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 35.39496579, 8.751e-05, 106.18489737, 0.00026252, 353.94965789, 0.00087505, -35.39496579, -8.751e-05, -106.18489737, -0.00026252, -353.94965789, -0.00087505, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 10.65, 17.4, 2.7)
    ops.node(122022, 10.65, 17.4, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.105, 28773795.87523847, 11989081.6146827, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 127.72869298, 0.00128603, 153.21112403, 0.01393949, 15.3211124, 0.04034151, -127.72869298, -0.00128603, -153.21112403, -0.01393949, -15.3211124, -0.04034151, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 174.03777295, 0.00112736, 208.75906732, 0.01438118, 20.87590673, 0.04385195, -174.03777295, -0.00112736, -208.75906732, -0.01438118, -20.87590673, -0.04385195, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 136.34251707, 0.02572065, 136.34251707, 0.07716196, 95.43976195, -2063.26143465, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 34.08562927, 8.123e-05, 102.2568878, 0.00024369, 340.85629267, 0.0008123, -34.08562927, -8.123e-05, -102.2568878, -0.00024369, -340.85629267, -0.0008123, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 145.26602125, 0.02254721, 145.26602125, 0.06764162, 101.68621487, -2354.15018048, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 36.31650531, 8.655e-05, 108.94951594, 0.00025964, 363.16505312, 0.00086547, -36.31650531, -8.655e-05, -108.94951594, -0.00025964, -363.16505312, -0.00086547, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 14.5, 17.4, 2.725)
    ops.node(122023, 14.5, 17.4, 4.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.14, 27398926.139446, 11416219.22476917, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 163.26079686, 0.00110096, 196.47550558, 0.01312554, 19.64755056, 0.03709136, -163.26079686, -0.00110096, -196.47550558, -0.01312554, -19.64755056, -0.03709136, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 216.69235365, 0.00099705, 260.77748338, 0.01349201, 26.07774834, 0.03974158, -216.69235365, -0.00099705, -260.77748338, -0.01349201, -26.07774834, -0.03974158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 161.51434468, 0.02201911, 161.51434468, 0.06605733, 113.06004128, -2381.12187421, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 40.37858617, 7.579e-05, 121.13575851, 0.00022738, 403.7858617, 0.00075792, -40.37858617, -7.579e-05, -121.13575851, -0.00022738, -403.7858617, -0.00075792, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 172.74793841, 0.01994105, 172.74793841, 0.05982316, 120.92355689, -2669.24593671, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 43.1869846, 8.106e-05, 129.56095381, 0.00024319, 431.86984603, 0.00081063, -43.1869846, -8.106e-05, -129.56095381, -0.00024319, -431.86984603, -0.00081063, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 18.35, 17.4, 2.8)
    ops.node(122024, 18.35, 17.4, 4.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.0625, 27877473.28220074, 11615613.86758364, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 67.9350721, 0.0015588, 81.14578582, 0.01394723, 8.11457858, 0.04602178, -67.9350721, -0.0015588, -81.14578582, -0.01394723, -8.11457858, -0.04602178, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 77.35206536, 0.0015588, 92.39401584, 0.01394723, 9.23940158, 0.04602178, -77.35206536, -0.0015588, -92.39401584, -0.01394723, -9.23940158, -0.04602178, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 103.63973014, 0.03117598, 103.63973014, 0.09352795, 72.5478111, -1974.71391962, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 25.90993254, 0.00010707, 77.72979761, 0.00032121, 259.09932536, 0.00107069, -25.90993254, -0.00010707, -77.72979761, -0.00032121, -259.09932536, -0.00107069, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 103.63973014, 0.03117598, 103.63973014, 0.09352795, 72.5478111, -1974.71391962, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 25.90993254, 0.00010707, 77.72979761, 0.00032121, 259.09932536, 0.00107069, -25.90993254, -0.00010707, -77.72979761, -0.00032121, -259.09932536, -0.00107069, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.3)
    ops.node(123001, 0.0, 0.0, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 27584856.71586768, 11493690.2982782, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 43.61450812, 0.00140193, 52.58422671, 0.01451855, 5.25842267, 0.05598276, -43.61450812, -0.00140193, -52.58422671, -0.01451855, -5.25842267, -0.05598276, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 43.61450812, 0.00140193, 52.58422671, 0.01451855, 5.25842267, 0.05598276, -43.61450812, -0.00140193, -52.58422671, -0.01451855, -5.25842267, -0.05598276, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 95.2168887, 0.0280386, 95.2168887, 0.08411581, 66.65182209, -2000.22000485, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 23.80422218, 9.941e-05, 71.41266653, 0.00029823, 238.04222176, 0.00099411, -23.80422218, -9.941e-05, -71.41266653, -0.00029823, -238.04222176, -0.00099411, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 95.2168887, 0.0280386, 95.2168887, 0.08411581, 66.65182209, -2000.22000485, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 23.80422218, 9.941e-05, 71.41266653, 0.00029823, 238.04222176, 0.00099411, -23.80422218, -9.941e-05, -71.41266653, -0.00029823, -238.04222176, -0.00099411, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.85, 0.0, 5.225)
    ops.node(123002, 3.85, 0.0, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0875, 27604231.51047998, 11501763.12936666, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 73.99748634, 0.00153854, 88.97421602, 0.01414518, 8.8974216, 0.04009947, -73.99748634, -0.00153854, -88.97421602, -0.01414518, -8.8974216, -0.04009947, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 108.13093794, 0.00113253, 130.01611146, 0.01511883, 13.00161115, 0.04832348, -108.13093794, -0.00113253, -130.01611146, -0.01511883, -13.00161115, -0.04832348, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 108.49733602, 0.03077085, 108.49733602, 0.09231256, 75.94813522, -1699.92141842, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 27.12433401, 8.086e-05, 81.37300202, 0.00024257, 271.24334006, 0.00080855, -27.12433401, -8.086e-05, -81.37300202, -0.00024257, -271.24334006, -0.00080855, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 126.5046632, 0.02265062, 126.5046632, 0.06795185, 88.55326424, -2345.61653461, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 31.6261658, 9.427e-05, 94.8784974, 0.00028282, 316.261658, 0.00094275, -31.6261658, -9.427e-05, -94.8784974, -0.00028282, -316.261658, -0.00094275, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 14.5, 0.0, 5.225)
    ops.node(123005, 14.5, 0.0, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0875, 28376587.9715132, 11823578.32146383, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 72.87796897, 0.00151122, 87.6027326, 0.01382633, 8.76027326, 0.04108612, -72.87796897, -0.00151122, -87.6027326, -0.01382633, -8.76027326, -0.04108612, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 106.54763125, 0.00111027, 128.07524388, 0.01477314, 12.80752439, 0.04964798, -106.54763125, -0.00111027, -128.07524388, -0.01477314, -12.80752439, -0.04964798, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 102.60100633, 0.03022435, 102.60100633, 0.09067304, 71.82070443, -1638.57192446, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 25.65025158, 7.438e-05, 76.95075475, 0.00022314, 256.50251582, 0.0007438, -25.65025158, -7.438e-05, -76.95075475, -0.00022314, -256.50251582, -0.0007438, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 125.97868282, 0.02220533, 125.97868282, 0.066616, 88.18507797, -2244.90321917, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 31.4946707, 9.133e-05, 94.48401211, 0.00027398, 314.94670704, 0.00091327, -31.4946707, -9.133e-05, -94.48401211, -0.00027398, -314.94670704, -0.00091327, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 18.35, 0.0, 5.3)
    ops.node(123006, 18.35, 0.0, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 27810862.23994924, 11587859.26664552, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 43.34695635, 0.00140576, 52.2552984, 0.01515453, 5.22552984, 0.05715515, -43.34695635, -0.00140576, -52.2552984, -0.01515453, -5.22552984, -0.05715515, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 43.34695635, 0.00140576, 52.2552984, 0.01515453, 5.22552984, 0.05715515, -43.34695635, -0.00140576, -52.2552984, -0.01515453, -5.22552984, -0.05715515, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 97.53285957, 0.02811511, 97.53285957, 0.08434532, 68.2730017, -2087.78706655, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 24.38321489, 0.000101, 73.14964468, 0.00030301, 243.83214892, 0.00101002, -24.38321489, -0.000101, -73.14964468, -0.00030301, -243.83214892, -0.00101002, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 97.53285957, 0.02811511, 97.53285957, 0.08434532, 68.2730017, -2087.78706655, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 24.38321489, 0.000101, 73.14964468, 0.00030301, 243.83214892, 0.00101002, -24.38321489, -0.000101, -73.14964468, -0.00030301, -243.83214892, -0.00101002, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 5.8, 5.3)
    ops.node(123007, 0.0, 5.8, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0875, 29172134.69635449, 12155056.12348104, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 95.10171155, 0.00104959, 114.11627433, 0.01390327, 11.41162743, 0.05457727, -95.10171155, -0.00104959, -114.11627433, -0.01390327, -11.41162743, -0.05457727, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 71.01397013, 0.00139956, 85.2124485, 0.01292618, 8.52124485, 0.04433531, -71.01397013, -0.00139956, -85.2124485, -0.01292618, -8.52124485, -0.04433531, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 143.56736442, 0.02099178, 143.56736442, 0.06297533, 100.49715509, -2787.55906771, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 35.8918411, 0.00010124, 107.67552331, 0.00030372, 358.91841105, 0.0010124, -35.8918411, -0.00010124, -107.67552331, -0.00030372, -358.91841105, -0.0010124, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 122.36040821, 0.02799113, 122.36040821, 0.08397339, 85.65228575, -1987.85913516, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 30.59010205, 8.629e-05, 91.77030616, 0.00025886, 305.90102052, 0.00086285, -30.59010205, -8.629e-05, -91.77030616, -0.00025886, -305.90102052, -0.00086285, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 3.85, 5.8, 5.225)
    ops.node(123008, 3.85, 5.8, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.125, 27828952.93729831, 11595397.05720763, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 270.24238399, 0.00090215, 324.6716313, 0.01535932, 32.46716313, 0.0482978, -270.24238399, -0.00090215, -324.6716313, -0.01535932, -32.46716313, -0.0482978, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 155.18116612, 0.00156856, 186.43604903, 0.01337621, 18.6436049, 0.03375365, -155.18116612, -0.00156856, -186.43604903, -0.01337621, -18.6436049, -0.03375365, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 208.15894051, 0.01804307, 208.15894051, 0.05412922, 145.71125836, -3323.92755919, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 52.03973513, 0.00010771, 156.11920538, 0.00032313, 520.39735127, 0.00107711, -52.03973513, -0.00010771, -156.11920538, -0.00032313, -520.39735127, -0.00107711, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 135.78509114, 0.03137121, 135.78509114, 0.09411364, 95.0495638, -1848.74842298, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 33.94627278, 7.026e-05, 101.83881835, 0.00021078, 339.46272785, 0.00070262, -33.94627278, -7.026e-05, -101.83881835, -0.00021078, -339.46272785, -0.00070262, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 7.7, 5.8, 5.225)
    ops.node(123009, 7.7, 5.8, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.125, 26602686.18153297, 11084452.57563874, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 238.54272493, 0.00089708, 286.66671116, 0.01476699, 28.66667112, 0.0452466, -238.54272493, -0.00089708, -286.66671116, -0.01476699, -28.66667112, -0.0452466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 129.37184134, 0.0015725, 155.47152102, 0.01290052, 15.5471521, 0.03175678, -129.37184134, -0.0015725, -155.47152102, -0.01290052, -15.5471521, -0.03175678, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 201.7090297, 0.01794156, 201.7090297, 0.05382469, 141.19632079, -3338.99236568, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 50.42725742, 0.00010918, 151.28177227, 0.00032755, 504.27257424, 0.00109185, -50.42725742, -0.00010918, -151.28177227, -0.00032755, -504.27257424, -0.00109185, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 130.35956276, 0.03145008, 130.35956276, 0.09435024, 91.25169393, -1841.12016522, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 32.58989069, 7.056e-05, 97.76967207, 0.00021169, 325.89890691, 0.00070563, -32.58989069, -7.056e-05, -97.76967207, -0.00021169, -325.89890691, -0.00070563, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 10.65, 5.8, 5.225)
    ops.node(123010, 10.65, 5.8, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.125, 27453647.18005611, 11439019.65835671, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 241.54257042, 0.00091398, 290.32599432, 0.01460861, 29.03259943, 0.0471083, -241.54257042, -0.00091398, -290.32599432, -0.01460861, -29.03259943, -0.0471083, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 129.50489748, 0.00163206, 155.66050351, 0.01281691, 15.56605035, 0.0329229, -129.50489748, -0.00163206, -155.66050351, -0.01281691, -15.56605035, -0.0329229, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 203.04082538, 0.01827964, 203.04082538, 0.05483893, 142.12857777, -3231.07184903, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 50.76020635, 0.0001065, 152.28061904, 0.0003195, 507.60206345, 0.00106499, -50.76020635, -0.0001065, -152.28061904, -0.0003195, -507.60206345, -0.00106499, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 129.28181077, 0.03264118, 129.28181077, 0.09792354, 90.49726754, -1800.94376349, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 32.32045269, 6.781e-05, 96.96135808, 0.00020343, 323.20452692, 0.00067811, -32.32045269, -6.781e-05, -96.96135808, -0.00020343, -323.20452692, -0.00067811, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 14.5, 5.8, 5.225)
    ops.node(123011, 14.5, 5.8, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.125, 28615495.08058058, 11923122.95024191, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 266.92862795, 0.00089984, 320.5866024, 0.0153151, 32.05866024, 0.04995133, -266.92862795, -0.00089984, -320.5866024, -0.0153151, -32.05866024, -0.04995133, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 150.2509364, 0.00159666, 180.45436931, 0.01337009, 18.04543693, 0.03479784, -150.2509364, -0.00159666, -180.45436931, -0.01337009, -18.04543693, -0.03479784, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 209.9654711, 0.01799676, 209.9654711, 0.05399027, 146.97582977, -3243.69616794, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 52.49136777, 0.00010566, 157.47410332, 0.00031698, 524.91367774, 0.0010566, -52.49136777, -0.00010566, -157.47410332, -0.00031698, -524.91367774, -0.0010566, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 135.03973897, 0.03193322, 135.03973897, 0.09579967, 94.52781728, -1818.77054723, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 33.75993474, 6.796e-05, 101.27980423, 0.00020387, 337.59934743, 0.00067955, -33.75993474, -6.796e-05, -101.27980423, -0.00020387, -337.59934743, -0.00067955, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 18.35, 5.8, 5.3)
    ops.node(123012, 18.35, 5.8, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0875, 27539782.31906125, 11474909.29960885, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 93.99631623, 0.00106151, 112.86680887, 0.01349326, 11.28668089, 0.05009715, -93.99631623, -0.00106151, -112.86680887, -0.01349326, -11.28668089, -0.05009715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 70.18246597, 0.00141889, 84.27214268, 0.01256714, 8.42721427, 0.04083327, -70.18246597, -0.00141889, -84.27214268, -0.01256714, -8.42721427, -0.04083327, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 140.22207176, 0.02123022, 140.22207176, 0.06369066, 98.15545023, -2834.72554945, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 35.05551794, 0.00010474, 105.16655382, 0.00031423, 350.5551794, 0.00104742, -35.05551794, -0.00010474, -105.16655382, -0.00031423, -350.5551794, -0.00104742, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 118.68692114, 0.02837788, 118.68692114, 0.08513365, 83.0808448, -2016.29099655, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 29.67173029, 8.866e-05, 89.01519086, 0.00026597, 296.71730285, 0.00088656, -29.67173029, -8.866e-05, -89.01519086, -0.00026597, -296.71730285, -0.00088656, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 11.6, 5.3)
    ops.node(123013, 0.0, 11.6, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0875, 26181098.34604938, 10908790.97752057, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 91.83255036, 0.00109001, 110.26798601, 0.01356806, 11.0267986, 0.04694075, -91.83255036, -0.00109001, -110.26798601, -0.01356806, -11.0267986, -0.04694075, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 68.28786276, 0.0014715, 81.99668927, 0.01266127, 8.19966893, 0.03843221, -68.28786276, -0.0014715, -81.99668927, -0.01266127, -8.19966893, -0.03843221, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 135.44767385, 0.02180015, 135.44767385, 0.06540044, 94.8133717, -2816.61011227, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 33.86191846, 0.00010643, 101.58575539, 0.00031928, 338.61918464, 0.00106426, -33.86191846, -0.00010643, -101.58575539, -0.00031928, -338.61918464, -0.00106426, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 114.08890631, 0.02942996, 114.08890631, 0.08828987, 79.86223442, -1997.36961461, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 28.52222658, 8.964e-05, 85.56667973, 0.00026893, 285.22226578, 0.00089644, -28.52222658, -8.964e-05, -85.56667973, -0.00026893, -285.22226578, -0.00089644, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 3.85, 11.6, 5.225)
    ops.node(123014, 3.85, 11.6, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.125, 27173540.72653969, 11322308.6360582, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 264.91374466, 0.0009315, 318.48305517, 0.01277914, 31.84830552, 0.03871201, -264.91374466, -0.0009315, -318.48305517, -0.01277914, -31.84830552, -0.03871201, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 130.04144307, 0.00167, 156.33766433, 0.01153565, 15.63376643, 0.02833349, -130.04144307, -0.00167, -156.33766433, -0.01153565, -15.63376643, -0.02833349, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 182.24012328, 0.0186299, 182.24012328, 0.05588971, 127.56808629, -2548.8027195, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 45.56003082, 9.657e-05, 136.68009246, 0.00028972, 455.60030819, 0.00096574, -45.56003082, -9.657e-05, -136.68009246, -0.00028972, -455.60030819, -0.00096574, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 89.51591097, 0.03339994, 89.51591097, 0.10019983, 62.66113768, -1535.26030396, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 22.37897774, 4.744e-05, 67.13693323, 0.00014231, 223.78977742, 0.00047437, -22.37897774, -4.744e-05, -67.13693323, -0.00014231, -223.78977742, -0.00047437, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.7, 11.6, 5.2)
    ops.node(123015, 7.7, 11.6, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.125, 26517997.71690856, 11049165.71537857, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 224.20971702, 0.00090028, 270.21846009, 0.01448993, 27.02184601, 0.04751352, -224.20971702, -0.00090028, -270.21846009, -0.01448993, -27.02184601, -0.04751352, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 119.91568459, 0.00157403, 144.52286931, 0.01267315, 14.45228693, 0.03310325, -119.91568459, -0.00157403, -144.52286931, -0.01267315, -14.45228693, -0.03310325, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 194.67830707, 0.01800557, 194.67830707, 0.0540167, 136.27481495, -3292.17899662, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 48.66957677, 0.00010572, 146.00873031, 0.00031715, 486.69576769, 0.00105716, -48.66957677, -0.00010572, -146.00873031, -0.00031715, -486.69576769, -0.00105716, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 122.46576498, 0.03148069, 122.46576498, 0.09444208, 85.72603549, -1741.74947291, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 30.61644124, 6.65e-05, 91.84932373, 0.00019951, 306.16441245, 0.00066502, -30.61644124, -6.65e-05, -91.84932373, -0.00019951, -306.16441245, -0.00066502, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 10.65, 11.6, 5.2)
    ops.node(123016, 10.65, 11.6, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.125, 29899798.5694064, 12458249.40391933, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 223.30484909, 0.00086147, 268.480195, 0.01555073, 26.8480195, 0.05532285, -223.30484909, -0.00086147, -268.480195, -0.01555073, -26.8480195, -0.05532285, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 118.31320497, 0.00150318, 142.24837692, 0.01350038, 14.22483769, 0.03810547, -118.31320497, -0.00150318, -142.24837692, -0.01350038, -14.22483769, -0.03810547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 213.91554135, 0.01722932, 213.91554135, 0.05168796, 149.74087894, -3401.30875859, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 53.47888534, 0.00010302, 160.43665601, 0.00030907, 534.78885337, 0.00103024, -53.47888534, -0.00010302, -160.43665601, -0.00030907, -534.78885337, -0.00103024, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 140.91065999, 0.03006358, 140.91065999, 0.09019075, 98.63746199, -1781.33680114, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 35.227665, 6.786e-05, 105.68299499, 0.00020359, 352.27664997, 0.00067864, -35.227665, -6.786e-05, -105.68299499, -0.00020359, -352.27664997, -0.00067864, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 14.5, 11.6, 5.225)
    ops.node(123017, 14.5, 11.6, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.125, 29353960.10187443, 12230816.70911434, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 268.19591953, 0.00090239, 322.0815333, 0.01270292, 32.20815333, 0.04237327, -268.19591953, -0.00090239, -322.0815333, -0.01270292, -32.20815333, -0.04237327, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 132.29494245, 0.00159076, 158.87548918, 0.01141717, 15.88754892, 0.03063596, -132.29494245, -0.00159076, -158.87548918, -0.01141717, -15.88754892, -0.03063596, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 189.61601653, 0.0180478, 189.61601653, 0.05414341, 132.73121157, -2432.1206357, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 47.40400413, 9.302e-05, 142.2120124, 0.00027906, 474.04004133, 0.00093019, -47.40400413, -9.302e-05, -142.2120124, -0.00027906, -474.04004133, -0.00093019, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 98.01202468, 0.03181519, 98.01202468, 0.09544558, 68.60841727, -1489.79257436, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 24.50300617, 4.808e-05, 73.50901851, 0.00014424, 245.03006169, 0.00048081, -24.50300617, -4.808e-05, -73.50901851, -0.00014424, -245.03006169, -0.00048081, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 18.35, 11.6, 5.3)
    ops.node(123018, 18.35, 11.6, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0875, 28446412.30822515, 11852671.79509382, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 92.16009358, 0.00103446, 110.69180793, 0.01379671, 11.06918079, 0.0532832, -92.16009358, -0.00103446, -110.69180793, -0.01379671, -11.06918079, -0.0532832, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 68.73714439, 0.00138094, 82.55893075, 0.01282556, 8.25589307, 0.04331768, -68.73714439, -0.00138094, -82.55893075, -0.01282556, -8.25589307, -0.04331768, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 137.62967301, 0.02068921, 137.62967301, 0.06206762, 96.3407711, -2655.31937164, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 34.40741825, 9.953e-05, 103.22225475, 0.00029859, 344.07418252, 0.00099529, -34.40741825, -9.953e-05, -103.22225475, -0.00029859, -344.07418252, -0.00099529, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 117.39381734, 0.02761872, 117.39381734, 0.08285615, 82.17567214, -1900.13567168, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 29.34845433, 8.49e-05, 88.045363, 0.00025469, 293.48454335, 0.00084895, -29.34845433, -8.49e-05, -88.045363, -0.00025469, -293.48454335, -0.00084895, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 17.4, 5.3)
    ops.node(123019, 0.0, 17.4, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 27951959.79522955, 11646649.91467898, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 44.02545258, 0.00136323, 53.06851877, 0.01487563, 5.30685188, 0.05720505, -44.02545258, -0.00136323, -53.06851877, -0.01487563, -5.30685188, -0.05720505, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 44.02545258, 0.00136323, 53.06851877, 0.01487563, 5.30685188, 0.05720505, -44.02545258, -0.00136323, -53.06851877, -0.01487563, -5.30685188, -0.05720505, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 97.42619157, 0.02726452, 97.42619157, 0.08179356, 68.1983341, -2070.26061278, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 24.35654789, 0.00010038, 73.06964368, 0.00030115, 243.56547892, 0.00100382, -24.35654789, -0.00010038, -73.06964368, -0.00030115, -243.56547892, -0.00100382, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 97.42619157, 0.02726452, 97.42619157, 0.08179356, 68.1983341, -2070.26061278, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 24.35654789, 0.00010038, 73.06964368, 0.00030115, 243.56547892, 0.00100382, -24.35654789, -0.00010038, -73.06964368, -0.00030115, -243.56547892, -0.00100382, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 3.85, 17.4, 5.225)
    ops.node(123020, 3.85, 17.4, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0875, 28344022.70482242, 11810009.46034267, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 74.64183221, 0.00153218, 89.72465059, 0.01342454, 8.97246506, 0.04063113, -74.64183221, -0.00153218, -89.72465059, -0.01342454, -8.97246506, -0.04063113, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 109.03699559, 0.00112914, 131.07001851, 0.01432299, 13.10700185, 0.04912978, -109.03699559, -0.00112914, -131.07001851, -0.01432299, -13.10700185, -0.04912978, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 104.21737279, 0.03064362, 104.21737279, 0.09193086, 72.95216095, -1641.23762483, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 26.0543432, 7.564e-05, 78.16302959, 0.00022692, 260.54343197, 0.00075639, -26.0543432, -7.564e-05, -78.16302959, -0.00022692, -260.54343197, -0.00075639, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 126.00470745, 0.02258282, 126.00470745, 0.06774845, 88.20329521, -2249.27179651, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 31.50117686, 9.145e-05, 94.50353059, 0.00027435, 315.01176862, 0.00091451, -31.50117686, -9.145e-05, -94.50353059, -0.00027435, -315.01176862, -0.00091451, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 7.7, 17.4, 5.2)
    ops.node(123021, 7.7, 17.4, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.075, 26951226.28414627, 11229677.61839428, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 69.65803228, 0.00155817, 83.72421772, 0.01400014, 8.37242177, 0.04135431, -69.65803228, -0.00155817, -83.72421772, -0.01400014, -8.37242177, -0.04135431, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 85.81649528, 0.00130845, 103.1455914, 0.01448679, 10.31455914, 0.04583834, -85.81649528, -0.00130845, -103.1455914, -0.01448679, -10.31455914, -0.04583834, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 95.32425796, 0.03116339, 95.32425796, 0.09349016, 66.72698057, -1653.80698472, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 23.83106449, 8.489e-05, 71.49319347, 0.00025466, 238.31064489, 0.00084886, -23.83106449, -8.489e-05, -71.49319347, -0.00025466, -238.31064489, -0.00084886, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 106.37827833, 0.02616896, 106.37827833, 0.07850687, 74.46479483, -1976.75122737, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 26.59456958, 9.473e-05, 79.78370875, 0.00028419, 265.94569584, 0.0009473, -26.59456958, -9.473e-05, -79.78370875, -0.00028419, -265.94569584, -0.0009473, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 10.65, 17.4, 5.2)
    ops.node(123022, 10.65, 17.4, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.075, 27286947.98524707, 11369561.66051961, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 69.148288, 0.00155408, 83.11599409, 0.01394756, 8.31159941, 0.04199131, -69.148288, -0.00155408, -83.11599409, -0.01394756, -8.31159941, -0.04199131, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 85.2169178, 0.00130319, 102.43042946, 0.01443018, 10.24304295, 0.04657208, -85.2169178, -0.00130319, -102.43042946, -0.01443018, -10.24304295, -0.04657208, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 94.70425258, 0.03108161, 94.70425258, 0.09324482, 66.2929768, -1677.52464001, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 23.67606314, 8.33e-05, 71.02818943, 0.00024989, 236.76063144, 0.00083296, -23.67606314, -8.33e-05, -71.02818943, -0.00024989, -236.76063144, -0.00083296, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 107.96178632, 0.0260638, 107.96178632, 0.07819139, 75.57325042, -2007.87824239, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 26.99044658, 9.496e-05, 80.97133974, 0.00028487, 269.90446579, 0.00094957, -26.99044658, -9.496e-05, -80.97133974, -0.00028487, -269.90446579, -0.00094957, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 14.5, 17.4, 5.225)
    ops.node(123023, 14.5, 17.4, 7.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.0875, 27786675.74057118, 11577781.55857133, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 74.29313887, 0.0014346, 89.32620241, 0.01383802, 8.93262024, 0.04010901, -74.29313887, -0.0014346, -89.32620241, -0.01383802, -8.93262024, -0.04010901, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 108.03123304, 0.00107401, 129.8911304, 0.01483485, 12.98911304, 0.04844468, -108.03123304, -0.00107401, -129.8911304, -0.01483485, -12.98911304, -0.04844468, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 109.99211211, 0.02869202, 109.99211211, 0.08607606, 76.99447848, -1737.30017204, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 27.49802803, 8.143e-05, 82.49408408, 0.00024429, 274.98028027, 0.00081431, -27.49802803, -8.143e-05, -82.49408408, -0.00024429, -274.98028027, -0.00081431, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 128.57091656, 0.02148026, 128.57091656, 0.06444079, 89.99964159, -2407.15117973, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 32.14272914, 9.519e-05, 96.42818742, 0.00028556, 321.42729139, 0.00095185, -32.14272914, -9.519e-05, -96.42818742, -0.00028556, -321.42729139, -0.00095185, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 18.35, 17.4, 5.3)
    ops.node(123024, 18.35, 17.4, 7.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 27432290.77154844, 11430121.15481185, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 43.75659125, 0.00138584, 52.75908426, 0.01500258, 5.27590843, 0.05609783, -43.75659125, -0.00138584, -52.75908426, -0.01500258, -5.27590843, -0.05609783, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 43.75659125, 0.00138584, 52.75908426, 0.01500258, 5.27590843, 0.05609783, -43.75659125, -0.00138584, -52.75908426, -0.01500258, -5.27590843, -0.05609783, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 97.6047652, 0.0277167, 97.6047652, 0.08315011, 68.32333564, -2124.87526847, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 24.4011913, 0.00010247, 73.2035739, 0.00030741, 244.01191301, 0.00102471, -24.4011913, -0.00010247, -73.2035739, -0.00030741, -244.01191301, -0.00102471, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 97.6047652, 0.0277167, 97.6047652, 0.08315011, 68.32333564, -2124.87526847, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 24.4011913, 0.00010247, 73.2035739, 0.00030741, 244.01191301, 0.00102471, -24.4011913, -0.00010247, -73.2035739, -0.00030741, -244.01191301, -0.00102471, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 7.8)
    ops.node(124001, 0.0, 0.0, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26366582.23586136, 10986075.9316089, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 40.26318674, 0.00133017, 49.16558623, 0.01786251, 4.91655862, 0.07360653, -40.26318674, -0.00133017, -49.16558623, -0.01786251, -4.91655862, -0.07360653, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 44.80700391, 0.00133017, 54.71406496, 0.01786251, 5.4714065, 0.07360653, -44.80700391, -0.00133017, -54.71406496, -0.01786251, -5.4714065, -0.07360653, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 85.38495235, 0.02660349, 85.38495235, 0.07981047, 59.76946665, -3363.92171758, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 21.34623809, 9.327e-05, 64.03871427, 0.0002798, 213.46238089, 0.00093265, -21.34623809, -9.327e-05, -64.03871427, -0.0002798, -213.46238089, -0.00093265, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 85.38495235, 0.02660349, 85.38495235, 0.07981047, 59.76946665, -3363.92171758, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 21.34623809, 9.327e-05, 64.03871427, 0.0002798, 213.46238089, 0.00093265, -21.34623809, -9.327e-05, -64.03871427, -0.0002798, -213.46238089, -0.00093265, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.85, 0.0, 7.725)
    ops.node(124002, 3.85, 0.0, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0875, 29561045.92235452, 12317102.46764771, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 57.56746661, 0.00136889, 69.73390227, 0.01599347, 6.97339023, 0.05374179, -57.56746661, -0.00136889, -69.73390227, -0.01599347, -6.97339023, -0.05374179, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 84.70003974, 0.00102163, 102.60073339, 0.01724671, 10.26007334, 0.06554008, -84.70003974, -0.00102163, -102.60073339, -0.01724671, -10.26007334, -0.06554008, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 97.18563775, 0.02737785, 97.18563775, 0.08213354, 68.02994643, -1801.41790603, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 24.29640944, 6.763e-05, 72.88922831, 0.00020289, 242.96409438, 0.00067631, -24.29640944, -6.763e-05, -72.88922831, -0.00020289, -242.96409438, -0.00067631, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 118.07226793, 0.02043259, 118.07226793, 0.06129777, 82.65058755, -2856.40015326, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 29.51806698, 8.217e-05, 88.55420095, 0.0002465, 295.18066982, 0.00082166, -29.51806698, -8.217e-05, -88.55420095, -0.0002465, -295.18066982, -0.00082166, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 14.5, 0.0, 7.725)
    ops.node(124005, 14.5, 0.0, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0875, 27613911.03063542, 11505796.26276476, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 58.13019745, 0.00139808, 70.66649329, 0.01576897, 7.06664933, 0.05178865, -58.13019745, -0.00139808, -70.66649329, -0.01576897, -7.06664933, -0.05178865, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 85.43571238, 0.00104469, 103.86068621, 0.01698832, 10.38606862, 0.06307015, -85.43571238, -0.00104469, -103.86068621, -0.01698832, -10.38606862, -0.06307015, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 88.03777987, 0.02796164, 88.03777987, 0.08388491, 61.62644591, -1747.05513387, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 22.00944497, 6.559e-05, 66.0283349, 0.00019676, 220.09444968, 0.00065585, -22.00944497, -6.559e-05, -66.0283349, -0.00019676, -220.09444968, -0.00065585, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 111.63588151, 0.02089385, 111.63588151, 0.06268154, 78.14511706, -2760.64551548, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 27.90897038, 8.316e-05, 83.72691113, 0.00024949, 279.08970378, 0.00083165, -27.90897038, -8.316e-05, -83.72691113, -0.00024949, -279.08970378, -0.00083165, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 18.35, 0.0, 7.8)
    ops.node(124006, 18.35, 0.0, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 27744747.66448511, 11560311.5268688, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 39.68720983, 0.00134141, 48.35417327, 0.01732705, 4.83541733, 0.07468823, -39.68720983, -0.00134141, -48.35417327, -0.01732705, -4.83541733, -0.07468823, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 43.80572292, 0.00134141, 53.37209457, 0.01732705, 5.33720946, 0.07468823, -43.80572292, -0.00134141, -53.37209457, -0.01732705, -5.33720946, -0.07468823, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 86.08870897, 0.02682814, 86.08870897, 0.08048442, 60.26209628, -3189.51255453, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 21.52217724, 8.936e-05, 64.56653173, 0.00026809, 215.22177242, 0.00089363, -21.52217724, -8.936e-05, -64.56653173, -0.00026809, -215.22177242, -0.00089363, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 86.08870897, 0.02682814, 86.08870897, 0.08048442, 60.26209628, -3189.51255453, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 21.52217724, 8.936e-05, 64.56653173, 0.00026809, 215.22177242, 0.00089363, -21.52217724, -8.936e-05, -64.56653173, -0.00026809, -215.22177242, -0.00089363, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 5.8, 7.8)
    ops.node(124007, 0.0, 5.8, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0875, 27358059.12289379, 11399191.30120574, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 72.44088445, 0.0010032, 88.12864467, 0.01686755, 8.81286447, 0.07021917, -72.44088445, -0.0010032, -88.12864467, -0.01686755, -8.81286447, -0.07021917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 45.48187531, 0.00135006, 55.33140655, 0.01557651, 5.53314066, 0.05677551, -45.48187531, -0.00135006, -55.33140655, -0.01557651, -5.53314066, -0.05677551, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 127.18209505, 0.02006402, 127.18209505, 0.06019207, 89.02746654, -4060.14079822, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 31.79552376, 9.563e-05, 95.38657129, 0.0002869, 317.95523763, 0.00095632, -31.79552376, -9.563e-05, -95.38657129, -0.0002869, -317.95523763, -0.00095632, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 105.19874494, 0.0270011, 105.19874494, 0.08100331, 73.63912146, -2468.26342781, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 26.29968623, 7.91e-05, 78.8990587, 0.00023731, 262.99686235, 0.00079102, -26.29968623, -7.91e-05, -78.8990587, -0.00023731, -262.99686235, -0.00079102, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 3.85, 5.8, 7.725)
    ops.node(124008, 3.85, 5.8, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.125, 27205570.22213296, 11335654.25922207, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 190.69296108, 0.00084243, 231.56711719, 0.0170416, 23.15671172, 0.06038433, -190.69296108, -0.00084243, -231.56711719, -0.0170416, -23.15671172, -0.06038433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 79.68200546, 0.00147166, 96.76147558, 0.01470206, 9.67614756, 0.0415161, -79.68200546, -0.00147166, -96.76147558, -0.01470206, -9.67614756, -0.0415161, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 185.61340068, 0.01684858, 185.61340068, 0.05054574, 129.92938047, -3894.54205121, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 46.40335017, 9.825e-05, 139.21005051, 0.00029474, 464.03350169, 0.00098246, -46.40335017, -9.825e-05, -139.21005051, -0.00029474, -464.03350169, -0.00098246, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 117.81805157, 0.02943311, 117.81805157, 0.08829933, 82.4726361, -1680.96857274, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 29.45451289, 6.236e-05, 88.36353868, 0.00018708, 294.54512893, 0.00062361, -29.45451289, -6.236e-05, -88.36353868, -0.00018708, -294.54512893, -0.00062361, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 7.7, 5.8, 7.7)
    ops.node(124009, 7.7, 5.8, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.125, 27498258.771178, 11457607.82132417, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 190.8412076, 0.0008393, 231.84400527, 0.01729976, 23.18440053, 0.06210467, -190.8412076, -0.0008393, -231.84400527, -0.01729976, -23.18440053, -0.06210467, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 79.59427314, 0.0014486, 96.69533805, 0.0148924, 9.6695338, 0.04261103, -79.59427314, -0.0014486, -96.69533805, -0.0148924, -9.6695338, -0.04261103, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 187.51037764, 0.01678596, 187.51037764, 0.05035789, 131.25726435, -4168.4862295, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 46.87759441, 9.819e-05, 140.63278323, 0.00029458, 468.7759441, 0.00098193, -46.87759441, -9.819e-05, -140.63278323, -0.00029458, -468.7759441, -0.00098193, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 119.96152571, 0.02897198, 119.96152571, 0.08691593, 83.973068, -1736.47166521, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 29.99038143, 6.282e-05, 89.97114429, 0.00018846, 299.90381428, 0.0006282, -29.99038143, -6.282e-05, -89.97114429, -0.00018846, -299.90381428, -0.0006282, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 10.65, 5.8, 7.7)
    ops.node(124010, 10.65, 5.8, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.125, 28548679.90146926, 11895283.29227886, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 189.35811013, 0.00081729, 229.6697463, 0.01717184, 22.96697463, 0.06335983, -189.35811013, -0.00081729, -229.6697463, -0.01717184, -22.96697463, -0.06335983, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 79.15771646, 0.00139579, 96.00926332, 0.0147531, 9.60092633, 0.04332737, -79.15771646, -0.00139579, -96.00926332, -0.0147531, -9.60092633, -0.04332737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 188.59176978, 0.01634573, 188.59176978, 0.04903718, 132.01423884, -3928.42346379, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 47.14794244, 9.513e-05, 141.44382733, 0.00028538, 471.47942445, 0.00095126, -47.14794244, -9.513e-05, -141.44382733, -0.00028538, -471.47942445, -0.00095126, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 120.18170041, 0.02791588, 120.18170041, 0.08374764, 84.12719029, -1658.74178821, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 30.0454251, 6.062e-05, 90.13627531, 0.00018186, 300.45425102, 0.0006062, -30.0454251, -6.062e-05, -90.13627531, -0.00018186, -300.45425102, -0.0006062, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 14.5, 5.8, 7.725)
    ops.node(124011, 14.5, 5.8, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.125, 28268445.41777076, 11778518.92407115, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 200.06950778, 0.0008326, 242.60537234, 0.01632665, 24.26053723, 0.06121399, -200.06950778, -0.0008326, -242.60537234, -0.01632665, -24.26053723, -0.06121399, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 83.9821968, 0.00140164, 101.8372682, 0.01405615, 10.18372682, 0.04182577, -83.9821968, -0.00140164, -101.8372682, -0.01405615, -10.18372682, -0.04182577, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 187.05021283, 0.0166519, 187.05021283, 0.04995571, 130.93514898, -3689.69332521, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 46.76255321, 9.528e-05, 140.28765962, 0.00028585, 467.62553207, 0.00095284, -46.76255321, -9.528e-05, -140.28765962, -0.00028585, -467.62553207, -0.00095284, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 115.62980402, 0.02803285, 115.62980402, 0.08409855, 80.94086282, -1613.46072197, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 28.90745101, 5.89e-05, 86.72235302, 0.00017671, 289.07451006, 0.00058902, -28.90745101, -5.89e-05, -86.72235302, -0.00017671, -289.07451006, -0.00058902, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 18.35, 5.8, 7.8)
    ops.node(124012, 18.35, 5.8, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0875, 27481665.46781997, 11450693.94492499, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 73.58395695, 0.00099661, 89.50299419, 0.01643072, 8.95029942, 0.06996323, -73.58395695, -0.00099661, -89.50299419, -0.01643072, -8.95029942, -0.06996323, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 46.09992171, 0.00133198, 56.07310609, 0.01517261, 5.60731061, 0.0565113, -46.09992171, -0.00133198, -56.07310609, -0.01517261, -5.60731061, -0.0565113, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 124.7954877, 0.0199322, 124.7954877, 0.05979659, 87.35684139, -3843.80536156, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 31.19887193, 9.342e-05, 93.59661578, 0.00028025, 311.98871925, 0.00093416, -31.19887193, -9.342e-05, -93.59661578, -0.00028025, -311.98871925, -0.00093416, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 103.58209005, 0.02663957, 103.58209005, 0.0799187, 72.50746304, -2347.64233763, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 25.89552251, 7.754e-05, 77.68656754, 0.00023261, 258.95522513, 0.00077536, -25.89552251, -7.754e-05, -77.68656754, -0.00023261, -258.95522513, -0.00077536, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 11.6, 7.8)
    ops.node(124013, 0.0, 11.6, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0875, 25944895.63551983, 10810373.1814666, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 73.79348055, 0.00101237, 89.95456705, 0.01686515, 8.99545671, 0.06841462, -73.79348055, -0.00101237, -89.95456705, -0.01686515, -8.99545671, -0.06841462, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 46.05003392, 0.00135003, 56.13518746, 0.01556612, 5.61351875, 0.05537347, -46.05003392, -0.00135003, -56.13518746, -0.01556612, -5.61351875, -0.05537347, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 122.07627906, 0.0202473, 122.07627906, 0.06074191, 85.45339534, -4031.28279522, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 30.51906977, 9.679e-05, 91.5572093, 0.00029038, 305.19069765, 0.00096793, -30.51906977, -9.679e-05, -91.5572093, -0.00029038, -305.19069765, -0.00096793, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 100.46892757, 0.02700065, 100.46892757, 0.08100196, 70.3282493, -2444.87066097, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 25.11723189, 7.966e-05, 75.35169568, 0.00023898, 251.17231892, 0.00079661, -25.11723189, -7.966e-05, -75.35169568, -0.00023898, -251.17231892, -0.00079661, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 3.85, 11.6, 7.725)
    ops.node(124014, 3.85, 11.6, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.125, 28437746.00914134, 11849060.83714222, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 198.22886438, 0.00086246, 240.37777112, 0.01423048, 24.03777711, 0.05103532, -198.22886438, -0.00086246, -240.37777112, -0.01423048, -24.03777711, -0.05103532, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 90.03940018, 0.00150728, 109.18425223, 0.01263895, 10.91842522, 0.03647905, -90.03940018, -0.00150728, -109.18425223, -0.01263895, -10.91842522, -0.03647905, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 166.86082489, 0.01724923, 166.86082489, 0.0517477, 116.80257743, -2633.270447, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 41.71520622, 8.449e-05, 125.14561867, 0.00025348, 417.15206223, 0.00084493, -41.71520622, -8.449e-05, -125.14561867, -0.00025348, -417.15206223, -0.00084493, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 78.58071413, 0.03014551, 78.58071413, 0.09043652, 55.00649989, -1245.18867573, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 19.64517853, 3.979e-05, 58.93553559, 0.00011937, 196.45178532, 0.00039791, -19.64517853, -3.979e-05, -58.93553559, -0.00011937, -196.45178532, -0.00039791, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.7, 11.6, 7.7)
    ops.node(124015, 7.7, 11.6, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.125, 27229633.27405487, 11345680.5308562, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 164.98982839, 0.00082931, 200.67076091, 0.01632902, 20.06707609, 0.0618339, -164.98982839, -0.00082931, -200.67076091, -0.01632902, -20.06707609, -0.0618339, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 71.37991509, 0.00143019, 86.816636, 0.01408932, 8.6816636, 0.04224098, -71.37991509, -0.00143019, -86.816636, -0.01408932, -8.6816636, -0.04224098, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 177.9353686, 0.01658618, 177.9353686, 0.04975855, 124.55475802, -3904.3931285, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 44.48384215, 9.41e-05, 133.45152645, 0.0002823, 444.83842149, 0.00094099, -44.48384215, -9.41e-05, -133.45152645, -0.0002823, -444.83842149, -0.00094099, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 108.90802917, 0.02860373, 108.90802917, 0.08581119, 76.23562042, -1615.91117294, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 27.22700729, 5.759e-05, 81.68102188, 0.00017278, 272.27007294, 0.00057594, -27.22700729, -5.759e-05, -81.68102188, -0.00017278, -272.27007294, -0.00057594, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 10.65, 11.6, 7.7)
    ops.node(124016, 10.65, 11.6, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.125, 27910660.76253617, 11629441.98439007, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 166.55075991, 0.00081743, 202.3662503, 0.01627123, 20.23662503, 0.06265973, -166.55075991, -0.00081743, -202.3662503, -0.01627123, -20.23662503, -0.06265973, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 72.28644726, 0.00138908, 87.83110499, 0.01401071, 8.7831105, 0.04270902, -72.28644726, -0.00138908, -87.83110499, -0.01401071, -8.7831105, -0.04270902, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 181.21234089, 0.01634851, 181.21234089, 0.04904553, 126.84863863, -3914.42164992, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 45.30308522, 9.349e-05, 135.90925567, 0.00028048, 453.03085223, 0.00093493, -45.30308522, -9.349e-05, -135.90925567, -0.00028048, -453.03085223, -0.00093493, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 111.15836429, 0.02778151, 111.15836429, 0.08334452, 77.81085501, -1619.13652278, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 27.78959107, 5.735e-05, 83.36877322, 0.00017205, 277.89591074, 0.0005735, -27.78959107, -5.735e-05, -83.36877322, -0.00017205, -277.89591074, -0.0005735, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 14.5, 11.6, 7.725)
    ops.node(124017, 14.5, 11.6, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.125, 26159882.08283219, 10899950.86784675, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 196.07998491, 0.00088884, 238.43159573, 0.01395597, 23.84315957, 0.04799567, -196.07998491, -0.00088884, -238.43159573, -0.01395597, -23.84315957, -0.04799567, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 88.71885704, 0.00157503, 107.88137639, 0.01245615, 10.78813764, 0.03450516, -88.71885704, -0.00157503, -107.88137639, -0.01245615, -10.78813764, -0.03450516, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 154.30949306, 0.0177769, 154.30949306, 0.05333069, 108.01664514, -2530.53794307, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 38.57737327, 8.494e-05, 115.7321198, 0.00025482, 385.77373266, 0.00084941, -38.57737327, -8.494e-05, -115.7321198, -0.00025482, -385.77373266, -0.00084941, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 70.4079312, 0.03150067, 70.4079312, 0.09450202, 49.28555184, -1209.77058447, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 17.6019828, 3.876e-05, 52.8059484, 0.00011627, 176.01982799, 0.00038757, -17.6019828, -3.876e-05, -52.8059484, -0.00011627, -176.01982799, -0.00038757, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 18.35, 11.6, 7.8)
    ops.node(124018, 18.35, 11.6, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0875, 28086811.52729093, 11702838.13637122, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 73.55359167, 0.00098539, 89.4016371, 0.01628226, 8.94016371, 0.07105863, -73.55359167, -0.00098539, -89.4016371, -0.01628226, -8.94016371, -0.07105863, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 46.03165373, 0.00131173, 55.94975185, 0.0150293, 5.59497518, 0.05732851, -46.03165373, -0.00131173, -55.94975185, -0.0150293, -5.59497518, -0.05732851, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 125.22658041, 0.01970786, 125.22658041, 0.05912359, 87.65860629, -3856.90968833, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 31.3066451, 9.172e-05, 93.91993531, 0.00027516, 313.06645104, 0.00091719, -31.3066451, -9.172e-05, -93.91993531, -0.00027516, -313.06645104, -0.00091719, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 104.22941166, 0.02623468, 104.22941166, 0.07870404, 72.96058816, -2347.78500122, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 26.05735292, 7.634e-05, 78.17205875, 0.00022902, 260.57352916, 0.0007634, -26.05735292, -7.634e-05, -78.17205875, -0.00022902, -260.57352916, -0.0007634, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 17.4, 7.8)
    ops.node(124019, 0.0, 17.4, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 27499623.79075484, 11458176.57948118, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 39.69336368, 0.00133155, 48.3829593, 0.01801633, 4.83829593, 0.07511206, -39.69336368, -0.00133155, -48.3829593, -0.01801633, -4.83829593, -0.07511206, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 43.89588564, 0.00133155, 53.50548937, 0.01801633, 5.35054894, 0.07511206, -43.89588564, -0.00133155, -53.50548937, -0.01801633, -5.35054894, -0.07511206, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 87.54703179, 0.02663094, 87.54703179, 0.07989282, 61.28292225, -3383.55141702, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 21.88675795, 9.169e-05, 65.66027384, 0.00027506, 218.86757947, 0.00091687, -21.88675795, -9.169e-05, -65.66027384, -0.00027506, -218.86757947, -0.00091687, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 87.54703179, 0.02663094, 87.54703179, 0.07989282, 61.28292225, -3383.55141702, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 21.88675795, 9.169e-05, 65.66027384, 0.00027506, 218.86757947, 0.00091687, -21.88675795, -9.169e-05, -65.66027384, -0.00027506, -218.86757947, -0.00091687, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 3.85, 17.4, 7.725)
    ops.node(124020, 3.85, 17.4, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0875, 27730299.67653756, 11554291.53189065, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 57.01142959, 0.00146389, 69.29423659, 0.01536102, 6.92942366, 0.05149658, -57.01142959, -0.00146389, -69.29423659, -0.01536102, -6.92942366, -0.05149658, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 84.23511921, 0.00107718, 102.38312425, 0.01649519, 10.23831243, 0.06272527, -84.23511921, -0.00107718, -102.38312425, -0.01649519, -10.23831243, -0.06272527, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 88.99682643, 0.02927789, 88.99682643, 0.08783368, 62.2977785, -1754.07226818, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 22.24920661, 6.602e-05, 66.74761983, 0.00019806, 222.49206608, 0.00066021, -22.24920661, -6.602e-05, -66.74761983, -0.00019806, -222.49206608, -0.00066021, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 112.11655955, 0.02154351, 112.11655955, 0.06463054, 78.48159168, -2772.99615174, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 28.02913989, 8.317e-05, 84.08741966, 0.00024952, 280.29139887, 0.00083172, -28.02913989, -8.317e-05, -84.08741966, -0.00024952, -280.29139887, -0.00083172, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 7.7, 17.4, 7.7)
    ops.node(124021, 7.7, 17.4, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.075, 27558125.32389544, 11482552.21828977, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 62.55736767, 0.00151126, 76.05237524, 0.01698303, 7.60523752, 0.05708977, -62.55736767, -0.00151126, -76.05237524, -0.01698303, -7.60523752, -0.05708977, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 82.85023903, 0.00126604, 100.72286771, 0.01765351, 10.07228677, 0.06362122, -82.85023903, -0.00126604, -100.72286771, -0.01765351, -10.07228677, -0.06362122, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 86.37343885, 0.03022511, 86.37343885, 0.09067534, 60.4614072, -1912.45148893, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 21.59335971, 7.522e-05, 64.78007914, 0.00022566, 215.93359713, 0.00075221, -21.59335971, -7.522e-05, -64.78007914, -0.00022566, -215.93359713, -0.00075221, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 97.24269409, 0.02532086, 97.24269409, 0.07596259, 68.06988586, -2470.73819091, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 24.31067352, 8.469e-05, 72.93202057, 0.00025406, 243.10673523, 0.00084687, -24.31067352, -8.469e-05, -72.93202057, -0.00025406, -243.10673523, -0.00084687, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 10.65, 17.4, 7.7)
    ops.node(124022, 10.65, 17.4, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.075, 27419561.66541083, 11424817.36058785, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 63.17906827, 0.00145961, 76.8235842, 0.01657413, 7.68235842, 0.05652272, -63.17906827, -0.00145961, -76.8235842, -0.01657413, -7.68235842, -0.05652272, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 83.82514607, 0.00123107, 101.92850802, 0.01724014, 10.1928508, 0.06302658, -83.82514607, -0.00123107, -101.92850802, -0.01724014, -10.1928508, -0.06302658, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 80.64373909, 0.02919226, 80.64373909, 0.08757677, 56.45061736, -1808.08827371, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 20.16093477, 7.059e-05, 60.48280432, 0.00021176, 201.60934773, 0.00070586, -20.16093477, -7.059e-05, -60.48280432, -0.00021176, -201.60934773, -0.00070586, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 94.78550334, 0.0246214, 94.78550334, 0.07386421, 66.34985234, -2328.50300708, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 23.69637584, 8.296e-05, 71.08912751, 0.00024889, 236.96375836, 0.00082965, -23.69637584, -8.296e-05, -71.08912751, -0.00024889, -236.96375836, -0.00082965, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 14.5, 17.4, 7.725)
    ops.node(124023, 14.5, 17.4, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.0875, 27843225.51297492, 11601343.96373955, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 57.07838468, 0.00148194, 69.36343773, 0.01591169, 6.93634377, 0.05215804, -57.07838468, -0.00148194, -69.36343773, -0.01591169, -6.93634377, -0.05215804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 84.39768677, 0.0010871, 102.56270782, 0.01709603, 10.25627078, 0.06346784, -84.39768677, -0.0010871, -102.56270782, -0.01709603, -10.25627078, -0.06346784, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 97.34339827, 0.02963879, 97.34339827, 0.08891636, 68.14037879, -1887.59775022, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 24.33584957, 7.192e-05, 73.0075487, 0.00021576, 243.35849568, 0.0007192, -24.33584957, -7.192e-05, -73.0075487, -0.00021576, -243.35849568, -0.0007192, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 115.91414031, 0.02174191, 115.91414031, 0.06522574, 81.13989822, -3008.52594908, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 28.97853508, 8.564e-05, 86.93560523, 0.00025692, 289.78535078, 0.00085641, -28.97853508, -8.564e-05, -86.93560523, -0.00025692, -289.78535078, -0.00085641, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 18.35, 17.4, 7.8)
    ops.node(124024, 18.35, 17.4, 9.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 29385691.93850982, 12244038.30771242, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 41.05841284, 0.00126662, 49.85447373, 0.0177868, 4.98544737, 0.07671371, -41.05841284, -0.00126662, -49.85447373, -0.0177868, -4.98544737, -0.07671371, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 45.74740285, 0.00126662, 55.54799944, 0.0177868, 5.55479994, 0.07671371, -45.74740285, -0.00126662, -55.54799944, -0.0177868, -5.55479994, -0.07671371, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 92.02486215, 0.02533238, 92.02486215, 0.07599713, 64.41740351, -3496.83112532, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 23.00621554, 9.019e-05, 69.01864661, 0.00027057, 230.06215538, 0.00090191, -23.00621554, -9.019e-05, -69.01864661, -0.00027057, -230.06215538, -0.00090191, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 92.02486215, 0.02533238, 92.02486215, 0.07599713, 64.41740351, -3496.83112532, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 23.00621554, 9.019e-05, 69.01864661, 0.00027057, 230.06215538, 0.00090191, -23.00621554, -9.019e-05, -69.01864661, -0.00027057, -230.06215538, -0.00090191, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 7.7, 0.0, 0.0)
    ops.node(124025, 7.7, 0.0, 1.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.14, 26746104.96671351, 11144210.40279729, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 286.77594391, 0.00094663, 341.87064159, 0.01428107, 34.18706416, 0.0338677, -286.77594391, -0.00094663, -341.87064159, -0.01428107, -34.18706416, -0.0338677, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 261.93695438, 0.00088114, 312.25964573, 0.01476832, 31.22596457, 0.03633595, -261.93695438, -0.00088114, -312.25964573, -0.01476832, -31.22596457, -0.03633595, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 269.39330567, 0.01893266, 269.39330567, 0.05679797, 188.57531397, -5897.30438564, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 67.34832642, 6.475e-05, 202.04497925, 0.00019425, 673.48326417, 0.0006475, -67.34832642, -6.475e-05, -202.04497925, -0.00019425, -673.48326417, -0.0006475, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 302.61041506, 0.01762271, 302.61041506, 0.05286814, 211.82729054, -6515.54783837, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 75.65260377, 7.273e-05, 226.9578113, 0.0002182, 756.52603766, 0.00072734, -75.65260377, -7.273e-05, -226.9578113, -0.0002182, -756.52603766, -0.00072734, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 7.7, 0.0, 1.5)
    ops.node(121003, 7.7, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.14, 27334418.72312696, 11389341.13463623, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 203.37158933, 0.00090603, 243.12819783, 0.01476287, 24.31281978, 0.03695082, -203.37158933, -0.00090603, -243.12819783, -0.01476287, -24.31281978, -0.03695082, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 235.07172884, 0.00084662, 281.02531913, 0.01527787, 28.10253191, 0.03970992, -235.07172884, -0.00084662, -281.02531913, -0.01527787, -28.10253191, -0.03970992, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 272.54948132, 0.01812065, 272.54948132, 0.05436195, 190.78463693, -6002.60196315, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 68.13737033, 6.41e-05, 204.41211099, 0.0001923, 681.37370331, 0.00064099, -68.13737033, -6.41e-05, -204.41211099, -0.0001923, -681.37370331, -0.00064099, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 306.23560351, 0.01693247, 306.23560351, 0.0507974, 214.36492246, -6687.9591704, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 76.55890088, 7.202e-05, 229.67670263, 0.00021606, 765.58900877, 0.00072021, -76.55890088, -7.202e-05, -229.67670263, -0.00021606, -765.58900877, -0.00072021, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 10.65, 0.0, 0.0)
    ops.node(124026, 10.65, 0.0, 1.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.14, 26333446.51420285, 10972269.38091785, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 284.290144, 0.00095084, 338.68824413, 0.01427081, 33.86882441, 0.03296745, -284.290144, -0.00095084, -338.68824413, -0.01427081, -33.86882441, -0.03296745, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 259.92367953, 0.00088437, 309.65932687, 0.01475649, 30.96593269, 0.03534411, -259.92367953, -0.00088437, -309.65932687, -0.01475649, -30.96593269, -0.03534411, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 268.05835134, 0.01901679, 268.05835134, 0.05705036, 187.64084594, -6012.34844406, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 67.01458783, 6.544e-05, 201.0437635, 0.00019632, 670.14587835, 0.00065439, -67.01458783, -6.544e-05, -201.0437635, -0.00019632, -670.14587835, -0.00065439, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 301.17336815, 0.01768735, 301.17336815, 0.05306204, 210.8213577, -6653.80508072, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 75.29334204, 7.352e-05, 225.88002611, 0.00022057, 752.93342037, 0.00073523, -75.29334204, -7.352e-05, -225.88002611, -0.00022057, -752.93342037, -0.00073523, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 10.65, 0.0, 1.5)
    ops.node(121004, 10.65, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.14, 28272746.168736, 11780310.90364, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 205.62558227, 0.00090231, 245.91124294, 0.01492349, 24.59112429, 0.0389534, -205.62558227, -0.00090231, -245.91124294, -0.01492349, -24.59112429, -0.0389534, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 237.6670627, 0.00084356, 284.23021176, 0.01544596, 28.42302118, 0.04190626, -237.6670627, -0.00084356, -284.23021176, -0.01544596, -28.42302118, -0.04190626, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 280.06351224, 0.01804621, 280.06351224, 0.05413863, 196.04445857, -6000.31089232, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 70.01587806, 6.368e-05, 210.04763418, 0.00019104, 700.15878059, 0.0006368, -70.01587806, -6.368e-05, -210.04763418, -0.00019104, -700.15878059, -0.0006368, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 314.620792, 0.01687128, 314.620792, 0.05061385, 220.2345544, -6685.1953866, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 78.655198, 7.154e-05, 235.965594, 0.00021461, 786.55198, 0.00071538, -78.655198, -7.154e-05, -235.965594, -0.00021461, -786.55198, -0.00071538, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.7, 0.0, 2.7)
    ops.node(124027, 7.7, 0.0, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.14, 28076030.86234329, 11698346.19264304, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 157.49624143, 0.00087858, 189.19367265, 0.01272505, 18.91936726, 0.03657855, -157.49624143, -0.00087858, -189.19367265, -0.01272505, -18.91936726, -0.03657855, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 198.13929222, 0.00082252, 238.01647615, 0.01313239, 23.80164762, 0.03925895, -198.13929222, -0.00082252, -238.01647615, -0.01313239, -23.80164762, -0.03925895, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 251.07614092, 0.01757167, 251.07614092, 0.05271501, 175.75329864, -4879.27451786, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 62.76903523, 5.749e-05, 188.30710569, 0.00017247, 627.6903523, 0.00057489, -62.76903523, -5.749e-05, -188.30710569, -0.00017247, -627.6903523, -0.00057489, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 281.89057305, 0.01645038, 281.89057305, 0.04935115, 197.32340114, -5440.7340205, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 70.47264326, 6.454e-05, 211.41792979, 0.00019363, 704.72643263, 0.00064545, -70.47264326, -6.454e-05, -211.41792979, -0.00019363, -704.72643263, -0.00064545, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 7.7, 0.0, 4.0)
    ops.node(122003, 7.7, 0.0, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.14, 27086421.4415645, 11286008.93398521, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 149.94586327, 0.00088837, 180.53672048, 0.012855, 18.05367205, 0.03663273, -149.94586327, -0.00088837, -180.53672048, -0.012855, -18.05367205, -0.03663273, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 189.29375501, 0.00083051, 227.91208102, 0.01326525, 22.7912081, 0.03930881, -189.29375501, -0.00083051, -227.91208102, -0.01326525, -22.7912081, -0.03930881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 236.32888178, 0.01776736, 236.32888178, 0.05330209, 165.43021724, -4713.94534252, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 59.08222044, 5.609e-05, 177.24666133, 0.00016827, 590.82220444, 0.00056089, -59.08222044, -5.609e-05, -177.24666133, -0.00016827, -590.82220444, -0.00056089, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 265.40586138, 0.01661024, 265.40586138, 0.04983072, 185.78410296, -5290.09960487, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 66.35146534, 6.299e-05, 199.05439603, 0.00018897, 663.51465344, 0.0006299, -66.35146534, -6.299e-05, -199.05439603, -0.00018897, -663.51465344, -0.0006299, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 10.65, 0.0, 2.7)
    ops.node(124028, 10.65, 0.0, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.14, 27562041.95944459, 11484184.14976858, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 157.48682056, 0.00089531, 189.20014409, 0.01246777, 18.92001441, 0.03549958, -157.48682056, -0.00089531, -189.20014409, -0.01246777, -18.92001441, -0.03549958, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 198.10542441, 0.00083655, 237.99816841, 0.0128617, 23.79981684, 0.03808826, -198.10542441, -0.00083655, -237.99816841, -0.0128617, -23.79981684, -0.03808826, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 245.77379804, 0.01790611, 245.77379804, 0.05371832, 172.04165863, -4800.36968859, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 61.44344951, 5.732e-05, 184.33034853, 0.00017197, 614.4344951, 0.00057324, -61.44344951, -5.732e-05, -184.33034853, -0.00017197, -614.4344951, -0.00057324, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 275.93813872, 0.016731, 275.93813872, 0.05019301, 193.15669711, -5345.54190546, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 68.98453468, 6.436e-05, 206.95360404, 0.00019308, 689.8453468, 0.0006436, -68.98453468, -6.436e-05, -206.95360404, -0.00019308, -689.8453468, -0.0006436, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 10.65, 0.0, 4.0)
    ops.node(122004, 10.65, 0.0, 4.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.14, 28044937.45338374, 11685390.60557656, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 147.12501269, 0.00084395, 177.09065686, 0.01296712, 17.70906569, 0.03823405, -147.12501269, -0.00084395, -177.09065686, -0.01296712, -17.70906569, -0.03823405, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 185.48629667, 0.00079217, 223.26516419, 0.01338957, 22.32651642, 0.04106423, -185.48629667, -0.00079217, -223.26516419, -0.01338957, -22.32651642, -0.04106423, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 243.41669516, 0.016879, 243.41669516, 0.05063699, 170.39168661, -4697.89536576, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 60.85417379, 5.58e-05, 182.56252137, 0.00016739, 608.5417379, 0.00055797, -60.85417379, -5.58e-05, -182.56252137, -0.00016739, -608.5417379, -0.00055797, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 273.30961706, 0.0158433, 273.30961706, 0.04752991, 191.31673195, -5270.66942517, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 68.32740427, 6.265e-05, 204.9822128, 0.00018795, 683.27404266, 0.00062649, -68.32740427, -6.265e-05, -204.9822128, -0.00018795, -683.27404266, -0.00062649, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.7, 0.0, 5.2)
    ops.node(124029, 7.7, 0.0, 6.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.0875, 28085150.79333648, 11702146.1638902, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 98.49714597, 0.00111124, 118.22477739, 0.01365429, 11.82247774, 0.03917547, -98.49714597, -0.00111124, -118.22477739, -0.01365429, -11.82247774, -0.03917547, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 130.33273111, 0.00088652, 156.4365949, 0.01480228, 15.64365949, 0.04745283, -130.33273111, -0.00088652, -156.4365949, -0.01480228, -15.64365949, -0.04745283, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 125.2570461, 0.02222474, 125.2570461, 0.06667423, 87.67993227, -3385.72421133, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 31.31426153, 4.587e-05, 93.94278458, 0.00013762, 313.14261526, 0.00045873, -31.31426153, -4.587e-05, -93.94278458, -0.00013762, -313.14261526, -0.00045873, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 181.05900912, 0.01773031, 181.05900912, 0.05319094, 126.74130638, -4588.29467158, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 45.26475228, 6.631e-05, 135.79425684, 0.00019893, 452.6475228, 0.0006631, -45.26475228, -6.631e-05, -135.79425684, -0.00019893, -452.6475228, -0.0006631, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 7.7, 0.0, 6.475)
    ops.node(123003, 7.7, 0.0, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.0875, 26955228.12887306, 11231345.05369711, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 71.56837678, 0.00113453, 86.23131414, 0.01337681, 8.62313141, 0.03974639, -71.56837678, -0.00113453, -86.23131414, -0.01337681, -8.62313141, -0.03974639, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 104.74767742, 0.00089767, 126.20839377, 0.01447974, 12.62083938, 0.0482157, -104.74767742, -0.00089767, -126.20839377, -0.01447974, -12.62083938, -0.0482157, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 113.84301343, 0.02269061, 113.84301343, 0.06807182, 79.6901094, -3229.03209662, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 28.46075336, 4.344e-05, 85.38226007, 0.00013032, 284.60753358, 0.00043441, -28.46075336, -4.344e-05, -85.38226007, -0.00013032, -284.60753358, -0.00043441, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 167.5619515, 0.01795343, 167.5619515, 0.0538603, 117.29336605, -4503.36562623, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 41.89048787, 6.394e-05, 125.67146362, 0.00019182, 418.90487874, 0.00063939, -41.89048787, -6.394e-05, -125.67146362, -0.00019182, -418.90487874, -0.00063939, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 10.65, 0.0, 5.2)
    ops.node(124030, 10.65, 0.0, 6.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.0875, 28738690.54415097, 11974454.39339624, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 95.93050168, 0.00111628, 115.11277226, 0.01373769, 11.51127723, 0.04036587, -95.93050168, -0.00111628, -115.11277226, -0.01373769, -11.51127723, -0.04036587, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 128.07097984, 0.0008834, 153.68006292, 0.01488609, 15.36800629, 0.04895289, -128.07097984, -0.0008834, -153.68006292, -0.01488609, -15.36800629, -0.04895289, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 125.68410423, 0.02232556, 125.68410423, 0.06697667, 87.97887296, -3354.35133246, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 31.42102606, 4.498e-05, 94.26307817, 0.00013495, 314.21026057, 0.00044983, -31.42102606, -4.498e-05, -94.26307817, -0.00013495, -314.21026057, -0.00044983, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 183.59657181, 0.01766793, 183.59657181, 0.05300378, 128.51760027, -4537.1880206, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 45.89914295, 6.571e-05, 137.69742886, 0.00019713, 458.99142952, 0.0006571, -45.89914295, -6.571e-05, -137.69742886, -0.00019713, -458.99142952, -0.0006571, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 10.65, 0.0, 6.475)
    ops.node(123004, 10.65, 0.0, 7.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.0875, 28380725.09280906, 11825302.12200378, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 70.58085013, 0.00108345, 84.98994175, 0.01421045, 8.49899418, 0.04293768, -70.58085013, -0.00108345, -84.98994175, -0.01421045, -8.49899418, -0.04293768, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 103.26180594, 0.00086212, 124.34271982, 0.01542572, 12.43427198, 0.05217794, -103.26180594, -0.00086212, -124.34271982, -0.01542572, -12.43427198, -0.05217794, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 125.56789948, 0.02166905, 125.56789948, 0.06500714, 87.89752964, -3366.98548595, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 31.39197487, 4.551e-05, 94.17592461, 0.00013652, 313.91974871, 0.00045508, -31.39197487, -4.551e-05, -94.17592461, -0.00013652, -313.91974871, -0.00045508, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 177.17429136, 0.01724238, 177.17429136, 0.05172715, 124.02200395, -4731.89103549, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 44.29357284, 6.421e-05, 132.88071852, 0.00019263, 442.9357284, 0.00064211, -44.29357284, -6.421e-05, -132.88071852, -0.00019263, -442.9357284, -0.00064211, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.7, 0.0, 7.7)
    ops.node(124031, 7.7, 0.0, 8.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.0875, 26829685.76651913, 11179035.73604964, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 59.46477358, 0.00104388, 72.31820843, 0.01562097, 7.23182084, 0.05013076, -59.46477358, -0.00104388, -72.31820843, -0.01562097, -7.23182084, -0.05013076, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 87.2724247, 0.00084115, 106.13654134, 0.01701356, 10.61365413, 0.06116371, -87.2724247, -0.00084115, -106.13654134, -0.01701356, -10.61365413, -0.06116371, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 106.09508857, 0.02087754, 106.09508857, 0.06263261, 74.266562, -3597.06071638, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 26.52377214, 4.067e-05, 79.57131643, 0.00012202, 265.23772142, 0.00040674, -26.52377214, -4.067e-05, -79.57131643, -0.00012202, -265.23772142, -0.00040674, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 152.50864509, 0.01682309, 152.50864509, 0.05046928, 106.75605156, -5654.47003425, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 38.12716127, 5.847e-05, 114.38148382, 0.0001754, 381.27161272, 0.00058467, -38.12716127, -5.847e-05, -114.38148382, -0.0001754, -381.27161272, -0.00058467, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 7.7, 0.0, 8.95)
    ops.node(124003, 7.7, 0.0, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.0875, 28685284.4072923, 11952201.83637179, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 53.96333905, 0.00100077, 65.65557032, 0.01619061, 6.56555703, 0.05623438, -53.96333905, -0.00100077, -65.65557032, -0.01619061, -6.56555703, -0.05623438, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 79.55313055, 0.00081011, 96.78989939, 0.01766231, 9.67898994, 0.06889237, -79.55313055, -0.00081011, -96.78989939, -0.01766231, -9.67898994, -0.06889237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 104.01628823, 0.02001541, 104.01628823, 0.06004624, 72.81140176, -4270.35826453, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 26.00407206, 3.73e-05, 78.01221617, 0.00011189, 260.04072058, 0.00037297, -26.00407206, -3.73e-05, -78.01221617, -0.00011189, -260.04072058, -0.00037297, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 150.476022, 0.01620224, 150.476022, 0.04860673, 105.3332154, -7202.10097565, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 37.6190055, 5.396e-05, 112.8570165, 0.00016187, 376.190055, 0.00053956, -37.6190055, -5.396e-05, -112.8570165, -0.00016187, -376.190055, -0.00053956, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 10.65, 0.0, 7.7)
    ops.node(124032, 10.65, 0.0, 8.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.0875, 28300095.56479199, 11791706.48532999, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 57.95131241, 0.00104344, 70.33241785, 0.01577272, 7.03324179, 0.05185534, -57.95131241, -0.00104344, -70.33241785, -0.01577272, -7.03324179, -0.05185534, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 85.43793207, 0.0008341, 103.69146252, 0.01717535, 10.36914625, 0.06333769, -85.43793207, -0.0008341, -103.69146252, -0.01717535, -10.36914625, -0.06333769, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 111.32712176, 0.02086884, 111.32712176, 0.06260653, 77.92898523, -3531.22143531, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 27.83178044, 4.046e-05, 83.49534132, 0.00012139, 278.31780439, 0.00040462, -27.83178044, -4.046e-05, -83.49534132, -0.00012139, -278.31780439, -0.00040462, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 158.22817072, 0.01668204, 158.22817072, 0.05004613, 110.75971951, -5538.96491966, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 39.55704268, 5.751e-05, 118.67112804, 0.00017252, 395.57042681, 0.00057508, -39.55704268, -5.751e-05, -118.67112804, -0.00017252, -395.57042681, -0.00057508, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 10.65, 0.0, 8.95)
    ops.node(124004, 10.65, 0.0, 9.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.0875, 28441322.78929318, 11850551.16220549, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 53.5012102, 0.00099526, 65.1271801, 0.01626813, 6.51271801, 0.05616783, -53.5012102, -0.00099526, -65.1271801, -0.01626813, -6.51271801, -0.05616783, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 78.87199533, 0.00080616, 96.01111125, 0.01775048, 9.60111112, 0.06879622, -78.87199533, -0.00080616, -96.01111125, -0.01775048, -9.60111112, -0.06879622, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 103.53474126, 0.01990511, 103.53474126, 0.05971534, 72.47431888, -4354.82448799, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 25.88368531, 3.744e-05, 77.65105594, 0.00011233, 258.83685314, 0.00037443, -25.88368531, -3.744e-05, -77.65105594, -0.00011233, -258.83685314, -0.00037443, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 150.17277718, 0.01612316, 150.17277718, 0.04836948, 105.12094403, -7355.73042108, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 37.5431943, 5.431e-05, 112.62958289, 0.00016293, 375.43194296, 0.0005431, -37.5431943, -5.431e-05, -112.62958289, -0.00016293, -375.43194296, -0.0005431, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
