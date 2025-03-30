import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.0625, 27822730.79933828, 11592804.49972428, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 47.00437851, 0.00110965, 55.83731389, 0.01624273, 5.58373139, 0.04336267, -47.00437851, -0.00110965, -55.83731389, -0.01624273, -5.58373139, -0.04336267, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 49.58002472, 0.00110965, 58.89696855, 0.01624273, 5.88969686, 0.04336267, -49.58002472, -0.00110965, -58.89696855, -0.01624273, -5.88969686, -0.04336267, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 78.80321321, 0.0221929, 78.80321321, 0.0665787, 55.16224925, -798.3110636, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 19.7008033, 0.00012073, 59.10240991, 0.00036218, 197.00803302, 0.00120725, -19.7008033, -0.00012073, -59.10240991, -0.00036218, -197.00803302, -0.00120725, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 78.80321321, 0.0221929, 78.80321321, 0.0665787, 55.16224925, -798.3110636, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 19.7008033, 0.00012073, 59.10240991, 0.00036218, 197.00803302, 0.00120725, -19.7008033, -0.00012073, -59.10240991, -0.00036218, -197.00803302, -0.00120725, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.15, 0.0, 0.0)
    ops.node(121002, 4.15, 0.0, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.09, 29604556.89257659, 12335232.03857358, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 92.29239325, 0.00095605, 109.53400329, 0.01606186, 10.95340033, 0.03904664, -92.29239325, -0.00095605, -109.53400329, -0.01606186, -10.95340033, -0.03904664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 99.18001967, 0.00095605, 117.70834213, 0.01606186, 11.77083421, 0.03904664, -99.18001967, -0.00095605, -117.70834213, -0.01606186, -11.77083421, -0.03904664, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 111.15393211, 0.01912107, 111.15393211, 0.0573632, 77.80775248, -1030.64749275, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 27.78848303, 0.00011114, 83.36544908, 0.00033341, 277.88483028, 0.00111137, -27.78848303, -0.00011114, -83.36544908, -0.00033341, -277.88483028, -0.00111137, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 111.15393211, 0.01912107, 111.15393211, 0.0573632, 77.80775248, -1030.64749275, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 27.78848303, 0.00011114, 83.36544908, 0.00033341, 277.88483028, 0.00111137, -27.78848303, -0.00011114, -83.36544908, -0.00033341, -277.88483028, -0.00111137, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 15.4, 0.0, 0.0)
    ops.node(121005, 15.4, 0.0, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.09, 29350185.11536952, 12229243.79807063, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 93.01728225, 0.00094308, 110.38836387, 0.01595388, 11.03883639, 0.03841489, -93.01728225, -0.00094308, -110.38836387, -0.01595388, -11.03883639, -0.03841489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 100.36910578, 0.00094308, 119.11314867, 0.01595388, 11.91131487, 0.03841489, -100.36910578, -0.00094308, -119.11314867, -0.01595388, -11.91131487, -0.03841489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 110.06977214, 0.01886163, 110.06977214, 0.05658488, 77.0488405, -1026.11724149, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 27.51744303, 0.00011101, 82.5523291, 0.00033302, 275.17443035, 0.00111007, -27.51744303, -0.00011101, -82.5523291, -0.00033302, -275.17443035, -0.00111007, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 110.06977214, 0.01886163, 110.06977214, 0.05658488, 77.0488405, -1026.11724149, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 27.51744303, 0.00011101, 82.5523291, 0.00033302, 275.17443035, 0.00111007, -27.51744303, -0.00011101, -82.5523291, -0.00033302, -275.17443035, -0.00111007, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 19.55, 0.0, 0.0)
    ops.node(121006, 19.55, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.0625, 29316645.48374938, 12215268.95156224, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 48.17591134, 0.00105662, 57.2817086, 0.01706817, 5.72817086, 0.04840625, -48.17591134, -0.00105662, -57.2817086, -0.01706817, -5.72817086, -0.04840625, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 51.14196406, 0.00105662, 60.80837915, 0.01706817, 6.08083792, 0.04840625, -51.14196406, -0.00105662, -60.80837915, -0.01706817, -6.08083792, -0.04840625, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 82.493446, 0.02113248, 82.493446, 0.06339743, 57.7454122, -807.43295848, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 20.6233615, 0.00011994, 61.8700845, 0.00035982, 206.233615, 0.00119939, -20.6233615, -0.00011994, -61.8700845, -0.00035982, -206.233615, -0.00119939, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 82.493446, 0.02113248, 82.493446, 0.06339743, 57.7454122, -807.43295848, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 20.6233615, 0.00011994, 61.8700845, 0.00035982, 206.233615, 0.00119939, -20.6233615, -0.00011994, -61.8700845, -0.00035982, -206.233615, -0.00119939, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.85, 0.0)
    ops.node(121007, 0.0, 4.85, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 29108038.54940441, 12128349.39558517, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 139.77772246, 0.00082208, 166.93553641, 0.01686143, 16.69355364, 0.04068423, -139.77772246, -0.00082208, -166.93553641, -0.01686143, -16.69355364, -0.04068423, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 148.16261184, 0.00082208, 176.94954996, 0.01686143, 17.694955, 0.04068423, -148.16261184, -0.00082208, -176.94954996, -0.01686143, -17.694955, -0.04068423, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 133.97411618, 0.01644158, 133.97411618, 0.04932474, 93.78188133, -1120.10867532, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 33.49352905, 0.00010009, 100.48058714, 0.00030028, 334.93529046, 0.00100094, -33.49352905, -0.00010009, -100.48058714, -0.00030028, -334.93529046, -0.00100094, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 133.97411618, 0.01644158, 133.97411618, 0.04932474, 93.78188133, -1120.10867532, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 33.49352905, 0.00010009, 100.48058714, 0.00030028, 334.93529046, 0.00100094, -33.49352905, -0.00010009, -100.48058714, -0.00030028, -334.93529046, -0.00100094, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.15, 4.85, 0.0)
    ops.node(121008, 4.15, 4.85, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.16, 28772788.93017679, 11988662.05424033, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 237.8421867, 0.00075704, 284.24023817, 0.01494882, 28.42402382, 0.03294673, -237.8421867, -0.00075704, -284.24023817, -0.01494882, -28.42402382, -0.03294673, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 256.97781501, 0.00075704, 307.10882858, 0.01494882, 30.71088286, 0.03294673, -256.97781501, -0.00075704, -307.10882858, -0.01494882, -30.71088286, -0.03294673, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 158.44099929, 0.01514072, 158.44099929, 0.04542215, 110.9086995, -1231.1122899, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 39.61024982, 9.169e-05, 118.83074947, 0.00027506, 396.10249822, 0.00091685, -39.61024982, -9.169e-05, -118.83074947, -0.00027506, -396.10249822, -0.00091685, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 158.44099929, 0.01514072, 158.44099929, 0.04542215, 110.9086995, -1231.1122899, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 39.61024982, 9.169e-05, 118.83074947, 0.00027506, 396.10249822, 0.00091685, -39.61024982, -9.169e-05, -118.83074947, -0.00027506, -396.10249822, -0.00091685, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 8.3, 4.85, 0.0)
    ops.node(121009, 8.3, 4.85, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 29763744.8946366, 12401560.37276525, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 247.27561336, 0.00074892, 295.49234702, 0.01590506, 29.5492347, 0.03540199, -247.27561336, -0.00074892, -295.49234702, -0.01590506, -29.5492347, -0.03540199, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 247.27561336, 0.00074892, 295.49234702, 0.01590506, 29.5492347, 0.03540199, -247.27561336, -0.00074892, -295.49234702, -0.01590506, -29.5492347, -0.03540199, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 163.39528937, 0.01497845, 163.39528937, 0.04493535, 114.37670256, -1223.47565648, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 40.84882234, 9.14e-05, 122.54646702, 0.00027421, 408.48822342, 0.00091404, -40.84882234, -9.14e-05, -122.54646702, -0.00027421, -408.48822342, -0.00091404, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 163.39528937, 0.01497845, 163.39528937, 0.04493535, 114.37670256, -1223.47565648, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 40.84882234, 9.14e-05, 122.54646702, 0.00027421, 408.48822342, 0.00091404, -40.84882234, -9.14e-05, -122.54646702, -0.00027421, -408.48822342, -0.00091404, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 11.25, 4.85, 0.0)
    ops.node(121010, 11.25, 4.85, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 29032683.72199382, 12096951.55083076, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 240.83749108, 0.00077508, 287.91327167, 0.0159439, 28.79132717, 0.03450104, -240.83749108, -0.00077508, -287.91327167, -0.0159439, -28.79132717, -0.03450104, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 240.83749108, 0.00077508, 287.91327167, 0.0159439, 28.79132717, 0.03450104, -240.83749108, -0.00077508, -287.91327167, -0.0159439, -28.79132717, -0.03450104, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 159.93866502, 0.01550161, 159.93866502, 0.04650484, 111.95706551, -1229.27929677, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 39.98466626, 9.172e-05, 119.95399877, 0.00027517, 399.84666255, 0.00091723, -39.98466626, -9.172e-05, -119.95399877, -0.00027517, -399.84666255, -0.00091723, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 159.93866502, 0.01550161, 159.93866502, 0.04650484, 111.95706551, -1229.27929677, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 39.98466626, 9.172e-05, 119.95399877, 0.00027517, 399.84666255, 0.00091723, -39.98466626, -9.172e-05, -119.95399877, -0.00027517, -399.84666255, -0.00091723, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 15.4, 4.85, 0.0)
    ops.node(121011, 15.4, 4.85, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 28948284.03663175, 12061785.01526323, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 231.65663589, 0.00077225, 276.83864972, 0.01514967, 27.68386497, 0.03338444, -231.65663589, -0.00077225, -276.83864972, -0.01514967, -27.68386497, -0.03338444, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 248.95465567, 0.00077225, 297.51045316, 0.01514967, 29.75104532, 0.03338444, -248.95465567, -0.00077225, -297.51045316, -0.01514967, -29.75104532, -0.03338444, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 159.4720358, 0.01544503, 159.4720358, 0.0463351, 111.63042506, -1232.77032327, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 39.86800895, 9.172e-05, 119.60402685, 0.00027517, 398.6800895, 0.00091723, -39.86800895, -9.172e-05, -119.60402685, -0.00027517, -398.6800895, -0.00091723, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 159.4720358, 0.01544503, 159.4720358, 0.0463351, 111.63042506, -1232.77032327, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 39.86800895, 9.172e-05, 119.60402685, 0.00027517, 398.6800895, 0.00091723, -39.86800895, -9.172e-05, -119.60402685, -0.00027517, -398.6800895, -0.00091723, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 19.55, 4.85, 0.0)
    ops.node(121012, 19.55, 4.85, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 29768114.55131588, 12403381.06304828, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 138.80544087, 0.00081916, 165.72381455, 0.01710333, 16.57238146, 0.04205731, -138.80544087, -0.00081916, -165.72381455, -0.01710333, -16.57238146, -0.04205731, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 146.85811829, 0.00081916, 175.3381381, 0.01710333, 17.53381381, 0.04205731, -146.85811829, -0.00081916, -175.3381381, -0.01710333, -17.53381381, -0.04205731, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 136.18822636, 0.01638311, 136.18822636, 0.04914934, 95.33175845, -1112.73352985, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 34.04705659, 9.949e-05, 102.14116977, 0.00029847, 340.47056591, 0.00099492, -34.04705659, -9.949e-05, -102.14116977, -0.00029847, -340.47056591, -0.00099492, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 136.18822636, 0.01638311, 136.18822636, 0.04914934, 95.33175845, -1112.73352985, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 34.04705659, 9.949e-05, 102.14116977, 0.00029847, 340.47056591, 0.00099492, -34.04705659, -9.949e-05, -102.14116977, -0.00029847, -340.47056591, -0.00099492, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.7, 0.0)
    ops.node(121013, 0.0, 9.7, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0625, 29558680.10729924, 12316116.71137469, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 49.58359233, 0.0010771, 58.95847069, 0.01796164, 5.89584707, 0.04999246, -49.58359233, -0.0010771, -58.95847069, -0.01796164, -5.89584707, -0.04999246, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 54.71335164, 0.0010771, 65.05812482, 0.01796164, 6.50581248, 0.04999246, -54.71335164, -0.0010771, -65.05812482, -0.01796164, -6.50581248, -0.04999246, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 83.02905805, 0.02154209, 83.02905805, 0.06462626, 58.12034063, -807.69125272, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 20.75726451, 0.00011973, 62.27179354, 0.00035919, 207.57264512, 0.00119729, -20.75726451, -0.00011973, -62.27179354, -0.00035919, -207.57264512, -0.00119729, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 83.02905805, 0.02154209, 83.02905805, 0.06462626, 58.12034063, -807.69125272, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 20.75726451, 0.00011973, 62.27179354, 0.00035919, 207.57264512, 0.00119729, -20.75726451, -0.00011973, -62.27179354, -0.00035919, -207.57264512, -0.00119729, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.15, 9.7, 0.0)
    ops.node(121014, 4.15, 9.7, 3.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.09, 28532222.42798179, 11888426.01165908, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 95.40543657, 0.00096943, 113.17639719, 0.01571569, 11.31763972, 0.03648683, -95.40543657, -0.00096943, -113.17639719, -0.01571569, -11.31763972, -0.03648683, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 106.15888369, 0.00096943, 125.93286524, 0.01571569, 12.59328652, 0.03648683, -106.15888369, -0.00096943, -125.93286524, -0.01571569, -12.59328652, -0.03648683, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 107.60726518, 0.01938858, 107.60726518, 0.05816575, 75.32508562, -1026.86225341, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 26.90181629, 0.00011163, 80.70544888, 0.0003349, 269.01816294, 0.00111634, -26.90181629, -0.00011163, -80.70544888, -0.0003349, -269.01816294, -0.00111634, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 107.60726518, 0.01938858, 107.60726518, 0.05816575, 75.32508562, -1026.86225341, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 26.90181629, 0.00011163, 80.70544888, 0.0003349, 269.01816294, 0.00111634, -26.90181629, -0.00011163, -80.70544888, -0.0003349, -269.01816294, -0.00111634, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 8.3, 9.7, 0.0)
    ops.node(121015, 8.3, 9.7, 3.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.0625, 29524053.25041422, 12301688.85433926, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 64.43099427, 0.00116331, 76.00617138, 0.01615751, 7.60061714, 0.04135325, -64.43099427, -0.00116331, -76.00617138, -0.01615751, -7.60061714, -0.04135325, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 67.29744472, 0.00116331, 79.38758628, 0.01615751, 7.93875863, 0.04135325, -67.29744472, -0.00116331, -79.38758628, -0.01615751, -7.93875863, -0.04135325, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 88.22406618, 0.02326628, 88.22406618, 0.06979884, 61.75684632, -919.45208765, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 22.05601654, 0.00012737, 66.16804963, 0.00038211, 220.56016544, 0.00127369, -22.05601654, -0.00012737, -66.16804963, -0.00038211, -220.56016544, -0.00127369, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 88.22406618, 0.02326628, 88.22406618, 0.06979884, 61.75684632, -919.45208765, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 22.05601654, 0.00012737, 66.16804963, 0.00038211, 220.56016544, 0.00127369, -22.05601654, -0.00012737, -66.16804963, -0.00038211, -220.56016544, -0.00127369, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 11.25, 9.7, 0.0)
    ops.node(121016, 11.25, 9.7, 3.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.0625, 28709464.04057002, 11962276.68357084, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 64.61024043, 0.00117548, 76.14406232, 0.01568737, 7.61440623, 0.03858782, -64.61024043, -0.00117548, -76.14406232, -0.01568737, -7.61440623, -0.03858782, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 67.56709479, 0.00117548, 79.6287561, 0.01568737, 7.96287561, 0.03858782, -67.56709479, -0.00117548, -79.6287561, -0.01568737, -7.96287561, -0.03858782, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 86.79669795, 0.02350954, 86.79669795, 0.07052862, 60.75768856, -925.96577085, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 21.69917449, 0.00012886, 65.09752346, 0.00038659, 216.99174487, 0.00128864, -21.69917449, -0.00012886, -65.09752346, -0.00038659, -216.99174487, -0.00128864, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 86.79669795, 0.02350954, 86.79669795, 0.07052862, 60.75768856, -925.96577085, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 21.69917449, 0.00012886, 65.09752346, 0.00038659, 216.99174487, 0.00128864, -21.69917449, -0.00012886, -65.09752346, -0.00038659, -216.99174487, -0.00128864, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 15.4, 9.7, 0.0)
    ops.node(121017, 15.4, 9.7, 3.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.09, 30201579.21782729, 12583991.34076137, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 95.51096339, 0.00098585, 113.35594327, 0.01649307, 11.33559433, 0.04071915, -95.51096339, -0.00098585, -113.35594327, -0.01649307, -11.33559433, -0.04071915, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 105.26893194, 0.00098585, 124.93706118, 0.01649307, 12.49370612, 0.04071915, -105.26893194, -0.00098585, -124.93706118, -0.01649307, -12.49370612, -0.04071915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 112.48653974, 0.01971692, 112.48653974, 0.05915076, 78.74057782, -1021.86063529, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 28.12163494, 0.00011025, 84.36490481, 0.00033074, 281.21634936, 0.00110246, -28.12163494, -0.00011025, -84.36490481, -0.00033074, -281.21634936, -0.00110246, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 112.48653974, 0.01971692, 112.48653974, 0.05915076, 78.74057782, -1021.86063529, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 28.12163494, 0.00011025, 84.36490481, 0.00033074, 281.21634936, 0.00110246, -28.12163494, -0.00011025, -84.36490481, -0.00033074, -281.21634936, -0.00110246, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 19.55, 9.7, 0.0)
    ops.node(121018, 19.55, 9.7, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.0625, 30441083.63528915, 12683784.84803715, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 50.43202398, 0.00110947, 59.94989224, 0.01819406, 5.99498922, 0.05250789, -50.43202398, -0.00110947, -59.94989224, -0.01819406, -5.99498922, -0.05250789, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 55.46961473, 0.00110947, 65.93821076, 0.01819406, 6.59382108, 0.05250789, -55.46961473, -0.00110947, -65.93821076, -0.01819406, -6.59382108, -0.05250789, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 85.07301956, 0.02218948, 85.07301956, 0.06656844, 59.55111369, -810.20196168, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 21.26825489, 0.00011912, 63.80476467, 0.00035736, 212.68254891, 0.0011912, -21.26825489, -0.00011912, -63.80476467, -0.00035736, -212.68254891, -0.0011912, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 85.07301956, 0.02218948, 85.07301956, 0.06656844, 59.55111369, -810.20196168, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 21.26825489, 0.00011912, 63.80476467, 0.00035736, 212.68254891, 0.0011912, -21.26825489, -0.00011912, -63.80476467, -0.00035736, -212.68254891, -0.0011912, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.95)
    ops.node(122001, 0.0, 0.0, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.0625, 29481137.17334965, 12283807.15556235, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 39.29636763, 0.00096449, 47.04548756, 0.01885803, 4.70454876, 0.05784102, -39.29636763, -0.00096449, -47.04548756, -0.01885803, -4.70454876, -0.05784102, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 41.42745715, 0.00096449, 49.59682122, 0.01885803, 4.95968212, 0.05784102, -41.42745715, -0.00096449, -49.59682122, -0.01885803, -4.95968212, -0.05784102, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 77.28190975, 0.01928973, 77.28190975, 0.05786919, 54.09733683, -852.0596709, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 19.32047744, 9.362e-05, 57.96143231, 0.00028085, 193.20477438, 0.00093616, -19.32047744, -9.362e-05, -57.96143231, -0.00028085, -193.20477438, -0.00093616, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 77.28190975, 0.01928973, 77.28190975, 0.05786919, 54.09733683, -852.0596709, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 19.32047744, 9.362e-05, 57.96143231, 0.00028085, 193.20477438, 0.00093616, -19.32047744, -9.362e-05, -57.96143231, -0.00028085, -193.20477438, -0.00093616, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.15, 0.0, 3.9)
    ops.node(122002, 4.15, 0.0, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.09, 30412020.66071639, 12671675.27529849, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 76.09320107, 0.00080882, 90.88104578, 0.01749872, 9.08810458, 0.04728888, -76.09320107, -0.00080882, -90.88104578, -0.01749872, -9.08810458, -0.04728888, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 79.4548262, 0.00080882, 94.89596437, 0.01749872, 9.48959644, 0.04728888, -79.4548262, -0.00080882, -94.89596437, -0.01749872, -9.48959644, -0.04728888, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 105.35160431, 0.01617648, 105.35160431, 0.04852943, 73.74612302, -1038.17254224, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 26.33790108, 8.591e-05, 79.01370323, 0.00025773, 263.37901077, 0.00085911, -26.33790108, -8.591e-05, -79.01370323, -0.00025773, -263.37901077, -0.00085911, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 105.35160431, 0.01617648, 105.35160431, 0.04852943, 73.74612302, -1038.17254224, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 26.33790108, 8.591e-05, 79.01370323, 0.00025773, 263.37901077, 0.00085911, -26.33790108, -8.591e-05, -79.01370323, -0.00025773, -263.37901077, -0.00085911, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 15.4, 0.0, 3.9)
    ops.node(122005, 15.4, 0.0, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.09, 28274496.97854435, 11781040.40772681, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 75.07328588, 0.00083017, 89.76082304, 0.01700206, 8.9760823, 0.04274831, -75.07328588, -0.00083017, -89.76082304, -0.01700206, -8.9760823, -0.04274831, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 78.37909704, 0.00083017, 93.71339187, 0.01700206, 9.37133919, 0.04274831, -78.37909704, -0.00083017, -93.71339187, -0.01700206, -9.37133919, -0.04274831, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 99.16192663, 0.01660331, 99.16192663, 0.04980993, 69.41334864, -1040.75607498, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 24.79048166, 8.698e-05, 74.37144497, 0.00026093, 247.90481657, 0.00086976, -24.79048166, -8.698e-05, -74.37144497, -0.00026093, -247.90481657, -0.00086976, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 99.16192663, 0.01660331, 99.16192663, 0.04980993, 69.41334864, -1040.75607498, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 24.79048166, 8.698e-05, 74.37144497, 0.00026093, 247.90481657, 0.00086976, -24.79048166, -8.698e-05, -74.37144497, -0.00026093, -247.90481657, -0.00086976, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 19.55, 0.0, 3.95)
    ops.node(122006, 19.55, 0.0, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.0625, 29505554.99546578, 12293981.24811074, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 39.1994413, 0.00091198, 46.92854882, 0.01921345, 4.69285488, 0.05825457, -39.1994413, -0.00091198, -46.92854882, -0.01921345, -4.69285488, -0.05825457, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 41.56567717, 0.00091198, 49.7613447, 0.01921345, 4.97613447, 0.05825457, -41.56567717, -0.00091198, -49.7613447, -0.01921345, -4.97613447, -0.05825457, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 77.58441239, 0.01823958, 77.58441239, 0.05471875, 54.30908867, -857.79855795, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 19.3961031, 9.39e-05, 58.18830929, 0.00028171, 193.96103098, 0.00093904, -19.3961031, -9.39e-05, -58.18830929, -0.00028171, -193.96103098, -0.00093904, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 77.58441239, 0.01823958, 77.58441239, 0.05471875, 54.30908867, -857.79855795, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 19.3961031, 9.39e-05, 58.18830929, 0.00028171, 193.96103098, 0.00093904, -19.3961031, -9.39e-05, -58.18830929, -0.00028171, -193.96103098, -0.00093904, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.85, 3.95)
    ops.node(122007, 0.0, 4.85, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 28186091.72620538, 11744204.88591891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 96.73736594, 0.00069496, 116.2820402, 0.01707208, 11.62820402, 0.04393175, -96.73736594, -0.00069496, -116.2820402, -0.01707208, -11.62820402, -0.04393175, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 92.77122587, 0.00069496, 111.51458706, 0.01707208, 11.15145871, 0.04393175, -92.77122587, -0.00069496, -111.51458706, -0.01707208, -11.15145871, -0.04393175, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 121.23782454, 0.01389915, 121.23782454, 0.04169746, 84.86647718, -1141.22039413, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 30.30945614, 7.837e-05, 90.92836841, 0.00023512, 303.09456135, 0.00078372, -30.30945614, -7.837e-05, -90.92836841, -0.00023512, -303.09456135, -0.00078372, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 121.23782454, 0.01389915, 121.23782454, 0.04169746, 84.86647718, -1141.22039413, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 30.30945614, 7.837e-05, 90.92836841, 0.00023512, 303.09456135, 0.00078372, -30.30945614, -7.837e-05, -90.92836841, -0.00023512, -303.09456135, -0.00078372, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.15, 4.85, 3.925)
    ops.node(122008, 4.15, 4.85, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.16, 29334061.25741038, 12222525.52392099, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 141.55516488, 0.00064291, 169.99838903, 0.01480331, 16.9998389, 0.03659832, -141.55516488, -0.00064291, -169.99838903, -0.01480331, -16.9998389, -0.03659832, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 141.55516488, 0.00064291, 169.99838903, 0.01480331, 16.9998389, 0.03659832, -141.55516488, -0.00064291, -169.99838903, -0.01480331, -16.9998389, -0.03659832, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 151.1942528, 0.01285827, 151.1942528, 0.03857482, 105.83597696, -1237.54930642, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 37.7985632, 7.19e-05, 113.3956896, 0.0002157, 377.985632, 0.00071901, -37.7985632, -7.19e-05, -113.3956896, -0.0002157, -377.985632, -0.00071901, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 151.1942528, 0.01285827, 151.1942528, 0.03857482, 105.83597696, -1237.54930642, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 37.7985632, 7.19e-05, 113.3956896, 0.0002157, 377.985632, 0.00071901, -37.7985632, -7.19e-05, -113.3956896, -0.0002157, -377.985632, -0.00071901, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 8.3, 4.85, 3.925)
    ops.node(122009, 8.3, 4.85, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 28364455.65409087, 11818523.18920453, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 141.19920726, 0.00064965, 169.7754753, 0.01478995, 16.97754753, 0.03569255, -141.19920726, -0.00064965, -169.7754753, -0.01478995, -16.97754753, -0.03569255, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 141.19920726, 0.00064965, 169.7754753, 0.01478995, 16.97754753, 0.03569255, -141.19920726, -0.00064965, -169.7754753, -0.01478995, -16.97754753, -0.03569255, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 145.00810385, 0.01299308, 145.00810385, 0.03897923, 101.5056727, -1210.95842106, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 36.25202596, 7.132e-05, 108.75607789, 0.00021395, 362.52025964, 0.00071317, -36.25202596, -7.132e-05, -108.75607789, -0.00021395, -362.52025964, -0.00071317, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 145.00810385, 0.01299308, 145.00810385, 0.03897923, 101.5056727, -1210.95842106, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 36.25202596, 7.132e-05, 108.75607789, 0.00021395, 362.52025964, 0.00071317, -36.25202596, -7.132e-05, -108.75607789, -0.00021395, -362.52025964, -0.00071317, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 11.25, 4.85, 3.925)
    ops.node(122010, 11.25, 4.85, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 28502347.76707625, 11875978.23628177, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 140.82732957, 0.00064927, 169.31335435, 0.01499339, 16.93133543, 0.03606493, -140.82732957, -0.00064927, -169.31335435, -0.01499339, -16.93133543, -0.03606493, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 140.82732957, 0.00064927, 169.31335435, 0.01499339, 16.93133543, 0.03606493, -140.82732957, -0.00064927, -169.31335435, -0.01499339, -16.93133543, -0.03606493, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 145.88699722, 0.01298534, 145.88699722, 0.03895602, 102.12089806, -1214.535586, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 36.47174931, 7.14e-05, 109.41524792, 0.00021421, 364.71749306, 0.00071402, -36.47174931, -7.14e-05, -109.41524792, -0.00021421, -364.71749306, -0.00071402, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 145.88699722, 0.01298534, 145.88699722, 0.03895602, 102.12089806, -1214.535586, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 36.47174931, 7.14e-05, 109.41524792, 0.00021421, 364.71749306, 0.00071402, -36.47174931, -7.14e-05, -109.41524792, -0.00021421, -364.71749306, -0.00071402, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 15.4, 4.85, 3.925)
    ops.node(122011, 15.4, 4.85, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 29711434.97458602, 12379764.57274417, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 142.75952693, 0.00063629, 171.37152333, 0.01473977, 17.13715233, 0.03695719, -142.75952693, -0.00063629, -171.37152333, -0.01473977, -17.13715233, -0.03695719, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 142.75952693, 0.00063629, 171.37152333, 0.01473977, 17.13715233, 0.03695719, -142.75952693, -0.00063629, -171.37152333, -0.01473977, -17.13715233, -0.03695719, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 152.93167817, 0.01272583, 152.93167817, 0.03817749, 107.05217472, -1234.1260021, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 38.23291954, 7.18e-05, 114.69875863, 0.00021541, 382.32919543, 0.00071804, -38.23291954, -7.18e-05, -114.69875863, -0.00021541, -382.32919543, -0.00071804, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 152.93167817, 0.01272583, 152.93167817, 0.03817749, 107.05217472, -1234.1260021, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 38.23291954, 7.18e-05, 114.69875863, 0.00021541, 382.32919543, 0.00071804, -38.23291954, -7.18e-05, -114.69875863, -0.00021541, -382.32919543, -0.00071804, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 19.55, 4.85, 3.95)
    ops.node(122012, 19.55, 4.85, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 28835944.71810736, 12014976.96587807, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 96.8179459, 0.00069781, 116.33073275, 0.0172783, 11.63307327, 0.04518803, -96.8179459, -0.00069781, -116.33073275, -0.0172783, -11.63307327, -0.04518803, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 92.93814884, 0.00069781, 111.66899746, 0.0172783, 11.16689975, 0.04518803, -92.93814884, -0.00069781, -111.66899746, -0.0172783, -11.16689975, -0.04518803, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 123.40697531, 0.01395613, 123.40697531, 0.04186839, 86.38488272, -1134.63542758, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 30.85174383, 7.798e-05, 92.55523148, 0.00023393, 308.51743828, 0.00077976, -30.85174383, -7.798e-05, -92.55523148, -0.00023393, -308.51743828, -0.00077976, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 123.40697531, 0.01395613, 123.40697531, 0.04186839, 86.38488272, -1134.63542758, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 30.85174383, 7.798e-05, 92.55523148, 0.00023393, 308.51743828, 0.00077976, -30.85174383, -7.798e-05, -92.55523148, -0.00023393, -308.51743828, -0.00077976, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.7, 3.95)
    ops.node(122013, 0.0, 9.7, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0625, 28414397.05274494, 11839332.10531039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 39.56323026, 0.0009213, 47.38967329, 0.01886337, 4.73896733, 0.0551861, -39.56323026, -0.0009213, -47.38967329, -0.01886337, -4.73896733, -0.0551861, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 42.10693041, 0.0009213, 50.4365711, 0.01886337, 5.04365711, 0.0551861, -42.10693041, -0.0009213, -50.4365711, -0.01886337, -5.04365711, -0.0551861, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 75.47207121, 0.01842597, 75.47207121, 0.05527791, 52.83044985, -859.80047638, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 18.8680178, 9.486e-05, 56.60405341, 0.00028457, 188.68017804, 0.00094855, -18.8680178, -9.486e-05, -56.60405341, -0.00028457, -188.68017804, -0.00094855, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 75.47207121, 0.01842597, 75.47207121, 0.05527791, 52.83044985, -859.80047638, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 18.8680178, 9.486e-05, 56.60405341, 0.00028457, 188.68017804, 0.00094855, -18.8680178, -9.486e-05, -56.60405341, -0.00028457, -188.68017804, -0.00094855, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.15, 9.7, 3.875)
    ops.node(122014, 4.15, 9.7, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.09, 28819413.93867648, 12008089.1411152, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 78.89164228, 0.00082731, 94.3232784, 0.01721427, 9.43232784, 0.04405688, -78.89164228, -0.00082731, -94.3232784, -0.01721427, -9.43232784, -0.04405688, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 85.64065432, 0.00082731, 102.39243405, 0.01721427, 10.23924341, 0.04405688, -85.64065432, -0.00082731, -102.39243405, -0.01721427, -10.23924341, -0.04405688, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 100.18005221, 0.01654614, 100.18005221, 0.04963843, 70.12603655, -1029.2961786, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 25.04501305, 8.621e-05, 75.13503916, 0.00025862, 250.45013053, 0.00086208, -25.04501305, -8.621e-05, -75.13503916, -0.00025862, -250.45013053, -0.00086208, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 100.18005221, 0.01654614, 100.18005221, 0.04963843, 70.12603655, -1029.2961786, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 25.04501305, 8.621e-05, 75.13503916, 0.00025862, 250.45013053, 0.00086208, -25.04501305, -8.621e-05, -75.13503916, -0.00025862, -250.45013053, -0.00086208, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 8.3, 9.7, 3.875)
    ops.node(122015, 8.3, 9.7, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.0625, 29154531.46772906, 12147721.44488711, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 49.2673953, 0.00096031, 58.61929636, 0.01792064, 5.86192964, 0.04947379, -49.2673953, -0.00096031, -58.61929636, -0.01792064, -5.86192964, -0.04947379, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 54.59673456, 0.00096031, 64.96024692, 0.01792064, 6.49602469, 0.04947379, -54.59673456, -0.00096031, -64.96024692, -0.01792064, -6.49602469, -0.04947379, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 82.12908793, 0.01920618, 82.12908793, 0.05761853, 57.49036155, -962.39753974, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 20.53227198, 0.0001006, 61.59681594, 0.0003018, 205.32271982, 0.00100602, -20.53227198, -0.0001006, -61.59681594, -0.0003018, -205.32271982, -0.00100602, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 82.12908793, 0.01920618, 82.12908793, 0.05761853, 57.49036155, -962.39753974, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 20.53227198, 0.0001006, 61.59681594, 0.0003018, 205.32271982, 0.00100602, -20.53227198, -0.0001006, -61.59681594, -0.0003018, -205.32271982, -0.00100602, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 11.25, 9.7, 3.875)
    ops.node(122016, 11.25, 9.7, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.0625, 29422481.4410108, 12259367.26708784, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 49.87366727, 0.00094821, 59.34132483, 0.0177872, 5.93413248, 0.05006133, -49.87366727, -0.00094821, -59.34132483, -0.0177872, -5.93413248, -0.05006133, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 55.57942008, 0.00094821, 66.13021663, 0.0177872, 6.61302166, 0.05006133, -55.57942008, -0.00094821, -66.13021663, -0.0177872, -6.61302166, -0.05006133, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 82.34893344, 0.01896418, 82.34893344, 0.05689255, 57.64425341, -955.1553385, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 20.58723336, 9.995e-05, 61.76170008, 0.00029986, 205.8723336, 0.00099952, -20.58723336, -9.995e-05, -61.76170008, -0.00029986, -205.8723336, -0.00099952, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 82.34893344, 0.01896418, 82.34893344, 0.05689255, 57.64425341, -955.1553385, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 20.58723336, 9.995e-05, 61.76170008, 0.00029986, 205.8723336, 0.00099952, -20.58723336, -9.995e-05, -61.76170008, -0.00029986, -205.8723336, -0.00099952, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 15.4, 9.7, 3.875)
    ops.node(122017, 15.4, 9.7, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.09, 28763916.87455272, 11984965.36439697, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 78.23533242, 0.00084384, 93.5396489, 0.01728461, 9.35396489, 0.04401762, -78.23533242, -0.00084384, -93.5396489, -0.01728461, -9.35396489, -0.04401762, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 84.57280728, 0.00084384, 101.11685418, 0.01728461, 10.11168542, 0.04401762, -84.57280728, -0.00084384, -101.11685418, -0.01728461, -10.11168542, -0.04401762, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 100.04449923, 0.01687681, 100.04449923, 0.05063042, 70.03114946, -1029.83764169, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 25.01112481, 8.626e-05, 75.03337442, 0.00025877, 250.11124808, 0.00086258, -25.01112481, -8.626e-05, -75.03337442, -0.00025877, -250.11124808, -0.00086258, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 100.04449923, 0.01687681, 100.04449923, 0.05063042, 70.03114946, -1029.83764169, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 25.01112481, 8.626e-05, 75.03337442, 0.00025877, 250.11124808, 0.00086258, -25.01112481, -8.626e-05, -75.03337442, -0.00025877, -250.11124808, -0.00086258, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 19.55, 9.7, 3.95)
    ops.node(122018, 19.55, 9.7, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.0625, 29813771.69456388, 12422404.87273495, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 39.11367805, 0.00090756, 46.81330759, 0.01904559, 4.68133076, 0.05881011, -39.11367805, -0.00090756, -46.81330759, -0.01904559, -4.68133076, -0.05881011, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 41.44529223, 0.00090756, 49.6039061, 0.01904559, 4.96039061, 0.05881011, -41.44529223, -0.00090756, -49.6039061, -0.01904559, -4.96039061, -0.05881011, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 77.74923043, 0.01815113, 77.74923043, 0.05445339, 54.4244613, -847.30069392, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 19.43730761, 9.313e-05, 58.31192282, 0.00027939, 194.37307607, 0.00093131, -19.43730761, -9.313e-05, -58.31192282, -0.00027939, -194.37307607, -0.00093131, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 77.74923043, 0.01815113, 77.74923043, 0.05445339, 54.4244613, -847.30069392, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 19.43730761, 9.313e-05, 58.31192282, 0.00027939, 194.37307607, 0.00093131, -19.43730761, -9.313e-05, -58.31192282, -0.00027939, -194.37307607, -0.00093131, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 7.05)
    ops.node(123001, 0.0, 0.0, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 29456380.08809245, 12273491.70337186, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 27.96880231, 0.00083097, 33.71047629, 0.02046009, 3.37104763, 0.06801271, -27.96880231, -0.00083097, -33.71047629, -0.02046009, -3.37104763, -0.06801271, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 27.96880231, 0.00083097, 33.71047629, 0.02046009, 3.37104763, 0.06801271, -27.96880231, -0.00083097, -33.71047629, -0.02046009, -3.37104763, -0.06801271, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 71.48077399, 0.01661949, 71.48077399, 0.04985847, 50.0365418, -784.8683271, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 17.8701935, 8.666e-05, 53.6105805, 0.00025998, 178.70193499, 0.00086661, -17.8701935, -8.666e-05, -53.6105805, -0.00025998, -178.70193499, -0.00086661, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 71.48077399, 0.01661949, 71.48077399, 0.04985847, 50.0365418, -784.8683271, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 17.8701935, 8.666e-05, 53.6105805, 0.00025998, 178.70193499, 0.00086661, -17.8701935, -8.666e-05, -53.6105805, -0.00025998, -178.70193499, -0.00086661, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.15, 0.0, 6.975)
    ops.node(123002, 4.15, 0.0, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.0625, 29505534.20344594, 12293972.58476914, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 44.54771876, 0.00096851, 53.31561852, 0.01882937, 5.33156185, 0.05238072, -44.54771876, -0.00096851, -53.31561852, -0.01882937, -5.33156185, -0.05238072, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 44.54771876, 0.00096851, 53.31561852, 0.01882937, 5.33156185, 0.05238072, -44.54771876, -0.00096851, -53.31561852, -0.01882937, -5.33156185, -0.05238072, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 72.7143136, 0.01937013, 72.7143136, 0.05811038, 50.90001952, -769.20347609, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 18.1785784, 8.801e-05, 54.5357352, 0.00026403, 181.785784, 0.0008801, -18.1785784, -8.801e-05, -54.5357352, -0.00026403, -181.785784, -0.0008801, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 72.7143136, 0.01937013, 72.7143136, 0.05811038, 50.90001952, -769.20347609, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 18.1785784, 8.801e-05, 54.5357352, 0.00026403, 181.785784, 0.0008801, -18.1785784, -8.801e-05, -54.5357352, -0.00026403, -181.785784, -0.0008801, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 15.4, 0.0, 6.975)
    ops.node(123005, 15.4, 0.0, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 29240689.8067724, 12183620.75282183, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 44.69242024, 0.00095227, 53.49853047, 0.01842188, 5.34985305, 0.05141685, -44.69242024, -0.00095227, -53.49853047, -0.01842188, -5.34985305, -0.05141685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 44.69242024, 0.00095227, 53.49853047, 0.01842188, 5.34985305, 0.05141685, -44.69242024, -0.00095227, -53.49853047, -0.01842188, -5.34985305, -0.05141685, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 69.8955737, 0.01904545, 69.8955737, 0.05713636, 48.92690159, -761.46993022, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 17.47389342, 8.536e-05, 52.42168027, 0.00025609, 174.73893424, 0.00085364, -17.47389342, -8.536e-05, -52.42168027, -0.00025609, -174.73893424, -0.00085364, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 69.8955737, 0.01904545, 69.8955737, 0.05713636, 48.92690159, -761.46993022, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 17.47389342, 8.536e-05, 52.42168027, 0.00025609, 174.73893424, 0.00085364, -17.47389342, -8.536e-05, -52.42168027, -0.00025609, -174.73893424, -0.00085364, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 19.55, 0.0, 7.05)
    ops.node(123006, 19.55, 0.0, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 30227655.90669308, 12594856.62778878, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 27.80179176, 0.00088207, 33.46571979, 0.02017409, 3.34657198, 0.06908843, -27.80179176, -0.00088207, -33.46571979, -0.02017409, -3.34657198, -0.06908843, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 27.80179176, 0.00088207, 33.46571979, 0.02017409, 3.34657198, 0.06908843, -27.80179176, -0.00088207, -33.46571979, -0.02017409, -3.34657198, -0.06908843, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 72.41813578, 0.01764142, 72.41813578, 0.05292427, 50.69269505, -769.54345355, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 18.10453395, 8.556e-05, 54.31360184, 0.00025667, 181.04533946, 0.00085557, -18.10453395, -8.556e-05, -54.31360184, -0.00025667, -181.04533946, -0.00085557, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 72.41813578, 0.01764142, 72.41813578, 0.05292427, 50.69269505, -769.54345355, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 18.10453395, 8.556e-05, 54.31360184, 0.00025667, 181.04533946, 0.00085557, -18.10453395, -8.556e-05, -54.31360184, -0.00025667, -181.04533946, -0.00085557, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.85, 7.05)
    ops.node(123007, 0.0, 4.85, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 29673107.50280973, 12363794.79283739, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 45.95271077, 0.00095286, 54.95888571, 0.01867108, 5.49588857, 0.0520054, -45.95271077, -0.00095286, -54.95888571, -0.01867108, -5.49588857, -0.0520054, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 45.95271077, 0.00095286, 54.95888571, 0.01867108, 5.49588857, 0.0520054, -45.95271077, -0.00095286, -54.95888571, -0.01867108, -5.49588857, -0.0520054, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 74.03059244, 0.01905712, 74.03059244, 0.05717136, 51.82141471, -787.21657868, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 18.50764811, 8.91e-05, 55.52294433, 0.00026729, 185.07648111, 0.00089097, -18.50764811, -8.91e-05, -55.52294433, -0.00026729, -185.07648111, -0.00089097, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 74.03059244, 0.01905712, 74.03059244, 0.05717136, 51.82141471, -787.21657868, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 18.50764811, 8.91e-05, 55.52294433, 0.00026729, 185.07648111, 0.00089097, -18.50764811, -8.91e-05, -55.52294433, -0.00026729, -185.07648111, -0.00089097, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.15, 4.85, 6.975)
    ops.node(123008, 4.15, 4.85, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 28635075.94096793, 11931281.64206997, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 100.37016937, 0.00070111, 120.83076286, 0.01555708, 12.08307629, 0.03958733, -100.37016937, -0.00070111, -120.83076286, -0.01555708, -12.08307629, -0.03958733, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 100.37016937, 0.00070111, 120.83076286, 0.01555708, 12.08307629, 0.03958733, -100.37016937, -0.00070111, -120.83076286, -0.01555708, -12.08307629, -0.03958733, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 112.22397089, 0.01402216, 112.22397089, 0.04206649, 78.55677962, -927.20115287, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 28.05599272, 7.141e-05, 84.16797817, 0.00021422, 280.55992722, 0.00071408, -28.05599272, -7.141e-05, -84.16797817, -0.00021422, -280.55992722, -0.00071408, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 112.22397089, 0.01402216, 112.22397089, 0.04206649, 78.55677962, -927.20115287, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 28.05599272, 7.141e-05, 84.16797817, 0.00021422, 280.55992722, 0.00071408, -28.05599272, -7.141e-05, -84.16797817, -0.00021422, -280.55992722, -0.00071408, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 8.3, 4.85, 6.975)
    ops.node(123009, 8.3, 4.85, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 29963530.92484351, 12484804.55201813, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 98.91158132, 0.00069057, 118.94218438, 0.0163762, 11.89421844, 0.04233572, -98.91158132, -0.00069057, -118.94218438, -0.0163762, -11.89421844, -0.04233572, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 98.91158132, 0.00069057, 118.94218438, 0.0163762, 11.89421844, 0.04233572, -98.91158132, -0.00069057, -118.94218438, -0.0163762, -11.89421844, -0.04233572, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 116.95953071, 0.01381141, 116.95953071, 0.04143423, 81.8716715, -920.65520046, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 29.23988268, 7.112e-05, 87.71964803, 0.00021336, 292.39882677, 0.00071121, -29.23988268, -7.112e-05, -87.71964803, -0.00021336, -292.39882677, -0.00071121, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 116.95953071, 0.01381141, 116.95953071, 0.04143423, 81.8716715, -920.65520046, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 29.23988268, 7.112e-05, 87.71964803, 0.00021336, 292.39882677, 0.00071121, -29.23988268, -7.112e-05, -87.71964803, -0.00021336, -292.39882677, -0.00071121, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 11.25, 4.85, 6.975)
    ops.node(123010, 11.25, 4.85, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 31136101.84242232, 12973375.76767597, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 97.41266447, 0.00068979, 116.89101003, 0.01650291, 11.689101, 0.0436332, -97.41266447, -0.00068979, -116.89101003, -0.01650291, -11.689101, -0.0436332, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 97.41266447, 0.00068979, 116.89101003, 0.01650291, 11.689101, 0.0436332, -97.41266447, -0.00068979, -116.89101003, -0.01650291, -11.689101, -0.0436332, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 121.31656185, 0.01379579, 121.31656185, 0.04138737, 84.92159329, -916.33330602, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 30.32914046, 7.099e-05, 90.98742139, 0.00021298, 303.29140462, 0.00070993, -30.32914046, -7.099e-05, -90.98742139, -0.00021298, -303.29140462, -0.00070993, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 121.31656185, 0.01379579, 121.31656185, 0.04138737, 84.92159329, -916.33330602, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 30.32914046, 7.099e-05, 90.98742139, 0.00021298, 303.29140462, 0.00070993, -30.32914046, -7.099e-05, -90.98742139, -0.00021298, -303.29140462, -0.00070993, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 15.4, 4.85, 6.975)
    ops.node(123011, 15.4, 4.85, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 29493935.56057769, 12289139.81690737, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 99.00322438, 0.00069819, 119.07178204, 0.01608298, 11.9071782, 0.04113644, -99.00322438, -0.00069819, -119.07178204, -0.01608298, -11.9071782, -0.04113644, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 99.00322438, 0.00069819, 119.07178204, 0.01608298, 11.9071782, 0.04113644, -99.00322438, -0.00069819, -119.07178204, -0.01608298, -11.9071782, -0.04113644, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 115.81566583, 0.01396371, 115.81566583, 0.04189113, 81.07096608, -933.29308687, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 28.95391646, 7.155e-05, 86.86174937, 0.00021464, 289.53916458, 0.00071547, -28.95391646, -7.155e-05, -86.86174937, -0.00021464, -289.53916458, -0.00071547, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 115.81566583, 0.01396371, 115.81566583, 0.04189113, 81.07096608, -933.29308687, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 28.95391646, 7.155e-05, 86.86174937, 0.00021464, 289.53916458, 0.00071547, -28.95391646, -7.155e-05, -86.86174937, -0.00021464, -289.53916458, -0.00071547, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 19.55, 4.85, 7.05)
    ops.node(123012, 19.55, 4.85, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 30597044.86677891, 12748768.69449121, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 46.25881724, 0.00093183, 55.27278255, 0.01886708, 5.52727825, 0.05404664, -46.25881724, -0.00093183, -55.27278255, -0.01886708, -5.52727825, -0.05404664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 46.25881724, 0.00093183, 55.27278255, 0.01886708, 5.52727825, 0.05404664, -46.25881724, -0.00093183, -55.27278255, -0.01886708, -5.52727825, -0.05404664, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 75.9002558, 0.01863658, 75.9002558, 0.05590974, 53.13017906, -784.51840893, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 18.97506395, 8.859e-05, 56.92519185, 0.00026577, 189.7506395, 0.00088589, -18.97506395, -8.859e-05, -56.92519185, -0.00026577, -189.7506395, -0.00088589, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 75.9002558, 0.01863658, 75.9002558, 0.05590974, 53.13017906, -784.51840893, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 18.97506395, 8.859e-05, 56.92519185, 0.00026577, 189.7506395, 0.00088589, -18.97506395, -8.859e-05, -56.92519185, -0.00026577, -189.7506395, -0.00088589, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.7, 7.05)
    ops.node(123013, 0.0, 9.7, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 29135056.63365114, 12139606.93068798, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 27.97654711, 0.00084659, 33.73561224, 0.02060669, 3.37356122, 0.0675575, -27.97654711, -0.00084659, -33.73561224, -0.02060669, -3.37356122, -0.0675575, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 27.97654711, 0.00084659, 33.73561224, 0.02060669, 3.37356122, 0.0675575, -27.97654711, -0.00084659, -33.73561224, -0.02060669, -3.37356122, -0.0675575, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 71.19409853, 0.01693172, 71.19409853, 0.05079517, 49.83586897, -793.98817495, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 17.79852463, 8.727e-05, 53.3955739, 0.0002618, 177.98524634, 0.00087265, -17.79852463, -8.727e-05, -53.3955739, -0.0002618, -177.98524634, -0.00087265, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 71.19409853, 0.01693172, 71.19409853, 0.05079517, 49.83586897, -793.98817495, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 17.79852463, 8.727e-05, 53.3955739, 0.0002618, 177.98524634, 0.00087265, -17.79852463, -8.727e-05, -53.3955739, -0.0002618, -177.98524634, -0.00087265, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.15, 9.7, 6.975)
    ops.node(123014, 4.15, 9.7, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 29643926.87312956, 12351636.19713732, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 45.41094467, 0.00095806, 54.342774, 0.01850525, 5.4342774, 0.05234239, -45.41094467, -0.00095806, -54.342774, -0.01850525, -5.4342774, -0.05234239, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 45.41094467, 0.00095806, 54.342774, 0.01850525, 5.4342774, 0.05234239, -45.41094467, -0.00095806, -54.342774, -0.01850525, -5.4342774, -0.05234239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 71.0840513, 0.0191612, 71.0840513, 0.0574836, 49.75883591, -755.59503089, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 17.77101282, 8.563e-05, 53.31303847, 0.0002569, 177.71012825, 0.00085635, -17.77101282, -8.563e-05, -53.31303847, -0.0002569, -177.71012825, -0.00085635, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 71.0840513, 0.0191612, 71.0840513, 0.0574836, 49.75883591, -755.59503089, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 17.77101282, 8.563e-05, 53.31303847, 0.0002569, 177.71012825, 0.00085635, -17.77101282, -8.563e-05, -53.31303847, -0.0002569, -177.71012825, -0.00085635, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 8.3, 9.7, 6.975)
    ops.node(123015, 8.3, 9.7, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 29332768.68434987, 12221986.95181245, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 36.55613131, 0.00091443, 43.8727328, 0.01941879, 4.38727328, 0.06085078, -36.55613131, -0.00091443, -43.8727328, -0.01941879, -4.38727328, -0.06085078, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 38.81516723, 0.00091443, 46.58390808, 0.01941879, 4.65839081, 0.06085078, -38.81516723, -0.00091443, -46.58390808, -0.01941879, -4.65839081, -0.06085078, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 75.13982683, 0.01828852, 75.13982683, 0.05486556, 52.59787878, -824.01327742, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 18.78495671, 9.148e-05, 56.35487012, 0.00027444, 187.84956707, 0.00091481, -18.78495671, -9.148e-05, -56.35487012, -0.00027444, -187.84956707, -0.00091481, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 75.13982683, 0.01828852, 75.13982683, 0.05486556, 52.59787878, -824.01327742, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 18.78495671, 9.148e-05, 56.35487012, 0.00027444, 187.84956707, 0.00091481, -18.78495671, -9.148e-05, -56.35487012, -0.00027444, -187.84956707, -0.00091481, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 11.25, 9.7, 6.975)
    ops.node(123016, 11.25, 9.7, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 29353371.1610828, 12230571.31711783, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 36.92885262, 0.00087277, 44.3191658, 0.01964063, 4.43191658, 0.06111912, -36.92885262, -0.00087277, -44.3191658, -0.01964063, -4.43191658, -0.06111912, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 39.50423042, 0.00087277, 47.40993595, 0.01964063, 4.7409936, 0.06111912, -39.50423042, -0.00087277, -47.40993595, -0.01964063, -4.7409936, -0.06111912, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 75.1507674, 0.01745545, 75.1507674, 0.05236634, 52.60553718, -823.29518636, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 18.78769185, 9.143e-05, 56.36307555, 0.00027429, 187.87691849, 0.0009143, -18.78769185, -9.143e-05, -56.36307555, -0.00027429, -187.87691849, -0.0009143, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 75.1507674, 0.01745545, 75.1507674, 0.05236634, 52.60553718, -823.29518636, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 18.78769185, 9.143e-05, 56.36307555, 0.00027429, 187.87691849, 0.0009143, -18.78769185, -9.143e-05, -56.36307555, -0.00027429, -187.87691849, -0.0009143, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 15.4, 9.7, 6.975)
    ops.node(123017, 15.4, 9.7, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 30174667.91990622, 12572778.29996092, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 45.83350745, 0.00093065, 54.82030565, 0.01899749, 5.48203056, 0.05389969, -45.83350745, -0.00093065, -54.82030565, -0.01899749, -5.48203056, -0.05389969, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 45.83350745, 0.00093065, 54.82030565, 0.01899749, 5.48203056, 0.05389969, -45.83350745, -0.00093065, -54.82030565, -0.01899749, -5.48203056, -0.05389969, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 75.24264244, 0.01861302, 75.24264244, 0.05583907, 52.66984971, -778.66493849, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 18.81066061, 8.905e-05, 56.43198183, 0.00026715, 188.1066061, 0.0008905, -18.81066061, -8.905e-05, -56.43198183, -0.00026715, -188.1066061, -0.0008905, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 75.24264244, 0.01861302, 75.24264244, 0.05583907, 52.66984971, -778.66493849, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 18.81066061, 8.905e-05, 56.43198183, 0.00026715, 188.1066061, 0.0008905, -18.81066061, -8.905e-05, -56.43198183, -0.00026715, -188.1066061, -0.0008905, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 19.55, 9.7, 7.05)
    ops.node(123018, 19.55, 9.7, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 29573095.02816795, 12322122.92840331, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 28.04591931, 0.00083961, 33.79731288, 0.02058041, 3.37973129, 0.06834648, -28.04591931, -0.00083961, -33.79731288, -0.02058041, -3.37973129, -0.06834648, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 28.04591931, 0.00083961, 33.79731288, 0.02058041, 3.37973129, 0.06834648, -28.04591931, -0.00083961, -33.79731288, -0.02058041, -3.37973129, -0.06834648, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 71.47713036, 0.01679216, 71.47713036, 0.05037648, 50.03399125, -778.60286763, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 17.86928259, 8.631e-05, 53.60784777, 0.00025894, 178.69282591, 0.00086315, -17.86928259, -8.631e-05, -53.60784777, -0.00025894, -178.69282591, -0.00086315, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 71.47713036, 0.01679216, 71.47713036, 0.05037648, 50.03399125, -778.60286763, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 17.86928259, 8.631e-05, 53.60784777, 0.00025894, 178.69282591, 0.00086315, -17.86928259, -8.631e-05, -53.60784777, -0.00025894, -178.69282591, -0.00086315, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 10.15)
    ops.node(124001, 0.0, 0.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 31020624.39152125, 12925260.16313385, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 17.97741283, 0.00074581, 21.74613895, 0.0219934, 2.17461389, 0.08289062, -17.97741283, -0.00074581, -21.74613895, -0.0219934, -2.17461389, -0.08289062, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 17.97741283, 0.00074581, 21.74613895, 0.0219934, 2.17461389, 0.08289062, -17.97741283, -0.00074581, -21.74613895, -0.0219934, -2.17461389, -0.08289062, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 65.31509138, 0.01491617, 65.31509138, 0.04474852, 45.72056396, -921.2233075, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 16.32877284, 7.519e-05, 48.98631853, 0.00022558, 163.28772845, 0.00075193, -16.32877284, -7.519e-05, -48.98631853, -0.00022558, -163.28772845, -0.00075193, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 65.31509138, 0.01491617, 65.31509138, 0.04474852, 45.72056396, -921.2233075, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 16.32877284, 7.519e-05, 48.98631853, 0.00022558, 163.28772845, 0.00075193, -16.32877284, -7.519e-05, -48.98631853, -0.00022558, -163.28772845, -0.00075193, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.15, 0.0, 10.1)
    ops.node(124002, 4.15, 0.0, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.0625, 29592332.04092986, 12330138.35038744, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 30.51246756, 0.00089713, 36.91955382, 0.02166461, 3.69195538, 0.06849233, -30.51246756, -0.00089713, -36.91955382, -0.02166461, -3.69195538, -0.06849233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 30.51246756, 0.00089713, 36.91955382, 0.02166461, 3.69195538, 0.06849233, -30.51246756, -0.00089713, -36.91955382, -0.02166461, -3.69195538, -0.06849233, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 59.56539523, 0.01794255, 59.56539523, 0.05382764, 41.69577666, -627.18309635, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 14.89134881, 7.188e-05, 44.67404642, 0.00021565, 148.91348807, 0.00071883, -14.89134881, -7.188e-05, -44.67404642, -0.00021565, -148.91348807, -0.00071883, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 59.56539523, 0.01794255, 59.56539523, 0.05382764, 41.69577666, -627.18309635, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 14.89134881, 7.188e-05, 44.67404642, 0.00021565, 148.91348807, 0.00071883, -14.89134881, -7.188e-05, -44.67404642, -0.00021565, -148.91348807, -0.00071883, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 15.4, 0.0, 10.1)
    ops.node(124005, 15.4, 0.0, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 28288363.00231304, 11786817.91763043, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 31.36751733, 0.00085332, 38.04408291, 0.02212478, 3.80440829, 0.06735128, -31.36751733, -0.00085332, -38.04408291, -0.02212478, -3.80440829, -0.06735128, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 31.36751733, 0.00085332, 38.04408291, 0.02212478, 3.80440829, 0.06735128, -31.36751733, -0.00085332, -38.04408291, -0.02212478, -3.80440829, -0.06735128, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 59.11269178, 0.01706648, 59.11269178, 0.05119944, 41.37888425, -641.04775346, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 14.77817294, 7.463e-05, 44.33451883, 0.00022388, 147.78172945, 0.00074625, -14.77817294, -7.463e-05, -44.33451883, -0.00022388, -147.78172945, -0.00074625, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 59.11269178, 0.01706648, 59.11269178, 0.05119944, 41.37888425, -641.04775346, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 14.77817294, 7.463e-05, 44.33451883, 0.00022388, 147.78172945, 0.00074625, -14.77817294, -7.463e-05, -44.33451883, -0.00022388, -147.78172945, -0.00074625, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 19.55, 0.0, 10.15)
    ops.node(124006, 19.55, 0.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 29193245.06808516, 12163852.11170215, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 17.71163017, 0.00077054, 21.52599121, 0.02316655, 2.15259912, 0.08278413, -17.71163017, -0.00077054, -21.52599121, -0.02316655, -2.15259912, -0.08278413, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 17.71163017, 0.00077054, 21.52599121, 0.02316655, 2.15259912, 0.08278413, -17.71163017, -0.00077054, -21.52599121, -0.02316655, -2.15259912, -0.08278413, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 62.97126393, 0.01541078, 62.97126393, 0.04623233, 44.07988475, -976.94211893, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 15.74281598, 7.703e-05, 47.22844795, 0.0002311, 157.42815984, 0.00077033, -15.74281598, -7.703e-05, -47.22844795, -0.0002311, -157.42815984, -0.00077033, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 62.97126393, 0.01541078, 62.97126393, 0.04623233, 44.07988475, -976.94211893, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 15.74281598, 7.703e-05, 47.22844795, 0.0002311, 157.42815984, 0.00077033, -15.74281598, -7.703e-05, -47.22844795, -0.0002311, -157.42815984, -0.00077033, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.85, 10.15)
    ops.node(124007, 0.0, 4.85, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 30428713.35648407, 12678630.5652017, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 31.18256366, 0.00084859, 37.66724498, 0.02187016, 3.7667245, 0.06981737, -31.18256366, -0.00084859, -37.66724498, -0.02187016, -3.7667245, -0.06981737, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 31.18256366, 0.00084859, 37.66724498, 0.02187016, 3.7667245, 0.06981737, -31.18256366, -0.00084859, -37.66724498, -0.02187016, -3.7667245, -0.06981737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 62.74569257, 0.01697185, 62.74569257, 0.05091555, 43.9219848, -640.35411627, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 15.68642314, 7.364e-05, 47.05926942, 0.00022092, 156.86423141, 0.0007364, -15.68642314, -7.364e-05, -47.05926942, -0.00022092, -156.86423141, -0.0007364, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 62.74569257, 0.01697185, 62.74569257, 0.05091555, 43.9219848, -640.35411627, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 15.68642314, 7.364e-05, 47.05926942, 0.00022092, 156.86423141, 0.0007364, -15.68642314, -7.364e-05, -47.05926942, -0.00022092, -156.86423141, -0.0007364, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.15, 4.85, 10.1)
    ops.node(124008, 4.15, 4.85, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 29284838.15243782, 12202015.89684909, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 74.90509691, 0.00067194, 90.77052092, 0.01752577, 9.07705209, 0.04834759, -74.90509691, -0.00067194, -90.77052092, -0.01752577, -9.07705209, -0.04834759, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 74.90509691, 0.00067194, 90.77052092, 0.01752577, 9.07705209, 0.04834759, -74.90509691, -0.00067194, -90.77052092, -0.01752577, -9.07705209, -0.04834759, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 100.60794095, 0.01343881, 100.60794095, 0.04031644, 70.42555867, -703.69006608, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 25.15198524, 6.26e-05, 75.45595572, 0.00018779, 251.51985238, 0.00062596, -25.15198524, -6.26e-05, -75.45595572, -0.00018779, -251.51985238, -0.00062596, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 100.60794095, 0.01343881, 100.60794095, 0.04031644, 70.42555867, -703.69006608, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 25.15198524, 6.26e-05, 75.45595572, 0.00018779, 251.51985238, 0.00062596, -25.15198524, -6.26e-05, -75.45595572, -0.00018779, -251.51985238, -0.00062596, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 8.3, 4.85, 10.1)
    ops.node(124009, 8.3, 4.85, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 27840061.29149565, 11600025.53812319, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 72.64391155, 0.00064881, 88.3196015, 0.01875058, 8.83196015, 0.04910046, -72.64391155, -0.00064881, -88.3196015, -0.01875058, -8.83196015, -0.04910046, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 72.64391155, 0.00064881, 88.3196015, 0.01875058, 8.83196015, 0.04910046, -72.64391155, -0.00064881, -88.3196015, -0.01875058, -8.83196015, -0.04910046, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 94.2289823, 0.0129762, 94.2289823, 0.03892859, 65.96028761, -692.76442467, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 23.55724557, 6.167e-05, 70.67173672, 0.00018501, 235.57245574, 0.0006167, -23.55724557, -6.167e-05, -70.67173672, -0.00018501, -235.57245574, -0.0006167, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 94.2289823, 0.0129762, 94.2289823, 0.03892859, 65.96028761, -692.76442467, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 23.55724557, 6.167e-05, 70.67173672, 0.00018501, 235.57245574, 0.0006167, -23.55724557, -6.167e-05, -70.67173672, -0.00018501, -235.57245574, -0.0006167, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 11.25, 4.85, 10.1)
    ops.node(124010, 11.25, 4.85, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 28895389.69429726, 12039745.70595719, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 72.900425, 0.0006563, 88.46288655, 0.01813751, 8.84628866, 0.04924364, -72.900425, -0.0006563, -88.46288655, -0.01813751, -8.84628866, -0.04924364, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 72.900425, 0.0006563, 88.46288655, 0.01813751, 8.84628866, 0.04924364, -72.900425, -0.0006563, -88.46288655, -0.01813751, -8.84628866, -0.04924364, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 97.62693809, 0.01312599, 97.62693809, 0.03937796, 68.33885666, -683.54800014, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 24.40673452, 6.156e-05, 73.22020357, 0.00018468, 244.06734522, 0.0006156, -24.40673452, -6.156e-05, -73.22020357, -0.00018468, -244.06734522, -0.0006156, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 97.62693809, 0.01312599, 97.62693809, 0.03937796, 68.33885666, -683.54800014, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 24.40673452, 6.156e-05, 73.22020357, 0.00018468, 244.06734522, 0.0006156, -24.40673452, -6.156e-05, -73.22020357, -0.00018468, -244.06734522, -0.0006156, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 15.4, 4.85, 10.1)
    ops.node(124011, 15.4, 4.85, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 28198308.26073333, 11749295.10863889, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 74.59225879, 0.00066603, 90.57384886, 0.01755437, 9.05738489, 0.04757707, -74.59225879, -0.00066603, -90.57384886, -0.01755437, -9.05738489, -0.04757707, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 74.59225879, 0.00066603, 90.57384886, 0.01755437, 9.05738489, 0.04757707, -74.59225879, -0.00066603, -90.57384886, -0.01755437, -9.05738489, -0.04757707, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 96.57978195, 0.01332052, 96.57978195, 0.03996156, 67.60584736, -700.86981065, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 24.14494549, 6.241e-05, 72.43483646, 0.00018722, 241.44945487, 0.00062405, -24.14494549, -6.241e-05, -72.43483646, -0.00018722, -241.44945487, -0.00062405, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 96.57978195, 0.01332052, 96.57978195, 0.03996156, 67.60584736, -700.86981065, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 24.14494549, 6.241e-05, 72.43483646, 0.00018722, 241.44945487, 0.00062405, -24.14494549, -6.241e-05, -72.43483646, -0.00018722, -241.44945487, -0.00062405, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 19.55, 4.85, 10.15)
    ops.node(124012, 19.55, 4.85, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 31794396.62053964, 13247665.25855818, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 31.25567648, 0.00081584, 37.62330139, 0.02154613, 3.76233014, 0.07075664, -31.25567648, -0.00081584, -37.62330139, -0.02154613, -3.76233014, -0.07075664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 31.25567648, 0.00081584, 37.62330139, 0.02154613, 3.76233014, 0.07075664, -31.25567648, -0.00081584, -37.62330139, -0.02154613, -3.76233014, -0.07075664, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 64.70505, 0.01631674, 64.70505, 0.04895022, 45.293535, -632.57450032, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 16.1762625, 7.268e-05, 48.5287875, 0.00021803, 161.762625, 0.00072678, -16.1762625, -7.268e-05, -48.5287875, -0.00021803, -161.762625, -0.00072678, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 64.70505, 0.01631674, 64.70505, 0.04895022, 45.293535, -632.57450032, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 16.1762625, 7.268e-05, 48.5287875, 0.00021803, 161.762625, 0.00072678, -16.1762625, -7.268e-05, -48.5287875, -0.00021803, -161.762625, -0.00072678, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.7, 10.15)
    ops.node(124013, 0.0, 9.7, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 31213971.14753272, 13005821.31147197, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 17.97901127, 0.00077092, 21.73599812, 0.02190636, 2.17359981, 0.08292188, -17.97901127, -0.00077092, -21.73599812, -0.02190636, -2.17359981, -0.08292188, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 17.97901127, 0.00077092, 21.73599812, 0.02190636, 2.17359981, 0.08292188, -17.97901127, -0.00077092, -21.73599812, -0.02190636, -2.17359981, -0.08292188, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 65.57260522, 0.01541844, 65.57260522, 0.04625531, 45.90082366, -915.51774684, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 16.39315131, 7.502e-05, 49.17945392, 0.00022507, 163.93151306, 0.00075022, -16.39315131, -7.502e-05, -49.17945392, -0.00022507, -163.93151306, -0.00075022, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 65.57260522, 0.01541844, 65.57260522, 0.04625531, 45.90082366, -915.51774684, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 16.39315131, 7.502e-05, 49.17945392, 0.00022507, 163.93151306, 0.00075022, -16.39315131, -7.502e-05, -49.17945392, -0.00022507, -163.93151306, -0.00075022, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.15, 9.7, 10.1)
    ops.node(124014, 4.15, 9.7, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 30248916.66944319, 12603715.27893466, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 31.18147961, 0.00085042, 37.67570132, 0.02163444, 3.76757013, 0.06917659, -31.18147961, -0.00085042, -37.67570132, -0.02163444, -3.76757013, -0.06917659, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 31.18147961, 0.00085042, 37.67570132, 0.02163444, 3.76757013, 0.06917659, -31.18147961, -0.00085042, -37.67570132, -0.02163444, -3.76757013, -0.06917659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 61.05547233, 0.01700832, 61.05547233, 0.05102495, 42.73883063, -628.04700214, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 15.26386808, 7.208e-05, 45.79160425, 0.00021625, 152.63868082, 0.00072082, -15.26386808, -7.208e-05, -45.79160425, -0.00021625, -152.63868082, -0.00072082, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 61.05547233, 0.01700832, 61.05547233, 0.05102495, 42.73883063, -628.04700214, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 15.26386808, 7.208e-05, 45.79160425, 0.00021625, 152.63868082, 0.00072082, -15.26386808, -7.208e-05, -45.79160425, -0.00021625, -152.63868082, -0.00072082, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 8.3, 9.7, 10.1)
    ops.node(124015, 8.3, 9.7, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 29723133.21736702, 12384638.84056959, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 20.937552, 0.00079852, 25.35279818, 0.0222057, 2.53527982, 0.07804168, -20.937552, -0.00079852, -25.35279818, -0.0222057, -2.53527982, -0.07804168, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 20.937552, 0.00079852, 25.35279818, 0.0222057, 2.53527982, 0.07804168, -20.937552, -0.00079852, -25.35279818, -0.0222057, -2.53527982, -0.07804168, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 66.1417145, 0.01597045, 66.1417145, 0.04791136, 46.29920015, -799.05159012, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 16.53542863, 7.947e-05, 49.60628588, 0.00023841, 165.35428625, 0.00079469, -16.53542863, -7.947e-05, -49.60628588, -0.00023841, -165.35428625, -0.00079469, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 66.1417145, 0.01597045, 66.1417145, 0.04791136, 46.29920015, -799.05159012, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 16.53542863, 7.947e-05, 49.60628588, 0.00023841, 165.35428625, 0.00079469, -16.53542863, -7.947e-05, -49.60628588, -0.00023841, -165.35428625, -0.00079469, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 11.25, 9.7, 10.1)
    ops.node(124016, 11.25, 9.7, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 30140039.15801616, 12558349.6491734, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 21.31390534, 0.00079044, 25.78411788, 0.02213485, 2.57841179, 0.07843236, -21.31390534, -0.00079044, -25.78411788, -0.02213485, -2.57841179, -0.07843236, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 21.31390534, 0.00079044, 25.78411788, 0.02213485, 2.57841179, 0.07843236, -21.31390534, -0.00079044, -25.78411788, -0.02213485, -2.57841179, -0.07843236, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 67.3503133, 0.01580883, 67.3503133, 0.04742648, 47.14521931, -814.98265881, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 16.83757833, 7.98e-05, 50.51273498, 0.0002394, 168.37578326, 0.00079801, -16.83757833, -7.98e-05, -50.51273498, -0.0002394, -168.37578326, -0.00079801, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 67.3503133, 0.01580883, 67.3503133, 0.04742648, 47.14521931, -814.98265881, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 16.83757833, 7.98e-05, 50.51273498, 0.0002394, 168.37578326, 0.00079801, -16.83757833, -7.98e-05, -50.51273498, -0.0002394, -168.37578326, -0.00079801, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 15.4, 9.7, 10.1)
    ops.node(124017, 15.4, 9.7, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 28658988.31722701, 11941245.13217792, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 31.18802593, 0.00085113, 37.80326313, 0.02216106, 3.78032631, 0.06786913, -31.18802593, -0.00085113, -37.80326313, -0.02216106, -3.78032631, -0.06786913, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 31.18802593, 0.00085113, 37.80326313, 0.02216106, 3.78032631, 0.06786913, -31.18802593, -0.00085113, -37.80326313, -0.02216106, -3.78032631, -0.06786913, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 59.88355793, 0.01702256, 59.88355793, 0.05106768, 41.91849055, -640.88675599, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 14.97088948, 7.462e-05, 44.91266845, 0.00022386, 149.70889482, 0.00074621, -14.97088948, -7.462e-05, -44.91266845, -0.00022386, -149.70889482, -0.00074621, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 59.88355793, 0.01702256, 59.88355793, 0.05106768, 41.91849055, -640.88675599, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 14.97088948, 7.462e-05, 44.91266845, 0.00022386, 149.70889482, 0.00074621, -14.97088948, -7.462e-05, -44.91266845, -0.00022386, -149.70889482, -0.00074621, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 19.55, 9.7, 10.15)
    ops.node(124018, 19.55, 9.7, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 29015982.99376784, 12089992.91406994, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 17.80692254, 0.00076127, 21.65061375, 0.02262478, 2.16506137, 0.0821008, -17.80692254, -0.00076127, -21.65061375, -0.02262478, -2.16506137, -0.0821008, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 17.80692254, 0.00076127, 21.65061375, 0.02262478, 2.16506137, 0.0821008, -17.80692254, -0.00076127, -21.65061375, -0.02262478, -2.16506137, -0.0821008, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 61.16564178, 0.01522547, 61.16564178, 0.04567642, 42.81594924, -899.5823882, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 15.29141044, 7.528e-05, 45.87423133, 0.00022584, 152.91410444, 0.00075281, -15.29141044, -7.528e-05, -45.87423133, -0.00022584, -152.91410444, -0.00075281, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 61.16564178, 0.01522547, 61.16564178, 0.04567642, 42.81594924, -899.5823882, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 15.29141044, 7.528e-05, 45.87423133, 0.00022584, 152.91410444, 0.00075281, -15.29141044, -7.528e-05, -45.87423133, -0.00022584, -152.91410444, -0.00075281, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.3, 0.0, 0.0)
    ops.node(124019, 8.3, 0.0, 1.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 170003, 124019, 0.1225, 29547375.95342891, 12311406.64726205, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 173.52630189, 0.00059782, 207.12585502, 0.03198647, 20.7125855, 0.07331756, -173.52630189, -0.00059782, -207.12585502, -0.03198647, -20.7125855, -0.07331756, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 173.52630189, 0.00059782, 207.12585502, 0.03198647, 20.7125855, 0.07331756, -173.52630189, -0.00059782, -207.12585502, -0.03198647, -20.7125855, -0.07331756, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 188.41246338, 0.0119564, 188.41246338, 0.03586919, 131.88872437, -3293.3132245, 0.05, 2, 0, 70003, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 47.10311584, 6.934e-05, 141.30934753, 0.00020801, 471.03115845, 0.00069336, -47.10311584, -6.934e-05, -141.30934753, -0.00020801, -471.03115845, -0.00069336, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 188.41246338, 0.0119564, 188.41246338, 0.03586919, 131.88872437, -3293.3132245, 0.05, 2, 0, 70003, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 47.10311584, 6.934e-05, 141.30934753, 0.00020801, 471.03115845, 0.00069336, -47.10311584, -6.934e-05, -141.30934753, -0.00020801, -471.03115845, -0.00069336, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 8.3, 0.0, 2.1)
    ops.node(121003, 8.3, 0.0, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 121003, 0.1225, 29170535.41267037, 12154389.75527932, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 137.60509634, 0.00059885, 164.5733553, 0.03040163, 16.45733553, 0.07287579, -137.60509634, -0.00059885, -164.5733553, -0.03040163, -16.45733553, -0.07287579, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 130.55660763, 0.00059885, 156.14348267, 0.03040163, 15.61434827, 0.07287579, -130.55660763, -0.00059885, -156.14348267, -0.03040163, -15.61434827, -0.07287579, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 183.33941725, 0.01197692, 183.33941725, 0.03593075, 128.33759207, -3221.68407312, 0.05, 2, 0, 74019, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 45.83485431, 6.834e-05, 137.50456294, 0.00020502, 458.34854312, 0.00068341, -45.83485431, -6.834e-05, -137.50456294, -0.00020502, -458.34854312, -0.00068341, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 183.33941725, 0.01197692, 183.33941725, 0.03593075, 128.33759207, -3221.68407312, 0.05, 2, 0, 74019, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 45.83485431, 6.834e-05, 137.50456294, 0.00020502, 458.34854312, 0.00068341, -45.83485431, -6.834e-05, -137.50456294, -0.00020502, -458.34854312, -0.00068341, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 11.25, 0.0, 0.0)
    ops.node(124020, 11.25, 0.0, 1.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 170004, 124020, 0.1225, 28037298.35132778, 11682207.64638657, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 172.04001097, 0.00062037, 205.36067778, 0.03084145, 20.53606778, 0.06752593, -172.04001097, -0.00062037, -205.36067778, -0.03084145, -20.53606778, -0.06752593, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 172.04001097, 0.00062037, 205.36067778, 0.03084145, 20.53606778, 0.06752593, -172.04001097, -0.00062037, -205.36067778, -0.03084145, -20.53606778, -0.06752593, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 180.71890698, 0.01240746, 180.71890698, 0.03722239, 126.50323489, -3281.20153791, 0.05, 2, 0, 70004, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 45.17972675, 7.009e-05, 135.53918024, 0.00021026, 451.79726746, 0.00070087, -45.17972675, -7.009e-05, -135.53918024, -0.00021026, -451.79726746, -0.00070087, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 180.71890698, 0.01240746, 180.71890698, 0.03722239, 126.50323489, -3281.20153791, 0.05, 2, 0, 70004, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 45.17972675, 7.009e-05, 135.53918024, 0.00021026, 451.79726746, 0.00070087, -45.17972675, -7.009e-05, -135.53918024, -0.00021026, -451.79726746, -0.00070087, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 11.25, 0.0, 2.1)
    ops.node(121004, 11.25, 0.0, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 121004, 0.1225, 31434178.94242973, 13097574.55934572, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 141.17341097, 0.00058096, 168.43331082, 0.03091337, 16.84333108, 0.07936231, -141.17341097, -0.00058096, -168.43331082, -0.03091337, -16.84333108, -0.07936231, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 133.70168174, 0.00058096, 159.51882698, 0.03091337, 15.9518827, 0.07936231, -133.70168174, -0.00058096, -159.51882698, -0.03091337, -15.9518827, -0.07936231, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 194.39967211, 0.01161915, 194.39967211, 0.03485746, 136.07977048, -3218.28334821, 0.05, 2, 0, 74020, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 48.59991803, 6.725e-05, 145.79975408, 0.00020174, 485.99918028, 0.00067245, -48.59991803, -6.725e-05, -145.79975408, -0.00020174, -485.99918028, -0.00067245, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 194.39967211, 0.01161915, 194.39967211, 0.03485746, 136.07977048, -3218.28334821, 0.05, 2, 0, 74020, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 48.59991803, 6.725e-05, 145.79975408, 0.00020174, 485.99918028, 0.00067245, -48.59991803, -6.725e-05, -145.79975408, -0.00020174, -485.99918028, -0.00067245, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.3, 0.0, 3.9)
    ops.node(124021, 8.3, 0.0, 5.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 171003, 124021, 0.1225, 29363664.02316358, 12234860.00965149, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 103.9158644, 0.0005421, 124.76138821, 0.02095432, 12.47613882, 0.05339425, -103.9158644, -0.0005421, -124.76138821, -0.02095432, -12.47613882, -0.05339425, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 96.95303753, 0.0005421, 116.40181817, 0.02095432, 11.64018182, 0.05339425, -96.95303753, -0.0005421, -116.40181817, -0.02095432, -11.64018182, -0.05339425, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 176.21397054, 0.01084191, 176.21397054, 0.03252573, 123.34977938, -2594.64995058, 0.05, 2, 0, 71003, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 44.05349264, 5.467e-05, 132.16047791, 0.00016401, 440.53492635, 0.00054671, -44.05349264, -5.467e-05, -132.16047791, -0.00016401, -440.53492635, -0.00054671, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 176.21397054, 0.01084191, 176.21397054, 0.03252573, 123.34977938, -2594.64995058, 0.05, 2, 0, 71003, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 44.05349264, 5.467e-05, 132.16047791, 0.00016401, 440.53492635, 0.00054671, -44.05349264, -5.467e-05, -132.16047791, -0.00016401, -440.53492635, -0.00054671, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 8.3, 0.0, 5.5)
    ops.node(122003, 8.3, 0.0, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 122003, 0.1225, 29502791.1085671, 12292829.62856962, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 99.82126495, 0.00053707, 120.03038285, 0.01794313, 12.00303829, 0.04810126, -99.82126495, -0.00053707, -120.03038285, -0.01794313, -12.00303829, -0.04810126, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 92.64412457, 0.00053707, 111.40020863, 0.01794313, 11.14002086, 0.04810126, -92.64412457, -0.00053707, -111.40020863, -0.01794313, -11.14002086, -0.04810126, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 165.29018723, 0.01074137, 165.29018723, 0.0322241, 115.70313106, -2174.72977303, 0.05, 2, 0, 74021, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 41.32254681, 5.104e-05, 123.96764042, 0.00015312, 413.22546807, 0.0005104, -41.32254681, -5.104e-05, -123.96764042, -0.00015312, -413.22546807, -0.0005104, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 165.29018723, 0.01074137, 165.29018723, 0.0322241, 115.70313106, -2174.72977303, 0.05, 2, 0, 74021, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 41.32254681, 5.104e-05, 123.96764042, 0.00015312, 413.22546807, 0.0005104, -41.32254681, -5.104e-05, -123.96764042, -0.00015312, -413.22546807, -0.0005104, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 11.25, 0.0, 3.9)
    ops.node(124022, 11.25, 0.0, 5.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 171004, 124022, 0.1225, 29091600.08226525, 12121500.03427719, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 103.67395468, 0.00054506, 124.50352711, 0.02089108, 12.45035271, 0.0528581, -103.67395468, -0.00054506, -124.50352711, -0.02089108, -12.45035271, -0.0528581, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 96.77248415, 0.00054506, 116.21545296, 0.02089108, 11.6215453, 0.0528581, -96.77248415, -0.00054506, -116.21545296, -0.02089108, -11.6215453, -0.0528581, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 174.08378291, 0.01090128, 174.08378291, 0.03270384, 121.85864803, -2568.63430553, 0.05, 2, 0, 71004, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 43.52094573, 5.452e-05, 130.56283718, 0.00016355, 435.20945727, 0.00054515, -43.52094573, -5.452e-05, -130.56283718, -0.00016355, -435.20945727, -0.00054515, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 174.08378291, 0.01090128, 174.08378291, 0.03270384, 121.85864803, -2568.63430553, 0.05, 2, 0, 71004, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 43.52094573, 5.452e-05, 130.56283718, 0.00016355, 435.20945727, 0.00054515, -43.52094573, -5.452e-05, -130.56283718, -0.00016355, -435.20945727, -0.00054515, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 11.25, 0.0, 5.5)
    ops.node(122004, 11.25, 0.0, 6.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 122004, 0.1225, 28929448.73600231, 12053936.9733343, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 97.78200607, 0.00054246, 117.65615965, 0.01818382, 11.76561596, 0.04752085, -97.78200607, -0.00054246, -117.65615965, -0.01818382, -11.76561596, -0.04752085, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 91.07565803, 0.00054246, 109.58674906, 0.01818382, 10.95867491, 0.04752085, -91.07565803, -0.00054246, -109.58674906, -0.01818382, -10.95867491, -0.04752085, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 162.20569316, 0.01084927, 162.20569316, 0.03254781, 113.54398521, -2178.65377858, 0.05, 2, 0, 74022, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 40.55142329, 5.108e-05, 121.65426987, 0.00015324, 405.5142329, 0.0005108, -40.55142329, -5.108e-05, -121.65426987, -0.00015324, -405.5142329, -0.0005108, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 162.20569316, 0.01084927, 162.20569316, 0.03254781, 113.54398521, -2178.65377858, 0.05, 2, 0, 74022, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 40.55142329, 5.108e-05, 121.65426987, 0.00015324, 405.5142329, 0.0005108, -40.55142329, -5.108e-05, -121.65426987, -0.00015324, -405.5142329, -0.0005108, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.3, 0.0, 6.975)
    ops.node(124023, 8.3, 0.0, 8.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 172003, 124023, 0.0625, 29240683.46867206, 12183618.11194669, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 46.70101329, 0.00067165, 55.84279306, 0.01899147, 5.58427931, 0.05094524, -46.70101329, -0.00067165, -55.84279306, -0.01899147, -5.58427931, -0.05094524, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 46.70101329, 0.00067165, 55.84279306, 0.01899147, 5.58427931, 0.05094524, -46.70101329, -0.00067165, -55.84279306, -0.01899147, -5.58427931, -0.05094524, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 75.12971127, 0.01343297, 75.12971127, 0.0402989, 52.59079789, -1578.90920445, 0.05, 2, 0, 72003, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 18.78242782, 4.588e-05, 56.34728345, 0.00013764, 187.82427818, 0.00045878, -18.78242782, -4.588e-05, -56.34728345, -0.00013764, -187.82427818, -0.00045878, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 75.12971127, 0.01343297, 75.12971127, 0.0402989, 52.59079789, -1578.90920445, 0.05, 2, 0, 72003, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 18.78242782, 4.588e-05, 56.34728345, 0.00013764, 187.82427818, 0.00045878, -18.78242782, -4.588e-05, -56.34728345, -0.00013764, -187.82427818, -0.00045878, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 8.3, 0.0, 8.55)
    ops.node(123003, 8.3, 0.0, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 123003, 0.0625, 30357664.43954884, 12649026.84981202, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 42.56231165, 0.00065581, 51.00841278, 0.01993727, 5.10084128, 0.0575697, -42.56231165, -0.00065581, -51.00841278, -0.01993727, -5.10084128, -0.0575697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 42.56231165, 0.00065581, 51.00841278, 0.01993727, 5.10084128, 0.0575697, -42.56231165, -0.00065581, -51.00841278, -0.01993727, -5.10084128, -0.0575697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 72.77508786, 0.01311618, 72.77508786, 0.03934854, 50.9425615, -1445.88524021, 0.05, 2, 0, 74023, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 18.19377196, 4.281e-05, 54.58131589, 0.00012842, 181.93771964, 0.00042805, -18.19377196, -4.281e-05, -54.58131589, -0.00012842, -181.93771964, -0.00042805, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 72.77508786, 0.01311618, 72.77508786, 0.03934854, 50.9425615, -1445.88524021, 0.05, 2, 0, 74023, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 18.19377196, 4.281e-05, 54.58131589, 0.00012842, 181.93771964, 0.00042805, -18.19377196, -4.281e-05, -54.58131589, -0.00012842, -181.93771964, -0.00042805, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 11.25, 0.0, 6.975)
    ops.node(124024, 11.25, 0.0, 8.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 172004, 124024, 0.0625, 30059672.92295786, 12524863.71789911, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 46.7235122, 0.00068375, 55.83690965, 0.01898334, 5.58369096, 0.05265955, -46.7235122, -0.00068375, -55.83690965, -0.01898334, -5.58369096, -0.05265955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 46.7235122, 0.00068375, 55.83690965, 0.01898334, 5.58369096, 0.05265955, -46.7235122, -0.00068375, -55.83690965, -0.01898334, -5.58369096, -0.05265955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 76.18045281, 0.01367505, 76.18045281, 0.04102514, 53.32631697, -1583.54575386, 0.05, 2, 0, 72004, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 19.0451132, 4.525e-05, 57.13533961, 0.00013576, 190.45113202, 0.00045253, -19.0451132, -4.525e-05, -57.13533961, -0.00013576, -190.45113202, -0.00045253, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 76.18045281, 0.01367505, 76.18045281, 0.04102514, 53.32631697, -1583.54575386, 0.05, 2, 0, 72004, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 19.0451132, 4.525e-05, 57.13533961, 0.00013576, 190.45113202, 0.00045253, -19.0451132, -4.525e-05, -57.13533961, -0.00013576, -190.45113202, -0.00045253, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 11.25, 0.0, 8.55)
    ops.node(123004, 11.25, 0.0, 9.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 123004, 0.0625, 29223038.73213694, 12176266.13839039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 42.24921609, 0.00066027, 50.70015838, 0.01976593, 5.07001584, 0.05525443, -42.24921609, -0.00066027, -50.70015838, -0.01976593, -5.07001584, -0.05525443, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 42.24921609, 0.00066027, 50.70015838, 0.01976593, 5.07001584, 0.05525443, -42.24921609, -0.00066027, -50.70015838, -0.01976593, -5.07001584, -0.05525443, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 70.15728782, 0.01320548, 70.15728782, 0.03961645, 49.11010148, -1444.47047117, 0.05, 2, 0, 74024, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 17.53932196, 4.287e-05, 52.61796587, 0.0001286, 175.39321956, 0.00042868, -17.53932196, -4.287e-05, -52.61796587, -0.0001286, -175.39321956, -0.00042868, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 70.15728782, 0.01320548, 70.15728782, 0.03961645, 49.11010148, -1444.47047117, 0.05, 2, 0, 74024, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 17.53932196, 4.287e-05, 52.61796587, 0.0001286, 175.39321956, 0.00042868, -17.53932196, -4.287e-05, -52.61796587, -0.0001286, -175.39321956, -0.00042868, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.3, 0.0, 10.1)
    ops.node(124025, 8.3, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4061, 173003, 124025, 0.0625, 27588891.6174261, 11495371.50726088, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24061, 31.66307032, 0.00063015, 38.41600225, 0.02295603, 3.84160022, 0.06633994, -31.66307032, -0.00063015, -38.41600225, -0.02295603, -3.84160022, -0.06633994, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14061, 31.66307032, 0.00063015, 38.41600225, 0.02295603, 3.84160022, 0.06633994, -31.66307032, -0.00063015, -38.41600225, -0.02295603, -3.84160022, -0.06633994, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24061, 4061, 0.0, 61.51321065, 0.01260293, 61.51321065, 0.0378088, 43.05924746, -1318.29751821, 0.05, 2, 0, 73003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44061, 15.37830266, 3.981e-05, 46.13490799, 0.00011944, 153.78302663, 0.00039812, -15.37830266, -3.981e-05, -46.13490799, -0.00011944, -153.78302663, -0.00039812, 0.4, 0.3, 0.003, 0.0, 0.0, 24061, 2)
    ops.limitCurve('ThreePoint', 14061, 4061, 0.0, 61.51321065, 0.01260293, 61.51321065, 0.0378088, 43.05924746, -1318.29751821, 0.05, 2, 0, 73003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34061, 15.37830266, 3.981e-05, 46.13490799, 0.00011944, 153.78302663, 0.00039812, -15.37830266, -3.981e-05, -46.13490799, -0.00011944, -153.78302663, -0.00039812, 0.4, 0.3, 0.003, 0.0, 0.0, 14061, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4061, 99999, 'P', 44061, 'Vy', 34061, 'Vz', 24061, 'My', 14061, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4061, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4061, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 8.3, 0.0, 11.625)
    ops.node(124003, 8.3, 0.0, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 174025, 124003, 0.0625, 30239701.23109622, 12599875.51295676, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 27.44986777, 0.00058278, 33.25563316, 0.02368756, 3.32556332, 0.07512854, -27.44986777, -0.00058278, -33.25563316, -0.02368756, -3.32556332, -0.07512854, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 27.44986777, 0.00058278, 33.25563316, 0.02368756, 3.32556332, 0.07512854, -27.44986777, -0.00058278, -33.25563316, -0.02368756, -3.32556332, -0.07512854, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 60.69469341, 0.01165555, 60.69469341, 0.03496666, 42.48628539, -1390.2160041, 0.05, 2, 0, 74025, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 15.17367335, 3.584e-05, 45.52102006, 0.00010752, 151.73673352, 0.00035839, -15.17367335, -3.584e-05, -45.52102006, -0.00010752, -151.73673352, -0.00035839, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 60.69469341, 0.01165555, 60.69469341, 0.03496666, 42.48628539, -1390.2160041, 0.05, 2, 0, 74025, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 15.17367335, 3.584e-05, 45.52102006, 0.00010752, 151.73673352, 0.00035839, -15.17367335, -3.584e-05, -45.52102006, -0.00010752, -151.73673352, -0.00035839, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 11.25, 0.0, 10.1)
    ops.node(124026, 11.25, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 173004, 124026, 0.0625, 28955036.54104822, 12064598.55877009, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 31.56206862, 0.00062823, 38.21491121, 0.02291772, 3.82149112, 0.06822167, -31.56206862, -0.00062823, -38.21491121, -0.02291772, -3.82149112, -0.06822167, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 31.56206862, 0.00062823, 38.21491121, 0.02291772, 3.82149112, 0.06822167, -31.56206862, -0.00062823, -38.21491121, -0.02291772, -3.82149112, -0.06822167, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 64.01192781, 0.01256455, 64.01192781, 0.03769366, 44.80834947, -1318.00258126, 0.05, 2, 0, 73004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 16.00298195, 3.947e-05, 48.00894586, 0.00011842, 160.02981953, 0.00039475, -16.00298195, -3.947e-05, -48.00894586, -0.00011842, -160.02981953, -0.00039475, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 64.01192781, 0.01256455, 64.01192781, 0.03769366, 44.80834947, -1318.00258126, 0.05, 2, 0, 73004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 16.00298195, 3.947e-05, 48.00894586, 0.00011842, 160.02981953, 0.00039475, -16.00298195, -3.947e-05, -48.00894586, -0.00011842, -160.02981953, -0.00039475, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 11.25, 0.0, 11.625)
    ops.node(124004, 11.25, 0.0, 12.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174026, 124004, 0.0625, 29679217.27517597, 12366340.53132332, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 27.63184984, 0.00058492, 33.52252952, 0.02388659, 3.35225295, 0.0749296, -27.63184984, -0.00058492, -33.52252952, -0.02388659, -3.35225295, -0.0749296, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 27.63184984, 0.00058492, 33.52252952, 0.02388659, 3.35225295, 0.0749296, -27.63184984, -0.00058492, -33.52252952, -0.02388659, -3.35225295, -0.0749296, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 59.41336223, 0.01169848, 59.41336223, 0.03509545, 41.58935356, -1344.8250921, 0.05, 2, 0, 74026, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 14.85334056, 3.575e-05, 44.56002167, 0.00010724, 148.53340557, 0.00035745, -14.85334056, -3.575e-05, -44.56002167, -0.00010724, -148.53340557, -0.00035745, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 59.41336223, 0.01169848, 59.41336223, 0.03509545, 41.58935356, -1344.8250921, 0.05, 2, 0, 74026, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 14.85334056, 3.575e-05, 44.56002167, 0.00010724, 148.53340557, 0.00035745, -14.85334056, -3.575e-05, -44.56002167, -0.00010724, -148.53340557, -0.00035745, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4064, '-orient', 0, 0, 1, 0, 1, 0)
