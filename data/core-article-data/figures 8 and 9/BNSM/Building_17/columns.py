import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 8.5, 0.0, 0.0)
    ops.node(121003, 8.5, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.105, 27740401.98307873, 11558500.8262828, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 114.16596388, 0.00076178, 133.77840645, 0.00661855, 13.37784065, 0.02046795, -114.16596388, -0.00076178, -133.77840645, -0.00661855, -13.37784065, -0.02046795, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 128.10537311, 0.00069949, 150.11245112, 0.00684916, 15.01124511, 0.0223982, -128.10537311, -0.00069949, -150.11245112, -0.00684916, -15.01124511, -0.0223982, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 147.09224541, 0.01523563, 147.09224541, 0.04570689, 102.96457178, -2235.29786786, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 36.77306135, 9.999e-05, 110.31918405, 0.00029997, 367.73061351, 0.00099989, -36.77306135, -9.999e-05, -110.31918405, -0.00029997, -367.73061351, -0.00099989, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 154.27497234, 0.01398989, 154.27497234, 0.04196968, 107.99248064, -2391.0328247, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 38.56874308, 0.00010487, 115.70622925, 0.00031462, 385.68743084, 0.00104872, -38.56874308, -0.00010487, -115.70622925, -0.00031462, -385.68743084, -0.00104872, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.85, 0.0, 0.0)
    ops.node(121004, 13.85, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.0625, 31407283.37034314, 13086368.07097631, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 75.90114579, 0.00130789, 89.37641004, 0.0103118, 8.937641, 0.03866458, -75.90114579, -0.00130789, -89.37641004, -0.0103118, -8.937641, -0.03866458, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 72.33245942, 0.00130789, 85.17414968, 0.0103118, 8.51741497, 0.03866458, -72.33245942, -0.00130789, -85.17414968, -0.0103118, -8.51741497, -0.03866458, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 112.88155814, 0.02615789, 112.88155814, 0.07847368, 79.0170907, -1713.54454539, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 28.22038953, 0.00011386, 84.6611686, 0.00034159, 282.20389534, 0.00113862, -28.22038953, -0.00011386, -84.6611686, -0.00034159, -282.20389534, -0.00113862, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 112.88155814, 0.02615789, 112.88155814, 0.07847368, 79.0170907, -1713.54454539, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 28.22038953, 0.00011386, 84.6611686, 0.00034159, 282.20389534, 0.00113862, -28.22038953, -0.00011386, -84.6611686, -0.00034159, -282.20389534, -0.00113862, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.2, 0.0)
    ops.node(121005, 0.0, 4.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.0625, 30869879.35122587, 12862449.72967745, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 64.01188216, 0.00119965, 75.51824162, 0.00963236, 7.55182416, 0.0381149, -64.01188216, -0.00119965, -75.51824162, -0.00963236, -7.55182416, -0.0381149, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 64.01188216, 0.00119965, 75.51824162, 0.00963236, 7.55182416, 0.0381149, -64.01188216, -0.00119965, -75.51824162, -0.00963236, -7.55182416, -0.0381149, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 106.32805505, 0.0239931, 106.32805505, 0.0719793, 74.42963854, -1582.25533682, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 26.58201376, 0.00010912, 79.74604129, 0.00032736, 265.82013763, 0.00109118, -26.58201376, -0.00010912, -79.74604129, -0.00032736, -265.82013763, -0.00109118, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 106.32805505, 0.0239931, 106.32805505, 0.0719793, 74.42963854, -1582.25533682, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 26.58201376, 0.00010912, 79.74604129, 0.00032736, 265.82013763, 0.00109118, -26.58201376, -0.00010912, -79.74604129, -0.00032736, -265.82013763, -0.00109118, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 3.15, 4.2, 0.0)
    ops.node(121006, 3.15, 4.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.135, 30799367.16867132, 12833069.65361305, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 281.99213228, 0.0007647, 333.72121277, 0.01074277, 33.37212128, 0.03423342, -281.99213228, -0.0007647, -333.72121277, -0.01074277, -33.37212128, -0.03423342, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 217.79263122, 0.00101937, 257.74485421, 0.00989451, 25.77448542, 0.0276865, -217.79263122, -0.00101937, -257.74485421, -0.00989451, -25.77448542, -0.0276865, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 213.49630226, 0.01529407, 213.49630226, 0.04588222, 149.44741158, -2872.2518432, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 53.37407557, 0.00010167, 160.1222267, 0.000305, 533.74075566, 0.00101667, -53.37407557, -0.00010167, -160.1222267, -0.000305, -533.74075566, -0.00101667, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 184.26150694, 0.02038734, 184.26150694, 0.06116201, 128.98305486, -2365.48124703, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 46.06537674, 8.775e-05, 138.19613021, 0.00026324, 460.65376736, 0.00087745, -46.06537674, -8.775e-05, -138.19613021, -0.00026324, -460.65376736, -0.00087745, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 8.5, 4.2, 0.0)
    ops.node(121007, 8.5, 4.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.24, 30362611.69571528, 12651088.20654804, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 577.26856967, 0.00065697, 688.32621421, 0.01416451, 68.83262142, 0.04498746, -577.26856967, -0.00065697, -688.32621421, -0.01416451, -68.83262142, -0.04498746, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 503.89216456, 0.00081044, 600.83331091, 0.01277195, 60.08333109, 0.03587399, -503.89216456, -0.00081044, -600.83331091, -0.01277195, -60.08333109, -0.03587399, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 407.44803601, 0.01313936, 407.44803601, 0.03941808, 285.21362521, -4071.81347055, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 101.862009, 0.00011071, 305.58602701, 0.00033213, 1018.62009003, 0.0011071, -101.862009, -0.00011071, -305.58602701, -0.00033213, -1018.62009003, -0.0011071, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 286.69237044, 0.01620888, 286.69237044, 0.04862665, 200.68465931, -3270.85038834, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 71.67309261, 7.79e-05, 215.01927783, 0.0002337, 716.7309261, 0.00077899, -71.67309261, -7.79e-05, -215.01927783, -0.0002337, -716.7309261, -0.00077899, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 13.85, 4.2, 0.0)
    ops.node(121008, 13.85, 4.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.0875, 29667241.18818079, 12361350.49507533, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 181.38869852, 0.00096797, 212.32179766, 0.00913105, 21.23217977, 0.02936927, -181.38869852, -0.00096797, -212.32179766, -0.00913105, -21.23217977, -0.02936927, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 126.52238168, 0.00128255, 148.0988603, 0.00860284, 14.80988603, 0.02423113, -126.52238168, -0.00128255, -148.0988603, -0.00860284, -14.80988603, -0.02423113, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 154.76287818, 0.01935948, 154.76287818, 0.05807844, 108.33401473, -2481.22995561, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 38.69071955, 0.00011804, 116.07215864, 0.00035413, 386.90719546, 0.00118045, -38.69071955, -0.00011804, -116.07215864, -0.00035413, -386.90719546, -0.00118045, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 138.40830135, 0.02565103, 138.40830135, 0.0769531, 96.88581094, -2118.09617289, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 34.60207534, 0.00010557, 103.80622601, 0.00031671, 346.02075337, 0.0010557, -34.60207534, -0.00010557, -103.80622601, -0.00031671, -346.02075337, -0.0010557, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.4, 0.0)
    ops.node(121009, 0.0, 8.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.0625, 31745954.51912984, 13227481.04963744, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 66.20848553, 0.001257, 77.97811896, 0.01007973, 7.7978119, 0.03956971, -66.20848553, -0.001257, -77.97811896, -0.01007973, -7.7978119, -0.03956971, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 66.20848553, 0.001257, 77.97811896, 0.01007973, 7.7978119, 0.03956971, -66.20848553, -0.001257, -77.97811896, -0.01007973, -7.7978119, -0.03956971, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 110.10451525, 0.02514005, 110.10451525, 0.07542015, 77.07316067, -1626.86988721, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 27.52612881, 0.00010988, 82.57838643, 0.00032963, 275.26128811, 0.00109876, -27.52612881, -0.00010988, -82.57838643, -0.00032963, -275.26128811, -0.00109876, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 110.10451525, 0.02514005, 110.10451525, 0.07542015, 77.07316067, -1626.86988721, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 27.52612881, 0.00010988, 82.57838643, 0.00032963, 275.26128811, 0.00109876, -27.52612881, -0.00010988, -82.57838643, -0.00032963, -275.26128811, -0.00109876, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 3.15, 8.4, 0.0)
    ops.node(121010, 3.15, 8.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.135, 30205609.85479016, 12585670.77282923, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 284.87386927, 0.00080694, 337.46442796, 0.00898112, 33.7464428, 0.03189637, -284.87386927, -0.00080694, -337.46442796, -0.00898112, -33.7464428, -0.03189637, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 218.18916334, 0.00109489, 258.46905995, 0.00836554, 25.84690599, 0.02572172, -218.18916334, -0.00109489, -258.46905995, -0.00836554, -25.84690599, -0.02572172, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 195.43707882, 0.0161387, 195.43707882, 0.0484161, 136.80595517, -2523.11764776, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 48.85926971, 9.49e-05, 146.57780912, 0.00028469, 488.59269705, 0.00094897, -48.85926971, -9.49e-05, -146.57780912, -0.00028469, -488.59269705, -0.00094897, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 169.72642573, 0.02189773, 169.72642573, 0.0656932, 118.80849801, -2132.81812074, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 42.43160643, 8.241e-05, 127.2948193, 0.00024724, 424.31606433, 0.00082413, -42.43160643, -8.241e-05, -127.2948193, -0.00024724, -424.31606433, -0.00082413, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.5, 8.4, 0.0)
    ops.node(121011, 8.5, 8.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.24, 30030246.22341901, 12512602.59309125, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 599.72057006, 0.00065417, 715.28532703, 0.01630614, 71.5285327, 0.04646387, -599.72057006, -0.00065417, -715.28532703, -0.01630614, -71.5285327, -0.04646387, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 497.4044882, 0.00080892, 593.25317452, 0.01466941, 59.32531745, 0.03727285, -497.4044882, -0.00080892, -593.25317452, -0.01466941, -59.32531745, -0.03727285, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 407.22541587, 0.01308349, 407.22541587, 0.03925048, 285.05779111, -4159.08864526, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 101.80635397, 0.00011187, 305.4190619, 0.00033562, 1018.06353968, 0.00111874, -101.80635397, -0.00011187, -305.4190619, -0.00033562, -1018.06353968, -0.00111874, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 286.35824951, 0.01617839, 286.35824951, 0.04853516, 200.45077466, -3322.92734767, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 71.58956238, 7.867e-05, 214.76868714, 0.00023601, 715.89562379, 0.00078669, -71.58956238, -7.867e-05, -214.76868714, -0.00023601, -715.89562379, -0.00078669, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 13.85, 8.4, 0.0)
    ops.node(121012, 13.85, 8.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.0875, 31755276.53861723, 13231365.22442385, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 174.5502694, 0.00100524, 204.65227772, 0.00974465, 20.46522777, 0.03554133, -174.5502694, -0.00100524, -204.65227772, -0.00974465, -20.46522777, -0.03554133, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 121.63674573, 0.00139056, 142.61357003, 0.00922768, 14.261357, 0.0291483, -121.63674573, -0.00139056, -142.61357003, -0.00922768, -14.261357, -0.0291483, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 160.52905001, 0.02010483, 160.52905001, 0.06031448, 112.37033501, -2452.15797805, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 40.1322625, 0.00011439, 120.39678751, 0.00034318, 401.32262503, 0.00114392, -40.1322625, -0.00011439, -120.39678751, -0.00034318, -401.32262503, -0.00114392, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 144.53539766, 0.02781121, 144.53539766, 0.08343364, 101.17477836, -2098.89728251, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 36.13384941, 0.00010299, 108.40154824, 0.00030898, 361.33849414, 0.00102995, -36.13384941, -0.00010299, -108.40154824, -0.00030898, -361.33849414, -0.00102995, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 12.6, 0.0)
    ops.node(121013, 0.0, 12.6, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0625, 31310018.02162411, 13045840.84234338, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 66.98279503, 0.00120766, 78.90152692, 0.010066, 7.89015269, 0.03843736, -66.98279503, -0.00120766, -78.90152692, -0.010066, -7.89015269, -0.03843736, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 66.98279503, 0.00120766, 78.90152692, 0.010066, 7.89015269, 0.03843736, -66.98279503, -0.00120766, -78.90152692, -0.010066, -7.89015269, -0.03843736, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 111.12805204, 0.02415324, 111.12805204, 0.07245971, 77.78963643, -1676.00129253, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 27.78201301, 0.00011244, 83.34603903, 0.00033732, 277.8201301, 0.00112441, -27.78201301, -0.00011244, -83.34603903, -0.00033732, -277.8201301, -0.00112441, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 111.12805204, 0.02415324, 111.12805204, 0.07245971, 77.78963643, -1676.00129253, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 27.78201301, 0.00011244, 83.34603903, 0.00033732, 277.8201301, 0.00112441, -27.78201301, -0.00011244, -83.34603903, -0.00033732, -277.8201301, -0.00112441, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 3.15, 12.6, 0.0)
    ops.node(121014, 3.15, 12.6, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.135, 29173225.20600023, 12155510.50250009, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 277.61162402, 0.00076679, 328.76288494, 0.01047088, 32.87628849, 0.03125825, -277.61162402, -0.00076679, -328.76288494, -0.01047088, -32.87628849, -0.03125825, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 216.21366416, 0.00101901, 256.05205923, 0.00965047, 25.60520592, 0.02539497, -216.21366416, -0.00101901, -256.05205923, -0.00965047, -25.60520592, -0.02539497, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 200.44910307, 0.01533574, 200.44910307, 0.04600721, 140.31437215, -2755.06648239, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 50.11227577, 0.00010077, 150.33682731, 0.00030232, 501.12275769, 0.00100775, -50.11227577, -0.00010077, -150.33682731, -0.00030232, -501.12275769, -0.00100775, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 172.73275505, 0.02038027, 172.73275505, 0.06114082, 120.91292853, -2274.1293509, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 43.18318876, 8.684e-05, 129.54956629, 0.00026052, 431.83188762, 0.0008684, -43.18318876, -8.684e-05, -129.54956629, -0.00026052, -431.83188762, -0.0008684, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 8.5, 12.6, 0.0)
    ops.node(121015, 8.5, 12.6, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.24, 31236704.02526855, 13015293.3438619, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 610.45052628, 0.00066928, 727.18550347, 0.01798762, 72.71855035, 0.05047857, -610.45052628, -0.00066928, -727.18550347, -0.01798762, -72.71855035, -0.05047857, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 500.09332142, 0.00083619, 595.72495732, 0.01617233, 59.57249573, 0.04052455, -500.09332142, -0.00083619, -595.72495732, -0.01617233, -59.57249573, -0.04052455, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 445.01867305, 0.01338552, 445.01867305, 0.04015655, 311.51307113, -4779.23823068, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 111.25466826, 0.00011753, 333.76400479, 0.0003526, 1112.54668262, 0.00117535, -111.25466826, -0.00011753, -333.76400479, -0.0003526, -1112.54668262, -0.00117535, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 312.23185702, 0.0167238, 312.23185702, 0.05017139, 218.56229992, -3689.2095302, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 78.05796426, 8.246e-05, 234.17389277, 0.00024739, 780.57964256, 0.00082464, -78.05796426, -8.246e-05, -234.17389277, -0.00024739, -780.57964256, -0.00082464, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 13.85, 12.6, 0.0)
    ops.node(121016, 13.85, 12.6, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.0875, 29536797.98176469, 12306999.15906862, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 178.44484887, 0.00096951, 208.82970786, 0.00751399, 20.88297079, 0.02739712, -178.44484887, -0.00096951, -208.82970786, -0.00751399, -20.88297079, -0.02739712, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 124.33843194, 0.00129413, 145.51027155, 0.00716293, 14.55102715, 0.02251701, -124.33843194, -0.00129413, -145.51027155, -0.00716293, -14.55102715, -0.02251701, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 143.25893033, 0.01939026, 143.25893033, 0.05817079, 100.28125123, -2232.31713268, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 35.81473258, 0.00010975, 107.44419775, 0.00032926, 358.14732583, 0.00109753, -35.81473258, -0.00010975, -107.44419775, -0.00032926, -358.14732583, -0.00109753, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 124.73190473, 0.0258826, 124.73190473, 0.07764779, 87.31233331, -1952.84119341, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 31.18297618, 9.556e-05, 93.54892855, 0.00028668, 311.82976183, 0.00095559, -31.18297618, -9.556e-05, -93.54892855, -0.00028668, -311.82976183, -0.00095559, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 16.8, 0.0)
    ops.node(121017, 0.0, 16.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.0625, 32686810.6782801, 13619504.44928337, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 67.93856459, 0.00117581, 79.95791545, 0.01019505, 7.99579155, 0.04201523, -67.93856459, -0.00117581, -79.95791545, -0.01019505, -7.99579155, -0.04201523, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 67.93856459, 0.00117581, 79.95791545, 0.01019505, 7.99579155, 0.04201523, -67.93856459, -0.00117581, -79.95791545, -0.01019505, -7.99579155, -0.04201523, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 112.73014004, 0.0235163, 112.73014004, 0.07054889, 78.91109803, -1636.64504017, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 28.18253501, 0.00010926, 84.54760503, 0.00032777, 281.8253501, 0.00109258, -28.18253501, -0.00010926, -84.54760503, -0.00032777, -281.8253501, -0.00109258, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 112.73014004, 0.0235163, 112.73014004, 0.07054889, 78.91109803, -1636.64504017, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 28.18253501, 0.00010926, 84.54760503, 0.00032777, 281.8253501, 0.00109258, -28.18253501, -0.00010926, -84.54760503, -0.00032777, -281.8253501, -0.00109258, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 3.15, 16.8, 0.0)
    ops.node(121018, 3.15, 16.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.135, 33207291.86222024, 13836371.60925843, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 274.80113386, 0.00075042, 324.59869752, 0.01043834, 32.45986975, 0.03884228, -274.80113386, -0.00075042, -324.59869752, -0.01043834, -32.45986975, -0.03884228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 209.59852776, 0.00100592, 247.58052544, 0.009623, 24.75805254, 0.03113634, -209.59852776, -0.00100592, -247.58052544, -0.009623, -24.75805254, -0.03113634, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 214.01726418, 0.01500831, 214.01726418, 0.04502494, 149.81208492, -2596.87744785, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 53.50431604, 9.453e-05, 160.51294813, 0.00028358, 535.04316044, 0.00094525, -53.50431604, -9.453e-05, -160.51294813, -0.00028358, -535.04316044, -0.00094525, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 187.67051314, 0.0201184, 187.67051314, 0.0603552, 131.3693592, -2177.93881642, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 46.91762828, 8.289e-05, 140.75288485, 0.00024867, 469.17628284, 0.00082888, -46.91762828, -8.289e-05, -140.75288485, -0.00024867, -469.17628284, -0.00082888, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 8.5, 16.8, 0.0)
    ops.node(121019, 8.5, 16.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.24, 31145958.86428956, 12977482.86012065, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 588.34315869, 0.00064839, 700.93413534, 0.01662723, 70.09341353, 0.04895045, -588.34315869, -0.00064839, -700.93413534, -0.01662723, -70.09341353, -0.04895045, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 480.14749877, 0.00080655, 572.03311863, 0.0149565, 57.20331186, 0.039183, -480.14749877, -0.00080655, -572.03311863, -0.0149565, -57.20331186, -0.039183, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 416.30185581, 0.01296773, 416.30185581, 0.0389032, 291.41129906, -4070.35945073, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 104.07546395, 0.00011027, 312.22639185, 0.00033081, 1040.75463952, 0.00110271, -104.07546395, -0.00011027, -312.22639185, -0.00033081, -1040.75463952, -0.00110271, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 293.03592277, 0.01613099, 293.03592277, 0.04839296, 205.12514594, -3269.98157715, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 73.25898069, 7.762e-05, 219.77694208, 0.00023286, 732.58980693, 0.0007762, -73.25898069, -7.762e-05, -219.77694208, -0.00023286, -732.58980693, -0.0007762, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 13.85, 16.8, 0.0)
    ops.node(121020, 13.85, 16.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.0875, 33143914.22527458, 13809964.26053108, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 183.3278521, 0.00095819, 214.80138878, 0.00805937, 21.48013888, 0.03734322, -183.3278521, -0.00095819, -214.80138878, -0.00805937, -21.48013888, -0.03734322, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 127.92975932, 0.00127177, 149.89260853, 0.0076398, 14.98926085, 0.03025328, -127.92975932, -0.00127177, -149.89260853, -0.0076398, -14.98926085, -0.03025328, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 159.00643948, 0.01916385, 159.00643948, 0.05749155, 111.30450763, -2310.43431266, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 39.75160987, 0.00010856, 119.25482961, 0.00032568, 397.51609869, 0.0010856, -39.75160987, -0.00010856, -119.25482961, -0.00032568, -397.51609869, -0.0010856, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 136.37766456, 0.02543548, 136.37766456, 0.07630645, 95.46436519, -2004.92355574, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 34.09441614, 9.311e-05, 102.28324842, 0.00027933, 340.9441614, 0.0009311, -34.09441614, -9.311e-05, -102.28324842, -0.00027933, -340.9441614, -0.0009311, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 0.0, 21.0, 0.0)
    ops.node(121021, 0.0, 21.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.0625, 28648574.50466887, 11936906.04361203, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 66.20692903, 0.00127886, 77.82497621, 0.0077442, 7.78249762, 0.02884955, -66.20692903, -0.00127886, -77.82497621, -0.0077442, -7.78249762, -0.02884955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 66.20692903, 0.00127886, 77.82497621, 0.0077442, 7.78249762, 0.02884955, -66.20692903, -0.00127886, -77.82497621, -0.0077442, -7.78249762, -0.02884955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 91.86810104, 0.02557714, 91.86810104, 0.07673143, 64.30767073, -1489.60295154, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 22.96702526, 0.00010159, 68.90107578, 0.00030477, 229.67025259, 0.00101589, -22.96702526, -0.00010159, -68.90107578, -0.00030477, -229.67025259, -0.00101589, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 91.86810104, 0.02557714, 91.86810104, 0.07673143, 64.30767073, -1489.60295154, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 22.96702526, 0.00010159, 68.90107578, 0.00030477, 229.67025259, 0.00101589, -22.96702526, -0.00010159, -68.90107578, -0.00030477, -229.67025259, -0.00101589, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 3.15, 21.0, 0.0)
    ops.node(121022, 3.15, 21.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.135, 31197573.65977765, 12998989.02490735, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 278.24617558, 0.0007704, 329.49156174, 0.0089183, 32.94915617, 0.03376611, -278.24617558, -0.0007704, -329.49156174, -0.0089183, -32.94915617, -0.03376611, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 213.62435817, 0.00103394, 252.96816121, 0.00828121, 25.29681612, 0.02710112, -213.62435817, -0.00103394, -252.96816121, -0.00828121, -25.29681612, -0.02710112, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 197.22524626, 0.01540803, 197.22524626, 0.0462241, 138.05767238, -2451.9029275, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 49.30631157, 9.272e-05, 147.9189347, 0.00027816, 493.06311566, 0.0009272, -49.30631157, -9.272e-05, -147.9189347, -0.00027816, -493.06311566, -0.0009272, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 166.92328698, 0.02067871, 166.92328698, 0.06203614, 116.84630089, -2089.08199109, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 41.73082175, 7.847e-05, 125.19246524, 0.00023542, 417.30821745, 0.00078474, -41.73082175, -7.847e-05, -125.19246524, -0.00023542, -417.30821745, -0.00078474, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 8.5, 21.0, 0.0)
    ops.node(121023, 8.5, 21.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.24, 28469704.83172237, 11862377.01321765, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 541.66831471, 0.00063556, 646.29240354, 0.01412852, 64.62924035, 0.04093196, -541.66831471, -0.00063556, -646.29240354, -0.01412852, -64.62924035, -0.04093196, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 467.53222732, 0.00078424, 557.83681402, 0.01273283, 55.7836814, 0.03282221, -467.53222732, -0.00078424, -557.83681402, -0.01273283, -55.7836814, -0.03282221, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 387.1213051, 0.0127112, 387.1213051, 0.0381336, 270.98491357, -4092.11932556, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 96.78032628, 0.00011218, 290.34097883, 0.00033654, 967.80326276, 0.00112181, -96.78032628, -0.00011218, -290.34097883, -0.00033654, -967.80326276, -0.00112181, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 272.0946562, 0.01568472, 272.0946562, 0.04705416, 190.46625934, -3282.97947343, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 68.02366405, 7.885e-05, 204.07099215, 0.00023654, 680.2366405, 0.00078848, -68.02366405, -7.885e-05, -204.07099215, -0.00023654, -680.2366405, -0.00078848, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 13.85, 21.0, 0.0)
    ops.node(121024, 13.85, 21.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.0875, 30835971.22915247, 12848321.34548019, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 177.79828855, 0.0009305, 208.39765826, 0.00915293, 20.83976583, 0.03253897, -177.79828855, -0.0009305, -208.39765826, -0.00915293, -20.83976583, -0.03253897, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 124.15190405, 0.00122824, 145.51864522, 0.00860176, 14.55186452, 0.02666085, -124.15190405, -0.00122824, -145.51864522, -0.00860176, -14.55186452, -0.02666085, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 157.56253227, 0.01860993, 157.56253227, 0.05582978, 110.29377259, -2455.45878985, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 39.39063307, 0.00011563, 118.17189921, 0.00034688, 393.90633068, 0.00115625, -39.39063307, -0.00011563, -118.17189921, -0.00034688, -393.90633068, -0.00115625, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 141.52779353, 0.02456489, 141.52779353, 0.07369468, 99.06945547, -2101.07840876, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 35.38194838, 0.00010386, 106.14584515, 0.00031157, 353.81948382, 0.00103858, -35.38194838, -0.00010386, -106.14584515, -0.00031157, -353.81948382, -0.00103858, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170025, 0.0, 25.2, 0.0)
    ops.node(121025, 0.0, 25.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 25, 170025, 121025, 0.0625, 28831162.20095946, 12012984.25039978, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20025, 49.99770349, 0.0011287, 59.63408349, 0.00996165, 5.96340835, 0.04302554, -49.99770349, -0.0011287, -59.63408349, -0.00996165, -5.96340835, -0.04302554, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10025, 49.99770349, 0.0011287, 59.63408349, 0.00996165, 5.96340835, 0.04302554, -49.99770349, -0.0011287, -59.63408349, -0.00996165, -5.96340835, -0.04302554, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20025, 25, 0.0, 88.87728887, 0.02257403, 88.87728887, 0.06772208, 62.21410221, -1276.38025114, 0.05, 2, 0, 70025, 21025, 2, 3)
    ops.uniaxialMaterial('LimitState', 40025, 22.21932222, 9.766e-05, 66.65796665, 0.00029298, 222.19322217, 0.00097659, -22.21932222, -9.766e-05, -66.65796665, -0.00029298, -222.19322217, -0.00097659, 0.4, 0.3, 0.003, 0.0, 0.0, 20025, 2)
    ops.limitCurve('ThreePoint', 10025, 25, 0.0, 88.87728887, 0.02257403, 88.87728887, 0.06772208, 62.21410221, -1276.38025114, 0.05, 2, 0, 70025, 21025, 1, 3)
    ops.uniaxialMaterial('LimitState', 30025, 22.21932222, 9.766e-05, 66.65796665, 0.00029298, 222.19322217, 0.00097659, -22.21932222, -9.766e-05, -66.65796665, -0.00029298, -222.19322217, -0.00097659, 0.4, 0.3, 0.003, 0.0, 0.0, 10025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 25, 99999, 'P', 40025, 'Vy', 30025, 'Vz', 20025, 'My', 10025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170025, 70025, 170025, 25, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121025, 121025, 21025, 25, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170026, 3.15, 25.2, 0.0)
    ops.node(121026, 3.15, 25.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 26, 170026, 121026, 0.09, 29112165.54338898, 12130068.97641208, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20026, 123.94975273, 0.00100166, 146.22367603, 0.00810059, 14.6223676, 0.02923472, -123.94975273, -0.00100166, -146.22367603, -0.00810059, -14.6223676, -0.02923472, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10026, 112.18849308, 0.00100166, 132.34890353, 0.00810059, 13.23489035, 0.02923472, -112.18849308, -0.00100166, -132.34890353, -0.00810059, -13.23489035, -0.02923472, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20026, 26, 0.0, 132.53714612, 0.02003326, 132.53714612, 0.06009977, 92.77600229, -1928.37200108, 0.05, 2, 0, 70026, 21026, 2, 3)
    ops.uniaxialMaterial('LimitState', 40026, 33.13428653, 0.00010016, 99.40285959, 0.00030047, 331.34286531, 0.00100158, -33.13428653, -0.00010016, -99.40285959, -0.00030047, -331.34286531, -0.00100158, 0.4, 0.3, 0.003, 0.0, 0.0, 20026, 2)
    ops.limitCurve('ThreePoint', 10026, 26, 0.0, 132.53714612, 0.02003326, 132.53714612, 0.06009977, 92.77600229, -1928.37200108, 0.05, 2, 0, 70026, 21026, 1, 3)
    ops.uniaxialMaterial('LimitState', 30026, 33.13428653, 0.00010016, 99.40285959, 0.00030047, 331.34286531, 0.00100158, -33.13428653, -0.00010016, -99.40285959, -0.00030047, -331.34286531, -0.00100158, 0.4, 0.3, 0.003, 0.0, 0.0, 10026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 26, 99999, 'P', 40026, 'Vy', 30026, 'Vz', 20026, 'My', 10026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170026, 70026, 170026, 26, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121026, 121026, 21026, 26, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170027, 8.5, 25.2, 0.0)
    ops.node(121027, 8.5, 25.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 27, 170027, 121027, 0.105, 31634465.25138603, 13181027.18807751, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20027, 170.46523172, 0.00110449, 200.63920113, 0.00909268, 20.06392011, 0.02848112, -170.46523172, -0.00110449, -200.63920113, -0.00909268, -20.06392011, -0.02848112, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10027, 183.73176764, 0.00096654, 216.25404025, 0.00933373, 21.62540403, 0.03097573, -183.73176764, -0.00096654, -216.25404025, -0.00933373, -21.62540403, -0.03097573, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20027, 27, 0.0, 157.69032883, 0.02208974, 157.69032883, 0.06626923, 110.38323018, -2139.86318984, 0.05, 2, 0, 70027, 21027, 2, 3)
    ops.uniaxialMaterial('LimitState', 40027, 39.42258221, 9.4e-05, 118.26774662, 0.000282, 394.22582208, 0.00093998, -39.42258221, -9.4e-05, -118.26774662, -0.000282, -394.22582208, -0.00093998, 0.4, 0.3, 0.003, 0.0, 0.0, 20027, 2)
    ops.limitCurve('ThreePoint', 10027, 27, 0.0, 164.11875627, 0.01933072, 164.11875627, 0.05799215, 114.88312939, -2276.03989635, 0.05, 2, 0, 70027, 21027, 1, 3)
    ops.uniaxialMaterial('LimitState', 30027, 41.02968907, 9.783e-05, 123.0890672, 0.00029349, 410.29689068, 0.0009783, -41.02968907, -9.783e-05, -123.0890672, -0.00029349, -410.29689068, -0.0009783, 0.4, 0.3, 0.003, 0.0, 0.0, 10027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 27, 99999, 'P', 40027, 'Vy', 30027, 'Vz', 20027, 'My', 10027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170027, 70027, 170027, 27, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121027, 121027, 21027, 27, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170028, 13.85, 25.2, 0.0)
    ops.node(121028, 13.85, 25.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 28, 170028, 121028, 0.0625, 29797622.31469679, 12415675.96445699, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20028, 75.73478514, 0.00122513, 89.13105548, 0.00887328, 8.91310555, 0.03292096, -75.73478514, -0.00122513, -89.13105548, -0.00887328, -8.91310555, -0.03292096, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10028, 71.5904571, 0.00122513, 84.2536622, 0.00887328, 8.42536622, 0.03292096, -71.5904571, -0.00122513, -84.2536622, -0.00887328, -8.42536622, -0.03292096, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20028, 28, 0.0, 101.95856712, 0.02450269, 101.95856712, 0.07350806, 71.37099698, -1543.11578712, 0.05, 2, 0, 70028, 21028, 2, 3)
    ops.uniaxialMaterial('LimitState', 40028, 25.48964178, 0.0001084, 76.46892534, 0.0003252, 254.89641779, 0.001084, -25.48964178, -0.0001084, -76.46892534, -0.0003252, -254.89641779, -0.001084, 0.4, 0.3, 0.003, 0.0, 0.0, 20028, 2)
    ops.limitCurve('ThreePoint', 10028, 28, 0.0, 101.95856712, 0.02450269, 101.95856712, 0.07350806, 71.37099698, -1543.11578712, 0.05, 2, 0, 70028, 21028, 1, 3)
    ops.uniaxialMaterial('LimitState', 30028, 25.48964178, 0.0001084, 76.46892534, 0.0003252, 254.89641779, 0.001084, -25.48964178, -0.0001084, -76.46892534, -0.0003252, -254.89641779, -0.001084, 0.4, 0.3, 0.003, 0.0, 0.0, 10028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 28, 99999, 'P', 40028, 'Vy', 30028, 'Vz', 20028, 'My', 10028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170028, 70028, 170028, 28, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121028, 121028, 21028, 28, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.5, 0.0, 3.0)
    ops.node(122003, 8.5, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.105, 28932777.84087041, 12055324.10036267, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 109.47218131, 0.00102257, 129.90201144, 0.00785366, 12.99020114, 0.02993855, -109.47218131, -0.00102257, -129.90201144, -0.00785366, -12.99020114, -0.02993855, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 140.18159442, 0.00090034, 166.34245215, 0.00807305, 16.63424521, 0.03286826, -140.18159442, -0.00090034, -166.34245215, -0.00807305, -16.63424521, -0.03286826, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 138.00683647, 0.02045139, 138.00683647, 0.06135418, 96.60478553, -1851.53017944, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 34.50170912, 8.995e-05, 103.50512736, 0.00026984, 345.01709119, 0.00089947, -34.50170912, -8.995e-05, -103.50512736, -0.00026984, -345.01709119, -0.00089947, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 144.79459062, 0.01800671, 144.79459062, 0.05402012, 101.35621343, -2007.46194676, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 36.19864765, 9.437e-05, 108.59594296, 0.00028311, 361.98647655, 0.00094371, -36.19864765, -9.437e-05, -108.59594296, -0.00028311, -361.98647655, -0.00094371, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.85, 0.0, 3.0)
    ops.node(122004, 13.85, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.0625, 29763467.94681929, 12401444.97784137, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 64.49761687, 0.00114017, 76.59187362, 0.0107118, 7.65918736, 0.04205968, -64.49761687, -0.00114017, -76.59187362, -0.0107118, -7.65918736, -0.04205968, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 60.44709558, 0.00114017, 71.78181969, 0.0107118, 7.17818197, 0.04205968, -60.44709558, -0.00114017, -71.78181969, -0.0107118, -7.17818197, -0.04205968, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 98.92872803, 0.02280343, 98.92872803, 0.0684103, 69.25010962, -1467.26598489, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 24.73218201, 0.0001053, 74.19654602, 0.0003159, 247.32182007, 0.00105299, -24.73218201, -0.0001053, -74.19654602, -0.0003159, -247.32182007, -0.00105299, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 98.92872803, 0.02280343, 98.92872803, 0.0684103, 69.25010962, -1467.26598489, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 24.73218201, 0.0001053, 74.19654602, 0.0003159, 247.32182007, 0.00105299, -24.73218201, -0.0001053, -74.19654602, -0.0003159, -247.32182007, -0.00105299, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.2, 3.0)
    ops.node(122005, 0.0, 4.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.0625, 30459682.73689429, 12691534.47370596, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 54.19478507, 0.00114676, 64.43218516, 0.00915894, 6.44321852, 0.04368065, -54.19478507, -0.00114676, -64.43218516, -0.00915894, -6.44321852, -0.04368065, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 54.19478507, 0.00114676, 64.43218516, 0.00915894, 6.44321852, 0.04368065, -54.19478507, -0.00114676, -64.43218516, -0.00915894, -6.44321852, -0.04368065, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 87.80520418, 0.02293523, 87.80520418, 0.0688057, 61.46364293, -1317.80215228, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 21.95130105, 9.132e-05, 65.85390314, 0.00027397, 219.51301046, 0.00091323, -21.95130105, -9.132e-05, -65.85390314, -0.00027397, -219.51301046, -0.00091323, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 87.80520418, 0.02293523, 87.80520418, 0.0688057, 61.46364293, -1317.80215228, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 21.95130105, 9.132e-05, 65.85390314, 0.00027397, 219.51301046, 0.00091323, -21.95130105, -9.132e-05, -65.85390314, -0.00027397, -219.51301046, -0.00091323, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 3.15, 4.2, 3.0)
    ops.node(122006, 3.15, 4.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.135, 31022146.02594959, 12925894.177479, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 199.91480744, 0.00071986, 238.01451103, 0.00894774, 23.8014511, 0.03764619, -199.91480744, -0.00071986, -238.01451103, -0.00894774, -23.8014511, -0.03764619, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 135.14014888, 0.00095311, 160.89511762, 0.00827153, 16.08951176, 0.03000793, -135.14014888, -0.00095311, -160.89511762, -0.00827153, -16.08951176, -0.03000793, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 183.51732947, 0.01439726, 183.51732947, 0.04319177, 128.46213063, -2141.93285288, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 45.87933237, 8.676e-05, 137.6379971, 0.00026029, 458.79332367, 0.00086763, -45.87933237, -8.676e-05, -137.6379971, -0.00026029, -458.79332367, -0.00086763, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 152.7732235, 0.01906222, 152.7732235, 0.05718666, 106.94125645, -1771.2527938, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 38.19330588, 7.223e-05, 114.57991763, 0.00021668, 381.93305876, 0.00072228, -38.19330588, -7.223e-05, -114.57991763, -0.00021668, -381.93305876, -0.00072228, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 8.5, 4.2, 3.0)
    ops.node(122007, 8.5, 4.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.24, 29648948.29106077, 12353728.45460865, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 414.79254474, 0.00064402, 497.35232194, 0.00942648, 49.73523219, 0.0350392, -414.79254474, -0.00064402, -497.35232194, -0.00942648, -49.73523219, -0.0350392, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 243.83368618, 0.00080244, 292.36603099, 0.00870458, 29.2366031, 0.0286409, -243.83368618, -0.00080244, -292.36603099, -0.00870458, -29.2366031, -0.0286409, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 345.0046151, 0.01288035, 345.0046151, 0.03864106, 241.50323057, -2962.45616311, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 86.25115378, 9.6e-05, 258.75346133, 0.000288, 862.51153776, 0.00096, -86.25115378, -9.6e-05, -258.75346133, -0.000288, -862.51153776, -0.00096, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 243.46826612, 0.01604885, 243.46826612, 0.04814655, 170.42778628, -2407.12490194, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 60.86706653, 6.775e-05, 182.60119959, 0.00020324, 608.67066529, 0.00067747, -60.86706653, -6.775e-05, -182.60119959, -0.00020324, -608.67066529, -0.00067747, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 13.85, 4.2, 3.0)
    ops.node(122008, 13.85, 4.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.0875, 31852761.18597458, 13271983.82748941, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 133.48829, 0.00087063, 157.7615518, 0.00877714, 15.77615518, 0.04181582, -133.48829, -0.00087063, -157.7615518, -0.00877714, -15.77615518, -0.04181582, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 93.48397727, 0.00113843, 110.48292943, 0.00822864, 11.04829294, 0.03374165, -93.48397727, -0.00113843, -110.48292943, -0.00822864, -11.04829294, -0.03374165, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 141.4339349, 0.01741259, 141.4339349, 0.05223776, 99.00375443, -1957.18777411, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 35.35848373, 0.00010048, 106.07545118, 0.00030143, 353.58483725, 0.00100476, -35.35848373, -0.00010048, -106.07545118, -0.00030143, -353.58483725, -0.00100476, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 121.69400727, 0.02276851, 121.69400727, 0.06830553, 85.18580509, -1651.00715019, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 30.42350182, 8.645e-05, 91.27050545, 0.00025936, 304.23501817, 0.00086453, -30.42350182, -8.645e-05, -91.27050545, -0.00025936, -304.23501817, -0.00086453, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.4, 3.0)
    ops.node(122009, 0.0, 8.4, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.0625, 31093670.5558692, 12955696.0649455, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 55.94932512, 0.00114399, 66.41287733, 0.00952335, 6.64128773, 0.0444581, -55.94932512, -0.00114399, -66.41287733, -0.00952335, -6.64128773, -0.0444581, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 55.94932512, 0.00114399, 66.41287733, 0.00952335, 6.64128773, 0.0444581, -55.94932512, -0.00114399, -66.41287733, -0.00952335, -6.64128773, -0.0444581, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 94.87768267, 0.02287983, 94.87768267, 0.06863948, 66.41437787, -1341.06870985, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 23.71942067, 9.667e-05, 71.15826201, 0.00029, 237.19420669, 0.00096667, -23.71942067, -9.667e-05, -71.15826201, -0.00029, -237.19420669, -0.00096667, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 94.87768267, 0.02287983, 94.87768267, 0.06863948, 66.41437787, -1341.06870985, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 23.71942067, 9.667e-05, 71.15826201, 0.00029, 237.19420669, 0.00096667, -23.71942067, -9.667e-05, -71.15826201, -0.00029, -237.19420669, -0.00096667, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 3.15, 8.4, 3.0)
    ops.node(122010, 3.15, 8.4, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.135, 31197529.69108484, 12998970.70461868, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 201.50994223, 0.0007184, 239.99040417, 0.00946824, 23.99904042, 0.03893155, -201.50994223, -0.0007184, -239.99040417, -0.00946824, -23.99904042, -0.03893155, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 137.03700889, 0.00093999, 163.20568001, 0.00872267, 16.320568, 0.0310384, -137.03700889, -0.00093999, -163.20568001, -0.00872267, -16.320568, -0.0310384, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 188.69991666, 0.01436797, 188.69991666, 0.04310392, 132.08994166, -2246.8211236, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 47.17497916, 8.871e-05, 141.52493749, 0.00026614, 471.74979165, 0.00088712, -47.17497916, -8.871e-05, -141.52493749, -0.00026614, -471.74979165, -0.00088712, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 162.70005083, 0.01879973, 162.70005083, 0.0563992, 113.89003558, -1820.98625352, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 40.67501271, 7.649e-05, 122.02503812, 0.00022947, 406.75012708, 0.00076489, -40.67501271, -7.649e-05, -122.02503812, -0.00022947, -406.75012708, -0.00076489, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.5, 8.4, 3.0)
    ops.node(122011, 8.5, 8.4, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.24, 30639979.47479929, 12766658.1144997, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 409.09406275, 0.00062673, 489.89234146, 0.00945076, 48.98923415, 0.03189594, -409.09406275, -0.00062673, -489.89234146, -0.00945076, -48.98923415, -0.03189594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 253.19028917, 0.00077945, 303.1967337, 0.00881665, 30.31967337, 0.02680148, -253.19028917, -0.00077945, -303.1967337, -0.00881665, -30.31967337, -0.02680148, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 347.2471647, 0.01253458, 347.2471647, 0.03760374, 243.07301529, -2760.90722269, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 86.81179118, 9.35e-05, 260.43537353, 0.0002805, 868.11791176, 0.00093498, -86.81179118, -9.35e-05, -260.43537353, -0.0002805, -868.11791176, -0.00093498, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 245.49623068, 0.01558892, 245.49623068, 0.04676677, 171.84736148, -2285.45026361, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 61.37405767, 6.61e-05, 184.12217301, 0.0001983, 613.7405767, 0.00066101, -61.37405767, -6.61e-05, -184.12217301, -0.0001983, -613.7405767, -0.00066101, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 13.85, 8.4, 3.0)
    ops.node(122012, 13.85, 8.4, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.0875, 32743280.02781167, 13643033.34492153, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 132.134392, 0.00090803, 155.99959891, 0.00925871, 15.59995989, 0.04441109, -132.134392, -0.00090803, -155.99959891, -0.00925871, -15.59995989, -0.04441109, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 92.32945179, 0.0012183, 109.00536362, 0.00870683, 10.90053636, 0.03585208, -92.32945179, -0.0012183, -109.00536362, -0.00870683, -10.90053636, -0.03585208, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 146.33780645, 0.01816051, 146.33780645, 0.05448152, 102.43646451, -2005.92131047, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 36.58445161, 0.00010113, 109.75335484, 0.0003034, 365.84451612, 0.00101133, -36.58445161, -0.00010113, -109.75335484, -0.0003034, -365.84451612, -0.00101133, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 130.18858365, 0.02436599, 130.18858365, 0.07309798, 91.13200855, -1682.93459126, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 32.54714591, 8.997e-05, 97.64143773, 0.00026992, 325.47145911, 0.00089972, -32.54714591, -8.997e-05, -97.64143773, -0.00026992, -325.47145911, -0.00089972, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 12.6, 3.0)
    ops.node(122013, 0.0, 12.6, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0625, 31552901.56802548, 13147042.32001062, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 55.60441487, 0.00112717, 65.97337615, 0.01111793, 6.59733761, 0.04715336, -55.60441487, -0.00112717, -65.97337615, -0.01111793, -6.59733761, -0.04715336, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 55.60441487, 0.00112717, 65.97337615, 0.01111793, 6.59733761, 0.04715336, -55.60441487, -0.00112717, -65.97337615, -0.01111793, -6.59733761, -0.04715336, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 104.11637059, 0.02254333, 104.11637059, 0.06763, 72.88145941, -1502.0786703, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 26.02909265, 0.00010454, 78.08727794, 0.00031361, 260.29092647, 0.00104536, -26.02909265, -0.00010454, -78.08727794, -0.00031361, -260.29092647, -0.00104536, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 104.11637059, 0.02254333, 104.11637059, 0.06763, 72.88145941, -1502.0786703, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 26.02909265, 0.00010454, 78.08727794, 0.00031361, 260.29092647, 0.00104536, -26.02909265, -0.00010454, -78.08727794, -0.00031361, -260.29092647, -0.00104536, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 3.15, 12.6, 3.0)
    ops.node(122014, 3.15, 12.6, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.135, 29383932.72866164, 12243305.30360902, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 197.45282038, 0.00073681, 235.50058553, 0.00920769, 23.55005855, 0.03534796, -197.45282038, -0.00073681, -235.50058553, -0.00920769, -23.55005855, -0.03534796, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 133.26250511, 0.00098256, 158.94124948, 0.00851711, 15.89412495, 0.02831594, -133.26250511, -0.00098256, -158.94124948, -0.00851711, -15.89412495, -0.02831594, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 175.81547496, 0.01473622, 175.81547496, 0.04420865, 123.07083247, -2146.16544476, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 43.95386874, 8.776e-05, 131.86160622, 0.00026327, 439.53868739, 0.00087756, -43.95386874, -8.776e-05, -131.86160622, -0.00026327, -439.53868739, -0.00087756, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 150.7371821, 0.01965117, 150.7371821, 0.05895352, 105.51602747, -1760.39563747, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 37.68429552, 7.524e-05, 113.05288657, 0.00022572, 376.84295524, 0.00075239, -37.68429552, -7.524e-05, -113.05288657, -0.00022572, -376.84295524, -0.00075239, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 8.5, 12.6, 3.0)
    ops.node(122015, 8.5, 12.6, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.24, 32173567.68366997, 13405653.20152915, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 411.0321969, 0.00061029, 490.80792582, 0.00964039, 49.08079258, 0.03358621, -411.0321969, -0.00061029, -490.80792582, -0.00964039, -49.08079258, -0.03358621, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 254.84324179, 0.00074866, 304.30483027, 0.00897356, 30.43048303, 0.02816081, -254.84324179, -0.00074866, -304.30483027, -0.00897356, -30.43048303, -0.02816081, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 364.26262244, 0.0122058, 364.26262244, 0.03661739, 254.98383571, -2761.39719024, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 91.06565561, 9.34e-05, 273.19696683, 0.00028021, 910.65655611, 0.00093405, -91.06565561, -9.34e-05, -273.19696683, -0.00028021, -910.65655611, -0.00093405, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 257.68073568, 0.01497318, 257.68073568, 0.04491955, 180.37651498, -2285.74745135, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 64.42018392, 6.607e-05, 193.26055176, 0.00019822, 644.2018392, 0.00066075, -64.42018392, -6.607e-05, -193.26055176, -0.00019822, -644.2018392, -0.00066075, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 13.85, 12.6, 3.0)
    ops.node(122016, 13.85, 12.6, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.0875, 34740952.45671548, 14475396.85696478, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 135.02056622, 0.00089969, 158.79036495, 0.00891743, 15.8790365, 0.04836963, -135.02056622, -0.00089969, -158.79036495, -0.00891743, -15.8790365, -0.04836963, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 94.40528085, 0.00119576, 111.02493063, 0.00838572, 11.10249306, 0.03885136, -94.40528085, -0.00119576, -111.02493063, -0.00838572, -11.10249306, -0.03885136, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 152.5627914, 0.01799377, 152.5627914, 0.05398131, 106.79395398, -1998.87551255, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 38.14069785, 9.937e-05, 114.42209355, 0.00029812, 381.40697849, 0.00099372, -38.14069785, -9.937e-05, -114.42209355, -0.00029812, -381.40697849, -0.00099372, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 133.11215705, 0.02391512, 133.11215705, 0.07174536, 93.17850993, -1678.32393306, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 33.27803926, 8.67e-05, 99.83411779, 0.00026011, 332.78039262, 0.00086703, -33.27803926, -8.67e-05, -99.83411779, -0.00026011, -332.78039262, -0.00086703, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 16.8, 3.0)
    ops.node(122017, 0.0, 16.8, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.0625, 31173006.9773976, 12988752.907249, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 55.4198343, 0.0012074, 65.7797341, 0.01097868, 6.57797341, 0.04610614, -55.4198343, -0.0012074, -65.7797341, -0.01097868, -6.57797341, -0.04610614, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 55.4198343, 0.0012074, 65.7797341, 0.01097868, 6.57797341, 0.04610614, -55.4198343, -0.0012074, -65.7797341, -0.01097868, -6.57797341, -0.04610614, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 102.55622349, 0.02414809, 102.55622349, 0.07244427, 71.78935644, -1482.87806006, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 25.63905587, 0.00010422, 76.91716762, 0.00031267, 256.39055873, 0.00104224, -25.63905587, -0.00010422, -76.91716762, -0.00031267, -256.39055873, -0.00104224, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 102.55622349, 0.02414809, 102.55622349, 0.07244427, 71.78935644, -1482.87806006, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 25.63905587, 0.00010422, 76.91716762, 0.00031267, 256.39055873, 0.00104224, -25.63905587, -0.00010422, -76.91716762, -0.00031267, -256.39055873, -0.00104224, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 3.15, 16.8, 3.0)
    ops.node(122018, 3.15, 16.8, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.135, 33548430.65450311, 13978512.77270963, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 196.92636326, 0.00074828, 233.50851564, 0.00928589, 23.35085156, 0.04238908, -196.92636326, -0.00074828, -233.50851564, -0.00928589, -23.35085156, -0.04238908, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 131.79331632, 0.00102273, 156.27598639, 0.00861664, 15.62759864, 0.03368923, -131.79331632, -0.00102273, -156.27598639, -0.00861664, -15.62759864, -0.03368923, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 196.24171995, 0.01496569, 196.24171995, 0.04489707, 137.36920396, -2150.80025883, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 49.06042999, 8.579e-05, 147.18128996, 0.00025738, 490.60429987, 0.00085793, -49.06042999, -8.579e-05, -147.18128996, -0.00025738, -490.60429987, -0.00085793, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 167.56545387, 0.02045452, 167.56545387, 0.06136357, 117.29581771, -1763.19367017, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 41.89136347, 7.326e-05, 125.67409041, 0.00021977, 418.91363468, 0.00073256, -41.89136347, -7.326e-05, -125.67409041, -0.00021977, -418.91363468, -0.00073256, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 8.5, 16.8, 3.0)
    ops.node(122019, 8.5, 16.8, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.24, 30419003.01311731, 12674584.58879888, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 426.62220374, 0.00062688, 511.0486282, 0.00757962, 51.10486282, 0.02978992, -426.62220374, -0.00062688, -511.0486282, -0.00757962, -51.10486282, -0.02978992, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 264.01793295, 0.00076688, 316.26577631, 0.00709965, 31.62657763, 0.02489628, -264.01793295, -0.00076688, -316.26577631, -0.00709965, -31.62657763, -0.02489628, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 332.42753677, 0.01253755, 332.42753677, 0.03761266, 232.69927574, -2480.44321152, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 83.10688419, 9.016e-05, 249.32065258, 0.00027048, 831.06884192, 0.00090158, -83.10688419, -9.016e-05, -249.32065258, -0.00027048, -831.06884192, -0.00090158, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 229.55419203, 0.01533753, 229.55419203, 0.0460126, 160.68793442, -2114.11668792, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 57.38854801, 6.226e-05, 172.16564402, 0.00018677, 573.88548007, 0.00062258, -57.38854801, -6.226e-05, -172.16564402, -0.00018677, -573.88548007, -0.00062258, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 13.85, 16.8, 3.0)
    ops.node(122020, 13.85, 16.8, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.0875, 31490873.63180486, 13121197.34658536, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 132.7954713, 0.00090129, 156.98834587, 0.01071227, 15.69883459, 0.04285747, -132.7954713, -0.00090129, -156.98834587, -0.01071227, -15.69883459, -0.04285747, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 92.80630108, 0.00119749, 109.71388972, 0.00999555, 10.97138897, 0.03481861, -92.80630108, -0.00119749, -109.71388972, -0.00999555, -10.97138897, -0.03481861, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 151.91827, 0.01802579, 151.91827, 0.05407738, 106.342789, -2242.753708, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 37.9795675, 0.00010916, 113.9387025, 0.00032749, 379.79567501, 0.00109165, -37.9795675, -0.00010916, -113.9387025, -0.00032749, -379.79567501, -0.00109165, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 135.12513349, 0.02394986, 135.12513349, 0.07184957, 94.58759344, -1836.93232595, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 33.78128337, 9.71e-05, 101.34385012, 0.00029129, 337.81283373, 0.00097098, -33.78128337, -9.71e-05, -101.34385012, -0.00029129, -337.81283373, -0.00097098, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 0.0, 21.0, 3.0)
    ops.node(122021, 0.0, 21.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.0625, 30833253.78289012, 12847189.07620422, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 55.15312821, 0.0012214, 65.48124814, 0.01114837, 6.54812481, 0.04544306, -55.15312821, -0.0012214, -65.48124814, -0.01114837, -6.54812481, -0.04544306, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 55.15312821, 0.0012214, 65.48124814, 0.01114837, 6.54812481, 0.04544306, -55.15312821, -0.0012214, -65.48124814, -0.01114837, -6.54812481, -0.04544306, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 103.55099788, 0.02442801, 103.55099788, 0.07328402, 72.48569852, -1529.31884841, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 25.88774947, 0.00010639, 77.66324841, 0.00031918, 258.8774947, 0.00106395, -25.88774947, -0.00010639, -77.66324841, -0.00031918, -258.8774947, -0.00106395, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 103.55099788, 0.02442801, 103.55099788, 0.07328402, 72.48569852, -1529.31884841, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 25.88774947, 0.00010639, 77.66324841, 0.00031918, 258.8774947, 0.00106395, -25.88774947, -0.00010639, -77.66324841, -0.00031918, -258.8774947, -0.00106395, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 3.15, 21.0, 3.0)
    ops.node(122022, 3.15, 21.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.135, 30876581.74064044, 12865242.39193352, 0.002377, 0.00111375, 0.00250594, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 200.67122295, 0.00073161, 239.083926, 0.00886902, 23.9083926, 0.037778, -200.67122295, -0.00073161, -239.083926, -0.00886902, -23.9083926, -0.037778, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 135.85108873, 0.00096782, 161.85585142, 0.00820577, 16.18558514, 0.03010163, -135.85108873, -0.00096782, -161.85585142, -0.00820577, -16.18558514, -0.03010163, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 180.84341723, 0.01463216, 180.84341723, 0.04389649, 126.59039206, -2096.99327151, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 45.21085431, 8.59e-05, 135.63256292, 0.00025771, 452.10854307, 0.00085902, -45.21085431, -8.59e-05, -135.63256292, -0.00025771, -452.10854307, -0.00085902, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 150.85687463, 0.01935642, 150.85687463, 0.05806926, 105.59981224, -1730.66081883, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 37.71421866, 7.166e-05, 113.14265597, 0.00021498, 377.14218657, 0.00071658, -37.71421866, -7.166e-05, -113.14265597, -0.00021498, -377.14218657, -0.00071658, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 8.5, 21.0, 3.0)
    ops.node(122023, 8.5, 21.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.24, 32628585.07440268, 13595243.78100112, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 412.47923905, 0.00060958, 492.02235442, 0.00880139, 49.20223544, 0.0380094, -412.47923905, -0.00060958, -492.02235442, -0.00880139, -49.20223544, -0.0380094, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 242.70002815, 0.00074304, 289.50266575, 0.00811374, 28.95026657, 0.03084853, -242.70002815, -0.00074304, -289.50266575, -0.00811374, -28.95026657, -0.03084853, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 373.47697886, 0.01219167, 373.47697886, 0.03657502, 261.4338852, -2857.30487208, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 93.36924472, 9.443e-05, 280.10773415, 0.0002833, 933.69244716, 0.00094432, -93.36924472, -9.443e-05, -280.10773415, -0.0002833, -933.69244716, -0.00094432, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 264.07692448, 0.01486083, 264.07692448, 0.0445825, 184.85384714, -2343.78646919, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 66.01923112, 6.677e-05, 198.05769336, 0.00020031, 660.19231121, 0.00066771, -66.01923112, -6.677e-05, -198.05769336, -0.00020031, -660.19231121, -0.00066771, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 13.85, 21.0, 3.0)
    ops.node(122024, 13.85, 21.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.0875, 31340563.46419737, 13058568.11008224, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 136.87318063, 0.00090599, 161.82472666, 0.01049466, 16.18247267, 0.04226298, -136.87318063, -0.00090599, -161.82472666, -0.01049466, -16.18247267, -0.04226298, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 95.77582426, 0.00118873, 113.23545278, 0.00978743, 11.32354528, 0.03431946, -95.77582426, -0.00118873, -113.23545278, -0.00978743, -11.32354528, -0.03431946, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 149.97071438, 0.01811973, 149.97071438, 0.05435919, 104.97950007, -2205.62885831, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 37.4926786, 0.00010828, 112.47803579, 0.00032485, 374.92678596, 0.00108282, -37.4926786, -0.00010828, -112.47803579, -0.00032485, -374.92678596, -0.00108282, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 133.59740497, 0.02377458, 133.59740497, 0.07132373, 93.51818348, -1812.91225869, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 33.39935124, 9.646e-05, 100.19805373, 0.00028938, 333.99351242, 0.0009646, -33.39935124, -9.646e-05, -100.19805373, -0.00028938, -333.99351242, -0.0009646, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171025, 0.0, 25.2, 3.0)
    ops.node(122025, 0.0, 25.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1025, 171025, 122025, 0.0625, 34483736.1112569, 14368223.37969038, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21025, 43.74690265, 0.00109915, 51.92718022, 0.01061786, 5.19271802, 0.06100283, -43.74690265, -0.00109915, -51.92718022, -0.01061786, -5.19271802, -0.06100283, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11025, 43.74690265, 0.00109915, 51.92718022, 0.01061786, 5.19271802, 0.06100283, -43.74690265, -0.00109915, -51.92718022, -0.01061786, -5.19271802, -0.06100283, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21025, 1025, 0.0, 96.89826109, 0.02198297, 96.89826109, 0.0659489, 67.82878276, -1244.72866203, 0.05, 2, 0, 71025, 22025, 2, 3)
    ops.uniaxialMaterial('LimitState', 41025, 24.22456527, 8.902e-05, 72.67369582, 0.00026706, 242.24565272, 0.0008902, -24.22456527, -8.902e-05, -72.67369582, -0.00026706, -242.24565272, -0.0008902, 0.4, 0.3, 0.003, 0.0, 0.0, 21025, 2)
    ops.limitCurve('ThreePoint', 11025, 1025, 0.0, 96.89826109, 0.02198297, 96.89826109, 0.0659489, 67.82878276, -1244.72866203, 0.05, 2, 0, 71025, 22025, 1, 3)
    ops.uniaxialMaterial('LimitState', 31025, 24.22456527, 8.902e-05, 72.67369582, 0.00026706, 242.24565272, 0.0008902, -24.22456527, -8.902e-05, -72.67369582, -0.00026706, -242.24565272, -0.0008902, 0.4, 0.3, 0.003, 0.0, 0.0, 11025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1025, 99999, 'P', 41025, 'Vy', 31025, 'Vz', 21025, 'My', 11025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171025, 71025, 171025, 1025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122025, 122025, 22025, 1025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171026, 3.15, 25.2, 3.0)
    ops.node(122026, 3.15, 25.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1026, 171026, 122026, 0.09, 31381350.19339714, 13075562.58058214, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21026, 109.25344556, 0.00098254, 129.85300964, 0.01009334, 12.98530096, 0.04245307, -109.25344556, -0.00098254, -129.85300964, -0.01009334, -12.98530096, -0.04245307, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11026, 97.98605075, 0.00098254, 116.46116539, 0.01009334, 11.64611654, 0.04245307, -97.98605075, -0.00098254, -116.46116539, -0.01009334, -11.64611654, -0.04245307, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21026, 1026, 0.0, 134.22063993, 0.01965083, 134.22063993, 0.05895248, 93.95444795, -1782.73543701, 0.05, 2, 0, 71026, 22026, 2, 3)
    ops.uniaxialMaterial('LimitState', 41026, 33.55515998, 9.41e-05, 100.66547995, 0.00028229, 335.55159983, 0.00094096, -33.55515998, -9.41e-05, -100.66547995, -0.00028229, -335.55159983, -0.00094096, 0.4, 0.3, 0.003, 0.0, 0.0, 21026, 2)
    ops.limitCurve('ThreePoint', 11026, 1026, 0.0, 134.22063993, 0.01965083, 134.22063993, 0.05895248, 93.95444795, -1782.73543701, 0.05, 2, 0, 71026, 22026, 1, 3)
    ops.uniaxialMaterial('LimitState', 31026, 33.55515998, 9.41e-05, 100.66547995, 0.00028229, 335.55159983, 0.00094096, -33.55515998, -9.41e-05, -100.66547995, -0.00028229, -335.55159983, -0.00094096, 0.4, 0.3, 0.003, 0.0, 0.0, 11026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1026, 99999, 'P', 41026, 'Vy', 31026, 'Vz', 21026, 'My', 11026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171026, 71026, 171026, 1026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122026, 122026, 22026, 1026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171027, 8.5, 25.2, 3.0)
    ops.node(122027, 8.5, 25.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1027, 171027, 122027, 0.105, 28676680.34297918, 11948616.80957466, 0.00152551, 0.00117906, 0.00086625, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21027, 119.61996435, 0.00103474, 141.91918974, 0.00950273, 14.19191897, 0.02839429, -119.61996435, -0.00103474, -141.91918974, -0.00950273, -14.19191897, -0.02839429, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11027, 141.12699941, 0.00091686, 167.43550725, 0.00978663, 16.74355073, 0.03087398, -141.12699941, -0.00091686, -167.43550725, -0.00978663, -16.74355073, -0.03087398, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21027, 1027, 0.0, 137.71577932, 0.02069487, 137.71577932, 0.0620846, 96.40104552, -1865.81508712, 0.05, 2, 0, 71027, 22027, 2, 3)
    ops.uniaxialMaterial('LimitState', 41027, 34.42894483, 9.056e-05, 103.28683449, 0.00027168, 344.2894483, 0.00090559, -34.42894483, -9.056e-05, -103.28683449, -0.00027168, -344.2894483, -0.00090559, 0.4, 0.3, 0.003, 0.0, 0.0, 21027, 2)
    ops.limitCurve('ThreePoint', 11027, 1027, 0.0, 144.60910584, 0.01833728, 144.60910584, 0.05501183, 101.22637409, -2024.81927914, 0.05, 2, 0, 71027, 22027, 1, 3)
    ops.uniaxialMaterial('LimitState', 31027, 36.15227646, 9.509e-05, 108.45682938, 0.00028528, 361.5227646, 0.00095092, -36.15227646, -9.509e-05, -108.45682938, -0.00028528, -361.5227646, -0.00095092, 0.4, 0.3, 0.003, 0.0, 0.0, 11027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1027, 99999, 'P', 41027, 'Vy', 31027, 'Vz', 21027, 'My', 11027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171027, 71027, 171027, 1027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122027, 122027, 22027, 1027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171028, 13.85, 25.2, 3.0)
    ops.node(122028, 13.85, 25.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1028, 171028, 122028, 0.0625, 30540629.80366812, 12725262.41819505, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21028, 63.22969856, 0.00111261, 75.06955406, 0.00971128, 7.50695541, 0.04307984, -63.22969856, -0.00111261, -75.06955406, -0.00971128, -7.50695541, -0.04307984, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11028, 59.40619963, 0.00111261, 70.53009924, 0.00971128, 7.05300992, 0.04307984, -59.40619963, -0.00111261, -70.53009924, -0.00971128, -7.05300992, -0.04307984, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21028, 1028, 0.0, 91.56922767, 0.02225224, 91.56922767, 0.06675673, 64.09845937, -1361.21843388, 0.05, 2, 0, 71028, 22028, 2, 3)
    ops.uniaxialMaterial('LimitState', 41028, 22.89230692, 9.499e-05, 68.67692075, 0.00028496, 228.92306917, 0.00094985, -22.89230692, -9.499e-05, -68.67692075, -0.00028496, -228.92306917, -0.00094985, 0.4, 0.3, 0.003, 0.0, 0.0, 21028, 2)
    ops.limitCurve('ThreePoint', 11028, 1028, 0.0, 91.56922767, 0.02225224, 91.56922767, 0.06675673, 64.09845937, -1361.21843388, 0.05, 2, 0, 71028, 22028, 1, 3)
    ops.uniaxialMaterial('LimitState', 31028, 22.89230692, 9.499e-05, 68.67692075, 0.00028496, 228.92306917, 0.00094985, -22.89230692, -9.499e-05, -68.67692075, -0.00028496, -228.92306917, -0.00094985, 0.4, 0.3, 0.003, 0.0, 0.0, 11028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1028, 99999, 'P', 41028, 'Vy', 31028, 'Vz', 21028, 'My', 11028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171028, 71028, 171028, 1028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122028, 122028, 22028, 1028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.5, 0.0, 5.75)
    ops.node(123003, 8.5, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0625, 33180308.59191259, 13825128.57996358, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 60.27753609, 0.00117537, 71.17283633, 0.00959609, 7.11728363, 0.04659996, -60.27753609, -0.00117537, -71.17283633, -0.00959609, -7.11728363, -0.04659996, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 60.27753609, 0.00117537, 71.17283633, 0.00959609, 7.11728363, 0.04659996, -60.27753609, -0.00117537, -71.17283633, -0.00959609, -7.11728363, -0.04659996, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 104.94186235, 0.02350741, 104.94186235, 0.07052224, 73.45930365, -1418.69251957, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 26.23546559, 0.0001002, 78.70639676, 0.00030059, 262.35465588, 0.00100197, -26.23546559, -0.0001002, -78.70639676, -0.00030059, -262.35465588, -0.00100197, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 104.94186235, 0.02350741, 104.94186235, 0.07052224, 73.45930365, -1418.69251957, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 26.23546559, 0.0001002, 78.70639676, 0.00030059, 262.35465588, 0.00100197, -26.23546559, -0.0001002, -78.70639676, -0.00030059, -262.35465588, -0.00100197, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.85, 0.0, 5.75)
    ops.node(123004, 13.85, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 30732571.37929501, 12805238.07470626, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 43.89659964, 0.00120116, 52.53488535, 0.01242982, 5.25348854, 0.05554094, -43.89659964, -0.00120116, -52.53488535, -0.01242982, -5.25348854, -0.05554094, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 43.89659964, 0.00120116, 52.53488535, 0.01242982, 5.25348854, 0.05554094, -43.89659964, -0.00120116, -52.53488535, -0.01242982, -5.25348854, -0.05554094, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 96.0076795, 0.02402319, 96.0076795, 0.07206957, 67.20537565, -1445.02815716, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 24.00191988, 9.897e-05, 72.00575963, 0.0002969, 240.01919875, 0.00098967, -24.00191988, -9.897e-05, -72.00575963, -0.0002969, -240.01919875, -0.00098967, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 96.0076795, 0.02402319, 96.0076795, 0.07206957, 67.20537565, -1445.02815716, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 24.00191988, 9.897e-05, 72.00575963, 0.0002969, 240.01919875, 0.00098967, -24.00191988, -9.897e-05, -72.00575963, -0.0002969, -240.01919875, -0.00098967, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.2, 5.75)
    ops.node(123005, 0.0, 4.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 27774971.16689382, 11572904.65287242, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 40.69847688, 0.001193, 48.8696726, 0.01133739, 4.88696726, 0.04858713, -40.69847688, -0.001193, -48.8696726, -0.01133739, -4.88696726, -0.04858713, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 40.69847688, 0.001193, 48.8696726, 0.01133739, 4.88696726, 0.04858713, -40.69847688, -0.001193, -48.8696726, -0.01133739, -4.88696726, -0.04858713, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 85.26816334, 0.02385993, 85.26816334, 0.07157978, 59.68771434, -1310.74719873, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 21.31704083, 9.726e-05, 63.9511225, 0.00029177, 213.17040835, 0.00097256, -21.31704083, -9.726e-05, -63.9511225, -0.00029177, -213.17040835, -0.00097256, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 85.26816334, 0.02385993, 85.26816334, 0.07157978, 59.68771434, -1310.74719873, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 21.31704083, 9.726e-05, 63.9511225, 0.00029177, 213.17040835, 0.00097256, -21.31704083, -9.726e-05, -63.9511225, -0.00029177, -213.17040835, -0.00097256, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 3.15, 4.2, 5.75)
    ops.node(123006, 3.15, 4.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0875, 29920603.87423344, 12466918.2809306, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 115.76723495, 0.00086273, 137.8145328, 0.01054302, 13.78145328, 0.0401945, -115.76723495, -0.00086273, -137.8145328, -0.01054302, -13.78145328, -0.0401945, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 80.22852204, 0.00113668, 95.50764763, 0.00986207, 9.55076476, 0.03303904, -80.22852204, -0.00113668, -95.50764763, -0.00986207, -9.55076476, -0.03303904, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 125.02987211, 0.01725458, 125.02987211, 0.05176373, 87.52091048, -1708.48783918, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 31.25746803, 9.456e-05, 93.77240409, 0.00028368, 312.57468028, 0.00094558, -31.25746803, -9.456e-05, -93.77240409, -0.00028368, -312.57468028, -0.00094558, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 100.69526579, 0.02273367, 100.69526579, 0.06820101, 70.48668605, -1403.28471194, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 25.17381645, 7.615e-05, 75.52144934, 0.00022846, 251.73816447, 0.00076155, -25.17381645, -7.615e-05, -75.52144934, -0.00022846, -251.73816447, -0.00076155, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 8.5, 4.2, 5.75)
    ops.node(123007, 8.5, 4.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.175, 28494389.09857085, 11872662.12440452, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 243.97147037, 0.00067014, 293.10504074, 0.00909808, 29.31050407, 0.03616376, -243.97147037, -0.00067014, -293.10504074, -0.00909808, -29.31050407, -0.03616376, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 155.48153215, 0.00082785, 186.79405729, 0.00846454, 18.67940573, 0.02988629, -155.48153215, -0.00082785, -186.79405729, -0.00846454, -18.67940573, -0.02988629, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 210.83242277, 0.0134027, 210.83242277, 0.0402081, 147.58269594, -2174.92559257, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 52.70810569, 8.372e-05, 158.12431708, 0.00025115, 527.08105693, 0.00083715, -52.70810569, -8.372e-05, -158.12431708, -0.00025115, -527.08105693, -0.00083715, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 172.29083004, 0.01655696, 172.29083004, 0.04967087, 120.60358103, -1778.48247517, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 43.07270751, 6.841e-05, 129.21812253, 0.00020523, 430.72707511, 0.00068412, -43.07270751, -6.841e-05, -129.21812253, -0.00020523, -430.72707511, -0.00068412, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 13.85, 4.2, 5.75)
    ops.node(123008, 13.85, 4.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 36225502.4401664, 15093959.35006933, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 68.67330042, 0.00118837, 80.51591729, 0.00906395, 8.05159173, 0.05273699, -68.67330042, -0.00118837, -80.51591729, -0.00906395, -8.05159173, -0.05273699, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 65.0310871, 0.00118837, 76.24560926, 0.00906395, 7.62456093, 0.05273699, -65.0310871, -0.00118837, -76.24560926, -0.00906395, -7.62456093, -0.05273699, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 101.01153624, 0.02376736, 101.01153624, 0.07130209, 70.70807537, -1352.04561758, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 25.25288406, 8.834e-05, 75.75865218, 0.00026501, 252.52884059, 0.00088337, -25.25288406, -8.834e-05, -75.75865218, -0.00026501, -252.52884059, -0.00088337, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 101.01153624, 0.02376736, 101.01153624, 0.07130209, 70.70807537, -1352.04561758, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 25.25288406, 8.834e-05, 75.75865218, 0.00026501, 252.52884059, 0.00088337, -25.25288406, -8.834e-05, -75.75865218, -0.00026501, -252.52884059, -0.00088337, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.4, 5.75)
    ops.node(123009, 0.0, 8.4, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 34914939.33983225, 14547891.39159677, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 43.9897797, 0.00108053, 52.11761786, 0.01184987, 5.21176179, 0.06209759, -43.9897797, -0.00108053, -52.11761786, -0.01184987, -5.21176179, -0.06209759, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 43.9897797, 0.00108053, 52.11761786, 0.01184987, 5.21176179, 0.06209759, -43.9897797, -0.00108053, -52.11761786, -0.01184987, -5.21176179, -0.06209759, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 102.77841732, 0.02161066, 102.77841732, 0.06483199, 71.94489212, -1379.17952857, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 25.69460433, 9.326e-05, 77.08381299, 0.00027977, 256.9460433, 0.00093256, -25.69460433, -9.326e-05, -77.08381299, -0.00027977, -256.9460433, -0.00093256, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 102.77841732, 0.02161066, 102.77841732, 0.06483199, 71.94489212, -1379.17952857, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 25.69460433, 9.326e-05, 77.08381299, 0.00027977, 256.9460433, 0.00093256, -25.69460433, -9.326e-05, -77.08381299, -0.00027977, -256.9460433, -0.00093256, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 3.15, 8.4, 5.75)
    ops.node(123010, 3.15, 8.4, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0875, 32789356.50358199, 13662231.87649249, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 115.70324798, 0.00084972, 137.30839715, 0.01000493, 13.73083971, 0.04573349, -115.70324798, -0.00084972, -137.30839715, -0.01000493, -13.73083971, -0.04573349, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 80.24094563, 0.00111639, 95.22425535, 0.0093685, 9.52242553, 0.03729559, -80.24094563, -0.00111639, -95.22425535, -0.0093685, -9.52242553, -0.03729559, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 129.57949589, 0.0169944, 129.57949589, 0.05098321, 90.70564712, -1606.86216678, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 32.39487397, 8.943e-05, 97.18462192, 0.00026828, 323.94873973, 0.00089425, -32.39487397, -8.943e-05, -97.18462192, -0.00026828, -323.94873973, -0.00089425, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 97.85350501, 0.02232786, 97.85350501, 0.06698359, 68.49745351, -1331.51966678, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 24.46337625, 6.753e-05, 73.39012876, 0.00020259, 244.63376253, 0.00067531, -24.46337625, -6.753e-05, -73.39012876, -0.00020259, -244.63376253, -0.00067531, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.5, 8.4, 5.75)
    ops.node(123011, 8.5, 8.4, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.175, 31659380.94517132, 13191408.72715472, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 246.79129305, 0.00069229, 295.23093613, 0.00850372, 29.52309361, 0.03455917, -246.79129305, -0.00069229, -295.23093613, -0.00850372, -29.52309361, -0.03455917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 167.29487905, 0.00087502, 200.13114377, 0.00802752, 20.01311438, 0.02916789, -167.29487905, -0.00087502, -200.13114377, -0.00802752, -20.01311438, -0.02916789, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 220.31194041, 0.01384589, 220.31194041, 0.04153766, 154.21835828, -1904.02343884, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 55.0779851, 7.873e-05, 165.2339553, 0.0002362, 550.77985102, 0.00078734, -55.0779851, -7.873e-05, -165.2339553, -0.0002362, -550.77985102, -0.00078734, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 168.9717475, 0.01750046, 168.9717475, 0.05250138, 118.28022325, -1605.71482572, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 42.24293687, 6.039e-05, 126.72881062, 0.00018116, 422.42936875, 0.00060386, -42.24293687, -6.039e-05, -126.72881062, -0.00018116, -422.42936875, -0.00060386, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 13.85, 8.4, 5.75)
    ops.node(123012, 13.85, 8.4, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 32553738.24122203, 13564057.60050918, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 65.95868508, 0.00117671, 78.01427463, 0.01071769, 7.80142746, 0.04709487, -65.95868508, -0.00117671, -78.01427463, -0.01071769, -7.80142746, -0.04709487, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 62.52192168, 0.00117671, 73.94935728, 0.01071769, 7.39493573, 0.04709487, -62.52192168, -0.00117671, -73.94935728, -0.01071769, -7.39493573, -0.04709487, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 106.93589307, 0.02353422, 106.93589307, 0.07060266, 74.85512515, -1506.06659218, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 26.73397327, 0.00010407, 80.20191981, 0.0003122, 267.33973268, 0.00104066, -26.73397327, -0.00010407, -80.20191981, -0.0003122, -267.33973268, -0.00104066, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 106.93589307, 0.02353422, 106.93589307, 0.07060266, 74.85512515, -1506.06659218, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 26.73397327, 0.00010407, 80.20191981, 0.0003122, 267.33973268, 0.00104066, -26.73397327, -0.00010407, -80.20191981, -0.0003122, -267.33973268, -0.00104066, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 12.6, 5.75)
    ops.node(123013, 0.0, 12.6, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 29433028.67200749, 12263761.94666979, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 44.91464697, 0.0010892, 53.83993582, 0.01076345, 5.38399358, 0.05108532, -44.91464697, -0.0010892, -53.83993582, -0.01076345, -5.38399358, -0.05108532, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 44.91464697, 0.0010892, 53.83993582, 0.01076345, 5.38399358, 0.05108532, -44.91464697, -0.0010892, -53.83993582, -0.01076345, -5.38399358, -0.05108532, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 87.80965812, 0.02178397, 87.80965812, 0.06535191, 61.46676069, -1271.41270746, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 21.95241453, 9.451e-05, 65.85724359, 0.00028354, 219.52414531, 0.00094513, -21.95241453, -9.451e-05, -65.85724359, -0.00028354, -219.52414531, -0.00094513, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 87.80965812, 0.02178397, 87.80965812, 0.06535191, 61.46676069, -1271.41270746, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 21.95241453, 9.451e-05, 65.85724359, 0.00028354, 219.52414531, 0.00094513, -21.95241453, -9.451e-05, -65.85724359, -0.00028354, -219.52414531, -0.00094513, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 3.15, 12.6, 5.75)
    ops.node(123014, 3.15, 12.6, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0875, 30170868.96795686, 12571195.40331536, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 114.75380823, 0.00087518, 136.65051884, 0.01060149, 13.66505188, 0.04119617, -114.75380823, -0.00087518, -136.65051884, -0.01060149, -13.66505188, -0.04119617, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 79.39451418, 0.00116065, 94.54415259, 0.00992751, 9.45441526, 0.03384173, -79.39451418, -0.00116065, -94.54415259, -0.00992751, -9.45441526, -0.03384173, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 126.4847257, 0.01750365, 126.4847257, 0.05251094, 88.53930799, -1728.70712622, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 31.62118143, 9.487e-05, 94.86354428, 0.0002846, 316.21181426, 0.00094865, -31.62118143, -9.487e-05, -94.86354428, -0.0002846, -316.21181426, -0.00094865, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 101.368093, 0.02321291, 101.368093, 0.06963872, 70.9576651, -1410.433301, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 25.34202325, 7.603e-05, 76.02606975, 0.00022808, 253.4202325, 0.00076027, -25.34202325, -7.603e-05, -76.02606975, -0.00022808, -253.4202325, -0.00076027, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 8.5, 12.6, 5.75)
    ops.node(123015, 8.5, 12.6, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.175, 31286074.76146504, 13035864.48394377, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 251.76127703, 0.00066508, 301.39883538, 0.00999068, 30.13988354, 0.03566687, -251.76127703, -0.00066508, -301.39883538, -0.00999068, -30.13988354, -0.03566687, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 172.03390983, 0.00081934, 205.95232389, 0.00935829, 20.59523239, 0.03019093, -172.03390983, -0.00081934, -205.95232389, -0.00935829, -20.59523239, -0.03019093, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 227.03483687, 0.01330159, 227.03483687, 0.03990476, 158.92438581, -2124.70069775, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 56.75870922, 8.21e-05, 170.27612765, 0.00024631, 567.58709217, 0.00082105, -56.75870922, -8.21e-05, -170.27612765, -0.00024631, -567.58709217, -0.00082105, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 186.53848617, 0.01638675, 186.53848617, 0.04916025, 130.57694032, -1746.64839366, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 46.63462154, 6.746e-05, 139.90386463, 0.00020238, 466.34621543, 0.0006746, -46.63462154, -6.746e-05, -139.90386463, -0.00020238, -466.34621543, -0.0006746, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 13.85, 12.6, 5.75)
    ops.node(123016, 13.85, 12.6, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 30493132.69180626, 12705471.95491927, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 68.30720765, 0.00120635, 80.94053096, 0.00935895, 8.0940531, 0.04071466, -68.30720765, -0.00120635, -80.94053096, -0.00935895, -8.0940531, -0.04071466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 64.28160573, 0.00120635, 76.17039954, 0.00935895, 7.61703995, 0.04071466, -64.28160573, -0.00120635, -76.17039954, -0.00935895, -7.61703995, -0.04071466, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 95.20730386, 0.02412703, 95.20730386, 0.0723811, 66.6451127, -1386.12907326, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 23.80182596, 9.891e-05, 71.40547789, 0.00029674, 238.01825964, 0.00098913, -23.80182596, -9.891e-05, -71.40547789, -0.00029674, -238.01825964, -0.00098913, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 95.20730386, 0.02412703, 95.20730386, 0.0723811, 66.6451127, -1386.12907326, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 23.80182596, 9.891e-05, 71.40547789, 0.00029674, 238.01825964, 0.00098913, -23.80182596, -9.891e-05, -71.40547789, -0.00029674, -238.01825964, -0.00098913, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 16.8, 5.75)
    ops.node(123017, 0.0, 16.8, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 28169917.09349846, 11737465.45562436, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 43.01747166, 0.00108873, 51.60224742, 0.01026639, 5.16022474, 0.047495, -43.01747166, -0.00108873, -51.60224742, -0.01026639, -5.16022474, -0.047495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 43.01747166, 0.00108873, 51.60224742, 0.01026639, 5.16022474, 0.047495, -43.01747166, -0.00108873, -51.60224742, -0.01026639, -5.16022474, -0.047495, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 79.86357993, 0.02177453, 79.86357993, 0.06532359, 55.90450595, -1210.05464647, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 19.96589498, 8.981e-05, 59.89768495, 0.00026944, 199.65894983, 0.00089815, -19.96589498, -8.981e-05, -59.89768495, -0.00026944, -199.65894983, -0.00089815, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 79.86357993, 0.02177453, 79.86357993, 0.06532359, 55.90450595, -1210.05464647, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 19.96589498, 8.981e-05, 59.89768495, 0.00026944, 199.65894983, 0.00089815, -19.96589498, -8.981e-05, -59.89768495, -0.00026944, -199.65894983, -0.00089815, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 3.15, 16.8, 5.75)
    ops.node(123018, 3.15, 16.8, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0875, 35409311.70032092, 14753879.87513372, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 119.34929279, 0.00086107, 140.68418679, 0.00932235, 14.06841868, 0.04919221, -119.34929279, -0.00086107, -140.68418679, -0.00932235, -14.06841868, -0.04919221, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 82.83300719, 0.00112885, 97.64024557, 0.00875549, 9.76402456, 0.0399196, -82.83300719, -0.00112885, -97.64024557, -0.00875549, -9.76402456, -0.0399196, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 137.42308502, 0.01722131, 137.42308502, 0.05166393, 96.19615952, -1597.63922129, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 34.35577126, 8.782e-05, 103.06731377, 0.00026346, 343.55771255, 0.00087821, -34.35577126, -8.782e-05, -103.06731377, -0.00026346, -343.55771255, -0.00087821, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 101.50885133, 0.02257699, 101.50885133, 0.06773098, 71.05619593, -1325.52091845, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 25.37721283, 6.487e-05, 76.1316385, 0.00019461, 253.77212832, 0.0006487, -25.37721283, -6.487e-05, -76.1316385, -0.00019461, -253.77212832, -0.0006487, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 8.5, 16.8, 5.75)
    ops.node(123019, 8.5, 16.8, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.175, 30898239.49953636, 12874266.45814015, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 253.8403545, 0.00067125, 304.10169207, 0.00877542, 30.41016921, 0.03404257, -253.8403545, -0.00067125, -304.10169207, -0.00877542, -30.41016921, -0.03404257, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 173.4630192, 0.00082752, 207.8093444, 0.00824806, 20.78093444, 0.02874883, -173.4630192, -0.00082752, -207.8093444, -0.00824806, -20.78093444, -0.02874883, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 219.00654971, 0.01342501, 219.00654971, 0.04027502, 153.3045848, -1992.9122923, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 54.75163743, 8.02e-05, 164.25491229, 0.00024059, 547.51637428, 0.00080196, -54.75163743, -8.02e-05, -164.25491229, -0.00024059, -547.51637428, -0.00080196, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 170.23130742, 0.01655036, 170.23130742, 0.04965107, 119.1619152, -1662.70028778, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 42.55782686, 6.234e-05, 127.67348057, 0.00018701, 425.57826855, 0.00062335, -42.55782686, -6.234e-05, -127.67348057, -0.00018701, -425.57826855, -0.00062335, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 13.85, 16.8, 5.75)
    ops.node(123020, 13.85, 16.8, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 31191729.16530515, 12996553.81887715, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 68.66274092, 0.00114866, 81.33370706, 0.01133052, 8.13337071, 0.04446438, -68.66274092, -0.00114866, -81.33370706, -0.01133052, -8.13337071, -0.04446438, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 64.35058635, 0.00114866, 76.22579101, 0.01133052, 7.6225791, 0.04446438, -64.35058635, -0.00114866, -76.22579101, -0.01133052, -7.6225791, -0.04446438, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 108.43219209, 0.02297319, 108.43219209, 0.06891958, 75.90253446, -1624.82702512, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 27.10804802, 0.00011013, 81.32414407, 0.00033039, 271.08048022, 0.0011013, -27.10804802, -0.00011013, -81.32414407, -0.00033039, -271.08048022, -0.0011013, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 108.43219209, 0.02297319, 108.43219209, 0.06891958, 75.90253446, -1624.82702512, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 27.10804802, 0.00011013, 81.32414407, 0.00033039, 271.08048022, 0.0011013, -27.10804802, -0.00011013, -81.32414407, -0.00033039, -271.08048022, -0.0011013, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 0.0, 21.0, 5.75)
    ops.node(123021, 0.0, 21.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 30328327.43030292, 12636803.09595955, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 43.61446144, 0.00107703, 52.22926789, 0.01012027, 5.22292679, 0.05243285, -43.61446144, -0.00107703, -52.22926789, -0.01012027, -5.22292679, -0.05243285, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 43.61446144, 0.00107703, 52.22926789, 0.01012027, 5.22292679, 0.05243285, -43.61446144, -0.00107703, -52.22926789, -0.01012027, -5.22292679, -0.05243285, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 79.39233194, 0.02154064, 79.39233194, 0.06462192, 55.57463236, -1160.33618667, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 19.84808299, 8.293e-05, 59.54424896, 0.00024879, 198.48082985, 0.00082931, -19.84808299, -8.293e-05, -59.54424896, -0.00024879, -198.48082985, -0.00082931, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 79.39233194, 0.02154064, 79.39233194, 0.06462192, 55.57463236, -1160.33618667, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 19.84808299, 8.293e-05, 59.54424896, 0.00024879, 198.48082985, 0.00082931, -19.84808299, -8.293e-05, -59.54424896, -0.00024879, -198.48082985, -0.00082931, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 3.15, 21.0, 5.75)
    ops.node(123022, 3.15, 21.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0875, 29991180.37062142, 12496325.15442559, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 114.6029392, 0.00083439, 136.48462073, 0.01108682, 13.64846207, 0.04129005, -114.6029392, -0.00083439, -136.48462073, -0.01108682, -13.64846207, -0.04129005, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 79.63235169, 0.00108622, 94.83693346, 0.01032731, 9.48369335, 0.03393555, -79.63235169, -0.00108622, -94.83693346, -0.01032731, -9.48369335, -0.03393555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 126.88608177, 0.01668779, 126.88608177, 0.05006338, 88.82025724, -1752.76769008, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 31.72152044, 9.574e-05, 95.16456132, 0.00028721, 317.21520441, 0.00095737, -31.72152044, -9.574e-05, -95.16456132, -0.00028721, -317.21520441, -0.00095737, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 106.02756879, 0.02172436, 106.02756879, 0.06517308, 74.21929816, -1425.94570964, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 26.5068922, 8e-05, 79.5206766, 0.00024, 265.06892198, 0.00079999, -26.5068922, -8e-05, -79.5206766, -0.00024, -265.06892198, -0.00079999, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 8.5, 21.0, 5.75)
    ops.node(123023, 8.5, 21.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.175, 30639966.19199067, 12766652.57999611, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 243.8818521, 0.00065766, 292.29761209, 0.01140119, 29.22976121, 0.04164478, -243.8818521, -0.00065766, -292.29761209, -0.01140119, -29.22976121, -0.04164478, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 155.72511245, 0.00080886, 186.6398755, 0.01054375, 18.66398755, 0.03448072, -155.72511245, -0.00080886, -186.6398755, -0.01054375, -18.66398755, -0.03448072, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 236.57679153, 0.01315312, 236.57679153, 0.03945937, 165.60375407, -2478.39945264, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 59.14419788, 8.736e-05, 177.43259365, 0.00026208, 591.44197883, 0.0008736, -59.14419788, -8.736e-05, -177.43259365, -0.00026208, -591.44197883, -0.0008736, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 192.53379988, 0.01617724, 192.53379988, 0.04853173, 134.77365992, -1969.1635104, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 48.13344997, 7.11e-05, 144.40034991, 0.00021329, 481.3344997, 0.00071096, -48.13344997, -7.11e-05, -144.40034991, -0.00021329, -481.3344997, -0.00071096, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 13.85, 21.0, 5.75)
    ops.node(123024, 13.85, 21.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 33025542.08895647, 13760642.5370652, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 69.66497942, 0.00115582, 82.33600126, 0.01123386, 8.23360013, 0.04866508, -69.66497942, -0.00115582, -82.33600126, -0.01123386, -8.23360013, -0.04866508, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 65.3468743, 0.00115582, 77.23249715, 0.01123386, 7.72324972, 0.04866508, -65.3468743, -0.00115582, -77.23249715, -0.01123386, -7.72324972, -0.04866508, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 112.34091155, 0.02311632, 112.34091155, 0.06934895, 78.63863809, -1618.65422842, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 28.08522789, 0.00010776, 84.25568366, 0.00032329, 280.85227888, 0.00107764, -28.08522789, -0.00010776, -84.25568366, -0.00032329, -280.85227888, -0.00107764, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 112.34091155, 0.02311632, 112.34091155, 0.06934895, 78.63863809, -1618.65422842, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 28.08522789, 0.00010776, 84.25568366, 0.00032329, 280.85227888, 0.00107764, -28.08522789, -0.00010776, -84.25568366, -0.00032329, -280.85227888, -0.00107764, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172025, 0.0, 25.2, 5.75)
    ops.node(123025, 0.0, 25.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2025, 172025, 123025, 0.0625, 32380365.31471355, 13491818.88113065, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22025, 35.881033, 0.00104488, 43.02157566, 0.01156339, 4.30215757, 0.06518317, -35.881033, -0.00104488, -43.02157566, -0.01156339, -4.30215757, -0.06518317, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12025, 35.881033, 0.00104488, 43.02157566, 0.01156339, 4.30215757, 0.06518317, -35.881033, -0.00104488, -43.02157566, -0.01156339, -4.30215757, -0.06518317, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22025, 2025, 0.0, 87.26711557, 0.02089757, 87.26711557, 0.06269272, 61.0869809, -1285.64383918, 0.05, 2, 0, 72025, 23025, 2, 3)
    ops.uniaxialMaterial('LimitState', 42025, 21.81677889, 8.538e-05, 65.45033668, 0.00025614, 218.16778892, 0.0008538, -21.81677889, -8.538e-05, -65.45033668, -0.00025614, -218.16778892, -0.0008538, 0.4, 0.3, 0.003, 0.0, 0.0, 22025, 2)
    ops.limitCurve('ThreePoint', 12025, 2025, 0.0, 87.26711557, 0.02089757, 87.26711557, 0.06269272, 61.0869809, -1285.64383918, 0.05, 2, 0, 72025, 23025, 1, 3)
    ops.uniaxialMaterial('LimitState', 32025, 21.81677889, 8.538e-05, 65.45033668, 0.00025614, 218.16778892, 0.0008538, -21.81677889, -8.538e-05, -65.45033668, -0.00025614, -218.16778892, -0.0008538, 0.4, 0.3, 0.003, 0.0, 0.0, 12025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2025, 99999, 'P', 42025, 'Vy', 32025, 'Vz', 22025, 'My', 12025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172025, 72025, 172025, 2025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123025, 123025, 23025, 2025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172026, 3.15, 25.2, 5.75)
    ops.node(123026, 3.15, 25.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2026, 172026, 123026, 0.0625, 30602999.13451618, 12751249.63938174, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22026, 51.24720669, 0.00112966, 61.0328584, 0.01079567, 6.10328584, 0.04761615, -51.24720669, -0.00112966, -61.0328584, -0.01079567, -6.10328584, -0.04761615, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12026, 51.24720669, 0.00112966, 61.0328584, 0.01079567, 6.10328584, 0.04761615, -51.24720669, -0.00112966, -61.0328584, -0.01079567, -6.10328584, -0.04761615, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22026, 2026, 0.0, 97.60686208, 0.02259314, 97.60686208, 0.06777942, 68.32480346, -1406.61073966, 0.05, 2, 0, 72026, 23026, 2, 3)
    ops.uniaxialMaterial('LimitState', 42026, 24.40171552, 0.00010104, 73.20514656, 0.00030313, 244.0171552, 0.00101042, -24.40171552, -0.00010104, -73.20514656, -0.00030313, -244.0171552, -0.00101042, 0.4, 0.3, 0.003, 0.0, 0.0, 22026, 2)
    ops.limitCurve('ThreePoint', 12026, 2026, 0.0, 97.60686208, 0.02259314, 97.60686208, 0.06777942, 68.32480346, -1406.61073966, 0.05, 2, 0, 72026, 23026, 1, 3)
    ops.uniaxialMaterial('LimitState', 32026, 24.40171552, 0.00010104, 73.20514656, 0.00030313, 244.0171552, 0.00101042, -24.40171552, -0.00010104, -73.20514656, -0.00030313, -244.0171552, -0.00101042, 0.4, 0.3, 0.003, 0.0, 0.0, 12026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2026, 99999, 'P', 42026, 'Vy', 32026, 'Vz', 22026, 'My', 12026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172026, 72026, 172026, 2026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123026, 123026, 23026, 2026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172027, 8.5, 25.2, 5.75)
    ops.node(123027, 8.5, 25.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2027, 172027, 123027, 0.0625, 27276067.01378705, 11365027.92241127, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22027, 72.84084722, 0.00121866, 85.96111526, 0.00868592, 8.59611153, 0.02726303, -72.84084722, -0.00121866, -85.96111526, -0.00868592, -8.59611153, -0.02726303, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12027, 72.84084722, 0.00121866, 85.96111526, 0.00868592, 8.59611153, 0.02726303, -72.84084722, -0.00121866, -85.96111526, -0.00868592, -8.59611153, -0.02726303, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22027, 2027, 0.0, 67.11298844, 0.02437315, 67.11298844, 0.07311946, 46.97909191, -1282.28508472, 0.05, 2, 0, 72027, 23027, 2, 3)
    ops.uniaxialMaterial('LimitState', 42027, 16.77824711, 7.795e-05, 50.33474133, 0.00023385, 167.78247109, 0.00077949, -16.77824711, -7.795e-05, -50.33474133, -0.00023385, -167.78247109, -0.00077949, 0.4, 0.3, 0.003, 0.0, 0.0, 22027, 2)
    ops.limitCurve('ThreePoint', 12027, 2027, 0.0, 67.11298844, 0.02437315, 67.11298844, 0.07311946, 46.97909191, -1282.28508472, 0.05, 2, 0, 72027, 23027, 1, 3)
    ops.uniaxialMaterial('LimitState', 32027, 16.77824711, 7.795e-05, 50.33474133, 0.00023385, 167.78247109, 0.00077949, -16.77824711, -7.795e-05, -50.33474133, -0.00023385, -167.78247109, -0.00077949, 0.4, 0.3, 0.003, 0.0, 0.0, 12027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2027, 99999, 'P', 42027, 'Vy', 32027, 'Vz', 22027, 'My', 12027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172027, 72027, 172027, 2027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123027, 123027, 23027, 2027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172028, 13.85, 25.2, 5.75)
    ops.node(123028, 13.85, 25.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2028, 172028, 123028, 0.0625, 32769380.76241527, 13653908.65100636, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22028, 43.90400444, 0.00108651, 52.33338987, 0.01251437, 5.23333899, 0.05943838, -43.90400444, -0.00108651, -52.33338987, -0.01251437, -5.23333899, -0.05943838, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12028, 43.90400444, 0.00108651, 52.33338987, 0.01251437, 5.23333899, 0.05943838, -43.90400444, -0.00108651, -52.33338987, -0.01251437, -5.23333899, -0.05943838, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22028, 2028, 0.0, 99.32163157, 0.02173019, 99.32163157, 0.06519056, 69.5251421, -1414.97299459, 0.05, 2, 0, 72028, 23028, 2, 3)
    ops.uniaxialMaterial('LimitState', 42028, 24.83040789, 9.602e-05, 74.49122368, 0.00028806, 248.30407894, 0.0009602, -24.83040789, -9.602e-05, -74.49122368, -0.00028806, -248.30407894, -0.0009602, 0.4, 0.3, 0.003, 0.0, 0.0, 22028, 2)
    ops.limitCurve('ThreePoint', 12028, 2028, 0.0, 99.32163157, 0.02173019, 99.32163157, 0.06519056, 69.5251421, -1414.97299459, 0.05, 2, 0, 72028, 23028, 1, 3)
    ops.uniaxialMaterial('LimitState', 32028, 24.83040789, 9.602e-05, 74.49122368, 0.00028806, 248.30407894, 0.0009602, -24.83040789, -9.602e-05, -74.49122368, -0.00028806, -248.30407894, -0.0009602, 0.4, 0.3, 0.003, 0.0, 0.0, 12028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2028, 99999, 'P', 42028, 'Vy', 32028, 'Vz', 22028, 'My', 12028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172028, 72028, 172028, 2028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123028, 123028, 23028, 2028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.5, 0.0, 8.5)
    ops.node(124003, 8.5, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0625, 30044257.62528654, 12518440.67720272, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 37.42190668, 0.00115663, 45.04134962, 0.01331709, 4.50413496, 0.06130337, -37.42190668, -0.00115663, -45.04134962, -0.01331709, -4.50413496, -0.06130337, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 37.42190668, 0.00115663, 45.04134962, 0.01331709, 4.50413496, 0.06130337, -37.42190668, -0.00115663, -45.04134962, -0.01331709, -4.50413496, -0.06130337, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 90.11500428, 0.02313258, 90.11500428, 0.06939774, 63.08050299, -1480.31679576, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 22.52875107, 9.502e-05, 67.58625321, 0.00028506, 225.28751069, 0.00095021, -22.52875107, -9.502e-05, -67.58625321, -0.00028506, -225.28751069, -0.00095021, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 90.11500428, 0.02313258, 90.11500428, 0.06939774, 63.08050299, -1480.31679576, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 22.52875107, 9.502e-05, 67.58625321, 0.00028506, 225.28751069, 0.00095021, -22.52875107, -9.502e-05, -67.58625321, -0.00028506, -225.28751069, -0.00095021, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.85, 0.0, 8.5)
    ops.node(124004, 13.85, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 31565896.55974474, 13152456.89989364, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 29.5709818, 0.0009595, 35.64245918, 0.01131327, 3.56424592, 0.0690239, -29.5709818, -0.0009595, -35.64245918, -0.01131327, -3.56424592, -0.0690239, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 29.5709818, 0.0009595, 35.64245918, 0.01131327, 3.56424592, 0.0690239, -29.5709818, -0.0009595, -35.64245918, -0.01131327, -3.56424592, -0.0690239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 70.01117002, 0.01918994, 70.01117002, 0.05756982, 49.00781902, -1253.28931176, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 17.50279251, 7.026e-05, 52.50837752, 0.00021079, 175.02792505, 0.00070264, -17.50279251, -7.026e-05, -52.50837752, -0.00021079, -175.02792505, -0.00070264, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 70.01117002, 0.01918994, 70.01117002, 0.05756982, 49.00781902, -1253.28931176, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 17.50279251, 7.026e-05, 52.50837752, 0.00021079, 175.02792505, 0.00070264, -17.50279251, -7.026e-05, -52.50837752, -0.00021079, -175.02792505, -0.00070264, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.2, 8.5)
    ops.node(124005, 0.0, 4.2, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 27729973.64045276, 11554155.68352198, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 27.57526309, 0.00110108, 33.51778084, 0.01467137, 3.35177808, 0.06806763, -27.57526309, -0.00110108, -33.51778084, -0.01467137, -3.35177808, -0.06806763, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 27.57526309, 0.00110108, 33.51778084, 0.01467137, 3.35177808, 0.06806763, -27.57526309, -0.00110108, -33.51778084, -0.01467137, -3.35177808, -0.06806763, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 79.19624647, 0.02202156, 79.19624647, 0.06606468, 55.43737253, -1755.17668174, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 19.79906162, 9.048e-05, 59.39718486, 0.00027143, 197.99061619, 0.00090477, -19.79906162, -9.048e-05, -59.39718486, -0.00027143, -197.99061619, -0.00090477, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 79.19624647, 0.02202156, 79.19624647, 0.06606468, 55.43737253, -1755.17668174, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 19.79906162, 9.048e-05, 59.39718486, 0.00027143, 197.99061619, 0.00090477, -19.79906162, -9.048e-05, -59.39718486, -0.00027143, -197.99061619, -0.00090477, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 3.15, 4.2, 8.5)
    ops.node(124006, 3.15, 4.2, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0875, 31965593.52345823, 13318997.30144093, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 84.99089296, 0.0008103, 101.97109468, 0.01244557, 10.19710947, 0.05785602, -84.99089296, -0.0008103, -101.97109468, -0.01244557, -10.19710947, -0.05785602, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 58.2861674, 0.00106074, 69.93107247, 0.01154826, 6.99310725, 0.04704316, -58.2861674, -0.00106074, -69.93107247, -0.01154826, -6.99310725, -0.04704316, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 116.77543373, 0.01620593, 116.77543373, 0.0486178, 81.74280361, -1596.51313108, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 29.19385843, 8.267e-05, 87.58157529, 0.000248, 291.93858431, 0.00082666, -29.19385843, -8.267e-05, -87.58157529, -0.000248, -291.93858431, -0.00082666, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 92.92750577, 0.02121473, 92.92750577, 0.06364419, 65.04925404, -1148.95262472, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 23.23187644, 6.578e-05, 69.69562933, 0.00019735, 232.31876442, 0.00065784, -23.23187644, -6.578e-05, -69.69562933, -0.00019735, -232.31876442, -0.00065784, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 8.5, 4.2, 8.5)
    ops.node(124007, 8.5, 4.2, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.175, 30643008.21673224, 12767920.0903051, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 178.20065173, 0.00062772, 215.11009312, 0.01307859, 21.51100931, 0.05051843, -178.20065173, -0.00062772, -215.11009312, -0.01307859, -21.51100931, -0.05051843, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 111.12562955, 0.00077192, 134.14229571, 0.01205385, 13.41422957, 0.04168645, -111.12562955, -0.00077192, -134.14229571, -0.01205385, -13.41422957, -0.04168645, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 215.55598515, 0.01255447, 215.55598515, 0.03766341, 150.88918961, -2542.31554302, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 53.88899629, 7.959e-05, 161.66698887, 0.00023877, 538.88996288, 0.0007959, -53.88899629, -7.959e-05, -161.66698887, -0.00023877, -538.88996288, -0.0007959, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 173.49314412, 0.01543832, 173.49314412, 0.04631495, 121.44520088, -1751.61083068, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 43.37328603, 6.406e-05, 130.11985809, 0.00019218, 433.73286029, 0.00064059, -43.37328603, -6.406e-05, -130.11985809, -0.00019218, -433.73286029, -0.00064059, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 13.85, 4.2, 8.5)
    ops.node(124008, 13.85, 4.2, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 31159251.63887655, 12983021.51619856, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 37.50260317, 0.00102958, 45.0378226, 0.01079757, 4.50378226, 0.0605454, -37.50260317, -0.00102958, -45.0378226, -0.01079757, -4.50378226, -0.0605454, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 37.50260317, 0.00102958, 45.0378226, 0.01079757, 4.50378226, 0.0605454, -37.50260317, -0.00102958, -45.0378226, -0.01079757, -4.50378226, -0.0605454, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 77.84063935, 0.02059163, 77.84063935, 0.06177488, 54.48844755, -1146.78667535, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 19.46015984, 7.914e-05, 58.38047951, 0.00023742, 194.60159838, 0.00079142, -19.46015984, -7.914e-05, -58.38047951, -0.00023742, -194.60159838, -0.00079142, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 77.84063935, 0.02059163, 77.84063935, 0.06177488, 54.48844755, -1146.78667535, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 19.46015984, 7.914e-05, 58.38047951, 0.00023742, 194.60159838, 0.00079142, -19.46015984, -7.914e-05, -58.38047951, -0.00023742, -194.60159838, -0.00079142, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.4, 8.5)
    ops.node(124009, 0.0, 8.4, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 30773524.16792804, 12822301.73663668, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 30.1994748, 0.00104027, 36.4719431, 0.01147047, 3.64719431, 0.06819487, -30.1994748, -0.00104027, -36.4719431, -0.01147047, -3.64719431, -0.06819487, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 30.1994748, 0.00104027, 36.4719431, 0.01147047, 3.64719431, 0.06819487, -30.1994748, -0.00104027, -36.4719431, -0.01147047, -3.64719431, -0.06819487, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 72.00558562, 0.02080548, 72.00558562, 0.06241645, 50.40390993, -1272.48201966, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 18.0013964, 7.413e-05, 54.00418921, 0.00022238, 180.01396405, 0.00074127, -18.0013964, -7.413e-05, -54.00418921, -0.00022238, -180.01396405, -0.00074127, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 72.00558562, 0.02080548, 72.00558562, 0.06241645, 50.40390993, -1272.48201966, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 18.0013964, 7.413e-05, 54.00418921, 0.00022238, 180.01396405, 0.00074127, -18.0013964, -7.413e-05, -54.00418921, -0.00022238, -180.01396405, -0.00074127, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 3.15, 8.4, 8.5)
    ops.node(124010, 3.15, 8.4, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0875, 30464840.46705861, 12693683.52794109, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 81.73028532, 0.00082655, 98.38278125, 0.01197841, 9.83827812, 0.05532954, -81.73028532, -0.00082655, -98.38278125, -0.01197841, -9.83827812, -0.05532954, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 55.78375668, 0.00110366, 67.14966318, 0.01115546, 6.71496632, 0.04504071, -55.78375668, -0.00110366, -67.14966318, -0.01115546, -6.71496632, -0.04504071, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 109.56351568, 0.01653092, 109.56351568, 0.04959275, 76.69446098, -1481.01182217, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 27.39087892, 8.138e-05, 82.17263676, 0.00024414, 273.90878921, 0.00081381, -27.39087892, -8.138e-05, -82.17263676, -0.00024414, -273.90878921, -0.00081381, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 80.53959533, 0.0220732, 80.53959533, 0.06621961, 56.37771673, -1081.04025156, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 20.13489883, 5.982e-05, 60.40469649, 0.00017947, 201.34898831, 0.00059823, -20.13489883, -5.982e-05, -60.40469649, -0.00017947, -201.34898831, -0.00059823, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.5, 8.4, 8.5)
    ops.node(124011, 8.5, 8.4, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.175, 31413547.41988742, 13088978.09161976, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 185.38173562, 0.00064698, 223.34382059, 0.01066697, 22.33438206, 0.04207379, -185.38173562, -0.00064698, -223.34382059, -0.01066697, -22.33438206, -0.04207379, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 124.86152515, 0.00080402, 150.43040772, 0.00997878, 15.04304077, 0.03546103, -124.86152515, -0.00080402, -150.43040772, -0.00997878, -15.04304077, -0.03546103, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 198.2355336, 0.01293967, 198.2355336, 0.038819, 138.76487352, -1749.69379065, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 49.5588834, 7.14e-05, 148.6766502, 0.0002142, 495.58883401, 0.00071399, -49.5588834, -7.14e-05, -148.6766502, -0.0002142, -495.58883401, -0.00071399, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 162.14288923, 0.01608034, 162.14288923, 0.04824102, 113.50002246, -1284.34955869, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 40.53572231, 5.84e-05, 121.60716692, 0.0001752, 405.35722307, 0.00058399, -40.53572231, -5.84e-05, -121.60716692, -0.0001752, -405.35722307, -0.00058399, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 13.85, 8.4, 8.5)
    ops.node(124012, 13.85, 8.4, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 34990466.72894374, 14579361.13705989, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 37.83186306, 0.00105007, 44.93591127, 0.01051747, 4.49359113, 0.06523324, -37.83186306, -0.00105007, -44.93591127, -0.01051747, -4.49359113, -0.06523324, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 37.83186306, 0.00105007, 44.93591127, 0.01051747, 4.49359113, 0.06523324, -37.83186306, -0.00105007, -44.93591127, -0.01051747, -4.49359113, -0.06523324, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 88.16131591, 0.02100141, 88.16131591, 0.06300424, 61.71292114, -1159.72518873, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 22.04032898, 7.982e-05, 66.12098693, 0.00023946, 220.40328978, 0.0007982, -22.04032898, -7.982e-05, -66.12098693, -0.00023946, -220.40328978, -0.0007982, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 88.16131591, 0.02100141, 88.16131591, 0.06300424, 61.71292114, -1159.72518873, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 22.04032898, 7.982e-05, 66.12098693, 0.00023946, 220.40328978, 0.0007982, -22.04032898, -7.982e-05, -66.12098693, -0.00023946, -220.40328978, -0.0007982, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 12.6, 8.5)
    ops.node(124013, 0.0, 12.6, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 28986713.76592508, 12077797.40246878, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 29.49902558, 0.00100823, 35.76851724, 0.01449195, 3.57685172, 0.06918029, -29.49902558, -0.00100823, -35.76851724, -0.01449195, -3.57685172, -0.06918029, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 29.49902558, 0.00100823, 35.76851724, 0.01449195, 3.57685172, 0.06918029, -29.49902558, -0.00100823, -35.76851724, -0.01449195, -3.57685172, -0.06918029, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 82.22548256, 0.02016458, 82.22548256, 0.06049373, 57.5578378, -1756.88883739, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 20.55637064, 8.987e-05, 61.66911192, 0.0002696, 205.56370641, 0.00089865, -20.55637064, -8.987e-05, -61.66911192, -0.0002696, -205.56370641, -0.00089865, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 82.22548256, 0.02016458, 82.22548256, 0.06049373, 57.5578378, -1756.88883739, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 20.55637064, 8.987e-05, 61.66911192, 0.0002696, 205.56370641, 0.00089865, -20.55637064, -8.987e-05, -61.66911192, -0.0002696, -205.56370641, -0.00089865, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 3.15, 12.6, 8.5)
    ops.node(124014, 3.15, 12.6, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0875, 30275935.9935401, 12614973.33064171, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 84.13542128, 0.00079204, 101.31521009, 0.01235069, 10.13152101, 0.05543762, -84.13542128, -0.00079204, -101.31521009, -0.01235069, -10.13152101, -0.05543762, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 57.81617471, 0.00102955, 69.62178115, 0.01144801, 6.96217812, 0.04512674, -57.81617471, -0.00102955, -69.62178115, -0.01144801, -6.96217812, -0.04512674, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 108.56623731, 0.01584081, 108.56623731, 0.04752242, 75.99636611, -1464.47487089, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 27.14155933, 8.114e-05, 81.42467798, 0.00024343, 271.41559327, 0.00081144, -27.14155933, -8.114e-05, -81.42467798, -0.00024343, -271.41559327, -0.00081144, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 83.51353257, 0.02059098, 83.51353257, 0.06177295, 58.4594728, -1070.94379644, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 20.87838314, 6.242e-05, 62.63514943, 0.00018726, 208.78383143, 0.00062419, -20.87838314, -6.242e-05, -62.63514943, -0.00018726, -208.78383143, -0.00062419, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 8.5, 12.6, 8.5)
    ops.node(124015, 8.5, 12.6, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.175, 28099157.52460898, 11707982.30192041, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 181.69910371, 0.0006463, 220.42886495, 0.01054287, 22.0428865, 0.03954724, -181.69910371, -0.0006463, -220.42886495, -0.01054287, -22.0428865, -0.03954724, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 122.24730373, 0.00080398, 148.30471837, 0.00986573, 14.83047184, 0.03339873, -122.24730373, -0.00080398, -148.30471837, -0.00986573, -14.83047184, -0.03339873, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 174.2997245, 0.01292601, 174.2997245, 0.03877802, 122.00980715, -1636.32488239, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 43.57493112, 7.018e-05, 130.72479337, 0.00021055, 435.74931124, 0.00070183, -43.57493112, -7.018e-05, -130.72479337, -0.00021055, -435.74931124, -0.00070183, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 137.84457933, 0.01607951, 137.84457933, 0.04823854, 96.49120553, -1216.15005521, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 34.46114483, 5.55e-05, 103.38343449, 0.00016651, 344.61144831, 0.00055504, -34.46114483, -5.55e-05, -103.38343449, -0.00016651, -344.61144831, -0.00055504, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 13.85, 12.6, 8.5)
    ops.node(124016, 13.85, 12.6, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 32390218.73811891, 13495924.47421621, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 36.97673024, 0.00116665, 44.27584937, 0.01029536, 4.42758494, 0.06186527, -36.97673024, -0.00116665, -44.27584937, -0.01029536, -4.42758494, -0.06186527, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 36.97673024, 0.00116665, 44.27584937, 0.01029536, 4.42758494, 0.06186527, -36.97673024, -0.00116665, -44.27584937, -0.01029536, -4.42758494, -0.06186527, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 75.74470686, 0.02333293, 75.74470686, 0.06999878, 53.0212948, -1070.71946234, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 18.93617672, 7.408e-05, 56.80853015, 0.00022225, 189.36176716, 0.00074084, -18.93617672, -7.408e-05, -56.80853015, -0.00022225, -189.36176716, -0.00074084, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 75.74470686, 0.02333293, 75.74470686, 0.06999878, 53.0212948, -1070.71946234, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 18.93617672, 7.408e-05, 56.80853015, 0.00022225, 189.36176716, 0.00074084, -18.93617672, -7.408e-05, -56.80853015, -0.00022225, -189.36176716, -0.00074084, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 16.8, 8.5)
    ops.node(124017, 0.0, 16.8, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 31941059.28846615, 13308774.70352756, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 28.82819776, 0.00097497, 34.70578502, 0.01132477, 3.4705785, 0.06915674, -28.82819776, -0.00097497, -34.70578502, -0.01132477, -3.4705785, -0.06915674, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 28.82819776, 0.00097497, 34.70578502, 0.01132477, 3.4705785, 0.06915674, -28.82819776, -0.00097497, -34.70578502, -0.01132477, -3.4705785, -0.06915674, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 70.22505073, 0.01949933, 70.22505073, 0.05849798, 49.15753551, -1226.48749255, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 17.55626268, 6.965e-05, 52.66878805, 0.00020895, 175.56262682, 0.00069651, -17.55626268, -6.965e-05, -52.66878805, -0.00020895, -175.56262682, -0.00069651, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 70.22505073, 0.01949933, 70.22505073, 0.05849798, 49.15753551, -1226.48749255, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 17.55626268, 6.965e-05, 52.66878805, 0.00020895, 175.56262682, 0.00069651, -17.55626268, -6.965e-05, -52.66878805, -0.00020895, -175.56262682, -0.00069651, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 3.15, 16.8, 8.5)
    ops.node(124018, 3.15, 16.8, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0875, 29729058.49416246, 12387107.70590102, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 81.70656933, 0.00080226, 98.48743881, 0.01141191, 9.84874388, 0.05370219, -81.70656933, -0.00080226, -98.48743881, -0.01141191, -9.84874388, -0.05370219, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 55.90529592, 0.00105687, 67.38710799, 0.01061995, 6.7387108, 0.04367598, -55.90529592, -0.00105687, -67.38710799, -0.01061995, -6.7387108, -0.04367598, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 104.35513589, 0.01604528, 104.35513589, 0.04813583, 73.04859513, -1372.41060093, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 26.08878397, 7.943e-05, 78.26635192, 0.00023829, 260.88783973, 0.00079431, -26.08878397, -7.943e-05, -78.26635192, -0.00023829, -260.88783973, -0.00079431, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 71.14376426, 0.0211375, 71.14376426, 0.06341249, 49.80063498, -1014.55860931, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 17.78594106, 5.415e-05, 53.35782319, 0.00016246, 177.85941064, 0.00054152, -17.78594106, -5.415e-05, -53.35782319, -0.00016246, -177.85941064, -0.00054152, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 8.5, 16.8, 8.5)
    ops.node(124019, 8.5, 16.8, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.175, 30782272.0230338, 12825946.67626408, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 186.89385161, 0.00062904, 225.52788068, 0.01001872, 22.55278807, 0.04103923, -186.89385161, -0.00062904, -225.52788068, -0.01001872, -22.55278807, -0.04103923, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 126.72677079, 0.00076975, 152.92327594, 0.00936737, 15.29232759, 0.03453618, -126.72677079, -0.00076975, -152.92327594, -0.00936737, -15.29232759, -0.03453618, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 189.35444041, 0.01258085, 189.35444041, 0.03774256, 132.54810829, -1594.58283474, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 47.3386101, 6.96e-05, 142.01583031, 0.0002088, 473.38610104, 0.00069599, -47.3386101, -6.96e-05, -142.01583031, -0.0002088, -473.38610104, -0.00069599, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 147.3304293, 0.01539497, 147.3304293, 0.04618491, 103.13130051, -1190.9293155, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 36.83260732, 5.415e-05, 110.49782197, 0.00016246, 368.32607324, 0.00054153, -36.83260732, -5.415e-05, -110.49782197, -0.00016246, -368.32607324, -0.00054153, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 13.85, 16.8, 8.5)
    ops.node(124020, 13.85, 16.8, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 31870350.82702997, 13279312.84459582, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 37.60818098, 0.00101717, 45.09110061, 0.01187203, 4.50911006, 0.06270164, -37.60818098, -0.00101717, -45.09110061, -0.01187203, -4.50911006, -0.06270164, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 37.60818098, 0.00101717, 45.09110061, 0.01187203, 4.50911006, 0.06270164, -37.60818098, -0.00101717, -45.09110061, -0.01187203, -4.50911006, -0.06270164, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 87.28705739, 0.02034332, 87.28705739, 0.06102995, 61.10094017, -1234.74050848, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 21.82176435, 8.677e-05, 65.46529304, 0.0002603, 218.21764348, 0.00086766, -21.82176435, -8.677e-05, -65.46529304, -0.0002603, -218.21764348, -0.00086766, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 87.28705739, 0.02034332, 87.28705739, 0.06102995, 61.10094017, -1234.74050848, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 21.82176435, 8.677e-05, 65.46529304, 0.0002603, 218.21764348, 0.00086766, -21.82176435, -8.677e-05, -65.46529304, -0.0002603, -218.21764348, -0.00086766, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 0.0, 21.0, 8.5)
    ops.node(124021, 0.0, 21.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 31961813.47337841, 13317422.28057434, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 30.38550079, 0.00099635, 36.57839312, 0.01228997, 3.65783931, 0.07014024, -30.38550079, -0.00099635, -36.57839312, -0.01228997, -3.65783931, -0.07014024, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 30.38550079, 0.00099635, 36.57839312, 0.01228997, 3.65783931, 0.07014024, -30.38550079, -0.00099635, -36.57839312, -0.01228997, -3.65783931, -0.07014024, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 82.28625114, 0.01992702, 82.28625114, 0.05978107, 57.6003758, -1446.45683903, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 20.57156278, 8.156e-05, 61.71468835, 0.00024468, 205.71562784, 0.00081561, -20.57156278, -8.156e-05, -61.71468835, -0.00024468, -205.71562784, -0.00081561, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 82.28625114, 0.01992702, 82.28625114, 0.05978107, 57.6003758, -1446.45683903, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 20.57156278, 8.156e-05, 61.71468835, 0.00024468, 205.71562784, 0.00081561, -20.57156278, -8.156e-05, -61.71468835, -0.00024468, -205.71562784, -0.00081561, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 3.15, 21.0, 8.5)
    ops.node(124022, 3.15, 21.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0875, 29441770.02975371, 12267404.17906405, 0.0010204, 0.0005013, 0.00098255, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 84.92922241, 0.00080731, 102.42009551, 0.01196863, 10.24200955, 0.05382076, -84.92922241, -0.00080731, -102.42009551, -0.01196863, -10.24200955, -0.05382076, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 58.30028965, 0.0010528, 70.3070282, 0.01111313, 7.03070282, 0.04382668, -58.30028965, -0.0010528, -70.3070282, -0.01111313, -7.03070282, -0.04382668, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 107.90050539, 0.01614612, 107.90050539, 0.04843835, 75.53035377, -1519.86438246, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 26.97512635, 8.293e-05, 80.92537904, 0.00024879, 269.75126346, 0.00082931, -26.97512635, -8.293e-05, -80.92537904, -0.00024879, -269.75126346, -0.00082931, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 78.98530127, 0.02105592, 78.98530127, 0.06316777, 55.28971089, -1104.72517962, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 19.74632532, 6.071e-05, 59.23897595, 0.00018212, 197.46325317, 0.00060707, -19.74632532, -6.071e-05, -59.23897595, -0.00018212, -197.46325317, -0.00060707, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 8.5, 21.0, 8.5)
    ops.node(124023, 8.5, 21.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.175, 33466619.38917395, 13944424.74548914, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 177.05241436, 0.00065254, 212.004011, 0.01202131, 21.2004011, 0.05133709, -177.05241436, -0.00065254, -212.004011, -0.01202131, -21.2004011, -0.05133709, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 111.05777916, 0.00082134, 132.98149432, 0.01112276, 13.29814943, 0.04224012, -111.05777916, -0.00082134, -132.98149432, -0.01112276, -13.29814943, -0.04224012, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 224.81704516, 0.01305087, 224.81704516, 0.03915261, 157.37193161, -2206.99740982, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 56.20426129, 7.601e-05, 168.61278387, 0.00022802, 562.0426129, 0.00076005, -56.20426129, -7.601e-05, -168.61278387, -0.00022802, -562.0426129, -0.00076005, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 182.86808696, 0.01642688, 182.86808696, 0.04928065, 128.00766087, -1555.70038129, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 45.71702174, 6.182e-05, 137.15106522, 0.00018547, 457.17021739, 0.00061823, -45.71702174, -6.182e-05, -137.15106522, -0.00018547, -457.17021739, -0.00061823, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 13.85, 21.0, 8.5)
    ops.node(124024, 13.85, 21.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 32638099.83738373, 13599208.26557655, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 36.58074548, 0.00109157, 43.77272682, 0.01279621, 4.37727268, 0.06470487, -36.58074548, -0.00109157, -43.77272682, -0.01279621, -4.37727268, -0.06470487, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 36.58074548, 0.00109157, 43.77272682, 0.01279621, 4.37727268, 0.06470487, -36.58074548, -0.00109157, -43.77272682, -0.01279621, -4.37727268, -0.06470487, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 92.68631701, 0.02183144, 92.68631701, 0.06549431, 64.88042191, -1375.26737313, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 23.17157925, 8.997e-05, 69.51473776, 0.0002699, 231.71579252, 0.00089965, -23.17157925, -8.997e-05, -69.51473776, -0.0002699, -231.71579252, -0.00089965, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 92.68631701, 0.02183144, 92.68631701, 0.06549431, 64.88042191, -1375.26737313, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 23.17157925, 8.997e-05, 69.51473776, 0.0002699, 231.71579252, 0.00089965, -23.17157925, -8.997e-05, -69.51473776, -0.0002699, -231.71579252, -0.00089965, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173025, 0.0, 25.2, 8.5)
    ops.node(124025, 0.0, 25.2, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3025, 173025, 124025, 0.0625, 29168162.10824942, 12153400.87843726, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23025, 25.98327307, 0.00097746, 31.59206307, 0.01267723, 3.15920631, 0.07290938, -25.98327307, -0.00097746, -31.59206307, -0.01267723, -3.15920631, -0.07290938, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13025, 25.98327307, 0.00097746, 31.59206307, 0.01267723, 3.15920631, 0.07290938, -25.98327307, -0.00097746, -31.59206307, -0.01267723, -3.15920631, -0.07290938, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23025, 3025, 0.0, 72.08110044, 0.01954913, 72.08110044, 0.05864739, 50.45677031, -1939.88954174, 0.05, 2, 0, 73025, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 43025, 18.02027511, 7.829e-05, 54.06082533, 0.00023487, 180.20275111, 0.00078288, -18.02027511, -7.829e-05, -54.06082533, -0.00023487, -180.20275111, -0.00078288, 0.4, 0.3, 0.003, 0.0, 0.0, 23025, 2)
    ops.limitCurve('ThreePoint', 13025, 3025, 0.0, 72.08110044, 0.01954913, 72.08110044, 0.05864739, 50.45677031, -1939.88954174, 0.05, 2, 0, 73025, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 33025, 18.02027511, 7.829e-05, 54.06082533, 0.00023487, 180.20275111, 0.00078288, -18.02027511, -7.829e-05, -54.06082533, -0.00023487, -180.20275111, -0.00078288, 0.4, 0.3, 0.003, 0.0, 0.0, 13025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3025, 99999, 'P', 43025, 'Vy', 33025, 'Vz', 23025, 'My', 13025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173025, 73025, 173025, 3025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 3025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173026, 3.15, 25.2, 8.5)
    ops.node(124026, 3.15, 25.2, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3026, 173026, 124026, 0.0625, 33342350.53081751, 13892646.0545073, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23026, 34.8599172, 0.00100693, 41.71062025, 0.01079174, 4.17106202, 0.06674905, -34.8599172, -0.00100693, -41.71062025, -0.01079174, -4.17106202, -0.06674905, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13026, 34.8599172, 0.00100693, 41.71062025, 0.01079174, 4.17106202, 0.06674905, -34.8599172, -0.00100693, -41.71062025, -0.01079174, -4.17106202, -0.06674905, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23026, 3026, 0.0, 81.039968, 0.02013866, 81.039968, 0.06041598, 56.7279776, -1217.41428466, 0.05, 2, 0, 73026, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 43026, 20.259992, 7.7e-05, 60.779976, 0.000231, 202.59992, 0.00077, -20.259992, -7.7e-05, -60.779976, -0.000231, -202.59992, -0.00077, 0.4, 0.3, 0.003, 0.0, 0.0, 23026, 2)
    ops.limitCurve('ThreePoint', 13026, 3026, 0.0, 81.039968, 0.02013866, 81.039968, 0.06041598, 56.7279776, -1217.41428466, 0.05, 2, 0, 73026, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 33026, 20.259992, 7.7e-05, 60.779976, 0.000231, 202.59992, 0.00077, -20.259992, -7.7e-05, -60.779976, -0.000231, -202.59992, -0.00077, 0.4, 0.3, 0.003, 0.0, 0.0, 13026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3026, 99999, 'P', 43026, 'Vy', 33026, 'Vz', 23026, 'My', 13026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173026, 73026, 173026, 3026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 3026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173027, 8.5, 25.2, 8.5)
    ops.node(124027, 8.5, 25.2, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3027, 173027, 124027, 0.0625, 32452913.84218792, 13522047.43424497, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23027, 53.08641133, 0.00110313, 63.55882461, 0.01097917, 6.35588246, 0.05584401, -53.08641133, -0.00110313, -63.55882461, -0.01097917, -6.35588246, -0.05584401, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13027, 53.08641133, 0.00110313, 63.55882461, 0.01097917, 6.35588246, 0.05584401, -53.08641133, -0.00110313, -63.55882461, -0.01097917, -6.35588246, -0.05584401, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23027, 3027, 0.0, 55.94978442, 0.02206257, 55.94978442, 0.06618771, 39.16484909, -978.90770781, 0.05, 2, 0, 73027, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 43027, 13.9874461, 5.462e-05, 41.96233831, 0.00016385, 139.87446105, 0.00054617, -13.9874461, -5.462e-05, -41.96233831, -0.00016385, -139.87446105, -0.00054617, 0.4, 0.3, 0.003, 0.0, 0.0, 23027, 2)
    ops.limitCurve('ThreePoint', 13027, 3027, 0.0, 55.94978442, 0.02206257, 55.94978442, 0.06618771, 39.16484909, -978.90770781, 0.05, 2, 0, 73027, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 33027, 13.9874461, 5.462e-05, 41.96233831, 0.00016385, 139.87446105, 0.00054617, -13.9874461, -5.462e-05, -41.96233831, -0.00016385, -139.87446105, -0.00054617, 0.4, 0.3, 0.003, 0.0, 0.0, 13027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3027, 99999, 'P', 43027, 'Vy', 33027, 'Vz', 23027, 'My', 13027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173027, 73027, 173027, 3027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 3027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173028, 13.85, 25.2, 8.5)
    ops.node(124028, 13.85, 25.2, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3028, 173028, 124028, 0.0625, 32777624.47073738, 13657343.52947391, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23028, 30.50006751, 0.00097515, 36.62960762, 0.01151228, 3.66296076, 0.07024253, -30.50006751, -0.00097515, -36.62960762, -0.01151228, -3.66296076, -0.07024253, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13028, 30.50006751, 0.00097515, 36.62960762, 0.01151228, 3.66296076, 0.07024253, -30.50006751, -0.00097515, -36.62960762, -0.01151228, -3.66296076, -0.07024253, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23028, 3028, 0.0, 80.44261278, 0.01950291, 80.44261278, 0.05850872, 56.30982894, -1423.17326857, 0.05, 2, 0, 73028, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 43028, 20.11065319, 7.775e-05, 60.33195958, 0.00023325, 201.10653194, 0.00077749, -20.11065319, -7.775e-05, -60.33195958, -0.00023325, -201.10653194, -0.00077749, 0.4, 0.3, 0.003, 0.0, 0.0, 23028, 2)
    ops.limitCurve('ThreePoint', 13028, 3028, 0.0, 80.44261278, 0.01950291, 80.44261278, 0.05850872, 56.30982894, -1423.17326857, 0.05, 2, 0, 73028, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 33028, 20.11065319, 7.775e-05, 60.33195958, 0.00023325, 201.10653194, 0.00077749, -20.11065319, -7.775e-05, -60.33195958, -0.00023325, -201.10653194, -0.00077749, 0.4, 0.3, 0.003, 0.0, 0.0, 13028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3028, 99999, 'P', 43028, 'Vy', 33028, 'Vz', 23028, 'My', 13028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173028, 73028, 173028, 3028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 3028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124029, 0.0, 0.0, 1.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 170001, 124029, 0.075, 31377253.01256163, 13073855.42190068, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 72.67380509, 0.00067523, 86.88012167, 0.01938636, 8.68801217, 0.08750537, -72.67380509, -0.00067523, -86.88012167, -0.01938636, -8.68801217, -0.08750537, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 55.68116882, 0.00074856, 66.56575524, 0.01825869, 6.65657552, 0.0764592, -55.68116882, -0.00074856, -66.56575524, -0.01825869, -6.65657552, -0.0764592, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 164.83792662, 0.0135046, 164.83792662, 0.04051381, 115.38654864, -5034.98891843, 0.05, 2, 0, 70001, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 41.20948166, 6.935e-05, 123.62844497, 0.00020804, 412.09481656, 0.00069345, -41.20948166, -6.935e-05, -123.62844497, -0.00020804, -412.09481656, -0.00069345, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 137.36493885, 0.01497111, 137.36493885, 0.04491332, 96.1554572, -4130.07339396, 0.05, 2, 0, 70001, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 34.34123471, 5.779e-05, 103.02370414, 0.00017336, 343.41234713, 0.00057788, -34.34123471, -5.779e-05, -103.02370414, -0.00017336, -343.41234713, -0.00057788, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 0.0, 0.0, 1.575)
    ops.node(121001, 0.0, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 174029, 121001, 0.075, 29766670.20121895, 12402779.2505079, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 66.20941929, 0.00063426, 79.52233777, 0.02190537, 7.95223378, 0.08942944, -66.20941929, -0.00063426, -79.52233777, -0.02190537, -7.95223378, -0.08942944, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 50.33597272, 0.00069609, 60.45717162, 0.02060189, 6.04571716, 0.07829409, -50.33597272, -0.00069609, -60.45717162, -0.02060189, -6.04571716, -0.07829409, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 168.56602371, 0.01268524, 168.56602371, 0.03805572, 117.9962166, -6340.43579145, 0.05, 2, 0, 74029, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 42.14150593, 7.475e-05, 126.42451778, 0.00022425, 421.41505927, 0.0007475, -42.14150593, -7.475e-05, -126.42451778, -0.00022425, -421.41505927, -0.0007475, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 140.47168642, 0.01392186, 140.47168642, 0.04176557, 98.3301805, -5056.37505817, 0.05, 2, 0, 74029, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 35.11792161, 6.229e-05, 105.35376482, 0.00018688, 351.17921606, 0.00062292, -35.11792161, -6.229e-05, -105.35376482, -0.00018688, -351.17921606, -0.00062292, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.15, 0.0, 0.0)
    ops.node(124030, 3.15, 0.0, 1.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 170002, 124030, 0.09, 33893999.72372704, 14122499.88488627, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 129.74957473, 0.00068205, 152.53614332, 0.00995073, 15.25361433, 0.04051216, -129.74957473, -0.00068205, -152.53614332, -0.00995073, -15.25361433, -0.04051216, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 117.87149501, 0.00068205, 138.57203998, 0.00995073, 13.857204, 0.04051216, -117.87149501, -0.00068205, -138.57203998, -0.00995073, -13.857204, -0.04051216, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 200.59766206, 0.01364094, 200.59766206, 0.04092282, 140.41836344, -4302.950364, 0.05, 2, 0, 70002, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 50.14941552, 6.51e-05, 150.44824655, 0.00019531, 501.49415516, 0.00065102, -50.14941552, -6.51e-05, -150.44824655, -0.00019531, -501.49415516, -0.00065102, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 200.59766206, 0.01364094, 200.59766206, 0.04092282, 140.41836344, -4302.950364, 0.05, 2, 0, 70002, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 50.14941552, 6.51e-05, 150.44824655, 0.00019531, 501.49415516, 0.00065102, -50.14941552, -6.51e-05, -150.44824655, -0.00019531, -501.49415516, -0.00065102, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 3.15, 0.0, 1.575)
    ops.node(121002, 3.15, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4077, 174030, 121002, 0.09, 31611656.73258133, 13171523.63857556, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24077, 124.57745615, 0.00072486, 147.0802869, 0.01233552, 14.70802869, 0.04466239, -124.57745615, -0.00072486, -147.0802869, -0.01233552, -14.70802869, -0.04466239, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14077, 113.75851939, 0.00072486, 134.30709043, 0.01233552, 13.43070904, 0.04466239, -113.75851939, -0.00072486, -134.30709043, -0.01233552, -13.43070904, -0.04466239, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24077, 4077, 0.0, 201.43741423, 0.01449719, 201.43741423, 0.04349156, 141.00618996, -4909.08127633, 0.05, 2, 0, 74030, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44077, 50.35935356, 7.009e-05, 151.07806067, 0.00021028, 503.59353557, 0.00070095, -50.35935356, -7.009e-05, -151.07806067, -0.00021028, -503.59353557, -0.00070095, 0.4, 0.3, 0.003, 0.0, 0.0, 24077, 2)
    ops.limitCurve('ThreePoint', 14077, 4077, 0.0, 201.43741423, 0.01449719, 201.43741423, 0.04349156, 141.00618996, -4909.08127633, 0.05, 2, 0, 74030, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34077, 50.35935356, 7.009e-05, 151.07806067, 0.00021028, 503.59353557, 0.00070095, -50.35935356, -7.009e-05, -151.07806067, -0.00021028, -503.59353557, -0.00070095, 0.4, 0.3, 0.003, 0.0, 0.0, 14077, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4077, 99999, 'P', 44077, 'Vy', 34077, 'Vz', 24077, 'My', 14077, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4077, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4077, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.0)
    ops.node(124031, 0.0, 0.0, 3.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 171001, 124031, 0.075, 30441945.88297385, 12684144.11790577, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 63.56155444, 0.00064657, 76.39889964, 0.01094762, 7.63988996, 0.05868982, -63.56155444, -0.00064657, -76.39889964, -0.01094762, -7.63988996, -0.05868982, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 48.20979708, 0.00071264, 57.9465918, 0.01041213, 5.79465918, 0.05180393, -48.20979708, -0.00071264, -57.9465918, -0.01041213, -5.79465918, -0.05180393, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 126.51579652, 0.01293143, 126.51579652, 0.03879429, 88.56105756, -3045.56368373, 0.05, 2, 0, 71001, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 31.62894913, 5.486e-05, 94.88684739, 0.00016458, 316.2894913, 0.00054859, -31.62894913, -5.486e-05, -94.88684739, -0.00016458, -316.2894913, -0.00054859, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 104.32108996, 0.01425273, 104.32108996, 0.0427582, 73.02476297, -2541.65090998, 0.05, 2, 0, 71001, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 26.08027249, 4.523e-05, 78.24081747, 0.0001357, 260.80272489, 0.00045235, -26.08027249, -4.523e-05, -78.24081747, -0.0001357, -260.80272489, -0.00045235, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 0.0, 0.0, 4.3)
    ops.node(122001, 0.0, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 174031, 122001, 0.075, 30013489.38920699, 12505620.57883625, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 57.9218952, 0.00064716, 69.82939654, 0.01272346, 6.98293965, 0.06297004, -57.9218952, -0.00064716, -69.82939654, -0.01272346, -6.98293965, -0.06297004, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 43.841755, 0.00071635, 52.85468101, 0.01208743, 5.2854681, 0.05565048, -43.841755, -0.00071635, -52.85468101, -0.01208743, -5.2854681, -0.05565048, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 123.05385927, 0.01294322, 123.05385927, 0.03882965, 86.13770149, -3266.38623556, 0.05, 2, 0, 74031, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 30.76346482, 5.412e-05, 92.29039445, 0.00016236, 307.63464818, 0.00054119, -30.76346482, -5.412e-05, -92.29039445, -0.00016236, -307.63464818, -0.00054119, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 102.54488273, 0.01432694, 102.54488273, 0.04298083, 71.78141791, -2663.51482711, 0.05, 2, 0, 74031, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 25.63622068, 4.51e-05, 76.90866204, 0.0001353, 256.36220681, 0.00045099, -25.63622068, -4.51e-05, -76.90866204, -0.0001353, -256.36220681, -0.00045099, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.15, 0.0, 3.0)
    ops.node(124032, 3.15, 0.0, 3.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 171002, 124032, 0.09, 33834038.1359603, 14097515.88998346, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 98.67588775, 0.00068464, 116.66432932, 0.00955002, 11.66643293, 0.0454816, -98.67588775, -0.00068464, -116.66432932, -0.00955002, -11.66643293, -0.0454816, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 93.57044685, 0.00068464, 110.62817548, 0.00955002, 11.06281755, 0.0454816, -93.57044685, -0.00068464, -110.62817548, -0.00955002, -11.06281755, -0.0454816, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 183.2697386, 0.01369283, 183.2697386, 0.04107848, 128.28881702, -3684.17412314, 0.05, 2, 0, 71002, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 45.81743465, 5.958e-05, 137.45230395, 0.00017875, 458.1743465, 0.00059584, -45.81743465, -5.958e-05, -137.45230395, -0.00017875, -458.1743465, -0.00059584, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 183.2697386, 0.01369283, 183.2697386, 0.04107848, 128.28881702, -3684.17412314, 0.05, 2, 0, 71002, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 45.81743465, 5.958e-05, 137.45230395, 0.00017875, 458.1743465, 0.00059584, -45.81743465, -5.958e-05, -137.45230395, -0.00017875, -458.1743465, -0.00059584, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4081, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 3.15, 0.0, 4.3)
    ops.node(122002, 3.15, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4082, 174032, 122002, 0.09, 30796377.9843172, 12831824.16013217, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24082, 104.14936518, 0.00069195, 123.93685643, 0.01056967, 12.39368564, 0.04229912, -104.14936518, -0.00069195, -123.93685643, -0.01056967, -12.39368564, -0.04229912, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14082, 94.09467575, 0.00069195, 111.97186175, 0.01056967, 11.19718617, 0.04229912, -94.09467575, -0.00069195, -111.97186175, -0.01056967, -11.19718617, -0.04229912, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24082, 4082, 0.0, 166.87376731, 0.01383898, 166.87376731, 0.04151693, 116.81163712, -3607.1533425, 0.05, 2, 0, 74032, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44082, 41.71844183, 5.96e-05, 125.15532548, 0.00017881, 417.18441828, 0.00059605, -41.71844183, -5.96e-05, -125.15532548, -0.00017881, -417.18441828, -0.00059605, 0.4, 0.3, 0.003, 0.0, 0.0, 24082, 2)
    ops.limitCurve('ThreePoint', 14082, 4082, 0.0, 166.87376731, 0.01383898, 166.87376731, 0.04151693, 116.81163712, -3607.1533425, 0.05, 2, 0, 74032, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34082, 41.71844183, 5.96e-05, 125.15532548, 0.00017881, 417.18441828, 0.00059605, -41.71844183, -5.96e-05, -125.15532548, -0.00017881, -417.18441828, -0.00059605, 0.4, 0.3, 0.003, 0.0, 0.0, 14082, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4082, 99999, 'P', 44082, 'Vy', 34082, 'Vz', 24082, 'My', 14082, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4082, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4082, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.75)
    ops.node(124033, 0.0, 0.0, 6.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4084, 172001, 124033, 0.0625, 31362291.85588434, 13067621.60661848, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24084, 35.91161779, 0.00070678, 43.17941353, 0.01243184, 4.31794135, 0.06503039, -35.91161779, -0.00070678, -43.17941353, -0.01243184, -4.31794135, -0.06503039, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14084, 35.91161779, 0.00070678, 43.17941353, 0.01243184, 4.31794135, 0.06503039, -35.91161779, -0.00070678, -43.17941353, -0.01243184, -4.31794135, -0.06503039, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24084, 4084, 0.0, 96.40953606, 0.01413551, 96.40953606, 0.04240654, 67.48667524, -2876.65512105, 0.05, 2, 0, 72001, 24033, 2, 3)
    ops.uniaxialMaterial('LimitState', 44084, 24.10238401, 4.869e-05, 72.30715204, 0.00014608, 241.02384015, 0.00048693, -24.10238401, -4.869e-05, -72.30715204, -0.00014608, -241.02384015, -0.00048693, 0.4, 0.3, 0.003, 0.0, 0.0, 24084, 2)
    ops.limitCurve('ThreePoint', 14084, 4084, 0.0, 96.40953606, 0.01413551, 96.40953606, 0.04240654, 67.48667524, -2876.65512105, 0.05, 2, 0, 72001, 24033, 1, 3)
    ops.uniaxialMaterial('LimitState', 34084, 24.10238401, 4.869e-05, 72.30715204, 0.00014608, 241.02384015, 0.00048693, -24.10238401, -4.869e-05, -72.30715204, -0.00014608, -241.02384015, -0.00048693, 0.4, 0.3, 0.003, 0.0, 0.0, 14084, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4084, 99999, 'P', 44084, 'Vy', 34084, 'Vz', 24084, 'My', 14084, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4084, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124033, 124033, 24033, 4084, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174033, 0.0, 0.0, 7.05)
    ops.node(123001, 0.0, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4085, 174033, 123001, 0.0625, 31692084.99597235, 13205035.41498848, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24085, 30.16835354, 0.00068441, 36.33760912, 0.01265149, 3.63376091, 0.06991038, -30.16835354, -0.00068441, -36.33760912, -0.01265149, -3.63376091, -0.06991038, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14085, 30.16835354, 0.00068441, 36.33760912, 0.01265149, 3.63376091, 0.06991038, -30.16835354, -0.00068441, -36.33760912, -0.01265149, -3.63376091, -0.06991038, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24085, 4085, 0.0, 91.18460906, 0.01368813, 91.18460906, 0.04106439, 63.82922634, -3039.92228418, 0.05, 2, 0, 74033, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44085, 22.79615226, 4.557e-05, 68.38845679, 0.00013672, 227.96152264, 0.00045575, -22.79615226, -4.557e-05, -68.38845679, -0.00013672, -227.96152264, -0.00045575, 0.4, 0.3, 0.003, 0.0, 0.0, 24085, 2)
    ops.limitCurve('ThreePoint', 14085, 4085, 0.0, 91.18460906, 0.01368813, 91.18460906, 0.04106439, 63.82922634, -3039.92228418, 0.05, 2, 0, 74033, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34085, 22.79615226, 4.557e-05, 68.38845679, 0.00013672, 227.96152264, 0.00045575, -22.79615226, -4.557e-05, -68.38845679, -0.00013672, -227.96152264, -0.00045575, 0.4, 0.3, 0.003, 0.0, 0.0, 14085, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4085, 99999, 'P', 44085, 'Vy', 34085, 'Vz', 24085, 'My', 14085, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174033, 74033, 174033, 4085, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4085, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.15, 0.0, 5.75)
    ops.node(124034, 3.15, 0.0, 6.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4086, 172002, 124034, 0.0625, 32980557.88211738, 13741899.11754891, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24086, 54.12196002, 0.00076382, 64.16685579, 0.00968526, 6.41668558, 0.0505821, -54.12196002, -0.00076382, -64.16685579, -0.00968526, -6.41668558, -0.0505821, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14086, 54.12196002, 0.00076382, 64.16685579, 0.00968526, 6.41668558, 0.0505821, -54.12196002, -0.00076382, -64.16685579, -0.00968526, -6.41668558, -0.0505821, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24086, 4086, 0.0, 111.96219215, 0.01527648, 111.96219215, 0.04582943, 78.3735345, -2718.45426556, 0.05, 2, 0, 72002, 24034, 2, 3)
    ops.uniaxialMaterial('LimitState', 44086, 27.99054804, 5.377e-05, 83.97164411, 0.00016132, 279.90548037, 0.00053774, -27.99054804, -5.377e-05, -83.97164411, -0.00016132, -279.90548037, -0.00053774, 0.4, 0.3, 0.003, 0.0, 0.0, 24086, 2)
    ops.limitCurve('ThreePoint', 14086, 4086, 0.0, 111.96219215, 0.01527648, 111.96219215, 0.04582943, 78.3735345, -2718.45426556, 0.05, 2, 0, 72002, 24034, 1, 3)
    ops.uniaxialMaterial('LimitState', 34086, 27.99054804, 5.377e-05, 83.97164411, 0.00016132, 279.90548037, 0.00053774, -27.99054804, -5.377e-05, -83.97164411, -0.00016132, -279.90548037, -0.00053774, 0.4, 0.3, 0.003, 0.0, 0.0, 14086, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4086, 99999, 'P', 44086, 'Vy', 34086, 'Vz', 24086, 'My', 14086, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4086, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124034, 124034, 24034, 4086, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174034, 3.15, 0.0, 7.05)
    ops.node(123002, 3.15, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4087, 174034, 123002, 0.0625, 31767458.65881805, 13236441.10784085, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24087, 49.2017717, 0.00075235, 58.60367912, 0.00915132, 5.86036791, 0.05047793, -49.2017717, -0.00075235, -58.60367912, -0.00915132, -5.86036791, -0.05047793, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14087, 49.2017717, 0.00075235, 58.60367912, 0.00915132, 5.86036791, 0.05047793, -49.2017717, -0.00075235, -58.60367912, -0.00915132, -5.86036791, -0.05047793, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24087, 4087, 0.0, 94.87779619, 0.0150471, 94.87779619, 0.04514129, 66.41445733, -2470.91058157, 0.05, 2, 0, 74034, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44087, 23.71944905, 4.731e-05, 71.15834714, 0.00014192, 237.19449047, 0.00047308, -23.71944905, -4.731e-05, -71.15834714, -0.00014192, -237.19449047, -0.00047308, 0.4, 0.3, 0.003, 0.0, 0.0, 24087, 2)
    ops.limitCurve('ThreePoint', 14087, 4087, 0.0, 94.87779619, 0.0150471, 94.87779619, 0.04514129, 66.41445733, -2470.91058157, 0.05, 2, 0, 74034, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34087, 23.71944905, 4.731e-05, 71.15834714, 0.00014192, 237.19449047, 0.00047308, -23.71944905, -4.731e-05, -71.15834714, -0.00014192, -237.19449047, -0.00047308, 0.4, 0.3, 0.003, 0.0, 0.0, 14087, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4087, 99999, 'P', 44087, 'Vy', 34087, 'Vz', 24087, 'My', 14087, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174034, 74034, 174034, 4087, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4087, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.5)
    ops.node(124035, 0.0, 0.0, 9.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4089, 173001, 124035, 0.0625, 29484751.74447232, 12285313.22686347, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24089, 28.66346954, 0.0006588, 34.80231093, 0.01404364, 3.48023109, 0.07337074, -28.66346954, -0.0006588, -34.80231093, -0.01404364, -3.48023109, -0.07337074, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14089, 28.66346954, 0.0006588, 34.80231093, 0.01404364, 3.48023109, 0.07337074, -28.66346954, -0.0006588, -34.80231093, -0.01404364, -3.48023109, -0.07337074, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24089, 4089, 0.0, 86.69494972, 0.0131761, 86.69494972, 0.03952829, 60.6864648, -4459.37359059, 0.05, 2, 0, 73001, 24035, 2, 3)
    ops.uniaxialMaterial('LimitState', 44089, 21.67373743, 4.657e-05, 65.02121229, 0.00013972, 216.7373743, 0.00046575, -21.67373743, -4.657e-05, -65.02121229, -0.00013972, -216.7373743, -0.00046575, 0.4, 0.3, 0.003, 0.0, 0.0, 24089, 2)
    ops.limitCurve('ThreePoint', 14089, 4089, 0.0, 86.69494972, 0.0131761, 86.69494972, 0.03952829, 60.6864648, -4459.37359059, 0.05, 2, 0, 73001, 24035, 1, 3)
    ops.uniaxialMaterial('LimitState', 34089, 21.67373743, 4.657e-05, 65.02121229, 0.00013972, 216.7373743, 0.00046575, -21.67373743, -4.657e-05, -65.02121229, -0.00013972, -216.7373743, -0.00046575, 0.4, 0.3, 0.003, 0.0, 0.0, 14089, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4089, 99999, 'P', 44089, 'Vy', 34089, 'Vz', 24089, 'My', 14089, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4089, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124035, 124035, 24035, 4089, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174035, 0.0, 0.0, 9.8)
    ops.node(124001, 0.0, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4090, 174035, 124001, 0.0625, 31607616.96291844, 13169840.40121602, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24090, 21.04154033, 0.00069038, 25.46901582, 0.01382826, 2.54690158, 0.07954596, -21.04154033, -0.00069038, -25.46901582, -0.01382826, -2.54690158, -0.07954596, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14090, 21.04154033, 0.00069038, 25.46901582, 0.01382826, 2.54690158, 0.07954596, -21.04154033, -0.00069038, -25.46901582, -0.01382826, -2.54690158, -0.07954596, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24090, 4090, 0.0, 83.27182701, 0.01380757, 83.27182701, 0.04142272, 58.29027891, -13936.02326504, 0.05, 2, 0, 74035, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44090, 20.81795675, 4.173e-05, 62.45387026, 0.00012519, 208.17956752, 0.00041731, -20.81795675, -4.173e-05, -62.45387026, -0.00012519, -208.17956752, -0.00041731, 0.4, 0.3, 0.003, 0.0, 0.0, 24090, 2)
    ops.limitCurve('ThreePoint', 14090, 4090, 0.0, 83.27182701, 0.01380757, 83.27182701, 0.04142272, 58.29027891, -13936.02326504, 0.05, 2, 0, 74035, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34090, 20.81795675, 4.173e-05, 62.45387026, 0.00012519, 208.17956752, 0.00041731, -20.81795675, -4.173e-05, -62.45387026, -0.00012519, -208.17956752, -0.00041731, 0.4, 0.3, 0.003, 0.0, 0.0, 14090, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4090, 99999, 'P', 44090, 'Vy', 34090, 'Vz', 24090, 'My', 14090, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174035, 74035, 174035, 4090, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4090, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.15, 0.0, 8.5)
    ops.node(124036, 3.15, 0.0, 9.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4091, 173002, 124036, 0.0625, 31122678.4260865, 12967782.67753604, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24091, 35.9293743, 0.00070672, 43.23410468, 0.01010683, 4.32341047, 0.06269803, -35.9293743, -0.00070672, -43.23410468, -0.01010683, -4.32341047, -0.06269803, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14091, 35.9293743, 0.00070672, 43.23410468, 0.01010683, 4.32341047, 0.06269803, -35.9293743, -0.00070672, -43.23410468, -0.01010683, -4.32341047, -0.06269803, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24091, 4091, 0.0, 79.01629055, 0.01413434, 79.01629055, 0.04240301, 55.31140339, -2204.15216606, 0.05, 2, 0, 73002, 24036, 2, 3)
    ops.uniaxialMaterial('LimitState', 44091, 19.75407264, 4.022e-05, 59.26221791, 0.00012065, 197.54072638, 0.00040216, -19.75407264, -4.022e-05, -59.26221791, -0.00012065, -197.54072638, -0.00040216, 0.4, 0.3, 0.003, 0.0, 0.0, 24091, 2)
    ops.limitCurve('ThreePoint', 14091, 4091, 0.0, 79.01629055, 0.01413434, 79.01629055, 0.04240301, 55.31140339, -2204.15216606, 0.05, 2, 0, 73002, 24036, 1, 3)
    ops.uniaxialMaterial('LimitState', 34091, 19.75407264, 4.022e-05, 59.26221791, 0.00012065, 197.54072638, 0.00040216, -19.75407264, -4.022e-05, -59.26221791, -0.00012065, -197.54072638, -0.00040216, 0.4, 0.3, 0.003, 0.0, 0.0, 14091, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4091, 99999, 'P', 44091, 'Vy', 34091, 'Vz', 24091, 'My', 14091, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4091, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124036, 124036, 24036, 4091, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174036, 3.15, 0.0, 9.8)
    ops.node(124002, 3.15, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4092, 174036, 124002, 0.0625, 31398933.49469465, 13082888.95612277, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24092, 30.96179504, 0.00066496, 37.33080879, 0.01101121, 3.73308088, 0.06832804, -30.96179504, -0.00066496, -37.33080879, -0.01101121, -3.73308088, -0.06832804, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14092, 30.96179504, 0.00066496, 37.33080879, 0.01101121, 3.73308088, 0.06832804, -30.96179504, -0.00066496, -37.33080879, -0.01101121, -3.73308088, -0.06832804, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24092, 4092, 0.0, 80.91120705, 0.01329923, 80.91120705, 0.03989768, 56.63784494, -2712.18685136, 0.05, 2, 0, 74036, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44092, 20.22780176, 4.082e-05, 60.68340529, 0.00012245, 202.27801764, 0.00040818, -20.22780176, -4.082e-05, -60.68340529, -0.00012245, -202.27801764, -0.00040818, 0.4, 0.3, 0.003, 0.0, 0.0, 24092, 2)
    ops.limitCurve('ThreePoint', 14092, 4092, 0.0, 80.91120705, 0.01329923, 80.91120705, 0.03989768, 56.63784494, -2712.18685136, 0.05, 2, 0, 74036, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34092, 20.22780176, 4.082e-05, 60.68340529, 0.00012245, 202.27801764, 0.00040818, -20.22780176, -4.082e-05, -60.68340529, -0.00012245, -202.27801764, -0.00040818, 0.4, 0.3, 0.003, 0.0, 0.0, 14092, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4092, 99999, 'P', 44092, 'Vy', 34092, 'Vz', 24092, 'My', 14092, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174036, 74036, 174036, 4092, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4092, '-orient', 0, 0, 1, 0, 1, 0)
