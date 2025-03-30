import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 26119670.70288791, 10883196.1262033, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 47.89408477, 0.00085311, 56.00625761, 0.0077892, 5.60062576, 0.02288797, -47.89408477, -0.00085311, -56.00625761, -0.0077892, -5.60062576, -0.02288797, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 46.31248022, 0.00085311, 54.15676508, 0.0077892, 5.41567651, 0.02288797, -46.31248022, -0.00085311, -54.15676508, -0.0077892, -5.41567651, -0.02288797, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 97.04169672, 0.01706213, 97.04169672, 0.05118638, 67.9291877, -1217.2576825, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 24.26042418, 0.00015622, 72.78127254, 0.00046866, 242.6042418, 0.0015622, -24.26042418, -0.00015622, -72.78127254, -0.00046866, -242.6042418, -0.0015622, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 97.04169672, 0.01706213, 97.04169672, 0.05118638, 67.9291877, -1217.2576825, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 24.26042418, 0.00015622, 72.78127254, 0.00046866, 242.6042418, 0.0015622, -24.26042418, -0.00015622, -72.78127254, -0.00046866, -242.6042418, -0.0015622, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 5.8, 0.0, 0.0)
    ops.node(121002, 5.8, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.14, 29572314.77056647, 12321797.82106936, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 178.46642336, 0.00103288, 212.29360135, 0.00865102, 21.22936013, 0.03140719, -178.46642336, -0.00103288, -212.29360135, -0.00865102, -21.22936013, -0.03140719, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 182.18607303, 0.00092995, 216.718287, 0.00886388, 21.6718287, 0.03392162, -182.18607303, -0.00092995, -216.718287, -0.00886388, -21.6718287, -0.03392162, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 178.72701167, 0.02065753, 178.72701167, 0.06197259, 125.10890817, -1706.4516118, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 44.68175292, 0.00011345, 134.04525875, 0.00034035, 446.81752918, 0.00113449, -44.68175292, -0.00011345, -134.04525875, -0.00034035, -446.81752918, -0.00113449, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 185.85654043, 0.01859902, 185.85654043, 0.05579706, 130.0995783, -1829.60480929, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 46.46413511, 0.00011797, 139.39240532, 0.00035392, 464.64135107, 0.00117975, -46.46413511, -0.00011797, -139.39240532, -0.00035392, -464.64135107, -0.00117975, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 11.6, 0.0, 0.0)
    ops.node(121003, 11.6, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.14, 29066308.54822284, 12110961.89509285, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 180.05349366, 0.00104289, 214.17606315, 0.00867817, 21.41760631, 0.03047909, -180.05349366, -0.00104289, -214.17606315, -0.00867817, -21.41760631, -0.03047909, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 183.28811457, 0.00093928, 218.02368842, 0.00889107, 21.80236884, 0.03289695, -183.28811457, -0.00093928, -218.02368842, -0.00889107, -21.80236884, -0.03289695, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 180.72240538, 0.0208577, 180.72240538, 0.06257311, 126.50568376, -1782.05495405, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 45.18060134, 0.00011671, 135.54180403, 0.00035014, 451.80601345, 0.00116713, -45.18060134, -0.00011671, -135.54180403, -0.00035014, -451.80601345, -0.00116713, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 188.48137876, 0.01878565, 188.48137876, 0.05635696, 131.93696513, -1919.17273364, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 47.12034469, 0.00012172, 141.36103407, 0.00036517, 471.2034469, 0.00121724, -47.12034469, -0.00012172, -141.36103407, -0.00036517, -471.2034469, -0.00121724, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 26.0, 0.0, 0.0)
    ops.node(121006, 26.0, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.14, 28999916.03559846, 12083298.34816602, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 180.18205377, 0.0010646, 214.32562879, 0.00841676, 21.43256288, 0.0300901, -180.18205377, -0.0010646, -214.32562879, -0.00841676, -21.43256288, -0.0300901, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 183.946411, 0.00095679, 218.80331239, 0.00861372, 21.88033124, 0.03247911, -183.946411, -0.00095679, -218.80331239, -0.00861372, -21.88033124, -0.03247911, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 177.44753187, 0.02129201, 177.44753187, 0.06387603, 124.21327231, -1731.08956948, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 44.36188297, 0.00011486, 133.08564891, 0.00034458, 443.61882968, 0.0011486, -44.36188297, -0.00011486, -133.08564891, -0.00034458, -443.61882968, -0.0011486, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 184.78369109, 0.01913588, 184.78369109, 0.05740765, 129.34858376, -1858.77167171, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 46.19592277, 0.00011961, 138.58776832, 0.00035883, 461.95922773, 0.00119609, -46.19592277, -0.00011961, -138.58776832, -0.00035883, -461.95922773, -0.00119609, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 31.8, 0.0, 0.0)
    ops.node(121007, 31.8, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.14, 28588677.97429515, 11911949.15595631, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 174.08449999, 0.00106744, 207.03884082, 0.00982806, 20.70388408, 0.03069978, -174.08449999, -0.00106744, -207.03884082, -0.00982806, -20.70388408, -0.03069978, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 179.57263544, 0.00095519, 213.56588488, 0.01007897, 21.35658849, 0.03306166, -179.57263544, -0.00095519, -213.56588488, -0.01007897, -21.35658849, -0.03306166, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 183.19783425, 0.0213487, 183.19783425, 0.06404611, 128.23848397, -1865.16341411, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 45.79945856, 0.00012029, 137.39837569, 0.00036087, 457.99458562, 0.00120288, -45.79945856, -0.00012029, -137.39837569, -0.00036087, -457.99458562, -0.00120288, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 191.63351881, 0.01910381, 191.63351881, 0.05731144, 134.14346317, -2017.85396466, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 47.9083797, 0.00012583, 143.72513911, 0.00037748, 479.08379703, 0.00125827, -47.9083797, -0.00012583, -143.72513911, -0.00037748, -479.08379703, -0.00125827, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 37.6, 0.0, 0.0)
    ops.node(121008, 37.6, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.0625, 27933934.44590719, 11639139.35246133, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 55.28216745, 0.00110284, 65.02351215, 0.00750173, 6.50235121, 0.02785617, -55.28216745, -0.00110284, -65.02351215, -0.00750173, -6.50235121, -0.02785617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 53.36912751, 0.00110284, 62.77337288, 0.00750173, 6.27733729, 0.02785617, -53.36912751, -0.00110284, -62.77337288, -0.00750173, -6.27733729, -0.02785617, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 86.31735955, 0.02205688, 86.31735955, 0.06617064, 60.42215168, -1086.64599814, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 21.57933989, 0.00012993, 64.73801966, 0.00038979, 215.79339887, 0.00129931, -21.57933989, -0.00012993, -64.73801966, -0.00038979, -215.79339887, -0.00129931, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 86.31735955, 0.02205688, 86.31735955, 0.06617064, 60.42215168, -1086.64599814, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 21.57933989, 0.00012993, 64.73801966, 0.00038979, 215.79339887, 0.00129931, -21.57933989, -0.00012993, -64.73801966, -0.00038979, -215.79339887, -0.00129931, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 4.75, 0.0)
    ops.node(121009, 0.0, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.14, 29891199.07830913, 12454666.28262881, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 190.92036418, 0.00093346, 227.39503166, 0.01027177, 22.73950317, 0.03374009, -190.92036418, -0.00093346, -227.39503166, -0.01027177, -22.73950317, -0.03374009, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 177.9160781, 0.00104012, 211.90632223, 0.01002689, 21.19063222, 0.03145343, -177.9160781, -0.00104012, -211.90632223, -0.01002689, -21.19063222, -0.03145343, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 182.65255267, 0.01866916, 182.65255267, 0.05600749, 127.85678687, -1744.16744343, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 45.66313817, 0.0001147, 136.9894145, 0.00034411, 456.63138168, 0.00114704, -45.66313817, -0.0001147, -136.9894145, -0.00034411, -456.63138168, -0.00114704, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 175.79734435, 0.02080246, 175.79734435, 0.06240738, 123.05814104, -1625.15447383, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 43.94933609, 0.0001104, 131.84800826, 0.0003312, 439.49336087, 0.00110399, -43.94933609, -0.0001104, -131.84800826, -0.0003312, -439.49336087, -0.00110399, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 5.8, 4.75, 0.0)
    ops.node(121010, 5.8, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.3, 28440848.95627252, 11850353.73178022, 0.01240246, 0.006875, 0.0099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 612.49228922, 0.00070579, 736.56957314, 0.01013046, 73.65695731, 0.02873739, -612.49228922, -0.00070579, -736.56957314, -0.01013046, -73.65695731, -0.02873739, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 675.41366543, 0.00078553, 812.23741751, 0.00984224, 81.22374175, 0.02677191, -675.41366543, -0.00078553, -812.23741751, -0.00984224, -81.22374175, -0.02677191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 299.2902562, 0.01411586, 299.2902562, 0.04234759, 209.50317934, -2174.01310206, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 74.82256405, 9.218e-05, 224.46769215, 0.00027655, 748.22564051, 0.00092184, -74.82256405, -9.218e-05, -224.46769215, -0.00027655, -748.22564051, -0.00092184, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 277.04438404, 0.01571063, 277.04438404, 0.04713189, 193.93106883, -1998.34642932, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 69.26109601, 8.533e-05, 207.78328803, 0.000256, 692.6109601, 0.00085332, -69.26109601, -8.533e-05, -207.78328803, -0.000256, -692.6109601, -0.00085332, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 11.6, 4.75, 0.0)
    ops.node(121011, 11.6, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.3, 28275730.93428167, 11781554.55595069, 0.01240246, 0.006875, 0.0099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 591.33276863, 0.00073092, 711.19734957, 0.00919816, 71.11973496, 0.02762682, -591.33276863, -0.00073092, -711.19734957, -0.00919816, -71.11973496, -0.02762682, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 627.35413926, 0.00081837, 754.52033907, 0.00895503, 75.45203391, 0.02572249, -627.35413926, -0.00081837, -754.52033907, -0.00895503, -75.45203391, -0.02572249, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 292.9769578, 0.01461848, 292.9769578, 0.04385545, 205.08387046, -2095.15005017, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 73.24423945, 9.077e-05, 219.73271835, 0.0002723, 732.4423945, 0.00090766, -73.24423945, -9.077e-05, -219.73271835, -0.0002723, -732.4423945, -0.00090766, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 271.59349247, 0.01636734, 271.59349247, 0.04910201, 190.11544473, -1935.26215772, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 67.89837312, 8.414e-05, 203.69511935, 0.00025242, 678.98373118, 0.00084141, -67.89837312, -8.414e-05, -203.69511935, -0.00025242, -678.98373118, -0.00084141, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 17.4, 4.75, 0.0)
    ops.node(121012, 17.4, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.2, 29899976.45938116, 12458323.52474215, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 388.32023551, 0.0008447, 464.78204462, 0.00854959, 46.47820446, 0.02924117, -388.32023551, -0.0008447, -464.78204462, -0.00854959, -46.47820446, -0.02924117, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 369.61759725, 0.00100115, 442.39678202, 0.00830412, 44.2396782, 0.02652642, -369.61759725, -0.00100115, -442.39678202, -0.00830412, -44.2396782, -0.02652642, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 212.72676273, 0.01689405, 212.72676273, 0.05068214, 148.90873391, -1652.74170305, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 53.18169068, 9.349e-05, 159.54507204, 0.00028046, 531.81690681, 0.00093486, -53.18169068, -9.349e-05, -159.54507204, -0.00028046, -531.81690681, -0.00093486, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 203.20032703, 0.02002293, 203.20032703, 0.0600688, 142.24022892, -1511.79975597, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 50.80008176, 8.93e-05, 152.40024528, 0.0002679, 508.00081759, 0.00089299, -50.80008176, -8.93e-05, -152.40024528, -0.0002679, -508.00081759, -0.00089299, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 20.2, 4.75, 0.0)
    ops.node(121013, 20.2, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.2, 29480732.14386581, 12283638.39327742, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 397.76103699, 0.00084106, 476.26168774, 0.00791577, 47.62616877, 0.02810291, -397.76103699, -0.00084106, -476.26168774, -0.00791577, -47.62616877, -0.02810291, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 384.82074654, 0.00098966, 460.76754931, 0.00769533, 46.07675493, 0.02547338, -384.82074654, -0.00098966, -460.76754931, -0.00769533, -46.07675493, -0.02547338, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 208.79806026, 0.01682127, 208.79806026, 0.05046382, 146.15864218, -1633.27636557, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 52.19951507, 9.306e-05, 156.5985452, 0.00027919, 521.99515066, 0.00093064, -52.19951507, -9.306e-05, -156.5985452, -0.00027919, -521.99515066, -0.00093064, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 193.34927637, 0.01979325, 193.34927637, 0.05937974, 135.34449346, -1496.89904876, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 48.33731909, 8.618e-05, 145.01195727, 0.00025854, 483.37319092, 0.00086179, -48.33731909, -8.618e-05, -145.01195727, -0.00025854, -483.37319092, -0.00086179, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 26.0, 4.75, 0.0)
    ops.node(121014, 26.0, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.3, 27468781.31711004, 11445325.54879585, 0.01240246, 0.006875, 0.0099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 589.64534821, 0.00072665, 709.38098352, 0.00792514, 70.93809835, 0.02544191, -589.64534821, -0.00072665, -709.38098352, -0.00792514, -70.93809835, -0.02544191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 630.0147024, 0.00081199, 757.94789288, 0.00772945, 75.79478929, 0.02366721, -630.0147024, -0.00081199, -757.94789288, -0.00772945, -75.79478929, -0.02366721, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 278.82954898, 0.01453293, 278.82954898, 0.04359879, 195.18068428, -1991.66214772, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 69.70738724, 8.892e-05, 209.12216173, 0.00026676, 697.07387244, 0.00088921, -69.70738724, -8.892e-05, -209.12216173, -0.00026676, -697.07387244, -0.00088921, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 258.88381623, 0.01623977, 258.88381623, 0.04871931, 181.21867136, -1852.23864707, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 64.72095406, 8.256e-05, 194.16286217, 0.00024768, 647.20954056, 0.0008256, -64.72095406, -8.256e-05, -194.16286217, -0.00024768, -647.20954056, -0.0008256, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 31.8, 4.75, 0.0)
    ops.node(121015, 31.8, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.3, 29411701.51323947, 12254875.63051645, 0.01240246, 0.006875, 0.0099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 619.1884455, 0.00072491, 743.96469859, 0.00952905, 74.39646986, 0.02912913, -619.1884455, -0.00072491, -743.96469859, -0.00952905, -74.39646986, -0.02912913, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 671.98714445, 0.00081145, 807.40316945, 0.00927186, 80.74031695, 0.02710515, -671.98714445, -0.00081145, -807.40316945, -0.00927186, -80.74031695, -0.02710515, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 302.55237986, 0.0144982, 302.55237986, 0.04349459, 211.7866659, -2067.64803143, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 75.63809497, 9.011e-05, 226.9142849, 0.00027034, 756.38094966, 0.00090112, -75.63809497, -9.011e-05, -226.9142849, -0.00027034, -756.38094966, -0.00090112, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 280.88937122, 0.01622897, 280.88937122, 0.04868691, 196.62255986, -1913.22597726, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 70.22234281, 8.366e-05, 210.66702842, 0.00025098, 702.22342806, 0.0008366, -70.22234281, -8.366e-05, -210.66702842, -0.00025098, -702.22342806, -0.0008366, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 37.6, 4.75, 0.0)
    ops.node(121016, 37.6, 4.75, 3.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.14, 27811112.37580542, 11587963.48991892, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 189.52087421, 0.00094287, 225.63549613, 0.00853283, 22.56354961, 0.02815198, -189.52087421, -0.00094287, -225.63549613, -0.00853283, -22.56354961, -0.02815198, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 176.86399677, 0.00105102, 210.5667559, 0.00835526, 21.05667559, 0.02626751, -176.86399677, -0.00105102, -210.5667559, -0.00835526, -21.05667559, -0.02626751, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 165.43791286, 0.01885733, 165.43791286, 0.05657199, 115.806539, -1614.77487943, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 41.35947821, 0.00011166, 124.07843464, 0.00033499, 413.59478214, 0.00111664, -41.35947821, -0.00011166, -124.07843464, -0.00033499, -413.59478214, -0.00111664, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 159.51580523, 0.0210204, 159.51580523, 0.0630612, 111.66106366, -1515.669999, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 39.87895131, 0.00010767, 119.63685393, 0.000323, 398.78951308, 0.00107667, -39.87895131, -0.00010767, -119.63685393, -0.000323, -398.78951308, -0.00107667, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 9.5, 0.0)
    ops.node(121017, 0.0, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.0625, 30777085.77421134, 12823785.73925472, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 73.67465729, 0.00153484, 86.92200994, 0.01096036, 8.69220099, 0.03923617, -73.67465729, -0.00153484, -86.92200994, -0.01096036, -8.69220099, -0.03923617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 69.7154597, 0.00153484, 82.25091373, 0.01096036, 8.22509137, 0.03923617, -69.7154597, -0.00153484, -82.25091373, -0.01096036, -8.22509137, -0.03923617, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 108.530487, 0.03069675, 108.530487, 0.09209026, 75.9713409, -1236.45256434, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 27.13262175, 0.00014828, 81.39786525, 0.00044483, 271.3262175, 0.00148276, -27.13262175, -0.00014828, -81.39786525, -0.00044483, -271.3262175, -0.00148276, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 108.530487, 0.03069675, 108.530487, 0.09209026, 75.9713409, -1236.45256434, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 27.13262175, 0.00014828, 81.39786525, 0.00044483, 271.3262175, 0.00148276, -27.13262175, -0.00014828, -81.39786525, -0.00044483, -271.3262175, -0.00148276, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 5.8, 9.5, 0.0)
    ops.node(121018, 5.8, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.14, 31267157.87698254, 13027982.44874272, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 179.41588263, 0.00101778, 213.20076938, 0.010044, 21.32007694, 0.03577277, -179.41588263, -0.00101778, -213.20076938, -0.010044, -21.32007694, -0.03577277, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 183.26577272, 0.00091739, 217.77561258, 0.01031778, 21.77756126, 0.03864875, -183.26577272, -0.00091739, -217.77561258, -0.01031778, -21.77756126, -0.03864875, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 195.12838784, 0.02035554, 195.12838784, 0.06106663, 136.58987149, -1848.71952753, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 48.78209696, 0.00011715, 146.34629088, 0.00035144, 487.8209696, 0.00117147, -48.78209696, -0.00011715, -146.34629088, -0.00035144, -487.8209696, -0.00117147, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 203.43139339, 0.01834775, 203.43139339, 0.05504325, 142.40197537, -1998.3111159, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 50.85784835, 0.00012213, 152.57354504, 0.00036639, 508.57848348, 0.00122131, -50.85784835, -0.00012213, -152.57354504, -0.00036639, -508.57848348, -0.00122131, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 11.6, 9.5, 0.0)
    ops.node(121019, 11.6, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.14, 29326258.13271105, 12219274.22196294, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 179.51061733, 0.00105821, 213.53747056, 0.00942891, 21.35374706, 0.03172438, -179.51061733, -0.00105821, -213.53747056, -0.00942891, -21.35374706, -0.03172438, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 183.48199101, 0.00095104, 218.26163174, 0.00966872, 21.82616317, 0.03421916, -183.48199101, -0.00095104, -218.26163174, -0.00966872, -21.82616317, -0.03421916, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 182.14670057, 0.0211643, 182.14670057, 0.06349289, 127.5026904, -1785.3129452, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 45.53667514, 0.00011659, 136.61002543, 0.00034977, 455.36675142, 0.0011659, -45.53667514, -0.00011659, -136.61002543, -0.00034977, -455.36675142, -0.0011659, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 189.93249568, 0.01902077, 189.93249568, 0.0570623, 132.95274698, -1923.03692315, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 47.48312392, 0.00012157, 142.44937176, 0.00036472, 474.83123921, 0.00121574, -47.48312392, -0.00012157, -142.44937176, -0.00036472, -474.83123921, -0.00121574, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 17.4, 9.5, 0.0)
    ops.node(121020, 17.4, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.09, 31207483.07457853, 13003117.94774106, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 105.37722891, 0.00120756, 124.85619638, 0.00893965, 12.48561964, 0.03793561, -105.37722891, -0.00120756, -124.85619638, -0.00893965, -12.48561964, -0.03793561, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 116.69571726, 0.00120756, 138.26690587, 0.00893965, 13.82669059, 0.03793561, -116.69571726, -0.00120756, -138.26690587, -0.00893965, -13.82669059, -0.03793561, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 134.23433871, 0.0241511, 134.23433871, 0.07245331, 93.96403709, -1350.84324498, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 33.55858468, 0.0001256, 100.67575403, 0.0003768, 335.58584677, 0.00125599, -33.55858468, -0.0001256, -100.67575403, -0.0003768, -335.58584677, -0.00125599, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 134.23433871, 0.0241511, 134.23433871, 0.07245331, 93.96403709, -1350.84324498, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 33.55858468, 0.0001256, 100.67575403, 0.0003768, 335.58584677, 0.00125599, -33.55858468, -0.0001256, -100.67575403, -0.0003768, -335.58584677, -0.00125599, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 20.2, 9.5, 0.0)
    ops.node(121021, 20.2, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.09, 26974783.30074484, 11239493.04197701, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 104.87141001, 0.00124328, 123.89413905, 0.00793255, 12.3894139, 0.02671712, -104.87141001, -0.00124328, -123.89413905, -0.00793255, -12.3894139, -0.02671712, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 117.08620541, 0.00124328, 138.32458829, 0.00793255, 13.83245883, 0.02671712, -117.08620541, -0.00124328, -138.32458829, -0.00793255, -13.83245883, -0.02671712, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 122.73512559, 0.02486565, 122.73512559, 0.07459696, 85.91458791, -1382.18455624, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 30.6837814, 0.00013286, 92.05134419, 0.00039858, 306.83781398, 0.0013286, -30.6837814, -0.00013286, -92.05134419, -0.00039858, -306.83781398, -0.0013286, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 122.73512559, 0.02486565, 122.73512559, 0.07459696, 85.91458791, -1382.18455624, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 30.6837814, 0.00013286, 92.05134419, 0.00039858, 306.83781398, 0.0013286, -30.6837814, -0.00013286, -92.05134419, -0.00039858, -306.83781398, -0.0013286, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 26.0, 9.5, 0.0)
    ops.node(121022, 26.0, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.14, 29374857.33694636, 12239523.89039432, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 180.14119357, 0.00102992, 214.28788025, 0.00959579, 21.42878803, 0.03198283, -180.14119357, -0.00102992, -214.28788025, -0.00959579, -21.42878803, -0.03198283, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 183.1464582, 0.00092873, 217.86280819, 0.00984968, 21.78628082, 0.03450095, -183.1464582, -0.00092873, -217.86280819, -0.00984968, -21.78628082, -0.03450095, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 188.57310819, 0.02059845, 188.57310819, 0.06179535, 132.00117573, -1894.47729315, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 47.14327705, 0.0001205, 141.42983114, 0.00036151, 471.43277047, 0.00120504, -47.14327705, -0.0001205, -141.42983114, -0.00036151, -471.43277047, -0.00120504, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 197.24387197, 0.01857459, 197.24387197, 0.05572378, 138.07071038, -2052.71327996, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 49.31096799, 0.00012604, 147.93290398, 0.00037813, 493.10967992, 0.00126045, -49.31096799, -0.00012604, -147.93290398, -0.00037813, -493.10967992, -0.00126045, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 31.8, 9.5, 0.0)
    ops.node(121023, 31.8, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.14, 26806364.07744209, 11169318.36560087, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 183.90759148, 0.00110813, 218.2523317, 0.00745422, 21.82523317, 0.02464523, -183.90759148, -0.00110813, -218.2523317, -0.00745422, -21.82523317, -0.02464523, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 186.44471454, 0.00099557, 221.26326246, 0.00760472, 22.12632625, 0.02653443, -186.44471454, -0.00099557, -221.26326246, -0.00760472, -22.12632625, -0.02653443, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 165.85943022, 0.02216268, 165.85943022, 0.06648803, 116.10160115, -1708.58690221, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 41.46485756, 0.00011614, 124.39457267, 0.00034843, 414.64857555, 0.00116145, -41.46485756, -0.00011614, -124.39457267, -0.00034843, -414.64857555, -0.00116145, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 173.00692574, 0.01991147, 173.00692574, 0.0597344, 121.10484802, -1832.13174759, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 43.25173144, 0.00012115, 129.75519431, 0.00036345, 432.51731436, 0.0012115, -43.25173144, -0.00012115, -129.75519431, -0.00036345, -432.51731436, -0.0012115, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 37.6, 9.5, 0.0)
    ops.node(121024, 37.6, 9.5, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.0625, 29034381.50609666, 12097658.96087361, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 76.23279706, 0.0015783, 89.84116302, 0.00854897, 8.9841163, 0.03205304, -76.23279706, -0.0015783, -89.84116302, -0.00854897, -8.9841163, -0.03205304, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 71.65535651, 0.0015783, 84.44660059, 0.00854897, 8.44466006, 0.03205304, -71.65535651, -0.0015783, -84.44660059, -0.00854897, -8.44466006, -0.03205304, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 94.77574756, 0.03156597, 94.77574756, 0.0946979, 66.34302329, -1103.99150994, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 23.69393689, 0.00013726, 71.08181067, 0.00041177, 236.93936889, 0.00137256, -23.69393689, -0.00013726, -71.08181067, -0.00041177, -236.93936889, -0.00137256, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 94.77574756, 0.03156597, 94.77574756, 0.0946979, 66.34302329, -1103.99150994, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 23.69393689, 0.00013726, 71.08181067, 0.00041177, 236.93936889, 0.00137256, -23.69393689, -0.00013726, -71.08181067, -0.00041177, -236.93936889, -0.00137256, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.95)
    ops.node(122001, 0.0, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 27146703.3221064, 11311126.384211, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 62.3925461, 0.00125066, 74.11153042, 0.01036913, 7.41115304, 0.0361488, -62.3925461, -0.00125066, -74.11153042, -0.01036913, -7.41115304, -0.0361488, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 58.5490666, 0.00125066, 69.54614295, 0.01036913, 6.9546143, 0.0361488, -58.5490666, -0.00125066, -69.54614295, -0.01036913, -6.9546143, -0.0361488, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 93.24791503, 0.0250133, 93.24791503, 0.07503989, 65.27354052, -1447.46336247, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 23.31197876, 0.0001108, 69.93593627, 0.00033239, 233.11978758, 0.00110798, -23.31197876, -0.0001108, -69.93593627, -0.00033239, -233.11978758, -0.00110798, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 93.24791503, 0.0250133, 93.24791503, 0.07503989, 65.27354052, -1447.46336247, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 23.31197876, 0.0001108, 69.93593627, 0.00033239, 233.11978758, 0.00110798, -23.31197876, -0.0001108, -69.93593627, -0.00033239, -233.11978758, -0.00110798, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 5.8, 0.0, 3.95)
    ops.node(122002, 5.8, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.14, 27411289.06153249, 11421370.4423052, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 135.10275979, 0.00086628, 161.83778925, 0.00859063, 16.18377892, 0.03227374, -135.10275979, -0.00086628, -161.83778925, -0.00859063, -16.18377892, -0.03227374, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 178.84423567, 0.00079116, 214.23511826, 0.0088357, 21.42351183, 0.03491413, -178.84423567, -0.00079116, -214.23511826, -0.0088357, -21.42351183, -0.03491413, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 156.74925823, 0.01732559, 156.74925823, 0.05197678, 109.72448076, -1939.78316673, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 39.18731456, 8.235e-05, 117.56194368, 0.00024704, 391.87314559, 0.00082345, -39.18731456, -8.235e-05, -117.56194368, -0.00024704, -391.87314559, -0.00082345, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 163.88109169, 0.01582314, 163.88109169, 0.04746943, 114.71676419, -2115.62231676, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 40.97027292, 8.609e-05, 122.91081877, 0.00025828, 409.70272923, 0.00086092, -40.97027292, -8.609e-05, -122.91081877, -0.00025828, -409.70272923, -0.00086092, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 11.6, 0.0, 3.95)
    ops.node(122003, 11.6, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.14, 29786223.56417813, 12410926.48507422, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 136.23347975, 0.00086263, 163.07625725, 0.00957824, 16.30762572, 0.037525, -136.23347975, -0.00086263, -163.07625725, -0.00957824, -16.30762572, -0.037525, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 179.44583722, 0.00078743, 214.80296594, 0.00986433, 21.48029659, 0.04063763, -179.44583722, -0.00078743, -214.80296594, -0.00986433, -21.48029659, -0.04063763, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 171.02093473, 0.01725252, 171.02093473, 0.05175756, 119.71465431, -2027.89762506, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 42.75523368, 8.268e-05, 128.26570105, 0.00024804, 427.55233682, 0.00082679, -42.75523368, -8.268e-05, -128.26570105, -0.00024804, -427.55233682, -0.00082679, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 178.66883767, 0.01574851, 178.66883767, 0.04724553, 125.06818637, -2220.90000265, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 44.66720942, 8.638e-05, 134.00162825, 0.00025913, 446.67209417, 0.00086377, -44.66720942, -8.638e-05, -134.00162825, -0.00025913, -446.67209417, -0.00086377, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 26.0, 0.0, 3.95)
    ops.node(122006, 26.0, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.14, 28056698.06312323, 11690290.85963468, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 136.65234843, 0.00086869, 163.7153019, 0.01011379, 16.37153019, 0.03503794, -136.65234843, -0.00086869, -163.7153019, -0.01011379, -16.37153019, -0.03503794, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 181.13605821, 0.0007938, 217.00867051, 0.01042214, 21.70086705, 0.03786713, -181.13605821, -0.0007938, -217.00867051, -0.01042214, -21.70086705, -0.03786713, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 168.14927181, 0.01737378, 168.14927181, 0.05212135, 117.70449027, -2151.26290222, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 42.03731795, 8.63e-05, 126.11195386, 0.00025891, 420.37317953, 0.00086302, -42.03731795, -8.63e-05, -126.11195386, -0.00025891, -420.37317953, -0.00086302, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 176.50121635, 0.01587606, 176.50121635, 0.04762817, 123.55085145, -2368.64618614, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 44.12530409, 9.059e-05, 132.37591226, 0.00027177, 441.25304088, 0.00090589, -44.12530409, -9.059e-05, -132.37591226, -0.00027177, -441.25304088, -0.00090589, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 31.8, 0.0, 3.95)
    ops.node(122007, 31.8, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.14, 27242382.07450357, 11350992.53104316, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 137.59798561, 0.00086865, 164.81400504, 0.00877258, 16.4814005, 0.03212073, -137.59798561, -0.00086865, -164.81400504, -0.00877258, -16.4814005, -0.03212073, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 183.46151749, 0.00079512, 219.74905618, 0.00902668, 21.97490562, 0.03473628, -183.46151749, -0.00079512, -219.74905618, -0.00902668, -21.97490562, -0.03473628, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 160.97360378, 0.017373, 160.97360378, 0.052119, 112.68152265, -2061.4668723, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 40.24340095, 8.509e-05, 120.73020284, 0.00025527, 402.43400945, 0.00085089, -40.24340095, -8.509e-05, -120.73020284, -0.00025527, -402.43400945, -0.00085089, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 168.81515781, 0.0159023, 168.81515781, 0.0477069, 118.17061047, -2261.0642034, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 42.20378945, 8.923e-05, 126.61136836, 0.0002677, 422.03789453, 0.00089234, -42.20378945, -8.923e-05, -126.61136836, -0.0002677, -422.03789453, -0.00089234, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 37.6, 0.0, 3.95)
    ops.node(122008, 37.6, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.0625, 28024539.16208893, 11676891.31753705, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 62.59419232, 0.00124752, 74.43252003, 0.00990787, 7.443252, 0.03828644, -62.59419232, -0.00124752, -74.43252003, -0.00990787, -7.443252, -0.03828644, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 58.78980242, 0.00124752, 69.90861267, 0.00990787, 6.99086127, 0.03828644, -58.78980242, -0.00124752, -69.90861267, -0.00990787, -6.99086127, -0.03828644, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 91.65324941, 0.02495046, 91.65324941, 0.07485137, 64.15727458, -1357.17696308, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 22.91331235, 0.00010549, 68.73993706, 0.00031648, 229.13312352, 0.00105492, -22.91331235, -0.00010549, -68.73993706, -0.00031648, -229.13312352, -0.00105492, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 91.65324941, 0.02495046, 91.65324941, 0.07485137, 64.15727458, -1357.17696308, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 22.91331235, 0.00010549, 68.73993706, 0.00031648, 229.13312352, 0.00105492, -22.91331235, -0.00010549, -68.73993706, -0.00031648, -229.13312352, -0.00105492, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 4.75, 3.975)
    ops.node(122009, 0.0, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.14, 28680077.64586187, 11950032.35244245, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 167.19900874, 0.00077662, 200.49748358, 0.00903859, 20.04974836, 0.03501817, -167.19900874, -0.00077662, -200.49748358, -0.00903859, -20.04974836, -0.03501817, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 138.38791522, 0.00084933, 165.94852426, 0.00880028, 16.59485243, 0.0325196, -138.38791522, -0.00084933, -165.94852426, -0.00880028, -16.59485243, -0.0325196, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 153.41939463, 0.0155323, 153.41939463, 0.04659691, 107.39357624, -1731.11995275, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 38.35484866, 7.703e-05, 115.06454598, 0.00023109, 383.54848659, 0.0007703, -38.35484866, -7.703e-05, -115.06454598, -0.00023109, -383.54848659, -0.0007703, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 148.06780114, 0.01698658, 148.06780114, 0.05095973, 103.6474608, -1608.09798694, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 37.01695029, 7.434e-05, 111.05085086, 0.00022303, 370.16950285, 0.00074343, -37.01695029, -7.434e-05, -111.05085086, -0.00022303, -370.16950285, -0.00074343, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 5.8, 4.75, 3.975)
    ops.node(122010, 5.8, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.3, 29209679.05183822, 12170699.60493259, 0.01240246, 0.006875, 0.0099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 476.55885453, 0.00060216, 574.87273394, 0.00892068, 57.48727339, 0.03061766, -476.55885453, -0.00060216, -574.87273394, -0.00892068, -57.48727339, -0.03061766, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 340.84203728, 0.00065154, 411.15759775, 0.00864529, 41.11575977, 0.02838646, -340.84203728, -0.00065154, -411.15759775, -0.00864529, -41.11575977, -0.02838646, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 349.81563288, 0.01204317, 349.81563288, 0.03612952, 244.87094301, -2311.16698373, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 87.45390822, 8.048e-05, 262.36172466, 0.00024144, 874.53908219, 0.00080479, -87.45390822, -8.048e-05, -262.36172466, -0.00024144, -874.53908219, -0.00080479, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 291.5130274, 0.01303083, 291.5130274, 0.03909248, 204.05911918, -2102.08789256, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 72.87825685, 6.707e-05, 218.63477055, 0.0002012, 728.78256849, 0.00067066, -72.87825685, -6.707e-05, -218.63477055, -0.0002012, -728.78256849, -0.00067066, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 11.6, 4.75, 3.975)
    ops.node(122011, 11.6, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.3, 27916710.31017665, 11631962.62924027, 0.01240246, 0.006875, 0.0099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 434.60992964, 0.00061765, 525.0849132, 0.00791038, 52.50849132, 0.02844638, -434.60992964, -0.00061765, -525.0849132, -0.00791038, -52.50849132, -0.02844638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 324.16726509, 0.00067006, 391.65083134, 0.00767806, 39.16508313, 0.02636291, -324.16726509, -0.00067006, -391.65083134, -0.00767806, -39.16508313, -0.02636291, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 330.65884388, 0.01235302, 330.65884388, 0.03705907, 231.46119072, -2241.71092111, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 82.66471097, 7.959e-05, 247.99413291, 0.00023878, 826.6471097, 0.00079595, -82.66471097, -7.959e-05, -247.99413291, -0.00023878, -826.6471097, -0.00079595, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 275.54903657, 0.01340115, 275.54903657, 0.04020344, 192.8843256, -2046.83480013, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 68.88725914, 6.633e-05, 206.66177742, 0.00019899, 688.87259142, 0.00066329, -68.88725914, -6.633e-05, -206.66177742, -0.00019899, -688.87259142, -0.00066329, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 17.4, 4.75, 3.975)
    ops.node(122012, 17.4, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.2, 29991765.57221067, 12496568.98842111, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 283.52980796, 0.00067389, 340.80452338, 0.00910769, 34.08045234, 0.03278579, -283.52980796, -0.00067389, -340.80452338, -0.00910769, -34.08045234, -0.03278579, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 210.24374723, 0.00076756, 252.71424047, 0.00876142, 25.27142405, 0.02961384, -210.24374723, -0.00076756, -252.71424047, -0.00876142, -25.27142405, -0.02961384, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 226.56869336, 0.01347781, 226.56869336, 0.04043344, 158.59808535, -1962.1725486, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 56.64217334, 7.615e-05, 169.92652002, 0.00022844, 566.42173341, 0.00076148, -56.64217334, -7.615e-05, -169.92652002, -0.00022844, -566.42173341, -0.00076148, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 194.58213661, 0.01535115, 194.58213661, 0.04605344, 136.20749563, -1738.93626658, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 48.64553415, 6.54e-05, 145.93660246, 0.00019619, 486.45534152, 0.00065398, -48.64553415, -6.54e-05, -145.93660246, -0.00019619, -486.45534152, -0.00065398, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 20.2, 4.75, 3.975)
    ops.node(122013, 20.2, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.2, 29277024.7654951, 12198760.31895629, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 282.55827712, 0.00066446, 339.97216745, 0.00855656, 33.99721674, 0.03149843, -282.55827712, -0.00066446, -339.97216745, -0.00855656, -33.99721674, -0.03149843, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 209.42495534, 0.00075408, 251.9786598, 0.00823451, 25.19786598, 0.02843855, -209.42495534, -0.00075408, -251.9786598, -0.00823451, -25.19786598, -0.02843855, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 218.02254595, 0.01328915, 218.02254595, 0.03986746, 152.61578217, -1882.81118248, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 54.50563649, 7.506e-05, 163.51690946, 0.00022519, 545.05636488, 0.00075065, -54.50563649, -7.506e-05, -163.51690946, -0.00022519, -545.05636488, -0.00075065, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 186.02664502, 0.01508159, 186.02664502, 0.04524478, 130.21865151, -1679.07511065, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 46.50666125, 6.405e-05, 139.51998376, 0.00019215, 465.06661255, 0.00064048, -46.50666125, -6.405e-05, -139.51998376, -0.00019215, -465.06661255, -0.00064048, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 26.0, 4.75, 3.975)
    ops.node(122014, 26.0, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.3, 29374815.93712174, 12239506.64046739, 0.01240246, 0.006875, 0.0099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 444.90736333, 0.00061855, 536.55772717, 0.00760989, 53.65577272, 0.02944366, -444.90736333, -0.00061855, -536.55772717, -0.00760989, -53.65577272, -0.02944366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 331.50344474, 0.00066995, 399.7927423, 0.00738834, 39.97927423, 0.02725397, -331.50344474, -0.00066995, -399.7927423, -0.00738834, -39.97927423, -0.02725397, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 347.28269424, 0.01237091, 347.28269424, 0.03711274, 243.09788597, -2205.99900596, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 86.82067356, 7.945e-05, 260.46202068, 0.00023834, 868.20673561, 0.00079447, -86.82067356, -7.945e-05, -260.46202068, -0.00023834, -868.20673561, -0.00079447, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 289.4022452, 0.013399, 289.4022452, 0.04019701, 202.58157164, -2018.38321751, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 72.3505613, 6.621e-05, 217.0516839, 0.00019862, 723.50561301, 0.00066206, -72.3505613, -6.621e-05, -217.0516839, -0.00019862, -723.50561301, -0.00066206, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 31.8, 4.75, 3.975)
    ops.node(122015, 31.8, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.3, 28849840.55794065, 12020766.89914194, 0.01240246, 0.006875, 0.0099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 488.27953291, 0.00063173, 589.30847509, 0.00997587, 58.93084751, 0.03136605, -488.27953291, -0.00063173, -589.30847509, -0.00997587, -58.93084751, -0.03136605, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 349.82888406, 0.00068848, 422.21127922, 0.0096678, 42.22112792, 0.02912983, -349.82888406, -0.00068848, -422.21127922, -0.0096678, -42.22112792, -0.02912983, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 352.91209563, 0.01263469, 352.91209563, 0.03790407, 247.03846694, -2490.02734149, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 88.22802391, 8.22e-05, 264.68407172, 0.00024661, 882.28023907, 0.00082204, -88.22802391, -8.22e-05, -264.68407172, -0.00024661, -882.28023907, -0.00082204, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 294.09341302, 0.01376959, 294.09341302, 0.04130876, 205.86538912, -2243.9022254, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 73.52335326, 6.85e-05, 220.57005977, 0.00020551, 735.23353256, 0.00068503, -73.52335326, -6.85e-05, -220.57005977, -0.00020551, -735.23353256, -0.00068503, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 37.6, 4.75, 3.975)
    ops.node(122016, 37.6, 4.75, 6.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.14, 30830255.90546865, 12845939.96061194, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 165.43733015, 0.000779, 197.94599933, 0.01025083, 19.79459993, 0.03952449, -165.43733015, -0.000779, -197.94599933, -0.01025083, -19.79459993, -0.03952449, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 137.28674052, 0.00085453, 164.26377906, 0.0099698, 16.42637791, 0.0366966, -137.28674052, -0.00085453, -164.26377906, -0.0099698, -16.42637791, -0.0366966, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 170.86816506, 0.01557991, 170.86816506, 0.04673972, 119.60771554, -1916.06745773, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 42.71704126, 7.981e-05, 128.15112379, 0.00023942, 427.17041265, 0.00079808, -42.71704126, -7.981e-05, -128.15112379, -0.00023942, -427.17041265, -0.00079808, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 164.55414346, 0.01709062, 164.55414346, 0.05127185, 115.18790042, -1763.70626076, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 41.13853586, 7.686e-05, 123.41560759, 0.00023058, 411.38535865, 0.00076859, -41.13853586, -7.686e-05, -123.41560759, -0.00023058, -411.38535865, -0.00076859, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 9.5, 3.95)
    ops.node(122017, 0.0, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.0625, 29709425.23400282, 12378927.18083451, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 63.24546228, 0.00115956, 75.24845029, 0.01057692, 7.52484503, 0.04360668, -63.24546228, -0.00115956, -75.24845029, -0.01057692, -7.52484503, -0.04360668, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 59.0661404, 0.00115956, 70.27595925, 0.01057692, 7.02759593, 0.04360668, -59.0661404, -0.00115956, -70.27595925, -0.01057692, -7.02759593, -0.04360668, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 95.98855021, 0.02319118, 95.98855021, 0.06957355, 67.19198515, -1377.47056947, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 23.99713755, 0.00010422, 71.99141266, 0.00031265, 239.97137554, 0.00104216, -23.99713755, -0.00010422, -71.99141266, -0.00031265, -239.97137554, -0.00104216, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 95.98855021, 0.02319118, 95.98855021, 0.06957355, 67.19198515, -1377.47056947, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 23.99713755, 0.00010422, 71.99141266, 0.00031265, 239.97137554, 0.00104216, -23.99713755, -0.00010422, -71.99141266, -0.00031265, -239.97137554, -0.00104216, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 5.8, 9.5, 3.95)
    ops.node(122018, 5.8, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.14, 27667178.2657157, 11527990.94404821, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 133.67367443, 0.00087614, 160.13912976, 0.0084741, 16.01391298, 0.03265664, -133.67367443, -0.00087614, -160.13912976, -0.0084741, -16.01391298, -0.03265664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 175.56692516, 0.00079742, 210.32663857, 0.00871034, 21.03266386, 0.03533872, -175.56692516, -0.00079742, -210.32663857, -0.00871034, -21.03266386, -0.03533872, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 155.89808245, 0.01752271, 155.89808245, 0.05256813, 109.12865771, -1892.28299059, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 38.97452061, 8.114e-05, 116.92356184, 0.00024342, 389.74520612, 0.00081141, -38.97452061, -8.114e-05, -116.92356184, -0.00024342, -389.74520612, -0.00081141, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 162.74684864, 0.01594839, 162.74684864, 0.04784517, 113.92279405, -2058.96243686, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 40.68671216, 8.471e-05, 122.06013648, 0.00025412, 406.8671216, 0.00084705, -40.68671216, -8.471e-05, -122.06013648, -0.00025412, -406.8671216, -0.00084705, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 11.6, 9.5, 3.95)
    ops.node(122019, 11.6, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.14, 30293828.9700036, 12622428.7375015, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 134.35797822, 0.00084393, 160.74321392, 0.01078181, 16.07432139, 0.03953394, -134.35797822, -0.00084393, -160.74321392, -0.01078181, -16.07432139, -0.03953394, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 176.48909185, 0.00077088, 211.14804064, 0.01112072, 21.11480406, 0.04278084, -176.48909185, -0.00077088, -211.14804064, -0.01112072, -21.11480406, -0.04278084, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 180.00210882, 0.0168786, 180.00210882, 0.0506358, 126.00147617, -2195.30789817, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 45.0005272, 8.556e-05, 135.00158161, 0.00025669, 450.00527205, 0.00085563, -45.0005272, -8.556e-05, -135.00158161, -0.00025669, -450.00527205, -0.00085563, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 188.6005048, 0.01541758, 188.6005048, 0.04625274, 132.02035336, -2421.48925199, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 47.1501262, 8.965e-05, 141.4503786, 0.00026895, 471.50126199, 0.0008965, -47.1501262, -8.965e-05, -141.4503786, -0.00026895, -471.50126199, -0.0008965, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 17.4, 9.5, 3.95)
    ops.node(122020, 17.4, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.09, 32711214.44554438, 13629672.68564349, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 88.99774238, 0.0009608, 105.82924696, 0.01012995, 10.5829247, 0.04775228, -88.99774238, -0.0009608, -105.82924696, -0.01012995, -10.5829247, -0.04775228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 99.18500232, 0.0009608, 117.94315029, 0.01012995, 11.79431503, 0.04775228, -99.18500232, -0.0009608, -117.94315029, -0.01012995, -11.79431503, -0.04775228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 130.66789006, 0.01921607, 130.66789006, 0.05764822, 91.46752304, -1581.4303903, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 32.66697252, 8.948e-05, 98.00091755, 0.00026844, 326.66972515, 0.00089479, -32.66697252, -8.948e-05, -98.00091755, -0.00026844, -326.66972515, -0.00089479, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 130.66789006, 0.01921607, 130.66789006, 0.05764822, 91.46752304, -1581.4303903, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 32.66697252, 8.948e-05, 98.00091755, 0.00026844, 326.66972515, 0.00089479, -32.66697252, -8.948e-05, -98.00091755, -0.00026844, -326.66972515, -0.00089479, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 20.2, 9.5, 3.95)
    ops.node(122021, 20.2, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.09, 29351725.96147385, 12229885.81728077, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 88.80327134, 0.00095638, 106.06364439, 0.01064241, 10.60636444, 0.04179745, -88.80327134, -0.00095638, -106.06364439, -0.01064241, -10.60636444, -0.04179745, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 100.01017191, 0.00095638, 119.44878999, 0.01064241, 11.944879, 0.04179745, -100.01017191, -0.00095638, -119.44878999, -0.01064241, -11.944879, -0.04179745, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 123.92226356, 0.01912764, 123.92226356, 0.05738292, 86.74558449, -1671.25500615, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 30.98056589, 9.457e-05, 92.94169767, 0.00028372, 309.80565891, 0.00094572, -30.98056589, -9.457e-05, -92.94169767, -0.00028372, -309.80565891, -0.00094572, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 123.92226356, 0.01912764, 123.92226356, 0.05738292, 86.74558449, -1671.25500615, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 30.98056589, 9.457e-05, 92.94169767, 0.00028372, 309.80565891, 0.00094572, -30.98056589, -9.457e-05, -92.94169767, -0.00028372, -309.80565891, -0.00094572, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 26.0, 9.5, 3.95)
    ops.node(122022, 26.0, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.14, 31588365.65630184, 13161819.0234591, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 133.00310008, 0.00080559, 158.81085768, 0.00977939, 15.88108577, 0.04042675, -133.00310008, -0.00080559, -158.81085768, -0.00977939, -15.88108577, -0.04042675, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 174.9369742, 0.00073885, 208.88152905, 0.01008465, 20.8881529, 0.04383169, -174.9369742, -0.00073885, -208.88152905, -0.01008465, -20.8881529, -0.04383169, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 180.34294597, 0.01611172, 180.34294597, 0.04833515, 126.24006218, -2052.09272406, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 45.08573649, 8.221e-05, 135.25720948, 0.00024664, 450.85736493, 0.00082212, -45.08573649, -8.221e-05, -135.25720948, -0.00024664, -450.85736493, -0.00082212, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 188.13058299, 0.01477705, 188.13058299, 0.04433114, 131.69140809, -2249.84539128, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 47.03264575, 8.576e-05, 141.09793724, 0.00025729, 470.32645748, 0.00085762, -47.03264575, -8.576e-05, -141.09793724, -0.00025729, -470.32645748, -0.00085762, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 31.8, 9.5, 3.95)
    ops.node(122023, 31.8, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.14, 28641774.63244529, 11934072.76351887, 0.00271929, 0.00205333, 0.00157208, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 137.51628646, 0.00085764, 164.73409832, 0.00862002, 16.47340983, 0.03461578, -137.51628646, -0.00085764, -164.73409832, -0.00862002, -16.47340983, -0.03461578, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 182.80013864, 0.00078533, 218.9807243, 0.00886948, 21.89807243, 0.03749446, -182.80013864, -0.00078533, -218.9807243, -0.00886948, -21.89807243, -0.03749446, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 161.1520203, 0.01715276, 161.1520203, 0.05145829, 112.80641421, -1913.99944778, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 40.28800507, 8.102e-05, 120.86401522, 0.00024306, 402.88005074, 0.00081021, -40.28800507, -8.102e-05, -120.86401522, -0.00024306, -402.88005074, -0.00081021, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 168.13063675, 0.01570655, 168.13063675, 0.04711964, 117.69144572, -2084.85830915, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 42.03265919, 8.453e-05, 126.09797756, 0.00025359, 420.32659187, 0.0008453, -42.03265919, -8.453e-05, -126.09797756, -0.00025359, -420.32659187, -0.0008453, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 37.6, 9.5, 3.95)
    ops.node(122024, 37.6, 9.5, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.0625, 29651021.27614199, 12354592.1983925, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 60.62287015, 0.0011689, 72.12898857, 0.01027947, 7.21289886, 0.04315602, -60.62287015, -0.0011689, -72.12898857, -0.01027947, -7.21289886, -0.04315602, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 57.06413008, 0.0011689, 67.89480565, 0.01027947, 6.78948056, 0.04315602, -57.06413008, -0.0011689, -67.89480565, -0.01027947, -6.78948056, -0.04315602, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 93.95793749, 0.02337792, 93.95793749, 0.07013376, 65.77055624, -1328.02185782, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 23.48948437, 0.00010221, 70.46845312, 0.00030664, 234.89484372, 0.00102213, -23.48948437, -0.00010221, -70.46845312, -0.00030664, -234.89484372, -0.00102213, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 93.95793749, 0.02337792, 93.95793749, 0.07013376, 65.77055624, -1328.02185782, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 23.48948437, 0.00010221, 70.46845312, 0.00030664, 234.89484372, 0.00102213, -23.48948437, -0.00010221, -70.46845312, -0.00030664, -234.89484372, -0.00102213, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.75)
    ops.node(123001, 0.0, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 29031822.8264651, 12096592.84436046, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 41.29358584, 0.00112298, 49.59649727, 0.01213542, 4.95964973, 0.05349037, -41.29358584, -0.00112298, -49.59649727, -0.01213542, -4.95964973, -0.05349037, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 41.29358584, 0.00112298, 49.59649727, 0.01213542, 4.95964973, 0.05349037, -41.29358584, -0.00112298, -49.59649727, -0.01213542, -4.95964973, -0.05349037, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 89.29890063, 0.02245958, 89.29890063, 0.06737874, 62.50923044, -1356.59448294, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 22.32472516, 9.922e-05, 66.97417547, 0.00029765, 223.24725156, 0.00099216, -22.32472516, -9.922e-05, -66.97417547, -0.00029765, -223.24725156, -0.00099216, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 89.29890063, 0.02245958, 89.29890063, 0.06737874, 62.50923044, -1356.59448294, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 22.32472516, 9.922e-05, 66.97417547, 0.00029765, 223.24725156, 0.00099216, -22.32472516, -9.922e-05, -66.97417547, -0.00029765, -223.24725156, -0.00099216, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 5.8, 0.0, 6.75)
    ops.node(123002, 5.8, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0875, 29072619.35094796, 12113591.39622832, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 65.44319824, 0.00110057, 78.33420034, 0.01073605, 7.83342003, 0.03967935, -65.44319824, -0.00110057, -78.33420034, -0.01073605, -7.83342003, -0.03967935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 88.16830204, 0.00083734, 105.5356954, 0.01158216, 10.55356954, 0.04906297, -88.16830204, -0.00083734, -105.5356954, -0.01158216, -10.55356954, -0.04906297, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 114.61309939, 0.02201139, 114.61309939, 0.06603417, 80.22916957, -1512.24500166, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 28.65327485, 9.083e-05, 85.95982454, 0.00027249, 286.53274848, 0.00090831, -28.65327485, -9.083e-05, -85.95982454, -0.00027249, -286.53274848, -0.00090831, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 131.62140869, 0.01674683, 131.62140869, 0.05024048, 92.13498608, -1997.06656721, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 32.90535217, 0.00010431, 98.71605651, 0.00031293, 329.05352171, 0.0010431, -32.90535217, -0.00010431, -98.71605651, -0.00031293, -329.05352171, -0.0010431, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 11.6, 0.0, 6.75)
    ops.node(123003, 11.6, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0875, 30722261.99766035, 12800942.49902515, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 63.12947955, 0.00105914, 75.44737123, 0.00920991, 7.54473712, 0.04111631, -63.12947955, -0.00105914, -75.44737123, -0.00920991, -7.54473712, -0.04111631, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 96.6411568, 0.00081779, 115.49788285, 0.00990696, 11.54978828, 0.05122491, -96.6411568, -0.00081779, -115.49788285, -0.00990696, -11.54978828, -0.05122491, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 106.28010395, 0.02118272, 106.28010395, 0.06354815, 74.39607277, -1298.70447243, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 26.57002599, 7.97e-05, 79.71007796, 0.00023911, 265.70025988, 0.00079704, -26.57002599, -7.97e-05, -79.71007796, -0.00023911, -265.70025988, -0.00079704, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 124.66032448, 0.01635575, 124.66032448, 0.04906725, 87.26222714, -1656.3661177, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 31.16508112, 9.349e-05, 93.49524336, 0.00028047, 311.6508112, 0.00093488, -31.16508112, -9.349e-05, -93.49524336, -0.00028047, -311.6508112, -0.00093488, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 26.0, 0.0, 6.75)
    ops.node(123006, 26.0, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0875, 29509492.97083487, 12295622.07118119, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 64.45419253, 0.00113064, 77.12926846, 0.00970146, 7.71292685, 0.03947057, -64.45419253, -0.00113064, -77.12926846, -0.00970146, -7.71292685, -0.03947057, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 98.87799279, 0.00086438, 118.32259393, 0.01042196, 11.83225939, 0.04897217, -98.87799279, -0.00086438, -118.32259393, -0.01042196, -11.83225939, -0.04897217, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 110.17767195, 0.02261272, 110.17767195, 0.06783816, 77.12437036, -1365.35323747, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 27.54441799, 8.602e-05, 82.63325396, 0.00025807, 275.44417987, 0.00086023, -27.54441799, -8.602e-05, -82.63325396, -0.00025807, -275.44417987, -0.00086023, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 124.91438831, 0.01728764, 124.91438831, 0.05186291, 87.44007182, -1762.05842983, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 31.22859708, 9.753e-05, 93.68579123, 0.00029259, 312.28597077, 0.00097529, -31.22859708, -9.753e-05, -93.68579123, -0.00029259, -312.28597077, -0.00097529, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 31.8, 0.0, 6.75)
    ops.node(123007, 31.8, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0875, 32469025.9492538, 13528760.81218908, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 65.1176805, 0.00117603, 77.58374883, 0.00901214, 7.75837488, 0.04361863, -65.1176805, -0.00117603, -77.58374883, -0.00901214, -7.75837488, -0.04361863, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 88.75479418, 0.0008721, 105.74592962, 0.00961038, 10.57459296, 0.05442486, -88.75479418, -0.0008721, -105.74592962, -0.00961038, -10.57459296, -0.05442486, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 108.4120057, 0.02352065, 108.4120057, 0.07056194, 75.88840399, -1308.1158215, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 27.10300143, 7.693e-05, 81.30900428, 0.00023079, 271.03001426, 0.00076929, -27.10300143, -7.693e-05, -81.30900428, -0.00023079, -271.03001426, -0.00076929, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 130.33771168, 0.01744192, 130.33771168, 0.05232577, 91.23639818, -1671.25255484, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 32.58442792, 9.249e-05, 97.75328376, 0.00027746, 325.84427921, 0.00092488, -32.58442792, -9.249e-05, -97.75328376, -0.00027746, -325.84427921, -0.00092488, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 37.6, 0.0, 6.75)
    ops.node(123008, 37.6, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 29547896.73788899, 12311623.64078708, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 41.47259463, 0.00116538, 49.78578748, 0.01086982, 4.97857875, 0.05337677, -41.47259463, -0.00116538, -49.78578748, -0.01086982, -4.97857875, -0.05337677, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 41.47259463, 0.00116538, 49.78578748, 0.01086982, 4.97857875, 0.05337677, -41.47259463, -0.00116538, -49.78578748, -0.01086982, -4.97857875, -0.05337677, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 85.31413765, 0.02330758, 85.31413765, 0.06992273, 59.71989635, -1197.76825178, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 21.32853441, 9.313e-05, 63.98560324, 0.0002794, 213.28534412, 0.00093133, -21.32853441, -9.313e-05, -63.98560324, -0.0002794, -213.28534412, -0.00093133, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 85.31413765, 0.02330758, 85.31413765, 0.06992273, 59.71989635, -1197.76825178, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 21.32853441, 9.313e-05, 63.98560324, 0.0002794, 213.28534412, 0.00093133, -21.32853441, -9.313e-05, -63.98560324, -0.0002794, -213.28534412, -0.00093133, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 4.75, 6.775)
    ops.node(123009, 0.0, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0875, 27001247.05718, 11250519.60715833, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 99.26481193, 0.00085344, 118.93240854, 0.01136408, 11.89324085, 0.03999007, -99.26481193, -0.00085344, -118.93240854, -0.01136408, -11.89324085, -0.03999007, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 68.38807844, 0.00112806, 81.93798715, 0.01060189, 8.19379872, 0.03297728, -68.38807844, -0.00112806, -81.93798715, -0.01060189, -8.19379872, -0.03297728, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 112.02364322, 0.01706881, 112.02364322, 0.05120642, 78.41655026, -1611.22265898, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 28.00591081, 9.559e-05, 84.01773242, 0.00028677, 280.05910806, 0.00095589, -28.00591081, -9.559e-05, -84.01773242, -0.00028677, -280.05910806, -0.00095589, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 91.87985902, 0.02256125, 91.87985902, 0.06768374, 64.31590131, -1258.19647309, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 22.96996475, 7.84e-05, 68.90989426, 0.0002352, 229.69964755, 0.00078401, -22.96996475, -7.84e-05, -68.90989426, -0.0002352, -229.69964755, -0.00078401, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 5.8, 4.75, 6.775)
    ops.node(123010, 5.8, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.2, 28756295.38523661, 11981789.74384859, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 288.66949619, 0.00065769, 348.35575014, 0.01034652, 34.83557501, 0.03436843, -288.66949619, -0.00065769, -348.35575014, -0.01034652, -34.83557501, -0.03436843, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 206.26664021, 0.00074388, 248.91500878, 0.00992731, 24.89150088, 0.03108251, -206.26664021, -0.00074388, -248.91500878, -0.00992731, -24.89150088, -0.03108251, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 211.35954583, 0.01315375, 211.35954583, 0.03946125, 147.95168208, -1871.0555007, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 52.83988646, 7.409e-05, 158.51965937, 0.00022226, 528.39886456, 0.00074088, -52.83988646, -7.409e-05, -158.51965937, -0.00022226, -528.39886456, -0.00074088, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 181.16401648, 0.01487768, 181.16401648, 0.04463303, 126.81481154, -1626.60955661, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 45.29100412, 6.35e-05, 135.87301236, 0.00019051, 452.9100412, 0.00063504, -45.29100412, -6.35e-05, -135.87301236, -0.00019051, -452.9100412, -0.00063504, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 11.6, 4.75, 6.775)
    ops.node(123011, 11.6, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.2, 31241751.10258349, 13017396.29274312, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 273.80808352, 0.00067366, 328.97405364, 0.0094877, 32.89740536, 0.03570918, -273.80808352, -0.00067366, -328.97405364, -0.0094877, -32.89740536, -0.03570918, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 202.08722016, 0.00076541, 242.80310191, 0.00911968, 24.28031019, 0.03221195, -202.08722016, -0.00076541, -242.80310191, -0.00911968, -24.28031019, -0.03221195, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 228.01575059, 0.01347327, 228.01575059, 0.04041982, 159.61102541, -1845.03945162, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 57.00393765, 7.357e-05, 171.01181294, 0.0002207, 570.03937648, 0.00073568, -57.00393765, -7.357e-05, -171.01181294, -0.0002207, -570.03937648, -0.00073568, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 195.81611685, 0.01530818, 195.81611685, 0.04592453, 137.07128179, -1607.19419591, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 48.95402921, 6.318e-05, 146.86208764, 0.00018954, 489.54029212, 0.00063179, -48.95402921, -6.318e-05, -146.86208764, -0.00018954, -489.54029212, -0.00063179, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 17.4, 4.75, 6.775)
    ops.node(123012, 17.4, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.14, 28937022.7861094, 12057092.82754558, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 165.08868396, 0.00078436, 198.82890982, 0.00863076, 19.88289098, 0.03356883, -165.08868396, -0.00078436, -198.82890982, -0.00863076, -19.88289098, -0.03356883, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 142.44510551, 0.00086038, 171.55751901, 0.00844029, 17.1557519, 0.03141591, -142.44510551, -0.00086038, -171.55751901, -0.00844029, -17.1557519, -0.03141591, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 135.17467116, 0.01568726, 135.17467116, 0.04706177, 94.62226981, -1361.52913046, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 33.79366779, 6.727e-05, 101.38100337, 0.0002018, 337.93667791, 0.00067267, -33.79366779, -6.727e-05, -101.38100337, -0.0002018, -337.93667791, -0.00067267, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 117.82883886, 0.01720757, 117.82883886, 0.05162272, 82.4801872, -1259.74134056, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 29.45720972, 5.864e-05, 88.37162915, 0.00017591, 294.57209716, 0.00058635, -29.45720972, -5.864e-05, -88.37162915, -0.00017591, -294.57209716, -0.00058635, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 20.2, 4.75, 6.775)
    ops.node(123013, 20.2, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.14, 26152220.18426416, 10896758.41011007, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 162.78799966, 0.00075173, 196.30314295, 0.00913516, 19.63031429, 0.03031315, -162.78799966, -0.00075173, -196.30314295, -0.00913516, -19.63031429, -0.03031315, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 140.77806118, 0.00081976, 169.76175103, 0.00891847, 16.9761751, 0.0284299, -140.77806118, -0.00081976, -169.76175103, -0.00891847, -16.9761751, -0.0284299, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 129.04819699, 0.01503455, 129.04819699, 0.04510364, 90.33373789, -1437.33991242, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 32.26204925, 7.106e-05, 96.78614774, 0.00021317, 322.62049248, 0.00071057, -32.26204925, -7.106e-05, -96.78614774, -0.00021317, -322.62049248, -0.00071057, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 115.99401059, 0.01639525, 115.99401059, 0.04918576, 81.19580741, -1323.46995806, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 28.99850265, 6.387e-05, 86.99550794, 0.00019161, 289.98502646, 0.00063869, -28.99850265, -6.387e-05, -86.99550794, -0.00019161, -289.98502646, -0.00063869, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 26.0, 4.75, 6.775)
    ops.node(123014, 26.0, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.2, 28172494.4326057, 11738539.34691904, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 273.07344381, 0.00069413, 329.75270526, 0.00884344, 32.97527053, 0.03225638, -273.07344381, -0.00069413, -329.75270526, -0.00884344, -32.97527053, -0.03225638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 201.1710963, 0.00079306, 242.92627032, 0.00851728, 24.29262703, 0.02913618, -201.1710963, -0.00079306, -242.92627032, -0.00851728, -24.29262703, -0.02913618, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 202.86356925, 0.01388255, 202.86356925, 0.04164766, 142.00449847, -1760.83046456, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 50.71589231, 7.258e-05, 152.14767694, 0.00021775, 507.15892312, 0.00072584, -50.71589231, -7.258e-05, -152.14767694, -0.00021775, -507.15892312, -0.00072584, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 174.06401599, 0.01586126, 174.06401599, 0.04758378, 121.84481119, -1544.21404976, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 43.516004, 6.228e-05, 130.54801199, 0.00018684, 435.16003997, 0.00062279, -43.516004, -6.228e-05, -130.54801199, -0.00018684, -435.16003997, -0.00062279, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 31.8, 4.75, 6.775)
    ops.node(123015, 31.8, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.2, 26829606.16751771, 11179002.56979905, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 288.36658039, 0.00068497, 348.54288059, 0.00903371, 34.85428806, 0.03089225, -288.36658039, -0.00068497, -348.54288059, -0.00903371, -34.85428806, -0.03089225, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 205.92998776, 0.00078153, 248.90343062, 0.00869478, 24.89034306, 0.02794477, -205.92998776, -0.00078153, -248.90343062, -0.00869478, -24.89034306, -0.02794477, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 194.26898208, 0.01369934, 194.26898208, 0.04109802, 135.98828746, -1774.06250997, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 48.56724552, 7.299e-05, 145.70173656, 0.00021896, 485.6724552, 0.00072988, -48.56724552, -7.299e-05, -145.70173656, -0.00021896, -485.6724552, -0.00072988, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 166.50311774, 0.0156306, 166.50311774, 0.0468918, 116.55218242, -1554.12450207, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 41.62577944, 6.256e-05, 124.87733831, 0.00018767, 416.25779436, 0.00062556, -41.62577944, -6.256e-05, -124.87733831, -0.00018767, -416.25779436, -0.00062556, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 37.6, 4.75, 6.775)
    ops.node(123016, 37.6, 4.75, 8.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0875, 34109029.68749252, 14212095.70312188, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 101.76804727, 0.00084924, 120.81717615, 0.01198754, 12.08171762, 0.05394996, -101.76804727, -0.00084924, -120.81717615, -0.01198754, -12.08171762, -0.05394996, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 70.17140289, 0.00112581, 83.30621419, 0.01116539, 8.33062142, 0.04396516, -70.17140289, -0.00112581, -83.30621419, -0.01116539, -8.33062142, -0.04396516, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 133.73107956, 0.01698476, 133.73107956, 0.05095427, 93.61175569, -1645.68782685, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 33.43276989, 9.033e-05, 100.29830967, 0.000271, 334.3276989, 0.00090333, -33.43276989, -9.033e-05, -100.29830967, -0.000271, -334.3276989, -0.00090333, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 114.63734795, 0.02251623, 114.63734795, 0.06754869, 80.24614357, -1279.92889287, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 28.65933699, 7.744e-05, 85.97801096, 0.00023231, 286.59336988, 0.00077435, -28.65933699, -7.744e-05, -85.97801096, -0.00023231, -286.59336988, -0.00077435, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 9.5, 6.75)
    ops.node(123017, 0.0, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 32875036.15571297, 13697931.73154707, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 41.56444061, 0.0011101, 49.58725739, 0.01189162, 4.95872574, 0.06058807, -41.56444061, -0.0011101, -49.58725739, -0.01189162, -4.95872574, -0.06058807, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 41.56444061, 0.0011101, 49.58725739, 0.01189162, 4.95872574, 0.06058807, -41.56444061, -0.0011101, -49.58725739, -0.01189162, -4.95872574, -0.06058807, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 96.19494826, 0.02220194, 96.19494826, 0.06660581, 67.33646378, -1326.27282654, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 24.04873706, 9.438e-05, 72.14621119, 0.00028315, 240.48737065, 0.00094384, -24.04873706, -9.438e-05, -72.14621119, -0.00028315, -240.48737065, -0.00094384, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 96.19494826, 0.02220194, 96.19494826, 0.06660581, 67.33646378, -1326.27282654, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 24.04873706, 9.438e-05, 72.14621119, 0.00028315, 240.48737065, 0.00094384, -24.04873706, -9.438e-05, -72.14621119, -0.00028315, -240.48737065, -0.00094384, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 5.8, 9.5, 6.75)
    ops.node(123018, 5.8, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0875, 30873640.36597519, 12864016.81915633, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 65.44228852, 0.00114973, 78.19494555, 0.0106389, 7.81949456, 0.0427965, -65.44228852, -0.00114973, -78.19494555, -0.0106389, -7.81949456, -0.0427965, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 88.7960224, 0.00086184, 106.09959239, 0.0114435, 10.60995924, 0.05308673, -88.7960224, -0.00086184, -106.09959239, -0.0114435, -10.60995924, -0.05308673, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 116.65710805, 0.02299466, 116.65710805, 0.06898397, 81.65997564, -1430.24728038, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 29.16427701, 8.706e-05, 87.49283104, 0.00026117, 291.64277013, 0.00087057, -29.16427701, -8.706e-05, -87.49283104, -0.00026117, -291.64277013, -0.00087057, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 132.41171964, 0.01723685, 132.41171964, 0.05171054, 92.68820375, -1865.54651883, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 33.10292991, 9.881e-05, 99.30878973, 0.00029644, 331.0292991, 0.00098815, -33.10292991, -9.881e-05, -99.30878973, -0.00029644, -331.0292991, -0.00098815, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 11.6, 9.5, 6.75)
    ops.node(123019, 11.6, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0875, 29809683.56008601, 12420701.48336917, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 64.49547477, 0.00113542, 77.15960202, 0.00872378, 7.7159602, 0.03904296, -64.49547477, -0.00113542, -77.15960202, -0.00872378, -7.7159602, -0.03904296, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 98.89350087, 0.0008667, 118.31191565, 0.00932871, 11.83119156, 0.04859124, -98.89350087, -0.0008667, -118.31191565, -0.00932871, -11.83119156, -0.04859124, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 100.93468666, 0.02270846, 100.93468666, 0.06812537, 70.65428066, -1282.84222975, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 25.23367167, 7.801e-05, 75.701015, 0.00023404, 252.33671666, 0.00078013, -25.23367167, -7.801e-05, -75.701015, -0.00023404, -252.33671666, -0.00078013, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 121.11911083, 0.01733392, 121.11911083, 0.05200176, 84.78337758, -1631.30527163, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 30.27977771, 9.361e-05, 90.83933312, 0.00028084, 302.79777708, 0.00093613, -30.27977771, -9.361e-05, -90.83933312, -0.00028084, -302.79777708, -0.00093613, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 17.4, 9.5, 6.75)
    ops.node(123020, 17.4, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 30651788.08610618, 12771578.36921091, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 47.96943092, 0.00108909, 57.31162851, 0.01230352, 5.73116285, 0.05297767, -47.96943092, -0.00108909, -57.31162851, -0.01230352, -5.73116285, -0.05297767, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 47.96943092, 0.00108909, 57.31162851, 0.01230352, 5.73116285, 0.05297767, -47.96943092, -0.00108909, -57.31162851, -0.01230352, -5.73116285, -0.05297767, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 101.75890494, 0.02178189, 101.75890494, 0.06534567, 71.23123346, -1556.09236061, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 25.43972623, 0.00010708, 76.3191787, 0.00032125, 254.39726235, 0.00107085, -25.43972623, -0.00010708, -76.3191787, -0.00032125, -254.39726235, -0.00107085, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 101.75890494, 0.02178189, 101.75890494, 0.06534567, 71.23123346, -1556.09236061, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 25.43972623, 0.00010708, 76.3191787, 0.00032125, 254.39726235, 0.00107085, -25.43972623, -0.00010708, -76.3191787, -0.00032125, -254.39726235, -0.00107085, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 20.2, 9.5, 6.75)
    ops.node(123021, 20.2, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 27713405.78159033, 11547252.40899597, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 46.73683078, 0.00113182, 55.92028926, 0.00929975, 5.59202893, 0.04263692, -46.73683078, -0.00113182, -55.92028926, -0.00929975, -5.59202893, -0.04263692, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 46.73683078, 0.00113182, 55.92028926, 0.00929975, 5.59202893, 0.04263692, -46.73683078, -0.00113182, -55.92028926, -0.00929975, -5.59202893, -0.04263692, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 75.10847819, 0.02263637, 75.10847819, 0.06790911, 52.57593474, -1161.37914914, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 18.77711955, 8.742e-05, 56.33135865, 0.00026226, 187.77119549, 0.0008742, -18.77711955, -8.742e-05, -56.33135865, -0.00026226, -187.77119549, -0.0008742, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 75.10847819, 0.02263637, 75.10847819, 0.06790911, 52.57593474, -1161.37914914, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 18.77711955, 8.742e-05, 56.33135865, 0.00026226, 187.77119549, 0.0008742, -18.77711955, -8.742e-05, -56.33135865, -0.00026226, -187.77119549, -0.0008742, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 26.0, 9.5, 6.75)
    ops.node(123022, 26.0, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0875, 28408137.80361635, 11836724.08484015, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 60.63923115, 0.00115211, 72.59938164, 0.01088402, 7.25993816, 0.03851307, -60.63923115, -0.00115211, -72.59938164, -0.01088402, -7.25993816, -0.03851307, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 92.2009129, 0.00085986, 110.38611698, 0.01171222, 11.0386117, 0.04749109, -92.2009129, -0.00085986, -110.38611698, -0.01171222, -11.0386117, -0.04749109, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 112.63287259, 0.02304221, 112.63287259, 0.06912664, 78.84301081, -1509.48576036, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 28.15821815, 9.135e-05, 84.47465444, 0.00027405, 281.58218148, 0.00091349, -28.15821815, -9.135e-05, -84.47465444, -0.00027405, -281.58218148, -0.00091349, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 129.59955553, 0.0171973, 129.59955553, 0.05159189, 90.71968887, -1992.62782802, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 32.39988888, 0.00010511, 97.19966665, 0.00031533, 323.99888882, 0.0010511, -32.39988888, -0.00010511, -97.19966665, -0.00031533, -323.99888882, -0.0010511, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 31.8, 9.5, 6.75)
    ops.node(123023, 31.8, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.0875, 29458187.76720933, 12274244.90300389, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 65.14490863, 0.00114617, 77.9587367, 0.00988962, 7.79587367, 0.03956331, -65.14490863, -0.00114617, -77.9587367, -0.00988962, -7.79587367, -0.03956331, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 88.27629733, 0.00086078, 105.64000725, 0.01061086, 10.56400072, 0.0490375, -88.27629733, -0.00086078, -105.64000725, -0.01061086, -10.56400072, -0.0490375, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 111.01583372, 0.02292345, 111.01583372, 0.06877034, 77.7110836, -1390.28349282, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 27.75395843, 8.683e-05, 83.26187529, 0.00026048, 277.5395843, 0.00086828, -27.75395843, -8.683e-05, -83.26187529, -0.00026048, -277.5395843, -0.00086828, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 126.14639634, 0.01721553, 126.14639634, 0.0516466, 88.30247744, -1801.7500354, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 31.53659909, 9.866e-05, 94.60979726, 0.00029599, 315.36599086, 0.00098662, -31.53659909, -9.866e-05, -94.60979726, -0.00029599, -315.36599086, -0.00098662, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 37.6, 9.5, 6.75)
    ops.node(123024, 37.6, 9.5, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 28711573.28921484, 11963155.53717285, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 43.14289164, 0.00111667, 51.83082087, 0.01177018, 5.18308209, 0.0523816, -43.14289164, -0.00111667, -51.83082087, -0.01177018, -5.18308209, -0.0523816, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 43.14289164, 0.00111667, 51.83082087, 0.01177018, 5.18308209, 0.0523816, -43.14289164, -0.00111667, -51.83082087, -0.01177018, -5.18308209, -0.0523816, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 88.54444621, 0.02233333, 88.54444621, 0.06699998, 61.98111235, -1352.56081998, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 22.13611155, 9.948e-05, 66.40833466, 0.00029843, 221.36111553, 0.00099475, -22.13611155, -9.948e-05, -66.40833466, -0.00029843, -221.36111553, -0.00099475, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 88.54444621, 0.02233333, 88.54444621, 0.06699998, 61.98111235, -1352.56081998, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 22.13611155, 9.948e-05, 66.40833466, 0.00029843, 221.36111553, 0.00099475, -22.13611155, -9.948e-05, -66.40833466, -0.00029843, -221.36111553, -0.00099475, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.55)
    ops.node(124001, 0.0, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26524091.41939091, 11051704.75807955, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 37.23530297, 0.00108561, 45.39332257, 0.01432999, 4.53933226, 0.0679506, -37.23530297, -0.00108561, -45.39332257, -0.01432999, -4.53933226, -0.0679506, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 34.0339949, 0.00108561, 41.49062813, 0.01432999, 4.14906281, 0.0679506, -34.0339949, -0.00108561, -41.49062813, -0.01432999, -4.14906281, -0.0679506, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 72.27585771, 0.02171226, 72.27585771, 0.06513679, 50.59310039, -1625.92204419, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 18.06896443, 8.789e-05, 54.20689328, 0.00026368, 180.68964426, 0.00087895, -18.06896443, -8.789e-05, -54.20689328, -0.00026368, -180.68964426, -0.00087895, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 72.27585771, 0.02171226, 72.27585771, 0.06513679, 50.59310039, -1625.92204419, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 18.06896443, 8.789e-05, 54.20689328, 0.00026368, 180.68964426, 0.00087895, -18.06896443, -8.789e-05, -54.20689328, -0.00026368, -180.68964426, -0.00087895, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 5.8, 0.0, 9.55)
    ops.node(124002, 5.8, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0875, 33340524.8414375, 13891885.35059896, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 41.87778847, 0.00101918, 50.17352104, 0.01039003, 5.0173521, 0.05531774, -41.87778847, -0.00101918, -50.17352104, -0.01039003, -5.0173521, -0.05531774, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 65.8022841, 0.00077959, 78.83731226, 0.01122932, 7.88373123, 0.06940951, -65.8022841, -0.00077959, -78.83731226, -0.01122932, -7.88373123, -0.06940951, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 98.78488826, 0.0203835, 98.78488826, 0.06115051, 69.14942178, -1113.97199015, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 24.69622207, 6.827e-05, 74.0886662, 0.0002048, 246.96222066, 0.00068265, -24.69622207, -6.827e-05, -74.0886662, -0.0002048, -246.96222066, -0.00068265, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 114.44107225, 0.01559189, 114.44107225, 0.04677568, 80.10875057, -1656.39673734, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 28.61026806, 7.908e-05, 85.83080419, 0.00023725, 286.10268062, 0.00079085, -28.61026806, -7.908e-05, -85.83080419, -0.00023725, -286.10268062, -0.00079085, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 11.6, 0.0, 9.55)
    ops.node(124003, 11.6, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0875, 29093011.75661206, 12122088.23192169, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 40.46730962, 0.00097586, 49.02276439, 0.01128621, 4.90227644, 0.05273144, -40.46730962, -0.00097586, -49.02276439, -0.01128621, -4.90227644, -0.05273144, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 63.8575989, 0.0007538, 77.3581455, 0.01225118, 7.73581455, 0.06592166, -63.8575989, -0.0007538, -77.3581455, -0.01225118, -7.73581455, -0.06592166, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 92.37557204, 0.01951712, 92.37557204, 0.05855136, 64.66290042, -1242.78354556, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 23.09389301, 7.316e-05, 69.28167903, 0.00021947, 230.93893009, 0.00073156, -23.09389301, -7.316e-05, -69.28167903, -0.00021947, -230.93893009, -0.00073156, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 107.6728313, 0.01507594, 107.6728313, 0.04522781, 75.37098191, -1877.18881788, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 26.91820783, 8.527e-05, 80.75462348, 0.00025581, 269.18207826, 0.00085271, -26.91820783, -8.527e-05, -80.75462348, -0.00025581, -269.18207826, -0.00085271, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 26.0, 0.0, 9.55)
    ops.node(124006, 26.0, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0875, 29369354.30670407, 12237230.96112669, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 41.03780481, 0.00104366, 49.68721128, 0.01089031, 4.96872113, 0.05262066, -41.03780481, -0.00104366, -49.68721128, -0.01089031, -4.96872113, -0.05262066, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 64.58111248, 0.00079262, 78.19266638, 0.01177291, 7.81926664, 0.06581261, -64.58111248, -0.00079262, -78.19266638, -0.01177291, -7.81926664, -0.06581261, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 88.78624223, 0.02087329, 88.78624223, 0.06261988, 62.15036956, -1149.14884549, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 22.19656056, 6.965e-05, 66.58968167, 0.00020896, 221.96560556, 0.00069652, -22.19656056, -6.965e-05, -66.58968167, -0.00020896, -221.96560556, -0.00069652, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 104.95949157, 0.01585236, 104.95949157, 0.04755708, 73.4716441, -1716.51822798, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 26.23987289, 8.234e-05, 78.71961868, 0.00024702, 262.39872894, 0.0008234, -26.23987289, -8.234e-05, -78.71961868, -0.00024702, -262.39872894, -0.0008234, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 31.8, 0.0, 9.55)
    ops.node(124007, 31.8, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0875, 28556396.76498147, 11898498.65207561, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 41.56914091, 0.00101043, 50.40619954, 0.01263419, 5.04061995, 0.05349715, -41.56914091, -0.00101043, -50.40619954, -0.01263419, -5.04061995, -0.05349715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 65.70680768, 0.00077792, 79.67522028, 0.01373992, 7.96752203, 0.06665637, -65.70680768, -0.00077792, -79.67522028, -0.01373992, -7.96752203, -0.06665637, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 95.47229737, 0.02020866, 95.47229737, 0.06062597, 66.83060816, -1395.75878153, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 23.86807434, 7.703e-05, 71.60422303, 0.00023109, 238.68074343, 0.00077029, -23.86807434, -7.703e-05, -71.60422303, -0.00023109, -238.68074343, -0.00077029, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 111.62749244, 0.01555836, 111.62749244, 0.04667508, 78.13924471, -2141.46308984, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 27.90687311, 9.006e-05, 83.72061933, 0.00027019, 279.06873111, 0.00090064, -27.90687311, -9.006e-05, -83.72061933, -0.00027019, -279.06873111, -0.00090064, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 37.6, 0.0, 9.55)
    ops.node(124008, 37.6, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 28238947.50153174, 11766228.12563823, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 37.52864254, 0.00101849, 45.62838812, 0.01477637, 4.56283881, 0.07068728, -37.52864254, -0.00101849, -45.62838812, -0.01477637, -4.56283881, -0.07068728, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 34.06955813, 0.00101849, 41.42273517, 0.01477637, 4.14227352, 0.07068728, -34.06955813, -0.00101849, -41.42273517, -0.01477637, -4.14227352, -0.07068728, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 80.02239694, 0.02036983, 80.02239694, 0.06110948, 56.01567786, -1927.47285042, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 20.00559923, 9.141e-05, 60.0167977, 0.00027422, 200.05599234, 0.00091406, -20.00559923, -9.141e-05, -60.0167977, -0.00027422, -200.05599234, -0.00091406, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 80.02239694, 0.02036983, 80.02239694, 0.06110948, 56.01567786, -1927.47285042, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 20.00559923, 9.141e-05, 60.0167977, 0.00027422, 200.05599234, 0.00091406, -20.00559923, -9.141e-05, -60.0167977, -0.00027422, -200.05599234, -0.00091406, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 4.75, 9.575)
    ops.node(124009, 0.0, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0875, 28849828.05117931, 12020761.68799138, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 74.0608976, 0.00078946, 89.75689509, 0.0121588, 8.97568951, 0.05836733, -74.0608976, -0.00078946, -89.75689509, -0.0121588, -8.97568951, -0.05836733, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 50.60369947, 0.00102885, 61.32832698, 0.01127668, 6.1328327, 0.0473954, -50.60369947, -0.00102885, -61.32832698, -0.01127668, -6.1328327, -0.0473954, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 99.08795713, 0.01578914, 99.08795713, 0.04736743, 69.36156999, -1513.6115347, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 24.77198928, 7.913e-05, 74.31596785, 0.0002374, 247.71989283, 0.00079133, -24.77198928, -7.913e-05, -74.31596785, -0.0002374, -247.71989283, -0.00079133, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 65.69291312, 0.02057709, 65.69291312, 0.06173126, 45.98503918, -1030.51182199, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 16.42322828, 5.246e-05, 49.26968484, 0.00015739, 164.2322828, 0.00052464, -16.42322828, -5.246e-05, -49.26968484, -0.00015739, -164.2322828, -0.00052464, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 5.8, 4.75, 9.575)
    ops.node(124010, 5.8, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.2, 31096026.82304648, 12956677.84293604, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 233.4737076, 0.00063534, 282.00126867, 0.01125917, 28.20012687, 0.04153334, -233.4737076, -0.00063534, -282.00126867, -0.01125917, -28.20012687, -0.04153334, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 164.34219555, 0.00071896, 198.50075676, 0.01078862, 19.85007568, 0.03744995, -164.34219555, -0.00071896, -198.50075676, -0.01078862, -19.85007568, -0.03744995, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 207.94289672, 0.0127067, 207.94289672, 0.03812011, 145.5600277, -1816.44482631, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 51.98572418, 6.741e-05, 155.95717254, 0.00020222, 519.85724179, 0.00067406, -51.98572418, -6.741e-05, -155.95717254, -0.00020222, -519.85724179, -0.00067406, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 177.8801112, 0.01437923, 177.8801112, 0.04313769, 124.51607784, -1445.82311653, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 44.4700278, 5.766e-05, 133.4100834, 0.00017298, 444.70027801, 0.00057661, -44.4700278, -5.766e-05, -133.4100834, -0.00017298, -444.70027801, -0.00057661, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 11.6, 4.75, 9.575)
    ops.node(124011, 11.6, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.2, 30488544.4621688, 12703560.19257033, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 209.87987747, 0.00062368, 253.90998124, 0.00912777, 25.39099812, 0.03913243, -209.87987747, -0.00062368, -253.90998124, -0.00912777, -25.39099812, -0.03913243, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 152.73393581, 0.00070372, 184.77555468, 0.00876421, 18.47755547, 0.03518819, -152.73393581, -0.00070372, -184.77555468, -0.00876421, -18.47755547, -0.03518819, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 192.34514155, 0.01247354, 192.34514155, 0.03742063, 134.64159909, -1429.29409772, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 48.08628539, 6.359e-05, 144.25885616, 0.00019078, 480.86285388, 0.00063592, -48.08628539, -6.359e-05, -144.25885616, -0.00019078, -480.86285388, -0.00063592, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 158.89365432, 0.01407441, 158.89365432, 0.04222324, 111.22555802, -1167.7918375, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 39.72341358, 5.253e-05, 119.17024074, 0.0001576, 397.2341358, 0.00052533, -39.72341358, -5.253e-05, -119.17024074, -0.0001576, -397.2341358, -0.00052533, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 17.4, 4.75, 9.575)
    ops.node(124012, 17.4, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.14, 28815020.79176477, 12006258.66323532, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 123.34216885, 0.00072158, 149.71216111, 0.00950453, 14.97121611, 0.04065453, -123.34216885, -0.00072158, -149.71216111, -0.00950453, -14.97121611, -0.04065453, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 106.03671151, 0.00078963, 128.70687604, 0.0092743, 12.8706876, 0.03797301, -106.03671151, -0.00078963, -128.70687604, -0.0092743, -12.8706876, -0.03797301, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 113.18280887, 0.01443151, 113.18280887, 0.04329453, 79.22796621, -1128.72635827, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 28.29570222, 5.656e-05, 84.88710665, 0.00016969, 282.95702217, 0.00056562, -28.29570222, -5.656e-05, -84.88710665, -0.00016969, -282.95702217, -0.00056562, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 96.22659473, 0.01579266, 96.22659473, 0.04737799, 67.35861631, -994.91983509, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 24.05664868, 4.809e-05, 72.16994605, 0.00014426, 240.56648683, 0.00048088, -24.05664868, -4.809e-05, -72.16994605, -0.00014426, -240.56648683, -0.00048088, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 20.2, 4.75, 9.575)
    ops.node(124013, 20.2, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.14, 25682464.47562659, 10701026.86484441, 0.00271929, 0.00157208, 0.00205333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 130.41702743, 0.00072087, 159.01121211, 0.01041213, 15.90112121, 0.03898082, -130.41702743, -0.00072087, -159.01121211, -0.01041213, -15.90112121, -0.03898082, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 112.53842775, 0.00078425, 137.21269498, 0.01014637, 13.7212695, 0.0364669, -112.53842775, -0.00078425, -137.21269498, -0.01014637, -13.7212695, -0.0364669, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 110.99892587, 0.01441739, 110.99892587, 0.04325218, 77.69924811, -1252.84731104, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 27.74973147, 6.224e-05, 83.2491944, 0.00018671, 277.49731467, 0.00062236, -27.74973147, -6.224e-05, -83.2491944, -0.00018671, -277.49731467, -0.00062236, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 96.74436882, 0.01568499, 96.74436882, 0.04705498, 67.72105817, -1096.70439669, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 24.1860922, 5.424e-05, 72.55827661, 0.00016273, 241.86092205, 0.00054244, -24.1860922, -5.424e-05, -72.55827661, -0.00016273, -241.86092205, -0.00054244, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 26.0, 4.75, 9.575)
    ops.node(124014, 26.0, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.2, 30854831.70625789, 12856179.87760746, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 210.47312794, 0.00062285, 254.38524536, 0.00955749, 25.43852454, 0.03972711, -210.47312794, -0.00062285, -254.38524536, -0.00955749, -25.43852454, -0.03972711, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 153.18968269, 0.00070242, 185.15045317, 0.009171, 18.51504532, 0.03574027, -153.18968269, -0.00070242, -185.15045317, -0.009171, -18.51504532, -0.03574027, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 196.35939013, 0.01245694, 196.35939013, 0.03737083, 137.45157309, -1476.74881406, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 49.08984753, 6.415e-05, 147.2695426, 0.00019245, 490.89847533, 0.00064149, -49.08984753, -6.415e-05, -147.2695426, -0.00019245, -490.89847533, -0.00064149, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 167.51183477, 0.0140485, 167.51183477, 0.04214549, 117.25828434, -1202.07520416, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 41.87795869, 5.472e-05, 125.63387608, 0.00016417, 418.77958693, 0.00054725, -41.87795869, -5.472e-05, -125.63387608, -0.00016417, -418.77958693, -0.00054725, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 31.8, 4.75, 9.575)
    ops.node(124015, 31.8, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.2, 28288923.7208566, 11787051.55035692, 0.00547417, 0.00293333, 0.00458333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 249.42806618, 0.00065266, 303.22059719, 0.01065724, 30.32205972, 0.03949025, -249.42806618, -0.00065266, -303.22059719, -0.01065724, -30.32205972, -0.03949025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 174.58384924, 0.00073624, 212.2352141, 0.01021895, 21.22352141, 0.0356111, -174.58384924, -0.00073624, -212.2352141, -0.01021895, -21.22352141, -0.0356111, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 186.23057023, 0.01305315, 186.23057023, 0.03915944, 130.36139916, -1723.7061152, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 46.55764256, 6.636e-05, 139.67292767, 0.00019907, 465.57642558, 0.00066358, -46.55764256, -6.636e-05, -139.67292767, -0.00019907, -465.57642558, -0.00066358, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 159.07704743, 0.01472482, 159.07704743, 0.04417447, 111.3539332, -1379.54275292, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 39.76926186, 5.668e-05, 119.30778557, 0.00017005, 397.69261857, 0.00056683, -39.76926186, -5.668e-05, -119.30778557, -0.00017005, -397.69261857, -0.00056683, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 37.6, 4.75, 9.575)
    ops.node(124016, 37.6, 4.75, 11.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0875, 29721660.9941299, 12384025.41422079, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 73.22655032, 0.00078528, 88.59442995, 0.01251981, 8.859443, 0.05973433, -73.22655032, -0.00078528, -88.59442995, -0.01251981, -8.859443, -0.05973433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 49.98884443, 0.0010257, 60.47988274, 0.01160269, 6.04798827, 0.04850773, -49.98884443, -0.0010257, -60.47988274, -0.01160269, -6.04798827, -0.04850773, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 101.66376186, 0.01570563, 101.66376186, 0.04711688, 71.16463331, -1526.37207926, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 25.41594047, 7.881e-05, 76.2478214, 0.00023643, 254.15940466, 0.00078809, -25.41594047, -7.881e-05, -76.2478214, -0.00023643, -254.15940466, -0.00078809, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 71.42196859, 0.02051396, 71.42196859, 0.06154188, 49.99537801, -1038.03043946, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 17.85549215, 5.537e-05, 53.56647644, 0.0001661, 178.55492147, 0.00055366, -17.85549215, -5.537e-05, -53.56647644, -0.0001661, -178.55492147, -0.00055366, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 9.5, 9.55)
    ops.node(124017, 0.0, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 26109851.63553866, 10879104.84814111, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 38.85109169, 0.00101997, 47.38671872, 0.0153958, 4.73867187, 0.06837918, -38.85109169, -0.00101997, -47.38671872, -0.0153958, -4.73867187, -0.06837918, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 34.98422704, 0.00101997, 42.67029971, 0.0153958, 4.26702997, 0.06837918, -34.98422704, -0.00101997, -42.67029971, -0.0153958, -4.26702997, -0.06837918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 78.68663797, 0.02039948, 78.68663797, 0.06119844, 55.08064658, -2092.21003232, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 19.67165949, 9.721e-05, 59.01497848, 0.00029163, 196.71659493, 0.00097209, -19.67165949, -9.721e-05, -59.01497848, -0.00029163, -196.71659493, -0.00097209, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 78.68663797, 0.02039948, 78.68663797, 0.06119844, 55.08064658, -2092.21003232, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 19.67165949, 9.721e-05, 59.01497848, 0.00029163, 196.71659493, 0.00097209, -19.67165949, -9.721e-05, -59.01497848, -0.00029163, -196.71659493, -0.00097209, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 5.8, 9.5, 9.55)
    ops.node(124018, 5.8, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0875, 30098005.68731456, 12540835.70304773, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 41.68707178, 0.00103303, 50.39568124, 0.01239992, 5.03956812, 0.05483718, -41.68707178, -0.00103303, -50.39568124, -0.01239992, -5.03956812, -0.05483718, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 65.6981784, 0.0007892, 79.42281181, 0.01346477, 7.94228118, 0.06841988, -65.6981784, -0.0007892, -79.42281181, -0.01346477, -7.94228118, -0.06841988, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 99.33715553, 0.02066068, 99.33715553, 0.06198203, 69.53600887, -1388.86330452, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 24.83428888, 7.604e-05, 74.50286665, 0.00022813, 248.34288882, 0.00076043, -24.83428888, -7.604e-05, -74.50286665, -0.00022813, -248.34288882, -0.00076043, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 115.42538307, 0.01578403, 115.42538307, 0.04735209, 80.79776815, -2129.50746125, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 28.85634577, 8.836e-05, 86.5690373, 0.00026507, 288.56345768, 0.00088358, -28.85634577, -8.836e-05, -86.5690373, -0.00026507, -288.56345768, -0.00088358, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 11.6, 9.5, 9.55)
    ops.node(124019, 11.6, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0875, 28852692.34581239, 12021955.1440885, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 40.61228311, 0.0010831, 49.22028533, 0.01184417, 4.92202853, 0.05303342, -40.61228311, -0.0010831, -49.22028533, -0.01184417, -4.92202853, -0.05303342, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 63.65214469, 0.00081144, 77.14357538, 0.01281143, 7.71435754, 0.06615042, -63.65214469, -0.00081144, -77.14357538, -0.01281143, -7.71435754, -0.06615042, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 94.26897075, 0.02166208, 94.26897075, 0.06498623, 65.98827952, -1315.75701963, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 23.56724269, 7.528e-05, 70.70172806, 0.00022583, 235.67242687, 0.00075277, -23.56724269, -7.528e-05, -70.70172806, -0.00022583, -235.67242687, -0.00075277, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 109.63671486, 0.01622881, 109.63671486, 0.04868642, 76.7457004, -2002.99740084, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 27.40917871, 8.755e-05, 82.22753614, 0.00026265, 274.09178714, 0.00087549, -27.40917871, -8.755e-05, -82.22753614, -0.00026265, -274.09178714, -0.00087549, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 17.4, 9.5, 9.55)
    ops.node(124020, 17.4, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 29338774.27776011, 12224489.28240005, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 30.1493526, 0.00106306, 36.50175125, 0.01282703, 3.65017513, 0.06663729, -30.1493526, -0.00106306, -36.50175125, -0.01282703, -3.65017513, -0.06663729, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 30.1493526, 0.00106306, 36.50175125, 0.01282703, 3.65017513, 0.06663729, -30.1493526, -0.00106306, -36.50175125, -0.01282703, -3.65017513, -0.06663729, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 79.23746104, 0.02126114, 79.23746104, 0.06378341, 55.46622273, -1418.0104022, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 19.80936526, 8.712e-05, 59.42809578, 0.00026135, 198.0936526, 0.00087116, -19.80936526, -8.712e-05, -59.42809578, -0.00026135, -198.0936526, -0.00087116, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 79.23746104, 0.02126114, 79.23746104, 0.06378341, 55.46622273, -1418.0104022, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 19.80936526, 8.712e-05, 59.42809578, 0.00026135, 198.0936526, 0.00087116, -19.80936526, -8.712e-05, -59.42809578, -0.00026135, -198.0936526, -0.00087116, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 20.2, 9.5, 9.55)
    ops.node(124021, 20.2, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 28975582.9105846, 12073159.54607692, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 30.61002095, 0.00101876, 37.08508809, 0.01131486, 3.70850881, 0.06462919, -30.61002095, -0.00101876, -37.08508809, -0.01131486, -3.70850881, -0.06462919, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 30.61002095, 0.00101876, 37.08508809, 0.01131486, 3.70850881, 0.06462919, -30.61002095, -0.00101876, -37.08508809, -0.01131486, -3.70850881, -0.06462919, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 65.55746951, 0.02037523, 65.55746951, 0.06112568, 45.89022865, -1182.72393256, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 16.38936738, 7.298e-05, 49.16810213, 0.00021894, 163.89367376, 0.00072979, -16.38936738, -7.298e-05, -49.16810213, -0.00021894, -163.89367376, -0.00072979, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 65.55746951, 0.02037523, 65.55746951, 0.06112568, 45.89022865, -1182.72393256, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 16.38936738, 7.298e-05, 49.16810213, 0.00021894, 163.89367376, 0.00072979, -16.38936738, -7.298e-05, -49.16810213, -0.00021894, -163.89367376, -0.00072979, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 26.0, 9.5, 9.55)
    ops.node(124022, 26.0, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0875, 28684934.03595847, 11952055.84831603, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 41.54981251, 0.00101617, 50.37157155, 0.01025091, 5.03715716, 0.05125689, -41.54981251, -0.00101617, -50.37157155, -0.01025091, -5.03715716, -0.05125689, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 65.64636427, 0.00078086, 79.58424683, 0.01107879, 7.95842468, 0.06418045, -65.64636427, -0.00078086, -79.58424683, -0.01107879, -7.95842468, -0.06418045, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 80.63873625, 0.02032349, 80.63873625, 0.06097048, 56.44711538, -1129.63902184, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 20.15968406, 6.477e-05, 60.47905219, 0.00019431, 201.59684063, 0.0006477, -20.15968406, -6.477e-05, -60.47905219, -0.00019431, -201.59684063, -0.0006477, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 102.44699897, 0.01561721, 102.44699897, 0.04685164, 71.71289928, -1683.15662781, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 25.61174974, 8.229e-05, 76.83524923, 0.00024686, 256.11749742, 0.00082286, -25.61174974, -8.229e-05, -76.83524923, -0.00024686, -256.11749742, -0.00082286, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 31.8, 9.5, 9.55)
    ops.node(124023, 31.8, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.0875, 29578212.84340128, 12324255.3514172, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 42.32649083, 0.00095006, 51.22584553, 0.01281418, 5.12258455, 0.05475366, -42.32649083, -0.00095006, -51.22584553, -0.01281418, -5.12258455, -0.05475366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 66.99046807, 0.00074588, 81.07554636, 0.01397592, 8.10755464, 0.06828643, -66.99046807, -0.00074588, -81.07554636, -0.01397592, -8.10755464, -0.06828643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 98.74088825, 0.01900121, 98.74088825, 0.05700364, 69.11862177, -1421.0209332, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 24.68522206, 7.691e-05, 74.05566618, 0.00023074, 246.85222062, 0.00076914, -24.68522206, -7.691e-05, -74.05566618, -0.00023074, -246.85222062, -0.00076914, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 115.1400222, 0.01491765, 115.1400222, 0.04475295, 80.59801554, -2185.29618041, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 28.78500555, 8.969e-05, 86.35501665, 0.00026907, 287.8500555, 0.00089689, -28.78500555, -8.969e-05, -86.35501665, -0.00026907, -287.8500555, -0.00089689, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 37.6, 9.5, 9.55)
    ops.node(124024, 37.6, 9.5, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 32946150.86175956, 13727562.85906648, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 38.2533541, 0.00105415, 45.94856204, 0.01355153, 4.5948562, 0.07365894, -38.2533541, -0.00105415, -45.94856204, -0.01355153, -4.5948562, -0.07365894, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 35.03067939, 0.00105415, 42.07760033, 0.01355153, 4.20776003, 0.07365894, -35.03067939, -0.00105415, -42.07760033, -0.01355153, -4.20776003, -0.07365894, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 85.20877719, 0.02108302, 85.20877719, 0.06324905, 59.64614403, -1686.10625936, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 21.3021943, 8.342e-05, 63.90658289, 0.00025027, 213.02194298, 0.00083424, -21.3021943, -8.342e-05, -63.90658289, -0.00025027, -213.02194298, -0.00083424, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 85.20877719, 0.02108302, 85.20877719, 0.06324905, 59.64614403, -1686.10625936, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 21.3021943, 8.342e-05, 63.90658289, 0.00025027, 213.02194298, 0.00083424, -21.3021943, -8.342e-05, -63.90658289, -0.00025027, -213.02194298, -0.00083424, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 17.4, 0.0, 0.0)
    ops.node(124025, 17.4, 0.0, 1.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 170004, 124025, 0.1225, 27293166.79645327, 11372152.83185553, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 195.92936131, 0.00073769, 232.70427528, 0.00963068, 23.27042753, 0.02722265, -195.92936131, -0.00073769, -232.70427528, -0.00963068, -23.27042753, -0.02722265, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 181.95359879, 0.00073769, 216.10533541, 0.00963068, 21.61053354, 0.02722265, -181.95359879, -0.00073769, -216.10533541, -0.00963068, -21.61053354, -0.02722265, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 174.97047007, 0.01475379, 174.97047007, 0.04426137, 122.47932905, -3140.37618915, 0.05, 2, 0, 70004, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 43.74261752, 6.877e-05, 131.22785256, 0.0002063, 437.42617519, 0.00068765, -43.74261752, -6.877e-05, -131.22785256, -0.0002063, -437.42617519, -0.00068765, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 174.97047007, 0.01475379, 174.97047007, 0.04426137, 122.47932905, -3140.37618915, 0.05, 2, 0, 70004, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 43.74261752, 6.877e-05, 131.22785256, 0.0002063, 437.42617519, 0.00068765, -43.74261752, -6.877e-05, -131.22785256, -0.0002063, -437.42617519, -0.00068765, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 17.4, 0.0, 2.075)
    ops.node(121004, 17.4, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 174025, 121004, 0.1225, 28507066.29469013, 11877944.28945422, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 167.05932339, 0.00071292, 199.02895853, 0.00951382, 19.90289585, 0.03061866, -167.05932339, -0.00071292, -199.02895853, -0.00951382, -19.90289585, -0.03061866, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 153.957774, 0.00071292, 183.42020544, 0.00951382, 18.34202054, 0.03061866, -153.957774, -0.00071292, -183.42020544, -0.00951382, -18.34202054, -0.03061866, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 176.2614203, 0.01425844, 176.2614203, 0.04277532, 123.38299421, -2983.98403301, 0.05, 2, 0, 74025, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 44.06535507, 6.632e-05, 132.19606522, 0.00019897, 440.65355075, 0.00066323, -44.06535507, -6.632e-05, -132.19606522, -0.00019897, -440.65355075, -0.00066323, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 176.2614203, 0.01425844, 176.2614203, 0.04277532, 123.38299421, -2983.98403301, 0.05, 2, 0, 74025, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 44.06535507, 6.632e-05, 132.19606522, 0.00019897, 440.65355075, 0.00066323, -44.06535507, -6.632e-05, -132.19606522, -0.00019897, -440.65355075, -0.00066323, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 20.2, 0.0, 0.0)
    ops.node(124026, 20.2, 0.0, 1.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 170005, 124026, 0.1225, 26457465.97396301, 11023944.15581792, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 195.65244731, 0.00076121, 232.01181153, 0.00750844, 23.20118115, 0.02337116, -195.65244731, -0.00076121, -232.01181153, -0.00750844, -23.20118115, -0.02337116, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 182.02413707, 0.00076121, 215.85086394, 0.00750844, 21.58508639, 0.02337116, -182.02413707, -0.00076121, -215.85086394, -0.00750844, -21.58508639, -0.02337116, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 161.74411614, 0.01522425, 161.74411614, 0.04567275, 113.2208813, -2832.51501473, 0.05, 2, 0, 70005, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 40.43602903, 6.558e-05, 121.3080871, 0.00019673, 404.36029035, 0.00065575, -40.43602903, -6.558e-05, -121.3080871, -0.00019673, -404.36029035, -0.00065575, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 161.74411614, 0.01522425, 161.74411614, 0.04567275, 113.2208813, -2832.51501473, 0.05, 2, 0, 70005, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 40.43602903, 6.558e-05, 121.3080871, 0.00019673, 404.36029035, 0.00065575, -40.43602903, -6.558e-05, -121.3080871, -0.00019673, -404.36029035, -0.00065575, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 20.2, 0.0, 2.075)
    ops.node(121005, 20.2, 0.0, 3.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 174026, 121005, 0.1225, 30497822.19991756, 12707425.91663232, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 169.47604731, 0.00070132, 201.81290988, 0.00936109, 20.18129099, 0.03398454, -169.47604731, -0.00070132, -201.81290988, -0.00936109, -20.18129099, -0.03398454, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 156.03506269, 0.00070132, 185.80731935, 0.00936109, 18.58073194, 0.03398454, -156.03506269, -0.00070132, -185.80731935, -0.00936109, -18.58073194, -0.03398454, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 183.03713386, 0.01402634, 183.03713386, 0.04207903, 128.1259937, -2868.7602766, 0.05, 2, 0, 74026, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 45.75928346, 6.438e-05, 137.27785039, 0.00019313, 457.59283465, 0.00064377, -45.75928346, -6.438e-05, -137.27785039, -0.00019313, -457.59283465, -0.00064377, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 183.03713386, 0.01402634, 183.03713386, 0.04207903, 128.1259937, -2868.7602766, 0.05, 2, 0, 74026, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 45.75928346, 6.438e-05, 137.27785039, 0.00019313, 457.59283465, 0.00064377, -45.75928346, -6.438e-05, -137.27785039, -0.00019313, -457.59283465, -0.00064377, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 17.4, 0.0, 3.95)
    ops.node(124027, 17.4, 0.0, 4.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4067, 171004, 124027, 0.1225, 30074904.86349335, 12531210.3597889, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24067, 130.73037556, 0.00063816, 156.45533873, 0.01101458, 15.64553387, 0.03853387, -130.73037556, -0.00063816, -156.45533873, -0.01101458, -15.64553387, -0.03853387, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14067, 136.84887369, 0.00063816, 163.77782744, 0.01101458, 16.37778274, 0.03853387, -136.84887369, -0.00063816, -163.77782744, -0.01101458, -16.37778274, -0.03853387, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24067, 4067, 0.0, 215.77511864, 0.01276325, 215.77511864, 0.03828974, 151.04258305, -3684.80107959, 0.05, 2, 0, 71004, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44067, 53.94377966, 5.904e-05, 161.83133898, 0.00017711, 539.4377966, 0.00059037, -53.94377966, -5.904e-05, -161.83133898, -0.00017711, -539.4377966, -0.00059037, 0.4, 0.3, 0.003, 0.0, 0.0, 24067, 2)
    ops.limitCurve('ThreePoint', 14067, 4067, 0.0, 215.77511864, 0.01276325, 215.77511864, 0.03828974, 151.04258305, -3684.80107959, 0.05, 2, 0, 71004, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34067, 53.94377966, 5.904e-05, 161.83133898, 0.00017711, 539.4377966, 0.00059037, -53.94377966, -5.904e-05, -161.83133898, -0.00017711, -539.4377966, -0.00059037, 0.4, 0.3, 0.003, 0.0, 0.0, 14067, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4067, 99999, 'P', 44067, 'Vy', 34067, 'Vz', 24067, 'My', 14067, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4067, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4067, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 17.4, 0.0, 5.25)
    ops.node(122004, 17.4, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 174027, 122004, 0.1225, 27992140.07958784, 11663391.69982827, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 130.94349839, 0.00063399, 157.17343331, 0.00977617, 15.71734333, 0.0351379, -130.94349839, -0.00063399, -157.17343331, -0.00977617, -15.71734333, -0.0351379, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 124.73204453, 0.00063399, 149.71773263, 0.00977617, 14.97177326, 0.0351379, -124.73204453, -0.00063399, -149.71773263, -0.00977617, -14.97177326, -0.0351379, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 190.87557218, 0.01267973, 190.87557218, 0.03803918, 133.61290052, -3204.46163099, 0.05, 2, 0, 74027, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 47.71889304, 5.611e-05, 143.15667913, 0.00016833, 477.18893044, 0.0005611, -47.71889304, -5.611e-05, -143.15667913, -0.00016833, -477.18893044, -0.0005611, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 190.87557218, 0.01267973, 190.87557218, 0.03803918, 133.61290052, -3204.46163099, 0.05, 2, 0, 74027, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 47.71889304, 5.611e-05, 143.15667913, 0.00016833, 477.18893044, 0.0005611, -47.71889304, -5.611e-05, -143.15667913, -0.00016833, -477.18893044, -0.0005611, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 20.2, 0.0, 3.95)
    ops.node(124028, 20.2, 0.0, 4.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 171005, 124028, 0.1225, 28983819.67279368, 12076591.5303307, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 129.69917672, 0.00063011, 155.36110307, 0.00884349, 15.53611031, 0.03461731, -129.69917672, -0.00063011, -155.36110307, -0.00884349, -15.53611031, -0.03461731, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 135.95000255, 0.00063011, 162.8487003, 0.00884349, 16.28487003, 0.03461731, -135.95000255, -0.00063011, -162.8487003, -0.00884349, -16.28487003, -0.03461731, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 199.99083652, 0.01260215, 199.99083652, 0.03780645, 139.99358556, -3253.01146021, 0.05, 2, 0, 71005, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 49.99770913, 5.678e-05, 149.99312739, 0.00017033, 499.9770913, 0.00056778, -49.99770913, -5.678e-05, -149.99312739, -0.00017033, -499.9770913, -0.00056778, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 199.99083652, 0.01260215, 199.99083652, 0.03780645, 139.99358556, -3253.01146021, 0.05, 2, 0, 71005, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 49.99770913, 5.678e-05, 149.99312739, 0.00017033, 499.9770913, 0.00056778, -49.99770913, -5.678e-05, -149.99312739, -0.00017033, -499.9770913, -0.00056778, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 20.2, 0.0, 5.25)
    ops.node(122005, 20.2, 0.0, 6.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 174028, 122005, 0.1225, 30008327.53956894, 12503469.80815372, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 132.1059528, 0.00065371, 158.33808626, 0.00886029, 15.83380863, 0.03746511, -132.1059528, -0.00065371, -158.33808626, -0.00886029, -15.83380863, -0.03746511, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 126.28122911, 0.00065371, 151.35675361, 0.00886029, 15.13567536, 0.03746511, -126.28122911, -0.00065371, -151.35675361, -0.00886029, -15.13567536, -0.03746511, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 201.19775428, 0.01307414, 201.19775428, 0.03922241, 140.838428, -3094.19324761, 0.05, 2, 0, 74028, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 50.29943857, 5.517e-05, 150.89831571, 0.00016551, 502.99438571, 0.0005517, -50.29943857, -5.517e-05, -150.89831571, -0.00016551, -502.99438571, -0.0005517, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 201.19775428, 0.01307414, 201.19775428, 0.03922241, 140.838428, -3094.19324761, 0.05, 2, 0, 74028, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 50.29943857, 5.517e-05, 150.89831571, 0.00016551, 502.99438571, 0.0005517, -50.29943857, -5.517e-05, -150.89831571, -0.00016551, -502.99438571, -0.0005517, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 17.4, 0.0, 6.75)
    ops.node(124029, 17.4, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4072, 172004, 124029, 0.0625, 30094446.48642823, 12539352.70267843, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24072, 65.44626381, 0.0008169, 77.98209414, 0.00944183, 7.79820941, 0.04038933, -65.44626381, -0.0008169, -77.98209414, -0.00944183, -7.79820941, -0.04038933, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14072, 65.44626381, 0.0008169, 77.98209414, 0.00944183, 7.79820941, 0.04038933, -65.44626381, -0.0008169, -77.98209414, -0.00944183, -7.79820941, -0.04038933, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24072, 4072, 0.0, 70.21196406, 0.01633793, 70.21196406, 0.04901379, 49.14837484, -2179.35574346, 0.05, 2, 0, 72004, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44072, 17.55299102, 3.763e-05, 52.65897305, 0.00011288, 175.52991016, 0.00037627, -17.55299102, -3.763e-05, -52.65897305, -0.00011288, -175.52991016, -0.00037627, 0.4, 0.3, 0.003, 0.0, 0.0, 24072, 2)
    ops.limitCurve('ThreePoint', 14072, 4072, 0.0, 70.21196406, 0.01633793, 70.21196406, 0.04901379, 49.14837484, -2179.35574346, 0.05, 2, 0, 72004, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34072, 17.55299102, 3.763e-05, 52.65897305, 0.00011288, 175.52991016, 0.00037627, -17.55299102, -3.763e-05, -52.65897305, -0.00011288, -175.52991016, -0.00037627, 0.4, 0.3, 0.003, 0.0, 0.0, 14072, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4072, 99999, 'P', 44072, 'Vy', 34072, 'Vz', 24072, 'My', 14072, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4072, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4072, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 17.4, 0.0, 8.025)
    ops.node(123004, 17.4, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 174029, 123004, 0.0625, 27721636.42604771, 11550681.84418655, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 63.01283475, 0.00077717, 75.36025584, 0.0097454, 7.53602558, 0.03827759, -63.01283475, -0.00077717, -75.36025584, -0.0097454, -7.53602558, -0.03827759, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 63.01283475, 0.00077717, 75.36025584, 0.0097454, 7.53602558, 0.03827759, -63.01283475, -0.00077717, -75.36025584, -0.0097454, -7.53602558, -0.03827759, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 66.18698449, 0.0155434, 66.18698449, 0.04663021, 46.33088914, -2188.53316966, 0.05, 2, 0, 74029, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 16.54674612, 3.851e-05, 49.64023837, 0.00011552, 165.46746122, 0.00038507, -16.54674612, -3.851e-05, -49.64023837, -0.00011552, -165.46746122, -0.00038507, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 66.18698449, 0.0155434, 66.18698449, 0.04663021, 46.33088914, -2188.53316966, 0.05, 2, 0, 74029, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 16.54674612, 3.851e-05, 49.64023837, 0.00011552, 165.46746122, 0.00038507, -16.54674612, -3.851e-05, -49.64023837, -0.00011552, -165.46746122, -0.00038507, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 20.2, 0.0, 6.75)
    ops.node(124030, 20.2, 0.0, 7.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 172005, 124030, 0.0625, 31511334.20911921, 13129722.58713301, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 65.33078224, 0.00084267, 77.73230094, 0.01118616, 7.77323009, 0.04502798, -65.33078224, -0.00084267, -77.73230094, -0.01118616, -7.77323009, -0.04502798, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 65.33078224, 0.00084267, 77.73230094, 0.01118616, 7.77323009, 0.04502798, -65.33078224, -0.00084267, -77.73230094, -0.01118616, -7.77323009, -0.04502798, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 94.96648616, 0.0168533, 94.96648616, 0.05055991, 66.47654031, -2475.88413766, 0.05, 2, 0, 72005, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 23.74162154, 4.861e-05, 71.22486462, 0.00014582, 237.41621541, 0.00048605, -23.74162154, -4.861e-05, -71.22486462, -0.00014582, -237.41621541, -0.00048605, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 94.96648616, 0.0168533, 94.96648616, 0.05055991, 66.47654031, -2475.88413766, 0.05, 2, 0, 72005, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 23.74162154, 4.861e-05, 71.22486462, 0.00014582, 237.41621541, 0.00048605, -23.74162154, -4.861e-05, -71.22486462, -0.00014582, -237.41621541, -0.00048605, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 20.2, 0.0, 8.025)
    ops.node(123005, 20.2, 0.0, 8.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 174030, 123005, 0.0625, 30731220.86119926, 12804675.35883303, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 61.54759701, 0.00069794, 73.50281033, 0.01030424, 7.35028103, 0.0453795, -61.54759701, -0.00069794, -73.50281033, -0.01030424, -7.35028103, -0.0453795, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 61.54759701, 0.00069794, 73.50281033, 0.01030424, 7.35028103, 0.0453795, -61.54759701, -0.00069794, -73.50281033, -0.01030424, -7.35028103, -0.0453795, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 69.31447213, 0.01395874, 69.31447213, 0.04187621, 48.52013049, -2179.1254764, 0.05, 2, 0, 74030, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 17.32861803, 3.638e-05, 51.9858541, 0.00010913, 173.28618033, 0.00036377, -17.32861803, -3.638e-05, -51.9858541, -0.00010913, -173.28618033, -0.00036377, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 69.31447213, 0.01395874, 69.31447213, 0.04187621, 48.52013049, -2179.1254764, 0.05, 2, 0, 74030, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 17.32861803, 3.638e-05, 51.9858541, 0.00010913, 173.28618033, 0.00036377, -17.32861803, -3.638e-05, -51.9858541, -0.00010913, -173.28618033, -0.00036377, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 17.4, 0.0, 9.55)
    ops.node(124031, 17.4, 0.0, 10.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4077, 173004, 124031, 0.0625, 27464014.03053401, 11443339.17938917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24077, 48.06538959, 0.00072698, 58.25828272, 0.0132818, 5.82582827, 0.05501643, -48.06538959, -0.00072698, -58.25828272, -0.0132818, -5.82582827, -0.05501643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14077, 48.06538959, 0.00072698, 58.25828272, 0.0132818, 5.82582827, 0.05501643, -48.06538959, -0.00072698, -58.25828272, -0.0132818, -5.82582827, -0.05501643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24077, 4077, 0.0, 68.97971482, 0.0145396, 68.97971482, 0.04361881, 48.28580038, -2263.56887544, 0.05, 2, 0, 73004, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44077, 17.24492871, 4.051e-05, 51.73478612, 0.00012152, 172.44928705, 0.00040508, -17.24492871, -4.051e-05, -51.73478612, -0.00012152, -172.44928705, -0.00040508, 0.4, 0.3, 0.003, 0.0, 0.0, 24077, 2)
    ops.limitCurve('ThreePoint', 14077, 4077, 0.0, 68.97971482, 0.0145396, 68.97971482, 0.04361881, 48.28580038, -2263.56887544, 0.05, 2, 0, 73004, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34077, 17.24492871, 4.051e-05, 51.73478612, 0.00012152, 172.44928705, 0.00040508, -17.24492871, -4.051e-05, -51.73478612, -0.00012152, -172.44928705, -0.00040508, 0.4, 0.3, 0.003, 0.0, 0.0, 14077, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4077, 99999, 'P', 44077, 'Vy', 34077, 'Vz', 24077, 'My', 14077, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4077, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4077, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 17.4, 0.0, 10.825)
    ops.node(124004, 17.4, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 174031, 124004, 0.0625, 31394325.75117134, 13080969.06298806, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 46.06516292, 0.00071452, 55.58142361, 0.01163993, 5.55814236, 0.06239879, -46.06516292, -0.00071452, -55.58142361, -0.01163993, -5.55814236, -0.06239879, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 46.06516292, 0.00071452, 55.58142361, 0.01163993, 5.55814236, 0.06239879, -46.06516292, -0.00071452, -55.58142361, -0.01163993, -5.55814236, -0.06239879, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 54.88895048, 0.01429041, 54.88895048, 0.04287123, 38.42226534, -2019.90820955, 0.05, 2, 0, 74031, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 13.72223762, 2.82e-05, 41.16671286, 8.459e-05, 137.2223762, 0.00028198, -13.72223762, -2.82e-05, -41.16671286, -8.459e-05, -137.2223762, -0.00028198, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 54.88895048, 0.01429041, 54.88895048, 0.04287123, 38.42226534, -2019.90820955, 0.05, 2, 0, 74031, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 13.72223762, 2.82e-05, 41.16671286, 8.459e-05, 137.2223762, 0.00028198, -13.72223762, -2.82e-05, -41.16671286, -8.459e-05, -137.2223762, -0.00028198, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 20.2, 0.0, 9.55)
    ops.node(124032, 20.2, 0.0, 10.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 173005, 124032, 0.0625, 30556854.34638626, 12732022.64432761, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 47.08716213, 0.00071044, 56.78069178, 0.01423029, 5.67806918, 0.06029501, -47.08716213, -0.00071044, -56.78069178, -0.01423029, -5.67806918, -0.06029501, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 47.08716213, 0.00071044, 56.78069178, 0.01423029, 5.67806918, 0.06029501, -47.08716213, -0.00071044, -56.78069178, -0.01423029, -5.67806918, -0.06029501, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 84.75734352, 0.01420877, 84.75734352, 0.04262631, 59.33014046, -2389.36671039, 0.05, 2, 0, 73005, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 21.18933588, 4.474e-05, 63.56800764, 0.00013421, 211.89335879, 0.00044735, -21.18933588, -4.474e-05, -63.56800764, -0.00013421, -211.89335879, -0.00044735, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 84.75734352, 0.01420877, 84.75734352, 0.04262631, 59.33014046, -2389.36671039, 0.05, 2, 0, 73005, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 21.18933588, 4.474e-05, 63.56800764, 0.00013421, 211.89335879, 0.00044735, -21.18933588, -4.474e-05, -63.56800764, -0.00013421, -211.89335879, -0.00044735, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 20.2, 0.0, 10.825)
    ops.node(124005, 20.2, 0.0, 11.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 174032, 124005, 0.0625, 30862593.77642816, 12859414.07351173, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 43.88796304, 0.00069064, 53.03099157, 0.0146583, 5.30309916, 0.06502006, -43.88796304, -0.00069064, -53.03099157, -0.0146583, -5.30309916, -0.06502006, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 43.88796304, 0.00069064, 53.03099157, 0.0146583, 5.30309916, 0.06502006, -43.88796304, -0.00069064, -53.03099157, -0.0146583, -5.30309916, -0.06502006, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 82.23157843, 0.01381273, 82.23157843, 0.0414382, 57.5621049, -2885.79422827, 0.05, 2, 0, 74032, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 20.55789461, 4.297e-05, 61.67368382, 0.00012892, 205.57894608, 0.00042972, -20.55789461, -4.297e-05, -61.67368382, -0.00012892, -205.57894608, -0.00042972, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 82.23157843, 0.01381273, 82.23157843, 0.0414382, 57.5621049, -2885.79422827, 0.05, 2, 0, 74032, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 20.55789461, 4.297e-05, 61.67368382, 0.00012892, 205.57894608, 0.00042972, -20.55789461, -4.297e-05, -61.67368382, -0.00012892, -205.57894608, -0.00042972, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 4080, '-orient', 0, 0, 1, 0, 1, 0)
