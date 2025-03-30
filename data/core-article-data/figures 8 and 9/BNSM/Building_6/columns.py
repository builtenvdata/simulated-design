import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.105, 24563224.2069678, 10234676.75290325, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 129.03320035, 0.00099304, 152.57395484, 0.00797659, 15.25739548, 0.02096942, -129.03320035, -0.00099304, -152.57395484, -0.00797659, -15.25739548, -0.02096942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 138.91207101, 0.00088267, 164.25512186, 0.00819756, 16.42551219, 0.02270057, -138.91207101, -0.00088267, -164.25512186, -0.00819756, -16.42551219, -0.02270057, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 114.91127126, 0.01986086, 114.91127126, 0.05958257, 80.43788988, -1647.85808792, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 28.72781782, 8.822e-05, 86.18345345, 0.00026465, 287.27817815, 0.00088217, -28.72781782, -8.822e-05, -86.18345345, -0.00026465, -287.27817815, -0.00088217, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 121.21071659, 0.01765341, 121.21071659, 0.05296022, 84.84750161, -1795.97411414, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 30.30267915, 9.305e-05, 90.90803744, 0.00027916, 303.02679147, 0.00093053, -30.30267915, -9.305e-05, -90.90803744, -0.00027916, -303.02679147, -0.00093053, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.85, 0.0, 0.0)
    ops.node(121004, 12.85, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.105, 27810128.47716095, 11587553.5321504, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 130.59119871, 0.0009984, 155.53738381, 0.0086773, 15.55373838, 0.02852597, -130.59119871, -0.0009984, -155.53738381, -0.0086773, -15.55373838, -0.02852597, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 141.35962324, 0.00088579, 168.36284674, 0.00892903, 16.83628467, 0.03108474, -141.35962324, -0.00088579, -168.36284674, -0.00892903, -16.83628467, -0.03108474, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 118.70757293, 0.01996798, 118.70757293, 0.05990395, 83.09530105, -1572.00241911, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 29.67689323, 8.049e-05, 89.0306797, 0.00024148, 296.76893232, 0.00080492, -29.67689323, -8.049e-05, -89.0306797, -0.00024148, -296.76893232, -0.00080492, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 128.31633538, 0.01771579, 128.31633538, 0.05314738, 89.82143477, -1703.7120326, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 32.07908385, 8.701e-05, 96.23725154, 0.00026102, 320.79083846, 0.00087007, -32.07908385, -8.701e-05, -96.23725154, -0.00026102, -320.79083846, -0.00087007, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.65, 0.0)
    ops.node(121005, 0.0, 4.65, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.21, 27334274.68746622, 11389281.11977759, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 410.32796032, 0.00065504, 490.78695741, 0.00874333, 49.07869574, 0.03050551, -410.32796032, -0.00065504, -490.78695741, -0.00874333, -49.07869574, -0.03050551, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 278.29609703, 0.00089804, 332.86567802, 0.00790163, 33.2865678, 0.02336704, -278.29609703, -0.00089804, -332.86567802, -0.00790163, -33.2865678, -0.02336704, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 299.14498456, 0.01310072, 299.14498456, 0.03930217, 209.40148919, -2956.11385981, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 74.78624614, 0.00010319, 224.35873842, 0.00030956, 747.86246139, 0.00103186, -74.78624614, -0.00010319, -224.35873842, -0.00030956, -747.86246139, -0.00103186, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 204.72368781, 0.01796076, 204.72368781, 0.05388228, 143.30658147, -2289.1296499, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 51.18092195, 7.062e-05, 153.54276586, 0.00021185, 511.80921953, 0.00070617, -51.18092195, -7.062e-05, -153.54276586, -0.00021185, -511.80921953, -0.00070617, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 4.95, 4.65, 0.0)
    ops.node(121006, 4.95, 4.65, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.36, 27271838.44193284, 11363266.01747202, 0.01576053, 0.0066825, 0.02112, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 925.73720076, 0.00058952, 1116.26028819, 0.00959121, 111.62602882, 0.02919113, -925.73720076, -0.00058952, -1116.26028819, -0.00959121, -111.62602882, -0.02919113, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 684.8394664, 0.00074289, 825.78414208, 0.00872616, 82.57841421, 0.02346844, -684.8394664, -0.00074289, -825.78414208, -0.00872616, -82.57841421, -0.02346844, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 538.85583035, 0.01179033, 538.85583035, 0.03537099, 377.19908125, -3333.92089998, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 134.71395759, 0.00010867, 404.14187276, 0.00032602, 1347.13957588, 0.00108673, -134.71395759, -0.00010867, -404.14187276, -0.00032602, -1347.13957588, -0.00108673, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 303.10640457, 0.01485778, 303.10640457, 0.04457335, 212.1744832, -2566.47416394, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 75.77660114, 6.113e-05, 227.32980343, 0.00018339, 757.76601143, 0.00061128, -75.77660114, -6.113e-05, -227.32980343, -0.00018339, -757.76601143, -0.00061128, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 7.9, 4.65, 0.0)
    ops.node(121007, 7.9, 4.65, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.36, 26885105.66811134, 11202127.36171306, 0.01576053, 0.0066825, 0.02112, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 926.25545163, 0.00058836, 1116.9781092, 0.00979981, 111.69781092, 0.02892984, -926.25545163, -0.00058836, -1116.9781092, -0.00979981, -111.69781092, -0.02892984, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 690.39473043, 0.00073828, 832.55196958, 0.00890757, 83.25519696, 0.02329642, -690.39473043, -0.00073828, -832.55196958, -0.00890757, -83.25519696, -0.02329642, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 534.72293331, 0.01176716, 534.72293331, 0.03530147, 374.30605332, -3419.98908542, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 133.68073333, 0.00010939, 401.04219999, 0.00032817, 1336.80733328, 0.00109391, -133.68073333, -0.00010939, -401.04219999, -0.00032817, -1336.80733328, -0.00109391, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 300.78164999, 0.01476562, 300.78164999, 0.04429686, 210.54715499, -2608.85423418, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 75.1954125, 6.153e-05, 225.58623749, 0.0001846, 751.95412497, 0.00061532, -75.1954125, -6.153e-05, -225.58623749, -0.0001846, -751.95412497, -0.00061532, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 12.85, 4.65, 0.0)
    ops.node(121008, 12.85, 4.65, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.21, 26269377.68789311, 10945574.03662213, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 407.75871537, 0.0006458, 487.18857528, 0.00870122, 48.71885753, 0.02831301, -407.75871537, -0.0006458, -487.18857528, -0.00870122, -48.71885753, -0.02831301, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 280.64892982, 0.00087252, 335.31828289, 0.00784765, 33.53182829, 0.02178487, -280.64892982, -0.00087252, -335.31828289, -0.00784765, -33.53182829, -0.02178487, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 289.19515028, 0.01291602, 289.19515028, 0.03874807, 202.4366052, -2953.51862385, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 72.29878757, 0.0001038, 216.89636271, 0.00031139, 722.9878757, 0.00103798, -72.29878757, -0.0001038, -216.89636271, -0.00031139, -722.9878757, -0.00103798, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 197.61264808, 0.01745036, 197.61264808, 0.05235109, 138.32885365, -2287.79735488, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 49.40316202, 7.093e-05, 148.20948606, 0.00021278, 494.03162019, 0.00070927, -49.40316202, -7.093e-05, -148.20948606, -0.00021278, -494.03162019, -0.00070927, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 9.3, 0.0)
    ops.node(121009, 0.0, 9.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.21, 28110010.77032863, 11712504.48763693, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 415.93529585, 0.00066251, 497.78425846, 0.00977633, 49.77842585, 0.03321175, -415.93529585, -0.00066251, -497.78425846, -0.00977633, -49.77842585, -0.03321175, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 282.42624189, 0.00090974, 338.00290284, 0.00880133, 33.80029028, 0.02545583, -282.42624189, -0.00090974, -338.00290284, -0.00880133, -33.80029028, -0.02545583, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 310.16848996, 0.01325017, 310.16848996, 0.03975052, 217.11794297, -3054.28149071, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 77.54212249, 0.00010404, 232.62636747, 0.00031211, 775.42122491, 0.00104036, -77.54212249, -0.00010404, -232.62636747, -0.00031211, -775.42122491, -0.00104036, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 211.98831254, 0.01819473, 211.98831254, 0.05458418, 148.39181878, -2329.27812531, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 52.99707814, 7.11e-05, 158.99123441, 0.00021331, 529.97078135, 0.00071104, -52.99707814, -7.11e-05, -158.99123441, -0.00021331, -529.97078135, -0.00071104, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 4.95, 9.3, 0.0)
    ops.node(121010, 4.95, 9.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.3, 26746085.64158459, 11144202.35066025, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 752.90784634, 0.00059818, 905.68206965, 0.01130644, 90.56820697, 0.03391397, -752.90784634, -0.00059818, -905.68206965, -0.01130644, -90.56820697, -0.03391397, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 541.08193706, 0.00080107, 650.87408904, 0.009959, 65.0874089, 0.02555942, -541.08193706, -0.00080107, -650.87408904, -0.009959, -65.0874089, -0.02555942, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 471.31428377, 0.01196358, 471.31428377, 0.03589073, 329.91999864, -3948.68197962, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 117.82857094, 0.0001163, 353.48571283, 0.00034891, 1178.28570942, 0.00116304, -117.82857094, -0.0001163, -353.48571283, -0.00034891, -1178.28570942, -0.00116304, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 265.79556038, 0.01602146, 265.79556038, 0.04806438, 186.05689227, -2747.61672739, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 66.44889009, 6.559e-05, 199.34667028, 0.00019677, 664.48890095, 0.00065589, -66.44889009, -6.559e-05, -199.34667028, -0.00019677, -664.48890095, -0.00065589, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.9, 9.3, 0.0)
    ops.node(121011, 7.9, 9.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.3, 26590806.84649917, 11079502.85270799, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 762.02131023, 0.00059469, 916.5985478, 0.01012604, 91.65985478, 0.03246689, -762.02131023, -0.00059469, -916.5985478, -0.01012604, -91.65985478, -0.03246689, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 562.09730568, 0.00078311, 676.11964022, 0.00893452, 67.61196402, 0.02435092, -562.09730568, -0.00078311, -676.11964022, -0.00893452, -67.61196402, -0.02435092, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 456.34146536, 0.01189372, 456.34146536, 0.03568117, 319.43902575, -3626.73460465, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 114.08536634, 0.00011327, 342.25609902, 0.0003398, 1140.85366339, 0.00113267, -114.08536634, -0.00011327, -342.25609902, -0.0003398, -1140.85366339, -0.00113267, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 257.71275336, 0.01566221, 257.71275336, 0.04698662, 180.39892735, -2603.28806745, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 64.42818834, 6.397e-05, 193.28456502, 0.0001919, 644.28188341, 0.00063966, -64.42818834, -6.397e-05, -193.28456502, -0.0001919, -644.28188341, -0.00063966, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 12.85, 9.3, 0.0)
    ops.node(121012, 12.85, 9.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.21, 28118265.11555659, 11715943.79814858, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 409.19503527, 0.00065553, 489.71800806, 0.01064309, 48.97180081, 0.03409366, -409.19503527, -0.00065553, -489.71800806, -0.01064309, -48.97180081, -0.03409366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 276.26187435, 0.00090208, 330.62574847, 0.00955023, 33.06257485, 0.0262155, -276.26187435, -0.00090208, -330.62574847, -0.00955023, -33.06257485, -0.0262155, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 320.06339674, 0.01311069, 320.06339674, 0.03933207, 224.04437772, -3297.88699712, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 80.01584918, 0.00010732, 240.04754755, 0.00032197, 800.15849185, 0.00107323, -80.01584918, -0.00010732, -240.04754755, -0.00032197, -800.15849185, -0.00107323, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 217.77064696, 0.01804154, 217.77064696, 0.05412463, 152.43945287, -2452.58441011, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 54.44266174, 7.302e-05, 163.32798522, 0.00021907, 544.4266174, 0.00073023, -54.44266174, -7.302e-05, -163.32798522, -0.00021907, -544.4266174, -0.00073023, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 13.95, 0.0)
    ops.node(121013, 0.0, 13.95, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.105, 27724003.17264619, 11551667.98860258, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 132.65543743, 0.00100421, 158.07991358, 0.01017407, 15.80799136, 0.03021266, -132.65543743, -0.00100421, -158.07991358, -0.01017407, -15.80799136, -0.03021266, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 142.97193445, 0.00089256, 170.37364981, 0.0104975, 17.03736498, 0.03286521, -142.97193445, -0.00089256, -170.37364981, -0.0104975, -17.03736498, -0.03286521, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 131.1932783, 0.0200842, 131.1932783, 0.06025259, 91.83529481, -1778.69533174, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 32.79831958, 8.923e-05, 98.39495873, 0.0002677, 327.98319575, 0.00089234, -32.79831958, -8.923e-05, -98.39495873, -0.0002677, -327.98319575, -0.00089234, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 138.53316006, 0.01785125, 138.53316006, 0.05355374, 96.97321204, -1960.4935778, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 34.63329002, 9.423e-05, 103.89987005, 0.00028268, 346.33290016, 0.00094227, -34.63329002, -9.423e-05, -103.89987005, -0.00028268, -346.33290016, -0.00094227, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.95, 13.95, 0.0)
    ops.node(121014, 4.95, 13.95, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.1575, 25831942.59450376, 10763309.41437657, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 222.5262091, 0.00087431, 265.38169954, 0.00941385, 26.53816995, 0.02662866, -222.5262091, -0.00087431, -265.38169954, -0.00941385, -26.53816995, -0.02662866, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 243.8260684, 0.00074413, 290.7836191, 0.00994962, 29.07836191, 0.03052095, -243.8260684, -0.00074413, -290.7836191, -0.00994962, -29.07836191, -0.03052095, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 172.77030208, 0.01748624, 172.77030208, 0.05245872, 120.93921146, -2319.91463253, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 43.19257552, 8.408e-05, 129.57772656, 0.00025224, 431.9257552, 0.00084081, -43.19257552, -8.408e-05, -129.57772656, -0.00025224, -431.9257552, -0.00084081, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 194.4031923, 0.01488264, 194.4031923, 0.04464791, 136.08223461, -2721.10372411, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 48.60079808, 9.461e-05, 145.80239423, 0.00028383, 486.00798075, 0.00094609, -48.60079808, -9.461e-05, -145.80239423, -0.00028383, -486.00798075, -0.00094609, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.9, 13.95, 0.0)
    ops.node(121015, 7.9, 13.95, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.1575, 27659086.01206975, 11524619.17169573, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 231.7927061, 0.00086364, 277.03517853, 0.00941169, 27.70351785, 0.0301814, -231.7927061, -0.00086364, -277.03517853, -0.00941169, -27.70351785, -0.0301814, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 251.74376482, 0.00073971, 300.88038578, 0.00995438, 30.08803858, 0.03477373, -251.74376482, -0.00073971, -300.88038578, -0.00995438, -30.08803858, -0.03477373, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 182.63379297, 0.01727274, 182.63379297, 0.05181821, 127.84365508, -2337.69202694, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 45.65844824, 8.301e-05, 136.97534473, 0.00024903, 456.58448242, 0.0008301, -45.65844824, -8.301e-05, -136.97534473, -0.00024903, -456.58448242, -0.0008301, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 204.91017597, 0.01479415, 204.91017597, 0.04438244, 143.43712318, -2745.86677869, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 51.22754399, 9.313e-05, 153.68263198, 0.0002794, 512.27543992, 0.00093134, -51.22754399, -9.313e-05, -153.68263198, -0.0002794, -512.27543992, -0.00093134, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.85, 13.95, 0.0)
    ops.node(121016, 12.85, 13.95, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.105, 26153874.46889042, 10897447.69537101, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 127.71076697, 0.00101931, 151.84106631, 0.00888351, 15.18410663, 0.02570039, -127.71076697, -0.00101931, -151.84106631, -0.00888351, -15.18410663, -0.02570039, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 138.45467458, 0.00090151, 164.61498056, 0.00913884, 16.46149806, 0.02791038, -138.45467458, -0.00090151, -164.61498056, -0.00913884, -16.46149806, -0.02791038, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 121.26661632, 0.02038611, 121.26661632, 0.06115833, 84.88663142, -1669.76698673, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 30.31665408, 8.743e-05, 90.94996224, 0.0002623, 303.16654079, 0.00087434, -30.31665408, -8.743e-05, -90.94996224, -0.0002623, -303.16654079, -0.00087434, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 127.84338177, 0.01803027, 127.84338177, 0.05409081, 89.49036724, -1827.30848164, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 31.96084544, 9.218e-05, 95.88253633, 0.00027653, 319.60845442, 0.00092176, -31.96084544, -9.218e-05, -95.88253633, -0.00027653, -319.60845442, -0.00092176, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.0)
    ops.node(122001, 0.0, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.105, 28943108.3151231, 12059628.46463462, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 124.80533281, 0.00102272, 149.68032311, 0.01152374, 14.96803231, 0.03815811, -124.80533281, -0.00102272, -149.68032311, -0.01152374, -14.96803231, -0.03815811, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 131.2498051, 0.00089985, 157.40924521, 0.01189911, 15.74092452, 0.04162923, -131.2498051, -0.00089985, -157.40924521, -0.01189911, -15.74092452, -0.04162923, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 123.73344851, 0.02045441, 123.73344851, 0.06136324, 86.61341396, -1516.55808248, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 30.93336213, 8.062e-05, 92.80008639, 0.00024185, 309.33362128, 0.00080615, -30.93336213, -8.062e-05, -92.80008639, -0.00024185, -309.33362128, -0.00080615, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 130.44741194, 0.01799704, 130.44741194, 0.05399111, 91.31318835, -1694.20616094, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 32.61185298, 8.499e-05, 97.83555895, 0.00025497, 326.11852984, 0.0008499, -32.61185298, -8.499e-05, -97.83555895, -0.00025497, -326.11852984, -0.0008499, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.85, 0.0, 3.0)
    ops.node(122004, 12.85, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.105, 29403977.48437407, 12251657.28515586, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 117.89242718, 0.00098255, 141.33930045, 0.01215635, 14.13393004, 0.03952838, -117.89242718, -0.00098255, -141.33930045, -0.01215635, -14.13393004, -0.03952838, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 124.84300045, 0.00086371, 149.67222892, 0.01256766, 14.96722289, 0.04312119, -124.84300045, -0.00086371, -149.67222892, -0.01256766, -14.96722289, -0.04312119, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 126.82436228, 0.019651, 126.82436228, 0.05895301, 88.77705359, -1556.45377217, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 31.70609057, 8.133e-05, 95.11827171, 0.000244, 317.0609057, 0.00081334, -31.70609057, -8.133e-05, -95.11827171, -0.000244, -317.0609057, -0.00081334, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 133.79510384, 0.0172742, 133.79510384, 0.0518226, 93.65657269, -1743.43492487, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 33.44877596, 8.58e-05, 100.34632788, 0.00025741, 334.4877596, 0.00085804, -33.44877596, -8.58e-05, -100.34632788, -0.00025741, -334.4877596, -0.00085804, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.65, 3.05)
    ops.node(122005, 0.0, 4.65, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.21, 27578734.12184899, 11491139.21743708, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 334.97851001, 0.00060453, 403.17222081, 0.01034734, 40.31722208, 0.03702336, -334.97851001, -0.00060453, -403.17222081, -0.01034734, -40.31722208, -0.03702336, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 170.71564169, 0.00080665, 205.46931319, 0.00924287, 20.54693132, 0.02820033, -170.71564169, -0.00080665, -205.46931319, -0.00924287, -20.54693132, -0.02820033, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 285.46208449, 0.01209066, 285.46208449, 0.03627198, 199.82345914, -2766.1794097, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 71.36552112, 9.759e-05, 214.09656336, 0.00029278, 713.65521121, 0.00097593, -71.36552112, -9.759e-05, -214.09656336, -0.00029278, -713.65521121, -0.00097593, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 194.37841698, 0.01613297, 194.37841698, 0.04839891, 136.06489189, -1988.98830075, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 48.59460424, 6.645e-05, 145.78381273, 0.00019936, 485.94604245, 0.00066454, -48.59460424, -6.645e-05, -145.78381273, -0.00019936, -485.94604245, -0.00066454, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 4.95, 4.65, 3.05)
    ops.node(122006, 4.95, 4.65, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.36, 29347858.64705681, 12228274.43627367, 0.01576053, 0.0066825, 0.02112, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 703.75942993, 0.00056463, 849.86700996, 0.00807857, 84.986701, 0.03211212, -703.75942993, -0.00056463, -849.86700996, -0.00807857, -84.986701, -0.03211212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 334.07936508, 0.00069535, 403.43762232, 0.00735919, 40.34376223, 0.02543628, -334.07936508, -0.00069535, -403.43762232, -0.00735919, -40.34376223, -0.02543628, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 537.00286698, 0.01129252, 537.00286698, 0.03387757, 375.90200689, -2736.0719651, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 134.25071675, 0.00010064, 402.75215024, 0.00030191, 1342.50716746, 0.00100638, -134.25071675, -0.00010064, -402.75215024, -0.00030191, -1342.50716746, -0.00100638, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 302.06411268, 0.01390702, 302.06411268, 0.04172106, 211.44487887, -2043.78578912, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 75.51602817, 5.661e-05, 226.54808451, 0.00016983, 755.1602817, 0.00056609, -75.51602817, -5.661e-05, -226.54808451, -0.00016983, -755.1602817, -0.00056609, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 7.9, 4.65, 3.05)
    ops.node(122007, 7.9, 4.65, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.36, 25367381.45314012, 10569742.27214172, 0.01576053, 0.0066825, 0.02112, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 663.44486859, 0.0005551, 803.84681239, 0.01016158, 80.38468124, 0.03016071, -663.44486859, -0.0005551, -803.84681239, -0.01016158, -80.38468124, -0.03016071, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 314.46743549, 0.0006848, 381.01680725, 0.00920443, 38.10168073, 0.02424698, -314.46743549, -0.0006848, -381.01680725, -0.00920443, -38.10168073, -0.02424698, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 475.28233492, 0.01110193, 475.28233492, 0.03330578, 332.69763444, -3155.97440796, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 118.82058373, 0.00010305, 356.46175119, 0.00030914, 1188.2058373, 0.00103048, -118.82058373, -0.00010305, -356.46175119, -0.00030914, -1188.2058373, -0.00103048, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 267.34631339, 0.01369596, 267.34631339, 0.04108787, 187.14241937, -2245.38115336, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 66.83657835, 5.796e-05, 200.50973504, 0.00017389, 668.36578348, 0.00057964, -66.83657835, -5.796e-05, -200.50973504, -0.00017389, -668.36578348, -0.00057964, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 12.85, 4.65, 3.05)
    ops.node(122008, 12.85, 4.65, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.21, 27624437.34542678, 11510182.22726116, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 347.44636116, 0.00062194, 418.1728699, 0.01076318, 41.81728699, 0.03751728, -347.44636116, -0.00062194, -418.1728699, -0.01076318, -41.81728699, -0.03751728, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 176.48156106, 0.00083203, 212.40631397, 0.00961325, 21.2406314, 0.0286262, -176.48156106, -0.00083203, -212.40631397, -0.00961325, -21.2406314, -0.0286262, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 290.44487344, 0.01243882, 290.44487344, 0.03731645, 203.31141141, -2889.46341677, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 72.61121836, 9.913e-05, 217.83365508, 0.0002974, 726.11218361, 0.00099133, -72.61121836, -9.913e-05, -217.83365508, -0.0002974, -726.11218361, -0.00099133, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 197.33950806, 0.01664054, 197.33950806, 0.04992162, 138.13765564, -2049.76254769, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 49.33487701, 6.735e-05, 148.00463104, 0.00020206, 493.34877015, 0.00067354, -49.33487701, -6.735e-05, -148.00463104, -0.00020206, -493.34877015, -0.00067354, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 9.3, 3.05)
    ops.node(122009, 0.0, 9.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.21, 25208998.17220958, 10503749.23842066, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 338.84069992, 0.00061921, 407.52911179, 0.00876119, 40.75291118, 0.03113536, -338.84069992, -0.00061921, -407.52911179, -0.00876119, -40.75291118, -0.03113536, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 171.65695516, 0.00082836, 206.45455662, 0.00787843, 20.64545566, 0.02377876, -171.65695516, -0.00082836, -206.45455662, -0.00787843, -20.64545566, -0.02377876, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 257.82471053, 0.01238426, 257.82471053, 0.03715279, 180.47729737, -2597.27445859, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 64.45617763, 9.643e-05, 193.3685329, 0.00028929, 644.56177633, 0.00096431, -64.45617763, -9.643e-05, -193.3685329, -0.00028929, -644.56177633, -0.00096431, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 175.38578, 0.01656717, 175.38578, 0.04970152, 122.770046, -1896.9150112, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 43.846445, 6.56e-05, 131.539335, 0.00019679, 438.46445001, 0.00065597, -43.846445, -6.56e-05, -131.539335, -0.00019679, -438.46445001, -0.00065597, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 4.95, 9.3, 3.05)
    ops.node(122010, 4.95, 9.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.3, 27304250.14761152, 11376770.89483813, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 540.32147159, 0.00056258, 652.99193626, 0.01012724, 65.29919363, 0.03711736, -540.32147159, -0.00056258, -652.99193626, -0.01012724, -65.29919363, -0.03711736, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 238.96157064, 0.00072876, 288.79100111, 0.00890866, 28.87910011, 0.0275333, -238.96157064, -0.00072876, -288.79100111, -0.00890866, -28.87910011, -0.0275333, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 432.5002454, 0.01125166, 432.5002454, 0.03375499, 302.75017178, -3156.52816043, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 108.12506135, 0.00010454, 324.37518405, 0.00031363, 1081.25061351, 0.00104544, -108.12506135, -0.00010454, -324.37518405, -0.00031363, -1081.25061351, -0.00104544, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 244.33827644, 0.0145753, 244.33827644, 0.0437259, 171.03679351, -2154.82113818, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 61.08456911, 5.906e-05, 183.25370733, 0.00017718, 610.84569109, 0.00059062, -61.08456911, -5.906e-05, -183.25370733, -0.00017718, -610.84569109, -0.00059062, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.9, 9.3, 3.05)
    ops.node(122011, 7.9, 9.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.3, 25529056.92288116, 10637107.05120048, 0.01066025, 0.0044, 0.01546875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 533.42363586, 0.00057886, 644.83682857, 0.0093343, 64.48368286, 0.03357168, -533.42363586, -0.00057886, -644.83682857, -0.0093343, -64.48368286, -0.03357168, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 236.28538842, 0.00077345, 285.63698768, 0.00826128, 28.56369877, 0.02498639, -236.28538842, -0.00077345, -285.63698768, -0.00826128, -28.56369877, -0.02498639, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 406.94671801, 0.01157723, 406.94671801, 0.03473169, 284.86270261, -3198.24468801, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 101.7366795, 0.00010521, 305.21003851, 0.00031562, 1017.36679502, 0.00105208, -101.7366795, -0.00010521, -305.21003851, -0.00031562, -1017.36679502, -0.00105208, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 229.63724175, 0.015469, 229.63724175, 0.04640701, 160.74606923, -2173.18237907, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 57.40931044, 5.937e-05, 172.22793131, 0.0001781, 574.09310438, 0.00059368, -57.40931044, -5.937e-05, -172.22793131, -0.0001781, -574.09310438, -0.00059368, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 12.85, 9.3, 3.05)
    ops.node(122012, 12.85, 9.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.21, 25777876.2481099, 10740781.77004579, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 348.49412507, 0.00063632, 419.3714178, 0.0086944, 41.93714178, 0.03223155, -348.49412507, -0.00063632, -419.3714178, -0.0086944, -41.93714178, -0.03223155, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 176.28612825, 0.00085788, 212.13948306, 0.00783532, 21.21394831, 0.02456212, -176.28612825, -0.00085788, -212.13948306, -0.00783532, -21.21394831, -0.02456212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 260.99668257, 0.01272643, 260.99668257, 0.03817929, 182.6976778, -2552.11882412, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 65.24917064, 9.546e-05, 195.74751193, 0.00028639, 652.49170642, 0.00095463, -65.24917064, -9.546e-05, -195.74751193, -0.00028639, -652.49170642, -0.00095463, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 177.88892476, 0.01715768, 177.88892476, 0.05147304, 124.52224733, -1874.37273422, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 44.47223119, 6.507e-05, 133.41669357, 0.0001952, 444.72231191, 0.00065065, -44.47223119, -6.507e-05, -133.41669357, -0.0001952, -444.72231191, -0.00065065, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 13.95, 3.0)
    ops.node(122013, 0.0, 13.95, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.105, 28011290.64789016, 11671371.10328757, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 131.07644153, 0.00093625, 157.33082667, 0.01123484, 15.73308267, 0.03662242, -131.07644153, -0.00093625, -157.33082667, -0.01123484, -15.73308267, -0.03662242, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 133.68891039, 0.00083799, 160.46656854, 0.0116252, 16.04665685, 0.03996363, -133.68891039, -0.00083799, -160.46656854, -0.0116252, -16.04665685, -0.03996363, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 120.87690882, 0.0187251, 120.87690882, 0.05617529, 84.61383618, -1526.80890305, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 30.21922721, 8.137e-05, 90.65768162, 0.00024412, 302.19227205, 0.00081374, -30.21922721, -8.137e-05, -90.65768162, -0.00024412, -302.19227205, -0.00081374, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 127.72552642, 0.01675981, 127.72552642, 0.05027944, 89.4078685, -1710.86804333, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 31.93138161, 8.598e-05, 95.79414482, 0.00025795, 319.31381606, 0.00085985, -31.93138161, -8.598e-05, -95.79414482, -0.00025795, -319.31381606, -0.00085985, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.95, 13.95, 3.0)
    ops.node(122014, 4.95, 13.95, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.1575, 26384825.93716229, 10993677.47381762, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 165.95583754, 0.0008637, 199.5791393, 0.00841731, 19.95791393, 0.0312967, -165.95583754, -0.0008637, -199.5791393, -0.00841731, -19.95791393, -0.0312967, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 181.60794024, 0.00073455, 218.40241923, 0.00887723, 21.84024192, 0.03621761, -181.60794024, -0.00073455, -218.40241923, -0.00887723, -21.84024192, -0.03621761, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 158.53334767, 0.01727404, 158.53334767, 0.05182211, 110.97334337, -1931.02711964, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 39.63333692, 7.554e-05, 118.90001075, 0.00022661, 396.33336918, 0.00075535, -39.63333692, -7.554e-05, -118.90001075, -0.00022661, -396.33336918, -0.00075535, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 178.0541214, 0.01469102, 178.0541214, 0.04407305, 124.63788498, -2312.63646083, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 44.51353035, 8.484e-05, 133.54059105, 0.00025451, 445.13530349, 0.00084836, -44.51353035, -8.484e-05, -133.54059105, -0.00025451, -445.13530349, -0.00084836, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.9, 13.95, 3.0)
    ops.node(122015, 7.9, 13.95, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.1575, 25619034.26883273, 10674597.61201364, 0.00337604, 0.00292359, 0.00176859, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 162.27973937, 0.00086464, 195.04350739, 0.00942763, 19.50435074, 0.03085188, -162.27973937, -0.00086464, -195.04350739, -0.00942763, -19.50435074, -0.03085188, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 178.52461126, 0.00073326, 214.56816772, 0.00996404, 21.45681677, 0.03556556, -178.52461126, -0.00073326, -214.56816772, -0.00996404, -21.45681677, -0.03556556, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 159.0830463, 0.01729274, 159.0830463, 0.05187821, 111.35813241, -2037.6087067, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 39.77076157, 7.806e-05, 119.31228472, 0.00023419, 397.70761574, 0.00078063, -39.77076157, -7.806e-05, -119.31228472, -0.00023419, -397.70761574, -0.00078063, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 179.62128132, 0.01466519, 179.62128132, 0.04399556, 125.73489692, -2462.95233655, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 44.90532033, 8.814e-05, 134.71596099, 0.00026442, 449.05320329, 0.00088141, -44.90532033, -8.814e-05, -134.71596099, -0.00026442, -449.05320329, -0.00088141, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.85, 13.95, 3.0)
    ops.node(122016, 12.85, 13.95, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.105, 26354583.35465271, 10981076.39777196, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 122.29724803, 0.00102065, 146.71858577, 0.00923642, 14.67185858, 0.03151102, -122.29724803, -0.00102065, -146.71858577, -0.00923642, -14.67185858, -0.03151102, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 128.0535856, 0.00089848, 153.62439698, 0.00950406, 15.3624397, 0.03436768, -128.0535856, -0.00089848, -153.62439698, -0.00950406, -15.3624397, -0.03436768, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 102.27535153, 0.02041305, 102.27535153, 0.06123914, 71.59274607, -1372.17662094, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 25.56883788, 7.318e-05, 76.70651365, 0.00021954, 255.68837884, 0.0007318, -25.56883788, -7.318e-05, -76.70651365, -0.00021954, -255.68837884, -0.0007318, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 115.24675931, 0.01796961, 115.24675931, 0.05390884, 80.67273151, -1520.41955425, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 28.81168983, 8.246e-05, 86.43506948, 0.00024738, 288.11689827, 0.00082461, -28.81168983, -8.246e-05, -86.43506948, -0.00024738, -288.11689827, -0.00082461, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.75)
    ops.node(123001, 0.0, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 26971058.91961571, 11237941.21650655, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 58.30045822, 0.00120286, 69.8117457, 0.00986767, 6.98117457, 0.03795158, -58.30045822, -0.00120286, -69.8117457, -0.00986767, -6.98117457, -0.03795158, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 58.30045822, 0.00120286, 69.8117457, 0.00986767, 6.98117457, 0.03795158, -58.30045822, -0.00120286, -69.8117457, -0.00986767, -6.98117457, -0.03795158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 50.89225487, 0.02405726, 50.89225487, 0.07217178, 35.62457841, -1049.6857663, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 12.72306372, 5.978e-05, 38.16919115, 0.00017933, 127.23063716, 0.00059778, -12.72306372, -5.978e-05, -38.16919115, -0.00017933, -127.23063716, -0.00059778, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 50.89225487, 0.02405726, 50.89225487, 0.07217178, 35.62457841, -1049.6857663, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 12.72306372, 5.978e-05, 38.16919115, 0.00017933, 127.23063716, 0.00059778, -12.72306372, -5.978e-05, -38.16919115, -0.00017933, -127.23063716, -0.00059778, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.85, 0.0, 5.75)
    ops.node(123004, 12.85, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 27469101.87824628, 11445459.11593595, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 57.87886946, 0.00117428, 69.32571794, 0.01205702, 6.93257179, 0.04137348, -57.87886946, -0.00117428, -69.32571794, -0.01205702, -6.93257179, -0.04137348, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 57.87886946, 0.00117428, 69.32571794, 0.01205702, 6.93257179, 0.04137348, -57.87886946, -0.00117428, -69.32571794, -0.01205702, -6.93257179, -0.04137348, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 77.20182588, 0.02348566, 77.20182588, 0.07045698, 54.04127812, -1201.36951112, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 19.30045647, 8.904e-05, 57.90136941, 0.00026711, 193.00456471, 0.00089037, -19.30045647, -8.904e-05, -57.90136941, -0.00026711, -193.00456471, -0.00089037, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 77.20182588, 0.02348566, 77.20182588, 0.07045698, 54.04127812, -1201.36951112, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 19.30045647, 8.904e-05, 57.90136941, 0.00026711, 193.00456471, 0.00089037, -19.30045647, -8.904e-05, -57.90136941, -0.00026711, -193.00456471, -0.00089037, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.65, 5.8)
    ops.node(123005, 0.0, 4.65, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.125, 26253179.92213515, 10938824.96755631, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 174.62966169, 0.00065453, 209.69196522, 0.01009206, 20.96919652, 0.03918168, -174.62966169, -0.00065453, -209.69196522, -0.01009206, -20.96919652, -0.03918168, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 86.8889046, 0.00105169, 104.3345385, 0.00875963, 10.43345385, 0.02675596, -86.8889046, -0.00105169, -104.3345385, -0.00875963, -10.43345385, -0.02675596, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 158.21482365, 0.01309063, 158.21482365, 0.0392719, 110.75037656, -2015.21850082, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 39.55370591, 9.546e-05, 118.66111774, 0.00028638, 395.53705913, 0.0009546, -39.55370591, -9.546e-05, -118.66111774, -0.00028638, -395.53705913, -0.0009546, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 94.67485959, 0.02103371, 94.67485959, 0.06310113, 66.27240171, -1294.82296485, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 23.6687149, 5.712e-05, 71.00614469, 0.00017137, 236.68714896, 0.00057123, -23.6687149, -5.712e-05, -71.00614469, -0.00017137, -236.68714896, -0.00057123, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 4.95, 4.65, 5.8)
    ops.node(123006, 4.95, 4.65, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.2625, 28204584.60188689, 11751910.25078621, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 458.88557584, 0.00056211, 555.52168287, 0.01106294, 55.55216829, 0.0385124, -458.88557584, -0.00056211, -555.52168287, -0.01106294, -55.55216829, -0.0385124, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 185.96988396, 0.00079846, 225.13303607, 0.00964133, 22.51330361, 0.02790146, -185.96988396, -0.00079846, -225.13303607, -0.00964133, -22.51330361, -0.02790146, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 376.08017206, 0.01124219, 376.08017206, 0.03372657, 263.25612044, -2676.17534075, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 94.02004301, 0.00010058, 282.06012904, 0.00030173, 940.20043015, 0.00100577, -94.02004301, -0.00010058, -282.06012904, -0.00030173, -940.20043015, -0.00100577, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 207.25177393, 0.01596921, 207.25177393, 0.04790764, 145.07624175, -1598.16463496, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 51.81294348, 5.543e-05, 155.43883045, 0.00016628, 518.12943482, 0.00055426, -51.81294348, -5.543e-05, -155.43883045, -0.00016628, -518.12943482, -0.00055426, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 7.9, 4.65, 5.8)
    ops.node(123007, 7.9, 4.65, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.2625, 27532434.52446334, 11471847.71852639, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 460.2845863, 0.00056666, 557.65735135, 0.0095308, 55.76573514, 0.03627376, -460.2845863, -0.00056666, -557.65735135, -0.0095308, -55.76573514, -0.03627376, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 186.19898274, 0.00080994, 225.58919987, 0.00835875, 22.55891999, 0.02614889, -186.19898274, -0.00080994, -225.58919987, -0.00835875, -22.55891999, -0.02614889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 357.89595757, 0.01133324, 357.89595757, 0.03399971, 250.5271703, -2413.92970834, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 89.47398939, 9.805e-05, 268.42196818, 0.00029415, 894.73989394, 0.0009805, -89.47398939, -9.805e-05, -268.42196818, -0.00029415, -894.73989394, -0.0009805, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 186.00394334, 0.01619888, 186.00394334, 0.04859664, 130.20276034, -1502.62566434, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 46.50098584, 5.096e-05, 139.50295751, 0.00015287, 465.00985835, 0.00050958, -46.50098584, -5.096e-05, -139.50295751, -0.00015287, -465.00985835, -0.00050958, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 12.85, 4.65, 5.8)
    ops.node(123008, 12.85, 4.65, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.125, 27624398.41257858, 11510166.00524108, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 184.9026801, 0.00068578, 222.13261423, 0.01083528, 22.21326142, 0.0432366, -184.9026801, -0.00068578, -222.13261423, -0.01083528, -22.21326142, -0.0432366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 92.1252326, 0.00110914, 110.67453833, 0.00939857, 11.06745383, 0.02944369, -92.1252326, -0.00110914, -110.67453833, -0.00939857, -11.06745383, -0.02944369, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 171.50234994, 0.01371565, 171.50234994, 0.04114695, 120.05164496, -2221.68003204, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 42.87558749, 9.834e-05, 128.62676246, 0.00029502, 428.75587486, 0.00098341, -42.87558749, -9.834e-05, -128.62676246, -0.00029502, -428.75587486, -0.00098341, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 110.42736733, 0.02218278, 110.42736733, 0.06654833, 77.29915713, -1376.81119051, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 27.60684183, 6.332e-05, 82.8205255, 0.00018996, 276.06841833, 0.0006332, -27.60684183, -6.332e-05, -82.8205255, -0.00018996, -276.06841833, -0.0006332, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 9.3, 5.8)
    ops.node(123009, 0.0, 9.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.125, 27130705.82017782, 11304460.75840742, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 180.5403197, 0.00068565, 216.94775467, 0.01055044, 21.69477547, 0.04207745, -180.5403197, -0.00068565, -216.94775467, -0.01055044, -21.69477547, -0.04207745, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 89.3287897, 0.001125, 107.34267218, 0.00918191, 10.73426722, 0.02868614, -89.3287897, -0.001125, -107.34267218, -0.00918191, -10.73426722, -0.02868614, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 167.41874174, 0.01371293, 167.41874174, 0.04113879, 117.19311922, -2175.51341972, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 41.85468543, 9.775e-05, 125.5640563, 0.00029324, 418.54685434, 0.00097746, -41.85468543, -9.775e-05, -125.5640563, -0.00029324, -418.54685434, -0.00097746, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 104.40838167, 0.02250003, 104.40838167, 0.06750009, 73.08586717, -1351.52696556, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 26.10209542, 6.096e-05, 78.30628625, 0.00018287, 261.02095417, 0.00060958, -26.10209542, -6.096e-05, -78.30628625, -0.00018287, -261.02095417, -0.00060958, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 4.95, 9.3, 5.8)
    ops.node(123010, 4.95, 9.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.2275, 28993110.08850084, 12080462.53687535, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 362.32120979, 0.00059046, 437.63827995, 0.0103128, 43.763828, 0.0433733, -362.32120979, -0.00059046, -437.63827995, -0.0103128, -43.763828, -0.0433733, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 164.50843111, 0.00080191, 198.7054163, 0.00906341, 19.87054163, 0.03153195, -164.50843111, -0.00080191, -198.7054163, -0.00906341, -19.87054163, -0.03153195, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 314.19369664, 0.01180919, 314.19369664, 0.03542758, 219.93558765, -2618.08921649, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 78.54842416, 9.432e-05, 235.64527248, 0.00028295, 785.48424161, 0.00094316, -78.54842416, -9.432e-05, -235.64527248, -0.00028295, -785.48424161, -0.00094316, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 198.41083796, 0.01603816, 198.41083796, 0.04811447, 138.88758657, -1682.26502711, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 49.60270949, 5.956e-05, 148.80812847, 0.00017868, 496.02709491, 0.0005956, -49.60270949, -5.956e-05, -148.80812847, -0.00017868, -496.02709491, -0.0005956, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.9, 9.3, 5.8)
    ops.node(123011, 7.9, 9.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.2275, 27939068.65764095, 11641278.60735039, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 364.53306554, 0.00059564, 440.90633461, 0.00994998, 44.09063346, 0.0416642, -364.53306554, -0.00059564, -440.90633461, -0.00994998, -44.09063346, -0.0416642, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 165.18548013, 0.00081053, 199.79346583, 0.00875934, 19.97934658, 0.03031291, -165.18548013, -0.00081053, -199.79346583, -0.00875934, -19.97934658, -0.03031291, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 300.72617476, 0.0119127, 300.72617476, 0.03573811, 210.50832233, -2542.1188137, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 75.18154369, 9.368e-05, 225.54463107, 0.00028104, 751.81543691, 0.00093679, -75.18154369, -9.368e-05, -225.54463107, -0.00028104, -751.81543691, -0.00093679, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 189.82385994, 0.01621067, 189.82385994, 0.048632, 132.87670195, -1649.39482892, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 47.45596498, 5.913e-05, 142.36789495, 0.0001774, 474.55964984, 0.00059132, -47.45596498, -5.913e-05, -142.36789495, -0.0001774, -474.55964984, -0.00059132, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 12.85, 9.3, 5.8)
    ops.node(123012, 12.85, 9.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.125, 26018517.25641327, 10841048.85683887, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 180.95545324, 0.0007113, 217.31721614, 0.01037186, 21.73172161, 0.03914574, -180.95545324, -0.0007113, -217.31721614, -0.01037186, -21.73172161, -0.03914574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 88.6454454, 0.00120595, 106.45814245, 0.00909606, 10.64581424, 0.02689706, -88.6454454, -0.00120595, -106.45814245, -0.00909606, -10.64581424, -0.02689706, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 161.96386587, 0.01422591, 161.96386587, 0.04267773, 113.37470611, -2159.82713094, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 40.49096647, 9.86e-05, 121.4728994, 0.00029581, 404.90966467, 0.00098603, -40.49096647, -9.86e-05, -121.4728994, -0.00029581, -404.90966467, -0.00098603, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 102.75941489, 0.02411897, 102.75941489, 0.0723569, 71.93159042, -1345.34098049, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 25.68985372, 6.256e-05, 77.06956116, 0.00018768, 256.89853721, 0.0006256, -25.68985372, -6.256e-05, -77.06956116, -0.00018768, -256.89853721, -0.0006256, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 13.95, 5.75)
    ops.node(123013, 0.0, 13.95, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 28488648.32723416, 11870270.13634757, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 60.78580235, 0.0011428, 72.84885531, 0.01242489, 7.28488553, 0.04459909, -60.78580235, -0.0011428, -72.84885531, -0.01242489, -7.28488553, -0.04459909, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 60.78580235, 0.0011428, 72.84885531, 0.01242489, 7.28488553, 0.04459909, -60.78580235, -0.0011428, -72.84885531, -0.01242489, -7.28488553, -0.04459909, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 84.10712364, 0.02285594, 84.10712364, 0.06856781, 58.87498655, -1277.79948231, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 21.02678091, 9.353e-05, 63.08034273, 0.00028059, 210.26780909, 0.00093529, -21.02678091, -9.353e-05, -63.08034273, -0.00028059, -210.26780909, -0.00093529, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 84.10712364, 0.02285594, 84.10712364, 0.06856781, 58.87498655, -1277.79948231, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 21.02678091, 9.353e-05, 63.08034273, 0.00028059, 210.26780909, 0.00093529, -21.02678091, -9.353e-05, -63.08034273, -0.00028059, -210.26780909, -0.00093529, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.95, 13.95, 5.75)
    ops.node(123014, 4.95, 13.95, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.105, 30761984.08654795, 12817493.36939498, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 90.29831162, 0.00090713, 108.29240442, 0.00946704, 10.82924044, 0.04498011, -90.29831162, -0.00090713, -108.29240442, -0.00946704, -10.82924044, -0.04498011, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 95.0229688, 0.00080876, 113.95856226, 0.00979675, 11.39585623, 0.0496681, -95.0229688, -0.00080876, -113.95856226, -0.00979675, -11.39585623, -0.0496681, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 125.60749865, 0.01814254, 125.60749865, 0.05442761, 87.92524906, -1436.23764991, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 31.40187466, 7.7e-05, 94.20562399, 0.00023099, 314.01874663, 0.00076998, -31.40187466, -7.7e-05, -94.20562399, -0.00023099, -314.01874663, -0.00076998, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 132.20592638, 0.01617521, 132.20592638, 0.04852563, 92.54414846, -1619.48251917, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 33.05148159, 8.104e-05, 99.15444478, 0.00024313, 330.51481595, 0.00081042, -33.05148159, -8.104e-05, -99.15444478, -0.00024313, -330.51481595, -0.00081042, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.9, 13.95, 5.75)
    ops.node(123015, 7.9, 13.95, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.105, 27602684.34676113, 11501118.47781714, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 90.05658396, 0.00094224, 108.35525241, 0.01141348, 10.83552524, 0.0415742, -90.05658396, -0.00094224, -108.35525241, -0.01141348, -10.83552524, -0.0415742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 94.75519423, 0.00083716, 114.00857703, 0.01183207, 11.4008577, 0.04569421, -94.75519423, -0.00083716, -114.00857703, -0.01183207, -11.4008577, -0.04569421, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 125.51025621, 0.01884475, 125.51025621, 0.05653425, 87.85717934, -1728.44728127, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 31.37756405, 8.574e-05, 94.13269216, 0.00025723, 313.77564052, 0.00085744, -31.37756405, -8.574e-05, -94.13269216, -0.00025723, -313.77564052, -0.00085744, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 133.83298183, 0.01674327, 133.83298183, 0.05022981, 93.68308728, -1983.14173631, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 33.45824546, 9.143e-05, 100.37473637, 0.00027429, 334.58245457, 0.0009143, -33.45824546, -9.143e-05, -100.37473637, -0.00027429, -334.58245457, -0.0009143, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.85, 13.95, 5.75)
    ops.node(123016, 12.85, 13.95, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 29706044.79564267, 12377518.66485111, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 56.35742801, 0.0012075, 67.49005373, 0.01096362, 6.74900537, 0.04570646, -56.35742801, -0.0012075, -67.49005373, -0.01096362, -6.74900537, -0.04570646, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 56.35742801, 0.0012075, 67.49005373, 0.01096362, 6.74900537, 0.04570646, -56.35742801, -0.0012075, -67.49005373, -0.01096362, -6.74900537, -0.04570646, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 60.40663404, 0.02414995, 60.40663404, 0.07244986, 42.28464383, -1065.22128435, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 15.10165851, 6.442e-05, 45.30497553, 0.00019326, 151.01658511, 0.00064421, -15.10165851, -6.442e-05, -45.30497553, -0.00019326, -151.01658511, -0.00064421, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 60.40663404, 0.02414995, 60.40663404, 0.07244986, 42.28464383, -1065.22128435, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 15.10165851, 6.442e-05, 45.30497553, 0.00019326, 151.01658511, 0.00064421, -15.10165851, -6.442e-05, -45.30497553, -0.00019326, -151.01658511, -0.00064421, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.5)
    ops.node(124001, 0.0, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26935038.34657495, 11222932.64440623, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 46.17559672, 0.00108965, 56.1506483, 0.01458612, 5.61506483, 0.05891461, -46.17559672, -0.00108965, -56.1506483, -0.01458612, -5.61506483, -0.05891461, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 46.17559672, 0.00108965, 56.1506483, 0.01458612, 5.61506483, 0.05891461, -46.17559672, -0.00108965, -56.1506483, -0.01458612, -5.61506483, -0.05891461, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 66.25535783, 0.021793, 66.25535783, 0.06537901, 46.37875048, -1263.26216021, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 16.56383946, 7.793e-05, 49.69151837, 0.00023378, 165.63839456, 0.00077927, -16.56383946, -7.793e-05, -49.69151837, -0.00023378, -165.63839456, -0.00077927, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 66.25535783, 0.021793, 66.25535783, 0.06537901, 46.37875048, -1263.26216021, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 16.56383946, 7.793e-05, 49.69151837, 0.00023378, 165.63839456, 0.00077927, -16.56383946, -7.793e-05, -49.69151837, -0.00023378, -165.63839456, -0.00077927, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.85, 0.0, 8.5)
    ops.node(124004, 12.85, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 27884144.93644137, 11618393.72351724, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 46.42212026, 0.00106591, 56.37821852, 0.01213732, 5.63782185, 0.05778756, -46.42212026, -0.00106591, -56.37821852, -0.01213732, -5.63782185, -0.05778756, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 46.42212026, 0.00106591, 56.37821852, 0.01213732, 5.63782185, 0.05778756, -46.42212026, -0.00106591, -56.37821852, -0.01213732, -5.63782185, -0.05778756, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 42.93506587, 0.02131829, 42.93506587, 0.06395488, 30.05454611, -992.571186, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 10.73376647, 4.878e-05, 32.2012994, 0.00014634, 107.33766467, 0.0004878, -10.73376647, -4.878e-05, -32.2012994, -0.00014634, -107.33766467, -0.0004878, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 42.93506587, 0.02131829, 42.93506587, 0.06395488, 30.05454611, -992.571186, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 10.73376647, 4.878e-05, 32.2012994, 0.00014634, 107.33766467, 0.0004878, -10.73376647, -4.878e-05, -32.2012994, -0.00014634, -107.33766467, -0.0004878, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.65, 8.55)
    ops.node(124005, 0.0, 4.65, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.125, 27301843.93728144, 11375768.3072006, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 138.02194213, 0.00064997, 167.79555611, 0.01256004, 16.77955561, 0.05768957, -138.02194213, -0.00064997, -167.79555611, -0.01256004, -16.77955561, -0.05768957, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 60.0023008, 0.00108023, 72.94578872, 0.01080758, 7.29457887, 0.03872703, -60.0023008, -0.00108023, -72.94578872, -0.01080758, -7.29457887, -0.03872703, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 146.95908521, 0.01299941, 146.95908521, 0.03899822, 102.87135965, -2265.79423412, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 36.7397713, 8.526e-05, 110.21931391, 0.00025579, 367.39771303, 0.00085263, -36.7397713, -8.526e-05, -110.21931391, -0.00025579, -367.39771303, -0.00085263, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 86.23401207, 0.0216046, 86.23401207, 0.0648138, 60.36380845, -1057.6648869, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 21.55850302, 5.003e-05, 64.67550905, 0.00015009, 215.58503017, 0.00050031, -21.55850302, -5.003e-05, -64.67550905, -0.00015009, -215.58503017, -0.00050031, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 4.95, 4.65, 8.55)
    ops.node(124006, 4.95, 4.65, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.2625, 27340209.43542022, 11391753.93142509, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 375.77855566, 0.00054959, 458.23861564, 0.01124734, 45.82386156, 0.04325685, -375.77855566, -0.00054959, -458.23861564, -0.01124734, -45.82386156, -0.04325685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 148.13907787, 0.00077255, 180.64640715, 0.00978126, 18.06464071, 0.03107485, -148.13907787, -0.00077255, -180.64640715, -0.00978126, -18.06464071, -0.03107485, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 320.90331162, 0.01099181, 320.90331162, 0.03297544, 224.63231813, -2611.02531932, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 80.2258279, 8.853e-05, 240.67748371, 0.0002656, 802.25827904, 0.00088534, -80.2258279, -8.853e-05, -240.67748371, -0.0002656, -802.25827904, -0.00088534, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 171.81729515, 0.0154511, 171.81729515, 0.04635329, 120.27210661, -1193.47661525, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 42.95432379, 4.74e-05, 128.86297136, 0.00014221, 429.54323788, 0.00047402, -42.95432379, -4.74e-05, -128.86297136, -0.00014221, -429.54323788, -0.00047402, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 7.9, 4.65, 8.55)
    ops.node(124007, 7.9, 4.65, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.2625, 28891551.43561214, 12038146.43150506, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 381.89731359, 0.00055229, 464.28590669, 0.00954621, 46.42859067, 0.04241572, -381.89731359, -0.00055229, -464.28590669, -0.00954621, -46.42859067, -0.04241572, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 150.7738755, 0.00077701, 183.30106811, 0.0083509, 18.33010681, 0.03021659, -150.7738755, -0.00077701, -183.30106811, -0.0083509, -18.33010681, -0.03021659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 332.75142838, 0.01104585, 332.75142838, 0.03313756, 232.92599987, -2257.98748593, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 83.1878571, 8.687e-05, 249.56357129, 0.00026062, 831.87857096, 0.00086873, -83.1878571, -8.687e-05, -249.56357129, -0.00026062, -831.87857096, -0.00086873, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 165.55338227, 0.01554018, 165.55338227, 0.04662055, 115.88736759, -1080.83844913, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 41.38834557, 4.322e-05, 124.1650367, 0.00012967, 413.88345567, 0.00043222, -41.38834557, -4.322e-05, -124.1650367, -0.00012967, -413.88345567, -0.00043222, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 12.85, 4.65, 8.55)
    ops.node(124008, 12.85, 4.65, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.125, 27751050.16911313, 11562937.57046381, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 145.66776684, 0.0006464, 176.97811677, 0.0138137, 17.69781168, 0.0595484, -145.66776684, -0.0006464, -176.97811677, -0.0138137, -17.69781168, -0.0595484, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 63.75678537, 0.00103034, 77.46089646, 0.01178451, 7.74608965, 0.04007835, -63.75678537, -0.00103034, -77.46089646, -0.01178451, -7.74608965, -0.04007835, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 155.69640199, 0.01292809, 155.69640199, 0.03878428, 108.98748139, -2594.07726064, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 38.9241005, 8.887e-05, 116.77230149, 0.00026661, 389.24100497, 0.0008887, -38.9241005, -8.887e-05, -116.77230149, -0.00026661, -389.24100497, -0.0008887, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 103.41149344, 0.0206069, 103.41149344, 0.06182069, 72.38804541, -1168.79355262, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 25.85287336, 5.903e-05, 77.55862008, 0.00017708, 258.52873361, 0.00059026, -25.85287336, -5.903e-05, -77.55862008, -0.00017708, -258.52873361, -0.00059026, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 9.3, 8.55)
    ops.node(124009, 0.0, 9.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.125, 30534227.3739001, 12722594.73912504, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 139.40514288, 0.00062851, 168.45834148, 0.01375539, 16.84583415, 0.06270625, -139.40514288, -0.00062851, -168.45834148, -0.01375539, -16.84583415, -0.06270625, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 61.02373127, 0.00100749, 73.74158763, 0.01172866, 7.37415876, 0.04201218, -61.02373127, -0.00100749, -73.74158763, -0.01172866, -7.37415876, -0.04201218, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 165.3580686, 0.01257019, 165.3580686, 0.03771056, 115.75064802, -2506.65876016, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 41.33951715, 8.578e-05, 124.01855145, 0.00025734, 413.39517149, 0.00085781, -41.33951715, -8.578e-05, -124.01855145, -0.00025734, -413.39517149, -0.00085781, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 111.55955569, 0.02014985, 111.55955569, 0.06044956, 78.09168898, -1134.35478391, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 27.88988892, 5.787e-05, 83.66966676, 0.00017362, 278.89888922, 0.00057873, -27.88988892, -5.787e-05, -83.66966676, -0.00017362, -278.89888922, -0.00057873, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 4.95, 9.3, 8.55)
    ops.node(124010, 4.95, 9.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.2275, 27787165.49197738, 11577985.62165724, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 288.5205455, 0.00057235, 351.28809089, 0.01261323, 35.12880909, 0.0508205, -288.5205455, -0.00057235, -351.28809089, -0.01261323, -35.12880909, -0.0508205, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 126.497329, 0.00077341, 154.01677939, 0.01100508, 15.40167794, 0.03697146, -126.497329, -0.00077341, -154.01677939, -0.01100508, -15.40167794, -0.03697146, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 278.44221552, 0.01144707, 278.44221552, 0.03434122, 194.90955087, -3098.63186767, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 69.61055388, 8.721e-05, 208.83166164, 0.00026164, 696.10553881, 0.00087212, -69.61055388, -8.721e-05, -208.83166164, -0.00026164, -696.10553881, -0.00087212, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 173.7345732, 0.01546825, 173.7345732, 0.04640475, 121.61420124, -1537.79469811, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 43.4336433, 5.442e-05, 130.3009299, 0.00016325, 434.33643301, 0.00054416, -43.4336433, -5.442e-05, -130.3009299, -0.00016325, -434.33643301, -0.00054416, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.9, 9.3, 8.55)
    ops.node(124011, 7.9, 9.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.2275, 25392268.25933572, 10580111.77472322, 0.00616035, 0.00255464, 0.00881089, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 288.01393951, 0.00057939, 351.83442163, 0.01235228, 35.18344216, 0.04832776, -288.01393951, -0.00057939, -351.83442163, -0.01235228, -35.18344216, -0.04832776, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 125.80827681, 0.0007885, 153.68590278, 0.01079245, 15.36859028, 0.03524206, -125.80827681, -0.0007885, -153.68590278, -0.01079245, -15.36859028, -0.03524206, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 253.86057189, 0.01158784, 253.86057189, 0.03476351, 177.70240032, -3018.07681535, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 63.46514297, 8.701e-05, 190.39542891, 0.00026104, 634.65142971, 0.00087012, -63.46514297, -8.701e-05, -190.39542891, -0.00026104, -634.65142971, -0.00087012, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 157.69580862, 0.01577006, 157.69580862, 0.04731017, 110.38706603, -1507.19021298, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 39.42395215, 5.405e-05, 118.27185646, 0.00016215, 394.23952154, 0.00054051, -39.42395215, -5.405e-05, -118.27185646, -0.00016215, -394.23952154, -0.00054051, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 12.85, 9.3, 8.55)
    ops.node(124012, 12.85, 9.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.125, 27042734.91592156, 11267806.21496732, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 136.89458996, 0.00062486, 166.50524618, 0.0140916, 16.65052462, 0.05905457, -136.89458996, -0.00062486, -166.50524618, -0.0140916, -16.65052462, -0.05905457, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 59.8069175, 0.00099679, 72.74330946, 0.01199552, 7.27433095, 0.03981193, -59.8069175, -0.00099679, -72.74330946, -0.01199552, -7.27433095, -0.03981193, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 153.39666745, 0.01249729, 153.39666745, 0.03749188, 107.37766721, -2655.26672531, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 38.34916686, 8.985e-05, 115.04750059, 0.00026955, 383.49166862, 0.0008985, -38.34916686, -8.985e-05, -115.04750059, -0.00026955, -383.49166862, -0.0008985, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 99.81927354, 0.01993586, 99.81927354, 0.05980759, 69.87349148, -1184.15493315, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 24.95481838, 5.847e-05, 74.86445515, 0.0001754, 249.54818384, 0.00058468, -24.95481838, -5.847e-05, -74.86445515, -0.0001754, -249.54818384, -0.00058468, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 13.95, 8.5)
    ops.node(124013, 0.0, 13.95, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 29380084.67565384, 12241701.9481891, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 43.07645319, 0.00105475, 52.18744699, 0.01236626, 5.2187447, 0.06012271, -43.07645319, -0.00105475, -52.18744699, -0.01236626, -5.2187447, -0.06012271, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 43.07645319, 0.00105475, 52.18744699, 0.01236626, 5.2187447, 0.06012271, -43.07645319, -0.00105475, -52.18744699, -0.01236626, -5.2187447, -0.06012271, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 44.8089968, 0.02109504, 44.8089968, 0.06328513, 31.36629776, -951.93066545, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 11.2022492, 4.832e-05, 33.6067476, 0.00014495, 112.022492, 0.00048317, -11.2022492, -4.832e-05, -33.6067476, -0.00014495, -112.022492, -0.00048317, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 44.8089968, 0.02109504, 44.8089968, 0.06328513, 31.36629776, -951.93066545, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 11.2022492, 4.832e-05, 33.6067476, 0.00014495, 112.022492, 0.00048317, -11.2022492, -4.832e-05, -33.6067476, -0.00014495, -112.022492, -0.00048317, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.95, 13.95, 8.5)
    ops.node(124014, 4.95, 13.95, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.105, 27212692.94175111, 11338622.05906296, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 67.93646169, 0.00087786, 82.66714265, 0.01197611, 8.26671426, 0.0530271, -67.93646169, -0.00087786, -82.66714265, -0.01197611, -8.26671426, -0.0530271, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 69.33306057, 0.00078401, 84.36656643, 0.01243728, 8.43665664, 0.05852618, -69.33306057, -0.00078401, -84.36656643, -0.01243728, -8.43665664, -0.05852618, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 104.35894198, 0.01755721, 104.35894198, 0.05267163, 73.05125939, -1599.48816199, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 26.0897355, 7.232e-05, 78.26920649, 0.00021695, 260.89735495, 0.00072316, -26.0897355, -7.232e-05, -78.26920649, -0.00021695, -260.89735495, -0.00072316, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 111.78009416, 0.01568021, 111.78009416, 0.04704062, 78.24606591, -1946.7861247, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 27.94502354, 7.746e-05, 83.83507062, 0.00023238, 279.45023539, 0.00077458, -27.94502354, -7.746e-05, -83.83507062, -0.00023238, -279.45023539, -0.00077458, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.9, 13.95, 8.5)
    ops.node(124015, 7.9, 13.95, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.105, 24593834.09550582, 10247430.87312743, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 65.97275819, 0.00089171, 80.46916069, 0.01045393, 8.04691607, 0.0478785, -65.97275819, -0.00089171, -80.46916069, -0.01045393, -8.04691607, -0.0478785, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 67.58948695, 0.00079369, 82.44113838, 0.01083411, 8.24411384, 0.05285154, -67.58948695, -0.00079369, -82.44113838, -0.01083411, -8.24411384, -0.05285154, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 92.38238106, 0.01783411, 92.38238106, 0.05350233, 64.66766674, -1409.66888847, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 23.09559527, 7.083e-05, 69.2867858, 0.0002125, 230.95595265, 0.00070834, -23.09559527, -7.083e-05, -69.2867858, -0.0002125, -230.95595265, -0.00070834, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 99.07017582, 0.01587372, 99.07017582, 0.04762116, 69.34912307, -1702.91147826, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 24.76754395, 7.596e-05, 74.30263186, 0.00022788, 247.67543955, 0.00075961, -24.76754395, -7.596e-05, -74.30263186, -0.00022788, -247.67543955, -0.00075961, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.85, 13.95, 8.5)
    ops.node(124016, 12.85, 13.95, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 26493722.11040679, 11039050.87933616, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 45.91574484, 0.00109113, 55.87925521, 0.01416799, 5.58792552, 0.05824125, -45.91574484, -0.00109113, -55.87925521, -0.01416799, -5.58792552, -0.05824125, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 45.91574484, 0.00109113, 55.87925521, 0.01416799, 5.58792552, 0.05824125, -45.91574484, -0.00109113, -55.87925521, -0.01416799, -5.58792552, -0.05824125, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 60.42585531, 0.02182255, 60.42585531, 0.06546766, 42.29809871, -1227.74804008, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 15.10646383, 7.225e-05, 45.31939148, 0.00021676, 151.06463826, 0.00072255, -15.10646383, -7.225e-05, -45.31939148, -0.00021676, -151.06463826, -0.00072255, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 60.42585531, 0.02182255, 60.42585531, 0.06546766, 42.29809871, -1227.74804008, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 15.10646383, 7.225e-05, 45.31939148, 0.00021676, 151.06463826, 0.00072255, -15.10646383, -7.225e-05, -45.31939148, -0.00021676, -151.06463826, -0.00072255, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.95, 0.0, 0.0)
    ops.node(124017, 4.95, 0.0, 1.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 170002, 124017, 0.175, 25230855.28809975, 10512856.37004156, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 260.58743594, 0.00066001, 310.6697828, 0.00810676, 31.06697828, 0.02175077, -260.58743594, -0.00066001, -310.6697828, -0.00810676, -31.06697828, -0.02175077, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 308.48675853, 0.00060081, 367.77488494, 0.00881913, 36.77748849, 0.0260579, -308.48675853, -0.00060081, -367.77488494, -0.00881913, -36.77748849, -0.0260579, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 247.67900837, 0.01320015, 247.67900837, 0.03960044, 173.37530586, -4256.12483596, 0.05, 2, 0, 70002, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 61.91975209, 5.553e-05, 185.75925628, 0.0001666, 619.19752093, 0.00055533, -61.91975209, -5.553e-05, -185.75925628, -0.0001666, -619.19752093, -0.00055533, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 313.02988842, 0.01201618, 313.02988842, 0.03604855, 219.12092189, -5139.31978703, 0.05, 2, 0, 70002, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 78.2574721, 7.019e-05, 234.77241631, 0.00021056, 782.57472105, 0.00070186, -78.2574721, -7.019e-05, -234.77241631, -0.00021056, -782.57472105, -0.00070186, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 4.95, 0.0, 1.6)
    ops.node(121002, 4.95, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 174017, 121002, 0.175, 32076504.83906619, 13365210.34961091, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 190.77186966, 0.00067528, 227.55138186, 0.01315289, 22.75513819, 0.04436081, -190.77186966, -0.00067528, -227.55138186, -0.01315289, -22.75513819, -0.04436081, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 257.31827079, 0.00060064, 306.92747416, 0.01455541, 30.69274742, 0.05524911, -257.31827079, -0.00060064, -306.92747416, -0.01455541, -30.69274742, -0.05524911, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 322.91840202, 0.01350555, 322.91840202, 0.04051665, 226.04288141, -4904.01260815, 0.05, 2, 0, 74017, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 80.72960051, 5.695e-05, 242.18880152, 0.00017085, 807.29600505, 0.00056951, -80.72960051, -5.695e-05, -242.18880152, -0.00017085, -807.29600505, -0.00056951, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 408.77877319, 0.01201288, 408.77877319, 0.03603863, 286.14514123, -6271.58802126, 0.05, 2, 0, 74017, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 102.1946933, 7.209e-05, 306.58407989, 0.00021628, 1021.94693298, 0.00072094, -102.1946933, -7.209e-05, -306.58407989, -0.00021628, -1021.94693298, -0.00072094, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 7.9, 0.0, 0.0)
    ops.node(124018, 7.9, 0.0, 1.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 170003, 124018, 0.175, 30916043.81580766, 12881684.92325319, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 265.24465588, 0.00064296, 316.7117734, 0.00824343, 31.67117734, 0.03020752, -265.24465588, -0.00064296, -316.7117734, -0.00824343, -31.67117734, -0.03020752, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 316.23150196, 0.00058908, 377.59192342, 0.00897705, 37.75919234, 0.03672797, -316.23150196, -0.00058908, -377.59192342, -0.00897705, -37.75919234, -0.03672797, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 294.25315542, 0.01285925, 294.25315542, 0.03857774, 205.97720879, -4015.71853813, 0.05, 2, 0, 70003, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 73.56328885, 5.384e-05, 220.68986656, 0.00016153, 735.63288855, 0.00053844, -73.56328885, -5.384e-05, -220.68986656, -0.00016153, -735.63288855, -0.00053844, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 369.09514559, 0.01178165, 369.09514559, 0.03534495, 258.36660191, -4763.57292938, 0.05, 2, 0, 70003, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 92.2737864, 6.754e-05, 276.82135919, 0.00020262, 922.73786398, 0.00067539, -92.2737864, -6.754e-05, -276.82135919, -0.00020262, -922.73786398, -0.00067539, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 7.9, 0.0, 1.6)
    ops.node(121003, 7.9, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4044, 174018, 121003, 0.175, 29033909.31000108, 12097462.21250045, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24044, 193.52465977, 0.00063867, 231.7534337, 0.01368917, 23.17534337, 0.0402588, -193.52465977, -0.00063867, -231.7534337, -0.01368917, -23.17534337, -0.0402588, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14044, 255.78576223, 0.00058277, 306.31356624, 0.01517825, 30.63135662, 0.04982383, -255.78576223, -0.00058277, -306.31356624, -0.01517825, -30.63135662, -0.04982383, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24044, 4044, 0.0, 298.93655547, 0.01277337, 298.93655547, 0.03832012, 209.25558883, -5134.77429598, 0.05, 2, 0, 74018, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44044, 74.73413887, 5.825e-05, 224.2024166, 0.00017474, 747.34138868, 0.00058247, -74.73413887, -5.825e-05, -224.2024166, -0.00017474, -747.34138868, -0.00058247, 0.4, 0.3, 0.003, 0.0, 0.0, 24044, 2)
    ops.limitCurve('ThreePoint', 14044, 4044, 0.0, 380.27652661, 0.01165537, 380.27652661, 0.03496611, 266.19356863, -6645.51848916, 0.05, 2, 0, 74018, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34044, 95.06913165, 7.41e-05, 285.20739496, 0.00022229, 950.69131652, 0.00074095, -95.06913165, -7.41e-05, -285.20739496, -0.00022229, -950.69131652, -0.00074095, 0.4, 0.3, 0.003, 0.0, 0.0, 14044, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4044, 99999, 'P', 44044, 'Vy', 34044, 'Vz', 24044, 'My', 14044, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4044, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4044, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.95, 0.0, 3.0)
    ops.node(124019, 4.95, 0.0, 3.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 171002, 124019, 0.175, 28033352.68480995, 11680563.61867081, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 154.12951023, 0.00062099, 185.46128366, 0.00941215, 18.54612837, 0.03108509, -154.12951023, -0.00062099, -185.46128366, -0.00941215, -18.54612837, -0.03108509, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 225.70034908, 0.00057049, 271.58119429, 0.01027251, 27.15811943, 0.03765556, -225.70034908, -0.00057049, -271.58119429, -0.01027251, -27.15811943, -0.03765556, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 252.59157837, 0.01241987, 252.59157837, 0.0372596, 176.81410486, -3675.66067738, 0.05, 2, 0, 71002, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 63.14789459, 5.097e-05, 189.44368377, 0.00015292, 631.47894592, 0.00050973, -63.14789459, -5.097e-05, -189.44368377, -0.00015292, -631.47894592, -0.00050973, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 319.02856065, 0.01140975, 319.02856065, 0.03422924, 223.31999245, -4636.534525, 0.05, 2, 0, 71002, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 79.75714016, 6.438e-05, 239.27142048, 0.00019314, 797.57140162, 0.0006438, -79.75714016, -6.438e-05, -239.27142048, -0.00019314, -797.57140162, -0.0006438, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 4.95, 0.0, 4.325)
    ops.node(122002, 4.95, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 122002, 0.175, 28825276.99785455, 12010532.0824394, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 156.76720202, 0.00062253, 188.76531892, 0.00854407, 18.87653189, 0.03206722, -156.76720202, -0.00062253, -188.76531892, -0.00854407, -18.87653189, -0.03206722, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 211.62768607, 0.00057211, 254.8235035, 0.00931441, 25.48235035, 0.03903515, -211.62768607, -0.00057211, -254.8235035, -0.00931441, -25.48235035, -0.03903515, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 250.47839108, 0.01245063, 250.47839108, 0.03735189, 175.33487376, -3353.14302179, 0.05, 2, 0, 74019, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 62.61959777, 4.916e-05, 187.85879331, 0.00014747, 626.19597771, 0.00049158, -62.61959777, -4.916e-05, -187.85879331, -0.00014747, -626.19597771, -0.00049158, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 315.6044941, 0.01144212, 315.6044941, 0.03432635, 220.92314587, -4220.90805598, 0.05, 2, 0, 74019, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 78.90112353, 6.194e-05, 236.70337058, 0.00018582, 789.01123526, 0.00061939, -78.90112353, -6.194e-05, -236.70337058, -0.00018582, -789.01123526, -0.00061939, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.9, 0.0, 3.0)
    ops.node(124020, 7.9, 0.0, 3.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 171003, 124020, 0.175, 26061990.11829871, 10859162.54929113, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 156.97753913, 0.00061517, 188.87027136, 0.00906007, 18.88702714, 0.02792224, -156.97753913, -0.00061517, -188.87027136, -0.00906007, -18.88702714, -0.02792224, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 229.11198278, 0.00056976, 275.66008869, 0.00988964, 27.56600887, 0.03372139, -229.11198278, -0.00056976, -275.66008869, -0.00988964, -27.56600887, -0.03372139, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 236.96575237, 0.01230331, 236.96575237, 0.03690994, 165.87602666, -3743.45261774, 0.05, 2, 0, 71003, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 59.24143809, 5.144e-05, 177.72431427, 0.00015431, 592.41438091, 0.00051437, -59.24143809, -5.144e-05, -177.72431427, -0.00015431, -592.41438091, -0.00051437, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 300.13030992, 0.0113951, 300.13030992, 0.03418531, 210.09121695, -4745.43965992, 0.05, 2, 0, 71003, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 75.03257748, 6.515e-05, 225.09773244, 0.00019544, 750.32577481, 0.00065148, -75.03257748, -6.515e-05, -225.09773244, -0.00019544, -750.32577481, -0.00065148, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 7.9, 0.0, 4.325)
    ops.node(122003, 7.9, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 122003, 0.175, 26715323.71560545, 11131384.88150227, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 163.88378653, 0.00061523, 197.55251475, 0.00922628, 19.75525148, 0.0300485, -163.88378653, -0.00061523, -197.55251475, -0.00922628, -19.75525148, -0.0300485, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 217.54010109, 0.000572, 262.23212765, 0.01007525, 26.22321277, 0.03638345, -217.54010109, -0.000572, -262.23212765, -0.01007525, -26.22321277, -0.03638345, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 236.72722836, 0.0123046, 236.72722836, 0.03691381, 165.70905985, -3571.47218488, 0.05, 2, 0, 74020, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 59.18180709, 5.013e-05, 177.54542127, 0.00015039, 591.81807089, 0.00050129, -59.18180709, -5.013e-05, -177.54542127, -0.00015039, -591.81807089, -0.00050129, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 299.6342664, 0.01143993, 299.6342664, 0.0343198, 209.74398648, -4572.35365039, 0.05, 2, 0, 74020, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 74.9085666, 6.345e-05, 224.7256998, 0.00019035, 749.08566599, 0.00063449, -74.9085666, -6.345e-05, -224.7256998, -0.00019035, -749.08566599, -0.00063449, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.95, 0.0, 5.75)
    ops.node(124021, 4.95, 0.0, 6.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 172002, 124021, 0.12, 27702802.19409181, 11542834.24753826, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 88.76610641, 0.00067388, 106.90955963, 0.00877313, 10.69095596, 0.03385244, -88.76610641, -0.00067388, -106.90955963, -0.00877313, -10.69095596, -0.03385244, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 121.61313251, 0.00060166, 146.47039245, 0.00941704, 14.64703924, 0.040079, -121.61313251, -0.00060166, -146.47039245, -0.00941704, -14.64703924, -0.040079, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 146.14851474, 0.01347769, 146.14851474, 0.04043307, 102.30396032, -2671.25211683, 0.05, 2, 0, 72002, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 36.53712869, 4.352e-05, 109.61138606, 0.00013057, 365.37128686, 0.00043524, -36.53712869, -4.352e-05, -109.61138606, -0.00013057, -365.37128686, -0.00043524, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 204.75122003, 0.01203322, 204.75122003, 0.03609966, 143.32585402, -3278.16146054, 0.05, 2, 0, 72002, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 51.18780501, 6.098e-05, 153.56341502, 0.00018293, 511.87805006, 0.00060976, -51.18780501, -6.098e-05, -153.56341502, -0.00018293, -511.87805006, -0.00060976, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 4.95, 0.0, 7.075)
    ops.node(123002, 4.95, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 123002, 0.12, 27000677.76734246, 11250282.40305936, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 108.88015406, 0.00064906, 131.47455366, 0.01036131, 13.14745537, 0.03613755, -108.88015406, -0.00064906, -131.47455366, -0.01036131, -13.14745537, -0.03613755, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 134.15804975, 0.00058737, 161.99802308, 0.01115837, 16.19980231, 0.04267239, -134.15804975, -0.00058737, -161.99802308, -0.01115837, -16.19980231, -0.04267239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 147.05834467, 0.01298129, 147.05834467, 0.03894387, 102.94084127, -2637.04174108, 0.05, 2, 0, 74021, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 36.76458617, 4.493e-05, 110.29375851, 0.0001348, 367.64586169, 0.00044933, -36.76458617, -4.493e-05, -110.29375851, -0.0001348, -367.64586169, -0.00044933, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 196.0777929, 0.0117474, 196.0777929, 0.0352422, 137.25445503, -3318.92904798, 0.05, 2, 0, 74021, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 49.01944822, 5.991e-05, 147.05834467, 0.00017973, 490.19448225, 0.00059911, -49.01944822, -5.991e-05, -147.05834467, -0.00017973, -490.19448225, -0.00059911, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.9, 0.0, 5.75)
    ops.node(124022, 7.9, 0.0, 6.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 172003, 124022, 0.12, 24943545.87512372, 10393144.11463489, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 90.61099255, 0.00067066, 109.01747732, 0.00992511, 10.90174773, 0.03025282, -90.61099255, -0.00067066, -109.01747732, -0.00992511, -10.90174773, -0.03025282, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 123.8464374, 0.00060302, 149.00428524, 0.01067574, 14.90042852, 0.03552841, -123.8464374, -0.00060302, -149.00428524, -0.01067574, -14.90042852, -0.03552841, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 146.07455682, 0.01341324, 146.07455682, 0.04023971, 102.25218978, -2994.98453719, 0.05, 2, 0, 72003, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 36.51863921, 4.831e-05, 109.55591762, 0.00014494, 365.18639206, 0.00048314, -36.51863921, -4.831e-05, -109.55591762, -0.00014494, -365.18639206, -0.00048314, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 194.76607576, 0.01206047, 194.76607576, 0.03618141, 136.33625303, -3759.11519335, 0.05, 2, 0, 72003, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 48.69151894, 6.442e-05, 146.07455682, 0.00019325, 486.91518941, 0.00064418, -48.69151894, -6.442e-05, -146.07455682, -0.00019325, -486.91518941, -0.00064418, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 7.9, 0.0, 7.075)
    ops.node(123003, 7.9, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 123003, 0.12, 31353794.47060417, 13064081.02941841, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 102.36956791, 0.00069573, 122.89657923, 0.00953857, 12.28965792, 0.0405877, -102.36956791, -0.00069573, -122.89657923, -0.00953857, -12.28965792, -0.0405877, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 130.29988687, 0.00061022, 156.42744906, 0.01023495, 15.64274491, 0.04819561, -130.29988687, -0.00061022, -156.42744906, -0.01023495, -15.64274491, -0.04819561, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 160.78525653, 0.01391459, 160.78525653, 0.04174377, 112.54967957, -2548.24758053, 0.05, 2, 0, 74022, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 40.19631413, 4.231e-05, 120.5889424, 0.00012692, 401.96314134, 0.00042307, -40.19631413, -4.231e-05, -120.5889424, -0.00012692, -401.96314134, -0.00042307, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 223.84292072, 0.01220444, 223.84292072, 0.03661331, 156.6900445, -3186.32338162, 0.05, 2, 0, 74022, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 55.96073018, 5.89e-05, 167.88219054, 0.0001767, 559.60730179, 0.00058899, -55.96073018, -5.89e-05, -167.88219054, -0.0001767, -559.60730179, -0.00058899, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.95, 0.0, 8.5)
    ops.node(124023, 4.95, 0.0, 9.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 173002, 124023, 0.12, 27359386.6769002, 11399744.44870842, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 60.71603572, 0.00064613, 73.89593172, 0.01145908, 7.38959317, 0.04489079, -60.71603572, -0.00064613, -73.89593172, -0.01145908, -7.38959317, -0.04489079, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 84.22699279, 0.00057624, 102.5105153, 0.01234526, 10.25105153, 0.05321887, -84.22699279, -0.00057624, -102.5105153, -0.01234526, -10.25105153, -0.05321887, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 132.68567462, 0.0129226, 132.68567462, 0.03876781, 92.87997223, -2574.43821148, 0.05, 2, 0, 73002, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 33.17141865, 4.001e-05, 99.51425596, 0.00012003, 331.71418654, 0.0004001, -33.17141865, -4.001e-05, -99.51425596, -0.00012003, -331.71418654, -0.0004001, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 176.91423282, 0.01152476, 176.91423282, 0.03457428, 123.83996298, -3622.95794618, 0.05, 2, 0, 73002, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 44.22855821, 5.335e-05, 132.68567462, 0.00016004, 442.28558206, 0.00053347, -44.22855821, -5.335e-05, -132.68567462, -0.00016004, -442.28558206, -0.00053347, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 4.95, 0.0, 9.825)
    ops.node(124002, 4.95, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 124002, 0.12, 27619262.23555664, 11508025.93148193, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 69.11865001, 0.00065497, 84.27792514, 0.01220296, 8.42779251, 0.04818899, -69.11865001, -0.00065497, -84.27792514, -0.01220296, -8.42779251, -0.04818899, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 90.35961322, 0.0005842, 110.17750951, 0.01315325, 11.01775095, 0.05714977, -90.35961322, -0.0005842, -110.17750951, -0.01315325, -11.01775095, -0.05714977, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 129.47418322, 0.01309945, 129.47418322, 0.03929836, 90.63192825, -2918.89722343, 0.05, 2, 0, 74023, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 32.3685458, 3.867e-05, 97.10563741, 0.00011602, 323.68545804, 0.00038675, -32.3685458, -3.867e-05, -97.10563741, -0.00011602, -323.68545804, -0.00038675, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 172.63224429, 0.01168394, 172.63224429, 0.03505181, 120.842571, -4342.18821679, 0.05, 2, 0, 74023, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 43.15806107, 5.157e-05, 129.47418322, 0.0001547, 431.58061073, 0.00051566, -43.15806107, -5.157e-05, -129.47418322, -0.0001547, -431.58061073, -0.00051566, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.9, 0.0, 8.5)
    ops.node(124024, 7.9, 0.0, 9.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 173003, 124024, 0.12, 26854748.06555718, 11189478.36064883, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 63.63327283, 0.00063027, 77.50170724, 0.01029668, 7.75017072, 0.04327294, -63.63327283, -0.00063027, -77.50170724, -0.01029668, -7.75017072, -0.04327294, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 87.85079701, 0.00056974, 106.99727436, 0.01109085, 10.69972744, 0.05140762, -87.85079701, -0.00056974, -106.99727436, -0.01109085, -10.69972744, -0.05140762, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 121.14076856, 0.01260532, 121.14076856, 0.03781595, 84.79853799, -2339.80426957, 0.05, 2, 0, 73003, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 30.28519214, 3.722e-05, 90.85557642, 0.00011165, 302.8519214, 0.00037215, -30.28519214, -3.722e-05, -90.85557642, -0.00011165, -302.8519214, -0.00037215, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 169.55911203, 0.01139479, 169.55911203, 0.03418438, 118.69137842, -3252.93197043, 0.05, 2, 0, 73003, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 42.38977801, 5.209e-05, 127.16933402, 0.00015627, 423.89778007, 0.0005209, -42.38977801, -5.209e-05, -127.16933402, -0.00015627, -423.89778007, -0.0005209, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 7.9, 0.0, 9.825)
    ops.node(124003, 7.9, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 124003, 0.12, 26556215.30374904, 11065089.70989543, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 69.3998799, 0.00062123, 84.77408107, 0.01351011, 8.47740811, 0.04879571, -69.3998799, -0.00062123, -84.77408107, -0.01351011, -8.47740811, -0.04879571, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 89.69245943, 0.00056324, 109.56208914, 0.01459174, 10.95620891, 0.05773192, -89.69245943, -0.00056324, -109.56208914, -0.01459174, -10.95620891, -0.05773192, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 128.63610096, 0.01242464, 128.63610096, 0.03727393, 90.04527067, -3343.56063883, 0.05, 2, 0, 74024, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 32.15902524, 3.996e-05, 96.47707572, 0.00011989, 321.5902524, 0.00039962, -32.15902524, -3.996e-05, -96.47707572, -0.00011989, -321.5902524, -0.00039962, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 171.51480128, 0.01126476, 171.51480128, 0.03379428, 120.06036089, -5034.97575992, 0.05, 2, 0, 74024, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 42.87870032, 5.328e-05, 128.63610096, 0.00015985, 428.7870032, 0.00053283, -42.87870032, -5.328e-05, -128.63610096, -0.00015985, -428.7870032, -0.00053283, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4059, '-orient', 0, 0, 1, 0, 1, 0)
