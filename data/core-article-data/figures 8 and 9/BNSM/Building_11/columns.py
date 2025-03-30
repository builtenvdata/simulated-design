import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(121003, 9.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.2025, 26164800.56154356, 10902000.23397648, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 314.67048161, 0.000913, 374.3749421, 0.01128641, 37.43749421, 0.0257991, -314.67048161, -0.000913, -374.3749421, -0.01128641, -37.43749421, -0.0257991, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 352.64872346, 0.000913, 419.5590408, 0.01128641, 41.95590408, 0.0257991, -352.64872346, -0.000913, -419.5590408, -0.01128641, -41.95590408, -0.0257991, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 220.59601217, 0.01825997, 220.59601217, 0.05477992, 154.41720852, -2540.78005559, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 55.14900304, 9.443e-05, 165.44700912, 0.00028328, 551.49003042, 0.00094427, -55.14900304, -9.443e-05, -165.44700912, -0.00028328, -551.49003042, -0.00094427, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 220.59601217, 0.01825997, 220.59601217, 0.05477992, 154.41720852, -2540.78005559, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 55.14900304, 9.443e-05, 165.44700912, 0.00028328, 551.49003042, 0.00094427, -55.14900304, -9.443e-05, -165.44700912, -0.00028328, -551.49003042, -0.00094427, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 14.95, 0.0, 0.0)
    ops.node(121004, 14.95, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.09, 27840449.32158704, 11600187.21732793, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 131.2015177, 0.00131165, 155.32420182, 0.01284419, 15.53242018, 0.03139394, -131.2015177, -0.00131165, -155.32420182, -0.01284419, -15.53242018, -0.03139394, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 120.29048552, 0.00131165, 142.40706949, 0.01284419, 14.24070695, 0.03139394, -120.29048552, -0.00131165, -142.40706949, -0.01284419, -14.24070695, -0.03139394, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 124.37750451, 0.02623308, 124.37750451, 0.07869925, 87.06425316, -1579.68441302, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 31.09437613, 0.00011258, 93.28312838, 0.00033774, 310.94376128, 0.00112581, -31.09437613, -0.00011258, -93.28312838, -0.00033774, -310.94376128, -0.00112581, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 124.37750451, 0.02623308, 124.37750451, 0.07869925, 87.06425316, -1579.68441302, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 31.09437613, 0.00011258, 93.28312838, 0.00033774, 310.94376128, 0.00112581, -31.09437613, -0.00011258, -93.28312838, -0.00033774, -310.94376128, -0.00112581, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 3.95, 0.0)
    ops.node(121005, 0.0, 3.95, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.09, 27601235.31822017, 11500514.71592507, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 92.20694085, 0.0012159, 109.75096848, 0.01253789, 10.97509685, 0.03707771, -92.20694085, -0.0012159, -109.75096848, -0.01253789, -10.97509685, -0.03707771, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 87.02089024, 0.0012159, 103.57817854, 0.01253789, 10.35781785, 0.03707771, -87.02089024, -0.0012159, -103.57817854, -0.01253789, -10.35781785, -0.03707771, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 125.20518013, 0.024318, 125.20518013, 0.07295399, 87.64362609, -1616.89781976, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 31.30129503, 0.00011431, 93.9038851, 0.00034294, 313.01295033, 0.00114313, -31.30129503, -0.00011431, -93.9038851, -0.00034294, -313.01295033, -0.00114313, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 125.20518013, 0.024318, 125.20518013, 0.07295399, 87.64362609, -1616.89781976, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 31.30129503, 0.00011431, 93.9038851, 0.00034294, 313.01295033, 0.00114313, -31.30129503, -0.00011431, -93.9038851, -0.00034294, -313.01295033, -0.00114313, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 3.05, 3.95, 0.0)
    ops.node(121006, 3.05, 3.95, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.25, 27569694.28155567, 11487372.61731486, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 462.57061538, 0.00086172, 554.29823929, 0.01156701, 55.42982393, 0.02724296, -462.57061538, -0.00086172, -554.29823929, -0.01156701, -55.42982393, -0.02724296, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 481.11447173, 0.00086172, 576.51933719, 0.01156701, 57.65193372, 0.02724296, -481.11447173, -0.00086172, -576.51933719, -0.01156701, -57.65193372, -0.02724296, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 249.50448408, 0.01723441, 249.50448408, 0.05170322, 174.65313886, -2377.80300081, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 62.37612102, 8.21e-05, 187.12836306, 0.0002463, 623.76121021, 0.00082101, -62.37612102, -8.21e-05, -187.12836306, -0.0002463, -623.76121021, -0.00082101, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 249.50448408, 0.01723441, 249.50448408, 0.05170322, 174.65313886, -2377.80300081, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 62.37612102, 8.21e-05, 187.12836306, 0.0002463, 623.76121021, 0.00082101, -62.37612102, -8.21e-05, -187.12836306, -0.0002463, -623.76121021, -0.00082101, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 9.0, 3.95, 0.0)
    ops.node(121007, 9.0, 3.95, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.3025, 27373518.03730932, 11405632.51554555, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 679.08687605, 0.00081843, 811.92191697, 0.01114339, 81.1921917, 0.02488776, -679.08687605, -0.00081843, -811.92191697, -0.01114339, -81.1921917, -0.02488776, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 742.33920978, 0.00081843, 887.54693324, 0.01114339, 88.75469332, 0.02488776, -742.33920978, -0.00081843, -887.54693324, -0.01114339, -88.75469332, -0.02488776, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 323.30666117, 0.01636866, 323.30666117, 0.04910598, 226.31466282, -2889.93227426, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 80.82666529, 8.855e-05, 242.47999588, 0.00026566, 808.26665294, 0.00088553, -80.82666529, -8.855e-05, -242.47999588, -0.00026566, -808.26665294, -0.00088553, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 323.30666117, 0.01636866, 323.30666117, 0.04910598, 226.31466282, -2889.93227426, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 80.82666529, 8.855e-05, 242.47999588, 0.00026566, 808.26665294, 0.00088553, -80.82666529, -8.855e-05, -242.47999588, -0.00026566, -808.26665294, -0.00088553, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 14.95, 3.95, 0.0)
    ops.node(121008, 14.95, 3.95, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.16, 27058245.626104, 11274269.01087667, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 309.13713185, 0.0010589, 366.80936125, 0.01068512, 36.68093612, 0.02348715, -309.13713185, -0.0010589, -366.80936125, -0.01068512, -36.68093612, -0.02348715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 294.34636733, 0.0010589, 349.25925054, 0.01068512, 34.92592505, 0.02348715, -294.34636733, -0.0010589, -349.25925054, -0.01068512, -34.92592505, -0.02348715, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 177.77442874, 0.02117792, 177.77442874, 0.06353375, 124.44210012, -2017.9810542, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 44.44360719, 9.313e-05, 133.33082156, 0.00027939, 444.43607185, 0.00093131, -44.44360719, -9.313e-05, -133.33082156, -0.00027939, -444.43607185, -0.00093131, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 177.77442874, 0.02117792, 177.77442874, 0.06353375, 124.44210012, -2017.9810542, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 44.44360719, 9.313e-05, 133.33082156, 0.00027939, 444.43607185, 0.00093131, -44.44360719, -9.313e-05, -133.33082156, -0.00027939, -444.43607185, -0.00093131, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 7.9, 0.0)
    ops.node(121009, 0.0, 7.9, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.09, 27990151.46102585, 11662563.10876077, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 94.43046767, 0.00122464, 112.29360194, 0.01279209, 11.22936019, 0.03735658, -94.43046767, -0.00122464, -112.29360194, -0.01279209, -11.22936019, -0.03735658, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 89.30267634, 0.00122464, 106.19580138, 0.01279209, 10.61958014, 0.03735658, -89.30267634, -0.00122464, -106.19580138, -0.01279209, -10.61958014, -0.03735658, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 128.06080799, 0.02449274, 128.06080799, 0.07347822, 89.6425656, -1650.3644355, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 32.015202, 0.0001153, 96.045606, 0.00034589, 320.15201999, 0.00115295, -32.015202, -0.0001153, -96.045606, -0.00034589, -320.15201999, -0.00115295, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 128.06080799, 0.02449274, 128.06080799, 0.07347822, 89.6425656, -1650.3644355, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 32.015202, 0.0001153, 96.045606, 0.00034589, 320.15201999, 0.00115295, -32.015202, -0.0001153, -96.045606, -0.00034589, -320.15201999, -0.00115295, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 3.05, 7.9, 0.0)
    ops.node(121010, 3.05, 7.9, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.25, 27302653.53285908, 11376105.63869128, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 488.94798133, 0.00084296, 586.24318397, 0.01178584, 58.6243184, 0.02743197, -488.94798133, -0.00084296, -586.24318397, -0.01178584, -58.6243184, -0.02743197, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 488.94798133, 0.00084296, 586.24318397, 0.01178584, 58.6243184, 0.02743197, -488.94798133, -0.00084296, -586.24318397, -0.01178584, -58.6243184, -0.02743197, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 244.27071047, 0.01685918, 244.27071047, 0.05057754, 170.98949733, -2314.42364834, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 61.06767762, 8.117e-05, 183.20303286, 0.0002435, 610.67677619, 0.00081165, -61.06767762, -8.117e-05, -183.20303286, -0.0002435, -610.67677619, -0.00081165, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 244.27071047, 0.01685918, 244.27071047, 0.05057754, 170.98949733, -2314.42364834, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 61.06767762, 8.117e-05, 183.20303286, 0.0002435, 610.67677619, 0.00081165, -61.06767762, -8.117e-05, -183.20303286, -0.0002435, -610.67677619, -0.00081165, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 9.0, 7.9, 0.0)
    ops.node(121011, 9.0, 7.9, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.3025, 27223283.14499593, 11343034.6437483, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 718.73927544, 0.00081937, 859.23895686, 0.01120815, 85.92389569, 0.02476458, -718.73927544, -0.00081937, -859.23895686, -0.01120815, -85.92389569, -0.02476458, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 761.16134673, 0.00081937, 909.9537258, 0.01120815, 90.99537258, 0.02476458, -761.16134673, -0.00081937, -909.9537258, -0.01120815, -90.99537258, -0.02476458, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 321.88312741, 0.01638733, 321.88312741, 0.04916198, 225.31818918, -2893.43653873, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 80.47078185, 8.865e-05, 241.41234555, 0.00026595, 804.70781851, 0.00088649, -80.47078185, -8.865e-05, -241.41234555, -0.00026595, -804.70781851, -0.00088649, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 321.88312741, 0.01638733, 321.88312741, 0.04916198, 225.31818918, -2893.43653873, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 80.47078185, 8.865e-05, 241.41234555, 0.00026595, 804.70781851, 0.00088649, -80.47078185, -8.865e-05, -241.41234555, -0.00026595, -804.70781851, -0.00088649, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 14.95, 7.9, 0.0)
    ops.node(121012, 14.95, 7.9, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 27994260.73399261, 11664275.30583026, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 301.85562881, 0.00100454, 358.63919742, 0.01240213, 35.86391974, 0.02948115, -301.85562881, -0.00100454, -358.63919742, -0.01240213, -35.86391974, -0.02948115, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 277.03141434, 0.00100454, 329.14517608, 0.01240213, 32.91451761, 0.02948115, -277.03141434, -0.00100454, -329.14517608, -0.01240213, -32.91451761, -0.02948115, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 196.18691602, 0.02009085, 196.18691602, 0.06027255, 137.33084121, -2272.44211688, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 49.046729, 9.934e-05, 147.14018701, 0.00029802, 490.46729004, 0.0009934, -49.046729, -9.934e-05, -147.14018701, -0.00029802, -490.46729004, -0.0009934, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 196.18691602, 0.02009085, 196.18691602, 0.06027255, 137.33084121, -2272.44211688, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 49.046729, 9.934e-05, 147.14018701, 0.00029802, 490.46729004, 0.0009934, -49.046729, -9.934e-05, -147.14018701, -0.00029802, -490.46729004, -0.0009934, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 11.85, 0.0)
    ops.node(121013, 0.0, 11.85, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.09, 27797306.29059401, 11582210.95441417, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 94.77026199, 0.00118, 112.6759276, 0.01267999, 11.26759276, 0.03675699, -94.77026199, -0.00118, -112.6759276, -0.01267999, -11.26759276, -0.03675699, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 89.27370072, 0.00118, 106.14085926, 0.01267999, 10.61408593, 0.03675699, -89.27370072, -0.00118, -106.14085926, -0.01267999, -10.61408593, -0.03675699, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 128.25185311, 0.02359991, 128.25185311, 0.07079974, 89.77629718, -1667.76462183, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 32.06296328, 0.00011627, 96.18888983, 0.00034881, 320.62963278, 0.00116268, -32.06296328, -0.00011627, -96.18888983, -0.00034881, -320.62963278, -0.00116268, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 128.25185311, 0.02359991, 128.25185311, 0.07079974, 89.77629718, -1667.76462183, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 32.06296328, 0.00011627, 96.18888983, 0.00034881, 320.62963278, 0.00116268, -32.06296328, -0.00011627, -96.18888983, -0.00034881, -320.62963278, -0.00116268, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 3.05, 11.85, 0.0)
    ops.node(121014, 3.05, 11.85, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.25, 26832014.25445624, 11180005.93935677, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 492.04269246, 0.00088169, 589.81247072, 0.01147334, 58.98124707, 0.02651116, -492.04269246, -0.00088169, -589.81247072, -0.01147334, -58.98124707, -0.02651116, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 492.04269246, 0.00088169, 589.81247072, 0.01147334, 58.98124707, 0.02651116, -492.04269246, -0.00088169, -589.81247072, -0.01147334, -58.98124707, -0.02651116, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 240.25006809, 0.01763377, 240.25006809, 0.05290131, 168.17504766, -2308.72528653, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 60.06251702, 8.123e-05, 180.18755107, 0.00024369, 600.62517022, 0.00081229, -60.06251702, -8.123e-05, -180.18755107, -0.00024369, -600.62517022, -0.00081229, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 240.25006809, 0.01763377, 240.25006809, 0.05290131, 168.17504766, -2308.72528653, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 60.06251702, 8.123e-05, 180.18755107, 0.00024369, 600.62517022, 0.00081229, -60.06251702, -8.123e-05, -180.18755107, -0.00024369, -600.62517022, -0.00081229, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 11.85, 0.0)
    ops.node(121015, 9.0, 11.85, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.3025, 27764742.8153908, 11568642.83974617, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 730.92425505, 0.00082165, 874.07930485, 0.0114014, 87.40793048, 0.02562624, -730.92425505, -0.00082165, -874.07930485, -0.0114014, -87.40793048, -0.02562624, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 774.43043593, 0.00082165, 926.10638163, 0.0114014, 92.61063816, 0.02562624, -774.43043593, -0.00082165, -926.10638163, -0.0114014, -92.61063816, -0.02562624, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 327.48095991, 0.01643303, 327.48095991, 0.04929909, 229.23667193, -2888.99429757, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 81.87023998, 8.843e-05, 245.61071993, 0.0002653, 818.70239977, 0.00088432, -81.87023998, -8.843e-05, -245.61071993, -0.0002653, -818.70239977, -0.00088432, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 327.48095991, 0.01643303, 327.48095991, 0.04929909, 229.23667193, -2888.99429757, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 81.87023998, 8.843e-05, 245.61071993, 0.0002653, 818.70239977, 0.00088432, -81.87023998, -8.843e-05, -245.61071993, -0.0002653, -818.70239977, -0.00088432, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 14.95, 11.85, 0.0)
    ops.node(121016, 14.95, 11.85, 2.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.16, 26998694.20683129, 11249455.91951304, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 292.90926689, 0.00105887, 347.51658166, 0.01029158, 34.75165817, 0.02300031, -292.90926689, -0.00105887, -347.51658166, -0.01029158, -34.75165817, -0.02300031, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 264.18633359, 0.00105887, 313.43880836, 0.01029158, 31.34388084, 0.02300031, -264.18633359, -0.00105887, -313.43880836, -0.01029158, -31.34388084, -0.02300031, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 176.62631622, 0.02117734, 176.62631622, 0.06353201, 123.63842135, -2002.69511051, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 44.15657905, 9.273e-05, 132.46973716, 0.0002782, 441.56579054, 0.00092733, -44.15657905, -9.273e-05, -132.46973716, -0.0002782, -441.56579054, -0.00092733, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 176.62631622, 0.02117734, 176.62631622, 0.06353201, 123.63842135, -2002.69511051, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 44.15657905, 9.273e-05, 132.46973716, 0.0002782, 441.56579054, 0.00092733, -44.15657905, -9.273e-05, -132.46973716, -0.0002782, -441.56579054, -0.00092733, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 15.8, 0.0)
    ops.node(121017, 0.0, 15.8, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.0625, 28401895.65062046, 11834123.18775853, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 50.50078976, 0.00141577, 60.22293938, 0.01417706, 6.02229394, 0.04596635, -50.50078976, -0.00141577, -60.22293938, -0.01417706, -6.02229394, -0.04596635, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 50.50078976, 0.00141577, 60.22293938, 0.01417706, 6.02229394, 0.04596635, -50.50078976, -0.00141577, -60.22293938, -0.01417706, -6.02229394, -0.04596635, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 95.1233878, 0.02831543, 95.1233878, 0.0849463, 66.58637146, -1286.21841229, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 23.78084695, 0.00012154, 71.34254085, 0.00036461, 237.80846951, 0.00121535, -23.78084695, -0.00012154, -71.34254085, -0.00036461, -237.80846951, -0.00121535, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 95.1233878, 0.02831543, 95.1233878, 0.0849463, 66.58637146, -1286.21841229, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 23.78084695, 0.00012154, 71.34254085, 0.00036461, 237.80846951, 0.00121535, -23.78084695, -0.00012154, -71.34254085, -0.00036461, -237.80846951, -0.00121535, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 3.05, 15.8, 0.0)
    ops.node(121018, 3.05, 15.8, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.16, 28627128.22616072, 11927970.09423363, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 239.30260664, 0.00093332, 285.84439691, 0.01284977, 28.58443969, 0.03668537, -239.30260664, -0.00093332, -285.84439691, -0.01284977, -28.58443969, -0.03668537, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 247.37254339, 0.00093332, 295.4838498, 0.01284977, 29.54838498, 0.03668537, -247.37254339, -0.00093332, -295.4838498, -0.01284977, -29.54838498, -0.03668537, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 200.95452958, 0.01866639, 200.95452958, 0.05599917, 140.6681707, -2292.15376966, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 50.23863239, 9.95e-05, 150.71589718, 0.00029851, 502.38632394, 0.00099505, -50.23863239, -9.95e-05, -150.71589718, -0.00029851, -502.38632394, -0.00099505, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 200.95452958, 0.01866639, 200.95452958, 0.05599917, 140.6681707, -2292.15376966, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 50.23863239, 9.95e-05, 150.71589718, 0.00029851, 502.38632394, 0.00099505, -50.23863239, -9.95e-05, -150.71589718, -0.00029851, -502.38632394, -0.00099505, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 9.0, 15.8, 0.0)
    ops.node(121019, 9.0, 15.8, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.2025, 27724384.06680581, 11551826.69450242, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 352.42245735, 0.00090375, 420.18974056, 0.01255713, 42.01897406, 0.02976892, -352.42245735, -0.00090375, -420.18974056, -0.01255713, -42.01897406, -0.02976892, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 371.02143621, 0.00090375, 442.36511543, 0.01255713, 44.23651154, 0.02976892, -371.02143621, -0.00090375, -442.36511543, -0.01255713, -44.23651154, -0.02976892, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 232.29107361, 0.01807491, 232.29107361, 0.05422473, 162.60375153, -2570.03355062, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 58.0727684, 9.384e-05, 174.21830521, 0.00028152, 580.72768402, 0.0009384, -58.0727684, -9.384e-05, -174.21830521, -0.00028152, -580.72768402, -0.0009384, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 232.29107361, 0.01807491, 232.29107361, 0.05422473, 162.60375153, -2570.03355062, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 58.0727684, 9.384e-05, 174.21830521, 0.00028152, 580.72768402, 0.0009384, -58.0727684, -9.384e-05, -174.21830521, -0.00028152, -580.72768402, -0.0009384, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 14.95, 15.8, 0.0)
    ops.node(121020, 14.95, 15.8, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.09, 28599797.08678026, 11916582.11949178, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 131.31626204, 0.00130335, 155.60785406, 0.01323922, 15.56078541, 0.0334581, -131.31626204, -0.00130335, -155.60785406, -0.01323922, -15.56078541, -0.0334581, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 120.55396323, 0.00130335, 142.85468704, 0.01323922, 14.2854687, 0.0334581, -120.55396323, -0.00130335, -142.85468704, -0.01323922, -14.2854687, -0.0334581, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 126.02017936, 0.02606697, 126.02017936, 0.07820091, 88.21412555, -1565.12271127, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 31.50504484, 0.00011104, 94.51513452, 0.00033312, 315.0504484, 0.0011104, -31.50504484, -0.00011104, -94.51513452, -0.00033312, -315.0504484, -0.0011104, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 126.02017936, 0.02606697, 126.02017936, 0.07820091, 88.21412555, -1565.12271127, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 31.50504484, 0.00011104, 94.51513452, 0.00033312, 315.0504484, 0.0011104, -31.50504484, -0.00011104, -94.51513452, -0.00033312, -315.0504484, -0.0011104, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.45)
    ops.node(122003, 9.0, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.2025, 26589646.42101824, 11079019.34209093, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 262.51936095, 0.00087037, 315.10161639, 0.01258933, 31.51016164, 0.03200595, -262.51936095, -0.00087037, -315.10161639, -0.01258933, -31.51016164, -0.03200595, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 236.14805862, 0.00087037, 283.44817963, 0.01258933, 28.34481796, 0.03200595, -236.14805862, -0.00087037, -283.44817963, -0.01258933, -28.34481796, -0.03200595, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 207.12178056, 0.01740744, 207.12178056, 0.05222231, 144.98524639, -2197.5700155, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 51.78044514, 8.724e-05, 155.34133542, 0.00026173, 517.80445141, 0.00087243, -51.78044514, -8.724e-05, -155.34133542, -0.00026173, -517.80445141, -0.00087243, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 207.12178056, 0.01740744, 207.12178056, 0.05222231, 144.98524639, -2197.5700155, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 51.78044514, 8.724e-05, 155.34133542, 0.00026173, 517.80445141, 0.00087243, -51.78044514, -8.724e-05, -155.34133542, -0.00026173, -517.80445141, -0.00087243, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 14.95, 0.0, 3.45)
    ops.node(122004, 14.95, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.09, 27747346.85397518, 11561394.52248966, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 116.71816355, 0.00127153, 139.41043639, 0.01445876, 13.94104364, 0.03846517, -116.71816355, -0.00127153, -139.41043639, -0.01445876, -13.94104364, -0.03846517, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 106.10515423, 0.00127153, 126.73405239, 0.01445876, 12.67340524, 0.03846517, -106.10515423, -0.00127153, -126.73405239, -0.01445876, -12.67340524, -0.03846517, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 115.72334374, 0.02543069, 115.72334374, 0.07629206, 81.00634062, -1406.47006382, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 28.93083594, 0.0001051, 86.79250781, 0.0003153, 289.30835936, 0.00105099, -28.93083594, -0.0001051, -86.79250781, -0.0003153, -289.30835936, -0.00105099, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 115.72334374, 0.02543069, 115.72334374, 0.07629206, 81.00634062, -1406.47006382, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 28.93083594, 0.0001051, 86.79250781, 0.0003153, 289.30835936, 0.00105099, -28.93083594, -0.0001051, -86.79250781, -0.0003153, -289.30835936, -0.00105099, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 3.95, 3.5)
    ops.node(122005, 0.0, 3.95, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.09, 26506509.15412935, 11044378.81422056, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 78.95761828, 0.00116138, 94.64875066, 0.01406402, 9.46487507, 0.04216687, -78.95761828, -0.00116138, -94.64875066, -0.01406402, -9.46487507, -0.04216687, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 73.77452738, 0.00116138, 88.43563166, 0.01406402, 8.84356317, 0.04216687, -73.77452738, -0.00116138, -88.43563166, -0.01406402, -8.84356317, -0.04216687, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 117.94507543, 0.02322753, 117.94507543, 0.0696826, 82.5615528, -1589.48141285, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 29.48626886, 0.00011213, 88.45880657, 0.00033639, 294.86268858, 0.00112132, -29.48626886, -0.00011213, -88.45880657, -0.00033639, -294.86268858, -0.00112132, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 117.94507543, 0.02322753, 117.94507543, 0.0696826, 82.5615528, -1589.48141285, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 29.48626886, 0.00011213, 88.45880657, 0.00033639, 294.86268858, 0.00112132, -29.48626886, -0.00011213, -88.45880657, -0.00033639, -294.86268858, -0.00112132, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 3.05, 3.95, 3.5)
    ops.node(122006, 3.05, 3.95, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.25, 27586072.2657209, 11494196.77738371, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 314.43969896, 0.00081668, 378.86950138, 0.01173084, 37.88695014, 0.0302191, -314.43969896, -0.00081668, -378.86950138, -0.01173084, -37.88695014, -0.0302191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 297.9112749, 0.00081668, 358.95434498, 0.01173084, 35.8954345, 0.0302191, -297.9112749, -0.00081668, -358.95434498, -0.01173084, -35.8954345, -0.0302191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 231.76575117, 0.01633369, 231.76575117, 0.04900107, 162.23602582, -2019.80837135, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 57.94143779, 7.622e-05, 173.82431338, 0.00022866, 579.41437793, 0.00076219, -57.94143779, -7.622e-05, -173.82431338, -0.00022866, -579.41437793, -0.00076219, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 231.76575117, 0.01633369, 231.76575117, 0.04900107, 162.23602582, -2019.80837135, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 57.94143779, 7.622e-05, 173.82431338, 0.00022866, 579.41437793, 0.00076219, -57.94143779, -7.622e-05, -173.82431338, -0.00022866, -579.41437793, -0.00076219, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 9.0, 3.95, 3.5)
    ops.node(122007, 9.0, 3.95, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.3025, 26674244.54409361, 11114268.560039, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 451.58178073, 0.0007885, 543.12482242, 0.01098887, 54.31248224, 0.02661881, -451.58178073, -0.0007885, -543.12482242, -0.01098887, -54.31248224, -0.02661881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 411.8034226, 0.0007885, 495.28273795, 0.01098887, 49.5282738, 0.02661881, -411.8034226, -0.0007885, -495.28273795, -0.01098887, -49.5282738, -0.02661881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 293.88733297, 0.01576991, 293.88733297, 0.04730972, 205.72113308, -2454.42201092, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 73.47183324, 8.261e-05, 220.41549973, 0.00024782, 734.71833244, 0.00082605, -73.47183324, -8.261e-05, -220.41549973, -0.00024782, -734.71833244, -0.00082605, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 293.88733297, 0.01576991, 293.88733297, 0.04730972, 205.72113308, -2454.42201092, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 73.47183324, 8.261e-05, 220.41549973, 0.00024782, 734.71833244, 0.00082605, -73.47183324, -8.261e-05, -220.41549973, -0.00024782, -734.71833244, -0.00082605, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 14.95, 3.95, 3.5)
    ops.node(122008, 14.95, 3.95, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.16, 26803919.79636461, 11168299.91515192, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 257.98947857, 0.00102358, 308.6419668, 0.01148207, 30.86419668, 0.02755033, -257.98947857, -0.00102358, -308.6419668, -0.01148207, -30.86419668, -0.02755033, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 231.11350757, 0.00102358, 276.48928911, 0.01148207, 27.64892891, 0.02755033, -231.11350757, -0.00102358, -276.48928911, -0.01148207, -27.64892891, -0.02755033, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 162.07884137, 0.02047161, 162.07884137, 0.06141484, 113.45518896, -1684.51193623, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 40.51971034, 8.571e-05, 121.55913103, 0.00025714, 405.19710344, 0.00085714, -40.51971034, -8.571e-05, -121.55913103, -0.00025714, -405.19710344, -0.00085714, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 162.07884137, 0.02047161, 162.07884137, 0.06141484, 113.45518896, -1684.51193623, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 40.51971034, 8.571e-05, 121.55913103, 0.00025714, 405.19710344, 0.00085714, -40.51971034, -8.571e-05, -121.55913103, -0.00025714, -405.19710344, -0.00085714, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 7.9, 3.5)
    ops.node(122009, 0.0, 7.9, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.09, 27940958.63968185, 11642066.09986744, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 80.06779293, 0.00114638, 95.94287423, 0.01447297, 9.59428742, 0.04519448, -80.06779293, -0.00114638, -95.94287423, -0.01447297, -9.59428742, -0.04519448, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 75.10492845, 0.00114638, 89.99602012, 0.01447297, 8.99960201, 0.04519448, -75.10492845, -0.00114638, -89.99602012, -0.01447297, -8.99960201, -0.04519448, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 121.90484914, 0.02292757, 121.90484914, 0.0687827, 85.3333944, -1572.22732732, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 30.47621228, 0.00010995, 91.42863685, 0.00032984, 304.76212284, 0.00109946, -30.47621228, -0.00010995, -91.42863685, -0.00032984, -304.76212284, -0.00109946, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 121.90484914, 0.02292757, 121.90484914, 0.0687827, 85.3333944, -1572.22732732, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 30.47621228, 0.00010995, 91.42863685, 0.00032984, 304.76212284, 0.00109946, -30.47621228, -0.00010995, -91.42863685, -0.00032984, -304.76212284, -0.00109946, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 3.05, 7.9, 3.5)
    ops.node(122010, 3.05, 7.9, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.25, 27117638.0203096, 11299015.84179567, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 315.16487758, 0.00081614, 379.96511401, 0.01177774, 37.9965114, 0.02997698, -315.16487758, -0.00081614, -379.96511401, -0.01177774, -37.9965114, -0.02997698, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 297.78009908, 0.00081614, 359.0058961, 0.01177774, 35.90058961, 0.02997698, -297.78009908, -0.00081614, -359.0058961, -0.01177774, -35.90058961, -0.02997698, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 227.01682479, 0.01632289, 227.01682479, 0.04896867, 158.91177736, -1998.61386969, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 56.7542062, 7.595e-05, 170.2626186, 0.00022784, 567.54206198, 0.00075947, -56.7542062, -7.595e-05, -170.2626186, -0.00022784, -567.54206198, -0.00075947, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 227.01682479, 0.01632289, 227.01682479, 0.04896867, 158.91177736, -1998.61386969, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 56.7542062, 7.595e-05, 170.2626186, 0.00022784, 567.54206198, 0.00075947, -56.7542062, -7.595e-05, -170.2626186, -0.00022784, -567.54206198, -0.00075947, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 9.0, 7.9, 3.5)
    ops.node(122011, 9.0, 7.9, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.3025, 26721209.98199302, 11133837.49249709, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 449.00886443, 0.000781, 540.03856027, 0.01108462, 54.00385603, 0.02677088, -449.00886443, -0.000781, -540.03856027, -0.01108462, -54.00385603, -0.02677088, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 409.57384876, 0.000781, 492.60869691, 0.01108462, 49.26086969, 0.02677088, -409.57384876, -0.000781, -492.60869691, -0.01108462, -49.26086969, -0.02677088, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 295.33412246, 0.01562008, 295.33412246, 0.04686024, 206.73388572, -2473.01435969, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 73.83353062, 8.287e-05, 221.50059185, 0.0002486, 738.33530615, 0.00082866, -73.83353062, -8.287e-05, -221.50059185, -0.0002486, -738.33530615, -0.00082866, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 295.33412246, 0.01562008, 295.33412246, 0.04686024, 206.73388572, -2473.01435969, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 73.83353062, 8.287e-05, 221.50059185, 0.0002486, 738.33530615, 0.00082866, -73.83353062, -8.287e-05, -221.50059185, -0.0002486, -738.33530615, -0.00082866, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 14.95, 7.9, 3.5)
    ops.node(122012, 14.95, 7.9, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 27102092.29440457, 11292538.4560019, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 249.08777723, 0.0009824, 298.06550602, 0.01326257, 29.8065506, 0.03307779, -249.08777723, -0.0009824, -298.06550602, -0.01326257, -29.8065506, -0.03307779, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 211.38205113, 0.0009824, 252.94576367, 0.01326257, 25.29457637, 0.03307779, -211.38205113, -0.0009824, -252.94576367, -0.01326257, -25.29457637, -0.03307779, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 178.89907799, 0.01964801, 178.89907799, 0.05894402, 125.22935459, -1995.84682414, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 44.7247695, 9.357e-05, 134.17430849, 0.0002807, 447.24769497, 0.00093568, -44.7247695, -9.357e-05, -134.17430849, -0.0002807, -447.24769497, -0.00093568, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 178.89907799, 0.01964801, 178.89907799, 0.05894402, 125.22935459, -1995.84682414, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 44.7247695, 9.357e-05, 134.17430849, 0.0002807, 447.24769497, 0.00093568, -44.7247695, -9.357e-05, -134.17430849, -0.0002807, -447.24769497, -0.00093568, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 11.85, 3.5)
    ops.node(122013, 0.0, 11.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.09, 27417240.48656357, 11423850.20273482, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 79.95044724, 0.00118436, 95.79167685, 0.01426386, 9.57916769, 0.04373898, -79.95044724, -0.00118436, -95.79167685, -0.01426386, -9.57916769, -0.04373898, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 75.13948494, 0.00118436, 90.02747963, 0.01426386, 9.00274796, 0.04373898, -75.13948494, -0.00118436, -90.02747963, -0.01426386, -9.00274796, -0.04373898, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 121.14006461, 0.0236872, 121.14006461, 0.07106161, 84.79804523, -1590.84025844, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 30.28501615, 0.00011134, 90.85504846, 0.00033403, 302.85016153, 0.00111343, -30.28501615, -0.00011134, -90.85504846, -0.00033403, -302.85016153, -0.00111343, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 121.14006461, 0.0236872, 121.14006461, 0.07106161, 84.79804523, -1590.84025844, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 30.28501615, 0.00011134, 90.85504846, 0.00033403, 302.85016153, 0.00111343, -30.28501615, -0.00011134, -90.85504846, -0.00033403, -302.85016153, -0.00111343, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 3.05, 11.85, 3.5)
    ops.node(122014, 3.05, 11.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.25, 27669223.57413147, 11528843.15588811, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 314.58336355, 0.00083055, 379.18944412, 0.01166201, 37.91894441, 0.03047802, -314.58336355, -0.00083055, -379.18944412, -0.01166201, -37.91894441, -0.03047802, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 297.87329264, 0.00083055, 359.0476209, 0.01166201, 35.90476209, 0.03047802, -297.87329264, -0.00083055, -359.0476209, -0.01166201, -35.90476209, -0.03047802, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 230.77840567, 0.01661095, 230.77840567, 0.04983285, 161.54488397, -1989.17970694, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 57.69460142, 7.567e-05, 173.08380425, 0.000227, 576.94601417, 0.00075666, -57.69460142, -7.567e-05, -173.08380425, -0.000227, -576.94601417, -0.00075666, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 230.77840567, 0.01661095, 230.77840567, 0.04983285, 161.54488397, -1989.17970694, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 57.69460142, 7.567e-05, 173.08380425, 0.000227, 576.94601417, 0.00075666, -57.69460142, -7.567e-05, -173.08380425, -0.000227, -576.94601417, -0.00075666, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 11.85, 3.5)
    ops.node(122015, 9.0, 11.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.3025, 27049902.24789109, 11270792.60328796, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 449.1125768, 0.0007713, 540.2007216, 0.01131645, 54.02007216, 0.0273905, -449.1125768, -0.0007713, -540.2007216, -0.01131645, -54.02007216, -0.0273905, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 409.45986802, 0.0007713, 492.50572707, 0.01131645, 49.25057271, 0.0273905, -409.45986802, -0.0007713, -492.50572707, -0.01131645, -49.25057271, -0.0273905, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 299.28786311, 0.01542596, 299.28786311, 0.04627788, 209.50150418, -2484.19724792, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 74.82196578, 8.295e-05, 224.46589733, 0.00024886, 748.21965778, 0.00082955, -74.82196578, -8.295e-05, -224.46589733, -0.00024886, -748.21965778, -0.00082955, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 299.28786311, 0.01542596, 299.28786311, 0.04627788, 209.50150418, -2484.19724792, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 74.82196578, 8.295e-05, 224.46589733, 0.00024886, 748.21965778, 0.00082955, -74.82196578, -8.295e-05, -224.46589733, -0.00024886, -748.21965778, -0.00082955, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 14.95, 11.85, 3.5)
    ops.node(122016, 14.95, 11.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.16, 28037197.21121729, 11682165.50467387, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 262.23896926, 0.00100636, 313.92239175, 0.01198729, 31.39223918, 0.02986168, -262.23896926, -0.00100636, -313.92239175, -0.01198729, -31.39223918, -0.02986168, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 234.64273525, 0.00100636, 280.88734815, 0.01198729, 28.08873481, 0.02986168, -234.64273525, -0.00100636, -280.88734815, -0.01198729, -28.08873481, -0.02986168, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 168.37815407, 0.02012712, 168.37815407, 0.06038137, 117.86470785, -1685.46834426, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 42.09453852, 8.513e-05, 126.28361556, 0.00025539, 420.94538519, 0.00085128, -42.09453852, -8.513e-05, -126.28361556, -0.00025539, -420.94538519, -0.00085128, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 168.37815407, 0.02012712, 168.37815407, 0.06038137, 117.86470785, -1685.46834426, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 42.09453852, 8.513e-05, 126.28361556, 0.00025539, 420.94538519, 0.00085128, -42.09453852, -8.513e-05, -126.28361556, -0.00025539, -420.94538519, -0.00085128, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 15.8, 3.45)
    ops.node(122017, 0.0, 15.8, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.0625, 27701102.23286538, 11542125.93036058, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 43.20802256, 0.00133708, 51.88588241, 0.01516299, 5.18858824, 0.05227191, -43.20802256, -0.00133708, -51.88588241, -0.01516299, -5.18858824, -0.05227191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 43.20802256, 0.00133708, 51.88588241, 0.01516299, 5.18858824, 0.05227191, -43.20802256, -0.00133708, -51.88588241, -0.01516299, -5.18858824, -0.05227191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 88.72582985, 0.02674166, 88.72582985, 0.08022498, 62.10808089, -1246.90150681, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 22.18145746, 0.00011623, 66.54437238, 0.00034869, 221.81457461, 0.00116229, -22.18145746, -0.00011623, -66.54437238, -0.00034869, -221.81457461, -0.00116229, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 88.72582985, 0.02674166, 88.72582985, 0.08022498, 62.10808089, -1246.90150681, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 22.18145746, 0.00011623, 66.54437238, 0.00034869, 221.81457461, 0.00116229, -22.18145746, -0.00011623, -66.54437238, -0.00034869, -221.81457461, -0.00116229, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 3.05, 15.8, 3.45)
    ops.node(122018, 3.05, 15.8, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.16, 27747327.30093216, 11561386.3753884, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 172.41537421, 0.0009098, 207.25862183, 0.01356093, 20.72586218, 0.04049546, -172.41537421, -0.0009098, -207.25862183, -0.01356093, -20.72586218, -0.04049546, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 151.75350808, 0.0009098, 182.42122018, 0.01356093, 18.24212202, 0.04049546, -151.75350808, -0.0009098, -182.42122018, -0.01356093, -18.24212202, -0.04049546, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 187.62752084, 0.01819591, 187.62752084, 0.05458774, 131.33926459, -2167.71418012, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 46.90688021, 9.585e-05, 140.72064063, 0.00028755, 469.0688021, 0.00095851, -46.90688021, -9.585e-05, -140.72064063, -0.00028755, -469.0688021, -0.00095851, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 187.62752084, 0.01819591, 187.62752084, 0.05458774, 131.33926459, -2167.71418012, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 46.90688021, 9.585e-05, 140.72064063, 0.00028755, 469.0688021, 0.00095851, -46.90688021, -9.585e-05, -140.72064063, -0.00028755, -469.0688021, -0.00095851, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 9.0, 15.8, 3.45)
    ops.node(122019, 9.0, 15.8, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.2025, 27498264.73159692, 11457610.30483205, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 264.14277963, 0.00087209, 317.15096134, 0.01283105, 31.71509613, 0.03369997, -264.14277963, -0.00087209, -317.15096134, -0.01283105, -31.71509613, -0.03369997, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 237.95589017, 0.00087209, 285.70888604, 0.01283105, 28.5708886, 0.03369997, -237.95589017, -0.00087209, -285.70888604, -0.01283105, -28.5708886, -0.03369997, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 212.45140764, 0.01744183, 212.45140764, 0.05232549, 148.71598535, -2190.31064449, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 53.11285191, 8.653e-05, 159.33855573, 0.00025959, 531.12851909, 0.00086531, -53.11285191, -8.653e-05, -159.33855573, -0.00025959, -531.12851909, -0.00086531, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 212.45140764, 0.01744183, 212.45140764, 0.05232549, 148.71598535, -2190.31064449, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 53.11285191, 8.653e-05, 159.33855573, 0.00025959, 531.12851909, 0.00086531, -53.11285191, -8.653e-05, -159.33855573, -0.00025959, -531.12851909, -0.00086531, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 14.95, 15.8, 3.45)
    ops.node(122020, 14.95, 15.8, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.09, 28426418.45423739, 11844341.02259891, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 114.77064527, 0.0012581, 137.11486065, 0.01459352, 13.71148606, 0.04002832, -114.77064527, -0.0012581, -137.11486065, -0.01459352, -13.71148606, -0.04002832, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 104.7274825, 0.0012581, 125.11643666, 0.01459352, 12.51164367, 0.04002832, -104.7274825, -0.0012581, -125.11643666, -0.01459352, -12.51164367, -0.04002832, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 116.39473937, 0.02516209, 116.39473937, 0.07548627, 81.47631756, -1376.90416374, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 29.09868484, 0.00010318, 87.29605453, 0.00030955, 290.98684842, 0.00103184, -29.09868484, -0.00010318, -87.29605453, -0.00030955, -290.98684842, -0.00103184, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 116.39473937, 0.02516209, 116.39473937, 0.07548627, 81.47631756, -1376.90416374, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 29.09868484, 0.00010318, 87.29605453, 0.00030955, 290.98684842, 0.00103184, -29.09868484, -0.00010318, -87.29605453, -0.00030955, -290.98684842, -0.00103184, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.6)
    ops.node(123003, 9.0, 0.0, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.1225, 27904915.06573193, 11627047.94405497, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 133.09399518, 0.00103962, 159.58423826, 0.01367758, 15.95842383, 0.03808585, -133.09399518, -0.00103962, -159.58423826, -0.01367758, -15.95842383, -0.03808585, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 126.91793621, 0.00103962, 152.17893297, 0.01367758, 15.2178933, 0.03808585, -126.91793621, -0.00103962, -152.17893297, -0.01367758, -15.2178933, -0.03808585, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 142.40523536, 0.02079242, 142.40523536, 0.06237726, 99.68366476, -1586.50563061, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 35.60130884, 9.448e-05, 106.80392652, 0.00028345, 356.01308841, 0.00094483, -35.60130884, -9.448e-05, -106.80392652, -0.00028345, -356.01308841, -0.00094483, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 142.40523536, 0.02079242, 142.40523536, 0.06237726, 99.68366476, -1586.50563061, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 35.60130884, 9.448e-05, 106.80392652, 0.00028345, 356.01308841, 0.00094483, -35.60130884, -9.448e-05, -106.80392652, -0.00028345, -356.01308841, -0.00094483, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 14.95, 0.0, 6.6)
    ops.node(123004, 14.95, 0.0, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 26928738.82379294, 11220307.84324706, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 60.51836333, 0.00148845, 72.39324157, 0.01510459, 7.23932416, 0.04226368, -60.51836333, -0.00148845, -72.39324157, -0.01510459, -7.23932416, -0.04226368, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 60.51836333, 0.00148845, 72.39324157, 0.01510459, 7.23932416, 0.04226368, -60.51836333, -0.00148845, -72.39324157, -0.01510459, -7.23932416, -0.04226368, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 80.57913941, 0.02976898, 80.57913941, 0.08930695, 56.40539759, -1087.37629063, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 20.14478485, 0.00010858, 60.43435456, 0.00032575, 201.44784852, 0.00108585, -20.14478485, -0.00010858, -60.43435456, -0.00032575, -201.44784852, -0.00108585, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 80.57913941, 0.02976898, 80.57913941, 0.08930695, 56.40539759, -1087.37629063, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 20.14478485, 0.00010858, 60.43435456, 0.00032575, 201.44784852, 0.00108585, -20.14478485, -0.00010858, -60.43435456, -0.00032575, -201.44784852, -0.00108585, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 3.95, 6.65)
    ops.node(123005, 0.0, 3.95, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 28178032.43047657, 11740846.84603191, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 42.45279418, 0.00133138, 50.98620115, 0.01590695, 5.09862011, 0.05451907, -42.45279418, -0.00133138, -50.98620115, -0.01590695, -5.09862011, -0.05451907, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 42.45279418, 0.00133138, 50.98620115, 0.01590695, 5.09862011, 0.05451907, -42.45279418, -0.00133138, -50.98620115, -0.01590695, -5.09862011, -0.05451907, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 90.35265568, 0.02662763, 90.35265568, 0.07988289, 63.24685897, -1272.22496093, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 22.58816392, 0.00011636, 67.76449176, 0.00034907, 225.88163919, 0.00116357, -22.58816392, -0.00011636, -67.76449176, -0.00034907, -225.88163919, -0.00116357, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 90.35265568, 0.02662763, 90.35265568, 0.07988289, 63.24685897, -1272.22496093, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 22.58816392, 0.00011636, 67.76449176, 0.00034907, 225.88163919, 0.00116357, -22.58816392, -0.00011636, -67.76449176, -0.00034907, -225.88163919, -0.00116357, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 3.05, 3.95, 6.65)
    ops.node(123006, 3.05, 3.95, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.16, 29280730.9550745, 12200304.56461438, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 177.87312233, 0.0009272, 213.86256734, 0.01229234, 21.38625673, 0.03475676, -177.87312233, -0.0009272, -213.86256734, -0.01229234, -21.38625673, -0.03475676, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 177.87312233, 0.0009272, 213.86256734, 0.01229234, 21.38625673, 0.03475676, -177.87312233, -0.0009272, -213.86256734, -0.01229234, -21.38625673, -0.03475676, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 163.8074384, 0.01854409, 163.8074384, 0.05563226, 114.66520688, -1471.38542773, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 40.9518596, 7.93e-05, 122.8555788, 0.0002379, 409.518596, 0.000793, -40.9518596, -7.93e-05, -122.8555788, -0.0002379, -409.518596, -0.000793, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 163.8074384, 0.01854409, 163.8074384, 0.05563226, 114.66520688, -1471.38542773, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 40.9518596, 7.93e-05, 122.8555788, 0.0002379, 409.518596, 0.000793, -40.9518596, -7.93e-05, -122.8555788, -0.0002379, -409.518596, -0.000793, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 9.0, 3.95, 6.65)
    ops.node(123007, 9.0, 3.95, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.25, 27736419.81023252, 11556841.58759688, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 301.98078035, 0.00079494, 364.35816251, 0.01190603, 36.43581625, 0.03137915, -301.98078035, -0.00079494, -364.35816251, -0.01190603, -36.43581625, -0.03137915, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 285.34512764, 0.00079494, 344.28623658, 0.01190603, 34.42862366, 0.03137915, -285.34512764, -0.00079494, -344.28623658, -0.01190603, -34.42862366, -0.03137915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 228.13667895, 0.01589886, 228.13667895, 0.04769659, 159.69567527, -1932.65194567, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 57.03416974, 7.462e-05, 171.10250922, 0.00022386, 570.34169739, 0.00074619, -57.03416974, -7.462e-05, -171.10250922, -0.00022386, -570.34169739, -0.00074619, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 228.13667895, 0.01589886, 228.13667895, 0.04769659, 159.69567527, -1932.65194567, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 57.03416974, 7.462e-05, 171.10250922, 0.00022386, 570.34169739, 0.00074619, -57.03416974, -7.462e-05, -171.10250922, -0.00022386, -570.34169739, -0.00074619, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 14.95, 3.95, 6.65)
    ops.node(123008, 14.95, 3.95, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 28773795.87523847, 11989081.6146827, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 141.57899885, 0.00108163, 169.93602381, 0.01298864, 16.99360238, 0.03523147, -141.57899885, -0.00108163, -169.93602381, -0.01298864, -16.99360238, -0.03523147, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 141.57899885, 0.00108163, 169.93602381, 0.01298864, 16.99360238, 0.03523147, -141.57899885, -0.00108163, -169.93602381, -0.01298864, -16.99360238, -0.03523147, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 133.36053682, 0.02163263, 133.36053682, 0.0648979, 93.35237577, -1323.95090572, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 33.34013421, 8.581e-05, 100.02040262, 0.00025743, 333.40134205, 0.0008581, -33.34013421, -8.581e-05, -100.02040262, -0.00025743, -333.40134205, -0.0008581, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 133.36053682, 0.02163263, 133.36053682, 0.0648979, 93.35237577, -1323.95090572, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 33.34013421, 8.581e-05, 100.02040262, 0.00025743, 333.40134205, 0.0008581, -33.34013421, -8.581e-05, -100.02040262, -0.00025743, -333.40134205, -0.0008581, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 7.9, 6.65)
    ops.node(123009, 0.0, 7.9, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 27398926.139446, 11416219.22476917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 42.93757193, 0.00138452, 51.52882164, 0.01529281, 5.15288216, 0.05093125, -42.93757193, -0.00138452, -51.52882164, -0.01529281, -5.15288216, -0.05093125, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 42.93757193, 0.00138452, 51.52882164, 0.01529281, 5.15288216, 0.05093125, -42.93757193, -0.00138452, -51.52882164, -0.01529281, -5.15288216, -0.05093125, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 89.37826213, 0.02769034, 89.37826213, 0.08307103, 62.56478349, -1271.32191894, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 22.34456553, 0.00011838, 67.0336966, 0.00035513, 223.44565533, 0.00118375, -22.34456553, -0.00011838, -67.0336966, -0.00035513, -223.44565533, -0.00118375, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 89.37826213, 0.02769034, 89.37826213, 0.08307103, 62.56478349, -1271.32191894, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 22.34456553, 0.00011838, 67.0336966, 0.00035513, 223.44565533, 0.00118375, -22.34456553, -0.00011838, -67.0336966, -0.00035513, -223.44565533, -0.00118375, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 3.05, 7.9, 6.65)
    ops.node(123010, 3.05, 7.9, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.16, 27877473.28220074, 11615613.86758364, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 177.29147372, 0.00095173, 213.47072508, 0.01247682, 21.34707251, 0.0334828, -177.29147372, -0.00095173, -213.47072508, -0.01247682, -21.34707251, -0.0334828, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 177.29147372, 0.00095173, 213.47072508, 0.01247682, 21.34707251, 0.0334828, -177.29147372, -0.00095173, -213.47072508, -0.01247682, -21.34707251, -0.0334828, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 157.76985143, 0.01903459, 157.76985143, 0.05710377, 110.438896, -1493.15084108, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 39.44246286, 8.022e-05, 118.32738857, 0.00024067, 394.42462858, 0.00080222, -39.44246286, -8.022e-05, -118.32738857, -0.00024067, -394.42462858, -0.00080222, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 157.76985143, 0.01903459, 157.76985143, 0.05710377, 110.438896, -1493.15084108, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 39.44246286, 8.022e-05, 118.32738857, 0.00024067, 394.42462858, 0.00080222, -39.44246286, -8.022e-05, -118.32738857, -0.00024067, -394.42462858, -0.00080222, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 9.0, 7.9, 6.65)
    ops.node(123011, 9.0, 7.9, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.25, 27584856.71586768, 11493690.2982782, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 303.34293354, 0.00079194, 366.03605313, 0.01180006, 36.60360531, 0.03111384, -303.34293354, -0.00079194, -366.03605313, -0.01180006, -36.60360531, -0.03111384, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 286.34536937, 0.00079194, 345.52553315, 0.01180006, 34.55255331, 0.03111384, -286.34536937, -0.00079194, -345.52553315, -0.01180006, -34.55255331, -0.03111384, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 225.4019379, 0.01583876, 225.4019379, 0.04751628, 157.78135653, -1900.26437881, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 56.35048448, 7.413e-05, 169.05145343, 0.00022239, 563.50484475, 0.00074129, -56.35048448, -7.413e-05, -169.05145343, -0.00022239, -563.50484475, -0.00074129, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 225.4019379, 0.01583876, 225.4019379, 0.04751628, 157.78135653, -1900.26437881, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 56.35048448, 7.413e-05, 169.05145343, 0.00022239, 563.50484475, 0.00074129, -56.35048448, -7.413e-05, -169.05145343, -0.00022239, -563.50484475, -0.00074129, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 14.95, 7.9, 6.65)
    ops.node(123012, 14.95, 7.9, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 27604231.51047998, 11501763.12936666, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 129.44869375, 0.00105892, 155.43583091, 0.01422275, 15.54358309, 0.03914059, -129.44869375, -0.00105892, -155.43583091, -0.01422275, -15.54358309, -0.03914059, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 123.38697965, 0.00105892, 148.1572131, 0.01422275, 14.81572131, 0.03914059, -123.38697965, -0.00105892, -148.1572131, -0.01422275, -14.81572131, -0.03914059, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 142.37105691, 0.02117831, 142.37105691, 0.06353492, 99.65973984, -1625.98149666, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 35.59276423, 9.549e-05, 106.77829269, 0.00028647, 355.92764228, 0.00095489, -35.59276423, -9.549e-05, -106.77829269, -0.00028647, -355.92764228, -0.00095489, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 142.37105691, 0.02117831, 142.37105691, 0.06353492, 99.65973984, -1625.98149666, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 35.59276423, 9.549e-05, 106.77829269, 0.00028647, 355.92764228, 0.00095489, -35.59276423, -9.549e-05, -106.77829269, -0.00028647, -355.92764228, -0.00095489, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 11.85, 6.65)
    ops.node(123013, 0.0, 11.85, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 28376587.9715132, 11823578.32146383, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 43.18369727, 0.00132855, 51.81915734, 0.01552722, 5.18191573, 0.05373201, -43.18369727, -0.00132855, -51.81915734, -0.01552722, -5.18191573, -0.05373201, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 43.18369727, 0.00132855, 51.81915734, 0.01552722, 5.18191573, 0.05373201, -43.18369727, -0.00132855, -51.81915734, -0.01552722, -5.18191573, -0.05373201, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 91.68130768, 0.02657103, 91.68130768, 0.0797131, 64.17691538, -1282.49139311, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 22.92032692, 0.00011724, 68.76098076, 0.00035173, 229.20326921, 0.00117242, -22.92032692, -0.00011724, -68.76098076, -0.00035173, -229.20326921, -0.00117242, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 91.68130768, 0.02657103, 91.68130768, 0.0797131, 64.17691538, -1282.49139311, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 22.92032692, 0.00011724, 68.76098076, 0.00035173, 229.20326921, 0.00117242, -22.92032692, -0.00011724, -68.76098076, -0.00035173, -229.20326921, -0.00117242, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 3.05, 11.85, 6.65)
    ops.node(123014, 3.05, 11.85, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.16, 27810862.23994924, 11587859.26664552, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 176.27686474, 0.00093973, 212.2557398, 0.0121853, 21.22557398, 0.03310786, -176.27686474, -0.00093973, -212.2557398, -0.0121853, -21.22557398, -0.03310786, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 176.27686474, 0.00093973, 212.2557398, 0.0121853, 21.22557398, 0.03310786, -176.27686474, -0.00093973, -212.2557398, -0.0121853, -21.22557398, -0.03310786, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 155.97622053, 0.01879459, 155.97622053, 0.05638377, 109.18335437, -1462.07266796, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 38.99405513, 7.95e-05, 116.9821654, 0.0002385, 389.94055133, 0.000795, -38.99405513, -7.95e-05, -116.9821654, -0.0002385, -389.94055133, -0.000795, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 155.97622053, 0.01879459, 155.97622053, 0.05638377, 109.18335437, -1462.07266796, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 38.99405513, 7.95e-05, 116.9821654, 0.0002385, 389.94055133, 0.000795, -38.99405513, -7.95e-05, -116.9821654, -0.0002385, -389.94055133, -0.000795, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 11.85, 6.65)
    ops.node(123015, 9.0, 11.85, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.25, 29172134.69635449, 12155056.12348104, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 305.99474171, 0.00079541, 368.67545142, 0.01184273, 36.86754514, 0.03270726, -305.99474171, -0.00079541, -368.67545142, -0.01184273, -36.86754514, -0.03270726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 289.26866003, 0.00079541, 348.52315835, 0.01184273, 34.85231583, 0.03270726, -289.26866003, -0.00079541, -348.52315835, -0.01184273, -34.85231583, -0.03270726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 238.46247192, 0.01590826, 238.46247192, 0.04772477, 166.92373034, -1916.03144384, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 59.61561798, 7.416e-05, 178.84685394, 0.00022247, 596.15617979, 0.00074157, -59.61561798, -7.416e-05, -178.84685394, -0.00022247, -596.15617979, -0.00074157, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 238.46247192, 0.01590826, 238.46247192, 0.04772477, 166.92373034, -1916.03144384, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 59.61561798, 7.416e-05, 178.84685394, 0.00022247, 596.15617979, 0.00074157, -59.61561798, -7.416e-05, -178.84685394, -0.00022247, -596.15617979, -0.00074157, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 14.95, 11.85, 6.65)
    ops.node(123016, 14.95, 11.85, 9.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1225, 27828952.93729831, 11595397.05720763, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 145.24383837, 0.0010901, 174.39936052, 0.01229012, 17.43993605, 0.03320777, -145.24383837, -0.0010901, -174.39936052, -0.01229012, -17.43993605, -0.03320777, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 145.24383837, 0.0010901, 174.39936052, 0.01229012, 17.43993605, 0.03320777, -145.24383837, -0.0010901, -174.39936052, -0.01229012, -17.43993605, -0.03320777, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 128.39003293, 0.02180203, 128.39003293, 0.06540608, 89.87302305, -1295.847812, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 32.09750823, 8.542e-05, 96.2925247, 0.00025625, 320.97508232, 0.00085416, -32.09750823, -8.542e-05, -96.2925247, -0.00025625, -320.97508232, -0.00085416, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 128.39003293, 0.02180203, 128.39003293, 0.06540608, 89.87302305, -1295.847812, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 32.09750823, 8.542e-05, 96.2925247, 0.00025625, 320.97508232, 0.00085416, -32.09750823, -8.542e-05, -96.2925247, -0.00025625, -320.97508232, -0.00085416, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 15.8, 6.6)
    ops.node(123017, 0.0, 15.8, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 26602686.18153297, 11084452.57563874, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 35.66516226, 0.00130556, 43.17445226, 0.01670582, 4.31744523, 0.06041156, -35.66516226, -0.00130556, -43.17445226, -0.01670582, -4.31744523, -0.06041156, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 35.66516226, 0.00130556, 43.17445226, 0.01670582, 4.31744523, 0.06041156, -35.66516226, -0.00130556, -43.17445226, -0.01670582, -4.31744523, -0.06041156, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 80.64443699, 0.02611118, 80.64443699, 0.07833355, 56.4511059, -1281.89515875, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 20.16110925, 0.00011, 60.48332775, 0.00033001, 201.61109249, 0.00110005, -20.16110925, -0.00011, -60.48332775, -0.00033001, -201.61109249, -0.00110005, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 80.64443699, 0.02611118, 80.64443699, 0.07833355, 56.4511059, -1281.89515875, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 20.16110925, 0.00011, 60.48332775, 0.00033001, 201.61109249, 0.00110005, -20.16110925, -0.00011, -60.48332775, -0.00033001, -201.61109249, -0.00110005, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 3.05, 15.8, 6.6)
    ops.node(123018, 3.05, 15.8, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1225, 27453647.18005611, 11439019.65835671, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 112.3726761, 0.00096586, 135.48522697, 0.01452329, 13.5485227, 0.04625697, -112.3726761, -0.00096586, -135.48522697, -0.01452329, -13.5485227, -0.04625697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 99.36166484, 0.00096586, 119.79814115, 0.01452329, 11.97981412, 0.04625697, -99.36166484, -0.00096586, -119.79814115, -0.01452329, -11.97981412, -0.04625697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 144.71369433, 0.01931724, 144.71369433, 0.05795172, 101.29958603, -1784.38999841, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 36.17842358, 9.759e-05, 108.53527075, 0.00029278, 361.78423582, 0.00097593, -36.17842358, -9.759e-05, -108.53527075, -0.00029278, -361.78423582, -0.00097593, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 144.71369433, 0.01931724, 144.71369433, 0.05795172, 101.29958603, -1784.38999841, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 36.17842358, 9.759e-05, 108.53527075, 0.00029278, 361.78423582, 0.00097593, -36.17842358, -9.759e-05, -108.53527075, -0.00029278, -361.78423582, -0.00097593, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 9.0, 15.8, 6.6)
    ops.node(123019, 9.0, 15.8, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1225, 28615495.08058058, 11923122.95024191, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 134.62832048, 0.00103329, 161.39980184, 0.01426352, 16.13998018, 0.03991905, -134.62832048, -0.00103329, -161.39980184, -0.01426352, -16.13998018, -0.03991905, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 128.29890145, 0.00103329, 153.81174776, 0.01426352, 15.38117478, 0.03991905, -128.29890145, -0.00103329, -153.81174776, -0.01426352, -15.38117478, -0.03991905, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 147.64694754, 0.02066585, 147.64694754, 0.06199755, 103.35286328, -1642.6241947, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 36.91173688, 9.553e-05, 110.73521065, 0.00028658, 369.11736885, 0.00095528, -36.91173688, -9.553e-05, -110.73521065, -0.00028658, -369.11736885, -0.00095528, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 147.64694754, 0.02066585, 147.64694754, 0.06199755, 103.35286328, -1642.6241947, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 36.91173688, 9.553e-05, 110.73521065, 0.00028658, 369.11736885, 0.00095528, -36.91173688, -9.553e-05, -110.73521065, -0.00028658, -369.11736885, -0.00095528, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 14.95, 15.8, 6.6)
    ops.node(123020, 14.95, 15.8, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 27539782.31906125, 11474909.29960885, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 59.70387261, 0.00147222, 71.4474388, 0.01560389, 7.14474388, 0.04429072, -59.70387261, -0.00147222, -71.4474388, -0.01560389, -7.14474388, -0.04429072, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 59.70387261, 0.00147222, 71.4474388, 0.01560389, 7.14474388, 0.04429072, -59.70387261, -0.00147222, -71.4474388, -0.01560389, -7.14474388, -0.04429072, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 83.68623075, 0.02944439, 83.68623075, 0.08833317, 58.58036152, -1099.38207257, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 20.92155769, 0.00011027, 62.76467306, 0.00033081, 209.21557686, 0.0011027, -20.92155769, -0.00011027, -62.76467306, -0.00033081, -209.21557686, -0.0011027, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 83.68623075, 0.02944439, 83.68623075, 0.08833317, 58.58036152, -1099.38207257, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 20.92155769, 0.00011027, 62.76467306, 0.00033081, 209.21557686, 0.0011027, -20.92155769, -0.00011027, -62.76467306, -0.00033081, -209.21557686, -0.0011027, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 9.75)
    ops.node(124003, 9.0, 0.0, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.1225, 26181098.34604938, 10908790.97752057, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 96.39963252, 0.00098475, 117.28851788, 0.01624863, 11.72885179, 0.04975594, -96.39963252, -0.00098475, -117.28851788, -0.01624863, -11.72885179, -0.04975594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 90.52174892, 0.00098475, 110.1369527, 0.01624863, 11.01369527, 0.04975594, -90.52174892, -0.00098475, -110.1369527, -0.01624863, -11.01369527, -0.04975594, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 116.78702687, 0.01969494, 116.78702687, 0.05908482, 81.75091881, -1463.04255301, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 29.19675672, 8.259e-05, 87.59027016, 0.00024776, 291.96756719, 0.00082587, -29.19675672, -8.259e-05, -87.59027016, -0.00024776, -291.96756719, -0.00082587, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 116.78702687, 0.01969494, 116.78702687, 0.05908482, 81.75091881, -1463.04255301, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 29.19675672, 8.259e-05, 87.59027016, 0.00024776, 291.96756719, 0.00082587, -29.19675672, -8.259e-05, -87.59027016, -0.00024776, -291.96756719, -0.00082587, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 14.95, 0.0, 9.75)
    ops.node(124004, 14.95, 0.0, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 27173540.72653969, 11322308.6360582, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 45.31872004, 0.00133299, 55.08020606, 0.01878717, 5.50802061, 0.06316276, -45.31872004, -0.00133299, -55.08020606, -0.01878717, -5.50802061, -0.06316276, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 45.31872004, 0.00133299, 55.08020606, 0.01878717, 5.50802061, 0.06316276, -45.31872004, -0.00133299, -55.08020606, -0.01878717, -5.50802061, -0.06316276, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 67.90225615, 0.02665982, 67.90225615, 0.07997947, 47.5315793, -1138.42928985, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 16.97556404, 9.068e-05, 50.92669211, 0.00027203, 169.75564037, 0.00090678, -16.97556404, -9.068e-05, -50.92669211, -0.00027203, -169.75564037, -0.00090678, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 67.90225615, 0.02665982, 67.90225615, 0.07997947, 47.5315793, -1138.42928985, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 16.97556404, 9.068e-05, 50.92669211, 0.00027203, 169.75564037, 0.00090678, -16.97556404, -9.068e-05, -50.92669211, -0.00027203, -169.75564037, -0.00090678, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 3.95, 9.8)
    ops.node(124005, 0.0, 3.95, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 26517997.71690856, 11049165.71537857, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 29.30056981, 0.00125903, 35.67842571, 0.01875, 3.56784257, 0.0705143, -29.30056981, -0.00125903, -35.67842571, -0.01875, -3.56784257, -0.0705143, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 29.30056981, 0.00125903, 35.67842571, 0.01875, 3.56784257, 0.0705143, -29.30056981, -0.00125903, -35.67842571, -0.01875, -3.56784257, -0.0705143, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 77.98792824, 0.02518066, 77.98792824, 0.07554198, 54.59154977, -1602.80106081, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 19.49698206, 0.00010672, 58.49094618, 0.00032016, 194.96982059, 0.00106721, -19.49698206, -0.00010672, -58.49094618, -0.00032016, -194.96982059, -0.00106721, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 77.98792824, 0.02518066, 77.98792824, 0.07554198, 54.59154977, -1602.80106081, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 19.49698206, 0.00010672, 58.49094618, 0.00032016, 194.96982059, 0.00106721, -19.49698206, -0.00010672, -58.49094618, -0.00032016, -194.96982059, -0.00106721, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 3.05, 3.95, 9.8)
    ops.node(124006, 3.05, 3.95, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.16, 29899798.5694064, 12458249.40391933, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 134.9752841, 0.00089364, 163.34803235, 0.01363387, 16.33480324, 0.04239995, -134.9752841, -0.00089364, -163.34803235, -0.01363387, -16.33480324, -0.04239995, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 134.9752841, 0.00089364, 163.34803235, 0.01363387, 16.33480324, 0.04239995, -134.9752841, -0.00089364, -163.34803235, -0.01363387, -16.33480324, -0.04239995, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 146.91997271, 0.01787289, 146.91997271, 0.05361868, 102.84398089, -1235.84611839, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 36.72999318, 6.965e-05, 110.18997953, 0.00020896, 367.29993177, 0.00069652, -36.72999318, -6.965e-05, -110.18997953, -0.00020896, -367.29993177, -0.00069652, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 146.91997271, 0.01787289, 146.91997271, 0.05361868, 102.84398089, -1235.84611839, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 36.72999318, 6.965e-05, 110.18997953, 0.00020896, 367.29993177, 0.00069652, -36.72999318, -6.965e-05, -110.18997953, -0.00020896, -367.29993177, -0.00069652, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 9.0, 3.95, 9.8)
    ops.node(124007, 9.0, 3.95, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.25, 29353960.10187443, 12230816.70911434, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 239.04147029, 0.00074904, 289.83245121, 0.01320867, 28.98324512, 0.0387789, -239.04147029, -0.00074904, -289.83245121, -0.01320867, -28.98324512, -0.0387789, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 222.55202182, 0.00074904, 269.83936271, 0.01320867, 26.98393627, 0.0387789, -222.55202182, -0.00074904, -269.83936271, -0.01320867, -26.98393627, -0.0387789, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 211.837792, 0.01498073, 211.837792, 0.04494219, 148.2864544, -1558.18744566, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 52.959448, 6.547e-05, 158.878344, 0.00019641, 529.59447999, 0.0006547, -52.959448, -6.547e-05, -158.878344, -0.00019641, -529.59447999, -0.0006547, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 211.837792, 0.01498073, 211.837792, 0.04494219, 148.2864544, -1558.18744566, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 52.959448, 6.547e-05, 158.878344, 0.00019641, 529.59447999, 0.0006547, -52.959448, -6.547e-05, -158.878344, -0.00019641, -529.59447999, -0.0006547, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 14.95, 3.95, 9.8)
    ops.node(124008, 14.95, 3.95, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 28446412.30822515, 11852671.79509382, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 109.91938462, 0.00100216, 133.3492186, 0.01491953, 13.33492186, 0.04470562, -109.91938462, -0.00100216, -133.3492186, -0.01491953, -13.33492186, -0.04470562, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 109.91938462, 0.00100216, 133.3492186, 0.01491953, 13.33492186, 0.04470562, -109.91938462, -0.00100216, -133.3492186, -0.01491953, -13.33492186, -0.04470562, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 114.37178178, 0.02004314, 114.37178178, 0.06012943, 80.06024725, -1129.79861507, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 28.59294545, 7.444e-05, 85.77883634, 0.00022332, 285.92945446, 0.00074439, -28.59294545, -7.444e-05, -85.77883634, -0.00022332, -285.92945446, -0.00074439, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 114.37178178, 0.02004314, 114.37178178, 0.06012943, 80.06024725, -1129.79861507, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 28.59294545, 7.444e-05, 85.77883634, 0.00022332, 285.92945446, 0.00074439, -28.59294545, -7.444e-05, -85.77883634, -0.00022332, -285.92945446, -0.00074439, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 7.9, 9.8)
    ops.node(124009, 0.0, 7.9, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 27951959.79522955, 11646649.91467898, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 29.72217986, 0.00129631, 36.11183657, 0.01822692, 3.61118366, 0.07181397, -29.72217986, -0.00129631, -36.11183657, -0.01822692, -3.61118366, -0.07181397, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 29.72217986, 0.00129631, 36.11183657, 0.01822692, 3.61118366, 0.07181397, -29.72217986, -0.00129631, -36.11183657, -0.01822692, -3.61118366, -0.07181397, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 79.66543844, 0.02592629, 79.66543844, 0.07777888, 55.76580691, -1525.0940468, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 19.91635961, 0.00010342, 59.74907883, 0.00031027, 199.16359611, 0.00103424, -19.91635961, -0.00010342, -59.74907883, -0.00031027, -199.16359611, -0.00103424, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 79.66543844, 0.02592629, 79.66543844, 0.07777888, 55.76580691, -1525.0940468, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 19.91635961, 0.00010342, 59.74907883, 0.00031027, 199.16359611, 0.00103424, -19.91635961, -0.00010342, -59.74907883, -0.00031027, -199.16359611, -0.00103424, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 3.05, 7.9, 9.8)
    ops.node(124010, 3.05, 7.9, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.16, 28344022.70482242, 11810009.46034267, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 138.31523751, 0.00091942, 167.89474663, 0.0139611, 16.78947466, 0.04165992, -138.31523751, -0.00091942, -167.89474663, -0.0139611, -16.78947466, -0.04165992, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 138.31523751, 0.00091942, 167.89474663, 0.0139611, 16.78947466, 0.04165992, -138.31523751, -0.00091942, -167.89474663, -0.0139611, -16.78947466, -0.04165992, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 140.80199101, 0.01838836, 140.80199101, 0.05516509, 98.56139371, -1266.95930822, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 35.20049775, 7.042e-05, 105.60149326, 0.00021125, 352.00497752, 0.00070416, -35.20049775, -7.042e-05, -105.60149326, -0.00021125, -352.00497752, -0.00070416, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 140.80199101, 0.01838836, 140.80199101, 0.05516509, 98.56139371, -1266.95930822, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 35.20049775, 7.042e-05, 105.60149326, 0.00021125, 352.00497752, 0.00070416, -35.20049775, -7.042e-05, -105.60149326, -0.00021125, -352.00497752, -0.00070416, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 9.0, 7.9, 9.8)
    ops.node(124011, 9.0, 7.9, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.25, 26951226.28414627, 11229677.61839428, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 233.93117044, 0.0007818, 284.82862896, 0.01353735, 28.4828629, 0.03768887, -233.93117044, -0.0007818, -284.82862896, -0.01353735, -28.4828629, -0.03768887, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 218.29242376, 0.0007818, 265.78728971, 0.01353735, 26.57872897, 0.03768887, -218.29242376, -0.0007818, -265.78728971, -0.01353735, -26.57872897, -0.03768887, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 195.52568143, 0.01563599, 195.52568143, 0.04690797, 136.867977, -1594.35807498, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 48.88142036, 6.582e-05, 146.64426107, 0.00019745, 488.81420357, 0.00065816, -48.88142036, -6.582e-05, -146.64426107, -0.00019745, -488.81420357, -0.00065816, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 195.52568143, 0.01563599, 195.52568143, 0.04690797, 136.867977, -1594.35807498, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 48.88142036, 6.582e-05, 146.64426107, 0.00019745, 488.81420357, 0.00065816, -48.88142036, -6.582e-05, -146.64426107, -0.00019745, -488.81420357, -0.00065816, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 14.95, 7.9, 9.8)
    ops.node(124012, 14.95, 7.9, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 27286947.98524707, 11369561.66051961, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 109.02482548, 0.00101206, 132.49299016, 0.01672533, 13.24929902, 0.05156726, -109.02482548, -0.00101206, -132.49299016, -0.01672533, -13.24929902, -0.05156726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 98.01532268, 0.00101206, 119.11363423, 0.01672533, 11.91136342, 0.05156726, -98.01532268, -0.00101206, -119.11363423, -0.01672533, -11.91136342, -0.05156726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 120.38144148, 0.0202412, 120.38144148, 0.0607236, 84.26700903, -1455.05177922, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 30.09536037, 8.168e-05, 90.28608111, 0.00024504, 300.9536037, 0.00081679, -30.09536037, -8.168e-05, -90.28608111, -0.00024504, -300.9536037, -0.00081679, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 120.38144148, 0.0202412, 120.38144148, 0.0607236, 84.26700903, -1455.05177922, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 30.09536037, 8.168e-05, 90.28608111, 0.00024504, 300.9536037, 0.00081679, -30.09536037, -8.168e-05, -90.28608111, -0.00024504, -300.9536037, -0.00081679, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 11.85, 9.8)
    ops.node(124013, 0.0, 11.85, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 27786675.74057118, 11577781.55857133, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 29.99116322, 0.00123616, 36.44815893, 0.01827292, 3.64481589, 0.07162239, -29.99116322, -0.00123616, -36.44815893, -0.01827292, -3.64481589, -0.07162239, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 29.99116322, 0.00123616, 36.44815893, 0.01827292, 3.64481589, 0.07162239, -29.99116322, -0.00123616, -36.44815893, -0.01827292, -3.64481589, -0.07162239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 79.50424875, 0.02472323, 79.50424875, 0.07416969, 55.65297413, -1532.10607354, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 19.87606219, 0.00010383, 59.62818656, 0.00031149, 198.76062188, 0.00103829, -19.87606219, -0.00010383, -59.62818656, -0.00031149, -198.76062188, -0.00103829, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 79.50424875, 0.02472323, 79.50424875, 0.07416969, 55.65297413, -1532.10607354, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 19.87606219, 0.00010383, 59.62818656, 0.00031149, 198.76062188, 0.00103829, -19.87606219, -0.00010383, -59.62818656, -0.00031149, -198.76062188, -0.00103829, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 3.05, 11.85, 9.8)
    ops.node(124014, 3.05, 11.85, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.16, 27432290.77154844, 11430121.15481185, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 136.34792608, 0.00092061, 165.74098748, 0.01414348, 16.57409875, 0.04114803, -136.34792608, -0.00092061, -165.74098748, -0.01414348, -16.57409875, -0.04114803, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 136.34792608, 0.00092061, 165.74098748, 0.01414348, 16.57409875, 0.04114803, -136.34792608, -0.00092061, -165.74098748, -0.01414348, -16.57409875, -0.04114803, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 136.48228732, 0.01841227, 136.48228732, 0.05523682, 95.53760113, -1263.98425505, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 34.12057183, 7.052e-05, 102.36171549, 0.00021157, 341.20571831, 0.00070524, -34.12057183, -7.052e-05, -102.36171549, -0.00021157, -341.20571831, -0.00070524, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 136.48228732, 0.01841227, 136.48228732, 0.05523682, 95.53760113, -1263.98425505, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 34.12057183, 7.052e-05, 102.36171549, 0.00021157, 341.20571831, 0.00070524, -34.12057183, -7.052e-05, -102.36171549, -0.00021157, -341.20571831, -0.00070524, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 11.85, 9.8)
    ops.node(124015, 9.0, 11.85, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.25, 26366582.23586136, 10986075.9316089, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 237.20505651, 0.00078398, 289.0233327, 0.0131497, 28.90233327, 0.03688282, -237.20505651, -0.00078398, -289.0233327, -0.0131497, -28.90233327, -0.03688282, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 220.86226951, 0.00078398, 269.11040659, 0.0131497, 26.91104066, 0.03688282, -220.86226951, -0.00078398, -269.11040659, -0.0131497, -26.91104066, -0.03688282, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 190.07262349, 0.01567967, 190.07262349, 0.04703901, 133.05083645, -1559.05515946, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 47.51815587, 6.54e-05, 142.55446762, 0.0001962, 475.18155873, 0.00065399, -47.51815587, -6.54e-05, -142.55446762, -0.0001962, -475.18155873, -0.00065399, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 190.07262349, 0.01567967, 190.07262349, 0.04703901, 133.05083645, -1559.05515946, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 47.51815587, 6.54e-05, 142.55446762, 0.0001962, 475.18155873, 0.00065399, -47.51815587, -6.54e-05, -142.55446762, -0.0001962, -475.18155873, -0.00065399, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 14.95, 11.85, 9.8)
    ops.node(124016, 14.95, 11.85, 12.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1225, 29561045.92235452, 12317102.46764771, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 109.06224856, 0.00102826, 132.03061525, 0.01454831, 13.20306153, 0.04516884, -109.06224856, -0.00102826, -132.03061525, -0.01454831, -13.20306153, -0.04516884, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 109.06224856, 0.00102826, 132.03061525, 0.01454831, 13.20306153, 0.04516884, -109.06224856, -0.00102826, -132.03061525, -0.01454831, -13.20306153, -0.04516884, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 117.00009634, 0.02056529, 117.00009634, 0.06169588, 81.90006743, -1087.45967053, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 29.25002408, 7.328e-05, 87.75007225, 0.00021983, 292.50024084, 0.00073278, -29.25002408, -7.328e-05, -87.75007225, -0.00021983, -292.50024084, -0.00073278, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 117.00009634, 0.02056529, 117.00009634, 0.06169588, 81.90006743, -1087.45967053, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 29.25002408, 7.328e-05, 87.75007225, 0.00021983, 292.50024084, 0.00073278, -29.25002408, -7.328e-05, -87.75007225, -0.00021983, -292.50024084, -0.00073278, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 15.8, 9.75)
    ops.node(124017, 0.0, 15.8, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 27613911.03063542, 11505796.26276476, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 25.18696715, 0.00125171, 30.72763892, 0.01946489, 3.07276389, 0.07854901, -25.18696715, -0.00125171, -30.72763892, -0.01946489, -3.07276389, -0.07854901, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 25.18696715, 0.00125171, 30.72763892, 0.01946489, 3.07276389, 0.07854901, -25.18696715, -0.00125171, -30.72763892, -0.01946489, -3.07276389, -0.07854901, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 75.66916101, 0.02503422, 75.66916101, 0.07510265, 52.96841271, -2126.29443714, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 18.91729025, 9.944e-05, 56.75187076, 0.00029832, 189.17290254, 0.00099438, -18.91729025, -9.944e-05, -56.75187076, -0.00029832, -189.17290254, -0.00099438, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 75.66916101, 0.02503422, 75.66916101, 0.07510265, 52.96841271, -2126.29443714, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 18.91729025, 9.944e-05, 56.75187076, 0.00029832, 189.17290254, 0.00099438, -18.91729025, -9.944e-05, -56.75187076, -0.00029832, -189.17290254, -0.00099438, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 3.05, 15.8, 9.75)
    ops.node(124018, 3.05, 15.8, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1225, 27744747.66448511, 11560311.5268688, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 81.38992539, 0.00089946, 99.06053725, 0.01697868, 9.90605373, 0.05991677, -81.38992539, -0.00089946, -99.06053725, -0.01697868, -9.90605373, -0.05991677, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 69.98689248, 0.00089946, 85.18178554, 0.01697868, 8.51817855, 0.05991677, -69.98689248, -0.00089946, -85.18178554, -0.01697868, -8.51817855, -0.05991677, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 129.78533779, 0.01798925, 129.78533779, 0.05396776, 90.84973645, -2060.92322578, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 32.44633445, 8.661e-05, 97.33900334, 0.00025982, 324.46334447, 0.00086607, -32.44633445, -8.661e-05, -97.33900334, -0.00025982, -324.46334447, -0.00086607, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 129.78533779, 0.01798925, 129.78533779, 0.05396776, 90.84973645, -2060.92322578, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 32.44633445, 8.661e-05, 97.33900334, 0.00025982, 324.46334447, 0.00086607, -32.44633445, -8.661e-05, -97.33900334, -0.00025982, -324.46334447, -0.00086607, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 9.0, 15.8, 9.75)
    ops.node(124019, 9.0, 15.8, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1225, 27358059.12289379, 11399191.30120574, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 95.20684768, 0.00099115, 115.68988287, 0.01657158, 11.56898829, 0.05149217, -95.20684768, -0.00099115, -115.68988287, -0.01657158, -11.56898829, -0.05149217, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 89.70787566, 0.00099115, 109.0078485, 0.01657158, 10.90078485, 0.05149217, -89.70787566, -0.00099115, -109.0078485, -0.01657158, -10.90078485, -0.05149217, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 122.24623915, 0.01982304, 122.24623915, 0.05946911, 85.57236741, -1510.68636889, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 30.56155979, 8.273e-05, 91.68467936, 0.00024819, 305.61559788, 0.00082729, -30.56155979, -8.273e-05, -91.68467936, -0.00024819, -305.61559788, -0.00082729, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 122.24623915, 0.01982304, 122.24623915, 0.05946911, 85.57236741, -1510.68636889, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 30.56155979, 8.273e-05, 91.68467936, 0.00024819, 305.61559788, 0.00082729, -30.56155979, -8.273e-05, -91.68467936, -0.00024819, -305.61559788, -0.00082729, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 14.95, 15.8, 9.75)
    ops.node(124020, 14.95, 15.8, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 27205570.22213296, 11335654.25922207, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 45.61387729, 0.00133553, 55.43673656, 0.01916557, 5.54367366, 0.06358787, -45.61387729, -0.00133553, -55.43673656, -0.01916557, -5.54367366, -0.06358787, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 45.61387729, 0.00133553, 55.43673656, 0.01916557, 5.54367366, 0.06358787, -45.61387729, -0.00133553, -55.43673656, -0.01916557, -5.54367366, -0.06358787, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 72.23591784, 0.02671067, 72.23591784, 0.08013201, 50.56514249, -1198.22857284, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 18.05897946, 9.635e-05, 54.17693838, 0.00028905, 180.58979459, 0.00096351, -18.05897946, -9.635e-05, -54.17693838, -0.00028905, -180.58979459, -0.00096351, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 72.23591784, 0.02671067, 72.23591784, 0.08013201, 50.56514249, -1198.22857284, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 18.05897946, 9.635e-05, 54.17693838, 0.00028905, 180.58979459, 0.00096351, -18.05897946, -9.635e-05, -54.17693838, -0.00028905, -180.58979459, -0.00096351, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124021, 0.0, 0.0, 1.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 170001, 124021, 0.0625, 27498258.771178, 11457607.82132417, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 57.33324799, 0.00096731, 68.4494213, 0.01401328, 6.84494213, 0.04477019, -57.33324799, -0.00096731, -68.4494213, -0.01401328, -6.84494213, -0.04477019, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 53.52836912, 0.00096731, 63.90682577, 0.01401328, 6.39068258, 0.04477019, -53.52836912, -0.00096731, -63.90682577, -0.01401328, -6.39068258, -0.04477019, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 93.26459496, 0.01934618, 93.26459496, 0.05803853, 65.28521647, -2561.01187152, 0.05, 2, 0, 70001, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 23.31614874, 6.154e-05, 69.94844622, 0.00018461, 233.16148739, 0.00061538, -23.31614874, -6.154e-05, -69.94844622, -0.00018461, -233.16148739, -0.00061538, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 93.26459496, 0.01934618, 93.26459496, 0.05803853, 65.28521647, -2561.01187152, 0.05, 2, 0, 70001, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 23.31614874, 6.154e-05, 69.94844622, 0.00018461, 233.16148739, 0.00061538, -23.31614874, -6.154e-05, -69.94844622, -0.00018461, -233.16148739, -0.00061538, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 0.0, 0.0, 1.775)
    ops.node(121001, 0.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 174021, 121001, 0.0625, 28548679.90146926, 11895283.29227886, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 45.52715482, 0.00093368, 54.54161436, 0.01475552, 5.45416144, 0.05162516, -45.52715482, -0.00093368, -54.54161436, -0.01475552, -5.45416144, -0.05162516, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 45.52715482, 0.00093368, 54.54161436, 0.01475552, 5.45416144, 0.05162516, -45.52715482, -0.00093368, -54.54161436, -0.01475552, -5.45416144, -0.05162516, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 93.00158365, 0.01867357, 93.00158365, 0.0560207, 65.10110856, -2516.33728488, 0.05, 2, 0, 74021, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 23.25039591, 5.911e-05, 69.75118774, 0.00017732, 232.50395913, 0.00059107, -23.25039591, -5.911e-05, -69.75118774, -0.00017732, -232.50395913, -0.00059107, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 93.00158365, 0.01867357, 93.00158365, 0.0560207, 65.10110856, -2516.33728488, 0.05, 2, 0, 74021, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 23.25039591, 5.911e-05, 69.75118774, 0.00017732, 232.50395913, 0.00059107, -23.25039591, -5.911e-05, -69.75118774, -0.00017732, -232.50395913, -0.00059107, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.05, 0.0, 0.0)
    ops.node(124022, 3.05, 0.0, 1.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 170002, 124022, 0.16, 28268445.41777076, 11778518.92407115, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 245.03251175, 0.00072889, 292.33357587, 0.01210239, 29.23335759, 0.0344598, -245.03251175, -0.00072889, -292.33357587, -0.01210239, -29.23335759, -0.0344598, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 253.09127489, 0.00072889, 301.94800225, 0.01210239, 30.19480022, 0.0344598, -253.09127489, -0.00072889, -301.94800225, -0.01210239, -30.19480022, -0.0344598, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 285.11886506, 0.01457788, 285.11886506, 0.04373365, 199.58320554, -4666.86075179, 0.05, 2, 0, 70002, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 71.27971626, 7.149e-05, 213.83914879, 0.00021446, 712.79716264, 0.00071485, -71.27971626, -7.149e-05, -213.83914879, -0.00021446, -712.79716264, -0.00071485, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 285.11886506, 0.01457788, 285.11886506, 0.04373365, 199.58320554, -4666.86075179, 0.05, 2, 0, 70002, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 71.27971626, 7.149e-05, 213.83914879, 0.00021446, 712.79716264, 0.00071485, -71.27971626, -7.149e-05, -213.83914879, -0.00021446, -712.79716264, -0.00071485, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 3.05, 0.0, 1.775)
    ops.node(121002, 3.05, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4055, 174022, 121002, 0.16, 27481665.46781997, 11450693.94492499, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24055, 202.72937481, 0.00071693, 242.09740575, 0.01190174, 24.20974058, 0.03360917, -202.72937481, -0.00071693, -242.09740575, -0.01190174, -24.20974058, -0.03360917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14055, 179.73183366, 0.00071693, 214.63397054, 0.01190174, 21.46339705, 0.03360917, -179.73183366, -0.00071693, -214.63397054, -0.01190174, -21.46339705, -0.03360917, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24055, 4055, 0.0, 275.31574947, 0.01433861, 275.31574947, 0.04301582, 192.72102463, -4604.84667465, 0.05, 2, 0, 74022, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44055, 68.82893737, 7.1e-05, 206.4868121, 0.00021301, 688.28937368, 0.00071004, -68.82893737, -7.1e-05, -206.4868121, -0.00021301, -688.28937368, -0.00071004, 0.4, 0.3, 0.003, 0.0, 0.0, 24055, 2)
    ops.limitCurve('ThreePoint', 14055, 4055, 0.0, 275.31574947, 0.01433861, 275.31574947, 0.04301582, 192.72102463, -4604.84667465, 0.05, 2, 0, 74022, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34055, 68.82893737, 7.1e-05, 206.4868121, 0.00021301, 688.28937368, 0.00071004, -68.82893737, -7.1e-05, -206.4868121, -0.00021301, -688.28937368, -0.00071004, 0.4, 0.3, 0.003, 0.0, 0.0, 14055, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4055, 99999, 'P', 44055, 'Vy', 34055, 'Vz', 24055, 'My', 14055, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4055, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4055, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.45)
    ops.node(124023, 0.0, 0.0, 4.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 171001, 124023, 0.0625, 25944895.63551983, 10810373.1814666, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 41.16584394, 0.00096111, 49.44673933, 0.01468846, 4.94467393, 0.04790154, -41.16584394, -0.00096111, -49.44673933, -0.01468846, -4.94467393, -0.04790154, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 41.16584394, 0.00096111, 49.44673933, 0.01468846, 4.94467393, 0.04790154, -41.16584394, -0.00096111, -49.44673933, -0.01468846, -4.94467393, -0.04790154, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 85.99930952, 0.01922211, 85.99930952, 0.05766634, 60.19951666, -2527.38486085, 0.05, 2, 0, 71001, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 21.49982738, 6.014e-05, 64.49948214, 0.00018043, 214.9982738, 0.00060142, -21.49982738, -6.014e-05, -64.49948214, -0.00018043, -214.9982738, -0.00060142, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 85.99930952, 0.01922211, 85.99930952, 0.05766634, 60.19951666, -2527.38486085, 0.05, 2, 0, 71001, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 21.49982738, 6.014e-05, 64.49948214, 0.00018043, 214.9982738, 0.00060142, -21.49982738, -6.014e-05, -64.49948214, -0.00018043, -214.9982738, -0.00060142, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 0.0, 0.0, 4.925)
    ops.node(122001, 0.0, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 174023, 122001, 0.0625, 28437746.00914134, 11849060.83714222, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 38.27171689, 0.00089357, 46.12721458, 0.01612649, 4.61272146, 0.05988578, -38.27171689, -0.00089357, -46.12721458, -0.01612649, -4.61272146, -0.05988578, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 38.27171689, 0.00089357, 46.12721458, 0.01612649, 4.61272146, 0.05988578, -38.27171689, -0.00089357, -46.12721458, -0.01612649, -4.61272146, -0.05988578, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 87.79251216, 0.01787132, 87.79251216, 0.05361396, 61.45475851, -2522.21234963, 0.05, 2, 0, 74023, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 21.94812804, 5.601e-05, 65.84438412, 0.00016804, 219.4812804, 0.00056014, -21.94812804, -5.601e-05, -65.84438412, -0.00016804, -219.4812804, -0.00056014, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 87.79251216, 0.01787132, 87.79251216, 0.05361396, 61.45475851, -2522.21234963, 0.05, 2, 0, 74023, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 21.94812804, 5.601e-05, 65.84438412, 0.00016804, 219.4812804, 0.00056014, -21.94812804, -5.601e-05, -65.84438412, -0.00016804, -219.4812804, -0.00056014, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.05, 0.0, 3.45)
    ops.node(124024, 3.05, 0.0, 4.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 171002, 124024, 0.16, 27229633.27405487, 11345680.5308562, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 180.50718346, 0.00068862, 216.77314445, 0.0125511, 21.67731445, 0.03775789, -180.50718346, -0.00068862, -216.77314445, -0.0125511, -21.67731445, -0.03775789, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 157.16161423, 0.00068862, 188.73718293, 0.0125511, 18.87371829, 0.03775789, -157.16161423, -0.00068862, -188.73718293, -0.0125511, -18.87371829, -0.03775789, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 256.94581479, 0.01377245, 256.94581479, 0.04131736, 179.86207035, -4244.73796674, 0.05, 2, 0, 71002, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 64.2364537, 6.688e-05, 192.70936109, 0.00020064, 642.36453697, 0.00066879, -64.2364537, -6.688e-05, -192.70936109, -0.00020064, -642.36453697, -0.00066879, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 256.94581479, 0.01377245, 256.94581479, 0.04131736, 179.86207035, -4244.73796674, 0.05, 2, 0, 71002, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 64.2364537, 6.688e-05, 192.70936109, 0.00020064, 642.36453697, 0.00066879, -64.2364537, -6.688e-05, -192.70936109, -0.00020064, -642.36453697, -0.00066879, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 3.05, 0.0, 4.925)
    ops.node(122002, 3.05, 0.0, 6.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4060, 174024, 122002, 0.16, 27910660.76253617, 11629441.98439007, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24060, 172.28810539, 0.00069429, 207.19120087, 0.01343771, 20.71912009, 0.04103623, -172.28810539, -0.00069429, -207.19120087, -0.01343771, -20.71912009, -0.04103623, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14060, 150.90199491, 0.00069429, 181.47257159, 0.01343771, 18.14725716, 0.04103623, -150.90199491, -0.00069429, -181.47257159, -0.01343771, -18.14725716, -0.04103623, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24060, 4060, 0.0, 259.38193221, 0.01388586, 259.38193221, 0.04165758, 181.56735255, -4233.0225397, 0.05, 2, 0, 74024, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44060, 64.84548305, 6.587e-05, 194.53644916, 0.0001976, 648.45483052, 0.00065866, -64.84548305, -6.587e-05, -194.53644916, -0.0001976, -648.45483052, -0.00065866, 0.4, 0.3, 0.003, 0.0, 0.0, 24060, 2)
    ops.limitCurve('ThreePoint', 14060, 4060, 0.0, 259.38193221, 0.01388586, 259.38193221, 0.04165758, 181.56735255, -4233.0225397, 0.05, 2, 0, 74024, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34060, 64.84548305, 6.587e-05, 194.53644916, 0.0001976, 648.45483052, 0.00065866, -64.84548305, -6.587e-05, -194.53644916, -0.0001976, -648.45483052, -0.00065866, 0.4, 0.3, 0.003, 0.0, 0.0, 14060, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4060, 99999, 'P', 44060, 'Vy', 34060, 'Vz', 24060, 'My', 14060, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4060, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4060, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.6)
    ops.node(124025, 0.0, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 172001, 124025, 0.0625, 26159882.08283219, 10899950.86784675, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 35.10123962, 0.00088547, 42.50245063, 0.01657874, 4.25024506, 0.05936159, -35.10123962, -0.00088547, -42.50245063, -0.01657874, -4.25024506, -0.05936159, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 35.10123962, 0.00088547, 42.50245063, 0.01657874, 4.25024506, 0.05936159, -35.10123962, -0.00088547, -42.50245063, -0.01657874, -4.25024506, -0.05936159, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 81.6901021, 0.0177094, 81.6901021, 0.05312819, 57.18307147, -2665.32378399, 0.05, 2, 0, 72001, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 20.42252553, 5.666e-05, 61.26757658, 0.00016998, 204.22525525, 0.00056659, -20.42252553, -5.666e-05, -61.26757658, -0.00016998, -204.22525525, -0.00056659, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 81.6901021, 0.0177094, 81.6901021, 0.05312819, 57.18307147, -2665.32378399, 0.05, 2, 0, 72001, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 20.42252553, 5.666e-05, 61.26757658, 0.00016998, 204.22525525, 0.00056659, -20.42252553, -5.666e-05, -61.26757658, -0.00016998, -204.22525525, -0.00056659, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 0.0, 0.0, 8.075)
    ops.node(123001, 0.0, 0.0, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 174025, 123001, 0.0625, 28086811.52729093, 11702838.13637122, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 29.94959641, 0.00085441, 36.34888221, 0.01823634, 3.63488822, 0.07065315, -29.94959641, -0.00085441, -36.34888221, -0.01823634, -3.63488822, -0.07065315, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 29.94959641, 0.00085441, 36.34888221, 0.01823634, 3.63488822, 0.07065315, -29.94959641, -0.00085441, -36.34888221, -0.01823634, -3.63488822, -0.07065315, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 81.59435808, 0.01708824, 81.59435808, 0.05126471, 57.11605066, -2943.16340733, 0.05, 2, 0, 74025, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 20.39858952, 5.271e-05, 61.19576856, 0.00015813, 203.9858952, 0.0005271, -20.39858952, -5.271e-05, -61.19576856, -0.00015813, -203.9858952, -0.0005271, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 81.59435808, 0.01708824, 81.59435808, 0.05126471, 57.11605066, -2943.16340733, 0.05, 2, 0, 74025, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 20.39858952, 5.271e-05, 61.19576856, 0.00015813, 203.9858952, 0.0005271, -20.39858952, -5.271e-05, -61.19576856, -0.00015813, -203.9858952, -0.0005271, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.05, 0.0, 6.6)
    ops.node(124026, 3.05, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 172002, 124026, 0.1225, 27499623.79075484, 11458176.57948118, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 114.79188779, 0.00073246, 138.27603012, 0.01367294, 13.82760301, 0.04465849, -114.79188779, -0.00073246, -138.27603012, -0.01367294, -13.82760301, -0.04465849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 101.97551718, 0.00073246, 122.8376844, 0.01367294, 12.28376844, 0.04465849, -101.97551718, -0.00073246, -122.8376844, -0.01367294, -12.28376844, -0.04465849, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 181.28558072, 0.0146493, 181.28558072, 0.0439479, 126.8999065, -3517.19037891, 0.05, 2, 0, 72002, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 45.32139518, 6.103e-05, 135.96418554, 0.00018308, 453.2139518, 0.00061026, -45.32139518, -6.103e-05, -135.96418554, -0.00018308, -453.2139518, -0.00061026, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 181.28558072, 0.0146493, 181.28558072, 0.0439479, 126.8999065, -3517.19037891, 0.05, 2, 0, 72002, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 45.32139518, 6.103e-05, 135.96418554, 0.00018308, 453.2139518, 0.00061026, -45.32139518, -6.103e-05, -135.96418554, -0.00018308, -453.2139518, -0.00061026, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 3.05, 0.0, 8.075)
    ops.node(123002, 3.05, 0.0, 9.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 174026, 123002, 0.1225, 27730299.67653756, 11554291.53189065, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 105.01700684, 0.00072199, 126.74851088, 0.01440716, 12.67485109, 0.04780174, -105.01700684, -0.00072199, -126.74851088, -0.01440716, -12.67485109, -0.04780174, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 93.71483706, 0.00072199, 113.10754707, 0.01440716, 11.31075471, 0.04780174, -93.71483706, -0.00072199, -113.10754707, -0.01440716, -11.31075471, -0.04780174, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 177.67554644, 0.01443979, 177.67554644, 0.04331937, 124.37288251, -3456.82429862, 0.05, 2, 0, 74026, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 44.41888661, 5.931e-05, 133.25665983, 0.00017794, 444.1888661, 0.00059313, -44.41888661, -5.931e-05, -133.25665983, -0.00017794, -444.1888661, -0.00059313, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 177.67554644, 0.01443979, 177.67554644, 0.04331937, 124.37288251, -3456.82429862, 0.05, 2, 0, 74026, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 44.41888661, 5.931e-05, 133.25665983, 0.00017794, 444.1888661, 0.00059313, -44.41888661, -5.931e-05, -133.25665983, -0.00017794, -444.1888661, -0.00059313, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.75)
    ops.node(124027, 0.0, 0.0, 10.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4067, 173001, 124027, 0.0625, 27558125.32389544, 11482552.21828977, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24067, 26.41041037, 0.00084527, 32.19621613, 0.01883129, 3.21962161, 0.07638508, -26.41041037, -0.00084527, -32.19621613, -0.01883129, -3.21962161, -0.07638508, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14067, 26.41041037, 0.00084527, 32.19621613, 0.01883129, 3.21962161, 0.07638508, -26.41041037, -0.00084527, -32.19621613, -0.01883129, -3.21962161, -0.07638508, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24067, 4067, 0.0, 76.70765792, 0.01690538, 76.70765792, 0.05071613, 53.69536054, -3766.24605619, 0.05, 2, 0, 73001, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44067, 19.17691448, 5.05e-05, 57.53074344, 0.00015151, 191.76914479, 0.00050504, -19.17691448, -5.05e-05, -57.53074344, -0.00015151, -191.76914479, -0.00050504, 0.4, 0.3, 0.003, 0.0, 0.0, 24067, 2)
    ops.limitCurve('ThreePoint', 14067, 4067, 0.0, 76.70765792, 0.01690538, 76.70765792, 0.05071613, 53.69536054, -3766.24605619, 0.05, 2, 0, 73001, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34067, 19.17691448, 5.05e-05, 57.53074344, 0.00015151, 191.76914479, 0.00050504, -19.17691448, -5.05e-05, -57.53074344, -0.00015151, -191.76914479, -0.00050504, 0.4, 0.3, 0.003, 0.0, 0.0, 14067, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4067, 99999, 'P', 44067, 'Vy', 34067, 'Vz', 24067, 'My', 14067, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4067, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4067, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 0.0, 0.0, 11.225)
    ops.node(124001, 0.0, 0.0, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 174027, 124001, 0.0625, 27419561.66541083, 11424817.36058785, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 22.08161371, 0.00080499, 27.03228618, 0.0198082, 2.70322862, 0.08438614, -22.08161371, -0.00080499, -27.03228618, -0.0198082, -2.70322862, -0.08438614, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 22.08161371, 0.00080499, 27.03228618, 0.0198082, 2.70322862, 0.08438614, -22.08161371, -0.00080499, -27.03228618, -0.0198082, -2.70322862, -0.08438614, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 72.13201667, 0.01609974, 72.13201667, 0.04829921, 50.49241167, -11190.03581667, 0.05, 2, 0, 74027, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 18.03300417, 4.773e-05, 54.0990125, 0.00014319, 180.33004167, 0.00047731, -18.03300417, -4.773e-05, -54.0990125, -0.00014319, -180.33004167, -0.00047731, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 72.13201667, 0.01609974, 72.13201667, 0.04829921, 50.49241167, -11190.03581667, 0.05, 2, 0, 74027, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 18.03300417, 4.773e-05, 54.0990125, 0.00014319, 180.33004167, 0.00047731, -18.03300417, -4.773e-05, -54.0990125, -0.00014319, -180.33004167, -0.00047731, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.05, 0.0, 9.75)
    ops.node(124028, 3.05, 0.0, 10.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 173002, 124028, 0.1225, 27843225.51297492, 11601343.96373955, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 81.63232829, 0.00069314, 99.29699271, 0.0163273, 9.92969927, 0.05882364, -81.63232829, -0.00069314, -99.29699271, -0.0163273, -9.92969927, -0.05882364, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 70.89619199, 0.00069314, 86.23763167, 0.0163273, 8.62376317, 0.05882364, -70.89619199, -0.00069314, -86.23763167, -0.0163273, -8.62376317, -0.05882364, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 160.37738367, 0.01386285, 160.37738367, 0.04158856, 112.26416857, -3982.08309903, 0.05, 2, 0, 73002, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 40.09434592, 5.332e-05, 120.28303775, 0.00015996, 400.94345918, 0.00053321, -40.09434592, -5.332e-05, -120.28303775, -0.00015996, -400.94345918, -0.00053321, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 160.37738367, 0.01386285, 160.37738367, 0.04158856, 112.26416857, -3982.08309903, 0.05, 2, 0, 73002, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 40.09434592, 5.332e-05, 120.28303775, 0.00015996, 400.94345918, 0.00053321, -40.09434592, -5.332e-05, -120.28303775, -0.00015996, -400.94345918, -0.00053321, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 3.05, 0.0, 11.225)
    ops.node(124002, 3.05, 0.0, 12.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 174028, 124002, 0.1225, 29385691.93850982, 12244038.30771242, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 78.37267827, 0.00067534, 95.20730106, 0.01633637, 9.52073011, 0.06248104, -78.37267827, -0.00067534, -95.20730106, -0.01633637, -9.52073011, -0.06248104, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 66.92560351, 0.00067534, 81.30136959, 0.01633637, 8.13013696, 0.06248104, -66.92560351, -0.00067534, -81.30136959, -0.01633637, -8.13013696, -0.06248104, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 162.04383209, 0.01350687, 162.04383209, 0.04052061, 113.43068246, -4569.07127412, 0.05, 2, 0, 74028, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 40.51095802, 5.105e-05, 121.53287407, 0.00015314, 405.10958022, 0.00051047, -40.51095802, -5.105e-05, -121.53287407, -0.00015314, -405.10958022, -0.00051047, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 162.04383209, 0.01350687, 162.04383209, 0.04052061, 113.43068246, -4569.07127412, 0.05, 2, 0, 74028, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 40.51095802, 5.105e-05, 121.53287407, 0.00015314, 405.10958022, 0.00051047, -40.51095802, -5.105e-05, -121.53287407, -0.00015314, -405.10958022, -0.00051047, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4070, '-orient', 0, 0, 1, 0, 1, 0)
