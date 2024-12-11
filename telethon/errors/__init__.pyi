from .rpcbaseerrors import *
from .rpcerrorlist import *
from .common import AlreadyInConversationError as AlreadyInConversationError, AuthKeyNotFound as AuthKeyNotFound, BadMessageError as BadMessageError, CdnFileTamperedError as CdnFileTamperedError, InvalidBufferError as InvalidBufferError, InvalidChecksumError as InvalidChecksumError, MultiError as MultiError, ReadCancelledError as ReadCancelledError, SecurityError as SecurityError, TypeNotFoundError as TypeNotFoundError

def rpc_message_to_error(rpc_error, request): ...
