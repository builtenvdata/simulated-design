import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 24563224.2069678, 10234676.75290325, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 80.03808286, 0.00059793, 94.13589088, 0.00733571, 9.41358909, 0.02151078, -80.03808286, -0.00059793, -94.13589088, -0.00733571, -9.41358909, -0.02151078, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 74.14702946, 0.00059793, 87.20719469, 0.00733571, 8.72071947, 0.02151078, -74.14702946, -0.00059793, -87.20719469, -0.00733571, -8.72071947, -0.02151078, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 114.46821302, 0.0119585, 114.46821302, 0.03587551, 80.12774911, -1769.86472072, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 28.61705325, 0.00010439, 85.85115976, 0.00031316, 286.17053254, 0.00104387, -28.61705325, -0.00010439, -85.85115976, -0.00031316, -286.17053254, -0.00104387, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 114.46821302, 0.0119585, 114.46821302, 0.03587551, 80.12774911, -1769.86472072, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 28.61705325, 0.00010439, 85.85115976, 0.00031316, 286.17053254, 0.00104387, -28.61705325, -0.00010439, -85.85115976, -0.00031316, -286.17053254, -0.00104387, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.0, 0.0, 0.0)
    ops.node(121004, 13.0, 0.0, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.09, 27810128.47716095, 11587553.5321504, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 127.61558099, 0.00102781, 151.4574209, 0.00858048, 15.14574209, 0.03143611, -127.61558099, -0.00102781, -151.4574209, -0.00858048, -15.14574209, -0.03143611, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 116.20022769, 0.00102781, 137.90938894, 0.00858048, 13.79093889, 0.03143611, -116.20022769, -0.00102781, -137.90938894, -0.00858048, -13.79093889, -0.03143611, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 120.12585448, 0.02055614, 120.12585448, 0.06166841, 84.08809814, -1674.9466136, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 30.03146362, 9.676e-05, 90.09439086, 0.00029027, 300.31463621, 0.00096757, -30.03146362, -9.676e-05, -90.09439086, -0.00029027, -300.31463621, -0.00096757, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 120.12585448, 0.02055614, 120.12585448, 0.06166841, 84.08809814, -1674.9466136, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 30.03146362, 9.676e-05, 90.09439086, 0.00029027, 300.31463621, 0.00096757, -30.03146362, -9.676e-05, -90.09439086, -0.00029027, -300.31463621, -0.00096757, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.4, 0.0)
    ops.node(121005, 0.0, 4.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.16, 27334274.68746622, 11389281.11977759, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 302.84853425, 0.00085766, 360.09900322, 0.00821409, 36.00990032, 0.02487499, -302.84853425, -0.00085766, -360.09900322, -0.00821409, -36.00990032, -0.02487499, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 286.79446101, 0.00085766, 341.01006894, 0.00821409, 34.10100689, 0.02487499, -286.79446101, -0.00085766, -341.01006894, -0.00821409, -34.10100689, -0.02487499, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 181.31628482, 0.01715322, 181.31628482, 0.05145966, 126.92139937, -2297.23995654, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 45.3290712, 8.358e-05, 135.98721361, 0.00025074, 453.29071204, 0.0008358, -45.3290712, -8.358e-05, -135.98721361, -0.00025074, -453.29071204, -0.0008358, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 181.31628482, 0.01715322, 181.31628482, 0.05145966, 126.92139937, -2297.23995654, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 45.3290712, 8.358e-05, 135.98721361, 0.00025074, 453.29071204, 0.0008358, -45.3290712, -8.358e-05, -135.98721361, -0.00025074, -453.29071204, -0.0008358, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 5.05, 4.4, 0.0)
    ops.node(121006, 5.05, 4.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.25, 27271838.44193284, 11363266.01747202, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 478.48943064, 0.00071894, 573.78323011, 0.00858461, 57.37832301, 0.02426164, -478.48943064, -0.00071894, -573.78323011, -0.00858461, -57.37832301, -0.02426164, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 516.16033142, 0.00071894, 618.95649778, 0.00858461, 61.89564978, 0.02426164, -516.16033142, -0.00071894, -618.95649778, -0.00858461, -61.89564978, -0.02426164, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 263.01307523, 0.01437873, 263.01307523, 0.04313618, 184.10915266, -2502.46436157, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 65.75326881, 7.777e-05, 197.25980642, 0.00023331, 657.53268807, 0.0007777, -65.75326881, -7.777e-05, -197.25980642, -0.00023331, -657.53268807, -0.0007777, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 263.01307523, 0.01437873, 263.01307523, 0.04313618, 184.10915266, -2502.46436157, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 65.75326881, 7.777e-05, 197.25980642, 0.00023331, 657.53268807, 0.0007777, -65.75326881, -7.777e-05, -197.25980642, -0.00023331, -657.53268807, -0.0007777, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 7.95, 4.4, 0.0)
    ops.node(121007, 7.95, 4.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.25, 26885105.66811134, 11202127.36171306, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 480.27606922, 0.00071531, 575.81827599, 0.0087302, 57.5818276, 0.02390887, -480.27606922, -0.00071531, -575.81827599, -0.0087302, -57.5818276, -0.02390887, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 518.87844477, 0.00071531, 622.09989351, 0.0087302, 62.20998935, 0.02390887, -518.87844477, -0.00071531, -622.09989351, -0.0087302, -62.20998935, -0.02390887, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 261.84815519, 0.01430624, 261.84815519, 0.04291871, 183.29370863, -2550.42092403, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 65.4620388, 7.854e-05, 196.38611639, 0.00023562, 654.62038797, 0.0007854, -65.4620388, -7.854e-05, -196.38611639, -0.00023562, -654.62038797, -0.0007854, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 261.84815519, 0.01430624, 261.84815519, 0.04291871, 183.29370863, -2550.42092403, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 65.4620388, 7.854e-05, 196.38611639, 0.00023562, 654.62038797, 0.0007854, -65.4620388, -7.854e-05, -196.38611639, -0.00023562, -654.62038797, -0.0007854, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 13.0, 4.4, 0.0)
    ops.node(121008, 13.0, 4.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.16, 26269377.68789311, 10945574.03662213, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 304.25214929, 0.00083643, 361.07605607, 0.0080672, 36.10760561, 0.02271196, -304.25214929, -0.00083643, -361.07605607, -0.0080672, -36.10760561, -0.02271196, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 287.15679364, 0.00083643, 340.78787204, 0.0080672, 34.0787872, 0.02271196, -287.15679364, -0.00083643, -340.78787204, -0.0080672, -34.0787872, -0.02271196, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 175.66146551, 0.0167286, 175.66146551, 0.0501858, 122.96302586, -2295.68460774, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 43.91536638, 8.426e-05, 131.74609913, 0.00025277, 439.15366378, 0.00084255, -43.91536638, -8.426e-05, -131.74609913, -0.00025277, -439.15366378, -0.00084255, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 175.66146551, 0.0167286, 175.66146551, 0.0501858, 122.96302586, -2295.68460774, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 43.91536638, 8.426e-05, 131.74609913, 0.00025277, 439.15366378, 0.00084255, -43.91536638, -8.426e-05, -131.74609913, -0.00025277, -439.15366378, -0.00084255, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.8, 0.0)
    ops.node(121009, 0.0, 8.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 28110010.77032863, 11712504.48763693, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 306.71851946, 0.00087242, 364.99961195, 0.00799802, 36.4999612, 0.02306137, -306.71851946, -0.00087242, -364.99961195, -0.00799802, -36.4999612, -0.02306137, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 292.44944619, 0.00087242, 348.01920197, 0.00799802, 34.8019202, 0.02306137, -292.44944619, -0.00087242, -348.01920197, -0.00799802, -34.8019202, -0.02306137, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 175.87021586, 0.01744832, 175.87021586, 0.05234495, 123.1091511, -2097.35430845, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 43.96755397, 7.883e-05, 131.9026619, 0.0002365, 439.67553965, 0.00078832, -43.96755397, -7.883e-05, -131.9026619, -0.0002365, -439.67553965, -0.00078832, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 175.87021586, 0.01744832, 175.87021586, 0.05234495, 123.1091511, -2097.35430845, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 43.96755397, 7.883e-05, 131.9026619, 0.0002365, 439.67553965, 0.00078832, -43.96755397, -7.883e-05, -131.9026619, -0.0002365, -439.67553965, -0.00078832, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 5.05, 8.8, 0.0)
    ops.node(121010, 5.05, 8.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.2025, 26746085.64158459, 11144202.35066025, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 386.64601755, 0.00077229, 461.51758182, 0.00858055, 46.15175818, 0.02255409, -386.64601755, -0.00077229, -461.51758182, -0.00858055, -46.15175818, -0.02255409, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 402.70945545, 0.00077229, 480.69160321, 0.00858055, 48.06916032, 0.02255409, -402.70945545, -0.00077229, -480.69160321, -0.00858055, -48.06916032, -0.02255409, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 208.87002866, 0.01544572, 208.87002866, 0.04633715, 146.20902006, -2408.07143252, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 52.21750716, 7.775e-05, 156.65252149, 0.00023324, 522.17507164, 0.00077747, -52.21750716, -7.775e-05, -156.65252149, -0.00023324, -522.17507164, -0.00077747, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 208.87002866, 0.01544572, 208.87002866, 0.04633715, 146.20902006, -2408.07143252, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 52.21750716, 7.775e-05, 156.65252149, 0.00023324, 522.17507164, 0.00077747, -52.21750716, -7.775e-05, -156.65252149, -0.00023324, -522.17507164, -0.00077747, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.95, 8.8, 0.0)
    ops.node(121011, 7.95, 8.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 26590806.84649917, 11079502.85270799, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 396.09258024, 0.00075798, 472.6979106, 0.00763973, 47.26979106, 0.02138618, -396.09258024, -0.00075798, -472.6979106, -0.00763973, -47.26979106, -0.02138618, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 413.61703861, 0.00075798, 493.61164459, 0.00763973, 49.36116446, 0.02138618, -413.61703861, -0.00075798, -493.61164459, -0.00763973, -49.36116446, -0.02138618, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 202.21129104, 0.01515956, 202.21129104, 0.04547869, 141.54790373, -2290.9249858, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 50.55282276, 7.571e-05, 151.65846828, 0.00022712, 505.5282276, 0.00075708, -50.55282276, -7.571e-05, -151.65846828, -0.00022712, -505.5282276, -0.00075708, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 202.21129104, 0.01515956, 202.21129104, 0.04547869, 141.54790373, -2290.9249858, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 50.55282276, 7.571e-05, 151.65846828, 0.00022712, 505.5282276, 0.00075708, -50.55282276, -7.571e-05, -151.65846828, -0.00022712, -505.5282276, -0.00075708, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 13.0, 8.8, 0.0)
    ops.node(121012, 13.0, 8.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 28118265.11555659, 11715943.79814858, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 300.15709104, 0.00086456, 357.19367177, 0.00872167, 35.71936718, 0.02379725, -300.15709104, -0.00086456, -357.19367177, -0.00872167, -35.71936718, -0.02379725, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 286.54374647, 0.00086456, 340.99348635, 0.00872167, 34.09934864, 0.02379725, -286.54374647, -0.00086456, -340.99348635, -0.00872167, -34.09934864, -0.02379725, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 180.82286881, 0.01729111, 180.82286881, 0.05187332, 126.57600816, -2198.84845316, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 45.2057172, 8.103e-05, 135.6171516, 0.00024308, 452.05717202, 0.00081028, -45.2057172, -8.103e-05, -135.6171516, -0.00024308, -452.05717202, -0.00081028, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 180.82286881, 0.01729111, 180.82286881, 0.05187332, 126.57600816, -2198.84845316, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 45.2057172, 8.103e-05, 135.6171516, 0.00024308, 452.05717202, 0.00081028, -45.2057172, -8.103e-05, -135.6171516, -0.00024308, -452.05717202, -0.00081028, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 13.2, 0.0)
    ops.node(121013, 0.0, 13.2, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.09, 27724003.17264619, 11551667.98860258, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 130.67158466, 0.00104181, 155.06683392, 0.01014269, 15.50668339, 0.02989198, -130.67158466, -0.00104181, -155.06683392, -0.01014269, -15.50668339, -0.02989198, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 118.87100671, 0.00104181, 141.06319063, 0.01014269, 14.10631906, 0.02989198, -118.87100671, -0.00104181, -141.06319063, -0.01014269, -14.10631906, -0.02989198, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 122.55116952, 0.02083629, 122.55116952, 0.06250888, 85.78581867, -1738.3555476, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 30.63779238, 9.902e-05, 91.91337714, 0.00029705, 306.37792381, 0.00099017, -30.63779238, -9.902e-05, -91.91337714, -0.00029705, -306.37792381, -0.00099017, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 122.55116952, 0.02083629, 122.55116952, 0.06250888, 85.78581867, -1738.3555476, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 30.63779238, 9.902e-05, 91.91337714, 0.00029705, 306.37792381, 0.00099017, -30.63779238, -9.902e-05, -91.91337714, -0.00029705, -306.37792381, -0.00099017, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 5.05, 13.2, 0.0)
    ops.node(121014, 5.05, 13.2, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.1225, 25831942.59450376, 10763309.41437657, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 187.79872002, 0.00091692, 222.26554624, 0.00928695, 22.22655462, 0.02367058, -187.79872002, -0.00091692, -222.26554624, -0.00928695, -22.22655462, -0.02367058, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 187.79872002, 0.00091692, 222.26554624, 0.00928695, 22.22655462, 0.02367058, -187.79872002, -0.00091692, -222.26554624, -0.00928695, -22.22655462, -0.02367058, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 144.87351915, 0.01833849, 144.87351915, 0.05501547, 101.41146341, -2032.42898736, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 36.21837979, 9.23e-05, 108.65513937, 0.00027689, 362.18379788, 0.00092297, -36.21837979, -9.23e-05, -108.65513937, -0.00027689, -362.18379788, -0.00092297, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 144.87351915, 0.01833849, 144.87351915, 0.05501547, 101.41146341, -2032.42898736, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 36.21837979, 9.23e-05, 108.65513937, 0.00027689, 362.18379788, 0.00092297, -36.21837979, -9.23e-05, -108.65513937, -0.00027689, -362.18379788, -0.00092297, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.95, 13.2, 0.0)
    ops.node(121015, 7.95, 13.2, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.1225, 27659086.01206975, 11524619.17169573, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 195.03841833, 0.00090391, 231.69647117, 0.00955066, 23.16964712, 0.02772671, -195.03841833, -0.00090391, -231.69647117, -0.00955066, -23.16964712, -0.02772671, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 195.03841833, 0.00090391, 231.69647117, 0.00955066, 23.16964712, 0.02772671, -195.03841833, -0.00090391, -231.69647117, -0.00955066, -23.16964712, -0.02772671, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 152.88504789, 0.01807811, 152.88504789, 0.05423434, 107.01953353, -2046.38216105, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 38.22126197, 9.097e-05, 114.66378592, 0.0002729, 382.21261973, 0.00090967, -38.22126197, -9.097e-05, -114.66378592, -0.0002729, -382.21261973, -0.00090967, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 152.88504789, 0.01807811, 152.88504789, 0.05423434, 107.01953353, -2046.38216105, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 38.22126197, 9.097e-05, 114.66378592, 0.0002729, 382.21261973, 0.00090967, -38.22126197, -9.097e-05, -114.66378592, -0.0002729, -382.21261973, -0.00090967, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 13.0, 13.2, 0.0)
    ops.node(121016, 13.0, 13.2, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.09, 26153874.46889042, 10897447.69537101, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 125.66666099, 0.00105891, 148.65477003, 0.00875475, 14.865477, 0.02489208, -125.66666099, -0.00105891, -148.65477003, -0.00875475, -14.865477, -0.02489208, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 114.87121087, 0.00105891, 135.88451623, 0.00875475, 13.58845162, 0.02489208, -114.87121087, -0.00105891, -135.88451623, -0.00875475, -13.58845162, -0.02489208, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 113.25910093, 0.0211782, 113.25910093, 0.06353459, 79.28137065, -1630.98985567, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 28.31477523, 9.7e-05, 84.9443257, 0.00029101, 283.14775232, 0.00097003, -28.31477523, -9.7e-05, -84.9443257, -0.00029101, -283.14775232, -0.00097003, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 113.25910093, 0.0211782, 113.25910093, 0.06353459, 79.28137065, -1630.98985567, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 28.31477523, 9.7e-05, 84.9443257, 0.00029101, 283.14775232, 0.00097003, -28.31477523, -9.7e-05, -84.9443257, -0.00029101, -283.14775232, -0.00097003, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.075)
    ops.node(122001, 0.0, 0.0, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 28943108.3151231, 12059628.46463462, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 105.22991352, 0.00103078, 125.92025765, 0.01135586, 12.59202576, 0.04322446, -105.22991352, -0.00103078, -125.92025765, -0.01135586, -12.59202576, -0.04322446, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 90.95916698, 0.00103078, 108.8435917, 0.01135586, 10.88435917, 0.04322446, -90.95916698, -0.00103078, -108.8435917, -0.01135586, -10.88435917, -0.04322446, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 122.53837405, 0.02061566, 122.53837405, 0.06184698, 85.77686184, -1686.4474801, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 30.63459351, 9.484e-05, 91.90378054, 0.00028451, 306.34593513, 0.00094836, -30.63459351, -9.484e-05, -91.90378054, -0.00028451, -306.34593513, -0.00094836, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 122.53837405, 0.02061566, 122.53837405, 0.06184698, 85.77686184, -1686.4474801, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 30.63459351, 9.484e-05, 91.90378054, 0.00028451, 306.34593513, 0.00094836, -30.63459351, -9.484e-05, -91.90378054, -0.00028451, -306.34593513, -0.00094836, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.0, 0.0, 3.075)
    ops.node(122004, 13.0, 0.0, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.09, 29403977.48437407, 12251657.28515586, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 99.85373771, 0.0009907, 119.45826393, 0.0120659, 11.94582639, 0.04492977, -99.85373771, -0.0009907, -119.45826393, -0.0120659, -11.94582639, -0.04492977, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 87.1443207, 0.0009907, 104.2535763, 0.0120659, 10.42535763, 0.04492977, -87.1443207, -0.0009907, -104.2535763, -0.0120659, -10.42535763, -0.04492977, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 125.73769831, 0.01981394, 125.73769831, 0.05944183, 88.01638882, -1737.43155011, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 31.43442458, 9.579e-05, 94.30327373, 0.00028736, 314.34424577, 0.00095787, -31.43442458, -9.579e-05, -94.30327373, -0.00028736, -314.34424577, -0.00095787, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 125.73769831, 0.01981394, 125.73769831, 0.05944183, 88.01638882, -1737.43155011, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 31.43442458, 9.579e-05, 94.30327373, 0.00028736, 314.34424577, 0.00095787, -31.43442458, -9.579e-05, -94.30327373, -0.00028736, -314.34424577, -0.00095787, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.4, 3.1)
    ops.node(122005, 0.0, 4.4, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.16, 27578734.12184899, 11491139.21743708, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 224.06587601, 0.00077303, 268.52786094, 0.00976374, 26.85278609, 0.03119983, -224.06587601, -0.00077303, -268.52786094, -0.00976374, -26.85278609, -0.03119983, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 194.58533687, 0.00077303, 233.19742037, 0.00976374, 23.31974204, 0.03119983, -194.58533687, -0.00077303, -233.19742037, -0.00976374, -23.31974204, -0.03119983, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 172.7030807, 0.01546061, 172.7030807, 0.04638184, 120.89215649, -2045.24916239, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 43.17577017, 7.89e-05, 129.52731052, 0.00023671, 431.75770174, 0.00078904, -43.17577017, -7.89e-05, -129.52731052, -0.00023671, -431.75770174, -0.00078904, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 172.7030807, 0.01546061, 172.7030807, 0.04638184, 120.89215649, -2045.24916239, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 43.17577017, 7.89e-05, 129.52731052, 0.00023671, 431.75770174, 0.00078904, -43.17577017, -7.89e-05, -129.52731052, -0.00023671, -431.75770174, -0.00078904, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 5.05, 4.4, 3.1)
    ops.node(122006, 5.05, 4.4, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.25, 29347858.64705681, 12228274.43627367, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 323.40415317, 0.00067616, 389.27621349, 0.0075192, 38.92762135, 0.02809101, -323.40415317, -0.00067616, -389.27621349, -0.0075192, -38.92762135, -0.02809101, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 305.15816289, 0.00067616, 367.31381771, 0.0075192, 36.73138177, 0.02809101, -305.15816289, -0.00067616, -367.31381771, -0.0075192, -36.73138177, -0.02809101, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 257.38883294, 0.01352319, 257.38883294, 0.04056957, 180.17218306, -2009.44866628, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 64.34720824, 7.072e-05, 193.04162471, 0.00021217, 643.47208236, 0.00070724, -64.34720824, -7.072e-05, -193.04162471, -0.00021217, -643.47208236, -0.00070724, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 257.38883294, 0.01352319, 257.38883294, 0.04056957, 180.17218306, -2009.44866628, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 64.34720824, 7.072e-05, 193.04162471, 0.00021217, 643.47208236, 0.00070724, -64.34720824, -7.072e-05, -193.04162471, -0.00021217, -643.47208236, -0.00070724, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 7.95, 4.4, 3.1)
    ops.node(122007, 7.95, 4.4, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.25, 25367381.45314012, 10569742.27214172, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 305.26479744, 0.00066675, 367.91362938, 0.00913963, 36.79136294, 0.0252494, -305.26479744, -0.00066675, -367.91362938, -0.00913963, -36.79136294, -0.0252494, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 288.44839894, 0.00066675, 347.6460379, 0.00913963, 34.76460379, 0.0252494, -288.44839894, -0.00066675, -347.6460379, -0.00913963, -34.76460379, -0.0252494, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 233.43583456, 0.01333495, 233.43583456, 0.04000484, 163.40508419, -2239.2768426, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 58.35895864, 7.421e-05, 175.07687592, 0.00022262, 583.5895864, 0.00074207, -58.35895864, -7.421e-05, -175.07687592, -0.00022262, -583.5895864, -0.00074207, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 233.43583456, 0.01333495, 233.43583456, 0.04000484, 163.40508419, -2239.2768426, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 58.35895864, 7.421e-05, 175.07687592, 0.00022262, 583.5895864, 0.00074207, -58.35895864, -7.421e-05, -175.07687592, -0.00022262, -583.5895864, -0.00074207, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 13.0, 4.4, 3.1)
    ops.node(122008, 13.0, 4.4, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.16, 27624437.34542678, 11510182.22726116, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 233.50458705, 0.00079719, 279.84252906, 0.01015905, 27.98425291, 0.03167299, -233.50458705, -0.00079719, -279.84252906, -0.01015905, -27.98425291, -0.03167299, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 201.75654005, 0.00079719, 241.79422398, 0.01015905, 24.1794224, 0.03167299, -201.75654005, -0.00079719, -241.79422398, -0.01015905, -24.1794224, -0.03167299, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 175.98187118, 0.01594387, 175.98187118, 0.04783162, 123.18730982, -2117.12891997, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 43.99546779, 8.027e-05, 131.98640338, 0.00024081, 439.95467795, 0.00080268, -43.99546779, -8.027e-05, -131.98640338, -0.00024081, -439.95467795, -0.00080268, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 175.98187118, 0.01594387, 175.98187118, 0.04783162, 123.18730982, -2117.12891997, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 43.99546779, 8.027e-05, 131.98640338, 0.00024081, 439.95467795, 0.00080268, -43.99546779, -8.027e-05, -131.98640338, -0.00024081, -439.95467795, -0.00080268, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.8, 3.1)
    ops.node(122009, 0.0, 8.8, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 25208998.17220958, 10503749.23842066, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 253.00632501, 0.00080658, 302.44462581, 0.00718275, 30.24446258, 0.02138194, -253.00632501, -0.00080658, -302.44462581, -0.00718275, -30.24446258, -0.02138194, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 225.16273389, 0.00080658, 269.16030182, 0.00718275, 26.91603018, 0.02138194, -225.16273389, -0.00080658, -269.16030182, -0.00718275, -26.91603018, -0.02138194, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 139.21899231, 0.01613165, 139.21899231, 0.04839496, 97.45329462, -1696.25787395, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 34.80474808, 6.958e-05, 104.41424424, 0.00020875, 348.04748079, 0.00069585, -34.80474808, -6.958e-05, -104.41424424, -0.00020875, -348.04748079, -0.00069585, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 139.21899231, 0.01613165, 139.21899231, 0.04839496, 97.45329462, -1696.25787395, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 34.80474808, 6.958e-05, 104.41424424, 0.00020875, 348.04748079, 0.00069585, -34.80474808, -6.958e-05, -104.41424424, -0.00020875, -348.04748079, -0.00069585, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 5.05, 8.8, 3.1)
    ops.node(122010, 5.05, 8.8, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.2025, 27304250.14761152, 11376770.89483813, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 269.21554442, 0.00071407, 323.58451063, 0.00805588, 32.35845106, 0.02591277, -269.21554442, -0.00071407, -323.58451063, -0.00805588, -32.35845106, -0.02591277, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 253.76743524, 0.00071407, 305.01660491, 0.00805588, 30.50166049, 0.02591277, -253.76743524, -0.00071407, -305.01660491, -0.00805588, -30.50166049, -0.02591277, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 189.71585198, 0.01428135, 189.71585198, 0.04284404, 132.80109638, -1882.73192568, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 47.42896299, 6.917e-05, 142.28688898, 0.00020752, 474.28962994, 0.00069173, -47.42896299, -6.917e-05, -142.28688898, -0.00020752, -474.28962994, -0.00069173, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 189.71585198, 0.01428135, 189.71585198, 0.04284404, 132.80109638, -1882.73192568, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 47.42896299, 6.917e-05, 142.28688898, 0.00020752, 474.28962994, 0.00069173, -47.42896299, -6.917e-05, -142.28688898, -0.00020752, -474.28962994, -0.00069173, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.95, 8.8, 3.1)
    ops.node(122011, 7.95, 8.8, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 25529056.92288116, 10637107.05120048, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 262.75106094, 0.00075431, 315.47087674, 0.0073068, 31.54708767, 0.02270099, -262.75106094, -0.00075431, -315.47087674, -0.0073068, -31.54708767, -0.02270099, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 248.84844259, 0.00075431, 298.7787607, 0.0073068, 29.87787607, 0.02270099, -248.84844259, -0.00075431, -298.7787607, -0.0073068, -29.87787607, -0.02270099, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 179.21032122, 0.01508626, 179.21032122, 0.04525878, 125.44722485, -1897.60194237, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 44.8025803, 6.989e-05, 134.40774091, 0.00020966, 448.02580305, 0.00069887, -44.8025803, -6.989e-05, -134.40774091, -0.00020966, -448.02580305, -0.00069887, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 179.21032122, 0.01508626, 179.21032122, 0.04525878, 125.44722485, -1897.60194237, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 44.8025803, 6.989e-05, 134.40774091, 0.00020966, 448.02580305, 0.00069887, -44.8025803, -6.989e-05, -134.40774091, -0.00020966, -448.02580305, -0.00069887, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 13.0, 8.8, 3.1)
    ops.node(122012, 13.0, 8.8, 5.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 25777876.2481099, 10740781.77004579, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 260.81027887, 0.00083425, 312.08246091, 0.00717573, 31.20824609, 0.02230891, -260.81027887, -0.00083425, -312.08246091, -0.00717573, -31.20824609, -0.02230891, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 232.18502178, 0.00083425, 277.82982058, 0.00717573, 27.78298206, 0.02230891, -232.18502178, -0.00083425, -277.82982058, -0.00717573, -27.78298206, -0.02230891, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 141.07324993, 0.01668504, 141.07324993, 0.05005512, 98.75127495, -1677.75165151, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 35.26831248, 6.896e-05, 105.80493744, 0.00020687, 352.68312482, 0.00068955, -35.26831248, -6.896e-05, -105.80493744, -0.00020687, -352.68312482, -0.00068955, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 141.07324993, 0.01668504, 141.07324993, 0.05005512, 98.75127495, -1677.75165151, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 35.26831248, 6.896e-05, 105.80493744, 0.00020687, 352.68312482, 0.00068955, -35.26831248, -6.896e-05, -105.80493744, -0.00020687, -352.68312482, -0.00068955, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 13.2, 3.075)
    ops.node(122013, 0.0, 13.2, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.09, 28011290.64789016, 11671371.10328757, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 117.02377395, 0.00095986, 140.0489688, 0.01119681, 14.00489688, 0.03714576, -117.02377395, -0.00095986, -140.0489688, -0.01119681, -14.00489688, -0.03714576, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 105.04353835, 0.00095986, 125.7115433, 0.01119681, 12.57115433, 0.03714576, -105.04353835, -0.00095986, -125.7115433, -0.01119681, -12.57115433, -0.03714576, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 112.58657991, 0.01919722, 112.58657991, 0.05759166, 78.81060594, -1493.87207231, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 28.14664498, 9.003e-05, 84.43993494, 0.0002701, 281.46644979, 0.00090033, -28.14664498, -9.003e-05, -84.43993494, -0.0002701, -281.46644979, -0.00090033, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 112.58657991, 0.01919722, 112.58657991, 0.05759166, 78.81060594, -1493.87207231, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 28.14664498, 9.003e-05, 84.43993494, 0.0002701, 281.46644979, 0.00090033, -28.14664498, -9.003e-05, -84.43993494, -0.0002701, -281.46644979, -0.00090033, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 5.05, 13.2, 3.075)
    ops.node(122014, 5.05, 13.2, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.1225, 26384825.93716229, 10993677.47381762, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 161.85091337, 0.00091271, 193.63225212, 0.00894252, 19.36322521, 0.02948802, -161.85091337, -0.00091271, -193.63225212, -0.00894252, -19.36322521, -0.02948802, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 155.20117735, 0.00091271, 185.67676187, 0.00894252, 18.56767619, 0.02948802, -155.20117735, -0.00091271, -185.67676187, -0.00894252, -18.56767619, -0.02948802, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 132.14297733, 0.01825425, 132.14297733, 0.05476276, 92.50008413, -1670.46793419, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 33.03574433, 8.242e-05, 99.107233, 0.00024727, 330.35744333, 0.00082422, -33.03574433, -8.242e-05, -99.107233, -0.00024727, -330.35744333, -0.00082422, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 132.14297733, 0.01825425, 132.14297733, 0.05476276, 92.50008413, -1670.46793419, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 33.03574433, 8.242e-05, 99.107233, 0.00024727, 330.35744333, 0.00082422, -33.03574433, -8.242e-05, -99.107233, -0.00024727, -330.35744333, -0.00082422, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.95, 13.2, 3.075)
    ops.node(122015, 7.95, 13.2, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.1225, 25619034.26883273, 10674597.61201364, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 158.15760443, 0.0009147, 189.00098065, 0.00980703, 18.90009806, 0.0287404, -158.15760443, -0.0009147, -189.00098065, -0.00980703, -18.90009806, -0.0287404, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 151.8302247, 0.0009147, 181.43965612, 0.00980703, 18.14396561, 0.0287404, -151.8302247, -0.0009147, -181.43965612, -0.00980703, -18.14396561, -0.0287404, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 132.70705305, 0.01829397, 132.70705305, 0.0548819, 92.89493714, -1753.60436499, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 33.17676326, 8.525e-05, 99.53028979, 0.00025574, 331.76763263, 0.00085248, -33.17676326, -8.525e-05, -99.53028979, -0.00025574, -331.76763263, -0.00085248, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 132.70705305, 0.01829397, 132.70705305, 0.0548819, 92.89493714, -1753.60436499, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 33.17676326, 8.525e-05, 99.53028979, 0.00025574, 331.76763263, 0.00085248, -33.17676326, -8.525e-05, -99.53028979, -0.00025574, -331.76763263, -0.00085248, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 13.0, 13.2, 3.075)
    ops.node(122016, 13.0, 13.2, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.09, 26354583.35465271, 10981076.39777196, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 109.47843511, 0.00104761, 130.86528904, 0.00912914, 13.0865289, 0.03144881, -109.47843511, -0.00104761, -130.86528904, -0.00912914, -13.0865289, -0.03144881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 99.95862278, 0.00104761, 119.48576036, 0.00912914, 11.94857604, 0.03144881, -99.95862278, -0.00104761, -119.48576036, -0.00912914, -11.94857604, -0.03144881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 94.65474916, 0.02095211, 94.65474916, 0.06285632, 66.25832442, -1341.34359252, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 23.66368729, 8.045e-05, 70.99106187, 0.00024135, 236.63687291, 0.00080452, -23.66368729, -8.045e-05, -70.99106187, -0.00024135, -236.63687291, -0.00080452, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 94.65474916, 0.02095211, 94.65474916, 0.06285632, 66.25832442, -1341.34359252, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 23.66368729, 8.045e-05, 70.99106187, 0.00024135, 236.63687291, 0.00080452, -23.66368729, -8.045e-05, -70.99106187, -0.00024135, -236.63687291, -0.00080452, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.875)
    ops.node(123001, 0.0, 0.0, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 26971058.91961571, 11237941.21650655, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 52.94094184, 0.00118671, 63.4478684, 0.00968942, 6.34478684, 0.04291256, -52.94094184, -0.00118671, -63.4478684, -0.00968942, -6.34478684, -0.04291256, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 49.42127804, 0.00118671, 59.22967435, 0.00968942, 5.92296744, 0.04291256, -49.42127804, -0.00118671, -59.22967435, -0.00968942, -5.92296744, -0.04291256, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 73.37737405, 0.0237341, 73.37737405, 0.07120231, 51.36416183, -1180.30836305, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 18.34434351, 8.776e-05, 55.03303054, 0.00026327, 183.44343512, 0.00087756, -18.34434351, -8.776e-05, -55.03303054, -0.00026327, -183.44343512, -0.00087756, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 73.37737405, 0.0237341, 73.37737405, 0.07120231, 51.36416183, -1180.30836305, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 18.34434351, 8.776e-05, 55.03303054, 0.00026327, 183.44343512, 0.00087756, -18.34434351, -8.776e-05, -55.03303054, -0.00026327, -183.44343512, -0.00087756, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.0, 0.0, 5.875)
    ops.node(123004, 13.0, 0.0, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 27469101.87824628, 11445459.11593595, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 52.57362417, 0.00115894, 63.02157776, 0.01208507, 6.30215778, 0.0467144, -52.57362417, -0.00115894, -63.02157776, -0.01208507, -6.30215778, -0.0467144, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 49.05897936, 0.00115894, 58.80846777, 0.01208507, 5.88084678, 0.0467144, -49.05897936, -0.00115894, -58.80846777, -0.01208507, -5.88084678, -0.0467144, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 88.45340475, 0.02317873, 88.45340475, 0.06953618, 61.91738333, -1375.94625386, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 22.11335119, 0.00010387, 66.34005357, 0.0003116, 221.13351189, 0.00103868, -22.11335119, -0.00010387, -66.34005357, -0.0003116, -221.13351189, -0.00103868, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 88.45340475, 0.02317873, 88.45340475, 0.06953618, 61.91738333, -1375.94625386, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 22.11335119, 0.00010387, 66.34005357, 0.0003116, 221.13351189, 0.00103868, -22.11335119, -0.00010387, -66.34005357, -0.0003116, -221.13351189, -0.00103868, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.4, 5.9)
    ops.node(123005, 0.0, 4.4, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 26253179.92213515, 10938824.96755631, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 122.76200468, 0.00081203, 147.51474768, 0.00942173, 14.75147477, 0.03264483, -122.76200468, -0.00081203, -147.51474768, -0.00942173, -14.75147477, -0.03264483, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 116.63231326, 0.00081203, 140.1491146, 0.00942173, 14.01491146, 0.03264483, -116.63231326, -0.00081203, -140.1491146, -0.00942173, -14.01491146, -0.03264483, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 124.32460989, 0.01624064, 124.32460989, 0.04872192, 87.02722692, -1508.06900678, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 31.08115247, 7.793e-05, 93.24345742, 0.0002338, 310.81152473, 0.00077934, -31.08115247, -7.793e-05, -93.24345742, -0.0002338, -310.81152473, -0.00077934, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 124.32460989, 0.01624064, 124.32460989, 0.04872192, 87.02722692, -1508.06900678, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 31.08115247, 7.793e-05, 93.24345742, 0.0002338, 310.81152473, 0.00077934, -31.08115247, -7.793e-05, -93.24345742, -0.0002338, -310.81152473, -0.00077934, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 5.05, 4.4, 5.9)
    ops.node(123006, 5.05, 4.4, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.16, 28204584.60188689, 11751910.25078621, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 175.70767799, 0.00076478, 211.56982315, 0.00992382, 21.15698232, 0.03147023, -175.70767799, -0.00076478, -211.56982315, -0.00992382, -21.15698232, -0.03147023, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 175.70767799, 0.00076478, 211.56982315, 0.00992382, 21.15698232, 0.03147023, -175.70767799, -0.00076478, -211.56982315, -0.00992382, -21.15698232, -0.03147023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 157.28878583, 0.01529552, 157.28878583, 0.04588657, 110.10215008, -1631.76698725, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 39.32219646, 7.027e-05, 117.96658937, 0.0002108, 393.22196457, 0.00070267, -39.32219646, -7.027e-05, -117.96658937, -0.0002108, -393.22196457, -0.00070267, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 157.28878583, 0.01529552, 157.28878583, 0.04588657, 110.10215008, -1631.76698725, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 39.32219646, 7.027e-05, 117.96658937, 0.0002108, 393.22196457, 0.00070267, -39.32219646, -7.027e-05, -117.96658937, -0.0002108, -393.22196457, -0.00070267, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 7.95, 4.4, 5.9)
    ops.node(123007, 7.95, 4.4, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.16, 27532434.52446334, 11471847.71852639, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 175.82796624, 0.0007751, 211.78732145, 0.00853869, 21.17873215, 0.02925091, -175.82796624, -0.0007751, -211.78732145, -0.00853869, -21.17873215, -0.02925091, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 175.82796624, 0.0007751, 211.78732145, 0.00853869, 21.17873215, 0.02925091, -175.82796624, -0.0007751, -211.78732145, -0.00853869, -21.17873215, -0.02925091, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 149.13795174, 0.01550203, 149.13795174, 0.04650609, 104.39656622, -1518.24916104, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 37.28448794, 6.825e-05, 111.85346381, 0.00020476, 372.84487935, 0.00068252, -37.28448794, -6.825e-05, -111.85346381, -0.00020476, -372.84487935, -0.00068252, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 149.13795174, 0.01550203, 149.13795174, 0.04650609, 104.39656622, -1518.24916104, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 37.28448794, 6.825e-05, 111.85346381, 0.00020476, 372.84487935, 0.00068252, -37.28448794, -6.825e-05, -111.85346381, -0.00020476, -372.84487935, -0.00068252, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 13.0, 4.4, 5.9)
    ops.node(123008, 13.0, 4.4, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 27624398.41257858, 11510166.00524108, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 130.30202497, 0.0008551, 156.63180446, 0.01009823, 15.66318045, 0.03588003, -130.30202497, -0.0008551, -156.63180446, -0.01009823, -15.66318045, -0.03588003, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 123.6284032, 0.0008551, 148.6096619, 0.01009823, 14.86096619, 0.03588003, -123.6284032, -0.0008551, -148.6096619, -0.01009823, -14.86096619, -0.03588003, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 134.47350353, 0.01710201, 134.47350353, 0.05130603, 94.13145247, -1634.63674763, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 33.61837588, 8.011e-05, 100.85512765, 0.00024034, 336.18375882, 0.00080112, -33.61837588, -8.011e-05, -100.85512765, -0.00024034, -336.18375882, -0.00080112, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 134.47350353, 0.01710201, 134.47350353, 0.05130603, 94.13145247, -1634.63674763, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 33.61837588, 8.011e-05, 100.85512765, 0.00024034, 336.18375882, 0.00080112, -33.61837588, -8.011e-05, -100.85512765, -0.00024034, -336.18375882, -0.00080112, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.8, 5.9)
    ops.node(123009, 0.0, 8.8, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 27130705.82017782, 11304460.75840742, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 141.0243399, 0.00087421, 169.52085889, 0.0086559, 16.95208589, 0.02922295, -141.0243399, -0.00087421, -169.52085889, -0.0086559, -16.95208589, -0.02922295, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 141.0243399, 0.00087421, 169.52085889, 0.0086559, 16.95208589, 0.02922295, -141.0243399, -0.00087421, -169.52085889, -0.0086559, -16.95208589, -0.02922295, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 108.43130127, 0.01748427, 108.43130127, 0.0524528, 75.90191089, -1341.50167364, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 27.10782532, 6.577e-05, 81.32347596, 0.00019732, 271.07825318, 0.00065773, -27.10782532, -6.577e-05, -81.32347596, -0.00019732, -271.07825318, -0.00065773, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 108.43130127, 0.01748427, 108.43130127, 0.0524528, 75.90191089, -1341.50167364, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 27.10782532, 6.577e-05, 81.32347596, 0.00019732, 271.07825318, 0.00065773, -27.10782532, -6.577e-05, -81.32347596, -0.00019732, -271.07825318, -0.00065773, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 5.05, 8.8, 5.9)
    ops.node(123010, 5.05, 8.8, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 28993110.08850084, 12080462.53687535, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 152.20771014, 0.00086821, 182.43568038, 0.00824091, 18.24356804, 0.02994591, -152.20771014, -0.00086821, -182.43568038, -0.00824091, -18.24356804, -0.02994591, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 152.20771014, 0.00086821, 182.43568038, 0.00824091, 18.24356804, 0.02994591, -152.20771014, -0.00086821, -182.43568038, -0.00824091, -18.24356804, -0.02994591, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 113.52127464, 0.01736416, 113.52127464, 0.05209248, 79.46489225, -1369.27327675, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 28.38031866, 6.444e-05, 85.14095598, 0.00019331, 283.8031866, 0.00064437, -28.38031866, -6.444e-05, -85.14095598, -0.00019331, -283.8031866, -0.00064437, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 113.52127464, 0.01736416, 113.52127464, 0.05209248, 79.46489225, -1369.27327675, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 28.38031866, 6.444e-05, 85.14095598, 0.00019331, 283.8031866, 0.00064437, -28.38031866, -6.444e-05, -85.14095598, -0.00019331, -283.8031866, -0.00064437, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.95, 8.8, 5.9)
    ops.node(123011, 7.95, 8.8, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 27939068.65764095, 11641278.60735039, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 153.04044027, 0.0008783, 183.49628505, 0.00784375, 18.3496285, 0.02804558, -153.04044027, -0.0008783, -183.49628505, -0.00784375, -18.3496285, -0.02804558, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 153.04044027, 0.0008783, 183.49628505, 0.00784375, 18.3496285, 0.02804558, -153.04044027, -0.0008783, -183.49628505, -0.00784375, -18.3496285, -0.02804558, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 106.11132404, 0.01756606, 106.11132404, 0.05269819, 74.27792683, -1346.39493155, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 26.52783101, 6.25e-05, 79.58349303, 0.00018751, 265.2783101, 0.00062503, -26.52783101, -6.25e-05, -79.58349303, -0.00018751, -265.2783101, -0.00062503, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 106.11132404, 0.01756606, 106.11132404, 0.05269819, 74.27792683, -1346.39493155, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 26.52783101, 6.25e-05, 79.58349303, 0.00018751, 265.2783101, 0.00062503, -26.52783101, -6.25e-05, -79.58349303, -0.00018751, -265.2783101, -0.00062503, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 13.0, 8.8, 5.9)
    ops.node(123012, 13.0, 8.8, 8.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 26018517.25641327, 10841048.85683887, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 140.37994957, 0.00092061, 168.65446091, 0.00855299, 16.86544609, 0.02735259, -140.37994957, -0.00092061, -168.65446091, -0.00855299, -16.86544609, -0.02735259, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 140.37994957, 0.00092061, 168.65446091, 0.00855299, 16.86544609, 0.02735259, -140.37994957, -0.00092061, -168.65446091, -0.00855299, -16.86544609, -0.02735259, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 106.82302388, 0.0184122, 106.82302388, 0.0552366, 74.77611672, -1334.96929046, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 26.70575597, 6.757e-05, 80.11726791, 0.0002027, 267.0575597, 0.00067567, -26.70575597, -6.757e-05, -80.11726791, -0.0002027, -267.0575597, -0.00067567, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 106.82302388, 0.0184122, 106.82302388, 0.0552366, 74.77611672, -1334.96929046, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 26.70575597, 6.757e-05, 80.11726791, 0.0002027, 267.0575597, 0.00067567, -26.70575597, -6.757e-05, -80.11726791, -0.0002027, -267.0575597, -0.00067567, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 13.2, 5.875)
    ops.node(123013, 0.0, 13.2, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 28488648.32723416, 11870270.13634757, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 60.55105773, 0.00115611, 72.58263243, 0.01247519, 7.25826324, 0.04484965, -60.55105773, -0.00115611, -72.58263243, -0.01247519, -7.25826324, -0.04484965, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 60.55105773, 0.00115611, 72.58263243, 0.01247519, 7.25826324, 0.04484965, -60.55105773, -0.00115611, -72.58263243, -0.01247519, -7.25826324, -0.04484965, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 83.94461506, 0.02312212, 83.94461506, 0.06936637, 58.76123054, -1253.2336701, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 20.98615376, 9.505e-05, 62.95846129, 0.00028514, 209.86153764, 0.00095045, -20.98615376, -9.505e-05, -62.95846129, -0.00028514, -209.86153764, -0.00095045, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 83.94461506, 0.02312212, 83.94461506, 0.06936637, 58.76123054, -1253.2336701, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 20.98615376, 9.505e-05, 62.95846129, 0.00028514, 209.86153764, 0.00095045, -20.98615376, -9.505e-05, -62.95846129, -0.00028514, -209.86153764, -0.00095045, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 5.05, 13.2, 5.875)
    ops.node(123014, 5.05, 13.2, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 30761984.08654795, 12817493.36939498, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 65.5027936, 0.00116975, 77.94814453, 0.01003036, 7.79481445, 0.04166279, -65.5027936, -0.00116975, -77.94814453, -0.01003036, -7.79481445, -0.04166279, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 65.5027936, 0.00116975, 77.94814453, 0.01003036, 7.79481445, 0.04166279, -65.5027936, -0.00116975, -77.94814453, -0.01003036, -7.79481445, -0.04166279, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 64.0561006, 0.02339493, 64.0561006, 0.0701848, 44.83927042, -1091.30219483, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 16.01402515, 6.717e-05, 48.04207545, 0.0002015, 160.14025151, 0.00067167, -16.01402515, -6.717e-05, -48.04207545, -0.0002015, -160.14025151, -0.00067167, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 64.0561006, 0.02339493, 64.0561006, 0.0701848, 44.83927042, -1091.30219483, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 16.01402515, 6.717e-05, 48.04207545, 0.0002015, 160.14025151, 0.00067167, -16.01402515, -6.717e-05, -48.04207545, -0.0002015, -160.14025151, -0.00067167, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.95, 13.2, 5.875)
    ops.node(123015, 7.95, 13.2, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 27602684.34676113, 11501118.47781714, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 65.13279375, 0.00122625, 77.49871913, 0.01127018, 7.74987191, 0.03556131, -65.13279375, -0.00122625, -77.49871913, -0.01127018, -7.74987191, -0.03556131, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 65.13279375, 0.00122625, 77.49871913, 0.01127018, 7.74987191, 0.03556131, -65.13279375, -0.00122625, -77.49871913, -0.01127018, -7.74987191, -0.03556131, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 85.29899816, 0.02452501, 85.29899816, 0.07357503, 59.70929871, -1268.39795426, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 21.32474954, 9.968e-05, 63.97424862, 0.00029904, 213.24749541, 0.00099679, -21.32474954, -9.968e-05, -63.97424862, -0.00029904, -213.24749541, -0.00099679, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 85.29899816, 0.02452501, 85.29899816, 0.07357503, 59.70929871, -1268.39795426, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 21.32474954, 9.968e-05, 63.97424862, 0.00029904, 213.24749541, 0.00099679, -21.32474954, -9.968e-05, -63.97424862, -0.00029904, -213.24749541, -0.00099679, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 13.0, 13.2, 5.875)
    ops.node(123016, 13.0, 13.2, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 29706044.79564267, 12377518.66485111, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 56.12439822, 0.0012217, 67.22316242, 0.01100564, 6.72231624, 0.04593651, -56.12439822, -0.0012217, -67.22316242, -0.01100564, -6.72231624, -0.04593651, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 56.12439822, 0.0012217, 67.22316242, 0.01100564, 6.72231624, 0.04593651, -56.12439822, -0.0012217, -67.22316242, -0.01100564, -6.72231624, -0.04593651, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 60.24061139, 0.02443405, 60.24061139, 0.07330215, 42.16842797, -1043.54826104, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 15.06015285, 6.541e-05, 45.18045854, 0.00019623, 150.60152848, 0.00065412, -15.06015285, -6.541e-05, -45.18045854, -0.00019623, -150.60152848, -0.00065412, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 60.24061139, 0.02443405, 60.24061139, 0.07330215, 42.16842797, -1043.54826104, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 15.06015285, 6.541e-05, 45.18045854, 0.00019623, 150.60152848, 0.00065412, -15.06015285, -6.541e-05, -45.18045854, -0.00019623, -150.60152848, -0.00065412, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.675)
    ops.node(124001, 0.0, 0.0, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26935038.34657495, 11222932.64440623, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 40.6916946, 0.00107397, 49.50163847, 0.0145219, 4.95016385, 0.06625691, -40.6916946, -0.00107397, -49.50163847, -0.0145219, -4.95016385, -0.06625691, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 36.95783432, 0.00107397, 44.95937982, 0.0145219, 4.49593798, 0.06625691, -36.95783432, -0.00107397, -44.95937982, -0.0145219, -4.49593798, -0.06625691, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 76.44044866, 0.0214795, 76.44044866, 0.06443849, 53.50831406, -1611.28194953, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 19.11011216, 9.154e-05, 57.33033649, 0.00027462, 191.10112164, 0.00091541, -19.11011216, -9.154e-05, -57.33033649, -0.00027462, -191.10112164, -0.00091541, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 76.44044866, 0.0214795, 76.44044866, 0.06443849, 53.50831406, -1611.28194953, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 19.11011216, 9.154e-05, 57.33033649, 0.00027462, 191.10112164, 0.00091541, -19.11011216, -9.154e-05, -57.33033649, -0.00027462, -191.10112164, -0.00091541, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.0, 0.0, 8.675)
    ops.node(124004, 13.0, 0.0, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 27884144.93644137, 11618393.72351724, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 40.89438071, 0.00105124, 49.68243236, 0.01183457, 4.96824324, 0.06504382, -40.89438071, -0.00105124, -49.68243236, -0.01183457, -4.96824324, -0.06504382, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 37.07434362, 0.00105124, 45.04148338, 0.01183457, 4.50414834, 0.06504382, -37.07434362, -0.00105124, -45.04148338, -0.01183457, -4.50414834, -0.06504382, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 65.04105845, 0.02102483, 65.04105845, 0.06307449, 45.52874091, -1241.22467432, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 16.26026461, 7.524e-05, 48.78079383, 0.00022572, 162.60264611, 0.00075239, -16.26026461, -7.524e-05, -48.78079383, -0.00022572, -162.60264611, -0.00075239, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 65.04105845, 0.02102483, 65.04105845, 0.06307449, 45.52874091, -1241.22467432, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 16.26026461, 7.524e-05, 48.78079383, 0.00022572, 162.60264611, 0.00075239, -16.26026461, -7.524e-05, -48.78079383, -0.00022572, -162.60264611, -0.00075239, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.4, 8.7)
    ops.node(124005, 0.0, 4.4, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 27301843.93728144, 11375768.3072006, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 104.90887408, 0.0008284, 127.56814892, 0.01177591, 12.75681489, 0.04728861, -104.90887408, -0.0008284, -127.56814892, -0.01177591, -12.75681489, -0.04728861, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 94.53034087, 0.0008284, 114.94795563, 0.01177591, 11.49479556, 0.04728861, -94.53034087, -0.0008284, -114.94795563, -0.01177591, -11.49479556, -0.04728861, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 114.55612779, 0.01656795, 114.55612779, 0.04970384, 80.18928945, -1467.18730755, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 28.63903195, 6.905e-05, 85.91709584, 0.00020716, 286.39031947, 0.00069053, -28.63903195, -6.905e-05, -85.91709584, -0.00020716, -286.39031947, -0.00069053, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 114.55612779, 0.01656795, 114.55612779, 0.04970384, 80.18928945, -1467.18730755, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 28.63903195, 6.905e-05, 85.91709584, 0.00020716, 286.39031947, 0.00069053, -28.63903195, -6.905e-05, -85.91709584, -0.00020716, -286.39031947, -0.00069053, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 5.05, 4.4, 8.7)
    ops.node(124006, 5.05, 4.4, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.16, 27340209.43542022, 11391753.93142509, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 135.84861627, 0.00073134, 165.20878783, 0.01045955, 16.52087878, 0.03765248, -135.84861627, -0.00073134, -165.20878783, -0.01045955, -16.52087878, -0.03765248, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 135.84861627, 0.00073134, 165.20878783, 0.01045955, 16.52087878, 0.03765248, -135.84861627, -0.00073134, -165.20878783, -0.01045955, -16.52087878, -0.03765248, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 131.85999773, 0.01462689, 131.85999773, 0.04388066, 92.30199841, -1308.75801466, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 32.96499943, 6.077e-05, 98.89499829, 0.00018231, 329.64999431, 0.00060769, -32.96499943, -6.077e-05, -98.89499829, -0.00018231, -329.64999431, -0.00060769, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 131.85999773, 0.01462689, 131.85999773, 0.04388066, 92.30199841, -1308.75801466, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 32.96499943, 6.077e-05, 98.89499829, 0.00018231, 329.64999431, 0.00060769, -32.96499943, -6.077e-05, -98.89499829, -0.00018231, -329.64999431, -0.00060769, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 7.95, 4.4, 8.7)
    ops.node(124007, 7.95, 4.4, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.16, 28891551.43561214, 12038146.43150506, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 138.07635424, 0.00073507, 167.48465587, 0.00897289, 16.74846559, 0.03727962, -138.07635424, -0.00073507, -167.48465587, -0.00897289, -16.74846559, -0.03727962, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 138.07635424, 0.00073507, 167.48465587, 0.00897289, 16.74846559, 0.03727962, -138.07635424, -0.00073507, -167.48465587, -0.00897289, -16.74846559, -0.03727962, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 129.36702044, 0.01470145, 129.36702044, 0.04410434, 90.55691431, -1170.12815242, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 32.34175511, 5.642e-05, 97.02526533, 0.00016926, 323.4175511, 0.00056419, -32.34175511, -5.642e-05, -97.02526533, -0.00016926, -323.4175511, -0.00056419, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 129.36702044, 0.01470145, 129.36702044, 0.04410434, 90.55691431, -1170.12815242, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 32.34175511, 5.642e-05, 97.02526533, 0.00016926, 323.4175511, 0.00056419, -32.34175511, -5.642e-05, -97.02526533, -0.00016926, -323.4175511, -0.00056419, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 13.0, 4.4, 8.7)
    ops.node(124008, 13.0, 4.4, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 27751050.16911313, 11562937.57046381, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 112.3808751, 0.00081043, 136.5655162, 0.0129113, 13.65655162, 0.04888743, -112.3808751, -0.00081043, -136.5655162, -0.0129113, -13.65655162, -0.04888743, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 99.98469392, 0.00081043, 121.5016463, 0.0129113, 12.15016463, 0.04888743, -99.98469392, -0.00081043, -121.5016463, -0.0129113, -12.15016463, -0.04888743, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 120.93676448, 0.01620862, 120.93676448, 0.04862586, 84.65573514, -1654.08069505, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 30.23419112, 7.172e-05, 90.70257336, 0.00021516, 302.3419112, 0.00071719, -30.23419112, -7.172e-05, -90.70257336, -0.00021516, -302.3419112, -0.00071719, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 120.93676448, 0.01620862, 120.93676448, 0.04862586, 84.65573514, -1654.08069505, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 30.23419112, 7.172e-05, 90.70257336, 0.00021516, 302.3419112, 0.00071719, -30.23419112, -7.172e-05, -90.70257336, -0.00021516, -302.3419112, -0.00071719, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.8, 8.7)
    ops.node(124009, 0.0, 8.8, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 30534227.3739001, 12722594.73912504, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 131.508307, 0.00080904, 158.92461275, 0.01147919, 15.89246127, 0.04314256, -131.508307, -0.00080904, -158.92461275, -0.01147919, -15.89246127, -0.04314256, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 121.58006806, 0.00080904, 146.92657578, 0.01147919, 14.69265758, 0.04314256, -121.58006806, -0.00080904, -146.92657578, -0.01147919, -14.69265758, -0.04314256, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 116.4193003, 0.0161808, 116.4193003, 0.0485424, 81.49351021, -1169.13554697, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 29.10482508, 6.275e-05, 87.31447523, 0.00018824, 291.04825076, 0.00062747, -29.10482508, -6.275e-05, -87.31447523, -0.00018824, -291.04825076, -0.00062747, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 116.4193003, 0.0161808, 116.4193003, 0.0485424, 81.49351021, -1169.13554697, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 29.10482508, 6.275e-05, 87.31447523, 0.00018824, 291.04825076, 0.00062747, -29.10482508, -6.275e-05, -87.31447523, -0.00018824, -291.04825076, -0.00062747, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 5.05, 8.8, 8.7)
    ops.node(124010, 5.05, 8.8, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 27787165.49197738, 11577985.62165724, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 117.09515838, 0.00082521, 141.97182115, 0.01055014, 14.19718212, 0.03840198, -117.09515838, -0.00082521, -141.97182115, -0.01055014, -14.19718212, -0.03840198, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 117.09515838, 0.00082521, 141.97182115, 0.01055014, 14.19718212, 0.03840198, -117.09515838, -0.00082521, -141.97182115, -0.01055014, -14.19718212, -0.03840198, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 106.04442267, 0.01650424, 106.04442267, 0.04951273, 74.23109587, -1151.24318384, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 26.51110567, 6.281e-05, 79.533317, 0.00018842, 265.11105668, 0.00062806, -26.51110567, -6.281e-05, -79.533317, -0.00018842, -265.11105668, -0.00062806, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 106.04442267, 0.01650424, 106.04442267, 0.04951273, 74.23109587, -1151.24318384, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 26.51110567, 6.281e-05, 79.533317, 0.00018842, 265.11105668, 0.00062806, -26.51110567, -6.281e-05, -79.533317, -0.00018842, -265.11105668, -0.00062806, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.95, 8.8, 8.7)
    ops.node(124011, 7.95, 8.8, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 25392268.25933572, 10580111.77472322, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 116.37892342, 0.00084334, 141.36329772, 0.0101185, 14.13632977, 0.03521804, -116.37892342, -0.00084334, -141.36329772, -0.0101185, -14.13632977, -0.03521804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 116.37892342, 0.00084334, 141.36329772, 0.0101185, 14.13632977, 0.03521804, -116.37892342, -0.00084334, -141.36329772, -0.0101185, -14.13632977, -0.03521804, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 94.57018361, 0.01686675, 94.57018361, 0.05060024, 66.19912853, -1130.83208167, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 23.6425459, 6.129e-05, 70.92763771, 0.00018388, 236.42545904, 0.00061292, -23.6425459, -6.129e-05, -70.92763771, -0.00018388, -236.42545904, -0.00061292, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 94.57018361, 0.01686675, 94.57018361, 0.05060024, 66.19912853, -1130.83208167, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 23.6425459, 6.129e-05, 70.92763771, 0.00018388, 236.42545904, 0.00061292, -23.6425459, -6.129e-05, -70.92763771, -0.00018388, -236.42545904, -0.00061292, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 13.0, 8.8, 8.7)
    ops.node(124012, 13.0, 8.8, 10.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 27042734.91592156, 11267806.21496732, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 129.1089543, 0.00080295, 157.04870154, 0.01176087, 15.70487015, 0.04086888, -129.1089543, -0.00080295, -157.04870154, -0.01176087, -15.70487015, -0.04086888, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 119.02760003, 0.00080295, 144.78569774, 0.01176087, 14.47856977, 0.04086888, -119.02760003, -0.00080295, -144.78569774, -0.01176087, -14.47856977, -0.04086888, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 105.23987934, 0.01605898, 105.23987934, 0.04817694, 73.66791554, -1222.56413691, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 26.30996983, 6.404e-05, 78.9299095, 0.00019213, 263.09969834, 0.00064045, -26.30996983, -6.404e-05, -78.9299095, -0.00019213, -263.09969834, -0.00064045, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 105.23987934, 0.01605898, 105.23987934, 0.04817694, 73.66791554, -1222.56413691, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 26.30996983, 6.404e-05, 78.9299095, 0.00019213, 263.09969834, 0.00064045, -26.30996983, -6.404e-05, -78.9299095, -0.00019213, -263.09969834, -0.00064045, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 13.2, 8.675)
    ops.node(124013, 0.0, 13.2, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 29380084.67565384, 12241701.9481891, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 51.87519968, 0.00109194, 62.85161276, 0.01275696, 6.28516128, 0.0606136, -51.87519968, -0.00109194, -62.85161276, -0.01275696, -6.28516128, -0.0606136, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 48.65071203, 0.00109194, 58.94484709, 0.01275696, 5.89448471, 0.0606136, -48.65071203, -0.00109194, -58.94484709, -0.01275696, -5.89448471, -0.0606136, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 44.73012435, 0.02183885, 44.73012435, 0.06551654, 31.31108704, -937.02624379, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 11.18253109, 4.911e-05, 33.54759326, 0.00014733, 111.82531087, 0.00049109, -11.18253109, -4.911e-05, -33.54759326, -0.00014733, -111.82531087, -0.00049109, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 44.73012435, 0.02183885, 44.73012435, 0.06551654, 31.31108704, -937.02624379, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 11.18253109, 4.911e-05, 33.54759326, 0.00014733, 111.82531087, 0.00049109, -11.18253109, -4.911e-05, -33.54759326, -0.00014733, -111.82531087, -0.00049109, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 5.05, 13.2, 8.675)
    ops.node(124014, 5.05, 13.2, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 27212692.94175111, 11338622.05906296, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 48.2276017, 0.00110961, 58.41438898, 0.01303644, 5.8414389, 0.05319743, -48.2276017, -0.00110961, -58.41438898, -0.01303644, -5.8414389, -0.05319743, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 48.2276017, 0.00110961, 58.41438898, 0.01303644, 5.8414389, 0.05319743, -48.2276017, -0.00110961, -58.41438898, -0.01303644, -5.8414389, -0.05319743, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 58.05930697, 0.0221921, 58.05930697, 0.06657631, 40.64151488, -1036.40836675, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 14.51482674, 6.882e-05, 43.54448023, 0.00020646, 145.14826743, 0.00068819, -14.51482674, -6.882e-05, -43.54448023, -0.00020646, -145.14826743, -0.00068819, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 58.05930697, 0.0221921, 58.05930697, 0.06657631, 40.64151488, -1036.40836675, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 14.51482674, 6.882e-05, 43.54448023, 0.00020646, 145.14826743, 0.00068819, -14.51482674, -6.882e-05, -43.54448023, -0.00020646, -145.14826743, -0.00068819, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.95, 13.2, 8.675)
    ops.node(124015, 7.95, 13.2, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 24593834.09550582, 10247430.87312743, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 46.65761021, 0.0011377, 56.54274054, 0.01125544, 5.65427405, 0.04590135, -46.65761021, -0.0011377, -56.54274054, -0.01125544, -5.65427405, -0.04590135, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 46.65761021, 0.0011377, 56.54274054, 0.01125544, 5.65427405, 0.04590135, -46.65761021, -0.0011377, -56.54274054, -0.01125544, -5.65427405, -0.04590135, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 38.73689035, 0.02275404, 38.73689035, 0.06826212, 27.11582324, -928.13852748, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 9.68422259, 5.081e-05, 29.05266776, 0.00015242, 96.84222587, 0.00050805, -9.68422259, -5.081e-05, -29.05266776, -0.00015242, -96.84222587, -0.00050805, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 38.73689035, 0.02275404, 38.73689035, 0.06826212, 27.11582324, -928.13852748, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 9.68422259, 5.081e-05, 29.05266776, 0.00015242, 96.84222587, 0.00050805, -9.68422259, -5.081e-05, -29.05266776, -0.00015242, -96.84222587, -0.00050805, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 13.0, 13.2, 8.675)
    ops.node(124016, 13.0, 13.2, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 26493722.11040679, 11039050.87933616, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 55.55467817, 0.00112974, 67.61650307, 0.01462142, 6.76165031, 0.05882525, -55.55467817, -0.00112974, -67.61650307, -0.01462142, -6.76165031, -0.05882525, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 51.76347467, 0.00112974, 63.00216758, 0.01462142, 6.30021676, 0.05882525, -51.76347467, -0.00112974, -63.00216758, -0.01462142, -6.30021676, -0.05882525, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 60.3495506, 0.02259478, 60.3495506, 0.06778435, 42.24468542, -1209.76481074, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 15.08738765, 7.348e-05, 45.26216295, 0.00022043, 150.87387651, 0.00073475, -15.08738765, -7.348e-05, -45.26216295, -0.00022043, -150.87387651, -0.00073475, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 60.3495506, 0.02259478, 60.3495506, 0.06778435, 42.24468542, -1209.76481074, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 15.08738765, 7.348e-05, 45.26216295, 0.00022043, 150.87387651, 0.00073475, -15.08738765, -7.348e-05, -45.26216295, -0.00022043, -150.87387651, -0.00073475, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 5.05, 0.0, 0.0)
    ops.node(124017, 5.05, 0.0, 1.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 170002, 124017, 0.16, 25230855.28809975, 10512856.37004156, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 221.86797939, 0.00063042, 264.02903225, 0.00812077, 26.40290323, 0.02303058, -221.86797939, -0.00063042, -264.02903225, -0.00812077, -26.40290323, -0.02303058, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 238.34231566, 0.00063042, 283.63394809, 0.00812077, 28.36339481, 0.02303058, -238.34231566, -0.00063042, -283.63394809, -0.00812077, -28.36339481, -0.02303058, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 263.35571064, 0.01260843, 263.35571064, 0.03782528, 184.34899745, -4385.04893454, 0.05, 2, 0, 70002, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 65.83892766, 6.576e-05, 197.51678298, 0.00019728, 658.3892766, 0.00065758, -65.83892766, -6.576e-05, -197.51678298, -0.00019728, -658.3892766, -0.00065758, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 263.35571064, 0.01260843, 263.35571064, 0.03782528, 184.34899745, -4385.04893454, 0.05, 2, 0, 70002, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 65.83892766, 6.576e-05, 197.51678298, 0.00019728, 658.3892766, 0.00065758, -65.83892766, -6.576e-05, -197.51678298, -0.00019728, -658.3892766, -0.00065758, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 5.05, 0.0, 1.6)
    ops.node(121002, 5.05, 0.0, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 174017, 121002, 0.16, 32076504.83906619, 13365210.34961091, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 201.20102376, 0.00064167, 239.79956256, 0.00877975, 23.97995626, 0.03566527, -201.20102376, -0.00064167, -239.79956256, -0.00877975, -23.97995626, -0.03566527, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 189.42310456, 0.00064167, 225.76215947, 0.00877975, 22.57621595, 0.03566527, -189.42310456, -0.00064167, -225.76215947, -0.00877975, -22.57621595, -0.03566527, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 319.67415586, 0.01283332, 319.67415586, 0.03849995, 223.7719091, -4074.9706848, 0.05, 2, 0, 74017, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 79.91853896, 6.279e-05, 239.75561689, 0.00018836, 799.18538964, 0.00062786, -79.91853896, -6.279e-05, -239.75561689, -0.00018836, -799.18538964, -0.00062786, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 319.67415586, 0.01283332, 319.67415586, 0.03849995, 223.7719091, -4074.9706848, 0.05, 2, 0, 74017, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 79.91853896, 6.279e-05, 239.75561689, 0.00018836, 799.18538964, 0.00062786, -79.91853896, -6.279e-05, -239.75561689, -0.00018836, -799.18538964, -0.00062786, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 7.95, 0.0, 0.0)
    ops.node(124018, 7.95, 0.0, 1.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 170003, 124018, 0.16, 30916043.81580766, 12881684.92325319, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 226.71378761, 0.00061543, 270.45497926, 0.00836855, 27.04549793, 0.03301806, -226.71378761, -0.00061543, -270.45497926, -0.00836855, -27.04549793, -0.03301806, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 242.78904247, 0.00061543, 289.63172525, 0.00836855, 28.96317252, 0.03301806, -242.78904247, -0.00061543, -289.63172525, -0.00836855, -28.96317252, -0.03301806, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 310.97411826, 0.0123085, 310.97411826, 0.03692551, 217.68188279, -4104.31862567, 0.05, 2, 0, 70003, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 77.74352957, 6.337e-05, 233.2305887, 0.00019011, 777.43529566, 0.0006337, -77.74352957, -6.337e-05, -233.2305887, -0.00019011, -777.43529566, -0.0006337, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 310.97411826, 0.0123085, 310.97411826, 0.03692551, 217.68188279, -4104.31862567, 0.05, 2, 0, 70003, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 77.74352957, 6.337e-05, 233.2305887, 0.00019011, 777.43529566, 0.0006337, -77.74352957, -6.337e-05, -233.2305887, -0.00019011, -777.43529566, -0.0006337, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 7.95, 0.0, 1.6)
    ops.node(121003, 7.95, 0.0, 2.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4044, 174018, 121003, 0.16, 29033909.31000108, 12097462.21250045, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24044, 203.27734349, 0.00061385, 243.16171392, 0.00937894, 24.31617139, 0.03205481, -203.27734349, -0.00061385, -243.16171392, -0.00937894, -24.31617139, -0.03205481, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14044, 188.94701304, 0.00061385, 226.01967707, 0.00937894, 22.60196771, 0.03205481, -188.94701304, -0.00061385, -226.01967707, -0.00937894, -22.60196771, -0.03205481, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24044, 4044, 0.0, 293.60367933, 0.01227704, 293.60367933, 0.03683112, 205.52257553, -4236.14675405, 0.05, 2, 0, 74018, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44044, 73.40091983, 6.371e-05, 220.2027595, 0.00019113, 734.00919833, 0.00063708, -73.40091983, -6.371e-05, -220.2027595, -0.00019113, -734.00919833, -0.00063708, 0.4, 0.3, 0.003, 0.0, 0.0, 24044, 2)
    ops.limitCurve('ThreePoint', 14044, 4044, 0.0, 293.60367933, 0.01227704, 293.60367933, 0.03683112, 205.52257553, -4236.14675405, 0.05, 2, 0, 74018, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34044, 73.40091983, 6.371e-05, 220.2027595, 0.00019113, 734.00919833, 0.00063708, -73.40091983, -6.371e-05, -220.2027595, -0.00019113, -734.00919833, -0.00063708, 0.4, 0.3, 0.003, 0.0, 0.0, 14044, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4044, 99999, 'P', 44044, 'Vy', 34044, 'Vz', 24044, 'My', 14044, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4044, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4044, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 5.05, 0.0, 3.075)
    ops.node(124019, 5.05, 0.0, 4.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 171002, 124019, 0.16, 28033352.68480995, 11680563.61867081, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 180.87854301, 0.00060051, 217.44415644, 0.00983742, 21.74441564, 0.03414973, -180.87854301, -0.00060051, -217.44415644, -0.00983742, -21.74441564, -0.03414973, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 166.84941137, 0.00060051, 200.57895704, 0.00983742, 20.0578957, 0.03414973, -166.84941137, -0.00060051, -200.57895704, -0.00983742, -20.0578957, -0.03414973, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 267.79610189, 0.01201026, 267.79610189, 0.03603079, 187.45727132, -3862.15604615, 0.05, 2, 0, 71002, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 66.94902547, 6.018e-05, 200.84707642, 0.00018055, 669.49025472, 0.00060182, -66.94902547, -6.018e-05, -200.84707642, -0.00018055, -669.49025472, -0.00060182, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 267.79610189, 0.01201026, 267.79610189, 0.03603079, 187.45727132, -3862.15604615, 0.05, 2, 0, 71002, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 66.94902547, 6.018e-05, 200.84707642, 0.00018055, 669.49025472, 0.00060182, -66.94902547, -6.018e-05, -200.84707642, -0.00018055, -669.49025472, -0.00060182, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 5.05, 0.0, 4.4)
    ops.node(122002, 5.05, 0.0, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 122002, 0.16, 28825276.99785455, 12010532.0824394, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 177.9581939, 0.00060219, 214.10155271, 0.00893793, 21.41015527, 0.03540124, -177.9581939, -0.00060219, -214.10155271, -0.00893793, -21.41015527, -0.03540124, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 163.68518918, 0.00060219, 196.92969676, 0.00893793, 19.69296968, 0.03540124, -163.68518918, -0.00060219, -196.92969676, -0.00893793, -19.69296968, -0.03540124, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 265.2201262, 0.01204378, 265.2201262, 0.03613135, 185.65408834, -3524.6627342, 0.05, 2, 0, 74019, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 66.30503155, 5.797e-05, 198.91509465, 0.0001739, 663.05031549, 0.00057966, -66.30503155, -5.797e-05, -198.91509465, -0.0001739, -663.05031549, -0.00057966, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 265.2201262, 0.01204378, 265.2201262, 0.03613135, 185.65408834, -3524.6627342, 0.05, 2, 0, 74019, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 66.30503155, 5.797e-05, 198.91509465, 0.0001739, 663.05031549, 0.00057966, -66.30503155, -5.797e-05, -198.91509465, -0.0001739, -663.05031549, -0.00057966, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.95, 0.0, 3.075)
    ops.node(124020, 7.95, 0.0, 4.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 171003, 124020, 0.16, 26061990.11829871, 10859162.54929113, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 184.83279998, 0.00059707, 222.11937217, 0.00943428, 22.21193722, 0.03043161, -184.83279998, -0.00059707, -222.11937217, -0.00943428, -22.21193722, -0.03043161, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 169.15282752, 0.00059707, 203.27625752, 0.00943428, 20.32762575, 0.03043161, -169.15282752, -0.00059707, -203.27625752, -0.00943428, -20.32762575, -0.03043161, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 251.80423329, 0.01194148, 251.80423329, 0.03582444, 176.2629633, -3942.32802081, 0.05, 2, 0, 71003, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 62.95105832, 6.087e-05, 188.85317497, 0.00018261, 629.51058322, 0.00060869, -62.95105832, -6.087e-05, -188.85317497, -0.00018261, -629.51058322, -0.00060869, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 251.80423329, 0.01194148, 251.80423329, 0.03582444, 176.2629633, -3942.32802081, 0.05, 2, 0, 71003, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 62.95105832, 6.087e-05, 188.85317497, 0.00018261, 629.51058322, 0.00060869, -62.95105832, -6.087e-05, -188.85317497, -0.00018261, -629.51058322, -0.00060869, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 7.95, 0.0, 4.4)
    ops.node(122003, 7.95, 0.0, 5.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 122003, 0.16, 26715323.71560545, 11131384.88150227, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 185.7315982, 0.00059824, 223.6463884, 0.00962506, 22.36463884, 0.03288114, -185.7315982, -0.00059824, -223.6463884, -0.00962506, -22.36463884, -0.03288114, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 168.8732234, 0.00059824, 203.34658656, 0.00962506, 20.33465866, 0.03288114, -168.8732234, -0.00059824, -203.34658656, -0.00962506, -20.33465866, -0.03288114, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 251.51445097, 0.01196477, 251.51445097, 0.03589431, 176.06011568, -3782.78119559, 0.05, 2, 0, 74020, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 62.87861274, 5.931e-05, 188.63583822, 0.00017794, 628.78612741, 0.00059312, -62.87861274, -5.931e-05, -188.63583822, -0.00017794, -628.78612741, -0.00059312, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 251.51445097, 0.01196477, 251.51445097, 0.03589431, 176.06011568, -3782.78119559, 0.05, 2, 0, 74020, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 62.87861274, 5.931e-05, 188.63583822, 0.00017794, 628.78612741, 0.00059312, -62.87861274, -5.931e-05, -188.63583822, -0.00017794, -628.78612741, -0.00059312, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 5.05, 0.0, 5.875)
    ops.node(124021, 5.05, 0.0, 6.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 172002, 124021, 0.1225, 27702802.19409181, 11542834.24753826, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 117.56894888, 0.00063413, 141.73114123, 0.00929879, 14.17311412, 0.03753893, -117.56894888, -0.00063413, -141.73114123, -0.00929879, -14.17311412, -0.03753893, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 111.81650916, 0.00063413, 134.79648838, 0.00929879, 13.47964884, 0.03753893, -111.81650916, -0.00063413, -134.79648838, -0.00929879, -13.47964884, -0.03753893, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 177.3006146, 0.01268269, 177.3006146, 0.03804807, 124.11043022, -2885.08024032, 0.05, 2, 0, 72002, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 44.32515365, 5.266e-05, 132.97546095, 0.00015799, 443.2515365, 0.00052664, -44.32515365, -5.266e-05, -132.97546095, -0.00015799, -443.2515365, -0.00052664, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 177.3006146, 0.01268269, 177.3006146, 0.03804807, 124.11043022, -2885.08024032, 0.05, 2, 0, 72002, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 44.32515365, 5.266e-05, 132.97546095, 0.00015799, 443.2515365, 0.00052664, -44.32515365, -5.266e-05, -132.97546095, -0.00015799, -443.2515365, -0.00052664, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 5.05, 0.0, 7.2)
    ops.node(123002, 5.05, 0.0, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 123002, 0.1225, 27000677.76734246, 11250282.40305936, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 113.38122168, 0.0006063, 137.0257659, 0.01066754, 13.70257659, 0.03962251, -113.38122168, -0.0006063, -137.0257659, -0.01066754, -13.70257659, -0.03962251, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 107.02763027, 0.0006063, 129.34719517, 0.01066754, 12.93471952, 0.03962251, -107.02763027, -0.0006063, -129.34719517, -0.01066754, -12.93471952, -0.03962251, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 169.99504, 0.01212602, 169.99504, 0.03637805, 118.996528, -2896.5763018, 0.05, 2, 0, 74021, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 42.49876, 5.181e-05, 127.49628, 0.00015542, 424.9876, 0.00051807, -42.49876, -5.181e-05, -127.49628, -0.00015542, -424.9876, -0.00051807, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 169.99504, 0.01212602, 169.99504, 0.03637805, 118.996528, -2896.5763018, 0.05, 2, 0, 74021, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 42.49876, 5.181e-05, 127.49628, 0.00015542, 424.9876, 0.00051807, -42.49876, -5.181e-05, -127.49628, -0.00015542, -424.9876, -0.00051807, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.95, 0.0, 5.875)
    ops.node(124022, 7.95, 0.0, 6.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 172003, 124022, 0.1225, 24943545.87512372, 10393144.11463489, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 120.41669189, 0.00063364, 145.0688127, 0.01059485, 14.50688127, 0.03375137, -120.41669189, -0.00063364, -145.0688127, -0.01059485, -14.50688127, -0.03375137, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 113.90960302, 0.00063364, 137.22957014, 0.01059485, 13.72295701, 0.03375137, -113.90960302, -0.00063364, -137.22957014, -0.01059485, -13.72295701, -0.03375137, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 168.6328042, 0.01267288, 168.6328042, 0.03801865, 118.04296294, -3282.66882163, 0.05, 2, 0, 72003, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 42.15820105, 5.563e-05, 126.47460315, 0.00016689, 421.58201049, 0.0005563, -42.15820105, -5.563e-05, -126.47460315, -0.00016689, -421.58201049, -0.0005563, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 168.6328042, 0.01267288, 168.6328042, 0.03801865, 118.04296294, -3282.66882163, 0.05, 2, 0, 72003, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 42.15820105, 5.563e-05, 126.47460315, 0.00016689, 421.58201049, 0.0005563, -42.15820105, -5.563e-05, -126.47460315, -0.00016689, -421.58201049, -0.0005563, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 7.95, 0.0, 7.2)
    ops.node(123003, 7.95, 0.0, 8.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 123003, 0.1225, 31353794.47060417, 13064081.02941841, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 107.91333868, 0.00063718, 129.61871947, 0.00974999, 12.96187195, 0.04428399, -107.91333868, -0.00063718, -129.61871947, -0.00974999, -12.96187195, -0.04428399, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 103.26603133, 0.00063718, 124.036666, 0.00974999, 12.4036666, 0.04428399, -103.26603133, -0.00063718, -124.036666, -0.00974999, -12.4036666, -0.04428399, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 194.23243092, 0.01274365, 194.23243092, 0.03823094, 135.96270164, -2787.24156407, 0.05, 2, 0, 74022, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 48.55810773, 5.097e-05, 145.67432319, 0.00015292, 485.58107729, 0.00050975, -48.55810773, -5.097e-05, -145.67432319, -0.00015292, -485.58107729, -0.00050975, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 194.23243092, 0.01274365, 194.23243092, 0.03823094, 135.96270164, -2787.24156407, 0.05, 2, 0, 74022, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 48.55810773, 5.097e-05, 145.67432319, 0.00015292, 485.58107729, 0.00050975, -48.55810773, -5.097e-05, -145.67432319, -0.00015292, -485.58107729, -0.00050975, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 5.05, 0.0, 8.675)
    ops.node(124023, 5.05, 0.0, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 173002, 124023, 0.1225, 27359386.6769002, 11399744.44870842, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 84.89201095, 0.00061, 103.36703558, 0.01209218, 10.33670356, 0.04921101, -84.89201095, -0.00061, -103.36703558, -0.01209218, -10.33670356, -0.04921101, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 80.23469655, 0.00061, 97.69615115, 0.01209218, 9.76961511, 0.04921101, -80.23469655, -0.00061, -97.69615115, -0.01209218, -9.76961511, -0.04921101, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 153.81174018, 0.01219991, 153.81174018, 0.03659974, 107.66821812, -3049.22208582, 0.05, 2, 0, 73002, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 38.45293504, 4.626e-05, 115.35880513, 0.00013878, 384.52935044, 0.0004626, -38.45293504, -4.626e-05, -115.35880513, -0.00013878, -384.52935044, -0.0004626, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 153.81174018, 0.01219991, 153.81174018, 0.03659974, 107.66821812, -3049.22208582, 0.05, 2, 0, 73002, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 38.45293504, 4.626e-05, 115.35880513, 0.00013878, 384.52935044, 0.0004626, -38.45293504, -4.626e-05, -115.35880513, -0.00013878, -384.52935044, -0.0004626, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 5.05, 0.0, 10.0)
    ops.node(124002, 5.05, 0.0, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 124002, 0.1225, 27619262.23555664, 11508025.93148193, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 82.23765296, 0.00061174, 100.30330987, 0.01265491, 10.03033099, 0.05241241, -82.23765296, -0.00061174, -100.30330987, -0.01265491, -10.03033099, -0.05241241, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 77.2821476, 0.00061174, 94.25919782, 0.01265491, 9.42591978, 0.05241241, -77.2821476, -0.00061174, -94.25919782, -0.01265491, -9.42591978, -0.05241241, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 150.43682956, 0.01223473, 150.43682956, 0.03670419, 105.30578069, -3591.3245885, 0.05, 2, 0, 74023, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 37.60920739, 4.482e-05, 112.82762217, 0.00013446, 376.09207389, 0.00044819, -37.60920739, -4.482e-05, -112.82762217, -0.00013446, -376.09207389, -0.00044819, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 150.43682956, 0.01223473, 150.43682956, 0.03670419, 105.30578069, -3591.3245885, 0.05, 2, 0, 74023, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 37.60920739, 4.482e-05, 112.82762217, 0.00013446, 376.09207389, 0.00044819, -37.60920739, -4.482e-05, -112.82762217, -0.00013446, -376.09207389, -0.00044819, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.95, 0.0, 8.675)
    ops.node(124024, 7.95, 0.0, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 173003, 124024, 0.1225, 26854748.06555718, 11189478.36064883, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 89.20061914, 0.00059945, 108.69402723, 0.01086885, 10.86940272, 0.04751389, -89.20061914, -0.00059945, -108.69402723, -0.01086885, -10.86940272, -0.04751389, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 83.7142642, 0.00059945, 102.00871475, 0.01086885, 10.20087147, 0.04751389, -83.7142642, -0.00059945, -102.00871475, -0.01086885, -10.20087147, -0.04751389, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 147.37578157, 0.01198905, 147.37578157, 0.03596716, 103.1630471, -2747.89275555, 0.05, 2, 0, 73003, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 36.84394539, 4.516e-05, 110.53183618, 0.00013547, 368.43945393, 0.00045157, -36.84394539, -4.516e-05, -110.53183618, -0.00013547, -368.43945393, -0.00045157, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 147.37578157, 0.01198905, 147.37578157, 0.03596716, 103.1630471, -2747.89275555, 0.05, 2, 0, 73003, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 36.84394539, 4.516e-05, 110.53183618, 0.00013547, 368.43945393, 0.00045157, -36.84394539, -4.516e-05, -110.53183618, -0.00013547, -368.43945393, -0.00045157, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 7.95, 0.0, 10.0)
    ops.node(124003, 7.95, 0.0, 11.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 124003, 0.1225, 26556215.30374904, 11065089.70989543, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 82.29185587, 0.00058563, 100.55526282, 0.01403576, 10.05552628, 0.05306657, -82.29185587, -0.00058563, -100.55526282, -0.01403576, -10.05552628, -0.05306657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 76.8605126, 0.00058563, 93.91851678, 0.01403576, 9.39185168, 0.05306657, -76.8605126, -0.00058563, -93.91851678, -0.01403576, -9.39185168, -0.05306657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 149.45189017, 0.01171258, 149.45189017, 0.03513775, 104.61632312, -4148.96591075, 0.05, 2, 0, 74024, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 37.36297254, 4.631e-05, 112.08891763, 0.00013893, 373.62972544, 0.00046308, -37.36297254, -4.631e-05, -112.08891763, -0.00013893, -373.62972544, -0.00046308, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 149.45189017, 0.01171258, 149.45189017, 0.03513775, 104.61632312, -4148.96591075, 0.05, 2, 0, 74024, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 37.36297254, 4.631e-05, 112.08891763, 0.00013893, 373.62972544, 0.00046308, -37.36297254, -4.631e-05, -112.08891763, -0.00013893, -373.62972544, -0.00046308, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4059, '-orient', 0, 0, 1, 0, 1, 0)
