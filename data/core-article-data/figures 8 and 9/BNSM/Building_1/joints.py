import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 0.5)
    # Central joint node
    ops.node(4029, 0.0, 0.0, 1.425, '-mass', 2.816430937818552, 2.816430937818552, 2.816430937818552, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34029, 0.125, 0.0, 1.425)
    ops.element('elasticBeamColumn', 34029, 4029, 34029, 99999, 88888)
    ops.node(24029, 0.0, 0.0, 1.225)
    ops.element('elasticBeamColumn', 24029, 24029, 4029, 99999, 99999)
    ops.node(74029, 0.0, 0.0, 1.625)
    ops.element('elasticBeamColumn', 74029, 4029, 74029, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 0.5)
    # Central joint node
    ops.node(4030, 2.95, 0.0, 1.425, '-mass', 3.0256052497451575, 3.0256052497451575, 3.0256052497451575, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54030, 2.775, 0.0, 1.425)
    ops.element('elasticBeamColumn', 54030, 54030, 4030, 99999, 88888)
    ops.node(24030, 2.95, 0.0, 1.225)
    ops.element('elasticBeamColumn', 24030, 24030, 4030, 99999, 99999)
    ops.node(74030, 2.95, 0.0, 1.625)
    ops.element('elasticBeamColumn', 74030, 4030, 74030, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 1.5)
    # Central joint node
    ops.node(4031, 0.0, 0.0, 4.275, '-mass', 2.7803453109072374, 2.7803453109072374, 2.7803453109072374, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34031, 0.125, 0.0, 4.275)
    ops.element('elasticBeamColumn', 34031, 4031, 34031, 99999, 88888)
    ops.node(24031, 0.0, 0.0, 4.1)
    ops.element('elasticBeamColumn', 24031, 24031, 4031, 99999, 99999)
    ops.node(74031, 0.0, 0.0, 4.45)
    ops.element('elasticBeamColumn', 74031, 4031, 74031, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 1.5)
    # Central joint node
    ops.node(4032, 2.95, 0.0, 4.275, '-mass', 2.9895196228338428, 2.9895196228338428, 2.9895196228338428, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54032, 2.775, 0.0, 4.275)
    ops.element('elasticBeamColumn', 54032, 54032, 4032, 99999, 88888)
    ops.node(24032, 2.95, 0.0, 4.1)
    ops.element('elasticBeamColumn', 24032, 24032, 4032, 99999, 99999)
    ops.node(74032, 2.95, 0.0, 4.45)
    ops.element('elasticBeamColumn', 74032, 4032, 74032, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 2.5)
    # Central joint node
    ops.node(4033, 0.0, 0.0, 7.125, '-mass', 2.7803453109072374, 2.7803453109072374, 2.7803453109072374, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34033, 0.125, 0.0, 7.125)
    ops.element('elasticBeamColumn', 34033, 4033, 34033, 99999, 88888)
    ops.node(24033, 0.0, 0.0, 6.95)
    ops.element('elasticBeamColumn', 24033, 24033, 4033, 99999, 99999)
    ops.node(74033, 0.0, 0.0, 7.3)
    ops.element('elasticBeamColumn', 74033, 4033, 74033, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 2.5)
    # Central joint node
    ops.node(4034, 2.95, 0.0, 7.125, '-mass', 2.7803453109072374, 2.7803453109072374, 2.7803453109072374, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54034, 2.825, 0.0, 7.125)
    ops.element('elasticBeamColumn', 54034, 54034, 4034, 99999, 88888)
    ops.node(24034, 2.95, 0.0, 6.95)
    ops.element('elasticBeamColumn', 24034, 24034, 4034, 99999, 99999)
    ops.node(74034, 2.95, 0.0, 7.3)
    ops.element('elasticBeamColumn', 74034, 4034, 74034, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 3.5)
    # Central joint node
    ops.node(4035, 0.0, 0.0, 9.975, '-mass', 2.7803453109072374, 2.7803453109072374, 2.7803453109072374, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34035, 0.125, 0.0, 9.975)
    ops.element('elasticBeamColumn', 34035, 4035, 34035, 99999, 88888)
    ops.node(24035, 0.0, 0.0, 9.8)
    ops.element('elasticBeamColumn', 24035, 24035, 4035, 99999, 99999)
    ops.node(74035, 0.0, 0.0, 10.15)
    ops.element('elasticBeamColumn', 74035, 4035, 74035, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 3.5)
    # Central joint node
    ops.node(4036, 2.95, 0.0, 9.975, '-mass', 2.7803453109072374, 2.7803453109072374, 2.7803453109072374, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54036, 2.825, 0.0, 9.975)
    ops.element('elasticBeamColumn', 54036, 54036, 4036, 99999, 88888)
    ops.node(24036, 2.95, 0.0, 9.8)
    ops.element('elasticBeamColumn', 24036, 24036, 4036, 99999, 99999)
    ops.node(74036, 2.95, 0.0, 10.15)
    ops.element('elasticBeamColumn', 74036, 4036, 74036, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 2.85, '-mass', 2.7244138634046893, 2.7244138634046893, 2.7244138634046893, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.125, 0.0, 2.85)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 2.55)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.15)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.125, 2.85)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301001, 45028.11815)
    ops.uniaxialMaterial('Elastic', 401001, 68098.83375)
    ops.section('Aggregator', 11001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401001, 'My', 301001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11001, 1001, 11001, 11001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 2.95, 0.0, 2.85, '-mass', 10.30979539600166, 10.30979539600166, 10.30979539600166, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 2.775, 0.0, 2.85)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 3.125, 0.0, 2.85)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 2.95, 0.0, 2.55)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 2.95, 0.0, 3.15)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 2.95, 0.175, 2.85)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301002, 82179.1421)
    ops.uniaxialMaterial('Elastic', 401002, 207103.4083)
    ops.section('Aggregator', 11002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401002, 'My', 301002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11002, 1002, 11002, 11002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 9.6, 0.0, 2.85, '-mass', 16.3144939520441, 16.3144939520441, 16.3144939520441, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 9.4, 0.0, 2.85)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 9.8, 0.0, 2.85)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 9.6, 0.0, 2.55)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 9.6, 0.0, 3.15)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 9.6, 0.2, 2.85)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301003, 92600.44315)
    ops.uniaxialMaterial('Elastic', 401003, 213598.90695)
    ops.section('Aggregator', 11003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401003, 'My', 301003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11003, 1003, 11003, 11003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 16.25, 0.0, 2.85, '-mass', 9.663159310374748, 9.663159310374748, 9.663159310374748, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 16.1, 0.0, 2.85)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(21004, 16.25, 0.0, 2.55)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 16.25, 0.0, 3.15)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 16.25, 0.15, 2.85)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301004, 57931.284)
    ops.uniaxialMaterial('Elastic', 401004, 87460.01875)
    ops.section('Aggregator', 11004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401004, 'My', 301004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11004, 1004, 11004, 11004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1005, 0.0, 3.65, 2.85, '-mass', 7.991689449439301, 7.991689449439301, 7.991689449439301, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31005, 0.125, 3.65, 2.85)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 0.0, 3.65, 2.5)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 0.0, 3.65, 3.2)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(61005, 0.0, 3.525, 2.85)
    ops.element('elasticBeamColumn', 61005, 61005, 1005, 99999, 77777)
    ops.node(41005, 0.0, 3.775, 2.85)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301005, 69474.98045)
    ops.uniaxialMaterial('Elastic', 401005, 82752.78965)
    ops.section('Aggregator', 11005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401005, 'My', 301005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11005, 1005, 11005, 11005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1006, 2.95, 3.65, 2.85, '-mass', 15.952972392309086, 15.952972392309086, 15.952972392309086, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 2.75, 3.65, 2.85)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(31006, 3.15, 3.65, 2.85)
    ops.element('elasticBeamColumn', 31006, 1006, 31006, 99999, 88888)
    ops.node(21006, 2.95, 3.65, 2.5)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 2.95, 3.65, 3.2)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(61006, 2.95, 3.45, 2.85)
    ops.element('elasticBeamColumn', 61006, 61006, 1006, 99999, 77777)
    ops.node(41006, 2.95, 3.85, 2.85)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301006, 126711.3972)
    ops.uniaxialMaterial('Elastic', 401006, 245347.2323)
    ops.section('Aggregator', 11006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401006, 'My', 301006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11006, 1006, 11006, 11006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1007, 9.6, 3.65, 2.85, '-mass', 19.472311043741612, 19.472311043741612, 19.472311043741612, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51007, 9.375, 3.65, 2.85)
    ops.element('elasticBeamColumn', 51007, 51007, 1007, 99999, 88888)
    ops.node(31007, 9.825, 3.65, 2.85)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 9.6, 3.65, 2.5)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 9.6, 3.65, 3.2)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 9.6, 3.425, 2.85)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 9.6, 3.875, 2.85)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301007, 158119.42415)
    ops.uniaxialMaterial('Elastic', 401007, 306161.59195)
    ops.section('Aggregator', 11007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401007, 'My', 301007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11007, 1007, 11007, 11007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1008, 16.25, 3.65, 2.85, '-mass', 12.756695786906482, 12.756695786906482, 12.756695786906482, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 16.075, 3.65, 2.85)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(21008, 16.25, 3.65, 2.5)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 16.25, 3.65, 3.2)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 16.25, 3.475, 2.85)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 16.25, 3.825, 2.85)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301008, 104557.89565)
    ops.uniaxialMaterial('Elastic', 401008, 145023.4851)
    ops.section('Aggregator', 11008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401008, 'My', 301008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11008, 1008, 11008, 11008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1009, 0.0, 7.3, 2.85, '-mass', 7.598835066054951, 7.598835066054951, 7.598835066054951, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31009, 0.125, 7.3, 2.85)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 0.0, 7.3, 2.5)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 0.0, 7.3, 3.2)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 0.0, 7.175, 2.85)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 0.0, 7.425, 2.85)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301009, 67267.68885)
    ops.uniaxialMaterial('Elastic', 401009, 80315.36095)
    ops.section('Aggregator', 11009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401009, 'My', 301009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11009, 1009, 11009, 11009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1010, 2.95, 7.3, 2.85, '-mass', 14.257875399342677, 14.257875399342677, 14.257875399342677, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 2.75, 7.3, 2.85)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 3.15, 7.3, 2.85)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 2.95, 7.3, 2.5)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 2.95, 7.3, 3.2)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 2.95, 7.1, 2.85)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 2.95, 7.5, 2.85)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301010, 120640.5021)
    ops.uniaxialMaterial('Elastic', 401010, 233592.352)
    ops.section('Aggregator', 11010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401010, 'My', 301010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11010, 1010, 11010, 11010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1011, 9.6, 7.3, 2.85, '-mass', 19.472311043741612, 19.472311043741612, 19.472311043741612, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 9.375, 7.3, 2.85)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 9.825, 7.3, 2.85)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 9.6, 7.3, 2.5)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 9.6, 7.3, 3.2)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 9.6, 7.075, 2.85)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 9.6, 7.525, 2.85)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301011, 158119.42415)
    ops.uniaxialMaterial('Elastic', 401011, 306161.59195)
    ops.section('Aggregator', 11011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401011, 'My', 301011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11011, 1011, 11011, 11011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1012, 16.25, 7.3, 2.85, '-mass', 12.756695786906482, 12.756695786906482, 12.756695786906482, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 16.075, 7.3, 2.85)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 16.25, 7.3, 2.5)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 16.25, 7.3, 3.2)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 16.25, 7.125, 2.85)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 16.25, 7.475, 2.85)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301012, 104557.89565)
    ops.uniaxialMaterial('Elastic', 401012, 145023.4851)
    ops.section('Aggregator', 11012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401012, 'My', 301012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11012, 1012, 11012, 11012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    # Central joint node
    ops.node(1013, 0.0, 10.95, 2.85, '-mass', 7.598835066054952, 7.598835066054952, 7.598835066054952, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.125, 10.95, 2.85)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 10.95, 2.5)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 10.95, 3.2)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 10.825, 2.85)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    ops.node(41013, 0.0, 11.075, 2.85)
    ops.element('elasticBeamColumn', 41013, 1013, 41013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301013, 67267.68885)
    ops.uniaxialMaterial('Elastic', 401013, 80315.36095)
    ops.section('Aggregator', 11013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401013, 'My', 301013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11013, 1013, 11013, 11013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    # Central joint node
    ops.node(1014, 2.95, 10.95, 2.85, '-mass', 14.257875399342678, 14.257875399342678, 14.257875399342678, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 2.75, 10.95, 2.85)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 3.15, 10.95, 2.85)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 2.95, 10.95, 2.5)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 2.95, 10.95, 3.2)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 2.95, 10.75, 2.85)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    ops.node(41014, 2.95, 11.15, 2.85)
    ops.element('elasticBeamColumn', 41014, 1014, 41014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301014, 120640.5021)
    ops.uniaxialMaterial('Elastic', 401014, 233592.352)
    ops.section('Aggregator', 11014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401014, 'My', 301014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11014, 1014, 11014, 11014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    # Central joint node
    ops.node(1015, 9.6, 10.95, 2.85, '-mass', 19.472311043741612, 19.472311043741612, 19.472311043741612, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 9.375, 10.95, 2.85)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 9.825, 10.95, 2.85)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 9.6, 10.95, 2.5)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 9.6, 10.95, 3.2)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 9.6, 10.725, 2.85)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    ops.node(41015, 9.6, 11.175, 2.85)
    ops.element('elasticBeamColumn', 41015, 1015, 41015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301015, 158119.42415)
    ops.uniaxialMaterial('Elastic', 401015, 306161.59195)
    ops.section('Aggregator', 11015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401015, 'My', 301015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11015, 1015, 11015, 11015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    # Central joint node
    ops.node(1016, 16.25, 10.95, 2.85, '-mass', 12.756695786906482, 12.756695786906482, 12.756695786906482, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 16.075, 10.95, 2.85)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(21016, 16.25, 10.95, 2.5)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 16.25, 10.95, 3.2)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 16.25, 10.775, 2.85)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    ops.node(41016, 16.25, 11.125, 2.85)
    ops.element('elasticBeamColumn', 41016, 1016, 41016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301016, 104557.89565)
    ops.uniaxialMaterial('Elastic', 401016, 145023.4851)
    ops.section('Aggregator', 11016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401016, 'My', 301016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11016, 1016, 11016, 11016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 1)
    # Central joint node
    ops.node(1017, 0.0, 14.6, 2.85, '-mass', 7.598835066054953, 7.598835066054953, 7.598835066054953, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31017, 0.125, 14.6, 2.85)
    ops.element('elasticBeamColumn', 31017, 1017, 31017, 99999, 88888)
    ops.node(21017, 0.0, 14.6, 2.5)
    ops.element('elasticBeamColumn', 21017, 21017, 1017, 99999, 99999)
    ops.node(71017, 0.0, 14.6, 3.2)
    ops.element('elasticBeamColumn', 71017, 1017, 71017, 99999, 99999)
    ops.node(61017, 0.0, 14.475, 2.85)
    ops.element('elasticBeamColumn', 61017, 61017, 1017, 99999, 77777)
    ops.node(41017, 0.0, 14.725, 2.85)
    ops.element('elasticBeamColumn', 41017, 1017, 41017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301017, 67267.68885)
    ops.uniaxialMaterial('Elastic', 401017, 80315.36095)
    ops.section('Aggregator', 11017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401017, 'My', 301017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11017, 1017, 11017, 11017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 1)
    # Central joint node
    ops.node(1018, 2.95, 14.6, 2.85, '-mass', 14.257875399342678, 14.257875399342678, 14.257875399342678, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51018, 2.75, 14.6, 2.85)
    ops.element('elasticBeamColumn', 51018, 51018, 1018, 99999, 88888)
    ops.node(31018, 3.15, 14.6, 2.85)
    ops.element('elasticBeamColumn', 31018, 1018, 31018, 99999, 88888)
    ops.node(21018, 2.95, 14.6, 2.5)
    ops.element('elasticBeamColumn', 21018, 21018, 1018, 99999, 99999)
    ops.node(71018, 2.95, 14.6, 3.2)
    ops.element('elasticBeamColumn', 71018, 1018, 71018, 99999, 99999)
    ops.node(61018, 2.95, 14.4, 2.85)
    ops.element('elasticBeamColumn', 61018, 61018, 1018, 99999, 77777)
    ops.node(41018, 2.95, 14.8, 2.85)
    ops.element('elasticBeamColumn', 41018, 1018, 41018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301018, 120640.5021)
    ops.uniaxialMaterial('Elastic', 401018, 233592.352)
    ops.section('Aggregator', 11018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401018, 'My', 301018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11018, 1018, 11018, 11018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 1)
    # Central joint node
    ops.node(1019, 9.6, 14.6, 2.85, '-mass', 19.472311043741612, 19.472311043741612, 19.472311043741612, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51019, 9.375, 14.6, 2.85)
    ops.element('elasticBeamColumn', 51019, 51019, 1019, 99999, 88888)
    ops.node(31019, 9.825, 14.6, 2.85)
    ops.element('elasticBeamColumn', 31019, 1019, 31019, 99999, 88888)
    ops.node(21019, 9.6, 14.6, 2.5)
    ops.element('elasticBeamColumn', 21019, 21019, 1019, 99999, 99999)
    ops.node(71019, 9.6, 14.6, 3.2)
    ops.element('elasticBeamColumn', 71019, 1019, 71019, 99999, 99999)
    ops.node(61019, 9.6, 14.375, 2.85)
    ops.element('elasticBeamColumn', 61019, 61019, 1019, 99999, 77777)
    ops.node(41019, 9.6, 14.825, 2.85)
    ops.element('elasticBeamColumn', 41019, 1019, 41019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301019, 158119.42415)
    ops.uniaxialMaterial('Elastic', 401019, 306161.59195)
    ops.section('Aggregator', 11019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401019, 'My', 301019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11019, 1019, 11019, 11019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 1)
    # Central joint node
    ops.node(1020, 16.25, 14.6, 2.85, '-mass', 12.756695786906482, 12.756695786906482, 12.756695786906482, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51020, 16.075, 14.6, 2.85)
    ops.element('elasticBeamColumn', 51020, 51020, 1020, 99999, 88888)
    ops.node(21020, 16.25, 14.6, 2.5)
    ops.element('elasticBeamColumn', 21020, 21020, 1020, 99999, 99999)
    ops.node(71020, 16.25, 14.6, 3.2)
    ops.element('elasticBeamColumn', 71020, 1020, 71020, 99999, 99999)
    ops.node(61020, 16.25, 14.425, 2.85)
    ops.element('elasticBeamColumn', 61020, 61020, 1020, 99999, 77777)
    ops.node(41020, 16.25, 14.775, 2.85)
    ops.element('elasticBeamColumn', 41020, 1020, 41020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301020, 104557.89565)
    ops.uniaxialMaterial('Elastic', 401020, 145023.4851)
    ops.section('Aggregator', 11020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401020, 'My', 301020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11020, 1020, 11020, 11020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 1)
    # Central joint node
    ops.node(1021, 0.0, 18.25, 2.85, '-mass', 7.598835066054952, 7.598835066054952, 7.598835066054952, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31021, 0.125, 18.25, 2.85)
    ops.element('elasticBeamColumn', 31021, 1021, 31021, 99999, 88888)
    ops.node(21021, 0.0, 18.25, 2.5)
    ops.element('elasticBeamColumn', 21021, 21021, 1021, 99999, 99999)
    ops.node(71021, 0.0, 18.25, 3.2)
    ops.element('elasticBeamColumn', 71021, 1021, 71021, 99999, 99999)
    ops.node(61021, 0.0, 18.125, 2.85)
    ops.element('elasticBeamColumn', 61021, 61021, 1021, 99999, 77777)
    ops.node(41021, 0.0, 18.375, 2.85)
    ops.element('elasticBeamColumn', 41021, 1021, 41021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301021, 67267.68885)
    ops.uniaxialMaterial('Elastic', 401021, 80315.36095)
    ops.section('Aggregator', 11021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401021, 'My', 301021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11021, 1021, 11021, 11021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 1)
    # Central joint node
    ops.node(1022, 2.95, 18.25, 2.85, '-mass', 14.257875399342677, 14.257875399342677, 14.257875399342677, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51022, 2.75, 18.25, 2.85)
    ops.element('elasticBeamColumn', 51022, 51022, 1022, 99999, 88888)
    ops.node(31022, 3.15, 18.25, 2.85)
    ops.element('elasticBeamColumn', 31022, 1022, 31022, 99999, 88888)
    ops.node(21022, 2.95, 18.25, 2.5)
    ops.element('elasticBeamColumn', 21022, 21022, 1022, 99999, 99999)
    ops.node(71022, 2.95, 18.25, 3.2)
    ops.element('elasticBeamColumn', 71022, 1022, 71022, 99999, 99999)
    ops.node(61022, 2.95, 18.05, 2.85)
    ops.element('elasticBeamColumn', 61022, 61022, 1022, 99999, 77777)
    ops.node(41022, 2.95, 18.45, 2.85)
    ops.element('elasticBeamColumn', 41022, 1022, 41022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301022, 120640.5021)
    ops.uniaxialMaterial('Elastic', 401022, 233592.352)
    ops.section('Aggregator', 11022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401022, 'My', 301022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11022, 1022, 11022, 11022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 1)
    # Central joint node
    ops.node(1023, 9.6, 18.25, 2.85, '-mass', 19.472311043741612, 19.472311043741612, 19.472311043741612, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51023, 9.375, 18.25, 2.85)
    ops.element('elasticBeamColumn', 51023, 51023, 1023, 99999, 88888)
    ops.node(31023, 9.825, 18.25, 2.85)
    ops.element('elasticBeamColumn', 31023, 1023, 31023, 99999, 88888)
    ops.node(21023, 9.6, 18.25, 2.5)
    ops.element('elasticBeamColumn', 21023, 21023, 1023, 99999, 99999)
    ops.node(71023, 9.6, 18.25, 3.2)
    ops.element('elasticBeamColumn', 71023, 1023, 71023, 99999, 99999)
    ops.node(61023, 9.6, 18.025, 2.85)
    ops.element('elasticBeamColumn', 61023, 61023, 1023, 99999, 77777)
    ops.node(41023, 9.6, 18.475, 2.85)
    ops.element('elasticBeamColumn', 41023, 1023, 41023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301023, 158119.42415)
    ops.uniaxialMaterial('Elastic', 401023, 306161.59195)
    ops.section('Aggregator', 11023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401023, 'My', 301023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11023, 1023, 11023, 11023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 1)
    # Central joint node
    ops.node(1024, 16.25, 18.25, 2.85, '-mass', 12.756695786906482, 12.756695786906482, 12.756695786906482, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51024, 16.075, 18.25, 2.85)
    ops.element('elasticBeamColumn', 51024, 51024, 1024, 99999, 88888)
    ops.node(21024, 16.25, 18.25, 2.5)
    ops.element('elasticBeamColumn', 21024, 21024, 1024, 99999, 99999)
    ops.node(71024, 16.25, 18.25, 3.2)
    ops.element('elasticBeamColumn', 71024, 1024, 71024, 99999, 99999)
    ops.node(61024, 16.25, 18.075, 2.85)
    ops.element('elasticBeamColumn', 61024, 61024, 1024, 99999, 77777)
    ops.node(41024, 16.25, 18.425, 2.85)
    ops.element('elasticBeamColumn', 41024, 1024, 41024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301024, 104557.89565)
    ops.uniaxialMaterial('Elastic', 401024, 145023.4851)
    ops.section('Aggregator', 11024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401024, 'My', 301024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11024, 1024, 11024, 11024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 6, 1)
    # Central joint node
    ops.node(1025, 0.0, 21.9, 2.85, '-mass', 5.385554128338382, 5.385554128338382, 5.385554128338382, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31025, 0.125, 21.9, 2.85)
    ops.element('elasticBeamColumn', 31025, 1025, 31025, 99999, 88888)
    ops.node(21025, 0.0, 21.9, 2.55)
    ops.element('elasticBeamColumn', 21025, 21025, 1025, 99999, 99999)
    ops.node(71025, 0.0, 21.9, 3.15)
    ops.element('elasticBeamColumn', 71025, 1025, 71025, 99999, 99999)
    ops.node(61025, 0.0, 21.775, 2.85)
    ops.element('elasticBeamColumn', 61025, 61025, 1025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301025, 40050.46155)
    ops.uniaxialMaterial('Elastic', 401025, 55179.2945)
    ops.section('Aggregator', 11025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401025, 'My', 301025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11025, 1025, 11025, 11025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 6, 1)
    # Central joint node
    ops.node(1026, 2.95, 21.9, 2.85, '-mass', 11.877867363279899, 11.877867363279899, 11.877867363279899, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51026, 2.775, 21.9, 2.85)
    ops.element('elasticBeamColumn', 51026, 51026, 1026, 99999, 88888)
    ops.node(31026, 3.125, 21.9, 2.85)
    ops.element('elasticBeamColumn', 31026, 1026, 31026, 99999, 88888)
    ops.node(21026, 2.95, 21.9, 2.55)
    ops.element('elasticBeamColumn', 21026, 21026, 1026, 99999, 99999)
    ops.node(71026, 2.95, 21.9, 3.15)
    ops.element('elasticBeamColumn', 71026, 1026, 71026, 99999, 99999)
    ops.node(61026, 2.95, 21.725, 2.85)
    ops.element('elasticBeamColumn', 61026, 61026, 1026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301026, 69282.0389)
    ops.uniaxialMaterial('Elastic', 401026, 158938.57005)
    ops.section('Aggregator', 11026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401026, 'My', 301026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11026, 1026, 11026, 11026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 6, 1)
    # Central joint node
    ops.node(1027, 9.6, 21.9, 2.85, '-mass', 16.3144939520441, 16.3144939520441, 16.3144939520441, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51027, 9.4, 21.9, 2.85)
    ops.element('elasticBeamColumn', 51027, 51027, 1027, 99999, 88888)
    ops.node(31027, 9.8, 21.9, 2.85)
    ops.element('elasticBeamColumn', 31027, 1027, 31027, 99999, 88888)
    ops.node(21027, 9.6, 21.9, 2.55)
    ops.element('elasticBeamColumn', 21027, 21027, 1027, 99999, 99999)
    ops.node(71027, 9.6, 21.9, 3.15)
    ops.element('elasticBeamColumn', 71027, 1027, 71027, 99999, 99999)
    ops.node(61027, 9.6, 21.7, 2.85)
    ops.element('elasticBeamColumn', 61027, 61027, 1027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301027, 92600.44315)
    ops.uniaxialMaterial('Elastic', 401027, 213598.90695)
    ops.section('Aggregator', 11027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401027, 'My', 301027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11027, 1027, 11027, 11027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 6, 1)
    # Central joint node
    ops.node(1028, 16.25, 21.9, 2.85, '-mass', 9.663159310374748, 9.663159310374748, 9.663159310374748, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51028, 16.1, 21.9, 2.85)
    ops.element('elasticBeamColumn', 51028, 51028, 1028, 99999, 88888)
    ops.node(21028, 16.25, 21.9, 2.55)
    ops.element('elasticBeamColumn', 21028, 21028, 1028, 99999, 99999)
    ops.node(71028, 16.25, 21.9, 3.15)
    ops.element('elasticBeamColumn', 71028, 1028, 71028, 99999, 99999)
    ops.node(61028, 16.25, 21.75, 2.85)
    ops.element('elasticBeamColumn', 61028, 61028, 1028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301028, 57931.284)
    ops.uniaxialMaterial('Elastic', 401028, 87460.01875)
    ops.section('Aggregator', 11028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401028, 'My', 301028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11028, 1028, 11028, 11028, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 5.7, '-mass', 2.7244138634046893, 2.7244138634046893, 2.7244138634046893, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.125, 0.0, 5.7)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 5.4)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 6.0)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.125, 5.7)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302001, 38341.0272)
    ops.uniaxialMaterial('Elastic', 402001, 58163.24665)
    ops.section('Aggregator', 12001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402001, 'My', 302001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12001, 2001, 12001, 12001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 2.95, 0.0, 5.7, '-mass', 10.205208240038356, 10.205208240038356, 10.205208240038356, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 2.775, 0.0, 5.7)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 3.125, 0.0, 5.7)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 2.95, 0.0, 5.4)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 2.95, 0.0, 6.0)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 2.95, 0.175, 5.7)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302002, 70160.6102)
    ops.uniaxialMaterial('Elastic', 402002, 175836.6714)
    ops.section('Aggregator', 12002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402002, 'My', 302002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12002, 2002, 12002, 12002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 9.6, 0.0, 5.7, '-mass', 16.049815052961527, 16.049815052961527, 16.049815052961527, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 9.4, 0.0, 5.7)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 9.8, 0.0, 5.7)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 9.6, 0.0, 5.4)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 9.6, 0.0, 6.0)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 9.6, 0.2, 5.7)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302003, 68350.6713)
    ops.uniaxialMaterial('Elastic', 402003, 183109.93)
    ops.section('Aggregator', 12003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402003, 'My', 302003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12003, 2003, 12003, 12003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 16.25, 0.0, 5.7, '-mass', 9.522639432698908, 9.522639432698908, 9.522639432698908, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 16.1, 0.0, 5.7)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(22004, 16.25, 0.0, 5.4)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 16.25, 0.0, 6.0)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 16.25, 0.15, 5.7)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302004, 42618.6329)
    ops.uniaxialMaterial('Elastic', 402004, 75427.42085)
    ops.section('Aggregator', 12004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402004, 'My', 302004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12004, 2004, 12004, 12004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2005, 0.0, 3.65, 5.7, '-mass', 7.991689449439301, 7.991689449439301, 7.991689449439301, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32005, 0.125, 3.65, 5.7)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 0.0, 3.65, 5.35)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 0.0, 3.65, 6.05)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(62005, 0.0, 3.525, 5.7)
    ops.element('elasticBeamColumn', 62005, 62005, 2005, 99999, 77777)
    ops.node(42005, 0.0, 3.775, 5.7)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302005, 59677.3885)
    ops.uniaxialMaterial('Elastic', 402005, 71933.4169)
    ops.section('Aggregator', 12005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402005, 'My', 302005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12005, 2005, 12005, 12005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2006, 2.95, 3.65, 5.7, '-mass', 15.822238447354955, 15.822238447354955, 15.822238447354955, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 2.75, 3.65, 5.7)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(32006, 3.15, 3.65, 5.7)
    ops.element('elasticBeamColumn', 32006, 2006, 32006, 99999, 88888)
    ops.node(22006, 2.95, 3.65, 5.35)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 2.95, 3.65, 6.05)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(62006, 2.95, 3.45, 5.7)
    ops.element('elasticBeamColumn', 62006, 62006, 2006, 99999, 77777)
    ops.node(42006, 2.95, 3.85, 5.7)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302006, 110103.8182)
    ops.uniaxialMaterial('Elastic', 402006, 213190.5074)
    ops.section('Aggregator', 12006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402006, 'My', 302006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12006, 2006, 12006, 12006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2007, 9.6, 3.65, 5.7, '-mass', 18.92552205291592, 18.92552205291592, 18.92552205291592, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52007, 9.375, 3.65, 5.7)
    ops.element('elasticBeamColumn', 52007, 52007, 2007, 99999, 88888)
    ops.node(32007, 9.825, 3.65, 5.7)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 9.6, 3.65, 5.35)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 9.6, 3.65, 6.05)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 9.6, 3.425, 5.7)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 9.6, 3.875, 5.7)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302007, 118480.3997)
    ops.uniaxialMaterial('Elastic', 402007, 258784.6189)
    ops.section('Aggregator', 12007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402007, 'My', 302007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12007, 2007, 12007, 12007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2008, 16.25, 3.65, 5.7, '-mass', 12.45822483889425, 12.45822483889425, 12.45822483889425, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 16.075, 3.65, 5.7)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(22008, 16.25, 3.65, 5.35)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 16.25, 3.65, 6.05)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 16.25, 3.475, 5.7)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 16.25, 3.825, 5.7)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302008, 77568.3377)
    ops.uniaxialMaterial('Elastic', 402008, 126090.26265)
    ops.section('Aggregator', 12008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402008, 'My', 302008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12008, 2008, 12008, 12008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2009, 0.0, 7.3, 5.7, '-mass', 7.598835066054951, 7.598835066054951, 7.598835066054951, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32009, 0.125, 7.3, 5.7)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 0.0, 7.3, 5.35)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 0.0, 7.3, 6.05)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 0.0, 7.175, 5.7)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 0.0, 7.425, 5.7)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302009, 57641.6166)
    ops.uniaxialMaterial('Elastic', 402009, 69685.23725)
    ops.section('Aggregator', 12009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402009, 'My', 302009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12009, 2009, 12009, 12009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2010, 2.95, 7.3, 5.7, '-mass', 14.127141454388546, 14.127141454388546, 14.127141454388546, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 2.75, 7.3, 5.7)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 3.15, 7.3, 5.7)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 2.95, 7.3, 5.35)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 2.95, 7.3, 6.05)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 2.95, 7.1, 5.7)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 2.95, 7.5, 5.7)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302010, 105079.8443)
    ops.uniaxialMaterial('Elastic', 402010, 203462.7471)
    ops.section('Aggregator', 12010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402010, 'My', 302010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12010, 2010, 12010, 12010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2011, 9.6, 7.3, 5.7, '-mass', 18.92552205291592, 18.92552205291592, 18.92552205291592, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 9.375, 7.3, 5.7)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 9.825, 7.3, 5.7)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 9.6, 7.3, 5.35)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 9.6, 7.3, 6.05)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 9.6, 7.075, 5.7)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 9.6, 7.525, 5.7)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302011, 118480.3997)
    ops.uniaxialMaterial('Elastic', 402011, 258784.6189)
    ops.section('Aggregator', 12011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402011, 'My', 302011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12011, 2011, 12011, 12011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2012, 16.25, 7.3, 5.7, '-mass', 12.45822483889425, 12.45822483889425, 12.45822483889425, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 16.075, 7.3, 5.7)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 16.25, 7.3, 5.35)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 16.25, 7.3, 6.05)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 16.25, 7.125, 5.7)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 16.25, 7.475, 5.7)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302012, 77568.3377)
    ops.uniaxialMaterial('Elastic', 402012, 126090.26265)
    ops.section('Aggregator', 12012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402012, 'My', 302012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12012, 2012, 12012, 12012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    # Central joint node
    ops.node(2013, 0.0, 10.95, 5.7, '-mass', 7.598835066054952, 7.598835066054952, 7.598835066054952, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.125, 10.95, 5.7)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 10.95, 5.35)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 10.95, 6.05)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 10.825, 5.7)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    ops.node(42013, 0.0, 11.075, 5.7)
    ops.element('elasticBeamColumn', 42013, 2013, 42013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302013, 57641.6166)
    ops.uniaxialMaterial('Elastic', 402013, 69685.23725)
    ops.section('Aggregator', 12013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402013, 'My', 302013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12013, 2013, 12013, 12013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    # Central joint node
    ops.node(2014, 2.95, 10.95, 5.7, '-mass', 14.12714145438855, 14.12714145438855, 14.12714145438855, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 2.75, 10.95, 5.7)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 3.15, 10.95, 5.7)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 2.95, 10.95, 5.35)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 2.95, 10.95, 6.05)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 2.95, 10.75, 5.7)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    ops.node(42014, 2.95, 11.15, 5.7)
    ops.element('elasticBeamColumn', 42014, 2014, 42014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302014, 105079.8443)
    ops.uniaxialMaterial('Elastic', 402014, 203462.7471)
    ops.section('Aggregator', 12014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402014, 'My', 302014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12014, 2014, 12014, 12014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    # Central joint node
    ops.node(2015, 9.6, 10.95, 5.7, '-mass', 18.92552205291592, 18.92552205291592, 18.92552205291592, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 9.375, 10.95, 5.7)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 9.825, 10.95, 5.7)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 9.6, 10.95, 5.35)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 9.6, 10.95, 6.05)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 9.6, 10.725, 5.7)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    ops.node(42015, 9.6, 11.175, 5.7)
    ops.element('elasticBeamColumn', 42015, 2015, 42015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302015, 118480.3997)
    ops.uniaxialMaterial('Elastic', 402015, 258784.6189)
    ops.section('Aggregator', 12015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402015, 'My', 302015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12015, 2015, 12015, 12015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    # Central joint node
    ops.node(2016, 16.25, 10.95, 5.7, '-mass', 12.45822483889425, 12.45822483889425, 12.45822483889425, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 16.075, 10.95, 5.7)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(22016, 16.25, 10.95, 5.35)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 16.25, 10.95, 6.05)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 16.25, 10.775, 5.7)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    ops.node(42016, 16.25, 11.125, 5.7)
    ops.element('elasticBeamColumn', 42016, 2016, 42016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302016, 77568.3377)
    ops.uniaxialMaterial('Elastic', 402016, 126090.26265)
    ops.section('Aggregator', 12016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402016, 'My', 302016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12016, 2016, 12016, 12016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 2)
    # Central joint node
    ops.node(2017, 0.0, 14.6, 5.7, '-mass', 7.598835066054953, 7.598835066054953, 7.598835066054953, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32017, 0.125, 14.6, 5.7)
    ops.element('elasticBeamColumn', 32017, 2017, 32017, 99999, 88888)
    ops.node(22017, 0.0, 14.6, 5.35)
    ops.element('elasticBeamColumn', 22017, 22017, 2017, 99999, 99999)
    ops.node(72017, 0.0, 14.6, 6.05)
    ops.element('elasticBeamColumn', 72017, 2017, 72017, 99999, 99999)
    ops.node(62017, 0.0, 14.475, 5.7)
    ops.element('elasticBeamColumn', 62017, 62017, 2017, 99999, 77777)
    ops.node(42017, 0.0, 14.725, 5.7)
    ops.element('elasticBeamColumn', 42017, 2017, 42017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302017, 57641.6166)
    ops.uniaxialMaterial('Elastic', 402017, 69685.23725)
    ops.section('Aggregator', 12017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402017, 'My', 302017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12017, 2017, 12017, 12017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 2)
    # Central joint node
    ops.node(2018, 2.95, 14.6, 5.7, '-mass', 14.12714145438855, 14.12714145438855, 14.12714145438855, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52018, 2.75, 14.6, 5.7)
    ops.element('elasticBeamColumn', 52018, 52018, 2018, 99999, 88888)
    ops.node(32018, 3.15, 14.6, 5.7)
    ops.element('elasticBeamColumn', 32018, 2018, 32018, 99999, 88888)
    ops.node(22018, 2.95, 14.6, 5.35)
    ops.element('elasticBeamColumn', 22018, 22018, 2018, 99999, 99999)
    ops.node(72018, 2.95, 14.6, 6.05)
    ops.element('elasticBeamColumn', 72018, 2018, 72018, 99999, 99999)
    ops.node(62018, 2.95, 14.4, 5.7)
    ops.element('elasticBeamColumn', 62018, 62018, 2018, 99999, 77777)
    ops.node(42018, 2.95, 14.8, 5.7)
    ops.element('elasticBeamColumn', 42018, 2018, 42018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302018, 105079.8443)
    ops.uniaxialMaterial('Elastic', 402018, 203462.7471)
    ops.section('Aggregator', 12018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402018, 'My', 302018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12018, 2018, 12018, 12018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 2)
    # Central joint node
    ops.node(2019, 9.6, 14.6, 5.7, '-mass', 18.92552205291592, 18.92552205291592, 18.92552205291592, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52019, 9.375, 14.6, 5.7)
    ops.element('elasticBeamColumn', 52019, 52019, 2019, 99999, 88888)
    ops.node(32019, 9.825, 14.6, 5.7)
    ops.element('elasticBeamColumn', 32019, 2019, 32019, 99999, 88888)
    ops.node(22019, 9.6, 14.6, 5.35)
    ops.element('elasticBeamColumn', 22019, 22019, 2019, 99999, 99999)
    ops.node(72019, 9.6, 14.6, 6.05)
    ops.element('elasticBeamColumn', 72019, 2019, 72019, 99999, 99999)
    ops.node(62019, 9.6, 14.375, 5.7)
    ops.element('elasticBeamColumn', 62019, 62019, 2019, 99999, 77777)
    ops.node(42019, 9.6, 14.825, 5.7)
    ops.element('elasticBeamColumn', 42019, 2019, 42019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302019, 118480.3997)
    ops.uniaxialMaterial('Elastic', 402019, 258784.6189)
    ops.section('Aggregator', 12019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402019, 'My', 302019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12019, 2019, 12019, 12019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 2)
    # Central joint node
    ops.node(2020, 16.25, 14.6, 5.7, '-mass', 12.45822483889425, 12.45822483889425, 12.45822483889425, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52020, 16.075, 14.6, 5.7)
    ops.element('elasticBeamColumn', 52020, 52020, 2020, 99999, 88888)
    ops.node(22020, 16.25, 14.6, 5.35)
    ops.element('elasticBeamColumn', 22020, 22020, 2020, 99999, 99999)
    ops.node(72020, 16.25, 14.6, 6.05)
    ops.element('elasticBeamColumn', 72020, 2020, 72020, 99999, 99999)
    ops.node(62020, 16.25, 14.425, 5.7)
    ops.element('elasticBeamColumn', 62020, 62020, 2020, 99999, 77777)
    ops.node(42020, 16.25, 14.775, 5.7)
    ops.element('elasticBeamColumn', 42020, 2020, 42020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302020, 77568.3377)
    ops.uniaxialMaterial('Elastic', 402020, 126090.26265)
    ops.section('Aggregator', 12020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402020, 'My', 302020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12020, 2020, 12020, 12020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 2)
    # Central joint node
    ops.node(2021, 0.0, 18.25, 5.7, '-mass', 7.598835066054952, 7.598835066054952, 7.598835066054952, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32021, 0.125, 18.25, 5.7)
    ops.element('elasticBeamColumn', 32021, 2021, 32021, 99999, 88888)
    ops.node(22021, 0.0, 18.25, 5.35)
    ops.element('elasticBeamColumn', 22021, 22021, 2021, 99999, 99999)
    ops.node(72021, 0.0, 18.25, 6.05)
    ops.element('elasticBeamColumn', 72021, 2021, 72021, 99999, 99999)
    ops.node(62021, 0.0, 18.125, 5.7)
    ops.element('elasticBeamColumn', 62021, 62021, 2021, 99999, 77777)
    ops.node(42021, 0.0, 18.375, 5.7)
    ops.element('elasticBeamColumn', 42021, 2021, 42021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302021, 57641.6166)
    ops.uniaxialMaterial('Elastic', 402021, 69685.23725)
    ops.section('Aggregator', 12021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402021, 'My', 302021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12021, 2021, 12021, 12021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 2)
    # Central joint node
    ops.node(2022, 2.95, 18.25, 5.7, '-mass', 14.127141454388546, 14.127141454388546, 14.127141454388546, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52022, 2.75, 18.25, 5.7)
    ops.element('elasticBeamColumn', 52022, 52022, 2022, 99999, 88888)
    ops.node(32022, 3.15, 18.25, 5.7)
    ops.element('elasticBeamColumn', 32022, 2022, 32022, 99999, 88888)
    ops.node(22022, 2.95, 18.25, 5.35)
    ops.element('elasticBeamColumn', 22022, 22022, 2022, 99999, 99999)
    ops.node(72022, 2.95, 18.25, 6.05)
    ops.element('elasticBeamColumn', 72022, 2022, 72022, 99999, 99999)
    ops.node(62022, 2.95, 18.05, 5.7)
    ops.element('elasticBeamColumn', 62022, 62022, 2022, 99999, 77777)
    ops.node(42022, 2.95, 18.45, 5.7)
    ops.element('elasticBeamColumn', 42022, 2022, 42022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302022, 105079.8443)
    ops.uniaxialMaterial('Elastic', 402022, 203462.7471)
    ops.section('Aggregator', 12022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402022, 'My', 302022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12022, 2022, 12022, 12022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 2)
    # Central joint node
    ops.node(2023, 9.6, 18.25, 5.7, '-mass', 18.92552205291592, 18.92552205291592, 18.92552205291592, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52023, 9.375, 18.25, 5.7)
    ops.element('elasticBeamColumn', 52023, 52023, 2023, 99999, 88888)
    ops.node(32023, 9.825, 18.25, 5.7)
    ops.element('elasticBeamColumn', 32023, 2023, 32023, 99999, 88888)
    ops.node(22023, 9.6, 18.25, 5.35)
    ops.element('elasticBeamColumn', 22023, 22023, 2023, 99999, 99999)
    ops.node(72023, 9.6, 18.25, 6.05)
    ops.element('elasticBeamColumn', 72023, 2023, 72023, 99999, 99999)
    ops.node(62023, 9.6, 18.025, 5.7)
    ops.element('elasticBeamColumn', 62023, 62023, 2023, 99999, 77777)
    ops.node(42023, 9.6, 18.475, 5.7)
    ops.element('elasticBeamColumn', 42023, 2023, 42023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302023, 118480.3997)
    ops.uniaxialMaterial('Elastic', 402023, 258784.6189)
    ops.section('Aggregator', 12023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402023, 'My', 302023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12023, 2023, 12023, 12023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 2)
    # Central joint node
    ops.node(2024, 16.25, 18.25, 5.7, '-mass', 12.45822483889425, 12.45822483889425, 12.45822483889425, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52024, 16.075, 18.25, 5.7)
    ops.element('elasticBeamColumn', 52024, 52024, 2024, 99999, 88888)
    ops.node(22024, 16.25, 18.25, 5.35)
    ops.element('elasticBeamColumn', 22024, 22024, 2024, 99999, 99999)
    ops.node(72024, 16.25, 18.25, 6.05)
    ops.element('elasticBeamColumn', 72024, 2024, 72024, 99999, 99999)
    ops.node(62024, 16.25, 18.075, 5.7)
    ops.element('elasticBeamColumn', 62024, 62024, 2024, 99999, 77777)
    ops.node(42024, 16.25, 18.425, 5.7)
    ops.element('elasticBeamColumn', 42024, 2024, 42024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302024, 77568.3377)
    ops.uniaxialMaterial('Elastic', 402024, 126090.26265)
    ops.section('Aggregator', 12024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402024, 'My', 302024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12024, 2024, 12024, 12024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 6, 2)
    # Central joint node
    ops.node(2025, 0.0, 21.9, 5.7, '-mass', 5.385554128338382, 5.385554128338382, 5.385554128338382, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32025, 0.125, 21.9, 5.7)
    ops.element('elasticBeamColumn', 32025, 2025, 32025, 99999, 88888)
    ops.node(22025, 0.0, 21.9, 5.4)
    ops.element('elasticBeamColumn', 22025, 22025, 2025, 99999, 99999)
    ops.node(72025, 0.0, 21.9, 6.0)
    ops.element('elasticBeamColumn', 72025, 2025, 72025, 99999, 99999)
    ops.node(62025, 0.0, 21.775, 5.7)
    ops.element('elasticBeamColumn', 62025, 62025, 2025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302025, 34503.6604)
    ops.uniaxialMaterial('Elastic', 402025, 47668.7139)
    ops.section('Aggregator', 12025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402025, 'My', 302025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12025, 2025, 12025, 12025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 6, 2)
    # Central joint node
    ops.node(2026, 2.95, 21.9, 5.7, '-mass', 11.668693051353294, 11.668693051353294, 11.668693051353294, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52026, 2.775, 21.9, 5.7)
    ops.element('elasticBeamColumn', 52026, 52026, 2026, 99999, 88888)
    ops.node(32026, 3.125, 21.9, 5.7)
    ops.element('elasticBeamColumn', 32026, 2026, 32026, 99999, 88888)
    ops.node(22026, 2.95, 21.9, 5.4)
    ops.element('elasticBeamColumn', 22026, 22026, 2026, 99999, 99999)
    ops.node(72026, 2.95, 21.9, 6.0)
    ops.element('elasticBeamColumn', 72026, 2026, 72026, 99999, 99999)
    ops.node(62026, 2.95, 21.725, 5.7)
    ops.element('elasticBeamColumn', 62026, 62026, 2026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302026, 59650.21125)
    ops.uniaxialMaterial('Elastic', 402026, 136106.35245)
    ops.section('Aggregator', 12026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402026, 'My', 302026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12026, 2026, 12026, 12026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 6, 2)
    # Central joint node
    ops.node(2027, 9.6, 21.9, 5.7, '-mass', 16.049815052961527, 16.049815052961527, 16.049815052961527, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52027, 9.4, 21.9, 5.7)
    ops.element('elasticBeamColumn', 52027, 52027, 2027, 99999, 88888)
    ops.node(32027, 9.8, 21.9, 5.7)
    ops.element('elasticBeamColumn', 32027, 2027, 32027, 99999, 88888)
    ops.node(22027, 9.6, 21.9, 5.4)
    ops.element('elasticBeamColumn', 22027, 22027, 2027, 99999, 99999)
    ops.node(72027, 9.6, 21.9, 6.0)
    ops.element('elasticBeamColumn', 72027, 2027, 72027, 99999, 99999)
    ops.node(62027, 9.6, 21.7, 5.7)
    ops.element('elasticBeamColumn', 62027, 62027, 2027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302027, 68350.6713)
    ops.uniaxialMaterial('Elastic', 402027, 183109.93)
    ops.section('Aggregator', 12027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402027, 'My', 302027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12027, 2027, 12027, 12027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 6, 2)
    # Central joint node
    ops.node(2028, 16.25, 21.9, 5.7, '-mass', 9.522639432698908, 9.522639432698908, 9.522639432698908, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52028, 16.1, 21.9, 5.7)
    ops.element('elasticBeamColumn', 52028, 52028, 2028, 99999, 88888)
    ops.node(22028, 16.25, 21.9, 5.4)
    ops.element('elasticBeamColumn', 22028, 22028, 2028, 99999, 99999)
    ops.node(72028, 16.25, 21.9, 6.0)
    ops.element('elasticBeamColumn', 72028, 2028, 72028, 99999, 99999)
    ops.node(62028, 16.25, 21.75, 5.7)
    ops.element('elasticBeamColumn', 62028, 62028, 2028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302028, 42618.6329)
    ops.uniaxialMaterial('Elastic', 402028, 75427.42085)
    ops.section('Aggregator', 12028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402028, 'My', 302028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12028, 2028, 12028, 12028, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 8.55, '-mass', 2.6351172273190624, 2.6351172273190624, 2.6351172273190624, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 8.55)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 8.25)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 8.85)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 8.55)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303001, 29350.17015)
    ops.uniaxialMaterial('Elastic', 403001, 44808.2616)
    ops.section('Aggregator', 13001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403001, 'My', 303001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13001, 3001, 13001, 13001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 2.95, 0.0, 8.55, '-mass', 9.966676129946613, 9.966676129946613, 9.966676129946613, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 2.825, 0.0, 8.55)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 3.075, 0.0, 8.55)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 2.95, 0.0, 8.25)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 2.95, 0.0, 8.85)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 2.95, 0.125, 8.55)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303002, 39374.4548)
    ops.uniaxialMaterial('Elastic', 403002, 97276.9481)
    ops.section('Aggregator', 13002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403002, 'My', 303002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13002, 3002, 13002, 13002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 9.6, 0.0, 8.55, '-mass', 15.874432789964585, 15.874432789964585, 15.874432789964585, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 9.425, 0.0, 8.55)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 9.775, 0.0, 8.55)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 9.6, 0.0, 8.25)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 9.6, 0.0, 8.85)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 9.6, 0.175, 8.55)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303003, 40424.39035)
    ops.uniaxialMaterial('Elastic', 403003, 128119.9059)
    ops.section('Aggregator', 13003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403003, 'My', 303003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13003, 3003, 13003, 13003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 16.25, 0.0, 8.55, '-mass', 9.382119555023067, 9.382119555023067, 9.382119555023067, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 16.125, 0.0, 8.55)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(23004, 16.25, 0.0, 8.25)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 16.25, 0.0, 8.85)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 16.25, 0.125, 8.55)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303004, 26224.12455)
    ops.uniaxialMaterial('Elastic', 403004, 50714.38795)
    ops.section('Aggregator', 13004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403004, 'My', 303004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13004, 3004, 13004, 13004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3005, 0.0, 3.65, 8.55, '-mass', 7.813096177268047, 7.813096177268047, 7.813096177268047, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33005, 0.125, 3.65, 8.55)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 0.0, 3.65, 8.2)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 0.0, 3.65, 8.9)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(63005, 0.0, 3.525, 8.55)
    ops.element('elasticBeamColumn', 63005, 63005, 3005, 99999, 77777)
    ops.node(43005, 0.0, 3.775, 8.55)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303005, 47916.6828)
    ops.uniaxialMaterial('Elastic', 403005, 58944.9435)
    ops.section('Aggregator', 13005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403005, 'My', 303005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13005, 3005, 13005, 13005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3006, 2.95, 3.65, 8.55, '-mass', 15.423614594143942, 15.423614594143942, 15.423614594143942, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 2.775, 3.65, 8.55)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(33006, 3.125, 3.65, 8.55)
    ops.element('elasticBeamColumn', 33006, 3006, 33006, 99999, 88888)
    ops.node(23006, 2.95, 3.65, 8.2)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 2.95, 3.65, 8.9)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(63006, 2.95, 3.475, 8.55)
    ops.element('elasticBeamColumn', 63006, 63006, 3006, 99999, 77777)
    ops.node(43006, 2.95, 3.825, 8.55)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303006, 68039.72415)
    ops.uniaxialMaterial('Elastic', 403006, 152977.6189)
    ops.section('Aggregator', 13006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403006, 'My', 303006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13006, 3006, 13006, 13006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3007, 9.6, 3.65, 8.55, '-mass', 18.557326334261486, 18.557326334261486, 18.557326334261486, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53007, 9.425, 3.65, 8.55)
    ops.element('elasticBeamColumn', 53007, 53007, 3007, 99999, 88888)
    ops.node(33007, 9.775, 3.65, 8.55)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 9.6, 3.65, 8.2)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 9.6, 3.65, 8.9)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 9.6, 3.475, 8.55)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 9.6, 3.825, 8.55)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303007, 64038.9354)
    ops.uniaxialMaterial('Elastic', 403007, 170630.24275)
    ops.section('Aggregator', 13007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403007, 'My', 303007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13007, 3007, 13007, 13007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3008, 16.25, 3.65, 8.55, '-mass', 12.159753890882017, 12.159753890882017, 12.159753890882017, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 16.125, 3.65, 8.55)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(23008, 16.25, 3.65, 8.2)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 16.25, 3.65, 8.9)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 16.25, 3.525, 8.55)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 16.25, 3.775, 8.55)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303008, 44656.2743)
    ops.uniaxialMaterial('Elastic', 403008, 73892.0442)
    ops.section('Aggregator', 13008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403008, 'My', 303008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13008, 3008, 13008, 13008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3009, 0.0, 7.3, 8.55, '-mass', 7.420241793883697, 7.420241793883697, 7.420241793883697, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33009, 0.125, 7.3, 8.55)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 0.0, 7.3, 8.2)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 0.0, 7.3, 8.9)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 0.0, 7.175, 8.55)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 0.0, 7.425, 8.55)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303009, 46045.30335)
    ops.uniaxialMaterial('Elastic', 403009, 56878.0093)
    ops.section('Aggregator', 13009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403009, 'My', 303009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13009, 3009, 13009, 13009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3010, 2.95, 7.3, 8.55, '-mass', 13.728517601177536, 13.728517601177536, 13.728517601177536, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 2.775, 7.3, 8.55)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 3.125, 7.3, 8.55)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 2.95, 7.3, 8.2)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 2.95, 7.3, 8.9)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 2.95, 7.125, 8.55)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 2.95, 7.475, 8.55)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303010, 65225.37995)
    ops.uniaxialMaterial('Elastic', 403010, 146649.9673)
    ops.section('Aggregator', 13010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403010, 'My', 303010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13010, 3010, 13010, 13010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3011, 9.6, 7.3, 8.55, '-mass', 18.557326334261486, 18.557326334261486, 18.557326334261486, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 9.425, 7.3, 8.55)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 9.775, 7.3, 8.55)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 9.6, 7.3, 8.2)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 9.6, 7.3, 8.9)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 9.6, 7.125, 8.55)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 9.6, 7.475, 8.55)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303011, 64038.9354)
    ops.uniaxialMaterial('Elastic', 403011, 170630.24275)
    ops.section('Aggregator', 13011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403011, 'My', 303011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13011, 3011, 13011, 13011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3012, 16.25, 7.3, 8.55, '-mass', 12.159753890882017, 12.159753890882017, 12.159753890882017, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 16.125, 7.3, 8.55)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 16.25, 7.3, 8.2)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 16.25, 7.3, 8.9)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 16.25, 7.175, 8.55)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 16.25, 7.425, 8.55)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303012, 44656.2743)
    ops.uniaxialMaterial('Elastic', 403012, 73892.0442)
    ops.section('Aggregator', 13012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403012, 'My', 303012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13012, 3012, 13012, 13012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    # Central joint node
    ops.node(3013, 0.0, 10.95, 8.55, '-mass', 7.420241793883698, 7.420241793883698, 7.420241793883698, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.125, 10.95, 8.55)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 10.95, 8.2)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 10.95, 8.9)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 10.825, 8.55)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    ops.node(43013, 0.0, 11.075, 8.55)
    ops.element('elasticBeamColumn', 43013, 3013, 43013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303013, 46045.30335)
    ops.uniaxialMaterial('Elastic', 403013, 56878.0093)
    ops.section('Aggregator', 13013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403013, 'My', 303013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13013, 3013, 13013, 13013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    # Central joint node
    ops.node(3014, 2.95, 10.95, 8.55, '-mass', 13.728517601177536, 13.728517601177536, 13.728517601177536, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 2.775, 10.95, 8.55)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 3.125, 10.95, 8.55)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 2.95, 10.95, 8.2)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 2.95, 10.95, 8.9)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 2.95, 10.775, 8.55)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    ops.node(43014, 2.95, 11.125, 8.55)
    ops.element('elasticBeamColumn', 43014, 3014, 43014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303014, 65225.37995)
    ops.uniaxialMaterial('Elastic', 403014, 146649.9673)
    ops.section('Aggregator', 13014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403014, 'My', 303014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13014, 3014, 13014, 13014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    # Central joint node
    ops.node(3015, 9.6, 10.95, 8.55, '-mass', 18.557326334261486, 18.557326334261486, 18.557326334261486, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 9.425, 10.95, 8.55)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 9.775, 10.95, 8.55)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 9.6, 10.95, 8.2)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 9.6, 10.95, 8.9)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 9.6, 10.775, 8.55)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    ops.node(43015, 9.6, 11.125, 8.55)
    ops.element('elasticBeamColumn', 43015, 3015, 43015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303015, 64038.9354)
    ops.uniaxialMaterial('Elastic', 403015, 170630.24275)
    ops.section('Aggregator', 13015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403015, 'My', 303015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13015, 3015, 13015, 13015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    # Central joint node
    ops.node(3016, 16.25, 10.95, 8.55, '-mass', 12.159753890882017, 12.159753890882017, 12.159753890882017, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 16.125, 10.95, 8.55)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(23016, 16.25, 10.95, 8.2)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 16.25, 10.95, 8.9)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 16.25, 10.825, 8.55)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    ops.node(43016, 16.25, 11.075, 8.55)
    ops.element('elasticBeamColumn', 43016, 3016, 43016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303016, 44656.2743)
    ops.uniaxialMaterial('Elastic', 403016, 73892.0442)
    ops.section('Aggregator', 13016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403016, 'My', 303016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13016, 3016, 13016, 13016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 3)
    # Central joint node
    ops.node(3017, 0.0, 14.6, 8.55, '-mass', 7.420241793883698, 7.420241793883698, 7.420241793883698, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33017, 0.125, 14.6, 8.55)
    ops.element('elasticBeamColumn', 33017, 3017, 33017, 99999, 88888)
    ops.node(23017, 0.0, 14.6, 8.2)
    ops.element('elasticBeamColumn', 23017, 23017, 3017, 99999, 99999)
    ops.node(73017, 0.0, 14.6, 8.9)
    ops.element('elasticBeamColumn', 73017, 3017, 73017, 99999, 99999)
    ops.node(63017, 0.0, 14.475, 8.55)
    ops.element('elasticBeamColumn', 63017, 63017, 3017, 99999, 77777)
    ops.node(43017, 0.0, 14.725, 8.55)
    ops.element('elasticBeamColumn', 43017, 3017, 43017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303017, 46045.30335)
    ops.uniaxialMaterial('Elastic', 403017, 56878.0093)
    ops.section('Aggregator', 13017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403017, 'My', 303017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13017, 3017, 13017, 13017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 3)
    # Central joint node
    ops.node(3018, 2.95, 14.6, 8.55, '-mass', 13.728517601177536, 13.728517601177536, 13.728517601177536, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53018, 2.775, 14.6, 8.55)
    ops.element('elasticBeamColumn', 53018, 53018, 3018, 99999, 88888)
    ops.node(33018, 3.125, 14.6, 8.55)
    ops.element('elasticBeamColumn', 33018, 3018, 33018, 99999, 88888)
    ops.node(23018, 2.95, 14.6, 8.2)
    ops.element('elasticBeamColumn', 23018, 23018, 3018, 99999, 99999)
    ops.node(73018, 2.95, 14.6, 8.9)
    ops.element('elasticBeamColumn', 73018, 3018, 73018, 99999, 99999)
    ops.node(63018, 2.95, 14.425, 8.55)
    ops.element('elasticBeamColumn', 63018, 63018, 3018, 99999, 77777)
    ops.node(43018, 2.95, 14.775, 8.55)
    ops.element('elasticBeamColumn', 43018, 3018, 43018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303018, 65225.37995)
    ops.uniaxialMaterial('Elastic', 403018, 146649.9673)
    ops.section('Aggregator', 13018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403018, 'My', 303018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13018, 3018, 13018, 13018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 3)
    # Central joint node
    ops.node(3019, 9.6, 14.6, 8.55, '-mass', 18.557326334261486, 18.557326334261486, 18.557326334261486, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53019, 9.425, 14.6, 8.55)
    ops.element('elasticBeamColumn', 53019, 53019, 3019, 99999, 88888)
    ops.node(33019, 9.775, 14.6, 8.55)
    ops.element('elasticBeamColumn', 33019, 3019, 33019, 99999, 88888)
    ops.node(23019, 9.6, 14.6, 8.2)
    ops.element('elasticBeamColumn', 23019, 23019, 3019, 99999, 99999)
    ops.node(73019, 9.6, 14.6, 8.9)
    ops.element('elasticBeamColumn', 73019, 3019, 73019, 99999, 99999)
    ops.node(63019, 9.6, 14.425, 8.55)
    ops.element('elasticBeamColumn', 63019, 63019, 3019, 99999, 77777)
    ops.node(43019, 9.6, 14.775, 8.55)
    ops.element('elasticBeamColumn', 43019, 3019, 43019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303019, 64038.9354)
    ops.uniaxialMaterial('Elastic', 403019, 170630.24275)
    ops.section('Aggregator', 13019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403019, 'My', 303019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13019, 3019, 13019, 13019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 3)
    # Central joint node
    ops.node(3020, 16.25, 14.6, 8.55, '-mass', 12.159753890882017, 12.159753890882017, 12.159753890882017, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53020, 16.125, 14.6, 8.55)
    ops.element('elasticBeamColumn', 53020, 53020, 3020, 99999, 88888)
    ops.node(23020, 16.25, 14.6, 8.2)
    ops.element('elasticBeamColumn', 23020, 23020, 3020, 99999, 99999)
    ops.node(73020, 16.25, 14.6, 8.9)
    ops.element('elasticBeamColumn', 73020, 3020, 73020, 99999, 99999)
    ops.node(63020, 16.25, 14.475, 8.55)
    ops.element('elasticBeamColumn', 63020, 63020, 3020, 99999, 77777)
    ops.node(43020, 16.25, 14.725, 8.55)
    ops.element('elasticBeamColumn', 43020, 3020, 43020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303020, 44656.2743)
    ops.uniaxialMaterial('Elastic', 403020, 73892.0442)
    ops.section('Aggregator', 13020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403020, 'My', 303020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13020, 3020, 13020, 13020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 3)
    # Central joint node
    ops.node(3021, 0.0, 18.25, 8.55, '-mass', 7.420241793883696, 7.420241793883696, 7.420241793883696, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33021, 0.125, 18.25, 8.55)
    ops.element('elasticBeamColumn', 33021, 3021, 33021, 99999, 88888)
    ops.node(23021, 0.0, 18.25, 8.2)
    ops.element('elasticBeamColumn', 23021, 23021, 3021, 99999, 99999)
    ops.node(73021, 0.0, 18.25, 8.9)
    ops.element('elasticBeamColumn', 73021, 3021, 73021, 99999, 99999)
    ops.node(63021, 0.0, 18.125, 8.55)
    ops.element('elasticBeamColumn', 63021, 63021, 3021, 99999, 77777)
    ops.node(43021, 0.0, 18.375, 8.55)
    ops.element('elasticBeamColumn', 43021, 3021, 43021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303021, 46045.30335)
    ops.uniaxialMaterial('Elastic', 403021, 56878.0093)
    ops.section('Aggregator', 13021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403021, 'My', 303021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13021, 3021, 13021, 13021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 3)
    # Central joint node
    ops.node(3022, 2.95, 18.25, 8.55, '-mass', 13.728517601177536, 13.728517601177536, 13.728517601177536, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53022, 2.775, 18.25, 8.55)
    ops.element('elasticBeamColumn', 53022, 53022, 3022, 99999, 88888)
    ops.node(33022, 3.125, 18.25, 8.55)
    ops.element('elasticBeamColumn', 33022, 3022, 33022, 99999, 88888)
    ops.node(23022, 2.95, 18.25, 8.2)
    ops.element('elasticBeamColumn', 23022, 23022, 3022, 99999, 99999)
    ops.node(73022, 2.95, 18.25, 8.9)
    ops.element('elasticBeamColumn', 73022, 3022, 73022, 99999, 99999)
    ops.node(63022, 2.95, 18.075, 8.55)
    ops.element('elasticBeamColumn', 63022, 63022, 3022, 99999, 77777)
    ops.node(43022, 2.95, 18.425, 8.55)
    ops.element('elasticBeamColumn', 43022, 3022, 43022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303022, 65225.37995)
    ops.uniaxialMaterial('Elastic', 403022, 146649.9673)
    ops.section('Aggregator', 13022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403022, 'My', 303022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13022, 3022, 13022, 13022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 3)
    # Central joint node
    ops.node(3023, 9.6, 18.25, 8.55, '-mass', 18.557326334261486, 18.557326334261486, 18.557326334261486, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53023, 9.425, 18.25, 8.55)
    ops.element('elasticBeamColumn', 53023, 53023, 3023, 99999, 88888)
    ops.node(33023, 9.775, 18.25, 8.55)
    ops.element('elasticBeamColumn', 33023, 3023, 33023, 99999, 88888)
    ops.node(23023, 9.6, 18.25, 8.2)
    ops.element('elasticBeamColumn', 23023, 23023, 3023, 99999, 99999)
    ops.node(73023, 9.6, 18.25, 8.9)
    ops.element('elasticBeamColumn', 73023, 3023, 73023, 99999, 99999)
    ops.node(63023, 9.6, 18.075, 8.55)
    ops.element('elasticBeamColumn', 63023, 63023, 3023, 99999, 77777)
    ops.node(43023, 9.6, 18.425, 8.55)
    ops.element('elasticBeamColumn', 43023, 3023, 43023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303023, 64038.9354)
    ops.uniaxialMaterial('Elastic', 403023, 170630.24275)
    ops.section('Aggregator', 13023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403023, 'My', 303023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13023, 3023, 13023, 13023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 3)
    # Central joint node
    ops.node(3024, 16.25, 18.25, 8.55, '-mass', 12.159753890882017, 12.159753890882017, 12.159753890882017, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53024, 16.125, 18.25, 8.55)
    ops.element('elasticBeamColumn', 53024, 53024, 3024, 99999, 88888)
    ops.node(23024, 16.25, 18.25, 8.2)
    ops.element('elasticBeamColumn', 23024, 23024, 3024, 99999, 99999)
    ops.node(73024, 16.25, 18.25, 8.9)
    ops.element('elasticBeamColumn', 73024, 3024, 73024, 99999, 99999)
    ops.node(63024, 16.25, 18.125, 8.55)
    ops.element('elasticBeamColumn', 63024, 63024, 3024, 99999, 77777)
    ops.node(43024, 16.25, 18.375, 8.55)
    ops.element('elasticBeamColumn', 43024, 3024, 43024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303024, 44656.2743)
    ops.uniaxialMaterial('Elastic', 403024, 73892.0442)
    ops.section('Aggregator', 13024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403024, 'My', 303024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13024, 3024, 13024, 13024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 6, 3)
    # Central joint node
    ops.node(3025, 0.0, 21.9, 8.55, '-mass', 5.296257492252755, 5.296257492252755, 5.296257492252755, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33025, 0.125, 21.9, 8.55)
    ops.element('elasticBeamColumn', 33025, 3025, 33025, 99999, 88888)
    ops.node(23025, 0.0, 21.9, 8.25)
    ops.element('elasticBeamColumn', 23025, 23025, 3025, 99999, 99999)
    ops.node(73025, 0.0, 21.9, 8.85)
    ops.element('elasticBeamColumn', 73025, 3025, 73025, 99999, 99999)
    ops.node(63025, 0.0, 21.775, 8.55)
    ops.element('elasticBeamColumn', 63025, 63025, 3025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303025, 27766.9639)
    ops.uniaxialMaterial('Elastic', 403025, 38548.829)
    ops.section('Aggregator', 13025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403025, 'My', 303025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13025, 3025, 13025, 13025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 6, 3)
    # Central joint node
    ops.node(3026, 2.95, 21.9, 8.55, '-mass', 11.325573785298248, 11.325573785298248, 11.325573785298248, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53026, 2.825, 21.9, 8.55)
    ops.element('elasticBeamColumn', 53026, 53026, 3026, 99999, 88888)
    ops.node(33026, 3.075, 21.9, 8.55)
    ops.element('elasticBeamColumn', 33026, 3026, 33026, 99999, 88888)
    ops.node(23026, 2.95, 21.9, 8.25)
    ops.element('elasticBeamColumn', 23026, 23026, 3026, 99999, 99999)
    ops.node(73026, 2.95, 21.9, 8.85)
    ops.element('elasticBeamColumn', 73026, 3026, 73026, 99999, 99999)
    ops.node(63026, 2.95, 21.775, 8.55)
    ops.element('elasticBeamColumn', 63026, 63026, 3026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303026, 34977.8576)
    ops.uniaxialMaterial('Elastic', 403026, 77168.30895)
    ops.section('Aggregator', 13026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403026, 'My', 303026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13026, 3026, 13026, 13026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 6, 3)
    # Central joint node
    ops.node(3027, 9.6, 21.9, 8.55, '-mass', 15.874432789964585, 15.874432789964585, 15.874432789964585, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53027, 9.425, 21.9, 8.55)
    ops.element('elasticBeamColumn', 53027, 53027, 3027, 99999, 88888)
    ops.node(33027, 9.775, 21.9, 8.55)
    ops.element('elasticBeamColumn', 33027, 3027, 33027, 99999, 88888)
    ops.node(23027, 9.6, 21.9, 8.25)
    ops.element('elasticBeamColumn', 23027, 23027, 3027, 99999, 99999)
    ops.node(73027, 9.6, 21.9, 8.85)
    ops.element('elasticBeamColumn', 73027, 3027, 73027, 99999, 99999)
    ops.node(63027, 9.6, 21.725, 8.55)
    ops.element('elasticBeamColumn', 63027, 63027, 3027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303027, 40424.39035)
    ops.uniaxialMaterial('Elastic', 403027, 128119.9059)
    ops.section('Aggregator', 13027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403027, 'My', 303027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13027, 3027, 13027, 13027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 6, 3)
    # Central joint node
    ops.node(3028, 16.25, 21.9, 8.55, '-mass', 9.382119555023067, 9.382119555023067, 9.382119555023067, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53028, 16.125, 21.9, 8.55)
    ops.element('elasticBeamColumn', 53028, 53028, 3028, 99999, 88888)
    ops.node(23028, 16.25, 21.9, 8.25)
    ops.element('elasticBeamColumn', 23028, 23028, 3028, 99999, 99999)
    ops.node(73028, 16.25, 21.9, 8.85)
    ops.element('elasticBeamColumn', 73028, 3028, 73028, 99999, 99999)
    ops.node(63028, 16.25, 21.775, 8.55)
    ops.element('elasticBeamColumn', 63028, 63028, 3028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303028, 26224.12455)
    ops.uniaxialMaterial('Elastic', 403028, 50714.38795)
    ops.section('Aggregator', 13028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403028, 'My', 303028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13028, 3028, 13028, 13028, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 11.4, '-mass', 0.8279051987767585, 0.8279051987767585, 0.8279051987767585, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 11.4)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 11.15)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 11.4)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304001, 11977.9218)
    ops.uniaxialMaterial('Elastic', 404001, 22402.02065)
    ops.section('Aggregator', 14001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404001, 'My', 304001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14001, 4001, 14001, 14001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 2.95, 0.0, 11.4, '-mass', 4.768956965828368, 4.768956965828368, 4.768956965828368, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 2.825, 0.0, 11.4)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 3.075, 0.0, 11.4)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 2.95, 0.0, 11.15)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 2.95, 0.125, 11.4)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304002, 24652.1853)
    ops.uniaxialMaterial('Elastic', 404002, 43274.98175)
    ops.section('Aggregator', 14002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404002, 'My', 304002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14002, 4002, 14002, 14002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 9.6, 0.0, 11.4, '-mass', 8.577057662543586, 8.577057662543586, 8.577057662543586, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 9.425, 0.0, 11.4)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 9.775, 0.0, 11.4)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 9.6, 0.0, 11.15)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 9.6, 0.175, 11.4)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304003, 45594.3545)
    ops.uniaxialMaterial('Elastic', 404003, 78980.02575)
    ops.section('Aggregator', 14003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404003, 'My', 304003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14003, 4003, 14003, 14003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 16.25, 0.0, 11.4, '-mass', 4.426831583565372, 4.426831583565372, 4.426831583565372, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 16.125, 0.0, 11.4)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(24004, 16.25, 0.0, 11.15)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 16.25, 0.125, 11.4)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304004, 23929.84025)
    ops.uniaxialMaterial('Elastic', 404004, 42077.7436)
    ops.section('Aggregator', 14004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404004, 'My', 304004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14004, 4004, 14004, 14004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4005, 0.0, 3.65, 11.4, '-mass', 4.412930529969372, 4.412930529969372, 4.412930529969372, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34005, 0.125, 3.65, 11.4)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 0.0, 3.65, 11.1)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(64005, 0.0, 3.525, 11.4)
    ops.element('elasticBeamColumn', 64005, 64005, 4005, 99999, 77777)
    ops.node(44005, 0.0, 3.775, 11.4)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304005, 26423.2795)
    ops.uniaxialMaterial('Elastic', 404005, 51790.87965)
    ops.section('Aggregator', 14005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404005, 'My', 304005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14005, 4005, 14005, 14005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4006, 2.95, 3.65, 11.4, '-mass', 11.934789415754548, 11.934789415754548, 11.934789415754548, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 2.775, 3.65, 11.4)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(34006, 3.125, 3.65, 11.4)
    ops.element('elasticBeamColumn', 34006, 4006, 34006, 99999, 88888)
    ops.node(24006, 2.95, 3.65, 11.1)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(64006, 2.95, 3.475, 11.4)
    ops.element('elasticBeamColumn', 64006, 64006, 4006, 99999, 77777)
    ops.node(44006, 2.95, 3.825, 11.4)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304006, 49797.90105)
    ops.uniaxialMaterial('Elastic', 404006, 104986.19455)
    ops.section('Aggregator', 14006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404006, 'My', 304006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14006, 4006, 14006, 14006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4007, 9.6, 3.65, 11.4, '-mass', 15.588213184414391, 15.588213184414391, 15.588213184414391, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54007, 9.425, 3.65, 11.4)
    ops.element('elasticBeamColumn', 54007, 54007, 4007, 99999, 88888)
    ops.node(34007, 9.775, 3.65, 11.4)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 9.6, 3.65, 11.1)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 9.6, 3.475, 11.4)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 9.6, 3.825, 11.4)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304007, 56322.9866)
    ops.uniaxialMaterial('Elastic', 404007, 117988.66095)
    ops.section('Aggregator', 14007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404007, 'My', 304007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14007, 4007, 14007, 14007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4008, 16.25, 3.65, 11.4, '-mass', 8.066354298629214, 8.066354298629214, 8.066354298629214, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 16.125, 3.65, 11.4)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(24008, 16.25, 3.65, 11.1)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 16.25, 3.525, 11.4)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 16.25, 3.775, 11.4)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304008, 34633.63495)
    ops.uniaxialMaterial('Elastic', 404008, 66700.1067)
    ops.section('Aggregator', 14008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404008, 'My', 304008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14008, 4008, 14008, 14008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4009, 0.0, 7.3, 11.4, '-mass', 3.855435473802148, 3.855435473802148, 3.855435473802148, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34009, 0.125, 7.3, 11.4)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 0.0, 7.3, 11.1)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 0.0, 7.175, 11.4)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 0.0, 7.425, 11.4)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304009, 24911.5522)
    ops.uniaxialMaterial('Elastic', 404009, 49052.0069)
    ops.section('Aggregator', 14009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404009, 'My', 304009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14009, 4009, 14009, 14009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4010, 2.95, 7.3, 11.4, '-mass', 11.377294359587324, 11.377294359587324, 11.377294359587324, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 2.775, 7.3, 11.4)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 3.125, 7.3, 11.4)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 2.95, 7.3, 11.1)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 2.95, 7.125, 11.4)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 2.95, 7.475, 11.4)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304010, 48721.27265)
    ops.uniaxialMaterial('Elastic', 404010, 102842.09545)
    ops.section('Aggregator', 14010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404010, 'My', 304010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14010, 4010, 14010, 14010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4011, 9.6, 7.3, 11.4, '-mass', 15.588213184414391, 15.588213184414391, 15.588213184414391, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 9.425, 7.3, 11.4)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 9.775, 7.3, 11.4)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 9.6, 7.3, 11.1)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 9.6, 7.125, 11.4)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 9.6, 7.475, 11.4)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304011, 56322.9866)
    ops.uniaxialMaterial('Elastic', 404011, 117988.66095)
    ops.section('Aggregator', 14011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404011, 'My', 304011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14011, 4011, 14011, 14011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4012, 16.25, 7.3, 11.4, '-mass', 8.066354298629214, 8.066354298629214, 8.066354298629214, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 16.125, 7.3, 11.4)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 16.25, 7.3, 11.1)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 16.25, 7.175, 11.4)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 16.25, 7.425, 11.4)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304012, 34633.63495)
    ops.uniaxialMaterial('Elastic', 404012, 66700.1067)
    ops.section('Aggregator', 14012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404012, 'My', 304012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14012, 4012, 14012, 14012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    # Central joint node
    ops.node(4013, 0.0, 10.95, 11.4, '-mass', 3.855435473802148, 3.855435473802148, 3.855435473802148, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.125, 10.95, 11.4)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 10.95, 11.1)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 10.825, 11.4)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    ops.node(44013, 0.0, 11.075, 11.4)
    ops.element('elasticBeamColumn', 44013, 4013, 44013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304013, 24911.5522)
    ops.uniaxialMaterial('Elastic', 404013, 49052.0069)
    ops.section('Aggregator', 14013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404013, 'My', 304013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14013, 4013, 14013, 14013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    # Central joint node
    ops.node(4014, 2.95, 10.95, 11.4, '-mass', 11.377294359587324, 11.377294359587324, 11.377294359587324, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 2.775, 10.95, 11.4)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 3.125, 10.95, 11.4)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 2.95, 10.95, 11.1)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 2.95, 10.775, 11.4)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    ops.node(44014, 2.95, 11.125, 11.4)
    ops.element('elasticBeamColumn', 44014, 4014, 44014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304014, 48721.27265)
    ops.uniaxialMaterial('Elastic', 404014, 102842.09545)
    ops.section('Aggregator', 14014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404014, 'My', 304014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14014, 4014, 14014, 14014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    # Central joint node
    ops.node(4015, 9.6, 10.95, 11.4, '-mass', 15.588213184414391, 15.588213184414391, 15.588213184414391, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 9.425, 10.95, 11.4)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 9.775, 10.95, 11.4)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 9.6, 10.95, 11.1)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 9.6, 10.775, 11.4)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    ops.node(44015, 9.6, 11.125, 11.4)
    ops.element('elasticBeamColumn', 44015, 4015, 44015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304015, 56322.9866)
    ops.uniaxialMaterial('Elastic', 404015, 117988.66095)
    ops.section('Aggregator', 14015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404015, 'My', 304015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14015, 4015, 14015, 14015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    # Central joint node
    ops.node(4016, 16.25, 10.95, 11.4, '-mass', 8.066354298629214, 8.066354298629214, 8.066354298629214, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 16.125, 10.95, 11.4)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(24016, 16.25, 10.95, 11.1)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 16.25, 10.825, 11.4)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    ops.node(44016, 16.25, 11.075, 11.4)
    ops.element('elasticBeamColumn', 44016, 4016, 44016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304016, 34633.63495)
    ops.uniaxialMaterial('Elastic', 404016, 66700.1067)
    ops.section('Aggregator', 14016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404016, 'My', 304016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14016, 4016, 14016, 14016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 4)
    # Central joint node
    ops.node(4017, 0.0, 14.6, 11.4, '-mass', 3.8554354738021486, 3.8554354738021486, 3.8554354738021486, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34017, 0.125, 14.6, 11.4)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 0.0, 14.6, 11.1)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(64017, 0.0, 14.475, 11.4)
    ops.element('elasticBeamColumn', 64017, 64017, 4017, 99999, 77777)
    ops.node(44017, 0.0, 14.725, 11.4)
    ops.element('elasticBeamColumn', 44017, 4017, 44017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304017, 24911.5522)
    ops.uniaxialMaterial('Elastic', 404017, 49052.0069)
    ops.section('Aggregator', 14017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404017, 'My', 304017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14017, 4017, 14017, 14017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 4)
    # Central joint node
    ops.node(4018, 2.95, 14.6, 11.4, '-mass', 11.377294359587324, 11.377294359587324, 11.377294359587324, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 2.775, 14.6, 11.4)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(34018, 3.125, 14.6, 11.4)
    ops.element('elasticBeamColumn', 34018, 4018, 34018, 99999, 88888)
    ops.node(24018, 2.95, 14.6, 11.1)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(64018, 2.95, 14.425, 11.4)
    ops.element('elasticBeamColumn', 64018, 64018, 4018, 99999, 77777)
    ops.node(44018, 2.95, 14.775, 11.4)
    ops.element('elasticBeamColumn', 44018, 4018, 44018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304018, 48721.27265)
    ops.uniaxialMaterial('Elastic', 404018, 102842.09545)
    ops.section('Aggregator', 14018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404018, 'My', 304018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14018, 4018, 14018, 14018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 4)
    # Central joint node
    ops.node(4019, 9.6, 14.6, 11.4, '-mass', 15.588213184414391, 15.588213184414391, 15.588213184414391, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54019, 9.425, 14.6, 11.4)
    ops.element('elasticBeamColumn', 54019, 54019, 4019, 99999, 88888)
    ops.node(34019, 9.775, 14.6, 11.4)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 9.6, 14.6, 11.1)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(64019, 9.6, 14.425, 11.4)
    ops.element('elasticBeamColumn', 64019, 64019, 4019, 99999, 77777)
    ops.node(44019, 9.6, 14.775, 11.4)
    ops.element('elasticBeamColumn', 44019, 4019, 44019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304019, 56322.9866)
    ops.uniaxialMaterial('Elastic', 404019, 117988.66095)
    ops.section('Aggregator', 14019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404019, 'My', 304019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14019, 4019, 14019, 14019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 4)
    # Central joint node
    ops.node(4020, 16.25, 14.6, 11.4, '-mass', 8.066354298629214, 8.066354298629214, 8.066354298629214, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 16.125, 14.6, 11.4)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(24020, 16.25, 14.6, 11.1)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(64020, 16.25, 14.475, 11.4)
    ops.element('elasticBeamColumn', 64020, 64020, 4020, 99999, 77777)
    ops.node(44020, 16.25, 14.725, 11.4)
    ops.element('elasticBeamColumn', 44020, 4020, 44020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304020, 34633.63495)
    ops.uniaxialMaterial('Elastic', 404020, 66700.1067)
    ops.section('Aggregator', 14020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404020, 'My', 304020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14020, 4020, 14020, 14020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 4)
    # Central joint node
    ops.node(4021, 0.0, 18.25, 11.4, '-mass', 3.8554354738021477, 3.8554354738021477, 3.8554354738021477, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34021, 0.125, 18.25, 11.4)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 0.0, 18.25, 11.1)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(64021, 0.0, 18.125, 11.4)
    ops.element('elasticBeamColumn', 64021, 64021, 4021, 99999, 77777)
    ops.node(44021, 0.0, 18.375, 11.4)
    ops.element('elasticBeamColumn', 44021, 4021, 44021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304021, 24911.5522)
    ops.uniaxialMaterial('Elastic', 404021, 49052.0069)
    ops.section('Aggregator', 14021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404021, 'My', 304021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14021, 4021, 14021, 14021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 4)
    # Central joint node
    ops.node(4022, 2.95, 18.25, 11.4, '-mass', 11.377294359587323, 11.377294359587323, 11.377294359587323, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 2.775, 18.25, 11.4)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(34022, 3.125, 18.25, 11.4)
    ops.element('elasticBeamColumn', 34022, 4022, 34022, 99999, 88888)
    ops.node(24022, 2.95, 18.25, 11.1)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(64022, 2.95, 18.075, 11.4)
    ops.element('elasticBeamColumn', 64022, 64022, 4022, 99999, 77777)
    ops.node(44022, 2.95, 18.425, 11.4)
    ops.element('elasticBeamColumn', 44022, 4022, 44022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304022, 48721.27265)
    ops.uniaxialMaterial('Elastic', 404022, 102842.09545)
    ops.section('Aggregator', 14022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404022, 'My', 304022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14022, 4022, 14022, 14022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 4)
    # Central joint node
    ops.node(4023, 9.6, 18.25, 11.4, '-mass', 15.58821318441439, 15.58821318441439, 15.58821318441439, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54023, 9.425, 18.25, 11.4)
    ops.element('elasticBeamColumn', 54023, 54023, 4023, 99999, 88888)
    ops.node(34023, 9.775, 18.25, 11.4)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 9.6, 18.25, 11.1)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(64023, 9.6, 18.075, 11.4)
    ops.element('elasticBeamColumn', 64023, 64023, 4023, 99999, 77777)
    ops.node(44023, 9.6, 18.425, 11.4)
    ops.element('elasticBeamColumn', 44023, 4023, 44023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304023, 56322.9866)
    ops.uniaxialMaterial('Elastic', 404023, 117988.66095)
    ops.section('Aggregator', 14023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404023, 'My', 304023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14023, 4023, 14023, 14023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 4)
    # Central joint node
    ops.node(4024, 16.25, 18.25, 11.4, '-mass', 8.066354298629214, 8.066354298629214, 8.066354298629214, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 16.125, 18.25, 11.4)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 16.25, 18.25, 11.1)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(64024, 16.25, 18.125, 11.4)
    ops.element('elasticBeamColumn', 64024, 64024, 4024, 99999, 77777)
    ops.node(44024, 16.25, 18.375, 11.4)
    ops.element('elasticBeamColumn', 44024, 4024, 44024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304024, 34633.63495)
    ops.uniaxialMaterial('Elastic', 404024, 66700.1067)
    ops.section('Aggregator', 14024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404024, 'My', 304024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14024, 4024, 14024, 14024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 6, 4)
    # Central joint node
    ops.node(4025, 0.0, 21.9, 11.4, '-mass', 2.1629623852191164, 2.1629623852191164, 2.1629623852191164, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34025, 0.125, 21.9, 11.4)
    ops.element('elasticBeamColumn', 34025, 4025, 34025, 99999, 88888)
    ops.node(24025, 0.0, 21.9, 11.15)
    ops.element('elasticBeamColumn', 24025, 24025, 4025, 99999, 99999)
    ops.node(64025, 0.0, 21.775, 11.4)
    ops.element('elasticBeamColumn', 64025, 64025, 4025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304025, 17586.82845)
    ops.uniaxialMaterial('Elastic', 404025, 31590.4668)
    ops.section('Aggregator', 14025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404025, 'My', 304025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14025, 4025, 14025, 14025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 6, 4)
    # Central joint node
    ops.node(4026, 2.95, 21.9, 11.4, '-mass', 6.104014152270726, 6.104014152270726, 6.104014152270726, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54026, 2.825, 21.9, 11.4)
    ops.element('elasticBeamColumn', 54026, 54026, 4026, 99999, 88888)
    ops.node(34026, 3.075, 21.9, 11.4)
    ops.element('elasticBeamColumn', 34026, 4026, 34026, 99999, 88888)
    ops.node(24026, 2.95, 21.9, 11.15)
    ops.element('elasticBeamColumn', 24026, 24026, 4026, 99999, 99999)
    ops.node(64026, 2.95, 21.775, 11.4)
    ops.element('elasticBeamColumn', 64026, 64026, 4026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304026, 27644.52285)
    ops.uniaxialMaterial('Elastic', 404026, 48238.5208)
    ops.section('Aggregator', 14026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404026, 'My', 304026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14026, 4026, 14026, 14026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 6, 4)
    # Central joint node
    ops.node(4027, 9.6, 21.9, 11.4, '-mass', 8.577057662543584, 8.577057662543584, 8.577057662543584, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54027, 9.425, 21.9, 11.4)
    ops.element('elasticBeamColumn', 54027, 54027, 4027, 99999, 88888)
    ops.node(34027, 9.775, 21.9, 11.4)
    ops.element('elasticBeamColumn', 34027, 4027, 34027, 99999, 88888)
    ops.node(24027, 9.6, 21.9, 11.15)
    ops.element('elasticBeamColumn', 24027, 24027, 4027, 99999, 99999)
    ops.node(64027, 9.6, 21.725, 11.4)
    ops.element('elasticBeamColumn', 64027, 64027, 4027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304027, 45594.3545)
    ops.uniaxialMaterial('Elastic', 404027, 78980.02575)
    ops.section('Aggregator', 14027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404027, 'My', 304027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14027, 4027, 14027, 14027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 6, 4)
    # Central joint node
    ops.node(4028, 16.25, 21.9, 11.4, '-mass', 4.426831583565371, 4.426831583565371, 4.426831583565371, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54028, 16.125, 21.9, 11.4)
    ops.element('elasticBeamColumn', 54028, 54028, 4028, 99999, 88888)
    ops.node(24028, 16.25, 21.9, 11.15)
    ops.element('elasticBeamColumn', 24028, 24028, 4028, 99999, 99999)
    ops.node(64028, 16.25, 21.775, 11.4)
    ops.element('elasticBeamColumn', 64028, 64028, 4028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304028, 23929.84025)
    ops.uniaxialMaterial('Elastic', 404028, 42077.7436)
    ops.section('Aggregator', 14028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404028, 'My', 304028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14028, 4028, 14028, 14028, '-orient', 0, 0, 1, 0, 1, 0)
