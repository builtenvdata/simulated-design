import openseespy.opensees as ops


def add_foundations() -> None:
    """Add foundation components to ops domain (nodes and constraints).
    """
    # Foundation or support under the column 1
    # Fixed node
    ops.node(1, 0.0, 0.0, 0.0)
    ops.fix(1, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70001, 0.0, 0.0, 0.0, '-mass', 0.24464831804281348, 0.24464831804281348, 0.24464831804281348, 0.0, 0.0, 0.0)
    ops.equalDOF(1, 70001, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 7
    # Fixed node
    ops.node(7, 0.0, 3.5, 0.0)
    ops.fix(7, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70007, 0.0, 3.5, 0.0, '-mass', 0.3522935779816514, 0.3522935779816514, 0.3522935779816514, 0.0, 0.0, 0.0)
    ops.equalDOF(7, 70007, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 13
    # Fixed node
    ops.node(13, 0.0, 7.0, 0.0)
    ops.fix(13, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70013, 0.0, 7.0, 0.0, '-mass', 0.3522935779816514, 0.3522935779816514, 0.3522935779816514, 0.0, 0.0, 0.0)
    ops.equalDOF(13, 70013, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 19
    # Fixed node
    ops.node(19, 0.0, 10.5, 0.0)
    ops.fix(19, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70019, 0.0, 10.5, 0.0, '-mass', 0.24464831804281348, 0.24464831804281348, 0.24464831804281348, 0.0, 0.0, 0.0)
    ops.equalDOF(19, 70019, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 2
    # Fixed node
    ops.node(2, 7.4, 0.0, 0.0)
    ops.fix(2, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70002, 7.4, 0.0, 0.0, '-mass', 0.6262996941896026, 0.6262996941896026, 0.6262996941896026, 0.0, 0.0, 0.0)
    ops.equalDOF(2, 70002, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 8
    # Fixed node
    ops.node(8, 7.4, 3.5, 0.0)
    ops.fix(8, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70008, 7.4, 3.5, 0.0, '-mass', 0.7926605504587156, 0.7926605504587156, 0.7926605504587156, 0.0, 0.0, 0.0)
    ops.equalDOF(8, 70008, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 14
    # Fixed node
    ops.node(14, 7.4, 7.0, 0.0)
    ops.fix(14, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70014, 7.4, 7.0, 0.0, '-mass', 0.7926605504587156, 0.7926605504587156, 0.7926605504587156, 0.0, 0.0, 0.0)
    ops.equalDOF(14, 70014, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 20
    # Fixed node
    ops.node(20, 7.4, 10.5, 0.0)
    ops.fix(20, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70020, 7.4, 10.5, 0.0, '-mass', 0.6262996941896026, 0.6262996941896026, 0.6262996941896026, 0.0, 0.0, 0.0)
    ops.equalDOF(20, 70020, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4063
    # Fixed node
    ops.node(3, 14.8, 0.0, 0.0)
    ops.fix(3, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70003, 14.8, 0.0, 0.0, '-mass', 0.1761467889908257, 0.1761467889908257, 0.1761467889908257, 0.0, 0.0, 0.0)
    ops.equalDOF(3, 70003, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 9
    # Fixed node
    ops.node(9, 14.8, 3.5, 0.0)
    ops.fix(9, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70009, 14.8, 3.5, 0.0, '-mass', 0.6262996941896026, 0.6262996941896026, 0.6262996941896026, 0.0, 0.0, 0.0)
    ops.equalDOF(9, 70009, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 15
    # Fixed node
    ops.node(15, 14.8, 7.0, 0.0)
    ops.fix(15, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70015, 14.8, 7.0, 0.0, '-mass', 0.4795107033639143, 0.4795107033639143, 0.4795107033639143, 0.0, 0.0, 0.0)
    ops.equalDOF(15, 70015, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 21
    # Fixed node
    ops.node(21, 14.8, 10.5, 0.0)
    ops.fix(21, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70021, 14.8, 10.5, 0.0, '-mass', 0.3522935779816514, 0.3522935779816514, 0.3522935779816514, 0.0, 0.0, 0.0)
    ops.equalDOF(21, 70021, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4065
    # Fixed node
    ops.node(4, 17.8, 0.0, 0.0)
    ops.fix(4, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70004, 17.8, 0.0, 0.0, '-mass', 0.1761467889908257, 0.1761467889908257, 0.1761467889908257, 0.0, 0.0, 0.0)
    ops.equalDOF(4, 70004, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 10
    # Fixed node
    ops.node(10, 17.8, 3.5, 0.0)
    ops.fix(10, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70010, 17.8, 3.5, 0.0, '-mass', 0.6262996941896026, 0.6262996941896026, 0.6262996941896026, 0.0, 0.0, 0.0)
    ops.equalDOF(10, 70010, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 16
    # Fixed node
    ops.node(16, 17.8, 7.0, 0.0)
    ops.fix(16, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70016, 17.8, 7.0, 0.0, '-mass', 0.4795107033639143, 0.4795107033639143, 0.4795107033639143, 0.0, 0.0, 0.0)
    ops.equalDOF(16, 70016, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 22
    # Fixed node
    ops.node(22, 17.8, 10.5, 0.0)
    ops.fix(22, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70022, 17.8, 10.5, 0.0, '-mass', 0.3522935779816514, 0.3522935779816514, 0.3522935779816514, 0.0, 0.0, 0.0)
    ops.equalDOF(22, 70022, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 5
    # Fixed node
    ops.node(5, 25.2, 0.0, 0.0)
    ops.fix(5, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70005, 25.2, 0.0, 0.0, '-mass', 0.6262996941896026, 0.6262996941896026, 0.6262996941896026, 0.0, 0.0, 0.0)
    ops.equalDOF(5, 70005, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 11
    # Fixed node
    ops.node(11, 25.2, 3.5, 0.0)
    ops.fix(11, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70011, 25.2, 3.5, 0.0, '-mass', 0.7926605504587156, 0.7926605504587156, 0.7926605504587156, 0.0, 0.0, 0.0)
    ops.equalDOF(11, 70011, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 17
    # Fixed node
    ops.node(17, 25.2, 7.0, 0.0)
    ops.fix(17, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70017, 25.2, 7.0, 0.0, '-mass', 0.7926605504587156, 0.7926605504587156, 0.7926605504587156, 0.0, 0.0, 0.0)
    ops.equalDOF(17, 70017, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 23
    # Fixed node
    ops.node(23, 25.2, 10.5, 0.0)
    ops.fix(23, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70023, 25.2, 10.5, 0.0, '-mass', 0.6262996941896026, 0.6262996941896026, 0.6262996941896026, 0.0, 0.0, 0.0)
    ops.equalDOF(23, 70023, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 6
    # Fixed node
    ops.node(6, 32.6, 0.0, 0.0)
    ops.fix(6, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70006, 32.6, 0.0, 0.0, '-mass', 0.24464831804281348, 0.24464831804281348, 0.24464831804281348, 0.0, 0.0, 0.0)
    ops.equalDOF(6, 70006, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 12
    # Fixed node
    ops.node(12, 32.6, 3.5, 0.0)
    ops.fix(12, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70012, 32.6, 3.5, 0.0, '-mass', 0.3522935779816514, 0.3522935779816514, 0.3522935779816514, 0.0, 0.0, 0.0)
    ops.equalDOF(12, 70012, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 18
    # Fixed node
    ops.node(18, 32.6, 7.0, 0.0)
    ops.fix(18, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70018, 32.6, 7.0, 0.0, '-mass', 0.3522935779816514, 0.3522935779816514, 0.3522935779816514, 0.0, 0.0, 0.0)
    ops.equalDOF(18, 70018, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 24
    # Fixed node
    ops.node(24, 32.6, 10.5, 0.0)
    ops.fix(24, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70024, 32.6, 10.5, 0.0, '-mass', 0.24464831804281348, 0.24464831804281348, 0.24464831804281348, 0.0, 0.0, 0.0)
    ops.equalDOF(24, 70024, 1, 2, 3, 4, 5, 6)
