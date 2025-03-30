import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.075, 26164800.56154356, 10902000.23397648, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 92.75346483, 0.00129571, 109.87561633, 0.01259785, 10.98756163, 0.0294397, -92.75346483, -0.00129571, -109.87561633, -0.01259785, -10.98756163, -0.0294397, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 103.13870099, 0.00109894, 122.17795161, 0.01306999, 12.21779516, 0.03237301, -103.13870099, -0.00109894, -122.17795161, -0.01306999, -12.21779516, -0.03237301, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 93.2634903, 0.02591429, 93.2634903, 0.07774286, 65.28444321, -1700.19965789, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 23.31587258, 7.87e-05, 69.94761773, 0.00023611, 233.15872576, 0.00078703, -23.31587258, -7.87e-05, -69.94761773, -0.00023611, -233.15872576, -0.00078703, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 103.16596485, 0.02197883, 103.16596485, 0.0659365, 72.2161754, -1911.64038152, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 25.79149121, 8.706e-05, 77.37447364, 0.00026118, 257.91491214, 0.0008706, -25.79149121, -8.706e-05, -77.37447364, -0.00026118, -257.91491214, -0.0008706, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.8, 0.0, 0.0)
    ops.node(121004, 13.8, 0.0, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.075, 27840449.32158704, 11600187.21732793, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 93.09378533, 0.00128025, 110.61437573, 0.0133714, 11.06143757, 0.03406103, -93.09378533, -0.00128025, -110.61437573, -0.0133714, -11.06143757, -0.03406103, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 103.87802318, 0.00108511, 123.42824653, 0.01389187, 12.34282465, 0.03760497, -103.87802318, -0.00108511, -123.42824653, -0.01389187, -12.34282465, -0.03760497, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 95.23464983, 0.02560496, 95.23464983, 0.07681487, 66.66425488, -1677.59417985, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 23.80866246, 7.553e-05, 71.42598738, 0.00022659, 238.08662459, 0.0007553, -23.80866246, -7.553e-05, -71.42598738, -0.00022659, -238.08662459, -0.0007553, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 106.39134291, 0.02170214, 106.39134291, 0.06510641, 74.47394004, -1882.88913658, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 26.59783573, 8.438e-05, 79.79350718, 0.00025313, 265.97835727, 0.00084378, -26.59783573, -8.438e-05, -79.79350718, -0.00025313, -265.97835727, -0.00084378, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.45, 0.0)
    ops.node(121005, 0.0, 4.45, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.135, 27601235.31822017, 11500514.71592507, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 232.20570582, 0.00080511, 277.14351541, 0.01362457, 27.71435154, 0.03685312, -232.20570582, -0.00080511, -277.14351541, -0.01362457, -27.71435154, -0.03685312, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 176.71138058, 0.00107998, 210.909603, 0.01248244, 21.0909603, 0.03007591, -176.71138058, -0.00107998, -210.909603, -0.01248244, -21.0909603, -0.03007591, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 199.99333617, 0.01610228, 199.99333617, 0.04830683, 139.99533532, -2868.8964581, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 49.99833404, 8.888e-05, 149.99500213, 0.00026665, 499.98334043, 0.00088882, -49.99833404, -8.888e-05, -149.99500213, -0.00026665, -499.98334043, -0.00088882, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 151.36704596, 0.02159957, 151.36704596, 0.06479871, 105.95693217, -2261.02269587, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 37.84176149, 6.727e-05, 113.52528447, 0.00020181, 378.41761491, 0.00067271, -37.84176149, -6.727e-05, -113.52528447, -0.00020181, -378.41761491, -0.00067271, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 5.45, 4.45, 0.0)
    ops.node(121006, 5.45, 4.45, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.22, 27569694.28155567, 11487372.61731486, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 410.09554965, 0.00070768, 493.23332551, 0.01482534, 49.32333255, 0.03865827, -410.09554965, -0.00070768, -493.23332551, -0.01482534, -49.32333255, -0.03865827, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 391.4328017, 0.00084265, 470.78711939, 0.01381784, 47.07871194, 0.03332718, -391.4328017, -0.00084265, -470.78711939, -0.01381784, -47.07871194, -0.03332718, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 321.80497559, 0.01415355, 321.80497559, 0.04246066, 225.26348292, -3470.26360517, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 80.4512439, 8.786e-05, 241.3537317, 0.00026358, 804.51243899, 0.00087861, -80.4512439, -8.786e-05, -241.3537317, -0.00026358, -804.51243899, -0.00087861, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 234.03998225, 0.01685291, 234.03998225, 0.05055872, 163.82798758, -2834.38681229, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 58.50999556, 6.39e-05, 175.52998669, 0.0001917, 585.09995563, 0.00063899, -58.50999556, -6.39e-05, -175.52998669, -0.0001917, -585.09995563, -0.00063899, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 8.35, 4.45, 0.0)
    ops.node(121007, 8.35, 4.45, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.22, 27373518.03730932, 11405632.51554555, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 410.34576982, 0.00070701, 493.54614882, 0.01483474, 49.35461488, 0.03835246, -410.34576982, -0.00070701, -493.54614882, -0.01483474, -49.35461488, -0.03835246, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 393.26494061, 0.00084059, 473.00206601, 0.01382503, 47.3002066, 0.03307635, -393.26494061, -0.00084059, -473.00206601, -0.01382503, -47.3002066, -0.03307635, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 320.65051448, 0.01414027, 320.65051448, 0.0424208, 224.45536013, -3497.6054037, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 80.16262862, 8.817e-05, 240.48788586, 0.00026452, 801.62628619, 0.00088174, -80.16262862, -8.817e-05, -240.48788586, -0.00026452, -801.62628619, -0.00088174, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 233.20037416, 0.0168118, 233.20037416, 0.05043541, 163.24026192, -2852.35094632, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 58.30009354, 6.413e-05, 174.90028062, 0.00019238, 583.00093541, 0.00064126, -58.30009354, -6.413e-05, -174.90028062, -0.00019238, -583.00093541, -0.00064126, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 13.8, 4.45, 0.0)
    ops.node(121008, 13.8, 4.45, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.135, 27058245.626104, 11274269.01087667, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 232.02871151, 0.00080009, 276.79302577, 0.01345778, 27.67930258, 0.03547927, -232.02871151, -0.00080009, -276.79302577, -0.01345778, -27.67930258, -0.03547927, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 177.9962487, 0.00106596, 212.3363093, 0.01232454, 21.23363093, 0.02900377, -177.9962487, -0.00106596, -212.3363093, -0.01232454, -21.23363093, -0.02900377, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 196.65770292, 0.01600186, 196.65770292, 0.04800557, 137.66039205, -2857.438445, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 49.16442573, 8.915e-05, 147.49327719, 0.00026746, 491.64425731, 0.00089153, -49.16442573, -8.915e-05, -147.49327719, -0.00026746, -491.64425731, -0.00089153, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 148.75274053, 0.02131919, 148.75274053, 0.06395756, 104.12691837, -2254.23970433, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 37.18818513, 6.744e-05, 111.5645554, 0.00020231, 371.88185132, 0.00067436, -37.18818513, -6.744e-05, -111.5645554, -0.00020231, -371.88185132, -0.00067436, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.9, 0.0)
    ops.node(121009, 0.0, 8.9, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.135, 27990151.46102585, 11662563.10876077, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 253.01906231, 0.00081187, 302.05496899, 0.01413905, 30.2054969, 0.03820737, -253.01906231, -0.00081187, -302.05496899, -0.01413905, -30.2054969, -0.03820737, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 184.58861502, 0.00109055, 220.3624813, 0.01294462, 22.03624813, 0.03117414, -184.58861502, -0.00109055, -220.3624813, -0.01294462, -22.03624813, -0.03117414, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 202.36863088, 0.01623737, 202.36863088, 0.04871211, 141.65804162, -2876.27599881, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 50.59215772, 8.869e-05, 151.77647316, 0.00026606, 505.92157721, 0.00088688, -50.59215772, -8.869e-05, -151.77647316, -0.00026606, -505.92157721, -0.00088688, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 153.23211058, 0.02181108, 153.23211058, 0.06543325, 107.26247741, -2265.38949915, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 38.30802765, 6.715e-05, 114.92408294, 0.00020146, 383.08027645, 0.00067154, -38.30802765, -6.715e-05, -114.92408294, -0.00020146, -383.08027645, -0.00067154, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 5.45, 8.9, 0.0)
    ops.node(121010, 5.45, 8.9, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.175, 27302653.53285908, 11376105.63869128, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 343.64719429, 0.00074806, 412.52934292, 0.01526789, 41.25293429, 0.03946902, -343.64719429, -0.00074806, -412.52934292, -0.01526789, -41.25293429, -0.03946902, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 280.42913406, 0.0009381, 336.63957784, 0.01409475, 33.66395778, 0.03324928, -280.42913406, -0.0009381, -336.63957784, -0.01409475, -33.66395778, -0.03324928, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 252.07736829, 0.01496128, 252.07736829, 0.04488383, 176.4541578, -3173.29722999, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 63.01934207, 8.737e-05, 189.05802621, 0.0002621, 630.19342071, 0.00087368, -63.01934207, -8.737e-05, -189.05802621, -0.0002621, -630.19342071, -0.00087368, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 179.81570176, 0.01876202, 179.81570176, 0.05628606, 125.87099123, -2513.28926307, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 44.95392544, 6.232e-05, 134.86177632, 0.00018697, 449.53925441, 0.00062323, -44.95392544, -6.232e-05, -134.86177632, -0.00018697, -449.53925441, -0.00062323, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.35, 8.9, 0.0)
    ops.node(121011, 8.35, 8.9, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.175, 27223283.14499593, 11343034.6437483, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 346.96140741, 0.00074237, 416.50017319, 0.01495051, 41.65001732, 0.03900379, -346.96140741, -0.00074237, -416.50017319, -0.01495051, -41.65001732, -0.03900379, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 285.95303607, 0.00092398, 343.26437035, 0.0137982, 34.32643703, 0.03283572, -285.95303607, -0.00092398, -343.26437035, -0.0137982, -34.32643703, -0.03283572, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 249.66963454, 0.01484748, 249.66963454, 0.04454243, 174.76874418, -3115.69741545, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 62.41740864, 8.679e-05, 187.25222591, 0.00026036, 624.17408635, 0.00086786, -62.41740864, -8.679e-05, -187.25222591, -0.00026036, -624.17408635, -0.00086786, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 178.11906665, 0.01847969, 178.11906665, 0.05543907, 124.68334666, -2477.37150014, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 44.52976666, 6.191e-05, 133.58929999, 0.00018574, 445.29766663, 0.00061914, -44.52976666, -6.191e-05, -133.58929999, -0.00018574, -445.29766663, -0.00061914, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 13.8, 8.9, 0.0)
    ops.node(121012, 13.8, 8.9, 1.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.135, 27994260.73399261, 11664275.30583026, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 250.95870895, 0.00080796, 299.59588371, 0.01437367, 29.95958837, 0.03845076, -250.95870895, -0.00080796, -299.59588371, -0.01437367, -29.95958837, -0.03845076, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 182.68295743, 0.00108689, 218.08791694, 0.01315312, 21.80879169, 0.03138928, -182.68295743, -0.00108689, -218.08791694, -0.01315312, -21.80879169, -0.03138928, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 204.29658374, 0.01615928, 204.29658374, 0.04847783, 143.00760862, -2934.81634453, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 51.07414594, 8.952e-05, 153.22243781, 0.00026856, 510.74145935, 0.0008952, -51.07414594, -8.952e-05, -153.22243781, -0.00026856, -510.74145935, -0.0008952, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 154.52039525, 0.02173778, 154.52039525, 0.06521333, 108.16427667, -2299.98149065, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 38.63009881, 6.771e-05, 115.89029643, 0.00020313, 386.30098811, 0.00067709, -38.63009881, -6.771e-05, -115.89029643, -0.00020313, -386.30098811, -0.00067709, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 13.35, 0.0)
    ops.node(121013, 0.0, 13.35, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.075, 27797306.29059401, 11582210.95441417, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 94.33568636, 0.00128262, 112.08451067, 0.01366555, 11.20845107, 0.03425942, -94.33568636, -0.00128262, -112.08451067, -0.01366555, -11.20845107, -0.03425942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 104.99541292, 0.00108899, 124.74981561, 0.0142048, 12.47498156, 0.03780814, -104.99541292, -0.00108899, -124.74981561, -0.0142048, -12.47498156, -0.03780814, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 100.86858167, 0.02565241, 100.86858167, 0.07695724, 70.60800717, -1736.60773244, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 25.21714542, 8.012e-05, 75.65143625, 0.00024037, 252.17145417, 0.00080122, -25.21714542, -8.012e-05, -75.65143625, -0.00024037, -252.17145417, -0.00080122, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 108.71988877, 0.02177979, 108.71988877, 0.06533938, 76.10392214, -1957.99947504, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 27.17997219, 8.636e-05, 81.53991658, 0.00025908, 271.79972192, 0.00086359, -27.17997219, -8.636e-05, -81.53991658, -0.00025908, -271.79972192, -0.00086359, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 5.45, 13.35, 0.0)
    ops.node(121014, 5.45, 13.35, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.105, 26832014.25445624, 11180005.93935677, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 140.56868226, 0.00102683, 167.36447679, 0.01291818, 16.73644768, 0.03381554, -140.56868226, -0.00102683, -167.36447679, -0.01291818, -16.73644768, -0.03381554, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 145.90898659, 0.00091277, 173.72277244, 0.0133988, 17.37227724, 0.03686075, -145.90898659, -0.00091277, -173.72277244, -0.0133988, -17.37227724, -0.03686075, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 134.56666444, 0.02053667, 134.56666444, 0.06161, 94.19666511, -2316.97440127, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 33.64166611, 7.91e-05, 100.92499833, 0.00023729, 336.41666111, 0.00079096, -33.64166611, -7.91e-05, -100.92499833, -0.00023729, -336.41666111, -0.00079096, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 143.006837, 0.01825531, 143.006837, 0.05476594, 100.1047859, -2579.32440464, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 35.75170925, 8.406e-05, 107.25512775, 0.00025217, 357.51709249, 0.00084057, -35.75170925, -8.406e-05, -107.25512775, -0.00025217, -357.51709249, -0.00084057, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 8.35, 13.35, 0.0)
    ops.node(121015, 8.35, 13.35, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.105, 27764742.8153908, 11568642.83974617, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 143.63405404, 0.00100729, 171.19652196, 0.01316082, 17.1196522, 0.03619853, -143.63405404, -0.00100729, -171.19652196, -0.01316082, -17.1196522, -0.03619853, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 148.38107249, 0.00089872, 176.85446328, 0.01366005, 17.68544633, 0.03952502, -148.38107249, -0.00089872, -176.85446328, -0.01366005, -17.68544633, -0.03952502, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 138.68514165, 0.02014577, 138.68514165, 0.0604373, 97.07959916, -2345.19057765, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 34.67128541, 7.878e-05, 104.01385624, 0.00023634, 346.71285413, 0.00078778, -34.67128541, -7.878e-05, -104.01385624, -0.00023634, -346.71285413, -0.00078778, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 147.28030406, 0.01797444, 147.28030406, 0.05392332, 103.09621284, -2614.06812056, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 36.82007601, 8.366e-05, 110.46022804, 0.00025098, 368.20076014, 0.00083661, -36.82007601, -8.366e-05, -110.46022804, -0.00025098, -368.20076014, -0.00083661, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 13.8, 13.35, 0.0)
    ops.node(121016, 13.8, 13.35, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.075, 26998694.20683129, 11249455.91951304, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 92.34217287, 0.00131045, 109.5870089, 0.01312311, 10.95870089, 0.03191035, -92.34217287, -0.00131045, -109.5870089, -0.01312311, -10.95870089, -0.03191035, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 103.2057922, 0.00110724, 122.47940152, 0.01361903, 12.24794015, 0.03515173, -103.2057922, -0.00110724, -122.47940152, -0.01361903, -12.24794015, -0.03515173, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 96.0804023, 0.02620898, 96.0804023, 0.07862695, 67.25628161, -1714.98409576, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 24.02010058, 7.858e-05, 72.06030173, 0.00023573, 240.20100575, 0.00078576, -24.02010058, -7.858e-05, -72.06030173, -0.00023573, -240.20100575, -0.00078576, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 105.83775422, 0.02214475, 105.83775422, 0.06643425, 74.08642795, -1930.45792708, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 26.45943855, 8.656e-05, 79.37831566, 0.00025967, 264.59438554, 0.00086556, -26.45943855, -8.656e-05, -79.37831566, -0.00025967, -264.59438554, -0.00086556, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 2.6)
    ops.node(122001, 0.0, 0.0, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.075, 28401895.65062046, 11834123.18775853, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 91.05148228, 0.00128324, 109.06452525, 0.01589907, 10.90645252, 0.04335712, -91.05148228, -0.00128324, -109.06452525, -0.01589907, -10.90645252, -0.04335712, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 98.13983841, 0.00108077, 117.55519642, 0.01656164, 11.75551964, 0.04803225, -98.13983841, -0.00108077, -117.55519642, -0.01656164, -11.75551964, -0.04803225, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 94.35476903, 0.02566482, 94.35476903, 0.07699446, 66.04833832, -1538.07391558, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 23.58869226, 7.335e-05, 70.76607677, 0.00022006, 235.88692257, 0.00073353, -23.58869226, -7.335e-05, -70.76607677, -0.00022006, -235.88692257, -0.00073353, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 102.32019907, 0.02161547, 102.32019907, 0.0648464, 71.62413935, -1775.73879779, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 25.58004977, 7.955e-05, 76.7401493, 0.00023864, 255.80049768, 0.00079545, -25.58004977, -7.955e-05, -76.7401493, -0.00023864, -255.80049768, -0.00079545, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.8, 0.0, 2.6)
    ops.node(122004, 13.8, 0.0, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.075, 28627128.22616072, 11927970.09423363, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 88.67683966, 0.00125656, 106.21415823, 0.01618495, 10.62141582, 0.04408323, -88.67683966, -0.00125656, -106.21415823, -0.01618495, -10.62141582, -0.04408323, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 95.92824377, 0.00105745, 114.899648, 0.01686937, 11.4899648, 0.04884454, -95.92824377, -0.00105745, -114.899648, -0.01686937, -11.4899648, -0.04884454, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 95.70563012, 0.02513126, 95.70563012, 0.07539379, 66.99394108, -1548.22615503, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 23.92640753, 7.382e-05, 71.77922259, 0.00022145, 239.2640753, 0.00073817, -23.92640753, -7.382e-05, -71.77922259, -0.00022145, -239.2640753, -0.00073817, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 103.2385104, 0.02114896, 103.2385104, 0.06344688, 72.26695728, -1788.83144507, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 25.8096276, 7.963e-05, 77.4288828, 0.00023888, 258.09627599, 0.00079627, -25.8096276, -7.963e-05, -77.4288828, -0.00023888, -258.09627599, -0.00079627, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.45, 2.625)
    ops.node(122005, 0.0, 4.45, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.135, 27724384.06680581, 11551826.69450242, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 174.1803794, 0.00074538, 209.29195931, 0.01461909, 20.92919593, 0.04326062, -174.1803794, -0.00074538, -209.29195931, -0.01461909, -20.92919593, -0.04326062, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 107.36059725, 0.00098175, 129.00253076, 0.01332193, 12.90025308, 0.03501524, -107.36059725, -0.00098175, -129.00253076, -0.01332193, -12.90025308, -0.03501524, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 188.48857025, 0.01490761, 188.48857025, 0.04472283, 131.94199917, -2666.82664107, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 47.12214256, 8.34e-05, 141.36642769, 0.00025019, 471.22142562, 0.00083397, -47.12214256, -8.34e-05, -141.36642769, -0.00025019, -471.22142562, -0.00083397, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 142.13918398, 0.01963499, 142.13918398, 0.05890496, 99.49742879, -1991.77857206, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 35.53479599, 6.289e-05, 106.60438798, 0.00018867, 355.34795995, 0.0006289, -35.53479599, -6.289e-05, -106.60438798, -0.00018867, -355.34795995, -0.0006289, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 5.45, 4.45, 2.625)
    ops.node(122006, 5.45, 4.45, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.22, 28599797.08678026, 11916582.11949178, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 308.02021848, 0.0006654, 371.78878343, 0.01443624, 37.17887834, 0.04308241, -308.02021848, -0.0006654, -371.78878343, -0.01443624, -37.17887834, -0.04308241, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 192.54993606, 0.00078122, 232.41301116, 0.01343767, 23.24130112, 0.03688707, -192.54993606, -0.00078122, -232.41301116, -0.01343767, -23.24130112, -0.03688707, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 311.98748998, 0.01330801, 311.98748998, 0.03992403, 218.39124298, -3193.46535059, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 77.99687249, 8.211e-05, 233.99061748, 0.00024634, 779.96872494, 0.00082113, -77.99687249, -8.211e-05, -233.99061748, -0.00024634, -779.96872494, -0.00082113, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 226.89999271, 0.0156245, 226.89999271, 0.04687349, 158.8299949, -2512.5806523, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 56.72499818, 5.972e-05, 170.17499453, 0.00017916, 567.24998178, 0.00059719, -56.72499818, -5.972e-05, -170.17499453, -0.00017916, -567.24998178, -0.00059719, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 8.35, 4.45, 2.625)
    ops.node(122007, 8.35, 4.45, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.22, 26589646.42101824, 11079019.34209093, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 299.99507061, 0.0006696, 362.63692265, 0.01484288, 36.26369227, 0.04072693, -299.99507061, -0.0006696, -362.63692265, -0.01484288, -36.26369227, -0.04072693, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 187.58430055, 0.00078971, 226.75370416, 0.01381602, 22.67537042, 0.03500439, -187.58430055, -0.00078971, -226.75370416, -0.01381602, -22.67537042, -0.03500439, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 294.50832113, 0.01339195, 294.50832113, 0.04017585, 206.15582479, -3287.40248404, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 73.62708028, 8.337e-05, 220.88124085, 0.00025012, 736.27080284, 0.00083372, -73.62708028, -8.337e-05, -220.88124085, -0.00025012, -736.27080284, -0.00083372, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 214.18786992, 0.01579415, 214.18786992, 0.04738245, 149.93150894, -2573.10028672, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 53.54696748, 6.063e-05, 160.64090244, 0.0001819, 535.46967479, 0.00060635, -53.54696748, -6.063e-05, -160.64090244, -0.0001819, -535.46967479, -0.00060635, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 13.8, 4.45, 2.625)
    ops.node(122008, 13.8, 4.45, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.135, 27747346.85397518, 11561394.52248966, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 176.88680031, 0.00075594, 212.54316846, 0.01464945, 21.25431685, 0.04333601, -176.88680031, -0.00075594, -212.54316846, -0.01464945, -21.25431685, -0.04333601, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 108.96967672, 0.00099575, 130.93549273, 0.01335355, 13.09354927, 0.03508095, -108.96967672, -0.00099575, -130.93549273, -0.01335355, -13.09354927, -0.03508095, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 189.10679792, 0.01511882, 189.10679792, 0.04535646, 132.37475854, -2683.8648829, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 47.27669948, 8.36e-05, 141.83009844, 0.0002508, 472.76699479, 0.00083601, -47.27669948, -8.36e-05, -141.83009844, -0.0002508, -472.76699479, -0.00083601, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 142.56721746, 0.01991493, 142.56721746, 0.05974479, 99.79705222, -2001.59149897, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 35.64180436, 6.303e-05, 106.92541309, 0.00018908, 356.41804365, 0.00063027, -35.64180436, -6.303e-05, -106.92541309, -0.00018908, -356.41804365, -0.00063027, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.9, 2.625)
    ops.node(122009, 0.0, 8.9, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.135, 26506509.15412935, 11044378.81422056, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 175.39948463, 0.00076222, 210.70352425, 0.01391393, 21.07035242, 0.04003663, -175.39948463, -0.00076222, -210.70352425, -0.01391393, -21.07035242, -0.04003663, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 107.97757129, 0.00100638, 129.7110699, 0.01270437, 12.97110699, 0.03248989, -107.97757129, -0.00100638, -129.7110699, -0.01270437, -12.97110699, -0.03248989, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 181.39133841, 0.01524442, 181.39133841, 0.04573327, 126.97393689, -2640.33523137, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 45.3478346, 8.394e-05, 136.04350381, 0.00025183, 453.47834603, 0.00083944, -45.3478346, -8.394e-05, -136.04350381, -0.00025183, -453.47834603, -0.00083944, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 136.57381015, 0.02012764, 136.57381015, 0.06038292, 95.60166711, -1976.50696824, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 34.14345254, 6.32e-05, 102.43035761, 0.00018961, 341.43452538, 0.00063204, -34.14345254, -6.32e-05, -102.43035761, -0.00018961, -341.43452538, -0.00063204, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 5.45, 8.9, 2.625)
    ops.node(122010, 5.45, 8.9, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.175, 27586072.2657209, 11494196.77738371, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 218.88647287, 0.00069459, 264.07420592, 0.01482705, 26.40742059, 0.04347912, -218.88647287, -0.00069459, -264.07420592, -0.01482705, -26.40742059, -0.04347912, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 138.36251105, 0.00085504, 166.92657958, 0.01366069, 16.69265796, 0.03633802, -138.36251105, -0.00085504, -166.92657958, -0.01366069, -16.69265796, -0.03633802, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 236.14500868, 0.01389175, 236.14500868, 0.04167524, 165.30150608, -2862.80647804, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 59.03625217, 8.1e-05, 177.10875651, 0.00024301, 590.3625217, 0.00081005, -59.03625217, -8.1e-05, -177.10875651, -0.00024301, -590.3625217, -0.00081005, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 168.43776083, 0.01710083, 168.43776083, 0.05130249, 117.90643258, -2186.79314016, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 42.10944021, 5.778e-05, 126.32832062, 0.00017334, 421.09440207, 0.00057779, -42.10944021, -5.778e-05, -126.32832062, -0.00017334, -421.09440207, -0.00057779, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.35, 8.9, 2.625)
    ops.node(122011, 8.35, 8.9, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.175, 26674244.54409361, 11114268.560039, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 216.57880428, 0.00071445, 261.3678565, 0.01448894, 26.13678565, 0.04162169, -216.57880428, -0.00071445, -261.3678565, -0.01448894, -26.13678565, -0.04162169, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 136.93265844, 0.00089091, 165.25068342, 0.01337219, 16.52506834, 0.03484702, -136.93265844, -0.00089091, -165.25068342, -0.01337219, -16.52506834, -0.03484702, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 230.68760952, 0.01428907, 230.68760952, 0.04286721, 161.48132667, -2903.83825173, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 57.67190238, 8.184e-05, 173.01570714, 0.00024551, 576.7190238, 0.00081838, -57.67190238, -8.184e-05, -173.01570714, -0.00024551, -576.7190238, -0.00081838, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 164.49329891, 0.01781825, 164.49329891, 0.05345475, 115.14530923, -2211.87839295, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 41.12332473, 5.836e-05, 123.36997418, 0.00017507, 411.23324726, 0.00058355, -41.12332473, -5.836e-05, -123.36997418, -0.00017507, -411.23324726, -0.00058355, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 13.8, 8.9, 2.625)
    ops.node(122012, 13.8, 8.9, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.135, 26803919.79636461, 11168299.91515192, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 177.28203328, 0.000772, 212.99600228, 0.01391104, 21.29960023, 0.04067273, -177.28203328, -0.000772, -212.99600228, -0.01391104, -21.29960023, -0.04067273, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 109.09050146, 0.00102208, 131.06709274, 0.0127088, 13.10670927, 0.0329783, -109.09050146, -0.00102208, -131.06709274, -0.0127088, -13.10670927, -0.0329783, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 182.31288782, 0.01544002, 182.31288782, 0.04632005, 127.61902148, -2619.62764354, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 45.57822196, 8.343e-05, 136.73466587, 0.0002503, 455.78221956, 0.00083434, -45.57822196, -8.343e-05, -136.73466587, -0.0002503, -455.78221956, -0.00083434, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 137.39029238, 0.02044161, 137.39029238, 0.06132484, 96.17320467, -1964.55735038, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 34.3475731, 6.288e-05, 103.04271929, 0.00018863, 343.47573096, 0.00062876, -34.3475731, -6.288e-05, -103.04271929, -0.00018863, -343.47573096, -0.00062876, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 13.35, 2.6)
    ops.node(122013, 0.0, 13.35, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.075, 27940958.63968185, 11642066.09986744, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 95.00275452, 0.00120999, 113.79997843, 0.01566371, 11.37999784, 0.04219565, -95.00275452, -0.00120999, -113.79997843, -0.01566371, -11.37999784, -0.04219565, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 100.24229547, 0.00103399, 120.07621379, 0.01634315, 12.00762138, 0.04675232, -100.24229547, -0.00103399, -120.07621379, -0.01634315, -12.00762138, -0.04675232, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 93.35101308, 0.02419976, 93.35101308, 0.07259927, 65.34570916, -1551.41657286, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 23.33775327, 7.377e-05, 70.01325981, 0.00022131, 233.3775327, 0.00073769, -23.33775327, -7.377e-05, -70.01325981, -0.00022131, -233.3775327, -0.00073769, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 101.71307437, 0.02067982, 101.71307437, 0.06203947, 71.19915206, -1792.94694246, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 25.42826859, 8.038e-05, 76.28480578, 0.00024113, 254.28268592, 0.00080378, -25.42826859, -8.038e-05, -76.28480578, -0.00024113, -254.28268592, -0.00080378, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 5.45, 13.35, 2.6)
    ops.node(122014, 5.45, 13.35, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.105, 27117638.0203096, 11299015.84179567, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 108.31658881, 0.00099318, 130.01846174, 0.01357433, 13.00184617, 0.0407374, -108.31658881, -0.00099318, -130.01846174, -0.01357433, -13.00184617, -0.0407374, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 109.18025578, 0.0008838, 131.05516953, 0.01409413, 13.10551695, 0.04459074, -109.18025578, -0.0008838, -131.05516953, -0.01409413, -13.10551695, -0.04459074, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 127.27081639, 0.01986355, 127.27081639, 0.05959064, 89.08957147, -2129.90963811, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 31.8177041, 7.402e-05, 95.45311229, 0.00022206, 318.17704096, 0.0007402, -31.8177041, -7.402e-05, -95.45311229, -0.00022206, -318.17704096, -0.0007402, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 135.69234738, 0.01767594, 135.69234738, 0.05302781, 94.98464317, -2424.13170966, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 33.92308684, 7.892e-05, 101.76926053, 0.00023675, 339.23086845, 0.00078918, -33.92308684, -7.892e-05, -101.76926053, -0.00023675, -339.23086845, -0.00078918, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 8.35, 13.35, 2.6)
    ops.node(122015, 8.35, 13.35, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.105, 26721209.98199302, 11133837.49249709, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 107.1355402, 0.0009984, 128.57776718, 0.01377999, 12.85777672, 0.04007767, -107.1355402, -0.0009984, -128.57776718, -0.01377999, -12.85777672, -0.04007767, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 108.2788048, 0.00088715, 129.94984605, 0.01430795, 12.9949846, 0.04383297, -108.2788048, -0.00088715, -129.94984605, -0.01430795, -12.9949846, -0.04383297, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 126.24368591, 0.01996799, 126.24368591, 0.05990397, 88.37058013, -2138.54431962, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 31.56092148, 7.451e-05, 94.68276443, 0.00022354, 315.60921476, 0.00074512, -31.56092148, -7.451e-05, -94.68276443, -0.00022354, -315.60921476, -0.00074512, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 134.70774219, 0.01774308, 134.70774219, 0.05322925, 94.29541954, -2434.87981052, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 33.67693555, 7.951e-05, 101.03080665, 0.00023852, 336.76935549, 0.00079507, -33.67693555, -7.951e-05, -101.03080665, -0.00023852, -336.76935549, -0.00079507, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 13.8, 13.35, 2.6)
    ops.node(122016, 13.8, 13.35, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.075, 27102092.29440457, 11292538.4560019, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 90.55900326, 0.00129971, 108.44470805, 0.01500428, 10.8444708, 0.03976399, -90.55900326, -0.00129971, -108.44470805, -0.01500428, -10.8444708, -0.03976399, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 97.3977729, 0.00109408, 116.63415748, 0.01560975, 11.66341575, 0.0439877, -97.3977729, -0.00109408, -116.63415748, -0.01560975, -11.66341575, -0.0439877, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 86.71812583, 0.02599413, 86.71812583, 0.0779824, 60.70268808, -1522.55149963, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 21.67953146, 7.065e-05, 65.03859437, 0.00021195, 216.79531458, 0.00070649, -21.67953146, -7.065e-05, -65.03859437, -0.00021195, -216.79531458, -0.00070649, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 98.65264728, 0.02188151, 98.65264728, 0.06564453, 69.05685309, -1755.73037589, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 24.66316182, 8.037e-05, 73.98948546, 0.00024112, 246.63161819, 0.00080372, -24.66316182, -8.037e-05, -73.98948546, -0.00024112, -246.63161819, -0.00080372, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 4.9)
    ops.node(123001, 0.0, 0.0, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 27417240.48656357, 11423850.20273482, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 53.32728479, 0.00121352, 64.22795256, 0.01620328, 6.42279526, 0.05064259, -53.32728479, -0.00121352, -64.22795256, -0.01620328, -6.42279526, -0.05064259, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 53.32728479, 0.00121352, 64.22795256, 0.01620328, 6.42279526, 0.05064259, -53.32728479, -0.00121352, -64.22795256, -0.01620328, -6.42279526, -0.05064259, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 73.78009459, 0.02427045, 73.78009459, 0.07281134, 51.64606621, -1414.09796915, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 18.44502365, 7.13e-05, 55.33507094, 0.0002139, 184.45023648, 0.00071301, -18.44502365, -7.13e-05, -55.33507094, -0.0002139, -184.45023648, -0.00071301, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 73.78009459, 0.02427045, 73.78009459, 0.07281134, 51.64606621, -1414.09796915, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 18.44502365, 7.13e-05, 55.33507094, 0.0002139, 184.45023648, 0.00071301, -18.44502365, -7.13e-05, -55.33507094, -0.0002139, -184.45023648, -0.00071301, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.8, 0.0, 4.9)
    ops.node(123004, 13.8, 0.0, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 27669223.57413147, 11528843.15588811, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 53.17404306, 0.00119667, 64.03810998, 0.01682478, 6.403811, 0.05180822, -53.17404306, -0.00119667, -64.03810998, -0.01682478, -6.403811, -0.05180822, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 53.17404306, 0.00119667, 64.03810998, 0.01682478, 6.403811, 0.05180822, -53.17404306, -0.00119667, -64.03810998, -0.01682478, -6.403811, -0.05180822, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 79.3348622, 0.0239334, 79.3348622, 0.0718002, 55.53440354, -1450.56077102, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 19.83371555, 7.597e-05, 59.50114665, 0.00022791, 198.33715549, 0.00075971, -19.83371555, -7.597e-05, -59.50114665, -0.00022791, -198.33715549, -0.00075971, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 79.3348622, 0.0239334, 79.3348622, 0.0718002, 55.53440354, -1450.56077102, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 19.83371555, 7.597e-05, 59.50114665, 0.00022791, 198.33715549, 0.00075971, -19.83371555, -7.597e-05, -59.50114665, -0.00022791, -198.33715549, -0.00075971, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.45, 4.925)
    ops.node(123005, 0.0, 4.45, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0875, 27049902.24789109, 11270792.60328796, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 94.60007243, 0.00087743, 113.65037254, 0.01518142, 11.36503725, 0.04631479, -94.60007243, -0.00087743, -113.65037254, -0.01518142, -11.36503725, -0.04631479, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 65.09658593, 0.00115386, 78.20555578, 0.01404685, 7.82055558, 0.03838213, -65.09658593, -0.00115386, -78.20555578, -0.01404685, -7.82055558, -0.03838213, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 111.23613515, 0.01754856, 111.23613515, 0.05264568, 77.8652946, -1979.60237236, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 27.80903379, 7.783e-05, 83.42710136, 0.00023348, 278.09033787, 0.00077827, -27.80903379, -7.783e-05, -83.42710136, -0.00023348, -278.09033787, -0.00077827, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 93.24276512, 0.02307729, 93.24276512, 0.06923188, 65.26993558, -1508.88413741, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 23.31069128, 6.524e-05, 69.93207384, 0.00019571, 233.10691279, 0.00065238, -23.31069128, -6.524e-05, -69.93207384, -0.00019571, -233.10691279, -0.00065238, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 5.45, 4.45, 4.925)
    ops.node(123006, 5.45, 4.45, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.175, 28037197.21121729, 11682165.50467387, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 197.83655345, 0.00068279, 239.42202495, 0.01601371, 23.94220249, 0.04851006, -197.83655345, -0.00068279, -239.42202495, -0.01601371, -23.94220249, -0.04851006, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 123.9709554, 0.00083884, 150.02979307, 0.01473043, 15.00297931, 0.0404504, -123.9709554, -0.00083884, -150.02979307, -0.01473043, -15.00297931, -0.0404504, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 230.51728372, 0.01365588, 230.51728372, 0.04096765, 161.3620986, -2880.57506373, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 57.62932093, 7.78e-05, 172.88796279, 0.00023341, 576.29320929, 0.00077802, -57.62932093, -7.78e-05, -172.88796279, -0.00023341, -576.29320929, -0.00077802, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 164.35090034, 0.01677683, 164.35090034, 0.05033048, 115.04563024, -2090.27096513, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 41.08772509, 5.547e-05, 123.26317526, 0.00016641, 410.87725086, 0.0005547, -41.08772509, -5.547e-05, -123.26317526, -0.00016641, -410.87725086, -0.0005547, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 8.35, 4.45, 4.925)
    ops.node(123007, 8.35, 4.45, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.175, 27701102.23286538, 11542125.93036058, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 197.89536575, 0.00068794, 239.58297929, 0.01561155, 23.95829793, 0.04766619, -197.89536575, -0.00068794, -239.58297929, -0.01561155, -23.95829793, -0.04766619, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 123.96878145, 0.00084703, 150.08340336, 0.01436955, 15.00834034, 0.03973993, -123.96878145, -0.00084703, -150.08340336, -0.01436955, -15.00834034, -0.03973993, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 226.91034149, 0.01375872, 226.91034149, 0.04127617, 158.83723904, -2833.2119912, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 56.72758537, 7.751e-05, 170.18275612, 0.00023254, 567.27585373, 0.00077514, -56.72758537, -7.751e-05, -170.18275612, -0.00023254, -567.27585373, -0.00077514, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 161.7807, 0.01694057, 161.7807, 0.05082172, 113.24649, -2062.00782898, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 40.445175, 5.527e-05, 121.335525, 0.0001658, 404.45174999, 0.00055265, -40.445175, -5.527e-05, -121.335525, -0.0001658, -404.45174999, -0.00055265, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 13.8, 4.45, 4.925)
    ops.node(123008, 13.8, 4.45, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0875, 27747327.30093216, 11561386.3753884, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 97.01188426, 0.00089399, 116.55214521, 0.01539118, 11.65521452, 0.04814275, -97.01188426, -0.00089399, -116.55214521, -0.01539118, -11.65521452, -0.04814275, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 66.7675783, 0.00117592, 80.21599148, 0.01424305, 8.02159915, 0.03984319, -66.7675783, -0.00117592, -80.21599148, -0.01424305, -8.02159915, -0.03984319, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 114.60139766, 0.01787989, 114.60139766, 0.05363967, 80.22097836, -2033.96234491, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 28.65034941, 7.817e-05, 85.95104824, 0.0002345, 286.50349414, 0.00078167, -28.65034941, -7.817e-05, -85.95104824, -0.0002345, -286.50349414, -0.00078167, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 97.81669881, 0.02351843, 97.81669881, 0.07055528, 68.47168917, -1542.74164403, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 24.4541747, 6.672e-05, 73.36252411, 0.00020015, 244.54174703, 0.00066718, -24.4541747, -6.672e-05, -73.36252411, -0.00020015, -244.54174703, -0.00066718, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.9, 4.925)
    ops.node(123009, 0.0, 8.9, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0875, 27498264.73159692, 11457610.30483205, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 95.97551803, 0.00089955, 115.30929667, 0.01529231, 11.53092967, 0.04747707, -95.97551803, -0.00089955, -115.30929667, -0.01529231, -11.53092967, -0.04747707, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 65.95773099, 0.00118962, 79.24457952, 0.01416263, 7.92445795, 0.03931972, -65.95773099, -0.00118962, -79.24457952, -0.01416263, -7.92445795, -0.03931972, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 113.80410302, 0.01799097, 113.80410302, 0.0539729, 79.66287212, -2029.45250478, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 28.45102576, 7.833e-05, 85.35307727, 0.00023498, 284.51025756, 0.00078326, -28.45102576, -7.833e-05, -85.35307727, -0.00023498, -284.51025756, -0.00078326, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 96.43497674, 0.02379247, 96.43497674, 0.07137741, 67.50448372, -1539.93587705, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 24.10874419, 6.637e-05, 72.32623256, 0.00019911, 241.08744185, 0.00066371, -24.10874419, -6.637e-05, -72.32623256, -0.00019911, -241.08744185, -0.00066371, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 5.45, 8.9, 4.925)
    ops.node(123010, 5.45, 8.9, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1, 28426418.45423739, 11844341.02259891, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 116.47396373, 0.00080001, 140.06120539, 0.01592401, 14.00612054, 0.05133854, -116.47396373, -0.00080001, -140.06120539, -0.01592401, -14.00612054, -0.05133854, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 69.53848088, 0.00114377, 83.62077791, 0.0142627, 8.36207779, 0.03953598, -69.53848088, -0.00114377, -83.62077791, -0.0142627, -8.36207779, -0.03953598, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 138.74665886, 0.01600021, 138.74665886, 0.04800062, 97.1226612, -2262.00397199, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 34.68666471, 8.083e-05, 104.05999414, 0.00024248, 346.86664714, 0.00080828, -34.68666471, -8.083e-05, -104.05999414, -0.00024248, -346.86664714, -0.00080828, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 105.51303505, 0.02287536, 105.51303505, 0.06862607, 73.85912453, -1545.5566104, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 26.37825876, 6.147e-05, 79.13477629, 0.0001844, 263.78258762, 0.00061467, -26.37825876, -6.147e-05, -79.13477629, -0.0001844, -263.78258762, -0.00061467, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.35, 8.9, 4.925)
    ops.node(123011, 8.35, 8.9, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1, 27904915.06573193, 11627047.94405497, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 116.70148512, 0.00080731, 140.37287488, 0.01571156, 14.03728749, 0.05002961, -116.70148512, -0.00080731, -140.37287488, -0.01571156, -14.03728749, -0.05002961, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 69.6645742, 0.00115571, 83.79513378, 0.01408402, 8.37951338, 0.03857481, -69.6645742, -0.00115571, -83.79513378, -0.01408402, -8.37951338, -0.03857481, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 136.47697307, 0.0161462, 136.47697307, 0.04843859, 95.53388115, -2244.31547387, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 34.11924327, 8.099e-05, 102.3577298, 0.00024297, 341.19243268, 0.00080991, -34.11924327, -8.099e-05, -102.3577298, -0.00024297, -341.19243268, -0.00080991, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 103.06762623, 0.02311413, 103.06762623, 0.06934239, 72.14733836, -1536.4139079, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 25.76690656, 6.116e-05, 77.30071967, 0.00018349, 257.66906556, 0.00061165, -25.76690656, -6.116e-05, -77.30071967, -0.00018349, -257.66906556, -0.00061165, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 13.8, 8.9, 4.925)
    ops.node(123012, 13.8, 8.9, 6.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0875, 26928738.82379294, 11220307.84324706, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 95.6544366, 0.00092629, 114.91291534, 0.0151124, 11.49129153, 0.04595477, -95.6544366, -0.00092629, -114.91291534, -0.0151124, -11.49129153, -0.04595477, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 65.59339537, 0.00123737, 78.79956808, 0.01402411, 7.87995681, 0.03813193, -65.59339537, -0.00123737, -78.79956808, -0.01402411, -7.87995681, -0.03813193, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 111.84202773, 0.0185258, 111.84202773, 0.05557741, 78.28941941, -2013.67478074, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 27.96050693, 7.86e-05, 83.8815208, 0.00023581, 279.60506932, 0.00078603, -27.96050693, -7.86e-05, -83.8815208, -0.00023581, -279.60506932, -0.00078603, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 95.13187383, 0.02474747, 95.13187383, 0.07424241, 66.59231168, -1530.11544258, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 23.78296846, 6.686e-05, 71.34890537, 0.00020058, 237.82968457, 0.00066859, -23.78296846, -6.686e-05, -71.34890537, -0.00020058, -237.82968457, -0.00066859, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 13.35, 4.9)
    ops.node(123013, 0.0, 13.35, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 28178032.43047657, 11740846.84603191, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 54.72918419, 0.00117622, 65.89336224, 0.01686617, 6.58933622, 0.05290906, -54.72918419, -0.00117622, -65.89336224, -0.01686617, -6.58933622, -0.05290906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 54.72918419, 0.00117622, 65.89336224, 0.01686617, 6.58933622, 0.05290906, -54.72918419, -0.00117622, -65.89336224, -0.01686617, -6.58933622, -0.05290906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 81.68844802, 0.02352438, 81.68844802, 0.07057315, 57.18191361, -1487.25709739, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 20.422112, 7.681e-05, 61.26633601, 0.00023044, 204.22112004, 0.00076812, -20.422112, -7.681e-05, -61.26633601, -0.00023044, -204.22112004, -0.00076812, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 81.68844802, 0.02352438, 81.68844802, 0.07057315, 57.18191361, -1487.25709739, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 20.422112, 7.681e-05, 61.26633601, 0.00023044, 204.22112004, 0.00076812, -20.422112, -7.681e-05, -61.26633601, -0.00023044, -204.22112004, -0.00076812, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 5.45, 13.35, 4.9)
    ops.node(123014, 5.45, 13.35, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 29280730.9550745, 12200304.56461438, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 44.61691555, 0.00109482, 53.45229917, 0.0150594, 5.34522992, 0.05419522, -44.61691555, -0.00109482, -53.45229917, -0.0150594, -5.34522992, -0.05419522, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 44.61691555, 0.00109482, 53.45229917, 0.0150594, 5.34522992, 0.05419522, -44.61691555, -0.00109482, -53.45229917, -0.0150594, -5.34522992, -0.05419522, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 92.05750172, 0.02189648, 92.05750172, 0.06568945, 64.44025121, -1671.72751512, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 23.01437543, 8.33e-05, 69.04312629, 0.00024991, 230.14375431, 0.00083302, -23.01437543, -8.33e-05, -69.04312629, -0.00024991, -230.14375431, -0.00083302, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 92.05750172, 0.02189648, 92.05750172, 0.06568945, 64.44025121, -1671.72751512, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 23.01437543, 8.33e-05, 69.04312629, 0.00024991, 230.14375431, 0.00083302, -23.01437543, -8.33e-05, -69.04312629, -0.00024991, -230.14375431, -0.00083302, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 8.35, 13.35, 4.9)
    ops.node(123015, 8.35, 13.35, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 27736419.81023252, 11556841.58759688, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 44.47106117, 0.00112995, 53.30296321, 0.0151944, 5.33029632, 0.05038483, -44.47106117, -0.00112995, -53.30296321, -0.0151944, -5.33029632, -0.05038483, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 44.47106117, 0.00112995, 53.30296321, 0.0151944, 5.33029632, 0.05038483, -44.47106117, -0.00112995, -53.30296321, -0.0151944, -5.33029632, -0.05038483, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 90.85686692, 0.02259902, 90.85686692, 0.06779705, 63.59980684, -1742.75840806, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 22.71421673, 8.679e-05, 68.14265019, 0.00026038, 227.1421673, 0.00086794, -22.71421673, -8.679e-05, -68.14265019, -0.00026038, -227.1421673, -0.00086794, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 90.85686692, 0.02259902, 90.85686692, 0.06779705, 63.59980684, -1742.75840806, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 22.71421673, 8.679e-05, 68.14265019, 0.00026038, 227.1421673, 0.00086794, -22.71421673, -8.679e-05, -68.14265019, -0.00026038, -227.1421673, -0.00086794, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 13.8, 13.35, 4.9)
    ops.node(123016, 13.8, 13.35, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 28773795.87523847, 11989081.6146827, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 52.68613541, 0.00120031, 63.40325171, 0.01663311, 6.34032517, 0.05385152, -52.68613541, -0.00120031, -63.40325171, -0.01663311, -6.34032517, -0.05385152, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 52.68613541, 0.00120031, 63.40325171, 0.01663311, 6.34032517, 0.05385152, -52.68613541, -0.00120031, -63.40325171, -0.01663311, -6.34032517, -0.05385152, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 77.34730141, 0.02400623, 77.34730141, 0.0720187, 54.14311099, -1419.0363039, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 19.33682535, 7.122e-05, 58.01047606, 0.00021367, 193.36825352, 0.00071224, -19.33682535, -7.122e-05, -58.01047606, -0.00021367, -193.36825352, -0.00071224, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 77.34730141, 0.02400623, 77.34730141, 0.0720187, 54.14311099, -1419.0363039, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 19.33682535, 7.122e-05, 58.01047606, 0.00021367, 193.36825352, 0.00071224, -19.33682535, -7.122e-05, -58.01047606, -0.00021367, -193.36825352, -0.00071224, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 7.2)
    ops.node(124001, 0.0, 0.0, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 27398926.139446, 11416219.22476917, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 42.55259639, 0.00112461, 51.85333484, 0.01969763, 5.18533348, 0.06842807, -42.55259639, -0.00112461, -51.85333484, -0.01969763, -5.18533348, -0.06842807, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 42.55259639, 0.00112461, 51.85333484, 0.01969763, 5.18533348, 0.06842807, -42.55259639, -0.00112461, -51.85333484, -0.01969763, -5.18533348, -0.06842807, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 69.35330936, 0.02249217, 69.35330936, 0.06747651, 48.54731655, -1863.55652682, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 17.33832734, 6.707e-05, 52.01498202, 0.0002012, 173.38327339, 0.00067068, -17.33832734, -6.707e-05, -52.01498202, -0.0002012, -173.38327339, -0.00067068, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 69.35330936, 0.02249217, 69.35330936, 0.06747651, 48.54731655, -1863.55652682, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 17.33832734, 6.707e-05, 52.01498202, 0.0002012, 173.38327339, 0.00067068, -17.33832734, -6.707e-05, -52.01498202, -0.0002012, -173.38327339, -0.00067068, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.8, 0.0, 7.2)
    ops.node(124004, 13.8, 0.0, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 27877473.28220074, 11615613.86758364, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 42.70566046, 0.00110694, 51.99638565, 0.01904789, 5.19963857, 0.06825846, -42.70566046, -0.00110694, -51.99638565, -0.01904789, -5.19963857, -0.06825846, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 42.70566046, 0.00110694, 51.99638565, 0.01904789, 5.19963857, 0.06825846, -42.70566046, -0.00110694, -51.99638565, -0.01904789, -5.19963857, -0.06825846, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 65.01696036, 0.02213875, 65.01696036, 0.06641625, 45.51187225, -1773.99529451, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 16.25424009, 6.18e-05, 48.76272027, 0.00018539, 162.54240089, 0.00061795, -16.25424009, -6.18e-05, -48.76272027, -0.00018539, -162.54240089, -0.00061795, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 65.01696036, 0.02213875, 65.01696036, 0.06641625, 45.51187225, -1773.99529451, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 16.25424009, 6.18e-05, 48.76272027, 0.00018539, 162.54240089, 0.00061795, -16.25424009, -6.18e-05, -48.76272027, -0.00018539, -162.54240089, -0.00061795, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.45, 7.225)
    ops.node(124005, 0.0, 4.45, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0875, 27584856.71586768, 11493690.2982782, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 70.14653219, 0.00084678, 85.27637165, 0.01824277, 8.52763716, 0.06426189, -70.14653219, -0.00084678, -85.27637165, -0.01824277, -8.52763716, -0.06426189, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 47.56027194, 0.001121, 57.8185022, 0.01680098, 5.78185022, 0.05277164, -47.56027194, -0.001121, -57.8185022, -0.01680098, -5.78185022, -0.05277164, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 100.81411367, 0.0169356, 100.81411367, 0.05080681, 70.56987957, -2280.59503558, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 25.20352842, 6.917e-05, 75.61058526, 0.0002075, 252.03528418, 0.00069168, -25.20352842, -6.917e-05, -75.61058526, -0.0002075, -252.03528418, -0.00069168, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 83.29569632, 0.02241992, 83.29569632, 0.06725977, 58.30698742, -1487.33692932, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 20.82392408, 5.715e-05, 62.47177224, 0.00017145, 208.2392408, 0.00057148, -20.82392408, -5.715e-05, -62.47177224, -0.00017145, -208.2392408, -0.00057148, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 5.45, 4.45, 7.225)
    ops.node(124006, 5.45, 4.45, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.175, 27604231.51047998, 11501763.12936666, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 157.74696362, 0.00066172, 192.24471652, 0.01738994, 19.22447165, 0.05615844, -157.74696362, -0.00066172, -192.24471652, -0.01738994, -19.22447165, -0.05615844, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 96.55016375, 0.00080885, 117.66476156, 0.01596655, 11.76647616, 0.04665076, -96.55016375, -0.00080885, -117.66476156, -0.01596655, -11.76647616, -0.04665076, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 204.72033766, 0.01323437, 204.72033766, 0.03970312, 143.30423636, -3327.4328503, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 51.18008442, 7.018e-05, 153.54025325, 0.00021054, 511.80084416, 0.00070179, -51.18008442, -7.018e-05, -153.54025325, -0.00021054, -511.80084416, -0.00070179, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 145.81326778, 0.01617694, 145.81326778, 0.04853081, 102.06928745, -2100.29850076, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 36.45331695, 4.999e-05, 109.35995084, 0.00014996, 364.53316946, 0.00049985, -36.45331695, -4.999e-05, -109.35995084, -0.00014996, -364.53316946, -0.00049985, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 8.35, 4.45, 7.225)
    ops.node(124007, 8.35, 4.45, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.175, 28376587.9715132, 11823578.32146383, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 158.83873484, 0.00066006, 193.29038217, 0.01685939, 19.32903822, 0.05616708, -158.83873484, -0.00066006, -193.29038217, -0.01685939, -19.32903822, -0.05616708, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 97.26757181, 0.00080598, 118.36461772, 0.01548446, 11.83646177, 0.04659542, -97.26757181, -0.00080598, -118.36461772, -0.01548446, -11.83646177, -0.04659542, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 208.73399297, 0.01320117, 208.73399297, 0.03960352, 146.11379508, -3240.96906435, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 52.18349824, 6.961e-05, 156.55049473, 0.00020882, 521.83498242, 0.00069607, -52.18349824, -6.961e-05, -156.55049473, -0.00020882, -521.83498242, -0.00069607, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 148.72346318, 0.01611962, 148.72346318, 0.04835887, 104.10642422, -2052.17491557, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 37.18086579, 4.96e-05, 111.54259738, 0.00014879, 371.80865794, 0.00049595, -37.18086579, -4.96e-05, -111.54259738, -0.00014879, -371.80865794, -0.00049595, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 13.8, 4.45, 7.225)
    ops.node(124008, 13.8, 4.45, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0875, 27810862.23994924, 11587859.26664552, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 72.31783394, 0.00083612, 87.88577467, 0.01846273, 8.78857747, 0.0647693, -72.31783394, -0.00083612, -87.88577467, -0.01846273, -8.78857747, -0.0647693, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 49.25860428, 0.00109218, 59.86255893, 0.01698003, 5.98625589, 0.05317539, -49.25860428, -0.00109218, -59.86255893, -0.01698003, -5.98625589, -0.05317539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 102.15878231, 0.01672248, 102.15878231, 0.05016744, 71.51114762, -2329.00813505, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 25.53969558, 6.952e-05, 76.61908673, 0.00020856, 255.39695577, 0.00069521, -25.53969558, -6.952e-05, -76.61908673, -0.00020856, -255.39695577, -0.00069521, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 86.81305996, 0.02184368, 86.81305996, 0.06553104, 60.76914197, -1515.24642031, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 21.70326499, 5.908e-05, 65.10979497, 0.00017723, 217.0326499, 0.00059078, -21.70326499, -5.908e-05, -65.10979497, -0.00017723, -217.0326499, -0.00059078, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.9, 7.225)
    ops.node(124009, 0.0, 8.9, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0875, 29172134.69635449, 12155056.12348104, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 70.95532808, 0.00081771, 86.01968266, 0.01845329, 8.60196827, 0.06632573, -70.95532808, -0.00081771, -86.01968266, -0.01845329, -8.60196827, -0.06632573, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 48.27330188, 0.00106948, 58.52209018, 0.01696542, 5.85220902, 0.05438473, -48.27330188, -0.00106948, -58.52209018, -0.01696542, -5.85220902, -0.05438473, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 105.14628611, 0.0163542, 105.14628611, 0.04906259, 73.60240027, -2298.22532375, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 26.28657153, 6.821e-05, 78.85971458, 0.00020464, 262.86571526, 0.00068215, -26.28657153, -6.821e-05, -78.85971458, -0.00020464, -262.86571526, -0.00068215, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 89.76312783, 0.02138969, 89.76312783, 0.06416907, 62.83418948, -1497.5044573, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 22.44078196, 5.823e-05, 67.32234588, 0.0001747, 224.40781958, 0.00058235, -22.44078196, -5.823e-05, -67.32234588, -0.0001747, -224.40781958, -0.00058235, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 5.45, 8.9, 7.225)
    ops.node(124010, 5.45, 8.9, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1, 27828952.93729831, 11595397.05720763, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 88.95491415, 0.00076454, 108.02057867, 0.01851606, 10.80205787, 0.06382532, -88.95491415, -0.00076454, -108.02057867, -0.01851606, -10.80205787, -0.06382532, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 52.40107533, 0.00108885, 63.63217293, 0.01648695, 6.36321729, 0.04882153, -52.40107533, -0.00108885, -63.63217293, -0.01648695, -6.36321729, -0.04882153, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 123.82866867, 0.01529076, 123.82866867, 0.04587228, 86.68006807, -2526.72981154, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 30.95716717, 7.369e-05, 92.8715015, 0.00022106, 309.57167167, 0.00073686, -30.95716717, -7.369e-05, -92.8715015, -0.00022106, -309.57167167, -0.00073686, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 94.04888682, 0.02177691, 94.04888682, 0.06533074, 65.83422077, -1441.63154939, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 23.5122217, 5.597e-05, 70.53666511, 0.0001679, 235.12221704, 0.00055965, -23.5122217, -5.597e-05, -70.53666511, -0.0001679, -235.12221704, -0.00055965, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.35, 8.9, 7.225)
    ops.node(124011, 8.35, 8.9, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1, 26602686.18153297, 11084452.57563874, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 88.68866577, 0.00077924, 107.86249946, 0.01840395, 10.78624995, 0.06193073, -88.68866577, -0.00077924, -107.86249946, -0.01840395, -10.78624995, -0.06193073, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 52.15396682, 0.00111698, 63.42926877, 0.01640509, 6.34292688, 0.04746761, -52.15396682, -0.00111698, -63.42926877, -0.01640509, -6.34292688, -0.04746761, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 119.75568118, 0.01558488, 119.75568118, 0.04675465, 83.82897683, -2516.61455861, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 29.9389203, 7.455e-05, 89.81676089, 0.00022364, 299.38920296, 0.00074547, -29.9389203, -7.455e-05, -89.81676089, -0.00022364, -299.38920296, -0.00074547, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 89.9772411, 0.0223396, 89.9772411, 0.0670188, 62.98406877, -1436.85538076, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 22.49431028, 5.601e-05, 67.48293083, 0.00016803, 224.94310276, 0.0005601, -22.49431028, -5.601e-05, -67.48293083, -0.00016803, -224.94310276, -0.0005601, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 13.8, 8.9, 7.225)
    ops.node(124012, 13.8, 8.9, 8.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0875, 27453647.18005611, 11439019.65835671, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 70.44304391, 0.00082544, 85.65322787, 0.01863521, 8.56532279, 0.06448356, -70.44304391, -0.00082544, -85.65322787, -0.01863521, -8.56532279, -0.06448356, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 47.92257996, 0.00108015, 58.27010637, 0.0171331, 5.82701064, 0.05297028, -47.92257996, -0.00108015, -58.27010637, -0.0171331, -5.82701064, -0.05297028, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 101.65686919, 0.01650872, 101.65686919, 0.04952616, 71.15980843, -2353.82359366, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 25.4142173, 7.008e-05, 76.24265189, 0.00021024, 254.14217298, 0.00070079, -25.4142173, -7.008e-05, -76.24265189, -0.00021024, -254.14217298, -0.00070079, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 85.98273597, 0.02160298, 85.98273597, 0.06480895, 60.18791518, -1529.5392654, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 21.49568399, 5.927e-05, 64.48705198, 0.00017782, 214.95683992, 0.00059274, -21.49568399, -5.927e-05, -64.48705198, -0.00017782, -214.95683992, -0.00059274, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 13.35, 7.2)
    ops.node(124013, 0.0, 13.35, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 28615495.08058058, 11923122.95024191, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 41.35627986, 0.00109641, 50.2815947, 0.01909759, 5.02815947, 0.06899022, -41.35627986, -0.00109641, -50.2815947, -0.01909759, -5.02815947, -0.06899022, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 41.35627986, 0.00109641, 50.2815947, 0.01909759, 5.02815947, 0.06899022, -41.35627986, -0.00109641, -50.2815947, -0.01909759, -5.02815947, -0.06899022, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 65.80263348, 0.02192813, 65.80263348, 0.06578438, 46.06184344, -1734.58747831, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 16.45065837, 6.093e-05, 49.35197511, 0.00018279, 164.5065837, 0.00060929, -16.45065837, -6.093e-05, -49.35197511, -0.00018279, -164.5065837, -0.00060929, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 65.80263348, 0.02192813, 65.80263348, 0.06578438, 46.06184344, -1734.58747831, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 16.45065837, 6.093e-05, 49.35197511, 0.00018279, 164.5065837, 0.00060929, -16.45065837, -6.093e-05, -49.35197511, -0.00018279, -164.5065837, -0.00060929, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 5.45, 13.35, 7.2)
    ops.node(124014, 5.45, 13.35, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 27539782.31906125, 11474909.29960885, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 30.07411015, 0.00103221, 36.54735604, 0.01809743, 3.6547356, 0.07042928, -30.07411015, -0.00103221, -36.54735604, -0.01809743, -3.6547356, -0.07042928, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 30.07411015, 0.00103221, 36.54735604, 0.01809743, 3.6547356, 0.07042928, -30.07411015, -0.00103221, -36.54735604, -0.01809743, -3.6547356, -0.07042928, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 78.86663045, 0.02064429, 78.86663045, 0.06193288, 55.20664132, -2015.94545357, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 19.71665761, 7.588e-05, 59.14997284, 0.00022763, 197.16657613, 0.00075878, -19.71665761, -7.588e-05, -59.14997284, -0.00022763, -197.16657613, -0.00075878, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 78.86663045, 0.02064429, 78.86663045, 0.06193288, 55.20664132, -2015.94545357, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 19.71665761, 7.588e-05, 59.14997284, 0.00022763, 197.16657613, 0.00075878, -19.71665761, -7.588e-05, -59.14997284, -0.00022763, -197.16657613, -0.00075878, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 8.35, 13.35, 7.2)
    ops.node(124015, 8.35, 13.35, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 26181098.34604938, 10908790.97752057, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 29.67370651, 0.00105396, 36.11766943, 0.01769992, 3.61176694, 0.06771714, -29.67370651, -0.00105396, -36.11766943, -0.01769992, -3.61176694, -0.06771714, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 29.67370651, 0.00105396, 36.11766943, 0.01769992, 3.61176694, 0.06771714, -29.67370651, -0.00105396, -36.11766943, -0.01769992, -3.61176694, -0.06771714, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 75.81941723, 0.02107916, 75.81941723, 0.06323749, 53.07359206, -1972.87380274, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 18.95485431, 7.673e-05, 56.86456292, 0.00023019, 189.54854308, 0.00076731, -18.95485431, -7.673e-05, -56.86456292, -0.00023019, -189.54854308, -0.00076731, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 75.81941723, 0.02107916, 75.81941723, 0.06323749, 53.07359206, -1972.87380274, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 18.95485431, 7.673e-05, 56.86456292, 0.00023019, 189.54854308, 0.00076731, -18.95485431, -7.673e-05, -56.86456292, -0.00023019, -189.54854308, -0.00076731, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 13.8, 13.35, 7.2)
    ops.node(124016, 13.8, 13.35, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 27173540.72653969, 11322308.6360582, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 42.56436333, 0.00112871, 51.88679475, 0.01960836, 5.18867948, 0.06810155, -42.56436333, -0.00112871, -51.88679475, -0.01960836, -5.18867948, -0.06810155, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 42.56436333, 0.00112871, 51.88679475, 0.01960836, 5.18867948, 0.06810155, -42.56436333, -0.00112871, -51.88679475, -0.01960836, -5.18867948, -0.06810155, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 68.13455519, 0.02257415, 68.13455519, 0.06772246, 47.69418863, -1854.1296694, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 17.0336388, 6.644e-05, 51.10091639, 0.00019931, 170.33638796, 0.00066436, -17.0336388, -6.644e-05, -51.10091639, -0.00019931, -170.33638796, -0.00066436, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 68.13455519, 0.02257415, 68.13455519, 0.06772246, 47.69418863, -1854.1296694, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 17.0336388, 6.644e-05, 51.10091639, 0.00019931, 170.33638796, 0.00066436, -17.0336388, -6.644e-05, -51.10091639, -0.00019931, -170.33638796, -0.00066436, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 5.45, 0.0, 0.0)
    ops.node(124017, 5.45, 0.0, 0.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 170002, 124017, 0.12, 26517997.71690856, 11049165.71537857, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 152.02973751, 0.00084626, 180.68642194, 0.0115783, 18.06864219, 0.02712197, -152.02973751, -0.00084626, -180.68642194, -0.0115783, -18.06864219, -0.02712197, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 184.50153666, 0.00073892, 219.27895849, 0.01241989, 21.92789585, 0.03142358, -184.50153666, -0.00073892, -219.27895849, -0.01241989, -21.92789585, -0.03142358, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 202.83243174, 0.0169251, 202.83243174, 0.0507753, 141.98270222, -4490.56305022, 0.05, 2, 0, 70002, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 50.70810794, 5.278e-05, 152.12432381, 0.00015833, 507.08107936, 0.00052777, -50.70810794, -5.278e-05, -152.12432381, -0.00015833, -507.08107936, -0.00052777, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 248.73188566, 0.01477837, 248.73188566, 0.04433512, 174.11231996, -5297.67713923, 0.05, 2, 0, 70002, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 62.18297141, 6.472e-05, 186.54891424, 0.00019416, 621.82971414, 0.0006472, -62.18297141, -6.472e-05, -186.54891424, -0.00019416, -621.82971414, -0.0006472, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 5.45, 0.0, 1.35)
    ops.node(121002, 5.45, 0.0, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 174017, 121002, 0.12, 29899798.5694064, 12458249.40391933, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 165.98519331, 0.00084158, 197.99383457, 0.01985492, 19.79938346, 0.0497765, -165.98519331, -0.00084158, -197.99383457, -0.01985492, -19.79938346, -0.0497765, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 194.87495412, 0.00072813, 232.45470671, 0.02162915, 23.24547067, 0.05908325, -194.87495412, -0.00072813, -232.45470671, -0.02162915, -23.24547067, -0.05908325, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 241.44495489, 0.01683153, 241.44495489, 0.05049459, 169.01146842, -5544.20700299, 0.05, 2, 0, 74017, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 60.36123872, 5.572e-05, 181.08371616, 0.00016716, 603.61238721, 0.00055718, -60.36123872, -5.572e-05, -181.08371616, -0.00016716, -603.61238721, -0.00055718, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 297.72099, 0.01456258, 297.72099, 0.04368773, 208.404693, -6934.23999844, 0.05, 2, 0, 74017, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 74.4302475, 6.871e-05, 223.2907425, 0.00020612, 744.30247499, 0.00068705, -74.4302475, -6.871e-05, -223.2907425, -0.00020612, -744.30247499, -0.00068705, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.35, 0.0, 0.0)
    ops.node(124018, 8.35, 0.0, 0.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 170003, 124018, 0.12, 29353960.10187443, 12230816.70911434, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 153.53353056, 0.00080593, 182.90491244, 0.01242321, 18.29049124, 0.03302187, -153.53353056, -0.00080593, -182.90491244, -0.01242321, -18.29049124, -0.03302187, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 186.60955946, 0.00071038, 222.30847562, 0.01335486, 22.23084756, 0.03853878, -186.60955946, -0.00071038, -222.30847562, -0.01335486, -22.23084756, -0.03853878, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 220.49796858, 0.01611853, 220.49796858, 0.0483556, 154.34857801, -4429.33499932, 0.05, 2, 0, 70003, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 55.12449215, 5.183e-05, 165.37347644, 0.00015549, 551.24492146, 0.00051831, -55.12449215, -5.183e-05, -165.37347644, -0.00015549, -551.24492146, -0.00051831, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 269.74139688, 0.01420768, 269.74139688, 0.04262303, 188.81897781, -5209.07541463, 0.05, 2, 0, 70003, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 67.43534922, 6.341e-05, 202.30604766, 0.00019022, 674.3534922, 0.00063406, -67.43534922, -6.341e-05, -202.30604766, -0.00019022, -674.3534922, -0.00063406, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 8.35, 0.0, 1.35)
    ops.node(121003, 8.35, 0.0, 2.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4044, 174018, 121003, 0.12, 28446412.30822515, 11852671.79509382, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24044, 168.53170948, 0.0008271, 201.09064076, 0.01947678, 20.10906408, 0.04625863, -168.53170948, -0.0008271, -201.09064076, -0.01947678, -20.10906408, -0.04625863, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14044, 194.59952496, 0.00072245, 232.19454242, 0.02122371, 23.21945424, 0.05474766, -194.59952496, -0.00072245, -232.19454242, -0.02122371, -23.21945424, -0.05474766, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24044, 4044, 0.0, 232.45439075, 0.01654204, 232.45439075, 0.04962611, 162.71807352, -5587.22683118, 0.05, 2, 0, 74018, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44044, 58.11359769, 5.638e-05, 174.34079306, 0.00016915, 581.13597686, 0.00056384, -58.11359769, -5.638e-05, -174.34079306, -0.00016915, -581.13597686, -0.00056384, 0.4, 0.3, 0.003, 0.0, 0.0, 24044, 2)
    ops.limitCurve('ThreePoint', 14044, 4044, 0.0, 287.04363282, 0.01444906, 287.04363282, 0.04334719, 200.93054298, -6998.41241798, 0.05, 2, 0, 74018, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34044, 71.76090821, 6.963e-05, 215.28272462, 0.00020888, 717.60908206, 0.00069626, -71.76090821, -6.963e-05, -215.28272462, -0.00020888, -717.60908206, -0.00069626, 0.4, 0.3, 0.003, 0.0, 0.0, 14044, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4044, 99999, 'P', 44044, 'Vy', 34044, 'Vz', 24044, 'My', 14044, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4044, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4044, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 5.45, 0.0, 2.6)
    ops.node(124019, 5.45, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 171002, 124019, 0.12, 27951959.79522955, 11646649.91467898, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 132.81772737, 0.00080152, 159.30217959, 0.01365571, 15.93021796, 0.03622532, -132.81772737, -0.00080152, -159.30217959, -0.01365571, -15.93021796, -0.03622532, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 161.00961265, 0.00070415, 193.1156536, 0.0146949, 19.31156536, 0.04228851, -161.00961265, -0.00070415, -193.1156536, -0.0146949, -19.31156536, -0.04228851, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 196.09117525, 0.01603036, 196.09117525, 0.04809108, 137.26382268, -3947.34844465, 0.05, 2, 0, 71002, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 49.02279381, 4.841e-05, 147.06838144, 0.00014522, 490.22793814, 0.00048406, -49.02279381, -4.841e-05, -147.06838144, -0.00014522, -490.22793814, -0.00048406, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 240.64856352, 0.0140831, 240.64856352, 0.04224929, 168.45399446, -4835.50160598, 0.05, 2, 0, 71002, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 60.16214088, 5.94e-05, 180.48642264, 0.00017821, 601.6214088, 0.00059405, -60.16214088, -5.94e-05, -180.48642264, -0.00017821, -601.6214088, -0.00059405, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 5.45, 0.0, 3.65)
    ops.node(122002, 5.45, 0.0, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 122002, 0.12, 28344022.70482242, 11810009.46034267, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 129.64003303, 0.00079582, 155.74460359, 0.01377959, 15.57446036, 0.03818717, -129.64003303, -0.00079582, -155.74460359, -0.01377959, -15.57446036, -0.03818717, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 156.73634959, 0.00070033, 188.29708745, 0.01483211, 18.82970874, 0.04467281, -156.73634959, -0.00070033, -188.29708745, -0.01483211, -18.82970874, -0.04467281, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 193.66331425, 0.01591645, 193.66331425, 0.04774935, 135.56431998, -3787.67694884, 0.05, 2, 0, 74019, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 48.41582856, 4.714e-05, 145.24748569, 0.00014143, 484.15828563, 0.00047145, -48.41582856, -4.714e-05, -145.24748569, -0.00014143, -484.15828563, -0.00047145, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 237.65413383, 0.01400651, 237.65413383, 0.04201954, 166.35789368, -4687.22483997, 0.05, 2, 0, 74019, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 59.41353346, 5.785e-05, 178.24060037, 0.00017356, 594.13533458, 0.00057854, -59.41353346, -5.785e-05, -178.24060037, -0.00017356, -594.13533458, -0.00057854, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.35, 0.0, 2.6)
    ops.node(124020, 8.35, 0.0, 3.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 171003, 124020, 0.12, 26951226.28414627, 11229677.61839428, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 134.9745813, 0.00080356, 161.85115613, 0.01332269, 16.18511561, 0.03418924, -134.9745813, -0.00080356, -161.85115613, -0.01332269, -16.18511561, -0.03418924, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 162.21181578, 0.00070829, 194.51195676, 0.01433435, 19.45119568, 0.03984581, -162.21181578, -0.00070829, -194.51195676, -0.01433435, -19.45119568, -0.03984581, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 190.26959179, 0.01607126, 190.26959179, 0.04821379, 133.18871425, -3973.92105924, 0.05, 2, 0, 71003, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 47.56739795, 4.871e-05, 142.70219384, 0.00014614, 475.67397946, 0.00048712, -47.56739795, -4.871e-05, -142.70219384, -0.00014614, -475.67397946, -0.00048712, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 233.73507276, 0.01416589, 233.73507276, 0.04249768, 163.61455093, -4874.72906061, 0.05, 2, 0, 71003, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 58.43376819, 5.984e-05, 175.30130457, 0.00017952, 584.33768189, 0.0005984, -58.43376819, -5.984e-05, -175.30130457, -0.00017952, -584.33768189, -0.0005984, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 8.35, 0.0, 3.65)
    ops.node(122003, 8.35, 0.0, 4.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 122003, 0.12, 27286947.98524707, 11369561.66051961, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 133.69340699, 0.00079414, 160.64873476, 0.01371928, 16.06487348, 0.03644418, -133.69340699, -0.00079414, -160.64873476, -0.01371928, -16.06487348, -0.03644418, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 159.40540798, 0.00070335, 191.54480152, 0.01477132, 19.15448015, 0.04255479, -159.40540798, -0.00070335, -191.54480152, -0.01477132, -19.15448015, -0.04255479, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 187.80828778, 0.01588277, 187.80828778, 0.04764832, 131.46580145, -3831.78724033, 0.05, 2, 0, 74020, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 46.95207195, 4.749e-05, 140.85621584, 0.00014247, 469.52071946, 0.00047491, -46.95207195, -4.749e-05, -140.85621584, -0.00014247, -469.52071946, -0.00047491, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 230.7377604, 0.01406693, 230.7377604, 0.04220079, 161.51643228, -4752.68840588, 0.05, 2, 0, 74020, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 57.6844401, 5.835e-05, 173.0533203, 0.00017504, 576.84440099, 0.00058346, -57.6844401, -5.835e-05, -173.0533203, -0.00017504, -576.84440099, -0.00058346, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 5.45, 0.0, 4.9)
    ops.node(124021, 5.45, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 172002, 124021, 0.0875, 27786675.74057118, 11577781.55857133, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 73.59833084, 0.00090383, 88.47991528, 0.01417646, 8.84799153, 0.04035129, -73.59833084, -0.00090383, -88.47991528, -0.01417646, -8.84799153, -0.04035129, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 101.90771694, 0.00074164, 122.51345999, 0.01546682, 12.251346, 0.04895362, -101.90771694, -0.00074164, -122.51345999, -0.01546682, -12.251346, -0.04895362, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 119.29247987, 0.01807655, 119.29247987, 0.05422966, 83.50473591, -3013.54906936, 0.05, 2, 0, 72002, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 29.82311997, 4.063e-05, 89.4693599, 0.00012188, 298.23119968, 0.00040626, -29.82311997, -4.063e-05, -89.4693599, -0.00012188, -298.23119968, -0.00040626, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 173.9840378, 0.01483276, 173.9840378, 0.04449828, 121.78882646, -3982.87342246, 0.05, 2, 0, 72002, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 43.49600945, 5.925e-05, 130.48802835, 0.00017775, 434.96009451, 0.00059251, -43.49600945, -5.925e-05, -130.48802835, -0.00017775, -434.96009451, -0.00059251, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 5.45, 0.0, 5.95)
    ops.node(123002, 5.45, 0.0, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 123002, 0.0875, 27432290.77154844, 11430121.15481185, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 70.63625738, 0.00086659, 85.17131619, 0.0149758, 8.51713162, 0.04284783, -70.63625738, -0.00086659, -85.17131619, -0.0149758, -8.51713162, -0.04284783, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 97.08078477, 0.00072133, 117.05742239, 0.01637465, 11.70574224, 0.05203277, -97.08078477, -0.00072133, -117.05742239, -0.01637465, -11.70574224, -0.05203277, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 116.08558636, 0.01733172, 116.08558636, 0.05199515, 81.25991045, -2898.47292553, 0.05, 2, 0, 74021, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 29.02139659, 4.004e-05, 87.06418977, 0.00012013, 290.2139659, 0.00040044, -29.02139659, -4.004e-05, -87.06418977, -0.00012013, -290.2139659, -0.00040044, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 166.13818379, 0.01442663, 166.13818379, 0.04327989, 116.29672865, -3932.66255574, 0.05, 2, 0, 74021, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 41.53454595, 5.731e-05, 124.60363784, 0.00017193, 415.34545948, 0.0005731, -41.53454595, -5.731e-05, -124.60363784, -0.00017193, -415.34545948, -0.0005731, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.35, 0.0, 4.9)
    ops.node(124022, 8.35, 0.0, 5.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 172003, 124022, 0.0875, 26366582.23586136, 10986075.9316089, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 74.68530905, 0.00091522, 89.76601002, 0.01416731, 8.976601, 0.03773098, -74.68530905, -0.00091522, -89.76601002, -0.01416731, -8.976601, -0.03773098, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 102.91560358, 0.00075299, 123.69665761, 0.01545537, 12.36966576, 0.04560158, -102.91560358, -0.00075299, -123.69665761, -0.01545537, -12.36966576, -0.04560158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 119.07104689, 0.01830447, 119.07104689, 0.0549134, 83.34973282, -3062.58190641, 0.05, 2, 0, 72003, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 29.76776172, 4.273e-05, 89.30328517, 0.0001282, 297.67761722, 0.00042734, -29.76776172, -4.273e-05, -89.30328517, -0.0001282, -297.67761722, -0.00042734, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 167.64316735, 0.0150597, 167.64316735, 0.0451791, 117.35021714, -4061.86042561, 0.05, 2, 0, 72003, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 41.91079184, 6.017e-05, 125.73237551, 0.0001805, 419.10791837, 0.00060166, -41.91079184, -6.017e-05, -125.73237551, -0.0001805, -419.10791837, -0.00060166, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 8.35, 0.0, 5.95)
    ops.node(123003, 8.35, 0.0, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 123003, 0.0875, 29561045.92235452, 12317102.46764771, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 68.22296523, 0.00088596, 82.10005404, 0.01501528, 8.2100054, 0.0460482, -68.22296523, -0.00088596, -82.10005404, -0.01501528, -8.2100054, -0.0460482, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 95.01109768, 0.00072423, 114.33710376, 0.01639985, 11.43371038, 0.05610185, -95.01109768, -0.00072423, -114.33710376, -0.01639985, -11.43371038, -0.05610185, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 121.83570915, 0.01771929, 121.83570915, 0.05315787, 85.28499641, -2906.71911521, 0.05, 2, 0, 74022, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 30.45892729, 3.9e-05, 91.37678187, 0.000117, 304.58927288, 0.00039001, -30.45892729, -3.9e-05, -91.37678187, -0.000117, -304.58927288, -0.00039001, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 177.44937639, 0.01448457, 177.44937639, 0.04345372, 124.21456347, -3946.1119383, 0.05, 2, 0, 74022, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 44.3623441, 5.68e-05, 133.08703229, 0.00017041, 443.62344098, 0.00056804, -44.3623441, -5.68e-05, -133.08703229, -0.00017041, -443.62344098, -0.00056804, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 5.45, 0.0, 7.2)
    ops.node(124023, 5.45, 0.0, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 173002, 124023, 0.0875, 27613911.03063542, 11505796.26276476, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 46.27635838, 0.00084606, 56.28189236, 0.01676954, 5.62818924, 0.05328151, -46.27635838, -0.00084606, -56.28189236, -0.01676954, -5.62818924, -0.05328151, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 68.37795676, 0.00069847, 83.16213585, 0.0183646, 8.31621358, 0.06507624, -68.37795676, -0.00069847, -83.16213585, -0.0183646, -8.31621358, -0.06507624, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 103.17157036, 0.0169213, 103.17157036, 0.0507639, 72.22009925, -2995.3336885, 0.05, 2, 0, 73002, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 25.79289259, 3.536e-05, 77.37867777, 0.00010607, 257.92892591, 0.00035355, -25.79289259, -3.536e-05, -77.37867777, -0.00010607, -257.92892591, -0.00035355, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 148.14739191, 0.01396937, 148.14739191, 0.04190812, 103.70317434, -4634.18676678, 0.05, 2, 0, 73002, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 37.03684798, 5.077e-05, 111.11054393, 0.0001523, 370.36847977, 0.00050768, -37.03684798, -5.077e-05, -111.11054393, -0.0001523, -370.36847977, -0.00050768, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 5.45, 0.0, 8.25)
    ops.node(124002, 5.45, 0.0, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 124002, 0.0875, 27744747.66448511, 11560311.5268688, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 52.0895916, 0.00085256, 63.51698484, 0.01782206, 6.35169848, 0.05765459, -52.0895916, -0.00085256, -63.51698484, -0.01782206, -6.35169848, -0.05765459, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 72.2740632, 0.00070337, 88.12951753, 0.01952999, 8.81295175, 0.0704898, -72.2740632, -0.00070337, -88.12951753, -0.01952999, -8.81295175, -0.0704898, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 99.28077889, 0.01705129, 99.28077889, 0.05115386, 69.49654522, -3558.33187078, 0.05, 2, 0, 74023, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 24.82019472, 3.386e-05, 74.46058416, 0.00010158, 248.20194721, 0.00033862, -24.82019472, -3.386e-05, -74.46058416, -0.00010158, -248.20194721, -0.00033862, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 141.67321992, 0.01406731, 141.67321992, 0.04220192, 99.17125395, -5905.11664483, 0.05, 2, 0, 74023, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 35.41830498, 4.832e-05, 106.25491494, 0.00014496, 354.1830498, 0.0004832, -35.41830498, -4.832e-05, -106.25491494, -0.00014496, -354.1830498, -0.0004832, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.35, 0.0, 7.2)
    ops.node(124024, 8.35, 0.0, 7.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 173003, 124024, 0.0875, 27358059.12289379, 11399191.30120574, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 47.45262694, 0.00083447, 57.73471296, 0.0164373, 5.7734713, 0.05270027, -47.45262694, -0.00083447, -57.73471296, -0.0164373, -5.7734713, -0.05270027, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 69.90360614, 0.00069527, 85.05039437, 0.01800566, 8.50503944, 0.06439874, -69.90360614, -0.00069527, -85.05039437, -0.01800566, -8.50503944, -0.06439874, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 99.73548594, 0.01668936, 99.73548594, 0.05006807, 69.81484016, -2942.83830573, 0.05, 2, 0, 73003, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 24.93387148, 3.45e-05, 74.80161445, 0.00010349, 249.33871485, 0.00034497, -24.93387148, -3.45e-05, -74.80161445, -0.00010349, -249.33871485, -0.00034497, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 146.19201287, 0.01390542, 146.19201287, 0.04171626, 102.33440901, -4542.82337293, 0.05, 2, 0, 73003, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 36.54800322, 5.057e-05, 109.64400965, 0.0001517, 365.48003217, 0.00050566, -36.54800322, -5.057e-05, -109.64400965, -0.0001517, -365.48003217, -0.00050566, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 8.35, 0.0, 8.25)
    ops.node(124003, 8.35, 0.0, 8.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 124003, 0.0875, 27205570.22213296, 11335654.25922207, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 52.48453864, 0.00082924, 64.06254807, 0.01822157, 6.40625481, 0.05770533, -52.48453864, -0.00082924, -64.06254807, -0.01822157, -6.40625481, -0.05770533, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 72.32013913, 0.00069152, 88.27385186, 0.01998726, 8.82738519, 0.07050086, -72.32013913, -0.00069152, -88.27385186, -0.01998726, -8.82738519, -0.07050086, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 99.91849462, 0.01658481, 99.91849462, 0.04975444, 69.94294623, -3654.72246559, 0.05, 2, 0, 74024, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 24.97962365, 3.475e-05, 74.93887096, 0.00010426, 249.79623654, 0.00034754, -24.97962365, -3.475e-05, -74.93887096, -0.00010426, -249.79623654, -0.00034754, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 140.0156302, 0.01383044, 140.0156302, 0.04149133, 98.01094114, -6079.05903573, 0.05, 2, 0, 74024, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 35.00390755, 4.87e-05, 105.01172265, 0.0001461, 350.0390755, 0.00048701, -35.00390755, -4.87e-05, -105.01172265, -0.0001461, -350.0390755, -0.00048701, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4059, '-orient', 0, 0, 1, 0, 1, 0)
