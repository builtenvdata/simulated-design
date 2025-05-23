from .baselib.building import TaxonomyData, BuildingBase
from .eu_cdn.building import Building as EuCDN
from .eu_cdl.building import Building as EuCDL
from .eu_cdm.building import Building as EuCDM
from .eu_cdh.building import Building as EuCDH
from .tr_pre75.building import Building as TrPre75
from .tr_7599.building import Building as Tr7599
from .tr_0018_dch.building import Building as Tr0018DCH
from .tr_0018_dcm.building import Building as Tr0018DCM
from .tr_post18_dch.building import Building as TrPost18DCH
from .tr_post18_dcm.building import Building as TrPost18DCM


class BDIM:
    """
    Factory class to dynamically create a BDIM instance of the corresponding
    design class based on taxonomy data.
    """

    _design_classes = {
        "eu_cdn": EuCDN,
        "eu_cdl": EuCDL,
        "eu_cdm": EuCDM,
        "eu_cdh": EuCDH,
        "tr_pre75": TrPre75,
        "tr_7599": Tr7599,
        "tr_0018_dch": Tr0018DCH,
        "tr_0018_dcm": Tr0018DCM,
        "tr_post18_dch": TrPost18DCH,
        "tr_post18_dcm": TrPost18DCM,
    }
    """Design class mapper."""

    def __new__(cls, taxonomy: TaxonomyData) -> BuildingBase:
        """
        Dynamically creates a BDIM instance based on the design class.

        Parameters
        ----------
        taxonomy : TaxonomyData
            Building taxonomy data.

        Returns
        -------
        BuildingBase
            A BDIM instance of the corresponding design class.

        Raises
        ------
        TypeError
            If taxonomy is not an instance of TaxonomyData.
        ValueError
            If taxonomy.design_class is invalid.
        """
        # Type checking for taxonomy
        if not isinstance(taxonomy, TaxonomyData):
            raise TypeError(
                "Expected taxonomy to be an instance of TaxonomyData"
            )
        # Get appropriate bdim class
        bdim_class = cls._design_classes.get(taxonomy.design_class)
        # Check if the design_class in taxonomy is valid
        if bdim_class is None:
            valid_classes = ", ".join(cls._design_classes.keys())
            raise ValueError(
                f"Invalid design class: {taxonomy.design_class}."
                f"Valid options are: {valid_classes}."
            )
        # Instantiate and return the appropriate class
        return bdim_class(taxonomy)
