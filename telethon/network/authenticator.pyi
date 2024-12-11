from .. import helpers as helpers
from ..crypto import AES as AES, AuthKey as AuthKey, Factorization as Factorization, rsa as rsa
from ..errors import SecurityError as SecurityError
from ..extensions import BinaryReader as BinaryReader
from ..tl.functions import ReqDHParamsRequest as ReqDHParamsRequest, ReqPqMultiRequest as ReqPqMultiRequest, SetClientDHParamsRequest as SetClientDHParamsRequest
from ..tl.types import ClientDHInnerData as ClientDHInnerData, DhGenFail as DhGenFail, DhGenOk as DhGenOk, DhGenRetry as DhGenRetry, PQInnerData as PQInnerData, ResPQ as ResPQ, ServerDHInnerData as ServerDHInnerData, ServerDHParamsFail as ServerDHParamsFail, ServerDHParamsOk as ServerDHParamsOk

async def do_authentication(sender): ...
def get_int(byte_array, signed: bool = True): ...
