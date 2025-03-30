import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 3.1)
    ops.node(11002, 4.5, 0.0, 3.1)
    ops.node(11003, 9.0, 0.0, 3.1)
    ops.node(11004, 12.0, 0.0, 3.1)
    ops.node(11005, 16.5, 0.0, 3.1)
    ops.node(11006, 21.0, 0.0, 3.1)
    ops.node(11007, 0.0, 4.5, 3.1)
    ops.node(11008, 4.5, 4.5, 3.1)
    ops.node(11009, 9.0, 4.5, 3.1)
    ops.node(11010, 12.0, 4.5, 3.1)
    ops.node(11011, 16.5, 4.5, 3.1)
    ops.node(11012, 21.0, 4.5, 3.1)
    ops.node(11013, 0.0, 9.0, 3.1)
    ops.node(11014, 4.5, 9.0, 3.1)
    ops.node(11015, 9.0, 9.0, 3.1)
    ops.node(11016, 12.0, 9.0, 3.1)
    ops.node(11017, 16.5, 9.0, 3.1)
    ops.node(11018, 21.0, 9.0, 3.1)
    ops.node(11019, 0.0, 13.5, 3.1)
    ops.node(11020, 4.5, 13.5, 3.1)
    ops.node(11021, 9.0, 13.5, 3.1)
    ops.node(11022, 12.0, 13.5, 3.1)
    ops.node(11023, 16.5, 13.5, 3.1)
    ops.node(11024, 21.0, 13.5, 3.1)
    # Retained floor node
    ops.node(91000, 10.4940523, 6.85957603, 3.1)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020, 11021, 11022, 11023, 11024)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 5.9)
    ops.node(12002, 4.5, 0.0, 5.9)
    ops.node(12003, 9.0, 0.0, 5.9)
    ops.node(12004, 12.0, 0.0, 5.9)
    ops.node(12005, 16.5, 0.0, 5.9)
    ops.node(12006, 21.0, 0.0, 5.9)
    ops.node(12007, 0.0, 4.5, 5.9)
    ops.node(12008, 4.5, 4.5, 5.9)
    ops.node(12009, 9.0, 4.5, 5.9)
    ops.node(12010, 12.0, 4.5, 5.9)
    ops.node(12011, 16.5, 4.5, 5.9)
    ops.node(12012, 21.0, 4.5, 5.9)
    ops.node(12013, 0.0, 9.0, 5.9)
    ops.node(12014, 4.5, 9.0, 5.9)
    ops.node(12015, 9.0, 9.0, 5.9)
    ops.node(12016, 12.0, 9.0, 5.9)
    ops.node(12017, 16.5, 9.0, 5.9)
    ops.node(12018, 21.0, 9.0, 5.9)
    ops.node(12019, 0.0, 13.5, 5.9)
    ops.node(12020, 4.5, 13.5, 5.9)
    ops.node(12021, 9.0, 13.5, 5.9)
    ops.node(12022, 12.0, 13.5, 5.9)
    ops.node(12023, 16.5, 13.5, 5.9)
    ops.node(12024, 21.0, 13.5, 5.9)
    # Retained floor node
    ops.node(92000, 10.51311144, 6.88334373, 5.9)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020, 12021, 12022, 12023, 12024)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 8.7)
    ops.node(13002, 4.5, 0.0, 8.7)
    ops.node(13003, 9.0, 0.0, 8.7)
    ops.node(13004, 12.0, 0.0, 8.7)
    ops.node(13005, 16.5, 0.0, 8.7)
    ops.node(13006, 21.0, 0.0, 8.7)
    ops.node(13007, 0.0, 4.5, 8.7)
    ops.node(13008, 4.5, 4.5, 8.7)
    ops.node(13009, 9.0, 4.5, 8.7)
    ops.node(13010, 12.0, 4.5, 8.7)
    ops.node(13011, 16.5, 4.5, 8.7)
    ops.node(13012, 21.0, 4.5, 8.7)
    ops.node(13013, 0.0, 9.0, 8.7)
    ops.node(13014, 4.5, 9.0, 8.7)
    ops.node(13015, 9.0, 9.0, 8.7)
    ops.node(13016, 12.0, 9.0, 8.7)
    ops.node(13017, 16.5, 9.0, 8.7)
    ops.node(13018, 21.0, 9.0, 8.7)
    ops.node(13019, 0.0, 13.5, 8.7)
    ops.node(13020, 4.5, 13.5, 8.7)
    ops.node(13021, 9.0, 13.5, 8.7)
    ops.node(13022, 12.0, 13.5, 8.7)
    ops.node(13023, 16.5, 13.5, 8.7)
    ops.node(13024, 21.0, 13.5, 8.7)
    # Retained floor node
    ops.node(93000, 10.5, 6.87763717, 8.7)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020, 13021, 13022, 13023, 13024)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 11.5)
    ops.node(14002, 4.5, 0.0, 11.5)
    ops.node(14003, 9.0, 0.0, 11.5)
    ops.node(14004, 12.0, 0.0, 11.5)
    ops.node(14005, 16.5, 0.0, 11.5)
    ops.node(14006, 21.0, 0.0, 11.5)
    ops.node(14007, 0.0, 4.5, 11.5)
    ops.node(14008, 4.5, 4.5, 11.5)
    ops.node(14009, 9.0, 4.5, 11.5)
    ops.node(14010, 12.0, 4.5, 11.5)
    ops.node(14011, 16.5, 4.5, 11.5)
    ops.node(14012, 21.0, 4.5, 11.5)
    ops.node(14013, 0.0, 9.0, 11.5)
    ops.node(14014, 4.5, 9.0, 11.5)
    ops.node(14015, 9.0, 9.0, 11.5)
    ops.node(14016, 12.0, 9.0, 11.5)
    ops.node(14017, 16.5, 9.0, 11.5)
    ops.node(14018, 21.0, 9.0, 11.5)
    ops.node(14019, 0.0, 13.5, 11.5)
    ops.node(14020, 4.5, 13.5, 11.5)
    ops.node(14021, 9.0, 13.5, 11.5)
    ops.node(14022, 12.0, 13.5, 11.5)
    ops.node(14023, 16.5, 13.5, 11.5)
    ops.node(14024, 21.0, 13.5, 11.5)
    # Retained floor node
    ops.node(94000, 10.5, 6.92415527, 11.5)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020, 14021, 14022, 14023, 14024)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
