import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 0.5)
    # Central joint node
    ops.node(4021, 0.0, 0.0, 1.75, '-mass', 3.1386977573904176, 3.1386977573904176, 3.1386977573904176, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34021, 0.15, 0.0, 1.75)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 0.0, 0.0, 1.55)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(74021, 0.0, 0.0, 1.95)
    ops.element('elasticBeamColumn', 74021, 4021, 74021, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 0.5)
    # Central joint node
    ops.node(4022, 2.9, 0.0, 1.75, '-mass', 3.202917940876656, 3.202917940876656, 3.202917940876656, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 2.75, 0.0, 1.75)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(24022, 2.9, 0.0, 1.55)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(74022, 2.9, 0.0, 1.95)
    ops.element('elasticBeamColumn', 74022, 4022, 74022, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 1.5)
    # Central joint node
    ops.node(4023, 0.0, 0.0, 4.95, '-mass', 2.9772298674821602, 2.9772298674821602, 2.9772298674821602, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34023, 0.15, 0.0, 4.95)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 0.0, 0.0, 4.775)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(74023, 0.0, 0.0, 5.125)
    ops.element('elasticBeamColumn', 74023, 4023, 74023, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 1.5)
    # Central joint node
    ops.node(4024, 2.9, 0.0, 4.95, '-mass', 3.0304408766564723, 3.0304408766564723, 3.0304408766564723, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 2.75, 0.0, 4.95)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 2.9, 0.0, 4.775)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(74024, 2.9, 0.0, 5.125)
    ops.element('elasticBeamColumn', 74024, 4024, 74024, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 2.5)
    # Central joint node
    ops.node(4025, 0.0, 0.0, 7.85, '-mass', 2.9328873598369003, 2.9328873598369003, 2.9328873598369003, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34025, 0.125, 0.0, 7.85)
    ops.element('elasticBeamColumn', 34025, 4025, 34025, 99999, 88888)
    ops.node(24025, 0.0, 0.0, 7.675)
    ops.element('elasticBeamColumn', 24025, 24025, 4025, 99999, 99999)
    ops.node(74025, 0.0, 0.0, 8.025)
    ops.element('elasticBeamColumn', 74025, 4025, 74025, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 2.5)
    # Central joint node
    ops.node(4026, 2.9, 0.0, 7.85, '-mass', 2.9328873598369003, 2.9328873598369003, 2.9328873598369003, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54026, 2.775, 0.0, 7.85)
    ops.element('elasticBeamColumn', 54026, 54026, 4026, 99999, 88888)
    ops.node(24026, 2.9, 0.0, 7.675)
    ops.element('elasticBeamColumn', 24026, 24026, 4026, 99999, 99999)
    ops.node(74026, 2.9, 0.0, 8.025)
    ops.element('elasticBeamColumn', 74026, 4026, 74026, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 3.5)
    # Central joint node
    ops.node(4027, 0.0, 0.0, 10.75, '-mass', 2.9328873598369, 2.9328873598369, 2.9328873598369, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34027, 0.125, 0.0, 10.75)
    ops.element('elasticBeamColumn', 34027, 4027, 34027, 99999, 88888)
    ops.node(24027, 0.0, 0.0, 10.575)
    ops.element('elasticBeamColumn', 24027, 24027, 4027, 99999, 99999)
    ops.node(74027, 0.0, 0.0, 10.925)
    ops.element('elasticBeamColumn', 74027, 4027, 74027, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 3.5)
    # Central joint node
    ops.node(4028, 2.9, 0.0, 10.75, '-mass', 2.9328873598369, 2.9328873598369, 2.9328873598369, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54028, 2.775, 0.0, 10.75)
    ops.element('elasticBeamColumn', 54028, 54028, 4028, 99999, 88888)
    ops.node(24028, 2.9, 0.0, 10.575)
    ops.element('elasticBeamColumn', 24028, 24028, 4028, 99999, 99999)
    ops.node(74028, 2.9, 0.0, 10.925)
    ops.element('elasticBeamColumn', 74028, 4028, 74028, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 3.5, '-mass', 2.5782874617736997, 2.5782874617736997, 2.5782874617736997, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.15, 0.0, 3.5)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 3.25)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.75)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.125, 3.5)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301001, 8.69279255, 0.0002, 8.69279255, 0.0132, 5.36455486, 0.027, -8.69279255, -0.0002, -8.69279255, -0.0132, -5.36455486, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401001, 11.74077935, 0.0002, 11.74077935, 0.0132, 7.23822912, 0.027, -11.74077935, -0.0002, -11.74077935, -0.0132, -7.23822912, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401001, 'My', 301001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11001, 1001, 11001, 11001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 2.9, 0.0, 3.5, '-mass', 8.095143341898456, 8.095143341898456, 8.095143341898456, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 2.75, 0.0, 3.5)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 3.05, 0.0, 3.5)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 2.9, 0.0, 3.25)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 2.9, 0.0, 3.75)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 2.9, 0.15, 3.5)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301002, 13.52336449, 0.0002, 13.52336449, 0.0132, 8.42905605, 0.027, -13.52336449, -0.0002, -13.52336449, -0.0132, -8.42905605, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401002, 25.95220063, 0.0002, 31.2923152, 0.009, 31.2923152, 0.02, -25.95220063, -0.0002, -31.2923152, -0.009, -31.2923152, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401002, 'My', 301002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11002, 1002, 11002, 11002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 7.9, 0.0, 3.5, '-mass', 11.918115429974282, 11.918115429974282, 11.918115429974282, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 7.75, 0.0, 3.5)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 8.05, 0.0, 3.5)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 7.9, 0.0, 3.25)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 7.9, 0.0, 3.75)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 7.9, 0.15, 3.5)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301003, 12.56995327, 0.0002, 12.56995327, 0.0132, 7.84329845, 0.027, -12.56995327, -0.0002, -12.56995327, -0.0132, -7.84329845, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401003, 23.167462, 0.0002, 27.92814137, 0.009, 27.92814137, 0.02, -23.167462, -0.0002, -27.92814137, -0.009, -27.92814137, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401003, 'My', 301003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11003, 1003, 11003, 11003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 12.9, 0.0, 3.5, '-mass', 7.640097470338823, 7.640097470338823, 7.640097470338823, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 12.775, 0.0, 3.5)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(21004, 12.9, 0.0, 3.25)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 12.9, 0.0, 3.75)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 12.9, 0.125, 3.5)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301004, 7.19072811, 0.0002, 7.19072811, 0.0132, 4.47976098, 0.027, -7.19072811, -0.0002, -7.19072811, -0.0132, -4.47976098, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401004, 10.97420577, 0.0002, 10.97420577, 0.0132, 6.79073495, 0.027, -10.97420577, -0.0002, -10.97420577, -0.0132, -6.79073495, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401004, 'My', 301004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11004, 1004, 11004, 11004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1005, 0.0, 4.05, 3.5, '-mass', 8.219722924521085, 8.219722924521085, 8.219722924521085, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31005, 0.125, 4.05, 3.5)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 0.0, 4.05, 3.225)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 0.0, 4.05, 3.775)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(61005, 0.0, 3.925, 3.5)
    ops.element('elasticBeamColumn', 61005, 61005, 1005, 99999, 77777)
    ops.node(41005, 0.0, 4.175, 3.5)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301005, 13.72853248, 0.0002, 16.55486549, 0.009, 16.55486549, 0.02, -13.72853248, -0.0002, -16.55486549, -0.009, -16.55486549, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401005, 12.97731993, 0.0002, 12.97731993, 0.0132, 8.0233858, 0.027, -12.97731993, -0.0002, -12.97731993, -0.0132, -8.0233858, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401005, 'My', 301005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11005, 1005, 11005, 11005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1006, 2.9, 4.05, 3.5, '-mass', 14.210111545117181, 14.210111545117181, 14.210111545117181, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 2.7, 4.05, 3.5)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(31006, 3.1, 4.05, 3.5)
    ops.element('elasticBeamColumn', 31006, 1006, 31006, 99999, 88888)
    ops.node(21006, 2.9, 4.05, 3.225)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 2.9, 4.05, 3.775)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(61006, 2.9, 3.875, 3.5)
    ops.element('elasticBeamColumn', 61006, 61006, 1006, 99999, 77777)
    ops.node(41006, 2.9, 4.225, 3.5)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301006, 23.31169842, 0.0002, 28.12273832, 0.009, 28.12273832, 0.02, -23.31169842, -0.0002, -28.12273832, -0.009, -28.12273832, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401006, 33.64026719, 0.0002, 40.58290452, 0.009, 40.58290452, 0.02, -33.64026719, -0.0002, -40.58290452, -0.009, -40.58290452, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401006, 'My', 301006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11006, 1006, 11006, 11006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1007, 7.9, 4.05, 3.5, '-mass', 15.660899565351217, 15.660899565351217, 15.660899565351217, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51007, 7.675, 4.05, 3.5)
    ops.element('elasticBeamColumn', 51007, 51007, 1007, 99999, 88888)
    ops.node(31007, 8.125, 4.05, 3.5)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 7.9, 4.05, 3.225)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 7.9, 4.05, 3.775)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 7.9, 3.85, 3.5)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 7.9, 4.25, 3.5)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301007, 28.0187816, 0.0002, 33.81311505, 0.009, 33.81311505, 0.02, -28.0187816, -0.0002, -33.81311505, -0.009, -33.81311505, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401007, 40.43288834, 0.0002, 48.79448095, 0.009, 48.79448095, 0.02, -40.43288834, -0.0002, -48.79448095, -0.009, -48.79448095, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401007, 'My', 301007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11007, 1007, 11007, 11007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1008, 12.9, 4.05, 3.5, '-mass', 10.918523177171021, 10.918523177171021, 10.918523177171021, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 12.75, 4.05, 3.5)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(21008, 12.9, 4.05, 3.225)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 12.9, 4.05, 3.775)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 12.9, 3.9, 3.5)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 12.9, 4.2, 3.5)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301008, 14.95951268, 0.0002, 18.03563991, 0.009, 18.03563991, 0.02, -14.95951268, -0.0002, -18.03563991, -0.009, -18.03563991, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401008, 17.83739026, 0.0002, 17.83739026, 0.0132, 11.06223162, 0.027, -17.83739026, -0.0002, -17.83739026, -0.0132, -11.06223162, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401008, 'My', 301008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11008, 1008, 11008, 11008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1009, 0.0, 8.1, 3.5, '-mass', 7.791204258828105, 7.791204258828105, 7.791204258828105, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31009, 0.125, 8.1, 3.5)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 0.0, 8.1, 3.225)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 0.0, 8.1, 3.775)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 0.0, 7.975, 3.5)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 0.0, 8.225, 3.5)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301009, 13.26735371, 0.0002, 16.00101993, 0.009, 16.00101993, 0.02, -13.26735371, -0.0002, -16.00101993, -0.009, -16.00101993, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401009, 12.56713466, 0.0002, 12.56713466, 0.0132, 7.76285963, 0.027, -12.56713466, -0.0002, -12.56713466, -0.0132, -7.76285963, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401009, 'My', 301009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11009, 1009, 11009, 11009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1010, 2.9, 8.1, 3.5, '-mass', 12.062632634775886, 12.062632634775886, 12.062632634775886, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 2.725, 8.1, 3.5)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 3.075, 8.1, 3.5)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 2.9, 8.1, 3.225)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 2.9, 8.1, 3.775)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 2.9, 7.95, 3.5)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 2.9, 8.25, 3.5)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301010, 18.77733842, 0.0002, 22.64525758, 0.009, 22.64525758, 0.02, -18.77733842, -0.0002, -22.64525758, -0.009, -22.64525758, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401010, 27.0968966, 0.0002, 32.67855056, 0.009, 32.67855056, 0.02, -27.0968966, -0.0002, -32.67855056, -0.009, -32.67855056, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401010, 'My', 301010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11010, 1010, 11010, 11010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1011, 7.9, 8.1, 3.5, '-mass', 15.660899565351217, 15.660899565351217, 15.660899565351217, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 7.675, 8.1, 3.5)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 8.125, 8.1, 3.5)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 7.9, 8.1, 3.225)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 7.9, 8.1, 3.775)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 7.9, 7.9, 3.5)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 7.9, 8.3, 3.5)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301011, 28.0187816, 0.0002, 33.81311505, 0.009, 33.81311505, 0.02, -28.0187816, -0.0002, -33.81311505, -0.009, -33.81311505, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401011, 40.43288834, 0.0002, 48.79448095, 0.009, 48.79448095, 0.02, -40.43288834, -0.0002, -48.79448095, -0.009, -48.79448095, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401011, 'My', 301011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11011, 1011, 11011, 11011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1012, 12.9, 8.1, 3.5, '-mass', 10.918523177171021, 10.918523177171021, 10.918523177171021, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 12.75, 8.1, 3.5)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 12.9, 8.1, 3.225)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 12.9, 8.1, 3.775)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 12.9, 7.95, 3.5)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 12.9, 8.25, 3.5)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301012, 14.95951268, 0.0002, 18.03563991, 0.009, 18.03563991, 0.02, -14.95951268, -0.0002, -18.03563991, -0.009, -18.03563991, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401012, 17.83739026, 0.0002, 17.83739026, 0.0132, 11.06223162, 0.027, -17.83739026, -0.0002, -17.83739026, -0.0132, -11.06223162, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401012, 'My', 301012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11012, 1012, 11012, 11012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    # Central joint node
    ops.node(1013, 0.0, 12.15, 3.5, '-mass', 7.791204258828104, 7.791204258828104, 7.791204258828104, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.125, 12.15, 3.5)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 12.15, 3.225)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 12.15, 3.775)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 12.025, 3.5)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    ops.node(41013, 0.0, 12.275, 3.5)
    ops.element('elasticBeamColumn', 41013, 1013, 41013, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301013, 13.26735371, 0.0002, 16.00101993, 0.009, 16.00101993, 0.02, -13.26735371, -0.0002, -16.00101993, -0.009, -16.00101993, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401013, 12.56713466, 0.0002, 12.56713466, 0.0132, 7.76285963, 0.027, -12.56713466, -0.0002, -12.56713466, -0.0132, -7.76285963, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401013, 'My', 301013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11013, 1013, 11013, 11013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    # Central joint node
    ops.node(1014, 2.9, 12.15, 3.5, '-mass', 12.062632634775884, 12.062632634775884, 12.062632634775884, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 2.725, 12.15, 3.5)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 3.075, 12.15, 3.5)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 2.9, 12.15, 3.225)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 2.9, 12.15, 3.775)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 2.9, 12.0, 3.5)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    ops.node(41014, 2.9, 12.3, 3.5)
    ops.element('elasticBeamColumn', 41014, 1014, 41014, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301014, 18.77733842, 0.0002, 22.64525758, 0.009, 22.64525758, 0.02, -18.77733842, -0.0002, -22.64525758, -0.009, -22.64525758, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401014, 27.0968966, 0.0002, 32.67855056, 0.009, 32.67855056, 0.02, -27.0968966, -0.0002, -32.67855056, -0.009, -32.67855056, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401014, 'My', 301014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11014, 1014, 11014, 11014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    # Central joint node
    ops.node(1015, 7.9, 12.15, 3.5, '-mass', 15.660899565351217, 15.660899565351217, 15.660899565351217, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 7.675, 12.15, 3.5)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 8.125, 12.15, 3.5)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 7.9, 12.15, 3.225)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 7.9, 12.15, 3.775)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 7.9, 11.95, 3.5)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    ops.node(41015, 7.9, 12.35, 3.5)
    ops.element('elasticBeamColumn', 41015, 1015, 41015, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301015, 28.0187816, 0.0002, 33.81311505, 0.009, 33.81311505, 0.02, -28.0187816, -0.0002, -33.81311505, -0.009, -33.81311505, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401015, 40.43288834, 0.0002, 48.79448095, 0.009, 48.79448095, 0.02, -40.43288834, -0.0002, -48.79448095, -0.009, -48.79448095, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401015, 'My', 301015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11015, 1015, 11015, 11015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    # Central joint node
    ops.node(1016, 12.9, 12.15, 3.5, '-mass', 10.918523177171021, 10.918523177171021, 10.918523177171021, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 12.75, 12.15, 3.5)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(21016, 12.9, 12.15, 3.225)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 12.9, 12.15, 3.775)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 12.9, 12.0, 3.5)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    ops.node(41016, 12.9, 12.3, 3.5)
    ops.element('elasticBeamColumn', 41016, 1016, 41016, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301016, 14.95951268, 0.0002, 18.03563991, 0.009, 18.03563991, 0.02, -14.95951268, -0.0002, -18.03563991, -0.009, -18.03563991, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401016, 17.83739026, 0.0002, 17.83739026, 0.0132, 11.06223162, 0.027, -17.83739026, -0.0002, -17.83739026, -0.0132, -11.06223162, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401016, 'My', 301016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11016, 1016, 11016, 11016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 1)
    # Central joint node
    ops.node(1017, 0.0, 16.2, 3.5, '-mass', 5.423532812390605, 5.423532812390605, 5.423532812390605, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31017, 0.15, 16.2, 3.5)
    ops.element('elasticBeamColumn', 31017, 1017, 31017, 99999, 88888)
    ops.node(21017, 0.0, 16.2, 3.25)
    ops.element('elasticBeamColumn', 21017, 21017, 1017, 99999, 99999)
    ops.node(71017, 0.0, 16.2, 3.75)
    ops.element('elasticBeamColumn', 71017, 1017, 71017, 99999, 99999)
    ops.node(61017, 0.0, 16.075, 3.5)
    ops.element('elasticBeamColumn', 61017, 61017, 1017, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301017, 7.76601653, 0.0002, 7.76601653, 0.0132, 4.79572208, 0.027, -7.76601653, -0.0002, -7.76601653, -0.0132, -4.79572208, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401017, 10.04989663, 0.0002, 10.04989663, 0.0132, 6.19995054, 0.027, -10.04989663, -0.0002, -10.04989663, -0.0132, -6.19995054, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401017, 'My', 301017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11017, 1017, 11017, 11017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 1)
    # Central joint node
    ops.node(1018, 2.9, 16.2, 3.5, '-mass', 9.43671896774472, 9.43671896774472, 9.43671896774472, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51018, 2.75, 16.2, 3.5)
    ops.element('elasticBeamColumn', 51018, 51018, 1018, 99999, 88888)
    ops.node(31018, 3.05, 16.2, 3.5)
    ops.element('elasticBeamColumn', 31018, 1018, 31018, 99999, 88888)
    ops.node(21018, 2.9, 16.2, 3.25)
    ops.element('elasticBeamColumn', 21018, 21018, 1018, 99999, 99999)
    ops.node(71018, 2.9, 16.2, 3.75)
    ops.element('elasticBeamColumn', 71018, 1018, 71018, 99999, 99999)
    ops.node(61018, 2.9, 16.075, 3.5)
    ops.element('elasticBeamColumn', 61018, 61018, 1018, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301018, 10.31021592, 0.0002, 10.31021592, 0.0132, 6.41175834, 0.027, -10.31021592, -0.0002, -10.31021592, -0.0132, -6.41175834, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401018, 18.83366963, 0.0002, 22.70575518, 0.009, 22.70575518, 0.02, -18.83366963, -0.0002, -22.70575518, -0.009, -22.70575518, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401018, 'My', 301018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11018, 1018, 11018, 11018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 1)
    # Central joint node
    ops.node(1019, 7.9, 16.2, 3.5, '-mass', 11.918115429974282, 11.918115429974282, 11.918115429974282, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51019, 7.75, 16.2, 3.5)
    ops.element('elasticBeamColumn', 51019, 51019, 1019, 99999, 88888)
    ops.node(31019, 8.05, 16.2, 3.5)
    ops.element('elasticBeamColumn', 31019, 1019, 31019, 99999, 88888)
    ops.node(21019, 7.9, 16.2, 3.25)
    ops.element('elasticBeamColumn', 21019, 21019, 1019, 99999, 99999)
    ops.node(71019, 7.9, 16.2, 3.75)
    ops.element('elasticBeamColumn', 71019, 1019, 71019, 99999, 99999)
    ops.node(61019, 7.9, 16.05, 3.5)
    ops.element('elasticBeamColumn', 61019, 61019, 1019, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301019, 12.56995327, 0.0002, 12.56995327, 0.0132, 7.84329845, 0.027, -12.56995327, -0.0002, -12.56995327, -0.0132, -7.84329845, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401019, 23.167462, 0.0002, 27.92814137, 0.009, 27.92814137, 0.02, -23.167462, -0.0002, -27.92814137, -0.009, -27.92814137, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401019, 'My', 301019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11019, 1019, 11019, 11019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 1)
    # Central joint node
    ops.node(1020, 12.9, 16.2, 3.5, '-mass', 7.737956797555948, 7.737956797555948, 7.737956797555948, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51020, 12.75, 16.2, 3.5)
    ops.element('elasticBeamColumn', 51020, 51020, 1020, 99999, 88888)
    ops.node(21020, 12.9, 16.2, 3.25)
    ops.element('elasticBeamColumn', 21020, 21020, 1020, 99999, 99999)
    ops.node(71020, 12.9, 16.2, 3.75)
    ops.element('elasticBeamColumn', 71020, 1020, 71020, 99999, 99999)
    ops.node(61020, 12.9, 16.075, 3.5)
    ops.element('elasticBeamColumn', 61020, 61020, 1020, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301020, 7.93290049, 0.0002, 7.93290049, 0.0132, 4.9338859, 0.027, -7.93290049, -0.0002, -7.93290049, -0.0132, -4.9338859, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401020, 11.99197246, 0.0002, 11.99197246, 0.0132, 7.43398991, 0.027, -11.99197246, -0.0002, -11.99197246, -0.0132, -7.43398991, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401020, 'My', 301020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11020, 1020, 11020, 11020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 6.4, '-mass', 2.528593272171253, 2.528593272171253, 2.528593272171253, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.15, 0.0, 6.4)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 6.15)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 6.65)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.125, 6.4)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302001, 7.38008875, 0.0002, 7.38008875, 0.0132, 4.52936148, 0.027, -7.38008875, -0.0002, -7.38008875, -0.0132, -4.52936148, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402001, 9.97310956, 0.0002, 9.97310956, 0.0132, 6.11341802, 0.027, -9.97310956, -0.0002, -9.97310956, -0.0132, -6.11341802, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402001, 'My', 302001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12001, 2001, 12001, 12001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 2.9, 0.0, 6.4, '-mass', 7.864715207341881, 7.864715207341881, 7.864715207341881, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 2.75, 0.0, 6.4)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 3.05, 0.0, 6.4)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 2.9, 0.0, 6.15)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 2.9, 0.0, 6.65)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 2.9, 0.15, 6.4)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302002, 9.68319217, 0.0002, 9.68319217, 0.0132, 6.02965233, 0.027, -9.68319217, -0.0002, -9.68319217, -0.0132, -6.02965233, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402002, 21.99070501, 0.0002, 26.53571769, 0.009, 26.53571769, 0.02, -21.99070501, -0.0002, -26.53571769, -0.009, -26.53571769, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402002, 'My', 302002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12002, 2002, 12002, 12002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 7.9, 0.0, 6.4, '-mass', 11.556341729668471, 11.556341729668471, 11.556341729668471, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 7.75, 0.0, 6.4)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 8.05, 0.0, 6.4)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 7.9, 0.0, 6.15)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 7.9, 0.0, 6.65)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 7.9, 0.15, 6.4)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302003, 7.78369248, 0.0002, 7.78369248, 0.0132, 4.86361014, 0.027, -7.78369248, -0.0002, -7.78369248, -0.0132, -4.86361014, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402003, 19.84035133, 0.0002, 23.93208613, 0.009, 23.93208613, 0.02, -19.84035133, -0.0002, -23.93208613, -0.009, -23.93208613, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402003, 'My', 302003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12003, 2003, 12003, 12003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 12.9, 0.0, 6.4, '-mass', 7.544684626302127, 7.544684626302127, 7.544684626302127, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 12.775, 0.0, 6.4)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(22004, 12.9, 0.0, 6.15)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 12.9, 0.0, 6.65)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 12.9, 0.125, 6.4)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302004, 5.17897063, 0.0002, 5.17897063, 0.0132, 3.2248649, 0.027, -5.17897063, -0.0002, -5.17897063, -0.0132, -3.2248649, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402004, 9.46210523, 0.0002, 9.46210523, 0.0132, 5.8300183, 0.027, -9.46210523, -0.0002, -9.46210523, -0.0132, -5.8300183, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402004, 'My', 302004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12004, 2004, 12004, 12004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2005, 0.0, 4.05, 6.4, '-mass', 8.173851364888057, 8.173851364888057, 8.173851364888057, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32005, 0.125, 4.05, 6.4)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 0.0, 4.05, 6.125)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 0.0, 4.05, 6.675)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(62005, 0.0, 3.925, 6.4)
    ops.element('elasticBeamColumn', 62005, 62005, 2005, 99999, 77777)
    ops.node(42005, 0.0, 4.175, 6.4)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302005, 11.79407649, 0.0002, 14.23231423, 0.009, 14.23231423, 0.02, -11.79407649, -0.0002, -14.23231423, -0.009, -14.23231423, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402005, 11.25659836, 0.0002, 11.25659836, 0.0132, 6.93015977, 0.027, -11.25659836, -0.0002, -11.25659836, -0.0132, -6.93015977, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402005, 'My', 302005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12005, 2005, 12005, 12005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2006, 2.9, 4.05, 6.4, '-mass', 13.623873013007092, 13.623873013007092, 13.623873013007092, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 2.7, 4.05, 6.4)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(32006, 3.1, 4.05, 6.4)
    ops.element('elasticBeamColumn', 32006, 2006, 32006, 99999, 88888)
    ops.node(22006, 2.9, 4.05, 6.125)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 2.9, 4.05, 6.675)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(62006, 2.9, 3.875, 6.4)
    ops.element('elasticBeamColumn', 62006, 62006, 2006, 99999, 77777)
    ops.node(42006, 2.9, 4.225, 6.4)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302006, 17.38763182, 0.0002, 20.99308641, 0.009, 20.99308641, 0.02, -17.38763182, -0.0002, -20.99308641, -0.009, -20.99308641, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402006, 29.12680064, 0.0002, 35.16645908, 0.009, 35.16645908, 0.02, -29.12680064, -0.0002, -35.16645908, -0.009, -35.16645908, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402006, 'My', 302006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12006, 2006, 12006, 12006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2007, 7.9, 4.05, 6.4, '-mass', 14.928483663210546, 14.928483663210546, 14.928483663210546, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52007, 7.675, 4.05, 6.4)
    ops.element('elasticBeamColumn', 52007, 52007, 2007, 99999, 88888)
    ops.node(32007, 8.125, 4.05, 6.4)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 7.9, 4.05, 6.125)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 7.9, 4.05, 6.675)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 7.9, 3.85, 6.4)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 7.9, 4.25, 6.4)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302007, 17.6964361, 0.0002, 21.3753959, 0.009, 21.3753959, 0.02, -17.6964361, -0.0002, -21.3753959, -0.009, -21.3753959, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402007, 35.12010171, 0.0002, 42.42131431, 0.009, 42.42131431, 0.02, -35.12010171, -0.0002, -42.42131431, -0.009, -42.42131431, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402007, 'My', 302007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12007, 2007, 12007, 12007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2008, 12.9, 4.05, 6.4, '-mass', 10.655832045672549, 10.655832045672549, 10.655832045672549, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 12.75, 4.05, 6.4)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(22008, 12.9, 4.05, 6.125)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 12.9, 4.05, 6.675)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 12.9, 3.9, 6.4)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 12.9, 4.2, 6.4)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302008, 10.856506, 0.0002, 13.09729591, 0.009, 13.09729591, 0.02, -10.856506, -0.0002, -13.09729591, -0.009, -13.09729591, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402008, 15.46501735, 0.0002, 15.46501735, 0.0132, 9.55539761, 0.027, -15.46501735, -0.0002, -15.46501735, -0.0132, -9.55539761, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402008, 'My', 302008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12008, 2008, 12008, 12008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2009, 0.0, 8.1, 6.4, '-mass', 7.745332699195078, 7.745332699195078, 7.745332699195078, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32009, 0.125, 8.1, 6.4)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 0.0, 8.1, 6.125)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 0.0, 8.1, 6.675)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 0.0, 7.975, 6.4)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 0.0, 8.225, 6.4)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302009, 11.36876333, 0.0002, 13.72192173, 0.009, 13.72192173, 0.02, -11.36876333, -0.0002, -13.72192173, -0.009, -13.72192173, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402009, 10.87821048, 0.0002, 10.87821048, 0.0132, 6.68962596, 0.027, -10.87821048, -0.0002, -10.87821048, -0.0132, -6.68962596, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402009, 'My', 302009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12009, 2009, 12009, 12009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2010, 2.9, 8.1, 6.4, '-mass', 11.537556182176495, 11.537556182176495, 11.537556182176495, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 2.725, 8.1, 6.4)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 3.075, 8.1, 6.4)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 2.9, 8.1, 6.125)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 2.9, 8.1, 6.675)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 2.9, 7.95, 6.4)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 2.9, 8.25, 6.4)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302010, 14.04919154, 0.0002, 16.95479525, 0.009, 16.95479525, 0.02, -14.04919154, -0.0002, -16.95479525, -0.009, -16.95479525, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402010, 23.53442985, 0.0002, 28.40173672, 0.009, 28.40173672, 0.02, -23.53442985, -0.0002, -28.40173672, -0.009, -28.40173672, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402010, 'My', 302010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12010, 2010, 12010, 12010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2011, 7.9, 8.1, 6.4, '-mass', 14.928483663210546, 14.928483663210546, 14.928483663210546, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 7.675, 8.1, 6.4)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 8.125, 8.1, 6.4)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 7.9, 8.1, 6.125)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 7.9, 8.1, 6.675)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 7.9, 7.9, 6.4)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 7.9, 8.3, 6.4)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302011, 17.6964361, 0.0002, 21.3753959, 0.009, 21.3753959, 0.02, -17.6964361, -0.0002, -21.3753959, -0.009, -21.3753959, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402011, 35.12010171, 0.0002, 42.42131431, 0.009, 42.42131431, 0.02, -35.12010171, -0.0002, -42.42131431, -0.009, -42.42131431, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402011, 'My', 302011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12011, 2011, 12011, 12011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2012, 12.9, 8.1, 6.4, '-mass', 10.65583204567255, 10.65583204567255, 10.65583204567255, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 12.75, 8.1, 6.4)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 12.9, 8.1, 6.125)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 12.9, 8.1, 6.675)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 12.9, 7.95, 6.4)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 12.9, 8.25, 6.4)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302012, 10.856506, 0.0002, 13.09729591, 0.009, 13.09729591, 0.02, -10.856506, -0.0002, -13.09729591, -0.009, -13.09729591, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402012, 15.46501735, 0.0002, 15.46501735, 0.0132, 9.55539761, 0.027, -15.46501735, -0.0002, -15.46501735, -0.0132, -9.55539761, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402012, 'My', 302012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12012, 2012, 12012, 12012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    # Central joint node
    ops.node(2013, 0.0, 12.15, 6.4, '-mass', 7.745332699195077, 7.745332699195077, 7.745332699195077, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.125, 12.15, 6.4)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 12.15, 6.125)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 12.15, 6.675)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 12.025, 6.4)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    ops.node(42013, 0.0, 12.275, 6.4)
    ops.element('elasticBeamColumn', 42013, 2013, 42013, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302013, 11.36876333, 0.0002, 13.72192173, 0.009, 13.72192173, 0.02, -11.36876333, -0.0002, -13.72192173, -0.009, -13.72192173, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402013, 10.87821048, 0.0002, 10.87821048, 0.0132, 6.68962596, 0.027, -10.87821048, -0.0002, -10.87821048, -0.0132, -6.68962596, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402013, 'My', 302013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12013, 2013, 12013, 12013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    # Central joint node
    ops.node(2014, 2.9, 12.15, 6.4, '-mass', 11.537556182176496, 11.537556182176496, 11.537556182176496, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 2.725, 12.15, 6.4)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 3.075, 12.15, 6.4)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 2.9, 12.15, 6.125)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 2.9, 12.15, 6.675)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 2.9, 12.0, 6.4)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    ops.node(42014, 2.9, 12.3, 6.4)
    ops.element('elasticBeamColumn', 42014, 2014, 42014, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302014, 14.04919154, 0.0002, 16.95479525, 0.009, 16.95479525, 0.02, -14.04919154, -0.0002, -16.95479525, -0.009, -16.95479525, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402014, 23.53442985, 0.0002, 28.40173672, 0.009, 28.40173672, 0.02, -23.53442985, -0.0002, -28.40173672, -0.009, -28.40173672, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402014, 'My', 302014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12014, 2014, 12014, 12014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    # Central joint node
    ops.node(2015, 7.9, 12.15, 6.4, '-mass', 14.928483663210546, 14.928483663210546, 14.928483663210546, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 7.675, 12.15, 6.4)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 8.125, 12.15, 6.4)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 7.9, 12.15, 6.125)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 7.9, 12.15, 6.675)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 7.9, 11.95, 6.4)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    ops.node(42015, 7.9, 12.35, 6.4)
    ops.element('elasticBeamColumn', 42015, 2015, 42015, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302015, 17.6964361, 0.0002, 21.3753959, 0.009, 21.3753959, 0.02, -17.6964361, -0.0002, -21.3753959, -0.009, -21.3753959, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402015, 35.12010171, 0.0002, 42.42131431, 0.009, 42.42131431, 0.02, -35.12010171, -0.0002, -42.42131431, -0.009, -42.42131431, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402015, 'My', 302015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12015, 2015, 12015, 12015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    # Central joint node
    ops.node(2016, 12.9, 12.15, 6.4, '-mass', 10.655832045672549, 10.655832045672549, 10.655832045672549, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 12.75, 12.15, 6.4)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(22016, 12.9, 12.15, 6.125)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 12.9, 12.15, 6.675)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 12.9, 12.0, 6.4)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    ops.node(42016, 12.9, 12.3, 6.4)
    ops.element('elasticBeamColumn', 42016, 2016, 42016, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302016, 10.856506, 0.0002, 13.09729591, 0.009, 13.09729591, 0.02, -10.856506, -0.0002, -13.09729591, -0.009, -13.09729591, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402016, 15.46501735, 0.0002, 15.46501735, 0.0132, 9.55539761, 0.027, -15.46501735, -0.0002, -15.46501735, -0.0132, -9.55539761, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402016, 'My', 302016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12016, 2016, 12016, 12016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 2)
    # Central joint node
    ops.node(2017, 0.0, 16.2, 6.4, '-mass', 5.324144433185713, 5.324144433185713, 5.324144433185713, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32017, 0.15, 16.2, 6.4)
    ops.element('elasticBeamColumn', 32017, 2017, 32017, 99999, 88888)
    ops.node(22017, 0.0, 16.2, 6.15)
    ops.element('elasticBeamColumn', 22017, 22017, 2017, 99999, 99999)
    ops.node(72017, 0.0, 16.2, 6.65)
    ops.element('elasticBeamColumn', 72017, 2017, 72017, 99999, 99999)
    ops.node(62017, 0.0, 16.075, 6.4)
    ops.element('elasticBeamColumn', 62017, 62017, 2017, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302017, 6.6755864, 0.0002, 6.6755864, 0.0132, 4.10211275, 0.027, -6.6755864, -0.0002, -6.6755864, -0.0132, -4.10211275, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402017, 8.64290627, 0.0002, 8.64290627, 0.0132, 5.30486818, 0.027, -8.64290627, -0.0002, -8.64290627, -0.0132, -5.30486818, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402017, 'My', 302017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12017, 2017, 12017, 12017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 2)
    # Central joint node
    ops.node(2018, 2.9, 16.2, 6.4, '-mass', 9.188706735328818, 9.188706735328818, 9.188706735328818, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52018, 2.75, 16.2, 6.4)
    ops.element('elasticBeamColumn', 52018, 52018, 2018, 99999, 88888)
    ops.node(32018, 3.05, 16.2, 6.4)
    ops.element('elasticBeamColumn', 32018, 2018, 32018, 99999, 88888)
    ops.node(22018, 2.9, 16.2, 6.15)
    ops.element('elasticBeamColumn', 22018, 22018, 2018, 99999, 99999)
    ops.node(72018, 2.9, 16.2, 6.65)
    ops.element('elasticBeamColumn', 72018, 2018, 72018, 99999, 99999)
    ops.node(62018, 2.9, 16.075, 6.4)
    ops.element('elasticBeamColumn', 62018, 62018, 2018, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302018, 7.61123311, 0.0002, 7.61123311, 0.0132, 4.72962712, 0.027, -7.61123311, -0.0002, -7.61123311, -0.0132, -4.72962712, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402018, 16.13498521, 0.0002, 19.46480017, 0.009, 19.46480017, 0.02, -16.13498521, -0.0002, -19.46480017, -0.009, -19.46480017, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402018, 'My', 302018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12018, 2018, 12018, 12018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 2)
    # Central joint node
    ops.node(2019, 7.9, 16.2, 6.4, '-mass', 11.556341729668471, 11.556341729668471, 11.556341729668471, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52019, 7.75, 16.2, 6.4)
    ops.element('elasticBeamColumn', 52019, 52019, 2019, 99999, 88888)
    ops.node(32019, 8.05, 16.2, 6.4)
    ops.element('elasticBeamColumn', 32019, 2019, 32019, 99999, 88888)
    ops.node(22019, 7.9, 16.2, 6.15)
    ops.element('elasticBeamColumn', 22019, 22019, 2019, 99999, 99999)
    ops.node(72019, 7.9, 16.2, 6.65)
    ops.element('elasticBeamColumn', 72019, 2019, 72019, 99999, 99999)
    ops.node(62019, 7.9, 16.05, 6.4)
    ops.element('elasticBeamColumn', 62019, 62019, 2019, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302019, 7.78369248, 0.0002, 7.78369248, 0.0132, 4.86361014, 0.027, -7.78369248, -0.0002, -7.78369248, -0.0132, -4.86361014, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402019, 19.84035133, 0.0002, 23.93208613, 0.009, 23.93208613, 0.02, -19.84035133, -0.0002, -23.93208613, -0.009, -23.93208613, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402019, 'My', 302019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12019, 2019, 12019, 12019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 2)
    # Central joint node
    ops.node(2020, 12.9, 16.2, 6.4, '-mass', 7.589027133947385, 7.589027133947385, 7.589027133947385, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52020, 12.75, 16.2, 6.4)
    ops.element('elasticBeamColumn', 52020, 52020, 2020, 99999, 88888)
    ops.node(22020, 12.9, 16.2, 6.15)
    ops.element('elasticBeamColumn', 22020, 22020, 2020, 99999, 99999)
    ops.node(72020, 12.9, 16.2, 6.65)
    ops.element('elasticBeamColumn', 72020, 2020, 72020, 99999, 99999)
    ops.node(62020, 12.9, 16.075, 6.4)
    ops.element('elasticBeamColumn', 62020, 62020, 2020, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302020, 5.70885317, 0.0002, 5.70885317, 0.0132, 3.54851506, 0.027, -5.70885317, -0.0002, -5.70885317, -0.0132, -3.54851506, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402020, 10.3213593, 0.0002, 10.3213593, 0.0132, 6.37252743, 0.027, -10.3213593, -0.0002, -10.3213593, -0.0132, -6.37252743, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402020, 'My', 302020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12020, 2020, 12020, 12020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 9.3, '-mass', 2.506422018348623, 2.506422018348623, 2.506422018348623, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 9.3)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 9.05)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 9.55)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 9.3)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303001, 5.08178504, 0.0002, 5.08178504, 0.0132, 3.09347815, 0.027, -5.08178504, -0.0002, -5.08178504, -0.0132, -3.09347815, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403001, 7.01369698, 0.0002, 7.01369698, 0.0132, 4.23204142, 0.027, -7.01369698, -0.0002, -7.01369698, -0.0132, -4.23204142, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403001, 'My', 303001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13001, 3001, 13001, 13001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 2.9, 0.0, 9.3, '-mass', 7.815938448932095, 7.815938448932095, 7.815938448932095, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 2.775, 0.0, 9.3)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 3.025, 0.0, 9.3)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 2.9, 0.0, 9.05)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 2.9, 0.0, 9.55)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 2.9, 0.125, 9.3)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303002, 6.31893178, 0.0002, 6.31893178, 0.0132, 3.91558859, 0.027, -6.31893178, -0.0002, -6.31893178, -0.0132, -3.91558859, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403002, 14.17713367, 0.0002, 17.11458897, 0.009, 17.11458897, 0.02, -14.17713367, -0.0002, -17.11458897, -0.009, -17.11458897, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403002, 'My', 303002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13002, 3002, 13002, 13002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 7.9, 0.0, 9.3, '-mass', 11.4587882128489, 11.4587882128489, 11.4587882128489, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 7.775, 0.0, 9.3)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 8.025, 0.0, 9.3)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 7.9, 0.0, 9.05)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 7.9, 0.0, 9.55)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 7.9, 0.125, 9.3)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303003, 5.242789, 0.0002, 5.242789, 0.0132, 3.26538909, 0.027, -5.242789, -0.0002, -5.242789, -0.0132, -3.26538909, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403003, 13.25329681, 0.0002, 15.98954553, 0.009, 15.98954553, 0.02, -13.25329681, -0.0002, -15.98954553, -0.009, -15.98954553, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403003, 'My', 303003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13003, 3003, 13003, 13003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 12.9, 0.0, 9.3, '-mass', 7.544684626302126, 7.544684626302126, 7.544684626302126, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 12.775, 0.0, 9.3)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(23004, 12.9, 0.0, 9.05)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 12.9, 0.0, 9.55)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 12.9, 0.125, 9.3)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303004, 4.16326457, 0.0002, 4.16326457, 0.0132, 2.5795252, 0.027, -4.16326457, -0.0002, -4.16326457, -0.0132, -2.5795252, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403004, 7.6631397, 0.0002, 7.6631397, 0.0132, 4.68559088, 0.027, -7.6631397, -0.0002, -7.6631397, -0.0132, -4.68559088, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403004, 'My', 303004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13004, 3004, 13004, 13004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3005, 0.0, 4.05, 9.3, '-mass', 8.173851364888057, 8.173851364888057, 8.173851364888057, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33005, 0.125, 4.05, 9.3)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 0.0, 4.05, 9.025)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 0.0, 4.05, 9.575)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(63005, 0.0, 3.925, 9.3)
    ops.element('elasticBeamColumn', 63005, 63005, 3005, 99999, 77777)
    ops.node(43005, 0.0, 4.175, 9.3)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303005, 9.49504141, 0.0002, 11.47491759, 0.009, 11.47491759, 0.02, -9.49504141, -0.0002, -11.47491759, -0.009, -11.47491759, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403005, 9.21080375, 0.0002, 9.21080375, 0.0132, 5.62886161, 0.027, -9.21080375, -0.0002, -9.21080375, -0.0132, -5.62886161, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403005, 'My', 303005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13005, 3005, 13005, 13005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3006, 2.9, 4.05, 9.3, '-mass', 13.437634480897001, 13.437634480897001, 13.437634480897001, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 2.725, 4.05, 9.3)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(33006, 3.075, 4.05, 9.3)
    ops.element('elasticBeamColumn', 33006, 3006, 33006, 99999, 88888)
    ops.node(23006, 2.9, 4.05, 9.025)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 2.9, 4.05, 9.575)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(63006, 2.9, 3.925, 9.3)
    ops.element('elasticBeamColumn', 63006, 63006, 3006, 99999, 77777)
    ops.node(43006, 2.9, 4.175, 9.3)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303006, 11.26846663, 0.0002, 13.60198679, 0.009, 13.60198679, 0.02, -11.26846663, -0.0002, -13.60198679, -0.009, -13.60198679, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403006, 18.87631303, 0.0002, 22.78529715, 0.009, 22.78529715, 0.02, -18.87631303, -0.0002, -22.78529715, -0.009, -22.78529715, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403006, 'My', 303006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13006, 3006, 13006, 13006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3007, 7.9, 4.05, 9.3, '-mass', 14.72450812804235, 14.72450812804235, 14.72450812804235, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53007, 7.725, 4.05, 9.3)
    ops.element('elasticBeamColumn', 53007, 53007, 3007, 99999, 88888)
    ops.node(33007, 8.075, 4.05, 9.3)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 7.9, 4.05, 9.025)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 7.9, 4.05, 9.575)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 7.9, 3.875, 9.3)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 7.9, 4.225, 9.3)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303007, 12.06078751, 0.0002, 14.56798287, 0.009, 14.56798287, 0.02, -12.06078751, -0.0002, -14.56798287, -0.009, -14.56798287, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403007, 23.93567167, 0.0002, 28.91141681, 0.009, 28.91141681, 0.02, -23.93567167, -0.0002, -28.91141681, -0.009, -28.91141681, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403007, 'My', 303007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13007, 3007, 13007, 13007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3008, 12.9, 4.05, 9.3, '-mass', 10.558278528852977, 10.558278528852977, 10.558278528852977, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 12.775, 4.05, 9.3)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(23008, 12.9, 4.05, 9.025)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 12.9, 4.05, 9.575)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 12.9, 3.925, 9.3)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 12.9, 4.175, 9.3)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303008, 8.00224513, 0.0002, 9.66048675, 0.009, 9.66048675, 0.02, -8.00224513, -0.0002, -9.66048675, -0.009, -9.66048675, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403008, 10.55469835, 0.0002, 10.55469835, 0.0132, 6.48392821, 0.027, -10.55469835, -0.0002, -10.55469835, -0.0132, -6.48392821, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403008, 'My', 303008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13008, 3008, 13008, 13008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3009, 0.0, 8.1, 9.3, '-mass', 7.745332699195077, 7.745332699195077, 7.745332699195077, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33009, 0.125, 8.1, 9.3)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 0.0, 8.1, 9.025)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 0.0, 8.1, 9.575)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 0.0, 7.975, 9.3)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 0.0, 8.225, 9.3)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303009, 9.10509856, 0.0002, 11.00769736, 0.009, 11.00769736, 0.02, -9.10509856, -0.0002, -11.00769736, -0.009, -11.00769736, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403009, 8.86368729, 0.0002, 8.86368729, 0.0132, 5.40781438, 0.027, -8.86368729, -0.0002, -8.86368729, -0.0132, -5.40781438, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403009, 'My', 303009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13009, 3009, 13009, 13009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3010, 2.9, 8.1, 9.3, '-mass', 11.386791656182611, 11.386791656182611, 11.386791656182611, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 2.775, 8.1, 9.3)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 3.025, 8.1, 9.3)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 2.9, 8.1, 9.025)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 2.9, 8.1, 9.575)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 2.9, 7.975, 9.3)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 2.9, 8.225, 9.3)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303010, 9.80985731, 0.0002, 11.84023201, 0.009, 11.84023201, 0.02, -9.80985731, -0.0002, -11.84023201, -0.009, -11.84023201, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403010, 14.98475449, 0.0002, 18.07748487, 0.009, 18.07748487, 0.02, -14.98475449, -0.0002, -18.07748487, -0.009, -18.07748487, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403010, 'My', 303010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13010, 3010, 13010, 13010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3011, 7.9, 8.1, 9.3, '-mass', 14.72450812804235, 14.72450812804235, 14.72450812804235, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 7.725, 8.1, 9.3)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 8.075, 8.1, 9.3)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 7.9, 8.1, 9.025)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 7.9, 8.1, 9.575)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 7.9, 7.925, 9.3)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 7.9, 8.275, 9.3)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303011, 12.06078751, 0.0002, 14.56798287, 0.009, 14.56798287, 0.02, -12.06078751, -0.0002, -14.56798287, -0.009, -14.56798287, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403011, 23.93567167, 0.0002, 28.91141681, 0.009, 28.91141681, 0.02, -23.93567167, -0.0002, -28.91141681, -0.009, -28.91141681, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403011, 'My', 303011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13011, 3011, 13011, 13011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3012, 12.9, 8.1, 9.3, '-mass', 10.558278528852979, 10.558278528852979, 10.558278528852979, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 12.775, 8.1, 9.3)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 12.9, 8.1, 9.025)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 12.9, 8.1, 9.575)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 12.9, 7.975, 9.3)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 12.9, 8.225, 9.3)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303012, 8.00224513, 0.0002, 9.66048675, 0.009, 9.66048675, 0.02, -8.00224513, -0.0002, -9.66048675, -0.009, -9.66048675, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403012, 10.55469835, 0.0002, 10.55469835, 0.0132, 6.48392821, 0.027, -10.55469835, -0.0002, -10.55469835, -0.0132, -6.48392821, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403012, 'My', 303012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13012, 3012, 13012, 13012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    # Central joint node
    ops.node(3013, 0.0, 12.15, 9.3, '-mass', 7.745332699195076, 7.745332699195076, 7.745332699195076, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.125, 12.15, 9.3)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 12.15, 9.025)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 12.15, 9.575)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 12.025, 9.3)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    ops.node(43013, 0.0, 12.275, 9.3)
    ops.element('elasticBeamColumn', 43013, 3013, 43013, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303013, 9.10509856, 0.0002, 11.00769736, 0.009, 11.00769736, 0.02, -9.10509856, -0.0002, -11.00769736, -0.009, -11.00769736, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403013, 8.86368729, 0.0002, 8.86368729, 0.0132, 5.40781438, 0.027, -8.86368729, -0.0002, -8.86368729, -0.0132, -5.40781438, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403013, 'My', 303013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13013, 3013, 13013, 13013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    # Central joint node
    ops.node(3014, 2.9, 12.15, 9.3, '-mass', 11.386791656182613, 11.386791656182613, 11.386791656182613, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 2.775, 12.15, 9.3)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 3.025, 12.15, 9.3)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 2.9, 12.15, 9.025)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 2.9, 12.15, 9.575)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 2.9, 12.025, 9.3)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    ops.node(43014, 2.9, 12.275, 9.3)
    ops.element('elasticBeamColumn', 43014, 3014, 43014, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303014, 9.80985731, 0.0002, 11.84023201, 0.009, 11.84023201, 0.02, -9.80985731, -0.0002, -11.84023201, -0.009, -11.84023201, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403014, 14.98475449, 0.0002, 18.07748487, 0.009, 18.07748487, 0.02, -14.98475449, -0.0002, -18.07748487, -0.009, -18.07748487, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403014, 'My', 303014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13014, 3014, 13014, 13014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    # Central joint node
    ops.node(3015, 7.9, 12.15, 9.3, '-mass', 14.72450812804235, 14.72450812804235, 14.72450812804235, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 7.725, 12.15, 9.3)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 8.075, 12.15, 9.3)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 7.9, 12.15, 9.025)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 7.9, 12.15, 9.575)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 7.9, 11.975, 9.3)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    ops.node(43015, 7.9, 12.325, 9.3)
    ops.element('elasticBeamColumn', 43015, 3015, 43015, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303015, 12.06078751, 0.0002, 14.56798287, 0.009, 14.56798287, 0.02, -12.06078751, -0.0002, -14.56798287, -0.009, -14.56798287, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403015, 23.93567167, 0.0002, 28.91141681, 0.009, 28.91141681, 0.02, -23.93567167, -0.0002, -28.91141681, -0.009, -28.91141681, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403015, 'My', 303015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13015, 3015, 13015, 13015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    # Central joint node
    ops.node(3016, 12.9, 12.15, 9.3, '-mass', 10.558278528852977, 10.558278528852977, 10.558278528852977, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 12.775, 12.15, 9.3)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(23016, 12.9, 12.15, 9.025)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 12.9, 12.15, 9.575)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 12.9, 12.025, 9.3)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    ops.node(43016, 12.9, 12.275, 9.3)
    ops.element('elasticBeamColumn', 43016, 3016, 43016, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303016, 8.00224513, 0.0002, 9.66048675, 0.009, 9.66048675, 0.02, -8.00224513, -0.0002, -9.66048675, -0.009, -9.66048675, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403016, 10.55469835, 0.0002, 10.55469835, 0.0132, 6.48392821, 0.027, -10.55469835, -0.0002, -10.55469835, -0.0132, -6.48392821, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403016, 'My', 303016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13016, 3016, 13016, 13016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 3)
    # Central joint node
    ops.node(3017, 0.0, 16.2, 9.3, '-mass', 5.279801925540452, 5.279801925540452, 5.279801925540452, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33017, 0.125, 16.2, 9.3)
    ops.element('elasticBeamColumn', 33017, 3017, 33017, 99999, 88888)
    ops.node(23017, 0.0, 16.2, 9.05)
    ops.element('elasticBeamColumn', 23017, 23017, 3017, 99999, 99999)
    ops.node(73017, 0.0, 16.2, 9.55)
    ops.element('elasticBeamColumn', 73017, 3017, 73017, 99999, 99999)
    ops.node(63017, 0.0, 16.075, 9.3)
    ops.element('elasticBeamColumn', 63017, 63017, 3017, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303017, 4.85617164, 0.0002, 4.85617164, 0.0132, 2.96820117, 0.027, -4.85617164, -0.0002, -4.85617164, -0.0132, -2.96820117, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403017, 6.40763127, 0.0002, 6.40763127, 0.0132, 3.88520715, 0.027, -6.40763127, -0.0002, -6.40763127, -0.0132, -3.88520715, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403017, 'My', 303017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13017, 3017, 13017, 13017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 3)
    # Central joint node
    ops.node(3018, 2.9, 16.2, 9.3, '-mass', 9.144364227683559, 9.144364227683559, 9.144364227683559, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53018, 2.775, 16.2, 9.3)
    ops.element('elasticBeamColumn', 53018, 53018, 3018, 99999, 88888)
    ops.node(33018, 3.025, 16.2, 9.3)
    ops.element('elasticBeamColumn', 33018, 3018, 33018, 99999, 88888)
    ops.node(23018, 2.9, 16.2, 9.05)
    ops.element('elasticBeamColumn', 23018, 23018, 3018, 99999, 99999)
    ops.node(73018, 2.9, 16.2, 9.55)
    ops.element('elasticBeamColumn', 73018, 3018, 73018, 99999, 99999)
    ops.node(63018, 2.9, 16.075, 9.3)
    ops.element('elasticBeamColumn', 63018, 63018, 3018, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303018, 5.61222099, 0.0002, 5.61222099, 0.0132, 3.47731971, 0.027, -5.61222099, -0.0002, -5.61222099, -0.0132, -3.47731971, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403018, 11.82698411, 0.0002, 14.27786308, 0.009, 14.27786308, 0.02, -11.82698411, -0.0002, -14.27786308, -0.009, -14.27786308, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403018, 'My', 303018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13018, 3018, 13018, 13018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 3)
    # Central joint node
    ops.node(3019, 7.9, 16.2, 9.3, '-mass', 11.4587882128489, 11.4587882128489, 11.4587882128489, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53019, 7.775, 16.2, 9.3)
    ops.element('elasticBeamColumn', 53019, 53019, 3019, 99999, 88888)
    ops.node(33019, 8.025, 16.2, 9.3)
    ops.element('elasticBeamColumn', 33019, 3019, 33019, 99999, 88888)
    ops.node(23019, 7.9, 16.2, 9.05)
    ops.element('elasticBeamColumn', 23019, 23019, 3019, 99999, 99999)
    ops.node(73019, 7.9, 16.2, 9.55)
    ops.element('elasticBeamColumn', 73019, 3019, 73019, 99999, 99999)
    ops.node(63019, 7.9, 16.075, 9.3)
    ops.element('elasticBeamColumn', 63019, 63019, 3019, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303019, 5.242789, 0.0002, 5.242789, 0.0132, 3.26538909, 0.027, -5.242789, -0.0002, -5.242789, -0.0132, -3.26538909, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403019, 13.25329681, 0.0002, 15.98954553, 0.009, 15.98954553, 0.02, -13.25329681, -0.0002, -15.98954553, -0.009, -15.98954553, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403019, 'My', 303019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13019, 3019, 13019, 13019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 3)
    # Central joint node
    ops.node(3020, 12.9, 16.2, 9.3, '-mass', 7.544684626302125, 7.544684626302125, 7.544684626302125, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53020, 12.775, 16.2, 9.3)
    ops.element('elasticBeamColumn', 53020, 53020, 3020, 99999, 88888)
    ops.node(23020, 12.9, 16.2, 9.05)
    ops.element('elasticBeamColumn', 23020, 23020, 3020, 99999, 99999)
    ops.node(73020, 12.9, 16.2, 9.55)
    ops.element('elasticBeamColumn', 73020, 3020, 73020, 99999, 99999)
    ops.node(63020, 12.9, 16.075, 9.3)
    ops.element('elasticBeamColumn', 63020, 63020, 3020, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303020, 4.16326457, 0.0002, 4.16326457, 0.0132, 2.5795252, 0.027, -4.16326457, -0.0002, -4.16326457, -0.0132, -2.5795252, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403020, 7.6631397, 0.0002, 7.6631397, 0.0132, 4.68559088, 0.027, -7.6631397, -0.0002, -7.6631397, -0.0132, -4.68559088, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403020, 'My', 303020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13020, 3020, 13020, 13020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 12.2, '-mass', 0.6918960244648318, 0.6918960244648318, 0.6918960244648318, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 12.2)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 12.0)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 12.2)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304001, 2.40137675, 0.0002, 2.40137675, 0.0132, 1.37279644, 0.027, -2.40137675, -0.0002, -2.40137675, -0.0132, -1.37279644, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404001, 3.4176117, 0.0002, 3.4176117, 0.0132, 1.91165982, 0.027, -3.4176117, -0.0002, -3.4176117, -0.0132, -1.91165982, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404001, 'My', 304001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14001, 4001, 14001, 14001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 2.9, 0.0, 12.2, '-mass', 3.682197368402024, 3.682197368402024, 3.682197368402024, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 2.775, 0.0, 12.2)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 3.025, 0.0, 12.2)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 2.9, 0.0, 12.0)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 2.9, 0.125, 12.2)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304002, 4.65128881, 0.0002, 4.65128881, 0.0132, 2.82910693, 0.027, -4.65128881, -0.0002, -4.65128881, -0.0132, -2.82910693, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404002, 6.39641159, 0.0002, 6.39641159, 0.0132, 3.84757189, 0.027, -6.39641159, -0.0002, -6.39641159, -0.0132, -3.84757189, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404002, 'My', 304002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14002, 4002, 14002, 14002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 7.9, 0.0, 12.2, '-mass', 6.499562932522703, 6.499562932522703, 6.499562932522703, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 7.775, 0.0, 12.2)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 8.025, 0.0, 12.2)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 7.9, 0.0, 12.0)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 7.9, 0.125, 12.2)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304003, 6.01329271, 0.0002, 6.01329271, 0.0132, 3.69859326, 0.027, -6.01329271, -0.0002, -6.01329271, -0.0132, -3.69859326, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404003, 8.20781938, 0.0002, 8.20781938, 0.0132, 5.00568743, 0.027, -8.20781938, -0.0002, -8.20781938, -0.0132, -5.00568743, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404003, 'My', 304003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14003, 4003, 14003, 14003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 12.9, 0.0, 12.2, '-mass', 3.5092615885855105, 3.5092615885855105, 3.5092615885855105, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 12.775, 0.0, 12.2)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(24004, 12.9, 0.0, 12.0)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 12.9, 0.125, 12.2)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304004, 4.57534069, 0.0002, 4.57534069, 0.0132, 2.78049715, 0.027, -4.57534069, -0.0002, -4.57534069, -0.0132, -2.78049715, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404004, 6.29549156, 0.0002, 6.29549156, 0.0132, 3.78284934, 0.027, -6.29549156, -0.0002, -6.29549156, -0.0132, -3.78284934, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404004, 'My', 304004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14004, 4004, 14004, 14004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4005, 0.0, 4.05, 12.2, '-mass', 4.54258225173821, 4.54258225173821, 4.54258225173821, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34005, 0.125, 4.05, 12.2)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 0.0, 4.05, 11.95)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(64005, 0.0, 3.925, 12.2)
    ops.element('elasticBeamColumn', 64005, 64005, 4005, 99999, 77777)
    ops.node(44005, 0.0, 4.175, 12.2)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304005, 5.12196191, 0.0002, 5.12196191, 0.0132, 3.13000405, 0.027, -5.12196191, -0.0002, -5.12196191, -0.0132, -3.13000405, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404005, 9.02464714, 0.0002, 9.02464714, 0.0132, 5.40557086, 0.027, -9.02464714, -0.0002, -9.02464714, -0.0132, -5.40557086, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404005, 'My', 304005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14005, 4005, 14005, 14005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4006, 2.9, 4.05, 12.2, '-mass', 10.397802676615655, 10.397802676615655, 10.397802676615655, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 2.725, 4.05, 12.2)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(34006, 3.075, 4.05, 12.2)
    ops.element('elasticBeamColumn', 34006, 4006, 34006, 99999, 88888)
    ops.node(24006, 2.9, 4.05, 11.95)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(64006, 2.9, 3.925, 12.2)
    ops.element('elasticBeamColumn', 64006, 64006, 4006, 99999, 77777)
    ops.node(44006, 2.9, 4.175, 12.2)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304006, 8.39905607, 0.0002, 8.39905607, 0.0132, 5.16557019, 0.027, -8.39905607, -0.0002, -8.39905607, -0.0132, -5.16557019, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404006, 14.18768012, 0.0002, 14.18768012, 0.0132, 8.68329692, 0.027, -14.18768012, -0.0002, -14.18768012, -0.0132, -8.68329692, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404006, 'My', 304006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14006, 4006, 14006, 14006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4007, 7.9, 4.05, 12.2, '-mass', 12.562122806941431, 12.562122806941431, 12.562122806941431, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54007, 7.725, 4.05, 12.2)
    ops.element('elasticBeamColumn', 54007, 54007, 4007, 99999, 88888)
    ops.node(34007, 8.075, 4.05, 12.2)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 7.9, 4.05, 11.95)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 7.9, 3.875, 12.2)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 7.9, 4.225, 12.2)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304007, 10.77039628, 0.0002, 10.77039628, 0.0132, 6.65948291, 0.027, -10.77039628, -0.0002, -10.77039628, -0.0132, -6.65948291, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404007, 18.60991848, 0.0002, 18.60991848, 0.0132, 11.35738953, 0.027, -18.60991848, -0.0002, -18.60991848, -0.0132, -11.35738953, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404007, 'My', 304007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14007, 4007, 14007, 14007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4008, 12.9, 4.05, 12.2, '-mass', 6.582743360657259, 6.582743360657259, 6.582743360657259, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 12.775, 4.05, 12.2)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(24008, 12.9, 4.05, 11.95)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 12.9, 3.925, 12.2)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 12.9, 4.175, 12.2)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304008, 6.04806525, 0.0002, 6.04806525, 0.0132, 3.72075055, 0.027, -6.04806525, -0.0002, -6.04806525, -0.0132, -3.72075055, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404008, 10.56019148, 0.0002, 10.56019148, 0.0132, 6.38807194, 0.027, -10.56019148, -0.0002, -10.56019148, -0.0132, -6.38807194, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404008, 'My', 304008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14008, 4008, 14008, 14008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4009, 0.0, 8.1, 12.2, '-mass', 3.934476430081927, 3.934476430081927, 3.934476430081927, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34009, 0.125, 8.1, 12.2)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 0.0, 8.1, 11.95)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 0.0, 7.975, 12.2)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 0.0, 8.225, 12.2)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304009, 4.80848275, 0.0002, 4.80848275, 0.0132, 2.92966344, 0.027, -4.80848275, -0.0002, -4.80848275, -0.0132, -2.92966344, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404009, 8.50562637, 0.0002, 8.50562637, 0.0132, 5.07257427, 0.027, -8.50562637, -0.0002, -8.50562637, -0.0132, -5.07257427, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404009, 'My', 304009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14009, 4009, 14009, 14009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4010, 2.9, 8.1, 12.2, '-mass', 9.701011839668851, 9.701011839668851, 9.701011839668851, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 2.775, 8.1, 12.2)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 3.025, 8.1, 12.2)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 2.9, 8.1, 11.95)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 2.9, 7.975, 12.2)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 2.9, 8.225, 12.2)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304010, 6.77423145, 0.0002, 6.77423145, 0.0132, 4.18315832, 0.027, -6.77423145, -0.0002, -6.77423145, -0.0132, -4.18315832, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404010, 11.76583339, 0.0002, 11.76583339, 0.0132, 7.15755055, 0.027, -11.76583339, -0.0002, -11.76583339, -0.0132, -7.15755055, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404010, 'My', 304010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14010, 4010, 14010, 14010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4011, 7.9, 8.1, 12.2, '-mass', 12.562122806941431, 12.562122806941431, 12.562122806941431, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 7.725, 8.1, 12.2)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 8.075, 8.1, 12.2)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 7.9, 8.1, 11.95)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 7.9, 7.925, 12.2)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 7.9, 8.275, 12.2)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304011, 10.77039628, 0.0002, 10.77039628, 0.0132, 6.65948291, 0.027, -10.77039628, -0.0002, -10.77039628, -0.0132, -6.65948291, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404011, 18.60991848, 0.0002, 18.60991848, 0.0132, 11.35738953, 0.027, -18.60991848, -0.0002, -18.60991848, -0.0132, -11.35738953, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404011, 'My', 304011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14011, 4011, 14011, 14011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4012, 12.9, 8.1, 12.2, '-mass', 6.582743360657259, 6.582743360657259, 6.582743360657259, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 12.775, 8.1, 12.2)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 12.9, 8.1, 11.95)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 12.9, 7.975, 12.2)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 12.9, 8.225, 12.2)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304012, 6.04806525, 0.0002, 6.04806525, 0.0132, 3.72075055, 0.027, -6.04806525, -0.0002, -6.04806525, -0.0132, -3.72075055, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404012, 10.56019148, 0.0002, 10.56019148, 0.0132, 6.38807194, 0.027, -10.56019148, -0.0002, -10.56019148, -0.0132, -6.38807194, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404012, 'My', 304012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14012, 4012, 14012, 14012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    # Central joint node
    ops.node(4013, 0.0, 12.15, 12.2, '-mass', 3.9344764300819266, 3.9344764300819266, 3.9344764300819266, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.125, 12.15, 12.2)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 12.15, 11.95)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 12.025, 12.2)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    ops.node(44013, 0.0, 12.275, 12.2)
    ops.element('elasticBeamColumn', 44013, 4013, 44013, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304013, 4.80848275, 0.0002, 4.80848275, 0.0132, 2.92966344, 0.027, -4.80848275, -0.0002, -4.80848275, -0.0132, -2.92966344, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404013, 8.50562637, 0.0002, 8.50562637, 0.0132, 5.07257427, 0.027, -8.50562637, -0.0002, -8.50562637, -0.0132, -5.07257427, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404013, 'My', 304013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14013, 4013, 14013, 14013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    # Central joint node
    ops.node(4014, 2.9, 12.15, 12.2, '-mass', 9.70101183966885, 9.70101183966885, 9.70101183966885, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 2.775, 12.15, 12.2)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 3.025, 12.15, 12.2)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 2.9, 12.15, 11.95)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 2.9, 12.025, 12.2)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    ops.node(44014, 2.9, 12.275, 12.2)
    ops.element('elasticBeamColumn', 44014, 4014, 44014, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304014, 6.77423145, 0.0002, 6.77423145, 0.0132, 4.18315832, 0.027, -6.77423145, -0.0002, -6.77423145, -0.0132, -4.18315832, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404014, 11.76583339, 0.0002, 11.76583339, 0.0132, 7.15755055, 0.027, -11.76583339, -0.0002, -11.76583339, -0.0132, -7.15755055, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404014, 'My', 304014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14014, 4014, 14014, 14014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    # Central joint node
    ops.node(4015, 7.9, 12.15, 12.2, '-mass', 12.562122806941431, 12.562122806941431, 12.562122806941431, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 7.725, 12.15, 12.2)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 8.075, 12.15, 12.2)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 7.9, 12.15, 11.95)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 7.9, 11.975, 12.2)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    ops.node(44015, 7.9, 12.325, 12.2)
    ops.element('elasticBeamColumn', 44015, 4015, 44015, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304015, 10.77039628, 0.0002, 10.77039628, 0.0132, 6.65948291, 0.027, -10.77039628, -0.0002, -10.77039628, -0.0132, -6.65948291, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404015, 18.60991848, 0.0002, 18.60991848, 0.0132, 11.35738953, 0.027, -18.60991848, -0.0002, -18.60991848, -0.0132, -11.35738953, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404015, 'My', 304015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14015, 4015, 14015, 14015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    # Central joint node
    ops.node(4016, 12.9, 12.15, 12.2, '-mass', 6.582743360657259, 6.582743360657259, 6.582743360657259, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 12.775, 12.15, 12.2)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(24016, 12.9, 12.15, 11.95)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 12.9, 12.025, 12.2)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    ops.node(44016, 12.9, 12.275, 12.2)
    ops.element('elasticBeamColumn', 44016, 4016, 44016, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304016, 6.04806525, 0.0002, 6.04806525, 0.0132, 3.72075055, 0.027, -6.04806525, -0.0002, -6.04806525, -0.0132, -3.72075055, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404016, 10.56019148, 0.0002, 10.56019148, 0.0132, 6.38807194, 0.027, -10.56019148, -0.0002, -10.56019148, -0.0132, -6.38807194, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404016, 'My', 304016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14016, 4016, 14016, 14016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 4)
    # Central joint node
    ops.node(4017, 0.0, 16.2, 12.2, '-mass', 2.1401739948574767, 2.1401739948574767, 2.1401739948574767, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34017, 0.125, 16.2, 12.2)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 0.0, 16.2, 12.0)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(64017, 0.0, 16.075, 12.2)
    ops.element('elasticBeamColumn', 64017, 64017, 4017, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304017, 3.71526222, 0.0002, 3.71526222, 0.0132, 2.22843152, 0.027, -3.71526222, -0.0002, -3.71526222, -0.0132, -2.22843152, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404017, 5.15370847, 0.0002, 5.15370847, 0.0132, 3.04808711, 0.027, -5.15370847, -0.0002, -5.15370847, -0.0132, -3.04808711, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404017, 'My', 304017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14017, 4017, 14017, 14017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 4)
    # Central joint node
    ops.node(4018, 2.9, 16.2, 12.2, '-mass', 5.130475338794669, 5.130475338794669, 5.130475338794669, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 2.775, 16.2, 12.2)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(34018, 3.025, 16.2, 12.2)
    ops.element('elasticBeamColumn', 34018, 4018, 34018, 99999, 88888)
    ops.node(24018, 2.9, 16.2, 12.0)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(64018, 2.9, 16.075, 12.2)
    ops.element('elasticBeamColumn', 64018, 64018, 4018, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304018, 5.4064126, 0.0002, 5.4064126, 0.0132, 3.31160634, 0.027, -5.4064126, -0.0002, -5.4064126, -0.0132, -3.31160634, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404018, 7.40038686, 0.0002, 7.40038686, 0.0132, 4.49015719, 0.027, -7.40038686, -0.0002, -7.40038686, -0.0132, -4.49015719, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404018, 'My', 304018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14018, 4018, 14018, 14018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 4)
    # Central joint node
    ops.node(4019, 7.9, 16.2, 12.2, '-mass', 6.499562932522703, 6.499562932522703, 6.499562932522703, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54019, 7.775, 16.2, 12.2)
    ops.element('elasticBeamColumn', 54019, 54019, 4019, 99999, 88888)
    ops.node(34019, 8.025, 16.2, 12.2)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 7.9, 16.2, 12.0)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(64019, 7.9, 16.075, 12.2)
    ops.element('elasticBeamColumn', 64019, 64019, 4019, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304019, 6.01329271, 0.0002, 6.01329271, 0.0132, 3.69859326, 0.027, -6.01329271, -0.0002, -6.01329271, -0.0132, -3.69859326, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404019, 8.20781938, 0.0002, 8.20781938, 0.0132, 5.00568743, 0.027, -8.20781938, -0.0002, -8.20781938, -0.0132, -5.00568743, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404019, 'My', 304019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14019, 4019, 14019, 14019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 4)
    # Central joint node
    ops.node(4020, 12.9, 16.2, 12.2, '-mass', 3.5092615885855105, 3.5092615885855105, 3.5092615885855105, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 12.775, 16.2, 12.2)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(24020, 12.9, 16.2, 12.0)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(64020, 12.9, 16.075, 12.2)
    ops.element('elasticBeamColumn', 64020, 64020, 4020, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304020, 4.57534069, 0.0002, 4.57534069, 0.0132, 2.78049715, 0.027, -4.57534069, -0.0002, -4.57534069, -0.0132, -2.78049715, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404020, 6.29549156, 0.0002, 6.29549156, 0.0132, 3.78284934, 0.027, -6.29549156, -0.0002, -6.29549156, -0.0132, -3.78284934, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404020, 'My', 304020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14020, 4020, 14020, 14020, '-orient', 0, 0, 1, 0, 1, 0)
