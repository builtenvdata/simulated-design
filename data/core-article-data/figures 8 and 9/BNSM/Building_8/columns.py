import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.09, 23059682.11080355, 9608200.87950148, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 63.24236612, 0.00049428, 73.97884262, 0.00520079, 7.39788426, 0.01493935, -63.24236612, -0.00049428, -73.97884262, -0.00520079, -7.39788426, -0.01493935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 59.63833938, 0.00049428, 69.76297052, 0.00520079, 6.97629705, 0.01493935, -59.63833938, -0.00049428, -69.76297052, -0.00520079, -6.97629705, -0.01493935, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 72.52043004, 0.0098857, 72.52043004, 0.0296571, 50.76430103, -1414.44518799, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 18.13010751, 6.667e-05, 54.39032253, 0.00020002, 181.30107511, 0.00066672, -18.13010751, -6.667e-05, -54.39032253, -0.00020002, -181.30107511, -0.00066672, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 72.52043004, 0.0098857, 72.52043004, 0.0296571, 50.76430103, -1414.44518799, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 18.13010751, 6.667e-05, 54.39032253, 0.00020002, 181.30107511, 0.00066672, -18.13010751, -6.667e-05, -54.39032253, -0.00020002, -181.30107511, -0.00066672, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 7.3, 0.0, 0.0)
    ops.node(121002, 7.3, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.2025, 27779840.65496076, 11574933.60623365, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 271.39038509, 0.00071145, 324.68133332, 0.00823975, 32.46813333, 0.02981771, -271.39038509, -0.00071145, -324.68133332, -0.00823975, -32.46813333, -0.02981771, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 314.48271423, 0.00071145, 376.23538848, 0.00823975, 37.62353885, 0.02981771, -314.48271423, -0.00071145, -376.23538848, -0.00823975, -37.62353885, -0.02981771, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 239.07109946, 0.01422908, 239.07109946, 0.04268723, 167.34976962, -2863.4765118, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 59.76777487, 8.109e-05, 179.3033246, 0.00024326, 597.67774865, 0.00081087, -59.76777487, -8.109e-05, -179.3033246, -0.00024326, -597.67774865, -0.00081087, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 239.07109946, 0.01422908, 239.07109946, 0.04268723, 167.34976962, -2863.4765118, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 59.76777487, 8.109e-05, 179.3033246, 0.00024326, 597.67774865, 0.00081087, -59.76777487, -8.109e-05, -179.3033246, -0.00024326, -597.67774865, -0.00081087, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 24.95, 0.0, 0.0)
    ops.node(121005, 24.95, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.2025, 27069896.11427422, 11279123.38094759, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 277.14557394, 0.00070567, 331.43195513, 0.00827295, 33.14319551, 0.02853972, -277.14557394, -0.00070567, -331.43195513, -0.00827295, -33.14319551, -0.02853972, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 325.87241235, 0.00070567, 389.70324948, 0.00827295, 38.97032495, 0.02853972, -325.87241235, -0.00070567, -389.70324948, -0.00827295, -38.97032495, -0.02853972, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 231.45074542, 0.01411336, 231.45074542, 0.04234009, 162.01552179, -2799.39845595, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 57.86268635, 8.056e-05, 173.58805906, 0.00024168, 578.62686354, 0.00080561, -57.86268635, -8.056e-05, -173.58805906, -0.00024168, -578.62686354, -0.00080561, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 231.45074542, 0.01411336, 231.45074542, 0.04234009, 162.01552179, -2799.39845595, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 57.86268635, 8.056e-05, 173.58805906, 0.00024168, 578.62686354, 0.00080561, -57.86268635, -8.056e-05, -173.58805906, -0.00024168, -578.62686354, -0.00080561, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 32.25, 0.0, 0.0)
    ops.node(121006, 32.25, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.09, 26977200.55969074, 11240500.23320447, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 135.49177903, 0.00099146, 160.88022429, 0.00803701, 16.08802243, 0.02709603, -135.49177903, -0.00099146, -160.88022429, -0.00803701, -16.08802243, -0.02709603, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 121.68524312, 0.00099146, 144.48662011, 0.00803701, 14.44866201, 0.02709603, -121.68524312, -0.00099146, -144.48662011, -0.00803701, -14.44866201, -0.02709603, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 100.42227281, 0.01982919, 100.42227281, 0.05948757, 70.29559097, -1520.93552395, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 25.1055682, 7.892e-05, 75.31670461, 0.00023675, 251.05568202, 0.00078917, -25.1055682, -7.892e-05, -75.31670461, -0.00023675, -251.05568202, -0.00078917, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 100.42227281, 0.01982919, 100.42227281, 0.05948757, 70.29559097, -1520.93552395, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 25.1055682, 7.892e-05, 75.31670461, 0.00023675, 251.05568202, 0.00078917, -25.1055682, -7.892e-05, -75.31670461, -0.00023675, -251.05568202, -0.00078917, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 3.65, 0.0)
    ops.node(121007, 0.0, 3.65, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 26405407.80327706, 11002253.25136544, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 216.05558804, 0.00093419, 256.12082813, 0.00705498, 25.61208281, 0.02270681, -216.05558804, -0.00093419, -256.12082813, -0.00705498, -25.61208281, -0.02270681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 181.74627538, 0.00093419, 215.44921371, 0.00705498, 21.54492137, 0.02270681, -181.74627538, -0.00093419, -215.44921371, -0.00705498, -21.54492137, -0.02270681, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 132.02963711, 0.01868373, 132.02963711, 0.0560512, 92.42074598, -1896.64048941, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 33.00740928, 7.788e-05, 99.02222783, 0.00023364, 330.07409278, 0.00077879, -33.00740928, -7.788e-05, -99.02222783, -0.00023364, -330.07409278, -0.00077879, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 132.02963711, 0.01868373, 132.02963711, 0.0560512, 92.42074598, -1896.64048941, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 33.00740928, 7.788e-05, 99.02222783, 0.00023364, 330.07409278, 0.00077879, -33.00740928, -7.788e-05, -99.02222783, -0.00023364, -330.07409278, -0.00077879, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 7.3, 3.65, 0.0)
    ops.node(121008, 7.3, 3.65, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.25, 25503508.75089377, 10626461.97953907, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 418.07157439, 0.00070963, 500.2965557, 0.00547743, 50.02965557, 0.01861286, -418.07157439, -0.00070963, -500.2965557, -0.00547743, -50.02965557, -0.01861286, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 501.7482733, 0.00070963, 600.43052036, 0.00547743, 60.04305204, 0.01861286, -501.7482733, -0.00070963, -600.43052036, -0.00547743, -60.04305204, -0.01861286, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 245.43475434, 0.01419252, 245.43475434, 0.04257757, 171.80432804, -2360.66020406, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 61.35868859, 7.345e-05, 184.07606576, 0.00022034, 613.58688586, 0.00073447, -61.35868859, -7.345e-05, -184.07606576, -0.00022034, -613.58688586, -0.00073447, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 245.43475434, 0.01419252, 245.43475434, 0.04257757, 171.80432804, -2360.66020406, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 61.35868859, 7.345e-05, 184.07606576, 0.00022034, 613.58688586, 0.00073447, -61.35868859, -7.345e-05, -184.07606576, -0.00022034, -613.58688586, -0.00073447, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 14.6, 3.65, 0.0)
    ops.node(121009, 14.6, 3.65, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.2025, 28230383.34066348, 11762659.72527645, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 306.62815929, 0.00072323, 367.87205844, 0.00810349, 36.78720584, 0.02962131, -306.62815929, -0.00072323, -367.87205844, -0.00810349, -36.78720584, -0.02962131, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 335.28480148, 0.00072323, 402.25239054, 0.00810349, 40.22523905, 0.02962131, -335.28480148, -0.00072323, -402.25239054, -0.00810349, -40.22523905, -0.02962131, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 218.79019423, 0.01446464, 218.79019423, 0.04339393, 153.15313596, -2314.37619588, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 54.69754856, 7.302e-05, 164.09264567, 0.00021907, 546.97548558, 0.00073024, -54.69754856, -7.302e-05, -164.09264567, -0.00021907, -546.97548558, -0.00073024, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 218.79019423, 0.01446464, 218.79019423, 0.04339393, 153.15313596, -2314.37619588, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 54.69754856, 7.302e-05, 164.09264567, 0.00021907, 546.97548558, 0.00073024, -54.69754856, -7.302e-05, -164.09264567, -0.00021907, -546.97548558, -0.00073024, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 17.65, 3.65, 0.0)
    ops.node(121010, 17.65, 3.65, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.2025, 26200863.45402438, 10917026.43917683, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 287.13700834, 0.00078475, 344.24445137, 0.00894177, 34.42444514, 0.02721959, -287.13700834, -0.00078475, -344.24445137, -0.00894177, -34.42444514, -0.02721959, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 308.20387236, 0.00078475, 369.50121325, 0.00894177, 36.95012132, 0.02721959, -308.20387236, -0.00078475, -369.50121325, -0.00894177, -36.95012132, -0.02721959, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 211.50480205, 0.01569505, 211.50480205, 0.04708514, 148.05336144, -2470.7030677, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 52.87620051, 7.606e-05, 158.62860154, 0.00022818, 528.76200513, 0.0007606, -52.87620051, -7.606e-05, -158.62860154, -0.00022818, -528.76200513, -0.0007606, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 211.50480205, 0.01569505, 211.50480205, 0.04708514, 148.05336144, -2470.7030677, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 52.87620051, 7.606e-05, 158.62860154, 0.00022818, 528.76200513, 0.0007606, -52.87620051, -7.606e-05, -158.62860154, -0.00022818, -528.76200513, -0.0007606, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 24.95, 3.65, 0.0)
    ops.node(121011, 24.95, 3.65, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.25, 25973024.81783127, 10822093.67409636, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 389.58635484, 0.00072664, 466.53249422, 0.00610266, 46.65324942, 0.01990499, -389.58635484, -0.00072664, -466.53249422, -0.00610266, -46.65324942, -0.01990499, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 452.16715688, 0.00072664, 541.47345995, 0.00610266, 54.14734599, 0.01990499, -452.16715688, -0.00072664, -541.47345995, -0.00610266, -54.14734599, -0.01990499, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 251.0134309, 0.01453282, 251.0134309, 0.04359846, 175.70940163, -2386.83070264, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 62.75335772, 7.376e-05, 188.26007317, 0.00022128, 627.53357724, 0.00073759, -62.75335772, -7.376e-05, -188.26007317, -0.00022128, -627.53357724, -0.00073759, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 251.0134309, 0.01453282, 251.0134309, 0.04359846, 175.70940163, -2386.83070264, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 62.75335772, 7.376e-05, 188.26007317, 0.00022128, 627.53357724, 0.00073759, -62.75335772, -7.376e-05, -188.26007317, -0.00022128, -627.53357724, -0.00073759, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 32.25, 3.65, 0.0)
    ops.node(121012, 32.25, 3.65, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 28242818.79137745, 11767841.16307394, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 205.57433658, 0.00092698, 244.3829225, 0.00774526, 24.43829225, 0.02712744, -205.57433658, -0.00092698, -244.3829225, -0.00774526, -24.43829225, -0.02712744, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 176.47677842, 0.00092698, 209.79229013, 0.00774526, 20.97922901, 0.02712744, -176.47677842, -0.00092698, -209.79229013, -0.00774526, -20.97922901, -0.02712744, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 136.51528384, 0.01853964, 136.51528384, 0.05561891, 95.56069869, -1833.70946553, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 34.12882096, 7.529e-05, 102.38646288, 0.00022586, 341.28820961, 0.00075286, -34.12882096, -7.529e-05, -102.38646288, -0.00022586, -341.28820961, -0.00075286, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 136.51528384, 0.01853964, 136.51528384, 0.05561891, 95.56069869, -1833.70946553, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 34.12882096, 7.529e-05, 102.38646288, 0.00022586, 341.28820961, 0.00075286, -34.12882096, -7.529e-05, -102.38646288, -0.00022586, -341.28820961, -0.00075286, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 7.3, 0.0)
    ops.node(121013, 0.0, 7.3, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.09, 27650893.35929574, 11521205.56637323, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 114.15470999, 0.00092993, 135.67960828, 0.0091317, 13.56796083, 0.02971893, -114.15470999, -0.00092993, -135.67960828, -0.0091317, -13.56796083, -0.02971893, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 104.87971058, 0.00092993, 124.65572422, 0.0091317, 12.46557242, 0.02971893, -104.87971058, -0.00092993, -124.65572422, -0.0091317, -12.46557242, -0.02971893, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 104.09078679, 0.01859868, 104.09078679, 0.05579604, 72.86355075, -1532.84804068, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 26.0226967, 7.981e-05, 78.06809009, 0.00023942, 260.22696697, 0.00079807, -26.0226967, -7.981e-05, -78.06809009, -0.00023942, -260.22696697, -0.00079807, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 104.09078679, 0.01859868, 104.09078679, 0.05579604, 72.86355075, -1532.84804068, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 26.0226967, 7.981e-05, 78.06809009, 0.00023942, 260.22696697, 0.00079807, -26.0226967, -7.981e-05, -78.06809009, -0.00023942, -260.22696697, -0.00079807, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 7.3, 7.3, 0.0)
    ops.node(121014, 7.3, 7.3, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.2025, 24869145.18893842, 10362143.82872434, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 273.44741302, 0.00072853, 325.81039036, 0.00653662, 32.58103904, 0.0223571, -273.44741302, -0.00072853, -325.81039036, -0.00653662, -32.58103904, -0.0223571, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 320.3209221, 0.00072853, 381.65979892, 0.00653662, 38.16597989, 0.0223571, -320.3209221, -0.00072853, -381.65979892, -0.00653662, -38.16597989, -0.0223571, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 214.90865914, 0.01457055, 214.90865914, 0.04371164, 150.4360614, -2764.33260532, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 53.72716478, 8.142e-05, 161.18149435, 0.00024427, 537.27164785, 0.00081423, -53.72716478, -8.142e-05, -161.18149435, -0.00024427, -537.27164785, -0.00081423, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 214.90865914, 0.01457055, 214.90865914, 0.04371164, 150.4360614, -2764.33260532, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 53.72716478, 8.142e-05, 161.18149435, 0.00024427, 537.27164785, 0.00081423, -53.72716478, -8.142e-05, -161.18149435, -0.00024427, -537.27164785, -0.00081423, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 14.6, 7.3, 0.0)
    ops.node(121015, 14.6, 7.3, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.1225, 27553831.27838653, 11480763.03266105, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 159.31571744, 0.00086938, 189.83977715, 0.00697569, 18.98397772, 0.02949401, -159.31571744, -0.00086938, -189.83977715, -0.00697569, -18.98397772, -0.02949401, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 159.31571744, 0.00086938, 189.83977715, 0.00697569, 18.98397772, 0.02949401, -159.31571744, -0.00086938, -189.83977715, -0.00697569, -18.98397772, -0.02949401, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 139.03622173, 0.01738764, 139.03622173, 0.05216293, 97.32535521, -1831.37376865, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 34.75905543, 7.859e-05, 104.2771663, 0.00023578, 347.59055434, 0.00078594, -34.75905543, -7.859e-05, -104.2771663, -0.00023578, -347.59055434, -0.00078594, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 139.03622173, 0.01738764, 139.03622173, 0.05216293, 97.32535521, -1831.37376865, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 34.75905543, 7.859e-05, 104.2771663, 0.00023578, 347.59055434, 0.00078594, -34.75905543, -7.859e-05, -104.2771663, -0.00023578, -347.59055434, -0.00078594, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 17.65, 7.3, 0.0)
    ops.node(121016, 17.65, 7.3, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1225, 25335490.09793978, 10556454.20747491, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 163.2646244, 0.00090237, 193.74418384, 0.00669367, 19.37441838, 0.02391298, -163.2646244, -0.00090237, -193.74418384, -0.00669367, -19.37441838, -0.02391298, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 163.2646244, 0.00090237, 193.74418384, 0.00669367, 19.37441838, 0.02391298, -163.2646244, -0.00090237, -193.74418384, -0.00669367, -19.37441838, -0.02391298, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 134.50171103, 0.01804744, 134.50171103, 0.05414232, 94.15119772, -1930.3883816, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 33.62542776, 8.269e-05, 100.87628327, 0.00024806, 336.25427758, 0.00082688, -33.62542776, -8.269e-05, -100.87628327, -0.00024806, -336.25427758, -0.00082688, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 134.50171103, 0.01804744, 134.50171103, 0.05414232, 94.15119772, -1930.3883816, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 33.62542776, 8.269e-05, 100.87628327, 0.00024806, 336.25427758, 0.00082688, -33.62542776, -8.269e-05, -100.87628327, -0.00024806, -336.25427758, -0.00082688, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 24.95, 7.3, 0.0)
    ops.node(121017, 24.95, 7.3, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.2025, 29494634.06406985, 12289430.8600291, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 279.2411331, 0.00076772, 333.96940928, 0.00763081, 33.39694093, 0.03210365, -279.2411331, -0.00076772, -333.96940928, -0.00763081, -33.39694093, -0.03210365, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 317.78594935, 0.00076772, 380.06859735, 0.00763081, 38.00685974, 0.03210365, -317.78594935, -0.00076772, -380.06859735, -0.00763081, -38.00685974, -0.03210365, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 243.87563042, 0.0153543, 243.87563042, 0.04606291, 170.71294129, -2686.29110497, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 60.96890761, 7.791e-05, 182.90672282, 0.00023372, 609.68907605, 0.00077907, -60.96890761, -7.791e-05, -182.90672282, -0.00023372, -609.68907605, -0.00077907, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 243.87563042, 0.0153543, 243.87563042, 0.04606291, 170.71294129, -2686.29110497, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 60.96890761, 7.791e-05, 182.90672282, 0.00023372, 609.68907605, 0.00077907, -60.96890761, -7.791e-05, -182.90672282, -0.00023372, -609.68907605, -0.00077907, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 32.25, 7.3, 0.0)
    ops.node(121018, 32.25, 7.3, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.09, 30201907.96195455, 12584128.31748106, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 124.75640267, 0.00107012, 148.39661493, 0.00970068, 14.83966149, 0.03559551, -124.75640267, -0.00107012, -148.39661493, -0.00970068, -14.83966149, -0.03559551, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 115.23230526, 0.00107012, 137.06778702, 0.00970068, 13.7067787, 0.03559551, -115.23230526, -0.00107012, -137.06778702, -0.00970068, -13.7067787, -0.03559551, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 119.67298223, 0.02140241, 119.67298223, 0.06420723, 83.77108756, -1577.60372746, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 29.91824556, 8.4e-05, 89.75473667, 0.00025201, 299.18245558, 0.00084004, -29.91824556, -8.4e-05, -89.75473667, -0.00025201, -299.18245558, -0.00084004, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 119.67298223, 0.02140241, 119.67298223, 0.06420723, 83.77108756, -1577.60372746, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 29.91824556, 8.4e-05, 89.75473667, 0.00025201, 299.18245558, 0.00084004, -29.91824556, -8.4e-05, -89.75473667, -0.00025201, -299.18245558, -0.00084004, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.0)
    ops.node(122001, 0.0, 0.0, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.09, 27433849.34831724, 11430770.56179885, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 104.90613154, 0.00119659, 125.70418953, 0.00931043, 12.57041895, 0.03513219, -104.90613154, -0.00119659, -125.70418953, -0.00931043, -12.57041895, -0.03513219, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 98.48367326, 0.00119659, 118.00845334, 0.00931043, 11.80084533, 0.03513219, -98.48367326, -0.00119659, -118.00845334, -0.00931043, -11.80084533, -0.03513219, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 93.68367289, 0.02393173, 93.68367289, 0.07179518, 65.57857102, -1351.70151244, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 23.42091822, 7.24e-05, 70.26275467, 0.00021719, 234.20918222, 0.00072396, -23.42091822, -7.24e-05, -70.26275467, -0.00021719, -234.20918222, -0.00072396, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 93.68367289, 0.02393173, 93.68367289, 0.07179518, 65.57857102, -1351.70151244, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 23.42091822, 7.24e-05, 70.26275467, 0.00021719, 234.20918222, 0.00072396, -23.42091822, -7.24e-05, -70.26275467, -0.00021719, -234.20918222, -0.00072396, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 7.3, 0.0, 3.0)
    ops.node(122002, 7.3, 0.0, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.2025, 30115486.64328622, 12548119.43470259, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 250.49775398, 0.00071426, 300.86646053, 0.00927525, 30.08664605, 0.03858004, -250.49775398, -0.00071426, -300.86646053, -0.00927525, -30.08664605, -0.03858004, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 212.68320652, 0.00071426, 255.44837246, 0.00927525, 25.54483725, 0.03858004, -212.68320652, -0.00071426, -255.44837246, -0.00927525, -25.54483725, -0.03858004, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 244.12143218, 0.01428527, 244.12143218, 0.04285581, 170.88500253, -2674.20276852, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 61.03035805, 7.638e-05, 183.09107414, 0.00022913, 610.30358046, 0.00076378, -61.03035805, -7.638e-05, -183.09107414, -0.00022913, -610.30358046, -0.00076378, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 244.12143218, 0.01428527, 244.12143218, 0.04285581, 170.88500253, -2674.20276852, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 61.03035805, 7.638e-05, 183.09107414, 0.00022913, 610.30358046, 0.00076378, -61.03035805, -7.638e-05, -183.09107414, -0.00022913, -610.30358046, -0.00076378, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 24.95, 0.0, 3.0)
    ops.node(122005, 24.95, 0.0, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.2025, 24201301.1982156, 10083875.4992565, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 240.30046848, 0.00072801, 288.58596287, 0.00885874, 28.85859629, 0.02815676, -240.30046848, -0.00072801, -288.58596287, -0.00885874, -28.85859629, -0.02815676, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 203.98815704, 0.00072801, 244.97712836, 0.00885874, 24.49771284, 0.02815676, -203.98815704, -0.00072801, -244.97712836, -0.00885874, -24.49771284, -0.02815676, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 208.33063689, 0.01456014, 208.33063689, 0.04368041, 145.83144583, -2775.66689996, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 52.08265922, 8.111e-05, 156.24797767, 0.00024333, 520.82659223, 0.00081109, -52.08265922, -8.111e-05, -156.24797767, -0.00024333, -520.82659223, -0.00081109, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 208.33063689, 0.01456014, 208.33063689, 0.04368041, 145.83144583, -2775.66689996, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 52.08265922, 8.111e-05, 156.24797767, 0.00024333, 520.82659223, 0.00081109, -52.08265922, -8.111e-05, -156.24797767, -0.00024333, -520.82659223, -0.00081109, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 32.25, 0.0, 3.0)
    ops.node(122006, 32.25, 0.0, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.09, 27502072.27622139, 11459196.78175891, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 104.01180256, 0.00095272, 124.63537902, 0.01101533, 12.4635379, 0.03698089, -104.01180256, -0.00095272, -124.63537902, -0.01101533, -12.4635379, -0.03698089, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 94.92850665, 0.00095272, 113.75103704, 0.01101533, 11.3751037, 0.03698089, -94.92850665, -0.00095272, -113.75103704, -0.01101533, -11.3751037, -0.03698089, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 106.1104535, 0.01905444, 106.1104535, 0.05716332, 74.27731745, -1452.23068821, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 26.52761337, 8.18e-05, 79.58284012, 0.00024539, 265.27613374, 0.00081795, -26.52761337, -8.18e-05, -79.58284012, -0.00024539, -265.27613374, -0.00081795, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 106.1104535, 0.01905444, 106.1104535, 0.05716332, 74.27731745, -1452.23068821, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 26.52761337, 8.18e-05, 79.58284012, 0.00024539, 265.27613374, 0.00081795, -26.52761337, -8.18e-05, -79.58284012, -0.00024539, -265.27613374, -0.00081795, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 3.65, 3.0)
    ops.node(122007, 0.0, 3.65, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 23975001.20258065, 9989583.83440861, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 220.16060059, 0.00087977, 261.99395988, 0.0087982, 26.19939599, 0.02402727, -220.16060059, -0.00087977, -261.99395988, -0.0087982, -26.19939599, -0.02402727, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 171.34187074, 0.00087977, 203.89904045, 0.0087982, 20.38990405, 0.02402727, -171.34187074, -0.00087977, -203.89904045, -0.0087982, -20.38990405, -0.02402727, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 122.61685491, 0.01759546, 122.61685491, 0.05278639, 85.83179843, -1752.34142726, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 30.65421373, 7.966e-05, 91.96264118, 0.00023898, 306.54213726, 0.00079659, -30.65421373, -7.966e-05, -91.96264118, -0.00023898, -306.54213726, -0.00079659, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 122.61685491, 0.01759546, 122.61685491, 0.05278639, 85.83179843, -1752.34142726, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 30.65421373, 7.966e-05, 91.96264118, 0.00023898, 306.54213726, 0.00079659, -30.65421373, -7.966e-05, -91.96264118, -0.00023898, -306.54213726, -0.00079659, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 7.3, 3.65, 3.0)
    ops.node(122008, 7.3, 3.65, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.25, 27025307.15290509, 11260544.64704379, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 306.29876709, 0.00064807, 369.22455589, 0.00822973, 36.92245559, 0.02623816, -306.29876709, -0.00064807, -369.22455589, -0.00822973, -36.92245559, -0.02623816, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 290.02608444, 0.00064807, 349.60882553, 0.00822973, 34.96088255, 0.02623816, -290.02608444, -0.00064807, -349.60882553, -0.00822973, -34.96088255, -0.02623816, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 254.12211479, 0.01296137, 254.12211479, 0.0388841, 177.88548035, -2259.03232035, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 63.5305287, 7.176e-05, 190.59158609, 0.00021529, 635.30528698, 0.00071765, -63.5305287, -7.176e-05, -190.59158609, -0.00021529, -635.30528698, -0.00071765, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 254.12211479, 0.01296137, 254.12211479, 0.0388841, 177.88548035, -2259.03232035, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 63.5305287, 7.176e-05, 190.59158609, 0.00021529, 635.30528698, 0.00071765, -63.5305287, -7.176e-05, -190.59158609, -0.00021529, -635.30528698, -0.00071765, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 14.6, 3.65, 3.0)
    ops.node(122009, 14.6, 3.65, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.2025, 24433034.88105787, 10180431.20044078, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 245.49275727, 0.00071679, 295.72165952, 0.00760606, 29.57216595, 0.02657828, -245.49275727, -0.00071679, -295.72165952, -0.00760606, -29.57216595, -0.02657828, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 216.85714642, 0.00071679, 261.22707623, 0.00760606, 26.12270762, 0.02657828, -216.85714642, -0.00071679, -261.22707623, -0.00760606, -26.12270762, -0.02657828, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 182.15553372, 0.01433584, 182.15553372, 0.04300752, 127.5088736, -2072.87510434, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 45.53888343, 7.025e-05, 136.61665029, 0.00021074, 455.3888343, 0.00070245, -45.53888343, -7.025e-05, -136.61665029, -0.00021074, -455.3888343, -0.00070245, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 182.15553372, 0.01433584, 182.15553372, 0.04300752, 127.5088736, -2072.87510434, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 45.53888343, 7.025e-05, 136.61665029, 0.00021074, 455.3888343, 0.00070245, -45.53888343, -7.025e-05, -136.61665029, -0.00021074, -455.3888343, -0.00070245, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 17.65, 3.65, 3.0)
    ops.node(122010, 17.65, 3.65, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.2025, 24791109.24488717, 10329628.85203632, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 242.20757915, 0.00071319, 291.89653481, 0.00880756, 29.18965348, 0.02842263, -242.20757915, -0.00071319, -291.89653481, -0.00880756, -29.18965348, -0.02842263, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 214.59351191, 0.00071319, 258.61743361, 0.00880756, 25.86174336, 0.02842263, -214.59351191, -0.00071319, -258.61743361, -0.00880756, -25.86174336, -0.02842263, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 188.91282474, 0.01426384, 188.91282474, 0.04279151, 132.23897732, -2189.09426992, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 47.22820619, 7.18e-05, 141.68461856, 0.0002154, 472.28206186, 0.00071799, -47.22820619, -7.18e-05, -141.68461856, -0.0002154, -472.28206186, -0.00071799, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 188.91282474, 0.01426384, 188.91282474, 0.04279151, 132.23897732, -2189.09426992, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 47.22820619, 7.18e-05, 141.68461856, 0.0002154, 472.28206186, 0.00071799, -47.22820619, -7.18e-05, -141.68461856, -0.0002154, -472.28206186, -0.00071799, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 24.95, 3.65, 3.0)
    ops.node(122011, 24.95, 3.65, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.25, 28081799.69338064, 11700749.87224193, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 315.50957621, 0.00064093, 380.15878162, 0.00773191, 38.01587816, 0.02690884, -315.50957621, -0.00064093, -380.15878162, -0.00773191, -38.01587816, -0.02690884, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 297.81317094, 0.00064093, 358.83631037, 0.00773191, 35.88363104, 0.02690884, -297.81317094, -0.00064093, -358.83631037, -0.00773191, -35.88363104, -0.02690884, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 260.85927915, 0.0128185, 260.85927915, 0.03845551, 182.60149541, -2191.06887512, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 65.21481979, 7.09e-05, 195.64445936, 0.00021269, 652.14819788, 0.00070896, -65.21481979, -7.09e-05, -195.64445936, -0.00021269, -652.14819788, -0.00070896, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 260.85927915, 0.0128185, 260.85927915, 0.03845551, 182.60149541, -2191.06887512, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 65.21481979, 7.09e-05, 195.64445936, 0.00021269, 652.14819788, 0.00070896, -65.21481979, -7.09e-05, -195.64445936, -0.00021269, -652.14819788, -0.00070896, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 32.25, 3.65, 3.0)
    ops.node(122012, 32.25, 3.65, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 25671816.96329775, 10696590.40137406, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 220.72824426, 0.00090775, 263.78772222, 0.01009076, 26.37877222, 0.02911472, -220.72824426, -0.00090775, -263.78772222, -0.01009076, -26.37877222, -0.02911472, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 174.39807595, 0.00090775, 208.41950413, 0.01009076, 20.84195041, 0.02911472, -174.39807595, -0.00090775, -208.41950413, -0.01009076, -20.84195041, -0.02911472, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 127.83420285, 0.01815509, 127.83420285, 0.05446528, 89.48394199, -1725.01599003, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 31.95855071, 7.756e-05, 95.87565214, 0.00023268, 319.58550712, 0.00077559, -31.95855071, -7.756e-05, -95.87565214, -0.00023268, -319.58550712, -0.00077559, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 127.83420285, 0.01815509, 127.83420285, 0.05446528, 89.48394199, -1725.01599003, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 31.95855071, 7.756e-05, 95.87565214, 0.00023268, 319.58550712, 0.00077559, -31.95855071, -7.756e-05, -95.87565214, -0.00023268, -319.58550712, -0.00077559, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 7.3, 3.0)
    ops.node(122013, 0.0, 7.3, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.09, 24562320.24335422, 10234300.10139759, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 125.35941083, 0.00101315, 149.61260958, 0.01036172, 14.96126096, 0.02948827, -125.35941083, -0.00101315, -149.61260958, -0.01036172, -14.96126096, -0.02948827, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 108.1859664, 0.00101315, 129.11663069, 0.01036172, 12.91166307, 0.02948827, -108.1859664, -0.00101315, -129.11663069, -0.01036172, -12.91166307, -0.02948827, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 100.01346411, 0.02026291, 100.01346411, 0.06078873, 70.00942487, -1507.85917452, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 25.00336603, 8.632e-05, 75.01009808, 0.00025897, 250.03366026, 0.00086323, -25.00336603, -8.632e-05, -75.01009808, -0.00025897, -250.03366026, -0.00086323, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 100.01346411, 0.02026291, 100.01346411, 0.06078873, 70.00942487, -1507.85917452, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 25.00336603, 8.632e-05, 75.01009808, 0.00025897, 250.03366026, 0.00086323, -25.00336603, -8.632e-05, -75.01009808, -0.00025897, -250.03366026, -0.00086323, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 7.3, 7.3, 3.0)
    ops.node(122014, 7.3, 7.3, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.2025, 25627691.6281012, 10678204.84504217, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 243.01540991, 0.00071868, 292.42488073, 0.00714365, 29.24248807, 0.02934787, -243.01540991, -0.00071868, -292.42488073, -0.00714365, -29.24248807, -0.02934787, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 205.9561437, 0.00071868, 247.83078892, 0.00714365, 24.78307889, 0.02934787, -205.9561437, -0.00071868, -247.83078892, -0.00714365, -24.78307889, -0.02934787, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 203.27960716, 0.01437359, 203.27960716, 0.04312078, 142.29572501, -2392.94469891, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 50.81990179, 7.474e-05, 152.45970537, 0.00022421, 508.19901789, 0.00074737, -50.81990179, -7.474e-05, -152.45970537, -0.00022421, -508.19901789, -0.00074737, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 203.27960716, 0.01437359, 203.27960716, 0.04312078, 142.29572501, -2392.94469891, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 50.81990179, 7.474e-05, 152.45970537, 0.00022421, 508.19901789, 0.00074737, -50.81990179, -7.474e-05, -152.45970537, -0.00022421, -508.19901789, -0.00074737, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 14.6, 7.3, 3.0)
    ops.node(122015, 14.6, 7.3, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.1225, 26532138.40400457, 11055057.66833524, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 120.43806395, 0.0008005, 144.53583598, 0.00985068, 14.4535836, 0.03578321, -120.43806395, -0.0008005, -144.53583598, -0.00985068, -14.4535836, -0.03578321, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 107.91980232, 0.0008005, 129.51286607, 0.00985068, 12.95128661, 0.03578321, -107.91980232, -0.0008005, -129.51286607, -0.00985068, -12.95128661, -0.03578321, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 141.11780099, 0.01601006, 141.11780099, 0.04803019, 98.78246069, -2008.94664767, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 35.27945025, 8.284e-05, 105.83835074, 0.00024853, 352.79450248, 0.00082842, -35.27945025, -8.284e-05, -105.83835074, -0.00024853, -352.79450248, -0.00082842, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 141.11780099, 0.01601006, 141.11780099, 0.04803019, 98.78246069, -2008.94664767, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 35.27945025, 8.284e-05, 105.83835074, 0.00024853, 352.79450248, 0.00082842, -35.27945025, -8.284e-05, -105.83835074, -0.00024853, -352.79450248, -0.00082842, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 17.65, 7.3, 3.0)
    ops.node(122016, 17.65, 7.3, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1225, 27270427.59172032, 11362678.1632168, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 127.74227232, 0.00081278, 153.35307684, 0.0087346, 15.33530768, 0.03627935, -127.74227232, -0.00081278, -153.35307684, -0.0087346, -15.33530768, -0.03627935, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 113.2333577, 0.00081278, 135.9352976, 0.0087346, 13.59352976, 0.03627935, -113.2333577, -0.00081278, -135.9352976, -0.0087346, -13.59352976, -0.03627935, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 138.19013372, 0.01625564, 138.19013372, 0.04876692, 96.7330936, -1850.20497101, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 34.54753343, 7.893e-05, 103.64260029, 0.00023678, 345.4753343, 0.00078927, -34.54753343, -7.893e-05, -103.64260029, -0.00023678, -345.4753343, -0.00078927, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 138.19013372, 0.01625564, 138.19013372, 0.04876692, 96.7330936, -1850.20497101, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 34.54753343, 7.893e-05, 103.64260029, 0.00023678, 345.4753343, 0.00078927, -34.54753343, -7.893e-05, -103.64260029, -0.00023678, -345.4753343, -0.00078927, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 24.95, 7.3, 3.0)
    ops.node(122017, 24.95, 7.3, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.2025, 25479924.09391183, 10616635.03912993, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 236.02994879, 0.00074226, 283.98052454, 0.00755312, 28.39805245, 0.02947098, -236.02994879, -0.00074226, -283.98052454, -0.00755312, -28.39805245, -0.02947098, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 203.4535761, 0.00074226, 244.78611106, 0.00755312, 24.47861111, 0.02947098, -203.4535761, -0.00074226, -244.78611106, -0.00755312, -24.47861111, -0.02947098, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 203.63855433, 0.01484517, 203.63855433, 0.0445355, 142.54698803, -2427.25601233, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 50.90963858, 7.53e-05, 152.72891575, 0.00022591, 509.09638583, 0.00075304, -50.90963858, -7.53e-05, -152.72891575, -0.00022591, -509.09638583, -0.00075304, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 203.63855433, 0.01484517, 203.63855433, 0.0445355, 142.54698803, -2427.25601233, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 50.90963858, 7.53e-05, 152.72891575, 0.00022591, 509.09638583, 0.00075304, -50.90963858, -7.53e-05, -152.72891575, -0.00022591, -509.09638583, -0.00075304, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 32.25, 7.3, 3.0)
    ops.node(122018, 32.25, 7.3, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.09, 28372971.32706002, 11822071.38627501, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 112.00254368, 0.00094362, 134.21566189, 0.00991982, 13.42156619, 0.03765496, -112.00254368, -0.00094362, -134.21566189, -0.00991982, -13.42156619, -0.03765496, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 98.90706224, 0.00094362, 118.5229941, 0.00991982, 11.85229941, 0.03765496, -98.90706224, -0.00094362, -118.5229941, -0.00991982, -11.85229941, -0.03765496, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 92.20525515, 0.01887246, 92.20525515, 0.05661737, 64.5436786, -1308.08599297, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 23.05131379, 6.889e-05, 69.15394136, 0.00020668, 230.51313786, 0.00068895, -23.05131379, -6.889e-05, -69.15394136, -0.00020668, -230.51313786, -0.00068895, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 92.20525515, 0.01887246, 92.20525515, 0.05661737, 64.5436786, -1308.08599297, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 23.05131379, 6.889e-05, 69.15394136, 0.00020668, 230.51313786, 0.00068895, -23.05131379, -6.889e-05, -69.15394136, -0.00020668, -230.51313786, -0.00068895, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.65)
    ops.node(123001, 0.0, 0.0, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 27364793.8075369, 11401997.41980704, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 55.23501877, 0.00105171, 66.32816064, 0.01114574, 6.63281606, 0.04254708, -55.23501877, -0.00105171, -66.32816064, -0.01114574, -6.63281606, -0.04254708, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 55.23501877, 0.00105171, 66.32816064, 0.01114574, 6.63281606, 0.04254708, -55.23501877, -0.00105171, -66.32816064, -0.01114574, -6.63281606, -0.04254708, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 58.03719778, 0.02103414, 58.03719778, 0.06310241, 40.62603845, -1155.90789162, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 14.50929944, 6.475e-05, 43.52789833, 0.00019424, 145.09299445, 0.00064746, -14.50929944, -6.475e-05, -43.52789833, -0.00019424, -145.09299445, -0.00064746, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 58.03719778, 0.02103414, 58.03719778, 0.06310241, 40.62603845, -1155.90789162, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 14.50929944, 6.475e-05, 43.52789833, 0.00019424, 145.09299445, 0.00064746, -14.50929944, -6.475e-05, -43.52789833, -0.00019424, -145.09299445, -0.00064746, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 7.3, 0.0, 5.65)
    ops.node(123002, 7.3, 0.0, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1225, 27502014.1356547, 11459172.55652279, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 113.44197264, 0.00085054, 136.45720159, 0.01002913, 13.64572016, 0.03974307, -113.44197264, -0.00085054, -136.45720159, -0.01002913, -13.64572016, -0.03974307, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 103.00039931, 0.00085054, 123.89723067, 0.01002913, 12.38972307, 0.03974307, -103.00039931, -0.00085054, -123.89723067, -0.01002913, -12.38972307, -0.03974307, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 140.78072827, 0.0170107, 140.78072827, 0.0510321, 98.54650979, -1928.33070335, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 35.19518207, 7.973e-05, 105.5855462, 0.00023919, 351.95182067, 0.0007973, -35.19518207, -7.973e-05, -105.5855462, -0.00023919, -351.95182067, -0.0007973, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 140.78072827, 0.0170107, 140.78072827, 0.0510321, 98.54650979, -1928.33070335, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 35.19518207, 7.973e-05, 105.5855462, 0.00023919, 351.95182067, 0.0007973, -35.19518207, -7.973e-05, -105.5855462, -0.00023919, -351.95182067, -0.0007973, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 24.95, 0.0, 5.65)
    ops.node(123005, 24.95, 0.0, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 26768059.92980502, 11153358.30408542, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 113.51178007, 0.00081047, 136.53549361, 0.00770851, 13.65354936, 0.03590976, -113.51178007, -0.00081047, -136.53549361, -0.00770851, -13.65354936, -0.03590976, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 102.06840887, 0.00081047, 122.77105142, 0.00770851, 12.27710514, 0.03590976, -102.06840887, -0.00081047, -122.77105142, -0.00770851, -12.27710514, -0.03590976, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 129.59103053, 0.01620934, 129.59103053, 0.04862802, 90.71372137, -1689.38885709, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 32.39775763, 7.541e-05, 97.1932729, 0.00022622, 323.97757632, 0.00075405, -32.39775763, -7.541e-05, -97.1932729, -0.00022622, -323.97757632, -0.00075405, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 129.59103053, 0.01620934, 129.59103053, 0.04862802, 90.71372137, -1689.38885709, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 32.39775763, 7.541e-05, 97.1932729, 0.00022622, 323.97757632, 0.00075405, -32.39775763, -7.541e-05, -97.1932729, -0.00022622, -323.97757632, -0.00075405, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 32.25, 0.0, 5.65)
    ops.node(123006, 32.25, 0.0, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 29571098.93943129, 12321291.22476304, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 54.7247345, 0.00142214, 65.64554569, 0.01031254, 6.56455457, 0.04642949, -54.7247345, -0.00142214, -65.64554569, -0.01031254, -6.56455457, -0.04642949, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 54.7247345, 0.00142214, 65.64554569, 0.01031254, 6.56455457, 0.04642949, -54.7247345, -0.00142214, -65.64554569, -0.01031254, -6.56455457, -0.04642949, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 51.20196454, 0.02844287, 51.20196454, 0.0853286, 35.84137518, -1028.6296994, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 12.80049113, 5.286e-05, 38.4014734, 0.00015858, 128.00491135, 0.00052859, -12.80049113, -5.286e-05, -38.4014734, -0.00015858, -128.00491135, -0.00052859, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 51.20196454, 0.02844287, 51.20196454, 0.0853286, 35.84137518, -1028.6296994, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 12.80049113, 5.286e-05, 38.4014734, 0.00015858, 128.00491135, 0.00052859, -12.80049113, -5.286e-05, -38.4014734, -0.00015858, -128.00491135, -0.00052859, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 3.65, 5.65)
    ops.node(123007, 0.0, 3.65, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 27973264.05106907, 11655526.68794545, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 83.92267695, 0.00122061, 99.87559567, 0.01128231, 9.98755957, 0.03639027, -83.92267695, -0.00122061, -99.87559567, -0.01128231, -9.98755957, -0.03639027, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 76.58429532, 0.00122061, 91.1422561, 0.01128231, 9.11422561, 0.03639027, -76.58429532, -0.00122061, -91.1422561, -0.01128231, -9.11422561, -0.03639027, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 75.02550158, 0.02441223, 75.02550158, 0.0732367, 52.51785111, -1336.43764405, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 18.7563754, 8.188e-05, 56.26912619, 0.00024563, 187.56375395, 0.00081877, -18.7563754, -8.188e-05, -56.26912619, -0.00024563, -187.56375395, -0.00081877, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 75.02550158, 0.02441223, 75.02550158, 0.0732367, 52.51785111, -1336.43764405, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 18.7563754, 8.188e-05, 56.26912619, 0.00024563, 187.56375395, 0.00081877, -18.7563754, -8.188e-05, -56.26912619, -0.00024563, -187.56375395, -0.00081877, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 7.3, 3.65, 5.65)
    ops.node(123008, 7.3, 3.65, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.16, 25139062.19864048, 10474609.24943353, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 182.27461979, 0.00075817, 219.24846863, 0.00667717, 21.92484686, 0.02369301, -182.27461979, -0.00075817, -219.24846863, -0.00667717, -21.92484686, -0.02369301, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 182.27461979, 0.00075817, 219.24846863, 0.00667717, 21.92484686, 0.02369301, -182.27461979, -0.00075817, -219.24846863, -0.00667717, -21.92484686, -0.02369301, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 118.98246554, 0.01516343, 118.98246554, 0.04549028, 83.28772588, -1501.52712551, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 29.74561638, 5.644e-05, 89.23684915, 0.00016932, 297.45616384, 0.00056441, -29.74561638, -5.644e-05, -89.23684915, -0.00016932, -297.45616384, -0.00056441, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 118.98246554, 0.01516343, 118.98246554, 0.04549028, 83.28772588, -1501.52712551, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 29.74561638, 5.644e-05, 89.23684915, 0.00016932, 297.45616384, 0.00056441, -29.74561638, -5.644e-05, -89.23684915, -0.00016932, -297.45616384, -0.00056441, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 14.6, 3.65, 5.65)
    ops.node(123009, 14.6, 3.65, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 28802688.24714015, 12001120.10297506, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 127.6065955, 0.00081425, 153.51668563, 0.00942269, 15.35166856, 0.03831702, -127.6065955, -0.00081425, -153.51668563, -0.00942269, -15.35166856, -0.03831702, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 120.79800342, 0.00081425, 145.32563183, 0.00942269, 14.53256318, 0.03831702, -120.79800342, -0.00081425, -145.32563183, -0.00942269, -14.53256318, -0.03831702, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 135.34947826, 0.0162851, 135.34947826, 0.0488553, 94.74463478, -1649.81447792, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 33.83736956, 7.319e-05, 101.51210869, 0.00021958, 338.37369565, 0.00073192, -33.83736956, -7.319e-05, -101.51210869, -0.00021958, -338.37369565, -0.00073192, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 135.34947826, 0.0162851, 135.34947826, 0.0488553, 94.74463478, -1649.81447792, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 33.83736956, 7.319e-05, 101.51210869, 0.00021958, 338.37369565, 0.00073192, -33.83736956, -7.319e-05, -101.51210869, -0.00021958, -338.37369565, -0.00073192, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 17.65, 3.65, 5.65)
    ops.node(123010, 17.65, 3.65, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 32318170.82684648, 13465904.51118603, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 119.84502341, 0.00081025, 143.31525777, 0.01019585, 14.33152578, 0.04355916, -119.84502341, -0.00081025, -143.31525777, -0.01019585, -14.33152578, -0.04355916, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 114.49406235, 0.00081025, 136.91637409, 0.01019585, 13.69163741, 0.04355916, -114.49406235, -0.00081025, -136.91637409, -0.01019585, -13.69163741, -0.04355916, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 147.8869608, 0.0162049, 147.8869608, 0.04861471, 103.52087256, -1614.5773846, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 36.9717402, 7.127e-05, 110.9152206, 0.00021382, 369.717402, 0.00071273, -36.9717402, -7.127e-05, -110.9152206, -0.00021382, -369.717402, -0.00071273, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 147.8869608, 0.0162049, 147.8869608, 0.04861471, 103.52087256, -1614.5773846, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 36.9717402, 7.127e-05, 110.9152206, 0.00021382, 369.717402, 0.00071273, -36.9717402, -7.127e-05, -110.9152206, -0.00021382, -369.717402, -0.00071273, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 24.95, 3.65, 5.65)
    ops.node(123011, 24.95, 3.65, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.16, 27469593.70963404, 11445664.04568085, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 172.48772853, 0.00074046, 207.68728219, 0.00959866, 20.76872822, 0.02999214, -172.48772853, -0.00074046, -207.68728219, -0.00959866, -20.76872822, -0.02999214, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 172.48772853, 0.00074046, 207.68728219, 0.00959866, 20.76872822, 0.02999214, -172.48772853, -0.00074046, -207.68728219, -0.00959866, -20.76872822, -0.02999214, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 150.83778123, 0.0148093, 150.83778123, 0.04442789, 105.58644686, -1651.4697162, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 37.70944531, 6.548e-05, 113.12833592, 0.00019644, 377.09445307, 0.00065481, -37.70944531, -6.548e-05, -113.12833592, -0.00019644, -377.09445307, -0.00065481, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 150.83778123, 0.0148093, 150.83778123, 0.04442789, 105.58644686, -1651.4697162, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 37.70944531, 6.548e-05, 113.12833592, 0.00019644, 377.09445307, 0.00065481, -37.70944531, -6.548e-05, -113.12833592, -0.00019644, -377.09445307, -0.00065481, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 32.25, 3.65, 5.65)
    ops.node(123012, 32.25, 3.65, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 30668497.86614798, 12778540.77756166, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 85.6578241, 0.0011514, 101.92900154, 0.01210487, 10.19290015, 0.0434313, -85.6578241, -0.0011514, -101.92900154, -0.01210487, -10.19290015, -0.0434313, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 77.8623423, 0.0011514, 92.65272485, 0.01210487, 9.26527249, 0.0434313, -77.8623423, -0.0011514, -92.65272485, -0.01210487, -9.26527249, -0.0434313, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 81.50839972, 0.02302809, 81.50839972, 0.06908428, 57.0558798, -1314.45581615, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 20.37709993, 8.113e-05, 61.13129979, 0.0002434, 203.7709993, 0.00081135, -20.37709993, -8.113e-05, -61.13129979, -0.0002434, -203.7709993, -0.00081135, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 81.50839972, 0.02302809, 81.50839972, 0.06908428, 57.0558798, -1314.45581615, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 20.37709993, 8.113e-05, 61.13129979, 0.0002434, 203.7709993, 0.00081135, -20.37709993, -8.113e-05, -61.13129979, -0.0002434, -203.7709993, -0.00081135, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 7.3, 5.65)
    ops.node(123013, 0.0, 7.3, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 26479004.57992667, 11032918.57496945, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 55.93346573, 0.00112881, 67.14262496, 0.01207471, 6.7142625, 0.04131771, -55.93346573, -0.00112881, -67.14262496, -0.01207471, -6.7142625, -0.04131771, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 55.93346573, 0.00112881, 67.14262496, 0.01207471, 6.7142625, 0.04131771, -55.93346573, -0.00112881, -67.14262496, -0.01207471, -6.7142625, -0.04131771, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 74.78317297, 0.02257617, 74.78317297, 0.06772851, 52.34822108, -1288.34230331, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 18.69579324, 8.622e-05, 56.08737973, 0.00025866, 186.95793242, 0.00086219, -18.69579324, -8.622e-05, -56.08737973, -0.00025866, -186.95793242, -0.00086219, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 74.78317297, 0.02257617, 74.78317297, 0.06772851, 52.34822108, -1288.34230331, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 18.69579324, 8.622e-05, 56.08737973, 0.00025866, 186.95793242, 0.00086219, -18.69579324, -8.622e-05, -56.08737973, -0.00025866, -186.95793242, -0.00086219, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 7.3, 7.3, 5.65)
    ops.node(123014, 7.3, 7.3, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1225, 27890818.18734644, 11621174.24472768, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 122.20589898, 0.00085969, 146.98423556, 0.00804149, 14.69842356, 0.03851726, -122.20589898, -0.00085969, -146.98423556, -0.00804149, -14.69842356, -0.03851726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 109.12291813, 0.00085969, 131.24856358, 0.00804149, 13.12485636, 0.03851726, -109.12291813, -0.00085969, -131.24856358, -0.00804149, -13.12485636, -0.03851726, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 131.91996219, 0.01719372, 131.91996219, 0.05158117, 92.34397353, -1638.43920021, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 32.97999055, 7.367e-05, 98.93997164, 0.00022101, 329.79990547, 0.0007367, -32.97999055, -7.367e-05, -98.93997164, -0.00022101, -329.79990547, -0.0007367, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 131.91996219, 0.01719372, 131.91996219, 0.05158117, 92.34397353, -1638.43920021, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 32.97999055, 7.367e-05, 98.93997164, 0.00022101, 329.79990547, 0.0007367, -32.97999055, -7.367e-05, -98.93997164, -0.00022101, -329.79990547, -0.0007367, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 14.6, 7.3, 5.65)
    ops.node(123015, 14.6, 7.3, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 27021734.7892512, 11259056.162188, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 47.23729613, 0.00120095, 56.40556025, 0.00830292, 5.64055603, 0.03819807, -47.23729613, -0.00120095, -56.40556025, -0.00830292, -5.64055603, -0.03819807, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 47.23729613, 0.00120095, 56.40556025, 0.00830292, 5.64055603, 0.03819807, -47.23729613, -0.00120095, -56.40556025, -0.00830292, -5.64055603, -0.03819807, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 68.31512309, 0.024019, 68.31512309, 0.07205701, 47.82058617, -1285.3363818, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 17.07878077, 7.718e-05, 51.23634232, 0.00023154, 170.78780774, 0.0007718, -17.07878077, -7.718e-05, -51.23634232, -0.00023154, -170.78780774, -0.0007718, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 68.31512309, 0.024019, 68.31512309, 0.07205701, 47.82058617, -1285.3363818, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 17.07878077, 7.718e-05, 51.23634232, 0.00023154, 170.78780774, 0.0007718, -17.07878077, -7.718e-05, -51.23634232, -0.00023154, -170.78780774, -0.0007718, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 17.65, 7.3, 5.65)
    ops.node(123016, 17.65, 7.3, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 27078712.61291431, 11282796.92204763, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 48.90024678, 0.00103791, 58.39462119, 0.00945762, 5.83946212, 0.03952186, -48.90024678, -0.00103791, -58.39462119, -0.00945762, -5.83946212, -0.03952186, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 48.90024678, 0.00103791, 58.39462119, 0.00945762, 5.83946212, 0.03952186, -48.90024678, -0.00103791, -58.39462119, -0.00945762, -5.83946212, -0.03952186, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 83.21722239, 0.02075829, 83.21722239, 0.06227488, 58.25205567, -1324.68408131, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 20.8043056, 9.382e-05, 62.41291679, 0.00028145, 208.04305597, 0.00093817, -20.8043056, -9.382e-05, -62.41291679, -0.00028145, -208.04305597, -0.00093817, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 83.21722239, 0.02075829, 83.21722239, 0.06227488, 58.25205567, -1324.68408131, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 20.8043056, 9.382e-05, 62.41291679, 0.00028145, 208.04305597, 0.00093817, -20.8043056, -9.382e-05, -62.41291679, -0.00028145, -208.04305597, -0.00093817, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 24.95, 7.3, 5.65)
    ops.node(123017, 24.95, 7.3, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.1225, 29415860.18708752, 12256608.41128647, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 123.59654613, 0.00081478, 148.48511017, 0.0109805, 14.84851102, 0.04419069, -123.59654613, -0.00081478, -148.48511017, -0.0109805, -14.84851102, -0.04419069, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 109.52107356, 0.00081478, 131.57526794, 0.0109805, 13.15752679, 0.04419069, -109.52107356, -0.00081478, -131.57526794, -0.0109805, -13.15752679, -0.04419069, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 156.62767194, 0.01629563, 156.62767194, 0.04888689, 109.63937036, -2185.94310586, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 39.15691799, 8.293e-05, 117.47075396, 0.0002488, 391.56917986, 0.00082933, -39.15691799, -8.293e-05, -117.47075396, -0.0002488, -391.56917986, -0.00082933, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 156.62767194, 0.01629563, 156.62767194, 0.04888689, 109.63937036, -2185.94310586, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 39.15691799, 8.293e-05, 117.47075396, 0.0002488, 391.56917986, 0.00082933, -39.15691799, -8.293e-05, -117.47075396, -0.0002488, -391.56917986, -0.00082933, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 32.25, 7.3, 5.65)
    ops.node(123018, 32.25, 7.3, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 27691366.73448351, 11538069.47270146, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 56.43213355, 0.00110178, 67.76648831, 0.01211761, 6.77664883, 0.04427583, -56.43213355, -0.00110178, -67.76648831, -0.01211761, -6.77664883, -0.04427583, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 56.43213355, 0.00110178, 67.76648831, 0.01211761, 6.77664883, 0.04427583, -56.43213355, -0.00110178, -67.76648831, -0.01211761, -6.77664883, -0.04427583, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 70.48866122, 0.02203562, 70.48866122, 0.06610687, 49.34206285, -1157.91662177, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 17.6221653, 7.771e-05, 52.86649591, 0.00023313, 176.22165304, 0.00077709, -17.6221653, -7.771e-05, -52.86649591, -0.00023313, -176.22165304, -0.00077709, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 70.48866122, 0.02203562, 70.48866122, 0.06610687, 49.34206285, -1157.91662177, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 17.6221653, 7.771e-05, 52.86649591, 0.00023313, 176.22165304, 0.00077709, -17.6221653, -7.771e-05, -52.86649591, -0.00023313, -176.22165304, -0.00077709, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.3)
    ops.node(124001, 0.0, 0.0, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 31959918.2927652, 13316632.6219855, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 43.20778409, 0.00094467, 52.05575661, 0.01048928, 5.20557566, 0.06184907, -43.20778409, -0.00094467, -52.05575661, -0.01048928, -5.20557566, -0.06184907, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 43.20778409, 0.00094467, 52.05575661, 0.01048928, 5.20557566, 0.06184907, -43.20778409, -0.00094467, -52.05575661, -0.01048928, -5.20557566, -0.06184907, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 43.80629977, 0.01889334, 43.80629977, 0.05668002, 30.66440984, -1017.43064634, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 10.95157494, 4.184e-05, 32.85472483, 0.00012553, 109.51574943, 0.00041844, -10.95157494, -4.184e-05, -32.85472483, -0.00012553, -109.51574943, -0.00041844, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 43.80629977, 0.01889334, 43.80629977, 0.05668002, 30.66440984, -1017.43064634, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 10.95157494, 4.184e-05, 32.85472483, 0.00012553, 109.51574943, 0.00041844, -10.95157494, -4.184e-05, -32.85472483, -0.00012553, -109.51574943, -0.00041844, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 7.3, 0.0, 8.3)
    ops.node(124002, 7.3, 0.0, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1225, 27745440.79391793, 11560600.33079914, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 78.83374092, 0.00086252, 95.92049303, 0.00887198, 9.5920493, 0.05142858, -78.83374092, -0.00086252, -95.92049303, -0.00887198, -9.5920493, -0.05142858, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 70.7920692, 0.00086252, 86.13583602, 0.00887198, 8.6135836, 0.05142858, -70.7920692, -0.00086252, -86.13583602, -0.00887198, -8.6135836, -0.05142858, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 113.16938785, 0.01725047, 113.16938785, 0.05175142, 79.21857149, -1566.27041225, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 28.29234696, 6.353e-05, 84.87704088, 0.00019059, 282.92346962, 0.0006353, -28.29234696, -6.353e-05, -84.87704088, -0.00019059, -282.92346962, -0.0006353, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 113.16938785, 0.01725047, 113.16938785, 0.05175142, 79.21857149, -1566.27041225, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 28.29234696, 6.353e-05, 84.87704088, 0.00019059, 282.92346962, 0.0006353, -28.29234696, -6.353e-05, -84.87704088, -0.00019059, -282.92346962, -0.0006353, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 24.95, 0.0, 8.3)
    ops.node(124005, 24.95, 0.0, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 24236924.1569918, 10098718.39874659, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 83.46539828, 0.00075345, 101.9324298, 0.01106851, 10.19324298, 0.04916338, -83.46539828, -0.00075345, -101.9324298, -0.01106851, -10.19324298, -0.04916338, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 71.20817825, 0.00075345, 86.96325401, 0.01106851, 8.6963254, 0.04916338, -71.20817825, -0.00075345, -86.96325401, -0.01106851, -8.6963254, -0.04916338, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 109.51225836, 0.0150689, 109.51225836, 0.0452067, 76.65858085, -1943.4821887, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 27.37806459, 7.038e-05, 82.13419377, 0.00021113, 273.78064589, 0.00070376, -27.37806459, -7.038e-05, -82.13419377, -0.00021113, -273.78064589, -0.00070376, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 109.51225836, 0.0150689, 109.51225836, 0.0452067, 76.65858085, -1943.4821887, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 27.37806459, 7.038e-05, 82.13419377, 0.00021113, 273.78064589, 0.00070376, -27.37806459, -7.038e-05, -82.13419377, -0.00021113, -273.78064589, -0.00070376, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 32.25, 0.0, 8.3)
    ops.node(124006, 32.25, 0.0, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 26637972.97810646, 11099155.40754436, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 41.16641402, 0.00103744, 50.16886714, 0.01488793, 5.01688671, 0.06126169, -41.16641402, -0.00103744, -50.16886714, -0.01488793, -5.01688671, -0.06126169, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 41.16641402, 0.00103744, 50.16886714, 0.01488793, 5.01688671, 0.06126169, -41.16641402, -0.00103744, -50.16886714, -0.01488793, -5.01688671, -0.06126169, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 63.06630993, 0.02074885, 63.06630993, 0.06224654, 44.14641695, -1590.2939566, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 15.76657748, 7.228e-05, 47.29973244, 0.00021683, 157.66577481, 0.00072276, -15.76657748, -7.228e-05, -47.29973244, -0.00021683, -157.66577481, -0.00072276, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 63.06630993, 0.02074885, 63.06630993, 0.06224654, 44.14641695, -1590.2939566, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 15.76657748, 7.228e-05, 47.29973244, 0.00021683, 157.66577481, 0.00072276, -15.76657748, -7.228e-05, -47.29973244, -0.00021683, -157.66577481, -0.00072276, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 3.65, 8.3)
    ops.node(124007, 0.0, 3.65, 10.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 30165103.66561431, 12568793.19400596, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 67.08514734, 0.00111345, 80.88512397, 0.01313177, 8.0885124, 0.05742483, -67.08514734, -0.00111345, -80.88512397, -0.01313177, -8.0885124, -0.05742483, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 60.43300133, 0.00111345, 72.86457582, 0.01313177, 7.28645758, 0.05742483, -60.43300133, -0.00111345, -72.86457582, -0.01313177, -7.28645758, -0.05742483, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 55.26903136, 0.02226898, 55.26903136, 0.06680693, 38.68832195, -1051.5431395, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 13.81725784, 5.593e-05, 41.45177352, 0.0001678, 138.17257839, 0.00055934, -13.81725784, -5.593e-05, -41.45177352, -0.0001678, -138.17257839, -0.00055934, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 55.26903136, 0.02226898, 55.26903136, 0.06680693, 38.68832195, -1051.5431395, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 13.81725784, 5.593e-05, 41.45177352, 0.0001678, 138.17257839, 0.00055934, -13.81725784, -5.593e-05, -41.45177352, -0.0001678, -138.17257839, -0.00055934, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 7.3, 3.65, 8.3)
    ops.node(124008, 7.3, 3.65, 10.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.16, 26889488.3976437, 11203953.49901821, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 143.92224133, 0.00078635, 175.06038912, 0.00894645, 17.50603891, 0.03545108, -143.92224133, -0.00078635, -175.06038912, -0.00894645, -17.50603891, -0.03545108, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 143.92224133, 0.00078635, 175.06038912, 0.00894645, 17.50603891, 0.03545108, -143.92224133, -0.00078635, -175.06038912, -0.00894645, -17.50603891, -0.03545108, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 125.77058607, 0.01572707, 125.77058607, 0.04718121, 88.03941025, -1279.23723011, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 31.44264652, 5.578e-05, 94.32793955, 0.00016733, 314.42646518, 0.00055777, -31.44264652, -5.578e-05, -94.32793955, -0.00016733, -314.42646518, -0.00055777, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 125.77058607, 0.01572707, 125.77058607, 0.04718121, 88.03941025, -1279.23723011, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 31.44264652, 5.578e-05, 94.32793955, 0.00016733, 314.42646518, 0.00055777, -31.44264652, -5.578e-05, -94.32793955, -0.00016733, -314.42646518, -0.00055777, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 14.6, 3.65, 8.3)
    ops.node(124009, 14.6, 3.65, 10.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 23102799.87197462, 9626166.61332276, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 93.7518322, 0.0007466, 114.26557184, 0.01295626, 11.42655718, 0.04269443, -93.7518322, -0.0007466, -114.26557184, -0.01295626, -11.42655718, -0.04269443, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 87.45260507, 0.0007466, 106.58801745, 0.01295626, 10.65880174, 0.04269443, -87.45260507, -0.0007466, -106.58801745, -0.01295626, -10.65880174, -0.04269443, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 103.01406562, 0.01493195, 103.01406562, 0.04479585, 72.10984593, -1658.94733272, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 25.7535164, 6.945e-05, 77.26054921, 0.00020835, 257.53516404, 0.0006945, -25.7535164, -6.945e-05, -77.26054921, -0.00020835, -257.53516404, -0.0006945, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 103.01406562, 0.01493195, 103.01406562, 0.04479585, 72.10984593, -1658.94733272, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 25.7535164, 6.945e-05, 77.26054921, 0.00020835, 257.53516404, 0.0006945, -25.7535164, -6.945e-05, -77.26054921, -0.00020835, -257.53516404, -0.0006945, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 17.65, 3.65, 8.3)
    ops.node(124010, 17.65, 3.65, 10.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 25830910.97060874, 10762879.57108697, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 97.36263495, 0.0007956, 118.59508308, 0.00983842, 11.85950831, 0.04374633, -97.36263495, -0.0007956, -118.59508308, -0.00983842, -11.85950831, -0.04374633, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 91.22574507, 0.0007956, 111.11988516, 0.00983842, 11.11198852, 0.04374633, -91.22574507, -0.0007956, -111.11988516, -0.00983842, -11.11198852, -0.04374633, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 103.34596051, 0.01591204, 103.34596051, 0.04773613, 72.34217236, -1321.09307528, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 25.83649013, 6.232e-05, 77.50947038, 0.00018695, 258.36490127, 0.00062315, -25.83649013, -6.232e-05, -77.50947038, -0.00018695, -258.36490127, -0.00062315, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 103.34596051, 0.01591204, 103.34596051, 0.04773613, 72.34217236, -1321.09307528, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 25.83649013, 6.232e-05, 77.50947038, 0.00018695, 258.36490127, 0.00062315, -25.83649013, -6.232e-05, -77.50947038, -0.00018695, -258.36490127, -0.00062315, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 24.95, 3.65, 8.3)
    ops.node(124011, 24.95, 3.65, 10.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.16, 24006188.75395412, 10002578.64748088, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 139.07383923, 0.00074259, 169.45405972, 0.00819069, 16.94540597, 0.03166191, -139.07383923, -0.00074259, -169.45405972, -0.00819069, -16.94540597, -0.03166191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 139.07383923, 0.00074259, 169.45405972, 0.00819069, 16.94540597, 0.03166191, -139.07383923, -0.00074259, -169.45405972, -0.00819069, -16.94540597, -0.03166191, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 101.69896484, 0.01485185, 101.69896484, 0.04455554, 71.18927539, -1215.66892158, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 25.42474121, 5.052e-05, 76.27422363, 0.00015156, 254.24741211, 0.00050519, -25.42474121, -5.052e-05, -76.27422363, -0.00015156, -254.24741211, -0.00050519, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 101.69896484, 0.01485185, 101.69896484, 0.04455554, 71.18927539, -1215.66892158, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 25.42474121, 5.052e-05, 76.27422363, 0.00015156, 254.24741211, 0.00050519, -25.42474121, -5.052e-05, -76.27422363, -0.00015156, -254.24741211, -0.00050519, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 32.25, 3.65, 8.3)
    ops.node(124012, 32.25, 3.65, 10.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 34411675.39313839, 14338198.08047433, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 65.58061788, 0.00098048, 78.15408008, 0.01227025, 7.81540801, 0.06102863, -65.58061788, -0.00098048, -78.15408008, -0.01227025, -7.81540801, -0.06102863, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 58.73205147, 0.00098048, 69.99247038, 0.01227025, 6.99924704, 0.06102863, -58.73205147, -0.00098048, -69.99247038, -0.01227025, -6.99924704, -0.06102863, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 57.11642088, 0.01960957, 57.11642088, 0.05882872, 39.98149462, -967.3826015, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 14.27910522, 5.067e-05, 42.83731566, 0.00015201, 142.79105221, 0.0005067, -14.27910522, -5.067e-05, -42.83731566, -0.00015201, -142.79105221, -0.0005067, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 57.11642088, 0.01960957, 57.11642088, 0.05882872, 39.98149462, -967.3826015, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 14.27910522, 5.067e-05, 42.83731566, 0.00015201, 142.79105221, 0.0005067, -14.27910522, -5.067e-05, -42.83731566, -0.00015201, -142.79105221, -0.0005067, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 7.3, 8.3)
    ops.node(124013, 0.0, 7.3, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 32561254.49185663, 13567189.37160693, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 44.53347417, 0.00108141, 53.55363597, 0.01053483, 5.3553636, 0.06227434, -44.53347417, -0.00108141, -53.55363597, -0.01053483, -5.3553636, -0.06227434, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 44.53347417, 0.00108141, 53.55363597, 0.01053483, 5.3553636, 0.06227434, -44.53347417, -0.00108141, -53.55363597, -0.01053483, -5.3553636, -0.06227434, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 44.98551035, 0.02162823, 44.98551035, 0.0648847, 31.48985724, -1008.367462, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 11.24637759, 4.218e-05, 33.73913276, 0.00012653, 112.46377586, 0.00042176, -11.24637759, -4.218e-05, -33.73913276, -0.00012653, -112.46377586, -0.00042176, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 44.98551035, 0.02162823, 44.98551035, 0.0648847, 31.48985724, -1008.367462, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 11.24637759, 4.218e-05, 33.73913276, 0.00012653, 112.46377586, 0.00042176, -11.24637759, -4.218e-05, -33.73913276, -0.00012653, -112.46377586, -0.00042176, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 7.3, 7.3, 8.3)
    ops.node(124014, 7.3, 7.3, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1225, 29633539.74791497, 12347308.2282979, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 82.33505272, 0.0007548, 99.80775053, 0.00918581, 9.98077505, 0.05340534, -82.33505272, -0.0007548, -99.80775053, -0.00918581, -9.98077505, -0.05340534, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 71.33511614, 0.0007548, 86.47346713, 0.00918581, 8.64734671, 0.05340534, -71.33511614, -0.0007548, -86.47346713, -0.00918581, -8.64734671, -0.05340534, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 120.54600128, 0.01509591, 120.54600128, 0.04528774, 84.38220089, -1593.95322779, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 30.13650032, 6.336e-05, 90.40950096, 0.00019008, 301.3650032, 0.00063359, -30.13650032, -6.336e-05, -90.40950096, -0.00019008, -301.3650032, -0.00063359, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 120.54600128, 0.01509591, 120.54600128, 0.04528774, 84.38220089, -1593.95322779, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 30.13650032, 6.336e-05, 90.40950096, 0.00019008, 301.3650032, 0.00063359, -30.13650032, -6.336e-05, -90.40950096, -0.00019008, -301.3650032, -0.00063359, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 14.6, 7.3, 8.3)
    ops.node(124015, 14.6, 7.3, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 28114982.58111627, 11714576.07546511, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 28.97189553, 0.00100924, 35.15021601, 0.01355778, 3.5150216, 0.06555159, -28.97189553, -0.00100924, -35.15021601, -0.01355778, -3.5150216, -0.06555159, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 28.97189553, 0.00100924, 35.15021601, 0.01355778, 3.5150216, 0.06555159, -28.97189553, -0.00100924, -35.15021601, -0.01355778, -3.5150216, -0.06555159, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 76.36181906, 0.02018474, 76.36181906, 0.06055422, 53.45327334, -1463.31021907, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 19.09045476, 8.292e-05, 57.27136429, 0.00024875, 190.90454765, 0.00082916, -19.09045476, -8.292e-05, -57.27136429, -0.00024875, -190.90454765, -0.00082916, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 76.36181906, 0.02018474, 76.36181906, 0.06055422, 53.45327334, -1463.31021907, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 19.09045476, 8.292e-05, 57.27136429, 0.00024875, 190.90454765, 0.00082916, -19.09045476, -8.292e-05, -57.27136429, -0.00024875, -190.90454765, -0.00082916, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 17.65, 7.3, 8.3)
    ops.node(124016, 17.65, 7.3, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 29314702.52674033, 12214459.38614181, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 31.30403699, 0.00099299, 37.90039545, 0.01395989, 3.79003954, 0.06769069, -31.30403699, -0.00099299, -37.90039545, -0.01395989, -3.79003954, -0.06769069, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 31.30403699, 0.00099299, 37.90039545, 0.01395989, 3.79003954, 0.06769069, -31.30403699, -0.00099299, -37.90039545, -0.01395989, -3.79003954, -0.06769069, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 83.11544186, 0.01985988, 83.11544186, 0.05957965, 58.1808093, -1703.08393475, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 20.77886046, 8.656e-05, 62.33658139, 0.00025967, 207.78860464, 0.00086555, -20.77886046, -8.656e-05, -62.33658139, -0.00025967, -207.78860464, -0.00086555, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 83.11544186, 0.01985988, 83.11544186, 0.05957965, 58.1808093, -1703.08393475, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 20.77886046, 8.656e-05, 62.33658139, 0.00025967, 207.78860464, 0.00086555, -20.77886046, -8.656e-05, -62.33658139, -0.00025967, -207.78860464, -0.00086555, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 24.95, 7.3, 8.3)
    ops.node(124017, 24.95, 7.3, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.1225, 25202093.65485706, 10500872.35619044, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 81.6036308, 0.00074355, 99.60288916, 0.01142319, 9.96028892, 0.05096429, -81.6036308, -0.00074355, -99.60288916, -0.01142319, -9.96028892, -0.05096429, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 69.95022348, 0.00074355, 85.37909756, 0.01142319, 8.53790976, 0.05096429, -69.95022348, -0.00074355, -85.37909756, -0.01142319, -8.53790976, -0.05096429, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 112.86605315, 0.01487091, 112.86605315, 0.04461273, 79.00623721, -1953.25661441, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 28.21651329, 6.975e-05, 84.64953986, 0.00020926, 282.16513288, 0.00069754, -28.21651329, -6.975e-05, -84.64953986, -0.00020926, -282.16513288, -0.00069754, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 112.86605315, 0.01487091, 112.86605315, 0.04461273, 79.00623721, -1953.25661441, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 28.21651329, 6.975e-05, 84.64953986, 0.00020926, 282.16513288, 0.00069754, -28.21651329, -6.975e-05, -84.64953986, -0.00020926, -282.16513288, -0.00069754, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 32.25, 7.3, 8.3)
    ops.node(124018, 32.25, 7.3, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 26155674.19322466, 10898197.58051028, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 41.90004758, 0.00098996, 51.09264297, 0.01122434, 5.1092643, 0.0569492, -41.90004758, -0.00098996, -51.09264297, -0.01122434, -5.1092643, -0.0569492, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 41.90004758, 0.00098996, 51.09264297, 0.01122434, 5.1092643, 0.0569492, -41.90004758, -0.00098996, -51.09264297, -0.01122434, -5.1092643, -0.0569492, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 33.14029836, 0.01979927, 33.14029836, 0.05939782, 23.19820885, -922.3946672, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 8.28507459, 3.868e-05, 24.85522377, 0.00011604, 82.85074591, 0.0003868, -8.28507459, -3.868e-05, -24.85522377, -0.00011604, -82.85074591, -0.0003868, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 33.14029836, 0.01979927, 33.14029836, 0.05939782, 23.19820885, -922.3946672, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 8.28507459, 3.868e-05, 24.85522377, 0.00011604, 82.85074591, 0.0003868, -8.28507459, -3.868e-05, -24.85522377, -0.00011604, -82.85074591, -0.0003868, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 14.6, 0.0, 0.0)
    ops.node(124019, 14.6, 0.0, 1.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 170003, 124019, 0.1225, 27619181.81829989, 11507992.42429162, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 170.37278646, 0.00062402, 202.28949243, 0.00708723, 20.22894924, 0.027421, -170.37278646, -0.00062402, -202.28949243, -0.00708723, -20.22894924, -0.027421, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 177.25011762, 0.00062402, 210.45518519, 0.00708723, 21.04551852, 0.027421, -177.25011762, -0.00062402, -210.45518519, -0.00708723, -21.04551852, -0.027421, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 223.2785532, 0.01248041, 223.2785532, 0.03744122, 156.29498724, -4217.26474038, 0.05, 2, 0, 70003, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 55.8196383, 6.296e-05, 167.4589149, 0.00018887, 558.196383, 0.00062958, -55.8196383, -6.296e-05, -167.4589149, -0.00018887, -558.196383, -0.00062958, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 223.2785532, 0.01248041, 223.2785532, 0.03744122, 156.29498724, -4217.26474038, 0.05, 2, 0, 70003, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 55.8196383, 6.296e-05, 167.4589149, 0.00018887, 558.196383, 0.00062958, -55.8196383, -6.296e-05, -167.4589149, -0.00018887, -558.196383, -0.00062958, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 14.6, 0.0, 1.525)
    ops.node(121003, 14.6, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 121003, 0.1225, 26575855.65737681, 11073273.19057367, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 166.33619544, 0.0006712, 197.52032505, 0.00847011, 19.75203251, 0.02745346, -166.33619544, -0.0006712, -197.52032505, -0.00847011, -19.75203251, -0.02745346, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 144.71170677, 0.0006712, 171.8417527, 0.00847011, 17.18417527, 0.02745346, -144.71170677, -0.0006712, -171.8417527, -0.00847011, -17.18417527, -0.02745346, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 217.7585894, 0.01342409, 217.7585894, 0.04027227, 152.43101258, -4348.40160473, 0.05, 2, 0, 74019, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 54.43964735, 6.381e-05, 163.31894205, 0.00019144, 544.39647351, 0.00063812, -54.43964735, -6.381e-05, -163.31894205, -0.00019144, -544.39647351, -0.00063812, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 217.7585894, 0.01342409, 217.7585894, 0.04027227, 152.43101258, -4348.40160473, 0.05, 2, 0, 74019, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 54.43964735, 6.381e-05, 163.31894205, 0.00019144, 544.39647351, 0.00063812, -54.43964735, -6.381e-05, -163.31894205, -0.00019144, -544.39647351, -0.00063812, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 17.65, 0.0, 0.0)
    ops.node(124020, 17.65, 0.0, 1.125)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 170004, 124020, 0.1225, 23597312.5093995, 9832213.54558312, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 100.65093494, 0.00042353, 117.91870096, 0.00518411, 11.7918701, 0.01586725, -100.65093494, -0.00042353, -117.91870096, -0.00518411, -11.7918701, -0.01586725, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 103.20685931, 0.00042353, 120.91312203, 0.00518411, 12.0913122, 0.01586725, -103.20685931, -0.00042353, -120.91312203, -0.00518411, -12.0913122, -0.01586725, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 195.0865738, 0.00847055, 195.0865738, 0.02541166, 136.56060166, -4172.01425856, 0.05, 2, 0, 70004, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 48.77164345, 6.438e-05, 146.31493035, 0.00019315, 487.7164345, 0.00064384, -48.77164345, -6.438e-05, -146.31493035, -0.00019315, -487.7164345, -0.00064384, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 195.0865738, 0.00847055, 195.0865738, 0.02541166, 136.56060166, -4172.01425856, 0.05, 2, 0, 70004, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 48.77164345, 6.438e-05, 146.31493035, 0.00019315, 487.7164345, 0.00064384, -48.77164345, -6.438e-05, -146.31493035, -0.00019315, -487.7164345, -0.00064384, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 17.65, 0.0, 1.525)
    ops.node(121004, 17.65, 0.0, 2.3)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 121004, 0.1225, 33255265.40187414, 13856360.58411422, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 182.34969864, 0.00063554, 216.10595265, 0.00819305, 21.61059527, 0.04035881, -182.34969864, -0.00063554, -216.10595265, -0.00819305, -21.61059527, -0.04035881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 154.96877846, 0.00063554, 183.65632491, 0.00819305, 18.36563249, 0.04035881, -154.96877846, -0.00063554, -183.65632491, -0.00819305, -18.36563249, -0.04035881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 262.01990066, 0.01271074, 262.01990066, 0.03813221, 183.41393046, -4206.86497626, 0.05, 2, 0, 74020, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 65.50497516, 6.136e-05, 196.51492549, 0.00018408, 655.04975164, 0.0006136, -65.50497516, -6.136e-05, -196.51492549, -0.00018408, -655.04975164, -0.0006136, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 262.01990066, 0.01271074, 262.01990066, 0.03813221, 183.41393046, -4206.86497626, 0.05, 2, 0, 74020, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 65.50497516, 6.136e-05, 196.51492549, 0.00018408, 655.04975164, 0.0006136, -65.50497516, -6.136e-05, -196.51492549, -0.00018408, -655.04975164, -0.0006136, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 14.6, 0.0, 3.0)
    ops.node(124021, 14.6, 0.0, 3.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 171003, 124021, 0.1225, 27107208.33806206, 11294670.14085919, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 126.34825699, 0.00060632, 151.2282717, 0.00930306, 15.12282717, 0.03422106, -126.34825699, -0.00060632, -151.2282717, -0.00930306, -15.12282717, -0.03422106, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 114.12130705, 0.00060632, 136.59363762, 0.00930306, 13.65936376, 0.03422106, -114.12130705, -0.00060632, -136.59363762, -0.00930306, -13.65936376, -0.03422106, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 216.29044049, 0.01212645, 216.29044049, 0.03637934, 151.40330835, -4432.34831709, 0.05, 2, 0, 71003, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 54.07261012, 6.214e-05, 162.21783037, 0.00018642, 540.72610124, 0.00062139, -54.07261012, -6.214e-05, -162.21783037, -0.00018642, -540.72610124, -0.00062139, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 216.29044049, 0.01212645, 216.29044049, 0.03637934, 151.40330835, -4432.34831709, 0.05, 2, 0, 71003, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 54.07261012, 6.214e-05, 162.21783037, 0.00018642, 540.72610124, 0.00062139, -54.07261012, -6.214e-05, -162.21783037, -0.00018642, -540.72610124, -0.00062139, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 14.6, 0.0, 4.175)
    ops.node(122003, 14.6, 0.0, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 122003, 0.1225, 27494344.3588389, 11455976.81618288, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 130.12050313, 0.00061826, 156.04597629, 0.00755461, 15.60459763, 0.03468757, -130.12050313, -0.00061826, -156.04597629, -0.00755461, -15.60459763, -0.03468757, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 115.84541609, 0.00061826, 138.92669194, 0.00755461, 13.89266919, 0.03468757, -115.84541609, -0.00061826, -138.92669194, -0.00755461, -13.89266919, -0.03468757, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 201.95650251, 0.01236524, 201.95650251, 0.03709571, 141.36955176, -3636.06826954, 0.05, 2, 0, 74021, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 50.48912563, 5.72e-05, 151.46737688, 0.00017161, 504.89125628, 0.00057204, -50.48912563, -5.72e-05, -151.46737688, -0.00017161, -504.89125628, -0.00057204, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 201.95650251, 0.01236524, 201.95650251, 0.03709571, 141.36955176, -3636.06826954, 0.05, 2, 0, 74021, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 50.48912563, 5.72e-05, 151.46737688, 0.00017161, 504.89125628, 0.00057204, -50.48912563, -5.72e-05, -151.46737688, -0.00017161, -504.89125628, -0.00057204, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 17.65, 0.0, 3.0)
    ops.node(124022, 17.65, 0.0, 3.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 171004, 124022, 0.1225, 26360696.51085193, 10983623.5461883, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 125.61217213, 0.00061456, 150.24094636, 0.00903704, 15.02409464, 0.0322427, -125.61217213, -0.00061456, -150.24094636, -0.00903704, -15.02409464, -0.0322427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 113.69499273, 0.00061456, 135.98716601, 0.00903704, 13.5987166, 0.0322427, -113.69499273, -0.00061456, -135.98716601, -0.00903704, -13.5987166, -0.0322427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 206.70269431, 0.01229114, 206.70269431, 0.03687341, 144.69188602, -4170.92567675, 0.05, 2, 0, 71004, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 51.67567358, 6.107e-05, 155.02702073, 0.0001832, 516.75673578, 0.00061066, -51.67567358, -6.107e-05, -155.02702073, -0.0001832, -516.75673578, -0.00061066, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 206.70269431, 0.01229114, 206.70269431, 0.03687341, 144.69188602, -4170.92567675, 0.05, 2, 0, 71004, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 51.67567358, 6.107e-05, 155.02702073, 0.0001832, 516.75673578, 0.00061066, -51.67567358, -6.107e-05, -155.02702073, -0.0001832, -516.75673578, -0.00061066, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 17.65, 0.0, 4.175)
    ops.node(122004, 17.65, 0.0, 4.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 122004, 0.1225, 25922359.48376984, 10800983.11823743, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 120.84195729, 0.00062287, 144.75138257, 0.00887076, 14.47513826, 0.03246438, -120.84195729, -0.00062287, -144.75138257, -0.00887076, -14.47513826, -0.03246438, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 109.3704537, 0.00062287, 131.01016187, 0.00887076, 13.10101619, 0.03246438, -109.3704537, -0.00062287, -131.01016187, -0.00887076, -13.10101619, -0.03246438, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 195.39009591, 0.01245749, 195.39009591, 0.03737247, 136.77306714, -3822.51898852, 0.05, 2, 0, 74022, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 48.84752398, 5.87e-05, 146.54257193, 0.0001761, 488.47523978, 0.000587, -48.84752398, -5.87e-05, -146.54257193, -0.0001761, -488.47523978, -0.000587, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 195.39009591, 0.01245749, 195.39009591, 0.03737247, 136.77306714, -3822.51898852, 0.05, 2, 0, 74022, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 48.84752398, 5.87e-05, 146.54257193, 0.0001761, 488.47523978, 0.000587, -48.84752398, -5.87e-05, -146.54257193, -0.0001761, -488.47523978, -0.000587, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 14.6, 0.0, 5.65)
    ops.node(124023, 14.6, 0.0, 6.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 172003, 124023, 0.0625, 26768042.52338123, 11153351.05140885, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 62.87334306, 0.00076356, 74.74294465, 0.00952497, 7.47429447, 0.03525693, -62.87334306, -0.00076356, -74.74294465, -0.00952497, -7.47429447, -0.03525693, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 58.36225278, 0.00076356, 69.38022407, 0.00952497, 6.93802241, 0.03525693, -58.36225278, -0.00076356, -69.38022407, -0.00952497, -6.93802241, -0.03525693, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 100.2680539, 0.01527118, 100.2680539, 0.04581354, 70.18763773, -2919.18816642, 0.05, 2, 0, 72003, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 25.06701347, 5.718e-05, 75.20104042, 0.00017153, 250.67013474, 0.00057176, -25.06701347, -5.718e-05, -75.20104042, -0.00017153, -250.67013474, -0.00057176, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 100.2680539, 0.01527118, 100.2680539, 0.04581354, 70.18763773, -2919.18816642, 0.05, 2, 0, 72003, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 25.06701347, 5.718e-05, 75.20104042, 0.00017153, 250.67013474, 0.00057176, -25.06701347, -5.718e-05, -75.20104042, -0.00017153, -250.67013474, -0.00057176, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 14.6, 0.0, 6.825)
    ops.node(123003, 14.6, 0.0, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 123003, 0.0625, 29954296.43260404, 12480956.84691835, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 59.91108406, 0.00077136, 71.54598458, 0.0091607, 7.15459846, 0.04684098, -59.91108406, -0.00077136, -71.54598458, -0.0091607, -7.15459846, -0.04684098, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 55.80859888, 0.00077136, 66.64678527, 0.0091607, 6.66467853, 0.04684098, -55.80859888, -0.00077136, -66.64678527, -0.0091607, -6.66467853, -0.04684098, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 93.01285188, 0.01542711, 93.01285188, 0.04628134, 65.10899631, -2507.49825867, 0.05, 2, 0, 74023, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 23.25321297, 4.74e-05, 69.75963891, 0.00014219, 232.53212969, 0.00047397, -23.25321297, -4.74e-05, -69.75963891, -0.00014219, -232.53212969, -0.00047397, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 93.01285188, 0.01542711, 93.01285188, 0.04628134, 65.10899631, -2507.49825867, 0.05, 2, 0, 74023, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 23.25321297, 4.74e-05, 69.75963891, 0.00014219, 232.53212969, 0.00047397, -23.25321297, -4.74e-05, -69.75963891, -0.00014219, -232.53212969, -0.00047397, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 17.65, 0.0, 5.65)
    ops.node(124024, 17.65, 0.0, 6.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 172004, 124024, 0.0625, 29080830.63540678, 12117012.76475282, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 64.02860707, 0.0008308, 76.26653351, 0.00891021, 7.62665335, 0.04132161, -64.02860707, -0.0008308, -76.26653351, -0.00891021, -7.62665335, -0.04132161, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 60.0737648, 0.0008308, 71.55579367, 0.00891021, 7.15557937, 0.04132161, -60.0737648, -0.0008308, -71.55579367, -0.00891021, -7.15557937, -0.04132161, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 102.96304356, 0.01661591, 102.96304356, 0.04984772, 72.07413049, -2875.94917067, 0.05, 2, 0, 72004, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 25.74076089, 5.404e-05, 77.22228267, 0.00016213, 257.40760889, 0.00054043, -25.74076089, -5.404e-05, -77.22228267, -0.00016213, -257.40760889, -0.00054043, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 102.96304356, 0.01661591, 102.96304356, 0.04984772, 72.07413049, -2875.94917067, 0.05, 2, 0, 72004, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 25.74076089, 5.404e-05, 77.22228267, 0.00016213, 257.40760889, 0.00054043, -25.74076089, -5.404e-05, -77.22228267, -0.00016213, -257.40760889, -0.00054043, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 17.65, 0.0, 6.825)
    ops.node(123004, 17.65, 0.0, 7.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 123004, 0.0625, 26719613.75397731, 11133172.39749055, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 58.06424639, 0.00076524, 69.30020435, 0.00838206, 6.93002044, 0.03724851, -58.06424639, -0.00076524, -69.30020435, -0.00838206, -6.93002044, -0.03724851, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 54.00854393, 0.00076524, 64.45968671, 0.00838206, 6.44596867, 0.03724851, -54.00854393, -0.00076524, -64.45968671, -0.00838206, -6.44596867, -0.03724851, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 81.53509642, 0.01530475, 81.53509642, 0.04591424, 57.07456749, -2473.80118769, 0.05, 2, 0, 74024, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 20.3837741, 4.658e-05, 61.15132231, 0.00013973, 203.83774105, 0.00046578, -20.3837741, -4.658e-05, -61.15132231, -0.00013973, -203.83774105, -0.00046578, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 81.53509642, 0.01530475, 81.53509642, 0.04591424, 57.07456749, -2473.80118769, 0.05, 2, 0, 74024, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 20.3837741, 4.658e-05, 61.15132231, 0.00013973, 203.83774105, 0.00046578, -20.3837741, -4.658e-05, -61.15132231, -0.00013973, -203.83774105, -0.00046578, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4059, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 14.6, 0.0, 8.3)
    ops.node(124025, 14.6, 0.0, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4061, 173003, 124025, 0.0625, 22483132.19678178, 9367971.74865908, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24061, 32.35818265, 0.00071196, 39.1867533, 0.01248548, 3.91867533, 0.04771908, -32.35818265, -0.00071196, -39.1867533, -0.01248548, -3.91867533, -0.04771908, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14061, 32.35818265, 0.00071196, 39.1867533, 0.01248548, 3.91867533, 0.04771908, -32.35818265, -0.00071196, -39.1867533, -0.01248548, -3.91867533, -0.04771908, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24061, 4061, 0.0, 82.35243782, 0.01423922, 82.35243782, 0.04271766, 57.64670647, -3542.77839627, 0.05, 2, 0, 73003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44061, 20.58810945, 5.591e-05, 61.76432836, 0.00016773, 205.88109454, 0.0005591, -20.58810945, -5.591e-05, -61.76432836, -0.00016773, -205.88109454, -0.0005591, 0.4, 0.3, 0.003, 0.0, 0.0, 24061, 2)
    ops.limitCurve('ThreePoint', 14061, 4061, 0.0, 82.35243782, 0.01423922, 82.35243782, 0.04271766, 57.64670647, -3542.77839627, 0.05, 2, 0, 73003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34061, 20.58810945, 5.591e-05, 61.76432836, 0.00016773, 205.88109454, 0.0005591, -20.58810945, -5.591e-05, -61.76432836, -0.00016773, -205.88109454, -0.0005591, 0.4, 0.3, 0.003, 0.0, 0.0, 14061, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4061, 99999, 'P', 44061, 'Vy', 34061, 'Vz', 24061, 'My', 14061, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4061, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4061, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 14.6, 0.0, 9.475)
    ops.node(124003, 14.6, 0.0, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 174025, 124003, 0.0625, 29606464.11343613, 12336026.71393172, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 28.40836853, 0.00062873, 34.42297622, 0.01238189, 3.44229762, 0.06882162, -28.40836853, -0.00062873, -34.42297622, -0.01238189, -3.44229762, -0.06882162, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 28.40836853, 0.00062873, 34.42297622, 0.01238189, 3.44229762, 0.06882162, -28.40836853, -0.00062873, -34.42297622, -0.01238189, -3.44229762, -0.06882162, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 84.66502538, 0.01257462, 84.66502538, 0.03772385, 59.26551777, -3067.69123628, 0.05, 2, 0, 74025, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 21.16625635, 4.365e-05, 63.49876904, 0.00013095, 211.66256345, 0.0004365, -21.16625635, -4.365e-05, -63.49876904, -0.00013095, -211.66256345, -0.0004365, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 84.66502538, 0.01257462, 84.66502538, 0.03772385, 59.26551777, -3067.69123628, 0.05, 2, 0, 74025, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 21.16625635, 4.365e-05, 63.49876904, 0.00013095, 211.66256345, 0.0004365, -21.16625635, -4.365e-05, -63.49876904, -0.00013095, -211.66256345, -0.0004365, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 17.65, 0.0, 8.3)
    ops.node(124026, 17.65, 0.0, 9.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 173004, 124026, 0.0625, 25991204.53560818, 10829668.55650341, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 32.19953051, 0.00072781, 39.07079907, 0.01336601, 3.90707991, 0.05842628, -32.19953051, -0.00072781, -39.07079907, -0.01336601, -3.90707991, -0.05842628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 32.19953051, 0.00072781, 39.07079907, 0.01336601, 3.90707991, 0.05842628, -32.19953051, -0.00072781, -39.07079907, -0.01336601, -3.90707991, -0.05842628, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 89.22040906, 0.01455618, 89.22040906, 0.04366853, 62.45428634, -3507.19613901, 0.05, 2, 0, 73004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 22.30510227, 5.24e-05, 66.9153068, 0.00015719, 223.05102266, 0.00052397, -22.30510227, -5.24e-05, -66.9153068, -0.00015719, -223.05102266, -0.00052397, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 89.22040906, 0.01455618, 89.22040906, 0.04366853, 62.45428634, -3507.19613901, 0.05, 2, 0, 73004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 22.30510227, 5.24e-05, 66.9153068, 0.00015719, 223.05102266, 0.00052397, -22.30510227, -5.24e-05, -66.9153068, -0.00015719, -223.05102266, -0.00052397, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 17.65, 0.0, 9.475)
    ops.node(124004, 17.65, 0.0, 10.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174026, 124004, 0.0625, 27990546.91930006, 11662727.88304169, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 29.03871361, 0.00063459, 35.29786119, 0.01291806, 3.52978612, 0.06741026, -29.03871361, -0.00063459, -35.29786119, -0.01291806, -3.52978612, -0.06741026, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 29.03871361, 0.00063459, 35.29786119, 0.01291806, 3.52978612, 0.06741026, -29.03871361, -0.00063459, -35.29786119, -0.01291806, -3.52978612, -0.06741026, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 77.42949379, 0.01269175, 77.42949379, 0.03807524, 54.20064565, -2628.71008654, 0.05, 2, 0, 74026, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 19.35737345, 4.222e-05, 58.07212034, 0.00012667, 193.57373447, 0.00042224, -19.35737345, -4.222e-05, -58.07212034, -0.00012667, -193.57373447, -0.00042224, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 77.42949379, 0.01269175, 77.42949379, 0.03807524, 54.20064565, -2628.71008654, 0.05, 2, 0, 74026, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 19.35737345, 4.222e-05, 58.07212034, 0.00012667, 193.57373447, 0.00042224, -19.35737345, -4.222e-05, -58.07212034, -0.00012667, -193.57373447, -0.00042224, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4064, '-orient', 0, 0, 1, 0, 1, 0)
