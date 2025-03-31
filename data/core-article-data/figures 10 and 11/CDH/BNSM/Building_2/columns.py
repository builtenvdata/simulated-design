import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 28171992.66113896, 11738330.27547457, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 118.29629767, 0.00156094, 140.82316169, 0.03894662, 14.08231617, 0.11113362, -118.29629767, -0.00156094, -140.82316169, -0.03894662, -14.08231617, -0.11113362, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 118.29629767, 0.00156094, 140.82316169, 0.03894662, 14.08231617, 0.11113362, -118.29629767, -0.00156094, -140.82316169, -0.03894662, -14.08231617, -0.11113362, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.5, 0.0, 0.0)
    ops.node(121002, 4.5, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.1225, 30146450.7232196, 12561021.13467483, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 184.93801589, 0.00126809, 219.21925114, 0.03189484, 21.92192511, 0.1007394, -184.93801589, -0.00126809, -219.21925114, -0.03189484, -21.92192511, -0.1007394, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 184.93801589, 0.00126809, 219.21925114, 0.03189484, 21.92192511, 0.1007394, -184.93801589, -0.00126809, -219.21925114, -0.03189484, -21.92192511, -0.1007394, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.5, 0.0, 0.0)
    ops.node(121005, 16.5, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.1225, 28459127.10995806, 11857969.62914919, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 183.35035131, 0.00132604, 217.15820914, 0.03009381, 21.71582091, 0.08847113, -183.35035131, -0.00132604, -217.15820914, -0.03009381, -21.71582091, -0.08847113, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 183.35035131, 0.00132604, 217.15820914, 0.03009381, 21.71582091, 0.08847113, -183.35035131, -0.00132604, -217.15820914, -0.03009381, -21.71582091, -0.08847113, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 21.0, 0.0, 0.0)
    ops.node(121006, 21.0, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.09, 28128671.11286058, 11720279.63035857, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 119.32827079, 0.00149608, 142.04731813, 0.0386959, 14.20473181, 0.11058112, -119.32827079, -0.00149608, -142.04731813, -0.0386959, -14.20473181, -0.11058112, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 119.32827079, 0.00149608, 142.04731813, 0.0386959, 14.20473181, 0.11058112, -119.32827079, -0.00149608, -142.04731813, -0.0386959, -14.20473181, -0.11058112, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.5, 0.0)
    ops.node(121007, 0.0, 4.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 28014913.05918365, 11672880.44132652, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 181.11774594, 0.00125671, 214.39196907, 0.02690744, 21.43919691, 0.08239161, -181.11774594, -0.00125671, -214.39196907, -0.02690744, -21.43919691, -0.08239161, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 204.95051031, 0.00125671, 242.60319297, 0.02690744, 24.2603193, 0.08239161, -204.95051031, -0.00125671, -242.60319297, -0.02690744, -24.2603193, -0.08239161, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.5, 4.5, 0.0)
    ops.node(121008, 4.5, 4.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.2025, 28849467.95308392, 12020611.6471183, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 365.11225162, 0.0010587, 434.91964086, 0.02530588, 43.49196409, 0.07368825, -365.11225162, -0.0010587, -434.91964086, -0.02530588, -43.49196409, -0.07368825, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 333.04255681, 0.0010587, 396.71840251, 0.02530588, 39.67184025, 0.07368825, -333.04255681, -0.0010587, -396.71840251, -0.02530588, -39.67184025, -0.07368825, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.0, 4.5, 0.0)
    ops.node(121009, 9.0, 4.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.2025, 29357638.77075427, 12232349.48781428, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 343.22236221, 0.00100803, 410.0221824, 0.02667068, 41.00221824, 0.08162276, -343.22236221, -0.00100803, -410.0221824, -0.02667068, -41.00221824, -0.08162276, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 311.58712338, 0.00100803, 372.22991974, 0.02667068, 37.22299197, 0.08162276, -311.58712338, -0.00100803, -372.22991974, -0.02667068, -37.22299197, -0.08162276, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.0, 4.5, 0.0)
    ops.node(121010, 12.0, 4.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.2025, 28988809.38776533, 12078670.57823556, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 341.80723247, 0.00102138, 408.38466353, 0.02711441, 40.83846635, 0.08063045, -341.80723247, -0.00102138, -408.38466353, -0.02711441, -40.83846635, -0.08063045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 310.60950911, 0.00102138, 371.11022769, 0.02711441, 37.11102277, 0.08063045, -310.60950911, -0.00102138, -371.11022769, -0.02711441, -37.11102277, -0.08063045, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 16.5, 4.5, 0.0)
    ops.node(121011, 16.5, 4.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 28067695.21309378, 11694873.00545574, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 363.38477427, 0.00105379, 432.70963723, 0.02458455, 43.27096372, 0.06964159, -363.38477427, -0.00105379, -432.70963723, -0.02458455, -43.27096372, -0.06964159, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 330.8467108, 0.00105379, 393.96411281, 0.02458455, 39.39641128, 0.06964159, -330.8467108, -0.00105379, -393.96411281, -0.02458455, -39.39641128, -0.06964159, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 21.0, 4.5, 0.0)
    ops.node(121012, 21.0, 4.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 30379169.23356236, 12657987.18065098, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 184.5991795, 0.00125065, 218.80922328, 0.02963447, 21.88092233, 0.09985005, -184.5991795, -0.00125065, -218.80922328, -0.02963447, -21.88092233, -0.09985005, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 207.74224852, 0.00125065, 246.24118138, 0.02963447, 24.62411814, 0.09985005, -207.74224852, -0.00125065, -246.24118138, -0.02963447, -24.62411814, -0.09985005, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.1225, 28963055.11222184, 12067939.63009243, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 182.61053438, 0.00123144, 216.38139513, 0.02816108, 21.63813951, 0.08975599, -182.61053438, -0.00123144, -216.38139513, -0.02816108, -21.63813951, -0.08975599, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 206.82477267, 0.00123144, 245.07366461, 0.02816108, 24.50736646, 0.08975599, -206.82477267, -0.00123144, -245.07366461, -0.02816108, -24.50736646, -0.08975599, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.5, 9.0, 0.0)
    ops.node(121014, 4.5, 9.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.2025, 29702617.92737174, 12376090.80307156, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 361.32842536, 0.00100417, 430.38273997, 0.02634259, 43.038274, 0.07816771, -361.32842536, -0.00100417, -430.38273997, -0.02634259, -43.038274, -0.07816771, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 329.55364419, 0.00100417, 392.53540656, 0.02634259, 39.25354066, 0.07816771, -329.55364419, -0.00100417, -392.53540656, -0.02634259, -39.25354066, -0.07816771, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 9.0, 0.0)
    ops.node(121015, 9.0, 9.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.2025, 28999093.56691035, 12082955.65287931, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 340.94707668, 0.00102186, 407.31665153, 0.02691719, 40.73166515, 0.08032011, -340.94707668, -0.00102186, -407.31665153, -0.02691719, -40.73166515, -0.08032011, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 310.16479408, 0.00102186, 370.54221604, 0.02691719, 37.0542216, 0.08032011, -310.16479408, -0.00102186, -370.54221604, -0.02691719, -37.0542216, -0.08032011, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.0, 9.0, 0.0)
    ops.node(121016, 12.0, 9.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.2025, 28951009.78483889, 12062920.74368287, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 340.07742725, 0.00100792, 406.28212004, 0.02663968, 40.628212, 0.07985223, -340.07742725, -0.00100792, -406.28212004, -0.02663968, -40.628212, -0.07985223, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 309.08926325, 0.00100792, 369.26132431, 0.02663968, 36.92613243, 0.07985223, -309.08926325, -0.00100792, -369.26132431, -0.02663968, -36.92613243, -0.07985223, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 16.5, 9.0, 0.0)
    ops.node(121017, 16.5, 9.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.2025, 27782287.66946178, 11575953.19560908, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 367.29931874, 0.00105738, 437.2684012, 0.02488296, 43.72684012, 0.06868713, -367.29931874, -0.00105738, -437.2684012, -0.02488296, -43.72684012, -0.06868713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 333.46683343, 0.00105738, 396.99095988, 0.02488296, 39.69909599, 0.06868713, -333.46683343, -0.00105738, -396.99095988, -0.02488296, -39.69909599, -0.06868713, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.1225, 28399578.10402948, 11833157.54334562, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 181.13037426, 0.00131852, 214.51448986, 0.02770906, 21.45144899, 0.08570149, -181.13037426, -0.00131852, -214.51448986, -0.02770906, -21.45144899, -0.08570149, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 202.80623608, 0.00131852, 240.18542693, 0.02770906, 24.01854269, 0.08570149, -202.80623608, -0.00131852, -240.18542693, -0.02770906, -24.01854269, -0.08570149, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.09, 28564195.98273878, 11901748.32614116, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 121.34357805, 0.00151378, 144.48200193, 0.03877272, 14.44820019, 0.11365728, -121.34357805, -0.00151378, -144.48200193, -0.03877272, -14.44820019, -0.11365728, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 121.34357805, 0.00151378, 144.48200193, 0.03877272, 14.44820019, 0.11365728, -121.34357805, -0.00151378, -144.48200193, -0.03877272, -14.44820019, -0.11365728, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 4.5, 13.5, 0.0)
    ops.node(121020, 4.5, 13.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.1225, 29334359.91789567, 12222649.96578986, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 185.26075949, 0.00133478, 219.5697808, 0.03140837, 21.95697808, 0.09532616, -185.26075949, -0.00133478, -219.5697808, -0.03140837, -21.95697808, -0.09532616, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 185.26075949, 0.00133478, 219.5697808, 0.03140837, 21.95697808, 0.09532616, -185.26075949, -0.00133478, -219.5697808, -0.03140837, -21.95697808, -0.09532616, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 9.0, 13.5, 0.0)
    ops.node(121021, 9.0, 13.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.1225, 29985885.61885705, 12494119.0078571, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 172.87322797, 0.00128344, 205.61666861, 0.0329845, 20.56166686, 0.10810758, -172.87322797, -0.00128344, -205.61666861, -0.0329845, -20.56166686, -0.10810758, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 172.87322797, 0.00128344, 205.61666861, 0.0329845, 20.56166686, 0.10810758, -172.87322797, -0.00128344, -205.61666861, -0.0329845, -20.56166686, -0.10810758, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 12.0, 13.5, 0.0)
    ops.node(121022, 12.0, 13.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.1225, 28869664.30177101, 12029026.79240459, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 174.89205497, 0.00129503, 208.02127429, 0.03238666, 20.80212743, 0.10082022, -174.89205497, -0.00129503, -208.02127429, -0.03238666, -20.80212743, -0.10082022, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 174.89205497, 0.00129503, 208.02127429, 0.03238666, 20.80212743, 0.10082022, -174.89205497, -0.00129503, -208.02127429, -0.03238666, -20.80212743, -0.10082022, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 16.5, 13.5, 0.0)
    ops.node(121023, 16.5, 13.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.1225, 28946368.05670452, 12060986.69029355, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 184.13411454, 0.00129579, 218.1840801, 0.03127993, 21.81840801, 0.09276947, -184.13411454, -0.00129579, -218.1840801, -0.03127993, -21.81840801, -0.09276947, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 184.13411454, 0.00129579, 218.1840801, 0.03127993, 21.81840801, 0.09276947, -184.13411454, -0.00129579, -218.1840801, -0.03127993, -21.81840801, -0.09276947, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.09, 27886354.61364824, 11619314.42235343, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 119.91893349, 0.00153949, 142.72254172, 0.03867918, 14.27225417, 0.10886277, -119.91893349, -0.00153949, -142.72254172, -0.03867918, -14.27225417, -0.10886277, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 119.91893349, 0.00153949, 142.72254172, 0.03867918, 14.27225417, 0.10886277, -119.91893349, -0.00153949, -142.72254172, -0.03867918, -14.27225417, -0.10886277, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.3)
    ops.node(122001, 0.0, 0.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 29276942.8222922, 12198726.17595509, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 108.29981797, 0.00136169, 129.77703467, 0.04405218, 12.97770347, 0.13999667, -108.29981797, -0.00136169, -129.77703467, -0.04405218, -12.97770347, -0.13999667, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 108.29981797, 0.00136169, 129.77703467, 0.04405218, 12.97770347, 0.13999667, -108.29981797, -0.00136169, -129.77703467, -0.04405218, -12.97770347, -0.13999667, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.5, 0.0, 3.3)
    ops.node(122002, 4.5, 0.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.1225, 29983777.21754815, 12493240.50731173, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 157.22099064, 0.0012062, 187.61884447, 0.03485135, 18.76188445, 0.11773705, -157.22099064, -0.0012062, -187.61884447, -0.03485135, -18.76188445, -0.11773705, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 157.22099064, 0.0012062, 187.61884447, 0.03485135, 18.76188445, 0.11773705, -157.22099064, -0.0012062, -187.61884447, -0.03485135, -18.76188445, -0.11773705, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.5, 0.0, 3.3)
    ops.node(122005, 16.5, 0.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.1225, 28324076.02951979, 11801698.34563325, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 160.89830082, 0.00122071, 192.08671944, 0.03405598, 19.20867194, 0.10727037, -160.89830082, -0.00122071, -192.08671944, -0.03405598, -19.20867194, -0.10727037, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 160.89830082, 0.00122071, 192.08671944, 0.03405598, 19.20867194, 0.10727037, -160.89830082, -0.00122071, -192.08671944, -0.03405598, -19.20867194, -0.10727037, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 21.0, 0.0, 3.3)
    ops.node(122006, 21.0, 0.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.09, 26719602.6483393, 11133167.77014138, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 106.48330536, 0.00144739, 127.61143468, 0.04093432, 12.76114347, 0.12037207, -106.48330536, -0.00144739, -127.61143468, -0.04093432, -12.76114347, -0.12037207, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 106.48330536, 0.00144739, 127.61143468, 0.04093432, 12.76114347, 0.12037207, -106.48330536, -0.00144739, -127.61143468, -0.04093432, -12.76114347, -0.12037207, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.3)
    ops.node(122007, 0.0, 4.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 28313317.32499262, 11797215.55208026, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 170.28910998, 0.00118645, 203.29726805, 0.03242849, 20.3297268, 0.10557633, -170.28910998, -0.00118645, -203.29726805, -0.03242849, -20.3297268, -0.10557633, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 203.0447382, 0.00118645, 242.40211587, 0.03242849, 24.24021159, 0.10557633, -203.0447382, -0.00118645, -242.40211587, -0.03242849, -24.24021159, -0.10557633, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.5, 4.5, 3.3)
    ops.node(122008, 4.5, 4.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.2025, 29408319.40775915, 12253466.41989965, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 321.36415799, 0.00095102, 384.93022363, 0.02808527, 38.49302236, 0.08781489, -321.36415799, -0.00095102, -384.93022363, -0.02808527, -38.49302236, -0.08781489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 290.86744551, 0.00095102, 348.4012391, 0.02808527, 34.84012391, 0.08781489, -290.86744551, -0.00095102, -348.4012391, -0.02808527, -34.84012391, -0.08781489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.0, 4.5, 3.3)
    ops.node(122009, 9.0, 4.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.2025, 28869719.10746099, 12029049.62810875, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 300.47514413, 0.00094834, 360.90119104, 0.02944051, 36.0901191, 0.0914732, -300.47514413, -0.00094834, -360.90119104, -0.02944051, -36.0901191, -0.0914732, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 271.45567677, 0.00094834, 326.04586095, 0.02944051, 32.60458609, 0.0914732, -271.45567677, -0.00094834, -326.04586095, -0.02944051, -32.60458609, -0.0914732, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.0, 4.5, 3.3)
    ops.node(122010, 12.0, 4.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.2025, 30144443.78081202, 12560184.90867168, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 306.03593906, 0.00093501, 367.06908799, 0.02878991, 36.7069088, 0.0950722, -306.03593906, -0.00093501, -367.06908799, -0.02878991, -36.7069088, -0.0950722, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 276.1223084, 0.00093501, 331.1897427, 0.02878991, 33.11897427, 0.0950722, -276.1223084, -0.00093501, -331.1897427, -0.02878991, -33.11897427, -0.0950722, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 16.5, 4.5, 3.3)
    ops.node(122011, 16.5, 4.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 28061049.99688608, 11692104.1653692, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 322.22281597, 0.00098063, 386.17971479, 0.02768615, 38.61797148, 0.08227581, -322.22281597, -0.00098063, -386.17971479, -0.02768615, -38.61797148, -0.08227581, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 291.14086245, 0.00098063, 348.9284112, 0.02768615, 34.89284112, 0.08227581, -291.14086245, -0.00098063, -348.9284112, -0.02768615, -34.89284112, -0.08227581, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.3)
    ops.node(122012, 21.0, 4.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 30221821.11777773, 12592425.46574072, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 173.34688737, 0.00114163, 206.82350113, 0.03278934, 20.68235011, 0.11696485, -173.34688737, -0.00114163, -206.82350113, -0.03278934, -20.68235011, -0.11696485, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 207.23624715, 0.00114163, 247.25754726, 0.03278934, 24.72575473, 0.11696485, -207.23624715, -0.00114163, -247.25754726, -0.03278934, -24.72575473, -0.11696485, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.3)
    ops.node(122013, 0.0, 9.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.1225, 29278846.50758622, 12199519.37816093, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 172.4064659, 0.00115537, 205.81746884, 0.03316558, 20.58174688, 0.11208864, -172.4064659, -0.00115537, -205.81746884, -0.03316558, -20.58174688, -0.11208864, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 206.48225777, 0.00115537, 246.49687836, 0.03316558, 24.64968784, 0.11208864, -206.48225777, -0.00115537, -246.49687836, -0.03316558, -24.64968784, -0.11208864, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.5, 9.0, 3.3)
    ops.node(122014, 4.5, 9.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.2025, 30381501.89240102, 12658959.12183376, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 324.0762154, 0.00093697, 387.78695986, 0.027929, 38.77869599, 0.0910164, -324.0762154, -0.00093697, -387.78695986, -0.027929, -38.77869599, -0.0910164, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 293.22368714, 0.00093697, 350.86907582, 0.027929, 35.08690758, 0.0910164, -293.22368714, -0.00093697, -350.86907582, -0.027929, -35.08690758, -0.0910164, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 9.0, 3.3)
    ops.node(122015, 9.0, 9.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.2025, 30403263.32896081, 12668026.38706701, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 309.26133135, 0.00092024, 370.74804412, 0.02920964, 37.07480441, 0.09602255, -309.26133135, -0.00092024, -370.74804412, -0.02920964, -37.07480441, -0.09602255, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 278.45761005, 0.00092024, 333.81998921, 0.02920964, 33.38199892, 0.09602255, -278.45761005, -0.00092024, -333.81998921, -0.02920964, -33.38199892, -0.09602255, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.0, 9.0, 3.3)
    ops.node(122016, 12.0, 9.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.2025, 28732234.16407426, 11971764.23503094, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 307.31770142, 0.00094525, 369.09718745, 0.02835185, 36.90971875, 0.08959525, -307.31770142, -0.00094525, -369.09718745, -0.02835185, -36.90971875, -0.08959525, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 276.43757005, 0.00094525, 332.00928271, 0.02835185, 33.20092827, 0.08959525, -276.43757005, -0.00094525, -332.00928271, -0.02835185, -33.20092827, -0.08959525, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 16.5, 9.0, 3.3)
    ops.node(122017, 16.5, 9.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.2025, 29083049.60271313, 12117937.3344638, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 324.98196258, 0.00094472, 389.35290069, 0.02817464, 38.93529007, 0.08671645, -324.98196258, -0.00094472, -389.35290069, -0.02817464, -38.93529007, -0.08671645, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 293.00162701, 0.00094472, 351.03804678, 0.02817464, 35.10380468, 0.08671645, -293.00162701, -0.00094472, -351.03804678, -0.02817464, -35.10380468, -0.08671645, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.3)
    ops.node(122018, 21.0, 9.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.1225, 27547377.0063777, 11478073.75265738, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 169.2791189, 0.00118796, 202.01126839, 0.03131421, 20.20112684, 0.09959984, -169.2791189, -0.00118796, -202.01126839, -0.03131421, -20.20112684, -0.09959984, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 202.55964093, 0.00118796, 241.72697881, 0.03131421, 24.17269788, 0.09959984, -202.55964093, -0.00118796, -241.72697881, -0.03131421, -24.17269788, -0.09959984, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.3)
    ops.node(122019, 0.0, 13.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.09, 28448725.93587481, 11853635.8066145, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 105.29581956, 0.00139188, 126.23350339, 0.04342514, 12.62335034, 0.13439816, -105.29581956, -0.00139188, -126.23350339, -0.04342514, -12.62335034, -0.13439816, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 105.29581956, 0.00139188, 126.23350339, 0.04342514, 12.62335034, 0.13439816, -105.29581956, -0.00139188, -126.23350339, -0.04342514, -12.62335034, -0.13439816, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 4.5, 13.5, 3.3)
    ops.node(122020, 4.5, 13.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.1225, 28833605.38011491, 12014002.24171454, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 158.95147496, 0.00124103, 189.7717106, 0.03436018, 18.97717106, 0.11066983, -158.95147496, -0.00124103, -189.7717106, -0.03436018, -18.97717106, -0.11066983, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 158.95147496, 0.00124103, 189.7717106, 0.03436018, 18.97717106, 0.11066983, -158.95147496, -0.00124103, -189.7717106, -0.03436018, -18.97717106, -0.11066983, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.3)
    ops.node(122021, 9.0, 13.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.1225, 28524119.93168663, 11885049.9715361, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 151.19990935, 0.00119209, 181.05623839, 0.03538702, 18.10562384, 0.11677416, -151.19990935, -0.00119209, -181.05623839, -0.03538702, -18.10562384, -0.11677416, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 151.19990935, 0.00119209, 181.05623839, 0.03538702, 18.10562384, 0.11677416, -151.19990935, -0.00119209, -181.05623839, -0.03538702, -18.10562384, -0.11677416, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.3)
    ops.node(122022, 12.0, 13.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.1225, 28475381.74435409, 11864742.39348087, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 148.50122127, 0.00119097, 177.8264521, 0.03574303, 17.78264521, 0.116846, -148.50122127, -0.00119097, -177.8264521, -0.03574303, -17.78264521, -0.116846, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 148.50122127, 0.00119097, 177.8264521, 0.03574303, 17.78264521, 0.116846, -148.50122127, -0.00119097, -177.8264521, -0.03574303, -17.78264521, -0.116846, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 16.5, 13.5, 3.3)
    ops.node(122023, 16.5, 13.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.1225, 28538810.48410513, 11891171.0350438, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 157.34636841, 0.00120101, 187.85385621, 0.03432635, 18.78538562, 0.10885872, -157.34636841, -0.00120101, -187.85385621, -0.03432635, -18.78538562, -0.10885872, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 157.34636841, 0.00120101, 187.85385621, 0.03432635, 18.78538562, 0.10885872, -157.34636841, -0.00120101, -187.85385621, -0.03432635, -18.78538562, -0.10885872, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.3)
    ops.node(122024, 21.0, 13.5, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.09, 28523454.06782252, 11884772.52825938, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 109.21550482, 0.00135336, 130.92935909, 0.04311876, 13.09293591, 0.13455492, -109.21550482, -0.00135336, -130.92935909, -0.04311876, -13.09293591, -0.13455492, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 109.21550482, 0.00135336, 130.92935909, 0.04311876, 13.09293591, 0.13455492, -109.21550482, -0.00135336, -130.92935909, -0.04311876, -13.09293591, -0.13455492, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.1)
    ops.node(123001, 0.0, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.09, 28691328.24760136, 11954720.10316724, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 92.03102168, 0.00133992, 111.05758827, 0.04828792, 11.10575883, 0.14828792, -92.03102168, -0.00133992, -111.05758827, -0.04828792, -11.10575883, -0.14828792, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 92.03102168, 0.00133992, 111.05758827, 0.04828792, 11.10575883, 0.14828792, -92.03102168, -0.00133992, -111.05758827, -0.04828792, -11.10575883, -0.14828792, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.5, 0.0, 6.1)
    ops.node(123002, 4.5, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1225, 28915980.09156365, 12048325.03815152, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 157.63025339, 0.00116419, 189.61506711, 0.04004608, 18.96150671, 0.13616765, -157.63025339, -0.00116419, -189.61506711, -0.04004608, -18.96150671, -0.13616765, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 147.42039681, 0.00116419, 177.33352471, 0.04004608, 17.73335247, 0.13616765, -147.42039681, -0.00116419, -177.33352471, -0.04004608, -17.73335247, -0.13616765, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.5, 0.0, 6.1)
    ops.node(123005, 16.5, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 27723062.9021742, 11551276.20923925, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 163.2327231, 0.00120101, 196.51550128, 0.03861016, 19.65155013, 0.12848857, -163.2327231, -0.00120101, -196.51550128, -0.03861016, -19.65155013, -0.12848857, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 151.96444781, 0.00120101, 182.94965048, 0.03861016, 18.29496505, 0.12848857, -151.96444781, -0.00120101, -182.94965048, -0.03861016, -18.29496505, -0.12848857, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 21.0, 0.0, 6.1)
    ops.node(123006, 21.0, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.09, 29776046.75268529, 12406686.1469522, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 95.67491906, 0.00128399, 115.27362127, 0.04741756, 11.52736213, 0.14741756, -95.67491906, -0.00128399, -115.27362127, -0.04741756, -11.52736213, -0.14741756, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 95.67491906, 0.00128399, 115.27362127, 0.04741756, 11.52736213, 0.14741756, -95.67491906, -0.00128399, -115.27362127, -0.04741756, -11.52736213, -0.14741756, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.1)
    ops.node(123007, 0.0, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 28198780.87455999, 11749492.03106667, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 148.76410418, 0.00111227, 179.05353569, 0.03632811, 17.90535357, 0.12878279, -148.76410418, -0.00111227, -179.05353569, -0.03632811, -17.90535357, -0.12878279, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 182.23652588, 0.00111227, 219.34118094, 0.03632811, 21.93411809, 0.12878279, -182.23652588, -0.00111227, -219.34118094, -0.03632811, -21.93411809, -0.12878279, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.5, 4.5, 6.1)
    ops.node(123008, 4.5, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.2025, 28363421.26852272, 11818092.1952178, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 278.70315352, 0.00094362, 336.0844423, 0.03039198, 33.60844423, 0.09750311, -278.70315352, -0.00094362, -336.0844423, -0.03039198, -33.60844423, -0.09750311, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 249.72299964, 0.00094362, 301.13765849, 0.03039198, 30.11376585, 0.09750311, -249.72299964, -0.00094362, -301.13765849, -0.03039198, -30.11376585, -0.09750311, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.1)
    ops.node(123009, 9.0, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.2025, 28894102.54073643, 12039209.39197351, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 271.68316551, 0.00093188, 328.01461904, 0.03112741, 32.8014619, 0.10366506, -271.68316551, -0.00093188, -328.01461904, -0.03112741, -32.8014619, -0.10366506, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 241.88563292, 0.00093188, 292.038793, 0.03112741, 29.2038793, 0.10366506, -241.88563292, -0.00093188, -292.038793, -0.03112741, -29.2038793, -0.10366506, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.1)
    ops.node(123010, 12.0, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.2025, 27850484.34329462, 11604368.47637276, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 266.54902524, 0.00094024, 322.20976128, 0.03108069, 32.22097613, 0.10049335, -266.54902524, -0.00094024, -322.20976128, -0.03108069, -32.22097613, -0.10049335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 237.60251441, 0.00094024, 287.21864347, 0.03108069, 28.72186435, 0.10049335, -237.60251441, -0.00094024, -287.21864347, -0.03108069, -28.72186435, -0.10049335, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 16.5, 4.5, 6.1)
    ops.node(123011, 16.5, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.2025, 26970645.92373956, 11237769.13489148, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 281.89992243, 0.00095783, 340.22933163, 0.02994838, 34.02293316, 0.09215461, -281.89992243, -0.00095783, -340.22933163, -0.02994838, -34.02293316, -0.09215461, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 251.26025503, 0.00095783, 303.24984802, 0.02994838, 30.3249848, 0.09215461, -251.26025503, -0.00095783, -303.24984802, -0.02994838, -30.3249848, -0.09215461, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.1)
    ops.node(123012, 21.0, 4.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 28354397.05412301, 11814332.10588459, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 148.0936628, 0.00112523, 178.22803692, 0.03594017, 17.82280369, 0.12921237, -148.0936628, -0.00112523, -178.22803692, -0.03594017, -17.82280369, -0.12921237, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 180.28583814, 0.00112523, 216.97073601, 0.03594017, 21.6970736, 0.12921237, -180.28583814, -0.00112523, -216.97073601, -0.03594017, -21.6970736, -0.12921237, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.1)
    ops.node(123013, 0.0, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.1225, 29179792.43480535, 12158246.84783556, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 148.13106362, 0.0011261, 178.13932399, 0.03626042, 17.8139324, 0.13366721, -148.13106362, -0.0011261, -178.13932399, -0.03626042, -17.8139324, -0.13366721, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 179.09666587, 0.0011261, 215.37791067, 0.03626042, 21.53779107, 0.13366721, -179.09666587, -0.0011261, -215.37791067, -0.03626042, -21.53779107, -0.13366721, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.5, 9.0, 6.1)
    ops.node(123014, 4.5, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.2025, 29511899.12359496, 12296624.63483123, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 281.71159774, 0.00092877, 339.2421052, 0.03045635, 33.92421052, 0.10111209, -281.71159774, -0.00092877, -339.2421052, -0.03045635, -33.92421052, -0.10111209, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 252.36707462, 0.00092877, 303.90490972, 0.03045635, 30.39049097, 0.10111209, -252.36707462, -0.00092877, -303.90490972, -0.03045635, -30.39049097, -0.10111209, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.1)
    ops.node(123015, 9.0, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.2025, 28799120.42305537, 11999633.50960641, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 265.5969642, 0.00090718, 320.63572953, 0.03115724, 32.06357295, 0.10293917, -265.5969642, -0.00090718, -320.63572953, -0.03115724, -32.06357295, -0.10293917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 237.05107666, 0.00090718, 286.17437375, 0.03115724, 28.61743738, 0.10293917, -237.05107666, -0.00090718, -286.17437375, -0.03115724, -28.61743738, -0.10293917, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.1)
    ops.node(123016, 12.0, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.2025, 28689745.98277812, 11954060.82615755, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 270.93167019, 0.00093017, 327.12259112, 0.03130577, 32.71225911, 0.10276953, -270.93167019, -0.00093017, -327.12259112, -0.03130577, -32.71225911, -0.10276953, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 241.49606733, 0.00093017, 291.58207763, 0.03130577, 29.15820776, 0.10276953, -241.49606733, -0.00093017, -291.58207763, -0.03130577, -29.15820776, -0.10276953, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 16.5, 9.0, 6.1)
    ops.node(123017, 16.5, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.2025, 29413992.17863301, 12255830.07443042, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 284.60289617, 0.00091406, 342.77205891, 0.03002206, 34.27720589, 0.10039205, -284.60289617, -0.00091406, -342.77205891, -0.03002206, -34.27720589, -0.10039205, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 253.94123262, 0.00091406, 305.84354663, 0.03002206, 30.58435466, 0.10039205, -253.94123262, -0.00091406, -305.84354663, -0.03002206, -30.58435466, -0.10039205, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.1)
    ops.node(123018, 21.0, 9.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1225, 28682349.43846076, 11950978.93269199, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 147.94323201, 0.00111145, 178.00093649, 0.03662122, 17.80009365, 0.13157637, -147.94323201, -0.00111145, -178.00093649, -0.03662122, -17.80009365, -0.13157637, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 180.13785192, 0.00111145, 216.73655431, 0.03662122, 21.67365543, 0.13157637, -180.13785192, -0.00111145, -216.73655431, -0.03662122, -21.67365543, -0.13157637, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.1)
    ops.node(123019, 0.0, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.09, 29786819.70148348, 12411174.87561812, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 93.3249446, 0.00130397, 112.44023368, 0.04845985, 11.24402337, 0.14845985, -93.3249446, -0.00130397, -112.44023368, -0.04845985, -11.24402337, -0.14845985, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 93.3249446, 0.00130397, 112.44023368, 0.04845985, 11.24402337, 0.14845985, -93.3249446, -0.00130397, -112.44023368, -0.04845985, -11.24402337, -0.14845985, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 4.5, 13.5, 6.1)
    ops.node(123020, 4.5, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1225, 29619982.48268694, 12341659.36778622, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 157.94903936, 0.00117782, 189.8452718, 0.04005242, 18.98452718, 0.13953018, -157.94903936, -0.00117782, -189.8452718, -0.04005242, -18.98452718, -0.13953018, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 148.01782717, 0.00117782, 177.9085504, 0.04005242, 17.79085504, 0.13953018, -148.01782717, -0.00117782, -177.9085504, -0.04005242, -17.79085504, -0.13953018, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.1)
    ops.node(123021, 9.0, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.1225, 29462749.74273761, 12276145.72614067, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 167.06690586, 0.00115282, 201.20019609, 0.04225673, 20.12001961, 0.14225673, -167.06690586, -0.00115282, -201.20019609, -0.04225673, -20.12001961, -0.14225673, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 167.06690586, 0.00115282, 201.20019609, 0.04225673, 20.12001961, 0.14225673, -167.06690586, -0.00115282, -201.20019609, -0.04225673, -20.12001961, -0.14225673, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.1)
    ops.node(123022, 12.0, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.1225, 28200443.98773813, 11750184.99489089, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 165.14402155, 0.00118825, 199.17561608, 0.04147431, 19.91756161, 0.13975566, -165.14402155, -0.00118825, -199.17561608, -0.04147431, -19.91756161, -0.13975566, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 165.14402155, 0.00118825, 199.17561608, 0.04147431, 19.91756161, 0.13975566, -165.14402155, -0.00118825, -199.17561608, -0.04147431, -19.91756161, -0.13975566, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 16.5, 13.5, 6.1)
    ops.node(123023, 16.5, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 28979479.29863358, 12074783.04109732, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 160.29913207, 0.00115921, 192.81328574, 0.03960514, 19.28132857, 0.13603913, -160.29913207, -0.00115921, -192.81328574, -0.03960514, -19.28132857, -0.13603913, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 149.60388436, 0.00115921, 179.94867552, 0.03960514, 17.99486755, 0.13603913, -149.60388436, -0.00115921, -179.94867552, -0.03960514, -17.99486755, -0.13603913, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.1)
    ops.node(123024, 21.0, 13.5, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.09, 30123186.53883194, 12551327.72451331, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 95.75537025, 0.00126695, 115.30080053, 0.048033, 11.53008005, 0.148033, -95.75537025, -0.00126695, -115.30080053, -0.048033, -11.53008005, -0.148033, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 95.75537025, 0.00126695, 115.30080053, 0.048033, 11.53008005, 0.148033, -95.75537025, -0.00126695, -115.30080053, -0.048033, -11.53008005, -0.148033, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.9)
    ops.node(124001, 0.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.09, 28065363.77186851, 11693901.57161188, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 89.75887139, 0.00141593, 109.28248882, 0.05605951, 10.92824888, 0.15605951, -89.75887139, -0.00141593, -109.28248882, -0.05605951, -10.92824888, -0.15605951, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 96.83166784, 0.00141593, 117.89370225, 0.05605951, 11.78937023, 0.15605951, -96.83166784, -0.00141593, -117.89370225, -0.05605951, -11.78937023, -0.15605951, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.5, 0.0, 8.9)
    ops.node(124002, 4.5, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1225, 28856984.96102967, 12023743.73376236, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 145.02317603, 0.00111367, 175.98340513, 0.04636781, 17.59834051, 0.14636781, -145.02317603, -0.00111367, -175.98340513, -0.04636781, -17.59834051, -0.14636781, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 145.02317603, 0.00111367, 175.98340513, 0.04636781, 17.59834051, 0.14636781, -145.02317603, -0.00111367, -175.98340513, -0.04636781, -17.59834051, -0.14636781, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.5, 0.0, 8.9)
    ops.node(124005, 16.5, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 29443011.75311004, 12267921.56379585, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 147.86523994, 0.0011017, 179.21642857, 0.04584291, 17.92164286, 0.14584291, -147.86523994, -0.0011017, -179.21642857, -0.04584291, -17.92164286, -0.14584291, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 147.86523994, 0.0011017, 179.21642857, 0.04584291, 17.92164286, 0.14584291, -147.86523994, -0.0011017, -179.21642857, -0.04584291, -17.92164286, -0.14584291, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 21.0, 0.0, 8.9)
    ops.node(124006, 21.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.09, 30048237.24145513, 12520098.85060631, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 91.79226782, 0.00131527, 111.26880369, 0.05511152, 11.12688037, 0.15511152, -91.79226782, -0.00131527, -111.26880369, -0.05511152, -11.12688037, -0.15511152, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 99.42128276, 0.00131527, 120.51654739, 0.05511152, 12.05165474, 0.15511152, -99.42128276, -0.00131527, -120.51654739, -0.05511152, -12.05165474, -0.15511152, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 8.9)
    ops.node(124007, 0.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 28586722.73181906, 11911134.47159127, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 136.19176079, 0.0010651, 165.35210214, 0.04258326, 16.53521021, 0.14258326, -136.19176079, -0.0010651, -165.35210214, -0.04258326, -16.53521021, -0.14258326, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 179.37063599, 0.0010651, 217.77610885, 0.04258326, 21.77761089, 0.14258326, -179.37063599, -0.0010651, -217.77610885, -0.04258326, -21.77761089, -0.14258326, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.5, 4.5, 8.9)
    ops.node(124008, 4.5, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.2025, 26973401.73501252, 11238917.38958855, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 219.39134355, 0.00094286, 267.06872624, 0.03437896, 26.70687262, 0.11473287, -219.39134355, -0.00094286, -267.06872624, -0.03437896, -26.70687262, -0.11473287, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 260.71289226, 0.00094286, 317.37013376, 0.03437896, 31.73701338, 0.11473287, -260.71289226, -0.00094286, -317.37013376, -0.03437896, -31.73701338, -0.11473287, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.0, 4.5, 8.9)
    ops.node(124009, 9.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.2025, 29795198.72432537, 12414666.13513557, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 250.72627211, 0.00089457, 303.94854684, 0.03526764, 30.39485468, 0.12356928, -250.72627211, -0.00089457, -303.94854684, -0.03526764, -30.39485468, -0.12356928, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 279.4866478, 0.00089457, 338.81395733, 0.03526764, 33.88139573, 0.12356928, -279.4866478, -0.00089457, -338.81395733, -0.03526764, -33.88139573, -0.12356928, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.0, 4.5, 8.9)
    ops.node(124010, 12.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.2025, 29650940.71432991, 12354558.6309708, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 246.74917535, 0.00088232, 299.22860621, 0.03566828, 29.92286062, 0.12376723, -246.74917535, -0.00088232, -299.22860621, -0.03566828, -29.92286062, -0.12376723, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 274.97957651, 0.00088232, 333.46314247, 0.03566828, 33.34631425, 0.12376723, -274.97957651, -0.00088232, -333.46314247, -0.03566828, -33.34631425, -0.12376723, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 16.5, 4.5, 8.9)
    ops.node(124011, 16.5, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.2025, 29400394.6115024, 12250164.42145933, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 225.50585528, 0.00088436, 273.35620646, 0.03351748, 27.33562065, 0.11873078, -225.50585528, -0.00088436, -273.35620646, -0.03351748, -27.33562065, -0.11873078, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 269.95841915, 0.00088436, 327.24121184, 0.03351748, 32.72412118, 0.11873078, -269.95841915, -0.00088436, -327.24121184, -0.03351748, -32.72412118, -0.11873078, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 8.9)
    ops.node(124012, 21.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 28512480.08505565, 11880200.03543985, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 134.18012033, 0.00107212, 162.93220083, 0.04298252, 16.29322008, 0.14298252, -134.18012033, -0.00107212, -162.93220083, -0.04298252, -16.29322008, -0.14298252, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 175.31166456, 0.00107212, 212.87740143, 0.04298252, 21.28774014, 0.14298252, -175.31166456, -0.00107212, -212.87740143, -0.04298252, -21.28774014, -0.14298252, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.0, 8.9)
    ops.node(124013, 0.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.1225, 30400488.43428635, 12666870.18095265, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 135.92667496, 0.00104721, 164.3839319, 0.04211418, 16.43839319, 0.14211418, -135.92667496, -0.00104721, -164.3839319, -0.04211418, -16.43839319, -0.14211418, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 176.96119175, 0.00104721, 214.00932894, 0.04211418, 21.40093289, 0.14211418, -176.96119175, -0.00104721, -214.00932894, -0.04211418, -21.40093289, -0.14211418, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.5, 9.0, 8.9)
    ops.node(124014, 4.5, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.2025, 28918156.14845604, 12049231.72852335, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 216.22497766, 0.00090653, 262.3667308, 0.03457361, 26.23667308, 0.11893875, -216.22497766, -0.00090653, -262.3667308, -0.03457361, -26.23667308, -0.11893875, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 255.03891304, 0.00090653, 309.46344205, 0.03457361, 30.94634421, 0.11893875, -255.03891304, -0.00090653, -309.46344205, -0.03457361, -30.94634421, -0.11893875, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 9.0, 8.9)
    ops.node(124015, 9.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.2025, 29755079.90233963, 12397949.95930818, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 248.08917771, 0.00089274, 300.69879807, 0.0348413, 30.06987981, 0.12237775, -248.08917771, -0.00089274, -300.69879807, -0.0348413, -30.06987981, -0.12237775, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 275.75128098, 0.00089274, 334.22690793, 0.0348413, 33.42269079, 0.12237775, -275.75128098, -0.00089274, -334.22690793, -0.0348413, -33.42269079, -0.12237775, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.0, 9.0, 8.9)
    ops.node(124016, 12.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.2025, 27717531.24046704, 11548971.3501946, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 252.7698669, 0.00091555, 307.62923582, 0.03502695, 30.76292358, 0.11913905, -252.7698669, -0.00091555, -307.62923582, -0.03502695, -30.76292358, -0.11913905, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 282.69343732, 0.00091555, 344.04720453, 0.03502695, 34.40472045, 0.11913905, -282.69343732, -0.00091555, -344.04720453, -0.03502695, -34.40472045, -0.11913905, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 16.5, 9.0, 8.9)
    ops.node(124017, 16.5, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.2025, 29294531.08320606, 12206054.61800253, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 224.8147717, 0.00091102, 272.57972444, 0.03416948, 27.25797244, 0.11920105, -224.8147717, -0.00091102, -272.57972444, -0.03416948, -27.25797244, -0.11920105, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 267.35260951, 0.00091102, 324.15530384, 0.03416948, 32.41553038, 0.11920105, -267.35260951, -0.00091102, -324.15530384, -0.03416948, -32.41553038, -0.11920105, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 21.0, 9.0, 8.9)
    ops.node(124018, 21.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1225, 28276579.87146988, 11781908.27977912, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 136.09677084, 0.0010861, 165.32993447, 0.04317059, 16.53299345, 0.14317059, -136.09677084, -0.0010861, -165.32993447, -0.04317059, -16.53299345, -0.14317059, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 178.5216202, 0.0010861, 216.86750969, 0.04317059, 21.68675097, 0.14317059, -178.5216202, -0.0010861, -216.86750969, -0.04317059, -21.68675097, -0.14317059, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 13.5, 8.9)
    ops.node(124019, 0.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.09, 29059762.37737821, 12108234.32390759, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 89.55312114, 0.00138651, 108.80820692, 0.05593529, 10.88082069, 0.15593529, -89.55312114, -0.00138651, -108.80820692, -0.05593529, -10.88082069, -0.15593529, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 96.48847017, 0.00138651, 117.23474618, 0.05593529, 11.72347462, 0.15593529, -96.48847017, -0.00138651, -117.23474618, -0.05593529, -11.72347462, -0.15593529, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 4.5, 13.5, 8.9)
    ops.node(124020, 4.5, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1225, 29008850.08368358, 12087020.86820149, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 145.22001782, 0.00109943, 176.16921778, 0.04592889, 17.61692178, 0.14592889, -145.22001782, -0.00109943, -176.16921778, -0.04592889, -17.61692178, -0.14592889, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 145.22001782, 0.00109943, 176.16921778, 0.04592889, 17.61692178, 0.14592889, -145.22001782, -0.00109943, -176.16921778, -0.04592889, -17.61692178, -0.14592889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 8.9)
    ops.node(124021, 9.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.1225, 29430899.32516948, 12262874.71882062, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 170.04073241, 0.00113795, 206.24620636, 0.04836378, 20.62462064, 0.14836378, -170.04073241, -0.00113795, -206.24620636, -0.04836378, -20.62462064, -0.14836378, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 159.55073247, 0.00113795, 193.52265089, 0.04836378, 19.35226509, 0.14836378, -159.55073247, -0.00113795, -193.52265089, -0.04836378, -19.35226509, -0.14836378, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 8.9)
    ops.node(124022, 12.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.1225, 30088173.06093352, 12536738.77538897, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 170.46690352, 0.0011302, 206.44713376, 0.04773404, 20.64471338, 0.14773404, -170.46690352, -0.0011302, -206.44713376, -0.04773404, -20.64471338, -0.14773404, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 160.03120869, 0.0011302, 193.80879024, 0.04773404, 19.38087902, 0.14773404, -160.03120869, -0.0011302, -193.80879024, -0.04773404, -19.38087902, -0.14773404, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 16.5, 13.5, 8.9)
    ops.node(124023, 16.5, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 29910122.49124818, 12462551.03802007, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 143.69563838, 0.00108378, 173.98198689, 0.04565749, 17.39819869, 0.14565749, -143.69563838, -0.00108378, -173.98198689, -0.04565749, -17.39819869, -0.14565749, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 143.69563838, 0.00108378, 173.98198689, 0.04565749, 17.39819869, 0.14565749, -143.69563838, -0.00108378, -173.98198689, -0.04565749, -17.39819869, -0.14565749, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 21.0, 13.5, 8.9)
    ops.node(124024, 21.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.09, 28340378.52256946, 11808491.05107061, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 91.6047498, 0.00128928, 111.46982525, 0.05633696, 11.14698253, 0.15633696, -91.6047498, -0.00128928, -111.46982525, -0.05633696, -11.14698253, -0.15633696, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 99.81465698, 0.00128928, 121.46010328, 0.05633696, 12.14601033, 0.15633696, -99.81465698, -0.00128928, -121.46010328, -0.05633696, -12.14601033, -0.15633696, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(124025, 9.0, 0.0, 1.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.1225, 28386603.27091398, 11827751.36288082, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 172.91949748, 0.00101998, 205.64586074, 0.0322505, 20.56458607, 0.09785145, -172.91949748, -0.00101998, -205.64586074, -0.0322505, -20.56458607, -0.09785145, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 172.91949748, 0.00101998, 205.64586074, 0.0322505, 20.56458607, 0.09785145, -172.91949748, -0.00101998, -205.64586074, -0.0322505, -20.56458607, -0.09785145, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.7)
    ops.node(121003, 9.0, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.1225, 27329416.16481504, 11387256.7353396, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 167.36760698, 0.00102391, 199.22790956, 0.0318844, 19.92279096, 0.09425556, -167.36760698, -0.00102391, -199.22790956, -0.0318844, -19.92279096, -0.09425556, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 167.36760698, 0.00102391, 199.22790956, 0.0318844, 19.92279096, 0.09425556, -167.36760698, -0.00102391, -199.22790956, -0.0318844, -19.92279096, -0.09425556, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.0, 0.0, 0.0)
    ops.node(124026, 12.0, 0.0, 1.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.1225, 29187082.31193115, 12161284.29663798, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 174.03786044, 0.00099542, 207.04111589, 0.03260753, 20.70411159, 0.10319434, -174.03786044, -0.00099542, -207.04111589, -0.03260753, -20.70411159, -0.10319434, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 174.03786044, 0.00099542, 207.04111589, 0.03260753, 20.70411159, 0.10319434, -174.03786044, -0.00099542, -207.04111589, -0.03260753, -20.70411159, -0.10319434, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.7)
    ops.node(121004, 12.0, 0.0, 2.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.1225, 28657095.79237412, 11940456.58015588, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 167.22135676, 0.00099908, 199.24859553, 0.03262252, 19.92485955, 0.10353922, -167.22135676, -0.00099908, -199.24859553, -0.03262252, -19.92485955, -0.10353922, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 167.22135676, 0.00099908, 199.24859553, 0.03262252, 19.92485955, 0.10353922, -167.22135676, -0.00099908, -199.24859553, -0.03262252, -19.92485955, -0.10353922, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.3)
    ops.node(124027, 9.0, 0.0, 4.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.1225, 28715545.48534923, 11964810.61889551, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 174.51445495, 0.00095372, 208.9851863, 0.03660879, 20.89851863, 0.11935684, -174.51445495, -0.00095372, -208.9851863, -0.03660879, -20.89851863, -0.11935684, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 163.54307398, 0.00095372, 195.84669816, 0.03660879, 19.58466982, 0.11935684, -163.54307398, -0.00095372, -195.84669816, -0.03660879, -19.58466982, -0.11935684, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.65)
    ops.node(122003, 9.0, 0.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.1225, 29505996.50175001, 12294165.20906251, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 145.7213674, 0.00093571, 174.70173554, 0.03711185, 17.47017355, 0.128412, -145.7213674, -0.00093571, -174.70173554, -0.03711185, -17.47017355, -0.128412, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 145.7213674, 0.00093571, 174.70173554, 0.03711185, 17.47017355, 0.128412, -145.7213674, -0.00093571, -174.70173554, -0.03711185, -17.47017355, -0.128412, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.3)
    ops.node(124028, 12.0, 0.0, 4.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.1225, 28576250.54640857, 11906771.06100357, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 174.29115752, 0.00095335, 208.72659266, 0.03696808, 20.87265927, 0.11891518, -174.29115752, -0.00095335, -208.72659266, -0.03696808, -20.87265927, -0.11891518, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 163.30121405, 0.00095335, 195.56531995, 0.03696808, 19.556532, 0.11891518, -163.30121405, -0.00095335, -195.56531995, -0.03696808, -19.556532, -0.11891518, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.65)
    ops.node(122004, 12.0, 0.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.1225, 29735496.10630044, 12389790.04429185, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 144.52093708, 0.00093026, 173.22246814, 0.03758622, 17.32224681, 0.13005036, -144.52093708, -0.00093026, -173.22246814, -0.03758622, -17.32224681, -0.13005036, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 144.52093708, 0.00093026, 173.22246814, 0.03758622, 17.32224681, 0.13005036, -144.52093708, -0.00093026, -173.22246814, -0.03758622, -17.32224681, -0.13005036, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.1)
    ops.node(124029, 9.0, 0.0, 7.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.1225, 28898462.86144735, 12041026.19226973, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 166.91169155, 0.00095074, 201.18325892, 0.04128355, 20.11832589, 0.14128355, -166.91169155, -0.00095074, -201.18325892, -0.04128355, -20.11832589, -0.14128355, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 166.91169155, 0.00095074, 201.18325892, 0.04128355, 20.11832589, 0.14128355, -166.91169155, -0.00095074, -201.18325892, -0.04128355, -20.11832589, -0.14128355, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.45)
    ops.node(123003, 9.0, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.1225, 28211120.30226747, 11754633.45927811, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 123.34013371, 0.00090396, 149.08190828, 0.0410504, 14.90819083, 0.1410504, -123.34013371, -0.00090396, -149.08190828, -0.0410504, -14.90819083, -0.1410504, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 123.34013371, 0.00090396, 149.08190828, 0.0410504, 14.90819083, 0.1410504, -123.34013371, -0.00090396, -149.08190828, -0.0410504, -14.90819083, -0.1410504, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.1)
    ops.node(124030, 12.0, 0.0, 7.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.1225, 29228268.39425199, 12178445.16427167, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 164.09385294, 0.00095102, 197.70367314, 0.04211536, 19.77036731, 0.14211536, -164.09385294, -0.00095102, -197.70367314, -0.04211536, -19.77036731, -0.14211536, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 164.09385294, 0.00095102, 197.70367314, 0.04211536, 19.77036731, 0.14211536, -164.09385294, -0.00095102, -197.70367314, -0.04211536, -19.77036731, -0.14211536, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.45)
    ops.node(123004, 12.0, 0.0, 8.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.1225, 27894563.40986128, 11622734.75410887, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 119.97394415, 0.00090233, 145.06220381, 0.04090107, 14.50622038, 0.14090107, -119.97394415, -0.00090233, -145.06220381, -0.04090107, -14.50622038, -0.14090107, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 119.97394415, 0.00090233, 145.06220381, 0.04090107, 14.50622038, 0.14090107, -119.97394415, -0.00090233, -145.06220381, -0.04090107, -14.50622038, -0.14090107, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 8.9)
    ops.node(124031, 9.0, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.1225, 29180137.97929075, 12158390.82470448, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 102.84111515, 0.0008773, 124.81945412, 0.04369168, 12.48194541, 0.14369168, -102.84111515, -0.0008773, -124.81945412, -0.04369168, -12.48194541, -0.14369168, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 102.84111515, 0.0008773, 124.81945412, 0.04369168, 12.48194541, 0.14369168, -102.84111515, -0.0008773, -124.81945412, -0.04369168, -12.48194541, -0.14369168, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 9.0, 0.0, 10.25)
    ops.node(124003, 9.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.1225, 28249596.73326936, 11770665.3055289, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 165.64296896, 0.00090425, 201.83692865, 0.05040622, 20.18369287, 0.15040622, -165.64296896, -0.00090425, -201.83692865, -0.05040622, -20.18369287, -0.15040622, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 154.63360775, 0.00090425, 188.42195748, 0.05040622, 18.84219575, 0.15040622, -154.63360775, -0.00090425, -188.42195748, -0.05040622, -18.84219575, -0.15040622, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 8.9)
    ops.node(124032, 12.0, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.1225, 28884505.83171959, 12035210.7632165, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 102.45585574, 0.00086597, 124.42955609, 0.04419935, 12.44295561, 0.14419935, -102.45585574, -0.00086597, -124.42955609, -0.04419935, -12.44295561, -0.14419935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 102.45585574, 0.00086597, 124.42955609, 0.04419935, 12.44295561, 0.14419935, -102.45585574, -0.00086597, -124.42955609, -0.04419935, -12.44295561, -0.14419935, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 12.0, 0.0, 10.25)
    ops.node(124004, 12.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.1225, 28326437.18227691, 11802682.15928205, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 162.75681436, 0.00091976, 198.28780478, 0.05011845, 19.82878048, 0.15011845, -162.75681436, -0.00091976, -198.28780478, -0.05011845, -19.82878048, -0.15011845, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 152.31721757, 0.00091976, 185.56916847, 0.05011845, 18.55691685, 0.15011845, -152.31721757, -0.00091976, -185.56916847, -0.05011845, -18.55691685, -0.15011845, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Use rigid material for shear behaviour of plastic hinge
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
