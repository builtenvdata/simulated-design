import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.25, 28171992.66113896, 11738330.27547457, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 424.60476205, 0.00098088, 513.5015488, 0.03649713, 51.35015488, 0.10227154, -424.60476205, -0.00098088, -513.5015488, -0.03649713, -51.35015488, -0.10227154, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 449.91410459, 0.00098088, 544.10974672, 0.03649713, 54.41097467, 0.10227154, -449.91410459, -0.00098088, -544.10974672, -0.03649713, -54.41097467, -0.10227154, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.5, 0.0, 0.0)
    ops.node(121002, 4.5, 0.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.3025, 30146450.7232196, 12561021.13467483, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 750.65466987, 0.0009056, 902.30909803, 0.05283097, 90.2309098, 0.15283097, -750.65466987, -0.0009056, -902.30909803, -0.05283097, -90.2309098, -0.15283097, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 782.05548041, 0.0009056, 940.05380031, 0.05283097, 94.00538003, 0.15283097, -782.05548041, -0.0009056, -940.05380031, -0.05283097, -94.00538003, -0.15283097, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.5, 0.0, 0.0)
    ops.node(121005, 16.5, 0.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.3025, 28459127.10995806, 11857969.62914919, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 744.92635898, 0.0009395, 897.33320502, 0.05215032, 89.7333205, 0.14829887, -744.92635898, -0.0009395, -897.33320502, -0.05215032, -89.7333205, -0.14829887, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 776.185513, 0.0009395, 934.98776849, 0.05215032, 93.49877685, 0.14829887, -776.185513, -0.0009395, -934.98776849, -0.05215032, -93.49877685, -0.14829887, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 21.0, 0.0, 0.0)
    ops.node(121006, 21.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.25, 28128671.11286058, 11720279.63035857, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 424.86020828, 0.00095492, 513.83650854, 0.03631503, 51.38365085, 0.10197314, -424.86020828, -0.00095492, -513.83650854, -0.03631503, -51.38365085, -0.10197314, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 450.93583227, 0.00095492, 545.37301709, 0.03631503, 54.53730171, 0.10197314, -450.93583227, -0.00095492, -545.37301709, -0.03631503, -54.53730171, -0.10197314, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.5, 0.0)
    ops.node(121007, 0.0, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.4225, 28014913.05918365, 11672880.44132652, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 1153.02747072, 0.00082943, 1394.89203276, 0.05191394, 139.48920328, 0.14260471, -1153.02747072, -0.00082943, -1394.89203276, -0.05191394, -139.48920328, -0.14260471, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 1191.01099919, 0.00082943, 1440.84316801, 0.05191394, 144.0843168, 0.14260471, -1191.01099919, -0.00082943, -1440.84316801, -0.05191394, -144.0843168, -0.14260471, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.5, 4.5, 0.0)
    ops.node(121008, 4.5, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.64, 28849467.95308392, 12020611.6471183, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 2391.0148507, 0.00076194, 2892.132898, 0.08610861, 289.2132898, 0.18610861, -2391.0148507, -0.00076194, -2892.132898, -0.08610861, -289.2132898, -0.18610861, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 2547.56169097, 0.00076194, 3081.48942447, 0.08610861, 308.14894245, 0.18610861, -2547.56169097, -0.00076194, -3081.48942447, -0.08610861, -308.14894245, -0.18610861, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.0, 4.5, 0.0)
    ops.node(121009, 9.0, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.5625, 29357638.77075427, 12232349.48781428, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 1953.49182674, 0.00076267, 2361.05434403, 0.06731275, 236.1054344, 0.16731275, -1953.49182674, -0.00076267, -2361.05434403, -0.06731275, -236.1054344, -0.16731275, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 1953.49182674, 0.00076267, 2361.05434403, 0.06731275, 236.1054344, 0.16731275, -1953.49182674, -0.00076267, -2361.05434403, -0.06731275, -236.1054344, -0.16731275, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.0, 4.5, 0.0)
    ops.node(121010, 12.0, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.5625, 28988809.38776533, 12078670.57823556, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 1947.51303588, 0.00076987, 2355.31539412, 0.06799907, 235.53153941, 0.16799907, -1947.51303588, -0.00076987, -2355.31539412, -0.06799907, -235.53153941, -0.16799907, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 1947.51303588, 0.00076987, 2355.31539412, 0.06799907, 235.53153941, 0.16799907, -1947.51303588, -0.00076987, -2355.31539412, -0.06799907, -235.53153941, -0.16799907, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 16.5, 4.5, 0.0)
    ops.node(121011, 16.5, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.64, 28067695.21309378, 11694873.00545574, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 2366.32615281, 0.00075976, 2865.46987528, 0.08587783, 286.54698753, 0.18587783, -2366.32615281, -0.00075976, -2865.46987528, -0.08587783, -286.54698753, -0.18587783, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 2523.0296472, 0.00075976, 3055.22780108, 0.08587783, 305.52278011, 0.18587783, -2523.0296472, -0.00075976, -3055.22780108, -0.08587783, -305.52278011, -0.18587783, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 21.0, 4.5, 0.0)
    ops.node(121012, 21.0, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.4225, 30379169.23356236, 12657987.18065098, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 1180.44938439, 0.00082261, 1422.65402913, 0.05245037, 142.26540291, 0.1508818, -1180.44938439, -0.00082261, -1422.65402913, -0.05245037, -142.26540291, -0.1508818, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 1218.3476081, 0.00082261, 1468.32821167, 0.05245037, 146.83282117, 0.1508818, -1218.3476081, -0.00082261, -1468.32821167, -0.05245037, -146.83282117, -0.1508818, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.4225, 28963055.11222184, 12067939.63009243, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 1123.12256815, 0.00081324, 1357.00651877, 0.05168236, 135.70065188, 0.14572963, -1123.12256815, -0.00081324, -1357.00651877, -0.05168236, -135.70065188, -0.14572963, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 1123.12256815, 0.00081324, 1357.00651877, 0.05168236, 135.70065188, 0.14572963, -1123.12256815, -0.00081324, -1357.00651877, -0.05168236, -135.70065188, -0.14572963, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.5, 9.0, 0.0)
    ops.node(121014, 4.5, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.64, 29702617.92737174, 12376090.80307156, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 2338.89127384, 0.00072977, 2824.88106526, 0.08647428, 282.48810653, 0.18647428, -2338.89127384, -0.00072977, -2824.88106526, -0.08647428, -282.48810653, -0.18647428, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 2491.75266152, 0.00072977, 3009.50496998, 0.08647428, 300.950497, 0.18647428, -2491.75266152, -0.00072977, -3009.50496998, -0.08647428, -300.950497, -0.18647428, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 9.0, 0.0)
    ops.node(121015, 9.0, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.5625, 28999093.56691035, 12082955.65287931, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 2030.08955264, 0.00077124, 2455.05638944, 0.06841043, 245.50563894, 0.16841043, -2030.08955264, -0.00077124, -2455.05638944, -0.06841043, -245.50563894, -0.16841043, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 1984.73050826, 0.00077124, 2400.20215328, 0.06841043, 240.02021533, 0.16841043, -1984.73050826, -0.00077124, -2400.20215328, -0.06841043, -240.02021533, -0.16841043, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.0, 9.0, 0.0)
    ops.node(121016, 12.0, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.5625, 28951009.78483889, 12062920.74368287, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 2017.41899358, 0.00076289, 2439.92510446, 0.06815594, 243.99251045, 0.16815594, -2017.41899358, -0.00076289, -2439.92510446, -0.06815594, -243.99251045, -0.16815594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 1972.14130003, 0.00076289, 2385.16494729, 0.06815594, 238.51649473, 0.16815594, -1972.14130003, -0.00076289, -2385.16494729, -0.06815594, -238.51649473, -0.16815594, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 16.5, 9.0, 0.0)
    ops.node(121017, 16.5, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.64, 27782287.66946178, 11575953.19560908, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 2394.13731323, 0.0007651, 2900.15438435, 0.08630719, 290.01543844, 0.18630719, -2394.13731323, -0.0007651, -2900.15438435, -0.08630719, -290.01543844, -0.18630719, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 2554.6641442, 0.0007651, 3094.6096439, 0.08630719, 309.46096439, 0.18630719, -2554.6641442, -0.0007651, -3094.6096439, -0.08630719, -309.46096439, -0.18630719, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.4225, 28399578.10402948, 11833157.54334562, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 1114.94789152, 0.0008479, 1348.1966371, 0.05169835, 134.81966371, 0.14379465, -1114.94789152, -0.0008479, -1348.1966371, -0.05169835, -134.81966371, -0.14379465, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 1114.94789152, 0.0008479, 1348.1966371, 0.05169835, 134.81966371, 0.14379465, -1114.94789152, -0.0008479, -1348.1966371, -0.05169835, -134.81966371, -0.14379465, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.25, 28564195.98273878, 11901748.32614116, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 492.33834262, 0.00097839, 595.10711183, 0.04283756, 59.51071118, 0.12108551, -492.33834262, -0.00097839, -595.10711183, -0.04283756, -59.51071118, -0.12108551, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 492.33834262, 0.00097839, 595.10711183, 0.04283756, 59.51071118, 0.12108551, -492.33834262, -0.00097839, -595.10711183, -0.04283756, -59.51071118, -0.12108551, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 4.5, 13.5, 0.0)
    ops.node(121020, 4.5, 13.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.3025, 29334359.91789567, 12222649.96578986, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 757.77346948, 0.00094583, 911.91150715, 0.05287545, 91.19115071, 0.15287545, -757.77346948, -0.00094583, -911.91150715, -0.05287545, -91.19115071, -0.15287545, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 789.2585125, 0.00094583, 949.80089518, 0.05287545, 94.98008952, 0.15287545, -789.2585125, -0.00094583, -949.80089518, -0.05287545, -94.98008952, -0.15287545, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 9.0, 13.5, 0.0)
    ops.node(121021, 9.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.3025, 29985885.61885705, 12494119.0078571, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 766.02039257, 0.00092218, 922.3657335, 0.04480099, 92.23657335, 0.13278202, -766.02039257, -0.00092218, -922.3657335, -0.04480099, -92.23657335, -0.13278202, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 735.09781162, 0.00092218, 885.13183041, 0.04480099, 88.51318304, 0.13278202, -735.09781162, -0.00092218, -885.13183041, -0.04480099, -88.51318304, -0.13278202, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 12.0, 13.5, 0.0)
    ops.node(121022, 12.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.3025, 28869664.30177101, 12029026.79240459, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 776.67113801, 0.00093643, 936.75462814, 0.04502489, 93.67546281, 0.12922454, -776.67113801, -0.00093643, -936.75462814, -0.04502489, -93.67546281, -0.12922454, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 744.34804567, 0.00093643, 897.76926501, 0.04502489, 89.7769265, 0.12922454, -744.34804567, -0.00093643, -897.76926501, -0.04502489, -89.7769265, -0.12922454, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 16.5, 13.5, 0.0)
    ops.node(121023, 16.5, 13.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.3025, 28946368.05670452, 12060986.69029355, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 747.50850942, 0.00092305, 899.97352478, 0.05306789, 89.99735248, 0.15145704, -747.50850942, -0.00092305, -899.97352478, -0.05306789, -89.99735248, -0.15145704, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 779.0491799, 0.00092305, 937.94736458, 0.05306789, 93.79473646, 0.15145704, -779.0491799, -0.00092305, -937.94736458, -0.05306789, -93.79473646, -0.15145704, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.25, 27886354.61364824, 11619314.42235343, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 486.63476226, 0.00098875, 588.69060192, 0.04354498, 58.86906019, 0.11967418, -486.63476226, -0.00098875, -588.69060192, -0.04354498, -58.86906019, -0.11967418, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 486.63476226, 0.00098875, 588.69060192, 0.04354498, 58.86906019, 0.11967418, -486.63476226, -0.00098875, -588.69060192, -0.04354498, -58.86906019, -0.11967418, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.425)
    ops.node(122001, 0.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.25, 29276942.8222922, 12198726.17595509, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 438.69847029, 0.00091561, 531.16799686, 0.03894094, 53.11679969, 0.1132975, -438.69847029, -0.00091561, -531.16799686, -0.03894094, -53.11679969, -0.1132975, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 491.55147365, 0.00091561, 595.16143615, 0.03894094, 59.51614361, 0.1132975, -491.55147365, -0.00091561, -595.16143615, -0.03894094, -59.51614361, -0.1132975, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.5, 0.0, 3.475)
    ops.node(122002, 4.5, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.3025, 29983777.21754815, 12493240.50731173, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 658.19158807, 0.00087469, 793.95518752, 0.03879687, 79.39551875, 0.11774707, -658.19158807, -0.00087469, -793.95518752, -0.03879687, -79.39551875, -0.11774707, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 658.19158807, 0.00087469, 793.95518752, 0.03879687, 79.39551875, 0.11774707, -658.19158807, -0.00087469, -793.95518752, -0.03879687, -79.39551875, -0.11774707, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.5, 0.0, 3.475)
    ops.node(122005, 16.5, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.3025, 28324076.02951979, 11801698.34563325, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 674.89410272, 0.00089573, 816.27597335, 0.0392217, 81.62759733, 0.11380065, -674.89410272, -0.00089573, -816.27597335, -0.0392217, -81.62759733, -0.11380065, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 674.89410272, 0.00089573, 816.27597335, 0.0392217, 81.62759733, 0.11380065, -674.89410272, -0.00089573, -816.27597335, -0.0392217, -81.62759733, -0.11380065, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 21.0, 0.0, 3.425)
    ops.node(122006, 21.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.25, 26719602.6483393, 11133167.77014138, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 431.79143688, 0.00096266, 524.7821359, 0.03808269, 52.47821359, 0.1067989, -431.79143688, -0.00096266, -524.7821359, -0.03808269, -52.47821359, -0.1067989, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 484.31459495, 0.00096266, 588.61669286, 0.03808269, 58.86166929, 0.1067989, -484.31459495, -0.00096266, -588.61669286, -0.03808269, -58.86166929, -0.1067989, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.475)
    ops.node(122007, 0.0, 4.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.4225, 28313317.32499262, 11797215.55208026, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 703.33765109, 0.00077679, 853.07098759, 0.03701405, 85.30709876, 0.10713263, -703.33765109, -0.00077679, -853.07098759, -0.03701405, -85.30709876, -0.10713263, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 807.30032619, 0.00077679, 979.16624466, 0.03701405, 97.91662447, 0.10713263, -807.30032619, -0.00077679, -979.16624466, -0.03701405, -97.91662447, -0.10713263, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.5, 4.5, 3.475)
    ops.node(122008, 4.5, 4.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.64, 29408319.40775915, 12253466.41989965, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 1480.08094657, 0.00069587, 1792.64275357, 0.04369613, 179.26427536, 0.12777683, -1480.08094657, -0.00069587, -1792.64275357, -0.04369613, -179.26427536, -0.12777683, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 1551.72507635, 0.00069587, 1879.41660901, 0.04369613, 187.9416609, 0.12777683, -1551.72507635, -0.00069587, -1879.41660901, -0.04369613, -187.9416609, -0.12777683, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.0, 4.5, 3.475)
    ops.node(122009, 9.0, 4.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.5625, 28869719.10746099, 12029049.62810875, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 1511.62049282, 0.00072563, 1832.88883612, 0.05487643, 183.28888361, 0.15487643, -1511.62049282, -0.00072563, -1832.88883612, -0.05487643, -183.28888361, -0.15487643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 1342.43054164, 0.00072563, 1627.7405372, 0.05487643, 162.77405372, 0.15487643, -1342.43054164, -0.00072563, -1627.7405372, -0.05487643, -162.77405372, -0.15487643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.0, 4.5, 3.475)
    ops.node(122010, 12.0, 4.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.5625, 30144443.78081202, 12560184.90867168, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 1542.95638521, 0.00071961, 1865.91069423, 0.05344101, 186.59106942, 0.15344101, -1542.95638521, -0.00071961, -1865.91069423, -0.05344101, -186.59106942, -0.15344101, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 1370.04083789, 0.00071961, 1656.80240572, 0.05344101, 165.68024057, 0.15344101, -1370.04083789, -0.00071961, -1656.80240572, -0.05344101, -165.68024057, -0.15344101, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 16.5, 4.5, 3.475)
    ops.node(122011, 16.5, 4.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.64, 28061049.99688608, 11692104.1653692, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 1485.71822488, 0.00071347, 1803.88764287, 0.04418642, 180.38876429, 0.12545934, -1485.71822488, -0.00071347, -1803.88764287, -0.04418642, -180.38876429, -0.12545934, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 1558.49532881, 0.00071347, 1892.25010371, 0.04418642, 189.22501037, 0.12545934, -1558.49532881, -0.00071347, -1892.25010371, -0.04418642, -189.22501037, -0.12545934, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.475)
    ops.node(122012, 21.0, 4.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.4225, 30221821.11777773, 12592425.46574072, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 714.82753415, 0.00075604, 863.80932661, 0.0359358, 86.38093266, 0.10951552, -714.82753415, -0.00075604, -863.80932661, -0.0359358, -86.38093266, -0.10951552, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 820.64128446, 0.00075604, 991.67639948, 0.0359358, 99.16763995, 0.10951552, -820.64128446, -0.00075604, -991.67639948, -0.0359358, -99.16763995, -0.10951552, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.475)
    ops.node(122013, 0.0, 9.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.4225, 29278846.50758622, 12199519.37816093, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 868.43802487, 0.00077421, 1051.51847192, 0.03782067, 105.15184719, 0.10979157, -868.43802487, -0.00077421, -1051.51847192, -0.03782067, -105.15184719, -0.10979157, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 904.44856874, 0.00077421, 1095.120607, 0.03782067, 109.5120607, 0.10979157, -904.44856874, -0.00077421, -1095.120607, -0.03782067, -109.5120607, -0.10979157, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.5, 9.0, 3.475)
    ops.node(122014, 4.5, 9.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.64, 30381501.89240102, 12658959.12183376, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 1493.03602465, 0.00068912, 1804.44631998, 0.04292048, 180.444632, 0.12875497, -1493.03602465, -0.00068912, -1804.44631998, -0.04292048, -180.444632, -0.12875497, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 1565.20549663, 0.00068912, 1891.66855438, 0.04292048, 189.16685544, 0.12875497, -1565.20549663, -0.00068912, -1891.66855438, -0.04292048, -189.16685544, -0.12875497, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 9.0, 3.475)
    ops.node(122015, 9.0, 9.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.5625, 30403263.32896081, 12668026.38706701, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 1551.30327496, 0.00071213, 1874.77611552, 0.05372879, 187.47761155, 0.15372879, -1551.30327496, -0.00071213, -1874.77611552, -0.05372879, -187.47761155, -0.15372879, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 1376.0228763, 0.00071213, 1662.94680385, 0.05372879, 166.29468038, 0.15372879, -1376.0228763, -0.00071213, -1662.94680385, -0.05372879, -166.29468038, -0.15372879, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.0, 9.0, 3.475)
    ops.node(122016, 12.0, 9.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.5625, 28732234.16407426, 11971764.23503094, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 1541.47279384, 0.00072776, 1869.4511382, 0.05387485, 186.94511382, 0.15387485, -1541.47279384, -0.00072776, -1869.4511382, -0.05387485, -186.94511382, -0.15387485, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 1365.75231383, 0.00072776, 1656.34270536, 0.05387485, 165.63427054, 0.15387485, -1365.75231383, -0.00072776, -1656.34270536, -0.05387485, -165.63427054, -0.15387485, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 16.5, 9.0, 3.475)
    ops.node(122017, 16.5, 9.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.64, 29083049.60271313, 12117937.3344638, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 1490.7348879, 0.00069579, 1806.71840848, 0.04401449, 180.67184085, 0.12746012, -1490.7348879, -0.00069579, -1806.71840848, -0.04401449, -180.67184085, -0.12746012, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 1564.21003462, 0.00069579, 1895.76770975, 0.04401449, 189.57677097, 0.12746012, -1564.21003462, -0.00069579, -1895.76770975, -0.04401449, -189.57677097, -0.12746012, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.475)
    ops.node(122018, 21.0, 9.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.4225, 27547377.0063777, 11478073.75265738, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 852.59483108, 0.0007901, 1035.26089018, 0.03756638, 103.52608902, 0.10604947, -852.59483108, -0.0007901, -1035.26089018, -0.03756638, -103.52608902, -0.10604947, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 888.06413718, 0.0007901, 1078.32939596, 0.03756638, 107.8329396, 0.10604947, -888.06413718, -0.0007901, -1078.32939596, -0.03756638, -107.8329396, -0.10604947, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.425)
    ops.node(122019, 0.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.25, 28448725.93587481, 11853635.8066145, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 427.72951417, 0.00092427, 518.64331864, 0.03895068, 51.86433186, 0.11161812, -427.72951417, -0.00092427, -518.64331864, -0.03895068, -51.86433186, -0.11161812, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 478.25058778, 0.00092427, 579.90263419, 0.03895068, 57.99026342, 0.11161812, -478.25058778, -0.00092427, -579.90263419, -0.03895068, -57.99026342, -0.11161812, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 4.5, 13.5, 3.475)
    ops.node(122020, 4.5, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.3025, 28833605.38011491, 12014002.24171454, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 668.61749178, 0.00090157, 808.08423246, 0.03908787, 80.80842325, 0.11500847, -668.61749178, -0.00090157, -808.08423246, -0.03908787, -80.80842325, -0.11500847, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 668.61749178, 0.00090157, 808.08423246, 0.03908787, 80.80842325, 0.11500847, -668.61749178, -0.00090157, -808.08423246, -0.03908787, -80.80842325, -0.11500847, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.425)
    ops.node(122021, 9.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.3025, 28524119.93168663, 11885049.9715361, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 688.27445629, 0.00088405, 833.27078992, 0.03954549, 83.32707899, 0.11752086, -688.27445629, -0.00088405, -833.27078992, -0.03954549, -83.32707899, -0.11752086, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 627.2118549, 0.00088405, 759.34434731, 0.03954549, 75.93443473, 0.11752086, -627.2118549, -0.00088405, -759.34434731, -0.03954549, -75.93443473, -0.11752086, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.425)
    ops.node(122022, 12.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.3025, 28475381.74435409, 11864742.39348087, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 673.58995507, 0.00087811, 815.5520996, 0.03996402, 81.55520996, 0.11781248, -673.58995507, -0.00087811, -815.5520996, -0.03996402, -81.55520996, -0.11781248, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 614.80623837, 0.00087811, 744.37944743, 0.03996402, 74.43794474, 0.11781248, -614.80623837, -0.00087811, -744.37944743, -0.03996402, -74.43794474, -0.11781248, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 16.5, 13.5, 3.475)
    ops.node(122023, 16.5, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.3025, 28538810.48410513, 11891171.0350438, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 656.45954502, 0.00087683, 793.72208371, 0.03931559, 79.37220837, 0.11441617, -656.45954502, -0.00087683, -793.72208371, -0.03931559, -79.37220837, -0.11441617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 656.45954502, 0.00087683, 793.72208371, 0.03931559, 79.37220837, 0.11441617, -656.45954502, -0.00087683, -793.72208371, -0.03931559, -79.37220837, -0.11441617, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.425)
    ops.node(122024, 21.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.25, 28523454.06782252, 11884772.52825938, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 440.06323825, 0.00091707, 533.53255318, 0.03858363, 53.35325532, 0.11140589, -440.06323825, -0.00091707, -533.53255318, -0.03858363, -53.35325532, -0.11140589, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 494.36846719, 0.00091707, 599.37219832, 0.03858363, 59.93721983, 0.11140589, -494.36846719, -0.00091707, -599.37219832, -0.03858363, -59.93721983, -0.11140589, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.225)
    ops.node(123001, 0.0, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.25, 28691328.24760136, 11954720.10316724, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 402.05693248, 0.00090987, 488.73137896, 0.04076151, 48.8731379, 0.1205396, -402.05693248, -0.00090987, -488.73137896, -0.04076151, -48.8731379, -0.1205396, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 451.38180682, 0.00090987, 548.68958863, 0.04076151, 54.86895886, 0.1205396, -451.38180682, -0.00090987, -548.68958863, -0.04076151, -54.86895886, -0.1205396, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.5, 0.0, 6.225)
    ops.node(123002, 4.5, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.3025, 28915980.09156365, 12048325.03815152, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 580.91994697, 0.0008525, 704.56930597, 0.04111827, 70.4569306, 0.12599681, -580.91994697, -0.0008525, -704.56930597, -0.04111827, -70.4569306, -0.12599681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 552.25738062, 0.0008525, 669.80588533, 0.04111827, 66.98058853, 0.12599681, -552.25738062, -0.0008525, -669.80588533, -0.04111827, -66.98058853, -0.12599681, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.5, 0.0, 6.225)
    ops.node(123005, 16.5, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.3025, 27723062.9021742, 11551276.20923925, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 601.33643789, 0.0008853, 730.83636573, 0.04042605, 73.08363657, 0.12278218, -601.33643789, -0.0008853, -730.83636573, -0.04042605, -73.08363657, -0.12278218, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 570.60761752, 0.0008853, 693.48998525, 0.04042605, 69.34899853, 0.12278218, -570.60761752, -0.0008853, -693.48998525, -0.04042605, -69.34899853, -0.12278218, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 21.0, 0.0, 6.225)
    ops.node(123006, 21.0, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.25, 29776046.75268529, 12406686.1469522, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 414.33390119, 0.00088882, 502.4377835, 0.039372, 50.24377835, 0.12056507, -414.33390119, -0.00088882, -502.4377835, -0.039372, -50.24377835, -0.12056507, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 466.76502394, 0.00088882, 566.01785028, 0.039372, 56.60178503, 0.12056507, -466.76502394, -0.00088882, -566.01785028, -0.039372, -56.60178503, -0.12056507, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.275)
    ops.node(123007, 0.0, 4.5, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.4225, 28198780.87455999, 11749492.03106667, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 771.25831338, 0.00076769, 938.372897, 0.03948901, 93.8372897, 0.11576785, -771.25831338, -0.00076769, -938.372897, -0.03948901, -93.8372897, -0.11576785, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 878.22368103, 0.00076769, 1068.51528922, 0.03948901, 106.85152892, 0.11576785, -878.22368103, -0.00076769, -1068.51528922, -0.03948901, -106.85152892, -0.11576785, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.5, 4.5, 6.275)
    ops.node(123008, 4.5, 4.5, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.64, 28363421.26852272, 11818092.1952178, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 1298.95810055, 0.00069593, 1580.26449288, 0.03857698, 158.02644929, 0.11396145, -1298.95810055, -0.00069593, -1580.26449288, -0.03857698, -158.02644929, -0.11396145, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 1298.95810055, 0.00069593, 1580.26449288, 0.03857698, 158.02644929, 0.11396145, -1298.95810055, -0.00069593, -1580.26449288, -0.03857698, -158.02644929, -0.11396145, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.275)
    ops.node(123009, 9.0, 4.5, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.5625, 28894102.54073643, 12039209.39197351, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 1534.54794009, 0.00073305, 1864.99022548, 0.04758112, 186.49902255, 0.14206025, -1534.54794009, -0.00073305, -1864.99022548, -0.04758112, -186.49902255, -0.14206025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 1402.74445636, 0.00073305, 1704.80480382, 0.04758112, 170.48048038, 0.14206025, -1402.74445636, -0.00073305, -1704.80480382, -0.04758112, -170.48048038, -0.14206025, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.275)
    ops.node(123010, 12.0, 4.5, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.5625, 27850484.34329462, 11604368.47637276, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 1502.8658551, 0.00073664, 1830.29581855, 0.04807716, 183.02958186, 0.14083597, -1502.8658551, -0.00073664, -1830.29581855, -0.04807716, -183.02958186, -0.14083597, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 1373.86867758, 0.00073664, 1673.19397622, 0.04807716, 167.31939762, 0.14083597, -1373.86867758, -0.00073664, -1673.19397622, -0.04807716, -167.31939762, -0.14083597, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 16.5, 4.5, 6.275)
    ops.node(123011, 16.5, 4.5, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.64, 26970645.92373956, 11237769.13489148, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 1307.47728188, 0.00070804, 1594.55177924, 0.03894035, 159.45517792, 0.11225228, -1307.47728188, -0.00070804, -1594.55177924, -0.03894035, -159.45517792, -0.11225228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 1307.47728188, 0.00070804, 1594.55177924, 0.03894035, 159.45517792, 0.11225228, -1307.47728188, -0.00070804, -1594.55177924, -0.03894035, -159.45517792, -0.11225228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.275)
    ops.node(123012, 21.0, 4.5, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.4225, 28354397.05412301, 11814332.10588459, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 768.30524309, 0.00077053, 934.49918332, 0.0390526, 93.44991833, 0.11555687, -768.30524309, -0.00077053, -934.49918332, -0.0390526, -93.44991833, -0.11555687, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 873.37095983, 0.00077053, 1062.29191592, 0.0390526, 106.22919159, 0.11555687, -873.37095983, -0.00077053, -1062.29191592, -0.0390526, -106.22919159, -0.11555687, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.275)
    ops.node(123013, 0.0, 9.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.4225, 29179792.43480535, 12158246.84783556, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 768.40413245, 0.00076615, 933.01543574, 0.03881035, 93.30154357, 0.11643503, -768.40413245, -0.00076615, -933.01543574, -0.03881035, -93.30154357, -0.11643503, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 871.62860075, 0.00076615, 1058.35315609, 0.03881035, 105.83531561, 0.11643503, -871.62860075, -0.00076615, -1058.35315609, -0.03881035, -105.83531561, -0.11643503, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.5, 9.0, 6.275)
    ops.node(123014, 4.5, 9.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.64, 29511899.12359496, 12296624.63483123, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 1470.5271006, 0.00069309, 1784.56243068, 0.03853287, 178.45624307, 0.11535611, -1470.5271006, -0.00069309, -1784.56243068, -0.03853287, -178.45624307, -0.11535611, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 1399.68751577, 0.00069309, 1698.59484692, 0.03853287, 169.85948469, 0.11535611, -1399.68751577, -0.00069309, -1698.59484692, -0.03853287, -169.85948469, -0.11535611, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.275)
    ops.node(123015, 9.0, 9.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.5625, 28799120.42305537, 11999633.50960641, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 1484.1554567, 0.0007139, 1803.9661064, 0.04771875, 180.39661064, 0.14182224, -1484.1554567, -0.0007139, -1803.9661064, -0.04771875, -180.39661064, -0.14182224, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 1357.57846922, 0.0007139, 1650.11389757, 0.04771875, 165.01138976, 0.14182224, -1357.57846922, -0.0007139, -1650.11389757, -0.04771875, -165.01138976, -0.14182224, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.275)
    ops.node(123016, 12.0, 9.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.5625, 28689745.98277812, 11954060.82615755, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 1521.70799973, 0.00073052, 1850.03541957, 0.04792297, 185.00354196, 0.14185265, -1521.70799973, -0.00073052, -1850.03541957, -0.04792297, -185.00354196, -0.14185265, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 1391.34877697, 0.00073052, 1691.54957378, 0.04792297, 169.15495738, 0.14185265, -1391.34877697, -0.00073052, -1691.54957378, -0.04792297, -169.15495738, -0.14185265, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 16.5, 9.0, 6.275)
    ops.node(123017, 16.5, 9.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.64, 29413992.17863301, 12255830.07443042, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 1477.46662865, 0.00068782, 1793.39032884, 0.038145, 179.33903288, 0.11485396, -1477.46662865, -0.00068782, -1793.39032884, -0.038145, -179.33903288, -0.11485396, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 1405.17362784, 0.00068782, 1705.63906192, 0.038145, 170.56390619, 0.11485396, -1405.17362784, -0.00068782, -1705.63906192, -0.038145, -170.56390619, -0.11485396, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.275)
    ops.node(123018, 21.0, 9.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.4225, 28682349.43846076, 11950978.93269199, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 766.52962222, 0.00076269, 931.72662155, 0.03942147, 93.17266215, 0.1163857, -766.52962222, -0.00076269, -931.72662155, -0.03942147, -93.17266215, -0.1163857, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 871.27592892, 0.00076269, 1059.04710549, 0.03942147, 105.90471055, 0.1163857, -871.27592892, -0.00076269, -1059.04710549, -0.03942147, -105.90471055, -0.1163857, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.225)
    ops.node(123019, 0.0, 13.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.25, 29786819.70148348, 12411174.87561812, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 464.14264795, 0.000902, 562.81123457, 0.04121466, 56.28112346, 0.1223688, -464.14264795, -0.000902, -562.81123457, -0.04121466, -56.28112346, -0.1223688, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 489.56727563, 0.000902, 593.64069218, 0.04121466, 59.36406922, 0.1223688, -489.56727563, -0.000902, -593.64069218, -0.04121466, -59.36406922, -0.1223688, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 4.5, 13.5, 6.225)
    ops.node(123020, 4.5, 13.5, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.3025, 29619982.48268694, 12341659.36778622, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 649.58430776, 0.00086604, 786.68590551, 0.04139514, 78.66859055, 0.12749953, -649.58430776, -0.00086604, -786.68590551, -0.04139514, -78.66859055, -0.12749953, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 592.13243873, 0.00086604, 717.10821547, 0.04139514, 71.71082155, 0.12749953, -592.13243873, -0.00086604, -717.10821547, -0.04139514, -71.71082155, -0.12749953, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.225)
    ops.node(123021, 9.0, 13.5, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.3025, 29462749.74273761, 12276145.72614067, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 706.95100819, 0.00085563, 857.0842153, 0.04269394, 85.70842153, 0.1304344, -706.95100819, -0.00085563, -857.0842153, -0.04269394, -85.70842153, -0.1304344, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 618.0142373, 0.00085563, 749.26019127, 0.04269394, 74.92601913, 0.1304344, -618.0142373, -0.00085563, -749.26019127, -0.04269394, -74.92601913, -0.1304344, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.225)
    ops.node(123022, 12.0, 13.5, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.3025, 28200443.98773813, 11750184.99489089, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 699.99355791, 0.00087673, 850.78282659, 0.04258389, 85.07828266, 0.1280525, -699.99355791, -0.00087673, -850.78282659, -0.04258389, -85.07828266, -0.1280525, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 611.93362061, 0.00087673, 743.75343822, 0.04258389, 74.37534382, 0.1280525, -611.93362061, -0.00087673, -743.75343822, -0.04258389, -74.37534382, -0.1280525, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 16.5, 13.5, 6.225)
    ops.node(123023, 16.5, 13.5, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.3025, 28979479.29863358, 12074783.04109732, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 655.91130917, 0.00086116, 795.39365542, 0.04131546, 79.53936554, 0.12621926, -655.91130917, -0.00086116, -795.39365542, -0.04131546, -79.53936554, -0.12621926, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 596.13707871, 0.00086116, 722.9081791, 0.04131546, 72.29081791, 0.12621926, -596.13707871, -0.00086116, -722.9081791, -0.04131546, -72.29081791, -0.12621926, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.225)
    ops.node(123024, 21.0, 13.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.25, 30123186.53883194, 12551327.72451331, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 473.00192693, 0.00088884, 573.08227337, 0.04065538, 57.30822734, 0.12221002, -473.00192693, -0.00088884, -573.08227337, -0.04065538, -57.30822734, -0.12221002, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 499.60244147, 0.00088884, 605.31107092, 0.04065538, 60.53110709, 0.12221002, -499.60244147, -0.00088884, -605.31107092, -0.04065538, -60.53110709, -0.12221002, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.975)
    ops.node(124001, 0.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.25, 28065363.77186851, 11693901.57161188, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 253.35544473, 0.00090366, 309.39980821, 0.04013659, 30.93998082, 0.12738127, -253.35544473, -0.00090366, -309.39980821, -0.04013659, -30.93998082, -0.12738127, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 275.97789398, 0.00090366, 337.02653424, 0.04013659, 33.70265342, 0.12738127, -275.97789398, -0.00090366, -337.02653424, -0.04013659, -33.70265342, -0.12738127, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.5, 0.0, 9.025)
    ops.node(124002, 4.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.3025, 28856984.96102967, 12023743.73376236, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 441.59445555, 0.00082259, 537.78196314, 0.04251946, 53.77819631, 0.13794275, -441.59445555, -0.00082259, -537.78196314, -0.04251946, -53.77819631, -0.13794275, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 497.73599161, 0.00082259, 606.15217273, 0.04251946, 60.61521727, 0.13794275, -497.73599161, -0.00082259, -606.15217273, -0.04251946, -60.61521727, -0.13794275, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.5, 0.0, 9.025)
    ops.node(124005, 16.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.3025, 29443011.75311004, 12267921.56379585, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 448.75001791, 0.00081807, 545.71282511, 0.04190482, 54.57128251, 0.13784282, -448.75001791, -0.00081807, -545.71282511, -0.04190482, -54.57128251, -0.13784282, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 506.33020814, 0.00081807, 615.73454551, 0.04190482, 61.57345455, 0.13784282, -506.33020814, -0.00081807, -615.73454551, -0.04190482, -61.57345455, -0.13784282, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 21.0, 0.0, 8.975)
    ops.node(124006, 21.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.25, 30048237.24145513, 12520098.85060631, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 256.68309232, 0.00085824, 311.89845569, 0.03913667, 31.18984557, 0.12748261, -256.68309232, -0.00085824, -311.89845569, -0.03913667, -31.18984557, -0.12748261, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 280.06635721, 0.00085824, 340.31171868, 0.03913667, 34.03117187, 0.12748261, -280.06635721, -0.00085824, -340.31171868, -0.03913667, -34.03117187, -0.12748261, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 9.025)
    ops.node(124007, 0.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.4225, 28586722.73181906, 11911134.47159127, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 542.47911306, 0.00073171, 661.54161198, 0.03955167, 66.1541612, 0.1237269, -542.47911306, -0.00073171, -661.54161198, -0.03955167, -66.1541612, -0.1237269, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 609.86168899, 0.00073171, 743.71321422, 0.03955167, 74.37132142, 0.1237269, -609.86168899, -0.00073171, -743.71321422, -0.03955167, -74.37132142, -0.1237269, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.5, 4.5, 9.025)
    ops.node(124008, 4.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.64, 26973401.73501252, 11238917.38958855, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 1100.38416891, 0.0006966, 1346.35746498, 0.04016039, 134.6357465, 0.12094607, -1100.38416891, -0.0006966, -1346.35746498, -0.04016039, -134.6357465, -0.12094607, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 1033.46824831, 0.0006966, 1264.48355969, 0.04016039, 126.44835597, 0.12094607, -1033.46824831, -0.0006966, -1264.48355969, -0.04016039, -126.44835597, -0.12094607, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.0, 4.5, 9.025)
    ops.node(124009, 9.0, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.5625, 29795198.72432537, 12414666.13513557, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 1102.2632314, 0.00069508, 1340.01861034, 0.04054353, 134.00186103, 0.12821116, -1102.2632314, -0.00069508, -1340.01861034, -0.04054353, -134.00186103, -0.12821116, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 1061.03651687, 0.00069508, 1289.89939821, 0.04054353, 128.98993982, 0.12821116, -1061.03651687, -0.00069508, -1289.89939821, -0.04054353, -128.98993982, -0.12821116, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.0, 4.5, 9.025)
    ops.node(124010, 12.0, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.5625, 29650940.71432991, 12354558.6309708, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 1083.46627253, 0.00068671, 1317.67425754, 0.04095886, 131.76742575, 0.12854532, -1083.46627253, -0.00068671, -1317.67425754, -0.04095886, -131.76742575, -0.12854532, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 1042.97671568, 0.00068671, 1268.43225701, 0.04095886, 126.8432257, 0.12854532, -1042.97671568, -0.00068671, -1268.43225701, -0.04095886, -126.8432257, -0.12854532, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 16.5, 4.5, 9.025)
    ops.node(124011, 16.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.64, 29400394.6115024, 12250164.42145933, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 1124.97055971, 0.0006685, 1368.90234383, 0.0385342, 136.89023438, 0.12101844, -1124.97055971, -0.0006685, -1368.90234383, -0.0385342, -136.89023438, -0.12101844, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 1055.64477507, 0.0006685, 1284.54437707, 0.0385342, 128.45443771, 0.12101844, -1055.64477507, -0.0006685, -1284.54437707, -0.0385342, -128.45443771, -0.12101844, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 9.025)
    ops.node(124012, 21.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.4225, 28512480.08505565, 11880200.03543985, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 535.00575696, 0.00073069, 652.54300183, 0.03985903, 65.25430018, 0.1239875, -535.00575696, -0.00073069, -652.54300183, -0.03985903, -65.25430018, -0.1239875, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 600.53854469, 0.00073069, 732.47291186, 0.03985903, 73.24729119, 0.1239875, -600.53854469, -0.00073069, -732.47291186, -0.03985903, -73.24729119, -0.1239875, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.0, 9.025)
    ops.node(124013, 0.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.4225, 30400488.43428635, 12666870.18095265, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 540.4291919, 0.0007152, 655.9241897, 0.03859157, 65.59241897, 0.12376894, -540.4291919, -0.0007152, -655.9241897, -0.03859157, -65.59241897, -0.12376894, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 605.95136001, 0.0007152, 735.44908522, 0.03859157, 73.54490852, 0.12376894, -605.95136001, -0.0007152, -735.44908522, -0.03859157, -73.54490852, -0.12376894, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.5, 9.0, 9.025)
    ops.node(124014, 4.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.64, 28918156.14845604, 12049231.72852335, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 1080.94135478, 0.00067177, 1316.91978546, 0.03965335, 131.69197855, 0.12184572, -1080.94135478, -0.00067177, -1316.91978546, -0.03965335, -131.69197855, -0.12184572, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 1016.80236263, 0.00067177, 1238.77872128, 0.03965335, 123.87787213, 0.12184572, -1016.80236263, -0.00067177, -1238.77872128, -0.03965335, -123.87787213, -0.12184572, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 9.0, 9.025)
    ops.node(124015, 9.0, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.5625, 29755079.90233963, 12397949.95930818, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 1085.70703087, 0.00069075, 1319.90464834, 0.04023021, 131.99046483, 0.1276212, -1085.70703087, -0.00069075, -1319.90464834, -0.04023021, -131.99046483, -0.1276212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 1045.61363886, 0.00069075, 1271.16271984, 0.04023021, 127.11627198, 0.1276212, -1045.61363886, -0.00069075, -1271.16271984, -0.04023021, -127.11627198, -0.1276212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.0, 9.0, 9.025)
    ops.node(124016, 12.0, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.5625, 27717531.24046704, 11548971.3501946, 0.04456055, 0.02900391, 0.02900391, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 1104.70235403, 0.0007109, 1349.5904549, 0.04102222, 134.95904549, 0.12702667, -1104.70235403, -0.0007109, -1349.5904549, -0.04102222, -134.95904549, -0.12702667, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 1062.52995972, 0.0007109, 1298.06937266, 0.04102222, 129.80693727, 0.12702667, -1062.52995972, -0.0007109, -1298.06937266, -0.04102222, -129.80693727, -0.12702667, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 16.5, 9.0, 9.025)
    ops.node(124017, 16.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.64, 29294531.08320606, 12206054.61800253, 0.05768533, 0.03754667, 0.03754667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 1125.50479056, 0.0006802, 1369.9235427, 0.03915949, 136.99235427, 0.12158135, -1125.50479056, -0.0006802, -1369.9235427, -0.03915949, -136.99235427, -0.12158135, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 1057.32084246, 0.0006802, 1286.93251812, 0.03915949, 128.69325181, 0.12158135, -1057.32084246, -0.0006802, -1286.93251812, -0.03915949, -128.69325181, -0.12158135, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 21.0, 9.0, 9.025)
    ops.node(124018, 21.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.4225, 28276579.87146988, 11781908.27977912, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 543.05114314, 0.0007413, 662.72078045, 0.04008141, 66.27207804, 0.1240579, -543.05114314, -0.0007413, -662.72078045, -0.04008141, -66.27207804, -0.1240579, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 610.08793925, 0.0007413, 744.53016139, 0.04008141, 74.45301614, 0.1240579, -610.08793925, -0.0007413, -744.53016139, -0.04008141, -74.45301614, -0.1240579, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 13.5, 8.975)
    ops.node(124019, 0.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.25, 29059762.37737821, 12108234.32390759, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 311.2547876, 0.00090142, 379.20084742, 0.04072542, 37.92008474, 0.12856131, -311.2547876, -0.00090142, -379.20084742, -0.04072542, -37.92008474, -0.12856131, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 311.2547876, 0.00090142, 379.20084742, 0.04072542, 37.92008474, 0.12856131, -311.2547876, -0.00090142, -379.20084742, -0.04072542, -37.92008474, -0.12856131, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 4.5, 13.5, 9.025)
    ops.node(124020, 4.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.3025, 29008850.08368358, 12087020.86820149, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 506.1060391, 0.00082331, 616.121723, 0.04281164, 61.6121723, 0.13837239, -506.1060391, -0.00082331, -616.121723, -0.04281164, -61.6121723, -0.13837239, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 534.70198915, 0.00082331, 650.93376763, 0.04281164, 65.09337676, 0.13837239, -534.70198915, -0.00082331, -650.93376763, -0.04281164, -65.09337676, -0.13837239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 9.025)
    ops.node(124021, 9.0, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.3025, 29430899.32516948, 12262874.71882062, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 578.32020576, 0.00084527, 703.50446293, 0.04420957, 70.35044629, 0.14096746, -578.32020576, -0.00084527, -703.50446293, -0.04420957, -70.35044629, -0.14096746, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 578.32020576, 0.00084527, 703.50446293, 0.04420957, 70.35044629, 0.14096746, -578.32020576, -0.00084527, -703.50446293, -0.04420957, -70.35044629, -0.14096746, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 9.025)
    ops.node(124022, 12.0, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.3025, 30088173.06093352, 12536738.77538897, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 580.17860536, 0.00083938, 704.54082066, 0.04350499, 70.45408207, 0.14073863, -580.17860536, -0.00083938, -704.54082066, -0.04350499, -70.45408207, -0.14073863, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 580.17860536, 0.00083938, 704.54082066, 0.04350499, 70.45408207, 0.14073863, -580.17860536, -0.00083938, -704.54082066, -0.04350499, -70.45408207, -0.14073863, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 16.5, 13.5, 9.025)
    ops.node(124023, 16.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.3025, 29910122.49124818, 12462551.03802007, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 501.83506048, 0.00080989, 609.53078191, 0.04233394, 60.95307819, 0.1386533, -501.83506048, -0.00080989, -609.53078191, -0.04233394, -60.95307819, -0.1386533, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 529.76064625, 0.00080989, 643.44930509, 0.04233394, 64.34493051, 0.1386533, -529.76064625, -0.00080989, -643.44930509, -0.04233394, -64.34493051, -0.1386533, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 21.0, 13.5, 8.975)
    ops.node(124024, 21.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.25, 28340378.52256946, 11808491.05107061, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 313.85973452, 0.00086843, 383.04467312, 0.04122849, 38.30446731, 0.12864531, -313.85973452, -0.00086843, -383.04467312, -0.04122849, -38.30446731, -0.12864531, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 313.85973452, 0.00086843, 383.04467312, 0.04122849, 38.30446731, 0.12864531, -313.85973452, -0.00086843, -383.04467312, -0.04122849, -38.30446731, -0.12864531, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(124025, 9.0, 0.0, 1.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.3025, 28386603.27091398, 11827751.36288082, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 869.48980383, 0.0008347, 1049.08587602, 0.08785233, 104.9085876, 0.18785233, -869.48980383, -0.0008347, -1049.08587602, -0.08785233, -104.9085876, -0.18785233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 837.12576556, 0.0008347, 1010.03693571, 0.08785233, 101.00369357, 0.18785233, -837.12576556, -0.0008347, -1010.03693571, -0.08785233, -101.00369357, -0.18785233, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.8)
    ops.node(121003, 9.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.3025, 27329416.16481504, 11387256.7353396, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 689.25727703, 0.00082242, 833.16864812, 0.06405229, 83.31686481, 0.16405229, -689.25727703, -0.00082242, -833.16864812, -0.06405229, -83.31686481, -0.16405229, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 594.70406466, 0.00082242, 718.87348614, 0.06405229, 71.88734861, 0.16405229, -594.70406466, -0.00082242, -718.87348614, -0.06405229, -71.88734861, -0.16405229, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.0, 0.0, 0.0)
    ops.node(124026, 12.0, 0.0, 1.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.3025, 29187082.31193115, 12161284.29663798, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 875.15436409, 0.0008194, 1054.90399344, 0.08788451, 105.49039934, 0.18788451, -875.15436409, -0.0008194, -1054.90399344, -0.08788451, -105.49039934, -0.18788451, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 842.54688071, 0.0008194, 1015.59919666, 0.08788451, 101.55991967, 0.18788451, -842.54688071, -0.0008194, -1015.59919666, -0.08788451, -101.55991967, -0.18788451, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.8)
    ops.node(121004, 12.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.3025, 28657095.79237412, 11940456.58015588, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 688.14498181, 0.00080407, 830.76907259, 0.06405268, 83.07690726, 0.16405268, -688.14498181, -0.00080407, -830.76907259, -0.06405268, -83.07690726, -0.16405268, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 595.4657943, 0.00080407, 718.88130956, 0.06405268, 71.88813096, 0.16405268, -595.4657943, -0.00080407, -718.88130956, -0.06405268, -71.88813096, -0.16405268, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.425)
    ops.node(124027, 9.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.3025, 28715545.48534923, 11964810.61889551, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 684.58515182, 0.00079007, 828.45349068, 0.08781697, 82.84534907, 0.18781697, -684.58515182, -0.00079007, -828.45349068, -0.08781697, -82.84534907, -0.18781697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 624.05934341, 0.00079007, 755.20793879, 0.08781697, 75.52079388, 0.18781697, -624.05934341, -0.00079007, -755.20793879, -0.08781697, -75.52079388, -0.18781697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.825)
    ops.node(122003, 9.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.3025, 29505996.50175001, 12294165.20906251, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 681.48125132, 0.00078831, 824.25285293, 0.08892515, 82.42528529, 0.18892515, -681.48125132, -0.00078831, -824.25285293, -0.08892515, -82.42528529, -0.18892515, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 621.19237644, 0.00078831, 751.33334557, 0.08892515, 75.13333456, 0.18892515, -621.19237644, -0.00078831, -751.33334557, -0.08892515, -75.13333456, -0.18892515, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.425)
    ops.node(124028, 12.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.3025, 28576250.54640857, 11906771.06100357, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 683.25682906, 0.00078993, 827.02269636, 0.08817052, 82.70226964, 0.18817052, -683.25682906, -0.00078993, -827.02269636, -0.08817052, -82.70226964, -0.18817052, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 622.73701043, 0.00078993, 753.76874344, 0.08817052, 75.37687434, 0.18817052, -622.73701043, -0.00078993, -753.76874344, -0.08817052, -75.37687434, -0.18817052, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.825)
    ops.node(122004, 12.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.3025, 29735496.10630044, 12389790.04429185, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 674.83915605, 0.00078272, 815.84673068, 0.08912306, 81.58467307, 0.18912306, -674.83915605, -0.00078272, -815.84673068, -0.08912306, -81.58467307, -0.18912306, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 615.73074522, 0.00078272, 744.38762328, 0.08912306, 74.43876233, 0.18912306, -615.73074522, -0.00078272, -744.38762328, -0.08912306, -74.43876233, -0.18912306, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.225)
    ops.node(124029, 9.0, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.3025, 28898462.86144735, 12041026.19226973, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 645.14879893, 0.00078782, 783.05832061, 0.07129376, 78.30583206, 0.17129376, -645.14879893, -0.00078782, -783.05832061, -0.07129376, -78.30583206, -0.17129376, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 586.45410174, 0.00078782, 711.81681619, 0.07129376, 71.18168162, 0.17129376, -586.45410174, -0.00078782, -711.81681619, -0.07129376, -71.18168162, -0.17129376, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.55)
    ops.node(123003, 9.0, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.3025, 28211120.30226747, 11754633.45927811, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 401.46983715, 0.00075692, 488.42221917, 0.04024833, 48.84222192, 0.12827496, -401.46983715, -0.00075692, -488.42221917, -0.04024833, -48.84222192, -0.12827496, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 401.46983715, 0.00075692, 488.42221917, 0.04024833, 48.84222192, 0.12827496, -401.46983715, -0.00075692, -488.42221917, -0.04024833, -48.84222192, -0.12827496, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.225)
    ops.node(124030, 12.0, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.3025, 29228268.39425199, 12178445.16427167, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 635.10091638, 0.00078377, 770.33895287, 0.07175649, 77.03389529, 0.17175649, -635.10091638, -0.00078377, -770.33895287, -0.07175649, -77.03389529, -0.17175649, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 578.49789234, 0.00078377, 701.68291232, 0.07175649, 70.16829123, 0.17175649, -578.49789234, -0.00078377, -701.68291232, -0.07175649, -70.16829123, -0.17175649, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.55)
    ops.node(123004, 12.0, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.3025, 27894563.40986128, 11622734.75410887, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 390.75054597, 0.00075193, 475.6604687, 0.0402551, 47.56604687, 0.12773119, -390.75054597, -0.00075193, -475.6604687, -0.0402551, -47.56604687, -0.12773119, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 390.75054597, 0.00075193, 475.6604687, 0.0402551, 47.56604687, 0.12773119, -390.75054597, -0.00075193, -475.6604687, -0.0402551, -47.56604687, -0.12773119, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 9.025)
    ops.node(124031, 9.0, 0.0, 9.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.3025, 29180137.97929075, 12158390.82470448, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 364.70496936, 0.00074459, 443.9300087, 0.04057938, 44.39300087, 0.13714156, -364.70496936, -0.00074459, -443.9300087, -0.04057938, -44.39300087, -0.13714156, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 364.70496936, 0.00074459, 443.9300087, 0.04057938, 44.39300087, 0.13714156, -364.70496936, -0.00074459, -443.9300087, -0.04057938, -44.39300087, -0.13714156, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 9.0, 0.0, 10.35)
    ops.node(124003, 9.0, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.3025, 28249596.73326936, 11770665.3055289, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 357.42913574, 0.00074159, 436.46552327, 0.04268723, 43.64655233, 0.14133879, -357.42913574, -0.00074159, -436.46552327, -0.04268723, -43.64655233, -0.14133879, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 357.42913574, 0.00074159, 436.46552327, 0.04268723, 43.64655233, 0.14133879, -357.42913574, -0.00074159, -436.46552327, -0.04268723, -43.64655233, -0.14133879, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 9.025)
    ops.node(124032, 12.0, 0.0, 9.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.3025, 28884505.83171959, 12035210.7632165, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 362.05451374, 0.0007382, 441.02322807, 0.04110371, 44.10232281, 0.13742906, -362.05451374, -0.0007382, -441.02322807, -0.04110371, -44.10232281, -0.13742906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 362.05451374, 0.0007382, 441.02322807, 0.04110371, 44.10232281, 0.13742906, -362.05451374, -0.0007382, -441.02322807, -0.04110371, -44.10232281, -0.13742906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 12.0, 0.0, 10.35)
    ops.node(124004, 12.0, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.3025, 28326437.18227691, 11802682.15928205, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 354.0643987, 0.00074716, 432.27791765, 0.04243213, 43.22779176, 0.14112791, -354.0643987, -0.00074716, -432.27791765, -0.04243213, -43.22779176, -0.14112791, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 354.0643987, 0.00074716, 432.27791765, 0.04243213, 43.22779176, 0.14112791, -354.0643987, -0.00074716, -432.27791765, -0.04243213, -43.22779176, -0.14112791, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
