import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 2.95)
    ops.node(11002, 3.85, 0.0, 2.95)
    ops.node(11003, 7.7, 0.0, 2.95)
    ops.node(11004, 11.55, 0.0, 2.95)
    ops.node(11005, 14.6, 0.0, 2.95)
    ops.node(11006, 18.45, 0.0, 2.95)
    ops.node(11007, 22.3, 0.0, 2.95)
    ops.node(11008, 26.15, 0.0, 2.95)
    ops.node(11009, 0.0, 4.8, 2.95)
    ops.node(11010, 3.85, 4.8, 2.95)
    ops.node(11011, 7.7, 4.8, 2.95)
    ops.node(11012, 11.55, 4.8, 2.95)
    ops.node(11013, 14.6, 4.8, 2.95)
    ops.node(11014, 18.45, 4.8, 2.95)
    ops.node(11015, 22.3, 4.8, 2.95)
    ops.node(11016, 26.15, 4.8, 2.95)
    ops.node(11017, 0.0, 9.6, 2.95)
    ops.node(11018, 3.85, 9.6, 2.95)
    ops.node(11019, 7.7, 9.6, 2.95)
    ops.node(11020, 11.55, 9.6, 2.95)
    ops.node(11021, 14.6, 9.6, 2.95)
    ops.node(11022, 18.45, 9.6, 2.95)
    ops.node(11023, 22.3, 9.6, 2.95)
    ops.node(11024, 26.15, 9.6, 2.95)
    ops.node(11025, 0.0, 14.4, 2.95)
    ops.node(11026, 3.85, 14.4, 2.95)
    ops.node(11027, 7.7, 14.4, 2.95)
    ops.node(11028, 11.55, 14.4, 2.95)
    ops.node(11029, 14.6, 14.4, 2.95)
    ops.node(11030, 18.45, 14.4, 2.95)
    ops.node(11031, 22.3, 14.4, 2.95)
    ops.node(11032, 26.15, 14.4, 2.95)
    # Retained floor node
    ops.node(91000, 13.075, 7.26864334, 2.95)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020, 11021, 11022, 11023, 11024, 11025, 11026, 11027, 11028, 11029, 11030, 11031, 11032)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 5.9)
    ops.node(12002, 3.85, 0.0, 5.9)
    ops.node(12003, 7.7, 0.0, 5.9)
    ops.node(12004, 11.55, 0.0, 5.9)
    ops.node(12005, 14.6, 0.0, 5.9)
    ops.node(12006, 18.45, 0.0, 5.9)
    ops.node(12007, 22.3, 0.0, 5.9)
    ops.node(12008, 26.15, 0.0, 5.9)
    ops.node(12009, 0.0, 4.8, 5.9)
    ops.node(12010, 3.85, 4.8, 5.9)
    ops.node(12011, 7.7, 4.8, 5.9)
    ops.node(12012, 11.55, 4.8, 5.9)
    ops.node(12013, 14.6, 4.8, 5.9)
    ops.node(12014, 18.45, 4.8, 5.9)
    ops.node(12015, 22.3, 4.8, 5.9)
    ops.node(12016, 26.15, 4.8, 5.9)
    ops.node(12017, 0.0, 9.6, 5.9)
    ops.node(12018, 3.85, 9.6, 5.9)
    ops.node(12019, 7.7, 9.6, 5.9)
    ops.node(12020, 11.55, 9.6, 5.9)
    ops.node(12021, 14.6, 9.6, 5.9)
    ops.node(12022, 18.45, 9.6, 5.9)
    ops.node(12023, 22.3, 9.6, 5.9)
    ops.node(12024, 26.15, 9.6, 5.9)
    ops.node(12025, 0.0, 14.4, 5.9)
    ops.node(12026, 3.85, 14.4, 5.9)
    ops.node(12027, 7.7, 14.4, 5.9)
    ops.node(12028, 11.55, 14.4, 5.9)
    ops.node(12029, 14.6, 14.4, 5.9)
    ops.node(12030, 18.45, 14.4, 5.9)
    ops.node(12031, 22.3, 14.4, 5.9)
    ops.node(12032, 26.15, 14.4, 5.9)
    # Retained floor node
    ops.node(92000, 13.075, 7.26191095, 5.9)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020, 12021, 12022, 12023, 12024, 12025, 12026, 12027, 12028, 12029, 12030, 12031, 12032)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 8.85)
    ops.node(13002, 3.85, 0.0, 8.85)
    ops.node(13003, 7.7, 0.0, 8.85)
    ops.node(13004, 11.55, 0.0, 8.85)
    ops.node(13005, 14.6, 0.0, 8.85)
    ops.node(13006, 18.45, 0.0, 8.85)
    ops.node(13007, 22.3, 0.0, 8.85)
    ops.node(13008, 26.15, 0.0, 8.85)
    ops.node(13009, 0.0, 4.8, 8.85)
    ops.node(13010, 3.85, 4.8, 8.85)
    ops.node(13011, 7.7, 4.8, 8.85)
    ops.node(13012, 11.55, 4.8, 8.85)
    ops.node(13013, 14.6, 4.8, 8.85)
    ops.node(13014, 18.45, 4.8, 8.85)
    ops.node(13015, 22.3, 4.8, 8.85)
    ops.node(13016, 26.15, 4.8, 8.85)
    ops.node(13017, 0.0, 9.6, 8.85)
    ops.node(13018, 3.85, 9.6, 8.85)
    ops.node(13019, 7.7, 9.6, 8.85)
    ops.node(13020, 11.55, 9.6, 8.85)
    ops.node(13021, 14.6, 9.6, 8.85)
    ops.node(13022, 18.45, 9.6, 8.85)
    ops.node(13023, 22.3, 9.6, 8.85)
    ops.node(13024, 26.15, 9.6, 8.85)
    ops.node(13025, 0.0, 14.4, 8.85)
    ops.node(13026, 3.85, 14.4, 8.85)
    ops.node(13027, 7.7, 14.4, 8.85)
    ops.node(13028, 11.55, 14.4, 8.85)
    ops.node(13029, 14.6, 14.4, 8.85)
    ops.node(13030, 18.45, 14.4, 8.85)
    ops.node(13031, 22.3, 14.4, 8.85)
    ops.node(13032, 26.15, 14.4, 8.85)
    # Retained floor node
    ops.node(93000, 13.075, 7.26575848, 8.85)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020, 13021, 13022, 13023, 13024, 13025, 13026, 13027, 13028, 13029, 13030, 13031, 13032)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 11.8)
    ops.node(14002, 3.85, 0.0, 11.8)
    ops.node(14003, 7.7, 0.0, 11.8)
    ops.node(14004, 11.55, 0.0, 11.8)
    ops.node(14005, 14.6, 0.0, 11.8)
    ops.node(14006, 18.45, 0.0, 11.8)
    ops.node(14007, 22.3, 0.0, 11.8)
    ops.node(14008, 26.15, 0.0, 11.8)
    ops.node(14009, 0.0, 4.8, 11.8)
    ops.node(14010, 3.85, 4.8, 11.8)
    ops.node(14011, 7.7, 4.8, 11.8)
    ops.node(14012, 11.55, 4.8, 11.8)
    ops.node(14013, 14.6, 4.8, 11.8)
    ops.node(14014, 18.45, 4.8, 11.8)
    ops.node(14015, 22.3, 4.8, 11.8)
    ops.node(14016, 26.15, 4.8, 11.8)
    ops.node(14017, 0.0, 9.6, 11.8)
    ops.node(14018, 3.85, 9.6, 11.8)
    ops.node(14019, 7.7, 9.6, 11.8)
    ops.node(14020, 11.55, 9.6, 11.8)
    ops.node(14021, 14.6, 9.6, 11.8)
    ops.node(14022, 18.45, 9.6, 11.8)
    ops.node(14023, 22.3, 9.6, 11.8)
    ops.node(14024, 26.15, 9.6, 11.8)
    ops.node(14025, 0.0, 14.4, 11.8)
    ops.node(14026, 3.85, 14.4, 11.8)
    ops.node(14027, 7.7, 14.4, 11.8)
    ops.node(14028, 11.55, 14.4, 11.8)
    ops.node(14029, 14.6, 14.4, 11.8)
    ops.node(14030, 18.45, 14.4, 11.8)
    ops.node(14031, 22.3, 14.4, 11.8)
    ops.node(14032, 26.15, 14.4, 11.8)
    # Retained floor node
    ops.node(94000, 13.075, 7.31087835, 11.8)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020, 14021, 14022, 14023, 14024, 14025, 14026, 14027, 14028, 14029, 14030, 14031, 14032)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
