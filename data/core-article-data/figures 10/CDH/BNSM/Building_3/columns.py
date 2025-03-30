import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 28171992.66113896, 11738330.27547457, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 150.37995607, 0.00173799, 178.99784739, 0.04436802, 17.89978474, 0.11633199, -150.37995607, -0.00173799, -178.99784739, -0.04436802, -17.89978474, -0.11633199, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 150.37995607, 0.00173799, 178.99784739, 0.04436802, 17.89978474, 0.11633199, -150.37995607, -0.00173799, -178.99784739, -0.04436802, -17.89978474, -0.11633199, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.5, 0.0, 0.0)
    ops.node(121002, 4.5, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.16, 30146450.7232196, 12561021.13467483, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 269.15703322, 0.00117083, 320.8921263, 0.03192527, 32.08921263, 0.09335206, -269.15703322, -0.00117083, -320.8921263, -0.03192527, -32.08921263, -0.09335206, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 269.15703322, 0.00117083, 320.8921263, 0.03192527, 32.08921263, 0.09335206, -269.15703322, -0.00117083, -320.8921263, -0.03192527, -32.08921263, -0.09335206, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.5, 0.0, 0.0)
    ops.node(121005, 16.5, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.16, 28459127.10995806, 11857969.62914919, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 266.88314797, 0.00122467, 318.30673229, 0.03067893, 31.83067323, 0.08469355, -266.88314797, -0.00122467, -318.30673229, -0.03067893, -31.83067323, -0.08469355, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 266.88314797, 0.00122467, 318.30673229, 0.03067893, 31.83067323, 0.08469355, -266.88314797, -0.00122467, -318.30673229, -0.03067893, -31.83067323, -0.08469355, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 21.0, 0.0, 0.0)
    ops.node(121006, 21.0, 0.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.09, 28128671.11286058, 11720279.63035857, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 152.26064468, 0.00166004, 181.23081373, 0.04410742, 18.12308137, 0.11576941, -152.26064468, -0.00166004, -181.23081373, -0.04410742, -18.12308137, -0.11576941, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 152.26064468, 0.00166004, 181.23081373, 0.04410742, 18.12308137, 0.11576941, -152.26064468, -0.00166004, -181.23081373, -0.04410742, -18.12308137, -0.11576941, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.16, 28014913.05918365, 11672880.44132652, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 247.81626625, 0.00114596, 295.48257305, 0.02675206, 29.5482573, 0.07852992, -247.81626625, -0.00114596, -295.48257305, -0.02675206, -29.5482573, -0.07852992, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 275.06658425, 0.00114596, 327.97436303, 0.02675206, 32.7974363, 0.07852992, -275.06658425, -0.00114596, -327.97436303, -0.02675206, -32.7974363, -0.07852992, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.5, 4.5, 0.0)
    ops.node(121008, 4.5, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.25, 28849467.95308392, 12020611.6471183, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 529.03429371, 0.00103464, 632.87949687, 0.0361538, 63.28794969, 0.09494622, -529.03429371, -0.00103464, -632.87949687, -0.0361538, -63.28794969, -0.09494622, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 557.36638878, 0.00103464, 666.77295574, 0.0361538, 66.67729557, 0.09494622, -557.36638878, -0.00103464, -666.77295574, -0.0361538, -66.67729557, -0.09494622, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.2025, 29357638.77075427, 12232349.48781428, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 465.10948784, 0.00110353, 555.5276743, 0.03805005, 55.55276743, 0.10225748, -465.10948784, -0.00110353, -555.5276743, -0.03805005, -55.55276743, -0.10225748, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 439.93374086, 0.00110353, 525.45771328, 0.03805005, 52.54577133, 0.10225748, -439.93374086, -0.00110353, -525.45771328, -0.03805005, -52.54577133, -0.10225748, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.2025, 28988809.38776533, 12078670.57823556, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 462.77782124, 0.00111992, 552.8100603, 0.03838265, 55.28100603, 0.10089716, -462.77782124, -0.00111992, -552.8100603, -0.03838265, -55.28100603, -0.10089716, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 437.94480915, 0.00111992, 523.14584935, 0.03838265, 52.31458494, 0.10089716, -437.94480915, -0.00111992, -523.14584935, -0.03838265, -52.31458494, -0.10089716, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 16.5, 4.5, 0.0)
    ops.node(121011, 16.5, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.25, 28067695.21309378, 11694873.00545574, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 525.41810925, 0.00103089, 628.58978103, 0.03539823, 62.8589781, 0.09082231, -525.41810925, -0.00103089, -628.58978103, -0.03539823, -62.8589781, -0.09082231, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 554.0645767, 0.00103089, 662.8613, 0.03539823, 66.28613, 0.09082231, -554.0645767, -0.00103089, -662.8613, -0.03539823, -66.28613, -0.09082231, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 30379169.23356236, 12657987.18065098, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 252.44528619, 0.00113687, 300.89230693, 0.02869375, 30.08923069, 0.09094574, -252.44528619, -0.00113687, -300.89230693, -0.02869375, -30.08923069, -0.09094574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 279.11014237, 0.00113687, 332.67444163, 0.02869375, 33.26744416, 0.09094574, -279.11014237, -0.00113687, -332.67444163, -0.02869375, -33.26744416, -0.09094574, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.16, 28963055.11222184, 12067939.63009243, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 249.65811385, 0.00112316, 297.77359245, 0.02769732, 29.77735925, 0.08397475, -249.65811385, -0.00112316, -297.77359245, -0.02769732, -29.77735925, -0.08397475, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 277.27645634, 0.00112316, 330.71469312, 0.02769732, 33.07146931, 0.08397475, -277.27645634, -0.00112316, -330.71469312, -0.02769732, -33.07146931, -0.08397475, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.5, 9.0, 0.0)
    ops.node(121014, 4.5, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.25, 29702617.92737174, 12376090.80307156, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 521.13568668, 0.00097924, 623.17418371, 0.0371998, 62.31741837, 0.09953638, -521.13568668, -0.00097924, -623.17418371, -0.0371998, -62.31741837, -0.09953638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 549.09090342, 0.00097924, 656.60303884, 0.0371998, 65.66030388, 0.09953638, -549.09090342, -0.00097924, -656.60303884, -0.0371998, -65.66030388, -0.09953638, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.2025, 28999093.56691035, 12082955.65287931, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 409.96516818, 0.00110893, 489.70341996, 0.03190633, 48.970342, 0.08509336, -409.96516818, -0.00110893, -489.70341996, -0.03190633, -48.970342, -0.08509336, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 409.96516818, 0.00110893, 489.70341996, 0.03190633, 48.970342, 0.08509336, -409.96516818, -0.00110893, -489.70341996, -0.03190633, -48.970342, -0.08509336, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.2025, 28951009.78483889, 12062920.74368287, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 408.70374559, 0.00109275, 488.20157696, 0.03163247, 48.8201577, 0.08462871, -408.70374559, -0.00109275, -488.20157696, -0.03163247, -48.8201577, -0.08462871, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 408.70374559, 0.00109275, 488.20157696, 0.03163247, 48.8201577, 0.08462871, -408.70374559, -0.00109275, -488.20157696, -0.03163247, -48.8201577, -0.08462871, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 16.5, 9.0, 0.0)
    ops.node(121017, 16.5, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.25, 27782287.66946178, 11575953.19560908, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 530.77448567, 0.00103588, 634.99404837, 0.03569603, 63.49940484, 0.08994713, -530.77448567, -0.00103588, -634.99404837, -0.03569603, -63.49940484, -0.08994713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 560.44327573, 0.00103588, 670.48841673, 0.03569603, 67.04884167, 0.08994713, -560.44327573, -0.00103588, -670.48841673, -0.03569603, -67.04884167, -0.08994713, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.16, 28399578.10402948, 11833157.54334562, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 247.13884358, 0.00119462, 294.74429853, 0.0274172, 29.47442985, 0.08110844, -247.13884358, -0.00119462, -294.74429853, -0.0274172, -29.47442985, -0.08110844, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 272.35798201, 0.00119462, 324.82130771, 0.0274172, 32.48213077, 0.08110844, -272.35798201, -0.00119462, -324.82130771, -0.0274172, -32.48213077, -0.08110844, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.09, 28564195.98273878, 11901748.32614116, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 155.24627532, 0.00168013, 184.83111791, 0.044306, 18.48311179, 0.1189696, -155.24627532, -0.00168013, -184.83111791, -0.044306, -18.48311179, -0.1189696, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 155.24627532, 0.00168013, 184.83111791, 0.044306, 18.48311179, 0.1189696, -155.24627532, -0.00168013, -184.83111791, -0.044306, -18.48311179, -0.1189696, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 4.5, 13.5, 0.0)
    ops.node(121020, 4.5, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.1225, 29334359.91789567, 12222649.96578986, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 264.38305225, 0.00148277, 313.30321228, 0.03771957, 31.33032123, 0.10138388, -264.38305225, -0.00148277, -313.30321228, -0.03771957, -31.33032123, -0.10138388, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 246.45777703, 0.00148277, 292.06113091, 0.03771957, 29.20611309, 0.10138388, -246.45777703, -0.00148277, -292.06113091, -0.03771957, -29.20611309, -0.10138388, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.1225, 29985885.61885705, 12494119.0078571, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 251.81821355, 0.00142657, 299.48657694, 0.0398041, 29.94865769, 0.11471939, -251.81821355, -0.00142657, -299.48657694, -0.0398041, -29.94865769, -0.11471939, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 234.37462568, 0.00142657, 278.740975, 0.0398041, 27.8740975, 0.11471939, -234.37462568, -0.00142657, -278.740975, -0.0398041, -27.8740975, -0.11471939, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.16, 28869664.30177101, 12029026.79240459, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 328.8237647, 0.00123951, 393.37706726, 0.03455317, 39.33770673, 0.095644, -328.8237647, -0.00123951, -393.37706726, -0.03455317, -39.33770673, -0.095644, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 328.8237647, 0.00123951, 393.37706726, 0.03455317, 39.33770673, 0.095644, -328.8237647, -0.00123951, -393.37706726, -0.03455317, -39.33770673, -0.095644, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 16.5, 13.5, 0.0)
    ops.node(121023, 16.5, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.1225, 28946368.05670452, 12060986.69029355, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 262.94042593, 0.00143586, 311.51979142, 0.03748584, 31.15197914, 0.09872048, -262.94042593, -0.00143586, -311.51979142, -0.03748584, -31.15197914, -0.09872048, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 244.6023948, 0.00143586, 289.79373081, 0.03748584, 28.97937308, 0.09872048, -244.6023948, -0.00143586, -289.79373081, -0.03748584, -28.97937308, -0.09872048, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.09, 27886354.61364824, 11619314.42235343, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 153.07913724, 0.00171245, 182.16887598, 0.04402951, 18.2168876, 0.11398878, -153.07913724, -0.00171245, -182.16887598, -0.04402951, -18.2168876, -0.11398878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 153.07913724, 0.00171245, 182.16887598, 0.04402951, 18.2168876, 0.11398878, -153.07913724, -0.00171245, -182.16887598, -0.04402951, -18.2168876, -0.11398878, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.325)
    ops.node(122001, 0.0, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 29276942.8222922, 12198726.17595509, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 159.30768981, 0.00155505, 190.89169361, 0.05312965, 19.08916936, 0.14894365, -159.30768981, -0.00155505, -190.89169361, -0.05312965, -19.08916936, -0.14894365, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 173.18981194, 0.00155505, 207.52605574, 0.05312965, 20.75260557, 0.14894365, -173.18981194, -0.00155505, -207.52605574, -0.05312965, -20.75260557, -0.14894365, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.5, 0.0, 3.35)
    ops.node(122002, 4.5, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.16, 29983777.21754815, 12493240.50731173, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 258.71447951, 0.00114267, 310.10169756, 0.03531383, 31.01016976, 0.1063662, -258.71447951, -0.00114267, -310.10169756, -0.03531383, -31.01016976, -0.1063662, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 277.23045689, 0.00114267, 332.29541486, 0.03531383, 33.22954149, 0.1063662, -277.23045689, -0.00114267, -332.29541486, -0.03531383, -33.22954149, -0.1063662, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.5, 0.0, 3.35)
    ops.node(122005, 16.5, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.16, 28324076.02951979, 11801698.34563325, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 265.42962158, 0.00116457, 318.57636352, 0.03498556, 31.85763635, 0.09949793, -265.42962158, -0.00116457, -318.57636352, -0.03498556, -31.85763635, -0.09949793, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 286.14484438, 0.00116457, 343.43937734, 0.03498556, 34.34393773, 0.09949793, -286.14484438, -0.00116457, -343.43937734, -0.03498556, -34.34393773, -0.09949793, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 21.0, 0.0, 3.325)
    ops.node(122006, 21.0, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.09, 26719602.6483393, 11133167.77014138, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 156.12205387, 0.0016679, 187.08778459, 0.04955464, 18.70877846, 0.12884591, -156.12205387, -0.0016679, -187.08778459, -0.04955464, -18.70877846, -0.12884591, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 169.78273622, 0.0016679, 203.45796891, 0.04955464, 20.34579689, 0.12884591, -169.78273622, -0.0016679, -203.45796891, -0.04955464, -20.34579689, -0.12884591, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.35)
    ops.node(122007, 0.0, 4.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.16, 28313317.32499262, 11797215.55208026, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 218.93780053, 0.00107861, 262.76902302, 0.03048783, 26.2769023, 0.0948994, -218.93780053, -0.00107861, -262.76902302, -0.03048783, -26.2769023, -0.0948994, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 243.93809173, 0.00107861, 292.77435821, 0.03048783, 29.27743582, 0.0948994, -243.93809173, -0.00107861, -292.77435821, -0.03048783, -29.27743582, -0.0948994, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.5, 4.5, 3.35)
    ops.node(122008, 4.5, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.25, 29408319.40775915, 12253466.41989965, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 446.76166855, 0.00093006, 536.80951588, 0.03302504, 53.68095159, 0.09287557, -446.76166855, -0.00093006, -536.80951588, -0.03302504, -53.68095159, -0.09287557, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 446.76166855, 0.00093006, 536.80951588, 0.03302504, 53.68095159, 0.09287557, -446.76166855, -0.00093006, -536.80951588, -0.03302504, -53.68095159, -0.09287557, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.0, 4.5, 3.35)
    ops.node(122009, 9.0, 4.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.2025, 28869719.10746099, 12029049.62810875, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 494.29360037, 0.00106588, 593.65769554, 0.03757472, 59.36576955, 0.09948556, -494.29360037, -0.00106588, -593.65769554, -0.03757472, -59.36576955, -0.09948556, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 470.4918203, 0.00106588, 565.07122407, 0.03757472, 56.50712241, 0.09948556, -470.4918203, -0.00106588, -565.07122407, -0.03757472, -56.50712241, -0.09948556, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.0, 4.5, 3.35)
    ops.node(122010, 12.0, 4.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.2025, 30144443.78081202, 12560184.90867168, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 505.81214393, 0.00104752, 606.65227164, 0.03698804, 60.66522716, 0.10315757, -505.81214393, -0.00104752, -606.65227164, -0.03698804, -60.66522716, -0.10315757, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 481.2860302, 0.00104752, 577.23656309, 0.03698804, 57.72365631, 0.10315757, -481.2860302, -0.00104752, -577.23656309, -0.03698804, -57.72365631, -0.10315757, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 16.5, 4.5, 3.35)
    ops.node(122011, 16.5, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.25, 28061049.99688608, 11692104.1653692, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 448.11875006, 0.00096117, 539.03389357, 0.03276185, 53.90338936, 0.08833264, -448.11875006, -0.00096117, -539.03389357, -0.03276185, -53.90338936, -0.08833264, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 448.11875006, 0.00096117, 539.03389357, 0.03276185, 53.90338936, 0.08833264, -448.11875006, -0.00096117, -539.03389357, -0.03276185, -53.90338936, -0.08833264, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.35)
    ops.node(122012, 21.0, 4.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 30221821.11777773, 12592425.46574072, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 222.7534685, 0.00103908, 266.91063393, 0.03037849, 26.69106339, 0.1022404, -222.7534685, -0.00103908, -266.91063393, -0.03037849, -26.69106339, -0.1022404, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 248.50348526, 0.00103908, 297.76516267, 0.03037849, 29.77651627, 0.1022404, -248.50348526, -0.00103908, -297.76516267, -0.03037849, -29.77651627, -0.1022404, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.325)
    ops.node(122013, 0.0, 9.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.16, 29278846.50758622, 12199519.37816093, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 221.60021395, 0.00105235, 265.81200684, 0.0309302, 26.58120068, 0.09932457, -221.60021395, -0.00105235, -265.81200684, -0.0309302, -26.58120068, -0.09932457, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 247.46324106, 0.00105235, 296.83500549, 0.0309302, 29.68350055, 0.09932457, -247.46324106, -0.00105235, -296.83500549, -0.0309302, -29.68350055, -0.09932457, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.5, 9.0, 3.35)
    ops.node(122014, 4.5, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.25, 30381501.89240102, 12658959.12183376, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 391.73866721, 0.00090628, 470.0813857, 0.03213285, 47.00813857, 0.09479003, -391.73866721, -0.00090628, -470.0813857, -0.03213285, -47.00813857, -0.09479003, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 418.41787547, 0.00090628, 502.09609407, 0.03213285, 50.20960941, 0.09479003, -418.41787547, -0.00090628, -502.09609407, -0.03213285, -50.20960941, -0.09479003, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 9.0, 3.35)
    ops.node(122015, 9.0, 9.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.2025, 30403263.32896081, 12668026.38706701, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 459.40017815, 0.00101869, 550.72051684, 0.03650182, 55.07205168, 0.10325446, -459.40017815, -0.00101869, -550.72051684, -0.03650182, -55.07205168, -0.10325446, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 459.40017815, 0.00101869, 550.72051684, 0.03650182, 55.07205168, 0.10325446, -459.40017815, -0.00101869, -550.72051684, -0.03650182, -55.07205168, -0.10325446, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.0, 9.0, 3.35)
    ops.node(122016, 12.0, 9.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.2025, 28732234.16407426, 11971764.23503094, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 455.94224538, 0.00105108, 547.57941817, 0.03553988, 54.75794182, 0.09671656, -455.94224538, -0.00105108, -547.57941817, -0.03553988, -54.75794182, -0.09671656, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 455.94224538, 0.00105108, 547.57941817, 0.03553988, 54.75794182, 0.09671656, -455.94224538, -0.00105108, -547.57941817, -0.03553988, -54.75794182, -0.09671656, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 16.5, 9.0, 3.35)
    ops.node(122017, 16.5, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.25, 29083049.60271313, 12117937.3344638, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 391.97891897, 0.00091624, 471.16205002, 0.03248853, 47.116205, 0.09140591, -391.97891897, -0.00091624, -471.16205002, -0.03248853, -47.116205, -0.09140591, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 419.52040083, 0.00091624, 504.26714937, 0.03248853, 50.42671494, 0.09140591, -419.52040083, -0.00091624, -504.26714937, -0.03248853, -50.42671494, -0.09140591, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.325)
    ops.node(122018, 21.0, 9.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.16, 27547377.0063777, 11478073.75265738, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 217.74408326, 0.00108168, 261.37376053, 0.02969695, 26.13737605, 0.09080339, -217.74408326, -0.00108168, -261.37376053, -0.02969695, -26.13737605, -0.09080339, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 243.06044404, 0.00108168, 291.76279484, 0.02969695, 29.17627948, 0.09080339, -243.06044404, -0.00108168, -291.76279484, -0.02969695, -29.17627948, -0.09080339, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.325)
    ops.node(122019, 0.0, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.09, 28448725.93587481, 11853635.8066145, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 154.07434613, 0.00159615, 184.70217963, 0.05239357, 18.47021796, 0.14323044, -154.07434613, -0.00159615, -184.70217963, -0.05239357, -18.47021796, -0.14323044, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 166.93266391, 0.00159615, 200.11655185, 0.05239357, 20.01165518, 0.14323044, -166.93266391, -0.00159615, -200.11655185, -0.05239357, -20.01165518, -0.14323044, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 4.5, 13.5, 3.35)
    ops.node(122020, 4.5, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.1225, 28833605.38011491, 12014002.24171454, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 236.19358001, 0.00139307, 281.97093391, 0.0413868, 28.19709339, 0.11753606, -236.19358001, -0.00139307, -281.97093391, -0.0413868, -28.19709339, -0.11753606, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 219.69110128, 0.00139307, 262.27006254, 0.0413868, 26.22700625, 0.11753606, -219.69110128, -0.00139307, -262.27006254, -0.0413868, -26.22700625, -0.11753606, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.35)
    ops.node(122021, 9.0, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.1225, 28524119.93168663, 11885049.9715361, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 230.89177597, 0.0013383, 276.47415362, 0.04271424, 27.64741536, 0.12401266, -230.89177597, -0.0013383, -276.47415362, -0.04271424, -27.64741536, -0.12401266, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 213.47708597, 0.0013383, 255.6214764, 0.04271424, 25.56214764, 0.12401266, -213.47708597, -0.0013383, -255.6214764, -0.04271424, -25.56214764, -0.12401266, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.35)
    ops.node(122022, 12.0, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.16, 28475381.74435409, 11864742.39348087, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 291.96335131, 0.00115579, 351.21908564, 0.03746719, 35.12190856, 0.10730678, -291.96335131, -0.00115579, -351.21908564, -0.03746719, -35.12190856, -0.10730678, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 291.96335131, 0.00115579, 351.21908564, 0.03746719, 35.12190856, 0.10730678, -291.96335131, -0.00115579, -351.21908564, -0.03746719, -35.12190856, -0.10730678, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 16.5, 13.5, 3.35)
    ops.node(122023, 16.5, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.1225, 28538810.48410513, 11891171.0350438, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 233.55955903, 0.00134426, 278.82346045, 0.0412839, 27.88234604, 0.11565416, -233.55955903, -0.00134426, -278.82346045, -0.0412839, -27.88234604, -0.11565416, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 216.88107707, 0.00134426, 258.91268447, 0.0412839, 25.89126845, 0.11565416, -216.88107707, -0.00134426, -258.91268447, -0.0412839, -25.89126845, -0.11565416, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.325)
    ops.node(122024, 21.0, 13.5, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.09, 28523454.06782252, 11884772.52825938, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 160.87145522, 0.00154473, 192.84576492, 0.05209756, 19.28457649, 0.14339807, -160.87145522, -0.00154473, -192.84576492, -0.05209756, -19.28457649, -0.14339807, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 175.52133556, 0.00154473, 210.40740988, 0.05209756, 21.04074099, 0.14339807, -175.52133556, -0.00154473, -210.40740988, -0.05209756, -21.04074099, -0.14339807, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.125)
    ops.node(123001, 0.0, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.09, 28691328.24760136, 11954720.10316724, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 141.82814885, 0.00154991, 171.14981311, 0.05831462, 17.11498131, 0.15831462, -141.82814885, -0.00154991, -171.14981311, -0.05831462, -17.11498131, -0.15831462, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 154.13399482, 0.00154991, 185.99977946, 0.05831462, 18.59997795, 0.15831462, -154.13399482, -0.00154991, -185.99977946, -0.05831462, -18.59997795, -0.15831462, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.5, 0.0, 6.15)
    ops.node(123002, 4.5, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.16, 28915980.09156365, 12048325.03815152, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 275.62973768, 0.00112183, 332.66990899, 0.04012924, 33.2669909, 0.11994878, -275.62973768, -0.00112183, -332.66990899, -0.04012924, -33.2669909, -0.11994878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 275.62973768, 0.00112183, 332.66990899, 0.04012924, 33.2669909, 0.11994878, -275.62973768, -0.00112183, -332.66990899, -0.04012924, -33.2669909, -0.11994878, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.5, 0.0, 6.15)
    ops.node(123005, 16.5, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.16, 27723062.9021742, 11551276.20923925, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 286.09755766, 0.00116399, 345.76192189, 0.03902826, 34.57619219, 0.11479513, -286.09755766, -0.00116399, -345.76192189, -0.03902826, -34.57619219, -0.11479513, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 286.09755766, 0.00116399, 345.76192189, 0.03902826, 34.57619219, 0.11479513, -286.09755766, -0.00116399, -345.76192189, -0.03902826, -34.57619219, -0.11479513, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 21.0, 0.0, 6.125)
    ops.node(123006, 21.0, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.09, 29776046.75268529, 12406686.1469522, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 148.21161433, 0.0014741, 178.57229111, 0.05748283, 17.85722911, 0.15748283, -148.21161433, -0.0014741, -178.57229111, -0.05748283, -17.85722911, -0.15748283, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 161.98153201, 0.0014741, 195.16293254, 0.05748283, 19.51629325, 0.15748283, -161.98153201, -0.0014741, -195.16293254, -0.05748283, -19.51629325, -0.15748283, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.125)
    ops.node(123007, 0.0, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.16, 28198780.87455999, 11749492.03106667, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 192.62175334, 0.00102114, 232.68652942, 0.03331652, 23.26865294, 0.11076315, -192.62175334, -0.00102114, -232.68652942, -0.03331652, -23.26865294, -0.11076315, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 218.02717781, 0.00102114, 263.37620982, 0.03331652, 26.33762098, 0.11076315, -218.02717781, -0.00102114, -263.37620982, -0.03331652, -26.33762098, -0.11076315, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.5, 4.5, 6.15)
    ops.node(123008, 4.5, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.25, 28363421.26852272, 11818092.1952178, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 340.2837335, 0.00091831, 411.37663481, 0.03469766, 41.13766348, 0.10071976, -340.2837335, -0.00091831, -411.37663481, -0.03469766, -41.13766348, -0.10071976, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 365.54475937, 0.00091831, 441.91525535, 0.03469766, 44.19152553, 0.10071976, -365.54475937, -0.00091831, -441.91525535, -0.03469766, -44.19152553, -0.10071976, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.125)
    ops.node(123009, 9.0, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.2025, 28894102.54073643, 12039209.39197351, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 396.94831492, 0.00103229, 479.25255161, 0.03802022, 47.92525516, 0.11055787, -396.94831492, -0.00103229, -479.25255161, -0.03802022, -47.92525516, -0.11055787, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 372.94354484, 0.00103229, 450.27057366, 0.03802022, 45.02705737, 0.11055787, -372.94354484, -0.00103229, -450.27057366, -0.03802022, -45.02705737, -0.11055787, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.125)
    ops.node(123010, 12.0, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.2025, 27850484.34329462, 11604368.47637276, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 388.34083603, 0.00104414, 469.43412365, 0.03793682, 46.94341236, 0.10734948, -388.34083603, -0.00104414, -469.43412365, -0.03793682, -46.94341236, -0.10734948, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 365.01576091, 0.00104414, 441.23830908, 0.03793682, 44.12383091, 0.10734948, -365.01576091, -0.00104414, -441.23830908, -0.03793682, -44.12383091, -0.10734948, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 16.5, 4.5, 6.15)
    ops.node(123011, 16.5, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.25, 26970645.92373956, 11237769.13489148, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 343.1318456, 0.00093575, 415.36439617, 0.03441661, 41.53643962, 0.09645731, -343.1318456, -0.00093575, -415.36439617, -0.03441661, -41.53643962, -0.09645731, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 369.69215964, 0.00093575, 447.51591153, 0.03441661, 44.75159115, 0.09645731, -369.69215964, -0.00093575, -447.51591153, -0.03441661, -44.75159115, -0.09645731, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.125)
    ops.node(123012, 21.0, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.16, 28354397.05412301, 11814332.10588459, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 191.53239346, 0.00103023, 231.3311964, 0.03294196, 23.13311964, 0.11091942, -191.53239346, -0.00103023, -231.3311964, -0.03294196, -23.13311964, -0.11091942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 216.105368, 0.00103023, 261.01022614, 0.03294196, 26.10102261, 0.11091942, -216.105368, -0.00103023, -261.01022614, -0.03294196, -26.10102261, -0.11091942, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.125)
    ops.node(123013, 0.0, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.16, 29179792.43480535, 12158246.84783556, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 191.24619851, 0.00102782, 230.73702238, 0.03306674, 23.07370224, 0.11371314, -191.24619851, -0.00102782, -230.73702238, -0.03306674, -23.07370224, -0.11371314, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 215.02183761, 0.00102782, 259.42214247, 0.03306674, 25.94221425, 0.11371314, -215.02183761, -0.00102782, -259.42214247, -0.03306674, -25.94221425, -0.11371314, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.5, 9.0, 6.15)
    ops.node(123014, 4.5, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.25, 29511899.12359496, 12296624.63483123, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 343.96290837, 0.00090311, 415.11958155, 0.03463567, 41.51195815, 0.10350222, -343.96290837, -0.00090311, -415.11958155, -0.03463567, -41.51195815, -0.10350222, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 369.52057227, 0.00090311, 445.9644386, 0.03463567, 44.59644386, 0.10350222, -369.52057227, -0.00090311, -445.9644386, -0.03463567, -44.59644386, -0.10350222, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.125)
    ops.node(123015, 9.0, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.2025, 28799120.42305537, 11999633.50960641, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 284.91148671, 0.0009763, 343.95273555, 0.03615326, 34.39527356, 0.10793519, -284.91148671, -0.0009763, -343.95273555, -0.03615326, -34.39527356, -0.10793519, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 307.13096845, 0.0009763, 370.77668574, 0.03615326, 37.07766857, 0.10793519, -307.13096845, -0.0009763, -370.77668574, -0.03615326, -37.07766857, -0.10793519, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.125)
    ops.node(123016, 12.0, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.2025, 28689745.98277812, 11954060.82615755, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 290.81665532, 0.00100291, 351.1316996, 0.03629353, 35.11316996, 0.10775729, -290.81665532, -0.00100291, -351.1316996, -0.03629353, -35.11316996, -0.10775729, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 313.73382271, 0.00100291, 378.80186149, 0.03629353, 37.88018615, 0.10775729, -313.73382271, -0.00100291, -378.80186149, -0.03629353, -37.88018615, -0.10775729, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 16.5, 9.0, 6.15)
    ops.node(123017, 16.5, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.25, 29413992.17863301, 12255830.07443042, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 346.51751548, 0.00089046, 418.27174598, 0.03424967, 41.8271746, 0.10288788, -346.51751548, -0.00089046, -418.27174598, -0.03424967, -41.8271746, -0.10288788, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 373.08122387, 0.00089046, 450.33606652, 0.03424967, 45.03360665, 0.10288788, -373.08122387, -0.00089046, -450.33606652, -0.03424967, -45.03360665, -0.10288788, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.125)
    ops.node(123018, 21.0, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.16, 28682349.43846076, 11950978.93269199, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 191.29816724, 0.00101765, 230.95747938, 0.03347684, 23.09574794, 0.1125438, -191.29816724, -0.00101765, -230.95747938, -0.03347684, -23.09574794, -0.1125438, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 215.85377512, 0.00101765, 260.6038758, 0.03347684, 26.06038758, 0.1125438, -215.85377512, -0.00101765, -260.6038758, -0.03347684, -26.06038758, -0.1125438, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.125)
    ops.node(123019, 0.0, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.09, 29786819.70148348, 12411174.87561812, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 144.12971834, 0.00150126, 173.65109918, 0.05850076, 17.36510992, 0.15850076, -144.12971834, -0.00150126, -173.65109918, -0.05850076, -17.36510992, -0.15850076, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 156.81845541, 0.00150126, 188.93880781, 0.05850076, 18.89388078, 0.15850076, -156.81845541, -0.00150126, -188.93880781, -0.05850076, -18.89388078, -0.15850076, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 4.5, 13.5, 6.15)
    ops.node(123020, 4.5, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1225, 29619982.48268694, 12341659.36778622, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 211.41229192, 0.00130592, 254.10489474, 0.04698375, 25.41048947, 0.14646151, -211.41229192, -0.00130592, -254.10489474, -0.04698375, -25.41048947, -0.14646151, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 195.73437157, 0.00130592, 235.26097482, 0.04698375, 23.52609748, 0.14646151, -195.73437157, -0.00130592, -235.26097482, -0.04698375, -23.52609748, -0.14646151, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.125)
    ops.node(123021, 9.0, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.1225, 29462749.74273761, 12276145.72614067, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 245.25442632, 0.0012826, 295.36213897, 0.05029697, 29.5362139, 0.15029697, -245.25442632, -0.0012826, -295.36213897, -0.05029697, -29.5362139, -0.15029697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 211.76247897, 0.0012826, 255.02748179, 0.05029697, 25.50274818, 0.15029697, -211.76247897, -0.0012826, -255.02748179, -0.05029697, -25.50274818, -0.15029697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.125)
    ops.node(123022, 12.0, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.16, 28200443.98773813, 11750184.99489089, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 268.80999683, 0.00113275, 325.23046098, 0.04038377, 32.5230461, 0.12154045, -268.80999683, -0.00113275, -325.23046098, -0.04038377, -32.5230461, -0.12154045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 268.80999683, 0.00113275, 325.23046098, 0.04038377, 32.5230461, 0.12154045, -268.80999683, -0.00113275, -325.23046098, -0.04038377, -32.5230461, -0.12154045, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 16.5, 13.5, 6.15)
    ops.node(123023, 16.5, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 28979479.29863358, 12074783.04109732, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 215.41364677, 0.00128447, 259.1069115, 0.04651615, 25.91069115, 0.14295014, -215.41364677, -0.00128447, -259.1069115, -0.04651615, -25.91069115, -0.14295014, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 198.52758183, 0.00128447, 238.79577431, 0.04651615, 23.87957743, 0.14295014, -198.52758183, -0.00128447, -238.79577431, -0.04651615, -23.87957743, -0.14295014, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.125)
    ops.node(123024, 21.0, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.09, 30123186.53883194, 12551327.72451331, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 148.3547475, 0.00145188, 178.63667702, 0.05807243, 17.8636677, 0.15807243, -148.3547475, -0.00145188, -178.63667702, -0.05807243, -17.8636677, -0.15807243, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 162.18892946, 0.00145188, 195.29466968, 0.05807243, 19.52946697, 0.15807243, -162.18892946, -0.00145188, -195.29466968, -0.05807243, -19.52946697, -0.15807243, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.9)
    ops.node(124001, 0.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.09, 28065363.77186851, 11693901.57161188, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 110.44546672, 0.00156681, 134.4686636, 0.06183372, 13.44686636, 0.16183372, -110.44546672, -0.00156681, -134.4686636, -0.06183372, -13.44686636, -0.16183372, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 110.44546672, 0.00156681, 134.4686636, 0.06183372, 13.44686636, 0.16183372, -110.44546672, -0.00156681, -134.4686636, -0.06183372, -13.44686636, -0.16183372, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.5, 0.0, 8.9)
    ops.node(124002, 4.5, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.16, 28856984.96102967, 12023743.73376236, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 220.50124985, 0.00105277, 267.95263023, 0.04258192, 26.79526302, 0.13991704, -220.50124985, -0.00105277, -267.95263023, -0.04258192, -26.79526302, -0.13991704, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 201.86686836, 0.00105277, 245.30817114, 0.04258192, 24.53081711, 0.13991704, -201.86686836, -0.00105277, -245.30817114, -0.04258192, -24.53081711, -0.13991704, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.5, 0.0, 8.9)
    ops.node(124005, 16.5, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.16, 29443011.75311004, 12267921.56379585, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 224.88238527, 0.00104265, 272.92298794, 0.04205409, 27.29229879, 0.14032245, -224.88238527, -0.00104265, -272.92298794, -0.04205409, -27.29229879, -0.14032245, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 205.6083722, 0.00104265, 249.531555, 0.04205409, 24.9531555, 0.14032245, -205.6083722, -0.00104265, -249.531555, -0.04205409, -24.9531555, -0.14032245, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 21.0, 0.0, 8.9)
    ops.node(124006, 21.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.09, 30048237.24145513, 12520098.85060631, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 113.53556156, 0.00144407, 137.62560192, 0.06073489, 13.76256019, 0.16073489, -113.53556156, -0.00144407, -137.62560192, -0.06073489, -13.76256019, -0.16073489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 113.53556156, 0.00144407, 137.62560192, 0.06073489, 13.76256019, 0.16073489, -113.53556156, -0.00144407, -137.62560192, -0.06073489, -13.76256019, -0.16073489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 8.9)
    ops.node(124007, 0.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.16, 28586722.73181906, 11911134.47159127, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 193.42595952, 0.00099615, 235.18294865, 0.03832701, 23.51829487, 0.13520664, -193.42595952, -0.00099615, -235.18294865, -0.03832701, -23.51829487, -0.13520664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 243.60422967, 0.00099615, 296.19375383, 0.03832701, 29.61937538, 0.13520664, -243.60422967, -0.00099615, -296.19375383, -0.03832701, -29.61937538, -0.13520664, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.5, 4.5, 8.9)
    ops.node(124008, 4.5, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.25, 26973401.73501252, 11238917.38958855, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 283.32326233, 0.00091467, 345.38443919, 0.03805346, 34.53844392, 0.11456815, -283.32326233, -0.00091467, -345.38443919, -0.03805346, -34.53844392, -0.11456815, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 307.21100297, 0.00091467, 374.50472333, 0.03805346, 37.45047233, 0.11456815, -307.21100297, -0.00091467, -374.50472333, -0.03805346, -37.45047233, -0.11456815, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.0, 4.5, 8.9)
    ops.node(124009, 9.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.2025, 29795198.72432537, 12414666.13513557, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 299.41403714, 0.00095796, 362.971382, 0.0406133, 36.2971382, 0.12891493, -299.41403714, -0.00095796, -362.971382, -0.0406133, -36.2971382, -0.12891493, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 299.41403714, 0.00095796, 362.971382, 0.0406133, 36.2971382, 0.12891493, -299.41403714, -0.00095796, -362.971382, -0.0406133, -36.2971382, -0.12891493, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.0, 4.5, 8.9)
    ops.node(124010, 12.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.2025, 29650940.71432991, 12354558.6309708, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 294.52244913, 0.00094425, 357.16245789, 0.04099226, 35.71624579, 0.12909121, -294.52244913, -0.00094425, -357.16245789, -0.04099226, -35.71624579, -0.12909121, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 294.52244913, 0.00094425, 357.16245789, 0.04099226, 35.71624579, 0.12909121, -294.52244913, -0.00094425, -357.16245789, -0.04099226, -35.71624579, -0.12909121, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 16.5, 4.5, 8.9)
    ops.node(124011, 16.5, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.25, 29400394.6115024, 12250164.42145933, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 291.53177941, 0.00085829, 353.76917344, 0.03701079, 35.37691734, 0.11729942, -291.53177941, -0.00085829, -353.76917344, -0.03701079, -35.37691734, -0.11729942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 317.02794956, 0.00085829, 384.70837004, 0.03701079, 38.470837, 0.11729942, -317.02794956, -0.00085829, -384.70837004, -0.03701079, -38.470837, -0.11729942, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 8.9)
    ops.node(124012, 21.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.16, 28512480.08505565, 11880200.03543985, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 190.41681402, 0.0010002, 231.55903474, 0.03867764, 23.15590347, 0.13542924, -190.41681402, -0.0010002, -231.55903474, -0.03867764, -23.15590347, -0.13542924, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 238.50017113, 0.0010002, 290.03147489, 0.03867764, 29.00314749, 0.13542924, -238.50017113, -0.0010002, -290.03147489, -0.03867764, -29.00314749, -0.13542924, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.0, 8.9)
    ops.node(124013, 0.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.16, 30400488.43428635, 12666870.18095265, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 220.81892975, 0.00098675, 267.36586022, 0.03851565, 26.73658602, 0.13816243, -220.81892975, -0.00098675, -267.36586022, -0.03851565, -26.73658602, -0.13816243, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 257.35584271, 0.00098675, 311.60447315, 0.03851565, 31.16044732, 0.13816243, -257.35584271, -0.00098675, -311.60447315, -0.03851565, -31.16044732, -0.13816243, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.5, 9.0, 8.9)
    ops.node(124014, 4.5, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.25, 28918156.14845604, 12049231.72852335, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 278.32396775, 0.00087538, 338.09808945, 0.03800195, 33.80980895, 0.11763472, -278.32396775, -0.00087538, -338.09808945, -0.03800195, -33.80980895, -0.11763472, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 300.8678329, 0.00087538, 365.48357765, 0.03800195, 36.54835777, 0.11763472, -300.8678329, -0.00087538, -365.48357765, -0.03800195, -36.54835777, -0.11763472, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 9.0, 8.9)
    ops.node(124015, 9.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.2025, 29755079.90233963, 12397949.95930818, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 295.20343963, 0.00095563, 357.80407796, 0.0401886, 35.7804078, 0.12772505, -295.20343963, -0.00095563, -357.80407796, -0.0401886, -35.7804078, -0.12772505, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 295.20343963, 0.00095563, 357.80407796, 0.0401886, 35.7804078, 0.12772505, -295.20343963, -0.00095563, -357.80407796, -0.0401886, -35.7804078, -0.12772505, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.0, 9.0, 8.9)
    ops.node(124016, 12.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.2025, 27717531.24046704, 11548971.3501946, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 302.51189452, 0.0009851, 368.16691831, 0.04048254, 36.81669183, 0.12459464, -302.51189452, -0.0009851, -368.16691831, -0.04048254, -36.81669183, -0.12459464, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 302.51189452, 0.0009851, 368.16691831, 0.04048254, 36.81669183, 0.12459464, -302.51189452, -0.0009851, -368.16691831, -0.04048254, -36.81669183, -0.12459464, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 16.5, 9.0, 8.9)
    ops.node(124017, 16.5, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.25, 29294531.08320606, 12206054.61800253, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 290.14900046, 0.00088226, 352.17486048, 0.03760133, 35.21748605, 0.11774952, -290.14900046, -0.00088226, -352.17486048, -0.03760133, -35.21748605, -0.11774952, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 314.69079615, 0.00088226, 381.96301573, 0.03760133, 38.19630157, 0.11774952, -314.69079615, -0.00088226, -381.96301573, -0.03760133, -38.19630157, -0.11774952, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 21.0, 9.0, 8.9)
    ops.node(124018, 21.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.16, 28276579.87146988, 11781908.27977912, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 221.71024499, 0.00102712, 269.73979952, 0.03966896, 26.97397995, 0.13600516, -221.71024499, -0.00102712, -269.73979952, -0.03966896, -26.97397995, -0.13600516, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 259.38444163, 0.00102712, 315.57543625, 0.03966896, 31.55754363, 0.13600516, -259.38444163, -0.00102712, -315.57543625, -0.03966896, -31.55754363, -0.13600516, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 13.5, 8.9)
    ops.node(124019, 0.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.09, 29059762.37737821, 12108234.32390759, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 110.0487414, 0.00152953, 133.71065209, 0.06161314, 13.37106521, 0.16161314, -110.0487414, -0.00152953, -133.71065209, -0.06161314, -13.37106521, -0.16161314, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 110.0487414, 0.00152953, 133.71065209, 0.06161314, 13.37106521, 0.16161314, -110.0487414, -0.00152953, -133.71065209, -0.06161314, -13.37106521, -0.16161314, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 4.5, 13.5, 8.9)
    ops.node(124020, 4.5, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1225, 29008850.08368358, 12087020.86820149, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 186.32968654, 0.00120374, 226.04015356, 0.05262674, 22.60401536, 0.15262674, -186.32968654, -0.00120374, -226.04015356, -0.05262674, -22.60401536, -0.15262674, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 170.25928139, 0.00120374, 206.54483365, 0.05262674, 20.65448336, 0.15262674, -170.25928139, -0.00120374, -206.54483365, -0.05262674, -20.65448336, -0.15262674, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 8.9)
    ops.node(124021, 9.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.1225, 29430899.32516948, 12262874.71882062, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 225.29169382, 0.00125484, 273.26133284, 0.05606656, 27.32613328, 0.15606656, -225.29169382, -0.00125484, -273.26133284, -0.05606656, -27.32613328, -0.15606656, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 192.32147085, 0.00125484, 233.2710122, 0.05606656, 23.32710122, 0.15606656, -192.32147085, -0.00125484, -233.2710122, -0.05606656, -23.32710122, -0.15606656, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 8.9)
    ops.node(124022, 12.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.16, 30088173.06093352, 12536738.77538897, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 221.96033087, 0.00105005, 269.09750307, 0.04245802, 26.90975031, 0.14245802, -221.96033087, -0.00105005, -269.09750307, -0.04245802, -26.90975031, -0.14245802, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 203.20546157, 0.00105005, 246.35970809, 0.04245802, 24.63597081, 0.14245802, -203.20546157, -0.00105005, -246.35970809, -0.04245802, -24.63597081, -0.14245802, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 16.5, 13.5, 8.9)
    ops.node(124023, 16.5, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 29910122.49124818, 12462551.03802007, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 183.94939199, 0.00118377, 222.71991736, 0.05229911, 22.27199174, 0.15229911, -183.94939199, -0.00118377, -222.71991736, -0.05229911, -22.27199174, -0.15229911, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 168.43562195, 0.00118377, 203.93635116, 0.05229911, 20.39363512, 0.15229911, -168.43562195, -0.00118377, -203.93635116, -0.05229911, -20.39363512, -0.15229911, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 21.0, 13.5, 8.9)
    ops.node(124024, 21.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.09, 28340378.52256946, 11808491.05107061, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 114.064849, 0.00141841, 138.8005405, 0.06201714, 13.88005405, 0.16201714, -114.064849, -0.00141841, -138.8005405, -0.06201714, -13.88005405, -0.16201714, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 114.064849, 0.00141841, 138.8005405, 0.06201714, 13.88005405, 0.16201714, -114.064849, -0.00141841, -138.8005405, -0.06201714, -13.88005405, -0.16201714, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(124025, 9.0, 0.0, 1.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.16, 28386603.27091398, 11827751.36288082, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 301.62443619, 0.00100324, 360.84263062, 0.04655359, 36.08426306, 0.13159547, -301.62443619, -0.00100324, -360.84263062, -0.04655359, -36.08426306, -0.13159547, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 280.45461923, 0.00100324, 335.51652462, 0.04655359, 33.55165246, 0.13159547, -280.45461923, -0.00100324, -335.51652462, -0.04655359, -33.55165246, -0.13159547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.725)
    ops.node(121003, 9.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.16, 27329416.16481504, 11387256.7353396, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 318.74543517, 0.00102371, 381.82853229, 0.03435391, 38.18285323, 0.09094777, -318.74543517, -0.00102371, -381.82853229, -0.03435391, -38.18285323, -0.09094777, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 318.74543517, 0.00102371, 381.82853229, 0.03435391, 38.18285323, 0.09094777, -318.74543517, -0.00102371, -381.82853229, -0.03435391, -38.18285323, -0.09094777, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.0, 0.0, 0.0)
    ops.node(124026, 12.0, 0.0, 1.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.16, 29187082.31193115, 12161284.29663798, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 303.82860418, 0.00097914, 363.40327804, 0.04691328, 36.3403278, 0.13699776, -303.82860418, -0.00097914, -363.40327804, -0.04691328, -36.3403278, -0.13699776, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 282.3861936, 0.00097914, 337.75644233, 0.04691328, 33.77564423, 0.13699776, -282.3861936, -0.00097914, -337.75644233, -0.04691328, -33.77564423, -0.13699776, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.725)
    ops.node(121004, 12.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.16, 28657095.79237412, 11940456.58015588, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 318.12411211, 0.0009967, 381.1045896, 0.03468692, 38.11045896, 0.09728538, -318.12411211, -0.0009967, -381.1045896, -0.03468692, -38.11045896, -0.09728538, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 318.12411211, 0.0009967, 381.1045896, 0.03468692, 38.11045896, 0.09728538, -318.12411211, -0.0009967, -381.1045896, -0.03468692, -38.11045896, -0.09728538, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.35)
    ops.node(124027, 9.0, 0.0, 4.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.16, 28715545.48534923, 11964810.61889551, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 296.83275993, 0.00095176, 356.99102311, 0.06389646, 35.69910231, 0.16389646, -296.83275993, -0.00095176, -356.99102311, -0.06389646, -35.69910231, -0.16389646, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 296.83275993, 0.00095176, 356.99102311, 0.06389646, 35.69910231, 0.16389646, -296.83275993, -0.00095176, -356.99102311, -0.06389646, -35.69910231, -0.16389646, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.75)
    ops.node(122003, 9.0, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.16, 29505996.50175001, 12294165.20906251, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 268.19501439, 0.00093417, 322.71867434, 0.06374094, 32.27186743, 0.16374094, -268.19501439, -0.00093417, -322.71867434, -0.06374094, -32.27186743, -0.16374094, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 248.37624318, 0.00093417, 298.8707755, 0.06374094, 29.88707755, 0.16374094, -248.37624318, -0.00093417, -298.8707755, -0.06374094, -29.88707755, -0.16374094, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.35)
    ops.node(124028, 12.0, 0.0, 4.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.16, 28576250.54640857, 11906771.06100357, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 296.3495736, 0.00095154, 356.44991905, 0.06418031, 35.64499191, 0.16418031, -296.3495736, -0.00095154, -356.44991905, -0.06418031, -35.64499191, -0.16418031, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 296.3495736, 0.00095154, 356.44991905, 0.06418031, 35.64499191, 0.16418031, -296.3495736, -0.00095154, -356.44991905, -0.06418031, -35.64499191, -0.16418031, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.75)
    ops.node(122004, 12.0, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.16, 29735496.10630044, 12389790.04429185, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 265.40643771, 0.00092756, 319.25928953, 0.06411818, 31.92592895, 0.16411818, -265.40643771, -0.00092756, -319.25928953, -0.06411818, -31.92592895, -0.16411818, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 246.09555675, 0.00092756, 296.03009362, 0.06411818, 29.60300936, 0.16411818, -246.09555675, -0.00092756, -296.03009362, -0.06411818, -29.60300936, -0.16411818, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.125)
    ops.node(124029, 9.0, 0.0, 7.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.16, 28898462.86144735, 12041026.19226973, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 291.62160113, 0.00094376, 352.50910614, 0.04705263, 35.25091061, 0.14530427, -291.62160113, -0.00094376, -352.50910614, -0.04705263, -35.25091061, -0.14530427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 252.72559737, 0.00094376, 305.4920283, 0.04705263, 30.54920283, 0.14530427, -252.72559737, -0.00094376, -305.4920283, -0.04705263, -30.54920283, -0.14530427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.475)
    ops.node(123003, 9.0, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.16, 28211120.30226747, 11754633.45927811, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 196.76328623, 0.00089939, 238.46822511, 0.03929064, 23.84682251, 0.12474913, -196.76328623, -0.00089939, -238.46822511, -0.03929064, -23.84682251, -0.12474913, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 196.76328623, 0.00089939, 238.46822511, 0.03929064, 23.84682251, 0.12474913, -196.76328623, -0.00089939, -238.46822511, -0.03929064, -23.84682251, -0.12474913, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.125)
    ops.node(124030, 12.0, 0.0, 7.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.16, 29228268.39425199, 12178445.16427167, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 285.84113108, 0.00094143, 345.3396796, 0.04774658, 34.53396796, 0.14710398, -285.84113108, -0.00094143, -345.3396796, -0.04774658, -34.53396796, -0.14710398, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 248.87530852, 0.00094143, 300.67932835, 0.04774658, 30.06793283, 0.14710398, -248.87530852, -0.00094143, -300.67932835, -0.04774658, -30.06793283, -0.14710398, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.475)
    ops.node(123004, 12.0, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.16, 27894563.40986128, 11622734.75410887, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 191.01494786, 0.00089592, 231.60359895, 0.03921044, 23.1603599, 0.12376524, -191.01494786, -0.00089592, -231.60359895, -0.03921044, -23.1603599, -0.12376524, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 191.01494786, 0.00089592, 231.60359895, 0.03921044, 23.1603599, 0.12376524, -191.01494786, -0.00089592, -231.60359895, -0.03921044, -23.1603599, -0.12376524, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 8.9)
    ops.node(124031, 9.0, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.16, 29180137.97929075, 12158390.82470448, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 172.59269772, 0.00087782, 209.7215663, 0.04089133, 20.97215663, 0.14063662, -172.59269772, -0.00087782, -209.7215663, -0.04089133, -20.97215663, -0.14063662, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 172.59269772, 0.00087782, 209.7215663, 0.04089133, 20.97215663, 0.14063662, -172.59269772, -0.00087782, -209.7215663, -0.04089133, -20.97215663, -0.14063662, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.16, 28249596.73326936, 11770665.3055289, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 216.08612155, 0.00088442, 263.52678261, 0.04469717, 26.35267826, 0.14469717, -216.08612155, -0.00088442, -263.52678261, -0.04469717, -26.35267826, -0.14469717, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 196.4663405, 0.00088442, 239.59957369, 0.04469717, 23.95995737, 0.14469717, -196.4663405, -0.00088442, -239.59957369, -0.04469717, -23.95995737, -0.14469717, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 8.9)
    ops.node(124032, 12.0, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.16, 28884505.83171959, 12035210.7632165, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 171.80617547, 0.00086748, 208.90467179, 0.04137599, 20.89046718, 0.14069943, -171.80617547, -0.00086748, -208.90467179, -0.04137599, -20.89046718, -0.14069943, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 171.80617547, 0.00086748, 208.90467179, 0.04137599, 20.89046718, 0.14069943, -171.80617547, -0.00086748, -208.90467179, -0.04137599, -20.89046718, -0.14069943, 1.0, 1.0, 0.0, 0.0, 0.0)
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
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.16, 28326437.18227691, 11802682.15928205, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 212.56220693, 0.00089658, 259.18496167, 0.04444504, 25.91849617, 0.14444504, -212.56220693, -0.00089658, -259.18496167, -0.04444504, -25.91849617, -0.14444504, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 193.81736736, 0.00089658, 236.3286854, 0.04444504, 23.63286854, 0.14444504, -193.81736736, -0.00089658, -236.3286854, -0.04444504, -23.63286854, -0.14444504, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
