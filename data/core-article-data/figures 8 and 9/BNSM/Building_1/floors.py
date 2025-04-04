import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 2.85)
    ops.node(11002, 2.95, 0.0, 2.85)
    ops.node(11003, 9.6, 0.0, 2.85)
    ops.node(11004, 16.25, 0.0, 2.85)
    ops.node(11005, 0.0, 3.65, 2.85)
    ops.node(11006, 2.95, 3.65, 2.85)
    ops.node(11007, 9.6, 3.65, 2.85)
    ops.node(11008, 16.25, 3.65, 2.85)
    ops.node(11009, 0.0, 7.3, 2.85)
    ops.node(11010, 2.95, 7.3, 2.85)
    ops.node(11011, 9.6, 7.3, 2.85)
    ops.node(11012, 16.25, 7.3, 2.85)
    ops.node(11013, 0.0, 10.95, 2.85)
    ops.node(11014, 2.95, 10.95, 2.85)
    ops.node(11015, 9.6, 10.95, 2.85)
    ops.node(11016, 16.25, 10.95, 2.85)
    ops.node(11017, 0.0, 14.6, 2.85)
    ops.node(11018, 2.95, 14.6, 2.85)
    ops.node(11019, 9.6, 14.6, 2.85)
    ops.node(11020, 16.25, 14.6, 2.85)
    ops.node(11021, 0.0, 18.25, 2.85)
    ops.node(11022, 2.95, 18.25, 2.85)
    ops.node(11023, 9.6, 18.25, 2.85)
    ops.node(11024, 16.25, 18.25, 2.85)
    ops.node(11025, 0.0, 21.9, 2.85)
    ops.node(11026, 2.95, 21.9, 2.85)
    ops.node(11027, 9.6, 21.9, 2.85)
    ops.node(11028, 16.25, 21.9, 2.85)
    # Retained floor node
    ops.node(91000, 8.11569605, 11.03757188, 2.85)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020, 11021, 11022, 11023, 11024, 11025, 11026, 11027, 11028)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 5.7)
    ops.node(12002, 2.95, 0.0, 5.7)
    ops.node(12003, 9.6, 0.0, 5.7)
    ops.node(12004, 16.25, 0.0, 5.7)
    ops.node(12005, 0.0, 3.65, 5.7)
    ops.node(12006, 2.95, 3.65, 5.7)
    ops.node(12007, 9.6, 3.65, 5.7)
    ops.node(12008, 16.25, 3.65, 5.7)
    ops.node(12009, 0.0, 7.3, 5.7)
    ops.node(12010, 2.95, 7.3, 5.7)
    ops.node(12011, 9.6, 7.3, 5.7)
    ops.node(12012, 16.25, 7.3, 5.7)
    ops.node(12013, 0.0, 10.95, 5.7)
    ops.node(12014, 2.95, 10.95, 5.7)
    ops.node(12015, 9.6, 10.95, 5.7)
    ops.node(12016, 16.25, 10.95, 5.7)
    ops.node(12017, 0.0, 14.6, 5.7)
    ops.node(12018, 2.95, 14.6, 5.7)
    ops.node(12019, 9.6, 14.6, 5.7)
    ops.node(12020, 16.25, 14.6, 5.7)
    ops.node(12021, 0.0, 18.25, 5.7)
    ops.node(12022, 2.95, 18.25, 5.7)
    ops.node(12023, 9.6, 18.25, 5.7)
    ops.node(12024, 16.25, 18.25, 5.7)
    ops.node(12025, 0.0, 21.9, 5.7)
    ops.node(12026, 2.95, 21.9, 5.7)
    ops.node(12027, 9.6, 21.9, 5.7)
    ops.node(12028, 16.25, 21.9, 5.7)
    # Retained floor node
    ops.node(92000, 8.07477568, 11.03579579, 5.7)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020, 12021, 12022, 12023, 12024, 12025, 12026, 12027, 12028)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 8.55)
    ops.node(13002, 2.95, 0.0, 8.55)
    ops.node(13003, 9.6, 0.0, 8.55)
    ops.node(13004, 16.25, 0.0, 8.55)
    ops.node(13005, 0.0, 3.65, 8.55)
    ops.node(13006, 2.95, 3.65, 8.55)
    ops.node(13007, 9.6, 3.65, 8.55)
    ops.node(13008, 16.25, 3.65, 8.55)
    ops.node(13009, 0.0, 7.3, 8.55)
    ops.node(13010, 2.95, 7.3, 8.55)
    ops.node(13011, 9.6, 7.3, 8.55)
    ops.node(13012, 16.25, 7.3, 8.55)
    ops.node(13013, 0.0, 10.95, 8.55)
    ops.node(13014, 2.95, 10.95, 8.55)
    ops.node(13015, 9.6, 10.95, 8.55)
    ops.node(13016, 16.25, 10.95, 8.55)
    ops.node(13017, 0.0, 14.6, 8.55)
    ops.node(13018, 2.95, 14.6, 8.55)
    ops.node(13019, 9.6, 14.6, 8.55)
    ops.node(13020, 16.25, 14.6, 8.55)
    ops.node(13021, 0.0, 18.25, 8.55)
    ops.node(13022, 2.95, 18.25, 8.55)
    ops.node(13023, 9.6, 18.25, 8.55)
    ops.node(13024, 16.25, 18.25, 8.55)
    ops.node(13025, 0.0, 21.9, 8.55)
    ops.node(13026, 2.95, 21.9, 8.55)
    ops.node(13027, 9.6, 21.9, 8.55)
    ops.node(13028, 16.25, 21.9, 8.55)
    # Retained floor node
    ops.node(93000, 8.0865209, 11.03435305, 8.55)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020, 13021, 13022, 13023, 13024, 13025, 13026, 13027, 13028)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 11.4)
    ops.node(14002, 2.95, 0.0, 11.4)
    ops.node(14003, 9.6, 0.0, 11.4)
    ops.node(14004, 16.25, 0.0, 11.4)
    ops.node(14005, 0.0, 3.65, 11.4)
    ops.node(14006, 2.95, 3.65, 11.4)
    ops.node(14007, 9.6, 3.65, 11.4)
    ops.node(14008, 16.25, 3.65, 11.4)
    ops.node(14009, 0.0, 7.3, 11.4)
    ops.node(14010, 2.95, 7.3, 11.4)
    ops.node(14011, 9.6, 7.3, 11.4)
    ops.node(14012, 16.25, 7.3, 11.4)
    ops.node(14013, 0.0, 10.95, 11.4)
    ops.node(14014, 2.95, 10.95, 11.4)
    ops.node(14015, 9.6, 10.95, 11.4)
    ops.node(14016, 16.25, 10.95, 11.4)
    ops.node(14017, 0.0, 14.6, 11.4)
    ops.node(14018, 2.95, 14.6, 11.4)
    ops.node(14019, 9.6, 14.6, 11.4)
    ops.node(14020, 16.25, 14.6, 11.4)
    ops.node(14021, 0.0, 18.25, 11.4)
    ops.node(14022, 2.95, 18.25, 11.4)
    ops.node(14023, 9.6, 18.25, 11.4)
    ops.node(14024, 16.25, 18.25, 11.4)
    ops.node(14025, 0.0, 21.9, 11.4)
    ops.node(14026, 2.95, 21.9, 11.4)
    ops.node(14027, 9.6, 21.9, 11.4)
    ops.node(14028, 16.25, 21.9, 11.4)
    # Retained floor node
    ops.node(94000, 8.12882028, 11.03961875, 11.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020, 14021, 14022, 14023, 14024, 14025, 14026, 14027, 14028)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
