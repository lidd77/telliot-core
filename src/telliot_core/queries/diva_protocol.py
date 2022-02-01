import logging
from dataclasses import dataclass

from telliot_core.dtypes.float_type import UnsignedFloatType
from telliot_core.dtypes.value_type import ValueType
from telliot_core.queries.abi_query import AbiQuery

logger = logging.getLogger(__name__)


@dataclass
class divaProtocolPolygon(AbiQuery):
    """Returns the result for a given option ID (a specific prediction market) on the
    Diva Protocol on Polygon.

    Attributes:
        option_id:
            Specifies the requested data a of a valid prediction market that's ready to
            be settled on the Diva Protocol, on the Polygon network.

            More about this query:
            https://github.com/tellor-io/dataSpecs/blob/main/types/DivaProtocolPolygon.md

            More about Diva Protocol:
            https://divaprotocol.io
    """

    optionID: int

    #: ABI used for encoding/decoding parameters
    abi = [{"name": "optionID", "type": "uint256"}]

    @property
    def value_type(self) -> ValueType:
        """Data type returned for a divaProtocolPolygon query.

        - `ufixed256x18`: 256-bit unsigned integer with 18 decimals of precision
        - `packed`: false
        """
        return UnsignedFloatType(abi_type="ufixed256x18", packed=False)
