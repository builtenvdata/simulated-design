import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.16, 28171992.66113896, 11738330.27547457, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 246.61852401, 0.00121076, 296.85071214, 0.0367891, 29.68507121, 0.1062612, -246.61852401, -0.00121076, -296.85071214, -0.0367891, -29.68507121, -0.1062612, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 265.48990934, 0.00121076, 319.56589218, 0.0367891, 31.95658922, 0.1062612, -265.48990934, -0.00121076, -319.56589218, -0.0367891, -31.95658922, -0.1062612, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.5, 0.0, 0.0)
    ops.node(121002, 4.5, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.2025, 30146450.7232196, 12561021.13467483, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 420.24915279, 0.00106537, 502.93542101, 0.0401903, 50.2935421, 0.11306619, -420.24915279, -0.00106537, -502.93542101, -0.0401903, -50.2935421, -0.11306619, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 444.79289366, 0.00106537, 532.30827414, 0.0401903, 53.23082741, 0.11306619, -444.79289366, -0.00106537, -532.30827414, -0.0401903, -53.23082741, -0.11306619, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.5, 0.0, 0.0)
    ops.node(121005, 16.5, 0.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.2025, 28459127.10995806, 11857969.62914919, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 416.64884647, 0.00111106, 499.22529616, 0.03909814, 49.92252962, 0.10473699, -416.64884647, -0.00111106, -499.22529616, -0.03909814, -49.92252962, -0.10473699, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 440.99115321, 0.00111106, 528.39205227, 0.03909814, 52.83920523, 0.10473699, -440.99115321, -0.00111106, -528.39205227, -0.03909814, -52.83920523, -0.10473699, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 21.0, 0.0, 0.0)
    ops.node(121006, 21.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.16, 28128671.11286058, 11720279.63035857, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 247.58845675, 0.00117122, 298.02608797, 0.03657966, 29.8026088, 0.10587888, -247.58845675, -0.00117122, -298.02608797, -0.03657966, -29.8026088, -0.10587888, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 267.32742076, 0.00117122, 321.78618689, 0.03657966, 32.17861869, 0.10587888, -267.32742076, -0.00117122, -321.78618689, -0.03657966, -32.17861869, -0.10587888, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.5, 0.0)
    ops.node(121007, 0.0, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.2025, 28014913.05918365, 11672880.44132652, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 365.33260729, 0.00109647, 437.73072536, 0.03771406, 43.77307254, 0.10113257, -365.33260729, -0.00109647, -437.73072536, -0.03771406, -43.77307254, -0.10113257, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 413.82593198, 0.00109647, 495.83399281, 0.03771406, 49.58339928, 0.10113257, -413.82593198, -0.00109647, -495.83399281, -0.03771406, -49.58339928, -0.10113257, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.5, 4.5, 0.0)
    ops.node(121008, 4.5, 4.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.3025, 28849467.95308392, 12020611.6471183, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 799.65859688, 0.00096947, 959.54066608, 0.04963842, 95.95406661, 0.1379857, -799.65859688, -0.00096947, -959.54066608, -0.04963842, -95.95406661, -0.1379857, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 832.00979554, 0.00096947, 998.36009581, 0.04963842, 99.83600958, 0.1379857, -832.00979554, -0.00096947, -998.36009581, -0.04963842, -99.83600958, -0.1379857, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.0, 4.5, 0.0)
    ops.node(121009, 9.0, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.25, 29357638.77075427, 12232349.48781428, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 564.7828751, 0.00099786, 676.87594011, 0.03833218, 67.68759401, 0.10303776, -564.7828751, -0.00099786, -676.87594011, -0.03833218, -67.68759401, -0.10303776, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 564.7828751, 0.00099786, 676.87594011, 0.03833218, 67.68759401, 0.10303776, -564.7828751, -0.00099786, -676.87594011, -0.03833218, -67.68759401, -0.10303776, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.0, 4.5, 0.0)
    ops.node(121010, 12.0, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.25, 28988809.38776533, 12078670.57823556, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 562.38418913, 0.00101126, 674.1819774, 0.03875189, 67.41819774, 0.10202694, -562.38418913, -0.00101126, -674.1819774, -0.03875189, -67.41819774, -0.10202694, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 562.38418913, 0.00101126, 674.1819774, 0.03875189, 67.41819774, 0.10202694, -562.38418913, -0.00101126, -674.1819774, -0.03875189, -67.41819774, -0.10202694, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 16.5, 4.5, 0.0)
    ops.node(121011, 16.5, 4.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.3025, 28067695.21309378, 11694873.00545574, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 793.44255536, 0.0009659, 952.41467601, 0.04884865, 95.2414676, 0.13286197, -793.44255536, -0.0009659, -952.41467601, -0.04884865, -95.2414676, -0.13286197, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 826.05703475, 0.0009659, 991.56370906, 0.04884865, 99.15637091, 0.13286197, -826.05703475, -0.0009659, -991.56370906, -0.04884865, -99.15637091, -0.13286197, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 21.0, 4.5, 0.0)
    ops.node(121012, 21.0, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.2025, 30379169.23356236, 12657987.18065098, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 372.67678879, 0.00108443, 445.85308093, 0.03953914, 44.58530809, 0.11320955, -372.67678879, -0.00108443, -445.85308093, -0.03953914, -44.58530809, -0.11320955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 420.41120867, 0.00108443, 502.96030845, 0.03953914, 50.29603085, 0.11320955, -420.41120867, -0.00108443, -502.96030845, -0.03953914, -50.29603085, -0.11320955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.2025, 28963055.11222184, 12067939.63009243, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 419.43359986, 0.00108571, 502.44137802, 0.03961659, 50.2441378, 0.10744406, -419.43359986, -0.00108571, -502.44137802, -0.03961659, -50.2441378, -0.10744406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 444.28764219, 0.00108571, 532.21414606, 0.03961659, 53.22141461, 0.10744406, -444.28764219, -0.00108571, -532.21414606, -0.03961659, -53.22141461, -0.10744406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.5, 9.0, 0.0)
    ops.node(121014, 4.5, 9.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.3025, 29702617.92737174, 12376090.80307156, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 785.98196537, 0.00091937, 942.45075641, 0.05071671, 94.24507564, 0.14353138, -785.98196537, -0.00091937, -942.45075641, -0.05071671, -94.24507564, -0.14353138, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 817.80521173, 0.00091937, 980.60919251, 0.05071671, 98.06091925, 0.14353138, -817.80521173, -0.00091937, -980.60919251, -0.05071671, -98.06091925, -0.14353138, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 9.0, 0.0)
    ops.node(121015, 9.0, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.25, 28999093.56691035, 12082955.65287931, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 559.95770603, 0.00101099, 671.23531389, 0.03856966, 67.12353139, 0.10179126, -559.95770603, -0.00101099, -671.23531389, -0.03856966, -67.12353139, -0.10179126, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 559.95770603, 0.00101099, 671.23531389, 0.03856966, 67.12353139, 0.10179126, -559.95770603, -0.00101099, -671.23531389, -0.03856966, -67.12353139, -0.10179126, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.0, 9.0, 0.0)
    ops.node(121016, 12.0, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.25, 28951009.78483889, 12062920.74368287, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 557.78837343, 0.00099708, 668.65472329, 0.0382987, 66.86547233, 0.1013303, -557.78837343, -0.00099708, -668.65472329, -0.0382987, -66.86547233, -0.1013303, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 557.78837343, 0.00099708, 668.65472329, 0.0382987, 66.86547233, 0.1013303, -557.78837343, -0.00099708, -668.65472329, -0.0382987, -66.86547233, -0.1013303, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 16.5, 9.0, 0.0)
    ops.node(121017, 16.5, 9.0, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.3025, 27782287.66946178, 11575953.19560908, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 802.95969253, 0.00097125, 963.91145826, 0.04917801, 96.39114583, 0.13161377, -802.95969253, -0.00097125, -963.91145826, -0.04917801, -96.39114583, -0.13161377, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 836.63816453, 0.00097125, 1004.34071687, 0.04917801, 100.43407169, 0.13161377, -836.63816453, -0.00097125, -1004.34071687, -0.04917801, -100.43407169, -0.13161377, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.2025, 28399578.10402948, 11833157.54334562, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 413.61139952, 0.00115215, 495.57106614, 0.03932697, 49.55710661, 0.1046056, -413.61139952, -0.00115215, -495.57106614, -0.03932697, -49.55710661, -0.1046056, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 436.67724988, 0.00115215, 523.20755794, 0.03932697, 52.32075579, 0.1046056, -436.67724988, -0.00115215, -523.20755794, -0.03932697, -52.32075579, -0.1046056, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.1225, 28564195.98273878, 11901748.32614116, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 191.40486522, 0.00136835, 229.32436157, 0.04147755, 22.93243616, 0.12444921, -191.40486522, -0.00136835, -229.32436157, -0.04147755, -22.93243616, -0.12444921, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 191.40486522, 0.00136835, 229.32436157, 0.04147755, 22.93243616, 0.12444921, -191.40486522, -0.00136835, -229.32436157, -0.04147755, -22.93243616, -0.12444921, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 4.5, 13.5, 0.0)
    ops.node(121020, 4.5, 13.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.2025, 29334359.91789567, 12222649.96578986, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 423.12737522, 0.00111854, 506.74722548, 0.04002285, 50.67472255, 0.10946308, -423.12737522, -0.00111854, -506.74722548, -0.04002285, -50.67472255, -0.10946308, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 447.56427519, 0.00111854, 536.01342755, 0.04002285, 53.60134275, 0.10946308, -447.56427519, -0.00111854, -536.01342755, -0.04002285, -53.60134275, -0.10946308, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 9.0, 13.5, 0.0)
    ops.node(121021, 9.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.2025, 29985885.61885705, 12494119.0078571, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 481.70310319, 0.00109634, 577.7752581, 0.04200568, 57.77752581, 0.11882404, -481.70310319, -0.00109634, -577.7752581, -0.04200568, -57.77752581, -0.11882404, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 433.25443252, 0.00109634, 519.66385501, 0.04200568, 51.9663855, 0.11882404, -433.25443252, -0.00109634, -519.66385501, -0.04200568, -51.9663855, -0.11882404, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 12.0, 13.5, 0.0)
    ops.node(121022, 12.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.2025, 28869664.30177101, 12029026.79240459, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 489.98862277, 0.00111172, 588.38885849, 0.04188019, 58.83888585, 0.11426083, -489.98862277, -0.00111172, -588.38885849, -0.04188019, -58.83888585, -0.11426083, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 438.85745111, 0.00111172, 526.98944975, 0.04188019, 52.69894497, 0.11426083, -438.85745111, -0.00111172, -526.98944975, -0.04188019, -52.69894497, -0.11426083, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 16.5, 13.5, 0.0)
    ops.node(121023, 16.5, 13.5, 2.825)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.2025, 28946368.05670452, 12060986.69029355, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 418.49481422, 0.00108843, 501.32070549, 0.04008515, 50.13207055, 0.10783688, -418.49481422, -0.00108843, -501.32070549, -0.04008515, -50.13207055, -0.10783688, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 443.16310368, 0.00108843, 530.87118941, 0.04008515, 53.08711894, 0.10783688, -443.16310368, -0.00108843, -530.87118941, -0.04008515, -53.08711894, -0.10783688, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.1225, 27886354.61364824, 11619314.42235343, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 189.03426052, 0.00138991, 226.50128078, 0.04169789, 22.65012808, 0.12067148, -189.03426052, -0.00138991, -226.50128078, -0.04169789, -22.65012808, -0.12067148, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 189.03426052, 0.00138991, 226.50128078, 0.04169789, 22.65012808, 0.12067148, -189.03426052, -0.00138991, -226.50128078, -0.04169789, -22.65012808, -0.12067148, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.35)
    ops.node(122001, 0.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.16, 29276942.8222922, 12198726.17595509, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 233.6410595, 0.00109399, 282.01495132, 0.03936925, 28.20149513, 0.12178101, -233.6410595, -0.00109399, -282.01495132, -0.03936925, -28.20149513, -0.12178101, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 253.26145984, 0.00109399, 305.69763047, 0.03936925, 30.56976305, 0.12178101, -253.26145984, -0.00109399, -305.69763047, -0.03936925, -30.56976305, -0.12178101, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.5, 0.0, 3.375)
    ops.node(122002, 4.5, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.2025, 29983777.21754815, 12493240.50731173, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 427.7893987, 0.00104189, 514.28581364, 0.03729221, 51.42858136, 0.10727991, -427.7893987, -0.00104189, -514.28581364, -0.03729221, -51.42858136, -0.10727991, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 427.7893987, 0.00104189, 514.28581364, 0.03729221, 51.42858136, 0.10727991, -427.7893987, -0.00104189, -514.28581364, -0.03729221, -51.42858136, -0.10727991, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.5, 0.0, 3.375)
    ops.node(122005, 16.5, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.2025, 28324076.02951979, 11801698.34563325, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 440.41380688, 0.0010638, 530.50084886, 0.03729498, 53.05008489, 0.10202875, -440.41380688, -0.0010638, -530.50084886, -0.03729498, -53.05008489, -0.10202875, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 440.41380688, 0.0010638, 530.50084886, 0.03729498, 53.05008489, 0.10202875, -440.41380688, -0.0010638, -530.50084886, -0.03729498, -53.05008489, -0.10202875, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 21.0, 0.0, 3.35)
    ops.node(122006, 21.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.16, 26719602.6483393, 11133167.77014138, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 229.87727096, 0.00115861, 278.21461807, 0.03788109, 27.82146181, 0.1115818, -229.87727096, -0.00115861, -278.21461807, -0.03788109, -27.82146181, -0.1115818, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 249.30376684, 0.00115861, 301.72601226, 0.03788109, 30.17260123, 0.1115818, -249.30376684, -0.00115861, -301.72601226, -0.03788109, -30.17260123, -0.1115818, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.35)
    ops.node(122007, 0.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.2025, 28313317.32499262, 11797215.55208026, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 331.15464653, 0.00104243, 398.85704625, 0.03583007, 39.88570462, 0.10033862, -331.15464653, -0.00104243, -398.85704625, -0.03583007, -39.88570462, -0.10033862, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 376.29962347, 0.00104243, 453.2316182, 0.03583007, 45.32316182, 0.10033862, -376.29962347, -0.00104243, -453.2316182, -0.03583007, -45.32316182, -0.10033862, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.5, 4.5, 3.375)
    ops.node(122008, 4.5, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.3025, 29408319.40775915, 12253466.41989965, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 575.39633236, 0.00086926, 692.9112649, 0.03639362, 69.29112649, 0.10785351, -575.39633236, -0.00086926, -692.9112649, -0.03639362, -69.29112649, -0.10785351, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 635.76955625, 0.00086926, 765.61469484, 0.03639362, 76.56146948, 0.10785351, -635.76955625, -0.00086926, -765.61469484, -0.03639362, -76.56146948, -0.10785351, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.0, 4.5, 3.35)
    ops.node(122009, 9.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.25, 28869719.10746099, 12029049.62810875, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 511.393303, 0.00094913, 615.88606427, 0.03568844, 61.58860643, 0.09702387, -511.393303, -0.00094913, -615.88606427, -0.03568844, -61.58860643, -0.09702387, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 511.393303, 0.00094913, 615.88606427, 0.03568844, 61.58860643, 0.09702387, -511.393303, -0.00094913, -615.88606427, -0.03568844, -61.58860643, -0.09702387, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.0, 4.5, 3.35)
    ops.node(122010, 12.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.25, 30144443.78081202, 12560184.90867168, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 522.24782733, 0.00093516, 627.8577495, 0.03493591, 62.78577495, 0.09977364, -522.24782733, -0.00093516, -627.8577495, -0.03493591, -62.78577495, -0.09977364, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 522.24782733, 0.00093516, 627.8577495, 0.03493591, 62.78577495, 0.09977364, -522.24782733, -0.00093516, -627.8577495, -0.03493591, -62.78577495, -0.09977364, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 16.5, 4.5, 3.375)
    ops.node(122011, 16.5, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.3025, 28061049.99688608, 11692104.1653692, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 576.93548066, 0.00089704, 695.79278374, 0.03630462, 69.57927837, 0.10340334, -576.93548066, -0.00089704, -695.79278374, -0.03630462, -69.57927837, -0.10340334, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 638.38354848, 0.00089704, 769.90006887, 0.03630462, 76.99000689, 0.10340334, -638.38354848, -0.00089704, -769.90006887, -0.03630462, -76.99000689, -0.10340334, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.35)
    ops.node(122012, 21.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.2025, 30221821.11777773, 12592425.46574072, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 337.27598878, 0.00100333, 405.28472983, 0.0355089, 40.52847298, 0.1060142, -337.27598878, -0.00100333, -405.28472983, -0.0355089, -40.52847298, -0.1060142, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 383.59843998, 0.00100333, 460.94769649, 0.0355089, 46.09476965, 0.1060142, -383.59843998, -0.00100333, -460.94769649, -0.0355089, -46.09476965, -0.1060142, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.35)
    ops.node(122013, 0.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.2025, 29278846.50758622, 12199519.37816093, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 335.52461799, 0.00101736, 403.73713847, 0.03614381, 40.37371385, 0.10387857, -335.52461799, -0.00101736, -403.73713847, -0.03614381, -40.37371385, -0.10387857, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 382.02000248, 0.00101736, 459.68508531, 0.03614381, 45.96850853, 0.10387857, -382.02000248, -0.00101736, -459.68508531, -0.03614381, -45.96850853, -0.10387857, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.5, 9.0, 3.375)
    ops.node(122014, 4.5, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.3025, 30381501.89240102, 12658959.12183376, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 580.27052444, 0.00085686, 697.70805764, 0.03601248, 69.77080576, 0.11031367, -580.27052444, -0.00085686, -697.70805764, -0.03601248, -69.77080576, -0.11031367, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 641.21880173, 0.00085686, 770.99129774, 0.03601248, 77.09912977, 0.11031367, -641.21880173, -0.00085686, -770.99129774, -0.03601248, -77.09912977, -0.11031367, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 9.0, 3.35)
    ops.node(122015, 9.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.25, 30403263.32896081, 12668026.38706701, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 526.62198092, 0.00092017, 632.7829864, 0.03533016, 63.27829864, 0.10065704, -526.62198092, -0.00092017, -632.7829864, -0.03533016, -63.27829864, -0.10065704, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 526.62198092, 0.00092017, 632.7829864, 0.03533016, 63.27829864, 0.10065704, -526.62198092, -0.00092017, -632.7829864, -0.03533016, -63.27829864, -0.10065704, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.0, 9.0, 3.35)
    ops.node(122016, 12.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.25, 28732234.16407426, 11971764.23503094, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 522.84129041, 0.00094735, 629.69970669, 0.03464912, 62.96997067, 0.09539093, -522.84129041, -0.00094735, -629.69970669, -0.03464912, -62.96997067, -0.09539093, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 522.84129041, 0.00094735, 629.69970669, 0.03464912, 62.96997067, 0.09539093, -522.84129041, -0.00094735, -629.69970669, -0.03464912, -62.96997067, -0.09539093, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 16.5, 9.0, 3.375)
    ops.node(122017, 16.5, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.3025, 29083049.60271313, 12117937.3344638, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 580.14287104, 0.0008661, 698.94819722, 0.03658618, 69.89481972, 0.10710695, -580.14287104, -0.0008661, -698.94819722, -0.03658618, -69.89481972, -0.10710695, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 642.81768, 0.0008661, 774.45794993, 0.03658618, 77.44579499, 0.10710695, -642.81768, -0.0008661, -774.45794993, -0.03658618, -77.44579499, -0.10710695, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.35)
    ops.node(122018, 21.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.2025, 27547377.0063777, 11478073.75265738, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 329.28468199, 0.00104687, 396.79454402, 0.03515638, 39.6794544, 0.09696924, -329.28468199, -0.00104687, -396.79454402, -0.03515638, -39.6794544, -0.09696924, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 374.88406873, 0.00104687, 451.74270546, 0.03515638, 45.17427055, 0.09696924, -374.88406873, -0.00104687, -451.74270546, -0.03515638, -45.17427055, -0.09696924, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.35)
    ops.node(122019, 0.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.1225, 28448725.93587481, 11853635.8066145, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 170.01913085, 0.00127102, 204.79221683, 0.04547022, 20.47922168, 0.14188204, -170.01913085, -0.00127102, -204.79221683, -0.04547022, -20.47922168, -0.14188204, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 170.01913085, 0.00127102, 204.79221683, 0.04547022, 20.47922168, 0.14188204, -170.01913085, -0.00127102, -204.79221683, -0.04547022, -20.47922168, -0.14188204, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 4.5, 13.5, 3.375)
    ops.node(122020, 4.5, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.2025, 28833605.38011491, 12014002.24171454, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 384.68751595, 0.00106339, 463.13958317, 0.036385, 46.31395832, 0.10274232, -384.68751595, -0.00106339, -463.13958317, -0.036385, -46.31395832, -0.10274232, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 407.66990788, 0.00106339, 490.80893811, 0.036385, 49.08089381, 0.10274232, -407.66990788, -0.00106339, -490.80893811, -0.036385, -49.08089381, -0.10274232, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.35)
    ops.node(122021, 9.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.2025, 28524119.93168663, 11885049.9715361, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 423.86517824, 0.00103523, 511.39077078, 0.03702461, 51.13907708, 0.1060049, -423.86517824, -0.00103523, -511.39077078, -0.03702461, -51.13907708, -0.1060049, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 352.33347246, 0.00103523, 425.08820092, 0.03702461, 42.50882009, 0.1060049, -352.33347246, -0.00103523, -425.08820092, -0.03702461, -42.50882009, -0.1060049, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.35)
    ops.node(122022, 12.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.2025, 28475381.74435409, 11864742.39348087, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 413.9708811, 0.00103023, 499.4798479, 0.03740346, 49.94798479, 0.10623098, -413.9708811, -0.00103023, -499.4798479, -0.03740346, -49.94798479, -0.10623098, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 345.55684881, 0.00103023, 416.93435496, 0.03740346, 41.6934355, 0.10623098, -345.55684881, -0.00103023, -416.93435496, -0.03740346, -41.6934355, -0.10623098, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 16.5, 13.5, 3.375)
    ops.node(122023, 16.5, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.2025, 28538810.48410513, 11891171.0350438, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 378.48958677, 0.00103092, 455.8069741, 0.03651097, 45.58069741, 0.10188908, -378.48958677, -0.00103092, -455.8069741, -0.03651097, -45.58069741, -0.10188908, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 401.45461157, 0.00103092, 483.46326593, 0.03651097, 48.34632659, 0.10188908, -401.45461157, -0.00103092, -483.46326593, -0.03651097, -48.34632659, -0.10188908, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.35)
    ops.node(122024, 21.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.1225, 28523454.06782252, 11884772.52825938, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 176.6251945, 0.00124513, 212.73535886, 0.04513427, 21.27353589, 0.14191816, -176.6251945, -0.00124513, -212.73535886, -0.04513427, -21.27353589, -0.14191816, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 176.6251945, 0.00124513, 212.73535886, 0.04513427, 21.27353589, 0.14191816, -176.6251945, -0.00124513, -212.73535886, -0.04513427, -21.27353589, -0.14191816, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.15)
    ops.node(123001, 0.0, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.16, 28691328.24760136, 11954720.10316724, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 233.57742921, 0.00110586, 283.30392897, 0.04310859, 28.3303929, 0.13387743, -233.57742921, -0.00110586, -283.30392897, -0.04310859, -28.3303929, -0.13387743, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 270.30268982, 0.00110586, 327.84766189, 0.04310859, 32.78476619, 0.13387743, -270.30268982, -0.00110586, -327.84766189, -0.04310859, -32.78476619, -0.13387743, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.5, 0.0, 6.15)
    ops.node(123002, 4.5, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.2025, 28915980.09156365, 12048325.03815152, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 270.20176404, 0.00097514, 326.860175, 0.0376937, 32.6860175, 0.11468973, -270.20176404, -0.00097514, -326.860175, -0.0376937, -32.6860175, -0.11468973, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 291.84245322, 0.00097514, 353.03868453, 0.0376937, 35.30386845, 0.11468973, -291.84245322, -0.00097514, -353.03868453, -0.0376937, -35.30386845, -0.11468973, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.5, 0.0, 6.15)
    ops.node(123005, 16.5, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.2025, 27723062.9021742, 11551276.20923925, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 278.87614816, 0.00101276, 337.91656648, 0.0368477, 33.79165665, 0.11068429, -278.87614816, -0.00101276, -337.91656648, -0.0368477, -33.79165665, -0.11068429, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 302.33240826, 0.00101276, 366.33871347, 0.0368477, 36.63387135, 0.11068429, -302.33240826, -0.00101276, -366.33871347, -0.0368477, -36.63387135, -0.11068429, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 21.0, 0.0, 6.15)
    ops.node(123006, 21.0, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.16, 29776046.75268529, 12406686.1469522, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 241.55712638, 0.00107079, 292.34962418, 0.04179576, 29.23496242, 0.13488618, -241.55712638, -0.00107079, -292.34962418, -0.04179576, -29.23496242, -0.13488618, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 281.27572728, 0.00107079, 340.41990147, 0.04179576, 34.04199015, 0.13488618, -281.27572728, -0.00107079, -340.41990147, -0.04179576, -34.04199015, -0.13488618, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.15)
    ops.node(123007, 0.0, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.2025, 28198780.87455999, 11749492.03106667, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 352.48677109, 0.00101019, 426.83320877, 0.03955846, 42.68332088, 0.11458972, -352.48677109, -0.00101019, -426.83320877, -0.03955846, -42.68332088, -0.11458972, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 375.81915903, 0.00101019, 455.0868592, 0.03955846, 45.50868592, 0.11458972, -375.81915903, -0.00101019, -455.0868592, -0.03955846, -45.50868592, -0.11458972, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.5, 4.5, 6.15)
    ops.node(123008, 4.5, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.3025, 28363421.26852272, 11818092.1952178, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 485.3644943, 0.00086346, 587.82505689, 0.03813617, 58.78250569, 0.11597239, -485.3644943, -0.00086346, -587.82505689, -0.03813617, -58.78250569, -0.11597239, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 514.149691, 0.00086346, 622.6868156, 0.03813617, 62.26868156, 0.11597239, -514.149691, -0.00086346, -622.6868156, -0.03813617, -62.26868156, -0.11597239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.15)
    ops.node(123009, 9.0, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.25, 28894102.54073643, 12039209.39197351, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 545.16512393, 0.00095163, 659.49470569, 0.03828998, 65.94947057, 0.10848883, -545.16512393, -0.00095163, -659.49470569, -0.03828998, -65.94947057, -0.10848883, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 517.62964307, 0.00095163, 626.18460744, 0.03828998, 62.61846074, 0.10848883, -517.62964307, -0.00095163, -626.18460744, -0.03828998, -62.61846074, -0.10848883, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.15)
    ops.node(123010, 12.0, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.25, 27850484.34329462, 11604368.47637276, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 533.32832897, 0.00096099, 646.13055284, 0.03835352, 64.61305528, 0.10604305, -533.32832897, -0.00096099, -646.13055284, -0.03835352, -64.61305528, -0.10604305, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 506.51785425, 0.00096099, 613.64949771, 0.03835352, 61.36494977, 0.10604305, -506.51785425, -0.00096099, -613.64949771, -0.03835352, -61.36494977, -0.10604305, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 16.5, 4.5, 6.15)
    ops.node(123011, 16.5, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.3025, 26970645.92373956, 11237769.13489148, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 489.3936391, 0.00087985, 593.67814881, 0.03801476, 59.36781488, 0.11187781, -489.3936391, -0.00087985, -593.67814881, -0.03801476, -59.36781488, -0.11187781, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 519.50751036, 0.00087985, 630.20896146, 0.03801476, 63.02089615, 0.11187781, -519.50751036, -0.00087985, -630.20896146, -0.03801476, -63.02089615, -0.11187781, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.15)
    ops.node(123012, 21.0, 4.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.2025, 28354397.05412301, 11814332.10588459, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 349.96928976, 0.00101792, 423.69398279, 0.03918062, 42.36939828, 0.1146273, -349.96928976, -0.00101792, -423.69398279, -0.03918062, -42.36939828, -0.1146273, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 372.64925361, 0.00101792, 451.15171836, 0.03918062, 45.11517184, 0.1146273, -372.64925361, -0.00101792, -451.15171836, -0.03918062, -45.11517184, -0.1146273, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.15)
    ops.node(123013, 0.0, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.2025, 29179792.43480535, 12158246.84783556, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 348.78328404, 0.00101317, 421.72254708, 0.03920718, 42.17225471, 0.11678917, -348.78328404, -0.00101317, -421.72254708, -0.03920718, -42.17225471, -0.11678917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 370.83004965, 0.00101317, 448.37983995, 0.03920718, 44.83798399, 0.11678917, -370.83004965, -0.00101317, -448.37983995, -0.03920718, -44.83798399, -0.11678917, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.5, 9.0, 6.15)
    ops.node(123014, 4.5, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.3025, 29511899.12359496, 12296624.63483123, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 490.51308033, 0.00085009, 592.936897, 0.03795625, 59.2936897, 0.1186715, -490.51308033, -0.00085009, -592.936897, -0.03795625, -59.2936897, -0.1186715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 519.60340566, 0.00085009, 628.10156014, 0.03795625, 62.81015601, 0.1186715, -519.60340566, -0.00085009, -628.10156014, -0.03795625, -62.81015601, -0.1186715, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.15)
    ops.node(123015, 9.0, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.25, 28799120.42305537, 11999633.50960641, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 528.31576017, 0.00092407, 639.11029133, 0.03834257, 63.91102913, 0.10800419, -528.31576017, -0.00092407, -639.11029133, -0.03834257, -63.91102913, -0.10800419, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 501.94186502, 0.00092407, 607.20545509, 0.03834257, 60.72054551, 0.10800419, -501.94186502, -0.00092407, -607.20545509, -0.03834257, -60.72054551, -0.10800419, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.15)
    ops.node(123016, 12.0, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.25, 28689745.98277812, 11954060.82615755, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 541.05027616, 0.00094909, 654.62596349, 0.03850399, 65.46259635, 0.10791115, -541.05027616, -0.00094909, -654.62596349, -0.03850399, -65.46259635, -0.10791115, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 513.85364499, 0.00094909, 621.72029526, 0.03850399, 62.17202953, 0.10791115, -513.85364499, -0.00094909, -621.72029526, -0.03850399, -62.17202953, -0.10791115, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 16.5, 9.0, 6.15)
    ops.node(123017, 16.5, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.3025, 29413992.17863301, 12255830.07443042, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 493.92175838, 0.00083938, 597.16662406, 0.03754517, 59.71666241, 0.11803563, -493.92175838, -0.00083938, -597.16662406, -0.03754517, -59.71666241, -0.11803563, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 524.00604569, 0.00083938, 633.53945435, 0.03754517, 63.35394544, 0.11803563, -524.00604569, -0.00083938, -633.53945435, -0.03754517, -63.35394544, -0.11803563, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.15)
    ops.node(123018, 21.0, 9.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.2025, 28682349.43846076, 11950978.93269199, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 349.24082791, 0.00100478, 422.61874989, 0.03966455, 42.26187499, 0.11601922, -349.24082791, -0.00100478, -422.61874989, -0.03966455, -42.26187499, -0.11601922, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 371.88149274, 0.00100478, 450.01637555, 0.03966455, 45.00163755, 0.11601922, -371.88149274, -0.00100478, -450.01637555, -0.03966455, -45.00163755, -0.11601922, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.15)
    ops.node(123019, 0.0, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1225, 29786819.70148348, 12411174.87561812, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 214.27036504, 0.00125865, 258.8565779, 0.05350495, 25.88565779, 0.15350495, -214.27036504, -0.00125865, -258.8565779, -0.05350495, -25.88565779, -0.15350495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 214.27036504, 0.00125865, 258.8565779, 0.05350495, 25.88565779, 0.15350495, -214.27036504, -0.00125865, -258.8565779, -0.05350495, -25.88565779, -0.15350495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 4.5, 13.5, 6.15)
    ops.node(123020, 4.5, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.2025, 29619982.48268694, 12341659.36778622, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 322.32943108, 0.00099825, 389.43525563, 0.03840838, 38.94352556, 0.11707091, -322.32943108, -0.00099825, -389.43525563, -0.03840838, -38.94352556, -0.11707091, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 322.32943108, 0.00099825, 389.43525563, 0.03840838, 38.94352556, 0.11707091, -322.32943108, -0.00099825, -389.43525563, -0.03840838, -38.94352556, -0.11707091, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.15)
    ops.node(123021, 9.0, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.2025, 29462749.74273761, 12276145.72614067, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 469.61252255, 0.00100976, 568.15515137, 0.04217077, 56.81551514, 0.12301112, -469.61252255, -0.00100976, -568.15515137, -0.04217077, -56.81551514, -0.12301112, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 399.35479236, 0.00100976, 483.15466817, 0.04217077, 48.31546682, 0.12301112, -399.35479236, -0.00100976, -483.15466817, -0.04217077, -48.31546682, -0.12301112, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.15)
    ops.node(123022, 12.0, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.2025, 28200443.98773813, 11750184.99489089, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 464.28044775, 0.0010391, 562.93162088, 0.04185988, 56.29316209, 0.11984045, -464.28044775, -0.0010391, -562.93162088, -0.04185988, -56.29316209, -0.11984045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 394.94025493, 0.0010391, 478.85789492, 0.04185988, 47.88578949, 0.11984045, -394.94025493, -0.0010391, -478.85789492, -0.04185988, -47.88578949, -0.11984045, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 16.5, 13.5, 6.15)
    ops.node(123023, 16.5, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.2025, 28979479.29863358, 12074783.04109732, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 325.90504061, 0.00098938, 394.20274169, 0.03822527, 39.42027417, 0.11537736, -325.90504061, -0.00098938, -394.20274169, -0.03822527, -39.42027417, -0.11537736, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 325.90504061, 0.00098938, 394.20274169, 0.03822527, 39.42027417, 0.11537736, -325.90504061, -0.00098938, -394.20274169, -0.03822527, -39.42027417, -0.11537736, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.15)
    ops.node(123024, 21.0, 13.5, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.1225, 30123186.53883194, 12551327.72451331, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 220.15774979, 0.00122616, 265.78664767, 0.05295975, 26.57866477, 0.15295975, -220.15774979, -0.00122616, -265.78664767, -0.05295975, -26.57866477, -0.15295975, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 220.15774979, 0.00122616, 265.78664767, 0.05295975, 26.57866477, 0.15295975, -220.15774979, -0.00122616, -265.78664767, -0.05295975, -26.57866477, -0.15295975, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.925)
    ops.node(124001, 0.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.16, 28065363.77186851, 11693901.57161188, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 190.38118094, 0.0011284, 232.27219969, 0.04456995, 23.22721997, 0.14456995, -190.38118094, -0.0011284, -232.27219969, -0.04456995, -23.22721997, -0.14456995, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 207.46723546, 0.0011284, 253.11782868, 0.04456995, 25.31178287, 0.14456995, -207.46723546, -0.0011284, -253.11782868, -0.04456995, -25.31178287, -0.14456995, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.5, 0.0, 8.925)
    ops.node(124002, 4.5, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.2025, 28856984.96102967, 12023743.73376236, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 285.81178445, 0.00095385, 347.65392828, 0.04152462, 34.76539283, 0.13183686, -285.81178445, -0.00095385, -347.65392828, -0.04152462, -34.76539283, -0.13183686, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 285.81178445, 0.00095385, 347.65392828, 0.04152462, 34.76539283, 0.13183686, -285.81178445, -0.00095385, -347.65392828, -0.04152462, -34.76539283, -0.13183686, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.5, 0.0, 8.925)
    ops.node(124005, 16.5, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.2025, 29443011.75311004, 12267921.56379585, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 291.01865087, 0.00094632, 353.50724205, 0.04097185, 35.3507242, 0.13197977, -291.01865087, -0.00094632, -353.50724205, -0.04097185, -35.3507242, -0.13197977, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 291.01865087, 0.00094632, 353.50724205, 0.04097185, 35.3507242, 0.13197977, -291.01865087, -0.00094632, -353.50724205, -0.04097185, -35.3507242, -0.13197977, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 21.0, 0.0, 8.925)
    ops.node(124006, 21.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.16, 30048237.24145513, 12520098.85060631, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 193.80232417, 0.00105906, 235.31149642, 0.04357405, 23.53114964, 0.14357405, -193.80232417, -0.00105906, -235.31149642, -0.04357405, -23.53114964, -0.14357405, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 211.70167706, 0.00105906, 257.04458724, 0.04357405, 25.70445872, 0.14357405, -211.70167706, -0.00105906, -257.04458724, -0.04357405, -25.70445872, -0.14357405, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 8.925)
    ops.node(124007, 0.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.2025, 28586722.73181906, 11911134.47159127, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 264.97710723, 0.00095579, 322.50232509, 0.04178621, 32.25023251, 0.13175844, -264.97710723, -0.00095579, -322.50232509, -0.04178621, -32.25023251, -0.13175844, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 309.26036002, 0.00095579, 376.39925277, 0.04178621, 37.63992528, 0.13175844, -309.26036002, -0.00095579, -376.39925277, -0.04178621, -37.63992528, -0.13175844, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.5, 4.5, 8.925)
    ops.node(124008, 4.5, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.3025, 26973401.73501252, 11238917.38958855, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 356.89946761, 0.0008548, 435.53487182, 0.04067092, 43.55348718, 0.12888635, -356.89946761, -0.0008548, -435.53487182, -0.04067092, -43.55348718, -0.12888635, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 411.03386587, 0.0008548, 501.5966633, 0.04067092, 50.15966633, 0.12888635, -411.03386587, -0.0008548, -501.5966633, -0.04067092, -50.15966633, -0.12888635, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.0, 4.5, 8.925)
    ops.node(124009, 9.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.25, 29795198.72432537, 12414666.13513557, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 375.16206354, 0.00088254, 455.18157685, 0.03959809, 45.51815769, 0.122242, -375.16206354, -0.00088254, -455.18157685, -0.03959809, -45.51815769, -0.122242, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 400.62055926, 0.00088254, 486.07019635, 0.03959809, 48.60701963, 0.122242, -400.62055926, -0.00088254, -486.07019635, -0.03959809, -48.60701963, -0.122242, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.0, 4.5, 8.925)
    ops.node(124010, 12.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.25, 29650940.71432991, 12354558.6309708, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 368.98499066, 0.00087021, 447.84485999, 0.03997756, 44.784486, 0.12246553, -368.98499066, -0.00087021, -447.84485999, -0.03997756, -44.784486, -0.12246553, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 393.97729057, 0.00087021, 478.17854114, 0.03997756, 47.81785411, 0.12246553, -393.97729057, -0.00087021, -478.17854114, -0.03997756, -47.81785411, -0.12246553, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 16.5, 4.5, 8.925)
    ops.node(124011, 16.5, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.3025, 29400394.6115024, 12250164.42145933, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 366.20051253, 0.00080623, 444.7291279, 0.03940535, 44.47291279, 0.13125063, -366.20051253, -0.00080623, -444.7291279, -0.03940535, -44.47291279, -0.13125063, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 423.52784991, 0.00080623, 514.3498299, 0.03940535, 51.43498299, 0.13125063, -423.52784991, -0.00080623, -514.3498299, -0.03940535, -51.43498299, -0.13125063, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 8.925)
    ops.node(124012, 21.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.2025, 28512480.08505565, 11880200.03543985, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 260.6227801, 0.00095789, 317.25319678, 0.04210164, 31.72531968, 0.13197823, -260.6227801, -0.00095789, -317.25319678, -0.04210164, -31.72531968, -0.13197823, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 303.23665061, 0.00095789, 369.12658497, 0.04210164, 36.9126585, 0.13197823, -303.23665061, -0.00095789, -369.12658497, -0.04210164, -36.9126585, -0.13197823, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.0, 8.925)
    ops.node(124013, 0.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.2025, 30400488.43428635, 12666870.18095265, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 263.43958839, 0.00093165, 319.23004484, 0.04099749, 31.92300448, 0.13303058, -263.43958839, -0.00093165, -319.23004484, -0.04099749, -31.92300448, -0.13303058, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 305.98958935, 0.00093165, 370.79115908, 0.04099749, 37.07911591, 0.13303058, -305.98958935, -0.00093165, -370.79115908, -0.04099749, -37.07911591, -0.13303058, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.5, 9.0, 8.925)
    ops.node(124014, 4.5, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.3025, 28918156.14845604, 12049231.72852335, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 351.16282665, 0.00081902, 426.9358295, 0.040486, 42.69358295, 0.1317025, -351.16282665, -0.00081902, -426.9358295, -0.040486, -42.69358295, -0.1317025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 402.46202105, 0.00081902, 489.30423085, 0.040486, 48.93042308, 0.1317025, -402.46202105, -0.00081902, -489.30423085, -0.040486, -48.93042308, -0.1317025, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 9.0, 8.925)
    ops.node(124015, 9.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.25, 29755079.90233963, 12397949.95930818, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 402.65950851, 0.00089008, 488.48512747, 0.0400246, 48.84851275, 0.12208733, -402.65950851, -0.00089008, -488.48512747, -0.0400246, -48.84851275, -0.12208733, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 452.56516662, 0.00089008, 549.02802103, 0.0400246, 54.9028021, 0.12208733, -452.56516662, -0.00089008, -549.02802103, -0.0400246, -54.9028021, -0.12208733, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.0, 9.0, 8.925)
    ops.node(124016, 12.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.25, 27717531.24046704, 11548971.3501946, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 410.64113435, 0.00091796, 500.33187544, 0.04046477, 50.03318754, 0.11988163, -410.64113435, -0.00091796, -500.33187544, -0.04046477, -50.03318754, -0.11988163, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 464.24259623, 0.00091796, 565.64077342, 0.04046477, 56.56407734, 0.11988163, -464.24259623, -0.00091796, -565.64077342, -0.04046477, -56.56407734, -0.11988163, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 16.5, 9.0, 8.925)
    ops.node(124017, 16.5, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.3025, 29294531.08320606, 12206054.61800253, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 365.42961041, 0.00082675, 443.90260595, 0.04003667, 44.39026059, 0.13174738, -365.42961041, -0.00082675, -443.90260595, -0.04003667, -44.39026059, -0.13174738, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 420.92421227, 0.00082675, 511.31421595, 0.04003667, 51.1314216, 0.13174738, -420.92421227, -0.00082675, -511.31421595, -0.04003667, -51.1314216, -0.13174738, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 21.0, 9.0, 8.925)
    ops.node(124018, 21.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.2025, 28276579.87146988, 11781908.27977912, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 264.73009715, 0.00097306, 322.41264158, 0.04230345, 32.24126416, 0.13186961, -264.73009715, -0.00097306, -322.41264158, -0.04230345, -32.24126416, -0.13186961, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 308.50783749, 0.00097306, 375.72919704, 0.04230345, 37.5729197, 0.13186961, -308.50783749, -0.00097306, -375.72919704, -0.04230345, -37.5729197, -0.13186961, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 13.5, 8.925)
    ops.node(124019, 0.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1225, 29059762.37737821, 12108234.32390759, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 158.98038424, 0.00129037, 193.37950696, 0.05578214, 19.3379507, 0.15578214, -158.98038424, -0.00129037, -193.37950696, -0.05578214, -19.3379507, -0.15578214, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 172.98307452, 0.00129037, 210.41200663, 0.05578214, 21.04120066, 0.15578214, -172.98307452, -0.00129037, -210.41200663, -0.05578214, -21.04120066, -0.15578214, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 4.5, 13.5, 8.925)
    ops.node(124020, 4.5, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.2025, 29008850.08368358, 12087020.86820149, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 285.89306919, 0.00094323, 347.63377212, 0.04112083, 34.76337721, 0.1316187, -285.89306919, -0.00094323, -347.63377212, -0.04112083, -34.76337721, -0.1316187, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 285.89306919, 0.00094323, 347.63377212, 0.04112083, 34.76337721, 0.1316187, -285.89306919, -0.00094323, -347.63377212, -0.04112083, -34.76337721, -0.1316187, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 8.925)
    ops.node(124021, 9.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.2025, 29430899.32516948, 12262874.71882062, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 287.74005729, 0.00095963, 349.6857671, 0.04188025, 34.96857671, 0.1340531, -287.74005729, -0.00095963, -349.6857671, -0.04188025, -34.96857671, -0.1340531, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 287.74005729, 0.00095963, 349.6857671, 0.04188025, 34.96857671, 0.1340531, -287.74005729, -0.00095963, -349.6857671, -0.04188025, -34.96857671, -0.1340531, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 8.925)
    ops.node(124022, 12.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.2025, 30088173.06093352, 12536738.77538897, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 288.54925139, 0.0009524, 350.08492889, 0.04125728, 35.00849289, 0.13407345, -288.54925139, -0.0009524, -350.08492889, -0.04125728, -35.00849289, -0.13407345, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 288.54925139, 0.0009524, 350.08492889, 0.04125728, 35.00849289, 0.13407345, -288.54925139, -0.0009524, -350.08492889, -0.04125728, -35.00849289, -0.13407345, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 16.5, 13.5, 8.925)
    ops.node(124023, 16.5, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.2025, 29910122.49124818, 12462551.03802007, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 283.07157562, 0.00092736, 343.4577837, 0.04073145, 34.34577837, 0.13225583, -283.07157562, -0.00092736, -343.4577837, -0.04073145, -34.34577837, -0.13225583, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 283.07157562, 0.00092736, 343.4577837, 0.04073145, 34.34577837, 0.13225583, -283.07157562, -0.00092736, -343.4577837, -0.04073145, -34.34577837, -0.13225583, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 21.0, 13.5, 8.925)
    ops.node(124024, 21.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.1225, 28340378.52256946, 11808491.05107061, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 162.29276708, 0.0012135, 197.72738526, 0.05628804, 19.77273853, 0.15628804, -162.29276708, -0.0012135, -197.72738526, -0.05628804, -19.77273853, -0.15628804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 178.26098666, 0.0012135, 217.18206807, 0.05628804, 21.71820681, 0.15628804, -178.26098666, -0.0012135, -217.18206807, -0.05628804, -21.71820681, -0.15628804, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.2025, 28386603.27091398, 11827751.36288082, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 563.44115811, 0.0009485, 676.68168779, 0.08242656, 67.66816878, 0.18242656, -563.44115811, -0.0009485, -676.68168779, -0.08242656, -67.66816878, -0.18242656, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 512.13639046, 0.0009485, 615.06567649, 0.08242656, 61.50656765, 0.18242656, -512.13639046, -0.0009485, -615.06567649, -0.08242656, -61.50656765, -0.18242656, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.8)
    ops.node(121003, 9.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.2025, 27329416.16481504, 11387256.7353396, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 502.588114, 0.0009413, 604.56192157, 0.06094496, 60.45619216, 0.16094496, -502.588114, -0.0009413, -604.56192157, -0.06094496, -60.45619216, -0.16094496, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 400.91504571, 0.0009413, 482.25965491, 0.06094496, 48.22596549, 0.16094496, -400.91504571, -0.0009413, -482.25965491, -0.06094496, -48.22596549, -0.16094496, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.2025, 29187082.31193115, 12161284.29663798, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 567.75277577, 0.00092745, 681.48273086, 0.08297713, 68.14827309, 0.18297713, -567.75277577, -0.00092745, -681.48273086, -0.08297713, -68.14827309, -0.18297713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 515.92101932, 0.00092745, 619.26824519, 0.08297713, 61.92682452, 0.18297713, -515.92101932, -0.00092745, -619.26824519, -0.08297713, -61.92682452, -0.18297713, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.8)
    ops.node(121004, 12.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.2025, 28657095.79237412, 11940456.58015588, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 500.72922789, 0.00091775, 601.99215691, 0.06161784, 60.19921569, 0.16161784, -500.72922789, -0.00091775, -601.99215691, -0.06161784, -60.19921569, -0.16161784, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 401.50850125, 0.00091775, 482.70593211, 0.06161784, 48.27059321, 0.16161784, -401.50850125, -0.00091775, -482.70593211, -0.06161784, -48.27059321, -0.16161784, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.35)
    ops.node(124027, 9.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.2025, 28715545.48534923, 11964810.61889551, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 524.42098726, 0.00089183, 632.50530474, 0.09435082, 63.25053047, 0.19435082, -524.42098726, -0.00089183, -632.50530474, -0.09435082, -63.25053047, -0.19435082, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 402.99808075, 0.00089183, 486.05687047, 0.08618994, 48.60568705, 0.18618994, -402.99808075, -0.00089183, -486.05687047, -0.08618994, -48.60568705, -0.18618994, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.825)
    ops.node(122003, 9.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.2025, 29505996.50175001, 12294165.20906251, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 469.09133932, 0.00088083, 565.8154315, 0.08591651, 56.58154315, 0.18591651, -469.09133932, -0.00088083, -565.8154315, -0.08591651, -56.58154315, -0.18591651, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 374.02054697, 0.00088083, 451.14155695, 0.08591651, 45.1141557, 0.18591651, -374.02054697, -0.00088083, -451.14155695, -0.08591651, -45.1141557, -0.18591651, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.35)
    ops.node(124028, 12.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.2025, 28576250.54640857, 11906771.06100357, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 523.58585119, 0.00089162, 631.5983686, 0.0946496, 63.15983686, 0.1946496, -523.58585119, -0.00089162, -631.5983686, -0.0946496, -63.15983686, -0.1946496, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 402.10509847, 0.00089162, 485.05688918, 0.08646261, 48.50568892, 0.18646261, -402.10509847, -0.00089162, -485.05688918, -0.08646261, -48.50568892, -0.18646261, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.825)
    ops.node(122004, 12.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.2025, 29735496.10630044, 12389790.04429185, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 463.74331772, 0.00087449, 559.14843528, 0.08620014, 55.91484353, 0.18620014, -463.74331772, -0.00087449, -559.14843528, -0.08620014, -55.91484353, -0.18620014, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 370.84758905, 0.00087449, 447.14142765, 0.08620014, 44.71414276, 0.18620014, -370.84758905, -0.00087449, -447.14142765, -0.08620014, -44.71414276, -0.18620014, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.15)
    ops.node(124029, 9.0, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.2025, 28898462.86144735, 12041026.19226973, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 317.0371191, 0.00085947, 383.96433594, 0.05383315, 38.39643359, 0.15383315, -317.0371191, -0.00085947, -383.96433594, -0.05383315, -38.39643359, -0.15383315, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 317.0371191, 0.00085947, 383.96433594, 0.05383315, 38.39643359, 0.15383315, -317.0371191, -0.00085947, -383.96433594, -0.05383315, -38.39643359, -0.15383315, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.55)
    ops.node(123003, 9.0, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.2025, 28211120.30226747, 11754633.45927811, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 281.03011334, 0.00083832, 341.21424799, 0.05442477, 34.1214248, 0.15442477, -281.03011334, -0.00083832, -341.21424799, -0.05442477, -34.1214248, -0.15442477, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 258.37561697, 0.00083832, 313.70816741, 0.05442477, 31.37081674, 0.15442477, -258.37561697, -0.00083832, -313.70816741, -0.05442477, -31.37081674, -0.15442477, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.15)
    ops.node(124030, 12.0, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.2025, 29228268.39425199, 12178445.16427167, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 311.99406864, 0.00085601, 377.6307992, 0.05440899, 37.76307992, 0.15440899, -311.99406864, -0.00085601, -377.6307992, -0.05440899, -37.76307992, -0.15440899, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 311.99406864, 0.00085601, 377.6307992, 0.05440899, 37.76307992, 0.15440899, -311.99406864, -0.00085601, -377.6307992, -0.05440899, -37.76307992, -0.15440899, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.55)
    ops.node(123004, 12.0, 0.0, 8.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.2025, 27894563.40986128, 11622734.75410887, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 272.73817856, 0.00083397, 331.31563528, 0.05440045, 33.13156353, 0.15440045, -272.73817856, -0.00083397, -331.31563528, -0.05440045, -33.13156353, -0.15440045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 251.2381414, 0.00083397, 305.19791861, 0.05440045, 30.51979186, 0.15440045, -251.2381414, -0.00083397, -305.19791861, -0.05440045, -30.51979186, -0.15440045, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 8.925)
    ops.node(124031, 9.0, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.2025, 29180137.97929075, 12158390.82470448, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 252.91156475, 0.00082194, 307.56414807, 0.04007217, 30.75641481, 0.13215373, -252.91156475, -0.00082194, -307.56414807, -0.04007217, -30.75641481, -0.13215373, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 231.9083367, 0.00082194, 282.0222558, 0.04007217, 28.20222558, 0.13215373, -231.9083367, -0.00082194, -282.0222558, -0.04007217, -28.20222558, -0.13215373, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 9.0, 0.0, 10.25)
    ops.node(124003, 9.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.2025, 28249596.73326936, 11770665.3055289, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 249.35248334, 0.00081448, 304.27441329, 0.04229082, 30.42744133, 0.13699676, -249.35248334, -0.00081448, -304.27441329, -0.04229082, -30.42744133, -0.13699676, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 227.02733659, 0.00081448, 277.03196983, 0.04229082, 27.70319698, 0.13699676, -227.02733659, -0.00081448, -277.03196983, -0.04229082, -27.70319698, -0.13699676, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 8.925)
    ops.node(124032, 12.0, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.2025, 28884505.83171959, 12035210.7632165, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 251.57412514, 0.00081326, 306.14957194, 0.04056626, 30.61495719, 0.13233367, -251.57412514, -0.00081326, -306.14957194, -0.04056626, -30.61495719, -0.13233367, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 230.41758867, 0.00081326, 280.40342424, 0.04056626, 28.04034242, 0.13233367, -230.41758867, -0.00081326, -280.40342424, -0.04056626, -28.04034242, -0.13233367, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 12.0, 0.0, 10.25)
    ops.node(124004, 12.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.2025, 28326437.18227691, 11802682.15928205, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 245.91106688, 0.00082334, 300.02219599, 0.04204607, 30.0022196, 0.13681254, -245.91106688, -0.00082334, -300.02219599, -0.04204607, -30.0022196, -0.13681254, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 224.44782821, 0.00082334, 273.8361114, 0.04204607, 27.38361114, 0.13681254, -224.44782821, -0.00082334, -273.8361114, -0.04204607, -27.38361114, -0.13681254, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
