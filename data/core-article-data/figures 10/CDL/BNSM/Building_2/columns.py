import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 26205772.19626042, 10919071.74844184, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 76.38839148, 0.00085396, 90.75574494, 0.01493785, 9.07557449, 0.03606238, -76.38839148, -0.00085396, -90.75574494, -0.01493785, -9.07557449, -0.03606238, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 76.38839148, 0.00085396, 90.75574494, 0.01493785, 9.07557449, 0.03606238, -76.38839148, -0.00085396, -90.75574494, -0.01493785, -9.07557449, -0.03606238, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 102.21378555, 0.01707912, 102.21378555, 0.05123737, 71.54964989, -1232.90366742, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 25.55344639, 9.673e-05, 76.66033916, 0.00029019, 255.53446388, 0.00096731, -25.55344639, -9.673e-05, -76.66033916, -0.00029019, -255.53446388, -0.00096731, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 102.21378555, 0.01707912, 102.21378555, 0.05123737, 71.54964989, -1232.90366742, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 25.55344639, 9.673e-05, 76.66033916, 0.00029019, 255.53446388, 0.00096731, -25.55344639, -9.673e-05, -76.66033916, -0.00029019, -255.53446388, -0.00096731, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.5, 0.0, 0.0)
    ops.node(121002, 4.5, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.16, 28042426.02505859, 11684344.17710775, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 157.07369614, 0.00065378, 187.42559232, 0.01456431, 18.74255923, 0.03664874, -157.07369614, -0.00065378, -187.42559232, -0.01456431, -18.74255923, -0.03664874, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 178.22255388, 0.00065378, 212.66111733, 0.01456431, 21.26611173, 0.03664874, -178.22255388, -0.00065378, -212.66111733, -0.01456431, -21.26611173, -0.03664874, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 172.57322839, 0.01307562, 172.57322839, 0.03922686, 120.80125988, -1812.93437006, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 43.1433071, 8.585e-05, 129.4299213, 0.00025755, 431.43307099, 0.00085848, -43.1433071, -8.585e-05, -129.4299213, -0.00025755, -431.43307099, -0.00085848, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 172.57322839, 0.01307562, 172.57322839, 0.03922686, 120.80125988, -1812.93437006, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 43.1433071, 8.585e-05, 129.4299213, 0.00025755, 431.43307099, 0.00085848, -43.1433071, -8.585e-05, -129.4299213, -0.00025755, -431.43307099, -0.00085848, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.5, 0.0, 0.0)
    ops.node(121005, 16.5, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.16, 26472866.54226427, 11030361.05927678, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 155.88958001, 0.00066853, 185.70496904, 0.01366107, 18.5704969, 0.0324872, -155.88958001, -0.00066853, -185.70496904, -0.01366107, -18.5704969, -0.0324872, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 176.88102741, 0.00066853, 210.71123365, 0.01366107, 21.07112337, 0.0324872, -176.88102741, -0.00066853, -210.71123365, -0.01366107, -21.07112337, -0.0324872, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 164.56677476, 0.01337051, 164.56677476, 0.04011153, 115.19674233, -1815.07261283, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 41.14169369, 8.672e-05, 123.42508107, 0.00026016, 411.41693689, 0.00086719, -41.14169369, -8.672e-05, -123.42508107, -0.00026016, -411.41693689, -0.00086719, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 164.56677476, 0.01337051, 164.56677476, 0.04011153, 115.19674233, -1815.07261283, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 41.14169369, 8.672e-05, 123.42508107, 0.00026016, 411.41693689, 0.00086719, -41.14169369, -8.672e-05, -123.42508107, -0.00026016, -411.41693689, -0.00086719, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 21.0, 0.0, 0.0)
    ops.node(121006, 21.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.09, 26165474.20814762, 10902280.92006151, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 76.56323294, 0.00082528, 90.955474, 0.01479955, 9.0955474, 0.03581456, -76.56323294, -0.00082528, -90.955474, -0.01479955, -9.0955474, -0.03581456, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 76.56323294, 0.00082528, 90.955474, 0.01479955, 9.0955474, 0.03581456, -76.56323294, -0.00082528, -90.955474, -0.01479955, -9.0955474, -0.03581456, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 101.98560393, 0.0165055, 101.98560393, 0.0495165, 71.38992275, -1230.65809427, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 25.49640098, 9.666e-05, 76.48920295, 0.00028999, 254.96400982, 0.00096663, -25.49640098, -9.666e-05, -76.48920295, -0.00028999, -254.96400982, -0.00096663, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 101.98560393, 0.0165055, 101.98560393, 0.0495165, 71.38992275, -1230.65809427, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 25.49640098, 9.666e-05, 76.48920295, 0.00028999, 254.96400982, 0.00096663, -25.49640098, -9.666e-05, -76.48920295, -0.00028999, -254.96400982, -0.00096663, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.5, 0.0)
    ops.node(121007, 0.0, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.16, 26059655.72111316, 10858189.88379715, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 166.68021571, 0.00066337, 198.40407692, 0.01323421, 19.84040769, 0.03114313, -166.68021571, -0.00066337, -198.40407692, -0.01323421, -19.84040769, -0.03114313, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 150.81294617, 0.00066337, 179.51682655, 0.01323421, 17.95168265, 0.03114313, -150.81294617, -0.00066337, -179.51682655, -0.01323421, -17.95168265, -0.03114313, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 162.06431256, 0.01326731, 162.06431256, 0.03980194, 113.44501879, -1807.77954283, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 40.51607814, 8.675e-05, 121.54823442, 0.00026026, 405.16078139, 0.00086755, -40.51607814, -8.675e-05, -121.54823442, -0.00026026, -405.16078139, -0.00086755, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 162.06431256, 0.01326731, 162.06431256, 0.03980194, 113.44501879, -1807.77954283, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 40.51607814, 8.675e-05, 121.54823442, 0.00026026, 405.16078139, 0.00086755, -40.51607814, -8.675e-05, -121.54823442, -0.00026026, -405.16078139, -0.00086755, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.5, 4.5, 0.0)
    ops.node(121008, 4.5, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.25, 26835964.15260701, 11181651.73025292, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 298.66661649, 0.00060529, 357.33129553, 0.01229079, 35.73312955, 0.02650279, -298.66661649, -0.00060529, -357.33129553, -0.01229079, -35.73312955, -0.02650279, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 286.76052521, 0.00060529, 343.08658659, 0.01229079, 34.30865866, 0.02650279, -286.76052521, -0.00060529, -343.08658659, -0.01229079, -34.30865866, -0.02650279, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 225.84530143, 0.01210577, 225.84530143, 0.0363173, 158.091711, -2048.30233428, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 56.46132536, 7.514e-05, 169.38397607, 0.00022541, 564.61325357, 0.00075136, -56.46132536, -7.514e-05, -169.38397607, -0.00022541, -564.61325357, -0.00075136, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 225.84530143, 0.01210577, 225.84530143, 0.0363173, 158.091711, -2048.30233428, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 56.46132536, 7.514e-05, 169.38397607, 0.00022541, 564.61325357, 0.00075136, -56.46132536, -7.514e-05, -169.38397607, -0.00022541, -564.61325357, -0.00075136, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.0, 4.5, 0.0)
    ops.node(121009, 9.0, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.2025, 27308667.9774602, 11378611.65727508, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 227.82802359, 0.00060926, 272.16699899, 0.01376217, 27.2166999, 0.03373174, -227.82802359, -0.00060926, -272.16699899, -0.01376217, -27.2166999, -0.03373174, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 203.33497376, 0.00060926, 242.90721013, 0.01376217, 24.29072101, 0.03373174, -203.33497376, -0.00060926, -242.90721013, -0.01376217, -24.29072101, -0.03373174, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 204.61842808, 0.01218517, 204.61842808, 0.03655551, 143.23289965, -2108.08226682, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 51.15460702, 8.259e-05, 153.46382106, 0.00024776, 511.54607019, 0.00082587, -51.15460702, -8.259e-05, -153.46382106, -0.00024776, -511.54607019, -0.00082587, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 204.61842808, 0.01218517, 204.61842808, 0.03655551, 143.23289965, -2108.08226682, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 51.15460702, 8.259e-05, 153.46382106, 0.00024776, 511.54607019, 0.00082587, -51.15460702, -8.259e-05, -153.46382106, -0.00024776, -511.54607019, -0.00082587, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.0, 4.5, 0.0)
    ops.node(121010, 12.0, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.2025, 26965580.46831044, 11235658.52846268, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 227.17349479, 0.00061433, 271.2992801, 0.01394519, 27.12992801, 0.03326122, -227.17349479, -0.00061433, -271.2992801, -0.01394519, -27.12992801, -0.03326122, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 202.99059985, 0.00061433, 242.41914161, 0.01394519, 24.24191416, 0.03326122, -202.99059985, -0.00061433, -242.41914161, -0.01394519, -24.24191416, -0.03326122, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 203.43422213, 0.01228668, 203.43422213, 0.03686005, 142.40395549, -2127.56907253, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 50.85855553, 8.315e-05, 152.5756666, 0.00024946, 508.58555533, 0.00083154, -50.85855553, -8.315e-05, -152.5756666, -0.00024946, -508.58555533, -0.00083154, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 203.43422213, 0.01228668, 203.43422213, 0.03686005, 142.40395549, -2127.56907253, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 50.85855553, 8.315e-05, 152.5756666, 0.00024946, 508.58555533, 0.00083154, -50.85855553, -8.315e-05, -152.5756666, -0.00024946, -508.58555533, -0.00083154, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 16.5, 4.5, 0.0)
    ops.node(121011, 16.5, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.25, 26108754.02658393, 10878647.51107664, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 297.11980048, 0.00060194, 355.17979805, 0.01189737, 35.5179798, 0.02510954, -297.11980048, -0.00060194, -355.17979805, -0.01189737, -35.5179798, -0.02510954, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 285.05534824, 0.00060194, 340.75783862, 0.01189737, 34.07578386, 0.02510954, -285.05534824, -0.00060194, -340.75783862, -0.01189737, -34.07578386, -0.02510954, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 219.61086242, 0.01203872, 219.61086242, 0.03611615, 153.7276037, -2041.81956023, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 54.90271561, 7.51e-05, 164.70814682, 0.00022529, 549.02715606, 0.00075097, -54.90271561, -7.51e-05, -164.70814682, -0.00022529, -549.02715606, -0.00075097, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 219.61086242, 0.01203872, 219.61086242, 0.03611615, 153.7276037, -2041.81956023, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 54.90271561, 7.51e-05, 164.70814682, 0.00022529, 549.02715606, 0.00075097, -54.90271561, -7.51e-05, -164.70814682, -0.00022529, -549.02715606, -0.00075097, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 21.0, 4.5, 0.0)
    ops.node(121012, 21.0, 4.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 28258902.30848132, 11774542.62853388, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 169.02881946, 0.00066612, 201.70520637, 0.01465892, 20.17052064, 0.03715601, -169.02881946, -0.00066612, -201.70520637, -0.01465892, -20.17052064, -0.03715601, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 153.57647358, 0.00066612, 183.26563715, 0.01465892, 18.32656372, 0.03715601, -153.57647358, -0.00066612, -183.26563715, -0.01465892, -18.32656372, -0.03715601, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 175.0905535, 0.01332247, 175.0905535, 0.0399674, 122.56338745, -1839.48651334, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 43.77263837, 8.643e-05, 131.31791512, 0.0002593, 437.72638374, 0.00086433, -43.77263837, -8.643e-05, -131.31791512, -0.0002593, -437.72638374, -0.00086433, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 175.0905535, 0.01332247, 175.0905535, 0.0399674, 122.56338745, -1839.48651334, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 43.77263837, 8.643e-05, 131.31791512, 0.0002593, 437.72638374, 0.00086433, -43.77263837, -8.643e-05, -131.31791512, -0.0002593, -437.72638374, -0.00086433, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.16, 26941623.67242133, 11225676.53017555, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 167.68098249, 0.00065623, 199.8912593, 0.01388779, 19.98912593, 0.03372328, -167.68098249, -0.00065623, -199.8912593, -0.01388779, -19.98912593, -0.03372328, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 151.63937728, 0.00065623, 180.76818035, 0.01388779, 18.07681803, 0.03372328, -151.63937728, -0.00065623, -180.76818035, -0.01388779, -18.07681803, -0.03372328, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 166.48406137, 0.01312468, 166.48406137, 0.03937404, 116.53884296, -1805.69803529, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 41.62101534, 8.62e-05, 124.86304603, 0.00025861, 416.21015342, 0.00086203, -41.62101534, -8.62e-05, -124.86304603, -0.00025861, -416.21015342, -0.00086203, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 166.48406137, 0.01312468, 166.48406137, 0.03937404, 116.53884296, -1805.69803529, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 41.62101534, 8.62e-05, 124.86304603, 0.00025861, 416.21015342, 0.00086203, -41.62101534, -8.62e-05, -124.86304603, -0.00025861, -416.21015342, -0.00086203, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.5, 9.0, 0.0)
    ops.node(121014, 4.5, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.25, 27629569.84973869, 11512320.77072446, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 296.12373307, 0.00058559, 354.47634443, 0.01286415, 35.44763444, 0.02812778, -296.12373307, -0.00058559, -354.47634443, -0.01286415, -35.44763444, -0.02812778, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 284.36005648, 0.00058559, 340.39457857, 0.01286415, 34.03945786, 0.02812778, -284.36005648, -0.00058559, -340.39457857, -0.01286415, -34.03945786, -0.02812778, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 232.78215029, 0.01171188, 232.78215029, 0.03513563, 162.9475052, -2055.92061473, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 58.19553757, 7.522e-05, 174.58661272, 0.00022566, 581.95537572, 0.00075219, -58.19553757, -7.522e-05, -174.58661272, -0.00022566, -581.95537572, -0.00075219, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 232.78215029, 0.01171188, 232.78215029, 0.03513563, 162.9475052, -2055.92061473, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 58.19553757, 7.522e-05, 174.58661272, 0.00022566, 581.95537572, 0.00075219, -58.19553757, -7.522e-05, -174.58661272, -0.00022566, -581.95537572, -0.00075219, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 9.0, 0.0)
    ops.node(121015, 9.0, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.2025, 26975146.87914767, 11239644.5329782, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 226.74526981, 0.00061488, 270.77991615, 0.01385215, 27.07799161, 0.03316392, -226.74526981, -0.00061488, -270.77991615, -0.01385215, -27.07799161, -0.03316392, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 202.87609666, 0.00061488, 242.27527431, 0.01385215, 24.22752743, 0.03316392, -202.87609666, -0.00061488, -242.27527431, -0.01385215, -24.22752743, -0.03316392, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 204.1636406, 0.01229756, 204.1636406, 0.03689268, 142.91454842, -2140.57088263, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 51.04091015, 8.342e-05, 153.12273045, 0.00025027, 510.40910151, 0.00083423, -51.04091015, -8.342e-05, -153.12273045, -0.00025027, -510.40910151, -0.00083423, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 204.1636406, 0.01229756, 204.1636406, 0.03689268, 142.91454842, -2140.57088263, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 51.04091015, 8.342e-05, 153.12273045, 0.00025027, 510.40910151, 0.00083423, -51.04091015, -8.342e-05, -153.12273045, -0.00025027, -510.40910151, -0.00083423, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.0, 9.0, 0.0)
    ops.node(121016, 12.0, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.2025, 26930419.02995164, 11221007.92914652, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 226.23833902, 0.00060887, 270.16172286, 0.01369365, 27.01617229, 0.03291921, -226.23833902, -0.00060887, -270.16172286, -0.01369365, -27.01617229, -0.03291921, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 202.20405353, 0.00060887, 241.46126474, 0.01369365, 24.14612647, 0.03291921, -202.20405353, -0.00060887, -241.46126474, -0.01369365, -24.14612647, -0.03291921, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 202.75621227, 0.01217744, 202.75621227, 0.03653233, 141.92934859, -2119.42670854, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 50.68905307, 8.299e-05, 152.0671592, 0.00024896, 506.89053068, 0.00082985, -50.68905307, -8.299e-05, -152.0671592, -0.00024896, -506.89053068, -0.00082985, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 202.75621227, 0.01217744, 202.75621227, 0.03653233, 141.92934859, -2119.42670854, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 50.68905307, 8.299e-05, 152.0671592, 0.00024896, 506.89053068, 0.00082985, -50.68905307, -8.299e-05, -152.0671592, -0.00024896, -506.89053068, -0.00082985, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 16.5, 9.0, 0.0)
    ops.node(121017, 16.5, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.25, 25843266.05910226, 10768027.52462594, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 298.78878066, 0.00060232, 357.0428954, 0.0120395, 35.70428954, 0.02489094, -298.78878066, -0.00060232, -357.0428954, -0.0120395, -35.70428954, -0.02489094, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 286.29919681, 0.00060232, 342.11824807, 0.0120395, 34.21182481, 0.02489094, -286.29919681, -0.00060232, -342.11824807, -0.0120395, -34.21182481, -0.02489094, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 218.20999398, 0.01204634, 218.20999398, 0.03613902, 152.74699579, -2053.7561125, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 54.5524985, 7.538e-05, 163.65749549, 0.00022615, 545.52498495, 0.00075384, -54.5524985, -7.538e-05, -163.65749549, -0.00022615, -545.52498495, -0.00075384, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 218.20999398, 0.01204634, 218.20999398, 0.03613902, 152.74699579, -2053.7561125, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 54.5524985, 7.538e-05, 163.65749549, 0.00022615, 545.52498495, 0.00075384, -54.5524985, -7.538e-05, -163.65749549, -0.00022615, -545.52498495, -0.00075384, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.16, 26417473.66669993, 11007280.6944583, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 166.21124248, 0.00068597, 197.98441717, 0.01363966, 19.79844172, 0.0323516, -166.21124248, -0.00068597, -197.98441717, -0.01363966, -19.79844172, -0.0323516, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 151.50524619, 0.00068597, 180.46720196, 0.01363966, 18.0467202, 0.0323516, -151.50524619, -0.00068597, -180.46720196, -0.01363966, -18.0467202, -0.0323516, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 165.15968319, 0.01371931, 165.15968319, 0.04115793, 115.61177824, -1831.70236567, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 41.2899208, 8.721e-05, 123.86976239, 0.00026164, 412.89920798, 0.00087214, -41.2899208, -8.721e-05, -123.86976239, -0.00026164, -412.89920798, -0.00087214, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 165.15968319, 0.01371931, 165.15968319, 0.04115793, 115.61177824, -1831.70236567, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 41.2899208, 8.721e-05, 123.86976239, 0.00026164, 412.89920798, 0.00087214, -41.2899208, -8.721e-05, -123.86976239, -0.00026164, -412.89920798, -0.00087214, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.09, 26570602.29628523, 11071084.29011885, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 77.49731179, 0.00083261, 92.14048816, 0.01481531, 9.21404882, 0.03692369, -77.49731179, -0.00083261, -92.14048816, -0.01481531, -9.21404882, -0.03692369, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 77.49731179, 0.00083261, 92.14048816, 0.01481531, 9.21404882, 0.03692369, -77.49731179, -0.00083261, -92.14048816, -0.01481531, -9.21404882, -0.03692369, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 101.59483909, 0.01665227, 101.59483909, 0.04995682, 71.11638736, -1199.14832305, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 25.39870977, 9.482e-05, 76.19612932, 0.00028447, 253.98709772, 0.00094825, -25.39870977, -9.482e-05, -76.19612932, -0.00028447, -253.98709772, -0.00094825, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 101.59483909, 0.01665227, 101.59483909, 0.04995682, 71.11638736, -1199.14832305, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 25.39870977, 9.482e-05, 76.19612932, 0.00028447, 253.98709772, 0.00094825, -25.39870977, -9.482e-05, -76.19612932, -0.00028447, -253.98709772, -0.00094825, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 4.5, 13.5, 0.0)
    ops.node(121020, 4.5, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.16, 27287013.83597505, 11369589.09832294, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 157.63150697, 0.00067399, 187.98430733, 0.01432798, 18.79843073, 0.03488092, -157.63150697, -0.00067399, -187.98430733, -0.01432798, -18.79843073, -0.03488092, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 178.58994849, 0.00067399, 212.97841026, 0.01432798, 21.29784103, 0.03488092, -178.58994849, -0.00067399, -212.97841026, -0.01432798, -21.29784103, -0.03488092, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 169.3833954, 0.0134799, 169.3833954, 0.0404397, 118.56837678, -1827.01795758, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 42.34584885, 8.659e-05, 127.03754655, 0.00025978, 423.45848851, 0.00086594, -42.34584885, -8.659e-05, -127.03754655, -0.00025978, -423.45848851, -0.00086594, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 169.3833954, 0.0134799, 169.3833954, 0.0404397, 118.56837678, -1827.01795758, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 42.34584885, 8.659e-05, 127.03754655, 0.00025978, 423.45848851, 0.00086594, -42.34584885, -8.659e-05, -127.03754655, -0.00025978, -423.45848851, -0.00086594, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 9.0, 13.5, 0.0)
    ops.node(121021, 9.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.1225, 27893067.31273017, 11622111.38030424, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 117.28746112, 0.00074567, 139.4998732, 0.01429348, 13.94998732, 0.03613401, -117.28746112, -0.00074567, -139.4998732, -0.01429348, -13.94998732, -0.03613401, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 130.53437182, 0.00074567, 155.25554176, 0.01429348, 15.52555418, 0.03613401, -130.53437182, -0.00074567, -155.25554176, -0.01429348, -15.52555418, -0.03613401, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 139.16947001, 0.01491345, 139.16947001, 0.04474034, 97.41862901, -1554.23920141, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 34.7923675, 9.091e-05, 104.37710251, 0.00027273, 347.92367503, 0.00090909, -34.7923675, -9.091e-05, -104.37710251, -0.00027273, -347.92367503, -0.00090909, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 139.16947001, 0.01491345, 139.16947001, 0.04474034, 97.41862901, -1554.23920141, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 34.7923675, 9.091e-05, 104.37710251, 0.00027273, 347.92367503, 0.00090909, -34.7923675, -9.091e-05, -104.37710251, -0.00027273, -347.92367503, -0.00090909, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 12.0, 13.5, 0.0)
    ops.node(121022, 12.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.1225, 26854750.92851087, 11189479.5535462, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 117.35268537, 0.00074415, 139.37869607, 0.01384965, 13.93786961, 0.0332954, -117.35268537, -0.00074415, -139.37869607, -0.01384965, -13.93786961, -0.0332954, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 131.55541474, 0.00074415, 156.24714602, 0.01384965, 15.6247146, 0.0332954, -131.55541474, -0.00074415, -156.24714602, -0.01384965, -15.6247146, -0.0332954, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 136.17823955, 0.01488309, 136.17823955, 0.04464928, 95.32476768, -1577.41565672, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 34.04455989, 9.239e-05, 102.13367966, 0.00027718, 340.44559887, 0.00092394, -34.04455989, -9.239e-05, -102.13367966, -0.00027718, -340.44559887, -0.00092394, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 136.17823955, 0.01488309, 136.17823955, 0.04464928, 95.32476768, -1577.41565672, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 34.04455989, 9.239e-05, 102.13367966, 0.00027718, 340.44559887, 0.00092394, -34.04455989, -9.239e-05, -102.13367966, -0.00027718, -340.44559887, -0.00092394, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 16.5, 13.5, 0.0)
    ops.node(121023, 16.5, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.16, 26926101.26402185, 11219208.86000911, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 156.14979995, 0.00065975, 186.13943033, 0.01430323, 18.61394303, 0.03409997, -156.14979995, -0.00065975, -186.13943033, -0.01430323, -18.61394303, -0.03409997, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 177.45415106, 0.00065975, 211.53542687, 0.01430323, 21.15354269, 0.03409997, -177.45415106, -0.00065975, -211.53542687, -0.01430323, -21.15354269, -0.03409997, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 168.02489228, 0.013195, 168.02489228, 0.03958499, 117.6174246, -1836.65944858, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 42.00622307, 8.705e-05, 126.01866921, 0.00026115, 420.06223071, 0.00087051, -42.00622307, -8.705e-05, -126.01866921, -0.00026115, -420.06223071, -0.00087051, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 168.02489228, 0.013195, 168.02489228, 0.03958499, 117.6174246, -1836.65944858, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 42.00622307, 8.705e-05, 126.01866921, 0.00026115, 420.06223071, 0.00087051, -42.00622307, -8.705e-05, -126.01866921, -0.00026115, -420.06223071, -0.00087051, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.09, 25940069.81257878, 10808362.42190783, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 76.86074036, 0.00084138, 91.26150399, 0.01479908, 9.1261504, 0.03519862, -76.86074036, -0.00084138, -91.26150399, -0.01479908, -9.1261504, -0.03519862, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 76.86074036, 0.00084138, 91.26150399, 0.01479908, 9.1261504, 0.03519862, -76.86074036, -0.00084138, -91.26150399, -0.01479908, -9.1261504, -0.03519862, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 101.36041723, 0.01682765, 101.36041723, 0.05048295, 70.95229206, -1231.23141992, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 25.34010431, 9.691e-05, 76.02031292, 0.00029072, 253.40104307, 0.00096906, -25.34010431, -9.691e-05, -76.02031292, -0.00029072, -253.40104307, -0.00096906, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 101.36041723, 0.01682765, 101.36041723, 0.05048295, 70.95229206, -1231.23141992, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 25.34010431, 9.691e-05, 76.02031292, 0.00029072, 253.40104307, 0.00096906, -25.34010431, -9.691e-05, -76.02031292, -0.00029072, -253.40104307, -0.00096906, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.35)
    ops.node(122001, 0.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 27233604.07736643, 11347335.03223602, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 58.20141075, 0.00073563, 69.82550501, 0.01721195, 6.9825505, 0.04747574, -58.20141075, -0.00073563, -69.82550501, -0.01721195, -6.9825505, -0.04747574, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 61.54332511, 0.00073563, 73.83487275, 0.01721195, 7.38348727, 0.04747574, -61.54332511, -0.00073563, -73.83487275, -0.01721195, -7.38348727, -0.04747574, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 97.69482165, 0.01471261, 97.69482165, 0.04413782, 68.38637516, -1189.55302512, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 24.42370541, 8.036e-05, 73.27111624, 0.00024107, 244.23705413, 0.00080355, -24.42370541, -8.036e-05, -73.27111624, -0.00024107, -244.23705413, -0.00080355, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 97.69482165, 0.01471261, 97.69482165, 0.04413782, 68.38637516, -1189.55302512, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 24.42370541, 8.036e-05, 73.27111624, 0.00024107, 244.23705413, 0.00080355, -24.42370541, -8.036e-05, -73.27111624, -0.00024107, -244.23705413, -0.00080355, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.5, 0.0, 3.35)
    ops.node(122002, 4.5, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.16, 27891106.0640154, 11621294.19333975, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 125.22908142, 0.00061305, 150.41337504, 0.01567027, 15.0413375, 0.04223562, -125.22908142, -0.00061305, -150.41337504, -0.01567027, -15.0413375, -0.04223562, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 138.81862199, 0.00061305, 166.73585093, 0.01567027, 16.67358509, 0.04223562, -138.81862199, -0.00061305, -166.73585093, -0.01567027, -16.67358509, -0.04223562, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 159.53945251, 0.01226107, 159.53945251, 0.0367832, 111.67761676, -1709.46595723, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 39.88486313, 7.207e-05, 119.65458938, 0.00021622, 398.84863128, 0.00072073, -39.88486313, -7.207e-05, -119.65458938, -0.00021622, -398.84863128, -0.00072073, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 159.53945251, 0.01226107, 159.53945251, 0.0367832, 111.67761676, -1709.46595723, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 39.88486313, 7.207e-05, 119.65458938, 0.00021622, 398.84863128, 0.00072073, -39.88486313, -7.207e-05, -119.65458938, -0.00021622, -398.84863128, -0.00072073, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.5, 0.0, 3.35)
    ops.node(122005, 16.5, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.16, 26347241.14219429, 10978017.14258096, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 125.63946756, 0.00061222, 150.84639658, 0.01529981, 15.08463966, 0.0388842, -125.63946756, -0.00061222, -150.84639658, -0.01529981, -15.08463966, -0.0388842, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 140.79403567, 0.00061222, 169.04141154, 0.01529981, 16.90414115, 0.0388842, -140.79403567, -0.00061222, -169.04141154, -0.01529981, -16.90414115, -0.0388842, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 152.6916788, 0.0122444, 152.6916788, 0.03673321, 106.88417516, -1726.55423361, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 38.1729197, 7.302e-05, 114.5187591, 0.00021906, 381.72919701, 0.00073022, -38.1729197, -7.302e-05, -114.5187591, -0.00021906, -381.72919701, -0.00073022, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 152.6916788, 0.0122444, 152.6916788, 0.03673321, 106.88417516, -1726.55423361, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 38.1729197, 7.302e-05, 114.5187591, 0.00021906, 381.72919701, 0.00073022, -38.1729197, -7.302e-05, -114.5187591, -0.00021906, -381.72919701, -0.00073022, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 21.0, 0.0, 3.35)
    ops.node(122006, 21.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.09, 24854749.48823403, 10356145.62009751, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 57.38999559, 0.00075788, 68.66392048, 0.0153382, 6.86639205, 0.0393372, -57.38999559, -0.00075788, -68.66392048, -0.0153382, -6.86639205, -0.0393372, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 60.69421239, 0.00075788, 72.61723111, 0.0153382, 7.26172311, 0.0393372, -60.69421239, -0.00075788, -72.61723111, -0.0153382, -7.26172311, -0.0393372, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 90.35306127, 0.01515761, 90.35306127, 0.04547282, 63.24714289, -1169.82224348, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 22.58826532, 8.143e-05, 67.76479595, 0.00024429, 225.88265317, 0.00081429, -22.58826532, -8.143e-05, -67.76479595, -0.00024429, -225.88265317, -0.00081429, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 90.35306127, 0.01515761, 90.35306127, 0.04547282, 63.24714289, -1169.82224348, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 22.58826532, 8.143e-05, 67.76479595, 0.00024429, 225.88265317, 0.00081429, -22.58826532, -8.143e-05, -67.76479595, -0.00024429, -225.88265317, -0.00081429, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.35)
    ops.node(122007, 0.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.16, 26337233.32473681, 10973847.21864034, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 139.0466831, 0.00061606, 166.93232714, 0.01552135, 16.69323271, 0.03904351, -139.0466831, -0.00061606, -166.93232714, -0.01552135, -16.69323271, -0.03904351, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 124.81001125, 0.00061606, 149.84050797, 0.01552135, 14.9840508, 0.03904351, -124.81001125, -0.00061606, -149.84050797, -0.01552135, -14.9840508, -0.03904351, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 153.15520352, 0.01232111, 153.15520352, 0.03696332, 107.20864246, -1738.19518051, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 38.28880088, 7.327e-05, 114.86640264, 0.00021981, 382.88800879, 0.00073271, -38.28880088, -7.327e-05, -114.86640264, -0.00021981, -382.88800879, -0.00073271, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 153.15520352, 0.01232111, 153.15520352, 0.03696332, 107.20864246, -1738.19518051, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 38.28880088, 7.327e-05, 114.86640264, 0.00021981, 382.88800879, 0.00073271, -38.28880088, -7.327e-05, -114.86640264, -0.00021981, -382.88800879, -0.00073271, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.5, 4.5, 3.35)
    ops.node(122008, 4.5, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.25, 27355811.43813358, 11398254.76588899, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 252.4844083, 0.00055428, 303.94633655, 0.01372749, 30.39463365, 0.0314335, -252.4844083, -0.00055428, -303.94633655, -0.01372749, -30.39463365, -0.0314335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 241.33409465, 0.00055428, 290.52334141, 0.01372749, 29.05233414, 0.0314335, -241.33409465, -0.00055428, -290.52334141, -0.01372749, -29.05233414, -0.0314335, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 233.10607377, 0.01108561, 233.10607377, 0.03325684, 163.17425164, -1864.056844, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 58.27651844, 6.872e-05, 174.82955533, 0.00020615, 582.76518443, 0.00068715, -58.27651844, -6.872e-05, -174.82955533, -0.00020615, -582.76518443, -0.00068715, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 233.10607377, 0.01108561, 233.10607377, 0.03325684, 163.17425164, -1864.056844, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 58.27651844, 6.872e-05, 174.82955533, 0.00020615, 582.76518443, 0.00068715, -58.27651844, -6.872e-05, -174.82955533, -0.00020615, -582.76518443, -0.00068715, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.0, 4.5, 3.35)
    ops.node(122009, 9.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.2025, 26854801.90912285, 11189500.79546786, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 190.22102002, 0.00056825, 228.67631599, 0.01545223, 22.8676316, 0.03879979, -190.22102002, -0.00056825, -228.67631599, -0.01545223, -22.8676316, -0.03879979, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 168.12935968, 0.00056825, 202.11858068, 0.01545223, 20.21185807, 0.03879979, -168.12935968, -0.00056825, -202.11858068, -0.01545223, -20.21185807, -0.03879979, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 193.26427916, 0.01136491, 193.26427916, 0.03409472, 135.28499541, -2022.55240141, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 48.31606979, 7.165e-05, 144.94820937, 0.00021494, 483.1606979, 0.00071647, -48.31606979, -7.165e-05, -144.94820937, -0.00021494, -483.1606979, -0.00071647, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 193.26427916, 0.01136491, 193.26427916, 0.03409472, 135.28499541, -2022.55240141, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 48.31606979, 7.165e-05, 144.94820937, 0.00021494, 483.1606979, 0.00071647, -48.31606979, -7.165e-05, -144.94820937, -0.00021494, -483.1606979, -0.00071647, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.0, 4.5, 3.35)
    ops.node(122010, 12.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.2025, 28040559.15407874, 11683566.31419948, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 192.87294869, 0.00056501, 231.84935377, 0.01527956, 23.18493538, 0.04064074, -192.87294869, -0.00056501, -231.84935377, -0.01527956, -23.18493538, -0.04064074, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 170.1800449, 0.00056501, 204.57059272, 0.01527956, 20.45705927, 0.04064074, -170.1800449, -0.00056501, -204.57059272, -0.01527956, -20.45705927, -0.04064074, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 199.49283424, 0.01130016, 199.49283424, 0.03390048, 139.64498397, -1992.15190636, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 49.87320856, 7.083e-05, 149.61962568, 0.00021248, 498.73208561, 0.00070828, -49.87320856, -7.083e-05, -149.61962568, -0.00021248, -498.73208561, -0.00070828, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 199.49283424, 0.01130016, 199.49283424, 0.03390048, 139.64498397, -1992.15190636, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 49.87320856, 7.083e-05, 149.61962568, 0.00021248, 498.73208561, 0.00070828, -49.87320856, -7.083e-05, -149.61962568, -0.00021248, -498.73208561, -0.00070828, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 16.5, 4.5, 3.35)
    ops.node(122011, 16.5, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.25, 26102572.60291864, 10876071.91788276, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 252.62940542, 0.00056293, 304.04535923, 0.013456, 30.40453592, 0.02961363, -252.62940542, -0.00056293, -304.04535923, -0.013456, -30.40453592, -0.02961363, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 241.26231117, 0.00056293, 290.36479719, 0.013456, 29.03647972, 0.02961363, -241.26231117, -0.00056293, -290.36479719, -0.013456, -29.03647972, -0.02961363, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 222.69133635, 0.01125864, 222.69133635, 0.03377593, 155.88393545, -1871.43973781, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 55.67283409, 6.88e-05, 167.01850226, 0.00020639, 556.72834088, 0.00068797, -55.67283409, -6.88e-05, -167.01850226, -0.00020639, -556.72834088, -0.00068797, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 222.69133635, 0.01125864, 222.69133635, 0.03377593, 155.88393545, -1871.43973781, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 55.67283409, 6.88e-05, 167.01850226, 0.00020639, 556.72834088, 0.00068797, -55.67283409, -6.88e-05, -167.01850226, -0.00020639, -556.72834088, -0.00068797, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.35)
    ops.node(122012, 21.0, 4.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 28112536.06001035, 11713556.69167098, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 140.98936821, 0.00060491, 169.32513696, 0.01576027, 16.9325137, 0.0426837, -140.98936821, -0.00060491, -169.32513696, -0.01576027, -16.9325137, -0.0426837, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 126.38646871, 0.00060491, 151.78737515, 0.01576027, 15.17873751, 0.0426837, -126.38646871, -0.00060491, -151.78737515, -0.01576027, -15.17873751, -0.0426837, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 160.96726529, 0.01209817, 160.96726529, 0.0362945, 112.6770857, -1716.69881365, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 40.24181632, 7.215e-05, 120.72544897, 0.00021644, 402.41816322, 0.00072145, -40.24181632, -7.215e-05, -120.72544897, -0.00021644, -402.41816322, -0.00072145, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 160.96726529, 0.01209817, 160.96726529, 0.0362945, 112.6770857, -1716.69881365, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 40.24181632, 7.215e-05, 120.72544897, 0.00021644, 402.41816322, 0.00072145, -40.24181632, -7.215e-05, -120.72544897, -0.00021644, -402.41816322, -0.00072145, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.35)
    ops.node(122013, 0.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.16, 27235374.89790257, 11348072.87412607, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 140.34966766, 0.00060759, 168.5726805, 0.0159194, 16.85726805, 0.04124876, -140.34966766, -0.00060759, -168.5726805, -0.0159194, -16.85726805, -0.04124876, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 125.66534828, 0.00060759, 150.93548107, 0.0159194, 15.09354811, 0.04124876, -125.66534828, -0.00060759, -150.93548107, -0.0159194, -15.09354811, -0.04124876, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 157.46704973, 0.0121518, 157.46704973, 0.03645541, 110.22693481, -1736.17993059, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 39.36676243, 7.285e-05, 118.1002873, 0.00021855, 393.66762434, 0.0007285, -39.36676243, -7.285e-05, -118.1002873, -0.00021855, -393.66762434, -0.0007285, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 157.46704973, 0.0121518, 157.46704973, 0.03645541, 110.22693481, -1736.17993059, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 39.36676243, 7.285e-05, 118.1002873, 0.00021855, 393.66762434, 0.0007285, -39.36676243, -7.285e-05, -118.1002873, -0.00021855, -393.66762434, -0.0007285, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.5, 9.0, 3.35)
    ops.node(122014, 4.5, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.25, 28261072.16301993, 11775446.73459164, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 253.94233013, 0.0005503, 305.5977975, 0.01371273, 30.55977975, 0.03244826, -253.94233013, -0.0005503, -305.5977975, -0.01371273, -30.55977975, -0.03244826, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 242.69508481, 0.0005503, 292.06270315, 0.01371273, 29.20627032, 0.03244826, -242.69508481, -0.0005503, -292.06270315, -0.01371273, -29.20627032, -0.03244826, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 241.02067677, 0.01100609, 241.02067677, 0.03301828, 168.71447374, -1863.5997526, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 60.25516919, 6.877e-05, 180.76550758, 0.00020632, 602.55169192, 0.00068773, -60.25516919, -6.877e-05, -180.76550758, -0.00020632, -602.55169192, -0.00068773, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 241.02067677, 0.01100609, 241.02067677, 0.03301828, 168.71447374, -1863.5997526, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 60.25516919, 6.877e-05, 180.76550758, 0.00020632, 602.55169192, 0.00068773, -60.25516919, -6.877e-05, -180.76550758, -0.00020632, -602.55169192, -0.00068773, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 9.0, 3.35)
    ops.node(122015, 9.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.2025, 28281314.79391966, 11783881.16413319, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 194.42423064, 0.00055903, 233.6628444, 0.01556749, 23.36628444, 0.04122723, -194.42423064, -0.00055903, -233.6628444, -0.01556749, -23.36628444, -0.04122723, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 171.08617754, 0.00055903, 205.61471556, 0.01556749, 20.56147156, 0.04122723, -171.08617754, -0.00055903, -205.61471556, -0.01556749, -20.56147156, -0.04122723, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 202.66565319, 0.01118053, 202.66565319, 0.0335416, 141.86595724, -2027.81296758, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 50.6664133, 7.134e-05, 151.99923989, 0.00021403, 506.66413298, 0.00071342, -50.6664133, -7.134e-05, -151.99923989, -0.00021403, -506.66413298, -0.00071342, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 202.66565319, 0.01118053, 202.66565319, 0.0335416, 141.86595724, -2027.81296758, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 50.6664133, 7.134e-05, 151.99923989, 0.00021403, 506.66413298, 0.00071342, -50.6664133, -7.134e-05, -151.99923989, -0.00021403, -506.66413298, -0.00071342, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.0, 9.0, 3.35)
    ops.node(122016, 12.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.2025, 26726912.51378809, 11136213.5474117, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 193.20722564, 0.00056532, 232.22531332, 0.01482939, 23.22253133, 0.0378552, -193.20722564, -0.00056532, -232.22531332, -0.01482939, -23.22253133, -0.0378552, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 169.75442413, 0.00056532, 204.03623209, 0.01482939, 20.40362321, 0.0378552, -169.75442413, -0.00056532, -204.03623209, -0.01482939, -20.40362321, -0.0378552, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 191.29534189, 0.01130648, 191.29534189, 0.03391944, 133.90673932, -1996.83593898, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 47.82383547, 7.126e-05, 143.47150642, 0.00021377, 478.23835472, 0.00071256, -47.82383547, -7.126e-05, -143.47150642, -0.00021377, -478.23835472, -0.00071256, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 191.29534189, 0.01130648, 191.29534189, 0.03391944, 133.90673932, -1996.83593898, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 47.82383547, 7.126e-05, 143.47150642, 0.00021377, 478.23835472, 0.00071256, -47.82383547, -7.126e-05, -143.47150642, -0.00021377, -478.23835472, -0.00071256, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 16.5, 9.0, 3.35)
    ops.node(122017, 16.5, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.25, 27053243.33385048, 11272184.7224377, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 253.8814301, 0.00055097, 305.6461559, 0.01376232, 30.56461559, 0.03112828, -253.8814301, -0.00055097, -305.6461559, -0.01376232, -30.56461559, -0.03112828, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 242.25747479, 0.00055097, 291.65215384, 0.01376232, 29.16521538, 0.03112828, -242.25747479, -0.00055097, -291.65215384, -0.01376232, -29.16521538, -0.03112828, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 231.25251391, 0.01101939, 231.25251391, 0.03305816, 161.87675974, -1879.38267575, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 57.81312848, 6.893e-05, 173.43938543, 0.00020679, 578.13128478, 0.00068931, -57.81312848, -6.893e-05, -173.43938543, -0.00020679, -578.13128478, -0.00068931, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 231.25251391, 0.01101939, 231.25251391, 0.03305816, 161.87675974, -1879.38267575, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 57.81312848, 6.893e-05, 173.43938543, 0.00020679, 578.13128478, 0.00068931, -57.81312848, -6.893e-05, -173.43938543, -0.00020679, -578.13128478, -0.00068931, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.35)
    ops.node(122018, 21.0, 9.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.16, 25624750.62083347, 10676979.42534728, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 138.44567466, 0.00061473, 166.09783068, 0.01497196, 16.60978307, 0.03701363, -138.44567466, -0.00061473, -166.09783068, -0.01497196, -16.60978307, -0.03701363, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 124.01522811, 0.00061473, 148.78514921, 0.01497196, 14.87851492, 0.03701363, -124.01522811, -0.00061473, -148.78514921, -0.01497196, -14.87851492, -0.03701363, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 149.40139844, 0.01229468, 149.40139844, 0.03688405, 104.58097891, -1731.18516783, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 37.35034961, 7.346e-05, 112.05104883, 0.00022039, 373.50349611, 0.00073462, -37.35034961, -7.346e-05, -112.05104883, -0.00022039, -373.50349611, -0.00073462, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 149.40139844, 0.01229468, 149.40139844, 0.03688405, 104.58097891, -1731.18516783, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 37.35034961, 7.346e-05, 112.05104883, 0.00022039, 373.50349611, 0.00073462, -37.35034961, -7.346e-05, -112.05104883, -0.00022039, -373.50349611, -0.00073462, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.35)
    ops.node(122019, 0.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.09, 26463191.30196878, 11026329.70915366, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 57.33677661, 0.00074641, 68.75788978, 0.01679521, 6.87578898, 0.04514406, -57.33677661, -0.00074641, -68.75788978, -0.01679521, -6.87578898, -0.04514406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 60.44952521, 0.00074641, 72.49067766, 0.01679521, 7.24906777, 0.04514406, -60.44952521, -0.00074641, -72.49067766, -0.01679521, -7.24906777, -0.04514406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 95.62473177, 0.01492822, 95.62473177, 0.04478465, 66.93731224, -1191.30118116, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 23.90618294, 8.094e-05, 71.71854883, 0.00024283, 239.06182942, 0.00080942, -23.90618294, -8.094e-05, -71.71854883, -0.00024283, -239.06182942, -0.00080942, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 95.62473177, 0.01492822, 95.62473177, 0.04478465, 66.93731224, -1191.30118116, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 23.90618294, 8.094e-05, 71.71854883, 0.00024283, 239.06182942, 0.00080942, -23.90618294, -8.094e-05, -71.71854883, -0.00024283, -239.06182942, -0.00080942, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 4.5, 13.5, 3.35)
    ops.node(122020, 4.5, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.16, 26821208.68327714, 11175503.61803214, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 125.57825121, 0.00062063, 150.81499855, 0.01543054, 15.08149985, 0.03997063, -125.57825121, -0.00062063, -150.81499855, -0.01543054, -15.08149985, -0.03997063, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 139.8018874, 0.00062063, 167.89707805, 0.01543054, 16.78970781, 0.03997063, -139.8018874, -0.00062063, -167.89707805, -0.01543054, -16.78970781, -0.03997063, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 155.24272695, 0.01241259, 155.24272695, 0.03723778, 108.66990886, -1731.9285034, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 38.81068174, 7.293e-05, 116.43204521, 0.00021879, 388.10681737, 0.0007293, -38.81068174, -7.293e-05, -116.43204521, -0.00021879, -388.10681737, -0.0007293, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 155.24272695, 0.01241259, 155.24272695, 0.03723778, 108.66990886, -1731.9285034, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 38.81068174, 7.293e-05, 116.43204521, 0.00021879, 388.10681737, 0.0007293, -38.81068174, -7.293e-05, -116.43204521, -0.00021879, -388.10681737, -0.0007293, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.35)
    ops.node(122021, 9.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.1225, 26533323.29096138, 11055551.37123391, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 96.9788934, 0.00067592, 116.13107566, 0.0154461, 11.61310757, 0.03975929, -96.9788934, -0.00067592, -116.13107566, -0.0154461, -11.61310757, -0.03975929, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 109.85530261, 0.00067592, 131.55042311, 0.0154461, 13.15504231, 0.03975929, -109.85530261, -0.00067592, -131.55042311, -0.0154461, -13.15504231, -0.03975929, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 124.1787658, 0.01351849, 124.1787658, 0.04055546, 86.92513606, -1472.93743636, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 31.04469145, 7.702e-05, 93.13407435, 0.00023106, 310.4469145, 0.00077021, -31.04469145, -7.702e-05, -93.13407435, -0.00023106, -310.4469145, -0.00077021, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 124.1787658, 0.01351849, 124.1787658, 0.04055546, 86.92513606, -1472.93743636, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 31.04469145, 7.702e-05, 93.13407435, 0.00023106, 310.4469145, 0.00077021, -31.04469145, -7.702e-05, -93.13407435, -0.00023106, -310.4469145, -0.00077021, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.35)
    ops.node(122022, 12.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.1225, 26487986.70970289, 11036661.12904287, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 96.06836361, 0.00067728, 115.03560076, 0.0156422, 11.50356008, 0.03985077, -96.06836361, -0.00067728, -115.03560076, -0.0156422, -11.50356008, -0.03985077, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 108.28296473, 0.00067728, 129.66178909, 0.0156422, 12.96617891, 0.03985077, -108.28296473, -0.00067728, -129.66178909, -0.0156422, -12.96617891, -0.03985077, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 125.23171327, 0.0135456, 125.23171327, 0.04063681, 87.66219929, -1500.74883245, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 31.30792832, 7.781e-05, 93.92378495, 0.00023342, 313.07928318, 0.00077807, -31.30792832, -7.781e-05, -93.92378495, -0.00023342, -313.07928318, -0.00077807, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 125.23171327, 0.0135456, 125.23171327, 0.04063681, 87.66219929, -1500.74883245, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 31.30792832, 7.781e-05, 93.92378495, 0.00023342, 313.07928318, 0.00077807, -31.30792832, -7.781e-05, -93.92378495, -0.00023342, -313.07928318, -0.00077807, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 16.5, 13.5, 3.35)
    ops.node(122023, 16.5, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.16, 26546988.5390944, 11061245.22462267, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 124.22402217, 0.0006071, 149.16719463, 0.01544342, 14.91671946, 0.03943495, -124.22402217, -0.0006071, -149.16719463, -0.01544342, -14.91671946, -0.03943495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 138.53085393, 0.0006071, 166.34672174, 0.01544342, 16.63467217, 0.03943495, -138.53085393, -0.0006071, -166.34672174, -0.01544342, -16.63467217, -0.03943495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 153.62294448, 0.0121421, 153.62294448, 0.03642629, 107.53606114, -1725.60572156, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 38.40573612, 7.291e-05, 115.21720836, 0.00021874, 384.0573612, 0.00072914, -38.40573612, -7.291e-05, -115.21720836, -0.00021874, -384.0573612, -0.00072914, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 153.62294448, 0.0121421, 153.62294448, 0.03642629, 107.53606114, -1725.60572156, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 38.40573612, 7.291e-05, 115.21720836, 0.00021874, 384.0573612, 0.00072914, -38.40573612, -7.291e-05, -115.21720836, -0.00021874, -384.0573612, -0.00072914, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.35)
    ops.node(122024, 21.0, 13.5, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.09, 26532703.90003129, 11055293.29167971, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 58.22312888, 0.0007282, 69.82470511, 0.01661267, 6.98247051, 0.04513892, -58.22312888, -0.0007282, -69.82470511, -0.01661267, -6.98247051, -0.04513892, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 61.74662594, 0.0007282, 74.05029635, 0.01661267, 7.40502963, 0.04513892, -61.74662594, -0.0007282, -74.05029635, -0.01661267, -7.40502963, -0.04513892, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 95.34233249, 0.01456409, 95.34233249, 0.04369226, 66.73963274, -1179.73513555, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 23.83558312, 8.049e-05, 71.50674937, 0.00024148, 238.35583122, 0.00080492, -23.83558312, -8.049e-05, -71.50674937, -0.00024148, -238.35583122, -0.00080492, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 95.34233249, 0.01456409, 95.34233249, 0.04369226, 66.73963274, -1179.73513555, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 23.83558312, 8.049e-05, 71.50674937, 0.00024148, 238.35583122, 0.00080492, -23.83558312, -8.049e-05, -71.50674937, -0.00024148, -238.35583122, -0.00080492, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.15)
    ops.node(123001, 0.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 26688861.56221139, 11120358.98425475, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 32.44211846, 0.00085953, 38.98345185, 0.01853702, 3.89834518, 0.05379829, -32.44211846, -0.00085953, -38.98345185, -0.01853702, -3.89834518, -0.05379829, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 32.44211846, 0.00085953, 38.98345185, 0.01853702, 3.89834518, 0.05379829, -32.44211846, -0.00085953, -38.98345185, -0.01853702, -3.89834518, -0.05379829, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 70.2968737, 0.01719057, 70.2968737, 0.05157171, 49.20781159, -924.15440757, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 17.57421843, 8.496e-05, 52.72265528, 0.00025488, 175.74218426, 0.0008496, -17.57421843, -8.496e-05, -52.72265528, -0.00025488, -175.74218426, -0.0008496, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 70.2968737, 0.01719057, 70.2968737, 0.05157171, 49.20781159, -924.15440757, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 17.57421843, 8.496e-05, 52.72265528, 0.00025488, 175.74218426, 0.0008496, -17.57421843, -8.496e-05, -52.72265528, -0.00025488, -175.74218426, -0.0008496, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.5, 0.0, 6.15)
    ops.node(123002, 4.5, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1225, 26897834.17970275, 11207430.90820948, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 86.22619181, 0.00064633, 103.87652766, 0.01718934, 10.38765277, 0.04698568, -86.22619181, -0.00064633, -103.87652766, -0.01718934, -10.38765277, -0.04698568, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 78.50009557, 0.00064633, 94.56891436, 0.01718934, 9.45689144, 0.04698568, -78.50009557, -0.00064633, -94.56891436, -0.01718934, -9.45689144, -0.04698568, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 120.3040559, 0.0129266, 120.3040559, 0.0387798, 84.21283913, -1365.12760582, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 30.07601397, 7.361e-05, 90.22804192, 0.00022082, 300.76013974, 0.00073607, -30.07601397, -7.361e-05, -90.22804192, -0.00022082, -300.76013974, -0.00073607, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 120.3040559, 0.0129266, 120.3040559, 0.0387798, 84.21283913, -1365.12760582, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 30.07601397, 7.361e-05, 90.22804192, 0.00022082, 300.76013974, 0.00073607, -30.07601397, -7.361e-05, -90.22804192, -0.00022082, -300.76013974, -0.00073607, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.5, 0.0, 6.15)
    ops.node(123005, 16.5, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 25788174.79244663, 10745072.8301861, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 88.02602135, 0.00065351, 106.00532931, 0.01626302, 10.60053293, 0.04368412, -88.02602135, -0.00065351, -106.00532931, -0.01626302, -10.60053293, -0.04368412, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 79.52722072, 0.00065351, 95.77064932, 0.01626302, 9.57706493, 0.04368412, -79.52722072, -0.00065351, -95.77064932, -0.01626302, -9.57706493, -0.04368412, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 114.84003916, 0.01307018, 114.84003916, 0.03921053, 80.38802742, -1330.11596249, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 28.71000979, 7.329e-05, 86.13002937, 0.00021986, 287.10009791, 0.00073287, -28.71000979, -7.329e-05, -86.13002937, -0.00021986, -287.10009791, -0.00073287, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 114.84003916, 0.01307018, 114.84003916, 0.03921053, 80.38802742, -1330.11596249, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 28.71000979, 7.329e-05, 86.13002937, 0.00021986, 287.10009791, 0.00073287, -28.71000979, -7.329e-05, -86.13002937, -0.00021986, -287.10009791, -0.00073287, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 21.0, 0.0, 6.15)
    ops.node(123006, 21.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 27697873.8242552, 11540780.76010633, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 33.21067547, 0.00082631, 39.91247061, 0.01834334, 3.99124706, 0.05633537, -33.21067547, -0.00082631, -39.91247061, -0.01834334, -3.99124706, -0.05633537, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 33.21067547, 0.00082631, 39.91247061, 0.01834334, 3.99124706, 0.05633537, -33.21067547, -0.00082631, -39.91247061, -0.01834334, -3.99124706, -0.05633537, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 70.72100038, 0.01652624, 70.72100038, 0.04957873, 49.50470027, -883.90969552, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 17.6802501, 8.236e-05, 53.04075029, 0.00024708, 176.80250096, 0.00082359, -17.6802501, -8.236e-05, -53.04075029, -0.00024708, -176.80250096, -0.00082359, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 70.72100038, 0.01652624, 70.72100038, 0.04957873, 49.50470027, -883.90969552, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 17.6802501, 8.236e-05, 53.04075029, 0.00024708, 176.80250096, 0.00082359, -17.6802501, -8.236e-05, -53.04075029, -0.00024708, -176.80250096, -0.00082359, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.15)
    ops.node(123007, 0.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 26230690.76793905, 10929454.48664127, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 86.85809043, 0.00064383, 104.62040183, 0.0169007, 10.46204018, 0.04527017, -86.85809043, -0.00064383, -104.62040183, -0.0169007, -10.46204018, -0.04527017, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 78.72737251, 0.00064383, 94.82696784, 0.0169007, 9.48269678, 0.04527017, -78.72737251, -0.00064383, -94.82696784, -0.0169007, -9.48269678, -0.04527017, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 117.39627165, 0.01287662, 117.39627165, 0.03862986, 82.17739015, -1353.36975694, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 29.34906791, 7.365e-05, 88.04720373, 0.00022096, 293.49067911, 0.00073654, -29.34906791, -7.365e-05, -88.04720373, -0.00022096, -293.49067911, -0.00073654, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 117.39627165, 0.01287662, 117.39627165, 0.03862986, 82.17739015, -1353.36975694, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 29.34906791, 7.365e-05, 88.04720373, 0.00022096, 293.49067911, 0.00073654, -29.34906791, -7.365e-05, -88.04720373, -0.00022096, -293.49067911, -0.00073654, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.5, 4.5, 6.15)
    ops.node(123008, 4.5, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.16, 26383840.34136065, 10993266.80890027, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 140.18934422, 0.0006393, 168.51279618, 0.01399209, 16.85127962, 0.03199841, -140.18934422, -0.0006393, -168.51279618, -0.01399209, -16.85127962, -0.03199841, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 140.18934422, 0.0006393, 168.51279618, 0.01399209, 16.85127962, 0.03199841, -140.18934422, -0.0006393, -168.51279618, -0.01399209, -16.85127962, -0.03199841, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 135.62363745, 0.01278599, 135.62363745, 0.03835797, 94.93654621, -1349.70820877, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 33.90590936, 6.477e-05, 101.71772809, 0.00019431, 339.05909362, 0.00064769, -33.90590936, -6.477e-05, -101.71772809, -0.00019431, -339.05909362, -0.00064769, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 135.62363745, 0.01278599, 135.62363745, 0.03835797, 94.93654621, -1349.70820877, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 33.90590936, 6.477e-05, 101.71772809, 0.00019431, 339.05909362, 0.00064769, -33.90590936, -6.477e-05, -101.71772809, -0.00019431, -339.05909362, -0.00064769, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.15)
    ops.node(123009, 9.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 26877483.53855051, 11198951.47439605, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 99.20283696, 0.00066942, 118.96714027, 0.0158077, 11.89671403, 0.04179016, -99.20283696, -0.00066942, -118.96714027, -0.0158077, -11.89671403, -0.04179016, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 90.64836325, 0.00066942, 108.70834825, 0.0158077, 10.87083482, 0.04179016, -90.64836325, -0.00066942, -108.70834825, -0.0158077, -10.87083482, -0.04179016, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 125.08369849, 0.01338847, 125.08369849, 0.0401654, 87.55858894, -1463.24219921, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 31.27092462, 7.659e-05, 93.81277387, 0.00022977, 312.70924622, 0.00076589, -31.27092462, -7.659e-05, -93.81277387, -0.00022977, -312.70924622, -0.00076589, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 125.08369849, 0.01338847, 125.08369849, 0.0401654, 87.55858894, -1463.24219921, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 31.27092462, 7.659e-05, 93.81277387, 0.00022977, 312.70924622, 0.00076589, -31.27092462, -7.659e-05, -93.81277387, -0.00022977, -312.70924622, -0.00076589, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.15)
    ops.node(123010, 12.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 25906703.05202293, 10794459.60500956, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 97.83274803, 0.00067367, 117.21980997, 0.01537282, 11.721981, 0.03912495, -97.83274803, -0.00067367, -117.21980997, -0.01537282, -11.721981, -0.03912495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 89.53956313, 0.00067367, 107.28320308, 0.01537282, 10.72832031, 0.03912495, -89.53956313, -0.00067367, -107.28320308, -0.01537282, -10.72832031, -0.03912495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 122.3358747, 0.01347333, 122.3358747, 0.04042, 85.63511229, -1484.21038427, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 30.58396868, 7.771e-05, 91.75190603, 0.00023314, 305.83968675, 0.00077713, -30.58396868, -7.771e-05, -91.75190603, -0.00023314, -305.83968675, -0.00077713, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 122.3358747, 0.01347333, 122.3358747, 0.04042, 85.63511229, -1484.21038427, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 30.58396868, 7.771e-05, 91.75190603, 0.00023314, 305.83968675, 0.00077713, -30.58396868, -7.771e-05, -91.75190603, -0.00023314, -305.83968675, -0.00077713, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 16.5, 4.5, 6.15)
    ops.node(123011, 16.5, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.16, 25088271.5882031, 10453446.49508462, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 141.08015868, 0.00064096, 169.35965264, 0.0134306, 16.93596526, 0.02941692, -141.08015868, -0.00064096, -169.35965264, -0.0134306, -16.93596526, -0.02941692, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 141.08015868, 0.00064096, 169.35965264, 0.0134306, 16.93596526, 0.02941692, -141.08015868, -0.00064096, -169.35965264, -0.0134306, -16.93596526, -0.02941692, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 130.14005082, 0.01281914, 130.14005082, 0.03845743, 91.09803557, -1364.33569552, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 32.53501271, 6.536e-05, 97.60503812, 0.00019608, 325.35012705, 0.0006536, -32.53501271, -6.536e-05, -97.60503812, -0.00019608, -325.35012705, -0.0006536, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 130.14005082, 0.01281914, 130.14005082, 0.03845743, 91.09803557, -1364.33569552, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 32.53501271, 6.536e-05, 97.60503812, 0.00019608, 325.35012705, 0.0006536, -32.53501271, -6.536e-05, -97.60503812, -0.00019608, -325.35012705, -0.0006536, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.15)
    ops.node(123012, 21.0, 4.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 26375445.95798659, 10989769.14916108, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 86.38833288, 0.00065025, 104.06000011, 0.01674178, 10.40600001, 0.04542238, -86.38833288, -0.00065025, -104.06000011, -0.01674178, -10.40600001, -0.04542238, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 78.56638806, 0.00065025, 94.63799194, 0.01674178, 9.46379919, 0.04542238, -78.56638806, -0.00065025, -94.63799194, -0.01674178, -9.46379919, -0.04542238, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 117.30357239, 0.01300497, 117.30357239, 0.0390149, 82.11250067, -1338.05656286, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 29.3258931, 7.319e-05, 87.97767929, 0.00021958, 293.25893097, 0.00073192, -29.3258931, -7.319e-05, -87.97767929, -0.00021958, -293.25893097, -0.00073192, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 117.30357239, 0.01300497, 117.30357239, 0.0390149, 82.11250067, -1338.05656286, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 29.3258931, 7.319e-05, 87.97767929, 0.00021958, 293.25893097, 0.00073192, -29.3258931, -7.319e-05, -87.97767929, -0.00021958, -293.25893097, -0.00073192, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.15)
    ops.node(123013, 0.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.1225, 27143234.15025897, 11309680.89594124, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 86.21875189, 0.00065333, 103.86299471, 0.01703237, 10.38629947, 0.04729643, -86.21875189, -0.00065333, -103.86299471, -0.01703237, -10.38629947, -0.04729643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 78.6988943, 0.00065333, 94.80423531, 0.01703237, 9.48042353, 0.04729643, -78.6988943, -0.00065333, -94.80423531, -0.01703237, -9.48042353, -0.04729643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 120.29475047, 0.01306656, 120.29475047, 0.03919967, 84.20632533, -1342.23675237, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 30.07368762, 7.294e-05, 90.22106286, 0.00021881, 300.73687619, 0.00072936, -30.07368762, -7.294e-05, -90.22106286, -0.00021881, -300.73687619, -0.00072936, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 120.29475047, 0.01306656, 120.29475047, 0.03919967, 84.20632533, -1342.23675237, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 30.07368762, 7.294e-05, 90.22106286, 0.00021881, 300.73687619, 0.00072936, -30.07368762, -7.294e-05, -90.22106286, -0.00021881, -300.73687619, -0.00072936, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.5, 9.0, 6.15)
    ops.node(123014, 4.5, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.16, 27452161.96860532, 11438400.82025222, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 141.4565618, 0.00063311, 170.08062483, 0.01428736, 17.00806248, 0.03380692, -141.4565618, -0.00063311, -170.08062483, -0.01428736, -17.00806248, -0.03380692, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 141.4565618, 0.00063311, 170.08062483, 0.01428736, 17.00806248, 0.03380692, -141.4565618, -0.00063311, -170.08062483, -0.01428736, -17.00806248, -0.03380692, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 141.40884987, 0.01266227, 141.40884987, 0.03798682, 98.98619491, -1361.60343661, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 35.35221247, 6.49e-05, 106.0566374, 0.00019471, 353.52212468, 0.00064904, -35.35221247, -6.49e-05, -106.0566374, -0.00019471, -353.52212468, -0.00064904, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 141.40884987, 0.01266227, 141.40884987, 0.03798682, 98.98619491, -1361.60343661, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 35.35221247, 6.49e-05, 106.0566374, 0.00019471, 353.52212468, 0.00064904, -35.35221247, -6.49e-05, -106.0566374, -0.00019471, -353.52212468, -0.00064904, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.15)
    ops.node(123015, 9.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 26789130.55022599, 11162137.72926083, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 98.48075671, 0.00065969, 118.04370069, 0.01574639, 11.80437007, 0.04120168, -98.48075671, -0.00065969, -118.04370069, -0.01574639, -11.80437007, -0.04120168, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 90.26990536, 0.00065969, 108.20178526, 0.01574639, 10.82017853, 0.04120168, -90.26990536, -0.00065969, -108.20178526, -0.01574639, -10.82017853, -0.04120168, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 125.10680156, 0.01319385, 125.10680156, 0.03958154, 87.5747611, -1471.38929499, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 31.27670039, 7.686e-05, 93.83010117, 0.00023057, 312.76700391, 0.00076856, -31.27670039, -7.686e-05, -93.83010117, -0.00023057, -312.76700391, -0.00076856, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 125.10680156, 0.01319385, 125.10680156, 0.03958154, 87.5747611, -1471.38929499, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 31.27670039, 7.686e-05, 93.83010117, 0.00023057, 312.76700391, 0.00076856, -31.27670039, -7.686e-05, -93.83010117, -0.00023057, -312.76700391, -0.00076856, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.15)
    ops.node(123016, 12.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1225, 26687389.72910357, 11119745.72045982, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 99.67331656, 0.00067006, 119.46429689, 0.01578172, 11.94642969, 0.04100786, -99.67331656, -0.00067006, -119.46429689, -0.01578172, -11.94642969, -0.04100786, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 91.21271121, 0.00067006, 109.32376677, 0.01578172, 10.93237668, 0.04100786, -91.21271121, -0.00067006, -109.32376677, -0.01578172, -10.93237668, -0.04100786, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 125.20604481, 0.01340117, 125.20604481, 0.04020351, 87.64423136, -1482.53806503, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 31.3015112, 7.721e-05, 93.9045336, 0.00023163, 313.01511201, 0.0007721, -31.3015112, -7.721e-05, -93.9045336, -0.00023163, -313.01511201, -0.0007721, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 125.20604481, 0.01340117, 125.20604481, 0.04020351, 87.64423136, -1482.53806503, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 31.3015112, 7.721e-05, 93.9045336, 0.00023163, 313.01511201, 0.0007721, -31.3015112, -7.721e-05, -93.9045336, -0.00023163, -313.01511201, -0.0007721, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 16.5, 9.0, 6.15)
    ops.node(123017, 16.5, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.16, 27361088.28677649, 11400453.45282354, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 142.49491063, 0.00062312, 171.32980005, 0.01405565, 17.13298001, 0.03345158, -142.49491063, -0.00062312, -171.32980005, -0.01405565, -17.13298001, -0.03345158, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 142.49491063, 0.00062312, 171.32980005, 0.01405565, 17.13298001, 0.03345158, -142.49491063, -0.00062312, -171.32980005, -0.01405565, -17.13298001, -0.03345158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 140.34246465, 0.01246236, 140.34246465, 0.03738709, 98.23972525, -1348.85323367, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 35.08561616, 6.463e-05, 105.25684849, 0.00019389, 350.85616162, 0.00064629, -35.08561616, -6.463e-05, -105.25684849, -0.00019389, -350.85616162, -0.00064629, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 140.34246465, 0.01246236, 140.34246465, 0.03738709, 98.23972525, -1348.85323367, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 35.08561616, 6.463e-05, 105.25684849, 0.00019389, 350.85616162, 0.00064629, -35.08561616, -6.463e-05, -105.25684849, -0.00019389, -350.85616162, -0.00064629, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.15)
    ops.node(123018, 21.0, 9.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1225, 26680509.41510691, 11116878.92296121, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 86.36726469, 0.00064546, 104.04176307, 0.01712359, 10.40417631, 0.04644674, -86.36726469, -0.00064546, -104.04176307, -0.01712359, -10.40417631, -0.04644674, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 78.54536578, 0.00064546, 94.61916348, 0.01712359, 9.46191635, 0.04644674, -78.54536578, -0.00064546, -94.61916348, -0.01712359, -9.46191635, -0.04644674, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 119.966032, 0.0129092, 119.966032, 0.03872761, 83.9762224, -1376.37343306, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 29.991508, 7.4e-05, 89.974524, 0.00022199, 299.91508, 0.00073998, -29.991508, -7.4e-05, -89.974524, -0.00022199, -299.91508, -0.00073998, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 119.966032, 0.0129092, 119.966032, 0.03872761, 83.9762224, -1376.37343306, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 29.991508, 7.4e-05, 89.974524, 0.00022199, 299.91508, 0.00073998, -29.991508, -7.4e-05, -89.974524, -0.00022199, -299.91508, -0.00073998, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.15)
    ops.node(123019, 0.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 27707894.89182694, 11544956.20492789, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 32.75392761, 0.00084338, 39.36348897, 0.01899461, 3.9363489, 0.05701258, -32.75392761, -0.00084338, -39.36348897, -0.01899461, -3.9363489, -0.05701258, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 32.75392761, 0.00084338, 39.36348897, 0.01899461, 3.9363489, 0.05701258, -32.75392761, -0.00084338, -39.36348897, -0.01899461, -3.9363489, -0.05701258, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 71.52657087, 0.01686768, 71.52657087, 0.05060305, 50.06859961, -904.72531551, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 17.88164272, 8.327e-05, 53.64492815, 0.0002498, 178.81642717, 0.00083267, -17.88164272, -8.327e-05, -53.64492815, -0.0002498, -178.81642717, -0.00083267, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 71.52657087, 0.01686768, 71.52657087, 0.05060305, 50.06859961, -904.72531551, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 17.88164272, 8.327e-05, 53.64492815, 0.0002498, 178.81642717, 0.00083267, -17.88164272, -8.327e-05, -53.64492815, -0.0002498, -178.81642717, -0.00083267, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 4.5, 13.5, 6.15)
    ops.node(123020, 4.5, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1225, 27552701.81754821, 11480292.42397842, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 86.47437033, 0.00065423, 104.16358352, 0.01728424, 10.41635835, 0.04837282, -86.47437033, -0.00065423, -104.16358352, -0.01728424, -10.41635835, -0.04837282, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 78.96021866, 0.00065423, 95.1123356, 0.01728424, 9.51123356, 0.04837282, -78.96021866, -0.00065423, -95.1123356, -0.01728424, -9.51123356, -0.04837282, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 122.06871906, 0.01308464, 122.06871906, 0.03925391, 85.44810334, -1348.73597772, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 30.51717976, 7.291e-05, 91.55153929, 0.00021873, 305.17179764, 0.00072911, -30.51717976, -7.291e-05, -91.55153929, -0.00021873, -305.17179764, -0.00072911, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 122.06871906, 0.01308464, 122.06871906, 0.03925391, 85.44810334, -1348.73597772, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 30.51717976, 7.291e-05, 91.55153929, 0.00021873, 305.17179764, 0.00072911, -30.51717976, -7.291e-05, -91.55153929, -0.00021873, -305.17179764, -0.00072911, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.15)
    ops.node(123021, 9.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 27406442.89243533, 11419351.20518139, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 47.34995956, 0.0009136, 56.36816243, 0.01723485, 5.63681624, 0.04528045, -47.34995956, -0.0009136, -56.36816243, -0.01723485, -5.63681624, -0.04528045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 52.66784922, 0.0009136, 62.69888944, 0.01723485, 6.26988894, 0.04528045, -52.66784922, -0.0009136, -62.69888944, -0.01723485, -6.26988894, -0.04528045, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 77.49013501, 0.01827204, 77.49013501, 0.05481612, 54.24309451, -1041.11629778, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 19.37253375, 9.12e-05, 58.11760126, 0.00027361, 193.72533753, 0.00091202, -19.37253375, -9.12e-05, -58.11760126, -0.00027361, -193.72533753, -0.00091202, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 77.49013501, 0.01827204, 77.49013501, 0.05481612, 54.24309451, -1041.11629778, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 19.37253375, 9.12e-05, 58.11760126, 0.00027361, 193.72533753, 0.00091202, -19.37253375, -9.12e-05, -58.11760126, -0.00027361, -193.72533753, -0.00091202, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.15)
    ops.node(123022, 12.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0625, 26232237.80671642, 10930099.08613184, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 46.89559859, 0.00093633, 55.72004326, 0.01615221, 5.57200433, 0.04061377, -46.89559859, -0.00093633, -55.72004326, -0.01615221, -5.57200433, -0.04061377, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 52.06071698, 0.00093633, 61.85709297, 0.01615221, 6.1857093, 0.04061377, -52.06071698, -0.00093633, -61.85709297, -0.01615221, -6.1857093, -0.04061377, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 74.33552875, 0.01872658, 74.33552875, 0.05617973, 52.03487013, -1023.20278345, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 18.58388219, 9.141e-05, 55.75164656, 0.00027422, 185.83882188, 0.00091405, -18.58388219, -9.141e-05, -55.75164656, -0.00027422, -185.83882188, -0.00091405, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 74.33552875, 0.01872658, 74.33552875, 0.05617973, 52.03487013, -1023.20278345, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 18.58388219, 9.141e-05, 55.75164656, 0.00027422, 185.83882188, 0.00091405, -18.58388219, -9.141e-05, -55.75164656, -0.00027422, -185.83882188, -0.00091405, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 16.5, 13.5, 6.15)
    ops.node(123023, 16.5, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 26956901.5582561, 11232042.31594004, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 87.14030907, 0.00064346, 104.97770011, 0.01695515, 10.49777001, 0.04687134, -87.14030907, -0.00064346, -104.97770011, -0.01695515, -10.49777001, -0.04687134, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 79.06526935, 0.00064346, 95.2497211, 0.01695515, 9.52497211, 0.04687134, -79.06526935, -0.00064346, -95.2497211, -0.01695515, -9.52497211, -0.04687134, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 119.52588124, 0.01286917, 119.52588124, 0.03860752, 83.66811686, -1340.46531347, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 29.88147031, 7.297e-05, 89.64441093, 0.00021891, 298.81470309, 0.0007297, -29.88147031, -7.297e-05, -89.64441093, -0.00021891, -298.81470309, -0.0007297, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 119.52588124, 0.01286917, 119.52588124, 0.03860752, 83.66811686, -1340.46531347, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 29.88147031, 7.297e-05, 89.64441093, 0.00021891, 298.81470309, 0.0007297, -29.88147031, -7.297e-05, -89.64441093, -0.00021891, -298.81470309, -0.0007297, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.15)
    ops.node(123024, 21.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 28020785.52828126, 11675327.30345052, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 33.24476243, 0.00081874, 39.95022757, 0.01883864, 3.99502276, 0.05765517, -33.24476243, -0.00081874, -39.95022757, -0.01883864, -3.99502276, -0.05765517, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 33.24476243, 0.00081874, 39.95022757, 0.01883864, 3.99502276, 0.05765517, -33.24476243, -0.00081874, -39.95022757, -0.01883864, -3.99502276, -0.05765517, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 72.02750046, 0.01637486, 72.02750046, 0.04912457, 50.41925032, -901.90438668, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 18.00687512, 8.291e-05, 54.02062535, 0.00024874, 180.06875115, 0.00082914, -18.00687512, -8.291e-05, -54.02062535, -0.00024874, -180.06875115, -0.00082914, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 72.02750046, 0.01637486, 72.02750046, 0.04912457, 50.41925032, -901.90438668, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 18.00687512, 8.291e-05, 54.02062535, 0.00024874, 180.06875115, 0.00082914, -18.00687512, -8.291e-05, -54.02062535, -0.00024874, -180.06875115, -0.00082914, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.95)
    ops.node(124001, 0.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 26106585.30467727, 10877743.87694887, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 19.94017727, 0.00081319, 24.30871391, 0.02239182, 2.43087139, 0.07456873, -19.94017727, -0.00081319, -24.30871391, -0.02239182, -2.43087139, -0.07456873, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 19.94017727, 0.00081319, 24.30871391, 0.02239182, 2.43087139, 0.07456873, -19.94017727, -0.00081319, -24.30871391, -0.02239182, -2.43087139, -0.07456873, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 59.3112467, 0.01626375, 59.3112467, 0.04879124, 41.51787269, -927.75805747, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 14.82781168, 7.328e-05, 44.48343503, 0.00021985, 148.27811675, 0.00073282, -14.82781168, -7.328e-05, -44.48343503, -0.00021985, -148.27811675, -0.00073282, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 59.3112467, 0.01626375, 59.3112467, 0.04879124, 41.51787269, -927.75805747, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 14.82781168, 7.328e-05, 44.48343503, 0.00021985, 148.27811675, 0.00073282, -14.82781168, -7.328e-05, -44.48343503, -0.00021985, -148.27811675, -0.00073282, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.5, 0.0, 8.95)
    ops.node(124002, 4.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1225, 26842956.52266024, 11184565.2177751, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 51.05935015, 0.00059154, 62.19331711, 0.01996021, 6.21933171, 0.06120189, -51.05935015, -0.00059154, -62.19331711, -0.01996021, -6.21933171, -0.06120189, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 58.20129815, 0.00059154, 70.89263341, 0.01996021, 7.08926334, 0.06120189, -58.20129815, -0.00059154, -70.89263341, -0.01996021, -7.08926334, -0.06120189, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 103.66714314, 0.01183072, 103.66714314, 0.03549215, 72.5670002, -1207.23803732, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 25.91678579, 6.356e-05, 77.75035736, 0.00019067, 259.16785786, 0.00063557, -25.91678579, -6.356e-05, -77.75035736, -0.00019067, -259.16785786, -0.00063557, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 103.66714314, 0.01183072, 103.66714314, 0.03549215, 72.5670002, -1207.23803732, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 25.91678579, 6.356e-05, 77.75035736, 0.00019067, 259.16785786, 0.00063557, -25.91678579, -6.356e-05, -77.75035736, -0.00019067, -259.16785786, -0.00063557, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.5, 0.0, 8.95)
    ops.node(124005, 16.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 27388082.48513245, 11411701.03547185, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 51.67998659, 0.00058865, 62.90036279, 0.01976431, 6.29003628, 0.06161438, -51.67998659, -0.00058865, -62.90036279, -0.01976431, -6.29003628, -0.06161438, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 59.09121128, 0.00058865, 71.92065774, 0.01976431, 7.19206577, 0.06161438, -59.09121128, -0.00058865, -71.92065774, -0.01976431, -7.19206577, -0.06161438, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 104.54351904, 0.01177292, 104.54351904, 0.03531875, 73.18046333, -1170.53913649, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 26.13587976, 6.282e-05, 78.40763928, 0.00018846, 261.35879761, 0.00062819, -26.13587976, -6.282e-05, -78.40763928, -0.00018846, -261.35879761, -0.00062819, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 104.54351904, 0.01177292, 104.54351904, 0.03531875, 73.18046333, -1170.53913649, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 26.13587976, 6.282e-05, 78.40763928, 0.00018846, 261.35879761, 0.00062819, -26.13587976, -6.282e-05, -78.40763928, -0.00018846, -261.35879761, -0.00062819, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 21.0, 0.0, 8.95)
    ops.node(124006, 21.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 27951067.20068721, 11646278.00028634, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 20.33271928, 0.00077436, 24.72383401, 0.02245158, 2.4723834, 0.07734332, -20.33271928, -0.00077436, -24.72383401, -0.02245158, -2.4723834, -0.07734332, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 20.33271928, 0.00077436, 24.72383401, 0.02245158, 2.4723834, 0.07734332, -20.33271928, -0.00077436, -24.72383401, -0.02245158, -2.4723834, -0.07734332, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 62.2961223, 0.01548712, 62.2961223, 0.04646137, 43.60728561, -915.95493557, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 15.57403058, 7.189e-05, 46.72209173, 0.00021567, 155.74030575, 0.00071891, -15.57403058, -7.189e-05, -46.72209173, -0.00021567, -155.74030575, -0.00071891, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 62.2961223, 0.01548712, 62.2961223, 0.04646137, 43.60728561, -915.95493557, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 15.57403058, 7.189e-05, 46.72209173, 0.00021567, 155.74030575, 0.00071891, -15.57403058, -7.189e-05, -46.72209173, -0.00021567, -155.74030575, -0.00071891, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 8.95)
    ops.node(124007, 0.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 26591556.82590693, 11079815.34412789, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 58.52092489, 0.00059058, 71.30284997, 0.02004362, 7.130285, 0.060952, -58.52092489, -0.00059058, -71.30284997, -0.02004362, -7.130285, -0.060952, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 51.23865282, 0.00059058, 62.43001082, 0.02004362, 6.24300108, 0.060952, -51.23865282, -0.00059058, -62.43001082, -0.02004362, -6.24300108, -0.060952, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 102.27286858, 0.01181151, 102.27286858, 0.03543452, 71.591008, -1185.64918785, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 25.56821714, 6.33e-05, 76.70465143, 0.00018989, 255.68217144, 0.00063295, -25.56821714, -6.33e-05, -76.70465143, -0.00018989, -255.68217144, -0.00063295, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 102.27286858, 0.01181151, 102.27286858, 0.03543452, 71.591008, -1185.64918785, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 25.56821714, 6.33e-05, 76.70465143, 0.00018989, 255.68217144, 0.00063295, -25.56821714, -6.33e-05, -76.70465143, -0.00018989, -255.68217144, -0.00063295, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.5, 4.5, 8.95)
    ops.node(124008, 4.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.16, 25090835.0619092, 10454514.60912883, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 97.97936826, 0.00060507, 119.23740052, 0.01632055, 11.92374005, 0.04034733, -97.97936826, -0.00060507, -119.23740052, -0.01632055, -11.92374005, -0.04034733, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 97.97936826, 0.00060507, 119.23740052, 0.01632055, 11.92374005, 0.04034733, -97.97936826, -0.00060507, -119.23740052, -0.01632055, -11.92374005, -0.04034733, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 110.46742348, 0.01210133, 110.46742348, 0.03630398, 77.32719643, -946.87685099, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 27.61685587, 5.547e-05, 82.85056761, 0.00016642, 276.16855869, 0.00055474, -27.61685587, -5.547e-05, -82.85056761, -0.00016642, -276.16855869, -0.00055474, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 110.46742348, 0.01210133, 110.46742348, 0.03630398, 77.32719643, -946.87685099, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 27.61685587, 5.547e-05, 82.85056761, 0.00016642, 276.16855869, 0.00055474, -27.61685587, -5.547e-05, -82.85056761, -0.00016642, -276.16855869, -0.00055474, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.0, 4.5, 8.95)
    ops.node(124009, 9.0, 4.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 27715689.11378571, 11548203.79741071, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 66.84084967, 0.00060713, 81.09432357, 0.01930924, 8.10943236, 0.05827991, -66.84084967, -0.00060713, -81.09432357, -0.01930924, -8.10943236, -0.05827991, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 59.36829645, 0.00060713, 72.02828609, 0.01930924, 7.20282861, 0.05827991, -59.36829645, -0.00060713, -72.02828609, -0.01930924, -7.20282861, -0.05827991, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 111.48852366, 0.01214267, 111.48852366, 0.03642801, 78.04196656, -1205.55505856, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 27.87213092, 6.62e-05, 83.61639275, 0.0001986, 278.72130916, 0.000662, -27.87213092, -6.62e-05, -83.61639275, -0.0001986, -278.72130916, -0.000662, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 111.48852366, 0.01214267, 111.48852366, 0.03642801, 78.04196656, -1205.55505856, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 27.87213092, 6.62e-05, 83.61639275, 0.0001986, 278.72130916, 0.000662, -27.87213092, -6.62e-05, -83.61639275, -0.0001986, -278.72130916, -0.000662, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.0, 4.5, 8.95)
    ops.node(124010, 12.0, 4.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 27581499.36750476, 11492291.40312698, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 66.09563199, 0.00060125, 80.20400432, 0.01950889, 8.02040043, 0.05830038, -66.09563199, -0.00060125, -80.20400432, -0.01950889, -8.02040043, -0.05830038, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 58.75614145, 0.00060125, 71.29787069, 0.01950889, 7.12978707, 0.05830038, -58.75614145, -0.00060125, -71.29787069, -0.01950889, -7.12978707, -0.05830038, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 110.94391856, 0.01202491, 110.94391856, 0.03607473, 77.66074299, -1203.45703486, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 27.73597964, 6.62e-05, 83.20793892, 0.00019859, 277.35979641, 0.00066197, -27.73597964, -6.62e-05, -83.20793892, -0.00019859, -277.35979641, -0.00066197, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 110.94391856, 0.01202491, 110.94391856, 0.03607473, 77.66074299, -1203.45703486, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 27.73597964, 6.62e-05, 83.20793892, 0.00019859, 277.35979641, 0.00066197, -27.73597964, -6.62e-05, -83.20793892, -0.00019859, -277.35979641, -0.00066197, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 16.5, 4.5, 8.95)
    ops.node(124011, 16.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.16, 27348439.74072105, 11395183.22530044, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 100.9292827, 0.00057948, 122.60330137, 0.01630526, 12.26033014, 0.04260883, -100.9292827, -0.00057948, -122.60330137, -0.01630526, -12.26033014, -0.04260883, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 100.9292827, 0.00057948, 122.60330137, 0.01630526, 12.26033014, 0.04260883, -100.9292827, -0.00057948, -122.60330137, -0.01630526, -12.26033014, -0.04260883, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 120.23812534, 0.01158962, 120.23812534, 0.03476885, 84.16668774, -938.09276787, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 30.05953133, 5.54e-05, 90.178594, 0.00016619, 300.59531335, 0.00055396, -30.05953133, -5.54e-05, -90.178594, -0.00016619, -300.59531335, -0.00055396, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 120.23812534, 0.01158962, 120.23812534, 0.03476885, 84.16668774, -938.09276787, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 30.05953133, 5.54e-05, 90.178594, 0.00016619, 300.59531335, 0.00055396, -30.05953133, -5.54e-05, -90.178594, -0.00016619, -300.59531335, -0.00055396, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 8.95)
    ops.node(124012, 21.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 26522495.82934444, 11051039.92889352, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 57.62282719, 0.00059353, 70.21454436, 0.02022732, 7.02145444, 0.06105244, -57.62282719, -0.00059353, -70.21454436, -0.02022732, -7.02145444, -0.06105244, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 50.68399619, 0.00059353, 61.75944279, 0.02022732, 6.17594428, 0.06105244, -50.68399619, -0.00059353, -61.75944279, -0.02022732, -6.17594428, -0.06105244, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 102.79667129, 0.01187066, 102.79667129, 0.03561199, 71.9576699, -1213.35658089, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 25.69916782, 6.379e-05, 77.09750347, 0.00019136, 256.99167822, 0.00063785, -25.69916782, -6.379e-05, -77.09750347, -0.00019136, -256.99167822, -0.00063785, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 102.79667129, 0.01187066, 102.79667129, 0.03561199, 71.9576699, -1213.35658089, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 25.69916782, 6.379e-05, 77.09750347, 0.00019136, 256.99167822, 0.00063785, -25.69916782, -6.379e-05, -77.09750347, -0.00019136, -256.99167822, -0.00063785, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.0, 8.95)
    ops.node(124013, 0.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.1225, 28278733.56870843, 11782805.65362851, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 58.10049373, 0.00058881, 70.60804477, 0.02004523, 7.06080448, 0.06276768, -58.10049373, -0.00058881, -70.60804477, -0.02004523, -7.06080448, -0.06276768, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 51.17941097, 0.00058881, 62.19702981, 0.02004523, 6.21970298, 0.06276768, -51.17941097, -0.00058881, -62.19702981, -0.02004523, -6.21970298, -0.06276768, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 108.66410056, 0.01177625, 108.66410056, 0.03532875, 76.06487039, -1204.38226567, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 27.16602514, 6.324e-05, 81.49807542, 0.00018972, 271.6602514, 0.00063238, -27.16602514, -6.324e-05, -81.49807542, -0.00018972, -271.6602514, -0.00063238, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 108.66410056, 0.01177625, 108.66410056, 0.03532875, 76.06487039, -1204.38226567, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 27.16602514, 6.324e-05, 81.49807542, 0.00018972, 271.6602514, 0.00063238, -27.16602514, -6.324e-05, -81.49807542, -0.00018972, -271.6602514, -0.00063238, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.5, 9.0, 8.95)
    ops.node(124014, 4.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.16, 26899858.36208466, 11208274.31753528, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 96.53493238, 0.00059421, 117.32715254, 0.01675656, 11.73271525, 0.04265753, -96.53493238, -0.00059421, -117.32715254, -0.01675656, -11.73271525, -0.04265753, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 96.53493238, 0.00059421, 117.32715254, 0.01675656, 11.73271525, 0.04265753, -96.53493238, -0.00059421, -117.32715254, -0.01675656, -11.73271525, -0.04265753, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 118.65072425, 0.0118843, 118.65072425, 0.03565289, 83.05550698, -949.69333374, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 29.66268106, 5.558e-05, 88.98804319, 0.00016673, 296.62681063, 0.00055576, -29.66268106, -5.558e-05, -88.98804319, -0.00016673, -296.62681063, -0.00055576, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 118.65072425, 0.0118843, 118.65072425, 0.03565289, 83.05550698, -949.69333374, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 29.66268106, 5.558e-05, 88.98804319, 0.00016673, 296.62681063, 0.00055576, -29.66268106, -5.558e-05, -88.98804319, -0.00016673, -296.62681063, -0.00055576, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 9.0, 8.95)
    ops.node(124015, 9.0, 9.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 27678370.32265912, 11532654.30110797, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 67.3822404, 0.00061054, 81.71017522, 0.01897954, 8.17101752, 0.05726766, -67.3822404, -0.00061054, -81.71017522, -0.01897954, -8.17101752, -0.05726766, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 60.22882901, 0.00061054, 73.0356863, 0.01897954, 7.30356863, 0.05726766, -60.22882901, -0.00061054, -73.0356863, -0.01897954, -7.30356863, -0.05726766, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 111.32957294, 0.01221085, 111.32957294, 0.03663256, 77.93070106, -1182.5065622, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 27.83239323, 6.619e-05, 83.4971797, 0.00019858, 278.32393235, 0.00066195, -27.83239323, -6.619e-05, -83.4971797, -0.00019858, -278.32393235, -0.00066195, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 111.32957294, 0.01221085, 111.32957294, 0.03663256, 77.93070106, -1182.5065622, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 27.83239323, 6.619e-05, 83.4971797, 0.00019858, 278.32393235, 0.00066195, -27.83239323, -6.619e-05, -83.4971797, -0.00019858, -278.32393235, -0.00066195, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.0, 9.0, 8.95)
    ops.node(124016, 12.0, 9.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1225, 25783029.20447534, 10742928.83519806, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 68.61513043, 0.00061085, 83.33701798, 0.01853077, 8.3337018, 0.05387215, -68.61513043, -0.00061085, -83.33701798, -0.01853077, -8.3337018, -0.05387215, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 60.70145166, 0.00061085, 73.72540046, 0.01853077, 7.37254005, 0.05387215, -60.70145166, -0.00061085, -73.72540046, -0.01853077, -7.37254005, -0.05387215, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 105.24502802, 0.01221705, 105.24502802, 0.03665114, 73.67151961, -1199.02947711, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 26.31125701, 6.718e-05, 78.93377102, 0.00020153, 263.11257005, 0.00067177, -26.31125701, -6.718e-05, -78.93377102, -0.00020153, -263.11257005, -0.00067177, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 105.24502802, 0.01221705, 105.24502802, 0.03665114, 73.67151961, -1199.02947711, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 26.31125701, 6.718e-05, 78.93377102, 0.00020153, 263.11257005, 0.00067177, -26.31125701, -6.718e-05, -78.93377102, -0.00020153, -263.11257005, -0.00067177, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 16.5, 9.0, 8.95)
    ops.node(124017, 16.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.16, 27249964.79293175, 11354151.9970549, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 100.09013547, 0.00059408, 121.59883381, 0.01661433, 12.15988338, 0.04283145, -100.09013547, -0.00059408, -121.59883381, -0.01661433, -12.15988338, -0.04283145, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 100.09013547, 0.00059408, 121.59883381, 0.01661433, 12.15988338, 0.04283145, -100.09013547, -0.00059408, -121.59883381, -0.01661433, -12.15988338, -0.04283145, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 120.13633007, 0.01188156, 120.13633007, 0.03564469, 84.09543105, -946.8545453, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 30.03408252, 5.555e-05, 90.10224755, 0.00016665, 300.34082518, 0.00055549, -30.03408252, -5.555e-05, -90.10224755, -0.00016665, -300.34082518, -0.00055549, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 120.13633007, 0.01188156, 120.13633007, 0.03564469, 84.09543105, -946.8545453, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 30.03408252, 5.555e-05, 90.10224755, 0.00016665, 300.34082518, 0.00055549, -30.03408252, -5.555e-05, -90.10224755, -0.00016665, -300.34082518, -0.00055549, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 21.0, 9.0, 8.95)
    ops.node(124018, 21.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1225, 26303059.90471404, 10959608.29363085, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 58.35260472, 0.00059785, 71.12213873, 0.0202869, 7.11221387, 0.06084228, -58.35260472, -0.00059785, -71.12213873, -0.0202869, -7.11221387, -0.06084228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 51.20047528, 0.00059785, 62.40488017, 0.0202869, 6.24048802, 0.06084228, -51.20047528, -0.00059785, -62.40488017, -0.0202869, -6.24048802, -0.06084228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 101.88420748, 0.01195704, 101.88420748, 0.03587111, 71.31894524, -1207.29967502, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 25.47105187, 6.375e-05, 76.41315561, 0.00019124, 254.7105187, 0.00063746, -25.47105187, -6.375e-05, -76.41315561, -0.00019124, -254.7105187, -0.00063746, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 101.88420748, 0.01195704, 101.88420748, 0.03587111, 71.31894524, -1207.29967502, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 25.47105187, 6.375e-05, 76.41315561, 0.00019124, 254.7105187, 0.00063746, -25.47105187, -6.375e-05, -76.41315561, -0.00019124, -254.7105187, -0.00063746, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 13.5, 8.95)
    ops.node(124019, 0.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 27031581.40423301, 11263158.91843042, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 19.9138054, 0.00080701, 24.24897414, 0.02263661, 2.42489741, 0.07625808, -19.9138054, -0.00080701, -24.24897414, -0.02263661, -2.42489741, -0.07625808, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 19.9138054, 0.00080701, 24.24897414, 0.02263661, 2.42489741, 0.07625808, -19.9138054, -0.00080701, -24.24897414, -0.02263661, -2.42489741, -0.07625808, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 60.45633503, 0.01614013, 60.45633503, 0.04842038, 42.31943452, -906.89789718, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 15.11408376, 7.214e-05, 45.34225128, 0.00021642, 151.14083759, 0.00072141, -15.11408376, -7.214e-05, -45.34225128, -0.00021642, -151.14083759, -0.00072141, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 60.45633503, 0.01614013, 60.45633503, 0.04842038, 42.31943452, -906.89789718, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 15.11408376, 7.214e-05, 45.34225128, 0.00021642, 151.14083759, 0.00072141, -15.11408376, -7.214e-05, -45.34225128, -0.00021642, -151.14083759, -0.00072141, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 4.5, 13.5, 8.95)
    ops.node(124020, 4.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1225, 26984222.45498868, 11243426.02291195, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 51.05057285, 0.00058683, 62.17070973, 0.01974394, 6.21707097, 0.06114754, -51.05057285, -0.00058683, -62.17070973, -0.01974394, -6.21707097, -0.06114754, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 58.27214585, 0.00058683, 70.96532835, 0.01974394, 7.09653283, 0.06114754, -58.27214585, -0.00058683, -70.96532835, -0.01974394, -7.09653283, -0.06114754, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 103.78945961, 0.01173658, 103.78945961, 0.03520975, 72.65262173, -1193.92963325, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 25.9473649, 6.33e-05, 77.84209471, 0.0001899, 259.47364903, 0.00063299, -25.9473649, -6.33e-05, -77.84209471, -0.0001899, -259.47364903, -0.00063299, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 103.78945961, 0.01173658, 103.78945961, 0.03520975, 72.65262173, -1193.92963325, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 25.9473649, 6.33e-05, 77.84209471, 0.0001899, 259.47364903, 0.00063299, -25.9473649, -6.33e-05, -77.84209471, -0.0001899, -259.47364903, -0.00063299, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 8.95)
    ops.node(124021, 9.0, 13.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 27376815.42528432, 11407006.4272018, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 28.89063486, 0.00080769, 34.99157804, 0.02159456, 3.4991578, 0.06839886, -28.89063486, -0.00080769, -34.99157804, -0.02159456, -3.4991578, -0.06839886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 31.2205615, 0.00080769, 37.81352397, 0.02159456, 3.7813524, 0.06839886, -31.2205615, -0.00080769, -37.81352397, -0.02159456, -3.7813524, -0.06839886, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 65.91089065, 0.01615377, 65.91089065, 0.0484613, 46.13762346, -874.97068642, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 16.47772266, 7.766e-05, 49.43316799, 0.00023297, 164.77722663, 0.00077658, -16.47772266, -7.766e-05, -49.43316799, -0.00023297, -164.77722663, -0.00077658, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 65.91089065, 0.01615377, 65.91089065, 0.0484613, 46.13762346, -874.97068642, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 16.47772266, 7.766e-05, 49.43316799, 0.00023297, 164.77722663, 0.00077658, -16.47772266, -7.766e-05, -49.43316799, -0.00023297, -164.77722663, -0.00077658, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 8.95)
    ops.node(124022, 12.0, 13.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0625, 27988215.76168216, 11661756.56736757, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 28.97390176, 0.00080682, 35.069931, 0.02149044, 3.5069931, 0.06949891, -28.97390176, -0.00080682, -35.069931, -0.02149044, -3.5069931, -0.06949891, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 31.28287801, 0.00080682, 37.8647095, 0.02149044, 3.78647095, 0.06949891, -31.28287801, -0.00080682, -37.8647095, -0.02149044, -3.78647095, -0.06949891, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 66.1938439, 0.01613641, 66.1938439, 0.04840922, 46.33569073, -846.93281989, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 16.54846098, 7.629e-05, 49.64538293, 0.00022886, 165.48460975, 0.00076287, -16.54846098, -7.629e-05, -49.64538293, -0.00022886, -165.48460975, -0.00076287, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 66.1938439, 0.01613641, 66.1938439, 0.04840922, 46.33569073, -846.93281989, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 16.54846098, 7.629e-05, 49.64538293, 0.00022886, 165.48460975, 0.00076287, -16.54846098, -7.629e-05, -49.64538293, -0.00022886, -165.48460975, -0.00076287, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 16.5, 13.5, 8.95)
    ops.node(124023, 16.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 27822591.95492088, 11592746.6478837, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 50.8304866, 0.00058454, 61.82361878, 0.01974341, 6.18236188, 0.06204789, -50.8304866, -0.00058454, -61.82361878, -0.01974341, -6.18236188, -0.06204789, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 57.81090379, 0.00058454, 70.31369393, 0.01974341, 7.03136939, 0.06204789, -57.81090379, -0.00058454, -70.31369393, -0.01974341, -7.03136939, -0.06204789, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 104.4936725, 0.01169076, 104.4936725, 0.03507229, 73.14557075, -1114.59359785, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 26.12341813, 6.181e-05, 78.37025438, 0.00018542, 261.23418126, 0.00061808, -26.12341813, -6.181e-05, -78.37025438, -0.00018542, -261.23418126, -0.00061808, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 104.4936725, 0.01169076, 104.4936725, 0.03507229, 73.14557075, -1114.59359785, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 26.12341813, 6.181e-05, 78.37025438, 0.00018542, 261.23418126, 0.00061808, -26.12341813, -6.181e-05, -78.37025438, -0.00018542, -261.23418126, -0.00061808, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 21.0, 13.5, 8.95)
    ops.node(124024, 21.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 26362405.82806616, 10984335.76169423, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 20.35369542, 0.00074987, 24.80578434, 0.0226711, 2.48057843, 0.07526555, -20.35369542, -0.00074987, -24.80578434, -0.0226711, -2.48057843, -0.07526555, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 20.35369542, 0.00074987, 24.80578434, 0.0226711, 2.48057843, 0.07526555, -20.35369542, -0.00074987, -24.80578434, -0.0226711, -2.48057843, -0.07526555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 59.59742961, 0.01499732, 59.59742961, 0.04499195, 41.71820072, -920.75093493, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 14.8993574, 7.292e-05, 44.6980722, 0.00021876, 148.99357402, 0.00072921, -14.8993574, -7.292e-05, -44.6980722, -0.00021876, -148.99357402, -0.00072921, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 59.59742961, 0.01499732, 59.59742961, 0.04499195, 41.71820072, -920.75093493, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 14.8993574, 7.292e-05, 44.6980722, 0.00021876, 148.99357402, 0.00072921, -14.8993574, -7.292e-05, -44.6980722, -0.00021876, -148.99357402, -0.00072921, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(124025, 9.0, 0.0, 1.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.1225, 26405404.39190637, 11002251.82996099, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 113.04581684, 0.00057617, 134.12454229, 0.01346265, 13.41245423, 0.03176224, -113.04581684, -0.00057617, -134.12454229, -0.01346265, -13.41245423, -0.03176224, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 122.25901769, 0.00057617, 145.05565306, 0.01346265, 14.50556531, 0.03176224, -122.25901769, -0.00057617, -145.05565306, -0.01346265, -14.50556531, -0.03176224, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 179.85572976, 0.01152345, 179.85572976, 0.03457034, 125.89901083, -3208.65962772, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 44.96393244, 6.205e-05, 134.89179732, 0.00018616, 449.6393244, 0.00062053, -44.96393244, -6.205e-05, -134.89179732, -0.00018616, -449.6393244, -0.00062053, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 179.85572976, 0.01152345, 179.85572976, 0.03457034, 125.89901083, -3208.65962772, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 44.96393244, 6.205e-05, 134.89179732, 0.00018616, 449.6393244, 0.00062053, -44.96393244, -6.205e-05, -134.89179732, -0.00018616, -449.6393244, -0.00062053, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.775)
    ops.node(121003, 9.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.1225, 25422002.01762319, 10592500.84067633, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 116.04421478, 0.00057294, 137.68404144, 0.0133737, 13.76840414, 0.03059119, -116.04421478, -0.00057294, -137.68404144, -0.0133737, -13.76840414, -0.03059119, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 120.73971475, 0.00057294, 143.25515425, 0.0133737, 14.32551543, 0.03059119, -120.73971475, -0.00057294, -143.25515425, -0.0133737, -14.32551543, -0.03059119, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 170.09300423, 0.01145886, 170.09300423, 0.03437657, 119.06510296, -3062.05288482, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 42.52325106, 6.095e-05, 127.56975317, 0.00018286, 425.23251058, 0.00060954, -42.52325106, -6.095e-05, -127.56975317, -0.00018286, -425.23251058, -0.00060954, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 170.09300423, 0.01145886, 170.09300423, 0.03437657, 119.06510296, -3062.05288482, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 42.52325106, 6.095e-05, 127.56975317, 0.00018286, 425.23251058, 0.00060954, -42.52325106, -6.095e-05, -127.56975317, -0.00018286, -425.23251058, -0.00060954, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.0, 0.0, 0.0)
    ops.node(124026, 12.0, 0.0, 1.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.1225, 27150015.24173502, 11312506.35072293, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 113.55666321, 0.00056936, 134.91953025, 0.01373408, 13.49195302, 0.03379586, -113.55666321, -0.00056936, -134.91953025, -0.01373408, -13.49195302, -0.03379586, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 122.89093597, 0.00056936, 146.0098147, 0.01373408, 14.60098147, 0.03379586, -122.89093597, -0.00056936, -146.0098147, -0.01373408, -14.60098147, -0.03379586, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 183.30924628, 0.01138714, 183.30924628, 0.03416142, 128.3164724, -3174.95605186, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 45.82731157, 6.151e-05, 137.48193471, 0.00018453, 458.27311571, 0.0006151, -45.82731157, -6.151e-05, -137.48193471, -0.00018453, -458.27311571, -0.0006151, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 183.30924628, 0.01138714, 183.30924628, 0.03416142, 128.3164724, -3174.95605186, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 45.82731157, 6.151e-05, 137.48193471, 0.00018453, 458.27311571, 0.0006151, -45.82731157, -6.151e-05, -137.48193471, -0.00018453, -458.27311571, -0.0006151, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.775)
    ops.node(121004, 12.0, 0.0, 2.85)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.1225, 26657018.3080194, 11107090.96167475, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 116.43772095, 0.00056908, 138.53529531, 0.01389092, 13.85352953, 0.03411203, -116.43772095, -0.00056908, -138.53529531, -0.01389092, -13.85352953, -0.03411203, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 120.9771054, 0.00056908, 143.93616507, 0.01389092, 14.39361651, 0.03411203, -120.9771054, -0.00056908, -143.93616507, -0.01389092, -14.39361651, -0.03411203, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 175.98874902, 0.01138163, 175.98874902, 0.0341449, 123.19212431, -3018.45122028, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 43.99718725, 6.015e-05, 131.99156176, 0.00018044, 439.97187254, 0.00060145, -43.99718725, -6.015e-05, -131.99156176, -0.00018044, -439.97187254, -0.00060145, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 175.98874902, 0.01138163, 175.98874902, 0.0341449, 123.19212431, -3018.45122028, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 43.99718725, 6.015e-05, 131.99156176, 0.00018044, 439.97187254, 0.00060145, -43.99718725, -6.015e-05, -131.99156176, -0.00018044, -439.97187254, -0.00060145, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.35)
    ops.node(124027, 9.0, 0.0, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.1225, 26711388.59547016, 11129745.24811256, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 92.60843827, 0.00053808, 110.91197535, 0.01534926, 11.09119753, 0.0400478, -92.60843827, -0.00053808, -110.91197535, -0.01534926, -11.09119753, -0.0400478, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 101.06442019, 0.00053808, 121.03923455, 0.01534926, 12.10392346, 0.0400478, -101.06442019, -0.00053808, -121.03923455, -0.01534926, -12.10392346, -0.0400478, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 180.12884363, 0.01076165, 180.12884363, 0.03228496, 126.09019054, -2990.05763227, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 45.03221091, 5.549e-05, 135.09663272, 0.00016647, 450.32210908, 0.0005549, -45.03221091, -5.549e-05, -135.09663272, -0.00016647, -450.32210908, -0.0005549, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 180.12884363, 0.01076165, 180.12884363, 0.03228496, 126.09019054, -2990.05763227, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 45.03221091, 5.549e-05, 135.09663272, 0.00016647, 450.32210908, 0.0005549, -45.03221091, -5.549e-05, -135.09663272, -0.00016647, -450.32210908, -0.0005549, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.725)
    ops.node(122003, 9.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.1225, 27446671.3110828, 11436113.0462845, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 88.13082651, 0.00053539, 105.81080036, 0.01625278, 10.58108004, 0.04422851, -88.13082651, -0.00053539, -105.81080036, -0.01625278, -10.58108004, -0.04422851, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 96.35743466, 0.00053539, 115.68775293, 0.01625278, 11.56877529, 0.04422851, -96.35743466, -0.00053539, -115.68775293, -0.01625278, -11.56877529, -0.04422851, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 180.97798498, 0.01070789, 180.97798498, 0.03212366, 126.68458948, -2900.38187064, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 45.24449624, 5.426e-05, 135.73348873, 0.00016277, 452.44496245, 0.00054258, -45.24449624, -5.426e-05, -135.73348873, -0.00016277, -452.44496245, -0.00054258, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 180.97798498, 0.01070789, 180.97798498, 0.03212366, 126.68458948, -2900.38187064, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 45.24449624, 5.426e-05, 135.73348873, 0.00016277, 452.44496245, 0.00054258, -45.24449624, -5.426e-05, -135.73348873, -0.00016277, -452.44496245, -0.00054258, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.35)
    ops.node(124028, 12.0, 0.0, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.1225, 26581815.53040947, 11075756.47100395, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 92.4792789, 0.00053761, 110.74451168, 0.01552756, 11.07445117, 0.03992978, -92.4792789, -0.00053761, -110.74451168, -0.01552756, -11.07445117, -0.03992978, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 100.9518247, 0.00053761, 120.89043798, 0.01552756, 12.0890438, 0.03992978, -100.9518247, -0.00053761, -120.89043798, -0.01552756, -12.0890438, -0.03992978, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 180.51259015, 0.01075214, 180.51259015, 0.03225642, 126.3588131, -3043.6680045, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 45.12814754, 5.588e-05, 135.38444261, 0.00016764, 451.28147537, 0.00055879, -45.12814754, -5.588e-05, -135.38444261, -0.00016764, -451.28147537, -0.00055879, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 180.51259015, 0.01075214, 180.51259015, 0.03225642, 126.3588131, -3043.6680045, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 45.12814754, 5.588e-05, 135.38444261, 0.00016764, 451.28147537, 0.00055879, -45.12814754, -5.588e-05, -135.38444261, -0.00016764, -451.28147537, -0.00055879, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.725)
    ops.node(122004, 12.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.1225, 27660153.34724265, 11525063.89468444, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 87.83271997, 0.00053479, 105.45388176, 0.0165506, 10.54538818, 0.04496774, -87.83271997, -0.00053479, -105.45388176, -0.0165506, -10.54538818, -0.04496774, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 95.83095917, 0.00053479, 115.05674242, 0.0165506, 11.50567424, 0.04496774, -95.83095917, -0.00053479, -115.05674242, -0.0165506, -11.50567424, -0.04496774, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 183.01466481, 0.01069577, 183.01466481, 0.03208731, 128.11026536, -2935.04922364, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 45.7536662, 5.444e-05, 137.2609986, 0.00016333, 457.53666201, 0.00054445, -45.7536662, -5.444e-05, -137.2609986, -0.00016333, -457.53666201, -0.00054445, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 183.01466481, 0.01069577, 183.01466481, 0.03208731, 128.11026536, -2935.04922364, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 45.7536662, 5.444e-05, 137.2609986, 0.00016333, 457.53666201, 0.00054445, -45.7536662, -5.444e-05, -137.2609986, -0.00016333, -457.53666201, -0.00054445, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.15)
    ops.node(124029, 9.0, 0.0, 7.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.0625, 26881539.53745082, 11200641.47393784, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 44.51142375, 0.00066485, 52.95845413, 0.01583545, 5.29584541, 0.04241478, -44.51142375, -0.00066485, -52.95845413, -0.01583545, -5.29584541, -0.04241478, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 47.07923346, 0.00066485, 56.01356272, 0.01583545, 5.60135627, 0.04241478, -47.07923346, -0.00066485, -56.01356272, -0.01583545, -5.60135627, -0.04241478, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 82.80281168, 0.01329708, 82.80281168, 0.03989124, 57.96196818, -2043.18101555, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 20.70070292, 4.968e-05, 62.10210876, 0.00014904, 207.00702921, 0.00049679, -20.70070292, -4.968e-05, -62.10210876, -0.00014904, -207.00702921, -0.00049679, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 82.80281168, 0.01329708, 82.80281168, 0.03989124, 57.96196818, -2043.18101555, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 20.70070292, 4.968e-05, 62.10210876, 0.00014904, 207.00702921, 0.00049679, -20.70070292, -4.968e-05, -62.10210876, -0.00014904, -207.00702921, -0.00049679, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.5)
    ops.node(123003, 9.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.0625, 26242168.98445798, 10934237.07685749, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 37.98446554, 0.00062895, 45.36123719, 0.01648008, 4.53612372, 0.0449461, -37.98446554, -0.00062895, -45.36123719, -0.01648008, -4.53612372, -0.0449461, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 37.98446554, 0.00062895, 45.36123719, 0.01648008, 4.53612372, 0.0449461, -37.98446554, -0.00062895, -45.36123719, -0.01648008, -4.53612372, -0.0449461, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 78.90908426, 0.01257897, 78.90908426, 0.0377369, 55.23635898, -1947.95770415, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 19.72727107, 4.85e-05, 59.1818132, 0.00014549, 197.27271065, 0.00048496, -19.72727107, -4.85e-05, -59.1818132, -0.00014549, -197.27271065, -0.00048496, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 78.90908426, 0.01257897, 78.90908426, 0.0377369, 55.23635898, -1947.95770415, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 19.72727107, 4.85e-05, 59.1818132, 0.00014549, 197.27271065, 0.00048496, -19.72727107, -4.85e-05, -59.1818132, -0.00014549, -197.27271065, -0.00048496, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.15)
    ops.node(124030, 12.0, 0.0, 7.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.0625, 27188326.80541951, 11328469.50225813, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 44.19265032, 0.0006729, 52.60238885, 0.01642525, 5.26023889, 0.04393175, -44.19265032, -0.0006729, -52.60238885, -0.01642525, -5.26023889, -0.04393175, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 46.54235772, 0.0006729, 55.39923904, 0.01642525, 5.5399239, 0.04393175, -46.54235772, -0.0006729, -55.39923904, -0.01642525, -5.5399239, -0.04393175, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 84.11507458, 0.01345794, 84.11507458, 0.04037382, 58.8805522, -2071.13084465, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 21.02876864, 4.99e-05, 63.08630593, 0.00014969, 210.28768644, 0.00049897, -21.02876864, -4.99e-05, -63.08630593, -0.00014969, -210.28768644, -0.00049897, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 84.11507458, 0.01345794, 84.11507458, 0.04037382, 58.8805522, -2071.13084465, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 21.02876864, 4.99e-05, 63.08630593, 0.00014969, 210.28768644, 0.00049897, -21.02876864, -4.99e-05, -63.08630593, -0.00014969, -210.28768644, -0.00049897, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.5)
    ops.node(123004, 12.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.0625, 25947705.68861183, 10811544.0369216, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 37.35893184, 0.00063362, 44.59312574, 0.01624322, 4.45931257, 0.04379128, -37.35893184, -0.00063362, -44.59312574, -0.01624322, -4.45931257, -0.04379128, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 37.35893184, 0.00063362, 44.59312574, 0.01624322, 4.45931257, 0.04379128, -37.35893184, -0.00063362, -44.59312574, -0.01624322, -4.45931257, -0.04379128, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 78.57216073, 0.01267233, 78.57216073, 0.03801699, 55.00051251, -1963.7837941, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 19.64304018, 4.884e-05, 58.92912055, 0.00014651, 196.43040183, 0.00048837, -19.64304018, -4.884e-05, -58.92912055, -0.00014651, -196.43040183, -0.00048837, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 78.57216073, 0.01267233, 78.57216073, 0.03801699, 55.00051251, -1963.7837941, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 19.64304018, 4.884e-05, 58.92912055, 0.00014651, 196.43040183, 0.00048837, -19.64304018, -4.884e-05, -58.92912055, -0.00014651, -196.43040183, -0.00048837, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 8.95)
    ops.node(124031, 9.0, 0.0, 9.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.0625, 27143555.57800379, 11309814.82416824, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 25.0535178, 0.00058934, 30.35633895, 0.02025011, 3.0356339, 0.0668477, -25.0535178, -0.00058934, -30.35633895, -0.02025011, -3.0356339, -0.0668477, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 25.0535178, 0.00058934, 30.35633895, 0.02025011, 3.0356339, 0.0668477, -25.0535178, -0.00058934, -30.35633895, -0.02025011, -3.0356339, -0.0668477, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 69.76333054, 0.01178677, 69.76333054, 0.0353603, 48.83433138, -1673.67689969, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 17.44083263, 4.145e-05, 52.3224979, 0.00012435, 174.40832635, 0.00041452, -17.44083263, -4.145e-05, -52.3224979, -0.00012435, -174.40832635, -0.00041452, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 69.76333054, 0.01178677, 69.76333054, 0.0353603, 48.83433138, -1673.67689969, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 17.44083263, 4.145e-05, 52.3224979, 0.00012435, 174.40832635, 0.00041452, -17.44083263, -4.145e-05, -52.3224979, -0.00012435, -174.40832635, -0.00041452, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 9.0, 0.0, 10.3)
    ops.node(124003, 9.0, 0.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.0625, 26277960.01272812, 10949150.00530338, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 21.19319014, 0.00055531, 25.81865239, 0.0222826, 2.58186524, 0.07397485, -21.19319014, -0.00055531, -25.81865239, -0.0222826, -2.58186524, -0.07397485, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 21.19319014, 0.00055531, 25.81865239, 0.0222826, 2.58186524, 0.07397485, -21.19319014, -0.00055531, -25.81865239, -0.0222826, -2.58186524, -0.07397485, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 64.2577521, 0.01110629, 64.2577521, 0.03331886, 44.98042647, -1779.42896598, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 16.06443802, 3.944e-05, 48.19331407, 0.00011831, 160.64438024, 0.00039438, -16.06443802, -3.944e-05, -48.19331407, -0.00011831, -160.64438024, -0.00039438, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 64.2577521, 0.01110629, 64.2577521, 0.03331886, 44.98042647, -1779.42896598, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 16.06443802, 3.944e-05, 48.19331407, 0.00011831, 160.64438024, 0.00039438, -16.06443802, -3.944e-05, -48.19331407, -0.00011831, -160.64438024, -0.00039438, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 8.95)
    ops.node(124032, 12.0, 0.0, 9.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.0625, 26868556.6169318, 11195231.92372158, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 25.00971363, 0.00058114, 30.30976056, 0.02043938, 3.03097606, 0.06645771, -25.00971363, -0.00058114, -30.30976056, -0.02043938, -3.03097606, -0.06645771, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 25.00971363, 0.00058114, 30.30976056, 0.02043938, 3.03097606, 0.06645771, -25.00971363, -0.00058114, -30.30976056, -0.02043938, -3.03097606, -0.06645771, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 69.17486991, 0.01162275, 69.17486991, 0.03486825, 48.42240893, -1672.42636562, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 17.29371748, 4.152e-05, 51.88115243, 0.00012457, 172.93717477, 0.00041523, -17.29371748, -4.152e-05, -51.88115243, -0.00012457, -172.93717477, -0.00041523, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 69.17486991, 0.01162275, 69.17486991, 0.03486825, 48.42240893, -1672.42636562, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 17.29371748, 4.152e-05, 51.88115243, 0.00012457, 172.93717477, 0.00041523, -17.29371748, -4.152e-05, -51.88115243, -0.00012457, -172.93717477, -0.00041523, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 12.0, 0.0, 10.3)
    ops.node(124004, 12.0, 0.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.0625, 26349437.50196258, 10978932.29248441, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 20.87020284, 0.0005662, 25.42321665, 0.02214731, 2.54232167, 0.07396017, -20.87020284, -0.0005662, -25.42321665, -0.02214731, -2.54232167, -0.07396017, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 20.87020284, 0.0005662, 25.42321665, 0.02214731, 2.54232167, 0.07396017, -20.87020284, -0.0005662, -25.42321665, -0.02214731, -2.54232167, -0.07396017, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 65.20576775, 0.01132399, 65.20576775, 0.03397196, 45.64403742, -1848.88838284, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 16.30144194, 3.991e-05, 48.90432581, 0.00011973, 163.01441937, 0.00039911, -16.30144194, -3.991e-05, -48.90432581, -0.00011973, -163.01441937, -0.00039911, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 65.20576775, 0.01132399, 65.20576775, 0.03397196, 45.64403742, -1848.88838284, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 16.30144194, 3.991e-05, 48.90432581, 0.00011973, 163.01441937, 0.00039911, -16.30144194, -3.991e-05, -48.90432581, -0.00011973, -163.01441937, -0.00039911, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
