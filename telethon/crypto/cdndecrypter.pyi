from ..crypto import AESModeCTR as AESModeCTR
from ..errors import CdnFileTamperedError as CdnFileTamperedError
from ..tl.functions.upload import GetCdnFileRequest as GetCdnFileRequest, ReuploadCdnFileRequest as ReuploadCdnFileRequest
from ..tl.types.upload import CdnFile as CdnFile, CdnFileReuploadNeeded as CdnFileReuploadNeeded
from _typeshed import Incomplete

class CdnDecrypter:
    client: Incomplete
    file_token: Incomplete
    cdn_aes: Incomplete
    cdn_file_hashes: Incomplete
    def __init__(self, cdn_client, file_token, cdn_aes, cdn_file_hashes) -> None: ...
    @staticmethod
    async def prepare_decrypter(client, cdn_client, cdn_redirect): ...
    def get_file(self): ...
    @staticmethod
    def check(data, cdn_hash) -> None: ...
