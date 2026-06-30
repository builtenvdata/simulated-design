"""BDIM factory module.

This module provides a factory interface for creating Building Design
Information Model (BDIM) objects for a given design class.

The ``BDIM`` class dynamically maps a string-based design class identifier
(e.g., ``"eu_cdh"``) to the corresponding design-class-specific BDIM
implementation and directly instantiates and returns the appropriate
``BuildingBase`` subclass — not a ``BDIM`` instance itself.

All BDIM implementations inherit from ``BuildingBase`` and define
design-class-specific rules and practices.
"""

from .baselib.building import TaxonomyData, BuildingBase
from .eu_cdn import EuCDN
from .eu_cdl import EuCDL
from .eu_cdm import EuCDM
from .eu_cdh import EuCDH
from .tr_7599 import Tr7599
from .tr_0018_dch import Tr0018DCH
from .tr_0018_dcm import Tr0018DCM
from .tr_post18_dch import TrPost18DCH
from .tr_post18_dcm import TrPost18DCM


DCC = {
    "eu_cdn": EuCDN,
    "eu_cdl": EuCDL,
    "eu_cdm": EuCDM,
    "eu_cdh": EuCDH,
    "tr_7599": Tr7599,
    "tr_0018_dch": Tr0018DCH,
    "tr_0018_dcm": Tr0018DCM,
    "tr_post18_dch": TrPost18DCH,
    "tr_post18_dcm": TrPost18DCM
}
"""Registry of available BDIM implementations or design class constructors."""


class BDIM:
    """BDIM factory to generate design-class-specific BDIM instances.

    This class selects the appropriate
    :class:`~simdesign.rcmrf.bdim.baselib.building.BuildingBase`
    subclass from the module-level :data:`DCC` registry based on the
    ``design_class`` field of the input
    :class:`~simdesign.rcmrf.bdim.baselib.building.TaxonomyData`,
    and returns an initialized instance of that subclass directly.

    See Also
    --------
    :class:`EuCDN <simdesign.rcmrf.bdim.eu_cdn.building.Building>`
        Buildings designed without explicit seismic provisions. These typically
        represent structures constructed before the 1960s and designed only for
        gravity loads using allowable stress methods.

    :class:`EuCDL <simdesign.rcmrf.bdim.eu_cdl.building.Building>`
        Buildings designed with early seismic provisions (approximately
        1960s-1970s). Lateral loads are considered, but design is based on
        allowable stress methods and simplified seismic force distributions.

    :class:`EuCDM <simdesign.rcmrf.bdim.eu_cdm.building.Building>`
        Buildings designed according to more modern seismic design codes
        (approximately 1970s-2000s) using limit-state design concepts and
        improved detailing rules to enhance structural ductility.

    :class:`EuCDH <simdesign.rcmrf.bdim.eu_cdh.building.Building>`
        Buildings designed according to contemporary seismic design standards
        (early 2000s-present), implementing capacity design principles and
        reinforcement detailing rules aimed at achieving target ductility
        levels (e.g., Eurocode 8-based design for *moderate ductility
        level, DCM*).

    :class:`Tr7599 <simdesign.rcmrf.bdim.tr_7599.building.Building>`
        Buildings constructed between *1975 and 1999*, designed according to
        *TBEC-1975* and reinforced concrete design provisions in *TS500-1984*.
        This class represents early seismic design practices in Türkiye, often
        associated with relatively low ductility capacity and variable
        construction quality.

    :class:`Tr0018DCM <simdesign.rcmrf.bdim.tr_0018_dcm.building.Building>`
        Buildings constructed between *2000 and 2018* with *moderate
        ductility level (DCM)*. Designs follow provisions from *TBEC-1998*
        (largely retained in TBEC-2007) together with *TS500-2000* reinforced
        concrete design rules. Capacity design principles are generally not
        enforced.

    :class:`Tr0018DCH <simdesign.rcmrf.bdim.tr_0018_dch.building.Building>`
        Buildings constructed between *2000 and 2018* with *high ductility
        level (DCH)*. Designs follow *TBEC-1998 / TBEC-2007* seismic
        provisions and *TS500-2000*, including capacity design principles such
        as the strong-column-weak-beam concept.

    :class:`TrPost18DCM <simdesign.rcmrf.bdim.tr_post18_dcm.building.Building>`
        Buildings constructed *after 2018* with *moderate ductility level
        (DCM)*, designed according to the *TBEC-2018* seismic code and
        *TS500-2000*. These buildings incorporate updated seismic hazard
        definitions and improved detailing rules introduced in the modern code
        framework.

    :class:`TrPost18DCH <simdesign.rcmrf.bdim.tr_post18_dch.building.Building>`
        Buildings constructed *after 2018* with *high ductility level (DCH)*,
        designed according to *TBEC-2018* with full implementation of modern
        capacity design principles and stricter detailing requirements to
        ensure enhanced seismic performance.
    """

    def __new__(cls, taxonomy: TaxonomyData) -> BuildingBase:
        """
        Create a design-class-specific BDIM.

        Parameters
        ----------
        taxonomy : TaxonomyData
            Taxonomy and geometry data describing a single building
            realisation.

        Returns
        -------
        BuildingBase
            An instance of the ``BuildingBase`` subclass corresponding to
            ``taxonomy.design_class`` (e.g. ``EuCDH`` for ``"eu_cdh"``).
            Note that the returned object is *not* a ``BDIM`` instance.

        Raises
        ------
        TypeError
            If ``taxonomy`` is not an instance of ``TaxonomyData``.
        ValueError
            If ``taxonomy.design_class`` is not found in ``DCC``.
        """
        # Type checking for taxonomy
        if not isinstance(taxonomy, TaxonomyData):
            raise TypeError(
                "Expected taxonomy to be an instance of TaxonomyData"
            )
        # Get appropriate bdim class
        bdim_class = DCC.get(taxonomy.design_class)
        # Check if the design_class in taxonomy is valid
        if bdim_class is None:
            valid_classes = ", ".join(DCC.keys())
            raise ValueError(
                f"Invalid design class: {taxonomy.design_class}."
                f"Valid options are: {valid_classes}."
            )
        # Instantiate and return the appropriate class
        return bdim_class(taxonomy)
