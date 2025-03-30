import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 3.7)
    ops.node(11002, 2.95, 0.0, 3.7)
    ops.node(11003, 7.7, 0.0, 3.7)
    ops.node(11004, 12.45, 0.0, 3.7)
    ops.node(11005, 0.0, 5.15, 3.7)
    ops.node(11006, 2.95, 5.15, 3.7)
    ops.node(11007, 7.7, 5.15, 3.7)
    ops.node(11008, 12.45, 5.15, 3.7)
    ops.node(11009, 0.0, 10.3, 3.7)
    ops.node(11010, 2.95, 10.3, 3.7)
    ops.node(11011, 7.7, 10.3, 3.7)
    ops.node(11012, 12.45, 10.3, 3.7)
    ops.node(11013, 0.0, 15.45, 3.7)
    ops.node(11014, 2.95, 15.45, 3.7)
    ops.node(11015, 7.7, 15.45, 3.7)
    ops.node(11016, 12.45, 15.45, 3.7)
    ops.node(11017, 0.0, 20.6, 3.7)
    ops.node(11018, 2.95, 20.6, 3.7)
    ops.node(11019, 7.7, 20.6, 3.7)
    ops.node(11020, 12.45, 20.6, 3.7)
    ops.node(11021, 0.0, 25.75, 3.7)
    ops.node(11022, 2.95, 25.75, 3.7)
    ops.node(11023, 7.7, 25.75, 3.7)
    ops.node(11024, 12.45, 25.75, 3.7)
    ops.node(11025, 0.0, 30.9, 3.7)
    ops.node(11026, 2.95, 30.9, 3.7)
    ops.node(11027, 7.7, 30.9, 3.7)
    ops.node(11028, 12.45, 30.9, 3.7)
    # Retained floor node
    ops.node(91000, 6.39228195, 15.6897534, 3.7)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020, 11021, 11022, 11023, 11024, 11025, 11026, 11027, 11028)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 6.55)
    ops.node(12002, 2.95, 0.0, 6.55)
    ops.node(12003, 7.7, 0.0, 6.55)
    ops.node(12004, 12.45, 0.0, 6.55)
    ops.node(12005, 0.0, 5.15, 6.55)
    ops.node(12006, 2.95, 5.15, 6.55)
    ops.node(12007, 7.7, 5.15, 6.55)
    ops.node(12008, 12.45, 5.15, 6.55)
    ops.node(12009, 0.0, 10.3, 6.55)
    ops.node(12010, 2.95, 10.3, 6.55)
    ops.node(12011, 7.7, 10.3, 6.55)
    ops.node(12012, 12.45, 10.3, 6.55)
    ops.node(12013, 0.0, 15.45, 6.55)
    ops.node(12014, 2.95, 15.45, 6.55)
    ops.node(12015, 7.7, 15.45, 6.55)
    ops.node(12016, 12.45, 15.45, 6.55)
    ops.node(12017, 0.0, 20.6, 6.55)
    ops.node(12018, 2.95, 20.6, 6.55)
    ops.node(12019, 7.7, 20.6, 6.55)
    ops.node(12020, 12.45, 20.6, 6.55)
    ops.node(12021, 0.0, 25.75, 6.55)
    ops.node(12022, 2.95, 25.75, 6.55)
    ops.node(12023, 7.7, 25.75, 6.55)
    ops.node(12024, 12.45, 25.75, 6.55)
    ops.node(12025, 0.0, 30.9, 6.55)
    ops.node(12026, 2.95, 30.9, 6.55)
    ops.node(12027, 7.7, 30.9, 6.55)
    ops.node(12028, 12.45, 30.9, 6.55)
    # Retained floor node
    ops.node(92000, 6.39208183, 15.69342302, 6.55)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020, 12021, 12022, 12023, 12024, 12025, 12026, 12027, 12028)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 9.4)
    ops.node(13002, 2.95, 0.0, 9.4)
    ops.node(13003, 7.7, 0.0, 9.4)
    ops.node(13004, 12.45, 0.0, 9.4)
    ops.node(13005, 0.0, 5.15, 9.4)
    ops.node(13006, 2.95, 5.15, 9.4)
    ops.node(13007, 7.7, 5.15, 9.4)
    ops.node(13008, 12.45, 5.15, 9.4)
    ops.node(13009, 0.0, 10.3, 9.4)
    ops.node(13010, 2.95, 10.3, 9.4)
    ops.node(13011, 7.7, 10.3, 9.4)
    ops.node(13012, 12.45, 10.3, 9.4)
    ops.node(13013, 0.0, 15.45, 9.4)
    ops.node(13014, 2.95, 15.45, 9.4)
    ops.node(13015, 7.7, 15.45, 9.4)
    ops.node(13016, 12.45, 15.45, 9.4)
    ops.node(13017, 0.0, 20.6, 9.4)
    ops.node(13018, 2.95, 20.6, 9.4)
    ops.node(13019, 7.7, 20.6, 9.4)
    ops.node(13020, 12.45, 20.6, 9.4)
    ops.node(13021, 0.0, 25.75, 9.4)
    ops.node(13022, 2.95, 25.75, 9.4)
    ops.node(13023, 7.7, 25.75, 9.4)
    ops.node(13024, 12.45, 25.75, 9.4)
    ops.node(13025, 0.0, 30.9, 9.4)
    ops.node(13026, 2.95, 30.9, 9.4)
    ops.node(13027, 7.7, 30.9, 9.4)
    ops.node(13028, 12.45, 30.9, 9.4)
    # Retained floor node
    ops.node(93000, 6.39066649, 15.66833586, 9.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020, 13021, 13022, 13023, 13024, 13025, 13026, 13027, 13028)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 12.25)
    ops.node(14002, 2.95, 0.0, 12.25)
    ops.node(14003, 7.7, 0.0, 12.25)
    ops.node(14004, 12.45, 0.0, 12.25)
    ops.node(14005, 0.0, 5.15, 12.25)
    ops.node(14006, 2.95, 5.15, 12.25)
    ops.node(14007, 7.7, 5.15, 12.25)
    ops.node(14008, 12.45, 5.15, 12.25)
    ops.node(14009, 0.0, 10.3, 12.25)
    ops.node(14010, 2.95, 10.3, 12.25)
    ops.node(14011, 7.7, 10.3, 12.25)
    ops.node(14012, 12.45, 10.3, 12.25)
    ops.node(14013, 0.0, 15.45, 12.25)
    ops.node(14014, 2.95, 15.45, 12.25)
    ops.node(14015, 7.7, 15.45, 12.25)
    ops.node(14016, 12.45, 15.45, 12.25)
    ops.node(14017, 0.0, 20.6, 12.25)
    ops.node(14018, 2.95, 20.6, 12.25)
    ops.node(14019, 7.7, 20.6, 12.25)
    ops.node(14020, 12.45, 20.6, 12.25)
    ops.node(14021, 0.0, 25.75, 12.25)
    ops.node(14022, 2.95, 25.75, 12.25)
    ops.node(14023, 7.7, 25.75, 12.25)
    ops.node(14024, 12.45, 25.75, 12.25)
    ops.node(14025, 0.0, 30.9, 12.25)
    ops.node(14026, 2.95, 30.9, 12.25)
    ops.node(14027, 7.7, 30.9, 12.25)
    ops.node(14028, 12.45, 30.9, 12.25)
    # Retained floor node
    ops.node(94000, 6.45542918, 15.71186574, 12.25)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020, 14021, 14022, 14023, 14024, 14025, 14026, 14027, 14028)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
