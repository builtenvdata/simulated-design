import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 8.3, 0.0, 0.0)
    ops.node(121003, 8.3, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.1225, 27822730.79933828, 11592804.49972428, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 174.00666598, 0.00120294, 207.19549918, 0.0129848, 20.71954992, 0.0354587, -174.00666598, -0.00120294, -207.19549918, -0.0129848, -20.71954992, -0.0354587, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 186.98576609, 0.00120294, 222.65014348, 0.0129848, 22.26501435, 0.0354587, -186.98576609, -0.00120294, -222.65014348, -0.0129848, -22.26501435, -0.0354587, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 161.78944701, 0.02405876, 161.78944701, 0.07217629, 113.25261291, -1693.46120511, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 40.44736175, 0.00012646, 121.34208526, 0.00037938, 404.47361754, 0.00126459, -40.44736175, -0.00012646, -121.34208526, -0.00037938, -404.47361754, -0.00126459, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 161.78944701, 0.02405876, 161.78944701, 0.07217629, 113.25261291, -1693.46120511, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 40.44736175, 0.00012646, 121.34208526, 0.00037938, 404.47361754, 0.00126459, -40.44736175, -0.00012646, -121.34208526, -0.00037938, -404.47361754, -0.00126459, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.65, 0.0, 0.0)
    ops.node(121004, 13.65, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.0625, 29604556.89257659, 12335232.03857358, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 71.9005097, 0.00170248, 85.22719881, 0.01469711, 8.52271988, 0.04398326, -71.9005097, -0.00170248, -85.22719881, -0.01469711, -8.52271988, -0.04398326, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 71.9005097, 0.00170248, 85.22719881, 0.01469711, 8.52271988, 0.04398326, -71.9005097, -0.00170248, -85.22719881, -0.01469711, -8.52271988, -0.04398326, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 104.02740168, 0.0340496, 104.02740168, 0.1021488, 72.81918117, -1191.25035821, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 26.00685042, 0.00014978, 78.02055126, 0.00044933, 260.06850419, 0.00149776, -26.00685042, -0.00014978, -78.02055126, -0.00044933, -260.06850419, -0.00149776, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 104.02740168, 0.0340496, 104.02740168, 0.1021488, 72.81918117, -1191.25035821, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 26.00685042, 0.00014978, 78.02055126, 0.00044933, 260.06850419, 0.00149776, -26.00685042, -0.00014978, -78.02055126, -0.00044933, -260.06850419, -0.00149776, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.25, 0.0)
    ops.node(121005, 0.0, 4.25, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.09, 29350185.11536952, 12229243.79807063, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 107.1060282, 0.00132899, 127.79071042, 0.01481826, 12.77907104, 0.04501725, -107.1060282, -0.00132899, -127.79071042, -0.01481826, -12.77907104, -0.04501725, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 117.44392828, 0.00132899, 140.1251011, 0.01481826, 14.01251011, 0.04501725, -117.44392828, -0.00132899, -140.1251011, -0.01481826, -14.01251011, -0.04501725, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 129.9779366, 0.02657972, 129.9779366, 0.07973915, 90.98455562, -1377.75280552, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 32.49448415, 0.00013108, 97.48345245, 0.00039325, 324.9448415, 0.00131084, -32.49448415, -0.00013108, -97.48345245, -0.00039325, -324.9448415, -0.00131084, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 129.9779366, 0.02657972, 129.9779366, 0.07973915, 90.98455562, -1377.75280552, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 32.49448415, 0.00013108, 97.48345245, 0.00039325, 324.9448415, 0.00131084, -32.49448415, -0.00013108, -97.48345245, -0.00039325, -324.9448415, -0.00131084, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 2.95, 4.25, 0.0)
    ops.node(121006, 2.95, 4.25, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.16, 29316645.48374938, 12215268.95156224, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 282.9636284, 0.00109065, 338.2083476, 0.01282057, 33.82083476, 0.03170744, -282.9636284, -0.00109065, -338.2083476, -0.01282057, -33.82083476, -0.03170744, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 310.86120715, 0.00109065, 371.55254121, 0.01282057, 37.15525412, 0.03170744, -310.86120715, -0.00109065, -371.55254121, -0.01282057, -37.15525412, -0.03170744, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 180.30951253, 0.02181307, 180.30951253, 0.0654392, 126.21665877, -1527.04294848, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 45.07737813, 0.0001024, 135.2321344, 0.00030721, 450.77378132, 0.00102404, -45.07737813, -0.0001024, -135.2321344, -0.00030721, -450.77378132, -0.00102404, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 180.30951253, 0.02181307, 180.30951253, 0.0654392, 126.21665877, -1527.04294848, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 45.07737813, 0.0001024, 135.2321344, 0.00030721, 450.77378132, 0.00102404, -45.07737813, -0.0001024, -135.2321344, -0.00030721, -450.77378132, -0.00102404, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 8.3, 4.25, 0.0)
    ops.node(121007, 8.3, 4.25, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.16, 29108038.54940441, 12128349.39558517, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 297.75726579, 0.00111321, 355.15286296, 0.01190191, 35.5152863, 0.02935333, -297.75726579, -0.00111321, -355.15286296, -0.01190191, -35.5152863, -0.02935333, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 327.15687399, 0.00111321, 390.21953042, 0.01190191, 39.02195304, 0.02935333, -327.15687399, -0.00111321, -390.21953042, -0.01190191, -39.02195304, -0.02935333, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 180.88493613, 0.0222643, 180.88493613, 0.0667929, 126.61945529, -1565.89521924, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 45.22123403, 0.00010347, 135.6637021, 0.0003104, 452.21234033, 0.00103467, -45.22123403, -0.00010347, -135.6637021, -0.0003104, -452.21234033, -0.00103467, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 180.88493613, 0.0222643, 180.88493613, 0.0667929, 126.61945529, -1565.89521924, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 45.22123403, 0.00010347, 135.6637021, 0.0003104, 452.21234033, 0.00103467, -45.22123403, -0.00010347, -135.6637021, -0.0003104, -452.21234033, -0.00103467, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 13.65, 4.25, 0.0)
    ops.node(121008, 13.65, 4.25, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.1225, 28772788.93017679, 11988662.05424033, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 182.61008347, 0.001213, 217.76069624, 0.01410061, 21.77606962, 0.03626602, -182.61008347, -0.001213, -217.76069624, -0.01410061, -21.77606962, -0.03626602, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 203.25801524, 0.001213, 242.38314815, 0.01410061, 24.23831482, 0.03626602, -203.25801524, -0.001213, -242.38314815, -0.01410061, -24.23831482, -0.03626602, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 155.4356422, 0.02425993, 155.4356422, 0.07277979, 108.80494954, -1509.1038039, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 38.85891055, 0.00011748, 116.57673165, 0.00035244, 388.58910549, 0.00117481, -38.85891055, -0.00011748, -116.57673165, -0.00035244, -388.58910549, -0.00117481, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 155.4356422, 0.02425993, 155.4356422, 0.07277979, 108.80494954, -1509.1038039, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 38.85891055, 0.00011748, 116.57673165, 0.00035244, 388.58910549, 0.00117481, -38.85891055, -0.00011748, -116.57673165, -0.00035244, -388.58910549, -0.00117481, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.5, 0.0)
    ops.node(121009, 0.0, 8.5, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.09, 29763744.8946366, 12401560.37276525, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 104.35246643, 0.00133645, 124.64778239, 0.01530461, 12.46477824, 0.04766617, -104.35246643, -0.00133645, -124.64778239, -0.01530461, -12.46477824, -0.04766617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 114.2554589, 0.00133645, 136.47678934, 0.01530461, 13.64767893, 0.04766617, -114.2554589, -0.00133645, -136.47678934, -0.01530461, -13.64767893, -0.04766617, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 129.20094136, 0.02672905, 129.20094136, 0.08018715, 90.44065895, -1349.49373484, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 32.30023534, 0.00012849, 96.90070602, 0.00038547, 323.0023534, 0.0012849, -32.30023534, -0.00012849, -96.90070602, -0.00038547, -323.0023534, -0.0012849, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 129.20094136, 0.02672905, 129.20094136, 0.08018715, 90.44065895, -1349.49373484, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 32.30023534, 0.00012849, 96.90070602, 0.00038547, 323.0023534, 0.0012849, -32.30023534, -0.00012849, -96.90070602, -0.00038547, -323.0023534, -0.0012849, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 2.95, 8.5, 0.0)
    ops.node(121010, 2.95, 8.5, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.1225, 29032683.72199382, 12096951.55083076, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 197.51781805, 0.00124698, 235.40937362, 0.0139359, 23.54093736, 0.03620443, -197.51781805, -0.00124698, -235.40937362, -0.0139359, -23.54093736, -0.03620443, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 210.8313212, 0.00124698, 251.27692151, 0.0139359, 25.12769215, 0.03620443, -210.8313212, -0.00124698, -251.27692151, -0.0139359, -25.12769215, -0.03620443, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 156.79691517, 0.02493952, 156.79691517, 0.07481857, 109.75784062, -1514.36887885, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 39.19922879, 0.00011745, 117.59768638, 0.00035235, 391.99228793, 0.00117449, -39.19922879, -0.00011745, -117.59768638, -0.00035235, -391.99228793, -0.00117449, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 156.79691517, 0.02493952, 156.79691517, 0.07481857, 109.75784062, -1514.36887885, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 39.19922879, 0.00011745, 117.59768638, 0.00035235, 391.99228793, 0.00117449, -39.19922879, -0.00011745, -117.59768638, -0.00035235, -391.99228793, -0.00117449, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.3, 8.5, 0.0)
    ops.node(121011, 8.3, 8.5, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 28948284.03663175, 12061785.01526323, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 295.92522052, 0.0011102, 352.97193146, 0.01195016, 35.29719315, 0.02918248, -295.92522052, -0.0011102, -352.97193146, -0.01195016, -35.29719315, -0.02918248, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 325.04436937, 0.0011102, 387.70449732, 0.01195016, 38.77044973, 0.02918248, -325.04436937, -0.0011102, -387.70449732, -0.01195016, -38.77044973, -0.02918248, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 180.3762365, 0.02220396, 180.3762365, 0.06661187, 126.26336555, -1571.35172146, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 45.09405912, 0.00010375, 135.28217737, 0.00031124, 450.94059125, 0.00103746, -45.09405912, -0.00010375, -135.28217737, -0.00031124, -450.94059125, -0.00103746, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 180.3762365, 0.02220396, 180.3762365, 0.06661187, 126.26336555, -1571.35172146, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 45.09405912, 0.00010375, 135.28217737, 0.00031124, 450.94059125, 0.00103746, -45.09405912, -0.00010375, -135.28217737, -0.00031124, -450.94059125, -0.00103746, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 13.65, 8.5, 0.0)
    ops.node(121012, 13.65, 8.5, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 29768114.55131588, 12403381.06304828, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 179.03263092, 0.00122893, 213.45311552, 0.01441611, 21.34531155, 0.03834994, -179.03263092, -0.00122893, -213.45311552, -0.01441611, -21.34531155, -0.03834994, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 197.41293256, 0.00122893, 235.36718018, 0.01441611, 23.53671802, 0.03834994, -197.41293256, -0.00122893, -235.36718018, -0.01441611, -23.53671802, -0.03834994, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 159.44305555, 0.02457862, 159.44305555, 0.07373587, 111.61013888, -1507.91553906, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 39.86076389, 0.00011648, 119.58229166, 0.00034944, 398.60763887, 0.0011648, -39.86076389, -0.00011648, -119.58229166, -0.00034944, -398.60763887, -0.0011648, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 159.44305555, 0.02457862, 159.44305555, 0.07373587, 111.61013888, -1507.91553906, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 39.86076389, 0.00011648, 119.58229166, 0.00034944, 398.60763887, 0.0011648, -39.86076389, -0.00011648, -119.58229166, -0.00034944, -398.60763887, -0.0011648, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 12.75, 0.0)
    ops.node(121013, 0.0, 12.75, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.09, 29558680.10729924, 12316116.71137469, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 105.13673796, 0.00131742, 125.60111101, 0.0152646, 12.5601111, 0.04718843, -105.13673796, -0.00131742, -125.60111101, -0.0152646, -12.5601111, -0.04718843, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 115.60968886, 0.00131742, 138.1125727, 0.0152646, 13.81125727, 0.04718843, -115.60968886, -0.00131742, -138.1125727, -0.0152646, -13.81125727, -0.04718843, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 129.41349123, 0.02634848, 129.41349123, 0.07904545, 90.58944386, -1366.51157446, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 32.35337281, 0.00012959, 97.06011842, 0.00038878, 323.53372808, 0.00129594, -32.35337281, -0.00012959, -97.06011842, -0.00038878, -323.53372808, -0.00129594, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 129.41349123, 0.02634848, 129.41349123, 0.07904545, 90.58944386, -1366.51157446, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 32.35337281, 0.00012959, 97.06011842, 0.00038878, 323.53372808, 0.00129594, -32.35337281, -0.00012959, -97.06011842, -0.00038878, -323.53372808, -0.00129594, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 2.95, 12.75, 0.0)
    ops.node(121014, 2.95, 12.75, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.1225, 28532222.42798179, 11888426.01165908, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 210.07101679, 0.00121665, 250.34930217, 0.01443145, 25.03493022, 0.03577417, -210.07101679, -0.00121665, -250.34930217, -0.01443145, -25.03493022, -0.03577417, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 216.98073644, 0.00121665, 258.58386741, 0.01443145, 25.85838674, 0.03577417, -216.98073644, -0.00121665, -258.58386741, -0.01443145, -25.85838674, -0.03577417, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 156.13593135, 0.02433298, 156.13593135, 0.07299895, 109.29515194, -1538.88025585, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 39.03398284, 0.00011901, 117.10194851, 0.00035702, 390.33982837, 0.00119005, -39.03398284, -0.00011901, -117.10194851, -0.00035702, -390.33982837, -0.00119005, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 156.13593135, 0.02433298, 156.13593135, 0.07299895, 109.29515194, -1538.88025585, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 39.03398284, 0.00011901, 117.10194851, 0.00035702, 390.33982837, 0.00119005, -39.03398284, -0.00011901, -117.10194851, -0.00035702, -390.33982837, -0.00119005, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 8.3, 12.75, 0.0)
    ops.node(121015, 8.3, 12.75, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.16, 29524053.25041422, 12301688.85433926, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 315.07444866, 0.00113233, 375.76905083, 0.01282382, 37.57690508, 0.03083424, -315.07444866, -0.00113233, -375.76905083, -0.01282382, -37.57690508, -0.03083424, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 337.44120151, 0.00113233, 402.44443985, 0.01282382, 40.24444399, 0.03083424, -337.44120151, -0.00113233, -402.44443985, -0.01282382, -40.24444399, -0.03083424, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 185.24937965, 0.02264666, 185.24937965, 0.06793997, 129.67456576, -1600.31377233, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 46.31234491, 0.00010447, 138.93703474, 0.00031341, 463.12344913, 0.00104471, -46.31234491, -0.00010447, -138.93703474, -0.00031341, -463.12344913, -0.00104471, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 185.24937965, 0.02264666, 185.24937965, 0.06793997, 129.67456576, -1600.31377233, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 46.31234491, 0.00010447, 138.93703474, 0.00031341, 463.12344913, 0.00104471, -46.31234491, -0.00010447, -138.93703474, -0.00031341, -463.12344913, -0.00104471, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 13.65, 12.75, 0.0)
    ops.node(121016, 13.65, 12.75, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1225, 28709464.04057002, 11962276.68357084, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 194.93235129, 0.00122256, 232.45295104, 0.01389827, 23.2452951, 0.03594696, -194.93235129, -0.00122256, -232.45295104, -0.01389827, -23.2452951, -0.03594696, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 208.42906052, 0.00122256, 248.54750831, 0.01389827, 24.85475083, 0.03594696, -208.42906052, -0.00122256, -248.54750831, -0.01389827, -24.85475083, -0.03594696, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 153.12786615, 0.0244512, 153.12786615, 0.0733536, 107.1895063, -1472.75064323, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 38.28196654, 0.00011599, 114.84589961, 0.00034798, 382.81966537, 0.00115992, -38.28196654, -0.00011599, -114.84589961, -0.00034798, -382.81966537, -0.00115992, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 153.12786615, 0.0244512, 153.12786615, 0.0733536, 107.1895063, -1472.75064323, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 38.28196654, 0.00011599, 114.84589961, 0.00034798, 382.81966537, 0.00115992, -38.28196654, -0.00011599, -114.84589961, -0.00034798, -382.81966537, -0.00115992, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 17.0, 0.0)
    ops.node(121017, 0.0, 17.0, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.09, 30201579.21782729, 12583991.34076137, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 106.0675761, 0.00129889, 126.65119601, 0.01533757, 12.6651196, 0.04860987, -106.0675761, -0.00129889, -126.65119601, -0.01533757, -12.6651196, -0.04860987, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 116.85721498, 0.00129889, 139.53468707, 0.01533757, 13.95346871, 0.04860987, -116.85721498, -0.00129889, -139.53468707, -0.01533757, -13.95346871, -0.04860987, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 130.59094893, 0.02597773, 130.59094893, 0.07793318, 91.41366425, -1351.12595917, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 32.64773723, 0.00012799, 97.94321169, 0.00038397, 326.47737231, 0.0012799, -32.64773723, -0.00012799, -97.94321169, -0.00038397, -326.47737231, -0.0012799, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 130.59094893, 0.02597773, 130.59094893, 0.07793318, 91.41366425, -1351.12595917, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 32.64773723, 0.00012799, 97.94321169, 0.00038397, 326.47737231, 0.0012799, -32.64773723, -0.00012799, -97.94321169, -0.00038397, -326.47737231, -0.0012799, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 2.95, 17.0, 0.0)
    ops.node(121018, 2.95, 17.0, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.1225, 30441083.63528915, 12683784.84803715, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 207.71821205, 0.0011953, 247.42311109, 0.01483162, 24.74231111, 0.03953935, -207.71821205, -0.0011953, -247.42311109, -0.01483162, -24.74231111, -0.03953935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 214.20105943, 0.0011953, 255.1451411, 0.01483162, 25.51451411, 0.03953935, -214.20105943, -0.0011953, -255.1451411, -0.01483162, -25.51451411, -0.03953935, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 162.95443974, 0.02390604, 162.95443974, 0.07171811, 114.06810782, -1520.27934818, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 40.73860993, 0.00011641, 122.2158298, 0.00034924, 407.38609934, 0.00116414, -40.73860993, -0.00011641, -122.2158298, -0.00034924, -407.38609934, -0.00116414, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 162.95443974, 0.02390604, 162.95443974, 0.07171811, 114.06810782, -1520.27934818, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 40.73860993, 0.00011641, 122.2158298, 0.00034924, 407.38609934, 0.00116414, -40.73860993, -0.00011641, -122.2158298, -0.00034924, -407.38609934, -0.00116414, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 8.3, 17.0, 0.0)
    ops.node(121019, 8.3, 17.0, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.16, 29481137.17334965, 12283807.15556235, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 320.57265373, 0.0011146, 382.33232604, 0.01236824, 38.2332326, 0.03032176, -320.57265373, -0.0011146, -382.33232604, -0.01236824, -38.2332326, -0.03032176, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 334.59653361, 0.0011146, 399.05796546, 0.01236824, 39.90579655, 0.03032176, -334.59653361, -0.0011146, -399.05796546, -0.01236824, -39.90579655, -0.03032176, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 182.66632784, 0.02229201, 182.66632784, 0.06687603, 127.86642949, -1562.53080315, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 45.66658196, 0.00010316, 136.99974588, 0.00030949, 456.66581959, 0.00103164, -45.66658196, -0.00010316, -136.99974588, -0.00030949, -456.66581959, -0.00103164, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 182.66632784, 0.02229201, 182.66632784, 0.06687603, 127.86642949, -1562.53080315, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 45.66658196, 0.00010316, 136.99974588, 0.00030949, 456.66581959, 0.00103164, -45.66658196, -0.00010316, -136.99974588, -0.00030949, -456.66581959, -0.00103164, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 13.65, 17.0, 0.0)
    ops.node(121020, 13.65, 17.0, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.1225, 30412020.66071639, 12671675.27529849, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 197.6883866, 0.00120525, 235.59338322, 0.01421056, 23.55933832, 0.03922168, -197.6883866, -0.00120525, -235.59338322, -0.01421056, -23.55933832, -0.03922168, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 211.29617269, 0.00120525, 251.81034172, 0.01421056, 25.18103417, 0.03922168, -211.29617269, -0.00120525, -251.81034172, -0.01421056, -25.18103417, -0.03922168, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 161.78322381, 0.02410506, 161.78322381, 0.07231518, 113.24825667, -1502.13605706, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 40.44580595, 0.00011569, 121.33741786, 0.00034706, 404.45805953, 0.00115687, -40.44580595, -0.00011569, -121.33741786, -0.00034706, -404.45805953, -0.00115687, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 161.78322381, 0.02410506, 161.78322381, 0.07231518, 113.24825667, -1502.13605706, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 40.44580595, 0.00011569, 121.33741786, 0.00034706, 404.45805953, 0.00115687, -40.44580595, -0.00011569, -121.33741786, -0.00034706, -404.45805953, -0.00115687, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 0.0, 21.25, 0.0)
    ops.node(121021, 0.0, 21.25, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.09, 28274496.97854435, 11781040.40772681, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 97.84547605, 0.00138732, 116.92260916, 0.01420948, 11.69226092, 0.03952873, -97.84547605, -0.00138732, -116.92260916, -0.01420948, -11.69226092, -0.03952873, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 102.74333452, 0.00138732, 122.77541313, 0.01420948, 12.27754131, 0.03952873, -102.74333452, -0.00138732, -122.77541313, -0.01420948, -12.27754131, -0.03952873, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 115.11301354, 0.02774638, 115.11301354, 0.08323915, 80.57910948, -1157.31487113, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 28.77825339, 0.00012051, 86.33476016, 0.00036153, 287.78253386, 0.00120509, -28.77825339, -0.00012051, -86.33476016, -0.00036153, -287.78253386, -0.00120509, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 115.11301354, 0.02774638, 115.11301354, 0.08323915, 80.57910948, -1157.31487113, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 28.77825339, 0.00012051, 86.33476016, 0.00036153, 287.78253386, 0.00120509, -28.77825339, -0.00012051, -86.33476016, -0.00036153, -287.78253386, -0.00120509, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 2.95, 21.25, 0.0)
    ops.node(121022, 2.95, 21.25, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.1225, 29505554.99546578, 12293981.24811074, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 226.15616541, 0.00123046, 269.52445278, 0.01496278, 26.95244528, 0.03807783, -226.15616541, -0.00123046, -269.52445278, -0.01496278, -26.95244528, -0.03807783, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 238.1286885, 0.00123046, 283.79285765, 0.01496278, 28.37928577, 0.03807783, -238.1286885, -0.00123046, -283.79285765, -0.01496278, -28.37928577, -0.03807783, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 158.06127894, 0.02460917, 158.06127894, 0.07382752, 110.64289526, -1502.40574402, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 39.51531974, 0.0001165, 118.54595921, 0.0003495, 395.15319736, 0.00116498, -39.51531974, -0.0001165, -118.54595921, -0.0003495, -395.15319736, -0.00116498, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 158.06127894, 0.02460917, 158.06127894, 0.07382752, 110.64289526, -1502.40574402, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 39.51531974, 0.0001165, 118.54595921, 0.0003495, 395.15319736, 0.00116498, -39.51531974, -0.0001165, -118.54595921, -0.0003495, -395.15319736, -0.00116498, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 8.3, 21.25, 0.0)
    ops.node(121023, 8.3, 21.25, 3.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.16, 28186091.72620538, 11744204.88591891, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 344.89650453, 0.0011196, 411.31565959, 0.01229056, 41.13156596, 0.02844404, -344.89650453, -0.0011196, -411.31565959, -0.01229056, -41.13156596, -0.02844404, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 344.89650453, 0.0011196, 411.31565959, 0.01229056, 41.13156596, 0.02844404, -344.89650453, -0.0011196, -411.31565959, -0.01229056, -41.13156596, -0.02844404, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 176.06131608, 0.0223921, 176.06131608, 0.06717629, 123.24292126, -1566.79516661, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 44.01532902, 0.000104, 132.04598706, 0.00031201, 440.15329021, 0.00104002, -44.01532902, -0.000104, -132.04598706, -0.00031201, -440.15329021, -0.00104002, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 176.06131608, 0.0223921, 176.06131608, 0.06717629, 123.24292126, -1566.79516661, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 44.01532902, 0.000104, 132.04598706, 0.00031201, 440.15329021, 0.00104002, -44.01532902, -0.000104, -132.04598706, -0.00031201, -440.15329021, -0.00104002, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 13.65, 21.25, 0.0)
    ops.node(121024, 13.65, 21.25, 3.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.1225, 29334061.25741038, 12222525.52392099, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 213.19000243, 0.00119959, 254.21775723, 0.01497892, 25.42177572, 0.03815692, -213.19000243, -0.00119959, -254.21775723, -0.01497892, -25.42177572, -0.03815692, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 213.19000243, 0.00119959, 254.21775723, 0.01497892, 25.42177572, 0.03815692, -213.19000243, -0.00119959, -254.21775723, -0.01497892, -25.42177572, -0.03815692, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 158.11485382, 0.02399183, 158.11485382, 0.0719755, 110.68039768, -1516.04153014, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 39.52871346, 0.00011722, 118.58614037, 0.00035166, 395.28713456, 0.00117219, -39.52871346, -0.00011722, -118.58614037, -0.00035166, -395.28713456, -0.00117219, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 158.11485382, 0.02399183, 158.11485382, 0.0719755, 110.68039768, -1516.04153014, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 39.52871346, 0.00011722, 118.58614037, 0.00035166, 395.28713456, 0.00117219, -39.52871346, -0.00011722, -118.58614037, -0.00035166, -395.28713456, -0.00117219, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170025, 0.0, 25.5, 0.0)
    ops.node(121025, 0.0, 25.5, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 25, 170025, 121025, 0.09, 28364455.65409087, 11818523.18920453, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20025, 94.5659886, 0.00127278, 113.93513505, 0.01641915, 11.3935135, 0.05374024, -94.5659886, -0.00127278, -113.93513505, -0.01641915, -11.3935135, -0.05374024, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10025, 94.5659886, 0.00127278, 113.93513505, 0.01641915, 11.3935135, 0.05374024, -94.5659886, -0.00127278, -113.93513505, -0.01641915, -11.3935135, -0.05374024, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20025, 25, 0.0, 114.57394265, 0.02545551, 114.57394265, 0.07636652, 80.20175986, -1251.52423728, 0.05, 2, 0, 70025, 21025, 2, 3)
    ops.uniaxialMaterial('LimitState', 40025, 28.64348566, 0.00011956, 85.93045699, 0.00035869, 286.43485663, 0.00119565, -28.64348566, -0.00011956, -85.93045699, -0.00035869, -286.43485663, -0.00119565, 0.4, 0.3, 0.003, 0.0, 0.0, 20025, 2)
    ops.limitCurve('ThreePoint', 10025, 25, 0.0, 114.57394265, 0.02545551, 114.57394265, 0.07636652, 80.20175986, -1251.52423728, 0.05, 2, 0, 70025, 21025, 1, 3)
    ops.uniaxialMaterial('LimitState', 30025, 28.64348566, 0.00011956, 85.93045699, 0.00035869, 286.43485663, 0.00119565, -28.64348566, -0.00011956, -85.93045699, -0.00035869, -286.43485663, -0.00119565, 0.4, 0.3, 0.003, 0.0, 0.0, 10025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 25, 99999, 'P', 40025, 'Vy', 30025, 'Vz', 20025, 'My', 10025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170025, 70025, 170025, 25, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121025, 121025, 21025, 25, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170026, 2.95, 25.5, 0.0)
    ops.node(121026, 2.95, 25.5, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 26, 170026, 121026, 0.1225, 28502347.76707625, 11875978.23628177, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20026, 188.60703723, 0.00117708, 225.82660973, 0.01481064, 22.58266097, 0.03929889, -188.60703723, -0.00117708, -225.82660973, -0.01481064, -22.58266097, -0.03929889, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10026, 188.60703723, 0.00117708, 225.82660973, 0.01481064, 22.58266097, 0.03929889, -188.60703723, -0.00117708, -225.82660973, -0.01481064, -22.58266097, -0.03929889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20026, 26, 0.0, 147.23404154, 0.02354157, 147.23404154, 0.07062472, 103.06382908, -1390.06565293, 0.05, 2, 0, 70026, 21026, 2, 3)
    ops.uniaxialMaterial('LimitState', 40026, 36.80851038, 0.00011234, 110.42553115, 0.00033701, 368.08510384, 0.00112338, -36.80851038, -0.00011234, -110.42553115, -0.00033701, -368.08510384, -0.00112338, 0.4, 0.3, 0.003, 0.0, 0.0, 20026, 2)
    ops.limitCurve('ThreePoint', 10026, 26, 0.0, 147.23404154, 0.02354157, 147.23404154, 0.07062472, 103.06382908, -1390.06565293, 0.05, 2, 0, 70026, 21026, 1, 3)
    ops.uniaxialMaterial('LimitState', 30026, 36.80851038, 0.00011234, 110.42553115, 0.00033701, 368.08510384, 0.00112338, -36.80851038, -0.00011234, -110.42553115, -0.00033701, -368.08510384, -0.00112338, 0.4, 0.3, 0.003, 0.0, 0.0, 10026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 26, 99999, 'P', 40026, 'Vy', 30026, 'Vz', 20026, 'My', 10026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170026, 70026, 170026, 26, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121026, 121026, 21026, 26, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170027, 8.3, 25.5, 0.0)
    ops.node(121027, 8.3, 25.5, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 27, 170027, 121027, 0.1225, 29711434.97458602, 12379764.57274417, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20027, 194.52624178, 0.0012221, 231.73210256, 0.01413254, 23.17321026, 0.03736493, -194.52624178, -0.0012221, -231.73210256, -0.01413254, -23.17321026, -0.03736493, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10027, 188.2523583, 0.0012221, 224.25825124, 0.01413254, 22.42582512, 0.03736493, -188.2523583, -0.0012221, -224.25825124, -0.01413254, -22.42582512, -0.03736493, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20027, 27, 0.0, 160.51194505, 0.02444204, 160.51194505, 0.07332611, 112.35836154, -1530.64595603, 0.05, 2, 0, 70027, 21027, 2, 3)
    ops.uniaxialMaterial('LimitState', 40027, 40.12798626, 0.00011748, 120.38395879, 0.00035245, 401.27986263, 0.00117485, -40.12798626, -0.00011748, -120.38395879, -0.00035245, -401.27986263, -0.00117485, 0.4, 0.3, 0.003, 0.0, 0.0, 20027, 2)
    ops.limitCurve('ThreePoint', 10027, 27, 0.0, 160.51194505, 0.02444204, 160.51194505, 0.07332611, 112.35836154, -1530.64595603, 0.05, 2, 0, 70027, 21027, 1, 3)
    ops.uniaxialMaterial('LimitState', 30027, 40.12798626, 0.00011748, 120.38395879, 0.00035245, 401.27986263, 0.00117485, -40.12798626, -0.00011748, -120.38395879, -0.00035245, -401.27986263, -0.00117485, 0.4, 0.3, 0.003, 0.0, 0.0, 10027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 27, 99999, 'P', 40027, 'Vy', 30027, 'Vz', 20027, 'My', 10027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170027, 70027, 170027, 27, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121027, 121027, 21027, 27, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170028, 13.65, 25.5, 0.0)
    ops.node(121028, 13.65, 25.5, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 28, 170028, 121028, 0.0625, 28835944.71810736, 12014976.96587807, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20028, 71.85721573, 0.00165445, 85.14081455, 0.01413446, 8.51408146, 0.04128366, -71.85721573, -0.00165445, -85.14081455, -0.01413446, -8.51408146, -0.04128366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10028, 71.85721573, 0.00165445, 85.14081455, 0.01413446, 8.51408146, 0.04128366, -71.85721573, -0.00165445, -85.14081455, -0.01413446, -8.51408146, -0.04128366, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20028, 28, 0.0, 100.35236145, 0.03308893, 100.35236145, 0.09926678, 70.24665302, -1152.19682055, 0.05, 2, 0, 70028, 21028, 2, 3)
    ops.uniaxialMaterial('LimitState', 40028, 25.08809036, 0.00014834, 75.26427109, 0.00044501, 250.88090363, 0.00148336, -25.08809036, -0.00014834, -75.26427109, -0.00044501, -250.88090363, -0.00148336, 0.4, 0.3, 0.003, 0.0, 0.0, 20028, 2)
    ops.limitCurve('ThreePoint', 10028, 28, 0.0, 100.35236145, 0.03308893, 100.35236145, 0.09926678, 70.24665302, -1152.19682055, 0.05, 2, 0, 70028, 21028, 1, 3)
    ops.uniaxialMaterial('LimitState', 30028, 25.08809036, 0.00014834, 75.26427109, 0.00044501, 250.88090363, 0.00148336, -25.08809036, -0.00014834, -75.26427109, -0.00044501, -250.88090363, -0.00148336, 0.4, 0.3, 0.003, 0.0, 0.0, 10028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 28, 99999, 'P', 40028, 'Vy', 30028, 'Vz', 20028, 'My', 10028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170028, 70028, 170028, 28, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121028, 121028, 21028, 28, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.3, 0.0, 3.95)
    ops.node(122003, 8.3, 0.0, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.1225, 28414397.05274494, 11839332.10531039, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 123.09640931, 0.00099438, 147.65530365, 0.01349929, 14.76553036, 0.04275103, -123.09640931, -0.00099438, -147.65530365, -0.01349929, -14.76553036, -0.04275103, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 111.32703997, 0.00099438, 133.53783415, 0.01349929, 13.35378341, 0.04275103, -111.32703997, -0.00099438, -133.53783415, -0.01349929, -13.35378341, -0.04275103, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 153.65504417, 0.0198876, 153.65504417, 0.05966279, 107.55853092, -1837.73453797, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 38.41376104, 9.853e-05, 115.24128313, 0.00029559, 384.13761042, 0.0009853, -38.41376104, -9.853e-05, -115.24128313, -0.00029559, -384.13761042, -0.0009853, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 153.65504417, 0.0198876, 153.65504417, 0.05966279, 107.55853092, -1837.73453797, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 38.41376104, 9.853e-05, 115.24128313, 0.00029559, 384.13761042, 0.0009853, -38.41376104, -9.853e-05, -115.24128313, -0.00029559, -384.13761042, -0.0009853, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.65, 0.0, 3.95)
    ops.node(122004, 13.65, 0.0, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.0625, 28819413.93867648, 12008089.1411152, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 62.61170046, 0.00138458, 74.80797837, 0.01582827, 7.48079784, 0.05060116, -62.61170046, -0.00138458, -74.80797837, -0.01582827, -7.48079784, -0.05060116, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 62.61170046, 0.00138458, 74.80797837, 0.01582827, 7.48079784, 0.05060116, -62.61170046, -0.00138458, -74.80797837, -0.01582827, -7.48079784, -0.05060116, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 95.28346343, 0.0276915, 95.28346343, 0.08307451, 66.6984244, -1308.64818841, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 23.82086586, 0.00011807, 71.46259757, 0.00035422, 238.20865857, 0.00118072, -23.82086586, -0.00011807, -71.46259757, -0.00035422, -238.20865857, -0.00118072, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 95.28346343, 0.0276915, 95.28346343, 0.08307451, 66.6984244, -1308.64818841, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 23.82086586, 0.00011807, 71.46259757, 0.00035422, 238.20865857, 0.00118072, -23.82086586, -0.00011807, -71.46259757, -0.00035422, -238.20865857, -0.00118072, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.25, 3.925)
    ops.node(122005, 0.0, 4.25, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.09, 29154531.46772906, 12147721.44488711, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 77.89706287, 0.00112448, 93.51096404, 0.01488862, 9.3510964, 0.05054451, -77.89706287, -0.00112448, -93.51096404, -0.01488862, -9.3510964, -0.05054451, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 87.87978939, 0.00112448, 105.49465568, 0.01488862, 10.54946557, 0.05054451, -87.87978939, -0.00112448, -105.49465568, -0.01488862, -10.54946557, -0.05054451, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 121.05538005, 0.02248959, 121.05538005, 0.06746876, 84.73876603, -1528.76135429, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 30.26384501, 0.00010297, 90.79153503, 0.00030892, 302.63845012, 0.00102975, -30.26384501, -0.00010297, -90.79153503, -0.00030892, -302.63845012, -0.00102975, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 121.05538005, 0.02248959, 121.05538005, 0.06746876, 84.73876603, -1528.76135429, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 30.26384501, 0.00010297, 90.79153503, 0.00030892, 302.63845012, 0.00102975, -30.26384501, -0.00010297, -90.79153503, -0.00030892, -302.63845012, -0.00102975, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 2.95, 4.25, 3.9)
    ops.node(122006, 2.95, 4.25, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.16, 29422481.4410108, 12259367.26708784, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 180.50201404, 0.00092331, 216.8351384, 0.01220889, 21.68351384, 0.03436025, -180.50201404, -0.00092331, -216.8351384, -0.01220889, -21.68351384, -0.03436025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 180.50201404, 0.00092331, 216.8351384, 0.01220889, 21.68351384, 0.03436025, -180.50201404, -0.00092331, -216.8351384, -0.01220889, -21.68351384, -0.03436025, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 166.22467457, 0.01846622, 166.22467457, 0.05539867, 116.3572722, -1526.36524344, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 41.55616864, 7.881e-05, 124.66850593, 0.00023643, 415.56168644, 0.00078812, -41.55616864, -7.881e-05, -124.66850593, -0.00023643, -415.56168644, -0.00078812, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 166.22467457, 0.01846622, 166.22467457, 0.05539867, 116.3572722, -1526.36524344, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 41.55616864, 7.881e-05, 124.66850593, 0.00023643, 415.56168644, 0.00078812, -41.55616864, -7.881e-05, -124.66850593, -0.00023643, -415.56168644, -0.00078812, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 8.3, 4.25, 3.9)
    ops.node(122007, 8.3, 4.25, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.16, 28763916.87455272, 11984965.36439697, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 191.53395297, 0.00097631, 229.78695007, 0.01189433, 22.97869501, 0.03208178, -191.53395297, -0.00097631, -229.78695007, -0.01189433, -22.97869501, -0.03208178, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 191.53395297, 0.00097631, 229.78695007, 0.01189433, 22.97869501, 0.03208178, -191.53395297, -0.00097631, -229.78695007, -0.01189433, -22.97869501, -0.03208178, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 167.72234832, 0.0195263, 167.72234832, 0.0585789, 117.40564382, -1620.89432421, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 41.93058708, 8.134e-05, 125.79176124, 0.00024403, 419.3058708, 0.00081342, -41.93058708, -8.134e-05, -125.79176124, -0.00024403, -419.3058708, -0.00081342, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 167.72234832, 0.0195263, 167.72234832, 0.0585789, 117.40564382, -1620.89432421, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 41.93058708, 8.134e-05, 125.79176124, 0.00024403, 419.3058708, 0.00081342, -41.93058708, -8.134e-05, -125.79176124, -0.00024403, -419.3058708, -0.00081342, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 13.65, 4.25, 3.925)
    ops.node(122008, 13.65, 4.25, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.1225, 29813771.69456388, 12422404.87273495, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 144.84648268, 0.00100232, 173.68741752, 0.01445415, 17.36874175, 0.04296126, -144.84648268, -0.00100232, -173.68741752, -0.01445415, -17.36874175, -0.04296126, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 132.22756858, 0.00100232, 158.55590338, 0.01445415, 15.85559034, 0.04296126, -132.22756858, -0.00100232, -158.55590338, -0.01445415, -15.85559034, -0.04296126, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 147.89276128, 0.02004645, 147.89276128, 0.06013936, 103.5249329, -1579.80061345, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 36.97319032, 9.038e-05, 110.91957096, 0.00027115, 369.7319032, 0.00090383, -36.97319032, -9.038e-05, -110.91957096, -0.00027115, -369.7319032, -0.00090383, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 147.89276128, 0.02004645, 147.89276128, 0.06013936, 103.5249329, -1579.80061345, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 36.97319032, 9.038e-05, 110.91957096, 0.00027115, 369.7319032, 0.00090383, -36.97319032, -9.038e-05, -110.91957096, -0.00027115, -369.7319032, -0.00090383, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.5, 3.925)
    ops.node(122009, 0.0, 8.5, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.09, 29456380.08809245, 12273491.70337186, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 75.65754672, 0.00111004, 90.89451178, 0.01527894, 9.08945118, 0.05271466, -75.65754672, -0.00111004, -90.89451178, -0.01527894, -9.08945118, -0.05271466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 85.59066835, 0.00111004, 102.82810306, 0.01527894, 10.28281031, 0.05271466, -85.59066835, -0.00111004, -102.82810306, -0.01527894, -10.28281031, -0.05271466, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 120.0692586, 0.02220087, 120.0692586, 0.0666026, 84.04848102, -1507.68484546, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 30.01731465, 0.00010109, 90.05194395, 0.00030327, 300.1731465, 0.00101089, -30.01731465, -0.00010109, -90.05194395, -0.00030327, -300.1731465, -0.00101089, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 120.0692586, 0.02220087, 120.0692586, 0.0666026, 84.04848102, -1507.68484546, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 30.01731465, 0.00010109, 90.05194395, 0.00030327, 300.1731465, 0.00101089, -30.01731465, -0.00010109, -90.05194395, -0.00030327, -300.1731465, -0.00101089, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 2.95, 8.5, 3.9)
    ops.node(122010, 2.95, 8.5, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.1225, 29505534.20344594, 12293972.58476914, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 133.88003876, 0.00100482, 160.4695962, 0.01413458, 16.04695962, 0.04155252, -133.88003876, -0.00100482, -160.4695962, -0.01413458, -16.04695962, -0.04155252, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 127.51189588, 0.00100482, 152.83669345, 0.01413458, 15.28366935, 0.04155252, -127.51189588, -0.00100482, -152.83669345, -0.01413458, -15.28366935, -0.04155252, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 149.45880788, 0.02009633, 149.45880788, 0.060289, 104.62116552, -1634.54727911, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 37.36470197, 9.229e-05, 112.09410591, 0.00027688, 373.6470197, 0.00092295, -37.36470197, -9.229e-05, -112.09410591, -0.00027688, -373.6470197, -0.00092295, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 149.45880788, 0.02009633, 149.45880788, 0.060289, 104.62116552, -1634.54727911, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 37.36470197, 9.229e-05, 112.09410591, 0.00027688, 373.6470197, 0.00092295, -37.36470197, -9.229e-05, -112.09410591, -0.00027688, -373.6470197, -0.00092295, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.3, 8.5, 3.9)
    ops.node(122011, 8.3, 8.5, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 29240689.8067724, 12183620.75282183, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 189.51321347, 0.00095516, 227.28578394, 0.01229404, 22.72857839, 0.03306767, -189.51321347, -0.00095516, -227.28578394, -0.01229404, -22.72857839, -0.03306767, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 189.51321347, 0.00095516, 227.28578394, 0.01229404, 22.72857839, 0.03306767, -189.51321347, -0.00095516, -227.28578394, -0.01229404, -22.72857839, -0.03306767, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 171.73921463, 0.01910328, 171.73921463, 0.05730985, 120.21745024, -1653.39894548, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 42.93480366, 8.193e-05, 128.80441097, 0.0002458, 429.34803656, 0.00081932, -42.93480366, -8.193e-05, -128.80441097, -0.0002458, -429.34803656, -0.00081932, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 171.73921463, 0.01910328, 171.73921463, 0.05730985, 120.21745024, -1653.39894548, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 42.93480366, 8.193e-05, 128.80441097, 0.0002458, 429.34803656, 0.00081932, -42.93480366, -8.193e-05, -128.80441097, -0.0002458, -429.34803656, -0.00081932, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 13.65, 8.5, 3.925)
    ops.node(122012, 13.65, 8.5, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 30227655.90669308, 12594856.62778878, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 150.99486769, 0.00103114, 180.96564424, 0.01480613, 18.09656442, 0.04391441, -150.99486769, -0.00103114, -180.96564424, -0.01480613, -18.09656442, -0.04391441, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 145.02469727, 0.00103114, 173.81046239, 0.01480613, 17.38104624, 0.04391441, -145.02469727, -0.00103114, -173.81046239, -0.01480613, -17.38104624, -0.04391441, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 149.9601116, 0.02062285, 149.9601116, 0.06186855, 104.97207812, -1589.83307179, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 37.4900279, 9.039e-05, 112.4700837, 0.00027118, 374.900279, 0.00090392, -37.4900279, -9.039e-05, -112.4700837, -0.00027118, -374.900279, -0.00090392, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 149.9601116, 0.02062285, 149.9601116, 0.06186855, 104.97207812, -1589.83307179, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 37.4900279, 9.039e-05, 112.4700837, 0.00027118, 374.900279, 0.00090392, -37.4900279, -9.039e-05, -112.4700837, -0.00027118, -374.900279, -0.00090392, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 12.75, 3.925)
    ops.node(122013, 0.0, 12.75, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.09, 29673107.50280973, 12363794.79283739, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 68.6362054, 0.0010864, 82.4375063, 0.01541352, 8.24375063, 0.05324761, -68.6362054, -0.0010864, -82.4375063, -0.01541352, -8.24375063, -0.05324761, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 73.48482642, 0.0010864, 88.26108329, 0.01541352, 8.82610833, 0.05324761, -73.48482642, -0.0010864, -88.26108329, -0.01541352, -8.82610833, -0.05324761, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 122.38961946, 0.02172797, 122.38961946, 0.0651839, 85.67273362, -1555.58707621, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 30.59740487, 0.00010229, 91.7922146, 0.00030687, 305.97404865, 0.0010229, -30.59740487, -0.00010229, -91.7922146, -0.00030687, -305.97404865, -0.0010229, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 122.38961946, 0.02172797, 122.38961946, 0.0651839, 85.67273362, -1555.58707621, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 30.59740487, 0.00010229, 91.7922146, 0.00030687, 305.97404865, 0.0010229, -30.59740487, -0.00010229, -91.7922146, -0.00030687, -305.97404865, -0.0010229, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 2.95, 12.75, 3.9)
    ops.node(122014, 2.95, 12.75, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.1225, 28635075.94096793, 11931281.64206997, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 145.76226758, 0.00103934, 174.81836017, 0.01420608, 17.48183602, 0.04021233, -145.76226758, -0.00103934, -174.81836017, -0.01420608, -17.48183602, -0.04021233, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 133.56744719, 0.00103934, 160.19263748, 0.01420608, 16.01926375, 0.04021233, -133.56744719, -0.00103934, -160.19263748, -0.01420608, -16.01926375, -0.04021233, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 144.59743883, 0.02078682, 144.59743883, 0.06236047, 101.21820718, -1601.15257057, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 36.14935971, 9.201e-05, 108.44807912, 0.00027602, 361.49359708, 0.00092007, -36.14935971, -9.201e-05, -108.44807912, -0.00027602, -361.49359708, -0.00092007, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 144.59743883, 0.02078682, 144.59743883, 0.06236047, 101.21820718, -1601.15257057, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 36.14935971, 9.201e-05, 108.44807912, 0.00027602, 361.49359708, 0.00092007, -36.14935971, -9.201e-05, -108.44807912, -0.00027602, -361.49359708, -0.00092007, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 8.3, 12.75, 3.9)
    ops.node(122015, 8.3, 12.75, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.16, 29963530.92484351, 12484804.55201813, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 190.54071544, 0.00093099, 228.35085351, 0.01268524, 22.83508535, 0.03430072, -190.54071544, -0.00093099, -228.35085351, -0.01268524, -22.83508535, -0.03430072, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 190.54071544, 0.00093099, 228.35085351, 0.01268524, 22.83508535, 0.03430072, -190.54071544, -0.00093099, -228.35085351, -0.01268524, -22.83508535, -0.03430072, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 175.3126966, 0.01861976, 175.3126966, 0.05585929, 122.71888762, -1650.30296392, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 43.82817415, 8.162e-05, 131.48452245, 0.00024486, 438.2817415, 0.0008162, -43.82817415, -8.162e-05, -131.48452245, -0.00024486, -438.2817415, -0.0008162, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 175.3126966, 0.01861976, 175.3126966, 0.05585929, 122.71888762, -1650.30296392, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 43.82817415, 8.162e-05, 131.48452245, 0.00024486, 438.2817415, 0.0008162, -43.82817415, -8.162e-05, -131.48452245, -0.00024486, -438.2817415, -0.0008162, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 13.65, 12.75, 3.925)
    ops.node(122016, 13.65, 12.75, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1225, 31136101.84242232, 12973375.76767597, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 144.93039134, 0.00101371, 173.45060297, 0.01449799, 17.3450603, 0.04484597, -144.93039134, -0.00101371, -173.45060297, -0.01449799, -17.3450603, -0.04484597, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 132.81467718, 0.00101371, 158.95069094, 0.01449799, 15.89506909, 0.04484597, -132.81467718, -0.00101371, -158.95069094, -0.01449799, -15.89506909, -0.04484597, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 153.78233952, 0.02027413, 153.78233952, 0.06082239, 107.64763767, -1594.27558634, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 38.44558488, 8.999e-05, 115.33675464, 0.00026997, 384.45584881, 0.00089991, -38.44558488, -8.999e-05, -115.33675464, -0.00026997, -384.45584881, -0.00089991, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 153.78233952, 0.02027413, 153.78233952, 0.06082239, 107.64763767, -1594.27558634, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 38.44558488, 8.999e-05, 115.33675464, 0.00026997, 384.45584881, 0.00089991, -38.44558488, -8.999e-05, -115.33675464, -0.00026997, -384.45584881, -0.00089991, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 17.0, 3.925)
    ops.node(122017, 0.0, 17.0, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.09, 29493935.56057769, 12289139.81690737, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 68.60155548, 0.00111776, 82.41387334, 0.01534151, 8.24138733, 0.05284687, -68.60155548, -0.00111776, -82.41387334, -0.01534151, -8.24138733, -0.05284687, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 73.24048745, 0.00111776, 87.98681332, 0.01534151, 8.79868133, 0.05284687, -73.24048745, -0.00111776, -87.98681332, -0.01534151, -8.79868133, -0.05284687, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 121.53924171, 0.02235514, 121.53924171, 0.06706541, 85.0774692, -1545.99048907, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 30.38481043, 0.0001022, 91.15443128, 0.00030659, 303.84810428, 0.00102196, -30.38481043, -0.0001022, -91.15443128, -0.00030659, -303.84810428, -0.00102196, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 121.53924171, 0.02235514, 121.53924171, 0.06706541, 85.0774692, -1545.99048907, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 30.38481043, 0.0001022, 91.15443128, 0.00030659, 303.84810428, 0.00102196, -30.38481043, -0.0001022, -91.15443128, -0.00030659, -303.84810428, -0.00102196, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 2.95, 17.0, 3.9)
    ops.node(122018, 2.95, 17.0, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.1225, 30597044.86677891, 12748768.69449121, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 144.40967255, 0.00104011, 172.86509713, 0.01442997, 17.28650971, 0.04346859, -144.40967255, -0.00104011, -172.86509713, -0.01442997, -17.28650971, -0.04346859, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 133.16223493, 0.00104011, 159.40139097, 0.01442997, 15.9401391, 0.04346859, -133.16223493, -0.00104011, -159.40139097, -0.01442997, -15.9401391, -0.04346859, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 152.66889218, 0.02080213, 152.66889218, 0.0624064, 106.86822453, -1608.30156981, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 38.16722305, 9.091e-05, 114.50166914, 0.00027274, 381.67223045, 0.00090914, -38.16722305, -9.091e-05, -114.50166914, -0.00027274, -381.67223045, -0.00090914, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 152.66889218, 0.02080213, 152.66889218, 0.0624064, 106.86822453, -1608.30156981, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 38.16722305, 9.091e-05, 114.50166914, 0.00027274, 381.67223045, 0.00090914, -38.16722305, -9.091e-05, -114.50166914, -0.00027274, -381.67223045, -0.00090914, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 8.3, 17.0, 3.9)
    ops.node(122019, 8.3, 17.0, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.16, 29135056.63365114, 12139606.93068798, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 194.1564473, 0.00094675, 232.874283, 0.01178581, 23.2874283, 0.03243172, -194.1564473, -0.00094675, -232.874283, -0.01178581, -23.2874283, -0.03243172, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 194.1564473, 0.00094675, 232.874283, 0.01178581, 23.2874283, 0.03243172, -194.1564473, -0.00094675, -232.874283, -0.01178581, -23.2874283, -0.03243172, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 169.40747241, 0.01893509, 169.40747241, 0.05680527, 118.58523069, -1616.65951073, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 42.3518681, 8.111e-05, 127.05560431, 0.00024334, 423.51868102, 0.00081113, -42.3518681, -8.111e-05, -127.05560431, -0.00024334, -423.51868102, -0.00081113, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 169.40747241, 0.01893509, 169.40747241, 0.05680527, 118.58523069, -1616.65951073, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 42.3518681, 8.111e-05, 127.05560431, 0.00024334, 423.51868102, 0.00081113, -42.3518681, -8.111e-05, -127.05560431, -0.00024334, -423.51868102, -0.00081113, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 13.65, 17.0, 3.925)
    ops.node(122020, 13.65, 17.0, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.1225, 29643926.87312956, 12351636.19713732, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 151.76118034, 0.00103049, 182.01355987, 0.01511398, 18.20135599, 0.04336757, -151.76118034, -0.00103049, -182.01355987, -0.01511398, -18.20135599, -0.04336757, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 145.60531586, 0.00103049, 174.63057296, 0.01511398, 17.4630573, 0.04336757, -145.60531586, -0.00103049, -174.63057296, -0.01511398, -17.4630573, -0.04336757, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 149.34112655, 0.02060989, 149.34112655, 0.06182966, 104.53878858, -1629.59344771, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 37.33528164, 9.179e-05, 112.00584491, 0.00027537, 373.35281637, 0.00091791, -37.33528164, -9.179e-05, -112.00584491, -0.00027537, -373.35281637, -0.00091791, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 149.34112655, 0.02060989, 149.34112655, 0.06182966, 104.53878858, -1629.59344771, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 37.33528164, 9.179e-05, 112.00584491, 0.00027537, 373.35281637, 0.00091791, -37.33528164, -9.179e-05, -112.00584491, -0.00027537, -373.35281637, -0.00091791, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 0.0, 21.25, 3.925)
    ops.node(122021, 0.0, 21.25, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.09, 29332768.68434987, 12221986.95181245, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 79.06949931, 0.00117592, 95.00687763, 0.01568592, 9.50068776, 0.04814696, -79.06949931, -0.00117592, -95.00687763, -0.01568592, -9.50068776, -0.04814696, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 79.06949931, 0.00117592, 95.00687763, 0.01568592, 9.50068776, 0.04814696, -79.06949931, -0.00117592, -95.00687763, -0.01568592, -9.50068776, -0.04814696, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 113.06535925, 0.02351838, 113.06535925, 0.07055514, 79.14575148, -1327.62434614, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 28.26633981, 9.559e-05, 84.79901944, 0.00028678, 282.66339813, 0.00095593, -28.26633981, -9.559e-05, -84.79901944, -0.00028678, -282.66339813, -0.00095593, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 113.06535925, 0.02351838, 113.06535925, 0.07055514, 79.14575148, -1327.62434614, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 28.26633981, 9.559e-05, 84.79901944, 0.00028678, 282.66339813, 0.00095593, -28.26633981, -9.559e-05, -84.79901944, -0.00028678, -282.66339813, -0.00095593, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 2.95, 21.25, 3.9)
    ops.node(122022, 2.95, 21.25, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.1225, 29353371.1610828, 12230571.31711783, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 144.15171798, 0.00102643, 172.80463915, 0.01443954, 17.28046392, 0.0416185, -144.15171798, -0.00102643, -172.80463915, -0.01443954, -17.28046392, -0.0416185, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 133.07272568, 0.00102643, 159.52348445, 0.01443954, 15.95234845, 0.0416185, -133.07272568, -0.00102643, -159.52348445, -0.01443954, -15.95234845, -0.0416185, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 147.10871262, 0.02052859, 147.10871262, 0.06158577, 102.97609883, -1594.20884795, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 36.77717815, 9.131e-05, 110.33153446, 0.00027394, 367.77178155, 0.00091314, -36.77717815, -9.131e-05, -110.33153446, -0.00027394, -367.77178155, -0.00091314, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 147.10871262, 0.02052859, 147.10871262, 0.06158577, 102.97609883, -1594.20884795, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 36.77717815, 9.131e-05, 110.33153446, 0.00027394, 367.77178155, 0.00091314, -36.77717815, -9.131e-05, -110.33153446, -0.00027394, -367.77178155, -0.00091314, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 8.3, 21.25, 3.9)
    ops.node(122023, 8.3, 21.25, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.16, 30174667.91990622, 12572778.29996092, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 192.15691177, 0.00092827, 230.22744841, 0.01192214, 23.02274484, 0.03377314, -192.15691177, -0.00092827, -230.22744841, -0.01192214, -23.02274484, -0.03377314, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 192.15691177, 0.00092827, 230.22744841, 0.01192214, 23.02274484, 0.03377314, -192.15691177, -0.00092827, -230.22744841, -0.01192214, -23.02274484, -0.03377314, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 174.74518067, 0.01856544, 174.74518067, 0.05569633, 122.32162647, -1616.20815527, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 43.68629517, 8.079e-05, 131.0588855, 0.00024236, 436.86295168, 0.00080786, -43.68629517, -8.079e-05, -131.0588855, -0.00024236, -436.86295168, -0.00080786, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 174.74518067, 0.01856544, 174.74518067, 0.05569633, 122.32162647, -1616.20815527, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 43.68629517, 8.079e-05, 131.0588855, 0.00024236, 436.86295168, 0.00080786, -43.68629517, -8.079e-05, -131.0588855, -0.00024236, -436.86295168, -0.00080786, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 13.65, 21.25, 3.925)
    ops.node(122024, 13.65, 21.25, 6.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.1225, 29573095.02816795, 12322122.92840331, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 143.55641626, 0.00102235, 172.18619328, 0.01506432, 17.21861933, 0.04321099, -143.55641626, -0.00102235, -172.18619328, -0.01506432, -17.21861933, -0.04321099, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 132.12803931, 0.00102235, 158.47862957, 0.01506432, 15.84786296, 0.04321099, -132.12803931, -0.00102235, -158.47862957, -0.01506432, -15.84786296, -0.04321099, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 148.53495612, 0.02044694, 148.53495612, 0.06134082, 103.97446929, -1617.11392727, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 37.13373903, 9.151e-05, 111.40121709, 0.00027454, 371.33739031, 0.00091515, -37.13373903, -9.151e-05, -111.40121709, -0.00027454, -371.33739031, -0.00091515, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 148.53495612, 0.02044694, 148.53495612, 0.06134082, 103.97446929, -1617.11392727, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 37.13373903, 9.151e-05, 111.40121709, 0.00027454, 371.33739031, 0.00091515, -37.13373903, -9.151e-05, -111.40121709, -0.00027454, -371.33739031, -0.00091515, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171025, 0.0, 25.5, 3.95)
    ops.node(122025, 0.0, 25.5, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1025, 171025, 122025, 0.09, 31020624.39152125, 12925260.16313385, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21025, 57.22304611, 0.00105447, 68.89488095, 0.01603769, 6.8894881, 0.06193942, -57.22304611, -0.00105447, -68.89488095, -0.01603769, -6.8894881, -0.06193942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11025, 61.77940207, 0.00105447, 74.38060083, 0.01603769, 7.43806008, 0.06193942, -61.77940207, -0.00105447, -74.38060083, -0.01603769, -7.43806008, -0.06193942, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21025, 1025, 0.0, 117.36631361, 0.0210893, 117.36631361, 0.06326791, 82.15641952, -1553.92850716, 0.05, 2, 0, 71025, 22025, 2, 3)
    ops.uniaxialMaterial('LimitState', 41025, 29.3415784, 9.383e-05, 88.0247352, 0.00028149, 293.41578401, 0.00093831, -29.3415784, -9.383e-05, -88.0247352, -0.00028149, -293.41578401, -0.00093831, 0.4, 0.3, 0.003, 0.0, 0.0, 21025, 2)
    ops.limitCurve('ThreePoint', 11025, 1025, 0.0, 117.36631361, 0.0210893, 117.36631361, 0.06326791, 82.15641952, -1553.92850716, 0.05, 2, 0, 71025, 22025, 1, 3)
    ops.uniaxialMaterial('LimitState', 31025, 29.3415784, 9.383e-05, 88.0247352, 0.00028149, 293.41578401, 0.00093831, -29.3415784, -9.383e-05, -88.0247352, -0.00028149, -293.41578401, -0.00093831, 0.4, 0.3, 0.003, 0.0, 0.0, 11025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1025, 99999, 'P', 41025, 'Vy', 31025, 'Vz', 21025, 'My', 11025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171025, 71025, 171025, 1025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122025, 122025, 22025, 1025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171026, 2.95, 25.5, 3.95)
    ops.node(122026, 2.95, 25.5, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1026, 171026, 122026, 0.1225, 29592332.04092986, 12330138.35038744, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21026, 121.78264406, 0.00099586, 146.46348296, 0.01500736, 14.6463483, 0.04555388, -121.78264406, -0.00099586, -146.46348296, -0.01500736, -14.6463483, -0.04555388, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11026, 115.63346578, 0.00099586, 139.06809361, 0.01500736, 13.90680936, 0.04555388, -115.63346578, -0.00099586, -139.06809361, -0.01500736, -13.90680936, -0.04555388, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21026, 1026, 0.0, 143.23008758, 0.0199172, 143.23008758, 0.0597516, 100.26106131, -1541.23473629, 0.05, 2, 0, 71026, 22026, 2, 3)
    ops.uniaxialMaterial('LimitState', 41026, 35.8075219, 8.819e-05, 107.42256569, 0.00026457, 358.07521895, 0.00088189, -35.8075219, -8.819e-05, -107.42256569, -0.00026457, -358.07521895, -0.00088189, 0.4, 0.3, 0.003, 0.0, 0.0, 21026, 2)
    ops.limitCurve('ThreePoint', 11026, 1026, 0.0, 143.23008758, 0.0199172, 143.23008758, 0.0597516, 100.26106131, -1541.23473629, 0.05, 2, 0, 71026, 22026, 1, 3)
    ops.uniaxialMaterial('LimitState', 31026, 35.8075219, 8.819e-05, 107.42256569, 0.00026457, 358.07521895, 0.00088189, -35.8075219, -8.819e-05, -107.42256569, -0.00026457, -358.07521895, -0.00088189, 0.4, 0.3, 0.003, 0.0, 0.0, 11026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1026, 99999, 'P', 41026, 'Vy', 31026, 'Vz', 21026, 'My', 11026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171026, 71026, 171026, 1026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122026, 122026, 22026, 1026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171027, 8.3, 25.5, 3.95)
    ops.node(122027, 8.3, 25.5, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1027, 171027, 122027, 0.1225, 28288363.00231304, 11786817.91763043, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21027, 133.91688537, 0.00104548, 160.64104174, 0.01420412, 16.06410417, 0.03965734, -133.91688537, -0.00104548, -160.64104174, -0.01420412, -16.06410417, -0.03965734, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11027, 127.59825795, 0.00104548, 153.06148306, 0.01420412, 15.30614831, 0.03965734, -127.59825795, -0.00104548, -153.06148306, -0.01420412, -15.30614831, -0.03965734, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21027, 1027, 0.0, 144.86037646, 0.02090953, 144.86037646, 0.0627286, 101.40226352, -1638.86935916, 0.05, 2, 0, 71027, 22027, 2, 3)
    ops.uniaxialMaterial('LimitState', 41027, 36.21509411, 9.33e-05, 108.64528234, 0.00027991, 362.15094114, 0.00093304, -36.21509411, -9.33e-05, -108.64528234, -0.00027991, -362.15094114, -0.00093304, 0.4, 0.3, 0.003, 0.0, 0.0, 21027, 2)
    ops.limitCurve('ThreePoint', 11027, 1027, 0.0, 144.86037646, 0.02090953, 144.86037646, 0.0627286, 101.40226352, -1638.86935916, 0.05, 2, 0, 71027, 22027, 1, 3)
    ops.uniaxialMaterial('LimitState', 31027, 36.21509411, 9.33e-05, 108.64528234, 0.00027991, 362.15094114, 0.00093304, -36.21509411, -9.33e-05, -108.64528234, -0.00027991, -362.15094114, -0.00093304, 0.4, 0.3, 0.003, 0.0, 0.0, 11027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1027, 99999, 'P', 41027, 'Vy', 31027, 'Vz', 21027, 'My', 11027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171027, 71027, 171027, 1027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122027, 122027, 22027, 1027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171028, 13.65, 25.5, 3.95)
    ops.node(122028, 13.65, 25.5, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1028, 171028, 122028, 0.0625, 29193245.06808516, 12163852.11170215, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21028, 53.08647881, 0.00134431, 63.42133857, 0.01523399, 6.34213386, 0.05097798, -53.08647881, -0.00134431, -63.42133857, -0.01523399, -6.34213386, -0.05097798, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11028, 56.87588714, 0.00134431, 67.94846778, 0.01523399, 6.79484678, 0.05097798, -56.87588714, -0.00134431, -67.94846778, -0.01523399, -6.79484678, -0.05097798, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21028, 1028, 0.0, 95.38211327, 0.02688621, 95.38211327, 0.08065864, 66.76747929, -1290.98808627, 0.05, 2, 0, 71028, 22028, 2, 3)
    ops.uniaxialMaterial('LimitState', 41028, 23.84552832, 0.00011668, 71.53658496, 0.00035004, 238.45528319, 0.00116681, -23.84552832, -0.00011668, -71.53658496, -0.00035004, -238.45528319, -0.00116681, 0.4, 0.3, 0.003, 0.0, 0.0, 21028, 2)
    ops.limitCurve('ThreePoint', 11028, 1028, 0.0, 95.38211327, 0.02688621, 95.38211327, 0.08065864, 66.76747929, -1290.98808627, 0.05, 2, 0, 71028, 22028, 1, 3)
    ops.uniaxialMaterial('LimitState', 31028, 23.84552832, 0.00011668, 71.53658496, 0.00035004, 238.45528319, 0.00116681, -23.84552832, -0.00011668, -71.53658496, -0.00035004, -238.45528319, -0.00116681, 0.4, 0.3, 0.003, 0.0, 0.0, 11028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1028, 99999, 'P', 41028, 'Vy', 31028, 'Vz', 21028, 'My', 11028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171028, 71028, 171028, 1028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122028, 122028, 22028, 1028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.3, 0.0, 7.05)
    ops.node(123003, 8.3, 0.0, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0625, 30428713.35648407, 12678630.5652017, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 49.55018802, 0.00135321, 59.09903518, 0.01486749, 5.90990352, 0.05273755, -49.55018802, -0.00135321, -59.09903518, -0.01486749, -5.90990352, -0.05273755, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 49.55018802, 0.00135321, 59.09903518, 0.01486749, 5.90990352, 0.05273755, -49.55018802, -0.00135321, -59.09903518, -0.01486749, -5.90990352, -0.05273755, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 98.27306426, 0.02706429, 98.27306426, 0.08119286, 68.79114498, -1288.41652156, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 24.56826606, 0.00011534, 73.70479819, 0.00034601, 245.68266065, 0.00115336, -24.56826606, -0.00011534, -73.70479819, -0.00034601, -245.68266065, -0.00115336, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 98.27306426, 0.02706429, 98.27306426, 0.08119286, 68.79114498, -1288.41652156, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 24.56826606, 0.00011534, 73.70479819, 0.00034601, 245.68266065, 0.00115336, -24.56826606, -0.00011534, -73.70479819, -0.00034601, -245.68266065, -0.00115336, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.65, 0.0, 7.05)
    ops.node(123004, 13.65, 0.0, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 29284838.15243782, 12202015.89684909, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 38.39517267, 0.00134044, 46.2231374, 0.0168402, 4.62231374, 0.06210879, -38.39517267, -0.00134044, -46.2231374, -0.0168402, -4.62231374, -0.06210879, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 38.39517267, 0.00134044, 46.2231374, 0.0168402, 4.62231374, 0.06210879, -38.39517267, -0.00134044, -46.2231374, -0.0168402, -4.62231374, -0.06210879, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 89.9169253, 0.0268087, 89.9169253, 0.08042611, 62.94184771, -1313.56795356, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 22.47923132, 0.00010965, 67.43769397, 0.00032895, 224.79231325, 0.00109651, -22.47923132, -0.00010965, -67.43769397, -0.00032895, -224.79231325, -0.00109651, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 89.9169253, 0.0268087, 89.9169253, 0.08042611, 62.94184771, -1313.56795356, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 22.47923132, 0.00010965, 67.43769397, 0.00032895, 224.79231325, 0.00109651, -22.47923132, -0.00010965, -67.43769397, -0.00032895, -224.79231325, -0.00109651, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.25, 7.0)
    ops.node(123005, 0.0, 4.25, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 27840061.29149565, 11600025.53812319, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 45.24086955, 0.00139871, 54.43243819, 0.01658484, 5.44324382, 0.05630446, -45.24086955, -0.00139871, -54.43243819, -0.01658484, -5.44324382, -0.05630446, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 48.41618888, 0.00139871, 58.25288583, 0.01658484, 5.82528858, 0.05630446, -48.41618888, -0.00139871, -58.25288583, -0.01658484, -5.82528858, -0.05630446, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 87.98702317, 0.02797425, 87.98702317, 0.08392275, 61.59091622, -1281.20967587, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 21.99675579, 0.00011287, 65.99026738, 0.0003386, 219.96755793, 0.00112866, -21.99675579, -0.00011287, -65.99026738, -0.0003386, -219.96755793, -0.00112866, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 87.98702317, 0.02797425, 87.98702317, 0.08392275, 61.59091622, -1281.20967587, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 21.99675579, 0.00011287, 65.99026738, 0.0003386, 219.96755793, 0.00112866, -21.99675579, -0.00011287, -65.99026738, -0.0003386, -219.96755793, -0.00112866, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 2.95, 4.25, 7.0)
    ops.node(123006, 2.95, 4.25, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1225, 28895389.69429726, 12039745.70595719, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 131.66850726, 0.00103277, 158.57802489, 0.01346436, 15.85780249, 0.03831694, -131.66850726, -0.00103277, -158.57802489, -0.01346436, -15.85780249, -0.03831694, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 131.66850726, 0.00103277, 158.57802489, 0.01346436, 15.85780249, 0.03831694, -131.66850726, -0.00103277, -158.57802489, -0.01346436, -15.85780249, -0.03831694, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 127.07624326, 0.02065534, 127.07624326, 0.06196601, 88.95337028, -1226.14097707, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 31.76906082, 8.013e-05, 95.30718245, 0.00024039, 317.69060815, 0.0008013, -31.76906082, -8.013e-05, -95.30718245, -0.00024039, -317.69060815, -0.0008013, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 127.07624326, 0.02065534, 127.07624326, 0.06196601, 88.95337028, -1226.14097707, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 31.76906082, 8.013e-05, 95.30718245, 0.00024039, 317.69060815, 0.0008013, -31.76906082, -8.013e-05, -95.30718245, -0.00024039, -317.69060815, -0.0008013, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 8.3, 4.25, 7.0)
    ops.node(123007, 8.3, 4.25, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 28198308.26073333, 11749295.10863889, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 138.9814246, 0.00106099, 167.12625541, 0.0126432, 16.71262554, 0.03511414, -138.9814246, -0.00106099, -167.12625541, -0.0126432, -16.71262554, -0.03511414, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 138.9814246, 0.00106099, 167.12625541, 0.0126432, 16.71262554, 0.03511414, -138.9814246, -0.00106099, -167.12625541, -0.0126432, -16.71262554, -0.03511414, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 127.12569577, 0.02121983, 127.12569577, 0.06365949, 88.98798704, -1266.31332181, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 31.78142394, 8.214e-05, 95.34427183, 0.00024643, 317.81423943, 0.00082143, -31.78142394, -8.214e-05, -95.34427183, -0.00024643, -317.81423943, -0.00082143, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 127.12569577, 0.02121983, 127.12569577, 0.06365949, 88.98798704, -1266.31332181, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 31.78142394, 8.214e-05, 95.34427183, 0.00024643, 317.81423943, 0.00082143, -31.78142394, -8.214e-05, -95.34427183, -0.00024643, -317.81423943, -0.00082143, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 13.65, 4.25, 7.0)
    ops.node(123008, 13.65, 4.25, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 31794396.62053964, 13247665.25855818, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 62.63956226, 0.00143204, 74.62496641, 0.01554983, 7.46249664, 0.05170235, -62.63956226, -0.00143204, -74.62496641, -0.01554983, -7.46249664, -0.05170235, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 62.63956226, 0.00143204, 74.62496641, 0.01554983, 7.46249664, 0.05170235, -62.63956226, -0.00143204, -74.62496641, -0.01554983, -7.46249664, -0.05170235, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 88.13962293, 0.02864078, 88.13962293, 0.08592234, 61.69773605, -1099.52756186, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 22.03490573, 9.9e-05, 66.1047172, 0.000297, 220.34905732, 0.00099, -22.03490573, -9.9e-05, -66.1047172, -0.000297, -220.34905732, -0.00099, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 88.13962293, 0.02864078, 88.13962293, 0.08592234, 61.69773605, -1099.52756186, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 22.03490573, 9.9e-05, 66.1047172, 0.000297, 220.34905732, 0.00099, -22.03490573, -9.9e-05, -66.1047172, -0.000297, -220.34905732, -0.00099, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.5, 7.0)
    ops.node(123009, 0.0, 8.5, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 31213971.14753272, 13005821.31147197, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 45.00794569, 0.0012985, 53.98468982, 0.01721479, 5.39846898, 0.06542341, -45.00794569, -0.0012985, -53.98468982, -0.01721479, -5.39846898, -0.06542341, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 48.48584206, 0.0012985, 58.15624563, 0.01721479, 5.81562456, 0.06542341, -48.48584206, -0.0012985, -58.15624563, -0.01721479, -5.81562456, -0.06542341, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 93.83613028, 0.02596994, 93.83613028, 0.07790981, 65.6852912, -1296.57929215, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 23.45903257, 0.00010736, 70.37709771, 0.00032207, 234.5903257, 0.00107358, -23.45903257, -0.00010736, -70.37709771, -0.00032207, -234.5903257, -0.00107358, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 93.83613028, 0.02596994, 93.83613028, 0.07790981, 65.6852912, -1296.57929215, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 23.45903257, 0.00010736, 70.37709771, 0.00032207, 234.5903257, 0.00107358, -23.45903257, -0.00010736, -70.37709771, -0.00032207, -234.5903257, -0.00107358, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 2.95, 8.5, 7.0)
    ops.node(123010, 2.95, 8.5, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0625, 30248916.66944319, 12603715.27893466, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 65.07910044, 0.0014317, 77.55833851, 0.01519273, 7.75583385, 0.04673478, -65.07910044, -0.0014317, -77.55833851, -0.01519273, -7.75583385, -0.04673478, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 65.07910044, 0.0014317, 77.55833851, 0.01519273, 7.75583385, 0.04673478, -65.07910044, -0.0014317, -77.55833851, -0.01519273, -7.75583385, -0.04673478, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 87.86134139, 0.028634, 87.86134139, 0.08590201, 61.50293897, -1130.20972966, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 21.96533535, 0.00010373, 65.89600604, 0.00031119, 219.65335348, 0.00103729, -21.96533535, -0.00010373, -65.89600604, -0.00031119, -219.65335348, -0.00103729, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 87.86134139, 0.028634, 87.86134139, 0.08590201, 61.50293897, -1130.20972966, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 21.96533535, 0.00010373, 65.89600604, 0.00031119, 219.65335348, 0.00103729, -21.96533535, -0.00010373, -65.89600604, -0.00031119, -219.65335348, -0.00103729, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.3, 8.5, 7.0)
    ops.node(123011, 8.3, 8.5, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 29723133.21736702, 12384638.84056959, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 137.66078515, 0.00107413, 165.31046438, 0.01298001, 16.53104644, 0.03738015, -137.66078515, -0.00107413, -165.31046438, -0.01298001, -16.53104644, -0.03738015, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 137.66078515, 0.00107413, 165.31046438, 0.01298001, 16.53104644, 0.03738015, -137.66078515, -0.00107413, -165.31046438, -0.01298001, -16.53104644, -0.03738015, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 133.34030451, 0.02148264, 133.34030451, 0.06444792, 93.33821316, -1273.81558463, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 33.33507613, 8.174e-05, 100.00522838, 0.00024521, 333.35076128, 0.00081738, -33.33507613, -8.174e-05, -100.00522838, -0.00024521, -333.35076128, -0.00081738, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 133.34030451, 0.02148264, 133.34030451, 0.06444792, 93.33821316, -1273.81558463, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 33.33507613, 8.174e-05, 100.00522838, 0.00024521, 333.35076128, 0.00081738, -33.33507613, -8.174e-05, -100.00522838, -0.00024521, -333.35076128, -0.00081738, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 13.65, 8.5, 7.0)
    ops.node(123012, 13.65, 8.5, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 30140039.15801616, 12558349.6491734, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 61.38302424, 0.00143887, 73.28576711, 0.01583597, 7.32857671, 0.04880118, -61.38302424, -0.00143887, -73.28576711, -0.01583597, -7.32857671, -0.04880118, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 61.38302424, 0.00143887, 73.28576711, 0.01583597, 7.32857671, 0.04880118, -61.38302424, -0.00143887, -73.28576711, -0.01583597, -7.32857671, -0.04880118, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 88.8452305, 0.02877749, 88.8452305, 0.08633248, 62.19166135, -1133.46497086, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 22.21130762, 0.00010527, 66.63392287, 0.00031581, 222.11307625, 0.0010527, -22.21130762, -0.00010527, -66.63392287, -0.00031581, -222.11307625, -0.0010527, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 88.8452305, 0.02877749, 88.8452305, 0.08633248, 62.19166135, -1133.46497086, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 22.21130762, 0.00010527, 66.63392287, 0.00031581, 222.11307625, 0.0010527, -22.21130762, -0.00010527, -66.63392287, -0.00031581, -222.11307625, -0.0010527, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 12.75, 7.0)
    ops.node(123013, 0.0, 12.75, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 28658988.31722701, 11941245.13217792, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 45.42011696, 0.00131771, 54.69037509, 0.01675519, 5.46903751, 0.06002332, -45.42011696, -0.00131771, -54.69037509, -0.01675519, -5.46903751, -0.06002332, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 49.24680609, 0.00131771, 59.29809251, 0.01675519, 5.92980925, 0.06002332, -49.24680609, -0.00131771, -59.29809251, -0.01675519, -5.92980925, -0.06002332, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 88.13178569, 0.02635424, 88.13178569, 0.07906273, 61.69224999, -1275.17291943, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 22.03294642, 0.00010982, 66.09883927, 0.00032946, 220.32946424, 0.00109821, -22.03294642, -0.00010982, -66.09883927, -0.00032946, -220.32946424, -0.00109821, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 88.13178569, 0.02635424, 88.13178569, 0.07906273, 61.69224999, -1275.17291943, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 22.03294642, 0.00010982, 66.09883927, 0.00032946, 220.32946424, 0.00109821, -22.03294642, -0.00010982, -66.09883927, -0.00032946, -220.32946424, -0.00109821, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 2.95, 12.75, 7.0)
    ops.node(123014, 2.95, 12.75, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 29015982.99376784, 12089992.91406994, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 64.63850138, 0.00147425, 77.07076214, 0.01508207, 7.70707621, 0.04388815, -64.63850138, -0.00147425, -77.07076214, -0.01508207, -7.70707621, -0.04388815, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 64.63850138, 0.00147425, 77.07076214, 0.01508207, 7.70707621, 0.04388815, -64.63850138, -0.00147425, -77.07076214, -0.01508207, -7.70707621, -0.04388815, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 87.96664305, 0.02948507, 87.96664305, 0.08845522, 61.57665014, -1151.79041291, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 21.99166076, 0.00010827, 65.97498229, 0.0003248, 219.91660763, 0.00108267, -21.99166076, -0.00010827, -65.97498229, -0.0003248, -219.91660763, -0.00108267, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 87.96664305, 0.02948507, 87.96664305, 0.08845522, 61.57665014, -1151.79041291, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 21.99166076, 0.00010827, 65.97498229, 0.0003248, 219.91660763, 0.00108267, -21.99166076, -0.00010827, -65.97498229, -0.0003248, -219.91660763, -0.00108267, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 8.3, 12.75, 7.0)
    ops.node(123015, 8.3, 12.75, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 29547375.95342891, 12311406.64726205, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 140.31369078, 0.00103849, 168.53258505, 0.01367416, 16.8532585, 0.03786609, -140.31369078, -0.00103849, -168.53258505, -0.01367416, -16.8532585, -0.03786609, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 140.31369078, 0.00103849, 168.53258505, 0.01367416, 16.8532585, 0.03786609, -140.31369078, -0.00103849, -168.53258505, -0.01367416, -16.8532585, -0.03786609, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 134.07323859, 0.02076983, 134.07323859, 0.0623095, 93.85126701, -1305.05459662, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 33.51830965, 8.268e-05, 100.55492894, 0.00024803, 335.18309647, 0.00082676, -33.51830965, -8.268e-05, -100.55492894, -0.00024803, -335.18309647, -0.00082676, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 134.07323859, 0.02076983, 134.07323859, 0.0623095, 93.85126701, -1305.05459662, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 33.51830965, 8.268e-05, 100.55492894, 0.00024803, 335.18309647, 0.00082676, -33.51830965, -8.268e-05, -100.55492894, -0.00024803, -335.18309647, -0.00082676, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 13.65, 12.75, 7.0)
    ops.node(123016, 13.65, 12.75, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 29170535.41267037, 12154389.75527932, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 62.57485795, 0.00146592, 74.75324854, 0.015295, 7.47532485, 0.04618146, -62.57485795, -0.00146592, -74.75324854, -0.015295, -7.47532485, -0.04618146, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 62.57485795, 0.00146592, 74.75324854, 0.015295, 7.47532485, 0.04618146, -62.57485795, -0.00146592, -74.75324854, -0.015295, -7.47532485, -0.04618146, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 84.03419807, 0.02931836, 84.03419807, 0.08795509, 58.82393865, -1103.78353945, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 21.00854952, 0.00010288, 63.02564855, 0.00030864, 210.08549518, 0.00102879, -21.00854952, -0.00010288, -63.02564855, -0.00030864, -210.08549518, -0.00102879, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 84.03419807, 0.02931836, 84.03419807, 0.08795509, 58.82393865, -1103.78353945, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 21.00854952, 0.00010288, 63.02564855, 0.00030864, 210.08549518, 0.00102879, -21.00854952, -0.00010288, -63.02564855, -0.00030864, -210.08549518, -0.00102879, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 17.0, 7.0)
    ops.node(123017, 0.0, 17.0, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 28037298.35132778, 11682207.64638657, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 44.43925927, 0.00132512, 53.53580317, 0.016652, 5.35358032, 0.05851134, -44.43925927, -0.00132512, -53.53580317, -0.016652, -5.35358032, -0.05851134, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 48.02172974, 0.00132512, 57.85159145, 0.016652, 5.78515915, 0.05851134, -48.02172974, -0.00132512, -57.85159145, -0.016652, -5.78515915, -0.05851134, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 86.45812342, 0.02650243, 86.45812342, 0.07950729, 60.52068639, -1259.73507748, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 21.61453085, 0.00011012, 64.84359256, 0.00033037, 216.14530854, 0.00110124, -21.61453085, -0.00011012, -64.84359256, -0.00033037, -216.14530854, -0.00110124, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 86.45812342, 0.02650243, 86.45812342, 0.07950729, 60.52068639, -1259.73507748, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 21.61453085, 0.00011012, 64.84359256, 0.00033037, 216.14530854, 0.00110124, -21.61453085, -0.00011012, -64.84359256, -0.00033037, -216.14530854, -0.00110124, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 2.95, 17.0, 7.0)
    ops.node(123018, 2.95, 17.0, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 31434178.94242973, 13097574.55934572, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 66.12355027, 0.00142661, 78.70336119, 0.01517275, 7.87033612, 0.04911468, -66.12355027, -0.00142661, -78.70336119, -0.01517275, -7.87033612, -0.04911468, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 66.12355027, 0.00142661, 78.70336119, 0.01517275, 7.87033612, 0.04911468, -66.12355027, -0.00142661, -78.70336119, -0.01517275, -7.87033612, -0.04911468, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 89.63031805, 0.02853213, 89.63031805, 0.08559638, 62.74122263, -1133.92214729, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 22.40757951, 0.00010183, 67.22273854, 0.00030548, 224.07579512, 0.00101828, -22.40757951, -0.00010183, -67.22273854, -0.00030548, -224.07579512, -0.00101828, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 89.63031805, 0.02853213, 89.63031805, 0.08559638, 62.74122263, -1133.92214729, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 22.40757951, 0.00010183, 67.22273854, 0.00030548, 224.07579512, 0.00101828, -22.40757951, -0.00010183, -67.22273854, -0.00030548, -224.07579512, -0.00101828, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 8.3, 17.0, 7.0)
    ops.node(123019, 8.3, 17.0, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1225, 29363664.02316358, 12234860.00965149, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 140.8929489, 0.00104507, 169.26390611, 0.01298669, 16.92639061, 0.03695715, -140.8929489, -0.00104507, -169.26390611, -0.01298669, -16.92639061, -0.03695715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 140.8929489, 0.00104507, 169.26390611, 0.01298669, 16.92639061, 0.03695715, -140.8929489, -0.00104507, -169.26390611, -0.01298669, -16.92639061, -0.03695715, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 132.86746144, 0.02090134, 132.86746144, 0.06270402, 93.00722301, -1294.15300421, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 33.21686536, 8.245e-05, 99.65059608, 0.00024734, 332.16865359, 0.00082445, -33.21686536, -8.245e-05, -99.65059608, -0.00024734, -332.16865359, -0.00082445, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 132.86746144, 0.02090134, 132.86746144, 0.06270402, 93.00722301, -1294.15300421, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 33.21686536, 8.245e-05, 99.65059608, 0.00024734, 332.16865359, 0.00082445, -33.21686536, -8.245e-05, -99.65059608, -0.00024734, -332.16865359, -0.00082445, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 13.65, 17.0, 7.0)
    ops.node(123020, 13.65, 17.0, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 29502791.1085671, 12292829.62856962, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 62.88618277, 0.00142475, 75.11425319, 0.01580933, 7.51142532, 0.04742613, -62.88618277, -0.00142475, -75.11425319, -0.01580933, -7.51142532, -0.04742613, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 62.88618277, 0.00142475, 75.11425319, 0.01580933, 7.51142532, 0.04742613, -62.88618277, -0.00142475, -75.11425319, -0.01580933, -7.51142532, -0.04742613, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 90.24076795, 0.0284949, 90.24076795, 0.08548471, 63.16853756, -1151.93455115, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 22.56019199, 0.00010923, 67.68057596, 0.0003277, 225.60191987, 0.00109233, -22.56019199, -0.00010923, -67.68057596, -0.0003277, -225.60191987, -0.00109233, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 90.24076795, 0.0284949, 90.24076795, 0.08548471, 63.16853756, -1151.93455115, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 22.56019199, 0.00010923, 67.68057596, 0.0003277, 225.60191987, 0.00109233, -22.56019199, -0.00010923, -67.68057596, -0.0003277, -225.60191987, -0.00109233, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 0.0, 21.25, 7.0)
    ops.node(123021, 0.0, 21.25, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 29091600.08226525, 12121500.03427719, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 53.12702167, 0.0013823, 63.94130423, 0.01688237, 6.39413042, 0.05520132, -53.12702167, -0.0013823, -63.94130423, -0.01688237, -6.39413042, -0.05520132, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 53.12702167, 0.0013823, 63.94130423, 0.01688237, 6.39413042, 0.05520132, -53.12702167, -0.0013823, -63.94130423, -0.01688237, -6.39413042, -0.05520132, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 76.29426348, 0.02764599, 76.29426348, 0.08293798, 53.40598443, -1032.29334529, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 19.07356587, 9.366e-05, 57.22069761, 0.00028097, 190.7356587, 0.00093657, -19.07356587, -9.366e-05, -57.22069761, -0.00028097, -190.7356587, -0.00093657, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 76.29426348, 0.02764599, 76.29426348, 0.08293798, 53.40598443, -1032.29334529, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 19.07356587, 9.366e-05, 57.22069761, 0.00028097, 190.7356587, 0.00093657, -19.07356587, -9.366e-05, -57.22069761, -0.00028097, -190.7356587, -0.00093657, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 2.95, 21.25, 7.0)
    ops.node(123022, 2.95, 21.25, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0625, 28929448.73600231, 12053936.9733343, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 65.03605518, 0.00142156, 77.54477394, 0.01582164, 7.75447739, 0.04442651, -65.03605518, -0.00142156, -77.54477394, -0.01582164, -7.75447739, -0.04442651, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 65.03605518, 0.00142156, 77.54477394, 0.01582164, 7.75447739, 0.04442651, -65.03605518, -0.00142156, -77.54477394, -0.01582164, -7.75447739, -0.04442651, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 88.58819596, 0.02843123, 88.58819596, 0.0852937, 62.01173717, -1150.57336832, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 22.14704899, 0.00010936, 66.44114697, 0.00032807, 221.4704899, 0.00109358, -22.14704899, -0.00010936, -66.44114697, -0.00032807, -221.4704899, -0.00109358, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 88.58819596, 0.02843123, 88.58819596, 0.0852937, 62.01173717, -1150.57336832, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 22.14704899, 0.00010936, 66.44114697, 0.00032807, 221.4704899, 0.00109358, -22.14704899, -0.00010936, -66.44114697, -0.00032807, -221.4704899, -0.00109358, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 8.3, 21.25, 7.0)
    ops.node(123023, 8.3, 21.25, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 29240683.46867206, 12183618.11194669, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 139.13988792, 0.00103889, 167.17986435, 0.01326141, 16.71798643, 0.03708139, -139.13988792, -0.00103889, -167.17986435, -0.01326141, -16.71798643, -0.03708139, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 139.13988792, 0.00103889, 167.17986435, 0.01326141, 16.71798643, 0.03708139, -139.13988792, -0.00103889, -167.17986435, -0.01326141, -16.71798643, -0.03708139, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 132.23407076, 0.02077785, 132.23407076, 0.06233356, 92.56384954, -1290.68424368, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 33.05851769, 8.24e-05, 99.17555307, 0.00024719, 330.58517691, 0.00082397, -33.05851769, -8.24e-05, -99.17555307, -0.00024719, -330.58517691, -0.00082397, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 132.23407076, 0.02077785, 132.23407076, 0.06233356, 92.56384954, -1290.68424368, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 33.05851769, 8.24e-05, 99.17555307, 0.00024719, 330.58517691, 0.00082397, -33.05851769, -8.24e-05, -99.17555307, -0.00024719, -330.58517691, -0.00082397, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 13.65, 21.25, 7.0)
    ops.node(123024, 13.65, 21.25, 9.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 30357664.43954884, 12649026.84981202, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 63.31708109, 0.00142156, 75.57943224, 0.0165701, 7.55794322, 0.04998017, -63.31708109, -0.00142156, -75.57943224, -0.0165701, -7.55794322, -0.04998017, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 63.31708109, 0.00142156, 75.57943224, 0.0165701, 7.55794322, 0.04998017, -63.31708109, -0.00142156, -75.57943224, -0.0165701, -7.55794322, -0.04998017, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 91.69920421, 0.02843116, 91.69920421, 0.08529348, 64.18944295, -1154.78421605, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 22.92480105, 0.00010787, 68.77440316, 0.00032362, 229.24801052, 0.00107873, -22.92480105, -0.00010787, -68.77440316, -0.00032362, -229.24801052, -0.00107873, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 91.69920421, 0.02843116, 91.69920421, 0.08529348, 64.18944295, -1154.78421605, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 22.92480105, 0.00010787, 68.77440316, 0.00032362, 229.24801052, 0.00107873, -22.92480105, -0.00010787, -68.77440316, -0.00032362, -229.24801052, -0.00107873, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172025, 0.0, 25.5, 7.05)
    ops.node(123025, 0.0, 25.5, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2025, 172025, 123025, 0.0625, 30059672.92295786, 12524863.71789911, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22025, 38.91480216, 0.0012658, 46.99711802, 0.0180178, 4.6997118, 0.07117403, -38.91480216, -0.0012658, -46.99711802, -0.0180178, -4.6997118, -0.07117403, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12025, 42.43667835, 0.0012658, 51.25046178, 0.0180178, 5.12504618, 0.07117403, -42.43667835, -0.0012658, -51.25046178, -0.0180178, -5.12504618, -0.07117403, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22025, 2025, 0.0, 85.76104463, 0.02531597, 85.76104463, 0.07594792, 60.03273124, -1399.27773891, 0.05, 2, 0, 72025, 23025, 2, 3)
    ops.uniaxialMaterial('LimitState', 42025, 21.44026116, 0.00010189, 64.32078347, 0.00030566, 214.40261158, 0.00101887, -21.44026116, -0.00010189, -64.32078347, -0.00030566, -214.40261158, -0.00101887, 0.4, 0.3, 0.003, 0.0, 0.0, 22025, 2)
    ops.limitCurve('ThreePoint', 12025, 2025, 0.0, 85.76104463, 0.02531597, 85.76104463, 0.07594792, 60.03273124, -1399.27773891, 0.05, 2, 0, 72025, 23025, 1, 3)
    ops.uniaxialMaterial('LimitState', 32025, 21.44026116, 0.00010189, 64.32078347, 0.00030566, 214.40261158, 0.00101887, -21.44026116, -0.00010189, -64.32078347, -0.00030566, -214.40261158, -0.00101887, 0.4, 0.3, 0.003, 0.0, 0.0, 12025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2025, 99999, 'P', 42025, 'Vy', 32025, 'Vz', 22025, 'My', 12025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172025, 72025, 172025, 2025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123025, 123025, 23025, 2025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172026, 2.95, 25.5, 7.05)
    ops.node(123026, 2.95, 25.5, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2026, 172026, 123026, 0.0625, 29223038.73213694, 12176266.13839039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22026, 57.5138177, 0.00141939, 68.97045739, 0.01642057, 6.89704574, 0.05118638, -57.5138177, -0.00141939, -68.97045739, -0.01642057, -6.89704574, -0.05118638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12026, 57.5138177, 0.00141939, 68.97045739, 0.01642057, 6.89704574, 0.05118638, -57.5138177, -0.00141939, -68.97045739, -0.01642057, -6.89704574, -0.05118638, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22026, 2026, 0.0, 83.73386059, 0.02838786, 83.73386059, 0.08516358, 58.61370241, -1089.48489456, 0.05, 2, 0, 72026, 23026, 2, 3)
    ops.uniaxialMaterial('LimitState', 42026, 20.93346515, 0.00010233, 62.80039544, 0.00030698, 209.33465147, 0.00102327, -20.93346515, -0.00010233, -62.80039544, -0.00030698, -209.33465147, -0.00102327, 0.4, 0.3, 0.003, 0.0, 0.0, 22026, 2)
    ops.limitCurve('ThreePoint', 12026, 2026, 0.0, 83.73386059, 0.02838786, 83.73386059, 0.08516358, 58.61370241, -1089.48489456, 0.05, 2, 0, 72026, 23026, 1, 3)
    ops.uniaxialMaterial('LimitState', 32026, 20.93346515, 0.00010233, 62.80039544, 0.00030698, 209.33465147, 0.00102327, -20.93346515, -0.00010233, -62.80039544, -0.00030698, -209.33465147, -0.00102327, 0.4, 0.3, 0.003, 0.0, 0.0, 12026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2026, 99999, 'P', 42026, 'Vy', 32026, 'Vz', 22026, 'My', 12026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172026, 72026, 172026, 2026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123026, 123026, 23026, 2026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172027, 8.3, 25.5, 7.05)
    ops.node(123027, 8.3, 25.5, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2027, 172027, 123027, 0.0625, 27588891.6174261, 11495371.50726088, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22027, 63.07410654, 0.00147861, 75.25662843, 0.01464269, 7.52566284, 0.04099088, -63.07410654, -0.00147861, -75.25662843, -0.01464269, -7.52566284, -0.04099088, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12027, 63.07410654, 0.00147861, 75.25662843, 0.01464269, 7.52566284, 0.04099088, -63.07410654, -0.00147861, -75.25662843, -0.01464269, -7.52566284, -0.04099088, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22027, 2027, 0.0, 81.90824108, 0.02957217, 81.90824108, 0.0887165, 57.33576875, -1119.51291826, 0.05, 2, 0, 72027, 23027, 2, 3)
    ops.uniaxialMaterial('LimitState', 42027, 20.47706027, 0.00010602, 61.43118081, 0.00031807, 204.7706027, 0.00106025, -20.47706027, -0.00010602, -61.43118081, -0.00031807, -204.7706027, -0.00106025, 0.4, 0.3, 0.003, 0.0, 0.0, 22027, 2)
    ops.limitCurve('ThreePoint', 12027, 2027, 0.0, 81.90824108, 0.02957217, 81.90824108, 0.0887165, 57.33576875, -1119.51291826, 0.05, 2, 0, 72027, 23027, 1, 3)
    ops.uniaxialMaterial('LimitState', 32027, 20.47706027, 0.00010602, 61.43118081, 0.00031807, 204.7706027, 0.00106025, -20.47706027, -0.00010602, -61.43118081, -0.00031807, -204.7706027, -0.00106025, 0.4, 0.3, 0.003, 0.0, 0.0, 12027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2027, 99999, 'P', 42027, 'Vy', 32027, 'Vz', 22027, 'My', 12027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172027, 72027, 172027, 2027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123027, 123027, 23027, 2027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172028, 13.65, 25.5, 7.05)
    ops.node(123028, 13.65, 25.5, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2028, 172028, 123028, 0.0625, 30239701.23109622, 12599875.51295676, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22028, 47.80112579, 0.00130348, 57.4644829, 0.01745101, 5.74644829, 0.06455221, -47.80112579, -0.00130348, -57.4644829, -0.01745101, -5.74644829, -0.06455221, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12028, 44.29355742, 0.00130348, 53.24783319, 0.01745101, 5.32478332, 0.06455221, -44.29355742, -0.00130348, -53.24783319, -0.01745101, -5.32478332, -0.06455221, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22028, 2028, 0.0, 91.47479996, 0.02606968, 91.47479996, 0.07820905, 64.03235997, -1303.04375405, 0.05, 2, 0, 72028, 23028, 2, 3)
    ops.uniaxialMaterial('LimitState', 42028, 22.86869999, 0.00010803, 68.60609997, 0.00032409, 228.68699989, 0.00108028, -22.86869999, -0.00010803, -68.60609997, -0.00032409, -228.68699989, -0.00108028, 0.4, 0.3, 0.003, 0.0, 0.0, 22028, 2)
    ops.limitCurve('ThreePoint', 12028, 2028, 0.0, 91.47479996, 0.02606968, 91.47479996, 0.07820905, 64.03235997, -1303.04375405, 0.05, 2, 0, 72028, 23028, 1, 3)
    ops.uniaxialMaterial('LimitState', 32028, 22.86869999, 0.00010803, 68.60609997, 0.00032409, 228.68699989, 0.00108028, -22.86869999, -0.00010803, -68.60609997, -0.00032409, -228.68699989, -0.00108028, 0.4, 0.3, 0.003, 0.0, 0.0, 12028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2028, 99999, 'P', 42028, 'Vy', 32028, 'Vz', 22028, 'My', 12028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172028, 72028, 172028, 2028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123028, 123028, 23028, 2028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.3, 0.0, 10.15)
    ops.node(124003, 8.3, 0.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0625, 28955036.54104822, 12064598.55877009, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 31.93612652, 0.00128889, 38.66288593, 0.01808733, 3.86628859, 0.07014369, -31.93612652, -0.00128889, -38.66288593, -0.01808733, -3.86628859, -0.07014369, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 31.93612652, 0.00128889, 38.66288593, 0.01808733, 3.86628859, 0.07014369, -31.93612652, -0.00128889, -38.66288593, -0.01808733, -3.86628859, -0.07014369, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 84.28693599, 0.02577777, 84.28693599, 0.07733332, 59.00085519, -1457.92722556, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 21.071734, 0.00010396, 63.21520199, 0.00031187, 210.71733997, 0.00103956, -21.071734, -0.00010396, -63.21520199, -0.00031187, -210.71733997, -0.00103956, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 84.28693599, 0.02577777, 84.28693599, 0.07733332, 59.00085519, -1457.92722556, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 21.071734, 0.00010396, 63.21520199, 0.00031187, 210.71733997, 0.00103956, -21.071734, -0.00010396, -63.21520199, -0.00031187, -210.71733997, -0.00103956, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.65, 0.0, 10.15)
    ops.node(124004, 13.65, 0.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 29679217.27517597, 12366340.53132332, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 26.96845306, 0.00115938, 32.72118494, 0.01836059, 3.27211849, 0.07742158, -26.96845306, -0.00115938, -32.72118494, -0.01836059, -3.27211849, -0.07742158, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 26.96845306, 0.00115938, 32.72118494, 0.01836059, 3.27211849, 0.07742158, -26.96845306, -0.00115938, -32.72118494, -0.01836059, -3.27211849, -0.07742158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 79.39172338, 0.02318751, 79.39172338, 0.06956252, 55.57420637, -1787.43475114, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 19.84793085, 9.553e-05, 59.54379254, 0.00028659, 198.47930846, 0.00095529, -19.84793085, -9.553e-05, -59.54379254, -0.00028659, -198.47930846, -0.00095529, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 79.39172338, 0.02318751, 79.39172338, 0.06956252, 55.57420637, -1787.43475114, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 19.84793085, 9.553e-05, 59.54379254, 0.00028659, 198.47930846, 0.00095529, -19.84793085, -9.553e-05, -59.54379254, -0.00028659, -198.47930846, -0.00095529, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.25, 10.125)
    ops.node(124005, 0.0, 4.25, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 27817500.66166507, 11590625.27569378, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 27.35625605, 0.001261, 33.28407558, 0.019119, 3.32840756, 0.07444717, -27.35625605, -0.001261, -33.28407558, -0.019119, -3.32840756, -0.07444717, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 27.35625605, 0.001261, 33.28407558, 0.019119, 3.32840756, 0.07444717, -27.35625605, -0.001261, -33.28407558, -0.019119, -3.32840756, -0.07444717, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 79.21238777, 0.02522006, 79.21238777, 0.07566017, 55.44867144, -1729.84219664, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 19.80309694, 0.00010169, 59.40929083, 0.00030508, 198.03096942, 0.00101693, -19.80309694, -0.00010169, -59.40929083, -0.00030508, -198.03096942, -0.00101693, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 79.21238777, 0.02522006, 79.21238777, 0.07566017, 55.44867144, -1729.84219664, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 19.80309694, 0.00010169, 59.40929083, 0.00030508, 198.03096942, 0.00101693, -19.80309694, -0.00010169, -59.40929083, -0.00030508, -198.03096942, -0.00101693, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 2.95, 4.25, 10.125)
    ops.node(124006, 2.95, 4.25, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1225, 29866529.81731981, 12444387.42388326, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 106.71127537, 0.0009809, 129.23258019, 0.0148471, 12.92325802, 0.04663211, -106.71127537, -0.0009809, -129.23258019, -0.0148471, -12.92325802, -0.04663211, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 106.71127537, 0.0009809, 129.23258019, 0.0148471, 12.92325802, 0.04663211, -106.71127537, -0.0009809, -129.23258019, -0.0148471, -12.92325802, -0.04663211, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 116.64687614, 0.01961808, 116.64687614, 0.05885423, 81.6528133, -1143.07239771, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 29.16171903, 7.116e-05, 87.4851571, 0.00021349, 291.61719035, 0.00071162, -29.16171903, -7.116e-05, -87.4851571, -0.00021349, -291.61719035, -0.00071162, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 116.64687614, 0.01961808, 116.64687614, 0.05885423, 81.6528133, -1143.07239771, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 29.16171903, 7.116e-05, 87.4851571, 0.00021349, 291.61719035, 0.00071162, -29.16171903, -7.116e-05, -87.4851571, -0.00021349, -291.61719035, -0.00071162, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 8.3, 4.25, 10.125)
    ops.node(124007, 8.3, 4.25, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 29242134.9825918, 12184222.90941325, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 108.96916411, 0.00098979, 131.9892938, 0.01497393, 13.19892938, 0.04527151, -108.96916411, -0.00098979, -131.9892938, -0.01497393, -13.19892938, -0.04527151, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 108.96916411, 0.00098979, 131.9892938, 0.01497393, 13.19892938, 0.04527151, -108.96916411, -0.00098979, -131.9892938, -0.01497393, -13.19892938, -0.04527151, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 117.61651336, 0.01979574, 117.61651336, 0.05938723, 82.33155935, -1151.96975941, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 29.40412834, 7.329e-05, 88.21238502, 0.00021986, 294.0412834, 0.00073285, -29.40412834, -7.329e-05, -88.21238502, -0.00021986, -294.0412834, -0.00073285, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 117.61651336, 0.01979574, 117.61651336, 0.05938723, 82.33155935, -1151.96975941, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 29.40412834, 7.329e-05, 88.21238502, 0.00021986, 294.0412834, 0.00073285, -29.40412834, -7.329e-05, -88.21238502, -0.00021986, -294.0412834, -0.00073285, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 13.65, 4.25, 10.125)
    ops.node(124008, 13.65, 4.25, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 29487427.62516078, 12286428.17715032, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 46.71318263, 0.00132136, 56.48659736, 0.01819293, 5.64865974, 0.06374421, -46.71318263, -0.00132136, -56.48659736, -0.01819293, -5.64865974, -0.06374421, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 46.71318263, 0.00132136, 56.48659736, 0.01819293, 5.64865974, 0.06374421, -46.71318263, -0.00132136, -56.48659736, -0.01819293, -5.64865974, -0.06374421, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 72.11714773, 0.02642712, 72.11714773, 0.07928135, 50.48200341, -1084.80381304, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 18.02928693, 8.734e-05, 54.0878608, 0.00026202, 180.29286933, 0.00087341, -18.02928693, -8.734e-05, -54.0878608, -0.00026202, -180.29286933, -0.00087341, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 72.11714773, 0.02642712, 72.11714773, 0.07928135, 50.48200341, -1084.80381304, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 18.02928693, 8.734e-05, 54.0878608, 0.00026202, 180.29286933, 0.00087341, -18.02928693, -8.734e-05, -54.0878608, -0.00026202, -180.29286933, -0.00087341, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.5, 10.125)
    ops.node(124009, 0.0, 8.5, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 29304343.46012599, 12210143.10838583, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 27.47332417, 0.0012119, 33.35291937, 0.01830982, 3.33529194, 0.07652033, -27.47332417, -0.0012119, -33.35291937, -0.01830982, -3.33529194, -0.07652033, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 27.47332417, 0.0012119, 33.35291937, 0.01830982, 3.33529194, 0.07652033, -27.47332417, -0.0012119, -33.35291937, -0.01830982, -3.33529194, -0.07652033, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 79.13220097, 0.02423798, 79.13220097, 0.07271394, 55.39254068, -1728.10096936, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 19.78305024, 9.644e-05, 59.34915073, 0.00028931, 197.83050243, 0.00096435, -19.78305024, -9.644e-05, -59.34915073, -0.00028931, -197.83050243, -0.00096435, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 79.13220097, 0.02423798, 79.13220097, 0.07271394, 55.39254068, -1728.10096936, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 19.78305024, 9.644e-05, 59.34915073, 0.00028931, 197.83050243, 0.00096435, -19.78305024, -9.644e-05, -59.34915073, -0.00028931, -197.83050243, -0.00096435, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 2.95, 8.5, 10.125)
    ops.node(124010, 2.95, 8.5, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0625, 29156999.72786552, 12148749.88661063, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 48.87544373, 0.00138531, 58.99728302, 0.01785568, 5.8997283, 0.05990477, -48.87544373, -0.00138531, -58.99728302, -0.01785568, -5.8997283, -0.05990477, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 48.87544373, 0.00138531, 58.99728302, 0.01785568, 5.8997283, 0.05990477, -48.87544373, -0.00138531, -58.99728302, -0.01785568, -5.8997283, -0.05990477, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 76.24378753, 0.02770626, 76.24378753, 0.08311877, 53.37065127, -1074.4899422, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 19.06094688, 9.338e-05, 57.18284065, 0.00028015, 190.60946883, 0.00093385, -19.06094688, -9.338e-05, -57.18284065, -0.00028015, -190.60946883, -0.00093385, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 76.24378753, 0.02770626, 76.24378753, 0.08311877, 53.37065127, -1074.4899422, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 19.06094688, 9.338e-05, 57.18284065, 0.00028015, 190.60946883, 0.00093385, -19.06094688, -9.338e-05, -57.18284065, -0.00028015, -190.60946883, -0.00093385, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.3, 8.5, 10.125)
    ops.node(124011, 8.3, 8.5, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 29607508.99708243, 12336462.08211768, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 109.56753859, 0.00100368, 132.61594532, 0.01478542, 13.26159453, 0.04534547, -109.56753859, -0.00100368, -132.61594532, -0.01478542, -13.26159453, -0.04534547, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 109.56753859, 0.00100368, 132.61594532, 0.01478542, 13.26159453, 0.04534547, -109.56753859, -0.00100368, -132.61594532, -0.01478542, -13.26159453, -0.04534547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 118.24685354, 0.02007356, 118.24685354, 0.06022067, 82.77279748, -1130.51102326, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 29.56171339, 7.277e-05, 88.68514016, 0.00021831, 295.61713386, 0.00072769, -29.56171339, -7.277e-05, -88.68514016, -0.00021831, -295.61713386, -0.00072769, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 118.24685354, 0.02007356, 118.24685354, 0.06022067, 82.77279748, -1130.51102326, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 29.56171339, 7.277e-05, 88.68514016, 0.00021831, 295.61713386, 0.00072769, -29.56171339, -7.277e-05, -88.68514016, -0.00021831, -295.61713386, -0.00072769, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 13.65, 8.5, 10.125)
    ops.node(124012, 13.65, 8.5, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 31247713.66914677, 13019880.69547782, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 46.79720207, 0.00132095, 56.36736032, 0.01798284, 5.63673603, 0.06551563, -46.79720207, -0.00132095, -56.36736032, -0.01798284, -5.63673603, -0.06551563, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 46.79720207, 0.00132095, 56.36736032, 0.01798284, 5.63673603, 0.06551563, -46.79720207, -0.00132095, -56.36736032, -0.01798284, -5.63673603, -0.06551563, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 75.93499739, 0.02641905, 75.93499739, 0.07925714, 53.15449817, -1085.45781229, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 18.98374935, 8.678e-05, 56.95124804, 0.00026035, 189.83749347, 0.00086784, -18.98374935, -8.678e-05, -56.95124804, -0.00026035, -189.83749347, -0.00086784, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 75.93499739, 0.02641905, 75.93499739, 0.07925714, 53.15449817, -1085.45781229, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 18.98374935, 8.678e-05, 56.95124804, 0.00026035, 189.83749347, 0.00086784, -18.98374935, -8.678e-05, -56.95124804, -0.00026035, -189.83749347, -0.00086784, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 12.75, 10.125)
    ops.node(124013, 0.0, 12.75, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 28440869.5059365, 11850362.29414021, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 27.20747482, 0.00119963, 33.09085338, 0.0192033, 3.30908534, 0.07656693, -27.20747482, -0.00119963, -33.09085338, -0.0192033, -3.30908534, -0.07656693, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 27.20747482, 0.00119963, 33.09085338, 0.0192033, 3.30908534, 0.07656693, -27.20747482, -0.00119963, -33.09085338, -0.0192033, -3.30908534, -0.07656693, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 79.6744574, 0.02399263, 79.6744574, 0.07197788, 55.77212018, -1866.3917914, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 19.91861435, 0.00010004, 59.75584305, 0.00030013, 199.1861435, 0.00100044, -19.91861435, -0.00010004, -59.75584305, -0.00030013, -199.1861435, -0.00100044, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 79.6744574, 0.02399263, 79.6744574, 0.07197788, 55.77212018, -1866.3917914, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 19.91861435, 0.00010004, 59.75584305, 0.00030013, 199.1861435, 0.00100044, -19.91861435, -0.00010004, -59.75584305, -0.00030013, -199.1861435, -0.00100044, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 2.95, 12.75, 10.125)
    ops.node(124014, 2.95, 12.75, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 29066461.71069028, 12111025.71278762, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 50.00237423, 0.00133525, 60.36580633, 0.01790682, 6.03658063, 0.05981492, -50.00237423, -0.00133525, -60.36580633, -0.01790682, -6.03658063, -0.05981492, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 50.00237423, 0.00133525, 60.36580633, 0.01790682, 6.03658063, 0.05981492, -50.00237423, -0.00133525, -60.36580633, -0.01790682, -6.03658063, -0.05981492, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 76.38710073, 0.02670497, 76.38710073, 0.08011491, 53.47097051, -1060.78526391, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 19.09677518, 9.385e-05, 57.29032555, 0.00028156, 190.96775182, 0.00093852, -19.09677518, -9.385e-05, -57.29032555, -0.00028156, -190.96775182, -0.00093852, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 76.38710073, 0.02670497, 76.38710073, 0.08011491, 53.47097051, -1060.78526391, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 19.09677518, 9.385e-05, 57.29032555, 0.00028156, 190.96775182, 0.00093852, -19.09677518, -9.385e-05, -57.29032555, -0.00028156, -190.96775182, -0.00093852, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 8.3, 12.75, 10.125)
    ops.node(124015, 8.3, 12.75, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 28002062.98764221, 11667526.24485092, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 108.50317763, 0.00101685, 131.70984812, 0.01526007, 13.17098481, 0.04457243, -108.50317763, -0.00101685, -131.70984812, -0.01526007, -13.17098481, -0.04457243, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 108.50317763, 0.00101685, 131.70984812, 0.01526007, 13.17098481, 0.04457243, -108.50317763, -0.00101685, -131.70984812, -0.01526007, -13.17098481, -0.04457243, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 111.73672282, 0.02033693, 111.73672282, 0.06101079, 78.21570598, -1109.55788192, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 27.93418071, 7.27e-05, 83.80254212, 0.00021811, 279.34180706, 0.00072705, -27.93418071, -7.27e-05, -83.80254212, -0.00021811, -279.34180706, -0.00072705, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 111.73672282, 0.02033693, 111.73672282, 0.06101079, 78.21570598, -1109.55788192, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 27.93418071, 7.27e-05, 83.80254212, 0.00021811, 279.34180706, 0.00072705, -27.93418071, -7.27e-05, -83.80254212, -0.00021811, -279.34180706, -0.00072705, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 13.65, 12.75, 10.125)
    ops.node(124016, 13.65, 12.75, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 30064246.19062177, 12526769.24609241, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 45.93287618, 0.0014008, 55.47853396, 0.01800905, 5.5478534, 0.06425575, -45.93287618, -0.0014008, -55.47853396, -0.01800905, -5.5478534, -0.06425575, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 45.93287618, 0.0014008, 55.47853396, 0.01800905, 5.5478534, 0.06425575, -45.93287618, -0.0014008, -55.47853396, -0.01800905, -5.5478534, -0.06425575, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 71.97677456, 0.02801602, 71.97677456, 0.08404807, 50.38374219, -1055.93129575, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 17.99419364, 8.55e-05, 53.98258092, 0.00025649, 179.9419364, 0.00085498, -17.99419364, -8.55e-05, -53.98258092, -0.00025649, -179.9419364, -0.00085498, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 71.97677456, 0.02801602, 71.97677456, 0.08404807, 50.38374219, -1055.93129575, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 17.99419364, 8.55e-05, 53.98258092, 0.00025649, 179.9419364, 0.00085498, -17.99419364, -8.55e-05, -53.98258092, -0.00025649, -179.9419364, -0.00085498, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 17.0, 10.125)
    ops.node(124017, 0.0, 17.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 29855066.03650594, 12439610.84854414, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 26.92954182, 0.00117206, 32.65067906, 0.01831258, 3.26506791, 0.07701485, -26.92954182, -0.00117206, -32.65067906, -0.01831258, -3.26506791, -0.07701485, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 26.92954182, 0.00117206, 32.65067906, 0.01831258, 3.26506791, 0.07701485, -26.92954182, -0.00117206, -32.65067906, -0.01831258, -3.26506791, -0.07701485, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 79.93795828, 0.02344126, 79.93795828, 0.07032379, 55.9565708, -1714.45930089, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 19.98448957, 9.562e-05, 59.95346871, 0.00028686, 199.84489571, 0.0009562, -19.98448957, -9.562e-05, -59.95346871, -0.00028686, -199.84489571, -0.0009562, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 79.93795828, 0.02344126, 79.93795828, 0.07032379, 55.9565708, -1714.45930089, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 19.98448957, 9.562e-05, 59.95346871, 0.00028686, 199.84489571, 0.0009562, -19.98448957, -9.562e-05, -59.95346871, -0.00028686, -199.84489571, -0.0009562, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 2.95, 17.0, 10.125)
    ops.node(124018, 2.95, 17.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 28802750.10365355, 12001145.87652231, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 49.04785746, 0.00135919, 59.23579666, 0.01770605, 5.92357967, 0.05919529, -49.04785746, -0.00135919, -59.23579666, -0.01770605, -5.92357967, -0.05919529, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 49.04785746, 0.00135919, 59.23579666, 0.01770605, 5.92357967, 0.05919529, -49.04785746, -0.00135919, -59.23579666, -0.01770605, -5.92357967, -0.05919529, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 73.72702229, 0.02718386, 73.72702229, 0.08155159, 51.6089156, -1053.23286638, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 18.43175557, 9.141e-05, 55.29526671, 0.00027424, 184.31755572, 0.00091413, -18.43175557, -9.141e-05, -55.29526671, -0.00027424, -184.31755572, -0.00091413, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 73.72702229, 0.02718386, 73.72702229, 0.08155159, 51.6089156, -1053.23286638, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 18.43175557, 9.141e-05, 55.29526671, 0.00027424, 184.31755572, 0.00091413, -18.43175557, -9.141e-05, -55.29526671, -0.00027424, -184.31755572, -0.00091413, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 8.3, 17.0, 10.125)
    ops.node(124019, 8.3, 17.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1225, 29308508.27293496, 12211878.44705623, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 110.7772999, 0.00098211, 134.16182923, 0.01464762, 13.41618292, 0.04499376, -110.7772999, -0.00098211, -134.16182923, -0.01464762, -13.41618292, -0.04499376, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 110.7772999, 0.00098211, 134.16182923, 0.01464762, 13.41618292, 0.04499376, -110.7772999, -0.00098211, -134.16182923, -0.01464762, -13.41618292, -0.04499376, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 116.32566202, 0.01964223, 116.32566202, 0.05892669, 81.42796341, -1105.81048165, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 29.08141551, 7.232e-05, 87.24424652, 0.00021695, 290.81415505, 0.00072317, -29.08141551, -7.232e-05, -87.24424652, -0.00021695, -290.81415505, -0.00072317, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 116.32566202, 0.01964223, 116.32566202, 0.05892669, 81.42796341, -1105.81048165, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 29.08141551, 7.232e-05, 87.24424652, 0.00021695, 290.81415505, 0.00072317, -29.08141551, -7.232e-05, -87.24424652, -0.00021695, -290.81415505, -0.00072317, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 13.65, 17.0, 10.125)
    ops.node(124020, 13.65, 17.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 29822002.39648008, 12425834.3318667, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 46.81948081, 0.00130954, 56.57780561, 0.01844116, 5.65778056, 0.06440163, -46.81948081, -0.00130954, -56.57780561, -0.01844116, -5.65778056, -0.06440163, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 46.81948081, 0.00130954, 56.57780561, 0.01844116, 5.65778056, 0.06440163, -46.81948081, -0.00130954, -56.57780561, -0.01844116, -5.65778056, -0.06440163, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 75.01397648, 0.02619071, 75.01397648, 0.07857214, 52.50978353, -1096.99134647, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 18.75349412, 8.983e-05, 56.26048236, 0.00026949, 187.53494119, 0.0008983, -18.75349412, -8.983e-05, -56.26048236, -0.00026949, -187.53494119, -0.0008983, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 75.01397648, 0.02619071, 75.01397648, 0.07857214, 52.50978353, -1096.99134647, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 18.75349412, 8.983e-05, 56.26048236, 0.00026949, 187.53494119, 0.0008983, -18.75349412, -8.983e-05, -56.26048236, -0.00026949, -187.53494119, -0.0008983, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 0.0, 21.25, 10.125)
    ops.node(124021, 0.0, 21.25, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 29864763.85110749, 12443651.60462812, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 42.33739504, 0.00129013, 51.33069949, 0.01924439, 5.13306995, 0.07014563, -42.33739504, -0.00129013, -51.33069949, -0.01924439, -5.13306995, -0.07014563, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 42.33739504, 0.00129013, 51.33069949, 0.01924439, 5.13306995, 0.07014563, -42.33739504, -0.00129013, -51.33069949, -0.01924439, -5.13306995, -0.07014563, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 71.18720876, 0.02580268, 71.18720876, 0.07740805, 49.83104613, -1361.00672469, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 17.79680219, 8.512e-05, 53.39040657, 0.00025537, 177.96802191, 0.00085125, -17.79680219, -8.512e-05, -53.39040657, -0.00025537, -177.96802191, -0.00085125, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 71.18720876, 0.02580268, 71.18720876, 0.07740805, 49.83104613, -1361.00672469, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 17.79680219, 8.512e-05, 53.39040657, 0.00025537, 177.96802191, 0.00085125, -17.79680219, -8.512e-05, -53.39040657, -0.00025537, -177.96802191, -0.00085125, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 2.95, 21.25, 10.125)
    ops.node(124022, 2.95, 21.25, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0625, 28663243.73848553, 11943018.22436897, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 50.15843389, 0.00135479, 60.58844211, 0.01855644, 6.05884421, 0.05981906, -50.15843389, -0.00135479, -60.58844211, -0.01855644, -6.05884421, -0.05981906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 50.15843389, 0.00135479, 60.58844211, 0.01855644, 6.05884421, 0.05981906, -50.15843389, -0.00135479, -60.58844211, -0.01855644, -6.05884421, -0.05981906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 75.74032028, 0.02709576, 75.74032028, 0.08128728, 53.0182242, -1084.66028685, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 18.93508007, 9.437e-05, 56.80524021, 0.0002831, 189.3508007, 0.00094366, -18.93508007, -9.437e-05, -56.80524021, -0.0002831, -189.3508007, -0.00094366, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 75.74032028, 0.02709576, 75.74032028, 0.08128728, 53.0182242, -1084.66028685, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 18.93508007, 9.437e-05, 56.80524021, 0.0002831, 189.3508007, 0.00094366, -18.93508007, -9.437e-05, -56.80524021, -0.0002831, -189.3508007, -0.00094366, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 8.3, 21.25, 10.125)
    ops.node(124023, 8.3, 21.25, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 30559715.08953976, 12733214.62064156, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 107.85964029, 0.00101013, 130.26987391, 0.01468812, 13.02698739, 0.04587924, -107.85964029, -0.00101013, -130.26987391, -0.01468812, -13.02698739, -0.04587924, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 107.85964029, 0.00101013, 130.26987391, 0.01468812, 13.02698739, 0.04587924, -107.85964029, -0.00101013, -130.26987391, -0.01468812, -13.02698739, -0.04587924, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 120.97204171, 0.02020259, 120.97204171, 0.06060776, 84.68042919, -1106.20018873, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 30.24301043, 7.213e-05, 90.72903128, 0.00021638, 302.43010426, 0.00072126, -30.24301043, -7.213e-05, -90.72903128, -0.00021638, -302.43010426, -0.00072126, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 120.97204171, 0.02020259, 120.97204171, 0.06060776, 84.68042919, -1106.20018873, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 30.24301043, 7.213e-05, 90.72903128, 0.00021638, 302.43010426, 0.00072126, -30.24301043, -7.213e-05, -90.72903128, -0.00021638, -302.43010426, -0.00072126, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 13.65, 21.25, 10.125)
    ops.node(124024, 13.65, 21.25, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 30179067.18952144, 12574611.32896727, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 45.78471813, 0.00135647, 55.28602114, 0.0194713, 5.52860211, 0.06585082, -45.78471813, -0.00135647, -55.28602114, -0.0194713, -5.52860211, -0.06585082, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 45.78471813, 0.00135647, 55.28602114, 0.0194713, 5.52860211, 0.06585082, -45.78471813, -0.00135647, -55.28602114, -0.0194713, -5.52860211, -0.06585082, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 78.02433614, 0.02712949, 78.02433614, 0.08138848, 54.6170353, -1127.18724127, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 19.50608403, 9.233e-05, 58.5182521, 0.00027699, 195.06084035, 0.00092329, -19.50608403, -9.233e-05, -58.5182521, -0.00027699, -195.06084035, -0.00092329, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 78.02433614, 0.02712949, 78.02433614, 0.08138848, 54.6170353, -1127.18724127, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 19.50608403, 9.233e-05, 58.5182521, 0.00027699, 195.06084035, 0.00092329, -19.50608403, -9.233e-05, -58.5182521, -0.00027699, -195.06084035, -0.00092329, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173025, 0.0, 25.5, 10.15)
    ops.node(124025, 0.0, 25.5, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3025, 173025, 124025, 0.0625, 28529746.39561564, 11887394.33150652, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23025, 24.55638164, 0.00117065, 29.93111096, 0.01922359, 2.9931111, 0.08082968, -24.55638164, -0.00117065, -29.93111096, -0.01922359, -2.9931111, -0.08082968, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13025, 24.55638164, 0.00117065, 29.93111096, 0.01922359, 2.9931111, 0.08082968, -24.55638164, -0.00117065, -29.93111096, -0.01922359, -2.9931111, -0.08082968, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23025, 3025, 0.0, 76.34145384, 0.02341292, 76.34145384, 0.07023876, 53.43901769, -2664.08770011, 0.05, 2, 0, 73025, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 43025, 19.08536346, 9.556e-05, 57.25609038, 0.00028668, 190.85363461, 0.0009556, -19.08536346, -9.556e-05, -57.25609038, -0.00028668, -190.85363461, -0.0009556, 0.4, 0.3, 0.003, 0.0, 0.0, 23025, 2)
    ops.limitCurve('ThreePoint', 13025, 3025, 0.0, 76.34145384, 0.02341292, 76.34145384, 0.07023876, 53.43901769, -2664.08770011, 0.05, 2, 0, 73025, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 33025, 19.08536346, 9.556e-05, 57.25609038, 0.00028668, 190.85363461, 0.0009556, -19.08536346, -9.556e-05, -57.25609038, -0.00028668, -190.85363461, -0.0009556, 0.4, 0.3, 0.003, 0.0, 0.0, 13025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3025, 99999, 'P', 43025, 'Vy', 33025, 'Vz', 23025, 'My', 13025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173025, 73025, 173025, 3025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 3025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173026, 2.95, 25.5, 10.15)
    ops.node(124026, 2.95, 25.5, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3026, 173026, 124026, 0.0625, 30502924.87761529, 12709552.03233971, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23026, 45.21292309, 0.00129114, 54.64801331, 0.01843059, 5.46480133, 0.06757123, -45.21292309, -0.00129114, -54.64801331, -0.01843059, -5.46480133, -0.06757123, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13026, 45.21292309, 0.00129114, 54.64801331, 0.01843059, 5.46480133, 0.06757123, -45.21292309, -0.00129114, -54.64801331, -0.01843059, -5.46480133, -0.06757123, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23026, 3026, 0.0, 72.46084908, 0.02582289, 72.46084908, 0.07746867, 50.72259436, -1182.88531338, 0.05, 2, 0, 73026, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 43026, 18.11521227, 8.484e-05, 54.34563681, 0.00025451, 181.1521227, 0.00084835, -18.11521227, -8.484e-05, -54.34563681, -0.00025451, -181.1521227, -0.00084835, 0.4, 0.3, 0.003, 0.0, 0.0, 23026, 2)
    ops.limitCurve('ThreePoint', 13026, 3026, 0.0, 72.46084908, 0.02582289, 72.46084908, 0.07746867, 50.72259436, -1182.88531338, 0.05, 2, 0, 73026, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 33026, 18.11521227, 8.484e-05, 54.34563681, 0.00025451, 181.1521227, 0.00084835, -18.11521227, -8.484e-05, -54.34563681, -0.00025451, -181.1521227, -0.00084835, 0.4, 0.3, 0.003, 0.0, 0.0, 13026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3026, 99999, 'P', 43026, 'Vy', 33026, 'Vz', 23026, 'My', 13026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173026, 73026, 173026, 3026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 3026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173027, 8.3, 25.5, 10.15)
    ops.node(124027, 8.3, 25.5, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3027, 173027, 124027, 0.0625, 30093328.57870268, 12538886.90779278, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23027, 47.02020024, 0.0013311, 56.7982482, 0.01802911, 5.67982482, 0.06455144, -47.02020024, -0.0013311, -56.7982482, -0.01802911, -5.67982482, -0.06455144, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13027, 47.02020024, 0.0013311, 56.7982482, 0.01802911, 5.67982482, 0.06455144, -47.02020024, -0.0013311, -56.7982482, -0.01802911, -5.67982482, -0.06455144, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23027, 3027, 0.0, 73.01252967, 0.02662195, 73.01252967, 0.07986585, 51.10877077, -1105.92364254, 0.05, 2, 0, 73027, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 43027, 18.25313242, 8.664e-05, 54.75939726, 0.00025993, 182.53132418, 0.00086645, -18.25313242, -8.664e-05, -54.75939726, -0.00025993, -182.53132418, -0.00086645, 0.4, 0.3, 0.003, 0.0, 0.0, 23027, 2)
    ops.limitCurve('ThreePoint', 13027, 3027, 0.0, 73.01252967, 0.02662195, 73.01252967, 0.07986585, 51.10877077, -1105.92364254, 0.05, 2, 0, 73027, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 33027, 18.25313242, 8.664e-05, 54.75939726, 0.00025993, 182.53132418, 0.00086645, -18.25313242, -8.664e-05, -54.75939726, -0.00025993, -182.53132418, -0.00086645, 0.4, 0.3, 0.003, 0.0, 0.0, 13027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3027, 99999, 'P', 43027, 'Vy', 33027, 'Vz', 23027, 'My', 13027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173027, 73027, 173027, 3027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 3027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173028, 13.65, 25.5, 10.15)
    ops.node(124028, 13.65, 25.5, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3028, 173028, 124028, 0.0625, 30243504.65360117, 12601460.27233382, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23028, 27.35677363, 0.0011641, 33.14583582, 0.0182929, 3.31458358, 0.07780589, -27.35677363, -0.0011641, -33.14583582, -0.0182929, -3.31458358, -0.07780589, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13028, 27.35677363, 0.0011641, 33.14583582, 0.0182929, 3.31458358, 0.07780589, -27.35677363, -0.0011641, -33.14583582, -0.0182929, -3.31458358, -0.07780589, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23028, 3028, 0.0, 81.63392221, 0.02328194, 81.63392221, 0.06984582, 57.14374554, -1868.64565107, 0.05, 2, 0, 73028, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 43028, 20.40848055, 9.639e-05, 61.22544165, 0.00028918, 204.08480551, 0.00096395, -20.40848055, -9.639e-05, -61.22544165, -0.00028918, -204.08480551, -0.00096395, 0.4, 0.3, 0.003, 0.0, 0.0, 23028, 2)
    ops.limitCurve('ThreePoint', 13028, 3028, 0.0, 81.63392221, 0.02328194, 81.63392221, 0.06984582, 57.14374554, -1868.64565107, 0.05, 2, 0, 73028, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 33028, 20.40848055, 9.639e-05, 61.22544165, 0.00028918, 204.08480551, 0.00096395, -20.40848055, -9.639e-05, -61.22544165, -0.00028918, -204.08480551, -0.00096395, 0.4, 0.3, 0.003, 0.0, 0.0, 13028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3028, 99999, 'P', 43028, 'Vy', 33028, 'Vz', 23028, 'My', 13028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173028, 73028, 173028, 3028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 3028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124029, 0.0, 0.0, 1.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 170001, 124029, 0.09, 29590400.1754636, 12329333.40644317, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 121.61871445, 0.00093039, 146.10119985, 0.01640597, 14.61011998, 0.04936852, -121.61871445, -0.00093039, -146.10119985, -0.01640597, -14.61011998, -0.04936852, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 111.53385783, 0.00093039, 133.98620866, 0.01640597, 13.39862087, 0.04936852, -111.53385783, -0.00093039, -133.98620866, -0.01640597, -13.39862087, -0.04936852, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 115.04348719, 0.01860781, 115.04348719, 0.05582344, 80.53044103, -2165.71459372, 0.05, 2, 0, 70001, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 28.7608718, 5.754e-05, 86.28261539, 0.00017262, 287.60871797, 0.0005754, -28.7608718, -5.754e-05, -86.28261539, -0.00017262, -287.60871797, -0.0005754, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 115.04348719, 0.01860781, 115.04348719, 0.05582344, 80.53044103, -2165.71459372, 0.05, 2, 0, 70001, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 28.7608718, 5.754e-05, 86.28261539, 0.00017262, 287.60871797, 0.0005754, -28.7608718, -5.754e-05, -86.28261539, -0.00017262, -287.60871797, -0.0005754, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 0.0, 0.0, 2.1)
    ops.node(121001, 0.0, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 174029, 121001, 0.09, 28820964.2387471, 12008735.09947796, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 74.4509227, 0.00085824, 89.71309377, 0.03004801, 8.97130938, 0.08882529, -74.4509227, -0.00085824, -89.71309377, -0.03004801, -8.97130938, -0.08882529, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 74.4509227, 0.00085824, 89.71309377, 0.03004801, 8.97130938, 0.08882529, -74.4509227, -0.00085824, -89.71309377, -0.03004801, -8.97130938, -0.08882529, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 154.91735415, 0.01716477, 154.91735415, 0.05149431, 108.4421479, -4742.98861329, 0.05, 2, 0, 74029, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 38.72933854, 7.955e-05, 116.18801561, 0.00023866, 387.29338537, 0.00079552, -38.72933854, -7.955e-05, -116.18801561, -0.00023866, -387.29338537, -0.00079552, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 154.91735415, 0.01716477, 154.91735415, 0.05149431, 108.4421479, -4742.98861329, 0.05, 2, 0, 74029, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 38.72933854, 7.955e-05, 116.18801561, 0.00023866, 387.29338537, 0.00079552, -38.72933854, -7.955e-05, -116.18801561, -0.00023866, -387.29338537, -0.00079552, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 2.95, 0.0, 0.0)
    ops.node(124030, 2.95, 0.0, 1.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 170002, 124030, 0.1225, 30754225.14864149, 12814260.47860062, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 215.51548752, 0.00082496, 256.83199786, 0.01788481, 25.68319979, 0.04727264, -215.51548752, -0.00082496, -256.83199786, -0.01788481, -25.68319979, -0.04727264, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 208.6486725, 0.00082496, 248.64874458, 0.01788481, 24.86487446, 0.04727264, -208.6486725, -0.00082496, -248.64874458, -0.01788481, -24.86487446, -0.04727264, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 197.25710144, 0.01649925, 197.25710144, 0.04949774, 138.07997101, -3381.75272169, 0.05, 2, 0, 70002, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 49.31427536, 6.974e-05, 147.94282608, 0.00020923, 493.1427536, 0.00069742, -49.31427536, -6.974e-05, -147.94282608, -0.00020923, -493.1427536, -0.00069742, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 197.25710144, 0.01649925, 197.25710144, 0.04949774, 138.07997101, -3381.75272169, 0.05, 2, 0, 70002, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 49.31427536, 6.974e-05, 147.94282608, 0.00020923, 493.1427536, 0.00069742, -49.31427536, -6.974e-05, -147.94282608, -0.00020923, -493.1427536, -0.00069742, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 2.95, 0.0, 2.1)
    ops.node(121002, 2.95, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4077, 174030, 121002, 0.1225, 29700722.03834575, 12375300.84931073, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24077, 158.85913491, 0.00083108, 189.76482342, 0.01664644, 18.97648234, 0.04535746, -158.85913491, -0.00083108, -189.76482342, -0.01664644, -18.97648234, -0.04535746, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14077, 146.25392096, 0.00083108, 174.70729337, 0.01664644, 17.47072934, 0.04535746, -146.25392096, -0.00083108, -174.70729337, -0.01664644, -17.47072934, -0.04535746, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24077, 4077, 0.0, 189.91193507, 0.01662162, 189.91193507, 0.04986487, 132.93835455, -3348.28108138, 0.05, 2, 0, 74030, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44077, 47.47798377, 6.953e-05, 142.43395131, 0.00020858, 474.77983768, 0.00069527, -47.47798377, -6.953e-05, -142.43395131, -0.00020858, -474.77983768, -0.00069527, 0.4, 0.3, 0.003, 0.0, 0.0, 24077, 2)
    ops.limitCurve('ThreePoint', 14077, 4077, 0.0, 189.91193507, 0.01662162, 189.91193507, 0.04986487, 132.93835455, -3348.28108138, 0.05, 2, 0, 74030, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34077, 47.47798377, 6.953e-05, 142.43395131, 0.00020858, 474.77983768, 0.00069527, -47.47798377, -6.953e-05, -142.43395131, -0.00020858, -474.77983768, -0.00069527, 0.4, 0.3, 0.003, 0.0, 0.0, 14077, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4077, 99999, 'P', 44077, 'Vy', 34077, 'Vz', 24077, 'My', 14077, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4077, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4077, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.95)
    ops.node(124031, 0.0, 0.0, 5.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 171001, 124031, 0.09, 29146041.80335597, 12144184.08473166, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 70.64447505, 0.00080637, 85.25595612, 0.01592916, 8.52559561, 0.05234624, -70.64447505, -0.00080637, -85.25595612, -0.01592916, -8.52559561, -0.05234624, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 70.64447505, 0.00080637, 85.25595612, 0.01592916, 8.52559561, 0.05234624, -70.64447505, -0.00080637, -85.25595612, -0.01592916, -8.52559561, -0.05234624, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 121.53472222, 0.01612744, 121.53472222, 0.04838232, 85.07430555, -2564.74734986, 0.05, 2, 0, 71001, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 30.38368055, 5.171e-05, 91.15104166, 0.00015512, 303.83680554, 0.00051706, -30.38368055, -5.171e-05, -91.15104166, -0.00015512, -303.83680554, -0.00051706, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 121.53472222, 0.01612744, 121.53472222, 0.04838232, 85.07430555, -2564.74734986, 0.05, 2, 0, 71001, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 30.38368055, 5.171e-05, 91.15104166, 0.00015512, 303.83680554, 0.00051706, -30.38368055, -5.171e-05, -91.15104166, -0.00015512, -303.83680554, -0.00051706, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 0.0, 0.0, 5.45)
    ops.node(122001, 0.0, 0.0, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 174031, 122001, 0.09, 28940206.35920764, 12058419.31633652, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 65.53049395, 0.00080374, 79.27318122, 0.01672377, 7.92731812, 0.0551756, -65.53049395, -0.00080374, -79.27318122, -0.01672377, -7.92731812, -0.0551756, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 65.53049395, 0.00080374, 79.27318122, 0.01672377, 7.92731812, 0.0551756, -65.53049395, -0.00080374, -79.27318122, -0.01672377, -7.92731812, -0.0551756, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 116.93584997, 0.01607488, 116.93584997, 0.04822465, 81.85509498, -2576.88973532, 0.05, 2, 0, 74031, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 29.23396249, 5.01e-05, 87.70188748, 0.00015031, 292.33962493, 0.00050103, -29.23396249, -5.01e-05, -87.70188748, -0.00015031, -292.33962493, -0.00050103, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 116.93584997, 0.01607488, 116.93584997, 0.04822465, 81.85509498, -2576.88973532, 0.05, 2, 0, 74031, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 29.23396249, 5.01e-05, 87.70188748, 0.00015031, 292.33962493, 0.00050103, -29.23396249, -5.01e-05, -87.70188748, -0.00015031, -292.33962493, -0.00050103, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 2.95, 0.0, 3.95)
    ops.node(124032, 2.95, 0.0, 5.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 171002, 124032, 0.1225, 30727009.58702559, 12802920.66126066, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 129.65605024, 0.00074817, 155.31508343, 0.0143454, 15.53150834, 0.04436659, -129.65605024, -0.00074817, -155.31508343, -0.0143454, -15.53150834, -0.04436659, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 123.63302524, 0.00074817, 148.1000971, 0.0143454, 14.81000971, 0.04436659, -123.63302524, -0.00074817, -148.1000971, -0.0143454, -14.81000971, -0.04436659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 198.60452962, 0.01496346, 198.60452962, 0.04489039, 139.02317074, -3230.93263336, 0.05, 2, 0, 71002, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 49.65113241, 5.888e-05, 148.95339722, 0.00017665, 496.51132406, 0.00058884, -49.65113241, -5.888e-05, -148.95339722, -0.00017665, -496.51132406, -0.00058884, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 198.60452962, 0.01496346, 198.60452962, 0.04489039, 139.02317074, -3230.93263336, 0.05, 2, 0, 71002, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 49.65113241, 5.888e-05, 148.95339722, 0.00017665, 496.51132406, 0.00058884, -49.65113241, -5.888e-05, -148.95339722, -0.00017665, -496.51132406, -0.00058884, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4081, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 2.95, 0.0, 5.45)
    ops.node(122002, 2.95, 0.0, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4082, 174032, 122002, 0.1225, 29315222.80866833, 12214676.17027847, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24082, 123.35668677, 0.00075344, 148.2620915, 0.01473418, 14.82620915, 0.04401555, -123.35668677, -0.00075344, -148.2620915, -0.01473418, -14.82620915, -0.04401555, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14082, 117.43739823, 0.00075344, 141.14771349, 0.01473418, 14.11477135, 0.04401555, -117.43739823, -0.00075344, -141.14771349, -0.01473418, -14.11477135, -0.04401555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24082, 4082, 0.0, 186.03246361, 0.01506875, 186.03246361, 0.04520625, 130.22272453, -3125.89377129, 0.05, 2, 0, 74032, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44082, 46.5081159, 5.781e-05, 139.52434771, 0.00017344, 465.08115903, 0.00057813, -46.5081159, -5.781e-05, -139.52434771, -0.00017344, -465.08115903, -0.00057813, 0.4, 0.3, 0.003, 0.0, 0.0, 24082, 2)
    ops.limitCurve('ThreePoint', 14082, 4082, 0.0, 186.03246361, 0.01506875, 186.03246361, 0.04520625, 130.22272453, -3125.89377129, 0.05, 2, 0, 74032, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34082, 46.5081159, 5.781e-05, 139.52434771, 0.00017344, 465.08115903, 0.00057813, -46.5081159, -5.781e-05, -139.52434771, -0.00017344, -465.08115903, -0.00057813, 0.4, 0.3, 0.003, 0.0, 0.0, 14082, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4082, 99999, 'P', 44082, 'Vy', 34082, 'Vz', 24082, 'My', 14082, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4082, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4082, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 7.05)
    ops.node(124033, 0.0, 0.0, 8.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4084, 172001, 124033, 0.0625, 29583344.75544473, 12326393.64810197, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24084, 49.88900007, 0.00094159, 60.20699656, 0.01764952, 6.02069966, 0.06092876, -49.88900007, -0.00094159, -60.20699656, -0.01764952, -6.02069966, -0.06092876, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14084, 49.88900007, 0.00094159, 60.20699656, 0.01764952, 6.02069966, 0.06092876, -49.88900007, -0.00094159, -60.20699656, -0.01764952, -6.02069966, -0.06092876, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24084, 4084, 0.0, 80.35344949, 0.01883175, 80.35344949, 0.05649526, 56.24741464, -2194.3583412, 0.05, 2, 0, 72001, 24033, 2, 3)
    ops.uniaxialMaterial('LimitState', 44084, 20.08836237, 4.85e-05, 60.26508711, 0.0001455, 200.88362371, 0.000485, -20.08836237, -4.85e-05, -60.26508711, -0.0001455, -200.88362371, -0.000485, 0.4, 0.3, 0.003, 0.0, 0.0, 24084, 2)
    ops.limitCurve('ThreePoint', 14084, 4084, 0.0, 80.35344949, 0.01883175, 80.35344949, 0.05649526, 56.24741464, -2194.3583412, 0.05, 2, 0, 72001, 24033, 1, 3)
    ops.uniaxialMaterial('LimitState', 34084, 20.08836237, 4.85e-05, 60.26508711, 0.0001455, 200.88362371, 0.000485, -20.08836237, -4.85e-05, -60.26508711, -0.0001455, -200.88362371, -0.000485, 0.4, 0.3, 0.003, 0.0, 0.0, 14084, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4084, 99999, 'P', 44084, 'Vy', 34084, 'Vz', 24084, 'My', 14084, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4084, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124033, 124033, 24033, 4084, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174033, 0.0, 0.0, 8.55)
    ops.node(123001, 0.0, 0.0, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4085, 174033, 123001, 0.0625, 29738481.21097415, 12391033.83790589, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24085, 44.78830145, 0.00091661, 54.20233007, 0.01846841, 5.42023301, 0.06612768, -44.78830145, -0.00091661, -54.20233007, -0.01846841, -5.42023301, -0.06612768, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14085, 44.78830145, 0.00091661, 54.20233007, 0.01846841, 5.42023301, 0.06612768, -44.78830145, -0.00091661, -54.20233007, -0.01846841, -5.42023301, -0.06612768, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24085, 4085, 0.0, 76.09254746, 0.01833211, 76.09254746, 0.05499632, 53.26478322, -2361.22108752, 0.05, 2, 0, 74033, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44085, 19.02313687, 4.569e-05, 57.0694106, 0.00013707, 190.23136865, 0.00045689, -19.02313687, -4.569e-05, -57.0694106, -0.00013707, -190.23136865, -0.00045689, 0.4, 0.3, 0.003, 0.0, 0.0, 24085, 2)
    ops.limitCurve('ThreePoint', 14085, 4085, 0.0, 76.09254746, 0.01833211, 76.09254746, 0.05499632, 53.26478322, -2361.22108752, 0.05, 2, 0, 74033, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34085, 19.02313687, 4.569e-05, 57.0694106, 0.00013707, 190.23136865, 0.00045689, -19.02313687, -4.569e-05, -57.0694106, -0.00013707, -190.23136865, -0.00045689, 0.4, 0.3, 0.003, 0.0, 0.0, 14085, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4085, 99999, 'P', 44085, 'Vy', 34085, 'Vz', 24085, 'My', 14085, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174033, 74033, 174033, 4085, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4085, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 2.95, 0.0, 7.05)
    ops.node(124034, 2.95, 0.0, 8.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4086, 172002, 124034, 0.0625, 30336982.25366677, 12640409.27236115, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24086, 62.39318485, 0.0009908, 74.50924028, 0.01523276, 7.45092403, 0.04901885, -62.39318485, -0.0009908, -74.50924028, -0.01523276, -7.45092403, -0.04901885, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14086, 62.39318485, 0.0009908, 74.50924028, 0.01523276, 7.45092403, 0.04901885, -62.39318485, -0.0009908, -74.50924028, -0.01523276, -7.45092403, -0.04901885, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24086, 4086, 0.0, 89.05340219, 0.01981594, 89.05340219, 0.05944782, 62.33738153, -2221.77909136, 0.05, 2, 0, 72002, 24034, 2, 3)
    ops.uniaxialMaterial('LimitState', 44086, 22.26335055, 5.242e-05, 66.79005164, 0.00015725, 222.63350547, 0.00052416, -22.26335055, -5.242e-05, -66.79005164, -0.00015725, -222.63350547, -0.00052416, 0.4, 0.3, 0.003, 0.0, 0.0, 24086, 2)
    ops.limitCurve('ThreePoint', 14086, 4086, 0.0, 89.05340219, 0.01981594, 89.05340219, 0.05944782, 62.33738153, -2221.77909136, 0.05, 2, 0, 72002, 24034, 1, 3)
    ops.uniaxialMaterial('LimitState', 34086, 22.26335055, 5.242e-05, 66.79005164, 0.00015725, 222.63350547, 0.00052416, -22.26335055, -5.242e-05, -66.79005164, -0.00015725, -222.63350547, -0.00052416, 0.4, 0.3, 0.003, 0.0, 0.0, 14086, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4086, 99999, 'P', 44086, 'Vy', 34086, 'Vz', 24086, 'My', 14086, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4086, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124034, 124034, 24034, 4086, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174034, 2.95, 0.0, 8.55)
    ops.node(123002, 2.95, 0.0, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4087, 174034, 123002, 0.0625, 29773823.9013276, 12405759.9588865, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24087, 57.91175695, 0.00097975, 69.4034117, 0.0156276, 6.94034117, 0.05136318, -57.91175695, -0.00097975, -69.4034117, -0.0156276, -6.94034117, -0.05136318, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14087, 57.91175695, 0.00097975, 69.4034117, 0.0156276, 6.94034117, 0.05136318, -57.91175695, -0.00097975, -69.4034117, -0.0156276, -6.94034117, -0.05136318, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24087, 4087, 0.0, 82.66060675, 0.019595, 82.66060675, 0.05878501, 57.86242472, -2131.14080408, 0.05, 2, 0, 74034, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44087, 20.66515169, 4.957e-05, 61.99545506, 0.00014872, 206.65151687, 0.00049573, -20.66515169, -4.957e-05, -61.99545506, -0.00014872, -206.65151687, -0.00049573, 0.4, 0.3, 0.003, 0.0, 0.0, 24087, 2)
    ops.limitCurve('ThreePoint', 14087, 4087, 0.0, 82.66060675, 0.019595, 82.66060675, 0.05878501, 57.86242472, -2131.14080408, 0.05, 2, 0, 74034, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34087, 20.66515169, 4.957e-05, 61.99545506, 0.00014872, 206.65151687, 0.00049573, -20.66515169, -4.957e-05, -61.99545506, -0.00014872, -206.65151687, -0.00049573, 0.4, 0.3, 0.003, 0.0, 0.0, 14087, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4087, 99999, 'P', 44087, 'Vy', 34087, 'Vz', 24087, 'My', 14087, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174034, 74034, 174034, 4087, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4087, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 10.15)
    ops.node(124035, 0.0, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4089, 173001, 124035, 0.0625, 28684158.68428947, 11951732.78512061, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24089, 42.91285621, 0.00089335, 52.20209303, 0.01949043, 5.2202093, 0.07046245, -42.91285621, -0.00089335, -52.20209303, -0.01949043, -5.2202093, -0.07046245, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14089, 42.91285621, 0.00089335, 52.20209303, 0.01949043, 5.2202093, 0.07046245, -42.91285621, -0.00089335, -52.20209303, -0.01949043, -5.2202093, -0.07046245, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24089, 4089, 0.0, 72.80602794, 0.01786701, 72.80602794, 0.05360104, 50.96421956, -3075.08468206, 0.05, 2, 0, 73001, 24035, 2, 3)
    ops.uniaxialMaterial('LimitState', 44089, 18.20150699, 4.532e-05, 54.60452096, 0.00013597, 182.01506986, 0.00045322, -18.20150699, -4.532e-05, -54.60452096, -0.00013597, -182.01506986, -0.00045322, 0.4, 0.3, 0.003, 0.0, 0.0, 24089, 2)
    ops.limitCurve('ThreePoint', 14089, 4089, 0.0, 72.80602794, 0.01786701, 72.80602794, 0.05360104, 50.96421956, -3075.08468206, 0.05, 2, 0, 73001, 24035, 1, 3)
    ops.uniaxialMaterial('LimitState', 34089, 18.20150699, 4.532e-05, 54.60452096, 0.00013597, 182.01506986, 0.00045322, -18.20150699, -4.532e-05, -54.60452096, -0.00013597, -182.01506986, -0.00045322, 0.4, 0.3, 0.003, 0.0, 0.0, 14089, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4089, 99999, 'P', 44089, 'Vy', 34089, 'Vz', 24089, 'My', 14089, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4089, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124035, 124035, 24035, 4089, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174035, 0.0, 0.0, 11.625)
    ops.node(124001, 0.0, 0.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4090, 174035, 124001, 0.0625, 29698824.19555918, 12374510.08148299, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24090, 36.00644394, 0.00090525, 43.83187326, 0.02018221, 4.38318733, 0.07678952, -36.00644394, -0.00090525, -43.83187326, -0.02018221, -4.38318733, -0.07678952, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14090, 36.00644394, 0.00090525, 43.83187326, 0.02018221, 4.38318733, 0.07678952, -36.00644394, -0.00090525, -43.83187326, -0.02018221, -4.38318733, -0.07678952, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24090, 4090, 0.0, 68.98123702, 0.01810494, 68.98123702, 0.05431483, 48.28686592, -9199.77002097, 0.05, 2, 0, 74035, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44090, 17.24530926, 4.147e-05, 51.73592777, 0.00012442, 172.45309256, 0.00041474, -17.24530926, -4.147e-05, -51.73592777, -0.00012442, -172.45309256, -0.00041474, 0.4, 0.3, 0.003, 0.0, 0.0, 24090, 2)
    ops.limitCurve('ThreePoint', 14090, 4090, 0.0, 68.98123702, 0.01810494, 68.98123702, 0.05431483, 48.28686592, -9199.77002097, 0.05, 2, 0, 74035, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34090, 17.24530926, 4.147e-05, 51.73592777, 0.00012442, 172.45309256, 0.00041474, -17.24530926, -4.147e-05, -51.73592777, -0.00012442, -172.45309256, -0.00041474, 0.4, 0.3, 0.003, 0.0, 0.0, 14090, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4090, 99999, 'P', 44090, 'Vy', 34090, 'Vz', 24090, 'My', 14090, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174035, 74035, 174035, 4090, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4090, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 2.95, 0.0, 10.15)
    ops.node(124036, 2.95, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4091, 173002, 124036, 0.0625, 29470117.09053138, 12279215.45438807, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24091, 47.24349439, 0.00092964, 57.15274216, 0.01765001, 5.71527422, 0.06372907, -47.24349439, -0.00092964, -57.15274216, -0.01765001, -5.71527422, -0.06372907, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14091, 47.24349439, 0.00092964, 57.15274216, 0.01765001, 5.71527422, 0.06372907, -47.24349439, -0.00092964, -57.15274216, -0.01765001, -5.71527422, -0.06372907, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24091, 4091, 0.0, 71.99321866, 0.01859289, 71.99321866, 0.05577866, 50.39525306, -2156.24584388, 0.05, 2, 0, 73002, 24036, 2, 3)
    ops.uniaxialMaterial('LimitState', 44091, 17.99830466, 4.362e-05, 53.99491399, 0.00013086, 179.98304665, 0.00043621, -17.99830466, -4.362e-05, -53.99491399, -0.00013086, -179.98304665, -0.00043621, 0.4, 0.3, 0.003, 0.0, 0.0, 24091, 2)
    ops.limitCurve('ThreePoint', 14091, 4091, 0.0, 71.99321866, 0.01859289, 71.99321866, 0.05577866, 50.39525306, -2156.24584388, 0.05, 2, 0, 73002, 24036, 1, 3)
    ops.uniaxialMaterial('LimitState', 34091, 17.99830466, 4.362e-05, 53.99491399, 0.00013086, 179.98304665, 0.00043621, -17.99830466, -4.362e-05, -53.99491399, -0.00013086, -179.98304665, -0.00043621, 0.4, 0.3, 0.003, 0.0, 0.0, 14091, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4091, 99999, 'P', 44091, 'Vy', 34091, 'Vz', 24091, 'My', 14091, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4091, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124036, 124036, 24036, 4091, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174036, 2.95, 0.0, 11.625)
    ops.node(124002, 2.95, 0.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4092, 174036, 124002, 0.0625, 29600621.32773328, 12333592.21988887, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24092, 42.9177378, 0.00088753, 52.0661449, 0.01863282, 5.20661449, 0.0693058, -42.9177378, -0.00088753, -52.0661449, -0.01863282, -5.20661449, -0.0693058, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14092, 42.9177378, 0.00088753, 52.0661449, 0.01863282, 5.20661449, 0.0693058, -42.9177378, -0.00088753, -52.0661449, -0.01863282, -5.20661449, -0.0693058, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24092, 4092, 0.0, 70.14123014, 0.01775057, 70.14123014, 0.05325172, 49.0988611, -2708.15347712, 0.05, 2, 0, 74036, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44092, 17.53530754, 4.231e-05, 52.60592261, 0.00012693, 175.35307536, 0.00042311, -17.53530754, -4.231e-05, -52.60592261, -0.00012693, -175.35307536, -0.00042311, 0.4, 0.3, 0.003, 0.0, 0.0, 24092, 2)
    ops.limitCurve('ThreePoint', 14092, 4092, 0.0, 70.14123014, 0.01775057, 70.14123014, 0.05325172, 49.0988611, -2708.15347712, 0.05, 2, 0, 74036, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34092, 17.53530754, 4.231e-05, 52.60592261, 0.00012693, 175.35307536, 0.00042311, -17.53530754, -4.231e-05, -52.60592261, -0.00012693, -175.35307536, -0.00042311, 0.4, 0.3, 0.003, 0.0, 0.0, 14092, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4092, 99999, 'P', 44092, 'Vy', 34092, 'Vz', 24092, 'My', 14092, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174036, 74036, 174036, 4092, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4092, '-orient', 0, 0, 1, 0, 1, 0)
