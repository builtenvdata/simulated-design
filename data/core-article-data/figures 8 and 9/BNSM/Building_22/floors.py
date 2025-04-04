import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 2.75)
    ops.node(11002, 5.9, 0.0, 2.75)
    ops.node(11003, 8.75, 0.0, 2.75)
    ops.node(11004, 14.65, 0.0, 2.75)
    ops.node(11005, 0.0, 4.15, 2.75)
    ops.node(11006, 5.9, 4.15, 2.75)
    ops.node(11007, 8.75, 4.15, 2.75)
    ops.node(11008, 14.65, 4.15, 2.75)
    ops.node(11009, 0.0, 8.3, 2.75)
    ops.node(11010, 5.9, 8.3, 2.75)
    ops.node(11011, 8.75, 8.3, 2.75)
    ops.node(11012, 14.65, 8.3, 2.75)
    # Retained floor node
    ops.node(91000, 7.325, 4.22966394, 2.75)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 5.5)
    ops.node(12002, 5.9, 0.0, 5.5)
    ops.node(12003, 8.75, 0.0, 5.5)
    ops.node(12004, 14.65, 0.0, 5.5)
    ops.node(12005, 0.0, 4.15, 5.5)
    ops.node(12006, 5.9, 4.15, 5.5)
    ops.node(12007, 8.75, 4.15, 5.5)
    ops.node(12008, 14.65, 4.15, 5.5)
    ops.node(12009, 0.0, 8.3, 5.5)
    ops.node(12010, 5.9, 8.3, 5.5)
    ops.node(12011, 8.75, 8.3, 5.5)
    ops.node(12012, 14.65, 8.3, 5.5)
    # Retained floor node
    ops.node(92000, 7.325, 4.22544151, 5.5)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 8.25)
    ops.node(13002, 5.9, 0.0, 8.25)
    ops.node(13003, 8.75, 0.0, 8.25)
    ops.node(13004, 14.65, 0.0, 8.25)
    ops.node(13005, 0.0, 4.15, 8.25)
    ops.node(13006, 5.9, 4.15, 8.25)
    ops.node(13007, 8.75, 4.15, 8.25)
    ops.node(13008, 14.65, 4.15, 8.25)
    ops.node(13009, 0.0, 8.3, 8.25)
    ops.node(13010, 5.9, 8.3, 8.25)
    ops.node(13011, 8.75, 8.3, 8.25)
    ops.node(13012, 14.65, 8.3, 8.25)
    # Retained floor node
    ops.node(93000, 7.325, 4.22090911, 8.25)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 11.0)
    ops.node(14002, 5.9, 0.0, 11.0)
    ops.node(14003, 8.75, 0.0, 11.0)
    ops.node(14004, 14.65, 0.0, 11.0)
    ops.node(14005, 0.0, 4.15, 11.0)
    ops.node(14006, 5.9, 4.15, 11.0)
    ops.node(14007, 8.75, 4.15, 11.0)
    ops.node(14008, 14.65, 4.15, 11.0)
    ops.node(14009, 0.0, 8.3, 11.0)
    ops.node(14010, 5.9, 8.3, 11.0)
    ops.node(14011, 8.75, 8.3, 11.0)
    ops.node(14012, 14.65, 8.3, 11.0)
    # Retained floor node
    ops.node(94000, 7.325, 4.28725945, 11.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
