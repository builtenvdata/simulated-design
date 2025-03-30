import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.16, 26205772.19626042, 10919071.74844184, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 139.4799307, 0.00064454, 167.90184844, 0.0166384, 16.79018484, 0.04190193, -139.4799307, -0.00064454, -167.90184844, -0.0166384, -16.79018484, -0.04190193, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 148.84747484, 0.00064454, 179.17822325, 0.0166384, 17.91782233, 0.04190193, -148.84747484, -0.00064454, -179.17822325, -0.0166384, -17.91782233, -0.04190193, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 149.06044, 0.01289086, 149.06044, 0.03867257, 104.342308, -1502.33697508, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 37.26511, 7.935e-05, 111.79533, 0.00023805, 372.65110001, 0.00079349, -37.26511, -7.935e-05, -111.79533, -0.00023805, -372.65110001, -0.00079349, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 149.06044, 0.01289086, 149.06044, 0.03867257, 104.342308, -1502.33697508, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 37.26511, 7.935e-05, 111.79533, 0.00023805, 372.65110001, 0.00079349, -37.26511, -7.935e-05, -111.79533, -0.00023805, -372.65110001, -0.00079349, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.5, 0.0, 0.0)
    ops.node(121002, 4.5, 0.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.3025, 28042426.02505859, 11684344.17710775, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 433.65093699, 0.00055153, 522.90282575, 0.03059168, 52.29028258, 0.06531849, -433.65093699, -0.00055153, -522.90282575, -0.03059168, -52.29028258, -0.06531849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 485.65196849, 0.00055153, 585.60645209, 0.03059168, 58.56064521, 0.06531849, -485.65196849, -0.00055153, -585.60645209, -0.03059168, -58.56064521, -0.06531849, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 333.33010394, 0.01103057, 333.33010394, 0.03309171, 233.33107276, -3008.70633818, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 83.33252599, 8.771e-05, 249.99757796, 0.00026312, 833.32525986, 0.00087706, -83.33252599, -8.771e-05, -249.99757796, -0.00026312, -833.32525986, -0.00087706, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 333.33010394, 0.01103057, 333.33010394, 0.03309171, 233.33107276, -3008.70633818, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 83.33252599, 8.771e-05, 249.99757796, 0.00026312, 833.32525986, 0.00087706, -83.33252599, -8.771e-05, -249.99757796, -0.00026312, -833.32525986, -0.00087706, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.5, 0.0, 0.0)
    ops.node(121005, 16.5, 0.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.3025, 26472866.54226427, 11030361.05927678, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 430.30669127, 0.00056168, 519.16331018, 0.02976974, 51.91633102, 0.06139844, -430.30669127, -0.00056168, -519.16331018, -0.02976974, -51.91633102, -0.06139844, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 482.15651981, 0.00056168, 581.71992192, 0.02976974, 58.17199219, 0.06139844, -482.15651981, -0.00056168, -581.71992192, -0.02976974, -58.17199219, -0.06139844, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 317.42943114, 0.01123359, 317.42943114, 0.03370077, 222.2006018, -3014.70788391, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 79.35735778, 8.847e-05, 238.07207335, 0.00026542, 793.57357784, 0.00088474, -79.35735778, -8.847e-05, -238.07207335, -0.00026542, -793.57357784, -0.00088474, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 317.42943114, 0.01123359, 317.42943114, 0.03370077, 222.2006018, -3014.70788391, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 79.35735778, 8.847e-05, 238.07207335, 0.00026542, 793.57357784, 0.00088474, -79.35735778, -8.847e-05, -238.07207335, -0.00026542, -793.57357784, -0.00088474, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 21.0, 0.0, 0.0)
    ops.node(121006, 21.0, 0.0, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.16, 26165474.20814762, 10902280.92006151, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 139.4455725, 0.00062917, 167.85705552, 0.01651539, 16.78570555, 0.04169853, -139.4455725, -0.00062917, -167.85705552, -0.01651539, -16.78570555, -0.04169853, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 149.22095071, 0.00062917, 179.62412832, 0.01651539, 17.96241283, 0.04169853, -149.22095071, -0.00062917, -179.62412832, -0.01651539, -17.96241283, -0.04169853, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 148.72005195, 0.01258333, 148.72005195, 0.03774999, 104.10403637, -1499.171441, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 37.18001299, 7.929e-05, 111.54003896, 0.00023787, 371.80012988, 0.00079289, -37.18001299, -7.929e-05, -111.54003896, -0.00023787, -371.80012988, -0.00079289, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 148.72005195, 0.01258333, 148.72005195, 0.03774999, 104.10403637, -1499.171441, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 37.18001299, 7.929e-05, 111.54003896, 0.00023787, 371.80012988, 0.00079289, -37.18001299, -7.929e-05, -111.54003896, -0.00023787, -371.80012988, -0.00079289, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 4.5, 0.0)
    ops.node(121007, 0.0, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.3025, 26059655.72111316, 10858189.88379715, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 454.87598847, 0.00055968, 548.73893452, 0.02946403, 54.87389345, 0.06014987, -454.87598847, -0.00055968, -548.73893452, -0.02946403, -54.87389345, -0.06014987, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 454.87598847, 0.00055968, 548.73893452, 0.02946403, 54.87389345, 0.06014987, -454.87598847, -0.00055968, -548.73893452, -0.02946403, -54.87389345, -0.06014987, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 312.4375898, 0.01119356, 312.4375898, 0.03358069, 218.70631286, -2994.23596129, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 78.10939745, 8.846e-05, 234.32819235, 0.00026539, 781.0939745, 0.00088463, -78.10939745, -8.846e-05, -234.32819235, -0.00026539, -781.0939745, -0.00088463, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 312.4375898, 0.01119356, 312.4375898, 0.03358069, 218.70631286, -2994.23596129, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 78.10939745, 8.846e-05, 234.32819235, 0.00026539, 781.0939745, 0.00088463, -78.10939745, -8.846e-05, -234.32819235, -0.00026539, -781.0939745, -0.00088463, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 4.5, 4.5, 0.0)
    ops.node(121008, 4.5, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.4225, 26835964.15260701, 11181651.73025292, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 861.95196221, 0.00054809, 1040.27763135, 0.04690356, 104.02776314, 0.11056661, -861.95196221, -0.00054809, -1040.27763135, -0.04690356, -104.02776314, -0.11056661, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 912.17724559, 0.00054809, 1100.89381545, 0.04690356, 110.08938155, 0.11056661, -912.17724559, -0.00054809, -1100.89381545, -0.04690356, -110.08938155, -0.11056661, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 666.1286962, 0.01096185, 666.1286962, 0.03288556, 466.29008734, -8835.65525341, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 166.53217405, 0.00013113, 499.59652215, 0.0003934, 1665.3217405, 0.00131132, -166.53217405, -0.00013113, -499.59652215, -0.0003934, -1665.3217405, -0.00131132, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 666.1286962, 0.01096185, 666.1286962, 0.03288556, 466.29008734, -8835.65525341, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 166.53217405, 0.00013113, 499.59652215, 0.0003934, 1665.3217405, 0.00131132, -166.53217405, -0.00013113, -499.59652215, -0.0003934, -1665.3217405, -0.00131132, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 9.0, 4.5, 0.0)
    ops.node(121009, 9.0, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.4225, 27308667.9774602, 11378611.65727508, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 876.21069174, 0.00053545, 1059.13754077, 0.04909885, 105.91375408, 0.11800802, -876.21069174, -0.00053545, -1059.13754077, -0.04909885, -105.91375408, -0.11800802, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 901.02162369, 0.00053545, 1089.12826068, 0.04909885, 108.91282607, 0.11800802, -901.02162369, -0.00053545, -1089.12826068, -0.04909885, -108.91282607, -0.11800802, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 662.32609906, 0.01070902, 662.32609906, 0.03212706, 463.62826934, -8976.90219228, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 165.58152477, 0.00012813, 496.7445743, 0.00038438, 1655.81524765, 0.00128126, -165.58152477, -0.00012813, -496.7445743, -0.00038438, -1655.81524765, -0.00128126, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 662.32609906, 0.01070902, 662.32609906, 0.03212706, 463.62826934, -8976.90219228, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 165.58152477, 0.00012813, 496.7445743, 0.00038438, 1655.81524765, 0.00128126, -165.58152477, -0.00012813, -496.7445743, -0.00038438, -1655.81524765, -0.00128126, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 12.0, 4.5, 0.0)
    ops.node(121010, 12.0, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.4225, 26965580.46831044, 11235658.52846268, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 873.16842541, 0.00053892, 1055.66150672, 0.04913113, 105.56615067, 0.11680014, -873.16842541, -0.00053892, -1055.66150672, -0.04913113, -105.56615067, -0.11680014, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 897.79885169, 0.00053892, 1085.43971692, 0.04913113, 108.54397169, 0.11680014, -897.79885169, -0.00053892, -1085.43971692, -0.04913113, -108.54397169, -0.11680014, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 663.22167838, 0.01077835, 663.22167838, 0.03233504, 464.25517487, -9219.88336937, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 165.8054196, 0.00012993, 497.41625879, 0.0003898, 1658.05419595, 0.00129932, -165.8054196, -0.00012993, -497.41625879, -0.0003898, -1658.05419595, -0.00129932, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 663.22167838, 0.01077835, 663.22167838, 0.03233504, 464.25517487, -9219.88336937, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 165.8054196, 0.00012993, 497.41625879, 0.0003898, 1658.05419595, 0.00129932, -165.8054196, -0.00012993, -497.41625879, -0.0003898, -1658.05419595, -0.00129932, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 16.5, 4.5, 0.0)
    ops.node(121011, 16.5, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.4225, 26108754.02658393, 10878647.51107664, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 854.7938841, 0.00054522, 1031.6266743, 0.04616129, 103.16266743, 0.10683737, -854.7938841, -0.00054522, -1031.6266743, -0.04616129, -103.16266743, -0.10683737, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 905.30110748, 0.00054522, 1092.58242031, 0.04616129, 109.25824203, 0.10683737, -905.30110748, -0.00054522, -1092.58242031, -0.04616129, -109.25824203, -0.10683737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 650.50872584, 0.01090444, 650.50872584, 0.03271333, 455.35610809, -8717.98973868, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 162.62718146, 0.00013162, 487.88154438, 0.00039487, 1626.2718146, 0.00131624, -162.62718146, -0.00013162, -487.88154438, -0.00039487, -1626.2718146, -0.00131624, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 650.50872584, 0.01090444, 650.50872584, 0.03271333, 455.35610809, -8717.98973868, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 162.62718146, 0.00013162, 487.88154438, 0.00039487, 1626.2718146, 0.00131624, -162.62718146, -0.00013162, -487.88154438, -0.00039487, -1626.2718146, -0.00131624, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 21.0, 4.5, 0.0)
    ops.node(121012, 21.0, 4.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.3025, 28258902.30848132, 11774542.62853388, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 463.90762718, 0.00056169, 559.26793214, 0.03077612, 55.92679321, 0.0658539, -463.90762718, -0.00056169, -559.26793214, -0.03077612, -55.92679321, -0.0658539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 463.90762718, 0.00056169, 559.26793214, 0.03077612, 55.92679321, 0.0658539, -463.90762718, -0.00056169, -559.26793214, -0.03077612, -55.92679321, -0.0658539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 338.85761111, 0.01123384, 338.85761111, 0.03370152, 237.20032778, -3083.31028536, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 84.71440278, 8.848e-05, 254.14320833, 0.00026543, 847.14402778, 0.00088477, -84.71440278, -8.848e-05, -254.14320833, -0.00026543, -847.14402778, -0.00088477, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 338.85761111, 0.01123384, 338.85761111, 0.03370152, 237.20032778, -3083.31028536, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 84.71440278, 8.848e-05, 254.14320833, 0.00026543, 847.14402778, 0.00088477, -84.71440278, -8.848e-05, -254.14320833, -0.00026543, -847.14402778, -0.00088477, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 9.0, 0.0)
    ops.node(121013, 0.0, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.3025, 26941623.67242133, 11225676.53017555, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 458.41409564, 0.00055514, 553.04964331, 0.03012344, 55.30496433, 0.06271657, -458.41409564, -0.00055514, -553.04964331, -0.03012344, -55.30496433, -0.06271657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 458.41409564, 0.00055514, 553.04964331, 0.03012344, 55.30496433, 0.06271657, -458.41409564, -0.00055514, -553.04964331, -0.03012344, -55.30496433, -0.06271657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 321.16766128, 0.0111028, 321.16766128, 0.03330839, 224.81736289, -2990.07054856, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 80.29191532, 8.796e-05, 240.87574596, 0.00026387, 802.9191532, 0.00087958, -80.29191532, -8.796e-05, -240.87574596, -0.00026387, -802.9191532, -0.00087958, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 321.16766128, 0.0111028, 321.16766128, 0.03330839, 224.81736289, -2990.07054856, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 80.29191532, 8.796e-05, 240.87574596, 0.00026387, 802.9191532, 0.00087958, -80.29191532, -8.796e-05, -240.87574596, -0.00026387, -802.9191532, -0.00087958, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.5, 9.0, 0.0)
    ops.node(121014, 4.5, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.4225, 27629569.84973869, 11512320.77072446, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 893.64704018, 0.00053315, 1078.23507541, 0.04829321, 107.82350754, 0.11505124, -893.64704018, -0.00053315, -1078.23507541, -0.04829321, -107.82350754, -0.11505124, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 918.37780499, 0.00053315, 1108.07412468, 0.04829321, 110.80741247, 0.11505124, -918.37780499, -0.00053315, -1108.07412468, -0.04829321, -110.80741247, -0.11505124, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 684.50861689, 0.01066303, 684.50861689, 0.03198909, 479.15603183, -9015.97762506, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 171.12715422, 0.00013088, 513.38146267, 0.00039264, 1711.27154223, 0.0013088, -171.12715422, -0.00013088, -513.38146267, -0.00039264, -1711.27154223, -0.0013088, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 684.50861689, 0.01066303, 684.50861689, 0.03198909, 479.15603183, -9015.97762506, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 171.12715422, 0.00013088, 513.38146267, 0.00039264, 1711.27154223, 0.0013088, -171.12715422, -0.00013088, -513.38146267, -0.00039264, -1711.27154223, -0.0013088, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 9.0, 9.0, 0.0)
    ops.node(121015, 9.0, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.4225, 26975146.87914767, 11239644.5329782, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 869.02097078, 0.00053868, 1050.63882163, 0.04907134, 105.06388216, 0.11676857, -869.02097078, -0.00053868, -1050.63882163, -0.04907134, -105.06388216, -0.11676857, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 893.4073479, 0.00053868, 1080.12174021, 0.04907134, 108.01217402, 0.11676857, -893.4073479, -0.00053868, -1080.12174021, -0.04907134, -108.01217402, -0.11676857, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 667.19528902, 0.01077369, 667.19528902, 0.03232106, 467.03670231, -9359.76775171, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 166.79882225, 0.00013066, 500.39646676, 0.00039199, 1667.98822254, 0.00130664, -166.79882225, -0.00013066, -500.39646676, -0.00039199, -1667.98822254, -0.00130664, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 667.19528902, 0.01077369, 667.19528902, 0.03232106, 467.03670231, -9359.76775171, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 166.79882225, 0.00013066, 500.39646676, 0.00039199, 1667.98822254, 0.00130664, -166.79882225, -0.00013066, -500.39646676, -0.00039199, -1667.98822254, -0.00130664, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.0, 9.0, 0.0)
    ops.node(121016, 12.0, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.4225, 26930419.02995164, 11221007.92914652, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 864.6715839, 0.00053415, 1045.402231, 0.04894483, 104.5402231, 0.11647717, -864.6715839, -0.00053415, -1045.402231, -0.04894483, -104.5402231, -0.11647717, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 889.06353004, 0.00053415, 1074.89249689, 0.04894483, 107.48924969, 0.11647717, -889.06353004, -0.00053415, -1074.89249689, -0.04894483, -107.48924969, -0.11647717, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 659.26599784, 0.01068294, 659.26599784, 0.03204882, 461.48619849, -9094.85833577, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 164.81649946, 0.00012933, 494.44949838, 0.00038798, 1648.16499459, 0.00129326, -164.81649946, -0.00012933, -494.44949838, -0.00038798, -1648.16499459, -0.00129326, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 659.26599784, 0.01068294, 659.26599784, 0.03204882, 461.48619849, -9094.85833577, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 164.81649946, 0.00012933, 494.44949838, 0.00038798, 1648.16499459, 0.00129326, -164.81649946, -0.00012933, -494.44949838, -0.00038798, -1648.16499459, -0.00129326, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 16.5, 9.0, 0.0)
    ops.node(121017, 16.5, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.4225, 25843266.05910226, 10768027.52462594, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 911.87593188, 0.00054781, 1100.47980719, 0.04667768, 110.04798072, 0.10629035, -911.87593188, -0.00054781, -1100.47980719, -0.04667768, -110.04798072, -0.10629035, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 937.95134866, 0.00054781, 1131.9484189, 0.04667768, 113.19484189, 0.10629035, -937.95134866, -0.00054781, -1131.9484189, -0.04667768, -113.19484189, -0.10629035, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 653.35726308, 0.0109563, 653.35726308, 0.0328689, 457.35008416, -8976.27818301, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 163.33931577, 0.00013356, 490.01794731, 0.00040067, 1633.3931577, 0.00133558, -163.33931577, -0.00013356, -490.01794731, -0.00040067, -1633.3931577, -0.00133558, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 653.35726308, 0.0109563, 653.35726308, 0.0328689, 457.35008416, -8976.27818301, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 163.33931577, 0.00013356, 490.01794731, 0.00040067, 1633.3931577, 0.00133558, -163.33931577, -0.00013356, -490.01794731, -0.00040067, -1633.3931577, -0.00133558, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 21.0, 9.0, 0.0)
    ops.node(121018, 21.0, 9.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.3025, 26417473.66669993, 11007280.6944583, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 454.13879161, 0.00057382, 547.90726028, 0.02985722, 54.79072603, 0.06135539, -454.13879161, -0.00057382, -547.90726028, -0.02985722, -54.79072603, -0.06135539, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 454.13879161, 0.00057382, 547.90726028, 0.02985722, 54.79072603, 0.06135539, -454.13879161, -0.00057382, -547.90726028, -0.02985722, -54.79072603, -0.06135539, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 318.95597284, 0.01147634, 318.95597284, 0.03442902, 223.26918099, -3063.10438417, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 79.73899321, 8.909e-05, 239.21697963, 0.00026726, 797.3899321, 0.00089086, -79.73899321, -8.909e-05, -239.21697963, -0.00026726, -797.3899321, -0.00089086, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 318.95597284, 0.01147634, 318.95597284, 0.03442902, 223.26918099, -3063.10438417, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 79.73899321, 8.909e-05, 239.21697963, 0.00026726, 797.3899321, 0.00089086, -79.73899321, -8.909e-05, -239.21697963, -0.00026726, -797.3899321, -0.00089086, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 13.5, 0.0)
    ops.node(121019, 0.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.2025, 26570602.29628523, 11071084.29011885, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 193.35236339, 0.00059409, 233.71307802, 0.01702868, 23.3713078, 0.04092725, -193.35236339, -0.00059409, -233.71307802, -0.01702868, -23.3713078, -0.04092725, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 198.93080794, 0.00059409, 240.45597696, 0.01702868, 24.0455977, 0.04092725, -198.93080794, -0.00059409, -240.45597696, -0.01702868, -24.0455977, -0.04092725, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 166.54682984, 0.01188179, 166.54682984, 0.03564538, 116.58278089, -1410.83370526, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 41.63670746, 6.909e-05, 124.91012238, 0.00020726, 416.36707459, 0.00069088, -41.63670746, -6.909e-05, -124.91012238, -0.00020726, -416.36707459, -0.00069088, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 166.54682984, 0.01188179, 166.54682984, 0.03564538, 116.58278089, -1410.83370526, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 41.63670746, 6.909e-05, 124.91012238, 0.00020726, 416.36707459, 0.00069088, -41.63670746, -6.909e-05, -124.91012238, -0.00020726, -416.36707459, -0.00069088, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 4.5, 13.5, 0.0)
    ops.node(121020, 4.5, 13.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.3025, 27287013.83597505, 11369589.09832294, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 449.80149155, 0.00056609, 542.61130144, 0.0303805, 54.26113014, 0.06367657, -449.80149155, -0.00056609, -542.61130144, -0.0303805, -54.26113014, -0.06367657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 475.86634444, 0.00056609, 574.05424685, 0.0303805, 57.40542469, 0.06367657, -475.86634444, -0.00056609, -574.05424685, -0.0303805, -57.40542469, -0.06367657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 327.19112505, 0.01132171, 327.19112505, 0.03396514, 229.03378753, -3048.28044224, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 81.79778126, 8.847e-05, 245.39334378, 0.00026542, 817.97781261, 0.00088474, -81.79778126, -8.847e-05, -245.39334378, -0.00026542, -817.97781261, -0.00088474, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 327.19112505, 0.01132171, 327.19112505, 0.03396514, 229.03378753, -3048.28044224, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 81.79778126, 8.847e-05, 245.39334378, 0.00026542, 817.97781261, 0.00088474, -81.79778126, -8.847e-05, -245.39334378, -0.00026542, -817.97781261, -0.00088474, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 9.0, 13.5, 0.0)
    ops.node(121021, 9.0, 13.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.25, 27893067.31273017, 11622111.38030424, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 346.1862208, 0.00058979, 417.20181878, 0.02592922, 41.72018188, 0.05528918, -346.1862208, -0.00058979, -417.20181878, -0.02592922, -41.72018188, -0.05528918, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 369.18415089, 0.00058979, 444.91747493, 0.02592922, 44.49174749, 0.05528918, -369.18415089, -0.00058979, -444.91747493, -0.02592922, -44.49174749, -0.05528918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 243.62278669, 0.01179576, 243.62278669, 0.03538727, 170.53595069, -2193.13952483, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 60.90569667, 7.798e-05, 182.71709002, 0.00023394, 609.05696674, 0.00077979, -60.90569667, -7.798e-05, -182.71709002, -0.00023394, -609.05696674, -0.00077979, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 243.62278669, 0.01179576, 243.62278669, 0.03538727, 170.53595069, -2193.13952483, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 60.90569667, 7.798e-05, 182.71709002, 0.00023394, 609.05696674, 0.00077979, -60.90569667, -7.798e-05, -182.71709002, -0.00023394, -609.05696674, -0.00077979, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 12.0, 13.5, 0.0)
    ops.node(121022, 12.0, 13.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.25, 26854750.92851087, 11189479.5535462, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 349.47591325, 0.00059181, 421.3131763, 0.02564134, 42.13131763, 0.05320119, -349.47591325, -0.00059181, -421.3131763, -0.02564134, -42.13131763, -0.05320119, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 373.61003765, 0.00059181, 450.40824186, 0.02564134, 45.04082419, 0.05320119, -373.61003765, -0.00059181, -450.40824186, -0.02564134, -45.04082419, -0.05320119, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 237.70802722, 0.01183619, 237.70802722, 0.03550856, 166.39561905, -2239.83771043, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 59.4270068, 7.903e-05, 178.28102041, 0.00023708, 594.27006805, 0.00079027, -59.4270068, -7.903e-05, -178.28102041, -0.00023708, -594.27006805, -0.00079027, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 237.70802722, 0.01183619, 237.70802722, 0.03550856, 166.39561905, -2239.83771043, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 59.4270068, 7.903e-05, 178.28102041, 0.00023708, 594.27006805, 0.00079027, -59.4270068, -7.903e-05, -178.28102041, -0.00023708, -594.27006805, -0.00079027, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 16.5, 13.5, 0.0)
    ops.node(121023, 16.5, 13.5, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.3025, 26926101.26402185, 11219208.86000911, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 444.41277439, 0.00055589, 536.16601917, 0.0303338, 53.61660192, 0.06290714, -444.41277439, -0.00055589, -536.16601917, -0.0303338, -53.61660192, -0.06290714, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 470.5510468, 0.00055589, 567.70078657, 0.0303338, 56.77007866, 0.06290714, -470.5510468, -0.00055589, -567.70078657, -0.0303338, -56.77007866, -0.06290714, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 324.64183787, 0.0111178, 324.64183787, 0.03335339, 227.24928651, -3075.43302593, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 81.16045947, 8.896e-05, 243.4813784, 0.00026688, 811.60459467, 0.00088961, -81.16045947, -8.896e-05, -243.4813784, -0.00026688, -811.60459467, -0.00088961, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 324.64183787, 0.0111178, 324.64183787, 0.03335339, 227.24928651, -3075.43302593, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 81.16045947, 8.896e-05, 243.4813784, 0.00026688, 811.60459467, 0.00088961, -81.16045947, -8.896e-05, -243.4813784, -0.00026688, -811.60459467, -0.00088961, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 21.0, 13.5, 0.0)
    ops.node(121024, 21.0, 13.5, 2.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.2025, 25940069.81257878, 10808362.42190783, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 191.55415027, 0.0005971, 231.54843619, 0.017308, 23.15484362, 0.04028262, -191.55415027, -0.0005971, -231.54843619, -0.017308, -23.15484362, -0.04028262, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 197.03929579, 0.0005971, 238.17881651, 0.017308, 23.81788165, 0.04028262, -197.03929579, -0.0005971, -238.17881651, -0.017308, -23.81788165, -0.04028262, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 164.83157273, 0.01194204, 164.83157273, 0.03582611, 115.38210091, -1452.28319963, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 41.20789318, 7.004e-05, 123.62367955, 0.00021012, 412.07893183, 0.00070039, -41.20789318, -7.004e-05, -123.62367955, -0.00021012, -412.07893183, -0.00070039, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 164.83157273, 0.01194204, 164.83157273, 0.03582611, 115.38210091, -1452.28319963, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 41.20789318, 7.004e-05, 123.62367955, 0.00021012, 412.07893183, 0.00070039, -41.20789318, -7.004e-05, -123.62367955, -0.00021012, -412.07893183, -0.00070039, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.425)
    ops.node(122001, 0.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.16, 27233604.07736643, 11347335.03223602, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 101.98943347, 0.00057645, 123.41785808, 0.01776342, 12.34178581, 0.0494125, -101.98943347, -0.00057645, -123.41785808, -0.01776342, -12.34178581, -0.0494125, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 106.62725791, 0.00057645, 129.03010965, 0.01776342, 12.90301096, 0.0494125, -106.62725791, -0.00057645, -129.03010965, -0.01776342, -12.90301096, -0.0494125, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 144.14762729, 0.01152897, 144.14762729, 0.03458692, 100.9033391, -1482.66288969, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 36.03690682, 6.669e-05, 108.11072047, 0.00020008, 360.36906822, 0.00066692, -36.03690682, -6.669e-05, -108.11072047, -0.00020008, -360.36906822, -0.00066692, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 144.14762729, 0.01152897, 144.14762729, 0.03458692, 100.9033391, -1482.66288969, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 36.03690682, 6.669e-05, 108.11072047, 0.00020008, 360.36906822, 0.00066692, -36.03690682, -6.669e-05, -108.11072047, -0.00020008, -360.36906822, -0.00066692, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.5, 0.0, 3.475)
    ops.node(122002, 4.5, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.3025, 27891106.0640154, 11621294.19333975, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 270.81953794, 0.00051702, 327.91824284, 0.0146812, 32.79182428, 0.03549128, -270.81953794, -0.00051702, -327.91824284, -0.0146812, -32.79182428, -0.03549128, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 248.47063164, 0.00051702, 300.85736629, 0.0146812, 30.08573663, 0.03549128, -248.47063164, -0.00051702, -300.85736629, -0.0146812, -30.08573663, -0.03549128, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 279.66884013, 0.01034033, 279.66884013, 0.031021, 195.76818809, -1663.73439982, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 69.91721003, 6.683e-05, 209.7516301, 0.00020048, 699.17210032, 0.00066826, -69.91721003, -6.683e-05, -209.7516301, -0.00020048, -699.17210032, -0.00066826, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 279.66884013, 0.01034033, 279.66884013, 0.031021, 195.76818809, -1663.73439982, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 69.91721003, 6.683e-05, 209.7516301, 0.00020048, 699.17210032, 0.00066826, -69.91721003, -6.683e-05, -209.7516301, -0.00020048, -699.17210032, -0.00066826, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.5, 0.0, 3.475)
    ops.node(122005, 16.5, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.3025, 26347241.14219429, 10978017.14258096, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 275.28593162, 0.00052032, 333.75646433, 0.01469997, 33.37564643, 0.0341275, -275.28593162, -0.00052032, -333.75646433, -0.01469997, -33.37564643, -0.0341275, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 251.06502081, 0.00052032, 304.39104959, 0.01469997, 30.43910496, 0.0341275, -251.06502081, -0.00052032, -304.39104959, -0.01469997, -30.43910496, -0.0341275, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 263.26374847, 0.01040641, 263.26374847, 0.03121922, 184.28462393, -1677.59243778, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 65.81593712, 6.659e-05, 197.44781135, 0.00019978, 658.15937118, 0.00066592, -65.81593712, -6.659e-05, -197.44781135, -0.00019978, -658.15937118, -0.00066592, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 263.26374847, 0.01040641, 263.26374847, 0.03121922, 184.28462393, -1677.59243778, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 65.81593712, 6.659e-05, 197.44781135, 0.00019978, 658.15937118, 0.00066592, -65.81593712, -6.659e-05, -197.44781135, -0.00019978, -658.15937118, -0.00066592, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 21.0, 0.0, 3.425)
    ops.node(122006, 21.0, 0.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.16, 24854749.48823403, 10356145.62009751, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 100.63120474, 0.00058841, 121.81485844, 0.01654968, 12.18148584, 0.0440517, -100.63120474, -0.00058841, -121.81485844, -0.01654968, -12.18148584, -0.0440517, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 105.23655042, 0.00058841, 127.38966531, 0.01654968, 12.73896653, 0.0440517, -105.23655042, -0.00058841, -127.38966531, -0.01654968, -12.73896653, -0.0440517, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 132.14762697, 0.01176817, 132.14762697, 0.03530452, 92.50333888, -1454.37332227, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 33.03690674, 6.699e-05, 99.11072023, 0.00020097, 330.36906743, 0.00066992, -33.03690674, -6.699e-05, -99.11072023, -0.00020097, -330.36906743, -0.00066992, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 132.14762697, 0.01176817, 132.14762697, 0.03530452, 92.50333888, -1454.37332227, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 33.03690674, 6.699e-05, 99.11072023, 0.00020097, 330.36906743, 0.00066992, -33.03690674, -6.699e-05, -99.11072023, -0.00020097, -330.36906743, -0.00066992, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 4.5, 3.475)
    ops.node(122007, 0.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.3025, 26337233.32473681, 10973847.21864034, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 271.04886231, 0.00052054, 328.62376499, 0.01491929, 32.8623765, 0.03434182, -271.04886231, -0.00052054, -328.62376499, -0.01491929, -32.8623765, -0.03434182, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 247.95715847, 0.00052054, 300.62703188, 0.01491929, 30.06270319, 0.03434182, -247.95715847, -0.00052054, -300.62703188, -0.01491929, -30.06270319, -0.03434182, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 263.4823561, 0.01041083, 263.4823561, 0.0312325, 184.43764927, -1684.77513604, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 65.87058903, 6.667e-05, 197.61176708, 0.00020002, 658.70589025, 0.00066672, -65.87058903, -6.667e-05, -197.61176708, -0.00020002, -658.70589025, -0.00066672, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 263.4823561, 0.01041083, 263.4823561, 0.0312325, 184.43764927, -1684.77513604, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 65.87058903, 6.667e-05, 197.61176708, 0.00020002, 658.70589025, 0.00066672, -65.87058903, -6.667e-05, -197.61176708, -0.00020002, -658.70589025, -0.00066672, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 4.5, 4.5, 3.475)
    ops.node(122008, 4.5, 4.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.4225, 27355811.43813358, 11398254.76588899, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 478.05952676, 0.00049923, 579.22258408, 0.02655332, 57.92225841, 0.06188752, -478.05952676, -0.00049923, -579.22258408, -0.02655332, -57.92225841, -0.06188752, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 433.37511171, 0.00049923, 525.08241762, 0.02655332, 52.50824176, 0.06188752, -433.37511171, -0.00049923, -525.08241762, -0.02655332, -52.50824176, -0.06188752, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 510.02880879, 0.00998457, 510.02880879, 0.02995371, 357.02016615, -3979.83457633, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 127.5072022, 8.896e-05, 382.52160659, 0.00026689, 1275.07202196, 0.00088963, -127.5072022, -8.896e-05, -382.52160659, -0.00026689, -1275.07202196, -0.00088963, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 510.02880879, 0.00998457, 510.02880879, 0.02995371, 357.02016615, -3979.83457633, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 127.5072022, 8.896e-05, 382.52160659, 0.00026689, 1275.07202196, 0.00088963, -127.5072022, -8.896e-05, -382.52160659, -0.00026689, -1275.07202196, -0.00088963, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 9.0, 4.5, 3.475)
    ops.node(122009, 9.0, 4.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.4225, 26854801.90912285, 11189500.79546786, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 448.90046755, 0.00049675, 544.9098392, 0.02730586, 54.49098392, 0.0633878, -448.90046755, -0.00049675, -544.9098392, -0.02730586, -54.49098392, -0.0633878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 405.88232628, 0.00049675, 492.69111783, 0.02730586, 49.26911178, 0.0633878, -405.88232628, -0.00049675, -492.69111783, -0.02730586, -49.26911178, -0.0633878, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 493.13287826, 0.00993508, 493.13287826, 0.02980525, 345.19301479, -3998.41008108, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 123.28321957, 8.762e-05, 369.8496587, 0.00026286, 1232.83219566, 0.00087621, -123.28321957, -8.762e-05, -369.8496587, -0.00026286, -1232.83219566, -0.00087621, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 493.13287826, 0.00993508, 493.13287826, 0.02980525, 345.19301479, -3998.41008108, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 123.28321957, 8.762e-05, 369.8496587, 0.00026286, 1232.83219566, 0.00087621, -123.28321957, -8.762e-05, -369.8496587, -0.00026286, -1232.83219566, -0.00087621, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 12.0, 4.5, 3.475)
    ops.node(122010, 12.0, 4.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.4225, 28040559.15407874, 11683566.31419948, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 456.02812559, 0.00049518, 552.80651302, 0.02696049, 55.2806513, 0.06466357, -456.02812559, -0.00049518, -552.80651302, -0.02696049, -55.2806513, -0.06466357, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 412.03737397, 0.00049518, 499.48003458, 0.02696049, 49.94800346, 0.06466357, -412.03737397, -0.00049518, -499.48003458, -0.02696049, -49.94800346, -0.06466357, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 511.1897311, 0.00990363, 511.1897311, 0.02971089, 357.83281177, -3894.44456544, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 127.79743277, 8.699e-05, 383.39229832, 0.00026096, 1277.97432774, 0.00086988, -127.79743277, -8.699e-05, -383.39229832, -0.00026096, -1277.97432774, -0.00086988, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 511.1897311, 0.00990363, 511.1897311, 0.02971089, 357.83281177, -3894.44456544, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 127.79743277, 8.699e-05, 383.39229832, 0.00026096, 1277.97432774, 0.00086988, -127.79743277, -8.699e-05, -383.39229832, -0.00026096, -1277.97432774, -0.00086988, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 16.5, 4.5, 3.475)
    ops.node(122011, 16.5, 4.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.4225, 26102572.60291864, 10876071.91788276, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 479.18148566, 0.00050608, 581.07155601, 0.02633946, 58.1071556, 0.05964988, -479.18148566, -0.00050608, -581.07155601, -0.02633946, -58.1071556, -0.05964988, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 433.71943292, 0.00050608, 525.94274465, 0.02633946, 52.59427447, 0.05964988, -433.71943292, -0.00050608, -525.94274465, -0.02633946, -52.59427447, -0.05964988, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 488.73148035, 0.01012158, 488.73148035, 0.03036473, 342.11203625, -4018.11002701, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 122.18287009, 8.934e-05, 366.54861027, 0.00026802, 1221.82870089, 0.00089341, -122.18287009, -8.934e-05, -366.54861027, -0.00026802, -1221.82870089, -0.00089341, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 488.73148035, 0.01012158, 488.73148035, 0.03036473, 342.11203625, -4018.11002701, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 122.18287009, 8.934e-05, 366.54861027, 0.00026802, 1221.82870089, 0.00089341, -122.18287009, -8.934e-05, -366.54861027, -0.00026802, -1221.82870089, -0.00089341, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 21.0, 4.5, 3.475)
    ops.node(122012, 21.0, 4.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.3025, 28112536.06001035, 11713556.69167098, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 274.77486816, 0.00051364, 332.62039671, 0.01473359, 33.26203967, 0.03572664, -274.77486816, -0.00051364, -332.62039671, -0.01473359, -33.26203967, -0.03572664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 251.24459449, 0.00051364, 304.1365364, 0.01473359, 30.41365364, 0.03572664, -251.24459449, -0.00051364, -304.1365364, -0.01473359, -30.41365364, -0.03572664, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 282.31799434, 0.01027287, 282.31799434, 0.0308186, 197.62259604, -1667.33417917, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 70.57949859, 6.693e-05, 211.73849576, 0.00020078, 705.79498586, 0.00066927, -70.57949859, -6.693e-05, -211.73849576, -0.00020078, -705.79498586, -0.00066927, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 282.31799434, 0.01027287, 282.31799434, 0.0308186, 197.62259604, -1667.33417917, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 70.57949859, 6.693e-05, 211.73849576, 0.00020078, 705.79498586, 0.00066927, -70.57949859, -6.693e-05, -211.73849576, -0.00020078, -705.79498586, -0.00066927, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 9.0, 3.475)
    ops.node(122013, 0.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.3025, 27235374.89790257, 11348072.87412607, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 273.48159506, 0.00051569, 331.37779797, 0.01506633, 33.1377798, 0.0353421, -273.48159506, -0.00051569, -331.37779797, -0.01506633, -33.1377798, -0.0353421, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 249.87303593, 0.00051569, 302.77129398, 0.01506633, 30.2771294, 0.0353421, -249.87303593, -0.00051569, -302.77129398, -0.01506633, -30.2771294, -0.0353421, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 273.16081467, 0.01031388, 273.16081467, 0.03094164, 191.21257027, -1681.74524353, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 68.29020367, 6.684e-05, 204.870611, 0.00020053, 682.90203667, 0.00066842, -68.29020367, -6.684e-05, -204.870611, -0.00020053, -682.90203667, -0.00066842, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 273.16081467, 0.01031388, 273.16081467, 0.03094164, 191.21257027, -1681.74524353, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 68.29020367, 6.684e-05, 204.870611, 0.00020053, 682.90203667, 0.00066842, -68.29020367, -6.684e-05, -204.870611, -0.00020053, -682.90203667, -0.00066842, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.5, 9.0, 3.475)
    ops.node(122014, 4.5, 9.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.4225, 28261072.16301993, 11775446.73459164, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 480.80457449, 0.00049656, 581.96698883, 0.02646799, 58.19669888, 0.06312859, -480.80457449, -0.00049656, -581.96698883, -0.02646799, -58.19669888, -0.06312859, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 435.79837786, 0.00049656, 527.49138247, 0.02646799, 52.74913825, 0.06312859, -435.79837786, -0.00049656, -527.49138247, -0.02646799, -52.74913825, -0.06312859, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 526.78727967, 0.0099312, 526.78727967, 0.02979361, 368.75109577, -3986.92431958, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 131.69681992, 8.894e-05, 395.09045975, 0.00026683, 1316.96819917, 0.00088943, -131.69681992, -8.894e-05, -395.09045975, -0.00026683, -1316.96819917, -0.00088943, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 526.78727967, 0.0099312, 526.78727967, 0.02979361, 368.75109577, -3986.92431958, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 131.69681992, 8.894e-05, 395.09045975, 0.00026683, 1316.96819917, 0.00088943, -131.69681992, -8.894e-05, -395.09045975, -0.00026683, -1316.96819917, -0.00088943, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 9.0, 9.0, 3.475)
    ops.node(122015, 9.0, 9.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.4225, 28281314.79391966, 11783881.16413319, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 458.67259276, 0.00049159, 555.79841468, 0.02717021, 55.57984147, 0.06512984, -458.67259276, -0.00049159, -555.79841468, -0.02717021, -55.57984147, -0.06512984, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 413.9115287, 0.00049159, 501.55900985, 0.02717021, 50.15590099, 0.06512984, -413.9115287, -0.00049159, -501.55900985, -0.02717021, -50.15590099, -0.06512984, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 519.39564707, 0.00983182, 519.39564707, 0.02949546, 363.57695295, -3996.82035212, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 129.84891177, 8.763e-05, 389.5467353, 0.0002629, 1298.48911767, 0.00087632, -129.84891177, -8.763e-05, -389.5467353, -0.0002629, -1298.48911767, -0.00087632, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 519.39564707, 0.00983182, 519.39564707, 0.02949546, 363.57695295, -3996.82035212, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 129.84891177, 8.763e-05, 389.5467353, 0.0002629, 1298.48911767, 0.00087632, -129.84891177, -8.763e-05, -389.5467353, -0.0002629, -1298.48911767, -0.00087632, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.0, 9.0, 3.475)
    ops.node(122016, 12.0, 9.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.4225, 26726912.51378809, 11136213.5474117, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 456.09239477, 0.00049664, 553.67590207, 0.02678927, 55.36759021, 0.06263057, -456.09239477, -0.00049664, -553.67590207, -0.02678927, -55.36759021, -0.06263057, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 411.17377741, 0.00049664, 499.14669642, 0.02678927, 49.91466964, 0.06263057, -411.17377741, -0.00049664, -499.14669642, -0.02678927, -49.91466964, -0.06263057, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 487.4985961, 0.00993271, 487.4985961, 0.02979814, 341.24901727, -3890.94069877, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 121.87464903, 8.703e-05, 365.62394708, 0.0002611, 1218.74649025, 0.00087034, -121.87464903, -8.703e-05, -365.62394708, -0.0002611, -1218.74649025, -0.00087034, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 487.4985961, 0.00993271, 487.4985961, 0.02979814, 341.24901727, -3890.94069877, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 121.87464903, 8.703e-05, 365.62394708, 0.0002611, 1218.74649025, 0.00087034, -121.87464903, -8.703e-05, -365.62394708, -0.0002611, -1218.74649025, -0.00087034, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 16.5, 9.0, 3.475)
    ops.node(122017, 16.5, 9.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.4225, 27053243.33385048, 11272184.7224377, 0.02513963, 0.01636307, 0.01636307, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 480.94665633, 0.0004977, 582.89947562, 0.02661817, 58.28994756, 0.06153063, -480.94665633, -0.0004977, -582.89947562, -0.02661817, -58.28994756, -0.06153063, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 434.83164154, 0.0004977, 527.00883247, 0.02661817, 52.70088325, 0.06153063, -434.83164154, -0.0004977, -527.00883247, -0.02661817, -52.70088325, -0.06153063, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 507.45797362, 0.00995394, 507.45797362, 0.02986182, 355.22058154, -4069.01756108, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 126.86449341, 8.95e-05, 380.59348022, 0.00026851, 1268.64493406, 0.00089504, -126.86449341, -8.95e-05, -380.59348022, -0.00026851, -1268.64493406, -0.00089504, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 507.45797362, 0.00995394, 507.45797362, 0.02986182, 355.22058154, -4069.01756108, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 126.86449341, 8.95e-05, 380.59348022, 0.00026851, 1268.64493406, 0.00089504, -126.86449341, -8.95e-05, -380.59348022, -0.00026851, -1268.64493406, -0.00089504, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 21.0, 9.0, 3.475)
    ops.node(122018, 21.0, 9.0, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.3025, 25624750.62083347, 10676979.42534728, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 269.67913233, 0.00052005, 327.04836209, 0.01460334, 32.70483621, 0.03332095, -269.67913233, -0.00052005, -327.04836209, -0.01460334, -32.70483621, -0.03332095, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 246.41796664, 0.00052005, 298.83881515, 0.01460334, 29.88388152, 0.03332095, -246.41796664, -0.00052005, -298.83881515, -0.01460334, -29.88388152, -0.03332095, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 255.42786723, 0.01040103, 255.42786723, 0.03120309, 178.79950706, -1677.69351315, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 63.85696681, 6.643e-05, 191.57090042, 0.00019929, 638.56966808, 0.00066431, -63.85696681, -6.643e-05, -191.57090042, -0.00019929, -638.56966808, -0.00066431, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 255.42786723, 0.01040103, 255.42786723, 0.03120309, 178.79950706, -1677.69351315, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 63.85696681, 6.643e-05, 191.57090042, 0.00019929, 638.56966808, 0.00066431, -63.85696681, -6.643e-05, -191.57090042, -0.00019929, -638.56966808, -0.00066431, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 13.5, 3.425)
    ops.node(122019, 0.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.2025, 26463191.30196878, 11026329.70915366, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 143.16646412, 0.0005473, 173.83477026, 0.01791736, 17.38347703, 0.04506799, -143.16646412, -0.0005473, -173.83477026, -0.01791736, -17.38347703, -0.04506799, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 128.31246429, 0.0005473, 155.79883102, 0.01791736, 15.5798831, 0.04506799, -128.31246429, -0.0005473, -155.79883102, -0.01791736, -15.5798831, -0.04506799, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 160.97801914, 0.01094597, 160.97801914, 0.03283792, 112.6846134, -1421.00496421, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 40.24450479, 6.056e-05, 120.73351436, 0.00018168, 402.44504786, 0.00060561, -40.24450479, -6.056e-05, -120.73351436, -0.00018168, -402.44504786, -0.00060561, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 160.97801914, 0.01094597, 160.97801914, 0.03283792, 112.6846134, -1421.00496421, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 40.24450479, 6.056e-05, 120.73351436, 0.00018168, 402.44504786, 0.00060561, -40.24450479, -6.056e-05, -120.73351436, -0.00018168, -402.44504786, -0.00060561, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 4.5, 13.5, 3.475)
    ops.node(122020, 4.5, 13.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.3025, 26821208.68327714, 11175503.61803214, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 273.38476001, 0.00052399, 331.35746343, 0.014699, 33.13574634, 0.03457742, -273.38476001, -0.00052399, -331.35746343, -0.014699, -33.13574634, -0.03457742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 250.19295133, 0.00052399, 303.24770744, 0.014699, 30.32477074, 0.03457742, -250.19295133, -0.00052399, -303.24770744, -0.014699, -30.32477074, -0.03457742, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 268.64741009, 0.01047975, 268.64741009, 0.03143925, 188.05318706, -1681.94844022, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 67.16185252, 6.675e-05, 201.48555757, 0.00020026, 671.61852522, 0.00066753, -67.16185252, -6.675e-05, -201.48555757, -0.00020026, -671.61852522, -0.00066753, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 268.64741009, 0.01047975, 268.64741009, 0.03143925, 188.05318706, -1681.94844022, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 67.16185252, 6.675e-05, 201.48555757, 0.00020026, 671.61852522, 0.00066753, -67.16185252, -6.675e-05, -201.48555757, -0.00020026, -671.61852522, -0.00066753, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 9.0, 13.5, 3.475)
    ops.node(122021, 9.0, 13.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.25, 26533323.29096138, 11055551.37123391, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 218.4545234, 0.00054243, 264.69546867, 0.02540227, 26.46954687, 0.05676763, -218.4545234, -0.00054243, -264.69546867, -0.02540227, -26.46954687, -0.05676763, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 218.4545234, 0.00054243, 264.69546867, 0.02540227, 26.46954687, 0.05676763, -218.4545234, -0.00054243, -264.69546867, -0.02540227, -26.46954687, -0.05676763, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 236.17421497, 0.01084869, 236.17421497, 0.03254606, 165.32195048, -2192.23358951, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 59.04355374, 7.178e-05, 177.13066122, 0.00021533, 590.43553742, 0.00071778, -59.04355374, -7.178e-05, -177.13066122, -0.00021533, -590.43553742, -0.00071778, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 236.17421497, 0.01084869, 236.17421497, 0.03254606, 165.32195048, -2192.23358951, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 59.04355374, 7.178e-05, 177.13066122, 0.00021533, 590.43553742, 0.00071778, -59.04355374, -7.178e-05, -177.13066122, -0.00021533, -590.43553742, -0.00071778, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 12.0, 13.5, 3.475)
    ops.node(122022, 12.0, 13.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.25, 26487986.70970289, 11036661.12904287, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 215.35917488, 0.00054091, 260.95085688, 0.02556295, 26.09508569, 0.05685607, -215.35917488, -0.00054091, -260.95085688, -0.02556295, -26.09508569, -0.05685607, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 215.35917488, 0.00054091, 260.95085688, 0.02556295, 26.09508569, 0.05685607, -215.35917488, -0.00054091, -260.95085688, -0.02556295, -26.09508569, -0.05685607, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 237.98915202, 0.0108182, 237.98915202, 0.0324546, 166.59240641, -2250.34477697, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 59.49728801, 7.245e-05, 178.49186402, 0.00021736, 594.97288005, 0.00072453, -59.49728801, -7.245e-05, -178.49186402, -0.00021736, -594.97288005, -0.00072453, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 237.98915202, 0.0108182, 237.98915202, 0.0324546, 166.59240641, -2250.34477697, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 59.49728801, 7.245e-05, 178.49186402, 0.00021736, 594.97288005, 0.00072453, -59.49728801, -7.245e-05, -178.49186402, -0.00021736, -594.97288005, -0.00072453, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 16.5, 13.5, 3.475)
    ops.node(122023, 16.5, 13.5, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.3025, 26546988.5390944, 11061245.22462267, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 270.10227247, 0.00051455, 327.43677564, 0.01478102, 32.74367756, 0.03440156, -270.10227247, -0.00051455, -327.43677564, -0.01478102, -32.74367756, -0.03440156, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 247.01929266, 0.00051455, 299.45398078, 0.01478102, 29.94539808, 0.03440156, -247.01929266, -0.00051455, -299.45398078, -0.01478102, -29.94539808, -0.03440156, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 265.40485733, 0.01029093, 265.40485733, 0.03087278, 185.78340013, -1676.82352459, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 66.35121433, 6.663e-05, 199.05364299, 0.00019988, 663.51214331, 0.00066628, -66.35121433, -6.663e-05, -199.05364299, -0.00019988, -663.51214331, -0.00066628, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 265.40485733, 0.01029093, 265.40485733, 0.03087278, 185.78340013, -1676.82352459, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 66.35121433, 6.663e-05, 199.05364299, 0.00019988, 663.51214331, 0.00066628, -66.35121433, -6.663e-05, -199.05364299, -0.00019988, -663.51214331, -0.00066628, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 21.0, 13.5, 3.425)
    ops.node(122024, 21.0, 13.5, 5.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.2025, 26532703.90003129, 11055293.29167971, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 146.57657712, 0.00054251, 177.96605027, 0.01772703, 17.79660503, 0.04495945, -146.57657712, -0.00054251, -177.96605027, -0.01772703, -17.79660503, -0.04495945, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 130.49735493, 0.00054251, 158.44345177, 0.01772703, 15.84434518, 0.04495945, -130.49735493, -0.00054251, -158.44345177, -0.01772703, -15.84434518, -0.04495945, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 160.7963033, 0.0108501, 160.7963033, 0.03255031, 112.55741231, -1405.84858362, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 40.19907582, 6.033e-05, 120.59722747, 0.000181, 401.99075824, 0.00060334, -40.19907582, -6.033e-05, -120.59722747, -0.000181, -401.99075824, -0.00060334, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 160.7963033, 0.0108501, 160.7963033, 0.03255031, 112.55741231, -1405.84858362, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 40.19907582, 6.033e-05, 120.59722747, 0.000181, 401.99075824, 0.00060334, -40.19907582, -6.033e-05, -120.59722747, -0.000181, -401.99075824, -0.00060334, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.225)
    ops.node(123001, 0.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.1225, 26688861.56221139, 11120358.98425475, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 60.25278653, 0.00061823, 73.12402017, 0.01917182, 7.31240202, 0.05577923, -60.25278653, -0.00061823, -73.12402017, -0.01917182, -7.31240202, -0.05577923, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 67.26595465, 0.00061823, 81.63534516, 0.01917182, 8.16353452, 0.05577923, -67.26595465, -0.00061823, -81.63534516, -0.01917182, -8.16353452, -0.05577923, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 109.76435744, 0.01236468, 109.76435744, 0.03709403, 76.83505021, -1233.79732155, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 27.44108936, 6.768e-05, 82.32326808, 0.00020305, 274.41089361, 0.00067684, -27.44108936, -6.768e-05, -82.32326808, -0.00020305, -274.41089361, -0.00067684, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 109.76435744, 0.01236468, 109.76435744, 0.03709403, 76.83505021, -1233.79732155, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 27.44108936, 6.768e-05, 82.32326808, 0.00020305, 274.41089361, 0.00067684, -27.44108936, -6.768e-05, -82.32326808, -0.00020305, -274.41089361, -0.00067684, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.5, 0.0, 6.275)
    ops.node(123002, 4.5, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.25, 26897834.17970275, 11207430.90820948, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 178.13343247, 0.0005237, 216.51380379, 0.01586821, 21.65138038, 0.038716, -178.13343247, -0.0005237, -216.51380379, -0.01586821, -21.65138038, -0.038716, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 168.21907106, 0.0005237, 204.46330843, 0.01586821, 20.44633084, 0.038716, -168.21907106, -0.0005237, -204.46330843, -0.01586821, -20.44633084, -0.038716, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 198.49038569, 0.01047396, 198.49038569, 0.03142189, 138.94326998, -1299.25014756, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 49.62259642, 5.951e-05, 148.86778927, 0.00017852, 496.22596423, 0.00059508, -49.62259642, -5.951e-05, -148.86778927, -0.00017852, -496.22596423, -0.00059508, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 198.49038569, 0.01047396, 198.49038569, 0.03142189, 138.94326998, -1299.25014756, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 49.62259642, 5.951e-05, 148.86778927, 0.00017852, 496.22596423, 0.00059508, -49.62259642, -5.951e-05, -148.86778927, -0.00017852, -496.22596423, -0.00059508, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.5, 0.0, 6.275)
    ops.node(123005, 16.5, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.25, 25788174.79244663, 10745072.8301861, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 182.44429847, 0.00053249, 221.96838753, 0.01533741, 22.19683875, 0.03722123, -182.44429847, -0.00053249, -221.96838753, -0.01533741, -22.19683875, -0.03722123, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 171.77605114, 0.00053249, 208.98900874, 0.01533741, 20.89890087, 0.03722123, -171.77605114, -0.00053249, -208.98900874, -0.01533741, -20.89890087, -0.03722123, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 188.32123843, 0.01064972, 188.32123843, 0.03194916, 131.8248669, -1269.5936781, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 47.08030961, 5.889e-05, 141.24092882, 0.00017666, 470.80309608, 0.00058888, -47.08030961, -5.889e-05, -141.24092882, -0.00017666, -470.80309608, -0.00058888, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 188.32123843, 0.01064972, 188.32123843, 0.03194916, 131.8248669, -1269.5936781, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 47.08030961, 5.889e-05, 141.24092882, 0.00017666, 470.80309608, 0.00058888, -47.08030961, -5.889e-05, -141.24092882, -0.00017666, -470.80309608, -0.00058888, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 21.0, 0.0, 6.225)
    ops.node(123006, 21.0, 0.0, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1225, 27697873.8242552, 11540780.76010633, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 61.42260981, 0.00060574, 74.46793477, 0.01865993, 7.44679348, 0.05676726, -61.42260981, -0.00060574, -74.46793477, -0.01865993, -7.44679348, -0.05676726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 69.08307563, 0.00060574, 83.75537908, 0.01865993, 8.37553791, 0.05676726, -69.08307563, -0.00060574, -83.75537908, -0.01865993, -8.37553791, -0.05676726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 111.21809142, 0.01211484, 111.21809142, 0.03634453, 77.852664, -1170.54755269, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 27.80452286, 6.608e-05, 83.41356857, 0.00019825, 278.04522856, 0.00066082, -27.80452286, -6.608e-05, -83.41356857, -0.00019825, -278.04522856, -0.00066082, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 111.21809142, 0.01211484, 111.21809142, 0.03634453, 77.852664, -1170.54755269, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 27.80452286, 6.608e-05, 83.41356857, 0.00019825, 278.04522856, 0.00066082, -27.80452286, -6.608e-05, -83.41356857, -0.00019825, -278.04522856, -0.00066082, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 4.5, 6.225)
    ops.node(123007, 0.0, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.25, 26230690.76793905, 10929454.48664127, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 180.49973539, 0.00052453, 219.49523961, 0.01575831, 21.94952396, 0.03793485, -180.49973539, -0.00052453, -219.49523961, -0.01575831, -21.94952396, -0.03793485, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 170.21637672, 0.00052453, 206.9902447, 0.01575831, 20.69902447, 0.03793485, -170.21637672, -0.00052453, -206.9902447, -0.01575831, -20.69902447, -0.03793485, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 193.20168996, 0.01049053, 193.20168996, 0.03147159, 135.24118297, -1297.06766393, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 48.30042249, 5.94e-05, 144.90126747, 0.00017819, 483.0042249, 0.00059395, -48.30042249, -5.94e-05, -144.90126747, -0.00017819, -483.0042249, -0.00059395, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 193.20168996, 0.01049053, 193.20168996, 0.03147159, 135.24118297, -1297.06766393, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 48.30042249, 5.94e-05, 144.90126747, 0.00017819, 483.0042249, 0.00059395, -48.30042249, -5.94e-05, -144.90126747, -0.00017819, -483.0042249, -0.00059395, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 4.5, 4.5, 6.275)
    ops.node(123008, 4.5, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.3025, 26383840.34136065, 10993266.80890027, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 294.1114026, 0.00053227, 356.94021557, 0.01362611, 35.69402156, 0.03561756, -294.1114026, -0.00053227, -356.94021557, -0.01362611, -35.69402156, -0.03561756, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 276.23440075, 0.00053227, 335.24428391, 0.01362611, 33.52442839, 0.03561756, -276.23440075, -0.00053227, -335.24428391, -0.01362611, -33.52442839, -0.03561756, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 265.27110095, 0.01064545, 265.27110095, 0.03193635, 185.68977067, -1739.8375154, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 66.31777524, 6.701e-05, 198.95332571, 0.00020102, 663.17775238, 0.00067007, -66.31777524, -6.701e-05, -198.95332571, -0.00020102, -663.17775238, -0.00067007, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 265.27110095, 0.01064545, 265.27110095, 0.03193635, 185.68977067, -1739.8375154, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 66.31777524, 6.701e-05, 198.95332571, 0.00020102, 663.17775238, 0.00067007, -66.31777524, -6.701e-05, -198.95332571, -0.00020102, -663.17775238, -0.00067007, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 9.0, 4.5, 6.275)
    ops.node(123009, 9.0, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.3025, 26877483.53855051, 11198951.47439605, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 284.37708099, 0.000528, 345.50193688, 0.01387027, 34.55019369, 0.03734458, -284.37708099, -0.000528, -345.50193688, -0.01387027, -34.55019369, -0.03734458, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 266.14624409, 0.000528, 323.35250965, 0.01387027, 32.33525097, 0.03734458, -266.14624409, -0.000528, -323.35250965, -0.01387027, -32.33525097, -0.03734458, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 264.12286211, 0.01056005, 264.12286211, 0.03168014, 184.88600347, -1647.6142415, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 66.03071553, 6.549e-05, 198.09214658, 0.00019647, 660.30715526, 0.00065491, -66.03071553, -6.549e-05, -198.09214658, -0.00019647, -660.30715526, -0.00065491, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 264.12286211, 0.01056005, 264.12286211, 0.03168014, 184.88600347, -1647.6142415, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 66.03071553, 6.549e-05, 198.09214658, 0.00019647, 660.30715526, 0.00065491, -66.03071553, -6.549e-05, -198.09214658, -0.00019647, -660.30715526, -0.00065491, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 12.0, 4.5, 6.275)
    ops.node(123010, 12.0, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.3025, 25906703.05202293, 10794459.60500956, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 279.66685714, 0.00052915, 340.05425014, 0.01384319, 34.00542501, 0.0364167, -279.66685714, -0.00052915, -340.05425014, -0.01384319, -34.00542501, -0.0364167, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 261.87260759, 0.00052915, 318.41775645, 0.01384319, 31.84177565, 0.0364167, -261.87260759, -0.00052915, -318.41775645, -0.01384319, -31.84177565, -0.0364167, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 254.76863562, 0.01058298, 254.76863562, 0.03174895, 178.33804494, -1672.58000383, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 63.69215891, 6.554e-05, 191.07647672, 0.00019662, 636.92158906, 0.00065539, -63.69215891, -6.554e-05, -191.07647672, -0.00019662, -636.92158906, -0.00065539, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 254.76863562, 0.01058298, 254.76863562, 0.03174895, 178.33804494, -1672.58000383, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 63.69215891, 6.554e-05, 191.07647672, 0.00019662, 636.92158906, 0.00065539, -63.69215891, -6.554e-05, -191.07647672, -0.00019662, -636.92158906, -0.00065539, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 16.5, 4.5, 6.275)
    ops.node(123011, 16.5, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.3025, 25088271.5882031, 10453446.49508462, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 296.46658971, 0.00053532, 359.95381117, 0.01343322, 35.99538112, 0.03400491, -296.46658971, -0.00053532, -359.95381117, -0.01343322, -35.99538112, -0.03400491, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 277.73948256, 0.00053532, 337.21636343, 0.01343322, 33.72163634, 0.03400491, -277.73948256, -0.00053532, -337.21636343, -0.01343322, -33.72163634, -0.03400491, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 252.5992298, 0.01070631, 252.5992298, 0.03211894, 176.81946086, -1766.14746015, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 63.14980745, 6.71e-05, 189.44942235, 0.0002013, 631.4980745, 0.00067101, -63.14980745, -6.71e-05, -189.44942235, -0.0002013, -631.4980745, -0.00067101, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 252.5992298, 0.01070631, 252.5992298, 0.03211894, 176.81946086, -1766.14746015, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 63.14980745, 6.71e-05, 189.44942235, 0.0002013, 631.4980745, 0.00067101, -63.14980745, -6.71e-05, -189.44942235, -0.0002013, -631.4980745, -0.00067101, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 21.0, 4.5, 6.225)
    ops.node(123012, 21.0, 4.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.25, 26375445.95798659, 10989769.14916108, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 179.62167962, 0.00052726, 218.40099535, 0.01557343, 21.84009954, 0.03787761, -179.62167962, -0.00052726, -218.40099535, -0.01557343, -21.84009954, -0.03787761, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 169.59329256, 0.00052726, 206.20753563, 0.01557343, 20.62075356, 0.03787761, -169.59329256, -0.00052726, -206.20753563, -0.01557343, -20.62075356, -0.03787761, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 193.80938707, 0.01054524, 193.80938707, 0.03163573, 135.66657095, -1284.14638408, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 48.45234677, 5.926e-05, 145.3570403, 0.00017777, 484.52346768, 0.00059255, -48.45234677, -5.926e-05, -145.3570403, -0.00017777, -484.52346768, -0.00059255, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 193.80938707, 0.01054524, 193.80938707, 0.03163573, 135.66657095, -1284.14638408, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 48.45234677, 5.926e-05, 145.3570403, 0.00017777, 484.52346768, 0.00059255, -48.45234677, -5.926e-05, -145.3570403, -0.00017777, -484.52346768, -0.00059255, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 9.0, 6.225)
    ops.node(123013, 0.0, 9.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.25, 27143234.15025897, 11309680.89594124, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 179.00438654, 0.00052762, 217.48795406, 0.01564677, 21.74879541, 0.03861628, -179.00438654, -0.00052762, -217.48795406, -0.01564677, -21.74879541, -0.03861628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 169.22969799, 0.00052762, 205.61183718, 0.01564677, 20.56118372, 0.03861628, -169.22969799, -0.00052762, -205.61183718, -0.01564677, -20.56118372, -0.03861628, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 200.04202233, 0.01055241, 200.04202233, 0.03165724, 140.02941563, -1285.49057185, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 50.01050558, 5.943e-05, 150.03151675, 0.00017829, 500.10505584, 0.00059431, -50.01050558, -5.943e-05, -150.03151675, -0.00017829, -500.10505584, -0.00059431, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 200.04202233, 0.01055241, 200.04202233, 0.03165724, 140.02941563, -1285.49057185, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 50.01050558, 5.943e-05, 150.03151675, 0.00017829, 500.10505584, 0.00059431, -50.01050558, -5.943e-05, -150.03151675, -0.00017829, -500.10505584, -0.00059431, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.5, 9.0, 6.275)
    ops.node(123014, 4.5, 9.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.3025, 27452161.96860532, 11438400.82025222, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 296.35367744, 0.0005286, 359.34697886, 0.01366954, 35.93469789, 0.03671466, -296.35367744, -0.0005286, -359.34697886, -0.01366954, -35.93469789, -0.03671466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 278.31568264, 0.0005286, 337.47480574, 0.01366954, 33.74748057, 0.03671466, -278.31568264, -0.0005286, -337.47480574, -0.01366954, -33.74748057, -0.03671466, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 277.63579728, 0.01057207, 277.63579728, 0.03171622, 194.3450581, -1757.34111167, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 69.40894932, 6.74e-05, 208.22684796, 0.0002022, 694.08949321, 0.00067401, -69.40894932, -6.74e-05, -208.22684796, -0.0002022, -694.08949321, -0.00067401, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 277.63579728, 0.01057207, 277.63579728, 0.03171622, 194.3450581, -1757.34111167, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 69.40894932, 6.74e-05, 208.22684796, 0.0002022, 694.08949321, 0.00067401, -69.40894932, -6.74e-05, -208.22684796, -0.0002022, -694.08949321, -0.00067401, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 9.0, 9.0, 6.275)
    ops.node(123015, 9.0, 9.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.3025, 26789130.55022599, 11162137.72926083, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 278.48915779, 0.00051873, 338.33526909, 0.01392195, 33.83352691, 0.03722919, -278.48915779, -0.00051873, -338.33526909, -0.01392195, -33.83352691, -0.03722919, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 260.97315184, 0.00051873, 317.05514947, 0.01392195, 31.70551495, 0.03722919, -260.97315184, -0.00051873, -317.05514947, -0.01392195, -31.70551495, -0.03722919, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 263.57787169, 0.01037467, 263.57787169, 0.03112401, 184.50451018, -1651.54274261, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 65.89446792, 6.557e-05, 197.68340376, 0.00019671, 658.94467922, 0.00065572, -65.89446792, -6.557e-05, -197.68340376, -0.00019671, -658.94467922, -0.00065572, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 263.57787169, 0.01037467, 263.57787169, 0.03112401, 184.50451018, -1651.54274261, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 65.89446792, 6.557e-05, 197.68340376, 0.00019671, 658.94467922, 0.00065572, -65.89446792, -6.557e-05, -197.68340376, -0.00019671, -658.94467922, -0.00065572, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.0, 9.0, 6.275)
    ops.node(123016, 12.0, 9.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.3025, 26687389.72910357, 11119745.72045982, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 283.49721345, 0.00052696, 344.45317945, 0.01399877, 34.44531794, 0.03721484, -283.49721345, -0.00052696, -344.45317945, -0.01399877, -34.44531794, -0.03721484, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 265.46599435, 0.00052696, 322.54498968, 0.01399877, 32.25449897, 0.03721484, -265.46599435, -0.00052696, -322.54498968, -0.01399877, -32.25449897, -0.03721484, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 263.04301612, 0.01053912, 263.04301612, 0.03161737, 184.13011128, -1664.83350507, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 65.76075403, 6.569e-05, 197.28226209, 0.00019706, 657.6075403, 0.00065688, -65.76075403, -6.569e-05, -197.28226209, -0.00019706, -657.6075403, -0.00065688, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 263.04301612, 0.01053912, 263.04301612, 0.03161737, 184.13011128, -1664.83350507, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 65.76075403, 6.569e-05, 197.28226209, 0.00019706, 657.6075403, 0.00065688, -65.76075403, -6.569e-05, -197.28226209, -0.00019706, -657.6075403, -0.00065688, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 16.5, 9.0, 6.275)
    ops.node(123017, 16.5, 9.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.3025, 27361088.28677649, 11400453.45282354, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 298.48309482, 0.00052343, 361.96462264, 0.0134328, 36.19646226, 0.03639634, -298.48309482, -0.00052343, -361.96462264, -0.0134328, -36.19646226, -0.03639634, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 279.81828047, 0.00052343, 339.33016661, 0.0134328, 33.93301666, 0.03639634, -279.81828047, -0.00052343, -339.33016661, -0.0134328, -33.93301666, -0.03639634, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 275.62168666, 0.01046851, 275.62168666, 0.03140554, 192.93518066, -1734.38392517, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 68.90542167, 6.713e-05, 206.716265, 0.0002014, 689.05421666, 0.00067134, -68.90542167, -6.713e-05, -206.716265, -0.0002014, -689.05421666, -0.00067134, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 275.62168666, 0.01046851, 275.62168666, 0.03140554, 192.93518066, -1734.38392517, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 68.90542167, 6.713e-05, 206.716265, 0.0002014, 689.05421666, 0.00067134, -68.90542167, -6.713e-05, -206.716265, -0.0002014, -689.05421666, -0.00067134, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 21.0, 9.0, 6.225)
    ops.node(123018, 21.0, 9.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.25, 26680509.41510691, 11116878.92296121, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 179.12906471, 0.00052391, 217.74892257, 0.01584595, 21.77489226, 0.03843839, -179.12906471, -0.00052391, -217.74892257, -0.01584595, -21.77489226, -0.03843839, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 169.12411121, 0.00052391, 205.58692168, 0.01584595, 20.55869217, 0.03843839, -169.12411121, -0.00052391, -205.58692168, -0.01584595, -20.55869217, -0.03843839, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 197.50960653, 0.01047828, 197.50960653, 0.03143484, 138.25672457, -1314.31107013, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 49.37740163, 5.97e-05, 148.1322049, 0.00017909, 493.77401633, 0.00059696, -49.37740163, -5.97e-05, -148.1322049, -0.00017909, -493.77401633, -0.00059696, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 197.50960653, 0.01047828, 197.50960653, 0.03143484, 138.25672457, -1314.31107013, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 49.37740163, 5.97e-05, 148.1322049, 0.00017909, 493.77401633, 0.00059696, -49.37740163, -5.97e-05, -148.1322049, -0.00017909, -493.77401633, -0.00059696, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 13.5, 6.225)
    ops.node(123019, 0.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1225, 27707894.89182694, 11544956.20492789, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 72.31128976, 0.00062876, 87.66815316, 0.01939626, 8.76681532, 0.05285049, -72.31128976, -0.00062876, -87.66815316, -0.01939626, -8.76681532, -0.05285049, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 68.77620062, 0.00062876, 83.38231152, 0.01939626, 8.33823115, 0.05285049, -68.77620062, -0.00062876, -83.38231152, -0.01939626, -8.33823115, -0.05285049, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 106.40316028, 0.01257529, 106.40316028, 0.03772586, 74.48221219, -1031.87266777, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 26.60079007, 6.32e-05, 79.80237021, 0.00018959, 266.0079007, 0.00063198, -26.60079007, -6.32e-05, -79.80237021, -0.00018959, -266.0079007, -0.00063198, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 106.40316028, 0.01257529, 106.40316028, 0.03772586, 74.48221219, -1031.87266777, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 26.60079007, 6.32e-05, 79.80237021, 0.00018959, 266.0079007, 0.00063198, -26.60079007, -6.32e-05, -79.80237021, -0.00018959, -266.0079007, -0.00063198, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 4.5, 13.5, 6.275)
    ops.node(123020, 4.5, 13.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.25, 27552701.81754821, 11480292.42397842, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 178.91578651, 0.00052792, 217.2908958, 0.01579214, 21.72908958, 0.03914887, -178.91578651, -0.00052792, -217.2908958, -0.01579214, -21.72908958, -0.03914887, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 169.13716191, 0.00052792, 205.4148834, 0.01579214, 20.54148834, 0.03914887, -169.13716191, -0.00052792, -205.4148834, -0.01579214, -20.54148834, -0.03914887, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 203.25531181, 0.01055839, 203.25531181, 0.03167516, 142.27871827, -1285.37102106, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 50.81382795, 5.949e-05, 152.44148386, 0.00017846, 508.13827953, 0.00059488, -50.81382795, -5.949e-05, -152.44148386, -0.00017846, -508.13827953, -0.00059488, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 203.25531181, 0.01055839, 203.25531181, 0.03167516, 142.27871827, -1285.37102106, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 50.81382795, 5.949e-05, 152.44148386, 0.00017846, 508.13827953, 0.00059488, -50.81382795, -5.949e-05, -152.44148386, -0.00017846, -508.13827953, -0.00059488, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 9.0, 13.5, 6.275)
    ops.node(123021, 9.0, 13.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.16, 27406442.89243533, 11419351.20518139, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 111.47773964, 0.00059679, 135.00740224, 0.01601696, 13.50074022, 0.04014858, -111.47773964, -0.00059679, -135.00740224, -0.01601696, -13.50074022, -0.04014858, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 111.47773964, 0.00059679, 135.00740224, 0.01601696, 13.50074022, 0.04014858, -111.47773964, -0.00059679, -135.00740224, -0.01601696, -13.50074022, -0.04014858, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 127.49360288, 0.01193587, 127.49360288, 0.03580761, 89.24552202, -1065.00869968, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 31.87340072, 5.861e-05, 95.62020216, 0.00017584, 318.73400721, 0.00058615, -31.87340072, -5.861e-05, -95.62020216, -0.00017584, -318.73400721, -0.00058615, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 127.49360288, 0.01193587, 127.49360288, 0.03580761, 89.24552202, -1065.00869968, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 31.87340072, 5.861e-05, 95.62020216, 0.00017584, 318.73400721, 0.00058615, -31.87340072, -5.861e-05, -95.62020216, -0.00017584, -318.73400721, -0.00058615, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 12.0, 13.5, 6.275)
    ops.node(123022, 12.0, 13.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.16, 26232237.80671642, 10930099.08613184, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 110.51672595, 0.00060571, 133.94735456, 0.01561379, 13.39473546, 0.03842406, -110.51672595, -0.00060571, -133.94735456, -0.01561379, -13.39473546, -0.03842406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 110.51672595, 0.00060571, 133.94735456, 0.01561379, 13.39473546, 0.03842406, -110.51672595, -0.00060571, -133.94735456, -0.01561379, -13.39473546, -0.03842406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 121.29010784, 0.01211425, 121.29010784, 0.03634274, 84.90307549, -1047.36102491, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 30.32252696, 5.826e-05, 90.96758088, 0.00017478, 303.22526961, 0.00058259, -30.32252696, -5.826e-05, -90.96758088, -0.00017478, -303.22526961, -0.00058259, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 121.29010784, 0.01211425, 121.29010784, 0.03634274, 84.90307549, -1047.36102491, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 30.32252696, 5.826e-05, 90.96758088, 0.00017478, 303.22526961, 0.00058259, -30.32252696, -5.826e-05, -90.96758088, -0.00017478, -303.22526961, -0.00058259, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 16.5, 13.5, 6.275)
    ops.node(123023, 16.5, 13.5, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.25, 26956901.5582561, 11232042.31594004, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 180.13803196, 0.00052358, 218.93599632, 0.01564739, 21.89359963, 0.03854282, -180.13803196, -0.00052358, -218.93599632, -0.01564739, -21.89359963, -0.03854282, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 169.89999258, 0.00052358, 206.49289739, 0.01564739, 20.64928974, 0.03854282, -169.89999258, -0.00052358, -206.49289739, -0.01564739, -20.64928974, -0.03854282, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 198.08121883, 0.01047157, 198.08121883, 0.03141472, 138.65685318, -1278.36452889, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 49.52030471, 5.925e-05, 148.56091412, 0.00017776, 495.20304707, 0.00059255, -49.52030471, -5.925e-05, -148.56091412, -0.00017776, -495.20304707, -0.00059255, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 198.08121883, 0.01047157, 198.08121883, 0.03141472, 138.65685318, -1278.36452889, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 49.52030471, 5.925e-05, 148.56091412, 0.00017776, 495.20304707, 0.00059255, -49.52030471, -5.925e-05, -148.56091412, -0.00017776, -495.20304707, -0.00059255, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 21.0, 13.5, 6.225)
    ops.node(123024, 21.0, 13.5, 8.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.1225, 28020785.52828126, 11675327.30345052, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 73.6271976, 0.00061836, 89.22776873, 0.0191804, 8.92277687, 0.0530111, -73.6271976, -0.00061836, -89.22776873, -0.0191804, -8.92277687, -0.0530111, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 69.84058891, 0.00061836, 84.63883073, 0.0191804, 8.46388307, 0.0530111, -69.84058891, -0.00061836, -84.63883073, -0.0191804, -8.46388307, -0.0530111, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 107.401769, 0.01236727, 107.401769, 0.03710181, 75.1812383, -1028.45119281, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 26.85044225, 6.308e-05, 80.55132675, 0.00018924, 268.5044225, 0.00063079, -26.85044225, -6.308e-05, -80.55132675, -0.00018924, -268.5044225, -0.00063079, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 107.401769, 0.01236727, 107.401769, 0.03710181, 75.1812383, -1028.45119281, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 26.85044225, 6.308e-05, 80.55132675, 0.00018924, 268.5044225, 0.00063079, -26.85044225, -6.308e-05, -80.55132675, -0.00018924, -268.5044225, -0.00063079, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.95)
    ops.node(124001, 0.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.1225, 26106585.30467727, 10877743.87694887, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 48.21078756, 0.00060618, 59.00128445, 0.02119875, 5.90012844, 0.06642849, -48.21078756, -0.00060618, -59.00128445, -0.02119875, -5.90012844, -0.06642849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 41.96280516, 0.00060618, 51.35488401, 0.02119875, 5.1354884, 0.06642849, -41.96280516, -0.00060618, -51.35488401, -0.02119875, -5.1354884, -0.06642849, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 95.70891737, 0.01212351, 95.70891737, 0.03637054, 66.99624216, -1425.26318667, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 23.92722934, 6.033e-05, 71.78168802, 0.000181, 239.27229342, 0.00060333, -23.92722934, -6.033e-05, -71.78168802, -0.000181, -239.27229342, -0.00060333, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 95.70891737, 0.01212351, 95.70891737, 0.03637054, 66.99624216, -1425.26318667, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 23.92722934, 6.033e-05, 71.78168802, 0.000181, 239.27229342, 0.00060333, -23.92722934, -6.033e-05, -71.78168802, -0.000181, -239.27229342, -0.00060333, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.5, 0.0, 8.975)
    ops.node(124002, 4.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.25, 26842956.52266024, 11184565.2177751, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 133.53516207, 0.00049963, 163.25007285, 0.01705555, 16.32500729, 0.04411212, -133.53516207, -0.00049963, -163.25007285, -0.01705555, -16.32500729, -0.04411212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 124.09495015, 0.00049963, 151.70917787, 0.01705555, 15.17091779, 0.04411212, -124.09495015, -0.00049963, -151.70917787, -0.01705555, -15.17091779, -0.04411212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 175.44299053, 0.00999255, 175.44299053, 0.02997765, 122.81009337, -1068.7480108, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 43.86074763, 5.271e-05, 131.5822429, 0.00015812, 438.60747633, 0.00052706, -43.86074763, -5.271e-05, -131.5822429, -0.00015812, -438.60747633, -0.00052706, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 175.44299053, 0.00999255, 175.44299053, 0.02997765, 122.81009337, -1068.7480108, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 43.86074763, 5.271e-05, 131.5822429, 0.00015812, 438.60747633, 0.00052706, -43.86074763, -5.271e-05, -131.5822429, -0.00015812, -438.60747633, -0.00052706, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.5, 0.0, 8.975)
    ops.node(124005, 16.5, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.25, 27388082.48513245, 11411701.03547185, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 135.51215666, 0.00049871, 165.49897418, 0.0168348, 16.54989742, 0.04409705, -135.51215666, -0.00049871, -165.49897418, -0.0168348, -16.54989742, -0.04409705, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 125.80986414, 0.00049871, 153.64970915, 0.0168348, 15.36497092, 0.04409705, -125.80986414, -0.00049871, -153.64970915, -0.0168348, -15.36497092, -0.04409705, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 178.86669901, 0.00997426, 178.86669901, 0.02992279, 125.20668931, -1038.72031147, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 44.71667475, 5.266e-05, 134.15002426, 0.00015799, 447.16674752, 0.00052665, -44.71667475, -5.266e-05, -134.15002426, -0.00015799, -447.16674752, -0.00052665, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 178.86669901, 0.00997426, 178.86669901, 0.02992279, 125.20668931, -1038.72031147, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 44.71667475, 5.266e-05, 134.15002426, 0.00015799, 447.16674752, 0.00052665, -44.71667475, -5.266e-05, -134.15002426, -0.00015799, -447.16674752, -0.00052665, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 21.0, 0.0, 8.95)
    ops.node(124006, 21.0, 0.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1225, 27951067.20068721, 11646278.00028634, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 49.07754733, 0.00058714, 59.86109907, 0.02101862, 5.98610991, 0.06749523, -49.07754733, -0.00058714, -59.86109907, -0.02101862, -5.98610991, -0.06749523, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 42.4641926, 0.00058714, 51.79462664, 0.02101862, 5.17946266, 0.06749523, -42.4641926, -0.00058714, -51.79462664, -0.02101862, -5.17946266, -0.06749523, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 101.60374631, 0.01174282, 101.60374631, 0.03522846, 71.12262241, -1405.28998056, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 25.40093658, 5.982e-05, 76.20280973, 0.00017947, 254.00936577, 0.00059823, -25.40093658, -5.982e-05, -76.20280973, -0.00017947, -254.00936577, -0.00059823, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 101.60374631, 0.01174282, 101.60374631, 0.03522846, 71.12262241, -1405.28998056, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 25.40093658, 5.982e-05, 76.20280973, 0.00017947, 254.00936577, 0.00059823, -25.40093658, -5.982e-05, -76.20280973, -0.00017947, -254.00936577, -0.00059823, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 4.5, 8.975)
    ops.node(124007, 0.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.25, 26591556.82590693, 11079815.34412789, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 134.45631622, 0.0004998, 164.43953287, 0.01714866, 16.44395329, 0.04406038, -134.45631622, -0.0004998, -164.43953287, -0.01714866, -16.44395329, -0.04406038, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 124.88449853, 0.0004998, 152.73323841, 0.01714866, 15.27332384, 0.04406038, -124.88449853, -0.0004998, -152.73323841, -0.01714866, -15.27332384, -0.04406038, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 173.1719327, 0.00999608, 173.1719327, 0.02998823, 121.22035289, -1051.43893902, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 43.29298317, 5.252e-05, 129.87894952, 0.00015755, 432.92983175, 0.00052515, -43.29298317, -5.252e-05, -129.87894952, -0.00015755, -432.92983175, -0.00052515, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 173.1719327, 0.00999608, 173.1719327, 0.02998823, 121.22035289, -1051.43893902, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 43.29298317, 5.252e-05, 129.87894952, 0.00015755, 432.92983175, 0.00052515, -43.29298317, -5.252e-05, -129.87894952, -0.00015755, -432.92983175, -0.00052515, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 4.5, 4.5, 8.975)
    ops.node(124008, 4.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.3025, 25090835.0619092, 10454514.60912883, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 228.77884993, 0.00051852, 279.92982459, 0.01493222, 27.99298246, 0.0408478, -228.77884993, -0.00051852, -279.92982459, -0.01493222, -27.99298246, -0.0408478, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 212.22453068, 0.00051852, 259.67424726, 0.01493222, 25.96742473, 0.0408478, -212.22453068, -0.00051852, -259.67424726, -0.01493222, -25.96742473, -0.0408478, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 222.08733098, 0.01037036, 222.08733098, 0.03111108, 155.46113169, -1398.32490385, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 55.52183275, 5.899e-05, 166.56549824, 0.00017697, 555.21832746, 0.00058989, -55.52183275, -5.899e-05, -166.56549824, -0.00017697, -555.21832746, -0.00058989, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 222.08733098, 0.01037036, 222.08733098, 0.03111108, 155.46113169, -1398.32490385, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 55.52183275, 5.899e-05, 166.56549824, 0.00017697, 555.21832746, 0.00058989, -55.52183275, -5.899e-05, -166.56549824, -0.00017697, -555.21832746, -0.00058989, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 9.0, 4.5, 8.975)
    ops.node(124009, 9.0, 4.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.3025, 27715689.11378571, 11548203.79741071, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 224.61453321, 0.00050247, 273.98331384, 0.01514453, 27.39833138, 0.04318773, -224.61453321, -0.00050247, -273.98331384, -0.01514453, -27.39833138, -0.04318773, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 207.76485676, 0.00050247, 253.43019056, 0.01514453, 25.34301906, 0.04318773, -207.76485676, -0.00050247, -253.43019056, -0.01514453, -25.34301906, -0.04318773, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 245.51520875, 0.01004933, 245.51520875, 0.03014798, 171.86064612, -1397.26377386, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 61.37880219, 5.904e-05, 184.13640656, 0.00017711, 613.78802187, 0.00059036, -61.37880219, -5.904e-05, -184.13640656, -0.00017711, -613.78802187, -0.00059036, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 245.51520875, 0.01004933, 245.51520875, 0.03014798, 171.86064612, -1397.26377386, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 61.37880219, 5.904e-05, 184.13640656, 0.00017711, 613.78802187, 0.00059036, -61.37880219, -5.904e-05, -184.13640656, -0.00017711, -613.78802187, -0.00059036, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 12.0, 4.5, 8.975)
    ops.node(124010, 12.0, 4.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.3025, 27581499.36750476, 11492291.40312698, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 221.36263518, 0.00049787, 270.08688994, 0.01534662, 27.00868899, 0.04333403, -221.36263518, -0.00049787, -270.08688994, -0.01534662, -27.00868899, -0.04333403, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 204.81131407, 0.00049787, 249.89244818, 0.01534662, 24.98924482, 0.04333403, -204.81131407, -0.00049787, -249.89244818, -0.01534662, -24.98924482, -0.04333403, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 243.99848337, 0.00995739, 243.99848337, 0.02987218, 170.79893836, -1394.71865705, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 60.99962084, 5.896e-05, 182.99886253, 0.00017687, 609.99620842, 0.00058957, -60.99962084, -5.896e-05, -182.99886253, -0.00017687, -609.99620842, -0.00058957, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 243.99848337, 0.00995739, 243.99848337, 0.02987218, 170.79893836, -1394.71865705, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 60.99962084, 5.896e-05, 182.99886253, 0.00017687, 609.99620842, 0.00058957, -60.99962084, -5.896e-05, -182.99886253, -0.00017687, -609.99620842, -0.00058957, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 16.5, 4.5, 8.975)
    ops.node(124011, 16.5, 4.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.3025, 27348439.74072105, 11395183.22530044, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 235.07523785, 0.00050288, 286.72087201, 0.01457896, 28.6720872, 0.04182808, -235.07523785, -0.00050288, -286.72087201, -0.01457896, -28.6720872, -0.04182808, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 217.5587969, 0.00050288, 265.35609847, 0.01457896, 26.53560985, 0.04182808, -217.5587969, -0.00050288, -265.35609847, -0.01457896, -26.53560985, -0.04182808, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 244.99568444, 0.01005764, 244.99568444, 0.03017291, 171.49697911, -1381.34312931, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 61.24892111, 5.97e-05, 183.74676333, 0.00017911, 612.48921109, 0.00059702, -61.24892111, -5.97e-05, -183.74676333, -0.00017911, -612.48921109, -0.00059702, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 244.99568444, 0.01005764, 244.99568444, 0.03017291, 171.49697911, -1381.34312931, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 61.24892111, 5.97e-05, 183.74676333, 0.00017911, 612.48921109, 0.00059702, -61.24892111, -5.97e-05, -183.74676333, -0.00017911, -612.48921109, -0.00059702, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 21.0, 4.5, 8.975)
    ops.node(124012, 21.0, 4.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.25, 26522495.82934444, 11051039.92889352, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 132.49665916, 0.00050024, 162.06190901, 0.01730615, 16.2061909, 0.04418925, -132.49665916, -0.00050024, -162.06190901, -0.01730615, -16.2061909, -0.04418925, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 123.25021476, 0.00050024, 150.75221683, 0.01730615, 15.07522168, 0.04418925, -123.25021476, -0.00050024, -150.75221683, -0.01730615, -15.07522168, -0.04418925, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 173.30955199, 0.01000479, 173.30955199, 0.03001437, 121.31668639, -1073.99612678, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 43.327388, 5.269e-05, 129.98216399, 0.00015808, 433.27387997, 0.00052694, -43.327388, -5.269e-05, -129.98216399, -0.00015808, -433.27387997, -0.00052694, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 173.30955199, 0.01000479, 173.30955199, 0.03001437, 121.31668639, -1073.99612678, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 43.327388, 5.269e-05, 129.98216399, 0.00015808, 433.27387997, 0.00052694, -43.327388, -5.269e-05, -129.98216399, -0.00015808, -433.27387997, -0.00052694, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 9.0, 8.975)
    ops.node(124013, 0.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.25, 28278733.56870843, 11782805.65362851, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 133.25030302, 0.00049629, 162.43664751, 0.01697295, 16.24366475, 0.04452819, -133.25030302, -0.00049629, -162.43664751, -0.01697295, -16.24366475, -0.04452819, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 124.01698433, 0.00049629, 151.18091826, 0.01697295, 15.11809183, 0.04452819, -124.01698433, -0.00049629, -151.18091826, -0.01697295, -15.11809183, -0.04452819, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 186.95495338, 0.00992586, 186.95495338, 0.02977757, 130.86846736, -1066.73374183, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 46.73873834, 5.331e-05, 140.21621503, 0.00015994, 467.38738344, 0.00053312, -46.73873834, -5.331e-05, -140.21621503, -0.00015994, -467.38738344, -0.00053312, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 186.95495338, 0.00992586, 186.95495338, 0.02977757, 130.86846736, -1066.73374183, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 46.73873834, 5.331e-05, 140.21621503, 0.00015994, 467.38738344, 0.00053312, -46.73873834, -5.331e-05, -140.21621503, -0.00015994, -467.38738344, -0.00053312, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.5, 9.0, 8.975)
    ops.node(124014, 4.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.3025, 26899858.36208466, 11208274.31753528, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 224.18249656, 0.0005086, 273.65752034, 0.01512428, 27.36575203, 0.04218607, -224.18249656, -0.0005086, -273.65752034, -0.01512428, -27.36575203, -0.04218607, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 208.51364416, 0.0005086, 254.53069572, 0.01512428, 25.45306957, 0.04218607, -208.51364416, -0.0005086, -254.53069572, -0.01512428, -25.45306957, -0.04218607, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 240.68670062, 0.01017192, 240.68670062, 0.03051577, 168.48069043, -1402.13939595, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 60.17167515, 5.963e-05, 180.51502546, 0.00017889, 601.71675155, 0.0005963, -60.17167515, -5.963e-05, -180.51502546, -0.00017889, -601.71675155, -0.0005963, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 240.68670062, 0.01017192, 240.68670062, 0.03051577, 168.48069043, -1402.13939595, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 60.17167515, 5.963e-05, 180.51502546, 0.00017889, 601.71675155, 0.0005963, -60.17167515, -5.963e-05, -180.51502546, -0.00017889, -601.71675155, -0.0005963, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 9.0, 9.0, 8.975)
    ops.node(124015, 9.0, 9.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.3025, 27678370.32265912, 11532654.30110797, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 222.73857677, 0.00050155, 271.66569117, 0.01495177, 27.16656912, 0.04282889, -222.73857677, -0.00050155, -271.66569117, -0.01495177, -27.16656912, -0.04282889, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 206.43396479, 0.00050155, 251.77958187, 0.01495177, 25.17795819, 0.04282889, -206.43396479, -0.00050155, -251.77958187, -0.01495177, -25.17795819, -0.04282889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 245.09777406, 0.01003109, 245.09777406, 0.03009326, 171.56844184, -1364.44883911, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 61.27444351, 5.902e-05, 183.82333054, 0.00017705, 612.74443514, 0.00059015, -61.27444351, -5.902e-05, -183.82333054, -0.00017705, -612.74443514, -0.00059015, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 245.09777406, 0.01003109, 245.09777406, 0.03009326, 171.56844184, -1364.44883911, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 61.27444351, 5.902e-05, 183.82333054, 0.00017705, 612.74443514, 0.00059015, -61.27444351, -5.902e-05, -183.82333054, -0.00017705, -612.74443514, -0.00059015, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.0, 9.0, 8.975)
    ops.node(124016, 12.0, 9.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.3025, 25783029.20447534, 10742928.83519806, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 227.24184184, 0.00050684, 278.02521843, 0.01492672, 27.80252184, 0.04186777, -227.24184184, -0.00050684, -278.02521843, -0.01492672, -27.80252184, -0.04186777, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 209.81990917, 0.00050684, 256.70988056, 0.01492672, 25.67098806, 0.04186777, -209.81990917, -0.00050684, -256.70988056, -0.01492672, -25.67098806, -0.04186777, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 225.84246172, 0.01013675, 225.84246172, 0.03041026, 158.08972321, -1384.58444658, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 56.46061543, 5.838e-05, 169.38184629, 0.00017513, 564.60615431, 0.00058376, -56.46061543, -5.838e-05, -169.38184629, -0.00017513, -564.60615431, -0.00058376, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 225.84246172, 0.01013675, 225.84246172, 0.03041026, 158.08972321, -1384.58444658, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 56.46061543, 5.838e-05, 169.38184629, 0.00017513, 564.60615431, 0.00058376, -56.46061543, -5.838e-05, -169.38184629, -0.00017513, -564.60615431, -0.00058376, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 16.5, 9.0, 8.975)
    ops.node(124017, 16.5, 9.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.3025, 27249964.79293175, 11354151.9970549, 0.01288713, 0.00838807, 0.00838807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 233.2092088, 0.00051149, 284.50878107, 0.01492824, 28.45087811, 0.0421707, -233.2092088, -0.00051149, -284.50878107, -0.01492824, -28.45087811, -0.0421707, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 216.27244126, 0.00051149, 263.84639338, 0.01492824, 26.38463934, 0.0421707, -216.27244126, -0.00051149, -263.84639338, -0.01492824, -26.38463934, -0.0421707, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 244.21676536, 0.01022988, 244.21676536, 0.03068965, 170.95173576, -1396.62070159, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 61.05419134, 5.973e-05, 183.16257402, 0.00017918, 610.54191341, 0.00059728, -61.05419134, -5.973e-05, -183.16257402, -0.00017918, -610.54191341, -0.00059728, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 244.21676536, 0.01022988, 244.21676536, 0.03068965, 170.95173576, -1396.62070159, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 61.05419134, 5.973e-05, 183.16257402, 0.00017918, 610.54191341, 0.00059728, -61.05419134, -5.973e-05, -183.16257402, -0.00017918, -610.54191341, -0.00059728, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 21.0, 9.0, 8.975)
    ops.node(124018, 21.0, 9.0, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.25, 26303059.90471404, 10959608.29363085, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 133.99575049, 0.00050415, 163.96204257, 0.01739447, 16.39620426, 0.04421794, -133.99575049, -0.00050415, -163.96204257, -0.01739447, -16.39620426, -0.04421794, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 124.5206974, 0.00050415, 152.3680252, 0.01739447, 15.23680252, 0.04421794, -124.5206974, -0.00050415, -152.3680252, -0.01739447, -15.23680252, -0.04421794, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 171.28811251, 0.01008293, 171.28811251, 0.0302488, 119.90167876, -1069.1201234, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 42.82202813, 5.251e-05, 128.46608438, 0.00015754, 428.22028127, 0.00052514, -42.82202813, -5.251e-05, -128.46608438, -0.00015754, -428.22028127, -0.00052514, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 171.28811251, 0.01008293, 171.28811251, 0.0302488, 119.90167876, -1069.1201234, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 42.82202813, 5.251e-05, 128.46608438, 0.00015754, 428.22028127, 0.00052514, -42.82202813, -5.251e-05, -128.46608438, -0.00015754, -428.22028127, -0.00052514, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 13.5, 8.95)
    ops.node(124019, 0.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1225, 27031581.40423301, 11263158.91843042, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 52.52783069, 0.00062136, 64.1842231, 0.0213995, 6.41842231, 0.0616773, -52.52783069, -0.00062136, -64.1842231, -0.0213995, -6.41842231, -0.0616773, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 49.49376157, 0.00062136, 60.47686708, 0.0213995, 6.04768671, 0.0616773, -49.49376157, -0.00062136, -60.47686708, -0.0213995, -6.04768671, -0.0616773, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 92.19878606, 0.01242714, 92.19878606, 0.03728143, 64.53915024, -1088.84876856, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 23.04969651, 5.613e-05, 69.14908954, 0.0001684, 230.49696514, 0.00056132, -23.04969651, -5.613e-05, -69.14908954, -0.0001684, -230.49696514, -0.00056132, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 92.19878606, 0.01242714, 92.19878606, 0.03728143, 64.53915024, -1088.84876856, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 23.04969651, 5.613e-05, 69.14908954, 0.0001684, 230.49696514, 0.00056132, -23.04969651, -5.613e-05, -69.14908954, -0.0001684, -230.49696514, -0.00056132, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 4.5, 13.5, 8.975)
    ops.node(124020, 4.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.25, 26984222.45498868, 11243426.02291195, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 133.53240944, 0.00049671, 163.20506545, 0.01686261, 16.32050655, 0.04397406, -133.53240944, -0.00049671, -163.20506545, -0.01686261, -16.32050655, -0.04397406, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 124.03918239, 0.00049671, 151.60231862, 0.01686261, 15.16023186, 0.04397406, -124.03918239, -0.00049671, -151.60231862, -0.01686261, -15.16023186, -0.04397406, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 176.23324487, 0.00993413, 176.23324487, 0.0298024, 123.36327141, -1057.86294288, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 44.05831122, 5.267e-05, 132.17493365, 0.000158, 440.58311217, 0.00052666, -44.05831122, -5.267e-05, -132.17493365, -0.000158, -440.58311217, -0.00052666, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 176.23324487, 0.00993413, 176.23324487, 0.0298024, 123.36327141, -1057.86294288, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 44.05831122, 5.267e-05, 132.17493365, 0.000158, 440.58311217, 0.00052666, -44.05831122, -5.267e-05, -132.17493365, -0.000158, -440.58311217, -0.00052666, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 9.0, 13.5, 8.975)
    ops.node(124021, 9.0, 13.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.16, 27376815.42528432, 11407006.4272018, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 82.28524294, 0.00056846, 100.37042562, 0.01783283, 10.03704256, 0.04765295, -82.28524294, -0.00056846, -100.37042562, -0.01783283, -10.03704256, -0.04765295, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 82.28524294, 0.00056846, 100.37042562, 0.01783283, 10.03704256, 0.04765295, -82.28524294, -0.00056846, -100.37042562, -0.01783283, -10.03704256, -0.04765295, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 112.00647787, 0.01136921, 112.00647787, 0.03410762, 78.40453451, -875.06378927, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 28.00161947, 5.155e-05, 84.0048584, 0.00015465, 280.01619466, 0.0005155, -28.00161947, -5.155e-05, -84.0048584, -0.00015465, -280.01619466, -0.0005155, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 112.00647787, 0.01136921, 112.00647787, 0.03410762, 78.40453451, -875.06378927, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 28.00161947, 5.155e-05, 84.0048584, 0.00015465, 280.01619466, 0.0005155, -28.00161947, -5.155e-05, -84.0048584, -0.00015465, -280.01619466, -0.0005155, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 12.0, 13.5, 8.975)
    ops.node(124022, 12.0, 13.5, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.16, 27988215.76168216, 11661756.56736757, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 82.47055048, 0.00056749, 100.48141942, 0.01761665, 10.04814194, 0.04774881, -82.47055048, -0.00056749, -100.48141942, -0.01761665, -10.04814194, -0.04774881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 82.47055048, 0.00056749, 100.48141942, 0.01761665, 10.04814194, 0.04774881, -82.47055048, -0.00056749, -100.48141942, -0.01761665, -10.04814194, -0.04774881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 113.93163962, 0.0113497, 113.93163962, 0.03404911, 79.75214773, -847.68305493, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 28.4829099, 5.129e-05, 85.44872971, 0.00015387, 284.82909904, 0.00051291, -28.4829099, -5.129e-05, -85.44872971, -0.00015387, -284.82909904, -0.00051291, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 113.93163962, 0.0113497, 113.93163962, 0.03404911, 79.75214773, -847.68305493, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 28.4829099, 5.129e-05, 85.44872971, 0.00015387, 284.82909904, 0.00051291, -28.4829099, -5.129e-05, -85.44872971, -0.00015387, -284.82909904, -0.00051291, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 16.5, 13.5, 8.975)
    ops.node(124023, 16.5, 13.5, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.25, 27822591.95492088, 11592746.6478837, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 132.46068981, 0.00049379, 161.632052, 0.01677053, 16.1632052, 0.04418547, -132.46068981, -0.00049379, -161.632052, -0.01677053, -16.1632052, -0.04418547, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 123.20317362, 0.00049379, 150.33578485, 0.01677053, 15.03357848, 0.04418547, -123.20317362, -0.00049379, -150.33578485, -0.01677053, -15.03357848, -0.04418547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 180.95286076, 0.00987589, 180.95286076, 0.02962768, 126.66700254, -992.87390899, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 45.23821519, 5.245e-05, 135.71464557, 0.00015734, 452.38215191, 0.00052447, -45.23821519, -5.245e-05, -135.71464557, -0.00015734, -452.38215191, -0.00052447, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 180.95286076, 0.00987589, 180.95286076, 0.02962768, 126.66700254, -992.87390899, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 45.23821519, 5.245e-05, 135.71464557, 0.00015734, 452.38215191, 0.00052447, -45.23821519, -5.245e-05, -135.71464557, -0.00015734, -452.38215191, -0.00052447, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 21.0, 13.5, 8.95)
    ops.node(124024, 21.0, 13.5, 11.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.1225, 26362405.82806616, 10984335.76169423, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 53.57552281, 0.00059259, 65.54001197, 0.02154733, 6.5540012, 0.06140968, -53.57552281, -0.00059259, -65.54001197, -0.02154733, -6.5540012, -0.06140968, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 50.12451088, 0.00059259, 61.31831984, 0.02154733, 6.13183198, 0.06140968, -50.12451088, -0.00059259, -61.31831984, -0.02154733, -6.13183198, -0.06140968, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 90.30688364, 0.01185176, 90.30688364, 0.03555528, 63.21481855, -1106.12680417, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 22.57672091, 5.638e-05, 67.73016273, 0.00016913, 225.7672091, 0.00056375, -22.57672091, -5.638e-05, -67.73016273, -0.00016913, -225.7672091, -0.00056375, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 90.30688364, 0.01185176, 90.30688364, 0.03555528, 63.21481855, -1106.12680417, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 22.57672091, 5.638e-05, 67.73016273, 0.00016913, 225.7672091, 0.00056375, -22.57672091, -5.638e-05, -67.73016273, -0.00016913, -225.7672091, -0.00056375, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.0, 0.0, 0.0)
    ops.node(124025, 9.0, 0.0, 1.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.25, 26405404.39190637, 11002251.82996099, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 456.46774309, 0.00053305, 549.98135806, 0.06145039, 54.99813581, 0.16145039, -456.46774309, -0.00053305, -549.98135806, -0.06145039, -54.99813581, -0.16145039, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 418.39712741, 0.00053305, 504.11145985, 0.04067489, 50.41114598, 0.08567258, -418.39712741, -0.00053305, -504.11145985, -0.04067489, -50.41114598, -0.08567258, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 464.9149929, 0.01066096, 464.9149929, 0.03198288, 325.44049503, -7888.5977741, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 116.22874823, 7.86e-05, 348.68624468, 0.00023579, 1162.28748225, 0.00078597, -116.22874823, -7.86e-05, -348.68624468, -0.00023579, -1162.28748225, -0.00078597, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 726.42469739, 0.01066096, 726.42469739, 0.03198288, 508.49728817, -29618.08192862, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 181.60617435, 0.00012281, 544.81852304, 0.00036842, 1816.06174347, 0.00122807, -181.60617435, -0.00012281, -544.81852304, -0.00036842, -1816.06174347, -0.00122807, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 9.0, 0.0, 1.925)
    ops.node(121003, 9.0, 0.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.25, 25422002.01762319, 10592500.84067633, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 303.82784816, 0.00052084, 366.46506165, 0.04722791, 36.64650617, 0.12766851, -303.82784816, -0.00052084, -366.46506165, -0.04722791, -36.64650617, -0.12766851, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 285.45301455, 0.00052084, 344.30206845, 0.03663337, 34.43020685, 0.08033057, -285.45301455, -0.00052084, -344.30206845, -0.03663337, -34.43020685, -0.08033057, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 440.71873062, 0.01041671, 440.71873062, 0.03125014, 308.50311143, -7720.07676588, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 110.17968265, 7.739e-05, 330.53904796, 0.00023217, 1101.79682654, 0.00077388, -110.17968265, -7.739e-05, -330.53904796, -0.00023217, -1101.79682654, -0.00077388, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 569.03766033, 0.01041671, 569.03766033, 0.03125014, 398.32636223, -16987.53553762, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 142.25941508, 9.992e-05, 426.77824525, 0.00029976, 1422.59415082, 0.00099921, -142.25941508, -9.992e-05, -426.77824525, -0.00029976, -1422.59415082, -0.00099921, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.0, 0.0, 0.0)
    ops.node(124026, 12.0, 0.0, 1.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.25, 27150015.24173502, 11312506.35072293, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 459.50316364, 0.00052836, 553.65991228, 0.06219364, 55.36599123, 0.16219364, -459.50316364, -0.00052836, -553.65991228, -0.06219364, -55.36599123, -0.16219364, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 421.13994879, 0.00052836, 507.4356948, 0.04116306, 50.74356948, 0.08853039, -421.13994879, -0.00052836, -507.4356948, -0.04116306, -50.74356948, -0.08853039, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 472.93635005, 0.01056727, 472.93635005, 0.03170181, 331.05544504, -7712.299126, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 118.23408751, 7.776e-05, 354.70226254, 0.00023328, 1182.34087513, 0.0007776, -118.23408751, -7.776e-05, -354.70226254, -0.00023328, -1182.34087513, -0.0007776, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 728.17794455, 0.01056727, 728.17794455, 0.03170181, 509.72456119, -28596.43388142, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 182.04448614, 0.00011973, 546.13345841, 0.00035918, 1820.44486138, 0.00119727, -182.04448614, -0.00011973, -546.13345841, -0.00035918, -1820.44486138, -0.00119727, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 12.0, 0.0, 1.925)
    ops.node(121004, 12.0, 0.0, 2.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.25, 26657018.3080194, 11107090.96167475, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 303.87352113, 0.00051695, 366.65659026, 0.04832119, 36.66565903, 0.1362559, -303.87352113, -0.00051695, -366.65659026, -0.04832119, -36.66565903, -0.1362559, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 285.91869796, 0.00051695, 344.9921352, 0.03747777, 34.49921352, 0.08524595, -285.91869796, -0.00051695, -344.9921352, -0.03747777, -34.49921352, -0.08524595, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 454.80172474, 0.01033904, 454.80172474, 0.03101711, 318.36120732, -7488.45846705, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 113.70043119, 7.616e-05, 341.10129356, 0.00022848, 1137.00431185, 0.00076161, -113.70043119, -7.616e-05, -341.10129356, -0.00022848, -1137.00431185, -0.00076161, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 579.10818265, 0.01033904, 579.10818265, 0.03101711, 405.37572785, -16302.19895416, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 144.77704566, 9.698e-05, 434.33113699, 0.00029093, 1447.77045662, 0.00096978, -144.77704566, -9.698e-05, -434.33113699, -0.00029093, -1447.77045662, -0.00096978, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.0, 0.0, 3.475)
    ops.node(124027, 9.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.25, 26711388.59547016, 11129745.24811256, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 203.66341925, 0.00050272, 246.67481179, 0.04435659, 24.66748118, 0.12052909, -203.66341925, -0.00050272, -246.67481179, -0.04435659, -24.66748118, -0.12052909, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 220.34176605, 0.00050272, 266.87543532, 0.03833932, 26.68754353, 0.09201243, -220.34176605, -0.00050272, -266.87543532, -0.03833932, -26.68754353, -0.09201243, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 436.31662292, 0.01005437, 436.31662292, 0.03016312, 305.42163604, -8451.78590048, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 109.07915573, 6.586e-05, 327.23746719, 0.00019758, 1090.7915573, 0.00065861, -109.07915573, -6.586e-05, -327.23746719, -0.00019758, -1090.7915573, -0.00065861, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 499.40607782, 0.01005437, 499.40607782, 0.03016312, 349.58425447, -13640.8834464, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 124.85151945, 7.538e-05, 374.55455836, 0.00022615, 1248.51519455, 0.00075384, -124.85151945, -7.538e-05, -374.55455836, -0.00022615, -1248.51519455, -0.00075384, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 9.0, 0.0, 4.825)
    ops.node(122003, 9.0, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.25, 27446671.3110828, 11436113.0462845, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 231.54090287, 0.00050472, 280.62988414, 0.0465195, 28.06298841, 0.12830223, -231.54090287, -0.00050472, -280.62988414, -0.0465195, -28.06298841, -0.12830223, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 231.54090287, 0.00050472, 280.62988414, 0.04020572, 28.06298841, 0.09783195, -231.54090287, -0.00050472, -280.62988414, -0.04020572, -28.06298841, -0.09783195, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 441.6885687, 0.01009438, 441.6885687, 0.03028314, 309.18199809, -8738.46881906, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 110.42214218, 6.489e-05, 331.26642653, 0.00019466, 1104.22142175, 0.00064885, -110.42214218, -6.489e-05, -331.26642653, -0.00019466, -1104.22142175, -0.00064885, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 506.02609084, 0.01009438, 506.02609084, 0.03028314, 354.21826358, -14442.17349277, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 126.50652271, 7.434e-05, 379.51956813, 0.00022301, 1265.06522709, 0.00074337, -126.50652271, -7.434e-05, -379.51956813, -0.00022301, -1265.06522709, -0.00074337, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.0, 0.0, 3.475)
    ops.node(124028, 12.0, 0.0, 4.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.25, 26581815.53040947, 11075756.47100395, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 203.35557294, 0.00050243, 246.31879931, 0.04446026, 24.63187993, 0.12013228, -203.35557294, -0.00050243, -246.31879931, -0.04446026, -24.63187993, -0.12013228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 220.04172154, 0.00050243, 266.53025469, 0.03842872, 26.65302547, 0.09174918, -220.04172154, -0.00050243, -266.53025469, -0.03842872, -26.65302547, -0.09174918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 438.63270196, 0.01004859, 438.63270196, 0.03014577, 307.04289137, -8758.06168215, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 109.65817549, 6.653e-05, 328.97452647, 0.0001996, 1096.5817549, 0.00066533, -109.65817549, -6.653e-05, -328.97452647, -0.0001996, -1096.5817549, -0.00066533, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 503.816952, 0.01004859, 503.816952, 0.03014577, 352.6718664, -14225.46993699, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 125.954238, 7.642e-05, 377.862714, 0.00022926, 1259.54238, 0.0007642, -125.954238, -7.642e-05, -377.862714, -0.00022926, -1259.54238, -0.0007642, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 12.0, 0.0, 4.825)
    ops.node(122004, 12.0, 0.0, 5.525)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.25, 27660153.34724265, 11525063.89468444, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 229.96832909, 0.00050345, 278.65938247, 0.04672304, 27.86593825, 0.12920168, -229.96832909, -0.00050345, -278.65938247, -0.04672304, -27.86593825, -0.12920168, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 229.96832909, 0.00050345, 278.65938247, 0.04038116, 27.86593825, 0.09849775, -229.96832909, -0.00050345, -278.65938247, -0.04038116, -27.86593825, -0.09849775, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 447.43429329, 0.01006901, 447.43429329, 0.03020704, 313.2040053, -8943.53239965, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 111.85857332, 6.522e-05, 335.57571997, 0.00019567, 1118.58573323, 0.00065222, -111.85857332, -6.522e-05, -335.57571997, -0.00019567, -1118.58573323, -0.00065222, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 513.08584837, 0.01006901, 513.08584837, 0.03020704, 359.16009386, -14837.99395871, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 128.27146209, 7.479e-05, 384.81438628, 0.00022438, 1282.71462093, 0.00074792, -128.27146209, -7.479e-05, -384.81438628, -0.00022438, -1282.71462093, -0.00074792, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.0, 0.0, 6.275)
    ops.node(124029, 9.0, 0.0, 7.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.16, 26881539.53745082, 11200641.47393784, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 112.28901167, 0.000523, 136.02293818, 0.04172902, 13.60229382, 0.10766725, -112.28901167, -0.000523, -136.02293818, -0.04172902, -13.60229382, -0.10766725, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 112.28901167, 0.000523, 136.02293818, 0.04172902, 13.60229382, 0.10766725, -112.28901167, -0.000523, -136.02293818, -0.04172902, -13.60229382, -0.10766725, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 282.37424827, 0.01045992, 282.37424827, 0.03137975, 197.66197379, -6944.10839741, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 70.59356207, 6.618e-05, 211.7806862, 0.00019853, 705.93562067, 0.00066178, -70.59356207, -6.618e-05, -211.7806862, -0.00019853, -705.93562067, -0.00066178, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 282.37424827, 0.01045992, 282.37424827, 0.03137975, 197.66197379, -6944.10839741, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 70.59356207, 6.618e-05, 211.7806862, 0.00019853, 705.93562067, 0.00066178, -70.59356207, -6.618e-05, -211.7806862, -0.00019853, -705.93562067, -0.00066178, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 9.0, 0.0, 7.575)
    ops.node(123003, 9.0, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.16, 26242168.98445798, 10934237.07685749, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 105.07797248, 0.00051301, 127.6140393, 0.04314283, 12.76140393, 0.11136427, -105.07797248, -0.00051301, -127.6140393, -0.04314283, -12.76140393, -0.11136427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 105.07797248, 0.00051301, 127.6140393, 0.04314283, 12.76140393, 0.11136427, -105.07797248, -0.00051301, -127.6140393, -0.04314283, -12.76140393, -0.11136427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 272.04650967, 0.01026014, 272.04650967, 0.03078043, 190.43255677, -7446.80455097, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 68.01162742, 6.531e-05, 204.03488225, 0.00019593, 680.11627418, 0.00065311, -68.01162742, -6.531e-05, -204.03488225, -0.00019593, -680.11627418, -0.00065311, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 272.04650967, 0.01026014, 272.04650967, 0.03078043, 190.43255677, -7446.80455097, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 68.01162742, 6.531e-05, 204.03488225, 0.00019593, 680.11627418, 0.00065311, -68.01162742, -6.531e-05, -204.03488225, -0.00019593, -680.11627418, -0.00065311, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.0, 0.0, 6.275)
    ops.node(124030, 12.0, 0.0, 7.025)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.16, 27188326.80541951, 11328469.50225813, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 111.00131666, 0.00052365, 134.43262583, 0.04209218, 13.44326258, 0.10898595, -111.00131666, -0.00052365, -134.43262583, -0.04209218, -13.44326258, -0.10898595, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 111.00131666, 0.00052365, 134.43262583, 0.04209218, 13.44326258, 0.10898595, -111.00131666, -0.00052365, -134.43262583, -0.04209218, -13.44326258, -0.10898595, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 287.37729624, 0.01047298, 287.37729624, 0.03141895, 201.16410737, -7143.7122597, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 71.84432406, 6.659e-05, 215.53297218, 0.00019977, 718.44324061, 0.0006659, -71.84432406, -6.659e-05, -215.53297218, -0.00019977, -718.44324061, -0.0006659, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 287.37729624, 0.01047298, 287.37729624, 0.03141895, 201.16410737, -7143.7122597, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 71.84432406, 6.659e-05, 215.53297218, 0.00019977, 718.44324061, 0.0006659, -71.84432406, -6.659e-05, -215.53297218, -0.00019977, -718.44324061, -0.0006659, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 12.0, 0.0, 7.575)
    ops.node(123004, 12.0, 0.0, 8.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.16, 25947705.68861183, 10811544.0369216, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 102.75721696, 0.00051209, 124.81702253, 0.04298988, 12.48170225, 0.11029302, -102.75721696, -0.00051209, -124.81702253, -0.04298988, -12.48170225, -0.11029302, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 102.75721696, 0.00051209, 124.81702253, 0.04298988, 12.48170225, 0.11029302, -102.75721696, -0.00051209, -124.81702253, -0.04298988, -12.48170225, -0.11029302, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 270.90304359, 0.01024173, 270.90304359, 0.0307252, 189.63213051, -7567.35576126, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 67.7257609, 6.577e-05, 203.17728269, 0.00019732, 677.25760897, 0.00065774, -67.7257609, -6.577e-05, -203.17728269, -0.00019732, -677.25760897, -0.00065774, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 270.90304359, 0.01024173, 270.90304359, 0.0307252, 189.63213051, -7567.35576126, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 67.7257609, 6.577e-05, 203.17728269, 0.00019732, 677.25760897, 0.00065774, -67.7257609, -6.577e-05, -203.17728269, -0.00019732, -677.25760897, -0.00065774, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.0, 0.0, 8.975)
    ops.node(124031, 9.0, 0.0, 9.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.16, 27143555.57800379, 11309814.82416824, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 81.3601039, 0.00049946, 99.28379882, 0.01773904, 9.92837988, 0.04744549, -81.3601039, -0.00049946, -99.28379882, -0.01773904, -9.92837988, -0.04744549, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 81.3601039, 0.00049946, 99.28379882, 0.01773904, 9.92837988, 0.04744549, -81.3601039, -0.00049946, -99.28379882, -0.01773904, -9.92837988, -0.04744549, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 179.9051449, 0.00998926, 179.9051449, 0.02996777, 125.93360143, -1675.70018054, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 44.97628623, 4.176e-05, 134.92885868, 0.00012527, 449.76286225, 0.00041756, -44.97628623, -4.176e-05, -134.92885868, -0.00012527, -449.76286225, -0.00041756, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 179.9051449, 0.00998926, 179.9051449, 0.02996777, 125.93360143, -1675.70018054, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 44.97628623, 4.176e-05, 134.92885868, 0.00012527, 449.76286225, 0.00041756, -44.97628623, -4.176e-05, -134.92885868, -0.00012527, -449.76286225, -0.00041756, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 9.0, 0.0, 10.325)
    ops.node(124003, 9.0, 0.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.16, 26277960.01272812, 10949150.00530338, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 74.80553867, 0.00048875, 91.60288461, 0.01894021, 9.16028846, 0.0500311, -74.80553867, -0.00048875, -91.60288461, -0.01894021, -9.16028846, -0.0500311, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 74.80553867, 0.00048875, 91.60288461, 0.01894021, 9.16028846, 0.0500311, -74.80553867, -0.00048875, -91.60288461, -0.01894021, -9.16028846, -0.0500311, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 164.91943252, 0.00977507, 164.91943252, 0.02932521, 115.44360277, -1765.12037229, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 41.22985813, 3.954e-05, 123.68957439, 0.00011862, 412.29858131, 0.00039539, -41.22985813, -3.954e-05, -123.68957439, -0.00011862, -412.29858131, -0.00039539, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 164.91943252, 0.00977507, 164.91943252, 0.02932521, 115.44360277, -1765.12037229, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 41.22985813, 3.954e-05, 123.68957439, 0.00011862, 412.29858131, 0.00039539, -41.22985813, -3.954e-05, -123.68957439, -0.00011862, -412.29858131, -0.00039539, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.0, 0.0, 8.975)
    ops.node(124032, 12.0, 0.0, 9.875)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.16, 26868556.6169318, 11195231.92372158, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 81.02333786, 0.00049536, 98.91830903, 0.0179667, 9.8918309, 0.04751922, -81.02333786, -0.00049536, -98.91830903, -0.0179667, -9.8918309, -0.04751922, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 81.02333786, 0.00049536, 98.91830903, 0.0179667, 9.8918309, 0.04751922, -81.02333786, -0.00049536, -98.91830903, -0.0179667, -9.8918309, -0.04751922, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 177.64618503, 0.00990726, 177.64618503, 0.02972178, 124.35232952, -1674.48667855, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 44.41154626, 4.165e-05, 133.23463877, 0.00012496, 444.11546258, 0.00041654, -44.41154626, -4.165e-05, -133.23463877, -0.00012496, -444.11546258, -0.00041654, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 177.64618503, 0.00990726, 177.64618503, 0.02972178, 124.35232952, -1674.48667855, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 44.41154626, 4.165e-05, 133.23463877, 0.00012496, 444.11546258, 0.00041654, -44.41154626, -4.165e-05, -133.23463877, -0.00012496, -444.11546258, -0.00041654, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 12.0, 0.0, 10.325)
    ops.node(124004, 12.0, 0.0, 11.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.16, 26349437.50196258, 10978932.29248441, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 73.83670861, 0.00049302, 90.40535235, 0.01881206, 9.04053523, 0.04993236, -73.83670861, -0.00049302, -90.40535235, -0.01881206, -9.04053523, -0.04993236, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 73.83670861, 0.00049302, 90.40535235, 0.01881206, 9.04053523, 0.04993236, -73.83670861, -0.00049302, -90.40535235, -0.01881206, -9.04053523, -0.04993236, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 166.29366234, 0.00986034, 166.29366234, 0.02958103, 116.40556364, -1832.98116381, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 41.57341559, 3.976e-05, 124.72024676, 0.00011928, 415.73415586, 0.0003976, -41.57341559, -3.976e-05, -124.72024676, -0.00011928, -415.73415586, -0.0003976, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 166.29366234, 0.00986034, 166.29366234, 0.02958103, 116.40556364, -1832.98116381, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 41.57341559, 3.976e-05, 124.72024676, 0.00011928, 415.73415586, 0.0003976, -41.57341559, -3.976e-05, -124.72024676, -0.00011928, -415.73415586, -0.0003976, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
