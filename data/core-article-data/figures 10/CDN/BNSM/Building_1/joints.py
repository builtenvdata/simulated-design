import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (2, 0, 0.5)
    # Central joint node
    ops.node(4025, 9.0, 0.0, 1.55, '-mass', 3.3695718654434255, 3.3695718654434255, 3.3695718654434255, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34025, 9.15, 0.0, 1.55)
    ops.element('elasticBeamColumn', 34025, 4025, 34025, 99999, 88888)
    ops.node(24025, 9.0, 0.0, 1.375)
    ops.element('elasticBeamColumn', 24025, 24025, 4025, 99999, 99999)
    ops.node(74025, 9.0, 0.0, 1.725)
    ops.element('elasticBeamColumn', 74025, 4025, 74025, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 0.5)
    # Central joint node
    ops.node(4026, 12.0, 0.0, 1.55, '-mass', 3.3695718654434255, 3.3695718654434255, 3.3695718654434255, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54026, 11.85, 0.0, 1.55)
    ops.element('elasticBeamColumn', 54026, 54026, 4026, 99999, 88888)
    ops.node(24026, 12.0, 0.0, 1.375)
    ops.element('elasticBeamColumn', 24026, 24026, 4026, 99999, 99999)
    ops.node(74026, 12.0, 0.0, 1.725)
    ops.element('elasticBeamColumn', 74026, 4026, 74026, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 1.5)
    # Central joint node
    ops.node(4027, 9.0, 0.0, 4.5, '-mass', 3.3365443425076453, 3.3365443425076453, 3.3365443425076453, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34027, 9.15, 0.0, 4.5)
    ops.element('elasticBeamColumn', 34027, 4027, 34027, 99999, 88888)
    ops.node(24027, 9.0, 0.0, 4.325)
    ops.element('elasticBeamColumn', 24027, 24027, 4027, 99999, 99999)
    ops.node(74027, 9.0, 0.0, 4.675)
    ops.element('elasticBeamColumn', 74027, 4027, 74027, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 1.5)
    # Central joint node
    ops.node(4028, 12.0, 0.0, 4.5, '-mass', 3.3365443425076453, 3.3365443425076453, 3.3365443425076453, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54028, 11.85, 0.0, 4.5)
    ops.element('elasticBeamColumn', 54028, 54028, 4028, 99999, 88888)
    ops.node(24028, 12.0, 0.0, 4.325)
    ops.element('elasticBeamColumn', 24028, 24028, 4028, 99999, 99999)
    ops.node(74028, 12.0, 0.0, 4.675)
    ops.element('elasticBeamColumn', 74028, 4028, 74028, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 2.5)
    # Central joint node
    ops.node(4029, 9.0, 0.0, 7.3, '-mass', 3.242354740061162, 3.242354740061162, 3.242354740061162, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34029, 9.125, 0.0, 7.3)
    ops.element('elasticBeamColumn', 34029, 4029, 34029, 99999, 88888)
    ops.node(24029, 9.0, 0.0, 7.125)
    ops.element('elasticBeamColumn', 24029, 24029, 4029, 99999, 99999)
    ops.node(74029, 9.0, 0.0, 7.475)
    ops.element('elasticBeamColumn', 74029, 4029, 74029, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 2.5)
    # Central joint node
    ops.node(4030, 12.0, 0.0, 7.3, '-mass', 3.242354740061162, 3.242354740061162, 3.242354740061162, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54030, 11.875, 0.0, 7.3)
    ops.element('elasticBeamColumn', 54030, 54030, 4030, 99999, 88888)
    ops.node(24030, 12.0, 0.0, 7.125)
    ops.element('elasticBeamColumn', 24030, 24030, 4030, 99999, 99999)
    ops.node(74030, 12.0, 0.0, 7.475)
    ops.element('elasticBeamColumn', 74030, 4030, 74030, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 3.5)
    # Central joint node
    ops.node(4031, 9.0, 0.0, 10.1, '-mass', 3.242354740061162, 3.242354740061162, 3.242354740061162, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34031, 9.125, 0.0, 10.1)
    ops.element('elasticBeamColumn', 34031, 4031, 34031, 99999, 88888)
    ops.node(24031, 9.0, 0.0, 9.925)
    ops.element('elasticBeamColumn', 24031, 24031, 4031, 99999, 99999)
    ops.node(74031, 9.0, 0.0, 10.275)
    ops.element('elasticBeamColumn', 74031, 4031, 74031, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 3.5)
    # Central joint node
    ops.node(4032, 12.0, 0.0, 10.1, '-mass', 3.242354740061162, 3.242354740061162, 3.242354740061162, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54032, 11.875, 0.0, 10.1)
    ops.element('elasticBeamColumn', 54032, 54032, 4032, 99999, 88888)
    ops.node(24032, 12.0, 0.0, 9.925)
    ops.element('elasticBeamColumn', 24032, 24032, 4032, 99999, 99999)
    ops.node(74032, 12.0, 0.0, 10.275)
    ops.element('elasticBeamColumn', 74032, 4032, 74032, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 3.1, '-mass', 9.521024464831806, 9.521024464831806, 9.521024464831806, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.125, 0.0, 3.1)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 2.875)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.325)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.125, 3.1)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301001, 10.62823277, 0.0002, 10.62823277, 0.0132, 6.61299729, 0.027, -10.62823277, -0.0002, -10.62823277, -0.0132, -6.61299729, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401001, 9.2438579, 0.0002, 9.2438579, 0.0132, 5.76273178, 0.027, -9.2438579, -0.0002, -9.2438579, -0.0132, -5.76273178, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401001, 'My', 301001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11001, 1001, 11001, 11001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 4.5, 0.0, 3.1, '-mass', 15.193730886850151, 15.193730886850151, 15.193730886850151, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 4.325, 0.0, 3.1)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 4.675, 0.0, 3.1)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 4.5, 0.0, 2.875)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 4.5, 0.0, 3.325)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 4.5, 0.175, 3.1)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301002, 18.84137356, 0.0002, 18.84137356, 0.0132, 11.76595754, 0.027, -18.84137356, -0.0002, -18.84137356, -0.0132, -11.76595754, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401002, 23.57418486, 0.0002, 28.41668281, 0.009, 28.41668281, 0.02, -23.57418486, -0.0002, -28.41668281, -0.009, -28.41668281, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401002, 'My', 301002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11002, 1002, 11002, 11002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 9.0, 0.0, 3.1, '-mass', 9.75711009174312, 9.75711009174312, 9.75711009174312, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 8.85, 0.0, 3.1)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 9.15, 0.0, 3.1)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 9.0, 0.0, 2.85)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 9.0, 0.0, 3.35)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 9.0, 0.15, 3.1)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301003, 19.95238515, 0.0002, 19.95238515, 0.0132, 12.42145282, 0.027, -19.95238515, -0.0002, -19.95238515, -0.0132, -12.42145282, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401003, 20.93555288, 0.0002, 25.23215818, 0.009, 25.23215818, 0.02, -20.93555288, -0.0002, -25.23215818, -0.009, -25.23215818, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401003, 'My', 301003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11003, 1003, 11003, 11003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 12.0, 0.0, 3.1, '-mass', 9.75711009174312, 9.75711009174312, 9.75711009174312, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 11.85, 0.0, 3.1)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(31004, 12.15, 0.0, 3.1)
    ops.element('elasticBeamColumn', 31004, 1004, 31004, 99999, 88888)
    ops.node(21004, 12.0, 0.0, 2.85)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 12.0, 0.0, 3.35)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 12.0, 0.15, 3.1)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301004, 19.95238515, 0.0002, 19.95238515, 0.0132, 12.42145282, 0.027, -19.95238515, -0.0002, -19.95238515, -0.0132, -12.42145282, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401004, 20.93555288, 0.0002, 25.23215818, 0.009, 25.23215818, 0.02, -20.93555288, -0.0002, -25.23215818, -0.009, -25.23215818, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401004, 'My', 301004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11004, 1004, 11004, 11004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 1)
    # Central joint node
    ops.node(1005, 16.5, 0.0, 3.1, '-mass', 15.193730886850151, 15.193730886850151, 15.193730886850151, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51005, 16.325, 0.0, 3.1)
    ops.element('elasticBeamColumn', 51005, 51005, 1005, 99999, 88888)
    ops.node(31005, 16.675, 0.0, 3.1)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 16.5, 0.0, 2.875)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 16.5, 0.0, 3.325)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(41005, 16.5, 0.175, 3.1)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301005, 18.84137356, 0.0002, 18.84137356, 0.0132, 11.76595754, 0.027, -18.84137356, -0.0002, -18.84137356, -0.0132, -11.76595754, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401005, 23.57418486, 0.0002, 28.41668281, 0.009, 28.41668281, 0.02, -23.57418486, -0.0002, -28.41668281, -0.009, -28.41668281, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401005, 'My', 301005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11005, 1005, 11005, 11005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 1)
    # Central joint node
    ops.node(1006, 21.0, 0.0, 3.1, '-mass', 9.521024464831806, 9.521024464831806, 9.521024464831806, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 20.875, 0.0, 3.1)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(21006, 21.0, 0.0, 2.875)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 21.0, 0.0, 3.325)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(41006, 21.0, 0.125, 3.1)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301006, 10.62823277, 0.0002, 10.62823277, 0.0132, 6.61299729, 0.027, -10.62823277, -0.0002, -10.62823277, -0.0132, -6.61299729, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401006, 9.2438579, 0.0002, 9.2438579, 0.0132, 5.76273178, 0.027, -9.2438579, -0.0002, -9.2438579, -0.0132, -5.76273178, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401006, 'My', 301006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11006, 1006, 11006, 11006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1007, 0.0, 4.5, 3.1, '-mass', 15.37262996941896, 15.37262996941896, 15.37262996941896, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31007, 0.175, 4.5, 3.1)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 0.0, 4.5, 2.875)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 0.0, 4.5, 3.325)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 0.0, 4.325, 3.1)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 0.0, 4.675, 3.1)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301007, 27.07617651, 0.0002, 32.63758799, 0.009, 32.63758799, 0.02, -27.07617651, -0.0002, -32.63758799, -0.009, -32.63758799, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401007, 16.47354517, 0.0002, 16.47354517, 0.0132, 10.30345244, 0.027, -16.47354517, -0.0002, -16.47354517, -0.0132, -10.30345244, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401007, 'My', 301007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11007, 1007, 11007, 11007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1008, 4.5, 4.5, 3.1, '-mass', 22.47125382262997, 22.47125382262997, 22.47125382262997, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 4.3, 4.5, 3.1)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(31008, 4.7, 4.5, 3.1)
    ops.element('elasticBeamColumn', 31008, 1008, 31008, 99999, 88888)
    ops.node(21008, 4.5, 4.5, 2.875)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 4.5, 4.5, 3.325)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 4.5, 4.3, 3.1)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 4.5, 4.7, 3.1)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301008, 35.93861655, 0.0002, 43.31813733, 0.009, 43.31813733, 0.02, -35.93861655, -0.0002, -43.31813733, -0.009, -43.31813733, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401008, 31.42290454, 0.0002, 37.87518344, 0.009, 37.87518344, 0.02, -31.42290454, -0.0002, -37.87518344, -0.009, -37.87518344, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401008, 'My', 301008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11008, 1008, 11008, 11008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1009, 9.0, 4.5, 3.1, '-mass', 20.260244648318043, 20.260244648318043, 20.260244648318043, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51009, 8.8, 4.5, 3.1)
    ops.element('elasticBeamColumn', 51009, 51009, 1009, 99999, 88888)
    ops.node(31009, 9.2, 4.5, 3.1)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 9.0, 4.5, 2.85)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 9.0, 4.5, 3.35)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 9.0, 4.3, 3.1)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 9.0, 4.7, 3.1)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301009, 38.21719456, 0.0002, 46.07391624, 0.009, 46.07391624, 0.02, -38.21719456, -0.0002, -46.07391624, -0.009, -46.07391624, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401009, 29.57356413, 0.0002, 35.65332129, 0.009, 35.65332129, 0.02, -29.57356413, -0.0002, -35.65332129, -0.009, -35.65332129, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401009, 'My', 301009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11009, 1009, 11009, 11009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1010, 12.0, 4.5, 3.1, '-mass', 20.260244648318043, 20.260244648318043, 20.260244648318043, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 11.8, 4.5, 3.1)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 12.2, 4.5, 3.1)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 12.0, 4.5, 2.85)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 12.0, 4.5, 3.35)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 12.0, 4.3, 3.1)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 12.0, 4.7, 3.1)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301010, 38.21719456, 0.0002, 46.07391624, 0.009, 46.07391624, 0.02, -38.21719456, -0.0002, -46.07391624, -0.009, -46.07391624, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401010, 29.57356413, 0.0002, 35.65332129, 0.009, 35.65332129, 0.02, -29.57356413, -0.0002, -35.65332129, -0.009, -35.65332129, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401010, 'My', 301010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11010, 1010, 11010, 11010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 1)
    # Central joint node
    ops.node(1011, 16.5, 4.5, 3.1, '-mass', 22.47125382262997, 22.47125382262997, 22.47125382262997, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 16.3, 4.5, 3.1)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 16.7, 4.5, 3.1)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 16.5, 4.5, 2.875)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 16.5, 4.5, 3.325)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 16.5, 4.3, 3.1)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 16.5, 4.7, 3.1)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301011, 35.93861655, 0.0002, 43.31813733, 0.009, 43.31813733, 0.02, -35.93861655, -0.0002, -43.31813733, -0.009, -43.31813733, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401011, 31.42290454, 0.0002, 37.87518344, 0.009, 37.87518344, 0.02, -31.42290454, -0.0002, -37.87518344, -0.009, -37.87518344, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401011, 'My', 301011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11011, 1011, 11011, 11011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 1)
    # Central joint node
    ops.node(1012, 21.0, 4.5, 3.1, '-mass', 15.37262996941896, 15.37262996941896, 15.37262996941896, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 20.825, 4.5, 3.1)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 21.0, 4.5, 2.875)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 21.0, 4.5, 3.325)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 21.0, 4.325, 3.1)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 21.0, 4.675, 3.1)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301012, 27.07617651, 0.0002, 32.63758799, 0.009, 32.63758799, 0.02, -27.07617651, -0.0002, -32.63758799, -0.009, -32.63758799, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401012, 16.47354517, 0.0002, 16.47354517, 0.0132, 10.30345244, 0.027, -16.47354517, -0.0002, -16.47354517, -0.0132, -10.30345244, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401012, 'My', 301012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11012, 1012, 11012, 11012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1013, 0.0, 9.0, 3.1, '-mass', 15.37262996941896, 15.37262996941896, 15.37262996941896, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.175, 9.0, 3.1)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 9.0, 2.875)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 9.0, 3.325)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 8.825, 3.1)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    ops.node(41013, 0.0, 9.175, 3.1)
    ops.element('elasticBeamColumn', 41013, 1013, 41013, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301013, 27.07617651, 0.0002, 32.63758799, 0.009, 32.63758799, 0.02, -27.07617651, -0.0002, -32.63758799, -0.009, -32.63758799, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401013, 16.47354517, 0.0002, 16.47354517, 0.0132, 10.30345244, 0.027, -16.47354517, -0.0002, -16.47354517, -0.0132, -10.30345244, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401013, 'My', 301013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11013, 1013, 11013, 11013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1014, 4.5, 9.0, 3.1, '-mass', 22.47125382262997, 22.47125382262997, 22.47125382262997, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 4.3, 9.0, 3.1)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 4.7, 9.0, 3.1)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 4.5, 9.0, 2.875)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 4.5, 9.0, 3.325)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 4.5, 8.8, 3.1)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    ops.node(41014, 4.5, 9.2, 3.1)
    ops.element('elasticBeamColumn', 41014, 1014, 41014, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301014, 35.93861655, 0.0002, 43.31813733, 0.009, 43.31813733, 0.02, -35.93861655, -0.0002, -43.31813733, -0.009, -43.31813733, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401014, 31.42290454, 0.0002, 37.87518344, 0.009, 37.87518344, 0.02, -31.42290454, -0.0002, -37.87518344, -0.009, -37.87518344, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401014, 'My', 301014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11014, 1014, 11014, 11014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1015, 9.0, 9.0, 3.1, '-mass', 19.97354740061162, 19.97354740061162, 19.97354740061162, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 8.8, 9.0, 3.1)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 9.2, 9.0, 3.1)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 9.0, 9.0, 2.85)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 9.0, 9.0, 3.35)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 9.0, 8.8, 3.1)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    ops.node(41015, 9.0, 9.2, 3.1)
    ops.element('elasticBeamColumn', 41015, 1015, 41015, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301015, 38.27171014, 0.0002, 46.13940649, 0.009, 46.13940649, 0.02, -38.27171014, -0.0002, -46.13940649, -0.009, -46.13940649, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401015, 29.61574985, 0.0002, 35.70399953, 0.009, 35.70399953, 0.02, -29.61574985, -0.0002, -35.70399953, -0.009, -35.70399953, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401015, 'My', 301015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11015, 1015, 11015, 11015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1016, 12.0, 9.0, 3.1, '-mass', 19.97354740061162, 19.97354740061162, 19.97354740061162, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 11.8, 9.0, 3.1)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(31016, 12.2, 9.0, 3.1)
    ops.element('elasticBeamColumn', 31016, 1016, 31016, 99999, 88888)
    ops.node(21016, 12.0, 9.0, 2.85)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 12.0, 9.0, 3.35)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 12.0, 8.8, 3.1)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    ops.node(41016, 12.0, 9.2, 3.1)
    ops.element('elasticBeamColumn', 41016, 1016, 41016, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301016, 38.27171014, 0.0002, 46.13940649, 0.009, 46.13940649, 0.02, -38.27171014, -0.0002, -46.13940649, -0.009, -46.13940649, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401016, 29.61574985, 0.0002, 35.70399953, 0.009, 35.70399953, 0.02, -29.61574985, -0.0002, -35.70399953, -0.009, -35.70399953, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401016, 'My', 301016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11016, 1016, 11016, 11016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 1)
    # Central joint node
    ops.node(1017, 16.5, 9.0, 3.1, '-mass', 22.47125382262997, 22.47125382262997, 22.47125382262997, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51017, 16.3, 9.0, 3.1)
    ops.element('elasticBeamColumn', 51017, 51017, 1017, 99999, 88888)
    ops.node(31017, 16.7, 9.0, 3.1)
    ops.element('elasticBeamColumn', 31017, 1017, 31017, 99999, 88888)
    ops.node(21017, 16.5, 9.0, 2.875)
    ops.element('elasticBeamColumn', 21017, 21017, 1017, 99999, 99999)
    ops.node(71017, 16.5, 9.0, 3.325)
    ops.element('elasticBeamColumn', 71017, 1017, 71017, 99999, 99999)
    ops.node(61017, 16.5, 8.8, 3.1)
    ops.element('elasticBeamColumn', 61017, 61017, 1017, 99999, 77777)
    ops.node(41017, 16.5, 9.2, 3.1)
    ops.element('elasticBeamColumn', 41017, 1017, 41017, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301017, 35.93861655, 0.0002, 43.31813733, 0.009, 43.31813733, 0.02, -35.93861655, -0.0002, -43.31813733, -0.009, -43.31813733, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401017, 31.42290454, 0.0002, 37.87518344, 0.009, 37.87518344, 0.02, -31.42290454, -0.0002, -37.87518344, -0.009, -37.87518344, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 11017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401017, 'My', 301017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11017, 1017, 11017, 11017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 1)
    # Central joint node
    ops.node(1018, 21.0, 9.0, 3.1, '-mass', 15.37262996941896, 15.37262996941896, 15.37262996941896, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51018, 20.825, 9.0, 3.1)
    ops.element('elasticBeamColumn', 51018, 51018, 1018, 99999, 88888)
    ops.node(21018, 21.0, 9.0, 2.875)
    ops.element('elasticBeamColumn', 21018, 21018, 1018, 99999, 99999)
    ops.node(71018, 21.0, 9.0, 3.325)
    ops.element('elasticBeamColumn', 71018, 1018, 71018, 99999, 99999)
    ops.node(61018, 21.0, 8.825, 3.1)
    ops.element('elasticBeamColumn', 61018, 61018, 1018, 99999, 77777)
    ops.node(41018, 21.0, 9.175, 3.1)
    ops.element('elasticBeamColumn', 41018, 1018, 41018, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301018, 27.07617651, 0.0002, 32.63758799, 0.009, 32.63758799, 0.02, -27.07617651, -0.0002, -32.63758799, -0.009, -32.63758799, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401018, 16.47354517, 0.0002, 16.47354517, 0.0132, 10.30345244, 0.027, -16.47354517, -0.0002, -16.47354517, -0.0132, -10.30345244, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401018, 'My', 301018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11018, 1018, 11018, 11018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    # Central joint node
    ops.node(1019, 0.0, 13.5, 3.1, '-mass', 9.521024464831806, 9.521024464831806, 9.521024464831806, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31019, 0.125, 13.5, 3.1)
    ops.element('elasticBeamColumn', 31019, 1019, 31019, 99999, 88888)
    ops.node(21019, 0.0, 13.5, 2.875)
    ops.element('elasticBeamColumn', 21019, 21019, 1019, 99999, 99999)
    ops.node(71019, 0.0, 13.5, 3.325)
    ops.element('elasticBeamColumn', 71019, 1019, 71019, 99999, 99999)
    ops.node(61019, 0.0, 13.375, 3.1)
    ops.element('elasticBeamColumn', 61019, 61019, 1019, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301019, 10.62823277, 0.0002, 10.62823277, 0.0132, 6.61299729, 0.027, -10.62823277, -0.0002, -10.62823277, -0.0132, -6.61299729, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401019, 9.2438579, 0.0002, 9.2438579, 0.0132, 5.76273178, 0.027, -9.2438579, -0.0002, -9.2438579, -0.0132, -5.76273178, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401019, 'My', 301019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11019, 1019, 11019, 11019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    # Central joint node
    ops.node(1020, 4.5, 13.5, 3.1, '-mass', 15.193730886850151, 15.193730886850151, 15.193730886850151, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51020, 4.325, 13.5, 3.1)
    ops.element('elasticBeamColumn', 51020, 51020, 1020, 99999, 88888)
    ops.node(31020, 4.675, 13.5, 3.1)
    ops.element('elasticBeamColumn', 31020, 1020, 31020, 99999, 88888)
    ops.node(21020, 4.5, 13.5, 2.875)
    ops.element('elasticBeamColumn', 21020, 21020, 1020, 99999, 99999)
    ops.node(71020, 4.5, 13.5, 3.325)
    ops.element('elasticBeamColumn', 71020, 1020, 71020, 99999, 99999)
    ops.node(61020, 4.5, 13.325, 3.1)
    ops.element('elasticBeamColumn', 61020, 61020, 1020, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301020, 18.84137356, 0.0002, 18.84137356, 0.0132, 11.76595754, 0.027, -18.84137356, -0.0002, -18.84137356, -0.0132, -11.76595754, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401020, 23.57418486, 0.0002, 28.41668281, 0.009, 28.41668281, 0.02, -23.57418486, -0.0002, -28.41668281, -0.009, -28.41668281, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401020, 'My', 301020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11020, 1020, 11020, 11020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    # Central joint node
    ops.node(1021, 9.0, 13.5, 3.1, '-mass', 13.101758409785932, 13.101758409785932, 13.101758409785932, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51021, 8.85, 13.5, 3.1)
    ops.element('elasticBeamColumn', 51021, 51021, 1021, 99999, 88888)
    ops.node(31021, 9.15, 13.5, 3.1)
    ops.element('elasticBeamColumn', 31021, 1021, 31021, 99999, 88888)
    ops.node(21021, 9.0, 13.5, 2.85)
    ops.element('elasticBeamColumn', 21021, 21021, 1021, 99999, 99999)
    ops.node(71021, 9.0, 13.5, 3.35)
    ops.element('elasticBeamColumn', 71021, 1021, 71021, 99999, 99999)
    ops.node(61021, 9.0, 13.35, 3.1)
    ops.element('elasticBeamColumn', 61021, 61021, 1021, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301021, 17.14503028, 0.0002, 17.14503028, 0.0132, 10.68054122, 0.027, -17.14503028, -0.0002, -17.14503028, -0.0132, -10.68054122, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401021, 18.84545514, 0.0002, 22.71083026, 0.009, 22.71083026, 0.02, -18.84545514, -0.0002, -22.71083026, -0.009, -22.71083026, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401021, 'My', 301021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11021, 1021, 11021, 11021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    # Central joint node
    ops.node(1022, 12.0, 13.5, 3.1, '-mass', 13.101758409785932, 13.101758409785932, 13.101758409785932, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51022, 11.85, 13.5, 3.1)
    ops.element('elasticBeamColumn', 51022, 51022, 1022, 99999, 88888)
    ops.node(31022, 12.15, 13.5, 3.1)
    ops.element('elasticBeamColumn', 31022, 1022, 31022, 99999, 88888)
    ops.node(21022, 12.0, 13.5, 2.85)
    ops.element('elasticBeamColumn', 21022, 21022, 1022, 99999, 99999)
    ops.node(71022, 12.0, 13.5, 3.35)
    ops.element('elasticBeamColumn', 71022, 1022, 71022, 99999, 99999)
    ops.node(61022, 12.0, 13.35, 3.1)
    ops.element('elasticBeamColumn', 61022, 61022, 1022, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301022, 17.14503028, 0.0002, 17.14503028, 0.0132, 10.68054122, 0.027, -17.14503028, -0.0002, -17.14503028, -0.0132, -10.68054122, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401022, 18.84545514, 0.0002, 22.71083026, 0.009, 22.71083026, 0.02, -18.84545514, -0.0002, -22.71083026, -0.009, -22.71083026, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401022, 'My', 301022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11022, 1022, 11022, 11022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 1)
    # Central joint node
    ops.node(1023, 16.5, 13.5, 3.1, '-mass', 15.193730886850151, 15.193730886850151, 15.193730886850151, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51023, 16.325, 13.5, 3.1)
    ops.element('elasticBeamColumn', 51023, 51023, 1023, 99999, 88888)
    ops.node(31023, 16.675, 13.5, 3.1)
    ops.element('elasticBeamColumn', 31023, 1023, 31023, 99999, 88888)
    ops.node(21023, 16.5, 13.5, 2.875)
    ops.element('elasticBeamColumn', 21023, 21023, 1023, 99999, 99999)
    ops.node(71023, 16.5, 13.5, 3.325)
    ops.element('elasticBeamColumn', 71023, 1023, 71023, 99999, 99999)
    ops.node(61023, 16.5, 13.325, 3.1)
    ops.element('elasticBeamColumn', 61023, 61023, 1023, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301023, 18.84137356, 0.0002, 18.84137356, 0.0132, 11.76595754, 0.027, -18.84137356, -0.0002, -18.84137356, -0.0132, -11.76595754, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401023, 23.57418486, 0.0002, 28.41668281, 0.009, 28.41668281, 0.02, -23.57418486, -0.0002, -28.41668281, -0.009, -28.41668281, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401023, 'My', 301023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11023, 1023, 11023, 11023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 1)
    # Central joint node
    ops.node(1024, 21.0, 13.5, 3.1, '-mass', 9.521024464831806, 9.521024464831806, 9.521024464831806, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51024, 20.875, 13.5, 3.1)
    ops.element('elasticBeamColumn', 51024, 51024, 1024, 99999, 88888)
    ops.node(21024, 21.0, 13.5, 2.875)
    ops.element('elasticBeamColumn', 21024, 21024, 1024, 99999, 99999)
    ops.node(71024, 21.0, 13.5, 3.325)
    ops.element('elasticBeamColumn', 71024, 1024, 71024, 99999, 99999)
    ops.node(61024, 21.0, 13.375, 3.1)
    ops.element('elasticBeamColumn', 61024, 61024, 1024, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 301024, 10.62823277, 0.0002, 10.62823277, 0.0132, 6.61299729, 0.027, -10.62823277, -0.0002, -10.62823277, -0.0132, -6.61299729, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 401024, 9.2438579, 0.0002, 9.2438579, 0.0132, 5.76273178, 0.027, -9.2438579, -0.0002, -9.2438579, -0.0132, -5.76273178, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 11024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401024, 'My', 301024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11024, 1024, 11024, 11024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 5.9, '-mass', 9.498088685015292, 9.498088685015292, 9.498088685015292, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.125, 0.0, 5.9)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 5.675)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 6.125)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.125, 5.9)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302001, 9.19646533, 0.0002, 9.19646533, 0.0132, 5.70415624, 0.027, -9.19646533, -0.0002, -9.19646533, -0.0132, -5.70415624, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402001, 7.99164768, 0.0002, 7.99164768, 0.0132, 4.96799892, 0.027, -7.99164768, -0.0002, -7.99164768, -0.0132, -4.96799892, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402001, 'My', 302001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12001, 2001, 12001, 12001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 4.5, 0.0, 5.9, '-mass', 14.943272171253824, 14.943272171253824, 14.943272171253824, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 4.325, 0.0, 5.9)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 4.675, 0.0, 5.9)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 4.5, 0.0, 5.675)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 4.5, 0.0, 6.125)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 4.5, 0.175, 5.9)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302002, 16.35083149, 0.0002, 16.35083149, 0.0132, 10.18523103, 0.027, -16.35083149, -0.0002, -16.35083149, -0.0132, -10.18523103, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402002, 20.35138468, 0.0002, 24.54557196, 0.009, 24.54557196, 0.02, -20.35138468, -0.0002, -24.54557196, -0.009, -24.54557196, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402002, 'My', 302002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12002, 2002, 12002, 12002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 9.0, 0.0, 5.9, '-mass', 9.69350152905199, 9.69350152905199, 9.69350152905199, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 8.85, 0.0, 5.9)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 9.15, 0.0, 5.9)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 9.0, 0.0, 5.65)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 9.0, 0.0, 6.15)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 9.0, 0.15, 5.9)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302003, 17.15911603, 0.0002, 17.15911603, 0.0132, 10.64830575, 0.027, -17.15911603, -0.0002, -17.15911603, -0.0132, -10.64830575, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402003, 17.87542453, 0.0002, 21.55585876, 0.009, 21.55585876, 0.02, -17.87542453, -0.0002, -21.55585876, -0.009, -21.55585876, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402003, 'My', 302003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12003, 2003, 12003, 12003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 12.0, 0.0, 5.9, '-mass', 9.69350152905199, 9.69350152905199, 9.69350152905199, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 11.85, 0.0, 5.9)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(32004, 12.15, 0.0, 5.9)
    ops.element('elasticBeamColumn', 32004, 2004, 32004, 99999, 88888)
    ops.node(22004, 12.0, 0.0, 5.65)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 12.0, 0.0, 6.15)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 12.0, 0.15, 5.9)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302004, 17.15911603, 0.0002, 17.15911603, 0.0132, 10.64830575, 0.027, -17.15911603, -0.0002, -17.15911603, -0.0132, -10.64830575, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402004, 17.87542453, 0.0002, 21.55585876, 0.009, 21.55585876, 0.02, -17.87542453, -0.0002, -21.55585876, -0.009, -21.55585876, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402004, 'My', 302004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12004, 2004, 12004, 12004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 2)
    # Central joint node
    ops.node(2005, 16.5, 0.0, 5.9, '-mass', 14.943272171253824, 14.943272171253824, 14.943272171253824, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52005, 16.325, 0.0, 5.9)
    ops.element('elasticBeamColumn', 52005, 52005, 2005, 99999, 88888)
    ops.node(32005, 16.675, 0.0, 5.9)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 16.5, 0.0, 5.675)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 16.5, 0.0, 6.125)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(42005, 16.5, 0.175, 5.9)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302005, 16.35083149, 0.0002, 16.35083149, 0.0132, 10.18523103, 0.027, -16.35083149, -0.0002, -16.35083149, -0.0132, -10.18523103, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402005, 20.35138468, 0.0002, 24.54557196, 0.009, 24.54557196, 0.02, -20.35138468, -0.0002, -24.54557196, -0.009, -24.54557196, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402005, 'My', 302005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12005, 2005, 12005, 12005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 2)
    # Central joint node
    ops.node(2006, 21.0, 0.0, 5.9, '-mass', 9.498088685015292, 9.498088685015292, 9.498088685015292, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 20.875, 0.0, 5.9)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(22006, 21.0, 0.0, 5.675)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 21.0, 0.0, 6.125)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(42006, 21.0, 0.125, 5.9)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302006, 9.19646533, 0.0002, 9.19646533, 0.0132, 5.70415624, 0.027, -9.19646533, -0.0002, -9.19646533, -0.0132, -5.70415624, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402006, 7.99164768, 0.0002, 7.99164768, 0.0132, 4.96799892, 0.027, -7.99164768, -0.0002, -7.99164768, -0.0132, -4.96799892, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402006, 'My', 302006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12006, 2006, 12006, 12006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2007, 0.0, 4.5, 5.9, '-mass', 15.122171253822629, 15.122171253822629, 15.122171253822629, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32007, 0.175, 4.5, 5.9)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 0.0, 4.5, 5.675)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 0.0, 4.5, 6.125)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 0.0, 4.325, 5.9)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 0.0, 4.675, 5.9)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302007, 23.36107979, 0.0002, 28.17508214, 0.009, 28.17508214, 0.02, -23.36107979, -0.0002, -28.17508214, -0.009, -28.17508214, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402007, 14.27837737, 0.0002, 14.27837737, 0.0132, 8.91035408, 0.027, -14.27837737, -0.0002, -14.27837737, -0.0132, -8.91035408, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402007, 'My', 302007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12007, 2007, 12007, 12007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2008, 4.5, 4.5, 5.9, '-mass', 22.28409785932722, 22.28409785932722, 22.28409785932722, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 4.3, 4.5, 5.9)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(32008, 4.7, 4.5, 5.9)
    ops.element('elasticBeamColumn', 32008, 2008, 32008, 99999, 88888)
    ops.node(22008, 4.5, 4.5, 5.675)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 4.5, 4.5, 6.125)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 4.5, 4.3, 5.9)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 4.5, 4.7, 5.9)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302008, 31.40379255, 0.0002, 37.87054118, 0.009, 37.87054118, 0.02, -31.40379255, -0.0002, -37.87054118, -0.009, -37.87054118, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402008, 27.45788432, 0.0002, 33.11208151, 0.009, 33.11208151, 0.02, -27.45788432, -0.0002, -33.11208151, -0.009, -33.11208151, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402008, 'My', 302008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12008, 2008, 12008, 12008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2009, 9.0, 4.5, 5.9, '-mass', 20.073088685015293, 20.073088685015293, 20.073088685015293, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52009, 8.8, 4.5, 5.9)
    ops.element('elasticBeamColumn', 52009, 52009, 2009, 99999, 88888)
    ops.node(32009, 9.2, 4.5, 5.9)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 9.0, 4.5, 5.65)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 9.0, 4.5, 6.15)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 9.0, 4.3, 5.9)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 9.0, 4.7, 5.9)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302009, 33.30352788, 0.0002, 40.17262292, 0.009, 40.17262292, 0.02, -33.30352788, -0.0002, -40.17262292, -0.009, -40.17262292, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402009, 25.77122755, 0.0002, 31.08673082, 0.009, 31.08673082, 0.02, -25.77122755, -0.0002, -31.08673082, -0.009, -31.08673082, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402009, 'My', 302009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12009, 2009, 12009, 12009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2010, 12.0, 4.5, 5.9, '-mass', 20.073088685015293, 20.073088685015293, 20.073088685015293, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 11.8, 4.5, 5.9)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 12.2, 4.5, 5.9)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 12.0, 4.5, 5.65)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 12.0, 4.5, 6.15)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 12.0, 4.3, 5.9)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 12.0, 4.7, 5.9)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302010, 33.30352788, 0.0002, 40.17262292, 0.009, 40.17262292, 0.02, -33.30352788, -0.0002, -40.17262292, -0.009, -40.17262292, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402010, 25.77122755, 0.0002, 31.08673082, 0.009, 31.08673082, 0.02, -25.77122755, -0.0002, -31.08673082, -0.009, -31.08673082, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402010, 'My', 302010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12010, 2010, 12010, 12010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 2)
    # Central joint node
    ops.node(2011, 16.5, 4.5, 5.9, '-mass', 22.28409785932722, 22.28409785932722, 22.28409785932722, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 16.3, 4.5, 5.9)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 16.7, 4.5, 5.9)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 16.5, 4.5, 5.675)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 16.5, 4.5, 6.125)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 16.5, 4.3, 5.9)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 16.5, 4.7, 5.9)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302011, 31.40379255, 0.0002, 37.87054118, 0.009, 37.87054118, 0.02, -31.40379255, -0.0002, -37.87054118, -0.009, -37.87054118, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402011, 27.45788432, 0.0002, 33.11208151, 0.009, 33.11208151, 0.02, -27.45788432, -0.0002, -33.11208151, -0.009, -33.11208151, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402011, 'My', 302011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12011, 2011, 12011, 12011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 2)
    # Central joint node
    ops.node(2012, 21.0, 4.5, 5.9, '-mass', 15.122171253822629, 15.122171253822629, 15.122171253822629, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 20.825, 4.5, 5.9)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 21.0, 4.5, 5.675)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 21.0, 4.5, 6.125)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 21.0, 4.325, 5.9)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 21.0, 4.675, 5.9)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302012, 23.36107979, 0.0002, 28.17508214, 0.009, 28.17508214, 0.02, -23.36107979, -0.0002, -28.17508214, -0.009, -28.17508214, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402012, 14.27837737, 0.0002, 14.27837737, 0.0132, 8.91035408, 0.027, -14.27837737, -0.0002, -14.27837737, -0.0132, -8.91035408, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402012, 'My', 302012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12012, 2012, 12012, 12012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2013, 0.0, 9.0, 5.9, '-mass', 15.122171253822629, 15.122171253822629, 15.122171253822629, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.175, 9.0, 5.9)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 9.0, 5.675)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 9.0, 6.125)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 8.825, 5.9)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    ops.node(42013, 0.0, 9.175, 5.9)
    ops.element('elasticBeamColumn', 42013, 2013, 42013, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302013, 23.36107979, 0.0002, 28.17508214, 0.009, 28.17508214, 0.02, -23.36107979, -0.0002, -28.17508214, -0.009, -28.17508214, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402013, 14.27837737, 0.0002, 14.27837737, 0.0132, 8.91035408, 0.027, -14.27837737, -0.0002, -14.27837737, -0.0132, -8.91035408, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402013, 'My', 302013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12013, 2013, 12013, 12013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2014, 4.5, 9.0, 5.9, '-mass', 22.28409785932722, 22.28409785932722, 22.28409785932722, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 4.3, 9.0, 5.9)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 4.7, 9.0, 5.9)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 4.5, 9.0, 5.675)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 4.5, 9.0, 6.125)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 4.5, 8.8, 5.9)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    ops.node(42014, 4.5, 9.2, 5.9)
    ops.element('elasticBeamColumn', 42014, 2014, 42014, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302014, 31.40379255, 0.0002, 37.87054118, 0.009, 37.87054118, 0.02, -31.40379255, -0.0002, -37.87054118, -0.009, -37.87054118, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402014, 27.45788432, 0.0002, 33.11208151, 0.009, 33.11208151, 0.02, -27.45788432, -0.0002, -33.11208151, -0.009, -33.11208151, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402014, 'My', 302014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12014, 2014, 12014, 12014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2015, 9.0, 9.0, 5.9, '-mass', 19.78639143730887, 19.78639143730887, 19.78639143730887, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 8.8, 9.0, 5.9)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 9.2, 9.0, 5.9)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 9.0, 9.0, 5.65)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 9.0, 9.0, 6.15)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 9.0, 8.8, 5.9)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    ops.node(42015, 9.0, 9.2, 5.9)
    ops.element('elasticBeamColumn', 42015, 2015, 42015, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302015, 33.44070095, 0.0002, 40.33731941, 0.009, 40.33731941, 0.02, -33.44070095, -0.0002, -40.33731941, -0.009, -40.33731941, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402015, 25.87737602, 0.0002, 31.2141777, 0.009, 31.2141777, 0.02, -25.87737602, -0.0002, -31.2141777, -0.009, -31.2141777, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402015, 'My', 302015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12015, 2015, 12015, 12015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2016, 12.0, 9.0, 5.9, '-mass', 19.78639143730887, 19.78639143730887, 19.78639143730887, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 11.8, 9.0, 5.9)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(32016, 12.2, 9.0, 5.9)
    ops.element('elasticBeamColumn', 32016, 2016, 32016, 99999, 88888)
    ops.node(22016, 12.0, 9.0, 5.65)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 12.0, 9.0, 6.15)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 12.0, 8.8, 5.9)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    ops.node(42016, 12.0, 9.2, 5.9)
    ops.element('elasticBeamColumn', 42016, 2016, 42016, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302016, 33.44070095, 0.0002, 40.33731941, 0.009, 40.33731941, 0.02, -33.44070095, -0.0002, -40.33731941, -0.009, -40.33731941, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402016, 25.87737602, 0.0002, 31.2141777, 0.009, 31.2141777, 0.02, -25.87737602, -0.0002, -31.2141777, -0.009, -31.2141777, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402016, 'My', 302016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12016, 2016, 12016, 12016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 2)
    # Central joint node
    ops.node(2017, 16.5, 9.0, 5.9, '-mass', 22.28409785932722, 22.28409785932722, 22.28409785932722, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52017, 16.3, 9.0, 5.9)
    ops.element('elasticBeamColumn', 52017, 52017, 2017, 99999, 88888)
    ops.node(32017, 16.7, 9.0, 5.9)
    ops.element('elasticBeamColumn', 32017, 2017, 32017, 99999, 88888)
    ops.node(22017, 16.5, 9.0, 5.675)
    ops.element('elasticBeamColumn', 22017, 22017, 2017, 99999, 99999)
    ops.node(72017, 16.5, 9.0, 6.125)
    ops.element('elasticBeamColumn', 72017, 2017, 72017, 99999, 99999)
    ops.node(62017, 16.5, 8.8, 5.9)
    ops.element('elasticBeamColumn', 62017, 62017, 2017, 99999, 77777)
    ops.node(42017, 16.5, 9.2, 5.9)
    ops.element('elasticBeamColumn', 42017, 2017, 42017, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302017, 31.40379255, 0.0002, 37.87054118, 0.009, 37.87054118, 0.02, -31.40379255, -0.0002, -37.87054118, -0.009, -37.87054118, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402017, 27.45788432, 0.0002, 33.11208151, 0.009, 33.11208151, 0.02, -27.45788432, -0.0002, -33.11208151, -0.009, -33.11208151, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 12017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402017, 'My', 302017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12017, 2017, 12017, 12017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 2)
    # Central joint node
    ops.node(2018, 21.0, 9.0, 5.9, '-mass', 15.122171253822629, 15.122171253822629, 15.122171253822629, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52018, 20.825, 9.0, 5.9)
    ops.element('elasticBeamColumn', 52018, 52018, 2018, 99999, 88888)
    ops.node(22018, 21.0, 9.0, 5.675)
    ops.element('elasticBeamColumn', 22018, 22018, 2018, 99999, 99999)
    ops.node(72018, 21.0, 9.0, 6.125)
    ops.element('elasticBeamColumn', 72018, 2018, 72018, 99999, 99999)
    ops.node(62018, 21.0, 8.825, 5.9)
    ops.element('elasticBeamColumn', 62018, 62018, 2018, 99999, 77777)
    ops.node(42018, 21.0, 9.175, 5.9)
    ops.element('elasticBeamColumn', 42018, 2018, 42018, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302018, 23.36107979, 0.0002, 28.17508214, 0.009, 28.17508214, 0.02, -23.36107979, -0.0002, -28.17508214, -0.009, -28.17508214, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402018, 14.27837737, 0.0002, 14.27837737, 0.0132, 8.91035408, 0.027, -14.27837737, -0.0002, -14.27837737, -0.0132, -8.91035408, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402018, 'My', 302018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12018, 2018, 12018, 12018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    # Central joint node
    ops.node(2019, 0.0, 13.5, 5.9, '-mass', 9.498088685015292, 9.498088685015292, 9.498088685015292, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32019, 0.125, 13.5, 5.9)
    ops.element('elasticBeamColumn', 32019, 2019, 32019, 99999, 88888)
    ops.node(22019, 0.0, 13.5, 5.675)
    ops.element('elasticBeamColumn', 22019, 22019, 2019, 99999, 99999)
    ops.node(72019, 0.0, 13.5, 6.125)
    ops.element('elasticBeamColumn', 72019, 2019, 72019, 99999, 99999)
    ops.node(62019, 0.0, 13.375, 5.9)
    ops.element('elasticBeamColumn', 62019, 62019, 2019, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302019, 9.19646533, 0.0002, 9.19646533, 0.0132, 5.70415624, 0.027, -9.19646533, -0.0002, -9.19646533, -0.0132, -5.70415624, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402019, 7.99164768, 0.0002, 7.99164768, 0.0132, 4.96799892, 0.027, -7.99164768, -0.0002, -7.99164768, -0.0132, -4.96799892, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402019, 'My', 302019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12019, 2019, 12019, 12019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    # Central joint node
    ops.node(2020, 4.5, 13.5, 5.9, '-mass', 14.943272171253824, 14.943272171253824, 14.943272171253824, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52020, 4.325, 13.5, 5.9)
    ops.element('elasticBeamColumn', 52020, 52020, 2020, 99999, 88888)
    ops.node(32020, 4.675, 13.5, 5.9)
    ops.element('elasticBeamColumn', 32020, 2020, 32020, 99999, 88888)
    ops.node(22020, 4.5, 13.5, 5.675)
    ops.element('elasticBeamColumn', 22020, 22020, 2020, 99999, 99999)
    ops.node(72020, 4.5, 13.5, 6.125)
    ops.element('elasticBeamColumn', 72020, 2020, 72020, 99999, 99999)
    ops.node(62020, 4.5, 13.325, 5.9)
    ops.element('elasticBeamColumn', 62020, 62020, 2020, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302020, 16.35083149, 0.0002, 16.35083149, 0.0132, 10.18523103, 0.027, -16.35083149, -0.0002, -16.35083149, -0.0132, -10.18523103, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402020, 20.35138468, 0.0002, 24.54557196, 0.009, 24.54557196, 0.02, -20.35138468, -0.0002, -24.54557196, -0.009, -24.54557196, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402020, 'My', 302020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12020, 2020, 12020, 12020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    # Central joint node
    ops.node(2021, 9.0, 13.5, 5.9, '-mass', 12.974541284403669, 12.974541284403669, 12.974541284403669, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52021, 8.85, 13.5, 5.9)
    ops.element('elasticBeamColumn', 52021, 52021, 2021, 99999, 88888)
    ops.node(32021, 9.15, 13.5, 5.9)
    ops.element('elasticBeamColumn', 32021, 2021, 32021, 99999, 88888)
    ops.node(22021, 9.0, 13.5, 5.65)
    ops.element('elasticBeamColumn', 22021, 22021, 2021, 99999, 99999)
    ops.node(72021, 9.0, 13.5, 6.15)
    ops.element('elasticBeamColumn', 72021, 2021, 72021, 99999, 99999)
    ops.node(62021, 9.0, 13.35, 5.9)
    ops.element('elasticBeamColumn', 62021, 62021, 2021, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302021, 14.91393638, 0.0002, 14.91393638, 0.0132, 9.26446094, 0.027, -14.91393638, -0.0002, -14.91393638, -0.0132, -9.26446094, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402021, 16.28852234, 0.0002, 19.638626, 0.009, 19.638626, 0.02, -16.28852234, -0.0002, -19.638626, -0.009, -19.638626, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402021, 'My', 302021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12021, 2021, 12021, 12021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    # Central joint node
    ops.node(2022, 12.0, 13.5, 5.9, '-mass', 12.974541284403669, 12.974541284403669, 12.974541284403669, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52022, 11.85, 13.5, 5.9)
    ops.element('elasticBeamColumn', 52022, 52022, 2022, 99999, 88888)
    ops.node(32022, 12.15, 13.5, 5.9)
    ops.element('elasticBeamColumn', 32022, 2022, 32022, 99999, 88888)
    ops.node(22022, 12.0, 13.5, 5.65)
    ops.element('elasticBeamColumn', 22022, 22022, 2022, 99999, 99999)
    ops.node(72022, 12.0, 13.5, 6.15)
    ops.element('elasticBeamColumn', 72022, 2022, 72022, 99999, 99999)
    ops.node(62022, 12.0, 13.35, 5.9)
    ops.element('elasticBeamColumn', 62022, 62022, 2022, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302022, 14.91393638, 0.0002, 14.91393638, 0.0132, 9.26446094, 0.027, -14.91393638, -0.0002, -14.91393638, -0.0132, -9.26446094, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402022, 16.28852234, 0.0002, 19.638626, 0.009, 19.638626, 0.02, -16.28852234, -0.0002, -19.638626, -0.009, -19.638626, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402022, 'My', 302022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12022, 2022, 12022, 12022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 2)
    # Central joint node
    ops.node(2023, 16.5, 13.5, 5.9, '-mass', 14.943272171253824, 14.943272171253824, 14.943272171253824, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52023, 16.325, 13.5, 5.9)
    ops.element('elasticBeamColumn', 52023, 52023, 2023, 99999, 88888)
    ops.node(32023, 16.675, 13.5, 5.9)
    ops.element('elasticBeamColumn', 32023, 2023, 32023, 99999, 88888)
    ops.node(22023, 16.5, 13.5, 5.675)
    ops.element('elasticBeamColumn', 22023, 22023, 2023, 99999, 99999)
    ops.node(72023, 16.5, 13.5, 6.125)
    ops.element('elasticBeamColumn', 72023, 2023, 72023, 99999, 99999)
    ops.node(62023, 16.5, 13.325, 5.9)
    ops.element('elasticBeamColumn', 62023, 62023, 2023, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302023, 16.35083149, 0.0002, 16.35083149, 0.0132, 10.18523103, 0.027, -16.35083149, -0.0002, -16.35083149, -0.0132, -10.18523103, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402023, 20.35138468, 0.0002, 24.54557196, 0.009, 24.54557196, 0.02, -20.35138468, -0.0002, -24.54557196, -0.009, -24.54557196, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402023, 'My', 302023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12023, 2023, 12023, 12023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 2)
    # Central joint node
    ops.node(2024, 21.0, 13.5, 5.9, '-mass', 9.498088685015292, 9.498088685015292, 9.498088685015292, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52024, 20.875, 13.5, 5.9)
    ops.element('elasticBeamColumn', 52024, 52024, 2024, 99999, 88888)
    ops.node(22024, 21.0, 13.5, 5.675)
    ops.element('elasticBeamColumn', 22024, 22024, 2024, 99999, 99999)
    ops.node(72024, 21.0, 13.5, 6.125)
    ops.element('elasticBeamColumn', 72024, 2024, 72024, 99999, 99999)
    ops.node(62024, 21.0, 13.375, 5.9)
    ops.element('elasticBeamColumn', 62024, 62024, 2024, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 302024, 9.19646533, 0.0002, 9.19646533, 0.0132, 5.70415624, 0.027, -9.19646533, -0.0002, -9.19646533, -0.0132, -5.70415624, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 402024, 7.99164768, 0.0002, 7.99164768, 0.0132, 4.96799892, 0.027, -7.99164768, -0.0002, -7.99164768, -0.0132, -4.96799892, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 12024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402024, 'My', 302024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12024, 2024, 12024, 12024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 8.7, '-mass', 9.498088685015292, 9.498088685015292, 9.498088685015292, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 8.7)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 8.475)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 8.925)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 8.7)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303001, 7.4847677, 0.0002, 7.4847677, 0.0132, 4.61676307, 0.027, -7.4847677, -0.0002, -7.4847677, -0.0132, -4.61676307, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403001, 6.4944277, 0.0002, 6.4944277, 0.0132, 4.01708409, 0.027, -6.4944277, -0.0002, -6.4944277, -0.0132, -4.01708409, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403001, 'My', 303001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13001, 3001, 13001, 13001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 4.5, 0.0, 8.7, '-mass', 14.73776758409786, 14.73776758409786, 14.73776758409786, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 4.375, 0.0, 8.7)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 4.625, 0.0, 8.7)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 4.5, 0.0, 8.475)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 4.5, 0.0, 8.925)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 4.5, 0.125, 8.7)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303002, 9.55370277, 0.0002, 9.55370277, 0.0132, 5.93096673, 0.027, -9.55370277, -0.0002, -9.55370277, -0.0132, -5.93096673, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403002, 11.76460415, 0.0002, 14.1822818, 0.009, 14.1822818, 0.02, -11.76460415, -0.0002, -14.1822818, -0.009, -14.1822818, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403002, 'My', 303002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13002, 3002, 13002, 13002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 9.0, 0.0, 8.7, '-mass', 9.646406727828747, 9.646406727828747, 9.646406727828747, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 8.875, 0.0, 8.7)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 9.125, 0.0, 8.7)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 9.0, 0.0, 8.45)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 9.0, 0.0, 8.95)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 9.0, 0.125, 8.7)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303003, 11.37688993, 0.0002, 11.37688993, 0.0132, 7.02100529, 0.027, -11.37688993, -0.0002, -11.37688993, -0.0132, -7.02100529, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403003, 11.68165274, 0.0002, 14.09052381, 0.009, 14.09052381, 0.02, -11.68165274, -0.0002, -14.09052381, -0.009, -14.09052381, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403003, 'My', 303003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13003, 3003, 13003, 13003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 12.0, 0.0, 8.7, '-mass', 9.646406727828747, 9.646406727828747, 9.646406727828747, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 11.875, 0.0, 8.7)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(33004, 12.125, 0.0, 8.7)
    ops.element('elasticBeamColumn', 33004, 3004, 33004, 99999, 88888)
    ops.node(23004, 12.0, 0.0, 8.45)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 12.0, 0.0, 8.95)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 12.0, 0.125, 8.7)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303004, 11.37688993, 0.0002, 11.37688993, 0.0132, 7.02100529, 0.027, -11.37688993, -0.0002, -11.37688993, -0.0132, -7.02100529, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403004, 11.68165274, 0.0002, 14.09052381, 0.009, 14.09052381, 0.02, -11.68165274, -0.0002, -14.09052381, -0.009, -14.09052381, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403004, 'My', 303004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13004, 3004, 13004, 13004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 3)
    # Central joint node
    ops.node(3005, 16.5, 0.0, 8.7, '-mass', 14.73776758409786, 14.73776758409786, 14.73776758409786, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53005, 16.375, 0.0, 8.7)
    ops.element('elasticBeamColumn', 53005, 53005, 3005, 99999, 88888)
    ops.node(33005, 16.625, 0.0, 8.7)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 16.5, 0.0, 8.475)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 16.5, 0.0, 8.925)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(43005, 16.5, 0.125, 8.7)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303005, 9.55370277, 0.0002, 9.55370277, 0.0132, 5.93096673, 0.027, -9.55370277, -0.0002, -9.55370277, -0.0132, -5.93096673, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403005, 11.76460415, 0.0002, 14.1822818, 0.009, 14.1822818, 0.02, -11.76460415, -0.0002, -14.1822818, -0.009, -14.1822818, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403005, 'My', 303005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13005, 3005, 13005, 13005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 3)
    # Central joint node
    ops.node(3006, 21.0, 0.0, 8.7, '-mass', 9.498088685015292, 9.498088685015292, 9.498088685015292, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 20.875, 0.0, 8.7)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(23006, 21.0, 0.0, 8.475)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 21.0, 0.0, 8.925)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(43006, 21.0, 0.125, 8.7)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303006, 7.4847677, 0.0002, 7.4847677, 0.0132, 4.61676307, 0.027, -7.4847677, -0.0002, -7.4847677, -0.0132, -4.61676307, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403006, 6.4944277, 0.0002, 6.4944277, 0.0132, 4.01708409, 0.027, -6.4944277, -0.0002, -6.4944277, -0.0132, -4.01708409, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403006, 'My', 303006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13006, 3006, 13006, 13006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3007, 0.0, 4.5, 8.7, '-mass', 14.916666666666668, 14.916666666666668, 14.916666666666668, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33007, 0.125, 4.5, 8.7)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 0.0, 4.5, 8.475)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 0.0, 4.5, 8.925)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 0.0, 4.375, 8.7)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 0.0, 4.625, 8.7)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303007, 13.48862016, 0.0002, 16.26045345, 0.009, 16.26045345, 0.02, -13.48862016, -0.0002, -16.26045345, -0.009, -16.26045345, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403007, 8.32378769, 0.0002, 8.32378769, 0.0132, 5.17883525, 0.027, -8.32378769, -0.0002, -8.32378769, -0.0132, -5.17883525, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403007, 'My', 303007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13007, 3007, 13007, 13007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3008, 4.5, 4.5, 8.7, '-mass', 22.155657492354734, 22.155657492354734, 22.155657492354734, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 4.325, 4.5, 8.7)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(33008, 4.675, 4.5, 8.7)
    ops.element('elasticBeamColumn', 33008, 3008, 33008, 99999, 88888)
    ops.node(23008, 4.5, 4.5, 8.475)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 4.5, 4.5, 8.925)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 4.5, 4.325, 8.7)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 4.5, 4.675, 8.7)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303008, 22.81955265, 0.0002, 27.52483743, 0.009, 27.52483743, 0.02, -22.81955265, -0.0002, -27.52483743, -0.009, -27.52483743, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403008, 19.95226009, 0.0002, 24.06632259, 0.009, 24.06632259, 0.02, -19.95226009, -0.0002, -24.06632259, -0.009, -24.06632259, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403008, 'My', 303008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13008, 3008, 13008, 13008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3009, 9.0, 4.5, 8.7, '-mass', 19.944648318042812, 19.944648318042812, 19.944648318042812, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53009, 8.825, 4.5, 8.7)
    ops.element('elasticBeamColumn', 53009, 53009, 3009, 99999, 88888)
    ops.node(33009, 9.175, 4.5, 8.7)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 9.0, 4.5, 8.45)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 9.0, 4.5, 8.95)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 9.0, 4.325, 8.7)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 9.0, 4.675, 8.7)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303009, 24.0718438, 0.0002, 29.04509007, 0.009, 29.04509007, 0.02, -24.0718438, -0.0002, -29.04509007, -0.009, -29.04509007, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403009, 18.62748494, 0.0002, 22.47592592, 0.009, 22.47592592, 0.02, -18.62748494, -0.0002, -22.47592592, -0.009, -22.47592592, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403009, 'My', 303009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13009, 3009, 13009, 13009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3010, 12.0, 4.5, 8.7, '-mass', 19.944648318042812, 19.944648318042812, 19.944648318042812, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 11.825, 4.5, 8.7)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 12.175, 4.5, 8.7)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 12.0, 4.5, 8.45)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 12.0, 4.5, 8.95)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 12.0, 4.325, 8.7)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 12.0, 4.675, 8.7)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303010, 24.0718438, 0.0002, 29.04509007, 0.009, 29.04509007, 0.02, -24.0718438, -0.0002, -29.04509007, -0.009, -29.04509007, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403010, 18.62748494, 0.0002, 22.47592592, 0.009, 22.47592592, 0.02, -18.62748494, -0.0002, -22.47592592, -0.009, -22.47592592, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403010, 'My', 303010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13010, 3010, 13010, 13010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 3)
    # Central joint node
    ops.node(3011, 16.5, 4.5, 8.7, '-mass', 22.155657492354734, 22.155657492354734, 22.155657492354734, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 16.325, 4.5, 8.7)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 16.675, 4.5, 8.7)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 16.5, 4.5, 8.475)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 16.5, 4.5, 8.925)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 16.5, 4.325, 8.7)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 16.5, 4.675, 8.7)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303011, 22.81955265, 0.0002, 27.52483743, 0.009, 27.52483743, 0.02, -22.81955265, -0.0002, -27.52483743, -0.009, -27.52483743, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403011, 19.95226009, 0.0002, 24.06632259, 0.009, 24.06632259, 0.02, -19.95226009, -0.0002, -24.06632259, -0.009, -24.06632259, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403011, 'My', 303011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13011, 3011, 13011, 13011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 3)
    # Central joint node
    ops.node(3012, 21.0, 4.5, 8.7, '-mass', 14.916666666666668, 14.916666666666668, 14.916666666666668, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 20.875, 4.5, 8.7)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 21.0, 4.5, 8.475)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 21.0, 4.5, 8.925)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 21.0, 4.375, 8.7)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 21.0, 4.625, 8.7)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303012, 13.48862016, 0.0002, 16.26045345, 0.009, 16.26045345, 0.02, -13.48862016, -0.0002, -16.26045345, -0.009, -16.26045345, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403012, 8.32378769, 0.0002, 8.32378769, 0.0132, 5.17883525, 0.027, -8.32378769, -0.0002, -8.32378769, -0.0132, -5.17883525, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403012, 'My', 303012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13012, 3012, 13012, 13012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3013, 0.0, 9.0, 8.7, '-mass', 14.916666666666668, 14.916666666666668, 14.916666666666668, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.125, 9.0, 8.7)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 9.0, 8.475)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 9.0, 8.925)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 8.875, 8.7)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    ops.node(43013, 0.0, 9.125, 8.7)
    ops.element('elasticBeamColumn', 43013, 3013, 43013, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303013, 13.48862016, 0.0002, 16.26045345, 0.009, 16.26045345, 0.02, -13.48862016, -0.0002, -16.26045345, -0.009, -16.26045345, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403013, 8.32378769, 0.0002, 8.32378769, 0.0132, 5.17883525, 0.027, -8.32378769, -0.0002, -8.32378769, -0.0132, -5.17883525, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403013, 'My', 303013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13013, 3013, 13013, 13013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3014, 4.5, 9.0, 8.7, '-mass', 22.155657492354734, 22.155657492354734, 22.155657492354734, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 4.325, 9.0, 8.7)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 4.675, 9.0, 8.7)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 4.5, 9.0, 8.475)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 4.5, 9.0, 8.925)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 4.5, 8.825, 8.7)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    ops.node(43014, 4.5, 9.175, 8.7)
    ops.element('elasticBeamColumn', 43014, 3014, 43014, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303014, 22.81955265, 0.0002, 27.52483743, 0.009, 27.52483743, 0.02, -22.81955265, -0.0002, -27.52483743, -0.009, -27.52483743, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403014, 19.95226009, 0.0002, 24.06632259, 0.009, 24.06632259, 0.02, -19.95226009, -0.0002, -24.06632259, -0.009, -24.06632259, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403014, 'My', 303014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13014, 3014, 13014, 13014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3015, 9.0, 9.0, 8.7, '-mass', 19.657951070336388, 19.657951070336388, 19.657951070336388, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 8.825, 9.0, 8.7)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 9.175, 9.0, 8.7)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 9.0, 9.0, 8.45)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 9.0, 9.0, 8.95)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 9.0, 8.825, 8.7)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    ops.node(43015, 9.0, 9.175, 8.7)
    ops.element('elasticBeamColumn', 43015, 3015, 43015, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303015, 24.29568909, 0.0002, 29.31377688, 0.009, 29.31377688, 0.02, -24.29568909, -0.0002, -29.31377688, -0.009, -29.31377688, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403015, 18.80070287, 0.0002, 22.6838435, 0.009, 22.6838435, 0.02, -18.80070287, -0.0002, -22.6838435, -0.009, -22.6838435, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403015, 'My', 303015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13015, 3015, 13015, 13015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3016, 12.0, 9.0, 8.7, '-mass', 19.657951070336388, 19.657951070336388, 19.657951070336388, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 11.825, 9.0, 8.7)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(33016, 12.175, 9.0, 8.7)
    ops.element('elasticBeamColumn', 33016, 3016, 33016, 99999, 88888)
    ops.node(23016, 12.0, 9.0, 8.45)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 12.0, 9.0, 8.95)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 12.0, 8.825, 8.7)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    ops.node(43016, 12.0, 9.175, 8.7)
    ops.element('elasticBeamColumn', 43016, 3016, 43016, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303016, 24.29568909, 0.0002, 29.31377688, 0.009, 29.31377688, 0.02, -24.29568909, -0.0002, -29.31377688, -0.009, -29.31377688, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403016, 18.80070287, 0.0002, 22.6838435, 0.009, 22.6838435, 0.02, -18.80070287, -0.0002, -22.6838435, -0.009, -22.6838435, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403016, 'My', 303016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13016, 3016, 13016, 13016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 3)
    # Central joint node
    ops.node(3017, 16.5, 9.0, 8.7, '-mass', 22.155657492354734, 22.155657492354734, 22.155657492354734, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53017, 16.325, 9.0, 8.7)
    ops.element('elasticBeamColumn', 53017, 53017, 3017, 99999, 88888)
    ops.node(33017, 16.675, 9.0, 8.7)
    ops.element('elasticBeamColumn', 33017, 3017, 33017, 99999, 88888)
    ops.node(23017, 16.5, 9.0, 8.475)
    ops.element('elasticBeamColumn', 23017, 23017, 3017, 99999, 99999)
    ops.node(73017, 16.5, 9.0, 8.925)
    ops.element('elasticBeamColumn', 73017, 3017, 73017, 99999, 99999)
    ops.node(63017, 16.5, 8.825, 8.7)
    ops.element('elasticBeamColumn', 63017, 63017, 3017, 99999, 77777)
    ops.node(43017, 16.5, 9.175, 8.7)
    ops.element('elasticBeamColumn', 43017, 3017, 43017, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303017, 22.81955265, 0.0002, 27.52483743, 0.009, 27.52483743, 0.02, -22.81955265, -0.0002, -27.52483743, -0.009, -27.52483743, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403017, 19.95226009, 0.0002, 24.06632259, 0.009, 24.06632259, 0.02, -19.95226009, -0.0002, -24.06632259, -0.009, -24.06632259, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.section('Aggregator', 13017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403017, 'My', 303017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13017, 3017, 13017, 13017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 3)
    # Central joint node
    ops.node(3018, 21.0, 9.0, 8.7, '-mass', 14.916666666666668, 14.916666666666668, 14.916666666666668, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53018, 20.875, 9.0, 8.7)
    ops.element('elasticBeamColumn', 53018, 53018, 3018, 99999, 88888)
    ops.node(23018, 21.0, 9.0, 8.475)
    ops.element('elasticBeamColumn', 23018, 23018, 3018, 99999, 99999)
    ops.node(73018, 21.0, 9.0, 8.925)
    ops.element('elasticBeamColumn', 73018, 3018, 73018, 99999, 99999)
    ops.node(63018, 21.0, 8.875, 8.7)
    ops.element('elasticBeamColumn', 63018, 63018, 3018, 99999, 77777)
    ops.node(43018, 21.0, 9.125, 8.7)
    ops.element('elasticBeamColumn', 43018, 3018, 43018, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303018, 13.48862016, 0.0002, 16.26045345, 0.009, 16.26045345, 0.02, -13.48862016, -0.0002, -16.26045345, -0.009, -16.26045345, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403018, 8.32378769, 0.0002, 8.32378769, 0.0132, 5.17883525, 0.027, -8.32378769, -0.0002, -8.32378769, -0.0132, -5.17883525, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403018, 'My', 303018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13018, 3018, 13018, 13018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    # Central joint node
    ops.node(3019, 0.0, 13.5, 8.7, '-mass', 9.498088685015292, 9.498088685015292, 9.498088685015292, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33019, 0.125, 13.5, 8.7)
    ops.element('elasticBeamColumn', 33019, 3019, 33019, 99999, 88888)
    ops.node(23019, 0.0, 13.5, 8.475)
    ops.element('elasticBeamColumn', 23019, 23019, 3019, 99999, 99999)
    ops.node(73019, 0.0, 13.5, 8.925)
    ops.element('elasticBeamColumn', 73019, 3019, 73019, 99999, 99999)
    ops.node(63019, 0.0, 13.375, 8.7)
    ops.element('elasticBeamColumn', 63019, 63019, 3019, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303019, 7.4847677, 0.0002, 7.4847677, 0.0132, 4.61676307, 0.027, -7.4847677, -0.0002, -7.4847677, -0.0132, -4.61676307, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403019, 6.4944277, 0.0002, 6.4944277, 0.0132, 4.01708409, 0.027, -6.4944277, -0.0002, -6.4944277, -0.0132, -4.01708409, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403019, 'My', 303019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13019, 3019, 13019, 13019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    # Central joint node
    ops.node(3020, 4.5, 13.5, 8.7, '-mass', 14.73776758409786, 14.73776758409786, 14.73776758409786, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53020, 4.375, 13.5, 8.7)
    ops.element('elasticBeamColumn', 53020, 53020, 3020, 99999, 88888)
    ops.node(33020, 4.625, 13.5, 8.7)
    ops.element('elasticBeamColumn', 33020, 3020, 33020, 99999, 88888)
    ops.node(23020, 4.5, 13.5, 8.475)
    ops.element('elasticBeamColumn', 23020, 23020, 3020, 99999, 99999)
    ops.node(73020, 4.5, 13.5, 8.925)
    ops.element('elasticBeamColumn', 73020, 3020, 73020, 99999, 99999)
    ops.node(63020, 4.5, 13.375, 8.7)
    ops.element('elasticBeamColumn', 63020, 63020, 3020, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303020, 9.55370277, 0.0002, 9.55370277, 0.0132, 5.93096673, 0.027, -9.55370277, -0.0002, -9.55370277, -0.0132, -5.93096673, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403020, 11.76460415, 0.0002, 14.1822818, 0.009, 14.1822818, 0.02, -11.76460415, -0.0002, -14.1822818, -0.009, -14.1822818, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403020, 'My', 303020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13020, 3020, 13020, 13020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    # Central joint node
    ops.node(3021, 9.0, 13.5, 8.7, '-mass', 12.880351681957187, 12.880351681957187, 12.880351681957187, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53021, 8.875, 13.5, 8.7)
    ops.element('elasticBeamColumn', 53021, 53021, 3021, 99999, 88888)
    ops.node(33021, 9.125, 13.5, 8.7)
    ops.element('elasticBeamColumn', 33021, 3021, 33021, 99999, 88888)
    ops.node(23021, 9.0, 13.5, 8.45)
    ops.element('elasticBeamColumn', 23021, 23021, 3021, 99999, 99999)
    ops.node(73021, 9.0, 13.5, 8.95)
    ops.element('elasticBeamColumn', 73021, 3021, 73021, 99999, 99999)
    ops.node(63021, 9.0, 13.375, 8.7)
    ops.element('elasticBeamColumn', 63021, 63021, 3021, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303021, 10.21711986, 0.0002, 10.21711986, 0.0132, 6.31915594, 0.027, -10.21711986, -0.0002, -10.21711986, -0.0132, -6.31915594, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403021, 11.02906033, 0.0002, 13.29871053, 0.009, 13.29871053, 0.02, -11.02906033, -0.0002, -13.29871053, -0.009, -13.29871053, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403021, 'My', 303021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13021, 3021, 13021, 13021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    # Central joint node
    ops.node(3022, 12.0, 13.5, 8.7, '-mass', 12.880351681957187, 12.880351681957187, 12.880351681957187, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53022, 11.875, 13.5, 8.7)
    ops.element('elasticBeamColumn', 53022, 53022, 3022, 99999, 88888)
    ops.node(33022, 12.125, 13.5, 8.7)
    ops.element('elasticBeamColumn', 33022, 3022, 33022, 99999, 88888)
    ops.node(23022, 12.0, 13.5, 8.45)
    ops.element('elasticBeamColumn', 23022, 23022, 3022, 99999, 99999)
    ops.node(73022, 12.0, 13.5, 8.95)
    ops.element('elasticBeamColumn', 73022, 3022, 73022, 99999, 99999)
    ops.node(63022, 12.0, 13.375, 8.7)
    ops.element('elasticBeamColumn', 63022, 63022, 3022, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303022, 10.21711986, 0.0002, 10.21711986, 0.0132, 6.31915594, 0.027, -10.21711986, -0.0002, -10.21711986, -0.0132, -6.31915594, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403022, 11.02906033, 0.0002, 13.29871053, 0.009, 13.29871053, 0.02, -11.02906033, -0.0002, -13.29871053, -0.009, -13.29871053, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403022, 'My', 303022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13022, 3022, 13022, 13022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 3)
    # Central joint node
    ops.node(3023, 16.5, 13.5, 8.7, '-mass', 14.73776758409786, 14.73776758409786, 14.73776758409786, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53023, 16.375, 13.5, 8.7)
    ops.element('elasticBeamColumn', 53023, 53023, 3023, 99999, 88888)
    ops.node(33023, 16.625, 13.5, 8.7)
    ops.element('elasticBeamColumn', 33023, 3023, 33023, 99999, 88888)
    ops.node(23023, 16.5, 13.5, 8.475)
    ops.element('elasticBeamColumn', 23023, 23023, 3023, 99999, 99999)
    ops.node(73023, 16.5, 13.5, 8.925)
    ops.element('elasticBeamColumn', 73023, 3023, 73023, 99999, 99999)
    ops.node(63023, 16.5, 13.375, 8.7)
    ops.element('elasticBeamColumn', 63023, 63023, 3023, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303023, 9.55370277, 0.0002, 9.55370277, 0.0132, 5.93096673, 0.027, -9.55370277, -0.0002, -9.55370277, -0.0132, -5.93096673, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403023, 11.76460415, 0.0002, 14.1822818, 0.009, 14.1822818, 0.02, -11.76460415, -0.0002, -14.1822818, -0.009, -14.1822818, -0.02, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403023, 'My', 303023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13023, 3023, 13023, 13023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 3)
    # Central joint node
    ops.node(3024, 21.0, 13.5, 8.7, '-mass', 9.498088685015292, 9.498088685015292, 9.498088685015292, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53024, 20.875, 13.5, 8.7)
    ops.element('elasticBeamColumn', 53024, 53024, 3024, 99999, 88888)
    ops.node(23024, 21.0, 13.5, 8.475)
    ops.element('elasticBeamColumn', 23024, 23024, 3024, 99999, 99999)
    ops.node(73024, 21.0, 13.5, 8.925)
    ops.element('elasticBeamColumn', 73024, 3024, 73024, 99999, 99999)
    ops.node(63024, 21.0, 13.375, 8.7)
    ops.element('elasticBeamColumn', 63024, 63024, 3024, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 303024, 7.4847677, 0.0002, 7.4847677, 0.0132, 4.61676307, 0.027, -7.4847677, -0.0002, -7.4847677, -0.0132, -4.61676307, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 403024, 6.4944277, 0.0002, 6.4944277, 0.0132, 4.01708409, 0.027, -6.4944277, -0.0002, -6.4944277, -0.0132, -4.01708409, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 13024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403024, 'My', 303024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13024, 3024, 13024, 13024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 11.5, '-mass', 5.264525993883791, 5.264525993883791, 5.264525993883791, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 11.5)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 11.325)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 11.5)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304001, 6.25570988, 0.0002, 6.25570988, 0.0132, 3.82028539, 0.027, -6.25570988, -0.0002, -6.25570988, -0.0132, -3.82028539, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404001, 5.29482969, 0.0002, 5.29482969, 0.0132, 3.24828575, 0.027, -5.29482969, -0.0002, -5.29482969, -0.0132, -3.24828575, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404001, 'My', 304001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14001, 4001, 14001, 14001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 4.5, 0.0, 11.5, '-mass', 10.094801223241591, 10.094801223241591, 10.094801223241591, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 4.375, 0.0, 11.5)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 4.625, 0.0, 11.5)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 4.5, 0.0, 11.3)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 4.5, 0.125, 11.5)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304002, 9.68522294, 0.0002, 9.68522294, 0.0132, 5.95956928, 0.027, -9.68522294, -0.0002, -9.68522294, -0.0132, -5.95956928, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404002, 7.13170046, 0.0002, 7.13170046, 0.0132, 4.41775703, 0.027, -7.13170046, -0.0002, -7.13170046, -0.0132, -4.41775703, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404002, 'My', 304002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14002, 4002, 14002, 14002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 9.0, 0.0, 11.5, '-mass', 5.611620795107034, 5.611620795107034, 5.611620795107034, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 8.875, 0.0, 11.5)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 9.125, 0.0, 11.5)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 9.0, 0.0, 11.275)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 9.0, 0.125, 11.5)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304003, 8.45530907, 0.0002, 8.45530907, 0.0132, 5.12379061, 0.027, -8.45530907, -0.0002, -8.45530907, -0.0132, -5.12379061, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404003, 5.43340308, 0.0002, 5.43340308, 0.0132, 3.33665189, 0.027, -5.43340308, -0.0002, -5.43340308, -0.0132, -3.33665189, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404003, 'My', 304003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14003, 4003, 14003, 14003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 12.0, 0.0, 11.5, '-mass', 5.611620795107034, 5.611620795107034, 5.611620795107034, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 11.875, 0.0, 11.5)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(34004, 12.125, 0.0, 11.5)
    ops.element('elasticBeamColumn', 34004, 4004, 34004, 99999, 88888)
    ops.node(24004, 12.0, 0.0, 11.275)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 12.0, 0.125, 11.5)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304004, 8.45530907, 0.0002, 8.45530907, 0.0132, 5.12379061, 0.027, -8.45530907, -0.0002, -8.45530907, -0.0132, -5.12379061, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404004, 5.43340308, 0.0002, 5.43340308, 0.0132, 3.33665189, 0.027, -5.43340308, -0.0002, -5.43340308, -0.0132, -3.33665189, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404004, 'My', 304004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14004, 4004, 14004, 14004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 4)
    # Central joint node
    ops.node(4005, 16.5, 0.0, 11.5, '-mass', 10.094801223241591, 10.094801223241591, 10.094801223241591, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54005, 16.375, 0.0, 11.5)
    ops.element('elasticBeamColumn', 54005, 54005, 4005, 99999, 88888)
    ops.node(34005, 16.625, 0.0, 11.5)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 16.5, 0.0, 11.3)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(44005, 16.5, 0.125, 11.5)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304005, 9.68522294, 0.0002, 9.68522294, 0.0132, 5.95956928, 0.027, -9.68522294, -0.0002, -9.68522294, -0.0132, -5.95956928, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404005, 7.13170046, 0.0002, 7.13170046, 0.0132, 4.41775703, 0.027, -7.13170046, -0.0002, -7.13170046, -0.0132, -4.41775703, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404005, 'My', 304005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14005, 4005, 14005, 14005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 4)
    # Central joint node
    ops.node(4006, 21.0, 0.0, 11.5, '-mass', 5.264525993883791, 5.264525993883791, 5.264525993883791, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 20.875, 0.0, 11.5)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(24006, 21.0, 0.0, 11.325)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(44006, 21.0, 0.125, 11.5)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304006, 6.25570988, 0.0002, 6.25570988, 0.0132, 3.82028539, 0.027, -6.25570988, -0.0002, -6.25570988, -0.0132, -3.82028539, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404006, 5.29482969, 0.0002, 5.29482969, 0.0132, 3.24828575, 0.027, -5.29482969, -0.0002, -5.29482969, -0.0132, -3.24828575, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404006, 'My', 304006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14006, 4006, 14006, 14006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4007, 0.0, 4.5, 11.5, '-mass', 10.039755351681956, 10.039755351681956, 10.039755351681956, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34007, 0.125, 4.5, 11.5)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 0.0, 4.5, 11.325)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 0.0, 4.375, 11.5)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 0.0, 4.625, 11.5)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304007, 8.37599221, 0.0002, 8.37599221, 0.0132, 5.17081814, 0.027, -8.37599221, -0.0002, -8.37599221, -0.0132, -5.17081814, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404007, 8.37599221, 0.0002, 8.37599221, 0.0132, 5.17081814, 0.027, -8.37599221, -0.0002, -8.37599221, -0.0132, -5.17081814, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404007, 'My', 304007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14007, 4007, 14007, 14007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4008, 4.5, 4.5, 11.5, '-mass', 19.630581039755352, 19.630581039755352, 19.630581039755352, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 4.325, 4.5, 11.5)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(34008, 4.675, 4.5, 11.5)
    ops.element('elasticBeamColumn', 34008, 4008, 34008, 99999, 88888)
    ops.node(24008, 4.5, 4.5, 11.3)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 4.5, 4.325, 11.5)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 4.5, 4.675, 11.5)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304008, 17.35507942, 0.0002, 17.35507942, 0.0132, 10.74133393, 0.027, -17.35507942, -0.0002, -17.35507942, -0.0132, -10.74133393, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404008, 15.07886854, 0.0002, 15.07886854, 0.0132, 9.3565599, 0.027, -15.07886854, -0.0002, -15.07886854, -0.0132, -9.3565599, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404008, 'My', 304008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14008, 4008, 14008, 14008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4009, 9.0, 4.5, 11.5, '-mass', 16.41727828746177, 16.41727828746177, 16.41727828746177, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54009, 8.825, 4.5, 11.5)
    ops.element('elasticBeamColumn', 54009, 54009, 4009, 99999, 88888)
    ops.node(34009, 9.175, 4.5, 11.5)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 9.0, 4.5, 11.275)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 9.0, 4.325, 11.5)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 9.0, 4.675, 11.5)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304009, 18.12328306, 0.0002, 18.12328306, 0.0132, 11.15847944, 0.027, -18.12328306, -0.0002, -18.12328306, -0.0132, -11.15847944, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404009, 13.88047958, 0.0002, 13.88047958, 0.0132, 8.59415171, 0.027, -13.88047958, -0.0002, -13.88047958, -0.0132, -8.59415171, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404009, 'My', 304009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14009, 4009, 14009, 14009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4010, 12.0, 4.5, 11.5, '-mass', 16.41727828746177, 16.41727828746177, 16.41727828746177, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 11.825, 4.5, 11.5)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 12.175, 4.5, 11.5)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 12.0, 4.5, 11.275)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 12.0, 4.325, 11.5)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 12.0, 4.675, 11.5)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304010, 18.12328306, 0.0002, 18.12328306, 0.0132, 11.15847944, 0.027, -18.12328306, -0.0002, -18.12328306, -0.0132, -11.15847944, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404010, 13.88047958, 0.0002, 13.88047958, 0.0132, 8.59415171, 0.027, -13.88047958, -0.0002, -13.88047958, -0.0132, -8.59415171, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404010, 'My', 304010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14010, 4010, 14010, 14010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 4)
    # Central joint node
    ops.node(4011, 16.5, 4.5, 11.5, '-mass', 19.630581039755352, 19.630581039755352, 19.630581039755352, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 16.325, 4.5, 11.5)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 16.675, 4.5, 11.5)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 16.5, 4.5, 11.3)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 16.5, 4.325, 11.5)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 16.5, 4.675, 11.5)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304011, 17.35507942, 0.0002, 17.35507942, 0.0132, 10.74133393, 0.027, -17.35507942, -0.0002, -17.35507942, -0.0132, -10.74133393, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404011, 15.07886854, 0.0002, 15.07886854, 0.0132, 9.3565599, 0.027, -15.07886854, -0.0002, -15.07886854, -0.0132, -9.3565599, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404011, 'My', 304011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14011, 4011, 14011, 14011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 4)
    # Central joint node
    ops.node(4012, 21.0, 4.5, 11.5, '-mass', 10.039755351681956, 10.039755351681956, 10.039755351681956, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 20.875, 4.5, 11.5)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 21.0, 4.5, 11.325)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 21.0, 4.375, 11.5)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 21.0, 4.625, 11.5)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304012, 8.37599221, 0.0002, 8.37599221, 0.0132, 5.17081814, 0.027, -8.37599221, -0.0002, -8.37599221, -0.0132, -5.17081814, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404012, 8.37599221, 0.0002, 8.37599221, 0.0132, 5.17081814, 0.027, -8.37599221, -0.0002, -8.37599221, -0.0132, -5.17081814, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404012, 'My', 304012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14012, 4012, 14012, 14012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4013, 0.0, 9.0, 11.5, '-mass', 10.039755351681956, 10.039755351681956, 10.039755351681956, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.125, 9.0, 11.5)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 9.0, 11.325)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 8.875, 11.5)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    ops.node(44013, 0.0, 9.125, 11.5)
    ops.element('elasticBeamColumn', 44013, 4013, 44013, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304013, 8.37599221, 0.0002, 8.37599221, 0.0132, 5.17081814, 0.027, -8.37599221, -0.0002, -8.37599221, -0.0132, -5.17081814, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404013, 8.37599221, 0.0002, 8.37599221, 0.0132, 5.17081814, 0.027, -8.37599221, -0.0002, -8.37599221, -0.0132, -5.17081814, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404013, 'My', 304013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14013, 4013, 14013, 14013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4014, 4.5, 9.0, 11.5, '-mass', 19.630581039755352, 19.630581039755352, 19.630581039755352, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 4.325, 9.0, 11.5)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 4.675, 9.0, 11.5)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 4.5, 9.0, 11.3)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 4.5, 8.825, 11.5)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    ops.node(44014, 4.5, 9.175, 11.5)
    ops.element('elasticBeamColumn', 44014, 4014, 44014, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304014, 17.35507942, 0.0002, 17.35507942, 0.0132, 10.74133393, 0.027, -17.35507942, -0.0002, -17.35507942, -0.0132, -10.74133393, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404014, 15.07886854, 0.0002, 15.07886854, 0.0132, 9.3565599, 0.027, -15.07886854, -0.0002, -15.07886854, -0.0132, -9.3565599, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404014, 'My', 304014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14014, 4014, 14014, 14014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4015, 9.0, 9.0, 11.5, '-mass', 17.392048929663606, 17.392048929663606, 17.392048929663606, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 8.825, 9.0, 11.5)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 9.175, 9.0, 11.5)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 9.0, 9.0, 11.275)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 9.0, 8.825, 11.5)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    ops.node(44015, 9.0, 9.175, 11.5)
    ops.element('elasticBeamColumn', 44015, 4015, 44015, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304015, 18.60465383, 0.0002, 18.60465383, 0.0132, 11.46496774, 0.027, -18.60465383, -0.0002, -18.60465383, -0.0132, -11.46496774, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404015, 14.25522454, 0.0002, 14.25522454, 0.0132, 8.83262059, 0.027, -14.25522454, -0.0002, -14.25522454, -0.0132, -8.83262059, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404015, 'My', 304015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14015, 4015, 14015, 14015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4016, 12.0, 9.0, 11.5, '-mass', 17.392048929663606, 17.392048929663606, 17.392048929663606, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 11.825, 9.0, 11.5)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(34016, 12.175, 9.0, 11.5)
    ops.element('elasticBeamColumn', 34016, 4016, 34016, 99999, 88888)
    ops.node(24016, 12.0, 9.0, 11.275)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 12.0, 8.825, 11.5)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    ops.node(44016, 12.0, 9.175, 11.5)
    ops.element('elasticBeamColumn', 44016, 4016, 44016, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304016, 18.60465383, 0.0002, 18.60465383, 0.0132, 11.46496774, 0.027, -18.60465383, -0.0002, -18.60465383, -0.0132, -11.46496774, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404016, 14.25522454, 0.0002, 14.25522454, 0.0132, 8.83262059, 0.027, -14.25522454, -0.0002, -14.25522454, -0.0132, -8.83262059, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404016, 'My', 304016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14016, 4016, 14016, 14016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 4)
    # Central joint node
    ops.node(4017, 16.5, 9.0, 11.5, '-mass', 19.630581039755352, 19.630581039755352, 19.630581039755352, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54017, 16.325, 9.0, 11.5)
    ops.element('elasticBeamColumn', 54017, 54017, 4017, 99999, 88888)
    ops.node(34017, 16.675, 9.0, 11.5)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 16.5, 9.0, 11.3)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(64017, 16.5, 8.825, 11.5)
    ops.element('elasticBeamColumn', 64017, 64017, 4017, 99999, 77777)
    ops.node(44017, 16.5, 9.175, 11.5)
    ops.element('elasticBeamColumn', 44017, 4017, 44017, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304017, 17.35507942, 0.0002, 17.35507942, 0.0132, 10.74133393, 0.027, -17.35507942, -0.0002, -17.35507942, -0.0132, -10.74133393, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404017, 15.07886854, 0.0002, 15.07886854, 0.0132, 9.3565599, 0.027, -15.07886854, -0.0002, -15.07886854, -0.0132, -9.3565599, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404017, 'My', 304017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14017, 4017, 14017, 14017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 4)
    # Central joint node
    ops.node(4018, 21.0, 9.0, 11.5, '-mass', 10.039755351681956, 10.039755351681956, 10.039755351681956, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 20.875, 9.0, 11.5)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(24018, 21.0, 9.0, 11.325)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(64018, 21.0, 8.875, 11.5)
    ops.element('elasticBeamColumn', 64018, 64018, 4018, 99999, 77777)
    ops.node(44018, 21.0, 9.125, 11.5)
    ops.element('elasticBeamColumn', 44018, 4018, 44018, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304018, 8.37599221, 0.0002, 8.37599221, 0.0132, 5.17081814, 0.027, -8.37599221, -0.0002, -8.37599221, -0.0132, -5.17081814, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404018, 8.37599221, 0.0002, 8.37599221, 0.0132, 5.17081814, 0.027, -8.37599221, -0.0002, -8.37599221, -0.0132, -5.17081814, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404018, 'My', 304018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14018, 4018, 14018, 14018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    # Central joint node
    ops.node(4019, 0.0, 13.5, 11.5, '-mass', 5.264525993883791, 5.264525993883791, 5.264525993883791, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34019, 0.125, 13.5, 11.5)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 0.0, 13.5, 11.325)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(64019, 0.0, 13.375, 11.5)
    ops.element('elasticBeamColumn', 64019, 64019, 4019, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304019, 6.25570988, 0.0002, 6.25570988, 0.0132, 3.82028539, 0.027, -6.25570988, -0.0002, -6.25570988, -0.0132, -3.82028539, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404019, 5.29482969, 0.0002, 5.29482969, 0.0132, 3.24828575, 0.027, -5.29482969, -0.0002, -5.29482969, -0.0132, -3.24828575, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404019, 'My', 304019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14019, 4019, 14019, 14019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    # Central joint node
    ops.node(4020, 4.5, 13.5, 11.5, '-mass', 10.094801223241591, 10.094801223241591, 10.094801223241591, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 4.375, 13.5, 11.5)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(34020, 4.625, 13.5, 11.5)
    ops.element('elasticBeamColumn', 34020, 4020, 34020, 99999, 88888)
    ops.node(24020, 4.5, 13.5, 11.3)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(64020, 4.5, 13.375, 11.5)
    ops.element('elasticBeamColumn', 64020, 64020, 4020, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304020, 9.68522294, 0.0002, 9.68522294, 0.0132, 5.95956928, 0.027, -9.68522294, -0.0002, -9.68522294, -0.0132, -5.95956928, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404020, 7.13170046, 0.0002, 7.13170046, 0.0132, 4.41775703, 0.027, -7.13170046, -0.0002, -7.13170046, -0.0132, -4.41775703, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404020, 'My', 304020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14020, 4020, 14020, 14020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    # Central joint node
    ops.node(4021, 9.0, 13.5, 11.5, '-mass', 8.92966360856269, 8.92966360856269, 8.92966360856269, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54021, 8.875, 13.5, 11.5)
    ops.element('elasticBeamColumn', 54021, 54021, 4021, 99999, 88888)
    ops.node(34021, 9.125, 13.5, 11.5)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 9.0, 13.5, 11.275)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(64021, 9.0, 13.375, 11.5)
    ops.element('elasticBeamColumn', 64021, 64021, 4021, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304021, 10.40593479, 0.0002, 10.40593479, 0.0132, 6.36786349, 0.027, -10.40593479, -0.0002, -10.40593479, -0.0132, -6.36786349, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404021, 6.73732014, 0.0002, 6.73732014, 0.0132, 4.16693988, 0.027, -6.73732014, -0.0002, -6.73732014, -0.0132, -4.16693988, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404021, 'My', 304021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14021, 4021, 14021, 14021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    # Central joint node
    ops.node(4022, 12.0, 13.5, 11.5, '-mass', 8.92966360856269, 8.92966360856269, 8.92966360856269, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 11.875, 13.5, 11.5)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(34022, 12.125, 13.5, 11.5)
    ops.element('elasticBeamColumn', 34022, 4022, 34022, 99999, 88888)
    ops.node(24022, 12.0, 13.5, 11.275)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(64022, 12.0, 13.375, 11.5)
    ops.element('elasticBeamColumn', 64022, 64022, 4022, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304022, 10.40593479, 0.0002, 10.40593479, 0.0132, 6.36786349, 0.027, -10.40593479, -0.0002, -10.40593479, -0.0132, -6.36786349, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404022, 6.73732014, 0.0002, 6.73732014, 0.0132, 4.16693988, 0.027, -6.73732014, -0.0002, -6.73732014, -0.0132, -4.16693988, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404022, 'My', 304022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14022, 4022, 14022, 14022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 4)
    # Central joint node
    ops.node(4023, 16.5, 13.5, 11.5, '-mass', 10.094801223241591, 10.094801223241591, 10.094801223241591, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54023, 16.375, 13.5, 11.5)
    ops.element('elasticBeamColumn', 54023, 54023, 4023, 99999, 88888)
    ops.node(34023, 16.625, 13.5, 11.5)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 16.5, 13.5, 11.3)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(64023, 16.5, 13.375, 11.5)
    ops.element('elasticBeamColumn', 64023, 64023, 4023, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304023, 9.68522294, 0.0002, 9.68522294, 0.0132, 5.95956928, 0.027, -9.68522294, -0.0002, -9.68522294, -0.0132, -5.95956928, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404023, 7.13170046, 0.0002, 7.13170046, 0.0132, 4.41775703, 0.027, -7.13170046, -0.0002, -7.13170046, -0.0132, -4.41775703, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404023, 'My', 304023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14023, 4023, 14023, 14023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 4)
    # Central joint node
    ops.node(4024, 21.0, 13.5, 11.5, '-mass', 5.264525993883791, 5.264525993883791, 5.264525993883791, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 20.875, 13.5, 11.5)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 21.0, 13.5, 11.325)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(64024, 21.0, 13.375, 11.5)
    ops.element('elasticBeamColumn', 64024, 64024, 4024, 99999, 77777)
    # Joint flexibility element: Inelastic
    ops.uniaxialMaterial('Hysteretic', 304024, 6.25570988, 0.0002, 6.25570988, 0.0132, 3.82028539, 0.027, -6.25570988, -0.0002, -6.25570988, -0.0132, -3.82028539, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 404024, 5.29482969, 0.0002, 5.29482969, 0.0132, 3.24828575, 0.027, -5.29482969, -0.0002, -5.29482969, -0.0132, -3.24828575, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.section('Aggregator', 14024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404024, 'My', 304024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14024, 4024, 14024, 14024, '-orient', 0, 0, 1, 0, 1, 0)
