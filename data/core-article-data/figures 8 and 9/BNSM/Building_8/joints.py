import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (2, 0, 0.5)
    # Central joint node
    ops.node(4019, 14.6, 0.0, 1.325, '-mass', 3.158339704383281, 3.158339704383281, 3.158339704383281, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34019, 14.775, 0.0, 1.325)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 14.6, 0.0, 1.125)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(74019, 14.6, 0.0, 1.525)
    ops.element('elasticBeamColumn', 74019, 4019, 74019, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 0.5)
    # Central joint node
    ops.node(4020, 17.65, 0.0, 1.325, '-mass', 3.158339704383281, 3.158339704383281, 3.158339704383281, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 17.475, 0.0, 1.325)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(24020, 17.65, 0.0, 1.125)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(74020, 17.65, 0.0, 1.525)
    ops.element('elasticBeamColumn', 74020, 4020, 74020, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 1.5)
    # Central joint node
    ops.node(4021, 14.6, 0.0, 3.975, '-mass', 3.0837219673802223, 3.0837219673802223, 3.0837219673802223, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34021, 14.775, 0.0, 3.975)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 14.6, 0.0, 3.775)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(74021, 14.6, 0.0, 4.175)
    ops.element('elasticBeamColumn', 74021, 4021, 74021, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 1.5)
    # Central joint node
    ops.node(4022, 17.65, 0.0, 3.975, '-mass', 3.0837219673802223, 3.0837219673802223, 3.0837219673802223, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 17.475, 0.0, 3.975)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(24022, 17.65, 0.0, 3.775)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(74022, 17.65, 0.0, 4.175)
    ops.element('elasticBeamColumn', 74022, 4022, 74022, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 2.5)
    # Central joint node
    ops.node(4023, 14.6, 0.0, 6.625, '-mass', 2.8892265545361853, 2.8892265545361853, 2.8892265545361853, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34023, 14.725, 0.0, 6.625)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 14.6, 0.0, 6.425)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(74023, 14.6, 0.0, 6.825)
    ops.element('elasticBeamColumn', 74023, 4023, 74023, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 2.5)
    # Central joint node
    ops.node(4024, 17.65, 0.0, 6.625, '-mass', 2.8892265545361853, 2.8892265545361853, 2.8892265545361853, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 17.525, 0.0, 6.625)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 17.65, 0.0, 6.425)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(74024, 17.65, 0.0, 6.825)
    ops.element('elasticBeamColumn', 74024, 4024, 74024, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 3.5)
    # Central joint node
    ops.node(4025, 14.6, 0.0, 9.275, '-mass', 2.8892265545361853, 2.8892265545361853, 2.8892265545361853, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34025, 14.725, 0.0, 9.275)
    ops.element('elasticBeamColumn', 34025, 4025, 34025, 99999, 88888)
    ops.node(24025, 14.6, 0.0, 9.075)
    ops.element('elasticBeamColumn', 24025, 24025, 4025, 99999, 99999)
    ops.node(74025, 14.6, 0.0, 9.475)
    ops.element('elasticBeamColumn', 74025, 4025, 74025, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 3.5)
    # Central joint node
    ops.node(4026, 17.65, 0.0, 9.275, '-mass', 2.8892265545361853, 2.8892265545361853, 2.8892265545361853, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54026, 17.525, 0.0, 9.275)
    ops.element('elasticBeamColumn', 54026, 54026, 4026, 99999, 88888)
    ops.node(24026, 17.65, 0.0, 9.075)
    ops.element('elasticBeamColumn', 24026, 24026, 4026, 99999, 99999)
    ops.node(74026, 17.65, 0.0, 9.475)
    ops.element('elasticBeamColumn', 74026, 4026, 74026, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 2.65, '-mass', 10.756233435270133, 10.756233435270133, 10.756233435270133, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.15, 0.0, 2.65)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 2.3)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.0)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.15, 2.65)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301001, 12.37150814, 0.0002, 12.37150814, 0.0132, 7.7084917, 0.027, -12.37150814, -0.0002, -12.37150814, -0.0132, -7.7084917, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401001, 22.97551313, 0.0002, 22.97551313, 0.0132, 14.18055157, 0.027, -22.97551313, -0.0002, -22.97551313, -0.0132, -14.18055157, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401001, 'My', 301001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11001, 1001, 11001, 11001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 7.3, 0.0, 2.65, '-mass', 18.785963302752297, 18.785963302752297, 18.785963302752297, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 7.075, 0.0, 2.65)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 7.525, 0.0, 2.65)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 7.3, 0.0, 2.3)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 7.3, 0.0, 3.0)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 7.3, 0.225, 2.65)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301002, 22.54215236, 0.0002, 22.54215236, 0.0132, 14.1106596, 0.027, -22.54215236, -0.0002, -22.54215236, -0.0132, -14.1106596, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401002, 63.55035209, 0.0002, 76.64662483, 0.009, 76.64662483, 0.02, -63.55035209, -0.0002, -76.64662483, -0.009, -76.64662483, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401002, 'My', 301002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11002, 1002, 11002, 11002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 14.6, 0.0, 2.65, '-mass', 11.629016309887866, 11.629016309887866, 11.629016309887866, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 14.425, 0.0, 2.65)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 14.775, 0.0, 2.65)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 14.6, 0.0, 2.3)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 14.6, 0.0, 3.0)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 14.6, 0.175, 2.65)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301003, 20.88092477, 0.0002, 20.88092477, 0.0132, 13.03187688, 0.027, -20.88092477, -0.0002, -20.88092477, -0.0132, -13.03187688, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401003, 58.82411445, 0.0002, 70.91644326, 0.009, 70.91644326, 0.02, -58.82411445, -0.0002, -70.91644326, -0.009, -70.91644326, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401003, 'My', 301003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11003, 1003, 11003, 11003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 17.65, 0.0, 2.65, '-mass', 11.62901630988787, 11.62901630988787, 11.62901630988787, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 17.475, 0.0, 2.65)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(31004, 17.825, 0.0, 2.65)
    ops.element('elasticBeamColumn', 31004, 1004, 31004, 99999, 88888)
    ops.node(21004, 17.65, 0.0, 2.3)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 17.65, 0.0, 3.0)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 17.65, 0.175, 2.65)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301004, 20.88092477, 0.0002, 20.88092477, 0.0132, 13.03187688, 0.027, -20.88092477, -0.0002, -20.88092477, -0.0132, -13.03187688, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401004, 58.82411445, 0.0002, 70.91644326, 0.009, 70.91644326, 0.02, -58.82411445, -0.0002, -70.91644326, -0.009, -70.91644326, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401004, 'My', 301004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11004, 1004, 11004, 11004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 1)
    # Central joint node
    ops.node(1005, 24.95, 0.0, 2.65, '-mass', 18.7859633027523, 18.7859633027523, 18.7859633027523, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51005, 24.725, 0.0, 2.65)
    ops.element('elasticBeamColumn', 51005, 51005, 1005, 99999, 88888)
    ops.node(31005, 25.175, 0.0, 2.65)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 24.95, 0.0, 2.3)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 24.95, 0.0, 3.0)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(41005, 24.95, 0.225, 2.65)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301005, 22.54215236, 0.0002, 22.54215236, 0.0132, 14.1106596, 0.027, -22.54215236, -0.0002, -22.54215236, -0.0132, -14.1106596, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401005, 63.55035209, 0.0002, 76.64662483, 0.009, 76.64662483, 0.02, -63.55035209, -0.0002, -76.64662483, -0.009, -76.64662483, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401005, 'My', 301005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11005, 1005, 11005, 11005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 1)
    # Central joint node
    ops.node(1006, 32.25, 0.0, 2.65, '-mass', 10.756233435270135, 10.756233435270135, 10.756233435270135, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 32.1, 0.0, 2.65)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(21006, 32.25, 0.0, 2.3)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 32.25, 0.0, 3.0)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(41006, 32.25, 0.15, 2.65)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301006, 12.37150814, 0.0002, 12.37150814, 0.0132, 7.7084917, 0.027, -12.37150814, -0.0002, -12.37150814, -0.0132, -7.7084917, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401006, 22.97551313, 0.0002, 22.97551313, 0.0132, 14.18055157, 0.027, -22.97551313, -0.0002, -22.97551313, -0.0132, -14.18055157, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401006, 'My', 301006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11006, 1006, 11006, 11006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1007, 0.0, 3.65, 2.65, '-mass', 14.055484199796124, 14.055484199796124, 14.055484199796124, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31007, 0.175, 3.65, 2.65)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 0.0, 3.65, 2.3)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 0.0, 3.65, 3.0)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 0.0, 3.475, 2.65)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 0.0, 3.825, 2.65)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301007, 23.89085727, 0.0002, 28.80702766, 0.009, 28.80702766, 0.02, -23.89085727, -0.0002, -28.80702766, -0.009, -28.80702766, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401007, 31.16745762, 0.0002, 31.16745762, 0.0132, 19.30911912, 0.027, -31.16745762, -0.0002, -31.16745762, -0.0132, -19.30911912, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401007, 'My', 301007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11007, 1007, 11007, 11007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1008, 7.3, 3.65, 2.65, '-mass', 22.398634046890923, 22.398634046890923, 22.398634046890923, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 7.05, 3.65, 2.65)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(31008, 7.55, 3.65, 2.65)
    ops.element('elasticBeamColumn', 31008, 1008, 31008, 99999, 88888)
    ops.node(21008, 7.3, 3.65, 2.3)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 7.3, 3.65, 3.0)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 7.3, 3.4, 2.65)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 7.3, 3.9, 2.65)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301008, 38.26789112, 0.0002, 46.16416746, 0.009, 46.16416746, 0.02, -38.26789112, -0.0002, -46.16416746, -0.009, -46.16416746, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401008, 74.78130139, 0.0002, 90.21183084, 0.009, 90.21183084, 0.02, -74.78130139, -0.0002, -90.21183084, -0.009, -90.21183084, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401008, 'My', 301008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11008, 1008, 11008, 11008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1009, 14.6, 3.65, 2.65, '-mass', 17.869341233435264, 17.869341233435264, 17.869341233435264, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51009, 14.375, 3.65, 2.65)
    ops.element('elasticBeamColumn', 51009, 51009, 1009, 99999, 88888)
    ops.node(31009, 14.825, 3.65, 2.65)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 14.6, 3.65, 2.3)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 14.6, 3.65, 3.0)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 14.6, 3.425, 2.65)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 14.6, 3.875, 2.65)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301009, 34.88800311, 0.0002, 42.09037951, 0.009, 42.09037951, 0.02, -34.88800311, -0.0002, -42.09037951, -0.009, -42.09037951, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401009, 59.54613728, 0.0002, 71.83900748, 0.009, 71.83900748, 0.02, -59.54613728, -0.0002, -71.83900748, -0.009, -71.83900748, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401009, 'My', 301009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11009, 1009, 11009, 11009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1010, 17.65, 3.65, 2.65, '-mass', 17.86934123343527, 17.86934123343527, 17.86934123343527, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 17.425, 3.65, 2.65)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 17.875, 3.65, 2.65)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 17.65, 3.65, 2.3)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 17.65, 3.65, 3.0)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 17.65, 3.425, 2.65)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 17.65, 3.875, 2.65)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301010, 34.88800311, 0.0002, 42.09037951, 0.009, 42.09037951, 0.02, -34.88800311, -0.0002, -42.09037951, -0.009, -42.09037951, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401010, 59.54613728, 0.0002, 71.83900748, 0.009, 71.83900748, 0.02, -59.54613728, -0.0002, -71.83900748, -0.009, -71.83900748, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401010, 'My', 301010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11010, 1010, 11010, 11010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 1)
    # Central joint node
    ops.node(1011, 24.95, 3.65, 2.65, '-mass', 22.398634046890926, 22.398634046890926, 22.398634046890926, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 24.7, 3.65, 2.65)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 25.2, 3.65, 2.65)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 24.95, 3.65, 2.3)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 24.95, 3.65, 3.0)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 24.95, 3.4, 2.65)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 24.95, 3.9, 2.65)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301011, 38.26789112, 0.0002, 46.16416746, 0.009, 46.16416746, 0.02, -38.26789112, -0.0002, -46.16416746, -0.009, -46.16416746, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401011, 74.78130139, 0.0002, 90.21183084, 0.009, 90.21183084, 0.02, -74.78130139, -0.0002, -90.21183084, -0.009, -90.21183084, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401011, 'My', 301011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11011, 1011, 11011, 11011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 1)
    # Central joint node
    ops.node(1012, 32.25, 3.65, 2.65, '-mass', 14.055484199796126, 14.055484199796126, 14.055484199796126, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 32.075, 3.65, 2.65)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 32.25, 3.65, 2.3)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 32.25, 3.65, 3.0)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 32.25, 3.475, 2.65)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 32.25, 3.825, 2.65)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301012, 23.89085727, 0.0002, 28.80702766, 0.009, 28.80702766, 0.02, -23.89085727, -0.0002, -28.80702766, -0.009, -28.80702766, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401012, 31.16745762, 0.0002, 31.16745762, 0.0132, 19.30911912, 0.027, -31.16745762, -0.0002, -31.16745762, -0.0132, -19.30911912, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401012, 'My', 301012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11012, 1012, 11012, 11012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1013, 0.0, 7.3, 2.65, '-mass', 10.756233435270133, 10.756233435270133, 10.756233435270133, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.15, 7.3, 2.65)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 7.3, 2.3)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 7.3, 3.0)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 7.15, 2.65)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301013, 12.37150814, 0.0002, 12.37150814, 0.0132, 7.7084917, 0.027, -12.37150814, -0.0002, -12.37150814, -0.0132, -7.7084917, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401013, 22.97551313, 0.0002, 22.97551313, 0.0132, 14.18055157, 0.027, -22.97551313, -0.0002, -22.97551313, -0.0132, -14.18055157, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401013, 'My', 301013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11013, 1013, 11013, 11013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1014, 7.3, 7.3, 2.65, '-mass', 18.785963302752297, 18.785963302752297, 18.785963302752297, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 7.075, 7.3, 2.65)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 7.525, 7.3, 2.65)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 7.3, 7.3, 2.3)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 7.3, 7.3, 3.0)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 7.3, 7.075, 2.65)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301014, 22.54215236, 0.0002, 22.54215236, 0.0132, 14.1106596, 0.027, -22.54215236, -0.0002, -22.54215236, -0.0132, -14.1106596, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401014, 63.55035209, 0.0002, 76.64662483, 0.009, 76.64662483, 0.02, -63.55035209, -0.0002, -76.64662483, -0.009, -76.64662483, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401014, 'My', 301014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11014, 1014, 11014, 11014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1015, 14.6, 7.3, 2.65, '-mass', 13.230558103975534, 13.230558103975534, 13.230558103975534, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 14.425, 7.3, 2.65)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 14.775, 7.3, 2.65)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 14.6, 7.3, 2.3)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 14.6, 7.3, 3.0)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 14.6, 7.125, 2.65)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301015, 17.00159923, 0.0002, 17.00159923, 0.0132, 10.60498095, 0.027, -17.00159923, -0.0002, -17.00159923, -0.0132, -10.60498095, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401015, 41.42473003, 0.0002, 49.94629678, 0.009, 49.94629678, 0.02, -41.42473003, -0.0002, -49.94629678, -0.009, -49.94629678, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401015, 'My', 301015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11015, 1015, 11015, 11015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1016, 17.65, 7.3, 2.65, '-mass', 13.230558103975536, 13.230558103975536, 13.230558103975536, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 17.475, 7.3, 2.65)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(31016, 17.825, 7.3, 2.65)
    ops.element('elasticBeamColumn', 31016, 1016, 31016, 99999, 88888)
    ops.node(21016, 17.65, 7.3, 2.3)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 17.65, 7.3, 3.0)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 17.65, 7.125, 2.65)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301016, 17.00159923, 0.0002, 17.00159923, 0.0132, 10.60498095, 0.027, -17.00159923, -0.0002, -17.00159923, -0.0132, -10.60498095, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401016, 41.42473003, 0.0002, 49.94629678, 0.009, 49.94629678, 0.02, -41.42473003, -0.0002, -49.94629678, -0.009, -49.94629678, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401016, 'My', 301016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11016, 1016, 11016, 11016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 1)
    # Central joint node
    ops.node(1017, 24.95, 7.3, 2.65, '-mass', 18.7859633027523, 18.7859633027523, 18.7859633027523, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51017, 24.725, 7.3, 2.65)
    ops.element('elasticBeamColumn', 51017, 51017, 1017, 99999, 88888)
    ops.node(31017, 25.175, 7.3, 2.65)
    ops.element('elasticBeamColumn', 31017, 1017, 31017, 99999, 88888)
    ops.node(21017, 24.95, 7.3, 2.3)
    ops.element('elasticBeamColumn', 21017, 21017, 1017, 99999, 99999)
    ops.node(71017, 24.95, 7.3, 3.0)
    ops.element('elasticBeamColumn', 71017, 1017, 71017, 99999, 99999)
    ops.node(61017, 24.95, 7.075, 2.65)
    ops.element('elasticBeamColumn', 61017, 61017, 1017, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301017, 22.54215236, 0.0002, 22.54215236, 0.0132, 14.1106596, 0.027, -22.54215236, -0.0002, -22.54215236, -0.0132, -14.1106596, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401017, 63.55035209, 0.0002, 76.64662483, 0.009, 76.64662483, 0.02, -63.55035209, -0.0002, -76.64662483, -0.009, -76.64662483, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401017, 'My', 301017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11017, 1017, 11017, 11017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 1)
    # Central joint node
    ops.node(1018, 32.25, 7.3, 2.65, '-mass', 10.756233435270135, 10.756233435270135, 10.756233435270135, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51018, 32.1, 7.3, 2.65)
    ops.element('elasticBeamColumn', 51018, 51018, 1018, 99999, 88888)
    ops.node(21018, 32.25, 7.3, 2.3)
    ops.element('elasticBeamColumn', 21018, 21018, 1018, 99999, 99999)
    ops.node(71018, 32.25, 7.3, 3.0)
    ops.element('elasticBeamColumn', 71018, 1018, 71018, 99999, 99999)
    ops.node(61018, 32.25, 7.15, 2.65)
    ops.element('elasticBeamColumn', 61018, 61018, 1018, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301018, 12.37150814, 0.0002, 12.37150814, 0.0132, 7.7084917, 0.027, -12.37150814, -0.0002, -12.37150814, -0.0132, -7.7084917, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401018, 22.97551313, 0.0002, 22.97551313, 0.0132, 14.18055157, 0.027, -22.97551313, -0.0002, -22.97551313, -0.0132, -14.18055157, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401018, 'My', 301018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11018, 1018, 11018, 11018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 5.3, '-mass', 10.667089704383283, 10.667089704383283, 10.667089704383283, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.15, 0.0, 5.3)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 4.95)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 5.65)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.15, 5.3)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302001, 10.6473525, 0.0002, 10.6473525, 0.0132, 6.61370972, 0.027, -10.6473525, -0.0002, -10.6473525, -0.0132, -6.61370972, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402001, 19.86049657, 0.0002, 19.86049657, 0.0132, 12.20098494, 0.027, -19.86049657, -0.0002, -19.86049657, -0.0132, -12.20098494, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402001, 'My', 302001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12001, 2001, 12001, 12001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 7.3, 0.0, 5.3, '-mass', 18.52663608562691, 18.52663608562691, 18.52663608562691, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 7.075, 0.0, 5.3)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 7.525, 0.0, 5.3)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 7.3, 0.0, 4.95)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 7.3, 0.0, 5.65)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 7.3, 0.225, 5.3)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302002, 19.40968362, 0.0002, 19.40968362, 0.0132, 12.1220436, 0.027, -19.40968362, -0.0002, -19.40968362, -0.0132, -12.1220436, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402002, 54.50077327, 0.0002, 65.78368506, 0.009, 65.78368506, 0.02, -54.50077327, -0.0002, -65.78368506, -0.009, -65.78368506, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402002, 'My', 302002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12002, 2002, 12002, 12002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 14.6, 0.0, 5.3, '-mass', 11.53176860346585, 11.53176860346585, 11.53176860346585, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 14.425, 0.0, 5.3)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 14.775, 0.0, 5.3)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 14.6, 0.0, 4.95)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 14.6, 0.0, 5.65)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 14.6, 0.175, 5.3)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302003, 17.85966109, 0.0002, 17.85966109, 0.0132, 11.11400907, 0.027, -17.85966109, -0.0002, -17.85966109, -0.0132, -11.11400907, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402003, 50.01169801, 0.0002, 60.33316773, 0.009, 60.33316773, 0.02, -50.01169801, -0.0002, -60.33316773, -0.009, -60.33316773, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402003, 'My', 302003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12003, 2003, 12003, 12003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 17.65, 0.0, 5.3, '-mass', 11.531768603465853, 11.531768603465853, 11.531768603465853, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 17.475, 0.0, 5.3)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(32004, 17.825, 0.0, 5.3)
    ops.element('elasticBeamColumn', 32004, 2004, 32004, 99999, 88888)
    ops.node(22004, 17.65, 0.0, 4.95)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 17.65, 0.0, 5.65)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 17.65, 0.175, 5.3)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302004, 17.85966109, 0.0002, 17.85966109, 0.0132, 11.11400907, 0.027, -17.85966109, -0.0002, -17.85966109, -0.0132, -11.11400907, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402004, 50.01169801, 0.0002, 60.33316773, 0.009, 60.33316773, 0.02, -50.01169801, -0.0002, -60.33316773, -0.009, -60.33316773, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402004, 'My', 302004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12004, 2004, 12004, 12004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 2)
    # Central joint node
    ops.node(2005, 24.95, 0.0, 5.3, '-mass', 18.526636085626915, 18.526636085626915, 18.526636085626915, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52005, 24.725, 0.0, 5.3)
    ops.element('elasticBeamColumn', 52005, 52005, 2005, 99999, 88888)
    ops.node(32005, 25.175, 0.0, 5.3)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 24.95, 0.0, 4.95)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 24.95, 0.0, 5.65)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(42005, 24.95, 0.225, 5.3)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302005, 19.40968362, 0.0002, 19.40968362, 0.0132, 12.1220436, 0.027, -19.40968362, -0.0002, -19.40968362, -0.0132, -12.1220436, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402005, 54.50077327, 0.0002, 65.78368506, 0.009, 65.78368506, 0.02, -54.50077327, -0.0002, -65.78368506, -0.009, -65.78368506, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402005, 'My', 302005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12005, 2005, 12005, 12005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 2)
    # Central joint node
    ops.node(2006, 32.25, 0.0, 5.3, '-mass', 10.667089704383285, 10.667089704383285, 10.667089704383285, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 32.1, 0.0, 5.3)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(22006, 32.25, 0.0, 4.95)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 32.25, 0.0, 5.65)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(42006, 32.25, 0.15, 5.3)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302006, 10.6473525, 0.0002, 10.6473525, 0.0132, 6.61370972, 0.027, -10.6473525, -0.0002, -10.6473525, -0.0132, -6.61370972, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402006, 19.86049657, 0.0002, 19.86049657, 0.0132, 12.20098494, 0.027, -19.86049657, -0.0002, -19.86049657, -0.0132, -12.20098494, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402006, 'My', 302006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12006, 2006, 12006, 12006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2007, 0.0, 3.65, 5.3, '-mass', 13.860988786952088, 13.860988786952088, 13.860988786952088, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32007, 0.175, 3.65, 5.3)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 0.0, 3.65, 4.95)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 0.0, 3.65, 5.65)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 0.0, 3.475, 5.3)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 0.0, 3.825, 5.3)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302007, 20.63030447, 0.0002, 24.89192453, 0.009, 24.89192453, 0.02, -20.63030447, -0.0002, -24.89192453, -0.009, -24.89192453, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402007, 27.14227972, 0.0002, 27.14227972, 0.0132, 16.7524264, 0.027, -27.14227972, -0.0002, -27.14227972, -0.0132, -16.7524264, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402007, 'My', 302007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12007, 2007, 12007, 12007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2008, 7.3, 3.65, 5.3, '-mass', 22.106890927624868, 22.106890927624868, 22.106890927624868, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 7.05, 3.65, 5.3)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(32008, 7.55, 3.65, 5.3)
    ops.element('elasticBeamColumn', 32008, 2008, 32008, 99999, 88888)
    ops.node(22008, 7.3, 3.65, 4.95)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 7.3, 3.65, 5.65)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 7.3, 3.4, 5.3)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 7.3, 3.9, 5.3)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302008, 33.35573383, 0.0002, 40.26895222, 0.009, 40.26895222, 0.02, -33.35573383, -0.0002, -40.26895222, -0.009, -40.26895222, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402008, 65.18219614, 0.0002, 78.69168027, 0.009, 78.69168027, 0.02, -65.18219614, -0.0002, -78.69168027, -0.009, -78.69168027, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402008, 'My', 302008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12008, 2008, 12008, 12008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2009, 14.6, 3.65, 5.3, '-mass', 17.610014016309883, 17.610014016309883, 17.610014016309883, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52009, 14.375, 3.65, 5.3)
    ops.element('elasticBeamColumn', 52009, 52009, 2009, 99999, 88888)
    ops.node(32009, 14.825, 3.65, 5.3)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 14.6, 3.65, 4.95)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 14.6, 3.65, 5.65)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 14.6, 3.425, 5.3)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 14.6, 3.875, 5.3)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302009, 30.31783592, 0.0002, 36.60616809, 0.009, 36.60616809, 0.02, -30.31783592, -0.0002, -36.60616809, -0.009, -36.60616809, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402009, 51.74586845, 0.0002, 62.47866648, 0.009, 62.47866648, 0.02, -51.74586845, -0.0002, -62.47866648, -0.009, -62.47866648, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402009, 'My', 302009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12009, 2009, 12009, 12009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2010, 17.65, 3.65, 5.3, '-mass', 17.610014016309886, 17.610014016309886, 17.610014016309886, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 17.425, 3.65, 5.3)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 17.875, 3.65, 5.3)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 17.65, 3.65, 4.95)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 17.65, 3.65, 5.65)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 17.65, 3.425, 5.3)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 17.65, 3.875, 5.3)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302010, 30.31783592, 0.0002, 36.60616809, 0.009, 36.60616809, 0.02, -30.31783592, -0.0002, -36.60616809, -0.009, -36.60616809, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402010, 51.74586845, 0.0002, 62.47866648, 0.009, 62.47866648, 0.02, -51.74586845, -0.0002, -62.47866648, -0.009, -62.47866648, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402010, 'My', 302010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12010, 2010, 12010, 12010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 2)
    # Central joint node
    ops.node(2011, 24.95, 3.65, 5.3, '-mass', 22.10689092762487, 22.10689092762487, 22.10689092762487, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 24.7, 3.65, 5.3)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 25.2, 3.65, 5.3)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 24.95, 3.65, 4.95)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 24.95, 3.65, 5.65)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 24.95, 3.4, 5.3)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 24.95, 3.9, 5.3)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302011, 33.35573383, 0.0002, 40.26895222, 0.009, 40.26895222, 0.02, -33.35573383, -0.0002, -40.26895222, -0.009, -40.26895222, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402011, 65.18219614, 0.0002, 78.69168027, 0.009, 78.69168027, 0.02, -65.18219614, -0.0002, -78.69168027, -0.009, -78.69168027, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402011, 'My', 302011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12011, 2011, 12011, 12011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 2)
    # Central joint node
    ops.node(2012, 32.25, 3.65, 5.3, '-mass', 13.86098878695209, 13.86098878695209, 13.86098878695209, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 32.075, 3.65, 5.3)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 32.25, 3.65, 4.95)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 32.25, 3.65, 5.65)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 32.25, 3.475, 5.3)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 32.25, 3.825, 5.3)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302012, 20.63030447, 0.0002, 24.89192453, 0.009, 24.89192453, 0.02, -20.63030447, -0.0002, -24.89192453, -0.009, -24.89192453, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402012, 27.14227972, 0.0002, 27.14227972, 0.0132, 16.7524264, 0.027, -27.14227972, -0.0002, -27.14227972, -0.0132, -16.7524264, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402012, 'My', 302012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12012, 2012, 12012, 12012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2013, 0.0, 7.3, 5.3, '-mass', 10.667089704383283, 10.667089704383283, 10.667089704383283, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.15, 7.3, 5.3)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 7.3, 4.95)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 7.3, 5.65)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 7.15, 5.3)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302013, 10.6473525, 0.0002, 10.6473525, 0.0132, 6.61370972, 0.027, -10.6473525, -0.0002, -10.6473525, -0.0132, -6.61370972, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402013, 19.86049657, 0.0002, 19.86049657, 0.0132, 12.20098494, 0.027, -19.86049657, -0.0002, -19.86049657, -0.0132, -12.20098494, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402013, 'My', 302013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12013, 2013, 12013, 12013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2014, 7.3, 7.3, 5.3, '-mass', 18.52663608562691, 18.52663608562691, 18.52663608562691, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 7.075, 7.3, 5.3)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 7.525, 7.3, 5.3)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 7.3, 7.3, 4.95)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 7.3, 7.3, 5.65)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 7.3, 7.075, 5.3)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302014, 19.40968362, 0.0002, 19.40968362, 0.0132, 12.1220436, 0.027, -19.40968362, -0.0002, -19.40968362, -0.0132, -12.1220436, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402014, 54.50077327, 0.0002, 65.78368506, 0.009, 65.78368506, 0.02, -54.50077327, -0.0002, -65.78368506, -0.009, -65.78368506, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402014, 'My', 302014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12014, 2014, 12014, 12014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2015, 14.6, 7.3, 5.3, '-mass', 13.036062691131498, 13.036062691131498, 13.036062691131498, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 14.425, 7.3, 5.3)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 14.775, 7.3, 5.3)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 14.6, 7.3, 4.95)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 14.6, 7.3, 5.65)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 14.6, 7.125, 5.3)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302015, 14.65305112, 0.0002, 14.65305112, 0.0132, 9.11398535, 0.027, -14.65305112, -0.0002, -14.65305112, -0.0132, -9.11398535, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402015, 35.49374913, 0.0002, 42.82436423, 0.009, 42.82436423, 0.02, -35.49374913, -0.0002, -42.82436423, -0.009, -42.82436423, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402015, 'My', 302015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12015, 2015, 12015, 12015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2016, 17.65, 7.3, 5.3, '-mass', 13.0360626911315, 13.0360626911315, 13.0360626911315, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 17.475, 7.3, 5.3)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(32016, 17.825, 7.3, 5.3)
    ops.element('elasticBeamColumn', 32016, 2016, 32016, 99999, 88888)
    ops.node(22016, 17.65, 7.3, 4.95)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 17.65, 7.3, 5.65)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 17.65, 7.125, 5.3)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302016, 14.65305112, 0.0002, 14.65305112, 0.0132, 9.11398535, 0.027, -14.65305112, -0.0002, -14.65305112, -0.0132, -9.11398535, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402016, 35.49374913, 0.0002, 42.82436423, 0.009, 42.82436423, 0.02, -35.49374913, -0.0002, -42.82436423, -0.009, -42.82436423, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402016, 'My', 302016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12016, 2016, 12016, 12016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 2)
    # Central joint node
    ops.node(2017, 24.95, 7.3, 5.3, '-mass', 18.526636085626915, 18.526636085626915, 18.526636085626915, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52017, 24.725, 7.3, 5.3)
    ops.element('elasticBeamColumn', 52017, 52017, 2017, 99999, 88888)
    ops.node(32017, 25.175, 7.3, 5.3)
    ops.element('elasticBeamColumn', 32017, 2017, 32017, 99999, 88888)
    ops.node(22017, 24.95, 7.3, 4.95)
    ops.element('elasticBeamColumn', 22017, 22017, 2017, 99999, 99999)
    ops.node(72017, 24.95, 7.3, 5.65)
    ops.element('elasticBeamColumn', 72017, 2017, 72017, 99999, 99999)
    ops.node(62017, 24.95, 7.075, 5.3)
    ops.element('elasticBeamColumn', 62017, 62017, 2017, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302017, 19.40968362, 0.0002, 19.40968362, 0.0132, 12.1220436, 0.027, -19.40968362, -0.0002, -19.40968362, -0.0132, -12.1220436, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402017, 54.50077327, 0.0002, 65.78368506, 0.009, 65.78368506, 0.02, -54.50077327, -0.0002, -65.78368506, -0.009, -65.78368506, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402017, 'My', 302017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12017, 2017, 12017, 12017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 2)
    # Central joint node
    ops.node(2018, 32.25, 7.3, 5.3, '-mass', 10.667089704383285, 10.667089704383285, 10.667089704383285, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52018, 32.1, 7.3, 5.3)
    ops.element('elasticBeamColumn', 52018, 52018, 2018, 99999, 88888)
    ops.node(22018, 32.25, 7.3, 4.95)
    ops.element('elasticBeamColumn', 22018, 22018, 2018, 99999, 99999)
    ops.node(72018, 32.25, 7.3, 5.65)
    ops.element('elasticBeamColumn', 72018, 2018, 72018, 99999, 99999)
    ops.node(62018, 32.25, 7.15, 5.3)
    ops.element('elasticBeamColumn', 62018, 62018, 2018, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302018, 10.6473525, 0.0002, 10.6473525, 0.0132, 6.61370972, 0.027, -10.6473525, -0.0002, -10.6473525, -0.0132, -6.61370972, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402018, 19.86049657, 0.0002, 19.86049657, 0.0132, 12.20098494, 0.027, -19.86049657, -0.0002, -19.86049657, -0.0132, -12.20098494, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402018, 'My', 302018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12018, 2018, 12018, 12018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 7.95, '-mass', 10.488649337410806, 10.488649337410806, 10.488649337410806, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 7.95)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 7.6)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 8.3)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 7.95)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303001, 5.597848, 0.0002, 5.597848, 0.0132, 3.47306085, 0.027, -5.597848, -0.0002, -5.597848, -0.0132, -3.47306085, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403001, 13.39916351, 0.0002, 13.39916351, 0.0132, 8.16750887, 0.027, -13.39916351, -0.0002, -13.39916351, -0.0132, -8.16750887, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403001, 'My', 303001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13001, 3001, 13001, 13001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 7.3, 0.0, 7.95, '-mass', 18.08871559633027, 18.08871559633027, 18.08871559633027, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 7.125, 0.0, 7.95)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 7.475, 0.0, 7.95)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 7.3, 0.0, 7.6)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 7.3, 0.0, 8.3)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 7.3, 0.175, 7.95)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303002, 8.70306135, 0.0002, 8.70306135, 0.0132, 5.43990296, 0.027, -8.70306135, -0.0002, -8.70306135, -0.0132, -5.43990296, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403002, 33.78122081, 0.0002, 40.76897671, 0.009, 40.76897671, 0.02, -33.78122081, -0.0002, -40.76897671, -0.009, -40.76897671, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403002, 'My', 303002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13002, 3002, 13002, 13002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 14.6, 0.0, 7.95, '-mass', 11.28941386340469, 11.28941386340469, 11.28941386340469, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 14.475, 0.0, 7.95)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 14.725, 0.0, 7.95)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 14.6, 0.0, 7.6)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 14.6, 0.0, 8.3)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 14.6, 0.125, 7.95)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303003, 10.18147023, 0.0002, 10.18147023, 0.0132, 6.29754467, 0.027, -10.18147023, -0.0002, -10.18147023, -0.0132, -6.29754467, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403003, 27.76814116, 0.0002, 33.48627898, 0.009, 33.48627898, 0.02, -27.76814116, -0.0002, -33.48627898, -0.009, -33.48627898, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403003, 'My', 303003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13003, 3003, 13003, 13003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 17.65, 0.0, 7.95, '-mass', 11.289413863404691, 11.289413863404691, 11.289413863404691, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 17.525, 0.0, 7.95)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(33004, 17.775, 0.0, 7.95)
    ops.element('elasticBeamColumn', 33004, 3004, 33004, 99999, 88888)
    ops.node(23004, 17.65, 0.0, 7.6)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 17.65, 0.0, 8.3)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 17.65, 0.125, 7.95)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303004, 10.18147023, 0.0002, 10.18147023, 0.0132, 6.29754467, 0.027, -10.18147023, -0.0002, -10.18147023, -0.0132, -6.29754467, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403004, 27.76814116, 0.0002, 33.48627898, 0.009, 33.48627898, 0.02, -27.76814116, -0.0002, -33.48627898, -0.009, -33.48627898, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403004, 'My', 303004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13004, 3004, 13004, 13004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 3)
    # Central joint node
    ops.node(3005, 24.95, 0.0, 7.95, '-mass', 18.088715596330275, 18.088715596330275, 18.088715596330275, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53005, 24.775, 0.0, 7.95)
    ops.element('elasticBeamColumn', 53005, 53005, 3005, 99999, 88888)
    ops.node(33005, 25.125, 0.0, 7.95)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 24.95, 0.0, 7.6)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 24.95, 0.0, 8.3)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(43005, 24.95, 0.175, 7.95)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303005, 8.70306135, 0.0002, 8.70306135, 0.0132, 5.43990296, 0.027, -8.70306135, -0.0002, -8.70306135, -0.0132, -5.43990296, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403005, 33.78122081, 0.0002, 40.76897671, 0.009, 40.76897671, 0.02, -33.78122081, -0.0002, -40.76897671, -0.009, -40.76897671, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403005, 'My', 303005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13005, 3005, 13005, 13005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 3)
    # Central joint node
    ops.node(3006, 32.25, 0.0, 7.95, '-mass', 10.488649337410807, 10.488649337410807, 10.488649337410807, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 32.125, 0.0, 7.95)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(23006, 32.25, 0.0, 7.6)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 32.25, 0.0, 8.3)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(43006, 32.25, 0.125, 7.95)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303006, 5.597848, 0.0002, 5.597848, 0.0132, 3.47306085, 0.027, -5.597848, -0.0002, -5.597848, -0.0132, -3.47306085, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403006, 13.39916351, 0.0002, 13.39916351, 0.0132, 8.16750887, 0.027, -13.39916351, -0.0002, -13.39916351, -0.0132, -8.16750887, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403006, 'My', 303006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13006, 3006, 13006, 13006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3007, 0.0, 3.65, 7.95, '-mass', 13.487900101936797, 13.487900101936797, 13.487900101936797, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33007, 0.125, 3.65, 7.95)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 0.0, 3.65, 7.6)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 0.0, 3.65, 8.3)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 0.0, 3.525, 7.95)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 0.0, 3.775, 7.95)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303007, 9.90315079, 0.0002, 11.94954035, 0.009, 11.94954035, 0.02, -9.90315079, -0.0002, -11.94954035, -0.009, -11.94954035, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403007, 15.93574038, 0.0002, 15.93574038, 0.0132, 9.78105677, 0.027, -15.93574038, -0.0002, -15.93574038, -0.0132, -9.78105677, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403007, 'My', 303007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13007, 3007, 13007, 13007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3008, 7.3, 3.65, 7.95, '-mass', 21.4579612640163, 21.4579612640163, 21.4579612640163, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 7.1, 3.65, 7.95)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(33008, 7.5, 3.65, 7.95)
    ops.element('elasticBeamColumn', 33008, 3008, 33008, 99999, 88888)
    ops.node(23008, 7.3, 3.65, 7.6)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 7.3, 3.65, 8.3)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 7.3, 3.45, 7.95)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 7.3, 3.85, 7.95)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303008, 15.93268108, 0.0002, 19.23138674, 0.009, 19.23138674, 0.02, -15.93268108, -0.0002, -19.23138674, -0.009, -19.23138674, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403008, 42.95883237, 0.0002, 51.85303812, 0.009, 51.85303812, 0.02, -42.95883237, -0.0002, -51.85303812, -0.009, -51.85303812, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403008, 'My', 303008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13008, 3008, 13008, 13008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3009, 14.6, 3.65, 7.95, '-mass', 17.060472731906216, 17.060472731906216, 17.060472731906216, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53009, 14.425, 3.65, 7.95)
    ops.element('elasticBeamColumn', 53009, 53009, 3009, 99999, 88888)
    ops.node(33009, 14.775, 3.65, 7.95)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 14.6, 3.65, 7.6)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 14.6, 3.65, 8.3)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 14.6, 3.475, 7.95)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 14.6, 3.825, 7.95)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303009, 18.0388353, 0.0002, 21.78247808, 0.009, 21.78247808, 0.02, -18.0388353, -0.0002, -21.78247808, -0.009, -21.78247808, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403009, 32.94264299, 0.0002, 39.7627195, 0.009, 39.7627195, 0.02, -32.94264299, -0.0002, -39.7627195, -0.009, -39.7627195, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403009, 'My', 303009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13009, 3009, 13009, 13009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3010, 17.65, 3.65, 7.95, '-mass', 17.060472731906216, 17.060472731906216, 17.060472731906216, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 17.475, 3.65, 7.95)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 17.825, 3.65, 7.95)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 17.65, 3.65, 7.6)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 17.65, 3.65, 8.3)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 17.65, 3.475, 7.95)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 17.65, 3.825, 7.95)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303010, 18.0388353, 0.0002, 21.78247808, 0.009, 21.78247808, 0.02, -18.0388353, -0.0002, -21.78247808, -0.009, -21.78247808, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403010, 32.94264299, 0.0002, 39.7627195, 0.009, 39.7627195, 0.02, -32.94264299, -0.0002, -39.7627195, -0.009, -39.7627195, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403010, 'My', 303010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13010, 3010, 13010, 13010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 3)
    # Central joint node
    ops.node(3011, 24.95, 3.65, 7.95, '-mass', 21.457961264016305, 21.457961264016305, 21.457961264016305, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 24.75, 3.65, 7.95)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 25.15, 3.65, 7.95)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 24.95, 3.65, 7.6)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 24.95, 3.65, 8.3)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 24.95, 3.45, 7.95)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 24.95, 3.85, 7.95)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303011, 15.93268108, 0.0002, 19.23138674, 0.009, 19.23138674, 0.02, -15.93268108, -0.0002, -19.23138674, -0.009, -19.23138674, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403011, 42.95883237, 0.0002, 51.85303812, 0.009, 51.85303812, 0.02, -42.95883237, -0.0002, -51.85303812, -0.009, -51.85303812, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403011, 'My', 303011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13011, 3011, 13011, 13011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 3)
    # Central joint node
    ops.node(3012, 32.25, 3.65, 7.95, '-mass', 13.487900101936798, 13.487900101936798, 13.487900101936798, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 32.125, 3.65, 7.95)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 32.25, 3.65, 7.6)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 32.25, 3.65, 8.3)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 32.25, 3.525, 7.95)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 32.25, 3.775, 7.95)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303012, 9.90315079, 0.0002, 11.94954035, 0.009, 11.94954035, 0.02, -9.90315079, -0.0002, -11.94954035, -0.009, -11.94954035, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403012, 15.93574038, 0.0002, 15.93574038, 0.0132, 9.78105677, 0.027, -15.93574038, -0.0002, -15.93574038, -0.0132, -9.78105677, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403012, 'My', 303012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13012, 3012, 13012, 13012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3013, 0.0, 7.3, 7.95, '-mass', 10.488649337410806, 10.488649337410806, 10.488649337410806, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.125, 7.3, 7.95)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 7.3, 7.6)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 7.3, 8.3)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 7.175, 7.95)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303013, 5.597848, 0.0002, 5.597848, 0.0132, 3.47306085, 0.027, -5.597848, -0.0002, -5.597848, -0.0132, -3.47306085, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403013, 13.39916351, 0.0002, 13.39916351, 0.0132, 8.16750887, 0.027, -13.39916351, -0.0002, -13.39916351, -0.0132, -8.16750887, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403013, 'My', 303013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13013, 3013, 13013, 13013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3014, 7.3, 7.3, 7.95, '-mass', 18.08871559633027, 18.08871559633027, 18.08871559633027, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 7.125, 7.3, 7.95)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 7.475, 7.3, 7.95)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 7.3, 7.3, 7.6)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 7.3, 7.3, 8.3)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 7.3, 7.125, 7.95)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303014, 8.70306135, 0.0002, 8.70306135, 0.0132, 5.43990296, 0.027, -8.70306135, -0.0002, -8.70306135, -0.0132, -5.43990296, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403014, 33.78122081, 0.0002, 40.76897671, 0.009, 40.76897671, 0.02, -33.78122081, -0.0002, -40.76897671, -0.009, -40.76897671, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403014, 'My', 303014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13014, 3014, 13014, 13014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3015, 14.6, 7.3, 7.95, '-mass', 12.696460244648318, 12.696460244648318, 12.696460244648318, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 14.475, 7.3, 7.95)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 14.725, 7.3, 7.95)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 14.6, 7.3, 7.6)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 14.6, 7.3, 8.3)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 14.6, 7.175, 7.95)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303015, 8.74266343, 0.0002, 8.74266343, 0.0132, 5.40725052, 0.027, -8.74266343, -0.0002, -8.74266343, -0.0132, -5.40725052, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403015, 20.1591656, 0.0002, 24.31067978, 0.009, 24.31067978, 0.02, -20.1591656, -0.0002, -24.31067978, -0.009, -24.31067978, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403015, 'My', 303015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13015, 3015, 13015, 13015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3016, 17.65, 7.3, 7.95, '-mass', 12.69646024464832, 12.69646024464832, 12.69646024464832, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 17.525, 7.3, 7.95)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(33016, 17.775, 7.3, 7.95)
    ops.element('elasticBeamColumn', 33016, 3016, 33016, 99999, 88888)
    ops.node(23016, 17.65, 7.3, 7.6)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 17.65, 7.3, 8.3)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 17.65, 7.175, 7.95)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303016, 8.74266343, 0.0002, 8.74266343, 0.0132, 5.40725052, 0.027, -8.74266343, -0.0002, -8.74266343, -0.0132, -5.40725052, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403016, 20.1591656, 0.0002, 24.31067978, 0.009, 24.31067978, 0.02, -20.1591656, -0.0002, -24.31067978, -0.009, -24.31067978, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403016, 'My', 303016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13016, 3016, 13016, 13016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 3)
    # Central joint node
    ops.node(3017, 24.95, 7.3, 7.95, '-mass', 18.088715596330275, 18.088715596330275, 18.088715596330275, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53017, 24.775, 7.3, 7.95)
    ops.element('elasticBeamColumn', 53017, 53017, 3017, 99999, 88888)
    ops.node(33017, 25.125, 7.3, 7.95)
    ops.element('elasticBeamColumn', 33017, 3017, 33017, 99999, 88888)
    ops.node(23017, 24.95, 7.3, 7.6)
    ops.element('elasticBeamColumn', 23017, 23017, 3017, 99999, 99999)
    ops.node(73017, 24.95, 7.3, 8.3)
    ops.element('elasticBeamColumn', 73017, 3017, 73017, 99999, 99999)
    ops.node(63017, 24.95, 7.125, 7.95)
    ops.element('elasticBeamColumn', 63017, 63017, 3017, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303017, 8.70306135, 0.0002, 8.70306135, 0.0132, 5.43990296, 0.027, -8.70306135, -0.0002, -8.70306135, -0.0132, -5.43990296, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403017, 33.78122081, 0.0002, 40.76897671, 0.009, 40.76897671, 0.02, -33.78122081, -0.0002, -40.76897671, -0.009, -40.76897671, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403017, 'My', 303017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13017, 3017, 13017, 13017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 3)
    # Central joint node
    ops.node(3018, 32.25, 7.3, 7.95, '-mass', 10.488649337410807, 10.488649337410807, 10.488649337410807, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53018, 32.125, 7.3, 7.95)
    ops.element('elasticBeamColumn', 53018, 53018, 3018, 99999, 88888)
    ops.node(23018, 32.25, 7.3, 7.6)
    ops.element('elasticBeamColumn', 23018, 23018, 3018, 99999, 99999)
    ops.node(73018, 32.25, 7.3, 8.3)
    ops.element('elasticBeamColumn', 73018, 3018, 73018, 99999, 99999)
    ops.node(63018, 32.25, 7.175, 7.95)
    ops.element('elasticBeamColumn', 63018, 63018, 3018, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303018, 5.597848, 0.0002, 5.597848, 0.0132, 3.47306085, 0.027, -5.597848, -0.0002, -5.597848, -0.0132, -3.47306085, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403018, 13.39916351, 0.0002, 13.39916351, 0.0132, 8.16750887, 0.027, -13.39916351, -0.0002, -13.39916351, -0.0132, -8.16750887, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403018, 'My', 303018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13018, 3018, 13018, 13018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 10.6, '-mass', 5.123588175331294, 5.123588175331294, 5.123588175331294, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 10.6)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 10.35)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 10.6)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304001, 5.642227, 0.0002, 5.642227, 0.0132, 3.45052615, 0.027, -5.642227, -0.0002, -5.642227, -0.0132, -3.45052615, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404001, 8.9468376, 0.0002, 8.9468376, 0.0132, 5.39204515, 0.027, -8.9468376, -0.0002, -8.9468376, -0.0132, -5.39204515, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404001, 'My', 304001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14001, 4001, 14001, 14001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 7.3, 0.0, 10.6, '-mass', 9.971182466870541, 9.971182466870541, 9.971182466870541, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 7.125, 0.0, 10.6)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 7.475, 0.0, 10.6)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 7.3, 0.0, 10.35)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 7.3, 0.175, 10.6)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304002, 9.7640387, 0.0002, 9.7640387, 0.0132, 6.03803208, 0.027, -9.7640387, -0.0002, -9.7640387, -0.0132, -6.03803208, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404002, 16.86831021, 0.0002, 16.86831021, 0.0132, 10.29645592, 0.027, -16.86831021, -0.0002, -16.86831021, -0.0132, -10.29645592, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404002, 'My', 304002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14002, 4002, 14002, 14002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 14.6, 0.0, 10.6, '-mass', 5.581921508664628, 5.581921508664628, 5.581921508664628, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 14.475, 0.0, 10.6)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 14.725, 0.0, 10.6)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 14.6, 0.0, 10.35)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 14.6, 0.125, 10.6)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304003, 5.84603213, 0.0002, 5.84603213, 0.0132, 3.58062582, 0.027, -5.84603213, -0.0002, -5.84603213, -0.0132, -3.58062582, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404003, 9.25606359, 0.0002, 9.25606359, 0.0132, 5.58976288, 0.027, -9.25606359, -0.0002, -9.25606359, -0.0132, -5.58976288, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404003, 'My', 304003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14003, 4003, 14003, 14003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 17.65, 0.0, 10.6, '-mass', 5.581921508664628, 5.581921508664628, 5.581921508664628, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 17.525, 0.0, 10.6)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(34004, 17.775, 0.0, 10.6)
    ops.element('elasticBeamColumn', 34004, 4004, 34004, 99999, 88888)
    ops.node(24004, 17.65, 0.0, 10.35)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 17.65, 0.125, 10.6)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304004, 5.84603213, 0.0002, 5.84603213, 0.0132, 3.58062582, 0.027, -5.84603213, -0.0002, -5.84603213, -0.0132, -3.58062582, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404004, 9.25606359, 0.0002, 9.25606359, 0.0132, 5.58976288, 0.027, -9.25606359, -0.0002, -9.25606359, -0.0132, -5.58976288, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404004, 'My', 304004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14004, 4004, 14004, 14004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 4)
    # Central joint node
    ops.node(4005, 24.95, 0.0, 10.6, '-mass', 9.971182466870541, 9.971182466870541, 9.971182466870541, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54005, 24.775, 0.0, 10.6)
    ops.element('elasticBeamColumn', 54005, 54005, 4005, 99999, 88888)
    ops.node(34005, 25.125, 0.0, 10.6)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 24.95, 0.0, 10.35)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(44005, 24.95, 0.175, 10.6)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304005, 9.7640387, 0.0002, 9.7640387, 0.0132, 6.03803208, 0.027, -9.7640387, -0.0002, -9.7640387, -0.0132, -6.03803208, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404005, 16.86831021, 0.0002, 16.86831021, 0.0132, 10.29645592, 0.027, -16.86831021, -0.0002, -16.86831021, -0.0132, -10.29645592, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404005, 'My', 304005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14005, 4005, 14005, 14005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 4)
    # Central joint node
    ops.node(4006, 32.25, 0.0, 10.6, '-mass', 5.123588175331294, 5.123588175331294, 5.123588175331294, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 32.125, 0.0, 10.6)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(24006, 32.25, 0.0, 10.35)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(44006, 32.25, 0.125, 10.6)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304006, 5.642227, 0.0002, 5.642227, 0.0132, 3.45052615, 0.027, -5.642227, -0.0002, -5.642227, -0.0132, -3.45052615, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404006, 8.9468376, 0.0002, 8.9468376, 0.0132, 5.39204515, 0.027, -8.9468376, -0.0002, -8.9468376, -0.0132, -5.39204515, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404006, 'My', 304006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14006, 4006, 14006, 14006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4007, 0.0, 3.65, 10.6, '-mass', 9.39717635066259, 9.39717635066259, 9.39717635066259, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34007, 0.125, 3.65, 10.6)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 0.0, 3.65, 10.275)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 0.0, 3.525, 10.6)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 0.0, 3.775, 10.6)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304007, 8.06908837, 0.0002, 8.06908837, 0.0132, 4.97335704, 0.027, -8.06908837, -0.0002, -8.06908837, -0.0132, -4.97335704, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404007, 15.5831692, 0.0002, 15.5831692, 0.0132, 9.42435858, 0.027, -15.5831692, -0.0002, -15.5831692, -0.0132, -9.42435858, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404007, 'My', 304007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14007, 4007, 14007, 14007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4008, 7.3, 3.65, 10.6, '-mass', 18.372028542303767, 18.372028542303767, 18.372028542303767, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 7.1, 3.65, 10.6)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(34008, 7.5, 3.65, 10.6)
    ops.element('elasticBeamColumn', 34008, 4008, 34008, 99999, 88888)
    ops.node(24008, 7.3, 3.65, 10.275)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 7.3, 3.45, 10.6)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 7.3, 3.85, 10.6)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304008, 13.93648402, 0.0002, 13.93648402, 0.0132, 8.66076281, 0.027, -13.93648402, -0.0002, -13.93648402, -0.0132, -8.66076281, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404008, 31.73630654, 0.0002, 31.73630654, 0.0132, 19.36935926, 0.027, -31.73630654, -0.0002, -31.73630654, -0.0132, -19.36935926, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404008, 'My', 304008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14008, 4008, 14008, 14008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4009, 14.6, 3.65, 10.6, '-mass', 13.532809633027522, 13.532809633027522, 13.532809633027522, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54009, 14.425, 3.65, 10.6)
    ops.element('elasticBeamColumn', 54009, 54009, 4009, 99999, 88888)
    ops.node(34009, 14.775, 3.65, 10.6)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 14.6, 3.65, 10.275)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 14.6, 3.475, 10.6)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 14.6, 3.825, 10.6)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304009, 10.54546689, 0.0002, 10.54546689, 0.0132, 6.53576622, 0.027, -10.54546689, -0.0002, -10.54546689, -0.0132, -6.53576622, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404009, 24.21046463, 0.0002, 24.21046463, 0.0132, 14.69323592, 0.027, -24.21046463, -0.0002, -24.21046463, -0.0132, -14.69323592, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404009, 'My', 304009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14009, 4009, 14009, 14009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4010, 17.65, 3.65, 10.6, '-mass', 13.532809633027524, 13.532809633027524, 13.532809633027524, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 17.475, 3.65, 10.6)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 17.825, 3.65, 10.6)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 17.65, 3.65, 10.275)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 17.65, 3.475, 10.6)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 17.65, 3.825, 10.6)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304010, 10.54546689, 0.0002, 10.54546689, 0.0132, 6.53576622, 0.027, -10.54546689, -0.0002, -10.54546689, -0.0132, -6.53576622, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404010, 24.21046463, 0.0002, 24.21046463, 0.0132, 14.69323592, 0.027, -24.21046463, -0.0002, -24.21046463, -0.0132, -14.69323592, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404010, 'My', 304010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14010, 4010, 14010, 14010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 4)
    # Central joint node
    ops.node(4011, 24.95, 3.65, 10.6, '-mass', 18.37202854230377, 18.37202854230377, 18.37202854230377, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 24.75, 3.65, 10.6)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 25.15, 3.65, 10.6)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 24.95, 3.65, 10.275)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 24.95, 3.45, 10.6)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 24.95, 3.85, 10.6)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304011, 13.93648402, 0.0002, 13.93648402, 0.0132, 8.66076281, 0.027, -13.93648402, -0.0002, -13.93648402, -0.0132, -8.66076281, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404011, 31.73630654, 0.0002, 31.73630654, 0.0132, 19.36935926, 0.027, -31.73630654, -0.0002, -31.73630654, -0.0132, -19.36935926, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404011, 'My', 304011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14011, 4011, 14011, 14011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 4)
    # Central joint node
    ops.node(4012, 32.25, 3.65, 10.6, '-mass', 9.397176350662592, 9.397176350662592, 9.397176350662592, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 32.125, 3.65, 10.6)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 32.25, 3.65, 10.275)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 32.25, 3.525, 10.6)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 32.25, 3.775, 10.6)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304012, 8.06908837, 0.0002, 8.06908837, 0.0132, 4.97335704, 0.027, -8.06908837, -0.0002, -8.06908837, -0.0132, -4.97335704, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404012, 15.5831692, 0.0002, 15.5831692, 0.0132, 9.42435858, 0.027, -15.5831692, -0.0002, -15.5831692, -0.0132, -9.42435858, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404012, 'My', 304012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14012, 4012, 14012, 14012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4013, 0.0, 7.3, 10.6, '-mass', 5.123588175331294, 5.123588175331294, 5.123588175331294, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.125, 7.3, 10.6)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 7.3, 10.35)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 7.175, 10.6)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304013, 5.642227, 0.0002, 5.642227, 0.0132, 3.45052615, 0.027, -5.642227, -0.0002, -5.642227, -0.0132, -3.45052615, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404013, 8.9468376, 0.0002, 8.9468376, 0.0132, 5.39204515, 0.027, -8.9468376, -0.0002, -8.9468376, -0.0132, -5.39204515, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404013, 'My', 304013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14013, 4013, 14013, 14013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4014, 7.3, 7.3, 10.6, '-mass', 9.971182466870541, 9.971182466870541, 9.971182466870541, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 7.125, 7.3, 10.6)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 7.475, 7.3, 10.6)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 7.3, 7.3, 10.35)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 7.3, 7.125, 10.6)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304014, 9.7640387, 0.0002, 9.7640387, 0.0132, 6.03803208, 0.027, -9.7640387, -0.0002, -9.7640387, -0.0132, -6.03803208, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404014, 16.86831021, 0.0002, 16.86831021, 0.0132, 10.29645592, 0.027, -16.86831021, -0.0002, -16.86831021, -0.0132, -10.29645592, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404014, 'My', 304014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14014, 4014, 14014, 14014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4015, 14.6, 7.3, 10.6, '-mass', 6.9315137614678894, 6.9315137614678894, 6.9315137614678894, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 14.475, 7.3, 10.6)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 14.725, 7.3, 10.6)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 14.6, 7.3, 10.35)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 14.6, 7.175, 10.6)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304015, 6.46252215, 0.0002, 6.46252215, 0.0132, 3.97376655, 0.027, -6.46252215, -0.0002, -6.46252215, -0.0132, -3.97376655, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404015, 10.19179088, 0.0002, 10.19179088, 0.0132, 6.18732724, 0.027, -10.19179088, -0.0002, -10.19179088, -0.0132, -6.18732724, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404015, 'My', 304015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14015, 4015, 14015, 14015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4016, 17.65, 7.3, 10.6, '-mass', 6.9315137614678894, 6.9315137614678894, 6.9315137614678894, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 17.525, 7.3, 10.6)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(34016, 17.775, 7.3, 10.6)
    ops.element('elasticBeamColumn', 34016, 4016, 34016, 99999, 88888)
    ops.node(24016, 17.65, 7.3, 10.35)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 17.65, 7.175, 10.6)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304016, 6.46252215, 0.0002, 6.46252215, 0.0132, 3.97376655, 0.027, -6.46252215, -0.0002, -6.46252215, -0.0132, -3.97376655, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404016, 10.19179088, 0.0002, 10.19179088, 0.0132, 6.18732724, 0.027, -10.19179088, -0.0002, -10.19179088, -0.0132, -6.18732724, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404016, 'My', 304016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14016, 4016, 14016, 14016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 4)
    # Central joint node
    ops.node(4017, 24.95, 7.3, 10.6, '-mass', 9.971182466870541, 9.971182466870541, 9.971182466870541, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54017, 24.775, 7.3, 10.6)
    ops.element('elasticBeamColumn', 54017, 54017, 4017, 99999, 88888)
    ops.node(34017, 25.125, 7.3, 10.6)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 24.95, 7.3, 10.35)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(64017, 24.95, 7.125, 10.6)
    ops.element('elasticBeamColumn', 64017, 64017, 4017, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304017, 9.7640387, 0.0002, 9.7640387, 0.0132, 6.03803208, 0.027, -9.7640387, -0.0002, -9.7640387, -0.0132, -6.03803208, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404017, 16.86831021, 0.0002, 16.86831021, 0.0132, 10.29645592, 0.027, -16.86831021, -0.0002, -16.86831021, -0.0132, -10.29645592, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404017, 'My', 304017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14017, 4017, 14017, 14017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 4)
    # Central joint node
    ops.node(4018, 32.25, 7.3, 10.6, '-mass', 5.123588175331294, 5.123588175331294, 5.123588175331294, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 32.125, 7.3, 10.6)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(24018, 32.25, 7.3, 10.35)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(64018, 32.25, 7.175, 10.6)
    ops.element('elasticBeamColumn', 64018, 64018, 4018, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304018, 5.642227, 0.0002, 5.642227, 0.0132, 3.45052615, 0.027, -5.642227, -0.0002, -5.642227, -0.0132, -3.45052615, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404018, 8.9468376, 0.0002, 8.9468376, 0.0132, 5.39204515, 0.027, -8.9468376, -0.0002, -8.9468376, -0.0132, -5.39204515, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404018, 'My', 304018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14018, 4018, 14018, 14018, '-orient', 0, 0, 1, 0, 1, 0)
