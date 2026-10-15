"""Constants utilised in BNSM layer such as the geometric transformation
vectors and rigid-like material and section properties.
"""
LINEAR_TRANSF_Z = 99999
"""Geometric transformation tag for beam-column elements along Z (3)."""
VECXZ_Z = [-1, 0, 0]
"""X, Y, and Z components of vecxz for beam-column elements along Z (3)."""
LINEAR_TRANSF_X = 88888
"""Geometric transformation tag for beam-column elements along X (1)."""
VECXZ_X = [0, -1, 0]
"""X, Y, and Z components of vecxz for beam-column elements along X (1)."""
LINEAR_TRANSF_Y = 77777
"""Geometric transformation tag for beam-column elements along Y (2)."""
VECXZ_Y = [1, 0, 0]
"""X, Y, and Z components of vecxz for beam-column elements along Y (2)."""
PDELTA_TRANSF_Z = 66666
"""Geometric transformation tag for beam-column elements along Z (3)."""
RIGID_MAT = 99999
"""Tag of the rigid-like material defined in OpenSees."""
RIGID_SEC = 99999
"""Tag of the rigid-like section defined in OpenSees."""
BIG_VALUE = 1e9
"""A big value used to define stiffness of rigid materials."""
AXIAL_RELEASE_STIFFNESS_RATIO = 1e-3
"""Ratio of the stiffness of the axial beam releases (DP05) to the axial
stiffness of the beam, EA/L. The small stiffness keeps the stiffness matrix
regular when the axial stiffness of a softening beam vanishes, and the beam
is still practically free to elongate."""
GRAV_TS_TAG = 1
"""Tag for time-series which defines the relationship between time-domain
and gravity loads."""
GRAV_P_TAG = 1
"""Tag for load pattern which associates gravity time-series with the
gravity element and point loads."""
NSPA_TS_TAG = 2
"""Tag for time-series which defines the relationship between time-domain
and nspa loads."""
NSPA_P_TAG = 2
"""Tag for load pattern which associates nspa time-series with the
nspa point loads."""
NSPA_EQUILIBRIUM_TOL = 0.01
"""Largest relative difference between the base shear (sum of the support
reactions) and the applied lateral load accepted in a pushover step."""
NSPA_MAX_STIFFNESS_RATIO = 1.5
"""Largest ratio of the tangent stiffness of a pushover step (base shear over
control displacement increment) to the initial stiffness accepted."""
MIN_EIGEN_MODES = 3
"""Minimum number of modes solved for in the eigenvalue analysis. For a
single mode, the default ARPACK solver uses only two Lanczos vectors and may
not converge, in which case OpenSees returns unset eigenvalues without an
error. At least this number of modes is computed, and only the requested
ones are reported."""
MIN_EIGEN_VALUE = 1e-6
"""Smallest valid eigenvalue (rad^2/s^2), i.e., periods up to about 6300 s.
Smaller values are taken as unset eigenvalues of an unconverged solution,
and the next eigen solver is tried."""
